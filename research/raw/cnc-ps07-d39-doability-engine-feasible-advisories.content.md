# Doability Before Advice: A Feasibility Engine for Odisha

## 1. EXECUTIVE SUMMARY

- **The problem is real, but the product category is new**: Agricultural adoption evidence shows that credit, insurance, labor, training, markets, and risk can block technically correct action. In Rwanda, labor rather than credit or information was the main barrier to irrigation uptake even when inputs were free. The defensible claim is therefore not that a published "doability engine" already exists, but that established constraints justify building and testing one. [5]
- **Odisha already proves that voice advice can work, and also proves its limit**: In an RCT of Ama Krushi covering **13,675 farmers in 902 villages**, access raised average yield by **1.7%** and harvest by **4.1%**, while reducing severe crop-loss incidence by **10%**. Yet it produced no improvement in areas hit by severe Mahanadi flooding in 2022. That failure case is the opening for feasibility-aware action ranking. [16]
- **Basic-phone inclusion should be the primary path, not a fallback**: Avaaj Otalo found that many interviewed farmers did not compose or read SMS, while most could use simple IVR; users also preferred touchtone input over low-grade speech recognition. Build the core loop around outbound voice, DTMF, missed-call callbacks, and short SMS receipts. [21]
- **Farmer-as-sensor is credible in two different forms**: Ama Krushi used hotline questions to detect geographic concentrations of pest and disease reports, while Nuru showed that smartphone images can support diagnosis. Voice/DTMF works on basic phones; photos do not. The pitch must say "no new field hardware for the basic path," not "hardware goes to zero." [16][27]
- **Cash-before-flood is the strongest doability evidence**: WFP sent **BDT 4,500, about US$53, up to four days before critical flooding** to about **145,000 vulnerable people**. Recipients were **36% less likely to go a day without eating**, **12% more likely to evacuate household members**, and **17% more likely to evacuate livestock**. This supports finance-enabled action, but not a clean factorial claim that cash plus advice beats advice alone. [11]
- **Kisan Credit Card is relevant; PM Vishwakarma and PM SVANidhi usually are not**: KCC-credit officially covers cultivation, post-harvest needs, household consumption, asset maintenance, and investment, including tenant farmers, oral lessees, sharecroppers, SHGs, and JLGs. PM Vishwakarma is limited to listed artisan trades, and PM SVANidhi to urban street vending. Eligibility must be checked, not inferred from being a farmer. [19][17][13]
- **Claims evidence is useful but not self-executing**: PMFBY allows mobile-app crop-loss pictures as evidence, but localized-loss claims still require intimation within **72 hours**, survey-number and acreage details, documents, premium verification, and joint assessment. The product can create an evidence packet and reminder; it cannot promise claim acceptance. [20]
- **Collective action needs an orchestration layer, not merely group messages**: Odisha has village-level cyclone/flood shelter management committees as an institutional precedent, but the sourced material does not demonstrate that a new advisory group can successfully organize drainage or bund work. Shared actions require a named owner, authority, committed labor, completion confirmation, and government escalation. [12]
- **The MVP algorithm should be deterministic and auditable**: Filter unsafe, inapplicable, unaffordable, unauthorized, and deadline-infeasible actions first; then solve a small multi-resource selection problem that maximizes expected realized benefit. Constrained contextual bandits are a later research option because high-probability safety requires a known safe action and reliable cost feedback from the first round. [3]
- **Verdict**: A feasibility-first advisory engine is defensible and buildable as human-supervised decision support. The winning scope is IMD-triggered action libraries, progressive DTMF profiling, hard feasibility gates, explainable ranking, collective escalation, and PMFBY evidence packaging. Automatic credit, automatic scheme eligibility, automatic claims, unsafe AI exploration, and zero-hardware claims are not defensible today. [5][15]

## 2. INVENTORY

### Grading rule

**A** means direct causal evidence or an official mechanism that fits the proposed workflow. **B** means credible and useful, but adjacent, dated, or not yet validated as an integrated doability feature. **C** means promising precedent with important channel, outcome, or interoperability gaps. **D** means materially mis-scoped for ordinary crop farmers or unsupported as pitched.

| Item | What | Mechanism | Named source, URL and date | Scale/status | Feasibility for basic-phone farmers | Grade |
|---|---|---|---|---|---|---|
| Adoption-barrier evidence | Explains why correct advice is not enough | Credit, savings, insurance, labor, market access, infrastructure, and risk alter whether an action can be adopted | World Bank, *Adoption of Agricultural Technologies by Smallholder Farmers*, `https://documents1.worldbank.org/curated/en/099092925141086193/pdf/P500443-c5c1ae72-ed75-442e-885c-7ced9e0bb0ea.pdf`, July 2025 | Broad evidence synthesis; includes randomized and observational studies, so causal strength varies | Directly supports a short resource profile; it does not dictate the interface | A [5]
| Ama Krushi RCT | Odisha voice advisory and closest local comparator | Weekly recorded calls, hotline questions, agronomist replies, local weather and agronomy content | Precision Development, `https://precisiondev.org/customized-digital-advice-can-help-farmers-reduce-crop-loss-and-manage-weather-shocks-a-summary-or-as-much-as-we-can-summarize`, Feb. 26, 2025 | RCT: 13,675 farmers, 902 villages; 2021-2022 Kharif; 1.7% higher yield, 4.1% higher harvest, 10% lower severe-loss incidence | Strong: recorded calls and callback hotline; no smartphone required | A [16]
| Ama Krushi operating model | Shows government-scale voice delivery can survive handoff | Customized two-way service expanded to call center, radio, and in-person channels | PxD, *Ama Krushi Transition Insights Report*, `https://precisiondev.org/wp-content/uploads/2025/02/AK-transition-report-BMGF_condensed.pdf`, July 2023 | More than 5M farmers reached by June 2023; government-owned after June 2022; incremental user cost reported below US$0.22/year at scale | Strong for voice; operating quality and iteration slowed after transition | B [25]
| Avaaj Otalo | Field precedent for low-literacy, two-way farmer voice | Record a question, answer, browse Q&A; use DTMF for menu selection | Patel et al., *Avaaj Otalo*, `https://tap2k.org/papers/pap0310-patel.pdf`, 2010 | Extended rural India field study; influential but old and not disaster-specific | Very strong: phone access, voice content, DTMF; better fit than text-heavy UX | B [21]
| FarmerChat | Modern multimodal advisory baseline | Voice/text/photo input; RAG and expert-validated data; local-language output | Digital Green, `https://digitalgreentrust.org/farmerchat`, undated, accessed Aug. 16, 2026 | Public page reports 1.6M+ queries and 900K+ farmers helped; no causal evaluation or resource-feasibility rank is presented on the cited page | Voice/text can fit low connectivity; photos and app functions require a smartphone | C [23]
| Farmer photo sensing | Shows that hands and a phone can collect diagnostic observations | On-device image classification and guidance | Mrisho et al., PlantVillage Nuru preprint, `https://www.biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf`, Jan. 30, 2020 | Tested on 90 cassava plants; six-leaf accuracy 74-88%, but the paper is a non-peer-reviewed preprint | Weak for basic phones: Android, at least 2 GB RAM, about US$100-US$150; diagnosis can work offline | C [27]
| Low-friction constraint profile | Gives established categories for labor and household economics | Reuse small subsets of demographic, consumption, assets, debt, and advice-access questions | Government of India Microdata Library, *Situation Assessment Survey of Agricultural Households*, `https://microdata.gov.in/NADA/index.php/catalog/134`, 2013 survey; metadata 2015 | National survey instrument, not a real-time service; migration, tenancy, and group membership were not visible in the cited module list | Good only if converted to event-specific DTMF bands; copying a long survey would fail | B [4]
| Constraint-aware optimizer | Formal basis for ranking under reward and cost constraints | Hard feasibility set plus constrained optimization; later, a safe contextual bandit | Pacchiano et al., *Contextual Bandits with Stage-wise Constraints*, `https://www.jmlr.org/papers/volume26/24-0267/24-0267.pdf`, Aug. 2025 | Formal ML framework, not an agricultural deployment | Channel-neutral; result can be explained in one voice sentence | B [3]
| KCC-credit | Relevant farm liquidity rail | Revolving/flexible credit for cultivation, post-harvest, consumption, maintenance, and investment | PIB, *Kisan Credit Card*, `https://www.pib.gov.in/FactsheetDetails.aspx?Id=148600&lang=2&reg=3`, Jan. 17, 2022 | Official scheme; source reported more than 1.5 crore farmers and Rs 1.35 lakh crore sanctioned at that date | Discovery and reminders work by IVR; actual approval/disbursement is bank-dependent and not instant | A [19]
| PMFBY localized-loss workflow | Converts observations into a structured insurance support packet | 72-hour loss notice, claim form, plot/acreage details, pictures and external reports, then joint assessment | MoAFW, *Revised PMFBY Operational Guidelines*, `https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf`, revised edition undated in extract, accessed Aug. 16, 2026 | Official workflow for insured notified crops and covered perils | Good for voice reminders and toll-free reporting; photo evidence needs a camera phone or assisted agent | A [20]
| WFP anticipatory cash | Strongest evidence that resources before impact change behavior | Forecast trigger -> mobile-money transfer plus early warning before flood peak | Centre for Disaster Protection/WFP, *Acting Before a Flood to Protect the Most Vulnerable*, `https://www.anticipation-hub.org/Documents/Analysis/An_Independent_Review_of_WFPs_Anticipatory_Cash_Transfers_in_Bangladesh.pdf`, Aug. 2021 | About 145,000 people; evaluation data from more than 9,000 households | Warning can be voice/SMS, but payment requires an enrolled financial account and pre-arranged fund | A [11]
| Odisha shelter committees | Local precedent for assigning disaster tasks to community institutions | Village-level cyclone/flood shelter management and maintenance committees | OSDMA, `https://www.osdma.org/preparedness/multi-purpose-cyclone-flood-shelters/cs-fsmmc`, undated, accessed Aug. 16, 2026 | Real institution; cited page establishes CSMMC/FSMMC, not a causal outcome for farm drainage | Group voice trees are feasible; authority and completion still require local owners | C [12]
| PM Vishwakarma | Useful only for farmers who separately practice an eligible trade | Training, toolkit grant, and collateral-free enterprise loans for 18 traditional artisan trades | PM Vishwakarma portal, `https://pmvishwakarma.gov.in/`, accessed Aug. 16, 2026 | Official artisan scheme; cultivation is not one of the listed trades | Eligibility screening can be DTMF, but default farmer routing would mislead | D [17]
| PM SVANidhi | Useful only when the user is an eligible urban street vendor | Collateral-free working-capital loan and interest subsidy | MoHUA, `https://mohua.gov.in/pm_svandhi/guidelines.pdf`, June 1, 2020 | Official street-vendor scheme; first loan up to Rs 10,000 in the cited guidelines | Voice screening is feasible; cultivation alone does not qualify | D [13]
| Data protection | Governs constraint and evidence profiles | Plain-language notice, specific consent, necessary-data limit, withdrawal, security, erasure and grievance | India Code, *Digital Personal Data Protection Act, 2023*, `https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf`, Act 22 of 2023, text as on Nov. 19, 2025 | Binding legal baseline; implementation details also depend on applicable rules and notifications | Consent and grievance must be available in the same accessible language/channel as collection | A [15]

### Case study 1: Ama Krushi shows both the ceiling and the gap

Ama Krushi already did much of what a message-first entrant would propose. Farmers received 45-50 advisory calls in a season; **94% in Year 1 and 85% in Year 2** listened to at least one. The platform also used clusters of incoming pest and disease questions to localize outgoing advice. That is a genuine farmer-as-sensor feedback loop, not merely a broadcast list. [16]

The RCT nevertheless supplies the most important negative result: no measured improvement in the severe 2022 Mahanadi flood area. The report does not establish whether the binding cause was labor, liquidity, physical impossibility, warning lead time, or action quality, so the result does not prove the proposed mechanism. It does show why optimizing comprehension and agronomic relevance alone can be insufficient. The product implication is to preserve Ama Krushi's proven voice architecture but insert a resource-and-deadline decision layer before choosing the message. [16]

### Case study 2: WFP Bangladesh converts warning time into action capacity

WFP's 2020 activation did not merely describe a coming flood. It transferred BDT 4,500 through mobile money as early as four days before waters became critical. The measured outcomes included more evacuation of people and livestock and lower small-livestock and poultry loss, alongside better food security. That is the clearest mechanism in this evidence base: forecast lead time has value when a household receives a usable resource before the deadline. [11]

The limit matters. The evaluation supports an anticipatory cash package, not a three-arm trial of advice only versus cash only versus cash plus advice. Odisha should therefore treat "cash plus advice beats advice alone" as a pilot hypothesis. The engine can flag a finance gap and route a pre-enrolled farmer to an approved facility, but it cannot manufacture an instant KCC loan or WFP-style transfer.

### Case study 3: Photos can support a claim, but cannot become the claim

Nuru demonstrates the promise and cost of photo sensing. Under one six-leaf protocol, its 74-88% accuracy was similar to trained researchers and above the tested extension-agent and farmer groups. Yet it required an Android phone with at least 2 GB RAM, its preprint was not peer reviewed, and some tests and co-infected plants exposed weaker performance. A phone camera is therefore an optional assisted channel, not the universal interface. [27]

PMFBY makes the distinction operational. A crop-loss picture may be evidence, but the farmer must still notify within 72 hours, identify the insured crop and affected acreage, submit required documents, and participate in an assessment. The product should timestamp, geotag where consented, hash, and package evidence, while saying clearly: "This supports your report; it does not guarantee acceptance." [20]

## 3. COVERAGE TABLE

| Required capability | Evidence coverage | What can be built now | Unresolved gap | Coverage grade |
|---|---|---|---|---|
| Show that feasibility blocks adoption | Strong synthesis and several trials identify labor, liquidity, credit, insurance and market constraints | Resource-aware profile and action gates | No trial of this exact integrated engine in Odisha | A [5]
| Low-literacy basic-phone delivery | Avaaj field evidence and Odisha's Ama Krushi voice operation | Outbound IVR, DTMF replies, missed-call callback, recorded expert answer, SMS receipt | Modern testing across Odia dialects, disability and shared-phone use | A [21][16]
| Hyperlocal farmer sensing | Ama Krushi aggregates hotline reports; FarmerChat and Nuru accept richer inputs | DTMF status reports, voice notes through an assisted line, optional smartphone photo | Fraud, duplicate reports, geolocation error and image quality | B [16][23][27]
| Labor and liquidity profile | Adoption literature and NSS modules identify relevant categories | Small event-time bands for available labor, spendable cash, tools, transport and authority | Validity of self-report under stress; profile staleness | B [5][4]
| Tenancy and decision authority | KCC-credit and PMFBY officially recognize some tenants/sharecroppers | Ask "Can you authorize work on this plot?" separately from land ownership | Documentary proof, landlord consent and local variation | B [19][20]
| Multi-constraint ranking | Mature optimization concepts and safe-constraint research exist | Deterministic filter plus multi-resource knapsack/precedence solver | Local action cost, duration and benefit estimates | B [3]
| Anticipatory finance | Strong Bangladesh evidence for pre-flood cash | Detect a binding cash gap; route only pre-approved/available funds | No Odisha rail promising immediate disbursement at alert time | A for principle, C for Odisha rail [11]
| KCC-credit linkage | Officially relevant to cultivation and tenant groups | Eligibility pre-screen, document checklist, bank callback, pre-season onboarding | Approval latency; no evidence that a new application clears before a cyclone | B [19]
| PMFBY evidence and loss reporting | Detailed official workflow | 72-hour timer, hotline handoff, plot/evidence packet, assessor appointment reminders | API acceptance, insurer integration and evidentiary weight | A [20]
| Collective drainage/bund action | OSDMA provides a committee precedent | Group call tree, named coordinator, pledge/confirmation, escalation | Weak direct outcome evidence for farm-drainage coordination; authority ambiguity | C [12]
| Automatic scheme eligibility | Role-specific rules can be encoded | Conservative pre-screen with "possibly eligible" result | Authoritative registry and consented verification | C [17][13]
| Responsible data use | DPDP provides a clear baseline | Purpose-specific consent, minimal fields, retention limits, withdrawal and grievance | Exact operational roles and notified requirements for every partner | B [15]

**Coverage takeaway:** The communication, need, finance principle, official credit/insurance rules, and optimization mechanics are sufficiently grounded for a pilot. The weakest cells are instant liquidity, collective-action outcomes, claims interoperability, and automatic eligibility. Those should be partner-dependent experiments, not launch claims.

## 4. WHAT IS MISSING

1. **A direct doability trial.** No located study randomizes farmers between correctness-ranked and feasibility-ranked cyclone advice. Ama Krushi establishes that localized voice advice can improve outcomes and that severe flooding can erase those gains, but it does not identify the binding resource or test the proposed ranker. [16]

2. **A clean cash-plus-advice comparison.** WFP's Bangladesh evidence is strong for an anticipatory transfer package, yet it does not separately estimate advice-only, cash-only, and combined arms in the cited review. The pitch should say "pre-flood cash enabled protective behavior," not claim a proven universal interaction effect. [11]

3. **A validated Odisha action library.** The optimizer needs, by crop stage and hazard severity, a vetted set of actions with labor-hours, elapsed time, cash cost, tools, decision rights, dependencies, safe operating conditions, expected avoided loss, and fallback variants. These numbers cannot be generated safely by an LLM. The literature specifically warns that high upfront labor or capital and delayed returns can block adoption. [5]

4. **A truthful, fresh capacity signal.** Family size is not labor available before 18:00; a KCC account is not spendable liquidity; landholding is not decision authority; and group membership is not committed collective labor. The profile therefore needs static facts plus event-time checks. The NSS instrument supports demographic, expenditure, asset and indebtedness categories, but its cited catalog does not expose migration, tenancy or group-membership modules for direct reuse. [4]

5. **An instant finance rail.** KCC-credit is relevant but approval, documentation and disbursement are bank processes. PM Vishwakarma and PM SVANidhi cannot fill the general farmer gap. A defensible pilot must pre-enroll eligible farmers before cyclone season or partner with an authority that can pre-commit grant/cash triggers. [19][17][13]

6. **Claims-system interoperability.** PMFBY pictures are permitted evidence, not automatic claim decisions. Missing pieces include insurer/API acceptance, identity and policy matching, tamper handling, offline timestamps, chain of custody, and consented sharing. [20]

7. **Evidence for village work allocation.** OSDMA committees show that Odisha uses local institutions for disaster management, but the sourced evidence does not quantify whether advisory-created groups can mobilize labor for private drains, shared drainage, or bund maintenance. A pilot must distinguish private action, neighbor coordination, and public works that require panchayat or department authority. [12]

8. **Voice reliability under real farm noise.** Agricultural voice data include background talk as a dominant condition, while the older Avaaj study found touchtone more usable than low-grade speech recognition. DTMF should carry decisions; free speech should be transcribed for a human queue until dialect-specific accuracy is demonstrated. [22][21]

9. **Equity and privacy safeguards.** Shared phones, women's control of phones, tenants, migrants, debt sensitivity, and disability can all distort a resource profile. DPDP requires plain-language notice, specific and necessary data, and consent withdrawal that is as easy as giving consent. Nonresponse must remain "unknown," never "no capacity" or "ineligible." [15]

10. **Outcome evidence beyond engagement.** Listening, DTMF completion and photos submitted are intermediate metrics. The pilot needs preregistered measures of action completion, time to action, avoided loss, unsafe recommendations, grievance resolution, exclusion errors, and differential outcomes by gender, tenancy and phone type. Ama Krushi's self-reported profit measure had large variance, illustrating why objective and administrative outcomes matter. [16]

## 5. HOW IT FEEDS THE PRODUCT

### Product architecture: from alert to executable plan

| Evidence or constraint | Product feature | Executable rule |
|---|---|---|
| Labor and cash can bind adoption | **Event-time Doability Check** | Ask only variables that can change today's ranking: helpers available, cash spendable now, transport/tool access, and work authority [5] |
| Voice/DTMF fits low literacy | **Two-minute IVR branch** | Use DTMF for categorical decisions; replay and confirm; send SMS only as a receipt [21] |
| Farmer reports can localize advice | **Farmer Signal Queue** | Aggregate repeated DTMF/voice reports by village, crop, time and symptom; require expert review before changing agronomy [16] |
| Photo sensing has value but device cost | **Optional Assisted Photo** | Offer to smartphone users or village agents; never make a photo mandatory for receiving safety advice [27] |
| PMFBY has a 72-hour workflow | **Claim Evidence Pack** | Start timer, capture plot/crop/acreage and consented media, hand off to official channel, track acknowledgement [20] |
| KCC-credit fits agriculture | **Pre-season Finance Readiness** | Check account/limit/documents before hazard season; at alert time count only confirmed spendable credit [19] |
| Artisan/vendor schemes are narrow | **Scheme Guardrail** | Route to PM Vishwakarma only after eligible-trade confirmation and to PM SVANidhi only after street-vendor confirmation [17][13] |
| Shared work requires coordination | **Village Action Board** | Create a task only with owner, authority, required labor, pledges, deadline, completion proof and escalation path [12] |
| High-stakes learning needs safety | **Human-approved Safe Baseline** | Do not explore untested actions; learn only among pre-approved variants and retain a known safe fallback [3] |
| Constraint data are sensitive | **Purpose-bound Profile** | Explain each question, store bands rather than exact wealth where possible, expire event fields, support voice withdrawal and grievance [15] |

### Encode constraints without turning onboarding into an interrogation

Use a **two-speed profile**.

- **Stable layer, collected progressively:** language/dialect; village; crops and approximate area; phone type; preferred call time; owner/tenant/sharecropper; who can authorize work; insured crop/policy reference; existing KCC-credit, SHG/JLG/FPO or trusted group; usual access to pump, tarpaulin, transport and storage.
- **Event layer, asked only after a trigger:** crop stage and condition; standing, cut or stored status; labor-hours available before the deadline; amount spendable now in broad bands; whether an existing credit balance is immediately usable; water depth or access route; tool/transport availability; willingness to join a named group task.
- **Derived fields:** timestamp, confidence, source, expiry, contradiction flag, and whether the answer came from farmer, agent, sensor or administrative record.

The interaction rule is: **ask a question only when different answers can change the top action or escalation**. For example: "Before 6 PM, how many people can work? Press 1 for only me, 2 for two people, 3 for three or more, 9 if unsure." Do not ask exact income, full debt or title history during an emergency. Reuse known facts, read them back, and let the farmer correct them.

### The ranking math

For farmer or plot `f`, event `t`, and approved action `i`, define:

- `a_i`: agronomic and hazard applicability, either 0 or 1.
- `s_i`: safety approval, either 0 or 1.
- `r_i = (labor_hours, cash_now, elapsed_time, tools, transport, authority)`: resources required.
- `b_ft`: resources actually available before the deadline, with unknown values represented explicitly.
- `p_do(i|f,t)`: estimated probability the farmer can complete the action on time.
- `p_effect(i|h)`: probability the completed action works under hazard scenario `h`.
- `L_i`: avoidable loss if it works.
- `C_i`: out-of-pocket and opportunity cost.
- `R_i`: residual safety, exclusion, or evidence-risk penalty.

The expected realized value is:

`V_i = a_i * s_i * [p_do(i|f,t) * p_effect(i|h) * L_i - C_i - lambda * R_i]`

Select a set of actions `x_i in {0,1}`:

`maximize sum_i x_i * V_i`

subject to:

`sum_i x_i * labor_i <= labor_available_before_deadline`

`sum_i x_i * cash_i <= cash_spendable_before_deadline`

`finish_time_i <= hazard_deadline`

`x_i <= authority_i`

`x_i <= each required predecessor`

Life-safety actions do not compete with crop economics: evacuation and official safety instructions occupy a higher priority class. Unknown capacity lowers confidence and triggers a short question or a conservative fallback; it must not be silently treated as zero.

For the MVP, `p_do` should come from transparent rules and conservative bands. After enough consented outcome data exist, a calibrated logistic model can estimate it from labor slack, cash slack, deadline slack, prior completion, distance and tool access. A constrained contextual bandit is only a later option: the formal literature requires a known safe action and high-probability cost compliance, conditions that ordinary advisory experimentation may not meet. [3]

### Worked example: "harvest by 18:00, no labor"

The following values are **illustrative product-test data, not agronomic prescriptions**. The farmer has 6 labor-hours, Rs 600 spendable, and authority over the plot.

| Candidate action | Labor | Cash | Modeled avoided-loss points | Gate result |
|---|---:|---:|---:|---|
| Harvest the full plot | 16 h | Rs 1,600 | 100 | Reject: labor and cash infeasible |
| Prioritize the most exposed quarter | 5 h | Rs 400 | 45 | Feasible |
| Clear a private outlet | 2 h | Rs 100 | 18 | Feasible alone, but conflicts with the 5 h action |
| Move stored inputs above water | 1 h | Rs 0 | 8 | Feasible |

A correctness-only system may rank full harvest first and stop. The constrained set optimizer chooses "prioritize exposed quarter" plus "move stored inputs," consuming all 6 labor-hours and Rs 400 for 53 modeled points. If the farmer changes the answer to 2 labor-hours, the engine recomputes rather than repeating an impossible instruction. If local experts mark any action unsafe under wind or lightning, `s_i=0` removes it regardless of benefit.

### Collective-action rule

For shared action `j`, require:

`committed_labor_j >= required_labor_j`

`named_authority_j = true`

`safe_window_j = true`

`completion_confirmations_j >= threshold_j`

If any condition fails, do not tell each household "clear the village drain." Escalate one structured request to the named committee, panchayat or department, inform affected farmers that escalation occurred, and offer private fallback actions. This converts group messaging into accountable orchestration.

### Feedback and evidence loop

1. Ingest the official alert and map affected villages and deadlines.
2. Retrieve approved actions by crop, stage, hazard and locality.
3. Run hard safety/applicability gates.
4. Ask the minimum DTMF questions needed to resolve rank-changing unknowns.
5. Optimize the action bundle and state why the top choice fits: "This option needs one person, no cash, and can finish before 6 PM."
6. Collect `started`, `completed`, `could not do`, and a reason code. Voice/photo goes to a review queue.
7. Build a separate, consented evidence packet for PMFBY or finance readiness. Never reuse emergency answers for lending or eligibility without a new specified purpose.
8. Update completion estimates only after monitoring bias, shared-phone error, and exclusion by gender/tenancy.

## 6. REAL-vs-FILLER + NOISE LOG

| Pitch claim or source signal | Classification | Why | Product decision |
|---|---|---|---|
| Advice can improve farmer outcomes | **REAL** | Ama Krushi's randomized rollout reported modest average yield/harvest gains and lower severe-loss incidence [16] | Preserve personalized voice advice |
| Correct advice can fail under extreme conditions | **REAL, mechanism not identified** | Ama Krushi showed no improvement in severe 2022 Mahanadi flooding, but did not isolate labor or cash as the cause [16] | Ask and test binding constraints; do not claim proof yet |
| Labor, liquidity and credit affect adoption | **REAL** | Evidence synthesis includes labor as a primary barrier in one irrigation case and gains from savings/credit in others [5] | Hard resource gates and pre-season finance readiness |
| "PxD feasibility testing" is an established named engine | **FILLER AS STATED** | Located PxD evidence covers testing and customized advice, not a published multi-constraint doability ranker | Cite Ama Krushi accurately; present this engine as the proposed innovation |
| Farmer reports can improve hyperlocal awareness | **REAL** | Ama Krushi used geographic concentrations of hotline questions to shape pest/disease advice [16] | DTMF/voice signal aggregation with expert review |
| Farmer photos eliminate field hardware | **PARTLY REAL, OVERSTATED** | Nuru works offline but needs an Android phone with at least 2 GB RAM; compatible phones were estimated at US$100-US$150 [27] | Say "no new dedicated sensor for the basic path" |
| One photo automatically becomes a PMFBY claim | **FILLER** | Pictures are only one permissible evidence type inside a timed, documented, assessed process [20] | Evidence pack plus official handoff, no acceptance promise |
| The same profile automatically creates credit visibility and scheme eligibility | **FILLER** | Each program has legal eligibility and documentation rules; farmer status alone does not qualify for artisan or vendor schemes [19][17][13] | Conservative pre-screen and explicit consented verification |
| KCC-credit can make urgent action affordable | **CONDITIONAL** | It is relevant farm credit, including for tenants and groups, but the cited source does not establish same-day emergency approval [19] | Count only a confirmed available balance at alert time |
| PM Vishwakarma is a general farmer finance route | **FILLER** | Cultivation is absent from its 18 eligible artisan trades [17] | Show only after trade confirmation |
| PM SVANidhi is a general rural livelihood loan | **FILLER** | The scheme is for eligible urban street vendors, including some vendors from surrounding areas who vend within ULB limits [13] | Show only after vending-status confirmation |
| Cash plus advice is proven superior to advice alone | **TOO STRONG** | Bangladesh shows beneficial anticipatory cash-package outcomes, not a cited factorial comparison [11] | Phrase as an evidence-backed hypothesis for Odisha |
| Group messaging will solve bund/drainage coordination | **FILLER WITHOUT GOVERNANCE** | OSDMA committees are a useful precedent, but task ownership, authority, free-riding and outcome evidence remain unresolved [12] | Require pledges, named owner, threshold and escalation |
| AI should learn the best action online | **FILLER FOR MVP** | Safe constrained bandits need a known safe action and cost information; trying an unsafe action to learn its cost is unacceptable [3] | Deterministic, expert-approved library first |
| FarmerChat scale proves impact | **NOISY** | Its page reports usage and satisfaction-style figures but provides no causal evaluation or feasibility rank on the cited page [23] | Treat as capability precedent, not impact proof |

**Noise takeaway:** The durable story is narrower and stronger than the pitch: farmer-generated voice/DTMF data can expose constraints; an explainable optimizer can choose an executable action; optional media can support an evidence packet; and pre-arranged finance or collective capacity can unlock otherwise impossible actions. Data reuse, finance, claims and eligibility remain separate consented workflows with separate authorities.

## 7. VERDICT - SYNTHESIS

### Comparative synthesis

| Strategy | Mechanism | Scope and time horizon | Evidence base | Main trade-off |
|---|---|---|---|---|
| Ama Krushi message-first advisory | Localized recorded advice and hotline feedback | Seasonal agronomy and weather response | Odisha RCT plus large operating history | Scales cheaply, but does not explicitly solve immediate labor/cash infeasibility [16][25] |
| Proposed feasibility-first engine | Hard gates plus expected-realized-value optimization | Hours to days around a hazard; later recovery | Strong component evidence, no integrated field trial | More executable advice, but requires reliable resource and action-cost data |
| WFP anticipatory finance | Forecast trigger plus pre-arranged mobile cash and warning | Days before flood impact | High-quality independent evaluation | Powerful enabling resource, but requires funding, enrollment and payment rails [11] |
| Nuru/photo sensing | Smartphone image classification | Immediate field diagnosis and evidence capture | Small field evaluation and non-peer-reviewed preprint | Rich observation, but excludes many basic-phone users and can misclassify [27] |
| OSDMA-style community institution | Named village committee and maintenance responsibility | Preparedness and shared disaster tasks | Official institutional precedent; thin outcome evidence in sourced material | Can coordinate public goods, but authority and free-riding cannot be solved by messaging alone [12] |
| PMFBY/KCC-credit linkage | Official insurance and credit workflows | Pre-season readiness through post-loss recovery | Official rules | Real rails, but neither is an automatic real-time entitlement [19][20] |

The non-obvious tension is that the most inclusive channel carries the least data. DTMF and IVR reach basic-phone users but provide coarse signals; photos and app telemetry improve observation but introduce device, consent and quality barriers. The right architecture is therefore not app-first or IVR-only. It is an IVR decision core with optional assisted sensing, where richer data may improve confidence but never determine access to safety advice.

A second tension is between personalization and fairness. More financial, tenancy and behavioral data can improve feasibility estimates, yet the same data can stigmatize, exclude, or be repurposed for credit decisions. The engine should optimize with broad bands and uncertainty, while banks, insurers and schemes make their own authoritative decisions under separately consented workflows. DPDP's specified-purpose and necessary-data principles support that separation. [15]

### Final verdict

**Defensible:** Yes, as an evidence-informed hypothesis and a human-supervised decision-support system. The core insight is mathematically sound: realized value equals technical value multiplied by the probability that the farmer can complete the action before the deadline. Labor, cash, tools, transport, authority and collective commitments belong in the objective and constraints, not in an afterthought.

**Buildable now:** Yes, for an MVP containing an approved action library, IMD-trigger handling, stable plus event-time profiles, DTMF/IVR, hard safety and feasibility filters, a small constrained optimizer, explanations, completion feedback, group escalation, and PMFBY evidence packaging. Ama Krushi demonstrates a large-scale Odisha voice channel; Avaaj supports DTMF usability; PMFBY and KCC-credit provide real official workflows. [25][21][19][20]

**Not buildable as promised without partners:** Instant anticipatory cash, bank credit approval, official scheme determination, insurer acceptance, and public-works mobilization. These require pre-arranged agreements, funds, identity/policy matching, and accountable authorities. WFP's results came from an operational financing mechanism, not from better ranking alone. [11]

**Pilot decision:** Proceed, but test the central causal claim. Compare the approved current advisory with feasibility-ranked variants; preregister action completion and loss outcomes; log why actions fail; audit by gender, tenancy and phone type; and prohibit online exploration outside the safe action library. Scale only if the engine raises timely completion without increasing unsafe advice or exclusion. The honest winning line is:

> **Do not send the most correct action in the abstract. Send the safest high-value action this farmer, household, or village can complete before the hazard - and show the next-best fallback when they cannot.**

## References

1. *CROPIC*. https://pmfby.gov.in/cropic
2. *Anticipatory Action for climate shocks | World Food Programme*. https://www.wfp.org/anticipatory-actions
3. *Contextual Bandits with Stage-wise Constraints*. https://www.jmlr.org/papers/volume26/24-0267/24-0267.pdf
4. *India - Situation Assessment survey of Agricultural households,  NSS 70th Round : Jan - Dec 2013 : Visit 2*. https://microdata.gov.in/NADA/index.php/catalog/134
5. *World Bank Document*. https://documents1.worldbank.org/curated/en/099092925141086193/pdf/P500443-c5c1ae72-ed75-442e-885c-7ced9e0bb0ea.pdf
6. *Reserve Bank of India*. https://www.rbi.org.in/commonman/english/scripts/Notification.aspx?Id=2311
7. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. https://www.pmfby.gov.in/
8. *Acting Before a Flood to Protect the Most Vulnerable: An Independent Review of WFP’s Anticipatory Cash Transfers in Bangladesh | World Food Programme*. https://www.wfp.org/publications/acting-flood-protect-most-vulnerable-independent-review-wfps-anticipatory-cash
9. *PlantVillage Nuru: Pest and disease monitoring using AI - CGIAR Platform for Big Data in Agriculture*. https://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai
10. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | DM and Preparedness*. https://www.osdma.org/
11. *Acting Before a Flood to Protect the Most Vulnerable*. https://www.anticipation-hub.org/Documents/Analysis/An_Independent_Review_of_WFPs_Anticipatory_Cash_Transfers_in_Bangladesh.pdf
12. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Multi Purpose Cyclone/Flood Shelters*. https://www.osdma.org/preparedness/multi-purpose-cyclone-flood-shelters
13. *Pm Svandhi*. https://mohua.gov.in/pm_svandhi/guidelines.pdf
14. *PlantVillage*. https://plantvillage.psu.edu/
15. *The Digital Personal Data Protection Act, 2023*. https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf
16. *Customized Digital Advice Can Help Farmers Reduce Crop Loss and Manage Weather Shocks: A Summary (or as Much as We Can Summarize!) - Precision Development*. https://precisiondev.org/customized-digital-advice-can-help-farmers-reduce-crop-loss-and-manage-weather-shocks-a-summary-or-as-much-as-we-can-summarize
17. *PM Vishwakarma*. https://pmvishwakarma.gov.in/
18. [
	Press Release: Press Information Bureau
](https://pib.gov.in/PressReleaseIframePage.aspx?PRID=1963799)
19. [
	Factsheet Details:Factsheet Details | PIB
](https://www.pib.gov.in/FactsheetDetails.aspx?Id=148600&lang=2&reg=3)
20. *Revised Operational Guidelines*. https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf
21. *http://tap2k.org/papers/pap0310-patel.pdf*. http://tap2k.org/papers/pap0310-patel.pdf
22. *http://arxiv.org/html/2602.03868v1*. http://arxiv.org/html/2602.03868v1
23. *http://digitalgreentrust.org/farmerchat*. http://digitalgreentrust.org/farmerchat
24. *Impact Evaluation of Ama Krushi – PxD Experiment Registry*. https://registry.precisiondev.org/registry_entry/impact-evaluation-of-digital-extension-platform
25. *Ama Krushi Transition Insights Report*. https://precisiondev.org/wp-content/uploads/2025/02/AK-transition-report-BMGF_condensed.pdf
26. *AGROMET ADVISORY SERVICES | India Meteorological Department*. https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php
27. *biorxiv.org*. https://www.biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf
28. *Realizing the potential of digital development: The case of agricultural advice | Science*. https://www.science.org/doi/10.1126/science.aay3038
29. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | CSMMC*. https://www.osdma.org/preparedness/multi-purpose-cyclone-flood-shelters/cs-fsmmc
30. *Realizing the potential of digital development: The case of agricultural advice - PubMed*. https://pubmed.ncbi.nlm.nih.gov/31831641/
