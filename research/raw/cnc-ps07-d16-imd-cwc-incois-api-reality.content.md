# Government Hazard Feeds KrishiSetu Can Actually Use

**Research cut-off:** 2026-08-16. In this report, "public" means a developer can obtain the published artifact or use the documented interface without an MOU. It does not imply a service-level agreement, unrestricted redistribution, or production approval.

## 1. EXECUTIVE SUMMARY

- **Prototype Is A GO, Pilot Is Gated**: KrishiSetu can prototype today with IMD's public CAP RSS/XML feed, RSMC PDF bulletins, CWC forecast pages, India-WRIS APIs, INCOIS public products, Bhuvan layers, and local sensors. A production pilot remains gated because new IMD API registration is currently restricted to Government of India or NIC email addresses, while registration for other users is paused pending a new API Usage and Pricing Policy [33]. -> Build the adapter layer now, but pursue an Odisha government, ICAR, or NIC-backed onboarding path before promising live pilot coverage.

- **IMD Has A Real API, But Not An Open Anonymous One**: The official reference documents city, district, rainfall, nowcast, AWS/ARG, warning, marine, agromet, and cyclone APIs, with `/api/v1/` endpoints and JSON examples [16]. The public information page also points users to IP whitelisting and asks implementers to attribute IMD and cache responses during peak events [11]. -> Treat the IMD API as an official, controlled integration, not a no-key hackathon endpoint.

- **CAP XML Is The Best Immediate Warning Ingest**: IMD publishes a public RSS feed whose entries link to individual CAP XML alerts and include publication time, hazard text, and affected areas; a retrieved alert explicitly included Odisha [20]. -> Use CAP as the prototype's primary machine-readable trigger, with deduplication by alert identifier and timestamp.

- **MOSDAC Is Real, Documented, And Account-Tiered**: Anonymous users can search or preview without credentials, but downloads require an approved MOSDAC account; the published script uses `config.json` and `mdapi.py`, and the documented quota is **5,000 files per user per day** [22]. Its policy distinguishes anonymous Open Data NRT, registered general access with a 3-day latency, and privileged NRT access [19]. -> Use MOSDAC for satellite context and retrospective validation, not as the sole last-mile warning channel.

- **CWC Offers A Genuine API Catalog, Not Just PDFs**: India-WRIS lists River Water Level, discharge, rainfall, soil moisture, reservoir, and other datasets; its catalog accepts administrative or basin filters and can return JSON or XML, with CSV downloads and a **1,000-record request ceiling** [34]. -> Prototype the river-risk adapter against the catalog, but verify Odisha station IDs, actual latency, and continuity before field use.

- **INCOIS Products Are Stronger Than Its Public API Story**: SAMUDRA exposes high-wave, swell-surge, current, tsunami, storm-surge, astronomical-tide, and marine-heat-wave products, including 5-day ocean-current, significant-wave-height, swell, wind, and mixed-layer-depth forecasts [36]. INCOIS also exposes a Live Access Server with OPeNDAP/THREDDS links [38], but the research did not find a supported public API specifically guaranteeing operational storm-surge, tide-gauge, or buoy observations. -> Use public INCOIS products as an official coastal-risk confirmation layer; do not advertise an INCOIS buoy API until INCOIS confirms the dataset and terms.

- **Bhuvan Is Best For Static Exposure, Not Event Timing**: Bhuvan officially exposes OGC WMS/WMTS services for LULC, water bodies, flood hazard, annual flood layers, erosion, and related themes at 1:50,000 and 1:250,000 scales [14]. CartoDEM Version-3R1 is listed as a free 1 arc-second, approximately 32 m DEM [39]. -> Pre-cache elevation, drainage exposure, and land-cover context at the edge; do not poll Bhuvan as a live cyclone feed.

- **Global APIs Are Continuity Fallbacks, Not Authorities**: OpenWeather One Call advertises **1,000 free calls/day**, 10-minute updates, and history from 1979 [3]. WeatherAPI's current plans range from **$0/100K calls/month** to **$65/10M calls/month**, with no SLA below Enterprise [8]. Open-Meteo's free non-commercial tier allows fewer than 10,000 calls/day but carries no accuracy or availability warranty [35][32]. -> Use a global provider only to fill ordinary weather variables or detect source outages; IMD/CWC/INCOIS must control cyclone, flood, and coastal-hazard decisions.

## 2. DATA INVENTORY

**Reliability grading:** **A** = official, machine-readable, directly usable, and reasonably clear access path; **B** = official and useful but gated, partly manual, or lacking an SLA; **C** = request-based, incomplete, or operationally ambiguous; **D** = no verified supported interface for the claimed use.

| Item | Named source, URL, and date | Spec and access reality | Prototype feasibility | Reliability |
|---|---|---|---|---|
| IMD forecast, warning, AWS, and cyclone APIs | IMD API Reference, `https://api.imd.gov.in/public/api_reference.html`, accessed 2026-08-16 | Official `/api/v1/` catalog. It includes city and lat/lon forecasts, district rainfall, current weather, station/district nowcasts, AWS/ARG, warnings, river-basin QPF, marine bulletins, agromet, and cyclone products. Examples are JSON [16]. | **Conditional.** Implement against a mock or approved credential. Do not assume anonymous access merely because endpoint examples are visible. | **B** |
| IMD API onboarding | IMD registration, `https://api.imd.gov.in/public/register.php`, accessed 2026-08-16 | Registration is open only to Government of India/NIC email users; other registrations are paused until a new API Usage and Pricing Policy is finalized [33]. IP whitelisting is part of the official access page [11]. No public rate table, rate limit, SLA, or policy completion date was found. | **Gated for an independent team; feasible through a government partner.** | **C** |
| IMD CAP warnings | IMD CAP RSS, `https://cap-sources.s3.amazonaws.com/in-imd-en/rss.xml`, live feed observed 2026-08-13; accessed 2026-08-16 | Public RSS whose entries link to individual `.xml` CAP alerts. The feed exposes publication time, author, hazard headline, and affected-area text [20]. | **Yes.** Best immediate machine-readable prototype trigger. Preserve raw XML for audit and handle feed/network failure. | **A** |
| RSMC cyclone bulletins | RSMC New Delhi, `https://rsmcnewdelhi.imd.gov.in/`, bulletin observed 2026-08-13; accessed 2026-08-16 | Public National, RSMC, TCAC, quadrant-wind, GMDSS, hourly, graphics, track, and archive products. The observed National Bulletin was a PDF [27]. | **Yes, as a fallback parser and human verification screen.** PDF parsing is less robust than CAP/JSON. | **B** |
| MOSDAC catalog and Download API | MOSDAC Download API Manual, `https://www.mosdac.gov.in/downloadapi-manual`, updated 2026-08-06; Data Access Policy, `http://mosdac.gov.in/data-access-policy`, updated 2026-08-11 | Catalog families include satellite images, radar, weather, ocean state, forecast, nowcast, alerts, and met/ocean applications. Search/preview can be anonymous; downloads require approved account credentials in `config.json`; the supplied Python workflow runs `mdapi.py`; maximum 5,000 files/day/user [9][22]. | **Yes after account approval.** Anonymous metadata/open-data preview is usable immediately. | **B** |
| MOSDAC access tiers | MOSDAC Data Access Policy, same URL and date | Anonymous: metadata/images and Open Data with NRT access. Registered general: limited datasets with 3-day latency. Registered privileged: all data with NRT access [19]. Eligibility for privileged status is not stated on the page. | **General account for development; privileged access must be negotiated.** | **B** |
| IMD historical AWS/agromet data | IMD Data Service Portal, `https://dsp.imdpune.gov.in/`, Version 5.0 operational 2024-10-01; regional data-supply procedures, accessed 2026-08-16 | Holdings include AWS, ARG, agromet, surface, rainfall, wind, pressure, humidity, cloud, and climate data. Procurement requires portal enrollment or a formal request, station/period/purpose details, payment after estimate, and an undertaking. Regional procedures state data are chargeable, with 18% GST, and restrict reuse to the declared purpose [26][25]. The portal separately lists some free data series [21]. | **Poor for live warning ingestion; useful for training, baselines, and evaluation after approval/payment.** | **C** |
| IMD 2024-25 data-policy reality | DSP Version 5.0 and IMD API registration pages, dates above | The dated operational change found was DSP Version 5.0 on 2024-10-01 [21]. Archive supply remains a free-series plus chargeable-request model, while the newer API pricing framework is explicitly unfinished [33]. No defensible public 2024-25 API price table was found. | **Do not invent free/paid API tiers. Budget as unknown and seek written IMD terms.** | **D for price transparency** |
| CWC current flood forecast | CWC FFS, `https://ffs.india-water.gov.in/`; CWC AFF beta, `https://aff.india-water.gov.in/`, accessed 2026-08-16 | Public current forecast, hydrograph, table view, early warning, and 7-day advisory interfaces [10]. AFF states forecasts are updated every 3 hours [40] and warns that rainfall, reservoir releases, drainage congestion, flood measurements, and unknown factors create uncertainty [40]. | **Yes for dashboard confirmation and carefully cached ingestion; dynamic UI scraping is not a supported API contract.** | **B** |
| CWC/India-WRIS water API | India-WRIS API Catalog User Manual, `https://indiawris.gov.in/downloads/API%20Catalog_User%20Manual.pdf`, undated; accessed 2026-08-16 | Catalog includes River Water Level, discharge, rainfall, soil moisture, reservoir, and meteorological variables. Access begins by entering a valid email. Queries support state/district or basin/tributary filters and date ranges. Responses can be JSON or XML; CSV is available for download. Limit is 1,000 records/request [34]. | **Yes for a prototype.** The manual does not prove that every station is real-time or publish a latency/SLA. | **B** |
| CWC bulletins | CWC Flood Forecasting page, `https://cwc.gov.in/flood-forecasting-hydrological-observation`; 2026 SOP at `https://cwc.gov.in/sites/default/files/SOP_April_2026-FFM.pdf` | CWC reports a network of 325 stations, more than 7,000 forecasts/warnings annually, and historical overall forecast accuracy above 90% [12]. Orange bulletins are updated every 3 hours; Red bulletins every hour [12]. The 2026 SOP confirms daily flood bulletins [41]. | **Yes as official escalation evidence.** Expect PDF/human bulletin paths in addition to portal data. | **B** |
| INCOIS storm surge and coastal alerts | SAMUDRA, `https://incois.gov.in/site/SAMUDRA/index.html`; Storm Surge, `https://incois.gov.in/site/services/StormSurge.jsp`, accessed 2026-08-16 | Public products include storm surge, high waves, swell surge, currents, tsunami, astronomical tides, and threat maps [36]. The product pages establish official availability, but not a stable public REST/JSON contract. | **Yes for human confirmation or a licensed feed; no for claiming a supported storm-surge API without confirmation.** | **B for product, D for claimed API** |
| INCOIS wave and ocean forecasts | OSF, `https://incois.gov.in/oceanservices/osfforecast.jsp`; SAMUDRA, accessed 2026-08-16 | Coastal selector includes Odisha [2]. SAMUDRA describes 5-day forecasts for significant wave height, swells, winds, currents, and mixed-layer depth [36]. | **Useful coastal context.** Prototype can use displayed products, but production automation needs an approved machine interface. | **B** |
| INCOIS LAS/OPeNDAP | INCOIS LAS, `https://las.incois.gov.in/las/UI.vm`, accessed 2026-08-16 | Public page links to OPeNDAP/THREDDS and exposes gridded dataset selection and computation controls [38]. This proves programmatic ocean-data infrastructure exists, but not that live storm-surge, buoy, or tide-gauge observations are all available there. | **Useful for dataset exploration and selected gridded products; dataset-by-dataset verification required.** | **C** |
| INCOIS buoy and observed tide-gauge data | No supported public endpoint located after searches of INCOIS data-access, OPeNDAP, THREDDS, Ocean Data Bank, buoy, and tide-gauge terms | Astronomical tides appear in SAMUDRA [36], but an operational astronomical-tide product is not the same as observed tide-gauge data. No public documented buoy-observation API, station registry, cadence, or reuse terms were verified. | **Not prototype-safe as a claimed live feed. Request confirmation/data access from INCOIS or the producing agency.** | **D** |
| Bhuvan LULC and flood layers | Bhuvan WMS guide, `http://bhuvan.nrsc.gov.in/wiki/index.php/How_to_use_WMS_services`, last edited 2021-11-26 | OGC WMS/WMTS layers include LULC, urban LULC, water bodies, erosion, flood hazard, and annual flood layers at 1:50,000 and 1:250,000 [14]. They can be consumed by QGIS, OpenLayers, and other compatible clients [14]. | **Yes.** Pre-cache only the Odisha tiles/layers required by the farm-risk model. | **A for access, B for operational continuity** |
| Bhuvan DEM | Free-products list, `https://bhuvan.nrsc.gov.in/wiki/index.php/List_of_free_satellite_data_products`, last edited 2022-02-24 | Cartosat-1 DEM Version-3R1 is listed at 1 arc-second, approximately 32 m, in 1 degree x 1 degree India tiles [39]. | **Yes for static slope, relative elevation, drainage, and exposure features.** It is not a parcel survey or live flood-depth product. | **B** |
| OpenWeather One Call | `https://openweathermap.org/api/one-call-3`, accessed 2026-08-16 | API-key product with current/forecast/history services. Advertised allowance is 1,000 free calls/day, with pay-as-you-go above that; advertised update cadence is 10 minutes and history begins 1979-01-01 [3]. | **Easy technical fallback.** Not an Indian warning authority and no evidence supports using it to override IMD. | **C for hazard decisions** |
| WeatherAPI | `https://www.weatherapi.com/pricing.aspx`, accessed 2026-08-16 | Free: $0, 100K calls/month, 3-day forecast. Starter: $7, 3M calls/month, 7 days. Pro+: $25, 5M calls/month. Business: $65, 10M calls/month. Realtime updates every 10-15 minutes; forecast data every 4-6 hours. SLA only at Enterprise [8]. | **Low-friction fallback after key registration.** Validate location matching and outage behavior. | **C** |
| Open-Meteo | `https://open-meteo.com/en/pricing` and `/en/terms`, accessed 2026-08-16 | Free non-commercial access: under 10,000/day, 5,000/hour, 600/minute, 300K/month. Commercial subscriptions use a key and dedicated endpoint; paid plans target 99.9% uptime. Data are CC BY 4.0, but accuracy and uninterrupted availability are not guaranteed [35][32]. | **Excellent hackathon fallback if the prototype is genuinely non-commercial and attribution is shown. Commercial pilot needs a paid plan.** | **B for development, C for hazard authority** |
| Published developer guides | IMD API Reference; MOSDAC Download API Manual; India-WRIS API Catalog User Manual | These are official and describe products, parameters, sample responses, authentication workflows, and limits. They are more defensible than GitHub wrappers or scraper tutorials [16][22][34]. | **Use these as adapter contracts; archive copies and add contract tests.** | **A as documentation** |

**Inventory takeaway:** The misconception to avoid is "government data is either fully open or unavailable." The actual pattern is mixed: public CAP/XML and OGC layers, email-gated WRIS APIs, credentialed MOSDAC downloads, controlled IMD APIs, chargeable archives, and public INCOIS products without a verified hazard API contract.

## 3. COVERAGE TABLE

Counts below are research-audit counts, not search-engine totals. A "useful hit" directly answered a required access, format, cost, or reliability question. "Noise/missing" includes mirrors, generic home pages, stale wrappers, human-only displays, and pages that did not establish the claimed API.

| Source family | Useful hits reviewed | Noise or missing | Coverage judgment | Why |
|---|---:|---:|---|---|
| IMD API, Mausam, CAP, RSMC, DSP | 8 | 4 | **B** | Excellent product and format coverage, including JSON, XML, and PDF. Third-party registration, final API prices, rate limits, and SLA remain missing [16][33]. |
| MOSDAC | 5 | 2 | **A-** | Official access policy and working Download API manual settle registration, tier latency, script workflow, and daily quota [19][22]. Exact privileged-user eligibility remains unclear. |
| CWC and India-WRIS | 7 | 4 | **B** | Official forecast portals, 2026 SOP, and a detailed API Catalog manual exist. Station-level real-time semantics, latency, versioning, and SLA are not published in the reviewed manual [12][34]. |
| INCOIS | 6 | 7 | **C** | Strong public forecast, warning, app, LAS, OPeNDAP, and THREDDS evidence. Weak documentation for a supported external operational API covering storm surge, observed tides, and buoys [36][38]. |
| Bhuvan/NRSC | 5 | 3 | **B+** | WMS/WMTS and free DEM/LULC products are well evidenced. Update cadence, SLA, detailed reuse language, and all account requirements are less clear [14][39]. |
| Global API fallbacks | 6 | 3 | **B** | Costs, quotas, keys, forecast ranges, and terms are clear. None is an Indian cyclone/flood warning authority, and free tiers offer weak or no SLA [3][32][8]. |
| Third-party guides and code | 2 | 8 | **D** | Useful for learning request syntax, but wrappers and scrapers cannot establish legality, freshness, completeness, or production continuity. Official manuals supersede them. |

**Coverage judgment:** Government-source coverage is sufficient to build and demonstrate the complete ingestion architecture. It is not sufficient to claim an independently operated, always-on production service using every desired feed.

## 4. WHAT IS MISSING

1. **Final IMD API commercial policy.** The official registration page says the new usage and pricing framework is still being finalized [33]. Missing items are third-party eligibility, prices, free quota, rate limits, key rotation, IP-whitelist lead time, redistribution rights, uptime target, incident process, and a policy completion date.

2. **A public IMD schema/version contract.** The reference gives `/api/v1/` endpoints and sample JSON, but the reviewed pages do not publish a changelog, deprecation window, service status contract, or machine-readable OpenAPI specification. Client-side caching is recommended [11], but cache TTLs are not prescribed.

3. **Clear separation between live API data and chargeable archive data.** DSP includes free series and chargeable procurement, while regional procedures cover paid AWS/agromet archives with purpose-limited reuse [26][21]. A pilot needs written confirmation about which live API fields may be stored, transformed into advisories, and retained for model training.

4. **CWC station-operational metadata.** India-WRIS explicitly lists River Water Level and JSON/XML/CSV outputs [34], but the reviewed manual does not settle whether each Odisha gauge is real-time, its expected reporting delay, sensor quality flags, datum, warning/danger/highest-flood levels, maintenance state, station coordinates, or historical backfill behavior.

5. **CWC production guarantees.** The 1,000-record request limit is documented [34]; rate limits, costs, uptime, API versioning, and notification of schema changes are not. The AFF portal itself warns that rainfall uncertainty, reservoir releases, drainage congestion, measurement difficulties, and unknown factors affect forecasts [40].

6. **A verified INCOIS hazard API contract.** Public products establish wave, storm-surge, swell, tide, current, and tsunami information [36], while LAS proves OPeNDAP/THREDDS infrastructure [38]. Missing are a supported API catalog for operational storm-surge polygons/rasters, high-wave alerts, observed tide gauges, and buoys; station/product identifiers; JSON/NetCDF schemas; cadence; retention; auth; quota; and reuse terms.

7. **Bhuvan operational and legal details.** The open OGC layer path is clear, but a pilot still needs the precise attribution text, cache/redistribution rights, service capacity, maintenance notification, and update dates for each selected Odisha LULC or flood-hazard layer. The approximately 32 m DEM should not be represented as parcel-level elevation [39].

8. **Cyclone-period fallback performance.** Global services publish quotas and some uptime terms, not proof of local accuracy or uninterrupted cyclone operation. Open-Meteo expressly disclaims accuracy, completeness, and uninterrupted provision [32]. Load tests, multi-provider monitoring, and store-and-forward operation remain product responsibilities.

9. **Advisory governance.** None of these feeds supplies a complete, crop-stage-specific instruction engine. KrishiSetu still needs Odisha agriculture experts to approve action templates, confidence thresholds, escalation language, translation, IVR pronunciation, message expiry, and rules for conflicting or retracted alerts.

## 5. HOW IT FEEDS THE PRODUCT

| Product tier | Inputs | Decision powered | Edge and delivery behavior |
|---|---|---|---|
| **Tier 0: Static exposure** | Bhuvan CartoDEM, LULC, water bodies, flood hazard; farm boundary, crop, sowing date, phone, language | Baseline flood susceptibility, coastal exposure, drainage priority, which farms require earlier alerts | Pre-tile Odisha layers and store compact per-farm features. Static data remain usable during network loss. |
| **Tier 1: Official hazard truth** | IMD CAP, approved IMD API, RSMC bulletins; CWC FFS/WRIS; INCOIS storm-surge/high-wave products | Hazard existence, official severity, affected district/block, validity window, river escalation, coastal hazard | Preserve source, issue time, valid time, geography, raw payload hash, and parser version. Official warnings outrank global forecasts. |
| **Tier 2: Hyperlocal confirmation** | On-farm rain, wind, soil moisture, water-depth sensor, battery/network health; farm profile | Whether the official hazard has reached a farm, which action template applies, urgency and local confidence | Compute locally when disconnected. Never use a failed sensor reading as proof that an official hazard is absent. |
| **Tier 3: Continuity forecast** | OpenWeather, WeatherAPI, or Open-Meteo | Ordinary hourly weather, gap filling, trend context, detection that the official source may be stale | Mark as "fallback," retain provider/model/time, and prohibit it from downgrading an active IMD/CWC/INCOIS warning. |
| **Tier 4: Advisory delivery** | Rules approved by agriculture/disaster experts, language and literacy profile | SMS text, IVR call, retry schedule, acknowledgement, escalation to field worker | Use short verbs, absolute times, local units, and one action per sentence. Cache voice prompts and queue SMS/IVR for store-and-forward delivery. |
| **Tier 5: Recovery and audit** | Falling river level, expired official alert, local waterlogging, farmer acknowledgement and damage report | Safe inspection window, drainage/cleanup checklist, documentation and follow-up | Recovery advice requires a new decision state; it must not be generated merely because the initial alert expired. |

### Case study: cyclone approaching coastal Odisha

The ingestion chain receives an IMD CAP alert containing publication time and an Odisha affected-area statement [20]. KrishiSetu geocodes the alert to its farm registry and checks RSMC's current PDF/track product for operator confirmation [27]. INCOIS high-wave, swell-surge, current, or storm-surge products then add coastal context [36]. Bhuvan DEM/LULC features prioritize low-lying, water-adjacent farms, while local wind/rain sensors determine whether a message should say "prepare now" or "conditions detected locally."

The mechanism is source hierarchy, not AI prediction theater. IMD supplies official hazard truth; INCOIS supplies coastal mechanism; Bhuvan supplies exposure; farm data supplies consequence. The recommendation engine selects only a pre-approved action template. If IMD API credentials are unavailable, CAP plus RSMC remains a defensible demo path; the UI must state that it is using public bulletins rather than pretending to have privileged IMD AWS access.

### Case study: river flood and post-event transition

CWC's public system provides current forecasts, hydrographs, tables, and 7-day advisory products [10]. India-WRIS can supply River Water Level data in JSON/XML/CSV [34]. When a Severe/Orange message is active, the official cadence can be every 3 hours; Extreme/Red messages can update hourly [12]. The edge model combines that status with farm elevation, distance to drainage, local rain, and crop stage to rank SMS/IVR queues.

Recovery is a separate state transition. The platform should wait for an official downgrade or falling-water evidence plus local confirmation before moving from protection to inspection and recovery. Because CWC explicitly identifies forecast uncertainty [40], the product should communicate confidence and source time, not a false exact arrival time or flood depth.

## 6. REAL-vs-FILLER

| Genuinely usable now | Decorative or misleading claim to reject |
|---|---|
| Public IMD CAP RSS and linked XML alerts [20] | "Mausam has a completely open, no-key API for anyone." Official onboarding is controlled, and third-party registration is paused [33]. |
| Official IMD API reference, JSON samples, IP-whitelist route, attribution and caching guidance [16][11] | Hard-coding visible endpoints and calling that production integration without an approved account, written terms, or limit handling. |
| Public RSMC cyclone PDFs, tracks, graphics, and archives [27] | Calling a PDF page a JSON API, or silently scraping layout-dependent text without a human verification path. |
| MOSDAC anonymous catalog search plus credentialed download script and explicit quota [22] | "All MOSDAC data are open NRT." Registered general users may receive only limited data with 3-day latency [19]. |
| CWC FFS/AFF pages and India-WRIS JSON/XML/CSV API Catalog [34][40] | Claiming every CWC gauge is real-time because River Water Level appears in the catalog. The manual does not establish station-level latency. |
| INCOIS official SAMUDRA/OSF alerts and 5-day ocean products [36] | Advertising a live INCOIS buoy/tide/storm-surge REST API without a published endpoint, schema, account rule, or terms. |
| INCOIS LAS OPeNDAP/THREDDS for verified gridded datasets [38] | Treating the existence of LAS as proof that every operational warning and observation is available through it. |
| Bhuvan WMS/WMTS LULC and flood layers, plus free approximately 32 m CartoDEM [14][39] | Rendering a nationwide map in a demo without converting it into per-farm exposure features or acknowledging its scale. |
| A licensed global API for ordinary variables and continuity [3][35][8] | Allowing a global forecast to cancel or dilute an active official Indian warning. |
| Edge caching, source timestamps, fallback labels, raw-payload retention, and SMS/IVR store-and-forward | "AI predicts cyclones" or fabricated live sensor streams. The product's value is trusted translation from official hazard to farm action. |

**Decision-ready insight:** A convincing hackathon demo shows provenance and graceful degradation. A crowded map with many logos is filler unless every layer changes a documented decision.

## 7. NOISE LOG

| Searched and discarded | Why discarded | What replaced it |
|---|---|---|
| Scribd copies of IMD API lists | Unofficial mirror, uncertain date, and cannot establish current access or terms | Official IMD API Reference and registration page |
| `indianapi.in` weather guide and GitHub "IndianWeatherAPI" wrappers | May proxy, scrape, or repackage data; no authority over IMD availability, rate limits, or reuse | Official `/api/v1/` documentation [16] |
| GitHub CWC reservoir-data repositories | Useful code examples but commonly contain snapshots derived from India-WRIS, not a supported live CWC contract | India-WRIS API Catalog manual [34] |
| CWC Swagger/IAM page returning "Failed to load remote configuration" | It did not expose a usable contract and may be an internal or broken UI | Published India-WRIS manual plus FFS/AFF portals |
| Generic India-WRIS map pages with no API details | They prove a portal exists, not request parameters, output formats, or limits | API Catalog manual with JSON/XML/CSV and 1,000-record ceiling [34] |
| INCOIS vacancy-domain mirrors and old annual-report search hits | Weak route to current operational access; some pages were generic or historical | Current SAMUDRA, OSF, Storm Surge, port forecast, and LAS pages |
| Search results for "Ocean.io API" | Name collision with a private company-data product, unrelated to INCOIS | Restricted later searches to `incois.gov.in` and verified LAS |
| Generic ECMWF/NOAA cyclone charts | Valuable science but not the issuing authority for Odisha public warnings | IMD/RSMC for cyclone authority; INCOIS for coastal hazards |
| FreeAPIHub summaries of commercial weather services | Secondary pricing may be stale or omit terms and SLA | OpenWeather, WeatherAPI, and Open-Meteo first-party pricing/terms |
| Raw dashboard HTML/XHR discoveries | Undocumented internal endpoints can change and may breach intended access controls | Only published feeds, manuals, OGC services, and approved APIs are classified as real |

The discarded sources are not necessarily false. They fail the narrower test required here: can they establish that a developer may depend on a named, current, supported interface?

## 8. VERDICT: PROTOTYPE GO, PILOT GATED - SYNTHESIS

| Dimension | IMD | CWC/India-WRIS | INCOIS | MOSDAC/Bhuvan | Global fallback |
|---|---|---|---|---|---|
| **Mechanism** | Official warning/forecast authority; CAP, JSON, PDF | Gauge, discharge, flood forecast, bulletin | Coastal/ocean forecast and multi-hazard products | Satellite observation and static geospatial exposure | Multi-model/commercial weather aggregation |
| **Scope** | Cyclone, rain, nowcast, warnings, AWS/agromet, marine | River and reservoir conditions, flood escalation | Waves, surge, swell, tides, currents, tsunami | Clouds/rain/ocean imagery, DEM, LULC, flood layers | Current and forecast weather worldwide |
| **Time horizon** | Immediate warning through multi-day forecast | Current through 7-day advisory | Alerts and 5-day ocean forecast | NRT satellite in eligible tiers; mostly static Bhuvan context | Minutes to days, with provider-dependent cadence |
| **Primary trade-off** | Highest authority but strongest onboarding gate | Useful API/catalog but unclear station latency/SLA | Strong products, weak external API contract | Good data access, but not the final warning authority | Easy integration, weak legal/operational authority for Indian hazards |
| **Evidence base** | API reference, registration notice, CAP and RSMC | API manual, FFS/AFF, CWC SOP | SAMUDRA/OSF/Storm Surge/LAS | Access policy, download manual, OGC guides | First-party price and terms pages |

The non-obvious tension is that the most authoritative family, IMD, is not the easiest one for an independent team to automate. Conversely, the easiest providers, global weather APIs, are the least defensible for life-safety escalation. KrishiSetu should not choose one source. It should use a **source-authority architecture**: official Indian feeds determine hazard state, static government layers determine exposure, local IoT determines farm consequence, and global APIs provide labeled continuity only.

A second tension is format versus operational certainty. IMD CAP is openly machine-readable, while some official cyclone and flood evidence remains PDF or dashboard based. India-WRIS has a real API catalog, but "River Water Level" does not by itself guarantee a fresh reading from every station. INCOIS has rich public products and OPeNDAP/THREDDS infrastructure, but no verified single API covers the requested surge, observed tide, and buoy use cases. Therefore, parser success must never be confused with source completeness.

### Final decision

- **Hackathon prototype: GO.** Build with IMD CAP XML as the primary weather-warning trigger; RSMC and CWC public products as verification/fallback; India-WRIS JSON/XML/CSV for river data; INCOIS public coastal products; Bhuvan static features; MOSDAC account-based data where available; and Open-Meteo or another keyed global API for clearly labeled continuity. This is enough to demonstrate ingest -> geofence -> farm-profile match -> rule/edge inference -> SMS/IVR output.

- **Live-data prototype using every desired official API: PARTIAL.** IMD API registration is unavailable to ordinary third parties while policy work is underway [33]. INCOIS observed buoy/tide and operational storm-surge API access remains unverified. CWC station freshness needs station-by-station testing.

- **Odisha pilot: GATED.** Required gates are: (1) government-backed IMD onboarding and written API/reuse terms; (2) station and latency validation with CWC/NWIC; (3) written INCOIS confirmation of machine feeds and licenses; (4) Bhuvan/MOSDAC attribution and cache terms; (5) telecom consent, DLT/SMS and IVR delivery arrangements; (6) agriculture and disaster-management approval of advice templates; and (7) measured failover, offline, load, and alert-retraction tests.

- **Overall verdict: PARTIAL.** The concept is technically real and prototype-ready, not filler. The official data ecosystem is fragmented and access-controlled, so a production claim is premature until institutional access and operational contracts are secured.

## References

1. *ISRO's Geoportal | Gateway to Indian Earth Observation | Applications | Bhuvan | NRSC Open EO Data Archive | NOEDA | Ortho | DEM | Elevation | AWiFS | LISSIII | HySI | TCHP | OHC | Free GIS Data | Download*. http://bhuvan-app3.nrsc.gov.in/data/download/index.php
2. *INCOIS - Ocean State Forecast (OSF)*. https://incois.gov.in/oceanservices/osfforecast.jsp
3. *One Call API 3.0*. https://openweathermap.org/api/one-call-3
4. *incois.gov.in*. https://incois.gov.in/site/services/StormSurge.jsp
5. *incois.gov.in*. https://incois.gov.in/site/services/global.jsp
6. *INSAT-3D Payloads | Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/insat-3d-payloads
7. *IMD API Management*. https://api.imd.gov.in/public/index.php
8. [
	Pricing - WeatherAPI.com
](https://www.weatherapi.com/pricing.aspx)
9. *Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/
10. *Flood Forecast - Central Water Commision, Govt. Of India*. https://ffs.india-water.gov.in/
11. *IMD APIs | India Meteorological Department*. http://mausam.imd.gov.in/responsive/apis.php
12. *Flood Forecasting/ Hydrological Observation | Central Water Commission, Ministry of jal shakti, Department of Water Resources, River Development and Ganga Rejuvenation, GoI*. https://cwc.gov.in/flood-forecasting-hydrological-observation
13. *Digital Object Identifier (DOI) | Meteorological & Oceanographic Satellite Data Archival Centre*. https://mosdac.gov.in/digital-object-identifier-doi
14. *How to use WMS services - Bhuvan Wiki*. http://bhuvan.nrsc.gov.in/wiki/index.php/How_to_use_WMS_services
15. *Bhuvan Store*. http://bhuvan-app1.nrsc.gov.in/2dresources/bhuvanstore2.php
16. *Api Reference*. https://api.imd.gov.in/public/api_reference.html
17. *AWS ARG LOGIN*. http://aws.imd.gov.in:8091/internal/
18. *India-WRIS*. https://nwic.in/wris
19. *Data Access Policy | Meteorological & Oceanographic Satellite Data Archival Centre*. http://mosdac.gov.in/data-access-policy
20. *In Imd En*. https://cap-sources.s3.amazonaws.com/in-imd-en/rss.xml
21. *IMD-DSP*. https://dsp.imdpune.gov.in/
22. *User Manual for MOSDAC Data Download API | Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/downloadapi-manual
23. *India-WRIS*. https://indiawris.gov.in/wris
24. *Water Resources Information System (WRIS) | Central Water Commission, Ministry of jal shakti, Department of Water Resources, River Development and Ganga Rejuvenation, GoI*. https://www.cwc.gov.in/en/water-resources-information-system-wris
25. *Supply of Meteorological Data*. https://mausam.imd.gov.in/patna/mcdata/Data_Supply_Procedure%28ENGLISH%29.pdf
26. *Data Procedure*. https://mausam.imd.gov.in/newdelhi/docs/data-procedure.pdf
27. *RSMC*. https://rsmcnewdelhi.imd.gov.in/
28. *incois.gov.in*. https://incois.gov.in/site/services/osf.jsp
29. *Pricing*. https://openweathermap.org/price
30. *Sea State Forecasts for Ports and Harbors – INCOIS*. https://sarat.incois.gov.in/OSF
31. *How to start to work with Openweather API*. https://openweathermap.org/appid
32. *🧑‍⚖️ Terms | Open-Meteo.com*. https://open-meteo.com/en/terms
33. *Register | IMD API*. https://api.imd.gov.in/public/register.php
34. *Api Catalog User Manual*. https://indiawris.gov.in/downloads/API%20Catalog_User%20Manual.pdf
35. *💰 Pricing | Open-Meteo.com*. https://open-meteo.com/en/pricing
36. *SAMUDRA- The INCOIS Mobile Application*. https://incois.gov.in/site/SAMUDRA/index.html
37. *Bhuvan | NRSC Open EO Data Archive | NOEDA | Ortho | DEM | Elevation | AWiFS | LISSIII | HySI | TCHP | OHC | Free GIS Data | Download*. https://bhuvan-app3.nrsc.gov.in/data
38. *INCOIS LAS*. https://las.incois.gov.in/las/UI.vm
39. *List of free satellite data products - Bhuvan Wiki*. https://bhuvan.nrsc.gov.in/wiki/index.php/List_of_free_satellite_data_products
40. *CWC AFF (Beta)*. https://aff.india-water.gov.in/
41. *Government of India*. https://cwc.gov.in/sites/default/files/SOP_April_2026-FFM.pdf
