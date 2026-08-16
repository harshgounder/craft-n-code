# Odisha Farmer Risk Data for a Working Prototype

## 1. EXECUTIVE SUMMARY

- **Smallholder reality**: Odisha had **4.866M operational holdings** operating **4.619M ha** in 2015-16, an average of **0.95 ha**. Marginal holdings numbered 3.637M and small holdings 0.887M, so these two classes represented a calculated **93.0% of holdings** and **74.9% of operated area**. The advisory engine should therefore default to low-cost, short-horizon actions suitable for farmers with little land and limited capacity to absorb a failed season, but it must not infer an individual farmer's land size from this aggregate [12].

- **Tenancy is visible but not operationally resolved**: Odisha had India's highest reported state share of wholly leased-in operational holdings, **5.82%**, in the Agriculture Census. BALARAM separately recognizes oral lessees, sharecroppers and landless or marginal cultivators, but these sources do not provide a current farmer-to-plot tenancy registry [5][24]. A prototype needs a "cultivator, owner, tenant or sharecropper" field and document workflow rather than assuming the landowner is the user.

- **SMS plus IVR is supported by the phone evidence**: The 2025 telecom survey reports that **84.0% of rural Odisha households** had a mobile phone: 53.0% smartphone-only, 19.8% both smartphone and non-smartphone, and 11.2% non-smartphone-only. Thus at least 72.8% had a smartphone, but household access is not the same as individual farmer access, literacy, control of the phone or network reachability [27]. Build SMS and IVR first, while retaining village-worker and shared-phone escalation for the implied 16.0% of households without a mobile.

- **Fani confirms who bears the agricultural burden**: The government-led Fani assessment reports that **90% of farmers** in the 14 assessed districts were small or marginal. Agriculture, fisheries and livestock recorded **Rs 3,032.70 crore** in damage and loss and **Rs 2,614.66 crore** in recovery needs; crops alone recorded Rs 363.54 crore in damage and Rs 1,304 crore in loss [28]. This supports crop, livestock and fisheries branches in the engine, not a crop-only design.

- **Dana supplies useful local patterns, not statewide rates**: A rapid assessment in four blocks of Kendrapara and Bhadrak covered 27 gram panchayats, 98 villages and 69,133 affected people. It reported crop loss over **5,428 acres**, including paddy, pulses and vegetables, with waterlogging and saltwater intrusion [26]. These observations can seed local rules, but the selected-area assessment cannot estimate the statewide probability of loss.

- **Debt raises the cost of bad advice**: AIDIS 2019 estimated that **40.5% of rural Odisha households** were indebted and average debt was **Rs 31,000 per household** as of June 30, 2018 [2]. Because AIDIS defines indebtedness as any outstanding cash loan and reports an all-household state estimate, it is a vulnerability prior, not an event-specific farmer score [2].

- **PMFBY rules are implementable, but public claim analytics are not**: The 2023 PMFBY guidelines define a **72-hour loss-intimation window**, evidence routes and a maximum two-week post-harvest cover for specified crops and perils [14]. A prototype can build reminders and a claim-packet checklist today. It cannot calculate a defensible Fani, Yaas or Dana district-crop claim rate without policy, notified-area, claim and payment denominators from insurers or the National Crop Insurance Portal.

- **The public money rail is internally inconsistent**: A July 2023 PIB annexure reports Odisha paid claims of Rs 240.59 crore, Rs 164.94 crore, Rs 207.91 crore and Rs 457.97 crore for 2018-19 through 2021-22 [6]. A second official annexure, stated as of November 30, 2023, reports Rs 1,170.50 crore, Rs 1,157.96 crore, Rs 572.44 crore and Rs 1,041.22 crore for the same years [10]. The prototype should display provenance and vintage, not silently merge the series.

**Decision:** The project is **PARTIAL**. A free prototype can deliver alert-triggered, crop-stage-aware advice, phone-channel routing and claim-document assistance. Live eligibility, adjudication, rejection and payment tracking remain partner-gated.

## 2. DATA INVENTORY

Reliability grades used here are: **A** = official primary source with defined scope; **B** = official but old, aggregate or operationally awkward; **C** = limited or nonrepresentative case evidence; **D** = no usable public dataset located for the requested detail.

| Data item | Named source with URL and date | Granularity | Freshness | Access path | Reliability grade A-D |
|---|---|---|---|---|---|
| Landholding count, area and size class | Agriculture Census 2015-16, All India Report; https://www.thehinducentre.com/the-arena/current-issues/article28682480.ece/binary/T1_ac_2015_16.pdf; reference year 2015-16 | State x five holding-size classes; counts in thousands and area in thousand ha | Old structural baseline | Free PDF/report | A |
| Average holding size | Same Agriculture Census report; 2015-16 | State x size class x sex; Odisha all-class average 0.95 ha [12] | Old | Free PDF/report | A |
| Tenancy | Final Agriculture Census 2015-16 report; https://agcensus.da.gov.in/document/agcen1516/ac_1516_report_final-220221.pdf; 2015-16 | State share of wholly leased-in holdings; Odisha 5.82% [5] | Old and narrower than all tenancy | Free PDF/report | B |
| Farmer age, education and household characteristics | NSS 77th Round Situation Assessment of Agricultural Households; https://mospi.gov.in/unit-level-data-report-nss-77-th-round-schedule-331-january-2019-%E2%80%93-december-2019land-and-livestock; survey January-December 2019, released September 10, 2021 [11] | Anonymized survey microdata and published estimates, not an operational farmer registry | Medium-old | Free unit records/report; analysis required | B |
| Farmer-specific literacy and preferred voice/language | No current farmer-linked Odisha public source located | Required at farmer/contact level | Missing | Field collection and consent | D |
| Basic phone versus smartphone | Comprehensive Modular Survey: Telecom 2025; https://mospi.gov.in/sites/default/files/publication_reports/CMST_report_m.pdf; January-March 2025 | Rural Odisha household device mix [27] | Current survey baseline | Free PDF/report | A for households; C for individual farmers |
| Rural indebtedness | AIDIS 2019, NSS Report 588; https://www.thehinducentre.com/resources/article36470537.ece/binary/Report%20no.%20588-AIDIS-77Rm-Sept.pdf; debt reference date June 30, 2018, released September 2021 | Rural/urban state household estimates | Old, not disaster-linked | Free PDF/report | A for stated measure; C for farmer targeting |
| Tenant and sharecropper credit design | BALARAM Operational Guidelines; https://slbcorissa.com/wp-content/uploads/2020/12/36-BALARAM_OG_FINAL.pdf; 2020 | State program design; Joint Liability Groups of 4-10 people [24] | Program design, not current achievement | Free PDF/report; bank/program partner for records | B |
| KCC coverage and loan sizes | BALARAM target of 100,000 JLGs covering 500,000 farmers and a group loan ceiling up to Rs 1.60 lakh [24] | Target and financing rule, not achieved Odisha KCC coverage | Not a current stock measure | Free guideline; actual accounts require bank/NABARD data | C |
| Fani agricultural impact | Government of Odisha-led Fani DLNA; https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_emp/documents/publication/wcms_732468.pdf; assessment May 24-June 4, 2019 | 14 districts, 15 sectors, sector and selected district findings [28] | Event-specific historical baseline | Free PDF/report | A |
| Dana agricultural impact | Youth for Social Development Rapid Needs Assessment; https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf; field visit October 24-28, 2024 | Four selected blocks in Kendrapara and Bhadrak | Recent but nonrepresentative | Free PDF/report | C |
| Dana probable exposure | Special Relief Commissioner bulletin; https://srcodisha.nic.in/newspapper/dHx1Ir7zInformation%20on%20Cyclonic%20Storm%20%E2%80%9CDANA%E2%80%9D.pdf; October 23, 2024 | 14 districts identified before impact [19] | Event-current forecast, not final impact | Free PDF/bulletin | A for preparedness; D for realized loss |
| Yaas farmer and crop impact | Searches located an official page titled "Farmers affected by Cyclone Yaas," but its available content did not expose Odisha figures [16] | No usable district-crop table extracted | Missing for this use | Further government request, RTI or source recovery | D |
| Historical flood occurrence | Odisha Department of Water Resources, Major Flood Occurrence; https://dowr.odisha.gov.in/sites/default/files/2022-03/Major%20flood%20occurence.pdf; file posted 2022 | Event, river basin, districts and historical damaged area; static document | Historical, not a live feed | Free PDF/file; parsing required | B |
| PMFBY covered perils and claim workflow | PMFBY Operational Guidelines 2023; https://agriwelfare.gov.in/Documents/operational_guidelines_pmfby_2023.pdf; effective from Kharif 2023 | National rules applied to notified crops and insurance units | Current rule baseline | Free PDF/report | A |
| PMFBY Odisha premium and paid claims | PIB Annexure I; https://pib.gov.in/Pressreleaseshare.aspx?PRID=1941399; July 21, 2023 | State x year, gross premium and paid claims [6] | Reporting vintage makes 2022-23 immature | Free HTML/report | B |
| Second PMFBY paid-claims series | PIB annexure; https://static.pib.gov.in/WriteReadData/specificdocs/documents/2023/dec/doc20231215288601.pdf; as of November 30, 2023 | State x year, paid claims only [10] | Newer vintage but unreconciled definition | Free PDF/report | B |
| District-crop-event claims, delays and rejection reasons | PMFBY state dashboard; https://pmfby.gov.in/adminStatistics/stateWiseReport; last-updated marker August 13, 2026, but the public page exposed filters rather than reusable Odisha rows [22][23] | Requested level not obtained | Operational data may exist behind portal | Insurer, NCIP, state and bank partner; possible RTI | D for public prototype access |

### PMFBY money rail: two official series that do not reconcile

| Insurance year | July 2023 release: gross premium, Rs crore | July 2023 release: paid claims, Rs crore | November 2023 release: paid claims, Rs crore |
|---|---:|---:|---:|
| 2016-17 | 0.50 | 0.99 [6] | Not included |
| 2017-18 | 166.78 | 157.39 [6] | Not included |
| 2018-19 | 171.82 | 240.59 [6] | 1,170.50 [10] |
| 2019-20 | 428.49 | 164.94 [6] | 1,157.96 [10] |
| 2020-21 | 605.09 | 207.91 [6] | 572.44 [10] |
| 2021-22 | 558.79 | 457.97 [6] | 1,041.22 [10] |
| 2022-23 | 520.77 | 0.00 [6] | 497.10 [10] |

These are reporting aggregates, not farmer claim rates. A valid claim rate needs at least enrolled or affected-policy counts as a denominator, while an event loss ratio additionally needs event attribution, sum insured and assessed loss. Neither annexure supplies those fields.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing elements | Coverage judgment A-D |
|---|---|---|---|
| Agriculture Census | Exact Odisha holding counts, operated area, average size and a narrow tenancy measure [12][5] | Reference year 2015-16; no live farmer ID, crop stage, plot geometry or complete informal tenancy | A for population structure; C for targeting |
| NSS Situation Assessment and AIDIS | Agricultural-household microdata exists; rural Odisha indebtedness and debt amount are available [11][2] | Survey re-analysis needed for age/education; anonymous samples cannot drive individual messages; debt is not cyclone-linked | B |
| Telecom household survey | Recent rural Odisha device mix supports SMS/IVR channel design [27] | No farmer-only sample, ownership/control, literacy, preferred language, shared-phone status or signal quality | B |
| Government disaster assessments | Fani supplies high-quality sector losses, recovery needs and affected-farmer structure [28] | No harmonized Fani-Yaas-Dana district-crop panel and no insurance linkage | A for Fani; D for cross-event comparability |
| NGO rapid assessments | Dana provides current village/block observations on crops, salinity, livelihoods and migration [26] | Purposive four-block scope; not a statewide estimator | C |
| PMFBY guidelines | Exact perils, notice clock, evidence routes, claim assessment and exclusions [14] | Rules still depend on notified crop, insurance unit, enrolment and insurer records | A |
| PMFBY public financial releases | State-year premium and claims money [6] | Official series conflict; no district, crop, policy, event, rejection or timing record | C for analytics |
| PMFBY dashboard | State/season/year/scheme filter structure and current update marker [22][23] | No stable public Odisha export or documented free API was recovered | C as a viewing surface; D as an engine feed |
| BALARAM and KCC material | Explicit treatment of oral lessees/sharecroppers, field verification and financing design [24] | Targets are not achieved coverage; account-level KCC status and balance remain bank-held | B for workflow; D for current coverage |
| General web and news | Helped discover documents and a localized Yaas farmer case | Repeated national figures, untraceable summaries, duplicated press copy and pages without annexure data | D |

The strongest coverage is for **static structure, formal rules and one major event assessment**. The weakest coverage is exactly where a production engine needs live joins: farmer, plot, crop stage, insurance policy, loss notice, adjudication and payment.

## 4. WHAT IS MISSING

No reviewed public source provides the following fields as a joined, reusable Odisha dataset:

1. **Farmer-plot-crop-stage key**: consented farmer ID, plot ID, GPS polygon, crop, variety, sowing/transplant date and current growth stage.
2. **Verified cultivator status**: owner, tenant, oral lessee, sharecropper or landless cultivator linked to the plot. The Agriculture Census measures populations, while BALARAM's Certificate of Cultivation requires field verification [24].
3. **Farmer communication profile**: preferred language or dialect, literacy, IVR consent, basic versus smartphone, shared-phone status, preferred calling time and last successful delivery. The available 84.0% figure is household-level [27].
4. **Live crop exposure snapshot**: district-block-gram-panchayat crop area by growth stage immediately before each alert.
5. **Event-tagged PMFBY claim ledger**: a record linking Fani, Yaas, Dana or a named flood to policy, farmer, plot, notified crop, insurance unit and insurer.
6. **Claim-rate denominator**: enrolled policies, affected insured policies, sum insured, notified area and assessed loss. State-year paid rupees alone cannot produce a farmer claim rate [6].
7. **Rejection and document-deficiency codes**: late intimation, crop not notified, area not covered, premium not received, duplicate policy, insufficient evidence or another adjudication reason. Public material lists broad complaint categories, not Odisha counts by reason [6].
8. **Claim timestamps and payment trace**: peril time, first intimation, acknowledgement, survey appointment, survey completion, approval, bank credit, UTR and delay owner. The guideline supplies a process clock but not completed-case records [14].
9. **Harmonized Fani-Yaas-Dana impact panel**: district x block x crop x area x affected farmers x damage x recovery time under common definitions.
10. **Disaster-linked debt, suicide and migration panel**: household outcomes before and after an event. AIDIS is a general state household survey, while Dana supplies only localized qualitative migration evidence [2][26].
11. **Advice-effectiveness outcomes**: whether a farmer received, understood and acted on advice, what it cost, and how much crop or livestock loss it avoided.

These are not minor enrichment fields. They are the joins required to convert a district warning into a defensible individual recommendation and to demonstrate that the recommendation helped.

## 5. HOW IT FEEDS THE ENGINE

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| Holding-size class | Rank low-cost actions; avoid equipment-heavy defaults | Estimate feasible input and labor needs | Record cultivated area, but request farmer proof | Recommend diversification within land constraint | Small-plot scheduling, input pooling and shared equipment |
| Tenure/cultivator status | Route advice to the actual cultivator | Identify eligibility-document risk early | Ask for lease, Certificate of Cultivation or local verification | Encourage advance documentation before enrolment | Explain tenant credit and scheme routes |
| Age, education and literacy | Select message length, vocabulary and IVR pace | Use stepwise voice instructions | Voice-guided checklist | Training format and frequency | Routine crop and financial-literacy prompts |
| Phone/device profile | SMS for any mobile; IVR fallback; app features only when appropriate | Retry channel and village-worker escalation | Capture text acknowledgement and guided evidence upload | Maintain preferred channel | Weather, market and husbandry reminders outside disasters |
| Crop, variety and growth stage | Select harvest, drainage, staking, input protection or evacuation action | Select re-sowing, salinity, pest, carcass or feed advice | Prove crop and stage at time of peril | Shift calendar or variety using repeated local outcomes | Stage-specific irrigation and nutrient advice |
| Plot GPS and hazard layer | Geofence alert and prioritize river, coast or surge exposure | Direct field inspection and local recovery services | Timestamp and geotag evidence | Identify repeatedly exposed plots | Drainage, bund and shelter planning |
| AIDIS debt prior | Prefer actions with low cash requirement | Avoid advice that assumes immediate credit | Offer bank/insurance escalation rather than new debt by default | Debt-sensitive crop and input planning | KCC and repayment education with explicit consent |
| BALARAM/JLG workflow | Identify tenant farmers needing documentation support | Connect groups to formal credit rather than informal distress borrowing | Store Certificate of Cultivation and consent | Form or renew groups before monsoon | Shared borrowing, equipment and input purchase guidance |
| Fani DLNA patterns | Include livestock, poultry, fisheries, coconut and horticulture branches, not only paddy | Prioritize feed, shelter, animal health, boats/nets and livelihood restart | Expand evidence checklist beyond field-crop photographs | Build-back-better investments by livelihood | Multi-livelihood preparedness drills |
| Dana rapid assessment | Trigger paddy/pulse/vegetable, waterlogging and coastal-salinity playbooks | Test soil/water, drain standing water and sequence recovery support | Photograph standing crop, water line and salinity indicators | Salt-tolerant options and drainage planning where locally validated | Household preparedness where working-age men migrate |
| PMFBY rules | Tell insured farmers which notified covers may apply | Start the 72-hour clock and route intimation [14] | Generate a dated bundle of policy, crop, plot, photo and notice records | Check crop notification before sowing/enrolment | Insurance-literacy reminders before the peril |
| Claim-status partner feed | Confirm enrolment and avoid false assurance | Show survey and approval stage | Detect missing records and escalate delay | Compare insurer outcomes by crop/area | Renewal decision based on verified experience |
| Advice outcome log | Learn which actions are completed before landfall | Measure recovery time and unmet needs | Preserve an audit trail | Calibrate future recommendations | Stop sending advice that farmers cannot use |

The engine should use aggregate datasets as **priors and rule-selection inputs**, never as substitutes for farmer-provided or partner-verified facts. For example, the fact that 93.0% of holdings are small or marginal supports a low-cost default, but it does not prove that a particular caller owns less than 2 ha.

## 6. REAL-vs-FILLER

| Genuinely usable now | Decorative, misleading or unsafe if presented as operational |
|---|---|
| Exact Agriculture Census counts and areas for population priors [12] | Calling a 2015-16 state average a current farmer profile |
| Rural Odisha phone-type distribution for channel design [27] | Treating household possession as individual farmer ownership, literacy or network reach |
| PMFBY's 72-hour notice rule, allowed channels and evidence checklist [14] | A generic "insurance help" page with no notified-crop check, timer or document trail |
| Fani's measured crop, livestock and fisheries effects [28] | A single generic cyclone message for all agricultural livelihoods |
| Dana's localized evidence on paddy, pulses, vegetables, waterlogging and salinity [26] | Presenting four selected blocks as an Odisha-wide incidence rate |
| AIDIS debt estimate as a state vulnerability prior [2] | Labelling an individual farmer "indebted" from a state percentage |
| Both official PMFBY series displayed separately with date and provenance [6][10] | Combining contradictory values into a false trend or calling paid rupees a claim rate |
| SRC Dana's 14 probable districts for pre-event routing [19] | Calling all 14 districts realized agricultural-loss districts |
| BALARAM's cultivator verification and JLG workflow [24] | Reporting the target of 500,000 farmers as achieved KCC coverage |

### Case study: Fani shows why crop-only advice is inadequate

Fani's assessment places small and marginal farmers at the center of exposure: 90% of farmers in the assessed districts fell into those classes [28]. Yet the loss was not confined to standing crops. The assessment counted about 24.5 lakh large animals, 10 lakh small animals and 54 lakh poultry affected; it also recorded deaths of cattle, small ruminants and approximately 53 lakh chickens [28].

The mechanism is livelihood coupling. One household may depend on a small plot, poultry, dairy work or fisheries at the same time, so a paddy-only alert can protect one asset while leaving another exposed. The engine should therefore ask a short livelihood checklist and generate parallel actions: harvest or drain where appropriate, move feed and medicines, secure animals, preserve boat or net information, and photograph each insured asset class.

### Case study: Dana is actionable local evidence, not a denominator

The Dana rapid assessment documented 5,428 acres of crop loss in four selected blocks and described impacts on paddy, pulses and vegetables, along with saltwater intrusion [26]. It also reported that many men in Talachua and Satabhaya worked outside Odisha, leaving women and children especially vulnerable during the storm [26].

This supports locally tested modules for salinity, waterlogging, household role assignment and IVR delivery. It does not support a statewide statement such as "X percent of Dana farmers lost crops," because the four blocks were selected as heavily affected rather than sampled to represent Odisha [26]. That distinction separates evidence from filler.

## 7. NOISE LOG

| Search or candidate source | Disposition | Reason |
|---|---|---|
| NFHS-5 DHS Odisha report page | Discarded for numeric use | The fetched page was a maintenance notice, not the Odisha tables [7]. NFHS indicators also concern general populations rather than a live farmer contact registry. |
| National KCC press releases | Discarded as Odisha coverage evidence | They report more than 7.72 crore operational KCCs nationally, not current Odisha district or farmer coverage [17]. |
| Odisha RuPay KCC parliamentary-answer wrapper | Retained only as a lead | It states that a district-wise Odisha annexure exists, but the available excerpt does not contain the annexure values [25]. |
| PMFBY state-wise web dashboard | Retained as a partner/discovery lead, not an API | The accessible page exposed State, Season, Year and Scheme filters but no reusable Odisha records [22]. |
| PMFBY paid-claims releases | Retained with warning | Both are official, but their overlapping Odisha values do not reconcile [6][10]. |
| Cyclone Yaas official search result | Discarded for quantitative claims | The available source exposed only the title "Farmers affected by Cyclone Yaas," not Odisha district, crop or claim values [16]. |
| Dana SRC bulletin | Retained only for pre-event routing | Its 14 districts were "probable affected districts," and the bulletin said agriculture losses would be assessed later [19]. |
| Dana rapid assessment | Retained as a case study | Useful field observations, but selected blocks prevent statewide generalization [26]. |
| All-India farmer-suicide totals | Discarded from Odisha findings | National totals do not establish Odisha cyclone/flood-linked suicide patterns or causation. |
| General articles on migration, debt and cyclone vulnerability | Discarded unless traceable to a defined Odisha sample | Narrative relevance without sample, date, denominator and method cannot calibrate the engine. |
| Basic-versus-smartphone commentary sites | Discarded | The official 2025 telecom survey provides the stronger household benchmark [27]. |

The main noise pattern was **scope substitution**: national numbers offered as Odisha numbers, household measures offered as farmer measures, pre-event exposure offered as realized loss, and state-year insurance rupees offered as event-specific claim rates.

## 8. VERDICT

# Grade: PARTIAL

### What can be built today using free data

1. **A static risk and accessibility layer** using holding-size priors, rural phone mix, historical district exposure and Fani/Dana livelihood patterns.
2. **An alert-to-advice rules engine** that joins an incoming district or geospatial warning to farmer-supplied crop, stage, plot and livelihood fields.
3. **SMS and IVR workflows** with short, low-cost actions suitable for a predominantly smallholder population and a material non-smartphone segment.
4. **A PMFBY claim assistant** that checks whether the user says they are insured, starts the 72-hour timer, captures dated/geotagged evidence and identifies the correct notice channel [14].
5. **A recovery checklist** for crops, livestock, poultry and fisheries, informed by Fani's cross-sector effects and Dana's salinity and waterlogging observations [28][26].

### What the prototype must collect

Collect, with explicit consent: farmer/contact ID; preferred language; literacy and IVR preference; phone type and shared-phone status; village and plot GPS; cultivator/tenure type; crop, variety, area and growth stage; livestock/fisheries assets; insurance status and policy image; KCC/JLG status; alert receipt; action taken; pre/post-event photos; loss notice acknowledgement; and recovery outcome. Do not require debt amount for the minimum viable service unless there is a clear benefit and security design.

### What needs a partner

An insurer, state agriculture department, bank and/or NCIP integration is required for authoritative enrolment, notified crop and insurance unit, premium receipt, sum insured, claim number, survey, rejection code, settlement and bank-credit status. The guidelines explicitly make premium receipt and timely portal data material to eligibility [14], so the advisory system must not promise coverage based only on a farmer saying that a crop loan was sanctioned.

**Final decision:** Proceed with a free prototype, but describe it as an **advisory and claim-packet assistant**, not a claim-decision or payment system. Demonstrate three separate boundaries in the interface: "public rule," "farmer-provided fact" and "partner-verified status." That boundary is the difference between a useful prototype and a misleading insurance front end.

## SYNTHESIS

| Layer | Mechanism | Scope | Evidence base | Main trade-off | Time horizon |
|---|---|---|---|---|---|
| Census and NSS baseline | Supplies population priors and vulnerability segments | State and survey population | Official, method-defined but dated | Broadly reliable; weak for individual targeting | Structural, multi-year |
| Telecom baseline | Selects SMS, IVR and optional app channels | Rural households | Recent official survey | Current device mix; no proof of farmer access or literacy | Annual to multi-year |
| Fani DLNA | Quantifies cross-sector damage, loss and recovery need | 14 assessed districts and 15 sectors | Government-led post-disaster assessment | Deep event evidence; one event does not set all future rules | Event and recovery |
| Dana rapid assessment | Reveals localized salinity, crop and household patterns | Four selected blocks | Direct field case evidence | Recent and actionable; not representative | Event and immediate recovery |
| PMFBY guideline layer | Converts policy text into timers, questions and evidence tasks | Notified crops, areas and insured farmers | Official operational rules | Highly actionable; cannot confirm individual eligibility | Hours to weeks |
| Public PMFBY money series | Shows aggregate premium and paid-claim flows | State x year | Official releases with conflicting values | Useful for governance questions; unsafe for farmer-level rates | Annual, lagged |
| Collected farm profile | Converts a regional warning into crop-stage action | Individual farmer, plot and livelihood | Farmer-entered plus field verification | High relevance; consent, quality and maintenance burden | Live and seasonal |
| Partner claim ledger | Confirms eligibility, adjudication and payment | Individual policy and claim | Insurer, NCIP, bank and state systems | Authoritative; access and integration are gated | Near-real-time claim cycle |

The non-obvious tension is that the most authoritative public sources are least individualized, while the most individualized facts are either farmer-supplied or partner-held. The correct architecture is therefore not one giant "AI dataset." It is a provenance-aware stack: public hazard and policy rules, static population priors, a consented farm profile, an event evidence packet and a separately authenticated insurance feed.

A second tension concerns freshness versus representativeness. Fani offers a broad, government-led assessment but is historical; Dana is recent but localized. The engine should use Fani to define the breadth of livelihood modules and Dana to test local salinity, migration and communication scenarios, while collecting its own outcome data rather than pretending either event predicts every village.

Finally, insurance assistance has a different standard from agronomic advice. An agronomic recommendation can be presented as a risk-reduction action with uncertainty. A claim message can affect a farmer's legal and financial position, so it must preserve the 72-hour clock, source version, policy prerequisites and acknowledgement trail. The highest-value first release is consequently a **low-literacy action and evidence assistant**, with adjudication explicitly outside scope until partner data is available.

## References

1. *NFHS-5: National Family Health Survey (2019-20)*. https://github.com/pratapvardhan/NFHS-5
2. *अखिल भारत ऋण और खिवेश सवेक्षण - 2019 All India Debt & ...*. https://www.thehinducentre.com/resources/article36470537.ece/binary/Report%20no.%20588-AIDIS-77Rm-Sept.pdf
3. *Agriculture Census 2015-16*. https://www.fao.org/fileadmin/templates/ess/ess_test_folder/World_Census_Agriculture/WCA_2020/WCA_2020_new_doc/IND_REP_ENG_2015_2016.pdf
4. *Cyclone Fani 2019 DLNA Report - Odisha State Disaster ...*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
5. *All India Report on Agriculture Census 2015-16*. https://agcensus.da.gov.in/document/agcen1516/ac_1516_report_final-220221.pdf
6. *Premium Collection and Insurance Claims under Pradhan Mantri ...*. https://pib.gov.in/Pressreleaseshare.aspx?PRID=1941399
7. *Fr374 Odisha*. https://dhsprogram.com/pubs/pdf/FR374/FR374_Odisha.pdf
8. *State/UT- wise Details of Claims pending under Pradhan Mantri Fasal Bima Yojana (PMFBY) and Restructured Weather Based Crop Insurance Scheme (RWBCIS) as on 30-06-2024 | Open Government Data (OGD) Platform India*. https://www.data.gov.in/resource/stateut-wise-details-claims-pending-under-pradhan-mantri-fasal-bima-yojana-pmfby-and
9. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
10. *Annexure State-wise and year-wise details of claims paid to farmers during last 5 years i.e. 2018-19 to 2022-23 under PMFBY*. https://static.pib.gov.in/WriteReadData/specificdocs/documents/2023/dec/doc20231215288601.pdf
11. *Situation Assessment of Agricultural Households and Land and Livestock Holdings of Households in Rural India: NSS 77th Round (January-December 2019)*. https://ruralindiaonline.org/en/library/resource/situation-assessment-of-agricultural-households-and-land-and-livestock-holdings-of-households-in-rural-india/
12. *Agriculture Census 2015-16*. https://www.thehinducentre.com/the-arena/current-issues/article28682480.ece/binary/T1_ac_2015_16.pdf
13. [[file] Cyclone Fani 2019 Odisha India Damage Loss and Needs Assessment.pdf (74593)](https://recovery.preventionweb.net/media/74593/download)
14. *Microsoft Word - Final PMFBY Operational Guidelines 2023--120125*. https://agriwelfare.gov.in/Documents/operational_guidelines_pmfby_2023.pdf
15. *Press Release Page | Press Information Bureau*. https://pib.gov.in/PressReleasePage.aspx?PRID=2106230
16. *Farmers affected by Cyclone Yaas PIB https://www.pib.gov.in › PressReleasePage*. https://www.pib.gov.in/PressReleasePage.aspx?PRID=1742311
17. *Kisan Credit Card: Fueling Growth in Agriculture*. https://www.pib.gov.in/PressReleasePage.aspx?PRID=2238004&lang=1&reg=3
18. *Results of Comprehensive Modular Survey: Telecom, 2025*. https://pib.gov.in/PressReleasePage.aspx?PRID=2132330
19. *Dhx1Ir7Zinformation On Cyclonic Storm “Dana”*. https://srcodisha.nic.in/newspapper/dHx1Ir7zInformation%20on%20Cyclonic%20Storm%20%E2%80%9CDANA%E2%80%9D.pdf
20. *Access to phones and the internet | Data For India*. https://www.dataforindia.com/comm-tech
21. *BALARAM | Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/en/schemes-agriculture/agriculture/BALARAM
22. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://pmfby.gov.in/adminStatistics/stateWiseReport
23. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://pmfby.gov.in/adminStatistics/stateWise
24. *36 Balaram Og Final*. https://slbcorissa.com/wp-content/uploads/2020/12/36-BALARAM_OG_FINAL.pdf
25. *RuPay Kisan Credit Cards in Cooperative Sector in Odisha*. https://sansad.in/getFile/annex/270/AU2890_QH6EXi.pdf?source=pqars
26. *Cyclone Dana Assessment Report*. https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf
27. *व्यापक मॉड्यूलर सवेक्षण: टेलीकॉम, 2025 Comprehensive Modular Survey: Telecom, 2025 ( )*. https://mospi.gov.in/sites/default/files/publication_reports/CMST_report_m.pdf
28. *untitled*. https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_emp/documents/publication/wcms_732468.pdf
