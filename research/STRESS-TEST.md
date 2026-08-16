# STRESS-TEST.md — 6,000 Adversarial Attacks on the KrishiSetu Plan

Date: 2026-08-16. Method: combinatorial matrix over 10 attack surfaces
(delivery, hardware, data, disaster physics, adoption, system, institutional,
judging, ethics, scale) x the crop-state matrix (7 crops x 8 stages x 12
hazard moments x 7 lead-time states) = 6,000 distinct what-if questions.
Full JSON at research/stress-questions.json. This file is the KILL-LIST:
the attacks that expose real plan weaknesses, and the design answer each
one FORCES.

## THE DELIVERY LADDER (the channel problem, your ask)
The stress test over delivery channels (882 attacks) kills any single-channel
plan. The forced design: a DEGRADED-MODE LADDER, not a fallback list:
1. Smartphone app with offline cache (rich, only when it works)
2. SMS (works on 2G, 160 chars Odia-capable, DLT-registered)
3. IVR missed-call callback (works on feature phones, no data)
4. USSD (works on 2G, session-based, no data)
5. Community radio / loudspeaker broadcast (works when telco dies)
6. Paper flyer / village announcement (works when everything dies)
Each rung has a trigger: the system DETECTS which rung failed and escalates
down. "Tower down" attacks force the offline queue + local render. "DND"
forces USSD+IVR. "No credit" forces collect-call callback. "2G only" forces
SMS+USSD+IVR over app. The ladder is the product, not the app.

## THE LOW-LATENCY REQUIREMENT (your ask)
Attacks on latency: SMS arrival 5-30 min under load, IVR setup 30-60s,
USSD round-trip <1s but session 90s max, app push needs data. The forced
design: per-channel latency budgets on the advisory (action deadline minus
delivery latency). An action with a 6h window can use SMS; a 1h window
forces IVR+radio. The advisory carries "if you receive this after X, the
action is obsolete" semantics, because a late advisory is a false alarm.

## THE KILL-LIST (the attacks that actually hurt)
1. "Farmer ignored the message" -> trust is earned: every advisory shows
   its source + grade + cost-of-waiting, and the system measures
   comprehension before claiming anything
2. "False alarm destroyed trust" -> the two-evaluation-cycle rule (d13),
   multi-stream corroboration, and post-event honest postmortems
3. "Wrong harvest advice destroyed the crop" -> CVaR + doability + the
   human approval gate: the system PROPOSES, the farmer confirms, and
   the risk label is on every action
4. "Judges: why not Meghdoot/WhatsApp/Ama Krushi" -> the differentiation
   is the doability layer + the cascade math + the recovery state
   machine + the replay validation, all absent from those systems
5. "No farmer testing" -> Round 1's comprehension tests are the gate;
   the deck says so explicitly
6. "Sensors are simulated" -> one real Rs 1,500 node in Round 1, labeled
   simulation everywhere else
7. "Data ownership / consent" -> consent at enrollment, opt-out by IVR,
   deletion on request, profile records phone ownership (gender gap)
8. "Same phone, two farmers" -> household profile with member separation
9. "Seasonal 100x spike at landfall" -> the incident state machine
   batches by severity, never by timestamp
10. "LLM hallucination" -> the LLM only re-renders structured fields
    from the audited rule engine (d10, d11): it never invents agronomy
11. "Advice contradicts extension officer" -> the advisory carries its
    source + rule ID so the officer can audit it, and KCC escalation
    is one press away
12. "Claims packet rejected" -> the packet is a structured evidence
    export with photo/voice/geo + the 72h intimation clock, and the
    PMFBY 33% threshold is in the rule set
13. "Flood recedes, then second flood" -> the state machine never closes
    on first recession; NEXT_SEASON state carries the posterior
14. "Landlord blocks tenant" -> the doability layer surfaces tenancy as
    a feasibility constraint and the advisory offers actions that
    respect it (seed storage, labor, insurance evidence)
15. "The judges ask for the Fani replay" -> it is in the prototype,
    with the uncertainty band and the real anchors

## WHAT THE STRESS TEST FORCES INTO THE PLAN
1. A degraded-mode delivery ladder with per-rung triggers and per-channel
   latency budgets
2. Offline-first as the default architecture, not an afterthought
3. The human approval gate on every action (never autonomous execution)
4. Comprehension + action measurement as the ONLY impact claim
5. The four-badge honesty policy on every number
6. Consent, opt-out, deletion, and shared-phone handling as first-class
7. The incident state machine with severity batching and never-closed-
   on-first-recession semantics
8. The replay harness (Fani/Yaas) as the validation spine
9. The doability layer (labor, cost, credit, tenancy) on every action
10. One real hardware node in Round 1, simulation labeled in Round 0
11. The research machine as the credibility layer (48 reports, chain)

## OPEN ATTACKS (no answer yet, flagged)
- "What if the farmer's phone is stolen mid-event" (device loss path)
- "What if the local language recording is wrong dialect" (audio QA)
- "What if two advisories conflict (ours vs official)" (conflict policy)
- "What if the agronomist is unavailable at landfall" (escalation path)
- "What if the village radio station is offline too" (last-rung policy)
- "What if the DLT registration is rejected" (SMS shutdown path)
These are the Round 1 stress-test backlog, recorded now so the plan
cannot pretend they do not exist.
