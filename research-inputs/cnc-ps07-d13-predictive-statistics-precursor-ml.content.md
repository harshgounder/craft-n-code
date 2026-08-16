# Edge Statistics for Odisha Cyclone-Flood Warnings

## 1. EXECUTIVE SUMMARY

- **[1] BOCPD is edge-feasible, but not a cyclone oracle:** Adams-MacKay Bayesian Online Changepoint Detection (BOCPD) maintains a posterior over run length, or time since the last change. Exact per-sample time and memory grow linearly with stream age; truncating low-probability run lengths reduces average cost toward the expected run length. The original paper tested well-log, financial, and coal-disaster series, not meteorological pressure or wind [4]. -> Run a pruned, univariate BOCPD on the phone for pressure tendency and river-level regime changes, but calibrate it on Odisha replay data and never let it supersede IMD or CWC.

- **[2] No defensible Bay-of-Bengal pressure-drop alarm in hPa/hour was found:** IMD reports PHAILIN at **940 hPa** with a **66 hPa total pressure fall**, but gives no duration for converting that figure into hPa/hour [34]. The 2024 AMPHAN surface study records Kolkata's minimum at **958.8 hPa** and a sharp fall/rise pattern, yet likewise publishes no hourly pressure-tendency threshold [32]. -> Demo a learned change score, not a fabricated `2 hPa/hour = cyclone` rule.

- **[3] Official and satellite information leads; local sensors confirm local impact:** For PHAILIN, IMD used hourly coastal observations, 30-minute satellite imagery, and 10-minute radar imagery, while structured forecasts extended to **120 hours** [34]. A model-based genesis parameter signaled PHAILIN **168 hours before formation**, but its validation included **0.38 false-alarm ratio**, so this is neither a local-sensor result nor a guaranteed lead time [15]. -> IMD alert state must be the primary cyclone trigger; pressure, wind, and rain nodes should localize severity and detect outages.

- **[4] Flood sensing is more locally actionable, but thresholds are basin-specific:** The IIT Roorkee Kedarnath study used the form `I = alpha * D^(-beta)` and simulated **10-90 mm/hour** rainfall; all tested intensities except 10 mm/hour produced debris flow in that calibrated Himalayan model [19]. It reported no false-alarm/miss evaluation and is not an Odisha-plains calibration [19]. -> Fit village-specific intensity-duration, antecedent wetness, and gauge-rise rules from local events instead of copying Himalayan constants.

- **[5] Cheap sensors can resolve useful trends but are not safety-certified:** Bosch specifies BME280 relative pressure accuracy of **+/-0.12 hPa**, filtered RMS noise of **0.2 Pa**, and typical all-sensor current of **3.6 microamps at 1 Hz**; Bosch also says the part is not fit for safety-critical systems [5]. A 2025 low-cost ultrasonic river device achieved **5.00 cm RMSE** and below **3% average error** in two months of field data, with a sensor price of roughly **$6-$15** [33]. -> Use redundancy, calibration, health checks, and official alerts.

- **[6] Streaming statistics outrank heavyweight ML on the phone:** EWMA is constant-state; pruned BOCPD is bounded; Online-iForest was reported competitive with online methods and more efficient than comparators, while the nonstationary Gaussian-process fault model requires accumulated covariance and Monte Carlo inference without published scale benchmarks [30] [21][22]. -> Put EWMA, rules, and compact change/anomaly models on the phone; reserve GP and particle-filter experiments for the server.

- **[7] The offline LLM should phrase approved advice, not decide hazards:** A 2026 edge benchmark reports model memory from **392-576 MB for 0.5B** models and **2,411-7,297 MB for 7B** models; sub-4-bit compression sharply degraded capability, and its test hardware was a 16 GB laptop, not a low-end Indian phone [24]. -> Make deterministic agronomy and hazard rules produce a structured advisory, then let an optional small model simplify or translate it, with canned Odia SMS/IVR as the guaranteed fallback.

- **[8] Decision:** **Prototype = GO; pilot = GATED.** The prototype can replay IMD/CWC data, synthesize node streams, show offline change detection, and deliver SMS/IVR. A pilot is gated by missing Odisha thresholds, a formal real-time data path, ruggedized sensor validation, plot-level inundation mapping, false-alarm governance, and evidence that low-literacy users understand and act on the advice. Google SRE guidance warns that single-machine signals are too noisy to be actionable and recommends persistence across at least two evaluation cycles to avoid false alerts [35].

**Executive decision:** The defensible innovation is not "a phone predicts cyclones before IMD." It is an offline-resilient advisory mesh that fuses authoritative warnings with calibrated local evidence and continues operating when data or connectivity fails.

## 2. DATA INVENTORY

**Grade key:** A = official primary source, manufacturer datasheet, or directly relevant primary evidence; B = peer-reviewed and useful but transferred across geography or hazard; C = adjacent method evidence, incomplete validation, or retail specification; D = unsupported for the proposed decision.

| Sub-question / item | Named source (URL + date) | Spec / price | Feasibility for India | Reliability |
|---|---|---|---|---|
| BOCPD theory and cost | Adams and MacKay, *Bayesian Online Changepoint Detection*, http://arxiv.org/pdf/0710.3742, 19 Oct 2007 | Exact update is O(t) time and memory at sample t; probability-tail truncation gives roughly constant average cost tied to expected run length [4]. Open paper; no license price. | High on phone for 1-10 streams after pruning, log-space arithmetic, and a cap on run-length hypotheses. | A for method; C for cyclone use |
| BOCPD on pressure/wind | Same paper plus targeted meteorology search | Original experiments are well-log mean, Dow Jones variance, and coal-mine intervals, not pressure/wind [4]. No validated meteorology implementation cost found. | Technically straightforward; operational threshold and false-alarm rate remain unvalidated. | D for claimed published cyclone use |
| Cyclone surface pressure | IMD, *PHAILIN Report*, https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads/report/26/26_38a1d4_phailin.pdf, Oct 2013 | 940 hPa central pressure; 66 hPa total fall; no hPa/hour denominator [34]. | Use as historical replay and feature engineering, not a universal threshold. | A |
| Local cyclone precursors | Bondyopadhyay and Jana, *Precursors of hazard due to super cyclone AMPHAN for Kolkata*, https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/6259/5706, 2024 | Kolkata minimum 958.8 hPa; pressure and hourly rain rose/fell around closest approach; proposed surface scheme intended as 12-24 hour guidance, with 3 km mean error for its distance-pressure scheme [32]. No humidity saturation or hPa/hour rule. | Useful secondary guidance after IMD has identified a cyclone; not independent genesis detection. | A for case; C for transfer to Odisha villages |
| Wind shifts / humidity saturation | Same AMPHAN and PHAILIN sources | Landfall wind for PHAILIN was 200-210 km/h with gusts to 220 km/h, but the sources did not publish a reusable pre-landfall wind-direction or humidity-saturation trigger [34][32]. | Measure wind and RH, but learn local conditional features rather than hard-code a literature threshold. | D for universal trigger |
| Satellite and NWP precursor | IMD cyclone-prediction verification, https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/558/484/1888, 2015 | PHAILIN formation/location indication at 168 h before formation; POD 0.94, FAR 0.38, CSI 0.60, ETS 0.02 [15]. | Server ingests IMD products; phone caches warning state. Not reproducible from plot sensors. | A |
| Satellite rainfall nowcast | MAUSAM Meteosat-8 CRR validation, https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/272/203/836, 2020 cyclone season | Product every 15 min at 3 x 3 km; very-short-range forecast to 90 min; validation against 0.1-degree, 30-min IMERG [17]. | Strong regional context when available; still too coarse to replace farm rain gauges. | B |
| Rainfall intensity-duration | IIT Roorkee et al., *Numerical model derived intensity-duration thresholds...*, https://nhess.copernicus.org/preprints/nhess-2022-297/nhess-2022-297.pdf, 2022 preprint | `I = alpha * D^(-beta)`; 10-90 mm/h simulations; dry initial moisture 0.05 m3/m3; calibrated debris-flow volume 2.56M m3 vs empirical 2.29M m3 [19]. | Method is feasible; constants are not transferable from Kedarnath to Odisha farms. | B method; D as Odisha threshold |
| CWC river data and rise rate | CWC National Water Data Portal, https://nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc, updated 9 Aug 2026 | Hourly station, geography, date, and water-level records; no public universal cm/hour trigger or validation/cost data on the page [31]. | Good server baseline and replay source. Phone should compute station-specific slope only after station mapping and missing-data checks. | A for data; D for universal rise threshold |
| Soil saturation / API | *Optimality of antecedent precipitation index...*, Journal of Hydrology, https://www.sciencedirect.com/science/article/pii/S0022169421000743, 2021 | Recursive API uses current rain plus a decayed prior API; the literature warns that decay constant k is often chosen arbitrarily, impairing comparison [29]. Open formula; no hardware price. | High compute feasibility; k and alert cutoffs must be fitted by soil, season, crop, and drainage class. | B |
| Pressure/RH sensor | Bosch BME280 datasheet, https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf, Feb 2024 | Pressure absolute accuracy +/-1 hPa, relative +/-0.12 hPa, 0.2 Pa filtered RMS noise; RH +/-3%; 3.6 microamps at 1 Hz for all three [5]. Manufacturer price not stated. | Excellent prototype node component in a ventilated enclosure; field calibration and backup needed. | A specs |
| Water-level sensor | Sadeghi et al., *A low-cost ultrasonic sensor...*, https://www.sciencedirect.com/science/article/pii/S0955598624002577, Mar 2025 | GY-US42 range 20-720 cm, 15 Hz response, about $6-$15; field RMSE 5 cm, average error under 3% [33]. | Feasible for drains/canals if mounted above debris and corrected for temperature; wind/noise and calibration are explicit risks [33]. | B |
| Indian prototype sonar | DNA Technology India, https://www.dnatechindia.com/jsn-sr04t-waterproof-ultrasonic-distance-sensor.html, accessed 2026 | JSN-SR04T listed at Rs. 658.44 including GST [6]; page evidence did not establish river accuracy. | Demo only until enclosure, condensation, blind-zone, cable, and flood-debris tests pass. | C |
| Kalman fusion | Jahja et al., *Kalman Filter, Sensor Fusion, and Constrained Regression*, https://www.stat.berkeley.edu/~ryantibs/papers/sensorfus.pdf, plus adjacent low-cost sensor studies | Linear state update is cheap for small state dimension; no directly relevant Odisha low-cost weather-station validation was found. | Use scalar Kalman filters for water level and pressure, or fuse redundant same-unit sensors. Do not fuse unlike variables merely because they share timestamps. | B theory; D local evidence |
| Particle filter | Targeted weather/flood search | No Indian cheap-station cyclone/flood field result with compute, accuracy, and failure data was recovered. Particle count makes cost proportional to particles times state transition/likelihood. | Server experiment for nonlinear river states; unnecessary on ESP nodes and probably decorative on the phone prototype. | D |
| EWMA | NIST, *EWMA control chart*, https://www.itl.nist.gov/div898/handbook/mpc/section2/mpc2211.htm, n.d. | `z_t = lambda*x_t + (1-lambda)*z_(t-1)`; constant memory and arithmetic [30]. | Very high. Use for baseline, residual and rate monitoring with persistence and hysteresis. | A method |
| Isolation Forest | Leveni et al., *Online Isolation Forest*, https://proceedings.mlr.press/v235/leveni24a.html, ICML 2024 | Explicitly streaming and reported to rival offline methods while outperforming competitors in efficiency; page did not expose phone RAM/runtime numbers [21]. | Phone/server candidate after fixed feature design; ordinary batch iForest should not be relabeled streaming. | A method; C device sizing |
| GP novelty / fault separation | Reece et al., *Anomaly Detection and Removal Using Non-Stationary Gaussian Processes*, https://www.robots.ox.ac.uk/~sjrob/Pubs/anomalyDetection_nonStat_GP_reece_etal.pdf, n.d. | Models target plus separate bias/drift process; online inference uses prior observations and Monte Carlo hyperparameter integration; no scale benchmark [22]. | Server analysis and sensor-fault research, not the minimum phone path. | B method; C hazard transfer |
| EVT return periods | Chakraborty et al., *Flood Frequency Analysis of River Mahanadi, India*, https://link.springer.com/article/10.1007/s40030-024-00805-5, 2024 | Compares Gumbel Max, GEV, LP3 and log-normal flood-frequency models at Mahanadi gauges [23]. Paper access/result detail was incomplete in the search corpus; no sensor price. | Good basin-prior method. A plot-depth prior still needs station linkage, DEM and hydraulic/inundation mapping. | B |
| Indian spatial interpolation | *Comparison of ordinary and Bayesian kriging... north-west India*, https://link.springer.com/article/10.1007/s12665-017-6814-3, 27 Jul 2017 | Peer-reviewed comparison of ordinary and Bayesian kriging for annual rainfall [28]; no Odisha village network validation. | Server only. Fit variogram by season and cross-validate by leaving out entire stations. | B method; C transfer |
| Cheap IoT field case | Choosumrong et al., *Development of an IoT-Based Flood Monitoring System...*, https://www.mdpi.com/1424-8220/25/17/5477, 2025 | Ten JSN-SR04T/ESP8266 stations in Bang Rakam, Thailand; approximately 35,000 THB per station; complete data through 6 Oct 2022 during the deployment [11]. | Strong architecture comparator, but not on-device ML and not India. | B |
| Quantized phone LLM | *A Systematic Evaluation of On-Device LLMs*, http://arxiv.org/html/2505.15030v5, Mar 2026 | 0.5B memory 392-576 MB; 7B 2.411-7.297 GB; CPU power 7.9-9.5 W in tests; q2 harmed quality [24]. | Optional on mid/high-end phone. Low-end and non-smartphone access must remain template SMS/IVR. | B benchmark; C target-device transfer |

### Case study: PHAILIN and AMPHAN separate official lead from local confirmation

PHAILIN shows the operational hierarchy. IMD combined satellites, radar, surface stations and models, issued structured forecasts to 120 hours, and achieved landfall-point errors of 3-13 km and time errors of 1-3 hours for 12-72 hour forecasts [34]. A plot sensor cannot reproduce that basin-scale observing system. It can, however, tell a farmer that this village is already seeing rapidly falling pressure, damaging gusts, rain accumulation, or node failure.

AMPHAN provides the closest paper to the requested local precursor concept. Its authors found pressure fall, rainfall rise and gust behavior useful for 12-24 hour guidance, but explicitly kept NWP, satellite and radar in the final operational loop [32]. The correct prototype story is therefore "official warning plus local escalation," not "edge sensors discover a cyclone first."

### Case study: Kedarnath thresholds cannot be copied to coastal Odisha

The IIT Roorkee work demonstrates a legitimate method: calibrate a hydrologic/debris-flow model, sweep rainfall intensity, fit an I-D boundary, and test initial moisture. It also demonstrates why a visually impressive threshold is dangerous when moved across terrain. The calibration concerns steep Himalayan debris flow, sets a dry initial water content, and reports no event-level false-alarm rate [19].

For coastal Odisha, drainage congestion, river backwater, storm surge, embankments, paddy geometry and soil class change the response. The reusable asset is the workflow, not its alpha or beta. A pilot needs local event labels and should publish precision, recall, missed severe events, median lead time and alert burden per village.

## 3. COVERAGE TABLE

| Source family | Useful hits retained | Noise / missing | Coverage judgment |
|---|---:|---|---|
| IMD/RSMC official cyclone reports and MAUSAM papers | 6 | Strong event chronology, central pressure, wind, rainfall and forecast verification; no reusable Bay-of-Bengal hPa/hour or humidity-saturation alarm. | A for official cyclone context; C for local thresholds |
| CWC/NWDP official hydrology | 4 | Hourly level dataset and forecast portals exist; public page does not document a universal rise-rate trigger, farm mapping, API service level or all failure codes [31]. | A data; C integration |
| Peer-reviewed flood threshold/API | 4 | Strong formulations; India examples are Himalayan or generic, with no Odisha flood-event confusion matrix. | B |
| Manufacturer and validated cheap sensors | 4 | Bosch specifications and one two-month river validation are useful; retail modules lack safety certification and long monsoon/cyclone survivability data [5][33]. | B |
| Streaming statistics and anomaly methods | 7 | BOCPD, EWMA, iForest and GP are real methods; meteorology-specific BOCPD and target-phone benchmarks are missing. | A method; C application |
| EVT and Indian spatial statistics | 5 | Mahanadi flood frequency and Indian kriging establish applicability; plot-level depth, nonstationarity and Odisha cross-validation remain absent. | B |
| Global South low-cost IoT deployments | 3 | Thailand field case is substantive; many other hits were prototypes, vendor pages or architecture claims without lead time/failure data. | B-/C |
| Android/on-device LLM evidence | 4 | Resource trade-offs are measured, but benchmarks use laptop/server-class hardware and general tasks, not low-end Odisha phones or Odia advisory safety [24]. | B benchmark; C product fit |
| SMS/IVR and low-literacy delivery | 0 in this predictive-statistics run | The problem statement requires it, but no Odisha user study, language comprehension result, delivery rate, IVR cost or consent evidence was part of the recovered corpus. | D |

The coverage is enough to build a transparent replay prototype. It is not enough to claim calibrated early-warning performance in an Odisha village. The strongest sources support a layered design; the weakest area is not algorithm availability but local labels, operational integration and human-response evidence.

## 4. WHAT IS MISSING

1. **A pressure-drop rate label:** No recovered primary source supplies a transferable pre-landfall surface-pressure threshold in **hPa/hour** for Odisha. PHAILIN's 66 hPa is a total central pressure fall, and AMPHAN publishes a sharp local trend but no hourly alarm rate [34][32].

2. **Wind and humidity precursor thresholds:** No source provides a validated sequence such as a wind-direction rotation plus RH saturation that predicts damaging conditions with known lead time, false alarms and misses at Odisha farm stations.

3. **Local-versus-satellite lead-time benchmark:** The corpus contains official/satellite lead and a 12-24 hour AMPHAN surface guidance claim, but no same-event experiment comparing a cheap village node, satellite/NWP and ground truth at identical timestamps [32].

4. **Odisha flood labels:** There is no public table joining minute/hour rain, upstream level, soil moisture, embankment/reservoir operations, plot inundation depth, crop damage and action timestamps across enough events to fit village thresholds.

5. **A universal CWC rate-of-rise rule:** The official dataset is hourly; the public evidence does not state that `X cm/hour` means warning across all rivers [31]. Warning and danger levels are station-specific, and any slope threshold must also be station-specific.

6. **A calibrated API/soil model:** API is cheap to compute, but k, depth, sensor placement and saturation cutoff are uncalibrated for Odisha's soil, crop and drainage classes. The literature itself flags arbitrary k selection as a comparability problem [29].

7. **Direct low-cost fusion evidence:** No recovered paper field-tests BME280 plus cheap anemometer plus rain gauge plus water-level sensor under an Indian cyclone and reports raw-versus-Kalman/particle accuracy, power, packet loss and warning skill.

8. **Plot-level EVT depth prior:** Station return levels do not answer "this plot floods to X every N years." That requires geocoded event depths, DEM, drainage/river hydraulics, bias correction, land-use change and uncertainty propagation. National extreme-rainfall return levels also show spatial and temporal shifts, making stationarity a risk [8].

9. **An Indian on-device hazard-ML field case:** The Thailand case proves low-cost connected sensing, not an offline phone LLM or local continuous learning. No recovered India/Global South source combines cheap cyclone/flood sensors, on-device streaming ML, offline advisory generation, SMS/IVR and controlled field outcomes.

10. **Human factors and operations:** Missing evidence includes Odia dialect/voice intelligibility, low-literacy comprehension, opt-in and privacy, advisory liability, delivery receipts, acknowledgment/escalation, battery replacement, calibration visits, theft, salt corrosion, tower outage and disaster-time API capacity.

These are not invitation-to-invent gaps. They are the pilot's data-acquisition and governance backlog.

## 5. HOW IT FEEDS THE EDGE-AI ENGINE

| Tier | Inputs and methods | Decision powered | Guardrail / fallback |
|---|---|---|---|
| **Sensor node** | BME280 pressure/RH/temperature; tipping-bucket rain; anemometer; canal/drain ultrasound; optional soil moisture. Apply range checks, timestamp/sequence validation, median despiking, EWMA, battery/RSSI health and short local buffering. | "Is this reading plausible?" "Is the local environment changing fast?" "Is the node failing?" | Never issue a cyclone warning from one node. Require persistence, redundant evidence or official warning. Bosch disclaims safety-critical use [5]. |
| **Phone hub** | Cached IMD/CWC warning state, farm profile, recent node windows, pruned BOCPD, scalar Kalman filters, API, rate features and compact Online-iForest. | Escalate an official alert by plot vulnerability; detect local water/rain escalation; choose a pre-approved crop action and urgency. | Deterministic risk policy produces structured fields. LLM cannot change severity, timing, pesticide dose or evacuation instruction. |
| **Phone language layer** | A small quantized model, if the device passes RAM/thermal tests; otherwise templates. | Convert a structured advisory into short Odia text and a simple IVR script; answer only from cached approved content. | Grammar-constrained output, banned free-form agronomy, checksum/version, and canned SMS/IVR fallback. The edge benchmark shows steep memory and quality trade-offs [24]. |
| **Learning server** | Historical IMD/CWC, node telemetry, intervention/outcome labels, DEM/soil/crop layers. Fit local thresholds, hazard-conditioned BOCPD priors, iForest features, kriging/GP maps and GEV/GPD return levels. | Produce versioned parameters and model bundles by village/season; estimate uncertainty; identify dead sensors and coverage holes. | Offline cross-validation by event and by held-out station, not random rows. Champion/challenger deployment, rollback and signed packages. |
| **Monitoring/governance server** | Alert counts, false alarms, misses, delivery/acknowledgment, data drift and model versions. Use MMD or classifier drift only as retraining signals, not hazard alarms. | Decide whether to retrain, pause or roll back. MMD is a two-sample discrepancy with quadratic computation and linear approximations [36]. | Multiple parallel tests need false-discovery control; FDR seeks more discoveries while limiting the expected false-positive proportion [37]. Human approval before promotion. |
| **SMS/IVR gateway** | Final structured advisory, language, phone capability, retry state. | Deliver concise action, deadline, reason and acknowledgment path to non-smartphone and low-literacy users. | Duplicate suppression, retry/backoff, voice replay, DTMF acknowledgment, and escalation to village contact. No reliance on app push. |

### The decision pipeline

1. **Official trigger:** Parse and cache IMD/CWC state with issue time, valid window, geography, severity and source ID. IMD's public site documents dissemination through web, email, SMS and social channels, but product-level access and service guarantees still need an agreement [3].
2. **Local quality gate:** Reject impossible jumps, stale timestamps and low battery. Compare neighboring nodes and redundant channels.
3. **Feature update:** Compute 5/15/60-minute rain, pressure slope, gauge slope, EWMA residual, API, persistence and official-alert interaction. Do not expose a naked p-value as severity.
4. **State inference:** BOCPD answers "did the local regime change?" Kalman answers "what is the smoothed state?" iForest answers "is this feature vector unusual?" These are different questions and should not be blended into one opaque score.
5. **Policy:** A small audited rules table maps official severity, local evidence, crop stage, elevation/drainage and farmer profile to an action. Confidence controls wording and escalation, not fabricated precision.
6. **Delivery and learning:** Send SMS/IVR, log acknowledgment, and later collect observed depth/damage/action. Server updates are trained centrally, validated, signed, and rolled out gradually; the phone may adapt baselines locally, but it should not fine-tune safety policy unsupervised.

This tiering preserves offline resilience without confusing language generation with hazard inference.

## 6. REAL-vs-FILLER

| Claim or component | Evidence verdict | Why |
|---|---|---|
| IMD alert + hyperlocal profile + local escalation | **REAL** | It directly matches the problem statement and the evidence hierarchy. PHAILIN forecasting combined official multi-source observations and achieved measured landfall skill [34]. |
| BME280 trend sensing | **REAL, with redundancy** | Relative accuracy and noise are adequate to resolve multi-hPa trends, but the manufacturer excludes safety-critical use [5]. |
| Local water-level monitoring | **REAL** | A low-cost ultrasonic design was field-tested for two months with 5 cm RMSE; wind/noise and calibration remain real limitations [33]. |
| EWMA + persistence + hysteresis | **REAL and minimum viable** | Constant memory, explainable, testable, and aligned with operational alert persistence. |
| Pruned BOCPD | **REAL as a feature** | The posterior and complexity are published; cyclone pressure/wind performance is not [4]. Show run-length probability, not a magical cyclone label. |
| Scalar Kalman filter | **REAL for denoising** | Appropriate for a defined state and sensor model. It is filler if used as an unexplained "AI fusion" badge without calibration and residual checks. |
| Online-iForest | **REAL but secondary** | A true streaming version exists and has comparative efficiency evidence [21]. It needs fixed features, a bounded window and local evaluation. |
| GP novelty / particle filter on phone | **MOSTLY FILLER for this prototype** | GP fault separation is scientifically real, but the recovered implementation uses Monte Carlo inference and gives no scale benchmark [22]. Particle filtering adds cost without a validated local nonlinear state model. |
| Kriging map between villages | **REAL on server, conditional** | India has peer-reviewed ordinary/Bayesian kriging work [28]; a sparse network must still pass spatial holdout validation and uncertainty coverage. |
| "Every plot has an N-year flood depth" | **FILLER until hydraulically mapped** | EVT at a gauge estimates a return level at that gauge. Plot depth requires terrain, drainage and inundation translation, plus nonstationarity handling. |
| Small quantized LLM decides warnings | **FILLER and unsafe** | Resource constraints and quantization losses are measured; general benchmark accuracy is not hazard calibration [24]. |
| Small quantized LLM rewrites approved advice | **USABLE OPTIONAL LAYER** | It can simplify/translate structured content on capable phones, but deterministic templates must cover all users and outages. |
| Continuous local self-training | **FILLER if uncontrolled** | A phone may update baselines, but unsupervised policy or language-model fine-tuning can silently change safety behavior. Central validation, versioning and rollback are required. |
| "Village nodes detect a cyclone before satellite" | **CONTRADICTED BY THE EVIDENCE BASE** | Official PHAILIN monitoring had satellites every 30 minutes, radar every 10 minutes and forecasts to 120 hours; local AMPHAN surface guidance was framed for 12-24 hours and as a complement [34][32]. |

### Case study: Thailand proves sensing, not the marketing stack

The Bang Rakam study deployed ten ESP8266/ultrasonic stations rather than stopping at a breadboard. It therefore supports the proposition that a low-cost network can collect meaningful flood dynamics in a Global South setting. Each station cost about 35,000 THB, which is not the price of a bare Rs. 658 sensor; enclosure, power, communications and installation dominate a field station [11].

It does not prove the full proposed stack. It is not an Odisha cyclone trial, does not validate a phone LLM, and does not establish SMS/IVR behavior change. The honest prototype should cite it for field sensing architecture and then state the remaining integration work.

## 7. NOISE LOG

| Searched/discarded family | Examples | Why discarded or downgraded |
|---|---|---|
| SEO/vendor "AI flood" pages | Zbotic India guide; Aware Monitoring; 2026 market reports | No peer-reviewed field protocol, confusion matrix, lead-time distribution or failure log. Useful only for component discovery, not performance claims. |
| ResearchGate-only records | Bay of Bengal parametric cyclone and wave copies | Discovery pointers only when a publisher/official copy was unavailable; not used for core claims. |
| Mis-targeted MAUSAM PDFs | Atlantic seasonal storm-frequency paper | Search matched "cyclone" but the paper analyzed Atlantic annual indices and gave no local pressure/wind/humidity/landfall precursor [14]. |
| Model skill presented as sensor precursor | IMD GPP 168-hour result | Retained only with qualification: it is a model-based formation indicator with FAR 0.38, not evidence that a BME280 node sees a cyclone seven days early [15]. |
| Himalayan I-D threshold copied to Odisha | Kedarnath debris-flow paper | Retained for method, rejected as an Odisha constant because geology, slope and validation target differ [19]. |
| Non-Indian kriging hits | Simineh River, Iran; Pakistan regression-kriging | Good methods but lower relevance than the Indian ordinary/Bayesian kriging comparator; not used to claim Odisha accuracy. |
| Adjacent Kalman studies | Low-cost gas sensor and water-quality assimilation | Demonstrate filtering, not cyclone/flood warning from cheap weather stations. Downgraded rather than generalized. |
| Batch Isolation Forest relabeled online | Sliding-window iForest articles | A windowed retrain can be a valid baseline, but it is not inherently streaming. The report uses the explicit Online-iForest source instead [21]. |
| Consumer on-device LLM hype | Generic Android and vendor demos | No low-end Odisha phone, Odia safety, thermal, battery or offline-IVR benchmark. The report uses measured resource data and limits the LLM role. |
| Search metadata mismatch | Amphan PDF initially carried an unrelated ozone title | The PDF body, DOI and article text were checked; the source was retained based on its actual MAUSAM content [32]. |

The noise pattern is itself informative: hardware demos are abundant, but calibrated warning skill, failure behavior and human outcomes are scarce.

## 8. VERDICT

| Decision level | Verdict | What may be claimed | Exit criteria |
|---|---|---|---|
| **Hackathon prototype** | **GO** | "We integrate IMD/CWC state, replay historical events, detect local regime changes offline, personalize pre/post-disaster advice, and deliver SMS/IVR." | Demonstrate deterministic end-to-end replay, offline cache, sensor fault injection, explainable alert trace, Odia template, IVR call, and rollback. |
| **Limited technical field test** | **PARTIAL** | "We are measuring reliability and collecting local labels; alerts are shadow-mode or supervised." | 8-12 weeks plus at least one monsoon season is preferable; quantify uptime, calibration drift, packet loss, battery life, water-level error, alert burden and delivery rate. No autonomous life-safety claim. |
| **Farmer-facing operational pilot** | **GATED** | No claim of independent cyclone prediction or validated crop-loss reduction yet. | IMD/CWC data agreement; district approval; local threshold validation across events; ruggedization; plot mapping; agronomy sign-off; privacy/consent; SMS/IVR usability; incident response; audit and liability plan. |

### Prototype acceptance tests

1. Replaying PHAILIN/AMPHAN and synthetic sensor data produces the same alert trace twice, including source, timestamp, feature values, rule version and advisory version.
2. A lone pressure spike, missing rain packet and stuck-high water sensor do not trigger a hazard alert. Persistent corroborated change does.
3. Disconnecting the internet leaves the phone able to evaluate cached rules and generate a pre-approved SMS/IVR message.
4. The LLM is removed or forced to emit nonsense; the deterministic advisory and canned Odia fallback still work.
5. A high official alert with silent/broken local nodes still reaches farmers; missing local data lowers confidence but does not suppress IMD.
6. A local flood escalation can trigger from calibrated rain/water evidence even before a coarse official river update, but it is labeled "local sensor warning" and sent through a supervised policy.
7. Multiple-feature alerts are controlled for persistence and alert burden. FDR can be used in server analysis when testing many features, but not as a substitute for event-level validation [37].

### Synthesis

Across mechanism, scope, evidence and time horizon, the methods are complementary rather than interchangeable. **IMD satellite/NWP** has regional scope and days-scale potential but nonzero false alarms; **local sensors** have plot/village scope and minutes-to-hours responsiveness but only after the hazard is nearby; **CWC gauges** provide authoritative river context at hourly cadence; **EWMA/Kalman** suppress noise; **BOCPD/iForest** detect regime or multivariate novelty; **EVT/kriging** build long-horizon priors and spatial context; and the **LLM** only communicates an already-made decision.

The central tension is between sophistication and evidence. BOCPD, GP novelty, particle filters and quantized LLMs can make a demo look advanced, while the pilot's dominant risks are calibration, sensor survival, official-data continuity, false alarms and comprehension. The winning architecture therefore spends edge compute on quality control and transparent change features, spends server compute on cross-validated spatial/extreme models, and spends product effort on SMS/IVR reliability.

**Final recommendation:** build the prototype now, describe it as an **advisory and local-confirmation mesh**, and publish the six pilot gates on the demo screen. Do not advertise a numeric hPa/hour cyclone threshold, independent cyclone discovery, plot-level N-year flood depth, or continuously self-improving safety model until those claims have local data and controlled validation.

## References

1. *Flood Forecasting/ Hydrological Observation | Central Water ...*. https://cwc.gov.in/flood-forecasting-hydrological-observation
2. *Adaptive Dynamic Thresholds for Unsupervised Joint Anomaly ...*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12788306
3. *IMD APIs | India Meteorological Department*. https://mausam.imd.gov.in/responsive/apis.php
4. *Bayesian Online Changepoint Detection - arXiv.org*. http://arxiv.org/pdf/0710.3742
5. *BME280 Datasheet*. https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
6. *JSN-SR04T Waterproof Ultrasonic Distance Sensor*. https://www.dnatechindia.com/jsn-sr04t-waterproof-ultrasonic-distance-sensor.html
7. *Flood Forecasting/ Hydrological Observation*. https://www.cwc.gov.in/en/flood-forecasting-hydrological-observation
8. *Spatio‐Temporal Changes in Extreme Rainfall Events Over ...*. https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021EA001930
9. *APIs - National Water Data Portal - nwdp.nwic.gov.in*. https://nwdp.nwic.gov.in/dataset_api/home_api_page
10. *Comparison of Spatial Interpolation Methods for Mapping ...*. https://link.springer.com/chapter/10.1007/978-3-319-18663-4_27
11. *Development of an IoT-Based Flood Monitoring System ... - MDPI*. https://www.mdpi.com/1424-8220/25/17/5477
12. [
		CYCLONE
							| MAUSAM
			](https://mausamjournal.imd.gov.in/index.php/MAUSAM/catalog/category/CYCLONE)
13. [
		Study of the impact of high resolution ROMS-SST on the simulation of two intense tropical cyclones over Bay of Bengal using ARW modeling system
							| MAUSAM
			](https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/view/5766)
14. *mausamjournal.imd.gov.in*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/499/432/1745
15. *mausamjournal.imd.gov.in*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/558/484/1888
16. *mausamjournal.imd.gov.in*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/770/658/2740
17. *mausamjournal.imd.gov.in*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/137/105
18. *mausamjournal.imd.gov.in*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/1548/1360/5806
19. *Numerical model derived intensity-duration thresholds for early warning of rainfall-induced debris flows in the Himalayas*. https://nhess.copernicus.org/preprints/nhess-2022-297/nhess-2022-297.pdf
20. *mausamjournal.imd.gov.in*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/272/203/836
21. *Online Isolation Forest*. https://proceedings.mlr.press/v235/leveni24a.html
22. *Anomalydetection Nonstat Gp Reece Etal*. https://www.robots.ox.ac.uk/~sjrob/Pubs/anomalyDetection_nonStat_GP_reece_etal.pdf
23. *Flood Frequency Analysis of River Mahanadi, India | Journal of The Institution of Engineers (India): Series A | Springer Nature Link*. https://link.springer.com/article/10.1007/s40030-024-00805-5
24. *A Systematic Evaluation of On-Device LLMs: Quantization, Performance, and Resources*. http://arxiv.org/html/2505.15030v5
25. *A Kalman Filter Scheme for the Optimization of Low-Cost Gas Sensor Measurements*. https://www.mdpi.com/2079-9292/13/1/25
26. *LLM Inference guide for Android  |  Google AI Edge  |  Google AI for Developers*. https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/android
27. *Gemini Nano  |  AI  |  Android Developers*. https://developer.android.com/ai/gemini-nano
28. *Comparison of ordinary and Bayesian kriging techniques in depicting rainfall variability in arid and semi-arid regions of north-west India | Environmental Earth Sciences | Springer Nature Link*. https://link.springer.com/article/10.1007/s12665-017-6814-3
29. *Optimality of antecedent precipitation index and its application - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0022169421000743
30. *2.2.2.1.1. EWMA control chart*. https://www.itl.nist.gov/div898/handbook/mpc/section2/mpc2211.htm
31. *River Water Level (Telemetry - Hourly), Central Water Commission (CWC) - Dataset - National Water Data Portal*. https://nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc
32. *Measurement of Total Ozone, D-UV Radiation, Sulphur dioxide and Nitrogen dioxide with Brewer Spectrophotometer at Maitri Antarctica during 2000*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/6259/5706
33. *A low-cost ultrasonic sensor for online monitoring of water levels in rivers and channels - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0955598624002577
34. *PHAILIN Report(Final) 30*. https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads%2Freport%2F26%2F26_38a1d4_phailin.pdf
35. *http://sre.google/sre-book/practical-alerting*. http://sre.google/sre-book/practical-alerting
36. *http://jmlr.org/beta/papers/v13/gretton12a.html*. http://jmlr.org/beta/papers/v13/gretton12a.html
37. *http://publichealth.columbia.edu/research/population-health-methods/false-discovery-rate*. http://publichealth.columbia.edu/research/population-health-methods/false-discovery-rate
