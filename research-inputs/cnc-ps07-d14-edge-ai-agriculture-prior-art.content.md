# Odisha Edge-AI Agriculture: Prior Art, Gaps, and Go Gates

## 1. EXECUTIVE SUMMARY

- **No Verified Full Loop**: In the public material reviewed, no system combines farm sensors -> an offline phone-resident agriculture LLM -> Odia SMS/IVR advice -> outcome capture -> controlled daily adapter updates. The closest systems each cover only part of the chain: FarmBeats covers sensor-to-edge infrastructure, Nuru proves offline phone inference, FarmerChat provides conversational farm advice, and OSDMA provides resilient warning dissemination [31][32][25][30]. -> Treat the white space as a defensible integration claim, not as proof that every component is production-ready.

- **Odisha Already Has A Strong Warning Backbone**: OSDMA's EWDS operates across six coastal districts with 122 siren locations, GPRS/VHF triggering, satellite fallback, solar power, and 72-hour RTU battery standby [30]. -> Integrate with this backbone and IMD rather than presenting the prototype as a replacement emergency-warning network.

- **Real Edge-AI Exists, But Not Yet As An Agriculture LLM Loop**: PlantVillage Nuru performs diagnosis and management advice offline on Android phones with at least 2 GB RAM. In a Tanzania field study, six-leaf accuracy was 74-88%, but overall in-field accuracy was only 58.3% across 300 leaves [32]. -> Use Nuru as proof that bounded on-device agricultural inference is feasible and as a warning that promotional accuracy can fall sharply under field conditions.

- **Commercial Agritech Is Mostly Cloud-Backed Or Architecturally Undisclosed**: AgroStar explicitly hosts production and crop-advice services on Google Cloud; Plantix exposes disease analysis as an API; Fasal verifies sensors and automation but does not disclose where inference runs [33][8][7]. None of Cropin, Plantix, Fasal, DeHaat, Gramophone, AgroStar, or AquaConnect provides reviewed first-party evidence of a farmer-phone LLM running offline. -> Do not label an app, IoT station, or AI service as "edge AI" without a local model artifact and a disconnected-device test.

- **The Phone Hub Is Technically Plausible, But Odia Is Gated**: Gemma 3n's E2B and E4B variants have 5B and 8B raw parameters but memory footprints comparable to 2B and 4B models, with stated minimums of 2 GB and 3 GB [23]. AI4Bharat offers ASR across all 22 official Indian languages, but the reviewed source does not establish an offline Android Odia benchmark [36]. -> Prototype on a 2 GB to 4 GB Android device, but make Odia ASR, TTS, latency, thermals, and intelligibility explicit pilot tests.

- **Feature-Phone Access Requires A Separate Delivery Plane**: mKisan demonstrates preference-based text and voice advisory access without internet, while FarmerChat accepts voice, text, and photos [20][25]. An offline Android hub alone cannot reach a non-smartphone user when telecom service is down. -> Separate local inference from outbound delivery, using SMS/IVR when cellular service exists and OSDMA siren/community escalation when it does not.

- **Weather Density Is Not Yet Auditable**: Odisha's announced direction is an AWS at block level and an ARG in every gram panchayat; the state has 6,794 gram panchayats [29][38]. However, the reviewed public sources do not provide a current operational Odisha station count, uptime, calibration record, or open station feed. -> A pilot needs its own calibrated local sensors and a formal IMD/data-provider integration, not an assumption that public stations already provide farm-scale coverage.

- **Prototype GO, Pilot GATED**: A prototype can demonstrate disconnected sensing, cached IMD input, deterministic hazard rules, Odia rendering, queued outcomes, and a signed adapter update. A live pilot remains gated by alert-feed access, agronomic approval, Odia field testing, sensor calibration, telecom failover, data governance, and rollbackable model releases. The Odisha Crop Contingency Plan supplies an official knowledge base, but it is district/block planning material rather than an executable AI policy [37].

**Grade key used below:** **A** = official operational document, government source, or strong primary research with measurable evidence; **B** = first-party product source or substantial research with material limitations; **C** = partial marketing, secondary reporting, or a proposal without field validation; **D** = unverified, unauditable, or no useful public evidence found.

## 2. DATA INVENTORY

### 2.1 Named agritech: none of the seven proves phone-resident inference

| Item | Named source, URL, and date | Spec and public price | Feasibility for India and edge classification | Grade |
|---|---|---|---|---|
| **Cropin** | Cropin official site, https://www.cropin.com/, accessed 2026-08-16 | The reviewed page describes real-time GenAI in a Walmart supply-chain use case. Mobile offline mode, local model, public price, and hardware specification are not disclosed [14]. | Strong enterprise/cloud candidate for data and forecasting partnerships; **not verified on-device**. The public evidence is enterprise-oriented rather than a low-cost farmer-phone product. | B |
| **Plantix by PEAT** | Plantix, https://plantix.net/en, and API toolkit, https://plantix.net/en/plantix-intelligence/api-toolkit, accessed 2026-08-16 | Consumer crop diagnosis is advertised as free. The API covers 69 crops and 19 languages; API price, inference location, and consumer offline operation are not disclosed [12][8]. | Useful disease-diagnosis prior art. The API is a network service; the reviewed first-party material does **not** verify offline phone inference. | B |
| **Fasal** | Fasal official site, https://www.fasal.co/, and FAO STI profile, https://sti-portal.fao.org/innovations/fasal, accessed 2026-08-16 | Soil-moisture and temperature sensors, weather stations, irrigation automation, and fertigation automation are stated. Public hardware/subscription price and inference location are not [7][34]. | Highly relevant commercial sensor-and-advisory comparator, especially for horticulture. Classify as **sensor edge collection plus undisclosed analytics**, not verified phone edge AI. | B |
| **DeHaat** | DeHaat farmer helpline, https://agrevolution.in/advisory-farmers-helpline-and-support, accessed 2026-08-16 | Toll-free 1800 1036 110 provides free agricultural guidance. Hours, languages, sensor integration, and AI architecture are not stated [10]. | Strong human-service and last-mile pattern; no reviewed evidence of sensors or on-device models. | B |
| **Gramophone** | Google Play listing, https://play.google.com/store/apps/details?id=agstack.gramophone, accessed 2026-08-16 | The app lists Hindi, English, and Marathi. Public advisory price, offline behavior, sensors, and on-device inference are not stated [40]. | Relevant app and commerce comparator, but Odia and edge inference are unverified. | B |
| **AgroStar** | AgroStar, https://corporate.agrostar.in/, and Google Cloud case study, https://cloud.google.com/customers/agrostar, accessed 2026-08-16 | Advisory, inputs, and expert guidance are offered; public price is not stated. GKE, Compute Engine, Pub/Sub, Dataflow, Kafka, and BigQuery run the backend and crop-advice workflow [42][33]. | **Cloud-backed architecture is verified**. This is useful service-delivery prior art, not evidence of disconnected farmer-phone inference. | A |
| **AquaConnect** | AquaConnect, https://aquaconnect.blue/, accessed 2026-08-16 | The company states that it uses AI and satellite remote sensing for transparency and market linkages. Sensors, FarmMOJO architecture, offline mode, local inference, scale, and public price are not disclosed in the reviewed page [41]. | Relevant to Indian aquaculture and remote sensing, but weakly aligned with Odisha crop cyclone/flood advice. | C |

**Decision-ready insight:** The named market is not empty, but the edge claim is. Fasal is closest on sensors, AgroStar is clearest on cloud architecture, and Plantix is closest on image diagnosis. None establishes the requested phone-resident agriculture LLM.

### 2.2 Agriculture LLMs and the on-device language stack

| Item | Named source, URL, and date | Spec and price | India/Odisha feasibility | Grade |
|---|---|---|---|---|
| **AgriLLM** | CGIAR, https://www.cgiar.org/news-events/news/agrillm-how-cgiar-is-developing-an-ai-powered-agricultural-advisory-service-for-global-south, accessed 2026-08-16 | CGIAR and AI71 initiated an agriculture-tailored LLM advisory platform. Public phone runtime, model size, offline mode, language list, field outcomes, and price are absent from the reviewed evidence [15]. | Strong domain-LLM reference, but not deployable evidence for an Odisha offline prototype. | B |
| **KissanAI / Dhenu** | KissanAI, https://kissan.ai/, and Microsoft profile, https://www.microsoft.com/en-in/aifirstmovers/kissanai, accessed 2026-08-16 | KissanAI is described as multilingual, personalized, and voice-based. Dhenu model details, offline/on-device operation, scale, and price are not stated [39][3]. | Relevant interaction design; edge status remains unknown. | B |
| **Krishi Sathi** | BharatGen, https://bharatgen.com/products/krishi-sathi, accessed 2026-08-16 | Real-time AI insights are stated for Hindi and English. Model, field evidence, hosting, offline operation, and price are not disclosed [13]. | Relevant Indian farm assistant, but it does not meet the Odia or verified-offline requirement in reviewed material. | B |
| **FarmerChat** | Digital Green, http://digitalgreen.org/farmerchat and https://www.farmerchat.io/, accessed 2026-08-16 | Voice, text, and photo inputs; advice shaped by crops, local conditions, and knowledge. It reports more than 830,000 users and 5M queries across Kenya, Nigeria, Ethiopia, India, and Brazil. Public price, sensors, offline mode, and on-device inference are not stated [25][27]. | Closest conversational advisory comparator and strong UX prior art. It remains a networked advisory service in the available evidence. | B |
| **Gemma 3n** | Google Developers, https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide, accessed 2026-08-16 | E2B/E4B have 5B/8B raw parameters with 2 GB/3 GB stated memory footprints [23]. Open-model price is not the main cost; handset RAM, storage, battery, and integration are. | Plausible phone-hub base model. Odia quality and low-cost Android performance must be benchmarked rather than assumed. | A |
| **AI4Bharat IndicConformer** | AI4Bharat, https://ai4bharat.iitm.ac.in/areas/model/ASR/IndicConformer, accessed 2026-08-16 | Open-source ASR suite covering all 22 official Indian languages. The reviewed source does not provide model size, Android runtime, Odia-specific WER, or offline handset results [36]. | Promising Odia speech component, but not yet proof of a complete offline IVR stack. | B |
| **PlantVillage Nuru** | CGIAR overview and field study, http://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai and https://www.biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf, 2020 | Offline Android diagnosis and management advice; at least 2 GB RAM; cited compatible-phone cost about USD 100-150. Six-leaf accuracy 74-88%, but overall in-field accuracy 58.3% [32]. | Best proof that offline agricultural inference can work on commodity phones. It is bounded vision AI, not an LLM, cyclone system, sensor mesh, or Odia service. | B |

#### Case study: Nuru exposes both feasibility and field-risk

Nuru makes the strongest evidence-based case for the phone tier. It runs after installation without internet, provides diagnosis and management advice, and was tested in cassava fields in coastal Tanzania. With six leaves, its performance was similar to trained researchers and better than extension agents and farmers [32]. This is materially stronger evidence than an app-store claim or a laboratory accuracy number.

The same study also exposes the danger of using a headline metric. Across 300 in-field leaves, overall accuracy was 58.3%; co-infections, latent symptoms, and fewer leaves reduced reliability [32]. The design implication is that the CNC prototype should keep hazard classification and agronomic action selection deterministic and auditable. The LLM should translate and explain approved actions, not invent them.

### 2.3 IoT weather and environmental coverage in Odisha

| Item | Named source, URL, and date | Spec/coverage | India feasibility | Grade |
|---|---|---|---|---|
| **IMD public API** | IMD API Reference, https://api.imd.gov.in/public/api_reference.html, accessed 2026-08-16 | A seven-day city forecast endpoint is documented. The reviewed reference does not establish a district-warning endpoint, CAP feed, open AWS/ARG feed, authentication rules, or update cadence [35]. | Usable for a prototype city-forecast connector. A pilot needs a formal path for district warnings and cyclone products. | A for documented endpoint; C for complete pilot feed |
| **IMD AWS/ARG portal** | http://aws.imd.gov.in:8091/, accessed 2026-08-16 | The public search result exposes a login portal, not an auditable station inventory or open feed. | Do not build a pilot dependency on assumed access. | C |
| **Odisha planned state network** | OrissaPOST/New Indian Express coverage of state direction, https://www.orissapost.com/automatic-weather-stations-in-blocks-soon/ and https://www.newindianexpress.com/states/odisha/2026/Jul/03/odisha-districts-asked-to-identify-land-for-setting-up-aws-and-rain-gauges, July 2026 | Announced target: AWS at block level and ARG in every gram panchayat [29][6]. Odisha officially lists 6,794 gram panchayats [38]. Current operational count, uptime, calibration, and API access remain unreported in these sources. | Potentially transformative future coverage, but it is a deployment plan rather than present pilot infrastructure. | B for plan; D for current density |
| **Weather Underground** | https://www.wunderground.com/history/daily/VEBS, accessed 2026-08-16 | Search exposed Bhubaneswar history/forecast pages, not a reproducible count of personal weather stations across Odisha. | Decorative unless station IDs, ownership, uptime, calibration, and redistribution rights are audited. | D |
| **IITM/citizen networks** | No authoritative Odisha inventory located in the reviewed search, 2026-08-16 | No defensible Odisha station count or open rural feed was found. | Do not claim density. Treat any later-discovered network as a supplemental input until validated. | D |
| **Prototype-owned nodes** | Proposed architecture based on Fasal and FarmBeats prior art | Rain, temperature/humidity, soil moisture, and local water-level sensing; optional wind only with adequate siting and calibration. No price is asserted because the bill of materials has not been selected. | Necessary for hyperlocal evidence and for detecting when coarse official forecasts diverge from farm conditions. | Proposed, not graded as prior art |

**Coverage judgment:** Odisha's future plan is dense on paper, but current usable density is unknown. The prototype should show independent nodes and graceful degradation rather than draw a misleading station-density map.

### 2.4 Cyclone, flood, SMS, IVR, and anticipatory-action systems

| Item | Named source, URL, and date | Operational facts | On-device component and fit | Grade |
|---|---|---|---|---|
| **IMD Meghdoot** | Google Play listing, https://play.google.com/store/apps/details?id=com.aas.meghdoot, accessed 2026-08-16 | Aggregates district- and crop-wise advisories from Agro Met Field Units with forecast and historic weather [5]. | No offline model, sensor mesh, SMS/IVR, or phone inference is established in the reviewed listing. Useful as advisory content and workflow prior art. | B |
| **OSDMA EWDS** | Special Relief Commissioner Odisha SOP, https://srcodisha.nic.in/data/SOP%20EWDS%20Project%20Odisha%20by%20SRC%20office.pdf, accessed 2026-08-16 | Six coastal districts; 122 siren locations; control from SEOC/BEOC; SMS, voice, email, radio/TV, social, sirens; GPRS/VHF and satellite resilience [30]. | No farm-specific advice or AI. It is the strongest last-mile resilience layer and a vital escalation path. | A |
| **mKisan** | Government of India, https://mkisan.gov.in/alpha, accessed 2026-08-16 | Preference-based information/advisories via text and voice messages, with database access even without internet [20]. | Demonstrates non-smartphone-compatible delivery, not local AI. | A |
| **Kisan Sarathi** | PIB, https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278757, accessed 2026-08-16 | Timely, authentic, multilingual advisories, schemes, weather updates, and expert access [28]. | Relevant human-expert escalation; reviewed evidence does not prove Odia IVR or on-device operation. | A |
| **Odisha Crop Contingency Plan 2025** | Government of Odisha, https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf, 2025 | Covers floods, waterlogging, cyclones, pests, soil/nutrient/salinity management, seeds, and district/block planning [37]. | Best authoritative retrieval corpus. It is not executable code or AI-generated advice, so agronomists must convert it into versioned rules. | A |
| **WFP anticipatory action** | WFP, https://www.wfp.org/anticipatory-actions and https://www.wfp.org/publications/anticipatory-action-year-focus-2025, 2025-2026 | WFP supports anticipatory action for floods and cyclones; in 2025, more than USD 35M was disbursed before disasters to support over 1.2M people [18][22]. | Strong global mechanism, but no reviewed source verifies an Odisha cash-before-cyclone farmer pilot or an on-device component. | A globally; D for claimed Odisha pilot |

#### Case study: OSDMA is the resilient delivery layer, not the farm brain

OSDMA's SOP documents a mature communications system rather than an AI concept. Sirens can be triggered centrally or at block level, and the system combines GPRS, VHF, satellite communication, solar power, batteries, and operator testing [30]. That is the right pattern for life-safety redundancy.

Its boundary is equally important. The SOP disseminates warnings but does not select crop actions from farm profiles [30]. CNC's white space is therefore the decision layer between an authoritative hazard and a delivery network: "Which farm should do what, by when, and why?" A pilot should integrate with, not duplicate, OSDMA procedures.

### 2.5 Academic and field-tested edge-AI deployments

| Deployment | Field evidence | What it proves | What it does not prove | Grade |
|---|---|---|---|---|
| **FarmBeats** | More than six months on 5-acre and 100-acre US farms; over 10M sensor measurements, 500,000 images, and 100 drone surveys [31]. Weather-aware duty cycling reduced an earlier 30% downtime to zero during the same cloudy month [31]. | A farm gateway can cache data, compute local summaries, serve locally while cloud-disconnected, and send summaries to the cloud [31]. | No vernacular LLM, farmer SMS/IVR, cyclone/flood advice, or outcome-to-adapter loop. | A |
| **PlantVillage Nuru** | Coastal Tanzania field study; 90 plants, 300 leaves, plus comparisons involving researchers, extension agents, and farmers [32]. | Offline commodity-phone inference and management advice are real. | No sensors, Odia, disaster workflow, or continual adapter update. | B |
| **FarmerChat** | Claimed 830,000+ users and 5M+ queries in five countries [27]. | Multimodal, local-context farm conversation can reach substantial scale. | Usage is not accuracy, avoided loss, uptime, adoption, or offline edge evidence. | B |
| **TinyML apple/mango disease paper** | MobileNetV2 system is proposed; the reviewed evidence does not expose device, latency, energy, memory, or real-farm results [9]. | TinyML is a plausible research direction. | No dependable field-deployment evidence for this problem. | C |
| **Federated learning plus TinyML review** | The reviewed evidence discusses the combination but does not establish agriculture hardware, field outcomes, or daily adapter updates [4]. | A research framework exists. | It is not evidence that the requested learning loop has operated safely in rural agriculture. | C |

#### Case study: FarmBeats supplies the architectural skeleton

FarmBeats places a PC gateway at the farm, where it runs local applications, caches detailed data, computes summaries, and continues local service without cloud connectivity. The cloud handles long-term storage, remote access, and cross-farm analytics [31]. Its solar, battery-backed base station also adapts duty cycles to power and weather [31].

For CNC, the farmer Android phone can replace the PC gateway at prototype scale, but only if the team accepts a key scope tension: non-smartphone farmers cannot each supply that gateway. A village agent phone, shared panchayat hub, or dedicated low-cost gateway is therefore required alongside SMS/IVR delivery.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| **Odisha/India official operational sources** | OSDMA EWDS SOP, IMD API, mKisan, Kisan Sarathi, Odisha contingency plan, Odisha administrative profile | IMD district-warning/CAP access and current AWS/ARG inventory are incomplete; no public machine interface for every needed input | **A-** for warning and advisory foundations; **C** for integration completeness |
| **Named agritech first-party sources** | Cropin, Plantix, Fasal, DeHaat, Gramophone, AgroStar, AquaConnect | Public prices mostly absent; architecture often marketing-level; no verified phone LLM among the seven | **B-** |
| **Cloud-provider case studies** | AgroStar Google Cloud case study | Strong backend evidence but no handset model or disconnected workflow | **A** for cloud classification |
| **Field research** | FarmBeats and Nuru | Different crops/geographies; no Odisha cyclone/flood trial; Nuru preprint source notes peer-review limitation | **A/B** |
| **Agriculture conversational AI** | FarmerChat, AgriLLM, KissanAI, Krishi Sathi | Strong product direction, sparse model/runtime details, no offline Odia proof, little outcome evaluation | **B-/C+** |
| **On-device foundation and Indic speech models** | Gemma 3n, AI4Bharat IndicConformer | Memory feasibility is clearer than Odia accuracy, thermals, battery, or Android runtime | **B** |
| **Public/citizen weather networks** | IMD portal and Bhubaneswar Weather Underground pages | No reproducible current Odisha station inventory, rural density, calibration, uptime, or licensing | **D** for density claim |
| **Anticipatory action** | WFP global program and 2025 totals | No verified Odisha farmer cash-before-disaster deployment in reviewed evidence | **A** globally; **D** for Odisha-specific claim |
| **Generic edge/TinyML literature** | Several reviews and proposed frameworks | Lab datasets, proposed architectures, missing uptime/adoption/field metrics | **C/D** |

The evidence is strongest where government infrastructure and measured field systems are concerned. It is weakest exactly where the novelty claim sits: local-language phone inference, feature-phone delivery during outages, and safe continuous adaptation.

## 4. WHAT IS MISSING

| Required link in the full loop | Closest public evidence | Exact uncovered gap |
|---|---|---|
| **Authoritative hazard ingestion** | IMD documents a seven-day city forecast API [35]. | No reviewed public specification establishes the complete district warning, cyclone track, CAP, AWS/ARG, authentication, rate-limit, and service-level interface needed for a live pilot. |
| **Hyperlocal sensing** | Fasal verifies farm sensors; FarmBeats verifies resilient sensor-to-gateway operation [7][31]. | No open Odisha deployment documents calibration, placement, uptime, flood survivability, maintenance cost, or data rights for low-cost farm nodes. |
| **Offline agriculture LLM** | Gemma 3n shows a 2 GB minimum memory footprint; Nuru proves offline bounded inference [23][32]. | No cited system runs a generative agriculture LLM offline on low-cost rural phones with measured latency, battery drain, thermal behavior, hallucination rate, and cyclone/flood safety. |
| **Odia end-to-end interface** | AI4Bharat covers 22 official languages; KissanAI demonstrates voice-oriented farm assistance [36][39]. | No public end-to-end benchmark covers noisy Odia speech -> farm terminology -> safe advice -> intelligible Odia TTS on a disconnected low-cost Android handset. |
| **Non-smartphone path** | mKisan supports text/voice without internet; OSDMA offers siren, SMS, voice, and broadcast channels [20][30]. | The phone-hub concept does not itself serve feature phones or survive a cellular outage. An IVR gateway and community failover remain separate infrastructure. |
| **Approved pre/post-disaster logic** | Odisha's 2025 plan covers relevant hazards and agronomic categories [37]. | No public source converts the plan into machine-testable, crop-stage-specific, farm-profile-specific rules with contraindications, deadlines, confidence, and accountable approvers. |
| **Outcome capture** | FarmerChat shows interaction scale [27]. | No cited platform publicly documents whether the farmer complied, what crop loss occurred, what counterfactual loss would have occurred, and how missing or biased reports are handled. |
| **Daily adapter fine-tune** | Generic federated/TinyML research exists [4]. | No public agriculture deployment documents a daily server-side adapter, safety evaluation, signature, over-the-air phone delivery, canary release, rollback, or protection against poisoned feedback. |
| **Commercial viability** | Plantix consumer diagnosis and DeHaat helpline are explicitly free [12][10]. | Hardware, maintenance, IVR minutes, SMS, support, model hosting, and replacement costs are undisclosed for most comparators, preventing an evidence-based total-cost benchmark. |
| **Measured Odisha impact** | OSDMA supplies operational warning resilience [30]. | No field trial links this proposed architecture to reduced crop loss, increased timely action, lower false alarms, or adoption among low-literacy Odisha farmers. |

The central white-space statement should therefore be phrased narrowly: **"We found no publicly documented production system that combines all required links."** It should not be phrased as a universal patent-style claim that no private or unpublished implementation exists.

## 5. HOW IT FEEDS THE EDGE-AI ENGINE

### 5.1 Tier-to-decision architecture

| Tier | Evidence-backed inputs and functions | Decision it powers | Proposed statistics and controls |
|---|---|---|---|
| **Sensor node** | Rainfall, temperature/humidity, soil moisture, and local water level. Use periodic transmissions, local buffering, battery health, and sequence numbers. FarmBeats supports power-aware duty cycling and local caching [31]. | Is the farm actually receiving hazardous rain, saturation, or rising water? Is a sensor failing? | Range checks; rate-of-change limits; robust median across nearby nodes; missingness and battery flags; a node trust score; no advice from one implausible reading. |
| **Phone/shared hub** | Cached farm profile, latest official alert, local sensor window, approved contingency rules, Odia prompts, and a small quantized model. Nuru supports the feasibility of offline inference on a 2 GB phone [32]. | Which approved action applies to this crop, stage, soil, livestock, and lead time? How should it be explained in Odia? | Deterministic rule selection first; retrieval from versioned Odisha guidance second; LLM used only for compression, explanation, and dialogue. Log the rule ID and evidence behind every message. |
| **Delivery plane** | SMS for concise action, IVR/TTS for low literacy, missed-call/callback workflow, local audio replay, and OSDMA/community escalation. mKisan and OSDMA validate the channel pattern [20][30]. | Which channel can reach this farmer now, and has the message been acknowledged? | Channel success probability; retry schedule; duplicate suppression; acknowledgement and callback queue; escalation when no delivery path succeeds. |
| **Learning server** | De-identified sensor summaries, alert context, advice ID, delivery result, farmer response, agronomist label, and observed damage after reconnection. | Should a rule, risk model, retrieval corpus, or language adapter change? | Drift tests; calibration curves; Brier score for event risk; precision/recall weighted toward missed severe events; subgroup error by district, crop, gender, phone type, and literacy; signed model packages and rollback. |

### 5.2 Predictive statistics underneath the demo

1. **Sensor quality before prediction.** Each record should carry timestamp, location, calibration version, battery, and missingness. Apply physical range checks and robust neighborhood comparison. A missing or suspect node should lower confidence, not silently become zero rainfall.

2. **Hyperlocal forecast correction.** Maintain a rolling error between the IMD forecast and observed local rain or temperature. An exponentially weighted correction can adapt to recent local bias while retaining the authoritative IMD hazard class. This should be presented as a proposed prototype estimator, not as an IMD method.

3. **Probabilistic farm risk.** Estimate `P(hazard at farm | IMD alert, local rain, soil saturation, water level, terrain, crop stage)`. Calibrate that probability on held-out events. Do not show a bare neural-network score as a probability unless calibration has been tested.

4. **Decision-theoretic trigger.** Send an action when expected avoidable loss exceeds action cost: `event probability x exposed value x vulnerability x action effectiveness > action cost`, subject to official-warning and safety constraints. This makes different thresholds for harvesting, draining, moving livestock, or applying an input explainable.

5. **Bounded advisory generation.** The rule engine chooses the action and deadline from approved content; the LLM produces a short Odia SMS and IVR script. Chemical dose, evacuation, finance, and animal-health advice should require exact approved text or expert escalation.

6. **Learning without unsafe self-modification.** The phone may adapt preferences locally, such as speech speed, preferred channel, crop ordering, and cached vocabulary. Gradient training should occur on the server. A "daily adapter" should be released only after automated regression tests and agronomist approval, then signed, canaried, and rollbackable. Early pilots should update less often if daily labels are too sparse or biased.

### 5.3 Case study: from OSDMA alert to one farm decision

Suppose an official cyclone warning arrives while a paddy field's local node reports saturated soil and rising drainage-channel water. The phone does not ask the LLM to infer whether a cyclone exists. It validates the official alert, checks sensor freshness and trust, matches crop stage and field drainage against a versioned Odisha contingency rule, and generates a short action plus deadline.

If the farmer has a smartphone, the result is available offline with local audio. If the farmer has only a feature phone, the shared hub queues SMS/IVR through a connected gateway. If telecom fails, the system does not claim delivery; it hands off to OSDMA siren/community procedures. This division respects OSDMA's proven resilience while adding the missing farm-specific decision layer [30].

## 6. REAL-vs-FILLER

| Claim or component | Evidence status | Classification | Product decision |
|---|---|---|---|
| **OSDMA multi-channel warning and resilient sirens** | Detailed operational SOP, redundancy, power, control, and testing [30] | **Genuinely usable** | Integrate/escalate; do not duplicate. |
| **Offline phone agricultural inference** | Nuru works offline on Android with field results and stated minimum RAM [32] | **Genuinely usable, bounded scope** | Demo a constrained model and disclose its limitations. |
| **Sensor-to-local-gateway-to-cloud architecture** | FarmBeats field deployments and measured reliability [31] | **Genuinely usable** | Reuse the architectural pattern on a phone/shared hub. |
| **Fasal sensors plus automated advice/control** | Soil and weather sensors plus irrigation/fertigation automation are explicit [7] | **Genuinely usable commercial prior art** | Use as closest Indian sensor comparator; do not imply local inference. |
| **FarmerChat multimodal advisory** | Voice/text/photo and substantial claimed usage [25][27] | **Genuinely usable interaction prior art** | Copy interaction patterns, not unverified offline claims. |
| **mKisan text/voice without internet** | Government portal states text/voice and no-internet access [20] | **Genuinely usable channel precedent** | Use as accessibility benchmark. |
| **Odisha AWS in every block and ARG in every GP today** | Announced target, not verified operational inventory [29][6] | **Filler if presented as current coverage** | Label as planned; deploy/calibrate pilot nodes. |
| **Plantix is offline on-device** | Official reviewed pages show free diagnosis and an API but no offline/local-inference statement [12][8] | **Unverified** | Do not repeat without a disconnected test or technical source. |
| **Any app plus AI equals edge AI** | AgroStar explicitly shows a cloud backend [33]; several others omit runtime details | **Decorative wording** | Require model file, runtime, hardware, latency, and airplane-mode evidence. |
| **Gemma 3n automatically solves Odia advice** | Memory feasibility is documented; Odia quality is not [23] | **Partly real, partly filler** | Benchmark Odia and use curated fallback audio. |
| **Daily fine-tuning guarantees continuous improvement** | No reviewed deployment demonstrates the full safe loop [4] | **Filler and safety risk** | Demonstrate signed adapter replacement, not autonomous unreviewed learning. |
| **WFP cash-before-cyclone pilot in Odisha** | Global anticipatory action is real, but Odisha-specific evidence was not found [18][22] | **Unsupported locally** | Cite only the global mechanism unless an Odisha program document is obtained. |
| **Weather Underground gives dense Odisha coverage** | Public search produced city pages, not an auditable station inventory | **Decorative** | Exclude from coverage claims. |

The general test is simple: a useful edge claim must identify **where the model executes, what happens in airplane mode, which device was tested, and what field metric was measured**. Without those four items, classify the claim as marketing or incomplete evidence.

## 7. NOISE LOG

| Searched and discarded item | Why discarded |
|---|---|
| **GitHub project named "PlantiX" by Soumya Chakraborty** | It is a separate potato-leaf Android project, not PEAT's official Plantix product. The official Plantix source is the free crop-diagnosis service at plantix.net [12]. |
| **Generic "edge AI in agriculture" vendor articles** | They describe benefits but provide no Odisha deployment, hardware bill, disconnected test, uptime, adoption, or loss-reduction result. |
| **2025 proposed edge-agentic agriculture framework** | The reviewed evidence describes a development objective, not a deployed field system, and reports no hardware, language interface, or continual-learning result [16]. |
| **TinyML and federated-learning reviews** | Useful for vocabulary and future design, but not evidence of a daily agriculture adapter loop in production [9][4]. |
| **Weather Underground Bhubaneswar pages** | Airport/city history and forecasts do not establish personal-station density, rural coverage, calibration, or redistribution rights. |
| **IITM Odisha network query** | No authoritative station inventory or public rural feed was located. Absence from this search is not proof that no IITM instrument exists; it is proof that a coverage claim would be unauditable from the found material. |
| **WFP Odisha cash query** | The results supported WFP's global anticipatory-action program but not an Odisha-specific cash-before-cyclone farmer pilot [18][22]. |
| **Unofficial Cropin pricing aggregators** | Public price claims were not accepted because the reviewed first-party Cropin source did not disclose price [14]. |
| **Social-media statements about Fasal AI/IoT** | Replaced with Fasal's first-party sensor statements and the FAO profile [7][34]. |
| **Duplicate company-name records** | Searches and structured company data returned unrelated firms named AgroStar, DeHaat, and Gramophone. Only matching official domains and India agriculture entities were retained. |
| **"KisanLLM" as a generic label** | No sufficiently authoritative, technically specified project under that exact label was found. AgriLLM, KissanAI/Dhenu, Krishi Sathi, and FarmerChat were kept as identifiable alternatives. |

This log matters because the main analytical error in this market is entity and capability conflation: a mobile app is mistaken for an offline model, a sensor is mistaken for edge inference, and a global program is mistaken for an Odisha deployment.

## 8. VERDICT

### Prototype: **GO**

A statement-faithful prototype is achievable without pretending the full system is already field-proven. It should demonstrate:

1. One or more low-cost nodes sending rain, soil-moisture, temperature/humidity, and water-level observations to an Android/shared hub.
2. A real IMD seven-day city forecast connector plus a clearly labeled cached/simulated district cyclone-warning fixture, because the complete pilot alert interface is not yet verified [35].
3. A versioned rule engine derived from the Odisha Crop Contingency Plan, with each action linked to crop, stage, hazard, lead time, and source [37].
4. A small quantized phone model used only to summarize and explain the selected rule in Odia, with a curated template/audio fallback.
5. Airplane-mode inference and delayed synchronization on a representative 2 GB to 4 GB Android handset. Nuru and Gemma 3n establish plausible memory precedent, not guaranteed performance [32][23].
6. SMS and IVR simulation for feature phones, acknowledgement logging, and an explicit "delivery unavailable" state rather than a false success.
7. Offline outcome capture: received, understood, acted, not acted, observed damage, photo/voice note, and reason.
8. A server-side training demonstration that creates a small adapter from approved data, runs regression tests, signs it, sends it to a canary phone, and rolls it back. The demo should call this a **controlled update pipeline**, not proven continuous improvement.

The prototype's success metric is not crop-loss reduction yet. It is whether the complete path works under disconnection, every message is traceable to an approved rule, the Odia output is intelligible, and unsafe or low-confidence cases escalate rather than hallucinate.

### Pilot: **GATED**

A farmer-facing pilot should not launch until these gates close:

- **Authority gate**: written access and usage terms for operational IMD district/cyclone warnings and any AWS/ARG data; coordination with OSDMA, the Odisha agriculture department, and local extension staff.
- **Agronomy gate**: crop-stage decision tables approved by named agronomists, including prohibited actions, salinity/waterlogging cases, livestock handling, and post-event disease risks.
- **Hardware gate**: calibrated station placement, rainfall and water-level validation, weatherproofing, power budget, spare policy, and measured uptime through heavy rain.
- **Language gate**: low-literacy Odia comprehension testing for ASR, text, TTS, dialects, agricultural terms, and noisy phone calls. AI4Bharat's 22-language coverage is a starting point, not acceptance evidence [36].
- **Access gate**: a real IVR/SMS provider, consent, opt-out, retry/escalation logic, and a community/shared-hub plan for farmers without smartphones.
- **Safety gate**: deterministic hazard and action selection, no free-form chemical or evacuation instruction, confidence display, human escalation, complete audit logs, and kill switch.
- **Learning gate**: de-identification, poisoning checks, minimum label quality, offline evaluation, agronomist sign-off, signed artifacts, canary release, and rollback. "Daily" must remain optional until sufficient reliable labels exist.
- **Evidence gate**: a prospective evaluation measuring delivery, comprehension, action completion, false alarms, missed severe events, uptime, subgroup performance, and crop-loss outcomes. Usage and query counts alone are insufficient, as FarmerChat's scale evidence illustrates [27].
- **Economics gate**: a full per-farmer and per-village cost covering sensors, gateway/phone, solar/battery, installation, calibration, maintenance, replacements, SMS, IVR minutes, support, model hosting, and agronomist review.

**Final verdict:** **GO** for the prototype, because every tier can be demonstrated from existing components. **GATED** for a live pilot, because the unresolved issues concern authoritative feeds, safety, language quality, field reliability, and causal impact rather than slideware completeness.

## Synthesis

| Prior-art family | Mechanism | Scope | Evidence base | Main trade-off | Time horizon for CNC |
|---|---|---|---|---|---|
| **OSDMA + IMD + Meghdoot** | Authoritative hazard generation and resilient dissemination | District/coastal warning and crop advisory | Strongest operational/government evidence [30][5][35] | Trust and reach are high; farm personalization and open machine interfaces are incomplete | Integrate now for prototype; formalize access before pilot |
| **FarmBeats + Fasal** | Sensors, gateway, local summaries, cloud analytics, automation | Farm microclimate and operations | FarmBeats has measured field deployments; Fasal has Indian commercial product evidence [31][7] | Strong physical layer; no Odia LLM or disaster-specific advice | Reuse architecture immediately; validate local hardware in monsoon |
| **Nuru + Gemma 3n** | Offline on-device inference | Bounded vision diagnosis versus general multimodal language model | Nuru has field results; Gemma has device-memory specifications [32][23] | Offline speed/privacy versus field error, battery, and language uncertainty | Prototype now; safety benchmark before pilot |
| **FarmerChat + KissanAI + AgriLLM + Krishi Sathi** | Conversational, multilingual agricultural assistance | Broad farmer questions and personalized advice | Strong product claims and user scale for FarmerChat; sparse runtime/outcome details elsewhere [27][39][15][13] | Natural interaction versus unverified offline execution and outcome quality | Copy UX now; do not claim edge equivalence |
| **Cropin + Plantix + DeHaat + Gramophone + AgroStar + AquaConnect** | Enterprise intelligence, diagnosis, helplines, apps, commerce, remote sensing | Different segments of the agriculture value chain | First-party product evidence, but uneven technical disclosure [14][8][10][40][33][41] | Market maturity versus little proof of the requested end-to-end offline loop | Treat as component/market comparators, not direct replicas |
| **mKisan + Kisan Sarathi + WFP** | Text/voice outreach, expert advice, and anticipatory action | Non-smartphone access and pre-disaster assistance | Strong government/global program evidence [20][28][18][22] | Inclusive channels and proven program logic versus no local phone model or verified Odisha WFP pilot | Reuse channel and program patterns; verify local partners |
| **Daily adapter learning loop** | Outcome capture, server tuning, signed phone update | Cross-farm continual improvement | No comparable field-proven agriculture deployment found in reviewed sources [4] | Potential adaptation versus poisoning, drift, sparse labels, and unsafe regression | Demo as controlled MLOps; defer autonomous cadence |

The non-obvious conclusion is that the competitive gap is not "AI for agriculture." That field is crowded. It is the **controlled composition** of four mature but disconnected mechanisms: OSDMA/IMD authority, FarmBeats/Fasal sensing, Nuru-style offline inference, and mKisan/FarmerChat accessibility.

The largest tension is between the phrase "farmer phone as hub" and the requirement to serve non-smartphone users. A robust design resolves it by making the Android device a **shared or optional compute hub**, while SMS/IVR and OSDMA remain independent delivery paths. The second tension is between "continuous learning" and disaster safety. The correct pilot mechanism is not self-training on every farmer response; it is delayed, supervised, server-side adaptation with evaluation and rollback.

This yields a defensible white-space claim: **the prototype is novel in its end-to-end orchestration and Odisha-specific offline accessibility, not because any individual sensor, LLM, app, or warning channel is new.**

## References

1. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Early Warning ...*. https://www.osdma.org/preparedness/early-warning-communications/ewds
2. *Gramophone for Startups — Indian Agritech Distribution ...*. https://gobeunicorn.com/startup-ai-tools/gramophone
3. *KissanAI*. https://kissan.ai/
4. *Federated learning and TinyML on IoT edge devices*. https://www.sciencedirect.com/science/article/pii/S2405959525000839
5. *Meghdoot - Apps on Google Play*. https://play.google.com/store/apps/details?id=com.aas.meghdoot&hl=en-US
6. *Odisha districts asked to identify land for setting up AWS ...*. https://www.newindianexpress.com/states/odisha/2026/Jul/03/odisha-districts-asked-to-identify-land-for-setting-up-aws-and-rain-gauges
7. *Fasal - Smart Irrigation System | Agriculture Automation*. https://www.fasal.co/
8. *Crop Disease Diagnosis & Produce Grading API*. https://plantix.net/en/plantix-intelligence/api-toolkit
9. *TinyML for Plant Disease Detection: Efficient Edge AI ...*. https://www.sciencedirect.com/science/article/pii/S1877050925016515
10. *Farmers Helpline & Farmers Support | 1800 1036 110 - DeHaat*. https://agrevolution.in/advisory-farmers-helpline-and-support
11. *Advanced IoT Sensors & Smart Agriculture Automation*. https://www.fasal.co/fasal-story
12. *Plantix | #1 FREE app for crop diagnosis and treatments*. https://plantix.net/en
13. *Krishi Sathi: AI-Powered Farming Companion - BharatGen*. https://bharatgen.com/products/krishi-sathi
14. *Cropin | SaaS-based AgTech | Smart Farming App | Agriculture ...*. https://www.cropin.com/
15. *AgriLLM: How CGIAR is developing an AI-powered agricultural ...*. https://www.cgiar.org/news-events/news/agrillm-how-cgiar-is-developing-an-ai-powered-agricultural-advisory-service-for-global-south
16. *Edge-enabled smart agriculture framework: Integrating IoT ...*. https://www.sciencedirect.com/science/article/pii/S2590123025033973
17. *Accuracy of a Smartphone-Based Object Detection Model ...*. https://pubmed.ncbi.nlm.nih.gov/33391304
18. *Anticipatory Action for climate shocks | World Food Programme*. https://www.wfp.org/anticipatory-actions
19. *FarmBeats: AI, Edge & IoT for Agriculture*. http://microsoft.com/en-us/research/project/farmbeats-iot-agriculture
20. *mKisan:A Portal of Government of India for Farmer Centric ...*. https://mkisan.gov.in/alpha
21. *Gemma 3n — Google DeepMind*. https://deepmind.google/models/gemma/gemma-3n
22. *Anticipatory Action Year in Focus 2025*. https://www.wfp.org/publications/anticipatory-action-year-focus-2025
23. *Introducing Gemma 3n: The developer guide - Google Developers ...*. https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide
24. *ai4bharat/indictrans2-indic-en-dist-200M · Hugging Face*. https://huggingface.co/ai4bharat/indictrans2-indic-en-dist-200M
25. *FarmerChat: Farming answers in seconds | Digital Green*. http://digitalgreen.org/farmerchat
26. *PlantVillage Nuru: Pest and disease monitoring using AI*. http://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai
27. *Farmer Chat*. https://www.farmerchat.io/
28. *The Kisan Sarathi Platform*. https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278757&lang=1&reg=3
29. *Odisha:Automatic weather stations in blocks soon - OrissaPOST*. https://www.orissapost.com/automatic-weather-stations-in-blocks-soon/
30. *Special Relief Commissioner Odisha*. https://srcodisha.nic.in/data/SOP%20EWDS%20Project%20Odisha%20by%20SRC%20office.pdf
31. *Farmbeats Webpage 1*. https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf
32. *biorxiv.org*. https://www.biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf
33. *AgroStar Case Study  |  Google Cloud*. http://cloud.google.com/customers/agrostar
34. *Fasal - Science, Technology and Innovation (STI) Portal*. https://sti-portal.fao.org/innovations/fasal
35. *IMD API Reference*. https://api.imd.gov.in/public/api_reference.html
36. *IndicConformer - ai4bharat.iitm.ac.in*. https://ai4bharat.iitm.ac.in/areas/model/ASR/IndicConformer
37. *Crop Contigency Plan 2025*. https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
38. *Demographic Profile | Panchayati Raj & Drinking Water ...*. https://panchayat.odisha.gov.in/en/about-us/demographic-profile
39. *KissanAI: Navigating digital divide in agriculture*. https://www.microsoft.com/en-in/aifirstmovers/kissanai
40. *Gramophone - Smart Farming App - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en&id=agstack.gramophone
41. *Aquaconnect*. https://aquaconnect.blue/
42. *AgroStar | AgriTech Solutions India, Farm Advisory & Market ...*. https://corporate.agrostar.in/
