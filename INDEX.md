# INDEX - every file in this repo, what it's for

Updated: 2026-08-14 15:10 IST (re-audit refresh)

## Top level

| File | What it is |
|---|---|
| `README.md` | War-room home: status, competition, idea bank summary, edition history, people, winner forensics, participant universe, layout, watchdog, timeline, rules |
| `CONTINUATION-PROMPT.md` | ★ Handoff for a new window: full context reset, immediate mission, next steps, key facts, operating rules. Read this FIRST in any new session |
| `INDEX.md` | This file |

## scaffold/ - the night's weapon (verified 13/13 post-strip)

| File | What it is |
|---|---|
| `engine/engine.py` | ★ Domain-agnostic pipeline: ingest → dedupe → LLM summarize → rank → deadlines. LLM mode (ollama-cloud deepseek-v4-flash:0731) + full offline mode (regex dates + tf-idf + cache replay, zero deps). Demo never dies |
| `webapp/serve.py` | Zero-dependency python HTTP server: /api/stats, /api/digest, /api/search, /api/complaints (ticket flow) |
| `webapp/static/index.html` | Dark UI: "Today in 60 seconds" digest, 4 stat cards, 3 tabs (Feed/Ask/Requests) |
| `deck/deck-gen.js` | pptxgenjs skeleton → 4 sponsor-shaped decks (one source, 4 outputs) |
| `deck/deck-agentic.pptx` | IDEA A BriefLens deck (agentic ops, Google/Accenture DNA) |
| `deck/deck-multimodal.pptx` | IDEA B Kavach Circle deck (multimodal assistant, Meta DNA) |
| `deck/deck-creative.pptx` | IDEA C SignalStory deck (creative media workflow, Adobe DNA) |
| `deck/deck-kavach.pptx` | IDEA D Kavach deck (security lane) |
| `demo.sh` | One-command demo runner (generate feed + serve UI) |
| `README.md` | Scaffold usage: modes, seed data swap, deck regen, verification |

## docs/

| File | What it is |
|---|---|
| `DEMO-STORYBOARDS.md` | 4× 3-min storyboards (second-by-second voiceover scripts for pre-recorded videos) |
| `BUILD-SPEC.md` | ★ Plan-only spec for the 2 pending scaffold upgrades (approval gate + trace viewer/fixture replay): exact endpoints, table schemas, G1-G13/T1-T6 acceptance tests. Build awaits user go (asked 14 Aug, answer: hold builds) |
| `REPO-TOUR.md` | ★ The map: where everything lives and why, 30-second version + per-folder breakdown + reading order. Read this before anything else |
| `CODE-WALKTHROUGH.md` | ★ Every scaffold file explained function-by-function (engine.py, serve.py, index.html, deck-gen.js, demo.sh) + production lessons + how to audit the code yourself |
| `HARDWARE-GATE.md` | Archived option (PS-05 hardware sourcing checklist). NOT a track assumption - kept only as a what-if |

## research/ - the intel

### Strategy & action
| File | What it is |
|---|---|
| `IDEA-BANK.md` | ★ THE playbook: pre-built ideas for the 4 sponsor-shaped lanes (IDEA A BriefLens, IDEA B Kavach Circle, IDEA C SignalStory, IDEA D Kavach), decision tree for the 21:30 drop, §5 company-lane protocol (Rudra intel: real questions come from sponsors, site tracks are backup), scaffold status, risk table, action plan |
| `CHEATSHEET-BRIEF.md` | What matters most, what each sponsor makes/looks for (verified from their own hackathons), hottest tech for a 24h build |
| `WAVE-SYNTHESIS.md` | ★ Synthesis of the 4-run wave: 5 ranked predicted problem shapes, common denominator (one engine wins), 5 portable patterns, gaps table, 8.5h execution plan, zero-dependency rule, 10 questions to ask at reveal |
| `prompts/company-lane-prompt.md` | Deep-research prompt: sponsor question-pattern intelligence (run `cnc-company-lanes`) |
| `prompts/company-lane-prompt-2.md` | Pass-2 refire (run `cnc-company-lanes-2`, DEEP 90.1) |
| `prompts/sponsor-products-wave.md` | Wave prompt: sponsor product launches + verbatim problem shapes (run `cnc-sponsor-products`) |
| `prompts/winner-anatomy-wave.md` | Wave prompt: winner case studies + demo techniques (run `cnc-winner-anatomy`) |
| `prompts/problem-lanes-wave.md` | Wave prompt: evidence-mined most-likely problems + kill criteria (run `cnc-problem-lanes`) |
| `prompts/state-rounds-wave.md` | Wave prompt: state-round problem hunt (run `cnc-state-rounds`) |
| `2026-TOPIC-PROBABILITY.md` | Probability matrix: verbatim track bodies, sponsor-to-track mapping (SUPERSEDED by §5 company protocol; kept for the backup set) |
| `GAP-MAP.md` | 20 gaps still diggable, tiered execution order |
| `CNC-INTEL-EXECUTION-20260813.md` | Execution log of the intel campaign |
| `RE-AUDIT-FINDINGS.md` | Every correction from the Aug 14 re-audit sweep (11 rounds, 2024 winners, fee, timeline, pool) |
| `2025-STATE-SWEEP.md` | The 11-round 2025 map with reg/player counts + totals |

### Deep-research reports (company-lanes/)
| File | What it is |
|---|---|
| `company-lanes/cnc-company-lanes-pass1.content.md` | Pass-1 (65.5K, SURFACE): 5 named skins (BriefLens/Google, Kavach Swift/Apple, Kavach Circle/Meta, Kavach Ops/Accenture, SignalStory/Adobe), setter prior, 10-min cue table |
| `company-lanes/cnc-company-lanes-pass2.content.md` | Pass-2 (34.9K, DEEP 90.1, 111 cites): honest negative (no public proof of sponsor authorship), 3 ranked predicted prompt shapes, prep architecture, failure cases |
| `company-lanes/cnc-company-lanes-2.basis.json` | Pass-2 run basis (10.3K) |
| `company-lanes/cnc-sponsor-products.content.md` | Sponsor products wave (68K, ADECENT 230 cites): what each sponsor makes + looks for |
| `company-lanes/cnc-winner-anatomy.content.md` | Winner anatomy wave (62K, SURFACE 138 cites): winner common traits, zero-dependency rule |
| `company-lanes/cnc-problem-lanes.content.md` | Problem lanes wave (78K, ADECENT 333 cites): 5 ranked predicted problems + build cards + kill criteria + 5 portable patterns + 24h execution plan |
| `company-lanes/cnc-state-rounds.content.md` | State rounds wave (42K, ADECENT 125 cites): honest negative - no state-round problems publicly recoverable (Unstop cookie-blocked); 10 questions to ask the organizer |

### The competition
| File | What it is |
|---|---|
| `COMPETITIVE-INTEL-DOSSIER.md` | Org lineage + editions + people + sponsors + participants (the original big dossier) |
| `MASTER-DOSSIER.md` | Everything in one file: tracks, timeline, sponsors, strategy (v2) |
| `RECON.md` | Base recon + sponsor-topic intel |
| `RAJASTHAN-LISTING-1730314.md` | Our round's full Unstop listing (402 reg / 81 players, ₹299, contacts) |
| `STATE-QUALIFIER-SCAN.md` | 2026 state round scan (Rajasthan biggest, UP fresh) |

### People
| File | What it is |
|---|---|
| `PEOPLE-DOSSIER-CSC.md` | CSC MUJ: full 2026-27 roster (9 exec + 7 advisory + 10 heads + 19 joint + 18 coordinators), 4 organizer profiles, 26-claim verification table |
| `PEOPLE-DOSSIER-TECHSOC.md` | Tech Society IIIT-B: 7 mini-dossiers, 38-row verification (31 VERIFIED) |
| `JUDGE-DOSSERIS.md` | 6 judges (ultra8x run): backgrounds + how-to-win matrix |

### Winners & losers
| File | What it is |
|---|---|
| `WINNER-REVERSE-ENGINEERING.md` | AFTERPACKETS full stack + TrueMix 2024 + GENESIS 2024 + winning formula |
| `WINNER-EXACT-DEEP-DIVE.md` | AFTERPACKETS feature map (13 screens, C++ DPI parser), commit timeline, why-it-won argument, loser counterfactual (PromptBuddy, EduSynth) |
| `REJECTED-LOST-ENTRIES.md` | R1 mechanics (score 0-100, dup block), rejection patterns, 8-step R1 win formula |
| `COMPETITOR-POOL.md` | 20-team threat matrix + empty-lane strategy |
| `PARTICIPANT-UNIVERSE.md` | 25+ participant repos mapped across editions |

### Problems & format history
| File | What it is |
|---|---|
| `PROBLEM-BANK-SPONSOR-DNA.md` | 2024 full rules + sponsor company DNA + prep plan |
| `2024-STATE-QUALIFIER-FORMAT.md` | RVCE round: food-safety theme, 3 tracks, 4×25% judging, top-2 advance |
| `2025-FINALS-ROSTER.md` | 2025 national finals roster |
| `D3FEST-2022-PROBLEMS.md` | D3 2022 problems (the campus-tool family) |
| `D3FEST-2023-BROCHURE.md` | D3 2023 |
| `D3FEST-2026-BROCHURE.md` | Full D³ Fest 2026 lineup: CTF Arena, Workshop.exe, UI/UX Showdown, TechXpo, Code-o-lympics, Dev Dialogue |
| `BROCHURE-OCR.md` | 2024/2025 brochure pages 1-2 OCR + method note (pages 3+ unrecoverable) |

### Event site forensics
| File | What it is |
|---|---|
| `EVENT-SITE-FORENSICS.md` | 5 tracks verbatim, overnight run, submission flow, canteen menu, build history (v1-v3) |
| `EVENT-SITE-FORENSICS-v4.md` | Admin console (read-only, pitch-first), submission = plain INSERT (resubmit = new row, 23505 dup block), food route = UI mock |

### Companies
| File | What it is |
|---|---|
| `RABBITT-AI-DOSSIER.md` | Rabbitt AI (NEXORA partner): seed $2.1M TechCurators, Harneet Singh (IIT-D), ChanceRAG/DRIP |
| `NEXORA-FORENSICS.md` | NEXORA'26 portal: 6 tracks, Jury Score + redacted review + leaderboard, submission reqs |

### Raw & state
| File | What it is |
|---|---|
| `raw/rnr-phase1-full.txt` | ★ 2025 Phase-1 problems, FULL verbatim (7 challenges, exact MVP bullets) |
| `raw/rnr-phase2-full.txt` | ★ 2025 Phase-2 extensions, FULL verbatim (7 extensions) |
| `raw/rnr-phase1.pdf` / `rnr-phase2.pdf` | Source PDFs |
| `raw/rabbitt-runs.json` / `rabbitt-content.json` / `basis.json` | ultra8x parallel runs for Rabbitt + judge dossiers |
| `watch-state.json` | Watchdog state (last probe results per listing) |
| `INTEL-20260814-EVENING.md` | Live API findings: submission = PPT-only (pdf/pptx 50MB, multi-submit allowed), judge buttons (shortlist/reject/hold/noshow), score /5 weighted 100, D3 site live (d3fest.techsoc-iiitbbsr.com), 456 reg, Tirtha Desai new contact |

## Related repos (not in this tree)

- `~/iic-3` - IIC 3.0 project (R1 ends Aug 25, judge-watch cron live, decks filled)
- `~/muj-academics` - planner + drive sync (crons alive, verified Aug 13)
- `~/parallel-ai-stack` - deep-research launcher (pro-fast) + watcher + run-ledger (43/103 keys alive)
- `~/Desktop/parallel spams` - 130 parallel keys (newest at BOTTOM)
- `~/.hermes/scripts/craft-n-code-watch.py` - watchdog (cron every 6h)
- Winner repos (read-only): PrashamJ17/AfterPackets, Bit-Binary-2027/CraftNCode, Chandan-Kr-dev, manaspros/code, varunaditya27/EduSynth, Rudra-25-12/CraftnCode-2026 (event site source), cyb3r17/rvce-craft-n-code
