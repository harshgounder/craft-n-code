# MASTER-SYNTHESIS-D31-D47.md — The Complete KrishiSetu Thesis

Date: 2026-08-16. All 17 uniqueness-wave reports read end to end (d31-d47).
The one report still cooking (d41-refire, global farm practices) will patch
its slot when it lands. This doc is the thesis the product will be judged on.

## THE ONE SENTENCE
A consented Odisha farm-and-crop profile joined to authoritative hazard
feeds, a crop-stage action compiler with deadlines and cost-of-waiting,
a two-phase pre/post event state machine with recovery and claims,
delivered SMS/IVR with offline continuity, validated against replayed
real events, with causal assumptions, uncertainty, tail risk, and
cross-season consequences made explicit in one auditable incident.

## THE BURIED TRUTH (the adaptation gap, d37)
Farmers know the flood comes. They have adapted for generations. The
adaptation stops because the conditions were stripped: tenancy (Odisha's
5.82% leased-in is India's highest), scale (0.95 ha average, 3.6M
marginal), debt (40.5% of rural households, avg Rs 31,000), labor
migration, relief moral hazard, climate mis-calibration, memory decay
between events, and prospect theory's underweighting of rare loss.
CONCLUSION: advisories must optimize DOABILITY, not the message. The
engine ranks actions the farmer can actually execute: it knows labor,
cost, credit, tenancy, and collective context. Nobody else closes this
loop (d39 confirms: feasibility-aware advisories are rare; d38 confirms
the farmer can be the sensor network that feeds it).

## THE HUMAN WISDOM LAYER (d35, d36, d42)
Global + vernacular practice, evidence-graded:
- The universal sequence: protect seed and food, move animals, then people
- Koraput clay-pot + cow-dung seed storage (living tradition, measurable)
- Mangroves VALIDATED: 409-village 1999 study, fewer deaths behind wider belts
- FR13A, an Odisha landrace, became the Sub1 gene inside Swarna-Sub1:
  heritage literally became modern technology (the crown story)
- Sri Lanka tank cascades, qanats, Andean amunas, stilt granaries,
  chinampas, waru waru, bolanha tidal rice, baira floating gardens
  (8-10 day build-up, not an emergency raft), Ethiopian flood-retreat
- Folk indicators are OBSERVATIONS, not warnings: they support IMD,
  never override it. 73/100 farmers use local forecasts, 32% rely alone
- The science-validation tiering: every practice gets A-D grade, and only
  A/B becomes a rule. "Human wisdom, digitized and evidence-graded" is
  claimable. "All ancient wisdom validated" is not.

## THE GLOBAL RECORD (d44, d45, d46)
The completeness mandate, honestly executed: the archives (IBTrACS,
EM-DAT, Dartmouth) cannot certify a literal complete ledger, so every
grade-D row is an explicit unresolved join, never a silent zero. The
usable outcome is the evidence-graded minimum ledger:
- Sidr: 113,000 ha total, 1.4M ha partial, 1.3M tonnes, 100K livestock
- Idai: 715,000+ ha destroyed; Kenneth 55,500 ha
- Remal sequence: 498,300 ha (compound, not cyclone-only, $596M includes floods)
- Rai/Odette: 462,766 ha, P13.3B; Mocha: 327,000 ha, $22.6M, 13K livestock
- Yagi: 286,647 ha rice, 5.76M poultry; Damrey 2017: 59,392 ha
- Michael: $2B+ Georgia; Ian: $1.03B; Helene: $5.5B; Ida timber $300M
- Ditwah (2025): $814M agriculture, Sri Lanka
- Locust: 2.3M ha treated, 4.5M tonnes averted; causation fixed: Mekunu
  and Luban antecedent rain, NOT Idai/Kenneth
- Noise log: Rai/Odette dedup, two Damreys, Remal attribution, all flagged
- Rule seeds extracted: 6 trigger-context rows, each mapped to SMS/IVR
  action + validation target (d44 section 6)
- Effects catalog (d46): complete taxonomy during/immediate/weeks/years +
  positive effects, each with documented cases

## THE CASCADE ENGINE (d47, the crown)
- Typed signed time-sliced DAG: TRIGGER / AMPLIFY / CASCADE / COMPOUND,
  sign positive or negative, with lag, CP, effect distribution, evidence
  scope, source, calibration status per edge
- The Odisha triple is real (Mahanadi+Brahmani+Baitarani shared delta,
  high tide aggravation) but its Gumbel theta must be FITTED, not borrowed
- BN-FLEMO Delta precedent: MAE 0.18, CRPS 0.11, uncertainty-aware flood
  loss; dynamic BN fixes the static-DAG lag problem
- Monte Carlo with convergence gates (pilot + main, precision-based stops)
- 95% CVaR at every loss node, optimized only at action nodes:
  a* = argmin_a {CVaR(total loss|a) + cost(a) + infeasibility(a)}
- The advisory is an evolving incident (IMD 72/48/24/12 stages + CAP
  update semantics): MONITOR -> WATCH -> ALERT -> WARNING -> OUTLOOK ->
  IMPACT_SUSPECTED -> IMPACT_CONFIRMED -> RESPONSE -> RECOVERY ->
  NEXT_SEASON -> CLOSED. RECOVERY feeds NEXT_SEASON; it is not an end
- Four-badge honesty policy on every number: ODISHA-MEASURED /
  TRANSFER-PRIOR / SCENARIO-ASSUMPTION / UNKNOWN
- Calibration anchors: Fani (108,220 ha, Rs 1,304.58 cr, 2 lakh fishers
  evacuated zero casualties) and Yaas (130-140 kmph, 29 cm rain, 2-4 m
  surge over full-moon tide)
- Verdict: GO with a deliberately narrow mathematical core. The pitch:
  "this prototype makes causal assumptions, uncertainty, tail risk, and
  cross-season consequences explicit in one auditable advisory incident."

## THE DOABILITY ENGINE (d38, d39, d40, d31)
- Farmer-as-sensor: keypad before free-form ASR (Avaaj Otalo users chose
  touchtone), real-world Odia ASR WER 35.1%, missed-call callback, DTMF,
  photo capture where phone allows, KCC transcripts as the problem corpus
- The value loop: farmer data -> better advice -> claims evidence ->
  credit visibility -> more data. Consent + opt-out by IVR + deletion.
- Labor is the hidden constraint: Sri Lanka measured 233 man-hours/ha
  manual, 113.5 reaper, 9 combine. "Harvest by 18:00" is a labor question.
- Early harvest: 5.76% real cost (32-study meta, 977 pairs); harvest
  window 45-55 days after heading; delayed-harvest loss 5-11.41%
- Swarna-Sub1: +64 kg/ha per flood day, ~718 kg/ha under severe
  submergence, 180 kg/ha neutral when no flood, 128-village Odisha RCT
- Tillering rice: no yield loss under 4 days inundation, 80% at 6 days
- Salinity: 1.9 dS/m threshold + 9.1%/dS/m, transfer prior, needs local EC
- 32.9% waterlogging loss: global prior, NOT an Odisha coefficient
- Saltol = seedling-stage QTL, no naive tolerance-score addition
- Blast/BPH: real (40-70% losses) but flood is NOT a proven trigger:
  model weather + migration covariates, never a deterministic rule

## THE BUILDABLE DEMONSTRATION (what Round 0 shows)
1. Replay Fani: posterior crop-loss distribution vs the 108,220 ha /
   Rs 1,304.58 cr anchors, with uncertainty band
2. Replay Yaas: surge + tide + rain + embankment + salinity chain
3. CVaR harvest decision: wait vs partial vs immediate, with labor/price
4. Swarna-Sub1 next-season advice: posterior of submergence duration
5. Positive-cascade switch: recharge only for managed-recharge sites
6. The two-contrast demo: high-field mature paddy vs low-field weak
   embankment new transplant, same warning, different advice
7. Farmer reports saline water -> posterior + recommendation update live
8. One Odia SMS/IVR trace through all 11 incident states
9. The doability layer: labor + cost + credit + tenancy visible on every
   recommended action
10. The adaptation-gap story on one slide: why the message never worked,
    and what changes when feasibility is the product

## HONESTY BOUNDARIES (non-negotiable, from the reports)
- No borrowed Odisha copula coefficients, no Hawkes causality claims
- No flood->blast / flood->BPH deterministic rules
- No "flood automatically recharges" without managed infrastructure
- No fish-ingress yield claims (managed rice-fish only)
- No silt yield claims (test salinity/contamination first)
- No 32.9% or 1.9 dS/m presented as Odisha truth (transfer priors)
- No completeness claim for the global ledger: grade-D = unresolved join
- No loss-reduction claims without comprehension + action measurement
- Every number wears one of the four badges
