# SESSION LOG - 2026-08-14 (the all-in window)

Window: 15:10 IST to ~17:40 IST. This is the complete record of this
session. The campaign-wide timeline lives in atlas/content/BUILD-LOG.md;
this file is the session-level detail: decisions, whys, findings,
commits, and the exact state at window end.

## 1. WINDOW START (15:10)

- New window resumed off CONTINUATION-PROMPT.md (HEAD 009e196).
- State verified: watchdog healthy (Rajasthan 2026, 402 reg at the
  time), crons 12/12, repo clean, zero drift.

## 2. DECISIONS MADE THIS WINDOW

1. Builds gated on user go: user first said "hold builds, plan-only",
   then "lets go all in" (16:42). All scaffold builds happened after
   the go.
2. HARD RULE (user): ALL source code written via opencode CLI. Hermes
   = architect/reviewer (briefs, audits, tests, commits). Saved to
   memory + ~/AGENTS.md conventions.
3. Research frontier closed honestly: p-society org census showed NO
   public 2026 solutions repo exists; 2024 problems not in site source.
   Everything else is time-gated to the 21:30 drop.
4. Supabase backend NOT built (needs project + keys; schema is already
   Supabase-shaped, 20 min on the night if the problem demands cloud).
5. Atlas built as the full-repo documentation site (user request:
   "extreme detail, clickable file buttons").

## 3. THE BUILDS (all via opencode, all audited by Hermes)

### Approval gate (commit cfaf85a)
- scaffold/engine/approval.py: typed tool registry (4 tools),
  policy gate (read-only auto / reversible suggest / side-effecting
  require), proposals + audit_events tables, audit-before-status-flip.
- serve.py: GET /api/tools, GET+POST /api/proposals, POST /api/approve,
  GET /api/audit. UI: Actions tab with proposal cards + audit table.
- G1-G13 suite 13/13. Audit rounds: double-decision guard (no fake
  history), G13 bash -n check.

### Trace viewer + fixture replay (commit f131a2f)
- engine.py: TRACE deque(maxlen=200) ring buffer, per-item LLM modes,
  SCAM_WORDS cap (5.0, never urgent), _rank_why explainer.
- serve.py: --fixture NAME, --offline, mode in /api/stats, /api/trace.
- UI: mode badge (live/cached/offline/fixture) + trace drawer.
- fixtures/: happy, ambiguous, adversarial + expected_*.json.
- T1-T6 12/12. AUDIT FOUND A REAL BUG: --offline blanked the env AFTER
  engine import, LLM still fired with a key set. Fixed with lazy env
  reads + regression test.

### Provider adapter + multimodal + provenance (commit e0303de)
- providers.py: Provider protocol, OllamaProvider, NullProvider, lazy
  SIGNAL_PROVIDER read. Swap LLM backends via env, no code edits.
- multimodal.py: extract_text with runtime-detected extractors
  (builtin text, optional pypdf, optional tesseract), graceful None +
  reason, never hard-fails. POST /api/ingest.
- approval.py: consent table (UNIQUE upsert), provenance manifest with
  deterministic prompt_sha256, consent_required flag on proposals.
- P1-P4 9/9, M1-M4 4/4, Q1-Q4 4/4. Audit fix: provenance model label
  now reflects actual LLM usage.

### The Atlas (commits 88e8a0a + 1685b8d)
- atlas/build.py: stdlib generator, renders every file in full
  (md via minimal converter with tables/code/lists; code files as
  code blocks), 69 pages, ~795K source chars.
- atlas/site/index.html: reading ladder + 10 sections, PAGE + OPEN FILE
  buttons. atlas/serve.sh (chmod +x fixed 1685b8d). test_build green.

## 4. THE AGGRESSIVE AUDIT (17:05, user directive)

Findings and fixes (full detail in atlas/content/BUILD-LOG.md):
1. CRITICAL: test race. The four server-starting suites used a fixed
   1.2s sleep; serve.py computed mode at startup, which on a COLD DB
   runs the whole pipeline before binding. test_provenance (fake key
   for Q1) crashed on cold start. The earlier "42/42" claim was
   warm-state dependent. FIXED: wait_ready() polling (30s cap),
   per-suite fresh DB, non-blocking daemon-thread startup.
2. Test contamination: shared signal.db made suite order matter.
   FIXED by fresh-DB isolation.
3. Rule compliance: 377 em dashes across 33 files + ~20 AI-tell words
   in 8 files (pre-rule corpus + parallel-run output). Swept. Verbatim
   quotes + URL slugs left intact on purpose.
4. Stale doc numbers (CODE-WALKTHROUGH line counts). Fixed.
5. One false finding of my own (claimed a dead urllib import that the
   provider refactor had already removed). Corrected in the log.
6. demo-feed.json wart: documented, harmless, left as-is.

RE-VERIFIED after fixes, my own runs: both orders, fresh DBs,
42/42 order-independent. demo.sh end to end 9/9 endpoints 200.

## 5. RESEARCH DONE THIS WINDOW

- Evening intel refresh (a630777): submission = PPT only (pdf/pptx
  50MB), multiple submissions allowed, judge buttons shortlist/reject/
  hold/noshow, score /5 weighted 100, D3 site live at
  d3fest.techsoc-iiitbbsr.com, 456 reg, Tirtha Desai new contact.
- p-society harvest (91a07dc): org census complete, no 2026 solutions
  repo exists, 2024 problems dead end closed, 2025 already harvested.
- User's parallel keys: 137 in ~/Desktop/parallel spams, spot-probed
  newest 5 all alive (200/200). Watchdog re-probes + rebuilds the
  ledger automatically at 21:05.

## 6. KEY FACTS AT WINDOW END (verified)

- HEAD: 1685b8d (local == remote, clean tree).
- Suites: approval 13/13, trace 12/12, providers 9/9, multimodal 4/4,
  provenance 4/4, atlas test green. Order-independent on fresh DBs.
- Atlas: 69 pages, ~795K chars, serves via ./atlas/serve.sh on port
  8900 (or open atlas/site/index.html directly).
- Watchdog: craft-n-code-watch every 6h, next tick 21:05 IST (also
  re-probes all parallel keys).
- Remaining work: Rudra ask (user), 4 demo videos (team), pitch
  rehearsal (team), night flow 21:30 drop -> 06:00 submit, 10:00-17:30
  presentation at MUJ.
- The drop: Aug 15 21:30 IST (event site timeline), submission via
  Unstop round 1569450 (PPT, pdf/pptx, max 50MB, resubmit allowed,
  latest wins).

## 7. RULES IN FORCE

1. All code via opencode CLI. Hermes audits, tests, commits.
2. No em dashes, no AI-tell words (corpus now swept, 0 in sources).
3. Research waves one by one.
4. Zero uncontrolled dependencies in the demo.
5. Repo reflects true state, verified numbers, honest negatives.
