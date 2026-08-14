# 2026 State Qualifier Scan  -  Confirmed Listings

Compiled: 2026-08-13 | Method: Unstop API ID-range probing + search endpoint

## CONFIRMED 2026 STATE ROUNDS

| State | ID | Registered | Organizer | Notes |
|---|---|---|---|---|
| Rajasthan | 1730314 | 402 | CSC MUJ | LIVE, ends Aug 16 17:30, ₹50K, hybrid at MUJ |
| UP | 1730325 | 1 | IET Lucknow | LIVE, ends Sep 19, "50K+ pool" per listing |

## PROBED RANGES (no other Craft N Code state rounds found)

- 1730300-1730375: jobs/internships/workshops, no Craft N Code
- 1730320-1730340 + 1730400-1730420: no other state rounds
- Unstop search endpoint (q=craft n code, type=competition, pages 1-4): fuzzy matches only (jobs, workshops, unrelated hackathons)

## WHAT THIS MEANS

1. Rajasthan is the BIGGEST confirmed state round (402 reg vs UP's 1). The MUJ qualifier is the flagship.
2. Other states (Assam, Punjab, Bihar, TN had 2025 rounds) either haven't launched their 2026 listings yet or use different ID ranges. The watchdog's PROBE_RANGE will catch them if they appear near the known IDs.
3. The national finals (Oct 30-Nov 1) will draw the winners of ALL state rounds  -  the Rajasthan winner pool is the largest confirmed feeder.

## WATCHDOG STATUS

- craft-n-code-watch cron (every 6h, next 02:34): tracks 1730314 (Rajasthan) + 1730325 (UP) + 3 historical listings. Probes for new state siblings in the 17303xx/17304xx ranges.
- Will alert on: reg count changes, judge/mentor reveals (authors field), result flags.
