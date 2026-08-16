# Farmer-as-Sensor: Doability Without Farm Hardware

## 1. EXECUTIVE SUMMARY

- **Conditional go, with a narrower claim**: Build an IVR-first, store-and-forward farmer-observation system, but describe it as **"no new farm sensing hardware"**, not "zero hardware." The strongest photo pilot had to provide some participants with low-cost Android phones and data because of compatibility problems, and it used reference poles to standardize framing [14].

- **IMD is a credible hazard backbone, not hyperlocal farm truth**: Official IMD APIs expose district and station nowcasts, rainfall, current weather, and forecasts [11]. They can trigger the workflow, but the API documentation does not prove plot-level accuracy, uptime, or cyclone-to-farm impact prediction. Farmer reports should refine exposure and feasibility, not override official warnings.

- **Photo capture is feasible only when the protocol does most of the work**: In the Picture-Based Insurance, or PBI, study, farmers photographed the same plot from the same location and direction, ideally between 10 a.m. and 2 p.m.; geotags, a transparent alignment image, and reference poles reduced framing variation [14]. This is much stronger evidence than simply telling farmers to "upload a damage photo."

- **Participation declines sharply even when phones, data, training, and free insurance are supplied**: Of 548 trained PBI farmers, **22.3% submitted no repeat image**, **63% submitted at least four images**, and only **27.4% photographed twice monthly or more** [14]. Better advice and claim support may help, but sustained participation cannot be assumed.

- **Nuru proves narrow offline image AI, not generic cyclone-damage AI**: With six cassava leaves, Nuru achieved **74%-88% symptom-recognition accuracy**, similar to trained researchers and above the tested extension agents and farmers [7]. It can operate offline for diagnosis and management advice, but its discussion and expert-contact functions still require connectivity [7]. This supports tightly scoped models with explicit capture protocols, not broad crop, soil, flood-depth, or loss-percentage inference.

- **A 2-4 GB basic-smartphone deployment remains unproven**: A recent low-cost prototype kept its model below 10 MB, but inference was demonstrated through a browser/Streamlit system on laptop hardware; offline TensorFlow Lite deployment was future work, and RAM, low-end-camera performance, and phone latency were not reported [22]. The first release should put blur, darkness, framing, and a few validated binary classes on-device; broader analysis should be queued for cloud or human review.

- **DTMF is the strongest basic-phone input channel**: In the seven-month Avaaj Otalo agricultural pilot, farmers significantly preferred touchtone to voice commands because speech input was more error-prone [21]. The system logged **6,975 calls**, but the top 10 callers generated more than **80%** of calls and 17 participants were removed for non-use [21]. This validates the interface, while warning against treating call volume as representative survey data.

- **A photo can support a claim; it does not create entitlement**: PMFBY's revised guidelines require loss notice within **72 hours**, permit mobile reports containing coordinates and pictures, and allow crop-loss images to substantiate an event [20]. Loss is still jointly assessed by an insurer-appointed assessor, an agriculture officer, and the farmer [20]. The product should generate an evidence packet and deadline reminders, never promise automatic payout or scheme eligibility.

- **The quoted 48.4% female-ownership figure should not be used as Odisha fact**: Odisha NFHS-5 reports that **50.1%** of women aged 15-49 had a mobile phone they themselves used, including **47.9% in rural areas** and **58.8% in urban areas** [16]. Even these figures measure personal use, not necessarily ownership [16]. Shared-phone, callback, assisted-use, and privacy-safe workflows are therefore core requirements.

- **The insurance and aerial examples need correction**: Pula's documented area-yield product uses historical benchmark yields, while its public page does not state that farmer-shot photos verify claims [24]. Agremo uses drone and satellite imagery [8], and EOSDA is satellite analytics [1]. These are useful corroboration layers, but they do not validate a farmer-as-sensor, zero-hardware workflow.

- **The defensible innovation is the doability engine**: Existing services demonstrate alerts, advisories, photos, IVR, offline diagnosis, and claim support separately. The product opportunity is to join them through a constrained ranking engine that asks whether the farmer has time, labor, cash, access, tenure documents, transport, and communications before recommending an action. The system should rank actions by risk reduction subject to those constraints, then escalate unmet needs to people or institutions.

## 2. INVENTORY

**Grade rubric:** **A** = directly demonstrated and operationally relevant; **B** = strong pilot or live product with important transfer gaps; **C** = adjacent evidence or unvalidated product claim; **D** = mismatch, unsupported transfer, or filler for this concept.

| Item | What | Mechanism | Named source, URL + date | Scale/status | Feasibility for basic-phone farmers | Grade |
|---|---|---|---|---|---|---|
| IMD API layer | Official hazard and weather feed | District/station nowcasts, current weather, rainfall, and forecasts trigger advisories | IMD API Reference, https://api.imd.gov.in/public/api_reference.html, live page accessed 2026-08-16 | Official production documentation; district nowcasts include issue and validity times, messages, and severity colors [11] | Server-side integration; farmer needs only SMS/IVR delivery | **A** |
| Odisha contingency content | Local pre/post-disaster action library | Converts an official hazard into crop-specific do's and don'ts | Government of Odisha, *Crop Contingency Plan 2025*, http://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf, 2025 | Official state plan covering cyclone, flood, and excess-rain situations [25] | Excellent content source for SMS/IVR; does not itself personalize by doability | **A** |
| Meghdoot | District/crop weather advisories | Aggregates AMFU advisories with forecast and historical weather, issued Tuesday and Friday | Meghdoot app listing, https://play.google.com/store/apps/details?id=com.aas.meghdoot, live listing accessed 2026-08-16 | Joint IMD/IITM/ICAR initiative; advisories are district- and crop-wise and available in vernacular where available [26][27] | Smartphone app; useful source and benchmark, but not sufficient for feature-phone-only users | **A-** |
| mKisan | Low-bandwidth delivery precedent | Preference-based text and voice advisories with access to databases even without internet | mKisan, http://mkisan.gov.in/alpha, live page accessed 2026-08-16 | Government mobile-advisory platform [28] | Directly relevant to SMS/voice delivery | **A** |
| Plantix | Photo diagnosis and treatment guidance | Farmer uploads crop image; AI returns diagnosis and recommendations | Plantix, https://plantix.net/en and https://plantix.net/en/plantix-intelligence/api-toolkit, live pages accessed 2026-08-16 | Public product; API advertises **69 crops** and **19 languages** [29][23] | Smartphone and image upload required; no evidence here for Odisha flood damage, low-end camera robustness, or claims | **B** |
| FarmerChat | Multimodal agricultural assistant | Accepts voice, text, or photo and provides localized responses | Digital Green, https://digitalgreen.org/farmerchat and https://farmerchat.io/, live pages accessed 2026-08-16 | Product claims more than **830,000 users** and **5M queries** across Kenya, Nigeria, Ethiopia, India, and Brazil [30]; no independent outcome study is shown in the reviewed page | Voice is promising for low literacy; photos still require a camera phone and connectivity | **B** |
| PlantVillage Nuru | Offline plant-disease diagnosis | On-device object detection plus a six-leaf protocol | Mrisho et al., https://pubmed.ncbi.nlm.nih.gov/33391304 and https://www.biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf, 2020 | Tested cassava symptom recognition at **74%-88%** with six leaves [7] | Strong proof for a narrow offline smartphone task; not a feature-phone solution and not validated for Odisha flood damage | **A for its task; C for transfer** |
| Picture-Based Insurance | Farmer-shot crop time series supporting loss assessment | App-locked, georeferenced repeat photos are reviewed by multiple experts | Kramer et al., *The feasibility of picture-based insurance*, https://www.sciencedirect.com/science/article/pii/S2352728518300812, Rabi 2016-17 study | 736 farmers in the full sample; 548 trained; 345 submitted at least four repeat images [14] | Direct evidence, but smartphones, data, training, and reference poles were needed | **B+** |
| Avaaj Otalo | Agricultural IVR question-and-answer forum | Toll-free call, DTMF or voice navigation, recorded questions, expert/farmer answers | Patel et al., http://tap2k.org/papers/pap0310-patel.pdf, pilot 2008-09 | 51 scheduled users; 6,975 calls; 610 questions; 286 answers [21] | Works on ordinary phones and farmers preferred DTMF; all participants were male and use was highly concentrated | **A-** |
| CGNet Swara | Participatory rural voice-reporting pattern | Press 1 to record, press 2 to listen; journalist moderation before publication | Mudliar, Donner, and Thies, https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ictd12-swara.pdf, deployed 2010; evidence through Nov. 2011 | 70,500 calls and 1,100 published recordings by Nov. 2011 [15] | Ordinary handset and spoken content overcome some literacy barriers [15]; it is citizen journalism, not an agricultural DTMF survey | **B** |
| PMFBY claim workflow | Official route for reporting localized and post-harvest loss | Notice, supporting pictures/coordinates, eligibility check, then joint assessment | Government of India, *Revised PMFBY Operational Guidelines*, https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf, revised edition, accessed 2026-08-16 | Official scheme workflow; **72-hour** notice and multi-party assessment [20] | IVR/SMS can guide notice and package evidence; it cannot determine payout | **A** |
| KhetScore plus PBI | Early evidence of photo data linked to financial access | Picture-based monitoring combined with digital credit and insurance | IFPRI, https://www.ifpri.org/project/pbinsurance, program begun 2016; page accessed 2026-08-16 | IFPRI reports an Odisha evaluation linking PBI to KhetScore for marginal farmers [12] | Relevant pilot evidence, not proof that arbitrary farm photos create credit visibility | **B-** |
| Low-cost image-AI prototype | Small model for six plant-health classes | Under-10 MB model, browser upload, server/laptop inference | Mhembere, https://www.ijcaonline.org/archives/volume187/number32/mhembere-2025-ijca-925588.pdf, Aug. 2025 | 5,851 images, including 400 crowdsourced images; reported 91% test accuracy [22] | Not demonstrated offline on a 2-4 GB phone; low-end camera, RAM, and latency unreported | **C** |
| FieldPlant | Reality check for uncontrolled images | Field dataset exposes background, multiple-leaf, and domain-shift failures | FieldPlant, http://ieeexplore.ieee.org/document/10086516, publication page accessed 2026-08-16 | 6,334 field images collected, 5,170 retained, with 8,629 annotated leaves across 27 classes [19] | Shows why field validation and rejection rules are essential; not itself a farmer-facing product | **A as counter-evidence** |
| Agremo | Aerial damage analytics | Drone/satellite imagery is analyzed for crop-loss assessment | Agremo, https://www.agremo.com/products/crop-damage-detection, live page accessed 2026-08-16 | Commercial precision-agriculture tool aimed at insurance adjusters | Does not use only the farmer's phone; useful as optional corroboration | **C** |
| EOSDA | Satellite crop monitoring | Remote-sensing analytics over mapped fields | EOSDA Crop Monitoring, https://eos.com/products/crop-monitoring, live page accessed 2026-08-16 | Commercial satellite platform [1] | No farmer photo protocol; server-side corroboration only | **C** |
| Pula | Index insurance, not verified photo claims | Historical benchmark yields trigger area-yield payouts | Pula, https://pula-advisors.com/, live page accessed 2026-08-16 | Company reports work across 12 countries and support for millions of farmers [24] | Public evidence reviewed does not show farmer-shot claim verification | **D for the stated photo example** |
| OKO | Digital crop-insurance analogue | Low-tech distribution and automated remote verification | ITU, https://www.itu.int/hub/2021/02/meet-oko-finance-building-climate-resilience-through-digital-financial-inclusion-in-africa, 2021 | Operational insurance example | Useful insurance precedent, but the reviewed evidence does not establish a farmer-photo claim protocol | **C; D as photo proof** |

### Case study 1: PBI shows why capture design matters more than the classifier

The PBI team did not ask for arbitrary snapshots. Farmers had to revisit the same site, point in the same direction, photograph during a preferred time window, and align the scene using a transparent prior image. Images were captured within the app so farmers could not edit and upload unrelated files [14]. Three of six experts independently assessed each time series, with major disagreements resolved by consensus [14].

That protocol detected **71.4%** of sites with yields below 10 quintals per acre, while simulated area-yield insurance identified at most **34.4%** of severely damaged sites [14]. Yet the correlation between photographic assessment and crop-cutting yield was imperfect, and photos worked better for severe visible damage than moderate damage [14]. The product lesson is not "AI can settle claims." It is "structured farmer evidence can direct and improve expert assessment."

### Case study 2: Avaaj validates DTMF, but also reveals the participation cliff

Avaaj participants received role-play training and called a toll-free number. They could press 1, 2, or 3 for the question forum, announcements, or radio; within the forum they could record or browse questions and answers [21]. Farmers used DTMF more than voice commands and described speech input as error-prone [21]. This strongly supports keypad collection for crop stage, water entry, damage bands, and resource availability.

However, 10 users produced over 80% of calls, the top three produced 60%, and 17 people were removed after about three months because of low interest or non-use [21]. The loop therefore needs immediate individual value, repeated reminders, airtime protection, and assisted access. An aggregate call count is not evidence that the farmer population is represented.

### Case study 3: Nuru's success is narrow by design

Nuru reached expert-like performance only with a defined task and capture protocol: six cassava leaves, including upper and lower leaves, produced the best likelihood of diagnosis [7]. The app then returned real-time diagnosis and management advice [7]. Its offline operation directly addresses weak rural connectivity [7].

That success should shape the Odisha roadmap. Start with a few observable and consequential classes, such as image unusable/usable, standing water absent/present, crop lodged/not lodged, or severe visible damage/no severe visible damage. Do not transfer Nuru's accuracy to flood severity, soil moisture, crop stage, or percent loss without a locally labeled Odisha dataset and field validation.

### Case study 4: PMFBY defines the boundary between evidence and entitlement

For localized calamities, a farmer may report through the insurer, bank, agriculture department, district officials, a centralized toll-free number, or the national portal. The notice must identify the insured crop, survey number, and affected acreage; pictures and location can support the report [20]. For post-harvest losses, cyclone and cyclonic rain are covered only under specified conditions, including a maximum 14-day field-drying window [20].

The insurer still appoints an assessor, and assessment is performed with the block agriculture officer and farmer [20]. Therefore, the platform can improve timeliness, completeness, provenance, and claim navigation. It cannot infer coverage, title, premium status, insured acreage, causation, or payout from a photograph alone.

## 3. COVERAGE TABLE

| Required capability | Evidence now available | Phone/channel coverage | Current coverage | Decision |
|---|---|---|---|---|
| Official cyclone/flood trigger | IMD district/station nowcast, rainfall, forecast, and current-weather APIs [11] | Back end; output by SMS/IVR | **Strong** | Use IMD as authoritative hazard trigger |
| Odisha action content | State Crop Contingency Plan includes cyclone, flood, and excess-rain guidance [25] | SMS/IVR/app | **Strong content, weak personalization** | Encode actions as a versioned rules library |
| Feature-phone farm state | Avaaj and CGNet show DTMF/voice operation on ordinary phones [21][15] | Any voice-capable handset | **Strong interaction precedent** | Make DTMF the default structured channel |
| Smartphone crop/damage image | PBI, Plantix, FarmerChat, and Nuru | Camera smartphone | **Moderate to strong by task** | Require explicit capture protocol and quality gate |
| Offline image inference | Nuru only, for narrow disease tasks [7] | Android smartphone | **Narrow** | Limit edge AI to locally validated classes |
| Low-end 2-4 GB validation | No reviewed study reports complete RAM, latency, camera, thermal, and battery results | Unknown | **Missing** | Benchmark on representative Odisha devices before claims |
| Water-depth and soil measurement from image | No direct validated evidence found | Camera smartphone | **Missing** | Collect depth bands by DTMF; treat images as corroboration |
| Sustained participation | PBI and Avaaj document non-use and concentration [14][21] | All channels | **Weak** | Instrument cohort retention and return immediate value |
| Farmer data quality versus professionals | PBI used expert review; FieldPlant and citizen-science research document domain and observer bias [14][19][13] | All channels | **Partial** | Keep human review and model observation probability |
| Claim support | PMFBY accepts pictures/location as supporting information within a formal process [20] | App, portal, toll-free, assisted | **Strong for notice/support; not adjudication** | Generate evidence packet and deadline workflow |
| Credit linkage | IFPRI reports an Odisha PBI-KhetScore evaluation [12] | Smartphone/assisted | **Pilot-level** | Seek explicit lender partnership; do not infer creditworthiness |
| Scheme eligibility | No evidence that farmer observations automatically establish eligibility | All | **Missing** | Run authoritative registry and document checks |
| Gender and shared-phone inclusion | Only 47.9% of rural Odisha women aged 15-49 reported a phone they themselves used [16] | Shared IVR, callback, assisted | **High risk** | Measure who actually speaks and submits, not household phone reach |
| Privacy and consent | Citizen reports include location, crop, finance, and tenure-sensitive data | All | **Design gap** | Purpose-specific consent, minimal collection, deletion and redaction controls |
| Closed-loop outcome evidence | Mobile advisories can influence practice adoption, but the reviewed evidence does not validate this proposed loop [2] | All | **Unproven** | Evaluate action completion and avoided loss, not messages delivered |

The proposed system covers warning ingestion, two-way basic-phone interaction, and supporting evidence well enough for a pilot. It does not yet cover representative participation, precise image measurement, automatic financial eligibility, or outcome attribution.

## 4. WHAT IS MISSING

### 4.1 A validated doability model

No reviewed system provides the exact proposed combination of hazard, crop state, labor, cash, tenure, mobility, and institutional access. A labor question is not the same as knowing whether labor can arrive before landfall; a cash question is not the same as liquidity; and title is not the only basis on which a tenant or sharecropper may seek support.

The missing research artifact is an Odisha-specific **action-resource matrix**. For every official action, it should define time required, people required, cash/input requirement, tenure/document dependency, physical risk, transport dependency, crop-stage relevance, and fallback action. Extension staff, women farmers, tenant farmers, FPOs, insurers, and disaster officials must validate it before automation.

### 4.2 A low-literacy photo-training trial

PBI demonstrates a high-control protocol, not a low-literacy, no-assistance protocol. Its app used geotag warnings, a transparent alignment image, reference poles, training, and project-paid data [14]. Avaaj demonstrates that role-play can teach an IVR workflow [21], but it does not show that voice alone can teach reliable crop photography.

The pilot must compare at least: voice-only guidance, pictorial good/bad examples, a live silhouette/ghost overlay, assisted first capture, and automated blur/exposure feedback. Measure usable-image rate, retake count, task time, comprehension, and seven-day repeat performance. Do not claim that illiterate farmers can reliably frame damage evidence until this is tested.

### 4.3 Low-end camera and 2-4 GB deployment evidence

FieldPlant shows why laboratory accuracy is misleading: PlantVillage has one leaf and a uniform background, while models trained there perform poorly on complex field scenes [19]. Of 6,334 field images collected for FieldPlant, 5,170 remained after inconsistent images were removed [19]. That filtering burden is itself a warning about farmer-generated data.

No reviewed source provides an end-to-end test across representative low-cost Odisha phones covering camera focus, scratched lenses, motion blur, low light, RAM, install size, inference latency, battery, thermal throttling, and offline model update. This is a release gate, not a documentation detail.

### 4.4 A real DTMF survey completion rate

Avaaj offers agricultural interaction evidence, but **71% ever calling** is not a survey-completion rate; browsing, asking, and answering were voluntary activities [21]. CGNet's 70,500 calls likewise measure a voice forum, not completion of a fixed questionnaire [15].

The pilot must record answer-level funnels: numbers dialed, calls connected, consent completed, each question reached, each question answered, hang-up point, callback completion, repeat-cycle retention, and completion by sex, phone ownership, shared use, language, district, and disaster phase.

### 4.5 Incentive causality and the true dropout curve

The PBI trial gave insurance free of charge, and some farmers received a phone and data plan [14]. Its commercial take-up therefore cannot be inferred [14]. Avaaj removed 17 participants for non-use, while heavy users dominated traffic [21].

Test incentives separately: immediate personalized advice, claim-deadline protection, evidence receipt, airtime reimbursement, cash micro-incentive, seed/input benefit, and community recognition. Otherwise, the team will not know whether participation is sustained by value, subsidy, novelty, or a small group of enthusiasts.

### 4.6 Representative data, fraud control, and professional comparison

Citizen observation is produced by at least three processes: choosing where and when to look, detecting or identifying the condition, and deciding whether to report it [13]. In one citizen-science project, 32.5% of observations were within 5 km of the observer's residence, and equipment type affected what was reported [13]. That study is not agricultural validation, but its bias mechanisms transfer plausibly and must be tested locally.

Required controls include duplicate detection, impossible-time/location checks, app-locked media for high-stakes evidence, cross-farmer event consistency, random professional audits, expert inter-rater agreement, and separate model-confidence and evidence-confidence scores. Voice reports need moderation for safety-critical or publicly shared content, as CGNet used trained-journalist review [15].

### 4.7 Claims, credit, and scheme interoperability

A media packet can reduce missing information; it does not establish premium status, notified crop, insured acreage, title, tenancy, identity, or scheme rules. PMFBY explicitly retains eligibility verification and joint loss assessment [20]. Likewise, IFPRI's KhetScore work is an evaluated linkage, not a general rule that photographs improve a credit score [12].

The platform needs written data-acceptance agreements with insurers, banks, departments, and FPOs. Without them, "claim-ready," "credit-visible," and "scheme-eligible" are marketing phrases rather than product outcomes.

### 4.8 Privacy, phone sharing, and gendered control

Odisha NFHS-5's 50.1% figure concerns women who personally use a phone, not women who control a private smartphone [16]. A husband's or household phone may expose voice recordings, land status, debt, claim amounts, or location. Shared use can also misattribute who observed the crop and who made the decision.

The system needs a shared-phone mode, neutral callback labels, opt-in timing, PIN-free safety information, optional PIN protection for financial status, voice deletion, redaction, delegated reporting, and assisted channels through women SHGs or extension workers. Analytics must distinguish subscriber, respondent, observer, plot operator, and landholder rather than treating one phone number as one farmer.

## 5. HOW IT FEEDS THE PRODUCT

### 5.1 Product architecture: seven linked stages

1. **Official trigger:** Poll IMD warnings, nowcasts, and rainfall feeds; preserve the source, issue time, validity, geography, and severity.
2. **Farmer state packet:** Collect a short DTMF response first; add optional voice and photographs according to handset and consent.
3. **Quality and provenance:** Check whether the response is complete, timely, plausible, and attributable to a plot or event. Reject or request a retake before classification.
4. **Farm impact estimate:** Combine hazard, crop, stage, farmer observation, neighboring observations, and prior verified records. Keep uncertainty explicit.
5. **Doability constraints:** Represent labor, cash, tenure/documentation, mobility, time, tools, input availability, and assistance access.
6. **Constrained action ranking:** Recommend the safest high-impact action that fits known constraints; supply a fallback and help request when it does not.
7. **Evidence and learning:** Issue a receipt, queue relevant claim steps, record whether the action was feasible and completed, and use verified outcomes to recalibrate recommendations.

### 5.2 Feature, rule, and algorithm conversion

| Evidence or gap | Product feature | Rule or algorithm | Safety boundary |
|---|---|---|---|
| IMD APIs | Hazard Event Ingestor | Deduplicate by source, area, issue time, validity, and severity; version every update | Never downgrade an official warning from farmer reports |
| Odisha contingency plan | Action Knowledge Graph | Encode action, crop, stage, hazard, time window, required resources, and contraindications | Extension authority approves every production action |
| Avaaj DTMF preference | Four-to-six-step IVR state machine | DTMF for categorical fields; repeat answer for confirmation; callback after interruption | Voice recognition cannot silently overwrite a DTMF answer |
| CGNet moderation | Voice triage queue | Speech-to-text for routing, human review for ambiguous or safety-critical reports | Unreviewed voice does not become public truth |
| PBI capture protocol | Guided Evidence Camera | Same-location prompt, prior-image overlay, time-window guidance, wide plus close view, automated retake | No claim decision from a single image |
| FieldPlant domain shift | Image Quality Gate | Blur, darkness, obstruction, duplicate, and out-of-distribution checks before classification | "Unusable" and "uncertain" are valid outputs |
| Nuru offline proof | Narrow Edge Classifier | Only locally validated crop/task combinations; model card records device and dataset coverage | Never display Nuru's 74%-88% as Odisha flood accuracy |
| Weak connectivity | Store-and-forward media queue | Encrypt and queue image; send DTMF receipt immediately; upload on usable connection | Safety advice cannot wait for the image upload |
| Cloud alternative | Edge-cloud router | Edge for quality and narrow classes; cloud/human route for multi-image severity and claims | Benchmark data cost, latency, and outage behavior before launch |
| Observer bias | Observation Confidence Score | Model protocol completion, device, recency, location plausibility, observer history, and corroboration separately | Do not confuse frequent reporting with higher need or truth |
| Farmer constraints | Doability Vector | `labor, cash, time, tenure, mobility, tools, connectivity, assistance` with unknown allowed | Unknown must not default to available |
| Feasibility-aware ranking | Constrained Action Ranker | Rank by expected risk reduction, urgency, confidence, and fit with the doability vector | Life safety outranks crop and financial optimization |
| PMFBY workflow | Claim Readiness Assistant | 72-hour timer, crop/survey details checklist, media packet, channel routing, receipt and status | Say "submitted for assessment," never "claim approved" |
| KhetScore precedent | Consent-based Financial Export | Share only verified, purpose-specific fields with a named partner | No hidden credit scoring from disaster reports |
| Gender/shared phones | Private and Delegated Modes | Neutral callbacks, respondent/observer separation, assisted submission, channel-specific disclosure | Do not read debt, title, or claim amount aloud by default |
| Dropout evidence | Participation Health Monitor | Cohort retention, question-level abandonment, repeat submission, benefit delivery, and subgroup parity | Do not optimize only for total calls or power users |
| Human fallback | Extension and Assessor Console | Prioritize severe hazard, low confidence, contradictory data, vulnerable household, and claim deadline | Human decisions and edits are logged and appealable |

### 5.3 The minimum viable DTMF survey

A first-stage event survey should ask only fields that immediately change the recommendation:

1. Crop and broad stage.
2. Whether water has entered the plot.
3. Water-depth band or visible lodging/damage band.
4. Whether an able adult can act within the warning window.
5. Whether the farmer can spend from a small set of locally meaningful cost bands.
6. Whether the plot is insured and whether the respondent has the needed documents or knows who holds them.

Every answer needs "do not know" and "repeat" options. The system should not ask for a photograph before delivering urgent safety guidance. A voice note is optional after the structured answers, not a substitute for them.

### 5.4 Photo protocols by task

| Task | Capture protocol | Automated checks | Interpretation |
|---|---|---|---|
| Leaf diagnosis | Multiple leaves from defined canopy positions; leaf fills frame; repeat if blurred or dark | Focus, exposure, obstruction, crop/model coverage | Narrow disease class only; Nuru's six-leaf result supports multi-leaf protocol [7] |
| Field condition | Wide view from repeatable natural landmark and direction; prior-image overlay | Location consistency, horizon/coverage, duplicate, blur | Crop stage and gross condition after local validation |
| Flood entry | Wide view plus close view of crop base; DTMF depth band | Water visibility, scene consistency, recency | Presence/corroboration, not precise depth from pixels alone |
| Damage evidence | Pre-event or earlier baseline plus post-event views; app-locked capture where possible | Timestamp, location, edit path, duplicate, event window | Evidence packet for expert/assessor review |
| Soil condition | Close and contextual views plus structured farmer description | Blur and lighting only | Do not infer moisture, fertility, or remediation from an unvalidated image |

PBI's 10 a.m.-2 p.m. window and alignment system are useful starting points [14], but they should be validated for Odisha crops, monsoon light, and disaster conditions. If insurance-grade repeatability requires a scale marker or pole, the team must admit that the workflow is "minimal hardware," not zero hardware.

### 5.5 The doability algorithm

The first version should be a transparent rule engine, not a black-box recommender. For each candidate action, compute:

`priority = urgency x expected risk reduction x confidence x feasibility`

Feasibility is reduced by missing labor, unaffordable cost, inadequate time, unsafe access, absent tools, tenure/document restrictions, or unavailable assistance. Unknown inputs reduce confidence and trigger a safe fallback rather than a fabricated assumption.

Examples:

- **No labor:** Recommend only one-person actions that are safe, then create a help request for an FPO, SHG, neighbor group, or extension worker.
- **No cash:** Suppress purchase-dependent recommendations; offer no-cost steps and named assistance routes.
- **Tenant or unclear title:** Continue agronomic advice, but route financial or claim steps through the applicable documentation check rather than excluding the farmer.
- **No smartphone:** Complete the entire warning and doability path through DTMF/voice; an agent may add media later.
- **Low image confidence:** Ask for a retake, use the structured report provisionally, and send severe cases to human review.
- **Shared phone:** Deliver safety guidance openly but protect financial, land, and claim-status details.

### 5.6 Three evidence tiers

- **Tier 0 - Self-report:** DTMF or voice fields used for personalization and triage. Fast and inclusive, but not claim proof.
- **Tier 1 - Protocol media:** Timestamped/location-associated images, repeat views, and quality metadata. Useful for corroboration and evidence packets.
- **Tier 2 - Verified record:** Expert review, assessor finding, government record, insurer acknowledgment, or other authoritative validation.

Only Tier 2 should update high-stakes labels such as verified loss or accepted claim. Tier 0 and Tier 1 can improve routing and completeness, but must remain distinguishable in every downstream export.

### 5.7 Making the participation loop hold

The loop should return value within the same interaction: advice, a feasibility-adjusted alternative, a reference number, a claim deadline, or a visible help request. Later messages should explain what the farmer's report changed. This makes participation reciprocal rather than extractive.

Instrument four linked funnels: **contact -> completed observation -> usable/verified observation -> action or institutional response**. Then test whether the response increases the next observation. The mobile-advisory literature found that such services could reach many farmers and significantly influence new-practice adoption, but also that mobile ranked only fifth among seven information sources and women, older people, and small-scale farmers were less likely to use it [2]. Human extension and community institutions therefore remain part of the loop.

## 6. REAL-vs-FILLER + NOISE LOG

### 6.1 Real versus filler

| Claim or example | Classification | What the evidence really supports | Correction for the pitch |
|---|---|---|---|
| Nuru proves offline crop-image AI | **REAL, tightly scoped** | Cassava symptom recognition at 74%-88% with six leaves, with offline diagnosis/advice [7] | Say "narrow offline diagnosis is feasible," not "offline cyclone-damage AI is solved" |
| PBI proves farmers can create claim-relevant media | **REAL pilot** | Structured, repeat farmer photos supported expert assessment; participation was incomplete [14] | Use as the flagship farmer-as-sensor case |
| Avaaj proves basic-phone agricultural DTMF | **REAL pilot** | Farmers preferred touchtone; calls and questions were substantial, but use was concentrated [21] | Use for interface design, not population response-rate claims |
| CGNet proves citizen voice reporting | **REAL analogue** | Ordinary-phone recording plus trained moderation at meaningful scale [15] | Cite as participatory voice precedent, not a farm survey |
| Plantix supports photo diagnosis | **REAL product, limited evaluation here** | Live photo-diagnosis/API product claiming 69 crops and 19 languages [23] | Do not claim Odisha flood or claim-validation accuracy |
| FarmerChat supports photo/voice/text | **REAL product, product-reported scale** | Multimodal localized assistant with claimed users and queries [30][5] | Separate usage claims from measured farmer outcomes |
| Agremo/EOSDA prove farmer-phone damage assessment | **ADJACENT** | Drone and satellite analytics, not farmer-shot media [8][1] | Put them in optional corroboration, not core proof |
| Pula verifies claims from farmer photos | **FILLER/UNSUPPORTED** | Public page describes historical benchmark yield triggers and does not state farmer-photo verification [24] | Remove this claim |
| OKO proves farmer-photo verification | **UNPROVEN IN REVIEWED EVIDENCE** | Digital insurance and remote verification are relevant, but a farmer-photo protocol was not established | Describe only as an insurance-distribution analogue unless primary evidence is obtained |
| TinyML is ready on any 2-4 GB phone | **PREMATURE** | Small-model research exists, but the reviewed prototype did not report phone RAM, camera, latency, or offline deployment results [22] | Treat device benchmarking as a pilot gate |
| Every farmer photo improves credit and scheme eligibility | **OVERCLAIM** | One IFPRI program evaluated PBI linked to KhetScore in Odisha [12] | Require named partner rules and consent before any export |
| Hardware goes to zero | **SLOGAN, NOT LITERAL** | Phones, charging, network, and server infrastructure remain; PBI added phones, data, and reference poles [14] | Say "no dedicated farm sensor network" |
| Female phone ownership is 48.4% | **NOISY/WRONG DENOMINATOR FOR ODISHA** | NFHS-5 reports 50.1% personal use among women 15-49, 47.9% rural [16] | State the exact population, measure, geography, and year |
| Farmer data can replace professionals | **UNSUPPORTED** | PBI retained three-expert review and consensus; PMFBY retains joint assessment [14][20] | Position farmers as first-mile observers and partners, not sole adjudicators |

### 6.2 Noise log

1. **Denominator noise:** Household access, personal use, ownership, smartphone ownership, and internet use are different measures. Never combine them.
2. **Task-transfer noise:** Disease recognition, crop-stage classification, standing-water detection, damage percentage, and claim causation are different models.
3. **Laboratory-to-field noise:** Uniform-background leaf accuracy does not survive automatically under clutter, low light, multiple leaves, rain, blur, or damaged lenses [19].
4. **Participation noise:** Total calls or uploads hide who never responded and whether a few power users dominate. Avaaj's top 10 users generated more than 80% of calls [21].
5. **Marketing-to-outcome noise:** User and query counts do not establish yield, loss avoidance, accuracy, inclusion, or sustained behavior.
6. **Evidence-to-entitlement noise:** A geotagged photo can support a record, but cannot by itself establish insured status, eligible peril, ownership, causation, or payout.
7. **Remote-sensing conflation:** Drone or satellite analysis does not prove farmer-phone capture, even if both ultimately produce an image.
8. **Survivor bias:** Existing smartphone owners and trained volunteers are not representative of tenants, women sharing phones, older farmers, or people whose devices fail during a cyclone.
9. **Hazard-report bias:** People report visible, severe, accessible, or personally salient damage more often. Missing reports do not mean no damage.
10. **Feedback contamination:** If benefits depend on reported severity, farmers may learn to select more dramatic images or categories. Random audit and separation of advisory benefit from claim adjudication are necessary.

## 7. VERDICT

### Decision

**Conditional GO for a field pilot; NO-GO for the full marketing claim as currently written.**

The defensible product is:

> An IVR-first, no-new-sensor-network platform that combines official IMD hazards with structured farmer observations, optional protocol-guided photos, and human verification to rank actions by both risk and doability, while preparing claim-supporting evidence and assistance referrals.

The following claims should not be made at launch:

- "Zero hardware" in the literal sense.
- Automatic damage percentage from any low-end phone.
- Verified operation on all 2-4 GB phones.
- Automatic claim approval, credit improvement, or scheme eligibility.
- Representative coverage merely because a household phone number was reached.
- Pula or OKO as verified farmer-photo claim examples without stronger primary evidence.

### Build order

**Stage 1 - IVR-first advisory and doability:** Integrate IMD and the Odisha contingency plan; deploy the DTMF state machine, action-resource rules, SMS/voice receipts, and extension escalation. This serves feature phones and tests the core novelty without waiting for image AI.

**Stage 2 - Guided evidence capture:** Add optional smartphone capture for baseline and post-event field views. Start with quality control and evidence packaging, not automated loss adjudication. Test assisted first capture, overlays, local-language audio, and store-and-forward upload.

**Stage 3 - Narrow validated AI:** Train only on locally collected, expert-labeled Odisha data. Release one task at a time after device-stratified field testing and subgroup analysis. Keep cloud/human fallback for uncertain and high-stakes cases.

**Stage 4 - Institutional linkage:** Add PMFBY notice support first. Add credit or scheme exports only after a named partner confirms accepted fields, consent, correction, retention, and appeal rules.

### Pilot gates

Proceed beyond pilot only if the team can show:

- Question-level IVR completion and repeat retention, not merely calls placed.
- Usable-photo and successful-retake rates by device, sex, literacy, and shared-phone status.
- Model sensitivity and false-negative rates on real post-cyclone/flood conditions.
- Agreement between farmer evidence, expert review, and formal assessment.
- Time from IMD trigger to delivered advisory and completed observation.
- A measurable increase in actions farmers report as feasible and complete.
- No material subgroup is systematically under-contacted, over-rejected, or excluded from benefits.
- Insurer or department acknowledgment that generated packets are operationally useful.
- Documented consent, access, correction, deletion, and incident-response procedures.

### Synthesis

| Strategy | Mechanism | Scope | Main trade-off | Evidence horizon |
|---|---|---|---|---|
| IMD plus Meghdoot/mKisan | Official forecast and one-way advisory | Broad hazard and district/crop messaging | Reach without plot-level state or doability | Operational now [11][27][28] |
| Avaaj/CGNet | Farmer voice and DTMF participation | Basic-phone reporting and peer/expert communication | Inclusion improves, but participation concentrates and moderation costs persist | Multi-month/early deployment studies [21][15] |
| Plantix/FarmerChat/Nuru | Image or conversational diagnosis | Crop questions and narrow disease tasks | Rich input, but smartphone, task transfer, and validation limits | Live products plus narrow evaluation [23][5][7] |
| PBI/PMFBY | Protocol evidence plus formal assessment | Loss documentation and claims workflow | Better first-mile evidence, but not automatic entitlement | Field pilot plus official process [14][20] |
| Agremo/EOSDA/Pula | Aerial, satellite, or index analytics | Portfolio monitoring and remote corroboration | Scales spatially but does not make the farmer the sensor | Commercial/adjacent [8][1][24] |
| Proposed doability engine | Constrained action ranking and assistance routing | Pre-disaster action, post-disaster recovery, evidence reuse | Highest product differentiation, but least directly validated component | Must be established by Odisha pilot |

The non-obvious conclusion is that the project should **not** lead with image AI. Its strongest advantage is the ability to ask a farmer, on any phone, what is happening and what is actually possible, then turn that answer into a safer action, an assistance request, and a traceable evidence record. Photos and AI strengthen that loop where devices and confidence permit; they should not define who can participate.

The farmer becomes a partner only if three conditions hold: the farmer receives value before being asked for repeated data, uncertainty is visible rather than hidden, and institutions agree to act on the resulting record. Without those conditions, farmer-as-sensor becomes unpaid data collection. With them, it is a credible and differentiated response to PS-07.

## References

1. *Crop Monitoring Software For Remote Farm Analytics*. https://eos.com/products/crop-monitoring
2. *http://sciencedirect.com/science/article/pii/S2452292917300711*. http://sciencedirect.com/science/article/pii/S2452292917300711
3. *Application of smartphone-image processing and transfer ...*. https://www.sciencedirect.com/science/article/pii/S2772375523000254
4. *TinyML for Plant Disease Detection: Efficient Edge AI ...*. https://www.sciencedirect.com/science/article/pii/S1877050925016515
5. *http://digitalgreen.org/farmerchat*. http://digitalgreen.org/farmerchat
6. *Pradhan Mantri Fasal Bima Yojana - Crop Insurance | PMFBY - Crop Insurance*. http://pmfby.gov.in/
7. *http://biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf*. http://biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf
8. *Agremo: Field Analytics Software & Precision Agriculture*. https://www.agremo.com/
9. *Meet OKO Finance: Building climate resilience through digital financial inclusion in Africa - ITU*. http://itu.int/hub/2021/02/meet-oko-finance-building-climate-resilience-through-digital-financial-inclusion-in-africa
10. *Picture Based Insurance Transcript 5 14 20*. https://www.ifpri.org/wp-content/uploads/2020/10/picture_based_insurance_transcript_5-14-20.pdf
11. *Api Reference*. https://api.imd.gov.in/public/api_reference.html
12. *Picture-Based Crop Insurance (PBI) | IFPRI*. https://www.ifpri.org/project/pbinsurance
13. *Frontiers | A Framework of Observer-Based Biases in Citizen Science Biodiversity Monitoring: Semi-Structuring Unstructured Biodiversity Monitoring Protocols*. https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.693602/full
14. *The feasibility of picture-based insurance (PBI): Smartphone pictures for affordable crop insurance - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2352728518300812
15. *Ictd12 Swara*. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ictd12-swara.pdf
16. [Odish Final Report [FR374]](https://dhsprogram.com/pubs/pdf/FR374/FR374_Odisha.pdf)
17. *Phone Survey Methods | IPA*. https://poverty-action.org/phone-survey-methods
18. *Press Release Page | Press Information Bureau*. https://pib.gov.in/PressReleasePage.aspx?PRID=2132330
19. *Fetched web page*. http://ieeexplore.ieee.org/document/10086516
20. *Revised Operational Guidelines*. https://pmfby.gov.in/pdf/Revised_Operational_Guidelines.pdf
21. *Avaaj Otalo — A Field Study of an Interactive Voice Forum for Small Farmers in Rural India*. http://tap2k.org/papers/pap0310-patel.pdf
22. *Low-Cost Smartphone-based Plant Disease Diagnosis for Zimbabwean Farmers using Transfer Learning and Crowdsourced Image Data*. https://www.ijcaonline.org/archives/volume187/number32/mhembere-2025-ijca-925588.pdf
23. *http://plantix.net/en/plantix-intelligence/api-toolkit*. http://plantix.net/en/plantix-intelligence/api-toolkit
24. *HOME | PULA*. http://pula-advisors.com/
25. *http://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf*. http://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
26. *http://play.google.com/store/apps/details?hl=en-US&id=com.aas.meghdoot*. http://play.google.com/store/apps/details?hl=en-US&id=com.aas.meghdoot
27. *http://play.google.com/store/apps/details?hl=en_US&id=com.aas.meghdoot*. http://play.google.com/store/apps/details?hl=en_US&id=com.aas.meghdoot
28. *http://mkisan.gov.in/alpha*. http://mkisan.gov.in/alpha
29. *http://plantix.net/en*. http://plantix.net/en
30. *http://farmerchat.io/*. http://farmerchat.io/
