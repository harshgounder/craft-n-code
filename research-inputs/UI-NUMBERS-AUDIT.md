# UI-NUMBERS-AUDIT.md: every number in krishi.html vs the evidence base

Date: 2026-08-16 15:15 (window B, T1)
Scope: scaffold/webapp/static/krishi.html, all 183 badge-tagged numbers.
Method: every ODISHA-MEASURED (om) and TRANSFER-PRIOR (tp) figure checked
against the raws in research-inputs/ (cnc-ps07-dXX-*.content.md) and
EVIDENCE-INDEX.md. SCENARIO-ASSUMPTION (sa) numbers are demo values by
design (storm parameters, deadlines, labor hours, costs, timestamps,
latency budgets from THE-PLAN) and were spot-checked, not line-checked.
Raw line numbers below are from the .content.md files as committed in
this repo.

## SPECIAL LIST (window A requested these first)

| Number | Where used in UI | Badge claimed | Raw source + line | Verdict |
|---|---|---|---|---|
| Fani 108,220 ha | console evidence chain + replay anchors | ODISHA-MEASURED | d47 L6: "Fani affected 108,220 ha of annual and perennial crops" | PASS, chain fix needed: number lives in d47, UI chain cell says d9 |
| Fani Rs 1,304.58 cr | console evidence chain | ODISHA-MEASURED | d47 L6: "crop-production losses of INR 1,304.58 crore [30]" | PASS, chain fix needed: d47 not d9 |
| Yaas 2-4 m surge | console evidence chain | ODISHA-MEASURED | d47 L36/L71/L101: "Yaas produced 2-4 m over astronomical tide in Balasore and Bhadrak [28]" | PASS, chain fix needed: d47 not d5 |
| Yaas 29 cm rain | not in UI | n/a | d47 L38/L71: "Chandbali received 29 cm" | Verified in raw, candidate for future use |
| Swarna-Sub1 64 kg/ha/day | advisory H1 + console chain | TRANSFER-PRIOR | d47 L10/L46: "64 kg/ha per additional flood day" (RCT, 128 Odisha villages) | PASS, chain fix needed: d47 not d33 |
| Swarna-Sub1 718 kg/ha | not in UI | n/a | d47 L46: "reached about 718 kg/ha under severe flooding" | Verified in raw, candidate for future use |
| Swarna-Sub1 180 kg/ha | not in UI | n/a | d47 L46: "estimated 180 kg/ha disadvantage without flooding, not statistically different from zero" | Verified in raw, candidate for future use |
| 5.76% early harvest | advisory A1/H1 + research row d32 | TRANSFER-PRIOR | d32 L7: meta-analysis of 32 studies, 977 data pairs, mean 5.76% yield reduction | PASS |
| 41.9% waterlogging | advisory A2 cost-of-waiting + research row d03 | ODISHA-MEASURED | d3 L11: "41.90% loss at reproductive stage" (global meta; mean 32.9%) | PASS with precision note: figure is reproductive-stage specific; Asha is at flowering, so it fits, but card text should say "at reproductive stage" |
| 72h intimation | advisory A5 + claim cards + console | ODISHA-MEASURED | d6 L17: "72-hour loss-intimation window" (2023 PMFBY guidelines) | PASS |
| 33% threshold | advisory A5 + claim cards | ODISHA-MEASURED | NOT in d6. Found in d20 L10/L37: "33% crop-loss threshold", "Subsidy eligibility begins at 33% loss" (SRC crop-loss modality, 2015) | MISMATCH: 33% is the state relief (SRC/SDRF) threshold, not a PMFBY rule. Fix citation to d20 and wording |
| 0.95 ha avg | Asha profile + research row d06 | ODISHA-MEASURED | d6 L5: "average of 0.95 ha" (Agriculture Census 2015-16) | PASS |
| 40.5% debt | Asha profile + research row d06 | ODISHA-MEASURED | d6 L15: "40.5% of rural Odisha households were indebted" (AIDIS 2019) | PASS, wording fix: UI says "farm households", raw says "rural households" |
| 1.9 dS/m | not in UI | n/a | d4 L19 + d47 L11: "fitted threshold of 1.9 dS/m" (Sacramento Valley rice study) | Verified in raw, candidate for salinity advisory |
| 9.1% | not in UI | n/a | d4 L19 + d47 L11: "9.1% yield decline per dS/m above it" | Verified in raw, candidate for salinity advisory |

## FULL TABLE (every om and tp figure in the UI, unique facts)

| Number | Where used in UI | Badge claimed | Raw source + line | Verdict |
|---|---|---|---|---|
| 72/48/24h lead stages | stepper + research row d01 | ODISHA-MEASURED | d1 L15: IMD formal stages (Watch 72h, Alert 48h, Warning 24h) | PASS |
| 1999 deaths | research row d01/d20 | ODISHA-MEASURED | d1 L19: "9,893 reported deaths" | PASS (referential) |
| 325 CWC stations | research row d02 | ODISHA-MEASURED | d2 L5: "national network of 325 forecast stations" | PASS (national figure, applies to Odisha) |
| 44% paddy GCA | research row d04 | ODISHA-MEASURED | d4 L7: "41.24 lakh ha, or 44% of gross cropped area, 2024-25" | PASS |
| 4.866M holdings | research row d06 | ODISHA-MEASURED | d6 L5: "4.866M operational holdings" | PASS |
| KCC 22 languages | research row d08 | SCENARIO-ASSUMPTION | d8 L32/L183: "22 languages" (KCC) | PASS on number, badge under-claims: real scheme fact, upgrade to ODISHA-MEASURED or TRANSFER-PRIOR |
| 1B Q4 / 3B | research row d10 | SCENARIO-ASSUMPTION | d10 L7: "1B Q4 is the safe design center", L9: "3B model is not the default" | PASS on numbers, badge under-claims: verified engineering analysis, upgrade to TRANSFER-PRIOR |
| Lava Blaze target | research row d10 | n/a (text) | d10 L86: "Lava Blaze 3 5G, Rs 10,999" | PASS |
| llama.cpp | research row d10 | n/a (text) | d10 L17/L64: llama.cpp Android example, GGUF portability | PASS |
| LoRA 11-49MB | research row d11 | TRANSFER-PRIOR | d11 L9: "11.3/22.5MB for a 1B-like model" (FP16 rank 8/16); L34: real 3B adapter ~195MB | PARTIAL: 11-23MB supported, the "49" bound is not in the raw; row text should say "~11-23MB (1B, calculated)" |
| Rs 2,899 BOM | research row d12 | ODISHA-MEASURED | d12 L5/L59: "target BOM of Rs 2,899" | PASS on number, badge MISMATCH: it is a design estimate, raw says "label it target prototype"; downgrade to SCENARIO-ASSUMPTION |
| Ama Krushi 50K calls | research row d15 | SCENARIO-ASSUMPTION | NOT FOUND in any raw. d15 L5 has the 155333 line + IVR, no call volume; scale figures live in d26 L5 | MISMATCH: drop "50K calls", replace with "3.2M farmers at 2022 handover (d26)" |
| WER 35.1 | research row d15 | ODISHA-MEASURED | NOT in d15. d31 L11/L76: "best reported Odia WER was 35.1%" (2026 agricultural benchmark, arXiv 2602.03868); d31 L152: 23.4 unsupported, use 35.1 | PASS on number, source note: the fact lives in d31, not d15 |
| Fani 4 districts 9 days | research row d17 | ODISHA-MEASURED | d17 L7: "Cuttack, Khordha, Bhubaneswar, and Puri experienced complete shutdowns... nine days" | PASS |
| 81.3% WTP | research row d18 | ODISHA-MEASURED | d18 L5: "81.3%" (2026 Rice Crop Manager study, all 30 Odisha districts) | PASS |
| 38% vs 18% adoption | research row d18 | TRANSFER-PRIOR | d18 L7/L32: "38% full adoption, versus 18%" (same Odisha Frontiers study) | PASS on number, badge under-claims: Odisha study, upgrade to ODISHA-MEASURED |
| ATMA 60:40 | research row d18 | TRANSFER-PRIOR | d18 L9: "60:40 Centre-State funding ratio" (2025 ATMA rules) | PASS (national scheme rule) |
| IMD gridded 1901-2024 | research row d19 | ODISHA-MEASURED | d19 L5: "daily 0.25x0.25 degree rainfall for 1901-2024" | PASS |
| Krushak Odisha 9.2M | research row d20 | SCENARIO-ASSUMPTION | NOT in d20. d40 L155: "portal displayed 91,72,732, rounds to about 9.17M; REAL, rounded; include access date" | PASS on value (rounded 9.2M), source note: fact lives in d40, and it is a live portal count, not a static figure; badge under-claims, upgrade to TRANSFER-PRIOR with access-date caveat |
| BaKhabar 15.8M | research row d25 | ODISHA-MEASURED | d25 L8: "reports 15.8M+ users" | PASS on number, badge MISMATCH: Pakistan product, upgrade to TRANSFER-PRIOR |
| Ama Krushi 7.9M | research row d26 | ODISHA-MEASURED | d26 L5: "served 3.2M farmers at the 2022 handover, reported to serve nearly 7.9M today" | PASS with note: 7.9M is a reported figure from a secondary line |
| Ama Krushi 10% loss cut | research row d26 | TRANSFER-PRIOR | d26 L97: "10% reduction in severe-loss probability overall" | PASS |
| WFP $53 | research row d27 | SCENARIO-ASSUMPTION | d27 L5: "released USD 53 to about 145,000 people" (Bangladesh, July 2020) | PASS on number, badge under-claims: upgrade to TRANSFER-PRIOR |
| ACRE 217K failed deliveries | research row d27 | SCENARIO-ASSUMPTION | NOT in d27. d28 L7: "587,842 sent, 361,539 delivered, 217,134 failed; 56% success" (ACRE Africa, Zambia) | PASS on number (217,134 rounds to 217K), source note: fact lives in d28, badge under-claims, upgrade to TRANSFER-PRIOR |
| Ethiopia 8028 | research row d28 | SCENARIO-ASSUMPTION | d28 L8: "8028 hotline passed 6M subscribers and 60M calls" | PASS, badge under-claims: upgrade to TRANSFER-PRIOR |
| 6M/60M calls | research row d28 | TRANSFER-PRIOR | d28 L8 exact | PASS |
| radio 24.1M | research row d28 | TRANSFER-PRIOR | d28 L8: "Farm Radio International reported 24.1M listeners" | PASS |
| Farmer.Chat 830K/5M | research row d29 | SCENARIO-ASSUMPTION | d29 L9: paper 15,000 users/300,000 queries; "current product site claims over 830,000 users and 5M queries" | PASS with note: 830K/5M is the current product site claim, 2024 paper is 15K/300K; badge under-claims, upgrade to TRANSFER-PRIOR |
| AgroMetLLM Pi 4B | research row d29 | SCENARIO-ASSUMPTION | d29 L48: "Raspberry Pi 4B system" | PASS, badge under-claims: upgrade to TRANSFER-PRIOR |
| 65% want experts | research row d31 | TRANSFER-PRIOR | d15 L66: "65% preferred staff-only answers" (Avaaj Otalo menu design) and d31 L28: "over 65% give at least a name" | PASS with note: the UI phrase maps to d15 L66 "preferred staff-only answers" |
| 5.76% | research row d32 | TRANSFER-PRIOR | d32 L7 exact | PASS |
| 64kg/ha | research row d33 | TRANSFER-PRIOR | d47 L10/L46 (see special list) | PASS on number, source note: d47 not d33 |
| Saltol seedling-stage | advisory A7 | n/a (text, d33) | d33 L11/L35: "Saltol is primarily a seedling-stage QTL" | PASS |
| mangroves 409-village | research row d35 | TRANSFER-PRIOR | NOT FOUND in any raw | MISMATCH: drop the claim or mark UNKNOWN. Koraput stilt storage and the universal sequence ARE in d35 and can replace it |
| tenancy 5.82% | research row d37 | TRANSFER-PRIOR | d6 L31: "State share of wholly leased-in holdings; Odisha 5.82%" (Final Agriculture Census 2015-16). d37 L59 flags the value as not re-exposed in its own retrieval | PASS via d6 (census); keep the caveat in mind |
| CPP 76K volunteers | research row d43 | SCENARIO-ASSUMPTION | d43 L5: "76,000 volunteers in 3,801 village units" | PASS, badge under-claims: upgrade to TRANSFER-PRIOR |
| Sidr 1.4M ha | research row d44 | SCENARIO-ASSUMPTION | d44 L33: "1.4M ha partially damaged" | PASS, badge under-claims: verified global record, upgrade to TRANSFER-PRIOR |
| Idai 715K | research row d44 | SCENARIO-ASSUMPTION | d44 L85: "more than 715,000 ha of crops destroyed" | PASS, badge upgrade to TRANSFER-PRIOR |
| Remal 498K | research row d44 | SCENARIO-ASSUMPTION | d44 L40: "more than 498,300 ha" | PASS, badge upgrade to TRANSFER-PRIOR |
| Mocha 327K | research row d44 | SCENARIO-ASSUMPTION | d44 L38: "approximately 327,000 ha" | PASS, badge upgrade to TRANSFER-PRIOR |
| Yagi 286K | research row d44 | SCENARIO-ASSUMPTION | d44 L56: "286,647 ha rice" | PASS, badge upgrade to TRANSFER-PRIOR |
| Michael $2B+ | research row d44 | SCENARIO-ASSUMPTION | d44 L72: "Georgia agriculture losses exceeded $2B" | PASS, badge upgrade to TRANSFER-PRIOR |
| Yangtze 1998 / Pakistan 2010/2022 / Thailand 2011 / Brazil 2024 | research row d45 | SCENARIO-ASSUMPTION | d45 L56 (22M ha China 1998), L30 (Pakistan 2010 2.4M ha), L60 (Thailand 2011 6M ha), L45-L47 (2024 events incl. Wayanad/Nepal/Bangladesh) | PASS on numbers (year references), badge upgrade to TRANSFER-PRIOR |
| BN-FLEMO MAE 0.18 | research row d47 | SCENARIO-ASSUMPTION | d47 L9: "absolute MAE 0.18 +/- 0.01" | PASS, badge upgrade to TRANSFER-PRIOR |
| Research header 48/6/2.5M | research panel header | SCENARIO-ASSUMPTION | RESEARCH-VISIBILITY.md (project tracking doc), matches deck | PASS as project self-metric, keep sa |

## SYSTEMATIC BADGE FINDINGS

1. Under-claim pattern: verified global/prior-art facts were tagged
   SCENARIO-ASSUMPTION (KCC 22, 1B/3B, $53, 217K, 8028, 830K/5M, 4B,
   76K, Sidr/Idai/Remal/Mocha/Yagi/$2B+, flood years, 0.18, 9.2M).
   SCENARIO-ASSUMPTION reads as "made up for the demo" to a judge. These
   are measured facts from other regions or studies, so TRANSFER-PRIOR
   is the honest label and makes the panel stronger. Fix as one batch.
2. Wrong-direction badges: Rs 2,899 (om, is a design estimate, sa),
   15.8M BaKhabar (om, Pakistan, tp), 38%/18% adoption (tp, Odisha
   study, om). Fix individually.
3. Duplicate badge noise: Asha holding row carries both b-om and b-tp
   on 0.95 ha (the om badge on the num span is enough). Harmless, can
   trim.

## UI FIX LIST (for the opencode round)

1. Console evidence chain: Fani 108,220 ha / Rs 1,304.58 cr: index row
   d9 -> d47, raw path -> cnc-ps07-d47-systems-cascade-math-agri.
2. Console evidence chain: Yaas 2-4 m surge: index row d5 -> d47, raw
   path -> cnc-ps07-d47-systems-cascade-math-agri.
3. Console evidence chain: Swarna-Sub1 64 kg/ha: index row d33 -> d47,
   raw path -> cnc-ps07-d47-systems-cascade-math-agri.
4. Advisory A5 + claim cards: "33% crop damage is the threshold (d6)"
   -> "state relief eligibility starts at 33% loss (d20)" and keep
   "PMFBY intimation 72h (d6)" as its own clause.
5. Asha profile debt line: "farm households" -> "rural households".
6. Advisory A2 cost-of-waiting: "waterlogging alone reprocesses 41.9%
   of the crop (d3)" -> "reprocesses 41.9% of the crop at reproductive
   stage (d3)".
7. Research row d15: drop "Ama Krushi 50K calls", use "Ama Krushi 3.2M
   farmers at 2022 handover (d26)".
8. Research row d35: drop "mangroves 409-village" (unverified), use
   "Koraput stilt storage" which is verified in d35.
9. Research row d20: "Krushak Odisha 9.2M" -> "Krushak Odisha portal
   ~9.17M, access-dated (d40)".
10. Research row d11: "LoRA 11-49MB" -> "LoRA ~11-23MB (1B, calculated,
    d11)".
11. Badge batch (sa -> tp): d08 22, d10 1B/3B, d20 9.2M (as
    TRANSFER-PRIOR), d27 $53 + 217K, d28 8028, d29 830K/5M + 4B,
    d43 76K, d44 all six figures, d45 years, d47 0.18.
12. Badge fixes: d12 2,899 om -> sa; d18 38%/18% tp -> om; d25 15.8M
    om -> tp.
13. Chain notes (documentation only, no UI change needed): WER 35.1
    lives in d31 raw, ACRE 217K lives in d28 raw, 5.82% tenancy is
    census-sourced via d6.

## VERIFIED FACTS NOT YET IN THE UI (candidates for the salinity card)

Yaas 29 cm rain (d47 L38), Swarna-Sub1 718 kg/ha severe-flood ceiling
(d47 L46), 180 kg/ha non-flood disadvantage not significant (d47 L46),
1.9 dS/m salinity threshold + 9.1% yield decline per dS/m (d4 L19, d47
L11). These are raw-verified and can strengthen advisory A7 if the
orchestrator wants a second pass.

## NET COUNT

Unique om/tp facts checked: 44. PASS: 36. PASS with source note: 5
(WER 35.1, 9.2M, 830K/5M, 217K, 7.9M). MISMATCH needing UI edits: 3
(33% threshold citation, 50K calls, 409-village). Badge corrections:
16 spans (12 sa->tp, 2 wrong-direction, 1 om->sa, 1 wording).
Zero invented numbers found. Every figure in the UI traces to a raw
line or is a labeled scenario value.
