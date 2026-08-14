# Winner Reverse-Engineering  -  Craft N Code / D³ Fest Hackathons

Compiled: 2026-08-13 | Method: GitHub forensics (gh CLI), LinkedIn LD+JSON, rivalsearch

## 1. AFTERPACKETS  -  2025 National Winner (Team Highlanders, MUJ)

### The win
- 1st place among 1600-2000+ teams at Rewind & Recode National Hackathon (D³ Fest 2025, IIIT Bhubaneswar), Nov 7-9 2025.
- Team: Abhishek Chaturvedi, Prasham Jain, Hrishi Bhalaria, Tapish Thakur (all MUJ CSE).
- Project: mobile network traffic analysis + forensics platform.

### GitHub forensics (the actual code)
**PrashamJ17/AfterPackets** (created 2025-11-08 = FINALS DAY, 201MB, 2 stars, Java/Kotlin):
- Committed junk: .gradle caches, .cxx build dirs, .DS_Store, node_modules, .vite deps, a debug APK (mobile-packet-hunter-debug-current.apk). ZERO tests, ZERO CI. Classic hackathon-scrappy.
- Android app (Kotlin, 40+ files): VPNService-based capture (no root), native C++ DPI parser (packet_parser.cpp: IP/TCP/UDP/ICMP/HTTP/DNS/TLS), Room DB, Jetpack Compose UI, WebSocket server, firewall rule engine, app-level traffic tracking, location-based geo map, PCAP/JSON export, consent dialog + audit logging.
- Security alerts: MITM, DNS spoofing, data exfiltration, ARP spoofing, suspicious patterns (severity Low→Critical).
- Desktop web (React 18 + Vite + TS + Tailwind + Zustand): dashboard, import, geo map (globe.gl + three.js + Leaflet), timeline replay, rules builder. Express backend (multer uploads, cors).
- **hrishibhalaria/AfterPackets** + **Avshrek/AfterPackets** = same code (team copies).

### Why it won (deconstructed)
1. WORKING end-to-end product: real Android app (APK in repo) + web companion. Not a mockup.
2. Real-world problem: mobile network forensics (privacy/security visibility)  -  judges = cyber experts + police (ACP Anjana Tudu at Hackfest).
3. "Clarity, relevance, and execution" (winner's own words)  -  the README is a professional pitch.
4. Security-first framing: legal consent, audit logs, evidence bundles (forensic-grade).
5. Team was known: MUJ CSE dept celebrated them; Student Excellence Award from MUJ president.

## 2. TrueMix  -  2024 CraftNCode Participant (Bit-Binary-2027)

### The project
- Fact-checking platform: verify facts, read news, play games/quizzes. Gamification + leaderboard.
- **Bit-Binary-2027/CraftNCode** (created 2024-10-20, JavaScript): React frontend (Vite) + Express backend (Controllers/Models/Routes: Facts, Players, Users) + Python ML (LangDetect.joblib, Language-Detection.csv, detect.py) + Firebase.
- Team photos in repo: anuska.jpg, arna.jpg, chandu.jpg (3 members).
- **Chandan-Kr-dev/CraftNCode** + **Sapta-Dev27/TrueMix-CraftNCode-IIIT-BBS** = team member copies.

### Chandan Kumar (Chandan-Kr-dev)  -  the participant profile
- 34 public repos, created 2023-11. TMSL (GDG-ON-CAMPUS TMSL = Techno Main Salt Lake, Kolkata) involvement.
- Project history: EgramPanchayat (rural gov schemes), IIC-Job-dhundo (job portal), SIHJudicio (SIH project, frontend+backend), CVForge.ai, Health_Companion, Medical-Decentralized-App (Aptos blockchain), PragatiMeta, TalkWithMe (TS, 2026), Balance-3D (Unity/ShaderLab), Dragon-Slayer (Godot).
- Pattern: gov-scheme projects (Egram, SIH), hackathon circuit (IIC, SIH, CraftNCode, Hacktoberfest), full-stack JS + Python ML.

## 3. GENESIS  -  Hackfest 2024 Winner (SIT Bhubaneswar)

- Won Hackfest 2024 (Tech Society's own national hackathon, ADVITA 2024).
- Project: food distribution inefficiency solution  -  mobile app + dynamic web platform + advanced ML model for surplus food management.
- Social-impact framing (food waste) + working app + ML = the winning combo.
- Runner-up: TECHTITANS (IIIT-B).

## 4. The Winning Formula (across all editions)

| Factor | AFTERPACKETS 2025 | GENESIS 2024 | TrueMix 2024 |
|---|---|---|---|
| Working product | Android APK + web | mobile + web + ML | web + backend + ML |
| Real problem | network forensics | food waste | misinformation |
| ML/AI component | C++ DPI engine | ML model | LangDetect ML |
| Polish | professional README | social impact story | gamification |
| Team | 4 known MUJ students | SIT students | 3 students |

**Consensus**: working end-to-end build + real-world problem + ML/security depth + clear story. Scrappy code is FINE (all winners committed junk). The README IS the pitch.

## 5. What this means for Team 511

1. The bar is a WORKING demo (APK/web app), not a deck.
2. Security/network/forensics themes have won twice (AFTERPACKETS + Hackfest judges = cyber experts + police).
3. Sponsor companies (Google/Apple/FB/Accenture/Adobe 2026) will set the problem  -  build a flexible stack: React/Vite frontend + Express/FastAPI backend + ML component + mobile (Kotlin/Flutter) if feasible.
4. Commit clean (no .gradle/node_modules junk) = free points vs every past winner.
5. README as pitch: problem stats, features, quickstart, screenshots.
