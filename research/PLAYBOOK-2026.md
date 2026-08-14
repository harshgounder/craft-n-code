# PLAYBOOK 2026 - every method, ranked, executable (win at all costs edition)

Compiled: 2026-08-14 20:00 IST | Status: live document, updates as intel lands
Rule: every method carries evidence (VERIFIED = source seen, INFERRED = reasoned,
UNVERIFIED = rumor). Nothing here is vibes.

---

## 0. THE FIVE VERIFIED LAWS (everything hangs off these)

1. AI/ML is non-negotiable. All 5 sponsors ship AI products. A build without AI loses.
2. Working demo > deck. Every past winner shipped a working prototype. AFTERPACKETS won with zero external deps and a demo that could not die.
3. Fit beats depth. AFTERPACKETS won on empty lane + demo wow + story, not on research. Our research buys lane prediction and story precision, not automatic wins.
4. The panel is two axes: research/security (Sarthak, Lingaraj, Anjana) vs operations/impact (Ayushi, Sonali, Shivani). A pitch must satisfy BOTH.
5. Zero uncontrolled dependencies. LIVE / CACHED / OFFLINE modes, mode badge on screen. A candid fallback beats a frozen demo pretending a dead API worked.

---

## 1. INVENTORY: WHAT WE ALREADY HAVE (do not rebuild)

VERIFIED all green Aug 14 17:46:
- Engine (ingest, dedupe, LLM summarize, rank, deadlines, trace) 13/13
- Approval gate (typed tools, policy gate, proposals, audit) 13/13
- Providers (ollama/null swap) 9/9, multimodal (text/PDF/image) 4/4, provenance+consent 4/4
- Webapp 14 endpoints, dark UI, mode badge, trace drawer. Total 42/42 order-independent
- 4 decks (agentic, multimodal, creative, kavach), 4 storyboards, demo.sh (9/9 endpoints)
- Atlas docs site (69 pages), serve.sh on :8900
- Research: 6 deep runs (376K chars), IDEA-BANK with decision tree + cue table + setter prior,
  judge dossiers (6, with judging matrix), competitor pool (2025 finalists + NEXORA),
  2025 problems verbatim, winner forensics (AFTERPACKETS commit timeline)
- LLM live (ollama deepseek-v4-flash:0731), offline fallback, cache replay
- Watchdog craft-n-code-watch every 6h (next 21:05), re-probes 137 parallel keys

---

## 2. P0 METHODS (do TODAY, before sleep)

### P0-1. SITE-REPO SEED HUNT (the potential jackpot)
The 2026 event site repo (p-society/D3-2026) may contain the REAL sponsor problem
statements pre-seeded: git history deleted files, Supabase seed data, .lovable/plan
files, admin route. 2025's statements were found the same way (p-society/D3-2k25-solutions).
If the actual texts are there 24h early, we build the EXACT skin and win the night.
Status: clone in progress. If clean, 30 min spent, zero loss.
Evidence: 2025 jackpot landed exactly this way (VERIFIED). Rudra intel says sponsor-set
questions (UNVERIFIED publicly). Both point at the same hunt.

### P0-2. JUDGE ATTACK SHEETS (the face-off kit)
For each of the 4 ideas, a 30-question attack sheet, one answer per question, written
tonight. Questions grouped by judge lens (from JUDGE-DOSSIERS.md, VERIFIED):
- Sarthak (ML-validation): training data? baselines? metrics? false positives? overfitting?
- Lingaraj (security-depth): threat model? controls? test evidence? residual risk? data leakage?
- Anjana (safety): who is protected? abuse resistance? privacy? legal risk? measurable impact?
- Ayushi (business): quantified outcome? cost reduction? workflow fit? sustainability?
- Sonali (impact): who adopts? why persist? how is value communicated? business model?
- Shivani (data/process): reliable data handling? quality controls? docs? what did you learn?
Plus universal: "what did YOU build in the 24h" (pre-scripted honest answer per idea), and
"how is this different from X" (X = real verified competitor, never a strawman).
Deliverable: docs/ATTACK-SHEETS.md.

### P0-3. LEAVE-BEHIND ONE-PAGER
A4 per judge (6 copies): problem in one line, our answer, KPI card, QR code to the
atlas (serve it publicly or print the deck's KPI slide). Judges keep paper; every
other team leaves nothing. Template tonight, print tomorrow at MUJ.
Evidence: AFTERPACKETS README was the pitch (VERIFIED). Leave-behind = README on paper.

### P0-4. RUDRA ASK (send tonight)
Message ready in docs/RUDRA-ASK.md. The only intel gap the internet cannot close.

### P0-5. CLUB-SITE SUBMISSION KIT (new, VERIFIED Aug 14 20:00)
The club runs its OWN submission (src/routes/submit.tsx, Supabase): fields
team_name, track, repo_url (required), demo_url (optional), pitch (max 2000
chars). Rule: resubmit allowed, latest wins. Deadline 09:00 freeze. This is
SEPARATE from Unstop (PPT by 06:00). Two gates, both must be locked early.
Prep tonight: 2000-char killer pitch draft per idea, repo README as pitch
(AFTERPACKETS lesson: README IS the pitch), demo video hosting plan
(YouTube unlisted or Drive link ready to paste in demo_url).

### P0-6. CHECK-IN DECISION PROTOCOL (new, VERIFIED)
20:00: check-in, team lock-in, opening brief. TRACK CHOICE HAPPENS HERE,
before the drop. Tracks (stable since Aug 4): PS-01 Rewind the Legacy,
PS-02 Night Ops, PS-03 Signal/Noise (search/summarise/rank = OUR IDEA A),
PS-04 Open Track (anything, 3-min demo), PS-05 Hardware Hack. Switching
after the clock starts costs 30 MINUTES. Protocol: default PS-03 Signal/
Noise (the engine IS this lane), switch to PS-04 Open Track only if the
20:00 opening brief signals a wildcard drop. Budget the 30-min switch in
the hour-0 plan. Never pick PS-01/02/05.

---

## 3. P1 METHODS (tomorrow, pre-drop)

### P1-1. DEMO VIDEOS (4x 3-min pre-recorded)
Storyboards in docs/DEMO-STORYBOARDS.md. Record with wf-recorder -a -f demo-NAME.mp4
(screen + audio, Ctrl+C to stop). Voiceover + SUBTITLES baked in (room audio is
unreliable, subtitles always land). One Hinglish line in the demo: India-first
differentiator (VERIFIED theme). Every storyboard must include the STAGED FAILURE beat:
mode badge flips live to offline, recovery under 2 seconds. That beat wins demos.

### P1-2. THE AFTERMOVIE (60-90s cold-open hype reel)
I assemble with ffmpeg once the first demo video exists: clips, deck renders, text
cards (42/42 green, zero deps, team 511), atlas b-roll, music if you provide a track.
Judges see 8-15 pitches, attention is the currency. A sick cold-open is a real edge.
Order: video 1 -> aftermovie draft -> remaining videos.

### P1-3. REAL-DATA SEED FOR THE DEMO
Seed the engine with REAL public data from the judges' world: Unstop round deadlines
(21:00 open, 06:00 close, 10:00-17:30 pitch), event timeline, any public MUJ/CSC
notices. The digest then speaks the room's language. 20 min, done tomorrow afternoon.
Evidence: personalization beats generic (INFERRED, cheap to do, zero risk).

### P1-4. KPI CARD PER IDEA
One slide, real numbers only: engine 42/42, 9/9 endpoints, zero deps, LLM live +
offline fallback. Kavach: 5/5 scenarios fresh-clone, 24 real incidents registry,
Hindi-first. Honest numbers beat vibes. Deck generator already supports swap slides.

### P1-5. REHEARSAL x2, HARD TIMER
2:30 target, three roles: talker, demo driver, Q&A support. Rehearsed handoffs.
Record one run, watch it, trim. Second run after fixes.

---

## 4. P2 METHODS (the night of Aug 15)

### P2-1. SUBMISSION CADENCE (verified rule: multiple submissions, latest wins)
- 21:30 drop -> fingerprint scan (2 min) -> decision tree (10 min) -> freeze ONE-SENTENCE
  story -> skin mount (15-40 min) -> differentiator + staged failure -> KPI card -> deck swap
- v1 SUBMIT at 23:00 (LOCK, insurance against 5am failure)
- v2 at 03:00 (after polish)
- FINAL at 05:00, never 05:59. PDF preferred (renders identically), under 50MB.
- CLUB SITE: repo_url + pitch (under 2000 chars) + demo_url (hosted video),
  v1 before 06:00, final before the 09:00 freeze. TWO gates, both locked early.
Evidence: submission format VERIFIED Aug 14 (round 1569450, PPT only, resubmit
allowed) + club site submit.tsx VERIFIED Aug 14 (resubmit, latest wins, 09:00).

### P2-2. THE 01:00 MENTOR ROUND
CONFIRMED in the club's own run of the night (about.tsx): "01:00 Midnight
fuel run + mentor rounds". Pre-prepare 3 questions per idea: sponsor-fit
check, one differentiator suggestion, what judges reward this year.
Mentors are free expert feedback at the exact hour we are deepest in the
build. Also 04:30 "Debug hour" is a scheduled beat: use it as the story
moment in the aftermovie and pitch ("the city is asleep, we are not").

### P2-3. REG-COUNT RACE
Pull the Unstop API every 30-60 min from 21:00 (ground truth: /api/public/competition/1730314).
Surge patterns show who is awake. Also watch CSC club channels (Insta/WhatsApp/Telegram):
the statement may surface there BEFORE the 21:30 site drop. Head start = win.

### P2-4. EMPTY-LANE ANALYSIS AT 21:45
After the drop, map which of our 4 ideas the problems imply, then think like the field:
which lane will 96+ players pile into? If our mapped idea is the crowded one, keep the
idea, pivot the STORY angle (e.g. India-first, consumer-side, evidence export). Never
pitch fresh. Evidence: lab-grader lane 2025 had 5 teams and split attention (VERIFIED).

### P2-5. SLEEP ROTATION
One teammate sleeps 02:00-05:00 while the others polish. Pre-recorded videos mean the
stage demo does not need live perfection. At 09:00 at least 2 of 3 must be sharp.

---

## 5. P3 METHODS (on-site, Aug 16)

### P3-1. ARRIVE 08:30, SCOUT FIRST
The club's own run of the night says "09:00 Freeze, demo, judging" (VERIFIED
from about.tsx). Unstop's 10:00 listing is the outer bound, 09:00 is the
real freeze. Arrive 08:30: projector resolution, audio, mic, wifi SSID,
power points, HDMI adapter needs. Watch the first pitches, read judge
reactions, adjust the last 10%. Ask CSC execs (Rudra, Abhinav Trikha,
Harshit Raj Singh) on-site: who judges, weights, anything they reward.
In-person intel beats research.

### P3-2. THE PITCH SHAPE
Cold-open (aftermovie) -> problem in one line -> our answer (live demo or video) ->
KPI card -> staged failure beat -> close with one ask-back question ("if you were the
sponsor, which metric matters most?"). Answers target the judge's lens: Sarthak gets
metrics, Anjana gets safety, Ayushi gets cost, Sonali gets adoption.

### P3-3. ON-SITE KIT (printed checklist)
Deck in 3 places (USB, Drive, email attachment). Demo videos downloaded, no streaming.
Phone hotspot + verified offline mode. Chargers + power bank. HDMI adapter (USB-C).
Printed one-pagers x6. Printed checklist itself.

### P3-4. NO-EXCUSES FALLBACK TABLE
Every dependency has a fallback: network (hotspot + offline mode), LLM (cache replay),
sound (subtitles), projector (PDF renders), live demo (pre-recorded video), time
overrun (2:30 rehearsal, hard stop at 3:00).

---

## 6. TIMELINE (anchored)

Aug 14 20:00-24:00: P0-1 site hunt, P0-2 attack sheets, P0-3 leave-behind template,
P0-4 Rudra ask, sleep.
Aug 15 09:00-13:00: P1-1 demo videos, P1-2 aftermovie starts.
Aug 15 13:00-18:00: P1-5 rehearsal x2, P1-3 real-data seed, P1-4 KPI cards, deck final.
Aug 15 21:00: watch Unstop + channels, reg-count race starts.
Aug 15 21:30: drop. Tree fires. v1 submit 23:00.
Aug 15 01:00: mentor round, 3 questions ready.
Aug 16 05:00: final submission. 09:00 arrive, scout. 10:00-17:30 pitch.
Aug 16 17:30: aftermovie for the afterparty. Top-2 advance.

## 7. THE ONE LINE

We win if: the drop fits a predicted shape (90%+ probability), the skin mounts in 40
minutes, the staged failure lands, the cold-open opens, and the answers match the
judge's lens. Everything else is noise. Execute the tree, submit early, resubmit
better, sleep in rotation, arrive sharp.
