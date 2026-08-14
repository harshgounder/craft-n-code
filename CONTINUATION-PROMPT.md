# CONTINUATION-PROMPT - Craft N Code (read this FIRST in a new window)

> Drop this file's contents (or this path) as the first message in a new Hermes window. It fully resets context. Written 2026-08-14 15:10 IST (re-audit refresh).

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

**Repo state**: HEAD 073951b, 11 commits today, local == remote, zero drift. 76 files tracked.

### The scaffold (the night's weapon, all verified 13/13 post-strip)
- `scaffold/engine/engine.py`: domain-agnostic pipeline (ingest → dedupe → LLM summarize → rank → deadlines). LLM mode = ollama-cloud deepseek-v4-flash:0731 (OLLAMA_API_KEY in ~/.hermes/.env, LIVE). Offline mode = regex dates + tf-idf + cache replay (22 hits), zero deps. Demo never dies.
- `scaffold/engine/approval.py`: approval gate (typed tool registry, policy gate auto/suggest/require, proposals + audit tables). Verified 13/13.
- `scaffold/webapp/serve.py` + `static/index.html`: zero-dependency python server + dark UI (digest, ranked feed, search, request board). Verified: stats 11 items / 6 deadlines / skin_ready, search "fee" → 3 results, ticket flow → #C-117.
- `scaffold/deck/deck-gen.js` + 4 decks (deck-agentic, deck-multimodal, deck-creative, deck-kavach, ~107K each, schema-validated). One skeleton → 4 sponsor-shaped decks.
- `scaffold/demo.sh` (one-command demo runner), `scaffold/README.md`.
- `docs/DEMO-STORYBOARDS.md` (4× 3-min storyboards), `docs/HARDWARE-GATE.md` (archived option, NOT a track assumption).
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

1. **Approval gate: DONE** (built Aug 14 evening via opencode, verified 13/13 G1-G13: typed tool registry, policy gate, POST /api/approve, audit log, Actions tab in the UI).
1b. **Trace viewer + fixture replay: DONE** (built Aug 14 evening via opencode, verified 12/12 T1-T6: --fixture/--offline flags, mode badge, /api/trace drawer, 3 golden fixtures, scam cap. Real bug found + fixed in audit: --offline now truly forces offline even with a key set).
2. **Rudra ask (USER ACTION, can't do from phone)**: ask Rudra (or any CSC exec) for the 2025 RAJASTHAN state-round problems + judging format. The ONLY gap the internet can't close. If obtained, drop in repo or Telegram and fold in.
3. **Demo videos (TEAM ACTION)**: 4× 3-min pre-recorded (screen + voiceover), storyboards ready in docs/DEMO-STORYBOARDS.md.
4. **Pitch rehearsal (TEAM ACTION)**: 2:30 target, hard timer.
5. **Aug 15**: 21:00 watch Unstop. 21:30 problems drop → company fingerprint scan (cue table, 2 min) → decision tree (10 min) → pick idea A/B/C/D → pick deck + storyboard → swap seed data (15-40 min) → ./demo.sh → submit before 06:00.
6. **Aug 16**: pitch 10:00-17:30. 3-min demo (2:30 rehearsal target). Win the round, top-2 advance.
7. Parallel track: IIC 3.0 R1 ends Aug 25 (repo `~/iic-3`, judge-watch cron live).
8. After qualifier: national prep (Oct 30 - Nov 1). Watchdog cron (`craft-n-code-watch`, every 6h) tracks reg counts + judge/sponsor reveals; state in `research/watch-state.json`.

## OPERATING RULES

- Waves ONE BY ONE, no parallel fan-out (user directive). Extreme depth, no fluff.
- Verify before claiming: live Unstop API (`https://unstop.com/api/public/competition/<ID>`) is ground truth; tag claims VERIFIED / PARTIAL / NOT FOUND.
- Web infra degraded: Firecrawl 402; use rivalsearch (`mcp__rivalsearch__web_search`) + curl with Chrome UA + r.jina.ai + gh CLI (authed).
- NO em dashes, no AI-tell words (hard rule). Casual "bro" tone, lowercase-ish, kaomoji.
- Everything committed + pushed; report milestones via Telegram (token: `grep TELEGRAM_BOT_TOKEN ~/.hermes/.env`, chat_id=6408901386), no permission-asking.
- Report to user in terminal too (CLI session) - plain text, no markdown tables.
- Parallel deep-research: processor `pro-fast` is the ONLY working combo (lite 401s on every key). Rotate keys on 402. Keys: 130 in `~/Desktop/parallel spams`, 43/103 alive in `~/parallel-ai-stack/run-ledger/keys.json`.

## KEY FACTS (do not re-research)

- Unstop IDs: 1730314 Rajasthan 2026 (402 reg/81 players, ₹299, LIVE) · 1730325 UP 2026 · 1171379 national 2024 · 1175823 state 2024 · 1545708 RJ 2025 · 374277 D³ Fest 2025 (dead).
- 2026 question writers: the sponsor companies (Google, Apple, Meta, Accenture, Adobe) per club insider. The site's 5-track list is a BACKUP SET, not the real questions (Rudra intel, Aug 14). Only the timings are reliable from the site. Pass-2 deep research could NOT publicly verify sponsor authorship - Rudra's word is the best signal.
- 2025 winners: AFTERPACKETS (MUJ Highlanders) - zero external deps, Android VPNService + C++ DPI, empty lane. 2024: Wizard_Oz (CVRGU) 1st, Fork (RVCE) 2nd.
- The 3 predicted shapes (INFERRED, rehearsal only): 1) agentic ops/personal productivity (Google/Accenture) → IDEA A, 2) multimodal campus/community assistant (Meta/Apple) → IDEA B, 3) responsible creative/enterprise media workflow (Adobe/Accenture) → IDEA C. Security lane → IDEA D Kavach.
- Key people: Abhinav Trikha (CSC chair, +91 95994 15311), Spandan Hota (CSC contact, GSA), Soubhik Gon (2024 coordinator → Nasuni), Swoyam Nayak (→ Sarvam AI).
- 2025 problems verbatim in `research/raw/rnr-phase1-full.txt` + `rnr-phase2-full.txt`.
- The winner formula: AI non-negotiable, working demo > deck, real-world impact framing, zero external deps in demo, clean repo = free points.
- LLM layer: OLLAMA_API_KEY live (deepseek-v4-flash:0731 via https://ollama.com/v1/chat/completions). OPENROUTER + XIAOMI present. GEMINI/GROQ/UNOROUTER empty.
- Crons: 12/12 healthy. craft-n-code-watch every 6h (last tick 14:34, state committed 073951b).
- Telegram: bot artemas (token in ~/.hermes/.env), chat_id 6408901386, last message 1319 (full re-audit).

## CURRENT FILE TREE (key)

```
~/craft-n-code/
├── README.md               ← war-room index, fresh
├── CONTINUATION-PROMPT.md  ← this file
├── INDEX.md                ← file-by-file map
├── scaffold/               ← ★ THE NIGHT'S WEAPON (verified 13/13)
│   ├── engine/engine.py    ← ingest → dedupe → summarize → rank → deadlines
│   ├── webapp/serve.py + static/index.html
│   ├── deck/deck-gen.js + 4 .pptx (agentic/multimodal/creative/kavach)
│   ├── demo.sh + README.md
├── docs/                   ← DEMO-STORYBOARDS.md, HARDWARE-GATE.md (archived)
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

**Resume command**: read this file, then `research/IDEA-BANK.md`, then `research/WAVE-SYNTHESIS.md`. Do not re-harvest what's already verified. If the user said yes to the approval gate, build it first (30-45 min).
