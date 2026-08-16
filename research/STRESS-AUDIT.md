# STRESS-AUDIT.md: What We Can Answer, What We Cannot (6,000-question audit)

Date: 2026-08-16. Every one of the 6,000 attacks classified: COVERED if a
design mechanism answers it, OPEN if not. Result: 3,603 covered (60%),
2,397 open. Of the opens, 2,352 are CROP-STATE combinations that the rule
compiler itself is built to generate (expected, not a weakness). The real
gaps are 45: 10 data-integrity, 18 system-security, 7 institutional,
4 judging, 6 scale. This file is the CAN/CANNOT ledger + two simulations.

## CAN ANSWER (the mechanism that answers it)

| Attack family | Count | The answer |
|---|---|---|
| DELIVERY-CHANNEL (all 882) | 882/882 | The degraded-mode ladder: app -> SMS -> IVR -> USSD -> radio -> village. Per-rung triggers + per-channel latency budgets. Late-advisory-expiry semantics |
| ADOPTION-BEHAVIOR (all 48) | 48/48 | Trust badges (source+grade+cost-of-waiting), two-eval-cycle false-alarm rule, approval gate, comprehension testing, postmortems |
| DISASTER-PHYSICS (all 99) | 99/99 | CVaR + Monte Carlo, state machine (never closes on first recession), multi-stream corroboration, source hierarchy |
| HARDWARE (all 63) | 63/63 | One real Rs 1,500 node + simulation labeling; node failure = degrade to phone-only + official feed |
| ETHICS (all 8) | 8/8 | Consent, opt-out by IVR, deletion, shared-phone handling, gendered access flag |
| CROP-STATE (4,704) | 2,352/4,704 | The rule compiler generates the rest: per crop x stage x hazard x lead, from the evidence-graded rule base (d44 seeds + d47 edges). This is the BUILD, not a gap |
| DATA | 74/84 | Profile validation loop (farmer confirms via DTMF), source hierarchy, provenance manifests |
| SYSTEM | 60/78 | Trace, approval gate, idempotency, CAP semantics, signed events |
| SCALE | 4/10 | Severity batching, queue limits, DLT registration path |
| INSTITUTIONAL | 2/9 | ATMA 60:40, FPO rails, PMFBY earmark, OSDMA post-1999 structure |
| JUDGING | 11/15 | Differentiation (doability, cascade, recovery, replay), research machine, honesty labels |

## CANNOT ANSWER YET (the 45 real gaps, honest)

DATA-INTEGRITY (10, all compound "data vandalized + X"):
The answer is one design decision: every farm event is signed and
append-only (provenance manifest per profile), profile edits require
confirmation, and deletion is tombstone + purge. NOT YET BUILT, but the
design is decided. Cost: small. R1 item.

SYSTEM-SECURITY (18, all compound "X + account takeover / spoofed"):
One answer family: operator auth (API keys + mTLS), message signing
(advisory hash + issuer), CAP integrity (verify against IMD's published
feed), and no trust of unauthenticated inputs. Design decided, build is
R1. The prototype simulates: signed labels visible in the trace.

INSTITUTIONAL (7: OSDMA refuses, IMD API denied, no agronomist, FPO
won't pay, relief dependency, ATMA cold, scheme window closed):
PARTIAL answers exist in research (d18, d20, d16: ATMA 60:40, FPO
rails, KCC escalation, 81.3% WTP). The honest position: these are PILOT
gates, not product gates. The prototype says "pilot requires one
partner, the rails exist". We do NOT claim institutional buy-in.

JUDGING (4: Fani was 6 years ago, why Odisha not nationwide, who pays,
privacy):
ANSWERS: (1) Fani is the calibration anchor + Yaas 2021 + Dana 2024 are
fresh, replay is live; (2) Odisha is the statement's scope, nationwide
is Round 3+; (3) who pays: 81.3% WTP small co-pay, FPO rails, PMFBY
0.5% awareness earmark, Farmitra precedent, ATMA 60:40; (4) privacy:
consent + opt-out + deletion + data-as-asset framing.

SCALE (6: 1M farmers, 10M messages, concurrency, throughput, DLT, churn):
Design answers exist (severity batching, DLT registration, number-churn
handling via profile re-verify), but they are R1 architecture, not R0
prototype. The prototype shows the design, not the load.

## SIMULATION 1: FANI, END TO END (the 3-minute demo path)

Timeline: T-90h IMD watch -> T-66h alert -> T-36h warning -> landfall ->
T+24h impact -> T+72h response -> T+30d recovery -> next season.

| Time | Incident state | What the system does | Which attacks it survives |
|---|---|---|---|
| T-90h | MONITOR -> PRE_CYCLONE_WATCH | Profile check via IVR: "your paddy is flowering, confirm" | stale stage, wrong crop |
| T-66h | CYCLONE_ALERT | Advisory compiler: harvest-window check via CVaR (wait vs partial vs immediate), labor + price in the doability layer; SMS to all, IVR to high-risk plots | labor shortage, cost, tenancy |
| T-36h | CYCLONE_WARNING | One highest-value action per call: "harvest mature panicles by 18:00 tomorrow or move to raised platform. source: IMD + rule 14. cost of waiting: X%" | false alarm, trust, contradiction |
| T-24h | POST_LAND_FALL_OUTLOOK | Update the same incident (CAP update), never a new advisory | duplicate, confusion |
| Landfall | IMPACT_SUSPECTED | Sensor + gauge + farmer reports; offline queue renders local advice | tower down, no signal |
| T+24h | IMPACT_CONFIRMED | Farmer reports saline water via IVR -> posterior updates -> advice changes to "test EC, drain, flush" | saline, wrong advice |
| T+72h | RESPONSE | Safety-first, rescue routing, KCC escalation | agent unavailable, panic |
| T+30d | RECOVERY | Claims packet: photo + voice + geo + 72h clock + 33% threshold; recovery chain | claims rejected, evidence |
| Next season | NEXT_SEASON | Swarna-Sub1 variety advice from submergence posterior; salinity + debt carried forward | second flood, landlord, credit |
| Done | CLOSED | Audit trail frozen, feedback request, postmortem | data ownership, deletion |

Every rung of the ladder was exercised at least once. Every state
transition is CAP-linked. The Fani replay panel shows the posterior vs
the real anchors (108,220 ha / Rs 1,304.58 cr) with the uncertainty band.

## SIMULATION 2: THE EVERYTHING-FAILS RUN (the judge's nightmare)

Scenario: landfall night, tower down, power out, phone on 2G battery,
IMD feed cut, agronomist unreachable, second flood wave.

1. Tower down -> ladder drops to radio + village announcement (rung 5/6)
2. Phone 2G battery -> SMS + USSD + IVR still work (rung 2/3/4), app dead
3. IMD feed cut -> the last ingested bulletin + local sensor stream
   (BOCPD + pressure trend) drive the backup hazard layer, clearly
   labeled "LOCAL-CONFIRMATION"
4. Agronomist unreachable -> KCC escalation recorded, advisory carries
   "unreviewed, evidence-graded" badge instead of blocking
5. Second flood wave -> state machine never closed on first recession,
   NEXT_SEASON posterior updated
6. Everything the farmer receives is signed + badged + traceable

Result: the system degrades gracefully down the ladder and the honesty
labels get STRONGER as conditions worsen. That is the pitch moment:
the system that survives the disaster is the system worth trusting.

## THE OPEN-ITEMS REGISTER (R1 backlog, recorded, not hidden)
1. Signed append-only farm event store (data-integrity family)
2. Operator auth + message signing + CAP integrity (system-security)
3. DLT registration + SMS gateway real integration (scale)
4. Comprehension tests with farmers (the impact gate)
5. One real Rs 1,500 node (hardware truth)
6. Dialect QA for the Odia voice pack
7. Conflict policy when two advisories disagree
8. Village radio partnership path (last rung)
