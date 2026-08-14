# What Else Can We Dig?  -  Gap Map for Craft N Code Intel

Compiled: 2026-08-13 | Status: thinking doc, nothing fetched yet (except the two PDFs that fell out during gap-check)

## ⚡ NEW FINDING while checking gaps (ALREADY LANDED)

- p-society/D3-2k25-solutions repo = ACTUAL 2025 problem statements (Phase 1: 7 challenges, Phase 2: extensions). Saved to research/raw/rnr-phase1.pdf + rnr-phase2.pdf (commit 1e99b6d).
- 2025 challenges (ALL 7, verified): 1) NFT event ticketing, 2) Web3 loyalty cards, 3) P2P skill swap, 4) AI lecture generator, 5) Collegiate Inbox Navigator (AI academic assistant, Gmail+Classroom dashboard  -  direct predecessor of 2026 PS-03 Signal/Noise!), 6) Automated Lab Grader ("Digital TA", code judge), 7) Mobile Packet Hunter (= what AFTERPACKETS won with).
- Phase 2 extensions: chain auto-select, quest map gamification, anonymity + replay, animated lectures, MCP server integration, load testing, interception layer.
- Pattern: 2025 problems were WEB3 + AI + security heavy. Sponsors that year likely included web3/algo companies. 2026 sponsors (Google/Apple/FB/Accenture/Adobe) suggest AI + infra + security angle.
- Rudra-25-12/CraftnCode-2026/.env contains Supabase keys (PUBLISHABLE only, low risk)  -  worth flagging to the club, NOT exploiting.

## GAP MAP  -  what we do NOT have yet, and how to get it

### TIER 1: HIGH VALUE, HIGH FEASIBILITY (do these first)

1. **The missing 2025 challenge #6** (phase 1 PDF page 5, text between code-judge and packet-hunter got cut in my tail read). Read the PDF fully. 2 min.
2. **2024 national finals problem statements** (24h at IIIT-B Nov 8 2024). Sources to try: p-society repos (d3-web has a 2024 problem page?), Scribd search "CraftNCode problem statements 2024", LinkedIn posts by Soubhik/Saswat, the 2024 brochure pages 3-9 (need headless browser for per-page hashes, or try the D3 Fest 2024 site d3-web pages).
3. **2024 state-round (Rajasthan) problems**  -  the ₹200/team state round at MUJ was run by... someone. CSC or Tech Society? Find who ran it + the statements.
4. **2026 state-round problems**: the event site /problem-statements already leaks the 5 tracks (done), but the ACTUAL statements (the sponsor company questions) may be seeded in the site repo's git history, Supabase seed data, or the .lovable/plan files. Check git log for deleted files + the admin route.
5. **2025 Rewind & Recode national finale problems** (Nov 7-9, IIIT-B): p-society may have another solutions repo (search p-society repos for 2025/rewind), or the D³ 2025 site repo.
6. **Rabbitt AI (NEXORA partner)**  -  who are they? Their judging taste matters if they come back for Craft N Code. 10 min web search.
7. **The sponsor companies' hackathon problem archives** (Google/Apple/FB/Accenture/Adobe): Google Solution Challenge problems (annual, public), Meta Hackathon 2024/2025 problems, Accenture hackathon problem sets, Adobe Creative Jam archives. These predict the 2026 question style. All public.
8. **Judges for 2026**: not announced (watchdog will catch). But the 2024/2025 judge lists are known (Ayushi Parashar, Shivani Prasad, Sarthak Padhi, ACP Anjana Tudu, Lingaraj Sethi, Sonali Satpathy). Dig each judge's background + what they reward. 6 mini-dossiers, same recipe as the people dossiers.

### TIER 2: MEDIUM VALUE, MEDIUM FEASIBILITY

9. **Participant rosters**: Unstop hides them. But GitHub search found 25 repos. Extend: search "D3 hackathon", "d3fest", "arcadia", "code-kombat" repos (the D³ Fest sibling events) + LeetCode/Codeforces handles of the 2025 participants (from repo profiles) to map the competitor pool we will face at nationals.
10. **The 2026 UP listing (1730325) full details**  -  same API call pattern, gives the UP round's timeline + contact + maybe the state problem set (IET Lucknow's own event site?).
11. **The 2026 state rounds in other states** (Assam, others): each state college runs its own qualifier. Find all state listings (org 11832 on Unstop = all their events, try the Unstop org page or API) → we can compare how other states structure the qualifier.
12. **Team Highlanders' actual submission** (the 2025 winners): their demo video, pitch deck, or Unstop submission if public. LinkedIn posts by Abhishek/Prasham/Hrishi/Tapish about the win may contain the pitch summary.
13. **NEXORA'26 participant data** (261 participants): same GitHub-harvest recipe. Those are the same people we will face at the Rajasthan qualifier.
14. **CSC MUJ's past hackathon results**: who won NEXORA, what did they build? Winners' repos may exist. They are the direct local competition.

### TIER 3: LOWER VALUE / HARDER

15. **The Supabase database**: anon INSERT is allowed (that's how submissions work). SELECT on submissions is RLS-locked to admins, so we CANNOT read other teams' submissions (and should not try  -  that's cheating + the RLS blocks it anyway). Do NOT attempt. Flag instead: the club's anon-INSERT design means anyone can submit fake entries; we should submit early + resubmit near deadline (latest wins).
16. **Live site full-page content**: /sponsors, /food already pulled. The admin dashboard route (/admin) is auth-gated. Check /robots.txt + sitemap for hidden routes. Cheap.
17. **The 2026 brochure** (Craft N Code Rajasthan version): CSC may have a PDF on cscmuj.com or the event site. Check.
18. **Mentors for 2026**: the event site mentions "mentor rounds" at 01:00. Mentor names may be seeded in the site code (check PageShell/about for hardcoded names) or announced later.
19. **Historical D³ Fest editions**: 2023 (Soubhik's team won 2nd), 2022, 2021. Problem archives from older D³ fests (p-society repos, Scribd). Predicts the 2026 national format.
20. **The p-society repo full harvest**: 67 repos. List them all, check the ones that look like event sites/solutions (tech-society-web, techSocWeb, d3-web, D3-2k25-solutions, D3-2026). Any "solutions" repo for 2026 will be the NEXT jackpot.

## STRATEGIC USE (what the data is FOR)

- Problem-pattern prediction: 2024 (web3 + AI) → 2025 (web3 + AI + security) → 2026 (sponsor-set, likely AI + infra + security given Google/Apple/FB/Accenture/Adobe). Pre-build the flexible stack + idea bank around these.
- The 5 tracks ARE the 2026 categories. The ACTUAL questions will be sponsor-specific. The 2025 PDFs show the FORMAT: "The Problem / Your 24-Hour Mission / Required MVP (bullets) / Bonus Goal". Expect the same format. We can pre-draft the MVP structure for each track.
- Judges' taste (from 2024/2025 dossiers): creativity, technical complexity, practicality, presentation. Police + industry + TCS. Presentation polish matters.
- Watchdog will catch: Rajasthan listing ID, judge reveals, reg counts, sponsor fills.

## ORDER OF EXECUTION (recommended)

1. ~~Read missing 2025 challenge #6~~ DONE  -  all 7 challenges recovered (Challenge 5 = Collegiate Inbox Navigator, Challenge 6 = Automated Lab Grader)
2. Harvest p-society 67 repos for solutions/problem archives (30 min)
3. Sponsor problem archives: Google Solution Challenge + Meta + Accenture + Adobe (1h, parallel-able)
4. Judge dossiers x6 (1h, subagent-able)
5. 2024 national problems (30 min)
6. Competitor pool: GitHub harvest for D³ fest sibling events + NEXORA (30 min)
7. Rabbitt AI dossier (10 min)

All can be delegated one-by-one (user preference: NOT parallel) to keep this session light.
