# NIGHT RUNBOOK - Aug 15 20:00 to Aug 16 09:00 (print this)

Compiled: 2026-08-14 20:30 IST | Source of truth for the schedule:
the club's own event site (research/SITE-FORENSICS-20260814.md, VERIFIED).
Two submission gates: Unstop PPT (06:00) and club site (09:00). Both lock.

## ROLES (Team 511)

- Harsh (lead): fingerprint scan at 21:30, final decision call, pitch lead.
- Ayush: repo + engine ops, demo.sh runner, seed data swap.
- Sujal: deck + submission text, paste and submit at each gate.
- Backup rule: anyone can run ./demo.sh and ./atlas/serve.sh. No single point
  of failure. Phones charged, hotspot ready, HDMI adapter packed.

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

21:30 PROBLEM STATEMENTS DROP
- Fingerprint scan, 2 MINUTES: read the text for company vocab (cue table in
  IDEA-BANK section 5): agents/tools/deadlines = Google, Llama/multimodal/
  community = Meta, Firefly/creative/brand = Adobe, Swift/accessibility/
  on-device = Apple, workflow/case/KPI/approval = Accenture.
- Decision tree, 10 MINUTES: map to IDEA A/B/C/D (IDEA-BANK section 0).
  Freeze the ONE-SENTENCE STORY (SUBMISSION-TEXT-KIT).
- Write down: sponsor guess, shape, idea, deck, storyboard, acceptance test.

21:45 SKIN MOUNT (target 15-40 min)
- Swap seed data + UI labels, pick deck + storyboard, run ./demo.sh,
  verify endpoints. If any dependency fails its 60-90 min time gate:
  switch to fixture/replay mode, no exceptions.

22:30 VERTICAL SLICE + DIFFERENTIATOR
- One differentiator, one staged failure (the failure path wins demos).
- KPI card on screen: 42/42 checks, zero deps, mode badge.

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
- 3-min demo, 2:30 rehearsal target, hard timer. Cold open (aftermovie if
  it exists, else the one-sentence story) -> problem -> answer -> live
  demo -> KPI -> close.

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
