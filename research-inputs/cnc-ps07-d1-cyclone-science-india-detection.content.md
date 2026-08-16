# Odisha Cyclone Data: From Science to Farm Action

## 1. EXECUTIVE SUMMARY

- **A free official warning core exists**: IMD publishes named JSON endpoints for cyclone track, wind-warning polygons, and cone-of-uncertainty polygons, while its public cyclone page carries national, hourly, wind, surge, track, and archive products. This is enough for a prototype ingestion adapter, but the published reference does not state authentication rules, rate limits, pricing, update latency, or an SLA. Build polling, caching, schema validation, and a bulletin-PDF fallback rather than assuming production-grade API access. [36]

- **Cyclone formation is a heat-engine process, not an SST-only rule**: WMO training material calls for a warm upper ocean, background cyclonic rotation and Coriolis, deep moisture, organized convection, and weak vertical shear. It cites water warmer than about 26 C extending to roughly 60 m, mid-level relative humidity above 70%, and notes that genesis generally does not occur when 850-200 hPa shear exceeds 20-25 kt, while preserving exceptions. These variables explain risk but should not replace IMD alerts as an operational trigger. [8]

- **The Bay has two practical risk seasons**: pre-monsoon systems cluster around May-June, while the stronger climatological peak is post-monsoon, especially October-November. IMD's science plan says more than half of disturbances forming in March-May and November-December intensify into storms, and October systems more often strike the Odisha-West Bengal coast. Pre-load farmer profiles and action plans before both windows. [20]

- **The complete IMD hazard scale is directly machine-codable**: depression begins at 17 kt, cyclonic storm at 34 kt, very severe cyclonic storm at 64 kt, extremely severe at 90 kt, and super cyclonic storm at 120 kt. IMD also publishes crop, housing, road, power, fishing, and evacuation descriptors for each storm class, allowing transparent rules rather than opaque AI-generated advice. [11]

- **Odisha is observed by a layered system, not one sensor**: the Dana report documents actual use of INSAT-3DR, Oceansat-3 scatterometer data, ASCAT, microwave imagery, Paradip and Gopalpur DWRs, ships, buoys, and coastal observations. INSAT-3DS was launched on 17 February 2024 and began imaging with a 6-channel imager and 19-channel sounder on 7 March 2024. The public evidence proves these assets exist, but does not provide a live Odisha DWR coverage, blind-zone, calibration, or uptime map. [14][32]

- **Forecast availability is not the same as farmer lead time**: IMD's formal stages are Pre-Cyclone Watch at 72 hours, Cyclone Alert at least 48 hours, Cyclone Warning at least 24 hours, and Post-Landfall Outlook at least 12 hours before expected landfall. Cyclone warnings are normally updated every 3 hours, but no public source reviewed measures when a particular farmer received, understood, and acted on the warning. The platform must log delivery, playback, acknowledgement, and action separately. [5][11]

- **Forecast uncertainty must remain visible**: in 2024, across only four cyclones, basin-average track errors were 66, 84, and 116 km at 24, 48, and 72 hours; absolute intensity errors were 4, 5, and 5 kt. The small sample and unusually low 72-hour landfall-point error make these verification statistics unsuitable as fixed parcel-level guarantees. Display the official cone and horizon, not a single deterministic village-level landfall line. [16]

- **Historical performance supports action-oriented design**: the 1999 super cyclone had more than 48 hours of official warning but still caused 9,893 reported deaths and damaged 1.9M houses; Phailin was predicted 4-5 days in advance and Dana had a pre-cyclone watch about 4.5 days ahead. Better forecasts help, but evacuation capacity, trusted channels, farm-specific instructions, and response confirmation determine realized protection. [23][15][14]

- **The verdict is PARTIAL**: a free prototype can ingest official hazards, collect a small consented farm profile, issue rule-based SMS/IVR advisories, and assemble a time-stamped claim packet. Production is gated by stable IMD access, telecom and IVR delivery, OSDMA and Agriculture Department coordination, insurer linkage, and collection of parcel crop stage, farmer language, delivery outcomes, and verified losses. PMFBY's 72-hour intimation requirement makes the claim-packet feature immediately useful. [38]

## 2. DATA INVENTORY

### 2.1 Science and seasonality

A tropical cyclone is an organized, rotating, warm-core low-pressure system sustained by heat and moisture flux from a warm ocean. The SST threshold is a necessary-condition heuristic, not a binary detector: the WMO material used here states warmer than about 26 C through roughly 60 m, while the literature commonly uses 26-27 C. Background rotation and Coriolis supply spin, humid convection maintains latent heating, and weak shear allows the low- and upper-level circulation to remain aligned. [8]

The Bay of Bengal's warm pool, low-salinity upper water, monsoon trough, imported disturbances from the western North Pacific, and intraseasonal convection all support genesis or intensification. The often-repeated "shallow shelf and funnel" explanation should be assigned to coastal surge and inundation amplification, not to cyclone genesis itself. IMD's science plan ties surge prediction to storm intensity, landfall position, winds, bathymetry, and coastal resolution. [20]

### 2.2 Named data inventory

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade |
|---|---|---|---|---|---|
| Formation physics | WMO, *Cyclogenesis*, 2019, https://severeweather.wmo.int/TCFW/13WMO_Workshop2019/03_TC_genesis_WMO2019.pdf | Physical conditions and operational concepts; not a live dataset | Static training document | Free PDF | A |
| Bay seasonality and mechanisms | IMD, *Forecast Demonstration Project: Bay of Bengal Tropical Cyclone Experiment Science Plan*, publication date not shown, https://rsmcnewdelhi.imd.gov.in/images/pdf/cyclone_science_plan.pdf | Basin, month, process, research priorities | Static; access checked 16 Aug 2026 | Free PDF | A- |
| IMD intensity classes and damage descriptors | IMD, *Cyclone Warning in India: Standard Operation Procedure*, July 2024, https://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf | Wind class in kt and km/h; expected impacts and actions | Versioned report | Free PDF | A |
| INSAT-3DS status and payload | ISRO, *INSAT-3DS begins imaging the Earth*, 11 Mar 2024, https://www.isro.gov.in/INSAT-3DS_imaging_Earth.html | National geostationary coverage; payload-level metadata | Event/status page | Free web page | A |
| INSAT-3D/3DR products | MOSDAC, *INSAT-3D Data Products* and *INSAT-3DR*, updated site checked 16 Aug 2026, https://www.mosdac.gov.in/insat-3d-data-products and https://www.mosdac.gov.in/insat-3dr | Multispectral imagery, winds, SST, humidity, precipitation products | Near-real-time and archive, product dependent | Registration/download; HDF products; user-tier limits apply | A- |
| Odisha DWR display | IMD Paradip and Gopalpur radar pages, accessed 16 Aug 2026, https://mausam.imd.gov.in/imd_latest/contents/index_radar.php?id=Paradip and https://mausam.imd.gov.in/imd_latest/contents/index_radar.php?id=Gopalpur | Radar image; public page shows last 3 hours | Operational display, but uptime not stated | Free web display, no documented stable feed on page | B |
| Assets used for Dana | IMD, *Severe Cyclonic Storm Dana*, 7 Nov 2024, https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf | Event-specific sensor provenance | Post-event report | Free PDF | A |
| Surface and upper-air observation families | IMD Cyclone SOP, July 2024 | Land stations, AWS, ships, buoys, tide gauges, pilot balloon, radiosonde/radiowind, wind profilers | Operational network; station-specific status varies | Bulletins/reports; no single reviewed open Odisha status API | A for method, C for local availability |
| Current cyclone products | IMD Cyclone Information, accessed 16 Aug 2026, https://mausam.imd.gov.in/responsive/cycloneinformation.php | National/hourly bulletin, track, wind, surge, interactive track, preliminary report | Event-driven; 6-hourly at depression stage and 3-hourly at cyclone stage | Free web/PDF/graphics | A- |
| Cyclone JSON endpoints | IMD API Reference, accessed 16 Aug 2026, https://api.imd.gov.in/public/api_reference.html | Track points plus wind and cone polygons | No endpoint update SLA stated | Documented JSON/GeoJSON-style API; onboarding conditions unclear | B+ |
| Forecast verification | RSMC New Delhi, *Annual Verification Report on Cyclonic Disturbances during 2024*, 2024, https://rsmcnewdelhi.imd.gov.in/uploads/Annual_Veri_2024.pdf | Track, intensity, landfall point and time by forecast lead | Annual | Free PDF | A |
| Long historical tracks | IMD Cyclone eAtlas, 1891 to latest year, http://14.139.191.203/AboutEAtlas.aspx | North Indian Ocean cyclone/depression tracks | Annual or irregular archive update | Free interactive atlas; bulk-machine contract not established | B+ |
| Event reports | IMD/RSMC reports for 1999, Phailin, Fani, Yaas, Dana; URLs in Sources | Event track, intensity, forecast verification, selected impacts | Post-event | Free PDFs | A |
| Odisha siren and mass-warning footprint | OSDMA, *Early Warning Dissemination System*, commenced 23 Nov 2015 and implemented 9 Jul 2016, https://www.osdma.org/preparedness/early-warning-communications/ewds | 1,205 villages, 22 blocks, 6 coastal districts, 122 alert towers | Infrastructure page; live health not exposed | Government system; public description, partner access needed | A for design, C for live status |
| Farmer SMS and public dissemination | IMD Cyclone SOP, July 2024 | Registered-farmer SMS plus radio, TV, CAP, apps, IVRS, social media and marine channels | Event-driven | Free reception; sender integration requires partner/onboarding | A |
| Agromet advice | Meghdoot and IMD/ICAR agromet services; PIB announcement 2021, https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1739245 | District/crop advisory in the consumer service; machine-feed terms not established in reviewed page | Periodic, not cyclone-bulletin cadence | App/web; no reviewed public advisory-generation API | B- |
| Flood forecast | CWC Flood Forecasting and Hydrological Observation, accessed 16 Aug 2026, https://cwc.gov.in/flood-forecasting-hydrological-observation | Gauge/basin warning; severe-flood Orange Bulletin updated every 3 hours | Operational | Free web/bulletin; integration terms need checking | A- |
| Claim rules | MoAFW, *PMFBY Revised Operational Guidelines*, revised edition, https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf | Farmer, survey number, crop, affected acreage, event evidence and deadlines | Scheme version dependent | Free PDF and portal; insurer/NCIP linkage needed | A |
| Odisha crop statistics | Odisha Agriculture Department, *Agriculture Statistics 2023-24*, https://agri.odisha.gov.in/en/page/statistics | Published aggregate statistics; public page does not expose farmer or parcel records | Annual and lagged | Free reports | B for planning, D for live farm state |
| Hyperlocal farmer profile | No complete public source found | Required parcel, crop, variety, sowing date, stage, irrigation, storage, livestock, insurance and contact data | Must be continuously updated | Consent-based registration, extension verification and field collection | D until collected |

**Grade key**: A = authoritative primary source suitable as a source of truth; B = official or institutional but incomplete, manual, or lacking a stable interface; C = discovery/display value with material operational uncertainty; D = absent publicly or dependent on local collection.

### 2.3 Exact IMD classification and typical agricultural damage

| IMD class | Maximum sustained wind | Typical IMD damage relevant to a farm advisory |
|---|---:|---|
| Depression | 17-27 kt; 31-49 km/h | No class-specific damage table in the reviewed SOP; monitor rainfall, waterlogging and escalation. |
| Deep Depression | 28-33 kt; 50-61 km/h | No class-specific damage table in the reviewed SOP; prepare movable assets and check drainage. |
| Cyclonic Storm | 34-47 kt; 62-88 km/h | Thatched-hut damage; branches may break power/communication lines; kutcha roads damaged; some damage to paddy, banana, papaya and orchards; low-lying seawater inundation possible. |
| Severe Cyclonic Storm | 48-63 kt; 89-117 km/h | Major thatched-house and coastal-crop damage; roofs and metal sheets may fail; trees fall; roads and escape routes flood; embankments and salt pans may be damaged. |
| Very Severe Cyclonic Storm | 64-89 kt; 118-167 km/h | Extensive kutcha-house damage; power poles bend or fall; widespread standing-crop, plantation and orchard damage; boats may break moorings. |
| Extremely Severe Cyclonic Storm | 90-119 kt; 168-221 km/h | Extensive damage to standing crops, plantations and orchards; coconut and palm trees may fall; transport and communications can be widely disrupted. |
| Super Cyclonic Storm | >=120 kt; >=222 km/h | Total destruction of standing crops/orchards is possible, with severe building, bridge, road, rail, port, power and communications damage and large-scale coastal inundation. |

The thresholds come from IMD's classification table; the impact language is condensed from its damage/action tables. The source occasionally differs by 1 km/h between classification and damage tables because of conversion and endpoint conventions, so the engine should store knots as canonical and render rounded km/h to users. [11]

### 2.4 What the app receives, and when

| Stage or product | Official timing | App-usable content | Required behavior |
|---|---|---|---|
| Tropical Weather Outlook / pre-genesis monitoring | Before a named cyclone; schedule depends on product | Formation potential and basin context | Pre-stage profiles and templates; do not order costly actions solely from a model rumor. |
| Pre-Cyclone Watch | About 72 h before adverse weather | Likely development, intensification and threatened coastal belt | Confirm farmer location/crop stage, begin low-regret actions, test IVR and backup contacts. |
| Cyclone Alert, yellow | At least 48 h before adverse weather | Location, intensity, direction, likely intensification, affected coastal districts and advice | Send prioritized crop/livestock/storage actions; request acknowledgement. |
| Cyclone Warning, orange | At least 24 h before adverse weather; updates normally every 3 h | Landfall point/time, rain, wind, surge, expected impacts and official actions | Stop non-essential field work; escalate evacuation and asset protection; repeat by SMS and voice. |
| Post-Landfall Outlook, red | At least 12 h before expected landfall | Inland movement and post-landfall adverse weather | Keep inland/watershed farms warned; pre-stage recovery and claim workflows. |
| Track/cone/wind API | Event-driven; no public SLA in reference | Coordinates, observation time, category, wind polygon and cone polygon | Geospatially intersect with farms, retain source timestamp and expiry, and reject stale data. |
| CWC severe-flood bulletin | Every 3 h in severe situations | Gauge/basin flood status and special flood message | Combine with IMD rain and local elevation/drainage; never equate a gauge warning to parcel depth. |

The four cyclone stages and their colors are related but not identical: yellow starts at Cyclone Alert, orange at Cyclone Warning, and red at Post-Landfall Outlook; the Pre-Cyclone Watch is the first stage but is not assigned one of those three colors in the cited table. [11]

### 2.5 Historical Bay of Bengal event record

| Event | Track, peak and landfall | Documented impact | Warning lead achieved | Engine lesson and ideal use |
|---|---|---|---|---|
| 1999 Odisha Super Cyclone, 25 Oct-1 Nov | Super cyclonic storm; an IMD synopsis reports 120 kt and 260-270 km/h core winds, while a radar study reports a 140 kt best-track estimate. Landfall was near/south of Paradip on 29 Oct. | 9,893 reported deaths, 14 districts and 120 blocks affected, 1.9M houses damaged, 2.5M people marooned, major salinization and livestock loss; reported total damage USD 2.5B. | Bhubaneswar issued warning on 26 Oct, more than 48 h before impact. | Long meteorological lead did not guarantee protection. The engine must pair warning with evacuation, trusted voice, last-mile confirmation and explicit livestock/seed/document actions. [23] |
| Phailin, 8-14 Oct 2013 | Peak 115 kt; crossed near Gopalpur at about 2230 IST on 12 Oct, with best-track landfall wind 100 kt. | 12,396,065 people affected; 21 cyclone deaths plus 17 flood deaths; 668,268 ha of crops and 419,052 houses affected/damaged. | Genesis, track, intensity, landfall and hazards predicted 4-5 days ahead; landfall-point errors were 2-13 km at 12-72 h. | Use 72-120 h for low-regret preparation and 24-48 h for irreversible actions. Retain flood advice after the wind threat falls. [15] |
| Hudhud, Oct 2014 | NASA describes a Category 4 storm striking India's southeastern coast. The precise IMD track/landfall record was not recovered from a stable primary archive in this run, and Hudhud should not be mislabeled as an Odisha landfall. [46] | A normalized Odisha-specific crop/property-loss row was not found. | Comparable event-level warning lead was not found in the reviewed authoritative pages. | Keep the event in a regional-effects set, but do not train an Odisha landfall model on an unverified row. Resolve the IMD 2014 archive before production. |
| Fani, 26 Apr-5 May 2019 | Peak 115 kt; crossed close to Puri between 0800 and 1000 IST on 3 May with 175-185 km/h sustained wind, gusting to 205 km/h. | A joint Odisha-UN-World Bank-ADB DLNA exists, but its quantitative damage table was not exposed in the source page retrieved here; the IMD summary used here does not provide quantified Odisha crop loss. | First track, intensity and landfall information and cyclone watch about 90 h before landfall. At 24/48/72 h, landfall-point errors were 11/11/15 km and time errors 1.5/5.5/14.5 h. | Forecast landfall time can shift materially at longer horizons even when the point is good. Schedule advice by deadline and reversibility, not just distance to the track. [13][45] |
| Amphan, 16-21 May 2020 | Peak 130 kt super cyclonic storm; crossed the West Bengal-Bangladesh Sundarbans on 20 May at about 90 kt. It affected Odisha but was not an Odisha landfall. | The cited IMD summary reports 98 deaths overall, not an Odisha-only count. OSDMA lists preparedness notifications from 15 May and a restoration/damage report dated 23 May, but the retrieved page does not expose a normalized crop-loss total. | An Odisha preparedness notice existed on 15 May; exact farmer receipt and event-level forecast errors are absent from the reviewed page. | Separate "Odisha affected" from "Odisha landfall." Avoid copying basin-wide deaths or damage into a state claim model. [11][39] |
| Yaas, 23-28 May 2021 | Peak and landfall 75 kt, gusting 85 kt; crossed about 20 km south of Balasore between 1030 and 1130 IST on 26 May. | Two Odisha deaths; 2-4 m surge in low-lying Balasore/Bhadrak and 1-2 m in Kendrapara/Jagatsinghpur; quantified crop/property loss absent from the IMD report used here. | First bulletin about 72 h before landfall. Track errors at 24/48/72 h were 24.1/53.1/81.6 km; time errors at 12/24/48/60 h were 1/1/2.5/3.5 h. | Surge zone and flood route matter more than center-line distance. Trigger evacuation and livestock movement from surge polygons and local elevation. [21] |
| Dana, 22-26 Oct 2024 | Peak 60 kt; crossed between Bhitarkanika/Habalikhati and Dhamra from 0130 to 0330 IST on 25 Oct with 100-110 km/h wind, gusting to 120 km/h. | About 5,800 homes damaged, 800,000 people evacuated, 3.595M people affected in 14 districts, and no reported Odisha cyclone death; quantified crop effects absent from the IMD report. | Pre-Cyclone Watch about 4.5 days ahead and pre-genesis track/intensity/landfall prediction about 3.5 days ahead. At 24/48/72 h, point errors were 4/2/2 km and time errors 2.5/0.5/0.5 h. | Demonstrates excellent event-specific performance, but one storm cannot define future error bars. Continue showing cone, issue time, and uncertainty. [14] |

The historical archive is strong for meteorology but uneven for state-specific agricultural loss, actual farmer receipt, and normalized lead time. It is suitable for scenario replay and rule testing, not for loss prediction without a separately curated outcome dataset.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing material | Coverage judgment |
|---|---|---|---|
| IMD/RSMC SOP, annual verification and event reports | Exact wind scale, damage descriptors, warning stages, forecast products, sensor families, event tracks and verification | Some old event URLs are difficult to discover; crop loss and public-receipt outcomes are inconsistent across reports | A for cyclone science and warning; B for agricultural outcomes |
| IMD API and current cyclone pages | Track, wind and cone endpoint definitions; public bulletins, graphics and archives | No public rate limit, SLA, authentication workflow, retention guarantee, or endpoint update contract in the reviewed reference | B+ |
| ISRO/MOSDAC | INSAT-3D/3DR/3DS mission, payload and product evidence | Product-specific latency, reuse and user-tier conditions require onboarding; a satellite image alone is not an advisory | A- |
| Odisha government and OSDMA | EWDS footprint, event notices, Agriculture Statistics and some cyclone-specific advisories | No live siren-health API, parcel crop state, unified damage dataset, or farmer delivery telemetry | B |
| INCOIS/NIOT/ocean observations | Buoys and marine observing capability; IMD event reports confirm buoy use | No reviewed public event provenance identifying which buoy/observation changed a warning | B- |
| CWC flood systems | Severe-flood Orange Bulletins every 3 h and public forecast portals | Gauge/basin output is not parcel inundation depth; API and state-station completeness need implementation testing | B+ |
| PMFBY and insurer systems | 72-hour intimation, survey-number/crop/acreage fields, evidence and assessment workflow | Farmer policy/enrollment, insurer identity, notified crop and claim status are not available as a universal open feed | A for rules, C for integration |
| Meghdoot, mKisan and Kisan Call Centre | Existing farmer-facing advisory and voice ecosystem; IVRS supports farmer feedback in 12 languages | No reviewed open feed that converts a cyclone polygon plus farm profile into Odia SMS/IVR; consumer access does not equal integration access | B- |
| Academic, WMO, NASA and multilateral sources | Genesis theory, independent event context and damage-assessment discovery | Often not current operational truth; terminology and wind scales can differ from IMD | B for context, C for triggering |
| Local field collection | Can supply crop stage, assets, language, consent, receipt, actions and observed loss | Cost, privacy, update burden and verification risk | D initially; potentially A after governed collection |

**Coverage judgment**: the science-to-warning chain is well covered. The warning-to-farm-decision and farm-decision-to-measured-outcome chains are not. That distinction drives the PARTIAL verdict. [11]

## 4. WHAT IS MISSING

The following fields were not covered by a complete, authoritative public source in the reviewed material. They should be named as product requirements, not silently inferred:

1. **Live Odisha DWR coverage and health**: georeferenced range, beam blockage, blind zones, maintenance state, calibration, last successful scan and outage history for Paradip and Gopalpur. The public pages prove displays exist, not uninterrupted coverage. [2][1]
2. **Observation provenance per warning**: which buoy, ship, coastal station, radiosonde or scatterometer observation was assimilated, its quality flag, and whether it materially changed track or intensity.
3. **Parcel-level farm state**: latitude/longitude or polygon, elevation, drainage outlet, crop, variety, sowing/transplanting date, phenological stage, acreage, irrigation, soil salinity, standing water, harvest status, storage, machinery and livestock.
4. **Farmer communication profile**: verified phone, preferred Odia/dialect, literacy and voice preference, safe calling hours, household proxy, consent, opt-out status and device/network constraints.
5. **Actual last-mile lead time**: bulletin issue -> platform receipt -> SMS delivery -> IVR answered -> message completed -> farmer understood -> action taken. IMD's 72/48/24-hour stages measure issuance, not this chain. [5]
6. **Action and outcome ground truth**: which action was taken, when, cost, avoided loss, crop survival, livestock survival and reasons for non-action.
7. **Parcel-scale flood and surge depth**: time-varying inundation depth, salinity, drainage duration and road access. A basin/gauge warning or cyclone-center distance is not a substitute.
8. **Normalized historical agriculture loss**: event-by-event crop, stage, district/block, acreage, input loss, yield loss, livestock, salinity and recovery duration using consistent definitions.
9. **Production API contract**: keys, onboarding, rate limits, latency, schema versioning, archive retention, downtime status, licensing and SLA for IMD cyclone endpoints.
10. **Versioned recovery knowledge base**: Odisha crop- and stage-specific post-waterlogging, lodging, salinity, seed, livestock and food-safety actions approved by OUAT/ICAR/Agriculture Department, with contraindications and expiry dates.
11. **Insurance linkage**: current scheme, notified crop, insurer, policy/application number, survey number, insured acreage, coverage dates and claim status.
12. **Complete comparable Hudhud and Amphan Odisha rows**: authoritative state-specific damage, forecast lead and farmer-receipt fields were not available in the retrieved event pages.

These are not minor enrichment fields. Without items 3-6, the platform can broadcast hazards but cannot prove that advice was hyperlocal, accessible, acted upon, or effective.

## 5. HOW IT FEEDS THE ENGINE

The engine should implement a deterministic **hazard x exposure x vulnerability x deadline** framework. IMD remains the hazard authority; local data determines who is exposed and which approved action is feasible. AI can summarize and translate approved rules, but it should not invent a landfall, wind class, claim rule or pesticide recommendation.

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD track and cone | Select farms inside affected districts/polygons; prioritize by time to hazard | Identify likely inspection corridor | Save source JSON/PDF, issue time and farm-cone intersection | Map repeated exposure and evacuation constraints | Use outer-cone farms for low-cost preparation without premature destructive harvest |
| Wind polygon and IMD class | Tie trees, protect pumps, move tools, reinforce thatch, stop field work and fishing at approved thresholds | Inspect roofs, poles, treefall and lodged crops safely | Record official class and polygon at the parcel timestamp | Upgrade storage, anchoring and windbreak plans | Schedule safe pruning or support before the next risk season |
| Rain, surge and CWC flood status | Clear drains, move seed/fertilizer/livestock upward, protect freshwater sources | Wait for safe access; record water depth/duration; manage drainage and salinity under approved guidance | Add gauge/bulletin, geotagged water marks and timed photos | Redesign drainage, raised storage and evacuation routes | Capture safe excess rainwater where approved; reduce unnecessary irrigation before forecast rain |
| Satellite, microwave and DWR observations | Confirm rapid evolution and local rain bands through official bulletins | Establish event timing and broad flood extent | Supporting evidence only, not parcel-loss proof | Replay cases and test rules | Improve timing of irrigation or harvest windows after all-clear |
| Farmer parcel and elevation | Decide whether wind, surge, river flood or waterlogging is dominant | Route inspection and recovery by access/elevation | Supply survey number, location and affected acreage | Rank drainage, embankment and crop-diversification needs | Match normal-season water management to local terrain |
| Crop, variety, stage and harvest status | Choose among early harvest, drainage, staking, delayed sowing, input protection and no-action | Generate stage-specific re-sowing, lodging, rot and salinity workflow only from approved agronomy | State insured crop, acreage and pre-event condition | Adjust sowing windows, variety and seasonal risk strategy | Exploit forecast rain for sowing or saved irrigation when agronomically safe |
| Livestock, aquaculture and stored inputs | Move animals/feed, secure ponds/nets, protect seed, fertilizer and documents | Water/feed safety, carcass reporting, pond breach and disease surveillance | Photograph and itemize losses with timestamps | Raised shelters, backup fodder, pond embankment plans | Refill ponds or water stores only after quality and salinity checks |
| Farmer language/channel profile | Send short Odia SMS plus IVR; repeat critical action; route unanswered calls to a proxy or worker | Voice-led checklists and helpline routing | Prompt before the 72-hour claim deadline | Improve message timing and trust from feedback | Deliver routine beneficial weather advice, not only disaster alerts |
| Delivery and acknowledgement telemetry | Escalate undelivered or unheard messages; trigger human follow-up | Confirm safety and inspection availability | Prove advisory issue/delivery, but do not misrepresent it as proof of loss | Evaluate which channel and wording changes behavior | Personalize cadence without excluding non-smartphone users |
| Historical best tracks and reports | Scenario-test rules and expected update frequency | Pre-build recovery playbooks by hazard combination | Supply official event identity and timeline | Compare exposure under 1999, Phailin, Fani, Yaas and Dana scenarios | Conduct pre-season drills and farmer training |
| IMD damage descriptors | Convert wind class into an explainable action shortlist | Initialize inspection checklist | Contextual evidence, not automatic compensation | Prioritize resilient storage, roads, power and communications | Show why a low-cost action is recommended |
| Geotagged, time-stamped photos and farmer statement | Capture pre-event baseline only with consent and enough warning | Capture post-event condition safely | Required packet: claim form, survey-number crop/acreage, timestamps, photos and supporting IMD/media evidence | Create labeled outcomes after insurer or extension verification | Document successful protection practices |
| Policy and insurer profile | Warn only eligible farmers about the exact notified procedure | Route to insurer/bank/agriculture office/NCIP | Trigger immediate intimation within 72 h; track assessor and deadlines | Review coverage gaps before next season | Encourage timely enrollment without promising claim approval |

PMFBY requires immediate farmer intimation within 72 hours, with survey-number-wise insured crop and affected acreage. It permits notification through the insurer, bank, Agriculture Department, district officials, toll-free channel or NCIP, and recognizes supporting photos, IMD reports, media and local newspaper evidence for localized loss. [38]

### Decision sequence

1. **Ingest and validate** the latest IMD/CWC object, source time, valid time, category and polygon.
2. **Intersect** with consented farm location, then calculate time to expected adverse weather, not merely time to cyclone-center landfall.
3. **Select approved rules** by hazard, crop, stage, asset and deadline.
4. **Rank by reversibility**: low-cost preparation at 72-120 h; costly or irreversible actions only as confidence and official warning stage rise.
5. **Render for access**: one action per sentence, local language, SMS plus spoken IVR, with "do now," deadline, reason and official source time.
6. **Confirm delivery and action**, escalating failures to OSDMA/extension/community contacts where agreements permit.
7. **Open recovery and claim workflows** after the all-clear, preserving evidence and avoiding unsafe field inspection.

## 6. REAL-vs-FILLER

| Genuinely usable now | Why it is real | Decorative or unsafe if used alone | Why it is filler |
|---|---|---|---|
| IMD cyclone track, wind and cone endpoints | Named endpoints and response structures are published. [36] | A generic "AI cyclone predictor" | It duplicates the official authority and introduces uncalibrated risk. |
| IMD staged bulletins and exact wind classes | Timings, thresholds, impacts and recipients are documented. | A color badge with no issue time, horizon or action | Color alone omits uncertainty, validity and farmer deadline. |
| Polygon-to-farm matching | Produces an auditable exposure decision | Distance to forecast center line only | Wind, rain, surge and uncertainty extend beyond the center line. |
| Consent-based crop/stage profile | Changes the appropriate action materially | District-average crop statistics presented as a farmer profile | Annual aggregates do not identify a parcel's current crop or stage. [41] |
| SMS plus IVR with delivery/playback logs | Directly serves low-literacy and non-smartphone users | A smartphone dashboard or satellite gallery | A visual app does not prove warning receipt or comprehension. |
| OSDMA EWDS partnership | Existing infrastructure reaches priority coastal communities through towers, mass messaging and emergency centers. [10] | Claiming every Odisha farm is covered by sirens | The documented footprint is 1,205 villages in 22 blocks and 6 coastal districts, not statewide universal farm coverage. |
| Time-stamped claim packet | Maps directly to PMFBY's 72-hour workflow and evidence fields | An automatic "claim approved" score | Eligibility, notified crop, insurer assessment and policy status remain external. |
| Historical-event replay | Tests timing, escalation and channel logic | Training a loss model on seven headline cyclones | Event reports have inconsistent agricultural outcome labels and missing farmer-level counterfactuals. |
| IMD damage descriptors as transparent rules | They connect class to crop/infrastructure risk and actions. | Copying the same class advice to all crops and stages | Hazard class does not encode exposure, phenology, drainage, livestock or ability to act. |
| Sensor imagery as supporting context | It helps experts verify evolution | Raw radar or satellite images sent to low-literacy farmers | Images require interpretation and do not by themselves specify a safe action. |

The most important real-vs-filler test is simple: if removing a data field would not change **who acts, what they do, or by when**, it is probably explanatory content rather than an operational input.

## 7. NOISE LOG

| Searched or encountered | Disposition | Reason |
|---|---|---|
| Wikipedia cyclone pages | Discarded as evidence | Useful for query discovery, but not needed where IMD, ISRO, OSDMA, WMO or institutional reports exist. |
| ResearchGate and Scribd copies | Discarded | Unstable mirrors, unclear version control and weaker provenance than source PDFs. |
| Commercial weather/radar pages | Discarded | They did not establish IMD asset ownership, coverage, calibration or operational status. |
| Facebook claim about planned Odisha radars | Discarded | No corroborating official MoES/IMD/PIB statement was recovered. |
| Generic IMD home and dynamic current-bulletin pages | Used only for discovery | Search results were frequently overwritten by unrelated 2026 monsoon bulletins and did not preserve the historical event being researched. |
| False Hudhud result that opened the Dana report | Discarded for Hudhud | The document explicitly concerns Dana, so it cannot support Hudhud facts. [14] |
| Supposed Amphan report that opened an Oct 2020 Monthly Weather Review | Discarded for Amphan | The retrieved document concerned October systems, not Amphan's May lifecycle. [37] |
| Empty or navigation-only OSDMA publication pages | Discovery only | They identify that material exists but do not expose the quantitative table required for a normalized event row. |
| Unverified "shallow shelf causes cyclones" phrasing | Corrected | Shallow shelf and coastal geometry primarily affect surge/inundation; warm water, moisture, rotation and shear govern genesis. [20] |
| A nominal 72-hour official warning treated as farmer lead | Discarded as an inference | Issue lead does not establish SMS delivery, IVR completion, comprehension or action by an individual farmer. |

## 8. VERDICT

### Grade: **PARTIAL**

A **free prototype can be built today**, but only if its claim is carefully bounded:

- It can ingest or poll IMD's documented cyclone track, wind and cone products, retain source timestamps, and fall back to public bulletins.
- It can combine the official four-stage warning sequence with a small, consented demonstration farm registry.
- It can execute transparent rules from IMD damage descriptors and a separately approved Odisha agronomy knowledge base.
- It can send concise SMS and synthesized or recorded Odia IVR through a prototype messaging provider.
- It can preserve bulletins, farm coordinates, profile snapshots, delivery logs and geotagged photos in a PMFBY-oriented claim packet.
- It can replay 1999, Phailin, Fani, Yaas and Dana to test timing and escalation.

That prototype is **not yet a production early-warning service**. The following must be collected directly:

1. Parcel/crop/stage/assets, farmer language/channel/consent, safe contact times and insurance profile.
2. Delivery, playback, acknowledgement, comprehension, action and non-action reasons.
3. Verified post-event loss and recovery outcomes, preferably validated by extension workers, assessors or insurers.
4. Local drainage, inundation duration, salinity and road-access observations.

The following require partners:

- **IMD/MoES** for production API onboarding, schema/version notice, latency and service expectations.
- **OSDMA and district/block authorities** for EWDS integration, escalation and shelter/route data.
- **Odisha Agriculture Department, OUAT and ICAR** for versioned crop-stage action and recovery rules.
- **CWC/Water Resources** for flood-feed integration and station interpretation.
- **Telecom/SMS/IVR providers** for DLT-compliant high-volume delivery, Odia voice, retries and delivery receipts.
- **PMFBY insurers, banks and NCIP operators** for enrollment validation, policy linkage and claim status.

The go/no-go split is therefore:

| Capability | Decision |
|---|---|
| Hackathon demonstration with public data and synthetic/consented farm profiles | **GO** |
| Pilot with real farmers in selected coastal blocks | **PARTIAL**, after Agriculture Department, OSDMA, telecom and data-governance agreements |
| Autonomous statewide warning or crop-loss prediction | **GATED** |
| Replacement for IMD forecasts, evacuation orders or insurer assessment | **NO-GO** |

The safest product statement is: **"We translate official IMD and CWC hazards into timely, profile-aware, explainable farm actions and preserve evidence; we do not generate an unofficial cyclone forecast or promise claim approval."**

## Synthesis

| Layer | Mechanism | Scope and time horizon | Evidence strength | Core trade-off |
|---|---|---|---|---|
| Cyclone science | Warm ocean, rotation, moisture, convection and low shear enable genesis | Basin and days to seasons | Strong physical evidence | Explains risk but is too broad for farm triggering |
| Detection | Satellites observe the basin; radar and surface/ocean observations refine the near-coast picture | Basin to local; minutes to hours | Strong for named assets used in Dana | Rich observations, but incomplete public uptime/provenance metadata |
| Forecast and warning | IMD fuses observations/models into track, intensity, cone, rain, wind and surge products | 12-120 h | Strong, verified annually | Longer lead enables preparation but carries greater position/time uncertainty |
| Hyperlocal decision | Farm exposure and crop stage select an approved action | Parcel; hours to days | Missing until collected | Specificity improves usefulness but raises privacy and update burden |
| Last-mile delivery | SMS, IVR, sirens, radio and human networks deliver the action | Individual/community; minutes | Channels exist, outcome telemetry does not | Broad reach does not guarantee understanding or action |
| Recovery and claims | Post-event evidence, agronomy and policy rules guide recovery and intimation | Parcel; hours to seasons | Claim rules are strong; recovery and loss data are fragmented | Fast documentation helps claims, but unsafe or premature inspection can harm farmers |

The non-obvious tension is that the strongest part of the chain is also the least differentiating: IMD already detects and forecasts the cyclone. The platform's defensible value lies after the forecast, where it converts official hazard objects into a small number of deadline-aware actions, reaches farmers through accessible channels, confirms receipt, and records outcomes.

A second tension is between lead time and confidence. The 72-120-hour window is valuable for reversible preparation, while costly harvesting, evacuation or livestock movement should depend on updated official products, local exposure and action deadlines. The engine should therefore escalate actions rather than issue one static advisory.

Finally, historical improvement does not eliminate local uncertainty. Dana's very small landfall errors and Phailin's multi-day warning demonstrate capability, while 1999 shows that warning issuance alone does not prevent catastrophe. The design priority should be **official-source fidelity -> local relevance -> accessible delivery -> confirmed action -> measured outcome**.

## References

1. *Gopalpur - Radar*. https://mausam.imd.gov.in/imd_latest/contents/index_radar.php?id=Gopalpur
2. *Paradip - Radar*. https://mausam.imd.gov.in/imd_latest/contents/index_radar.php?id=Paradip
3. *Cyclone Information | India Meteorological Department*. https://mausam.imd.gov.in/responsive/cycloneinformation.php
4. *IMD API Management*. https://api.imd.gov.in/
5. *Four Stage Warning*. https://rsmcnewdelhi.imd.gov.in/four-stage-warning.php
6. *INSAT-3DR | Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/insat-3dr
7. *IMD Mausam - India Meteorological Department*. https://mausam.imd.gov.in/index_en.php
8. *13Wmo Workshop2019*. https://severeweather.wmo.int/TCFW/13WMO_Workshop2019/03_TC_genesis_WMO2019.pdf
9. *Imd Latest*. https://mausam.imd.gov.in/imd_latest/contents/cyclone.php
10. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Early Warning Dissemination System (EWDS)*. https://www.osdma.org/preparedness/early-warning-communications/ewds
11. *CYCLONE WARNING IN INDIA*. https://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf
12. *INSAT-3D Data Products | Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/insat-3d-data-products
13. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/archive/60/60_a53fa0_fani.pdf
14. *Press Release*. https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
15. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_38a1d4_phailin.pdf
16. *Annual Veri 2024*. https://rsmcnewdelhi.imd.gov.in/uploads/Annual_Veri_2024.pdf
17. *Press Release*. https://internal.imd.gov.in/press_release/20210427_pr_1077.pdf
18. *IMD API Management*. https://api.imd.gov.in/public/index.php
19. *Press Release*. https://internal.imd.gov.in/press_release/20260101_pr_4602.pdf
20. *Cyclone Science Plan*. https://rsmcnewdelhi.imd.gov.in/images/pdf/cyclone_science_plan.pdf
21. *26 77Afd4 Preliminary Report Yaas During 23 27 May 2021*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_77afd4_Preliminary%20Report%20YAAS%20during%2023-27%20May%202021.pdf
22. *Characteristic features of Orissa super cyclone of 29th October, 1999 as observed through CDR Paradip*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/450/449
23. *Orissa super cyclone – A Synopsis*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/449/450/1763
24. *Press Release*. https://internal.imd.gov.in/press_release/20210611_pr_1133.pdf
25. *Bulletins & Products*. https://rsmcnewdelhi.imd.gov.in/bulletins-products.php
26. *RSMC*. https://rsmcnewdelhi.imd.gov.in/
27. *Track Forecast*. https://rsmcnewdelhi.imd.gov.in/track-forecast.php
28. *Data Access Policy | Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/data-access-policy
29. *Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/
30. *Welcome to MOSDAC*. https://www.mosdac.gov.in/signup/
31. *Frequently Asked Questions | Meteorological & Oceanographic Satellite Data Archival Centre*. https://www.mosdac.gov.in/faq-page
32. [
  
    INSAT-3DS begins imaging the Earth
  
  ](https://www.isro.gov.in/INSAT-3DS_imaging_Earth.html)
33. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://pmfby.gov.in/guidelines
34. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://www.pmfby.gov.in/
35. *Home | Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/en
36. *Api Reference*. https://api.imd.gov.in/public/api_reference.html
37. *Press Release*. https://internal.imd.gov.in/press_release/20201105_pr_926.pdf
38. *Revised Operational Guidelines*. https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf
39. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | CYCLONE AMPHAN UPDATE*. https://www.osdma.org/cyclone-amphan-update
40. *'Meghdoot' – Mobile app for weather based agro advisories PIB https://www.pib.gov.in › PressReleaseIframePage*. https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1739245
41. *Statistics - Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/en/page/statistics
42. *Flood Forecasting/ Hydrological Observation | Central Water ...*. https://cwc.gov.in/flood-forecasting-hydrological-observation
43. *mKisan:IVRS*. https://mkisan.gov.in/Alpha/aboutivrs.aspx
44. *IMD releases a report on Super Cyclonic Storm "Amphan ... PIB https://www.pib.gov.in › Pressreleaseshare*. https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1631493
45. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
46. *Hudhud: Another Damaging Bay of Bengal Storm*. https://science.nasa.gov/earth/earth-observatory/hudhud-another-damaging-bay-of-bengal-storm-84547
