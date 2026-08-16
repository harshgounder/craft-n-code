# Global Last-Mile Prior Art for KrishiSetu

## 1. EXECUTIVE SUMMARY

- **Closest Global Precedent**: South Korea already operates a farm-specific early-warning system that combines registered farm, crop, and variety data with crop-stage weather hazards, response guidance, mobile web, and text messages. It covers 30 crop types and as many as 11 disaster factors; surveyed users rated disaster-prevention usefulness **4.15/5** [35]. -> Do not claim that farm-profiled weather warnings or SMS response guidance are globally new.
- **Closest Low-Income-Country Precedent**: Bangladesh's BAMIS joins weather, water, and agricultural information and publishes advisories for cyclone, river flood, flash flood, heat, salinity, and storms; its public portal still carried dated advisories in June 2026 [25][8]. -> Differentiate on closed-loop farm personalization, voice accessibility, and verified action, not merely on combining alerts with crop advice.
- **Delivery Failure Is a Product Requirement**: In ACRE Africa's Zambia program, **587,842** messages were sent, **361,539** were delivered, and **217,134** failed; the report called this a **56% success rate** and recorded inactive numbers, network problems, late messages, and difficulty understanding weather and cyclone content [26]. -> Build retry, voice fallback, number hygiene, comprehension checks, and timing service-level objectives into the core architecture.
- **Voice and Broadcast Have the Best Basic-Phone Scale Evidence**: Ethiopia's 8028 hotline passed **6M subscribers and 60M calls** [40], while Farm Radio International reported **24.1M listeners** and **4.8M people taking action** in FY2022-23 [23]. -> Use outbound IVR plus toll-free callback and interactive radio as the primary reach layer; treat SMS as a compact record and USSD as a pull channel.
- **Odisha Is Not a Greenfield**: Ama Krushi was designed as a customized, two-way digital advisory service for millions of Odisha smallholders [73], and Odisha research found periodic telephone advisories and reminders more effective than one-time interaction [99]. -> KrishiSetu must integrate or complement the existing advisory and disaster institutions rather than present another disconnected chatbot.
- **Redundancy Beats a Single Channel**: Multi-channel villages using SMS, voice, meetings, extension staff, clubs, and public announcements had higher awareness and advisory use, while farmers still preferred village training and extension discussion [100]. -> The best fit is a voice-first cascade: outbound IVR, SMS summary, missed-call callback, USSD status, radio escalation, and extension-worker follow-up.
- **Offline-First Does Not Mean Basic-Phone-First**: Nuru, ODK, CommCare, and the Community Health Toolkit prove offline capture, local inference, and store-and-forward synchronization, but they primarily equip smartphone users or frontline workers. ODK reports **2M users and 250M annual submissions**, and CommCare reports more than **1M frontline workers in 130+ countries** [34][32]. -> Put the offline app in the hands of extension workers and village operators, not make it the sole farmer interface.
- **Defensible Differentiation Is Narrow but Valuable**: No verified analogue in this sweep demonstrated the full Odisha-specific chain of official IMD/WINDS/OSDMA trigger, farm and crop-stage profile, agronomist-governed pre-event and post-event playbooks, redundant basic-phone delivery, acknowledgement, and measured recovery outcome. -> Claim a new orchestration and assurance layer, not the first use of AI, IoT, SMS, IVR, hyperlocal weather, or agricultural warnings.

## 2. WORLDWIDE INVENTORY

Classification rule: a **direct match** implements at least three links in the target chain - hazard or weather signal, farm/crop context, actionable advice, and constrained-connectivity delivery. An **indirect match** contributes a proven delivery, data, finance, diagnostic, or offline pattern. **Ideas-only** means a repository, paper, hackathon prototype, or concept for which this sweep found no credible deployment evidence. Scale figures preserve the source's own unit - registrations, people reached, calls, messages, listeners, or active users are not interchangeable.

### Direct matches and close partial matches

| Name | Country | Channel and what it does | Named source, URL, date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| Farm-specific Early Warning System | South Korea | Registered farm, crop, and variety data drive crop-stage forecasts, disaster warnings, response information, mobile web, and texts [35]. | Agronomy, <https://doi.org/10.3390/agronomy15030547>, 28 Feb 2025 | Operational regional system | 30 crop types; up to 11 disaster factors; 30 m output; surveyed usefulness 4.18/5 overall and 4.15/5 for disaster prevention [35] | The core logic is precedented. KrishiSetu can improve last-mile voice, local dialects, flood/cyclone recovery, and acknowledgement. |
| BAMIS | Bangladesh | Weather, river, crop, and hazard information supports advisories for cyclone, flood, heat, salinity, and storms; the program also developed web and dissemination mechanisms [25][8]. | Bangladesh Agrometeorological Information Service, <https://www.bamis.gov.bd/en/>, project records 2016-2021; portal observed 1 Jun 2026 | Project phase ended; public portal remained operational | Databases covered 487 upazilas; farmer-level active-use and outcome scale not disclosed [25] | Strong national data and hazard precedent; add farm-specific profiles, IVR confirmation, and outcome telemetry. |
| ACRE Africa tailored advisory campaign | Zambia | Weather and crop-management SMS were tailored by agroecological zone; the evaluation recorded delivery, timing, network, and comprehension failures [26]. | ACRE Africa, Zambia SMS Feedback Report, <https://acreafrica.com/>, Jan 2025 | Deployed campaign | 153,312 valid phone records; 587,842 sent; 361,539 delivered; 217,134 failed [26] | Design for failed delivery and misunderstood warnings, not just correct agronomy. |
| Ama Krushi / Krushi Samruddhi | Odisha, India | Customized two-way digital agricultural advice, including telephone delivery and repeated reminders [80][73]. | Precision Development, <https://precisiondev.org/>, Jul 2023 and Apr 2025 reports | Real program with government transition; current component boundaries should be confirmed before reuse | Source describes service for millions; audited active-user and disaster-specific outcome counts were not found | This is the most important local collision. Reuse farmer relationships, language content, and call operations where possible. |
| Rice Crop Manager dissemination | Odisha, India | Crop-specific advice delivered through printed CSC interactions or seasonal telephone calls followed by periodic calls and reminders [99]. | Frontiers in Sustainable Food Systems, <https://doi.org/10.3389/fsufs.2026.1701246>, 2026 | Evaluated deployment | Study covered participating farmers across all 30 Odisha districts [99] | Repeated voice contact outperforms a one-shot recommendation; disaster flows should use the same cadence. |
| M-Omulimisa | Uganda | USSD at **\*217\*101#**, SMS/voice interaction, weather and AgroMet information, and market information [20][47]. | M-Omulimisa, <https://momulimisa.com/>, undated; accessed 16 Aug 2026 | Live website and service endpoints | Credible current total active-user count not found | USSD provides low-bandwidth pull access, but urgent hazards still need pushed voice/SMS. |
| BaKhabar Kissan | Pakistan | App-based crop advice, expert access, rain alerts, satellite monitoring, and weather-station data [11]. | BaKhabar Kissan, <https://www.bkk.ag/>, undated; accessed 16 Aug 2026 | Live commercial platform | Marketing page says 15.8M+ service users and 300+ weather stations, without defining active use [11] | Sensor and agronomy integration is relevant; the app-led channel and marketing scale are not proof of basic-phone disaster reach. |
| IMD Agromet plus WINDS | India | IMD agrometeorological bulletins combine forecast and crop advice; WINDS is designed as a block and gram-panchayat network of automatic weather stations and rain gauges with APIs for crop advisories and disaster resilience [101]. | Government of India PMFBY/WINDS guidelines, <https://pmfby.gov.in/>, undated guidelines; IMD portal accessed 16 Aug 2026 | Government infrastructure and advisory system | Guidelines describe about 13,000 existing AWS, 20,000 ARG, and plans for 3,500 more AWS and about 160,000 ARG [101] | This should be KrishiSetu's data backbone, not a feature claimed as original. |
| Odisha EWDS | Odisha, India | Satellite and digital mobile radio links, 122 coastal alert towers, mass messaging, and warnings by message, voice, and siren [102]. | OSDMA, <https://www.osdma.org/preparedness/early-warning-communications/ewds/>, undated; accessed 16 Aug 2026 | Operational public warning infrastructure | Designed to reach remote coastal communities within minutes; farm-action conversion is outside its stated scope [102] | Trigger and redundancy layer already exists; KrishiSetu should translate a warning into plot and crop actions. |
| Sandji | Mali | Historical service sending daily French or Bambara SMS with short-horizon rainfall probability and intensity. | CCAFS/CGIAR case material, <https://ccafs.cgiar.org/>, 2016 case material | Historical deployment; present status unverified | Reliable active-user and outcome counts not found | Local language and predictable timing matter, but forecast messages alone do not close the action loop. |
| iShamba | Kenya | Agricultural information through SMS, weather updates, and access to a call centre [52][79]. | iShamba, <https://ishamba.com/>, undated; accessed 16 Aug 2026 | Live website; operating scale not independently verified | Not publicly established in the reviewed sources | Pair short messages with a human escalation path for ambiguous or high-risk cases. |
| Farmerline / Mergdata | Ghana and multi-country | Offline-capable, local-language farmer profiling and messaging for agribusiness and public programs [17]. | Farmerline, <https://farmerline.co/>, undated; accessed 16 Aug 2026 | Live commercial platform | Company reports 3,000+ partners in 50 countries and 2.3M+ farmers reached [17] | A reusable profiling and delivery layer can scale, but "reached" is not the same as warnings heard or actions completed. |

**Direct-match takeaway:** South Korea establishes that farm-specific hazard warnings with response advice are prior art. BAMIS and ACRE show the same idea in lower-connectivity settings, but also expose the unresolved gap: reliable voice delivery, comprehension, acknowledgement, and post-disaster recovery measured at farm level.

### Indirect systems and transferable delivery patterns

| Name | Country or region | Channel and what it contributes | Named source, URL, date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| Esoko | Ghana / Africa | SMS-based market and agricultural information plus farmer and value-chain data tools. | Esoko, <https://esoko.com/>, undated; accessed 16 Aug 2026 | Live company; original product evolved | Historical multi-country reach is reported, but a comparable current active-user figure was not verified | SMS is effective for concise prices and reminders; disaster instructions need voice, sequencing, and confirmation. |
| WeFarm | Kenya / UK-led | Historically a peer-to-peer SMS question network; its current public presence emphasizes web groups and community discussion [84]. | WeFarm, <https://wefarm.co/>, accessed 16 Aug 2026 | Real historical service; current web community visible, continuity of the original SMS network unverified | Do not reuse historical registration claims as current activity | Peer answers create trust, but urgent warnings need authoritative moderation and an escalation clock. |
| M-Farm | Kenya | Historical mobile market-price, buyer, and farmer-connection service. | M-Farm, <http://mfarm.co.ke/>, historical sources; checked 16 Aug 2026 | Historical company; current operating status unresolved, not proven dead | Historical claims vary; no current audited active scale found | Market linkage is useful during recovery, but evidence is insufficient for a live disaster-advisory comparison. |
| iCow | Kenya | Feature-phone SMS/USSD and keyword interactions use farm information and calendars to send actionable husbandry reminders [44]. | iCow, <https://www.icow.co.ke/>, undated; accessed 16 Aug 2026 | Live website; no evidence found that it has "died" | Company reports 1.6M farmers reached and 110M educational SMS, not audited active users [44] | Calendar-triggered micro-actions are an excellent pattern for crop-stage disaster preparation. |
| Farmer's Friend | Uganda, not Nigeria | Google/AppLab SMS keyword service for agricultural tips, alongside Google Trader [41]. | GSMA/AppLab case material, <https://www.gsma.com/mobilefordevelopment/>, historical | Real historical deployment; present status not found | No defensible current scale found | Correct the geography and classify as a historical SMS knowledge service, not a current Nigerian platform. |
| e-Krishok | Bangladesh | Telecentre-assisted farmer inquiries and agricultural problem solving. | ITU case study, <https://www.itu.int/>, 2013 | Real historical program; current status unclear | By Mar 2013, records reported 48,696 reached, 84,120 inquiries, 72,103 solutions, and about 29,035 beneficiary farmers [103] | Assisted access can overcome literacy and phone ownership constraints; maintain a village intermediary tier. |
| Viamo Platform / 3-2-1 | Africa and Asia | Basic-phone IVR and SMS in local languages, with subscriber profiles and targeted campaigns [78][53]. | Viamo, <https://viamo.io/>, undated; accessed 16 Aug 2026 | Live commercial delivery platform | Viamo reports 35M people engaged in one year across 20 countries and 70 languages; platform page reports 27M+ subscribers [78][53] | Buy or emulate mature voice operations rather than treating telephony as a thin API integration. |
| Arifu | Kenya and multi-country | Adaptive mobile learning through conversational messaging, used for agriculture and financial learning. | Arifu / 60 Decibels impact report, <https://www.arifu.com/>, 2020 | Live company | Reach claims exist, but this sweep did not find a like-for-like audited active-user and unit-cost figure [57] | Progressive lessons and quizzes can test comprehension after a warning. |
| Farm Radio International | Africa | Participatory radio campaigns combine scheduled programs, local broadcasters, call-ins, polling, and mobile interaction. | Farm Radio International, <https://farmradio.org/>, FY2022-23 impact report | Live nonprofit network | 24.1M listeners and 4.8M people reported taking action in FY2022-23 [23] | Radio is the widest failover channel, but targeting and attribution are weaker than IVR. |
| Uliza | Africa | Radio companion platform uses a free missed-call callback, IVR, polls, and listener interaction; more than 350 radio partners and 500,000 individual listeners were reported [37]. | Farm Radio International, <https://farmradio.org/uliza/>, undated | Live program/platform | More than 350 partners and 500,000 listeners reported | A missed-call callback removes airtime cost; cap or triage open questions because answer capacity is a known constraint [37]. |
| DigiFarm | Kenya | Integrated mobile platform joins customized farm information with inputs, finance, and market functions [31]. | Mercy Corps AgriFin, <https://www.mercycorpsagrifin.org/>, 9 Jun 2020 | Real scaled program | 1,038,817 registered users, but only 30% activity; 60,000 digital input loans with nearly 90% repayment [31] | Registration is a vanity metric. KrishiSetu should report delivery, listen-through, comprehension, action, and loss avoided. |
| Jaza Duka | Kenya | Merchant inventory credit combining Unilever distribution data, KCB finance, and Mastercard infrastructure; it is not a farm-advisory system [67]. | Mastercard, <https://www.mastercard.com/news/>, 1 May 2018 | Real finance program | Thousands of micro-retailers reported; not a farmer-warning scale | Relevant only as a mobile-credit/recovery analogy. It should not be cited as prior art for hazard advice or USSD without interface evidence. |
| 8028 Farmer Hotline | Ethiopia | Toll-free automated voice and helpdesk service for agricultural information [15]. | Ethiopian Agricultural Transformation Institute, <https://ati.gov.et/>, current page accessed 16 Aug 2026 | Live national service | More than 6M subscribers and 60M calls reported [40] | Toll-free pull voice can absorb repeat listening and questions after outbound alerts. |
| Airtel Kilimo | Kenya | Historical mobile agriculture value-added service using basic-phone information delivery. | GSMA mAgri case study, <https://www.gsma.com/mobilefordevelopment/>, 2015 | Real historical service; current status not established | Historical scale only; not used as a current benchmark | Operator distribution helps launch, but a carrier bundle does not prove sustained farmer value. |
| Vodafone Farmers' Club | Ghana | Mobile agricultural content bundled with farmer-oriented telecom services. | GSMA mAgri case material, <https://www.gsma.com/mobilefordevelopment/>, historical | Historical service | No current active scale established | Bundling can subsidize communication, but operator churn and changing bundles create continuity risk. |
| M'chikumbe 212 | Malawi | Dial-in agricultural voice service for feature-phone users. | GSMA/FAO case material, <https://www.gsma.com/mobilefordevelopment/>, historical | Real historical service; current status unclear | Historical usage reported, but no current audited figure found | A memorable short code and local-language menu are more usable than a deep app navigation tree. |
| Avaaj Otalo | Gujarat, India | Interactive voice forum lets farmers record questions, hear answers, and browse prior agricultural discussions [71]. | ACM/ICTD research, <https://dl.acm.org/>, 2010 | Field research deployment | Small study, not national scale | Voice community interaction is proven, but warnings require verified answers and priority routing. |
| PlantVillage Nuru | Africa and India | Smartphone-based, offline crop-disease diagnosis and extension support [22]. | PlantVillage/FAO case, <https://plantvillage.psu.edu/>, 10 Nov 2020 | Real field system | Grew from 30 to about 400 active users in the cited period; one farmer case reported 55% higher revenue and 146% higher yield, which is anecdotal rather than a population effect [22] | Run offline diagnosis on extension phones; send resulting actions to farmers over voice/SMS. |
| CommCare | Global | Offline mobile case management and forms that synchronize when connectivity returns [34]. | Dimagi, <https://www.dimagi.com/commcare/>, accessed 16 Aug 2026 | Live platform | 1M+ frontline workers in 130+ countries [34] | Strong template for extension-worker workflows and household follow-up, not for running an LLM on a feature phone. |
| ODK | Global | Offline forms, geospatial data, media, and delayed synchronization [32]. | ODK, <https://getodk.org/>, accessed 16 Aug 2026 | Live open-source platform | 2M users and 250M submissions annually reported [32] | Use for rapid damage assessment and farmer-profile updates after connectivity returns. |
| Community Health Toolkit / Medic | Global | Supports SMS on basic phones plus smartphone, tablet, and web workflows; local data can sync later [13]. | Community Health Toolkit, <https://communityhealthtoolkit.org/>, updated 27 Feb 2026 | Live open-source ecosystem | Six national government systems as of 2024 and about 1M home visits per month reported [13] | Best non-agricultural reference architecture for connecting basic phones to offline frontline workers and national systems. |
| DeHaat Farmer App | India | App offers regional-language voice calls, reminders, crop advice, weather, and market rates [104]. | DeHaat, <https://agrevolution.in/solution-for-farmers>, accessed 16 Aug 2026 | Live commercial service | Company says 1.4M+ farmers in 12 states [104] | Rich service bundle is useful for recovery, but app dependence excludes the target's weakest-connectivity segment. |
| Jiva | Indonesia and Asia | App and field-partner network combines personalized agronomy, commerce, finance, and harvest support [16]. | Jiva, <https://www.jiva.ag/>, accessed 16 Aug 2026 | Live company | Ambitious market statements were found, but no comparable audited disaster-advisory scale | Human agents plus software can close last-mile trust gaps; no verified basis was found for calling it a WhatsApp warning service. |
| WhatsApp farmer groups | Nigeria and other markets | Farmer-managed groups enable rapid peer and extension advice, including crop-management discussion [92]. | Frontiers and field studies, <https://www.frontiersin.org/>, 2024-2026 literature | Real channel pattern, not one platform | Group-specific; no unified scale or quality control | Useful as an optional smartphone channel, but forwarding, moderation, privacy, and network dependence make it unsafe as the primary alert path. |
| Sesame Workshop mobile-learning practice | Multi-country | Human-centered, iterative mobile learning and messaging, not a verified agricultural warning service. | Sesame Workshop, <https://sesameworkshop.org/>, accessed 16 Aug 2026 | Real organization and design practice; agricultural analogue not identified | Not applicable to farm-warning scale | Borrow message testing with low-literacy users; do not list it as deployed agricultural prior art. |

**Indirect-system takeaway:** Scale comes from distribution and interaction design, not from AI sophistication. Voice hotlines, radio, operator channels, and assisted village access repeatedly outrun app-only systems; offline apps are most credible as tools for extension workers.

### Ideas-only, repositories, hackathons, and research concepts

| Name | Country or scope | What the artefact proposes | Named source, URL, date | Status | Scale | What KrishiSetu can learn |
|---|---|---|---|---|---|---|
| Chenjezo | Malawi | NASA/weather-informed drought and flood warning concept with SMS alerts. | GitHub repository search, <https://github.com/search?q=Chenjezo&type=repositories>, created 22 Dec 2025 | Prototype / idea | 1 star, 0 forks, 2 commits when observed [28] | Architecturally close, but repository activity is not evidence of farmer deployment. |
| AgroFutures / ai-ussd-2g-feature-phone | Kenya-oriented | USSD workflow with personalized weather/satellite advice and voice callback in local languages [24]. | GitHub repository search, <https://github.com/search?q=ai-ussd-2g-feature-phone&type=repositories>, accessed 16 Aug 2026 | Prototype / idea | No verified deployment | Useful interaction mock-up; needs agronomic governance, carrier operations, and field evidence. |
| KrishiSakhi | India | Smart alerts, personalized crop advice, disease detection, and chatbot functions. | GitHub/SIH 2025 search, <https://github.com/search?q=KrishiSakhi+SIH&type=repositories>, 2025 | Hackathon prototype | No verified deployment [42] | Shows idea saturation: feature lists are not defensible novelty. |
| KisanVaani | India | Voice/SMS agricultural-assistance concept. | GitHub search, <https://github.com/search?q=KisanVaani&type=repositories>, accessed 16 Aug 2026 | Prototype / idea | No verified deployment [48] | Voice UX code can accelerate a demo, but production telephony and content liability remain unsolved. |
| PocketLLM | Research / global | Experiments with compact on-device language models and fine-tuning. | arXiv search, <https://arxiv.org/search/?query=PocketLLM&searchtype=all>, 2024 research | Research | No verified agricultural field deployment | Potential future tool for an extension smartphone; not credible for 2G feature phones or time-critical warnings today. |
| MobiLLM label | Research / global | Claimed mobile-LLM concept in search results. | Scholarly and repository sweep, accessed 16 Aug 2026 | Unresolved label, not a verified deployable system | None established | Exclude from the prior-art claim until a stable paper/repository and measured device profile are identified. |
| Offline agriculture app case pages | Unspecified | Vendor pages describe offline-first advisory apps, sometimes claiming thousands of farmers. | Vendor case pages, including Brainstack-style software portfolios, accessed 16 Aug 2026 | Marketing case, client often unnamed | Unverified | Treat anonymous portfolios as leads, not evidence. |
| Generic WhatsApp AI bots | Global | Chatbot demos answer farm questions over WhatsApp. | GitHub/Devpost sweep, accessed 16 Aug 2026 | Demo / idea unless a named deployment is shown | No credible farmer outcome scale found | WhatsApp is an optional channel, not a low-connectivity resilience strategy. |

**Ideas-only takeaway:** The architecture is easy to propose and common in hackathons. The difficult and differentiable work is authoritative data integration, agronomic safety, carrier-grade delivery, local-language comprehension, institutional ownership, and outcome measurement.

## 3. COVERAGE TABLE

Grades describe evidentiary usefulness for an honest differentiation claim, not the quality of the organizations.

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---|---|---|
| Government and meteorological sources | South Korea EWS, BAMIS, IMD/WINDS, Odisha EWDS, Ethiopia 8028 | Often omit active-user definitions, cost, delivery success, and controlled outcomes | **A** - strongest proof that systems and infrastructure are real |
| Peer-reviewed studies | South Korea design/evaluation, Odisha Rice Crop Manager, Avaaj Otalo, Nuru studies, digital-advisory reviews | Small samples, narrow crops or regions, and limited commercial-status information | **A** - best for mechanism and measured behavior |
| Implementer and donor evaluations | ACRE Zambia, PxD/Ama Krushi, Farm Radio International, Mercy Corps AgriFin | Self-reported reach; counterfactual and unit-cost data often absent | **B** - high operational value, moderate independence |
| Mobile-operator and GSMA case studies | DigiFarm, Airtel Kilimo, Farmers' Club, M'chikumbe, Farmer's Friend | Many are historical; registration is often confused with activity | **B** - strong channel history, weaker current-status evidence |
| Company and platform pages | Viamo, Farmerline, iCow, Arifu, BaKhabar Kissan, M-Omulimisa, iShamba | Marketing totals, undefined "users reached," little failure reporting | **C** - proves an offer exists, not that it works at scale |
| Open-source repositories and hackathons | Chenjezo, AgroFutures, KrishiSakhi, KisanVaani, PocketLLM | Little or no deployment, maintenance, safety, carrier, or outcome evidence | **D** - useful idea inventory only |
| Forums, social posts, aggregators, and keyword results | Leads on WhatsApp groups, startup status, and local names | Name collisions, copied claims, stale pages, SEO lists, no primary evidence | **D** - discovery leads, not citable proof |

The sweep is strongest for South Asia and East/Sub-Saharan Africa, where basic-phone programs are well documented. It is weaker for Latin America, francophone local programs beyond Mali, the Pacific, private carrier contracts, startup closures, and cost per farmer. Absence from this inventory therefore means "not found in the reviewed public evidence," not "does not exist."

## 4. WHAT IS MISSING

### The unclosed product loop

Most systems stop at one of four points: a weather bulletin without a farm profile, a profiled advisory without a hazard trigger, a message without proof it was understood, or an alert without post-disaster follow-up. Even the closest precedent in South Korea focuses on forecast, warning, and response guidance; the public evidence reviewed here does not establish a full loop of farmer acknowledgement, action verification, damage assessment, recovery recommendation, and measured loss avoided. BAMIS exposes many relevant hazards, but public evidence does not establish individualized plots and closed-loop recovery at scale [8].

The largest white space is therefore **assurance**, not generation: Was the message delivered? Was the voice call heard to completion? Did the farmer understand the local term for storm surge, lodging, drainage, or salinity? Was the action feasible given labor, credit, livestock, and harvest timing? What happened afterward? ACRE's results show why these questions matter: a technically correct campaign still lost messages to network and number failures, arrived late for some recipients, and left some users unable to understand cyclone or weather content [26].

### Missing evidence and economics

No reviewed source supplied a standardized, comparable **cost per farmer successfully warned**, **cost per completed action**, or **crop loss avoided per rupee** across SMS, IVR, USSD, radio, and app delivery. Public totals frequently count registered profiles, cumulative messages, calls, or people reached. DigiFarm's own distinction between more than 1M registrations and 30% activity shows why those totals cannot be treated as adoption [31].

Rigorous comprehension and outcome evidence is also thin. Farm Radio reports very large listening and action totals, but these are program monitoring figures rather than a universal causal estimate [23]. Nuru reports encouraging examples, including a large gain for one farmer, but that is not a population effect [22]. The Korea study offers the clearest user ratings, while Odisha's Rice Crop Manager research supports repeated telephone reminders but does not by itself prove disaster-loss reduction [99][35].

### Missing institutional integration

No public source in the sweep showed one production system spanning all of IMD/WINDS, OSDMA, Odisha's farmer registry, crop-stage data, district agronomists, telecom delivery receipts, community radio, CSC/extension offline workflows, crop-insurance claims, and recovery finance. Each component exists separately: WINDS is intended to expose hyperlocal data through standard APIs [101], and OSDMA already disseminates warnings by message, voice, siren, satellite, and radio-linked infrastructure [102]. The opportunity is to connect them without creating a parallel warning authority.

**Decision-ready insight:** KrishiSetu should make a narrow promise - verified translation of an official warning into feasible farm actions and a measured recovery loop - and build the evaluation framework before expanding features.

## 5. LESSONS

### South Korea and BAMIS: prior art is strong, but last-mile assurance is weak

South Korea is the clearest technical collision. A farmer registers location, crop, and variety; the system combines those records with high-resolution weather and crop-stage logic; warnings and response information reach mobile web and text [35]. The mechanism is sound: the same wind or temperature forecast has different consequences for different crops and growth stages. User ratings above 4/5 indicate perceived usefulness, although the published implementation also reports limited server power [35].

BAMIS proves that a national lower-income setting can expose crop advisories around cyclone, flash flood, river flood, heat, salinity, and storms [8]. Its public advice includes actions such as using cyclone shelters, harvesting where appropriate, avoiding planting or agrochemical application, improving drainage, and protecting against strong winds [36]. What public evidence does not show is reliable farm-level voice personalization, acknowledgement, or outcome attribution.

**Recommendation:** Borrow the Korea profile and crop-stage model, the BAMIS multi-hazard taxonomy, and Odisha's own warning authority. Differentiate through voice, feasibility filters, acknowledgement, and recovery evidence.

### ACRE Zambia: a sent message is not a delivered warning

ACRE's report is unusually valuable because it records failure. About **153,312** phone records were correctly captured, but the campaign's reported delivery success was **56%**; inactive numbers and network problems caused failures [26]. Some respondents did not understand weather or cyclone content, and some agroecological-zone advice arrived too late [26].

The mechanism is operational rather than algorithmic: agricultural value decays quickly after a warning window closes. A perfect recommendation delivered after harvest, or to an inactive shared phone, has zero preventive value. Low literacy also makes "delivered" an inadequate success event.

**Recommendation:** Implement automated retries across time windows, IVR fallback after SMS failure, alternate household contacts with consent, a toll-free replay number, one-key comprehension checks, and escalation to village workers. The service dashboard should separate generated, queued, sent, delivered, answered, heard, understood, committed, and completed.

### Ama Krushi and Rice Crop Manager: build on Odisha's installed trust

Ama Krushi already established a customized two-way advisory concept for Odisha smallholders [73]. Rice Crop Manager compared printed CSC delivery with telephone advice followed by periodic calls and reminders, and the telephonic repeated-contact mode was more effective for adoption than one-time interaction [99]. This means an entry claiming "voice advice for Odisha farmers" is not differentiated.

The causal mechanism is repetition plus trusted local context. A pre-cyclone sequence might require one call at 72 hours, a shorter reminder at 24 hours, a final safety message, and a post-event damage and recovery call. A single long AI-generated call is less likely to be remembered or acted upon.

**Recommendation:** Use existing content reviewers, district agronomists, CSCs, and farmer records where legally and operationally possible. Position KrishiSetu as the hazard orchestration and assurance module within that ecosystem, not a replacement brand competing for farmer attention.

### 8028, Viamo, Uliza, and radio: voice-first with broadcast redundancy

Ethiopia's 8028 demonstrates enormous demand for toll-free agricultural voice, with more than **6M subscribers and 60M calls** reported [40]. Viamo shows that IVR/SMS operations can span 20 countries and 70 languages [78]. Uliza adds a particularly relevant mechanism: a farmer places a free missed call and receives an IVR callback, avoiding airtime cost [37]. Radio then covers households with shared phones, weak registration, or damaged networks; Farm Radio's FY2022-23 figures indicate 24.1M listeners and 4.8M people taking action [23].

Each channel has a different trade-off. Outbound IVR is targeted and measurable but costs more and can congest. SMS is cheap and persistent but weak for low literacy. USSD is cheap and interactive but requires the user to initiate and navigate within a session. Radio is resilient and trusted but cannot easily personalize or prove who acted.

**Recommendation:** Use a cascade, not a winner-take-all channel: priority outbound IVR in Odia and selected local languages; SMS action checklist; missed-call replay; shallow USSD for status and help; interactive radio for district-level redundancy; and a human extension queue for high-risk exceptions.

### DigiFarm and iCow: engagement design matters more than registration

DigiFarm reports more than **1M registrations**, but only **30% activity** [31]. iCow's calendar and farm-data pattern turns broad husbandry knowledge into small, timed actions on basic phones [44]. Together they expose a critical distinction: a database entry is not an engaged farmer, but a well-timed micro-action can create repeated utility.

The same design should govern disaster advice. Instead of reading a general cyclone bulletin, send the few actions relevant to that crop stage, plot risk, and time window. Recovery should likewise be sequenced: immediate safety and drainage first, then disease surveillance, replanting or salvage, documentation for claims, and market or credit support.

**Recommendation:** Optimize for completed micro-actions. Report monthly reachable profiles, answered calls, listen-through, correct comprehension response, confirmed action, and verified outcome separately.

### Nuru, ODK, CommCare, and CHT: offline belongs with intermediaries

Nuru shows that offline diagnosis can work on a smartphone in field conditions [22]. ODK and CommCare demonstrate delayed synchronization at global scale [34][32]. The Community Health Toolkit is even closer architecturally: it joins SMS-accessible households to offline frontline-worker apps and national systems [13].

These systems do not justify putting a large language model on a farmer's basic phone. They support a split architecture: deterministic, pre-approved safety messages on the server and phone network; richer offline decision support on an extension worker's Android device; and store-and-forward damage records when connectivity returns.

**Recommendation:** Keep generative AI behind agronomic policy, retrieval, and approval. During severe alerts, use versioned playbooks and deterministic templates. Let AI help summarize profiles, translate approved content, prioritize cases, and assist extension workers, but never improvise an unreviewed life- or crop-critical instruction.

### What failed, and what is merely unverified

The sweep did **not** substantiate the premise that iCow is dead; a live site and current service description remain visible. It also did not establish a documented shutdown cause for M-Farm or the original WeFarm SMS network. M-Farm's current operation is unresolved, while WeFarm has a visible web community but no verified continuity of its original SMS network [84]. e-Krishok, Farmer's Friend, Airtel Kilimo, Farmers' Club, M'chikumbe, and Sandji have credible historical records but insufficient current evidence.

It would be dishonest to invent company-specific causes. The evidence does, however, reveal recurring failure mechanisms: invalid or shared phone records, network nondelivery, late content, misunderstanding, the gap between registration and activity, expensive human answer queues, app and data dependence, institutional handoff, and weak recurring-revenue evidence. These mechanisms should be treated as risks, not asserted as the documented cause of any particular startup's decline.

## 6. REAL-vs-FILLER

| Classification | Entries | Evidence-based interpretation |
|---|---|---|
| **Real and operational or visibly live** | South Korea EWS, BAMIS portal, OSDMA EWDS, IMD/WINDS, Ama Krushi lineage, M-Omulimisa, BaKhabar Kissan, Farmerline, iCow, Viamo, Farm Radio/Uliza, 8028, DigiFarm, iShamba, ODK, CommCare, CHT, DeHaat, Jiva | A government page, current platform, implementation report, or operational interface exists. This proves reality, not independently audited impact. |
| **Real, measured, but bounded** | ACRE Zambia campaign, Rice Crop Manager evaluation, Avaaj Otalo field work, Nuru field deployment | Useful evidence on delivery, adoption, interaction, or field operation; do not generalize beyond reported setting and sample. |
| **Real historical, current status unclear** | Original WeFarm SMS, M-Farm, Farmer's Friend, e-Krishok, Sandji, Airtel Kilimo, Farmers' Club, M'chikumbe | Keep as prior art. Label historical or unresolved rather than "live" or "dead." |
| **Marketing-supported, scale needs qualification** | iCow's cumulative reach/SMS, Farmerline's farmers reached, BaKhabar Kissan's service users, Viamo subscriber and engagement totals, company outcome pages | The services appear real, but cumulative reach, registrations, subscribers, calls, and active users measure different things. |
| **Prototype or research idea** | Chenjezo, AgroFutures, KrishiSakhi, KisanVaani, PocketLLM, generic WhatsApp bots | Relevant to novelty of the idea; irrelevant to proof of deployment, reliability, adoption, or impact. |
| **Misclassified analogue** | Jaza Duka | Real merchant credit system, not a hazard-advisory service. It informs recovery finance only. |
| **Unverified or filler** | G-Barn as a Nigerian ag-advisory platform, a Freshokartz WhatsApp advisory claim, "AgroDealer" as one identifiable global service, MobiLLM as a specific field system, anonymous offline-app portfolios | No sufficiently specific, credible deployment evidence emerged. Exclude from the differentiation claim and main competitor map. |

The appropriate diligence standard is not "has a website." A strong analogue needs an identifiable operator, operational channel, target population, dated evidence, and at least one concrete measure of reach, use, delivery, comprehension, action, outcome, or cost.

## 7. NOISE LOG

| Search lead discarded or downgraded | Why it was noise or insufficient | Disposition |
|---|---|---|
| G-Barn Nigeria | Searches returned unrelated barns, grants, Nigerian agritech lists, and generic agriculture pages; no stable operator or deployed service matched the claimed description | Exclude; retain only as an unverified lead |
| Farmer's Friend Nigeria | Credible evidence points to the AppLab service in **Uganda**, not Nigeria [41] | Correct geography; classify historical |
| Freshokartz as a WhatsApp advisory | Evidence supported an agricultural/VLE business, but not the specific WhatsApp advisory and disaster-delivery claim | Do not cite for WhatsApp prior art |
| Jiva or AgroDealer WhatsApp claims | Jiva's app, field partner, finance, commerce, and agronomy functions are real [16], but the searched sources did not establish the requested WhatsApp warning mechanism; "AgroDealer" was not one unique system | Keep Jiva as indirect; discard unsupported channel claim |
| Jaza Duka as USSD farm advice | Primary description is merchant inventory credit, not agronomic advice [67] | Keep only under recovery finance |
| DigiFarm name collision | Searches also surfaced unrelated U.S. precision/RTK firms and generic projects | Use Safaricom/Mercy Corps AgriFin context only |
| WeFarm name collisions | Results included unrelated farming businesses and communities in other countries | Use the Kenya-origin peer network/current Wefarm domain only |
| M-Farm status snippets | Aggregators and stale profiles could not establish current operations or closure | Mark status unresolved |
| "iCow decline" or death premise | A current site remained visible; no authoritative closure evidence was found | Reject death claim; qualify marketing scale |
| Generic Devpost and hackathon lists | Many agriculture chatbots repeated weather, disease, price, and alert features without users or field deployment | Ideas-only, not competitors |
| Anonymous vendor case studies | Claimed offline apps and farmer totals without a named client, methods, or independent evidence | Marketing filler |
| PocketLLM/MobiLLM search collisions | Papers and labels concerned mobile language models, not deployed feature-phone agricultural warning systems | Research context only |
| Forums and social posts | Useful for names and failure anecdotes but poor for dates, identity, causality, and scale | Lead generation only; no material claim based solely on them |
| Latin America and Pacific queries | No strong direct basic-phone, farm-profiled disaster advisory emerged in the reviewed public English-language evidence | Record as a coverage gap, not proof of absence |

## 8. VERDICT

### The honest differentiation claim

KrishiSetu is **not** the first agricultural SMS service, IVR service, USSD service, weather advisory, hyperlocal farm-data platform, crop-stage warning system, AI farm assistant, offline agricultural app, or pre-disaster advisory. South Korea's system is particularly close to the farm profile plus hazard plus action logic [35]. BAMIS covers the relevant hazard family in a comparable South Asian setting [8]. Odisha already has voice-advisory and public-warning assets [99][102].

A defensible claim is:

> **KrishiSetu is an Odisha-specific resilience orchestration and assurance layer that converts official IMD, WINDS, and OSDMA signals plus farm and crop-stage profiles into agronomist-governed pre-event and post-event action sequences, then delivers them through a redundant basic-phone-first cascade with acknowledgement, comprehension, offline field follow-up, and recovery-outcome measurement.**

This wording should remain a **differentiation claim**, not an absolute "world first." The sweep found no public evidence of another system implementing every part of that exact institutional and measurement chain, but private systems and under-documented regional programs may exist.

### Best-fit delivery pattern for Odisha basic-phone reality

The recommended pattern is a **voice-first, multi-channel, closed-loop cascade**:

1. **Authoritative trigger**: ingest signed IMD/OSDMA alerts and WINDS observations; deduplicate and geofence them.
2. **Deterministic farm translation**: combine village/plot, crop, variety, growth stage, irrigation, livestock, storage, and household constraints with approved agronomic playbooks.
3. **Priority outbound IVR**: call in Odia and selected local languages; put the most urgent action first; keep each call short; allow replay.
4. **SMS receipt**: send a compact numbered checklist and helpline reference for literate users and shared-family review.
5. **Toll-free missed-call callback**: copy Uliza's zero-airtime pull pattern for replay and questions [37].
6. **USSD status and acknowledgement**: use a shallow menu for "heard," "need help," "action impossible," and recovery reporting; M-Omulimisa confirms the basic-phone interaction pattern [47].
7. **Radio and public-warning redundancy**: issue district-level synchronized radio scripts and use OSDMA's message/voice/siren reach when phone delivery degrades [102].
8. **Offline extension workflow**: use ODK/CommCare/CHT patterns for cached farmer lists, door-to-door exceptions, geo-tagged damage, and delayed synchronization [34][32][13].
9. **Closed-loop metrics**: track generated, sent, delivered, answered, listen-through, comprehension, action, exception, damage, recovery, and loss avoided. Never report registrations as impact.

### Synthesis across mechanisms, scope, evidence, and trade-offs

| Strategy | Core mechanism | Best scope | Main trade-off | Evidence base | Time horizon |
|---|---|---|---|---|---|
| South Korea farm EWS | Fine-grained farm and crop-stage risk translation | Personalized prevention | Data, compute, and registration complexity; text/web accessibility | Operational study plus user ratings [35] | Hours to days before event |
| BAMIS | National agro-meteorological and multi-hazard advisory | Broad official guidance | Limited public proof of individual delivery and action | Government portal and project records [25][8] | Seasonal through immediate warning |
| ACRE SMS | Zone-tailored outbound messages | Rapid campaign delivery | Nondelivery, late timing, and comprehension failure | Operational delivery evaluation [26] | Days to weeks |
| 8028/Viamo/Uliza | Toll-free voice, outbound IVR, callback, and profiling | Low-literacy interaction at scale | Telephony cost, menu design, and answer capacity | Large implementer-reported usage [40][78][37] | Immediate plus repeated support |
| Farm Radio | Trusted broadcast plus call-in/mobile participation | Population-wide redundancy | Weak personalization and attribution | Large monitoring totals [23] | Immediate and campaign-long |
| DigiFarm/iCow | Profile, calendar, finance, and recurring micro-actions | Long-term engagement and recovery | Registrations overstate activity; business-model dependence | Program and company records [44][31] | Season-long |
| Nuru/ODK/CommCare/CHT | Offline local computation and store-and-forward field records | Extension and damage assessment | Requires a smartphone-equipped intermediary | Documented deployments at meaningful scale [34][32][13] | During outage and recovery |

The non-obvious conclusion is that the strongest system is not one channel or one model. Korea supplies the personalization logic, BAMIS the hazard taxonomy, ACRE the failure evidence, 8028/Viamo/Uliza the voice mechanics, Farm Radio the redundancy, Ama Krushi the local trust channel, and ODK/CommCare/CHT the offline recovery workflow. KrishiSetu becomes meaningfully different only when it integrates those mechanisms under Odisha's official institutions and proves that farmers received, understood, and completed the right action before and after a cyclone or flood.

## References

1. *Redirecting to https://www.farmersfriend.co.uk/*. https://www.farmersfriend.co.uk/node/1
2. *Guardian Agriculture Failure Analysis: $35M Lost — What Went Wrong | IdeaProof*. https://ideaproof.io/failure/guardian-agriculture
3. *agrojournal.org*. https://agrojournal.org/28/03-02.pdf
4. *Business Model Innovation in Agri-Businesses: Strategies and Barriers - Agriculture Notes by Agriculture.Institute*. https://agriculture.institute/agripreneurship/business-model-innovation-agribusiness-strategies-barriers
5. *Learning technologies for adult literacy: a scoping review and analysis of the current state of evidence | Educational technology research and development | Springer Nature Link*. https://link.springer.com/article/10.1007/s11423-023-10270-9
6. *Farmers Friend | Greenhouses, Tunnels, Farm Tools & Farming Supplies*. https://www.farmersfriend.com/
7. *MobileFineTuner: A Mobile-Native Framework for On-Device LLM Fine-Tuning in Real-World Embedded AI Applications*. https://arxiv.org/abs/2512.08211
8. *Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en
9. *Annual Report 2024-25 - Farm Radio International*. http://farmradio.org/publications/annual-report-2024-25
10. *Agriculture - Viamo*. https://viamo.io/category/agriculture
11. *BaKhabar Kissan | Pakistan's Largest AgriTech & Digital Agriculture Platform*. https://bkk.ag/
12. *Gsma Orgs*. https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/gsma_orgs/esoko
13. *Why the Community Health Toolkit? – Community Health Toolkit*. https://docs.communityhealthtoolkit.org/why-the-cht
14. *Farm Radio International*. https://farmradio.org/
15. *8028 Farmer Hotline - Agricultural Transformation Institute*. https://ati.gov.et/8028-farmer-hotline
16. *Jiva Agtech*. https://sg.linkedin.com/company/jiva-agtech
17. *Farmerline – Farmerline*. https://farmerline.co/
18. *Nigeria launches AI-powered digital agricultural advisory project for millions of smallholder farmers | News*. https://www.capmad.com/post/nigeria-launches-ai-powered-digital-agricultural-advisory-project-for-millions-of-smallholder-farmers
19. *Supporting smallholder farmer resilience with weather advisory information*. https://cgspace.cgiar.org/items/05bae0a1-85b9-4599-a5e8-1f5e47c02c5a
20. *M-Omulimisa - Digital Agriculture Services*. https://platform.m-omulimisa.com/
21. *Reforming Agricultural Extension and Advisory Services in Nigeria: A Strategic Review for Sustainable Agricultural Development – International Journal of Research and Innovation in Social Science*. https://rsisinternational.org/journals/ijriss/articles/reforming-agricultural-extension-and-advisory-services-in-nigeria-a-strategic-review-for-sustainable-agricultural-development
22. *PlantVillage Nuru: Pest and disease monitoring using AI - CGIAR Platform for Big Data in Agriculture*. https://bigdata.cgiar.org/digital-intervention/plantvillage-nuru-pest-and-disease-monitoring-using-ai
23. *Measuring our impact*. https://farmradio.org/measuring-our-impact
24. *GitHub - grafikinc/ai-ussd-2g-feature-phone: A USSD and voice interface for delivering AI-generated intelligence to any phone manufactured in the last 25 years. User dials a shortcode. System generates a personalized advisory from live data. Calls them back with it spoken in their language. Zero data cost. Zero literacy requirement. 4 languages live. Agriculture is the first vertical. · GitHub*. https://github.com/grafikinc/ai-ussd-2g-feature-phone
25. *Background - Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en/page/introduction
26. *cgspace.cgiar.org*. https://cgspace.cgiar.org/bitstreams/b2a0e20f-97c7-44de-8b30-e6db71219a89/download
27. *Winich Farms Agritech Nigeria*. https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/blog/winich-farms-agritech-nigeria
28. *GitHub - Walunji-Zdev05/Chenjezo-Drought-Flood-Alert: Drought & Flood Early Warning System with SMS Alerts for Smallholder Farmers in Malawi.  An  open-source web application providing real-time district-level climate risk maps and automated SMS warnings using free NASA weather data. Empowering rural communities to adapt to droughts and floods amid Malawi's 2025 climate crisis. · GitHub*. https://github.com/Walunji-Zdev05/Chenjezo-Drought-Flood-Alert
29. *Chatbot | Weather Impact*. https://www.weatherimpact.com/chatbot
30. *PlantVillage*. https://plantvillage.psu.edu/
31. *Safaricom Digifarm - CGIAR Platform for Big Data in Agriculture*. https://bigdata.cgiar.org/digital-intervention/safaricom-digifarm
32. *ODK - Collect data anywhere*. https://getodk.org/
33. *Program Overview – Mercycorps Agrifin*. https://mercycorpsagrifin.org/program-overview
34. *The Digital Platform for Frontline Success | CommCare*. https://dimagi.com/commcare
35. *Establishment and Operation of an Early Warning Service for Agrometeorological Disasters Customized for Farmers and Extension Workers at Metropolitan-Scale*. https://www.mdpi.com/2073-4433/16/3/291
36. *Bangladesh Agro-Meteorological Information Service (BAMIS)*. https://www.bamis.gov.bd/en/alert/nation/
37. *Uliza Services - Farm Radio International*. https://farmradio.org/uliza-services
38. *Digital training benefits farmers and agricultural institutions - Arifu*. https://arifu.com/digital-training-benefits-farmers-and-agricultural-institutions
39. *Our work in Uganda - Farm Radio International*. https://farmradio.org/uganda
40. *Now - Agricultural Transformation Institute*. http://ati.gov.et/timelines/1457
41. [AppLab -- an Initiative of the Grameen Foundation [Agriculture]](https://www.applab.org/section/uganda-ag-apps.html)
42. *GitHub - Adityaraj1904/KrishiSakhi: 🌱 + 🤖 | AI-powered farming assistant | Personalized crop advice, disease detection, chatbot & smart alerts (SIH 2025). · GitHub*. https://github.com/Adityaraj1904/KrishiSakhi
43. *cgspace.cgiar.org*. https://cgspace.cgiar.org/bitstreams/315049cd-588f-490e-a3d0-787efe3aaded/download
44. *iCow – iCow Kenya home*. https://icow.co.ke/
45. *Digital Agricultural Advisory Services (DAAS) – Advancing productivity for Ethiopian smallholder farmers – Precision Development (PxD)*. https://precisiondev.org/project/digital-agricultural-advisory-services-daas-advancing-livestock-productivity-for-ethiopian-smallholder-farmers
46. *rjwave.org*. https://rjwave.org/jaafr/papers/JAAFR26A3132.pdf
47. *M-Omulimisa - Innovative Agricultural Services*. https://m-omulimisa.com/
48. *GitHub - RDRishabh/kisan-vaani · GitHub*. https://github.com/RDRishabh/kisan-vaani
49. *Robot Challenge Screen*. https://4returns.commonland.com/toolbox/wefarm
50. *60 Decibels — Impact Measurement*. https://60decibels.com/
51. *Mastercard Expands its Jaza Duka Program | CIO Africa*. https://cioafrica.co/mastercard-expands-its-jaza-duka-micro-credit-program/
52. *iShamba*. https://ishamba.com/about
53. *The Viamo Platform | Reach Millions with Your Message*. https://viamo.io/services/viamo-platform
54. *Sustainable agri-radio programming: Reaching farmers with information about climate-resilient agriculture*. https://farmradio.org/reaching-farmers-with-information-about-climate-resilient-agriculture/
55. *Mfarmer Case Studies*. https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/gsma_resources/mfarmer-case-studies/
56. *Chi Talk Patel 4.0*. https://hci.stanford.edu/publications/2010/avaajotalo/chi_talk_patel_4.0.pdf
57. *60Db Arifu*. https://www.mercycorpsagrifin.org/wp-content/uploads/2021/02/60dB-Arifu.pdf
58. *Providing push-based agricultural advisory through IVRS calls to all farmers of Odisha  | CaseStudy*. https://samagragovernance.in/amritseries/krushi-samruddhi-helpline
59. *Mastercard and Unilever Target Micro Entrepreneurs with New Digital Lending Platform - Payments Afrika*. https://paymentsafrika.com/mastercard-and-unilever-break-down-barriers-to-growth-for-micro-entrepreneurs-with-first-of-its-kind-digital-lending-platform/
60. *GFRAS - #18 Using Radio in Agricultural Extension *. https://www.g-fras.org/en/good-practice-notes/using-radio-in-agricultural-extension.html?showall=1
61. [
        mKisan: A Portal of Government of State Base Services for Farmer centre Mobile Services
    ](https://mkisan.gov.in/Home/AboutPushSMS)
62. *Unilever, KCB and Mastercard to Support Cash-Strapped Retailers | The Kenyan Wallstreet*. https://kenyanwallstreet.com/unilever-will-provide-the-products-to-shops
63. *AGROMET ADVISORY SERVICES | India Meteorological Department*. https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php
64. *M-Farm - 2026 Company Profile, Team, Funding & Competitors - Tracxn*. https://tracxn.com/d/companies/mfarm/__FlWboiopTER-pAhvgI48kka9UT-TDiD1MudaJQKxH-c
65. [
        mKisan: A Portal of Government of State Base Services for Farmer centre Mobile Services
    ](https://mkisan.gov.in/)
66. *Impact - Arifu*. https://arifu.com/impact
67. *Home | Mastercard Newsroom*. https://newsroom.mastercard.com/news/press/2018/mastercard-and-unilever-break-down-barriers-to-growth-for-micro-entrepreneurs-with-first-of-its-kind-digital-lending-platform/
68. *WeFarm Food Company Profile & Overview*. https://internshala.com/company/wefarm-food-1782977136
69. *Realizing the potential of digital development: The case of agricultural advice | Science*. https://www.science.org/doi/10.1126/science.aay3038
70. *Impact of text messages on farmers' adoption of agriculture app and its effect on farm level outcomes - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2214804326000650
71. *Avaaj Otalo — A Field Study of an Interactive Voice Forum for Small Farmers in Rural India*. https://tap2k.org/papers/pap0310-patel.pdf
72. *Phone-based technology for agricultural information delivery | The Abdul Latif Jameel Poverty Action Lab*. https://www.povertyactionlab.org/case-study/phone-based-technology-agricultural-information-delivery
73. *Ama Krushi Transition Insights Report*. https://precisiondev.org/wp-content/uploads/2025/02/AK-transition-report-BMGF_condensed.pdf
74. *The evolving financial ecosystem for micro merchants: Enabling micro credit programs through digital solutions - Mastercard Newsroom | Mastercard US*. https://www.mastercard.com/us/en/news-and-trends/stories/2023/whats-in-stock-for-micro-merchants.html
75. *WeFarm - Wikipedia*. https://en.wikipedia.org/wiki/WeFarm
76. *A systematic review of mobile agricultural service applications for smallholder farmers in sub-Saharan Africa: perspectives from the technology acceptance model | Agriculture & Food Security | Springer Nature Link*. https://link.springer.com/article/10.1186/s40066-025-00563-y
77. *Avaaj Otalo | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. https://dl.acm.org/doi/10.1145/1753326.1753434
78. *#Viamo - Digital Made Easy*. https://viamo.io/
79. *iShamba*. https://ishamba.com/
80. *Ama Krushi Transition Insights Report*. https://precisiondev.org/wp-content/uploads/2025/04/AK-Transition-Insights-2025_condensed.pdf
81. *Creating Scalable Engaging Mobile Solutions For Agriculture*. https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/gsma_resources/creating-scalable-engaging-mobile-solutions-for-agriculture/
82. *dl.acm.org*. https://dl.acm.org/doi/pdf/10.1145/1753326.1753434
83. *Ama Krushi – Scaling advisory services to millions of farmers in Odisha, India – Precision Development (PxD)*. https://precisiondev.org/project/ama-krushi
84. *join.wefarm.com*. https://join.wefarm.com/
85. *(PDF) A systematic review of mobile agricultural service applications for smallholder farmers in sub-Saharan Africa: perspectives from the technology acceptance model*. https://www.researchgate.net/publication/398495832_A_systematic_review_of_mobile_agricultural_service_applications_for_smallholder_farmers_in_sub-Saharan_Africa_perspectives_from_the_technology_acceptance_model
86. *The impact of interactive radio*. https://farmradio.org/wp-content/uploads/2024/12/Evidence-brief-final.pdf
87. *Mercycorps Agrifin*. https://mercycorpsagrifin.org/
88. *A systematic review of mobile agricultural service applications for smallholder farmers in sub-Saharan Africa: perspectives from the technology acceptance model | Semantic Scholar*. https://www.semanticscholar.org/paper/A-systematic-review-of-mobile-agricultural-service-Muromba-Keeni/578c04c1109ce00128db649cbc1705a713320487
89. *Creating scalable, engaging mobile solutions for agriculture | e-Agriculture | Food and Agriculture Organization of the United Nations*. https://www.fao.org/e-agriculture/content/creating-scalable-engaging-mobile-solutions-agriculture
90. *Sustainable agri-radio programming: Reaching farmers with information about climate-resilient agriculture - Winrock International*. https://winrock.org/sustainable-agri-radio-programming-reaching-farmers-with-information-about-climate-resilient-agriculture/
91. *New & upcoming hackathons · Devpost*. https://devpost.com/hackathons
92. *Paper 15 Williams P G Whatsapp*. https://fuwjss.com/wp-content/uploads/2025/08/Paper-15-Williams-P-G-Whatsapp.pdf
93. *Farmers Weather | Weather Checker | Farmers Guide*. https://www.farmersguide.co.uk/weather
94. *Devpost - The home for hackathons*. https://devpost.com/
95. *Offline Mobile App Case Study | Brainstack Technologies*. https://www.brainstacktechnologies.com/case-study/offline-app
96. *devpost-hackathon · GitHub Topics · GitHub*. https://github.com/topics/devpost-hackathon
97. *epubs.icar.org.in*. https://epubs.icar.org.in/index.php/IJAgS/article/download/87605/35705/224542
98. *🌦️ Farm Weather & Agromet Advisory*. https://www.farmer.in/weather
99. *http://frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2026.1701246/full*. http://frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2026.1701246/full
100. *http://cgspace.cgiar.org/items/45b79d15-2bc1-44b0-afb9-279a15f3234f*. http://cgspace.cgiar.org/items/45b79d15-2bc1-44b0-afb9-279a15f3234f
101. *http://pmfby.amnex.co.in/pmfby/pdf/operational_guidelines_pmfby.pdf*. http://pmfby.amnex.co.in/pmfby/pdf/operational_guidelines_pmfby.pdf
102. *http://osdma.org/preparedness/early-warning-communications/ewds*. http://osdma.org/preparedness/early-warning-communications/ewds
103. *Fetched web page*. http://itu.int/net/WSIS/implementation/2013/forum/agenda/session_docs/86/Panelist1_BIID_Workshop_WSIS.pdf
104. *http://agrevolution.in/solution-for-farmers*. http://agrevolution.in/solution-for-farmers
