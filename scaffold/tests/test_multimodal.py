#!/usr/bin/env python3
"""Acceptance tests M1-M4 from BUILD-SPEC-2 item B (multimodal ingest).

Plain python3, zero external deps. Starts the real server on an ephemeral
port, POSTs to /api/ingest with local attachment paths, and verifies the item
lands in the feed and the trace shows the ingest:multimodal step.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
SERVE = ROOT / "webapp" / "serve.py"
FIXTURES = ROOT / "fixtures"
ATTACH = FIXTURES / "attachments"
DB = ROOT / "engine" / "signal.db"
CACHE = ROOT / "engine" / ".llm_cache.json"

PORT = 8125
BASE = f"http://localhost:{PORT}"

results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    mark = "PASS" if cond else "FAIL"
    print(f"  [{mark}] {name}" + (f"  -> {detail}" if detail else ""))


def jget(path):
    with urllib.request.urlopen(BASE + path) as r:
        return json.loads(r.read().decode())


def jpost(path, payload):
    req = urllib.request.Request(
        BASE + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as r:
        return r.status, json.loads(r.read().decode())


def fresh_db():
    """Delete generated artifacts so every suite runs against fresh state."""
    for p in (DB, CACHE):
        try:
            p.unlink()
        except FileNotFoundError:
            pass


def wait_ready(server, errfile):
    """Poll GET /api/stats until HTTP 200, up to 30s. Fail if server exits."""
    deadline = time.time() + 30
    while time.time() < deadline:
        if server.poll() is not None:
            err = ""
            try:
                err = Path(errfile).read_text()
            except Exception:
                pass
            raise RuntimeError(f"server exited during wait_ready (rc={server.returncode}): {err}")
        try:
            with urllib.request.urlopen(BASE + "/api/stats", timeout=2) as r:
                if r.status == 200:
                    return
        except (urllib.error.URLError, OSError):
            pass
        time.sleep(0.25)
    raise RuntimeError("server did not become ready within 30s")


def main():
    fresh_db()
    env = dict(os.environ)
    env.pop("OLLAMA_API_KEY", None)

    with tempfile.TemporaryDirectory() as td:
        errfile = Path(td) / "server.err"
        server = subprocess.Popen(
            [sys.executable, str(SERVE), "--port", str(PORT)],
            stdout=subprocess.DEVNULL, stderr=open(errfile, "w"),
            cwd=str(ROOT / "webapp"), env=env)
        wait_ready(server, errfile)
        try:
            # ── M1 text attachment extracts and lands in /api/feed ──
            st, res = jpost("/api/ingest", {
                "channel": "email", "source_id": "mm-1",
                "sender": "Registrar Office", "subject": "Exam schedule attachment",
                "body": "Please find the exam schedule attached.",
                "attachment_path": str(ATTACH / "schedule.txt"),
            })
            feed = jget("/api/feed")
            ids = [i["source_id"] for i in feed["items"]]
            m1 = (res.get("ok") and res["extraction"]["extractor"] == "builtin"
                  and "mm-1" in ids)
            check("M1 text attachment extracts + item in feed", m1,
                  f"extractor={res.get('extraction', {}).get('extractor')}")

            # ── M2 unsupported type -> extraction None with reason, still 200 ──
            st, res = jpost("/api/ingest", {
                "channel": "email", "source_id": "mm-2",
                "sender": "Unknown Sender", "subject": "Suspicious file",
                "body": "Open this file for a surprise.",
                "attachment_path": str(ATTACH / "weird.exe"),
            })
            feed = jget("/api/feed")
            ids = [i["source_id"] for i in feed["items"]]
            m2 = (st == 200 and res.get("ok")
                  and res["extraction"]["extractor"] is None
                  and res["extraction"]["reason"] == "no extractor for this type"
                  and "mm-2" in ids)
            check("M2 unsupported type -> None + reason, still 200", m2,
                  f"reason={res.get('extraction', {}).get('reason')}")

            # ── M3 /api/trace shows ingest:multimodal step with meta ──
            tr = jget("/api/trace")["steps"]
            mm_steps = [t for t in tr if t["step"] == "ingest:multimodal"]
            m3 = (len(mm_steps) >= 2
                  and all("extraction" in t for t in mm_steps)
                  and any(t.get("source_id") == "mm-1" for t in mm_steps))
            check("M3 trace shows ingest:multimodal with meta", m3,
                  f"{len(mm_steps)} steps")

            # ── M4 no attachment -> body-only item, no extraction entry ──
            st, res = jpost("/api/ingest", {
                "channel": "chat", "source_id": "mm-3",
                "sender": "Student Group", "subject": "No attachment here",
                "body": "Just a plain text message with no file.",
            })
            feed = jget("/api/feed")
            ids = [i["source_id"] for i in feed["items"]]
            m4 = (res.get("ok") and res["extraction"] is None and "mm-3" in ids)
            check("M4 no attachment -> body-only, no extraction", m4,
                  f"extraction={res.get('extraction')}")
        finally:
            if server.poll() is None:
                server.terminate(); server.wait()

    failed = [n for n, ok, _ in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    if failed:
        print("FAILED:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
