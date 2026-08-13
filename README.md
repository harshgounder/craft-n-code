# Craft N Code — Rajasthan State Qualifier 2026

**Team 511's full-war-room workspace** for the Craft N Code Rajasthan State Qualifier, the gateway to the **Craft N Code National Finals at IIIT Bhubaneswar (Oct 30 – Nov 1, 2026)**.

> 🏆 **Mission**: win the Rajasthan qualifier, advance to nationals, take the national title back to MUJ (MUJ's Team Highlanders won the 2025 nationals with AFTERPACKETS — we intend to repeat).

---

## 📌 Status (2026-08-13, live-verified)

| Step | Status |
|---|---|
| Unstop registration (team **511**) | ✅ DONE |
| Registration fee paid | ✅ DONE |
| Idea submission (Aug 15 21:00 → Aug 16 06:00 IST) | ⏳ PENDING |
| Presentation to judges (Aug 16 10:00 → 17:30 IST) | ⏳ PENDING |
| National finals qualification (top 2 advance) | ⏳ PENDING |
| National finals (IIIT Bhubaneswar, Oct 30 – Nov 1) | ⏳ PENDING |

**Watchdog**: `craft-n-code-watch` cron (every 6h) probes Unstop for the Rajasthan listing ID, judge/mentor reveals, sponsor fills, and registration counts. Silent when nothing changes.

---

## 🎯 The Competition (verified)

| Field | Value |
|---|---|
| Full name | Craft N Code — Rajasthan State Qualifier |
| Organizer | Cyber Space Club, Manipal University Jaipur (in collab with IIIT Bhubaneswar, national host) |
| Location | Manipal University, Jaipur (hybrid mode) |
| Team size | 2–4 members |
| Prizes | ₹50,000 cash (winner) + certificates; national pool ₹50K+ |
| Registration deadline | **Aug 14, 2026 11:59 PM IST** |
| Idea submission | Aug 15, 9:00 PM IST → Aug 16, 6:00 AM IST (Unstop) |
| Presentation | Aug 16, 10:00 AM → 5:30 PM IST (judges) |
| National finals | IIIT Bhubaneswar, Oct 30 – Nov 1, 2026 (problems released 08:00 IST Oct 30) |

**Win condition**: advancing to nationals is the real prize. The ₹50K state pool is secondary; the national stage (24h overnight hackathon in front of industry leaders) is the target.

---

## ⚡ THE 5 TRACKS (2026 problem structure — LIVE-VERIFIED from the event site source)

The event portal (craftncode-2026.vercel.app, source public on GitHub) leaks the full track structure:

| ID | Title | The brief | Points |
|---|---|---|---|
| PS-01 | **Rewind the Legacy** | Take an outdated tool your campus still depends on and rebuild it for 2026. | 100 |
| PS-02 | **Night Ops** | Tooling for people who work odd hours — sleep, safety, focus, logistics. | 200 |
| PS-03 | **Signal / Noise** | Cut through information overload with search, summarisation or ranking. | 300 |
| PS-04 | **Open Track** | Anything you can justify in a 3-minute demo. Surprise the judges. | 400 |
| PS-05 | **Hardware Hack** | Sensors, microcontrollers, ugly wiring. Physical output required. | 500 |

**Rules of the game**: choose ONE track at check-in. Switching after the clock starts costs 30 minutes. Track points (100–500) are scoring weights, not prizes.

**The sponsor twist** (club-insider verified): the topic is NOT set by the club. The sponsor companies behind the hackathon set the questions — historically **Google, Apple, Facebook, Accenture & Adobe** (per CSC's official post). The 5 tracks are the categories; the sponsors drop the actual problem statements.

---

## 🌙 The Overnight Run (nationals format, live-verified from the event site)

| Time | Event |
|---|---|
| 20:00 | Check-in, team lock-in, opening brief |
| 21:30 | **Problem statements go live. Clock starts.** |
| 01:00 | Midnight fuel run + mentor rounds |
| 04:30 | Debug hour. *"The city is asleep, you are not."* |
| 09:00 | Freeze, demo, judging |

**Submission flow** (live-verified): deadline 09:00. One submission per team; resubmit allowed until the clock hits zero — latest entry wins. Fields: `team_name`, `track`, `repo_url`, `demo_url` (optional), `pitch` (1–2000 chars). Supabase backend.

**Night canteen** (live-verified — this is what 3 AM looks like): Midnight Maggi ₹40 (served 22:00–05:00), Cutting Chai ₹15 ("the primary compiler"), Cold Brew Shot ₹60, Paneer Roll ₹80 ("one-handed, keyboard safe"), Grilled Sandwich ₹70, Pizza Slice ₹90 ("reheated at 03:00, honestly still good"). Runners deliver every 20 minutes; pay at the counter.

---

## 👥 Team 511

| Member | Role |
|---|---|
| Harsh Gounder | Team lead — systems, orchestration, pitch |
| Ayush Kharwar | Build — backend, integrations |
| Sujal Shukla | Build — frontend, demo engineering |

---

## 📜 Edition History (who ran it, how many times, who won)

### 2024 — CraftNCode (D³ Fest, IIIT Bhubaneswar)
- **Run by**: Tech Society, IIIT Bhubaneswar (Unstop org 11832). State prelims (₹400/team) → 24h national finals at IIIT-B (Nov 8). ₹30K / ₹20K / goodies.
- **Scale**: 1,318 registered, 280 players (national); 24 registered / 2 players on the combined Rajasthan+Assam+UP state listing (1175823).
- **Coordinators**: Soubhik Gon, Saswat Parasar Behera (both now Joint-Heads of the Programming Society, 2024–25).
- **Rules snapshot** (verified from the listing): ₹400/team, 2–4 members same state, 24h finals, **GitHub push required every 3 hours**, original work only, sleeper-fare reimbursement for non-Odisha teams, judging = creativity / technical complexity / practicality / presentation.
- **Participant projects found on GitHub**: TrueMix (fact-check + news + games, Bit-Binary-2027 / Chandan-Kr-dev / Sapta-Dev27), Food Safety Compliance Predictor (YJ3003), plus QuantumRebels, RoguePlayerOne, PratyushPoddar07.

### 2025 — Rewind & Recode (D³ Fest, IIIT Bhubaneswar)
- **Run by**: Tech Society + TARS (Robotics) Society. State rounds → nationals Nov 7–9. ₹50K per state listing.
- **State participation**: Rajasthan 706 registered / 147 players; Punjab 58/9; Bihar 15/1; Tamil Nadu 182/20.
- **WINNER: Team Highlanders (MUJ!)** won the national finale (1,600–2,000+ teams) with **AFTERPACKETS** — a mobile Deep Packet Inspection platform (Android VPNService + native C++ DPI + React web). Members: Abhishek Chaturvedi, Prasham Jain, Hrishi Bhalaria, Tapish Thakur. MUJ took the national crown on their own campus qualifier.
- **The 7 challenges** (recovered from p-society/D3-2k25-solutions — the ACTUAL statements, in `research/raw/`): 1) NFT event ticketing, 2) Web3 loyalty cards, 3) P2P skill swap, 4) AI lecture generator, 5) Collegiate Inbox Navigator, 6) Automated Lab Grader ("Digital TA"), 7) **Mobile Packet Hunter** (= AFTERPACKETS' problem, the one that won).
- **Phase 2 extensions**: cross-chain auto-selection, quest-map gamification, anonymity + replay, animated lectures, MCP server integration, load testing, interception layer.

### 2026 — Craft N Code (D³ Fest 2026, IIIT Bhubaneswar × state clubs)
- **Run by**: Tech Society IIIT-B (national) + Cyber Space Club MUJ (Rajasthan round). State rounds → nationals Oct 30 – Nov 1. ₹50K winner.
- **Sibling events at D³ Fest 2026** (from the official brochure): CTF Arena (cybersecurity battle), Workshop.exe (AI/Blockchain/Web3/AR/VR), UI/UX Showdown, TechXpo, Code-o-lympics, Dev Dialogue. 4-day fest, Tech + Robotics Societies.
- **The 5 tracks** above are the state-round structure. Sponsors (Google/Apple/FB/Accenture/Adobe) set the questions. ~200 builders expected at the overnight event.

---

## 🕵️ The People (who's behind all this)

### CSC MUJ (Rajasthan round organizers) — full dossier in `research/PEOPLE-DOSSIER-CSC.md`
- **Abhinav Trikha** — Chairperson 2026–27, pre-final B.Tech IT @ MUJ, ex-Joint Head of Events. Contact: +91 95994 15311, trikhaabhinav@gmail.com.
- **Ambika Seth** — Vice-Chairperson, MUJ from Varanasi. Cyber awareness camp volunteer (May 2026).
- **Spandan Hota** — Craft N Code contact; **Google Student Ambassador** (selected Sep 2025), intern @ Nursio Innovation. spandanhota2005@gmail.com.
- **Tirtha Desai** — contact; GitHub `TirthaDesai` (6 repos matching CSC workshop sessions: flutter-session, ML-session, nodejs food app).
- **Exec committee 2026–27**: 9 exec + 7 advisory + 10 heads + 19 joint heads + 18 coordinators (full roster in dossier). Faculty coordinators: Dr. Roheet Bhatnagar, Umashankar Rawat, Dr. Amit Kumar Bairwa.
- **CSC's other events**: NEXORA'26 (state-level online hackathon with Rabbitt AI, 261 participants, 48h, ₹10K pool, custom-built portal), Novus annual fest, Build Fest.

### Tech Society IIIT-B (national organizers) — full dossier in `research/PEOPLE-DOSSIER-TECHSOC.md`
- **Soubhik Gon** — CraftNCode 2024 coordinator → Oracle Project Intern (Jan 2026) → SWE @ Nasuni. Top contributor of the D³ Fest 2024 website (40 commits). GitHub `zakhaev26` (66 repos). 2nd place, D3 Hackathon 2023.
- **Saswat Parasar Behera** — 2024 coordinator, CSE '26. GitHub `majorbruteforce` (@smarbltech), Devpost profile. Now at Creuto/Smarbl.
- **Swoyam Siddharth Nayak** — former Tech Society Secretary + Placement Coordinator, CSE '25 CGPA 8.35, IEEE author (pest detection), now **SWE @ Sarvam AI** (Samvaad conversational-agent platform, India's sovereign AI). The alumni chain's elder.
- **Ehtisham Mohd** — Secretary 2024–25 (succeeded Swoyam), Coding Ninjas SC lead, posted the CraftNCode 2024 promo publicly, now SWE @ Param.ai.
- **Subrat Kumar Swain** — Placement Coordinator, NCIIPC-AICTE PENTATHON 2024 Grand Finalist, cybersecurity intern at Commissionerate Police BBSR (mentored by ACP Anjana Tudu — who later judged Hackfest), now Associate Developer @ Sapiens.
- **Sipra Mohanty** — GDSC Creative Lead → GDG on Campus Organizer → FDSE @ Sarvam AI (Bulbul/Samvaad work).
- **Raj Alpha Swain** — EEE '25, CodeChef 3★ (raj2803), 39 repos.
- **D³ Fest 2026 web team**: Aman Raj (lead, CSE '28, FullStack intern @ Hana), Spandan Hota, Ajit Kumar Panigrahi, Hrusikesh Kar.
- **The pattern**: a tight alumni chain — Swoyam → Ehtisham → Soubhik & Saswat — now spread across Sarvam AI, Param.ai, Oracle, Nasuni, Smarbl. The 2024 coordinators built the D³ Fest 2024 site and won 2nd place at D3 2023. These people know what winning looks like.

### The judges (2024/2025, taste profile)
- **Ayushi Parashar, Shivani Prasad, Sarthak Padhi, ACP Anjana Tudu (police), Lingaraj Sethi (cyber expert), Sonali Satpathy** — industry + police + cyber experts, 3-round funnel (114 teams → 21 → 8 → top 2).
- **What they reward** (from the 2024 rulebook): creativity, technical complexity, practicality, presentation. Working demo > deck. Real-world impact framing wins.

---

## 🏆 Winner Forensics (what actually won — and why)

### AFTERPACKETS — 2025 national winner (Team Highlanders, MUJ)
Full codebase recovered from GitHub (`PrashamJ17/AfterPackets`, 201MB, created during the finals Nov 8 2025):
- **Android app** (Kotlin, 40+ files): VPNService packet capture (no root), native C++ DPI parser (IP/TCP/UDP/ICMP/HTTP/DNS/TLS), Room DB, Jetpack Compose, WebSocket server, firewall rule engine, app-level tracking, geo map, PCAP/JSON export, consent + audit logging.
- **Security alerts**: MITM, DNS spoofing, data exfiltration, ARP spoofing (severity levels).
- **Desktop web**: React 18 + Vite + TS + Tailwind + Zustand + three.js/globe.gl + Leaflet + Recharts + Express.
- **Repo hygiene**: TERRIBLE (committed .gradle, node_modules, .DS_Store, debug APK) — and they still won. **Clean repo = free points.** We do not have to match their code, we have to beat their demo polish.

### The winning formula (synthesized across 3 winner sets)
1. **AI/ML is non-negotiable** (every winner had an ML or AI component).
2. **Working demo beats deck** — judges are industry + police + cyber experts; they poke, they test.
3. **Real-world impact framing** — every winner mapped to a concrete human problem (surplus food, network forensics, fact-checking).
4. **Presentation polish wins ties** — 3-minute demo discipline, one clear hero feature.

---

## 🔮 Problem-Pattern Analysis (the edge)

The 2025 statements are the strongest predictor of 2026's format. Pattern across editions:

| Edition | Themes | Format |
|---|---|---|
| 2024 | web3 + AI + general | "The Problem / 24-Hour Mission / Required MVP / Bonus Goal" |
| 2025 | web3 + AI + security + edu | Same format, 7 challenges, Phase 1 + Phase 2 extensions |
| 2026 (expected) | AI + infra + security (sponsor-flavored) | Same format, sponsor-set questions on the 5 tracks |

**Direct mapping**: 2025 Challenge 5 (Collegiate Inbox Navigator — Gmail/Classroom AI dashboard) is the predecessor of 2026 PS-03 Signal/Noise. Expect the 2026 questions to rework 2025 challenges into sponsor flavors (Google → search/summarisation; Accenture → enterprise tooling; Adobe → creative/media; Apple → privacy/hardware-adjacent; Meta → community/social).

---

## 🌐 Participant Universe (the field)

- **2024**: 1,318 reg / 280 players (national); 24/2 (state combined).
- **2025**: Rajasthan 706/147, Punjab 58/9, Bihar 15/1, TN 182/20. Nationals 1,600–2,000+ teams.
- **2026**: UP listing live (1 reg, fresh — count will explode). ~200 expected at the Rajasthan overnight.
- **GitHub-mapped repos**: 25 across 2024/2025/2026 (see `research/PARTICIPANT-UNIVERSE.md`). Unstop hides rosters; GitHub is the only public window. Known 2025 solutions: TrustChain (rural microfinance blockchain), BitSized (shopping assistant), Innovize (student health portal), Quantum Glitch, Chetna.

---

## 🗂️ Repo Layout

```
craft-n-code/
├── README.md                        ← this file
├── research/
│   ├── MASTER-DOSSIER.md            ← everything, one file (5 tracks, timeline, sponsors, strategy)
│   ├── COMPETITIVE-INTEL-DOSSIER.md ← org lineage + editions + people + sponsors + participants
│   ├── PEOPLE-DOSSIER-CSC.md        ← CSC MUJ full roster + 4 organizer profiles (26 claims, 21 verified)
│   ├── PEOPLE-DOSSIER-TECHSOC.md    ← Tech Society IIIT-B (38 claims, 31 verified)
│   ├── WINNER-REVERSE-ENGINEERING.md← AFTERPACKETS full stack + TrueMix + GENESIS + formula
│   ├── PROBLEM-BANK-SPONSOR-DNA.md  ← 2024 rules + sponsor company DNA + prep plan
│   ├── EVENT-SITE-FORENSICS.md      ← the 5 tracks, overnight run, submission, canteen, build history
│   ├── PARTICIPANT-UNIVERSE.md      ← 25 repos mapped across editions
│   ├── D3FEST-2026-BROCHURE.md      ← full D³ Fest 2026 lineup (CTF Arena, Workshop.exe, UI/UX...)
│   ├── BROCHURE-OCR.md              ← 2024/2025 brochure pages 1–2 + method note
│   ├── GAP-MAP.md                   ← 20 gaps still diggable, tiered execution order
│   ├── RECON.md                     ← base recon + sponsor-topic intel
│   └── raw/                         ← rnr-phase1.pdf, rnr-phase2.pdf (ACTUAL 2025 statements)
├── docs/                            ← idea drafts, submission prep (next)
└── assets/                          ← deck, media, evidence
```

---

## 🛰️ Watchdog (automation)

- **craft-n-code-watch** cron (every 6h, no-agent mode): probes Unstop for the Rajasthan 2026 listing ID (probes the 1730xxx range around the known UP listing 1730325), tracks register counts on all known listings, flags judge/mentor/sponsor changes. State in `research/watch-state.json`. Silent when nothing changes.
- **Next planned**: idea bank + pitch templates for the 5 tracks (drop-ready for the Aug 16 presentation).

---

## 📅 Timeline (IST, all verified)

```
Aug 14 23:59   registration deadline
Aug 15 21:00   idea submission opens (Unstop)
Aug 16 06:00   idea submission closes
Aug 16 10:00   presentation to judges (MUJ)
Aug 16 17:30   presentation ends
Oct 30 08:00   national problem statements released (IIIT Bhubaneswar)
Oct 30 – Nov 1 national finals (24h overnight + judging)
```

---

## 🛡️ Rules of the Workspace

- **PRIVATE repo** — hackathon recon stays private (per GitHub visibility plan).
- **No fake progress** — repo reflects true state, verified numbers only.
- **Version up, never delete** — every finding is committed with a clear message.
- **Sources tagged** — VERIFIED / PARTIAL / NOT FOUND on every claim in the dossiers.
- **The edge is information** — we know the tracks, the format, the judges' taste, the winners' stack, and the canteen menu. Now we build.

---

*Team 511 — Harsh, Ayush, Sujal. Let's hack. 🎮*
