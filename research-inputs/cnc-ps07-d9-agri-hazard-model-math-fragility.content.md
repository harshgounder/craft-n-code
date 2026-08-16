# Quantifying Odisha Farm Risk: Evidence, Gaps, and Build Path

## 1. EXECUTIVE SUMMARY

- **A real cyclone-hazard spine exists, but not a complete damage model**: Holland (1980) provides an analytic radial pressure and wind framework with empirically or climatologically estimated parameters, while IMD reports supply event tracks, winds, radar and satellite observations. Phailin crossed near Gopalpur with sustained winds of **200-210 km/h, gusting to 220 km/h**, and Dana crossed near Bhitarkanika-Dhamara with **100-110 km/h, gusting to 120 km/h** [1][33][35]. The prototype can ensemble these hazards now, but a reproducible Kalsi (2006) Bay of Bengal B-parameter fit was not recovered and must not be invented. Source tags: [1]-[3].

- **Flood recurrence is usable; field-scale depth is not**: Bates and De Roo's raster model couples one-dimensional kinematic-wave channel routing to two-dimensional diffusion-wave floodplain flow. It achieved **81.9% correctly classified wet and dry cells** on the Meuse test, but its authors warn that shallow gradients amplify small water-level errors [14]. Odisha's atlas adds 18 years of satellite-derived inundation frequency, yet it is a historical hazard layer rather than a forecast of water depth or duration [42]. Source tags: [5]-[7].

- **Swarna-Sub1 is the strongest Odisha-specific agronomic result**: A randomized trial across **128 Orissa villages** found an approximately **45% yield advantage after 10 days of submergence**, with a maximum estimated advantage of about **718 kg/ha, or 66%, near 13 days** [12]. This can support next-season variety advice, but it is not a generic paddy damage curve for every variety, stage, depth or salinity condition. Source tag: [8].

- **The requested joint crop-fragility curve does not exist in transferable public form**: General salinity studies report large yield effects, and a controlled 0.3% saltwater experiment quantifies losses in yield components, but neither supplies an Odisha-calibrated function of growth stage x depth x duration x salinity [10][20]. The lodging literature models culm mechanics but does not validate a cyclone wind-speed-to-yield-loss curve [19]. Source tags: [9]-[11].

- **Official damage totals are calibration checks, not farm labels**: The final Government of India statement says Dana affected **87,855 ha of Odisha cropped area at 33% loss or above**, based on state information and an inter-ministerial field visit [27]. The circulated **5,428-acre** figure could not be traced to an authoritative source and should be discarded unless its original district, date and assessment sheet are produced. Source tags: [12]-[14].

- **Claim-packet logic can be quantified sooner than biological loss**: Current SDRF/NDRF norms use a **33% crop-loss threshold**, with assistance of **Rs. 8,500/ha for rainfed annual crops, Rs. 17,000/ha for assured-irrigated annual crops, and Rs. 22,500/ha for perennial crops**, normally capped at 2 ha per farmer [34]. These are relief norms, not compensation or proof that a model-estimated loss is accepted. Source tag: [14].

- **Groundwater recharge has sound measurement math but no event-level Odisha number**: The water-table fluctuation method uses `R = Sy x Delta h / Delta t` and requires local specific yield plus observed water-level rise [18]. Odisha's 2024 assessment reports **17.46 BCM total annual recharge** and **16.04 BCM extractable groundwater**, but these statewide annual accounts cannot be attributed to a particular flood [43]. Source tags: [15]-[16].

- **Freshness must be an engineered confidence policy**: IMD cyclone bulletins can move from three-hourly to hourly updates; GKMS district and block advisories are issued Tuesday and Friday for the next five days [41][39]. Soil Health Card documentation is internally inconsistent between two- and three-year cycles, so those cycles are not evidence that soil values remain agronomically valid for that long [2]. Source tags: [17]-[19].

- **Overall verdict: PARTIAL**: A free prototype can ingest official warnings, overlay historical flood exposure, collect farm profiles, generate risk bands and assemble evidence packets. A defensible probability of farm damage, rupee-valued "cost of waiting," and automated claim determination remain gated by local fragility trials, farm-level outcome labels, better elevation and drainage data, and repeat soil-EC observations. Source tags: [1]-[20].

## 2. DATA INVENTORY

**Reliability rubric:** A = official or primary, Odisha-local and directly usable; B = strong peer-reviewed method or experiment requiring transfer calibration; C = indirect, aggregate or outside Odisha; D = unsupported, inaccessible, decorative or not reproducible.

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---|---|---|---|
| Holland parametric wind field | Holland, "An Analytic Model of the Wind and Pressure Profiles in Hurricanes," 1 Aug 1980. URL: `https://journals.ametsoc.org/view/journals/mwre/108/8/1520-0493_1980_108_1212_aamotw_2_0_co_2.xml` | Radial storm pressure and wind profile; two empirically or climatologically estimated parameters [1] | Static method; event inputs must update with each IMD advisory | Journal page/report; equation transcription must be checked against the paper | B |
| Bay of Bengal B fit attributed to Kalsi (2006) | Claimed Kalsi 2006 result; no exact indexed primary paper, coefficient table, uncertainty or reproducible equation recovered | Unknown | Unknown | Needs IMD library, author copy or partner retrieval | D |
| Recent Odisha cyclone winds and tracks | IMD Phailin report, Oct 2013; Dana report, 7 Nov 2024; Yaas report, 11 Jun 2021. URLs: `https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads/report/26/26_38a1d4_phailin.pdf`, `https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf`, `https://internal.imd.gov.in/press_release/20210611_pr_1133.pdf` | Track points, storm-level intensity, district/station rainfall, radar and forecast verification; not farm exposure | Three-hourly and hourly during active events; retrospective reports after the event [35][41] | Free official PDF; live products through IMD | A |
| IMD machine-readable warning feed | IMD API page, publication date not stated. URL: `http://mausam.imd.gov.in/responsive/apis.php`; API documentation: `https://api.imd.gov.in/public/api_reference.html`; CAP RSS: `https://cap-sources.s3.amazonaws.com/in-imd-en/rss.xml` | Warning/product level; no farm profile | Live/current; endpoint-specific interval was not stated on the catalogue page | Public CAP feed; API may require IP whitelisting and IMD attribution [3] | A for alerts; B for undocumented endpoint behavior |
| Diffusion-wave flood routing | Bates and De Roo, "A simple raster-based model for flood inundation simulation," 10 Sep 2000. URL: `https://www.sciencedirect.com/science/article/abs/pii/S002216940000278X` | Raster cells tested at 25, 50 and 100 m over a 35 km Meuse reach [14] | Static method; requires current discharge/stage and terrain | Abstract/journal; implementation required | B |
| DEM uncertainty | "Uncertainties in the SRTM Heights," 8 Feb 2017. URL: `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5296860` | 30-90 m DEM pixels; validation at 221 Indian GPS control points [13] | Static terrain, but embankments, channels and bias corrections change | Free SRTM plus local survey/GPS correction | B for screening; D for uncorrected field-depth prediction |
| Odisha historical flood recurrence | NRSC-OSDMA, "Flood Hazard Atlas (2001-2018)," uploaded 2019. URL: `https://www.osdma.org/wp-content/uploads/2019/09/Flood-Hazard-Atlas.pdf` | State, district and detailed maps; sensors from 10 m Sentinel-1 to 188 m IRS WiFS [42] | Historical, ending 2018; not a live inundation layer | Free PDF/report; operational raster/vector access not documented | A for historical exposure; C for current depth |
| Paddy submergence response in Odisha | Dar et al., "Flood-tolerant rice reduces yield variability and raises expected yield," 2013. URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307` | Plot/farmer trial in 128 Orissa villages; Swarna vs Swarna-Sub1 [12] | 2011 flood-season evidence; biological result remains relevant but transfer needs validation | Free full paper | A for variety choice; B for generalized fragility |
| Physiological Sub1 response | "Physiological basis of tolerance to complete submergence in rice," 2014. URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4243076` | Controlled genotype and submergence experiment | Static research result | Free full paper | B |
| General rice salinity response | "Salinity Stress in Rice: Multilayered Approaches for Sustainable Tolerance," 2025. URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC12250271` | Cross-study review; variety and stage heterogeneity | Current review, but not local monitoring | Free full paper | C |
| Salt treatment by growth period | Li et al., "Effects of Salt Stress During the Growth Period on the Yield...," published 2024. URL: `https://www.mdpi.com/2073-4395/15/1/21` | Two conventional and four hybrid varieties under continuous 0.3% saltwater irrigation in Hainan, China [20] | Two trial years, 2022-2023 | Free article | B for mechanism; C for Odisha transfer |
| Rice wind lodging | Wang et al., "Rice stem lodging properties and bending modeling...," 2024. URL: `http://www.ijabe.net/cn/article/pdf/preview/10.25165/j.ijabe.20241703.8585.pdf` | Mature culm mechanical measurements and bending equations | Static experiment | Free PDF | B for mechanics; D for cyclone damage probability |
| Drought cascade modifier | Hassan et al., "Drought stress in rice," 2023. URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC10391551` | Review by crop stage; cites drought-flood alternation work | Static research synthesis | Free full paper | C; no Odisha multiplier |
| Cyclone Fani agricultural loss evidence | Government of Odisha, UN, World Bank and ADB, "Cyclone Fani Damage, Loss, and Needs Assessment," 2019. URL: `https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf` | Sector and affected-district assessment; selected field visits and departmental data | Post-event snapshot; estimates may change | Free official PDF/report | A for event narrative and sector totals; C as farm-training data |
| Cyclone Dana affected crop area | Ministry of Agriculture and Farmers Welfare, "Losses Incurred to the Farmers Due to Dana Cyclone," 17 Dec 2024. URL: `https://pib.gov.in/PressReleasePage.aspx?PRID=2085215` | Odisha-wide cropped-area aggregate: 87,855 ha at 33% loss or above [27] | Final parliamentary response based on state information | Free official release | A for statewide total; C for farm calibration |
| Claim relief rules | MHA, "Revised List of Items and Norms of Assistance from SDRF and NDRF," 10 Oct 2022, applicable 2022-23 to 2025-26. URL: `https://srcodisha.nic.in/dmrule/New%20Iitems%20and%20Norms%20of%20assistance%20from%20SDRF%20and%20NDRF%20dtd%2010%20Oct%202022%20(2)%20(1).pdf` | Per hectare and farmer; 33% threshold and 2 ha ceiling [34] | Policy-period document; verify successor rules after 2025-26 | Free official PDF | A for rule-engine reference, not claim approval |
| Flood-related groundwater recharge method | Addisie, "Groundwater recharge estimation using water table fluctuation and empirical methods," 12 Aug 2022. URL: `https://iwaponline.com/h2open/article/5/3/457/90174/` | Monitoring-well/time-step method; catchment-scale case study outside Odisha | Recomputed whenever water-level and specific-yield observations update | Free article plus field monitoring | B for method; C for Odisha values |
| Odisha groundwater resource account | Odisha DoWR, "Ground Water," citing Ground Water Assessment Report 2024. URL: `https://dowr.odisha.gov.in/sites/default/files/2026-01/Ground%20Water.pdf` | Statewide annual recharge and extractable-resource totals | Assessment year 2024; not storm-specific | Free report | A for state accounting; D for flood-event attribution |
| Data-refresh anchors | IMD GKMS SOP 2020; Soil Health Card note 16 Aug 2025. URLs: `https://mausam.imd.gov.in/imd_latest/contents/pdf/gkms_sop.pdf`, `https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=155036&lang=2&reg=3` | District/block five-day advice; soil card per land holding [39][2] | Twice weekly for GKMS; conflicting two- and three-year statements for soil cards | Free reports/portal; farm updates still require collection | B for cadence; C for agronomic validity |
| Coastal-soil salinity recovery | No Odisha-specific, repeat-measurement recovery curve was found; available literature reports salinity impacts and snapshots rather than a transferable time-to-recovery function | Needed at field and soil-depth level | Must update after surge, rainfall, drainage and leaching | Field EC, SAR/ESP and water-table collection; ICAR/OUAT partner | D today |

**Inventory takeaway:** official hazard, exposure and policy data are much stronger than biological vulnerability and recovery data. The engine should therefore report an uncertainty-aware risk band, not pretend that a precise farm-loss percentage is known.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing fields | Coverage judgment |
|---|---:|---|---|
| IMD and RSMC official cyclone records | 3 strong event reports plus API/CAP catalogue | Search results often returned the wrong cyclone; live API formats and endpoint update intervals were not fully documented; no farm exposure | A for hazard, C for damage |
| OSDMA, NRSC and NDMA | Odisha flood atlas, Fani DLNA, disaster documents | Atlas ends in 2018; listing pages obscure direct files; no public field-depth forecast or easily consumable Odisha raster API | A for historical exposure, C operationally |
| Odisha Agriculture, SRC and PIB | Dana final area, relief rules and post-event statements | Aggregates lack parcel, crop, variety, stage, yield and counterfactual yield; disaster-loss records are not centrally maintained [27] | A for official totals, C for model labels |
| Hydraulics and DEM literature | Bates-De Roo model, SRTM uncertainty, flood-damage methodology | Validation is mostly outside Odisha; no calibrated Mahanadi delta depth-duration forecast; DEM vertical error is large relative to shallow farm flooding [14][13] | B |
| IRRI/CGIAR and peer-reviewed rice trials | Strong Swarna-Sub1 randomized trial and Sub1 physiology | No universal stage x depth x duration table; trial estimates depend on timing, turbidity, management and event conditions [12] | A for Swarna-Sub1, B overall |
| ICAR/NRRI/OUAT public search surface | Agronomic context and likely institutional expertise | No public Odisha farm fragility matrix or calibrated cyclone lodging curve was recovered | D for immediate engine input |
| Salinity and lodging literature | Salinity thresholds, yield components, culm mechanics | Different countries, varieties and treatments; no saline-submergence interaction or wind-speed-to-yield-loss validation | C |
| Groundwater literature and Odisha accounts | Water-table fluctuation method; state annual recharge account | No post-flood, district or farm event recharge; specific yield and pumping corrections absent from the state summary | B for method, C for decision values |
| Freshness documentation | IMD active-event cadence, GKMS twice-weekly schedule, Soil Health Card parameters | No published half-lives for farm identity, crop stage, inundation, soil EC or management data | B for update anchors, D for universal half-lives |
| Commercial sites, news and generic global damage tables | Discovery only | Promotional crop-loss claims, unrelated Bihar maps, current weather pages, residential depth-damage curves and unsourced acreage | D |

**Coverage judgment:** the source stack earns **A-B coverage for hazard detection and warning**, **B-C for historical exposure and resilient-variety advice**, and **C-D for farm damage, recovery duration and rupee-valued avoided loss**. That asymmetry should appear explicitly in every SMS/IVR confidence statement.

## 4. WHAT IS MISSING

The following gaps are not minor formatting problems. They are the exact missing state variables, labels or response functions that prevent a calibrated probabilistic farm-damage model:

1. **Reproducible Kalsi-2006 Bay-of-Bengal Holland-B calibration.** Needed fields: exact title, storm sample, pressure and wind observations, B equation or table, Rmax treatment, averaging period, surface reduction, fit error and license. The search found references to Holland parameter work but did not recover the claimed primary result. Until obtained, B must be an ensemble parameter, not a fixed "Kalsi value."

2. **Farm-coordinate wind exposure history.** IMD reports storm-scale and station-scale conditions, not maximum 10 m wind, gust duration, direction and surface roughness at each parcel. Phailin and Dana demonstrate that Odisha landfall intensities span very different ranges [33][35], but they do not label farm damage.

3. **Odisha delta forecast depth-duration raster.** The flood atlas records how often a pixel was observed inundated, not forecast depth, onset, velocity or recession time. Its imagery may miss the peak, although Odisha's gentle terrain can preserve post-peak inundation [42].

4. **Hydrologically corrected field-scale DTM.** Public DEMs do not reliably represent small embankments, field bunds, culverts, canals, drainage blocks or recent breaches. SRTM's tested Indian errors are measured in meters, while damaging crop inundation can vary over much smaller vertical differences [13].

5. **Odisha paddy joint fragility tensor:** `damage fraction = f(variety, growth stage, water depth, duration, flow velocity, turbidity, temperature, antecedent condition, management)`. Swarna-Sub1 provides a strong duration-dependent treatment effect, not this complete function [12].

6. **Freshwater-submergence versus saline-submergence interaction curve.** The public evidence separately covers submergence and salt stress. It does not quantify whether their combined loss is additive, multiplicative or threshold-driven. A 0.3% continuous salt-irrigation experiment is not a storm-surge pulse [20].

7. **Odisha rice wind-speed-to-lodging-to-yield curve.** Existing mechanics measure bending, stiffness and critical moments in mature culms, but no retrieved study maps IMD gust speed and duration to lodging probability and harvested yield for Odisha varieties [19].

8. **Sequential drought-flood cascade multiplier.** Rice is especially drought-sensitive around reproductive development, and severe flowering stress can cause complete yield failure in some settings [16]. The retrieved evidence does not supply an Odisha-calibrated modifier for drought followed by flood or cyclone.

9. **Farm-level cyclone outcome labels.** Dana's official **87,855 ha** is one statewide thresholded aggregate [27]. Missing labels include parcel geometry, crop, variety, stage, pre-event expected yield, measured harvested yield, water duration, salinity, lodging, management and assessment date.

10. **Provenance for the Dana "5,428 acres" claim.** Exact-phrase and official-source searches did not recover an authoritative assessment matching that number. It needs the original district report, cutoff date and damage definition; otherwise it is noise.

11. **Odisha coastal-soil recovery curve.** Missing fields include pre-surge EC and sodicity, surge-water salinity, inundation duration, soil texture, drainage, rainfall/leaching, groundwater salinity, EC by depth through time, intervention and return-to-yield date.

12. **Flood-event groundwater recharge.** The **17.46 BCM** Odisha value is annual statewide recharge accounting, not recharge caused by Dana, Fani or a particular flood [43]. Event attribution needs monitoring-well hydrographs, specific yield, pumping, canal leakage and base-flow separation.

13. **Evidence-backed data half-lives.** Official sources provide production cadences, not universal validity constants. Crop stage can change materially within days while a boundary polygon may remain useful for years. One half-life for all profile fields would be false precision.

14. **Action-effect curves for cost of waiting.** The literature does not quantify, by stage and lead time, how much loss is avoided by early harvest, drainage, staking, moving inputs, washing salt, applying amendments or replanting. Without those response curves, the engine can rank urgency but cannot honestly promise a rupee saving.

## 5. HOW IT FEEDS THE ENGINE

### 5.1 Probabilistic architecture

For farm `f` and event `e`, maintain four distinct objects:

1. `H_e`: hazard ensemble - track, central pressure, wind intensity, rainfall, surge and river stage.
2. `X_f(t)`: farm state - polygon, crop, variety, sowing/transplant date, inferred growth stage, irrigation, drainage, soil and assets.
3. `V_f`: vulnerability model - a probability distribution over damage fraction, not a single curve.
4. `O_f`: observed evidence - farmer IVR answers, photos, water marks, satellite inundation, EC tests and official inspection.

The core prediction should be:

`P(D_f | H_e, X_f, O_f, model_version)`

and expected economic loss should be:

`E[L_f] = area_f x baseline_yield_f x local_price x E[D_f]`.

Where no local fragility data exist, return broad quantiles such as low/central/high loss, expose the missing variable, and ask one high-value IVR question. Do not collapse hazard intensity into damage without vulnerability evidence.

### 5.2 Decision mapping

| Data item | Engine transformation | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning / positive use |
|---|---|---|---|---|---|
| IMD alert, track and intensity | Create time-indexed hazard ensemble; geofence farms; retain alert ID and issue time | Trigger escalating SMS/IVR windows; prioritize farms inside wind/rain/surge envelopes | Preserve event timeline and actual observations | Attach official warning ID, issue time, forecast lead and observed track | Update local event climatology |
| Holland-type wind field | Sample uncertain `B`, `Rmax`, pressure deficit, translation and surface-reduction terms; output wind quantiles | Rank urgency to secure pumps, seed, inputs and harvestable crops | Target lodging and structure inspection | Estimate exposure band, never claim it proves damage | Compare wind exposure by farm location |
| IMD event reports | Back-test track, intensity and forecast error; Dana's 24/48/72-hour track errors were 32/24/29 km [35] | Inflate geofence at longer lead times | Replace forecasts with observations after passage | Add authoritative event summary | Recalibrate warning thresholds |
| Bates-De Roo diffusion wave plus local terrain | Conservative grid water balance with channel routing, rainfall, boundaries and drainage; ensemble DEM and breach uncertainty | Identify likely early inundation and last safe drainage/harvest window | Predict ponding and drainage priority | Estimate onset, footprint and duration with uncertainty | Identify drainage and bund investments |
| Odisha Flood Hazard Atlas | Convert five recurrence classes into historical prior, not live probability. Classes run from one observed inundation to 10-14 during 2001-2018 [42] | Pre-position messages in recurrent zones | Prioritize rapid assessment | Add historical exposure context | Crop/variety and infrastructure planning |
| Swarna-Sub1 trial | Use as a variety-specific prior for 7-14 day complete submergence; preserve trial uncertainty | No immediate event action unless variety is known | Do not infer generic survival for other varieties | Record variety and duration | Recommend tolerant seed in recurrently submerged farms; the 10-day advantage is directly relevant [12] |
| Salt and EC observations | Maintain separate freshwater and saline-water states; infer salt dose from EC x duration only after local calibration | Close or protect freshwater sources from surge contamination | Test EC by depth, drain where safe, use rainfall/leaching and amendments under agronomic supervision | Record EC, sampling depth, date, photo and laboratory/kit method | Salt-tolerant variety and drainage planning |
| Lodging mechanics | Use crop height, maturity and variety as qualitative modifiers until wind validation exists | Flag mature, tall or weak-stem stands for earlier attention | Map lodged area and harvestability | Add geotagged lodging photos and area estimate | Partner trials for local varieties |
| Drought history | Treat antecedent drought as a latent stress flag; widen damage uncertainty | Avoid confident recovery promises for already stressed fields | Inspect reproductive-stage fields first | Record irrigation gaps and stage | Select stress-tolerant varieties and water plans |
| Official loss and relief rules | Separate model estimate, inspector determination and relief eligibility | None | Direct farmers to correct evidence and deadlines | Check area, crop, irrigation class, >=33% threshold and PMFBY interaction; relief is not compensation [27][34] | Improve documentation before the next season |
| Monitoring-well data | Apply `R = Sy x Delta h / Delta t`, with pumping and non-recharge corrections | Protect wells from contamination before surge | Estimate local recharge only after water-quality screening | Not normally a crop-loss proof | Positive-use advice: groundwater storage opportunity versus salinity risk [18] |
| Farm-profile timestamps | Apply confidence decay `q_j(age) = 2^(-age/h_j)` to each field; reduce weight or widen variance as data age | Ask only for stale, decision-critical facts | Refresh water depth, EC and damage observations | Preserve timestamp and collector | Maintain profile quality over seasons |

### 5.3 Freshness policy for the prototype

The following half-lives are **engineering starting policies, not published biological constants**:

| Field | Evidence anchor | Proposed refresh trigger | Prototype half-life |
|---|---|---|---:|
| Active IMD cyclone hazard | Three-hourly bulletins and hourly landfall updates [41] | Every new bulletin; immediate on category, track or warning change | 3 hours; 1 hour near landfall |
| District agromet advice | Tuesday/Friday, next five days [39] | Each GKMS issuance | 3 days |
| Crop stage | Derived from planting date but changed by transplanting, stress and variety | Confirm after sowing/transplanting and before an event | 5 days in rapid reproductive phases; 10 days otherwise |
| Standing-water depth | Fast-changing after rainfall, breach or drainage | IVR/sensor update after major rain and every recovery visit | 6 hours during flood |
| Soil EC after saline surge | Changes with rainfall, drainage, depth and groundwater | Test at 0, 3, 7, 14 and 30 days, then adapt | 3 days initially |
| Static farm polygon | Usually stable but affected by lease, subdivision and season | Seasonal confirmation or ownership/lease change | 180 days |
| Soil nutrient baseline | Soil Health Card is per holding, but official text conflicts on a two- versus three-year cycle [2] | Annual/seasonal review; retest after major deposition, erosion or salinity event | 1 year, except EC and pH after disaster |

A stale value should not vanish abruptly. Its confidence weight should halve, while the model's uncertainty expands. For example, an unconfirmed crop stage should trigger an IVR question before issuing stage-specific harvest or drainage advice.

### 5.4 Quantified cost of waiting

Define:

`C_wait(Delta t) = E[L | action at t + Delta t] - E[L | action now] + P(window closes) x irreversible_cost`.

This is publishable only when three inputs are defensible: a lead-time hazard distribution, a crop/action response curve and local action cost. IMD supplies the first. The public literature supplies a strong next-season Swarna-Sub1 response and official relief thresholds, but not Odisha action-response curves for early harvest, drainage, salt washing or lodging prevention. Therefore:

- **Quantify now:** forecast lead time, probability of farm entering a hazard envelope, historical inundation class, evidence completeness, relief-rate scenario and variety-specific Swarna-Sub1 advantage.
- **Use bands only:** likely damage from wind or flooding.
- **Do not quantify yet:** rupees saved by acting six hours earlier, exact yield loss from a predicted gust, salinity recovery date or claim acceptance probability.

## 6. REAL-vs-FILLER

| Evidence or feature | REAL: defensible use | FILLER or misuse to reject |
|---|---|---|
| IMD CAP/API and bulletins | Live alert ingestion, warning provenance, geofencing and timing. IMD lists CAP, API documentation, attribution and whitelisting paths [3] | Claiming that an IMD warning directly predicts crop-loss percentage |
| IMD cyclone reports | Event back-testing, observed/estimated landfall intensity, forecast-error envelopes and communication cadence | Using landfall wind as every farm's 10 m gust without roughness, distance and track modeling |
| Holland model | Transparent parametric baseline and uncertainty ensemble | Hard-coding an unverified "Kalsi 2006 B" or treating one B as Bay-of-Bengal truth |
| Bates-De Roo model | Fast screening model after local terrain, boundaries and calibration | Quoting its 81.9% Meuse result as expected Odisha accuracy [14] |
| SRTM DEM | Regional drainage/exposure screening after bias checks | Predicting centimeter-scale paddy depth from uncorrected 30 m SRTM; Indian RMSE remained material even after filtering [13] |
| Odisha Flood Hazard Atlas | Historical recurrence prior and district planning | Calling a 2001-2018 observation-frequency class a real-time depth forecast |
| Swarna-Sub1 trial | Strong next-season advice for flood-prone, Swarna-growing settings | Treating a 45% relative advantage as 45% damage avoided for all varieties and stages |
| General salinity review | Variable selection, sensor design and qualitative risk escalation | Applying the cited 29.29% average saline-soil yield reduction to every Odisha storm-surge farm [10] |
| Hainan 0.3% salt trial | Priors for which yield components may fail and why field EC matters | Equating continuous salt irrigation to transient saline submergence in Odisha |
| Rice culm mechanics | Design partner experiments and collect stem/height/maturity variables | Converting a bending equation into an unvalidated cyclone fragility curve |
| Dana 87,855 ha | Official statewide calibration total and administrative benchmark | Training a parcel model on one aggregate or relabeling it as harvested yield loss |
| Dana 5,428 acres | None until original provenance is produced | Repeating it because it appeared in a prompt or secondary article |
| Fani DLNA | Sectoral baseline, recovery categories and qualitative/quantitative assessment approach [40] | Treating tentative departmental estimates as parcel truth; the report notes missing asset breakdowns and possible +/-10% change in some estimates [40] |
| SDRF/NDRF rates | Rule-engine scenario and checklist | Calling relief rates market-value compensation or promising payment |
| Odisha 17.46 BCM recharge | State water-resource context | Claiming a particular flood produced 17.46 BCM of recharge |
| Fixed salinity recovery time | None | Telling farmers soil will recover in a universal number of months without repeat EC/sodicity measurements |
| Half-life decay | Transparent software confidence mechanism | Presenting proposed half-lives as agronomic laws |

**Evidence test:** an item is operationally real only if it has a named source, timestamp, spatial unit, access path, definable uncertainty and a decision it can legitimately change. A paper title or statewide total without those links is context, not a model feature.

## 7. NOISE LOG

| Search or candidate discarded | Why discarded |
|---|---|
| Exact searches for "Kalsi 2006," "Holland B," and Bay of Bengal coefficients | Returned unrelated cyclone-season pages, generic Holland-parameter papers and MAUSAM issue indexes, but no reproducible Kalsi paper or coefficient. Result remains **unverified**, not zero or assumed. |
| "Cyclone Dana 5,428 acres" | No authoritative exact-source result. The official December 2024 statement instead reports **87,855 ha at >=33% loss** statewide [27]. Different scopes or dates may exist, but conflating them is unsafe. |
| Dana preparedness note dated 23 Oct 2024 | It says departments **will assess** crop loss after the cyclone; it is not the final assessment [9]. |
| Farmonaut claim of 2.2M ha affected by Fani | Promotional secondary source with an implausibly broad unsourced number; superseded by the official OSDMA DLNA for evidentiary use. |
| Generic JRC/World Bank global depth-damage spreadsheets | Primarily asset and generic land-use functions; no Odisha paddy variety-stage-duration-salinity curve. |
| Residential depth-damage catalogues | Building first-floor damage is not crop physiology. |
| Bihar Flood Hazard Atlas and Bihar FMIS | Same source family and useful method clues, but wrong state; replaced with the direct Odisha atlas. |
| Live Weather.com results returned during historical Fani/Phailin searches | Current weather noise caused by query interpretation; irrelevant to historical cyclone validation. |
| Commercial EOS agriculture API | Potential product, but not necessary when assessing what official/free data can power the prototype; commercial accuracy and licensing were not evaluated. |
| ResearchGate-only and Facebook results | Used at most for discovery; not accepted where a primary paper or official report was available. |
| SRTM used "as is" | The Indian validation explicitly warns against unassessed use and documents substantial error [13]. |
| Salinity recovery searches returning impact snapshots | Demonstrated salinity harm but did not provide pre-event baseline through recovery time series for Odisha paddy. |
| New 2026 cyclone-salinity papers outside Odisha | Potential comparators, but too geographically and operationally indirect to become a fixed Odisha recovery curve. |

The noise log matters because the dominant failure mode is not lack of papers; it is assigning a precise field or number to a source that never measured it.

## 8. VERDICT

### Grade: PARTIAL

A useful prototype can be built today with mostly public sources, but it must be framed as a **hazard-aware advisory and evidence-collection system**, not a validated farm-loss oracle.

| Build layer | Today with free/public data | Requires local collection | Requires partner or controlled access |
|---|---|---|---|
| Cyclone warning | IMD CAP RSS, API catalogue, official advisories and event reports | Farm geolocation and contact preference | IMD whitelisting, stable service agreement and historical feeds |
| Farm exposure | Odisha historical flood atlas, public DEM, forecast rainfall/wind envelopes | Parcel boundary, elevation checks, bund/drain condition, water depth | NRSC/OSDMA raster services; DoWR river-stage and high-resolution terrain |
| Agronomic state | Generic crop calendars and manually entered profile | Crop, variety, planting date, stage, irrigation, expected harvest and assets | Odisha Agriculture, OUAT, ICAR-NRRI and extension validation |
| Damage probability | Broad expert priors and Swarna-Sub1 evidence | Event-linked observations and measured yield | Multi-season fragility trials with ICAR-NRRI/IRRI/OUAT |
| Recovery | General drainage, salinity-testing and replanting decision trees | Repeat EC/pH/sodicity, water quality, photos and field inspection | Soil labs, extension agronomists and coastal-salinity researchers |
| Claim packet | IMD event ID, timestamp, geotag, before/after media, farm and crop fields, 33% rule checklist | Farmer declarations, measured affected area and assessor visit | SRC/Agriculture workflow integration, PMFBY/insurer rules and official acceptance |
| Positive-use recharge | Water-table fluctuation method and state resource context | Monitoring wells, `Sy`, pumping, rainfall and water-quality data | CGWB/DoWR hydrogeology and observation-well access |
| SMS/IVR delivery | Rule-based Odia prompts and confidence bands | Language, literacy and usability testing | Telecom/IVR provider and government sender integration |

**GO now:** ingest warnings; maintain timestamped farm profiles; infer broad exposure; issue pre- and post-event checklists; ask low-literacy IVR questions; preserve advisory provenance; overlay historical flood recurrence; and build structured claim packets. IMD already uses web, email, SMS and social dissemination, and Yaas operations sent **69 lakh SMS messages**, showing that warning delivery at scale is institutionally established [3][41].

**Collection required:** parcel GPS, crop and variety, planting date, stage, irrigation type, expected yield, local drainage, pre-event images, post-event water depth and duration, lodging fraction, EC by depth, harvested yield and action timestamps. These are the minimum labels for converting an exposure model into a damage model.

**Partners required:**

- **IMD/RSMC:** stable API access, metadata, historical best track, rainfall and radar products.
- **OSDMA/NRSC/DoWR:** machine-readable flood layers, river stages, embankment/breach data and better terrain.
- **Odisha Agriculture/SRC/PMFBY stakeholders:** anonymized assessment sheets, crop-cut/yield records, claim outcomes and rule alignment.
- **ICAR-NRRI, IRRI and OUAT:** controlled stage x duration x depth x salinity trials, lodging wind tests and recovery experiments.
- **Soil and groundwater agencies:** EC, SAR/ESP, monitoring-well and specific-yield data.

**GATED for production claims:** exact percent yield loss, exact rupee cost of waiting, automated eligibility determination, fixed salinity recovery date, and farm-specific flood recharge. The model must not issue those as facts until local validation exists.

### Synthesis

| Dimension | Wind | Freshwater flood | Saline surge | Drought cascade | Groundwater recharge |
|---|---|---|---|---|---|
| Mechanism | Aerodynamic loading and lodging/asset damage | Hypoxia, burial, depth and duration | Osmotic/ionic stress plus inundation | Reduced reserves and reproductive injury before later hazard | Water-table rise and aquifer storage |
| Best evidence | IMD tracks/intensity plus Holland baseline | Historical atlas, diffusion-wave hydraulics, Swarna-Sub1 trial | General salinity and controlled salt treatments | Stage-sensitive drought reviews | Water-table fluctuation equation |
| Odisha specificity | High for hazard, low for crop fragility | High for recurrence and Sub1 trial, low for depth-duration curves | Low | Low | State total only, not event recharge |
| Time horizon | Hours to days | Hours to weeks | Days to seasons | Weeks to season | Days to annual accounting |
| Main trade-off | Fast warning but uncertain surface exposure | Good footprint but DEM/drainage sensitivity | Recovery depends on leaching, drainage and soil chemistry | A hidden antecedent modifier | More water can mean either useful recharge or saline contamination |
| Honest advisory output today | Hazard band and action deadline | Exposure/ponding band and drainage priority | Test-first recovery workflow | Elevated uncertainty and inspection priority | Measure-first positive-use assessment |

The central non-obvious result is that **hazard data are freshest where fragility data are weakest**. IMD can update a cyclone hourly, yet the system still may not know the farmer's variety, stage, culm strength or drainage. Conversely, the strongest crop result, Swarna-Sub1's Odisha trial, supports a slow next-season seed decision more defensibly than an urgent event-specific loss percentage.

The second tension is between **mapping and causality**. Satellite inundation and official affected-area totals show where water or loss occurred, but they do not identify depth, duration, salinity or avoided loss. The prototype should use them to prioritize, collect evidence and update priors, not as automatic claim proof.

The practical architecture is therefore asymmetric: automate hazard ingestion and message timing; keep biological loss probabilistic and conservative; use IVR to close the highest-value data gaps; and treat every disaster as a structured calibration campaign. That produces a useful system now while building the missing Odisha evidence needed for a later validated Ariadne-style transplant.

## References

1. *An Analytic Model of the Wind and Pressure Profiles in Hurricanes in: Monthly Weather Review Volume 108 Issue 8 (1980) *. https://journals.ametsoc.org/view/journals/mwre/108/8/1520-0493_1980_108_1212_aamotw_2_0_co_2.xml
2. [
	Press Note Details: Press Information Bureau
](https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=155036&lang=2&reg=3)
3. *IMD APIs | India Meteorological Department*. http://mausam.imd.gov.in/responsive/apis.php
4. *Loss and damage estimation from Extreme Climate Events in Rice Crop Using Remote Sensing Based Information for farmers’ risk reduction | Asia-Pacific Network for Global Change Research*. https://www.apn-gcr.org/project/loss-and-damage-estimation-from-extreme-climate-events-in-rice-crop-using-remote-sensing-based-information-for-farmers-risk-reduction
5. *Effects of Sodium Salts on Soils in Coastal Agricultural Fields | NC State Extension Publications*. https://content.ces.ncsu.edu/effects-of-sodium-salts-on-soils-in-coastal-agricultural-fields
6. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
7. *Initial soil moisture and soil texture control the impact of storm surges in coastal forests - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0048969724060674
8. *Flood Damage Assessment: A Review of Flood Stage–Damage Function Curve | SpringerLink*. https://link.springer.com/chapter/10.1007/978-981-287-365-1_13
9. *Dhx1Ir7Zinformation On Cyclonic Storm “Dana”*. https://srcodisha.nic.in/newspapper/dHx1Ir7zInformation%20on%20Cyclonic%20Storm%20%E2%80%9CDANA%E2%80%9D.pdf
10. [
            Salinity Stress in Rice: Multilayered Approaches for Sustainable Tolerance - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC12250271)
11. *Storm surge-induced soil salinization and its impact on agriculture in the coastal area of the Indian Sundarban - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2211464525001162
12. [
            Flood-tolerant rice reduces yield variability and raises expected yield, differentially benefitting socially disadvantaged groups - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307)
13. [
            Uncertainties in the Shuttle Radar Topography Mission (SRTM) Heights: Insights from the Indian Himalaya and Peninsula - PMC
        ](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5296860)
14. *A simple raster-based model for flood inundation simulation - ScienceDirect*. https://www.sciencedirect.com/science/article/abs/pii/S002216940000278X
15. *Ptc 52 Report Version3*. https://mausam.imd.gov.in/ptc/pdf/PTC-52_Report_Version3.pdf
16. [
            Drought stress in rice: morpho-physiological and molecular responses and marker-assisted breeding - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10391551)
17. *Cyclone Fani Impact: Lessons For Coastal Agriculture*. https://farmonaut.com/asia/cyclone-fani-impact-lessons-for-coastal-agriculture
18. *Groundwater recharge estimation using water table fluctuation and empirical methods | H2Open Journal | IWA Publishing*. https://iwaponline.com/h2open/article/5/3/457/90174/Groundwater-recharge-estimation-using-water-table
19. *ijabe.net*. http://www.ijabe.net/cn/article/pdf/preview/10.25165/j.ijabe.20241703.8585.pdf
20. *Effects of Salt Stress During the Growth Period on the Yield and Grain Quality of Hybrid Rice*. https://www.mdpi.com/2073-4395/15/1/21
21. [
	(at 10.00 Hrs. IST)- Super Cyclonic Storm ‘AMPHAN’ over Westcentral Bay of Bengal: Cyclone Warning for West Bengal and north Odisha coasts: RED Message 
](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1625271)
22. *Sub: Extremely Severe Cyclonic Storm “Biparjoy” (pronounced as “Biporjoy”) over eastcentral Arabian Sea: Cyclone Alert for Saurashtra & Kutch Coasts*. https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads%2Farchive%2F1%2F1_094174_41.%20National%20Bulletin%2020230610_0300.pdf
23. [
	(at 1730 Hrs. IST)-Super Cyclonic Storm ‘AMPHAN’ over West central Bay of Bengal: Cyclone Warning for West Bengal and north Odisha coasts: Orange Message
](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1625146)
24. [
	(at 1430 Hrs. IST)-Super Cyclonic Storm ‘AMPHAN’ over Westcentral Bay of Bengal: Cyclone Warning for West Bengal and north Odisha coasts: Orange Message
](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1625091)
25. [
	(at 1730 Hrs. IST)-Super Cyclonic Storm ‘AMPHAN’ over West central Bay of Bengal: Cyclone Warning for West Bengal and north Odisha coasts: Orange Message
](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1625146&reg=48&lang=2)
26. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
27. [
	Press Release Page | Press Information Bureau
](https://pib.gov.in/PressReleasePage.aspx?PRID=2085215)
28. *Flood Hazard Atlas*. https://ndem.nrsc.gov.in/hydrological_fhz.php
29. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Flood Hazard Zonation Atlas-Odisha*. https://www.osdma.org/publication/flood-hazard-zonation-atlas-odisha
30. [
		Vol. 57 No. 3 (2006): MAUSAM
							| MAUSAM
			](https://mausamjournal.imd.gov.in/index.php/MAUSAM/issue/view/45)
31. *Submergence stress in rice: Adaptive mechanisms, coping strategies and future research needs - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0098847221000770
32. [
            Physiological basis of tolerance to complete submergence in rice involves genetic factors in addition to the SUB1 gene - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC4243076)
33. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads%2Freport%2F26%2F26_38a1d4_phailin.pdf
34. *F.NO.33-03/2020-NDM-I (Vol-ll) Government of India Ministry of Home Affairs (Disaster Management Division) ‘C’Wing, 3rd Floor, NDCC-II, Jai Singh Road, New*. https://srcodisha.nic.in/dmrule/New%20Iitems%20and%20Norms%20of%20assistance%20from%20SDRF%20and%20NDRF%20dtd%2010%20Oct%202022%20(2)%20(1).pdf
35. *Press Release*. https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
36. *Submergence Stress Reduces the Ability of Rice to Regulate Recovery after Disaster*. https://www.mdpi.com/2073-4395/14/6/1319
37. *Wp Content*. https://www.osdma.org/wp-content/uploads/2026/04/20260413123924.pdf
38. *Wp Content*. https://www.osdma.org/wp-content/uploads/2026/03/606.pdf
39. *Gkms Sop*. https://mausam.imd.gov.in/imd_latest/contents/pdf/gkms_sop.pdf
40. *untitled*. https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
41. *Press Release*. https://internal.imd.gov.in/press_release/20210611_pr_1133.pdf
42. *nrsc*. https://www.osdma.org/wp-content/uploads/2019/09/Flood-Hazard-Atlas.pdf
43. *Ground Water - dowr.odisha.gov.in*. https://dowr.odisha.gov.in/sites/default/files/2026-01/Ground%20Water.pdf
