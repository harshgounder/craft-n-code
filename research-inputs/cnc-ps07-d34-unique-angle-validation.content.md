# Crop-Level Evacuation Decisions: Odisha's Defensible Advisory Frontier

## 1. EXECUTIVE SUMMARY

- **Qualified Go**: **GO**, but claim the novelty as a new combination, not as the first system to tell farmers to harvest or drain. BAMIS already tells farmers to harvest boro rice at **>=80% maturity**, cover harvested crops, clear drainage, raise bunds, brace banana, tie sugarcane, stop inputs, and net ponds before a cyclone [16][18]. -> Position CNC PS-07 as the first *verified in this sweep* to combine farm-specific action selection, quantified action-versus-wait tradeoffs, Odia IVR/SMS, and historical replay.

- **BAMIS Is The Closest Competitor**: The premise that BAMIS has "no thresholds" is too strong: its 2021 and 2024 bulletins contain an **80% rice-maturity trigger** [16][18]. What they do not show is a forecast-probability trigger, early-harvest penalty, expected loss avoided, farm-specific feasibility, recovery decision tree, or measured result [16][18]. -> Treat BAMIS as the baseline to beat, not as generic advice.

- **Odisha Already Has Agronomic Building Blocks**: Odisha's 2024 contingency plan says to use flood-tolerant rice, maintain buffer nurseries on high land, drain excess water, and transplant **40-65-day-old seedlings** after floodwater recedes; it also uses a **50% plant-population threshold** to choose resowing versus gap filling [28]. -> Convert these static plan rules into field-specific, hazard-timed decisions.

- **Operational Cyclone Advice Is Actionable But Narrow**: ICAR-NRRI's Cyclone Dana advice told Odisha rice farmers to open drainage for immature crops, protect harvested rice with tarpaulin, sun-dry grain for **1-2 days**, and use **7-10 days** of sealed fumigation when infestation occurs [26]. -> Preserve this expert content, but add crop stage, forecast lead time, expected benefit, labor and storage constraints, and evidence provenance.

- **Low-Literacy Interaction Is Not Unique By Itself**: Ama Krushi is a two-way Odisha advisory service using IVR and a live call center; it passed **3.2M farmers** at transition and **5M by June 2023** [4]. BaKhabar Kissan offers profile- and language-adaptive IVR, SMS/VMS, pull queries, and expert escalation [24]. -> Differentiate on what the dialogue computes, not merely on voice delivery.

- **Korea Solves Hyperlocal Risk, Not The Full Decision**: Korea's RDA AgMet service calculates field-level risk, includes crop growth stage, supports **44 crops**, forecasts weather up to **9 days**, and sends SMS/email alerts [29]. Its public evidence does not expose crop-by-stage physical-action thresholds or measured farm-loss reduction [29]. -> Use it as the benchmark for spatial and phenological targeting, then add action economics.

- **Crop Physics Proves Stage Matters**: A controlled rice study found no significant yield decrease below **4 days** of tillering-stage inundation, an **80% yield reduction at 6 days**, and over **50% yield loss after only 2 days** of flooding at booting or flowering [12]. -> Never issue one generic "drain the rice field" rule; stage, expected inundation duration, variety, and drainage capacity must alter priority.

- **The Key Quantitative Evidence Is Still Missing**: Rice studies identify optimum harvesting near **45-55 days after heading** and report delayed-harvest losses of roughly **5-11.41%** in tested settings; another cited experiment found a **9.8-24.4%** decrease after a 10-day delay [10][5]. They do not supply a portable Odisha curve for the penalty of harvesting several days *early*. -> The demo must label early-harvest tradeoffs as locally calibrated estimates, not universal facts.

- **Recovery Knowledge Is Deep But Not Message-Ready**: FAO covers early harvesting, waterproof seed storage, canal clearing, livestock evacuation, cash and asset protection; Alabama Extension supplies post-flood crop-disposition rules including example buffer, sediment-depth, and replanting-wait thresholds [21][13]. USDA's severe-storm page is dominated by insurance, records, reporting deadlines, and recovery programs [9]. -> Build a compact Odisha recovery state machine rather than sending farmers links to long manuals.

## 2. INVENTORY / EVIDENCE TABLE

**Grade meaning:** **A** = operational, crop-decision-specific, quantitatively validated; **B** = operational or official and actionable, but missing quantified outcomes or one major layer; **C** = useful component, research result, or broad guidance rather than an end-to-end service; **D** = unverified, marketing-only, or irrelevant to the decision slot. No reviewed system earns A for the complete proposed bundle.

| What | Named source, URL and date | Mechanism | Feasibility for Odisha | Grade |
|---|---|---|---|---|
| Crop-level cyclone protection | **BAMIS Special Agromet Advisory**, <https://www.bamis.gov.bd/res/public/pages/2021/05/23/23981.pdf>, 22 May 2021 | About four days before expected coastal impact, uses >=80% rice maturity to trigger harvest; also covers crop heaps, drains, bunds, banana, sugarcane, vegetables, fish and livestock [16] | High. Actions are familiar, low-cost and suitable for rule encoding. Missing expected-loss calculations and outcome validation. | **B** |
| Updated cyclone rule set | **BAMIS Cyclone Remal Advisory**, <https://www.bamis.gov.bd/res/public/pages/2024/05/25/27784.pdf>, issued 23 May and updated 25 May 2024 | Repeats the 80% boro trigger, immediate mature-produce harvest, no irrigation/fertilizer/pesticide, higher bunds, clear drains and physical supports [18] | High as a content baseline; medium as a decision engine because it does not use individual farm constraints. | **B** |
| Odisha flood contingency | **Government of Odisha Crop Contingency Plan 2024**, <http://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf>, 2024 | Uses crop condition and calendar thresholds: >50% mortality triggers resowing; <50% triggers gap filling; flood response includes tolerant varieties, highland buffer nurseries, drainage and older seedlings [28] | Very high. This should be the approved rule-library backbone, though it is a plan rather than a live optimizer. | **B** |
| Odisha cyclone operations | **ICAR-NRRI Cyclone Dana advisory**, <https://www.etvbharat.com/en/!bharat/cyclone-dana-icar-issues-advisory-for-standing-crops-in-littoral-odisha-enn24102306576>, 23 October 2024 | Distinguishes immature standing rice, harvested rice, wet grain, stored grain and late crops; maps each state to drainage, stacking, drying, fumigation or pest surveillance [26] | High for rice. Needs first-party digital publication, other crops, economic tradeoffs and direct IVR delivery. | **B** |
| Two-way low-literacy delivery | **Ama Krushi Transition Insights**, <https://precisiondev.org/wp-content/uploads/2025/02/AK-transition-report-BMGF_condensed.pdf>, report dated July 2023 | Customized, two-way advice through IVR, live call center, radio and hybrid delivery; expanded to 28 value chains [4] | Very high. Existing Odisha channel and governance model can host the proposed decision service. | **B** |
| Profile-based voice and expert escalation | **BaKhabar Kissan**, <http://abl.com/business-banking/agriculture-financing/bakhabar-kissan>, undated page | Regional-language IVR adapts to caller profile; SMS/VMS supports disaster alerts and pull queries; unresolved questions escalate to experts [24] | Technically high, but localization, evidence governance and Odisha integration remain unproven. | **C** |
| Conversational farmer interface | **Farmer.Chat paper**, <https://arxiv.org/abs/2409.08916>, submitted 13 September 2024, revised 8 October 2024 | Generative AI supplies personalized contextual advice; abstract reports deployment in four countries, 15,000+ farmers and 300,000+ queries [3] | Useful for dialogue design. Do not let the language model invent agronomy or action thresholds. | **C** |
| Field-level hazard and phenology | **Korea RDA Agricultural Weather Disaster Early Warning System**, <https://agmet.kr/>, current count stated for January 2026 | Field-level risk, crop stage, 44 crops, up to 9-day forecasts, SMS/email, daily farm-weather and hazard information [29] | Strong architecture analogue. Public evidence does not show detailed crop-evacuation rules or realized loss reduction. | **B** |
| Odisha multi-hazard transport | **OSDMA EWDS and Satark**, <https://www.osdma.org/preparedness/early-warning-communications/ewds> and <http://satark.rimes.int/>, operational pages | OSDMA can disseminate area-specific warnings through messages, voice and sirens; Satark covers cyclone, flood, drought, heat and other hazards [30][31] | High as warning infrastructure; low as evidence of crop-level decisions. | **C** |
| Forecast-triggered farm asset protection | **FAO Integrated Flood Management**, <https://openknowledge.fao.org/server/api/core/bitstreams/cfa77221-2b43-4616-983a-f2b4bdacd7d6/content>, date not established in extract | Links forecast thresholds and pre-arranged finance to early harvest, canal clearing, livestock routes, waterproof storage, feed and asset protection [21] | High for system logic and action taxonomy. Too broad for direct farmer SMS without localization. | **B** |
| US severe-storm recovery | **USDA Farmers.gov Severe Storm Resources**, <https://www.farmers.gov/protection-recovery/severe-storms>, undated page | Insurance, loss reporting, documentation, assistance programs and deadlines, including 72-hour and 15-day notices in specified cases [9] | Low-to-medium for Odisha agronomy; useful for designing administrative recovery workflows. | **C** |
| Post-flood food-safety decisions | **Alabama Cooperative Extension, Food Crop Producers After Flooding**, <https://www.aces.edu/blog/topics/crop-production/food-safety-for-southern-u-s-food-crop-producers-after-flooding/>, undated page | Early diversion to alternative markets; contaminated-crop disposal; example 30-foot buffer; <4-inch and 4-8-inch sediment branches; generally 30-60 days before replanting [13] | Mechanistically useful, but US regulation and pathogens cannot be transplanted unchanged to Odisha. | **C** |
| Recovery package implementation | **FAO Nepal Flood Recovery Project**, <https://openknowledge.fao.org/server/api/core/bitstreams/7c5e5242-29a7-4f42-b142-608c9e4250c9/content>, March 2023 | Seeds, production training, seed multiplication/storage and irrigation rehabilitation; reached 3,309 households and about 1,000 ha [17] | Good model for the recovery layer, but it is program delivery, not an immediate personalized advisory. | **C** |
| Rice inundation response surface | **Effects of Flooding Duration at Rice Growth Stages**, <https://www.aeeisp.com/nygcxb/en/article/doi/10.11975/j.issn.1002-6819.2019.03.016>, 2019 | Experimental stage x duration response: tillering tolerated short flooding better, while booting and flowering suffered >50% yield reduction after two days [12] | High scientific value, but local variety, salinity, temperature and field-flow calibration are required. | **B** |
| Harvest-window economics input | **Rice harvest-date studies**, <https://www.mdpi.com/2073-4395/14/7/1346>, 2024, and <https://www.sciencedirect.com/science/article/pii/S1161030121001532>, 2021 | Defines tested optimal windows and delayed-harvest losses; establishes that both advanced and delayed harvest can reduce output [10][5] | Suitable as a model structure and prior, not as an Odisha early-harvest lookup table. | **C** |

**Table takeaway:** Physical crop actions are not novel. The unoccupied space is the decision layer joining BAMIS-like actions, Odisha-approved contingency rules, Korea-like field risk, Ama Krushi-like voice access, and locally calibrated loss functions.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---|---|---|
| BAMIS and South Asian agromet bulletins | Direct commands for harvest, drainage, bunds, storage, banana, sugarcane, fish and input avoidance; one rice-stage threshold [16][18] | No farm profile, forecast probability, labor constraint, counterfactual loss, outcome measurement or recovery branch | **Best action-language coverage; incomplete decision science** |
| Odisha government, ICAR, OUAT and KVK family | Government contingency plan has stage and condition branches; NRRI Dana advice has concrete pre/post-rain rice actions [28][26] | Direct text from the official Fani page and primary OUAT/KVK cyclone bulletins was not recoverable; do not claim coverage that was not inspected | **Strong Odisha rule base; fragmented publication and delivery evidence** |
| Ama Krushi, BKK and Farmer.Chat | Two-way voice/call center, profile adaptation, pull questions, expert escalation and conversational personalization [4][24][3] | No demonstrated cyclone decision optimizer or quantified action-versus-wait tradeoff | **Accessibility solved in components; agronomic decision gap remains** |
| Korea RDA AgMet, including Jeonnam service areas | Field-level weather risk, growth stage, multiple crops, 9-day horizon and SMS/email [27][29] | Public material gives broad response guidance but not inspectable crop x stage x lead-time action thresholds or field outcomes | **Strongest hyperlocal hazard analogue, not a verified evacuation optimizer** |
| FAO and WFP-style anticipatory action | Trigger-based early action, early harvest, seed protection, canals, livestock, cash and pre-arranged finance [21] | Usually program or community scale rather than an individual crop decision in a short message | **Excellent action and trigger framework; weak last-mile personalization** |
| USDA and extension recovery | Insurance and documentation workflows plus detailed food-safety and replanting rules [9][13] | Jurisdiction-specific regulation, long-form web/PDF delivery, little Odisha crop-stage targeting | **Deep recovery reference, far from Odia IVR/SMS** |
| Crop-physics literature | Strong evidence that stage, flood duration, variety and treatment matter [12] | Mostly controlled or non-Odisha studies; few action-cost or implementation-feasibility measurements | **Good model priors; not deployable thresholds without calibration** |
| Harvest economics | Tested optimum windows and delayed-harvest losses [10][5] | No robust local curve for yield, quality, drying and price penalties from harvesting several days early | **The most important unresolved quantitative gap** |
| Commercial weather and satellite platforms | Weather, imagery and farm monitoring are widely marketed; BKK reports 300+ stations and 15.8M+ users [25] | Self-reported scale is not evidence of a crop-evacuation decision or avoided loss | **Infrastructure signal, not uniqueness-destroying evidence** |

**Coverage judgment:** The search found systems covering every *component*, but no verified source covering the complete chain: spoken farmer problem -> farm state -> crop/stage/hazard probability -> feasible physical action -> quantified tradeoff -> Odia IVR/SMS -> replayed outcome.

## 4. WHAT IS MISSING: THE EXACT RESEARCH GAP

The gap is not "weather alerts for farmers," "AI advice," "voice access," or even "harvest before a cyclone." All already exist in some form. The gap is a **counterfactual, constraint-aware crop-action policy**:

> For this farm, crop, variety, stage, expected hazard, lead time, labor, drainage, storage and market access, which feasible action minimizes expected loss, how much better is it than waiting, and how uncertain is that estimate?

BAMIS exposes the distinction. Its >=80% rule is real stage logic, so it would be inaccurate to say BAMIS has no thresholds [16][18]. But it does not show why 80% is optimal for a particular variety, whether a 70% mature crop should be harvested under a high-impact forecast, the likely yield and quality sacrificed, or whether the farmer has labor and dry storage. Its bulletin moves directly from forecast to universal action [16].

Five evidence gaps must therefore be closed:

1. **Local action-response curves.** Estimate yield, quality and price under harvest-now versus wait; loss under different flood depths and durations by stage; and effectiveness of drainage, bunding, banana support, nursery relocation, seed elevation and fodder cutting. The rice flood experiment proves that stage changes the loss function dramatically, but its two varieties and pot conditions are not Odisha deployment values [12].

2. **Early-harvest economics.** Existing studies quantify tested harvest windows and delayed losses, but the reviewed evidence does not provide an Odisha curve for harvesting 1, 3, 5 or 7 days before physiological maturity [10][5]. The model also needs labor, machine availability, drying, milling recovery, distress-sale price and storage spoilage.

3. **Lead-time feasibility.** "Brace banana" is useless if poles and labor cannot be obtained before landfall. Every action needs duration, crew, equipment, cost, safe working cutoff and dependency fields.

4. **Post-event state transitions.** Advice must branch on observed inundation duration, salinity, lodging, contamination, grain moisture, pest signs and surviving plant population. Odisha's >50% resow rule and 40-65-day seedling option are good examples of state-dependent recovery [28].

5. **Low-literacy problem capture.** Voice access exists, but a safe dialogue must turn an Odia utterance into confirmed slots: crop, acreage, stage, visible water, harvested status, storage, labor and farmer intent. The system should repeat uncertain fields and route unresolved cases to a human, following Ama Krushi's and BKK's call-center pattern [4][24].

This makes the defensible research claim narrower and stronger: **not a new list of precautions, but an empirically calibrated policy for choosing among them.**

## 5. HOW IT FEEDS THE ADVISORY ENGINE

### Decision architecture

| Engine component | Inputs | Algorithm or rule | Farmer-facing output |
|---|---|---|---|
| Farmer-state capture | Odia speech/DTMF, registered crop profile, plot location, variety, sowing date, acreage, storage, labor and equipment | Speech-to-slot extraction with read-back confirmation; call-center fallback for low confidence | "You said: 0.8 acre rice, near maturity, no dry store. Press 1 to confirm." |
| Hazard state | IMD track, rainfall, wind, river/flood forecast, soil moisture and plot elevation | Calibrated probability by hazard severity and arrival window; retain uncertainty rather than converting immediately to yes/no | Hazard, expected arrival and confidence stated in plain Odia |
| Phenology | Sowing/transplanting date, variety duration, remote sensing and farmer correction | Growing-degree-day or approved crop-calendar estimate, then farmer confirmation | Stage such as tillering, flowering, grain filling or >=80% mature |
| Action eligibility | Crop, stage, lead time, labor, tools, storage and safe-work limits | Hard constraints remove impossible or unsafe actions; expert rules provide conservative defaults | Only feasible choices are offered |
| Expected-loss optimizer | Hazard probability, stage-specific loss functions, action effectiveness, early-action penalty, price and action cost | For each action `a`, minimize `C_action + P(hazard)*Loss_after_action + (1-P(hazard))*False_alarm_loss`; show a range when evidence is weak | Ranked action, expected loss avoided, cost, uncertainty and alternative |
| Recovery state machine | Flood duration/depth, salinity, lodging, contamination, moisture, pests and surviving population | Branch to drain, dry, segregate, test, gap-fill, resow, replant or seek expert help; use Odisha-approved thresholds | One immediate action plus next observation time |
| Message generator | Structured decision object and evidence identifier | Deterministic template first; language model only translates/simplifies, never invents agronomy | Short SMS plus IVR explanation and repeat option |
| Safety and provenance | Rule version, source, confidence, contraindications | Human-approved rule registry; suppress unsupported numbers; escalate conflicts | "Estimate uncertain - connect to agriculture expert" |

The harvest policy should compare at least two counterfactuals. The **harvest-now cost** includes immature grain, quality/milling penalty, harvest labor, drying, storage and price. The **wait cost** includes forecast-weighted lodging, shattering, submergence, contamination and access loss. BAMIS's 80% maturity rule can seed the first rule, but the optimizer should be allowed to recommend "wait," "harvest the high-risk plot first," or "harvest only the mature area" when economics and feasibility differ [16].

### Rules that can be encoded now

- **Rice before cyclone:** If maturity is >=80% and safe harvest, labor and dry protection are available, raise harvest priority; otherwise protect harvested heaps, clear drainage and raise bunds. This is directly traceable to BAMIS [16].
- **Immature Odisha rice:** Open drainage before heavy rain; after rain, dry harvested grain for 1-2 days before bagging. Add moisture measurement when sensors or a meter are available [26].
- **Flood recovery:** If rice stand mortality is >50%, resow with a 10-15-day earlier variety; if it is <50%, gap-fill and redistribute hills [28].
- **Buffer nursery:** Maintain nursery material on high land and use 40-65-day-old seedlings after water recedes, subject to variety and season [28].
- **Reproductive-stage rice:** Escalate drainage priority when forecast inundation overlaps booting or flowering because short submergence caused much larger experimental yield effects than short tillering-stage submergence [12]. This must initially be an evidence-tiered warning, not a universal loss percentage.
- **Post-flood produce:** Separate potentially contaminated produce and prevent mixing with unaffected lots. Jurisdiction-specific disposal and replanting rules require Odisha food-safety approval before deployment [13].

### Replay and field validation

Replay each historical cyclone or flood at fixed decision times such as 120, 72, 48 and 24 hours before impact. Freeze the forecast and farm information available at that time, generate advice, and compare it with observed inundation, crop stage, remote-sensing damage, crop-cutting results and farmer reports. Odisha's existing assessment process already combines field verification, eye estimation, crop cutting and remote-sensing inundation cross-checks [32].

Report **decision regret per hectare**, avoided-loss estimate, false-action cost, calibration of hazard probability, action completion, IVR comprehension, and subgroup performance by crop, gender, literacy and phone type. Then run a prospective pilot comparing standard alerts against the decision service. Until replay and field trials agree, publish ranges and evidence grades rather than a single precise rupee-saving claim.

## 6. REAL-vs-FILLER

| Classification | What is real | What must not be overstated |
|---|---|---|
| **Verified operational** | BAMIS publishes concrete cyclone actions and an 80% maturity trigger [16][18]. Ama Krushi operates two-way IVR/call-center delivery at multi-million-user scale [4]. Korea RDA supplies field-level crop-stage risk and alerts [29]. | None proves the complete quantified crop-evacuation engine or reports avoided loss per farm. |
| **Verified official content** | Odisha's 2024 plan provides crop-condition thresholds, highland buffer nursery, drainage and post-flood transplant options [28]. NRRI's Dana advice gives direct rice protection and recovery steps [26]. | A government plan or news-carried expert advisory is not proof of personalized automated delivery or farmer compliance. |
| **Useful but program-level** | FAO anticipatory action links forecast triggers to early harvest, waterproof seed storage, canal work, feed and livestock protection [21]. FAO recovery projects distribute inputs and rebuild irrigation [17]. | These are not per-crop, per-stage SMS decisions, and project reach is not causal proof of crop loss avoided. |
| **Research-grade, not deployment-grade** | Rice flooding and harvest-date studies provide response shapes and candidate priors [12][10]. | Their varieties, climates and experimental conditions cannot be pasted into Odisha as universal thresholds. |
| **Marketing or self-reported** | BKK reports 300+ stations and 15.8M+ users; Korea lists technology-completeness percentages [25][29]. | User count, stations or "95% technology completion" do not demonstrate correct recommendations or crop-loss reduction. |
| **Filler** | "AI + IoT + satellite + blockchain," a chatbot demo, a weather dashboard, or generic "take precautions" text | These add no uniqueness unless they change a verified farm decision and expose evidence, uncertainty, feasibility and result. |

The real product should therefore keep the agronomic policy deterministic and auditable. Generative AI may capture and explain a farmer's problem, but it should not author the underlying harvest, drainage, chemical or fumigation decision.

## 7. NOISE LOG

| Excluded or down-weighted material | Why it is noise for this question |
|---|---|
| Financial "yield curve" search results | Keyword collision with crop yield curves; wholly unrelated to agricultural harvest response. |
| Generic severe-weather and insurance pages | Useful for preparedness administration, but USDA's reviewed page mainly covers insurance, records, reporting and assistance deadlines rather than physical crop choices [9]. |
| Crop-damage and compensation thresholds | Odisha's **33% crop-loss** enumeration threshold identifies affected farmers and subsidy eligibility; it is not a threshold for whether to harvest, drain or brace [32]. |
| Satellite damage-estimation papers | They measure what happened after a cyclone but do not necessarily choose a feasible pre-event action. They are more useful as replay ground truth than as the advisory policy. |
| Official Fani landing-page wrapper | The page title was found, but the action attachment could not be extracted. It is not used as evidence for specific Fani instructions. |
| Unverified "Jeonnam AI" summaries | The primary system that could be verified is Korea RDA's field-level AgMet service, including Jeonnam service areas [27][29]. Claims beyond its visible crop-stage, hazard and alert functions were excluded. |
| Banana-propping posters and extension slogans | They support the mechanism that props reduce toppling, but the reviewed material supplied no action-versus-inaction effect size. Thus no percentage benefit should appear in the engine yet. |
| BKK and chatbot scale claims | Scale supports feasibility, not decision efficacy. Farmer.Chat's abstract reports engagement and improved practices but exposes no cyclone crop/stage thresholds [3]. |
| Non-Odisha laboratory percentages | The stage-duration rice experiment is retained as scientific evidence, but its numeric losses are not presented as Odisha forecasts without local calibration [12]. |

## 8. VERDICT: GO - WITH A COMPARATIVE SYNTHESIS AND EVIDENCE GATES

### Comparative synthesis

| System or evidence family | Core mechanism | Scope and time horizon | Tradeoff evidence | Main strength | Main limitation |
|---|---|---|---|---|---|
| **BAMIS** | Hazard bulletin -> physical action list | District/crop bulletin, several days before cyclone | One maturity trigger, no expected-loss comparison | Closest crop-evacuation language | Not individualized or outcome-validated |
| **Odisha plan and NRRI** | Official contingency branches and event advice | Seasonal planning plus immediate cyclone response | Several agronomic thresholds, little economics | Locally legitimate content | Fragmented and mostly static |
| **Korea RDA AgMet** | Field-level weather, risk and phenology | Daily alerts, up to 9 days | Public thresholds/outcomes not exposed | Best hyperlocal risk architecture | Physical decisions remain broad [29] |
| **Ama Krushi, BKK, Farmer.Chat** | Voice, call center, profile and conversational capture | On-demand and recurring advisory | No verified disaster-action optimizer | Best accessibility and engagement layer | Advice quality and thresholds are the bottleneck |
| **FAO, WFP-style AA, USDA and extension** | Triggered asset protection and recovery workflows | Before impact through long recovery | Some operational and safety thresholds | Widest action and recovery coverage | Long-form, program-scale, jurisdiction dependent |
| **Crop and harvest science** | Experimental response surfaces | Stage-duration and harvest-window studies | Quantitative but externally limited | Supplies causal model structure | Not locally calibrated or end-to-end |

The non-obvious result is that the competitors are complementary rather than interchangeable. BAMIS knows *what physical precautions sound like*. Korea knows *where and when risk occurs*. Ama Krushi and BKK know *how to reach and hear low-literacy farmers*. FAO knows *how triggers mobilize assets and recovery*. Crop science knows *why stage changes loss*. The proposed system is defensible only if it integrates those strengths without pretending any one source already supplies a universal loss table.

### Decision

**GO**, with three claim gates:

1. **Permitted novelty claim:** "A farm-specific Odisha advisory that ranks pre-disaster crop actions using crop stage, lead time, feasibility and quantified tradeoffs, delivers the decision in Odia by IVR/SMS, and validates it through historical replay."
2. **Prohibited claim:** "The world's first system to tell farmers to harvest, drain or brace crops." BAMIS falsifies that broad claim [16].
3. **Evidence gate before deployment:** Every number must be tagged as Odisha field data, peer-reviewed external prior, expert rule or unvalidated estimate. High-risk chemical, food-safety and fumigation advice requires approved wording and human review.

### What judges will ask, and the answer

| Judge question | Defensible answer |
|---|---|
| **"BAMIS already says harvest and drain. What is new?"** | Correct. BAMIS is our baseline. We add field-specific crop stage, forecast probability, labor/storage feasibility, action-versus-wait loss, Odia two-way voice, recovery branching and replay. |
| **"Where does the early-harvest penalty come from?"** | The literature supplies model shape and delayed-harvest evidence, not a portable Odisha early-penalty curve [10][5]. We begin with conservative ranges, then calibrate by Odisha variety, stage, moisture, milling recovery, price and storm outcome. |
| **"What if IMD's forecast is wrong?"** | Optimize expected loss rather than issuing every precaution. Prefer low-regret actions at lower probabilities; reserve irreversible harvest for cases where forecast-weighted avoided loss exceeds early-harvest and execution costs. Show uncertainty and an alternative. |
| **"How do you prevent AI hallucination?"** | The model produces a structured decision from an approved rule and response-curve registry. AI only captures Odia speech and explains the result. Unsupported numbers are blocked; low confidence routes to an expert. |
| **"How is this for illiterate users rather than an app demo?"** | Use outbound IVR or missed-call access, spoken slot confirmation, keypad choices, replay of the action, and call-center escalation. Ama Krushi demonstrates that Odisha can operate IVR and live support at scale [4]. |
| **"Can a farmer actually complete the action before landfall?"** | The action library contains labor-hours, equipment, safe cutoff, storage and market dependencies. Infeasible actions are removed; plots and actions are ranked by avoidable loss per hour. |
| **"How will you prove it reduces loss?"** | First replay past events using only contemporaneous forecasts; then compare standard alerts with decision advice in a prospective pilot. Report regret, false-action cost, compliance, comprehension and realized loss, not only messages sent. |
| **"What is the minimum credible demo?"** | One district; rice plus banana or vegetables; 3 lead times; five physical actions; Odia IVR capture; a visible evidence card; counterfactual loss ranges; and replay of at least one documented cyclone. Do depth before adding more crops. |

**Bottom line:** The slot is defensible, but the uniqueness lives in the **quantified choice among actions**, not in the action vocabulary, weather alert, chatbot or IVR individually. Build the smallest scientifically honest optimizer that can say "harvest," "wait," "drain," "brace," or "move/protect" - and show why, at what confidence, under which farm constraints, and how replay says it would have performed.

## References

1. *Weathering the storm: What makes anticipating cyclones a ...*. https://www.wfp.org/publications/weathering-storm-what-makes-anticipating-cyclones-success
2. *Crop Advisory for likelihood of Severe Cyclone Storm "FANI*. https://agri.odisha.gov.in/en/agriculturedepartmenthometab/crop-advisory-likelihood-severe-cyclone-storm-fani-0
3. *Farmer.Chat: Scaling AI-Powered Agricultural Services for ...*. https://arxiv.org/abs/2409.08916
4. *Ama Krushi Transition Insights Report*. https://precisiondev.org/wp-content/uploads/2025/02/AK-transition-report-BMGF_condensed.pdf
5. *The effect of harvest date on yield loss of long and short-grain rice cultivars (Oryza sativa L.) in Northeast China - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S1161030121001532
6. *Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en/home
7. *Responses of rice to saline water flooding: interaction between salinity and hypoxia specific effects | Plant Physiology Reports | Springer Nature Link*. https://link.springer.com/article/10.1007/s40502-026-00943-x
8. *Ama Krushi – Scaling advisory services to millions of farmers ...*. https://precisiondev.org/project/ama-krushi
9. *Severe Storm Preparation and Recovery Resources | Farmers.gov*. https://www.farmers.gov/protection-recovery/severe-storms
10. *Expounding the Effect of Harvest Management on Rice (Oryza sativa L.) Yield and Latent Loss Based on the Accurate Measurement of Grain Data*. https://www.mdpi.com/2073-4395/14/7/1346
11. *Frontiers | Flood-tolerant rice for enhanced production and livelihood of smallholder farmers of Africa*. https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2023.1244460/full
12. *Effects of flooding duration in different growth stages on growth and yield component of rice *. https://www.aeeisp.com/nygcxb/en/article/doi/10.11975/j.issn.1002-6819.2019.03.016
13. *Food Safety for Southern U.S. Food Crop Producers After Flooding - Alabama Cooperative Extension System*. https://www.aces.edu/blog/topics/crop-production/food-safety-for-southern-u-s-food-crop-producers-after-flooding/
14. *FAO Knowledge Repository*. https://openknowledge.fao.org/bitstreams/093c62f3-9089-4a03-8bf6-aed1a2d41c06/download
15. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
16. *Special Agromet Advisories due to probable Cyclone*. https://www.bamis.gov.bd/res/public/pages/2021/05/23/23981.pdf
17. *Emergency and Early Recovery Support to Floods-Affected Farming Households in Western Terai, Nepal - TCP/NEP/3809*. https://openknowledge.fao.org/server/api/core/bitstreams/7c5e5242-29a7-4f42-b142-608c9e4250c9/content
18. *Special Agromet Advisory for Cyclone 'Remal' and Possible Heavy Rainfall (Updated)*. https://www.bamis.gov.bd/res/public/pages/2024/05/25/27784.pdf
19. *FAO Pakistan Update on Agriculture No 2*. https://www.fao.org/fileadmin/templates/tc/tce/pdf/Pakistan_Update_Agriculture_2.pdf
20. *fao.org*. https://www.fao.org/4/i2096e/i2096e.pdf
21. *Integrated flood management for resilient agrifood systems and rural development*. https://openknowledge.fao.org/server/api/core/bitstreams/cfa77221-2b43-4616-983a-f2b4bdacd7d6/content
22. *openknowledge.fao.org*. https://openknowledge.fao.org/server/api/core/bitstreams/beab3678-745c-4a28-98b4-79771a27f5bd/content
23. *Cash before the storm: WFP’s early action empowers ...*. https://www.wfp.org/stories/cash-storm-wfps-early-action-empowers-bangladeshis
24. *BaKhabar Kissan – Agriculture Advisory by Allied Bank*. http://abl.com/business-banking/agriculture-financing/bakhabar-kissan
25. *BaKhabar Kissan | Pakistan's Largest AgriTech & Digital Agriculture Platform*. http://bkk.ag/
26. *Cyclone Dana: ICAR Issues Advisory For Standing Crops In Littoral Odisha*. https://www.etvbharat.com/en/%21bharat/cyclone-dana-icar-issues-advisory-for-standing-crops-in-littoral-odisha-enn24102306576
27. *mobile.agmet.kr*. https://mobile.agmet.kr/mobile/login/
28. *CROP CONTINGENCY PLAN 2024 FINAL.pdf*. http://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf
29. *농촌진흥청 국립농업과학원 :: 농업기상재해 조기경보시스템*. https://agmet.kr/
30. *http://osdma.org/preparedness/early-warning-communications/ewds*. http://osdma.org/preparedness/early-warning-communications/ewds
31. *http://newindianexpress.com/odisha/2019/Mar/15/satark-app-to-alert-people-on-natural-disasters-1951882.html*. http://newindianexpress.com/odisha/2019/Mar/15/satark-app-to-alert-people-on-natural-disasters-1951882.html
32. *http://srcodisha.nic.in/guideline/3654.pdf*. http://srcodisha.nic.in/guideline/3654.pdf
