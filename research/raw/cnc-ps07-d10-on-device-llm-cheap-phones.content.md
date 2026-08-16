# Offline Farm AI on Rs 15,000 Phones: Reality Check

**Research cut-off:** August 16, 2026. **Reliability scale:** A = official specification or directly reproducible primary evidence; B = detailed research preprint, artifact repository, or dated market listing; C = community benchmark or secondary launch report; D = unverified marketing, proposal, or repository claim.

## 1. EXECUTIVE SUMMARY

- **A small offline model is feasible, but 1B Q4 is the safe design center:** Llama 3.2 1B Q4 has a **0.81 GB model file**, while a measured quantized 1B deployment on a 16 GB OnePlus 12 used **1,921-2,255 MiB RSS**. This supports a 1B-class prototype on a 4-6 GB phone, but it does not prove reliable operation under Android memory pressure on a Rs 10,000 handset. Start with Qwen3 0.6B or a 1B Q4 model, cap context, and measure on the actual phone [38][16].

- **A 3B model is not the default for this price band:** Qwen2.5 3B and Llama 3.2 3B Q4 files are **1.93 GB** and **2.02 GB**. On the 16 GB OnePlus 12, quantized Llama 3.2 3B still consumed **3,726-4,060 MiB RSS**. A 6 GB handset may launch it, but Android, the IVR/SMS app, retrieval index, and KV cache leave too little dependable headroom for a field pilot [36][35][16].

- **Qwen3 is the strongest language-coverage candidate, not yet a validated Odia agronomist:** Qwen3 0.6B and 1.7B have 32K context and Apache 2.0 licensing; the official April 29, 2025 language list includes Hindi and "Oriya" among 119 languages and dialects. No public evidence found establishes Odia tokenizer fertility, cyclone-advisory accuracy, dialect robustness, or safe agronomic generation for these small variants. Use it to render approved advice, not to invent advice [75].

- **Llama 3.2 is the better documented Hindi fallback:** Meta lists Hindi among the eight officially supported languages for its 1B and 3B models. Odia is not listed. TinyLlama, SmolLM2, and Phi-3 Mini are English-centered, making them weak choices for an Indic-first product despite fitting some memory envelopes [8][74][71][21].

- **Peak tokens/sec is a misleading pilot metric:** On a flagship OnePlus 12, ExecuTorch measured **45.8-50.2 tok/s** for quantized Llama 3.2 1B and **18.5-19.7 tok/s** for 3B. A sustained-load study on a Galaxy S24 Ultra running Qwen2.5 1.5B through MLC-LLM measured **37.58 tok/s** initially, but throughput fell to **25.31 tok/s by iteration 3**, a 37.3% decline from peak. Neither result is a benchmark of a sub-Rs 15,000 phone [16][76].

- **Use llama.cpp or ExecuTorch, not MediaPipe, as the prototype base:** llama.cpp supplies an Android example and broad GGUF portability. ExecuTorch supplies a documented AAR, Maven installation, XNNPACK CPU support, and optional Qualcomm, MediaTek, and Vulkan backends. MediaPipe LLM Inference is maintenance-only, is optimized for Pixel 8/Samsung S23-class hardware, and Google recommends migration to LiteRT-LM [39][41][28].

- **Phone-side adaptation should mean data adaptation, not continuous weight training:** Local rule JSON, retrieval, farm-state updates, prompt selection, and small online statistical models are realistic. MediaPipe's Android LoRA facility loads a pre-trained static adapter and requires GPU inference; it is not on-phone training. MobiLLM's 1.3B experiment required about **4.49 GB on the edge device plus an A100 server**, demonstrating why real-time LLM fine-tuning is not a cheap-phone feature [28][62].

- **The agricultural deployment precedent is adjacent, not equivalent:** FarmerChat documents a real agricultural assistant distributed through Google Play, while Indian systems such as Kisan Call Centres and Kisan Sarathi validate multilingual phone-based advisory delivery. None of the sources found documents a deployed, offline, on-phone LLM producing cyclone/flood advice for Odisha [60][48][64][56].

- **Decision:** The **prototype is GO** if the LLM is a bounded language layer over IMD data and reviewed rules. The **pilot is GATED** on Odia evaluation, target-phone sustained benchmarks, agronomic safety, offline voice testing, and signed update operations. The overall concept is therefore **PARTIAL**, not because offline inference is fictional, but because the unmeasured parts are exactly the parts that determine field reliability.

## 2. DATA INVENTORY

### Model inventory: what fits and what serves Hindi/Odia

"Fits" below means an engineering candidate based on artifact size and available runtime evidence. It does not mean a named cheap handset has passed sustained testing.

| Item | Named source, URL + date | Spec or measured fact | Feasibility for India | Grade |
|---|---|---|---|---|
| **Qwen3 0.6B** | Qwen, https://qwenlm.github.io/blog/qwen3/, 2025-04-29 | 0.6B, 32K context, Apache 2.0; official list includes Hindi and Oriya [75] | **Best first Odia candidate**, but use non-thinking mode and approved retrieval; Q4 size and Odia task quality still need measurement | A for spec, C for Odia readiness |
| **Qwen3 1.7B** | Same Qwen source, 2025-04-29 | 1.7B, 32K, Apache 2.0; same 119-language claim [75] | Candidate for a 6 GB phone only after profiling; potentially better quality than 0.6B but more memory and heat | A/C |
| **Gemma 3 1B IT** | Google model card, https://huggingface.co/google/gemma-3-1b-it, accessed 2026-08-16 | 1.0B; 32K input; Q4_K_M **0.81 GB**, Q8_0 **1.07 GB** [44][40] | Good compact fallback. The family claims 140+ languages, but Hindi and Odia are not individually documented for this 1B checkpoint [44] | A for spec, B for GGUF, C for Indic fit |
| **Llama 3.2 1B** | Meta model card, https://huggingface.co/meta-llama/Llama-3.2-1B, 2024-09-25 | 1.23B; Hindi officially supported; Q4_K_M **0.81 GB**, Q8_0 **1.32 GB** [8][38] | **Best documented Hindi option** and strong 4-6 GB prototype candidate; no official Odia support | A/B |
| **Qwen2.5 1.5B** | Qwen, https://qwen.ai/blog?id=qwen2.5-llm, 2024-09-18 | 1.54B, 32K; Q4_K_M **0.99 GB**, Q8_0 **1.65 GB**; positioned for edge use [11][42] | Plausible on 6 GB at Q4. Qwen2.5's cited language list does not establish Hindi or Odia quality | A/B for engineering, C for Indic fit |
| **SmolLM2 1.7B Instruct** | Hugging Face, https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct, 2025-02-04 | 1.7B, Apache 2.0, Q4_K_M **1.71 GB**, Q8_0 **2.78 GB**; primarily English [74][37] | Can fit a 6 GB test device at Q4, but language fit is poor for this problem | A/B, India grade D |
| **Gemma 2 2B IT** | Google model card, https://huggingface.co/google/gemma-2-2b-it, accessed 2026-08-16 | English-oriented card; MediaPipe lists Gemma 2 2B as supported [67][29] | Technically testable at Q4 on 6 GB, but superseded by Gemma 3 1B for this memory budget; exact selected GGUF size was not independently captured | B engineering, D Indic |
| **Llama 3.2 3B** | Meta model card and bartowski artifact, 2024-09-25/accessed 2026-08-16 | 3.21B; Q4_K_M **2.02 GB**, Q8_0 **3.42 GB** [8][35] | Hindi capable, but **not a safe 4 GB choice**; 6 GB remains a benchmark-only option because measured runtime RSS approaches 4 GB | A/B |
| **Qwen2.5 3B** | Qwen and bartowski artifact, 2024-09-18/accessed 2026-08-16 | 3.09B; Q4_K_M **1.93 GB**, Q8_0 **3.29 GB** [11][36] | Similar constraint to Llama 3B. Q4 may launch on 6 GB, but sustained pilot viability is unproved | A/B engineering, C Indic |
| **Phi-3 Mini** | Microsoft, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, 2024-06 | 3.8B, 4K; Q4_K_M **2.39 GB**, Q8_0 **4.06 GB**; primarily English [21][33] | **Reject for this use case:** too large for the quality/language trade-off on 4-6 GB phones | A/B, India grade D |
| **TinyLlama 1.1B Chat** | TinyLlama, https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0, training began 2023-09-01 | 1.1B, Apache 2.0, compact; English tagged [71] | Useful only as a speed/UI plumbing baseline; not an Odia advisory model | A spec, India grade D |

**Takeaway:** Select **Qwen3 0.6B non-thinking** for the first Odia experiment and **Llama 3.2 1B Q4** as the Hindi/control model. Gemma 3 1B is the third candidate. Do not spend the prototype cycle optimizing every listed model.

### Quantization, memory, speed, heat, and battery

| Item | Named source, URL + date | Spec or result | Feasibility for India | Grade |
|---|---|---|---|---|
| Q4 vs Q8 files | Hugging Face GGUF artifact repositories, accessed 2026-08-16 | Verified examples range from **0.81 GB Q4 / 1.07 GB Q8** for Gemma 3 1B to **2.39 GB Q4 / 4.06 GB Q8** for Phi-3 Mini [40][33] | Q4 is the practical phone baseline. File size is **not runtime RAM** | B |
| 1B runtime RSS and speed | ExecuTorch Llama benchmark, https://github.com/pytorch/executorch/blob/main/examples/models/llama/README.md, accessed 2026-08-16 | OnePlus 12: SpinQuant **50.2 tok/s, 1,921 MiB RSS**; QAT+LoRA **45.8 tok/s, 2,255 MiB RSS** [16] | Strong proof of mobile execution, but on a 16 GB flagship, not a cheap phone | A for device result, C for extrapolation |
| 3B runtime RSS and speed | Same ExecuTorch source | OnePlus 12: SpinQuant **19.7 tok/s, 3,726 MiB RSS**; QAT+LoRA **18.5 tok/s, 4,060 MiB RSS** [16] | Shows why a 3B model is risky on a 6 GB phone and unsuitable for 4 GB | A/C |
| Sustained heat | 2026 arXiv study, https://arxiv.org/html/2603.23640v1, 2026-03-24 | Galaxy S24 Ultra, Qwen2.5 1.5B, MLC-LLM: first two iterations averaged **37.58 tok/s**, then **25.31 tok/s** by iteration 3 [76] | Proves warm behavior matters; a cheaper passive-cooling design must be expected to throttle, but its amount is unknown | B |
| Energy evidence | Raspberry Pi 4 quantization study, https://arxiv.org/html/2504.03360v1, 2025-04-04 | Across its tested models, q3/q4 cut energy by up to **79%** and quantization reduced latency by up to **69%**, with diminishing benefits at extreme precision [77] | Supports Q4 direction only; not a phone battery benchmark | B, transfer grade C |
| Battery drain on target phones | No qualifying public source | No watt-hour/query, percent battery/hour, or hot-weather Odisha result for the named cheap handsets | Must be measured in the pilot gate | D/no coverage |

**Takeaway:** Publish no cheap-phone tokens/sec number until it is measured. A flagship result is an upper-bound reference, not a price-tier prediction.

### Offline Android stacks

| Stack | Named source, URL + date | Android reality | No-Play/APK implications | Grade |
|---|---|---|---|---|
| **llama.cpp** | https://github.com/ggml-org/llama.cpp/blob/master/docs/android.md, accessed 2026-08-16 | Android Studio example; GGUF portability; automatic compatible CPU-kernel selection [39] | Source-built or sideloaded deployment is possible. No stable apples-to-apples APK-size figure was found | A |
| **ExecuTorch** | https://docs.pytorch.org/executorch/stable/using-executorch-android.html, accessed 2026-08-16 | Maven or direct AAR; Java/Kotlin binding; XNNPACK, Vulkan, Qualcomm AI Engine, and MediaTek NeuroPilot options [41] | Direct AAR and local `.pte` files support controlled distribution; package size is not stated [41] | A |
| **MLC-LLM/MLCChat** | https://llm.mlc.ai/docs/deploy/android.html, documentation version 0.1.0 | Requires Android Studio, NDK, CMake, Rust, and JDK; demo targeted Samsung S23; physical GPU required [73] | Weights normally download from Hugging Face, but `bundle_weight` can place them on-device; core Java binding is about 60 KB, not the full APK/model [73] | A for workflow, C for cheap phones |
| **MediaPipe LLM Inference** | https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/android, accessed 2026-08-16 | Completely on-device inference, but optimized for Pixel 8/Samsung S23 or later and now maintenance-only [28] | Google says the model is too large to bundle in the APK; deployment normally downloads it. Static LoRA inference is GPU-only [28] | A, suitability D |

**Stack decision:** Use **llama.cpp first** for rapid GGUF comparison and a fully controlled offline build. Use **ExecuTorch second** if the team can freeze one model and invest in export plus backend-specific optimization. Keep MLC as a flagship benchmark path, not the cheap-phone default. Do not start a new product on maintenance-only MediaPipe.

### Phone-side adaptation and deployment precedents

| Item | Named source, URL + date | Evidence | Feasibility | Grade |
|---|---|---|---|---|
| Static LoRA at inference | Google MediaPipe Android guide, accessed 2026-08-16 | Loads an already trained adapter during initialization; GPU required [28] | Possible, but adapter training belongs on the server | A |
| MobiLLM | https://arxiv.org/html/2502.20421v1, 2025 | OPT-1.3B used about **4.49 GB** on Jetson Xavier NX and offloaded adapter backpropagation to an A100 server; slower links added overhead [62] | Research evidence for split learning, not offline Android fine-tuning | B |
| PocketLLM | https://aclanthology.org/2024.privatenlp-1.10, 2024 | Demonstrated research-stage on-device personalization on an OPPO Reno 6, but not a production agriculture stack [49] | Interesting future work; not a prototype dependency | B/C |
| FarmerChat | https://www.farmerchat.io/, accessed 2026-08-16 | Real agricultural AI assistant with Google Play distribution [60] | Validates user demand and language/voice UX, but does not establish offline phone inference | B |
| Government delivery analogues | http://dackkms.gov.in/account/aboutus.aspx and https://kisansarathi.in/, accessed 2026-08-16 | Kisan Call Centres and Kisan Sarathi provide real farmer advisory channels [48][64][56] | Strong channel precedent; not evidence for on-device LLM generation | A |
| Odisha on-device LLM deployment | No qualifying paper or official report found | No measured deployment matching offline phone LLM + Odisha agriculture + cyclone/flood + SMS/IVR | Treat as a new pilot, not a proven replication | D/no coverage |

### Concrete phone price list

| Phone and price evidence | Physical hardware | Model recommendation | Honest speed statement | Grade |
|---|---|---|---|---|
| **Lava Blaze 3 5G, Rs 10,999**, listed in stock on 2026-08-10; https://www.cashify.in/lava-blaze-3-5g-price-in-india [61] | 6 GB/128 GB, Dimensity 6300, 5,000 mAh [61] | Qwen3 0.6B Q4 first; then Gemma 3 1B or Llama 3.2 1B Q4. Qwen2.5 1.5B Q4 is a stretch test. Do not select 3B for the pilot | **No public model-specific tok/s result found for this phone** | B price/spec; D speed |
| **Moto G45 5G 8 GB/128 GB, Rs 12,999 launch price** on 2024-08-21; https://www.financialexpress.com/life/technology/moto-g45-affordable-5g-phone-with-snapdragon-6s-gen-3-launched-in-india-for-rs-10999-full-details-3588544 [24] | Snapdragon 6s Gen 3, 5,000 mAh [24] | Same 0.6B-1.5B Q4 set; 3B only as a non-pilot experiment | **No current price confirmation and no public LLM tok/s result found** | C price; D speed |
| **OnePlus 12 reference device, outside budget** | 16 GB flagship test platform [16] | Llama 3.2 1B/3B quantized | 1B **45.8-50.2 tok/s**; 3B **18.5-19.7 tok/s** [16] | A benchmark, not price-tier evidence |

**Takeaway:** The price list exposes the core market gap: affordable 6 GB hardware exists, and mobile LLM execution exists, but public evidence does not connect the two. The prototype team must create that missing benchmark.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---:|---|---|
| Official model cards and release blogs | 8+ model families | Language counts often apply to a family, not the small checkpoint; almost no Odia task scores or tokenizer measurements | **B** |
| Direct GGUF artifact repositories | 7 exact Q4/Q8 pairs | Third-party conversions; file size only, not RSS, speed, heat, or quality | **B** |
| Official Android runtime documentation | All 4 requested stacks | APK-size reporting is inconsistent; NPU support is device/export specific | **A-** |
| Reproducible mobile benchmarks | OnePlus 12 ExecuTorch, S24 Ultra MLC, experimental Snapdragon results | Nearly all use flagships; no sub-Rs 15,000 device; battery data sparse | **C+** for target decision |
| Indic-language benchmarks | Hindi coverage and broad multilingual claims | Odia is absent from the principal benchmark hit; tokenizer fertility and agronomic safety are unmeasured | **D** for Odia |
| Thermal and energy studies | One sustained flagship study plus edge quantization studies | No Odisha ambient-temperature test, low-cost SoC test, or battery-aging analysis | **C** |
| India phone price/spec sources | One current 6 GB in-stock listing; additional launch/near-miss listings | Prices change, listings go out of stock, and sellers do not benchmark LLMs | **C** |
| Agriculture and rural-delivery deployments | FarmerChat plus government call/advisory systems | Cloud/app delivery is frequently described as "low connectivity" without proving offline inference | **B** for channels, **D** for on-device LLM |
| Hackathon repositories and product pages | Many feature claims | No field protocol, agronomic audit, target-phone benchmark, or measured outcome | **D** |

The coverage is strong enough to choose a prototype architecture, but too weak to claim a deployment-ready Odia edge-LLM product. The largest evidence deficit is not model availability; it is the intersection of **cheap hardware, sustained use, Odia, agronomic safety, and rural delivery**.

## 4. WHAT IS MISSING

1. **Target-device benchmark:** No public source found tests Lava Blaze 3 5G, Moto G45 5G, or an equivalent sub-Rs 15,000 4-6 GB handset with Qwen3 0.6B/1.7B, Gemma 3 1B, Llama 3.2 1B, or Qwen2.5 1.5B under the same prompt, context, runtime, and quantization.

2. **Sustained thermal and battery curve:** Missing measurements include cold and warm tok/s, time-to-first-token, peak RSS, process-kill rate, skin and SoC temperature, watt-hours per 100 generated tokens, battery percentage per advisory, and behavior at 35-45 C ambient temperature. The flagship evidence already shows a 37.3% throughput drop by the third sustained iteration, so this is a gating test, not optional polish [76].

3. **Odia tokenizer and quality evidence:** Qwen3's official list includes Oriya, but there is no published comparison here of tokens per Odia character/word, code-mixed Odia-English-Hindi behavior, dialect coverage, agronomic terminology, hallucination rate, or SMS-length fidelity for 0.6B-3B models [75].

4. **Offline speech evidence:** The research did not establish a production-quality, fully offline Odia ASR/TTS stack that fits beside the LLM on 4-6 GB RAM. IVR itself also needs a telecom path even when advisory generation is offline.

5. **End-to-end APK/storage budget:** Official docs explain AARs, native libraries, and model delivery, but do not provide a comparable final APK, installed size, first-run download, and update delta for all four stacks. MediaPipe explicitly says its model is too large for APK bundling [28].

6. **Agronomic ground truth:** No public corpus was found mapping IMD alert severity, Odisha district, crop, variety, sowing date, soil/drainage, flood depth, and growth stage to approved pre-disaster and recovery actions with validity dates and responsible agronomists.

7. **Field outcome evidence:** No qualifying deployment reports crop-loss reduction, avoided input cost, warning lead-time utilization, comprehension by low-literacy farmers, or false-advice harm for an on-phone LLM system in Odisha.

8. **Operational governance:** Missing public evidence covers signed model/rule updates, rollback, device loss, consent, farmer-data deletion, audit logs, model drift, and who is legally accountable when an automatically generated advisory conflicts with an official recommendation.

These gaps should become the pilot test plan. They should not be filled with estimated tokens/sec, generic multilingual benchmark scores, or claims that a model "supports Odia" merely because its tokenizer accepts Odia characters.

## 5. HOW IT FEEDS THE EDGE-AI ENGINE

| Tier | What should run there | Predictive statistic or evidence mechanism | Decision powered |
|---|---|---|---|
| **Sensor node** | Rain gauge, water-level, soil-moisture and optional wind sensors; timestamping; median/outlier filtering; store-and-forward radio | Rolling median, rate-of-rise, missingness score, sensor-health bounds, and event threshold | Is the reading credible? Is water/rain rising fast enough to escalate? Send only compact observations, not prose |
| **Phone hub** | Farm profile, cached IMD warning, local rule JSON/SQLite, retrieval, small Q4 LLM, approved Odia/Hindi templates, queue for SMS/IVR | Risk score from official alert severity + local trend + crop stage + vulnerability; confidence and data-freshness flags | Which reviewed action applies now? Which language/channel and message length should be used? Should uncertain cases fall back to a fixed warning? |
| **Learning server** | Data validation, agronomist labeling, evaluation, model/rule versioning, adapter training, fleet telemetry and signed update production | Calibration curves, false-negative cost, district/crop error slices, drift tests, A/B comprehension outcomes | Is a new rule/model safer than the previous version? Which signed bundle should be released or rolled back? |

### Sensor node: statistics before language

A sensor node should not host an LLM. It should produce compact, inspectable evidence: current level, recent change, missing samples, battery state, and a quality flag. A robust median or Hampel-style filter can suppress a single bad reading; an exponentially weighted trend can detect rapid rise without storing a long history. These are design recommendations, not claims that an LLM predicts floods.

The phone should fuse this evidence with the official IMD product. IMD's API catalog includes city forecasts, subdivision rainfall forecasts, state/district rainfall forecasts, and all-India forecast bulletins [65]. For a safety system, the official alert remains authoritative; a sensor can escalate urgency or flag local divergence, but it must not silently downgrade an IMD warning.

### Phone hub: deterministic decision, generative rendering

The phone's primary decision engine should be a versioned policy table keyed by hazard, district, crop, growth stage, lead time, and known farm vulnerabilities. Retrieval selects the applicable reviewed actions. The small LLM then performs bounded transformations: simplify, translate, personalize quantities already present in the rule, create a short SMS, and create an IVR script.

For Odia, the first prototype should compare Qwen3 0.6B against fixed human-authored templates. Qwen3's language list supports testing it, but not trusting it [75]. Any missing field, stale IMD timestamp, low sensor quality, or retrieval miss should force a safe template rather than open-ended generation.

### Learning server: continuous learning without continuous phone training

The server can fine-tune or train after agronomist review, regression testing, and holdout evaluation. It can ship a signed Q4 model, static LoRA adapter, retrieval pack, or classical-model coefficients during connectivity windows. The phone "adapts" by updating farm state, retrieval ranking, user language, delivery success, and possibly a tiny calibrated risk model.

This architecture respects the physics. MobiLLM's ostensibly mobile 1.3B tuning still used roughly 4.49 GB at the edge and an A100 server [62]. In contrast, loading an already trained adapter at inference is supported, although MediaPipe restricts that LoRA path to GPU [28].

## 6. REAL-vs-FILLER

| Classification | Feature | Evidence-based judgment |
|---|---|---|
| **REAL** | Cache official IMD forecast/warning products | Official API catalog exists; integration and access testing are still required [65] |
| **REAL** | Sensor-assisted local escalation | Cheap numerical filtering and trend detection do not need an LLM and remain inspectable |
| **REAL** | Q4 0.6B-1.5B offline inference | Model artifacts fit within roughly 0.8-1.7 GB; 1B mobile execution is directly demonstrated on a flagship [38][42][16] |
| **REAL** | Local retrieval over reviewed JSON/SQLite | Retrieval reduces the generation problem to selecting and rendering known actions; it is compatible with all four runtime approaches |
| **REAL** | Hindi rendering with Llama 3.2 1B | Hindi is officially supported [8] |
| **REAL BUT GATED** | Odia rendering with Qwen3 | Oriya appears in the official 119-language list, but quality and tokenizer efficiency are unmeasured [75] |
| **REAL BUT GATED** | Server-trained static LoRA | Android can load a static adapter for inference; training remains server-side [28] |
| **REAL BUT GATED** | SMS and IVR delivery | India has operational farmer advisory channels, but automated telecom integration, consent, retry policy, and Odia voice testing remain project work [48][64] |
| **FILLER** | "Continuous on-phone LLM fine-tuning" | Available evidence is research-stage, memory-heavy, or server-assisted; it is not an offline cheap-phone production capability [62] |
| **FILLER** | "3B runs on 6 GB, therefore it is pilot-ready" | The measured 3B quantized process uses 3.7-4.1 GB RSS on a 16 GB phone before accounting for the rest of the application [16] |
| **FILLER** | "Q8 is always more accurate and therefore better" | Q8 files often consume most of the practical budget; the application also needs KV cache, runtime buffers, retrieval, speech, and Android headroom |
| **FILLER** | "NPU acceleration works on every Android phone" | ExecuTorch documents hardware-specific Qualcomm and MediaTek backends and recommends XNNPACK for compatibility first [41] |
| **FILLER** | "The model can live inside a normal APK" | Google explicitly says the MediaPipe model is too large to bundle in the APK [28] |
| **FILLER** | "Low-connectivity agriculture app equals on-device LLM deployment" | FarmerChat's Google Play presence proves a deployed app, not offline local inference [60] |

The genuinely useful innovation is not "a chatbot on every sensor." It is a resilient decision chain in which official alerts and local measurements choose reviewed actions, a small model improves accessibility, and every uncertain case degrades to a safe deterministic message.

## 7. NOISE LOG

| Searched and discarded | Reason for rejection |
|---|---|
| SmartKhet/Axora and hackathon repositories claiming production readiness | Feature lists and large farmer-market claims were not accompanied by field evaluation, target-device benchmarks, or evidence of deployed offline inference |
| Student repositories combining app + SMS + IVR + offline AI | Useful for UI ideas, but not evidence for reliability, model performance, or farmer outcomes |
| MediaPipe demo success as proof for cheap phones | Official guidance targets Pixel 8 and Samsung S23 or later, not entry-level hardware [28] |
| Experimental Snapdragon Hexagon result around 51.5 tok/s | The exact consumer device/SoC and thermal behavior were not specified, and the backend was labeled experimental [12] |
| Flagship Android benchmark ranges without a named phone or RAM | Helpful only as an upper bound; not used to assign speed to the price-list phones |
| Apple Silicon runtime comparisons | MLX, MLC, llama.cpp, Ollama, and PyTorch MPS results on a 192 GB M2 Ultra do not answer the cheap-Android question [78] |
| Raspberry Pi 4 energy results presented as phone battery results | Retained only as directional quantization evidence; the test platform was a 4 GB Raspberry Pi 4, not Android [77] |
| IndicMMLU-Pro as an Odia validation source | Its covered-language set did not resolve the requested Odia evidence gap; no Odia tokenizer-fertility comparison was found |
| Generic multilingual labels and tokenizer acceptance | A model emitting Odia Unicode text does not establish comprehension, terminology accuracy, or safe advice |
| Launch prices treated as current prices | Moto G45 is explicitly labeled a 2024 launch-price reference; current price and stock remain unverified [24] |
| Model-file size treated as RAM use | GGUF repositories explicitly separate file size from the RAM/VRAM needed to run the model [42] |
| "LoRA support" treated as on-phone training | The documented Android path loads static LoRA weights for inference [28] |

## 8. VERDICT: GO / PARTIAL / GATED

### Prototype verdict: **GO, with a narrow evidence-faithful scope**

A convincing prototype can run on a 6 GB Lava Blaze 3 5G-class phone if it demonstrates: cached IMD data; synthetic or real sensor events; farm-profile retrieval; a deterministic pre/post-disaster rule pack; Qwen3 0.6B or Llama 3.2 1B Q4 for bounded message rendering; an Odia/Hindi template fallback; and queued SMS/IVR output. The prototype should display model load time, peak RSS, cold and warm tok/s, temperature, and battery change rather than hiding them.

The demo should not train LLM weights. It can show the truthful learning loop: feedback is logged locally, uploaded when connected, reviewed and trained on the server, and returned as a signed rule/model/adapter update. This preserves the requested continuous-learning story without claiming impossible real-time weight adaptation.

### Pilot verdict: **GATED**

A farmer-facing pilot should not begin until five gates pass:

1. **Hardware:** at least two sub-Rs 15,000 models complete 20 consecutive advisories without process death, unsafe temperature, or unacceptable battery drain.
2. **Language:** native Odia reviewers test comprehension, dialects, numerals, crop terminology, code-mixing, and SMS/IVR rendering; Qwen3 must beat or at least safely match fixed templates.
3. **Agronomy:** every generated action traces to a dated, approved source rule; unsupported generation and downgrading of official alerts are blocked.
4. **Operations:** signed updates, rollback, offline expiry, duplicate suppression, consent, delivery receipts, and escalation to a human advisor work under intermittent connectivity.
5. **Outcomes:** the pilot measures warning receipt, comprehension, action taken, false alarms, unsafe advice, time saved, and crop-loss proxies, not only model speed.

### Synthesis: why the overall verdict is **PARTIAL**

| Dimension | Sensor-first deterministic system | 1B Q4 phone hub | 3B/Q8 phone-first system | Server-assisted learning |
|---|---|---|---|---|
| Mechanism | Thresholds, trends, official alerts, reviewed rules | Retrieves and renders bounded advice | Relies more heavily on free-form model capability | Trains/evaluates centrally and ships controlled updates |
| Evidence base | Strong and inspectable | Mobile execution proven, cheap-phone intersection missing | Flagship-only memory/speed makes affordability claim weak | Technically conventional; MobiLLM shows why heavy adaptation belongs off-phone |
| Primary benefit | Safety and explainability | Accessibility, personalization, offline continuity | Potentially better prose/reasoning | Governance, quality improvement, rollback |
| Main trade-off | Less conversational flexibility | Limited reasoning and Odia uncertainty | RAM, heat, battery, process-kill and deployment complexity | Needs periodic connectivity and operations discipline |
| Recommended horizon | Prototype and pilot | Prototype now; pilot after gates | Research demonstration only | Build from day one |

The non-obvious conclusion is that the LLM is **not** the predictive core. The predictive core is the fusion of official alert severity, sensor quality and trend, farm vulnerability, crop stage, and a calibrated action policy. The LLM is the accessibility layer that converts an already selected action into concise Hindi/Odia SMS and IVR text.

That division turns the project from a decorative "edge-AI mesh" into a defensible resilience system. It also makes failure graceful: if the model cannot load, overheats, or produces low-confidence text, the phone can still deliver the fixed official warning and reviewed action template.

## References

1. [
      Page Not Found
    ](https://www.amazon.com/bedrock/latest/userguide/model-card-meta-llama-3-2-1b-instruct.html)
2. *IndicMMLU-Pro: Benchmarking Indic Large Language Models on Multi-Task Language Understanding - Ashutosh Kumar's Portfolio*. https://ashu1069.github.io/indicmmlu-pro.html
3. *IndicMMLU-Pro: Benchmarking Indic Large Language Models on Multi-Task Language Understanding*. https://arxiv.org/abs/2501.15747
4. *executorch/extension/benchmark/android/benchmark at main · pytorch/executorch · GitHub*. https://github.com/pytorch/executorch/tree/main/extension/benchmark/android/benchmark
5. *IndicMMLU-Pro: Benchmarking Indic Large Language Models on Multi-Task Language Understanding - The Aula Fellowship - Think Tank and NGO*. https://theaulafellowship.org/2025/01/01/indicmmlu-pro-benchmarking-indic-large-language-models-on-multi-task-language-understanding
6. *MLC LLM | Home*. https://llm.mlc.ai/
7. *llama.cpp/tools/server/README.md at master · ggml-org/llama.cpp · GitHub*. https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
8. *meta-llama/Llama-3.2-1B · Hugging Face*. https://huggingface.co/meta-llama/Llama-3.2-1B
9. *What Is llama.cpp? Run GGUF Models Locally | explainx.ai Blog | explainx.ai*. https://explainx.ai/blog/what-is-llama-cpp-run-models-locally-2026
10. *GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub*. https://github.com/ggml-org/llama.cpp
11. *Qwen*. https://qwen.ai/blog?id=qwen2.5-llm
12. *benchmarks-llama.cpp/docs/backend/snapdragon/README.md at benchmarks · Liquid4All/benchmarks-llama.cpp · GitHub*. https://github.com/Liquid4All/benchmarks-llama.cpp/blob/benchmarks/docs/backend/snapdragon/README.md
13. *On-Device LLMs on Android in 2026: ExecuTorch, llama.cpp, and MNN Compared | AlephZero Labs Blog*. https://www.alephzerolabs.com/blog/on-device-llm-android-native-2026
14. *Performance of llama.cpp on Android device · ggml-org/llama.cpp · Discussion #14356 · GitHub*. https://github.com/ggml-org/llama.cpp/discussions/14356
15. *IndicMMLU-Pro: Benchmarking the Indic Large Language Models*. https://arxiv.org/html/2501.15747v1
16. *executorch/examples/models/llama/README.md at main · pytorch/executorch · GitHub*. https://github.com/pytorch/executorch/blob/main/examples/models/llama/README.md
17. *AI Model Catalog | Microsoft Foundry Models*. https://ai.azure.com/catalog/models/Phi-3-mini-4k-instruct
18. *AIKosh*. https://aikosh.indiaai.gov.in/home/use-cases/details/farmerchat_ai_powered_agricultural_advisory_at_scale.html
19. *Home | Krishimitra*. https://www.krishimitra.org/
20. *Empowering Farmers for Sustainable Practices and Carbon Credit Programs | Krishi Mithra*. https://krishimithra.com/
21. *microsoft/Phi-3-mini-4k-instruct · Hugging Face*. https://huggingface.co/microsoft/Phi-3-mini-4k-instruct
22. *Redmi 15 5G Phone Price, Specs, Comparison and Reviews (14th July 2026) | Gadgets 360*. https://www.gadgets360.com/redmi-15-5g-price-in-india-134052
23. *microsoft/Phi-3-mini-128k-instruct · Hugging Face*. https://huggingface.co/microsoft/Phi-3-mini-128k-instruct
24. *Moto G45 affordable 5G phone with Snapdragon 6s Gen 3 launched in India for Rs 10,999 – full details - Technology News | The Financial Express*. https://www.financialexpress.com/life/technology-moto-g45-affordable-5g-phone-with-snapdragon-6s-gen-3-launched-in-india-for-rs-10999-full-details-3588544
25. *Gemma 3n model overview  |  Google AI for Developers*. https://ai.google.dev/gemma/docs/gemma-3n
26. *CMF Phone (1) Price in India 2026, Specs & Features | Smartprix*. https://www.smartprix.com/mobiles/cmf-phone-1-ppd1l8h88mjl
27. *microsoft/Phi-3-mini-4k-instruct-gguf · Hugging Face*. https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf
28. *LLM Inference guide for Android  |  Google AI Edge  |  Google AI for Developers*. https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/android
29. *LLM Inference guide  |  Google AI Edge  |  Google for Developers*. https://developers.google.com/edge/mediapipe/solutions/genai/llm_inference
30. *mediapipe-samples/examples/llm_inference/android/README.md at main · google-ai-edge/mediapipe-samples · GitHub*. https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/llm_inference/android/README.md
31. *GitHub - mlc-ai/docs: The documents for TVM Unity*. https://github.com/mlc-ai/docs
32. *Maven Repository: org.pytorch » executorch-android*. https://mvnrepository.com/artifact/org.pytorch/executorch-android
33. *bartowski/Phi-3-mini-4k-instruct-GGUF · Hugging Face*. https://huggingface.co/bartowski/Phi-3-mini-4k-instruct-GGUF
34. *Maven Repository: org.pytorch » executorch-android*. https://mvnrepository.com/artifact/org.pytorch/executorch-android?sort=date
35. *bartowski/Llama-3.2-3B-Instruct-GGUF · Hugging Face*. https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF
36. *bartowski/Qwen2.5-3B-Instruct-GGUF · Hugging Face*. https://huggingface.co/bartowski/Qwen2.5-3B-Instruct-GGUF
37. *bartowski/gemma-2-2b-it-GGUF · Hugging Face*. https://huggingface.co/bartowski/gemma-2-2b-it-GGUF
38. *bartowski/Llama-3.2-1B-Instruct-GGUF · Hugging Face*. https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF
39. *llama.cpp/docs/android.md at master · ggml-org/llama.cpp · GitHub*. https://github.com/ggml-org/llama.cpp/blob/master/docs/android.md
40. *bartowski/google_gemma-3-1b-it-GGUF · Hugging Face*. https://huggingface.co/bartowski/google_gemma-3-1b-it-GGUF
41. *Using ExecuTorch on Android#*. https://docs.pytorch.org/executorch/stable/using-executorch-android.html
42. *bartowski/Qwen2.5-1.5B-Instruct-GGUF · Hugging Face*. https://huggingface.co/bartowski/Qwen2.5-1.5B-Instruct-GGUF
43. *IMD API Management*. https://api.imd.gov.in/public/index.php
44. *google/gemma-3-1b-it · Hugging Face*. https://huggingface.co/google/gemma-3-1b-it
45. *google/gemma-3-4b-it · Hugging Face*. https://huggingface.co/google/gemma-3-4b-it
46. *FarmerChat: Farming answers in seconds | Digital Green*. https://www.digitalgreen.org/farmerchat
47. *Lava Blaze X 5G - Price in India (Aug 2026), Specs, Reviews | Smartprix*. https://www.smartprix.com/mobiles/lava-blaze-x-ppd13qcw1pe3
48. [
	Kisan Call center
](http://dackkms.gov.in/account/aboutus.aspx)
49. *PocketLLM: Enabling On-Device Fine-Tuning for Personalized LLMs - ACL Anthology*. https://aclanthology.org/2024.privatenlp-1.10
50. *google/gemma-3-1b-it at main*. https://huggingface.co/google/gemma-3-1b-it/tree/main
51. *Moto G35 5G Launched in India: Price, Specs, Availability*. https://themobileindian.com/news/moto-g35-5g-launched-in-india-price-specs-availability
52. *Moto G35 5G - Price in India & Full Specifications (July 2025) | Beebom*. https://gadgets.beebom.com/mobile/moto-g35-5g
53. *DW Warnings | India Meteorological Department*. https://mausam.imd.gov.in/responsive/districtWiseWarning.php
54. *Moto G35 5G India Price Range Revealed Ahead of Launch Next Week | Technology News*. https://www.gadgets360.com/mobiles/news/moto-g35-5g-price-range-india-flipkart-listing-specifications-7179641
55. *IMD APIs | India Meteorological Department*. https://mausam.imd.gov.in/responsive/apis.php
56. *Kisan Sarathi | Kisan Sarthi Helpline | Kisan Sarthi*. https://kisansarathi.in/
57. *google/gemma-3-1b-it · Hugging Face*. https://huggingface.co/google/gemma-3-1b-it?autotrain=true
58. *Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM*. https://huggingface.co/blog/gemma3
59. [
    FarmerChat: AI-Powered Agricultural Advisory  ](https://wsa-global.org/winner/farmerchat)
60. *Farmer Chat*. https://www.farmerchat.io/
61. *Lava Blaze 3 5G - Price in India, Specifications & Features | Mobile Phones*. https://www.cashify.in/lava-blaze-3-5g-price-in-india
62. *arxiv.org*. https://arxiv.org/pdf/2502.20421
63. *FarmerChat – Digital Green*. https://digitalgreen.org/farmer-chat
64. [
	Press Release Page | Press Information Bureau
](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278757&lang=1&reg=3)
65. *Api Reference*. https://api.imd.gov.in/public/api_reference.html
66. *MobiLLM: Enabling LLM Fine-Tuning on the Mobile Device via Server Assisted Side Tuning*. https://arxiv.org/html/2502.20421v1
67. *google/gemma-2-2b-it · Hugging Face*. https://huggingface.co/google/gemma-2-2b-it
68. *Releases · mlc-ai/binary-mlc-llm-libs · GitHub*. https://github.com/mlc-ai/binary-mlc-llm-libs/releases
69. *Qwen/Qwen3-0.6B · Hugging Face*. https://huggingface.co/Qwen/Qwen3-0.6B
70. *LLM Inference at the Edge: Mobile, NPU, and GPU Performance Efficiency Trade-offs Under Sustained Load*. https://arxiv.org/abs/2603.23640
71. *TinyLlama/TinyLlama-1.1B-Chat-v1.0 · Hugging Face*. https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
72. *Qwen/Qwen3-1.7B · Hugging Face*. https://huggingface.co/Qwen/Qwen3-1.7B
73. *Android SDK — mlc-llm 0.1.0 documentation*. https://llm.mlc.ai/docs/deploy/android.html
74. *HuggingFaceTB/SmolLM2-1.7B-Instruct · Hugging Face*. https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct
75. *Qwen3: Think Deeper, Act Faster | Qwen*. https://qwenlm.github.io/blog/qwen3/
76. *LLM Inference at the Edge: Mobile, NPU, and GPU Performance Efficiency Trade-offs Under Sustained Load*. https://arxiv.org/html/2603.23640v1
77. *http://arxiv.org/html/2504.03360v1*. http://arxiv.org/html/2504.03360v1
78. *http://arxiv.org/pdf/2511.05502*. http://arxiv.org/pdf/2511.05502
