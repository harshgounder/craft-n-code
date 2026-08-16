# Odisha Real-Event Replays: A Validation-First Build Plan

## 1. EXECUTIVE SUMMARY

- **A viable five-event portfolio exists**: Phailin 2013, Titli 2018, Fani 2019, Yaas 2021, and the August 2022 Odisha floods collectively cover extreme wind, heavy rain, river flooding, coastal inundation, crop loss, and warning operations. Phailin, Titli, and Yaas have official IMD post-event track and observation reports; Fani and Phailin have unusually strong damage assessments. [2][3][1][17][18]

- **The track reconstruction is feasible, but a best track is not a complete hazard field**: IMD's Phailin table supplies 3-hourly position, intensity, central pressure, pressure drop, and storm grade. A Holland field can turn these into radial pressure and wind, but radius of maximum wind, boundary-layer reduction, translation asymmetry, terrain roughness, and inland decay must be estimated and calibrated to station observations. [2]

- **Observed data must correct, not merely decorate, the parametric model**: Phailin includes Gopalpur wind and pressure observations and 24-hour rainfall maxima; Titli provides several timestamped station winds and daily rain totals. These are useful calibration anchors, but they are not continuous public hourly series. [2][3]

- **Flood replay has a strong validation target but a weak access layer**: NRSC issued event-specific inundation maps, including a Sentinel-1A SAR map for 18 August 2022 at 1800 hours and a Fani inundation map for part of Puri. The public artifacts found are static PDFs, not analysis-ready flood rasters, so reliable pixel-level IoU requires obtaining or carefully georeferencing the underlying classification. [20]

- **Damage validation is strongest for Fani and Phailin**: Fani's DLNA reports 108,220 ha of damaged crops and INR 1,304.58 crore in production losses, with district rows for 11 districts. Phailin's RDNA reports INR 17,838.03 million of agriculture-sector loss, but names only Ganjam, Puri, and Khordha separately and groups the rest. [18][17]

- **Use project-set acceptance gates, not a fictitious universal standard**: no established cyclone or flood protocol called the "Ariadne discipline" was found. For this project, Ariadne should mean frozen inputs, no future-data leakage, versioned transformations, paired counterfactuals, and pre-registered gates. Recommended gates are district damage within +/-25%, event-total damage within +/-15%, SAR IoU at least 0.60, peak-stage error at most 0.30 m, peak-time error at most 3 hours, and exact reproduction of archived warning issue times.

- **Monte Carlo size should be convergence-driven**: start with 2,500 conditional realizations, then add batches of 500 until district mean loss changes by less than 2%, P90 loss by less than 5%, and key exceedance probabilities have a 95% half-width below 0.02. At worst-case probability 0.5, 2,401 independent samples give approximately +/-2 percentage-point precision; spatially correlated outputs may require more.

- **Counterfactual claims require behavior evidence, not assumed compliance**: model receipt, comprehension, feasibility, action, and action timing separately. Anticipatory-action evaluations show why early action is plausible, but some reported improvements cannot be causally attributed without a valid comparison group; one Red Cross review found 33% lower cost per beneficiary while explicitly warning that attribution was not possible. [6]

- **Overall verdict: PARTIAL**: a student team can build a credible warning, cyclone-hazard, flood-extent, and district-damage replay. Claims about plot-level loss avoided by SMS/IVR remain gated until the team obtains hourly station and gauge series, machine-readable flood extents, local crop calendars and fragility data, and Odisha farmer-response observations.

## 2. EVENT DATASET

### Reliability scale

- **A**: primary, event-specific government or intergovernmental record with stated observations or assessment method.
- **B**: authoritative event-specific record, but aggregated, static, incomplete, or difficult to machine-read.
- **C**: secondary or transferable research evidence requiring local calibration.
- **D**: generic portal, mirror, unsourced summary, or result with no usable event payload.

| Event | What exists | Named source, URL, and date | Format | Resolution | Access | Reliability |
|---|---|---|---|---|---|---|
| **Phailin, 8-14 Oct 2013** | Best track; landfall; station wind and pressure; 24-hour rain; observed surge; forecast verification; statewide affected crop area. Separate RDNA gives affected area and agriculture losses. | IMD, *Very Severe Cyclonic Storm Phailin*, Oct 2013: <https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_38a1d4_phailin.pdf>. OSDMA/ADB/World Bank, *Rapid Damage and Needs Assessment*, Dec 2013: <https://www.osdma.org/wp-content/uploads/2019/09/Odisha-Phailin.pdf>. | PDF tables, text, figures | Best track 3-hourly; station snapshots and 24-hour rainfall; district damage for 3 named districts plus "other" | Public download | **A** for IMD observations; **B** for district damage granularity |
| **Titli, 8-13 Oct 2018** | Best track, landfall, peak intensity, station winds, daily rainfall, tide observations, warnings, and forecast errors. No authoritative district crop-loss table was located. | IMD, *Very Severe Cyclonic Storm Titli*, Jan 2019: <https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_dd893c_Titli.pdf>. | 50-page PDF with tables and figures [3] | Track table at synoptic timestamps; sparse station observations; 24-hour rain totals | Public download | **A** for cyclone reconstruction; **D** for crop-loss validation until a district assessment is obtained |
| **Fani, 3 May 2019 landfall** | Warning chronology; SMS, siren, and FM dissemination counts; affected villages and districts; crop area, crop type, district loss, valuation, and recovery needs. NRSC static inundation map covers part of Puri. | OSDMA, *Cyclone Fani 2019 Odisha DLNA*: <https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf>. NRSC/SAC, Fani inundation map, issued 7 May 2019: <https://bhuvan-app1.nrsc.gov.in/disaster/usrtasks/documents/cyclone/Odisha_Statemap_plieades_sc1_Post_new_11.pdf>. | DLNA PDF tables; static flood-map PDF | District and crop-category damage; map covers only part of Puri; no public hourly station series located | Public download | **A** for aggregate crop losses and warning operations; **B** for inundation; **D** for continuous station forcing |
| **Yaas, 23-28 May 2021** | 3/6-hourly best track, landfall, central pressure, station wind, 24-hour rain, estimated surge, warnings, and forecast verification. The IMD summary reports West Bengal crop damage but no Odisha agriculture figure. | IMD, *Very Severe Cyclonic Storm Yaas*, June 2021: <https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_77afd4_Preliminary%20Report%20YAAS%20during%2023-27%20May%202021.pdf>. | PDF tables and figures | Best track 3/6-hourly; station snapshots; 24-hour rainfall | Public download | **A** for cyclone and warning replay; **D** for Odisha damage calibration |
| **Odisha floods, 16-21 Aug 2022** | Dated NRSC inundation maps; a Sentinel-1A SAR extent for 18 Aug at 1800 hours; state DoWR flood bulletin for 20 Aug; river and reservoir status. | NRSC map, 18 Aug 2022: <https://www.nrsc.gov.in/nrscnew/assets/pdf/maps_dms/Floodmap_OD_18Aug2022.pdf>. NRSC map, 21 Aug 2022: <https://www.nrsc.gov.in/nrscnew/assets/pdf/maps_dms/Floodmap_OD_21Aug2022OD.pdf>. Odisha DoWR bulletin, 20 Aug 2022: <https://dowr.odisha.gov.in/sites/default/files/2022-08/DoWR%20Flood%20Bulletin%2020_08_2022.pdf>. | Static map PDFs and bulletin PDF | Event snapshots at specific acquisition times; point river/reservoir status rather than a downloadable historical hydrograph | Public download | **B** for extent and operational chronology; **D** for raw raster, full hourly gauge, and crop-loss validation |

Phailin illustrates why each event needs multiple source types. The IMD report supplies 3-hourly hazard parameters and records a 2-2.5 m surge with 500 m to 1 km of coastal inundation; the RDNA supplies crop and monetary outcomes. Neither source alone can validate the full hazard-to-loss chain. [2][17]

**Decision:** use all five events, but designate Fani and Phailin as **damage-calibration events**, Titli and Yaas as **wind and warning validation events**, and August 2022 as the **flood-extent validation event**.

## 3. COVERAGE TABLE

| Source family | Useful hits | Useful evidence | Noise or missing material | Coverage judgment |
|---|---:|---|---|---|
| IMD/RSMC post-storm reports | 3 strong reports: Phailin, Titli, Yaas | Track, pressure, wind, rain, surge, warnings, and forecast errors | PDFs rather than tidy time-series files; no continuous public hourly station series found | **A** for storm chronology; **B** for gridded reconstruction |
| OSDMA, ADB, and World Bank assessments | 2: Fani DLNA, Phailin RDNA | Crop area, losses, valuation, recovery, and some district rows | Administrative aggregation and inconsistent district detail; not plot-level ground truth | **A/B** |
| IMD gridded rainfall | 1 national product | Daily rainfall in NetCDF at 0.25 x 0.25 degree for long-period analysis [14] | Daily and coarse for flash-flood timing; station data portal access may be required for sub-daily replay | **B** |
| Odisha DoWR and CWC hydrology | 1 event bulletin plus operational portals | River/reservoir operational state and warning context | No downloadable complete historical hourly hydrograph was established | **C** |
| NRSC/NDEM/Bhuvan satellite disaster maps | At least 4 relevant static maps: Fani and three August 2022 dates | Independent flood-location evidence at known acquisition times | Mostly PDF maps; raw classified raster, confidence mask, and complete metadata were not located | **B** |
| Copernicus/Sentinel open Earth observation | DEM GLO-30/GLO-90 and Sentinel-1 GRD families | Terrain and SAR inputs for independent reprocessing | DEM is a surface model that needs drainage conditioning; historical sensor coverage differs by event | **B** |
| Rice fragility research | Stage-duration experiments and agricultural damage-function studies | Demonstrates that tillering, booting, and flowering cannot share one flood-loss curve; experiments include 0, 2, 4, 6, 8, and 10 day submergence treatments [9] | Not Odisha varieties, soils, salinity, or management | **C** |
| WFP/FAO/Red Cross anticipatory-action evidence | Review plus Bangladesh cash evaluation | Counterfactual designs, early-action mechanisms, and behavior outcomes | Cash-transfer effects are not SMS/IVR compliance probabilities and are not Odisha-specific | **C** |
| Modeling tools and documentation | HEC-RAS, LISFLOOD-FP, SFINCS, Delft-FEWS, CLIMADA/PaHM | Enough to build cyclone and flood prototypes | Tool availability does not solve missing calibration data | **B** |

The coverage is asymmetric: hazard chronology is strong, but farm behavior and plot damage are weak. This means the first replay should test whether the engine receives the correct alert and generates timely advice, not claim that it has already proved a precise number of rupees saved.

**Decision:** the source base supports an auditable replay benchmark, but not an end-to-end causal impact claim without new local data.

## 4. WHAT IS MISSING

### Event-specific gaps

| Event | Exact unresolved gap | Consequence |
|---|---|---|
| **Phailin** | No public machine-readable hourly wind, pressure, and rainfall series was located. The RDNA names Ganjam, Puri, and Khordha separately, but combines Gajapati, Balasore, Mayurbhanj, Nayagarh, Cuttack, Jajpur, Kendrapara, Jagatsinghpur, and Bhadrak as "other districts." [17] | Station residuals cannot be robustly estimated at every hour; district validation outside the three named districts is impossible from this RDNA alone. |
| **Titli** | The IMD report provides spot winds and daily rainfall, not an open continuous hourly series. Searches did not locate an official district crop-loss table for Gajapati or Ganjam. | Good wind/lead-time test, weak damage test. Absence of a table must not be encoded as zero loss. |
| **Fani** | No complete public hourly station series was found. The extracted DLNA district table has rows for 11 districts, while the affected-district list also includes Mayurbhanj, Keonjhar, and Ganjam, for which the extracted table exposes no row. [18] The public Puri inundation artifact is a static partial map. | Strong aggregate calibration, but incomplete district and spatial validation. The three unexposed rows are "unconfirmed," not zero. |
| **Yaas** | No Odisha crop-loss figure appears in the IMD impact summary; the report only gives about 2.21 lakh ha for West Bengal. [1] Thus Balasore, Bhadrak, Kendrapara, and Jagatsinghpur lack verified agriculture figures in the identified primary source. | Use for cyclone, surge-warning, and lead-time validation, not Odisha crop-loss calibration. |
| **August 2022 flood** | Event map PDFs exist, but no raw classified inundation raster, confidence layer, complete hourly gauge hydrograph, or authoritative district crop-loss table was located. | A demonstrator can georeference maps, but publication-quality IoU and depth validation remain gated. |

### Cross-event gaps

1. **Radius of maximum wind and Holland B** are not consistently available in the IMD tables. Estimating both from intensity and climatology introduces structural uncertainty that must be sampled, not hidden.
2. **Surge observations are inconsistent**. Phailin has post-survey observed surge; Titli has a few reported tide heights; Yaas provides estimated inundation ranges. These are not equivalent calibration targets. [2][3][1]
3. **Crop calendars and varieties are missing at plot level**. A flood during tillering cannot use the same loss function as flowering or maturity.
4. **Administrative loss is not physical damage ground truth**. Fani's DLNA relies on departmental data, field corroboration, secondary data, and assessment judgment, and even warns that numbers may differ across chapters. [18]
5. **No Odisha farmer-response dataset was found** for SMS receipt, IVR listening, trust, labor availability, early harvest, drainage, input protection, or evacuation of livestock.
6. **Recovery outcomes are sparse**. The assessments recommend recovery actions, but do not supply farm-level longitudinal outcomes showing which advice restored yields fastest.

**Decision:** create a formal data-acquisition request for IMD station data, DoWR/CWC historical gauges, NRSC flood rasters, SRC district damage memoranda, and Agriculture Department crop calendars before presenting calibrated avoided-loss percentages.

## 5. HOW IT FEEDS THE REPLAY SIMULATION

### 5.1 Two clocks prevent future-data leakage

Maintain two synchronized timelines:

1. **Truth reconstruction** contains all post-event observations and is used to reconstruct what happened.
2. **Information-set replay** exposes the advisory engine only to alerts and observations available at that historical instant.

For example, Fani's cyclone watch was issued at 1:00 PM on 30 April and landfall occurred about 8:30 AM on 3 May. The engine must not see the final track or damage assessment while generating a 30 April advisory. [18] Similarly, Yaas's first low-pressure bulletin was issued about 90 hours before landfall. [1]

Store every input with `event_time`, `issue_time`, `ingest_time`, source hash, units, coordinate reference system, and quality flag. Replaying from this manifest is the practical Ariadne discipline.

### 5.2 Cyclone pressure and wind reconstruction

At each best-track time, interpolate storm-center latitude, longitude, central pressure, and maximum sustained wind. Use the Holland pressure profile:

`p(r) = pc + (pn - pc) * exp[-(Rmax/r)^B]`

Derive gradient wind from the pressure gradient, then convert it to 10 m surface wind. Add storm-translation asymmetry, surface-drag and roughness reduction, topographic exposure, and post-landfall decay. Keep `Rmax`, `B`, background pressure, reduction factor, and inland-decay rate as explicit uncertain parameters.

For each station and timestamp, compute residual `observed - modeled`. Krige or conditionally simulate the residual field and add it back to the Holland field. This preserves large-scale cyclone physics while making the reconstruction honor real observations. Do not apply Holland to rainfall: rain should be reconstructed separately from gauges, IMD grids, radar or satellite precipitation, using log-rainfall interpolation and terrain/cyclone-relative covariates.

Phailin is the strongest calibration event because its 3-hourly track, Gopalpur wind and pressure, 38 cm maximum 24-hour rainfall, and observed surge all coexist in one report. [2]

### 5.3 Monte Carlo with observed uncertainty

Build residual distributions from observations, stratified by coastal/inland location, storm quadrant, land/sea, and lead time. Preserve cross-variable dependence: a deeper pressure deficit, larger wind, and smaller Rmax cannot be sampled independently without producing physically implausible storms.

For a grid residual vector, fit a hazard-specific covariance or variogram and draw `epsilon = Lz`, where `LL'` is the covariance matrix and `z` is standard normal. Condition each realization on station observations. Jayaram-Baker is useful as a conceptual pattern for spatially correlated residuals, but it was developed from earthquake ground motions, not cyclone wind or rain; its correlation lengths must not be copied into Odisha. [8]

Use this convergence protocol:

- Run **500 pilot scenarios** to identify dominant parameters and failures.
- Run **2,500 production scenarios** as the first target.
- Add **500-scenario batches** until district mean loss changes by less than **2%**, P90 loss by less than **5%**, and critical-action exceedance probabilities have 95% confidence half-width below **0.02**.
- Extend toward **5,000-10,000** if tails or spatial dependence remain unstable.

Report the seed, sampled parameters, convergence plots, and effective rather than nominal sample size.

### 5.4 Rainfall-runoff and inundation

1. Correct gauge and gridded rainfall for timing, units, missingness, and bias.
2. Delineate catchments from a conditioned DEM. Burn known channels, preserve embankments and roads, hydro-flatten water surfaces, and remove spurious sinks.
3. Transform rainfall to runoff with HEC-HMS, a calibrated unit-hydrograph model, or a distributed alternative.
4. Route flow and inundation using HEC-RAS 2D, LISFLOOD-FP, or SFINCS. Add downstream tide/surge boundary conditions for coastal basins.
5. Export maximum depth, duration, velocity, arrival time, and recession time at plot resolution.
6. Compare the simulated wet/dry raster at the exact SAR acquisition time, not at the simulated peak unless they coincide.

For binary flood validation:

`IoU = TP / (TP + FP + FN)`

Also report probability of detection, false-alarm ratio, and area bias. Mask permanent water and SAR layover/shadow; test sensitivity to the classification threshold. The 18 August 2022 map explicitly identifies Sentinel-1A SAR and its 1800-hour acquisition, providing the temporal anchor required for a fair comparison. [20]

### 5.5 Plot crop damage and administrative reconciliation

Each plot record needs crop, variety, sowing or transplant date, phenological stage, expected yield/value, irrigation/drainage, and protective actions. Intersect it with maximum wind, flood depth, flood duration, salinity, and water arrival time.

Use separate stage-specific fragility functions, such as beta or logistic curves, for:

- wind lodging and shattering;
- freshwater depth and duration;
- saline inundation;
- waterlogging and root damage;
- harvest delay and quality loss;
- perennial-tree breakage and multi-year lost production.

Rice experiments that separately flood tillering, booting, and flowering stages for 0-10 days demonstrate why one generic "paddy flood" percentage is invalid. [9] Calibrate transferable curves to Odisha using crop-cutting experiments, insurance claims, or matched field surveys.

Aggregate simulated plot loss to the same definition used by the assessment. Fani's assessment largely counts damage above a 33% crop-damage threshold and values it using replanting cost, so a model of any biophysical yield reduction is not directly comparable until it applies the same threshold and valuation basis. [18]

### 5.6 Proposed Ariadne acceptance gates

These are **project acceptance criteria**, not universal scientific standards.

| Layer | Metric | Proposed pass gate | Failure interpretation |
|---|---|---:|---|
| Input integrity | Timestamp/source/hash completeness | **100%** | Replay is not auditable |
| Wind | Station 10 m wind MAE | **<=5 m/s or <=15%**, whichever is looser | Refit Rmax, B, reduction, or spatial residuals |
| Pressure | Station pressure MAE | **<=5 hPa** | Pressure profile or timing is wrong |
| Rain | 24-hour station total median absolute percentage error | **<=25%** | Rainfall interpolation is not event-faithful |
| River | Peak-stage error | **<=0.30 m** | Runoff, roughness, structure, or boundary error |
| River | Peak-time error | **<=3 h** | Advisory timing based on flood arrival is unreliable |
| Flood extent | SAR IoU | **>=0.60** | Do not use depth/duration for loss claims |
| Flood extent | Detection / false alarm | **POD >=0.70; FAR <=0.30** | Extent may look good only because of area imbalance |
| Damage | Event-total crop loss | **within +/-15%** | Fragility or exposure scale is wrong |
| Damage | Named district crop loss | **within +/-25%** | District-specific exposure or stage is wrong |
| Warning | Archived issue time and lead time | **exact timestamp; lead-time error <= one bulletin interval** | Future leakage or archive mismatch |
| Monte Carlo | Stability | **mean <2% change; P90 <5% change** | Increase scenarios or revise sampling |

IMD's own event verification shows that tight timing checks are realistic: Phailin landfall-time errors were 1-3 hours, Titli's first regional landfall information was issued about 43 hours in advance, and Yaas's 12-24 hour landfall-point errors were 7.8 km. [2][3][1]

### 5.7 Agent behavior and the counterfactual engine

Represent each farmer with channel reachability, literacy/language, crop stage, plot size, labor, machinery, cash, trust, prior warning experience, and action constraints. For each advisory, simulate five separate probabilities:

`receipt -> comprehension -> belief -> feasibility -> action before deadline`

Actions include early harvest, opening drainage, moving seed and inputs, securing trellises, moving livestock, switching irrigation off, and delaying replanting until salinity or water recedes. An IVR call and an SMS should have different receipt and comprehension models.

Run paired counterfactuals on the **same hazard realization and agent random seed**:

- **Observed/base behavior**: estimated actions without the system.
- **T+0**: advice sent at the first eligible IMD trigger.
- **T+12**: identical advice sent 12 hours later.
- **No receipt**, **receipt but no action**, and **full feasible compliance** sensitivity bounds.

For scenario `s`, avoided loss is:

`Delta L_s = L_s(base behavior) - L_s(advised behavior)`

Average paired differences and report uncertainty. Never multiply maximum physical protection by the total farmer population and call it impact.

Published anticipatory-action studies are mechanism evidence, not Odisha calibration. The WFP Bangladesh evaluation examines a transfer delivered five days before the flood peak [13]; the Red Cross review's 33% lower cost per beneficiary could not be causally attributed without better severity and comparison data. [6] A credible Odisha evaluation should therefore use randomized rollout, stepped-wedge assignment, or matched/doubly robust comparison of eligible farms, with pre-event registration and post-event crop measurements.

### 5.8 Tools a student team can run

| Tool | Role | Status and practical fit | Recommendation |
|---|---|---|---|
| **NOAA PaHM or a small Python Holland implementation** | Parametric cyclone wind/pressure | Lightweight and fast enough for thousands of realizations | **Use** for the first wind-field layer; validate against IMD stations |
| **CLIMADA Python** | Tropical-cyclone hazard, exposure, and impact framework | Reproducible Python workflow, but its default vulnerability functions are not Odisha crop curves | **Use selectively** for orchestration and comparison |
| **HEC-RAS 2D** | River hydraulics, rain-on-grid, inundation | Publicly downloadable and widely documented; not established here as open-source software | **Use** if the team prefers a GUI and has cross sections/structures |
| **LISFLOOD-FP** | Efficient 2D floodplain inundation | Designed for complex-topography floodplains [12] | **Use** if build and preprocessing skills are available |
| **SFINCS** | Coastal, riverine, pluvial, and wave-driven flooding | Explicitly described as a fast open-source flood model | **Best open-source all-hazard candidate** for a compact student stack |
| **Delft-FEWS** | Data ingestion, workflow, and warning orchestration | FEWS is an operational platform, not the hydraulic solver itself | **Defer** until the numerical replay works |
| **Python geospatial stack** | Preprocessing, Monte Carlo, scoring | `xarray`, `pandas`, `numpy`, `scipy`, `rasterio`, `geopandas`, `shapely`, `pyproj`, and `PyKrige` | **Use** as the reproducible glue layer |

**Decision:** the minimum viable stack is Python + PaHM/Holland + HEC-RAS 2D or SFINCS + raster scoring. Data acquisition, not software availability, is the main bottleneck.

## 6. REAL-vs-FILLER

| Classification | Component | Evidence-based reason |
|---|---|---|
| **REAL - use now** | IMD best-track tables | They contain event time, position, pressure, wind, pressure drop, and grade at synoptic intervals. [2][1] |
| **REAL - use now** | Timestamped station observations | They constrain model residuals and expose local bias, even when sparse. [3][2] |
| **REAL - use now** | Archived warning and landfall timing | Directly tests whether the advisory engine had the right lead time without using future information. [18][1] |
| **REAL - use now** | Fani and Phailin administrative losses | They provide defensible event and district aggregation targets, with documented limitations. [18][17] |
| **REAL - conditional** | NRSC static inundation maps | Valid independent observation, but reliable IoU needs raster extraction and acquisition-time alignment. [20] |
| **REAL - conditional** | IMD 0.25-degree daily rainfall | Real observation-derived forcing, but too coarse in time and space to stand alone for local flash-flood depth. [14] |
| **REAL - conditional** | Stage-specific rice experiments | Valid evidence that stage and duration matter, but coefficients need Odisha calibration. [9] |
| **REAL - conditional** | WFP/FAO behavior effects | Useful for model structure and sensitivity ranges, not direct Odisha SMS/IVR probabilities. [13][6] |
| **FILLER** | A smooth animated cyclone derived only from track points | Visual plausibility does not validate station wind, rain, surge, or loss. |
| **FILLER** | Independent random noise at each grid cell | It destroys spatially coherent hazard footprints and produces unrealistic district diversification. |
| **FILLER** | Copying district loss equally to every plot | Administrative totals do not reveal within-district crop stage, depth, duration, or behavior. |
| **FILLER** | Calling a static PDF map a 10 m truth raster | Scale, classification confidence, permanent-water masks, and georeferencing error remain unknown. |
| **FILLER** | Assuming every delivered SMS causes action | Delivery is not comprehension, feasibility, or compliance. |
| **FILLER** | Reporting one "loss avoided" number | Without paired hazards, response uncertainty, and a counterfactual design, it is scenario arithmetic rather than impact evidence. |

**Decision:** every dashboard layer should expose its source, observed/modelled status, spatial and temporal resolution, and uncertainty. Remove any layer that cannot affect a validation metric or advisory decision.

## 7. NOISE LOG

| Searched and discarded | Why discarded |
|---|---|
| Fitness and bodybuilding "V-taper" pages returned by a malformed Fani/VSCS query | Text-search collision with "V taper"; no cyclone relevance |
| Bihar FMIS inundation pages | Valid flood products for the wrong state |
| Scribd copies of the Odisha flood atlas and Yaas assessments | Mirrors with uncertain completeness when an official source is required |
| Wikipedia event summaries | Useful only for discovery; replaced by IMD, OSDMA, NRSC, and DoWR sources |
| Farmonaut and general agritech cyclone articles | Secondary summaries with unsupported or future-looking restoration figures |
| ResearchGate mirrors | Used only to identify titles; not accepted as the authoritative downloadable record |
| Generic NRSC/Bhuvan portal pages | Demonstrate that a service exists but do not prove that an event raster is downloadable |
| Searches for an established "Ariadne discipline" in hazard validation | Returned unrelated software, energy, maze, and AI frameworks; no recognized cyclone/flood standard was found |
| Generic HEC-RAS validation manuals without event metrics | Useful documentation, but not an Odisha hindcast or evidence for a universal IoU threshold |
| Cyclone Dana results returned during Yaas searches | Wrong event; excluded despite Odisha relevance |
| Jayaram-Baker code treated as a wind/rain model | The framework is for earthquake ground-motion correlation; retained only as a structural analogy [8] |

This log matters because replay credibility depends as much on excluding attractive but non-comparable material as on collecting useful data.

**Decision:** retain the noise log in the repository alongside the source manifest so future team members do not reintroduce rejected evidence.

## 8. VERDICT

# PARTIAL

### GO now

1. **Warning replay**: reproduce archived issue times, alert content, landfall lead time, SMS/IVR routing, and advice-generation latency.
2. **Cyclone hazard replay**: construct pressure and wind from the IMD track, calibrate to observed stations, and quantify uncertainty.
3. **Fani and Phailin damage reconciliation**: aggregate simulated plot losses to the same district and event definitions used by the DLNA/RDNA.
4. **August 2022 flood demonstrator**: reconstruct rainfall-runoff and compare a time-matched wet/dry result with the NRSC map.
5. **Paired what-if experiments**: compare no advisory, T+0, and T+12 under identical hazards, while clearly labelling behavior parameters as assumed ranges.

### GATED

1. **Publication-quality flood IoU** is gated on an analysis-ready SAR classification or documented georeferencing and uncertainty procedure.
2. **Hourly hazard calibration** is gated on IMD station and DoWR/CWC gauge time series.
3. **Plot-level crop-loss accuracy** is gated on local crop calendars, varieties, field elevations, drainage, salinity, and stage-specific Odisha fragility data.
4. **Causal avoided-loss claims** are gated on farmer-level receipt, comprehension, action, and outcome data with a valid comparison design.
5. **Operational surge-depth claims** are gated on coastal topography, bathymetry, tide boundaries, embankments, and observed water levels.

### Six-build-sequence recommendation

1. Freeze the five event manifests and warning timelines.
2. Build deterministic cyclone fields and station residual diagnostics.
3. Build the August 2022 flood model and map-overlap scorer.
4. Add crop-stage exposure and calibrate only to Fani/Phailin aggregate losses.
5. Add the receipt-to-action agent model and paired T+0/T+12 runs.
6. Add Monte Carlo only after deterministic failures are understood; then enforce the convergence and Ariadne gates.

The honest competition claim is: **"We built an auditable replay harness that reproduces historical warning conditions and tests whether advice would have been timely and physically relevant."** Do not claim: **"We proved the system would have saved X% of Odisha crop losses"** until the gated data are obtained.

## SYNTHESIS

| Layer | Mechanism | Scope | Evidence base | Main trade-off | Decision horizon |
|---|---|---|---|---|---|
| Parametric cyclone | Best track -> Holland pressure/wind -> station residual correction | Statewide wind and pressure | Strong IMD chronology, sparse local observations | Fast and interpretable, but structurally sensitive to Rmax and B | Hours to days before landfall |
| Hydrologic/hydraulic flood | Rainfall -> runoff -> routed depth/duration on conditioned terrain | Catchment and floodplain | Moderate: dated maps and bulletins, incomplete raw series | Spatial realism costs data and computation | Hours to several days |
| Crop fragility | Hazard x crop stage x duration x value | Plot to district | Strong aggregate Fani/Phailin loss, weak local curves | Plot detail can create false precision | Immediate damage through multi-year perennial loss |
| Farmer agent | Receipt -> comprehension -> feasibility -> action | Household and delivery channel | Transferable anticipatory-action evidence, no Odisha response panel | Necessary for avoided loss, but behavior dominates uncertainty | Minutes to days before impact |
| Warning replay | Archived information set -> advisory -> delivery | Entire advisory system | Strong IMD/OSDMA timestamps | Most directly testable, but does not alone prove physical loss reduction | Real time |
| Counterfactual engine | Paired identical hazards with different advice/action paths | Scenario and population | Methodologically sound if behavior is measured | Powerful but easy to overclaim | Pre-event action through recovery |

The non-obvious tension is that the most visually impressive layer, a high-resolution flood animation, is not the most defensible first result. Warning timing and district reconciliation have stronger evidence and clearer pass/fail criteria. Conversely, the layer closest to the problem's objective, avoided crop loss, has the weakest Odisha-specific causal data.

The correct architecture therefore separates **physical replay**, **information replay**, and **behavior counterfactuals**. It allows the first two to pass while the third remains uncertain, rather than tuning farmer compliance until the model reproduces a desired benefit. That separation is what turns the project from a synthetic demo into a research-grade validation harness.

## References

1. *Cyclone Warning Division - rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_77afd4_Preliminary%20Report%20YAAS%20during%2023-27%20May%202021.pdf
2. *Very Severe Cyclonic Storm, PHAILIN over the Bay of Bengal ...*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_38a1d4_phailin.pdf
3. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_dd893c_Titli.pdf
4. *HEC-RAS - Hydrologic Engineering Center - U.S. Army Hydrologic Engineering Center (.mil) https://www.hec.usace.army.mil › software › hec-ras*. https://www.hec.usace.army.mil/software/hec-ras
5. *Development of flood damage functions for agricultural ...*. https://www.sciencedirect.com/science/article/pii/S2214581821001014
6. *The evidence base on Anticipatory Action*. https://www.anticipation-hub.org/Documents/Reports/WFP-The_evidence_base_on_Anticipatory_Action.pdf
7. *The Two-Parameter Holland Pressure Model for Tropical Cyclones*. https://www.mdpi.com/2077-1312/12/1/92
8. *Correlation model for spatially distributed ground-motion ...*. https://www.jackwbaker.com/Publications/Jayaram_Baker_(2009)_spatial_correlation,_EESD.pdf
9. *Effects of flooding duration in different growth stages on ...*. https://www.aeeisp.com/nygcxb/en/article/doi/10.11975/j.issn.1002-6819.2019.03.016
10. *Copernicus DEM - Global and European Digital Elevation Model*. https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM
11. *The Dataset's Variables and Attributes*. https://erddap.aoml.noaa.gov/hdb/erddap/info/IBTRACS_last3years/index.html
12. *LISFLOOD-FP | School of Geographical Sciences | University of ...*. https://www.bristol.ac.uk/geography/research/hydrology/models/lisflood
13. *Importance of Being Early? Anticipatory Cash Transfers for ...*. https://academic.oup.com/wber/advance-article/doi/10.1093/wber/lhag016/8675570
14. *Yearly Gridded Rainfall (0.25 x 0.25) data NetCDF File*. https://www.imdpune.gov.in/cmpg/Griddata/Rainfall_25_NetCDF.html
15. *Sentinel-1 GRD*. https://docs.sentinel-hub.com/api/latest/data/sentinel-1-grd
16. *SFINCS - new fast numerical model | Deltares*. https://www.deltares.nl/en/software-and-data/products/sfincs
17. *Odisha Phailin report.indd*. https://www.osdma.org/wp-content/uploads/2019/09/Odisha-Phailin.pdf
18. *untitled*. https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
19. *Conditioning by Kriging - Geostatistics Lessons*. https://geostatisticslessons.com/lessons/conditioningbykriging
20. *Heavy Rain Inundated Areas in Part of Odisha State*. https://www.nrsc.gov.in/nrscnew/assets/pdf/maps_dms/Floodmap_OD_18Aug2022.pdf
21. *µ*. https://bhuvan-app1.nrsc.gov.in/disaster/usrtasks/documents/cyclone/Odisha_Statemap_plieades_sc1_Post_new_11.pdf
22. *Heavy Rain Inundated Areas in Part of Odisha State*. https://www.nrsc.gov.in/nrscnew/assets/pdf/maps_dms/Floodmap_OD_21Aug2022OD.pdf
