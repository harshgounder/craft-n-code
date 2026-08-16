# Voice-to-Action Crop Protection for Odisha Farmers

## 1. EXECUTIVE SUMMARY

- **Defensible Uniqueness**: SMS/IVR delivery is not novel. The defensible innovation is a closed loop in which a farmer records an actual field problem, the system converts it into confirmed crop-hazard slots, a human agronomist reviews uncertain or novel cases, and verified cases update retrieval, FAQs, and versioned rules. Avaaj Otalo proves that rural farmers will record questions, while CGNet Swara proves that callback, recording, moderation, and republication can operate on ordinary phones [13][6] -> Pitch the product as a "farmer-to-rule learning loop," not another weather-alert app.

- **Natural Problem Grammar**: Farmers should not be expected to state a scientific diagnosis. In Avaaj Otalo, callers commonly began with name, location, and phone number; more than 65% included at least their name, and 39% of questions concerned pests and diseases [13] -> Prompt for observable facts in the farmer's order: identity/location, local crop name, what changed, plant part, when it began, spread, water depth, and recent weather.

- **Keypad Before Free-Form ASR**: Avaaj used "question" or key 1, followed by key 1 to record or key 2 to listen. Recordings were limited to 30 seconds. Callers consistently preferred touchtone navigation, while voice navigation was more error-prone [13] -> Use DTMF for consent, language, crop family, urgency, replay, and confirmation; reserve ASR for the short problem narrative.

- **Odia ASR Is a Safety Gate**: A 2026 agricultural benchmark used 2,233 Odia recordings collected on mobile devices in real agricultural settings. The best reported Odia WER was 35.1%, not 23.4%; Whisper API reached 125.6%, and 12.3% of Odia recordings were classified as high-noise [12] -> Never let an unconfirmed transcript directly trigger destructive, chemical, or harvest advice.

- **KCC Is Useful, But Common Claims Are Inflated**: Kisan Call Centre service operates in 22 local languages and escalates unanswered calls to subject-matter specialists, but the public data page exposes StateName, DistrictName, BlockName, Season, and Sector and does not disclose a row count, raw audio, or raw text in 22 languages [7][4] -> Treat KCC as a candidate retrieval and taxonomy resource only after a row-level audit; do not advertise it as a verified 22-language speech corpus.

- **Crop Protection Must Mean Physical Decisions**: Odisha guidance supports opening drainage in non-mature paddy, moving harvested rice to a safer place under tarpaulin, and sun-drying it for one or two days after rain [10]. The state contingency plan uses a 50% damage threshold for retransplanting versus gap-filling [14] -> The advisory must output a verb, object, deadline, quantity, location, and safety constraint, not "take precautions."

- **The Strongest Quantified Crop Tradeoff Is Pre-Seasonal**: In a randomized experiment across 128 Odisha villages, Swarna-Sub1 raised yield about 45% after 10 days of flooding; the maximum estimated advantage was 718 kg/ha, or 66%, near 13 days. The estimated 5.3% no-flood penalty was not statistically significant [17] -> Recommend SUB1-compatible varieties before sowing in flood-prone profiles, but do not misrepresent varietal choice as a last-minute cyclone action.

- **Production Deployment Is Gated**: Mobile extension can improve recall, knowledge, and practice adoption without necessarily increasing yield: an Andhra Pradesh trial found a 0.232-SD knowledge gain and 4-7 percentage-point adoption gains, but no significant production or yield effect [18]. KCC records 100% of calls for six months, while mKisan's published privacy notice does not explain IVR recording consent, retention, opt-out, or deletion [7][5] -> Proceed with a human-reviewed pilot, not autonomous statewide advice.

## 2. INVENTORY / EVIDENCE TABLE

Grades used here are: **A = field-proven or authoritative enough for an MVP rule; B = deployed or empirically promising but requires local validation; C = useful analogue or self-reported capability; D = unsupported, mischaracterized, or unsuitable as evidence.**

| What | Named source (URL + date) | Mechanism | Feasibility | Grade A-D |
|---|---|---|---|---|
| Recorded farmer questions with DTMF fallback | Avaaj Otalo field study, CHI 2010; http://tap2k.org/papers/pap0310-patel.pdf | Caller selects Q&A, records a 30-second question, listens to questions/answers, and may contribute an answer. It accumulated 6,975 calls and 610 questions over seven months [13]. | High. Directly reusable for feature-phone elicitation; replace long browsing with search and callbacks. | A |
| Observed farmer utterance structure | Avaaj Otalo, 2010; same URL | Many callers introduce name, location, and phone before the problem; over 65% give at least a name [13]. | High for prompt order, but insufficient to infer a universal agricultural grammar. | A |
| Missed-call/callback community recording | CGNet Swara, data through November 2013; http://global.comminit.com/content/cgnet-swara | Ten voice lines call users back; key 1 records and key 2 listens. Journalists review recordings, with volunteer follow-up for fact-checking [6]. | High as an interaction precedent; agricultural triage and privacy controls must be added. | B |
| Human moderation at meaningful call volume | CGNet Swara, data through November 2013; same URL | Moderated spoken reports reached up to 400 calls per day [6]. | Medium. Demonstrates workflow, not agronomic correctness or disaster-scale capacity. | B |
| National farmer-call escalation | Ministry of Agriculture KCC guide, undated, accessed 2026-08-16; https://agriwelfare.gov.in/sites/default/files/KCC%20WEBSITE.pdf | Local-language Farm Tele Advisors answer first; unresolved questions are conferenced to State Agriculture, ICAR, or university specialists [7]. | High as a reviewer model and escalation template. | A |
| KCC recording and quality practice | KCC guide, accessed 2026-08-16; same URL | Call barging, farmer ratings, and 100% recording retained for six months support quality monitoring [7]. | Technically high; consent, deletion, access control, and retention justification remain governance gaps. | B |
| Public KCC query resource | Open Government Data India, updated 2026-08-15; https://www.data.gov.in/resource/kisan-call-centre-kcc-transcripts-farmers-queries-answers | Public metadata exposes geography, season, and sector fields across 2006-2025 [4]. | Medium only after downloading and profiling actual rows, languages, duplicates, answer quality, and licences. | B |
| "KCC corpus has farmer questions in 22 languages" | KCC service guide plus OGD page, accessed 2026-08-16 | The service answers in 22 languages, but the located public metadata does not establish raw audio or raw 22-language query text [7][4]. | Not usable as a training-corpus claim without a row-level audit. | D |
| Multimodal problem capture | FarmerChat, official Digital Green page, accessed 2026-08-16; https://www.digitalgreentrust.org/farmerchat | Farmers can submit text, speech/voice note, or a photo; responses can be text, voice, or video. The organization describes curated expert-validated data, RAG, feedback, and RLHF support [11]. | Technically high on smartphones; low-connectivity and feature-phone behavior require independent testing. | B |
| FarmerChat reach and quality | FarmerChat official page, accessed 2026-08-16; same URL | The page claims 1.6M+ queries and 900K+ farmers helped daily; it reports 95% satisfaction and a 67% usefulness rating, but no measured agronomic accuracy [11]. | Treat as vendor-reported adoption, not proof of safe diagnosis or yield impact. | C |
| WeFarm | Nesta case study, accessed 2026-08-16; https://www.nesta.org.uk/feature/ai-and-collective-intelligence-case-studies/wefarm | The located evidence describes peer-to-peer agricultural information through SMS without internet, not collection of voice notes. | Useful as text routing precedent; unsuitable evidence for voice capture. | C |
| African IVR question precedent | Ethiopia 8028 Farmer Hotline, accessed 2026-08-16; https://ati.gov.et/8028-farmer-hotline | An IVR-based help desk lets farmers ask questions and receive real-time expert responses [21]. | Transferable concept, but the source does not document DTMF versus recording, evaluation results, or reviewer credentials. | C |
| Low-literacy delivery efficacy | Digital extension trial, Andhra Pradesh, 2023; https://onlinelibrary.wiley.com/doi/full/10.1002/jaa2.42 | In-person video plus mobile IVR/SMS increased recall, knowledge, and adoption. Platform logs show 93.79% picked up at least one IVR, with 31.21 seconds average listening [18]. | Strong for layered delivery, but not isolated proof of problem-capture accuracy. | A |
| SMS comprehension boundary | Haryana agri-met study, 2021; https://www.sciencedirect.com/science/article/pii/S2212096321000504 | About 70% could read SMS; some illiterate farmers asked children to read regional-language messages. Apps and online transactions were used by only a small minority [16]. | SMS should be redundant with voice, not the sole low-literacy channel. | A |
| Agricultural Odia ASR benchmark | "Benchmarking Automatic Speech Recognition for Indian Languages in Agricultural Contexts," arXiv, 2026; https://arxiv.org/html/2602.03868v1 | Tests real agricultural mobile recordings with noise and speaker overlap; best reported Odia WER is 35.1% [12]. | Suitable for risk calibration and model selection; not proof of 8-kHz telephone performance. | A |
| Broad Indian speech data | IndicVoices, 2024; https://arxiv.org/html/2403.01926v1 | Natural and spontaneous speech across 22 languages, 7,348 hours, 16,237 speakers, and 145 districts in the cited version [9]. | Valuable for pretraining, not an agricultural hotline benchmark. | B |
| Official crop-contingency rules | Odisha Crop Contingency Plan 2024; http://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf | Converts crop condition and damage percentage into drainage, gap-filling, retransplanting, varietal, seed-rate, and nutrient actions [14]. | Highest-priority rule source, subject to OUAT/KVK validation and version control. | A |
| Immediate cyclone paddy protection | Odisha scientists' Cyclone Dana advisory, 2024; https://odishatv.in/news/odisha/how-odisha-paddy-farmers-can-minimise-losses-due-to-cyclone-dana-scientists-release-advisory-247268 | Open drains for immature paddy; move and cover harvested rice; dry grain one or two days after rain [10]. | High for a pilot. Timing must be reconciled with current IMD lead time and local safety orders. | A |
| Flood-tolerant rice tradeoff | Dar et al., Scientific Reports, 2013; https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307 | SUB1 restricts elongation under ethylene buildup, improving survival during 7-14 days of submergence without a statistically significant no-flood penalty [17]. | High as a pre-season farm-profile recommendation; not an emergency operation. | A |
| Peru diagnostic-learning analogue | Potato late-blight Farmer Field School study, 2004; https://apsjournals.apsnet.org/doi/10.1094/PDIS.2004.88.5.565 | Uses participatory diagnosis and knowledge-building rather than voice capture. | Useful for designing local symptom cards and reviewer training, but not evidence of IVR utterance structure. | C |
| Published mKisan privacy notice | mKisan, undated, accessed 2026-08-16; https://mkisan.gov.in/Alpha/privacy.aspx | Covers voluntarily submitted contact information and rejects commercial profiling, but says nothing specific about IVR consent, retention, opt-out, or deletion [5]. | Inadequate as the privacy design for recorded farmer problems. | C |
| Voice data as personal data | Digital Personal Data Protection Act 2023, text as of 2025-11-19; https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf | Identifiable digital voice recordings fall within personal-data processing [15]. | Build notice, purpose limitation, withdrawal, deletion handling, and grievance processes before collection. | A |

**Inventory takeaway:** There is enough Grade A evidence to build the interaction skeleton and a small crop-rule library. There is not enough evidence to claim reliable automatic Odia understanding, a clean 22-language KCC corpus, or autonomous diagnosis.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| Odisha government and agronomy | 3 strong items | Few labor-cost, market-price, early-harvest quality, or household-safety tradeoffs; cyclone pages can contain poor metadata | Strong for rule seeding; weak for optimization economics |
| Indian HCI and low-literacy extension | 4 strong studies/pages | Mostly Gujarat, Andhra Pradesh, and Haryana rather than Odisha; elicitation studies rarely publish raw utterance syntax | Strong for channel and prompt design; partial for Odia problem language |
| KCC operations and public data | 2 authoritative sources | "22 languages" applies to service operations, not proven corpus contents; no disclosed row count, raw audio, or full public taxonomy [7][4] | Strong operational precedent; gated as training data |
| ASR and speech corpora | 2 directly useful papers | Agricultural mobile audio is not the same as 8-kHz telephone audio; dialect, code-switching, cyclone wind, and older-speaker performance remain unmeasured | Strong evidence that confirmation is necessary; inadequate for autonomous transcription |
| Voice-first platforms | 4 deployed examples | CGNet is civic, 8028 documentation is sparse, WeFarm is SMS in located evidence, and FarmerChat metrics are self-reported | Good mechanism coverage; mixed outcome evidence |
| Crop physics and recovery | 3 high-value sources | Strong on paddy and flood tolerance; thinner on vegetables, banana, pulses, salinity, livestock feed, storage economics, and action deadlines | Strong paddy MVP; incomplete whole-farm coverage |
| Africa | 2 useful analogues | IVR access is documented, but direct studies of low-literacy symptom vocabulary, dialect structure, and expert-diagnosis disagreement were not located | Transfer evidence only; primary Odisha research still needed |
| Latin America | 1 useful diagnostic-learning analogue | Located work emphasizes participatory learning or WhatsApp information exchange, not controlled voice-problem elicitation | Weak for voice capture; do not overgeneralize |
| Consent and removal | 3 relevant texts/practices | KCC has a six-month recording practice, but a farmer-facing deletion workflow was not located; mKisan is generic; no Ama Krushi voice-data policy was located | Major production gate |

**Coverage judgment:** India supplies a credible design backbone. Africa and Latin America support transferability at the level of participatory extension and IVR access, but they do not establish a universal grammar for how low-literacy farmers verbalize crop problems. That gap should be stated, not filled with cultural assumptions.

## 4. WHAT IS MISSING

The exact research gap is **not** "Can farmers use voice?" Field systems already answer that. The gap is: **Can a short, noisy Odia phone utterance be converted into the minimum safe agronomic state needed to choose a time-critical physical action, while preserving consent and enabling correction?**

| Missing item | What the evidence establishes | What remains unknown | Minimum gap-closing study |
|---|---|---|---|
| Odisha farmer utterance grammar | Farmers can record questions and often introduce themselves first [13]. | Local names for crop, growth stage, water depth, lodging, salinity, color change, and severity; code-switching; indirect or narrative descriptions | Record and manually annotate 1,000 consented problems across coastal, delta, and tribal dialect regions; publish a de-identified slot and vocabulary audit |
| Farmer knowledge versus extension assumptions | Only 70% in one Haryana sample could read SMS, and sophisticated phone use was uncommon [16]. | Whether Odisha farmers reliably know variety names, scientific crop stages, soil classes, acreage, or input concentrations | Ask both jargon and observable-event versions, such as "panicle emergence" versus "has the ear come out?"; compare completion and agronomist agreement |
| Phone-band Odia ASR | Real-world mobile agricultural Odia produced a best WER of 35.1% [12]. | 8-kHz IVR WER, dialect-specific WER, cyclone-wind robustness, entity error rates, and semantic slot accuracy | Benchmark actual callback audio; report crop-name, number, negation, stage, and hazard-slot F1 in addition to WER |
| KCC corpus reality | The page covers 2006-2025 and exposes location, season, and sector metadata [4]. | Row count, languages/scripts, audio linkage, duplication, question/answer quality, consent, licence, and hazard labels | Download audit with data dictionary, language detection, duplicate rate, missingness, sampled agronomist scoring, and consent/licence review |
| Quantified emergency tradeoffs | Drainage, protected storage, drying, and damage-percentage rules exist [14][10]. | Labor-hours, safe lead time, early-harvest quality penalty, expected avoided loss, market access, tarpaulin capacity, and household evacuation conflicts | Randomized or stepped-wedge pilot comparing action timing, labor, cost, crop loss, quality, and safety compliance |
| Non-paddy crop rules | The state plan contains broad contingencies. | Decision-grade cyclone rules for vegetables, banana, coconut, pulses, nurseries, seed stores, and salinity recovery | Crop-specific OUAT review panels and controlled field validation; no automatic rule release from a single document |
| Consent and removal | KCC retains recordings for six months; mKisan's policy does not describe voice deletion [7][5]. | How a feature-phone farmer hears notice, withdraws consent, obtains a case ID, deletes audio, or preserves an advisory while deleting identity | DTMF consent usability test plus end-to-end deletion audit using a spoken case code and toll-free grievance route |
| Learning-loop efficacy | FarmerChat describes RAG, expert-validated data, feedback, and RLHF [11]. | Review turnaround, disagreement rate, unsafe-answer rate, rule-change governance, and whether feedback improves crop outcomes | Shadow-mode trial: AI drafts only; blinded agronomists score safety, relevance, and completeness before farmer delivery |

The principal scientific risk is **state misidentification**. A farmer may report "the plant has fallen" without distinguishing wind lodging, root rot, waterlogging, stem borer, or harvest maturity. No amount of generic weather context safely resolves that ambiguity without targeted follow-up questions, a photo where available, or human review.

## 5. HOW IT FEEDS THE ADVISORY ENGINE

### A working end-to-end capture loop

1. **Callback and minimal notice:** The farmer gives a missed call. The system calls back, states the purpose and retention period in Odia, and asks for consent by keypress. The farmer can press another key to hear deletion and grievance instructions.
2. **DTMF skeleton:** Select language/dialect, urgent weather versus crop problem, crop family, and whether a photo is available. Avaaj's evidence favors keypad navigation over voice commands [13].
3. **Short spoken narrative:** Ask: "Say your village, crop, what you see, when it started, and whether the field has standing water." Permit replay, rerecord, or agent transfer. Start with a 30-45 second limit, modeled on Avaaj's 30-second recordings [13].
4. **Observable follow-ups:** Do not ask only "What growth stage?" Ask event-anchored alternatives: days since sowing, flowering visible, grain hard or soft, water relative to ankle/knee, percentage of field affected, and whether plants are bent, uprooted, yellow, or submerged.
5. **ASR plus slot extraction:** Run an Odia/dialect ASR ensemble, but retain separate confidence scores for crop name, quantity, negation, stage, location, and hazard. WER alone is not a safety score.
6. **Read-back confirmation:** "I heard: immature paddy, water entering, half the field affected. Press 1 if correct, 2 to change, 3 for a person." Low-confidence numbers, crop names, and negations always require confirmation.
7. **Farm-state fusion:** Join confirmed slots to IMD alert, rainfall, wind, elevation, drainage, soil, sowing date, variety, previous advice, labor availability, and storage location.
8. **Rule and retrieval layer:** Deterministic crop-safety rules handle time-critical actions. Retrieval-augmented generation may explain an approved rule, but it must not invent the action. KCC examples can support retrieval only after corpus auditing.
9. **Human review queue:** An agronomist receives the audio, transcript, confidence, field profile, retrieved evidence, and proposed action. Novel symptoms, conflicts, chemicals, fumigation, severe crop loss, and low-confidence cases cannot bypass review.
10. **Outcome feedback:** After the event, call back: "Did you do the action? How much area? What happened?" Store the response as an outcome label, not as automatically trusted truth. Repeated reviewed patterns become FAQ candidates or rule-change proposals.

### Captured problem to algorithm, rule, or feature

| Captured feature | Engine component | Immediate use | Learning use after review |
|---|---|---|---|
| Local crop and variety name | Phonetic alias dictionary plus crop ontology | Resolve to approved crop/variety ID | Add a new alias only after language and agronomy review |
| Sowing/transplant date and observable stage | Stage estimator with event-based fallback | Select stage-specific action and deadline | Calibrate stage estimates against field-agent observations |
| Symptom, plant part, color, smell, lodging | Multi-label symptom classifier | Generate discriminating follow-up questions, not a final diagnosis | Add reviewed symptom-diagnosis pairs to a case library |
| Water depth, duration, field fraction | Flood-state rule engine | Choose drainage, gap-fill, retransplant, or escalation | Re-estimate outcome thresholds after local trials |
| IMD hazard, forecast lead time, local rainfall/wind | Hazard fusion and urgency score | Determine whether the action is still safe and feasible | Calibrate false alarms and missed-event costs |
| ASR confidence by slot | Safety policy | Read back, repeat, use DTMF, or transfer to agent | Active-learning queue for dialect and noise examples |
| Farmer action and observed outcome | Causal evaluation store | No immediate model update | Promote only agronomist-approved, repeated evidence into FAQ/rules |
| Consent, retention choice, case code | Consent ledger | Control recording, training eligibility, and deletion | Audit compliance; never use withdrawn data for new training |

### Crop-level evacuation and protection rules

The decision objective should be explicit:

`Net expected benefit = event probability x exposed yield/value x expected loss avoided - labor cost - quality penalty - safety risk - opportunity cost.`

A rule fires only if the action remains physically possible and safe before the forecast deadline. If a tradeoff term is unknown, the system should disclose uncertainty or escalate rather than insert a fabricated number.

| Field state | Physical action | Crop physics and expected benefit | Quantified tradeoff or guardrail |
|---|---|---|---|
| Non-mature paddy before heavy rain | Open and clear drainage channels; route water to a safe outlet | Shortens waterlogging and root-zone oxygen stress; this is protection of a standing crop rather than literal relocation [10]. | Do not send farmers into fields after unsafe wind or flood conditions begin; local drainage capacity must be known. |
| Harvested paddy exposed to rain | Move stacks to higher/safe storage, cover with tarpaulin, then sun-dry grain for one or two days after rain | Prevents repeated wetting and reduces grain moisture before bagging [10]. | Requires labor, dry space, and covers. If safe transport time is unavailable, household evacuation outranks crop movement. |
| Flooded rice with less than 50% plant loss | Drain, then gap-fill using clonal material | Preserves surviving stand and avoids full re-establishment [14]. | The 50% assessment itself needs farmer confirmation or field-agent/photo review. |
| Flooded rice with more than 50% plant loss | Retransplant an appropriate medium-duration crop | Rebuilds stand where gap-filling is unlikely to recover population [14]. | Depends on remaining season, seedling availability, and receding water; it is not universally feasible. |
| Delayed rice transplantation | Use medium-duration seedlings up to 45 days old or late-duration seedlings up to 60-70 days; use 5-7 seedlings per hill | Compensates for delayed establishment and reduced tillering opportunity [14]. | Must be linked to locally approved varieties and current season length. |
| Recurrently flood-prone farm before sowing | Offer Swarna-Sub1 or locally approved SUB1-compatible seed | Restricted elongation conserves plant resources during submergence. Estimated advantage was about 45% at 10 flood days and up to 718 kg/ha near 13 days [17]. | It is a seasonal preparedness choice, not a 48-hour evacuation action. The no-flood estimate was -5.3% but not statistically significant [17]. |
| Stored grain infestation after cyclone rain | Escalate to a storage specialist rather than automatically prescribing fumigant | The cited advisory discusses airtight aluminium-phosphide fumigation for 7-10 days [10]. | This is a high-risk chemical operation. The AI should give containment and expert-contact instructions, not an unsupervised dosage. |

### Who reviews what

- **Odia language reviewer:** dialect, crop aliases, code-switching, and mistranscription.
- **Block/KVK agronomist:** crop state, action, quantity, deadline, and contraindications.
- **OUAT/ICAR subject specialist:** novel symptoms, rule conflicts, chemicals, salinity, seed variety, and post-disaster recovery.
- **Disaster-operations reviewer:** whether the advised field action conflicts with evacuation, road closure, wind, lightning, or flood safety.
- **Data steward:** consent scope, training eligibility, retention clock, deletion, and grievance resolution.
- **Rule-change board:** approves versioned changes after reviewing case volume, agronomist agreement, outcomes, and safety incidents. KCC's first-line-advisor-to-specialist escalation is a practical institutional precedent [7].

## 6. REAL-vs-FILLER

| Claim or component | Classification | Evidence-based interpretation | Product decision |
|---|---|---|---|
| Farmers can record useful questions on ordinary phones | **Verified** | Avaaj received 610 questions; CGNet supports callback, recording, and moderation [13][6]. | Build it. |
| Simple DTMF beats voice menus for navigation | **Verified in one Indian field study** | Touchtone was selected significantly more often and unanimously preferred in interviews [13]. | Make DTMF the default control plane. |
| Voice delivery helps low-literacy access | **Verified, with attribution limits** | Supplementary mobile messages improved knowledge and adoption in a mixed video-plus-mobile intervention, but not yield [18]. | Use voice, but evaluate capture and delivery separately. |
| FarmerChat supports voice, text, photo, RAG, and expert-validated knowledge | **Verified as documented functionality** | The official page states these mechanisms [11]. | Treat as an architecture precedent. |
| FarmerChat is agronomically accurate at scale | **Marketing or unverified** | Reach, satisfaction, and usefulness are reported, but no diagnostic/advisory accuracy percentage or review turnaround is given [11]. | Do not use in a safety claim. |
| WeFarm is a voice-note capture system | **Filler in the located evidence** | The source found describes SMS peer exchange without internet. | Do not cite it for voice. |
| KCC public data is a 22-language transcript corpus | **Unsupported conflation** | KCC service answers in 22 languages, while the public metadata does not prove raw multilingual transcripts or audio [7][4]. | Audit before use or claim. |
| KCC has a known dataset size | **Unsupported** | 222,996 downloads and 249,422 views are shown, but no row count or byte size is disclosed [4]. | Report size as "not established." |
| "IndicVoices Odia WER is 23.4" | **Unsupported by the located benchmark** | The agricultural benchmark's best Odia WER is 35.1%; 23.4 does not appear in that evidence [12]. | Remove 23.4 from the pitch. |
| Translation across 22 Indian languages solves speech capture | **Lab-category mismatch** | IndicTrans2 supports translation across 22 scheduled languages, not noisy rural ASR [22]. | Use translation only after speech is safely captured. |
| Photo-only diagnosis is sufficient | **Lab-only unless field validated** | A photo cannot by itself establish water duration, variety, crop stage, field fraction, or recent operations. | Pair photo with voice slots and human review. |
| AI should automatically learn from every farmer report | **Unsafe filler** | Farmer statements are observations, not verified labels; feedback may contain mistaken diagnoses or confounded outcomes. | Learn through an active-learning queue with consent and agronomist approval. |
| Standing crops can be "evacuated" | **Misleading wording** | Most standing crops are protected through drainage, staking where validated, selective harvest, or seasonal variety choice. Harvested output, seed, nursery material, and equipment can be moved. | Say "crop protection and recoverable-yield evacuation." |

The key real-versus-filler distinction is **workflow evidence versus outcome evidence**. A deployed interface proves that people can use it; it does not prove that the diagnosis is correct, the action is safe, or crop loss falls.

## 7. NOISE LOG

| Noisy lead or contradiction | Why it is noisy | Resolution |
|---|---|---|
| The supplied "Odia 23.4 WER" figure | Not present in the located 2026 agricultural benchmark; its best Odia result is 35.1% [12]. | Reject the number unless a separate named model, split, and test condition are produced. |
| "KCC transcripts contain questions in 22 languages" | The official guide establishes 22-language service, not 22-language raw public records [7][4]. | Separate operating-language coverage from dataset-language coverage. |
| KCC download and view counts treated as row counts | They are page-use metrics, not corpus size [4]. | State that record count remains undisclosed. |
| Search results for KCC mixed with Kisan Credit Card | The same acronym produces finance pages rather than call-centre data. | Require the full phrase "Kisan Call Centre" and official agriculture domains. |
| WeFarm described as collecting voice notes | The located case study describes SMS. | Exclude it from voice evidence; retain only as offline peer-routing precedent. |
| Gram Vaani/Mobile Vaani claims without an evaluated workflow source | Search results were dominated by company/social profiles rather than primary interaction studies. | Do not use it as core evidence until prompt, moderation, and outcome documentation is obtained. |
| WhatsApp voice-note claims for Latin America | Search results mainly covered general chat-app information exchange, not controlled crop-problem elicitation by low-literacy farmers. | Treat WhatsApp as an optional channel, not a proven LatAm elicitation model. |
| FarmerChat scale equated with accuracy | Its official page reports reach and satisfaction, not unsafe-answer or agronomic-accuracy rates [11]. | Mark figures self-reported and require shadow-mode evaluation. |
| ASR benchmark equated with telephone performance | The benchmark uses real-world mobile agricultural recordings, but no 8-kHz IVR result is established. | Run a local callback benchmark before setting automation thresholds. |
| One symptom mapped directly to one diagnosis | Lodging, yellowing, wilting, and spots can have multiple biotic, abiotic, and management causes. | Ask discriminating follow-ups and use human review. |
| "Latest frontier science" used as a substitute for deployability | New germplasm or image models may be scientifically interesting without local seed availability, economics, or field validation. | Prefer an older Odisha randomized result over a newer unvalidated claim. |
| Official fumigation text copied directly into AI advice | The source specifies aluminium phosphide under airtight tarpaulin for 7-10 days [10], but the operation is safety-critical. | Convert it to specialist escalation, not a self-service instruction. |
| mKisan privacy notice assumed to cover voice deletion | It does not discuss IVR recording consent, retention, opt-out, or deletion [5]. | Write a dedicated spoken-data policy and deletion SOP. |
| Lack of Africa/LatAm utterance studies interpreted as universal behavior | Voice and participatory systems transfer at the mechanism level, not necessarily vocabulary or narrative structure. | Conduct Odisha primary elicitation rather than importing a universal grammar. |

## 8. VERDICT: GATED - SYNTHESIS

**Verdict: GATED.** Proceed with a prototype and supervised field pilot. Do not launch autonomous, statewide crop advice until the ASR, crop-rule, consent, and outcome gates below pass.

### Comparative synthesis

| Strategy | Mechanism | Scope | Main tradeoff | Evidence base | Appropriate horizon |
|---|---|---|---|---|---|
| One-way IMD plus SMS/IVR alerts | Push forecast and generic advice | Broad and fast | Accessible but does not capture the farmer's actual state; SMS still excludes some readers | Haryana and Andhra evidence supports usefulness and behavior change, not guaranteed yield [18][16] | Immediate baseline |
| CGNet/Avaaj-style voice forum | Callback, record, listen, moderate | Bottom-up problem collection | Inclusive and cheap, but navigation, backlog, misinformation, and specialist capacity constrain scale | Strong Indian field/deployment precedents [13][6] | Immediate capture layer |
| FarmerChat-style multimodal AI | Voice/text/photo plus retrieval and localized response | Rich smartphone interactions | More context, but official reach and satisfaction are not agronomic accuracy; feature-phone coverage is weaker | Documented capability, limited independent safety evidence [11] | Supervised pilot |
| Proposed closed-loop crop-action engine | DTMF plus voice slots, IMD/farm fusion, deterministic safety rules, agronomist review, and outcome feedback | Hyperlocal pre- and post-disaster decisions | Higher operational cost and slower handling of ambiguous cases, but errors are visible and correctable | Components are supported separately; the integrated loop remains to be validated | Gated field trial |

The non-obvious tension is that **the most inclusive input mode is also the least machine-reliable**. Voice removes reading barriers, but Odia agricultural ASR errors are high enough to corrupt crop names, numbers, stages, and negation. Therefore, accessibility and automation cannot be treated as the same objective. DTMF, read-back confirmation, and human escalation are not temporary workarounds; they are core safety mechanisms.

A second tension is between **immediate action and scientifically strongest evidence**. The best quantified Odisha result, Swarna-Sub1, is a pre-season variety decision, while the most urgent cyclone actions - drainage, protected stacking, drying, and retransplanting - have official agronomic support but thinner economic effect estimates. The engine should clearly label each recommendation as seasonal preparedness, pre-impact physical action, post-impact recovery, or expert-only intervention.

### Release gates

1. **Capture gate:** At least 90% completion of consent, crop selection, recording, replay, and confirmation among low-literacy pilot users, disaggregated by gender, age, dialect, and phone type.
2. **Semantic gate:** Agronomist agreement on crop, stage, hazard, severity, and timing slots; no reliance on aggregate WER alone.
3. **Safety gate:** Zero unreviewed chemical, fumigation, destructive harvest, or evacuation-conflicting recommendations during shadow mode.
4. **Agronomy gate:** Every production rule has source, crop, stage, trigger, action, deadline, contraindication, reviewer, and version fields.
5. **Data gate:** Spoken notice, explicit consent, training opt-in separate from service consent, case-code access, withdrawal, deletion, retention expiry, and grievance handling work on a feature phone.
6. **Outcome gate:** A controlled pilot measures action uptake, labor and cost, crop loss, grain quality, false alarms, missed events, and safety incidents. Knowledge gain alone is insufficient because prior mobile extension improved knowledge and adoption without improving yield [18].

**Recommended demo scope:** implement missed-call callback, Odia plus one local dialect, DTMF consent and crop selection, a replayable 30-second problem recording, slot read-back, human agronomist dashboard, and six versioned paddy actions: drainage, protected stacking, post-rain drying, less-than-50% gap-filling, more-than-50% retransplanting, and pre-season SUB1 recommendation. Add the post-event feedback call. That is both feasible and genuinely distinctive; autonomous diagnosis, universal crop coverage, and automatic model retraining are not yet defensible.

## References

1. *AIKosh*. https://aikosh.indiaai.gov.in/home/datasets/details/kisan_call_centre_kcc_transcripts_of_farmers_queries_and_answers.html
2. *WeFarm | Nesta*. https://www.nesta.org.uk/feature/ai-and-collective-intelligence-case-studies/wefarm
3. *FarmerChat | Digital Green*. http://digitalgreen.org/farmerchat
4. *Kisan Call Centre (KCC) - Transcripts of farmers queries  answers | Open Government Data (OGD) Platform India*. https://www.data.gov.in/resource/kisan-call-centre-kcc-transcripts-farmers-queries-answers
5. *mKisan:Privacy Policy*. https://mkisan.gov.in/Alpha/privacy.aspx
6. *CGNet Swara | The Communication Initiative*. http://global.comminit.com/content/cgnet-swara
7. *Kcc Website*. https://agriwelfare.gov.in/sites/default/files/KCC%20WEBSITE.pdf
8. *dl.acm.org*. https://dl.acm.org/doi/pdf/10.1145/1753326.1753434
9. *IndicVoices: Towards building an Inclusive Multilingual Speech Dataset for Indian Languages*. https://arxiv.org/html/2403.01926v1
10. * How Odisha paddy farmers can minimise losses due to Cyclone Dana; scientists release advisory*. https://odishatv.in/news/odisha/how-odisha-paddy-farmers-can-minimise-losses-due-to-cyclone-dana-scientists-release-advisory-247268
11. *FarmerChat — AI Advisory for Farmers · Digital Green Trust*. https://www.digitalgreentrust.org/farmerchat
12. *Benchmarking Automatic Speech Recognition for Indian Languages in Agricultural Contexts*. https://arxiv.org/html/2602.03868v1
13. *Avaaj Otalo — A Field Study of an Interactive Voice Forum for Small Farmers in Rural India*. http://tap2k.org/papers/pap0310-patel.pdf
14. *CROP CONTINGENCY PLAN 2024 FINAL.pdf*. http://agrisnetodisha.ori.nic.in/CROP%20CONTINGENCY%20PLAN%202024%20FINAL.pdf
15. *The Digital Personal Data Protection Act, 2023*. https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf
16. *Do phone-based short message services improve the uptake of agri-met advice by farmers? A case study in Haryana, India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212096321000504
17. [
            Flood-tolerant rice reduces yield variability and raises expected yield, differentially benefitting socially disadvantaged groups - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307)
18. *Digital tools for rural agriculture extension: Impacts of mobile‐based advisories on agricultural practices in Southern India - Singh - 2023 - Journal of the Agricultural and Applied Economics Association - Wiley Online Library*. https://onlinelibrary.wiley.com/doi/full/10.1002/jaa2.42
19. *Management of Potato Late Blight in the Peruvian Highlands: Evaluating the Benefits of Farmer Field Schools and Farmer Participatory Research | Plant Disease*. https://apsjournals.apsnet.org/doi/10.1094/PDIS.2004.88.5.565
20. *Using Data for Development: Evidence from a Phone System for Agricultural Advice*. https://www.povertyactionlab.org/sites/default/files/research-paper/working-paper_9244_Data-for-Development-Phone-System-for-Ag-Advice_Ethiopia_Oct2020.pdf
21. *8028 Farmer Hotline - Agricultural Transformation Institute*. https://ati.gov.et/8028-farmer-hotline
22. *http://openreview.net/forum?id=vfT4YuzAYA*. http://openreview.net/forum?id=vfT4YuzAYA
