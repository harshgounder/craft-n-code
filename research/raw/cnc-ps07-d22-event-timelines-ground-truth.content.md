# Replay-Ready Ground Truth for Odisha Cyclone Advisories

## 1. EXECUTIVE SUMMARY

- **Replay Verdict**: The evidence supports a **PARTIAL** build. Hazard tracks, warning milestones, landfall, evacuation, shelters, and headline crop damage can be replayed, but farmer-message delivery, observed farm actions, event-linked payouts, and plot recovery cannot yet be causally validated. For example, Fani has a roughly **67-hour watch-to-landfall interval**, 1,557,170 evacuees, and 1.49 lakh affected crop hectares, but no matched farmer-level action panel [31]. -> Build the hazard and public-warning replay now; gate claims about crops saved.

- **Warning-System Transformation**: In 1999, Odisha received more than 48 hours of warning, shifted nearly 150,000 people, and had 23 permanent shelters protecting about 30,000 people [20]. By Fani, the state used 1.8 crore SMS messages, hourly coastal voice messages and sirens, and more than 9,000 safe shelters [31]. -> Model warning capacity by event year; never back-cast today's last-mile system into 1999.

- **Best Human-Response Anchors**: Phailin evacuated 983,642 people for the cyclone and another 171,083 for subsequent flooding; Hudhud evacuated 255,043 into 2,143 shelters; Yaas evacuated 7.02 lakh into 8,410 shelters [17][6][18]. -> These are strong checks on evacuation and shelter modules, but not on farm-action compliance.

- **Farm-Advice Audit Trail Is the Bottleneck**: The only clearly dated, crop-specific pre-landfall item recovered is the **23 October 2024** ICAR-NRRI Dana advisory: keep rice drainage channels open, remove excess water, and protect harvested rice with tarpaulin [28]. Historical Meghdoot/AAS delivery logs for 1999, Phailin, Fani, Amphan, and Yaas were not recovered. -> Store synthetic recommendations separately from historically observed messages.

- **Damage Data Are Thresholded, Not Plot-Level**: Phailin recorded 651,490 ha with more than 50% crop loss and Rs 2,300 crore in estimated crop losses; Hudhud recorded 247,557 ha affected, 40,484.50 ha with more than 50% loss, and Rs 582.07 crore in crop loss [17][6]. -> Validate district and event aggregates, not individual-farm loss predictions.

- **The Seven-Day Rule Is a Workflow, Not an Outcome Dataset**: Odisha's procedure uses a Revenue Inspector, Village Agricultural Worker, and Horticulture Extension Worker; records farmers at or above 33% loss; completes village crop cutting within seven days; allows three days for objections; and pays by e-transfer [1]. -> Simulate assessment latency and eligibility, but do not infer that a stated subsidy requirement was actually paid.

- **Yaas Supplies the Clearest Recovery Constraint**: One month after Yaas, at least 5,882 ha in five Balasore blocks and around 1,400 ha in three Bhadrak blocks had seawater impacts; about 300 farmers remained uncertain about kharif sowing while OUAT and NRRI tested salinity and sought salt-tolerant crops [7]. -> Add a salinity state variable and delayed-sowing branch, but calibrate persistence only after obtaining soil-test time series.

- **Early Harvest Has a Real Opportunity Cost**: A rice harvest-time meta-analysis found that harvesting earlier than the 35-days-after-heading comparator reduced yield by **5.76%** [23]. -> Recommend emergency early harvest only when modeled cyclone loss exceeds this maturity penalty; do not treat early harvest as costless.

- **Insurance and Compensation Remain Non-Attributable**: Odisha PMFBY claims are available only as annual totals, from Rs 1,170.50 crore in 2018-19 to Rs 497.10 crore in 2022-23, without cyclone attribution [32]. -> PMFBY, KALIA, and state payment ledgers must be joined at season, district, peril, and beneficiary level before payout validation.

## 2. EVENT DATASET

### Reliability scale

- **A**: Contemporaneous or official first-party report with timestamps or administrative tables.
- **B**: Government-partner, multilateral, institutional, or attributed news report with useful but incomplete data.
- **C**: Secondary narrative, preliminary estimate, or source with unclear method.
- **D**: Tertiary, promotional, undated, conflated, or unsuitable for ground truth.

### Source inventory by event

| Event | What exists | Named source, URL and date | Format | Resolution | Access | Reliability |
|---|---|---|---|---|---|---|
| **1999 Super Cyclone** | Warning milestones, dissemination chain, landfall, evacuation, CWDS and shelter use | IMD, *Orissa Super Cyclone: A Synopsis*, https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/449/450/1763, retrospective IMD paper; Odisha SRC damage memorandum, https://www.srcodisha.nic.in/odia/data/MEMORANDUM-1999.pdf, 1999 | PDF | Day and selected clock times; state or coastal aggregate | Open, but the damage PDF was not fully machine-extractable | A for warning; B for currently extractable damage |
| **Phailin, 2013** | Full IMD development and warning narrative; state evacuation, relief, crop and livestock totals | IMD Phailin Report, https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_38a1d4_phailin.pdf, October 2013; Odisha SRC Memorandum, http://srcodisha.nic.in/calamity/MEMORANDUM.pdf, 2013 | PDF | Sub-daily warning milestones; event and some district administrative totals | Open | A |
| **Hudhud, 2014** | State warning chronology, district evacuation/shelter table, crop-loss table, relief and infrastructure recovery | Odisha SRC Hudhud Memorandum, https://srcodisha.nic.in/calamity/Memorandum%20Cyclone%20Hudhud%202014.pdf, 2014; post-event crop advisory, https://agriculture.vikaspedia.in/viewcontent/agriculture/best-practices/sustainable-agriculture/crop-management/advisory-1-for-hudhud-affected-areas-in-andhra-pradesh-and-odisha?lgn=en | PDF and HTML | Dated administrative milestones; district aggregates; crop-specific but undated web advice | Open | A for memorandum; B-C for advisory timing |
| **Fani, 2019** | Watch, alert and warning milestones; landfall; mass warning channels; evacuation, shelters, crop loss and input-subsidy requirement | IMD Fani Report, https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_7122ae_Preliminary%20Report%20on%20ESCS%20FANI_15082020.pdf, report updated 2020; Odisha SRC Fani Memorandum, https://srcodisha.nic.in/calamity/Memorandum_Cyclone%20FANI_3rd%20May%202019.pdf, 2019; OSDMA DLNA landing page, https://www.osdma.org/publication/cyclone-fani-2019-dlna-report, July 2019 | PDF and HTML | Timestamped warning stages; event and district administrative tables; sector-level needs | Open | A |
| **Amphan, 2020** | Odisha evacuation and shelter totals, affected population, crop area, affected crops, assessment orders | OSDMA Amphan Update, https://www.osdma.org/cyclone-amphan-update/, May 2020; attributed state briefing, https://www.indiatoday.in/india/story/cyclone-amphan-hits-45-lakh-odisha-naveen-patnaik-seeks-house-damage-report-7-days-1680576-2020-05-21, 21 May 2020 | HTML | Statewide totals; named districts; no full bulletin sequence | Open | B |
| **Yaas, 2021** | IMD-to-state warning milestone, evacuation and shelters, affected crop area, >=33% crop loss, input-subsidy requirement, embankment damage and restoration | Odisha SRC Yaas Memorandum, https://srcodisha.nic.in/calamity/Yass%20Cyclone%202021-%20Memorandum_compressed.pdf, 2021; Down To Earth salinity report, https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568, 21 June 2021 | PDF and HTML | Event and district totals; block-level saline-area reporting; one-month recovery snapshot | Open | A for memorandum; B for field recovery |
| **Dana, 2024** | Forecast-lead and error verification, landfall, evacuation/shelter estimates, dated rice advisory, rapid needs reports | IMD Dana Report, https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf, 7 November 2024; Sphere India SitRep, https://www.sphereindia.org.in/sites/default/files/2025-04/SI%20Sitrep-2__Cyclone%20Dana%20OD-WB%20%28Post%29_25%20Oct%20%2724_1800%20Hrs.pdf, 25 October 2024; ICAR-NRRI advisory report, https://www.etvbharat.com/en/!bharat/cyclone-dana-icar-issues-advisory-for-standing-crops-in-littoral-odisha-enn24102306576, 23 October 2024 | PDF and HTML | Timestamped forecast stages and errors; state response totals; crop-specific advice | Open | A for IMD; B for response and advisory delivery |

### 1999 Super Cyclone: technically warned, weakly observable at the last mile

IMD informed the Andaman administration on 25 October, began cyclone bulletins on 26 October, issued coastal alerts for West Bengal, Orissa and north Andhra Pradesh on the morning of 27 October, and began regular Odisha warning bulletins late that evening. Warnings were upgraded to 240-260 km/h winds and a 4-5 m surge, and continued until 13:15 IST on 31 October [20]. The report calls the coastline threat a three-day warning and says Bhubaneswar's warning was issued more than 48 hours before the cyclone struck [20].

Nearly 150,000 people were shifted across Puri, Bhadrak, Jagatsinghpur, Kendrapara and Balasore. Odisha had 35 Cyclone Warning Dissemination Systems, while 23 Red Cross cyclone shelters protected about 30,000 people [20]. The only recoverable sectoral advice is for fishers not to venture to sea [20]. There is no timestamped farm message, farmer-action survey, machine-readable district crop table, compensation ledger, or measured field-recovery series in the extracted corpus. The official damage memorandum exists, but the accessible extraction exposed only its annexure description, not the crop figures [33].

### Phailin: the strongest pre-Fani administrative record

IMD forecast a low-pressure formation on 3 October, formed the depression and started regular special bulletins on 8 October, forecast a very severe cyclone and likely Gopalpur landfall on 9 October, and increased expected landfall winds on 11 October. Phailin crossed near Gopalpur around 17:00 UTC on 12 October; IMD characterized its genesis, track, intensity and adverse weather as forecast four to five days ahead [10].

Odisha shifted about one million people during the final 36 hours. The memorandum records 983,642 cyclone evacuees and 171,083 flood evacuees. Its 4,197 free-kitchen or relief centres served 2,223,953 beneficiaries, but that beneficiary count is not a cyclone-shelter occupancy count [17]. Administratively recorded farm protection included moving 31,062 animals, deploying 283 veterinary teams, treating 89,840 livestock and vaccinating 230,400 cattle [17]. It does not establish which farmers received which crop advice.

Standing crops were damaged across about 6.71 lakh ha; 651,490 ha had more than 50% loss, and estimated crop loss was Rs 2,300 crore [17]. These totals are suitable for event-level validation. They are not enough to infer crop stage, message compliance, or how much loss warning alone avoided.

### Hudhud: district tables and fast civil recovery, but weak advisory timing

The state received its first IMD message on 6 October and circulated the 7 October depression forecast to 16 district collectors. Hudhud made landfall near Visakhapatnam around noon on 12 October and affected southern Odisha later that day [6]. Evacuation started on 11 October; 255,043 people were kept in 2,143 shelters across 11 districts [6].

The memorandum records 247,557 ha affected, 40,484.50 ha with more than 50% crop loss, and Rs 582.07 crore in estimated crop losses [6]. A government knowledge page contains post-Hudhud crop-wise contingency advice, but the recovered page does not establish its issue time, original agency, delivery channel, reach, or farmer compliance [25]. It is therefore useful as a recovery-policy input, not as observed pre-landfall advice.

Most roads to block level were cleared within two days and power restoration proceeded rapidly [6]. This supports a civil-infrastructure recovery clock, but not a field, market, pest, or next-sowing clock.

### Fani: the best end-to-end public-warning replay

The Odisha memorandum records no coastal warning on 26-27 April, heavy-rain guidance on 28 April, a cyclone watch at 13:00 on 30 April, and a yellow message at 06:30 on 1 May. Fani made landfall near Puri at about 08:30 on 3 May, with the eye crossing at 09:42. The watch therefore provided roughly 67 hours, although the forecast initially placed landfall farther south and later than observed [31].

Evacuation began on 1 May. The state moved 1,557,170 people from 19 districts to more than 9,000 safe shelters. It had 879 multipurpose shelters ready; a later relief count lists 9,180 camps accommodating 15.61 lakh people [31]. These fields should remain distinct: fixed multipurpose shelters, all safe shelters, and post-event relief camps are different denominators.

The warning stack included 1.8 crore SMS messages, activated sirens, hourly coastal voice messages, public-address systems, control rooms and media [31]. Crop and horticulture damage covered about 1.49 lakh ha; 143,373.90 ha had losses of 33% or more, producing a stated input-subsidy requirement of Rs 14,889.99 lakh [31]. The memorandum verifies an amount required, not payment to each farmer.

Roads were cleared within 72 hours, normal water supply returned in all 53 affected urban bodies from 9 May, and power was restored to 45.22 lakh of 46.27 lakh affected consumers [31]. No equivalently measured agricultural recovery trajectory or survey of early harvest, no action, livestock movement, or advisory receipt was found.

### Amphan: an Odisha impact record, not a complete IMD replay

Amphan made landfall in the Sundarbans rather than Odisha. A 21 May state briefing reported nearly 45 lakh people affected and about two lakh evacuees returning from approximately 3,000 shelters; Jagatsinghpur, Kendrapara, Bhadrak and Balasore were highlighted for restoration [15]. The recovered Odisha source set does not preserve each IMD bulletin, siren activation time, or evacuation-order timestamp.

The same briefing reports standing crops damaged over one lakh ha and extensive destruction of betel vines in Puri, Jagatsinghpur, Bhadrak and Balasore, but gives no crop-damage value [15]. Officials were ordered to assess agricultural crop damage within three days, house and building damage within one week, submit initial reports within two days, and detailed agriculture and horticulture reports afterward [15].

No event-specific KALIA payment, input-subsidy disbursement, PMFBY amount, farmer-action survey, crop recovery period, pest episode, market-disruption duration, or next-sowing date was verified.

### Yaas: the only event with a usable salinity-to-sowing branch

On 20 May, IMD told the state that a low-pressure area could form around 22 May, become a cyclone by 24 May, and reach the Odisha-West Bengal coast around 26 May. Yaas struck Odisha on 26 May, giving about six days from that first state-recorded outlook [18]. Odisha evacuated 7.02 lakh people to 8,410 shelters and provided dry food, water and free kitchens [18].

The memorandum records 5,672.99 ha affected and 2,197.34 ha with losses of 33% or more, with an input-subsidy requirement of Rs 26,336,034.50 [18]. Separately, one month later, field reporting found seawater effects over at least 5,882 ha in five Balasore blocks and around 1,400 ha in three Bhadrak blocks. Around 300 farmers were uncertain whether to sow kharif crops; OUAT and NRRI were collecting samples and evaluating salt-resistant crops [7].

The two area measures are not interchangeable: the memorandum's compensated crop-loss threshold and the later saline-inundation footprint measure different phenomena. The replay should represent both, but not merge them into one loss total.

### Dana: precise meteorology, dated rice advice, unresolved outcome totals

IMD's pre-cyclone watch was about 4.5 days before landfall, its alert about two days before, and its warning about 1.5 days before. Dana made landfall on 25 October near Bhitarkanika-Dhamara. Landfall-point errors were only 4, 2 and 2 km at 24, 48 and 72 hours; timing errors were 2.5, 0.5 and 0.5 hours [2]. This is the strongest source for testing hazard-timing accuracy.

Human-response totals conflict by source and time. The 25 October situation report says 584,888 people had been evacuated, later exceeding 600,000, with 6,008 shelters [16]. IMD's later report says eight lakh people were moved to 6,210 cyclone relief centres [2]. The replay dataset should retain both records with timestamps rather than silently choosing one.

The dated ICAR-NRRI advisory covered Ganjam, Puri, Jagatsinghpur, Jajpur, Kendrapara, Bhadrak, Balasore and Mayurbhanj. Rice farmers were told to keep drainage channels open, drain excess water and cover harvested rice with tarpaulin [28]. The recovered item contains no pulses, oilseeds, vegetables, livestock or fisheries instructions, and shows publication through ETV Bharat rather than an SMS/IVR delivery log [28].

The situation report says Odisha began a Joint Rapid Needs Assessment on 26 October with data collection through 29 October, but the reviewed official sources do not provide a final Odisha district crop-area/value table or payment ledger [16]. Dana is therefore hazard-ready and advisory-content-ready, but outcome-gated.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing fields | Coverage judgment |
|---|---|---|---|
| **IMD/RSMC cyclone reports** | 1999 warning synopsis; Phailin and Fani warning milestones; Dana lead-time and forecast-error verification | Do not contain farm-message receipt, individual action, plot loss, compensation or crop recovery | **A for hazard; D for human agriculture outcomes** |
| **Odisha SRC/OSDMA memoranda** | Phailin, Hudhud, Fani and Yaas evacuation, shelter, damage, relief and restoration tables | Different definitions across events; some landing pages hide files; Amphan and Dana lack equivalent final memoranda in the recovered set | **A-B** |
| **District or crop-loss administration** | >=33% and >50% thresholds; village assessment team; seven-day crop-cutting workflow; objections and e-transfer | No public row-level farmer ledger, payment date, or audit trail | **A for process; C for payout validation** |
| **IMD Agromet/Meghdoot** | Current state and district advisory portal establishes the service family | Historical event payloads, timestamps, language, phone delivery and acknowledgement were not found for five of seven events | **D for replay until archived** |
| **ICAR/NRRI and contingency advice** | Dana's dated rice actions; a post-Hudhud crop-advisory page | Dana item covers rice only; no delivery telemetry or compliance; Hudhud timing is unclear | **B** |
| **Multilateral/RDNA/DLNA and Red Cross** | Phailin rapid assessment, Fani DLNA/assessment, Dana rapid needs material | Usually post-event and sector-aggregate; rarely matched to advisory exposure | **B** |
| **Field journalism and farmer reports** | Amphan affected crops; Yaas salinity and sowing uncertainty | Small or undisclosed samples, preliminary figures, no counterfactual control group | **B-C** |
| **PMFBY/PIB aggregates** | Annual Odisha claims for 2018-19 through 2022-23 | No cyclone, district, crop, season, farmer or payment-latency attribution [32] | **C for fiscal context; D for event validation** |
| **Academic rice harvest research** | 35-days-after-heading comparator and 5.76% premature-harvest yield penalty [23] | Not Odisha-cyclone-specific; ecological zone and grain type alter effects [23] | **B for prior; C for local calibration** |
| **Tertiary web summaries** | Discovery of source names and common claims | Conflated states, unsupported acreage, copied numbers, missing dates and methods | **D** |

**Coverage judgment:** The source base is strongest for `forecast -> warning -> evacuation -> headline damage`. It becomes progressively weaker for `message delivered -> farmer understood -> action taken -> plot loss avoided -> compensation received -> recovery completed`.

## 4. WHAT IS MISSING

### Event and district gaps

| Event | Exact unresolved gap |
|---|---|
| **1999** | No recovered machine-readable district crop area/value; no full bulletin-by-bulletin archive; no siren activation log; no farmer-action, compensation or recovery series. The official memorandum exists, but the extracted record exposed only an annexure description [33]. |
| **Phailin** | Strong event totals, but no phone/message log, shelter-by-farmer linkage, crop stage, early-harvest/no-action survey, payment ledger or measured field recovery. The 4,197 centres are not a clean shelter-occupancy series. |
| **Hudhud** | District damage exists, but the crop-advisory publication and delivery time are unresolved; no recipient, comprehension or compliance sample; no agricultural recovery duration. |
| **Fani** | Strong public-warning and statewide crop totals, but no matched farm cohort, district-by-crop-stage loss panel, individual subsidy payment, coconut recovery curve, pest series or market-reopening series. |
| **Amphan** | No extracted Odisha IMD bulletin sequence; no warning lead calculation; no district crop hectares/value; no confirmed payout; no recovery, pest, market or sowing dates. |
| **Yaas** | No archived event-specific farmer message; no measured soil-electrical-conductivity time series; no date when each affected block became sowable; no payout ledger. The 5,672.99 ha administrative loss total and 7,282 ha reported saline footprint use different definitions [18][7]. |
| **Dana** | No authoritative final district crop area/value table in the reviewed set; conflicting evacuation snapshots; no farmer-action survey, final payout, salinity, market or next-sowing record. |

### Cross-event gaps

1. **No complete hourly human timeline.** Fani and Dana provide exact warning-stage times, but none of the seven events has a continuous hourly chain from IMD bulletin generation through state receipt, district forwarding, siren/SMS/IVR send, handset delivery, farmer acknowledgement and action.

2. **No historical SMS/IVR telemetry.** Message body, language, recipient count, send time, delivery status, retry, call completion, listen duration and acknowledgement are absent. Fani's 1.8 crore SMS total documents scale, not individual receipt [31].

3. **No event-level action denominator.** Apart from administrative livestock movement in Phailin, there is no defensible percentage for farmers who harvested early, drained fields, covered produce, moved livestock, sheltered, or took no action.

4. **No event-attributed insurance ledger.** PMFBY annual amounts cannot be assigned to Fani, Amphan or Yaas without claim-level peril and season fields [32]. No verified KALIA cyclone-specific payment table was found.

5. **No per-farmer compensation amount for these events.** Sources give eligibility rules, requirements, or deceased-person ex-gratia, but not a joined list of farm area, crop-loss percentage, sanctioned amount, payment date and failed transfer.

6. **No crop-stage exposure surface.** District crop area is not joined to sowing date, variety, phenological stage, expected harvest date or plot coordinates. This blocks a defensible early-harvest counterfactual.

7. **Recovery is measured mainly for infrastructure.** Hudhud roads, Fani roads/water/power and Yaas power have timestamps, but fields, soil salinity, pests, disease, market access and next sowing generally do not [6][31][18].

8. **Dedicated flood events are absent.** The requested list is cyclone-centered. Phailin's subsequent floods are counted, but a realistic Odisha flood replay also needs river-gauge, reservoir-release, inundation, breach and stand-alone monsoon flood events.

## 5. HOW IT FEEDS THE REPLAY SIMULATION

| Simulation layer | Historical inputs | Replay implementation | Validation test | Status |
|---|---|---|---|---|
| **Hazard field** | IMD track, intensity, warning stages, landfall time/location, wind and forecast errors | Version every bulletin as an event; interpolate only between stated track points; preserve forecast vintage | Predicted vs observed landfall time, point and intensity; Dana errors at 24/48/72 hours [2] | **GO** |
| **Public warning** | State receipt, watch/alert/warning stage, sirens, SMS, media, public-address use | Build a timestamped communication graph from IMD to state, district, village and channel | Match known milestones and total reach, such as Fani's 1.8 crore SMS [31] | **GO for milestones; GATED for delivery** |
| **Evacuation and shelter** | Evacuation totals, start dates, shelter or relief-centre counts | Model vulnerable population, order time, movement rate, capacity and occupancy as separate variables | Reproduce Phailin, Hudhud, Fani, Yaas and Dana totals within source uncertainty | **GO** |
| **Farm profile and crop stage** | Crop area, crop type where stated, season calendar, affected districts | Attach each synthetic plot to crop, variety, sowing date, stage, harvest readiness, livestock and storage | Compare aggregate exposed area with memorandum totals | **PARTIAL** |
| **Advisory generation** | Dana rice advice; Odisha contingency plan; post-Hudhud guidance | Generate crop/stage-specific actions with validity windows; label source as observed, policy-derived or synthetic | Exact-text comparison where an event advisory exists; policy-consistency otherwise | **PARTIAL** |
| **Farmer behavior** | Evacuation, shelter and Phailin livestock movement; almost no crop-action observations | Use explicit behavior scenarios rather than fitted compliance: no action, partial action and full action | Do not claim empirical calibration until action surveys exist | **GATED** |
| **Crop damage** | Affected ha, thresholded ha, crop-loss value and saline footprint | Use wind, inundation, duration, salinity and crop stage; aggregate synthetic plot losses to administrative units | Match Phailin, Hudhud, Fani and Yaas event totals and thresholds | **PARTIAL** |
| **Assessment and compensation** | >=33% eligibility, survey fields, seven-day crop cutting, objection period and e-transfer | Simulate inspection queue, eligibility, objections, sanction and payment latency | Validate process timing; later join actual beneficiary ledger [1] | **PARTIAL** |
| **Recovery** | Infrastructure restoration; Yaas saline area and sowing uncertainty | Model drainage, salt leaching, replanting, input delivery, market access and next sowing as separate clocks | Validate only fields for which measured follow-up dates exist | **GATED** |
| **Counterfactual savings** | Premature-harvest penalty of 5.76% relative to 35 days after heading | Compare `expected cyclone loss avoided` against `maturity yield penalty + harvest/quality/storage cost` | Report a range with sensitivity to stage and compliance, not a single saved-loss number [23] | **GATED pending local calibration** |

### Recommended event-replay schema

Every source observation should be immutable and carry: `event_id`, `source_id`, `issued_at`, `valid_from`, `valid_to`, `received_at`, `geography`, `hazard_vintage`, `message_text`, `language`, `channel`, `recipient_denominator`, `delivery_status`, `crop`, `stage`, `recommended_action`, `observed_action`, `damage_definition`, `area_ha`, `loss_value`, `assessment_date`, `payment_date`, `recovery_indicator`, `confidence`, and `source_reliability`.

The engine should score four distinct things. **Temporal fidelity** asks whether it acted using only information available at that replay time. **Action fidelity** asks whether advice was correct for crop stage and lead time. **Outcome fidelity** asks whether aggregate loss lies within the historical source range. **Causal value** asks whether action changed loss relative to a valid control. The first three can be partly implemented now; the fourth cannot.

## 6. REAL-vs-FILLER

| Classification | Evidence item | Permitted use |
|---|---|---|
| **REAL** | IMD issue times, forecast stages, landfall and forecast error | Hazard replay and temporal scoring |
| **REAL** | Official evacuation and shelter counts, with source date and definition | Human-response calibration |
| **REAL** | Crop hectares with stated threshold and damage value | Aggregate outcome validation |
| **REAL** | Fani SMS/siren/public-address totals | Channel-capacity scenario, not individual receipt |
| **REAL** | Dana's 23 October rice drainage and tarpaulin advice | Observed advisory-content test [28] |
| **REAL** | Odisha's seven-day village process, >=33% rule, objections and e-transfer | Assessment workflow simulation |
| **REAL** | Yaas's one-month saline footprint and sowing uncertainty | Recovery-state branch |
| **REAL, WITH LIMIT** | Rice 5.76% premature-harvest penalty | Prior or sensitivity bound, not Odisha-specific causal truth |
| **FILLER** | Generic claims that Odisha is "resilient" or warnings "saved crops" | Narrative only; no model calibration |
| **FILLER** | Today's EWDS coverage applied to 1999, Phailin or Hudhud | Prohibited back-cast |
| **FILLER** | Current Meghdoot functionality used as proof that a historical farmer got a message | Prohibited |
| **FILLER** | Statewide annual PMFBY totals assigned to a named cyclone | Prohibited [32] |
| **FILLER** | Preliminary media acreage treated as final district truth | Discovery only |
| **FILLER** | Shelter beneficiaries, free-kitchen beneficiaries and evacuees treated as the same count | Prohibited denominator conflation |
| **FILLER** | "Early harvest saved X%" derived by subtracting historical losses without a matched control | Prohibited causal claim |

The governing rule is simple: if a record lacks a source timestamp, geographic definition, denominator, and measurement definition, it may inform scenario design but cannot validate the engine.

## 7. NOISE LOG

| Searched and discarded | Why discarded |
|---|---|
| Wikipedia, Grokipedia, generic exam-preparation pages and unattributed cyclone roundups | Useful only for discovery; no primary tables or stable methodology |
| Farmonaut and promotional resilience articles | Unsupported or geographically conflated agricultural figures |
| Scribd mirrors | Unclear provenance and versioning when an official source exists |
| Current IMD Agromet state page | Shows today's service, not historical Fani, Amphan or Yaas payloads |
| Generic Odisha pest-surveillance pages | Not tied to a cyclone, post-event date or affected cohort |
| Fani NCAER Monsoon Mission economic-benefits report | Did not yield a Fani-specific farmer receipt/action counterfactual in the recovered text |
| 2025-2026 unseasonal-rain compensation stories | Search collisions, not cyclone-event payments |
| Annual PMFBY claims tables | Reliable fiscal totals but no cyclone attribution [32] |
| OSDMA landing pages without exposed document body | Good provenance but insufficient detail until the linked PDF is recovered |
| Dana rapid reports mixing Odisha and West Bengal crop impacts | State attribution is unsafe unless each table or sentence names Odisha |
| Yaas administrative loss area and journalistic saline footprint treated as duplicates | They measure different damage concepts and dates |
| Fani's 879 permanent shelters, more than 9,000 safe shelters and 9,180 relief camps collapsed into one field | Different facility definitions and reporting stages [31] |

## 8. VERDICT

# PARTIAL

### What can be built credibly now

1. A time-versioned **hazard replay** for all seven events, strongest for Phailin, Fani and Dana.
2. A **public-warning and evacuation replay** using official milestones and administrative totals.
3. An **aggregate crop-damage benchmark** for Phailin, Hudhud, Fani and Yaas.
4. A **policy advisory engine** tested against Dana's rice advice and Odisha's formal disaster procedures.
5. A **salinity-aware recovery branch** for Yaas, explicitly marked as incompletely calibrated.
6. A **process replay** for seven-day crop assessment, objections, eligibility and electronic payment.

### What remains gated

The project cannot yet claim that its simulated SMS/IVR advice reproduces what farmers actually heard, that farmers followed it, or that it would have saved a stated number of hectares or rupees. Those claims require five linked datasets that are currently absent:

- IMD/AAS, Agriculture Department, telecom, siren and IVR message logs with timestamps and delivery status.
- Event-stratified farmer surveys covering advice received, comprehension, early harvest, drainage, livestock movement, sheltering and no action.
- Plot or village crop-stage exposure joined to Crop Cutting Experiment losses.
- KALIA, SDRF/input-subsidy and PMFBY beneficiary/payment records with peril and event attribution.
- Follow-ups at approximately 7, 30 and 90 days for salinity, pests, replanting, market access and sowing.

**Decision:** Proceed with a transparent **Replay v1** whose dashboard labels every field `observed`, `derived`, `conflicting`, `missing`, or `synthetic`. Do not market it as a validated loss-savings simulator until farmer action and payment/recovery ledgers are acquired.

## Synthesis

| Era/event group | Warning mechanism | Human-response scope | Agricultural evidence | Recovery horizon | Central trade-off |
|---|---|---|---|---|---|
| **1999** | IMD bulletins, 35 CWDS, limited permanent shelters | Nearly 150,000 shifted; about 30,000 protected in 23 shelters | Fisher warning, but no usable farm-message/action record | Unmeasured in the recovered corpus | Warning existed, but last-mile capacity and observability were limited |
| **Phailin-Hudhud, 2013-2014** | Multi-day IMD-state coordination and collector instructions | Mass evacuation plus district shelter tables | Strong aggregate damage; Phailin livestock movement; weak crop-message evidence | Roads and utilities, not fields | Excellent life-safety record does not establish crop-loss causality |
| **Fani, 2019** | SMS, sirens, hourly voice messages, media and public address | 1.557M evacuated through a large mixed shelter network | Strong area and subsidy-requirement totals; no matched action survey | Roads, water and power measured | The richest communication record still lacks farmer-level behavior |
| **Amphan-Yaas, 2020-2021** | State warnings under multi-hazard and COVID constraints | Large evacuations; approximate Amphan records, stronger Yaas totals | Amphan crop categories; Yaas thresholded loss and saline footprint | Yaas gives one-month sowing uncertainty | Rapid evacuation and agricultural recovery require different data systems |
| **Dana, 2024** | Highly accurate forecast verification plus crop-specific institutional advice | Conflicting snapshots of 584,888 to 800,000 evacuees | Dated rice action, but no final official Odisha crop/payout table | Rapid assessment initiated; long recovery unmeasured | Better forecasts and advice do not automatically create outcome attribution |

The non-obvious result is that warning quality and agricultural outcome observability move at different speeds. Fani and Dana provide much better meteorology and public communication than 1999, yet neither supplies the matched `message -> action -> plot loss` record needed for causal savings. Evacuation systems optimize life safety; farm advisories must additionally resolve crop stage, labor, machinery, storage, livestock and market constraints.

Early harvest makes the tension explicit. It can remove a crop from wind or inundation exposure, but premature harvesting carries an observed yield penalty relative to 35 days after heading [23]. The advisory engine therefore needs an expected-loss decision rule, not a generic instruction to harvest. A realistic counterfactual is: advise early harvest only when predicted avoided cyclone loss exceeds maturity loss, quality loss, labor cost and storage risk, then report uncertainty across compliance scenarios.

The correct architecture is thus not one monolithic "AI accuracy" score. It is a chain of separately testable layers: forecast fidelity, message latency, delivery, comprehension, feasible action, damage, assessment, payout and recovery. Current evidence can validate the first, parts of the second, and event-level damage. The rest must remain visibly gated.

## References

1. *SRC || Special Relief Commissioner*. https://srcodisha.nic.in/guideline/3654.pdf
2. *Severe Cyclonic Storm “DANA” over the Bay of Bengal ( ... India Meteorological Department https://internal.imd.gov.in › press_release*. https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
3. *Cyclone Fani 2019 DLNA Report - Odisha State Disaster ...*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report/
4. *1999 Super Cyclone - Odisha State Disaster Management Authority*. https://www.osdma.org/publication/1999-super-cyclone/
5. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | CYCLONE AMPHAN UPDATE*. https://www.osdma.org/cyclone-amphan-update/
6. *CONTENTS for memorandum of Hudhud - srcodisha.nic.in*. https://srcodisha.nic.in/calamity/Memorandum%20Cyclone%20Hudhud%202014.pdf
7. *Cyclone Yaas aftermath: Odisha farmers in a fix over sowing ...*. https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568
8. *Cyclone Storm Yaas | Balasore*. https://balasore.odisha.gov.in/documents/natural-disaster-asiistance/cyclone-storm-yaas
9. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
10. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_38a1d4_phailin.pdf
11. * Cyclone Amphan Hits Agriculture Hard In Odisha*. https://odishatv.in/odisha-news/cyclone-amphan-hits-agriculture-hard-in-odisha-453057
12. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/survey/NCAER2020.pdf
13. *UNICEF India Flash Update No. 2 ( Cyclone Dana) - reporting period 28 Oct 2024 - India | ReliefWeb*. https://reliefweb.int/report/india/unicef-india-flash-update-no-2-cyclone-dana-reporting-period-28-oct-2024
14. * Amphan Cyclone Affected Nearly 45 Lakh People In Odisha: State Govt*. https://odishatv.in/odisha-news/amphan-cyclone-affected-nearly-45-lakh-people-in-odisha-state-govt-452756
15. *Cyclone Amphan hits 45 lakh in Odisha, Naveen Patnaik seeks house damage report in 7 days*. https://www.indiatoday.in/india/story/cyclone-amphan-hits-45-lakh-odisha-naveen-patnaik-seeks-house-damage-report-7-days-1680576-2020-05-21
16. *sphereindia.org.in*. https://www.sphereindia.org.in/sites/default/files/2025-04/SI%20Sitrep-2__Cyclone%20Dana%20OD-WB%20%28Post%29_25%20Oct%20%2724_1800%20Hrs.pdf
17. *Microsoft Word - FINAL MEMORANDUM.doc*. http://srcodisha.nic.in/calamity/MEMORANDUM.pdf
18. *1*. https://srcodisha.nic.in/calamity/Yass%20Cyclone%202021-%20Memorandum_compressed.pdf
19. *Odisha FANI cyclone Assessment Report*. https://ircsstoragedev.blob.core.windows.net/wordpresswebsite/2024/03/OdishaFaniAsessmentReport.pdf
20. *Orissa super cyclone – A Synopsis*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/449/450/1763
21. *agri.odisha.gov.in*. https://agri.odisha.gov.in/sites/default/files/2021-06/DMP.pdf
22. *Cyclone Dana Assessment Report*. https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf
23. *Effects of harvest time on rice yield and quality: A meta- ...*. https://www.sciencedirect.com/science/article/pii/S1161030125001704
24. *Harvesting - IRRI Rice Knowledge Bank*. http://www.knowledgebank.irri.org/training/fact-sheets/item/harvesting-fact-sheet
25. *Crop Advisory for Hudhud affected areas in Andhra Pradesh and Odisha | Vikaspedia - Agriculture*. https://agriculture.vikaspedia.in/viewcontent/agriculture/best-practices/sustainable-agriculture/crop-management/advisory-1-for-hudhud-affected-areas-in-andhra-pradesh-and-odisha?lgn=en
26. *Odisha's turnaround in disaster management has lessons for the world*. https://www.worldbank.org/en/news/opinion/2023/11/03/odisha-s-turnaround-in-disaster-management-has-lessons-for-the-world
27. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Early Warning Dissemination System (EWDS)*. https://www.osdma.org/preparedness/early-warning-communications/ewds
28. *Cyclone Dana: ICAR Issues Advisory For Standing Crops In Littoral Odisha*. https://www.etvbharat.com/en/%21bharat/cyclone-dana-icar-issues-advisory-for-standing-crops-in-littoral-odisha-enn24102306576
29. *Odisha Phailin Report Final*. http://ncrmp.gov.in/wp-content/uploads/2014/03/Odisha-Phailin-report-Final.pdf
30. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_7122ae_Preliminary%20Report%20on%20ESCS%20FANI_15082020.pdf
31. *Memorandum Cyclone Fani 3Rd May 2019*. https://srcodisha.nic.in/calamity/Memorandum_Cyclone%20FANI_3rd%20May%202019.pdf
32. *Annexure State-wise and year-wise details of claims paid to farmers during last 5 years i.e. 2018-19 to 2022-23 under PMFBY*. http://static.pib.gov.in/WriteReadData/specificdocs/documents/2023/dec/doc20231215288601.pdf
33. *SRC || Special Relief Commissioner*. https://www.srcodisha.nic.in/odia/data/MEMORANDUM-1999.pdf
