#!/usr/bin/env python3
"""Signal Engine web layer - zero-dependency server (stdlib only).

Serves the engine over HTTP so ANY machine with python3 can demo:
    python3 serve.py [--port 8000] [--seed]

Endpoints (Supabase-shape JSON, swap for FastAPI/api.py at nationals):
    GET  /                     → static UI (index.html)
    GET  /api/feed             → ranked feed
    GET  /api/digest           → today in 60 seconds
    GET  /api/search?q=...     → ranked semantic-ish search
    GET  /api/complaints       → complaint board
    POST /api/complaints       → add complaint  {"title","body","category"}
    GET  /api/stats            → channel counts, deadlines found

Craft N Code 2026 shared scaffold (IDEA-BANK §6). Team 511.
"""
from __future__ import annotations

import json
import mimetypes
import re
import sqlite3
import sys
import urllib.parse
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Optional

HERE = Path(__file__).parent
STATIC = HERE / "static"
DB = HERE.parent / "engine" / "signal.db"

sys.path.insert(0, str(HERE.parent / "engine"))
import engine as E  # noqa: E402

FEED_CACHE: Optional[dict] = None


def load_feed(profile: Optional[list] = None) -> dict:
    global FEED_CACHE
    profile = profile or ["general"]
    if FEED_CACHE is not None:
        return FEED_CACHE
    if DB.exists():
        conn = sqlite3.connect(DB)
        rows = conn.execute(
            "SELECT channel, source_id, sender, subject, body, received_at, summary, "
            "rank_score, deadline_iso, is_urgent, kind FROM items").fetchall()
        conn.close()
        items = []
        for r in rows:
            items.append(E.Item(channel=r[0], source_id=r[1], sender=r[2], subject=r[3],
                                body=r[4], received_at=r[5], summary=r[6], rank_score=r[7],
                                deadline_iso=r[8], is_urgent=bool(r[9]), kind=r[10]))
        if items:
            FEED_CACHE = {"generated_at": "from-db", "today": "", "llm": {"model": "db"},
                          "profile": profile, "total": len(items),
                          "items": [i.as_dict() for i in items]}
            return FEED_CACHE
    # no db → run the engine fresh
    FEED_CACHE = E.run_pipeline(E.seed_items(), profile)
    return FEED_CACHE


def search(items: list[dict], q: str, top: int = 5) -> list[dict]:
    terms = [t for t in re.findall(r"[a-z0-9]{2,}", q.lower())]
    if not terms:
        return []
    scored = []
    for it in items:
        hay = " ".join([it["subject"], it["body"], it["summary"], it["sender"]]).lower()
        s = sum(hay.count(t) * (2 if t in it["subject"].lower() else 1) for t in terms)
        if s > 0:
            scored.append((s, it))
    scored.sort(key=lambda x: -x[0])
    return [it for _, it in scored[:top]]


def route(handler: BaseHTTPRequestHandler, path: str, method: str, body: Optional[dict]):
    query = urllib.parse.parse_qs(urllib.parse.urlparse(path).query)
    path = path.split("?")[0]  # strip query string before segment split
    parts = [p for p in path.split("/") if p]

    if not parts or parts[0] == "index.html":
        f = STATIC / "index.html"
        handler.send_response(200)
        handler.send_header("Content-Type", "text/html; charset=utf-8")
        handler.end_headers()
        handler.wfile.write(f.read_bytes())
        return

    if parts[0] == "static":
        f = STATIC / parts[1]
        if f.exists():
            handler.send_response(200)
            handler.send_header("Content-Type", mimetypes.guess_type(str(f))[0] or "text/plain")
            handler.end_headers()
            handler.wfile.write(f.read_bytes())
        else:
            handler.send_response(404)
            handler.end_headers()
        return

    if parts[0] == "api":
        feed = load_feed()

        if parts[1] == "feed":
            return json_reply(handler, feed)

        if parts[1] == "digest":
            urgent = [i for i in feed["items"] if i.get("is_urgent")][:3]
            return json_reply(handler, {"urgent": urgent, "top": feed["items"][:5],
                                        "today": feed.get("today")})

        if parts[1] == "search":
            q = query.get("q", [""])[0]
            return json_reply(handler, {"query": q, "results": search(feed["items"], q)})

        if parts[1] == "complaints":
            if method == "POST" and body:
                complaints = [i for i in feed["items"] if i["kind"] == "complaint"]
                new = {
                    "channel": "ticket", "source_id": f"tkt{len(complaints)+4}",
                    "sender": body.get("sender", "User"), "subject": body.get("title", "New request"),
                    "body": body.get("body", ""), "received_at": "",
                    "summary": body.get("title", ""), "rank_score": 0,
                    "deadline_iso": None, "is_urgent": False,
                    "kind": "complaint",
                    "status": "open", "sla_hours": 48,
                    "category": body.get("category", "general"),
                }
                return json_reply(handler, {"ok": True, "ticket": f"#C-{len(complaints)+114}", "item": new}, 201)
            complaints = [i for i in feed["items"] if i["kind"] == "complaint"]
            return json_reply(handler, {"complaints": complaints})

        if parts[1] == "stats":
            counts = Counter(i["channel"] for i in feed["items"])
            deadlines = [i for i in feed["items"] if i.get("deadline_iso")]
            return json_reply(handler, {
                "total": feed["total"], "channels": dict(counts),
                "deadlines_found": len(deadlines),
                "llm": feed["llm"], "skin_ready": True,
            })

    handler.send_response(404)
    handler.end_headers()


def json_reply(handler: BaseHTTPRequestHandler, obj, code: int = 200):
    data = json.dumps(obj).encode()
    handler.send_response(code)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _serve(self, method: str):
        parsed = urllib.parse.urlparse(self.path)
        body = None
        if method == "POST":
            length = int(self.headers.get("Content-Length") or 0)
            if length:
                try:
                    body = json.loads(self.rfile.read(length).decode())
                except Exception:
                    body = None
        route(self, self.path, method, body)

    def do_GET(self):
        self._serve("GET")

    def do_POST(self):
        self._serve("POST")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    print(f"[serve] http://localhost:{args.port}  (ctrl-c to stop)")
    ThreadingHTTPServer(("0.0.0.0", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
