# BUILD-SPEC - the 2 pending scaffold upgrades (plan-only, no code yet)

Status: Parts 1 + 2 BUILT + VERIFIED (2026-08-14 evening, via opencode, audited by Hermes). Part 1 = approval gate (G1-G13, 13/13). Part 2 = trace viewer + fixture replay (T1-T6 + offline regression, 12/12). This spec is now a record of what was built; no further work pending on these two items.
Every item below is grounded in the CURRENT code (read serve.py + engine.py
line-by-line today), so the build is mechanical execution, zero design time.

Target: ~30-45 min for the approval gate, ~30-45 min for trace+fixtures.
Both fit in the "3h of remaining polish" window from WAVE-SYNTHESIS §10.
Reason: the rank-1 predicted problem shape (Google/Accenture lane) is a
"trustworthy agent with approved tools + audit trail". Judges see the control
plane. The current scaffold has NO approval concept at all.

---

## PART 1. APPROVAL GATE (typed tools + policy gate + audit)

### 1.1 What exists today (facts from the code, do not re-read)

- serve.py routes: GET /api/feed, /api/digest, /api/search?q=, /api/complaints
  (GET+POST), /api/stats. POST body JSON parsing already works in Handler._serve.
- serve.py has FEED_CACHE (module global) + route() is the SINGLE place to add
  endpoints. json_reply() exists for JSON responses.
- engine.py: Item dataclass, LLM (ollama-cloud + .llm_cache.json replay),
  offline fallback, sqlite persistence in main() to scaffold/engine/signal.db.
- UI: webapp/static/index.html, dark, 3 tabs (Feed/Ask/Requests).

### 1.2 New file: scaffold/engine/approval.py (~120 lines)

Data model (plain dataclasses, mirror Item style):

    @dataclass
    class Tool:
        name: str                 # e.g. "send_reminder", "pay_fee", "book_slot"
        description: str
        params: dict              # JSON schema-ish: {param: type}
        side_effect: str          # "read-only" | "reversible" | "side-effecting"

    TOOL_REGISTRY: dict[str, Tool]  # typed registry, 3-4 tools for the demo:
        - lookup_room("query")            → read-only (auto-executes)
        - send_reminder("who","what","when") → reversible (approval suggested)
        - submit_form("form_id","answers")   → side-effecting (approval REQUIRED)
        - pay_fee("amount","ref")            → side-effecting (approval REQUIRED)

    @dataclass
    class Proposal:
        id: str                   # "P-1", "P-2", ... (mirror ticket #C-117 style)
        tool: str
        params: dict
        reason: str               # one line, LLM or template
        evidence: list[dict]      # [{source_id, snippet}] from the item's body
        confidence: float         # 0.0-1.0
        status: str               # pending | approved | rejected | executed | snoozed
        created_at: str
        decided_at: str | None
        actor: str | None         # who decided (demo: "judge" or "user")

Policy gate (the "approved tools" story, pure function, testable):
    def gate(tool: Tool) -> str:
        read-only → "auto"          (executes immediately, still logged)
        reversible → "suggest"      (UI shows APPROVE / REJECT / SNOOZE)
        side-effecting → "require"  (blocks until human approves)

sqlite persistence: reuse scaffold/engine/signal.db, add 2 tables
(create-if-not-exists, do NOT drop the items table):

    CREATE TABLE IF NOT EXISTS proposals (
        id TEXT PRIMARY KEY, tool TEXT, params TEXT, reason TEXT,
        evidence TEXT, confidence REAL, status TEXT,
        created_at TEXT, decided_at TEXT, actor TEXT);
    CREATE TABLE IF NOT EXISTS audit_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, actor TEXT,
        decision TEXT, proposal_id TEXT, tool TEXT, params TEXT,
        evidence TEXT, reason TEXT);

Audit invariant: EVERY decision (approve/reject/snooze/auto-execute) writes
one audit row BEFORE the status flips. This is the demo's "trace" story.

### 1.3 New endpoints in serve.py (add inside route(), api branch)

    GET  /api/tools       → registry list (name, description, side_effect)
    GET  /api/proposals   → all proposals, newest first
    POST /api/proposals   → {"item_id","tool","params"} → engine proposes
                           (evidence pulled from the item's body, reason via
                           LLM with cache+offline fallback, confidence from
                           rank_score normalized)
    POST /api/approve     → {"proposal_id","decision","actor"}
                           decision: approve | reject | snooze
                           approve → status executed (side-effecting) OR
                           approved (reversible); audit row written first
    GET  /api/audit       → audit log, newest first (what, who, when, why)

No auth (local demo, judges click buttons). actor defaults to "user".

### 1.4 UI (index.html, third tab becomes "Actions")

- Proposal card: tool name, one-line reason, params preview, evidence panel
  (source_id + snippet, collapsible), confidence badge, status chip.
- APPROVE (green) / REJECT (red) / SNOOZE (amber) buttons per card.
- On approve: card flips to EXECUTED with a fake progress line
  ("tool called, result logged"), audit entry appears.
- Audit tab or collapsible panel: table of (ts, actor, decision, tool).
- The demo beat: digest → click proposal → evidence panel → APPROVE → status
  flips → audit row appears. ~30 seconds of stage time, sells the whole story.

### 1.5 Acceptance tests (run after build, mirror the 13/13 style)

    G1  GET /api/tools returns >= 3 tools, each with a side_effect class.
    G2  Propose a side-effecting tool → status "pending", NOT executed.
    G3  Propose a read-only tool → auto-executes, audit row present.
    G4  POST /api/approve approve → status "executed", audit row with actor.
    G5  POST /api/approve reject → status "rejected", NOT executed.
    G6  Snooze → status "snoozed", still listed, not executed.
    G7  GET /api/audit shows every decision, newest first, with actor+ts.
    G8  Proposals persist across server restart (sqlite).
    G9  Offline mode (no OLLAMA key): proposals still generate (template
        reason + rule-based confidence), same statuses work.
    G10 Cache replay: second run hits .llm_cache.json, identical reasons.
    G11 UI: card renders evidence panel; buttons flip status; no JS errors.
    G12 Existing endpoints still pass (regression: feed/digest/search/stats).
    G13 demo.sh still runs end-to-end (regression).

---

## PART 2. TRACE VIEWER + FIXTURE REPLAY (demo-failure insurance)

### 2.1 The problem it solves

WAVE-SYNTHESIS §4: "no explicit trace of what the engine did". A judge asks
"why is this ranked first?" and today the answer is invisible. Also: a live
demo can die at 3 AM; replay mode must be a first-class mode, not a hack.

### 2.2 Fixtures (new dir: scaffold/fixtures/)

Three golden feeds, each a JSON array of Item-shaped dicts (channel,
source_id, sender, subject, body, received_at, profile_tags, kind):
    happy.json       → 6 clean items, 2 deadlines, 1 obvious side-effecting action
    ambiguous.json   → near-dupes (dedupe story), missing dates, low confidence
    adversarial.json → a scam-ish urgent item, an item with no sender, a fake deadline

Plus expected.json per fixture: expected top-3 order + expected proposals,
so replay is deterministic AND assertable.

### 2.3 Replay mode (serve.py)

    python3 serve.py --fixture happy    → load_feed() reads fixtures/happy.json
    python3 serve.py --fixture happy --offline  → force offline, still works

Mode is surfaced: /api/stats gains "mode": "live" | "cached" | "offline" |
"fixture" (derived: fixture flag, OLLAMA_KEY presence, cache hit ratio).
UI badge top-right: LIVE / CACHED / OFFLINE / FIXTURE. Candid fallback wins
judges (zero-dependency rule, AFTERPACKETS lesson).

### 2.4 Trace endpoint (serve.py + engine.py)

Engine already prints pipeline steps to stdout; capture them into a small
in-memory ring buffer instead (collections.deque, maxlen=200) inside
run_pipeline(), one dict per step:
    {"step": "ingest", "n": 11}
    {"step": "dedupe", "dropped": 2, "kept": 9}
    {"step": "summarize", "mode": "llm|cache|offline", "per_item": [...]}
    {"step": "rank", "top3": [{source_id, score, why}]}   # why = profile/authority/recency/deadline/urgency weights

    GET /api/trace → the buffer, newest first.

UI: collapsible "Trace" drawer at the bottom. The demo beat: judge asks why
item X is top → open trace → point at the deadline pressure weight. 15
seconds of stage time, "we can explain every decision" is a Google-line.

### 2.5 Acceptance tests

    T1  --fixture happy returns the fixture's expected top-3 (assertable).
    T2  --fixture happy --offline works with no network and no key.
    T3  /api/trace shows ingest → dedupe → summarize → rank, in order.
    T4  /api/stats mode reflects fixture flag (and offline).
    T5  Adversarial fixture: scam item does NOT rank top (urgency caps).
    T6  Regression: default run (no flags) behaves exactly as today.

---

## 3. ORDER OF BUILD (when the go lands)

1. approval.py (registry + gate + sqlite)  → ~30 min
2. serve.py endpoints (tools/proposals/approve/audit) → ~15 min
3. index.html Actions tab + audit panel → ~15 min
4. fixtures/ + --fixture flag + mode badge → ~25 min
5. /api/trace ring buffer → ~15 min
6. Run G1-G13 + T1-T6, fix, commit, push, Telegram.

Total ~1.5-2h if done in one pass (approval gate alone ~45 min).

## 4. WHAT THIS UNBLOCKS (per predicted shape, WAVE-SYNTHESIS §1)

- Rank 1 (trustworthy agent, Google/Accenture): the ENTIRE story is Part 1.
- Rank 2 (creative production agent, Adobe): review/approve loop already fits
  (approve = reviewer approval, audit = provenance record).
- Rank 4 (multimodal assistant, Meta): escalation = reject/snooze + human.
- Rank 5 (governed case router, Accenture): case → proposal → policy gate →
  approval → KPI is literally the flow.
- Off-map: the approval + trace layer is a differentiator on ANY demo.

## 5. OPEN ITEMS (not code)

- User go-signal is the only blocker on Part 1 + Part 2 (asked 2026-08-14
  15:20 IST, answer: "hold builds, plan-only for now").
- Multimodal adapter (image/PDF → evidence) still unplanned in detail: that
  one needs its own 60-90 min slot, only worth it if Meta/Apple flavor looks
  likely on the night. Decide AT the drop, not before.
- Provider adapter interface + provenance/consent record: low priority,
  already partially covered (env-var provider swap + Kavach patterns).
