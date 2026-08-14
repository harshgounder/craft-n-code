# RE-AUDIT FINDINGS  -  corrections + new data (sweep 2026-08-14)

Compiled: 2026-08-14 | Method: live API re-fetches, ID-range sweeps, Instagram/LinkedIn/Scribd verification

## 1. CORRECTIONS (old dossier was WRONG)

### 1a. 2025 state rounds: 9, not 4-5
Old: "Rajasthan/Punjab/Bihar/TN/UP/Odisha"
Real (all live-verified): Rajasthan 706/147, Karnataka 196/34, Tamil Nadu 182/20, Maharashtra 95/19, UP 59/10, Punjab 58/9, MP 21/3, Gujarat 16/1, Bihar 15/1
- Odisha was NOT a state round (host state, nationals at IIIT-B)
- All rounds: ₹300 fee, ₹50K winner prize (uniform)
- TOTAL: 1,348 reg / 244 players

### 1b. 2024 national winners (NEW, verified via d3fest.iiitbh Instagram)
- 1st: Wizard_Oz (C.V. Raman Global University)  -  real-time student sentiment analysis for learning engagement
- 2nd: Fork (RVCE)  -  AI thumbnail keyframe detection + emotion analysis + text-to-image generation
- Finalists: team Loopception (Sambhav Shadangi, certificate on Scribd), Top-10 teams incl. Ravivarman B + Priyadharshini D (100+ teams)
- **MUJ did NOT win 2024. MUJ (Highlanders) won 2025.** The CSC post "Last year MUJ students won it" = 2025, correct.

### 1c. Fee discrepancy RESOLVED
- Live API payment_services: 2026 Rajasthan = ₹299 (CSC post RIGHT, ₹699 was wrong tier)
- 2024 national = ₹200, 2024 state = ₹400, 2025 states = ₹300, 2026 UP = ₹299

### 1d. D3 Fest 2025 listing 374277 = DEAD (404)
- The "3,000+ participants, ₹131K pool" claim came from the 2025 brochure (Scribd 917484478)  -  the brochure text layer was unrecoverable, so this claim is UNVERIFIED (from search snippets only). Flagged, not confirmed.

## 2. NEW DATA (sweep finds)

### 2a. 2026 field comparison
- Rajasthan 2026: 402 reg / 81 players (vs 706/147 in 2025)  -  SMALLER field
- UP 2026: 1 reg (vs 59/10 in 2025)  -  just launched
- Real competition at the event: ~30 teams (players_count funnel)

### 2b. 2024 national timeline (from repo forensics + Instagram)
- TrueMix team (Bit-Binary-2027): started Oct 23 2024 (RVCE state round), carried to nationals Nov 8-9 (CodeNCraft-Demo "Final Push" Nov 9 08:03)
- The 2024 finals: kicked off 11 PM Nov 8, 24h format (Instagram DCmUDxPN4eu: "As the clock struck 11 PM, Craft-N-Code  -  the ultimate 24-hour national hackathon  -  kicked off"), ended Nov 9
- The "8th-10th October" in the winner post = D3 Fest dates, NOT the hackathon. The certificate (Nov 8) + repo commits (Nov 9) are the ground truth.
- 3rd place: never posted publicly (only 1st/2nd on Instagram)

### 2c. 2024 national problems: still not public
- The 2024 problems were released on-site at the finals (24h format)
- The RVCE state round (Oct 23-24) theme = "AI and Big Data for food safety" (verified from cyb3r17/rvce-craft-n-code README)

### 2d. 2025 nationals themes (VERIFIED, LinkedIn sagarbm + RVCE post)
- The 2025 national finals (Nov 7-9) themes: **AI for Personal Development** + **Agentic Healthcare Systems**
- The Karnataka state round (RVCE Coding Club, Sep 27-28 2025, online): same themes, ₹50K+, top 2 → nationals with free travel/food/stay
- This confirms the state-round structure: each state club runs its own round, top 2 advance, nationals have 2-3 themes
- 2026 nationals (Oct 30-Nov 1): themes NOT yet public (released 8:00 AM IST Oct 30 per listing)

## 3. VERIFIED-CLEAN CLAIMS (re-checked, still true)

- 2025 winners: Team Highlanders (MUJ) with AFTERPACKETS  -  VERIFIED (roster + repo + commit dates)
- 2025 problem statements: all 7 + phase 2  -  VERIFIED (p-society PDFs)
- 2026 5 tracks + timeline + submission flow  -  VERIFIED (live site)
- 2026 Rajasthan listing 1730314, 402 reg, ₹50K, contacts  -  VERIFIED (live API)
- Sponsors set the questions (Google/Apple/FB/Accenture/Adobe)  -  VERIFIED (CSC post)
- Judges (Hackfest 2024): Anjana Tudu, Lingaraj Sethi, Sarthak Padhi  -  VERIFIED (ultra8x)
- Rabbitt AI: seed $2.1M, Harneet, NEXORA'26 mechanics  -  VERIFIED (ultra8x)
- NEXORA'26: 261 reg, ₹10K pool, 6 tracks  -  VERIFIED (live site + ultra8x)

## 4. REMAINING GAPS (honest)

- 2024 national problem statements: NOT public (on-site release)
- 2025 D³ Fest total pool (₹131K): UNVERIFIED (brochure text unrecoverable)
- 2026 Rajasthan judges: not revealed yet (watchdog watching)
- 2026 other state rounds: not listed yet (watchdog probing)
- 2024 3rd place: not found (only 1st/2nd posted)
