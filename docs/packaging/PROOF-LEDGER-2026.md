# PROOF-LEDGER-2026

Claim | Evidence | Condition | Status. Every number in the deck, README, trailer, and pitch gets a row here. A claim without a row does not ship. Updated live; kit-dependent rows land after the 22:00 drop.

## Kit-independent rows (verified 2026-08-15)

| # | Claim | Evidence | Condition | Status |
|---|---|---|---|---|
| 1 | Engine completes the full loop: ingest -> dedupe -> rank -> propose -> approve -> audit | Trace viewer + acceptance suites; test_trace 12/12 | Any configured provider; local mode with null provider | VERIFIED |
| 2 | 85/85 acceptance suites green | scaffold/tests fresh run 2026-08-15 20:11 (approval 13/13, trace 12/12, providers 9/9, multimodal 4/4, provenance 4/4, feeds 8/8, honesty 12/12, stress 23/23) | Fresh DB per suite; run BEFORE the demo server starts (port contention causes flakes) | VERIFIED (fresh run) |
| 3 | 46/46 lane fixture scenarios verified | B5 lane fixtures suite (support-ticket, volunteer-coordination, campus-ops golden sets) | Fixture data, dedupe pairs + scam items included | VERIFIED |
| 4 | Zero runtime deps beyond stdlib + optional LLM endpoint | Engine imports scan, requirements.txt, clean-machine run | Python 3.11+ | VERIFIED |
| 5 | Honest mode badge counts ACTUAL provider outcomes | Honesty suite 12/12 (incl. H7 live-outcome badge, no badge-lie) | Any provider | VERIFIED |
| 6 | Approval gate: typed tools, policy gate, human approve/reject | test_approval 13/13 (G13 demo.sh syntax gate) | Gate enabled | VERIFIED |
| 7 | Live keyless feeds: HN, GitHub, Unstop | test_feeds 8/8 (F4 DB isolation, fresh artifacts) | Network available; offline mode documented | VERIFIED |
| 8 | Approval fatigue guard: no silent autonomous actions | Engine code path: propose always precedes execute; audit rows written per action | Trace enabled | VERIFIED (code audit) |
| 9 | Storage layer: SQLite default byte-identical, Postgres optional | B9 suite + integration test | DATABASE_URL set for Postgres | VERIFIED |
| 10 | Realtime panel: SSE /api/events, 50-event replay, 8-client cap | B4 build, f96b9b1 | Webapp running | VERIFIED |

## Kit-dependent rows (fill after 22:00 drop)

| # | Claim | Evidence | Condition | Status |
|---|---|---|---|---|
| K1 | [KIT number block: victims/fraud amount/MSME count] | NUMBERS-2026 + kit research file | Source URL + date | PENDING |
| K2 | [KIT adoption claim: one rail, one pilot] | Pilot rails research (GeM/ONDC/ABDM/iStart) | Named rail + contactable pilot | PENDING |
| K3 | [Trailer proof line: specific result in defined context] | Trailer footage + dated demo | Footage matches current build | PENDING |
| K4 | [Deck traction timeline: primary metric monthly] | Live feed data + kit metrics | Dates + denominator stated | PENDING |

## PS-07 deck rows (KrishiSetu Round 0, added 2026-08-16)

| # | Claim | Evidence | Condition | Status |
|---|---|---|---|---|
| P1 | 5,428 acres crop loss, 4 blocks of Kendrapada + Bhadrak, Cyclone Dana 2024 | YSD Odisha rapid assessment (research/raw/v2 forensics [25]) | Call it a rapid assessment, not a census | VERIFIED |
| P2 | 5,882 ha cultivable land salt-affected, 5 Balasore blocks, Cyclone Yaas 2021 | Down To Earth post-Yaas report (forensics [23]) | Farmers "in a fix" context, not a loss total | VERIFIED |
| P3 | PMFBY: 88.5 lakh enrollments, Rs 2,580 cr claims paid (2020-25) | d21 [16]: Lok Sabha annexure, 88,55,046 enrollments, Rs 2,580.06 cr | Program scale, not our TAM | VERIFIED |
| P4 | Digital Agriculture Mission Rs 2,817 cr | PS-07 v1 mine [9] | Outlay, not our addressable spend | VERIFIED |
| P5 | 85/85 suites + 46/46 eval green | scaffold fresh run 2026-08-16 07:40 | Fresh DB, pre-server | VERIFIED |
| P6 | Prototype honesty: IMD feed simulated, SMS via simulator, curated seed rules | scaffold code + deck slide 5 | No live claims anywhere | VERIFIED |
| P7 | Research machine: 49 reports (47 numbered + 2 refires), 7 waves, 3.2M chars, 4,800 cited sources | krishisetu research/raw: 49 content files, 2,225,731 chars, 3,471 source mentions (window D measured 2026-08-16). hackathon-sota-lab research/raw/v2: 18 content files, 992,045 chars, 1,329 mentions. Combined 3,217,776 chars, 4,800 mentions | Holds only when both research waves count; "sources" = raw URL mentions, ~4,100 unique after dedupe | VERIFIED |

## Honesty rule

If the evidence is a projection, call it a projection. If the product is a prototype, call it a prototype. Every row survives a follow-up question. (wave24: the film should survive a skeptical screenshot; same rule for every artifact.)
