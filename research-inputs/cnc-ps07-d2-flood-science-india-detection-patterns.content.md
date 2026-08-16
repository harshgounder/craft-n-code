# Odisha Flood Data for a Farm Advisory Engine

## 1. EXECUTIVE SUMMARY

- **Operational warning backbone exists**: CWC monitors levels and discharges, issues forecasts to civil authorities, and operates a national network of 325 forecast stations. Its official Odisha count is **19 forecast stations: 12 level and 7 inflow sites**, spread across the Subarnarekha, Mahanadi, Brahmani, Baitarani, Mahanadi-to-Pennar, and Godavari systems [3][13]. This is enough to build a basin-level trigger layer, but not a field-level flood prediction layer. **[1] [2]**
- **The alert semantics are usable now**: CWC defines Normal, Above Normal/yellow, Severe/orange, and Extreme/red from warning level, danger level, and highest flood level. Orange bulletins are issued every three hours and red bulletins hourly [3]. Encode those official states directly rather than inventing a hackathon risk score. **[1]**
- **Machine-readable observations are real, but operational terms are incomplete**: the National Water Data Portal publishes CWC hourly water-level and discharge resources as downloadable CSV and labels them CSV/API. Odisha series include historical and 2026 data, with August 2026 updates [18][19]. The public metadata does not document a production endpoint, license, service-level agreement, or ingestion lag. **[3]**
- **IMD and Odisha DoWR provide the rainfall side, but mostly as products rather than a clean contract**: IMD Bhubaneswar exposes district warnings, agromet products, coastal and port warnings, radar, satellite, cyclone, and NWP links; Odisha flood bulletins include a river-sub-basin quantitative precipitation forecast, or QPF [29][16]. A prototype can parse or manually encode these, but unattended production use needs a documented feed or agency agreement. **[4] [5]**
- **The flood chain is compound, not single-hazard**: Odisha records show upstream rain and reservoir inflow raising rivers, cyclone rain and surge inundating the coast, and high tide or a turbulent sea delaying delta drainage. In 2021, Yaas combined surge with flooding in the Subarnarekha, Baitarani, and Budhabalanga systems; in 2020, the sea slowed discharge and kept delta areas submerged for three days [22]. The engine must join rain, river, reservoir, tide/surge, and drainage conditions. **[7]**
- **Historical maps are planning priors, not live farm warnings**: the NRSC/NDMA atlas aggregates satellite-observed flood-affected area for **1998-2022** at national, state, and district scales. Odisha totals 1,424,313 ha across 23 districts, led by Baleshwar, Bhadrak, Kendrapara, Puri, Jajpur, Cuttack, and Jagatsinghpur by cumulative affected area [10]. It does not supply village/plot return periods, depth, duration, or crop damage. **[6]**
- **Warnings already reach people through several public channels**: CWC uses phone, SMS, email, media, social media, and web channels; OSDMA's coastal EWDS uses sirens and voice from 122 alert towers; SACHET supplies area-specific alerts through SMS, app, browser, and CAP RSS [3][4][2]. The unresolved gap is not only message transport but measured time from forecast creation to farmer receipt, comprehension, and action. **[1] [8] [9]**
- **Agricultural rules exist, but personalization does not**: Odisha publishes a 2025 crop contingency plan, and an ICAR case from waterlogged Kanas, Puri reports fields inundated for 6-15 days and improved rice results from older seedlings [7][8]. No public source links those rules to a live farmer registry containing plot boundary, crop, sowing date, variety, livestock, phone, literacy/language preference, or observed loss. **[10] [11]**
- **Decision**: a free prototype is feasible for alert ingestion, basin/district risk, rules-based SMS/IVR, and farmer-reported recovery workflows. It is **PARTIAL**, not production-ready, because site-specific forecast horizons, stable APIs, plot exposure, live embankment/drainage condition, delivery telemetry, and claim-grade ground truth require collection or partners. **[1] [3] [4] [8] [9]**

## 2. DATA INVENTORY

### Flood processes, formation, and observed duration

| Flood type | How it forms in Odisha evidence | Duration supported by the record | Engine interpretation |
|---|---|---|---|
| Riverine: Mahanadi, Brahmani, Baitarani, Subarnarekha | Basin and upstream rainfall increases river inflow; Hirakud operation can alter the Mahanadi hydrograph. The 2011 flood involved all four named systems, while 2021 records increased Chhattisgarh inflow and 28 open Hirakud gates. | In 2011, Mahanadi and distributaries remained above danger for four days and part of the delta remained inundated for more than a fortnight. In 2020, documented river episodes lasted roughly two to six days. | Treat rise time, threshold crossing, reservoir inflow/release, and recession separately. Do not use one fixed flood duration. |
| Flash: interior and urban | Intense local rainfall produces rapid runoff in steep or poorly drained catchments. Heavy rain over the prior two days triggered Nagabali, Kalyani, Hati, and Tel flooding in Rayagada and Kalahandi by 16-17 July 2017 [6]. | The source demonstrates onset within about two days, but does not establish a universal duration. Urban drainage data were not found. | Nowcast and rain-intensity triggers matter more than a slow main-stem gauge alone. Require local rain, road, culvert, and low-point reports. |
| Coastal: cyclone surge and seawater ingress | Cyclonic wind and pressure drive surge around landfall; rain, surge, and elevated rivers can coincide. For Yaas, IMD forecast 2-4 m above astronomical tide for Balasore/Bhadrak and about 2 m for Kendrapara/Jagatsinghpur [17]. | Peak surge is landfall-linked; standing saline water lasts according to drainage and breach conditions. No authoritative Odisha-wide fixed duration was found. | Combine cyclone track, surge/tide, distance/elevation from coast, salinity report, and river stage. A rainfall-only warning is insufficient. |
| Delta waterlogging | Low relief, saturated fields, high river stage, tide, blocked drainage, or saline embankment failure slows outflow. In 2020, full-moon/turbulent-sea conditions slowed discharge and submerged delta areas for three days [22]. | ICAR reports 6-15 days of field inundation in Kanas, Puri [8]. | Ask for water depth, days submerged, salinity, crop stage, and drainage outlet status before recommending re-sowing or input application. |

**Takeaway:** duration is event- and location-specific. The engine should forecast and then update a recession clock from observed water level and farmer reports, rather than assign a static label such as "river flood = seven days."

### Named data sources and access

Reliability grades used here are: **A** = official operational or primary observed data; **B** = official periodic report or validated historical layer; **C** = useful derived/modelled or incompletely documented product; **D** = absent, unverified, or unsuitable for the claimed decision.

| Data item | Named source with URL + date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---|---|---|---|
| CWC forecast states, thresholds, cadence, dissemination | CWC, "Flood Forecasting/Hydrological Observation," https://cwc.gov.in/; updated **2026-08-14** [3] | Forecast site and river; national operating rules | Seasonal/live service; page current to Aug 2026 | Free web portal/report; no documented public production API on cited page | **A** for published status; **C** for automation contract |
| Odisha forecast-network coverage | Rajya Sabha Unstarred Question 891, CWC/Ministry of Jal Shakti, https://cwc.gov.in/; public answer, accessed **2026-08-16** | 19 sites summarized as 12 level + 7 inflow across six river systems [13] | Static network statement | Free parliamentary answer | **A** for counts and basins; **D** for missing site roster |
| Current forecast display and seven-day advisory | CWC Flood Forecasting System, https://ffs.india-water.gov.in/; accessed **2026-08-16** | Station hydrograph/table and advisory | Current portal | Free web/app [1] | **A** as official display; **C** for unattended ingestion |
| Hourly river water level | National Water Data Portal, CWC Hourly Water Level, https://nwdp.nwic.in/; updated **2026-08-09** [18] | Date, station identifier, geographic hierarchy, level; river-group CSVs include Odisha basins | Historical through 2025 plus a 2026-2030 resource currently populated | Free CSV; catalog labels CSV/API | **A** observation; **C** metadata/API completeness |
| Hourly discharge | National Water Data Portal, CWC Discharge, https://nwdp.nwic.in/; updated **2026-08-02** [19] | Station/hour; automated and manual observations | Historical and 2026 resource | Free CSV; catalog labels CSV/API | **A** observation; **C** metadata completeness |
| District rain warnings, nowcast, radar, satellite, cyclone/NWP and agromet products | IMD Meteorological Centre Bhubaneswar, https://mausam.imd.gov.in/bhubaneswar/; accessed **2026-08-16** | Odisha district/product; coastal and port products also listed | Operational web products | Free web/PDF; CAP RSS and data-service links exist [29][28] | **A** official forecast; **C** machine-interface documentation |
| River-sub-basin QPF and Odisha situation bulletin | Department of Water Resources, "Flood Bulletin," https://dowr.odisha.gov.in/; example dated **2025-08-29** [16] | River sub-basin, gauge situation, daily warning context | Bulletin/event based | Free PDF/report; no API documented | **A** official bulletin; **C** parser stability |
| Flood warning color system | CWC Flood Forecasting page, https://cwc.gov.in/; updated **2026-08-14** | Site state relative to warning, danger, and HFL | Operational | Free page/bulletin | **A** [3] |
| Historical affected footprint and district pattern | NRSC/NDMA, "Flood Affected Area Atlas of India, 1998-2022," https://ndem.nrsc.gov.in/; **March 2023, Version 1** [10] | National, state, district; satellite-derived cumulative footprint | Periodic retrospective layer | Free PDF; digital maps reported on NDEM [10] | **B** for planning prior; **D** for plot/live warning |
| Major Odisha event histories | Special Relief Commissioner annual reports, https://srcodisha.nic.in/; **2011-12, 2019, 2021, 2024** | Event, district/block/village totals, rivers, casualties, crop and infrastructure damage | Annual retrospective | Free reports/PDF | **B**, primary administrative record |
| Embankment breach consequences | SRC reports: 2011 breach counts, 2019 damage length, 2020 breach counts; https://srcodisha.nic.in/ [9] | Event totals, sometimes river/canal/saline class | Retrospective, not asset-live | Free report | **B** for event damage; **D** for present condition |
| Coastal mass warning | OSDMA Early Warning Dissemination System, https://www.osdma.org/; implementation began **2015-2016** [4] | 1,205 villages, 22 blocks, six coastal districts; 122 towers within 1.5 km of coast [4] | 24x7 infrastructure [4] | Government siren/voice network | **A** for covered geography; **D** outside footprint without other channels |
| Multi-hazard public alert relay | NDMA SACHET, https://sachet.ndma.gov.in/; Version 3.1 updated **2026-07-31** [2] | Geo-targeted/area-specific | Near-real-time [2] | Free SMS, app, browser, CAP RSS [2] | **A** official relay; **C** for receipt/action verification |
| Crop contingency rules | Odisha Department of Agriculture, "Odisha Crop Contingency Plan 2025," https://agri.odisha.gov.in/; **2025** [7] | Crop, season, hazard response guidance | Annual/static | Free file/report | **B** for rule library; **D** without plot/crop state |
| Waterlogging recovery evidence | ICAR case, Kanas block, Puri; https://icar.gov.in/; field results for **2018-2019** [8] | Demonstration farms/local practice | Historical case study | Free article/report | **B** locally relevant evidence; not a universal prescription |
| Plot profile, live crop state, loss evidence, literacy/language and consent | No complete linked public source found | Farmer/plot/season/message | Must be current | Consent-based registration, IVR/SMS interaction, field collection, insurer/department partner | **D** until collected |

### Historical flood and cyclone-rain pattern

| Year | Documented pattern | Scale or outcome relevant to the engine | What it proves - and does not prove |
|---|---|---|---|
| **2011** | Four flood phases affected 21 districts; September involved Mahanadi, Brahmani, Baitarani, Budhabalanga, and Subarnarekha. | September affected 122 blocks, 6,473 villages and about 6.0M people; more than 50% crop loss covered 260,256 ha. Hundreds of river and canal breaches were recorded in each of two phases [9]. | Strong multi-basin riverine and breach case; it does not yield a station-specific return period. |
| **2013** | Cyclone Phailin brought very heavy to extremely heavy rain, flooding, strong winds, and storm-surge coastal inundation [21]. | Compound cyclone-rain-surge case. | Confirms multi-hazard logic; event report is not a live data feed. |
| **2017** | Heavy rain in Rayagada and Kalahandi produced rapid Nagabali, Kalyani, Hati, and Tel flooding [6]. | More than 28,000 people and 50 villages in Rayagada Block were reported affected [6]. | Interior flash-flood case; not evidence of statewide river flooding. |
| **2019** | Flood/heavy-rain episodes ran from 27 July to 16 August across 21 districts; Fani was a separate major May cyclone. | 45,424.635 ha of cultivation was affected in the flood/heavy-rain episodes; 306.41 km of river/saline embankments and 43.17 km of breaches were reported damaged. | Shows one calendar year can contain different hazard regimes; do not merge cyclone and flood losses. |
| **2021** | Mahanadi flooding followed increased Chhattisgarh inflow and Hirakud releases; Yaas paired surge with multiple river floods; Jawad caused major waterlogging. | September flood/heavy rain affected 23 districts and 146,419.28 ha of crops; Jawad loss of at least 33% covered 394,916.22 ha [23]. | Best single-year evidence for separate river, coastal-compound, and waterlogging workflows. |
| **2024** | A September deep depression caused Malkangiri/Koraput flash flooding; later Subarnarekha, Budhabalanga, and Jalaka rose in Balasore/Mayurbhanj; Dana crossed north Odisha in October. | In the coastal river episode, full-moon conditions slowed sea discharge and Subarnarekha/Jalaka exceeded danger [24]. Dana affected 14 districts and 172,356.81 ha of crops [24]. | Confirms that an annual label hides several distinct events; the engine needs event IDs and time windows. |

The atlas rankings describe **cumulative affected footprint**, not the number of floods. Baleshwar (229,691 ha), Bhadrak (203,525 ha), Kendrapara (189,195 ha), Puri (168,662 ha), Jajpur (143,973 ha), Cuttack (120,270 ha), and Jagatsinghpur (118,994 ha) exceed 100,000 ha in the 1998-2022 atlas. A defensible district planning priority can use that footprint; a claim that these are the "most frequent" districts requires an event-count series that the atlas does not provide.

No authoritative statistical return-period table for Odisha villages/blocks was found in the reviewed public sources. The NRSC atlas is an observed cumulative footprint, and its authors warn that mapping depends on satellite availability and overpass timing and may miss short-duration flash floods.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing fields | Coverage judgment A-D |
|---|---|---|---|
| CWC forecast pages and FFS | Official stage semantics, cadence, hydrographs, current forecasts, seven-day advisory label, dissemination channels [3][1] | No cited public table joining all 19 Odisha forecast-site names, coordinates, warning/danger/HFL values, forecast issue time, target time, lead hours, model skill, and revision history | **B** overall: A for human operational use, C-D for a stable engine contract |
| National Water Data Portal | Hourly water level/discharge; direct CSV resources; basin and station identifiers; historical plus current-period resources [18][19] | Catalog says API but does not expose a complete public production contract in the reviewed metadata; sampled Odisha discharge material exposed sparse river/basin metadata | **B** |
| IMD Bhubaneswar | District warnings, nowcast, radar/satellite, cyclone/NWP, coastal/port, agromet, CAP and data-service paths [29][28] | Product pages do not, in the extracted text, define one stable schema joining QPF horizon, polygon, probability, issue/valid time, and revision | **B** |
| Odisha DoWR flood bulletins | River-sub-basin QPF, river situation and official event bulletin [16][15] | PDF/report access; layout and file naming can change; no documented API or delivery SLA | **B** |
| NRSC/NDMA atlas and NDEM | Official satellite-derived 1998-2022 footprint, district statistics, downloadable map context [10] | No village/block probability, return period, depth, duration, salinity, crop, or live extent; short events can be missed | **B** for planning; **D** for live/plot decisions |
| SRC annual reports | Rich event narratives, district/block/village totals, crop loss, evacuations, breaches and infrastructure damage | Annual PDF, changing definitions/layout, aggregated damage, no event API or consistent geocoded parcel records | **B** |
| OSDMA EWDS | Concrete coastal footprint, siren/voice towers, 24x7 state-district-block architecture [4] | Primarily coastal cyclone/tsunami footprint; no public per-farmer delivery, comprehension, or action log | **B** |
| NDMA SACHET | Official near-real-time, geo-targeted multi-hazard relay over SMS/app/browser/CAP RSS [2] | Alert transport is not a flood model; no evidence that every farmer receives, understands, or acts on a message | **B** |
| Odisha agriculture and ICAR | Official contingency rule source and locally observed waterlogging recovery case [7][8] | Advice is not automatically linked to crop stage, variety, salinity, available inputs, farmer capacity, or forecast confidence | **B** |
| Farmer, insurer and field layer | None as one public, current, consented, interoperable dataset | Nearly all personalization, claim and outcome variables are absent | **D** |

**Coverage judgment:** India and Odisha have credible hazard observations, public warnings, historical reports, and advisory source material. Coverage collapses at the final mile: stable machine interfaces, plot exposure, infrastructure condition, verified receipt, and measured outcome.

## 4. WHAT IS MISSING

The following are exact data gaps, not requests for another generic flood report:

1. **Named current roster of all 19 CWC Odisha forecast stations**, with station ID, river, latitude/longitude, district/block, forecast type, warning level, danger level, HFL, upstream dependencies, and active/inactive status. The official answer supplies counts and basins, not the full roster [13]. A downloaded telemetry station must not be silently treated as one of the 19 forecast stations.
2. **Site-specific forecast lead-time and skill table**: issue time, target time, effective lead hours, model/version, observed error, hit/false-alarm rate, and revision. CWC states that national forecast accuracy is above 90%, but that aggregate figure is not Odisha-site skill [3].
3. **Documented production APIs** for CWC forecasts/NWDP observations and IMD district/QPF products, including endpoint, authentication, license, rate limit, versioning, latency, uptime, retry policy, archive and deprecation notice.
4. **Village/block/plot flood probability and return-period layers** for riverine, flash, surge and waterlogging hazards. The national atlas stops at district statistics and cumulative footprint.
5. **Flood depth-duration-velocity-salinity surfaces** tied to crop stage. Binary "affected/not affected" cannot distinguish a short freshwater inundation from 10 days of saline standing water.
6. **Live embankment asset registry and condition feed**: GIS alignment, owner, crest/elevation, material, last inspection, weak point, seepage, repair, breach probability, current breach, and closure time. Historical damage proves importance, not present condition [9].
7. **Drainage and control-structure state**: outfall, sluice/tidal gate, canal, culvert, pump, blockage, siltation, operating schedule, local water level and capacity.
8. **Reservoir-release decision feed with advance notice**, linking planned/actual gate openings, release hydrograph, downstream travel time, and forecast revision.
9. **Current consented farm profile**: parcel boundary or village, farmer contact, preferred Odia/voice format, crop/variety, sowing/transplanting date, crop stage, irrigation/drainage, livestock, stored inputs/produce, machinery and safe shelter.
10. **Claim-grade event packet standard**: event and alert IDs, time/location proof, before/after geotagged media, water depth/duration/salinity, crop/area/stage, land and insurance references, assessor status, rule version, submission receipt and payout.
11. **End-to-end warning performance**: forecast-created time, message-generated time, gateway acceptance, handset delivery, IVR answered/listened, comprehension, intended action, completed action and reason for non-action. OSDMA's "minutes" objective concerns dissemination reach, not hazard forecast lead [4].
12. **Action-outcome training data** linking a specific advisory to avoided loss, recovery cost, yield, false-alarm burden and farmer feedback. Without it, "AI-generated" advice cannot be claimed to be optimized.
13. **Urban flash-flood low-point and drain sensor data** for Odisha towns, plus road/passability and safe-route status.

These gaps cannot be responsibly filled with interpolation from district averages. They require farmer consent, field instrumentation, local-government/DoWR/CWC/IMD data agreements, insurer coordination, or a clearly labeled model estimate.

## 5. HOW IT FEEDS THE ENGINE

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD district warning, QPF, radar/nowcast and cyclone/surge product | Set watch window; prioritize harvesting, input relocation, livestock movement, drainage clearing and communication timing | Identify likely rain continuation before draining, re-entering, spraying or re-sowing | Attach official issue/valid time and event ID | Compare crop calendar with recurring cyclone/monsoon windows | Capture safe rainfall for pond recharge or planned irrigation only when flood risk is low |
| CWC forecast state and forecast hydrograph | Trigger tiered SMS/IVR: yellow = prepare, orange = act, red = evacuate/protect life; preserve the official meaning [3] | Estimate recession and safe field access; continue alerts while levels remain elevated | Attach station, threshold state, issue time and hydrograph | Avoid highly exposed crop windows or raise/store assets | Use declining but adequate water levels for controlled recharge only under local approval |
| NWDP hourly level/discharge | Detect rising trend and threshold approach; calculate rate of rise with quality checks | Estimate peak/recession; request field observations where gauges diverge from local reports | Create immutable observation snapshot and source timestamp | Derive seasonal timing and duration features after validation | Support irrigation planning in non-flood periods; never equate river flow with field water availability automatically |
| Reservoir inflow/release | Warn downstream farmers based on planned/actual release and travel time | Explain secondary rise after rainfall ends | Record official release timeline | Align vulnerable operations with release history | Coordinate water availability when releases are beneficial and safe |
| Tide/surge/coastal proximity | Move livestock, seed, equipment and drinking water above expected ingress; close saline pathways where locally advised | Test salinity and delay unsuitable replanting; separate freshwater waterlogging from seawater ingress | Record surge/tide window and salinity evidence | Favor tolerant varieties or raised storage in recurrent ingress zones | Plan saline-water exclusion, pond protection and freshwater flushing with extension support |
| NRSC district footprint and SRC event history | Rank onboarding, sensor placement and rehearsal areas; not an evacuation trigger | Anticipate logistics demand and likely isolated areas | Context only; not proof that a specific parcel flooded | Compare crop and infrastructure choices across repeatedly affected districts | Target community drainage, raised seed banks and resilient demonstration plots |
| Embankment/breach and drainage status | Escalate downstream/local warnings; route around breach or blocked outfall | Prioritize dewatering, access and repair reporting | Geotag breach/blockage and responsible asset | Rank repair and community maintenance | Clear drains before forecast rain and maintain safe water-control assets |
| Farm profile and crop stage | Select feasible, crop-specific actions and channel/language; suppress irrelevant advice | Decide drain, salvage, seedling, re-sowing, livestock and input actions | Establish crop, area, stage, ownership/insurance references | Adjust planting date, crop mix, storage and asset location | Send ordinary agronomy, water-saving and market-readiness advice so the service has value outside disasters |
| Farmer/field observations | Confirm local rain, depth, road and water ingress through keypad/voice prompts | Track depth, days submerged, salinity, pest/disease signs and input needs | Supply timestamped, geotagged or village-verified evidence | Create local depth-duration and outcome history | Reward reporting with useful local summaries and follow-up advice |
| Delivery and IVR telemetry | Retry undelivered alerts; switch SMS to voice; escalate through community volunteers | Maintain two-way welfare and needs check | Prove that alert/advice was sent and acknowledged, while respecting consent | Improve language, timing and message length | Learn preferred format and reduce alert fatigue |
| Crop contingency and validated local trials | Convert hazard state into approved action templates rather than free-form model text | Select recovery options only after crop stage, depth, duration and salinity checks | Record the rule and version used | Compare alternatives and costs | Promote resilient seedlings, raised storage and drainage practices supported by local extension |

The advisory generator should be a **rules-and-evidence system with retrieval**, not an unconstrained text generator. Hazard feeds set urgency; the farm profile determines relevance; approved agriculture rules determine the action; delivery telemetry and farmer response close the loop. A language model may simplify an approved instruction for Odia SMS/IVR, but should not invent agronomic treatments, thresholds, claim rules, or evacuation advice.

A practical event object should preserve `event_id`, source, issue time, valid-from/to, location geometry, river/station, observed and forecast values, CWC color/state, IMD warning, confidence, source URL, data version and ingestion time. A farm decision object should separately preserve plot/village, crop stage, exposure, selected approved rule, message language/channel, send/receipt result, response and follow-up. That separation prevents a late observation from silently rewriting what the farmer was originally told.

## 6. REAL-vs-FILLER

| Classification | Evidence-based assessment | Why it matters |
|---|---|---|
| **REAL: CWC threshold states and cadence** | Official warning/danger/HFL relationships and yellow/orange/red states are explicitly defined; orange is three-hourly and red hourly [3]. | Directly usable as trigger semantics and audit fields. |
| **REAL: hourly level and discharge files** | NWDP identifies hourly CWC observations, fields, current-period resources and downloadable CSV/API formats [18][19]. | Usable for a demo adapter and historical feature construction, with schema/latency checks. |
| **REAL: IMD/DoWR official product set** | District, nowcast, cyclone, coastal, radar and NWP paths exist; DoWR bulletins contain river-sub-basin QPF [29][16]. | A human-assisted prototype can consume them today; production parsing remains brittle. |
| **REAL: official dissemination rails** | CWC, OSDMA EWDS and SACHET provide complementary web, SMS, voice/siren and CAP-style channels [3][4][2]. | Build on official alerts; do not impersonate the authority. Use a separate agriculture-advice identity and provenance. |
| **REAL: historical planning prior** | NRSC supplies a long-period satellite footprint and district statistics, with explicit remote-sensing limitations [10]. | Useful for prioritization and scenario testing, not parcel claims or live warnings. |
| **REAL: locally relevant recovery evidence** | Kanas fields remain inundated 6-15 days; older seedlings improved rice yield in the cited demonstrations [8]. | Supports a candidate rule for extension validation, not automatic statewide prescription. |
| **CONDITIONAL: "seven-day flood forecast"** | The official portal labels a seven-day advisory [1]. | The label alone does not establish accurate seven-day parcel lead time. Show issue/target times and confidence for each site. |
| **CONDITIONAL: national forecast accuracy above 90%** | CWC reports overall accuracy above 90% [3]. | Do not present it as accuracy for every Odisha site, flood type, lead time, or farm. |
| **FILLER: static atlas as a live village alert** | Atlas output is national/state/district cumulative area, and short events can be missed. | A colorful map without current depth, time and plot exposure cannot drive immediate action. |
| **FILLER: generic weather API as IMD integration** | The required evidence is official IMD/CWC hazard information, not a city-temperature icon. | Generic forecasts may enrich context but cannot replace official flood/cyclone warning provenance. |
| **FILLER: "AI" without farm state and approved rules** | Public sources do not supply a linked plot/crop/consent/outcome dataset. | Natural-language generation does not create missing exposure or agronomic truth. |
| **GATED: automated claims** | Historical reports aggregate loss; no public linked parcel-insurance-assessment-payout dataset was found. | The prototype can assemble a packet, but only the insurer/government process can validate and adjudicate it. |

The dividing line is simple: a source is genuinely usable when it has an authoritative owner, time and location, interpretable fields, accessible artifact, and a decision that those fields can support. A report title, dashboard screenshot, map color, or broad accuracy claim without these elements is context, not an engine input.

## 7. NOISE LOG

| Search path or candidate | Disposition | Reason discarded or downgraded |
|---|---|---|
| Generic weather and city forecast pages | Discarded | No official flood threshold, river station, QPF provenance, or Odisha farm decision support. |
| UK Environment Agency flood API | Discarded | Good API pattern, wrong jurisdiction and no Odisha coverage. |
| Wikipedia and generic cyclone/storm-surge explainers | Discarded | Secondary summaries were unnecessary once IMD, CWC, SRC and NRSC primary sources were located. |
| Facebook, YouTube and unsourced social posts | Discarded | Useful for discovery at most; no stable authoritative fields or archive. |
| Current news about 2025-2026 floods returned by searches for 2019 | Discarded | Wrong event year; annual SRC report used instead. |
| NDMA/NRSC state-atlas pages for Andhra Pradesh, Bihar, Uttar Pradesh or West Bengal | Discarded for Odisha granularity | They prove the program exists elsewhere, not that an equivalent Odisha village/block atlas exists. The national atlas was retained. |
| CWC appraisal/report cover pages without extractable Odisha station table | Downgraded | Could not substantiate the requested named 19-site roster; count-and-basin parliamentary answer retained. |
| Search snippets/blogs explaining flood colors | Discarded | Official CWC color definitions were available [3]. |
| Private or exploratory India flood models | Downgraded to research context | Modelled recurrence can be useful, but it is not a substitute for an official operational alert or an observed parcel loss. |
| Odisha DoWR pages with unrelated or mislabelled CMS content | Discarded | No flood data fields; retained only dated official flood bulletins. |
| FFS page inspection for a hidden public API | Negative/inconclusive | A human portal and app are visible, but the reviewed public material did not document a stable production endpoint, terms, or SLA. |
| Sample Odisha discharge download | Retained with warning | It exposed a station identifier such as Champua_1/Kendujhar, but sparse basin/river fields mean it cannot stand in for the 19-site forecast roster [26]. |

This log prevents three common errors: citing the wrong year because a search engine prefers recent news, mistaking any water-data station for an official forecast station, and claiming village precision from a district-scale map.

## 8. VERDICT

### Grade: **PARTIAL**

A **free prototype can be built today**. It can ingest or periodically snapshot NWDP hourly CSV observations; read CWC station status and preserve official yellow/orange/red semantics; consume IMD/DoWR warning products and SACHET CAP/RSS where available; use NRSC/SRC history as district priors; register farmers with consent; retrieve approved crop-contingency rules; and deliver short Odia SMS plus IVR prompts. The demo should expose source, issue time, valid time, station/district, confidence, rule version and last successful update instead of hiding uncertainty behind one risk score.

The prototype should include four bounded workflows:

1. **Pre-disaster**: official alert -> basin/district exposure -> farm profile -> approved action -> SMS/IVR -> acknowledgment/escalation.
2. **Post-disaster**: farmer reports depth, duration, salinity and crop stage -> rule-based recovery triage -> extension referral for high-risk cases.
3. **Claim packet**: freeze official alert/observation plus consented time/location/media and crop facts -> export a packet; do not claim automatic eligibility or payout.
4. **Next season**: combine validated event history, plot outcomes and farmer constraints -> recommend planning alternatives, clearly separated from emergency alerts.

**What must be collected:** consented farmer and plot profiles, seasonal crop state, language/channel preference, field depth-duration-salinity observations, delivery/comprehension/action telemetry, geotagged loss evidence, drainage/embankment observations, and advisory outcomes.

**What needs a partner:** CWC/IMD/DoWR for stable feeds, station metadata and lead/skill definitions; Water Resources/local bodies for reservoir, embankment, sluice and drainage state; OSDMA/telecom or an authorized gateway for resilient SMS/IVR and delivery reports; Agriculture/KVK/OUAT for rule approval and escalation; insurers/government for claim schema and adjudication.

The decisive limitation is not the absence of any flood data. It is the absence of a public, stable, joined chain from **official forecast -> local exposure -> current farm state -> approved action -> verified delivery -> observed outcome**. Until those joins are collected or contracted, the honest claim is: **basin/district early-warning and rules-based advisory prototype, with farmer-confirmed local conditions**. It is not yet a plot-level predictive flood model, guaranteed lead-time service, or automated insurance system.

## References

1. *Flood Forecast - Central Water Commision, Govt. Of India*. https://ffs.india-water.gov.in/
2. *SACHET - National Disaster Alert Portal*. https://sachet.ndma.gov.in/
3. *Flood Forecasting/ Hydrological Observation | Central Water Commission, Ministry of jal shakti, Department of Water Resources, River Development and Ganga Rejuvenation, GoI*. https://cwc.gov.in/flood-forecasting-hydrological-observation
4. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Early Warning Dissemination System (EWDS)*. https://www.osdma.org/preparedness/early-warning-communications/ewds/
5. *FLOOD FORECASTING AND WARNING NETWORK ...*. https://www.cwc.gov.in/sites/default/files/ffwnappraisal-report-2023.pdf
6. *Status of Flash Flood situation in Odisha Date: 17.07.2017 Due to heavy rainfall during last two days in Rayagada and*. https://www.srcodisha.nic.in/calamity/SITREP_17.07.2017.pdf
7. *Crop Contigency Plan 2025*. https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
8. *Agricultural Resilience in Flood-prone Areas through Post-flood Crop Management and IBFI | ICAR*. https://icar.org.in/en/node/5304
9. *Microsoft Word - Annual_Report_2011-12 on NC forwarded to GoI.doc*. https://www.srcodisha.nic.in/annualReport/JNHFfzpKANNUAL_REPORT2011-12.pdf
10. *Flood Affected Area Atlas Of India Satellite Based Study*. https://ndem.nrsc.gov.in/documents/downloads/Flood%20Affected%20Area%20%20Atlas%20of%20India%20-Satellite%20based%20study.pdf
11. *Crop Contingency Plan 2024 Final*. https://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf
12. *Flood - Odisha State Disaster Management Authority*. https://www.osdma.org/preparedness/one-stop-risk-management-system/flood/
13. *RAJYA SABHA UNSTARRED QUESTION NO. 891 FLOOD FORECASTING ...*. https://sansad.in/getFile/annex/262/AU891.pdf?source=pqars
14. *Flood Control & Drainage - Odisha*. https://dowr.odisha.gov.in/sites/default/files/2021-11/Flood%20Control%20_%20Drainage.pdf
15. *Flood Bulletin,2024 Department of Water Resources - Odisha*. https://dowr.odisha.gov.in/sites/default/files/2024-08/DoWR%20Flood%20Bulletin_11.08.2024..pdf
16. *Flood Bulletin,2025 Department of Water Resources*. https://dowr.odisha.gov.in/sites/default/files/2025-08/DoWR%20Flood%20Bulletin_29.08.2025_0.pdf
17. *VERY SEVERE CYCLONIC STORM YAAS’ BULLETIN NO. - osdma.org*. https://osdma.org/wp-content/uploads/2021/05/HourlyBulletin-02.pdf
18. *River Water Level (Telemetry - Hourly), Central Water Commission (CWC) - Dataset - National Water Data Portal*. https://nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc
19. *River Discharge (Telemetry - Hourly), Central Water Commission (CWC) - Dataset - National Water Data Portal*. https://nwdp.nwic.gov.in/dataset/river-discharge-telemetry-hourly-central-water-commission-cwc
20. *Severe Cyclonic Storm “DANA” over the Bay of Bengal (22nd ...*. https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
21. *PHAILIN Report(Final) 30 - IMD*. https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads/report/26/26_38a1d4_phailin.pdf
22. *ANNUAL REPORT ON NATURAL CALAMITIES 2020-21*. https://srcodisha.nic.in/annualReport/DZF3NXfMAnnual%20Report%20on%20NC%202020-21%20-REVISED%20(1).pdf
23. *ANNUAL REPORT ON NATURAL CALAMITIES 2021-22*. https://srcodisha.nic.in/annualReport/4vP2yUSqANNUAL%20REPORT%20ON%20NATURAL%20CALAMITIES,2021-22.pdf
24. *Microsoft Word - 6058A*. https://srcodisha.nic.in/annualReport/mkH6nV8yAnnual%20Report%202024-25.pdf
25. *Jhlgu3Hoannual Report On Nc 2019 20 Compressed*. https://srcodisha.nic.in/annualReport/JHLGu3hOAnnual%20Report%20on%20NC%202019-20_compressed.pdf
26. *River Discharge Tele Hr Cwc Od 2026 2030*. https://nwdp.nwic.gov.in/dataset/aee818d7-2cb6-4790-aa3c-126a72621170/resource/6e95b06d-3369-4ec1-a97f-5ece8cfc8e8b/download/river_discharge_tele_hr_cwc_od_2026_2030.csv
27. *River Discharge Tele Hr Cwc Od 1970 2025*. https://nwdp.nwic.gov.in/dataset/aee818d7-2cb6-4790-aa3c-126a72621170/resource/b3dbc4d2-08c8-429d-920a-4171305e2426/download/river_discharge_tele_hr_cwc_od_1970_2025.csv
28. *DW Warnings | India Meteorological Department*. https://mausam.imd.gov.in/responsive/districtWiseWarning.php
29. *Odisha*. https://mausam.imd.gov.in/bhubaneswar/
