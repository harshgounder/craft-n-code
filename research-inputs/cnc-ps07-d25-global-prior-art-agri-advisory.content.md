# Global Prior Art and White Space for KrishiSetu

Scope: non-Indian systems only. "Direct" below means a close functional analogue, not a complete duplicate. Page dates are shown where the source exposed one; otherwise "n.d.; accessed 2026-08-16" is used. Scale figures are reported, not independently audited.

## 1. EXECUTIVE SUMMARY

- **No complete duplicate was verified**: the sweep found systems that join hazard information to crop advice and low-tech delivery, but none that demonstrably closes all six links - official hazard ingest, hyperlocal farm profile, crop-stage action, SMS/IVR/offline delivery, pre-event preparation, and post-event agronomic recovery. Even the closest systems omit a verified recovery loop [14][33][25]. -> KrishiSetu should claim integration novelty, not novelty for any individual component.
- **BaKhabar Kissan is the closest commercial analogue**: it reports 15.8M+ users and 300+ weather stations, while its documented service combines land/crop/livestock/location profiles, multilingual adaptive IVR, SMS/VMS disaster alerts, localized weather, satellite field analysis, and expert escalation [55][14]. -> Differentiate on the missing event-specific pre/post protocol and measured loss reduction.
- **BAMIS is the closest public disaster-crop analogue**: Bangladesh advisories tell farmers to harvest before rain, drain fields, repair bunds, avoid inputs, brace banana and horticultural crops, or seek shelter before cyclones [33]. -> Treat its concise action language as a content benchmark, but add farm-profile selection, two-way voice, and recovery stages.
- **Personalization is already prior art**: PlantVillage can use crop, location, and planting date to generate advice, while iCow describes analyzing farm data and returning relevant feedback by SMS or notification [25]. -> Do not claim "AI-personalized farm advice" alone as differentiation.
- **Low-literacy delivery is also established**: Esoko uses SMS, voice SMS, and call centers; Jokalante uses SMS, voice, USSD, and a voice chatbot; BaKhabar Kissan adapts IVR to farmer profile and language [5][14]. -> Make voice an operationally tested fallback with delivery receipts and human escalation, not a demo feature.
- **Humanitarian systems prove trigger discipline, not agronomy**: WFP can release finance and messages before a forecast shock, R4 reports 550,000 households reached in 18 countries, and Africa RiskView estimates drought-response costs at first-level administrative resolution [10][30][2]. -> Borrow their pre-agreed trigger and audit logic, then translate it into plot-level crop actions.
- **The technical stack can be assembled from proven layers**: FarmBeats moved into Azure Data Manager for Agriculture; CommCare and TaroWorks show offline-first field case management; Arable combines in-field weather, crop, soil, and irrigation sensing [6][16][59]. -> Build KrishiSetu as an interoperable orchestration layer rather than recreating every sensor, registry, and messaging primitive.
- **Deaths matter**: Gro Intelligence closed after capital shortages despite raising about $117M, aWhere is listed as deadpooled, and WeFarm closed operations in 2022 after difficulty scaling under challenging market conditions [44][38][51]. -> A public-extension or B2G funding path, cost-per-active-farmer target, and continuity plan are product requirements.
- **The defensible white space is the recovery state machine**: USDA and FAO have deep recovery knowledge, but it sits apart from personalized warning channels; advisory platforms have channels and profiles, but generally stop before structured post-event diagnosis, salvage, replanting, soil/water safety, claims, and follow-up [9][29]. -> Make post-disaster recovery a first-class, evidence-tracked workflow.

## 2. WORLDWIDE INVENTORY

### Direct matches

These are the closest functional matches. None is a verified end-to-end duplicate.

| Name | Country | What it does | Named source, URL + date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| BaKhabar Kissan | Pakistan | Farmer profiles, localized weather, disaster alerts, targeted crop advice, satellite field analysis, adaptive IVR, SMS/VMS, app, and call center [14] | Allied Bank, https://www.abl.com/business-banking/agriculture-financing/bakhabar-kissan/, updated 2025-12-26 | Live | 15.8M+ reported users; 300+ weather stations [55] | Closest architecture; add explicit event playbooks, recovery, and outcome evidence. |
| BAMIS | Bangladesh | Forecast-linked SMS crop actions for rain, gusts, flood drainage, and cyclone shelter; advice is crop and field-condition specific [33] | DAE/BAMIS, https://www.bamis.gov.bd/en/alert/nation/, advisories dated 2019; main project page says expiry 2024-12-31 | Legacy service/page reachable; current program status unclear | Not disclosed | Use terse imperative actions; avoid BAMIS's unclear personalization, scale, and post-event continuity. |
| PlantVillage | Multi-country, Africa/Asia/Americas | Uses crop, location, planting date, soil/satellite and forecast data; sends advice through app, SMS, TV, and social extension networks [25] | Penn State, https://plantvillage.psu.edu/, n.d. | Live projects; AI page says beta | Extension officers across 12 countries; larger reach is aspirational [25] | Three-field onboarding is a strong minimum; add cyclone/flood event states and recovery. |
| m-Omulimisa AgroMet Advisory | Uganda | Converts weather forecasts into farmer-friendly decisions; reachable by app and USSD [12] | m-Omulimisa, https://m-omulimisa.com/category/weather-information, posts through 2026-05 | Live | Not disclosed | Weather must be translated, not forwarded; document exact actions and impact. |
| Esoko Digital Farmer Service | Ghana/Africa | Weather forecasts, agronomic advice and market information over SMS, voice SMS, and call centers [5] | FAO STI Portal, http://sti-portal.fao.org/innovations/esoko-digital-farmer-service, 2026-06-12; https://www.esoko.com/ | Live/pivoted last-mile platform | Not disclosed in reviewed source | Multi-channel reach is mature prior art; disaster phasing is not. |
| Farmerline/Mergdata | Ghana, multi-country | Local-language, offline-capable farmer and field-agent platform with training, inputs and market services [23] | Farmerline, https://farmerline.co/, n.d. | Live | 2.3M+ farmers, 3,000+ partners, 50 countries [23] | Offline field operations and local agents can sustain the last mile after networks degrade. |
| iCow | Kenya | Analyzes partner and farm data and returns relevant feedback by SMS or notifications; also operates a farmer marketplace | iCow, https://icow.co.ke/, n.d. | Live site; product mix has evolved | 150,000 users in a historical scale case | Farm-data-to-SMS is not new; hazard triggers and recovery remain open. |
| Jokalante | Senegal | Multilingual agricultural and climate information via SMS, voice messages, USSD, and voice chatbot | IETP, http://ietp.com/en/company/jokalante, portfolio entry 2025 | Live, seed-funded | Team of 19; farmer count not disclosed | Voice plus two-way interaction is the right inclusion pattern. |
| KALRO Kenya Agricultural Observatory Platform | Kenya | Real-time, location-specific weather, soil-health and crop-management advisories | KALRO, https://keep.kalro.org/, n.d. | Live web platform | Not disclosed | A government research platform can own localized agronomy; KrishiSetu should add disaster workflow and voice. |
| Zambia e-extension SMS advisory | Zambia | Delivers weather and agronomic information to rural smallholders by SMS | CGIAR report, https://cgspace.cgiar.org/bitstreams/315049cd-588f-490e-a3d0-787efe3aaded/download, n.d. | Evaluated program | Not disclosed in search record | SMS can carry combined weather and agronomy, but evidence must test comprehension and action. |

**Direct-match takeaway:** BaKhabar Kissan proves almost every front-end and data primitive, while BAMIS proves hazard-specific agricultural actions. The unoccupied intersection is a verified, farm-profiled, two-phase disaster workflow with structured recovery and outcome tracking.

### Indirect systems

| Name | Country/region | What it does | Named source, URL + date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| FarmBeats / Azure Data Manager for Agriculture | US/global | Low-cost sensors, drones, edge/ML and unified farm data for predictive or prescriptive solutions [6][54] | Microsoft Research, https://www.microsoft.com/en-us/research/project/farmbeats-iot-agriculture, n.d. | Research transitioned to product; Azure FarmBeats retired into ADMA [6] | Not disclosed | Use as a data plane, not as proof of farmer-facing disaster advice. |
| Climate FieldView | US/global | Commercial all-in-one digital farming and field decision platform [7] | Bayer Climate, https://climate.com/en-us.html, n.d. | Live | Not disclosed in reviewed page | Strong field record, weak fit for feature-phone disaster access and recovery. |
| Arable Crop Intelligence | US/global | In-field weather, plant, soil and irrigation sensing transformed into real-time crop intelligence [59] | Arable, https://www.arable.com/products and https://www.arable.com/solutions/water-sustainability, n.d. | Live | Organizations in 50+ countries [60] | Sensor fusion and irrigation precision; requires a separate alert, voice and recovery layer. |
| Gro Intelligence | Kenya-born/US | Enterprise agriculture, weather, trade and production analytics | Techpoint Africa, http://techpoint.africa/news/kenya-gro-intelligence-shuts-down, 2024 context | Dead, 2024 | About $117M raised [44] | Sophisticated analytics do not solve capital intensity or last-mile delivery. |
| aWhere | US/global | High-resolution weather-based agricultural intelligence/API | Tracxn, https://tracxn.com/d/companies/awhere/__4jgPcQybQWn4lJ9prgvFZjuxVTkvXj08t7rA0HjXnI4, 2025 profile | Deadpooled [38] | $16.6M funding reported by profile | Avoid dependence on a single proprietary forecast vendor. |
| Precision Development (PxD/PAD) | Asia/Africa | Designs and evaluates mobile agricultural information services | PxD, http://precisiondev.org/about-us, current page; scale year 2024 | Live nonprofit | 46M+ farmers reached in 2024 [15] | Optimize advice experimentally and measure production, profit and resilience, not message volume. |
| Digital Green | Kenya, Ethiopia, Nigeria, Brazil, Zimbabwe, others | Local agronomy and AI advice through farmer networks, voice, video and phones [18] | Digital Green, http://digitalgreen.org/about, timeline through 2026 | Live | FarmerChat 1.6M+ farmers and 8M+ answers [18] | Trusted language and peers drive use; reviewed evidence did not show disaster orchestration. |
| CommCare | Global | Offline-first longitudinal case and field-program platform; agriculture modules cover registration, extension, finance, logistics and outcomes [16] | Dimagi, https://dimagi.com/sectors/agricultural-programs, n.d. | Live platform | Pilot-to-national positioning; no single farmer count | Reuse its case-management pattern for event status and post-event follow-up. |
| TaroWorks | Global | Offline-first Salesforce field-operations app for nonprofits and social enterprises [57] | Salesforce AppExchange, https://appexchange.salesforce.com/appxListingDetail?listingId=a0N30000000ptbAEAQ, n.d. | Live platform | Not disclosed | Useful for extension-worker continuity; not an advisory product by itself. |
| Ethiopia 8028 Farmer Hotline | Ethiopia | Toll-free agronomic and livestock advisory hotline | ATI, https://ati.gov.et/8028-farmer-hotline/, live page 2026 | Live | Not disclosed in reviewed official page | IVR/hotline access is proven; connect it to event triggers and registered farms. |
| DigiFarm | Kenya | Agronomy/weather advice, markets, inputs, finance and loans through a digital platform | Safaricom, https://www.safaricom.co.ke/media-center-landing/frequently-asked-questions/digifarm-general, n.d. | Live | Not disclosed here | Bundled value improves retention; disaster advice should not depend on credit uptake. |
| M-Farm | Kenya | SMS price transparency, input purchasing and buyer matching [56] | FSD Kenya, https://www.fsdkenya.org/thematic-areas/digital-finance/m-farm/, n.d. | Historical; current status not verified | Not disclosed | A useful SMS commerce precedent, not hazard or agronomy prior art. |
| WeFarm | Kenya/Uganda | Peer-to-peer agricultural questions and crowdsourced answers through SMS and web [51] | Dealroom, http://app.dealroom.co/companies/wefarm, n.d. | Closed operations in 2022 [51] | Not disclosed in reviewed status source | Free peer content can spread, but weak unit economics and variable authority are risks. |
| e-Krishok | Bangladesh | Historical BIID/CIMMYT/ITC mobile service for farmers and local service providers [34] | FAO-hosted BIID deck, https://www.fao.org/fileadmin/templates/rap/files/uploads/ESF_Presentations/eKrishok_BIID.pdf, n.d. | Historical; current service not verified | Not disclosed | Mobile access alone is not evidence of hazard integration or survival. |
| Nigeria GES e-wallet | Nigeria | Mobile vouchers delivered subsidized farm inputs directly to farmers | Guardian Nigeria, https://guardian.ng/features/whither-the-e-wallet-scheme-2/, n.d. | Historical government program | Not reliably established in reviewed source | Farmer registry and entitlements can support recovery packages, but this was not an advisory system. |
| WFP Anticipatory Action | Multi-country | Pre-agreed forecast triggers release finance, mobile money and early-warning messages before shocks [10] | WFP, https://www.wfp.org/anticipatory-actions, current page | Live/scaling | Bangladesh capability cited as 350,000 people five days before flood [10] | Pre-authorize actions and budgets; WFP does not provide plot-specific crop instructions. |
| R4 Rural Resilience | 18 countries | Risk reduction, insurance, savings and credit for climate shocks | WFP, https://www.wfp.org/r4-rural-resilience-initiative, current page | Live | 550,000 households; $2.1M payouts after shocks [30] | Link recovery advice to insurance/benefits, but keep agronomy independent of payout eligibility. |
| ARC / Africa RiskView | Sub-Saharan Africa | Rainfall and crop-water models estimate drought response costs for governments at first-level administrative districts [2] | ARC, https://www.arc.int/africa-riskview, n.d. | Live institutional system | Continent-wide model coverage; farmer reach not stated | Borrow transparent trigger math; resolution and audience are too coarse for farm advice. |
| FEWS NET | Multi-country | Food-security early warning using livelihoods, markets, rainfall and remote sensing | FEWS NET, https://fews.net/, current service | Live | Multi-country; no direct farmer reach | Excellent situational intelligence, but outputs target analysts and decision-makers. |
| FAO GIEWS / ASIS / DRR | Global | Food-security and agricultural stress monitoring plus policy, preparedness and recovery knowledge [29] | FAO, https://www.fao.org/giews/en and https://asis.apps.fao.org/, current; DRR page updated 2024-06-17 | Live | Global | Use as upstream evidence and recovery content, not as the last-mile channel. |
| ACRE Africa Weather Index Cover | Africa | Location/acreage/risk-based index insurance; policy records by SMS and payouts by M-PESA | Engineering for Change, https://www.engineeringforchange.org/solutions/product/acre-africa-weather-index-covers, n.d. | Live/product listing | Not disclosed | A farm-risk profile can trigger financial recovery, but insurance is not crop guidance. |
| USDA Farmers.gov protection/recovery | US | Preparation, crop insurance, disaster assistance and recovery programs [9] | USDA, https://www.farmers.gov/protection-recovery, current | Live | National | Deep recovery content; lacks one personalized SMS/IVR pre/post flow. |
| Cornell NEWA | US Northeast | Weather-station network and science-driven IPM/crop decision tools | Cornell IPM, https://cals.cornell.edu/integrated-pest-management/risk-assessment/newa, n.d. | Live | Regional station network | Shows land-grant decision support; extreme-weather voice and recovery are outside scope. |
| My Climate View / Climate Services for Agriculture | Australia | Location-tailored climate-risk views extending decades into the future [3] | CSIRO, https://www.csiro.au/en/news/all/articles/2022/march/climate-data-for-farmers-with-the-click-of-a-button, 2022-03-03 | Live program/tool | National coverage goal; user count not disclosed | Good strategic adaptation, not urgent cyclone/flood action. |
| Climate Kelpie | Australia | Portal helping farmers find and understand climate tools | Bureau of Meteorology, https://www.bom.gov.au/watl/about/, n.d. | Live information portal | Not disclosed | Tool discovery is useful, but fragmentation is exactly what KrishiSetu should remove. |
| HortPlus MetWatch | New Zealand/Australia | Weather stations, short-range horticulture forecasts, pest/disease models and crop decision support [47] | HortPlus, https://www.hortplus.com/weather-data, n.d. | Live | Major horticultural regions; count not disclosed | Crop models plus local weather are strong; low-tech and disaster recovery remain gaps. |
| CMA Agricultural Meteorological Service | China | Seasonal services, agrometeorological-disaster monitoring/forecasting/warning, and pest/disease prevention [20] | China Meteorological Administration, https://www.cma.gov.cn/en/service/highlight/AgriculturalServices/202311/t20231123_5905105.html, updated 2025-02-21 | Live government service | National; farmer reach not disclosed | Strong upstream warning-agronomy institution; reviewed evidence does not show individual farm profiles or IVR. |
| CIMH/CariCOF | Caribbean | Regional seasonal rainfall and drought outlooks for climate-sensitive sectors | CIMH RCC, https://rcc.cimh.edu.bb/, current outlooks through 2026 | Live regional climate service | Caribbean region | Regional outlooks need a national extension and farmer-channel translation layer. |
| PICSA | Multi-country | Facilitated participatory use of climate information for farm planning | University of Reading, https://research.reading.ac.uk/picsa/picsa-practice, n.d. | Live methodology/program | Implemented in 20 countries per project page | Human facilitation improves interpretation; not a rapid event/recovery engine. |
| Fiji climate outlooks / Pacific climate services | Fiji/Pacific | Monthly and seasonal rainfall, temperature and ENSO information | Fiji Met Service, https://www.met.gov.fj/climate-services/climate-outlooks/, current | Live climate service | National/regional; direct farmer reach not disclosed | Valuable upstream forecasts; accessible crop action delivery was not verified. |

**Indirect-system takeaway:** prior art is dense at every layer - sensing, farm records, forecasts, advisory, voice, insurance, anticipatory finance, and recovery knowledge. It is sparse at the orchestration boundary between those layers.

### Ideas-only, research and open-source concepts

| Name | Country/region | What it does | Named source, URL + date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| Chenjezo Drought/Flood Alert | Malawi | Repository claims district climate-risk maps and automated SMS warnings using NASA data | GitHub, https://github.com/Walunji-Zdev05/Chenjezo-Drought-Flood-Alert, 2025 context | Open-source concept; deployment unverified | None verified | Good low-cost warning pattern; no verified crop-stage or recovery engine. |
| Community Voice EWS | IGAD/East Africa | Combines official ICPAC forecasts with crowdsourced SMS reports; no smartphone required [49] | GitHub, https://github.com/kawacukennedy/community_voice_ews, 2026 hackathon context | Prototype | None verified | Two-way reports can confirm local impact and trigger recovery triage. |
| Zindua | IGAD/East Africa | Ingests hazards, localizes SMS, records replies, and escalates unresolved help requests | GitHub, https://github.com/justuskitavi/zindua/tree/main, 2026 context | Prototype | None verified | Response coordination is a useful complement to agronomic advice. |
| NIGCOMSAT Team 7 amber-alert concept | Nigeria/Africa | Satellite-enabled cascading-climate warning concept promising seven-day harvest lead time [58] | GitHub, https://github.com/NIGCOMSAT-Accelerator/c3hkth-team7, 2026 context | Hackathon repository | None verified | Lead-time-to-action is the right framing; claims need field validation. |
| ESP32 flood-warning prototype | Research, country not established | Sensor prototype measures precipitation, water flow and level [41] | IEEE, https://ieeexplore.ieee.org/document/9044531, 2020 | Research prototype | Lab/prototype only | Local sensing is feasible; agriculture, advisory and recovery are absent. |
| IGAD Husika Hackathon brief | IGAD region | Calls for systems that turn early warning into timely action [37] | Devpost, https://igad-husika-hackathon.devpost.com/, 2026 | Challenge/idea space | No deployment | Confirms active design interest, not prior operational proof. |
| China 2026-2030 agromet plan | China | Plans field-level forecasting and short-, medium- and long-term disaster-risk warnings by 2030 [13] | ECNS/CMA plan report, https://www.ecns.cn/cns-wire/2026-07-17/detail-ihfhkrtk6177753.shtml, 2026-07-17 | Planned | National ambition | Monitor as future prior art; farmer-facing channels and recovery were not specified. |

**Ideas-only takeaway:** repositories are strongest on alert transport and weakest on validated agronomy, farmer identity, operational governance, post-event recovery, and field evidence. A polished GitHub README is not a deployed system.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---|---|---|
| Official government/agromet pages | BAMIS, ATI 8028, KALRO, USDA, CMA, Fiji Met, Cornell NEWA | Often omit reach, delivery metrics, personalization and lifecycle status | **A-** for existence/capability; **C** for impact |
| First-party platform pages | BaKhabar Kissan, PlantVillage, Farmerline, m-Omulimisa, Esoko, Microsoft, Dimagi, HortPlus | Marketing language, aspirational scale, sparse failure disclosure | **B+** |
| UN/multilateral and humanitarian sources | WFP AA, R4, ARC, FAO, FEWS NET | Target institutions or households, not individual crop decisions | **A** for trigger/scale; **C** for last mile |
| Academic and evaluation literature | FarmBeats paper, Zambia SMS study, flood-warning prototype, PICSA evidence | Many prototypes; deployment and current status decay quickly | **B** |
| GitHub and hackathons | Chenjezo, Community Voice, Zindua, NIGCOMSAT Team 7 | README claims, forks, unknown operators, no measured users | **B-** for idea discovery; **D** for operational proof |
| Startup databases and news | Gro, aWhere, WeFarm closure evidence | Secondary sourcing and inconsistent dates | **B-**, useful only for lifecycle triangulation |
| Search snippets, app stores and social pages | iCow history, MAFF app, Van-KIRAP mentions | Name collisions, SEO pages, missing scope, inaccessible local-language details | **C-/D** |
| Forums | No credible non-Indian integrated system surfaced | Generic weather-app requests and electronics demos without farmers or agronomy | **D** |

The search is strongest for named, institutional systems and weakest for local pilots, non-indexed government documents, closed commercial products, and repositories with no deployment record. Therefore the conclusion is a bounded prior-art assessment, not proof of global nonexistence.

## 4. WHAT IS MISSING

### The precise white space

The missing product is not "weather alerts for farmers" or "AI crop advice." Both are crowded. The white space is a **hazard-conditioned, farm-state workflow** with the following continuous chain:

1. **Authoritative event ingest:** IMD/CAP cyclone, flood, rainfall and wind warnings with versioning, confidence and geofenced lead time.
2. **Persistent farm twin:** village/GPS, crop and variety, sowing date/growth stage, acreage, soil/drainage, irrigation, livestock, assets, language, literacy/channel preference, and vulnerability.
3. **Action compiler:** hazard x lead time x crop stage x farm condition -> a short ranked instruction, rationale, deadline, safety guardrail and escalation path.
4. **Resilient delivery:** SMS plus adaptive IVR/voice, retry and acknowledgement, cached extension-worker mode, and printable/community-radio fallbacks.
5. **Two-phase event state:** preparedness before impact, then impact check, salvage, disease prevention, safe re-entry, replanting, soil/water remediation, input/credit/insurance linkage and repeated follow-up.
6. **Closed-loop evidence:** farmer acknowledgement, action taken, observed damage, expert override, message provenance, and measured avoided loss.

BaKhabar Kissan covers much of 1-4 but does not document 5. BAMIS demonstrates excellent pre-event crop actions but not individualized profiles or recovery. WFP/ARC/R4 cover triggers and finance but not agronomy. USDA/FAO cover recovery but not one low-tech personalized event flow. CommCare/TaroWorks can hold cases but do not generate the advice. This separation is the opportunity.

### What is specifically not white space

AI/ML, IoT sensors, satellite imagery, hyperlocal weather, farmer registration, crop calendars, SMS, IVR, local-language voice, chatbots, offline apps, disaster alerts, anticipatory cash, index insurance and post-disaster aid all have substantial prior art. KrishiSetu should not call itself the "first AI farmer alert," the "first voice crop advisory," or the "first hyperlocal agriculture platform."

## 5. LESSONS

| Strong analogue | What worked | What failed or remains weak | Why it matters for KrishiSetu |
|---|---|---|---|
| BaKhabar Kissan | One service unifies rich profiles, satellite intelligence, weather, disaster alerts, IVR/SMS and experts [14] | No documented post-event agronomic workflow or measured loss reduction | Treat it as the closest benchmark; recovery and proof, not feature count, must separate KrishiSetu. |
| BAMIS | Advice is concrete and time-bound: harvest, drain, brace, avoid inputs, shelter [33] | Public page shows old advisories and no measured reach, personalization or recovery | Build an approved action library with freshness controls and farmer-level selection. |
| PlantVillage | Minimal inputs generate tailored advice; multiple channels and extension networks widen reach [25] | Reviewed source does not show post-cyclone/flood recovery | Keep onboarding short, then enrich the profile over time. |
| Farmerline/Esoko/Jokalante | Local language, offline/voice/SMS/USSD and field agents address literacy and connectivity [23][5] | Disaster state and outcomes are not explicit | Channel diversity and trusted intermediaries are operational infrastructure, not optional UI. |
| iCow | Farm and partner data can drive relevant SMS feedback | Disaster trigger and recovery are not shown | Relevance depends on records; a generic district blast is not personalization. |
| PxD/Digital Green | Very large reach and behavioral evidence show digital advice can scale [15][18] | General advisory does not automatically become emergency guidance | A/B test comprehension and action, but never experiment with unreviewed safety-critical instructions. |
| WFP Anticipatory Action | Pre-agreed forecasts release action before impact [10] | Household cash/message is not crop-stage advice | Implement trigger thresholds, activation authority, budget and audit trail before cyclone season. |
| R4/ARC/ACRE | Risk models connect climate signals to finance or insurance [30][2] | Coarse resolution, basis risk and no full agronomic recovery flow | Link, but do not conflate, advice and financial entitlement. |
| FarmBeats/ADMA and Arable | Sensor, satellite and field-data fusion is mature [54][59] | Data platforms do not solve last-mile trust or disrupted communications | Buy or integrate the data plane; invest differentiation in decision and delivery governance. |
| CommCare/TaroWorks | Offline-first case management preserves field operations [16][57] | They are enabling platforms, not verified agronomic engines | Model every affected farm as a case with tasks, status, evidence and escalation. |
| USDA/FAO | Rich preparation, insurance, assistance and recovery knowledge exists [9][29] | Content is fragmented and not automatically selected for a specific farm | Convert authoritative recovery guidance into locally approved, stage-based micro-protocols. |
| WeFarm | SMS peer exchange removed the internet barrier [51] | Closed in 2022; cited reason was difficult scaling in challenging markets [51] | Free information needs durable payer economics and quality control. |
| Gro/aWhere | High-end weather and agriculture intelligence attracted funding and customers | Gro closed for lack of capital; aWhere is listed deadpooled [44][38] | Minimize fixed data cost, support vendor substitution, and plan public-service continuity. |

The recurring mechanism is clear: systems succeed when they reduce friction at one boundary - forecast to decision, message to farmer, risk to cash, or case to extension worker. They fail as analogues when they leave the next boundary to another institution. KrishiSetu's value is closing those handoffs while retaining human agronomic authority.

## 6. REAL-vs-FILLER

| Classification | Entries | Why |
|---|---|---|
| **Real, operational, closest analogues** | BaKhabar Kissan, PlantVillage, m-Omulimisa, Esoko, Farmerline, iCow, Jokalante, KALRO KAOP, ATI 8028, DigiFarm | Named operators and active service pages; several disclose channels or scale. They still do not prove the complete pre/post loop. |
| **Real public or humanitarian systems** | BAMIS, WFP AA, R4, ARC/Africa RiskView, FEWS NET, FAO GIEWS/ASIS/DRR, USDA, CMA, Fiji Met, Cornell NEWA | Institutional systems with real models, forecasts, finance or recovery. Most serve decision-makers or publish information rather than execute a personalized farm workflow. |
| **Real enabling infrastructure** | FarmBeats/ADMA, FieldView, Arable, CommCare, TaroWorks, My Climate View, Climate Kelpie, HortPlus | Production/research platforms with valuable components. Calling them cyclone/flood recovery systems would be marketing overreach. |
| **Real but historical, pivoted or dead** | Gro Intelligence, aWhere, WeFarm, M-Farm, e-Krishok, Nigeria GES e-wallet | Important prior art and failure evidence, but not current end-to-end competitors. Status is strongest for Gro, aWhere and WeFarm; weaker for M-Farm and e-Krishok. |
| **Research/prototype** | Chenjezo, Community Voice EWS, Zindua, NIGCOMSAT Team 7, ESP32 flood-warning prototype | Code or papers exist; field deployment, support, farmer count and outcomes were not verified. |
| **Marketing/plan rather than deployed evidence** | China 2030 plan, generic "AI crop advisory" pages, vendor directories | A roadmap or feature claim is not an operating farmer service. |
| **Not a verified system** | PAKISAMA digital advisory claim, generic Japan JA claim, "Australia ClimateKit" as an exact product, forum chatter | Searches did not locate a source supporting the claimed integrated service. They belong in the noise log, not the inventory of real competitors. |

A system counts as "real" here only when a named operator, usable service page, institutional program, code repository, or paper exists. It counts as a direct analogue only when the evidence demonstrates multiple links in the target chain. This avoids turning broad climate portals and pitch language into false competitors.

## 7. NOISE LOG

| Searched and discarded | Why discarded or downgraded |
|---|---|
| Indian services and Odisha cyclone pages | Explicitly out of scope, even when search engines ranked them highly. |
| PAKISAMA Philippines | The sweep found farmer-organization material but no verified PAKISAMA SMS/IVR weather-disaster advisory platform. |
| Generic Japan JA smart-agriculture claim | MAFF and disaster pages exist, but no named JA system with farm profiles, crop advice, warning and low-tech delivery was verified. The MAFF app is broad information distribution. |
| "Australia ClimateKit" | No exact, authoritative product match was verified. Climate Kelpie and My Climate View are the substantiated Australian analogues. |
| Generic New Zealand pastoral apps | DairyNZ pasture tools are management resources, not disaster systems. HortPlus MetWatch was retained because it has weather/crop decision support. |
| Van-KIRAP/Pacific search hits | Climate-service and multi-hazard projects exist, but reviewed results did not substantiate a farmer-profiled crop SMS/IVR workflow. Fiji Met was retained as the verified upstream service. |
| PAKISAMA, PAGASA and typhoon recovery news | PAGASA supplies weather; recovery stories describe aid and damage. Neither search set demonstrated the target integrated product. |
| RocketReach, SEO directories and name-collision pages | Employee/revenue estimates, similarly named firms, and vendor directories were not treated as capability evidence. |
| Generic ESP8266/GSM YouTube demos | They detect water and send SMS but have no farm profile, agronomy, operator or deployment evidence. One peer-reviewed prototype was retained as component research. |
| "AI crop advisory" marketing blogs | Often restated the desired architecture without a named deployment, users, dates or outcomes. |
| Social posts and Facebook-only pilots | Too weak for operational status or scale unless corroborated by an operator or institution. |
| Forums | No credible outside-India forum concept surfaced that added more than generic weather alerts or electronics advice. |
| Post-flood/cyclone digital recovery searches | Found USDA/NGO recovery guides and assistance portals, but no verified individual-farm SMS/IVR service that continued from warning into crop recovery. This negative result drives the white-space claim, with appropriate caution. |

## 8. VERDICT

### Synthesis

Across **mechanism**, commercial advisory systems personalize content and optimize engagement; humanitarian systems trigger early finance; agromet agencies forecast hazards; sensor platforms build field intelligence; recovery agencies manage aid and rehabilitation. Across **scope**, the first group reaches farmers but is usually hazard-general, while the second and third handle disasters but usually stop above the farm or before agronomic recovery. Across **trade-offs**, rich apps and sensors improve precision but raise cost and connectivity dependence; SMS/IVR widens reach but compresses nuance; centralized models provide consistency but need local agronomist oversight. Across **evidence**, reach is frequently reported, but avoided crop loss, action adherence and recovery time are rarely published.

The non-obvious tension is that the closest advisory analogue, BaKhabar Kissan, has more front-end breadth than many proposed hackathon systems, while the strongest disaster actors have the best trigger governance but the weakest crop personalization. KrishiSetu should combine those institutional strengths rather than present an LLM as the core invention.

### Honest differentiation claim

A defensible claim is:

> **"KrishiSetu unifies authoritative cyclone and flood alerts with a persistent hyperlocal farm profile to deliver crop-stage, time-bounded actions before impact and structured agronomic recovery after impact through SMS, adaptive IVR and offline extension workflows. In this non-Indian sweep, we found close systems for each component, but did not verify one operating system that closes the entire pre-to-post loop."**

Do **not** claim "world first," "first AI agricultural alert," "first hyperlocal advisory," or "first SMS/IVR service." The sweep cannot prove nonexistence, and those components have clear prior art.

### Decision-ready build implications

1. Make the **event state machine** the core product: watch, warning, 72/48/24/6 hours, impact check, 0-72 hour salvage, 3-14 day disease/replanting, and 15-60 day recovery.
2. Keep a **versioned agronomy rule base** approved by Odisha experts; use AI for retrieval, ranking, translation and dialogue, not unconstrained safety-critical prescriptions.
3. Build **channel resilience**: SMS, outbound IVR, inbound callback, retry, acknowledgement, extension-worker offline cache, and human escalation.
4. Store **action and outcome evidence**: who received what, when, in which language, whether it was understood and acted upon, damage observed, and expert overrides.
5. Integrate **recovery entitlements** without making advice conditional on insurance, credit or subsidy participation.
6. Prove differentiation with field metrics: delivery success, comprehension, action adoption, avoided loss versus comparison farms, time to recovery, false-alarm burden, and cost per actively protected farmer.

The verdict is favorable but narrow: KrishiSetu has credible architectural white space in the last-mile **continuity from warning through recovery**. Its differentiation will survive scrutiny only if the team demonstrates that continuity in real farmer workflows and measured outcomes, not merely in a feature diagram.

## References

1. *Participatory Integrated Climate Services for Agriculture (PICSA) CCAFS https://ccafs.cgiar.org › resources › tools › participatory...*. https://ccafs.cgiar.org/resources/tools/participatory-integrated-climate-services-agriculture-picsa
2. *Africa RiskView | African Risk Capacity Group*. https://www.arc.int/africa-riskview
3. *Climate data for farmers, with the click of a button*. https://www.csiro.au/en/news/all/articles/2022/march/climate-data-for-farmers-with-the-click-of-a-button
4. *Arable Crop Intelligence System Overview*. https://www.arable.com/products
5. *Esoko Digital Farmer Service*. http://sti-portal.fao.org/innovations/esoko-digital-farmer-service
6. *FarmBeats: AI, Edge & IoT for Agriculture - Microsoft Research*. https://www.microsoft.com/en-us/research/project/farmbeats-iot-agriculture
7. *Climate FieldView: Maximize Results with Our Digital Farming ...*. https://climate.com/en-us.html
8. *WeFarm*. https://weadapt.org/organisation/wefarm
9. *Protection and Recovery Programs and Resources | Farmers.gov*. https://www.farmers.gov/protection-recovery
10. *Anticipatory Action for climate shocks | World Food Programme*. https://www.wfp.org/anticipatory-actions
11. *PlantVillage Nuru: Pest and disease monitoring using AI*. https://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai
12. *Weather Information*. https://m-omulimisa.com/category/weather-information
13. *China unveils 2030 plan to strengthen agricultural weather ...*. https://www.ecns.cn/cns-wire/2026-07-17/detail-ihfhkrtk6177753.shtml
14. *BaKhabar Kissan – Agriculture Advisory by Allied Bank*. http://abl.com/business-banking/agriculture-financing/bakhabar-kissan
15. *About Us – Precision Development (PxD)*. http://precisiondev.org/about-us
16. *CommCare for Service Delivery | Case Management & ...*. https://dimagi.com/commcare/use-cases/service-delivery
17. *BaKhabar Kissan | Pakistan's Largest AgriTech & Digital ...*. https://bkk.ag/
18. *About Us | Digital Green*. http://digitalgreen.org/about
19. [
	Africa RiskView
](https://www.africariskview.org/)
20. *Agricultural Service*. https://www.cma.gov.cn/en/service/highlight/AgriculturalServices/202311/t20231123_5905105.html
21. *Zong Pakistan*. https://www.zong.com.pk/vas/bakhabar-kissan
22. *GIEWS - Global Information and Early Warning System on Food and Agriculture | Food and Agriculture Organization of the United Nations*. https://www.fao.org/giews/en
23. *Farmerline – Farmerline*. https://farmerline.co/
24. *GitHub - Walunji-Zdev05/Chenjezo-Drought-Flood-Alert: Drought & Flood Early Warning System with SMS Alerts for Smallholder Farmers in Malawi.  An  open-source web application providing real-time district-level climate risk maps and automated SMS warnings using free NASA weather data. Empowering rural communities to adapt to droughts and floods amid Malawi's 2025 climate crisis. · GitHub*. https://github.com/Walunji-Zdev05/Chenjezo-Drought-Flood-Alert
25. *PlantVillage*. https://plantvillage.psu.edu/
26. *Esoko - connecting last mile communities with services through digital innovations*. https://www.esoko.com/
27. *- TaroWorks, Powering Frontline Operations For Greater Impact*. https://taroworks.org/
28. *Background - Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en/page/introduction
29. [
	Resilient livelihoods: Disaster risk reduction for food and nutrition security
](https://www.fao.org/policy-support/policy-themes/disaster-risk-reduction-in-agriculture/Resilient-livelihoods-Disaster-risk-reduction-for-food-and-nutrition-security)
30. *The R4 Rural Resilience Initiative | World Food Programme*. https://www.wfp.org/r4-rural-resilience-initiative
31. *Farmbeats Webpage 1*. https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf
32. *Agriculture & Farmer Program Software | CommCare*. https://dimagi.com/sectors/agricultural-programs
33. *SMS Advisory - Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en/alert/nation/
34. *eKrishok: A Sustainable Business Model*. https://www.fao.org/fileadmin/templates/rap/files/uploads/ESF_Presentations/eKrishok_BIID.pdf
35. *Weather Apps and Services for Farmers Croptracker https://www.croptracker.com › Blog*. https://www.croptracker.com/blog/weather-apps-and-services-for-farmers.html
36. *K. M. Golam Dastogeer, PhD (Murdoch), Postdoc (TUAT & ...*. http://scholar.google.com/citations?hl=en&user=cX2Z0wUAAAAJ
37. *IGAD Hackathon 2026: Smarter Early Warning, Stronger ...*. https://igad-husika-hackathon.devpost.com/
38. *aWhere - 2025 Company Profile & Team - Tracxn*. https://tracxn.com/d/companies/awhere/__4jgPcQybQWn4lJ9prgvFZjuxVTkvXj08t7rA0HjXnI4
39. *AgTech's $120M Collapse*. https://newsletter.failory.com/p/agtechs-120m-collapse
40. *Ministry of Agriculture, Forestry and Fisheries - 農林水産省*. https://www.maff.go.jp/primaff/e/index.html
41. *A Prototype for Flood Warning and Management System ...*. https://ieeexplore.ieee.org/document/9044531
42. *BIID Foundation*. https://biid.org.bd/
43. *iCow – iCow Kenya home*. https://icow.co.ke/
44. *Kenya-based agritech Gro Intelligence to shut down two months after slashing headcount*. http://techpoint.africa/news/kenya-gro-intelligence-shuts-down
45. *Crop Disaster Recovery | Federal Help For Farmers & Ranchers*. https://cropdisasterrecovery.com/
46. *Pasture management for growth and quantity*. https://www.dairynz.co.nz/resources/tools/feedright-tutorials/pasture-management
47. *Weather Data Solutions | HortPlus | We Build Weather Insight ...*. https://www.hortplus.com/weather-data
48. *aWhere*. https://www.linkedin.com/company/awhere-inc-
49. *GitHub - kawacukennedy/community_voice_ews: Community Voice ...*. https://github.com/kawacukennedy/community_voice_ews
50. *The R4 Rural Resilience Initiative | WFP Innovation*. https://innovation.wfp.org/project/r4-rural-resilience-initiative
51. *WeFarm company information, funding & investors | Dealroom.co*. http://app.dealroom.co/companies/wefarm
52. *Ministry of Agriculture, Forestry and Fisheries - 農林水産省*. https://www.maff.go.jp/e/
53. *Resource Guide: Disaster Recovery for Small & Mid-Sized ...*. https://carolinafarmstewards.org/resources/disaster-recovery-for-small-mid-sized-organic-operations-resource-guide
54. *Announcing Microsoft Azure Data Manager for Agriculture ...*. https://azure.microsoft.com/en-us/blog/announcing-microsoft-azure-data-manager-for-agriculture-accelerating-innovation-across-the-agriculture-value-chain
55. *About Bakhabar Kissan — Pakistan's Smart Agriculture Platform*. http://bkk.ag/about-us
56. *M-Farm - Financial Sector Deepening Kenya (FSD Kenya)*. https://www.fsdkenya.org/thematic-areas/digital-finance/m-farm/
57. *TaroWorks: Use Salesforce Offline for Field Operations ...*. https://appexchange.salesforce.com/appxListingDetail?listingId=a0N30000000ptbAEAQ
58. *GitHub - NIGCOMSAT-Accelerator/c3hkth-team7: NIGCOMSAT ...*. https://github.com/NIGCOMSAT-Accelerator/c3hkth-team7
59. *http://arable.com/solutions/water-sustainability*. http://arable.com/solutions/water-sustainability
60. *http://arable.com/news/google-and-arable-collaborate-to-bring-innovative-water-stewardship-solution-to-nebraska-agriculture*. http://arable.com/news/google-and-arable-collaborate-to-bring-innovative-water-stewardship-solution-to-nebraska-agriculture
