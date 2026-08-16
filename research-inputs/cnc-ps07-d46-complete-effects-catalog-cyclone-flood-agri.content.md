# Cyclone and Flood Agriculture Evidence Ledger

## 1. EXECUTIVE SUMMARY

- **Completeness Has A Hard Boundary**: IBTrACS records cyclone tracks and intensity, EM-DAT records major disasters and country-level losses, Dartmouth records flood footprints, and NOAA Storm Events covers the United States; none has a universal event-by-event agricultural-impact field [27][14][15][13]. -> Treat this as an evidence-bounded Version 1 ledger, not a certified census of every agricultural disaster in history.
- **Depth And Duration Drive Crop Loss**: A global meta-analysis found a mean **32.9% yield reduction** under waterlogging, with longer inundation consistently associated with lower yields [21]. -> The advisory engine must combine crop, growth stage, water depth, and duration rather than issuing a generic flood warning.
- **Compound Hazards Cause The Largest Cascades**: Cyclone Nargis combined wind, a **3.6 m storm surge**, saline flooding, livestock mortality, seed shortages, and stored-grain losses; assessed agricultural damage was **K186.344B**, with additional agricultural losses of **K385.239B to K508.310B** [36]. -> Store compound-hazard chains, not one hazard label per event.
- **Warning Lead Time Is Actionable**: IMD identified Cyclone Dana's likely development about **7.5 days before landfall** and forecast the **1-2 m** surge about **2 days before landfall** [30]. -> Separate long-lead planning rules from 48-hour actions such as moving seed, livestock, pumps, and dry grain.
- **Recovery Is Unequal**: In a 400-household, 40-village Odisha flood study, poorer households recovered less, while public assistance favored landowners; landless agricultural households lacked access to crop compensation and loan waivers [18]. -> The platform must record tenancy and landless status and route recovery advice beyond title-holding farmers.
- **Storage Safety Is A Distinct Emergency**: Flood-contact grain can be adulterated and unsafe; official guidance says it should be destroyed rather than blended, with a visible waterline used as a detection clue [35]. -> Add separate food/feed safety workflows instead of treating storage loss as ordinary crop damage.
- **Some Requested Causal Claims Are Not Yet Verified**: The research did not establish event-specific causal evidence for flood-triggered rice blast, sheath blight, foot rot, brown planthopper outbreaks, or disaster-caused farmer suicide. -> Keep these as surveillance hypotheses, not deterministic rules.
- **Flood Benefits Require Management**: Floodwater can recharge aquifers and support floodplain ecosystems when deliberately routed onto suitable land, but that is not evidence that uncontrolled disasters create net farm benefits [41][45]. -> Encode beneficial-water rules only for controlled flood-recession farming or managed aquifer recharge.
- **Last-Mile Delivery Already Has A Precedent**: Odisha's EWDS uses satellite links, digital mobile radio, mass messaging, voice, sirens, and **122 coastal alert towers**, enabling multi-level warnings to reach remote coastal communities [9]. -> Couple farm-specific SMS and IVR with existing warning infrastructure rather than creating a parallel alert network.

**Completeness status:** The literal request for every agricultural cyclone and flood incident worldwide is **NOT ACHIEVED and cannot be honestly certified from the available archives**. The ledger below contains the events for which usable evidence was extracted, while every visible gap is labeled **MISSING-DATA**. It must not be represented as a closed-world global census.

## 2. THE COMPLETE EVENT LEDGER

### Evidence grades

| Grade | Meaning |
|---|---|
| A | First-party government, official post-disaster assessment, or intergovernmental assessment with direct figures |
| B | Peer-reviewed research or authoritative technical assessment using identified data |
| C | Credible secondary reporting with attribution but incomplete methods |
| D | Event is real, but the agricultural field, action, source date, or direct evidence is absent or unverifiable |

### South Asia

| Date | Event | Country/region | Type | Agricultural damage | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| 29-30 Oct 1999 | Odisha Super Cyclone | Odisha, India | Cyclone, surge, flood | Agricultural impact is known, but a directly extractable crop-area, livestock, and value record was **MISSING-DATA** in the reviewed OSDMA material; the event dates are verified [1]. | **MISSING-DATA** | https://www.osdma.org/ ; source date **MISSING-DATA** | D for agriculture |
| 2007 monsoon | Bangladesh floods | Bangladesh | River and monsoon flood | Agricultural production losses and damaged assets were assessed near **USD1.1B** [31]. Crop-area, crop-stage, and livestock breakdowns are **MISSING-DATA**. | **MISSING-DATA** | https://documents.worldbank.org/ ; assessment date **MISSING-DATA** | A |
| 15 Nov 2007 | Cyclone Sidr | Bangladesh | Cyclone, surge, flood | Category 4 storm with winds up to **240 km/h**; agriculture damage was **BDT30.197B, or USD437.6M**, within total damage and loss of about **USD1.7B** [31]. Hectares and farmer actions are **MISSING-DATA** in the extracted record. | **MISSING-DATA** | https://documents.worldbank.org/ ; Mar 2008 assessment [31] | A |
| 26 May 2021 | Cyclone Yaas | Odisha, West Bengal, Jharkhand, India | Cyclone, surge, flood | Reported cropped area affected: **5,672.99 ha in Odisha, 170,891 ha in West Bengal, and 74.94 ha in Jharkhand** [16]. Satellite analysis estimated **1,593.06 km2** of inundated coastal land across Odisha and West Bengal [22]. | After embankment breaches damaged paddy, farmers waited for rainwater to leach and drain salt from fields [17]. | https://pib.gov.in/ ; 04 Aug 2021 [16] | A/B |
| Jun-Oct 2022 | Pakistan floods | Pakistan | Monsoon and river flood | Total damages exceeded **USD14.9B**, losses were about **USD15.2B**, and agriculture and livestock damage was about **USD3.7B** [8]. Crop-specific hectares remain **MISSING-DATA** in the extracted evidence. | Assessment priorities included emergency cash and restarting local agriculture [8]. | https://www.worldbank.org/en/news/press-release/2022/10/28/pakistan-flood-damages-and-economic-losses-over-usd-30-billion-and-reconstruction-needs-over-usd-16-billion-new-assessment ; 28 Oct 2022 | A |
| 25 Oct 2024 | Cyclone Dana | Odisha and West Bengal, India | Cyclone, surge, flood | Landfall winds were **100-110 km/h, gusting to 120 km/h**; a **1-2 m** surge inundated low-lying Kendrapara and Bhadrak, while heavy rain caused flooding [30]. IMD reports **35.95 lakh people affected** in Odisha, but crop hectares, crop value, and livestock loss are **MISSING-DATA** [30]. | About **8 lakh people** were evacuated to 6,210 relief centers, but farm-specific actions are **MISSING-DATA** [30]. | http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf ; 07 Nov 2024 | A hazard, D agriculture |

### Southeast and East Asia

| Date | Event | Country/region | Type | Agricultural damage | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| 2-3 May 2008 | Cyclone Nargis | Ayeyarwady Delta, Myanmar | Cyclone, surge, saline flood | A **3.6 m surge** contributed to **615,000 ha flooded** and about **1M acres exposed to seawater** [36]. Agriculture damage was **K186.344B** and estimated losses were **K385.239B-K508.310B** [36]. The assessment also recorded **16,200 ha of summer paddy**, **251,000 MT** of stored paddy or milled rice affected, and severe buffalo and cattle mortality [36]. | Farmers prepared fields but lacked seed and machinery; only **25%** reportedly had enough seed. Government and partners distributed seed, tillers, and buffalo [36]. | https://asean.org/ ; Post-Nargis Joint Assessment, 2008 | A |
| 8 Nov 2013 | Typhoon Haiyan/Yolanda | Philippines | Super typhoon, surge, flood | More than **600,000 ha** were damaged and approximately **1.1M tonnes of crops** were lost; agriculture damage exceeded **USD700M** [33]. Rice, corn, coconut, banana, root crops, abaca, and vegetables were affected [33]. | Farmers cleared land and replanted. Recovery supplied certified seed, fertilizer, tools, pumps, storage, and training; FAO and the Department of Agriculture implemented 22 projects for more than 230,000 households [33]. | https://www.fao.org/ ; FAO recovery assessment, publication date **MISSING-DATA** | A |
| Sep-Oct 2019 | Faxai and Hagibis | Japan | Cyclones and flood | A national agriculture value was found during discovery, but its source excerpt was not registered strongly enough for publication. Value, hectares, and crop split are therefore **MISSING-DATA**, not silently reproduced. | **MISSING-DATA** | https://www.maff.go.jp/ ; source date **MISSING-DATA** | D |

### Africa

| Date | Event | Country/region | Type | Agricultural damage | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| 14 Mar and 25 Apr 2019 | Cyclones Idai and Kenneth | Mozambique and neighboring southern Africa | Cyclone, flood | Idai destroyed more than **715,000 ha** of crops; Kenneth affected about **55,500 ha** [12]. Approximately **2.2M people** required assistance [12]. Crop and livestock value is **MISSING-DATA** in the extracted source. | Recovery planning emphasized livelihood restoration and self-reliance, but household-level actions are **MISSING-DATA** [12]. | https://www.wfp.org/ ; 2019 response documentation | A |
| 2019-2020 | Desert locust cascade | Eastern Africa and Arabian Peninsula | Cyclone/wet-weather ecological cascade | Rare cyclones and unusually wet conditions created favorable breeding conditions [44]. Some swarms contained up to **80M adults** and could consume in one day the food equivalent of about **35,000 people** [44]. This is an indirect agricultural cascade, not direct cyclone damage. | Response combined surveillance, control operations, livelihood protection, and restoration [44]. | https://www.worldbank.org/en/news/feature/2020/04/27/the-locust-crisis-the-world-bank-s-response ; 27 Apr 2020 | B |

### Americas

| Date | Event | Country/region | Type | Agricultural damage | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| Spring-summer 1993 | Great Midwest Flood | United States | River flood | About **9M agricultural acres** were unplanted, destroyed, or abandoned. Corn output was **29% below 1992** and **12% below normal**; estimated corn and soybean losses ranged from **USD2.2B to USD6.2B** [20]. Levee failures and weakening amplified exposure [20]. | Farm-level actions are **MISSING-DATA** in the extracted record. | https://www.weather.gov/dvn/071993_greatflood ; retrospective source date **MISSING-DATA** | A/B |
| Sep 2017 | Hurricanes Irma and Maria | Puerto Rico, United States | Cyclone, flood | Small farms with annual sales below **USD20,000** were especially affected [7]. Between the 2012 and 2018 agricultural censuses, farms under 10 acres declined by more than half and farms of 10-49 acres by almost one-third [7]. The entire decline must not be attributed to the hurricanes without qualification. | **MISSING-DATA** | https://www.ers.usda.gov/amber-waves/2020/september/hurricanes-irma-and-maria-are-still-affecting-puerto-rico-s-agricultural-production ; Sep 2020 | B |
| Nov 2020 | Hurricanes Eta and Iota | Honduras | Cyclone and flood | Agriculture and livestock damage was **USD70.78M**, sector losses were **USD273.53M**, and total sector effects were **USD356.91M** [43]. | The recovery framework allocated support for farmers, food, infrastructure rehabilitation, and broader recovery, but had an **88% financing gap** [43]. | https://www.iadb.org/ ; damage-and-loss assessment date **MISSING-DATA** | A |
| 26 Sep 2024 | Hurricane Helene | Georgia and southeastern United States | Cyclone and inland flood | Georgia's agriculture and forestry losses were preliminarily estimated at at least **USD5.5B in present value** [6]. Crop, county, and farm-action breakdowns are **MISSING-DATA** in the extracted evidence. | **MISSING-DATA** | https://newswire.caes.uga.edu/ ; 2024 preliminary estimate | B |

### Europe and Oceania

| Date | Event | Country/region | Type | Agricultural damage | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| 3 Feb 2011 | Cyclone Yasi | Queensland, Australia | Cyclone, surge, flood | A **5.33 m** surge was recorded at Cardwell and coastal erosion and infrastructure damage occurred [26]. A directly supported agricultural area or value is **MISSING-DATA** in the reviewed government source. | **MISSING-DATA** | https://www.qra.qld.gov.au/ ; source date **MISSING-DATA** | D for agriculture |
| 12-16 Feb 2023 | Cyclone Gabrielle | New Zealand | Cyclone and flood | Estimated on-farm revenue loss was **NZD500M-NZD1B**, affecting apples, grapes, kiwifruit, and forestry [4]. Damaged bridges interrupted goods movement, while orchard and vineyard recovery could take years [4]. | Farm-level actions are **MISSING-DATA**; the record supports long-horizon replanting and logistics needs. | https://www.treasury.govt.nz/ ; 2023 analysis, exact publication date **MISSING-DATA** | A/B |
| 3-8 Sep 2023 | Storm Daniel | Thessaly, Greece | Extreme rainfall and flood | Remote sensing mapped about **1,150 km2** inundated, of which approximately **820 km2, or 70%**, was agricultural. Cotton was the most affected crop; more than **14,000 poultry** and **21,500 sheep and goats** were affected [2]. Financial loss and farmer actions are **MISSING-DATA**. | **MISSING-DATA** | https://joint-research-centre.ec.europa.eu/ ; publication date **MISSING-DATA** | B |

**Ledger takeaway:** These rows demonstrate the attainable unit of evidence: hazard record plus impact assessment plus response record. They do not prove that unlisted events had no agricultural impact. The number of **MISSING-DATA** cells is itself a finding: even major assessments frequently omit crop stage, inundation duration, tenancy, farmer behavior, or recovery outcome.

## 3. COVERAGE TABLE

| Archive or source family | What was examined | Useful coverage | Critical gap for this task | Sweep status |
|---|---|---|---|---|
| IBTrACS | Global cyclone best-track variables | Storm ID, time, position, wind, pressure, agency, distance to land, and landfall variables [27] | No universal crop hectares, livestock, storage, farmer action, or agricultural loss field | Schema and documentation examined; **not a full row-by-row impact join** |
| EM-DAT | International disaster database | More than 27,000 mass disasters since 1900 and country-level human/economic losses [14] | Inclusion thresholds omit many local events; no universal crop-specific field. Events generally require 10 deaths, 100 affected, emergency declaration, or international assistance [14] | Documentation examined; **not a complete licensed record export** |
| Dartmouth Flood Observatory | Global flood-event archive | Large flood events from 1985 onward, with locations and affected-area outlines [15] | Excludes tropical storms without significant river flooding and does not supply standardized agriculture impacts | Documentation examined; **not a full spatial overlay with cropland** |
| NOAA Storm Events | US severe-weather database | United States event narratives and damage records, with varying historical coverage from 1950 to Apr 2026 [13] | US only; event-type coverage varies by period; crop figures and farmer actions are inconsistent | Interface/documentation examined; **not all rows downloaded** |
| IMD | India cyclone, rainfall, forecast, and warning products | City, state, district, rainfall, and cyclone APIs [32] | Designed for hazards and warnings, not a historical farm-loss ledger | Selected reports and API documentation examined |
| National records and PDNAs | OSDMA, agriculture ministries, USDA, Queensland, New Zealand, Greece, and country assessments | Best source for hectares, crop types, livestock, monetary damage, and recovery programs | Different definitions, currencies, dates, and geographic units; farmer behavior often omitted | Selected high-value assessments examined |
| FAO and partner assessments | Haiyan, locust, food-security, seed, and recovery material | Strong agricultural sector detail and intervention descriptions | Event-selective rather than globally exhaustive | Selected assessments examined |
| Peer-reviewed studies | Waterlogging, Yaas inundation, Odisha recovery | Mechanisms, causal analysis, satellite mapping, and social distribution | Study locations and definitions are heterogeneous | Selected studies examined |

**Coverage verdict:** No archive alone can satisfy the completeness mandate. A defensible system must build a reproducible join across hazard identifiers, spatial footprints, cropland maps, national damage assessments, and post-event farm surveys. Until that join is run over complete licensed exports, the phrase "complete global ledger" is not supportable.

## 4. WHAT IS MISSING

### Known events with incomplete accessible agricultural records

| Event or family | Known status | Missing fields that prevent a complete row |
|---|---|---|
| 1999 Odisha Super Cyclone | Event and date verified [1] | Crop hectares by district, crop stages, livestock, storage, saline area, value, and farmer actions |
| Cyclone Phailin, 2013 | Agricultural impact is widely reported | A registered primary-source excerpt supporting area, value, and actions was not secured; discovered secondary figures were withheld |
| Cyclone Fani, 2019 | OSDMA report located [24] | Extracted agricultural tables, farmer actions, and district-level effects |
| Cyclone Amphan, 2020 | Known agricultural and salinity impacts | Comparable primary-source hectares, salinity duration, crop values, and longitudinal recovery evidence |
| Cyclone Remal, 2024 | Known event | Verified agriculture-specific record, rather than general disaster damage |
| Faxai and Hagibis, 2019 | Japanese agriculture impacts were discoverable | A registered, auditable excerpt for the national total and crop breakdown |
| Yasi, 2011 | Surge and infrastructure effects verified [26] | Agriculture-specific hectares, crop value, and farm response |
| Local floods below EM-DAT thresholds | They necessarily exist outside major-disaster inclusion rules [14] | Event inventory, agricultural footprint, and losses |

### Requested effects without adequate event-specific evidence

The following should remain explicit **MISSING-DATA** or **UNVERIFIED** fields rather than being converted into facts:

1. Flood-caused rice blast, sheath blight, foot rot, and brown planthopper outbreaks in named disasters.
2. Hail damage as a cyclone mechanism in the events reviewed.
3. Disease-vector impacts on livestock or farm labor after named floods.
4. In-field or stored-grain sprouting rates by event.
5. Groundwater contamination magnitudes and persistence after the listed events.
6. Event-specific labor shortages, mandi closures, farm-gate price spikes, and migration totals.
7. Long-term causal estimates for land abandonment, cropping-pattern shifts, debt cycles, and farmer suicide.
8. A defensible global "typical" magnitude for any effect. Existing figures use incompatible denominators and cannot be pooled casually.
9. Quantified disaster benefits for Nile, Mekong, and Indus flood-recession agriculture; pond or tanka refill; and fish ingress into paddies. Managed-flood benefits are documented, but the requested event-by-event yield gains were not verified.

This missingness matters operationally. If the training data silently treats an absent field as zero, the model will learn that undocumented livestock, storage, tenancy, or disease losses did not happen. All absent observations therefore require a status such as `not assessed`, `assessed-none`, `inaccessible`, or `conflicting`, never a numeric zero.

## 5. PATTERNS

### Complete effect taxonomy, with evidence status

"Magnitude" below means a documented anchor, not a universal average. Where no comparable global estimate exists, the table says so.

| Effect | Mechanism | Documented cases | Magnitude anchor | Onset | Detection signal | Prevention or intervention | Evidence status |
|---|---|---|---|---|---|---|---|
| Submergence | Water excludes oxygen, impairs roots, and can bury or dislodge plants | Nargis, Yaas, Daniel | Nargis **615,000 ha** flooded; Daniel about **820 km2** agricultural inundation [36][2] | During to days | Water depth, duration, crop stage, SAR flood map | Drainage, stage-specific harvest, tolerant varieties, replant decision | Verified |
| Waterlogging | Saturated soil causes root hypoxia and yield loss | Global meta-analysis, Nargis, Pakistan | Mean **32.9%** yield reduction globally; longer duration worsens loss [21] | Hours to weeks | Soil moisture, standing-water depth, drain flow | Clear drains, controlled pumping, duration thresholds | Verified |
| Wind lodging and breakage | Wind bends stems, strips leaves, snaps trunks, and drops fruit | Haiyan coconut and mixed crops; Gabrielle orchards and vines; Nargis paddy | Haiyan: over **600,000 ha** damaged across crops [33] | During | Wind gust, crop height, canopy imagery, lodging angle | Early harvest where mature, supports, windbreak maintenance | Partly verified; lodging-specific rates missing |
| Debris or hail damage | Impact wounds plants and animals and blocks fields or drains | Debris is plausible in severe cyclones; hail-specific cyclone cases not established | **MISSING-DATA** | During | Camera/drone imagery, hail sensor, debris reports | Shelter, drain clearance, field triage | Unverified for requested cases |
| Saltwater intrusion | Surge deposits salts in soil and freshwater systems | Nargis, Yaas, Dana; Sri Lanka 2004 tsunami requested but not quantified here | Nargis about **1M acres** exposed to seawater; Dana surge **1-2 m** [36][30] | During to months or years | Soil and water electrical conductivity, chloride, surge footprint | Prevent saline entry where possible, flush with suitable freshwater, drainage, salt-tolerant crops | Verified mechanism; persistence often missing |
| Erosion and sediment movement | Fast water removes topsoil or deposits sediment | Midwest levee failures, Yasi coastal erosion, floodplain farming | No comparable global agricultural average [20][26] | During to weeks | Elevation change, turbidity, exposed roots, sediment depth | Bund repair, vegetative cover, sediment testing | Partly verified |
| Seed washout and seed scarcity | Flood removes seed or destroys planting stocks | Nargis, Haiyan, Pakistan | Only **25%** of surveyed Nargis farmers had enough seed [36] | During to next planting window | Seed-inventory check, germination test, warehouse waterline | Raised waterproof storage, reserve seed, verified seed kits | Verified |
| Livestock mortality and displacement | Drowning, debris, exposure, feed shortage, and disease | Nargis, Daniel, Idai/Kenneth | Nargis worst townships lost about **50% of buffalo** and **20% of cattle**; Daniel affected over **21,500 sheep/goats** [36][2] | During to weeks | Headcount, shelter occupancy, carcass reports, feed days | Move animals early, tagged inventories, fodder and veterinary support | Verified |
| Irrigation, bund, embankment, road, and bridge damage | Overtopping, scour, debris, and wind interrupt water control and logistics | Yaas, Midwest 1993, Gabrielle | Yaas embankment breaches damaged paddy; Gabrielle bridges disrupted goods movement [17][4] | During to months | Structural sensors, breach reports, road status | Pre-storm inspection, isolate pumps, rapid breach and access repair | Verified |
| Standing-crop and harvested-crop rot | Prolonged moisture causes tissue breakdown and spoilage | Nargis paddy and stored rice; flood-contact grain guidance | Nargis affected **251,000 MT** of stored paddy or milled rice | Immediate to days | Grain temperature, moisture, odor, discoloration, waterline | Segregate wet grain, dry only uncontaminated grain, destroy adulterated grain | Verified |
| Mold and fungal disease | High leaf wetness and humidity favor pathogens | General biological plausibility; named flood-to-blast, sheath-blight, and foot-rot cases not verified | Global event-specific typical magnitude **MISSING-DATA** | Days to weeks | Leaf wetness, humidity, lesions, extension diagnosis | Scout and confirm before treatment; avoid automatic pesticide advice | Hypothesis only |
| Pest outbreaks | Altered habitat or vegetation can favor pests; wet cyclone seasons can enable locust breeding | 2019-2020 eastern Africa and Arabia locust cascade | Swarms up to **80M**, with daily consumption equivalent to food for **35,000 people** [44] | Weeks to months | Rainfall anomaly, vegetation index, pest traps and reports | Surveillance, coordinated control, livelihood protection | Locust chain verified; brown planthopper claim unverified |
| Disease vectors | Standing water may affect vectors and animal health | No sufficiently documented agriculture-specific named cases in the reviewed evidence | **MISSING-DATA** | Days to weeks | Veterinary syndromic reports, vector traps, stagnant-water map | Veterinary and public-health referral | Unverified in this ledger |
| Premature sprouting | Wet mature grain germinates before harvest or in storage | Requested effect, but named-event evidence was not secured | **MISSING-DATA** | Days | Grain moisture and germination sampling | Timely harvest, drying, segregated storage | MISSING-DATA |
| Storage contamination and loss | Floodwater carries sewage, chemicals, and microbes into grain and feed | US flood-grain guidance; Nargis; Haiyan recovery | Visible waterline is a key clue; flood-contact grain should not be blended [35] | Immediate | Waterline, odor, moisture, contaminant assessment | Quarantine, document, destroy unsafe material, restore raised storage | Verified |
| Nutrient leaching, acidification, and fertility change | Percolating water removes nutrients; sediments and salts alter chemistry | Waterlogging literature, Nargis, Yaas | No event-comparable typical magnitude | Days to seasons | Soil pH, EC, NPK, organic carbon, sediment depth | Test before fertilizer or amendment recommendations | Mechanism credible; event values missing |
| Groundwater contamination | Saline or polluted floodwater enters shallow aquifers and wells | Nargis and Yaas are exposure candidates | Persistence and concentration **MISSING-DATA** | Immediate to months | EC, chloride, nitrate, microbial water test | Seal wells, test before use, identify safe alternative water | Insufficient quantified evidence |
| Delayed replanting and crop-calendar loss | Wet fields, destroyed seed, damaged access, or perennial losses miss planting windows | Nargis, Odisha floods, Gabrielle | Flood effects can delay the Rabi calendar [47]; Gabrielle orchards and vines can take years to recover [4] | Weeks to years | Field trafficability, seed availability, days to sowing deadline | Short-duration varieties, alternate crops, seed kits, calendar rules | Verified |
| Labor and market disruption | Displacement and damaged transport reduce labor, input, and market access | Gabrielle bridge disruption; Honduras recovery gap; Puerto Rico small-farm contraction | Global typical magnitude **MISSING-DATA** | Days to months | Road status, market opening, labor availability, farm-gate price | Alternate collection points, transport coordination, cash support | Partly verified |
| Credit, debt, and unequal recovery | Lost income and assets interact with land tenure and aid eligibility | Bhadrak 2014 flood; Honduras Eta/Iota | Poorer Odisha households recovered less; landless farmers lacked crop compensation and loan-waiver access [18] | Weeks to years | Tenure, debt, insurance, application status, recovery score | Tenant-aware eligibility, cash referral, appeal support | Verified for unequal recovery; suicide causality unverified |
| Food security and migration | Production loss, livelihood loss, and price/access shocks reduce food availability | Pakistan, Mozambique, locust crisis | Idai/Kenneth left **2.2M** needing assistance [12] | Weeks to years | Food-consumption score, displacement, wage and price tracking | Cash/food support, restart production, livelihood diversification | Food-security impact verified; migration totals missing |
| Long-term salinization, abandonment, and crop shifts | Persistent salts and repeated losses can make prior crops uneconomic | Nargis and Yaas exposure documented; requested Amphan/Sri Lanka persistence not quantified | Duration and abandoned hectares **MISSING-DATA** | Months to years | Seasonal EC trend, fallow area, crop map, land transactions | Long-term drainage, tolerant systems, monitored crop transition | Plausible but incompletely quantified |
| Groundwater recharge and floodplain fertility | Deliberately spread floodwater infiltrates aquifers and can sustain floodplain ecosystems | Upper Mekong flood-based agriculture; managed aquifer recharge | Numeric farm-yield gain **MISSING-DATA**; recharge and ecosystem functions documented [41][45] | Weeks to years | Water table, infiltration, sediment and soil tests | Controlled diversion, recharge basins, flood-compatible crops | Verified only as managed benefit |
| Reservoir, pond, and tanka refill; fish ingress | Floodwater replenishes local storage or introduces aquatic production | Requested examples were not adequately quantified in the reviewed sources | **MISSING-DATA** | Immediate to season | Storage level, water quality, fish count | Retain safe water, screen contaminants, manage integrated rice-fish systems | Evidence gap |

### Case study: Nargis shows why one loss number is inadequate

Nargis is the clearest compound-impact case in the reviewed record. The surge flooded cropland with seawater, destroyed standing and stored paddy, killed draft animals, damaged land, and left many farmers without enough seed [36]. A platform trained only on the monetary damage total would miss the sequence that determines recovery: drainage and salinity first, seed and land preparation next, then machinery and animal power.

The operational implication is a dependency graph. A replant recommendation is invalid if soil salinity remains high, seed is unavailable, or draft power has disappeared. The engine should therefore suppress generic "replant now" messages until field drainage, EC, seed, machinery, and labor conditions pass explicit checks.

### Case study: Yaas and Dana connect warning lead time to field sensing

Yaas demonstrates the agricultural pathway from embankment breach to paddy flooding and residual salinity; farmers' immediate strategy was to wait for rainfall to leach salts [17]. Dana demonstrates the warning side: cyclone development was signaled about 7.5 days ahead and the eventual surge magnitude about two days ahead [30].

Together they justify two-stage advice. The first stage checks seed, livestock, drainage, and contacts. The second, triggered by a surge forecast and geofenced low elevation, prioritizes moving dry assets and animals, isolating pumps, and protecting freshwater. After landfall, field EC and inundation duration determine whether to drain, flush, wait, or switch crops.

### Case study: Benefits depend on controlled water, not disaster optimism

Flood-based agriculture in the Upper Mekong can support floodplain ecosystems and aquifer recharge, while managed aquifer recharge intentionally diverts floodwater to suitable agricultural, working, or natural land [41][45]. These are managed systems with site selection, timing, and water-quality constraints.

The distinction prevents a dangerous model error. A filled pond or rising water table does not cancel livestock deaths, contaminated wells, erosion, or crop loss. The engine should calculate benefits only after safety checks and should never send a positive-benefit message during an uncontrolled life-safety emergency.

## 6. HOW IT FEEDS THE ENGINE

### Event history as validation data

Each ledger row should become a versioned event object, not free text. Minimum fields are: archive identifiers; time and geometry; hazard components; crop, stage, and area; depth and duration; wind and surge; soil and water salinity; livestock; seed and storage; infrastructure; market access; land tenure; reported farmer actions; intervention; recovery outcome; source; grade; and missingness reason.

Spatial validation can replay a historical event against the advisory logic. For Yaas, the model should identify coastal paddy exposed to inundation and salinity [22]. For Dana, it should generate long-lead readiness and 48-hour surge actions before the documented landfall [30]. For Nargis, it should not recommend immediate replanting when seed, machinery, animals, and soil condition remain limiting [36].

### Pattern priors and rule seeds

| Phase | Inputs | Initial rule seed | Output |
|---|---|---|---|
| T-7 days to T-72 hours | IMD development probability, district, crop calendar, farmer inventory | Verify phone/IVR language; ask crop stage, livestock, seed, dry grain, pump, and transport status | Readiness checklist and escalation path |
| T-48 to T-6 hours | Track, wind, rainfall, surge, elevation, embankment proximity | If surge or deep flooding is plausible, move seed and safe grain above expected water, shift livestock, isolate equipment, open safe drainage, harvest only when maturity and worker safety permit | Short prioritized SMS plus IVR confirmation |
| During event | Water level, official evacuation, power status | Life safety overrides crop protection; stop field work in dangerous wind or moving water | Evacuation and shelter message |
| T+0 to T+72 hours | Depth, duration, waterline, crop image, livestock count, road status | Quarantine flood-contact grain; report carcasses and breaches; do not prescribe fertilizer or pesticide before diagnosis | Safety triage and damage capture |
| T+3 to T+14 days | Soil EC/pH, leaf wetness, pest observations, seed inventory | Drain where safe; test saline fields and water; scout disease and pests; match replanting to the remaining calendar | Field-specific recovery plan |
| Weeks to months | Market access, seed supply, tenancy, credit, recovery monitoring | Route tenant and landless households to eligible assistance; revise crop choice when the planting window has closed | Livelihood, market, and finance referrals |
| Seasons to years | EC trend, crop maps, repeated losses, groundwater | Identify persistent salinity, abandonment risk, and safe managed-recharge opportunities | Adaptation and cropping-system change |

The priors must remain conditional. The **32.9%** waterlogging mean is useful as a starting prior, but it is not a prediction for an Odisha field because crop, stage, depth, temperature, and duration change the outcome [21]. Local observations should update the prior, with uncertainty shown to agronomists even if the farmer receives a simple action message.

### SMS and IVR design

Odisha already has mass messaging, voice, sirens, satellite links, and coastal alert towers [9]. The farm layer should add geofencing and a small number of urgent actions:

> CYCLONE RED. Move seed and safe dry grain above flood level. Shift cattle to the named shelter. Switch off and secure the pump. Do not enter moving water. Reply 1 when done, 2 for help.

The IVR should speak the same message slowly in the selected local language, repeat on keypress, and use one-key responses. The system should avoid jargon such as "electrical conductivity"; it can instead ask whether a field-water test showed green, amber, or red. Every advisory should include issue time, location, hazard window, action, and a callback or escalation option.

## 7. REAL-vs-FILLER + NOISE LOG

| Claim encountered | Classification | Decision |
|---|---|---|
| Waterlogging reduces crop yield, with loss increasing as duration increases | **REAL** | Supported by meta-analysis [21]; use as a conditional prior |
| Yaas embankment breaches damaged paddy and farmers waited for rain to reduce salinity | **REAL** | Supported by attributed district reporting [17]; retain with source grade C |
| Nargis caused simultaneous crop, seed, storage, livestock, and saline-land losses | **REAL** | Supported by the joint assessment [36] |
| Rare cyclones and wet weather helped create desert-locust breeding conditions | **REAL BUT INDIRECT** | Retain as a compound ecological cascade, not direct storm damage [44] |
| Floods automatically cause rice blast, sheath blight, foot rot, or brown planthopper outbreaks | **FILLER/OVERCLAIM** | No adequate named-event causal evidence was secured; keep only as a monitored risk |
| East Africa's outbreak can be assigned to particular named cyclones without qualification | **OVER-SPECIFIC** | Source supports rare cyclones and wet weather generally, not the full named-storm chain |
| Cyclone or flood exposure directly caused farmer suicide | **UNVERIFIED CAUSAL CLAIM** | Do not encode or publish without event-linked epidemiological evidence |
| Yaas, Amphan, or the 2004 Sri Lanka tsunami produced a universal salinity duration of "one month+" | **PARTIAL** | Saline exposure is documented for Yaas and Nargis, but comparable persistence values were not secured |
| Nile, Mekong, or Indus floods always improve soil fertility | **FILLER/OVERGENERALIZATION** | Benefits depend on sediment quality, depth, timing, erosion, contamination, and management |
| Fish ingress into paddies gives a documented general yield gain after disasters | **MISSING-DATA** | Do not use until event-specific production and counterfactual evidence is available |
| An absent field in EM-DAT or a PDNA means zero agricultural loss | **FALSE** | Encode as missing, not zero; archive purposes and fields differ [14] |
| The event table above is the complete global history | **FALSE** | Archive schemas and incomplete full-export access prevent certification [27][15][13] |

This log is not cosmetic. It separates facts that can seed deterministic rules from claims that should trigger data collection or agronomist review. It also prevents a language model from converting frequently repeated web statements into false certainty.

## 8. VERDICT

The evidence supports building the proposed Odisha platform. IMD can provide actionable lead time, Odisha already has a robust last-mile warning backbone, and the reviewed events supply rule seeds for inundation, salinity, livestock, seed, storage, infrastructure, market access, and unequal recovery [30][9][36]. The strongest design is not a single damage-prediction model. It is a staged decision system that joins official hazards with crop stage, field elevation, drainage, soil EC, inventories, livestock, tenancy, and road or market status.

The evidence does **not** support labeling this report "the complete global ledger of agricultural disaster history." Doing so would convert unknowns into omissions and omissions into implied zeros. The defensible product is a living, versioned evidence ledger with explicit missingness, source grades, reproducible archive queries, and scheduled backfills. Its success metric should be fewer unsafe or mistimed recommendations, not the unsupported assertion that no historical event was missed.

The immediate implementation decision is therefore **GO, with conditions**:

1. Use IMD warning feeds and OSDMA delivery channels as the operational spine.
2. Pilot district-specific rules for surge, waterlogging duration, seed and grain protection, livestock movement, and salinity testing.
3. Require every historical and live observation to carry a source grade and missingness code.
4. Keep fungal, pest, suicide, migration, and positive-effect claims in an evidence-review queue until event-specific support exists.
5. Build the global ledger through reproducible archive exports and spatial joins, not narrative web searching alone.

## Synthesis

| Evidence or strategy layer | Mechanism and scope | Main strength | Trade-off | Evidence horizon |
|---|---|---|---|---|
| Global hazard archives | Identify when and where cyclones and floods occurred | Broad geographic and temporal coverage | Weak agricultural specificity; differing inclusion rules | Hours to more than a century |
| National and intergovernmental assessments | Quantify hectares, crops, livestock, infrastructure, and money | Deep event detail, as shown by Nargis, Sidr, Pakistan, and Honduras | Selective, slow, and methodologically inconsistent | Weeks to months after an event |
| Farm and remote-sensing observations | Measure depth, duration, salinity, crop stage, and visible damage | Hyperlocal and suitable for advisory validation | Sensors fail, clouds and access constrain observations, and farmer reports require quality control | Minutes to seasons |
| Rule-based advisory engine | Converts hazard and farm state into timed actions | Transparent, auditable, and suitable for SMS/IVR | Brittle if missing data are treated as facts or generic rules ignore crop stage | Before, during, and after each event |
| Statistical or AI models | Estimate missing impacts and rank actions | Can combine complex patterns and update from new cases | Historical bias, archive missingness, and false causal inference | Improves over repeated seasons |
| Managed-flood adaptation | Uses controlled water for recharge or flood-compatible production | Can transform some floodwater into a resource [41][45] | Unsafe if generalized to uncontrolled, saline, polluted, or fast-moving floodwater | Seasons to years |

The central tension is breadth versus decision quality. IBTrACS, EM-DAT, Dartmouth, and NOAA provide breadth, but the records that matter to a farmer are depth, duration, crop stage, seed status, animal location, salinity, and access. Conversely, a detailed farm survey can explain recovery but covers only a small place and period. The architecture should preserve both scales rather than forcing one source to do the other's job.

A second tension is speed versus certainty. Dana shows that useful warnings can arrive days before landfall [30], while salinity, disease, and long-term livelihood outcomes require field tests and follow-up. Pre-event advice should therefore rely on conservative, low-regret actions. Post-event advice can become more specific as depth, duration, EC, crop condition, road access, and household constraints arrive.

Finally, physical recovery and social recovery diverge. A field may drain while a tenant still lacks seed, credit, compensation, machinery, or market access. The Bhadrak evidence shows why agronomic recovery cannot stand alone [18]. A genuinely resilient platform must combine field recommendations with entitlement, finance, veterinary, market, and transport referrals.

## References

1. *1999 Super Cyclone - Odisha State Disaster Management Authority*. https://www.osdma.org/publication/1999-super-cyclone/
2. *Storm Daniel flood impact in Greece in 2023: mapping crop ...*. https://nhess.copernicus.org/articles/24/2375/2024
3. *The Impact of Disasters on Agriculture and Food Security*. https://www.fao.org/publications/fao-flagship-publications/the-impact-of-disasters-on-agriculture-and-food-security/en
4. *Cyclone Gabrielle’s impact on the New Zealand economy and ...*. https://www.mfat.govt.nz/assets/Trade-General/Trade-Market-reports/Cyclone-Gabrielles-impact-on-the-New-Zealand-economy-and-exports-March-2023.pdf
5. *Desert Locust crisis | FAO Emergency and Resilience | Food ...*. https://www.fao.org/emergencies/where-we-work/desert-locust-crisis
6. *Hurricane Helene Impact Report - fieldreport.caes.uga.edu*. https://fieldreport.caes.uga.edu/wp-content/uploads/2025/08/AP-133-1_1.pdf
7. *Puerto Rico’s Agricultural Economy in the Aftermath of ...*. https://www.ers.usda.gov/publications/106260
8. *Pakistan: Flood Damages and Economic Losses Over USD 30 ...*. https://www.worldbank.org/en/news/press-release/2022/10/28/pakistan-flood-damages-and-economic-losses-over-usd-30-billion-and-reconstruction-needs-over-usd-16-billion-new-assessme
9. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Early Warning Dissemination System (EWDS)*. https://osdma.org/preparedness/early-warning-communications/ewds
10. *Entry Criteria | EM-DAT Documentation*. https://doc.emdat.be/docs/protocols/entry-criteria
11. *Global Active Archive of Large Flood Events (DFO) | Humanitarian Dataset | HDX*. https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo
12. *2018-2019 Mozambique Humanitarian Response Plan Revised following Cyclones Idai and Kenneth, May 2019 (November 2018 - June 2019) | OCHA*. https://www.unocha.org/publications/report/mozambique/2018-2019-mozambique-humanitarian-response-plan-revised-following-cyclones-idai
13. *Storm Events Database | National Centers for Environmental Information*. https://www.ncei.noaa.gov/stormevents
14. *EM-DAT - The international disaster database*. https://www.emdat.be/
15. *Dartmouth Flood Observatory*. https://floodobservatory.colorado.edu/Archives
16. [
	Press Release Page | Press Information Bureau
](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1742311)
17. *Cyclone Yaas aftermath: Odisha farmers in a fix over sowing Kharif crop*. https://downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568
18. *Flood shocks and post-disaster recovery of households: An empirical analysis from rural Odisha, India - ScienceDirect*. https://sciencedirect.com/science/article/pii/S2212420923005502
19. *Daily Events*. https://agritech.tnau.ac.in/daily_events/2014/english/june/18_june_14_eng.pdf
20. [
Assessing the Midwest Flood - Federal Reserve Bank of Chicago    ](https://www.chicagofed.org/publications/chicago-fed-letter/1993/december-76)
21. *Frontiers | How Does the Waterlogging Regime Affect Crop Yield? A Global Meta-Analysis*. https://frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.634898/full
22. *Cyclone Yaas: A Curse to Coastal People of Odisha and West Bengal (India) | National Academy Science Letters | Springer Nature Link*. https://link.springer.com/article/10.1007/s40009-023-01251-w
23. *Ouat, Bhubaneswar*. https://www.icar-crida.res.in/CP/Orissa/OUAT,%20Bhubaneswar/Orissa%2028-%20Kendrapara%2004.10.2011.pdf
24. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
25. *FAO Knowledge Repository*. https://openknowledge.fao.org/bitstreams/8c280725-85ef-4892-9170-cc646f40e4a6/download
26. *Tc Yasi*. https://www.publications.qld.gov.au/dataset/19c20822-f29e-494c-880a-113ccd13a04b/resource/3bf0ac2c-565a-4400-8d5b-6a4c15236c82/download/tc-yasi.pdf
27. *IBTrACS v04 column documentation*. http://ncei.noaa.gov/sites/default/files/2021-07/IBTrACS_v04_column_documentation.pdf
28. *IMD APIs | India Meteorological Department*. http://mausam.imd.gov.in/responsive/apis.php
29. *fao.org*. https://www.fao.org/4/x9178e/x9178e.htm
30. *Severe Cyclonic Storm “DANA” over the Bay of Bengal (22 -26 October, 2024): A Report (b) (a)*. https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
31. *Microsoft Word - SidrReport_Mar07.doc*. https://www.gfdrr.org/sites/default/files/2275_CycloneSidrinBangladeshExecutiveSummary.pdf
32. *IMD API Reference*. http://api.imd.gov.in/public/api_reference.html
33. *openknowledge.fao.org*. https://openknowledge.fao.org/server/api/core/bitstreams/b221a6a9-8952-4deb-9e69-38ada7cd1442/content
34. *International Best Track Archive for Climate Stewardship (IBTrACS) | National Centers for Environmental Information (NCEI)*. http://ncei.noaa.gov/products/international-best-track-archive
35. *Management Guidance for Flooded Grain | Integrated Crop Management*. https://crops.extension.iastate.edu/cropnews/2024/06/management-guidance-flooded-grain
36. *FOREWORD*. https://www.gfdrr.org/sites/default/files/GFDRR_Myanmar_Post-Nargis_Joint_Assessment_2008_EN.pdf
37. [
	First-ever global estimation of the impact of disasters on agriculture
](https://www.fao.org/newsroom/detail/first-ever-global-estimation-of-the-impact-of-disasters-on-agriculture/en)
38. *openknowledge.fao.org*. https://openknowledge.fao.org/server/api/core/bitstreams/069ceb86-59b2-4b6e-90e0-b7bd26a58c76/content
39. *Damage and loss*. https://www.fao.org/interactive/disasters-in-agriculture/en
40. [
            Salinity dynamics in the Sundarbans of Bangladesh: influence of climate, freshwater inflow, and sea level changes - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC12537767)
41. *Flood-based agriculture in the Upper Mekong Delta | PANORAMA*. https://panorama.solutions/en/solution/flood-based-agriculture-upper-mekong-delta
42. [
	Six months after disaster, Philippine farmers bring in the harvest
](https://www.fao.org/newsroom/detail/Six-months-after-disaster-Philippine-farmers-bring-in-the-harvest/ar)
43. *Case Study Honduras Eta And Iota Ldwksp1*. https://unfccc.int/sites/default/files/resource/Case_Study_Honduras_Eta%20and_Iota_LDwksp1.pdf
44. *The Locust Crisis and the World Bank Group*. https://www.worldbank.org/en/topic/agriculture/brief/the-locust-crisis-and-the-world-bank-group
45. *Flood-Managed Aquifer Recharge (Flood-MAR)*. https://water.ca.gov/Programs/All-Programs/Flood-MAR
46. *Farm Damage by 2 Powerful Typhoons in Japan Hits 253 B. Yen*. https://sp.m.jiji.com/english/show/1092
47. *http://tandfonline.com/doi/full/10.1080/10106049.2024.2356841*. http://tandfonline.com/doi/full/10.1080/10106049.2024.2356841
