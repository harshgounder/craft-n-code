# THE-PLAN.md: KrishiSetu, The Complete Build Plan

Date: 2026-08-16. Base: 49 research reports (all read), 6,000-question
stress test + audit, two simulations, the R1-R16 global rule registry.
This is the plan the stress test FORCED, not a wish.

## PART 0: THE PRODUCT IN ONE PARAGRAPH
KrishiSetu is a cyclone and flood resilient agriculture advisory system
for Odisha. It joins a consented farm-and-crop profile to authoritative
IMD/CWC signals, compiles crop-stage-specific pre and post disaster
actions with deadlines, sources, and cost-of-waiting, ranks them by
what the farmer can ACTUALLY do (labor, cost, credit, tenancy), delivers
through a degraded-mode ladder (app -> SMS -> IVR -> USSD -> radio ->
village), tracks the incident through 11 states, and validates itself
against replayed real events (Fani, Yaas) with explicit uncertainty.
Every number wears a badge. The LLM renders, the audited engine decides.

## PART 1: THE DELIVERY LADDER (low latency, every network, every phone)
Designed for 4G and BELOW, 2G, radio, and no connectivity. No single
channel reaches everyone (R2).

| Rung | Channel | Works on | Latency budget | Trigger to use it | Fallback when it fails |
|---|---|---|---|---|---|
| 1 | App (offline-first PWA) | Smartphone, any data | <5s push | 4G/5G present | Cache renders from IndexedDB, queue syncs later |
| 2 | SMS (Odia-capable, DLT) | ANY phone incl. feature | 5-30 min | 2G/3G, no data | If unread after T, escalate to IVR |
| 3 | IVR missed-call callback | ANY phone, no data | 30-60s setup | DND, low literacy, no credit (collect) | If unacknowledged, escalate to volunteer |
| 4 | USSD (session-based) | ANY phone, 2G | <1s round trip, 90s session | 2G only, data dead, SMS slow | Session expiry -> SMS fallback |
| 5 | Community radio / loudspeaker | No phone needed | Broadcast schedule | Tower down, mass event | Village relay confirms |
| 6 | Village volunteer / paper | No phone needed | Hours | Everything dead | Post-event debrief |

RULES: (a) every advisory carries "if received after T, action is
obsolete"; (b) the system detects unacknowledged delivery and escalates
down the ladder (R2 redundant last mile); (c) latency budget per action
decides the rung: 6h window = SMS, 1h window = IVR+radio; (d) nothing
single-channel ever. Ama Krushi pattern: toll-free shortcode, IVR,
live agent, message history (d41).

## PART 2: THE INCIDENT STATE MACHINE (the evolving advisory)
11 states, CAP-linked, one versioned incident never one-shot texts:
MONITOR -> PRE_CYCLONE_WATCH (72h) -> CYCLONE_ALERT (48h) ->
CYCLONE_WARNING (24h) -> POST_LAND_FALL_OUTLOOK (12h) ->
IMPACT_SUSPECTED -> IMPACT_CONFIRMED -> RESPONSE -> RECOVERY ->
NEXT_SEASON -> CLOSED.
Rules: RECOVERY feeds NEXT_SEASON (never an end state); the machine
never closes on first recession (second-flood semantics); every
transition is CAP-linked (update, never duplicate); severity batching
under 100x spikes, never timestamp batching.

## PART 3: THE ADVISORY COMPILER (the brain)
- R1-R16 rule registry from the global practice sweep, each rule with
  machine trigger, advisory action, guardrail, grade
- Evidence-graded: A deploy now, B pilot with partner, C/D quarantine
  in admin library, never in farmer messages
- Four badges on every number: ODISHA-MEASURED / TRANSFER-PRIOR /
  SCENARIO-ASSUMPTION / UNKNOWN
- The doability layer (d37, d39): every action carries labor hours,
  cost, credit context, tenancy flag. A harvest order without labor is
  noise. Ranking: expected-loss comparator + CVaR + infeasibility
  penalty: a* = argmin CVaR(total loss|a) + cost(a) + infeasibility(a)
- Human approval gate: the system proposes, the farmer confirms via
  keypad, the trace records everything
- LLM renders ONLY the structured fields, never invents agronomy

## PART 4: THE CASCADE ENGINE (the intellectual crown, d47)
- Typed signed time-sliced DAG: TRIGGER/AMPLIFY/CASCADE/COMPOUND edges,
  sign positive or negative, lag, CP, evidence scope, source, grade
- Calibrated on Fani (108,220 ha, Rs 1,304.58 cr) and Yaas (2-4m surge
  over full-moon tide): the replay setup with uncertainty bands
- Monte Carlo with convergence gates (pilot + main, precision stops)
- 95% CVaR at loss nodes, optimized only at action nodes
- Copulas fitted locally, never borrowed (no invented Gumbel theta)
- Positive cascades conditional only: managed recharge, managed
  rice-fish, sediment tested for salinity first
- No flood->blast / flood->BPH deterministic rules (covariate models)

## PART 5: THE FARM PROFILE (the asset, d38-d40)
- Consented enrollment: crop, variety, stage, plot, elevation, soil,
  phone type, language, tenancy, livestock, pond, seed stock, labor
- Farmer-as-sensor: DTMF keypad first, voice capture second (real Odia
  ASR WER 35.1%: ASR is optional, never the sole path), photo where
  the phone allows
- Signed append-only event store (R1 backlog item), edits require
  confirmation, deletion = tombstone + purge
- Household profile with member separation (shared phone, gender gap)
- Opt-out by IVR one press, consent at enrollment, data-as-asset
  framing: better advice -> claims evidence -> credit visibility

## PART 6: THE RAILS (who pays, d18, d20)
- PMFBY claims packet: photo + voice + geo + 72h intimation clock +
  33% threshold, evidence export
- KCC escalation: one press, 22 languages
- OSDMA/extension integration: post-1999 institutions exist
- FPO rails, ATMA 60:40, PMFBY 0.5% awareness earmark, Farmitra
  precedent, 81.3% WTP small co-pay
- Pilot gate stated honestly: one partner, one block, one season

## PART 7: THE BUILD SCHEDULE
ROUND 0 (18:00 today): the zero-dep prototype, 10 panels: profile,
hazard trigger, compiler, two-farm contrast, CVaR harvest, Fani replay,
offline+voice trace, claims packet, doability, research machine.
Placeholders labeled ROADMAP on SMS/IVR/sensor/LoRA nodes.
ROUND 1 (next weekend, 12h): real SMS gateway + DLT, IVR with Odia
recordings, comprehension tests with farmers, the Rs 1,500 sensor node
live, signed event store, operator auth, dialect QA, advisory conflict
policy, village radio partnership path.
ROUND 2 (IIIT-B, new statements): the engine + kit + research method
remount, AFTERPACKETS style.

## PART 8: THE PARALLEL WINDOW PLAN (the delegation)
Window B (frontend): farmer app (Odia, low-literacy, DTMF-style),
operator console, offline PWA + IndexedDB + service worker, 4-badge
visual system. Builds against the scaffold's 14 endpoints.
Window C (backend): Postgres + PostGIS + Timescale schema (farms,
profiles, incidents, claims, sensor series), REST API, SMS/IVR adapter
stubs with delivery tracking + idempotency, CAP RSS ingest stub, seed
data (Fani/Yaas archives). Builds to the JSON contract.
Merge: both push to branches, I audit + merge + test, 16:30 buffer.

## PART 9: THE HONESTY CONTRACT (non-negotiable)
- No borrowed Odisha coefficients, no invented Gumbel theta
- No flood->pest deterministic rules
- No recharge/silt/fish benefits without managed infrastructure
- No 32.9% or 1.9 dS/m presented as Odisha truth
- No completeness claim on the global ledger
- No loss-reduction claims without comprehension + action measurement
- Every number wears a badge, every rule has a source, every
  placeholder is labeled
- The system that degrades gracefully is the system worth trusting

## THE OPEN REGISTER (R1 backlog, recorded, not hidden)
Comprehension tests with farmers (reality gap: only field presence
closes it) and the real Rs 1,500 node (reality gap: only hardware
closes it). EVERY other stress-test gap now has a designed answer in
IMPROVISED-ANSWERS.md with a condition attached. No design gap without
a design.
