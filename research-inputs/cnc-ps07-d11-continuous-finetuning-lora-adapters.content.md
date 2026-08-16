# Realistic Daily Learning Loop for Odisha Farm Advisories

## 1. EXECUTIVE SUMMARY

- **Split the learning loop by timescale**: Sensor thresholds and farm-profile retrieval can adapt in seconds or minutes, but a 1-4B LLM should be fine-tuned on a server, evaluated, signed, and then distributed. TensorFlow Lite warns that on-device training can take seconds or much longer and consume substantial battery; training a language model from scratch can take days even on powerful servers [2]. Therefore, "phone adapts instantly" should mean profile/retrieval updates, online statistics, or switching to a downloaded adapter - not phone-side QLoRA.

- **A modest GPU is sufficient, but published minimums are not service-level guarantees**: A current community table gives an absolute minimum of about **3.5GB VRAM for 3B QLoRA** versus **8GB for 16-bit LoRA**, while warning that models and settings vary [30]. A **24GB NVIDIA L4** has ample prototype headroom and a 72W power envelope [19]. Provision a 12GB-class GPU for a carefully constrained 1B experiment or a 24GB-class GPU for 3-4B work, but benchmark the selected model, sequence length, batch, and corpus before promising a daily completion time.

- **The requested 10-50MB adapter range is plausible, not automatic**: For stated transformer assumptions, FP16 rank-8/rank-16 LoRA adapters calculate to approximately **11.3/22.5MB for a 1B-like model** and **24.3/48.6MB for a 3B-like model**. QLoRA reduces base-model memory, not necessarily adapter precision [30]. A public 3B adapter artifact was about **195MB**, showing that target modules, rank, saved heads or embeddings, and serialization can push real releases outside the desired range [32].

- **There is no defensible universal "examples per day" threshold**: LIMA showed strong alignment from **1,000 carefully curated demonstrations**, but on a 65B model and a different task [5]. LESS found that a selected **5%** subset often beat training on the full instruction set [18]. For this project, outcome validity, crop/hazard coverage, and held-out improvement matter more than forcing a daily update from a small batch.

- **Synthetic data is useful only behind a real-data anchor**: Self-Instruct generated and filtered instruction/input/output triples and reported a 33 percentage-point improvement on one benchmark [40]. However, repeated training on generated data can erase low-probability parts of the original distribution; retaining real data substantially reduced degradation in a controlled study [41]. Use a larger model for paraphrases, Odia renderings, and rare scenario drafts, never to fabricate "farmer did X, result Y" outcome labels.

- **SMS is a notification channel, not an adapter transport**: Google Play Asset Delivery can perform compression, auto-updates, and delta patching, but it depends on the Play ecosystem [25]. Nearby Connections can move data peer-to-peer without Internet access [26]. Use SMS/IVR for warnings and update notices; use resumable HTTPS, village Wi-Fi, offline peer transfer, or supervised USB for adapter files.

- **Federation is PARTIAL, not production-ready for phone LLM fine-tuning**: Flower has an Android/TFLite example using WorkManager and federated averaging [34], but its Android SDK tutorial is marked experimental and incompatible with the latest Flower release [33]. TensorFlow Federated is strongest for declarative research and simulation, while its deployment documentation notes backend and construct limitations [12]. A prototype should federate a tiny classifier or aggregated statistic, not a 1-4B LoRA job.

- **Overall verdict - prototype GO, pilot GATED**: A convincing demo can combine IMD ingestion, deterministic agronomy rules, a quantized 1B phone model, a server-generated signed LoRA adapter, offline distribution, SMS/IVR, and rollback. A farmer-facing pilot remains gated on measured Odisha network delivery, Odia voice usability, outcome-labeled farm data, causal safety evaluation, privacy controls, poisoning defenses, and a measured server training SLA.

## 2. DATA INVENTORY

Reliability grades: **A** = peer-reviewed or first-party specification; **B** = official implementation documentation or direct production report; **C** = community benchmark, vendor claim, or transparent engineering estimate; **D** = unverified marketing, anecdote, or an unanswered requirement.

| Sub-question / item | Named source, URL, date | Spec / price | Feasibility for India | Grade |
|---|---|---|---|---|
| LoRA mechanism | Hu et al., "LoRA," http://arxiv.org/abs/2106.09685, 2021 | Freezes pretrained weights and injects trainable low-rank matrices [50]. No hardware price. | Strong fit for distributing small regional/language changes while retaining one base model. | A |
| QLoRA upper-bound demonstration | Dettmers et al., "QLoRA," https://arxiv.org/abs/2305.14314, 2023 | Fine-tuned a 65B model on one 48GB GPU [6]. This does not supply a 1-4B daily-job time. | Proves memory efficiency, not an Odisha deployment SLA. | A |
| 3B memory lower bounds | Unsloth memory requirements, https://docs.unsloth.ai/get-started/fine-tuning-llms-guide/memory-requirements, accessed 2026-08-16 | Approximate absolute minimum: **3.5GB QLoRA**, **8GB 16-bit LoRA** for 3B; some models require more [30]. Price not quoted. | Useful for screening hardware, but procure with headroom rather than at the minimum. | C |
| Practical GPU option | NVIDIA L4 product specification, https://www.nvidia.com/en-us/data-center/l4/, accessed 2026-08-16 | **24GB**, **300GB/s**, **72W** [19]. Source does not publish a stable India street or cloud price. | Good 3-4B prototype server target where power and cooling are limited; obtain local/cloud quotes. | A |
| CPU-only QLoRA | Intel Extension for Transformers QLoRA documentation, https://github.com/intel/intel-extension-for-transformers, accessed 2026-08-16 | Supports CPU execution with NF4/FP4/INT4/INT8 and `--no_cuda` [38]. No verified wall-clock or RAM figure for this farm workload. | Technically possible for a lab fallback; not acceptable as a daily SLA until timed end-to-end. | B for capability; D for cadence |
| Daily training time | No public benchmark matched a specified 1-4B model, sequence length, adapter rank, farm corpus size, epochs, and target hardware | **Missing**. Set an engineering acceptance target, then measure p50/p95 completion and energy. | A daily cadence is plausible on a GPU for small batches, but cannot be guaranteed from the available evidence. | D |
| Adapter byte estimate | Engineering calculation using `bytes x rank x sum(input+output dimensions)` across seven attention/MLP projections; 2026-08-16 | Stated assumptions: 1B-like, 16 layers, hidden 2,048, MLP 8,192, KV output 512 -> **11.27MB r8**, **22.54MB r16**. 3B-like, 28 layers, hidden 3,072, MLP 8,192, KV output 1,024 -> **24.31MB r8**, **48.63MB r16**. Excludes metadata, saved heads/embeddings, optimizer state, and packaging. | Supports a 10-50MB design target only if module selection and rank are controlled. | C |
| Real adapter-size counterexample | Hugging Face public Llama-3.2-3B adapter artifact, accessed 2026-08-16 | About **195MB** [32]. | Release pipeline must enforce a byte budget and test the actual artifact, not infer size from parameter count alone. | B |
| Save and load adapters | Hugging Face PEFT checkpoint format, https://huggingface.co/docs/peft/main/en/developer_guides/checkpoint, accessed 2026-08-16 | Saves adapter weights and configuration rather than the whole base model [22]. | Strong fit: install the base model once, then distribute signed adapters. | B |
| Hot-swap versus merge | Hugging Face PEFT hotswap documentation, https://huggingface.co/docs/peft/main/en/package_reference/hotswap, accessed 2026-08-16 | Hotswap replaces adapter weights in place and avoids recompilation, but supports LoRA only and requires compatible target-layer structure [37]. | Keep an immutable base plus A/B adapter slots for rollback. Merge only a stable, single-purpose release when runtime simplicity outweighs flexibility. | B |
| Number of examples | Zhou et al., "LIMA," https://arxiv.org/abs/2305.11206, 2023 | **1,000 curated demonstrations** on a 65B model [5]. No valid examples/day conversion. | Treat 500-1,000 accumulated, reviewed cases as a seed-planning range, not a performance guarantee or daily quota. | A evidence; C extrapolation |
| Data selection | Xia et al., "LESS," https://arxiv.org/abs/2402.04333, 2024 | Influence-based selection; selected **5%** often outperformed the full data set [18]. | Prioritize diverse, high-confidence cyclone/flood cases over every call-centre transcript. | A |
| Required outcome record | Project data contract, derived from the advisory objective | Minimum fields: alert and model version; farm, crop and stage; location granularity; advice; delivery/comprehension; action and timing; cost; observed damage/yield; confounders; label confidence. | Collect through KCC/extension workflows with consent, coarse location, and controlled vocabularies. Free text alone is insufficient. | C design requirement |
| Synthetic distillation | Wang et al., "Self-Instruct," https://aclanthology.org/2023.acl-long.754/, 2023 | Generates instruction/input/output examples, then filters invalid and near-duplicate records; reported 33-point benchmark improvement [40]. | Useful for Odia paraphrases, voice scripts, and scenario coverage after agronomist review. | A |
| Synthetic-data failure | Shumailov et al., "AI models collapse when trained on recursively generated data," https://www.nature.com/articles/s41586-024-07566-y, 2024 | Without original data, test perplexity worsened from about 20 to 28 in one OPT-125m experiment; retaining 10% original data caused only minor degradation [41]. | Maintain an immutable real-data replay set and provenance flag for every synthetic example. | A |
| India connectivity baseline | Ookla, village-level India 4G signal study, published 2025-10-07 | Sampled 4G signal above -110 dBm in **88.9% of villages** [3]. It is not an Odisha-specific completion-rate study. | Broad reach does not imply continuous service; all updates need pause/resume and offline paths. | B |
| Play-based distribution | Android Play Asset Delivery, https://developer.android.com/guide/playcore/asset-delivery, accessed 2026-08-16 | Compression, delta patching, delivery modes, and automatic updates [25]. Price not separately stated; Play dependency applies. | Useful for managed Play-distributed smartphones, not a universal rural channel. | A |
| Offline phone-to-phone distribution | Google Nearby Connections, https://developers.google.com/nearby/connections/overview, accessed 2026-08-16 | Fully offline, high-bandwidth peer-to-peer transfer [26]. | Good for extension-worker phones and village update days; still needs signing and transfer resumption. | A |
| Transfer physics | Payload-only engineering calculation, 2026-08-16 | At **0.1/1/10 Mbps**, 10MB takes about **13.33/1.33/0.13 min**; 50MB takes **66.67/6.67/0.67 min**. Retries, handshakes, congestion, and billing add overhead. | A 50MB daily cellular push is poor for weak links; schedule Wi-Fi/offline transfer and update only when the hash changes. | C |
| Farmer access channel | mKisan Kisan Call Centre, https://mkisan.gov.in/, accessed 2026-08-16 | **1800-180-1551**, reachable from mobile/landline networks; replies supported in 22 local languages [47]. | A credible human escalation and feedback route. It is not evidence that KCC will host USB or adapter distribution without an agreement. | A |
| IMD feed surface | IMD API list, https://mausam.imd.gov.in/responsive/api_list.php, accessed 2026-08-16 | Lists city, lat/long, subdivision rainfall, state/district rainfall, bulletin, Mausamgram and nowcast products [48]. | Good alert input; farm sensor fusion, caching, agronomy policy, authentication and operational SLA remain application responsibilities. | A |
| Flower on Android | Flower Android example, https://github.com/adap/flower/tree/main/examples/android, accessed 2026-08-16 | Android/Java, TensorFlow Lite, WorkManager; Python server with a custom ByteBuffer serialization path and FedAvg [34]. Example used CIFAR-10 and small client cohorts [34]. | Suitable as a proof for a tiny classifier, not evidence for 1-4B adapter training across real phones. | B |
| Flower version risk | Flower Android quickstart, https://flower.ai/docs/framework/tutorial-quickstart-android.html, accessed 2026-08-16 | Android SDK marked experimental and incompatible with latest Flower at the time documented [33]. | Pin versions or implement protocol messages directly; do not depend on an abandoned quickstart. | B |
| FedML mobile | FedML platform documentation, https://doc.fedml.ai/, accessed 2026-08-16 | Claims edge and smartphone on-device support [24]; the reviewed material did not expose an equally concrete current Android build path and compatibility matrix. | Candidate for a separate spike only. | C |
| TensorFlow Federated | TFF, https://www.tensorflow.org/federated, accessed 2026-08-16 | Declarative federated computation and multi-machine simulation [4]. Deployment docs are under construction and note that native backends may not support all constructs [12]. | Strong research/simulation tool; weak fit as a drop-in heterogeneous Android fleet runtime. | B |
| Secure aggregation | Bonawitz et al., "Practical Secure Aggregation," https://research.google/pubs/practical-secure-aggregation-for-privacy-preserving-machine-learning/, 2017 | Server learns only an aggregate over a sufficiently large surviving cohort [42]; protocol is designed for dropout tolerance [42]. Secure aggregation alone may be insufficient and can be combined with differential privacy [42]. | Use only with cohort minima, clipping, user-level DP, consent, and incident monitoring. | A |
| BOCPD | Adams and MacKay, "Bayesian Online Changepoint Detection," https://arxiv.org/abs/0710.3742, 2007 | Maintains a posterior over run length through recursive message passing [13]. Exact time/space grow linearly with observations; pruning can reduce average work [13]. | Feasible on a phone for a few streams with pruning; avoid unbounded histories on sensor microcontrollers. | A |
| Incremental tree | River Hoeffding Tree documentation, https://riverml.xyz/latest/api/tree/HoeffdingTreeClassifier/, accessed 2026-08-16 | One-pass `learn_one` updates; exposes a memory cap and memory-management behavior [35]. | Appropriate for phone CPU prediction if implemented in Android-compatible native/Java code. River itself is a Python reference. | B |
| Generic on-device gradient training | TensorFlow Lite on-device training, https://www.tensorflow.org/lite/examples/on_device_training/overview, accessed 2026-08-16 | Java/C++ can invoke a training signature [2], but jobs can be slow and battery-intensive [2]. | Reserve for tiny heads or classifiers while charging; reject as the primary 1-4B learning path. | A |
| Real fleet case | Google Gboard federated deployment paper and Google AI blog, https://research.google/pubs/federated-learning-for-mobile-keyboard-prediction/ and https://blog.google/technology/ai/federated-learning-collaborative-machine-learning-without-centralized-training-data/, accessed 2026-08-16 | Commercial-scale train/evaluate/deploy loop without directly collecting device data [43]; the documented live task used logistic click prediction, not an LLM [43]. Devices participate while idle, charging, and on free wireless [20]. | Valid architecture precedent for scheduling and fleet orchestration, but not proof of daily LoRA distribution. | A/B |
| Catastrophic forgetting | Luo et al., "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning," http://arxiv.org/html/2308.08747v5, 2023/updated version | Defines forgetting as loss of previously learned information while acquiring new knowledge and studies it in continual instruction tuning [51]. | Every candidate adapter needs replay, regression tests, agronomy safety tests, canary rollout, and rollback. | A |

### Adapter packaging decision

Use **one immutable quantized base model** per supported hardware class. Store two adapter slots: `current` and `previous`. Each release manifest should include the base-model hash, adapter hash, semantic version, crop/hazard/language scope, training-data snapshot, schema version, minimum runtime, creation time, expiry, signature, and rollback target.

Do not merge per-farm information into model weights. Farm profile, current crop stage, location, and recent sensor observations belong in a local structured store or retrieval context. Merge an adapter into the base only for a thoroughly tested, long-lived appliance build; otherwise load or hotswap the signed regional adapter. Hotswap is faster operationally, but the PEFT implementation requires compatible LoRA layer structures [37].

### Data acceptance decision

A training example is not "farmer asked a question." It becomes outcome evidence only when the project can connect advice, whether it was understood and acted upon, timing, later damage/yield, and relevant confounders. Daily collection can continue, but training should be triggered by a quality gate rather than the calendar: enough new coverage, no unresolved label conflicts, acceptable synthetic fraction, and measurable improvement on a frozen holdout.

A practical statistical benchmark is approximately **385 independent outcome labels** for estimating a binary success proportion to about plus or minus 5 percentage points at 95% confidence near 50%. That is a survey-style precision calculation, not proof of causal crop-loss reduction and not a fine-tuning threshold. Crop, district, hazard, language, and farm-size slices will require substantially more observations.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| Peer-reviewed PEFT and data-selection research | 8 strong sources: LoRA, QLoRA, LIMA, LESS, Self-Instruct, model collapse, LoRA+, DoRA | No exact 1-4B Odisha corpus, daily runtime, or adapter-transfer trial | **A for mechanisms; C for local sizing** |
| Official PEFT/runtime documentation | 6 useful hits: PEFT checkpoints/hotswap, TFLite training, Intel CPU path, NVIDIA L4, community memory table | Version-dependent APIs; no fixed end-to-end SLA or India price | **B** |
| Federated-learning frameworks | Flower has the clearest Android example; TFF has strong simulation semantics; FedML states mobile support | Flower Android version gap; TFF deployment limitations; no public heterogeneous Android LoRA fleet | **C overall** |
| Security and privacy research | Secure aggregation has a formal protocol and dropout analysis [42] | No Odisha-specific consent model, threat model, cohort size, DP budget, or poisoning benchmark | **A mechanism; D deployment** |
| Mobile distribution and India connectivity | Android asset delivery, Nearby, Ookla village coverage, mKisan/KCC, and IMD surfaces | No Odisha district-by-district 10/50MB completion rate, telecom cost, DLT workflow, or KCC distribution agreement | **B** |
| Online-learning methods | BOCPD, stream drift methods, Hoeffding trees, and TFLite signatures cover the main algorithm classes | No benchmark on the intended farmer phone, sensor rate, battery, or Java port | **B** |
| Production fleet case studies | Gboard demonstrates orchestration, eligibility, evaluation, and deployment at commercial scale [43] | Task was a small click model, not continual LLM LoRA [43] | **B as analogy; D as LLM proof** |
| Blogs, social posts, and model cards | Useful for discovering minimum-memory claims and real artifact sizes | Workloads, sequence lengths, power, data and evaluation are often omitted; marketing language dominates | **C-D** |

**Coverage judgment:** The evidence is strong enough to design and demonstrate the architecture. It is not strong enough to promise crop-loss reduction, daily adapter delivery, or safe production federation without local measurements.

## 4. WHAT IS MISSING

1. **A reproducible daily training benchmark.** No reviewed public source runs the project's exact 1B, 3B, or 4B model with its sequence length, target modules, rank, data volume, epochs, optimizer, GPU/CPU, and evaluation suite. Published memory minima cannot supply training time.

2. **A universal examples-per-day threshold.** LIMA supports the value of 1,000 carefully selected examples [5], and LESS supports targeted selection [18], but neither predicts measurable cyclone-advisory improvement from a daily count. Only a local learning curve can answer this.

3. **Public evidence of daily LoRA deployment to a heterogeneous Android fleet.** Gboard is a genuine fleet-scale federated case, but the documented production task is logistic click prediction [43]. Flower's Android path is an educational TFLite example with version caveats [33].

4. **Odisha transfer measurements.** The 88.9% village 4G signal result is nationwide and signal-threshold based [3]. It does not provide completion rates, interruption frequency, cost, p95 latency, or battery use for 10-50MB packages in cyclone-affected districts.

5. **Measured delta efficiency for adapters.** Play Asset Delivery supports delta patching [25], but no reviewed source shows the compression ratio between successive safetensors LoRA releases. Dense floating-point tensors can change throughout; "delta" does not guarantee a tiny file.

6. **Current IMD integration terms and operational SLA.** The public page lists forecast and warning products [48], but the reviewed evidence does not establish authentication, rate limits, redistribution rights, outage behavior, or contractual availability for this application.

7. **Odia and low-literacy safety evidence.** There is no public evaluation here for dialect coverage, text-to-speech intelligibility under noisy conditions, comprehension of time-sensitive instructions, or recovery advice accuracy.

8. **Causal outcome labels.** No public corpus connects a versioned advisory to farmer action, timing, cost, local exposure, and later crop loss or yield for this exact Odisha problem.

9. **A complete privacy and poisoning design.** Secure aggregation protects individual updates from the server under its protocol [42], but it does not by itself supply differential privacy or determine whether a malicious update is safe [42]. The required consent, retention, DP budget, robust aggregation, and incident response remain open.

10. **CPU-only economics.** CPU QLoRA is supported technically [38], but public evidence reviewed here does not establish RAM, power, wall-clock time, or total cost for a daily farm-advisory job.

## 5. HOW IT FEEDS THE EDGE-AI ENGINE

| Tier | Input and update mechanism | Decision it powers | Safe operating boundary |
|---|---|---|---|
| **Sensor node** | Soil moisture, water level, rainfall, temperature and battery; range checks, debounce, rolling median/EWMA, and adaptive thresholds | "Is the reading plausible?", "Has water risen unusually?", "Should the phone be awakened?" | Use deterministic arithmetic and tiny state. Do not run an LLM. Transmit observations plus quality flags. |
| **Sensor node or phone** | Pruned BOCPD over selected streams | "Did the local process change relative to its recent regime?" | Exact BOCPD cost grows with history; prune low-probability run lengths or cap the window [13]. It detects change, not agricultural causality. |
| **Phone hub** | Bounded Hoeffding tree or small online classifier updated one example at a time | "Does this sensor pattern merit escalation?", "Which delivery channel is currently reliable?" | Enforce a hard memory cap [35]. Port or reimplement for Android; do not assume Python River ships unchanged. |
| **Phone hub** | Cached IMD alert, farm profile, crop-stage table, local observations and deterministic action library | "Which pre-disaster or recovery actions are permitted and urgent?" | Agronomy policy selects actions. The LLM must not invent pesticide, evacuation, finance, or medical instructions. |
| **Phone hub** | Quantized 1B model plus signed regional/language LoRA adapter | Render the selected action as concise Odia text, conversational explanation, or an IVR script; answer bounded follow-ups offline | Start with 1B. Treat 3-4B as capable-phone options after RAM, latency, thermal and battery tests. A nominal 4-bit weight floor is about 0.5GB per 1B parameters before runtime and KV-cache overhead. |
| **Phone hub** | Profile/retrieval update, threshold update, or adapter A/B switch | Immediate personalization and recovery from a bad release | This is the honest meaning of instant adaptation. On-device LLM gradient training is not required. |
| **Phone hub** | Signed manifest, resumable download, Nearby transfer, or supervised USB | "Is this package authentic, compatible, newer, complete and safe to activate?" | Verify signature and hashes before activation; retain the previous known-good adapter. SMS contains only the notice or link. |
| **Learning server** | Consent-controlled, de-identified outcome records; real-data replay; provenance-tagged synthetic examples | "Is there enough new, trustworthy information to train a candidate?" | Quarantine duplicates, conflicting labels, implausible outcomes, and model-generated outcome claims. |
| **Learning server** | QLoRA/LoRA on 1-4B model | Produce a candidate language/domain adapter | GPU is the default. CPU is a fallback only after a measured completion SLA. The base remains immutable. |
| **Learning server** | Frozen evaluation by crop, hazard, district, language, literacy mode and pre/post-disaster phase | "Does the candidate improve usefulness without forgetting safety or earlier skills?" | Training loss is never a release criterion. Catastrophic forgetting is a documented continual-tuning risk [51]. |
| **Learning server** | Signing, canary assignment, telemetry, A/B release and rollback | "Who gets the update, when, and when is it withdrawn?" | Roll out to staff/test phones, then small opt-in cohorts. Stop on safety regression, crash, excessive latency, abnormal feedback, or outcome deterioration. |
| **Learning server** | SMS/IVR gateway and KCC escalation | Reach non-smartphone and low-literacy farmers | Non-smartphone users do not receive adapters. They receive centrally rendered SMS/IVR, with human escalation through a channel such as KCC [47]. |

### Three-loop operating model

**Loop 1 - seconds to minutes:** Nodes perform bounded filtering; the phone fuses local changes with cached IMD data. If connectivity disappears during a cyclone, deterministic rules and cached templates remain available.

**Loop 2 - minutes to hours:** The phone retrieves the farm profile, selects approved actions, and uses the small model only to explain or voice them. The farmer's answer updates the local state immediately; it does not rewrite the LLM.

**Loop 3 - daily collection, conditional release:** The server may ingest and quality-check data every day, but it trains or releases only when evidence passes gates. Candidate QLoRA is evaluated against the previous adapter, a no-adapter baseline, safety rules, and slice-specific holdouts. Successful candidates are signed and moved through canary rollout; failed candidates never reach phones.

## 6. REAL-vs-FILLER

| Claim or component | REAL - usable evidence | FILLER - unsupported extension | Decision |
|---|---|---|---|
| Server QLoRA | QLoRA demonstrates large memory savings and even 65B fine-tuning on a 48GB GPU [6]. | "Any CPU can finish every 3B daily job overnight." | Use GPU by default; benchmark CPU before mentioning an SLA. |
| Small adapter releases | PEFT saves adapter-only checkpoints [22]; controlled rank/module choices can calculate into 10-50MB. | "Every LoRA adapter is tiny" or "delta updates are always a few KB." | Enforce package-byte and download tests in CI. |
| Adapter switching | PEFT supports LoRA hotswap with structural compatibility constraints [37]. | Per-farmer merged base models or unversioned overwrites. | One base, scoped adapters, A/B slots, signed manifest. |
| Daily learning | Daily ingest and evaluation are operationally reasonable. | "The model improves every day" regardless of label count or distribution. | Release on evidence, not cadence. |
| Synthetic distillation | Self-Instruct shows useful generated-and-filtered instruction data [40]. | Synthetic crop outcomes treated as field evidence. | Permit synthetic wording/scenarios; prohibit synthetic outcome labels. |
| SMS/IVR accessibility | SMS/IVR and KCC-style multilingual support reach non-smartphone users [47]. | Sending 10-50MB adapter binaries through SMS. | SMS/IVR carry advisories and update notices only. |
| Offline mesh | Nearby Connections supports offline P2P transfer [26]. | A diagram labelled "mesh" without store-and-forward, identity, signature, expiry or rollback semantics. | Demo an interrupted, resumed, verified transfer. |
| Android federation | Flower has a concrete Java/TFLite/WorkManager example [34]. | Claiming this proves heterogeneous 1-4B federated QLoRA. | Federate only a small classifier/statistic in the prototype. |
| Privacy | Secure aggregation can hide individual updates inside an aggregate [42]. | "Federated means private" or "no compliance work is needed." | Add minimization, consent, DP, cohort thresholds, clipping and retention rules. |
| Fleet precedent | Gboard demonstrates large-scale federated orchestration [43]. | Calling Gboard a continuous on-device LLM fine-tuning deployment. | Use it as an orchestration case study, not an LLM case study. |
| On-device online ML | Hoeffding trees update one sample at a time and can enforce memory limits [35]. | Phone-side daily 3B QLoRA while farmers use the device. | Put classical adaptation on phone CPU; put LLM optimization on server. |
| Agronomy generation | An LLM can translate or explain a retrieved approved action. | Letting a generative model independently decide chemical, evacuation or recovery policy. | Deterministic policy first, generation second. |

### Case study 1 - Gboard shows the orchestration pattern, not the LLM claim

Google's Gboard work is the strongest public fleet analogy because it describes commercial train, evaluate and deploy operations without directly centralizing device data [43]. It also uses device eligibility conditions such as idle, charging and free wireless [20], which directly informs this project's update scheduler.

The boundary matters: the reported production task was logistic click prediction rather than LoRA on a multi-billion-parameter model [43]. The correct lesson is to copy cohort selection, versioned evaluation, eligibility constraints and cautious rollout. It does not justify claiming that farmer phones can continuously fine-tune a local LLM.

### Case study 2 - Flower proves Android federation only at small-model scale

Flower's Android example combines Java, TensorFlow Lite and WorkManager with a Python aggregation server [34]. That is enough to demonstrate a federated classifier for a hackathon: for example, phones could update a tiny model that predicts whether a sensor episode warrants human review.

The same evidence also exposes the limit. The example uses CIFAR-10-scale clients [34], and the Android SDK tutorial has a stated compatibility gap [33]. A pilot must either pin and maintain the protocol stack or implement a stable transport. It must not rename this small-model demo "federated LLM adaptation."

## 7. NOISE LOG

| Searched and discarded or constrained source | Reason |
|---|---|
| Reddit posts reporting 3B model memory figures | Model build, context length, optimizer, batch, data and wall-clock were not controlled; unsuitable for procurement or SLA claims. |
| Medium articles claiming generic "2x" or fixed 8GB requirements | Secondary claims without reproducible workload details. |
| Unsloth minimum-memory table | Retained only as a **lower-bound screening reference** [30], not as a guaranteed server configuration or training-time benchmark. |
| LIMA's 1,000 examples | Retained as evidence that quality can dominate quantity [5]; discarded as a universal daily farm-data threshold because the model and task differ. |
| FedML smartphone marketing | Retained only as a vendor-supported capability claim [24]; insufficient current Android build and production evidence for selection. |
| Generic TFF deployment pages | Useful for architecture, but not a turnkey Android client; documentation itself notes backend limitations [12]. |
| Nationwide mobile coverage headlines | Signal presence does not equal successful 50MB transfer during a cyclone. Ookla's result is retained only as broad context [3]. |
| Play Asset Delivery as a universal answer | Strong technology, but Play-dependent [25]; it does not cover unmanaged devices, non-smartphones or all offline installations. |
| Public 195MB 3B adapter artifact | Retained as a size counterexample [32], not as a typical adapter or proof of this project's expected package. |
| LoRA+ and DoRA as must-have features | Both are real research: LoRA+ reports up to about 2x speed and 1-2% performance improvement in its experiments [49], while DoRA reports improved capacity and stability without additional inference overhead [46]. They are optional experiments, not prerequisites for the prototype. |
| "Production fleet-scale continuous LLM LoRA" examples | No reviewed public source met all parts of this description: billions of parameters, continual adapter training, heterogeneous Android clients, production-scale rollout and published operational results. |
| Blockchain for adapter integrity | Discarded as decorative. Ordinary public-key signing, hashes, an append-only release log and A/B rollback solve the stated package-integrity problem more directly. |

## 8. VERDICT

### Prototype: **GO**

Build the following bounded demonstration:

1. Ingest a live or replayed IMD district/nowcast product from the documented API surface [48].
2. Add two or three cheap sensor streams and perform deterministic filtering plus one adaptive threshold or pruned BOCPD detector.
3. Use a structured farm profile and agronomist-authored pre/post-disaster action library as the authority.
4. Run a quantized **1B** model on the phone to translate, simplify and voice the selected action. Test a 3B model only on a named capable handset.
5. Fine-tune one scoped adapter on the server, ideally on a GPU with at least 12GB for the constrained 1B experiment or 24GB for 3-4B headroom. These are engineering starting points, not guarantees derived from the absolute minima [30].
6. Package the adapter under an explicit 10-50MB budget, sign it, transfer it by resumable Wi-Fi or Nearby, activate it in the alternate slot, and demonstrate rollback.
7. Send the same advisory through SMS and IVR. Demonstrate that a feature-phone farmer can receive the warning without the edge model.
8. If federation is required for judging, federate only a tiny classifier or aggregated outcome statistic using a pinned Flower example. Label it honestly as a federation proof, not federated LLM training.

A successful prototype should demonstrate one full failure drill: interrupt the adapter transfer, corrupt the package, reject it by hash/signature, remain on the previous adapter, then complete a valid resumed transfer.

### Federation component: **PARTIAL**

Flower offers the clearest path to an Android proof, but its version caveat and small educational workload prevent a production endorsement [33]. TFF is appropriate for algorithm simulation, and FedML deserves a time-boxed compatibility spike, but neither removes the need to build and maintain an Android runtime. For the first pilot, centralized opt-in, minimized outcome upload may be simpler and more auditable than federated LLM updates.

### Farmer pilot: **GATED**

Do not begin a broad pilot until all of these gates pass:

- **Agronomy:** approved rules for each crop, growth stage, hazard and pre/post-disaster phase; explicit unsafe-action exclusions.
- **Data:** consented, version-linked outcomes with action timing and exposure/confounder fields; synthetic examples clearly flagged.
- **Evaluation:** frozen real holdout, crop/hazard/language slices, forgetting tests, hallucination and unsafe-advice tests, and comparison against deterministic templates.
- **Usability:** measured Odia dialect and IVR comprehension with low-literacy participants, including noisy and stressful conditions.
- **Training operations:** measured p50/p95 daily job time, peak VRAM/RAM, energy, artifact bytes and failure recovery on selected hardware.
- **Distribution:** measured success, duration, data cost, battery use and retries for 10MB and 50MB packages across target Odisha districts and during degraded service.
- **Privacy and security:** data minimization, consent withdrawal, retention, access controls, signed provenance, poisoning defenses, user-level DP where claimed, cohort thresholds and an incident process. Secure aggregation alone is insufficient [42].
- **Release safety:** staff canary, small opt-in canary, automatic stop conditions, two-slot rollback and revocation.
- **External dependencies:** verified IMD access terms and reliability, telecom/DLT requirements, IVR capacity, and any formal KCC or extension-partner agreement.
- **Impact:** a pre-registered field evaluation showing improved timely action and, eventually, reduced loss relative to a suitable comparison group.

### Cross-cutting synthesis

The three adaptation mechanisms solve different problems. **Online statistics** have the shortest horizon and lowest cost, so they belong near sensors and should detect local change. **Phone-side profile and retrieval updates** personalize immediately without touching model weights. **Server-side LoRA/QLoRA** changes language or domain behavior only after enough trustworthy evidence has accumulated and passed regression tests.

Likewise, the delivery paths serve different populations. Smartphones can hold the quantized base and receive adapters over resumable or offline data links. Feature phones receive centrally generated SMS/IVR and require no model package. Federation may eventually reduce raw-data movement, but it adds runtime, privacy-accounting and poisoning complexity; secure aggregation protects an aggregate, not the truthfulness or safety of the updates.

The defensible architecture is therefore asymmetric: **fast and deterministic at the edge, expressive but bounded on the phone, slow and evidence-gated on the server**. Marketing collapses these horizons into "continuous learning." The prototype should instead make the separation visible and testable.

## References

1. *Bayesian Online Changepoint Detection*. https://gregorygundersen.com/blog/2019/08/13/bocd
2. *On-device training in TensorFlow Lite*. https://blog.tensorflow.org/2021/11/on-device-training-in-tensorflow-lite.html
3. *Mobile Connectivity and Its Impact on Rural India | Ookla*. https://www.ookla.com/articles/india-mobile-connectivity-1h2025
4. *TensorFlow Federated*. https://www.tensorflow.org/federated
5. *LIMA: Less Is More for Alignment - arXiv.org*. https://arxiv.org/abs/2305.11206
6. *QLoRA: Efficient Finetuning of Quantized LLMs*. https://arxiv.org/abs/2305.14314
7. *Fine-tuning LLMs Guide*. http://unsloth.ai/docs/get-started/fine-tuning-llms-guide
8. *AGROMET ADVISORY SERVICES - India Meteorological Department*. https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php
9. *HuggingFaceTB/SmolLM2-1.7B · Hugging Face*. https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B
10. *Differential Privacy in TFF | TensorFlow Federated*. https://www.tensorflow.org/federated/tutorials/federated_learning_with_differential_privacy
11. *Telecom Statistics India-2024 - Department of Telecommunication*. https://dot.gov.in/static/uploads/2025/07/f44e3a674c85aa98cd6fa881e4462b57.pdf
12. *Deployment | TensorFlow Federated*. https://www.tensorflow.org/federated/deployment
13. *Bayesian Online Changepoint Detection - arXiv.org*. https://arxiv.org/pdf/0710.3742
14. *An Empirical Study of Catastrophic Forgetting in Large ...*. https://arxiv.org/abs/2308.08747
15. *meta-llama/Llama-3.2-3B · Hugging Face*. https://huggingface.co/meta-llama/Llama-3.2-3B
16. *Private Federated Learning in Gboard*. https://arxiv.org/abs/2306.14793
17. *Bitsandbytes - Hugging Face*. https://huggingface.co/docs/transformers/en/quantization/bitsandbytes
18. *LESS: Selecting Influential Data for Targeted Instruction Tuning*. https://proceedings.mlr.press/v235/xia24c.html
19. *L4 Tensor Core GPU for AI & Graphics*. https://www.nvidia.com/en-us/data-center/l4
20. *Federated Learning: Collaborative Machine ...*. https://research.google/blog/federated-learning-collaborative-machine-learning-without-centralized-training-data
21. *GitHub - flwrlabs/flower: Flower: A Friendly Federated AI Framework · GitHub*. http://github.com/flwrlabs/flower
22. *Parameter-efficient fine-tuning*. http://huggingface.co/docs/transformers/peft
23. *Applied Federated Learning: Improving Google Keyboard Query ...*. https://ar5iv.labs.arxiv.org/html/1812.02903
24. *FEDML - The unified and scalable ML library for ...*. https://github.com/FedML-AI/FedML
25. *Other Play guides | Android Developers*. https://developer.android.com/guide/playcore/asset-delivery
26. *Overview | Nearby Connections | Google for Developers*. https://developers.google.com/nearby/connections/overview
27. *Fine-Tune LoRA Models Free on Colab and Kaggle in 2026*. https://www.mrcomputerscience.com/fine-tune-lora-models-free-on-colab-and-kaggle-in-2026
28. *Axolotl*. http://docs.axolotl.ai/
29. *QLoRA Fine-Tuning With Unsloth: 5 Steps On A Free Colab GPU*. https://technoscripts.com/python-qlora-fine-tuning
30. *Unsloth Requirements*. https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements
31. *Llama-3.2-3B-Instruct-abliterated uses 35GB VRAM (!)*. https://www.reddit.com/r/LocalLLaMA/comments/1hmbfa7/llama323binstructabliterated_uses_35gb_vram
32. *adapter_model.safetensors · AdrianFernandes/llama-3.2-3b-konkani-v2-lora at main*. https://huggingface.co/AdrianFernandes/llama-3.2-3b-konkani-v2-lora/blob/main/adapter_model.safetensors
33. *Quickstart Android - Flower Framework*. https://flower.ai/docs/framework/tutorial-quickstart-android.html
34. *flower/examples/android at main · flwrlabs/flower · GitHub*. https://github.com/flwrlabs/flower/tree/main/examples/android
35. *Incremental decision trees in river: the Hoeffding Tree case - River*. https://riverml.xyz/0.11.1/recipes/on-hoeffding-trees
36. *Concept drift - River*. https://riverml.xyz/dev/introduction/getting-started/concept-drift-detection
37. *Hotswapping adapters*. https://huggingface.co/docs/peft/main/en/package_reference/hotswap
38. *intel-extension-for-transformers/docs/qloracpu.md at main · intel/intel-extension-for-transformers · GitHub*. https://github.com/intel/intel-extension-for-transformers/blob/main/docs/qloracpu.md
39. *Model merging*. https://huggingface.co/docs/peft/en/developer_guides/model_merging
40. *Self-Instruct: Aligning Language Models with Self-Generated Instructions - ACL Anthology*. https://aclanthology.org/2023.acl-long.754
41. *AI models collapse when trained on recursively generated data | Nature*. https://www.nature.com/articles/s41586-024-07566-y
42. *eprint.iacr.org*. https://eprint.iacr.org/2017/281.pdf
43. *Applied Federated Learning: Improving Google Keyboard Query Suggestions*. https://arxiv.org/html/1812.02903
44. *TS 123 040 - V16.0.0*. https://www.etsi.org/deliver/etsi_ts/123000_123099/123040/16.00.00_60/ts_123040v160000p.pdf
45. *A Survey of Federated Learning Privacy Attacks, Defenses ... - arXiv*. https://arxiv.org/abs/2405.03636
46. *http://proceedings.mlr.press/v235/liu24bn.html*. http://proceedings.mlr.press/v235/liu24bn.html
47. *mKisan: A Portal of Government of State Base Services for ...*. https://mkisan.gov.in/Home/KCCFeature
48. *IMD API Reference*. https://api.imd.gov.in/public/api_reference.html
49. *http://proceedings.mlr.press/v235/hayou24a.html*. http://proceedings.mlr.press/v235/hayou24a.html
50. *http://arxiv.org/abs/2106.09685*. http://arxiv.org/abs/2106.09685
51. *http://arxiv.org/html/2308.08747v5*. http://arxiv.org/html/2308.08747v5
