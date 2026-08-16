# KrishiSetu's Evidence-Based White Space in Odisha

## 1. EXECUTIVE SUMMARY

- **Strong public foundation, weak integration**: IMD already produces five-day district/block forecasts, while expert AMFU/DAMU panels combine weather, crop stage, irrigation, stress, and pest information into crop-specific advice. Odisha and ICAR also publish contingency rulebooks. KrishiSetu should reuse these sources rather than invent agronomy, but it must build the missing event-to-farm-profile decision layer. [33]

- **The Tuesday/Friday gap is real but nuanced**: Routine GKMS advisories are prepared twice weekly, with forecast delivery, panel review, bulletin production, and SMS preparation scheduled on Tuesday and Friday. IMD also supports severe-weather advice, but the public documentation does not evidence a continuously running, individual-farm trigger that turns each cyclone or flood update into a deadline-bearing action. [33]

- **Feature-phone delivery infrastructure already exists**: Kisan Call Centre answers through local-language agricultural graduates, escalates unresolved questions to subject experts, supports **22 local languages**, and operates **06:00-22:00 every day**. mKisan supports text, voice, USSD, push, and pull services without requiring mobile internet. KrishiSetu should treat these as delivery and escalation precedents, not as sources of live farmer records. [36][31]

- **Published scale figures need careful interpretation**: mKisan's live About page shows an undated cumulative **327 crore messages / 1,044 crore SMSs** and cites potential reach to **8.93 crore farm families** using May 2014 telecom context. It does not publish a dated count of actually enrolled farmers. KCC has a daily open-data resource covering years 2006-2025, updated August 15, 2026, from which volume can be computed, but the reviewed official pages do not state a current headline call total. [31][30]

- **Odisha has useful rules, not a ready rules API**: The state publishes a **Crop Contingency Plan 2025**, and ICAR-CRIDA hosts district plans such as Ganjam with agro-climate, soil, irrigation, field-crop, horticulture, livestock, and fisheries context. These are free documents, but they require extraction, versioning, expert review, and conversion into machine-executable rules. [2][28]

- **Ama Krushi is the closest Odisha delivery prior art**: It demonstrates that free, two-way, localized voice advice can operate at state scale. Its published evaluation reports a **10% reduction in severe crop-loss probability** and a **9% harvest increase in excess-rainfall-affected areas**. This validates IVR and localized behavioral design, but its public page does not expose an advisory API, farm-profile export, or insurance-claim workflow. [14]

- **Private products solve valuable slices, not the complete disaster loop**: DeHaat combines photos, satellite signals, crop calendars, expert advice, commerce, and insurance access; Fasal is strongest in paid sensor-driven irrigation and fertigation; Gramophone combines stage-oriented advice, weather, experts, and commerce; BharatAgri is advisory-led input commerce; Aquaconnect specializes in pond intelligence, inputs, markets, and credit. Current public list pricing is absent for most, and none publicly evidences the full event-triggered + stage-aware + Odia + offline SMS/IVR + claim-packet combination. [25][23][7][3][22]

- **Verdict: PARTIAL**: A no-license-cost data prototype can ingest public IMD/CWC pages, convert Odisha contingency PDFs into reviewed rules, use KCC open data for question mining, and implement PMFBY checklists. A live farmer pilot still needs direct profile collection, telecom/IVR delivery, Odia content validation, stable alert feeds, and institutional partners. Claim filing and adjudication remain gated by insurers and government systems. [30][33][24]

## 2. DATA INVENTORY

**Reliability grading:** **A** = current primary government source or governed open data; **B** = primary/official but static, stale, document-shaped, or operationally incomplete; **C** = commercial self-description, implementation-partner evidence, or limited study; **D** = promotional, unverifiable, or discarded.

| Data item / sub-question | Named source, URL, and date | Granularity | Freshness | Access path | Grade |
|---|---|---|---|---|---|
| Meghdoot/GKMS generation | IMD, *Standard Operating Procedure for Agromet Advisory Services*, publication number dated 2020. https://mausam.imd.gov.in/imd_latest/contents/pdf/gkms_sop.pdf | District/block, crop, crop stage, five-day forecast, stress and pest context | Method is 2020; still corroborated by the February 4, 2026 parliamentary answer | Free PDF and public bulletins; no public API specified | A- [33]
| Meghdoot cadence and content quality | Same SOP: RMC/MC forecast by 12:00, panel by 12:30, operational bulletin and SMS by 15:00 on Tuesday/Friday; includes five previous observed days, next five forecast days, crop advice, and succeeding-week rainfall outlook | Twice-weekly operational cycle | Current operating model corroborated in 2026 | Free document; app/web/SMS dissemination | A- [33]
| Severe-weather advisory input | IMD cyclone page and GKMS SOP: heat, cold, hail, excess rainfall and dry-spell support; cyclone page provides outlooks, national/hourly bulletins, tracks, wind and storm-surge warnings | National, state, district/subdivision, cyclone track | Live pages | Free web pages/files; stable public API not documented | A-/B+ [16][33]
| Flood forecast input | Central Water Commission Flood Forecast portal, live page. https://ffs.india-water.gov.in/ | Forecast station/basin and seven-day advisory display | Live | Free web portal; API terms not established in reviewed material | A-/B+
| Kisan Call Centre operation | DAC KCC About page and MANAGE, live pages. https://www.dackkms.gov.in/account/aboutus.aspx and https://www.manage.gov.in/kcc/kcc.asp | Farmer question, local language, sector; Level I and expert escalation | Current page; no publication date | Toll-free telephone, **1800-180-1551** | A- [36]
| KCC hours, languages, answering model | Farm Tele Advisors are agriculture/allied graduates; unresolved calls go to State Agriculture, ICAR, KVK or SAU subject experts; **22 languages**, **06:00-22:00**, seven days | Call and subject level | Current operating page | Free call from mobile/landline; callback timing not documented | A- [36]
| KCC volume and reusable queries | OGD India, *KCC Transcripts of Farmers Queries and Answers*, published July 12, 2024; updated August 15, 2026. https://www.data.gov.in/resource/kisan-call-centre-kcc-transcripts-farmers-queries-answers | Daily; state, district, block, season and sector; years 2006-2025 selectable | Very current metadata; underlying years through 2025 | Free API/download under Government Open Data License - India | A [30]
| mKisan targeting and delivery | mKisan About and Farmer Registration pages, live; portal inaugurated July 16, 2013. https://mkisan.gov.in/Home/About and https://mkisan.gov.in/Home/FarmerRegistration | Mobile, name, state, district, subdistrict, block, village, age, gender, education, holding, language, mode, sector, category and crop | Live schema; program context partly anchored to May 2014 | Public registration; SMS, voice, USSD, push and pull; no public profile export/API documented | A-/B+ [31][29]
| mKisan registration base and traffic | Same About page: potential reach to **8.93 crore farm families** and undated cumulative **327 crore messages / 1,044 crore SMSs** | National aggregate | As-of date missing; not a registered-base count | Public report page only | B-/C+ [31]
| ICAR district contingency plans | ICAR-CRIDA Odisha directory and Ganjam Agricultural Contingency Plan, filename dated May 31, 2011. https://www.icar-crida.res.in/CP-2012/ and https://www.icar-crida.res.in/CP/Orissa/OUAT%2C%20Bhubaneswar/Orissa%2014-%20Ganjam%2031.05.2011.pdf | District, agro-climate, soil, land use, irrigation, crops, livestock, fisheries and hazard response | District files can be old; Ganjam is 2011 | Free PDFs | B [28]
| Odisha statewide contingency rules | Odisha Department of Agriculture and Farmers' Empowerment, *Crop Contingency Plan 2025*. https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf | State crop and hazard contingency actions | 2025 | Free 214K-character PDF; no API | A-/B+ [2]
| Ama Krushi | Precision Development, *Ama Krushi - Scaling advisory services to millions of farmers in Odisha*, live page retrieved August 16, 2026. https://precisiondev.org/project/ama-krushi | Registered-farmer voice advice, inbound questions, outbound localized advice and crop-level content | Current page, but not all metrics have as-of dates | Free farmer service; content/profile API not public | B+/C+ [14]
| KALIA context | Samagra, *Transforming Farmer Welfare in Odisha: The KALIA Story*, May 12, 2025. https://samagragovernance.in/blog/2025-05-12-transforming-farmer-welfare-in-odisha-the-kalia-story | Beneficiary and welfare-delivery context, not agronomic events | 2025 retrospective | Public case study; beneficiary database requires government partnership | B-/C+ [27]
| DeHaat | DeHaat Kisan Google Play listing, updated July 15, 2026. https://play.google.com/store/apps/details?id=app.intspvt.com.farmer | Individual photos/questions, farm satellite data, weather, crop calendar, expert response, inputs and insurance access | Current | Free app/advisory; commerce and insurance products priced separately; no general public price sheet | B+/C+ [25]
| Fasal | Fasal official product site, retrieved August 16, 2026. https://www.fasal.co/ | Farm sensor, soil moisture/temperature, weather station, disease/pest prediction, irrigation/fertigation | Live, undated | Hardware/service purchase; quote required | B-/C+ [23]
| BharatAgri | BharatAgri official site, content dated October-November 2024. https://bharatagri.com/ | Crop, pest/disease, app expert, input product and delivery address | Product catalog current; content dates 2024 | Free app/support; individual input prices shown, advisory subscription price not established | B-/C+ [3]
| Gramophone | Google Play listing, updated June 19, 2023. https://play.google.com/store/apps/details?id=agstack.gramophone | Crop, soil, area, weather, stage, experts, community, mandi and commerce | Stale listing | App and commerce; no authoritative current advisory price | C [7]
| Aquaconnect | Aquaconnect official site, retrieved August 16, 2026. https://aquaconnect.blue/ | Pond boundaries, fish/shrimp validation, culture-day prediction, demand/harvest, stores, market and credit | Live, undated | Partner/store/platform access; no list price | B-/C+ [22]
| PMFBY claim rules | Department of Agriculture and Farmers Welfare, *PMFBY Operational Guidelines 2023*, effective Kharif 2023. https://pmfby.amnex.co.in/pmfby/pdf/operational_guidelines_pmfby.pdf | Policy, notified crop/area, farmer/policy, event notice, evidence and assessment | Current reviewed operational edition | Free PDF; filing through PMFBY/insurer channels, not an open adjudication API | A- [24]
| Advisory failure evidence | CSE, *Agromet Advisories in India: An Assessment*, April 23, 2020; Sharma et al., Haryana randomized SMS study, 2021; Avaaj Otalo field study, 2010 | System assessment; 463-farmer Haryana analysis; small Gujarat IVR field study | Mixed, 2010-2021 | Free reports/articles | B [20][34][18]

**Inventory takeaway:** The free stack is rich in forecasts, bulletins, rulebooks, delivery precedents, historical questions, and claims policy. It is poor in joinable live farm profiles, machine-readable action rules, verified event damage, and production-grade APIs.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing fields | Coverage judgment |
|---|---|---|---|
| IMD/GKMS/Meghdoot | Five-day weather variables; crop-stage expert workflow; district/block bulletins; Tuesday/Friday schedule; severe-weather guidance; vernacular SMS and multiple media | No documented public API/SLA; routine cadence is not a continuously individualized trigger; no claims linkage | **A-** [33]
| CWC flood forecasts | Public seven-day flood advisory and station/basin display | No reviewed farm-plot mapping or stable API contract | **B+** [15]
| KCC and OGD transcripts | 22-language human fallback; expert escalation; daily open-data API for state/district/block/season/sector question mining | No current headline call total; open metadata does not list crop, full question, answer, date or language fields in the preview; callback SLA not documented | **A-/B+** [36][30]
| mKisan | Feature-phone reach, text/voice/USSD, detailed registration schema and preference targeting | Actual dated enrollment count absent; public export/API absent; cumulative traffic lacks an as-of date and denominator | **B+** [31][29]
| ICAR/KVK and Odisha contingency plans | District and state agronomy, hazard-response options, crops, livestock and fisheries | Mostly PDFs; district documents may be old; no normalized trigger/action schema or version API | **B+** [2][28]
| Odisha Ama Krushi | Free, two-way localized voice model and measured excess-rainfall outcomes | Public API, profile export, exact stage field and claim packet are not evidenced | **B+/C+** [14]
| KALIA | State farmer-welfare and beneficiary-network context useful for partnership and outreach | Not a public agronomic profile API; identity/beneficiary access is controlled | **B-/C+** [27]
| DeHaat, Fasal, BharatAgri, Gramophone, Aquaconnect | Strong patterns for photo diagnosis, sensors, crop calendars, stage advice, expert support, commerce, aqua intelligence and credit | Mostly self-reported; pricing often quote-only or undisclosed; no product publicly shows the full disaster-to-claim loop | **C+** [25][23][7][22]
| Failure-mode literature | CSE system diagnosis, Haryana randomized evidence, and low-literacy IVR precedent | Different states, crops and years; limited direct Odisha cyclone evidence | **B** [20][34][18]
| PMFBY claims | Official rule basis and report-loss workflow | Eligibility, policy, notified crop/area, loss verification and adjudication remain external | **A-** [24]

The best-covered layers are **weather**, **expert agronomy**, and **channel precedents**. The weakest are **farmer-specific state**, **real-time event orchestration**, **claim-system integration**, and **outcome telemetry**.

## 4. WHAT IS MISSING

The gap is not another weather app. It is a joinable, governed **Odia Cyclone-to-Claim Advisory Loop**. No reviewed public source or product evidences all five required capabilities in one operational chain: **event-triggered + crop-stage-aware + Odia + offline SMS/IVR + claim-linked**.

1. **A live, consented Odisha farm profile keyed to a plot.** Public sources do not provide a joinable record containing plot polygon or village, farmer phone, preferred language/channel, crop and variety, sowing/transplanting date, present phenological stage, irrigation/drainage, livestock/aquaculture assets, storage, insurance policy and consent. mKisan shows a useful registration schema, but no public export; KALIA is a controlled welfare database, not an open agronomic feed. [29][27]

2. **A machine-readable event-to-action rule set.** IMD supplies forecasts and expert bulletins; Odisha and CRIDA supply contingency documents. Missing is a versioned rule such as: `cyclone landfall <48h + paddy at panicle initiation + low-lying plot -> drain field, stop nitrogen, secure pump, deadline 18:00, source paragraph, confidence, escalation number`. The source knowledge exists, but not this executable join. [33][2]

3. **Continuous trigger orchestration.** Tuesday/Friday production is operationally disciplined, but a cyclone can intensify between runs. IMD supports severe-weather advice, yet the reviewed material does not establish a public event stream with a delivery SLA that automatically regenerates advice for every affected farm. [33]

4. **Validated Odia microcopy for low-literacy, high-stress use.** "Regional language" and voice support are not equivalent to tested Odia comprehension. Missing assets include short Odia scripts, dialect handling, action verbs, absolute deadlines, replay/confirmation, caregiver sharing, and human escalation, tested under power and network disruption.

5. **Observed damage and evidence provenance.** No public feed supplies plot-level post-event standing water, lodging, salinity, carcass loss, pond breach, geotagged photos, capture time, device identity, hash and farmer attestation as one claim-ready record.

6. **Policy-to-farmer insurance linkage.** PMFBY rules are public, but the farmer's insurer, season, notified crop/area, application/policy number and claim status are not openly joinable. KrishiSetu can prepare evidence and reminders; it cannot determine coverage or settle a claim. [24]

7. **Receipt, comprehension and action telemetry.** SMS sent is not advice understood. Missing are delivery receipts, IVR listen-through, replay, keypress confirmation, reported action, reason for non-action, damage avoided and agronomist audit. The Haryana trial shows that SMS can improve scheduling compliance while still producing no significant yield improvement, so transport volume is a poor success metric. [34]

8. **Current operating economics.** Public list prices are missing for Fasal hardware/service, Gramophone advisory, Aquaconnect services and most DeHaat commercial components. Telecom DLT, IVR minutes, human escalation, agronomist review, field verification and insurer integration must be costed separately.

## 5. HOW IT FEEDS THE ENGINE

| Data item | Pre-disaster action | Post-disaster recovery | Claim packet | Next-season planning | Positive-use advice |
|---|---|---|---|---|---|
| IMD five-day forecast and warnings | Determine event type, lead time, wind/rain window and affected district/block; trigger preparation deadline | Decide safe re-entry and whether rain/wind risk persists | Preserve bulletin ID, issue time and affected geography as event context | Build local event/forecast history | Schedule irrigation, spraying, fertilizer and harvest [33]
| IMD cyclone bulletins | Secure pumps, seed, livestock, pond equipment and harvested produce based on track, wind and surge | Stage safe inspection after warning downgrade | Attach official event timeline | Update cyclone exposure score | None outside event readiness
| CWC flood forecast | Escalate low-lying and river-adjacent farms; prioritize drainage, relocation and harvest | Estimate inundation persistence and access routes | Attach official station/basin alert | Update flood recurrence and crop suitability | Reservoir/river awareness where agronomically relevant
| Odisha 2025 contingency plan | Select approved crop/hazard actions | Generate re-sowing, drainage, sanitation, feed and disease-control checklists | Provide agronomic rationale, not proof of loss | Adjust varieties, sowing window and diversification | Seasonal contingency reminders [2]
| CRIDA district plans | Add district soil, irrigation, crop, livestock and fisheries context | Choose district-relevant recovery options | Identify normal district farming context | Support district crop/variety and water planning | Local crop calendar baseline [28]
| Farmer profile collected by KrishiSetu | Filter advice by exact plot, crop, variety, stage, assets, language and channel | Ask only relevant damage questions | Populate farmer, plot, crop, insurer and consent fields | Track outcomes and revise plan | Personal daily/weekly recommendations
| mKisan schema | Reuse field vocabulary and channel preferences | Route text versus voice follow-up | Carry identity/contact fields, subject to consent | Maintain longitudinal crop profile | Preference-based push/pull service [29]
| Ama Krushi design | Use concise, free voice pushes and two-way questions | Provide IVR triage and expert escalation | Explain next steps but do not adjudicate | Feed repeated questions into content priorities | Weekly localized advice; outcome evidence supports the approach [14]
| KCC workflow and transcripts | Escalate ambiguous agronomy to human experts | Resolve symptoms that should not be automated | Refer scheme/claim questions to an authorized channel | Mine recurring district/season questions | Human fallback in 22 languages [36][30]
| On-farm IoT, where purchased | Confirm local rainfall, soil moisture, water level, wind or pond conditions | Detect drainage recovery and irrigation readiness | Sensor log may support chronology but is not insurer validation | Calibrate plot risk and input use | Precision irrigation/fertigation, as Fasal demonstrates [23]
| Photo and satellite inputs | Detect pre-event stress and prioritize farms | Classify lodging, waterlogging, disease or pond damage for review | Build a timestamped, geotagged evidence bundle | Compare resilience by field | Diagnosis and crop-health monitoring, as DeHaat demonstrates [25]
| PMFBY guidelines | Warn insured farmers what to preserve and where to report | Drive a structured loss-intimation checklist | Produce a draft packet with policy/application identifiers, crop/plot/event data, photos, timestamps and farmer declaration | Explain insurance readiness for next season | Policy-literacy reminders [24]
| Market/input and aqua networks | Check availability of tarpaulins, seed, feed, medicines and equipment | Route replacement inputs, buyers or credit | Record invoices only where relevant | Compare resilient input and market options | Commerce and pond-management advice [22][3]
| Outcome telemetry | Confirm warning delivery and action completion | Measure recovery progress | Record submission and escalation status | Learn which advice reduced loss | A/B test timing, wording and channel

**Engine design implication:** Use a provenance-preserving rules engine, not unconstrained generative text. Each message should carry event timestamp, farm-state snapshot, rule/source version, action, deadline, reason, confidence, and escalation route. An LLM can translate and compress approved advice, but should not invent pesticide doses, insurance eligibility or disaster deadlines.

## 6. REAL-vs-FILLER

| Classification | Evidence-backed asset | Why it is real or filler |
|---|---|---|
| **REAL NOW** | IMD five-day district/block variables and GKMS bulletin workflow | Defined inputs, expert roles, schedule, crop-stage logic and dissemination exist. It can power a replayable rules prototype. [33]
| **REAL NOW** | IMD cyclone and CWC flood public pages | They provide official event context, though production use needs stable-feed agreements and monitoring.
| **REAL NOW** | Odisha Crop Contingency Plan 2025 and CRIDA district files | They contain substantive agronomic context and can be manually extracted and reviewed; their PDF form is inconvenient, not decorative. [2][28]
| **REAL NOW** | KCC open-data API | It is updated, daily, licensed for reuse, and useful for query taxonomy and content-gap discovery. It is not automatically a clean agronomy training set. [30]
| **REAL NOW** | mKisan registration schema | It supplies a practical minimum profile vocabulary and validates feature-phone modes. The records themselves are not open data. [31][29]
| **REAL NOW** | Haryana randomized evidence | SMS measurably reduced deviation from recommended timing for several farm operations and increased rainfall substitution by **9 percentage points**, while yield did not significantly improve. This is design evidence, not a guarantee for Odisha. [34]
| **REAL, PARTNER-DEPENDENT** | Ama Krushi voice delivery, KALIA reach, KVK/OUAT experts, PMFBY/insurer workflow | These have institutional value, but KrishiSetu cannot assume database, content, channel or adjudication access from public pages. [14][27][24]
| **REAL, PURCHASE-DEPENDENT** | Fasal sensors; DeHaat diagnostics; Aquaconnect pond/geospatial intelligence | Technically relevant, but hardware, platform access or commercial terms are not free public data. [23][25][22]
| **FILLER IF USED ALONE** | "AI-powered", "satellite-enabled", app download counts and broad reach claims | They do not specify trigger thresholds, accuracy, farmer action, deadline, cost, API or avoided loss.
| **FILLER IF MISREAD** | mKisan's 8.93 crore potential reach and cumulative SMS totals | Potential reach is not enrollment; sent messages are not receipt, comprehension, action or outcome. [31]
| **FILLER IF MISREAD** | KCC page download/view numbers | **222,996** is the dataset's download count, not call volume. Call volume must be calculated from records. [30]
| **FILLER IF MISREAD** | Presence of "insurance" in a private app | Selling or facilitating insurance is not a claim-ready advisory, verified loss report or insurer integration. DeHaat evidences insurance access, not the complete claim workflow. [25]
| **FILLER FOR THIS PROBLEM** | Smartphone-only commerce catalogs without Odia SMS/IVR or hazard triggers | They benchmark UX and supply linkages but do not solve the stated low-literacy disaster-delivery requirement. [3][7]

The distinction is operational: a source is real only if it changes a decision, supplies a required field, or validates a delivery mechanism. Brand claims without thresholds, interfaces, costs or outcomes should not enter the engine backlog as "data".

## 7. NOISE LOG

| Search lead discarded or downgraded | Reason |
|---|---|
| `kaliaportals.com`, SarkariYojana, Brinto and similar KALIA pages | Third-party beneficiary/status sites, sometimes styled like official services. They were not used for scheme facts or database access claims.
| Generic DeHaat pricing aggregators such as RevAvenues | Repeated features but did not establish authoritative farmer prices. Official app/site evidence took precedence.
| Search false positives from National Review, MangaTown, WhatsApp and YouTube | Query noise caused by mixed company names, `OR`, and `free`; unrelated to agriculture and excluded.
| LinkedIn company descriptions and third-party APK/download pages | Useful for discovery only; prone to stale or conflated company descriptions. Official sites and Google Play listings were used instead.
| Nigerian agricultural-app usability study | Relevant topic but wrong country and farming context; excluded from India-specific failure evidence.
| Promotional 2026 "voice AI" articles and a generic JETIR prototype | Assertions about literacy benefits without comparable field evidence; replaced by Avaaj Otalo and Ama Krushi.
| ResearchGate snippets for the Haryana paper | Search snippets conflated SMS and voice descriptions. The full ScienceDirect article was read instead. [34]
| Fasal `/fasal-story` URL | Returned `NoSuchKey`; excluded. The live official product page supplied current capability evidence. [19]
| CRIDA national landing page alone | Navigation did not expose enough Odisha detail. The Odisha directory and direct Ganjam PDF were used. [28]
| PIB KCC release of December 9, 2025 | Useful for center distribution and grievance context but did not provide call volume. Open-data records are the defensible volume path. [13][30]
| mKisan **8.93 crore** figure | Retained only as potential farm-family reach based on May 2014 telecom data, not presented as registered farmers. [31]
| Private-product price searches | No authoritative current advisory subscription or hardware/service list price was found for most products. "Not publicly disclosed / quote required" is reported instead of guessed pricing.

## 8. VERDICT

### Overall grade: **PARTIAL**

A prototype can use substantial public data today, but "free data" does not mean a free or production-ready service.

| Delivery level | Grade | What can be done now | Constraint |
|---|---|---|---|
| Offline data demonstration | **GO** | Download IMD/CRIDA/Odisha/PMFBY documents; model a cyclone or flood; register sample farms; generate approved pre-event, recovery and claim-checklist messages | Must clearly label simulated alerts and sample profiles
| Live alert ingestion pilot | **PARTIAL** | Monitor official IMD/CWC pages and route district/block events to consenting test farms | No reviewed stable API/SLA; polling and source-change monitoring are fragile
| Agronomic rules engine | **PARTIAL -> GO after review** | Convert Odisha 2025 and selected district plans into structured rules with provenance | KVK/OUAT/department agronomists must validate doses, timing and crop-stage conditions
| Odia SMS/IVR delivery | **PARTIAL** | Build scripts, IVR replay and keypress confirmation; reuse mKisan/KCC/Ama Krushi patterns | Telecom DLT, IVR minutes, Odia testing, opt-in/consent and human escalation are not free
| Hyperlocal farmer state | **GATED BY COLLECTION** | Collect village/plot, crop, variety, sowing date, stage, drainage, assets, channel, language and insurance fields | No public live farm-profile dataset supplies this bundle
| Claim-packet assistance | **PARTIAL** | Remind, capture identifiers, geotagged/time-stamped evidence, and export a structured draft packet | Policy validation, notified-area checks, loss assessment, submission acceptance and settlement remain with NCIP/insurer/government
| Statewide deployment | **GATED BY PARTNERS** | Potentially integrate official alerts, Ama Krushi/mKisan delivery, KALIA outreach, KVK experts and insurers | Requires agreements, data protection controls, security review, channel capacity and operating budget

**Build now with free sources:**

1. A versioned IMD/CWC event ingestor with source URL, issue time and checksum.
2. A small, expert-reviewed rule library for 3-5 Odisha districts, paddy plus one pulse/oilseed, livestock, and one aquaculture scenario.
3. A consented farmer-registration form derived from mKisan fields, adding plot, crop stage, drainage, assets and insurance identifiers.
4. Odia SMS and IVR templates with one action, one reason, one absolute deadline, replay, confirmation and KCC escalation.
5. A post-event evidence module that captures time, location, photo, farmer declaration and immutable audit history.
6. A PMFBY packet export that explicitly says "draft assistance, not coverage or settlement confirmation."
7. Outcome telemetry: delivered, listened, understood, acted, unable-to-act reason, damage and recovery.

**Collect directly:** exact plot/village, phone ownership/shared-phone status, consent, preferred Odia variant and channel, crop/variety, sowing/transplant date, present stage, irrigation/drainage, livestock/pond assets, storage, disability/accessibility needs, insurance/policy information, and verified post-event damage.

**Partner for:** an authorized/stable IMD warning feed; CWC operational integration; Odisha Agriculture, OUAT and KVK agronomic sign-off; Ama Krushi/mKisan/KALIA outreach or profile interoperability; telecom DLT and IVR capacity; PMFBY/NCIP and insurer submission/status integration; and local field verification.

The decisive product metric should be **eligible farms taking the right action before the deadline**, followed by avoided loss and claim completion. It should not be app downloads, messages generated, messages sent, or model fluency.

## Synthesis

| System | Mechanism | Scope and time horizon | Main strength | Main trade-off | KrishiSetu implication |
|---|---|---|---|---|---|
| Meghdoot/GKMS | Expert panel converts forecast plus crop-stage context into bulletins | District/block; five-day forecast; twice weekly with severe-weather support | Authoritative weather-agronomy chain | Cadence and public interfaces are not an individualized continuous trigger | Use as source of truth; add event orchestration and farm-state filtering [33]
| mKisan | Preference-targeted text, voice, USSD, push and pull | National delivery and registration | Feature-phone precedent and useful profile schema | Enrollment count/export and outcome data are not public | Reuse schema/channel concepts; collect consented profiles independently [31][29]
| KCC | Human first line plus specialist escalation | On demand, 16 hours daily, all week | Trust, ambiguity handling, 22 languages | Reactive and capacity-limited; volume must be derived from data | Use as escalation, not the primary mass-warning engine [36]
| ICAR/Odisha plans | Static expert contingency rulebooks | District/state; seasonal and hazard planning | Substantive crop/livestock/fisheries content | PDF-shaped, uneven age, not automatically event-linked | Convert selected rules with provenance and agronomist approval [2][28]
| Ama Krushi | Free two-way localized voice advisory | Weekly/on-demand Odisha farmer support | Closest delivery model; measured rainfall-related outcomes | Public API, exact stage state and claim linkage absent | Partner rather than duplicate; add disaster trigger and evidence workflow [14]
| Private agritech | App, sensors, diagnostics, experts, commerce and credit | Individual farm or commercial customer | Strong UX, personalization and supply linkage | Smartphone/hardware dependence, opaque pricing, no complete public disaster-to-claim evidence | Borrow patterns selectively; do not claim feature parity from marketing [25][23][22]
| PMFBY ecosystem | Policy-driven notice, evidence, assessment and settlement | Event and season-specific | Official claim pathway | Eligibility and adjudication remain institutional | Prepare complete, timely packets; never promise acceptance or payout [24]

The non-obvious tension is that India does not lack advice. It has authoritative forecasts, agronomists, call centers, SMS infrastructure, static contingency knowledge, state voice delivery and sophisticated private apps. What it lacks is the connective tissue: a continuously updated farm state, an event-triggered rules layer, tested Odia microcopy, verifiable action/evidence capture, and insurer handoff. That is the defensible KrishiSetu position.

## References

1. *Kisan Call Centre*. https://agriwelfare.gov.in/sites/default/files/KCC%20WEBSITE.pdf
2. *crop contingency plan ori.nic.in https://agrisnetodisha.ori.nic.in › crop contigency ...*. https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
3. *BharatAgri – Smart Farming & Crop Advisory App for Farmers*. https://bharatagri.com/
4. *'Meghdoot' – Mobile app for weather based agro advisories PIB https://www.pib.gov.in › PressReleaseIframePage*. https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1739245
5. *Fasal | Science, Technology and Innovation (STI) Portal*. https://sti-portal.fao.org/innovations/fasal
6. *Meghdoot - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en_US&id=com.aas.meghdoot
7. *Gramophone - Smart Farming App – Apps on Google Play*. https://play.google.com/store/apps/details?hl=en-IN&id=agstack.gramophone
8. *mKisan: A Portal of Government of State Base Services for ...*. https://mkisan.gov.in/
9. *Flood Forecasting/ Hydrological Observation | Central Water ...*. https://cwc.gov.in/flood-forecasting-hydrological-observation
10. *KALIA Scheme in Odisha: An Analysis of Agricultural ...*. https://www.ijfmr.com/research-paper.php?id=76821
11. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://pmfby.gov.in/guidelines
12. *Welcome to ICAR-CRIDA | भाकृअनुप – केंद्रीय बारानी कृषि अनुसंधान संस्थान*. https://icar-crida.res.in/Crop_Contingency_Plan.html
13. *kisan call centres*. https://www.pib.gov.in/PressReleasePage.aspx?PRID=2201003&lang=1&reg=3
14. *Ama Krushi – Scaling advisory services to millions of farmers ...*. https://precisiondev.org/project/ama-krushi
15. *Flood Forecast - Central Water Commision, Govt. Of India*. https://ffs.india-water.gov.in/
16. *Cyclone - IMD - India Meteorological Department*. https://mausam.imd.gov.in/imd_latest/contents/cyclone.php
17. *mKisan: A Portal of Government of State Base Services for ...*. https://mkisan.gov.in/Home/AboutKSEWA
18. *Chi Talk Patel 4.0*. https://hci.stanford.edu/publications/2010/avaajotalo/chi_talk_patel_4.0.pdf
19. *Fasal Story*. https://www.fasal.co/fasal-story
20. *cdn.cseindia.org*. https://cdn.cseindia.org/attachments/0.65638100_1587639351_agromet.pdf
21. *Dehaat Shop*. https://dehaat.in/en
22. *South Asia’s Largest Aquaculture Network*. https://aquaconnect.blue/
23. *Fasal - Smart Irrigation System | Agriculture Automation*. https://www.fasal.co/
24. *Operational Guidelines Pmfby*. https://pmfby.amnex.co.in/pmfby/pdf/operational_guidelines_pmfby.pdf
25. *DeHaat Kisan: Farming Guide - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en_US&id=app.intspvt.com.farmer
26. *Push SMS - mKisan*. https://mkisan.gov.in/alpha/pushsms.aspx
27. *Transforming Farmer Welfare in Odisha: The KALIA Story | Blog*. https://samagragovernance.in/blog/2025-05-12-transforming-farmer-welfare-in-odisha-the-kalia-story
28. *Microsoft Word - Ganjam_orissa_Suma-Final-05-05-11+LS*. https://www.icar-crida.res.in/CP/Orissa/OUAT%2C%20Bhubaneswar/Orissa%2014-%20Ganjam%2031.05.2011.pdf
29. [
        mKisan: A Portal of Government of State Base Services for Farmer centre Mobile Services
    ](https://mkisan.gov.in/Home/FarmerRegistration)
30. *Kisan Call Centre (KCC) - Transcripts of farmers queries  answers | Open Government Data (OGD) Platform India*. https://www.data.gov.in/resource/kisan-call-centre-kcc-transcripts-farmers-queries-answers
31. [
        mKisan: A Portal of Government of State Base Services for Farmer centre Mobile Services
    ](https://mkisan.gov.in/Home/About)
32. [
	Press Release Page | Press Information Bureau
](https://pib.gov.in/PressReleasePage.aspx?PRID=2223075)
33. *Gkms Sop*. https://mausam.imd.gov.in/imd_latest/contents/pdf/gkms_sop.pdf
34. *Do phone-based short message services improve the uptake of agri-met advice by farmers? A case study in Haryana, India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212096321000504
35. *MANAGE*. https://www.manage.gov.in/kcc/kcc.asp
36. [
	Kisan Call center
](https://www.dackkms.gov.in/account/aboutus.aspx)
