# Odisha Cyclone-Flood Data: Buildable Signals, Critical Gaps

## 1. EXECUTIVE SUMMARY

- **A warning-trigger prototype is buildable now**: IMD publishes district warnings, district nowcasts, 5-day district rainfall forecasts, cyclone track/wind endpoints and issue/valid times; for Cyclone Dana, IMD first signaled likely development about **7.5 days before landfall**. The engine can therefore ingest and version official triggers instead of scraping news, subject to IMD attribution, caching and possible IP whitelisting. [8][9]

- **Surge height is usable; farm-level inundation is not**: Dana's realized surge was estimated at **1-2 m** in low-lying Kendrapara and Bhadrak, while the public INCOIS service confirms a storm-surge map but does not document a farm-ready API, grid resolution, cadence or inland penetration distance. Use surge bulletins to escalate risk, but never label an individual plot inundated without a map partnership or field confirmation. [9][15]

- **Yaas proves that "flooded" and "salinized" are different states**: a 21 June 2021 field report, about a month after Yaas, recorded at least **5,882 ha** affected by seawater in five Balasore blocks. Coastal Odisha research classifies irrigation-water EC below 0.25 dS/m as low salinity and above 2.25 dS/m as very high, but no public source supplies parcel EC or a universal recovery clock. The app must ask whether water was saline and request an EC test before resowing advice. [10][24]

- **Waterlogging advice must be stage-and-duration aware**: a global meta-analysis found mean yield loss of **32.9%**, with **41.90%** loss at reproductive stage versus **34.75%** at vegetative stage; 15-28 days of field waterlogging produced the largest reported reduction, **53.19%**. These are priors, not Odisha plot predictions, so standing-water start/end time, depth, crop and stage must be collected locally. [6]

- **Post-flood pest messages can be scouting prompts, not outbreak forecasts**: blast is favored by extended leaf dampness, 92%-96% RH and 25-28 C and may show lesions within 3-5 days; an Odisha NRRI advisory uses **5-10 BPH per hill** as an economic-threshold trigger; sheath blight is favored by 28-32 C and 85%-100% canopy RH and is usually observed from tillering to milk stage. No public Odisha event series gives a reliable "days after flood" outbreak clock for all three. [36][29][32]

- **Claims support is unusually concrete**: PMFBY's revised guidelines cover standing-crop flood, inundation, lightning, storm and cyclone losses, permit only a maximum two-week post-harvest cover for specified field-dried crops, and require loss intimation within **72 hours** with survey number, crop and affected acreage. A claim packet can therefore be a real product: timestamped official warning, farmer ID, plot/survey ID, crop/stage, geotagged photos and the loss-intimation receipt. [37]

- **Positive use is real only when engineered and tested**: an Odisha farm-pond experiment at Phulbani covered the 2018-19 and 2019-20 seasons, while a 2026 Koraput/Nabarangpur case reports an integrated pond model combining aquaculture, crops and composting. Neither proves that arbitrary cyclone floodwater is safe; saline or contaminated inflow can reverse the benefit. Advise storage/reuse only after source, EC and basic water-quality checks and only where the structure is safe. [21][23]

- **Groundwater data are a baseline, not a post-flood recharge meter**: Odisha's 2024 assessment reports **17.46 BCM** annual recharge, more than 2,000 monitoring stations and block-level assessment, but it is an annual resource account rather than an event-attributed recharge rate. The requested "recharge after a major flood" remains a measurement gap requiring paired pre/post-event wells and rainfall records. [33]

- **Overall grade: PARTIAL**: public data can support a free or low-cost trigger layer, conservative rules and SMS text today; plot impacts, recovery clearance and positive-use safety require farmer/field collection; INCOIS model grids, OSDMA/AMAKRUSHI delivery, water laboratories, insurers and market authorities are partner gates. Odisha's 2024 plan reports weekly Crop Weather Watch and AMAKRUSHI IVRS delivery to more than **70 lakh** profiled farmers across more than **40 crops**, proving the delivery concept but also signaling that integration should complement, not duplicate, state infrastructure. [22]

## 2. DATA INVENTORY

**Reliability grades:** **A** = official operational or administrative source; **B** = official static report or peer-reviewed evidence with a transferability caveat; **C** = credible assessment, case report or media observation; **D** = no directly usable public source, or only a non-local proxy. "Free" means no purchase was identified; registration, IP whitelisting, rate limits or partner approval may still apply.

### During the event

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---|---|---|---|
| Cyclone track, wind and warning trigger | IMD API Reference, live reference page, <https://api.imd.gov.in/public/api_reference.html>; cyclone track/wind and district-warning endpoints are listed [8] | Cyclone track plus district warning/nowcast; station/district IDs | Issue-time; district rain forecast to 5 days and subdivision forecast to 7 days | Public documentation; API access, attribution, caching and possible IP whitelisting [4] | **A** |
| CAP alert stream and mass warning | IMD Cyclone SOP, current operational SOP; CAP feeds flow to WMO Alert Hub, Google, AccuWeather and GMAS [39] | Alert polygons/text depend on bulletin | Event-time | Open RSS/CAP feed plus IMD channels | **A** |
| Surge height and affected districts | IMD Dana Report, 7 Nov 2024, <http://internal.imd.gov.in/press_release/20241107_pr_3389.pdf>; forecast and realized 1-2 m surge [9] | Named low-lying districts, not plot | Event report; bulletin during cyclone | Free PDF/report | **A** |
| Storm-surge model and inland penetration | INCOIS StormSurge service, public page accessed 2026, <https://incois.gov.in/site/services/StormSurge.jsp> [15] | Interactive coastal map; documented farm resolution absent | Operational service, undocumented cadence | Free web map; model grid/API requires confirmation or partner | **B** for service; **D** for parcel penetration |
| Saline-intrusion extent and duration | Down To Earth, "Cyclone Yaas aftermath," 21 Jun 2021, <https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568> [10] | Five Balasore blocks; reported hectares | One event snapshot about one month after Yaas | Free report; parcel extent needs field/remote sensing | **C** |
| Torrential rain and district warning | IMD API district warnings, nowcasts, basin QPF and rainfall fields [8] | District, station and basin | Nowcast to 7-day products | API/file; likely whitelisting for some endpoints | **A** |
| River flood level and reservoir inflow | CWC Flood Forecasting, updated 14 Aug 2026, <https://cwc.gov.in/flood-forecasting-hydrological-observation>; 325 stations across 25 states including Odisha [18] | Forecast station/reservoir, not farm | Severe bulletins every 3 hours; extreme every hour in flood season [18] | Free portal/app; no farm API documented on the cited page | **A** |
| Field water depth and waterlogging duration | No public Odisha plot feed found | Individual plot; hourly/daily depth and start/end | Must be event-time | Farmer IVR/SMS, staff survey, low-cost gauge/IoT, or satellite-derived layer | **D** until collected |
| Wind damage and crop lodging | IMD wind warning plus Fani assessment: 152,985.40 ha agricultural area affected, but no crop-stage lodging field [11] | District damage total; no crop/stage pattern | Post-event assessment | Bulletin plus field photos/inspection | **C** for damage context; **D** for lodging prediction |
| Lightning | IMD API warning category Cat19: high cloud-to-ground lightning probability above 60%; Damini app is listed by IMD [8][4] | District/nowcast product; app location service | Nowcast/event-time | IMD warning API/CAP and Damini app | **A** |
| Tornado occurrence/forecast | No tornado-specific Odisha endpoint was found in IMD's documented API index; severe-thunderstorm categories cover gusts, lightning and text warnings [8] | None specific to farm plots | None | Treat as severe-thunderstorm text; do not fabricate tornado probability | **D** |

### After the event

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---|---|---|---|
| Crop-stage response to waterlogging | Tian et al., "How Does the Waterlogging Regime Affect Crop Yield?", Frontiers in Plant Science, 2021, <https://www.frontiersin.org/articles/10.3389/fpls.2021.634898/full> [6] | Meta-analysis by crop, growth stage and duration; not Odisha plot-level | Static research | Free article/rule prior | **B** |
| Odisha flood contingency actions | Government of Odisha, Crop Contingency Plan 2024 and 2025, <https://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf>; recommends tolerant rice, drainage, community nurseries and staggered replanting [22] | State with district/block planning and crop calendars | Annual plan; in-season monitoring described | Free PDF; partner/rule extraction | **A** |
| Rice blast risk | IRRI Rice Knowledge Bank factsheet and Asibi et al., Agronomy 2019, <https://www.mdpi.com/2073-4395/9/8/451>; all stages can be infected and favorable weather is quantified [38][36] | Biological/weather rule, not Odisha outbreak observations | Static evidence | Free article/factsheet | **B** |
| Brown planthopper risk | ICAR-NRRI Odisha advisory, first fortnight May 2024, <https://icar-crri.in/wp-content/uploads/2024/04/AAS_May_2024_I_English.pdf>; ETL 5-10 hoppers/hill [29] | Odisha; farmer scouting by hill | Dated fortnightly advisory | Free PDF; current observation must be collected | **A** for rule; **D** for flood-linked onset |
| Sheath blight risk | IRRI Rice Knowledge Bank factsheet, undated, <http://knowledgebank.irri.org/decision-tools/rice-doctor/rice-doctor-fact-sheets/item/sheath-blight> [32] | Crop stage and canopy weather | Static rule | Free factsheet | **B** |
| Coastal-soil salinity thresholds and management | Das, Senapati and Behera, 2020, "Salinity Problem and its Management in Coastal Belt of Odisha," <https://ijcmas.com/9-6-2020/Ashok%20Kumar%20Das%2C%20et%20al.pdf> [24] | Regional classes and crop tolerance, not parcel measurement | Static 2020 | Free PDF; EC meter/lab needed locally | **B** |
| Soil salinity recovery timeline | No public source established a universal Yaas recovery period; Yaas extent is a dated snapshot, while management depends on EC, drainage and fresh-water leaching [24][10] | Plot/lab | Must be resampled after drainage/rain/leaching | Field EC and soil sampling | **D** for timeline |
| Seed viability and stored-seed degradation | FAO emergency practice supports restoring access to good-quality seed, but no Odisha event-linked public germination/moisture dataset was found | Seed lot and storage site | Immediate post-event | Germination test, moisture, mold inspection; field collection | **D** |
| Pond, well and groundwater contamination | Fani assessment anticipated sanitation/vector risks and reported acute water shortage, but not event-linked EC, microbial or chemical test series [11] | Household source/pond/well | Must be sampled after event | Field kit plus accredited lab; public baseline only | **D** |
| Mandi prices and arrivals | DMI/Ministry data via CEDA Agri Market Data, accessed 2026, <https://agmarknet.ceda.ashoka.edu.in/>; downloadable daily/monthly/yearly market observations [34] | Market, commodity, district/state where reported | Daily source data, portal-dependent | Free portal/download; no closure cause field shown | **A/B** |
| Mandi closure, route loss and transport time | No authoritative unified Odisha event feed found; Fani assessment recorded continuing road clearance/restoration, not mandi status [11] | Road segment and mandi | Event-time needed | Partner feeds, call center and crowdsourced verification | **D** |
| Credit, debt, labor and migration effects | Chhotray and Few, rural Odisha flood recovery study, 2023, 400 households/40 villages after the 2014 Bhadrak flood; labor migration improved one-year recovery probability, while productive-asset sales reduced it [3] | Household survey; coastal Odisha | Retrospective study | Article/report; no live feed | **B** |
| Claim eligibility and evidence | PMFBY Revised Operational Guidelines, <https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf>; 72-hour intimation, plot/crop/acreage detail and joint assessment [37] | Insured notified crop and survey-number plot | Rule-based; scheme notification must be current | Free guideline/portal; insurer/state integration for status | **A** |

### Positive use and next-season planning

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---|---|---|---|
| Farm-pond/rainwater-harvesting performance | Journal of Agricultural Engineering, Phulbani study covering 2018-19 and 2019-20, <https://pub.isae.in/index.php/jae/article/view/1208> [21]; Odisha Farm Pond guidance is also publicly listed | Experimental farm/structure | Static two-season study | Free article/guidance; local pond geometry required | **B** |
| Integrated pond livelihood use | Down To Earth/MSSRF Koraput-Nabarangpur case, 1 Jul 2026, <https://www.downtoearth.org.in/agriculture/how-rainwater-harvesting-is-turning-seasonal-farming-into-year-round-livelihoods-in-this-odisha-district>; pond model combines aquaculture, crops and compost [23] | Participating farms in two districts | Current case report | Free report; program/field records needed | **C** |
| Groundwater recharge baseline | Government of Odisha and CGWB, Dynamic Ground Water Resources of Odisha 2024, published Jan 2025, <https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17435864691666329414file.pdf> [33] | Block/subunit; more than 2,000 monitoring stations | Annual assessment using pre/post-monsoon data | Free PDF and agency records | **A** |
| Recharge after a named major flood | No public study found that isolates cyclone/flood recharge in Odisha from monsoon recharge | Paired well/event | Missing | Pre/post-event loggers, rainfall and tracer/water-balance study | **D** |
| Flood-silt deposition and fertility | No Odisha study found that measures event-specific silt depth, nutrients/contaminants and subsequent yield together | Plot and sediment sample | Missing | Field cores and lab tests | **D** |
| Reservoir/check-dam fill enabling rabi irrigation | CWC explains that inflow forecasts support reservoir operation and storage for non-monsoon irrigation, but no source found attributes Odisha rabi hectares to a named flood [18] | Reservoir/check dam and command area | Operational levels; outcome attribution missing | CWC/DoWR partner data plus command-area crop map | **A** for levels; **D** for attribution |
| Community seed banks | MSSRF, "The quiet power of seed keepers in Odisha's community seed banks," 19 May 2026, <https://www.mssrf.org/stories-of-change/seed-keepers-odishas-community-seed-banks> [20] | Village/community and seed lot | Current narrative/program records | Free story; partner inventory and viability tests | **C** |
| Seed-bank network development | MSSRF DIVERSSIFARM project, Jan 2024-Dec 2026, <https://www.mssrf.org/projects/diversifarm-india-unfolding-potential-community-seed-banks-food-and-nutrition-security> [14] | Program/community | Active project | Partner access | **B/C** |

**Inventory takeaway:** the strongest public layer describes the **hazard and administrative rule**. The weakest layer describes the **farm outcome**. The engine should preserve that distinction explicitly in every advisory and confidence score.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing fields | Coverage judgment A-D |
|---|---|---|---|
| **IMD APIs, CAP and cyclone reports** | Track, wind, district warnings/nowcasts, rainfall, lightning category, issue/valid time, surge bulletins and verified event lead times [8] | No crop stage, plot drainage, standing-water duration, EC, loss or tornado-specific probability | **A** for triggers; **D** for farm impact |
| **INCOIS storm-surge service** | Official surge service and interactive map [15] | No public documentation found for farm grid, API, update cadence or inland penetration distance | **B** as authoritative service; **D** as open machine layer |
| **CWC flood forecasting** | Odisha coverage, station/reservoir forecasts, seasonal operation and 1-hour/3-hour severe-event cadence [18] | River gauge is not field depth; no crop or salinity variables | **A** for river state; **C/D** for farm translation |
| **Odisha Agriculture, OUAT/NRRI and AMAKRUSHI** | Annual contingency plans, crop calendars, tolerant varieties, weekly monitoring and IVRS reach above 70 lakh profiled farmers [22] | Public machine-readable advisory API, versioned rules and response/outcome logs not found | **A** content; **GATED** integration |
| **ICAR/IRRI agronomy sources** | BPH ETL, blast/sheath weather and stage conditions, flood-tolerant rice choices [29][32] | No Odisha event-linked onset clock or universal chemical recommendation; local diagnosis required | **B** |
| **Odisha/CGWB water resources** | Annual block recharge and monitoring baseline [33] | No named-flood recharge attribution, parcel groundwater quality or safe-use clearance | **A** baseline; **D** event causal data |
| **AGMARKNET/DMI and e-NAM family** | Commodity prices and arrivals with downloads [34] | No reliable closure reason, road delay, rejected lot, farmgate distress price or causal cyclone flag | **B** |
| **PMFBY/insurance rules** | Perils, 72-hour deadline, required plot/crop/acreage detail and process milestones [37] | Enrollment/notification and claim status require current state/insurer data | **A** rules; **GATED** status |
| **Peer-reviewed agronomy and social science** | Transferable duration/stage losses and a 400-household Bhadrak recovery case [6][3] | Retrospective, not operational; some results are association, not causal farm forecasts | **B** |
| **Assessment, media and NGO case reports** | Yaas saline extent, Fani field impacts, current pond and seed-bank cases [10][11][23] | Sampling and update cadence vary; cannot become live sensors by citation | **C** |

**Coverage judgment:** source discovery is **A/B** for warning, general agronomy and claim rules; **C/D** for plot impacts, post-event chains and positive-use causality. More web search will not close gaps that require measurements or institutional data-sharing.

## 4. WHAT IS MISSING

These gaps are named narrowly because each is a required state variable, not a generic request for "more data."

| Exact missing gap | Why no public source presently closes it | Minimum collection or partnership |
|---|---|---|
| **Plot-level storm-surge inland penetration, depth and arrival time** | Public bulletins name surge height/districts; INCOIS's public page does not document a farm-grid API [9][15] | INCOIS/IMD raster partnership plus cadastral overlay and field validation |
| **Parcel saline-intrusion boundary, residence time and EC decay curve** | Yaas reports hectares at block scale; regional EC classes do not measure an affected plot [10][24] | EC meter at drainage, 48-72 hour repeat and pre-sowing sample |
| **Field water depth-duration by crop stage** | CWC measures river/reservoir state, not standing water in a field | Farmer timestamp, staff observation, gauge/IoT or validated satellite water mask |
| **Wind lodging by crop, variety, stage and gust exposure** | Assessments aggregate affected hectares; no public Odisha lodging function was found | Before/after photo, variety, stage, planting density and measured/estimated gust |
| **Operational tornado probability or tornado footprint for Odisha farms** | IMD documentation exposes severe-thunderstorm/lightning categories, not a tornado-specific farm layer [8] | Use severe-thunderstorm fallback; partner with IMD for event confirmation |
| **Post-flood blast/BPH/sheath-blight onset clock and incidence surface** | Sources give biological conditions and scouting thresholds, not event-linked Odisha prevalence [36][29][32] | Sentinel plots, geotagged scouting and lab/extension confirmation |
| **Seed-lot moisture, mold, germination and varietal identity after inundation** | No public Odisha event-level seed-quality series was found | Lot ID, storage exposure, moisture reading and germination test |
| **Post-event pond/well EC, turbidity, E. coli and chemical contamination** | Fani assessment anticipated WASH risks but supplied no water-quality time series [11] | Field kit plus accredited lab and source-specific clearance |
| **Mandi closure status, road travel time, rejected loads and farmgate distress price** | Price/arrival portals do not expose a causal disruption field | Regulated-market authority, transport/GIS partner and IVR trader verification |
| **Event-linked credit drawdown, debt rollover, wage loss and migration timing** | The Bhadrak study identifies recovery associations but not a live household ledger [3] | Consented household pulse survey and SHG/bank/OLM partnership |
| **Named-flood groundwater recharge rate** | Annual estimates combine processes and use pre/post-monsoon observations [33] | Paired pre/post-event water levels, rainfall, pumping and aquifer parameters |
| **Flood-silt nutrient benefit versus sand, salt or contaminant harm** | No Odisha source jointly measured event sediment chemistry and later yield | Sediment depth, texture, EC, nutrients/metals and paired crop outcome |
| **Reservoir/check-dam fill causally converted to rabi irrigation** | Operational storage and irrigation purpose are known, but named-event command-area outcomes are not [18] | DoWR releases, command maps and crop-area change |
| **Community seed-bank emergency stock, viability and disaster drawdown** | Public stories document institutions, not auditable event stock flows [20] | Partner inventory, lot tests, loans/returns and beneficiary outcome log |
| **Stable farm identity and consent/provenance layer** | None of the hazard sources knows the farmer's crop, plot, stage, language or consent | Offline enrollment, survey/cadastral ID, crop calendar, preferred voice/language and audit log |

The product implication is strict: when a missing value controls safety, the engine must ask, measure or abstain. It must not fill a null with a district average and present it as a parcel fact.

## 5. HOW IT FEEDS THE ENGINE

### Decision mapping

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD track/wind/district warning | Harvest mature crop, secure seed/input stores, move pumps/livestock, stop fieldwork | Establish event ID and hazard window | Attach bulletin version and issue time | Compare repeated exposure | Not sufficient alone |
| IMD rainfall/nowcast and CWC level | Clear drains, protect low inputs, move equipment from low points | Start waterlogging clock and prioritize field checks | Attach rainfall/gauge context | Redesign drainage and crop calendar | Consider capture only if structure and water are safe |
| INCOIS/IMD surge bulletin | Trigger coastal evacuation and saltwater-risk message | Separate saline from freshwater pathway | Add surge/district evidence | Salt-tolerant variety and bund/sluice planning | Reject untested saline storage |
| Farmer plot/crop/stage profile | Select crop-specific action and voice script | Select stage-specific recovery rule | Identify insured plot, crop and acreage | Update variety/sowing-window choice | Match stored water to crop tolerance |
| Water depth and duration | No action until event, except place gauge | Drainage urgency, survival check, replant-versus-recover decision | Timestamped impact duration | Raised beds, drainage, tolerant variety | Estimate captured volume only after testing |
| Wind/lodging observation | Support/stake vulnerable horticulture where feasible | Dry, salvage or avoid unsafe harvest by crop | Before/after geotagged images | Variety, spacing, windbreak decisions | Biomass use only after contamination check |
| Lightning/severe-thunderstorm warning | Stop open-field work and shelter safely | Inspect fire/electrical damage | Add time/location evidence if covered | Work-safety protocol | None |
| Soil/water EC | Pre-position meter and keep fresh-water source protected | Decide leaching, drainage, crop hold or salt-tolerant option | Document saline inundation; scheme relevance depends on notification | Soil amendment/drainage and crop choice | Permit pond irrigation only within crop/water thresholds |
| Blast weather and scouting | Avoid excess nitrogen; prepare scouting message | Inspect in 3-5 day symptom window under favorable conditions, then obtain diagnosis [36] | Photograph diagnosed loss; do not infer disease from weather alone | Resistant variety and residue/nitrogen management | None |
| BPH hill count | Prepare scouting route | Act only at/above local ETL and extension advice | Record count, plot and diagnosis | Resistant/appropriate variety and pesticide stewardship | None |
| Sheath-blight stage/canopy | Flag dense, high-N tillering-to-milk fields | Scout sheath above soil/water line; confirm differential diagnosis | Record lesions and crop stage | Spacing, nitrogen and canopy management | None |
| Seed-lot test | Elevate bags and waterproof storage | Dry safely, inspect mold, run germination test, replace failed lot | Record inventory and damage | Seed-bank reservation and diversified lots | Save only viable, identified, uncontaminated seed |
| Pond/well water test | Cover/protect source where possible | Do not drink, stock fish or irrigate until source-specific clearance | Add lab/field report for infrastructure loss | Source protection and treatment design | Refill/reuse only after EC and contamination gate |
| AGMARKNET price/arrival | Identify alternate markets and harvest timing | Compare nearby market observations | Context only, not proof of individual loss | Crop/market diversification | Schedule sale from rabi/pond production |
| Mandi/road status | Reroute or delay dispatch | Arrange aggregation/cold storage if available | Log closure, route and rejected load | Local storage/cooperative plan | None |
| Household credit/labor/migration profile | Pre-arrange emergency contact and SHG/bank options | Target cash, labor exchange and social-protection referral | Keep expense and input receipts | Reduce distress asset sales; diversify income | Labor availability constrains pond/check-dam work |
| PMFBY enrollment and rule | Confirm notified crop, insurer, plot and contacts | Send loss-intimation prompt before 72 hours | Assemble survey ID, crop, acreage, photos, bulletin and receipt | Correct enrollment/land record before next season | None |
| Groundwater/block baseline | Identify water-stressed or saline blocks | Compare observation without claiming flood causality | Context only | Well monitoring and pumping plan | Recharge claim only after paired measurements |
| Reservoir/check-dam level | Protect downstream assets; monitor releases | Coordinate access and drainage | Context for flood path | Plan rabi only after confirmed allocation/release | Use stored water within allocation and quality limits |
| Farm pond/RWH structure | Check embankment, spillway and inlet; isolate dirty first flush | Inspect breach, sediment and water quality | Photograph structure loss | Size storage and supplemental irrigation from measured need | Aquaculture/vegetable use only after safety gate |
| Silt sample | None | Test before incorporation or removal | Document deposition depth/area | Nutrient credit only from laboratory result | Never label silt "fertile" by default |
| Community seed-bank stock | Move lots to dry elevated storage | Release tested, locally suitable seed with lot tracking | Record lost/issued lots | Replenish and diversify tolerant varieties | Seed saving is positive only with viability and identity controls |

### Case study 1: Dana turns an alert into a versioned action window

IMD first identified likely Dana development about 7.5 days before landfall, issued a pre-cyclone watch about 4.5 days ahead, and supplied the first pre-genesis track/intensity/landfall prediction about 3.5 days ahead. A 1-2 m storm surge was predicted about two days before landfall and later estimated as realized in low-lying Kendrapara and Bhadrak. [9]

The mechanism is a sequence, not one alert: readiness at extended range, asset protection at watch, district/crop action at warning, and exposure verification after landfall. The recommendation is to store every bulletin with `event_id`, `issued_at`, `valid_to`, source URL and affected geography, then recompute advice only when a newer official version arrives. That provenance also strengthens a later claim packet.

### Case study 2: Yaas forces a saline-versus-freshwater branch

One month after Yaas, 5,882 ha in five Balasore blocks was still reported as affected by seawater. Regional evidence also shows very different crop tolerance ranges: pulses are listed at 1.5-3 dS/m, sugarcane/groundnut/maize at 3-5 dS/m and rice/wheat/soybean/sorghum/mustard at 5-10 dS/m. [10][24]

The mechanism is osmotic and crop-specific, so elapsed days alone cannot clear a field. The engine should ask "Was water salty?" over IVR, route a local EC reading, and withhold precise amendment or sowing clearance until drainage and current EC are known. The same gate prevents a false positive-use message telling a farmer to save saline water in a pond.

### Case study 3: Fani links damage evidence to recovery logistics

The Red Cross assessment reported 152,985.40 ha of agricultural area affected, 279 fish ponds covering 66.92 ha damaged, road restoration still under way and acute water shortage where power failed. [11] These facts show why a crop-only workflow fails: pond integrity, road access, power and water availability constrain what recovery action is feasible.

The mechanism is cascading infrastructure loss. The engine should therefore ask a short dependency sequence before prescribing inputs: "Can the field be reached? Is drainage possible? Is safe water available? Is the pond bund intact?" A technically correct agronomic recommendation that cannot be executed is not actionable advice.

## 6. REAL-vs-FILLER

| Status | Data/product element | Evidence-based judgment |
|---|---|---|
| **REAL - use in MVP** | IMD CAP/API warning, nowcast, rainfall, cyclone track/wind | Official, timestamped, machine-oriented products with documented fields [8] |
| **REAL - use in MVP** | CWC station/reservoir forecast | Official flood state with known high-event bulletin cadence [18] |
| **REAL - use as rules** | Odisha Crop Contingency Plan and NRRI advisories | Odisha-specific crop actions, crop calendars and a measurable BPH ETL [22][29] |
| **REAL - use as claims workflow** | PMFBY 72-hour rule and evidence fields | Specific deadline, plot/crop/acreage details, joint survey and process milestones [37] |
| **REAL - use as observation, not causation** | AGMARKNET/DMI prices and arrivals | Useful market comparison; cannot prove a cyclone caused a price change [34] |
| **REAL - collect directly** | Crop/stage, water depth-duration, EC, pest counts, seed test, photos | These missing values determine branch safety and are feasible through SMS/IVR, staff or low-cost tools |
| **CONDITIONAL** | INCOIS surge map | Authoritative service, but open machine access and farm resolution are not documented [15] |
| **CONDITIONAL** | Waterlogging meta-analysis | Strong prior for triage; not an Odisha parcel loss calculator [6] |
| **CONDITIONAL** | Groundwater annual recharge | Strong baseline; not a post-flood recharge rate [33] |
| **CONDITIONAL** | Pond/RWH and seed-bank stories | Demonstrate feasible institutions; need local structure/stock records and safety/viability checks [23][20] |
| **FILLER - exclude from decision logic** | "Floods recharge groundwater" without paired wells | Direction may be plausible, but event quantity is not established for the farm |
| **FILLER - exclude** | "Flood silt improves fertility" without chemistry | Deposits may instead be sand, salt or contaminated material |
| **FILLER - exclude** | Exact outbreak day derived only from rainfall | Blast, BPH and sheath blight require host/stage/inoculum or pest counts, not weather alone |
| **FILLER - exclude** | Tornado probability inferred from a thunderstorm alert | The documented warning categories do not supply a tornado-specific probability [8] |
| **FILLER - exclude** | District affected hectares as an individual claim | Administrative totals do not prove plot impact; PMFBY asks for plot/crop/acreage information [37] |

A useful AI layer ranks and explains rules; it does not manufacture missing observations. The MVP should be deterministic for safety-critical branches, multilingual in delivery and explicit about confidence and source time.

## 7. NOISE LOG

| Search path or candidate | Disposition | Reason discarded or downgraded |
|---|---|---|
| General news pages on Cyclone Asani/Dana | Discarded where official IMD report existed | News repeated forecasts without machine access, method or authoritative realized values |
| Scribd mirror of Odisha Groundwater Quality Year Book | Discarded | Unofficial mirror and uncertain file provenance; official CGWB/Odisha 2024 resource assessment was preferred |
| Dynamic INCOIS map shell | Retained only as service evidence | Page confirms the service but yields no documented API, grid, lead time or farm-resolution fields [15] |
| Global/Pakistan flood-recession crop-suitability study | Discarded from Odisha engine | Useful method, wrong geography and no Odisha calibration |
| Generic global waterlogging studies | Retained only as prior | They quantify stage/duration effects but cannot substitute for Odisha field depth-duration [6] |
| Global blast/sheath loss examples | Excluded from local loss prediction | Weather biology transfers better than loss percentages; local variety, inoculum and management differ |
| ResearchGate and non-Odisha flood-silt results | Discarded | No primary Odisha event dataset linking silt chemistry to yield was found |
| Commercial mandi-rate pages and generic dashboards | Discarded | DMI-derived portal preferred; commercial pages lacked closure/transport provenance |
| General tornado searches | Negative finding | Returned IMD's generic API and severe-weather products, not a tornado-specific operational feed |
| Generic groundwater bacterial/arsenic papers | Discarded | Wrong geography or chronic contamination, not post-cyclone Odisha ponds/wells |
| Crop-insurance blogs | Discarded | Official PMFBY guidelines directly state the 72-hour and evidence rules [37] |
| Yaas hectare figures with different scopes | Not merged | The 5,882 ha Balasore figure is kept with its source/date; differently scoped state/district figures should remain separate records rather than be summed |
| Community seed-bank advocacy claims | Downgraded to C unless audited | Institution existence is useful, but disaster drawdown, seed viability and farmer outcome need program records |
| Claims that pond refill, recharge or silt are automatically beneficial | Rejected | Positive use depends on infrastructure integrity, water/sediment quality and an actual irrigation or livelihood plan |

The noise pattern is informative: open-web sources are adequate for **examples and rule discovery**, but repeated searching does not create the hyperlocal observations the product needs.

## 8. VERDICT

### Overall grade: **PARTIAL**

| Capability | Grade | Can it run today with free/public data? | Blocking condition |
|---|---|---|---|
| Official hazard trigger and versioned alert | **GO** | Yes: IMD CAP/web/API documentation and CWC portals | API whitelisting/rate policy and robust caching for production |
| Basic crop-specific pre-disaster advisory | **GO/PARTIAL** | Yes for conservative rules using crop/stage profile and Odisha contingency plans | Farm profile accuracy; current state validation of recommendations |
| Hyperlocal post-disaster recovery | **PARTIAL** | Only after farmer/field observations | Water depth-duration, EC, access, seed and pest diagnosis |
| SMS text delivery | **GO** | Technically yes through a messaging provider | Telecom cost, consent, language and delivery receipts |
| Low-literacy IVR | **PARTIAL/GATED** | Scripts can be built; state-scale delivery should partner with AMAKRUSHI/OSDMA | IVR/telecom integration, voice content approval and escalation staffing |
| Claim packet preparation | **GO/PARTIAL** | Yes for evidence capture and deadline reminders | Current enrollment/notified crop, insurer intake and official claim status |
| Mandi/transport advisory | **PARTIAL** | Prices/arrivals yes; closure and route reliability no | Market authority, transport data and local verification |
| Positive-use recommendation | **GATED** | General structure advice only | Water/sediment test, structure inspection, allocation and measured storage |
| Named-flood recharge or silt-benefit claim | **NO-GO as an automated claim** | No | New study/field measurements |

### What the free prototype should contain

1. **Source adapters:** IMD CAP/API/bulletins and CWC station forecasts, with event IDs, timestamps, geography, version history and failure fallback. IMD itself used national, hourly, SMS, social and customized bulletins during Dana, demonstrating the need to deduplicate many channels into one event record. [9]
2. **Minimal farm profile:** village/GPS or plot ID, crop, variety, sowing/transplant date, stage, acreage, irrigation/drainage, coastal/saline history, preferred language and SMS/voice mode.
3. **A conservative rule engine:** official Odisha contingency actions plus threshold-based scouting; no generative pesticide dose or resowing clearance without a current approved rule.
4. **Post-event micro-survey:** water source, saline taste/EC if available, field depth/start/end, crop stage, lodging, pest count/symptoms, seed exposure, road/mandi access and geotagged evidence.
5. **Claim timer and packet:** 72-hour countdown, insurer/channel details, survey number, crop/acreage, timestamped photos, official-event evidence and receipt storage. [37]
6. **SMS/IVR response design:** one hazard, one action, one deadline per message; numbered keypad responses; replay and human escalation. OSDMA already disseminates message, voice and siren warnings across state/district/block infrastructure, while the Odisha crop plan documents AMAKRUSHI IVRS at scale. [5][22]

### What must be collected

Collect plot water depth-duration, EC, seed viability, pest counts/diagnosis, pond/well quality, lodging/photos, route/mandi status and household recovery constraints. Store raw observation, unit, method, observer, timestamp, location, consent and confidence; never store only the AI interpretation.

### What needs a partner

- **IMD/RMC Bhubaneswar:** production access, attribution, alert semantics and escalation.
- **INCOIS:** surge/inundation raster, metadata, lead time, versioning and permitted reuse.
- **OSDMA and AMAKRUSHI/Odisha Agriculture:** last-mile voice/SMS, farmer profiles, approved advisory content and feedback.
- **CWC/DoWR and groundwater agencies:** gauges, releases, monitoring wells and command-area data.
- **OUAT/ICAR-NRRI/KVKs and soil/water laboratories:** diagnosis, EC/water tests, local thresholds and safe recovery clearance.
- **PMFBY insurers/state nodal agency:** enrollment, loss-intimation receipt and claim status.
- **Regulated markets/transport providers/SHGs and banks:** closure, logistics, price and household recovery information.

The build decision is therefore **PARTIAL, proceed with a bounded MVP**. Build the official-trigger, farm-profile, conservative-advisory, field-observation and claim-packet core now. Label parcel impact as "unverified" until observed. Gate resowing, chemical treatment, water reuse and recharge/fertility claims behind measurements or partners.

## Synthesis

| Dimension | Live hazard systems | Agronomy evidence | Socioeconomic/market evidence | Positive-use evidence |
|---|---|---|---|---|
| Mechanism | Detect atmosphere, coast and river state | Translate exposure plus crop stage into biological risk | Describe execution constraints and recovery choices | Convert stored freshwater, infrastructure or seed diversity into future production |
| Spatial scope | Cyclone, district, station, basin | Crop/stage; sometimes Odisha-wide, rarely plot | Household, village or market; often retrospective | Structure, aquifer block, command area or community |
| Time horizon | Minutes to 7.5-day early signal in the Dana case [9][18] | Days to a season; some annual contingency plans | Days for claims, months/one year for household recovery [37][3] | Season to multi-year planning |
| Strongest evidence | Official issue times, categories and bulletins | Quantified thresholds and stage/duration effects | PMFBY administrative rules; household survey associations | Engineered farm-pond studies and annual groundwater accounting |
| Central trade-off | Authoritative but too coarse for a farm | Specific biologically but not automatically local/current | Actionable administratively but fragmented and sensitive | Potentially beneficial but unsafe to generalize from any flood |
| Correct engine role | Trigger and prioritize | Generate conditional rule and scouting prompt | Route services, deadlines and feasible options | Recommend only after quality, integrity and allocation gates |

The non-obvious tension is that the most authoritative sources are the least farm-specific, while the most farm-specific observations are the least standardized. A reliable system should not try to resolve that tension with a larger language model. It should resolve it with provenance, short farmer questions, simple field measurements, approved rules and an abstention state.

A second tension is temporal. Warnings arrive quickly, but salinity, disease, debt and migration unfold on different clocks. One "post-cyclone" message is therefore structurally wrong. The engine needs a cascade scheduler: immediate safety and claim reminders; 24-72 hour depth/EC/access checks; 3-7 day scouting and seed tests; then seasonal soil, credit, market and water planning. The cited blast evidence supports a 3-5 day symptom-development watch under favorable conditions, but not a guaranteed outbreak date. [36]

Finally, positive use cannot be the cheerful mirror image of loss. Engineered rainwater harvesting can support supplemental irrigation and integrated livelihoods, yet seawater intrusion, contaminated ponds, damaged embankments and untested silt create opposite advice. The decision rule is simple: **capture is an opportunity; reuse is a clearance decision**.

## References

1. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
2. *Cyclone Yaas: A Curse to Coastal People of Odisha and West Bengal (India) | National Academy Science Letters | Springer Nature Link*. https://link.springer.com/article/10.1007/s40009-023-01251-w
3. *Flood shocks and post-disaster recovery of households: An empirical analysis from rural Odisha, India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212420923005502
4. *IMD APIs | India Meteorological Department*. https://mausam.imd.gov.in/responsive/apis.php
5. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Early Warning Dissemination System (EWDS)*. http://osdma.org/preparedness/early-warning-communications/ewds
6. *Frontiers | How Does the Waterlogging Regime Affect Crop Yield? A Global Meta-Analysis*. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.634898/full
7. *Full article: Remote sensing-based site suitability assessment and selection of Rabi crop cultivation areas following flood events*. https://www.tandfonline.com/doi/full/10.1080/10106049.2024.2356841
8. *Api Reference*. https://api.imd.gov.in/public/api_reference.html
9. *Severe Cyclonic Storm “DANA” over the Bay of Bengal (22 -26 October, 2024): A Report (b) (a)*. https://internal.imd.gov.in/press_release/20241107_pr_3389.pdf
10. *Cyclone Yaas aftermath: Odisha farmers in a fix over sowing Kharif crop*. https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568
11. *Odisha FANI cyclone Assessment Report*. https://ircsstoragedev.blob.core.windows.net/wordpresswebsite/2024/03/OdishaFaniAsessmentReport.pdf
12. *Flood Forecast - Central Water Commision, Govt. Of India*. https://ffs.india-water.gov.in/
13. *Stormsurge*. https://www.incois.gov.in/oceanservices/Stormsurge/index.html
14. *DIVERSIFARM India- Unfolding the Potential of Community Seed Banks for Food and Nutrition Security among Smallholder Farmers in India through the Realisation of Farmers’ Rights | M S Swaminathan Research Foundation *. https://www.mssrf.org/projects/diversifarm-india-unfolding-potential-community-seed-banks-food-and-nutrition-security
15. *incois.gov.in*. https://incois.gov.in/site/services/StormSurge.jsp
16. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
17. *Crop Contigency Plan 2025*. https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
18. *Flood Forecasting/ Hydrological Observation | Central Water Commission, Ministry of jal shakti, Department of Water Resources, River Development and Ganga Rejuvenation, GoI*. https://cwc.gov.in/flood-forecasting-hydrological-observation
19. *Seeds of Hope, Seeds of Resilience – Navdanya*. https://navdanya.org/seeds-of-resilience
20. *The quiet power of seed keepers in Odisha’s community seed banks | M S Swaminathan Research Foundation *. https://www.mssrf.org/stories-of-change/seed-keepers-odishas-community-seed-banks
21. [
		Rainwater Harvesting for Supplemental Irrigation to Enhance Crop Productivity under Rainfed Conditions: A Case Study of North Eastern Ghats Zone of Odisha
							| Journal of Agricultural Engineering (India)
			](https://pub.isae.in/index.php/jae/article/view/1208)
22. *Crop Contingency Plan 2024 Final*. https://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf
23. *How Rainwater Harvesting Is Transforming Seasonal Farming into Year-Round Livelihoods in Odisha’s Koraput District*. https://www.downtoearth.org.in/agriculture/how-rainwater-harvesting-is-turning-seasonal-farming-into-year-round-livelihoods-in-this-odisha-district
24. * *. https://ijcmas.com/9-6-2020/Ashok%20Kumar%20Das%2C%20et%20al.pdf
25. *Home-Agmarknet 2.0*. http://34.0.13.160/
26. [
		Effect of meteorological factors on rice sheath blight and exploratory development of a predictive model
							| The Indian Journal of Agricultural Sciences
			](https://epubs.icar.org.in/index.php/IJAgS/article/view/4572)
27. [
		Impact of soil and water conservation measures on groundwater recharge, irrigation potential and productivity of crops of a watershed
							| Indian Journal of Soil Conservation
			](https://ijsc.iaswc.com/index.php/ijsc/article/view/444)
28. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://www.pmfby.gov.in/
29. *Microsoft Word - AAS_May_2024_I_English*. https://icar-crri.in/wp-content/uploads/2024/04/AAS_May_2024_I_English.pdf
30. *BPH, Nilaparvata lugens Stal,Rice brown planthopper (BPH),Rice pests of DSS, croppest DSS *. http://www.icar-crida.res.in:8080/naip/bph.jsp
31. *Analyzing water level variability in Odisha: insights from multi-year data and spatial analysis | Discover Applied Sciences | Springer Nature Link*. https://link.springer.com/article/10.1007/s42452-024-05958-3
32. *Sheath blight - IRRI Rice Knowledge Bank*. http://knowledgebank.irri.org/decision-tools/rice-doctor/rice-doctor-fact-sheets/item/sheath-blight
33. *DYNAMIC GROUND WATER RESOURCES OF ODISHA, 2024*. https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17435864691666329414file.pdf
34. *CEDA Agri Market Data*. https://agmarknet.ceda.ashoka.edu.in/
35. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://pmfby.gov.in/guidelines
36. *Rice Blast: A Disease with Implications for Global Food Security*. https://www.mdpi.com/2073-4395/9/8/451
37. *Revised Operational Guidelines*. https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf
38. *Blast (leaf and collar) - IRRI Rice Knowledge Bank*. http://www.knowledgebank.irri.org/training/fact-sheets/pest-management/diseases/item/blast-leaf-collar
39. *http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf*. http://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf
