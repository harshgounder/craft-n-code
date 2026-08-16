# Replaying Odisha Cyclones and Floods From Real Data

Access audit date: **2026-08-16**. Reliability grades: **A** = official, machine-readable primary data; **B** = official event report or assessment with extractable tables; **C** = scholarly/secondary evidence or incomplete official coverage; **D** = discovery lead, generic product, or unsuitable for quantitative replay.

## 1. EXECUTIVE SUMMARY

- **Track replay is a GO**: NOAA IBTrACS v4.01 provides direct North Indian Ocean downloads in CSV, netCDF-4, and Shapefile, with UTC position, wind, pressure, agency fields, and mostly 6-hour observations, including some 3-hour or event observations. Use it as the common track schema for all seven cyclones, then retain IMD and JTWC values as separate agency realizations rather than averaging incompatible wind conventions. [14][15]
- **IMD reports add finer event timing**: the Fani, Yaas, Amphan, and Dana reports contain 3-hourly best-track tables, while the Phailin report documents hourly coastal observations, 30-minute satellite imagery, and 10-minute radar imagery. These PDFs are replay-ready for track, intensity, rainfall windows, and warning timing, but they are not raw AWS files. [13][10][20][21]
- **Open hourly station data are possible but not pre-packaged by event**: NOAA ISD provides hourly and synoptic wind, gust, station pressure, sea-level pressure, and precipitation in downloadable ASCII/CSV-style files. Station records can contain long breaks, so the team must perform a station-by-station inventory before claiming complete event coverage. [7]
- **IMD station data are authoritative but gated**: IMD's Data Supply Portal accepts station, period, and hourly/daily requests, may charge tariffs, requires a signed undertaking for some requests, and restricts redistribution. This is a request-and-license workflow, not an open event archive. [9]
- **Surge evidence is heterogeneous**: the 1999 study reports about **7 m** surge and seawater penetration up to **35 km** inland, whereas Fani's **1.5 m**, Yaas's **1-4 m**, and Dana's **1-2 m** values are reported as estimates or realized maxima, not downloadable tide-gauge residual series. These values can calibrate peak coastal impact, but not an hourly surge hydrograph. [12][13][10][11]
- **Damage validation is event-dependent**: Fani's DLNA provides district crop areas and losses; Amphan's final memorandum provides district crop and livestock tables; Phailin has strong state totals and district livestock exposure. Equivalent official district crop/livestock tables were not found for 1999, Hudhud, Yaas, or Dana. [24][23][26]
- **Flood hydrographs are more accessible than flood impact truth**: the National Water Data Portal exposes CWC hourly river-level CSV/API resources across historical periods, but event-specific district damage and inundation packages were found clearly only for 2013 and 2021. Searches did not produce equivalent primary packages for the requested 2011, 2017, 2019, or 2024 events. [4][26]
- **PMFBY cannot presently validate event-level recovery**: the official Lok Sabha annexure reports district aggregates for 2020-21 through 2024-25, totaling **88,55,046 enrollments** and **Rs. 2,580.06 crore** in claims paid, but it does not identify the cyclone/flood that caused each claim or settlement dates. [16]
- **Overall verdict is PARTIAL**: build realistic track, warning, rainfall, and river-stage replays now; treat hourly farm-level exposure, measured surge curves, district crop causality, and claim-settlement validation as gated workstreams requiring IMD/INCOIS/CWC/state requests.

## 2. EVENT DATASET

### 2.1 Cyclone events

| Event | What exists | Named source, URL, and date | Format | Resolution | Access | Reliability |
|---|---|---|---|---|---|---|
| **1999 Odisha Super Cyclone, 29 Oct 1999** | IBTrACS track; IMD/Mausam station observations; reported pressure minima at Paradip, Puri, and Bhubaneswar; wind observations at Puri and Bhubaneswar; about 7 m surge and inundation up to 35 km inland. The study says hourly coastal observations were composited, but no raw hourly download or district crop/livestock table was found. [12] | NOAA IBTrACS v4.01, current archive: `https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/`; IMD Mausam paper, event Oct 1999: `https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/1639/1454` | CSV/netCDF/Shapefile for track; PDF for observations | Mostly 6-hour track; isolated hourly station values/composite | Direct | **A track; B observations; C impact** |
| **Phailin, 8-14 Oct 2013** | IMD best track, hourly coastal observations, 30-minute satellite and 10-minute radar monitoring; 24-hour station rainfall; 2-2.5 m surge above astronomical tide and about 1 km saline-water penetration in Ganjam. State evidence reports 668,268 ha of crops affected; the annual report gives crop and district livestock totals, but the extracted evidence lacks district crop hectares. [21][26] | IMD Final Phailin Report, Oct 2013: `https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads/report/26/26_38a1d4_phailin.pdf`; Odisha Annual Report 2013-14: `https://srcodisha.nic.in/annualReport/dD4aVH69AnnualReport2013-14.pdf` | PDFs with tables and figures | Track/event table; hourly coastal observations described; daily rainfall; district/state damage | Direct | **B+** |
| **Hudhud, 7-14 Oct 2014** | IMD track and date-wise Odisha rainfall. Odisha totals include Mahendragarh 12 cm on 12 Oct and R. Udaigiri 26 cm on 13 Oct. No Odisha pressure series, observed wind series, surge measurement, or district crop/livestock table was found; detailed loss tables in the report are for Andhra Pradesh. [17] | IMD Hudhud Report, Oct 2014: `https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_fac6af_hud.pdf` | PDF | Best-track time series; daily rainfall observations | Direct | **B track; C Odisha impact** |
| **Fani, 26 Apr-4 May 2019** | IMD 3-hourly best track with wind and central pressure; 24-hour station rainfall; landfall wind maximum; estimated 1.5 m surge; warning timestamps. OSDMA DLNA provides district crop hectares and crop/livestock-sector losses. [13][24] | IMD Fani Summary, 2019: `https://rsmcnewdelhi.imd.gov.in/uploads/archive/60/60_a53fa0_fani.pdf`; OSDMA Fani DLNA, 2019: `https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf` | PDFs with track and district tables | 3-hour track; daily rainfall; district damage | Direct | **A-/B+** |
| **Amphan, 16-21 May 2020** | IMD 3-hourly track, intensity, rainfall, and warning chronology. Odisha final memorandum reports 10,726.18 ha of crops damaged, district crop areas, livestock deaths, and shoreline water levels of 3.70-4.00 m RL. RL is a datum-referenced level, not automatically a surge residual. [20][23] | IMD Amphan Summary, 14 Jun 2020: `https://internal.imd.gov.in/press_release/20200614_pr_840.pdf`; Odisha Final Memorandum, Aug 2020 posting: `https://www.osdma.org/wp-content/uploads/2020/08/Final-Memorandum-on-Super-Cyclone-AMPHAN-Shyamal.pdf` | PDFs | 3-hour track; daily rainfall; district damage | Direct | **B+** |
| **Yaas, 23-28 May 2021** | IMD 3-hourly track with estimated central pressure and wind; daily rainfall totals; estimated/realized surge of 2-4 m above astronomical tide in Balasore/Bhadrak and 1-2 m in Kendrapara/Jagatsinghpur. No continuous Odisha pressure/wind series or final district crop/livestock table was found. [10] | IMD Yaas Report, Jun 2021: `https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_77afd4_Preliminary%20Report%20YAAS%20during%2023-27%20May%202021.pdf` | PDF | 3-hour track; daily rainfall; district-level surge bands | Direct | **B hazard; C impact** |
| **Dana, 22-26 Oct 2024** | IMD best-track pressure series, daily rainfall windows, 100-110 kmph landfall winds gusting to 120 kmph, 1-2 m estimated surge, and warning lead times. The report gives aggregate impacts and names Kendrapara, Balasore, and Bhadrak as worst hit, but the official pre-event SRC notice only says crop loss will be assessed. [11][19] | IMD Dana Report, 7 Nov 2024: `http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf`; SRC notice, 23 Oct 2024: `https://srcodisha.nic.in/newspapper/dHx1Ir7zInformation%20on%20Cyclonic%20Storm%20%E2%80%9CDANA%E2%80%9D.pdf` | PDFs | 3-hour track; 24-hour rainfall; aggregate impact | Direct | **B hazard; C-/D district damage** |

**Cyclone takeaway:** Use IBTrACS as the normalized track table, IMD reports as the authoritative event and warning chronology, and OSDMA/SRC assessments as outcome truth only where district tables actually exist. Do not convert report maxima into hourly observations.

### 2.2 Flood events

| Event | What exists | Named source, URL, and date | Format | Resolution | Access | Reliability |
|---|---|---|---|---|---|---|
| **2011 flood** | CWC/NWDP historical hourly river levels should cover this period where the relevant station record exists. The Odisha flood-history file identifies 2011 as particularly severe, but searches did not recover a 2011 event hydrograph package, NRSC inundation layer, or district damage memorandum. [4][22] | CWC/NWDP hourly water levels, current: `https://www.nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc`; Odisha flood history: `https://dowr.odisha.gov.in/sites/default/files/2022-03/Major%20flood%20occurence.pdf` | CSV/API plus historical PDF | Hourly gauge data where available; state historical summary | Direct portal; station audit required | **B hydrology; D impact** |
| **2013 Phailin-related flood** | State report contains river danger levels/readings for 12-15 Oct, identifies Baitarani, Budhabalanga, Rusikulya, Subarnarekha, and Jalaka flooding, and supplies affected-area and livestock tables. [26] | Odisha Annual Report 2013-14: `https://srcodisha.nic.in/annualReport/dD4aVH69AnnualReport2013-14.pdf`; Phailin memorandum: `http://srcodisha.nic.in/calamity/MEMORANDUM.pdf` | PDF tables | Daily/intraday report readings; district/state damage | Direct | **B+** |
| **2017 flood** | CWC historical hourly levels are the usable raw layer. No event-specific Odisha damage memorandum or verified NRSC inundation product was found in the searched archives. | CWC/NWDP URL above | CSV/API | Hourly station level | Direct; impact request needed | **B hydrology; D impact** |
| **2019 flood** | No distinct 2019 Mahanadi/Brahmani/Baitarani event package was found. The NRSC Fani product maps flood-like low-lying areas after the cyclone, so it should be labeled a Fani compound-event layer, not silently substituted for a standalone 2019 river flood. | NRSC Fani report, 8 May 2019: `https://ndem.nrsc.gov.in/documents/Disaster_Document/2019/OD/odcyclone50dsc08052019/odcyclone50dsc08052019_report.pdf` | PDF rapid map/report | Satellite snapshot | Direct PDF | **C for Fani compound flooding; D for requested standalone flood** |
| **2021 flood** | CWC/NWDP provides a 2021-25 hourly level resource, and the Odisha Annual Report 2021-22 contains flood chronology, river water-level reporting, affected districts, and damage sections. A machine-readable inundation polygon was not found. [4] | Odisha Annual Report 2021-22: `https://srcodisha.nic.in/annualReport/4vP2yUSqANNUAL%20REPORT%20ON%20NATURAL%20CALAMITIES,2021-22.pdf`; CWC/NWDP URL above | PDF plus CSV/API | Event report plus hourly gauges | Direct | **B+ hydrology; B impact; C inundation** |
| **2024 flood** | CWC/NWDP's 2021-25 resource is the raw hydrology path. Targeted searches did not recover a verified Odisha 2024 NRSC rapid-map URL or a final district crop/livestock report; many returned products were for Andhra Pradesh or Assam. | CWC/NWDP URL above; SRC flood listing: `https://srcodisha.nic.in/flood.php` | CSV/API; portal listing | Hourly gauges; no verified event impact layer | Direct for gauges; state/NRSC request likely for missing products | **B hydrology; D impact** |

**Flood takeaway:** The replay can reconstruct river stage for all requested years only after station coverage is audited. Outcome validation is presently strongest for 2013 and 2021 and weak for 2011, 2017, 2019, and 2024.

### 2.3 PMFBY claims and published academic datasets

The best official claims source found is a Lok Sabha annexure dated **2 Dec 2025**, covering district-level enrollments and claims paid from **2020-21 to 2024-25**. It is a direct PDF, but the rows aggregate five years and do not identify event, crop, policy, loss date, notification date, approval date, or payment date. [16]

Use it only for a coarse recovery benchmark. It cannot test whether a Fani, Yaas, Dana, or flood advisory accelerated a specific payout. No PMFBY event package was found for 1999, Phailin, Hudhud, or Fani, and the discovered official annexure does not reach back to 2019.

No credible academic repository supplied a complete raw Odisha event package. The 1999 Mausam paper publishes valuable observations but no supplemental hourly file; Yaas studies describe Sentinel-1/GEE analysis but did not expose a reusable event raster in the discovered result; and generic Kaggle cyclone data lacked the provenance required for validation. These are methods or evidence sources, not substitutes for official raw archives.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing | Coverage judgment |
|---|---|---|---|
| **NOAA IBTrACS v4.01** | All seven cyclone tracks; UTC, latitude, longitude, wind, pressure, agency and interpolation flags; CSV/netCDF/Shapefile. [15][14] | Agency wind averaging differs; early tracks and pressure fields may be incomplete. [14] | **A** |
| **IMD/RSMC event reports** | Phailin, Hudhud, Fani, Amphan, Yaas, Dana; observed track, intensity, rainfall and warnings | Mostly PDF; station observations are often daily totals or maxima, not downloadable hourly AWS records | **B+** |
| **JTWC best track** | North Indian Ocean archive; 6-hour center/intensity; 1-minute mean wind; independent agency realization. [29] | Post-storm analysis may differ from warning positions by up to 120 nautical miles; recent intensity relies heavily on Dvorak analysis | **A-/B+** |
| **NOAA ISD / Global Hourly** | Open hourly/synoptic wind, gust, pressure and precipitation; direct bulk files and web services. [7] | Odisha station inventory and event completeness must be checked; station records contain gaps | **A data family; B event coverage** |
| **IMD Data Supply Portal** | Authoritative station-level hourly/daily observations and custom station-period requests | Tariffs, signed forms/undertaking, delay, purpose and redistribution restrictions [9] | **A quality; gated access** |
| **CWC/NWDP** | Historical hourly river levels in CSV/API by station and river grouping [4] | Event labels, rating curves, discharge completeness, QC and exact district mapping are not packaged with the replay | **A-/B+** |
| **NRSC/NDEM** | Rapid satellite flood/cyclone maps; useful for event footprints | Account/terms restrictions; older direct URLs are difficult to discover; map products may be preliminary and are not always GIS downloads [30] | **B for located maps; C/D for missing years** |
| **INCOIS storm-surge service** | Operational storm-surge guidance and coastal hazard context | No open historical Odisha tide-gauge time-series download was exposed by the retrieved page | **C** |
| **OSDMA/SRC assessments** | Strong Fani DLNA, Amphan memorandum, Phailin/2013 and 2021 annual reports | Inconsistent event coverage; PDFs; blanks and contradictory totals in some appendices | **B+ where present; D where absent** |
| **PMFBY/Parliament** | Official 2020-21 to 2024-25 district aggregate and Rs. 2,580.06 crore state total [16] | No event ID, individual claim, settlement date or payout timeline | **C** |
| **Academic/public repositories** | 1999 observational paper; Phailin review; remote-sensing methods | Generic Kaggle data, inaccessible supplements, or studies without reusable event files | **C evidence; D raw replay data** |

**Coverage decision:** Tracks and gauges have reusable schemas. Station weather, surge, crop damage, and claims must remain separate layers with explicit provenance and uncertainty rather than being forced into a falsely complete event table.

## 4. WHAT IS MISSING

### 4.1 Hourly meteorology

- **1999:** published hourly/composited coastal evidence exists, but no direct raw hourly station file was found. District agricultural loss tables are also absent from the retrieved primary study. [12]
- **Phailin:** IMD says coastal observations were hourly, but the event PDF does not provide a clean machine-readable continuous series for every station. A DSP request is still needed for raw pressure, sustained wind, gust, and rainfall.
- **Hudhud:** no Odisha station-pressure or observed wind series; only date-wise rainfall. The observed 1.4 m surge and detailed damage table are for Visakhapatnam/Andhra Pradesh, not Odisha. [17]
- **Fani:** no public Odisha station-pressure series in the located report; rainfall is 24-hour accumulation and wind is a landfall maximum. [13]
- **Amphan:** track is 3-hourly, but the open report does not supply a continuous Odisha AWS pressure/wind/gust series. [20]
- **Yaas and Dana:** estimated central pressure and daily rainfall are available, but no continuous Odisha station pressure/wind/gust file was found. [10][11]

### 4.2 Surge and inundation

- No downloadable high-frequency tide-gauge residual series was found for any of the seven events.
- **Hudhud:** no observed Odisha surge.
- **Fani, Yaas, Dana:** report maxima or spatial bands, not hydrographs.
- **Amphan:** 3.70-4.00 m RL must not be interpreted as surge above astronomical tide without the vertical datum and predicted tide. [23]
- No verified GIS inundation polygons were found for 1999, Phailin, Hudhud, Fani, Amphan, Dana, or the requested 2011, 2017, 2019, and 2024 floods. Yaas has published Sentinel-1 analysis, but no reusable raster link was verified.

### 4.3 District crop and livestock truth

- **1999:** no retrieved district crop-area, crop-value, or livestock table.
- **Phailin:** district livestock exposure exists, but district crop hectares were not present in the extracted evidence for the affected 19 districts. [26]
- **Hudhud:** no Odisha district crop/livestock table.
- **Fani:** best coverage, with district crop area and monetary losses; still distinguish assessed damage from crop-specific yield loss. [24]
- **Amphan:** strong district crop coverage, but poultry cells are blank for some districts and totals conflict between summary and appendix, including 1,903 versus 1,913 livestock affected/lost. [23]
- **Yaas:** no final district crop/livestock assessment found for Balasore, Bhadrak, Kendrapara, or Jagatsinghpur.
- **Dana:** no final district crop/livestock table found for the named worst-hit districts Kendrapara, Balasore, and Bhadrak; the official pre-event document promises assessment rather than reporting it. [19][11]

### 4.4 Flood and insurance gaps

- **2011, 2017, 2019, 2024:** no complete event bundle joining CWC hydrograph, NRSC inundation extent, and SRC district damage was found.
- Gauge-to-district mapping, station datum changes, rating curves, reservoir-release logs, embankment breaches, and backwater/drainage-congestion observations remain unassembled.
- PMFBY lacks event identifiers, crop/policy-level losses, notification dates, approval dates, bank-credit dates, rejection reasons, and individual timelines. The official table is district aggregate only. [16]

**Gap decision:** Do not report that an event had "no hourly data" in existence. Report the narrower verified conclusion: **no open, continuous, event-packaged Odisha series was found**, and list ISD/IMD DSP as the acquisition route.

## 5. HOW IT FEEDS THE REPLAY SIMULATION

| Simulation layer | Data input | Replay method | Validation test | Failure guardrail |
|---|---|---|---|---|
| **Hazard field** | IBTrACS/IMD/JTWC track, wind and pressure; CWC hourly level | Keep each agency track as a versioned realization; interpolate position only between valid times; construct wind/rain/flood fields with explicit model assumptions | Compare modeled landfall time, district exposure, station maxima and gauge crest timing to report observations | Never treat best-track central pressure as station pressure or daily rainfall as an hourly rate |
| **Advisory timing** | Archived IMD warnings and event-report lead times | Replay only information available at each simulated issue time; freeze later best-track revisions | Test whether advice was issued before the operational action window; Fani provides watch, alert, warning and post-landfall timestamps [13] | Do not leak final best track, final surge, or damage outcomes into the advisory engine |
| **Farm exposure** | Farm coordinates, crop, sowing date, growth stage, irrigation, livestock, soil and elevation | Spatially join each farm to hazard layers and district/block administration | Compare exposed hectares with OSDMA/SRC assessed hectares | Do not downscale district totals into fake farm observations without an uncertainty model |
| **Crop damage** | Fani DLNA, Amphan memorandum, Phailin totals, crop calendars | Fit event-specific or hierarchical damage functions by hazard, crop stage and duration | Hold out districts where tables exist; compare damaged hectares and loss ranges | Do not train and validate on the same district aggregate; flag blank/inconsistent cells |
| **Flood inundation** | CWC hydrographs, DEM, river network, NRSC footprint where available | Reconstruct stage timing first; add hydraulic or threshold inundation only where datum and terrain support it | Compare peak timing and mapped wet area, not just total district area | A static flood-hazard atlas is not an event footprint |
| **Storm surge** | Reported peak surge, tide level, shoreline water level and DEM | Calibrate peak coastal boundary with source-specific datum labels | Validate maximum coastal penetration or district band | Never mix "above astronomical tide", RL, total water level and modeled surge |
| **SMS/IVR delivery** | Warning issue times, local-language templates, acknowledgement/delivery logs | Simulate send queue, retry, IVR completion and farmer action latency | Measure delivery-before-deadline and action completion, not merely message generation | IMD's existing system sends SMS to registered farmers and fishermen, but that establishes a channel, not receipt or behavior [31] |
| **Recovery** | Damage assessment, relief, PMFBY district aggregates | Estimate when advice should shift from protection to drainage, re-sowing, livestock health and claim assistance | Compare aggregate recovery intensity only | Do not claim event-level payout acceleration without claim-level dates |

### Case study: Fani as the first full replay

Fani is the strongest initial case because it combines a 3-hourly IMD track, daily station rainfall, explicit warning lead times, a reported peak surge, and a district-level DLNA. The engine can be run in operational time from the 29 April watch through landfall, while the final IMD track remains hidden until scoring. [13]

The validation should have two stages. First, score hazard timing against landfall and district rain/wind observations. Second, score crop-risk ranking against DLNA district hectares and losses. A high rank correlation is defensible; a claim that the advisory "would have saved X rupees" is not, unless farmer action, adoption, and counterfactual damage are separately modeled.

### Case study: Hudhud as a deliberate failure test

Hudhud tests whether the system refuses to overclaim. The IMD report supplies Odisha rainfall observations, but pressure, observed surge, and detailed loss tables center on Andhra Pradesh. [17]

A robust replay should therefore produce a lower-confidence Odisha impact score and label missing validation channels. If the system generates precise Odisha crop savings from Andhra Pradesh losses, the simulation has failed provenance control.

## 6. REAL-vs-FILLER

| Classification | Evidence | Use |
|---|---|---|
| **REAL - core input** | IBTrACS CSV/netCDF/Shapefile | Canonical cross-event track table |
| **REAL - core input** | IMD 3-hourly best-track and warning tables | Operational chronology and intensity |
| **REAL - conditional input** | NOAA ISD hourly station files | Use only after station/date completeness and flags are audited |
| **REAL - gated input** | IMD DSP station observations | Highest-value request for pressure, gust and rainfall series |
| **REAL - core flood input** | CWC/NWDP hourly CSV/API | Hydrograph reconstruction after station/datum QC |
| **REAL - outcome truth** | Fani DLNA, Amphan memorandum, Phailin/2013 report | District damage validation with table-level caveats |
| **REAL - coarse outcome** | PMFBY parliamentary district aggregate | Recovery context, not event causality |
| **FILLER unless upgraded** | Cyclone path image, news infographic, generic rainfall map | Presentation only; no simulation values |
| **FILLER for event replay** | Static flood-hazard atlas | Prior-risk layer, not observed event inundation |
| **FILLER** | Generic Kaggle cyclone dataset without agency provenance | Exclude from validation |
| **FILLER** | Wikipedia event totals | Discovery only; replace with primary report |
| **FILLER** | Paper describing GEE/Sentinel analysis without downloadable output | Method reference, not a reusable event layer |
| **FILLER** | GSOD daily summaries when hourly timing is claimed | May support daily totals, but cannot validate hourly advisory timing |

**Decision rule:** A file enters the replay only if it has an event date, spatial reference or station identity, units, temporal resolution, provenance, and a documented meaning for missing values. Otherwise it belongs in the demo layer, not the scoring layer.

## 7. NOISE LOG

1. **OSDMA PDF 3890:** a printing-supply quotation, not a Phailin damage report. Discarded.
2. **Generic Kaggle cyclone dataset:** no verified IMD/JTWC/IBTrACS lineage for the requested events. Discarded.
3. **Wikipedia cyclone pages:** useful for query discovery only. Replaced by IMD and state reports.
4. **Scribd mirrors:** discarded whenever an official IMD/OSDMA PDF was available.
5. **Kosi flood Zenodo result:** wrong basin and geography. Discarded.
6. **NRSC search returns for Andhra Pradesh and Assam in 2024:** wrong state; not evidence of Odisha flood coverage.
7. **2018-19 Odisha annual report:** useful for Daye/Titli and general flood context, but it does not establish the requested standalone 2017 or 2019 flood package. [22]
8. **PSMSL long-term sea-level pages:** potentially useful for tide context, but no verified high-frequency Paradip/Gopalpur event series was found. Not used as surge truth.
9. **INCOIS operational storm-surge page:** establishes service existence but did not expose the requested historical raw tide-gauge archive. Not counted as a measured event dataset.
10. **Dana news crop estimates:** figures varied and lacked a final official district table. Excluded from validation.
11. **CivicDataSpace 2022-23 cumulative-loss map:** outside the requested flood years and combines multiple indicators. Not an event observation.
12. **PMFBY state-year or dashboard summaries:** retained only as context where official, never treated as cyclone/flood-linked claims.

## 8. VERDICT

# **PARTIAL**

### What can be built now

A student team can build a credible **hazard and advisory-timing replay** for all seven cyclones using IBTrACS plus IMD reports. It can also build flood-stage replays from CWC/NWDP after station coverage checks. Fani should be the primary end-to-end benchmark, with Phailin and Amphan as secondary damage cases and Hudhud as the missing-data stress test.

### What remains gated

A scientifically defensible farm-outcome replay is gated by four acquisitions:

1. **IMD DSP:** hourly pressure, sustained wind, gust and rainfall for selected Odisha stations and exact event windows.
2. **INCOIS/port authorities:** high-frequency tide-gauge observations, predicted tide, vertical datum and QC metadata.
3. **SRC/OSDMA/Agriculture Department:** final district/block crop and livestock tables for 1999, Hudhud, Yaas, Dana, and the missing flood years.
4. **PMFBY insurers/NCIP:** de-identified claim-level event/crop/policy dates and payout timelines, likely requiring a formal data-sharing agreement or MOU.

### Synthesis

The evidence has a non-obvious asymmetry. Cyclone tracks have high temporal resolution and open access but weak farm specificity. Damage reports have strong local meaning but low temporal resolution and inconsistent event coverage. CWC gauges are machine-readable but describe river stage rather than inundated farms. PMFBY data describe recovery money but erase the causal event and timeline.

The architecture should mirror that asymmetry: a versioned hazard layer, a separately licensed observation layer, an event-specific impact layer, and a recovery layer. Confidence must be scored per layer and per event. With those controls, the project is a **GO for realistic warning replays**, **PARTIAL for crop-damage validation**, and **GATED for claims and counterfactual savings**.

## References

1. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
2. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Amphan*. https://www.osdma.org/publication/amphan/
3. *The 1999 super cyclone in Odisha, India: A systematic review of documented losses - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212420920312929
4. *River Water Level (Telemetry - Hourly), Central Water Commission (CWC) - Dataset - National Water Data Portal*. https://www.nwdp.nwic.gov.in/dataset/river-water-level-telemetry-hourly-central-water-commission-cwc
5. *Cyclone 'AMPHAN' Report on Restoration and Damage Assessment 23.05.2020*. https://www.osdma.org/wp-content/uploads/2020/05/Situation-report.pdf
6. *Wp Content*. https://www.osdma.org/wp-content/uploads/2019/10/3890.pdf
7. *Global Hourly - Integrated Surface Database (ISD) | National Centers for Environmental Information (NCEI)*. https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database
8. *NCEI Search, Discovery, & Data Access*. https://www.ncei.noaa.gov/access/search/datasets/global-hourly/
9. *Meteorological Data Supply*. https://mausam.imd.gov.in/chennai/mcdata/data_supply.pdf
10. *26 77Afd4 Preliminary Report Yaas During 23 27 May 2021*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_77afd4_Preliminary%20Report%20YAAS%20during%2023-27%20May%202021.pdf
11. *Severe Cyclonic Storm “DANA” over the Bay of Bengal (22 -26 October, 2024): A Report (b) (a)*. http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
12. *Are You suprised ?*. https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/download/1639/1454
13. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/archive/60/60_a53fa0_fani.pdf
14. *International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4.01*. http://ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01552
15. *IBTrACS v04 column documentation*. http://ncei.noaa.gov/sites/default/files/2021-07/IBTrACS_v04_column_documentation.pdf
16. *Microsoft Word - ls36*. https://sansad.in/getFile/loksabhaquestions/annex/186/AS36_U80S8R.pdf?source=pqals
17. *26 Fac6Af Hud*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_fac6af_hud.pdf
18. *A review on Management of cyclone Phailin 2013 in Odisha*. https://www.ijfcm.org/archive/volume/2/issue/4/article/14268/pdf
19. *Dhx1Ir7Zinformation On Cyclonic Storm “Dana”*. https://srcodisha.nic.in/newspapper/dHx1Ir7zInformation%20on%20Cyclonic%20Storm%20%E2%80%9CDANA%E2%80%9D.pdf
20. *Press Release*. https://internal.imd.gov.in/press_release/20200614_pr_840.pdf
21. *PHAILIN Report(Final) 30*. https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads%2Freport%2F26%2F26_38a1d4_phailin.pdf
22. *Izqvhtymannual Report On Nc 2018 19 Compressed*. https://srcodisha.nic.in/annualReport/IZQVHTYMAnnual%20Report%20on%20NC%202018-19_compressed.pdf
23. *FINAL MEMORANDUM on SUPER CYCLONIC STORM “AMPHAN”*. https://www.osdma.org/wp-content/uploads/2020/08/Final-Memorandum-on-Super-Cyclone-AMPHAN-Shyamal.pdf
24. *untitled*. https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
25. *ANNUAL REPORT ON NATURAL CALAMITIES 2021-22*. https://srcodisha.nic.in/annualReport/4vP2yUSqANNUAL%20REPORT%20ON%20NATURAL%20CALAMITIES%2C2021-22.pdf
26. *srcodisha.nic.in*. https://srcodisha.nic.in/annualReport/dD4aVH69AnnualReport2013-14.pdf
27. *Joint Typhoon Warning Center (JTWC)*. https://www.metoc.navy.mil/jtwc/jtwc.html?north-indian-ocean
28. *incois.gov.in*. https://incois.gov.in/site/services/StormSurge.jsp
29. *ATCR report plan*. https://www.metoc.navy.mil/jtwc/products/best-tracks/tc-bt-report.html
30. *Hydrological Disaster*. https://ndem.nrsc.gov.in/hydrologicaldisasters/index.php
31. *http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf*. http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf
