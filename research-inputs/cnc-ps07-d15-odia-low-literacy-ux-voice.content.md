# KrishiSetu Odia Voice UX: Prototype Ready, Pilot Gated

## 1. EXECUTIVE SUMMARY

- **Local Delivery Proof**: Odisha already has a voice-first agricultural precedent in Ama Krushi: customized outbound calls, a 155333 inbound line, IVR, live-agent and expert escalation, operation across all 30 districts, and roughly 50,000 inbound calls per month. This validates voice as a real channel, not a hackathon assumption, but it does not make KrishiSetu's cyclone advice automatically safe or comprehensible [46]. -> Reuse the operating pattern, then separately validate disaster-specific scripts.
- **Translation Is Prototype-Ready, Not Publication-Ready**: IndicTrans2 covers all 22 scheduled Indian languages, including Odia, and distills 1.2B-parameter models to 200M parameters; its BPCC corpus contains 230M bitext pairs [11]. The authors also warn that automated metrics may not reflect real-world effectiveness and did not conduct full-scale human evaluation [11]. -> Use it to draft bounded advisories, never to send unreviewed emergency text.
- **Tokenizer Choice Can Break Odia**: In one zero-shot Oriya named-entity experiment, SentencePiece achieved F1 81.08 while BPE achieved F1 0.00, even though their token-level accuracies looked similar [9]. -> Freeze and test the exact tokenizer-model pair on villages, crop names, place names, numerals and units; do not treat aggregate accuracy as sufficient.
- **ASR Exists, But Dialect Evidence Does Not**: Google officially lists `or-IN` only for Chirp 2/3 configurations in specified regions [41]. Azure lists Odia for fast transcription and custom speech [28]. IndicVoices supplies 75 Odia training hours from 391 speakers plus a 5-hour, 92-speaker test set, but its reported IndicASR Odia WER is 23.4 and no coastal, western, tribal or code-switching split is published [43]. -> Treat ASR as optional intent capture with DTMF and human fallback, not as the sole emergency-control path.
- **Native Odia TTS Is The Main Technical Gap**: The reviewed Google and Azure official voice lists do not expose an Odia voice [40][55]. AI4Bharat's IndicF5 does support Odia, has 0.4B parameters and an MIT license, but its model card provides no Odia-specific MOS or emergency-vocabulary intelligibility score [59]. -> For the prototype, prefer recorded human prompts plus carefully reviewed synthesized variable slots.
- **BHASHINI Is A PoC Route, Not Yet A Costed Production Dependency**: Government documentation exposes ASR, TTS and translation tasks and a Search -> Config -> Compute pipeline [20][45]. The public API documentation says it is for proof-of-concept use and directs paid production users to contact BHASHINI; no reviewed page supplied a public Odia production tariff, SLA, quota or current service-ID matrix [45]. -> Integrate behind an adapter and keep an offline fallback.
- **Shallow IVR And Callback Are Evidence-Based**: Avaaj Otalo used a three-choice top menu and recorded 6,975 calls from a 51-farmer deployment; users wanted topic categories and trusted credentialed experts [17]. CGNet Swara used a free missed-call callback with only two principal choices and logged 70,500 calls and 9,100 listeners [33]. -> Use one decision per prompt, replay, numeric keys, callback and expert escalation.
- **SMS Is A Receipt, Not Proof Of Understanding**: IMD's GKMS procedure specifies vernacular SMS highlights of at most 262 characters and Tuesday/Friday dissemination [56]. In Haryana, 70% of study farmers could read SMS, yet only 25% had smartphones; information changed some timing decisions and rainfall-related irrigation behavior but did not improve yields [34]. -> Pair SMS with voice, confirmation and an explicit next action.
- **Effectiveness Depends On Comprehension And Complementary Support**: An Andhra Pradesh randomized trial spanning 332 communities and 2,014 final participants found knowledge and practice adoption gains from video plus IVR/SMS, but no significant production or yield effect [10]. -> A production pilot is gated on measured Odia task comprehension, call completion, correct action and escalation, not message delivery counts.

## 2. DATA INVENTORY

**Reliability rubric:** **A** = peer-reviewed evidence or first-party technical/operational specification; **B** = official operational source or well-documented field deployment without independent impact validation; **C** = provider/model card, project self-report or evidence transferred from another language/context; **D** = inaccessible, promotional or unverified lead.

### 2.1 Odia NLP resources, tokenization and small-model capability

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| Odia machine translation | IndicTrans2, OpenReview, published Dec. 20, 2023, https://openreview.net/forum?id=vfT4YuzAYA | Supports all 22 scheduled Indian languages; BPCC has 230M bitext pairs, including 126M newly added pairs and 644K manually translated pairs [11]. | **High for prototype drafting**. Use constrained templates and human review. Do not let free-form translation trigger a disaster action. | **A** |
| Edge-sized translation | IndicTrans2, same source | 1.2B-parameter teacher models were distilled to 200M parameters without reported performance compromise [11]. | **Medium-high**. Plausible for an edge gateway or district server; device latency and memory still require measurement on the actual hardware. | **A** |
| Translation-quality limit | IndicTrans2, same source | The paper says automated metrics may not reflect real-world effectiveness and full-scale human evaluation was infeasible [11]. | **Critical constraint**. Odia expert approval and farmer comprehension testing remain mandatory. | **A** |
| Odia tokenizer evidence | Tokenization study, arXiv, 2024, https://arxiv.org/abs/2410.13401 | The Oriya dataset had 196,793 training sentences, 993 validation sentences and 994 test sentences [9]. In the zero-shot result, SentencePiece F1 was 81.08 versus BPE F1 0.00 [9]. | **High-value test guidance**, not a universal benchmark. Evaluate names of blocks, gram panchayats, crops and inputs. | **A** |
| Small Odia LLM benchmark | IndicGenBench/AI4Bharat search trail, accessed Aug. 16, 2026 | The reviewed material establishes broad Indian-language benchmark activity but did not expose a decision-ready Odia-by-model matrix for small, edge-suitable LLMs. | **Gated**. Do not claim that a specific small LLM understands agronomic Odia until tested on the product corpus. | **D** |
| Safer generation pattern | Synthesis from translation evidence | Structured record -> approved Odia template -> variable insertion is more controllable than unconstrained Odia generation. | **High**. This should be KrishiSetu's default warning path. | **B** |

The practical conclusion is not "Odia NLP is solved." It is that Odia translation has a credible open foundation, while domain safety remains a product-owned evaluation problem. The tokenizer result is especially important because a superficially acceptable accuracy can coexist with unusable entity extraction [9].

### 2.2 Odia ASR, TTS and price visibility

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| Google Odia ASR | Google Cloud Speech-to-Text supported languages, accessed Aug. 16, 2026, https://cloud.google.com/speech-to-text/v2/docs/speech-to-text-supported-languages | `or-IN` is listed for Chirp 2/3 in specified regions, rather than across every recognizer [41]. | **Medium**. Suitable for a connected prototype; preserve region/model configuration and test telephone-band audio. | **A** |
| Google ASR cost | Google Cloud STT pricing, accessed Aug. 16, 2026, https://cloud.google.com/speech-to-text/pricing | V2 standard recognition starts at **USD 0.016/minute** for the first usage tier; dynamic batch is **USD 0.003/minute** [21]. | **Medium**. Affordable for experiments, but batch pricing is not a real-time IVR substitute. Telephony and callback charges are additional. | **A** |
| Google Odia TTS | Google Cloud TTS voice list, accessed Aug. 16, 2026, https://cloud.google.com/text-to-speech/docs/voices | The reviewed official list contains no Odia/`or-IN` voice entry [40]. | **No native Odia production path identified**. Generic Google TTS pricing does not cure language absence. | **A** |
| Azure Odia ASR | Microsoft Speech language support, accessed Aug. 16, 2026, https://learn.microsoft.com/azure/ai-services/speech-service/language-support | Odia `or-IN` is listed for fast transcription; custom speech can use human-labeled audio [28]. | **Medium-high for experimentation**, especially if a licensed farm-speech corpus can be collected. | **A** |
| Azure speech cost | Microsoft Azure Speech pricing, accessed Aug. 16, 2026, https://azure.microsoft.com/pricing/details/cognitive-services/speech-services/ | Reviewed pricing showed **USD 1/audio hour** for standard real-time STT, **USD 0.18/audio hour** for batch, and 5 free audio hours per month [19]. | **Medium**. Verify account region and current quote before budgeting. | **A** |
| Azure Odia TTS | Microsoft Speech language support, accessed Aug. 16, 2026, same URL | Odia is not present in the reviewed neural voice list [55]. | **No native Odia production path identified** despite generic neural-TTS pricing. | **A** |
| Open Odia speech corpus | IndicVoices, arXiv, Mar. 4, 2024, https://arxiv.org/abs/2403.01926 | Odia split: 391 speakers/75 hours train, 92 speakers/5 hours test, and 1 speaker/1 hour validation [43]. Dataset license is CC BY 4.0; tools are MIT [43]. | **High for baseline research**, insufficient by itself for Odisha dialect/noise certification. | **A** |
| Open ASR quality signal | IndicVoices/IndicASR, same source | Reported Odia WER is **23.4**, with no reviewed Odia dialect, telephone-noise or code-switch split [43]. | **Partial**. Use for intent suggestions or transcript assistance, not irreversible action. | **A** |
| Open Odia TTS | AI4Bharat IndicF5 model card, 2025, https://huggingface.co/ai4bharat/IndicF5 | Supports Odia among 11 languages; model size 0.4B; MIT license; reference audio controls voice/prosody [59]. No hosted inference provider is listed [59]. | **High for local prototype**, conditional on consent for reference voices and local intelligibility testing. | **B** |
| Open TTS quality | IndicF5 model card, same source | The card describes training over 1,417 hours overall but gives no Odia-specific MOS, disaster-vocabulary or number/unit score [59]. | **Gated for pilot**. A human-recorded voice remains safer for fixed warning phrases. | **C** |

**Cost finding:** the only clear public Odia speech prices found are for cloud ASR. Google and Azure generic TTS tariffs are not actionable for native Odia because their reviewed voice catalogs lack Odia. IndicF5 has no per-call license tariff, but local compute, telephony, monitoring and voice-consent costs remain real. No evidence supports calling any of these options "free production speech."

### 2.3 BHASHINI services, access, cost and quality

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| Task families | Government BHASHINI portal, accessed Aug. 16, 2026, https://bhashini.gov.in | Portal documentation names ASR, TTS and NMT task families and includes Odia in its language selector [20]. | **Promising**, but a language selector does not prove that every task has a currently deployable Odia model. | **A** |
| API workflow | BHASHINI API documentation, accessed Aug. 16, 2026, https://bhashini.gitbook.io/bhashini-apis | Pipeline Search returns pipeline/model identifiers, followed by Config and Compute calls [45]. | **High for an adapter-based PoC**. Cache model IDs and fail safely if discovery changes. | **A** |
| Production terms | BHASHINI API documentation, same source | Public documentation limits described access to PoC use and directs paid production use to BHASHINI/pricing contact [45]. | **Pilot blocker until written terms exist**. | **A** |
| Public Odia quality | Same official sources | No reviewed page supplied Odia ASR WER by dialect, Odia TTS MOS/intelligibility, or translation human-evaluation results for agricultural warnings. | **Unknown**. Run a bake-off rather than infer quality from availability. | **D** |
| Public tariff/SLA | Same official sources | No public production tariff, quota, latency target, uptime SLA or current Odia task-ID inventory was found in the reviewed official documentation [45]. | **Gated**. Procurement and service continuity cannot yet be costed. | **D** |

BHASHINI should therefore be one pluggable provider, not KrishiSetu's hard-coded dependency. A provider-neutral contract should accept text/audio and return a result plus language, model, confidence and latency metadata; recorded prompts and DTMF must continue to work if discovery or inference fails.

### 2.4 IVR design evidence from India

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| Avaaj Otalo | Patel et al., ICTD/ACM, Apr. 10, 2010, https://dl.acm.org/doi/10.1145/2369220.2369230 | Seven-month Gujarati deployment with 51 farmers in four districts; 6,975 calls, around five minutes each [17]. | **Highly transferable interaction pattern**, but not an Odia cyclone-effectiveness estimate. | **A** |
| Menu design | Avaaj Otalo, same source | Top level: ask question, announcements, radio; question sub-menu: record or hear others. Users wanted topic categories, and 65% preferred staff-only answers [17]. | **Use a shallow emergency menu**, but skip community-browse complexity during a warning. | **A** |
| Expert trust | Avaaj Otalo, same source | Farmers preferred credentialed expert answers [17]. | **High**. Identify the issuing authority and offer expert escalation. | **A** |
| CGNet Swara | Mudliar et al., ICTD, 2012, https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/cgnet-ictd2012.pdf | Press 1 to record, 2 to listen; missed call triggers free callback. Deployment logged 70,500 calls, 1,100 recordings and 9,100 listeners [33]. | **High** for callback and two-choice interaction. Moderation remains essential. | **A** |
| Gram Vaani | Gram Vaani, May 27, 2021, https://gramvaani.org/community-media-platforms/ | Missed-call callback, leave/hear model; source reports 2,000 calls/day and more than 35,000 users in Jharkhand [42]. | **Operationally plausible**, but source lacks measured comprehension or agronomic outcomes. | **B** |
| Low-literacy controls | Medhi et al., ACM TOCHI, Apr. 2011, https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/TOCHI-low-literacy.pdf | Ethnography covered 90 subjects. In the Bangalore experiment, task completion was 0% for text, 72% for voice and 100% for a graphical interface with prerecorded instruction [58]. | **Strong adjacent evidence** for voice, numeric keys and optional graphics. Not Odia-specific and not an emergency trial. | **A** |
| Human fallback | Medhi et al., same source | Electronic forms and SMS had mean error rates of 4.2% and 4.5%, compared with 0.45% for a live operator; the authors recommend human escalation [58]. | **Mandatory for ambiguous/high-risk cases**. | **A** |
| MeraVote | Exact-name and deployment searches, accessed Aug. 16, 2026 | No credible primary publication with menu or comprehension data was located. | **Not usable as evidence**. | **D** |

**Case study - Avaaj versus CGNet:** Avaaj demonstrates that farmers will spend time in an agriculture-specific audio community, but its sequential browsing and demand for topic categories show how voice menus become difficult as content grows [17]. CGNet took the opposite route: a missed call, server callback and two primary choices, with journalist moderation [33].

For KrishiSetu, the contrast favors the CGNet interaction envelope during a cyclone: callback, one message, replay, confirm, request help. Avaaj's richer browsing belongs in a non-emergency advisory library. Neither deployment supplies an Odia warning-comprehension rate, so both are design precedents rather than pilot validation.

### 2.5 SMS comprehension, language mixing and pictograms

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| IMD operational SMS | IMD GKMS Standard Operating Procedure, 2020, https://mausam.imd.gov.in/responsive/pdf_viewer_css/met2/Chapter%20I/1.3%20GKMS.pdf | SMS should carry bulletin highlights, use vernacular language and stay within 262 characters; bulletins are prepared/disseminated Tuesday and Friday [56]. | **High as a transport constraint**, not a comprehension rule. Cyclone alerts also require event-driven updates. | **A** |
| Hindi SMS comprehension proxy | Fafchamps and Minten, Haryana field study, published version at https://www.sciencedirect.com/science/article/pii/S0304387812000695 | Among 463 analysis farmers, 70% could read SMS and 25% had smartphones [34]. Messages affected some input-timing and crop-practice decisions [34]. | **Medium transferability**. It supports short, timely, specific messages but not Odia wording. | **A** |
| Yield limit | Same Haryana study | Information induced a 9 percentage-point substitution away from irrigation after rainfall, but the study found no yield effect [34]. | **Important caution**. Engagement or behavior change is not equivalent to crop-loss reduction. | **A** |
| Odia versus Odia-English | Search across agricultural-extension and usability studies, accessed Aug. 16, 2026 | No robust head-to-head study was found for Odia script, Romanized Odia, or Odia-English code-mixing among Odisha farmers. | **Unknown**. Must be tested by district and literacy profile. | **D** |
| Message length understood | IMD plus comprehension-study search | The 262-character figure is an IMD operational maximum, not a demonstrated comprehension optimum [56]. | **Gated**. Test action accuracy at multiple lengths instead of treating 262 as a target. | **D** |
| Pictograms | Medhi low-literacy study, Apr. 2011 | A graphical interface with prerecorded instruction reached 100% task completion in its experiment [58]. | **Useful only as a smartphone/app adjunct**. Basic SMS cannot reliably carry a consistent pictogram experience across handsets. | **C** |

**Case study - Haryana versus Andhra Pradesh:** The Haryana intervention shows that a readable, timely message can change a narrow decision without changing yield [34]. The Andhra trial layered video, IVR and SMS. Of 2,014 final respondents, 93.79% selected at least one IVR and the intervention improved knowledge and several practices, but still produced no significant production or yield effect [10].

The mechanism is clear: delivery enables exposure, while action also depends on credibility, timing, resources, weather evolution and the farmer's ability to execute. KrishiSetu should measure the complete chain - received -> replayed -> correctly understood -> feasible -> acted on -> outcome - rather than report sent-message totals as impact.

### 2.6 Existing Odia agricultural content

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| Meghdoot | Press Information Bureau/IMD description, accessed Aug. 16, 2026, https://pib.gov.in/PressReleasePage.aspx?PRID=1741424 | District-level crop and livestock advisories are issued every Tuesday and Friday in English and local language; the user chooses location and preferred language [62]. | **High as a content reference**, but app delivery and login are not a basic-phone interface or a public machine feed. | **A** |
| Odisha Meghdoot claim | OUAT/KVK Puri advisory PDF, accessed Aug. 16, 2026 | The reviewed Odisha advisory states that advisories are available through Meghdoot in English and Odia [63]. | **Useful confirmation**, but PDF publication is not an API and does not guarantee district-wide archive completeness. | **B** |
| State agro-advisory directory | Odisha Agriculture and Farmers' Empowerment Department, accessed Aug. 16, 2026, https://agri.odisha.gov.in | The state page links to an OUAT "Agro Advisory" resource [39]. | **Medium**. Use as a source registry; licensing, cadence and machine-readable access remain unverified. | **B** |
| Krishi Jagran Odia | Krishi Jagran Odia, accessed Aug. 16, 2026, https://odia.krishijagran.com | Active Odia agricultural publishing source found in search [31]. | **Good for vocabulary and topic discovery**, not an authoritative warning feed. | **C** |
| KVK Odia archive | KVK/OUAT searches, accessed Aug. 16, 2026 | Individual advisories were findable, but no complete, stable, licensed Odia corpus/API was established. | **Partial**. Build a curated source manifest; do not scrape opportunistically in an alert path. | **D** |
| Ama Krushi scripts | Precision Development/Ama Krushi sources, accessed Aug. 16, 2026 | The service demonstrates localized weekly voice advice and expert handling at scale [46]. Public reusable script corpus, ontology and license were not found. | **Strong partnership target**, not currently a downloadable content asset. | **B** |

These sources can seed an approved phrase bank and retrieval library, but none of the reviewed pages proves that KrishiSetu may automatically ingest, modify and redistribute all content. Each source needs authority, date, geography, crop stage, hazard, language, license and reviewer metadata.

### 2.7 Phone-use reality and effectiveness evidence

| item | named source (URL + date) | spec | feasibility | reliability grade A-D |
|---|---|---|---|---|
| Odisha smartphone context | Odisha Economic Survey 2025-26, https://finance.odisha.gov.in/sites/default/files/2025-08/OES%202025-26%20Highlights%20and%20Executive%20Summary%20-English.pdf | Smartphone ownership is reported as 78.1% among mobile users [64]. Around 81% of Odisha's population resides in rural areas [64]. | **Supports dual-channel design**, not app-only delivery. The statistic does not isolate low-literacy farmers or shared phones. | **A** |
| Rural phone use and gender | MoSPI CMS:T 2025 survey, May 29, 2025, https://mospi.gov.in/sites/default/files/publication_reports/CMS_T_Report_2025.pdf | Survey covered 34,950 households, including 19,071 rural households [50]. For rural people age 15+, mobile ownership was 80.7% for males and 48.4% for females; mobile use was 89.5% and 76.3%, respectively [50]. | **High-value inclusion warning**. Enrollment must record shared-device, preferred-time and privacy constraints. | **A** |
| Youth-use limitation | Same MoSPI survey | Rural mobile use among ages 15-29 was 96.8%, but the source is not a farmer study and does not characterize older farmers or phone sharing [50]. | **Do not generalize youth saturation to the target population**. | **A** |
| Odisha voice-channel reality | Ama Krushi operational reporting | Weekly outbound calls plus a 155333 inbound IVR/live-agent/expert path operate across all 30 districts; the project reports substantial inbound traffic and millions of registered users [46]. | **Best local channel precedent**. Seek partnership data on pickup, replay, language and action. | **B** |
| Missed-call behavior | CGNet Swara and Gram Vaani | Both use missed calls followed by server callback, removing user airtime burden [33][42]. | **High** for basic phones and cost sensitivity. | **A/B** |
| WhatsApp voice-note behavior | Searches of India farmer phone-use studies and program pages | No credible target-population study quantified how Odisha's low-literacy farmers use WhatsApp voice notes, who controls the handset, or whether warnings are heard in time. | **Unknown**. Keep WhatsApp optional until measured. | **D** |
| Agriculture-advisory impact | Andhra RCT, Mar. 15, 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10018648/ | Knowledge rose 0.224 SD and average reported practices were 1.0 versus 0.8, but production and yield effects were not significant [10]. | **Evidence for learning, not crop-loss claims**. | **A** |
| Large-program observational signal | Direct2Farm evaluation, Mar. 2019, https://www.sciencedirect.com/science/article/pii/S0308521X18311666 | Across six states, at least 40% of an initial 400,000 registered users became active; credibility was valued, while small, women and elderly farmers were less likely to participate [6]. | **Useful reach warning**, but weaker causal evidence than the RCT. | **B** |

## 3. COVERAGE TABLE

| source families | useful hits | noise/missing | coverage judgment (A-D) |
|---|---|---|---|
| Peer-reviewed/open NLP | IndicTrans2; Odia tokenizer study; IndicVoices | No complete small-model Odia capability matrix; no human disaster-advisory evaluation | **B** |
| First-party cloud speech docs | Google `or-IN` STT and price; Azure `or-IN` STT/custom speech and price | No Google/Azure Odia TTS; no dialect/noisy-IVR accuracy | **A for availability, C for target quality** |
| Government language infrastructure | BHASHINI task/API workflow | No public production tariff, SLA, quota, live Odia task matrix or Odia quality score | **C** |
| Open speech models | IndicF5; IndicVoices; IndicConformer lead | No Odia MOS, telephone-noise benchmark, edge-device latency or hosted production SLA | **B for prototype, C for pilot** |
| India low-literacy IVR research | Avaaj Otalo; CGNet Swara; Medhi et al. | Mostly Gujarati, Hindi-belt or Kannada contexts; no Odia cyclone comprehension | **A for design pattern, C for Odisha effect** |
| Operational voice platforms | Ama Krushi; Gram Vaani | Limited independent outcome, script, drop-off and comprehension data | **B** |
| Agricultural SMS/effect studies | IMD SOP; Haryana field study; Andhra RCT; Direct2Farm | No Odia wording, code-mix, pictogram or optimum-length trial | **B** |
| Official agricultural content | Meghdoot/PIB; Odisha department; OUAT/KVK PDFs | Fragmented pages/PDFs; no verified open API, license or complete Odia archive | **B/C** |
| Phone-use statistics | Odisha Economic Survey; MoSPI CMS:T | Not specific to low-literacy farmers; weak evidence on sharing, older farmers and WhatsApp audio | **B** |
| Commercial/community search results | Marketing TTS pages, generic AI answers, social posts | Entity conflation, no primary measurements, unclear dates and terms | **D** |

Coverage is good enough to choose a prototype architecture and interaction pattern. It is not good enough to state that a particular Odia voice, ASR model or wording will be understood in cyclone conditions. That distinction drives the GO/GATED split below [43][58].

## 4. WHAT IS MISSING

| exact gap | why current evidence is insufficient | blocked decision | minimum evidence needed |
|---|---|---|---|
| District/dialect ASR performance | IndicVoices reports one Odia WER, without coastal, Sambalpuri/western, tribal, code-switch or telephone-noise splits [43]. | Whether ASR may accept spoken confirmation or questions | Representative recordings from intended districts, feature phones and storm/noise conditions; report WER plus intent and critical-entity error rates. |
| Odia TTS intelligibility | IndicF5 has Odia support but no Odia-specific MOS or emergency-term score [59]. | Whether synthetic voice may carry the warning itself | Blind listening study covering place names, crops, dates, wind/rain amounts, dosage/units, negation and urgent actions. |
| BHASHINI production contract | Public docs defer paid production access to contact and disclose no reviewed SLA/tariff [45]. | Budget, capacity, privacy and fallback planning | Written price, quota, region/data retention, uptime/latency support, model versioning and commercial-use terms. |
| Small Odia LLM comparison | No decision-ready small-model-by-task benchmark was found. | Whether any local LLM belongs in the safety path | Fixed benchmark of approved advisories: extraction, translation, contradiction, hallucination, numerical fidelity and unsafe-action rejection. |
| Human translation safety | IndicTrans2 lacks full-scale human evaluation and cautions against relying only on automatic metrics [11]. | Whether generated Odia can be sent without review | Qualified agronomist and native-language review, followed by farmer teach-back testing. |
| Odia warning comprehension | Adjacent low-literacy studies establish interface patterns, not Odisha cyclone task success [58]. | Prompt wording, speaking rate, repetition and menu depth | Scenario test measuring correct paraphrase, selected action, time, replay, abandonment and request for help. |
| Script and code-mix preference | No Odia versus Romanized Odia versus Odia-English trial was found. | SMS and voice lexicon | District-stratified A/B comprehension test, including common English terms only where farmers already use them. |
| Effective SMS length | IMD's 262 characters is a ceiling, not a comprehension optimum [56]. | How much to put in the fallback SMS | Compare one-action, two-action and segmented messages using correct-action recall, not preference alone. |
| Shared-phone and gender effects | National data show a large rural ownership gap, but not Odisha farmer sharing/privacy behavior [50]. | Enrollment, consent, callback time and confidential profile use | Household/device mapping and women-focused interviews in intended pilot blocks. |
| WhatsApp voice-note reality | No credible target study quantified use or timely playback. | Whether WhatsApp deserves core status | Instrumented opt-in trial; measure delivery, playback delay, completion and action. |
| Reusable Odia advisory corpus | Official and media content exists, but complete API, redistribution license and provenance were not established. | Retrieval, fine-tuning and automated reuse | Signed data agreement or internally authored, versioned and expert-approved phrase bank. |
| Disaster outcome attribution | RCT evidence found learning/adoption but not yield effects [10]. | Claim that KrishiSetu minimizes crop loss | Pre-registered pilot with baseline, hazard exposure, action verification and agronomic outcome measurement; delivery analytics alone are insufficient. |

The most dangerous missing data are not another corpus size or model leaderboard. They are critical-word errors: an omitted negation, wrong village, wrong unit, or misunderstood deadline. Those errors must be separately tagged and reviewed even if average WER or BLEU looks acceptable.

## 5. HOW IT FEEDS THE PRODUCT

| product tier / decision | evidence-powered design | what the tier must not do |
|---|---|---|
| **Tier 0 - Authoritative event and farm record** | Keep IMD/hazard facts, location, crop, stage and approved action as structured fields. Attach source time and validity. IMD already distinguishes bulletin highlights and vernacular dissemination [56]. | Do not ask an LLM to invent hazard facts or agronomic actions. |
| **Tier 1 - Controlled Odia rendering** | Use an expert-approved template library. IndicTrans2 may draft new templates or back-translate reviewer changes; 200M distilled models make local deployment plausible [11]. | Do not directly publish free-form model output. Preserve numbers, units, negation and named entities. |
| **Tier 2 - Voice generation** | Record fixed safety phrases with native Odia speakers. Use IndicF5 only for reviewed variable content after intelligibility testing [59]. | Do not claim Google/Azure Odia TTS support; neither reviewed catalog lists it [40][55]. |
| **Tier 3 - Delivery orchestration** | Outbound call first for severe/urgent alerts; missed-call callback for replay; SMS receipt; optional app/WhatsApp copy. Follow Ama Krushi's voice-plus-human pattern and CGNet's low-cost callback [46][33]. | Do not make smartphone installation or data connectivity a prerequisite. |
| **Tier 4 - Comprehension loop** | Prompt pattern: identify trusted sender -> state hazard/time -> give one action -> replay -> "press 1 if understood, 2 to hear again, 3 for help." Low-literacy work favors spoken/numeric interaction and minimal hierarchy [58]. | Do not interpret keypress 1 as proof of understanding without periodic teach-back sampling. |
| **Tier 5 - ASR and question capture** | Use Google/Azure or an open model to transcribe optional questions. Store audio with consent, confidence and model version; route low-confidence or high-risk content to a human [41][28]. | Do not let ASR alone confirm pesticide dose, evacuation, livestock movement or other high-consequence action. |
| **Tier 6 - Monitoring and escalation** | Measure pickup, full-listen, replay, keypress, help request, agent resolution, correct teach-back and action. Live operators sharply reduced error in adjacent low-literacy tasks [58]. | Do not substitute send rate, call duration or registration count for comprehension or impact. |
| **Tier 7 - Offline resilience** | Cache active alerts, templates and human audio at the district/edge node; queue callbacks/SMS; log acknowledgments for later sync. | Do not let BHASHINI/cloud failure suppress the last approved warning. |

**Case study - Ama Krushi as the product bridge:** Ama Krushi proves that Odisha farmers can be reached through scheduled customized calls and can use a common number with IVR, live-agent and expert escalation at statewide scale [46]. KrishiSetu should therefore integrate with, partner with or at minimum emulate that service pattern rather than launch a deep standalone menu.

The new requirement is event urgency. A weekly advisory tolerates a missed call and later callback; a cyclone instruction may not. KrishiSetu should assign each action a deadline and escalation rule: retry the call, send the concise SMS receipt, notify a human queue, and never silently convert failed delivery into "farmer informed."

## 6. REAL-vs-FILLER

| component or claim | classification | evidence-only rationale | product treatment |
|---|---|---|---|
| IndicTrans2 Odia translation | **REAL for drafting** | All 22 scheduled languages, large bitext corpus, distilled 200M models [11]. | Use behind templates and review. |
| "Machine translation is safe enough for automatic emergency advice" | **FILLER** | Authors explicitly identify metric and human-evaluation limits [11]. | Prohibit unreviewed send. |
| Google/Azure Odia ASR | **REAL, bounded** | `or-IN` appears in official STT support documentation [41][28]. | Optional transcription and analytics; benchmark on telephony audio. |
| Commercial cloud Odia TTS | **FILLER today** | No Odia entry in reviewed Google or Azure voice catalogs [40][55]. | Do not put in architecture slides as an available native voice. |
| IndicF5 Odia TTS | **REAL for prototype** | Odia support, 0.4B model and MIT license are documented [59]. | Run locally; pair fixed human audio with validated synthesis. |
| "IndicF5 is human quality in Odia" | **FILLER** | No Odia-specific MOS/intelligibility result was found [59]. | Do not claim until tested. |
| BHASHINI PoC integration | **REAL** | Official Search -> Config -> Compute workflow exists [45]. | Provider adapter and bake-off. |
| BHASHINI free production service | **FILLER** | Public docs direct paid production use to contact [45]. | Obtain written commercial/SLA terms. |
| Shallow IVR and missed-call callback | **REAL** | Avaaj, CGNet and Gram Vaani document use and substantial call activity [17][33][42]. | Core basic-phone interaction. |
| Deep spoken content tree | **DECORATIVE/RISKY** | Avaaj users wanted categories and the system lacked search/filter for growing content [17]. | Keep emergency path shallow; use an agent or post-event library. |
| SMS-only low-literacy delivery | **FILLER** | Adjacent low-literacy electronic tasks had high errors; Haryana literacy and smartphone access were incomplete [58][34]. | SMS is receipt/fallback, not sole channel. |
| Pictograms in ordinary SMS | **DECORATIVE** | Evidence supports a graphical interface with audio, not consistent basic-SMS pictograms [58]. | Optional smartphone card only. |
| Meghdoot/Odia content as reference | **REAL** | Official source describes district, crop/livestock, twice-weekly local-language advisories [62]. | Curate with provenance and expert approval. |
| "A website/PDF is a production API" | **FILLER** | Reviewed Odisha content is linked or published as pages/PDFs, with no established machine-feed contract [63][39]. | Build a licensed ingestion agreement. |
| WhatsApp voice notes as the primary channel | **UNPROVEN** | No target-population usage/comprehension measurement was found. | Optional experiment, never the basic-phone fallback. |
| Registrations/calls equal crop-loss reduction | **FILLER** | Andhra trial improved knowledge/practice but not production or yield [10]. | Measure action and outcome separately. |

The rule is simple: a named model, service or content site is not a capability until its exact Odia task, quality, terms and fallback are verified. The genuinely usable core today is controlled text, recorded voice, shallow IVR, callback, DTMF, human escalation and versioned evidence.

## 7. NOISE LOG

| searched lead | discarded reason | consequence for the report |
|---|---|---|
| MeraVote IVR deployment | Exact-name searches did not produce a credible primary paper with menu, sample or comprehension results. | Not used as a design or outcome claim. |
| Commercial `bhashini.ai` pricing | It is not the Government of India BHASHINI service documented at bhashini.gov.in. | Its tariff is not reported as government API pricing. Official production terms remain unknown [45]. |
| Generic Gemini/LLM Odia claims | Product pages and broad multilingual claims did not provide a small-model Odia task matrix or agronomic safety test. | No small LLM is endorsed for direct advisory generation. |
| Google and Azure generic TTS price pages | Generic character pricing is irrelevant when the official voice list has no Odia voice [40][55]. | TTS cost is marked unavailable rather than falsely priced. |
| Azure Office/DISM language-pack pages | Operating-system UI language support is not Speech ASR/TTS support. | Excluded from the speech inventory. |
| AIKosh Odia Common Voice/FLEURS shells | Reviewed pages exposed dynamic shells without decision-grade hours, speakers, license or benchmark values [36][37]. | IndicVoices is used as the quantified corpus instead. |
| Social posts, Facebook, Reddit and Wikipedia | No stable primary measurements or service terms. | Excluded from evidence tables. |
| Vendor "human-like" voice marketing | No Odia-specific MOS, word-error or warning-intelligibility study. | Treated as a provider claim, not quality evidence [59]. |
| Krishi Jagran articles as official advice | Useful Odia vocabulary and topics, but no authority for emergency instructions [31]. | Reference only; not an alert trigger. |
| WhatsApp voice-note anecdotes | No representative Odisha low-literacy farmer measurement of playback, sharing or timely action. | Channel remains optional and experimental. |
| SMS pictogram search | Evidence concerned graphical/audio interfaces, not robust display in ordinary SMS. | Pictograms are excluded from the feature-phone core [58]. |
| Registration and call-count publicity | Reach figures do not independently establish comprehension or crop outcomes. | Operational scale and impact are reported separately [10]. |

This log prevents attractive but non-equivalent facts from entering the architecture: UI language packs are not speech APIs; generic TTS prices are not Odia availability; and reach is not comprehension.

## 8. VERDICT: GO / PARTIAL / GATED

### Prototype: **GO**

Build a bounded demonstrator now. Its safety path should be: structured IMD/hyperlocal record -> rule-selected approved action -> reviewed Odia template -> human-recorded fixed prompt plus validated variable speech -> outbound call -> replay/DTMF/help -> concise SMS receipt -> audit log. IndicTrans2 can assist template creation, IndicF5 can demonstrate local synthesis, and Google or Azure can transcribe optional questions, but none should independently author or authorize the action [11][59][41][28].

The IVR should expose no more than the immediate job: hear the active warning, replay it, confirm or request help. Use numeric keys, avoid scrolling concepts and deep hierarchies, identify the trusted agricultural/weather authority, and support a cost-free callback pattern [58][33]. Cache the last approved warning and audio at the edge so cloud or BHASHINI failure does not silence the service.

### Supervised usability trial: **PARTIAL**

A small, supervised study is justified to compare recorded and synthesized Odia; message lengths; local vocabulary; speech rate; replay behavior; DTMF versus optional speech; and one-action versus multi-action prompts. It must include intended districts, women, older farmers, shared-phone users, basic phones, noisy telephone audio and low-connectivity conditions. The output is a validated phrase and interaction library, not a crop-loss claim.

### Operational pilot: **GATED**

Do not launch unsupervised cyclone/flood advice until all of the following exist:

1. Native agronomist approval and farmer teach-back for every safety-critical template.
2. Dialect/noise ASR testing with separate critical-number, unit, negation, place-name and intent errors.
3. Odia TTS listening tests, with recorded-human fallback for any phrase that fails.
4. Written BHASHINI/cloud production price, quota, privacy, retention, region, model-version and SLA terms.
5. Consent, opt-out, retry, shared-phone, quiet-time and human-escalation procedures.
6. Monitoring that distinguishes delivered, heard, understood, feasible, acted and resolved.
7. A pre-specified evaluation of time-to-action and agronomic outcomes; message counts are not impact.

The gating standard follows the evidence: voice interfaces can dramatically improve task completion, yet multimodal advisories have improved knowledge without improving yield [58][10]. KrishiSetu can credibly promise a testable communication and decision-support system now. It cannot yet credibly promise autonomous Odia understanding, commercial BHASHINI readiness or measured crop-loss reduction.

## Synthesis

| strategy | mechanism | scope and evidence base | main trade-off | decision horizon |
|---|---|---|---|---|
| **Controlled IndicTrans2 templates** | Translate/rewrite approved structures | Strong multilingual technical evidence; weak direct farmer comprehension evidence [11] | Less expressive, much more auditable | Use now for prototype |
| **Google/Azure ASR** | Cloud speech recognition | Official `or-IN` availability and public price; no Odisha dialect/noisy-IVR benchmark [41][28] | Fast integration versus connectivity, privacy and error risk | Optional prototype; gated control path |
| **BHASHINI pipeline** | Government model discovery/config/compute | Official PoC workflow; undisclosed production economics/SLA [45] | India-language ecosystem fit versus procurement uncertainty | Adapter now; contract before pilot |
| **IndicF5 plus human recordings** | Local synthesis with recorded fixed prompts | Real open Odia support; no Odia MOS [59] | Offline control versus validation and compute burden | Best prototype TTS route |
| **Shallow callback IVR** | Missed call, one action, replay, DTMF, human help | Repeated Indian deployment evidence and local Ama Krushi precedent [33][46] | High accessibility but slower than app automation and incurs telephony/agent cost | Core prototype and pilot channel |
| **SMS receipt** | Persistent short text confirming action | Official IMD operational pattern; incomplete literacy and no Odia optimum [56][34] | Cheap and persistent, but weak proof of understanding | Always secondary |
| **App/WhatsApp visual/audio adjunct** | Rich media and asynchronous replay | Graphical/audio interfaces can aid low-literacy use, but target WhatsApp behavior is unmeasured [58] | Richer comprehension versus smartphone/data/shared-device exclusion | Optional experiment |
| **Free-form Odia AI agent** | Generate and converse without bounded scripts | No adequate small-model Odia safety matrix, dialect benchmark or outcome evidence | Flexible demonstration versus unacceptable silent error | Exclude from safety path |

Three tensions matter. First, the most scalable component - automation - is the least validated at the point of human comprehension. Second, the most accessible component - voice - still depends on telephony cost, trusted speakers and human escalation. Third, the richest channel - app or WhatsApp - is not the one guaranteed by the problem statement and may amplify gender, ownership and shared-device exclusions visible in rural phone statistics [50].

The best architecture is therefore deliberately asymmetric. Machines are strong at ingesting alerts, matching profiles, selecting approved rules, scheduling calls and logging outcomes. Humans remain responsible for the action library, Odia phrasing, uncertain questions and safety escalation. That is not a temporary workaround; it is the evidence-aligned design until Odisha-specific comprehension and outcome data justify moving a component across the boundary.

## References

1. *IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages - ACL Anthology*. https://aclanthology.org/2024.acl-long.595
2. *Meghdoot - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en_US&id=com.aas.meghdoot
3. *IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages*. https://arxiv.org/abs/2404.16816
4. *Meghdoot - Apps on Google Play*. https://play.google.com/store/apps/details?hl=en-US&id=com.aas.meghdoot
5. *Meghdoot weather-based mobile application*. https://pressroom.icrisat.org/meghdoot-weather-based-mobile-application
6. *Effectiveness of mobile agri-advisory service extension model: Evidence from Direct2Farm program in India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2452292917300711
7. *Bhashini*. https://bhashini.gov.in/api-documentation
8. *Azure Speech in Foundry Tools | Microsoft Azure*. https://azure.microsoft.com/en-us/products/ai-foundry/tools/speech
9. *Tokenization Matters: Improving Zero-Shot NER for Indic Languages*. https://arxiv.org/html/2504.16977
10. *Digital tools for rural agriculture extension: Impacts of mobile‐based advisories on agricultural practices in Southern India - Singh - 2023 - Journal of the Agricultural and Applied Economics Association - Wiley Online Library*. https://onlinelibrary.wiley.com/doi/full/10.1002/jaa2.42
11. *IndicTrans2: Towards High-Quality and Accessible Machine Translation Models for all 22 Scheduled Indian Languages | OpenReview*. https://openreview.net/forum?id=vfT4YuzAYA
12. *Bhashini*. https://bhashini.gov.in/ulca
13. *Do phone-based short message services improve the uptake of agri-met advice by farmers? A case study in Haryana, India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212096321000504
14. *Developing voice-based information sharing services to bridge the information divide in marginalized communities: A study of farmers using IBM’s spoken web in rural India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0268401220314821
15. *CGNet Swara | The Communication Initiative*. https://global.comminit.com/content/cgnet-swara
16. *Avaaj Otalo — A Field Study of an Interactive Voice Forum for Small Farmers in Rural India*. https://tap2k.org/papers/pap0310-patel.pdf
17. *dl.acm.org*. https://dl.acm.org/doi/pdf/10.1145/1753326.1753434
18. *Text to speech overview - Speech service - Foundry Tools | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech
19. *Pricing - Azure Speech in Foundry Tools | Microsoft Azure*. https://azure.microsoft.com/en-us/pricing/details/speech
20. *Bhashini*. https://bhashini.gov.in/
21. *Speech-to-Text API Pricing | Google Cloud*. https://cloud.google.com/speech-to-text/pricing
22. *AI4Bharat speech and TTS models on Hugging Face | IndiaAIPulse*. https://www.indiaaipulse.com/en/news/ai4bharat-expands-speech-model-lineup-on-hugging-face
23. *Language versions and language interface packs in Office 2016 - Office | Microsoft Learn*. https://learn.microsoft.com/en-us/office/2016/language/language-versions-language-interface-packs
24. *ai4bharat (AI4Bharat)*. https://huggingface.co/ai4bharat/models
25. *DISM Languages and International Servicing Command-Line Options | Microsoft Learn*. https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism-languages-and-international-servicing-command-line-options?view=windows-11
26. *IndicConformer - a ai4bharat Collection*. https://huggingface.co/collections/ai4bharat/indicconformer
27. *ai4bharat/IndicConformer · Hugging Face*. https://huggingface.co/ai4bharat/IndicConformer
28. *Language and Voice Support for Azure Speech - Foundry Tools | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=sv-SE
29. *Language and Voice Support for Azure Speech - Foundry Tools | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt
30. *Language and Voice Support for Azure Speech - Foundry Tools | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support
31. *Krishi Jagran Odia - Agriculture News in Odisha, Odia news, Bhubaneswar agriculture news, news from Odisha, news from cuttack*. https://odia.krishijagran.com/
32. *PowerPoint Presentation*. https://billthies.net/assets/pdf/swara-ictd12.pdf
33. *Ictd12 Swara*. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ictd12-swara.pdf
34. *(PDF) Do Phone-based Short Message Services Improve the Uptake of Agri-met Advice by Farmers? A Case Study in Haryana, India*. https://www.researchgate.net/publication/351581969_Do_Phone-based_Short_Message_Services_Improve_the_Uptake_of_Agri-met_Advice_by_Farmers_A_Case_Study_in_Haryana_India
35. *echasa.odisha.gov.in*. https://echasa.odisha.gov.in/
36. *AIKosh*. https://aikosh.indiaai.gov.in/home/datasets/details/odia_asr_benchmark_dataset_for_speech_recognition_fluers_odia.html
37. *AIKosh*. https://aikosh.indiaai.gov.in/home/datasets/details/odia_asr_benchmark_dataset_commonvoice_odia.html
38. *IndicVoices: Towards building an Inclusive Multilingual Speech Dataset for Indian Languages*. https://arxiv.org/abs/2403.01926
39. *Web Directory | Department of Agriculture & Farmers' Empowerment*. https://agri.odisha.gov.in/about-us/webs-directory
40. *Supported voices and languages  |  Cloud Text-to-Speech  |  Google Cloud Documentation*. https://cloud.google.com/text-to-speech/docs/list-voices-and-types
41. *Cloud Speech-to-Text V2 supported languages  |  Google Cloud Documentation*. https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
42. *A social media platform for the rural masses – gramvaani.org*. https://gramvaani.org/a-social-media-platform-for-the-rural-masses/
43. *IndicVoices: Towards building an Inclusive Multilingual Speech Dataset for Indian Languages*. https://arxiv.org/html/2403.01926v1
44. *gramvaani.org*. http://gramvaani.org/
45. *Overall Understanding of the API Calls | Bhashini APIs*. https://bhashini.gitbook.io/bhashini-apis
46. *Ama Krushi – Scaling advisory services to millions of farmers in Odisha, India – Precision Development (PxD)*. https://precisiondev.org/project/ama-krushi
47. *Adoption of mobile-based agricultural extension services: evidence from South India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S074301672500292X
48. *Various uses of Gram Vaani’s vSurvey technology – gramvaani.org*. https://gramvaani.org/various-uses-of-gram-vaanis-vsurvey-technology/
49. *Ama Krushi Transition Insights Report*. https://precisiondev.org/wp-content/uploads/2025/04/AK-Transition-Insights-2025_condensed.pdf
50. *GOVERNMENT OF INDIA MINISTRY OF STATISTICS AND PROGRAMME IMPLEMENTATION ज्येष्ठ शक संवत 8 1947 29 May, 2025 PRESS NOTE Results*. https://www.mospi.gov.in/sites/default/files/press_release/Final_press%20release_CMS_T.pdf
51. *Ama Krushi Transition Insights Report*. https://precisiondev.org/wp-content/uploads/2025/02/AK-transition-report-BMGF_condensed.pdf
52. *Review pricing for Text-to-Speech | Google Cloud*. https://cloud.google.com/text-to-speech/pricing
53. *CHI Conference - Proceedings*. https://dl.acm.org/conference/chi/proceedings
54. *Papers – CHI 2025*. https://chi2025.acm.org/for-authors/papers
55. *What are neural text to speech HD voices? - Foundry Tools | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/high-definition-voices
56. *Gkms Sop*. https://mausam.imd.gov.in/imd_latest/contents/pdf/gkms_sop.pdf
57. *Designing mobile interfaces for novice and low-literacy users | ACM Transactions on Computer-Human Interaction*. https://dl.acm.org/doi/10.1145/1959022.1959024
58. *(PDF) Designing Mobile Interfaces for Novice and Low-Literacy Users*. https://www.researchgate.net/publication/234829313_Designing_Mobile_Interfaces_for_Novice_and_Low-Literacy_Users
59. *ai4bharat/IndicF5 · Hugging Face*. https://huggingface.co/ai4bharat/IndicF5
60. *ai4bharat (AI4Bharat)*. http://huggingface.co/ai4bharat
61. *AI4Bharat Models*. https://models.ai4bharat.org/
62. *‘Meghdoot’ – Mobile app for weather based agro advisories*. https://pib.gov.in/PressReleaseIframePage.aspx?PRID=1739245
63. *Gramin Krishi Mausam Sewa India Meteorological Department*. https://ouat.ac.in/wp-content/uploads/2023/12/Puri_IAAS_English_29.12.2023_52_104.pdf
64. *http://finance.odisha.gov.in/sites/default/files/2025-08/OES%202025-26%20Highlights%20and%20Executive%20Summary%20-English.pdf*. http://finance.odisha.gov.in/sites/default/files/2025-08/OES%202025-26%20Highlights%20and%20Executive%20Summary%20-English.pdf
