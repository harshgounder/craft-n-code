# Odisha Cyclone-Flood Data: What the Advisory Can Use

## 1. EXECUTIVE SUMMARY

- **Overall Verdict**: The evidence supports a **PARTIAL** prototype today. Free public sources can drive subdivision-level weather alerts, historical flood-risk overlays, weekly reservoir context, mandi-price monitoring, and rule-based rice advice. They cannot yet supply a documented production API for every warning source, plot-level flood depth-duration, or verified field salinity. Build the first version with public feeds plus farmer and extension-worker reports, but design partner interfaces from day one [8][7][3].
- **Warning Stack Is Real But Integration Is Fragile**: IMD publishes dated Odisha warnings, CWC operates a flood-forecast portal, and CWC publishes reservoir-storage reports every Thursday [8][7][3]. However, the reviewed public pages do not document a stable, free, production-grade API, schema, service-level agreement, or redistribution terms -> use resilient page/file adapters for the demo and seek formal data access for deployment.
- **Storm Surge Remains Partner-Gated**: INCOIS has a public storm-surge information service, and its 2024 technical work uses downscaled ADCIRC+SWAN outputs [1][26]. What is missing publicly is the farm-ready operational object: forecast surge height, timestamped inland-inundation polygon or raster, uncertainty, and stable API endpoint for each Odisha landfall -> obtain a direct INCOIS/IMD feed rather than infer surge from wind speed.
- **Yaas Proves Persistent Saline Inundation, Not a Recovery Curve**: One month after Cyclone Yaas, at least **5,882 ha** in five Balasore blocks and about **1,400 ha** in three Bhadrak blocks were reported affected by seawater; some land remained inundated and farmers feared salt deposits would prevent kharif sowing [15]. OUAT and ICAR-NRRI sampled affected soils, but the article publishes no electrical-conductivity results or dated recovery series [15] -> the engine must request EC tests before recommending sowing or gypsum, not declare land recovered after a fixed number of days.
- **Waterlogging Advice Can Be Stage- and Duration-Aware Only With Farm Inputs**: A randomized evaluation across **128 villages** in Balasore and Bhadrak found Swarna-Sub1 resilient to submergence for up to **2-3 weeks** [16]. Following the 2011 flood, access raised total rice yield by **10.5%**; a 10-day flood corresponded to a **628 kg/ha** averted loss and a **45%** yield advantage [16] -> store variety, sowing/transplant date, growth stage, flood start, flood end, and maximum depth for every enrolled plot.
- **Pest And Disease Alerts Must Be Condition-Based, Not Day-After-Flood Claims**: Rice-blast evidence identifies long leaf wetness, high relative humidity, and **17-28 C** as favorable [19]. Sheath blight is associated with tillering through heading and begins near the water line [18]. The reviewed brown-planthopper, blast, and sheath-blight sources do not provide a universal outbreak day after a flood -> trigger scouting from crop stage plus humidity, temperature, standing water, canopy density, and farmer observations.
- **The Strongest Recovery And Claim Evidence Is Historical**: The 2019 Fani DLNA recorded **108,220 ha** of annual and perennial crops affected, crop and infrastructure damage of **INR 363.54 crore**, and crop-production losses of **INR 1,304.58 crore** [23]. It also recorded polluted ponds, temporary water-supply failure, lost workdays, wage losses, credit constraints, and migration [23] -> use its categories to design a claim packet, but collect event-specific evidence rather than treating 2019 values as current risk coefficients.
- **Positive Use Is Plausible But Often Overclaimed**: Odisha reported **16,468 check dams** covering **181,339 ha** by March 2024, while 600 MATY 2.0 dams created 15,204 ha of ayacut [10]. A Koraput-Nabarangpur integrated-farming project began with 20 aquaculture farmers, reported nearly double income relative to monocropping, and expanded to 193 farmers [11]. These findings support pond/check-dam and supplemental-irrigation advice, but they do not measure recharge caused by a named flood, silt-driven yield gains, or post-cyclone pond safety -> label those outcomes "unmeasured" until sensors or partners supply evidence.

## 2. DATA INVENTORY

**Reliability scale:** **A** = official operational data or strong primary evidence; **B** = official assessment, peer-reviewed study, or well-designed evaluation with transfer limits; **C** = credible secondary report or project case study; **D** = absent, decorative, unverified, or unusable for an automated decision.

| Data item / sub-question | Named source, URL, and date | Granularity | Freshness | Access path | Grade |
|---|---|---|---|---|---|
| Cyclone, heavy-rain, thunderstorm, lightning, and squall warning | IMD, "Warnings for Odisha," https://mausam.imd.gov.in/imd_latest/contents/subdivisionwise-warning_mc.php?id=10; captured issue date **2026-08-14** [8] | Odisha meteorological subdivision; day-wise outlook | Daily/current page | Free webpage; no stable API contract found | A for warning, C for integration |
| River flood forecast | CWC Flood Forecast portal, https://ffs.india-water.gov.in/; current service [3] | Forecast station/basin, not farm plot | Near-event portal; exact machine refresh not documented in reviewed page | Free web portal; production API not established | A for official status, C for ingestion |
| Reservoir level and storage | CWC, https://cwc.gov.in/en/reservoir-level-storage-bulletin; weekly every Thursday [7] | Reservoir and state/region bulletin | Weekly | Free report/file page | A |
| Storm-surge mechanism | INCOIS, "About Storm Surge," https://tsunami.incois.gov.in/TEWS/AboutStormSurge.jsp; current public explainer [1] | Coast/event concept | Static | Free webpage | B for mechanism, D for plot trigger |
| Surge and coastal-inundation model | INCOIS, "Enhancement of Coastal Flood Inundation Forecasting..." technical report, 2024, https://incois.gov.in/documents/Reports/TechnicalReports/TR_ESSO-INCOIS-OMARS-TR-07(2024)_20250701122038.pdf; ADCIRC+SWAN downscaling [26] | Model grid/coastal domain; not exposed as enrolled-farm records | Research/report | Free report; operational raster/API requires partner confirmation | B |
| Historical surge verification | IMD, "Verification of Storm Surge Associated with Tropical Cyclones over North Indian Ocean," covering cyclone cases through 2023, https://rsmcnewdelhi.imd.gov.in/images/storm_surge.pdf [22] | Cyclone and coastal sector | Historical | Free PDF | B; not a live Odisha feed |
| Historical flood susceptibility | NRSC/NDEM Flood Hazard Atlas service, https://ndem.nrsc.gov.in/hydrological_fhz.php [27] | Hazard zone/map, not field depth-time series | Historical aggregation | Free public map/service page | A for planning, C for event response |
| Local crop and irrigation profile | Government of Odisha e-Chasa Crop Survey, https://echasa.odisha.gov.in/; designed to record crops and irrigation across farmland [17] | Potentially parcel/farm | Seasonal survey; public update metadata not visible | Portal; bulk/API access not demonstrated, likely department partnership | B if access is granted, D for open ingestion |
| Soil-health record | Government of India Soil Health Card, https://www.soilhealth.dac.gov.in/soilhealthcard; farmer lookup interface [21] | Farmer/sample | Irregular sampling cycle | Free individual lookup; no verified bulk API in reviewed interface | A for a retrieved test, C for integration |
| Hyperlocal rain, wind, water depth, and soil EC | No complete public Odisha farm network located | Plot/sensor | Required at 5-60 minute or daily intervals | **Field collection** using rain gauge, water-depth staff/sensor, EC meter, anemometer, and farmer IVR | D until collected |
| Yaas seawater intrusion extent | Down To Earth, "Cyclone Yaas aftermath," 2021-06-21, https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568 | Five Balasore blocks and three Bhadrak blocks | One post-event snapshot | Free article/report | C |
| Yaas salinity duration | Same source: effects and saline inundation still reported one month after the cyclone [15] | Village/block narrative | One-month observation | Free report; no machine data | C |
| Plot EC and salinity-recovery trajectory | OUAT and ICAR-NRRI reportedly sampled affected soil, but no public dated results were found; the article names the sampling activity [15] | Needed by plot, depth, and date | Missing | Partner data or new field collection | D |
| Rain and waterlogging extent | IMD rain warning plus NRSC flood products | Subdivision and mapped inundation footprint | Daily warning or event map | Free pages/maps; no joined plot-depth-duration series | B for extent, D for duration |
| Crop damage by flood duration and variety | J-PAL, "Reducing Farmers' Risk through Flood-Tolerant Rice in India," 2011-2013 evaluation, https://www.povertyactionlab.org/evaluation/reducing-farmers-risk-through-flood-tolerant-rice-india | 128 villages, 64 treatment and 64 comparison, Balasore and Bhadrak [16] | Historical experiment | Free research page | A/B |
| Crop-stage-specific flood damage | J-PAL supports variety-duration effects, but no statewide crop-stage loss table was found | Village trial, not all Odisha crops/stages | Historical and incomplete | Research report plus local calibration | C |
| Wind lodging and uprooting | OSDMA, "Cyclone Fani 2019 Odisha DLNA," https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf | District/sector aggregates | Event snapshot | Free official PDF | B; no plot wind vector or lodging percentage |
| Total Fani crop exposure and loss | Same DLNA: **88,486 ha annual crops**, **19,734 ha perennial crops**, and **INR 1,304.58 crore** production loss [23] | Affected districts/sector | 2019 event | Free report | B |
| Lightning | IMD subdivision warning page | Subdivision/day | Daily warning | Free webpage | A for broad warning, D for strike-level farm history |
| Tornado or cyclone-embedded vortex | No authoritative Odisha event feed, probability layer, or farm-ready archive found | Needed as track/polygon/time | Missing | IMD/academic partner or field verification | D |
| Brown planthopper risk | IRRI Rice Knowledge Bank, "Planthopper," http://www.knowledgebank.irri.org/training/fact-sheets/pest-management/insects/item/planthopper | Crop-stage and field-condition guidance | Static extension knowledge | Free webpage | B |
| Rice blast risk | Asibi et al., "Rice Blast," 2019; favorable leaf wetness, humidity, and 17-28 C [19] | Field conditions, not Odisha plot | Static research | Free article | B |
| Sheath-blight risk | TNAU Agritech, "Sheath Blight"; tillering-heading and symptoms near water line [18] | Crop-stage guidance | Static | Free extension webpage | B |
| Fixed post-flood outbreak dates | No reviewed source supports "blast on day X," "BPH on day Y," or "sheath blight on day Z" for Odisha | Needed by plot and event | Missing | Local surveillance labels from OUAT, ICAR-NRRI, KVKs, and farmers | D |
| Pond and drinking-water disruption | Fani DLNA: **1,088 of 2,229** rural piped-water schemes affected; supply was severely hindered for two to three days in some areas [23] | Seven most-affected rural districts | 2019 event | Free official PDF | B |
| Pond/well contamination | Fani DLNA: debris blocked sewage and polluted ponds; tube wells and private wells were disinfected [23] | Assessment narrative, not lab samples | 2019 event | Free report | B for occurrence, D for concentration/duration |
| Market prices and arrivals | CEDA Agri Market Data using Ministry of Agriculture data, https://agmarknet.ceda.ashoka.edu.in/; daily, monthly, and yearly price and arrival views/downloads [28] | Mandi, commodity, district/state | Daily series | Free portal/download | B |
| Official current mandi-price resource | data.gov.in, https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi | Market-commodity-day | Current resource | Free resource page; API quota/schema should be tested | A/B |
| Mandi closure, road blockage, and transport time | No joined statewide live feed found; Fani DLNA provides post-event sector totals | Needed by road segment/mandi/hour | Missing live data | Field reports, Works Department, OSDMA, market committees, and logistics partners | D live, B historical |
| Labor and wage loss | Fani DLNA: **48.61 lakh** affected workers, **679.08 lakh person-days** lost, and **INR 2,779.50 crore** wage loss [23] | Sector/state assessment | 2019 snapshot | Free report | B |
| Agriculture and fisheries labor | Fani DLNA: agriculture/allied activities lost **95,77,803 person-days** and **INR 306.65 crore**; fisheries lost **11,84,738 person-days** and **INR 13.47 crore** [23] | Sector aggregate | 2019 | Free report | B |
| Credit and debt stress | Fani DLNA reports fishermen using private moneylenders at high interest because formal credit was inadequate [23] | Qualitative household/sector observation | 2019 | Free report | B/C |
| Migration | Fani DLNA reports fishermen migrating, but supplies no migration count or duration [23] | Qualitative | 2019 | Free report | C |
| Farm-pond water capture | Down To Earth, Koraput-Nabarangpur integrated-farming case, 2026-07-01, https://www.downtoearth.org.in/agriculture/how-rainwater-harvesting-is-turning-seasonal-farming-into-year-round-livelihoods-in-this-odisha-district | Pilot of 20, later 193 farmers [11] | Recent project report | Free article; project records by partner | C |
| Flood-attributable groundwater recharge rate | No Odisha study located that gives recharge volume or water-table rise caused by a named major flood | Needed by aquifer/block/event | Missing | CGWB/DoWR monitoring wells plus event water balance | D |
| Reservoir/check-dam water availability | Odisha Department of Water Resources Annual Report 2023-24, https://dowr.odisha.gov.in/sites/default/files/2025-07/WR_AR-23-24.pdf | Scheme, structure, ayacut | Annual | Free PDF/report | A |
| Check-dam irrigation potential | Same report: **16,468 dams**, **181,339 ha** covered by March 2024; 600 MATY 2.0 dams created 15,204 ha of ayacut [10] | Structure/program | Annual | Free report | A for assets, C for event-specific available water |
| Flood-silt fertility and contamination | No Odisha/Mahanadi field panel found linking a named flood's sediment nutrients or contaminants to the following crop's yield | Needed by deposit sample/plot/season | Missing | Soil and sediment sampling | D |
| Community seed banks | Odisha reports describe indigenous-variety conservation, including a festival credited with saving 60 varieties, but not post-cyclone seed delivery or yield outcomes [29] | Community/case | Occasional narrative | Free article/case material | C for conservation, D for disaster response |
| CHHATA/ARUA rainwater and aquifer schemes | Odisha DoWR Annual Report 2023-24; schemes began in 2022-23 to capture rooftop water and route surplus pond/tank water toward aquifers [10] | Scheme/site | Annual | Free report; site data may require department access | A for scheme existence, C for measured outcomes |

**Inventory takeaway:** The public stack is strongest at broad warnings, historical impact categories, prices, and water-infrastructure inventory. It becomes weakest precisely where a farm advisory needs causal precision: field depth-duration, crop stage, soil EC, water quality, road accessibility, and verified post-event outcomes.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing fields | Coverage judgment |
|---|---|---|---|
| IMD weather and cyclone products | Dated Odisha warnings; rain, storm, lightning, and squall context [8] | No reviewed open API contract, farm polygon, observed lodging, or strike history | **B** |
| INCOIS/IMD surge sources | Surge mechanism, verification reports, ADCIRC+SWAN technical work [1][26] | No verified production endpoint delivering Odisha farm-ready height, inland polygon, uncertainty, and timestamps | **C** operationally |
| CWC hydrology and storage | Flood portal and weekly reservoir bulletin [7][3] | Station-to-plot translation, local drainage, and depth-duration remain absent | **B** |
| NRSC/NDEM remote sensing | Historical flood-hazard and inundation mapping [27] | Cloud/revisit limitations, depth generally absent, and public plot time series not established | **B** for planning, **C** for immediate advice |
| Odisha farm and soil systems | e-Chasa crop/irrigation survey and Soil Health Card lookup [17][21] | Bulk access, identifiers, consent, current crop stage, and post-cyclone EC are not publicly exposed | **C** |
| Agronomic evidence | Swarna-Sub1 randomized evidence plus pest/disease condition guides [16][19][18] | Limited crops/varieties/stages; no Odisha event-relative pest clock | **B** |
| Damage and needs assessments | Fani DLNA provides crop, WASH, labor, market, credit, and migration categories [23] | Retrospective, aggregated, and not a live operational feed | **B** |
| Market and transport | Daily mandi prices/arrivals; Fani market and wage-loss totals [28][23] | Mandi closure, road passability, truck time, local stocks, and farm-gate prices missing | **C** |
| Positive-use water evidence | Check-dam assets and ayacut; farm-pond project outcomes [10][11] | No named-flood recharge coefficient, safe pond-water test, or event-specific rabi attribution | **C** |
| Seed, silt, and soil recovery | Some seed-diversity cases; Yaas saline-area report [29][15] | No seed viability/inventory feed, sediment nutrient panel, or salinity-recovery curve | **D** for automation |
| Lightning and tornadoes | Broad IMD lightning warning | No official farm-scale strike history or tornado/vortex archive found | **D** hyperlocally |

**Coverage judgment:** Official agencies describe the hazard and major impacts well, while farm-level state transitions are poorly observed. The product should therefore be built as a **hybrid evidence system**, not as an AI model that pretends broad alerts are hyperlocal truth.

## 4. WHAT IS MISSING

The following gaps remained after targeted searches of IMD, INCOIS, CWC, OSDMA, NRSC/NDEM, Odisha agriculture and water departments, ICAR-NRRI, research literature, and market-data portals:

1. **Production warning API and rights layer**: a documented IMD/INCOIS/CWC endpoint, schema, authentication process, redistribution rights, latency, uptime, versioning, and failure protocol suitable for SMS/IVR automation.
2. **Farm-to-hazard spatial join**: surveyed farm polygon or reliable coordinates linked to cyclone track, surge raster, river forecast, drainage catchment, embankment, and evacuation route.
3. **Storm-surge farm object**: predicted surge height, astronomical tide, wave setup, inland penetration, arrival time, duration, uncertainty, and update history for each coastal plot.
4. **Continuous flood depth-duration**: plot-level start time, peak depth, drainage time, and number of complete and partial submergence hours. A flood footprint alone does not answer this.
5. **Current crop state**: crop, variety, sowing/transplant date, phenological stage, plant height, expected harvest date, field bund/drainage condition, and stored-input inventory.
6. **Wind-loss calibration**: plot-level peak gust, gust duration/direction, lodging percentage, stem breakage, fruit drop, tree uprooting, and crop-stage response.
7. **Official lightning and tornado layer**: strike coordinate/time/confidence and any verified tornado or cyclone-embedded vortex track. Subdivision warnings are not a substitute.
8. **Yaas salinity-recovery curve**: EC or ECe, pH, sodium adsorption ratio, chloride, sampling depth, GPS point, crop threshold, rainfall/leaching, and repeated measurement date from impact through recovery.
9. **Odisha post-flood pest clock**: labeled observations connecting flood recession to first detection and economic threshold for blast, BPH, sheath blight, rodents, snails, and other locally relevant threats.
10. **Seed degradation record**: seed lot, crop/variety, storage location, flood depth and duration, moisture, germination percentage, fungal contamination, quantity recoverable, and replacement need.
11. **Pond and groundwater safety series**: salinity, turbidity, fecal contamination, nitrate, EC/TDS, sampling time, source type, disinfection, and date safe for irrigation, livestock, aquaculture, or drinking.
12. **Live market-access series**: mandi open/closed status, arrivals, farm-gate price, road passability, bridge damage, travel time, truck availability, cold-store power status, and spoilage.
13. **Household financial trajectory**: loan source, rate, repayment date, insurance/claim status, emergency borrowing, wage days lost, migration destination, duration, and return date.
14. **Flood-attributable recharge**: pre-event and post-event monitoring-well level, specific yield, recharge volume, aquifer, rainfall, river stage, and attribution method.
15. **Silt benefit-risk panel**: deposit depth, particle size, N-P-K and organic carbon, salinity, pathogens and metals, removal cost, next-season treatment, and crop yield relative to an unaffected control.
16. **Disaster seed-bank performance**: pre-event inventory, protected quantity, germination, households served, delivery time, planted area, and harvest outcome.
17. **Claim-ready provenance**: immutable alert snapshot, farm identity/consent, event time, geotag, crop-before/crop-after evidence, surveyor identity, loss calculation, and submission/decision status.

These are not minor feature gaps. They are the variables that separate a general warning broadcast from a defensible farm advisory and claim record.

## 5. HOW IT FEEDS THE ENGINE

The engine should implement an **Observation -> Mechanism -> Implication -> Recommendation** chain. A rule must not fire merely because a cyclone exists; it should fire because a known hazard overlaps a known farm state within a relevant time window.

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD warning and cyclone bulletin | Set urgency, delivery time, hazard wording, harvest/secure-input window | Preserve alert history; time first safety check | Official event timestamp and warning level | Compare recurring warning windows | Schedule safe pond/check-dam preparation before rain |
| Surge/inundation forecast | Move seed, fertilizer, machinery, livestock, and pumps above predicted reach; evacuate when directed | Do not enter saline or contaminated water; delay sowing pending EC | Predicted coastal exposure layer | Select salinity-tolerant crops only after soil confirmation | Route only safely captured freshwater; never promote direct use of saline surge |
| CWC river forecast | Clear field drains if safe; move portable assets; avoid low crossings | Prioritize plots where river stage has fallen but drainage remains blocked | River station and forecast snapshot | Redesign drainage/bunds and identify safer stores | Identify safe flood-spreading or recharge structures with authorities |
| Reservoir storage bulletin | Anticipate downstream releases only when paired with official notices | Assess irrigation availability after the event | Reservoir context, not proof of plot inundation | Plan rabi area against verified allocation | Recommend rabi planting only after local release/allocation confirmation |
| NRSC/NDEM flood layer | Identify historically exposed farms and evacuation routes | Target calls and field surveys to mapped inundation | Event/historical exposure overlay | Avoid critical storage in repeatedly inundated zones | Locate ponds/check dams outside contamination pathways |
| e-Chasa or farmer crop profile | Tailor message by crop, variety, stage, acreage, irrigation, and harvest date | Select drainage, replanting, pruning, salvage, or crop-switch workflow | Pre-event crop and area baseline | Recommend tolerant varieties and revised calendar | Match captured water to crop demand |
| Plot water depth-duration | Decide whether harvest, drainage, or evacuation remains feasible | Apply variety/stage-specific survival and replant thresholds | Objective duration and depth evidence | Redesign drainage and variety choice | Estimate recoverable water volume only if uncontaminated |
| Soil EC and chemistry | Establish pre-event baseline where available | Block sowing until EC falls below crop-specific threshold; retest after leaching | Before/after salinity evidence | Choose crop/variety and amendment from measured soil state | Use freshwater flushing only when drainage and downstream effects are acceptable |
| Rain, humidity, temperature, leaf wetness, crop stage | Warn against unnecessary nitrogen or risky spraying before heavy rain | Trigger blast, BPH, and sheath-blight scouting workflows, not automatic pesticide use | Time-stamped risk conditions and observations | Adjust spacing, canopy, variety, and nitrogen plan | No direct positive-use claim |
| Wind/gust and lodging survey | Support/harvest/prune only where crop-specific lead time and safety permit | Separate recoverable lodging from uprooting and structural loss | Lodging percentage, geotagged evidence, estimated affected area | Windbreak and crop-layout planning | Salvage biomass only after contamination and disease checks |
| Pond/well water-quality test | Cover or isolate vulnerable sources where practical | Assign use status: unsafe, disinfect, irrigation-only, livestock-only, aquaculture review, or safe | Laboratory/field-test record | Raise wellhead, improve drainage, protect pond inlet | Store freshwater and recharge only after quality and salinity checks |
| Mandi prices and arrivals | Advance harvest/sale only if crop maturity, storage, road, and price justify it | Find functioning market or temporary storage | Price/arrival context for avoided or realized loss | Diversify market routes and storage | Time rabi sales using actual market data |
| Road, mandi, power, and cold-store status | Reroute transport; protect perishable stock | Prioritize spoilage prevention and local aggregation | Closure duration, outage, spoilage, travel-time evidence | Pre-contract backup logistics | Use restored water assets only when access and power are safe |
| Credit, insurance, and wage profile | Send document checklist and emergency-cash warning; discourage predatory borrowing | Route farmer to formal relief, insurance, cooperative credit, or livelihood support | Loan, policy, loss, submission, and payment trail | Debt-sensitive crop and input plan | Finance ponds/check dams only with viable repayment and maintenance |
| Farm-pond and check-dam inventory | Create freeboard, inspect embankments and spillways, remove hazards only under official guidance | Test water and structural safety before pumping, irrigation, fish restocking, or recharge | Structure condition and repair evidence | Estimate supplemental rabi irrigation from measured storage | Core positive-use pathway: capture freshwater, supplemental irrigation, fisheries, and drought buffering |
| Seed-lot inventory and germination test | Move labeled lots to dry elevated storage | Dry, sample, test germination, discard contaminated lots safely, and request replacement | Lot, quantity, moisture, germination, and loss evidence | Replenish decentralized, diverse community stocks | Seed saving becomes actionable only when viability and distribution are recorded |
| Silt sample and deposit depth | No pre-event action beyond protecting soil baseline | Test before incorporation or removal; saline/contaminated silt may harm rather than fertilize | Deposit depth, lab result, affected area, removal cost | Apply nutrients from soil test, not a generic "floods fertilize" rule | Recommend incorporation only when nutrient benefit and safety are measured |

### Delivery logic for SMS and IVR

Every outbound message should contain four elements in plain Odia: **who is affected, what to do, by when, and what not to do**. The SMS should be short; IVR should repeat the action and accept keypad or spoken confirmation such as "field flooded," "water above crop," "salty water," "road blocked," or "need callback."

Confidence must be explicit inside the system even if it is simplified for the farmer:

- **Official alert**: issued by IMD, CWC, OSDMA, or another designated authority.
- **Model indication**: predicted, with time and uncertainty.
- **Remote-sensing observation**: mapped water, but depth or crop damage may remain unknown.
- **Farmer report**: unverified until cross-checked.
- **Field verified**: extension worker, sensor, laboratory, or claim survey confirms it.

This prevents the most dangerous failure mode: converting a broad model or old case study into a falsely precise instruction.

## 6. REAL-vs-FILLER

| Classification | Evidence test | Examples | Product treatment |
|---|---|---|---|
| **REAL - operational now** | Dated, recurring, accessible, and directly changes a decision | IMD warning page; CWC flood portal and weekly storage bulletin; daily mandi data [8][7][3][28] | Ingest with monitoring, provenance, cache, and manual fallback |
| **REAL - evidence/rule base** | Strong study or official assessment, but not a live feed | Swarna-Sub1 evaluation; Fani DLNA; rice disease-condition evidence [16][23][19] | Encode qualified rules and data fields; never copy historical loss values into current claims |
| **BRIDGE - useful with validation** | Relevant public source lacks farm resolution, API reliability, or current measurement | INCOIS model reports, NRSC maps, e-Chasa, Soil Health Card, farm-pond projects [26][27][17][21] | Partner access, farmer consent, field calibration, and human review |
| **FILLER - decorative** | Generic mechanism or impressive number cannot trigger or validate a local action | "Floods recharge groundwater," "silt improves fertility," generic Bangladesh salinity curves, unlinked seed-bank stories | Exclude from automated advice; retain only as a research hypothesis |
| **UNSAFE FILLER** | Recommendation could cause harm without a measurement | Automatic gypsum dose, drinking pond water after flooding, incorporating unknown silt, spraying pesticides immediately after flood | Block rule; require test or extension approval |

### Case study 1: Yaas is a scale signal, not a salinity sensor

The Yaas report is valuable because it establishes that seawater affected thousands of hectares and that effects persisted one month after the cyclone [15]. It also records an institutional response: OUAT and ICAR-NRRI collected soil samples and district officials expected rainfall to reduce salinity [15].

What it does not provide is equally important: no EC value, sample coordinates, repeated date, drainage rate, or crop-specific recovery threshold. The correct engine action is therefore "request or schedule a soil test and withhold crop-specific sowing approval," not "wait one month" or "rain will fix the field."

### Case study 2: Swarna-Sub1 supports a precise but bounded rule

The Balasore-Bhadrak evaluation links a named variety to flood duration through a randomized village design. Swarna-Sub1 tolerated up to two to three weeks of submergence, and its benefit increased with flooding duration in the 2011 event [16]. The non-flood year had no significant yield difference, showing that the mechanism is risk protection rather than an unconditional yield bonus [16].

This supports a next-season recommendation for repeatedly submerged rice land, but only after the engine knows the farmer's variety, flood regime, seed availability, and land conditions. It does not support recommending Swarna-Sub1 for every Odisha plot or extrapolating the result to vegetables, pulses, or perennial crops.

### Case study 3: Fani defines the claim schema

The Fani DLNA quantified crop area and loss, water-system damage, market disruption, person-days lost, wage losses, credit stress, and migration [23]. These categories reveal that agricultural recovery is not just a crop-yield problem: a farmer may have a standing crop but no clean water, road, labor, electricity, formal credit, or functioning market.

The DLNA is therefore genuinely useful for designing data fields and escalation pathways. It is filler if used as a current prediction table. A 2019 sector total cannot prove that a particular 2026 farmer lost a specific amount.

### Case study 4: Check dams and ponds are enabling assets, not proof of flood benefit

Odisha's annual report provides auditable infrastructure outputs, including check-dam counts and ayacut [10]. The Koraput-Nabarangpur project provides a smaller project case in which integrated pond systems expanded from 20 to 193 farmers and reported higher income than monocropping [11].

Together they justify collecting structure location, capacity, condition, water quality, and irrigation command area. They do not prove that a particular cyclone filled the structure safely, recharged a specific aquifer, or enabled a measured rabi yield. Those claims require event-specific storage readings, water tests, groundwater observations, and crop outcomes.

## 7. NOISE LOG

| Search path discarded or downgraded | Why it was rejected |
|---|---|
| Generic Kaggle crop, soil, and recommendation datasets | No Odisha event linkage, provenance, farm identifier, cyclone timestamp, flood depth, salinity sequence, or claim validity. They may demonstrate a classifier but cannot ground this advisory engine. |
| Bangladesh salinity studies | Useful for mechanism and hypothesis generation, but not an Odisha recovery timetable. Soil, drainage, tide, cyclone timing, and monsoon conditions differ. |
| Wikipedia, Scribd, and unsourced cyclone summaries | Discovery aids only; official IMD, INCOIS, OSDMA, and assessment reports take precedence. |
| Commercial mandi pages and scraped market sites | Unclear lineage, update quality, completeness, and terms. Prefer data.gov.in/AGMARKNET-derived records and retain raw provenance. |
| Private global lightning APIs | Potential purchase option, not proof of an official Odisha feed; coverage, latency, licensing, and rural detection quality require validation. |
| Generic recharge-zone maps | They rank where recharge may be feasible; they do not measure recharge caused by a named flood. |
| Odisha MAR suitability studies | Useful for site planning, but they do not provide event recharge volume or immediate post-flood water-table rise. |
| Generic statements that flood silt is fertile | No Odisha/Mahanadi plot-season panel tying deposit chemistry to subsequent yield was found; contamination and salinity can reverse the claimed benefit. |
| Coastal sediment and heavy-metal studies without farm-event linkage | They show contamination is plausible, but do not measure a named flood deposit on an enrolled farm. |
| Community seed-bank and seed-festival stories | Evidence of conservation, including saved varieties, but no verified cyclone response time, lot viability, households served, or post-disaster yield [29]. |
| IMD storm-surge verification PDF as a live feed | It is useful historical verification, not an API or current farm-level forecast object [22]. |
| NRSC flood-hazard atlas as current depth | A historical hazard map identifies exposure but does not establish today's water depth, start time, or drainage duration [27]. |
| e-Chasa home page as open data | The crop-survey purpose is relevant, but the reviewed public interface did not expose usable bulk data or API documentation [17]. |
| Fixed "days after flood" pest schedules | Reviewed BPH, blast, and sheath-blight sources support crop-stage and environmental triggers, not a universal day count [19][18]. |
| Tornado claims from general news or weak summaries | No authoritative Odisha cyclone-tornado track or farm-impact dataset was found. Treat reports as unverified until IMD or field investigation confirms them. |

## 8. VERDICT

### Grade: PARTIAL

A **free prototype can be built today**, but it should be presented as a warning-and-workflow prototype, not a complete hyperlocal loss-prediction system.

#### What is GO now

1. Poll and archive the IMD Odisha warning page, CWC flood portal, CWC reservoir bulletins, public NRSC/NDEM layers, and official mandi-price resources.
2. Enroll farms through IVR, SMS, an assisted call center, or extension workers. At minimum collect village, approximate location, crop, variety, acreage, sowing/transplant date, irrigation, phone language, livestock, pond/well, and consent.
3. Generate pre-event checklists by hazard, crop, stage, and lead time. Safety and official evacuation directions must override agricultural actions.
4. Run post-event IVR triage: flood start/end, water above crop, salty water, lodging, seed wetting, pond/well contamination, road access, market access, credit need, and callback request.
5. Produce a claim packet containing alert snapshot, farmer profile, event answers, field-worker verification, photos where available, sensor/lab results, and a transparent loss worksheet.
6. Use only bounded evidence rules, such as Swarna-Sub1's demonstrated flood-risk protection, and condition-based scouting for rice diseases and pests [16][19][18].
7. Provide positive-use advice only after structure and water checks: inspect farm ponds/check dams, measure stored water, test salinity/contamination, then plan supplemental or rabi irrigation.

#### What requires local collection

- Plot coordinates or polygon and reliable farm identity.
- Crop stage, variety, plant height, drainage and pre-event condition.
- Rain, wind/gust, flood depth and duration.
- Soil EC/ECe and repeated salinity tests.
- Pond/well EC, turbidity and microbial safety.
- Seed moisture, germination and fungal condition.
- Lodging, uprooting, affected area and yield samples.
- Road/mandi status, transport time and farm-gate price.
- Credit, wage-day, insurance, migration and recovery outcomes.
- Pond/check-dam storage, groundwater level and rabi water use.
- Silt chemistry, deposit depth and next-season yield.

These can begin with low-cost manual protocols and extension-worker forms. IoT should be added where its measurement changes a decision, not as decoration.

#### What requires a partner

- **IMD/RSMC**: documented warning feed, cyclone track, rainfall/wind products, rights and operational support.
- **INCOIS**: surge height, coastal-inundation raster/polygon, uncertainty, timestamps, and model metadata.
- **CWC and Odisha DoWR**: river forecasts, gauge and release data, reservoir/check-dam status, and downstream context.
- **OSDMA/SRC Odisha**: authoritative alert routing, road/embankment status, impact reports, and emergency protocols.
- **Odisha Agriculture Department/e-Chasa**: consented crop profile, survey identifiers, damage assessment and scheme routing.
- **OUAT, ICAR-NRRI, KVKs, and soil laboratories**: salinity thresholds, repeated Yaas-like field measurements, pest surveillance, crop-stage rules, and local-language validation.
- **Market committees and Works Department**: mandi closure, road passability, transport and cold-chain status.
- **Insurers, banks, cooperatives, and relief agencies**: claim schema, credit eligibility, status APIs, and grievance pathways.
- **Telecom/SMS/IVR provider**: Odia voice delivery, retry logic, keypad/speech capture, consent, and delivery receipts.

### Synthesis

| Dimension | Broad hazard feeds | Farm/agronomic evidence | Livelihood and recovery assessments | Positive-use evidence |
|---|---|---|---|---|
| Mechanism | Detect approaching rain, river flood, cyclone, or surge | Translate depth, duration, stage, variety, humidity, and salinity into biological risk | Record interruption of water, labor, markets, credit, and transport | Capture and store safe freshwater for later irrigation or livelihoods |
| Spatial scope | Subdivision, coast, basin, station, reservoir, or hazard map | Plot, crop, variety, stage, and sample | Household, market, district, or sector | Structure, command area, pond, aquifer, and farm |
| Time horizon | Hours to days; reservoir context weekly | Hours through a crop season | Days through years | Event through rabi and later dry seasons |
| Evidence strength | High authority, weak farm resolution and API clarity | Strong for selected mechanisms, incomplete for Odisha crops and post-flood timing | Rich historical categories, weak live feeds | Strong asset counts, weak event attribution |
| Main trade-off | Speed versus local precision | Specificity versus transferability | Comprehensiveness versus timeliness | Opportunity versus contamination, salinity, structural and attribution risk |

The central tension is that the most authoritative data is broad, while the most decision-relevant data is local and frequently absent. An IMD warning can establish that dangerous weather is coming, but it cannot reveal a farmer's variety, field depth, drainage, seed condition, road access, or pond salinity. Conversely, a farmer's IVR report is timely and local but may require verification.

The architecture should therefore be **event sourced and confidence aware**. Preserve every official alert, model update, farmer response, sensor reading, laboratory result, field verification, recommendation, delivery receipt, and later outcome. This creates an audit trail for claims and a growing Odisha-specific training set without allowing an opaque model to invent precision.

The positive-use theme exposes a second tension. Ponds, check dams, reservoirs, and seed banks can increase resilience, but a cyclone can also deliver saline or contaminated water, damage embankments, spoil seed, and deposit harmful sediment. The engine should never label disaster water or silt a benefit by default. The operational rule is: **measure first, classify the use, record the outcome, and learn locally**.

**Final decision:** Build the free prototype now with public warnings, historical evidence, mandi data, assisted farm profiles, SMS/IVR, and explicit uncertainty. Grade the full proposed platform **PARTIAL** until INCOIS/IMD/CWC interfaces and plot-level measurements are secured. Surge automation, salinity recovery, water-quality clearance, claim-grade loss estimation, flood recharge, silt fertility, and live market-access recommendations remain **GATED** by partners or field collection.

## References

1. *IMD issues Cyclone Alert for south Odisha north Andhra ... Pib.gov.in https://www.pib.gov.in › newsite › PrintRelease*. https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=183603
2. *Flooding or submergence - IRRI Rice Knowledge Bank*. http://www.knowledgebank.irri.org/decision-tools/rice-doctor/rice-doctor-fact-sheets/item/flooding-or-submergence
3. *Flood Forecast - Central Water Commision, Govt. Of India*. https://ffs.india-water.gov.in/
4. *Flood-tolerant rice for enhanced production and livelihood ...*. https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2023.1244460/full
5. *Odisha FANI cyclone Assessment Report*. https://ircsstoragedev.blob.core.windows.net/wordpresswebsite/2024/03/OdishaFaniAsessmentReport.pdf
6. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
7. *Reservoir Level & Storage Bulletin | Central Water Commission ...*. https://cwc.gov.in/en/reservoir-level-storage-bulletin
8. *Warnings - imd - India Meteorological Department*. https://mausam.imd.gov.in/imd_latest/contents/subdivisionwise-warning_mc.php?id=10
9. *Cyclone Dana Assessment Report - ysdindia.org*. https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf
10. *ANNUAL REPORT 2023-24 - dowr.odisha.gov.in*. https://dowr.odisha.gov.in/sites/default/files/2025-07/WR_AR-23-24.pdf
11. *How Rainwater Harvesting Is Transforming Seasonal Farming ...*. https://www.downtoearth.org.in/agriculture/how-rainwater-harvesting-is-turning-seasonal-farming-into-year-round-livelihoods-in-this-odisha-district
12. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report/
13. *Planthopper - IRRI Rice Knowledge Bank*. http://www.knowledgebank.irri.org/training/fact-sheets/pest-management/insects/item/planthopper
14. [
            Physiological basis of tolerance to complete submergence in rice involves genetic factors in addition to the SUB1 gene - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC4243076)
15. *Cyclone Yaas aftermath: Odisha farmers in a fix over sowing Kharif crop*. https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568
16. *Reducing Farmers' Risk through Flood-Tolerant Rice in India | The Abdul Latif Jameel Poverty Action Lab*. https://www.povertyactionlab.org/evaluation/reducing-farmers-risk-through-flood-tolerant-rice-india
17. *echasa.odisha.gov.in*. https://echasa.odisha.gov.in/
18. *Sheath Blight (Rhizoctonia solani)*. http://www.agritech.tnau.ac.in/expert_system/paddy/cpdissheathblight.html
19. *Rice Blast: A Disease with Implications for Global Food ...*. https://www.mdpi.com/2073-4395/9/8/451
20. *Current Daily Price of Various Commodities from Various Markets (Mandi) | Open Government Data (OGD) Platform India*. https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi
21. *Soil health card | Soil Health Card*. https://www.soilhealth.dac.gov.in/soilhealthcard
22. *Storm Surge*. https://rsmcnewdelhi.imd.gov.in/images/storm_surge.pdf
23. *untitled*. https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
24. *Flood Hazard Atlases | NDMA*. https://ndma.gov.in/flood-hazard-atlases
25. *Cyclone E2809Cfanie2809D Joint Rapid Needs Assessment Report 2019*. https://www.sphereindia.org.in/sites/default/files/2021-08/cyclone-e2809cfanie2809d-joint-rapid-needs-assessment-report-2019.pdf
26. *Enhancement of Coastal Flood Inundation Forecasting by*. https://incois.gov.in/documents/Reports/TechnicalReports/TR_ESSO-INCOIS-OMARS-TR-07(2024)_20250701122038.pdf
27. *Flood Hazard Atlas - National Remote Sensing Centre*. https://ndem.nrsc.gov.in/hydrological_fhz.php
28. *CEDA Agri Market Data*. https://agmarknet.ceda.ashoka.edu.in/
29. *Odisha's seed fest brings back 60 indigenous crops from ...*. https://101reporters.com/article/The_Promise_Of_Commons/Odishas_seed_fest_brings_back_60_indigenous_crops_from_the_brink
