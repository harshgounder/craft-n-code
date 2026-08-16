# Odisha Crop Data Readiness for Resilient Advisories

## 1. EXECUTIVE SUMMARY

- **Prototype is viable, but quantified loss advice is not**: Free official data can support district routing, crop-season priors, tolerant-variety suggestions, IMD warning ingestion, and rule-based pre/post-disaster messages. It cannot yet support a defensible Odisha-specific "wait 24 hours and lose X%" claim because no public source supplies a locally validated hazard x intensity x duration x crop x stage x variety loss matrix [12][16].

- **Paddy is both dominant and spatially concentrated**: Paddy covered **41.24 lakh ha**, or **44% of gross cropped area**, in 2024-25. Bargarh, Mayurbhanj, and Kalahandi were the three largest paddy-producing districts in the current official district table [18]. These districts should be first-wave targets alongside cyclone-exposed coastal districts.

- **The other requested crops are visible at state level, not as one current open district map**: Odisha reported **21.07 lakh ha of pulses, 7.91 lakh ha of vegetables, 2.27 lakh ha of spices, 2.71 lakh ha of millets, and 2.39 lakh ha of cotton** in 2024-25; oilseed production was **6.2 lakh MT** [18]. Pulses are reported as grown in all 30 districts, but current district rankings for pulses, oilseeds, vegetables, coconut, cashew, and spices were not exposed through a single usable public file [24].

- **Calendar priors exist, but they are not field-stage truth**: IMD's 2002 Odisha crop-weather calendar covers district clusters and crops including paddy, groundnut, mustard, mung, maize, and ragi. It places kharif paddy broadly between May/June and October/December and rabi paddy at Cuttack between December and April [21]. A farmer's actual sowing/transplanting date and variety duration are still required to determine tillering, panicle initiation, booting, flowering, and grain filling.

- **October-November risk overlaps different stages in different regions**: Puri's calendar extends through flowering, grain formation, and harvest from May to December, while the Mayurbhanj-Bolangir-Dhenkanal calendar reaches harvest by October [21]. The engine must therefore say "likely stage" until the farmer confirms transplanting date and current stage; a statewide rule that every October-November cyclone hits flowering or maturity would be false.

- **Swarna-Sub1 is operationally useful, but only within its tested envelope**: ICAR-NRRI lists Swarna-Sub1 for Odisha flood-prone shallow lowlands, with **145-day duration, 5.2 t/ha yield potential, and tolerance to 15-17 days of complete submergence** [9]. That is a variety specification, not a universal kill threshold for all rice varieties or reproductive stages.

- **Public fragility evidence is transferable only as a provisional prior**: A Myanmar rice-damage model estimates, at 1.0 m depth and eight days, damage of **50% in the vegetative stage, 40% in the reproductive stage, and 36% at maturity** [16]. It was not validated in Odisha and should be shown internally as a research prior with a wide uncertainty band, not sent to farmers as a precise loss forecast [16].

- **Fresh-water flooding, salinity, and wind must be separate hazards**: Controlled salinity studies found a fitted threshold of **1.9 dS/m** and a **9.1% yield-decline slope**, while exposure from the three-leaf stage to panicle initiation caused the largest reductions in several yield components [17]. A Japanese lodging study found full-ripening rice bending at 7-8 m/s and nearly 90 degrees at 12-14 m/s, but these old, non-Odisha observations are not local warning thresholds [19].

- **Farmer capability data are aggregate, not addressable**: In 2024-25, Odisha supplied 79,100 subsidized machines to 74,605 farmers, including 11,755 power tillers and 7,827 tractors; it also reported 44.54 lakh KCCs and INR 76.1 thousand crore in agricultural loans [18]. These totals cannot tell the engine whether a particular farmer has a pump, tractor, labor, storage, credit headroom, or transport today. Those facts require enrollment and IVR confirmation.

- **Overall verdict: PARTIAL**: A free prototype can produce timely, conservative advisories today. Quantified cost-of-waiting estimates, parcel-level feasibility, and claim-grade damage attribution remain gated by field collection, local calibration, and institutional data partnerships.

## 2. DATA INVENTORY

**Reliability scale:** A = official and reasonably current for the stated use; B = authoritative but stale, aggregated, or technically awkward; C = credible research but not validated for Odisha operations; D = inaccessible, decorative, or unfit for the intended decision.

| Data item | Named source, URL, and date | Granularity | Freshness | Access path | Grade |
|---|---|---|---|---|---:|
| Current state crop mix and paddy dominance | *Odisha Economic Survey 2025-26*, Government of Odisha, February 2026. `https://finance.odisha.gov.in/sites/default/files/2025-08/OES%202025-26%20Main%20Booklet.pdf` [18] | State; 2024-25 crop totals | Current | Free PDF/report | A |
| Current district paddy map | Same Economic Survey, Table 3.6, 2024-25 [18] | District production, all 30 districts | Current | Free PDF/report | A |
| District map for pulses, oilseeds, vegetables, coconut, cashew, spices | Odisha Agriculture Statistics listing, including the named 2023-24 edition. `https://agri.odisha.gov.in/en/page/statistics` [25] | Intended district/crop tables, but the file was not machine-retrievable in this run | Current title; access unresolved | Free report listing; direct file extraction failed | C |
| State pulse coverage | RKB Odisha, *Pulses in Odisha*, date not exposed. `https://rkb-odisha.in/pulses-in-odisha` [24] | State; states all 30 districts | Undated | Free web page | B |
| District-cluster crop calendars | IMD, *Crop Weather Calendars for Orissa*, 2002. `https://www.imdpune.gov.in/library/crop/CWC_Odhisha.pdf` [21] | District or district cluster; crop; week/month; broad stage | Very stale | Free PDF | B for priors; D for exact current stage |
| Current contingency actions and sowing windows | Odisha Department of Agriculture and Farmers' Empowerment, *Crop Contingency Plan 2025*. `https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf` [12] | State plus district sowing-window tables; named hazards/actions | Current | Free PDF; some text encoding is poor | A for official actions; B for machine extraction |
| Current IMD advisory and cyclone channels | IMD Agromet Advisory Services and Cyclone Information. `https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php`; `https://mausam.imd.gov.in/responsive/cycloneinformation.php` [22][23] | Warning/advisory product dependent | Live | Free web; API/feed terms need implementation testing | A for source; B for integration readiness |
| Released flood/saline rice varieties | ICAR-NRRI, *Released Varieties*, page dated January 31, 2026. `https://icar-crri.in/released-varieties` [9] | Variety, ecology, release year, duration, yield, target state | Current catalogue | Free web table | A |
| Swarna-Sub1 local adoption response | Dar et al., *Private Input Suppliers as Information Agents for Technology Adoption in Agriculture*, May 26, 2021. `http://povertyactionlab.org/sites/default/files/research-paper/working-paper_5092_Private-Input-Suppliers-As-Information-Agents_India_May2021.pdf` [20] | 10 flood-prone Odisha districts; block, dealer, farmer sample | 2016-2020 study data | Free research PDF | B |
| Rice flood depth-duration-stage functions | Shrestha et al., *Development of flood damage functions for agricultural crops and their applicability in regions of Asia*, 2021. `https://www.sciencedirect.com/science/article/pii/S2214581821001014` [16] | Stage x depth x duration; Myanmar model and Asian transfer tests | Method current enough; geography mismatched | Free article text in this run | C; D for direct farmer percentages |
| Rice salinity response | Grattan et al., *Rice is more sensitive to salinity than previously thought*. `https://www.ars.usda.gov/arsuserfiles/20361500/pdf_pubs/P1837.pdf` [17] | Controlled field and greenhouse experiments; EC x timing/stage | Old; non-Odisha | Free PDF | C |
| Rice lodging thresholds | Hitaka, *Studies on the Lodging of Rice Plants*, Japan, 1968. `https://www.jircas.go.jp/sites/default/files/publication/jarq/04-3-001-006_0.pdf` [19] | Experimental wind/rain observations at ripening | Very stale; non-Odisha | Free PDF | C for mechanism; D for warning threshold |
| State inputs and machinery distribution | *Odisha Economic Survey 2025-26*, Tables 3.4, 3.12, 3.13 and mechanization text [18] | State; some district input columns; subsidy distribution | Current | Free PDF | A for aggregate context; D for household capability |
| Irrigation potential | *Odisha Economic Survey 2025-26*, 2024-25 [18] | State and source category | Current | Free PDF | A for planning context |
| Minor-irrigation schemes | Sixth Minor Irrigation Census, reference year 2017-18. `https://mowr.nic.in/core/WebsiteUpload/2023/MI6.pdf` [14] | State total; limited status data extracted | Stale | Free PDF/report | B |
| Rural debt/financial inclusion | NABARD, *NAFIS 2021-22*. `https://www.nabard.org/auth/writereaddata/tender/2102255939NAFIS%202021-22%20Report%20Final.pdf` [1] | State estimates where published | 2021-22 | Free report | B |
| Detailed farmer expenses and operational inputs | MOSPI, NSS Report 587, 2019. `https://mospi.gov.in/sites/default/files/publication_reports/Report_587m_0.pdf` [11] | Survey/microdata design; requested Odisha input rows not retrievable from the report extraction | 2019 | Free report; microdata access separately required | C |
| Cadastral land-use context | ORSAC Odisha 4K Geo. `https://odisha4kgeo.in/` [7] | Cadastral land use and geotagged assets | Update/API status not established | Free portal view; data export/rights unclear | B for viewing; C for engine ingestion |
| Parcel crop, variety, stage, inputs, machinery access and farmer language | No complete public source located | Farmer/plot/event | Must be live | Enrollment, IVR/SMS confirmation, field collection | A if farmer-verified and timestamped; otherwise D |

### Evidence-backed crop and regional map

| Crop or system | What is currently supported | Coastal versus interior interpretation |
|---|---|---|
| Paddy | **41.24 lakh ha** in 2024-25; current production leaders were **Bargarh, Mayurbhanj, and Kalahandi** [18] | Paddy is statewide. The current leaders are mainly western/northern-interior districts, while IMD also has dedicated coastal calendars for Cuttack, Ganjam, Puri, and Balasore [21]. Exposure and production concentration are not the same map. |
| Pulses | **21.07 lakh ha** in 2024-25; reported across all 30 districts [18][24] | A current public district ranking was not recovered. Do not infer "interior-only" or "coastal-only" from the state total. |
| Oilseeds | **6.2 lakh MT** production in 2024-25 [18] | IMD calendars identify mustard in Mayurbhanj, Balasore, and Phulbani and groundnut in Dhenkanal, Sambalpur, and Ganjam, but this 2002 coverage is a calendar map, not a current production ranking [21]. |
| Vegetables | **7.91 lakh ha** and **111.02 lakh MT** in 2024-25 [18] | No verified current district split was exposed. |
| Spices | **2.27 lakh ha** in 2024-25 [18] | No verified current district split was exposed. |
| Coconut and cashew | The latest Economic Survey passages extracted here did not provide a current district table for either crop | Coastal concentration may be agronomically plausible, but the engine must not encode it as a district fact without a horticulture department or crop-board table. |

**Takeaway:** the usable current crop map is strong for paddy and state totals, but incomplete for district-level diversification. A prototype should use paddy-first deployment and mark non-paddy district assignments as "farmer-confirmed" unless a district table is obtained.

### Calendar and stage resolution

| Region represented in IMD's 2002 calendar | Kharif paddy window and stages exposed | Rabi coverage | Operational interpretation |
|---|---|---|---|
| Cuttack | June-December; sowing, transplanting, vegetative growth, harvest; 110-155 days [21] | December-April; sowing/transplanting, vegetative growth, flowering, grain formation; 90-135 days [21] | Useful season prior, not a live stage label. |
| Mayurbhanj-Bolangir-Dhenkanal | June-October; sowing/transplanting, vegetative growth, harvest; 100-135 days [21] | Not extracted | An October event can arrive near harvest for early crops. |
| Ganjam | May-December; sowing/transplanting, vegetative growth, flowering; 110-155 days [21] | Not extracted | Coastal cyclone overlap may include flowering, but variety and planting date decide it. |
| Kalahandi-Sambalpur | May-December; sowing/transplanting, vegetative growth, flowering, harvest; 110-155 days [21] | Not extracted | Long regional window creates high stage uncertainty without farmer data. |
| Puri | May-December; sowing/transplanting, vegetative growth, flowering, grain formation, harvest; 150-175 days [21] | Not extracted | Late-duration coastal paddy can overlap October-November flowering/grain filling/harvest. |
| Balasore | May-December; Swarna-1009, 140-155 days; broad sowing/transplanting and vegetative window [21] | Not extracted | Calendar alone does not resolve reproductive stages. |
| Sundargarh | May-October; sowing/transplanting, vegetative growth, harvest; 100-135 days [21] | Not extracted | Interior early crop may already be mature when a late cyclone arrives. |

No retrieved public calendar gives reliable, current, region-specific fixed dates for all requested paddy stages: nursery, transplanting, tillering, panicle initiation, booting, flowering, grain filling, and maturity. The correct prototype representation is:

`likely stage = farmer planting/transplanting date + variety duration curve + district calendar prior + latest farmer confirmation`

It should retain an uncertainty label such as "likely flowering, confirm by IVR" rather than silently converting a month into a stage.

### Fragility values that may seed, but not finalize, the engine

| Hazard | Public quantitative evidence | Safe prototype use | Unsafe use |
|---|---|---|---|
| Complete fresh-water submergence | Swarna-Sub1: 15-17 days tolerance in Odisha-targeted release information [9] | Variety-specific next-season recommendation and a conservative survival prior | Declaring that every paddy crop dies on day 18 |
| Flood depth-duration by broad rice stage | At 1.0 m for 8 days, Myanmar model damage was 50% vegetative, 40% reproductive, 36% maturity; model R-squared values were 0.835-0.854 [16] | Internal scenario range clearly labeled "unvalidated in Odisha" | Farmer-facing exact yield-loss or compensation figure |
| Complete-submergence duration in Myanmar model | Model reaches 100% damage at 27 days for vegetative/reproductive and 24 days at maturity [16] | Upper-bound research prior | A kill-day table for Odisha varieties |
| Salinity | Yield response fitted a 1.9 dS/m threshold and 9.1% decline slope; three-leaf through panicle-initiation exposure was especially damaging [17] | Trigger EC testing, drainage, fresh-water flushing advice, and separate saline-flood classification | Converting sea-water exposure hours directly into a loss percentage |
| Wind lodging in rice | Full-ripening rice bent about 45 degrees at 7-8 m/s, nearly 90 degrees at 12-14 m/s, and almost all culms broke at 15-16 m/s in a 1968 Japanese study [19] | Explain that wet, ripe, tall crops are more lodging-prone; prioritize harvest/staking/drainage where agronomically approved | Odisha warning thresholds without local cultivar and canopy validation |
| Wind plus rain | Rain with 15 m/s wind produced about 20% more broken culms than wind alone [19] | Treat wind and rain jointly in the risk model | Additive universal loss percentages |
| Other requested crops | No Odisha-validated stage x wind/flood/salinity loss table was found for pulses, oilseeds, vegetables, coconut, cashew, or spices | Qualitative crop-specific contingency rules and post-event scouting | Quantified "cost of waiting" claims |

### Tolerant varieties with Odisha evidence

| Variety | Ecology and release | Duration/yield | Verified stress statement |
|---|---|---|---|
| Lunishree | Coastal saline; 1992; Odisha | 145 days; 4.75 t/ha | Tolerant to salinity [9] |
| Sonamani | Coastal saline; 1996; Odisha | 155 days; 4.5 t/ha | Coastal-saline ecology; source also notes susceptibility to yellow stem borer [9] |
| Swarna-Sub1 | Flood-prone shallow lowland; 2009; Odisha | 145 days; 5.2 t/ha | Complete-submergence tolerance for 15-17 days [9] |
| Luna Suvarna, CR Dhan 403 | Coastal saline; 2010; Odisha | 150 days; 3.5-4.0 t/ha | Coastal-saline ecology [9] |
| Luna Sampad, CR Dhan 402 | Coastal saline; 2010; Odisha | 140 days; 3.6-4.2 t/ha | Coastal-saline ecology [9] |
| Luna Barial, CR Dhan 406 | Coastal saline; 2012; Odisha | 150 days; 4.1 t/ha | Coastal-saline ecology [9] |
| Luna Sankhi, CR Dhan 405 | Coastal saline; 2012; Odisha | 110 days; 4.6 t/ha | Coastal-saline ecology [9] |
| CR Dhan 505 | Deep water; 2014; Odisha and Assam | 162 days; 4.5 t/ha | Submergence tolerance plus elongation ability [9] |
| CR Dhan 801 | Shallow lowland; 2019; includes Odisha | 140 days; 6.3 t/ha | Intended for both submergence- and drought-prone areas [9] |
| CR Dhan 412 | Coastal ecology; 2021; Odisha | 140 days; yield not stated in the table | Coastal-salinity tolerance and moderate stagnant-flood tolerance [9] |

The retrieved NRRI catalogue did not verify a CSR-series variety as Odisha-released or distributed. CSR varieties should therefore remain a candidate list pending Odisha Seed Corporation, ICAR-CSSRI, or state seed-chain confirmation.

The strongest adoption evidence is not a statewide adoption rate. In 10 flood-prone Odisha districts, an agro-dealer intervention raised Swarna-Sub1 adoption by **3.5 percentage points from a 6.3% control mean**; the effect was **6.4 points for higher-flood-risk farmers versus 0.8 points for lower-risk farmers** [20]. This proves information and local stocking can shift uptake; it does not reveal present statewide seed availability.

### Farmer inputs and capability

- Total NPK use was **78.2 kg/ha** in 2024-25: N 42.6, P 19.9, and K 5.1 kg/ha [18]. Pesticide use was **0.22 kg/ha of technical-grade active ingredient**, not 78.2 kg/ha [18].
- Paddy's seed replacement rate was **28.31%** in 2024-25 [18]. This is a state rate, not the variety on an enrolled plot.
- Odisha created **74.2 lakh ha** of kharif-plus-rabi irrigation potential in 2024-25, close to 80% of gross cropped area, but utilized only **62.5%** of created potential [18]. Source shares were 34% minor lift, 32% major/medium, 12% minor flow, 4% mega lift, and 18% other [18].
- The Sixth Minor Irrigation Census counted **510,581 schemes** in Odisha in 2017-18; **43,620** were temporarily or permanently not in use [14]. It does not resolve a farmer's current pump or water access.
- The 2024-25 machinery numbers are machines **supplied under subsidy**, not an ownership census [18].
- NAFIS 2021-22 reports **61% indebtedness** for Odisha, while the requested Odisha-specific KCC, institutional-source, loan-amount, insurance, income, savings, and investment rows were not published in the retrieved tables [1].
- The Economic Survey's **44.54 lakh KCCs** and **INR 76.1 thousand crore** in agricultural lending are program totals, not a roster of unique farmers with usable emergency credit [18].

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing content | Coverage judgment |
|---|---|---|---:|
| Odisha Economic Survey 2025-26 | Current crop totals, district paddy table, irrigation, fertilizer, pesticides, seed replacement, machinery distribution, KCC and credit [18] | No unified current district table for every requested crop; no household capability | A for state/district-paddy context; C for personalization |
| Odisha Agriculture Statistics/DES | Named 2023-24 statistics listing [25] | Direct current file could not be extracted; district non-paddy table remained unresolved | C in this run |
| IMD crop-weather calendars | District-cluster calendars for paddy and five other crops; broad stages and hazards [21] | Published in 2002; no current sow-date observations; stages too broad | B for priors; D for exact stage |
| Odisha Crop Contingency Plan 2025 | Current official pre/post cyclone, flood, excess-rain, saline-soil and sowing-window sections [12] | Encoding corruption; many dates/actions require manual curation | A for authority; B for machine readiness |
| ICAR-NRRI variety catalogue | Odisha-targeted saline, submergence and deep-water varieties with duration/yield [9] | Distribution stock and district adoption are absent | A for eligibility; C for availability |
| Odisha Swarna-Sub1 field research | Large 10-district experiment with farmer/dealer behavior and flood-risk heterogeneity [20] | Historical intervention, not current statewide adoption | B |
| Peer-reviewed Asian flood functions | Numeric depth-duration-stage curves and validation statistics [16] | Myanmar calibration; no Odisha validation or variety detail | C for research; D for farmer-facing loss |
| USDA/UC salinity experiments | EC threshold, exposure timing and stage sensitivity [17] | Not cyclone saltwater inundation; non-Odisha genotypes and water conditions | C |
| Rice lodging experiments | Quantifies wind, wet-weight and ripening effects [19] | Japan, 1968; no Odisha cultivar/canopy calibration | C/D |
| NAFIS/NSS | Odisha indebtedness and national survey framework [1][11] | Most requested Odisha-specific input, KCC and expense rows unavailable in retrieved reports | C |
| Minor Irrigation Census | State scheme total and non-use status [14] | Old reference year; no farmer linkage; many Odisha class totals not exposed | B |
| IMD live warning/advisory pages | Authoritative operational warning and advisory entry points [22][23] | Feed stability, licensing, authentication and structured-field coverage require integration tests | A for authority; B for access readiness |
| Horticulture portal and general web search | Identified the Directorate of Horticulture portal | No usable current district table recovered for vegetables, coconut, cashew and spices | D for present engine use |

**Coverage judgment:** spatial-seasonal context is good enough for a paddy-first prototype. Stage truth, parcel capability, and calibrated loss functions are the critical weak layers.

## 4. WHAT IS MISSING

The following gaps should be named exactly in the project backlog. They are not safe to fill by interpolation.

1. **Current district x crop x season area, production, and yield table for pulses, oilseeds, vegetables, coconut, cashew, and spices.** State totals exist, but one current, openly machine-readable district table was not recovered.

2. **Plot-level crop and variety registry.** Public statistics cannot state what is currently planted on a particular farmer's parcel.

3. **Plot-level sowing, nursery, and transplanting date.** Without this, the engine cannot reliably distinguish tillering, panicle initiation, booting, flowering, grain filling, and maturity.

4. **Odisha-calibrated phenology curves by variety, establishment method, district, and season.** The 2002 IMD calendars expose broad stages, not current stage-date functions [21].

5. **Rice kill-days table by stage, variety, water depth, turbidity, temperature, and recovery condition.** Swarna-Sub1's 15-17 day specification is variety-specific [9]; the Myanmar curves are not Odisha kill thresholds [16].

6. **Odisha yield-loss matrix: flood depth x duration x crop stage x variety.** No validated local table was found for paddy, pulses, oilseeds, vegetables, coconut, cashew, or spices.

7. **Saltwater-inundation loss function: salinity x duration x stage x drainage delay.** Existing experiments vary electrical conductivity and timing, not cyclone saltwater residence time [17].

8. **Odisha wind-lodging and tree-crop breakage thresholds.** No local cultivar/canopy thresholds were found for paddy, coconut, cashew, vegetables, pulses, or oilseeds. The Japanese rice observations are mechanism evidence only [19].

9. **Current district/block inventory and retail availability of tolerant seed.** Release eligibility does not establish stock at a dealer, seed lot quality, price, or delivery time.

10. **Current adoption rate and planted area for Swarna-Sub1, saline varieties, and CSR varieties.** The Odisha experiment measured an intervention effect, not a present statewide denominator [20].

11. **Household machinery access, not just ownership.** The engine needs tractor, power tiller, pump, harvester, sprayer, transport, operator, fuel and rental availability at warning time. Subsidized distribution totals do not answer this [18].

12. **Field-level irrigation source and drainage outlet status.** State irrigation potential and scheme counts do not establish whether a farmer can drain, flush saline water, or irrigate after the event [18][14].

13. **Timestamped seed, fertilizer, pesticide, labor, storage, livestock and credit profile.** NSS/NABARD aggregates cannot drive individual feasibility decisions.

14. **Claim-grade event evidence standard.** Required fields include pre-event crop/stage, geotagged parcel, warning timestamp, water depth and duration, salinity test, post-event images, assessor record, and insurer/government scheme identifiers.

15. **Observed Odisha loss-and-recovery training set.** The engine needs paired hazard, farm, action, damage, yield and recovery-cost records, including farms that took no action. Without counterfactuals, it cannot learn a credible "cost of waiting."

16. **Stable machine-readable interfaces and rights.** IMD, ORSAC, land-record, insurance and departmental portals must be tested for structured access, rate limits, authentication, licensing and production reliability.

17. **Language and accessibility profile.** Phone number, preferred language/dialect, call time, IVR consent, hearing constraints and trusted local contact are not agricultural statistics but are mandatory for low-literacy delivery.

## 5. HOW IT FEEDS THE ENGINE

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD cyclone, rain, flood and wind alert | Set location, lead time, severity and message deadline | Determine when field inspection is safe | Preserve alert ID, issue time and forecast footprint | Build event history | Weather-timed routine operations when no extreme alert exists |
| Parcel location and elevation | Match warning polygon, drainage basin and coastal/saline exposure | Route local recovery and input support | Geotag the affected plot | Identify recurring flood/salinity risk | Location-specific crop and water advice |
| District crop map | Prioritize likely crops before farmer confirmation | Prepare crop-specific scouting workflow | Check crop plausibility, never replace field evidence | Target extension and seed supply | District-season crop options |
| Farmer crop, variety and planting date | Resolve likely stage and remaining harvest time | Select replant, ratoon, drainage or salvage branch | Establish pre-event crop and stage | Compare variety fit and duration | Routine stage-timed nutrition and pest prompts |
| Stage uncertainty/IVR confirmation | Ask one short question: "Is the crop flowering, grain filling, or ready to harvest?" | Reconfirm visible symptoms after the event | Store farmer response and timestamp | Improve local phenology model | Personalize future reminders |
| Flood depth, duration and water type | Move seed, inputs, livestock and portable equipment; prepare drainage only when safe | Separate brief fresh-water flooding from prolonged or saline inundation | Record depth, start/end times and salinity reading | Select submergence/salinity-tolerant ecology | Water-management advice |
| Crop-stage fragility prior | Rank urgency and select conservative action class | Rank scouting and replant priority | Provide an uncertainty-bounded technical note, not a payout estimate | Guide trial design | Explain why stage confirmation matters |
| Wind/lodging prior | Prioritize ripe, tall or wet stands for approved early harvest/support actions | Separate bent from broken plants and plan drying/harvest | Record lodging fraction and wind/rain context | Select lodging-resistant varieties and balanced nutrition | Canopy and harvest management |
| Tolerant-variety catalogue | Usually no immediate pre-event change once crop is planted | Identify replacement seed suitable for the ecology | Document the planted variety if known | Recommend only varieties released for the farmer's ecology and available locally | Seed-choice education before planting |
| Irrigation and drainage capability | Avoid advice requiring pumps or drainage that the farmer cannot execute | Route pump rental, fresh-water flushing, canal or pond support | Record infrastructure affected | Invest in drainage, raised storage, pump groups or water harvesting | Schedule irrigation efficiently |
| Machinery, labor and transport access | Decide whether early harvest, bund repair, input relocation or livestock movement is feasible | Arrange shared machinery and labor | Record hired services and receipts | Promote custom-hiring or producer groups | Normal mechanization scheduling |
| Inputs and storage | Move seed, fertilizer and pesticides above flood level; secure containers | Prevent contaminated-input use and plan replacement | Photograph lots, labels, quantities and invoices | Adjust resilient seed/input procurement | Timely input reminders |
| Credit/KCC/insurance profile | Avoid assuming emergency cash exists | Route KCC, relief, insurance and bank contacts | Attach policy/KCC identifiers and documents | Plan finance before cyclone season | Repayment and scheme reminders |
| Farmer language and channel | Generate a short Odia/local-language SMS and IVR call with deadline | Deliver symptom-based recovery prompts | Explain evidence requirements orally | Deliver pre-season voice modules | Reinforce successful practices |

### Recommended decision flow

1. **Ingest the official alert.** Preserve source, warning issue time, expected onset, hazards, affected geography and update cadence.
2. **Resolve the farm.** Match the farmer's parcel or village, then load crop, variety, planting date, irrigation, machinery, labor and channel profile.
3. **Infer stage with uncertainty.** Use the district calendar only as a prior. If the decision changes across plausible stages, ask the farmer by IVR.
4. **Apply hazard-specific logic.** Flood depth/duration, salinity, and wind/rain must enter separate branches. Do not collapse them into a single cyclone severity score.
5. **Gate recommendations by feasibility.** A pump-dependent action is invalid for a farmer without pump or rental access. Early harvest is invalid if grain is not mature or labor/transport is unavailable.
6. **Deliver one action per message.** State action, reason, deadline, safety constraint, and a callback/IVR confirmation. Low literacy favors short voice prompts over agronomic paragraphs.
7. **Create an event record automatically.** Save alert, advisory, farmer response, stage uncertainty, action taken, images/measurements and post-event outcome.
8. **Learn only from adjudicated outcomes.** Local loss functions should be updated from verified event records, not from self-reported damage alone.

This implements an observation -> mechanism -> implication -> recommendation chain. For example, a Puri farmer with a 150-175 day paddy crop planted in May may plausibly be in flowering, grain formation, or harvest during an October-November warning [21]. The uncertainty itself triggers an IVR stage check; the answer then determines whether the system discusses harvest readiness, lodging, drainage, or post-submergence recovery.

## 6. REAL-vs-FILLER

| Evidence or feature | Classification | Why |
|---|---|---|
| Live IMD cyclone and agromet products | **REAL NOW** | They provide the authoritative event trigger [22][23]. Production integration still needs feed testing. |
| 2025 Odisha contingency plan actions | **REAL NOW after manual curation** | It explicitly contains flood and cyclone pre/post sections and district sowing-window tables [12]. Encoding must be cleaned and agronomists must approve templates. |
| 2025-26 Economic Survey crop/input data | **REAL NOW for prioritization** | It supports crop mix, paddy district ranking and state capability context [18]. It does not personalize an advisory. |
| IMD 2002 crop calendar | **REAL as a prior, filler as exact stage truth** | It provides regional windows and broad stages [21]. Treating it as the farmer's present stage would be decorative precision. |
| NRRI released-variety table | **REAL for eligibility** | It names Odisha-targeted ecology, duration, yield and stress traits [9]. It does not prove local dealer stock or current adoption. |
| Swarna-Sub1 field experiment | **REAL behavioral evidence** | Adoption rose 3.5 points from a 6.3% control mean, and dealer stocking responded [20]. It is not a current statewide rate. |
| Myanmar flood curves | **REAL research prior, not operational truth** | The curves have quantified stage/depth/duration relationships and validation error [16]. Odisha use is gated by local validation. |
| USDA salinity response | **REAL mechanism evidence** | It supports separate salinity classification and EC testing [17]. It is not a cyclone saltwater duration curve. |
| Japanese lodging thresholds | **REAL mechanism evidence, weak local threshold** | Wind and rain effects were measured [19], but transfer across cultivar, canopy, rain, soil and era is unsafe. |
| State machinery/KCC totals | **REAL program context, filler for individual feasibility** | Distribution and issuance totals are documented [18]. They do not show which farmer can act now. |
| "AI will predict exact losses" without a local training set | **FILLER** | No Odisha hazard x stage x crop loss matrix or adjudicated counterfactual dataset was located. |
| Generic satellite map screenshot | **FILLER unless linked to parcel/event data** | A map is not an advisory input until resolution, timestamp, rights, uncertainty and farmer linkage are known. |
| Generic SMS saying "take precautions" | **FILLER** | It lacks crop, stage, action, deadline and feasibility. The problem requires actionable, time-sensitive advice. |
| Farmer-confirmed sow date, variety, stage, resources and observed water depth | **REAL and high value** | These few fields resolve the largest public-data gaps and should be collected even in the first prototype. |

The decisive principle is simple: **a dataset is real only if it changes a decision**. State averages are valuable for prioritizing deployment but become filler when used to pretend knowledge of a particular farm.

## 7. NOISE LOG

| Search or candidate | Disposition | Reason |
|---|---|---|
| Official Odisha Agriculture Statistics landing page | Retained as a named source, not used for unseen values | It lists a 2023-24 edition, but the direct file was not recoverable through text or raw-HTML extraction in this run [25]. |
| Scribd copy of *Odisha Agriculture Statistics 2023-24* | Discarded for district values | Extraction exposed contents headings, not the required district tables. A secondary host should not replace the official file. |
| 2006-07 Odisha agriculture statistics PDF | Discarded for current mapping | Official but too stale for a current district crop map. |
| Generic IMD home pages | Discarded | They confirmed IMD's existence but did not expose Odisha crop-stage data. The specific crop-calendar and live advisory/cyclone pages were retained instead. |
| ResearchGate figures and generic rice-growth websites | Discarded | They lacked authoritative Odisha calibration or supplied only generic stage descriptions. |
| Wikipedia lodging entry and social-media posts | Discarded | Non-primary and unnecessary once a quantitative experiment was located. |
| IndiaStat district pages | Discarded as core evidence | Search results suggested current district tables, but access is commercial/secondary and not a free prototype dependency. |
| Odisha horticulture portal search hits | Not used for district claims | No current downloadable district table for vegetables, coconut, cashew and spices was recovered. |
| Cyclone Fani damage-and-loss assessment | Retained only as event context, not a fragility function | Event-level sector loss does not supply crop-stage x intensity x duration response curves. |
| Myanmar flood-damage functions | Retained with a transfer warning | Strongest quantitative stage/depth/duration source found, but local assumptions and validation are required [16]. |
| Bangladesh salinity/adoption search results | Discarded for Odisha parameters | Relevant mechanisms, wrong deployment geography. The controlled USDA study was retained only as a provisional salinity prior. |
| Field-day attendance for Swarna-Sub1 | Discarded as adoption-rate evidence | Attendance demonstrates outreach, not adoption, planted area, repeated use, or current seed availability. |
| NAFIS/NSS all-India headline statistics | Discarded for Odisha personalization | National averages must not be presented as Odisha or household values; only the verified Odisha indebtedness estimate was retained [1]. |

## 8. VERDICT

### Overall grade: PARTIAL

| Capability | Grade | Can it be built free today? | Condition |
|---|---|---|---|
| Official alert ingestion and district/village routing | **GO** | Yes, as a prototype | Validate IMD page/API stability, alert identifiers, update handling and production rights. |
| Paddy-first crop/season prioritization | **GO** | Yes | Use current Economic Survey data and farmer confirmation. |
| Broad stage-aware advisory selection | **PARTIAL** | Yes | Use IMD calendars as priors; collect sowing/transplanting date, variety and IVR stage confirmation. |
| Pre-disaster action and post-disaster recovery messages | **GO** | Yes | Curate the 2025 contingency plan into agronomist-approved, hazard-specific rules with safety constraints. |
| Tolerant-variety recommendations | **PARTIAL** | Yes | Check ecology, current seed stock, price, certified lot and local extension approval. |
| Parcel-specific feasibility | **GATED** | No, not from public data alone | Collect machinery, pump, drainage, labor, storage, transport and credit access. |
| Quantified cost-of-waiting | **GATED** | No | Requires Odisha-calibrated hazard x stage x crop x variety damage functions and uncertainty bounds. |
| Automatic claim packet | **PARTIAL** | Basic packet yes; claim acceptance no | Partner on required evidence fields, policy/relief identifiers, assessor workflow and data-sharing rules. |
| Automatic claim valuation or loss attribution | **GATED** | No | Needs insurer/government methodology, CCE/remote-sensing access, calibrated models and human adjudication. |
| Next-season resilience planning | **PARTIAL** | Yes | Variety catalogue and event history are usable; current district seed availability, price and adoption need partners. |
| SMS/IVR delivery for low-literacy farmers | **GO** | Yes technically | Collect language/channel consent, test comprehension, limit each message to a specific action and deadline. |

### What the prototype should build now

1. A farm enrollment record with village/plot, crop, variety, planting/transplanting date, irrigation/drainage, machinery/labor access, KCC/insurance status, language and phone consent.
2. An IMD alert adapter that preserves warning provenance and update history.
3. A conservative stage estimator with explicit uncertainty and one-question IVR confirmation.
4. A manually curated rule library from the 2025 Odisha contingency plan, separated into pre-event, immediate post-event, recovery, claim evidence and next-season advice.
5. A tolerant-variety catalogue using only released, Odisha-relevant entries.
6. An event packet containing alert, advisory, farmer confirmation, action taken, geotagged observations, water depth/duration/type and post-event outcome.
7. An analytics screen that labels imported Myanmar, salinity and lodging relationships as **unvalidated research priors**, never as claim or payout formulas.

### What needs collection

Collect sowing/transplanting dates, observed stage, variety, field elevation, drainage outlet, irrigation source, machinery/rental/labor access, storage, current inputs, water depth and duration, fresh versus saline water, crop lodging/breakage, action taken, post-event yield, recovery cost, language and delivery response. These are the minimum fields that turn statewide statistics into a farm advisory.

### What needs a partner

- **Odisha Department of Agriculture and Farmers' Empowerment, OUAT and ICAR-NRRI** for rule validation, phenology, variety suitability, local trials and seed-chain data.
- **IMD and NDMA/OSDMA** for stable alert feeds, identifiers and operating procedures.
- **ORSAC and district administrations** for parcel/flood layers, remote-sensing products and event validation.
- **Odisha State Seeds Corporation, dealers and producer organizations** for real-time tolerant-seed stock and distribution.
- **PMFBY insurers, banks/SLBC and relief authorities** for claim schemas, KCC/insurance linkage, assessment rules and consented data exchange.
- **Farmers and local extension workers** for the ground-truth layer that no public report can replace.

**Final decision:** build the prototype. Use free official data for warning ingestion, paddy-first targeting, calendar priors, tolerant-variety eligibility and conservative action messages. Do not promise exact loss percentages, exact stage from month alone, or automatic claim valuation. Those three features remain gated until Odisha-specific field data and institutional partnerships exist.

## References

1. *NABARD All India Rural Financial Inclusion Survey (NAFIS 2*. https://www.nabard.org/auth/writereaddata/tender/2102255939NAFIS%202021-22%20Report%20Final.pdf
2. *Swarna Sub 1*. https://rkb-odisha.in/wp-content/uploads/2024/09/Production-Practices-of-Swarna-Sub-1-Rice-Variety-in-English.pdf
3. *Sub1 Rice: Engineering Rice for Climate Change - PMC - NIH*. https://pmc.ncbi.nlm.nih.gov/articles/PMC6886445
4. *Swarna-Sub1: Odisha's food for a goddess - Rice Today*. https://ricetoday.irri.org/swarna-sub1-odishas-food-for-a-goddess
5. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
6. *Crop Calendar - Rice Based Cropping Systems - RKB) Odisha*. https://rkb-odisha.in/rice-in-odisha/step-by-step-production/pre-planting/crop-calendar/
7. *ORSAC Geospatial Portal - for Rural & Urban Development*. https://odisha4kgeo.in/
8. *Welcome to ICAR-CRIDA | भाकृअनुप – केंद्रीय बारानी कृषि अनुसंधान संस्थान*. https://icar-crida.res.in/Crop_Contingency_Plan.html
9. *Released Varieties – Central Rice Research Institute*. https://icar-crri.in/released-varieties
10. *Odisha Agriculture Statistics 2023-24 | PDF | Workforce | Food Industry*. https://www.scribd.com/document/911305013/Agriculture-Statistics-Odisha
11. *Publication Reports*. https://mospi.gov.in/sites/default/files/publication_reports/Report_587m_0.pdf
12. *Crop Contigency Plan 2025*. https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
13. [
            Physiological basis of tolerance to complete submergence in rice involves genetic factors in addition to the SUB1 gene - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC4243076)
14. *mowr.nic.in*. https://mowr.nic.in/core/WebsiteUpload/2023/MI6.pdf
15. *Over 500 farmers in Odisha attend field day on flood-tolerant Swarna-Sub1 – Rice Today*. https://ricetoday.irri.org/over-500-farmers-in-odisha-attend-field-day-on-flood-tolerant-swarna-sub1/
16. *Development of flood damage functions for agricultural crops and their applicability in regions of Asia - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2214581821001014
17. *Pdf Pubs*. https://www.ars.usda.gov/arsuserfiles/20361500/pdf_pubs/P1837.pdf
18. *finance.odisha.gov.in*. https://finance.odisha.gov.in/sites/default/files/2025-08/OES%202025-26%20Main%20Booklet.pdf
19. *jircas.go.jp*. https://www.jircas.go.jp/sites/default/files/publication/jarq/04-3-001-006_0.pdf
20. *Private Input Suppliers as Information Agents for Technology Adoption in Agriculture*. http://povertyactionlab.org/sites/default/files/research-paper/working-paper_5092_Private-Input-Suppliers-As-Information-Agents_India_May2021.pdf
21. *Cwc Odhisha*. https://www.imdpune.gov.in/library/crop/CWC_Odhisha.pdf
22. *AGROMET ADVISORY SERVICES - imd imd https://mausam.imd.gov.in › agr...*. https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php
23. *Cyclone Information | India Meteorological Department - मौसम*. https://mausam.imd.gov.in/responsive/cycloneinformation.php
24. *Pulses in Odisha - Rice Based Cropping Systems*. https://rkb-odisha.in/pulses-in-odisha
25. *Statistics - Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/en/page/statistics
