# Farmer Data That Makes Odisha Advisories Doable

## 1. EXECUTIVE SUMMARY

- **Optimize doability, not message accuracy alone:** A Southern India trial found that mobile extension improved adoption of recommended practices by **4-7 percentage points**, but did not produce a significant yield change. Only **5.9%** of households listened beyond the average IVR message length of 47.25 seconds. The product should therefore ask about cash, labor, time, mobility, storage and tenure before recommending an action, and keep each voice action short [43].

- **The zero-new-hardware thesis is credible at the farmer edge:** Voice works on ordinary phones and avoids a literacy requirement [46]. Odisha already has a two-way model: Ama Krushi, renamed the Krushi Samruddhi Helpline in August 2024, is reported as serving nearly **7.9M farmers** [47]. The innovation is not another sensor box; it is structured DTMF, voice and assisted-photo collection over rails farmers already use.

- **A photo can start and strengthen a claim, but cannot prove one by itself:** The PMFBY Revised Operational Guidelines allow mobile applications to capture location and pictures as crop-loss evidence, but still require a claim form, relevant documents and joint assessment. Localized and post-harvest losses must be reported within **72 hours** [2]. The prototype must say "claim-ready packet," never "instant approved claim."

- **Odisha already has the identity and crop-data backbone:** The live Krushak Odisha portal displayed **91,72,732 farmers** when checked [5]. e-Chasa was launched in August 2024 after a four-district pilot covering about **30 lakh plots**, with a statewide target of roughly **3 crore plots**, **48 lakh hectares** and **48 lakh farmers** [27]. The product should become an evidence and doability layer over these rails, not a rival farmer registry.

- **The data-cooperative model is real, but it is governance infrastructure rather than a hackathon feature:** Dutch cooperative JoinData reports more than **16,000 farmer members**, about **260 participating parties**, and 70 parties using data for farmers. Farmers can grant and withdraw purpose-specific authorizations [9]. For Odisha, prototype the consent ledger now; institutionalize cooperative control only after farmer organizations and the state agree on governance.

- **Consent must produce a visible return:** The EU agricultural-data code gives the data originator a leading contractual role and says compensation may be money, services or improved products, but the code is voluntary and non-binding [8]. Every data request should therefore display "what you give, who sees it, how long it stays, and what you receive."

- **Credit visibility is plausible; automatic credit is not:** Apollo Agriculture uses satellite data, GPS mapping, soil sampling and harvest measurement to build credit profiles and bundle inputs, insurance and advice [14]. Its cited program page supplies no quantified outcome evidence, so the product should create a farmer-controlled evidence summary for a future lender pilot, not issue a score or promise a loan.

- **Juhudi Kilimo is a finance precedent, not a verified data-scoring precedent:** Authoritative pages describe productive-asset finance for dairy cows, poultry equipment and irrigation, but do not state that Juhudi underwrites with farmer-generated or alternative farm data [15][17]. Use it to show what credit can finance, not to validate the proposed scoring algorithm.

- **Carbon is an optional later loop, not the core return:** Kenya's Agricultural Carbon Project issued **24,788 metric tons** of carbon reductions; a World Bank fund expected to purchase part of the credits by 2017 for an estimated **$600,000**. Retrieved sources do not disclose per-farmer proceeds or transaction costs [41]. Better advisory, avoided loss and claim evidence must create value before any carbon promise.

- **Title and phone control are first-class safety variables:** The national Farmer Registry starts the farm ID in the landowner's favor and relies on owner authorization to direct scheme benefits to a cultivator without declaring tenancy [39]. The product must maintain separate owner, cultivator, claimant and phone-controller roles; otherwise better data could make exclusion more efficient.

- **The one-day vision test passes with a narrow claim:** A hackathon can demonstrate photo/DTMF input -> feasibility-aware advisory -> evidence receipt -> claim-packet JSON/PDF -> consented "future credit visibility" summary. It cannot demonstrate live PMFBY adjudication, Krushak/e-Chasa APIs, regulated underwriting, cooperative governance or carbon revenue. Those are year-one partnerships, not UI screens.

## 2. INVENTORY

**Grades:** A = directly evidenced and deployable on an existing Odisha/basic-phone rail; B = real and useful but needs integration or assisted access; C = a real precedent with weak transferability or outcome evidence; D = misleading or filler when used for the claimed purpose.

| What | Mechanism | Named source, URL and date | Scale/status | Feasibility for basic-phone farmers | Grade |
|---|---|---|---|---|---|
| **Farmer-as-sensor through voice/DTMF** | Farmer calls, follows prompts, records a question or condition report, and receives voice guidance. | Avaaj Otalo, Stanford HCI, 2010, `http://hci.stanford.edu/publications/2010/avaajotalo/chi_talk_patel_4.0.pdf` | Pilot included 63 mostly farming participants, all Gujarati speakers and computer/IVR novices [46]. | High. Works on ordinary phones and avoids text literacy; photo collection still needs an assisted or smartphone path. | **A** |
| **Ama Krushi/Krushi Samruddhi Helpline** | Toll-free IVR, live agent, weekly personalized calls, stored advisory history and agronomist answers. | Precision Development, project page, renamed August 2024, `https://precisiondev.org/project/ama-krushi` | Nearly 7.9M farmers reported after the rename; service spans Odisha [47]. It supports inbound IVR and live-agent escalation [47]. | Very high. This is the best existing delivery and profile rail. | **A** |
| **Kisan Call Centres** | Human experts plus dynamic IVR; queued callers hear wait estimates and seasonal advice. | Press Information Bureau, December 9, 2025, `https://pib.gov.in/PressReleasePage.aspx?PRID=2201003&lang=1&reg=3` | National operational network; scope includes agronomy, schemes, weather, markets and technology [48]. | High, but a data-sharing and referral protocol would be needed. | **A** |
| **Krushak Odisha** | Singular state farmer record and service-navigation layer. | Government of Odisha portal, accessed August 16, 2026, `https://krushak.odisha.gov.in/` | Portal displayed 91,72,732 farmers and linked Sugam, CM KISAN, Ama Krushi, AM-PIS and GO-SUGAM [5]. | Medium. It is an integration rail, not itself an IVR interface; no public API was found. | **B** |
| **e-Chasa digital crop survey** | Surveyors submit crop and plot records; supervisors verify them; headquarters checks anomalies, duplicate records and image reuse. | Odisha launch reporting, August 21, 2024, `https://odishabhaskar.in/odisha/odisha-echasa-digital-agriculture-survey-90616`; implementation reporting, September 11, 2025, `https://www.odishanewstimes.com/2025/09/11/odisha-pushes-for-100-accuracy-in-digital-crop-survey-2025` | Pilot: about 30 lakh plots. State target: about 3 crore plots and 48 lakh farmers [27]. In September 2025 reporting, survey coverage was 52.53% and initial approval 49.30% [38]. | Medium-low for direct use; high through assisted enumerators or helpline referrals. | **B** |
| **PMFBY loss evidence and claim packet** | 72-hour loss intimation through insurer, bank, agriculture officials, toll-free number or NCIP; app may attach location and pictures; joint assessor-agriculture officer-farmer survey decides loss. | PMFBY Revised Operational Guidelines, undated in retrieved PDF, accessed August 16, 2026, `https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf` | Official workflow for insured localized and post-harvest losses [2]. | Medium. Intimation can be basic-phone friendly, while photo and document assembly may require an agent or smartphone. | **A** for packet preparation; **D** for "photo equals approval" |
| **EU agricultural-data code** | Purpose-specific, informed contractual permission; authorized access; auditability; machine-readable return and portability; compensation defined in contract. | EU Code of Conduct on Agricultural Data Sharing by Contractual Agreement, 2020, `https://croplifeeurope.eu/wp-content/uploads/2021/03/EU_Code_of_conduct_on_agricultural_data_sharing_by_contractual_agreement_2020_ENGLISH.pdf` | Multi-association voluntary code, not binding law [8]. | High as a design checklist; low as legal authority in Odisha. | **B** |
| **JoinData farmer data cooperative** | Farmer dashboard grants and withdraws permissions; nonprofit exchange routes rather than owns/stores shared data; users pay and data-using companies pay. | USAID/DAI JoinData case study, February 2023, `https://cdn.prod.website-files.com/63b7bb07476f22ccbab419d5/6593f3490766f1d54510c4e9_Agricultural-Data_CaseStudy_Feb2023.pdf` | 16,000+ members, about 260 parties, 70 active data-using parties [9]. Almost 40% of dairy farmers reportedly did not know who they had authorized, showing that a dashboard alone does not create comprehension [9]. | Low for direct transplantation; medium as a cooperative-governance blueprint with voice consent. | **B** |
| **Apollo Agriculture data-to-credit** | Satellite-derived farm characteristics plus field GPS, soil and harvest data feed credit-risk models; finance bundles seed, fertilizer, insurance and advice. | Fund for Rural Prosperity, undated page, accessed August 16, 2026, `https://1.frp.org/agribusiness/apollo-agriculture` | Real Kenyan operating model, but retrieved page reports no quantified scale or measured borrower outcome [14]. | Medium. Apollo itself found its average customer did not engage effectively through SMS and used voice and field agents [14]. | **C** |
| **Juhudi Kilimo asset finance** | Microfinance buys productive farm assets and pairs finance with technical support. | Acumen, investment dated 2011, `https://acumen.org/companies/juhudi-kilimo`; Kiva partner page, started January 15, 2010, `https://www.kiva.org/about/where-kiva-works/partners/156` | Real Kenyan lender; retrieved sources do not establish alternative-data scoring [15][17]. | The loan purpose is relevant, but it does not validate this product's data model. | **D** as a scoring precedent; **B** as a finance precedent |
| **WeFarm peer-to-peer advice** | Free SMS accepts questions in multiple languages and routes them to other farmers for answers. | Nesta case study, undated page, accessed August 16, 2026, `https://www.nesta.org.uk/feature/ai-and-collective-intelligence-case-studies/wefarm` | Documented in Kenya, Uganda and Tanzania [21]. Retrieved material does not provide rigorous retention or income effects. | High channel feasibility; uncertain sustained incentive and business model. | **C** |
| **Esoko market/advisory service** | Historical SMS/voice/call-centre information combined market prices, weather and advice; current public site emphasizes a marketplace. | FAO STI portal, solution record dated June 12, 2026, `http://sti-portal.fao.org/innovations/esoko-digital-farmer-service`; current marketplace, accessed August 16, 2026, `https://marketplace.esoko.com/home` | A real multi-channel African service, but the retrieved evidence does not establish current retention or a causal payoff for farmer data contribution. | Medium. Useful as a channel lesson, not proof of a self-sustaining data loop. | **C** |
| **Kenya Agricultural Carbon Project** | Aggregates smallholders, promotes sustainable land management, measures soil/tree carbon, independently verifies it and sells credits. | World Bank press release, January 21, 2014, `https://www.worldbank.org/en/news/press-release/2014/01/21/kenyans-earn-first-ever-carbon-credits-from-sustainable-farming`; Vi Agroforestry, current project page, `https://www.viagroforestry.org/projects/kacp` | 24,788 metric tons initially issued; part of expected purchases was estimated at $600,000 by 2017 [41]. Project page targets 30,000 farmers and about 22,000 hectares [19]. | Low for a basic-phone MVP. Aggregation, practice verification, contracts and MRV are the expensive parts. | **C** |
| **Farmer Registry cultivator authorization** | Farm ID begins with landowner; owner can authorize a scheme-level beneficiary so a cultivator receives benefits without formal tenancy declaration. | Farmer Registry Administrative and Technical Clarifications v1.1, July 2024, `https://agristack.gov.in/assets/registries/farmerRegistry/farmer_registry_faqs.pdf` | National reference architecture; state implementation remains decisive [39]. | Medium. It supplies a possible inclusion route but also creates owner veto and coercion risks. | **B** |

**Inventory takeaway:** Odisha has enough real rails for an **A-grade advisory and evidence MVP**. The cooperative, credit and carbon layers are legitimate directions, but none should be presented as an immediate guaranteed farmer payout.

## 3. COVERAGE TABLE

| Value-loop stage | What already exists | Evidence strength | Uncovered break in the loop | MVP treatment |
|---|---|---|---|---|
| **Data collection** | IVR/DTMF precedents; farmer questions; e-Chasa photos and crop records; PMFBY pictures/location. | Strong for collection mechanics [46][2][38]. | No unified event schema, provenance standard or shared-phone identity model. | Capture a minimal event: farmer, cultivator, plot, crop, event, time, location confidence, photo/voice, and consent receipt. |
| **Better advisory** | Ama Krushi already personalizes weekly advice and stores it against a farmer profile [47]. | Strong operational precedent. | Existing systems optimize content more than the farmer's ability to execute it. | Add a DTMF "can-do" survey before selecting an action. |
| **Better outcome** | Ama Krushi reports a 10% lower probability of severe crop loss overall, 9% higher harvest in excess-rainfall areas and a 21% lower severe-loss probability under inadequate rainfall [47]. | Promising program evidence, but not proof for this new product. | No causal chain from a specific recommendation to completion, cost and outcome. | Ask for action confirmation and a short post-event outcome report; do not infer success from message delivery. |
| **Claim evidence** | PMFBY accepts app pictures among multiple evidence sources and uses joint assessment [2]. | Strong on procedure. | Photo quality, enrollment matching, document completeness and assessor acceptance. | Produce a completeness checklist and evidence packet; route official submission rather than claiming adjudication. |
| **Credit visibility** | Apollo demonstrates satellite/field-data underwriting for bundled input credit [14]. | Medium mechanism evidence; weak outcome evidence. | No Odisha lender agreement, consented feature specification, fairness testing or adverse-action process. | Show an opt-in evidence summary labeled "not a credit score." |
| **Scheme eligibility** | Krushak Odisha is the state record; Farmer Registry can prepopulate land data and permit owner-authorized cultivator benefits [5][39]. | Strong architecture evidence. | Tenant dependence on owner authorization; no confirmed public integration API. | Detect mismatches and create a referral/task ticket, not an eligibility decision. |
| **Premium/buyer market** | Traceability and carbon aggregation demonstrate possible downstream use; KACP routes carbon income to participating farmers [19]. | Real but incomplete. | No verified Odisha buyer, commodity premium, per-farmer carbon payout or MRV economics. | Keep out of the core promise; collect only optional, purpose-consented practice data for a later pilot. |
| **Collective control** | JoinData supplies granular authorization and a cooperative institution; EU code supplies purpose, portability and benefit principles [8][9]. | Strong design precedent, different jurisdiction. | Who represents tenants, women, sharecroppers and non-members; enforcement under Indian law. | Implement an auditable consent ledger and farmer data receipt; establish the cooperative only through a governed pilot. |

The coverage is strongest from **collection through claim preparation**, and weakest from **credit through premium markets**. The product should launch where evidence and institutional fit overlap, then earn permission to extend the loop.

## 4. WHAT IS MISSING

### Doability data, not more agronomy

The engine still needs a small, event-specific resource vector: available adults and hours, cash band, access to transport, safe storage, livestock shelter, tools, water, phone access, disability or mobility constraint, and whether the respondent can legally act on the plot. Without those fields, "move inputs," "harvest early" or "dig drainage" can remain impossible even when agronomically correct. This is the central missing dataset.

A doability field should be ephemeral unless it has a defined secondary purpose. Household cash, disability and labor data are highly sensitive; they should not silently become lender or eligibility features. The EU code's purpose restriction and originator permission provide the right minimum pattern, but not an Indian legal answer [8].

### Evidence integrity and institutional acceptance

A photo needs capture instructions, plot matching, event time, location confidence, duplicate detection and an accessible chain of custody. e-Chasa's implementation already encountered incorrect or premature photographs, image reuse, duplicate submissions and false crop or land-status entries [38]. The PMFBY packet also needs the insured crop, affected acreage, survey number, enrollment number, bank details and required documents, followed by official assessment [2].

What remains unverified is whether PMFBY, e-Chasa and Krushak Odisha expose usable APIs, accept third-party evidence packets, or support a common farmer/plot key. A hackathon mock adapter must be visibly labeled as a mock.

### The tenant and shared-phone problem

The product needs four separate roles: **landowner, actual cultivator, claimant, and phone/controller**. They may all be different people. The Farmer Registry's owner-authorization route can include cultivators, but the farm ID initially remains with the owner [39]. A landlord must not be able to view the tenant's cash constraint, suppress loss evidence or revoke historical proof after harvest.

For shared phones, do not display claim amounts, debt indicators or sensitive eligibility details in an unsolicited SMS. Use neutral callback notices, a farmer-chosen PIN or DTMF secret, replay controls, consent renewal, alternate trusted contacts and assisted correction. The research did not establish a safe assumption that every registered number is personally controlled, so the system must ask.

### A credible return for continued contribution

Advice alone is an uncertain incentive. In the Southern India study, farmers picked up at least one IVR at high rates, but the average recipient heard only 7 of 22 messages and no significant yield effect was detected [43]. Earlier Indian assessments also report message overload, mistrust about call charges, and a continuing need for practical training [49].

The immediate return should therefore be visible after every useful contribution: an improved action, evidence receipt, claim checklist, call-back from an expert, correction of a registry mismatch, or a small partner-funded benefit. Cash, airtime or input coupons may be tested, but they must be budgeted and evaluated rather than presented as inherent value from "owning data."

### Credit, carbon and buyer validation

No Odisha lender has agreed which fields are predictive, lawful or fair. No retrieved evidence shows Juhudi using the proposed data. Apollo proves technical plausibility, not local performance. Carbon evidence lacks per-farmer payout and MRV-cost figures; a price premium lacks a named buyer and verified purchasing rule. These stages require separate commercial and regulatory pilots.

### Hyperlocal uncertainty

Farmer reports can correct context but do not repair a poor forecast automatically. A 2020 assessment described a trade-off among lead time, accuracy and location specificity, and reported block-level five-day accuracy of around 60% in the pilots it examined [49]. The engine needs source confidence, report corroboration and an "uncertain" branch, not false precision.

## 5. HOW IT FEEDS THE PRODUCT

### Product rules and algorithms

| Research finding | Feature, rule or algorithm | One-day implementation | Year-one implementation |
|---|---|---|---|
| Farmers may know the hazard but lack resources. | **Doability vector** with labor, cash band, time, mobility, storage, tenure and transport. Apply hard constraints before ranking actions. | DTMF/web form with six yes/no or banded answers. | Adaptive IVR, seasonal defaults, assisted updates and outcome-based calibration. |
| Long voice messages lose attention. | **One-call, one-decision rule:** first action within 20 seconds; maximum three actions; key press to repeat or request a human. | Pre-recorded Odia prompts or TTS. | A/B test timing, voice, length and call-back windows; monitor complete listening rather than delivery. |
| Recommendations must vary by feasible resources. | **Constrained action ranker:** reject actions that violate time, labor, cash or tenure; rank the remainder by expected loss avoided, urgency, confidence and burden. | Transparent rule table, not an LLM. | Agronomist-reviewed rules, probabilistic confidence and observed completion/outcome learning. |
| Farmer observations are useful but noisy. | **Corroboration score:** combine IMD alert, nearby independent reports, e-Chasa crop record, photo metadata and historical profile; never let one report rewrite the forecast. | Mock IMD alert plus two farmer reports. | Spatial clustering, trust calibration, anomaly detection and human review for high-impact alerts. |
| PMFBY pictures support, but do not decide, claims. | **Evidence packet builder:** photo, timestamp, location confidence, voice description, survey number, crop/acreage, enrollment and missing-document flags. | Generate JSON plus a human-readable PDF with a "not submitted/not approved" banner. | Approved submission adapter, status tracking, assessor scheduling and immutable audit trail. |
| e-Chasa has duplicate and inaccurate image risks. | **Evidence quality gate:** blur/darkness check, capture checklist, duplicate hash, perceptual similarity, crop/profile mismatch and retake prompt. | Basic image-quality and duplicate-hash checks. | Offline capture, tamper-evident provenance, model monitoring and contested-evidence review [38]. |
| Data reuse can create value and harm. | **Purpose-bound consent ledger:** separate toggles for advisory, claim, registry correction, research, lender and buyer; expiry and withdrawal; voice receipt. | Store signed/DTMF consent events and display a plain-language receipt. | Farmer-organization oversight, independent audits, portability/export and deletion workflows modeled on the EU code [8]. |
| Tenant, owner and phone user may differ. | **Role-aware access control:** owner cannot automatically see cultivator hardship data; cultivator retains their contributed evidence; claim authority and land authority are distinct. | Four explicit role fields and a conflict flag. | Link to authorized-cultivator mechanisms, grievance desk and legal review; support evidence continuity when tenancy changes. |
| Advice alone may not sustain contribution. | **Give-back transaction:** every accepted report returns an advisory update, evidence receipt, status task or partner benefit. | Show a visible receipt and next action. | Randomized tests of airtime, cash, input coupons, faster expert response and cooperative patronage returns. |
| Farm data can support lending but may discriminate. | **Credit visibility card, not score:** farmer-selected facts such as verified cultivation history, practice completion and claim history, with provenance and correction. | Clearly labeled dummy export. | Lender-defined, consented pilot with bias tests, reason codes, appeal and deletion; no silent reuse. |
| Carbon/buyer value is costly to verify. | **MRV-ready optional log:** practice, date, area, evidence and verifier status, isolated from core service. | A future-value tab with no earnings estimate. | Named buyer/standard, group contract, published fee waterfall and net farmer payment. |

The first ranker should be intentionally simple. For each candidate action, evaluate:

`eligible = time_ok AND labor_ok AND cash_ok AND tenure_ok AND safety_ok`

Then rank eligible actions using a reviewable score such as:

`priority = urgency x expected_benefit x evidence_confidence / (burden + 1)`

The coefficients are product hypotheses, not agronomic facts. A human agronomist and disaster officer should approve the action library. An LLM may translate a selected action into plain Odia, but it should not decide claim eligibility, chemical dosage, evacuation safety or creditworthiness.

### The one-day prototype

1. Load one mocked IMD cyclone/flood alert and one farmer profile.
2. Accept a DTMF-style survey: crop stage, water level, labor, cash band, storage, transport and cultivator/owner status.
3. Accept one farmer or assisted-worker photo and a 20-second voice report.
4. Run deterministic feasibility rules and return one primary action, one lower-cost fallback and one escalation option by simulated IVR/SMS.
5. Generate an evidence receipt and PMFBY-oriented claim packet showing complete and missing fields.
6. Show separate consent toggles for advisory, claim and future lender sharing.
7. Generate a "future credit visibility" card with no score, loan offer or lender logo.
8. Display the audit trail: source, purpose, access, expiry, correction and withdrawal.

This proves the **loop and trust model**, not institutional integration.

### The year-one build

Year one should add live IMD alert ingestion; production telephony; Odia prompt testing; assisted-photo capture; Krushak/e-Chasa identity and plot mapping; a formally approved PMFBY referral/submission path; fraud and quality review; tenant grievance handling; field-officer workflow; security testing; and a controlled outcome evaluation. Only after that should a lender or buyer receive a farmer-consented export.

## 6. REAL-vs-FILLER + NOISE LOG

| Claim or source | Classification | What is real | What must be removed or qualified |
|---|---|---|---|
| **"PMFBY accepts farmer photos as claim evidence"** | **REAL, narrow** | App pictures and location can be evidence for localized loss [2]. | A photo is not an approved claim. Documents and joint assessment remain necessary. |
| **"Photo -> advisory -> claim packet"** | **REAL for a prototype** | All three artifacts can be created locally from documented fields. | Do not show insurer submission or payment unless a real integration exists. |
| **"Apollo proves farm data can support credit"** | **REAL precedent** | Satellite and field data feed credit profiling and bundled finance [14]. | It does not prove performance, fairness or regulatory fitness in Odisha. |
| **"Juhudi is an alternative-data scoring model"** | **FILLER as stated** | Juhudi genuinely finances productive agricultural assets [15]. | Retrieved authoritative sources do not establish data-based scoring. |
| **"Farmer data creates carbon income"** | **REAL but distant** | KACP issued credits and generated a revenue stream [41]. | No automatic eligibility, known net payout or low-cost MRV follows from collecting photos. |
| **"Traceability guarantees a buyer premium"** | **UNVERIFIED** | Better records can support traceability. | No named Odisha buyer, price rule, contract or measured premium was verified. |
| **"The farmer owns the data"** | **OVERSIMPLIFIED** | The EU code gives the originator contractual control over access and use [8]. | It is voluntary, jurisdiction-specific and not a substitute for Indian law, contracts or collective bargaining. |
| **"Krushak Odisha has 9.2M farmers"** | **REAL, rounded** | The current portal displayed 91,72,732, which rounds to about 9.17M [5]. | Do not freeze 9.2M as a permanent count. Include an access date. |
| **"e-Chasa is farmer-generated data"** | **PARTLY REAL** | Farmers can access/report issues, but the major survey workflow is surveyor- and supervisor-led [27][38]. | Do not present the entire dataset as crowdsourced by farmers. |
| **"Hardware goes to zero"** | **REAL only at the margin** | No new farm sensor is required for DTMF/voice and assisted photos. | Phones, towers, servers, surveyor devices, call centres and human verification remain infrastructure. |
| **"WeFarm/Esoko prove farmers will keep contributing"** | **FILLER if used as proof** | They show that SMS/voice can support exchange without mobile internet [21]. | Retrieved evidence does not establish durable retention, causal income gain or a sufficient contributor reward. |
| **Promotional sustainability and vendor pages** | **NOISE** | Useful for discovering vocabulary and candidates. | Excluded as proof where primary, government, investor, academic or operational sources were available. |
| **Unverified scheme blogs and social posts** | **NOISE/BACKUP** | They can reveal a search lead. | BALARAM and e-Chasa claims should come from official guidelines or corroborated reporting, not scheme-aggregator blogs. |
| **Future API, lender and carbon mock-ups** | **DEMO ONLY** | Useful for communicating architecture. | Every screen must say "simulated," "not submitted" or "future partner" as appropriate. |

The noise test is simple: if a source proves only that an organization describes a service, it supports **existence and mechanism**, not retention, impact, fairness or farmer income.

## 7. VERDICT

### Go, but build the evidence-and-doability layer

The winning proposition is not "AI advises farmers" and not "farm data becomes money." It is:

> **A farmer reports what is happening and what they can actually do; the system returns a feasible action immediately and preserves the same report as farmer-controlled evidence for the next institution.**

That proposition is differentiated, buildable and grounded in Odisha's actual rails. Ama Krushi/Krushi Samruddhi provides the low-literacy service pattern, Krushak Odisha provides the farmer backbone, e-Chasa supplies crop-survey context, KCC supplies human escalation, and PMFBY supplies a real evidence workflow [47][5][27][48][2].

### Comparative synthesis

| Layer | Primary mechanism | Scope | Main trade-off | Evidence base | Time horizon |
|---|---|---|---|---|---|
| **Doability-aware advisory** | Constrain actions by household and farm resources. | Immediate disaster action. | More sensitive questions in exchange for more realistic advice. | Strong channel precedents; algorithm still needs validation. | Hackathon -> pilot. |
| **Claim evidence** | Reuse time-, plot- and event-linked farmer reports. | Insured localized/post-harvest loss. | Faster preparation versus fraud, document and adjudication requirements. | Strong PMFBY procedural basis. | Hackathon packet -> year-one official path. |
| **Data cooperative** | Collective rules, granular consent, audit and negotiated value. | Reuse across institutions. | Greater farmer bargaining power versus governance cost and consent fatigue. | Strong JoinData/EU precedent, weak Odisha institutional fit so far. | Design now -> institution later. |
| **Credit visibility** | Consented, provenance-bearing farm history. | Input or productive-asset finance. | Inclusion opportunity versus discrimination, surveillance and debt risk. | Apollo proves plausibility; Juhudi does not validate scoring. | Year-one controlled pilot or later. |
| **Carbon/buyer premium** | Aggregate verified practices and transact with buyers. | Long-horizon secondary income. | Possible revenue versus MRV, aggregation, fees and delayed payment. | Real KACP precedent; incomplete net-benefit evidence. | Later, only with named buyer and fee waterfall. |

The non-obvious tension is that **the data becomes more commercially valuable as it becomes more sensitive**. Doability requires cash, labor and tenure; claims require damage and bank/enrollment details; credit reuses performance histories. A single broad consent would make the loop technically easy and ethically weak. Purpose separation is therefore not a compliance afterthought; it is the product architecture.

A second tension is between title and contribution. The cultivator may generate the observation and bear the loss while the owner controls the registered plot. The product must preserve the cultivator's authorship and evidence access without pretending that it can override land or insurance law. It should surface the conflict to an authorized grievance or scheme process.

A third tension is between zero hardware and reliable proof. Farmer phones remove the cost of installing sensors, but evidence still needs capture guidance, network access, identity resolution, quality checks and human verification. The right claim is **zero new farm hardware for the MVP**, not zero infrastructure or zero operating cost.

### Final decision

**Build the one-day prototype.** Grade the concept **A for advisory plus evidence preparation**, **B for government-rail integration**, **C for credit visibility**, and **C/D for carbon or buyer-premium claims without a named partner**.

The demo should end on three artifacts:

1. A feasible action and cheaper fallback.
2. A farmer-owned evidence receipt and clearly incomplete/complete claim packet.
3. A consent screen showing that advisory, claims, research, credit and buyer sharing are separate choices.

If those three artifacts work in Odia voice with a basic-phone simulation, the project demonstrates something greater than another alert: it shows a governed value loop in which a farmer's contribution produces an immediate return and can, with separate permission, support future institutional value.

## References

1. *EU Code 2018.pdf - FEFAC*. https://fefac.eu/wp-content/uploads/2020/07/eu_code_of_conduct_on_agricultural_data_sharing-1.pdf
2. *OPERATIONAL GUIDELINES - PMFBY*. https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf
3. *Kenya: Agricultural Carbon Project | KYOTO*. https://www.wbkyotofunds.org/projects/kenya-agricultural-carbon-project
4. *Adding value with smallholder data - english.rvo.nl*. https://english.rvo.nl/sites/default/files/2025-11/SPVO-Whitepaper-Adding-value-with-smallholder-data-2025_0.pdf
5. *Krushak Odisha Portal*. https://krushak.odisha.gov.in/
6. *About JoinData - JoinData*. https://join-data.nl/en/about-joindata
7. *Ag Data Coalition – Putting Farmers in the Driver's Seat*. https://agdatacoalition.org/
8. *Eu Code Of Conduct On Agricultural Data Sharing By Contractual Agreement 2020 English*. https://croplifeeurope.eu/wp-content/uploads/2021/03/EU_Code_of_conduct_on_agricultural_data_sharing_by_contractual_agreement_2020_ENGLISH.pdf
9. *CASE STUDY*. https://cdn.prod.website-files.com/63b7bb07476f22ccbab419d5/6593f3490766f1d54510c4e9_Agricultural-Data_CaseStudy_Feb2023.pdf
10. *echasa.odisha.gov.in*. https://echasa.odisha.gov.in/
11. *Krushak Odisha | Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/en/node/124118
12. *Oprational Guidelines*. https://pmfby.gov.in/pdf/Oprational_Guidelines.pdf
13. *Impact By Numbers - Juhudi Kilimo*. https://juhudikilimo.com/impact/by-numbers
14. *Apollo Agriculture | Fund for Rural Prosperity*. https://1.frp.org/agribusiness/apollo-agriculture
15. *Juhudi Kilimo – Acumen*. https://acumen.org/companies/juhudi-kilimo
16. *WINNING303 | Situs Mini Game Slot303 Multi-Server Terbaru 2026*. https://www.divportfolio.org/node/38853
17. *Where Kiva works | Kiva*. https://www.kiva.org/about/where-kiva-works/partners/156
18. *Kenya - Agricultural Carbon Project*. https://documents.worldbank.org/en/publication/documents-reports/documentdetail/812421468041352197
19. *KACP - Vi Agroforestry*. https://www.viagroforestry.org/projects/kacp
20. *Digital Advisory Services For Agriculture – AIM For Scale*. https://aimforscale.org/innovation-packages/digital-advisory
21. *WeFarm | Nesta*. https://www.nesta.org.uk/feature/ai-and-collective-intelligence-case-studies/wefarm
22. *WeFarm - weADAPT*. https://weadapt.org/organisation/wefarm
23. [
									Smallholder Farmers • Digital Farming • Grameen Foundation
						](https://grameenfoundation.org/her-outcomes/digital-farming/develop-skills-and-expertise)
24. *The Mobile Gender Gap Report 2020 | GSMA Intelligence*. https://www.gsmaintelligence.com/research/the-mobile-gender-gap-report-2020
25. *GSMA flags stalled progress on mobile gender gap*. https://www.mobileworldlive.com/gsma/gsma-flags-stalled-progress-on-mobile-gender-gap
26. *ODISHA RAY*. https://www.odisharay.com/pages/single_page.php?id=45110
27. *Odisha Launches e-Chasa App, Portal for Statewide Digital Crop Survey - Odisha Bhaskar English*. https://odishabhaskar.in/odisha/odisha-echasa-digital-agriculture-survey-90616
28. *Esoko - connecting last mile communities with services through digital innovations*. https://www.esoko.com/
29. *Launchin... - Department of Agriculture & Farmers' Empowerment | Facebook*. https://www.facebook.com/agriculture.odisha/posts/launching-the-e-chasa-app-portalnow-farmers-of-odisha-can-easily-access-vital-di/893840352790600
30. *Ghana's Esoko*. https://odimpact.org/case-ghanas-esoko.html
31. *Gender Gap 2024*. https://www.gsma.com/gender-gap-2024
32. *Esoko Market Place*. https://marketplace.esoko.com/home
33. *Accenture Esoko Case Study*. https://civictech.africa/wp-content/uploads/2020/08/Accenture-Esoko-Case-Study.pdf
34. *documents1.worldbank.org*. https://documents1.worldbank.org/curated/en/099108405182220140/pdf/IDU07e951dba0152f0476b09d050d6623569d0db.pdf
35. *The Mobile Gender Gap Report 2023*. https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/blog/the-mobile-gender-gap-report-2023
36. *Odisha launches e-Chasa for digital crop survey*. https://www.newindianexpress.com/states/odisha/2024/Aug/22/odisha-launches-e-chasa-for-digital-crop-survey
37. *Esoko Digital Farmer Service | Science, Technology and Innovation (STI) Portal*. http://sti-portal.fao.org/innovations/esoko-digital-farmer-service
38. *Odisha Pushes for 100% Accuracy in Digital Crop Survey 2025 – Odisha news today, Latest Oriya News Bhubaneswar*. https://www.odishanewstimes.com/2025/09/11/odisha-pushes-for-100-accuracy-in-digital-crop-survey-2025
39. *Farmer Registry*. https://agristack.gov.in/assets/registries/farmerRegistry/farmer_registry_faqs.pdf
40. *Deep Dive into the Kenya Agricultural Carbon Project - Verra*. https://verra.org/deep-dive-into-the-kenya-agricultural-carbon-project
41. *Kenyans Earn First Ever Carbon Credits From Sustainable Farming*. https://www.worldbank.org/en/news/press-release/2014/01/21/kenyans-earn-first-ever-carbon-credits-from-sustainable-farming
42. *Interactive voice response systems for delivering personalized agricultural extension advice to rural farmers*. https://www.extensionjournal.com/uploads/archives/9-2-176-811.pdf
43. *Digital tools for rural agriculture extension: Impacts of mobile‐based advisories on agricultural practices in Southern India - Singh - 2023 - Journal of the Agricultural and Applied Economics Association - Wiley Online Library*. http://onlinelibrary.wiley.com/doi/full/10.1002/jaa2.42
44. *Working Paper 9244 Data For Development Phone System For Ag Advice Ethiopia Oct2020*. http://povertyactionlab.org/sites/default/files/research-paper/working-paper_9244_Data-for-Development-Phone-System-for-Ag-Advice_Ethiopia_Oct2020.pdf
45. *Athey Et Al Sept 2024*. https://precisiondev.org/wp-content/uploads/2025/01/Athey-et-al-Sept-2024.pdf
46. *http://hci.stanford.edu/publications/2010/avaajotalo/chi_talk_patel_4.0.pdf*. http://hci.stanford.edu/publications/2010/avaajotalo/chi_talk_patel_4.0.pdf
47. *http://precisiondev.org/project/ama-krushi*. http://precisiondev.org/project/ama-krushi
48. *http://pib.gov.in/PressReleasePage.aspx?PRID=2201003&lang=1&reg=3*. http://pib.gov.in/PressReleasePage.aspx?PRID=2201003&lang=1&reg=3
49. *http://cdn.cseindia.org/attachments/0.65638100_1587639351_agromet.pdf*. http://cdn.cseindia.org/attachments/0.65638100_1587639351_agromet.pdf
