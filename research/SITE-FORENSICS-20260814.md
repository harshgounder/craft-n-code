# SITE FORENSICS - Craft N Code event site deep-read (Aug 14, 20:00 IST)

Method: full clone + git history of p-society/D3-2026 (landing only, no seeds)
and Rudra-25-12/CraftnCode-2026 (the real event site, Lovable-generated).
Every claim below is VERIFIED from source code or git history.

## 1. THE OFFICIAL RUN OF THE NIGHT (src/routes/about.tsx, VERIFIED)

- 20:00: Check-in, team lock-in, opening brief
- 21:30: Problem statements go live. Clock starts.
- 01:00: Midnight fuel run + mentor rounds
- 04:30: Debug hour. The city is asleep, you are not.
- 09:00: Freeze, demo, judging

CONFIRMS Rudra's 21:30 drop from the club's own source. Adds: check-in at
20:00 (before the drop), mentor rounds at 01:00 (confirmed), judging starts
09:00 (not 10:00, Unstop's listing says 10:00-17:30, treat 09:00 as the
real freeze and arrive 08:30).

## 2. THE FIVE TRACKS (src/routes/problem-statements.tsx, VERIFIED, stable since Aug 4)

"CHOOSE ONE TRACK AT CHECK-IN. SWITCHING AFTER THE CLOCK STARTS COSTS
30 MINUTES." Tracks:
- PS-01 Rewind the Legacy: rebuild an outdated campus tool for 2026
- PS-02 Night Ops: tooling for odd hours, sleep, safety, focus, logistics
- PS-03 Signal / Noise: cut through information overload with search,
  summarisation or ranking  <-- EXACTLY our IDEA A / the engine
- PS-04 Open Track: anything justifiable in a 3-minute demo
- PS-05 Hardware Hack: sensors, microcontrollers, physical output

NOTE: this differs from the earlier GAP-MAP list (Campus Pulse, Hygiene
Sentinel are GONE). The site changed. Current list is the truth.

READ: the 21:30 drop is sponsor-set per Rudra. If the drop text is mapped
to lanes, PS-03 Signal/Noise is our home lane (engine IS this). PS-04 Open
Track is the zero-constraint catch-all (any of our 4 ideas pitches clean).
Check-in decision at 20:00: PS-03 default, switch to PS-04 only if the
opening brief signals a wildcard. Budget the 30-min switch.

## 3. THE CLUB'S OWN SUBMISSION SYSTEM (src/routes/submit.tsx + migrations, VERIFIED)

Separate from Unstop. Fields: team_name, track, repo_url (required),
demo_url (optional), pitch (max 2000 chars). Rule: "One submission per
team. You can resubmit until the clock hits zero, latest entry wins."
Eyebrow: DEADLINE 09:00. Supabase RLS: INSERT open, SELECT admin-only
(no exploit vector, confirmed clean).

READ: TWO submissions are required. Unstop PPT by 06:00 (round 1569450,
pdf/pptx max 50MB, resubmit allowed, latest wins) AND the club site
(repo + pitch under 2000 chars) by the 09:00 freeze. The club site pitch
is where our 2000-char killer pitch drafts land. demo_url needs a hosted
video (YouTube unlisted or Drive link) ready to paste.

## 4. SPONSORS (src/routes/sponsors.tsx + full git history, VERIFIED)

All sponsor slots are open: TITLE PARTNER "Your Brand Here", POWERED BY
"Slot Open" x2, COMMUNITY "Slot Open" x3. Full git history grep for
google/apple/meta/accenture/adobe: only fonts.googleapis.com and
apple-touch-icon metadata. ZERO sponsor names ever in the site.

READ: the sponsor set is NOT locked on the site. Rudra's five-company
intel (Google, Apple, Meta, Accenture, Adobe) stays the best signal but
remains UNVERIFIED. If sponsors are still open to buyers, the setter
could differ from the big 5. The decision tree already handles this:
read the drop text, fingerprint it, ignore the prior when the text names
a product or vocabulary.

## 5. WHAT IS NOT THERE (honest negatives)

- No problem statement seeds in migrations, routes, or git history.
- No sponsor names, ever.
- No admin leak: RLS is correctly locked, submissions are INSERT-only
  for anon. The "read other teams" vector does not exist and is not
  attempted.
- D3-2026 (p-society) is a coming-soon landing page, no content.

## 6. NEW PLAYBOOK DELTAS (folded into PLAYBOOK-2026.md)

1. Arrive 08:30 Aug 16 (09:00 freeze is real).
2. Check-in at 20:00: track decision protocol (PS-03 default, PS-04 if
   the opening brief signals wildcard, 30-min switch budgeted).
3. Club-site submission kit: 2000-char pitch draft per idea, repo
   README as pitch (AFTERPACKETS lesson), demo video hosted with a
   shareable URL, submitted before 09:00 (v1 early, resubmit later).
4. Two deadline gates: Unstop 06:00, club site 09:00. Both locked early.
5. Aftermovie beat: 04:30 debug hour + "hall of 200 builders at 3 AM"
   framing (the sponsors page sells exactly this image, b-roll gold).
6. Mentor rounds at 01:00 confirmed: 3 questions per idea prepped.
