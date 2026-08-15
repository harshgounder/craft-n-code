#!/usr/bin/env python3
"""Acceptance tests H1-H6 from BUILD-SPEC-3 Part 1 (badge honesty fix).

Plain python3, zero external deps. Starts the real server on an ephemeral
port and verifies /api/stats mode tells the truth on failure: null provider,
no key, cached DB, fixture, offline flag, and (when a real key is present)
live mode with zero provider errors.
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
DB = ROOT / "engine" / "signal.db"
CACHE = ROOT / "engine" / ".llm_cache.json"

PORT = 8126
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
    env = dict(os.environ)
    env.pop("OLLAMA_API_KEY", None)

    with tempfile.TemporaryDirectory() as td:
        errfile = Path(td) / "server.err"

        # ── H1 null provider, fresh DB, no fixture -> offline, provider_errors >= 1 ──
        null_env = dict(env)
        null_env["SIGNAL_PROVIDER"] = "null"
        null_env["OLLAMA_API_KEY"] = "some-key"
        s = start_server(["--port", str(PORT)], null_env, errfile)
        wait_ready(s, errfile)
        try:
            stats = jget("/api/stats")
            llm = jget("/api/feed")["llm"]
            check("H1 null provider -> mode offline (not live)",
                  stats.get("mode") == "offline", stats.get("mode"))
            check("H1 llm.provider_errors >= 1",
                  llm.get("provider_errors", 0) >= 1, str(llm.get("provider_errors")))
        finally:
            stop(s)
        time.sleep(0.3)

        # ── H2 no key (empty) -> mode offline, model OFFLINE ──
        fresh_db()
        no_key_env = dict(env)
        no_key_env["OLLAMA_API_KEY"] = ""
        s = start_server(["--port", str(PORT)], no_key_env, errfile)
        wait_ready(s, errfile)
        try:
            stats = jget("/api/stats")
            llm = jget("/api/feed")["llm"]
            check("H2 no key -> mode offline", stats.get("mode") == "offline",
                  stats.get("mode"))
            check("H2 llm.model == OFFLINE", llm.get("model") == "OFFLINE",
                  str(llm.get("model")))
        finally:
            stop(s)
        time.sleep(0.3)

        # ── H3 seeded DB row -> mode cached ──
        fresh_db()
        db_env = dict(env)
        db_dir = ROOT / "engine"
        subprocess.run([sys.executable, str(db_dir / "engine.py"), "--seed"],
                       capture_output=True, env=db_env, cwd=str(db_dir))
        s = start_server(["--port", str(PORT)], db_env, errfile)
        wait_ready(s, errfile)
        try:
            stats = jget("/api/stats")
            check("H3 seeded DB -> mode cached", stats.get("mode") == "cached",
                  stats.get("mode"))
        finally:
            stop(s)
        time.sleep(0.3)

        # ── H4 --fixture happy -> mode fixture ──
        fresh_db()
        s = start_server(["--port", str(PORT), "--fixture", "happy"], env, errfile)
        wait_ready(s, errfile)
        try:
            stats = jget("/api/stats")
            check("H4 --fixture -> mode fixture", stats.get("mode") == "fixture",
                  stats.get("mode"))
        finally:
            stop(s)
        time.sleep(0.3)

        # ── H5 --offline flag -> mode offline ──
        fresh_db()
        off_env = dict(env)
        off_env["OLLAMA_API_KEY"] = "test-key-should-be-ignored"
        s = start_server(["--port", str(PORT), "--offline"], off_env, errfile)
        wait_ready(s, errfile)
        try:
            stats = jget("/api/stats")
            check("H5 --offline -> mode offline", stats.get("mode") == "offline",
                  stats.get("mode"))
        finally:
            stop(s)
        time.sleep(0.3)

        # ── H6 valid key present -> mode live, provider_errors == 0 ──
        real_key = os.environ.get("OLLAMA_API_KEY", "")
        if real_key:
            fresh_db()
            live_env = dict(env)
            live_env["OLLAMA_API_KEY"] = real_key
            s = start_server(["--port", str(PORT)], live_env, errfile)
            wait_ready(s, errfile)
            try:
                stats = jget("/api/stats")
                llm = jget("/api/feed")["llm"]
                check("H6 valid key -> mode live", stats.get("mode") == "live",
                      stats.get("mode"))
                check("H6 llm.provider_errors == 0",
                      llm.get("provider_errors", -1) == 0, str(llm.get("provider_errors")))
            finally:
                stop(s)
        else:
            check("H6 valid key present (skipped, no OLLAMA_API_KEY)", True,
                  "skipped: env key absent")

    failed = [n for n, ok, _ in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    if failed:
        print("FAILED:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
