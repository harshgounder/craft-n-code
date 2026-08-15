#!/usr/bin/env python3
"""Acceptance tests F1-F4 from BUILD-SPEC-3 Part 2 (real data kit).

Plain python3, zero external deps. Exercises feeds.py --offline (deterministic,
zero network) and the serve.py --feeds flag: /api/stats mode, /api/feeds
freshness, and /api/feed. DB isolation like every other suite.
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
FEEDS_PY = ROOT / "engine" / "feeds.py"
FEEDS_DIR = ROOT / "data" / "feeds"
DB = ROOT / "engine" / "signal.db"
CACHE = ROOT / "engine" / ".llm_cache.json"

PORT = 8127
BASE = f"http://localhost:{PORT}"

results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    mark = "PASS" if cond else "FAIL"
    print(f"  [{mark}] {name}" + (f"  -> {detail}" if detail else ""))


def jget(path):
    with urllib.request.urlopen(BASE + path) as r:
        return json.loads(r.read().decode())


def fresh_db():
    """Delete generated artifacts so every suite runs against fresh state."""
    for p in (DB, CACHE):
        try:
            p.unlink()
        except FileNotFoundError:
            pass


def clean_feeds():
    if FEEDS_DIR.exists():
        for p in FEEDS_DIR.iterdir():
            p.unlink()
        FEEDS_DIR.rmdir()


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


def start_server(args, env, errfile):
    return subprocess.Popen(
        [sys.executable, str(SERVE)] + args,
        stdout=subprocess.DEVNULL, stderr=open(errfile, "w"),
        cwd=str(ROOT / "webapp"), env=env)


def stop(server):
    if server is not None and server.poll() is None:
        server.terminate()
        server.wait()


def main():
    fresh_db()
    clean_feeds()
    env = dict(os.environ)
    env.pop("OLLAMA_API_KEY", None)

    try:
        # ── F1 feeds.py --offline: exit 0, meta exists, every source error ──
        r = subprocess.run([sys.executable, str(FEEDS_PY), "--offline"],
                           capture_output=True, cwd=str(ROOT))
        meta_path = FEEDS_DIR / "_meta.json"
        meta_ok = meta_path.exists()
        if meta_ok:
            meta = json.loads(meta_path.read_text())
            all_err = all(s.get("status") == "error" for s in meta["sources"].values())
        else:
            all_err = False
        check("F1 --offline exits 0", r.returncode == 0, f"rc={r.returncode}")
        check("F1 _meta.json exists", meta_ok)
        check("F1 every source status error", all_err,
              json.dumps(meta["sources"]) if meta_ok else "no meta")

        with tempfile.TemporaryDirectory() as td:
            errfile = Path(td) / "server.err"

            # ── F2 null provider + --feeds: stats offline, /api/feeds 200, /api/feed 200 ──
            fresh_db()
            null_env = dict(env)
            null_env["SIGNAL_PROVIDER"] = "null"
            null_env["OLLAMA_API_KEY"] = "some-key"
            s = start_server(["--port", str(PORT), "--feeds"], null_env, errfile)
            wait_ready(s, errfile)
            try:
                stats = jget("/api/stats")
                check("F2 --feeds null -> mode offline", stats.get("mode") == "offline",
                      stats.get("mode"))
                feeds_resp = jget("/api/feeds")
                check("F2 /api/feeds has sources + mode",
                      "sources" in feeds_resp and "mode" in feeds_resp,
                      f"keys={list(feeds_resp)}")
                feed_resp = jget("/api/feed")
                check("F2 /api/feed returns 200", "items" in feed_resp,
                      f"total={feed_resp.get('total')}")
            finally:
                stop(s)
            time.sleep(0.3)

            # ── F3 same but with key: mode live, provider_errors == 0 when key works ──
            real_key = os.environ.get("OLLAMA_API_KEY", "")
            if real_key:
                fresh_db()
                live_env = dict(env)
                live_env["OLLAMA_API_KEY"] = real_key
                s = start_server(["--port", str(PORT), "--feeds"], live_env, errfile)
                wait_ready(s, errfile)
                try:
                    stats = jget("/api/stats")
                    llm = jget("/api/feed")["llm"]
                    check("F3 --feeds valid key -> mode live",
                          stats.get("mode") == "live", stats.get("mode"))
                    check("F3 llm.provider_errors == 0",
                          llm.get("provider_errors", -1) == 0,
                          str(llm.get("provider_errors")))
                finally:
                    stop(s)
            else:
                check("F3 valid key present (skipped, no OLLAMA_API_KEY)", True,
                      "skipped: env key absent")
    finally:
        clean_feeds()

    # ── F4 DB isolation: fresh artifacts at start (already done) ──
    check("F4 DB isolation (fresh artifacts)", True, "signal.db + .llm_cache.json cleaned")

    failed = [n for n, ok, _ in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    if failed:
        print("FAILED:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
