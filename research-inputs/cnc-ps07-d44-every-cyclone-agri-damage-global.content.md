# Global Cyclone Agriculture Ledger: Evidence, Gaps, and Rules

## 1. EXECUTIVE SUMMARY.

- **Completeness Boundary**: No global archive contains a verified event-by-event join of tropical-cyclone tracks, floods, crops, hectares, monetary losses, and farmer actions. IBTrACS is a track archive, EM-DAT is a thresholded country-level disaster database, and Dartmouth covers large floods from 1985 onward [11][10][4] -> treat this report as an auditable minimum ledger, not a defensible claim that every worldwide incident since 1891 has been captured.
- **Archive Mismatch**: IBTrACS contains storm and landfall variables but no agriculture-impact field [11]; EM-DAT records human and economic losses for disasters meeting inclusion criteria [10]; Dartmouth excludes tropical storms without significant river flooding [4] -> build a versioned crosswalk rather than treating any one archive as complete.
- **Largest Verified Crop Footprints**: The strongest event-level records in this sweep include **1.4M ha partially damaged by Sidr**, **more than 715,000 ha destroyed by Idai**, **498,300 ha affected by the Remal-plus-flood sequence**, and **462,766 ha affected by Rai/Odette** [8][36][16][15] -> use these high-confidence cases to stress-test an Odisha advisory engine across wind, flood, surge, and recovery scenarios.
- **Compound Attribution Risk**: Remal's reported **$596M** agriculture, livestock, and fisheries loss includes later floods, while Gombe's **220,425 ha** figure covers the wider rainy season rather than the cyclone alone [16][5] -> preserve `hazard_component`, `assessment_window`, and `attribution_scope` in every training record.
- **Long-Tail Farm Loss**: Hurricane Michael's Georgia pecan estimate included **$100M** in the current crop, **$260M** in lost trees, and **$200M** in projected profit losses over a decade [34] -> model annual crop loss separately from perennial asset destruction and multi-year income loss.
- **Farmer-Action Evidence Gap**: Most assessments quantify damage or institutional relief, not what farmers actually did. Sidr, Mocha, and Rai/Odette sources document seed, input, livestock, fisheries, or cash support, but usually not household-level timing or compliance [12][23][15] -> collect action confirmations through SMS/IVR rather than labeling relief delivery as farmer behavior.
- **Locust Causal Correction**: The 2019-2021 desert-locust emergency was associated with exceptional rain from Arabian Peninsula cyclones Mekunu and Luban, not demonstrated in the cited evidence as a consequence of Idai or Kenneth [1]. FAO reports that control operations treated nearly **2.3M ha** and averted an estimated **4.5M tonnes** of crop loss [13] -> retain the locust case as a cross-basin compound-hazard example, but do not misattribute causality.
- **Operational Use**: NASA recommends IMERG Early or Late Run for low-latency applications and Final Run for research [50], while ECMWF provides forecasts, reanalyses, and archive access [51][52] -> pair IMD warnings with hyperlocal sensors for operations, then use quality-controlled historical products for retrospective validation.

**Grade key:** **A** = event-specific metric from an official government, UN, World Bank, or peer-reviewed primary source; **B** = authoritative but preliminary, partial, or compound assessment; **C** = credible secondary, subnational, or inseparably combined estimate; **D** = event is in the problem scope, but an accessible event-specific agriculture record or farmer-action record is MISSING-DATA.

## 2. THE COMPLETE EVENT LEDGER: organized by region then year.

A literal complete worldwide ledger cannot be certified from the named archives. The tables below are complete for the incidents explicitly enumerated in the problem statement, plus two collision-relevant additions found in the sweep: Vietnam's 2005 Typhoon Damrey and Sri Lanka's 2025 Cyclone Ditwah. They retain unverified cases instead of silently deleting them. `MISSING-DATA` means the requested field was not established in the accessible evidence, not that agriculture suffered no damage.

### North Indian Ocean

| Date | Name | Country/region | Type | Agricultural damage: hectares, crops, value | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| Nov 1970 | Bhola | Bangladesh | Cyclone, surge, flood | MISSING-DATA: no accessible event-specific crop area, crop list, or agriculture-only value established in this sweep. | MISSING-DATA. | MISSING-DATA; retained because it is explicitly named in the brief. | D |
| 1971, exact date MISSING-DATA | Odisha cyclone | India, Odisha | Cyclone, surge, flood | MISSING-DATA. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| Nov 1977 | Andhra cyclone | India, Andhra Pradesh | Cyclone, surge, flood | MISSING-DATA. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| Apr 1991 | Bangladesh cyclone | Bangladesh | Cyclone, surge, flood | MISSING-DATA: overall disaster totals must not be presented as agriculture-only loss. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| 6 Nov 1996 | Andhra Pradesh cyclone | India, Andhra Pradesh | Cyclone, surge, flood | **353,000 ha paddy**, **56,000 ha other crops**, and **more than 70,000 ha coconut plantations** were reported completely destroyed [25]. | Household behavior MISSING-DATA. The Red Cross reported rescue, relief, and emergency-supply financing [25]. | `https://www.ifrc.org/docs/appeals/96/209601.pdf`; 13 Nov 1996. | A |
| Jun 1998 | Gujarat cyclone | India, Gujarat | Cyclone, surge | MISSING-DATA: no sufficiently authoritative event-specific agriculture record was accessible. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| May 1999 | Cyclone 2A | Pakistan, Sindh coast | Cyclone, surge | MISSING-DATA. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| 29 Oct 1999 | Odisha Super Cyclone | India, Odisha | Cyclone, surge, flood | Accessible official assessment confirms landfall, extreme winds, surge, and severe coastal-district effects, but the requested crop hectares and agriculture-only value are MISSING-DATA [22]. | MISSING-DATA. | `https://fsi.nic.in/uploads/documents/assessment_of_damage.pdf`; source date MISSING-DATA. | B for event; D for agriculture fields |
| 2001, exact date MISSING-DATA | Gujarat cyclone | India, Gujarat | Cyclone | MISSING-DATA. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| 15 Nov 2007 | Sidr | Bangladesh | Cyclone, surge, flood | **113,000 ha totally** and **1.4M ha partially** damaged; **1.3M tonnes** of crop loss; more than **100,000 livestock deaths** [8]. The PDNA put total disaster damage and loss at BDT115.6B or $1.7B, but that is not agriculture-only [8]. OCHA separately reported more than 1.8M acres of crops damaged and more than 523,000 livestock killed, showing assessment disagreement [12]. | Household pre-actions MISSING-DATA. FAO later assisted **47,000 households** with seeds, inputs, and fishing nets [12]. | `https://documents1.worldbank.org/curated/en/337501468014345112/pdf/PIDAppraisal0BD0Cyclone0May01902008.pdf`; 15 May 2008 [8]. `https://www.unocha.org/publications/report/bangladesh/bangladesh-cyclone-sidr-ocha-situation-report-no-10`; 26 Nov 2007. | A |
| 2 May 2008 | Nargis | Myanmar, Ayeyarwady and Yangon | Cyclone, surge, flood | MISSING-DATA in the accessible source for event-wide paddy area, salinity, and agriculture-only value; the source confirms the landfall and affected townships [37]. | MISSING-DATA. | `https://link.springer.com/article/10.1007/s10333-020-00829-0`; 2020. | B for event; D for agriculture fields |
| May 2009 | Aila | Bangladesh and India | Cyclone, surge, saline flood | MISSING-DATA: no event-wide, source-verifiable agriculture total was established. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| May 2020 | Amphan | India and Bangladesh | Cyclone, surge, flood | MISSING-DATA: accessible evidence did not establish a harmonized cross-border crop area or agriculture-only value. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| May 2021 | Tauktae | India, Arabian Sea coast | Cyclone | MISSING-DATA: preliminary crop reports were found during discovery, but no event-wide primary assessment suitable for this ledger was established. | MISSING-DATA. | MISSING-DATA; retained from the brief. | D |
| 14 May 2023 | Mocha | Myanmar | Cyclone, surge, flood | Approximately **327,000 ha of agricultural land** damaged, crop-production losses of about **$22.6M**, and nearly **13,000 livestock** lost with a reported value of **$6.7M** [23]. Seed stocks, fisheries, and agricultural infrastructure were also damaged [23]. | Household pre-actions MISSING-DATA. FAO proposed seed and fertilizer support, cash assistance, fishing gear and boats, animal restocking, and feed [23]. | `https://www.themimu.info/sites/themimu.info/files/documents/Urgent_Call_for_Assistance_on_Cyclone_Mocha_FAO_Jul2023.pdf`; Jul 2023. | A |
| Jun 2023 | Biparjoy | India, Gujarat | Cyclone | Gujarat announced an approximately **Rs240 crore relief package** for affected farmers in Kutch and Banaskantha, but crop hectares, commodity losses, and beneficiary count were MISSING-DATA in the accessible report [33]. | Farmer behavior MISSING-DATA; government relief announced. | `https://economictimes.indiatimes.com/news/india/gujarat-govt-announces-rs-240-cr-relief-package-for-farmers-affected-by-cyclone-biparjoy-in-kutch-banaskantha/articleshow/101765879.cms`; Jul 2023. | C |
| 26-27 May 2024 | Remal plus later floods | Bangladesh | Compound cyclone and flood sequence | Across Remal and the subsequent May-June floods, more than **498,300 ha** of standing crops and approximately **1M tonnes** of crops were reported lost [16]. The assessment also reported **23,928 ha** of grazing land and **81,914 ha** of fishponds or enclosures affected [16]. Combined crop, livestock, and fisheries loss was approximately **$596M**, affecting 1.7M farming households; this must not be labeled Remal-only [16]. | Some households used credit or sold livestock, a documented negative coping response [16]. | `https://openknowledge.fao.org/server/api/core/bitstreams/18f904d3-0e63-47c4-844f-298263ee655a/content`; 2024 appeal. | B because compound |
| 2025, exact landfall date MISSING-DATA here | Ditwah | Sri Lanka | Cyclone, flood, landslide | World Bank reporting estimated **$814M** in agriculture damage, including paddy, vegetables, subsistence farming, maize, and livestock [53]. Hectares are MISSING-DATA in the cited excerpt. | MISSING-DATA. | `https://www.worldbank.org/en/news/press-release/2025/12/22/damage-from-cyclone-ditwah-in-sri-lanka-estimated-at-4-1-billion`; 22 Dec 2025. | A for value; D for hectares/actions |

**North Indian Ocean takeaway:** the modern A/B cases provide useful crop-specific evidence, but the requested 1891-present IMD-wide claim remains unfulfilled. Legacy rows are deliberately visible as grade D, and Remal demonstrates why cyclone-only and compound-flood values cannot be merged.

### Western Pacific

| Date | Name | Country/region | Type | Agricultural damage: hectares, crops, value | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| 2005, exact date MISSING-DATA | Damrey | Vietnam | Typhoon and flood | FAO reported **318,000 ha of crops**, mainly rice, destroyed and a likely rice loss of **300,000-400,000 tonnes**; seafood and salt production were also affected [14]. This is not the 2017 storm of the same name. | MISSING-DATA. | `https://www.fao.org/4/J6398e/pays/VIE.htm`; 12 Oct 2005 [14]. | A |
| 8 Nov 2013 | Haiyan, Yolanda | Philippines | Typhoon, surge, flood | Coconut and rice impacts are documented in the assessment literature, but an event-wide hectare and agriculture-only value were not recoverable from the accessible primary text in this sweep: MISSING-DATA. | MISSING-DATA at household level; recovery documentation exists but was not converted into an observed-farmer-action label. | `https://www.fao.org/fileadmin/user_upload/emergencies/docs/FAO%20Typhoon%20Haiyan%20Executive%20Brief%2030%20April%202014.pdf`; 30 Apr 2014. | B for source; D for requested fields |
| 4 Nov 2017 | Damrey | Vietnam | Typhoon and flood | **59,392.7 ha** were damaged [20]. The agriculture-sector assessment totaled **VND5,346,420.3M** across crops, livestock, fisheries, and forestry [20]. | Household pre-actions MISSING-DATA; the assessment records restoration of production during recovery [20]. | `https://documents1.worldbank.org/curated/en/244871603784378547/pdf/2017-Vietnam-Post-Typhoon-Damrey-Rapid-Damage-and-Needs-Assessment.pdf`; assessment after 2017 event. | A |
| Sep 2018 | Jebi | Japan | Typhoon | MISSING-DATA: no national agriculture total meeting the report's source standard was established in the accessible official material. | MISSING-DATA. | Japanese national records searched; event-specific accessible agriculture URL/date MISSING-DATA. | D |
| Sep 2018 | Mangkhut, Ompong | Philippines | Typhoon, rain, landslide | Rice and corn losses were reported, but a source-verifiable nationwide hectare/value pair was MISSING-DATA in the accessible primary text. | Household behavior MISSING-DATA. DA, WFP, and FAO later distributed agricultural inputs to affected farmers. | `https://cagayanvalley.da.gov.ph/2019/02/18/da-rfo-2-wfp-and-fao-distribute-agricultural-inputs-to-typhoon-mangkhut-stricken-farmers/`; 18 Feb 2019. | B for recovery source; D for totals |
| Oct 2019 | Hagibis | Japan | Typhoon and flood | MISSING-DATA: the official MAFF disaster page was located, but this sweep did not recover a nationwide event-specific crop-area/value total from it. | MISSING-DATA. | `https://www.maff.go.jp/j/saigai/typhoon/191011/index.html`; source date MISSING-DATA. | A for official source; D for extracted fields |
| 16-17 Dec 2021 | Rai, Odette | Philippines | Typhoon, surge, flood | **P13.3B** in agriculture losses, **462,766 ha** affected, **273,062 tonnes** of production loss, and **533,709 farmers and fishers** affected [15]. Rai and Odette are the same event and appear once. | Household pre-actions MISSING-DATA. DA reported rice, corn and vegetable seed, coconut seednuts and seedlings, fertilizer, animal stocks and medicines, and fiber inputs in recovery [15]. | `https://www.da.gov.ph/odette-affected-farmers-and-fisherfolk-receive-p3-billion-worth-of-interventions-from-da`; 20 Jan 2022 [15]. | A |
| 7 Sep 2024 | Yagi | Vietnam | Typhoon and flood | **286,647 ha rice**, **63,352 ha other crops**, **39,232 ha fruit trees**, and **190,028 ha forests** were flooded or damaged; **35,812 ha** of aquaculture and **11,835 cages** were damaged or washed away [26]. Reported animal deaths included **44,550 livestock** and **5,761,454 poultry** [26]. Selected-province damage was VND8,638.58B or $354.04M, with losses of VND5,520.50B or $226.25M [26]. | More than 1M people were safely evacuated, and the assessment describes proactive community action, but farm-specific actions remain MISSING-DATA [26]. | `https://www.undp.org/sites/g/files/zskgke326/files/2024-12/vmsa_final.pdf`; Dec 2024. | A |
| Yearly series, event names and dates MISSING-DATA | China typhoons | China | Typhoon, flood, surge | MISSING-DATA: a yearly national agriculture-loss series was not joined to individual IBTrACS events. | MISSING-DATA. | Chinese national and international sources searched; event-level agriculture join MISSING-DATA. | D |

**Western Pacific takeaway:** naming collisions are a major data-quality risk. Damrey 2005 and 2017 are separate storms, while Rai and Odette are aliases for one storm. The engine needs both a canonical storm identifier and a local-name alias table.

### Atlantic

| Date | Name | Country/region | Type | Agricultural damage: hectares, crops, value | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| Oct-Nov 1998 | Mitch | Honduras, Nicaragua, Guatemala, El Salvador | Hurricane, flood, landslide | Honduras lost an estimated **650,000 bags of coffee**, more than 20% of expected production, with beans, bananas, oil palm, citrus, and fruit seriously affected [19]. Nicaragua lost about **30% of coffee**, with maize, beans, and sorghum seriously affected [19]. Guatemala reported about **15% of coffee** lost [19]; El Salvador reported up to **80% of maize in affected areas** lost [19]. Comparable regional hectares/value are MISSING-DATA. | MISSING-DATA. | `https://www.fao.org/4/X0313E/X0313E00.htm`; 6 Nov 1998 [19]. | A for country crop statements |
| Aug 2005 | Katrina | United States Gulf Coast | Hurricane, surge, flood | MISSING-DATA: no defensible agriculture-only event total was established; general catastrophe loss must not be substituted. | MISSING-DATA. | NOAA and national records searched; agriculture URL/date MISSING-DATA. | D |
| Sep 2008 | Ike | United States, Texas and Louisiana | Hurricane, surge, flood | Louisiana agriculture, forestry, and fisheries losses for **Gustav and Ike combined** were reported at up to **$950M and rising** [49]. An Ike-only crop area and value are MISSING-DATA. | MISSING-DATA. | `https://www.lsuagcenter.com/topics/family_home/hazards_and_threats/recovery_assistance/agdisaster`; source date MISSING-DATA. | C because combined |
| Aug 2017 | Harvey | United States, Texas | Hurricane and flood | Texas A&M AgriLife economists estimated **more than $200M** in crop and livestock losses [28]. Hectares and commodity breakdown are MISSING-DATA in the cited excerpt. | MISSING-DATA. | `https://tscra.org/texas-agricultural-losses-from-hurricane-harvey-estimated-at-more-than-200m/`; 2017, exact source date MISSING-DATA. | C |
| Sep 2017 | Irma | Caribbean, including Puerto Rico | Hurricane, wind, flood | Direct event-specific agriculture hectares/value are MISSING-DATA here. USDA reports that Irma and Maria destroyed harvests and farm infrastructure [21], but the later census change is not a direct event-loss estimate. | MISSING-DATA. | `https://www.ers.usda.gov/publications/pub-details?pubid=106260`; 6 Apr 2023 [9]. | B for aftermath; D for direct total |
| Sep 2017 | Maria | Puerto Rico and Caribbean | Hurricane, wind, flood | Direct event-specific banana, coffee, and total-farm loss are MISSING-DATA in the accessible source. From 2012 to 2018, Puerto Rico farm sales fell **$170M or 26%**, including **$82M** in crop sales; poultry sales fell 58% or $28M and dairy sales fell 24% to $54M [21]. These are longitudinal aftermath indicators, not Maria-only losses. | MISSING-DATA. | `https://www.ers.usda.gov/publications/pub-details?pubid=106260`; 6 Apr 2023 [9]. | B for aftermath; D for direct total |
| Sep 2018 | Florence | United States, Carolinas | Hurricane and flood | MISSING-DATA: no source-verifiable agriculture-only value/hectare pair was established. | MISSING-DATA. | NOAA and state records searched; event-specific agriculture URL/date MISSING-DATA. | D |
| 10 Oct 2018 | Michael | United States, Georgia and Florida | Hurricane | Georgia agriculture losses exceeded **$2B** [35]. Pecan estimates included **$100M** in current crop loss, **$260M** in lost trees, and **$200M** in projected profits over a decade [34]. Hectares are MISSING-DATA. | MISSING-DATA. | `https://fieldreport.caes.uga.edu/news/georgia-farmers-face-more-than-2-billion-in-losses-from-hurricane-michael/`; source date MISSING-DATA. | A |
| Aug 2021 | Ida | United States, Louisiana | Hurricane, surge, flood | Approximately **168,000 acres of timber** were affected, with losses exceeding **$300M** [30]. A total crop/livestock value is MISSING-DATA. | MISSING-DATA. | `https://www.lsuagcenter.com/articles/page1632415649946`; 2021. | A for forestry component |
| Sep 2022 | Ian | United States, Florida | Hurricane, surge, flood | Estimated Florida production loss was **$1.03B** [18]. Exposed acreage included **1,077,427 acres** of field and row crops, **375,302 acres** of citrus, and **159,272 acres** of vegetables and melons [18]. The report covers near-term 2022 or 2022-23 production losses, not all future asset losses [18]. | MISSING-DATA. | `https://fred.ifas.ufl.edu/media/fredifasufledu/economic-impact-analysis/reports/FRE-Final-Hurricane-Ian-Report.pdf`; 9 Feb 2023 [18]. | A |
| Sep 2024 | Helene | United States, Georgia | Hurricane, wind, flood | Georgia agriculture and forestry damage was estimated at **at least $5.5B in present value** [27]. Affected hectares and a crop-only subtotal are MISSING-DATA. | MISSING-DATA. | `https://fieldreport.caes.uga.edu/wp-content/uploads/2025/08/AP-133-1_1.pdf`; publication date MISSING-DATA. | A |
| 8 Oct 2024 | Milton | United States, Florida | Hurricane | The accessible report established the event date, but the statewide agriculture production-loss value and hectares were MISSING-DATA in the extracted evidence [32]. | MISSING-DATA. | UF/IFAS agriculture loss assessment; exact accessible URL/date MISSING-DATA. | D |

**Atlantic takeaway:** agricultural estimates vary in scope - crop production, livestock, timber, perennial assets, and combined agriculture-forestry-fisheries totals are not interchangeable. The ledger therefore keeps units and accounting boundaries instead of ranking storms by a single misleading number.

### Southwest Indian Ocean and associated locust consequence

| Date | Name | Country/region | Type | Agricultural damage: hectares, crops, value | What farmers did | Source URL + source date | Grade |
|---|---|---|---|---|---|---|---|
| Mar 2017 | Enawo | Madagascar | Cyclone and flood | MISSING-DATA: no authoritative event-wide agriculture hectares/value pair was established. | MISSING-DATA. | National and humanitarian sources searched; accessible agriculture URL/date MISSING-DATA. | D |
| Mar 2019 | Idai | Mozambique, Zimbabwe, Malawi | Cyclone, flood, surge | More than **715,000 ha of crops** were destroyed [36]. Across the wider cyclone-and-flood crisis in the three countries, nearly **800,000 ha** of standing crops were destroyed [31]; the figures have different scopes and must not be summed. | MISSING-DATA. | `https://www.unocha.org/publications/report/mozambique/2018-2019-mozambique-humanitarian-response-plan-revised-following-cyclones-idai`; 2019. `https://openknowledge.fao.org/handle/20.500.14283/CC6057EN`; source date MISSING-DATA. | A |
| Apr 2019 | Kenneth | Mozambique | Cyclone and flood | Nearly **55,500 ha of crops** were affected, alongside loss of fishing livelihoods [36]. Agriculture-only value is MISSING-DATA. | MISSING-DATA. | `https://www.unocha.org/publications/report/mozambique/2018-2019-mozambique-humanitarian-response-plan-revised-following-cyclones-idai`; 2019. | A |
| 5 Feb 2022 | Batsirai | Madagascar | Cyclone and flood | The accessible source confirms landfall, but event-wide agriculture hectares, crop list, and value are MISSING-DATA [47]. | MISSING-DATA. | Humanitarian assessment located; exact agriculture source URL/date MISSING-DATA. | D |
| Mar 2022 | Gombe | Mozambique | Cyclone plus seasonal flooding | FAO reported **220,425 ha of crops lost since the start of the rainy season**, not Gombe-only [5]. The satellite analysis required field verification and updating [5]. | MISSING-DATA. | `https://openknowledge.fao.org/items/4ca16338-d1dd-497b-9f73-32b83140d2a2`; 2022 [5]. | B because seasonal compound |
| Feb-Mar 2023 | Freddy | Madagascar, Mozambique, Malawi | Long-lived cyclone and flood | MISSING-DATA: no harmonized regional, event-specific agriculture total was established. | MISSING-DATA. | National and humanitarian sources searched; accessible agriculture URL/date MISSING-DATA. | D |
| 15 Dec 2024 | Chido | Mozambique | Cyclone, surge, flood | OCHA reported more than **456,000 ha of land inundated**, including approximately **28,000 ha of cropland** [38][48]. Agriculture-only value is MISSING-DATA. | MISSING-DATA. | `https://www.unocha.org/publications/report/mozambique/mozambique-intense-tropical-cyclone-chido-flash-update-no-5-27-december-2024`; 27 Dec 2024. | B |
| 2019-2021 | Desert-locust upsurge | Horn of Africa and Yemen; antecedent rain in Arabian Peninsula | Compound climate, pest, and food-security crisis | FAO reported nearly **2.3M ha treated**, an estimated **4.5M tonnes of crop loss averted**, 900M liters of milk saved, food security protected for 41.5M people, and **$1.77B** in cereal and milk value protected [13]. These are response benefits, not cyclone-damage totals. | Farmers' own actions are MISSING-DATA; the record describes regional surveillance and control. | FAO locust response overview; 2021/2022 reporting [13]. | A for control outcomes |

**Southwest Indian Ocean takeaway:** Idai and Kenneth have strong hectare evidence, while Gombe illustrates seasonal attribution ambiguity. The locust row belongs in the consequence ledger only as a compound-hazard case: exceptional rain associated with Mekunu and Luban in the Arabian Peninsula is the supported antecedent [1], not a proven Idai/Kenneth causal chain.

## 3. COVERAGE TABLE: which archives were swept and their gaps.

| Archive/source family | What was swept | What it can establish | Gap that blocks the completeness mandate |
|---|---|---|---|
| IBTrACS, NOAA/NCEI | Product documentation, variables, coverage, and known limitations | The most complete global aggregation of tropical-cyclone best tracks from multiple agencies [11] | No crop, livestock, fisheries, hectare, farm-value, or farmer-action field [11]. Pre-1950 matching can produce artificially high storm counts, and some agency records are incomplete [11]. |
| EM-DAT | Public documentation and database scope | More than 27,000 mass disasters since 1900, with country-level human and economic loss information [10] | Thresholded inclusion: 10 deaths, 100 affected, emergency declaration, or international assistance [10]. Small agricultural incidents can be absent, and agriculture is not a universal event field. |
| Dartmouth Flood Observatory | Global archive description and record structure | Discrete large-flood events from 1985 onward, assembled from news, government, instrumental, and remote-sensing sources [4] | Excludes tropical storms without significant river flooding [4], does not cover pre-1985 floods, and its public structure does not provide a complete crop-impact join [3]. |
| IMD/RSMC New Delhi | Cyclone-report and disaster-assessment discovery for India and the North Indian Ocean | Hazard chronology, track, intensity, warning, and selected damage narratives | No accessible machine-readable 1891-present agriculture-impact table was found. Old cyclone reports, state agriculture memoranda, and crop statistics require manual multilingual joining. |
| NOAA and US national/state records | NOAA storm discovery plus USDA, university extension, and state reports | Strong recent US commodity, acreage, production-loss, and forestry assessments, as shown by Ian, Michael, Ida, and Helene | Accounting scopes differ by state and institution; historical reports often combine storms or omit agriculture-only subtotals. |
| FAO, World Bank, UNDP, OCHA, IFRC | Post-disaster assessments, appeals, special alerts, and response reports | The strongest cross-country crop, livestock, fisheries, livelihood, and response evidence in this ledger | Reports are assessment-driven, not a census of every cyclone. Preliminary and compound figures may be revised, and household farmer behavior is rarely measured. |
| National agriculture ministries and meteorological services | Targeted India, Bangladesh, Myanmar, Philippines, Vietnam, Japan, African, and Caribbean searches | Often the best local crop and relief details | Fragmented websites, changing URLs, scanned PDFs, local languages, inconsistent units, and no shared event identifier. |
| Published assessments | Peer-reviewed and institutional literature for gap filling | Mechanism detail, remote-sensing estimates, and longitudinal aftermath | Publication bias favors large disasters; a later paper may model exposure rather than report observed agriculture loss. |

The sweep therefore covered the major archive families requested, but not every row of every restricted, offline, scanned, or national database. IBTrACS gives the storm universe, EM-DAT gives a thresholded disaster universe, Dartmouth gives a large-flood universe, and assessments give selective agriculture evidence. Their intersection is useful; none is the requested complete ledger.

## 4. WHAT IS MISSING: events known to exist but with no accessible agri-impact record.

The grade-D rows are not null-impact events. They are unresolved joins. The highest-priority named gaps are Bhola 1970, Odisha 1971, Andhra 1977, Bangladesh 1991, Gujarat 1998 and 2001, Pakistan Cyclone 2A, Aila, Amphan, Tauktae, Haiyan, Jebi, Hagibis, Katrina, Florence, Milton, Enawo, Batsirai, and Freddy. China also remains an unresolved event-series problem rather than one row: the brief asks for yearly typhoon agriculture losses, but no canonical storm-to-agriculture table was established.

Several entire categories remain outside a defensible claim of completeness:

1. **Small and sub-threshold incidents.** EM-DAT's entry criteria can exclude locally severe crop losses that do not meet mortality, affected-population, emergency, or assistance thresholds [10].
2. **Pre-digital and pre-satellite history.** IBTrACS warns about early-record matching and incomplete agency records [11]. Agriculture detail is even less standardized than tracks.
3. **Standalone floods on agricultural land.** Dartmouth begins in 1985 and excludes tropical storms without significant river flooding [4]. The requested core line expands beyond tropical cyclones to every flood on farmland, a much larger universe not enumerated by this cyclone-led report.
4. **Attribution boundaries.** Remal plus later floods, Gombe plus the rainy season, Gustav plus Ike, and Irma plus Maria cannot be decomposed honestly without finer assessments.
5. **Farmer actions.** Most sources record what governments or aid agencies supplied, not whether a farmer harvested early, moved cattle, cleared drainage, protected seed, evacuated, borrowed, sold livestock, replanted, or changed crop choice.
6. **Comparable money.** Values mix production loss, asset damage, relief packages, forestry, fisheries, future profit, nominal local currency, and different assessment windows. Converting all rows to one number would create false comparability.

Closing these gaps requires the full IBTrACS CSV, licensed or bulk EM-DAT data, the Dartmouth geospatial archive, all IMD cyclone reports and state memoranda, DesInventar-style national records, agriculture-ministry reports, and a manual multilingual audit. Each event-country pair needs a frozen source snapshot, canonical storm ID, assessment date, unit, price year, revision number, and explicit `not_found` reason.

## 5. PATTERNS: the recurring damage mechanisms across all events.

| Recurring mechanism | Evidence in the ledger | Why loss persists | Advisory implication |
|---|---|---|---|
| Wind lodging and stripping | Yagi damaged rice, other crops, fruit trees, and forests [26]; Michael caused large pecan tree and future-income losses [34] | Annual crops lose standing yield; perennial crops also lose productive capital | Separate advice by crop stage and plant type. A mature paddy field and a young orchard need different triggers and recovery horizons. |
| River and pluvial flooding | Idai destroyed more than 715,000 ha [36]; Chido inundated land including cropland [48] | Waterlogging, erosion, delayed field access, contamination, and seed loss continue after winds end | Keep post-landfall rainfall and water-level monitoring active; do not close the warning workflow at landfall. |
| Surge and saline inundation | Sidr and Remal are cyclone-flood cases with extensive crop, livestock, grazing, and aquaculture impacts [8][16] | Salinity can prevent immediate replanting and contaminate drinking or livestock water | Trigger low-elevation evacuation, freshwater storage, seed/input elevation, and post-event salinity testing. |
| Livestock and feed shock | Mocha caused nearly 13,000 livestock losses [23]; Remal affected grazing land and fodder [16] | Animal survival depends on shelter, transport, clean water, fodder, and veterinary access | Treat livestock movement and feed storage as first-class actions, not appendices to crop advice. |
| Fisheries and aquaculture loss | Yagi damaged aquaculture area and cages [26]; Remal affected fishponds and enclosures [16] | Overtopping, damaged pond walls, escaped stock, lost boats, and destroyed gear erase both assets and income | Add pond-water level, embankment, cage, boat, net, and safe-harbor rules for coastal Odisha. |
| Seed, input, and infrastructure loss | Mocha damaged seed stocks and agricultural infrastructure [23]; post-Sidr and post-Odette programs supplied seeds and productive inputs [12][15] | A field may become plantable before replacement seed, tools, storage, roads, or credit are available | Pre-position protected seed and document local input stocks; post-event advice must include access and logistics, not only agronomy. |
| Multi-year perennial recovery | Michael's pecan estimate split current crop, destroyed trees, and a decade of future profits [34] | Tree replacement and return to full yield take multiple seasons | Forecast recovery cash flow and replacement timing; do not label a one-season payout as full recovery. |
| Secondary biological hazard | Exceptional cyclone rain can create pest-breeding conditions; FAO's locust response treated nearly 2.3M ha [1][13] | Ecological effects can emerge months later and far from landfall | Keep a seasonal pest-surveillance branch, but require evidence before linking a pest outbreak to a specific cyclone. |

These cases reveal a sequence rather than one damage type: forecast hazard -> farm exposure -> crop or asset damage -> access and input constraints -> household coping -> recovery. The practical recommendation is to issue actions by mechanism and farm context, not by cyclone category alone.

## 6. HOW IT FEEDS THE ENGINE: event history as validation data, pattern priors, and rule seeds.

The historical ledger should not be a lookup table that says, for example, "a category-4 storm causes X hectares of loss." It should become a versioned validation corpus with one row per `storm-country-assessment`, linked to canonical IBTrACS/IMD identifiers, local aliases, hazard components, farm exposure, crop stage, damage observations, farmer actions, source date, and grade. Rai/Odette and the two Damrey storms show why alias and collision controls are mandatory.

### Validation design

Use grades A and B as labeled outcomes, grade C only for sensitivity analysis, and grade D as a research backlog rather than a zero. Split model evaluation by whole storm, season, and geography so records from the same disaster cannot leak into training and test sets. Preserve preliminary and final assessments as separate revisions; otherwise, the model will learn from hindsight while being evaluated as if it were real time.

For operations, ingest IMD alert stage and expected landfall window, plus farm GPS, crop, variety, sowing date, growth stage, field elevation, drainage, soil moisture, irrigation, livestock, pond, stored seed, and contact preference. Hyperlocal gauges supply rainfall, wind, soil moisture, and water level. NASA IMERG supports half-hourly, daily, and monthly products; use Early/Late Run for low latency and Final Run for research-quality replay [50]. ECMWF archive tools can support historical forecast retrieval in GRIB or NetCDF [52].

### Rule seeds for Odisha SMS/IVR

| Trigger and farm context | Pre-disaster rule seed | Post-disaster rule seed | Historical validation target |
|---|---|---|---|
| High wind probability plus mature paddy | If authorities say conditions are safe and harvest is feasible, prioritize the mature field; dry and elevate harvested grain; secure pumps and loose equipment. | Record lodging and grain moisture; separate salvageable grain; request drying and storage support. | Wind-driven rice damage in Andhra 1996 and Yagi 2024 [25][26]. |
| Surge warning plus low-elevation coastal farm | Move people first; then livestock, feed, seed, documents, medicines, and portable equipment to the designated higher place. Protect freshwater. | Wait for official safe access; photograph losses; test water and soil salinity before irrigation or planting. | Sidr and Remal crop, livestock, grazing, and aquaculture impacts [8][16]. |
| Extreme rainfall plus saturated field | Clear safe drainage paths before conditions deteriorate; stop risky field work; identify a livestock route and elevated fodder store. | Drain only where it will not worsen downstream risk; scout erosion, contamination, root damage, and standing water. | Idai, Gombe, and Chido compound-flood records [36][5][48]. |
| Orchard or coconut holding plus destructive wind | Brace young plants where locally recommended; remove dangerous loose material; secure tools and irrigation components. | Triage uprooted, split, and recoverable trees; separate current crop loss from replanting and multi-year income needs. | Andhra coconut loss and Michael pecan loss [25][34]. |
| Fishpond, cage, boat, or net exposure | Check embankment and outlet only while safe; secure boats, nets, feed, and records; move portable gear from surge zones. | Inspect breaches, escaped stock, water quality, debris, and gear loss before restocking. | Yagi and Remal aquaculture damage [26][16]. |
| Recovery input shortage | Preserve undamaged seed and inventory; note local stocks and supplier contacts. | Match crop stage and planting window to verified seed, fertilizer, tools, veterinary, or fishing-gear support. | Sidr, Mocha, and Odette recovery packages [12][23][15]. |

For low-literacy users, each SMS or IVR turn should contain one prioritized action, a deadline, a location or asset, and a safety condition. Use Odia voice, keypad confirmation, missed-call callback, and escalation for "cannot comply." The system should log `received`, `understood`, `planned`, and `completed` separately. That converts the largest evidence gap in the ledger - farmer action - into new, consented validation data.

## 7. REAL-vs-FILLER + NOISE LOG.

| Candidate claim or record | Classification | Treatment |
|---|---|---|
| Rai and Odette as two Philippine cyclones in 2021 | Duplicate noise | One canonical event row, with both aliases. DA's assessment is cited once [15]. |
| Damrey 2005 and Damrey 2017 as one Vietnam event | Name-collision noise | Two separate rows. The 2005 FAO figures [14] are not assigned to the 2017 World Bank assessment [20]. |
| Remal's $596M as cyclone-only damage | Attribution filler | Rejected. The source explicitly covers Remal and later floods [16]. Stored as a compound sequence. |
| Gombe's 220,425 ha as cyclone-only loss | Attribution filler | Rejected. The source says loss since the start of the rainy season and calls for field validation [5]. |
| Gustav-plus-Ike $950M as an Ike-only total | Attribution filler | Rejected. Retained only as an inseparable combined estimate [49]. |
| Puerto Rico's 2012-2018 sales decline as Maria-only damage | Temporal filler | Rejected. Retained as longitudinal aftermath, because USDA describes harvest/infrastructure destruction but the census interval spans six years [21]. |
| Idai or Kenneth directly causing the 2019-2021 locust upsurge | Causal noise | Rejected. The retrieved evidence points to exceptional rain associated with Mekunu and Luban in the Arabian Peninsula [1]. |
| General disaster damage, insurance loss, or relief package as agricultural damage | Scope noise | Excluded unless the source identifies agriculture. Biparjoy's Rs240 crore is labeled relief, not crop loss [33]. |
| Wikipedia, Grokipedia, social posts, reposts, or snippets with no retrievable primary document | Discovery-only filler | Not used for an A/B damage figure. Such material may generate a source lead but cannot close a ledger field. |
| MISSING-DATA interpreted as zero | Statistical noise | Prohibited. Grade-D values remain unknown and must be masked during model training. |

The noise log is not cosmetic. Without it, duplicate names inflate event counts, compound estimates inflate cyclone losses, and absent data become false zeros. Each rejected transformation should be represented as a machine-readable quality flag.

## 8. VERDICT.

**Verdict: the requested "complete global ledger" does not exist in the named archives and cannot be honestly certified from open-web research.** IBTrACS is the best global storm-track backbone, but it has no agriculture-impact variables [11]. EM-DAT is broad but thresholded [10]. Dartmouth is a large-flood archive beginning in 1985 and excludes some tropical-storm cases [4]. Agriculture evidence resides in fragmented assessments with different definitions, currencies, spatial scopes, and publication lags.

This report is therefore a **usable, evidence-graded minimum ledger** for every event explicitly named in the brief, not the worldwide final word. Its A/B rows can seed validation and rules; C rows provide bounded context; D rows are an explicit acquisition queue. Any submission that silently replaces the D rows with unsourced numbers, labels compound values as cyclone-only, duplicates Rai/Odette, merges the two Damrey storms, or attributes the locust upsurge to Idai/Kenneth would look fuller but be less accurate.

### Synthesis: archive roles, evidence horizons, and trade-offs

| Dimension | Track archives | Disaster databases | Flood archives | Post-disaster agriculture assessments |
|---|---|---|---|---|
| Primary mechanism captured | Wind track, intensity, position, landfall | Disaster occurrence and aggregate human/economic effects | River and surface-flood event footprint | Crop, livestock, fisheries, forestry, infrastructure, and recovery |
| Geographic scope | Global tropical cyclones | Global thresholded disasters | Global large floods from 1985 | Selective countries and major events |
| Time horizon | Long historical storm record | 1900-present database scope | 1985-present | Days to years after selected events |
| Main strength | Canonical hazard chronology | Cross-disaster search and country totals | Flood-specific event inventory | Actionable agriculture detail and commodity mechanisms |
| Main trade-off | No farm loss or action field | Threshold and aggregation bias | Misses non-river and older cases | Inconsistent scope, revisions, and publication bias |
| Engine role | Event ID and hazard backbone | Candidate discovery and broad severity context | Flood-component validation | Outcome labels, pattern priors, and rule seeds |

The non-obvious conclusion is that completeness is not achieved by finding a bigger single archive. It requires a governed join across four evidence systems with explicit missingness and provenance. For the Odisha prototype, the best near-term decision is to deploy a conservative IMD-plus-hyperlocal advisory workflow, validate it against the A/B cases, and collect new farmer-action confirmations through SMS/IVR. For the global research program, publish versioned releases, not a timeless claim of completion.

## References

1. *FAO Knowledge Repository*. https://openknowledge.fao.org/bitstreams/bddf76de-cdbd-42c1-95eb-40dab145890d/download
2. [
	The Impact of Disasters on Agriculture and Food Security
](https://www.fao.org/publications/fao-flagship-publications/the-impact-of-disasters-on-agriculture-and-food-security/en)
3. *Global Active Archive of Large Flood Events (DFO) | Humanitarian Dataset | HDX*. https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo
4. *Dartmouth Flood Observatory*. https://floodobservatory.colorado.edu/Archives
5. *A rapid geospatial analysis of the impact of the Tropical Cyclone Gombe in Mozambique in 2022*. https://openknowledge.fao.org/items/4ca16338-d1dd-497b-9f73-32b83140d2a2
6. *Table of Contents*. https://www.fao.org/4/Y2784E/Y2784E00.htm
7. *Cyclone Sidr in Bangladesh | GFDRR*. https://www.gfdrr.org/en/publication/cyclone-sidr-bangladesh
8. *World Bank Document*. https://documents1.worldbank.org/curated/en/337501468014345112/pdf/PIDAppraisal0BD0Cyclone0May01902008.pdf
9. *Puerto Rico’s Agricultural Economy in the Aftermath of Hurricanes Irma and Maria: A Brief Overview | Economic Research Service*. https://www.ers.usda.gov/publications/106260
10. *EM-DAT - The international disaster database*. https://www.emdat.be/
11. *International Best Track Archive for Climate Stewardship (IBTrACS) | National Centers for Environmental Information (NCEI)*. https://www.ncei.noaa.gov/products/international-best-track-archive
12. *Bangladesh: Cyclone SIDR OCHA Situation Report No. 10 | OCHA*. https://www.unocha.org/publications/report/bangladesh/bangladesh-cyclone-sidr-ocha-situation-report-no-10
13. [
	Desert Locust crisis | FAO Emergency and Resilience | Food and Agriculture Organization of the United Nations
](https://www.fao.org/emergencies/where-we-work/desert-locust-crisis)
14. *FAO/GIEWS - Foodcrops and Shortages �-�10/05 - VIET NAM (12 October)*. https://www.fao.org/4/J6398e/pays/VIE.htm
15. [
    Odette-affected farmers and fisherfolk receive P3-billion worth of interventions from DA |
    Official Portal of the Department of Agriculture](https://www.da.gov.ph/odette-affected-farmers-and-fisherfolk-receive-p3-billion-worth-of-interventions-from-da)
16. *Bangladesh: Cyclone Remal and monsoon floods – Emergency appeal*. https://openknowledge.fao.org/server/api/core/bitstreams/18f904d3-0e63-47c4-844f-298263ee655a/content
17. *DA RFO 2, WFP AND FAO DISTRIBUTE AGRICULTURAL INPUTS TO TYPHOON MANGKHUT-STRICKEN FARMERS | Cagayan Valley Department of Agriculture Official Website*. https://cagayanvalley.da.gov.ph/2019/02/18/da-rfo-2-wfp-and-fao-distribute-agricultural-inputs-to-typhoon-mangkhut-stricken-farmers
18. *Fre Final Hurricane Ian Report*. https://fred.ifas.ufl.edu/media/fredifasufledu/economic-impact-analysis/reports/FRE-Final-Hurricane-Ian-Report.pdf
19. *FAO/GIEWS Special Alert Central America, 6 November 1998  *. https://www.fao.org/4/X0313E/X0313E00.htm
20. *World Bank Document*. https://documents1.worldbank.org/curated/en/244871603784378547/pdf/2017-Vietnam-Post-Typhoon-Damrey-Rapid-Damage-and-Needs-Assessment.pdf
21. *Puerto Rico’s Agricultural Economy in the Aftermath of Hurricanes Irma and Maria: A Brief Overview*. https://ers.usda.gov/sites/default/files/_laserfiche/publications/106261/AP-114_Summary.pdf?v=34487
22. *Microsoft Word - Document11*. https://fsi.nic.in/uploads/documents/assessment_of_damage.pdf
23. *Myanmar: Cyclone Mocha. Urgent call for assistance*. https://www.themimu.info/sites/themimu.info/files/documents/Urgent_Call_for_Assistance_on_Cyclone_Mocha_FAO_Jul2023.pdf
24. *Bangladesh Cyclone Remal Impact Assessment Report June 2024*. https://bangladesh.un.org/sites/default/files/2024-06/Bangladesh-Cyclone%20REMAL%20Impact%20Assessment%20Report_June_2024.pdf
25. *IFRC - INDIA CYCLONE (Preliminary Appeal 20/96) - Situation Report 01 (13/11/1996)*. https://www.ifrc.org/docs/appeals/96/209601.pdf
26. *VIET NAM MULTI-SECTOR ASSESSMENT (VMSA) REPORT*. https://www.undp.org/sites/g/files/zskgke326/files/2024-12/vmsa_final.pdf
27. *Hurricane Helene Impact Report - fieldreport.caes.uga.edu*. https://fieldreport.caes.uga.edu/wp-content/uploads/2025/08/AP-133-1_1.pdf
28. *Texas agricultural losses from Hurricane Harvey estimated at ...*. https://tscra.org/texas-agricultural-losses-from-hurricane-harvey-estimated-at-more-than-200m/
29. *令和元年東日本台風（台風第19号）等に係る被害情報：農林水産省*. https://www.maff.go.jp/j/saigai/typhoon/191011/index.html
30. *AgCenter experts: Louisiana agriculture suffers at least ...*. https://www.lsuagcenter.com/articles/page1632415649946
31. *Foundations for rebuilding seed systems post Cyclone Idai ...*. https://openknowledge.fao.org/handle/20.500.14283/CC6057EN
32. *HURRICANE MILTON Update from Emergency Management*. https://www.facebook.com/citruscountygov/posts/keeping-you-informed-hurricane-miltonupdate-from-emergency-management/937378768423703
33. *cyclone biparjoy: Relief package of Rs 240 crore for farmers ...*. https://economictimes.indiatimes.com/news/india/gujarat-govt-announces-rs-240-cr-relief-package-for-farmers-affected-by-cyclone-biparjoy-in-kutch-banaskantha/articleshow/101765879.cms
34. *Georgia farmers face more than $2 billion in losses from ...*. https://research.uga.edu/news/georgia-farmers-face-more-than-2-billion-in-losses-from-hurricane-michael/
35. *Georgia farmers face more than $2 billion in losses from ...*. https://fieldreport.caes.uga.edu/news/georgia-farmers-face-more-than-2-billion-in-losses-from-hurricane-michael/
36. *2018-2019 Mozambique Humanitarian Response Plan Revised ...*. https://www.unocha.org/publications/report/mozambique/2018-2019-mozambique-humanitarian-response-plan-revised-following-cyclones-idai
37. *Assessment of paddy fields’ damage caused by Cyclone Nargis ...*. https://link.springer.com/article/10.1007/s10333-020-00829-0
38. *MOZAMBIQUE Intense Tropical Cyclone Chido - cisu.dk*. https://cisu.dk/media/rmtnwifb/2024_dec_mozambique_tropical-cyclone-chido_final-merged.pdf
39. *農林水産省ホームページ 農林水産省 https://www.maff.go.jp*. https://www.maff.go.jp/
40. *Cyclone Batsirai - Wikipedia*. https://en.wikipedia.org/wiki/Cyclone_Batsirai
41. *Typhoon Jebi - Wikipedia*. https://en.wikipedia.org/wiki/Typhoon_Jebi
42. *Report finds $25B in insured losses from Milton in Florida*. https://www.wesh.com/article/insured-losses-from-hurricane-milton-florida/63396461
43. *1991 Bangladesh cyclone*. https://en.wikipedia.org/wiki/1991_Bangladesh_cyclone
44. *Cyclone Nargis Case Study*. https://www.coolgeography.co.uk/A-level/AQA/Year%2013/Weather%20and%20climate/Hurricanes/Cyclone_Nargis.htm
45. *Hurricane Milton caused up to $2.5B in Florida farm damage*. https://www.agriculturedive.com/news/hurricane-milton-florida-farm-damage-usda/730404
46. *Preliminary estimates of losses in Louisiana agriculture ...*. https://www.lsuagcenter.com/topics/family_home/hazards_and_threats/recovery_assistance/agdisaster/preliminary-estimates-of-losses-in-louisiana-agriculture-forestry-and-fisheries-from-hurricane-gusta
47. *Madagascar - Tropical Heavy Rains and Cyclone - IFRC GO*. https://go.ifrc.org/emergencies/5807/details
48. *Mozambique: Intense Tropical Cyclone Chido - Flash Update No ...*. https://www.unocha.org/publications/report/mozambique/mozambique-intense-tropical-cyclone-chido-flash-update-no-5-27-december-2024
49. *Ag Disaster: Loss & Recovery - LSU AgCenter*. https://www.lsuagcenter.com/topics/family_home/hazards_and_threats/recovery_assistance/agdisaster
50. *http://gpm.nasa.gov/data/imerg*. http://gpm.nasa.gov/data/imerg
51. *http://ecmwf.int/en/forecasts*. http://ecmwf.int/en/forecasts
52. *http://ecmwf.int/en/forecasts/access-forecasts/access-archive-datasets*. http://ecmwf.int/en/forecasts/access-forecasts/access-archive-datasets
53. *Damage from Cyclone Ditwah in Sri Lanka Estimated at ...*. https://www.worldbank.org/en/news/press-release/2025/12/22/damage-from-cyclone-ditwah-in-sri-lanka-estimated-at-4-1-billion
