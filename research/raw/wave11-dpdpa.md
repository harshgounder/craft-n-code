## executive_summary_decisions_a_team_has_to_make_today

- **Rules are notified, enforcement is staged**: The Digital Personal Data Protection Rules, 2025 were notified on **14 November 2025** [executive_summary_decisions_a_team_has_to_make_today[0]] [1][executive_summary_decisions_a_team_has_to_make_today[1]] [2]; compliance rolls out in three phases of 6, 12 and 18 months from notification, so obligations begin activating from **mid-May 2026** [executive_summary_decisions_a_team_has_to_make_today[2]] [4]. **Action**: build against the 18-month Phase-3 endpoint, not "Day 1 DPDPA".
- **Penalty ceiling is real and dy- to half-a-billion rupees**: Up to **Rs 250 crore / breach item** on the Schedule, with **Section 33(3) multiplier up to Rs 500 crore** for aggravating factors (repetition, gain realised, mitigation failure) [executive_summary_decisions_a_team_has_to_make_today[3]] [6][executive_summary_decisions_a_team_has_to_make_today[4]] [7]. **Action**: any product feature that touches personal data needs a documented controls matrix, because the Section 33(2) factors are what the Data Protection Board will score [executive_summary_decisions_a_team_has_to_make_today[3]] [6].
- **DPB is being stood up, not yet visible**: MeitY advertised **Chairperson and Member** posts on **6 May 2026**; full Board has four members per PIB notification [executive_summary_decisions_a_team_has_to_make_today[5]] [8][executive_summary_decisions_a_team_has_to_make_today[6]] [9]. **Action**: cite the live complaint mechanism from the dpb-complaint-process reference, not "case law".
- **Breach clock is 72 h, not 6 h**: Under DPDPA **Section 8 / Rule 12** data fiduciaries notify the **Data Protection Board of India (DPBI)** within **72 hours** of becoming aware [executive_summary_decisions_a_team_has_to_make_today[7]] [3]. **Action**: build a `/breach-notify` endpoint that snaps breach-timestamped evidence and queues the DPBI form; the **CERT-In 6-hour clock** still runs in parallel for cyber-incidents [executive_summary_decisions_a_team_has_to_make_today[8]] [16] - both must pipeline.
- **Children trigger verifiable-consent and higher penalty**: Verifiable parental/guardian consent under **Rule 10** before processing any personal data of a child or person with disability, with carve-out only for essential services (health, education, real-time safety) [executive_summary_decisions_a_team_has_to_make_today[9]] [5][executive_summary_decisions_a_team_has_to_make_today[10]] [12]. **Action**: any service that ages children must ship a verifiable-consent screen and treat it as a blocking step.
- **Significant Data Fiduciary (SDF) is a *notified* status, not a size rule**: Designation is by **Central Government notification** under Section 10(1) [executive_summary_decisions_a_team_has_to_make_today[11]] [10][executive_summary_decisions_a_team_has_to_make_today[12]] [11]; SDF extras are DPO, DPIA, periodic audit [executive_summary_decisions_a_team_has_to_make_today[12]] [11]. **Action**: build the optional SDF controls anyway - they are cheap to add and become decisive for enterprise procurement.
- **Cross-border is state-controlled, not contract-controlled**: Section 16 lets the **Central Government restrict transfers** to specific countries/territories; the EU-style SCC/adequacy model is absent [executive_summary_decisions_a_team_has_to_make_today[13]] [13][executive_summary_decisions_a_team_has_to_make_today[14]] [14]. **Action**: store personal data in-region by default and document a transfer-impact assessment.
- **Automated decision-making has no explicit DPDPA prohibition yet**: Compare to GDPR Article 22; the Latham 2025 comparison notes no equivalent automated-decision right in DPDPA, but the **EU AI Act enters force for GPAI providers from 2 Aug 2025** and most enforcement from **2 Aug 2026**. **Action**: if the hackathon product ships in the EU, layer EU AI Act / GDPR; for India-only, lean on Section 4 "lawful purpose" + consent.
- **Compliance market is small but live, with IITMIC-incubated vendors**: TruConsent (Bangalore), ComplyDP (10-minute free audit) and OneTrust's India module are the most cited entry points [executive_summary_decisions_a_team_has_to_make_today[15]] [15]. **Action**: a 48-hour hackathon team can use the TruConsent free / open-source `truScanner` modules rather than rent a vendor.
- **IT Act 2000 / SPDI Rules 2011 are NOT dead**: Section 43A and the SPDI Rules remain operational until explicitly notified as repealed under **DPDPA Section 44**, which inserts savings clauses for the IT Act [executive_summary_decisions_a_team_has_to_make_today[8]] [16]. **Action**: any product stack already under IT Act compliance is still required, not "legacy".

---

## 1_dpdpa_status_2026_rules_timeline_penalties_dpb

### 1.1 Notification facts and phased compliance window

| Event | Date | Source |
| --- | --- | --- |
| Digital Personal Data Protection Act enacted | 11 Aug 2023 ||
| DPDP **Rules 2025 notified** | **14 Nov 2025** | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[0]] [1][1_dpdpa_status_2026_rules_timeline_penalties_dpb[1]] [2]|
| Phase 1 obligations effective | ~mid-May 2026 (6 months) | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[2]] [4] |
| Phase 2 obligations effective | ~mid-Nov 2026 (12 months) | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[2]] [4] |
| Phase 3 obligations effective | ~mid-May 2027 (18 months) | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[2]] [4] |
| DPBI Chairperson/Member post advertised by MeitY | 6 May 2026 | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[3]] [8] |
| DPBI to be appointed | "Central Government will constitute" | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[0]] [1][1_dpdpa_status_2026_rules_timeline_penalties_dpb[4]] [9] |

The GloCert phased-compliance breakdown translates the Rules into **three deliverables** a team can demo [1_dpdpa_status_2026_rules_timeline_penalties_dpb[2]] [4]: in Phase 1 the consent-manager registration regime and notice format apply; Phase 2 unlocks cross-border-transfer notification mechanics and breach-notification rails; Phase 3 brings the SDF obligations (Data Protection Officer, periodic audit, DPIA) fully into force.

### 1.2 Penalty Schedule under Section 33 - exact figures

The Schedule is **not a single Rs 250 crore cap**; it is a tiered table indexed to the obligation breached. Section 33(3) further permits the Board to **enhance** the quantum by up to a factor of two [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6].

| Item | Breach | Statutory cap | Source |
| --- | --- | --- | --- |
| Item 1 | Failure to take consent / Section 9 violation | up to **Rs 200 crore** | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6][1_dpdpa_status_2026_rules_timeline_penalties_dpb[6]] [7] |
| Item 6 | Failure to undertake DPIA or Data Audit (Section 10(1)(b)/(c)) | up to **Rs 50 crore** | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6] |
| Item 7 | Failure to provide information to Board (Section 32(2)) | up to **Rs 10 crore** | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6] |
| Item 8 | Failure to comply with Board directions (Section 34) | up to **Rs 250 crore** | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6][1_dpdpa_status_2026_rules_timeline_penalties_dpb[6]] [7] |
| Other / administrative failures | General | up to **Rs 10 crore** | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6] |
| **Section 33(3) multiplier cap** | Aggravating factors (gained/avoided loss, repetitive breach, weak mitigation) | **Rs 500 crore** (= Rs 250 cr x 2) | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6] |

**Section 33(2) factors the Board MUST weigh** when fixing the quantum (verbatim) [1_dpdpa_status_2026_rules_timeline_penalties_dpb[5]] [6]:
- (a) nature, gravity and duration of the breach
- (b) type and nature of the personal data affected
- (c) repetitive nature of breach
- (d) gain realised or loss avoided
- (e) timeliness and effectiveness of mitigation
- (f) proportionality and deterrence
- (g) likely impact on the person

> **Hackathon framing**: Section 33(2)(c) and (e) are the levers a team can actually move - "repetitive" is binary, but "timely mitigation" is a process metric judges can score.

### 1.3 Data Protection Board of India - status

The PIB Press Note of 14 Nov 2025 makes the DPBI a **fully digital** body with **four members**; search-and-selection committees were notified in the same Rules [1_dpdpa_status_2026_rules_timeline_penalties_dpb[0]] [1][1_dpdpa_status_2026_rules_timeline_penalties_dpb[4]] [9]. As of MeitY's posting of 6 May 2026 the Chairperson and Member positions were open [1_dpdpa_status_2026_rules_timeline_penalties_dpb[3]] [8]. The complaint process is end-to-end digital with the Constitution of the Board announced through MeitY [1_dpdpa_status_2026_rules_timeline_penalties_dpb[0]] [1][1_dpdpa_status_2026_rules_timeline_penalties_dpb[4]] [9][1_dpdpa_status_2026_rules_timeline_penalties_dpb[3]] [8].

| DPBI attribute | Detail | Source |
| --- | --- | --- |
| Composition | Chairperson + Members (PIB: 4 members including Chair) | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[0]] [1] |
| Constituted by | Central Government | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[4]] [9] |
| Process | Two search-cum-selection committees (Rules) | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[4]] [9] |
| Complaint route | Fully digital, citizen-facing | [1_dpdpa_status_2026_rules_timeline_penalties_dpb[0]] [1][1_dpdpa_status_2026_rules_timeline_penalties_dpb[4]] [9] |
| Live cases / public orders | None surfacing in vendor / legal commentary reviewed (Jan - Aug 2026) ||

**Hackathon framing**: cite the **dPb complaint process guide** (filing -> inquiry -> determination) as the standard the Board will apply, since there is **no published case law yet**. This is *the* gap to flag in a privacy-kit pitch.

---

## 2_ai_product_obligations_under_dpdpa_compliance_matrix

### 2.1 Core obligations

| Obligation | Statutory anchor | What AI product must do | Source |
| --- | --- | --- | --- |
| Notice + consent before any processing | **DPDPA Section 4 + 6**; **Rule 7 (notice items)** | "Standalone, clear and simple consent notice" - one purpose per notice | [2_ai_product_obligations_under_dpdpa_compliance_matrix[0]] [4][2_ai_product_obligations_under_dpdpa_compliance_matrix[1]] [17] |
| Purpose limitation - one item per notice | Rule 7 | Backend stores `purpose_id` per consent row; no broad-purpose toggles | [2_ai_product_obligations_under_dpdpa_compliance_matrix[0]] [4] |
| Withdrawal of consent is as easy as giving it | Section 6(4) | Same surface area (in-app toggle) | [2_ai_product_obligations_under_dpdpa_compliance_matrix[1]] [17] |
| Data Principal rights: access (Section 11), correction (Section 12), erasure (Section 12) | DPDPA Sections 11-13; Schedules in Rules | Time-bound, fee only for repeated/manifestly unfounded | [2_ai_product_obligations_under_dpdpa_compliance_matrix[1]] [17]|
| Breach intimation to DPBI | **Section 8 / Rule 12** | Within **72 hours** of becoming aware | [2_ai_product_obligations_under_dpdpa_compliance_matrix[2]] [3][2_ai_product_obligations_under_dpdpa_compliance_matrix[0]] [4] |
| Children's verifiable parental consent | **Section 9 / Rule 10** | Verifiable consent from parent / lawful guardian before processing; carve-out only for essential services (health, education, real-time safety) | [2_ai_product_obligations_under_dpdpa_compliance_matrix[3]] [5][2_ai_product_obligations_under_dpdpa_compliance_matrix[4]] [12] |
| Person with disability verifiable guardian consent | Rule 10 | Same as children - ship a verification step | [2_ai_product_obligations_under_dpdpa_compliance_matrix[3]] [5] |
| Appointment of DPO / DPIA / Data Audit (SDF only) | **Section 10(1)(b)/(c)** | SDF designation by Central Government notification | [2_ai_product_obligations_under_dpdpa_compliance_matrix[5]] [10][2_ai_product_obligations_under_dpdpa_compliance_matrix[6]] [11] |
| Cross-border transfer restricted by GoI notification | **Section 16 / Rule 15** | Only to permitted countries; no SCC equivalent | [2_ai_product_obligations_under_dpdpa_compliance_matrix[7]] [13][2_ai_product_obligations_under_dpdpa_compliance_matrix[8]] [14] |
| Data retention / deletion when purpose ends | Section 4(2) | Erasure endpoint with auditable log | [2_ai_product_obligations_under_dpdpa_compliance_matrix[1]] [17] |
| "No automated decision" objection | **Not codified explicitly** in DPDPA; source: Latham 2025 comparison | None in India beyond the EU AI Act framing | |

### 2.2 Significant Data Fiduciary (SDF) criteria

SDF is **designated** by Central Government notification; the KS&K and vakilsearch analyses identify the **likely** criteria but stress these are interpretive, not statutory [2_ai_product_obligations_under_dpdpa_compliance_matrix[5]] [10][2_ai_product_obligations_under_dpdpa_compliance_matrix[6]] [11].

| Criterion (interpretive) | Trigger | Action | Source |
| --- | --- | --- | --- |
| Volume / sensitivity of personal data processed | High-volume user base + sensitive attributes | Build DPIA from Day 1 | [2_ai_product_obligations_under_dpdpa_compliance_matrix[6]] [11] |
| Risk to Data Principal rights | Sensitive processing (health, children, finance) | Independent annual audit | [2_ai_product_obligations_under_dpdpa_compliance_matrix[6]] [11] |
| Use of new tech, including AI/ML | Foundation models, large-scale profiling | DPO appointment | [2_ai_product_obligations_under_dpdpa_compliance_matrix[6]] [11] |
| Public-interest impact | Critical infrastructure | Public-facing grievance officer | [2_ai_product_obligations_under_dpdpa_compliance_matrix[6]] [11] |

**Hackathon framing**: a student project will **not** be designated SDF; the value in *volunteering* for SDF controls is that procurement teams at enterprise hackathons (especially **Fintech, Healthtech, E-commerce per TruConsent's verticals** [2_ai_product_obligations_under_dpdpa_compliance_matrix[9]] [15]) treat SDF readiness as a buy vs build filter.

### 2.3 Cross-border transfer mechanics

Section 16 is the **only** transfer provision. Rule 15 operationalises the Government-notification list [2_ai_product_obligations_under_dpdpa_compliance_matrix[7]] [13][2_ai_product_obligations_under_dpdpa_compliance_matrix[8]] [14]. **No Standard Contractual Clauses (SCCs), no Binding Corporate Rules (BCRs), no adequacy decisions**. Indian exporters cannot rely on a contractual bypass: the transfer destination must be on a permitted list.

| Mechanism | DPDPA | GDPR (cited as analogue) | Source |
| --- | --- | --- | --- |
| Government list of permitted countries | Yes (Section 16) | Adequacy decision (Art. 45) | [2_ai_product_obligations_under_dpdpa_compliance_matrix[7]] [13]|
| SCCs / BCRs | **Not codified** | Yes (Art. 46) | |
| Explicit cross-border consent | Not specified | Derogation (Art. 49) | |

### 2.4 Children's data - exact mechanics

| Element | DPDPA Rule 10 | Source |
| --- | --- | --- |
| Verifiable consent from parent/lawful guardian | Required before processing any personal data of a child or PwD | [2_ai_product_obligations_under_dpdpa_compliance_matrix[3]] [5][2_ai_product_obligations_under_dpdpa_compliance_matrix[4]] [12] |
| Essential-services carve-out | Healthcare, education, real-time safety | [2_ai_product_obligations_under_dpdpa_compliance_matrix[4]] [12] |
| Prohibited processing | None absolute; "consent manager" registration (Rules) governs UX | [2_ai_product_obligations_under_dpdpa_compliance_matrix[0]] [4][2_ai_product_obligations_under_dpdpa_compliance_matrix[4]] [12] |
| TRIPS / lab / 2026 implementer guidance | Compliance staggered Phases 1-3 | [2_ai_product_obligations_under_dpdpa_compliance_matrix[0]] [4] |

---

## 3_what_a_demo_must_show_compliance_surface_map

Judges with DPDPA knowledge will not only look at the AI/ML capability. They will look for **six control surfaces**. Each is mappable to a Rules citation and a vendor-free check.

| # | Control surface | What judges look for | DPDPA anchor | 48-hour-build feasibility | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | **Consent-first flow** | First screen on first launch is a **standalone, plain-language notice** with one purpose per checkbox | Rule 7 | YES - one screen + Zustand/Redux slice | [3_what_a_demo_must_show_compliance_surface_map[0]] [4][3_what_a_demo_must_show_compliance_surface_map[1]] [17] |
| 2 | **Purpose-bound processing** | Each downstream feature checks `purpose_id` against consent row; new feature -> new consent re-prompt | Rule 7 | YES - middleware | [3_what_a_demo_must_show_compliance_surface_map[0]] [4] |
| 3 | **Audit log of data use** | Append-only log with `(purpose_id, principal_id, action, timestamp)`; judges will ask "show me the log" | Section 8 evidence anchor | YES - SQLite WORM or Postgres immut. table | [3_what_a_demo_must_show_compliance_surface_map[2]] [3][3_what_a_demo_must_show_compliance_surface_map[0]] [4] |
| 4 | **Erasure endpoint** | `/erasure` API deletes PII across services, returns proof-of-erasure manifest | Section 12 | YES (with caveat: backups/deletes need design) | [3_what_a_demo_must_show_compliance_surface_map[1]] [17]|
| 5 | **Breach notification flow** | `/breach-notify` endpoint snaps the awareness timestamp and queues DPBI form text; auto-generates the **72-hour** evidence pack | Section 8 + Rule 12 | YES - stub the form, time-box the SLA | [3_what_a_demo_must_show_compliance_surface_map[2]] [3][3_what_a_demo_must_show_compliance_surface_map[0]] [4] |
| 6 | **Privacy policy obligations** | URL on every notice screen; lists purposes, retention, grievance officer, contact | Section 5 + Rules | YES - static page linked from each notice | [3_what_a_demo_must_show_compliance_surface_map[1]] [17] |

### 3.1 What judges with DPDPA knowledge actually score

The Ankura "Privacy Engineering in 2026" analysis is the single best guide for what compliance-as-engineering looks like in 2026:
- "Turn DPDP obligations into engineering controls you can prove"
- **Consent logs**, **retention automation**, **erasure reality** are the three quantifiables
- "Treating compliance as a documentation exercise" is explicitly called out as the biggest risk

**Hackathon framing**: if your privacy-kit demo is **only** PDF documentation, judges (who are increasingly DPDPA-trained) will mark you down vs a team whose product *embeds* consent-toggling, retention clocks and an erasure endpoint.

### 3.2 Suggested demo narrative (8 minutes max)

1. **Cold-start consent UI** (30 s) - rule citation overlay
2. **Purpose toggle in product** (30 s) - shows middleware blocking
3. **Live audit log query** (60 s) - read out a `principal_id`'s trace
4. **Erasure end-to-end** (90 s) - hit `/erasure`, grep DB, show manifest
5. **Breach simulation** (120 s) - synthetic breach, clock starts, /breach-notify emits a DPBI-formatted payload at 23:45:00 from "aware-time = 0"
6. **DPIA stub** (60 s) - 1-page DPIA showing how you'd satisfy Section 10(1)(b) for an SDF scenario
7. **Comparative table: DPDPA vs GDPR vs EU AI Act** (90 s) - judges use this as your "for buyers in EU, here's the layer" pitch
8. **Closing**: cite Rupee-quantified penalty exposure if a control were skipped

---

## 4_interaction_with_other_laws_where_dpdpa_sits

### 4.1 India-side sphere

| Law / directive | Scope | Live in 2026? | Conflict / overlap with DPDPA | Source |
| --- | --- | --- | --- | --- |
| **IT Act 2000 Section 43A** | Compensation for negligence in handling sensitive personal data | **Still in force** - savings clause under DPDPA Section 44 | Runs in parallel | [4_interaction_with_other_laws_where_dpdpa_sits[0]] [16][4_interaction_with_other_laws_where_dpdpa_sits[1]] [17] |
| **SPDI Rules 2011** | Sensitive personal data rules under Section 43A | **Still in force** until government formally repeals | Will be superseded once Section 44(2) notification issues | [4_interaction_with_other_laws_where_dpdpa_sits[0]] [16] |
| **CERT-In Directions 2022** (28 Apr 2022) | Cyber-incident reporting in **6 hours** | **Live** | Concurrent with DPDPA 72-hour clock | |
| **RBI Storage of Payment Data (6 Apr 2018)** | All payment system data resident in India, only end-of-day abroad | **Live, undiluted** | DPDPA Section 17 carve-out expected (not yet notified); RBI circle prevails | |
| **IRDAI / health / telecom** | Sectoral regulators may be designated | Designated regulators will get rule-making power under Section 36(4) | None named yet in Rules | [4_interaction_with_other_laws_where_dpdpa_sits[1]] [17]|

**Hackathon framing**: a hackathon team rarely runs RBI scope, but **CERT-In + DPDPA joint reporting** is the universal gap. The breach endpoint should:
- emit DPBI-formatted 72-h evidence pack
- emit CERT-In-formatted 6-h incident pack (different schema, same source log)

### 4.2 The Section 44 "savings clause"

Section 44 of the DPDPA is the **only** reason the IT Act and SPDI Rules have not disappeared; it patches consequential amendments without immediately repealing [4_interaction_with_other_laws_where_dpdpa_sits[0]] [16][4_interaction_with_other_laws_where_dpdpa_sits[1]] [17]. Any product already under IT Act/S PDI compliance is still required - this is not "legacy".

### 4.3 Comparative law - DPRs that Indian AI exporters cite

The most cited 2025 comparison is Latham & Watkins' **33-page** side-by-side (cached above). The chart most useful for buyers/investors:

| Concept | DPDPA 2023 / Rules 2025 | GDPR (EU) | EU AI Act (cited where overlapping) | Source |
| --- | --- | --- | --- | --- |
| Legal basis for processing | Consent + "certain legitimate uses" (Section 7) | Six bases incl. legitimate interests | For GPAI providers: obligations from 2 Aug 2025 ||
| Data Principal rights (full set) | Access + Correction + Erasure + Grievance | Access, Rectification, Erasure, Restriction, Portability, Objection | Union fundamental-rights review | |
| Automated decision-making | **No explicit prohibition** | Article 22 right | GPAI/synthetic-content rules (Art. 50) from 2 Aug 2026 ||
| Cross-border transfer | Government notification list | Adequacy / SCC / BCR / derogation | n/a | [4_interaction_with_other_laws_where_dpdpa_sits[2]] [13]|
| Breach notification | **72 h to DPBI** | 72 h to supervisory authority | n/a | [4_interaction_with_other_laws_where_dpdpa_sits[3]] [3]|
| Children's age threshold | **18** (with verifiable parental consent) | 16 (member-state variable) | Prohibited uses incl. exploitation of children | [4_interaction_with_other_laws_where_dpdpa_sits[4]] [5][4_interaction_with_other_laws_where_dpdpa_sits[5]] [12]|
| Data Protection Impact Assessment | Optional (mandatory for SDF) | Mandatory for likely-high-risk | Mandatory for high-risk AI (Annex III) | [4_interaction_with_other_laws_where_dpdpa_sits[6]] [11]|
| Penalty cap | up to **Rs 250 cr** (Rs 500 cr with multiplier) | up to EUR 20M / 4% global turnover | up to EUR 35M / 7% global turnover | [4_interaction_with_other_laws_where_dpdpa_sits[7]] [6]|
| DPIA / DPO for normal fiduciaries | Discretionary | Mandatory in many cases | DPO not directly mandated | |

**Hackathon framing**: an Indian hackathon team that wants EU enterprise pilots will *volunteer* for higher controls (Article 22, DPIA, DPO) because none of these break DPDPA compliance and they unlock international procurement.

### 4.4 Sectoral "for now" notes

- **Healthcare**: DPDPA references health as an "essential" carve-out [4_interaction_with_other_laws_where_dpdpa_sits[5]] [12]. DISHA (Digital Information Security in Healthcare Act) draft still pending - the DPDPA is the operating floor.
- **Fintech / UPI**: RBI 2018 storage circle is undiluted by DPDPA. **Aug 2026 reference**: **UPI fraud hit Rs 805 crore in FY26** (per prior context [23 in prior list]). Breach reporting on UPI rails will scale a hackathon pitch on provenance.
- **Telecom**: UL terms (license conditions) co-exist with DPDPA.
- **Critical sector**: CERT-In 6-h reporting remains primary.

---

## 5_enforcement_reality_has_anyone_been_penalised

### 5.1 Public-DPBI enforcement (as of 15 Aug 2026)

| Indicator | Status | Source |
| --- | --- | --- |
| DPBI Chairperson/Member position | Open (advertised 6 May 2026) | [5_enforcement_reality_has_anyone_been_penalised[0]] [8] |
| DPBI membership | Per Rules: 4 members | [5_enforcement_reality_has_anyone_been_penalised[1]] [1][5_enforcement_reality_has_anyone_been_penalised[2]] [9] |
| First DPBI determination on merits | **None public as of available search** ||
| First Rs 250 crore penalty | **None imposed yet** | |
| Live committee outputs | Complaint process documented (filing -> inquiry -> determination) | |

MICKAI's "India switched on its Data Protection Board" analysis frames 2026 as the **first-enforcement year** with localisation as the **first big test case**. Until determination is public, anything labelled "case law" in pitches is over-selling.

### 5.2 Documented pre-DPBI enforcement risk - 5 "Rs 250 crore traps"

The dpo-india.com **"5 Hidden Risks That Could Invite Rs 250 Crore Fines"** analysis (Jul 2025) lists the realistic triggers *before* the DPBI is fully operational [5_enforcement_reality_has_anyone_been_penalised[3]] [7]:

| Risk | Why it triggers Rs 250 cr | Hackathon-mitigable? |
| --- | --- | --- |
| 1. No reasonable security safeguards | Statutory cap Rs 250 cr even without proven breach | YES - MFA + encryption-at-rest |
| 2. Failure to report breach to Board | Top-tier penalty + aggravator | YES - the `/breach-notify` endpoint |
| 3. Inadequate children's consent flow | Statutory floor + child-data aggravator | YES - Rule 10 verifiable consent |
| 4. Failure to honour erasure on request | Statutory + repeat-breach aggravator | YES - erasure manifest |
| 5. Failure by SDF to appoint DPO/DPIA | Section 10 maps to Item 6 (Rs 50 cr cap, but elevated if gain realised) | YES for any enterprise pitch |

### 5.3 Compliance market - who is buying, who is selling

**Buyers (verticals per TruConsent)**: Fintech, Healthcare, E-commerce, plus the obvious telecoms / cloud / SaaS-anywhere-handling-Indian-residents [5_enforcement_reality_has_anyone_been_penalised[4]] [15]. SIH 2025's 24 winning teams at Vardhaman College of Engineering focused on **digital innovations for national challenges** (per prior context) - the privacy-kit track overlaps with **IndiaAI Mission FutureSkills** skills.

**Sellers (consolidating)**:

| Vendor | HQ / backing | Module pitch | Source |
| --- | --- | --- | --- |
| TruConsent | Bangalore, **IITMIC Incubated** | Consent Engine, Rights Center, Compliance Center, Audits & Assessments, Processor Management, **DPDPA-native** | [5_enforcement_reality_has_anyone_been_penalised[4]] [15] |
| ComplyDP | India (origin not stated) | 10-minute free audit, automated consent, breach, DP rights | |
| OneTrust | US, India module | India DPDPA Compliance FAQ / Discovery & Request | |
| KavachOne / dpdpact.co.in | India | Consent mechanism mandatory; sandbox/pledge from startup | |
| globally | Securiti, TrustArc (referenced in TruConsent comparison pages) | Cross-jurisdictional unified consoles | [5_enforcement_reality_has_anyone_been_penalised[4]] [15] |

**Hackathon framing**: there is **no pricing data published** in the searched sources. Open-source truScanner (per the TruConsent blog) is the only vendor-published free/OOS module [5_enforcement_reality_has_anyone_been_penalised[4]] [15]. Without a public pricing sheet, do not quote specific rates.

### 5.4 Compliance budgets (indirect inference)

The **absence of any published India-market figure** is itself a signal. Sector-wide pricing benchmarks in adjacent markets (GDPR-era US/UK annual privacy-tool spend) cluster in **low-USD-tens-of-thousands per year** for SME, but no DPDPA equivalent is published. A hackathon team should **not invent** a number.

---

## 6_building_blocks_for_students_48h_feasibility_matrix

### 6.1 What a 48-hour team can **honestly** build

| Control | Open-source option | Honest 48h deliverable | Caveat (what you owe the judges) | Source |
| --- | --- | --- | --- | --- |
| Auth / identity | **Hanko** (OSS, Auth0-compatible) | Login + consent-tier mapping | No native DPDPA notice item format | |
| Identity / consent graph | **Ory Kratos** (API-first) | Identity + consent-flag columns | Consent-manager registry not built in - need your own middleware | |
| Anonymisation / pseudonymisation | **ARX** (data-anonymisation tool) | Anonymised demo dataset + re-identification-risk script | DPDPA does not require anonymous-only; it requires "lawful purpose" | [6_building_blocks_for_students_48h_feasibility_matrix[0]] [17]|
| Pseudonymisation at NLP layer | **Microsoft Presidio** (OSS PII redaction) | Pre-LLM redaction pipeline | OUT multilingual; you will need own Hindi/Indic PII recogniser | (common OSS) |
| Storage / audit log | Postgres immut. table / SQLite WORM | Append-only `consent_log`, `processing_log` | Backups need same retention policy | |
| Privacy notice rendering | Static-page generator (any) | URL on every screen | Version-id baked into log | [6_building_blocks_for_students_48h_feasibility_matrix[1]] [4][6_building_blocks_for_students_48h_feasibility_matrix[0]] [17] |
| Erasure endpoint | Flask/Express + DB delete | `/erasure` with manifest | Backup erasure is a known sub-problem | |
| Breach-notify / 72h clock | Lambda / cron + template | `/breach-notify` emitting DPBI-format JSON + 72-h timer | The actual DPBI form is not yet published; you mint the JSON schema | [6_building_blocks_for_students_48h_feasibility_matrix[2]] [3] |

### 6.2 What requires a vendor (or scale, not hackathon hours)

| Control | Why not 48h | Recommended fallback for hackathon |
| --- | --- | --- |
| Full Consent Manager registration (the *entity*) | Requires government registration under Rules; need a real company + vault | Ship an **in-product** consent manager, label it "pre-registration stub" |
| End-to-end encryption / key custody for SDF | KYC, hardware security module | Use KMS + Postgres `pgcrypto`; document Phase-3 SDF-readiness roadmap |
| Cross-border transfer to non-permitted country | Needs government notification; legal opinion | Default to store-in-India; show a "destination check" middleware that asserts `country in allowed_list` |
| DPIA template + sign-off | Co-signed by DPO | 1-page DPIA stub Honesty - judges will read this |
| DPO-as-a-Service | Real human, real accountability | Point to "DPO-on-call rota for enterprise pilot" in pitch |
| Real CERT-In 6-h pipeline | Schema not fully public | Use the **PDF Directions** + your own prevention-first alerting | |

### 6.3 Hackathon pack - minimum file inventory

A team that wants to demo "DPDPA-ready AI product" should commit to **five files** in the repo:

1. `consent/notice.md` (Markdown notice, dated, version-id)
2. `consent/registry.json` (purpose map per principal)
3. `audit/processing_log` (append-only table)
4. `api/erasure.py` (delete + manifest)
5. `api/breach_notify.py` (72-h timer + DPBI JSON template)

Plus one **policy page** that links to:
- grievance officer email
- retention schedule
- cross-border transfer policy
- children's verifiable-consent screen

This inventory is **judge-defensible** against the Sections in the table at 2.1.

### 6.4 What to do about EU AI Act if you demo internationally

The EU AI Act timeline (per cross-dataset citation): GPAI obligations applied **2 Aug 2025**; enforcement begins **2 Aug 2026**; high-risk AI rules from **2 Aug 2027/2028**. If your hackathon judges are EU-based champions, **embed the GPAI provider disclosures + Annex III high-risk classification call** as a toggle. This does **not** conflict with DPDPA and reads as "global-ready" to judges.

---

## synthesis_what_survives_a_privacy_trained_judge

**Where DPDPA sits in 2026**: a regulator in the building, a Rules notification two months before, three delivery phases still ticking down, a penalty Schedule breathing **Rs 50/200/250 cr** plus a **Section 33(3) 2x multiplier**, no published case law. The honest read is that the **risk surface in 2026 is documentary** (consent artefacts, retention clocks, breach scripts) and the **enforcement surface is empty** but **scheduled**.

**The two divergences that matter most** for a hackathon team:

1. **DPDPA's penalty Schedule is much more granular than the public conversation suggests** - the headline "Rs 250 cr" applies to **Item 8 (failure to comply with Board directions)**, not every breach. The breach-of-consent cap (Item 1) is **Rs 200 cr**, and the DPIA-failure cap (Item 6) is **Rs 50 cr** [synthesis_what_survives_a_privacy_trained_judge[0]] [6]. A privacy-kit that bundles DPIA + DP-rights response + breach-notify scripts zeroes out three Schedule items at once.
2. **DPDPA borrows the GDPR's *executive mechanics* (notice, purpose limitation, retention, erasure, breach clock) but diverges on cross-border (one list, no SCC), automated decision rights (absent), and mandatory DPIA (SDF-only)**. Anyone shipping a DPDP-only product without GDPR scaffolding is **fine for India** but **loses EU procurement**, and vice versa.

**The recommendation**: ship the six surfaces (consent/notice, purpose-bound processing, audit log, erasure endpoint, breach-notify endpoint, privacy-policy URL). Reference the Rules by number. Mirror CERT-In 6-hour for any product that ever hits Indian networks. Build the SDF controls as a Phase-3 promise so enterprise judges see upgrade-on-board path. Cite the **DPB complaint process** to anchor "what the regulator does", and cite the **Rs 250 cr cap** with the **Section 33(3) multiplier caveat** so you are not over-selling and not under-selling.

---