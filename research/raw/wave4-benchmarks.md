## executive_summary

- **Agentic Saturation Reaches a Plateau**: AgentBench-style suites show 80% success variance across runs; HAL recommends multi-run evaluation with confidence intervals rather than point estimates for any 2026 agent demo. -> Use AgentBoard-style harnesses that report both pass@k and pass^k, not single-pass metrics.
- **SWE-bench Verified is the New Coding Litmus Test**: SWE-bench Verified (500 human-verified issues from Django/Flask/sklearn) is currently led by Claude Opus 5 at ~96% and Claude Mythos 5 at 95.5%; HumanEval is reported as saturated [90, 256]. -> If building a coding agent, target SWE-bench Verified and LiveCodeBench -- not HumanEval.
- **tau-bench Reduces Do-Nothing Agent Pass Rate by Half**: After Sierra's audit fixes, the prior "38% do-nothing airline / 6% retail" false pass was cut to negligible; leakages were 100% wrong by relative terms in older benchmarks [4-5]. -> Show trajectory-level metrics (tool calls, user turns) for any customer-service agent.
- **MTEB is Now Multilingual**: MTEB leaderboard tracks 196+ models with C-MTEB French category added; BEIR's NDCG@10 spread across zero-shot retrieval is the canonical generalization probe [61, 63]. -> Embedding work must score on MTEB and BEIR's domain-shift subsets.
- **CyberSecEval 3 is the Cybersecurity Bar**: Meta's CyberSecEval 3 (April 2024) extends CyberSecEval 2's prompt-injection and exploit-block tests; a Hacker News thread now recommends tasks ask clarifying questions, seek confirmation, handle infeasible instructions [110, 192]. -> Cyber-helper agents must pass CSE3 expectations explicitly.
- **RAGAS and ARES are Complementary**: RAGAS provides trajectory-level metrics (RAG context-relevance, faithfulness, answer-relevance), ARES auto-tunes lightweight LM judges per RAG domain using synthetic data [96, 356]. -> Combine RAGAS for fixed metrics, ARES for domain-specific fine-tuning.
- **OWASP 2025 Reorganization**: OWASP Top 10:2025 published with categories reordered around threat-agent patterns; OWASP API Security Top 10 (2023) remains canonical for fintech. -> Submit 2025 OWASP API citations explicitly in hackathon README.
- **India-Specific Compliance Stack is Converging**: DPDPA 2023 checklist + CERT-In Directions + RBI Digital Lending Directions 2025 + MeitY India AI Governance Guidelines (Nov 2025) form a 4-pillar compliance stack [70, 228, 316, 318]. -> Indian fintech/AI hackathon entries should reference all 4.
- **EU AI Act Risk Tiering Penalties Now Apply**: EU AI Act assigns applications to 3 risk categories (Unacceptable, High, Limited/Minimal) with fines under the Act effective from 2025-2026 [180, 184]. -> Any product demo for EU users must classify itself under the 3-tier scheme.
- **CWE Top 25 2025 Lists Vulnerabilities in Priority Order**: MITRE's 2025 CWE Top 25 was released; OWASP Top 10:2025 mirrors the same threat-actor reorganization [185, 188]. -> Run scoring against CWE Top 25 + OWASP 2025 jointly.
- **MITRE ATT&CK v18/v19.1 Redefines Detection**: ATT&CK v18 (Oct 2025) re-models how defenders detect adversary behavior; v19.1 (April 2026) extends further. -> Map any red-team/blue-team agent reports to ATT&CK v18+ IDs.

---

## 1_agentic_tool_use_benchmarks

### 1.1 Core Agent Evaluation Suites

| Benchmark | What it Measures | Top Score / Holder (or status) | Maintainer | URL |
|----------|-------------------|-------------------------------|-----------|-----|
| AgentBench | LLM-as-agent reasoning and decision across 8 environments | Multi-eval framework; cited by 1070+ papers | Fudan / THU / X. Liu et al. | http://arxiv.org/abs/2308.03688 |
| GAIA | General AI Assistants -- 466 questions across 3 levels | Cited 1132+; benchmark for general assistants | HuggingFace / G. Mialon et al. | http://openreview.net/forum?id=fibxvahvs3 |
| tau-bench / tau^2-bench / tau^3-bench | Tool-agent-user interaction; airline/retail | Up to ~40% overestimation before tau^3 fix [4-5] | Sierra Research | https://taubench.com/ |
| tau^3-Bench | Audited tau fixing 50+ airline/retail task issues | Updated 2025 | Sierra | https://taubench.com/blog/tau3-task-fixes.html |
| ABC Benchmark Survey | Assessed 10 agentic benchmarks for eval flaws -- up to 100% error bias | Research framework, not a benchmark | arXiv 2507.02825 | http://arxiv.org/html/2507.02825v3 |
| Holistic Agent Leaderboard (HAL) | Standardized, cost-aware, third-party agent eval | Live leaderboard; Princeton | S. Kapoor, B. Stroebl et al. | http://hal.cs.princeton.edu/ |
| Holistic Agent Leaderboard (paper) | Framework for HAL infrastructure | Research paper | Princeton/OpenReview | http://openreview.net/forum?id=vUaY1t6 (ref in prior context) |

### 1.2 Web / OS / Multimodal Agent Tasks

| Benchmark | What it Measures | Top Score / Holder | Maintainer | URL |
|----------|-------------------|-------------------|-----------|-----|
| WebArena | Functional web tasks on real sites | WebTactix (DeepSeek v3.2) 74.3%; Qwen3-235B-A22B 95.6% (separate systems) [254, 252] | CMU / Princeton | http://webshop-pnlp.github.io (related) |
| OSWorld / OSWorld-Verified | Cross-OS desktop tasks (Chrome, LibreOffice, etc.) | Claude Fable 5: 85%; Claude Mythos 5: 85%; Claude Opus 4.8: 83.4% | HKUST / SF / U Oregon | http://benchlm.ai/benchmarks/osWorldVerified (live) |
| SWE-bench Verified | 500 human-verified GitHub issue PRs | Claude Opus 5: 96%; Claude Mythos 5: 95.5%; Claude Fable 5: 95% | OpenAI + Princeton (SWE-bench team) | http://swebench.com/verified.html |
| SWE-bench Lite / Full | Original 2,294 PRs from 12 Python repos | Superseded by Verified | Original SWE-bench team | http://swebench.com/ |
| Terminal-Bench | CLI / terminal agent task suite | Live leaderboard | LAION / Tbench team | http://github.com/laude-institute/terminal-bench (referenced in prior context) |
| Mind2Web | Generalist web agent over 2,350 tasks | Original benchmark | OSU NLP Group / T. Xie et al. | https://osu-nlp-group.github.io/Mind2Web |
| Mind2Web 2 | 130 realistic long-horizon browsing tasks, agent-as-a-judge | Active in 2025 | OSU NLP Group | https://osu-nlp-group.github.io/Mind2Web-2 |
| AssistantBench | 214 realistic web tasks with time constraints | Active; web-agent benchmark | Microsoft Research (Y. Yao et al.) | https://arxiv.org/html/2407.15711v1 |
| AppWorld / AppWorld-UL | Controlled, executable app world; UL needs clarifying questions | Benchmark of day-to-day agent tasks | Stony Brook NLP / T. Trivedi | https://appworld.dev/ |
| WorkArena | 29 ServiceNow knowledge-worker tasks | ServiceNow-hosted | ServiceNow Research | https://github.com/ServiceNow/workarena |
| VisualWebArena | Multimodal web tasks (vision + DOM) | Maintenance; Fudan + Zhipu | Multimodal agent track | (referenced in prior context) |

### 1.3 Tool-Use / Function Calling

| Benchmark | What it Measures | Top Score / Holder | Maintainer | URL |
|----------|-------------------|-------------------|-----------|-----|
| BFCL (Berkeley Function Calling Leaderboard) | Serial/parallel function calls via AST eval | Live v4 leaderboard 2026 | UC Berkeley + Gorilla | http://gorilla.cs.berkeley.edu/leaderboard.html |
| BFCL v3 | Multi-turn interactions, holistic agentic eval (Apr 2026) | GPT-5-mini 2025-08-07 visible | UC Berkeley | http://gorilla.cs.berkeley.edu/leaderboard.html |
| Gorilla | LLM for API calls; original paper | Berkeley | Gorilla team | https://openreview.net/forum?id=2GmDdhBdDk |
| MetaTool | Tool-selection / awareness benchmark for LLMs | Cited 240+; benchmark eval | UC Santa Barbara + Yahoo | http://arxiv.org/abs/2310.03128 |
| API-Bank | 73-API tool-augmented LLM benchmark | Cited 689+; comprehensive tool-use | HKUST (M. Li et al.) | https://aclanthology.org/2023.emnlp-main.187 |
| ToolBench (sparse; refer to API-Bank/ToolLLM lineage) | Tool-augmented LLM benchmark | Various forks | Various (see API-Bank first) | https://arxiv.org/abs/2304.08244 |
| ToolEmu | Agent misuse via emulated tool execution; 68.8% failures valid | Cited 538+; safety eval | Yale + Microsoft | http://arxiv.org/abs/2309.15817 |
| AutoDAN | Stealthy jailbreak prompts via hierarchical GA | Cited 1423+; jailbreak method | UCSD team (X. Liu et al.) | https://arxiv.org/pdf/2310.04451 |
| AutoDAN-Turbo | Lifelong jailbreak agent from scratch | 2025 follow-up | UCSD / AI Safety | https://autodans.github.io/AutoDAN-Turbo |
| GPTFuzzer | Automated template red-teaming for LLMs | Open fuzzer framework | Fudan | https://arxiv.org/html/2309.10253v1 |
| PAIR (Prompt Automatic Iterative Refinement) | Black-box jailbreak method (used in JBB) | Used by JBB authors | NeurIPS 2024 D&B Track | https://arxiv.org/pdf/2404.01318 |

### 1.4 Autonomous Time / R&D / Multi-Agent

| Benchmark | What it Measures | Top Score / Holder | Maintainer | URL |
|----------|-------------------|-------------------|-----------|-----|
| RE-Bench | 7 ML research engineering tasks; cost-normalized | Best agents vs experts; frontier AI R&D | METR | https://arxiv.org/html/2411.15114v1 |
| MINT | Multi-turn interaction with tools + natural language feedback | Multi-turn benchmark | Stanford NLP (X. Wang) | https://xwang.dev/mint-bench |
| METR HCAST | 70-80% success on <1hr tasks, <20% on >4hr tasks | Long-horizon agent calibration | METR | https://metr.org/hcast.pdf |
| MAST | Multi-Agent Systems Failure Taxonomy; 1K+ traces | Diagnostic framework | MIT-IBM Watson + others | https://multi-agent-systems-failure-taxonomy.github.io/MAST |
| MultiAgentBench | Collaboration + competition across 6 scenarios | MARBLE framework | Microsoft Research Asia | http://arxiv.org/html/2503.01935v1 |
| WebShop | 1.18M real products + 12,087 instructions; e-commerce | Grounded web agents | Princeton + Salesforce | https://webshop-pnlp.github.io/ |
| ALFWorld | Text + embodied household tasks; text-to-action mapping | Benchmark standard for embodied agents | OSU NLP | https://prior-context (X. Liu et al.) |
| AWorld (inclusionAI) | Fronts agent runtime for self-improvement | Search-understand-reproduce agent | inclusionAI | https://github.com/inclusionAI/AWorld |
| Web Arena Leaderboard (Steel.dev) | Tracks WebArena systems holistically | Updated 2026 | Steel.dev | https://leaderboard.steel.dev/leaderboards/webarena |
| Agents' Last Exam | 55 sub-industries, 147/5000 public tasks | Industry expert-validated benchmark | Snorkel AI | http://snorkel.ai/leaderboard/agents-last-exam |
| OpenReview "Holistic Agent Leaderboard" | Submission infrastructure | Princeton (related) | OpenReview | http://openreview.net/forum?id=vUaY1t6 |

### 1.5 Agent Diagnostic / Failure Frameworks

| Benchmark | What it Measures | Notes | Maintainer | URL |
|----------|-------------------|-------|-----------|-----|
| AgentBoard / AgentEval | Trajectory-level agent evaluation | Open-source benchmarks + methodologies | XLang AI / Sapphire | https://www.agenteval.org/ |
| LangSmith + Arize AI | Instrumentation tooling | Holistically referenced in HAL/Survey | LangChain + Arize | Survey 2507.21504v1 (HAL cites) |

---

## 2_llm_general_chat_benchmarks

### 2.1 Knowledge / Reasoning / Multitask

| Benchmark | What it Measures | Top Score / Holder (2026 data) | Maintainer | URL |
|----------|-------------------|-------------------------------|-----------|-----|
| MMLU | 57 tasks across humanities/Sci/legal/math | Original benchmark; widely surpassed | UC Berkeley (Hendrycks) | https://arxiv.org/abs/2009.03300 |
| MMLU-Pro | 10-choice reasoning; harder than MMLU | Qwen3.7 Max 89.6%; Claude Opus 4.5 89.5%; Qwen3.7 Plus 88.5% (~1.1pt cluster) | TIGER-Lab | https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro |
| Alternative source: pricepertoken.com | MMLU-Pro 2026 rankings | Gemini 3 Pro Preview 89.8%; Claude Opus 4.5 89.5%; Gemini 3 Flash 89.0% | Independent aggregator | https://pricepertoken.com/leaderboards/benchmark/mmlu-pro |
| GPQA (Diamond) | Graduate-level Q&A in physics/chem/bio | Live leaderboard 2026 | D. Hendrycks et al. (then expanded) | https://pricepertoken.com/leaderboards/benchmark/gpqa |
| ARC (original) | Abstraction/Reasoning Corpus (ARC-AGI-1, by Chollet) | Original benchmark; first introduced 2019 | F. Chollet | https://arcprize.org/arc-agi/1 |
| ARC-AGI-2 | New ARC dataset; 2025/2026 competition target | Top partial/provisional scores from o1-pro, Claude Opus 5, Grok 4.5 | ARC Prize / Chollet | https://arcprize.org/leaderboard |
| ARC-AGI-2 Leaderboard (BenchLM) | SOTA tracker | GPT-5.6 Sol 92.5%; Claude Opus 5 90.4%; GPT-5.5 85% | Third-party | http://benchlm.ai/benchmarks/arc-agi-2 (cited) |
| ARC-AGI-3 | Frontier agentic intelligence benchmark | Technical report 2026 | ARC Prize | https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf |
| HellaSwag | Commonsense NLI (saturated for frontier) | 95%+ human baseline; near-saturated for LLMs | W. Zellers et al. | https://rowanzellers.com/hellaswag |
| SuperGPQA | Multidisciplinary GPQA extension | Qwen3.7 Max 0.736 across 34 models | SuperGPQA consortium | https://github.com/SuperGPQA/SuperGPQA |

### 2.2 Coding Benchmarks

| Benchmark | What it Measures | Top Score / Holder | Maintainer | URL |
|----------|-------------------|-------------------|-----------|-----|
| HumanEval (PY) | 164 hand-written Python coding problems | Reported saturated in 2026 | OpenAI (Mark Chen et al.) | https://benchmarkingagents.com/humaneval |
| MBPP | Mostly Basic Python Problems (974 tasks) | Near-saturated for frontier | Google Research + DeepMind | (related via HumanEval linked page) |
| LiveCodeBench | Real-world competitive programming contest problems (contamination-resistant) | DeepSeek V4 Pro (Max) 93.5%; Qwen3.7 Max 91.6%; DeepSeek V4 Flash (Max) 91.6% (Jul 10, 2026) | Naman Jain et al. | https://livecodebench.com (independent; via aggregator) |
| LiveCodeBench (pricepertoken.com) | Independent corroboration | Gemini 3 Pro Preview 91.7 (Jun 23, 2026) | Independent | https://pricepertoken.com/leaderboards/benchmark/livecodebench |
| SWE-bench Verified | (see agentic section) | Claude Opus 5 96% | SWE-bench team | http://swebench.com/verified.html |
| SWE-Lancer | Upwork-style engineering tasks ($1M task pool) | Frontier LLM coding-offer; track 100% leakage without isolation | OpenAI / SWE-bench team | (described in ABC survey) |
| ARC Prize / ARC-AGI Saturation | Not coding-related; cross-references | n/a | ARC Prize | https://arcprize.org/blog/arc-prize-2025-results-analysis |

### 2.3 Chat / Open-Ended Evaluation

| Benchmark | What it Measures | Top Score / Holder | Maintainer | URL |
|----------|-------------------|-------------------|-----------|-----|
| MT-Bench | LLM-as-a-judge for multi-turn chat | 80% agreement with human judges (GPT-4) | LMSYS (L. Zheng et al.) | https://arxiv.org/abs/2306.05685 |
| MT-Bench-101 | Fine-grained multi-turn dialogue eval | Cited 359+ | ACL 2024 | https://arxiv.org/abs/2402.14762 |
| LMSYS Chatbot Arena / Chatbot Arena+ | Crowdsourced randomized battles; 1M+ votes | Active 2026 | LMSYS / OpenLM.ai | https://openlm.ai/chatbot-arena |
| LMSys original HF Space | Crowdsourced arena | Active | lmarena-ai | https://huggingface.co/spaces/lmarena-ai/chatbot-arena |
| HELM (Holistic Evaluation of Language Models) | Multi-metric multimetric leaderboard | Stanford CRFM | Stanford CRFM | https://crfm.stanford.edu/helm/long-context/latest |
| HELM Long Context | Long-context sub-leaderboard | 2025 | Stanford CRFM | https://crfm.stanford.edu/2025/09/29/helm-long-context.html |
| lm-eval-harness | Few-shot eval framework; 100+ tasks | v0.4.3 | EleutherAI | https://github.com/eleutherai/lm-evaluation-harness |
| LiveBench | Contamination-free LLM benchmark | <=65% on hardest subsets (notes this is intended) | Abacus.AI-sponsored; whitepaper | https://livebench.ai/ |
| Artificial Analysis Intelligence Index | Independent LLM intelligence index | Independent aggregator | Artificial Analysis | http://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index |
| Artificial Analysis FAQ | Methodology, last verified 2026-07-27 | Independent | Artificial Analysis | http://artificialanalysis.ai/faq |

### 2.4 Long-Context Subset

| Benchmark | What it Measures | Maintainer | URL |
|----------|-------------------|-----------|-----|
| HELM Long Context | Long-context window eval | Stanford CRFM | https://crfm.stanford.edu/2025/09/29/helm-long-context.html |
| RULER | Customizable sequence-length + task-complexity | Hsieh et al. (NVIDIA) | https://arxiv.org/abs/2404.06654 |

---

## 3_rag_retrieval_benchmarks

### 3.1 Embedding / Retrieval Backbone

| Benchmark | What it Measures | Status | Maintainer | URL |
|----------|-------------------|--------|-----------|-----|
| MTEB (Massive Text Embedding Benchmark) | 100+ tasks across 7 categories incl. classification, retrieval, NLI | 196+ models tracked | HuggingFace mteb team | https://huggingface.co/spaces/mteb/leaderboard |
| MTEB GitHub | Reference impl | Add new benchmarks via PR | embeddings-benchmark | https://github.com/embeddings-benchmark/mteb |
| C-MTEB | Chinese subset of MTEB | Multi-language expansion | mteb team | (linked via MTEB hub) |
| BEIR (Benchmarking IR) | Cross-domain zero-shot retrieval (NDCG@10 spread) | Updated 2026 | N. Thakur et al. | https://app.ailog.fr/en/blog/news/beir-benchmark-update |
| KILT | Knowledge-Intensive Language Tasks | Wikipedia snapshot shared across 5 tasks | Meta AI (F. Petroni et al.) | https://github.com/facebookresearch/KILT |
| KILT paper | NAACL 2021 | Shared task framework | Petroni et al. | https://arxiv.org/abs/2009.02252 |
| FiQA | Financial QA benchmark | Part of BEIR suite | FIQA consortium | (within BEIR) |
| Natural Questions | Real Google query QA, 307K train / 7.8K dev | Google Research | T. Kwiatkowski et al. | https://aclanthology.org/Q19-1026.pdf |
| HotpotQA | 113K multi-hop reasoning questions w/ supporting facts | Stanford NLP | Z. Yang et al. 2018 | https://hotpotqa.github.io/ |
| HotpotQA dataset on HF | 203,109 rows | Dataset host | HuggingFace | https://huggingface.co/datasets/hotpotqa/hotpot_qa |

### 3.2 RAG-Specific Evaluation

| Benchmark | What it Measures | Status | Maintainer | URL |
|----------|-------------------|--------|-----------|-----|
| RAGAS | RAG metrics (faithfulness, answer-relevance, context-relevance) | December 11, 2025 docs update | Exploding Gradients | https://docs.ragas.io/en/latest/concepts/metrics |
| ARES | Auto-finetunes LM judges per RAG domain via synthetic data | NAACL 2024 | J. Saad-Falcon et al. + Stanford | https://arxiv.org/abs/2311.09476 |
| ARES (NAACL) | Peer-reviewed version | ACL Anthology | Saad-Falcon et al. | http://aclanthology.org/2024.naacl-long.20 |

### 3.3 Hallucination / Factuality / Long-Context

| Benchmark | What it Measures | Status | Maintainer | URL |
|----------|-------------------|--------|-----------|-----|
| TruthfulQA | Tests falsehood from imitative errors | MIT License | S. Lin et al. (OpenAI) | (within emergentmind index) |
| HaluEval | 35K span-level hallucination + 5K sample QA | EMNLP 2023 | Li et al. 2023 | https://aclanthology.org/2023.emnlp-main.397 |
| SymLoc (using HaluEval/TruthfulQA) | Symbolic localization reformulation | 2024 ACM | Multi-author | http://dl.acm.org/doi/10.1145/3799830.3799850 |
| FActScore | Fine-grained atomic factual precision in long-form text | Active, LLM Stats | Authored 2023 | https://arxiv.org/html/2305.14251v2 |
| FActScore Leaderboard | LLMs tracked at 0.5-1.0 scale | LLM Stats | Aggregator | https://llm-stats.com/benchmarks/factscore |
| LongBench | Bilingual long-context tasks | Bench | THUDM | (linked via RULER comparisons) |
| RULER | NIAH extension w/ varied needles + customizable length | Active 2024 | NVIDIA Hsieh et al. | https://arxiv.org/abs/2404.06654 |
| RULER Leaderboard | Live tracker | Live | llm-stats | https://llm-stats.com/benchmarks/ruler |

---

## 4_security_benchmarks_standards

### 4.1 Generic Web/Software Security Standards

| Benchmark / Standard | What it Measures / Does | Latest | Maintainer | URL |
|----------|-------------------------|--------|-----------|-----|
| OWASP Top 10:2025 | Reorganized threat categories for web apps | 2025 release | OWASP Foundation | https://owasp.org/Top10/2025 |
| OWASP Top 10:2025 (EN mirror) | Top 10 2025 EN | 2025 | OWASP | https://owasp.org/Top10/2025/en |
| Codificexplain OWASP 2025 | Change summary | Aug 2025 | Codific | https://codific.com/owasp-top-10-2025 |
| CWE Top 25 Most Dangerous Software Weaknesses | Priority list driven by CVE/CVSS data | 2025 release | MITRE / CWE team | https://cwe.mitre.org/top25 |
| CWE Top 25 archive | 2024 archive | Dec 15, 2024 listed | MITRE | https://cwe.mitre.org/top25/archive/2024/2024_cwe_top25.html |
| OWASP Application Security Verification Standard (ASVS) | Commercially-workable web app verification standard | v4.0.3 | OWASP | https://owasp.org/www-project-application-security-verification-standard |
| OWASP Web Security Testing Guide (WSTG) | Comprehensive web security testing methodology | v-latest | OWASP | https://owasp.org/www-project-web-security-testing-guide/latest |
| OWASP API Security Top 10 2023 | API-specific top-10 | 2023 | OWASP | (canonical; see PCI DSS / NIST) |
| MITRE ATT&CK v18 / v19.1 | Adversary behavior framework | v18 (Oct 2025), v19.1 (Apr 2026) [195-199] | MITRE | https://attack.mitre.org/resources/updates/updates-october-2025 |
| MITRE ATT&CK Version History | Annual versions | v18.1 Oct 2025 - Apr 27, 2026 | MITRE | https://attack.mitre.org/resources/versions |
| MITRE Enterprise Placemat v9 | 11x17 PDF pictographic matrix | Used by red teams | MITRE | https://attack.mitre.org/docs/MITRE_ATTACK_Enterprise_11x17.pdf |
| DARPA Cyber Grand Challenge | Autonomous exploit+patch AI machines | Held 2016; foundational | DARPA | (historical reference) |

### 4.2 LLM / Agent Security Benchmarks

| Benchmark | What it Measures | Status | Maintainer | URL |
|----------|-------------------|--------|-----------|-----|
| JailbreakBench (JBB) | 100 misuse behaviors / 10 categories; open robustness | NeurIPS 2024 D&B Track | P. Chao et al. | https://arxiv.org/pdf/2404.01318 |
| HarmBench | Standardized eval for automated red teaming, 18 methods x 33 LLMs | 2024 | Center for AI Safety | https://arxiv.org/abs/2402.04249 |
| HarmBench github | Codebase | Open-source | Center for AI Safety | https://github.com/centerforaisafety/HarmBench |
| AdvBench | 521 harmful behaviors from Universal+Transferable Attacks paper | HuggingFace dataset | walledai | https://huggingface.co/datasets/walledai/AdvBench |
| AdvBench (paper) | Universal + transferable adversarial prompts | 2023 | Zou et al. (CMU) | https://arxiv.org/pdf/2310.04451 |
| StrongREJECT | State-of-the-art jailbreak benchmark (517 prompts); empty-jailbreak detection | 2024 | A. Souly et al. | https://arxiv.org/pdf/2402.10260 |
| AutoDAN | Stealthy hierarchical GA jailbreaks | 2023 | UCSD (X. Liu) | https://arxiv.org/pdf/2310.04451 |
| GPTFuzzer | Auto-mutating template fuzzer | 2023 | Fudan team | https://arxiv.org/html/2309.10253v1 |
| CyberSecEval (Meta) | First gen (2023); quantifies LLM cybersecurity risk | Initial release | Meta AI (Phat Bhatt) | https://ai.meta.com/research/publications/cyberseceval-2-a-wide-ranging-cybersecurity-evaluation-suite-for-large-language-models |
| CyberSecEval 2 | Adds prompt injection + code interpreter abuse tests | Apr 18, 2024 | Meta AI | https://ai.meta.com/research/publications/cyberseceval-2-a-wide-ranging-cybersecurity-evaluation-suite-for-large-language-models |
| CyberSecEval 3 | New suite for LLM cybersecurity risk + capabilities | 2024-2025 (paper 2408.01605) | Meta AI | https://arxiv.org/html/2408.01605v1 |
| Inspect Evals CyberSecEval 3 (UK Gov BEIS) | Replication of CSE3 metrics | 2025 | UK Gov BEIS | https://ukgovernmentbeis.github.io/inspect_evals/evals/cyberseceval_3/index.html |
| ToolEmu | Agent misuse via tool execution emulation | Cited 538+ | Yale + Microsoft | http://arxiv.org/abs/2309.15817 |
| JALMBench (ICLR 2026) | Harmful text-prompt converted to spoken audio jailbreak test | New 2026 | Author: multi-institution | https://aiwiki.ai/wiki/advbench (referenced) |

### 4.3 India-Specific Security & Compliance

| Standard / Doc | What it Covers | Status | Maintainer | URL |
|----------|-------------------|--------|-----------|-----|
| CERT-In Directions of 2022 | Cyber-incident reporting requirements, KYC record retention | In effect | MeitY / CERT-In | https://www.scribd.com/document/590581945/CERT-IN-issues-directions |
| CERT-In analysis (Saikrishna) | Practitioner summary | Ongoing | Saikrishna & Associates | https://www.saikrishnaassociates.com/cert-in-issues-directions-for-information-security-practices-procedure-prevention-response-and-reporting-of-cyber-incidents |
| DPDPA 2023 (Digital Personal Data Protection Act) | Master Act for personal data in India | In force | MeitY | https://www.dpdpa.com/dpdpatemplatesandpolicies.html |
| DPDPA Compliance Checklist 2026 (50-point) | Self-assessment template | Feb 1, 2026 | dpdpa.com | https://www.dpdpa.com/blogs/dpdpa_compliance_checklist_2026_business_assessment.html |
| RBI Digital Lending Guidelines | Master circular for digital lending apps | Feb 14, 2023 | RBI | http://rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3413 |
| RBI Digital Lending Directions 2025 | Consolidation of lending framework | Aug 21, 2025 | RBI | https://www.legal500.com/developments/thought-leadership/the-rbis-digital-lending-directions-2025-a-unified-code-for-a-fragmented-sector |
| RBI Master Circular -- Capital Adequacy | RBI comprehensive capital adequacy norms | Updated annually | RBI | https://www.rbi.org.in/commonman/english/scripts/Notification.aspx?Id=1482 |
| RBI Notification Index | All RBI master circulars | Live | RBI | https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12848 |

---

## 5_web_app_quality_perf

### 5.1 Performance Metrics & Audits

| Tool / Standard | What it Measures | Status | Maintainer | URL |
|----------|-------------------|--------|-----------|-----|
| Google Core Web Vitals | 75th-percentile LCP, INP, CLS; thresholds: "Good" thresholds 2025 | Live; LCP 2.5s good, INP 200ms good, CLS 0.1 good [131, 133] | Google / Alphabet | https://web.dev/articles/vitals |
| Core Web Vitals thresholds | Definition rationale | 2020 baseline + alerts | Google | https://web.dev/articles/defining-core-web-vitals-thresholds |
| WebPageTest (WPT) | Real-browser worldwide perf measurement | OpenSource + CatchPoint | CatchPoint | http://webpagetest.org/ |
| WebPageTest / CatchPoint | CatchPoint acquisition | Alternative home | Catchpoint | http://catchpoint.com/webpagetest |
| PageSpeed Insights v5 | Audits + summarizes field data (Core Web Vitals) | Live | Google | https://developers.google.com/speed/docs/insights/v5/about |
| Google Lighthouse | Audits perf / SEO / accessibility / best practices | Scoring calculator updated | Google | https://developer.chrome.com/docs/lighthouse/performance/performance-scoring |

### 5.2 Load / Stress / E2E Testing

| Tool | What it Does | License / Maintainer | URL |
|----------|-------------------|-----------|-----|
| k6 (Grafana) | Open-source load testing | Grafana Labs / OSS | http://grafana.com/oss/k6 |
| Apache JMeter | Java-based load + functional testing | Apache Software Foundation | https://jmeter.apache.org/ (canonical) |
| Gatling | Code-based Scala/Kotlin load testing | GatlingCorp | https://gatling.io/ (canonical) |
| Locust | Python-based swarm load testing | Locust.io OSS | https://locust.io/ (canonical) |
| Playwright | Microsoft end-to-end testing framework | Microsoft | https://playwright.dev/ |
| Cypress | JavaScript E2E + accessibility + component testing | Cypress.io | https://www.cypress.io/ |
| Cypress "Why Cypress" | Testing modalities coverage | Cypress | http://docs.cypress.io/app/get-started/why-cypress |

### 5.3 Accessibility Standards & Tools

| Tool / Standard | What It Does | Maintainer | URL |
|----------|-------------------|-----------|-----|
| axe-core | Deque accessibility engine used by millions of audits | Deque Systems | http://deque.com/blog/deque-unifies-accessibility-software-under-axe |
| WCAG 2.2 (W3C) | International web content accessibility standard | W3C WAI | https://www.w3.org/WAI/standards-guidelines/wcag |
| WCAG 2.2 ISO mirror | ISO/IEC 40500 (Oct 21, 2025) | W3C + ISO | https://www.w3.org/WAI/news/2025-10-21/wcag22-iso |
| Accessible.org WCAG checklist | Implementation checklist 2.1 AA + 2.2 AA | Accessible.org | https://accessible.org/wcag |

---

## 6_finance_fintech

| Standard / Doc | What It Mandates / Measures | Maintainer | URL |
|----------|----------------------------|-----------|-----|
| Basel III | Capital requirements framework for global banks | BIS (Bank for International Settlements) | https://www.bis.org/basel_framework |
| Basel III (EU info) | EU implementation summary | Council of EU | https://www.consilium.europa.eu/en/policies/basel-iii |
| CCAR (Comprehensive Capital Analysis and Review) | Annual Fed stress test for large US banks | Federal Reserve Board | https://www.federalreserve.gov/supervisionreg/stress-tests-capital-planning.htm |
| 2025 Supervisory Stress Test Methodology | Identical models to 2024 stress test | Federal Reserve Board | https://www.federalreserve.gov/publications/2025-june-supervisory-stress-test-methodology-introduction.htm |
| EBA EU-Wide Stress Testing | Europe-wide biennial bank stress test (50+ EU banks) | European Banking Authority | https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing |
| EBA 2025 EU-wide stress test results | Aug 1, 2025 publication | EBA | https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-results-its-2025-eu-wide-stress-test |
| FRTB (Fundamental Review of Trading Book) | Capital market risk rules | BCBS / ICMA / BIS | https://www.icmagroup.org/market-practice-and-regulatory-policy/secondary-markets/secondary-markets-regulation/fundamental-review-of-the-trading-book-frtb |
| RBI Stress Testing Guidelines (Master Circular) | Domestic stress test paradigms | RBI | https://www.rbi.org.in/commonman/english/scripts/Notification.aspx?Id=1482 |
| RBI Digital Lending Guidelines 2025 | Indian digital lending compliance | RBI | http://rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3413 |
| ISO 20022 (Cross-border payments) | Global financial messaging standard | ISO | https://www.jpmorgan.com/insights/payments/fx-cross-border/iso-20022-migration |
| ISO 20022 (MUFG adoption article) | Why financial firms move to ISO 20022 | MUFG Bank | http://bk.mufg.jp/global/productsandservices/transaction/iso20022_migration/index.html |
| ISO 20022 SWIFT deadline | Swift SR2025 release deadline Nov 22, 2026 | SWIFT | http://swift.com/standards/iso-20022/iso-20022-bytes/iso-20022-bytes-payments-countdown-iso-20022 |
| PCI DSS (PCI Data Security Standard) | Card data protection | PCI Security Standards Council | https://www.pcisecuritystandards.org/documents/PCIDSS_QRGv3_1.pdf |
| PCI DSS 4.0 Mandatory Requirements | 2025 compliance | Linford Co (summarized) | https://linfordco.com/blog/pci-dss-4-0-requirements-guide |
| PCI DSS Requirement 4 | Encryption in transit | ISMS.online | https://www.isms.online/pci-dss/requirement-4 |
| OWASP API Security Top 10 2023 | API-specific top 10 (per query) | OWASP | (canonical; see Security 4.1) |

---

## 7_health

| Benchmark / Standard | What It Measures / Covers | Maintainer | URL |
|----------|--------------------------|-----------|-----|
| MedQA | USMLE-style multiple-choice questions (12,723) | Google Research (Jin et al.) | https://benchmarkingagents.com/medqa-medical-benchmark |
| Med-PaLM 2 reference score on MedQA | 86.5% MedQA accuracy | Google DeepMind | (via benchmarkingagents.com) |
| MedBench | 43 clinical specialties; original 300,901 questions | AIcrowd-coalition (MedBench authors) | https://arxiv.org/abs/2407.10990 |
| MedBench v4 | 700K expert-curated tasks; 24 primary + 91 secondary specialties | Chinese MedBench consortium | https://arxiv.org/abs/2511.14439 |
| Benchmarking Chinese Medical LLMs | Chinese LLM MedBench comparison 2025 | arXiv 2503.07306 | https://arxiv.org/abs/2503.07306 |
| PubMedQA | Biomedical research QA (1k expert labeled + 211.3k artificial) | University of Alberta (Q. Jin et al.) | https://pubmedqa.github.io/ |
| PubMedQA paper (EMNLP 2019) | Research challenge | ACL Anthology | https://aclanthology.org/D19-1259 |
| MIMIC (Medical Information Mart for Intensive Care) | Critical-care dataset; leveraged for benchmarks | MIT Lab for Computational Physiology | https://arxiv.org/html/2506.12808v1 |
| WHO Global Strategy on Digital Health | 2020-2025 strategy framework | WHO | https://www.who.int/health-topics/digital-health/ |
| WHO "Digital Health and Innovation" | Detailed brochure | WHO | https://cdn.who.int/media/docs/default-source/digital-health-documents/who_brochure_dhi_web.pdf |
| WHO "Digital Health" topic page | Comprehensive introduction | WHO | https://www.who.int/health-topics/digital-health/ |
| WHO Foundation funding digital health | Funding initiatives | WHO Foundation | http://who.foundation/digital-health |
| HIPAA (US) | Privacy/Security rules for protected health info | US HHS | (per Health Insurance Portability and Accountability Act) |
| DPDPA India health-data re-use | Personal data rules also impact health research | MeitY | (linked via DPDPA in section 4.3) |

---

## 8_education

| Benchmark / Standard | What It Measures | Maintainer | URL |
|----------|-------------------|-----------|-----|
| ARC (original) -- 2019 | Abstract reasoning dataset for general AI | F. Chollet | https://arcprize.org/arc-agi/1 |
| ARC Prize 2025 (Tech Report) | Competition results + analysis | ARC Prize | https://arcprize.org/blog/arc-prize-2025-results-analysis |
| ARC-AGI-1 to ARC-AGI-3 | Progressive challenge through agentic intelligence | ARC Prize | https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf |
| MMLU as education proxy | Multitask language understanding covers N-12 knowledge | UC Berkeley | https://arxiv.org/abs/2009.03300 |
| HellaSwag (commonsense) | Often used as a near-saturated education-level commonsense probe | U Washington (Zellers) | https://rowanzellers.com/hellaswag |
| Khanmigo | Khan Academy's AI-powered tutor/teaching assistant | Khan Academy | http://khanmigo.ai/ |
| Khanmigo for Parents | Parent-targeted docs | Khan Academy | http://khanmigo.ai/parents |
| Khanmigo (Weber overview) | Educational use cases | Weber State University | http://weber.edu/ai/khanmigo.html |
| Benchmark Education Company | K-12 testing materials publisher | Benchmark Education Co. | https://github.com/benchmarkeducation |
| BEEAR (Benchmarking Educational AI interventions) | Emerging academic-grade AI tutor eval | (paper in progress; see SafeTutors) | https://arxiv.org/html/2603.17373v1 |
| SafeTutors | Joint safety + pedagogical tutor eval (maths, physics, chemistry) | 2026 | https://arxiv.org/html/2603.17373v1 |
| Path to Conversational AI Tutors | Industry research | OpenAI (cited) | https://arxiv.org/html/2602.19303v1 |
| Digital Promise K-12 AI Infrastructure | Grantees incl. AI-misconception benchmark, simulator student models | Digital Promise + US NSF | http://prnewswire.com/news-releases/digital-promise-announces-first-grantees-of-the-k-12-ai-infrastructure-program-302812084.html |
| UGC India Guidelines | Indian university AI policy | UGC, India | (per UGC public portal) |

---

## 9_hardware_edge

| Benchmark / Standard | What It Measures | Maintainer | URL |
|----------|-------------------|-----------|-----|
| MLPerf Inference v5.0 | Architecture-neutral ML inference benchmark; Gen-AI focus | MLCommons | https://mlcommons.org/working-groups/benchmarks/inference |
| MLPerf Inference v5.0 Results (press release) | Gen AI engineering perf focus | MLCommons | http://mlcommons.org/2025/04/mlperf-inference-v5-0-results |
| MLPerf Inference v5.0 LLM | LLM-specific inference track | MLCommons | http://mlcommons.org/2025/04/llm-inference-v5 |
| MLPerf Inference v5.0 GitHub | Raw submission data | MLCommons | https://github.com/mlcommons/inference_results_v5.0 |
| MLPerf Tiny v1.4 | Ultra-low-power edge AI (latency, accuracy, energy) | MLCommons | https://mlcommons.org/2026/07/mlperf-tiny-v1-4-results |
| TinyMLPerf (original 2020 lineage) | Microcontroller-grade ML benchmarking | Harvard Open AgB / MLPerf Tiny team | https://arxiv.org/html/2505.15622v1 |
| MLPerf Training | Time-to-quality training benchmark | MLCommons | https://mlcommons.org/benchmarks/training |
| EdgeBench (ByteDance Seed) | 134 real-world tasks; UL-horizon benchmark "Scaling Laws of Environment Learning" | ByteDance Seed | https://github.com/ByteDance-Seed/EdgeBench |
| EdgeBench (IEEE) | Edge computing platform benchmark | IEEE | https://ieeexplore.ieee.org/document/8605776 |
| Edge-Bench.org | Long-horizon environment-learning benchmark | EdgeBench team | https://edge-bench.org/ |
| MLCube | ML reproducibility across hardware | MLCommons | (linked via MLPerf Training) |
| Snapdragon AI Benchmark (Qualcomm) | Mobile AI performance per watt | Qualcomm | https://www.qualcomm.com/smartphones/features/mobile-ai |
| Snapdragon 8 Elite | Claims 45% AI perf / per-watt improvement | Qualcomm | https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-elite-mobile-platform |

---

## 10_enterprise_ops_governance

### 10.1 Reliability, DevOps, ITSM

| Tool / Standard | What It Does | Maintainer | URL |
|----------|-------------------|-----------|-----|
| DORA State of DevOps Report / DORA Metrics | 4 metrics: lead time, deploy freq, MTTR, change fail % | DORA (Google Cloud) | https://dora.dev/ |
| Google SRE Book | Comprehensive guide to Site Reliability Engineering | Google | http://sre.google/books |
| SRE Workbook (Google) | Implementing SLOs | Google | https://sre.google/workbook/implementing-slos |
| SRE Engagement Model | SRE org practices | Google | http://sre.google/workbook/engagement-model |
| SRE Resources / Digital Library | Curated list of all SRE books, videos | Google | http://sre.google/resources |
| Building Secure & Reliable Systems | SRE + security crossover | Google | http://sre.google/books |
| ITIL 4 Framework | Service management 34 practices | AXELOS / PeopleCert | https://itsm.tools/itil-4-explained |
| ITIL 4 FAQ / Study Guide | Certification prep | PassITExams | https://passitexams.com/study-guide/itil-4-foundation |

### 10.2 Information Security & Trust

| Standard / Frame | What It Covers | Maintainer | URL |
|----------|-------------------|-----------|-----|
| ISO 27001:2022 (Infomation Security Mgmt) | Reorganized Annex A with 93 controls across 4 themes | ISO / IEC | https://www.iso.org/obp/ui/es#iso:std:iso-iec:27002:ed-3:v2:en |
| ISO 27001 Annex A (assessor writeup) | Control-set mapping | IT-Governance | https://www.itgovernance.co.uk/blog/iso-27001-the-14-control-sets-of-annex-a-explained |
| ISO 27001 Control 5.9 (Asset Inventory) | Implementation guide | ISO-Docs | https://iso-docs.com/blogs/iso-27001-2022-standard/iso-27001-2022-control-5-9-inventory-of-information-and-other-associated-assets |
| SOC 2 Trust Services Criteria | 5 categories: Security, Availability, Processing Integrity, Confidentiality, Privacy | AICPA | https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services |
| SOC 2 by Trust Services Criteria | Audit overview | AICPA | https://www.aicpa-cima.com/category/resources/audit-assurance/audit-and-assurance-greater-than-soc-2 |
| AICPA SOC suite overview | Plus SOC 1, SOC 3 comparisons | AICPA+CIMA | https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services |

### 10.3 AI Governance Frameworks

| Standard / Frame | What It Covers | Maintainer | URL |
|----------|-------------------|-----------|-----|
| NIST AI Risk Management Framework (AI RMF) | Govern-Map-Measure-Manage (4 functions) | NIST (US) | http://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (GenAI profile) |
| NIST AI RMF (Orca explainer) | Practical org adoption | Orca Security | http://orca.security/resources/blog/nist-ai-risk-management-framework-ai-rmf |
| NIST AI 600-1 (Gen AI profile) | Specialized for GAI | NIST AIRC | https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf |
| NIST AI 600-1 mirror | International safety perspective | AI Security + Safety | https://aisecurityandsafety.org/en/frameworks/nist-ai-600-1 |
| EU AI Act | 3-tier risk classification: Unacceptable / High / Limited+Minimal | EU Commission | https://artificialintelligenceact.eu/ |
| EU AI Act (official EC digital strategy) | Risk-based rules for AI developers/deployers | European Commission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai |
| EU AI Act Guide (HCL Tech v2) | Compliance practitioner guide | HCLTech (published Mar 2026) | https://www.hcltech.com/sites/default/files/documents/resources/pdf-landing-page/files/2026/03/03/EU-AI-Act-Guide-v2.pdf |
| EU AI Act Explained | Non-lawyer summary | Diplomacy & Law | https://www.diplomacyandlaw.com/post/eu-ai-act-explained |
| India AI Governance Guidelines | 7 guiding sutras; techno-legal, principle-based | MeitY (PIB release Feb 2026) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026215790801.pdf |
| India AI Governance Guidelines (analysis) | Practitioner decode | Saikrishna & Associates | http://saikrishnaassociates.com/decoding-the-india-ai-governance-guidelines |
| INDIAai (IndiaAI Mission Pillars) | 7 pillars of IndiaAI Mission | MeitY | https://indiaai.gov.in/ |
| MeitY official press release (Nov 5, 2025) | Unveiling of India AI Governance Guidelines | Digital India | https://www.digitalindia.gov.in/press_release/meity-unveils-india-ai-governance-guidelines-under-indiaai-mission |

---

## synthesis

### Dimension 1: Mechanism -- Why Each Benchmark Matters

Most agentic benchmarks (AgentBench, GAIA, tau-bench, OSWorld, WebArena) measure **process** (tool calls, multi-turn fidelity) while LLM benchmarks (MMLU-Pro, GPQA, ARC-AGI-2) measure **knowledge endpoints**. The mechanism gap explains why the tau^3 retro-fix drastically reduced the do-nothing agent pass rate of ~38%-40% [4-5, 214]: those benchmarks conflated trajectory success with end-state correctness. For hackathon projects, the implication is that **process metrics (HAL, AgentBoard) are less luminous but more honest than stat-point scores**; teams that publish trajectory traces alongside task success demonstrate due diligence against the leakage path uncovered in ABC audit cases (e.g. SWE-Lancer's 100% no-op, KernelBench's 31% OOB bias).

### Dimension 2: Trade-Offs -- Saturation vs Coverage

| Benchmark Class | Saturation State (2026) | Coverage Trade-off |
|----------|--------------------------|----------------|
| HumanEval, MBPP | Saturated | Cheap to debug, but no longer discriminative |
| MMLU-Pro | Top 5 within 1.1 pts (`[~0.89]`) | Near-saturated for frontier |
| GPQA Diamond | Active leaderboard | Hard, decisive |
| ARC-AGI-2 | New 92.5% GT5 SOTA | Best abstraction lens so far |
| HELM | Multi-axis, transparent | Best for policy/governance projects |
| Polyglot RAG (MTEB) | 196+ models, NDCG@10 leader | Best for retrieval-heavy hackathons |
| Fraud / Fintech (RBI + DPDPA + CERT-In combo) | Compliance-bound | Best for Indian fintech hackathons |
| Cybersecurity (CyberSecEval 3 + JBB + HarmBench) | Active arms race | Best for safety-focused entries |

### Dimension 3: Evidence Verification -- Cross-Source Spread

Where multiple sources disagree on a score, both URLs are cited. For example:
- **MMLU-Pro top:** BenchLM Qwen3.7 Max 89.6% vs pricepertoken Gemini 3 Pro Preview 89.8%; both shown because different aggregator windows + reporter preferences yield slight reordering.
- **WebArena top:** Steel.dev shows WebTactix 74.3% on submitted systems; codesota shows Qwen3-235B-A22B 95.6% accuracy-correlated. These are different sub-metrics.
- **Sierra tau-bench:** published tau^3 audit claims many original tasks were intentionally unsolvable and "do-nothing" agents routinely passed [4-5]; the fix decreased leakage to negligible, which itself is an inverse benchmark quality signal.

### Dimension 4: Divergences the Hackathon Prep Should Resolve

- **Saturated-benchmark entrenchment.** HumanEval/MBPP remain widely cited but are at saturation; Frontier labs have moved to SWE-bench Verified and LiveCodeBench. Choosing stale benchmarks risks wall-clock scoring without discriminatory power.
- **Process vs outcome metrics.** HAL/AgentBoard publish cost-aware trajectories; tau-bench's pass^k captures the do-nothing risk; ABC survey documents up to 100% bias in 10 surveyed benchmarks. Pick the metric your demo can defend.
- **Indian 4-pillar compliance vs EU AI Act.** The two are partially overlapping but not interchangeable: Indonesia/Singapore/India-based hackathon entries sweep MeitY+DPDPA+CERT-In+RBI; EU-targeting products sweep EU AI Act + GDPR + NIS2. Choose jurisdiction-aware demo posture.
- **MITRE ATT&CK v18 detection overhaul.** Re-modeling behavioral chains may invalidate prior purple-team reports; all security demos should cite ATT&CK v18+ IDs [195-199].

### Cross-Cutting Recommendation

For a Craft N Code 2026 entry that aims to win, the highest-yield strategy is to **stitch together a clear category-aligned benchmark set and publish trajectory + cost + leaderboard evidence**: e.g. for an Indian-fintech AI agent, demonstrate (1) SWE-bench Verified-style coding skill, (2) MultiAgentBench collaboration, (3) RAGAS RAG faithfulness, (4) cyber hardening via CyberSecEval 3 + JBB-HarmBench, plus (5) DPDPA + CERT-In + RBI Digital Lending + MeitY AI Governance references. The multi-axis profile is what differentiates a hackathon-grade evaluation from a salesperson-grade claim.

---