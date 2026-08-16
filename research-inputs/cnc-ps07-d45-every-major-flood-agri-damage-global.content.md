# Global Agricultural Flood Ledger for Odisha Advisory Validation

## 1. EXECUTIVE SUMMARY.

- **Completeness Boundary**: No source system defines "every major agricultural flood." EM-DAT is thresholded and country-level, DFO maps changing surface water, IBTrACS records cyclone tracks, and NOAA is US-centered. Therefore, the defensible product is a versioned, reproducible ledger with explicit missingness, not a claim that every farm inundation worldwide has been found [20][21][3]. -> Treat this report as a verified seed ledger and gap register, not the final global census.
- **Largest Verified Crop Footprints**: China in 1998 had about **22M ha affected and 4.8M ha destroyed**; Pakistan in 2010 lost **2.4M ha of unharvested crops and US$5.1B**; Pakistan in 2022 had **1,784,126 ha adversely affected**, with **US$3.725B damage and US$9.244B losses** [30][31][32]. -> Use these as upper-tail validation cases for Odisha's crop, irrigation, livestock, and logistics models.
- **Losses Extend Beyond Standing Crops**: Pakistan 2022 recorded crop, livestock, and fisheries damage; Sudan 2020 combined rainfed and irrigated crop loss with **108,044 livestock deaths**; NSW 2022 reported **AUD432.4M** of agricultural damage across crops, infrastructure, and livestock [32][2][4]. -> The engine must model stored seed, fodder, animals, ponds, machinery, roads, and irrigation, not only crop hectares.
- **Recovery Has Several Clocks**: Pakistan 2010 required support across **three or four cropping seasons over two years**; Thailand planned most reconstruction over **6-24 months**; Pakistan 2022 used short-term, intermediate, and long-term windows extending to **five years** [31][1][32]. -> Generate separate alerts for immediate life safety, next-planting decisions, and multi-season asset recovery.
- **Farmer-Behavior Evidence Is Weak**: Most assessments document agency distributions and proposed recovery programs rather than what farmers independently did. -> Store `farmer_action_observed`, `agency_action_delivered`, and `action_recommended` as separate fields; do not turn a recommendation into a historical fact.
- **Headline Statistics Are Often Misleading**: "One-third of Pakistan" describes broad inundation, while the PDNA's directly agricultural denominator is **1,784,126 ha adversely affected**. Brazil's estimated total flood loss and China's total natural-disaster loss are not agricultural losses. -> Reject sector-mismatched figures from model training.
- **Communications Must Match Odisha Conditions**: India's mKisan describes SMS as an effective channel reaching nearly nine crore farm families, while BAMIS demonstrates an agrometeorological model combining weather and agricultural data at subdistrict level [53][54]. -> Deliver short Odia SMS and IVR actions keyed to crop stage, field elevation, livestock, pond, and drainage status.
- **Decision**: The evidence is sufficient to build a high-quality validation corpus and rule library, but insufficient to label this a complete worldwide ledger. -> Publish it as version 0.1 with archive IDs, source snapshots, uncertainty grades, and a formal backfill queue.

## 2. THE COMPLETE EVENT LEDGER.

### Scope and grading

This heading follows the required structure, but the table is a **bounded candidate ledger**, not a scientifically complete global enumeration. A mathematically complete ledger would require full licensed EM-DAT extraction, all DFO records and revisions, event-level joins to agricultural statistics, national-language archival work, and field-level loss records that often do not exist.

Grades mean: **A** = primary governmental, UN, FAO, or PDNA evidence with quantified agriculture plus action or recovery detail; **B** = authoritative quantified agricultural evidence but important fields missing; **C** = credible event record with partial agricultural evidence; **D** = occurrence known or specified in the brief, but no accessible event-specific agricultural record sufficient for this ledger. "Agency action" is not represented as farmer behavior.

### South Asia, by year

| Date | Event | Country/region | Type | Agricultural damage: area, crops, value | What farmers did | Recovery duration | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|---|
| 1988; exact dates MISSING-DATA | National monsoon flood | Bangladesh | Flood | Area, crops, livestock, and value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific accessible source: MISSING-DATA | D |
| Mid-July onward, 1998 | National monsoon flood | Bangladesh | Flood | FAO reported **760,000 ha of farmland affected** and nearly **425,000 ha of rice and other crops destroyed**. Aus-rice output was revised from 1.9M to 1.6M tonnes; Aman nurseries and transplanting were disrupted [30]. A secondary compilation instead reports 800,000 ha affected and 575,000 ha destroyed, so the FAO figure is preferred [43] | Farmer behavior: MISSING-DATA | MISSING-DATA | https://openknowledge.fao.org/bitstreams/1675ed91-da8d-475c-9740-2228a5c55eb3/download; 27 Aug 1998 | A |
| 2004; exact dates MISSING-DATA | National monsoon flood | Bangladesh | Flood | MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific accessible source: MISSING-DATA | D |
| 2007; exact dates MISSING-DATA | Monsoon and Cyclone Sidr flood sequence | Bangladesh | Compound | MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific accessible source: MISSING-DATA | D |
| Late July 2010 onward | Pakistan super flood | Pakistan | Flood | **2.4M ha of unharvested crops** and **US$5.1B agricultural damage**; cotton, rice, maize, vegetables, sugar cane, and winter wheat were affected [31] | Farmer behavior independently observed: MISSING-DATA. Agency support reached 1.4M farm families; seed, vegetable kits, fodder, veterinary care, shelters, and more than 1,000 irrigation cash-for-work schemes were delivered [31] | Three or four cropping seasons over the following two years [31] | https://www.fao.org/4/ba0062e/ba0062e00.pdf; FAO 2011 | A |
| 2011; report point 21 Sep | Sindh monsoon flood | Pakistan | Flood | At least **880,000 ha of standing crops** were reported damaged in the contemporaneous FAO estimate; rice, maize, cotton, sugar cane, orchards, and vegetables were named. Stored seed, grain, and productive assets were also lost [44] | Farmer behavior: MISSING-DATA; continuing rain and damaged infrastructure impeded aid [47] | Standing water expected for an extended period; exact recovery duration MISSING-DATA [47] | https://www.fao.org/fileadmin/user_upload/emergencies/docs/Pakistan_Rapid_Response_Plan_2011.pdf; Sep 2011 | B |
| 16-17 Jun 2013 | Uttarakhand floods and landslides | India, Uttarakhand | Compound | **20,000 ha of agricultural land severely damaged** and **18,228 cattle killed** [14] | MISSING-DATA | MISSING-DATA | https://www.actionaidindia.org/emergency/uttarakhand-floods-2013/; source date MISSING-DATA | B |
| Sep 2014; exact dates MISSING-DATA | Jammu and Kashmir flood | India, Jammu and Kashmir | Flood | Hectares, crops, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | https://academicjournals.org/app/webroot/article/0a56e5e67009.pdf; publication date MISSING-DATA | D |
| 2014; exact dates MISSING-DATA | Punjab and Kashmir monsoon flood | Pakistan | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Nov-Dec 2015; exact dates MISSING-DATA | Chennai and Tamil Nadu flood | India, Tamil Nadu | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| May 2016; exact dates MISSING-DATA | Central Sri Lanka floods and landslides | Sri Lanka | Compound | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | FAO Crop Prospects search returned no event-level record; MISSING-DATA | D |
| May 2017; exact dates MISSING-DATA | Southwest monsoon flood | Sri Lanka | Compound | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific accessible agricultural assessment: MISSING-DATA | D |
| Aug 2017; exact dates MISSING-DATA | Bihar monsoon flood | India, Bihar | Flood | Hectares, crops, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Official event-specific crop memorandum: MISSING-DATA | D |
| 11-14 Aug 2017 | Terai flood | Nepal | Flood | Household food grains were damaged, but agricultural hectares, crop value, and livestock totals are MISSING-DATA [26] | MISSING-DATA | The national recovery assessment addressed medium-term needs, but event-specific farm duration is MISSING-DATA [26] | https://recovery.preventionweb.net/publication/nepal-flood-2017-post-flood-recovery-needs-assessment; 2017 | C |
| 2017; exact dates MISSING-DATA | Northern and central monsoon floods | Bangladesh | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific accessible agricultural assessment: MISSING-DATA | D |
| Aug 2018; exact dates MISSING-DATA | Kerala flood | India, Kerala | Compound flood and landslide | Hectares, crops, livestock, value: MISSING-DATA in the extracted evidence | MISSING-DATA | MISSING-DATA | Event is independently recognized among India's major recent floods [55]; PDNA agricultural table not recovered | D |
| Aug 2019; exact dates MISSING-DATA | Kerala flood and landslides | India, Kerala | Compound | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | https://sdma.kerala.gov.in/floods-2019/; page date MISSING-DATA [33] | C |
| Oct 2021; exact dates MISSING-DATA | Kerala flood and landslides | India, Kerala | Compound | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific accessible agricultural assessment: MISSING-DATA | D |
| Jul-Sep 2022 | Pakistan monsoon flood | Pakistan | Compound monsoon, river and flash flood | **1,784,126 ha adversely impacted**; more than **800,000 animals lost**; agriculture damage **PKR800B/US$3.725B** and losses **PKR1.986T/US$9.244B**. Cotton was most affected, followed by rice, sugar cane, and fruit trees [32] | Farmer behavior observed: MISSING-DATA. Documented recovery actions included debris clearance, canal and drainage restoration, seeds and inputs, short-cycle planting, feed, veterinary care, and restocking [32] | Up to 12 months, up to 3 years, and up to 5 years; Sindh waterlogging could last months or years [32] | https://documents1.worldbank.org/curated/en/099910001032330716/pdf/P17999109c267907f0aaa70f55da13e2371.pdf; Dec 2022 | A |
| 30 Jul 2024 | Wayanad debris flow and flash-flood disaster | India, Kerala | Compound landslide and flood | Plantation hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Occurrence record identifies the affected villages and date [56]; agricultural assessment MISSING-DATA | D |
| 2024; event dates MISSING-DATA | Nepal monsoon flood | Nepal | Compound flood and landslide | FAO conducted a DIEM impact assessment from 17-24 Nov 2024, but the extracted record did not expose a national hectare or value total [8] | MISSING-DATA | Assessment-stage only; MISSING-DATA | https://openknowledge.fao.org/handle/20.500.14283/CD5014EN; 2024 | C |
| 2024; exact dates MISSING-DATA | Eastern Bangladesh flood | Bangladesh | Flood | Event-specific national total MISSING-DATA. A separate Chattogram report described **15,911 ha** of damaged cropland, but it cannot be substituted for the national total | MISSING-DATA | MISSING-DATA | National event-specific agricultural assessment: MISSING-DATA | D |
| Annual monsoon cycle; full year series MISSING-DATA | Assam recurrent floods | India, Assam | Flood | ASDMA exposes daily-report archives, but a complete year-by-year agricultural series was not retrievable from the accessible pages [34][36] | MISSING-DATA | MISSING-DATA | https://asdma.assam.gov.in/information-services/assam-flood-report-0; archive date MISSING-DATA | D |

**South Asia takeaway:** Pakistan is the strongest multi-season evidence base. India, Bangladesh, Nepal, and Sri Lanka contain major gaps precisely where the Odisha engine needs crop-stage, farmer-action, and recovery labels. Those gaps should remain null, not be filled with regional averages.

### East and Southeast Asia, by year

| Date | Event | Country/region | Type | Agricultural damage: area, crops, value | What farmers did | Recovery duration | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|---|
| Mid-Jun onward, 1998 | Yangtze, Nen, Songhua and associated floods | China | Flood | About **22M ha of crops affected** and **4.8M ha destroyed**; early and late rice were affected [30] | Farmer behavior MISSING-DATA; official sources expected greater autumn-crop area to compensate [30] | A separate recovery report anticipated no harvest in a severely affected area until Aug 1999 [16] | https://openknowledge.fao.org/bitstreams/1675ed91-da8d-475c-9740-2228a5c55eb3/download; 27 Aug 1998 | A |
| 2000; exact dates MISSING-DATA | Mekong Delta flood | Vietnam | Flood | Hectares, crops, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Lower Mekong event record: MISSING-DATA | D |
| 2000; exact dates MISSING-DATA | Mekong flood | Cambodia | Flood | Hectares, crops, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Lower Mekong event record: MISSING-DATA | D |
| 2007; exact dates MISSING-DATA | Jakarta flood | Indonesia, Jakarta | Urban and river flood | Agricultural impact record MISSING-DATA; do not infer farm loss from urban loss | MISSING-DATA | MISSING-DATA | Event-specific agricultural source: MISSING-DATA | D |
| Jul-Dec 2011; some water to mid-Jan 2012 | Thailand national flood | Thailand | Compound monsoon and tropical-depression flood | More than **6M ha affected**; **18,000 sq km of farmland** remained underwater in Nov. Agriculture, livestock, and fisheries had **THB5.666B damage plus THB34.715B losses**, or **THB40.381B total** [1] | Farmer behavior MISSING-DATA; government centralized monitoring, relief, and recovery planning [1] | Agricultural recovery need **THB4.570B**, mainly within 6 months and 6-24 months; most reconstruction expected in 6-24 months [1] | https://documents1.worldbank.org/curated/en/677841468335414861/pdf/698220WP0v10P106011020120Box370022B.pdf; 2012 | A |
| 2011; exact dates MISSING-DATA | Lower Mekong flood | Cambodia and Vietnam | Compound regional flood | Country-specific agricultural areas and values MISSING-DATA in the recovered Mekong report [28] | Local action MISSING-DATA; report recommended decentralized management, better forecasts, data, and awareness [28] | Some regional flooding lasted to mid-Jan 2012; farm recovery MISSING-DATA [28] | https://reliefweb.int/report/cambodia/annual-mekong-flood-report-2011; 2012 | C |
| 2013; exact dates MISSING-DATA | Jakarta flood | Indonesia, Jakarta | Flood | Agricultural impact record MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural source: MISSING-DATA | D |
| 2013; exact dates MISSING-DATA | Lower Mekong flood | Cambodia and Vietnam | Compound flood and tropical storms | Hectares, crops, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | https://reliefweb.int/report/cambodia/annual-mekong-flood-report-2013; publication date MISSING-DATA | C |
| Jul-Oct 2015; exact dates MISSING-DATA | National flood and landslides | Myanmar | Compound | Hectares, crops, livestock, value: MISSING-DATA in recovered evidence | MISSING-DATA | MISSING-DATA | Myanmar PDNA record not recovered; MISSING-DATA | D |
| 2016; exact dates MISSING-DATA | Yangtze basin and southern China floods | China | Flood | Hectares, crops, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific official agricultural table: MISSING-DATA | D |
| 2020; exact dates MISSING-DATA | Yangtze basin flood | China | Flood | A searched secondary analysis reported a large cropland footprint, but no primary event table was recovered; publishable value MISSING-DATA | MISSING-DATA | MISSING-DATA | Primary national agricultural assessment: MISSING-DATA | D |
| 2020; exact dates MISSING-DATA | Jakarta flood | Indonesia, Jakarta | Flood | Agricultural impact record MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural source: MISSING-DATA | D |
| 2020; exact dates MISSING-DATA | Central Vietnam flood sequence | Vietnam | Compound tropical cyclone and flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific national agricultural table: MISSING-DATA | D |
| 11 May 2024 | West Sumatra flash flood and lahars | Indonesia, West Sumatra | Compound flood, lahar and landslide | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | https://sentinel-asia.org/EO/2024/article20240511ID.html; 11 May 2024; agriculture fields absent [41] | D |
| 2024; exact dates MISSING-DATA | Southern and central China flood sequence | China | Compound flood and typhoon rainfall | Event-specific crop hectares and agricultural value MISSING-DATA; a total natural-disaster loss figure is excluded as non-sectoral | MISSING-DATA | MISSING-DATA | Official crop-loss table: MISSING-DATA | D |

**East/Southeast Asia takeaway:** China 1998 and Thailand 2011 are strong agricultural benchmark events. The Mekong reports are valuable for hydrology and governance, but they cannot supply country-specific farm-loss labels without national agricultural assessments.

### Africa, by year

| Date | Event | Country/region | Type | Agricultural damage: area, crops, value | What farmers did | Recovery duration | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|---|
| 2012; exact dates MISSING-DATA | National flood | Nigeria | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| 2013; exact dates MISSING-DATA | Nile and flash floods | Sudan | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Since Jul 2020; emergency declared 4 Sep | Sudan national flood | Sudan | Flood | **2,216,362 ha rainfed cropland** and **103,320 ha irrigated land** damaged; estimated crop-production losses were **1,044,942 tonnes rainfed** and **557,928 tonnes irrigated**. Sorghum and sesame dominated traditional-sector losses; **108,044 animals** died [2] | Farmer behavior MISSING-DATA. Priority actions included seed and tool replacement, irrigation and water-point rehabilitation, restocking, feed, veterinary care, fishing gear, cash transfers, and cash-for-work [2] | Exact completion duration MISSING-DATA | https://www.fao.org/fileadmin/user_upload/emergencies/docs/The%20Sudan%20Flood%20Impact%20Assessment.pdf; Sep 2020 | A |
| 2020; exact dates MISSING-DATA | Sahel-wide flood season | West and Central Africa | Flood | Country-level agricultural series MISSING-DATA | MISSING-DATA | MISSING-DATA | Regional event-specific agriculture table: MISSING-DATA | D |
| Apr 2022; exact dates MISSING-DATA | KwaZulu-Natal flood | South Africa | Compound flood and landslide | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Sep-Oct 2022 | National flood | Nigeria | Flood | More than **569,000 ha of farmland destroyed or damaged** before the October harvest [17] | MISSING-DATA | MISSING-DATA | https://www.unocha.org/publications/report/nigeria/nigeria-situation-report-1-november-2022; 1 Nov 2022 | B |
| 2022; exact dates MISSING-DATA | Nile and flash floods | Sudan | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| 2023; exact dates MISSING-DATA | Deyr floods after prolonged drought | Somalia | Compound drought-to-flood shock | Cropland, crops, livestock, value: MISSING-DATA in accessible assessment | MISSING-DATA | MISSING-DATA | FAO/OCHA event-specific agricultural table: MISSING-DATA | D |
| 2023-24; exact dates MISSING-DATA | Flood and cyclone sequence | Mozambique and Malawi | Compound cyclone and flood | Hectares, crops, livestock, value: MISSING-DATA in recovered evidence | MISSING-DATA | MISSING-DATA | Event-specific national agricultural assessment: MISSING-DATA | D |
| 2023-24; exact dates MISSING-DATA | Seasonal flood sequence | Zambia | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Mar-May 2024 | El Nino and Indian Ocean Dipole flood sequence | Kenya, Tanzania, Burundi, Somalia, Ethiopia and wider East Africa | Compound regional flood and landslide | Crop destruction and livelihood disruption were documented, but a harmonized regional hectare/value total was not available in the recovered evidence [24] | Household/farmer action MISSING-DATA; regional sources emphasize early warning, evacuation, livelihood aid, and agricultural support | Recovery status ongoing at report date; duration MISSING-DATA | https://www.unocha.org/publications/report/somalia/eastern-africa-el-nino-floods-impact-snapshot-may-2024; May 2024 | C |
| 2024; exact dates MISSING-DATA | Sahel flood season | Sahel | Flood | Harmonized cropland hectares, crops, livestock, and value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Regional event-specific agriculture table: MISSING-DATA | D |

**Africa takeaway:** Sudan 2020 demonstrates why a crop-only engine is inadequate: rainfed fields, irrigation, pastoral livestock, fishing gear, water points, and road access failed together. Most other African cases need national-language and ministry-level backfilling.

### Europe, by year

| Date | Event | Country/region | Type | Agricultural damage: area, crops, value | What farmers did | Recovery duration | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|---|
| Summer 1997 | Oder flood | Poland, Czechia and Germany | Flood | In the studied German catchment, **50 sq km**, or **5,000 ha**, of cultivated land flooded and field vegetation was completely killed [15] | MISSING-DATA | MISSING-DATA | https://www.international-agrophysics.org/pdf-107035-37844; publication date MISSING-DATA | B |
| Aug 2002; exact dates MISSING-DATA | Central European/Elbe-Danube flood | Central Europe | Flood | Hectares, crops, livestock, agricultural value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Jun-Jul 2007; exact dates MISSING-DATA | Summer floods | United Kingdom | Flood | Farm-level research confirms severe agricultural and horticultural losses, but publishable hectares and value were not recovered [57] | MISSING-DATA | MISSING-DATA | https://onlinelibrary.wiley.com/doi/10.1111/j.1753-318X.2009.01031.x; 2009 | C |
| May-Jun 2013; exact dates MISSING-DATA | Central European flood | Germany, Austria, Czechia and neighbors | Flood | Hectares, crops, livestock, agricultural value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Mid-Dec 2013 to Mar 2014 | Winter floods | England, especially Somerset Levels and Thames Valley | Flood and prolonged waterlogging | The official assessment documents extensive farm flooding; inundation longer than **30 days** was significant in the Thames Valley and Somerset Levels [27] | Farmer behavior MISSING-DATA | Waterlogging exceeded 30 days in major areas; full productive recovery duration MISSING-DATA | https://assets.publishing.service.gov.uk/media/5a74a46d40f0b61df47774b1/RFI7086_Flood_Impacts_Report__2_.pdf; 4 Jun 2014 [27] | B |
| May-Jun 2016; exact dates MISSING-DATA | Seine-Loire flood | France | Flood | Hectares, crops, livestock, agricultural value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| 14-15 Jul 2021 | Ahr/Meuse flood | Germany and Belgium | Flash and river flood | Farm hectares, crops, livestock, agricultural value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| 1-3 and 16-17 May 2023 | Emilia-Romagna floods | Italy | Compound flood and landslide | Severe agricultural damage is documented, but event-specific hectares, crops, and agricultural value were not available in the recovered evidence [6] | MISSING-DATA | MISSING-DATA | https://www.mdpi.com/2073-445X/13/11/1800; 2024 | C |

**Europe takeaway:** European sources often provide excellent hydrology and total economic loss but weak agriculture-sector disaggregation. The England report is valuable for duration-dependent waterlogging, while the Oder study supplies direct field mortality evidence.

### Americas, by year

| Date | Event | Country/region | Type | Agricultural damage: area, crops, value | What farmers did | Recovery duration | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|---|
| Apr-Oct 1993; exact dates MISSING-DATA | Great Mississippi and Missouri flood | United States | Flood | Agricultural hectares/acres, crop value, livestock: MISSING-DATA in recovered authoritative evidence | MISSING-DATA | MISSING-DATA | NOAA/USDA event-level agricultural assessment: MISSING-DATA | D |
| 2010-11; exact dates MISSING-DATA | La Nina flood disaster | Colombia | Compound flood and landslide | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Apr-May 2011 | Mississippi River flood and induced levee breaches | United States | Flood | A study reported **53,824 ha/133,000 acres of Missouri farmland flooded**, loss of 2011 crops, and damage to future soil productivity [42]. A narrower estimate identified 8,094-12,146 ha of poorly drained soils not replanted in 2011 [52] | MISSING-DATA | Some land was not replanted in 2011; longer soil recovery MISSING-DATA [52] | https://www.tandfonline.com/doi/pdf/10.2489/jswc.67.1.5A; 2012 | B |
| Jun 2013; exact dates MISSING-DATA | Alberta flood | Canada | Flood | Farm-specific hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| 2015-16; exact dates MISSING-DATA | Litoral and Parana basin floods | Argentina | Flood | Hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Event-specific agricultural assessment: MISSING-DATA | D |
| Jan-Mar 2017 | Coastal El Nino | Peru | Compound flood and landslide | More than **60,000 ha of crops** were affected; about **445,000 people** were affected in the worst-hit northern coastal areas [12] | FAO supported recovery for approximately 7,000 farmers; independent farmer behavior MISSING-DATA | MISSING-DATA | https://news.un.org/en/story/2017/05/557772; May 2017 | B |
| Mar-Aug 2019; exact dates MISSING-DATA | Mississippi, Missouri and Midwest floods | United States | Flood and prolonged waterlogging | Prevented-planting, crop, livestock, and value fields: MISSING-DATA in recovered authoritative event record | MISSING-DATA | MISSING-DATA | USDA/NOAA event-level agricultural table: MISSING-DATA | D |
| Nov 2021 | Atmospheric river and Sumas Prairie flood | Canada, British Columbia | Compound rainfall, river flood and infrastructure failure | More than **640,000 animals** were reported dead, including **628,000 poultry, 12,000 hogs, and 420 dairy cows** [49] | Farmers evacuated animals where possible; a systematic behavior count is MISSING-DATA | MISSING-DATA | https://www.ctvnews.ca/vancouver/article/livestock-death-toll-from-bc-flooding-628000-poultry-12000-hogs-420-cows/; Nov 2021 | B |
| Jan-Mar 2023; exact dates MISSING-DATA | California atmospheric-river floods | United States, California | Compound flood and levee failure | Statewide agricultural hectares, crops, livestock, value: MISSING-DATA; total disaster loss is excluded from the farm column | MISSING-DATA | MISSING-DATA | NOAA event record found, but agriculture table MISSING-DATA | D |
| Apr-May 2024 | Rio Grande do Sul flood | Brazil | Compound rainfall, river and urban flood | The state is a major agricultural producer, but exact event-wide agricultural hectares and value were not exposed in the recovered report. Up to **800 mm** rain and unprecedented flooding were documented [9] | Farmer behavior MISSING-DATA | Recovery outlook MISSING-DATA | https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Unprecedented%20floods%20in%20Rio%20Grande%20do%20Sul%20threaten%20Brazil%27s%20agricultural%20output_Brasilia_Brazil_BR2024-0009; May 2024 | C |

**Americas takeaway:** The US 2011 levee-breach study is useful for soil-productivity and replanting labels, while British Columbia 2021 is a critical concentrated-livestock case. The absence of a recovered Brazil agriculture total prevents the widely quoted all-sector loss from being mislabeled as farm damage.

### Australia and Oceania, by year

| Date | Event | Country/region | Type | Agricultural damage: area, crops, value | What farmers did | Recovery duration | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|---|
| Dec 2010-Jan 2011 | Queensland floods | Australia, Queensland | Compound tropical rainfall and river flood | Agricultural hectares, crops, livestock, value: MISSING-DATA in recovered evidence | MISSING-DATA | MISSING-DATA | Official event-specific agricultural assessment: MISSING-DATA | D |
| Mar 2021; exact dates MISSING-DATA | NSW floods | Australia, New South Wales | Flood | Agricultural hectares, crops, livestock, value: MISSING-DATA | MISSING-DATA | MISSING-DATA | Official event-specific agricultural assessment: MISSING-DATA | D |
| Feb-Mar 2022 | Southeast Queensland rainfall and flood | Australia, Queensland | Compound rainfall and river flood | More than **2,250 primary producers across 17 local-government areas** were affected; the recovered official snippet did not expose a defensible sector-loss total [50] | MISSING-DATA | MISSING-DATA | https://statements.qld.gov.au/statements/95831; 2022 | B |
| 2022; reporting period extends through early 2023 | NSW flood sequence | Australia, New South Wales | Recurrent flood and waterlogging | More than **AUD432.4M** statewide agricultural damage: more than **AUD252.4M crops**, **AUD92.8M infrastructure**, and **AUD4.4M livestock** [4] | MISSING-DATA | Agriculture gross value added fell 2.8% in the Dec 2022 quarter as floods constrained livestock and grain production [58] | https://knowledge.aidr.org.au/resources/flood-new-south-wales-2022/; source date MISSING-DATA | A |

**Australia takeaway:** NSW provides one of the clearest category-separated loss records. Queensland demonstrates the need to retain producer counts even when hectare and sector-value fields remain unavailable.

## 3. COVERAGE TABLE.

| Archive or source family | What was actually checked | Coverage and useful fields | Agriculture-specific gap | Sweep status |
|---|---|---|---|---|
| IBTrACS | Dataset description and downloadable-resource metadata | Worldwide tropical-cyclone tracks; merged agency best tracks; public CSV and GeoJSON. The recovered description spans 1842-2026 [21] | No canonical crop hectares, farm values, farmer actions, or recovery duration. Early storm-matching issues can inflate historical storm counts [21] | **Metadata checked; no full row-by-row export sweep** |
| EM-DAT | Database site, archive description, methodology paper | 1900-present human/economic impacts; systematically recorded since 1988; country-event records and standard impact fields [20] | Thresholded at 10 deaths, 100 affected, emergency declaration, or international-assistance call. Indirect and long-term losses can be overlooked [20] | **Methodology checked; no licensed full-database reconciliation** |
| Dartmouth Flood Observatory | Observatory mission and archive descriptions | Remote-sensing maps of changing surface water and near-real-time flood measurement [3] | Surface-water extent does not prove cultivated-land impact, crop stage, value, farmer behavior, or recovery | **Metadata checked; no complete event export joined to cropland** |
| IMD | Search for event and national records | Relevant alert source for India and the required Odisha platform | No single public, normalized historical table linking every IMD alert to farm hectares, crop stage, action, and recovery was recovered | **Not exhaustively swept** |
| NOAA/NCEI Storm Events | Search interface and database description | US severe-weather records from Jan 1950 through Apr 2026, including event narratives and reported damage [19] | US-only; reported damage is inconsistent and not a global farm-loss taxonomy | **Interface checked; no full event-row export** |
| National records | Samples from Kerala SDMA, Assam SDMA, Queensland, NSW, US/Canada reporting and national assessments | Often best source for local hectares, producer counts, infrastructure, and program actions | Fragmented portals, changed links, scanned PDFs, local languages, revised totals, and non-machine-readable daily reports | **Sampled, not globally exhaustive** |
| FAO, OCHA, World Bank, UN and PDNAs | Full reports for Pakistan, Thailand, Sudan, Nepal, England, Peru and regional cases | Best evidence for agriculture-sector damage, losses, needs, actions, and recovery windows | Assessments are selective; farmer behavior is often replaced by agency plans; inaccessible areas may be estimated [32] | **Targeted primary-source sweep** |
| GDACS | API documentation from prior research | Custom event extraction is available in GeoJSON, with pagination beyond 100 records [59] | Hazard-event catalog, not a complete agricultural impact ledger | **API documentation checked; not used as farm-loss authority** |

The table establishes why an "all archives swept" statement would be false. The correct reproducibility unit is a dated archive snapshot, query, raw record ID, and join version.

## 4. WHAT IS MISSING.

| Gap class | Known affected events | Missing fields | Why it matters | Backfill route |
|---|---|---|---|---|
| No accessible event-level agricultural assessment | Kashmir 2014; Chennai 2015; Bihar 2017; Kerala 2021/2024; Sri Lanka 2016/2017; China 2016/2024; South Africa 2022; US 1993/2019; California 2023 | Crop hectares, commodities, value, actions, recovery | These cannot provide supervised loss labels | State or national disaster memoranda, agriculture-ministry compensation files, crop-insurance data |
| Series collapsed into a generic label | "Assam yearly," "Vietnam Mekong floods," "Cambodia," "Sahel floods," "France," "Canada," "Argentina," "Colombia," "NSW" | Event IDs, dates, annual denominator, severity threshold | A series label is not an event ledger | Define the event universe first, then export every archive record and deduplicate by time-space overlap |
| Occurrence known, agriculture unverified | West Sumatra 2024; Jakarta 2007/2013/2020; Ahr 2021; Emilia-Romagna 2023; Rio Grande do Sul 2024 | Sector-specific agricultural area and value | Total deaths or all-sector losses cannot train a farm-loss model | Local agriculture departments, producer associations, satellite cropland intersections, audited loss reports |
| Farmer behavior absent | Most rows | Evacuation, early harvest, livestock movement, seed protection, drainage, salvage, replanting choices | The advisory engine cannot learn action effectiveness from agency recommendations alone | Household surveys, extension logs, IVR call records, after-action interviews |
| Recovery duration absent | Most rows | Drainage completion, first planting, first harvest, livestock restocking, irrigation repair, debt recovery | "Recovered" is not one date | Track milestone-specific dates and censor still-open recoveries |
| Conflicting estimates | Bangladesh 1998 and many fast-moving disasters | Competing hectare totals and assessment dates | Silent selection creates label noise | Preserve each estimate, source date, method, geographic scope, and preferred-value rule |
| Weak historical coverage | Pre-1988 events and small rural events | Event occurrence and all farm effects | EM-DAT is systematically recorded only since 1988 and is thresholded [20] | Historical newspapers, agricultural censuses, hydrological yearbooks, district records |

The largest unresolved requirement is the phrase **"every major flood."** "Major" needs a computable rule, such as EM-DAT inclusion, DFO severity, at least 10,000 ha of agricultural land, at least US$10M farm loss, or a national emergency declaration. Different rules produce different ledgers.

## 5. PATTERNS.

| Recurring mechanism | Evidence case | Farm consequence | Advisory implication |
|---|---|---|---|
| Crop-stage submergence | Bangladesh 1998 damaged Aus harvests, Aman nurseries, and transplanting [30] | Yield loss depends on phenology, depth, and duration | Join forecast depth-duration to crop variety and growth stage |
| Prolonged waterlogging | Pakistan 2022 and England 2013-14 [32][27] | Delayed planting, root disease, machinery access failure | Send drainage and replant messages only after field accessibility and soil checks |
| Erosion, sand and debris deposition | US 2011 levee breaches damaged future soil productivity [42] | Multi-season productivity loss, not only current-crop loss | Add topsoil loss, sand depth, and remediation class to post-event survey |
| Irrigation and drainage failure | Pakistan 2010/2022 [31][32] | Fields stay flooded after rain stops; next crop is lost | Treat canal, pump, bund, culvert, and outlet status as first-class farm assets |
| Livestock mortality and fodder loss | Pakistan 2010, Sudan 2020, British Columbia 2021 [31][2][49] | Immediate asset loss plus milk, breeding, and nutrition impacts | Trigger animal movement, fodder reserve, vaccination, carcass, and shelter rules |
| Fisheries and ponds | Pakistan 2022 included fisheries/aquaculture damage [32] | Pond overtopping, stock escape, contamination, embankment failure | Ask whether the farmer owns ponds and provide separate water-quality and embankment actions |
| Stored input and food loss | Pakistan 2011 lost stored seed and grain [44] | Disaster removes both current food and next-season capacity | Pre-alerts should elevate and waterproof seed, feed, documents, medicines, and small equipment |
| Road and market isolation | Pakistan and Thailand assessments document infrastructure-dependent recovery | Produce spoils even where fields survive | Include route accessibility, collection-center status, cold storage, and buyer communication |
| Compound hazard sequence | Kerala, Myanmar, East Africa, and West Sumatra combine rainfall with flash flood, landslide, cyclone, or lahar | A flood-only rule can understate debris, slope, wind, and access hazards | Preserve multi-label hazard types and select the most restrictive safety action |

**Case study - Pakistan 2010 versus Pakistan 2022.** Both floods devastated agriculture, but their data reveal different mechanisms. In 2010, emergency seed and irrigation work protected the next wheat season and created measurable outputs. In 2022, widespread waterlogging, cotton and rice losses, livestock deaths, and damaged drainage produced a recovery plan extending to five years. This contrast shows that rainfall magnitude alone cannot determine recovery advice; drainage persistence and asset damage govern the clock.

**Case study - Thailand 2011.** More than 6M ha were affected, yet the flood also became a national logistics and industrial crisis. For an Odisha engine, the lesson is to distinguish direct field loss from market isolation: a farmer can lose income even when a crop survives if roads, processors, or buyers fail.

**Case study - Sudan 2020.** Rainfed crops, irrigated crops, livestock, water points, and fishing assets failed together. The mechanism supports a livelihood graph rather than a single crop record: each household node should connect plots, animals, ponds, water, storage, roads, and credit.

## 6. HOW IT FEEDS THE ENGINE.

### Validation data

Create one immutable row per `event x administrative unit x farm-system x assessment date`. Required fields are event ID, hazard labels, start/end dates, polygon, source date, crop, variety, growth stage, area exposed, area damaged, loss value and currency year, livestock/fish loss, infrastructure damage, observed action, delivered assistance, recovery milestone, grade, and missingness reason. Never use zero where the source says nothing.

Use the strongest cases as holdout tests:

| Test case | What it validates | Failure condition |
|---|---|---|
| Pakistan 2022 | Compound crop-livestock-fisheries losses and long waterlogging | Model predicts recovery immediately after rainfall stops |
| Thailand 2011 | Months-long inundation and supply-chain interruption | Model issues only field-level advice |
| Bangladesh 1998 | Crop-stage sensitivity and nursery/transplant disruption | Model treats all paddy stages equally |
| Sudan 2020 | Rainfed-irrigated-pastoral differentiation | Model sends the same action to every livelihood |
| US 2011 | Soil-productivity damage after levee breach | Model closes the case after current-crop loss |
| British Columbia 2021 | Intensive livestock evacuation and mortality | Model lacks species, housing, feed, and evacuation capacity |

### Pattern priors, not deterministic truth

Historical frequency can initialize priors such as `P(paddy loss | depth, duration, stage)` or `P(replant delay | drainage failure)`. It must not override a farm's current observations. Odisha's live posterior should update from IMD alerts, local rain and river sensors, field elevation, soil drainage, crop stage, farmer confirmation, and neighboring reports.

### Rule seeds

1. **Before inundation**: if warning lead time and safe access permit, prioritize human safety; move livestock and feed; raise seed, documents, medicines, pumps, and small equipment; harvest only mature crops where safe; clear drainage without entering dangerous water; photograph insured assets.
2. **During impact**: stop field-entry advice, isolate electricity and contaminated water risks, maintain IVR check-ins, and route only verified evacuation and animal-shelter information.
3. **After water recedes**: require field-access confirmation; assess depth-duration, erosion, sand/silt, contamination, carcasses, pond escape, and irrigation damage; then decide salvage, short-cycle replanting, fallow, or soil remediation.
4. **Recovery**: schedule reminders for loss reporting, seed and fodder requests, veterinary visits, canal repair, credit/insurance, first planting, first harvest, and unresolved debt.

### SMS/IVR implementation

Each message should contain one action, one deadline, and one confirmation question. Example: `RED FLOOD WARNING. Move cattle and dry fodder to the named shelter before 6 PM. Do not cross flowing water. Press 1 when complete; press 2 for transport help.` BAMIS demonstrates combining automated-weather-station and agricultural data across 487 subdistricts, while mKisan demonstrates the reach of rural SMS [54][53]. The interface should use Odia voice, digits for response, repeat-on-demand, and escalation to an extension worker when confidence is low.

## 7. REAL-vs-FILLER + NOISE LOG.

| Candidate datum or claim | Classification | Treatment |
|---|---|---|
| Pakistan 2022 PDNA agriculture figures | REAL, Grade A | Retain exact PKR and US dollar figures, hectares, sector, province, and assessment date [32] |
| Pakistan 2010 FAO hectares, value, inputs, and two-year horizon | REAL, Grade A | Retain as quantified damage plus documented intervention outcomes [31] |
| China 1998 FAO crop footprint | REAL, Grade A | Retain 22M ha affected and 4.8M ha destroyed [30] |
| Bangladesh 1998 760,000/425,000 ha versus 800,000/575,000 ha | CONFLICT | Prefer contemporaneous FAO for the main ledger; retain secondary estimate as an alternate, not an average [30][43] |
| "One-third of Pakistan was underwater" | NOISY HEADLINE | Keep only as qualitative context; do not use as agricultural hectares |
| Brazil 2024 total economic loss | WRONG SECTOR FOR THIS FIELD | Do not enter as agricultural damage without a sector breakdown |
| China 2024 total natural-disaster loss | WRONG SECTOR AND MULTI-HAZARD | Exclude from event-specific crop-loss target |
| Thailand 2011 "global supply-chain flood" | REAL CONTEXT, NOT A FARM METRIC | Keep as a mechanism tag; train agricultural loss only from the THB agriculture/livestock/fisheries table |
| West Sumatra 2024 fatalities | REAL EVENT EVIDENCE, NO FARM LABEL | Keep event occurrence; agricultural fields remain MISSING-DATA [41] |
| Agency proposal treated as farmer action | FILLER/SEMANTIC ERROR | Separate recommendation, delivery, uptake, and measured outcome |
| Missing field changed to zero | FILLER/STATISTICAL ERROR | Prohibit; use null plus a reason code |
| Repeated reports of one regional flood | DUPLICATE RISK | Link by event family and retain country impacts separately |
| Future-dated or revised live-archive endpoints | VERSION RISK | Snapshot query time, archive version, and retrieval date |

The noise-control principle is simple: an impressive number is not automatically the right label. Sector, geography, currency year, assessment date, and denominator must match the target variable.

## 8. VERDICT.

### Synthesis: archives, regions, mechanisms, and time horizons

| Dimension | South Asia | East/Southeast Asia | Africa | Europe | Americas | Australia |
|---|---|---|---|---|---|---|
| Best-supported mechanism | Multi-season crop, livestock, irrigation, and waterlogging loss | Basin-scale inundation plus logistics and rice-stage effects | Rainfed-irrigated-pastoral livelihood failure | Prolonged waterlogging and river-basin inundation | Levee, soil-productivity, livestock, and atmospheric-river effects | Crop, infrastructure, and livestock accounting |
| Strongest case | Pakistan 2022 | Thailand 2011 and China 1998 | Sudan 2020 | England 2013-14 and Oder 1997 | US 2011, Peru 2017, BC 2021 | NSW 2022 |
| Typical evidence base | PDNA, FAO, state memoranda | World Bank assessment, FAO and Mekong reports | FAO/OCHA rapid assessment | Government study and academic hydrology | National agencies, UN and case studies | State inquiries and disaster reports |
| Largest trade-off | Rich PDNAs but fragmented Indian state records | Excellent hydrology but weak country-specific farmer behavior | Large livelihood effects but sparse harmonized valuation | Strong total-loss data but weak farm disaggregation | Detailed local cases but poor continental normalization | Strong state reporting but limited historical harmonization |
| Recovery horizon revealed | Seasons to five years | Six months to five years | Immediate livelihood restoration plus unknown long tail | Weeks of waterlogging to multi-season soil repair | One missed planting through long soil/livestock recovery | Quarter-scale output loss plus infrastructure rebuilding |
| Odisha implication | Highest transfer value for monsoon paddy and drainage | Validate long inundation and market isolation | Add livestock, ponds, water points, and livelihood diversity | Model duration and soil access | Model levee breach, documentation, insurance, and intensive livestock | Use category-separated loss accounting |

The archive strategies are complementary, not interchangeable. **IBTrACS** answers where and how a cyclone moved; **DFO** answers where surface water expanded; **EM-DAT** answers whether a threshold-crossing disaster produced reported human or economic impacts; **NOAA** gives detailed US weather-event narratives; **national records and PDNAs** are where crop hectares, commodities, infrastructure, and recovery actions usually appear. Joining them creates evidence; substituting one for another creates false precision.

The non-obvious tension is between scale and usefulness. Global archives make events comparable but omit the farm variables required for advice. Local assessments contain actionable detail but use inconsistent currencies, crop calendars, boundaries, and methods. The system should therefore maintain two layers: a normalized global event index and an evidence-preserving local impact layer.

A second tension concerns actions. Historical assessments often report what governments supplied, not what farmers chose or whether the choice reduced loss. Consequently, history can seed rules and test plausibility, but it cannot by itself estimate the causal effectiveness of "harvest early," "move livestock," or "replant short-cycle rice." Prospective Odisha pilots must capture alert receipt, action taken, lead time, constraints, and outcome.

### Final verdict

**Verdict: usable as a high-value, explicitly incomplete seed corpus; not valid as "the complete global ledger."** The named-event requirement has been honored by retaining every candidate in the brief, including rows for which the agricultural record remains MISSING-DATA. However, asserting that no major agricultural flood worldwide has been omitted would be fabricated.

For a production release, define "major," acquire and snapshot the full archive exports, deduplicate event families, intersect event footprints with contemporaneous cropland, commission national-record backfills, and publish a machine-readable change log. Until then, grades A and B may support validation and rule design; Grade C supports context; Grade D must never be used as a numeric training label.

## References

1. *World Bank Document*. https://documents1.worldbank.org/curated/en/677841468335414861/pdf/698220WP0v10P106011020120Box370022B.pdf
2. *The Sudan 2020 Flood impact rapid assessment (September 2020)*. https://www.fao.org/fileadmin/user_upload/emergencies/docs/The%20Sudan%20Flood%20Impact%20Assessment.pdf
3. *Dartmouth Flood Observatory (DFO)*. https://un-spider.org/dartmouth-flood-observatory-dfo
4. *New South Wales Flood, 2022 - AIDR*. https://knowledge.aidr.org.au/resources/flood-new-south-wales-2022/
5. *Impact of 2014 Winter Floods on Agriculture in England - GOV.UK*. https://assets.publishing.service.gov.uk/media/5a74a46d40f0b61df47774b1/RFI7086_Flood_Impacts_Report__2_.pdf
6. *Causes and Impacts of Flood Events in Emilia-Romagna (Italy ...*. https://www.mdpi.com/2073-445X/13/11/1800
7. *Flood and Excessive Moisture - Farmers.gov*. https://www.farmers.gov/protection-recovery/flood
8. *Nepal: Flood impact assessment*. https://openknowledge.fao.org/handle/20.500.14283/CD5014EN
9. *Report Name: Unprecedented floods in Rio Grande do Sul ...*. https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Unprecedented%20floods%20in%20Rio%20Grande%20do%20Sul%20threaten%20Brazil%27s%20agricultural%20output_Brasilia_Brazil_BR2024-0009
10. *EM-DAT - The international disaster database*. https://www.emdat.be/
11. *Pakistan floods - a year later - fao.org*. https://www.fao.org/newsroom/detail/Pakistan-floods---a-year-later/
12. *Peru: UN agency supports recovery of some 7,000 farmers from ...*. https://news.un.org/en/story/2017/05/557772
13. *Nepal Flood 2017: Post Flood Recovery Needs Assessment - UN*. https://un.org.np/resource/nepal-flood-2017-post-flood-recovery-needs-assessment
14. *UTTARAKHAND FLOODS, 2013 - ActionAid India*. https://www.actionaidindia.org/emergency/uttarakhand-floods-2013/
15. *ODRA 1997 FLOOD EFFECTS ON SOIL PROPERTIES OF CULTIVATED ...*. https://www.international-agrophysics.org/pdf-107035-37844?filename=Odra-1997-flood-effects-o.pdf
16. *Final Report on 1998 Floods in the People's Republic of China*. https://reliefweb.int/report/china/final-report-1998-floods-peoples-republic-china
17. *Nigeria Situation Report, 1 November 2022 - UN-OCHA*. https://www.unocha.org/publications/report/nigeria/nigeria-situation-report-1-november-2022
18. *FAO Knowledge Repository*. https://openknowledge.fao.org/bitstreams/94c33ef0-ea20-4e0b-8846-da2ef9199ff5/download
19. *Storm Events Database | National Centers for Environmental Information*. https://www.ncei.noaa.gov/stormevents
20. *EM-DAT: the Emergency Events Database - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212420925003334
21. *IBTrACS: Global Storm Tracks | Humanitarian Dataset | HDX*. https://data.humdata.org/dataset/ibtracs-global-tropical-storm-tracks
22. *Eastern Africa: El Niño Floods Impact Snapshot (May 2024) | OCHA*. https://www.unocha.org/publications/report/somalia/eastern-africa-el-nino-floods-impact-snapshot-may-2024
23. *Annual Mekong Flood Report 2013 - Cambodia | ReliefWeb*. https://reliefweb.int/report/cambodia/annual-mekong-flood-report-2013
24. *Flood Management in East Africa: A Case Study of Kenya and Tanzania - Mashariki Research and Policy Centre*. https://masharikirpc.org/flood-management-in-east-africa-a-case-study-of-kenya-and-tanzania/
25. *El Nino Patterns On Climate Trends In Kenya And East Africa*. https://thekenyatimes.com/weather/world-met-explains-el-nino-patterns-in-kenya-and-east-africa/
26. *Nepal Flood 2017, Post Flood Recovery Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/nepal-flood-2017-post-flood-recovery-needs-assessment
27. *1*. https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/401235/RFI7086_Flood_Impacts_Report__2_.pdf
28. *Annual Mekong Flood Report 2011 - Cambodia | ReliefWeb*. https://reliefweb.int/report/cambodia/annual-mekong-flood-report-2011
29. *fao.org*. https://www.fao.org/4/ba0062e/ba0062e00.pdf
30. *FAO/GIEWS Special Report on Floods in Asia -  27 August 1998  *. https://openknowledge.fao.org/bitstreams/1675ed91-da8d-475c-9740-2228a5c55eb3/download
31. *PakistanFloods1yrBrochure_Artwork_HiRes_pat.pdf*. https://openknowledge.fao.org/server/api/core/bitstreams/d33e6dda-11f5-47cb-a1d3-2a8d9abb8e64/content
32. *World Bank Document*. https://documents1.worldbank.org/curated/en/099910001032330716/pdf/P17999109c267907f0aaa70f55da13e2371.pdf
33. *Floods 2019 - Kerala State Disaster Management Authority*. https://sdma.kerala.gov.in/floods-2019/
34. *ASDMA - sdrf.assam.gov.in*. https://sdrf.assam.gov.in/dfr/
35. *Economic losses from weather- and climate-related extremes in ...*. https://www.eea.europa.eu/en/analysis/indicators/economic-losses-from-climate-related
36. *Assam Flood Report | Assam State Disaster Management ...*. http://asdma.assam.gov.in/information-services/assam-flood-report-0
37. *Report Name: Climate Reports Highlight Agriculture*. https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Climate%20Reports%20Highlight%20Agriculture%20_Beijing_China%20-%20People%27s%20Republic%20of_CH2024-0046.pdf
38. *Annual economic losses caused by weather-and climate-related ...*. https://www.eea.europa.eu/en/analysis/indicators/economic-losses-from-climate-related-1760360184/annual-economic-losses-caused
39. *Ministry of Agriculture - On the Crop Forecast Survey for the ...*. https://www.parliament.gov.zm/node/11744
40. *Floods triggered by five consecutive days of heavy ...*. https://www.facebook.com/DailyStarNews/posts/floods-triggered-by-five-consecutive-days-of-heavy-monsoon-rain-have-submerged-a/1374438128170796
41. *Floods kill 43 in Indonesia's West Sumatra, 15 missing Reuters https://www.reuters.com › world › asia-pacific › floods-...*. https://www.reuters.com/world/asia-pacific/floods-kill-37-indonesias-west-sumatra-17-missing-2024-05-13
42. *The impacts of 2011 induced levee breaches on agricultural ...*. https://www.researchgate.net/publication/270376940_The_impacts_of_2011_induced_levee_breaches_on_agricultural_lands_of_Mississippi_River_Valley
43. *1998 Bangladesh flood*. https://en.wikipedia.org/wiki/1998_Bangladesh_flood
44. *PAKISTAN - Food and Agriculture Organization*. https://www.fao.org/fileadmin/user_upload/emergencies/docs/Pakistan11_Executive_Brief_07_10_11.pdf
45. *Analysis: Deforestation ignored as Sumatra faces its worst flood disaster*. https://www.thejakartapost.com/opinion/2025/12/16/analysis-deforestation-ignored-as-sumatra-faces-its-worst-flood-disaster
46. *The Humanitarian Impacts of El Niño in Southern Africa ...*. https://reliefweb.int/report/mozambique/humanitarian-impacts-el-nino-southern-africa-september-2024
47. *PAKISTAN FLOODS RAPID RESPONSE PLAN 2011 - fao.org*. https://www.fao.org/fileadmin/user_upload/emergencies/docs/Pakistan_Rapid_Response_Plan_2011.pdf
48. *Thousands of animals have died on flooded B.C. farms in ...*. https://www.cbc.ca/news/canada/british-columbia/bc-flooding-2021-livestock-deaths-abbotsford-1.6252774
49. *Livestock death toll from B.C. flooding: 628,000 poultry ...*. https://www.ctvnews.ca/vancouver/article/livestock-death-toll-from-bc-flooding-628000-poultry-12000-hogs-420-cows/
50. *Deloitte Report estimates $7.7 billion cost from the floods*. https://statements.qld.gov.au/statements/95831
51. *Document heading in Calibri Light green - qra.qld.gov.au*. https://www.qra.qld.gov.au/sites/default/files/2022-07/dae_report_-_south_east_queensland_rainfall_and_flooding_event_-_8_june_2022.pdf
52. *The impacts of 2011 induced levee breaches on agricultural ...*. https://www.tandfonline.com/doi/pdf/10.2489/jswc.67.1.5A
53. *http://mkisan.gov.in/Home/AboutPushSMS*. http://mkisan.gov.in/Home/AboutPushSMS
54. *http://bamis.gov.bd/en/page/introduction*. http://bamis.gov.bd/en/page/introduction
55. *Flash Floods Threaten India’s ‘Safe Zones’ – India Water ...*. https://www.indiawaterportal.org/climate-change/disasters/flash-floods-threaten-indias-safe-zones-climate-change-is-redrawingthe-risk-map
56. *2024 Wayanad landslides - Wikipedia*. https://en.wikipedia.org/wiki/2024_Wayanad_landslides
57. *Impacts of the summer 2007 floods on agriculture in England*. https://onlinelibrary.wiley.com/doi/10.1111/j.1753-318X.2009.01031.x
58. *Impacts of flooding in December quarter 2022 | Australian ...*. https://www.abs.gov.au/articles/impacts-flooding-december-quarter-2022
59. *http://gdacs.org/Documents/2025/GDACS_API_quickstart_v1.pdf*. http://gdacs.org/Documents/2025/GDACS_API_quickstart_v1.pdf
