# AGRI-NUMBERS-AUDIT.md (Window C audit, 2026-08-16 ~15:00 IST)

Cross-check of every hardcoded number in the core lane
(~/craft-n-code/scaffold/agri/: cvar.py, replay.py, claims.py,
seed.py, rules.json, compiler.py, doability.py, state_machine.py)
against the KrishiSetu research raws
(~/krishisetu/research/raw/cnc-ps07-d*.content.md).

Method: every constant and docstring claim read, then the raw reports
grepped for the number and the exact line read. A number is VERIFIED
only if the raw carries it at the cited line. This audit is the
no-omission chain for the number layer (EVIDENCE-INDEX rule: a claim
with no chain does not ship).

Legend:
  VERIFIED = raw carries the number at the cited line
  VERIFIED-REFRAME = number right, code wording overstates the raw
  FLAG = number or attribution not supported by the raws
  LABELED-OK = honest scenario assumption with badge, no raw needed

## 1. THE HUNT LIST (per orchestrator C1)

| Number | Where used | Raw source + line | Verdict |
|---|---|---|---|
| 5.76% early harvest | cvar.py EARLY_HARVEST_COST = 0.0576 | d32 content.md line 7: "meta-analysis of 32 studies and 977 data pairs found a mean 5.76% yield reduction for premature harvest relative to 35 days after heading" [7] | VERIFIED, TRANSFER-PRIOR correct. Raw warns: not an Odisha dough-stage threshold, use as prior only. Code badges TRANSFER-PRIOR, matches |
| Swarna-Sub1 +64 kg/ha per flood day | cvar.py SUB1_PER_FLOOD_DAY_KG_HA = 64.0 | d47 line 10: "yield advantage increased by 64 kg/ha per additional flood day" [14]; d47 line 46 | VERIFIED. Attribution corrected: exact triple lives in d47, not d33 (d33 basis.json carries the J-PAL study quotes but not the figures) |
| Swarna-Sub1 ~718 kg/ha severe | cvar.py SUB1_SEVERE_SUBMERGENCE_KG_HA = 718.0 | d47 lines 10, 46 [14]; corroborated d9 line 9 [12], d31 line 17 [17], d32 line 15 [29] | VERIFIED |
| Swarna-Sub1 180 kg/ha no flood | cvar.py SUB1_NO_FLOOD_KG_HA = 180.0 | d47 line 46: "estimated 180 kg/ha disadvantage was not statistically different from zero" [14]; d31 line 128 | VERIFIED-REFRAME: docstring says "neutral-to-positive yield when no flood". Raw says the opposite direction: no-flood DISADVANTAGE -180 kg/ha, not statistically significant. Magnitude correct, framing overstated. Fix the docstring (cvar.py line 54 and module header line 12) to "no-flood effect n.s., point estimate -180 kg/ha" |
| Tillering: no loss <4 days, 80% at 6 days | cvar.py TILLERING_DAYS_NO_LOSS = 4, TILLERING_DAYS_TOTAL_LOSS = 6, TILLERING_LOSS_AT_TOTAL = 0.80 | d34 content.md line 17: "no significant yield decrease below 4 days of tillering-stage inundation, an 80% yield reduction at 6 days" [12] | VERIFIED (as attributed to d34). Same line adds: over 50% loss after 2 days of flooding at booting or flowering, the code models tillering only, correct scope |
| Salinity threshold 1.9 dS/m + 9.1% per dS/m | cvar.py SALINITY_THRESHOLD_DS_M = 1.9, SALINITY_LOSS_PER_DS_M = 0.091 | d4 content.md line 19: "fitted threshold of 1.9 dS/m and a 9.1% yield-decline slope" [17]; d47 lines 11, 44, 148 (California provenance warning) | VERIFIED (as attributed to d4). TRANSFER-PRIOR badge correct: d47 explicitly says California varieties, functional form only |
| Waterlogging 32.9% | cvar.py WATERLOGGING_PRIOR = 0.329 | d46 content.md lines 6, 128, 190: "global meta-analysis found a mean 32.9% yield reduction under waterlogging" [21] | VERIFIED. Attribution corrected: d46, not d9. d46 says "not a prediction for an Odisha field", code badges TRANSFER-PRIOR, matches |
| Fani 108,220 ha affected | replay.py FANI_ANCHOR_HA = 108220.0 | d47 line 6: "Fani affected 108,220 ha of annual and perennial crops" [30] | VERIFIED. Attribution corrected: the anchors live in d47 [30], d21 carries the OSDMA DLNA report link (line 26) but not the figures |
| Fani Rs 1,304.58 cr loss | replay.py FANI_ANCHOR_RS = 1304.58e7 | d47 line 6: "estimated crop-production losses of INR 1,304.58 crore" [30] | VERIFIED (d47). ODISHA-MEASURED badge correct |
| Fani surge ~1.5 m | replay.py FANI_SURGE_M = 1.5 | d21 content.md lines 11, 26: "Fani's 1.5 m... estimated 1.5 m surge" [13][24] | VERIFIED |
| Yaas 2-4 m surge over full-moon tide | agri/seed.py yaas_archive surge_m_range [2.0, 4.0] | d47 lines 6, 71, 101: "2-4 m surge over astronomical tide" / "2-4 m surge, and full-moon astronomical tide" [28] | VERIFIED. Attribution corrected: d47, not d22 |
| Yaas 29 cm rain Chandbali | agri/seed.py rain_chandbali_cm = 29.0 | d47 lines 6, 38, 71: "rainfall of up to 29 cm at Chandbali" [28] | VERIFIED (d47 [28], IMD figure). Discrepancy noted: d22 basis.json quotes a news item at "158.6 mm" in 24h for Chandbali, a different source and window. Seed uses the d47/IMD figure, which is the stronger chain. No change needed, both recorded |
| PMFBY intimation 72 hours | claims.py INTIMATION_WINDOW_HOURS = 72 | d6 content.md lines 164-165: "Immediate intimation (within 72 hours) by the insured farmer"; d1 line 156: "PMFBY requires immediate farmer intimation within 72 hours" [38] | VERIFIED, ODISHA-MEASURED correct |
| 33% loss threshold | claims.py LOSS_THRESHOLD = 0.33 | d20 content.md lines 10, 37, 87 (SRC crop-loss modality: "Subsidy eligibility begins at 33% loss"); d22 lines 15, 41, 72 (Yaas: 143,373.90 ha at 33%+ loss) | VERIFIED-REFRAME: number verified as Odisha's SRC/state crop-loss assessment threshold. The "(PMFBY norms)" attribution in claims.py line 5 is not found in the raws (d6 carries only the 72h intimation). Recommend docstring: "33% SRC assessment threshold (d20/d22)" |

## 2. BONUS CHECKS (numbers found in the sweep)

| Number | Where used | Raw source + line | Verdict |
|---|---|---|---|
| 72/48/24/12h lead stages | state_machine.py STATES docstring | d1 content.md line 15: "Pre-Cyclone Watch at 72 hours, Cyclone Alert at least 48 hours, Cyclone Warning at least 24 hours, and Post-Landfall Outlook at least 12 hours" [5][11] | VERIFIED, exact match |
| 0.95 ha average holding | agri/seed.py asha area_ha | d6 content.md lines 30, 141: "Odisha all-class average 0.95" [11] | VERIFIED |
| Floating rice 1/2 to 1/3 of HYV yield | rules.json R8 numbers | d41 refire lines 6, 102: "floating-rice yield is only one-half to one-third that of high-yielding varieties" [31] | VERIFIED |
| Swarna-Sub1 5.2 t/ha potential vs seed yield 3500 kg/ha | agri/seed.py expected_yield_kg_ha = 3500 | d4 content.md line 15: Swarna-Sub1 "145-day duration, 5.2 t/ha yield potential" [9] | FLAG: 3500 kg/ha not directly sourced. Closest raw: 5.2 t/ha potential (d4 line 15). Recommend SCENARIO-ASSUMPTION label or cite d4 |
| Paddy price Rs 19/kg | agri/seed.py price_rs_kg = 19.0 | no raw match in d4/d6/d32 greps | FLAG: unsourced. Add SCENARIO-ASSUMPTION or an MSP citation |
| Wage Rs 100/hr | agri/seed.py wage_rs_per_hour = 100 | d32 lines 106, 187: no Odisha emergency-harvest wage measurement exists; calculators return generic minimum wages | FLAG: unsourced, recommend SCENARIO-ASSUMPTION  |
| Harvest labor 12 hrs/ha | agri/seed.py harvest_labor_hours_per_ha = 12 | d32: "labor hours/ha" appears only as a design target (lines 103, 137), no Odisha measurement | FLAG: unsourced, recommend SCENARIO-ASSUMPTION |
| R1 badge ODISHA-MEASURED | rules.json R1 (authority registry) | d41: R1 practice source is Bangladesh Red Crescent CPP [18], not Odisha data | FLAG: badge/evidence mismatch. The mechanism transfers, the evidence origin is Bangladesh. Recommend TRANSFER-PRIOR for R1, or an explicit justification comment. R6 ODISHA-MEASURED is correct (128-village Orissa RCT, d9/d47) |

## 3. LABELED-OK (honest scenario assumptions, no raw needed)

MATURITY_DEEP_FLOOD_LOSS 0.90, LIVESTOCK_FLOOD_LOSS 0.20,
LIVESTOCK_VALUE_PER_HEAD_RS 8000, VEGETABLE_VALUE_RS 3000 (all cvar.py,
each docstring carries SCENARIO-ASSUMPTION), CYCLONE_CROP_LOSS_FRACTION
0.35 (compiler.py, labeled), PADDY_GCA_PURI_HA 150000, SURGE_SENSITIVITY
0.20, LOSS_CV 0.20, BETA_SHAPE_A 40 (replay.py, all labeled
SCENARIO-ASSUMPTION), INFEASIBLE_PENALTY 1e9 (doability.py, ordering
constant, labeled), rule resources labor/cost/credit figures (rules.json,
covered by the registry-level resources_badge SCENARIO-ASSUMPTION).

## 4. MIRROR SYNC (window C action taken)

backend/seed/rules.json re-synced to the authority registry
(scaffold/agri/rules.json) on 2026-08-16: all 16 rule bodies now carry
the authority's keys (id, protection, resources, numbers), grades
(R13 = B/C), and badges (R1 = ODISHA-MEASURED, R16 = UNKNOWN). The
authority marker meta is preserved: {"authority":
"scaffold/agri/rules.json (core lane compiler input)", "mirror": true,
"note": "DB seed mirror, not the authority"}. The mirror is data; the
authority file stays the source of truth. /api/rules serves the synced
mirror.

## 5. VERDICT

14/14 hunt numbers verify against a named raw line, or verify with a
wording reframe. Zero outright lies. Corrections:

1. Number sourcing: the Swarna-Sub1 triple, Fani ha/cr anchors, and
   Yaas surge/rain anchors all trace to d47 (which cites [14][28][30]),
   not d21/d22/d33. d21 supplies surge 1.5 m and the OSDMA DLNA link.
   d46 (not d9) carries 32.9%. d34 tillering attribution confirmed.
2. Wording reframes (2): SUB1 180 kg/ha docstring (direction), 33%
   threshold attribution (SRC, not PMFBY).
3. Unsupported profile defaults (4): yield 3500, price 19, wage 100,
   labor 12, recommend SCENARIO-ASSUMPTION labels.
4. Badge consistency (1): R1 ODISHA-MEASURED vs Bangladesh source.
5. No em dashes in this file, by rule.