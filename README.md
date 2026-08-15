# Craft N Code  -  Rajasthan State Qualifier 2026

**Team 511's full war-room** for the Craft N Code Rajasthan State Qualifier (Cyber Space Club MUJ), gateway to the **Craft N Code National Finals at IIIT Bhubaneswar (Oct 30 – Nov 1, 2026)**.

> 🏆 **Mission**: win the Rajasthan qualifier, advance to nationals, and take the national title back to MUJ. MUJ's Team Highlanders (Abhishek Chaturvedi, Prasham Jain, Hrishi Bhalaria, Tapish Thakur) won the 2025 national finale with AFTERPACKETS  -  a mobile Deep Packet Inspection platform. We intend to repeat.

---

## 📌 Status (2026-08-14, live-verified)

| Step | Status |
|---|---|
| Unstop registration (team **511**: Harsh, Ayush, Sujal) | ✅ DONE |
| Registration fee paid (₹299/team  -  live API confirmed) | ✅ DONE |
| Idea submission (Aug 15 21:00 → Aug 16 06:00 IST) | ⏳ PENDING  -  problem statements drop **21:30 Aug 15** |
| Presentation to judges (Aug 16 10:00 → 17:30 IST, MUJ) | ⏳ PENDING |
| National finals qualification (top 2 advance) | ⏳ PENDING |
| National finals (IIIT Bhubaneswar, Oct 30 – Nov 1) | ⏳ PENDING |
| Shared scaffold (engine + webapp + 4 decks + storyboards) | ✅ DONE (verified 13/13, commit d00077b) |
| Deep-research wave (6 runs: sponsor DNA, winner anatomy, problem lanes, state rounds) | ✅ DONE (all landed, folded into IDEA-BANK §5 + WAVE-SYNTHESIS) |
| Approval gate (rank-1 predicted shape = approved tools) | ⏳ PENDING (30-45 min build, awaiting user go) |
| Demo videos (4× 3-min, screen + voiceover) | ⏳ PENDING (needs team, storyboards ready) |

**Watchdog**: `craft-n-code-watch` cron (every 6h, no-agent mode) probes Unstop for known listing IDs, tracks registration counts, flags judge/mentor/sponsor reveals. Silent when nothing changes. State in `research/watch-state.json`.

---

## 🎯 The Competition (verified)

- **Rajasthan State Qualifier** (Unstop listing **1730314**): **629 registered (watchdog 2026-08-15 10:04)**, ₹299/team, LIVE. Biggest confirmed 2026 state round (UP 1730325 has 1 reg). Problems are set by the state club (CSC MUJ)  -  own qualifier problems, contact-verified.
- **The event**: overnight hackathon at MUJ. Registration closed Aug 14 23:59. Idea submission Aug 15 21:00–Aug 16 06:00. Pitch to judges Aug 16 10:00–17:30.
- **Nationals**: IIIT Bhubaneswar, Oct 30 – Nov 1, 2026. Top 2 from each state advance. Travel sponsored. Problem statements release Oct 30 08:00.
- **2026 question writers (Rudra intel, Aug 14)**: the REAL problems are set by the sponsor companies (Google, Apple, Meta, Accenture, Adobe), not the club. The 5 site tracks are the club's BACKUP SET and are NOT the basis for prep. Only the timings are reliable from the site.
- **The overnight run** (nationals format): 20:00 check-in → 21:30 problems live + clock starts → 01:00 midnight fuel + mentors → 04:30 debug hour → 09:00 freeze/demo/judging.
- **Submission** (live-verified): deadline 09:00, one submission per team, resubmit until the clock hits zero, latest entry wins. Fields: `team_name`, `track`, `repo_url`, `demo_url` (optional), `pitch` (1–2000 chars). Supabase backend, plain INSERT (resubmit = new row; duplicate blocked).
- **The sponsor twist** (club-insider verified): the topic is NOT set by the club. Sponsor companies behind the hackathon set the questions  -  historically **Google, Apple, Facebook, Accenture & Adobe** (per CSC's official post: "inspired by", nuance documented). The 5 tracks are the categories; the sponsors drop the actual problem statements.
- **Night canteen** (live-verified  -  this is what 3 AM looks like): Midnight Maggi ₹40 (22:00–05:00), Cutting Chai ₹15 ("the primary compiler"), Cold Brew Shot ₹60, Paneer Roll ₹80 ("one-handed, keyboard safe"), Grilled Sandwich ₹70, Pizza Slice ₹90 ("reheated at 03:00, honestly still good"). Runners every 20 minutes.

---

## 🧠 The Idea Bank (drop-ready for 21:30 Aug 15)

**`research/IDEA-BANK.md`**  -  pre-built answers for the 4 sponsor-shaped lanes so we don't brainstorm on the night:

- **IDEA A "BriefLens"** (agentic ops / Google+Accenture DNA): ranked feed + AI proposes actions, human approves, audit logged.
- **IDEA B "Kavach Circle"** (multimodal assistant / Meta DNA): text + image + PDF in, evidence-backed answers with confidence, human escalation on risk.
- **IDEA C "SignalStory"** (creative media workflow / Adobe DNA): brief in → brand-consistent assets out, review loop, full provenance.
- **IDEA D "Kavach"** (security lane): our existing call-security product, real demo, security-judge DNA.

**The strategic core: one engine, many skins.** A domain-agnostic ingest/dedupe/summarize/rank/deadlines engine (built + verified 13/13) mounts any of the above with a different skin. Decision tree + cue table + setter prior + risk table + action plan in the file.

---

## 🛠️ The Shared Scaffold (the night's weapon, verified 13/13)

Whatever drops at 21:30, these are pre-built (`scaffold/`, see `scaffold/README.md`):

1. **The engine** (`scaffold/engine/engine.py`): ingest → dedupe → LLM summarize → rank → deadlines. Domain-agnostic, verified in LLM mode (ollama-cloud deepseek-v4-flash:0731, live) AND full offline mode (regex dates + tf-idf + cache replay, zero deps). The demo never dies (AFTERPACKETS rule).
2. **The webapp** (`scaffold/webapp/`): zero-dependency python server + dark UI (digest, ranked feed, search, request board). Runs on ANY machine with python3.
3. **4 decks** (`scaffold/deck/`): deck-agentic (BriefLens), deck-multimodal (Kavach Circle), deck-creative (SignalStory), deck-kavach. One pptxgenjs skeleton → 4 outputs, schema-validated.
4. **4 storyboards** (`docs/DEMO-STORYBOARDS.md`): second-by-second voiceover scripts for pre-recorded 3-min videos.
5. **demo.sh**: one command → generate feed + serve UI.

**Strip note (Aug 14)**: all site-track/campus assumptions removed (PS-01..PS-05, Campus Pulse, Night Ops, Hygiene Sentinel). The engine is domain-agnostic; only seed data changes on the night.

## 🔬 The Deep-Research Wave (6 runs, all landed)

| Run | Report | Depth | What it gave us |
|---|---|---|---|
| cnc-company-lanes (pass 1) | `research/company-lanes/cnc-company-lanes-pass1.content.md` | SURFACE | 5 named skins, setter prior, 10-min cue table |
| cnc-company-lanes-2 (pass 2) | `research/company-lanes/cnc-company-lanes-pass2.content.md` | DEEP 90.1 | honest negative (no public proof of sponsor authorship), 3 ranked predicted shapes, prep architecture |
| cnc-sponsor-products | `research/company-lanes/cnc-sponsor-products.content.md` | ADECENT 230 cites | what each sponsor makes + looks for (verified from their own hackathons) |
| cnc-winner-anatomy | `research/company-lanes/cnc-winner-anatomy.content.md` | SURFACE 138 cites | winner common traits, zero-dependency rule |
| cnc-problem-lanes | `research/company-lanes/cnc-problem-lanes.content.md` | ADECENT 333 cites | 5 ranked predicted problems + build cards + kill criteria + 24h plan |
| cnc-state-rounds | `research/company-lanes/cnc-state-rounds.content.md` | ADECENT 125 cites | honest negative: no state-round problems publicly recoverable; 10 questions to ask the organizer |

**Synthesis**: `research/WAVE-SYNTHESIS.md` (5 most likely problem shapes, common denominator = one engine wins, 5 portable patterns, gaps table, 8.5h execution plan, zero-dependency rule). **Cheatsheet**: `research/CHEATSHEET-BRIEF.md` (what matters most, sponsor DNA, hottest tech). **Re-fire prompts**: `research/prompts/` (6 files).

---

## 📜 Edition History (who ran it, how many times, who won)

### 2024  -  CraftNCode (D³ Fest, IIIT Bhubaneswar)
- **Run by**: Tech Society, IIIT Bhubaneswar (Unstop org 11832). State prelims (₹400/team) → 24h national finals at IIIT-B, **Nov 8 23:00 → Nov 9 23:00** (timeline re-audited: Instagram kickoff post + certificate + repo commits all agree). ₹30K / ₹20K / goodies.
- **Scale**: 1,318 registered, 280 players (national); 24 registered / 2 players on the combined Rajasthan+Assam+UP state listing (1175823).
- **Coordinators**: Soubhik Gon, Saswat Parasar Behera (both now Joint-Heads of the Programming Society, 2024–25).
- **Rules snapshot** (verified from the listing): ₹400/team, 2–4 members same state, 24h finals, **GitHub push required every 3 hours**, original work only, sleeper-fare reimbursement for non-Odisha teams, judging = creativity / technical complexity / practicality / presentation.
- **National winners (re-audited  -  previously unknown)**: **1st Wizard_Oz** (C.V. Raman Global University; real-time student sentiment analysis), **2nd Fork** (RVCE; AI thumbnail keyframe detection + emotion analysis + text-to-image). 3rd place never posted publicly. **MUJ did NOT win 2024**  -  that's the 2025 team.
- **State round (RVCE, Oct 23–24)**: food-safety theme, 3 tracks, 4×25% judging, top-2 advance. TrueMix (Bit-Binary-2027 / Chandan-Kr-dev) built there, carried to nationals.

### 2025  -  Rewind & Recode (D³ Fest, IIIT Bhubaneswar)
- **Run by**: Tech Society + TARS (Robotics) Society. State rounds → nationals Nov 7–9. ₹50K per state listing.
- **ELEVEN state rounds** (re-audited: was "4-5" in the first dossier): Rajasthan 706/147, Odisha host 231/40 (3-tier prizes), Karnataka 196/34, TN 182/20, Maharashtra 95/19, UP 59/10, Punjab 58/9, MP 21/3, Gujarat 16/1, Bihar 15/1, Jharkhand 13/1 → **1,592 reg / 285 players total**. Uniform ₹300 entry / ₹50K pool.
- **Nationals themes** (verified via LinkedIn sagarbm + RVCE post): **AI for Personal Development** + **Agentic Healthcare Systems**.
- **WINNER: Team Highlanders (MUJ!)** won the national finale (1,600–2,000+ teams) with **AFTERPACKETS**  -  Android VPNService + native C++ DPI parser + React web. The 7 challenges recovered verbatim (p-society/D3-2k25-solutions, in `research/raw/`): 1) NFT event ticketing, 2) Web3 loyalty cards, 3) P2P skill swap, 4) AI lecture generator, 5) Collegiate Inbox Navigator, 6) Automated Lab Grader, 7) **Mobile Packet Hunter** (= AFTERPACKETS' problem, the one that won). Phase 2: cross-chain auto-select, quest-map gamification, anonymity + replay, animated lectures, MCP server, load testing, interception layer.
- **D³ Fest 2025 pool ₹131K / 3,000+ participants**: VERIFIED via Scribd snippet (the Unstop listing 374277 is dead on the live API).

### 2026  -  Craft N Code (D³ Fest 2026, IIIT Bhubaneswar × state clubs)
- **Run by**: Tech Society IIIT-B (national) + Cyber Space Club MUJ (Rajasthan round). State rounds → nationals Oct 30 – Nov 1. ₹50K winner.
- **2026 state rounds found**: Rajasthan **1730314** (629 reg, watchdog 2026-08-15 10:04  -  biggest confirmed, down from 706 in 2025), UP **1730325** (1 reg, fresh). 17303xx range otherwise jobs/internships.
- **Sibling events at D³ Fest 2026** (official brochure): CTF Arena (cybersecurity battle), Workshop.exe (AI/Blockchain/Web3/AR/VR), UI/UX Showdown, TechXpo, Code-o-lympics, Dev Dialogue. 4-day fest, Tech + Robotics Societies.
- **Event site forensics**: the official site source is PUBLIC (Lovable, arcade theme, Supabase)  -  built by Rudra Pratap Singh (CSC dev). Admin console read-only, pitch-first; food route = UI mock. Renamed from "Rewind&Recode" Aug 9, 2026.

---

## 🕵️ The People (who's behind all this)

### CSC MUJ (Rajasthan round organizers)  -  `research/PEOPLE-DOSSIER-CSC.md`
- **Abhinav Trikha**  -  Chairperson 2026–27, pre-final B.Tech IT @ MUJ. +91 95994 15311, trikhaabhinav@gmail.com.
- **Ambika Seth**  -  Vice-Chairperson. **Spandan Hota**  -  Craft N Code contact; **Google Student Ambassador** (Sep 2025), intern @ Nursio Innovation. **Tirtha Desai**  -  contact; GitHub `TirthaDesai`.
- **Exec committee 2026–27**: 9 exec + 7 advisory + 10 heads + 19 joint heads + 18 coordinators (full roster in dossier). Faculty: Dr. Roheet Bhatnagar, Umashankar Rawat, Dr. Amit Kumar Bairwa.
- **CSC's other events**: NEXORA'26 (state-level online hackathon with Rabbitt AI, 261 participants, 48h, ₹10K pool, custom portal), Novus annual fest, Build Fest.

### Tech Society IIIT-B (national organizers)  -  `research/PEOPLE-DOSSIER-TECHSOC.md`
- **Soubhik Gon**  -  CraftNCode 2024 coordinator → Oracle intern → SWE @ Nasuni. GitHub `zakhaev26` (66 repos). 2nd place D3 Hackathon 2023.
- **Saswat Parasar Behera**  -  2024 coordinator → Creuto/Smarbl. **Swoyam Siddharth Nayak**  -  former Secretary → **SWE @ Sarvam AI** (CGPA 8.35, IEEE author). **Ehtisham Mohd**  -  Secretary 2024-25 → SWE @ Param.ai. **Sipra Mohanty**  -  GDSC Creative Lead → FDSE @ Sarvam AI. **Subrat Kumar Swain**  -  NCIIPC-AICTE PENTATHON finalist, police cyber intern → Sapiens. **Raj Alpha Swain**  -  EEE '25, CodeChef 3★.
- **The pattern**: a tight alumni chain  -  Swoyam → Ehtisham → Soubhik & Saswat  -  now across Sarvam AI, Param.ai, Oracle, Nasuni, Smarbl. These people know what winning looks like.

### The judges (2024/2025, taste profile)  -  `research/JUDGE-DOSSERIS.md`
- **Ayushi Parashar, Shivani Prasad, Sarthak Padhi, ACP Anjana Tudu (police), Lingaraj Sethi (cyber expert), Sonali Satpathy**  -  industry + police + cyber experts, 3-round funnel (114 → 21 → 8 → top 2).
- **What they reward** (2024 rulebook): creativity, technical complexity, practicality, presentation. Working demo > deck. Real-world impact framing wins. Security/safety themes land hard.

---

## 🏆 Winner Forensics (what actually won  -  and why)

### AFTERPACKETS  -  2025 national winner (Team Highlanders, MUJ)
Full codebase recovered from GitHub (`PrashamJ17/AfterPackets`, 201MB, created Nov 8 2025 = finals day):
- **Android app** (Kotlin, 40+ files): VPNService packet capture (no root), native C++ DPI parser (IP/TCP/UDP/ICMP/HTTP/DNS/TLS), Room DB, Jetpack Compose, WebSocket server, firewall rule engine, app-level tracking, geo map, PCAP/JSON export, consent + audit logging. **13 screens.**
- **Security alerts**: MITM, DNS spoofing, data exfiltration, ARP spoofing (severity levels).
- **Desktop web**: React 18 + Vite + TS + Tailwind + Zustand + three.js/globe.gl + Leaflet + Recharts + Express.
- **Why it won** (deep-dive in `research/WINNER-EXACT-DEEP-DIVE.md`): deepest stack + **ZERO external deps** (no OAuth/API keys/quota → demo ALWAYS worked) + security relevance + empty lane + live-demo visual. Commit workflow: core 06:56 → scope-down 07:17 (dropped geo-location, dropped desktop web app) → cleanup 07:26 → rebrand 08:01.
- **Repo hygiene**: TERRIBLE (committed .gradle, node_modules, .DS_Store, debug APK  -  201MB)  -  and they still won. **Clean repo = free points.**

### What LOST (counterfactual, `research/REJECTED-LOST-ENTRIES.md`)
- **PromptBuddy** (manaspros/code): war diary of Composio SDK bugs, Gemini 429 quota, 6 critical bugs fixed at 2am. External-dependency risk killed it.
- **EduSynth** (varunaditya27/EduSynth): 77MB production app, Gemini 2.5 Pro + FastAPI + Prisma + MoviePy  -  lost to the 201MB junk-committed Android app. Over-polish without lane differentiation.
- **R1 rejection patterns**: 404 repos (2/20), 18KB HTML-only repos, no deployment, weak pitch, crowded lanes.

### The winning formula (synthesized across 3 winner sets)
1. **AI/ML is non-negotiable** (every winner had it).
2. **Working demo beats deck**  -  judges poke and test.
3. **Real-world impact framing**  -  every winner mapped to a concrete human problem.
4. **Zero external dependencies in the demo**  -  no OAuth/API keys/quota to fail at 3 AM.
5. **Presentation polish wins ties**  -  3-minute demo discipline, one hero feature.

---

## 🔮 2026 Question Prediction (the edge)

Full matrix in `research/2026-TOPIC-PROBABILITY.md` (site track bodies kept for reference; they are the BACKUP SET per Rudra intel). The real prep is the company-lane protocol in `IDEA-BANK.md` §5: fingerprint table, cue table, setter prior (Google 24% > Accenture 22% > Meta 21% > Adobe 18% > Apple 15%), and the 3 predicted shapes from deep research (agentic ops / multimodal assistant / creative media workflow).

**Sponsor-to-shape map**: Google→agentic ops · Meta→multimodal assistant · Accenture→enterprise workflow · Adobe→creative media · Apple→mobile/accessibility.

**The 5 ranked predicted problems** (from `research/WAVE-SYNTHESIS.md`, INFERRED rehearsal only): 1) trustworthy agent with evidence + approval (Google/Accenture), 2) creative production agent with provenance (Adobe), 3) private personal intelligence on-device (Apple), 4) multimodal assistant on messaging with escalation (Meta), 5) governed enterprise case router (Accenture). All converge on ONE pipeline: input → extraction → evidence → ranking → proposed action → policy gate → human approval → audit trace. Our engine IS this pipeline; a skin = nouns + data + UI labels + provider adapter (15-40 min mount).

---

## 🌐 Participant Universe (the field)

- **2024**: 1,318 reg / 280 players (national); 24/2 (state combined). **2025**: 1,592 reg / 285 players across 11 state rounds; nationals 1,600–2,000+ teams. **2026**: Rajasthan 629 (watchdog 08-15 10:04, was 402/81 at README time), UP 1 (fresh). ~200 expected at the Rajasthan overnight.
- **GitHub-mapped repos**: 25+ across editions (see `research/PARTICIPANT-UNIVERSE.md`). Known 2025 solutions: TrustChain (rural microfinance blockchain), BitSized (shopping assistant), Innovize (student health portal), Quantum Glitch, Chetna. 2026 threat matrix in `research/COMPETITOR-POOL.md`.
- **The field is smaller this year** (629 and climbing vs 706 in 2025; was 402 at README write time)  -  the easiest qualifier in the event's history.

---

## 🗂️ Repo Layout

```
craft-n-code/
├── README.md                        ← this file (war-room index, fresh 2026-08-14)
├── CONTINUATION-PROMPT.md           ← handoff for a new window (read this first)
├── INDEX.md                         ← every file, one line each, what it's for
├── scaffold/                        ← ★ THE NIGHT'S WEAPON (verified 13/13)
│   ├── engine/engine.py             ← ingest → dedupe → summarize → rank → deadlines
│   ├── webapp/serve.py + static/    ← zero-dep server + dark UI
│   ├── deck/deck-gen.js + 4 .pptx   ← agentic/multimodal/creative/kavach
│   ├── demo.sh + README.md
├── docs/                            ← DEMO-STORYBOARDS.md, HARDWARE-GATE.md (archived)
├── research/
│   ├── MASTER-DOSSIER.md            ← everything in one file (tracks, timeline, sponsors, strategy)
│   ├── IDEA-BANK.md                 ← ★ THE crown jewel: pre-built answers for the 4 sponsor lanes
│   ├── CHEATSHEET-BRIEF.md          ← what matters, sponsor DNA, hottest tech
│   ├── WAVE-SYNTHESIS.md            ← 5 predicted shapes + gaps + execution plan
│   ├── company-lanes/               ← 6 deep-research reports (376K total)
│   ├── prompts/                     ← 6 re-fire prompts
│   ├── 2026-TOPIC-PROBABILITY.md    ← probability matrix (superseded by §5, kept for backup set)
│   ├── RE-AUDIT-FINDINGS.md         ← every correction made during the sweep
│   ├── 2025-STATE-SWEEP.md          ← the 11-round 2025 map + totals
│   ├── COMPETITIVE-INTEL-DOSSIER.md ← org lineage + editions + people + sponsors
│   ├── PEOPLE-DOSSIER-CSC.md        ← CSC MUJ full roster (18.7K)
│   ├── PEOPLE-DOSSIER-TECHSOC.md    ← Tech Society IIIT-B (23K, 38 claims)
│   ├── JUDGE-DOSSIERS.md            ← 6 judges + how-to-win matrix (ultra8x)
│   ├── WINNER-REVERSE-ENGINEERING.md← AFTERPACKETS stack + TrueMix + GENESIS + formula
│   ├── WINNER-EXACT-DEEP-DIVE.md    ← 13 screens, C++ parser, why-it-won, loser counterfactual
│   ├── REJECTED-LOST-ENTRIES.md     ← rejection patterns + 8-step R1 win formula
│   ├── COMPETITOR-POOL.md           ← 20-team threat matrix + empty-lane strategy
│   ├── PROBLEM-BANK-SPONSOR-DNA.md  ← 2024 rules + sponsor DNA + prep plan
│   ├── EVENT-SITE-FORENSICS.md      ← 5 tracks, overnight run, submission, canteen
│   ├── EVENT-SITE-FORENSICS-v4.md   ← admin console, submission flow, food mock
│   ├── RAJASTHAN-LISTING-1730314.md ← our round's full listing
│   ├── STATE-QUALIFIER-SCAN.md      ← 2026 state round scan
│   ├── 2024-STATE-QUALIFIER-FORMAT.md ← RVCE round: food-safety, 3 tracks, top-2
│   ├── 2025-FINALS-ROSTER.md        ← national finals roster
│   ├── PARTICIPANT-UNIVERSE.md      ← 25+ repos mapped across editions
│   ├── RABBITT-AI-DOSSIER.md        ← NEXORA partner company
│   ├── NEXORA-FORENSICS.md          ← NEXORA'26 portal forensics
│   ├── D3FEST-2022-PROBLEMS.md      ← D3 2022 problems (campus-tool family)
│   ├── D3FEST-2023-BROCHURE.md      ← D3 2023
│   ├── D3FEST-2026-BROCHURE.md      ← full 2026 lineup (CTF Arena, Workshop.exe...)
│   ├── BROCHURE-OCR.md              ← 2024/2025 brochure pages 1–2 + method
│   ├── GAP-MAP.md                   ← 20 gaps still diggable, tiered
│   ├── RECON.md                     ← base recon + sponsor-topic intel
│   ├── CNC-INTEL-EXECUTION-20260813.md ← execution log
│   ├── watch-state.json             ← watchdog state
│   └── raw/                         ← rnr-phase1/2.pdf + FULL verbatim 2025 statements
└── assets/                          ← deck, media, evidence
```

---

## 🛰️ Watchdog (automation)

- **craft-n-code-watch** cron (every 6h, no-agent mode): probes Unstop listing 1730314 (Rajasthan), 1730325 (UP), 1171379 (2024 national), 1175823 (2024 state), 1545708 (2025 RJ)  -  tracks register counts, flags judge/mentor/sponsor changes, watches for new state siblings in the 1730xxx range. State in `research/watch-state.json`. Silent when nothing changes.

---

## 📅 Timeline (IST, all verified)

```
Aug 14 23:59   registration deadline (DONE  -  team 511 in)
Aug 15 21:00   idea submission opens (Unstop)
Aug 15 21:30   ★ PROBLEM STATEMENTS DROP ★ (sponsor-written, decision tree fires)
Aug 16 06:00   idea submission closes
Aug 16 10:00   presentation to judges (MUJ)
Aug 16 17:30   presentation ends
Aug 30         IIC 3.0 results (R1, parallel track)
Sep 8–9        IIC R2 offline (if advanced)
Oct 30 08:00   national problem statements released (IIIT Bhubaneswar)
Oct 30 – Nov 1 national finals (24h overnight + judging)
```

## 🎯 Remaining Work (honest)

| Item | Who | Effort |
|---|---|---|
| Approval gate (typed tools, policy gate, audit trail) | Hermes + opencode | DONE, verified 13/13 (G1-G13) |
| Trace viewer + fixture replay (mode badge, /api/trace, 3 golden fixtures) | Hermes + opencode | DONE, verified 12/12 (T1-T6 + offline-key regression) |
| Rudra ask: 2025 Rajasthan state-round problems + judging format | User (can't do from phone) | 1 message |
| Demo videos (4× 3-min, screen + voiceover) | Team | ~1h each |
| Pitch rehearsal (2:30 target, hard timer) | Team | 30 min |
| Night flow: 21:30 drop → cue table (2 min) → decision tree (10 min) → pick idea → mount skin (15-40 min) → demo.sh → submit | All | 8.5h window |

---

## 🛡️ Rules of the Workspace

- **PRIVATE repo**  -  hackathon recon stays private.
- **No fake progress**  -  repo reflects true state, verified numbers only.
- **Version up, never delete**  -  every finding committed with a clear message.
- **Sources tagged**  -  VERIFIED / PARTIAL / NOT FOUND on every claim in the dossiers. Re-audits correct rather than defend.
- **The edge is information**  -  we know the tracks, the format, the judges' taste, the winners' stack, the canteen menu, and now the ideas. Tonight we build.

---

*Team 511  -  Harsh, Ayush, Sujal. Let's hack. 🎮*
