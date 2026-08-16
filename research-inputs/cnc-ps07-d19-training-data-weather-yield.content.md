# Training Data Reality Check for KrishiSetu

## 1. EXECUTIVE SUMMARY

- **Weather Backbone Is Ready**: IMD publishes daily **0.25 x 0.25 degree rainfall for 1901-2024 in yearly NetCDF files** [5], while its maximum and minimum temperature pages describe daily **1 x 1 degree data for 1951-2024** in binary grids [26][28]. -> Download and freeze these through 2024 as the prototype's reproducible weather baseline.
- **Free Download Does Not Equal Clear Reuse Rights**: The general Government Open Data License permits worldwide, royalty-free commercial and non-commercial reuse with attribution [15], but the retrieved IMD grid pages do not expressly attach that license. IMD's request route can also restrict redistribution and use to the declared purpose [27]. -> Treat GODL and IMD supply terms as separate; obtain written reuse confirmation before a public pilot.
- **The Best-Track Premise Needs Correction**: The live RSMC page currently labels its consolidated product **"Best Tracks Data (1982-2026)," not 1961-present** [32]. The page exposes an XLSX workbook and an explanatory best-track PDF, but the current year can be incomplete. -> Train against a versioned 1982-2024 snapshot and use IBTrACS only as a documented gap-fill or cross-check.
- **Hydrology Is Available but Not Yet Reproducible**: CWC states that unclassified hydrological-observation data are free to download through WRIS [11], and the National Water Data Portal identifies manual daily river-discharge observations [3]. It does not publish one uniform national start year in the retrieved metadata. -> Inventory Odisha stations and their individual record spans before claiming a river model.
- **Odisha Yield Labels Exist, but Mostly in PDFs**: *Odisha Agriculture Statistics 2023-24* contains district crop area, production, and yield tables, with historical spans varying by table, including crop-yield series from 2018-19 to 2023-24 and some state comparisons reaching 2006-07 [20]. -> Parse and manually validate these tables; they are useful district-season outcomes, not farm-level cyclone-loss labels.
- **Economic and Insurance Data Are Context, Not Ground Truth**: DES/CACP publishes cost-of-cultivation estimates through its official scheme [12], while public PMFBY material provides state-year and some district-level aggregates rather than open district-by-crop loss-assessment microdata [9][31]. -> Use costs to rank advisory value; do not train damage probability directly on PMFBY aggregates.
- **Satellite Inputs Are the Strongest Open Hyperlocal Layer**: Sentinel-1 supplies all-weather C-band radar imagery [24], Sentinel products are free for public, scientific, and commercial users [8], and NASA identifies a half-hourly 0.1-degree IMERG precipitation product [29]. -> Make Sentinel-1 the flood-extent layer, Sentinel-2 the crop-condition layer, and IMERG a gap-filling rainfall feature rather than a substitute for IMD observations.
- **Soil and Household Portals Overstate Model Readiness**: The Soil Health Card listing claims **5 crore samples** with nutrient profiles and fertilizer recommendations but does not verify a public bulk download or API [23]. VDSA requires registration/login [1], and ASUSE covers unincorporated **non-agricultural** establishments [19]. -> Keep these outside the prototype's critical path.
- **Decision**: The evidence supports a **GO** for an event-reconstruction and rule-plus-risk prototype. It supports only **PARTIAL** predictive validation and a **GATED** farmer pilot until parcel labels, Odisha gauge histories, licensing, and delivery consent are secured. IMD already distributes warnings through SMS to farmers and fishermen, demonstrating that the channel is operationally plausible [33].

## 2. DATA INVENTORY

**Grades:** A = authoritative, directly useful, and reproducibly obtainable; B = authoritative but requires conversion, registration, or coverage work; C = partial, aggregate, or operationally gated; D = unsuitable, unverified, or only decorative for training.

| Item | Named source, URL, and date | Specification | Student-team feasibility | Reliability grade |
|---|---|---|---|---|
| IMD gridded rainfall | IMD Pune, `https://imdpune.gov.in/cmpg/Griddata/Rainfall_25_NetCDF.html`, coverage shown through 2024; checked 2026-08-16 | Daily rainfall, India, **0.25 x 0.25 degree**, **1901-2024**, yearly NetCDF [5] | **Download now.** Script yearly files, preserve checksums, crop to Odisha, and stop at 2024 for a complete training window. | **A** |
| IMD gridded temperature | IMD Pune maximum/minimum pages, `https://imdpune.gov.in/cmpg/Griddata/Max_1_Bin.html` and `.../Min_1_Bin.html`; checked 2026-08-16 | Daily 1-degree, 31 x 31 India grid, Celsius, product description **1951-2024**, binary GRD. IMD warns that post-2008 grids use a smaller operational station set of about 180 [26][28]. | **Download and decode now.** Use the supplied grid layout; document the 2008 station-density break. Pages list years into 2025, but freeze at the last clearly described complete period. | **A-** |
| IMD data procurement and fees | IMD Data Service Portal and supply procedure, `https://dsp.imdpune.gov.in/` and `https://mausam.imd.gov.in/chennai/mcdata/data_supply.pdf`; procedure operational since 2019 [10] | Online application; applicant categories include student, educational, government, commercial, and foreign users. Payment advice contains data cost plus GST, but the retrieved procedure supplies no universal tariff table [27]. | **Gated for non-free/station data.** Submit purpose, request form, and undertaking; wait for a quote. Payment confirmation can delay supply [27]. | **B/C** |
| IMD/Government license | GODL India v0.4/finalization letter, `https://www.data.gov.in/sites/default/files/Draft_GODL.pdf`, 2016 | Permits use, adaptation, publication, derivative products, and commercial or non-commercial services with source/license attribution; sensitive, third-party, personal, and protected data are excluded [15]. | **Usable only where attached to the resource.** Do not infer that every IMD file is GODL-covered. IMD-requested data may prohibit onward transmission without approval [27]. | **A for GODL text; C for IMD applicability** |
| IMD cyclone best track | RSMC New Delhi, `https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=MzM=`, checked 2026-08-16 | Live consolidated listing is **1982-2026** [32]; page links an XLSX workbook plus `bestrack.pdf`, which identifies the product as best-track data for tropical disturbances over the North Indian Ocean [34]. | **Download now.** Convert workbook to tidy storm-time records; exclude incomplete 2026 and archive the source file. The requested 1961-present span was not confirmed on the live consolidated page. | **A for 1982 onward; C for asserted 1961-81** |
| CWC river gauges | CWC India-WRIS and NWDP, `https://cwc.gov.in/en/water-resources-information-system-wris` and `https://nwdp.nwic.gov.in/dataset/river-discharge-manual-dailly-central-water-commission-cwc`; checked 2026-08-16 | CWC says all unclassified HO-station data are free to download [11]. NWDP describes daily manual discharge observations from CWC stations [3]. Record starts, missingness, and variables differ by station; no single national start year was established. | **Downloadable after station discovery.** First build an Odisha station catalog for Mahanadi, Brahmani, Baitarani, Subarnarekha, Rushikulya, and coastal basins; record each station's first/last date and gaps. | **B** |
| Odisha crop area, production, yield | Odisha Department of Agriculture, `https://agri.odisha.gov.in/sites/default/files/2025-05/OAS%20A4.pdf`, *Odisha Agriculture Statistics 2023-24* | District area, production, yield, irrigation, fertilizer, seed, rainfall, and agro-climatic-zone tables. Coverage varies: recent crop yields span 2018-19 to 2023-24; some comparative series extend earlier [20]. | **Download now, transform manually.** PDF tables are partly extractable but contain fragmented rows and OCR corruption [20]. Dual-entry checks are needed for target crops and districts. | **A source / B format** |
| DES, DACNET, and CACP costs | DES Cost Studies, `https://desagri.gov.in/divisions-cell/cost-studies-cs`; checked 2026-08-16 | Official scheme generates cultivation and production cost estimates for principal crops [12]. The retrieved catalog did not expose a stable machine-readable Odisha-by-crop time series or complete year list [30]. | **Reports available; dataset assembly required.** Extract cost concepts such as paid-out and imputed inputs only after checking each report's definitions. Not needed for hazard prediction. | **B for reports; C for bulk data** |
| ICRISAT District Level Database | ICRISAT DLD, `http://data.icrisat.org/dld/`; checked 2026-08-16 | Portal reports **74 datasets, 571 districts, and 11M+ records** [13]. It separates an apportioned database using 1966 district boundaries from an unapportioned database using 2015 boundaries and includes season-wise crop area/production in additional variables [13]. | **Promising but test export/login.** Use it for harmonized long-run district covariates, not without reconciling district splits to Odisha's current boundaries. | **B** |
| ICRISAT VDSA | VDSA, `https://vdsa.icrisat.org/vdsa-database.aspx`; checked 2026-08-16 | Longitudinal village/household resource with separate micro/meso documentation. Dataset use requires registration/login; questionnaires are downloadable [1]. Retrieved evidence did not confirm Odisha village coverage. | **Gated.** Register and inspect coverage. If Odisha is absent, use only for methodology or transfer-learning experiments, not local validation. | **C** |
| PMFBY claims and loss assessment | PMFBY portal plus Parliament annexures, `https://pmfby.gov.in/`; public material checked 2026-08-16 | One official release provides state/company/year gross premiums and claims for 2016-17 to 2022-23 [9]. An Odisha annexure offers district enrollment and claims paid for the last five years, but no crop-level fields or loss-assessment microdata are identified [31]. | **Reports downloadable; training labels not.** District claim rate may be manually derived only when denominators and years align. Insurer/Crop Cutting Experiment microdata require a formal request or MOU. | **C for aggregates; D for parcel-loss labels** |
| Soil Health Card | Portal and AIKosh listing, `https://soilhealth.dac.gov.in/` and `https://aikosh.indiaai.gov.in/home/datasets/details/shc_dataset.html`; checked 2026-08-16 | Listing claims nationwide data from **5 crore samples**, nutrient profiles, fertilizer recommendations, and GIS mapping [23]. NIC confirms the portal is a Ministry web/mobile application [16]. Public bulk format, stable API, time coverage, and license were not verified. | **Dashboard viewing only until proven otherwise.** Ask Odisha Agriculture for an anonymized district/block aggregate or documented export. Do not scrape farmer-level records. | **C/D** |
| Sentinel-1 and Sentinel-2 | Copernicus Data Space, `https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/`; checked 2026-08-16 | Sentinel-1 uses all-weather C-band SAR [24], suitable for event flood masks. Sentinel-2 monitors land-surface change with a 290 km swath and high revisit [8]. Sentinel products are systematically free to public, scientific, and commercial users [8]. | **Download now through Copernicus Data Space.** Use S1 before/after pairs for inundation and S2 vegetation indices for crop condition, with explicit acquisition-date and quality masks. | **A** |
| NASA GPM IMERG | NASA Open Data/Earthdata, `https://data.nasa.gov/dataset/gpm-imerg-final-precipitation-l3-half-hourly-0-1-degree-x-0-1-degree-v07-gpm-3imerghh-at-g-fb698`; checked 2026-08-16 | The official catalog identifies Final V07 precipitation at **half-hourly, 0.1 x 0.1 degree** resolution [29]. | **Downloadable with Earthdata workflow.** Aggregate to farm-day/event features and bias-check against IMD. It is precipitation, not a flood-extent label. | **A-** |
| Bhuvan and GDACS flood layers | Bhuvan Disaster Services, `https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php`; GDACS search checked 2026-08-16 | Bhuvan exposes flood-inundation products and says aggregated flood maps are prepared from available historic flood maps [21]. Retrieved pages did not establish bulk raster/API access, Odisha event years, scale, or a training license. No equivalent model-ready GDACS India layer was found. | **Bhuvan is useful for visual validation and possible labels after access confirmation. GDACS is not a core training source.** | **C** |
| NSS 77 Situation Assessment and ASUSE | MoSPI Microdata Catalog, `https://microdata.gov.in/NADA/index.php/catalog/134`; ASUSE report `https://www.mospi.gov.in/sites/default/files/press_release/Press_Note_ASUSE_202324_Report%20-English.pdf` | The NSS catalog is the relevant route for agricultural-household economics. By contrast, ASUSE 2023-24 explicitly covers unincorporated **non-agricultural** manufacturing, trade, and services establishments [19]. | **NSS catalog: potentially downloadable after registration/document review. ASUSE: exclude from farmer training; at most use state economic context.** | **B/C for NSS; D for ASUSE fit** |

The central split is clear: physical hazard inputs are mostly open and reproducible, but damage, farm, insurance, and soil labels become progressively more aggregated or access-controlled. That makes KrishiSetu feasible as a hybrid advisory system before it is feasible as a farm-loss prediction system.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing elements | Coverage judgment |
|---|---|---|---|
| IMD gridded climate | Long daily rainfall and temperature histories; documented grids and formats [5][26] | No explicit license notice on retrieved grid pages; temperature station-density break after 2008 | **A-** |
| IMD cyclone archive | Current RSMC consolidated workbook and explanatory PDF [32][34] | Live consolidated span begins in 1982, not the requested 1961; current year may be incomplete | **B+** |
| CWC/WRIS hydrology | Authoritative free unclassified station data and daily discharge catalog [11][3] | No single uniform period, completeness report, or Odisha-only bulk package | **B** |
| Crop and yield statistics | Rich official district/crop PDF, including recent yield series [20] | Variable time spans, OCR corruption, boundary changes, no farm/event loss labels | **B+** |
| Costs and farm economics | Official DES/CACP program; NSS agricultural-household catalog | Report-oriented access; cost concepts differ; VDSA gated; ASUSE is out of scope | **C** |
| Insurance and loss | PMFBY state/year and some district aggregates [9][31] | No open district x crop x event claim table, CCE microdata, adjuster reports, or rejected-claim reasons | **C-/D** |
| Soil | Very large national SHC listing with nutrients and recommendations [23] | No verified public bulk export, API, license, temporal provenance, or safe farmer-level access | **C-** |
| Satellite and rainfall remote sensing | Free Sentinel archive; all-weather S1; IMERG 0.1-degree half-hourly product [24][29] | Requires substantial preprocessing; Bhuvan bulk access and event metadata remain unclear | **A-** |
| Advisory delivery evidence | IMD sends warnings through SMS to government agencies, the public, farmers, and fishermen [33] | No evidence here for KrishiSetu's IVR comprehension, consent, language quality, or delivery success | **B for channel precedent; D for product validation** |

**Coverage judgment:** The project has good hazard-feature coverage, moderate district-outcome coverage, and weak causal-loss and farm-level coverage. A prototype should therefore optimize for transparent event risk tiers and rule-based actions, not unsupported precision claims.

## 4. WHAT IS MISSING

1. **A farm-event-outcome join key.** No retrieved source links a specific Odisha plot, crop variety, sowing date, growth stage, cyclone/flood exposure, action taken, and measured post-event yield or loss. Without that table, supervised learning can estimate district risk but cannot honestly predict a named farmer's loss.

2. **A confirmed 1961-81 IMD best-track package.** The current consolidated RSMC listing begins in 1982 [32]. Historical annual PDFs, e-Atlas records, or IBTrACS may fill earlier years, but they must be reconciled field-by-field rather than silently concatenated.

3. **A reproducible Odisha gauge manifest.** CWC confirms free unclassified data [11], yet the team still needs station identifiers, coordinates, river/basin, gauge or discharge variable, units, datum changes, first/last date, missing-day rate, and telemetry/manual status for every selected station.

4. **Machine-readable crop outcomes.** Odisha's publication is authoritative but not clean. District boundaries, crop naming, Kharif/Rabi conventions, revisions, and OCR errors must be normalized. The report itself uses different historical windows by table [20].

5. **Insurance ground truth.** Public PMFBY evidence stops at premiums, enrollment, and claims paid [9][31]. Missing fields include notified unit, crop, season, insured area, sum insured, cause/date of loss, assessed yield, threshold yield, approved/rejected claim, payout date, and appeal outcome.

6. **Soil provenance and access contract.** The SHC listing does not establish whether sample coordinates are public, whether repeated samples can be linked over time, or whether bulk use and redistribution are permitted [23].

7. **Farm profile and consent data.** KrishiSetu must collect crop, variety, planting/transplanting date, plot polygon or village, irrigation/drainage, livestock/storage, phone language, IVR preference, consent, and opt-out status. These are product data, not recoverable from historical public portals.

8. **Action-effect labels.** Historical weather plus yield cannot reveal whether moving seed, draining a field, harvesting early, or delaying fertilizer caused a better outcome. A pilot needs randomized rollout, matched controls, or at least prospective action/outcome logging.

9. **Operational evaluation.** Delivery receipt is not comprehension. The project still needs Odia IVR tests, keypad response rates, repeat-listen behavior, message latency, false-alarm tolerance, and vulnerable-user accessibility measurements.

## 5. HOW IT FEEDS THE PRODUCT

| Product tier | Inputs | Model or mechanism | Decision powered |
|---|---|---|---|
| **Tier 0: Static farm baseline** | Farmer-entered crop, sowing date, land type, irrigation; Odisha crop statistics; optional validated soil aggregate | Crop-stage calendar, district prior, soil/drainage rules | Which advice applies to this farm before any alert |
| **Tier 1: Weather and cyclone trigger** | Live IMD alert plus historical IMD grids and RSMC track archive | Alert parser, distance-to-track, forecast rain/wind bands, historical percentile | Whether to activate pre-disaster mode and its urgency |
| **Tier 2: Flood exposure** | CWC gauges, IMERG accumulation, Sentinel-1 flood mask, Bhuvan reference layers | Basin threshold rules plus event classifier; no black-box farm-loss claim | Which villages face waterlogging/inundation and when |
| **Tier 3: Crop consequence risk** | Crop stage, district yield history, hazard duration/intensity, land type | Interpretable ordinal model: low, medium, high consequence | Whether to harvest, drain, stake, move inputs, protect livestock, or stop application |
| **Tier 4: Economic prioritization** | CACP/DES cost estimates, farmer inventory, optional PMFBY eligibility | Avoided-loss ranking and resource constraints | Which action has the largest plausible value under limited time/labor |
| **Tier 5: Post-event recovery** | Farmer IVR response, Sentinel change, observed water recession, extension rules | Damage triage and rule engine | Re-sowing, drainage, disease watch, claim documentation, or extension referral |
| **Tier 6: SMS/IVR delivery** | Odia templates, farmer literacy/channel preferences, alert deadline | Template-constrained generation, text-to-speech, retry and acknowledgement logic | A short action sequence, deadline, reason, and escalation contact |

### Case study: reconstructing Cyclone Dana before predicting losses

IMD reported that it first signaled likely depression development and intensification about **7.5 days before landfall** [35]. It issued a pre-genesis track, intensity, and landfall prediction about **3.5 days before landfall** and reiterated it consistently [35]. It also predicted the heavy-rainfall impact about **4.5 days ahead** [35].

For a credible prototype, Dana should become an event-reconstruction test: ingest the archived alert, compute farm-to-track and rainfall features, obtain CWC levels, derive a Sentinel-1 inundation mask, and compare resulting district risk tiers with observed crop outcomes. This tests the end-to-end decision mechanism without pretending that district yield changes prove plot-level causation.

The production recommendation is therefore a **hybrid architecture**: authoritative alerts trigger deterministic safety rules; statistical models rank local exposure; human-authored agronomy templates constrain every SMS/IVR action. The model may choose among vetted actions, but it should not invent pesticide, fertilizer, harvest, or insurance instructions.

## 6. REAL-vs-FILLER

| Classification | Dataset or feature | Evidence-based judgment |
|---|---|---|
| **REAL now** | IMD 0.25-degree rainfall | Long, daily, authoritative, yearly NetCDF, directly aligned with event-history features [5] |
| **REAL now** | IMD 1-degree maximum/minimum temperature | Long daily archive with stated binary layout; suitable for heat and crop-stage covariates, subject to the post-2008 station caveat [26][28] |
| **REAL now** | RSMC 1982-2024 best-track snapshot | Authoritative storm chronology; use a frozen complete-year subset rather than the mutable 2026 workbook [32] |
| **REAL after ETL** | Odisha district crop statistics | Directly useful for district-season baselines and retrospective validation, but PDF extraction must be audited [20] |
| **REAL after station audit** | CWC daily river data | Authoritative and free when unclassified, but not reproducible until station spans and gaps are cataloged [11][3] |
| **REAL now** | Sentinel-1/2 and GPM IMERG | Open, scalable physical-observation features. Sentinel-1's all-weather radar is particularly relevant during cyclone cloud cover [24]. |
| **SUPPORTING, not predictive truth** | CACP costs | Useful for action prioritization and avoided-loss estimates; not a label for flood probability or crop damage [12]. |
| **SUPPORTING, gated** | ICRISAT DLD/VDSA | DLD can supply harmonized district covariates, while VDSA requires registration and lacks confirmed Odisha coverage [13][1]. |
| **DECORATIVE if presented as labels** | PMFBY dashboard totals | State or district payout aggregates reflect insurance design, enrollment, settlement, and exposure together. They do not identify physical loss at a plot [9][31]. |
| **DECORATIVE until access is proven** | Soil Health Card "API" | A large listing is not an API. No stable bulk endpoint, license, or time provenance was verified [23]. |
| **OUT OF SCOPE** | ASUSE | It measures unincorporated non-agricultural establishments, not agricultural households [19]. |
| **DECORATIVE for training** | Generic GDACS flood pages | Useful for situational awareness, but no verified Odisha parcel-scale historical training layer emerged from the search. |

### Failure case: the claims-rate shortcut

A model might divide PMFBY claims paid by enrolled farmers and call the result "cyclone damage rate." That would be misleading: the public annexure exposes enrollment and claims-paid aggregates but not crop, cause of loss, assessed damage, rejection, or timing [31]. The measured number would combine physical damage with policy rules, farmer take-up, insurer operations, and settlement lags.

The safe use is descriptive: identify high-claim districts for investigation, then request crop-season-notified-unit records under an MOU. Until those arrive, train hazard exposure from weather, water, and satellite observations; validate consequences against official district yields; and label outputs "risk tier," not "expected claim" or "predicted loss percentage."

## 7. NOISE LOG

| Searched and discarded | Reason for exclusion |
|---|---|
| Indiastat district pages | Search results advertised recent Odisha district rice tables, but access is commercial and the source is not the primary Odisha publication. |
| Scribd copy of Odisha Agriculture Statistics | Unofficial mirror with uncertain version integrity; the official Odisha PDF is available. |
| Wikipedia and TyphoonZone cyclone pages | Discovery aids only; not authoritative best-track sources. RSMC and, if needed, NOAA IBTrACS are preferable. |
| Facebook cyclone posts | Useful for public communication, not a stable machine-readable archive or training source. |
| Bihar Flood Hazard Atlas | Authoritative for Bihar but geographically irrelevant to Odisha; it cannot substitute for an Odisha layer. |
| Bhuvan viewer labels without downloads | Evidence that products exist, but not proof of a bulk raster, API, license, event period, or model-ready Odisha archive [21]. |
| PMFBY portal marketing pages | Establish the scheme, not the required district x crop x event claim dataset. |
| Parliament state-level PMFBY totals | Useful policy statistics but too aggregated for causal or farm-level training [9]. |
| AIKosh Soil Health Card listing | Valuable lead, but the claim of 5 crore samples does not prove student downloadability, API access, or reuse permission [23]. |
| ASUSE 2022-23 and 2023-24 | Explicitly non-agricultural; using it as farmer microdata would be an entity/scope error [19]. |
| Generic cost-of-cultivation landing pages | Confirm the official program but do not expose a consistent Odisha crop-year machine-readable panel [12][30]. |
| GDACS flood-map searches | No verified India-specific historical label set with the necessary spatial resolution and bulk-access terms was found. |

The noise pattern matters: many portals prove that a program or map exists, but fewer prove bulk access, years, schema, license, and stable download. KrishiSetu should count a source as training-ready only after all five are recorded in a data manifest.

## 8. VERDICT

| Stage | Verdict | Reasons | Release condition |
|---|---|---|---|
| **Hackathon prototype** | **GO** | IMD grids, RSMC tracks, Odisha crop tables, Sentinel, and IMERG can support historical event reconstruction and transparent risk tiers. SMS delivery has a real institutional precedent [33]. | Freeze complete-year snapshots; show data provenance; phrase outputs as risk tiers and vetted actions. |
| **Predictive model validation** | **PARTIAL** | District yield outcomes and physical hazard features exist, but CWC station coverage needs auditing and there are no open farm-event-loss or action-effect labels. | Complete Odisha gauge manifest, parse yield tables, reconstruct multiple cyclones/floods, and evaluate by held-out event rather than random rows. |
| **Farmer-facing pilot** | **GATED** | License applicability, parcel consent, SHC/PMFBY access, agronomic safety review, Odia IVR comprehension, and escalation operations remain unresolved. | Written data permissions; DPIA/consent design; extension-officer sign-off; delivery and comprehension tests; prospective outcome logging. |

### Synthesis

Across **mechanism**, the open weather and satellite sources measure physical exposure, crop statistics measure aggregate outcomes, and PMFBY measures an administrative insurance process. These are not interchangeable labels. Across **scope**, IMD and Sentinel are spatially broad, CWC is station-specific, Odisha statistics are district-season specific, and farmer advice is plot- and time-specific. Across **time horizon**, climate grids support historical priors, live IMD alerts trigger immediate action, and post-event satellite/gauge observations support recovery triage.

The non-obvious tension is that the easiest datasets to download are not the labels the most ambitious AI claim requires. Weather, track, and imagery can robustly answer "what hazard reached this area?" District yields can partly answer "was the season abnormal?" They cannot independently answer "how many rupees will this farmer lose?" or "did this advisory prevent that loss?" PMFBY appears closer to damage, but its public aggregates mix physical loss with enrollment and settlement mechanisms.

Accordingly, the strongest architecture is not an end-to-end loss predictor. It is a **data-fusion and constrained-decision system**: open observations estimate exposure; local farm profiles determine relevance; agronomy rules specify safe actions; SMS/IVR delivers them; and the pilot creates the missing action/outcome labels. This path is statement-faithful, demonstrable now, and capable of becoming more predictive without inventing precision.

## References

1. *VDSA: Village Dynamics Studies in South Asia - ICRISAT*. https://vdsa.icrisat.org/vdsa-database.aspx
2. *IMERG: Integrated Multi-satellitE Retrievals for GPM | NASA ...*. https://gpm.nasa.gov/data/imerg
3. *River Discharge (Manual - Daily), Central Water Commission ...*. https://nwdp.nwic.gov.in/dataset/river-discharge-manual-dailly-central-water-commission-cwc
4. *Legacy Dashboard*. https://soilhealth.dac.gov.in/dashboard
5. *Yearly Gridded Rainfall (0.25 x 0.25) data NetCDF File*. https://imdpune.gov.in/cmpg/Griddata/Rainfall_25_NetCDF.html
6. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop ...*. https://pmfby.gov.in/
7. *Situation Assessment survey of Agricultural households ... Microdata.gov.in https://microdata.gov.in › ... › Central Data Catalog › OTH*. https://microdata.gov.in/NADA/index.php/catalog/134
8. *Sentinel-2 | Copernicus Data Space Ecosystem*. https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2
9. *Premium Collection and Insurance Claims under Pradhan Mantri ...*. https://pib.gov.in/Pressreleaseshare.aspx?PRID=1941399
10. *IMD - Data Service Portal - dsp.imdpune.gov.in*. https://dsp.imdpune.gov.in/home_freedataaccess.php
11. *Water Resources Information System (WRIS) | Central Water ...*. https://cwc.gov.in/en/water-resources-information-system-wris
12. *Cost Studies (CS) | Official website of Directorate of ...*. https://desagri.gov.in/divisions-cell/cost-studies-cs
13. *ICRISAT-District Level Data*. http://data.icrisat.org/dld
14. *Flood Hazard Atlas - National Remote Sensing Centre*. https://ndem.nrsc.gov.in/hydrological_fhz.php
15. *Home | Open Government Data (OGD) Platform India*. https://www.data.gov.in/sites/default/files/Draft_GODL.pdf
16. *Soil Health Card Portal | National Informatics Centre | India*. https://www.nic.gov.in/project/soil-health-card-portal
17. *India - Annual Survey of Unincorporated Sector Enterprises ...*. https://microdata.gov.in/NADA/index.php/catalog/238
18. *Statistics - Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/en/page/statistics
19. *PRESS NOTE*. https://www.mospi.gov.in/sites/default/files/press_release/Press_Note_ASUSE_202324_Report%20-English.pdf
20. *OAS - agri.odisha.gov.in*. https://agri.odisha.gov.in/sites/default/files/2025-05/OAS%20A4.pdf
21. *Disaster Services*. https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php
22. *Flood Hazard Zonation*. https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php?id=flood_hz
23. *SHC Dataset - aikosh.indiaai.gov.in*. https://aikosh.indiaai.gov.in/home/datasets/details/shc_dataset.html
24. *Sentinel-1 - Copernicus Data Space Ecosystem*. https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-1
25. *asuse 2022-23 की मुख्य बातें*. https://www.mospi.gov.in/sites/default/files/publication_reports/ASUSE_2022_23_Report_FinalN.pdf
26. *Climate Monitoring and Prediction Group*. https://imdpune.gov.in/cmpg/Griddata/Min_1_Bin.html
27. *Meteorological Data Supply*. https://mausam.imd.gov.in/chennai/mcdata/data_supply.pdf
28. *Climate Monitoring and Prediction Group*. https://imdpune.gov.in/cmpg/Griddata/Max_1_Bin.html
29. *GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree ... NASA Open Data Portal (.gov) https://data.nasa.gov › dataset › gp...*. https://data.nasa.gov/dataset/gpm-imerg-final-precipitation-l3-half-hourly-0-1-degree-x-0-1-degree-v07-gpm-3imerghh-at-g-fb698
30. *Cost of Cultivation/Production Estimates | Official website ...*. https://desagri.gov.in/document-report-category/cost-of-cultivation-production-estimates/
31. *ls36 - sansad.in*. https://sansad.in/getFile/loksabhaquestions/annex/186/AS36_U80S8R.pdf?source=pqals
32. *Best Track - IMD*. https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=MzM=
33. *http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf*. http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf
34. *Microsoft Word - Best track _website_.doc*. https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads/report/bestrack.pdf
35. *http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf*. http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
