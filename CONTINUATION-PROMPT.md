# CONTINUATION-PROMPT - Craft N Code (read this FIRST in a new window)

> Drop this file's contents (or this path) as the first message in a new Hermes window. It fully resets context. Written 2026-08-14 17:45 IST (all-in window refresh).

---

## WHO / WHAT

Team 511 (Harsh Gounder = lead, Ayush Kharwar, Sujal Shukla) is competing in the **Craft N Code Rajasthan State Qualifier** (Cyber Space Club MUJ, Unstop 1730314), gateway to the **Craft N Code National Finals at IIIT Bhubaneswar (Oct 30 - Nov 1 2026)**. This repo (`~/craft-n-code`, PRIVATE, remote github.com/harshgounder/craft-n-code) is the war-room: 40+ research files + a verified scaffold, all live-verified.

**We are already registered and paid (₹299/team, live API confirmed).**

## THE IMMEDIATE MISSION (the deadline is the whole game)

| When (IST) | What |
|---|---|
| **Aug 15 21:00** | Idea submission OPENS (Unstop) |
| **Aug 15 21:30** | ★ PROBLEM STATEMENTS DROP ★ (written by the sponsor companies) - our pre-built decision tree fires within 10 min |
| Aug 16 06:00 | Idea submission CLOSES (submit before this) |
| Aug 16 10:00-17:30 | Pitch to judges at MUJ (3-min demo, 2:30 target) |

**CRITICAL AUG 14 INTEL (Rudra, club, in person)**: the 5 site tracks are the CLUB'S BACKUP SET and are NOT the basis for prep. The REAL problem statements are written by the sponsor companies (Google, Apple, Meta, Accenture, Adobe) and drop at/just before the 21:00 window. Decision tree fires on COMPANY DNA first. See IDEA-BANK §5 (company-lane protocol) + the 6 deep-research runs in research/company-lanes/.

**The idea bank is already written**: `research/IDEA-BANK.md` - pre-built answers for the 4 sponsor-shaped lanes (IDEA A BriefLens = agentic ops, IDEA B Kavach Circle = multimodal assistant, IDEA C SignalStory = creative media workflow, IDEA D Kavach = security), cue table, setter prior (Google 24% > Accenture 22% > Meta 21% > Adobe 18% > Apple 15%), risk table, action plan. The strategic core: ONE engine (ingest → dedupe → summarize → rank → deadlines → propose → approve) with skins, + Kavach for the security lane.

## WHAT'S DONE (verified, committed, pushed)

**Repo state**: HEAD 1685b8d, local == remote, zero drift. ~180 files tracked.

### The scaffold (the night's weapon, ALL BUILT + verified order-independent)
- `scaffold/engine/engine.py`: domain-agnostic pipeline (ingest → dedupe → LLM summarize → rank → deadlines). LLM mode = ollama-cloud deepseek-v4-flash:0731 (OLLAMA_API_KEY in ~/.hermes/.env, LIVE). Offline mode = regex dates + tf-idf + cache replay (22 hits), zero deps. Trace ring buffer (last 200 steps).
- `scaffold/engine/approval.py`: approval gate (typed tool registry, policy gate auto/suggest/require, proposals + audit tables, consent records, provenance manifests). Verified 13/13.
- `scaffold/engine/providers.py`: provider adapter (SIGNAL_PROVIDER env swap: ollama / null, lazy reads). Verified 9/9.
- `scaffold/engine/multimodal.py`: multimodal input (text/PDF/image extractors, runtime-detected, graceful fallback). POST /api/ingest. Verified 4/4.
- `scaffold/webapp/serve.py` + `static/index.html`: zero-dependency python server (14 endpoints) + dark UI (digest, ranked feed, search, request board, Actions tab with approve/reject/snooze + audit trail, mode badge, trace drawer). Verified 12/12.
- `scaffold/tests/`: 5 acceptance suites (test_approval 13/13, test_trace 12/12, test_providers 9/9, test_multimodal 4/4, test_provenance 4/4). ALL order-independent on fresh DBs (wait_ready polling + per-suite fresh DB + non-blocking server startup).
- `scaffold/fixtures/`: 4 golden feeds (happy, ambiguous, adversarial, multimodal) + expected_*.json.
- `scaffold/deck/deck-gen.js` + 4 decks (deck-agentic, deck-multimodal, deck-creative, deck-kavach, ~107K each, schema-validated). One skeleton → 4 sponsor-shaped decks.
- `scaffold/demo.sh` (one-command demo runner, verified end to end: 9/9 endpoints 200), `scaffold/README.md`.
- `docs/DEMO-STORYBOARDS.md` (4× 3-min storyboards), `docs/HARDWARE-GATE.md` (archived option, NOT a track assumption).
- **The Atlas** (docs website, commit 88e8a0a): `atlas/site/index.html` renders EVERY repo file in full (69 pages, ~795K chars), reading ladder + OPEN FILE buttons. Run `./atlas/serve.sh` → http://localhost:8900/atlas/site/index.html (or double-click the index.html). Generator: `atlas/build.py` (stdlib). `atlas/content/BUILD-LOG.md` = full campaign timeline incl. the aggressive audit.
- STRIP DONE (commit d00077b): all site-track/campus assumptions removed (PS-01..PS-05, Campus Pulse, Night Ops, Hygiene Sentinel). Engine is domain-agnostic; only seed data changes on the night.

### The research stack (6 deep-research runs, all landed + pushed)
- `research/company-lanes/`: cnc-company-lanes-pass1 (65.5K, SURFACE, 5 named skins), cnc-company-lanes-pass2 (34.9K, DEEP 90.1, 111 cites, 3 predicted shapes), cnc-sponsor-products (68K, ADECENT 230 cites), cnc-winner-anatomy (62K, SURFACE 138 cites), cnc-problem-lanes (78K, ADECENT 333 cites, 5 ranked predicted problems + build cards + kill criteria + 24h plan), cnc-state-rounds (42K, ADECENT 125 cites, honest negative: no state-round problems publicly recoverable).
- `research/WAVE-SYNTHESIS.md`: the 5 most likely problem shapes ranked + common denominator (input → extraction → evidence → ranking → proposed action → policy gate → human approval → audit trace) + 5 portable patterns + gaps table + 8.5h execution plan + zero-dependency rule + 10 questions to ask at reveal.
- `research/CHEATSHEET-BRIEF.md`: what matters most, what each sponsor makes/looks for (verified from their own hackathons), hottest tech for a 24h build.
- `research/prompts/`: 6 prompt files (company-lane ×2, sponsor-products, winner-anatomy, problem-lanes, state-rounds) saved for re-fire.
- Full competitive intel: editions 2022/2023/2024/2025/2026, organizers, judges (6, taste profile), winners (AFTERPACKETS reverse-engineered; 2024 Wizard_Oz + Fork), losers (PromptBuddy, EduSynth), 2025 state map (11 rounds, 1,592 reg / 285 players), 2026 field (402 reg Rajasthan).
- 2025 problem statements: FULL verbatim (7 Phase-1 + 7 Phase-2) in `research/raw/`.
- Re-audit sweep (Aug 14): every claim re-checked, corrections in `research/RE-AUDIT-FINDINGS.md`.

## NEXT STEPS (in order)

1. **ALL SCAFFOLD BUILDS: DONE** (Aug 14 evening, via opencode, audited by Hermes):
   approval gate 13/13 (cfaf85a) · trace viewer + fixtures 12/12 (f131a2f) ·
   provider adapter 9/9 + multimodal 4/4 + provenance/consent 4/4 (e0303de) ·
   atlas docs site (88e8a0a, serve.sh exec fix 1685b8d) · aggressive audit fixes
   (3644d83: wait_ready polling, per-suite fresh DB, non-blocking startup,
   corpus rule sweep). All suites order-independent on fresh DBs: 42/42 in
   two orders, independently re-verified.
2. **Rudra ask (USER ACTION, can't do from phone)**: ask Rudra (or any CSC exec) for the 2025 RAJASTHAN state-round problems + judging format. The ONLY gap the internet can't close. If obtained, drop in repo or Telegram and fold in.
3. **Demo videos (TEAM ACTION)**: 4× 3-min pre-recorded (screen + voiceover), storyboards ready in docs/DEMO-STORYBOARDS.md.
4. **Pitch rehearsal (TEAM ACTION)**: 2:30 target, hard timer.
5. **Aug 15**: 21:00 watch Unstop. 21:30 problems drop → company fingerprint scan (cue table, 2 min) → decision tree (10 min) → pick idea A/B/C/D → pick deck + storyboard → swap seed data (15-40 min) → ./demo.sh → submit before 06:00 (PPT: pdf/pptx max 50MB, resubmit allowed, latest wins).
6. **Aug 16**: pitch 10:00-17:30. 3-min demo (2:30 rehearsal target). Win the round, top-2 advance.
7. Parallel track: IIC 3.0 R1 ends Aug 25 (repo `~/iic-3`, judge-watch cron live).
8. After qualifier: national prep (Oct 30 - Nov 1). Watchdog cron (`craft-n-code-watch`, every 6h) tracks reg counts + judge/sponsor reveals; state in `research/watch-state.json`.

## OPERATING RULES

- **ALL source code via opencode CLI (HARD RULE, user 2026-08-14)**. Hermes = architect/reviewer: writes briefs, audits diffs, tells opencode what's right/wrong, runs tests, commits. Hermes never writes source code itself (docs/research/tests/commands OK). See opencode skill (autonomous-ai-agents/opencode).
- Waves ONE BY ONE, no parallel fan-out (user directive). Extreme depth, no fluff.
- Verify before claiming: live Unstop API (`https://unstop.com/api/public/competition/<ID>`, data.competition nesting) is ground truth; tag claims VERIFIED / PARTIAL / NOT FOUND.
- Web infra degraded: Firecrawl 402; use rivalsearch (`mcp__rivalsearch__web_search`) + curl with Chrome UA + r.jina.ai + gh CLI (authed).
- NO em dashes, no AI-tell words (hard rule). Corpus swept Aug 14 (377 dashes removed; verbatim quotes + URL slugs left on purpose).
- Everything committed + pushed; report milestones via Telegram (token: `grep TELEGRAM_BOT_TOKEN ~/.hermes/.env`, chat_id=6408901386), no permission-asking.
- Report to user in terminal too (CLI session) - plain text, no markdown tables.
- Parallel deep-research: processor `pro-fast` is the ONLY working combo (lite 401s on every key). Rotate keys on 402. Keys: **137** in `~/Desktop/parallel spams` (newest at BOTTOM, spot-probed alive 2026-08-14), ledger auto-rebuilds at each watchdog tick.

## KEY FACTS (do not re-research)

- Unstop IDs: 1730314 Rajasthan 2026 (654 reg (live API 2026-08-15 15:02, was 629 at 10:04)/96 players, ₹299, LIVE) · 1730325 UP 2026 · 1171379 national 2024 · 1175823 state 2024 · 1545708 RJ 2025 · 374277 D³ Fest 2025 (dead).
- Submission format (VERIFIED Aug 14): PPT only (pdf/pptx, max 50MB, mandatory), multiple submissions allowed (latest wins), round 1569450 Aug 15 21:00 - Aug 16 06:00, presentation round Aug 16 10:00-17:30. Judge panel buttons: shortlist/reject/hold/noshow, score /5 weighted 100.
- 2026 question writers: the sponsor companies (Google, Apple, Meta, Accenture, Adobe) per club insider. The site's 5-track list is a BACKUP SET, not the real questions (Rudra intel, Aug 14). Only the timings are reliable from the site. Pass-2 deep research could NOT publicly verify sponsor authorship - Rudra's word is the best signal.
- 2025 winners: AFTERPACKETS (MUJ Highlanders) - zero external deps, Android VPNService + C++ DPI, empty lane. 2024: Wizard_Oz (CVRGU) 1st, Fork (RVCE) 2nd.
- The 3 predicted shapes (INFERRED, rehearsal only): 1) agentic ops/personal productivity (Google/Accenture) → IDEA A, 2) multimodal campus/community assistant (Meta/Apple) → IDEA B, 3) responsible creative/enterprise media workflow (Adobe/Accenture) → IDEA C. Security lane → IDEA D Kavach.
- Key people: Abhinav Trikha (CSC chair, +91 95994 15311), Spandan Hota (CSC contact, GSA), Soubhik Gon (2024 coordinator → Nasuni), Swoyam Nayak (→ Sarvam AI).
- 2025 problems verbatim in `research/raw/rnr-phase1-full.txt` + `rnr-phase2-full.txt`.
- The winner formula: AI non-negotiable, working demo > deck, real-world impact framing, zero external deps in demo, clean repo = free points.
- LLM layer: OLLAMA_API_KEY live (deepseek-v4-flash:0731 via https://ollama.com/v1/chat/completions). OPENROUTER + XIAOMI present. GEMINI/GROQ/UNOROUTER empty.
- Crons: 12/12 healthy. craft-n-code-watch every 6h (also re-probes all 137 parallel keys, rebuilds the ledger).
- Telegram: bot artemas (token in ~/.hermes/.env), chat_id 6408901386, last message 1324 (atlas live).
- Atlas: `./atlas/serve.sh` → http://localhost:8900/atlas/site/index.html (or double-click the file). Session detail: docs/SESSION-LOG-20260814.md.

## CURRENT FILE TREE (key)

```
~/craft-n-code/
├── README.md               ← war-room index
├── CONTINUATION-PROMPT.md  ← this file
├── INDEX.md                ← file-by-file map
├── atlas/                  ← ★ THE ATLAS (docs site, 69 pages)
│   ├── site/index.html     ← open this (or ./atlas/serve.sh → :8900)
│   ├── build.py + test_build.py + serve.sh + manifest.json
│   └── content/BUILD-LOG.md ← full campaign timeline + audit episode
├── scaffold/               ← ★ THE NIGHT'S WEAPON (all verified)
│   ├── engine/engine.py    ← ingest → dedupe → summarize → rank → deadlines + trace
│   ├── engine/approval.py  ← approval gate + consent + provenance
│   ├── engine/providers.py ← provider adapter (SIGNAL_PROVIDER)
│   ├── engine/multimodal.py← multimodal input adapter
│   ├── webapp/serve.py + static/index.html (14 endpoints, dark UI)
│   ├── tests/              ← 5 acceptance suites (42/42, order-independent)
│   ├── fixtures/           ← 4 golden feeds + expected
│   ├── deck/deck-gen.js + 4 .pptx (agentic/multimodal/creative/kavach)
│   ├── demo.sh + README.md
├── docs/                   ← REPO-TOUR, CODE-WALKTHROUGH, BUILD-SPEC(+2),
│                              DEMO-STORYBOARDS, SESSION-LOG-20260814, HARDWARE-GATE
└── research/               ← 40+ files (see INDEX.md)
    ├── IDEA-BANK.md        ← ★ THE playbook for Aug 15 21:30
    ├── CHEATSHEET-BRIEF.md ← what matters, sponsor DNA, hottest tech
    ├── WAVE-SYNTHESIS.md   ← 5 predicted shapes + gaps + execution plan
    ├── company-lanes/      ← 6 deep-research reports (376K total)
    ├── prompts/            ← 6 re-fire prompts
    └── raw/                ← 2025 verbatim problems
```

Related repos: `~/iic-3` (IIC 3.0, R1 ends Aug 25), `~/muj-academics` (planner + drive sync crons alive), `~/parallel-ai-stack` (launcher + watcher + run-ledger), `~/.hermes/scripts/craft-n-code-watch.py` (watchdog).

---

**Resume command**: read this file, then `research/IDEA-BANK.md`, then `research/WAVE-SYNTHESIS.md`, then `docs/SESSION-LOG-20260814.md`. Do not re-harvest what's already verified. ALL builds are done and verified (42/42 order-independent); the opencode rule is in force. Remaining work is user/team actions (Rudra ask, demo videos, rehearsal) + the Aug 15 night flow (drop at 21:30, submit by 06:00).

## LATEST STATE (refresh Aug 15 ~14:30 IST, read before anything else)

17 parallel.ai research runs integrated (wave2 + wave3-14 + wave15-18),
all raw JSON+MD in research/raw/, all committed. READ FIRST in a night
window, in order: research/NIGHT-CHEAT-SHEET-2026.md (the 21:30 mount
table), research/WAVE-SYNTHESIS-2026.md (master index of all 17),
research/PRIOR-ART-MAP-2026.md (the exists-map, three tensions, judge
attack answers), docs/NIGHT-RUNBOOK.md (timeline, format facts, 3-act
demo script, PRE-WARM RULE, 429 WATCH, honesty moment), docs/
SUBMISSION-TEXT-KIT.md (v2: evaluator closing line, fraud numbers),
docs/BUILD-SPEC-3.md + BUILD-SPEC-4.md (both built, both verified:
badge honesty H1-H6, feeds F1-F8, stress 23/23, deck MCP slide M1-M6).

STATE: 81/81 suites green, 5/5 kits, deck has MCP slide, tree clean
at HEAD, atlas 135 files (1.78M chars, refreshed Aug 15 15:40 with
all night files + raw waves + prompts). LLM provider rate-limits
under load (429 WATCH: two-pass pre-warm, warm cache fallback,
honesty story).

OPEN (night): Rudra ask (cutoff 21:00), 4 demo videos, rehearsal
2:30, venue fan-out 30 min before code (wave-17 rule), then the
night flow 21:30 -> 09:00. Problem drops 21:30; fingerprint -> tree
-> kit mount via NIGHT-CHEAT-SHEET; gates 23:00 / 05:00 / 09:00.

## ROUNDS (corrected 2026-08-16, user intel)
- Round 0: online, closes 18:00 Aug 16. PPT + prototype, IIIT-B faculty grade + suggestions, no elimination.
- Round 1: offline 12h sprint on campus, likely next weekend. BUILD UPON the Round 0 submission, same product.
- Round 2: at IIIT-B later. NEW problem statements, NEW product from scratch.
- Implication: the engine + kit system + research method are the durable weapon, not any single lane.
  Round 0/1 = PS-07 advisory engine. Round 2 = fresh mount, unknown statements.
- Internal politics delayed the event; CyberSpace holds it together, first big event. Dates soft, rounds real.
