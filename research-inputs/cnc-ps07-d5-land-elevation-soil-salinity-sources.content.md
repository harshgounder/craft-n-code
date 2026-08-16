# Free Geospatial Stack for Odisha Flood-Salinity Advice

## 1. EXECUTIVE SUMMARY

- **The free DEM premise needs correction:** USGS SRTM is **1 arc-second, about 30 m**, JAXA's free AW3D30 v4.1 is also **about 30 m**, and Bhuvan's publicly documented CartoDEM releases are **1 arc-second, about 32 m**. The researched official sources do not support treating free JAXA AW3D as a native 12.5 m DEM or public Bhuvan CartoDEM as 10 m [4][5][39].
- **All three DEM families cover Odisha, but none resolves plot microrelief by itself:** a 30-32 m cell can support regional flow-path and lowland screening, but it cannot reliably represent narrow bunds, roadside drains, field ditches, or small elevation differences within flat coastal-delta plots. Use DEM output as a risk prior, then calibrate it with surveyed elevations and observed flood depths [4][5][39].
- **Cropland can be identified programmatically today:** Bhuvan offers multi-date land-use/land-cover products at 1:50,000 and 1:250,000, while SIS-DP Phase 2 includes 1:10,000 products for 2018-2023. Sentinel-2 adds 10-20 m, five-day multispectral observations suitable for NDVI and seasonal crop signatures [45][6].
- **The public crop-mask gap is operational, not conceptual:** FASAL uses optical and microwave remote sensing for district, state, and national forecasts of nine crops, but the reviewed public material does not document a downloadable seasonal pixel-level crop-mask API. A prototype should therefore derive its own Sentinel-2 time-series mask or obtain an NRSC/MNCFC layer through partnership [14].
- **Soil properties exist, but plot linkage is incomplete:** ICAR-NBSS&LUP's BHOOMI describes maps from 1:1 million to 1:10,000 and includes pH, electrical conductivity, organic carbon, calcium carbonate, texture, and six depth intervals. Only eight Odisha blocks are reported at 1:10,000 in the reviewed document, and no documented bulk API was found [35].
- **Soil Health Card data is scientifically useful but not publicly integration-ready:** the program measures 12 parameters, including pH, EC and organic carbon, on nominal 2.5 ha irrigated and 10 ha rainfed grids. The current official source reports more than 25 crore cards nationally by July 2025, but no current numerical Odisha total was found; an older Odisha fact sheet reports only 40-50% of target achievement [17][42].
- **Yaas flood evidence must not be relabeled as salinity:** SAC used 10 m Sentinel-1 SAR to map inundation in Bhadrak and Kendrapara and Sentinel-2 to map turbidity. These products show water and sediment effects, not soil or water EC; post-surge salinity therefore requires field EC sampling or an independently validated salinity product [10].
- **Groundwater context is available at block scale:** CGWB's 2024 assessment reports Odisha recharge of 17.46 bcm, extractable resources of 16.04 bcm, extraction of 7.74 bcm, a 48.23% stage of extraction, and 6 saline assessment units among 314 blocks. India-WRIS says unclassified CGWB groundwater data can be downloaded free, but its public page does not establish a prototype-ready station API with consistent update metadata [24][9].
- **Overall verdict - PARTIAL:** free public data is sufficient for screening farms, prioritizing alerts, mapping event inundation, and supporting next-season planning. Claim-grade plot decisions and automatic salinity advisories remain gated by cadastral polygons, current crop and phenology records, surveyed micro-elevation, field EC, local drain condition, and validated water-depth observations [22][31][40].

## 2. DATA INVENTORY

**Grade key:** A = authoritative, documented, and directly machine-usable; B = authoritative or technically credible but coarse, partial, or manually accessed; C = useful research or historical proxy with important access or validation limits; D = unsuitable, unverified, or absent for the stated decision.

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---:|---|---|---:|
| SRTM elevation | USGS, **SRTM 1 Arc-Second Global**, data acquired 11-22 Feb 2000; https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-1-arc-second-global [4] | 1 arc-second, about 30 m; 60 N to 56 S [4] | Static 2000 terrain observation | Free file download through EarthExplorer; GeoTIFF, BIL and DTED formats are documented [4] | A |
| JAXA elevation | JAXA, **ALOS World 3D 30 m v4.1**, source observations 24 Jan 2006 to 12 May 2011; https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V4_1 [5] | Approximately 30 m DSM, not a native 12.5 m DEM [5] | Static 2006-2011 source period | No-charge files and Earth Engine catalog; quality, stack and water-mask bands are documented [5] | A |
| India-specific elevation | NRSC Bhuvan Wiki, **CartoDEM** releases: v1 Aug 2006, v1.1R1 Dec 2008, and v2R1/v3R1 generated from 2005-2014 data; https://bhuvan.nrsc.gov.in/wiki/index.php/CartoDEM [39] | 1 arc-second, about 32 m, tiled over India [39] | Static, release-dependent | Free Bhuvan download; no official 10 m public CartoDEM product was verified | B |
| Cartosat source imagery | ISRO, **Cartosat-1 mission**; https://www.isro.gov.in/Cartosat_1.html | Panchromatic sensor imagery at 2.5 m; this is not the same as DEM output resolution [27] | Mission-era imagery | Mission information; derivative DEM access is through Bhuvan | B |
| Multi-date LULC | NRSC, **Bhuvan Store LULC**; 1:50,000 epochs 2005-06, 2011-12 and 2015-16; 1:250,000 annual products through 2022-23; https://bhuvan-app3.nrsc.gov.in/data/download/index.php [45] | 1:50,000 and 1:250,000 | Latest verified annual epoch 2022-23; finer 1:50,000 layer is older | WMS; 1:250,000 also downloadable. The reviewed listing says no download for 1:50,000 [45] | B |
| Fine LULC and administrative planning layer | NRSC, **SIS-DP Phase 2**, 2018-2023; Bhuvan Store URL above [45] | 1:10,000 | 2018-2023 | WMS and download for Phase 2; district coverage must be checked tile by tile [45] | B |
| Historical annual cropland | NRSC, **Annual Cropland**, 2005-06 to 2013-14; Bhuvan Store URL above [45] | 5 km | Historical and too coarse for plots | Downloadable file [45] | D for plot use |
| Current crop observation | ESA/Copernicus, **Sentinel-2 multispectral imagery**; rolling archive, accessed 16 Aug 2026; https://collections.sentinel-hub.com/sentinel-2-l2a/ | 10 m and 20 m bands; five-day revisit [6] | Rolling observations, subject to cloud availability | Free catalog; Sentinel Hub offers REST interfaces for imagery and statistics [7] | A |
| Operational crop masks and forecasts | MNCFC, **FASAL**, operational page accessed 16 Aug 2026; https://www.mncfc.gov.in/fasal [14] | Forecasts at district, state and national levels for nine crops [14] | Operational seasonal program | Public reports/pages; no downloadable seasonal pixel-mask API was verified | C for programmatic masking |
| Soil maps and district/block soil properties | ICAR-NBSS&LUP, **BHOOMI Geoportal**, Aug 2023; https://icar-nbsslup.org.in/ and https://bhoomigeoportal-nbsslup.in/ [35] | 1:1 million, 1:250,000, 1:50,000 and 1:10,000; 82 districts and 339 blocks nationally at finer scales [35] | Compilation current to the 2023 document; source surveys vary | Portal visualization, access and query. No documented bulk API was found in the reviewed description [35] | B |
| Odisha fine soil coverage | BHOOMI, Aug 2023; URLs above | Eight Odisha blocks are reported at 1:10,000; the reviewed excerpt does not identify all eight [35] | Survey-dependent | Portal or institutional request | C |
| Soil laboratory parameters | BHOOMI and Soil Health Card program; Aug 2023 and July 2025; https://soilhealth.dac.gov.in/ | BHOOMI includes six depths and pH, EC, OC, CaCO3 and texture; SHC includes 12 fertility parameters [35][17] | SHC sampling is cyclical; the official release contains inconsistent two-year and three-year wording [17] | Portal/report; farmer card lookup. No public sample-level Odisha export was verified | B for parameters, C for integration |
| Odisha Soil Health Card count | Government SHC/PIB material, latest reviewed national update July 2025; https://soilhealth.dac.gov.in/ and https://www.pib.gov.in/ | State program total | **Current numerical Odisha count not found.** The 2022 state fact sheet reports 40-50% target achievement, not a card count [42] | State records or Department of Agriculture partnership required | D for requested count |
| Coastal saline-soil extent | ICAR-CSSRI, **Extent and distribution of salt-affected soils**, page undated; https://cssri.res.in/ | State aggregate: 147,138 ha of coastal saline soils under the historical label Orissa [20] | Date and method are not stated on the reviewed page | Web table/report; no downloadable polygon was verified | C |
| Yaas inundation and turbidity | ISRO-SAC, **Assessment of Cyclone Yaas using satellite observations**, event 26 May 2021; https://www.sac.gov.in/ [10] | Sentinel-1 inundation at 10 m; Sentinel-2 turbidity at 10 m | Event snapshot | Free report/map products; underlying analysis-ready raster access is not established by the report | B for flood evidence, D for salinity measurement |
| Yaas affected land and cropland | Peer-reviewed Wiley study, published 2025; https://onlinelibrary.wiley.com/ | Regional land-cover impact; 2,528.70 sq km affected, including reported Odisha cropland impacts in Bhadrak and Kendrapara [3] | Retrospective analysis of May 2021 event | Article; underlying data available on request [3] | B for retrospective exposure |
| Groundwater resource status | CGWB, **National Compilation on Dynamic Ground Water Resources of India 2024 - Odisha assessment**; https://cgwb.gov.in/ | Block assessment: 314 blocks, including 6 saline units [24] | 2024 assessment | Free official report | A |
| Depth-to-water observations | India-WRIS groundwater subsystem, accessed 16 Aug 2026; https://indiawris.gov.in/wris/ | Well or station records where published | Station-dependent; update semantics must be checked | Free download for unclassified CGWB groundwater data [9] | B |
| Drainage network and density proxy | HydroSHEDS, **HydroRIVERS v1**, landing page undated; https://www.hydrosheds.org/products/hydrorivers [31] | Global network from 15 arc-second source data; minimum catchment about 10 sq km or average flow 0.1 cubic m/s [31] | Static global product | Free shapefile/geodatabase download [31] | B for basin drainage, D for field drains |
| State flood-hazard atlas | OSDMA/NRSC/NDMA, **Flood Hazard Atlas of Odisha**, page undated; https://www.osdma.org/flood-hazard-atlas/ [2] | Published map/atlas; resolution and machine-readable village fields are not stated on the reviewed page | Undetermined | Public page/report; vector/API access not verified | C |
| Flood-prone village list | No current statewide machine-readable list was identified in the reviewed official sources | Village | Missing | State records request to SRC/OSDMA, Revenue Department and districts | D |
| Parcel identifiers and ownership | Odisha Revenue Department, **Bhulekh**, live portal accessed 16 Aug 2026; https://bhulekh.ori.nic.in/ | 59,794,909 plots; lookup by district, tahasil, village, RI circle, khatiyan, plot and tenant [22] | Live transactional portal | Public record-of-rights lookup; no documented bulk GIS/API was found | B for lookup, D for spatial joins |
| Published Odisha flood model | **Baitarani River flood-inundation model**, 2021 conference paper; CartoDEM plus ArcGIS, HEC-GeoRAS and 1D HEC-RAS [40] | Basin/reach model; cross-sections about 1,500 m apart and 2,000 m wide [40] | Retrospective model using 2001-2018 discharge [40] | Paper; model files not reported as a public operational service | C |

The inventory separates **source authority** from **decision readiness**. An official map can still receive B, C or D for plot-level use when it is too coarse, old, non-downloadable, or lacks the identifiers required to join it to a farm.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing elements | Coverage judgment A-D |
|---|---|---|---:|
| DEM and terrain | Three official, free products: SRTM, AW3D30 and CartoDEM. All cover Odisha at about 30-32 m [4][5][39] | The claimed free 12.5 m AW3D and 10 m CartoDEM were not supported; no surveyed plot micro-DEM | B |
| Cropland and land cover | Bhuvan 1:250,000 annual LULC, selected 1:50,000 layers, SIS-DP 1:10,000 and Sentinel-2 time series [45][6] | FASAL mask download/API unverified; clouds and crop-calendar differences complicate automated classification | B |
| Soil properties | BHOOMI multi-scale maps plus SHC's 12 parameters [35][17] | Fine coverage is incomplete; current Odisha card count and sample-level export missing | B for regional use, C for plots |
| Salinity | CSSRI state total, CGWB saline blocks, Yaas flood/turbidity observations [20][24][10] | No public post-Yaas EC raster, time series or plot-level salt-depth profile | C |
| Groundwater | CGWB 2024 block assessment and free India-WRIS downloads [24][9] | Prototype-ready well API, uniform timestamps and shallow farm water-table coverage not established | B |
| Drainage and flood administration | HydroRIVERS plus OSDMA flood-atlas page [31][2] | Small drains, embankment condition, pump capacity and current flood-prone village file absent | C |
| Parcels | Bhulekh gives extensive plot and RoR lookup coverage [22] | No documented bulk parcel polygons or stable spatial API | C |
| Models and indices | One Baitarani HEC-RAS case provides a local hydrodynamic precedent and flood-depth classes [40] | No verified statewide, plot-calibrated flood-salinity index; no reported calibration/validation metrics in the reviewed case [40] | C |

**Coverage judgment:** Odisha has enough open layers for a useful **exposure-screening stack**, but not a complete observation stack. Terrain, land cover and event water extent are much better covered than salinity concentration, local drainage performance, crop status and cadastral geometry.

## 4. WHAT IS MISSING

The following gaps were not covered by a current, public, machine-readable source in the reviewed evidence. These names should be retained as explicit acquisition requirements rather than hidden behind a generic "local data" field.

1. **Plot-boundary GIS polygons with stable Bhulekh plot identifiers and a documented bulk API.** Bhulekh supports individual RoR and plot lookup but does not document a bulk spatial service [22].
2. **Survey-grade relative elevation for farm plots, bund crests, road crossings, culverts and drainage outlets.** All three verified free DEMs have about 30-32 m spacing [4][5][39].
3. **A current Odisha seasonal crop-mask file or public FASAL pixel API with crop class, sowing date and confidence.** FASAL's public description establishes forecasts and methods, not an open mask endpoint [14].
4. **Current plot-level crop, variety, sowing date, growth stage and harvest-readiness records.** A spectral classifier can estimate some of these fields, but it cannot establish farmer-declared crop identity for claims.
5. **A current numerical count of Soil Health Cards issued in Odisha.** The latest reviewed official release provides a national total, while the Odisha factsheet supplies only a percentage of target [17][42].
6. **Public, geocoded SHC laboratory observations with sample date, depth, method, pH, EC and plot linkage.** The parameter schema exists, but a sample-level Odisha export was not verified [17].
7. **A post-Yaas soil and irrigation-water salinity time series measured as EC, with pre-event baseline and recovery dates.** The available SAC products identify inundation and turbidity, not EC [10].
8. **A field-scale coastal saline-belt polygon with survey date, soil depth, salinity class and seasonal uncertainty.** The CSSRI page supplies only a 147,138 ha state total without those metadata [20].
9. **Current shallow water-table depth at farm or dense observation-well scale with a documented update API.** CGWB's block assessment and India-WRIS downloads do not by themselves establish plot conditions [24][9].
10. **Field-drain, canal and culvert geometry with invert level, blockage status, discharge capacity and responsible agency.** HydroRIVERS deliberately omits catchments below its global thresholds [31].
11. **A current machine-readable statewide list of flood-prone villages with village codes, hazard class, derivation date and revision history.** The OSDMA page confirms an atlas but not such a file [2].
12. **Event-specific, claim-grade observations:** timestamped maximum water depth, duration, crop condition before and after the event, geotagged farmer photographs, field-inspection record and provenance chain.
13. **A calibrated statewide flood-salinity model with published validation metrics.** The reviewed Baitarani case uses coarse cross-sections and does not report calibration or validation measures in its results [40].

These are not optional refinements if the system will issue plot-specific loss estimates or insurance evidence. They are the line between **risk screening** and **adjudication**.

## 5. HOW IT FEEDS THE ENGINE

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| SRTM, AW3D30, CartoDEM | Rank low-lying clusters and likely flow paths for earlier alerts | Identify depressions where standing water may persist | Supply a reproducible terrain-context map, not proof of plot water depth | Locate recurring lowland exposure and possible raised storage sites | Route runoff toward verified drains and identify relatively safer high ground |
| Surveyed micro-elevation | Decide which bund, pump, livestock or input-storage action is urgent | Determine where drainage or pumping is physically feasible | Record plot, bund and outlet elevations | Design plot leveling, raised seed stores and drainage improvements | Improve water harvesting without assuming every depression is hazardous |
| Bhuvan LULC and SIS-DP | Exclude built-up, forest and water pixels; identify agricultural landscape | Separate affected cropland from non-crop water and settlement | Provide land-cover context around the claimed plot | Measure conversion, fragmentation and recurring exposure | Target landscape-scale drain or shelter investments |
| Sentinel-2 NDVI/time series | Estimate whether a plot is bare, newly planted, vegetative or near harvest when clouds permit [6] | Compare pre-event and recovery vegetation trajectories | Add dated pre/post imagery with cloud metadata | Build local crop calendars and crop-rotation features | Detect recovery and avoid unnecessary blanket input advice |
| FASAL or partner crop mask | Confirm seasonal crop class and district context | Select crop-specific recovery rule set | Cross-check farmer-declared crop | Estimate seasonal exposure by crop | Target normal-season advisories to likely crop type |
| BHOOMI soil maps | Add infiltration, texture and baseline EC/pH priors | Select fields requiring faster inspection for waterlogging or salt stress | Establish regional soil context, not plot laboratory proof | Match crop and drainage planning to soil constraints | Use pH, texture, OC and fertility layers for ordinary agronomic advice [35] |
| SHC laboratory data | Identify already saline, acidic, alkaline or nutrient-constrained fields | Compare post-event sample with dated baseline | Attach signed laboratory values and sample provenance | Build field-specific amendment and nutrient plans | Reuse the same profile for routine fertility recommendations [17] |
| CSSRI coastal-saline extent | Raise the prior risk for coastal blocks | Prioritize EC sampling after surge exposure | Context only; the state total cannot prove plot salinity | Focus salt-management trials and resistant-crop planning | Identify where drainage and freshwater flushing capacity matter most |
| CGWB saline units and resource status | Flag blocks where groundwater may be unsuitable or scarce | Avoid advising pumping for flushing without water-quality checks | Add official block classification | Plan groundwater use and recharge conservatively | Identify areas where recharge measures may have value [24] |
| India-WRIS water levels | Detect shallow pre-storm water tables that reduce storage capacity | Track recession where observations are timely | Add nearby station observations with distance and timestamp | Model seasonal waterlogging and irrigation reliability | Time recharge, drainage and irrigation advice around observed conditions |
| HydroRIVERS and derived drainage density | Estimate basin-scale concentration and distance to major channels | Identify downstream connectivity and possible isolation | Supply hydrologic context | Prioritize larger drainage corridors | Guide watershed-scale water management [31] |
| Local drain and culvert survey | Trigger drain clearance, gate checks and pump positioning | Route dewatering and detect blocked outlets | Document infrastructure condition affecting loss | Prioritize maintenance and capital works | Improve everyday drainage and irrigation conveyance |
| OSDMA atlas and village hazard records | Pre-position village-level alerts and response resources | Prioritize reconnaissance and input support | Add official hazard-zone context | Rank villages for mitigation programs | Direct training and preparedness investment [2] |
| Sentinel-1 event inundation | Continue mapping through cloud during a cyclone | Delineate water extent and monitor persistence | Add timestamped event footprint, with clear uncertainty | Update historical flood-frequency features | Locate areas where restored drainage produced faster recession [10] |
| Field EC observations | Not normally available before landfall unless a baseline exists | Distinguish salt injury from waterlogging and sediment effects | Provide direct, dated salinity evidence | Track leaching and recurrence | Prevent unnecessary salt-treatment advice where EC is normal |
| Bhulekh and cadastral polygons | Route an alert to the correct plot and owner after consent | Join observations to the affected holding | Anchor evidence to plot number and RoR | Maintain a plot exposure history | Deliver location-specific normal-season recommendations [22] |

### Interaction rules for the prototype

The engine should keep **flood exposure**, **salinity likelihood**, and **observed damage** as separate outputs:

1. **Flood-screening score:** combine low relative elevation, terrain convergence, proximity to mapped channels, soil infiltration constraints, shallow pre-event water table, and historical/event inundation. Do not publish precise depth from a 30 m DEM alone.
2. **Salinity-screening score:** combine coastal or surge exposure, flood persistence, the CSSRI/CGWB saline prior, poor drainage, and any post-event spectral anomaly. Label the output "salinity inspection priority" until EC is measured.
3. **Observed flood state:** use timestamped Sentinel-1 extent plus field reports. Sentinel-1 supplied 10 m Yaas inundation evidence in Bhadrak and Kendrapara [10].
4. **Claim-support state:** require parcel match, date, image provenance, crop identity, and field evidence. The EO stack may support a claim packet, but it should not automatically decide causation or compensation.
5. **Local model path:** the Baitarani study shows that CartoDEM, discharge, HEC-GeoRAS and 1D HEC-RAS can produce flood-depth classes of up to 1 m, 1-3 m and more than 3 m [40]. Its coarse sections and missing reported validation metrics make it a prototype reference, not a statewide operational standard [40].

The risk score should drive a **short decision code** for SMS/IVR, while the backend preserves the full evidence record. IMD already supplies five-day district/block forecasts and AMFU advisories twice weekly, and government dissemination includes SMS during extreme events [46]. The geospatial engine's role is to decide **who receives which action first**, not to replace the official alert.

## 6. REAL-vs-FILLER

| Classification | Data or claim | Evidence-based judgment |
|---|---|---|
| REAL | SRTM 30 m, AW3D30 about 30 m and CartoDEM about 32 m | Free, named and documented elevation sources that can be ingested now [4][5][39] |
| REAL | Sentinel-2 10-20 m, five-day observations | Suitable for a reproducible NDVI/time-series pipeline, with cloud handling [6] |
| REAL | Bhuvan LULC and SIS-DP | Named epochs, scales and WMS/download paths exist [45] |
| REAL | BHOOMI soil attributes | The source explicitly lists pH, EC, OC, CaCO3, texture and six depths [35] |
| REAL | CGWB 2024 block groundwater assessment | Official, current block categories and resource totals exist [24] |
| REAL | Sentinel-1 Yaas inundation | Event-specific 10 m flood mapping is documented [10] |
| REAL, BUT COARSE | CSSRI 147,138 ha Odisha coastal-saline total | Useful as a prior only; no date, method or field polygon is supplied on the reviewed page [20] |
| REAL, BUT GATED | Bhulekh plot records | Large official record base and individual lookup exist, but bulk GIS access is not documented [22] |
| FILLER IF PRESENTED AS FACT | "Free JAXA AW3D is 12.5 m" | The verified free AW3D30 v4.1 product is about 30 m [5] |
| FILLER IF PRESENTED AS FACT | "Bhuvan provides a 10 m public CartoDEM" | The public CartoDEM documentation reviewed lists 1 arc-second, about 32 m [39] |
| FILLER | Old 5 km annual-cropland data for plot classification | The historical layer is downloadable but far too coarse for individual farms [45] |
| FILLER | Calling Yaas turbidity or inundation a salinity map | SAC reports flood extent and turbidity, not EC [10] |
| FILLER | Deriving field-drain condition from HydroRIVERS | Its global threshold omits small catchments and local drains [31] |
| FILLER | Treating a 1:250,000 soil polygon as a plot laboratory result | BHOOMI scale and property layers provide spatial priors, not proof of current plot chemistry [35] |
| FILLER | Automatic claim approval from NDVI decline | NDVI can show vegetation change but cannot alone establish ownership, crop declaration, water depth, salinity or causation |

The genuinely usable stack is therefore not a single "AI data lake." It is a layered evidence system: authoritative coarse priors, frequently updated satellite observations, and locally collected measurements for decisions that carry agronomic or financial consequences.

## 7. NOISE LOG

| Search target or discarded hit | Why it was discarded |
|---|---|
| SRC "consolidated crop-loss village" PDF | It is a list for **Kharif 2011 drought** and villages with at least 50% crop loss, not a current statewide flood-prone-village dataset [12] |
| Generic web statements describing CartoDEM as 10 m | They conflicted with Bhuvan's own CartoDEM table, which lists 1 arc-second, about 32 m [39] |
| Pages labeling AW3D as 12.5 m | They did not establish an official free JAXA 12.5 m DSM. The official free AW3D30 v4.1 catalog says about 30 m [5] |
| FASAL forecast bulletins used as crop masks | Forecast outputs establish crop assessment activity but do not document a public pixel-mask download or API [14] |
| Bhuvan annual cropland 5 km layer | Real but historical and too coarse for farm identification [45] |
| Yaas flood and turbidity maps described as salinity evidence | The products identify inundation and turbidity, so using them as EC measurements would overstate the evidence [10] |
| Unrelated groundwater yearbooks for Gujarat and Chhattisgarh | Wrong state; they do not answer Odisha water-table or recharge questions |
| Flood-susceptibility studies for Chennai, other Indian states and non-Indian deltas | Useful method examples, but not validated for Odisha soils, drainage, tides or cyclone history |
| Generic global flood models | Useful for broad screening but insufficient as evidence of Odisha village or plot hazard without local calibration |
| Kaggle, vendor and unsourced GIS bundles | Provenance, release date, processing method or license could not be tied to the responsible Indian agency |
| The 2022 Odisha SHC factsheet as a current card count | It gives a target-achievement band rather than the requested numerical total [42] |
| Cartosat-1 sensor resolution used as DEM resolution | Cartosat-1's 2.5 m imagery specification does not establish the grid or vertical accuracy of the public CartoDEM derivative [27] |

The discarded results reveal a recurring failure mode: technically related material is often promoted one level beyond what it measures. Sensor resolution becomes DEM resolution, inundation becomes salinity, program forecasts become downloadable masks, and an online plot register becomes a spatial API.

## 8. VERDICT: SYNTHESIS

### Overall grade: **PARTIAL**

| Decision layer | Grade | What can be done now | Blocking condition |
|---|---|---|---|
| Regional and village exposure screening | GO | Ingest SRTM/AW3D30/CartoDEM, Bhuvan LULC, Sentinel-1/2, CGWB blocks and major drainage to rank alert priority | Clearly disclose coarse resolution and model uncertainty |
| Farm-level advisory prioritization | PARTIAL | Join farmer-supplied coordinates and crop profile to terrain, crop-stage, soil and event-water features | Needs verified plot location, crop/phenology, local drain observations and consented farmer registry |
| Post-event flood monitoring | GO | Use Sentinel-1 for cloudy-weather inundation and persistence, Sentinel-2 when clouds clear, and field reports for depth | Satellite extent does not directly provide plot water depth or crop causation [10] |
| Salinity advisory | PARTIAL | Prioritize inspection using coastal exposure, saline-block priors, drainage and inundation persistence | Treatment advice should wait for baseline and post-event EC, sample depth and water-quality checks |
| Claim packet preparation | PARTIAL | Assemble dated imagery, alert history, parcel reference, farmer photos and inspection records | Automatic adjudication is GATED by parcel polygons, crop declaration, provenance and field evidence |
| Next-season planning | GO with review | Use recurring inundation, soil constraints, groundwater context and observed recovery to rank drainage, crop-calendar and storage interventions | Local agronomist validation and farmer feedback remain necessary |

### Cross-cutting synthesis

The principal sources differ along four decisive dimensions. **DEMs** have complete spatial coverage and simple file access, but low event freshness and weak sensitivity to microrelief. **Sentinel imagery** is much fresher and directly observes surface change, but clouds limit optical data and neither SAR inundation nor turbidity proves salinity. **Soil and groundwater programs** provide stronger causal context, yet their useful measurements are sparse, cyclical or difficult to join to plots. **Administrative sources** contain the ownership and local infrastructure facts needed for action, but they are the least available as bulk geospatial data.

That contrast determines the architecture. The prototype should use satellites and DEMs for broad prioritization, laboratory and IoT observations for state confirmation, and state records for identity and accountability. Reversing that order creates false precision: a visually detailed map can still be less decision-worthy than a dated EC reading or a verified culvert blockage.

The non-obvious tension is between **coverage and evidentiary strength**. SRTM or Sentinel can cover all coastal Odisha consistently, while a soil sample covers only one place. Yet the sample is the stronger basis for a salinity treatment or claim. The system should therefore maintain explicit evidence states: `screened`, `satellite-observed`, `field-reported`, `instrument-confirmed`, and `officially-verified`. SMS/IVR language should reflect the state rather than presenting every model result as fact.

### What requires collection

- Plot centroid and, where possible, walked boundary.
- Crop, variety, sowing date, growth stage and expected harvest date.
- Pre-event and post-event geotagged photographs.
- Water depth, start time and recession time from a marked local gauge.
- Soil and irrigation-water EC, pH, sample depth, method and timestamp.
- Bund crest, plot, drain invert and safe-storage elevations at priority sites.
- Drain, culvert, sluice, embankment and pump condition.
- Farmer consent and a controlled link to plot or RoR identifiers.

### What requires a partner

- **NRSC/MNCFC:** operational crop masks, higher-resolution hazard products and clarification of Bhuvan service licenses.
- **OSDMA/SRC and district administrations:** hazard-atlas data, current flood-prone village codes, event records and official damage assessments.
- **Odisha Agriculture Department and ICAR institutions:** SHC observations, crop calendars, salt-management rules and field validation.
- **CGWB and the state groundwater organization:** monitoring-well metadata, current depth series and water-quality observations.
- **Revenue Department/Bhulekh:** authorized parcel geometry and stable plot identifiers.
- **Water Resources, panchayats and irrigation bodies:** local drain, embankment, sluice and pump inventories.
- **Insurers and relief authorities:** evidence schema and acceptance rules for claim packets.

**Final decision:** build the prototype now, but label it a **screening and advisory-prioritization system**, not a plot-level flood-depth oracle, salinity detector or automatic claim adjudicator. The free stack is strong enough to demonstrate useful pre-event targeting, cloud-resilient event mapping and next-season risk memory. Production deployment is **PARTIAL** until Odisha partners expose parcel, crop, soil, groundwater, village-hazard and drainage records and the team collects field EC and micro-elevation data.

## References

1. *Bhuvan | NRSC Open EO Data Archive | NOEDA | Ortho | DEM | Elevation | AWiFS | LISSIII | HySI | TCHP | OHC | Free GIS Data | Download*. https://bhuvan-app3.nrsc.gov.in/data
2. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Flood Hazard Zonation Atlas-Odisha*. https://www.osdma.org/publication/flood-hazard-zonation-atlas-odisha/
3. *Impact of Tropical Cyclone Yaas on Coastal Regions of Odisha and West Bengal, India: An Assessment Using Sentinel Datasets - Das - 2025 - Geological Journal - Wiley Online Library*. https://onlinelibrary.wiley.com/doi/full/10.1002/gj.5153
4. *USGS EROS Archive - Digital Elevation - Shuttle Radar Topography Mission (SRTM) 1 Arc-Second Global | U.S. Geological Survey*. https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-1
5. *ALOS DSM: Global 30m v4.1  |  Earth Engine Data Catalog  |  Google for Developers*. https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V4_1
6. *Agriculture*. https://www.sentinel-hub.com/explore/industries-and-showcases/agriculture
7. *Sentinel Hub | Copernicus Data Space Ecosystem*. https://dataspace.copernicus.eu/analyse/apis/sentinel-hub
8. *Cyclone Yaas: A Curse to Coastal People of Odisha and West Bengal (India) | National Academy Science Letters | Springer Nature Link*. https://link.springer.com/article/10.1007/s40009-023-01251-w
9. *Water Resources Information System (WRIS) | Central Water Commission, Ministry of jal shakti, Department of Water Resources, River Development and Ganga Rejuvenation, GoI*. https://cwc.gov.in/en/water-resources-information-system-wris
10. *Assessment of surface inundation and changes in water turbidity associated with Cyclone Yaas*. https://vedas.sac.gov.in/static/pdf/Cyclone_Yaas_Report_LHD_1.pdf
11. *Dataset｜ALOS@EORC*. https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/aw3d30_e.htm
12. *Consolidated Village List Updated*. https://srcodisha.nic.in/odia/data/CONSOLIDATED_VILLAGE_LIST_UPDATED.pdf
13. *Land Use-Land Cover*. https://www.nrsc.gov.in/nrscnew/Apps_LULC_overview.php
14. *Mahalanobis National Crop Forecast Centre*. https://www.ncfc.gov.in/about_fasal.html
15. *ODISHA GEOPORTAL*. http://gisodisha.nic.in/
16. *AICRP (SWS) – ICAR-CSSRI :: Central Soil Salinity Research Institute*. https://cssri.res.in/aicrp-sws
17. [
	Press Note Details: Press Information Bureau
](https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=155036&lang=2&reg=3)
18. *Bhoomi Geoportal*. https://bhoomigeoportal-nbsslup.in/
19. *Bhuvan | Thematic Data dissemination | Free GIS Data | OGC Services | Clip and Ship *. https://bhuvan-app1.nrsc.gov.in/thematic
20. *Extent and distribution of salt affected soils in India – ICAR-CSSRI :: Central Soil Salinity Research Institute*. https://cssri.res.in/extent-and-distribution-of-salt-affected-soils-in-india/
21. [
	Press Release Page | Press Information Bureau
](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1988294)
22. [
	.:BHULEKH || ODISHA:.
](https://bhulekh.ori.nic.in/)
23. *cgwb.gov.in*. https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17357169591419696804file.pdf
24. *2024*. http://cdnbbsr.s3waas.gov.in/s3a70dc40477bc2adceef4d2c90f47eb82/uploads/2024/12/20241231588319401.pdf
25. *New elevation data triple estimates of global vulnerability to ...*. https://pmc.ncbi.nlm.nih.gov/articles/PMC6820795
26. *Uncertainties in the Shuttle Radar Topography Mission (SRTM ...*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5296860
27. [
   CARTOSAT-1
  ](https://www.isro.gov.in/CARTOSAT_1.html)
28. *HydroSHEDS*. https://www.hydrosheds.org/
29. *Sentinel-1 C-band Synthetic Aperture Radar | NASA Earthdata*. https://www.earthdata.nasa.gov/data/instruments/sentinel-1-c-sar
30. *ESA - Sentinel-1*. https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1
31. *HydroRIVERS*. https://www.hydrosheds.org/products/hydrorivers
32. *Soil Health Card Portal | National Informatics Centre | India*. https://www.nic.gov.in/project/soil-health-card-portal
33. *Sentinel-1 SAR GRD: C-band Synthetic Aperture Radar Ground Range Detected, log scaling  |  Earth Engine Data Catalog  |  Google for Developers*. https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD
34. *Annual Report*. https://icar-nbsslup.org.in/wp-content/uploads/2021/10/Annual_Report/16_17.pdf
35. *Nbss At A Glance Corrected Fnl Part 02*. https://icar-nbsslup.org.in/wp-content/uploads/2023/Publication/NBSS-AT-A-GLANCE_corrected_FNL_PART_02.pdf
36. *E-BOOK NBSS&LUP_Part 1_pdf*. https://icar-nbsslup.org.in/wp-content/uploads/2021/E-book/E_BOOK_NBSS&LUP_Part1.pdf
37. *ISRO's Geoportal | Gateway to Indian Earth Observation | Applications | Bhuvan | NRSC Open EO Data Archive | NOEDA | Ortho | DEM | Elevation | AWiFS | LISSIII | HySI | TCHP | OHC | Free GIS Data | Download*. http://bhuvan-app3.nrsc.gov.in/data/download/index.php
38. *India-WRIS*. https://indiawris.gov.in/wris/
39. *List of free satellite data products - Bhuvan Wiki*. https://bhuvan.nrsc.gov.in/wiki/index.php/List_of_free_satellite_data_products
40. *(PDF) Flood Hazard Assessment of Baitarani River Basin using One- Dimensional Hydrodynamic Model*. https://www.researchgate.net/publication/349686549_Flood_Hazard_Assessment_of_Baitarani_River_Basin_using_One-_Dimensional_Hydrodynamic_Model
41. [
	Press Release Page | Press Information Bureau
](http://pib.gov.in/PressReleasePage.aspx?PRID=2104403)
42. [
	Factsheet Details:Factsheet Details | PIB
](https://www.pib.gov.in/FactsheetDetails.aspx?Id=148602)
43. *CENTRAL GROUND WATER BOARD*. https://cgwb.gov.in/cgwbpnm/public/uploads/documents/1687863154711949309file.pdf
44. *Flood - Odisha State Disaster Management Authority*. https://www.osdma.org/preparedness/one-stop-risk-management-system/flood/
45. *Bhuvan Store*. https://bhuvan-app1.nrsc.gov.in/2dresources/bhuvanstore.php
46. *http://pib.gov.in/PressReleasePage.aspx?PRID=2223075*. http://pib.gov.in/PressReleasePage.aspx?PRID=2223075
