# KrishiSetu's Defensible Edge Is Integration, Not Novel Components

## 1. EXECUTIVE SUMMARY

- **No Exact End-to-End Twin Found**: The sweep found operational systems for district-and-crop weather advice, farmer registries, SMS or voice delivery, flood detection, and forecast-triggered early action, but no documented system combining all of these with both pre-disaster and post-disaster crop actions for a persistent Odisha farm profile. Meghdoot, for example, publishes district-and-crop advisories twice weekly, while IFRC forecast-based action uses forecasts and risk analysis to release resources before disasters [6][9]. -> Claim differentiation around the integrated workflow, not around AI, alerts, SMS, IVR, or farm data individually.

- **Odisha Already Has the Hardest Identity Assets**: Krushak Odisha displayed **9,196,615 registered farmers**, while e-Chasa describes state farmer-and-crop data usable by multiple departments [10][4]. -> Treat these as consented upstream systems of record; do not build a competing farmer registry for the prototype.

- **A Student Team Can Build a Free Baseline Now**: SoilGrids supplies global soil properties at **250 m** under CC BY 4.0 through WCS, WMS, and WebDAV [35]. WorldCover supplies global **10 m** land cover free of charge, and GFSAD30 supplies freely usable global cropland extent [14][33]. -> Pre-cache Odisha subsets rather than depending on live third-party APIs during a cyclone.

- **Satellite Layers Are Priors, Not Farm Truth**: WorldCover is a 2021 land-cover snapshot with **76.7% overall accuracy**, not a current crop registry [14]. SoilGrids' 250 m cells and ERA5-Land's roughly 9 km native grid cannot represent every small plot [35][21]. -> Use e-Chasa or farmer confirmation for the sown crop, then use remote sensing only to enrich or cross-check the profile.

- **The Best Disaster Stack Splits Forecast From Observation**: GDACS offers free cyclone and flood event APIs, while GloFAS Global Flood Monitoring uses incoming Sentinel-1 SAR to map observed flooding worldwide in near real time [18][20]. -> Trigger preparation from IMD or GDACS forecasts; trigger damage triage and recovery workflows from observed rainfall, inundation, and farmer IVR responses.

- **Low-Literacy Delivery Needs More Than Text Translation**: mKisan was designed around mobile messaging because rural internet penetration was low and reported potential reach to nearly **9 crore farm families** [8]. Viamo and Esoko evidence also points to literacy and trust barriers. -> Use short outbound voice calls, repeatable keypad menus, missed-call callback, local crop vocabulary, and a human escalation path alongside SMS.

- **Blockchain Is Not the Missing Ingredient**: AgriDigital and GrainChain have real commodity-workflow products, but their public value propositions center on contracts, deliveries, inventory, payments, traceability, and supply-chain coordination, not disaster advice. -> Borrow append-only audit trails and permissioned data sharing; do not make blockchain part of the differentiation claim.

- **The Honest Differentiation Is Narrow but Strong**: The defensible claim is not "first agricultural advisory" or "first voice service." It is: **a consented Odisha farm-and-current-crop profile joined to official cyclone/flood triggers, crop-stage-specific pre-event and post-event actions, and closed-loop SMS/IVR delivery, with every recommendation replay-testable against historical events**. This is an integration and execution claim, not a patent-novelty opinion.

## 2. WORLDWIDE INVENTORY

The tables below retain every material, non-duplicate hit from the sweep. "Direct match" means that a system implements at least two links in the target chain: local farm or crop context, hazard or weather input, actionable agricultural output, accessible delivery, and pre/post-disaster timing. None implements all five links in the evidence reviewed.

### Direct matches and strong analogues

| Name | Country/region | What it does | Named source, URL and date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| **mKisan** | India | Government push-SMS infrastructure for agriculture; designed for rural reach where internet access is weak. The source describes reach to nearly 9 crore farm families [8]. | mKisan, `https://mkisan.gov.in/Home/AboutPushSMS`, accessed 2026-08-16 | Live portal | National potential reach; no cyclone-specific usage count verified | Reuse the channel architecture and preference-based targeting; add hazard triggers, IVR, acknowledgements, and post-event workflows. |
| **Meghdoot** | India | Aggregates district-and-crop advisories from Agro Met Field Units every Tuesday and Friday with forecast and historical weather [6]. | Meghdoot app listing, `https://apps.apple.com/us/app/meghdoot/id1474048155`, accessed 2026-08-16 | Live app | India; district granularity | It proves crop-contextual agromet advice, but a cyclone requires event-driven updates faster than a twice-weekly schedule and a non-app channel. |
| **BAMIS** | Bangladesh | Bangladesh Agro-Meteorological Information System joins meteorology, water, and extension institutions for agricultural weather information [3]. | BAMIS, `https://www.bamis.gov.bd/en/page/introduction`, accessed 2026-08-16 | Live web system/project | Bangladesh | The closest institutional pattern for flood-prone agriculture: connect meteorological, hydrological, and extension owners instead of forcing one model to replace them. |
| **Ignitia** | West Africa and other markets | Commercial weather intelligence and agricultural advice; documented evidence includes climate-smart forecasts and a 2021 Brazil market entry [7]. Another official catalogue describes rainfall forecasts delivered by SMS. | UNDP Digital X, `https://digitalx.undp.org/catalogs/ignitia.html`, accessed 2026-08-16 | Live company/web presence | WFP described operation in 11 countries; farmer totals were not consistently disclosed in primary evidence | Hyperlocal forecasts can be packaged as simple messages, but forecast precision claims must be locally calibrated and separated from IMD authority. |
| **Farmerline/Mergdata** | Ghana/global | Builds farmer records and communication workflows for agribusinesses, governments, and NGOs; its website says it began with 800 Ghanaian farmers in 2013. | Farmerline, `https://farmerline.co/`, accessed 2026-08-16 | Live company | Company reports more than 2.3M farmers and 3,000 partners across 50 countries; treat as company-reported | The reusable asset is profile + segmentation + localized communication, not a cyclone model. Preserve consent and let extension agents correct bad records. |
| **Viamo Platform/3-2-1** | Multi-country | Delivers development information over channels designed for basic phones and low-connectivity populations; agriculture is one content domain. | Viamo Agriculture, `https://viamo.io/category/agriculture`, accessed 2026-08-16 | Live company/platform | Multi-country; comparable agricultural deployment count not verified | Voice navigation and language localization are infrastructure. Hazard and farm personalization must be supplied by KrishiSetu. |
| **FAO anticipatory action** | Global humanitarian operations | Uses risk analysis and forecasts to trigger interventions before a shock becomes a humanitarian emergency [5]. | FAO, `https://www.fao.org/emergencies/our-focus/anticipatory-action/en`, accessed 2026-08-16 | Operational program/framework | Multi-country | Adopt the **forecast trigger -> pre-agreed action** discipline. A warning without an owned action, deadline, and responsible actor is not an advisory. |
| **IFRC forecast-based action/financing** | Global humanitarian operations | Uses forecasts and risk analysis to activate funding before extreme weather [9]. | IFRC, `https://www.ifrc.org/early-warning-early-action`, accessed 2026-08-16 | Operational framework | Multi-country | Pre-authorize actions and escalation thresholds. KrishiSetu should similarly lock action cards to IMD severity, lead time, crop, stage, and flood exposure. |
| **Sri Lanka Agro-Met Advisory** | Sri Lanka | Issues agricultural information from medium- and short-range weather forecasts to reduce crop losses from unexpected weather. | Sri Lanka Department of Agriculture, `https://doa.gov.lk/division-of-agro-climatology-and-climate-change/`, accessed 2026-08-16 | Government service | National, publication scale not disclosed | Official extension ownership matters. The evidence did not establish individualized SMS/IVR or a pre/post cyclone workflow. |
| **Arable Mark platform** | Global/commercial | A no-maintenance in-field device captures weather, plant, soil, irrigation, and crop-image data [47]; apps provide real-time data, forecasts, alerts, and an API [47]. | Arable, `https://arable.com/products`, verified 2026-08-11 | Live commercial platform | Customers or initiatives in more than 50 countries were reported [48] | It is a strong farm-data analogue, not a public-warning service. Borrow the unified field profile; avoid assuming every Odisha farmer can deploy hardware. |
| **PlantVillage Nuru** | Africa, Asia, Americas | Mobile crop-health support; FAO describes WaPOR-derived plot biomass information that helps farmers decide actions. | FAO product catalogue, `https://www.fao.org/in-action/remote-sensing-for-water-productivity/applications-and-uses/applications-catalogue/product-detail/PlantVillage-Nuru_1331767/en`, accessed 2026-08-16 | Deployed/research-backed app | Multi-region; exact active-user count not verified | Offline-first diagnosis and plot context are relevant. It is primarily crop-health support, not an official cyclone/flood warning and recovery engine. |
| **FAO FAMEWS** | Global | Field scouts and pheromone traps feed a platform mapping fall-armyworm infestation at global, national, and subnational levels. | FAO catalogue, `https://data.apps.fao.org/catalog/dataset/fao-famews`, accessed 2026-08-16 | Live specialized platform | Global pest surveillance | This is a useful **field observation -> map -> action** pattern, but for a biological hazard rather than cyclone or flood. |
| **My Farm Info** | India | Secondary search evidence described weather/disease SMS alerts plus flood and wind risk pages. | Historical domain listed at `http://www.myfarminfo.com`; secondary profile accessed 2026-08-16 | **Unverified/dead-looking** | No reliable current scale | This would be a close analogue if independently verified. Because the evidence was an aggregator and the product could not be confirmed as operational, it cannot support a novelty claim. |

**Takeaway:** mKisan, Meghdoot, BAMIS, Farmerline/Viamo, and FAO/IFRC collectively cover almost the whole chain, but in separate systems. KrishiSetu's opportunity is to compose these patterns with Odisha's existing identity and crop infrastructure.

### Indirect matches: borrowable data layer

#### Soil, cropland, and crop-type layers

| Name | Geography | What it provides and resolution | License/access; free today? | Odisha advisory role |
|---|---|---|---|---|
| **SoilGrids** | Global | Soil properties at **250 m**, six standard depth intervals; includes pH, organic carbon, texture, bulk density, CEC, and nitrogen [35]. | **CC BY 4.0; FREE.** WCS/WMS/WebDAV are available, although the REST API was temporarily paused [35]. | Pre-fill coarse soil priors for each farm; never present a 250 m estimate as a lab test or plot truth. |
| **AfSIS** | Africa | Three-dimensional African soil-property maps, with products up to **250 m** and some 1 km outputs [16]. | Open-science notebooks are published, but the reviewed page did not state a single product license/API. Project ran 2009-2016 [16]. | Methodological analogue only; it does not cover Odisha. |
| **USDA SSURGO/gSSURGO** | United States | Detailed soil surveys collected at approximately **1:12,000 to 1:63,360**, with water capacity, reaction, conductivity, flooding frequency, and yield-related attributes [26]. | Downloadable shapefile and text attributes; no reviewed source established an Odisha-reusable license [26]. | Architecture exemplar for joining polygons and interpretable soil attributes; no Indian coverage. |
| **EU LUCAS Soil 2018** | EU plus UK | Laboratory point samples, mainly 0-20 cm, including pH, carbon, nitrogen, phosphorus, potassium, EC, Fe, and Al [36]. | **FREE after registration** under a broad EU data license [36]. | Training/method comparison only. The source explicitly warns that points are not representative of field conditions [36]. |
| **HWSD v2.0 / China contribution** | Global | **1 km/30 arc-second** global inventory with seven layers down to 200 cm [45]. It incorporates national sources, including China's soil map, rather than exposing a new high-resolution Chinese farm service. | Downloadable FAO raster/database; exact license was not stated on the reviewed page. | Coarse fallback and taxonomy crosswalk. The search did not find a frictionless, current, high-resolution Chinese national soil API suitable for Odisha. |
| **ESA WorldCover** | Global | 2020 and 2021 land cover at **10 m** [28]. The 2021 product has 11 broad classes and 76.7% overall accuracy [14]. | **CC BY 4.0; FREE**, downloadable/WMTS [14]. | Locate probable cropland and exposure, not the current crop type. |
| **Copernicus HRL Croplands/Crop Types** | EEA Europe | Annual **10 m** crop-type and cropping-pattern products. | Copernicus products are free; product access is through Copernicus Land Monitoring/Data Space. | Excellent technical pattern, but Europe-only. The sweep did **not** verify a global CGLS 10 m crop-type product for Odisha. |
| **FAO WaPOR** | Africa and Near East | Water productivity, evapotranspiration, biomass, yield, precipitation, and crop-calendar layers: 250 m Level 1, 100 m Level 2, and 30 m pilot Level 3 [15]. | **Open catalogue, downloads and API; FREE** [15]. | Valuable model and API design, but its documented coverage excludes Odisha. Do not list it as an India data source. |
| **USDA NASS Cropland Data Layer** | United States | Annual crop-specific land cover; resolution changed from **30 m to 10 m** beginning in 2024 [40]. | Download and developer services exist; exact license was not stated on the reviewed announcement page. | Gold-standard crop-registry validation pattern, no Odisha coverage. |
| **GFSAD30** | Global | **30 m** cropland extent, including rainfed/irrigated distinctions, not a detailed current-crop registry [33]. | **FREE for educational, research, and commercial use** through LP DAAC and Google Earth Engine [33]. | Cross-check whether a registered parcel is plausibly cropped and derive broad exposure. |
| **GLAD global cropland** | Global | **30 m** cropland-extent epochs from 2000-2019 [29]. | GeoTIFF quadrants and Earth Engine IDs; the reviewed page did not state a clear license [29]. | Historical land-use baseline for replay. It excludes woody perennial crops, permanent pasture, and shifting cultivation [29]. |

These layers answer "where might cropland or a soil condition be?" They do not reliably answer "what did this farmer sow this season?" The correct data hierarchy is **registry/farmer confirmation -> field observation -> recent imagery -> coarse global priors**.

#### Farm registries and profile infrastructure

| Name | Country/region | Pattern and access | Status/scale | Odisha lesson |
|---|---|---|---|---|
| **Krushak Odisha** | Odisha, India | State farmer portal and single-record pattern; operational access is authenticated. | Live portal; displayed **9,196,615** registered farmers when reviewed [10]. | Use its farmer identifier and consented contact/profile data where permission exists; do not scrape the portal. |
| **e-Chasa Digital Crop Survey** | Odisha, India | State farmer-and-crop survey data intended for use by multiple departments and agents [4]. | Live portal; machine API and field schema were not publicly verified. | Best candidate for current crop, season, and parcel linkage. Design a mock adapter now and seek a sanctioned API later. |
| **AgriStack Farmer Registry** | India | National/state architecture using unique farm, farmland-plot, and owner-plot identifiers; FAQ version 1.1 is dated July 2024. | Government rollout; person-level data are not open bulk data. | Adopt stable IDs, versioned records, consent receipts, and source provenance rather than copying private attributes. |
| **EU IACS/LPIS** | European Union | Parcel-identification and agricultural-payment administration; an EU hub links to member-state geoportals publishing **some** IACS data. | Mature, but openness is fragmented by member state. | Separate parcel geometry, claimant identity, crop declaration, and payment eligibility. Public parcel data do not imply public personal profiles. |
| **USDA FSA farm/CLU records** | United States | Operational farm and common-land-unit records for program administration. | Mature but access-restricted; not a public farmer-profile API. | Government registries can be infrastructure without being open data. Build a minimum-data, purpose-bound integration. |
| **KIAMIS / e-voucher pattern** | Kenya | National digital public infrastructure describes a centralized farmer registry as a shared, interoperable agricultural-service backbone. | Live web presence; open person-level download was not found. | The registry should support many services through controlled interfaces; subsidy and advisory uses should not create an unrestricted data lake. |
| **ABARES Farm Data Portal/surveys** | Australia | Aggregated farm-survey information and analysis rather than a transaction-level farmer registry. | Live analytical portal; survey microdata access is controlled. | Useful for population baselines and policy evaluation, not for addressing a warning to a named farm. |

The registry comparison exposes the real governance requirement: profile-as-infrastructure works when identity, parcel, crop declaration, consent, provenance, and access control are separate objects. A flat spreadsheet of names, phone numbers, and crops is neither durable nor safe.

#### Weather and disaster data

| Name | Coverage and role | Resolution/cadence | License/access; free today? | Best KrishiSetu use |
|---|---|---|---|---|
| **IMD alerts and Agromet** | India; authoritative warnings and agricultural bulletins | Alert-dependent; district/state advisory products | Official source; machine-use terms and API access must be agreed with IMD | **Primary operational trigger.** Other global feeds should cross-check or backfill, never silently override IMD. |
| **NASA POWER** | Global meteorological and solar time series for agriculture and energy | Coarse reanalysis/analysis grid with hourly, daily, monthly, and climatology API products | **FREE API/download** [11] | Historical features, evapotranspiration inputs, and gap filling; not a plot-scale cyclone warning. |
| **ERA5-Land** | Global land-surface reanalysis, 1950-present | Hourly, distributed at **0.1 degrees** with roughly **9 km** native resolution; updated daily [21] | **CC BY; FREE** [21] | Long historical replay and baseline soil/water variables, not a warning forecast. |
| **CHIRPS** | Quasi-global land rainfall observation blend | Fine gridded rainfall history; CHIRPS v3 is available and v2 production is scheduled to end after December 2026 [46] | **FREE download** | Historical rainfall and drought/flood replay; validate version changes before training. |
| **IMD gridded rainfall** | India | Common research products include daily gridded rainfall; exact operational resolution and redistribution terms depend on product | Not verified as a frictionless public production API in this sweep | Prefer sanctioned access. Do not make a prototype dependent on an unconfirmed endpoint. |
| **AEMET OpenData** | Spain | Observation and forecast endpoints exposed through REST | **FREE REST API** under Spain's reuse framework | API and documentation pattern only; no Odisha coverage. |
| **Australia BOM data services** | Australia | Observation, forecast, radar, and warning feeds | Public data services, but endpoint and reuse terms vary | Architecture comparison only; no Odisha coverage. |
| **GDACS API** | Global cyclone, flood, earthquake and other events | Event/date/alert-level records; geospatial API, XML, GeoJSON, KML | **FREE API** with source acknowledgement [18] | Event discovery, severity cross-check, and historical replay indexing. It is not farm advice. |
| **GloFAS Global Flood Monitoring** | Global observed flooding from Sentinel-1 SAR | Near-real-time processing; input backscatter sampled at **10 x 10 m**, with output limitations and acquisition gaps [20] | Copernicus information is openly accessible [20] | Confirm likely inundation and prioritize post-event calls. It detects observed water; it is not a cyclone forecast [20]. |
| **Copernicus EMS On-Demand Mapping** | Global emergency activations | Activation-specific delineation and grading maps | **Free-of-charge mapping service** | High-quality event context and validation labels, but availability depends on activation and processing. |
| **NASA GPM IMERG** | Near-global precipitation observation | Half-hourly **0.1 degree** rainfall products, including near-real-time and research/final streams | **FREE via NASA Earthdata** | Rainfall accumulation, event replay, and anomaly detection. Grid scale is still much larger than many farms. |
| **USGS event pages/data** | Primarily US and event-specific holdings | Event-dependent | Public, but not one uniform global cyclone/flood API | Supplemental validation only; GDACS, Copernicus and NASA are more systematic for the Odisha prototype. |

A production design should not collapse these sources into one misleading "risk score." Keep source, issue time, valid time, spatial footprint, uncertainty, and authority in every hazard record.

#### Farm-data cooperatives and blockchain attempts

| Name | Country | Real product/status | What the sweep found | Lesson for KrishiSetu |
|---|---|---|---|---|
| **AgriDigital** | Australia | Live grain-management software | Current pages emphasize contracts, deliveries, inventory, payments, and reporting, not the blockchain story [44]. | Durable value came from workflow and shared records. Use ordinary signed audit logs unless distributed consensus solves a real multi-owner problem. |
| **GrainChain** | US/Mexico/Latin America | Live company/web presence | Offers farmer and commodity-supply-chain solutions; current public evidence did not establish a disaster-advisory use. | Interoperable participant records and traceability are relevant; tokenization is not. |
| **ripe.io** | United States | Historical food-blockchain venture; current operating status not verified | The sweep did not find sufficient recent first-party product evidence to call it an active farm-data utility. | Mark as unverified/dead-looking, not as proof that blockchain-based farm profiles work at public scale. |

### Ideas-only, prototypes, repositories and hackathons

| Name | Country/context | What it proposes | Source and date | Status | Scale | What to learn |
|---|---|---|---|---|---|---|
| **smart-crop-advisory-farmer-innovation** | India/GitHub | Proposed software combining soil, weather, crop requirements, and recommendations. | `https://github.com/VenkyVyshu656/smart-crop-advisory-farmer-innovation`, accessed 2026-08-16 | Repository/prototype | No deployment evidence found | Useful feature checklist; not evidence of operational prior art or cyclone recovery. |
| **WeatherWise Hack 2026** | Global online student event | General weather forecasting, disaster preparedness, and emergency-response challenge. | `http://weatherwise-hack.devpost.com/`, May 3-15, 2026 | Ended hackathon | 207 participants and 3 non-cash prizes were listed | Shows crowded idea space around warning apps, but not a farm-profile or SMS/IVR implementation. |
| **UW Databricks Weather-to-Yield Hackathon** | United States | Student anomaly detection and yield simulation from weather signals. | `http://uw-databricks-hackathon.devpost.com/`, February 28, 2026 | Ended hackathon | 93 participants listed | Relevant to offline validation and yield impact, not low-literacy disaster delivery. |
| **GitHub agriculture/farmer topic projects** | Global | Numerous apps mention weather, crop recommendation, irrigation, disease detection, and occasional flood alerts. | `https://github.com/topics/agriculture`, accessed 2026-08-16 | Ideas/code fragments | Repository-specific deployment usually absent | Code can accelerate UI or model experiments, but topic tags are not evidence of users, accuracy, licensing compatibility, or maintained integrations. |

**Inventory insight:** the idea space is crowded, while the deployment gap remains large. Novelty by feature list is weak; novelty by governed integration, local action quality, accessibility, and measured outcomes is much stronger.

## 3. COVERAGE TABLE

Grades assess this sweep, not the inherent quality of a data family: **A** means strong primary-source coverage and clear implementation implications; **D** means little reliable evidence.

| Source family | Useful hits retained | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| Direct farm-weather advisories | 9 strong or near-direct systems | Most pages omit post-disaster logic, active-user counts, or outcome evaluation | **B** |
| Low-literacy SMS/IVR delivery | mKisan, Viamo, Farmerline, Esoko evidence | Voice completion rates, language QA, cost per reached farmer, and accessibility testing rarely public | **B** |
| Digital soil maps | SoilGrids, AfSIS, SSURGO, LUCAS, HWSD | China-specific open high-resolution access remained unclear; maps are not plot tests | **A** |
| Cropland/crop-type layers | WorldCover, Copernicus HRL, WaPOR, CDL, GFSAD, GLAD | Search results often confused global cropland extent with current crop type; Europe/US products were frequently misrepresented as global | **A** |
| Farmer registries/profiles | Krushak Odisha, e-Chasa, AgriStack, IACS/LPIS, FSA, KIAMIS, ABARES | Person-level data are appropriately restricted; public APIs and profile schemas are uneven | **B** |
| Weather/reanalysis | IMD, POWER, ERA5-Land, CHIRPS, AEMET, BOM | Coarse grids are often marketed as hyperlocal; operational IMD API terms remain a partnership issue | **A** |
| Disaster and replay data | GDACS, GloFAS-GFM, Copernicus EMS, IMERG, USGS | Forecast, detection, activation mapping, and archive products are often conflated | **A** |
| Anticipatory-action frameworks | FAO and IFRC | Strong trigger/action governance, weak farm-level digital-delivery detail | **B** |
| Farm-data blockchain/cooperatives | AgriDigital, GrainChain, ripe.io | Heavy marketing, few comparable outcome metrics, unclear current status for ripe.io | **C** |
| Repositories/hackathons/forums | 4 retained groups | High duplication, aspirational README files, missing deployment and evaluation | **C** |
| Failure and counterevidence | RCT, GSMA/agent-network evidence, dead-looking services | Shutdown reasons and unit economics are rarely disclosed | **C** |

The broad data-layer families merit A grades because student-accessible inputs and their limitations are clear. The direct-match family remains B because operational detail is incomplete precisely where KrishiSetu's claim is strongest: current farm profile, hazard-specific timing, post-event recovery, and closed-loop voice delivery.

## 4. WHAT IS MISSING

### 4.1 A complete state machine from warning to recovery

No reviewed product publicly documented the full sequence:

`official alert -> affected farm intersection -> crop/stage action -> SMS and IVR delivery -> acknowledgement -> observed impact -> recovery advice -> case closure`.

Most systems stop after publication or one-way delivery. KrishiSetu should model an event as a state machine, with explicit transitions such as WATCH, PREPARE, PROTECT, SHELTER, ALL-CLEAR, ASSESS, RECOVER, and CLOSED. Each message must record the trigger, versioned rule, farm facts used, language, delivery result, and next check time.

### 4.2 A trustworthy current-crop layer

Global imagery identifies probable cropland, not necessarily the farmer, crop, sowing date, variety, stage, irrigation, livestock, stored inputs, or harvest readiness. WorldCover's 10 m product is global but dated, while SoilGrids and ERA5-Land are much coarser [14][35][21]. The missing asset is a seasonally refreshed, consented profile joined to parcel geometry. e-Chasa is therefore strategically more valuable than adding another global map.

### 4.3 Action cards with agronomic and safety accountability

A generic language model can produce plausible but unsafe instructions. The white space is a reviewed action-card library indexed by hazard, lead time, crop, stage, soil drainage, irrigation, livestock, asset, and district. It should encode contraindications, such as not asking a farmer to enter a flooded field, and distinguish agronomic guidance from emergency instructions issued by Odisha authorities.

### 4.4 Closed-loop voice evidence

An outbound call is not accessibility. The missing evidence includes completion by gender and language, repeat requests, keypad errors, shared-phone risks, call cost, network failure, and whether the farmer acted. Trust and low digital literacy are documented scaling barriers in agent-mediated services; a human extension or call-center escalation path is part of the product, not an optional support feature.

### 4.5 Data governance for emergency use

Registries are generally not public because phone numbers, identity, land tenure, and crop declarations are sensitive. KrishiSetu needs purpose limitation, field-level consent, role-based access, retention rules, grievance correction, offline-device security, and an emergency-access policy. A hackathon demo should use synthetic profiles or an explicitly consented cohort, not scraped registry data.

### 4.6 Outcome validation

The missing benchmark is not message accuracy but avoided loss. Replay historical Odisha cyclones and floods using archived alerts, IMERG/CHIRPS rainfall, GDACS events, Sentinel-1 inundation, and crop calendars. Then prospectively measure delivery, comprehension, action adoption, false alarms, crop loss, recovery time, and unequal reach. This turns a feature bundle into defensible evidence.

## 5. LESSONS

### Meghdoot and mKisan: distribution exists, urgency logic does not

**What worked:** Meghdoot demonstrates institutional production of contextual district-and-crop advice, and mKisan demonstrates government-scale messaging where mobile internet is weak [6][8]. The mechanism is organizational: experts own advisory content while a common channel distributes it.

**What is missing or can fail:** A twice-weekly bulletin is too slow for changing cyclone tracks. SMS alone can exclude non-readers, shared-phone users, and people whose local crop names differ from official terminology. **Recommendation:** consume approved agronomic content and government channels where possible, but add event-driven rule evaluation, voice, acknowledgement, retries, and district control-room override.

### BAMIS and anticipatory action: institutional joining beats one giant AI

**What worked:** BAMIS links meteorology, water, and extension bodies [3]. FAO and IFRC formalize a related causal mechanism: a forecast crosses a threshold, which activates a pre-agreed intervention before impact [5][9].

**What can fail:** Dashboards do not guarantee that a named farmer receives or understands an action before the deadline. Forecast-based financing acts at community/program scale and does not by itself select crop-stage advice. **Recommendation:** build small, auditable adapters around authoritative agencies. Keep AI downstream of the official trigger and upstream of human-approved templates.

### Farmerline, Viamo and Esoko: trust is a delivery feature

**What worked:** These services combine farmer segmentation, local content, basic-phone delivery, and, in Esoko's case, agent networks. Agents mitigate low literacy and trust barriers that purely digital channels struggle to overcome.

**What can fail:** Profile staleness, wrong language, one-way messages, donor-funded pilots, and weak willingness to pay can undermine scale. Company-reported farmer counts also do not prove sustained use or loss reduction. **Recommendation:** enroll through trusted local actors, allow IVR correction of crop/profile facts, expose a helpline, and report verified successful deliveries rather than registered numbers.

### SoilGrids, WorldCover and ERA5-Land: coverage is not precision

**What worked:** Their global coverage, machine access, and permissive terms make them ideal for prototypes. SoilGrids includes uncertainty-aware modeled properties at 250 m, WorldCover identifies broad land cover at 10 m, and ERA5-Land provides a long hourly history [35][14][21].

**What can fail:** A model may falsely label coarse interpolated data as "your farm's soil" or "hyperlocal weather." **Recommendation:** label provenance and resolution in the profile, expose confidence, and ask the farmer or extension worker to confirm high-impact facts.

### GDACS, GloFAS-GFM and IMERG: separate warning, observation and replay

**What worked:** GDACS is a free event-index API; GFM maps observed flood extent from SAR; IMERG supplies rainfall histories. These represent three different evidence stages.

**What can fail:** Treating post-acquisition flood detection as advance warning creates false lead time. SAR can also have acquisition gaps and classification masks [20]. **Recommendation:** use IMD for authoritative warning, GDACS for cross-check/event indexing, rainfall for accumulation, and GFM/Copernicus EMS for post-event prioritization and labels.

### Krushak Odisha and e-Chasa: integrate, do not duplicate

**What worked:** Odisha already has farmer scale and a stated farmer/crop survey layer [10][4]. The mechanism is a persistent identity and seasonal record that multiple services can reuse.

**What can fail:** Unauthorized scraping, ambiguous land tenure, stale crops, duplicate phone numbers, and opaque consent can make personalization harmful. **Recommendation:** prototype against synthetic adapters, define a minimal API contract, and seek formal data-sharing approval. Cache only fields needed for the active event.

### AgriDigital and GrainChain: workflow survived the hype

**What worked:** Current offerings emphasize transactions, inventory, payments, traceability, and shared records. These are repeated business processes with clear owners.

**What did not become the visible core:** Public pages no longer make blockchain the main user value proposition. That does not prove technical abandonment, but it shows that buyers care about workflow outcomes. **Recommendation:** use conventional databases, signed event logs, and interoperable IDs. Add distributed-ledger technology only if independent agencies must write to a shared log without a trusted operator.

## 6. REAL-vs-FILLER

| Classification | Entries | Decision rule |
|---|---|---|
| **Real operational public infrastructure** | IMD Agromet, mKisan, Krushak Odisha, e-Chasa, AgriStack, BAMIS, IACS/LPIS, FSA records, KIAMIS | Government or institutional systems with live portals, defined administrative owners, or active public-service roles. Access may be restricted. |
| **Real downloadable data products** | SoilGrids, SSURGO, LUCAS, HWSD, WorldCover, WaPOR, CDL, GFSAD30, GLAD, POWER, ERA5-Land, CHIRPS, GDACS, GFM, EMS, IMERG | Primary documentation gives a dataset, access path, coverage, and at least part of its specification. |
| **Real commercial or nonprofit platforms, adjacent rather than exact** | Farmerline, Viamo, Ignitia, Arable, PlantVillage, AgriDigital, GrainChain | Current first-party presence and concrete products exist, but public claims do not establish the full KrishiSetu chain. |
| **Real frameworks/programs, not farmer-facing products** | FAO anticipatory action, IFRC forecast-based action, WFP-style climate-risk monitoring | Operational concepts and programs exist, but they are not proof of an Odisha-ready farm advisory service. |
| **Research/pilot/idea** | FAMEWS in some deployments, smart-crop-advisory GitHub repository, WeatherWise Hack, UW Databricks hackathon, generic GitHub topic projects | Useful design or code evidence, but no verified sustained deployment, user base, or outcome evidence. |
| **Marketing-heavy or status-unverified** | ripe.io, My Farm Info, unsourced "AI hyperlocal" products, aggregator profiles | Current first-party operating evidence, comparable scale, methodology, or outcome evidence was absent. Do not cite these as strong prior art. |
| **Dead project versus completed project** | AfSIS 2009-2016 is a completed project with surviving outputs, not necessarily a failed service [16]. My Farm Info and ripe.io are status-unverified, not proven shutdowns. | Do not convert a stale website or ended grant into a failure claim without evidence. |

The key distinction is between **a real data product** and **a real farmer outcome**. A downloadable map can be technically real but irrelevant to current crop identity; a live company can be real but supported only by marketing claims about accuracy or reach.

## 7. NOISE LOG

| Searched/discarded item | Why it was discarded or demoted |
|---|---|
| Generic PAGASA, BOM, AEMET and national weather pages | Real weather services, but search results did not show farm profiles, crop actions, both pre/post phases, or low-literacy delivery. Retained only as regional API patterns where appropriate. |
| FAO Food Security Risk Monitor and broad hunger dashboards | Monitor regional food-crisis risk, not named-farm cyclone/flood actions. |
| Generic weather and agriculture GitHub topic pages | High duplication; README features do not establish working code, license compatibility, deployment, accuracy, or users. |
| WeatherWise Hack challenge page | A real event but not itself a submitted farm system. Retained under ideas-only, not direct prior art. |
| RocketReach profile for My Farm Info | Secondary aggregator with implausible/unverifiable company metrics and no confirmed current product. Used only to flag a lead, not substantiate differentiation. |
| Search-result claims that Copernicus has a global 10 m crop-type product | The reviewed 10 m crop-type layer is European. WorldCover is global at 10 m but broad land cover, not crop type. |
| WaPOR as an Odisha layer | Strong free infrastructure, but documented coverage is Africa and the Near East [15]. |
| USDA CDL, SSURGO and FSA records as deployable India data | Excellent US analogues with no Odisha coverage; FSA personal/operational records are also restricted. |
| LUCAS points as village soil truth | EU/UK only, and its own documentation warns against treating samples as field-representative [36]. |
| GloFAS Global Flood Monitoring as a flood forecast | GFM is near-real-time observed flood mapping from Sentinel-1, not advance prediction [20]. |
| Company-reported reach and accuracy | Retained only with attribution. Registrations, messages sent, and claimed forecast accuracy are not equivalent to active use or avoided crop loss. |
| "Blockchain for trust" articles | Mostly conceptual or vendor-authored. No evidence showed that blockchain improves cyclone advice, IVR accessibility, or farm-loss outcomes. |
| Future-dated or unverified event claims encountered in search | Omitted unless supported by a primary page and relevant to the inventory. |

This noise is informative. The most common false positive was a system matching two nouns, such as "farm" and "weather," while lacking the operational chain, accessibility, or disaster timing required by the problem.

## 8. VERDICT: SYNTHESIS

### Comparative synthesis

| Dimension | Government agromet systems | Commercial digital advisory | Humanitarian anticipatory action | Open geospatial data | Registries | KrishiSetu target |
|---|---|---|---|---|---|---|
| Core mechanism | Experts publish area/crop bulletins | Segment users and deliver content | Forecast threshold releases pre-agreed action/resources | Measure or model land, soil, rainfall, or flood | Persist identity, parcel, crop, and eligibility | Join all five mechanisms around one event and farm |
| Scope | District/state/national | Product- and market-dependent | Community/program scale | Pixel, point, grid, or event footprint | Person/holding/parcel | Named consented farm plus village aggregation |
| Time horizon | Routine forecast cycle | Routine seasonal decisions | Before impact | Historical, near-real-time, or snapshot | Multi-season administrative record | Hours before impact through recovery closure |
| Main strength | Authority and agronomic ownership | Usability and channel operations | Trigger discipline | Reproducibility and replay | Personalization | Actionable timing and continuity |
| Main trade-off | Slow cycles and limited feedback | Proprietary claims and uncertain economics | Often not crop-specific | Resolution and classification error | Privacy and stale records | Integration burden, safety review, consent, and false alarms |
| Evidence base | Operational bulletins | Company cases and some evaluations | Program frameworks and cases | Primary technical specifications | Administrative systems | Must still be demonstrated through Odisha replay and pilot outcomes |

The non-obvious tension is that **more data can reduce trust** when coarse estimates are presented as farm facts. Conversely, the least glamorous components - verified crop identity, a human-reviewed action card, voice retries, and a provenance log - create more defensible value than an additional AI model. Arable shows the benefit of a unified field picture [49]; FAO and IFRC show why triggers must map to pre-agreed actions [5][9]; Odisha's own systems supply the identity/crop starting point [10][4].

### Honest differentiation claim

Use this wording:

> **Based on a global sweep of operational advisory platforms, public farm registries, open soil/crop/weather/disaster datasets, commercial farm-data systems, research prototypes, repositories, and hackathons, we found no documented operational system that combines an authorized Odisha farmer-and-current-crop profile with official IMD cyclone/flood triggers, crop-stage-specific pre-event and post-event action cards, closed-loop SMS plus IVR delivery for low-literacy users, and historical event replay in one auditable workflow. KrishiSetu differentiates through this Odisha-specific integration and validation, not through any individual component.**

Do **not** claim:

- first AI agricultural adviser;
- first hyperlocal farm-data platform;
- first weather-to-crop advisory;
- first SMS, voice, or offline farmer service;
- first anticipatory-action system;
- first use of satellite flood or soil data; or
- legally novel/patentable without a formal patent and non-public prior-art search.

### Build decision

For the competition prototype, build a modular evidence pipeline:

1. **Synthetic or consented farm profile adapter** matching Krushak Odisha/e-Chasa identifiers.
2. **Official-alert adapter** for IMD bulletins, with GDACS only as cross-check/index.
3. **Free enrichment cache** using SoilGrids, WorldCover/GFSAD, ERA5-Land/CHIRPS, IMERG, and Sentinel-1/GFM.
4. **Versioned action-card engine**, with agronomist approval and explicit contraindications.
5. **SMS plus Odia IVR state machine**, including retry, acknowledgement, profile correction, and human escalation.
6. **Replay harness** for at least one historical cyclone and flood, measuring lead time, targeting precision, delivery, comprehension, action adoption, false alarms, and simulated avoided loss.

That prototype directly demonstrates the white space. A larger model, blockchain layer, or custom sensor network should be deferred until the team proves that the right farmer receives, understands, and acts on the right advice at the right time.

## References

1. *Agriculture - Viamo*. https://viamo.io/category/agriculture
2. *Meghdoot - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en-US&id=com.aas.meghdoot
3. *Background - Bangladesh Agro-Meteorological Information ...*. https://www.bamis.gov.bd/en/page/introduction
4. *Crop Survey*. https://echasa.odisha.gov.in/
5. *Anticipatory action | FAO Emergency and Resilience*. https://www.fao.org/emergencies/our-focus/anticipatory-action/en
6. *‎Meghdoot App - App Store*. https://apps.apple.com/us/app/meghdoot/id1474048155
7. *Digital X Solution: Ignitia*. http://digitalx.undp.org/catalogs/ignitia.html
8. *mKisan: A Portal of Government of State Base Services for ...*. https://mkisan.gov.in/Home/AboutPushSMS
9. *Early warning, early action | IFRC*. https://www.ifrc.org/early-warning-early-action
10. *Krushak Odisha Portal*. https://krushak.odisha.gov.in/
11. *NASA POWER | Page Not Found*. https://power.larc.nasa.gov/docs/tutorials/service-data-request/api
12. *High Resolution Layer Croplands — Copernicus Land Monitoring Service*. https://land.copernicus.eu/en/products/high-resolution-layer-croplands
13. *AfSIS – Africa Soil Information Service*. https://africasoils.info/
14. *Land cover (Global - 10m - 2021) - ESA WorldCover - Datasets - "FAO catalog"*. https://data.apps.fao.org/catalog/iso/8cf69f76-1be0-4339-a0b0-18a93c7f4760
15. *Geospatial Information*. https://www.fao.org/aquastat/en/geospatial-information/wapor
16. *Africa Soil Information Service (AfSIS)*. https://isric.org/projects/africa-soil-information-service-afsis
17. *REST entry page*. https://rest.isric.org/
18. *Gdacs Api Quickstart V1*. https://www.gdacs.org/Documents/2025/GDACS_API_quickstart_v1.pdf
19. *IMERG: Integrated Multi-satellitE Retrievals for GPM | NASA Global Precipitation Measurement Mission*. https://gpm.nasa.gov/data/imerg
20. *Global Flood Monitoring | Copernicus EMS - Global Flood Awareness System*. https://global-flood.emergency.copernicus.eu/react/technical-information/glofas-gfm
21. *ERA5-Land hourly data from 1950 to present*. https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview
22. *Digital tools for rural agriculture extension: Impacts of ...*. https://onlinelibrary.wiley.com/doi/full/10.1002/jaa2.42
23. *Leveraging agent networks in Ghana to improve digital ...*. https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/blog/leveraging-agent-networks-in-ghana-to-improve-digital-agriculture-service-delivery-to-farmers
24. *GrainChain*. https://www.grainchain.io/
25. *PlantVillage Nuru - fao.org*. https://www.fao.org/in-action/remote-sensing-for-water-productivity/applications-and-uses/applications-catalogue/product-detail/PlantVillage-Nuru_1331767/en
26. *Soil Survey Geographic Database (SSURGO) | Natural Resources Conservation Service*. https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo
27. *Farm survey data - DAFF*. https://www.agriculture.gov.au/abares/research-topics/surveys/farm-survey-data
28. *WorldCover | WORLDCOVER*. http://esa-worldcover.org/en
29. *Global cropland expansion in the 21st century | GLAD*. https://glad.umd.edu/dataset/croplands
30. *Farmer Registry*. https://agristack.gov.in/assets/registries/farmerRegistry/farmer_registry_faqs.pdf
31. *WeatherWise Hack: Build smart weather & disaster solutions that help people predict, prepare, and respond in real time. - Devpost*. http://weatherwise-hack.devpost.com/
32. *FAO-FAMEWS - Datasets - "FAO catalog"*. https://data.apps.fao.org/catalog/dataset/fao-famews
33. [
        Global Food Security Analysis-Support Data Project
    ](https://www.usgs.gov/apps/croplands/home)
34. *GitHub - VenkyVyshu656/smart-crop-advisory-farmer-innovation ...*. https://github.com/VenkyVyshu656/smart-crop-advisory-farmer-innovation
35. *SoilGrids - global gridded soil information – SoilGrids Documentation*. https://docs.isric.org/globaldata/soilgrids
36. *LUCAS 2018 TOPSOIL data - ESDAC - European Commission*. https://esdac.jrc.ec.europa.eu/content/lucas-2018-topsoil-data
37. *NASA POWER | API Pages*. https://power.larc.nasa.gov/api/pages
38. *Member State Geoportals (including some IACS data)*. https://agridata.ec.europa.eu/extensions/iacs/iacs.html
39. *AEMET OpenData - Agencia Estatal de Meteorología - AEMET. Gobierno de España*. https://www.aemet.es/es/datos_abiertos/AEMET_OpenData
40. *USDA - National Agricultural Statistics Service - Research and Science - CropScape and Cropland Data Layer - Announcements*. https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php
41. *AgriDigital Platform | Buy, sell, track and manage grain inventory to unlock growth opportunities.*. https://www.agridigital.io/agridigital-platform
42. *AgriDigital | Australia's leading grain management software*. https://www.agridigital.io/
43. *Farmerline – Farmerline*. https://farmerline.co/
44. *grainchain.com*. https://www.grainchain.com/
45. *Harmonized world soil database v2.0 | FAO SOILS PORTAL | Food and Agriculture Organization of the United Nations*. https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en
46. *CHIRPS: Rainfall Estimates from Rain Gauge and Satellite Observations | Climate Hazards Center - UC Santa Barbara*. https://www.chc.ucsb.edu/data/chirps
47. *http://arable.com/products*. http://arable.com/products
48. *http://arable.com/news/google-and-arable-collaborate-to-bring-innovative-water-stewardship-solution-to-nebraska-agriculture*. http://arable.com/news/google-and-arable-collaborate-to-bring-innovative-water-stewardship-solution-to-nebraska-agriculture
49. *http://arable.com/solutions/water-sustainability*. http://arable.com/solutions/water-sustainability
