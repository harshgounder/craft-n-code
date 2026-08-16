#!/usr/bin/env python3
"""Signal Engine web layer - zero-dependency server (stdlib only).

Serves the engine over HTTP so ANY machine with python3 can demo:
    python3 serve.py [--port 8000] [--seed] [--host 127.0.0.1] [--auth TOKEN]

Endpoints (Supabase-shape JSON, swap for FastAPI/api.py at nationals):
    GET  /                     → static UI (index.html)
    GET  /health               → health probe (always public)
    GET  /api/feed             → ranked feed
    GET  /api/digest           → today in 60 seconds
    GET  /api/search?q=...     → ranked semantic-ish search
    GET  /api/complaints       → complaint board
    POST /api/complaints       → add complaint  {"title","body","category"}
    GET  /api/stats            → channel counts, deadlines found

Auth gate (--auth TOKEN): every POST /api/* plus GET /api/stats and
GET /api/audit require the token via ?token= or an Authorization:
Bearer header; mismatch -> 401. GET feed/digest/search/complaints and
/health stay public. Without --auth the server behaves exactly as before.

Craft N Code 2026 shared scaffold (IDEA-BANK §6). Team 511.
"""
from __future__ import annotations

import json
import mimetypes
import re
import sys
import threading
import time
import urllib.parse
from collections import Counter
from hmac import compare_digest
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Optional

HERE = Path(__file__).parent
STATIC = HERE / "static"
DB = HERE.parent / "engine" / "signal.db"
FIXTURES = HERE.parent / "fixtures"

sys.path.insert(0, str(HERE.parent / "engine"))
import engine as E  # noqa: E402
import approval as A  # noqa: E402
import multimodal as M  # noqa: E402
import feeds  # noqa: E402
import providers as P  # noqa: E402
import storage as S  # noqa: E402

FEED_CACHE: Optional[dict] = None
FIXTURE: Optional[str] = None    # fixture name from --fixture NAME
OFFLINE: bool = False            # forced offline from --offline
FEEDS: bool = False              # real data kit from --feeds
FEEDS_DIR = HERE.parent / "data" / "feeds"
AUTH_TOKEN: Optional[str] = None  # token gate from --auth; None = no gate

# SSE event queue (BUILD-SPEC B4): thread-safe list + condition, stdlib only.
# Each event carries a monotonic seq; the queue keeps the last 50 so a
# reconnecting client with since=<old> can still catch up on missed events.
SSE_MAX_CLIENTS = 8          # connection cap: drop oldest when exceeded
SSE_KEEPALIVE = 15.0         # idle flush interval for ": keepalive" comments
SSE_HISTORY = 50             # events kept for replay

_sse_cond = threading.Condition()
_sse_seq = 0
_sse_events: list[dict] = []   # [{"seq": int, "type": str, "data": dict}]
_sse_clients: list = []        # [_SSEClient, ...] open connections


class _SSEClient:
    """One open SSE connection; closed Event flags a drop by the cap."""

    def __init__(self):
        self.closed = threading.Event()


def _push_event(event_type: str, data: dict) -> None:
    """Record a change and wake every connected SSE client."""
    global _sse_seq
    with _sse_cond:
        _sse_seq += 1
        _sse_events.append({"seq": _sse_seq, "type": event_type, "data": data})
        del _sse_events[:-SSE_HISTORY]
        _sse_cond.notify_all()


def load_fixture(name: str) -> list[E.Item]:
    """Load a golden fixture feed (scaffold/fixtures/{name}.json) as Items."""
    path = FIXTURES / f"{name}.json"
    rows = json.loads(path.read_text())
    return [E.Item(
        channel=r.get("channel", "email"),
        source_id=r["source_id"],
        sender=r.get("sender", ""),
        subject=r.get("subject", ""),
        body=r.get("body", ""),
        received_at=r.get("received_at", ""),
        profile_tags=r.get("profile_tags", []),
        kind=r.get("kind", "notice"),
    ) for r in rows]


def _persist_feed_cache() -> None:
    """Write the computed feed into the storage feed_cache table. Best effort:
    a failure must never take the demo down (BUILD-SPEC B9)."""
    try:
        S.get_storage(DB).upsert_feed(FEED_CACHE)
    except Exception:
        pass


def load_feed(profile: Optional[list] = None) -> dict:
    global FEED_CACHE
    profile = profile or ["general"]
    if FEED_CACHE is not None:
        return FEED_CACHE
    # fixture mode loads a golden feed instead of the DB / seed
    if FIXTURE:
        items = load_fixture(FIXTURE)
        FEED_CACHE = E.run_pipeline(items, profile)
        _persist_feed_cache()
        return FEED_CACHE
    # real data kit: live feeds through the real pipeline
    if FEEDS:
        feed_items, meta = feeds.load_feeds(FEEDS_DIR)
        if feed_items:
            FEED_CACHE = E.run_pipeline(feed_items, profile)
            FEED_CACHE["feeds_meta"] = meta
            _persist_feed_cache()
            return FEED_CACHE
    # cached feed lives behind the storage layer (SQLite by default)
    rows = S.get_storage(DB).list_items()
    items = []
    for r in rows:
        items.append(E.Item(channel=r.get("channel", ""), source_id=r.get("source_id", ""),
                            sender=r.get("sender", ""), subject=r.get("subject", ""),
                            body=r.get("body", ""), received_at=r.get("received_at", ""),
                            summary=r.get("summary", ""), rank_score=r.get("rank_score", 0.0),
                            deadline_iso=r.get("deadline_iso"),
                            is_urgent=bool(r.get("is_urgent", False)),
                            kind=r.get("kind", "notice")))
    if items:
        FEED_CACHE = {"generated_at": "from-db", "today": "", "llm": {"model": "db"},
                      "profile": profile, "total": len(items),
                      "items": [i.as_dict() for i in items]}
        _persist_feed_cache()
        return FEED_CACHE
    # no db → run the engine fresh
    FEED_CACHE = E.run_pipeline(E.seed_items(), profile)
    _persist_feed_cache()
    return FEED_CACHE


def current_mode() -> str:
    """Derive the demo mode badge from ACTUAL provider outcomes (BUILD-SPEC B2):
    offline | fixture | cached | live | degraded. The badge is honest: it can
    only say live when a recent provider call actually succeeded, and real
    failures surface as degraded instead of hiding behind intent flags."""
    if OFFLINE:
        return "offline"
    if FIXTURE:
        return "fixture"
    stats = P.get_stats()
    # Provider explicitly disabled (SIGNAL_PROVIDER=null) -> offline.
    if stats["errors"].get("disabled", 0) > 0:
        return "offline"
    feed = load_feed()
    llm = feed.get("llm") or {}
    has_cache = llm.get("cache_hits", 0) > 0 or llm.get("model") == "db"
    # No provider call was ever attempted and a cache exists -> cached.
    if stats["attempts"] == 0 and has_cache:
        return "cached"
    # Live only when every attempt within this run succeeded, or the last
    # recorded outcome was a success that is newer than the last failure.
    recovered = (stats["ok"] > 0 and stats["last_ok_at"] and stats["last_error_at"]
                 and stats["last_ok_at"] >= stats["last_error_at"])
    if stats["ok"] > 0 and (stats["attempts"] - stats["ok"] == 0 or recovered):
        return "live"
    # Any recorded provider error -> degraded (error counts surface in /api/stats).
    if sum(stats["errors"].values()) > 0:
        return "degraded"
    if llm.get("model") == "OFFLINE":
        return "offline"
    if llm.get("model") == "db":
        return "cached"
    return "offline"


def feeds_status() -> dict:
    """Data freshness for the real data kit, separate from the LLM mode badge.
    live if any source ok and fetched within 30 minutes, cached if files exist
    but stale or all errored, offline if no files."""
    meta_path = FEEDS_DIR / "_meta.json"
    if not meta_path.exists():
        return {"sources": [], "mode": "offline"}
    try:
        meta = json.loads(meta_path.read_text())
    except Exception:
        return {"sources": [], "mode": "offline"}
    sources = meta.get("sources", {})
    fetched_at = meta.get("fetched_at", "")
    fresh = False
    try:
        fetched = datetime.fromisoformat(fetched_at)
        fresh = (datetime.now(timezone.utc) - fetched).total_seconds() < 1800
    except Exception:
        fresh = False
    any_ok = any(s.get("status") == "ok" for s in sources.values())
    if any_ok and fresh:
        mode = "live"
    elif sources:
        mode = "cached"
    else:
        mode = "offline"
    return {"sources": list(sources.values()), "mode": mode}


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


def propose_for_item(item_id: str, tool: str, params: dict) -> dict:
    """Turn a feed item + tool into a Proposal. Evidence from the item body."""
    feed = load_feed()
    item = next((i for i in feed["items"] if i.get("source_id") == item_id), None)
    if item is None:
        return {"ok": False, "error": "item not found"}
    if tool not in A.TOOL_REGISTRY:
        return {"ok": False, "error": "unknown tool"}
    t = A.TOOL_REGISTRY[tool]
    evidence = [{"source_id": item.get("source_id"),
                 "snippet": (item.get("summary") or item.get("subject") or "")[:160]}]
    reason = (f"{t.description} for '{item.get('subject')}'. "
              f"Triggered by a {item.get('kind')} item from {item.get('sender')}.")
    confidence = max(0.0, min(1.0, (item.get("rank_score") or 0.0) / 10.0))
    prop = A.propose(tool, params, reason, evidence, round(confidence, 3))
    return {"ok": True, "proposal": prop.as_dict()}


def ingest_multimodal(body: dict) -> dict:
    """POST /api/ingest: accept a message with an optional local attachment.

    Runs extract_text, builds an Item, appends it to the feed cache, re-runs
    the pipeline, and pushes an ingest:multimodal trace step with the meta.
    Returns 200 even when extraction is None (graceful).
    """
    global FEED_CACHE
    attachment_path = body.get("attachment_path") or ""
    text, meta = M.extract_text(attachment_path) if attachment_path else (None, None)

    item_body = body.get("body", "")
    if text:
        item_body = (item_body + "\n" + text).strip() if item_body else text

    item = E.Item(
        channel=body.get("channel", "email"),
        source_id=body.get("source_id") or f"ingest-{int(time.time() * 1000)}",
        sender=body.get("sender", ""),
        subject=body.get("subject", ""),
        body=item_body,
        received_at=body.get("received_at", ""),
        profile_tags=body.get("profile_tags", []),
        kind=body.get("kind", "notice"),
    )

    feed = load_feed()
    items = [E.Item(**{k: v for k, v in i.items() if k in E.Item.__dataclass_fields__})
             for i in feed["items"]]
    items.append(item)
    result = E.run_pipeline(items, feed.get("profile") or ["general"])
    FEED_CACHE = result

    pos = next((i for i, it in enumerate(result["items"])
                if it.get("source_id") == item.source_id), None)
    if pos is not None:
        _push_event("item_new", {"id": item.source_id, "rank": pos})

    trace_meta = meta if meta is not None else {}
    E.push_trace({"step": "ingest:multimodal", "source_id": item.source_id,
                  "extraction": trace_meta})

    return {"ok": True, "item": item.as_dict(), "extraction": meta}


def _gate_routes(parts: list, method: str) -> bool:
    """Which /api/* routes require the token when --auth is set.

    Every POST /api/* plus GET /api/stats and GET /api/audit are gated;
    everything else on the demo screen (feed/digest/search/complaints)
    stays public. Returns True when the route needs a token.
    """
    if not parts or parts[0] != "api" or len(parts) < 2:
        return False
    if method == "POST":
        return True
    if method == "GET" and parts[1] in ("stats", "audit"):
        return True
    return False


def _request_token(handler: BaseHTTPRequestHandler, query: dict) -> str:
    """Extract the presented token from ?token= or Authorization: Bearer."""
    if query.get("token"):
        return query["token"][0]
    auth = handler.headers.get("Authorization", "")
    if auth.lower().startswith("bearer "):
        return auth[7:].strip()
    return ""


def _authorized(handler: BaseHTTPRequestHandler, query: dict, parts: list, method: str) -> bool:
    """Auth gate. With --auth set, gated routes need a matching token."""
    if AUTH_TOKEN is None:
        return True
    if not _gate_routes(parts, method):
        return True
    presented = _request_token(handler, query)
    return bool(presented) and compare_digest(presented, AUTH_TOKEN)


def route(handler: BaseHTTPRequestHandler, path: str, method: str, body: Optional[dict]):
    query = urllib.parse.parse_qs(urllib.parse.urlparse(path).query)
    path = path.split("?")[0]  # strip query string before segment split
    parts = [p for p in path.split("/") if p]

    if not parts or parts[0] == "index.html":
        f = STATIC / "krishi.html"
        if not f.exists():
            f = STATIC / "index.html"
        handler.send_response(200)
        handler.send_header("Content-Type", "text/html; charset=utf-8")
        handler.end_headers()
        handler.wfile.write(f.read_bytes())
        return

    if parts[0] in ("manifest.json", "sw.js"):
        # PWA install files served at the root (BUILD-SPEC B11)
        f = STATIC / parts[0]
        ctype = ("application/manifest+json" if parts[0] == "manifest.json"
                 else "application/javascript")
        handler.send_response(200)
        handler.send_header("Content-Type", ctype)
        handler.end_headers()
        handler.wfile.write(f.read_bytes())
        return

    if parts[0] == "static":
        # reject traversal: no "..", ".", or empty segments allowed
        if any(seg in ("..", ".", "") for seg in parts[1:]):
            handler.send_response(404)
            handler.end_headers()
            return
        f = (STATIC / Path(*parts[1:])).resolve()
        if not str(f).startswith(str(STATIC.resolve())) or not f.is_file():
            handler.send_response(404)
            handler.end_headers()
            return
        handler.send_response(200)
        handler.send_header("Content-Type", mimetypes.guess_type(str(f))[0] or "text/plain")
        handler.end_headers()
        handler.wfile.write(f.read_bytes())
        return

    if parts[0] == "health":
        return json_reply(handler, {"status": "ok", "auth": AUTH_TOKEN is not None})

    if parts[0] == "api":
        if not _authorized(handler, query, parts, method):
            return json_reply(handler, {"error": "unauthorized"}, 401)

        if parts[1] == "events":
            return _sse_stream(handler, query)

        feed = load_feed()

        if parts[1] == "feed":
            return json_reply(handler, feed)

        if parts[1] == "feeds":
            return json_reply(handler, feeds_status())

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
            stats = {
                "total": feed["total"], "channels": dict(counts),
                "deadlines_found": len(deadlines),
                "llm": feed["llm"], "skin_ready": True,
                "mode": current_mode(),
                "provider": P.get_stats(),
            }
            if P.is_injecting():
                stats["injected"] = True
            if FEEDS:
                stats["feeds"] = feed.get("feeds_meta")
            return json_reply(handler, stats)

        if parts[1] == "trace":
            return json_reply(handler, {"steps": E.get_trace()})

        if parts[1] == "ingest":
            if method == "POST" and body:
                return json_reply(handler, ingest_multimodal(body), 200)
            return json_reply(handler, {"ok": False, "error": "POST only"}, 405)

        if parts[1] == "tools":
            return json_reply(handler, {
                "tools": [
                    {"name": t.name, "description": t.description,
                     "side_effect": t.side_effect, "params": t.params}
                    for t in A.TOOL_REGISTRY.values()
                ]
            })

        if parts[1] == "proposals":
            if method == "POST" and body:
                item_id = body.get("item_id")
                tool = body.get("tool")
                params = body.get("params") or {}
                res = propose_for_item(item_id, tool, params)
                if res.get("ok"):
                    _push_event("proposal_new",
                                {"id": res["proposal"]["id"], "tool": res["proposal"]["tool"]})
                return json_reply(handler, res, 201 if res.get("ok") else 404)
            proposals = A.list_proposals()
            return json_reply(handler, {"proposals": [p.as_dict() for p in proposals]})

        if parts[1] == "approve":
            if method == "POST" and body:
                pid = body.get("proposal_id")
                decision = body.get("decision")
                actor = body.get("actor") or "user"
                if decision not in ("approve", "reject", "snooze"):
                    return json_reply(handler, {"ok": False, "error": "bad decision"}, 400)
                prop = A.decide(pid, decision, actor)
                if prop is None:
                    return json_reply(handler, {"ok": False, "error": "proposal not found"}, 404)
                _push_event("proposal_decided",
                            {"id": prop.id, "decision": decision, "actor": actor})
                _push_event("audit_new", {
                    "ts": prop.decided_at, "actor": actor, "decision": decision,
                    "proposal_id": prop.id, "tool": prop.tool,
                    "params": prop.params, "evidence": prop.evidence,
                    "reason": prop.reason})
                return json_reply(handler, {"ok": True, "proposal": prop.as_dict()})
            return json_reply(handler, {"ok": False, "error": "POST only"}, 405)

        if parts[1] == "audit":
            return json_reply(handler, {"events": A.list_audit()})

        if parts[1] == "provenance" and len(parts) >= 3:
            manifest = A.provenance(parts[2])
            if manifest is None:
                return json_reply(handler, {"ok": False, "error": "proposal not found"}, 404)
            return json_reply(handler, manifest)

        if parts[1] == "consent":
            if method == "POST" and body:
                subject = body.get("subject")
                scope = body.get("scope")
                granted_by = body.get("granted_by") or "user"
                if not subject or not scope:
                    return json_reply(handler, {"ok": False, "error": "subject and scope required"}, 400)
                row = A.grant_consent(subject, scope, granted_by)
                return json_reply(handler, {"ok": True, "consent": row}, 201)
            return json_reply(handler, {"consent": A.list_consent()})

    handler.send_response(404)
    handler.end_headers()


def json_reply(handler: BaseHTTPRequestHandler, obj, code: int = 200):
    data = json.dumps(obj).encode()
    handler.send_response(code)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def _sse_stream(handler: BaseHTTPRequestHandler, query: dict):
    """GET /api/events?since=<seq>: live event stream.

    Replays buffered events newer than the cursor (since=0 gives the last
    50), then holds the connection open, flushing ": keepalive" comment
    lines every 15 seconds of idle time. Each change on the write paths
    wakes every connected client immediately. When the connection cap is
    hit, the oldest client is dropped with a close event.
    """
    since = 0
    try:
        since = max(0, int(query.get("since", ["0"])[0] or 0))
    except (ValueError, IndexError):
        since = 0

    with _sse_cond:
        if len(_sse_clients) >= SSE_MAX_CLIENTS:
            _sse_clients.pop(0).closed.set()
            _sse_cond.notify_all()
        client = _SSEClient()
        _sse_clients.append(client)

    handler.send_response(200)
    handler.send_header("Content-Type", "text/event-stream")
    handler.send_header("Cache-Control", "no-cache")
    handler.end_headers()

    def send(event_type: str, seq: int, data: dict):
        payload = dict(data)
        payload["seq"] = seq
        handler.wfile.write(
            f"event: {event_type}\ndata: {json.dumps(payload)}\n\n".encode())
        handler.wfile.flush()

    last_seq = since
    with _sse_cond:
        for ev in _sse_events:
            if ev["seq"] > since:
                send(ev["type"], ev["seq"], ev["data"])
                last_seq = ev["seq"]

    try:
        while True:
            with _sse_cond:
                if client.closed.is_set():
                    break
                if _sse_seq <= last_seq:
                    if _sse_cond.wait(timeout=SSE_KEEPALIVE):
                        continue
                pending = [ev for ev in _sse_events if ev["seq"] > last_seq]
                last_seq = _sse_seq
            for ev in pending:
                send(ev["type"], ev["seq"], ev["data"])
            if not pending:
                handler.wfile.write(b": keepalive\n\n")
                handler.wfile.flush()
    except (BrokenPipeError, ConnectionResetError, OSError):
        pass
    finally:
        if client.closed.is_set():
            try:
                send("close", 0, {})
            except Exception:
                pass
        with _sse_cond:
            if client in _sse_clients:
                _sse_clients.remove(client)


# Security headers (BUILD-SPEC B11): applied to EVERY response via the
# send_response override below, so HTML, JSON, SSE and error paths all carry
# them. CSP is same-origin so fetch/EventSource are unaffected.
SECURITY_HEADERS = [
    ("Content-Security-Policy",
     "default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:"),
    ("X-Content-Type-Options", "nosniff"),
    ("X-Frame-Options", "DENY"),
    ("Referrer-Policy", "no-referrer"),
    ("Permissions-Policy",
     "geolocation=(), microphone=(), camera=(), payment=(), usb=(), display-capture=()"),
]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_response(self, code, message=None):
        super().send_response(code, message)
        for name, value in SECURITY_HEADERS:
            self.send_header(name, value)

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
    global FIXTURE, OFFLINE, FEEDS, AUTH_TOKEN
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--host", default="127.0.0.1",
                    help="bind address (127.0.0.1 = local only, 0.0.0.0 = stage)")
    ap.add_argument("--auth", default=None,
                    help="token gate: POST /api/* + GET /api/stats and /api/audit need ?token= or Bearer")
    ap.add_argument("--fixture", default="",
                    help="load a golden fixture feed from scaffold/fixtures/NAME.json")
    ap.add_argument("--offline", action="store_true",
                    help="force offline mode (no LLM key, no network)")
    ap.add_argument("--feeds", action="store_true",
                    help="use the real data kit (data/feeds) as the feed")
    ap.add_argument("--inject-failures", action="store_true",
                    help="simulate a provider timeout on every chat call (failure drill)")
    args = ap.parse_args()
    if args.fixture:
        FIXTURE = args.fixture
    OFFLINE = args.offline
    FEEDS = args.feeds
    AUTH_TOKEN = args.auth
    if args.inject_failures:
        P.set_inject_failures(True)
    if OFFLINE:
        import os
        os.environ["OLLAMA_API_KEY"] = ""
    # apply the canonical schema (idempotent) so the storage layer is ready
    # before any request lands; non-fatal on failure (BUILD-SPEC B9)
    try:
        S.get_storage(DB).migrate()
    except Exception as e:
        print(f"[serve] storage migrate warning: {e}")
    gate = "  (auth on)" if AUTH_TOKEN else ""
    print(f"[serve] http://{args.host}:{args.port}  (ctrl-c to stop){gate}")
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    # compute the mode badge in the background so the server binds and serves
    # immediately; load_feed may take a while on first cold start.
    def _announce():
        mode = current_mode()
        print(f"[serve] mode={mode} ready")
    threading.Thread(target=_announce, daemon=True).start()
    server.serve_forever()


if __name__ == "__main__":
    main()
