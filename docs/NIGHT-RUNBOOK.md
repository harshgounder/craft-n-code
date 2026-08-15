# NIGHT RUNBOOK - Aug 15 20:00 to Aug 16 09:00 (print this)

Compiled: 2026-08-14 20:30 IST | Source of truth for the schedule:
the club's own event site (research/SITE-FORENSICS-20260814.md, VERIFIED).
Two submission gates: Unstop PPT (06:00) and club site (09:00). Both lock.

## FORMAT UPDATE 2026-08-15 19:23-19:47 IST (organizer msgs, SUPERSEDES below)

- Round 0 = ONLINE screening, starts 22:00 IST tonight. Problem statements
  announced by 22:00. Submission = PPT AND Prototype BOTH required.
- Evaluated directly by IIIT BHUBANESWAR faculty (not sponsor companies).
- MIDNIGHT SURPRISE, revealed at midnight, unknown content. Keep 30-min slack.
- Round 1 = OFFLINE 12-hour sprint on campus, date TBA after Round 0 results.
- Round 2 = selected teams present in front of the panel.
- Old gates (Unstop 06:00 / club site 09:00) UNVERIFIED for Round 0: verify
  the live submission links + real deadline when the round opens at 22:00.
- 21:30 references below shift to 22:00. Judges for Round 0 = faculty:
  they probe claims, reward evidence. Proof ledger is the shield.


## ROLES (Team 511)

- Harsh (lead): fingerprint scan at 22:00, final decision call, pitch lead.
- Ayush: repo + engine ops, demo.sh runner, seed data swap.
- Sujal: deck + submission text, paste and submit at each gate.
- Backup rule: anyone can run ./demo.sh and ./atlas/serve.sh. No single point
  of failure. Phones charged, hotspot ready, HDMI adapter packed.
- CARRY THE CHEAT SHEET: research/NIGHT-CHEAT-SHEET-2026.md (print it).
  It has the 5 mount cards, 25 domain rows, the 6 judge attack answers,
  and the 3-minute script with second-level timing.

## FORMAT FACTS (VERIFIED, wave-7: CSC MUJ reel 12 Aug 2026 + public sources)

- 24-hour STATE-LEVEL hackathon, 15-16 Aug, Unstop round 1569450, reg Rs
  299/team, teams 2-4, prize pool Rs 50,000.
- TOP 2 TEAMS ADVANCE to the National Finale at IIIT-Bangalore. The pitch
  leads with the IIITB gate, not the Rs 50K.
- CSC MUJ = "the only Cybersecurity club of MUJ". Security-flavored builds
  get thematic tailwind. Same pipeline runs Nexora'26 -> Craft N Code ->
  IIITB.
- MUJ pedigree judges know: hosted SIH 2025 Hardware Grand Finale (4
  winners x Rs 1.5 lakh); HackX 3.0 national (Rs 5,00,000 pool, 10 themes
  incl. fintech, edtech, health, cyber+defence).
- SIH lesson: judges DO declare no-winner PS (5 in 2024). PS fidelity
  alone lost a team that was "the only one following the brief". Theme
  resonance + adoption language beat literalism.

## TIMELINE

20:00 CHECK-IN + OPENING BRIEF (MUJ)
- Team lock-in. LISTEN for wildcard signals: sponsor names, track changes,
  format changes. If the brief announces a wildcard drop or changes tracks,
  that overrides the plan. Track switch after the clock starts costs 30 min,
  only take it if the signal is clear.
- Verify wifi SSID + power points in the demo room.

21:00 PRE-DROP WATCH
- Open in tabs: Unstop round 1569450, club site problem-statements page,
  club WhatsApp/Telegram, Unstop app push notifications on.
- Pull reg count (unstop.com/api/public/competition/1730314), log it.

22:00 PROBLEM STATEMENTS DROP (Round 0, online)
- Fingerprint scan, 2 MINUTES: read the text for company vocab (cue table in
  IDEA-BANK section 5): agents/tools/deadlines = Google, Llama/multimodal/
  community = Meta, Firefly/creative/brand = Adobe, Swift/accessibility/
  on-device = Apple, workflow/case/KPI/approval = Accenture.
- Decision tree, 10 MINUTES: map to IDEA A/B/C/D (IDEA-BANK section 0).
  Freeze the ONE-SENTENCE STORY (SUBMISSION-TEXT-KIT).
- Write down: sponsor guess, shape, idea, deck, storyboard, acceptance test.

21:45 SKIN MOUNT (target 15-40 min, drill-proven, MOCK-DROPS)
- Fingerprint -> kit from the COMPANY FLAVOR MATRIX (SKIN-KITS-2026):
  Google/Accenture -> KIT-1 or KIT-5, Meta -> KIT-4 (KIT-4B if fraud
  words), Apple -> KIT-3, Adobe -> KIT-2, security words anywhere ->
  KIT-4B overrides.
- Mount: cp fixtures/<kit>.json fixtures/current.json (or --fixture <kit>),
  swap deck nouns, optional label patch (LABEL PATCH BRIEF in SKIN-KITS),
  ./demo.sh, verify endpoints.
- LIVE DATA beat (30 s, do not skip): python3 engine/feeds.py --refresh,
  restart with --feeds. The demo shows REAL recorded problems from HN +
  GitHub + the live Unstop reg count, with the freshness badge.
- PRE-WARM RULE (critical, learned Aug 15): a cold pipeline with 31 live
  items takes 3+ min (rate limits). ALWAYS pre-warm: start serve.py
  --feeds 15 min before the demo, let the pipeline finish, then at demo
  time POST /api/ingest ONE new item (live call ~2-5 s) and the badge
  reads live while everything else renders from cache. Never cold-boot
  on stage.
- 429 WATCH (learned Aug 15 ~13:45): the OLLAMA key now hits HTTP 429
  (Too Many Requests) under sustained cold-run load. Pre-warm in TWO
  spaced passes (start server, let it hit 429s, restart 5 min later;
  cache fills across passes), keep the .llm_cache.json warm copy in the
  repo data dir as the ultimate fallback, and be ready to tell the
  honesty story: "the provider rate-limited us, the badge flipped to
  offline, the feed kept ranking. that is the product."
- If any dependency fails its 60-90 min time gate: switch to
  fixture/replay mode, no exceptions. Run the DRILLS cheat sheet
  (BACKEND-DRILLS-2026) if anything misbehaves.

22:30 VERTICAL SLICE + DIFFERENTIATOR
- One differentiator, one staged failure (the failure path wins demos).
- KPI card on screen: 81/81 checks, zero deps, mode badge, feeds badge.
- THE HONESTY MOMENT (30 s): kill the LLM key mid-demo, show the badge
  flip to offline and the feed still ranking. This is the "what if it
  fails" answer. Practice it in DRILL 2.

23:00 GATE 1: v1 SUBMIT (both gates, insurance)
- Unstop: PPT (pdf preferred) uploaded, under 50MB. Club site: repo_url +
  pitch from SUBMISSION-TEXT-KIT + demo_url if video exists.
- Lock it. A bad v1 beats no v1 at 05:59.

23:00-01:00 POLISH + BACKUP VIDEO
- Record a 3-min backup video (wf-recorder -a -f backup.mp4), store on the
  phone too. Rehearse 2:30 once, record it, review.

01:00 MENTOR ROUND (club schedule)
- 3 prepped questions per idea: sponsor-fit check, one differentiator
  suggestion, what judges reward this year. Take notes, fold in fast.

03:00 GATE 2: v2 SUBMIT (both gates)
- Incorporate mentor notes + polish. Resubmit.

04:30 DEBUG HOUR (club schedule)
- The scheduled beat: use it as the story moment ("the city is asleep, we
  are not") in the pitch and aftermovie. Fix anything found in rehearsal.

05:00 GATE 3: FINAL SUBMIT
- Never 05:59. Latest wins, so the final is the last upload. Verify the
  file opens on the venue laptop (pdf renders identically everywhere).

06:00 UNSTOP CLOSE (hard stop)
- Club site still open until 09:00; use the window for README polish if
  something slipped.

08:30 ARRIVE AT MUJ, SCOUT
- Projector resolution, audio, mic, wifi, power, HDMI. Watch the first
  pitches, read judge reactions, adjust the last 10%. Ask CSC execs
  on-site: who judges, weights, anything they reward.

09:00 FREEZE, DEMO, JUDGING
- 3-min demo, 2:30 rehearsal target, hard timer. THREE-ACT ARC (wave-14,
  second-level): Act 1 problem 30-45 s (open 10 s with ONE victim, one
  cost: e.g. "Rs 4,057 crore, 3 lakh victims, one call"), Act 2 solution
  + live demo 90-120 s (demo intro 5 s, live demo 70 s, credibility line
  10 s), Act 3 impact 30-45 s (one quantified number 20 s, vision 15 s,
  ask 15 s). Demo never under 60 s.
- Failure-case moment: 20 s show the old way failing, 50 s show ours
  winning on the same input. Kills "does it solve the problem" + "is it
  better" in one beat.
- Deck: 7-10 slides. Slides 1-2 carry elimination risk. Architecture
  slide = max 4 boxes, numbered lifecycle, "built vs reused" honesty
  column. No AWS-icon diagrams.
- Recovery lines (rehearse 5x): "Let me show you a moment in our test
  data that captures exactly what the live system does."
- PLANTED Q&A: end with one metric that forces the question you want
  ("81/81 checks, zero deps, badge that cannot lie. Ask us how we tested
  it.").
- LLM FALLBACK LADDER (wave-12): OLLAMA primary -> OpenRouter :free
  suffix (26+ $0 models, no card) -> Cerebras 1M tokens/day -> deep
  offline mode. Never a dead demo.
- LIVE DATA rails (wave-9): HN Firebase API (keyless, no rate limit,
  CORS = browser fetch works), NPCI monthly UPI stats (23.66 bn txns /
  Rs 29.88 lakh crore, July 2026), data.gov.in, Wikipedia REST 200 rps.
  feeds.py already uses the HN source.

## WHAT TO CARRY

- Laptop + charger, phone + charger + hotspot, HDMI adapter, backup cable
- Printouts: this runbook, the cue table (IDEA-BANK 5), one-sentence
  stories, SUBMISSION-TEXT-KIT pitches
- Backup video on phone + laptop + one USB stick
- Water + snacks for the night, jacket (venue AC)

## PRE-AGREED KILL CRITERIA

- Any dependency failing its 60-90 min gate -> fixture/replay mode.
- LLM quota dead at 3 AM -> offline mode, badge shows it honestly.
- Pitch overruns -> the demo is the pitch; cut the deck, keep the story.
