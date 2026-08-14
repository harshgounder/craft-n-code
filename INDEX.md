# INDEX - every file in this repo, what it's for

Updated: 2026-08-14 09:56 IST

## Top level

| File | What it is |
|---|---|
| `README.md` | War-room home: status, competition, idea bank summary, edition history, people, winner forensics, topic probability, participant universe, layout, watchdog, timeline, rules |
| `CONTINUATION-PROMPT.md` | ★ Handoff for a new window: full context reset, immediate mission, next steps, key facts, operating rules. Read this FIRST in any new session |
| `INDEX.md` | This file |

## research/ - the intel

### Strategy & action
| File | What it is |
|---|---|
| `IDEA-BANK.md` | ★ THE playbook: pre-built ideas for the 4 sponsor-shaped lanes (IDEA A BriefLens, IDEA B Kavach Circle, IDEA C SignalStory, IDEA D Kavach), decision tree for the 21:30 drop, §5 company-lane protocol (Rudra intel: real questions come from sponsors, site tracks are backup), scaffold status, risk table, action plan |
| `prompts/company-lane-prompt.md` | Deep-research prompt: sponsor (Google/Apple/Meta/Accenture/Adobe) question-pattern intelligence, fired as parallel run `cnc-company-lanes` |
| `2026-TOPIC-PROBABILITY.md` | Probability matrix: verbatim track bodies, sponsor-to-track mapping, P(question lands) × P(we win), strategic read |
| `GAP-MAP.md` | 20 gaps still diggable, tiered execution order |
| `CNC-INTEL-EXECUTION-20260813.md` | Execution log of the intel campaign |
| `RE-AUDIT-FINDINGS.md` | Every correction from the Aug 14 re-audit sweep (11 rounds, 2024 winners, fee, timeline, pool) |
| `2025-STATE-SWEEP.md` | The 11-round 2025 map with reg/player counts + totals |

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
| `D3FEST-2022-PROBLEMS.md` | D3 2022 problems (the campus-tool family - PS-01 lineage) |
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

## docs/ + assets/

Empty, ready. docs/ = idea drafts + submission prep; assets/ = deck, media, evidence. First use: pre-recorded demo videos + deck skeleton per IDEA-BANK §6.

## Related repos (not in this tree)

- `~/iic-3` - IIC 3.0 project (R1 ends Aug 25, judge-watch cron live, decks filled)
- `~/muj-academics` - planner + drive sync (crons alive, verified Aug 13)
- `~/parallel-key-tracker` - 123 parallel keys (key#112 = ultra8x, used for dossiers)
- `~/.hermes/scripts/craft-n-code-watch.py` - watchdog (cron every 6h)
- Winner repos (read-only): PrashamJ17/AfterPackets, Bit-Binary-2027/CraftNCode, Chandan-Kr-dev, manaspros/code, varunaditya27/EduSynth, Rudra-25-12/CraftnCode-2026 (event site source), cyb3r17/rvce-craft-n-code
