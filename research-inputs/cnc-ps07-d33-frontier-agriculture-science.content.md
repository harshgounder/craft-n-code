# Odisha Crop Evacuation Engine: Evidence, Gates, and Rules

## 1. EXECUTIVE SUMMARY

- **The defensible uniqueness is a crop-action compiler, not another weather app**: IMD already disseminates warnings through SMS, apps, NavIC, social media, CAP, APIs, and disaster-management agencies [27]. The product should convert an IMD hazard and a farmer's spoken farm state into a physical decision such as drain, harvest, cover, dry, relocate, flush, or resow, then confirm completion by IVR. -> Build the moat around two-way problem capture and plot-specific action selection, while using IMD as the authoritative hazard source.

- **Low literacy does not mean speech recognition must be the main input**: In the seven-month Avaaj Otalo pilot with 51 Indian farmers, users preferred touchtone navigation to speech every week; speech was more error-prone, but farmers valued recording questions and hearing trusted experts and other farmers [13]. -> Use short Odia voice prompts, DTMF choices, an open-ended recorded-message fallback, callback by an agronomist, and repeat-back confirmation.

- **Swarna-Sub1 is deployment-ready, but it is not flood-proof**: A randomized study across 128 Odisha villages found about **45% higher yield than Swarna after 10 days of submergence**, benefits over 7-14 days, and no statistically significant penalty without flooding [5]. IRRI's Odisha deployment evidence warns that even Sub1 varieties can fail when stagnant flooding exceeds roughly 15 days [11]. -> Recommend Sub1 only for mapped flash-flood ecologies, expose the duration ceiling, and switch to rescue or re-establishment logic when forecast inundation exceeds it.

- **Flood tolerance and salt tolerance cannot be added like independent scores**: Saltol is primarily a seedling-stage QTL that improves K+/Na+ balance, while reproductive-stage salinity tolerance involves other loci [4]. A 2026 CR1009-Sub1 breeding paper pyramided Sub1, Saltol1, and Pup1, but its abstract reported neither combined-stress field performance nor cultivar release [10]. -> A coastal plot facing saline surge plus submergence must be labeled "combined-stress evidence unavailable," not promised the sum of Sub1 and Saltol benefits.

- **The newest priming result is promising but not yet an Odisha rule**: A March 2024 study used **1% CaCl2 halopriming** in rice seedlings exposed to 50 or 100 mM NaCl and saline or non-saline submergence; it reported physiological improvements but no farmer-scale yield, storage, or field-readiness result [3]. -> Keep halopriming in a supervised pilot module; do not broadcast a universal recipe. Hydropriming, PGPR, and mycorrhizal claims likewise need local flood-field validation.

- **Nutrient recovery is more credible than PGR spraying, but dosage still needs local sign-off**: A Cuttack experiment found that post-desubmergence foliar urea improved photosynthesis, flowering recovery, and productivity after 15 days of complete submergence [22]. A 2024 field preprint achieved approximately 98% survival and the highest reported yields by splitting N after an 18-day flood, but it remains a preprint and used specific Sub1 varieties and soils [7]. -> Trigger assessment and extension-approved N recovery only after drainage and survival checks; block automatic PGR, silicon, potassium, or zinc prescriptions where dose-response evidence is absent.

- **The strongest immediate physical rules are simple and time-sensitive**: The 24 October 2024 NRRI advisory said to keep drainage channels open in immature paddy, move harvested rice to safer places under tarpaulin, sun-dry grain for one or two days after rain, and store it in sound bags [2]. -> Deliver one action per call, include a deadline and "done/not possible" response, and escalate barriers such as no labor, pump, tarpaulin, or safe storage.

- **Resilient production systems are seasonal investments, not cyclone-hour evacuation steps**: Bangladesh floating gardens operate over about **2,500 ha** and are estimated by FAO to produce roughly ten times as much as similarly sized land cultivation, but FAO supplies no absolute yield, cost, or sample size [12]. A 2025 eastern India crop-fish study reported **13.40 t/ha rice-equivalent yield versus 3.52 t/ha control**, but required ponds, trenches, dykes, capital, and multi-season management [24]. -> Offer these through a pre-season investment planner, not as emergency SMS advice.

- **Climate models justify adaptation but cannot select tomorrow's action alone**: An Odisha DSSAT study projects 2026-2050 rice-yield declines of **18.8% under RCP4.5 and 20% under RCP8.5**, together with large increases in water footprint [23]. -> Use climate projections to prioritize districts, varieties, drainage, water storage, and trials; use real-time IMD, field water depth, crop stage, salinity, and farmer capacity for event decisions.

## 2. INVENTORY / EVIDENCE TABLE

**Grade rubric:** **A** = operationally usable in Odisha in 2026, supported by local field evidence or an authoritative operational advisory. **B** = credible field evidence or an established system, but transfer, dose, or implementation still needs local calibration. **C** = peer-reviewed laboratory, greenhouse, single-station, modeling, or preprint evidence suitable only for a supervised pilot. **D** = no qualifying flood-field validation found, ambiguous identity, or a marketing/speculative claim.

| What | Named source, URL, date | Mechanism and quantified evidence | 2026 feasibility | Grade |
|---|---|---|---|---|
| IMD alert ingestion | IMD, *Cyclone Warning in India: SOP*, current operational source, http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf | Multi-channel dissemination includes SMS, IVR, apps, NavIC, NAVTEX, CAP, APIs, and social media [27]. | Use CAP/API as authoritative trigger; preserve bulletin version and issue time. | A |
| Low-literacy problem capture | Patel et al., *Avaaj Otalo*, 2010, https://dl.acm.org/doi/10.1145/1753326.1753434 | Farmers recorded questions and browsed answers; DTMF outperformed speech preference and reliability in a 51-user, seven-month pilot [13]. | Ready as an interaction pattern, not proof of agronomic outcome. | A- |
| Pre/post-cyclone paddy actions | NRRI advisory reported 24 Oct 2024, https://odishatv.in/news/odisha/how-odisha-paddy-farmers-can-minimise-losses-due-to-cyclone-dana-scientists-release-advisory-247268 | Drain immature paddy; protect harvested grain; dry for 1-2 days; store safely [2]. | Direct rule set. Fumigation must retain label, airtightness, safety, and expert-control warnings [2]. | A |
| Swarna-Sub1 and FR13A/Sub1A | Dar et al., *Scientific Reports*, 2013, https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307 | FR13A-derived Sub1A uses quiescence. Odisha RCT: about 45% higher yield at 10 submerged days, reduced variability, no significant no-flood penalty [5]. | Recommend for suitable flash-flood lowlands and available certified seed. | A |
| Sub1A ceiling | IRRI Rice Today Odisha deployment, accessed 16 Aug 2026, https://ricetoday.irri.org/variety-based-climate-smart-intervention-helps-smallholder-farmers-cope-with-flood-in-the-lowlands-of-odisha | Sub1 conserves carbohydrate by limiting elongation, but stagnant flooding beyond about 15 days can defeat the variety [11]. | Hard guardrail: never describe it as indefinite flood tolerance. | A |
| Ethylene/ABA/GA signaling | Schmitz et al., *New Phytologist*, 2013, https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.12202 | Trapped ethylene induces SUB1A; DELLA proteins suppress GA-driven elongation; ABA-responsive genes support post-flood dehydration response [16]. | Useful for explaining early timing and variety behavior, not for unsupervised hormone dosing. | B for mechanism; D for spray rule |
| Saltol and Pokkali | Tiwari et al., *Plants*, 2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11054697 | Saltol on chromosome 1 improves seedling K+/Na+ homeostasis. Pokkali is a tolerant donor but is tall and low-yielding [4]. | Variety-planning evidence; require crop stage and soil/water EC. | B |
| CSR salt-tolerant varieties | ICAR-CSSRI crop-improvement catalog, accessed 16 Aug 2026, https://cssri.res.in/crop-improvement | The official catalog lists CSR releases including CSR10, CSR13, CSR27, CSR43, CSR46, CSR49, and CSR52; listed release years begin with CSR10 in 1989 [21]. | Use only where the notified geography, seed availability, duration, grain type, and measured salinity match the farm. Do not assume every CSR entry is Odisha-notified. | B |
| Combined Sub1 + Saltol + Pup1 | Rekha et al., *Molecular Biology Reports*, 2026, https://link.springer.com/article/10.1007/s11033-026-11461-2 | Marker-assisted backcrossing produced ten BC2F2 plants carrying all three loci, with up to 94.8% recurrent-parent recovery [10]. | Breeding result, not a released combined-stress recommendation; phenotype and multi-location field data remain missing. | C/D |
| Deepwater rice | ICAR-CRRI, *Rice varieties/hybrids developed during 1968-2025*, 2025, https://icar-crri.in/wp-content/uploads/2025/11/CRRIs-varieties-1968-2024.pdf | Deepwater ecology is defined as >50 cm to 2 m. Odisha-listed examples include CR Dhan 500, Jalamani/CR Dhan 503, Jayanti Dhan/CR Dhan 502, CR Dhan 505, 507, and 508, with catalog yields of 3.5-4.75 t/ha [19]. | Seasonal ecology choice, not a response to a cyclone already approaching. Verify certified seed and district suitability. | B |
| "Jaladhi" and "HBJ" labels | Same ICAR-CRRI catalog plus targeted search, 2025-2026 | Neither label was confirmed in the official CRRI catalog used here. Search hits connected HBJ to Hobiganj Boro material in Bangladesh, not a verified Odisha release. | Do not put either name into production recommendations until variety identity and notification are documented. | D |
| Hydropriming | 2024-2026 review/search corpus | General pre-germinative hydration is biologically plausible, but no recent Odisha on-farm flood trial with protocol, storage life, survival, and yield was located. | Optional research protocol only. | D for flood advisory |
| CaCl2 halopriming | Hussain et al., *Plant Physiology and Biochemistry*, Mar 2024, https://www.sciencedirect.com/science/article/pii/S0981942824001621 | 1% CaCl2 improved selected chlorophyll, H2O2, and sugar responses in seedlings under 50/100 mM NaCl and combined stress [3]. | Promising pilot; missing full farmer protocol and field yield. | C |
| PGPR biopriming and mycorrhizae | 2024-2026 search corpus; no qualifying Odisha flood-field trial | Products can be host-, soil-, formulation-, and environment-sensitive. The reviewed evidence did not establish a reproducible flood/submergence rule for Odisha. | Do not recommend by brand or generic organism class without local product-specific trials. | D |
| PGR sprays | Signaling review and targeted 2024-2026 search | SUB1A mechanism does not itself prove that ABA, ethylene inhibitors, brassinosteroids, melatonin, or GA inhibitors work safely in farmers' flooded fields. No dose-window-outcome trial adequate for a production rule was found. | Research mode only; no automated PGR prescription. | D |
| Silicon for lodging/salinity | 2025 salinity review and 2026 lodging review; no qualifying local cyclone field trial | Silicon has plausible structural and ion-homeostasis mechanisms, but the search did not establish an Odisha dose, formulation, timing, wind/rain threshold, or benefit-cost result. | Soil-test and extension-controlled pilot only. | C/D |
| Potassium timing | Singh et al. preprint, posted 8 Jan 2024, https://www.biorxiv.org/content/10.1101/2024.01.05.574436v1.full-text | Its best N schedule used full P and K basally, but it did not isolate a pre-flood K treatment effect [7]. | Do not infer a universal emergency K dose from this study. | C/D |
| Post-flood N | Gautam et al., *Ecological Engineering*, Apr 2015, https://www.sciencedirect.com/science/article/pii/S0925857415000464 | In Cuttack, foliar urea after desubmergence improved photosynthesis, flowering recovery, yield, and productivity following 15-day submergence [22]. | Use only after water recedes, survival is checked, and local extension supplies the dose. | B |
| Split N with Sub1 | Singh et al., bioRxiv, 8 Jan 2024, URL above | In a two-season field study, delayed split N after 18-day flooding produced about 98% survival and 3.26/2.97 t/ha in two Sub1 varieties [7]. | Useful trial design, but not yet peer-reviewed or Odisha-calibrated. | C |
| Zinc after flooding | Targeted 2024-2026 search | No post-flood Odisha dose-response trial linking Zn treatment to recovery and yield was located. Ordinary Zn-deficiency management is not evidence for a flood-recovery rule. | Diagnose deficiency; do not auto-dose because a flood occurred. | D |
| Bangladesh floating gardens, or baira/dhap | FAO GIAHS, site recognized 2015, https://www.fao.org/giahs/giahs-around-the-world/bangladesh-floating-garden-agricultural-practices/en | Water-hyacinth and bamboo beds support vegetables in flooded wetlands; FAO reports 2,500 ha and an estimated 10x area productivity [12]. | Demonstration in hydrologically comparable Odisha wetlands; first measure absolute yield, labor, biomass supply, tenure, and cost. | B- |
| Raised beds plus drainage | NRRI Dana advisory, 24 Oct 2024, URL above | Drainage is operationally supported for immature paddy [2]. The search did not find a rigorous Odisha raised-bed vegetable flood trial with dimensions and benefit-cost data. | Drainage is ready; raised-bed design needs local engineering trials. | A for drainage; C for bed specification |
| Sack gardens and vertical/hydroponic units | 2024-2026 targeted search | Search results were mainly generic, urban-agriculture, or promotional material. "Flood-proof" ignores anchoring, nutrient contamination, power, pump, structure, and cyclone-wind failure. | Exclude from emergency advice; test only as protected community infrastructure. | D |
| Mangroves/agroforestry | Mahanadi coastal-vulnerability literature, 2022-2026 | Coastal vegetation can be a landscape buffer, but no source located here quantified farm-level crop-loss reduction for a specified belt width and Odisha cyclone. Mangroves also occupy protected ecosystems and cannot be treated as an instant on-farm action. | Long-horizon coastal planning, not a plot-level evacuation recommendation. | C/D |
| Integrated crop-fish system | CABI Agriculture and Bioscience, 26 Feb 2025, https://www.cabidigitallibrary.org/doi/10.1079/ab.2025.0015 | Assam field system used 60% main field, 23% dykes, 7% refuge pond, and 10% trenches; rice-equivalent yield was 13.40 versus 3.52 t/ha control [24]. | Strong candidate for Odisha adaptive trials; requires capital, land modification, fish escape control, and seasonal planning. | B |
| Odisha climate adaptation model | Sahoo et al., *Environmental Monitoring and Assessment*, 2023, https://link.springer.com/article/10.1007/s10661-023-11117-9 | DSSAT projects 18.8-20% rice-yield decline by 2050 and 66.6-101.9% increases in total water footprint across varieties/scenarios [23]. | Good for portfolio and district planning; not an event-level loss estimator. | B |

**Inventory takeaway:** Only IMD ingestion, IVR/DTMF interaction, Sub1 deployment with a duration ceiling, drainage and grain-protection actions, and cautious post-flood N assessment are ready for the first production rules. The frontier genetics, priming, signaling, and resilient-system evidence should be visible in the product, but its evidence grade must constrain what the engine is allowed to say.

## 3. COVERAGE TABLE

"Useful hits" below means distinct sources that changed an evidence grade or an engine rule, not every duplicate search result.

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| IMD/RSMC official warnings and SOPs | 5+ | Strong hazard dissemination; does not contain plot-specific crop physics. | High for alert ingestion; low for crop action selection. |
| ICAR-NRRI/CRRI and Odisha advisories | 4 | Strong for paddy and released varieties; sparse for vegetables, orchards, livestock-feed crops, and quantitative action thresholds. | High for the paddy MVP. |
| ICAR-CSSRI and rice genetics literature | 6+ | Good single-stress genetics; weak combined salinity-submergence phenotype and Odisha release evidence. | Medium-high for seasonal variety planning. |
| 2024-2026 peer-reviewed priming literature | 3 | Mostly seedling physiology; missing on-farm yield, storage, formulation, and protocol reproducibility. | Low for production; adequate for pilots. |
| Stress-signaling and PGR literature | 3 | Strong molecular explanation; no adequate Odisha flood-field dose-window trial for sprays. | High for mechanism, very low for prescription. |
| Nutrient-management literature | 4 | N has field support; K is confounded with full fertilizer packages; Zn and silicon lack flood-specific local dose-response evidence. | Medium, with N-only initial scope. |
| Resilient production-system literature | 5 | Baira and crop-fish have field evidence, but Odisha transfer costs and cyclone failure modes remain uncertain. Sack and hydroponic hits were mostly generic. | Medium for pre-season pilots, low for emergency advice. |
| Odisha climate-model literature | 2 | One useful DSSAT study; little event-scale compound heat-flood-salinity validation. | Medium for prioritization, low for operational trigger thresholds. |
| HCI/IVR field studies | 2 | Strong interaction lessons but old, small, and not an Odisha agronomic-outcome RCT. | Medium-high for interface design; outcome validation still needed. |
| Commercial pages, YouTube, ResearchGate duplicates, generic blogs | Many | Unsupported variety names, "flood-proof" systems, vendor claims, and duplicate abstracts. | Excluded from rule evidence. |

The evidence is asymmetrical: hazard messaging and flash-flood rice are comparatively mature; combined coastal stresses, non-rice crop physics, and treatment dosing are not. Therefore, breadth in the user interface should not be confused with breadth in validated agronomy.

## 4. WHAT IS MISSING

### The exact research gap

The central missing artifact is an **Odisha crop-action response surface** linking:

`hazard x crop x variety x growth stage x water depth x duration x salinity EC x turbidity x wind x soil/drainage x available labor/assets -> physical action, deadline, expected avoided loss, cost, and recovery probability`.

No located study jointly estimates those variables. Existing work isolates pieces: Swarna-Sub1 under 7-14 days of submergence [5], Saltol mainly at seedling salinity [4], a seedling halopriming experiment [3], and a model of mid-century rice yield and water footprints [23]. The platform's most valuable output - "what should this farmer physically do now?" - therefore needs a local decision-trial program rather than an AI-generated synthesis alone.

Specific gaps are:

1. **Combined flood plus salt:** Multi-location Odisha trials of released and candidate rice lines under crossed water depth, submergence duration, EC, crop stage, turbidity, and recovery. The 2026 Sub1-Saltol1-Pup1 pyramid has genotype confirmation, not the required phenotype or release evidence [10].
2. **Thresholds for crop evacuation:** For each crop and stage, compare early harvest, in-field protection, drainage, relocation, and no action. Measure quality penalty, labor-hours, machinery access, avoided loss, and safe completion time.
3. **Priming translation:** Registered protocol, seed storage after priming, germination, stand survival, yield, cost, and farmer error rates across local varieties. A physiological seedling effect is insufficient [3].
4. **PGR timing:** Preregistered field trials of named compounds with formulation, dose, pre-flood window, crop stage, residue and safety controls, and yield. The SUB1A pathway cannot substitute for this evidence.
5. **N, K, silicon, and Zn decision curves:** Soil-test-stratified trials that separate nutrients, compare foliar and soil routes, specify when water has receded enough, and quantify lodging, survival, grain yield, runoff, and phytotoxicity.
6. **System transfer:** Odisha benefit-cost and failure testing for baira, crop-fish trenches, raised beds, sacks, and protected hydroponics under cyclone wind, saline water, debris, power loss, and insecure tenure. FAO's 10x baira estimate has no absolute yield or cost in the cited source [12].
7. **Deepwater nomenclature:** "Jaladhi" and "HBJ" need a citable release authority, genetic identity, ecology, and seed source before use. The official catalog instead supports named CR Dhan/Jalamani/Jayanti Dhan entries [19].
8. **Compound climate-to-event models:** Downscaled probabilities for cyclone wind, storm surge salinity, river flood, heat, and drainage congestion, connected to crop stage and observed loss - not only mid-century mean impacts.
9. **Voice capture validation:** An Odisha trial comparing DTMF, automatic speech recognition, recorded voice, and human callback on completion, comprehension, error, gender access, dialect, trust, and avoided crop loss.

**Decision-ready insight:** The research program should be designed around decisions, not products. "Does calcium chloride help a seedling?" is less useful than "Given a 48-hour warning, can a farmer execute this protocol, and does it beat drainage, early harvest, or doing nothing after costs and error are counted?"

## 5. HOW IT FEEDS THE ADVISORY ENGINE

### 5.1 Architecture: alert -> farm state -> feasible action -> confirmation

IMD should remain the hazard authority. Its four-stage system includes a Cyclone Alert at least 48 hours before expected adverse weather and a Cyclone Warning at least 24 hours before it [28]. During Cyclone Dana, IMD issued pre-genesis track, intensity, and landfall information about 3.5 days before landfall and repeated it consistently [29]. The engine should version every bulletin, geofence affected villages, and recompute advice only when track, wind, rainfall, surge, or timing materially changes.

The farmer state should be captured through a short Odia IVR:

1. Crop and plot.
2. Growth stage: seedbed, transplanted vegetative, flowering, grain filling, mature, harvested, or stored.
3. Current water depth and whether drainage is possible.
4. Coastal/saline-water exposure and EC if a sensor or extension worker has measured it.
5. Variety, if known; allow "do not know."
6. Assets: labor, pump, drain, tarpaulin, raised storage, transport, spare seedling nursery, safe pond refuge.
7. Farmer's recorded problem in up to 30 seconds.
8. DTMF confirmation: "done," "cannot do," "need callback," or "repeat."

This follows the field evidence that recorded questions and trusted expert responses are valuable, while touchtone navigation is more robust than speech recognition [13].

### 5.2 Evidence-constrained rule table

| Trigger/state | Engine action | Tradeoff shown to farmer | Evidence gate |
|---|---|---|---|
| IMD heavy rain/cyclone; immature paddy; drain exists | "Open and clear the drainage channel now. Reply 1 when done, 2 if blocked." | Labor now versus longer waterlogging. Escalate blocked drains to village response teams. | Production rule, A [2] |
| Paddy already harvested; prolonged rain expected | Move to the safest available raised place and cover fully with tarpaulin. | Movement labor and cover cost versus wet grain and storage loss. | Production rule, A [2] |
| Rain has stopped; grain became wet | Sun-dry for 1-2 days, then use sound bags; check moisture with an approved device if available. | Delayed storage versus mold/quality risk. | Production rule, A [2] |
| Flood-prone lowland; pre-season seed choice; expected flash flood <=14 days | Show locally notified Sub1 options and certified-seed source. | Small seed-switching cost; strong downside protection; do not promise survival beyond the tested range. | Production rule, A [5] |
| Forecast stagnant flooding >15 days | Suppress "Sub1 will protect" message. Activate nursery reserve, re-establishment, crop-switch, and loss-documentation workflow. | Rescue cost versus high failure risk beyond the variety's ceiling. | Hard guardrail [11] |
| Measured salinity; seedling stage | Rank locally notified salt-tolerant varieties using EC, duration, maturity, grain type, and seed supply. | Salt tolerance may trade against plant height, yield, maturity, and market preference. | Planner rule, B [4] |
| Salinity plus complete submergence | State that combined performance is uncertain; route to agronomist and collect EC/depth/duration outcome data. | Avoids false additive confidence from separate Saltol and Sub1 scores. | Gated [10] |
| Farmer asks about 1% CaCl2 priming | Offer only inside a registered pilot with an exact protocol and treated/untreated comparison. | Possible seedling benefit versus protocol error, storage loss, and absent field-yield evidence. | Research mode, C [3] |
| Water receded; surviving rice assessed | Ask an extension-approved module whether post-flood foliar/split N is appropriate; never invent a dose. | Recovery benefit versus runoff, scorch, cost, and inappropriate application while flooded. | Conditional B/C [22][7] |
| Request for PGR, silicon, K, Zn, PGPR, or mycorrhiza product | No automated dose. Capture product, crop, stage, soil test, and connect to expert or trial. | Prevents mechanism-to-prescription overreach and vendor substitution. | Gated C/D |
| Chronic seasonal flooding; land and capital available | Compare baira, drainage/raised bed, and crop-fish designs with local capital, labor, water, fish-escape, and market assumptions. | Higher diversification/productivity versus land modification and recurrent management. | Planning/pilot B [12][24] |

### 5.3 Quantified action selection

For every candidate action, compute:

`net action value = event probability x avoidable loss - direct cost - quality penalty - execution failure risk - safety penalty`

The engine should not pretend that every term is precisely known. It should display the evidence grade, data age, confidence range, deadline, and whether the action is reversible. It should reject an action when travel or field work violates official life-safety guidance, when the farmer lacks the required asset, or when completion time exceeds the forecast window.

A useful optimization target is **maximum expected crop value protected per constrained labor-hour**, subject to human safety, cash, equipment, and time. For example, covering already harvested grain may dominate a speculative spray because it is fast, reversible, locally advised, and protects value already created. This is the core crop-level "evacuation" concept: move vulnerable crop value into a safer state before the hazard, rather than merely telling the farmer that a cyclone is coming.

### 5.4 Learning loop without turning farmers into uncontrolled experiments

Every recommendation creates a structured outcome record: action offered, accepted/refused, reason, completion time, observed water depth/EC/duration, damage, yield, and farmer-rated usefulness. Research-mode interventions require consent, a comparison design, agronomist supervision, and predefined stop rules. Production rules may be promoted only after replication across districts and seasons.

**Decision-ready insight:** The algorithmic innovation is not a generative-advice chatbot. It is a constrained decision engine in which evidence grade controls which verbs are allowed: A can say "do," B can say "consider after checks," C can say "pilot under supervision," and D can only say "evidence insufficient."

## 6. REAL-vs-FILLER

| Classification | Claims that belong here | Product treatment |
|---|---|---|
| **Verified and usable** | IMD/CAP ingestion; DTMF plus recorded question/callback; drainage for immature paddy; tarpaulin protection and 1-2 day post-rain drying; locally suitable Sub1 for approximately 7-14 day flash flooding; explicit >15-day failure guardrail [2][5][11]. | Production rules with source, timestamp, deadline, safety check, and completion response. |
| **Verified but conditional** | Saltol/CSR seasonal variety planning; post-flood N recovery; deepwater CR Dhan/Jalamani/Jayanti Dhan varieties; baira; crop-fish systems; Odisha climate planning [4][22][19][24][23]. | Decision support only after local variety notification, soil/EC/asset checks, or an adaptation investment assessment. |
| **Peer-reviewed or scientific, but lab/early-stage** | 1% CaCl2 halopriming at seedling stage; Sub1-Saltol1-Pup1 marker pyramid; stress-signaling pathways; model projections outside event-scale validation [3][10][16]. | Explain and recruit supervised trials; no mass prescription. |
| **Preprint or single-setting evidence** | The 2024 split-N Sub1 study, with about 98% survival after an 18-day protocol, is useful but not peer-reviewed or Odisha-calibrated [7]. | Keep behind an agronomist approval gate. |
| **Marketing/filler until proven** | "AI predicts exact crop loss" without a local loss model; "flood-proof hydroponics" without wind, contamination, anchoring, and power tests; universal silicon/PGR/PGPR/Zn recipes; additive Sub1 + Saltol protection; unsupported Jaladhi/HBJ seed recommendations. | Exclude from farmer-facing claims and pitch-deck metrics. |

A credible system should be willing to return "not enough evidence" or "call an agronomist." That restraint is a feature: it protects farmers from converting molecular plausibility, a vendor testimonial, or a greenhouse result into an irreversible field action.

## 7. NOISE LOG

| Noise encountered | Why it was noisy | Disposition |
|---|---|---|
| "BAIRA" search results for the Bangladesh recruiting-agency association | Acronym collision with baira/dhap floating cultivation. | Excluded; used FAO's GIAHS floating-garden source instead. |
| "Jaladhi 2.0" videos and commercial seed pages | Marketing identity did not establish release authority, genetic identity, ecology, or notification. | Excluded pending an official varietal record. |
| HBJ search results | Results largely pointed to Hobiganj/Habiganj Boro material in Bangladesh, not a verified Odisha floating-rice release. | Marked unresolved; not used in recommendations. |
| Wikipedia, Grokipedia, generic cultivar lists | Helpful discovery leads but not adequate for release or performance claims. | Replaced with the ICAR-CRRI catalog [19]. |
| ResearchGate duplicates | Often duplicated abstracts without methods, complete results, or release status. | Used only to discover publisher or institutional sources; not used as decisive evidence. |
| Generic vertical-farm and hydroponic articles | Discussed water efficiency or urban production, not cyclone wind, surge contamination, anchoring, outage, and farmer economics. | Classified as filler for this problem. |
| Generic silicon, zinc, PGR, and microbial-product pages | Mechanisms or ordinary nutrient benefits were presented as if they proved flood recovery. | No production rule without crop-stage, dose, timing, safety, and yield evidence. |
| Non-Odisha salinity and storm-surge studies | Useful for hazard plausibility but not direct calibration of Odisha farm outcomes. | Context only; no local numeric threshold inferred. |
| Duplicate Cyclone Dana news reports | Repeated the same NRRI advisory rather than independent trials. | Counted as one advisory family, not multiple corroborating experiments. |
| Future-dated blogs and unsourced AI-agriculture papers | Contained broad claims without transparent field designs. | Excluded from evidence grading. |

The noise pattern itself is informative: the least mature topics generated the most promotional results. Search abundance is therefore not evidence maturity.

## 8. VERDICT: PARTIAL

### GO now

Proceed with an Odisha paddy-focused MVP that includes:

1. IMD CAP/API alert ingestion and bulletin versioning.
2. Village and plot geofencing.
3. Odia IVR with DTMF-first navigation, recorded questions, trusted-expert callback, and repeat-back confirmation.
4. Crop-stage and asset capture.
5. A small A-grade action library: drain immature paddy, protect harvested grain, post-rain drying/storage, Sub1 seasonal selection with the 15-day ceiling, and post-flood assessment.
6. Evidence grade, source, deadline, safety constraint, and "done/cannot do" feedback for every action.
7. Outcome logging for future Odisha decision trials.

This is technically and scientifically defensible. IMD demonstrated that cyclone information can arrive days before landfall, while local agencies can disseminate warnings rapidly [29][30]. Cyclone Dana also shows the potential scale: Odisha evacuated about 800,000 people, while approximately 3.595M people were affected and about 5,800 homes were damaged [29]. The missing value is not another alert; it is converting that lead time into feasible crop-value protection.

### GATED before production claims

Do not release automated farmer prescriptions for combined salt-submergence tolerance, CaCl2 or other priming, PGRs, silicon, emergency K or Zn, PGPR/mycorrhizae, sacks, hydroponics, or mangrove-based crop protection until local protocols and outcomes exist. Likewise, do not name Jaladhi or HBJ as Odisha recommendations without an official identity and notification.

Minimum promotion gates should include at least two Odisha seasons, multiple districts representing river flood and saline-surge ecologies, preregistered controls, certified input identity, crop-stage-specific protocols, yield and quality outcomes, cost/labor accounting, adverse-event reporting, and replication by an independent team. Voice advice also needs a usability and agronomic-outcome evaluation, not only call logs.

### Synthesis: why PARTIAL is the strongest answer

| Dimension | Sub1 genetics | Salt/combined genetics | Priming/PGR/nutrients | Resilient systems | IVR action engine |
|---|---|---|---|---|---|
| Mechanism | Quiescence conserves energy under temporary complete submergence. | Ion homeostasis and multiple stage-specific loci; joint stress remains unresolved. | Attempts to alter physiological preparedness or recovery. | Changes field geometry, crop location, water use, and enterprise mix. | Converts hazard plus farm state into a feasible physical action. |
| Scope | Variety and ecology, mainly rice. | Variety, stage, EC, and coastal hydrology. | Input, dose, and timing specific. | Whole farm or community infrastructure. | Multi-crop in principle, but only as broad as its validated rule library. |
| Evidence base | Odisha randomized field evidence and deployment history [5]. | Strong single-stress biology; weak combined field/release evidence [10]. | N has field support; 2024 halopriming is seedling-stage; most PGR/biological claims remain gated [22][3]. | Baira and crop-fish have real field histories, but transfer economics matter [12][24]. | Indian HCI field evidence supports DTMF/recording, but Odisha crop-loss impact remains to be tested [13]. |
| Time horizon | Pre-season seed choice; protects during a short flood. | Pre-season choice plus long-term breeding. | Hours/days only if a protocol has already been validated. | Months to years. | Minutes to seasons, depending on rule type. |
| Main tradeoff | Fails when inundation is too long or the ecology is wrong. | Tolerance at one stage may not protect another; yield and market traits matter. | Cheap in theory, but protocol errors, runoff, residues, and false confidence can destroy value. | Diversification and productivity versus capital, land modification, labor, and cyclone failure. | Accessibility and speed versus misclassification, overautomation, and stale evidence. |

Three tensions define the design. First, Sub1's **quiescence** strategy is not the same as deepwater rice's **escape/elongation** strategy; the engine must classify flood ecology rather than rank both on one "flood tolerance" score. Second, a mechanism can be well established while an intervention remains unproven: knowing that ethylene, ABA, and GA participate in submergence response does not validate a farmer spray. Third, emergency advice and resilient infrastructure have different clocks: drainage and grain covering belong in a 24-48 hour workflow, while crop-fish trenches, floating beds, mangroves, and variety portfolios belong in seasonal or landscape planning.

**Final decision:** **PARTIAL**. **GO** for the two-way, DTMF-first, evidence-constrained crop-action platform and a narrow paddy rule set. **GATE** frontier inputs and combined-stress recommendations behind Odisha trials. This division is itself the product's scientific uniqueness: it tells farmers what can be acted on now, what is a supervised option, and what remains an unanswered research question.

## References

1. *Using Data for Development: Evidence from a Phone System for ...*. https://www.povertyactionlab.org/sites/default/files/research-paper/working-paper_9244_Data-for-Development-Phone-System-for-Ag-Advice_Ethiopia_Oct2020.pdf
2. *How Odisha paddy farmers can minimise losses due to Cyclone ...*. https://odishatv.in/news/odisha/how-odisha-paddy-farmers-can-minimise-losses-due-to-cyclone-dana-scientists-release-advisory-247268
3. *Halopriming in the submergence-tolerant rice variety improved ...*. https://www.sciencedirect.com/science/article/pii/S0981942824001621
4. *QTLs and Genes for Salt Stress Tolerance - PMC - NIH*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11054697
5. *Flood-tolerant rice reduces yield variability and raises ...*. https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307
6. *Evaluation of the potential of multi-trait PGPR isolates as inoculants ...*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11682559
7. *Nitrogen Management on Improving Resilience of Flood- ...*. https://www.biorxiv.org/content/10.1101/2024.01.05.574436v1.full-text
8. *PGPR inoculants journey from lab to land: Challenges and limitations - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0944501324003112
9. *Adapting to salinity in coastal rice farming: integrating farmer perceptions with empirical field evidence | npj Climate Action*. https://www.nature.com/articles/s44168-025-00287-6
10. *Marker assisted pyramiding of Pup1 and Saltol1 QTLs and recurrent parent genome recovery in elite rice variety CR 1009 Sub1 | Molecular Biology Reports | Springer Nature Link*. https://link.springer.com/article/10.1007/s11033-026-11461-2
11. *Variety-based climate-smart intervention helps smallholder farmers cope with floods in the lowlands of Odisha – Rice Today*. https://ricetoday.irri.org/variety-based-climate-smart-intervention-helps-smallholder-farmers-cope-with-flood-in-the-lowlands-of-odisha
12. [
	Floating Garden Bangladesh | Globally Important Agricultural Heritage Systems | Food and Agriculture Organization of the United Nations
](https://www.fao.org/giahs/giahs-around-the-world/bangladesh-floating-garden-agricultural-practices/en)
13. *dl.acm.org*. https://dl.acm.org/doi/pdf/10.1145/1753326.1753434
14. [
            Physiological basis of tolerance to complete submergence in rice involves genetic factors in addition to the SUB1 gene - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC4243076)
15. *Frontiers | Flood-tolerant rice for enhanced production and livelihood of smallholder farmers of Africa*. https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2023.1244460/full
16. *SUB1A‐mediated submergence tolerance response in rice involves differential regulation of the brassinosteroid pathway - Schmitz - 2013 - New Phytologist - Wiley Online Library*. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.12202
17. *Salinity Stress in Rice: Multilayered Approaches for ... - PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12250271
18. *Submergence stress in rice: Adaptive mechanisms, coping ...*. https://www.sciencedirect.com/science/article/pii/S0098847221000770
19. *Microsoft Word - CRRI's varieties 1968-2024*. https://icar-crri.in/wp-content/uploads/2025/11/CRRIs-varieties-1968-2024.pdf
20. *Released Varieties – Central Rice Research Institute*. https://icar-crri.in/released-varieties/
21. *Crop Improvement – ICAR-CSSRI :: Central Soil Salinity Research Institute*. https://cssri.res.in/crop-improvement
22. *Effect of simulated flash flooding on rice and its recovery after flooding with nutrient management strategies - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0925857415000464
23. *Yield, water, and carbon footprint of rainfed rice production under the lens of mid-century climate change: a case study in the eastern coastal agro-climatic zone, Odisha, India | Environmental Monitoring and Assessment | Springer Nature Link*. https://link.springer.com/article/10.1007/s10661-023-11117-9
24. *Integrated crop-fish farming system improves land and water productivity in a flood prone lowland | CABI Agriculture and Bioscience*. https://www.cabidigitallibrary.org/doi/10.1079/ab.2025.0015
25. *Varieties Developed – ICAR-CSSRI :: Central Soil Salinity Research Institute*. https://cssri.res.in/varieties-developed
26. *Rice growth in a combined submergence and salinity stresses*. https://iopscience.iop.org/article/10.1088/1755-1315/752/1/012012/pdf
27. *http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf*. http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf
28. *http://rsmcnewdelhi.imd.gov.in/four-stage-warning.php*. http://rsmcnewdelhi.imd.gov.in/four-stage-warning.php
29. *http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf*. http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
30. *http://osdma.org/preparedness/early-warning-communications/ewds*. http://osdma.org/preparedness/early-warning-communications/ewds
