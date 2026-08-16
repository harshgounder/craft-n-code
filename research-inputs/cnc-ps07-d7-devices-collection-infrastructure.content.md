# Odisha Advisory Data: Buildable Rails, Critical Blind Spots

## 1. EXECUTIVE SUMMARY

- **A Public Warning Backbone Exists**: IMD already publishes real-time observations, forecasts, warnings and specialized bulletins through an API-management gateway, while GKMS supplies five-day district/block forecasts and twice-weekly agromet advisories nationally [4][53] -> use IMD warnings as the event trigger, but complete API onboarding and caching before the demo.
- **Odisha Weather-Station Coverage Is Not Fully Auditable**: the Bhubaneswar portal exposes current observations for eight named locations, and an undated procurement document proposes 10 additional GPRS AWS units, but neither source proves a current, district-by-district count of operational AWS, automatic rain gauges or agromet observatories [21][32] -> label the statewide count **not publicly established**, not "30 districts covered."
- **River Data Is The Strongest Free Operational Feed**: CWC maintains **19 flood-forecasting sites in Odisha**, comprising 12 water-level and seven inflow sites, while the National Water Data Portal publishes hourly, station-identified river levels in CSV/API formats [52][3] -> build threshold and rate-of-rise triggers first.
- **Odisha Has A Visible Coastal Gauge Footprint, But Availability Varies**: INCOIS's live tide-gauge page lists Paradeep, Astranga, Bahabalpur, Dhamra, Dosinga and Gopalpur in Odisha, yet the same page shows that some stations are "Not Reporting" [34] -> poll station timestamps and quality flags rather than treating a listed gauge as a live gauge.
- **The Best Free Satellite Stack Is Split By Time Horizon**: INSAT-3DR offers storm products such as quantitative precipitation estimates, outgoing long-wave radiation, sea-surface temperature and atmospheric-motion products; Sentinel-1 supplies free all-weather, day/night C-band radar; Sentinel-2 supplies free 10/20/60 m optical bands on a five-day design revisit [24][27][5] -> use INSAT/IMD for warning context, Sentinel-1 for flood extent and Sentinel-2 for vegetation recovery when clouds permit.
- **RISAT/EOS-04 Is Capable But Not Reliably Free**: EOS-04/RISAT-1A supports all-weather flood and agricultural imaging from 1 m to 50 m depending on mode, but Bhoonidhi mixes free and priced products and requires login and a financial account for ordering [49] -> keep Sentinel-1 as the default prototype feed and treat EOS-04 as an optional NRSC path.
- **Hyperlocality Requires Field Collection**: public feeds do not reveal a farmer's plot soil moisture, standing-water depth, salinity, crop stage or drainage condition. IMD's proposed Odisha AWS specification shows a feasible 1-15 minute, solar/GPRS design, but it is infrastructure procurement, not an open farm API [32] -> instrument a small calibration cohort rather than pretending public weather is plot weather.
- **Basic-Phone Delivery Is Feasible But Regulated**: a published SMS tier is **INR 0.18/message at 30,000 messages plus 18% GST**, cloud-IVR benchmarks are **INR 0.40-0.65/minute**, and TRAI requires registered headers for commercial communication [18][48][12] -> budget SMS as the universal short alert and IVR as the Odia explanation, using a DLT-compliant provider.
- **Crowd Reports Can Build Claim Packets, Not Approve Claims**: FarmerChat demonstrates local-language text, voice and image interaction, while the CCE ecosystem demonstrates online/offline field capture [54][17] -> store timestamp, location, media hash, crop profile and reviewer decision, then corroborate with Sentinel-1, CWC/IMD and an authorized assessor.
- **Overall Grade - PARTIAL**: weather warnings, river telemetry, tide visualization, free Sentinel data and SMS/IVR APIs can be assembled now; plot sensing, DLT/telephony, reliable raw ocean data, insurer acceptance and drone operations remain hardware- or partner-gated.

**Reliability scale used below:** **A** = current primary government or mission data suitable for operational use; **B** = primary technical source with an access, coverage or freshness qualification; **C** = vendor/secondary benchmark requiring a quote or validation; **D** = illustrative or unverified, unsuitable as an engine dependency.

## 2. DATA INVENTORY

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability |
|---|---|---|---|---|---|
| IMD forecasts, warnings and observations | IMD API Management, https://api.imd.gov.in/public/index.php, accessed 2026-08-16 | City, station, district and product dependent | Real-time observations plus forecast/warning cycles | Controlled key-based API; onboarding, attribution, IP whitelisting and client caching are operational requirements [4] | A- |
| Odisha current weather observations | Meteorological Centre Bhubaneswar, https://mausam.imd.gov.in/bhubaneswar/, accessed 2026-08-16 | Eight visible locations: Bhubaneswar Airport, Gopalpur, Paradip, Bhubaneswar-Cuttack, Balasore, Jharsuguda, Puri and Chandbali [21] | Observation timestamp shown on page | Free web page/PDF products; no page-level API commitment | A- |
| Odisha AWS count | IMD GeM technical specification, https://mkp.gem.gov.in/.../specification_of_gprs_based__aws_for_odisha_2023-10-12-10-32-09_b6f3bd8879a0b57352e26430835a4a3a.pdf, document date not stated | **10 proposed units**, locations to be supplied after the order; not an installed-network count [32] | Proposed procurement, not live status | Procurement report; FTP/GPRS design, not public API | B- |
| IMD automatic rain gauges | IMD AWS/ARG training note, https://imdpune.gov.in/training/icitc/LN_11_57_Notes%20on%20AWS%20and%20ARG.pdf, accessed 2026-08-16 | National instrumentation description; no verified Odisha count | Not operational status | Technical note/report | B- |
| Agromet stations/AMFUs | GKMS parliamentary response, https://pib.gov.in/PressReleasePage.aspx?PRID=2223075, verified 2026-08-15 | 130 AMFUs across 127 agroclimatic zones nationally; Odisha-specific number not provided [53] | Advisories every Tuesday and Friday | Free bulletin/app/state channels | A- |
| CWC Odisha flood-forecast sites | Rajya Sabha USQ 891, https://sansad.in/getFile/annex/262/AU891.pdf?source=pqars, accessed 2026-08-16 | **19 sites: 12 level, seven inflow**, across Subarnarekha, Mahanadi, Brahmani, Baitarani and connected basins [52] | Operational forecast network; per-site status must be polled | Official report and CWC forecast portal | A |
| CWC hourly river levels | National Water Data Portal, https://nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc, updated 2026-08-09 | Station ID plus geographic hierarchy and river level | Hourly; portal update timestamp published [3] | CSV and API [3] | A |
| India-WRIS hydro-observations | India-WRIS, https://cwc.gov.in/en/water-resources-information-system-wris, accessed 2026-08-16 | Basin, sub-basin, watershed, river, dam and observation-station layers | Theme dependent; reservoir data daily | Free download for unclassified CWC hydrological-observation data [23] | A- |
| Odisha coastal tide gauges | INCOIS Tide Gauge Subsystem, https://tsunami.incois.gov.in/TEWS/Link.do?function=tgStationList, timestamp 2026-08-16 | Paradeep, Astranga, Bahabalpur, Dhamra, Dosinga and Gopalpur [34] | Last-report timestamp per station; some stations not reporting | Public visualization/chart links; no documented download API on this page | A- |
| INCOIS wave-rider buoys | INCOIS Data Holdings, https://incois.gov.in/site/dataholdings.jsp, accessed 2026-08-16 | Platform/network level; Odisha buoy location not stated | Real time | Public visualization; no download option [28] | B |
| INCOIS moored/deep-ocean buoys | INCOIS Data Holdings, same URL/date | Atmospheric, wave, current, SST, salinity and subsurface profile variables; Odisha location not stated | Real time | Visualization only; no download option [28] | B |
| INCOIS tsunami buoys | INCOIS Data Holdings, same URL/date | Sea level at network platforms; Odisha platform not stated | Real time | Tsunami-centre visualization; no download [28] | B |
| INCOIS drifting buoys | INCOIS Data Holdings, same URL/date | Pressure, SST and ocean current by platform | Real time | Public visualization and download [28] | B+ |
| INCOIS ocean-state forecast | INCOIS OSF, https://incois.gov.in/site/services/osf.jsp, accessed 2026-08-16 | Basin, state/coast and location-oriented forecast products | Forecast issue dependent | Public web product; raw API not established [9] | A- |
| INSAT-3D/3DR products | MOSDAC, https://mosdac.gov.in/insat-3dr-data-products, accessed 2026-08-16 | Geostationary HDF products including QPE, OLR, SST, cloud-motion and water-vapour winds [24] | Product-specific cadence; exact latency was not stated on the catalog page | MOSDAC product/download workflow; endpoint testing required | A- |
| Sentinel-1 SAR | Copernicus Data Space, https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel1.html, accessed 2026-08-16 | C-band SAR; GRD/SLC products; coverage depends on mode | 12-day repeat under the documented one-satellite condition; six-day repeat expected with two satellites [27] | Free products; STAC and OData catalogs [27] | A |
| Sentinel-2 optical/NDVI inputs | Copernicus Data Space, https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2, accessed 2026-08-16 | Four bands at 10 m, six at 20 m and three at 60 m [5] | Five-day design revisit at equator; actual clear-sky availability varies | Free Level-1C/Level-2A products [5] | A |
| EOS-04/RISAT-1A SAR | NRSC EOS-04 Handbook, https://bhoonidhi.nrsc.gov.in/bhoonidhi_resources/help/docs/EOS-04_Handbook.pdf, October 2022 | 1, 3, 33 or 50 m modes with 15-223 km swaths [49] | 17-day repeat [49] | Bhoonidhi catalog; mixture of free and priced ordering, registration for orders | B+ |
| Bhoonidhi archive/API | Bhoonidhi, https://bhoonidhi.nrsc.gov.in/, accessed 2026-08-16 | Archive from 47 Indian/foreign satellites; regional Sentinel/Landsat distribution | Product dependent | API available by contact; open and priced products coexist [16] | B |
| Plot soil-moisture node | ESP32/LoRa design reference, https://zbotic.in/iot-soil-monitor-for-farms-esp32-lora-dashboard, accessed 2026-08-16 | One or several probes per representative plot/root zone | Configurable minutes; calibration dependent | Purchase/DIY field collection; node, gateway, solar and dashboard required [7] | C+ |
| Mini farm weather station | IMD Odisha AWS technical specification, URL above, date not stated | Rain, temperature, humidity, wind and pressure; optional soil/radiation variables | 1-15 minute configurable sampling; 15-minute dissemination, reducible to one minute during extremes [32] | Purchased hardware, installation, calibration, solar power and SIM/GPRS | B as design, not as an available feed |
| Complete AWS price anchor | Gaby Instruments and TradeIndia listings, accessed 2026-08-16 | Vendor-defined packages, not harmonized specifications | Quote dependent | Purchase; headline listings of **INR 30,090** and **INR 250,000** show why a same-spec quotation is necessary [55][56] | C- |
| Rain-presence sensor | ESP32 rain-sensor tutorial, https://esp32io.com/tutorials/esp32-rain-sensor, accessed 2026-08-16 | Point detection; digital wet/dry plus analog level | Instant at node | DIY purchase/field collection; not a calibrated rain gauge [46] | C |
| SMS rail | MSG91 India, https://msg91.com/in/pricing/sms, accessed 2026-08-16 | Per registered mobile number | Near real time; delivery receipts provider dependent | API purchase; 30,000 SMS at INR 0.18 each, INR 5,400 plus 18% GST [18] | B- |
| IVR/voice rail | Bonvoice India cost guide, https://bonvoice.com/insights/ivr-pricing-in-india, 2026-05-29 | One outbound call/session per farmer | Real time; retry logic required | Provider purchase; benchmark INR 0.40-0.65/minute, plus plan/setup/API costs [48] | C |
| USSD rail | IDRBT mobile-banking guide, https://www.idrbt.ac.in/wp-content/uploads/2024/07/MBTUSSD_IDRBT.pdf, published 2016-12-08 | Interactive session on any type of mobile phone | Live session | Mobile-operator channel; no agriculture API/short code identified [51] | B for capability, D for prototype access |
| WhatsApp Business rail | Meta pricing documentation and AiSensy provider quote, accessed 2026-08-16 | App account/phone number | Near real time | Business-platform/BSP purchase; provider quote: INR 1.09 marketing and INR 0.145 utility/authentication per message [57] | C+ |
| Farmer text/voice/image reports | Digital Green FarmerChat, https://digitalgreen.org/farmer-chat, accessed 2026-08-16 | Farmer, conversation and submitted media | Immediate submission; verification separate | App/partnership; local-language voice, text and images [54] | B for collection, D as claim proof alone |
| CCE and claim field capture | CCE Agri Mobile App presentation, https://www.ncfc.gov.in/.../Crop%20Insurance%20Portal.pdf, accessed 2026-08-16 | Crop-cutting experiment/field record | Offline capture, later synchronization | Government workflow/app; not an open claim-approval API [17][22] | B |
| Drone photogrammetry | AiRotor India guide, https://www.airotor.in/blog/drone-survey-cost-in-india-2026-per-acre-pricing-guide, 2026-07-03 | Centimetre-scale orthomosaic/DSM/DTM by mission | Post-event, after safe flying conditions | Contracted field collection; INR 800-2,000/acre, with mobilization minimums [41] | C |
| Drone compliance | Drone Rules 2021 and DigitalSky, https://digitalsky.dgca.gov.in/, rules dated 2021-08-25; portal accessed 2026-08-16 | Aircraft, pilot and airspace/mission | Approval/status dependent | UIN/registration, compliant aircraft, trained remote pilot and airspace checks [6][14] | A |

**Inventory takeaway:** The prototype has strong public hazard context and weaker plot context. No single row supplies the full advisory; the useful design is a timestamped fusion of official hazard feeds, farmer profiles, selectively deployed sensors and auditable human reports.

## 3. COVERAGE TABLE

| Source family | Useful hits retained | Noise or missing evidence | Coverage judgment |
|---|---|---|---|
| IMD observations and API | API portal, Bhubaneswar station page, GKMS, proposed 10-AWS specification | No authoritative current Odisha AWS/ARG/AMUS total; proposed hardware is not installed coverage; API SLA and historical licensing remain unclear | **B** |
| CWC river network | 19 Odisha forecast sites, hourly levels, CSV/API, free WRIS downloads | Station-to-village flood translation and live per-station completeness still require testing | **A** |
| INCOIS coastal/ocean | Six Odisha tide-gauge names, timestamps, OSF, real-time platform metadata | Several stations may be non-reporting; moored/wave/tsunami data are often visualization-only; Odisha buoy locations not established | **B** |
| INSAT/MOSDAC | QPE, OLR, SST and wind/cloud products in HDF | Exact product cadence, latency, cloud-top-temperature endpoint and automated entitlement require catalog testing | **B** |
| Copernicus Sentinel | Free Sentinel-1 radar and Sentinel-2 optical products with documented APIs/resolution | Revisit is not delivery latency; Sentinel-2 is cloud constrained; parcel inference needs processing and ground truth | **A** |
| NRSC/Bhoonidhi/RISAT | EOS-04 flood capability, modes, archive and API | Free-versus-priced entitlement and ordering latency are not predictable from the handbook alone | **B** |
| Farm IoT | Feasible ESP32/LoRa/solar architecture and a production-grade AWS specification | No defensible universal per-node price, no Odisha maintenance data, calibration and enclosure costs often omitted | **C** |
| SMS/IVR/USSD/WhatsApp | SMS price tiers, IVR benchmark, DLT rules, feature-phone USSD capability, WhatsApp quote | Vendor quotes vary; USSD lacks an off-the-shelf agriculture short code; WhatsApp is not the required universal basic-phone endpoint | **B-** |
| Crowdsourced reports | FarmerChat input modes, CCE offline pattern, PMFBY channels | No public source makes a farmer photo sufficient proof; voice/image model accuracy and fraud rate not disclosed | **B-** |
| Drones | DGCA/DigitalSky framework and survey price benchmark | Flying weather, local airspace, mobilization, battery logistics and official acceptance are mission dependent | **B-** |

**Coverage judgment:** Public data is good enough for a hazard-triggered advisory prototype, but not for automatic field-loss determination. The latter requires farm identity, parcel geometry, field measurements and a governed verification chain.

## 4. WHAT IS MISSING

1. **Current operational Odisha IMD network census.** No located public source gives a current, station-by-station list and status for every IMD AWS, ARG and agromet observatory, mapped to all 30 Odisha districts. The proposed 10 AWS are not evidence that 10 were commissioned [32].

2. **Plot identity and crop state.** Public feeds do not contain a farmer-consented parcel polygon, crop and variety, sowing/transplanting date, growth stage, expected harvest date, irrigation source, livestock location or stored-input inventory. Without these, advice remains district-generic.

3. **Plot hydrology.** There is no public statewide feed for root-zone soil moisture, standing-water depth and duration, drainage outlet condition, salinity after storm surge, pond/tube-well contamination or field-level flood arrival. River gauges and satellite water masks cannot directly substitute for these measurements.

4. **Guaranteed machine-readable coastal observations.** INCOIS exposes useful live visualization, but the data-holdings page explicitly withholds download for several moored, wave-rider and tsunami platforms [28]. A production service needs an API/data agreement, quality flags and a support contact.

5. **Delivery identity, consent and reachability.** The engine still needs a verified mobile number, preferred language, quiet hours, disability/accessibility needs, IVR retry policy and delivery receipts. DLT/header registration is a sender gate, not a farmer registry [12].

6. **Accepted claim-evidence schema.** A claim packet needs insurer/state-defined mandatory fields, reporting deadlines, assessor roles and an appeal trail. A geotagged photo or AI diagnosis is evidence to review, not proof of cause, date, area or insured interest.

7. **Operational cost and maintenance evidence for IoT.** Retail sensors do not establish installed cost. Missing items include calibration, waterproof enclosures, mast, solar/battery sizing, SIM/data, LoRa gateway backhaul, spares, technician visits, theft and cyclone survivability.

8. **Guaranteed satellite latency and entitlements.** A nominal revisit does not guarantee a usable scene immediately after landfall. EOS-04 products can enter a priced cart, while exact rates and tasking lead times are not stated [49].

9. **Drone mission readiness.** No public dataset supplies a ready pilot, compliant aircraft, local permission, safe weather window and mobilization contract for the affected block. These must be arranged before the event.

These are not small omissions. They define the boundary between a credible warning assistant and an unsupported automated-loss system.

## 5. HOW IT FEEDS THE ENGINE

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD cyclone, rain and district warnings | Trigger harvest, input relocation, drainage clearing, livestock shelter and pump protection by lead time | Identify when inspection is safe and where continuing rain threatens recovery | Attach official warning ID, issue time and affected district | Count repeated warning exposure by crop calendar | Time routine sowing, spraying and irrigation around five-day forecasts [53] |
| IMD/AWS observations | Confirm local rain, wind, humidity and pressure trend | Establish event timing and drying conditions | Add nearest-station series with distance disclaimer | Calibrate local thresholds and sensor bias | Irrigation and disease-risk guidance |
| CWC level/discharge and forecasts | Trigger riverine-flood escalation from level, warning state and rate of rise | Sequence access, drainage and re-entry around recession | Add gauge ID, hydrograph and timestamps | Identify chronically exposed river corridors | Reservoir/river-aware irrigation planning |
| INCOIS tide gauges and OSF | Combine high tide, waves and cyclone conditions for coastal drainage/storm-surge caution | Warn against saline-water access and unsafe coastal operations | Add nearest reporting gauge and data-quality status | Map recurring saline-inundation risk | Fishing/coastal work timing when outside disasters |
| INSAT QPE/cloud products | Detect storm organization and rainfall context between ground observations | Track residual convection | Regional event-context image, not parcel proof | Seasonal rainfall-pattern summaries | Broad cloud/rain scheduling |
| Sentinel-1 SAR | Pre-event baseline water mask and low-lying exposure | Map flood extent through cloud and darkness [27] | Before/after water extent, acquisition time and processing lineage | Repeated-inundation frequency by parcel | Wetland/water availability mapping |
| Sentinel-2 | Baseline crop/vegetation condition and field boundaries | NDVI/reflectance recovery after clouds clear | Before/after vegetation context with cloud mask | Crop vigor, fallow history and recovery duration | Nutrient/stress scouting support |
| EOS-04/RISAT-1A | Optional high-resolution SAR baseline or tasked acquisition | Detailed flood mapping where entitlement and scene timing work | Additional SAR evidence with NRSC product metadata | Crop and flood-history analysis | Soil-moisture/agriculture research uses [49] |
| Soil-moisture probe | Identify saturated plots where further rain creates waterlogging risk | Decide whether drainage, replanting or delayed field entry is appropriate | Time series from a calibrated device, with device ID | Compare crop response and irrigation efficiency | Irrigation scheduling |
| Plot rain gauge/mini AWS | Detect hyperlocal rain/wind missed by sparse stations | Establish local event magnitude and drying trend | Signed sensor record plus calibration/maintenance history | Local rainfall and microclimate profile | Spray, irrigation and disease timing |
| Water-depth/salinity field observation | Move assets before threshold crossing if a local depth sensor exists | Separate drainage, washout and salinity-response advice | Depth/salinity measurement with timestamp/location | Select drainage works, salt-tolerant crops and raised storage | Pond/soil management |
| Farmer profile and parcel polygon | Personalize action by crop stage, assets and exposure | Generate crop-specific recovery sequence | Link evidence to farmer, insured parcel and crop | Recommend variety/calendar changes | Routine localized crop advice |
| Farmer voice report | Capture low-literacy description and urgent needs | Triage blocked drainage, livestock or input needs | Transcript, original audio hash and reviewer disposition | Detect recurring farmer-reported failure modes | Question-answer advisory in Odia/local language |
| Farmer photo/video | Pre-event baseline of standing crop and stored assets | Document damage and identify cases for review | Geotag, timestamp, media hash, parcel match and duplicate check | Build labeled recovery outcomes | Pest/disease triage, with human escalation |
| SMS | Deliver short trigger, deadline and call-to-action on a basic phone | Send recovery sequence and office/helpline information | Confirm report receipt and missing fields | Seasonal reminders | Routine weather/agronomy nudges; mKisan already uses text/voice preferences [58] |
| IVR | Explain the same action in spoken Odia; collect keypad confirmation | Deliver stepwise recovery and record urgent requests | Capture consent and report reference number, not damage proof | Voice surveys and training | Spoken advisory for low-literacy users |
| USSD | Potential menu-based profile update without an app | Potential status lookup | Potential reference-number confirmation | Potential survey/menu | Only after operator/short-code partnership; current evidence proves phone capability, not open agriculture access [51] |
| WhatsApp | Rich optional alert with map/image for connected users | Photo upload and interactive support | Convenient intake channel with server-side audit copy | Rich media education | Optional supplement, never replacement for SMS/IVR |
| Drone orthomosaic/DSM | Rarely useful immediately before a cyclone unless a baseline exists | High-resolution mapping after weather and permissions allow | Parcel-scale visual/terrain exhibit subject to authority acceptance | Drainage and embankment planning | Farm layout and water-flow planning |

### Case study: From gauge trigger to farmer action

A workable pilot starts when CWC reports a fast-rising level at an Odisha forecast site and IMD predicts heavy rainfall. The rules engine intersects the threatened basin with village and parcel profiles, then sends a short SMS such as "Move seed and fertilizer above floor level before 18:00; press 1 for Odia call." The IVR explains crop-specific steps and records acknowledgement.

After the event, Sentinel-1 identifies inundated areas, while the farmer submits a voice report and photos. The system creates an evidence bundle containing source timestamps, parcel distance from the gauge, satellite acquisition metadata and original media hashes. It does not state "claim approved"; it states what was observed, by whom, when and with which confidence.

## 6. REAL-vs-FILLER

| Classification | Item | Evidence-based decision |
|---|---|---|
| **REAL NOW** | IMD warnings/forecast products | Use as the official event trigger after API onboarding; do not scrape presentation pages if an approved endpoint exists [4]. |
| **REAL NOW** | CWC hourly river data and 19-site Odisha forecast network | Build level, rate-of-rise and warning-state rules; retain station ID and timestamp [3][52]. |
| **REAL NOW, WITH HEALTH CHECKS** | INCOIS Odisha tide-gauge page | Poll last-report time and reject stale/not-reporting stations; a station list alone is insufficient [34]. |
| **REAL NOW** | Sentinel-1 and Sentinel-2 | Automate search/download through Copernicus APIs; store cloud mask, orbit/acquisition and processing lineage [27][5]. |
| **REAL AFTER ONBOARDING** | SMS and IVR | Implement through a DLT-compliant aggregator and voice provider; measure delivery, answer and completion rates. |
| **REAL AFTER SMALL HARDWARE PILOT** | Soil moisture, plot rain, water depth and salinity | Deploy only where each measurement changes a rule; calibrate against known references and budget maintenance. |
| **REAL AS INTAKE, NOT VERDICT** | Farmer photo/voice reports | Use for triage and claim-packet assembly; verify parcel, time, duplicates and hazard consistency. |
| **PARTNER-GATED** | INCOIS raw moored/wave/tsunami data | Public visualization is useful for a demo, but downloadable production feeds need an agreement where the portal says "no download" [28]. |
| **PARTNER-GATED** | USSD | It works on low-end phones, but no general agriculture short code/API was found; operator integration is the real project. |
| **PARTNER-GATED** | Drones | Contract an authorized operator for a defined post-event area; do not make a drone a prerequisite for every advisory. |
| **FILLER** | "AI hyperlocal forecast" created by interpolating sparse public stations | No public evidence establishes plot accuracy. Call it a model estimate and validate it against held-out gauges/sensors. |
| **FILLER** | A map of all IMD stations without current telemetry/status | Decorative coverage is not operational coverage. |
| **FILLER** | NDVI during cyclone cloud cover | Sentinel-2 is optical. Use Sentinel-1 for cloud-obscured flood extent and wait for clear optical imagery. |
| **FILLER** | A dashboard showing raw alerts without an action clock | The problem requires time-sensitive action, not another weather viewer. Every alert must produce actor, action, deadline and escalation path. |
| **FILLER** | "Blockchain claim verification" or an AI damage percentage from one photo | Neither establishes insured interest, event cause, affected area or authority acceptance. Preserve an auditable packet instead. |

### Case study: Why the six Odisha tide gauges do not equal six live feeds

The INCOIS station page is genuinely useful because it names six Odisha gauges and exposes last-report times. It also marks many national stations as "Not Reporting" [34]. The correct implementation therefore has a station-health layer: current, delayed, stale or unavailable. A demo pin that remains green whenever a station exists would be decorative; a status-aware trigger is operational.

### Case study: Why drones remain a targeted recovery tool

A 2026 provider guide places photogrammetry at INR 800-2,000 per acre, while a 10-acre example is INR 25,000-35,000 after mobilization [41]. That can be valuable for a concentrated high-loss pocket, but it is not economical or deployable as the first observation across every affected block. Sentinel-1 should triage the broad footprint; a compliant operator should then fly selected parcels where higher resolution changes recovery or assessment decisions.

## 7. NOISE LOG

| Search/discarded item | Why discarded or downgraded |
|---|---|
| Unrelated commercial "Ocean API" results | Not INCOIS and therefore not evidence of Indian public-ocean access. |
| Paradip tide-prediction websites | Predicted astronomical tides are not observed INCOIS gauge telemetry and do not prove storm-surge conditions. |
| ResearchGate station maps | Useful background, but not a current authoritative Odisha station census. |
| IMD national AWS/ARG totals | National counts do not answer how many operational instruments cover Odisha districts. |
| The proposed 10-Odisha-AWS procurement | Retained as design evidence only; discarded as proof of commissioning or current coverage. |
| Punjab/Assam IMD PDFs returned by station searches | Wrong state and irrelevant to Odisha coverage. |
| Reddit, Facebook and hobby soil-sensor posts | Useful for ideation, not defensible cost, calibration or field reliability. |
| Amazon component bundle | Wrong market/specification for an India field-node total; enclosure, sensor calibration, solar and gateway costs were not comparable. |
| Headline AWS prices of INR 30,090 and INR 250,000 | Retained only as quote anchors; packages were not specification-equivalent, so no false "average AWS price" was calculated. |
| Vendor IVR pricing guides | Retained as **C-grade budget benchmarks**, not contractual quotes; published estimates include setup, plan and hidden-fee caveats [48]. |
| USSD banking guides | Retained only to establish feature-phone capability. Banking's *99# access does not establish a purchasable agriculture USSD API. |
| WhatsApp provider rates | Retained as a provider quote, not a universal Meta bill; it does not satisfy the problem's basic-phone requirement by itself. |
| Stock-photo and generic crop-damage pages | No collection workflow, provenance or verification controls. |
| Plant-diagnosis marketing | Demonstrates photo intake but not cyclone-loss verification or insurer acceptance. |
| CCE App | Retained as an offline field-data pattern, but discarded as proof that a prototype can automatically approve a PMFBY claim. |
| Wikipedia EOS-04 result | Replaced by ISRO/NRSC primary sources. ISRO states that EOS-04 supports all-weather agriculture, hydrology and flood mapping [35]. |
| Drone spraying price per acre | Spraying and mapping have different aircraft, workflow, deliverables and economics; only mapping benchmarks were retained. |
| "Free RISAT" assumption | Rejected. Bhoonidhi includes both free and priced ordering paths, and the handbook gives no universal free entitlement [49]. |

**Noise-log insight:** The most common failure mode is category substitution: national counts for Odisha coverage, predictions for observations, visualization for API access, a sensor part for an installed node, or photo intake for verified loss. The prototype should expose these distinctions in its data catalog.

## 8. VERDICT AND SYNTHESIS: PARTIAL

### Final grade: **PARTIAL**

A credible prototype can use substantial free data today, but the complete system cannot be called free or fully open.

| Delivery tier | What can be built now | What remains gated | Decision |
|---|---|---|---|
| **Free public-data core** | IMD public warnings/products, CWC hourly levels and forecasts, live INCOIS tide visualization, Sentinel-1/2, public farm/profile forms | IMD API credentials, feed health, exact Odisha station census, automated INCOIS raw buoy access | **GO for prototype** |
| **Paid communications core** | DLT-compliant SMS API, outbound IVR, optional WhatsApp | Principal-entity/header/template setup, provider contract, Odia prompts, consent and delivery testing | **GO after onboarding** |
| **Field-data layer** | Farmer profile, voice/photo intake, a small soil-moisture/rain/water-depth pilot | Hardware procurement, calibration, installation, maintenance and cyclone hardening | **PARTIAL** |
| **Evidence/claim layer** | Timestamped packet with official alerts, river/tide series, satellite scenes, parcel and media hashes | Insurer/state schema, authorized assessor, legal acceptance and appeals | **GATED by partner** |
| **High-resolution assessment** | Sentinel triage and contracted drone survey of selected hotspots | DigitalSky compliance, pilot/operator, airspace, weather, mobilization and budget | **GATED by partner** |

### Synthesis across mechanism, scope, trade-offs and time horizon

IMD and CWC are **warning mechanisms**: they update quickly and support action before impact, but their spatial unit is station, district or basin rather than plot. INCOIS adds a **coastal mechanism**, but several raw networks offer visualization without download, and station uptime varies. These three families should determine urgency and escalation, not claim-level damage.

Sentinel-1, Sentinel-2 and EOS-04 are **spatial evidence mechanisms**. Sentinel-1 is the best default because it is free and sees through cloud and darkness; its trade-off is revisit timing and processing. Sentinel-2 adds vegetation detail at 10-20 m but waits on clear sky. EOS-04 adds Indian SAR modes down to 1 m, but access may be priced and its documented repeat is 17 days [49]. These sources are strongest after impact and for next-season exposure analysis.

Farm IoT and crowdsourcing are **plot-context mechanisms**. Sensors produce repeated measurements but cost money and fail without calibration and maintenance. Farmer reports are cheap and accessible but require provenance, deduplication and review. Drones provide the highest local spatial detail but have the narrowest operational scope and the highest mobilization/regulatory burden. The non-obvious conclusion is that "hyperlocal" should come first from a good parcel profile and farmer interaction, then from selective sensors, not from statewide hardware promises.

The recommended build order is:

1. **Wire the free core:** CWC hourly data, IMD approved products, INCOIS station health, Sentinel-1/2 and a versioned rule engine.
2. **Register the delivery core:** DLT-compliant SMS, Odia IVR, consent, retry and receipt logging.
3. **Pilot collection:** 50-100 representative farms with parcel/crop profiles, voice/photo intake and a small calibrated sensor subset.
4. **Create evidence packets:** retain original data, source time, processing lineage, confidence, reviewer and correction history.
5. **Secure partners:** IMD API access, INCOIS machine feeds, an Odisha agriculture/insurance authority and a DGCA-compliant drone operator.

The honest demo claim is therefore: **"The prototype generates auditable, time-sensitive advisories from official hazard feeds, public satellite data and farmer-specific inputs, and it prepares evidence packets for human review."** It should not claim complete Odisha sensor coverage, guaranteed claim approval, a free RISAT feed or plot-level accuracy without validation.

## References

1. *INCOIS - Ocean State Forecast (OSF)*. https://incois.gov.in/oceanservices/osfforecast.jsp
2. *INSAT-3D Data Products - MOSDAC*. https://www.mosdac.gov.in/insat-3d-data-products
3. *River Water Level (Telemetry - Hourly), Central Water ...*. https://nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc
4. *IMD APIs | India Meteorological Department*. http://mausam.imd.gov.in/responsive/apis.php
5. *Sentinel-2 - Copernicus Data Space Ecosystem*. https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2
6. *Drones Rules, 2021 dated 25 August 2021 - Ministry of Civil ...*. https://www.civilaviation.gov.in/ministry-documents/rules/drones-rules-2021-dated-25-august-2021
7. *IoT Soil Monitor for Farms: ESP32 + LoRa + Dashboard - Zbotic*. https://zbotic.in/iot-soil-monitor-for-farms-esp32-lora-dashboard
8. *IMD API Management*. https://api.imd.gov.in/public/index.php
9. *incois.gov.in*. https://incois.gov.in/site/services/osf.jsp
10. *Tcccpr | Telecom Regulatory Authority of India | Government of India*. https://trai.gov.in/tcccpr
11. *MoES- Earth System Science Data Portal*. https://incois.gov.in/essdp/ViewMetadata?fileid=3ead22ae-aa2c-464f-8974-85ede650d2d0
12. *Advice to Senders | Telecom Regulatory Authority of India | Government of India*. https://trai.gov.in/advice-to-senders
13. *MoES- Earth System Science Data Portal*. https://incois.gov.in/essdp/ViewMetadata?fileid=3d56ae21-e751-4e1e-9581-e0e6b5f2abf9
14. *Welcome to DigitalSky*. https://digitalsky.dgca.gov.in/
15. *Flood Forecast - Central Water Commision, Govt. Of India*. https://ffs.india-water.gov.in/
16. *Bhoonidhi Home*. https://bhoonidhi.nrsc.gov.in/bhoonidhi/home.html
17. *Crop Insurance Portal*. https://www.ncfc.gov.in/downloads/Workshop_PMFBY_29july2016/Crop%20Insurance%20Portal.pdf
18. *SMS Pricing in India | MSG91-India*. https://msg91.com/in/pricing/sms
19. *SMS Pricing in India for Text Messaging | Twilio*. https://www.twilio.com/en-us/sms/pricing/in
20. *Communication Network - Indian National Center for Ocean Information Services (INCOIS)*. https://incois.gov.in/site/services/comm-network.jsp
21. *Odisha*. https://mausam.imd.gov.in/bhubaneswar/
22. *CCE App - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en_US&id=com.farmguide.imagine.ccecentral.release
23. *Water Resources Information System (WRIS) | Central Water Commission, Ministry of jal shakti, Department of Water Resources, River Development and Ganga Rejuvenation, GoI*. https://cwc.gov.in/en/water-resources-information-system-wris
24. *INSAT-3DR Data Products | Meteorological & Oceanographic Satellite Data Archival Centre*. https://mosdac.gov.in/insat-3dr-data-products
25. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://pmfby.gov.in/
26. *Pricing on the WhatsApp Business Platform | Developer Documentation*. https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
27. *Sentinel-1 – Documentation*. https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel1.html
28. *Data Holdings - Indian National Center for Ocean Information Services (INCOIS)*. https://incois.gov.in/site/dataholdings.jsp
29. *tsunami.incois.gov.in*. https://tsunami.incois.gov.in/TEWS/Link.do?function=tgChartNat&stationName=Cochin&sensorName=RAD&timePeriod=1&flag=0
30. *Plantix | #1 FREE app for crop diagnosis and treatments*. https://plantix.net/en
31. *Drone Survey Cost in India: Factors, Prices, and ROI Explained*. https://asteria.co.in/blog/drone-survey-cost-india
32. *Technical Specfication Document For Procurement, Installation and commissioning of 10 Nos GPRS based Automatic Weather Stations in the Odissa Government*. https://mkp.gem.gov.in/uploaded_documents/51/16/877/OrderItem/BoqDocument/2023/10/12/specification_of_gprs_based__aws_for_odisha_2023-10-12-10-32-09_b6f3bd8879a0b57352e26430835a4a3a.pdf
33. *Digital Green | AI for Farmers, by Farmers*. https://www.digitalgreen.org/
34. *tsunami.incois.gov.in*. https://tsunami.incois.gov.in/TEWS/Link.do?function=tgStationList
35. [
   EOS-04
  ](https://www.isro.gov.in/mission_PSLV_C52_EOS_04.html)
36. *cloud IVR Solutions India - hosted ivr solution,hosted ivr services:Kookoo*. https://in1-cpaas.ozonetel.com/index.php/pricing
37. *EOS-04 - Wikipedia*. https://en.wikipedia.org/wiki/EOS-04
38. *Ozonetel Plans & Pricing: Full Guide for 2026 - CloudTalk*. https://www.cloudtalk.io/blog/ozonetel-pricing
39. *FarmerChat – Digital Green*. https://digitalgreen.org/farmer-chat
40. *DIY ESP32 solar LoRa + GPS node - Hackster.io*. https://www.hackster.io/powerfeatherdev/diy-esp32-solar-lora-gps-node-5c64be
41. *Drone Survey Cost in India 2026: Per Acre Pricing & Complete Guide*. https://www.airotor.in/blog/drone-survey-cost-in-india-2026-per-acre-pricing-guide
42. *USSD and SMS solutions for Today’s Landscape - Neural Technologies*. https://www.neuralt.com/news-insights/ussd-and-sms-solutions-for-todays-landscape
43. *USSD Banking - Unstructured Supplementary Service Data*. https://www.bankbazaar.com/ifsc/ussd.html
44. *Indian National Centre for Ocean Information Services (INCOIS)*. https://incois.gov.in/site/index.jsp
45. *Ln 11 57 Notes On Aws And Arg*. https://imdpune.gov.in/training/icitc/LN_11_57_Notes%20on%20AWS%20and%20ARG.pdf
46. *ESP32 - Rain Sensor | ESP32 Tutorial*. https://esp32io.com/tutorials/esp32-rain-sensor
47. *Amazon.com: Meshnology ESP32 Lo Ra V3 Development Board + 1100mAh Battery + Case + USB Charger Cable Set - with 915MHz Antenna and SX1262 Lo Ra V3 Devices for Mesh Tastic Ar duino Lo Rawan IOT (N30,4-in-1,Black) : Electronics*. https://www.amazon.com/ESP32-Development-1100mAh-Battery-Charger/dp/B0F4XPYLXR
48. *IVR Pricing in India: Complete Cost Guide 2026*. https://bonvoice.com/insights/ivr-pricing-in-india
49. *Eos 04 Handbook*. https://bhoonidhi.nrsc.gov.in/bhoonidhi_resources/help/docs/EOS-04_Handbook.pdf
50. *Drone Survey Cost in India 2025 — LiDAR, Photogrammetry, DGPS Pricing Guide | Dronimagination*. https://www.dronimagination.com/blog/drone-survey-cost-india-2025.html
51. *Microsoft Word - MBTS_IDRBT*. https://www.idrbt.ac.in/wp-content/uploads/2024/07/MBTUSSD_IDRBT.pdf
52. *RAJYA SABHA UNSTARRED QUESTION NO. 891 FLOOD FORECASTING ...*. https://sansad.in/getFile/annex/262/AU891.pdf?source=pqars
53. *http://pib.gov.in/PressReleasePage.aspx?PRID=2223075*. http://pib.gov.in/PressReleasePage.aspx?PRID=2223075
54. *http://digitalgreentrust.org/*. http://digitalgreentrust.org/
55. *Automatic Weather Station Products at price INR 30090 ... Gaby Instruments https://www.gabyinstruments.in › products › automatic-...*. https://www.gabyinstruments.in/products/automatic-weather-station/430
56. *Automatic Weather Station Setup at 250000.00 INR ... Tradeindia https://www.tradeindia.com › products › automatic-wea...*. https://www.tradeindia.com/products/automatic-weather-station-setup-6832213.html
57. *WhatsApp Business API Pricing in India (2026)*. https://aisensy.com/pricing
58. *http://mkisan.gov.in/*. http://mkisan.gov.in/
