# Global Prior Art for Safe Cyclone-Ready Farm AI

## 1. EXECUTIVE SUMMARY

- **Closest Odisha Analogue**: Ama Krushi, renamed Krushi Samruddhi Helpline in August 2024, already combines farmer profiles, outbound customized voice calls, inbound IVR, live agents, and expert agronomists across all 30 Odisha districts. Its source reports service to nearly **7.9M farmers**, a **10% reduction in severe crop-loss probability**, a **9% harvest increase in excess-rainfall areas**, and a **21% reduction in severe crop-loss probability under inadequate rainfall** [19]. -> KrishiSetu should integrate with or extend this channel rather than claim that profile-based IVR advisory is new.

- **Closest International Hazard Stack**: Bangladesh's BAMIS joins meteorological, water, crop, and historical farm data to produce agrometeorological decision support for a country exposed to floods, droughts, and tropical cyclones; its public site includes flood and cyclone risk products, while the program literature describes dissemination and feedback mechanisms [25][29]. -> The defensible novelty is not "weather plus agriculture," but automated, profile-specific pre- and post-disaster action generation with safety controls.

- **Farmer.Chat Proves RAG Scale, Not Perfect Reliability**: The 2024 paper reported deployments in India, Kenya, Ethiopia, and Nigeria, over **15,000 users** and **300,000 queries**; the current product site claims over **830,000 users** and **5M queries** across five countries [28][36]. In the published evaluation, average context precision was **71%**, nearly **80%** of answers had high faithfulness, and **18%** had low relevance [28]. -> Use constrained retrieval and abstention, not an unrestricted LLM, for time-critical disaster advice.

- **Offline AI Exists, But The Full Offline LLM Claim Does Not**: PlantVillage Nuru performs offline smartphone disease recognition and achieved **74-88%** symptom-recognition accuracy with six leaves [39][2]. AgroMetLLM runs quantized models on a Raspberry Pi 4B and produces irrigation advisories in **1-2 seconds**, but reports no field deployment, Odia support, SMS/IVR, hazard triggers, or post-disaster workflow [35]. -> KrishiSetu may credibly claim a new integration, but not that offline agricultural AI itself is new.

- **Voice Is The Proven Inclusion Mechanism**: Ethiopia's 8028 hotline explicitly uses IVR because of low literacy and limited smartphone penetration [14]; India's mKisan distributes text and voice advisories without requiring internet [40]; Ama Krushi shows that a two-way voice service can operate at state scale [19]. -> Treat IVR as a primary product, not a fallback added after the smartphone app.

- **Safety Evidence Is Incomplete And The Downside Is Real**: AgroBench's best tested vision-language model scored **79.26%** overall; lack of knowledge caused **51.92%** of analyzed errors, although the benchmark does not test real-world chemical safety [30]. A syndicated China report alleges that AI pesticide advice destroyed nearly **25 acres** of sesame, but the model is unidentified and an OECD incident record inconsistently says **150 acres** [38][37]. -> Chemical, veterinary, and flood-recovery recommendations need deterministic dose checks, source citations, and human escalation.

- **Odisha Already Owns The Authoritative Content And Data Components**: IMD exposes forecast APIs, while Odisha's 2025 contingency plan separately covers cyclones, floods, pest attack, climate stress, and crop-weather monitoring [33][41]. -> The product opportunity is to compile these authoritative components into a versioned, executable decision system.

- **Defensible White Space**: This sweep found no publicly documented, deployed system combining all of: authoritative cyclone/flood triggers, a farm-level profile, validated pre-event and post-event crop actions, Odia SMS and IVR, intermittent-connectivity operation, and a locally running small LLM. -> Claim the **validated closed-loop integration**, not "the first AI farmer assistant" or "the first weather advisory platform."

## 2. WORLDWIDE INVENTORY

### Direct and near-direct matches

| Name | Country or region | What it does | Named source, URL and date | Status | Scale | Safety record | What KrishiSetu can learn |
|---|---|---|---|---|---|---|---|
| **Ama Krushi / Krushi Samruddhi Helpline** | Odisha, India | Profile-based weekly outbound calls; inbound IVR, live agents, and agronomist answers; weather, crop, livestock, and fisheries advice [19] | Precision Development, https://precisiondev.org/project/ama-krushi, current page; renamed Aug. 2024 [19] | **Live, government-operated** | Nearly **7.9M farmers**; all 30 districts [19] | Expert agronomists answer questions; pesticide advice is broadcast as fixed content, not disclosed as LLM generation [19] | Closest delivery and personalization precedent. Add disaster triggers and post-event workflows rather than duplicate the helpline. |
| **BAMIS** | Bangladesh | Integrates weather, water, crop, yield, and upazila data for climate-risk advisories; portal exposes flood and cyclone risk products [25][29] | Bangladesh DAE/BMD/BWDB, https://www.bamis.gov.bd/en and /page/introduction; project approved 2017 [29] | **Live service; development phases completed** | Databases planned for **487 upazilas** [29] | Meteorologist-agriculturist collaboration and user feedback are described; no LLM safety evaluation [29] | Closest international architecture. Public evidence does not show farm-level generative pre/post recovery plans. |
| **iSAT** | ICRISAT programs, Africa and Asia | AI-based, location-specific, weather-informed advice tailored to crop stage and local conditions [9] | ICRISAT, https://issca.icrisat.org/index.php/scalable-solutions/intelligent-agricultural-systems-advisory-tool-isat, undated | **Operational/pilot platform** | Public page does not state scale | No published safety record on the product page | Weather plus crop-stage personalization is established prior art; channel and disaster-recovery integration remain differentiators. |
| **Meghdoot** | India | Aggregates district- and crop-wise Agro Met Field Unit advisories with forecasts and historical weather every Tuesday and Friday [6] | IMD/IITM/ICAR app listing, https://apps.apple.com/us/app/meghdoot/id1474048155, current listing | **Live app** | Not stated in reviewed source | Human institutional advisories; no generative safety disclosure | Strong authoritative feed, but scheduled app delivery is different from farm-specific emergency IVR. |
| **mKisan** | India | Government push/pull SMS, IVR, USSD, and text/voice advisory access without internet [40][4] | Government of India, https://mkisan.gov.in, current portal | **Live infrastructure** | Portal describes reach to nearly **9 crore farm families** for mobile messaging [4] | Sender organizations remain accountable; no generative model | Reuse as a dissemination pattern or integration point; it is not automated hazard-to-action reasoning. |
| **Kisan Sarathi** | India | Timely, authentic, multilingual advice plus schemes, weather updates, and expert access [42] | Government of India PIB, https://pib.gov.in/PressReleasePage.aspx?PRID=2278757 | **Live public platform** | Not stated in reviewed source | Authenticity and expert access are explicit; no LLM evaluation | Expert escalation and government provenance should be copied. |
| **Odisha Crop Contingency Plan + IMD APIs** | Odisha, India | Official cyclone, flood, pest, climate-stress, and monitoring playbooks combined with forecast APIs [41][33] | Odisha DAFE 2025 plan, https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf; IMD API reference | **Live authoritative components, not one system** | Statewide content | High-authority source material, but machine-readable validation and recommendation auditing are not shown | This should be KrishiSetu's approved rule and retrieval corpus. |
| **WFP Anticipatory Action** | Global | Uses early-warning systems and anticipatory action for droughts, floods, and cyclones [8] | World Food Programme, https://www.wfp.org/anticipatory-actions, current page | **Operational programs** | Multi-country; no comparable farmer-query count on reviewed page | Institutional trigger and action planning, not free-form LLM advice | Copy the trigger-before-impact philosophy; add crop and farm specificity. |
| **Ignitia** | Tropical regions | Delivers rainfall forecasts by SMS; an app supplies richer weather-risk content [17] | UNDP Digital X, https://digitalx.undp.org/catalogs/ignitia.html, current catalog | **Live commercial service** | Not stated in reviewed source | Forecast product, not disclosed as generative crop advice | Hyperlocal forecast-to-feature-phone delivery is prior art; recovery prescriptions are not. |
| **8028 Farmer Hotline** | Ethiopia | Toll-free agronomic and livestock advice through IVR, explicitly designed for low literacy and low smartphone penetration [14] | Ethiopian Agricultural Transformation Institute, http://ati.gov.et/8028-farmer-hotline, current page | **Operational** | Scale not stated on the reviewed hotline page | Curated hotline content; no LLM safety results | Voice inclusion works at national level; personalize hazard actions without removing human escalation. |
| **Farmerline / Mergdata** | Ghana and Africa | Sends agricultural information in mass voice-SMS format [43] | Farmerline case profile, https://nelisglobal.org/4revs/farmerline-empowering-farmers-via-mobile-technology, undated | **Live company/platform** | Not verified in reviewed source | No public generative-advice evaluation found | Local-language voice distribution is real, but not evidence of automated disaster recovery. |
| **Krishify Farmer Advisory Management** | India | Lets organizations map advice to crop stage and geography, add soil/weather/satellite data, and deliver by app, text, or voice [44] | Krishify, https://krishify.com/product/farmer-advisory-management/, current product page | **Commercial product** | Not disclosed | Curated advisory journeys; no independent outcome or LLM safety evidence | A direct workflow-builder analogue. KrishiSetu needs stronger disaster evidence and public evaluation. |

**Direct-match takeaway:** The individual links in the chain already exist. Ama Krushi proves profiles plus IVR at Odisha scale; BAMIS and WFP prove hazard-informed action; iSAT and Krishify prove weather-conditioned crop advice. No reviewed direct match documents the entire pre-disaster and post-disaster closed loop with offline Odia generation.

### Indirect but technically important systems

| Name | Country or region | What it does | Named source, URL and date | Status | Scale | Safety record | Lesson |
|---|---|---|---|---|---|---|---|
| **Farmer.Chat** | India, Kenya, Ethiopia, Nigeria, Brazil | Multilingual, multimodal RAG over vetted agronomy; retrieves by crop, location, and weather [28] | Digital Green paper, https://arxiv.org/html/2409.08916v1, Sept. 13, 2024 [28] | **Live and scaled** | Current site claims **830,000+ users, 5M+ queries** [36] | Approved-document restrictions produced no detected toxic output, but published relevance and faithfulness tails remain [28] | Best RAG analogue. Add hard action constraints and disaster-specific evaluation. |
| **PlantVillage Nuru** | Africa | Offline smartphone CNN/object detector diagnoses crop disease and then gives management advice [2] | CGIAR/IITA study, https://biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf, 2020 | **Deployed public-good app** | Described as widely used across Africa; no audited count in reviewed source | **74-88%** six-leaf accuracy, comparable to experts, but scope is visual diagnosis [2] | Proves offline field AI. It is not an LLM, weather trigger, or disaster recovery engine. |
| **AgroMetLLM** | India, research | Raspberry Pi 4B system combines five evapotranspiration models with quantized Qwen/Ollama to generate irrigation advice [35] | Journal of Agrometeorology, Sept. 1, 2025 [35] | **Research prototype** | No field deployment reported | Statistical model comparisons are reported, but no harmful-advice, language, or agronomist evaluation [35] | Most important edge-LLM prior art. KrishiSetu remains distinct on hazards, Odia, IVR, and field validation. |
| **FarmBeats** | United States / research | Edge gateway aggregates sensors, cameras, and drones, computes locally, and survives network outages [5] | Microsoft Research, https://microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf, 2017 | **Research architecture; Azure service retired** | No comparable farmer scale | Engineering resilience, not advisory safety | Copy gateway continuity; do not describe it as an LLM advisory service. |
| **FarmVibes.AI** | Global developer tool | Open-source geospatial ML workflows for satellite, weather, and sustainability insights [12] | Microsoft GitHub, https://github.com/microsoft/farmvibes-ai, created Sept. 6, 2022 [12] | **Active open-source repository** | **868 stars, 181 forks** when reviewed [12] | No farmer-advice safety layer | Valuable upstream feature engineering, not SMS/IVR or disaster recommendations. |
| **ExtensionBot** | United States | Research-grounded AI for Cooperative Extension, serving public and extension agents [22] | Extension Foundation, https://extension.org/extensionbot, developed since 2019 | **Live institutional AI** | Source reports over 60,000 conversations from May 2024-April 2025 [22] | Emphasizes trusted extension sources; no disaster safety benchmark found | A governance analogue for institution-owned knowledge and escalation. |
| **FBN Norm** | United States | ChatGPT-based agronomy assistant trained on FBN agronomy content [21] | Farmers Business Network, https://www.fbn.com/community/blog/norm-first-ai-ag-advisor, Apr. 15, 2023 [21] | **Commercial assistant** | Not publicly disclosed | Product page says answers should not replace professional agronomic advice; no public benchmark | Generic agronomy chat is crowded. Source citation and action validation matter more than branding. |
| **Bayer expert GenAI** | Global / pilot | Agronomy expert system trained on proprietary data and validated by Bayer agronomists [24] | Bayer, https://www.bayer.com/media/en-us/bayer-pilots-unique-generative-ai-tool-for-agriculture, Mar. 14, 2024 | **Pilot/integration program** | No public farmer scale | Agronomist validation is claimed; independent error rates are absent | Human validation is good prior art; proprietary cloud tooling does not solve Odisha feature-phone resilience. |
| **Cropwise AI** | Global | Combines satellite and sensor data for planting, pest, and crop decisions | Syngenta Cropwise, https://www.cropwise.com/innovations/cropwise_ai, current page | **Commercial platform** | Not disclosed on reviewed page | No public generative safety benchmark | Precision decision support is established, but not low-connectivity disaster voice service. |
| **FieldView and xarvio FIELD MANAGER** | Global | Field-level digital agronomy, historic/current weather, weather-station integration, crop-health and disease-risk tools [45][46][47] | Bayer, https://www.cropscience.bayer.us/tools/fieldview and https://www.xarvio.com, current pages | **Live commercial platforms** | Global claims, no comparable reviewed count | No LLM or disaster-recovery safety results | Useful comparison, but "AI" should not be conflated with conversational or offline generation. |
| **Fasal** | India | IoT-based precision-agriculture platform using real-time farm microclimate sensors [48] | FAO STI Portal, https://sti-portal.fao.org/innovations/fasal, current page | **Live commercial platform** | Not stated in reviewed source | Sensor-driven recommendations; no disaster LLM evaluation | A strong hyperlocal-data input partner or architecture, not a complete analogue. |
| **Plantix API** | Global | Visual crop-health intelligence covering **69 crops and 19 languages** [49] | Plantix, https://plantix.net/en/plantix-intelligence/api-toolkit, current page | **Live API/product** | Product coverage, not user count | No disaster or chemical-dose record reviewed | Use as optional diagnosis evidence, never as a cyclone action engine. |
| **AgroStar and Gramophone** | India | Advisory plus farm inputs and broader agricultural services; Gramophone supports Hindi, English, and Marathi [50][51] | https://corporate.agrostar.in and Google Play Gramophone listing, current pages | **Live companies/apps** | Not verified here | Commercial advice may create input-sales conflicts; no public LLM safety benchmark found | Separate advice quality from product sales and disclose conflicts. |
| **KissanAI / Dhenu** | India | Markets multilingual voice, vision, and agricultural engagement capabilities [52][7] | https://dhenu.ai and Microsoft case page, current | **Product/marketing stage** | No verified scale in reviewed sources | No public evaluation or offline disclosure | Treat as a competitor signal, not evidence of proven disaster advice. |
| **Odia AgriBot GitHub prototype** | India | Gemini API plus Web Speech API; claims Hindi, Tamil, Odia, and other voice interactions [13] | https://github.com/REETIKAJENA025/AGRICULTURAL-BOT, current repository | **Prototype** | No deployment evidence | No agronomy evaluation, guardrails, or incident record | Odia voice demos exist; production reliability is still open. |

### Ideas-only, research assets, and prototypes

| Name | Country or region | What it is | Source and date | Status / scale | Safety and lesson |
|---|---|---|---|---|---|
| **AgriLLM** | CGIAR / Global South | Proposed agriculture-tailored LLM advisory platform with AI71 [11] | CGIAR, https://www.cgiar.org/news-events/news/agrillm-how-cgiar-is-developing-an-ai-powered-agricultural-advisory-service-for-global-south | **Development initiated; no reviewed scale** | Important direction, but no public language, safety, or deployment metrics in the reviewed source. |
| **CropGPT project** | Global research | A 2023 call for a coordinated crop foundation model; a separate May 2026 paper presents a multimodal pest/disease diagnostic model [3][34] | Molecular Plant 2023 proposal; ScienceDirect, May 2026 | **Proposal plus research model** | Not a deployed farmer disaster assistant; do not merge the proposal and later diagnostic paper into one product. |
| **AgriBERT** | Research | BERT-era language model for semantic matching between food descriptions and nutrition data [53] | IJCAI 2022, https://www.ijcai.org/proceedings/2022/715 | **Published model** | It is neither generative crop advice nor a farmer-facing LLM; useful mainly as historical agricultural NLP prior art. |
| **Agricultural QA/BERT dataset work** | Research | BERT and knowledge-graph agricultural question answering [54][55] | IEEE paper, 2025 | **Research** | Evaluation is task-specific; no cyclone, voice, field-scale, or harmful-dose assessment. |
| **AgroBench** | Japan / international research | **4,342** expert-annotated QA pairs over seven agricultural vision-language tasks [30] | ICCV 2025 paper, https://openaccess.thecvf.com/content/ICCV2025/papers/Shinoda_AgroBench_Vision-Language_Model_Benchmark_in_Agriculture_ICCV_2025_paper.pdf | **Benchmark** | Strong correctness benchmark, but not a longitudinal advisory-safety benchmark [30]. |
| **AI AgriBench Smallholders** | Global | Leaderboard based on real questions from farmer-facing services in India, Africa, and other smallholder regions [27] | https://aiagribench.org/smallholders, current | **Benchmark scaffold** | Scores accuracy, relevance, completeness, and conciseness; reviewed page did not expose loaded results or disaster-safety scoring. |
| **AgriGPT ecosystem** | Research | Modular agricultural LLM ecosystem covering data construction, retrieval, and evaluation [56] | arXiv, 2025 | **Preprint/research** | Architecture idea, not field deployment. |
| **AgriVoice** | India | Multilingual voice/text farming-assistant concept [57] | JETIR, 2025 | **Paper/prototype** | No robust field, safety, or scale evidence found. |
| **A2SV Crop-Intel-AI repository** | Africa-oriented hackathon | Prototype combines weather prediction with planting, irrigation, and harvest planning [32] | https://github.com/Crop-Intel-Ai/A2SV-Hackathon, current repository | **Hackathon prototype; no scale** | No verified SMS/IVR, cyclone recovery, evaluation, or safety layer. |
| **SHELTER** | Africa | Landing page proposes satellite and AI flood/crop/health warnings over existing channels [58] | https://shelter.zerorate.io, current page | **Idea/early product claim** | Attractive direct wording, but no reviewed deployment, outcome, or safety evidence. |
| **Edge-enabled agentic agriculture framework** | Research | Proposes edge-deployable deep learning, agentic AI, and IoT for field decisions [59] | ScienceDirect research article, 2025 | **Research framework** | Shows conceptual overlap, not a low-resource-language disaster deployment. |
| **KisanGPT/KissanGPT web demos** | India | Multiple unrelated sites claim multilingual or AI farming assistance [60][61][62] | kisangpt.online, kisangpt.com, Streamlit, current | **Unverified demos** | One site explicitly says chemical advice is indicative and should be confirmed locally [63]; names and provenance are fragmented. |
| **KisanVaani assets** | India | English agricultural QA dataset and separate voice-assistant repositories use the same name [64][65][66] | Hugging Face/GitHub/dev.to, current | **Dataset and prototypes** | Naming collision; no verified common production platform or Odia disaster benchmark. |

## 3. COVERAGE TABLE

The grades below describe this sweep's ability to support an honest differentiation claim, not the overall quality of each source family. "Useful hits" counts retained, materially relevant artifacts rather than every search result.

| Source family | Useful hits retained | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| Government and official public platforms | 10 | Strong on functions and policy; weak on model internals, uptime, and outcome evaluation | **A** |
| Peer-reviewed papers and major preprints | 12 | Strong technical detail; many lab prototypes lack deployment, language, and safety evidence | **A-** |
| IGO, CGIAR, and development-organization sources | 9 | Strong smallholder relevance; several pages describe programs without comparable metrics | **A-** |
| Corporate product and press pages | 11 | Good for existence and launch status; marketing claims, limited error rates, limited independent scale | **B** |
| GitHub and Hugging Face | 7 | Verifiable code or data existence; deployment, maintenance, safety, and real users often absent | **B-** |
| App stores and product catalogs | 5 | Useful channel/language snapshots; dates, scale, and evaluation are usually missing | **C+** |
| News and incident databases | 3 | Found the only concrete alleged pesticide-loss case, but source chains and units conflict | **C** |
| Forums, hackathons, blogs, and idea pages | 8 | High prototype and naming noise; almost no audited outcomes | **D** |
| Failed-startup and shutdown search | 1 verified retirement | No well-documented failed startup matched the full problem; many generic "agtech failure" essays were discarded | **D** |

**Coverage judgment:** The sweep is strong enough to reject broad novelty claims and identify the closest analogues. It is not a patentability opinion, a complete private-product census, or proof that no unpublished pilot exists.

## 4. WHAT IS MISSING

### The missing product is the closed loop, not another chatbot

No reviewed deployment publicly documents all seven steps in one system:

1. Ingest an authoritative IMD cyclone, flood, rainfall, or district warning.
2. Resolve the affected farmer's village, field, crop, variety, stage, soil, drainage, livestock, stored inputs, and communication preference.
3. Select a versioned, expert-approved pre-event action plan.
4. Recompute advice as the warning, landfall, inundation, or river forecast changes.
5. Collect post-event observations through IVR, SMS, an agent, or a photo when available.
6. Generate a crop-stage-specific recovery sequence with explicit contraindications.
7. Deliver, confirm receipt, record action, and escalate high-risk cases.

The data and content pieces are available: IMD supplies forecast APIs [33], Odisha has official cyclone and flood contingency material [41], and Ama Krushi already stores customized advice against farmer profiles and exposes it through IVR [19]. What is missing is a governed orchestration layer that turns those pieces into event-specific, auditable tasks.

### The offline gap is narrower than "no edge LLM"

Nuru proves offline agricultural inference [39], FarmBeats proves local operation through network outages [5], and AgroMetLLM proves a quantized local language model can produce structured irrigation advice on Raspberry Pi hardware [35]. Therefore, "first offline AI for farmers" and "first edge agricultural LLM" are unsafe claims.

The defensible gap is more specific: no verified field deployment in this sweep runs a small offline language model that generates **cyclone- or flood-specific pre/post crop advice in Odia**, with SMS/IVR delivery and an approved safety corpus. AgroMetLLM still calls Open-Meteo for inputs, reports no local-language support, and has no hazard or recovery evaluation [35]. A feature phone also cannot host such a model, so "offline" should mean a block-level gateway, extension-agent phone, or cached decision package, not inference inside the IVR handset.

### The largest research gap is safety measurement

Farmer.Chat reports faithfulness, relevance, toxicity, and gender red-teaming [28]. AgroBench tests agricultural correctness but explicitly does not measure refusal behavior or real-world intervention safety [30]. None of the reviewed systems publishes a benchmark covering pesticide dose, prohibited chemicals, livestock medicine, flooded-soil re-entry, electrical hazards, contaminated fodder, or uncertainty under missing farm-profile fields.

KrishiSetu therefore needs its own Odisha Disaster Agronomy Safety Set: expert-authored cases, counterfactual crops and stages, ambiguous farmer speech, obsolete labels, conflicting weather updates, and adversarial dose requests. The pass criterion should be safe action selection and correct abstention, not fluent Odia.

## 5. LESSONS

| Strong analogue | What worked | What failed or remains unproven | Why it matters |
|---|---|---|---|
| Ama Krushi | Two-way IVR, saved profiles, expert answers, state handoff, measured weather-shock benefits [19] | Weekly and human-curated workflow is not shown as automatic cyclone/post-flood reasoning | Reuse the installed channel and trust network. |
| Farmer.Chat | Vetted RAG, multilingual/multimodal interaction, large query volume, human feedback [28] | **29%** of evaluated retrieval context was outside average precision; **18%** of answers had low relevance [28] | Retrieval and generation need separate gates. |
| BAMIS | Joins meteorology, water, crops, yields, and local databases [29] | Public pages do not show farm-level generative recovery plans | Hazard intelligence alone is not action personalization. |
| Nuru | Offline inference and strong constrained-task accuracy [2] | Narrow visual task; six leaves are recommended for best performance [2] | Constrained models can outperform open-ended chat where stakes are high. |
| AgroMetLLM | Edge feasibility and fast structured output [35] | No field, language, safety, voice, or disaster evaluation | Use as an edge feasibility reference, not a deployment benchmark. |
| FarmBeats | Local computation and continuity during outages [5] | Cloud-oriented analytics and retired Azure product path [16] | Design for graceful degradation and technology replacement. |

### Case study: Ama Krushi shows the shortest path to impact

Ama Krushi's mechanism is operational rather than novel: capture crop, livestock, land type, and location; push a weekly customized call; store that message against the farmer profile; and let the farmer call back through IVR or reach an agent [19]. The reported weather-shock outcomes suggest that timely customization can change losses even without an LLM [19].

The implication is uncomfortable but useful: a new standalone KrishiSetu number could fragment attention and duplicate a service now reaching nearly 7.9M farmers. The recommendation is an integration pilot in selected cyclone-prone blocks, using the Krushi Samruddhi profile and telephony layer while KrishiSetu supplies event detection, disaster rules, and post-event triage.

### Case study: Farmer.Chat shows why RAG is necessary but insufficient

Farmer.Chat uses expert-vetted documents, vector retrieval, farmer context, GPT models, translation, speech recognition, and human-created golden answers [28]. That architecture scaled from the paper's 15,000-user deployment to a current vendor claim exceeding 830,000 users [28][36].

Yet the evaluation exposes a reliability tail: approximately 10% of queries had low faithfulness and 18% had low relevance [28]. For general questions, that may trigger clarification. For pesticide, evacuation, drainage, or livestock actions, it can cause harm. KrishiSetu should let the LLM translate, explain, and compress an approved action object; it should not invent the action object.

### Case study: The China report illustrates trust accumulation risk

A 67-year-old farmer reportedly followed an unidentified chatbot's pesticide advice after earlier successful interactions and lost nearly 25 acres of sesame [38]. This is not a peer-reviewed causal study, and the OECD record's 150-acre figure conflicts with the syndicated account [37]. It should not be presented as settled fact.

The mechanism remains credible: repeated correct low-stakes answers create automation trust, then one confident high-stakes error bypasses local expertise. KrishiSetu should display the source and validity date, block unlabeled chemical combinations, require crop-stage and area confirmation, convert units deterministically, and route novel or dangerous requests to an agronomist.

## 6. REAL-vs-FILLER

| Classification | Entries | Evidence-based judgment |
|---|---|---|
| **Real, operational, and directly relevant** | Ama Krushi/Krushi Samruddhi, BAMIS, mKisan, Meghdoot, 8028, WFP Anticipatory Action | These are real services or programs. None alone proves the complete KrishiSetu loop. |
| **Real and operational, but indirect** | Farmer.Chat, Nuru, Farmerline, Ignitia, FieldView, xarvio, Fasal, Plantix, AgroStar, Gramophone | Useful components or lessons; not offline Odia cyclone-recovery LLMs. |
| **Real institutional AI with partial evidence** | iSAT, ExtensionBot, FBN Norm, Bayer GenAI pilot, Cropwise AI, KissanAI/Dhenu | Product existence is credible; public safety, scale, or outcome evidence varies sharply. |
| **Real research, not field systems** | AgroMetLLM, AgroBench, AgriBERT, agricultural QA work, CropGPT 2026, AgriGPT, edge-agent framework | Cite as technical prior art only. Do not call them deployed farmer services. |
| **Code/demo exists, production unproven** | Digital Green open-source Farmer.Chat code, Odia AgriBot, A2SV Crop-Intel-AI, KisanVaani repositories, KisanGPT web demos | Repositories demonstrate implementation intent, not adoption, uptime, agronomic accuracy, or safety. |
| **Marketing or idea-stage** | SHELTER landing page, generic "AI operating system" claims, undated copilot pages without metrics | Keep in competitor monitoring, exclude from proof of what works. |
| **Retired or time-bounded** | Azure FarmBeats; original Avaaj Otalo field deployment | Azure FarmBeats was retired Sept. 30, 2023 [16]. Avaaj Otalo's studied deployment ran Dec. 24, 2008-July 16, 2009 [31]. Their lessons survive; the deployments should not be labeled current. |

A real system can still have filler claims. Conversely, a retired or academic system can contain valuable engineering prior art. The correct filter is not "AI" in the name; it is documented users, an operational workflow, measured outcomes, model boundaries, and accountable content ownership.

## 7. NOISE LOG

| Searched term or candidate | Disposition | Reason for discard or downgrade |
|---|---|---|
| **Agriflow** | Discarded as unresolved | Searches returned unrelated agricultural workflow and commerce products, not a verified LLM advisory system matching the prompt. |
| **GrainChat** | Discarded as unresolved | No authoritative product, paper, repository, or deployment matching the proposed agricultural assistant was found. |
| **TARS / John Deere** | Discarded as a product name | Deere's official AI case study discusses See and Spray and internal AI workflows, not a farmer advisory product named TARS [26]. |
| **"AGRO apps"** | Too ambiguous | The label maps to many unrelated apps. Only named, attributable products were retained. |
| **Generic ESP32 LLM examples** | Discarded | Search results were microcontroller tutorials rather than deployed agricultural language models [67]. TinyML crop sensors and classifiers are relevant edge prior art, but not LLM advice. |
| **Crop Disaster Recovery** | Discarded | The result concerned US disaster-program assistance, not AI crop recovery generation. |
| **KisanGPT / KissanGPT** | Downgraded | Multiple unrelated sites use the name. No common organization, audited scale, or validated disaster system was established. |
| **KisanVaani** | Split into separate assets | The name refers to an English QA dataset and unrelated voice prototypes, so treating it as one deployed platform would conflate entities. |
| **SHELTER** | Ideas-only | Directly relevant landing-page language, but no reviewed deployment, users, technical paper, or outcome evidence [58]. |
| **Failed agtech startups** | No matching case retained | The search found generic failure essays but no well-sourced shutdown of a system matching the full problem. Azure FarmBeats is the only verified retirement and was a Microsoft service, not a failed startup [16]. |
| **China pesticide incident** | Retained with warning | It is the only concrete harm report found, but is syndicated, names no model, and conflicts with the OECD incident record on area [38][37]. |
| **Pure weather, insurance, market-price, and disease-only apps** | Mostly excluded | They do not transform authoritative hazards and farm profiles into pre/post crop actions. Representative component systems remain in the indirect table. |

The noise pattern is itself informative: agricultural AI search is saturated with renamed demos, generic chat wrappers, corporate "AI" pages, and repositories with no users. A credible KrishiSetu claim should publish its architecture, evaluation set, failure rates, advisory provenance, and field outcomes.

## 8. VERDICT: SYNTHESIS

### Comparative synthesis

| Approach | Mechanism | Scope and time horizon | Evidence base | Main trade-off |
|---|---|---|---|---|
| **Ama Krushi** | Profile plus curated voice advisory and human agronomists | Continuous/weekly, including weather shocks | State-scale service and reported crop-loss/harvest outcomes [19] | Trusted and inclusive, but not automatically event-triggered. |
| **BAMIS/WFP/iSAT** | Forecast or hazard data translated into anticipatory/agromet advice | Before and during climate hazards | Institutional programs and system descriptions [8][9][29] | Strong hazard authority, weaker farm-level recovery personalization. |
| **Farmer.Chat/ExtensionBot** | RAG over vetted extension knowledge | On-demand general advice | Usage data plus partial quality evaluation [28] | Broad and conversational, but nonzero unsafe-quality tail. |
| **Nuru/AgroMetLLM/FarmBeats** | Local classifier, local LLM, or edge gateway | Immediate diagnosis, irrigation, or outage continuity | Academic evaluation and prototypes [2][5][35] | Resilient computation, but narrow tasks and little disaster-language validation. |
| **FieldView/xarvio/Cropwise/Fasal** | Sensor, satellite, weather, and field analytics | Seasonal precision management | Operational commercial products, limited public error data [48][45][46] | Rich data, but smartphone/cloud orientation and limited public safety evidence. |

The non-obvious conclusion is that KrishiSetu's strongest competitor is not Farmer.Chat. It is the combination of **Ama Krushi's installed Odisha voice/profile infrastructure**, **IMD's forecast feeds**, and **Odisha's contingency manuals**. Farmer.Chat supplies the conversational pattern; BAMIS supplies the closest hazard architecture; Nuru and AgroMetLLM bound what "offline" can honestly mean.

### Honest differentiation claim

A defensible statement is:

> **"In the public systems and research reviewed through August 16, 2026, we found no verified deployed platform that unifies authoritative IMD cyclone/flood triggers, hyperlocal Odisha farm profiles, expert-validated pre- and post-disaster crop actions, Odia SMS/IVR delivery, and an offline-capable constrained language layer. KrishiSetu differentiates on that governed closed-loop integration, not on any single component."**

Avoid claiming:

- the first AI agricultural advisor;
- the first RAG system for farmers;
- the first hyperlocal weather advisory;
- the first IVR farm service;
- the first offline agricultural AI; or
- the first edge agricultural LLM.

### Recommended product and safety boundary

1. **Integrate before replacing.** Pilot through Krushi Samruddhi Helpline profiles, shortcode, agents, and outbound calls.
2. **Make actions deterministic.** Convert Odisha contingency guidance into approved action objects with crop, stage, hazard, lead time, contraindications, evidence, version, and expiry.
3. **Use the LLM at the language boundary.** Let it classify intent, retrieve an approved action, translate into Odia, simplify for IVR, and answer follow-ups. Do not let it create pesticide doses or livestock treatment plans.
4. **Design offline in layers.** Cache district forecasts and action bundles at block gateways or extension phones; retain SMS and IVR when data fails; use the local LLM only where hardware permits.
5. **Require two-way confirmation.** Ask whether the crop is standing or harvested, whether water has entered the plot, crop stage, acreage, and access to labor before issuing irreversible actions.
6. **Escalate high-risk cases.** Chemicals, veterinary medicine, electrocution, contaminated water/fodder, and conflicting warnings go to a human expert.
7. **Publish a safety scorecard.** Measure source faithfulness, correct action, harmful-action rate, abstention quality, Odia speech error, delivery latency, message completion, and farmer action uptake separately.
8. **Version every advisory.** Store the IMD alert, profile snapshot, retrieved rule, generated wording, delivery status, farmer response, and override. This creates the audit trail missing from most prior art.

The winning differentiation is therefore **safe orchestration under disaster conditions**. It is narrower than "AI for agriculture," but stronger, more credible, and more useful.

## SOURCES / REFERENCES

1. Digital Green, "Farmer.Chat: Scaling AI-Powered Agricultural Services for Smallholder Farmers," Sept. 13, 2024: https://arxiv.org/html/2409.08916v1 [28]
2. Farmer.Chat current product page: https://farmerchat.io/ [36]
3. Precision Development, Ama Krushi project page: https://precisiondev.org/project/ama-krushi [19]
4. Precision Development, 2024 weather-shock evidence: https://precisiondev.org/2024-annual-report/customized-digital-advice-can-help-farmers-manage-crop-loss-and-weather-shocks-evidence-from-pxds-work-in-odisha [18]
5. Bangladesh Agro-Meteorological Information Service: https://www.bamis.gov.bd/en and https://www.bamis.gov.bd/en/page/introduction [25][29]
6. ICRISAT, Intelligent Agricultural Systems Advisory Tool: https://issca.icrisat.org/index.php/scalable-solutions/intelligent-agricultural-systems-advisory-tool-isat [9]
7. Odisha Department of Agriculture, Crop Contingency Plan 2025: https://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf [41]
8. India Meteorological Department API Reference: https://api.imd.gov.in/public/api_reference.html [33]
9. World Food Programme, Anticipatory Action: https://www.wfp.org/anticipatory-actions [8]
10. Ethiopia Agricultural Transformation Institute, 8028 Farmer Hotline: http://ati.gov.et/8028-farmer-hotline [14]
11. PlantVillage Nuru evaluation: https://biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf [2]
12. Ray, "AgroMetLLM," Journal of Agrometeorology, Sept. 2025: https://journal.agrimetassociation.org/index.php/jam/article/view/3081 [35]
13. Shinoda et al., "AgroBench," ICCV 2025: https://openaccess.thecvf.com/content/ICCV2025/papers/Shinoda_AgroBench_Vision-Language_Model_Benchmark_in_Agriculture_ICCV_2025_paper.pdf [30]
14. Microsoft FarmBeats research paper: https://microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf [5]
15. Microsoft FarmVibes.AI repository: https://github.com/microsoft/farmvibes-ai [12]
16. FBN, "Meet Norm," Apr. 15, 2023: https://www.fbn.com/community/blog/norm-first-ai-ag-advisor [21]
17. Bayer, agricultural GenAI pilot, Mar. 14, 2024: https://www.bayer.com/media/en-us/bayer-pilots-unique-generative-ai-tool-for-agriculture [24]
18. CGIAR, AgriLLM: https://www.cgiar.org/news-events/news/agrillm-how-cgiar-is-developing-an-ai-powered-agricultural-advisory-service-for-global-south [11]
19. Extension Foundation, ExtensionBot: https://extension.org/extensionbot [22]
20. Reported China pesticide incident and OECD.AI record: https://www.latestly.com/world/china-farmer-loses-nearly-25-acres-of-sesame-crop-in-anhui-after-following-ai-pesticide-advice-7556191.html and https://oecd.ai/en/incidents/2026-08-01-90d7 [38][37]

## References

1. *Farmer.Chat: Scaling AI-Powered Agricultural Services for ...*. https://arxiv.org/abs/2409.08916
2. *http://biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf*. http://biorxiv.org/content/10.1101/2020.01.26.919449v2.full.pdf
3. *The CropGPT project: Call for a global, coordinated effort in ...*. https://www.cell.com/molecular-plant/pdf/S1674-2052%2823%2900409-4.pdf
4. *mKisan: A Portal of Government of State Base Services for ...*. https://mkisan.gov.in/Home/AboutPushSMS
5. *http://microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf*. http://microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf
6. *‎Meghdoot App - App Store*. https://apps.apple.com/us/app/meghdoot/id1474048155
7. *Dhenu | The AI Operating System for Agriculture, by KissanAI*. https://dhenu.ai/
8. *http://wfp.org/anticipatory-actions*. http://wfp.org/anticipatory-actions
9. *ISSCA - Intelligent Agricultural Systems Advisory Tool (iSAT)*. https://issca.icrisat.org/index.php/scalable-solutions/intelligent-agricultural-systems-advisory-tool-isat
10. *Building agricultural database for farmers | OpenAI*. http://openai.com/index/digital-green
11. *AgriLLM: How CGIAR is developing an AI-powered agricultural ...*. https://www.cgiar.org/news-events/news/agrillm-how-cgiar-is-developing-an-ai-powered-agricultural-advisory-service-for-global-south
12. *GitHub - microsoft/farmvibes-ai: FarmVibes.AI: Multi-Modal ...*. https://github.com/microsoft/farmvibes-ai
13. *GitHub - REETIKAJENA025/AGRICULTURAL-BOT: AgriBot is a ...*. https://github.com/REETIKAJENA025/AGRICULTURAL-BOT
14. *8028 Farmer Hotline - Agricultural Transformation Institute*. http://ati.gov.et/8028-farmer-hotline
15. *Evaluating iSAT climate-informed agro-advisories for farm decisions and system performance in Senegal’s drylands*. https://www.nature.com/articles/s41598-026-44231-y
16. *Azure September: Announced end of life | Microsoft Community Hub*. https://techcommunity.microsoft.com/discussions/azure/azure-september-announced-end-of-life/3941524
17. *Ignitia - Digital X Solution*. https://digitalx.undp.org/catalogs/ignitia.html
18. *Customized digital advice can help farmers manage crop loss ...*. https://precisiondev.org/2024-annual-report/customized-digital-advice-can-help-farmers-manage-crop-loss-and-weather-shocks-evidence-from-pxds-work-in-odisha
19. *Ama Krushi – Scaling advisory services to millions of farmers ...*. https://precisiondev.org/project/ama-krushi
20. *Ama Krushi Transition Insights Report - precisiondev.org*. https://precisiondev.org/wp-content/uploads/2025/04/AK-Transition-Insights-2025_condensed.pdf
21. *Meet Norm, the World's First AI Ag Advisor*. https://www.fbn.com/community/blog/norm-first-ai-ag-advisor
22. *ExtensionBot – Extension Foundation*. https://extension.org/extensionbot
23. *Cropwise AI | Cropwise*. https://www.cropwise.com/innovations/cropwise_ai
24. *Bayer pilots unique generative AI tool for agriculture*. https://www.bayer.com/media/en-us/bayer-pilots-unique-generative-ai-tool-for-agriculture
25. *Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en
26. *John Deere transforms agriculture with AI | OpenAI*. https://openai.com/index/john-deere-justin-rose
27. *Smallholders Leaderboard - AI AgriBench*. https://aiagribench.org/smallholders
28. *Farmer.Chat: Scaling AI-Powered Agricultural Services for Smallholder Farmers*. https://arxiv.org/html/2409.08916v1
29. *Background - Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en/page/introduction
30. *AgroBench: Vision-Language Model Benchmark in Agriculture*. https://openaccess.thecvf.com/content/ICCV2025/papers/Shinoda_AgroBench_Vision-Language_Model_Benchmark_in_Agriculture_ICCV_2025_paper.pdf
31. *dl.acm.org*. https://dl.acm.org/doi/pdf/10.1145/1753326.1753434
32. *GitHub - Crop-Intel-Ai/A2SV-Hackathon: AI-Powered ...*. https://github.com/Crop-Intel-Ai/A2SV-Hackathon
33. *http://api.imd.gov.in/public/api_reference.html*. http://api.imd.gov.in/public/api_reference.html
34. *CropGPT: A large multimodal model for precise and explainable diagnosis of crop pests and diseases - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2452414X26000488
35. [
		AgroMetLLM: An evapotranspiration and agro-advisory system using localized large language models in resource-constrained edge
							| Journal of Agrometeorology
			](https://journal.agrimetassociation.org/index.php/jam/article/view/3081)
36. *http://farmerchat.io/*. http://farmerchat.io/
37. *AI-Generated Pesticide Advice Destroys 150 Acres of Sesame in ...*. https://oecd.ai/en/incidents/2026-08-01-90d7
38. *China: Farmer Loses Nearly 25 Acres of Sesame Crop in Anhui ...*. https://www.latestly.com/world/china-farmer-loses-nearly-25-acres-of-sesame-crop-in-anhui-after-following-ai-pesticide-advice-7556191.html
39. *http://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai*. http://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai
40. *http://mkisan.gov.in/alpha*. http://mkisan.gov.in/alpha
41. *http://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf*. http://agrisnetodisha.ori.nic.in/crop%20contigency%20plan%202025.pdf
42. *http://pib.gov.in/PressReleasePage.aspx?PRID=2278757&lang=1&reg=3*. http://pib.gov.in/PressReleasePage.aspx?PRID=2278757&lang=1&reg=3
43. *Farmerline: Empowering farmers via mobile technology*. https://nelisglobal.org/4revs/farmerline-empowering-farmers-via-mobile-technology
44. *Farmer Advisory Management | Real-time farmer advisory.*. https://krishify.com/product/farmer-advisory-management/
45. *FieldView™ - Digital Farming's Platform - Bayer Crop Science*. https://www.cropscience.bayer.us/tools/fieldview
46. *xarvio® Digital Farming Solutions - USA (English)*. https://www.xarvio.com/
47. *FIELD MANAGER - xarvio*. https://www.xarvio.com/us/en/products/field-manager.html
48. *http://sti-portal.fao.org/innovations/fasal*. http://sti-portal.fao.org/innovations/fasal
49. *http://plantix.net/en/plantix-intelligence/api-toolkit*. http://plantix.net/en/plantix-intelligence/api-toolkit
50. *http://corporate.agrostar.in/*. http://corporate.agrostar.in/
51. *http://play.google.com/store/apps/details?hl=en&id=agstack.gramophone*. http://play.google.com/store/apps/details?hl=en&id=agstack.gramophone
52. *http://microsoft.com/en-in/aifirstmovers/kissanai*. http://microsoft.com/en-in/aifirstmovers/kissanai
53. *AgriBERT: Knowledge-Infused Agricultural Language Models for ...*. https://www.ijcai.org/proceedings/2022/715
54. *Agricultural Question Answering Dataset Creation and its ...*. https://ieeexplore.ieee.org/document/10969374
55. *Agricultural Question Answering Dataset Creation and its ...*. https://www.researchgate.net/publication/391046735_Agricultural_Question_Answering_Dataset_Creation_and_its_Evaluation_through_BERT_based_Experimental_Analysis
56. *AgriGPT: a Large Language Model Ecosystem for Agriculture*. https://arxiv.org/abs/2508.08632
57. *AGRIVOICE-MULTILINGUAL VOICE & TEXT FARMING ASSISTANT*. https://www.jetir.org/view?paper=JETIR2507621
58. *SHELTER — 7-day satellite early warning for African agriculture*. https://shelter.zerorate.io/
59. *http://sciencedirect.com/science/article/pii/S2590123025033973*. http://sciencedirect.com/science/article/pii/S2590123025033973
60. *KisanGPT — Smart AI for Farmers | by ArtifyCode*. https://kisangpt.online/
61. *BharatKisanGPT.com*. https://kisangpt.com/
62. *KissanGPT - Your AI Farming Assistant*. https://kissangpt.streamlit.app/
63. *Crop Analyzer – BharatKisanGPT*. https://kisangpt.com/crop_analyzer.php
64. *KisanVaani/agriculture-qa-english-only · Datasets at Hugging Face*. https://huggingface.co/datasets/KisanVaani/agriculture-qa-english-only
65. *GitHub - frenchfryfeatures/kisan-vaani*. https://github.com/frenchfryfeatures/kisan-vaani
66. *How I Built Kisan Vaani: A Multi-Agent Voice AI Assistant for ...*. https://dev.to/_adi_17/how-i-built-kisan-vaani-a-multi-agent-voice-ai-assistant-for-indian-farmers-550c
67. *TinyML with ESP32 Tutorial - Microcontroller Tutorials*. https://www.teachmemicro.com/tinyml-with-esp32-tutorial
