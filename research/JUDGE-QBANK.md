# JUDGE-QBANK.md: the 30 most likely Round 0 questions, model answers

Date: 2026-08-16 (window B, T3). Source: stress-questions.json (6,000
questions), filtered to COMPETITION-JUDGING (all 15) plus the delivery,
data, ethics, institutional and scale questions most likely to come
from IIIT Bhubaneswar faculty. Every answer is grounded in
EVIDENCE-INDEX (dXX), THE-PLAN.md or BUILD-MATRIX.md. If a judge asks
something not on this list, the answer rules are: name the badge,
name the source, never claim live.

## A. COMPETITION-JUDGING (15)

1. Why not Meghdoot?
Meghdoot is IMD's own advisory: district-level agromet bulletins
without a farm profile, without doability (labor, cost, credit,
tenancy), without a delivery ladder and without replay validation.
KrishiSetu ingests the same official signals (public CAP RSS, d16) and
compiles them through a farm profile into staged actions with cost of
waiting. We are not a bulletin service, we are a compiler (d8, GKMS
cadence as prior art).

2. Why not WhatsApp?
WhatsApp needs a smartphone and data. Odisha rural: 53% of households
smartphone-only, 19.8% basic phone, and towers die in cyclones (d6,
d17: Fani knocked out 4 districts for 9 days). WhatsApp cannot run on
a feature phone, cannot do keypad acks, and is a single-vendor rail.
In our ladder WhatsApp is an optional app-layer rung, never the
backbone.

3. Why not Ama Krushi?
Ama Krushi proved the demand: 3.2M farmers served at the 2022
handover, reported near 7.9M today (d26). What it does not do is
personalize under stress: no recovery state machine, no doability
engine, no claims rail, no replay validation. Our thesis is built on
top of that institutional fit, not against it (d26).

4. Your LLM is a wrapper.
Correct framing: the LLM only renders. The advisory engine is
deterministic rules over JSON (R1-R16 registry, rules are data, not
code) with audit (d47, THE-PLAN). If the LLM is absent, the same
advisory ships as fixed Odia templates (PRODUCT-CORE). A wrapper
decides nothing; our engine decides and the LLM speaks.

5. Fani was 6 years ago.
That is exactly why it is our calibration anchor: official DLNA
numbers (108,220 ha, Rs 1,304.58 crore, d47 L6) are stable, dated and
uncontested. The replay runs the compiler backward over Fani and Yaas
and shows the posterior with an uncertainty band (agri/replay.py). And
Dana, October 2024, gives a near-current second anchor (d6: four-block
Kendrapara/Bhadrak assessment).

6. No real deployment.
True, and labeled: every feed, channel and stream on screen is
SIMULATED, SIMULATOR or ROADMAP. What is real is the thesis carriers:
the compiler, the doability layer, the 11-state machine, the replay
and the claims packet, all under 85 passing test suites. We present
the prototype and the documented final shape (BUILD-MATRIX tiers).

7. Your sensors are simulated.
Yes, SIMULATED STREAM. Sensors are the backup trigger, not the
product: IMD is the primary trigger (PRODUCT-CORE). A Rs 2,899 node
BOM exists on paper (d12) but the demo runs cached samples, and one
real node is a Round 1 buy.

8. Your SMS is simulated.
Yes, SIMULATOR. Live SMS needs DLT registration and a gateway, which
is Round 1 (BUILD-MATRIX TIER 2). What ships in the prototype is the
pattern: latency budgets, unread escalation, ack tracking, all
visible in the delivery log.

9. The claims packet is fake.
The packet structure is real engine code (agri/claims.py): photo,
voice note, geo, 72-hour intimation clock, 33% state relief threshold
(d20). The payload in the demo is sample data, and the UI says so. No
live claim was ever filed.

10. No farmer testing.
Correct. Field testing is gated on a Round 1 pilot. What we did
<<<<<<< HEAD
instead: 48 research reports including farmer-voice evidence (d6, d15,
=======
instead: 49 research reports across 7 waves including farmer-voice evidence (d6, d15,
>>>>>>> window-c
d31), an adaptation-gap thesis built from tenancy, debt and labor data
(d37), and replay validation against real events. We do not claim
field validation.

11. Your math is borrowed.
The math is standard and cited: Holland wind field (d9), BN-FLEMO
MAE 0.18 (d47), sample-based CVaR. Borrowed with citation is fine for
a Round 0 prototype. What is ours is the combination: doability-gated
compiler, 11-state machine, replay calibration, honesty badges, which
the unique-angle validation report rated QUALIFIED GO (d34).

12. Show me the Fani replay.
The replay panel runs the compiler backward over Fani's timeline and
plots the posterior against the 108,220 ha / Rs 1,304.58 cr anchors
with an uncertainty band. If the panel is not on screen, the evidence
chain is: deck slide 7, ledger rows P1-P6, index row d47, raw
cnc-ps07-d47-systems-cascade-math-agri.

13. Why Odisha and not nationwide?
One rail, one pilot, one quarter (BUILD-MATRIX TIER 3). Rule packs
are data (R1-R16 JSON), so a new state means new rules and profile
fields, not new software. Odisha first because the problem is the
best documented here: paddy is 44% of gross cropped area (d4), 4.866M
small holdings at 0.95 ha average (d6), a working disaster ecosystem
(d20).

14. Who pays?
ATMA 60:40 Centre-State funding is the lead payer rail for advisory
delivery (d18). Willingness to pay exists but is small: 81.3% of
Odisha farmers in a 2026 study accept a small co-pay (d18). Claims
ride the PMFBY premium ecosystem (d6), and the data-cooperative value
loop is a Round 2 pilot (d40).

15. Privacy?
Consent-first farm profile, farm-level data with phone and plot
fields, no data sale clause, zero-cloud default (the engine runs on a
laptop or Raspberry Pi, PRODUCT-CORE). Consent withdrawal deletes the
profile and stops advisories, handled by the scaffold consent
endpoint. The profile only ever leaves the device as a signed,
consented export.

## B. DELIVERY-CHANNEL (6, from the 882-question grid)

16. SMS: tower down, never sent.
The ladder exists for this: SMS is rung 2, not the system. Unacked
messages escalate down: IVR, USSD, radio, volunteer (THE-PLAN rules).
Every rung attempt is recorded in the operator delivery log, so the
operator sees the gap, not the farmer's silence.

17. SMS: delivered but unread.
Escalation timer: unread after a latency budget, IVR callback with
collect-call. The demo trace is real: SMS 13:58 unread, IVR 14:05,
Asha acks 14:12. That trace is the product.

18. SMS: sent to the wrong number.
Number churn is a scale reality (SCALE grid: 20% per year). The
mitigation is identity on the voice rail: IVR confirms the farm
profile (last 4 digits of the plot or KCC), wrong numbers get caught
on first call, and USSD re-registration fixes the record.

19. IVR: dropped call or noise.
Missed-call callback (the CGNet Swara pattern, d28), retry with
backoff, and a session resume token: the farmer continues where the
call dropped instead of restarting. The ack is keyed on the action,
not the call.

20. USSD: session timeout.
USSD is a 90-second session rail, never a store (THE-PLAN ladder).
On timeout the system sends the SMS summary and flags the farm for
the volunteer rung. The fallback arrow is the design, not a failure.

21. Radio: bulletin missed.
Radio is the wide net, not the targeted one. The village volunteer is
the confirmation rung (d28: Farm Radio International 24.1M listeners;
d43: CPP's 76,000 volunteers as the human-relay model). The console
tracks per-farm ack so a missed bulletin surfaces as an unacked farm,
not a lost message.

## C. DATA (4, from the 84-question grid)

22. Crop entered wrong + IMD feed down.
The compiler fails safe: profile fields are confirmed at consent time
via IVR/DTMF (d31), and with IMD down the backup predictor is down
too, so the system drops to generic stage-based advisories wearing
UNKNOWN badges. It never guesses a hazard.

23. Stage stale + CAP RSS stale.
Stage staleness is detected from sowing date plus a re-confirm prompt
on the next call. CAP staleness gets a timestamp badge (CACHED
SAMPLE), with Open-Meteo as fallback (d16) and the backup predictor
as the last trigger.

24. Two advisories conflict.
One current state, CAP semantics: incident versions supersede (the
console shows v3 CAP-linked updates), the scaffold dedupe layer merges
identical intents, and genuine conflicts surface to the operator
console for a human call. They never resolve silently (d47: keep
dependence separate from causation).

25. Data vandalized or sensor anomaly.
Every change sits in the scaffold audit ring (trace). Anomaly
detection flags jumps (d13: BOCPD, iForest), and a vandalized profile
field bounces against consent re-confirmation before any advisory
ships.

## D. ETHICS-SAFETY + INSTITUTIONAL + SCALE (5)

26. Wrong harvest advice destroys a crop.
The ethics gate: advice comes from deterministic rules reviewed
against KVK/OUAT practice (d20), every action carries a source badge
and a cost of waiting, and the tiered evidence gate (d36) blocks
unverified rules from shipping. The replay shows the uncertainty
band; we do not sell certainty.

27. Your advice contradicts the extension officer.
The system complements the human: conflicts escalate to the extension
officer (KCC-style expert escalation, d8, d31: 65% of farmers want
expert answers), and the operator console shows both sides. The
system never overrides a human authority.

28. The landlord blocks the tenant's action.
Tenancy is the doability gate: the compiler checks the tenancy flag
before proposing structural work, as Asha's embankment card shows:
owner approval required, pending via IVR. The tenant-legal fallback
actions ship instead: move seed, shelter livestock, claims prep. This
is the adaptation-gap thesis in one card (d37: 5.82% wholly leased-in
holdings, split incentives).

29. OSDMA refuses to integrate.
No dependency: the prototype needs zero institutional permission,
zero API keys, public CAP RSS (d16). OSDMA is an integration partner,
not a gate. The documented institutional route is KVK/OUAT rule
review and ATMA 60:40 funding (d20, d18).

30. What happens at 1M farmers or a 100x seasonal spike?
Advisories are compiled per farm from JSON rules, which is
embarrassingly parallel and batch-friendly (THE-PLAN). SMS and IVR
scale through the same rails the telecom operators already run (d7),
and the 100x spike is absorbed by the ladder: most farms get SMS,
only unacked ones consume IVR minutes. DLT registration and gateway
capacity are Round 1 items, not architecture changes.

## ANSWER RULES FOR ANYTHING NOT ON THIS LIST

1. Name the badge on the number (ODISHA-MEASURED, TRANSFER-PRIOR,
   SCENARIO-ASSUMPTION, UNKNOWN).
2. Name the source (rule id or report id) or say "not yet sourced,
   marked UNKNOWN".
3. Never claim live anything: feeds are SIMULATED, channels SIMULATOR
   or ROADMAP, sensors SIMULATED STREAM.
4. If the question is about the future: the answer is BUILD-MATRIX
   tiers (Round 1 pilot, Round 2 rails), never a promise.
