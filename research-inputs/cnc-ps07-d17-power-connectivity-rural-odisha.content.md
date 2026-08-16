# KrishiSetu Offline-First Infrastructure Reality for Coastal Odisha

## 1. EXECUTIVE SUMMARY

- **No defensible district 2G/3G/4G matrix exists in the public evidence reviewed.** Opensignal exposes measurement-based coverage maps and a national June 2025 report, but the retrieved material does not publish downloadable Odisha district figures by radio generation [2][5]. A March 2026 report says **1,237 Odisha villages had no mobile-network coverage**, with Rayagada highest at 145, but it gives neither the coastal-district breakdown nor separate 2G, 3G, and 4G counts [6]. Treat every pilot village as unverified until multi-operator drive and stationary tests are completed.

- **A cyclone can remove both the access network and its dependencies.** During Fani, Cuttack, Khordha, Bhubaneswar, and Puri experienced complete shutdowns of power and telecommunications; nine days after landfall, Odisha's situation was still described as fluid because communications, roads, and electricity had broken down [28]. SMS/IVR must therefore be front-loaded before landfall and cannot be the only post-landfall path.

- **Dana confirms that this is a coastal-block problem, not merely a statewide average.** The assessment found all telephone and cell-phone services down in Rajnagar and Chandabali blocks, with major impacts in Satabhaya, Talachua, Dosinga, and Jagula; damaged towers, poles, substations, transmission lines, and inundated roads failed together [12]. KrishiSetu needs local caching and store-and-forward behavior at the village tier.

- **Normal-year electricity statistics hide disaster tails.** The Ministry of Power reports **23.4 hours/day** of average rural supply in Odisha in FY2023-24 [27], while NFHS-5 reports electricity in **95.8% of rural households** [1]. Neither figure measures cyclone continuity. Size the system for **96 hours at full function plus degraded survival through day 9**, rather than for the 0.6-hour average daily gap.

- **Phone reach is high, but Internet and smartphone readiness are not equivalent.** NFHS-5 reports a mobile phone in **86.9% of rural households** but Internet access in only **30.9%** [1]. These are household indicators, not unique farmer ownership, smartphone share, literacy, affordability, signal quality, or charging availability. SMS plus Odia IVR remains statement-faithful; an app must stay optional.

- **Solar is viable, but only partial price evidence is public.** An Odisha policy document states average solar radiation of **5.5 kWh/m2/day** and about **300 clear days per year** [25]. A current seller page lists 12 V panels at **INR 1,000 for 10 W** and **INR 1,500 for 20 W** [29]. Battery, controller, enclosure, mast, installation, and maintenance costs still require local quotations.

- **Fallback channels are not interchangeable.** The Kerala-flood example involved **300 ham operators** helping trace stranded people and pass information to officials [22], which demonstrates responder communications, not mass farmer delivery. Cell broadcast is one-to-many and geo-targeted in concept [8], but India's service was reported temporarily suspended following an NDMA advisory on June 16, 2026, with no resumption date in the retrieved evidence [31]. Neither should be a prototype dependency.

- **Decision:** **Prototype GO; limited field trial PARTIAL; operational coastal pilot GATED.** The architecture, offline queue, local advisory cache, solar node, SMS, and IVR can be demonstrated now. Deployment claims must wait for village RF measurements, measured outage distributions, verified device mix, local solar quotations, and operator/IVR failover tests.

## 2. DATA INVENTORY

**Reliability grades:** A = primary government, official survey, or direct incident report; B = credible institutional source with a scope limitation; C = secondary, vendor, or incomplete evidence; D = missing or unsuitable for a deployment claim.

| Item / sub-question | Named source, URL, and date | Specification found | Prototype or pilot feasibility | Grade |
|---|---|---|---|---|
| Coastal district 2G/3G/4G availability | Opensignal Coverage Maps, `https://insights.opensignal.com/coverage-maps`, current page; India Mobile Network Experience, `https://insights.opensignal.com/reports/2025/06/india/mobile-network-experience`, June 2025 | Maps are measurement-based, but the retrieved sources provide no district-by-RAT table or downloadable Odisha figures [2][5] | Prototype: use simulated profiles. Pilot: mandatory RF survey with Jio, Airtel, Vi, and BSNL SIMs | D for district matrix |
| Villages with no network | Times of India report, `https://timesofindia.indiatimes.com/city/bhubaneswar/no-mobile-network-in-states-1237-villages-mahaling/articleshow/129353681.cms`, March 10, 2026 | 1,237 Odisha villages without mobile-network coverage; Rayagada highest at 145; no coastal breakdown and no RAT split [6] | Useful only as proof that nominal statewide coverage is incomplete | C |
| 4G expansion | USOF/DBN 4G Saturation Project, `https://usof.gov.in/en/saturation-of-4g-mobile-services`, approved July 27, 2022 | National project approved at INR 26,316 crore [7]; retrieved page does not establish which coastal villages are live today | Track project status, but do not count a planned tower as working coverage | B for scheme; D for village status |
| Fani communication and power failure | UNICEF Fani Situation Report, `https://www.unicef.org/media/82111/file/India-Cyclone-Fani-SitRep-12-May-2019.pdf`, May 12, 2019 | Complete power and telecom shutdown in named locations; disruption remained consequential nine days after landfall [28] | Direct basis for offline design envelope | A |
| Fani pre-landfall mobile warning | Same UNICEF report, May 12, 2019 | Location-based SMS alerts and suggested actions reached 18M subscribers in likely affected areas [28] | Strong evidence for sending personalized actions before network degradation | A |
| Fani BTS restoration | Times of India, `https://timesofindia.indiatimes.com/india/cyclone-fani-telecom-firms-operationalise-over-900-base-stations-in-odisha-restoration-work-on/articleshow/69184542.cms`, May 2019 | 932 BTSs reportedly operationalized during restoration [11]; no failed-site denominator or full restoration date | Shows restoration activity, not survival probability | C |
| Amphan tower mechanism | ET Telecom, `https://telecom.economictimes.indiatimes.com/news/cyclone-amphan-telcos-infrastructure-providers-rush-to-restore-telecom-network/75867056`, May 2020 | More than 50% of West Bengal tower sites were estimated damaged or affected by interrupted power [18] | Useful stress analogue, not an Odisha rate | C |
| Amphan backhaul failure | ET Telecom, `https://telecom.economictimes.indiatimes.com/news/amphan-impact-mobile-broadband-normalcy-in-wb/kolkata-only-next-week/75897469`, May 2020 | Power outages and frequent fiber cuts disrupted service [24] | Requires both local power and backhaul-loss states in tests | C |
| Dana coastal outage | YSD Rapid Needs Assessment, `https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf`, fieldwork October 24-28, 2024 | All phone service down in Rajnagar and Chandabali; named Gram Panchayats severely affected; towers, grid assets, and roads damaged [12] | Strong site-selection and failure-mode evidence | B |
| Dana restoration duration | Same assessment | Road communication restored in Kendrapara and Bhadrak while work continued in Balasore, but no exact phone, power, or road outage duration is reported [12] | Duration must be instrumented during the pilot | D for duration |
| Normal rural electricity supply | Ministry of Power, Rajya Sabha Q2709, `https://www.sansad.in/getFile/annex/267/AU2709_g7kjOi.pdf?source=pqars`, March 24, 2025 | Odisha rural average: 23.4 hours/day in FY2023-24 [27] | Baseline for recharge opportunity, not cyclone autonomy | A |
| Household power and phone access | NFHS-5 Odisha, `https://preview.dhsprogram.com/pubs/pdf/fr374/fr374_odisha.pdf`, survey 2019-21 | Rural households: electricity 95.8%, mobile phone 86.9%, Internet 30.9% [1] | Supports SMS/IVR priority and assisted access; too old/coarse for village deployment | A for survey; B for current design |
| Smartphone penetration | ASER 2024 National Findings, `https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-National-findings.pdf`, 2024 | The retrieved material did not provide an Odisha-specific rural smartphone percentage [4] | Do not convert national youth use into farmer ownership | D |
| Basic-phone share and data affordability | NFHS/ASER/TRAI search set, through August 16, 2026 | No current Odisha rural split among feature phones, shared smartphones, and personal smartphones; no Odisha-specific pack-affordability distribution | Add household survey and operator-plan audit before pilot | D |
| Solar resource | Government of Odisha Solar Power Policy copy, `https://www.cbip.org/policies2019/PD_07_Dec_2018_Policies/Orissa/1-Solar/2%20Order%20Odisha-Solar-Power-Policy.pdf`, document date blank | 5.5 kWh/m2/day average radiation and about 300 clear days/year [25] | Adequate for prototype sizing; pilot needs monthly site GHI and shading data | B |
| Small panel price | Loom Solar, `https://www.loomsolar.com/collections/solar-panels`, retrieved August 16, 2026 | 10 W/12 V panel INR 1,000; 20 W/12 V panel INR 1,500 [29] | Indicative retail quote only | C |
| Battery availability | Saurally Solar, `https://saurally.com/product/12ah-12-8v-lfp-lifepo4-battery-pack-with-bms`, retrieved August 16, 2026 | 12.8 V, 12 Ah LiFePO4 pack with BMS; visible extract has no price or stock status [32] | Component class is real; total kit price remains unverified | C |
| Tower battery backup | TRAI/DoT/industry searches through August 16, 2026 | No authoritative per-site battery-autonomy number or cyclone operating distribution found | Never assume a tower lasts 4, 8, 24, or 72 hours; measure operator behavior | D |
| Cell broadcast | ITU Cell Broadcast page, current; NDTV suspension report, `https://www.ndtv.com/india-news/centre-suspends-cell-broadcast-service-temporarily-11641737`, June 16, 2026 | Cell broadcast supports geo-located mass alerts [8], but India's service was reported temporarily suspended after an NDMA advisory [31] | Optional external ingress only; not a committed delivery path | B for capability; C for current status |
| Ham radio | NDTV, `https://www.ndtv.com/india-news/how-300-radio-operators-are-helping-rescue-people-in-flood-hit-kerala-1903973`, August 2018 | 300 operators helped trace stranded people and pass information to officials [22] | Responder bridge requiring trained operators; not farmer-scale SMS/IVR | C |
| Community radio, VSAT, satellite phones | OSDMA, academic, and open-web searches through August 16, 2026 | No sufficiently specific Odisha inventory, availability SLA, cyclone survival result, or named station power record was recovered | Partnership option only after written confirmation and field test | D |

### Coastal district coverage status: what can and cannot be claimed

| Coastal district | 2G baseline | 3G baseline | 4G baseline | Incident evidence recovered | Decision |
|---|---|---|---|---|---|
| Balasore | Not publicly resolved | Not publicly resolved | Not publicly resolved | Dana restoration work continued there after roads in Kendrapara and Bhadrak were restored [12] | RF survey required |
| Bhadrak | Not publicly resolved | Not publicly resolved | Not publicly resolved | Dana damaged communications, power, and roads; Chandabali block lost all phone service [12] | High-priority stress-test district |
| Kendrapara | Not publicly resolved | Not publicly resolved | Not publicly resolved | Rajnagar, Satabhaya, and Talachua had major cellular disruption during Dana [12] | High-priority stress-test district |
| Jagatsinghpur | Not publicly resolved | Not publicly resolved | Not publicly resolved | Listed among severely affected Fani districts, but no RAT table or outage duration [28] | RF and restoration survey required |
| Puri | Not publicly resolved | Not publicly resolved | Not publicly resolved | Complete power and telecom shutdown during Fani; Puri was the worst-hit coastal area [28][10] | High-priority offline test district |
| Ganjam | Not publicly resolved | Not publicly resolved | Not publicly resolved | No usable district coverage or outage statistic recovered | Do not infer from neighboring districts |

This is deliberately an **unknown matrix**, not a zero-coverage matrix. The evidence establishes severe event-level failures in specific districts and blocks; it does not establish normal-day 2G, 3G, or 4G percentages.

### Case study: Fani turns nominal coverage into a nine-day systems problem

Fani made landfall on May 3, 2019, with sustained winds of 175-180 km/h and gusts up to 205 km/h [10]. By the May 12 UNICEF report, Odisha still faced a combined breakdown of communications, roads, and electricity; most areas were described as inaccessible because telecommunications and road connectivity were disrupted [28]. This is a common-cause failure: a tower can be structurally intact yet unavailable because the grid, fiber, fuel route, or repair access has failed.

The same incident also demonstrates what worked before failure. Location-based SMS delivered warnings and suggested actions to 18M subscribers [28]. KrishiSetu should exploit that pre-landfall window, cache the exact advice sent, and avoid promising interactive IVR once towers are down.

### Case study: Dana exposes block-level dependencies

Dana made landfall on October 25, 2024, between Bhitarkanika and Dhamra, and the rapid assessment covered fieldwork from October 24-28 [12]. In Rajnagar and Chandabali, all telephone and cellular service was down; power failures also interrupted piped water, while inundated and damaged roads constrained access [12].

Unlike Fani, the Dana report gives useful named places but no precise outage duration. This makes it suitable for selecting pilot blocks and designing failure injections, but not for deriving a statistical service-level target.

## 3. COVERAGE TABLE

The table reports **useful hits in this research run**, not the total number of documents that exist.

| Source family | Useful hits | Noise or missing fields | Coverage judgment |
|---|---:|---|---|
| TRAI, DoT, USOF/DBN | 1 strong scheme page; several regulator pages | No coastal district 2G/3G/4G availability table; no tower battery duration; project approval is not live service | C |
| Opensignal and operator maps | 2 relevant public pages | National/operator visualization, no retrieved district RAT export, no cyclone survival history [2][5] | C |
| Ookla | 0 deployment-grade hits | No usable Odisha coastal district table recovered | D |
| Ministry of Power and parliamentary data | 1 high-value primary answer | Annual average lacks SAIDI/SAIFI tails, feeder variation, and cyclone restoration distribution | A for baseline; C for resilience |
| NFHS and ASER | 1 high-value Odisha report; 1 national report | Household phone and Internet access are not smartphone ownership, personal control, literacy, or affordability | B |
| UNICEF, OSDMA-linked, and rapid assessments | 2 high-value incident reports | Strong mechanisms and named places; incomplete service-duration and tower-denominator data | A-B |
| Telecom/media incident reporting | 3 useful partial hits | BTS restorations and Amphan tower impacts lack comparable denominators and Odisha-specific timelines | C |
| Odisha solar policy and retail vendors | 1 resource claim; 2 component records | No monthly worst-case GHI, installed kit price, local warranty, or flood survivability | B-C |
| Cell broadcast, ham, radio, VSAT, satellite | 3 partial hits | Current CB suspended; ham is responder-scale; Odisha radio/VSAT/satellite inventories and SLAs missing | C-D |

**Coverage judgment:** the evidence is strong enough to set a conservative architecture, but not to certify a coastal pilot's coverage, uptime, or power SLA.

## 4. WHAT IS MISSING

1. **Village-level RAT truth:** latitude/longitude, operator, SIM, 2G/3G/4G/5G technology, RSRP, RSRQ, SINR, indoor/outdoor availability, voice success, SMS delay, IVR setup success, and packet-loss measurements for each proposed village.

2. **A current coastal-district denominator:** covered villages divided by all villages for Balasore, Bhadrak, Kendrapara, Jagatsinghpur, Puri, and Ganjam. The latest retrieved statewide report supplies only the total no-network count and Rayagada's figure [6].

3. **Tower failure denominators:** affected sites, total sites, structurally damaged sites, grid-only failures, fiber-cut failures, generator fuel exhaustion, battery state of health, and restoration percentiles. The Fani figure of 932 restored BTSs cannot answer any of these alone [11].

4. **Restoration distributions:** median, 90th percentile, and worst-case hours for cellular, electricity, feeder access, and roads after Fani, Yaas, Dana, and comparable floods. Fani supports a nine-day stress envelope, while Dana does not report exact durations [28][12].

5. **Feeder reliability beneath the state average:** village-level SAIDI, SAIFI, planned cuts, voltage quality, restoration priority, and phone-charging access. A 23.4-hour state average cannot represent a flooded feeder [27].

6. **Farmer device and control profile:** personal versus shared phone, feature phone versus smartphone, SIM/operator, Odia keypad capability, charging location, digital literacy, hearing/vision constraints, preferred IVR dialect, and women's independent access. NFHS household ownership cannot fill these fields.

7. **Affordability:** local prepaid pack price as a share of household disposable income, recharge frequency, zero-balance frequency, incoming-call continuity, and the cost of listening to IVR. No Odisha rural distribution was recovered.

8. **Installed solar kit cost and durability:** battery and controller quotations, enclosure IP rating, mounting, lightning/surge protection, transport, installation, replacement cycle, warranty, salt-corrosion resistance, and flood-elevation cost. The current evidence prices only small panels [29].

9. **Fallback-channel commitments:** named community-radio station coverage and backup power; licensed ham operators; OSDMA/district VSAT or satellite-phone inventory; activation authority; training; capacity; and test schedule. Search results alone do not establish availability.

10. **Cell-broadcast resumption:** the service was reported suspended on June 16, 2026, and the retrieved evidence supplies no restart date [31].

## 5. HOW IT FEEDS THE PRODUCT

### Tier and decision mapping

| Product tier | Infrastructure assumption | Product decision it powers | Failure behavior |
|---|---|---|---|
| Tier 0: Cloud control plane | Internet and upstream data available | Ingest IMD/CAP alerts, combine farm profile and forecast, generate pre/post-disaster advisory | Version every advisory; do not overwrite the last valid local package |
| Tier 1: SMS/IVR delivery | At least one operator has voice/SMS service and the phone has charge | Low-bandwidth, low-literacy farmer delivery | Pre-send before landfall; attach expiry and sequence; retry idempotently; record delivery separately from generation |
| Tier 2: Village edge gateway | Backhaul may disappear for 96 hours or longer | Cache local farm profiles, rules, Odia audio prompts, and last warning; queue outbound messages | Continue local lookup and assisted playback; synchronize when any SIM returns |
| Tier 3: Farm sensor node | Grid absent; solar intermittently available; no immediate uplink | Measure and timestamp local conditions; preserve evidence for post-disaster advice | Store locally, reduce sampling/transmit duty, use brownout-safe writes, and send summaries rather than raw streams |
| Tier 4: Institutional fallback | Partner infrastructure and trained operators exist | District EOC coordination through ham, VSAT, satellite, or radio | Never silently substitute for farmer SMS/IVR; expose status as an operator-only channel |

The key product distinction is **advisory generation versus advisory delivery**. KrishiSetu may generate the right advice locally while cellular delivery is impossible. The UI and audit log must show those as separate states.

### Offline-window and power math

The incident evidence supports a conservative engineering envelope, not a measured SLA:

- **Full-function autonomy target:** 96 hours with no grid or backhaul.
- **Survival target:** continue minimum logging, local advisory lookup, and queued delivery through day 9, because Fani's combined infrastructure disruption remained consequential at that point [28].
- **Recovery:** opportunistic synchronization over whichever operator returns first; upload summaries and exceptions before raw sensor history.

| Node | Explicit design assumption | Storage calculation | Practical starting hardware | Solar calculation |
|---|---|---|---|---|
| Low-power sensor | 3 Wh/day normal; 25% load in survival mode | Four normal days plus five survival days = 15.75 Wh load. At 80% usable battery and 85% conversion, nominal need = 15.75 / (0.80 x 0.85) = **23.2 Wh** | **12.8 V, 3 Ah = 38.4 Wh** minimum starting point | At a conservative 2 peak-sun-hours and 65% system efficiency, recharge floor = 3 / (2 x 0.65) = **2.3 W**; use **10 W** for margin |
| Village gateway | 24 Wh/day normal; 25% survival load | Four normal days plus five survival days = 126 Wh load. Nominal need = 126 / (0.80 x 0.85) = **185.3 Wh** | A 12.8 V, 12 Ah pack is only 153.6 Wh and is insufficient for this envelope; start near **12.8 V, 24 Ah = 307.2 Wh** | Recharge floor = 24 / (2 x 0.65) = **18.5 W**; use **40-50 W** to recover after cloudy days |

These load values are **engineering assumptions to be measured**, not source statistics. The Odisha policy's 5.5 kWh/m2/day annual average supports solar feasibility [25], but cyclone-season clouds justify the deliberately lower 2-hour sizing case. Lab-test the actual board, modem, sensors, speaker, amplifier, and idle current before freezing the battery.

The visible component evidence supports only a partial cost floor: INR 1,000 for a 10 W panel and INR 1,500 for a 20 W panel [29]. A complete budget must remain "quote required" until battery, controller, enclosure, mounting, protection, and labor are priced locally.

## 6. REAL-vs-FILLER

| Genuinely usable now | Why it is usable | Decorative or unsafe if overinterpreted | Why it is filler |
|---|---|---|---|
| Fani's complete shutdown and nine-day combined disruption | Directly sets offline and graceful-degradation tests [28] | "Odisha is almost fully electrified" | Connection presence says nothing about cyclone uptime; NFHS reports access, not continuity [1] |
| Dana's named block and GP failures | Identifies realistic pilot locations and common-cause failures [12] | Statewide mobile subscription totals | SIM counts do not establish village signal, device control, or disaster survivability |
| 23.4 rural supply-hours/day | Provides a normal-operation recharge baseline [27] | Treating 0.6 hours/day as the required battery | The annual mean erases multi-day event outages |
| Rural phone 86.9% and Internet 30.9% | Supports SMS/IVR-first and app-optional architecture [1] | Calling 86.9% "smartphone penetration" | NFHS reports household mobile-phone presence, not smartphone type or farmer ownership |
| 5.5 kWh/m2/day solar resource plus small-panel quotes | Supports a real prototype power rig and an initial cost floor [25][29] | State solar potential in gigawatts | Utility-scale potential does not size a shaded, flooded village node |
| CB suspension status | Prevents an unavailable channel becoming a dependency [31] | "India has cell broadcast, so delivery is solved" | Launch/capability does not prove current operational availability or tower survival |
| Ham's Kerala responder role | Shows a trained human network can bridge failed communications [22] | Treating 300 Kerala operators as Odisha farmer reach | Different state, event, licensing, users, and one-to-one operating model |
| Unknown district RAT table | Forces an honest pilot gate | Coloring a map from operator marketing screenshots | Visual nominal coverage is not measured voice, SMS, or IVR performance |

The central rule is simple: retain evidence that changes a design parameter or test; discard numbers that merely make the presentation look complete.

## 7. NOISE LOG

| Searched and discarded | Reason for discard |
|---|---|
| Opensignal June 2025 India rankings | National/operator-level experience does not answer coastal Odisha district 2G/3G/4G availability [5] |
| Ookla district searches | No usable public district RAT table was recovered |
| Jio public coverage map | Operator self-map, dynamic presentation, no multi-operator measured table or cyclone uptime |
| Facebook and Instagram infrastructure claims | Unstable attribution and no reproducible district dataset |
| Generic NISE and utility-scale solar-potential pages | Useful for state potential, not monthly off-grid node sizing |
| US Walmart charge-controller result | Wrong market and currency for an Odisha BOM |
| Generic VSAT Slideshare/Scribd results | Explain the technology but do not prove Odisha inventory, activation, or cyclone survival |
| OSDMA cyclone listing pages without detailed documents | Authority is strong, but the retrieved listing text contained no operating metrics |
| Broad community-radio journal abstract | Discussed resilience conceptually but yielded no named station, backup-power record, audience reach, or outage result |
| PIB result numbered PRID 2257102 | Extracted page was about LokOS rural livelihoods, not cell broadcast [23] |
| 1,921-village secondary report | Older/conflicting with the later March 2026 count of 1,237 and supplied no coastal annexure; retained only in research notes, not as the current figure |
| Dana statewide impact headline alone | Large affected-population totals do not answer phone, road, or power duration; only the block-level observations were retained |
| Fani's 932 restored BTSs as a failure rate | No total-site or failed-site denominator [11] |

## 8. VERDICT

### Prototype: **GO**

Build the KrishiSetu prototype with real offline behavior, not a connectivity-themed mockup:

1. Cloud alert ingestion and farm-profile advisory generation.
2. SMS and IVR adapters with simulated success, delay, duplicate, and total-failure states.
3. A village gateway holding the last valid alert, local farm profiles, Odia audio, and an outbound queue.
4. A solar-powered sensor node with brownout-safe local storage and selectable normal/survival duty cycles.
5. A dashboard that separates "generated," "queued," "sent," "delivered," "played," and "expired."
6. A 96-hour no-grid/no-backhaul test followed by five days of survival mode.

The prototype can credibly demonstrate the official problem statement without claiming that SMS or IVR works while cellular infrastructure is down.

### Limited field trial: **PARTIAL**

A small non-production trial in one resilient and one weak-signal coastal village is justified if the team first measures all operators, obtains local solar quotations, recruits users across phone types and literacy levels, and runs planned power/network cut tests. Results must remain site-specific.

### Operational coastal pilot: **GATED**

Do not promise production readiness until the team has:

- a measured district and village coverage matrix;
- restoration percentiles from operators, DISCOMs, and district authorities;
- verified 96-hour energy tests through cloudy and flooded conditions;
- household device, charging, language, and affordability data;
- written SMS/IVR provider limits and multi-SIM failover behavior;
- confirmed OSDMA/community-radio/ham/VSAT/satellite partnerships where claimed; and
- confirmation that cell broadcast has resumed, if the design references it.

**Overall verdict:** KrishiSetu is a **GO as an offline-first prototype**, **PARTIAL as a controlled research trial**, and **GATED as an operational coastal service**.

## Synthesis

| Strategy | Mechanism and scope | Main strength | Trade-off and evidence base | Time horizon |
|---|---|---|---|---|
| SMS/IVR | Personalized one-to-one cellular delivery | Statement-faithful and compatible with non-smartphones | Fails with towers, power, backhaul, congestion, or an uncharged phone; strong pre-Fani SMS evidence, weak post-landfall continuity [28] | Best before landfall and after partial restoration |
| Cell broadcast | Geo-targeted one-to-many alert | Fast mass warning without a recipient list | Not personalized or two-way; current Indian service was reported suspended [31] | External alert ingress when operational |
| Village edge gateway | Local cache, rules, audio, and queue | Preserves knowledge and state without WAN | Requires solar, enclosure, maintenance, and a local access model | Landfall through restoration tail |
| Sensor store-and-forward | Local sensing with delayed summaries | Maintains farm evidence when backhaul fails | Cannot deliver farmer advice by itself; energy budget must be measured | Continuous, with survival duty cycle |
| Community radio | One-to-many local audio | Potentially accessible for low-literacy users | No deployment-grade Odisha cyclone survival evidence recovered | Partnership option, not baseline |
| Ham radio | Licensed human-operated responder link | Worked as a rescue-information bridge in Kerala [22] | Low capacity, trained operators, not mass personalization | Emergency coordination |
| VSAT/satellite phone | Infrastructure-independent institutional backhaul or voice | Can bypass terrestrial fiber and towers | Cost, licensing, terminals, trained users, and Odisha inventory remain unverified | District/EOC fallback if contracted |

The non-obvious conclusion is that **offline-first does not mean every delivery channel works offline**. It means the system preserves the last trusted warning, farm context, local observations, and a correctly ordered delivery queue while external networks fail. Fani justifies a long survival tail; Dana identifies where compound failures occur; NFHS justifies SMS/IVR over app-only delivery; solar evidence makes autonomous hardware plausible. The missing district and device data then become explicit pilot measurements rather than hidden assumptions.

## References

1. *2019-21*. https://preview.dhsprogram.com/pubs/pdf/fr374/fr374_odisha.pdf
2. *Coverage Maps - Opensignal*. https://insights.opensignal.com/coverage-maps
3. *Cyclone Fani 2019 DLNA Report - Odisha State Disaster ...*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report/
4. *ASER 2024 National Findings*. https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-National-findings.pdf
5. *India, June 2025, Mobile Network Experience Report | Opensignal*. https://insights.opensignal.com/reports/2025/06/india/mobile-network-experience
6. *No mobile network in state's 1237 villages: Mahaling*. https://timesofindia.indiatimes.com/city/bhubaneswar/no-mobile-network-in-states-1237-villages-mahaling/articleshow/129353681.cms
7. *Saturation of 4G Mobile Services Home Schemes & ...*. https://usof.gov.in/en/saturation-of-4g-mobile-services
8. *Cell broadcast early warning system - ITU*. https://www.itu.int/en/ITU-D/Emergency-Telecommunications/Pages/EW4ALL/cell-broadcast.aspx
9. *Cyclone Fani 2019: Telecom, Water Services Partially Restored ...*. https://www.ndtv.com/india-news/cyclone-fani-2019-telecom-water-services-partially-restored-in-bhubaneswar-puri-2033353
10. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
11. *Cyclone Fani: Telecom firms operationalise over 900 base ...*. https://timesofindia.indiatimes.com/india/cyclone-fani-telecom-firms-operationalise-over-900-base-stations-in-odisha-restoration-work-on/articleshow/69184542.cms
12. *Cyclone Dana Assessment Report*. https://ysdindia.org/wp-content/uploads/2025/01/Report-of-the-Rapid-Assessment_Cyclone-Dana_YSD-Odisha.pdf
13. *Floods 2018 - Kerala State Disaster Management Authority*. https://sdma.kerala.gov.in/floods_2018
14. *Cell Broadcast Service Temporarily Suspended by NDMA ET Telecom https://telecom.economictimes.indiatimes.com › industry*. https://telecom.economictimes.indiatimes.com/news/industry/cell-broadcast-service-temporarily-suspended-by-ndma-what-you-need-to-know/131731900
15. *Fostering resilience: Community radio and disaster ...*. https://journals.sagepub.com/doi/10.1177/01634437241282243
16. *2018 Kerala floods - Wikipedia*. https://en.wikipedia.org/wiki/2018_Kerala_floods
17. *1,921 Odisha Villages Still Off The Mobile Grid: Centre*. https://ommcomnews.com/odisha-news/1921-odisha-villages-still-off-the-mobile-grid-centre/
18. *Cyclone Amphan: Telcos, infrastructure providers rush to ...*. https://telecom.economictimes.indiatimes.com/news/cyclone-amphan-telcos-infrastructure-providers-rush-to-restore-telecom-network/75867056
19. *How HAM radio helped Kerala rescue mission | Kerala Flood ...*. https://www.manoramaonline.com/videos/news/kerala-floods/2018/08/21/how-ham-radio-helped-kerala-rescue-mission.html
20. *Kerala Flood 2018 Role of ham radio Service - Issuu*. https://issuu.com/activehams/docs/kerala_flood_-_mission_report
21. *Govt launches Cell Broadcast System to strengthen India's ...*. https://newsonair.gov.in/cell-broadcast-system-launched-to-enhance-disaster-communication
22. *How 300 Radio Operators Are Helping Rescue People In Flood ...*. https://www.ndtv.com/india-news/how-300-radio-operators-are-helping-rescue-people-in-flood-hit-kerala-1903973
23. *Government of India*. https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2257102&lang=1&reg=3
24. *Amphan impact: Mobile, broadband normalcy in WB/Kolkata only ...*. https://telecom.economictimes.indiatimes.com/news/amphan-impact-mobile-broadband-normalcy-in-wb/kolkata-only-next-week/75897469
25. *2 Order Odisha Solar Power Policy*. https://www.cbip.org/policies2019/PD_07_Dec_2018_Policies/Orissa/1-Solar/2%20Order%20Odisha-Solar-Power-Policy.pdf
26. *Odisha FANI cyclone Assessment Report*. https://ircsstoragedev.blob.core.windows.net/wordpresswebsite/2024/03/OdishaFaniAsessmentReport.pdf
27. *GOVERNMENT OF INDIA MINISTRY OF POWER RAJYA SABHA UNSTARRED QUESTION NO.2709 ANSWERED ON 24.03.2025 POWER SUPPLY IN RURAL AREAS 2709*. https://www.sansad.in/getFile/annex/267/AU2709_g7kjOi.pdf?source=pqars
28. *India Cyclone Fani Sitrep 12 May 2019*. https://www.unicef.org/media/82111/file/India-Cyclone-Fani-SitRep-12-May-2019.pdf
29. *Buy Rooftop Solar Panel Online at Best Prices in India*. https://www.loomsolar.com/collections/solar-panels
30. *Government launches indigenous Cell Broadcast System ... News On AIR https://newsonair.gov.in › government-of-india-launche...*. https://newsonair.gov.in/government-of-india-launches-indigenous-cell-broadcast-system-for-instant-disaster-alerts
31. *Centre Suspends Cell Broadcast Service Temporarily*. https://www.ndtv.com/india-news/centre-suspends-cell-broadcast-service-temporarily-11641737
32. *12Ah 12.8V LFP (LiFePO4) Battery Pack With BMS Saurally Solar https://saurally.com › Lithium Batteries*. https://saurally.com/product/12ah-12-8v-lfp-lifepo4-battery-pack-with-bms
