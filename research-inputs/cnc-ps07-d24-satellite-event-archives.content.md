# Replay-Ready Satellite Evidence for Odisha Cyclones and Floods

## 1. EXECUTIVE SUMMARY

- **Replay Is Feasible, Product Reuse Is Not Uniform**: All six proposed cases can be reconstructed from raw Sentinel and NASA archives, but the search found only one clear public, event-specific NRSC inundation map for Odisha, dated **16 August 2022**. No indexed Copernicus EMS or UNOSAT flood-extent activation was found for Fani, Amphan, Yaas, or Dana. Build an archive-first pipeline rather than assuming that finished flood shapefiles exist. [25][28]

- **Two Cases Provide The Strongest Validation Core**: The August 2022 flood has an NRSC inundation PDF, while Yaas has both an Odisha memorandum and a published study combining Sentinel-1 SAR with optical imagery. Use these as the primary spatial-validation cases; use Fani, Amphan, and Dana mainly as archive-derived replays with administrative impact checks. [25][17][22]

- **IMERG Removes The Rainfall Time-Series Gap**: GPM IMERG Final V07 covers **June 2000 to the present**, at **30-minute, 0.1 degree** resolution, so every named event has a common rainfall source. NASA does not provide a ready-made Odisha storm-total raster: the team must sum calibrated half-hourly precipitation over a declared event window. [14]

- **SAR Is The Operational Flood Backbone**: Sentinel-1 works through cloud and at night, whereas cyclone-period optical images are often obscured. The important exception is Dana: Sentinel-1B had stopped providing data in December 2021 and Sentinel-1C was not launched until December 2024, so the October 2024 replay relied on a single-satellite era and may have a wider before/after interval. [29][30]

- **MODIS/VIIRS Flood Products Are Triage, Not Field Truth**: NASA's MCDWD and VCDWD products are daily at approximately **250 m**. NASA explicitly warns that cloud shadows can create false positives, so they can identify the broad flood day but should not validate village or parcel inundation. [6]

- **Official Crop Baselines Are More Valuable Than Generic AI Accuracy**: Amphan's final memorandum reports **10,726.18 ha affected** and **3,393.50 ha with at least 33% loss**; Yaas reports **5,672.99 ha affected** and **2,197.34 ha with at least 33% loss**. These are appropriate district/state area checks, even though they are not pixel-level labels. [20][22]

- **Rice Mapping Accuracy Is Not Damage Accuracy**: A major Asian SAR study validated rice/non-rice mapping across 13 sites, using 1,334 validation points, but it did not validate flood-damage severity. An NDVI drop or SAR backscatter change must therefore be labeled a proxy until calibrated against Odisha crop-loss observations. [21]

- **Decision: PARTIAL**: A realistic hazard-and-advisory replay is achievable today with free data, and district-level outcome validation is credible for several events. Parcel-level avoided-loss claims remain gated by unavailable field labels, inconsistent event-product downloads, and no Odisha-specific validated conversion from a spectral change to percent crop loss. [31][32][28]

## 2. EVENT DATASET

### Reliability scale

- **A**: official or peer-reviewed event-specific geospatial product with usable metadata and a strong validation path.
- **B**: official impact report or event-specific satellite analysis, but only as a PDF/web layer, with incomplete resolution, export, or validation information.
- **C**: event is reconstructable from raw archives and has an impact baseline, but no reusable published extent product was located.
- **D**: generic context, unverified derivative, or search noise; not a replay truth layer.

| Event | What exists | Named source, URL, and date | Format and resolution | Access today | Reliability |
|---|---|---|---|---|---|
| **Cyclone Fani** | Raw Sentinel-1 GRD, Sentinel-2/Landsat optical scenes, and IMERG; official Fani Damage, Loss, and Needs Assessment. No indexed event-specific CEMS, UNOSAT, or public NRSC flood-extent product was found. | OSDMA, *Cyclone Fani 2019 Odisha DLNA Report*, event landfall **3 May 2019**: https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf [24] | DLNA PDF; raw S1 GRD has 10/25/40 m collection classes in Earth Engine; S2 has band-dependent 10/20/60 m data; Landsat is 30 m; IMERG is 0.1 degree. | Reports are public. Raw Copernicus and NASA data require free accounts. | **C** |
| **Cyclone Amphan** | Bhuvan exposes a named **"Amphan Cyclone and Space based Inputs"** layer sourced to SAC, Ahmedabad; an official final memorandum provides damage and daily rainfall baselines. No reusable vector/raster download or stated resolution was exposed. | Bhuvan Disaster Services, event layer for **May 2020**: https://bhuvan-app1.nrsc.gov.in/disaster/ [33]. Odisha SRC, *Final Memorandum on Super Cyclonic Storm Amphan*, event date **20 May 2020**: https://srcodisha.nic.in/calamity/Final%20Memorandum%20on%20Super%20Cyclone%20AMPHAN%20-%20Shyamal.pdf [20] | Dynamic Bhuvan web layer, resolution/export not disclosed; memorandum PDF; raw Sentinel and IMERG archives. | Viewer and PDF are public. Ask NRSC/SAC for machine-readable event layer if the web application does not expose export. | **B** |
| **Cyclone Yaas** | Published analysis combining Sentinel-1 flood inundation with optical data; official Odisha memorandum contains warning, advisory, district, and crop-loss records. The underlying study raster was not found as an open download. | Das and Dutta, *Impact of Tropical Cyclone Yaas on Coastal Regions of Odisha and West Bengal*, DOI 10.1002/gj.5153, event **26 May 2021**: https://www.semanticscholar.org/paper/1920784a71032a72aec47f6e1a978b15eb0c22ca [17]. Odisha memorandum: https://srcodisha.nic.in/calamity/Yass%20Cyclone%202021-%20Memorandum_compressed.pdf [22] | Published figures/article plus PDF; raw Sentinel-1 and optical scenes. Resolution and map accuracy were not reported in the accessible abstract. | Article metadata and memorandum are public; recreate the raster from Copernicus scenes unless authors provide data. | **B** |
| **Cyclone Dana** | ISRO tracked the cyclone with EOS-06 and INSAT-3DR from **20 October 2024**; raw Sentinel, optical, IMERG, and MODIS MCDWD archives can be used. The located ISRO page is a storm tracker, not an inundation or crop-damage map. | ISRO, *ISRO Satellites Track Cyclone DANA*, October 2024: https://www.isro.gov.in/ISROSatellitestrackCycloneDANA.html [7]. Youth for Social Development rapid assessment, **24-28 October 2024**: https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf [23] | Meteorological imagery/web page; NGO PDF; archive-derived S1/optical/IMERG. The rapid assessment gives no satellite-derived crop layer. | ISRO page and NGO report are public. No finished flood vector/raster was located. | **C** |
| **Odisha flood, 26 Aug-3 Sep 2020** | Official flood memorandum with a detailed district crop table and 24-hour rain observations; raw S1, S2/Landsat, MODIS, and IMERG are available. No event-specific public NDEM extent map was found in the indexed results. | Odisha SRC, *Memorandum on Flood and Heavy Rain 2020*: https://www.srcodisha.nic.in/calamity/Memorandum%20on%20Flood%20and%20Heavy%20Rain%202020.pdf [15] | PDF impact tables; raw satellite rasters. Rain gauges are reported for the preceding 24 hours at 08:30 AM. [15] | Public PDF and free raw archives. | **B** |
| **Odisha flood, 16 Aug 2022** | A named NRSC/NDEM map, *Flood Inundated Areas in Part of Odisha State*, covering 13 districts on 16 August 2022. This is the clearest finished flood-extent hit. | NRSC/NDEM, **16 August 2022**: https://ndem.nrsc.gov.in/documents/Disaster_Document/2022/OD/odflood50dsc16082022/odflood50dsc16082022_map.pdf [25] | Public map PDF. The indexed/extracted record did not expose the source sensor, pixel resolution, area total, or machine-readable vector. | Direct public PDF. Request GIS data from NRSC/NDEM if a downloadable layer is not available in the viewer. | **B** |

### Cross-event archive package

For each event, create the same four-layer bundle:

1. **Sentinel-1 GRD**: pre-event and post-event acquisitions with the same orbit direction, relative orbit, resolution, and polarization. Sentinel-1 IW provides a **250 km swath** and approximately **5 x 20 m instrument resolution**, while high-resolution GRD is commonly sampled at 10 m. [34]
2. **Sentinel-2 L2A or Landsat Collection 2 Level-2**: cloud-masked pre/post surface reflectance. Landsat Collection 2 is delivered as cloud-optimized GeoTIFF. [10]
3. **IMERG Final V07**: calibrated precipitation for every 30-minute interval, summed over the declared event window. NASA exposes it through GES DISC, OPeNDAP, THREDDS, Earthdata Search, and Giovanni. [14]
4. **Administrative truth**: event memorandum, DLNA, or rapid assessment containing affected districts, crop area, and recovery actions.

### What students can download now

| Source | Free? | Account/request | Practical note |
|---|---|---|---|
| Copernicus Data Space | Yes | Free registration for download/API | It advertises free instant Sentinel access. Use this current endpoint rather than designing around the old Open Access Hub name. [28] |
| NASA Earthdata/GES DISC | Yes | Earthdata Login | EOSDIS data are generally open and free; login is required for many downloads and full tool functions. [32][6] |
| USGS Landsat | Yes | Free USGS/EarthExplorer account for bulk workflows | Collection 2 Level-2 COGs avoid a proprietary conversion step. [10] |
| Bhuvan/NDEM | Viewer and many PDFs are free | Machine-readable event layers may require NDEM login or an agency request | ISRO describes disaster services as free, but the located public pages did not establish bulk event-vector downloads. [31] |
| Google Earth Engine S1 GRD | Free for eligible research/education use | Earth Engine project/account | The catalog contains all GRD scenes and allows district clipping before export, reducing local storage. [27] |

### Sentinel-1 scene-pair data-volume reality

A fixed file size cannot be quoted responsibly because it varies by mode, polarization, scene length, compression, and processing level. A transparent array calculation is more useful. At 10 m, one square kilometre contains 10,000 pixels.

| Example district AOI | Pixels at 10 m | Two dates, VV+VH, float32 array | Sensible workspace including masks and intermediates |
|---|---:|---:|---:|
| 1,000 sq km | 10M | 160 MB | 1-2 GB |
| 3,000 sq km | 30M | 480 MB | 2-4 GB |
| 5,000 sq km | 50M | 800 MB | 4-6 GB |

These are calculated raster-array sizes, not guaranteed SAFE download sizes. A student laptop with 8 GB RAM can work by clipping and tiling one polarization at a time; 16 GB is safer for dual-polarization SNAP processing. Earth Engine or a cloud COG workflow is preferable if repeated full-scene terrain correction is needed.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---|---|---|
| **Sentinel-1 raw archive** | Reconstructable SAR for all events; all-weather/day-night; 10/25/40 m GRD collection classes. [27] | No catalog-exported acquisition list was preserved in the located event reports; Dana has a weaker temporal configuration because S1B had failed before the event. [29] | **A for hazard reconstruction; C for ready-made products** |
| **Sentinel-2/Landsat** | Surface-reflectance archives suitable for NDVI and recovery trajectories; Landsat COG delivery. [10] | Cloud, shadow, crop phenology, harvest, and different acquisition dates can imitate damage. NDVI research warns that precipitation, cloud, human activity, and sensor effects introduce noise. [35] | **B** |
| **GPM IMERG** | One consistent half-hourly rainfall product for every event from 2019-2024. [14] | No ready-made Odisha storm-total download; 0.1 degree grid is too coarse for individual farms. Final data are delayed by about four months. | **A for regional hazard; C for hyperlocal rainfall** |
| **NASA MODIS/VIIRS flood** | Daily global MCDWD and VCDWD at approximately 250 m; Worldview/FLOOD viewer access. [6] | Cloud-shadow false positives; VCDWD was only released in April 2025, so historical product availability must be checked rather than assumed. [6] | **B for triage; D for parcel validation** |
| **NRSC/NDEM/Bhuvan** | 16 Aug 2022 inundation PDF; Amphan SAC/Bhuvan layer; national and state hazard atlases; official disaster repository. [33][25] | Inconsistent indexing, dynamic viewers, incomplete metadata, and unclear event-vector downloads. | **B** |
| **OSDMA/SRC impact reports** | Strongest area and recovery baselines: Amphan, Yaas, 2020 flood, Fani DLNA. | Usually administrative/field assessments, not pixel labels; some totals differ slightly between sections. | **A for district impact; C for spatial truth** |
| **Published Odisha satellite studies** | Yaas study combines Sentinel-1 and optical data. [17] | No comparable indexed vegetation-damage study was located for Fani, Amphan, or Dana; Yaas map resolution and accuracy were not exposed in the accessible record. | **C** |
| **SAR rice methods** | Multi-temporal SAR rice/non-rice mapping was validated across six countries and 13 sites. [21] | Validation concerns rice area, not flood depth, crop mortality, yield loss, or recovery. | **B for crop mask; D for uncalibrated damage severity** |
| **VIIRS FIRMS/Black Marble** | FIRMS can supply fire points; Black Marble gives daily/monthly/yearly nighttime-light composites at 750 m. [36][12] | Fire is not a normal cyclone crop-loss measure. A light decline can reflect clouds, moonlight correction, power outage, evacuation, or sensor effects and does not prove physical damage. | **D for core replay; C for context** |
| **Lightning** | LIS records lightning time, radiant energy, and location at roughly 4-8 km and one-minute to sub-hourly scales. [5] | The located record did not establish exact coverage for each Odisha event. VIIRS is not the appropriate lightning instrument. | **C for optional context; D for validation** |
| **Copernicus EMS, GDACS, UNOSAT** | Services are real and useful elsewhere. | Searches returned catalog home pages and unrelated maps, not a named Odisha flood-extent product for the four cyclones. | **D for these cases** |

The central contrast is between **high raw-data coverage** and **low finished-product coverage**. The team should judge success by whether it can reproduce a defensible extent and match independent impact records, not by how many branded map portals appear in the demo.

## 4. WHAT IS MISSING

### Temporal and rainfall gaps

- **No named event lacks sub-hourly satellite rainfall**: IMERG supplies 30-minute data for Fani, Amphan, Yaas, Dana, and both floods. [14]
- **All events lack a located public, continuous hourly district rain-gauge file**. Amphan and the 2020 flood reports provide observations accumulated over the preceding 24 hours at 08:30 AM, not hourly station series. [20][15]
- **Yaas's memorandum exposes date-specific forecasts rather than an hourly observed-rainfall archive**. It forecasts extremely heavy falls in Balasore, Bhadrak, Kendrapara, and Mayurbhanj on 26 May. [22]
- **No source supplied ready-computed IMERG storm totals**. Each replay must publish its start/end timestamps, AOI, IMERG field, and aggregation code.

### Spatial-product gaps

- No indexed Copernicus EMS, UNOSAT, or GDACS event product was located for any of the four named cyclones.
- Fani has an excellent multisector DLNA but no located published flood-extent raster. Its assessment drew on agriculture/horticulture departments, OUAT, economic statistics, and field visits, not a stated satellite crop map. [24]
- Amphan's Bhuvan/SAC layer is visible by name, but resolution, acquisition, processing method, and vector/raster download were not disclosed. [33]
- Yaas has a published Sentinel assessment, but the accessible record supplies neither the underlying map nor exact validation accuracy. [17]
- Dana's ISRO page documents cyclone tracking, not flood extent. The October 2024 single-Sentinel-1 era can also widen the pre/post interval. [7][29]
- The 2022 NDEM map is a PDF. Its indexed record did not expose sensor, scale, pixel resolution, total inundated area, or GIS download. [25]

### Exact crop-damage gaps by event and district

- **Fani**: the DLNA records field visits and sector methods, but the accessible extraction did not yield a reliable consolidated district-hectare table. Do not use the OCR-rendered statewide hectare figure because it is internally implausible.
- **Amphan**: ten districts are named, but the extracted report supports state totals rather than a complete district-by-district crop table. The state total is 10,726.18 ha affected; 3,393.50 ha had at least 33% loss. [20]
- **Yaas**: crop figures are available for Balasore, Bhadrak, Jagatsinghpur, Jajpur, Kendrapara, Keonjhar, Mayurbhanj, Puri, and Sundargarh. Cuttack and Dhenkanal are listed among affected districts but have no crop-area entries in the extracted crop table. [22]
- **Dana**: the rapid assessment gives a combined **5,428 acres** for Kendrapara and Bhadrak. It does not split the figure between those districts or among Rajnagar, Rajkanika, Basudevpur, and Chandbali blocks. [23]
- **2020 flood**: this is the strongest tabular baseline, with **313,650.713 ha affected** and **235,925.493 ha** at 33% or greater loss, plus district values. [15]
- **2022 flood**: the NDEM map identifies inundation in 13 districts but provides no crop-loss percentage, yield loss, or compensation figures in the indexed record. [25]

## 5. HOW IT FEEDS THE REPLAY SIMULATION

| Simulation layer | Evidence and transformation | Engine validation |
|---|---|---|
| **Hazard field** | Replay IMD bulletin/track timestamps; sum IMERG half-hourly precipitation; create pre/post Sentinel-1 water change; use MODIS MCDWD only as a coarse daily cross-check. | Rainfall timing error; flood-area agreement; map intersection-over-union and precision/recall where an independent extent exists. IMERG is regional, not farm-level truth. [14][6] |
| **Farm exposure** | Intersect the hazard field with farm boundary, crop type, sowing date, growth stage, elevation, and drainage. Use a validated rice/non-rice mask or the farmer profile rather than treating all green pixels as rice. | Compare exposed hectares by district with Odisha memoranda. Rice-mask accuracy and damage accuracy must be reported separately. [21] |
| **Crop damage proxy** | Compute same-season pre/post SAR backscatter change and cloud-masked NDVI anomaly. For Sentinel-2 use B8 and B4; for Landsat 8/9 use B5 and B4. Add persistence: one anomalous acquisition is "possible damage"; repeated anomaly plus mapped inundation is "probable damage." | Compare estimated affected area with the official >=33% loss area. Do not convert NDVI change directly to percent yield loss without local calibration. |
| **Advisory timing** | Freeze the simulation clock at each historical IMD bulletin. Feed only information available by that time to the advisory engine. Yaas is useful because IMD's 24 May bulletin predicted landfall about **54 hours** ahead. [37] | Lead time, percentage of exposed farms reached before the action deadline, and whether advice changes appropriately as confidence rises. |
| **Pre-disaster action** | Generate crop-stage-specific actions: harvest mature crop, move harvested produce, clear drainage, secure pumps, protect seed/fodder, and avoid unsafe field work. Amphan and Yaas reports confirm that OUAT/Directorate crop advisories were actually issued and broadcast. [20][22] | Compare the simulated recommendation category and issue time with the historical government advisory. Do not claim avoided loss unless an intervention model is calibrated. |
| **Recovery** | After landfall, switch to inundation persistence, vegetation recovery, farmer-reported condition, and official loss thresholds. Trigger re-sowing, drainage, disease watch, input support, and compensation guidance. | Area error against the official affected and >=33% loss totals; recovery-time curve from NDVI/SAR; agreement with documented relief measures. |

### Recommended case-study sequence

**Case 1, August 2022 flood**: Reconstruct a 16 August flood extent from Sentinel-1, then compare it with the NDEM PDF. This tests geospatial processing without the confounder of cyclone wind damage. Because the NDEM deliverable is a PDF rather than a verified open vector, record both georeferencing error and flood-classification error.

**Case 2, Cyclone Yaas**: Replay IMD warnings, use Sentinel-1 for inundation, optical data for post-event vegetation change, and the Odisha memorandum for crop totals. This tests the complete chain from warning through advisory to recovery. The published Yaas Sentinel study provides methodological corroboration, but its map should not be treated as an accuracy-certified label unless the full data and validation are obtained. [17]

**Case 3, 2020 flood**: Use the detailed district crop table as the area-validation benchmark. The memorandum reports 27 districts affected overall and a district-level crop table, making it better for statistical validation than for pixel validation. [15]

**Cases 4-6, Fani, Amphan, Dana**: Treat these as robustness tests across storm intensity, season, sensor cadence, and administrative-data quality. They add narrative breadth, but they should not carry the main claim of spatial accuracy.

## 6. REAL-vs-FILLER

| Evidence | REAL: defensible use | FILLER: claim to avoid |
|---|---|---|
| Sentinel-1 pre/post pair | Flood-candidate map after orbit matching, calibration, terrain correction, permanent-water masking, and independent checking. | "Satellite proves this parcel lost its crop" from one thresholded image. |
| IMERG Final | Common 30-minute rainfall forcing and storm-total grid for all events. [14] | "Hyperlocal rainfall at each farm" from a roughly 10 km grid. |
| Sentinel-2/Landsat NDVI | Vegetation-anomaly and recovery proxy after cloud masking and seasonal controls. | Direct yield-loss percentage or causal proof of cyclone damage. |
| NRSC 16 Aug 2022 PDF | Independent event-specific flood-map comparison. [25] | Calling it a downloadable, ground-validated 10 m vector without metadata. |
| Amphan/Yaas/2020 official reports | District/state area and >=33% loss benchmarks; historical advisory evidence. [20][22][15] | Pixel-level ground truth or randomized evidence that advice prevented loss. |
| Bhuvan Amphan layer | Demonstrates an Indian space-agency event product exists. [33] | Claiming open raster/vector access, resolution, or accuracy not shown by the portal. |
| ISRO Dana tracker | Hazard context and satellite-observation provenance. [7] | Flood extent, crop damage, or recovery map. |
| MODIS/VIIRS flood | Coarse day-level corroboration and rapid visual triage. [6] | Village or field boundary validation. |
| FIRMS active fire | Optional secondary-hazard context if a verified fire occurred. | Generic cyclone damage indicator. |
| Black Marble | Exploratory regional outage/recovery context at 750 m. [12] | Proof of crop damage, or a clean outage count without cloud and radiance controls. |
| LIS lightning | Optional storm-convection timeline where event coverage is confirmed. [5] | A VIIRS lightning product or a required agriculture-advisory input. |

The demo should prominently show the event clock, source timestamp, uncertainty, and validation target. Extra animated cyclone imagery adds presentation value but must not be counted as evidence that the advisory engine is accurate.

## 7. NOISE LOG

| Search path | Returned | Why discarded |
|---|---|---|
| Fani + NRSC/Bhuvan flood map | Satellite handbooks, ground-station pages, and generic Bhuvan forum pages | No event extent or damage product. |
| Amphan/Yaas/Dana + UNOSAT | Maps for Viet Nam, Mozambique, the Philippines, and later Pakistan floods | Correct technology, wrong event and geography. |
| Named cyclones + Copernicus EMS | CEMS home and activation catalog, including unrelated 2026 activations | A service landing page is not evidence of a named activation. |
| Named cyclones + GDACS | Cyclone summaries, Wikipedia, social posts, and meteorological images | Track/context only; no downloadable Odisha flood layer. |
| Fani + NDVI/crop satellite | Generic NDVI explainers and unrelated land-cover papers | No Fani/Odisha event validation. |
| Rice flood-damage accuracy | General flood mapping, paddy nutrient leaching, generic damage-function, and crop-health papers | Flood accuracy, crop presence, and physiological response are not the requested satellite damage-severity accuracy. |
| Sentinel-1 file size | SNAP installer size and processing tutorials | Installer size is not scene size; no authoritative fixed GRD scene-size value was found. |
| NRSC Odisha map search | 2025 and 2026 flood maps | Useful evidence of NRSC practice, but outside the requested replay events. |
| Dana crop figures from news | Preliminary totals ranging around 79,000 ha or separate damaged/submerged acre figures | Not adopted because the located official final district table was absent and preliminary reports differed. |
| Fani DLNA OCR | An internally implausible hectare rendering | Excluded rather than silently correcting an official-document OCR error. |

This discarded material is important to log because it prevents three common demo errors: presenting an unrelated flood map, mistaking a portal for an activation, and quoting a model accuracy that measures a different target.

## 8. VERDICT: PARTIAL

### What can be built credibly

1. **GO for hazard replay** across all named events using IMERG, Sentinel-1, optical archives, IMD chronology, and official reports.
2. **GO for end-to-end validation** on Yaas and the August 2022 flood, with explicit limitations on the published maps.
3. **GO for district-level crop-area validation** on Amphan, Yaas, and especially the 2020 flood.
4. **GO for SMS/IVR timing tests** by replaying historical warnings and checking whether advice arrives before farm-action deadlines.

### What remains gated

1. **GATED for parcel-level percent crop loss**: no Odisha event dataset was found that jointly supplies field boundaries, crop stage, flood depth/duration, observed yield, and satellite features.
2. **GATED for causal avoided-loss claims**: historical reports document impacts and advisories, but they do not provide treated-versus-untreated farms.
3. **GATED for plug-and-play finished maps for every cyclone**: the public product trail is too sparse and inconsistent.
4. **GATED for a claimed universal model accuracy**: rice-area validation cannot be transferred to flood-damage severity. [21]

The minimum defensible prototype is therefore a **replay and validation system**, not a loss-prevention simulator that invents counterfactual savings. It should output: warning lead time, rainfall accumulation, flood probability/extent, farms and crop hectares exposed, advisory delivered, observed administrative impact, and uncertainty. Keep predicted avoided loss as a scenario range, clearly labeled as modelled.

A practical build order is: **(1)** August 2022 flood for spatial QA, **(2)** Yaas for complete warning-to-recovery replay, **(3)** 2020 flood for district-area calibration, and **(4)** Fani, Amphan, and Dana as robustness cases. This sequence maximizes what can be validated before spending time digitizing weak map products or requesting restricted layers.

## Synthesis

| Strategy | Mechanism | Scope | Main trade-off | Recommended role |
|---|---|---|---|---|
| **Raw-archive-first** | Reprocess Sentinel and IMERG consistently for every event. | Broadest event coverage and reproducibility. | Requires SAR/optical QA and creates a team-generated rather than agency-published extent. | Core production pipeline. |
| **Published-product-first** | Reuse NRSC/Bhuvan or peer-reviewed event maps. | Strong provenance where products exist. | Sparse, inconsistently indexed, often PDF-only, and missing resolution/export metadata. | Independent check, not universal input. |
| **Impact-report-first** | Calibrate against official affected-area and >=33% loss tables. | Strong district/state outcome validation. | Administrative units are too coarse for field-level model accuracy. | Main crop-impact benchmark. |
| **Context-signal-first** | Add MODIS, Black Marble, fire, or lightning layers. | Rich storytelling and regional context. | Coarse resolution and weak causal connection to crop damage. | Optional diagnostics only. |

The non-obvious result is that the most realistic replay does not come from finding one perfect satellite damage product. It comes from combining three imperfect but independent evidence streams: a reproducible raw hazard reconstruction, an event-specific map where available, and official impact totals. Their disagreements should be displayed, not hidden. A Sentinel extent that matches an NRSC map but badly overpredicts district crop losses probably has a crop-mask or permanence problem; a strong match to administrative crop hectares but a weak spatial match may indicate PDF georeferencing or reporting-boundary error.

The final architecture should therefore preserve uncertainty at every join. Hazard evidence answers **where and when water or heavy rain occurred**; optical and SAR changes answer **where crops may have been stressed**; official reports answer **what authorities ultimately recorded**. Only their intersection supports a strong recovery advisory. That evidence discipline is what makes the replay statement-faithful rather than decorative.

## References

1. *Bhuvan | ISRO's Geoportal | Gateway to Indian Earth Observation | Disaster Services*. https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php
2. *Landsat Collection 2 Level-2 Science Products | U.S. Geological Survey*. https://www.usgs.gov/landsat-missions/landsat-collection-2-level-2-science-products
3. *Flood Affected Area Atlas Of India Satellite Based Study*. https://ndem.nrsc.gov.in/documents/downloads/Flood%20Affected%20Area%20%20Atlas%20of%20India%20-Satellite%20based%20study.pdf
4. *SRC || Cyclone Dana*. https://srcodisha.nic.in/Cyclone-Dana.php
5. *Lightning Imaging Sensor | NASA Earthdata*. https://earthdata.nasa.gov/data/instruments/lis
6. *FLOOD | NASA Earthdata*. https://www.earthdata.nasa.gov/data/tools/flood
7. [
        ISRO Satellites track Cyclone DANA
    ](https://www.isro.gov.in/ISROSatellitestrackCycloneDANA.html)
8. *Sentinel-2 L2A*. https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l2a
9. *Sentinel-2 | Copernicus Data Space Ecosystem*. https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2
10. *Landsat Collection 2 | U.S. Geological Survey*. https://www.usgs.gov/landsat-missions/landsat-collection-2
11. *FIRMS | NASA Earthdata*. https://www.earthdata.nasa.gov/data/tools/firms
12. *Black Marble | NASA Earthdata*. https://www.earthdata.nasa.gov/data/projects/black-marble
13. *Sentinel-1 GRD*. https://docs.sentinel-hub.com/api/latest/data/sentinel-1-grd
14. [GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHH) at GES DISC - Dataset 
          - 
        NASA Open Data Portal](https://data.nasa.gov/dataset/gpm-imerg-final-precipitation-l3-half-hourly-0-1-degree-x-0-1-degree-v07-gpm-3imerghh-at-g-fb698)
15. *CONTENTS*. https://www.srcodisha.nic.in/calamity/Memorandum%20on%20Flood%20and%20Heavy%20Rain%202020.pdf
16. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
17. *Impact of Tropical Cyclone Yaas on Coastal Regions of Odisha and West Bengal, India: An Assessment Using Sentinel Datasets | Semantic Scholar*. https://www.semanticscholar.org/paper/Impact-of-Tropical-Cyclone-Yaas-on-Coastal-Regions-Das-Dutta/1920784a71032a72aec47f6e1a978b15eb0c22ca
18. *Aerial Image Road Extraction Based on an Improved Generative Adversarial Network*. https://www.mdpi.com/2072-4292/11/8/930
19. *Fertilizer of the Future: Beneficial Bacteria Promote Strawberry Growth and Yield and May Reduce the Need for Chemical Fertilizer*. https://www.mdpi.com/2073-4395/12/10/2465
20. *Final Memorandum On Super Cyclone Amphan Shyamal*. https://srcodisha.nic.in/calamity/Final%20Memorandum%20on%20Super%20Cyclone%20AMPHAN%20-%20Shyamal.pdf
21. *Towards an Operational SAR-Based Rice Monitoring System in Asia: Examples from 13 Demonstration Sites across Asia in the RIICE Project*. https://www.mdpi.com/2072-4292/6/11/10773
22. *1*. https://srcodisha.nic.in/calamity/Yass%20Cyclone%202021-%20Memorandum_compressed.pdf
23. *Cyclone Dana Assessment Report*. https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf
24. *untitled*. https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
25. *Flood Inundated Areas in Part of Odisha State For official use*. https://ndem.nrsc.gov.in/documents/Disaster_Document/2022/OD/odflood50dsc16082022/odflood50dsc16082022_map.pdf
26. *Hydrological Disaster - National Remote Sensing Centre*. https://ndem.nrsc.gov.in/hydrologicaldisasters/index.php
27. *Sentinel-1 SAR GRD: C-band Synthetic Aperture Radar Ground ...*. https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD
28. *Copernicus Data Space Ecosystem | Europe's eyes on Earth*. http://dataspace.copernicus.eu/
29. *Sentinel-1 – Documentation - Copernicus*. https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel1.html
30. *Sentinel-1 - Sentinel Online*. https://sentinels.copernicus.eu/copernicus/sentinel-1
31. *Disaster management: National and international*. http://isro.gov.in/DisasterManagementNationalInternational.html
32. *NASA - Earthdata Login*. https://urs.earthdata.nasa.gov/
33. *ISRO's Geoportal | Gateway to Indian Earth Observation | 2D ...*. https://bhuvan-app1.nrsc.gov.in/disaster/
34. *Sentinel-1*. https://www.earthdata.nasa.gov/data/platforms/space-based-platforms/sentinel-1
35. *Field validation of NDVI to identify crop phenological ...*. https://link.springer.com/article/10.1007/s11119-024-10165-6
36. *NASA | LANCE | FIRMS - Active Fire Data*. http://firms.modaps.eosdis.nasa.gov/active_fire
37. *Very Severe Cyclonic Storm YAAS over the Bay of Bengal ... - IMD*. https://internal.imd.gov.in/press_release/20210611_pr_1133.pdf
