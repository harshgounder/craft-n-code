# Competitor Pool  -  2025 Finalists + NEXORA + 2024 (deep-dive)

Compiled: 2026-08-13 | Sources: GitHub commit forensics, repo metadata, READMEs

## 1. THE WINNERS' WORKFLOW (AFTERPACKETS commit forensics  -  VERIFIED)

Commit timeline (finals day, Nov 8 2025, freeze 09:00):

| Time | Commit | What it means |
|---|---|---|
| 06:56 | Initial commit | The build was done BEFORE the public commits  -  they committed the finished app |
| 07:17 | "Remove geo-location features from README" | SCOPE DOWN #1  -  cut a feature from the story |
| 07:26 | Delete debug APKs (cursor-mph-v1.apk, mobile-packet-hunter-debug.apk) | Cleanup  -  no junk in the submission |
| 08:01 | "Rename project from Mobile Packet Hunter to AFTERPACKETS" | REBRAND mid-hackathon  -  the name change happened 1h before freeze |
| 08:11 | "Remove Desktop Web App documentation" | SCOPE DOWN #2  -  dropped the web app from the story entirely |
| (next) | Apr 2026 README update | Nothing for 5 months  -  they shipped and stopped |

**The winning pattern:**
1. Build the core FIRST (the Android DPI engine), commit it whole
2. CUT features aggressively in the final hours (geo-location, desktop web app)
3. REBRAND for impact (Mobile Packet Hunter → AFTERPACKETS  -  a name that sounds like a product)
4. Clean the repo (delete debug APKs)
5. The story they told at 09:00 was SMALLER than what they built  -  focused, not sprawling

## 2. THE 2025 FINALISTS (20 teams, from p-society/D3-2k25-solutions)

Full roster + challenge mapping + tech stacks in 2025-FINALS-ROSTER.md. Key competitors:

| Team | Project | Challenge | Stack | Threat level |
|---|---|---|---|---|
| Highlanders | AFTERPACKETS | 7 (packet hunter) | Kotlin/C++/React | WON  -  the benchmark |
| Kon'nichiwa sekai | PromptBuddy | 5 (inbox navigator) | TS, Gemini 2.0 Flash + Composio | HIGH  -  AI-native, real integrations |
| Team CogniCode | EduSynth | 4 (lecture gen) | FastAPI + Next.js 16 + React 19 | HIGH  -  polished, animations |
| CodeX | SwapX | 3 (skill swap) | TypeScript | MEDIUM |
| Voxforge | Evalo | 6 (lab grader) | TypeScript | MEDIUM |
| Lone Wolf | digital-lab-grader | 6 (lab grader) | JavaScript | MEDIUM |
| Marine Drive | Acadify | 4/5 | TypeScript | MEDIUM |
| Hackasauras | Drawisly | 5/7 | TypeScript | MEDIUM |
| SentinelX | swap-sphere | 3 | TypeScript | MEDIUM |
| Magic Monks | Maven | 1/2 | JavaScript | LOW |
| Raccoon Fanclub | Codemia | 6 | JavaScript | LOW |
| Resolvers | DigiGrade | 6 | JavaScript | LOW |
| DIAMOND | Project_Kaushal | 2 | JavaScript | LOW |
| AgroFast | VedaScore | 2/5 | HTML | LOW |
| GITLERS | swapp | 3 | HTML | LOW |
| Just-Git-Gud | LECTRA | 4 | Python | LOW |

## 3. NEXORA'26 (the MUJ dress rehearsal)

- 261 registrations, Rajasthan-only, online, June 20-21 2026
- 6 tracks (Cybersecurity, Health Tech, Education Innovation, Data Driven, Smart Governance, Open Innovation)
- Winners NOT named publicly  -  but the format + judging stack are now known (NEXORA-FORENSICS.md)
- The 1st-place team was promised a Rabbitt AI Delhi finale slot
- Abhinav Trikha (President) + Harshit Raj Singh (Tech Sec) ran it  -  same people judging Craft N Code

## 4. THE 2024 STATE WINNERS (who advanced to nationals)

- RVCE round: top 2 advanced (food safety theme). 5 solutions mapped (2024-STATE-QUALIFIER-FORMAT.md)
- TrueMix (Bit-Binary-2027)  -  fact-check + news + games platform, React/Express/Python, Gemini 1.5 Flash
- The 2024 national winner: NOT publicly named (only 2025's Highlanders confirmed)

## 5. COMPETITOR INTELLIGENCE SUMMARY

1. **The 2025 winner's edge was DEPTH + SCOPE-DOWN, not breadth.** They built one hard thing (native DPI) and cut everything else.
2. **The AI-native teams (PromptBuddy, EduSynth) were the closest challengers**  -  Gemini + Composio integrations, polished UX. The 2026 sponsors (Google/Apple/FB/Accenture/Adobe) will reward exactly this.
3. **The crowded lanes lose.** 2025: lab grader (5 teams) and skill swap (4 teams) were the most crowded; the winner took the 1-team lane. 2026: expect PS-01 (Legacy) and PS-03 (Signal/Noise) to be crowded; PS-05 (Hardware) and PS-04 (Open) are the empty lanes.
4. **The club's judging stack is proven** (Jury Score, redacted review, leaderboard)  -  the Aug 16 presentation will use it.
5. **Repo hygiene matters more than it should.** AFTERPACKETS won with a 201MB repo full of node_modules  -  but they CLEANED the visible junk (debug APKs) before freeze. A clean repo = free points.
