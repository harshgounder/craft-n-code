# PER-TOPIC-BENCHMARKS-2026.md: benchmark + eval registry, one per domain

Purpose: for EVERY domain in TOPIC-UNIVERSE (30 domains), the named
benchmarks, eval standards, and tools that measure a product in that
domain. This is the answer to "what do we cite when the judge asks how
we measure it". Statuses: [PREFILL] = from model knowledge, wave-4
(parallel.ai, run in flight) will verify + add fresh 2026 numbers;
[VERIFIED] = numbers seen in a cited source this cycle.
WAVE-4 VERIFIED UPGRADES (raw/wave4-benchmarks.md): SWE-bench Verified
led by Claude Opus 5 ~96%, Claude Mythos 5 95.5% (HumanEval saturated;
target SWE-bench Verified + LiveCodeBench); AgentBench-style suites show
~80% success variance across runs -> multi-run eval with confidence
intervals, AgentBoard-style pass@k + pass^k; tau-bench false-pass fixed
(show trajectory metrics: tool calls, user turns); MTEB tracks 196+
models now multilingual (C-MTEB); BEIR NDCG@10 = generalization probe;
RAGAS + ARES complementary (fixed metrics + auto-tuned LM judges);
CyberSecEval 3 (Meta) = cyber bar; OWASP Top 10:2025 reorganized, OWASP
API Security Top 10 (2023) canonical for fintech; India 4-pillar
compliance stack = DPDPA 2023 + CERT-In Directions + RBI Digital
Lending Directions 2025 + MeitY India AI Governance Guidelines
(Nov 2025).

Coverage: 30 domain sections, ~250 named benchmarks/standards/tools.
Statuses: [PREFILL] rows = from model knowledge (wave-4 verified numbers
live in the block above; per-domain merge pending); [VERIFIED] = seen
in a cited source this cycle. EVIDENCE CHAIN (read once): wave-sourced
numbers are verified through the report's inline citations, not
independently re-measured; the recheck spot-checks URL reachability,
not content. When citing a number on stage, keep the same chain:
"per <source>, cited in our research, raw file on disk".

## 01 OPS / SRE / INCIDENT
[PREFILL] DORA metrics (deployment frequency, lead time, MTTR, change
failure rate), Google SRE book SLI/SLO/SLA framework, Error Budgets,
Site Reliability Engineering workbook, Chaos engineering suites
(Chaos Monkey, Chaos Mesh, Litmus), GameDays, Incident.io postmortem
standards, PagerDuty incident taxonomy, Gremlin failure injection.
Tools: k6, Prometheus, Grafana, Sentry, OpenTelemetry.
Stress mapping: our trace ring (200 steps) + deadline gates are an
SLO-measurement instance. VERIFIED in our code: timeout chain + circuit
breaker (providers.py 40s, offline fallback).

## 02 CUSTOMER SUPPORT
[PREFILL] CSAT/NPS/CSI standards, AHT (average handle time), FCR
(first contact resolution), SLA adherence, ticket deflection rate,
LLM support evals: SupportBench, TweetQA, Customer Support on HELM,
Koala/ShareGPT-style human preference, G-Eval for response quality,
Zendesk/Intercom benchmarks (proprietary), KPI: resolution accuracy,
escalation precision, hallucination rate on refunds/policies.

## 03 FINANCE / FINTECH
[PREFILL] EBA stress tests, CCAR (Fed), Basel III/IV ratios, FRTB,
RBI stress testing guidelines (2024-2026), OWASP API Security Top 10,
PCI DSS 4.0, ISO 20022 messaging, FIX protocol conformance, UPI spec
(NPCI), RTGS/NEFT rules, double-spend and reconciliation tests,
decimal precision (IEEE 754 traps: 0.1+0.2), idempotency tests,
audit trail standards (immutable logs, RFC 3164/5424 syslog),
GAAP/Ind-AS reporting, fraud detection evals: IEEE-CIS Fraud
Detection (Kaggle), PaySim, AML typologies (FATF 40).

## 04 SECURITY / CYBER
[PREFILL] OWASP ASVS 4.0 (levels 1-3), OWASP WSTG, OWASP Top 10 2021,
OWASP LLM Top 10 2025, CWE Top 25, MITRE ATT&CK (enterprise+mobile),
MITRE ATLAS (AI), DARPA Cyber Grand Challenge, AutoDAN, JailbreakBench,
HarmBench, AdvBench, StrongREJECT, PAIR, GPTFuzzer, Meta CyberSecEval,
SecurityEval, SEED-Bench, CyberMetric, Purdue/ICS frameworks,
CERT-In advisories, RBI/UPI security circulars, DPDPA compliance
checklist, NIST CSF 2.0, NIST AI RMF 1.0, ISO 27001, SOC 2, TPM/firmware
attestation standards (for hardware kits).
Our instance: S8 path traversal check, injection checks in stress
suite, provider key handling (anchored regex, no key in repo).

## 05 PRIVACY / DATA CONTROL
[PREFILL] DPDPA 2023 (rules 2025) compliance matrix, GDPR Art. 17
(right to erasure) tests, consent management standards (IAB TCF,
ISO 29184), data minimization checklists, differential privacy
benchmarks (DP-SGD utility tradeoff), k-anonymity/l-diversity tests,
Apple Privacy Nutrition Labels (for on-device kits), on-device
inference evals: MLC-LLM, ExecuTorch, CoreML performance, privacy
leak tests (side-channel, timing), PII detection evals: Presidio,
Microsoft Presidio benchmarks, AWS Comprehend PII F1.
Our instance: consent gate tests, no-data-leaves-device fixture
(kit3_privacy), do-not-upload test rows.

## 06 CREATIVE / BRAND
[PREFILL] Adobe Content Credentials / C2PA provenance spec,
brand-consistency evals (color/logo/voice violation detectors),
StyleGAN/Stable Diffusion fidelity evals: FID, IS, CLIP score,
ImageReward, Pick-a-Pic, HPS v2, DPG-Bench, T2I-CompBench, GenEval,
DSG-1K, Brandmark tests, A/B creative testing (Meta Ad Library
patterns), font licensing (OFL), WCAG color contrast for assets.
Our instance: kit2_creative fixture (brief -> variants -> violation
caught -> approved export), brand-rule gate tests.

## 07 MESSAGING / COMMUNITY
[PREFILL] moderation evals: Jigsaw Perspective API (toxicity),
HateCheck, HONEST, CivilComments, Multitask-Toxicity, PAN-clef
(troll/abuse), semantic similarity for duplicate detection (STS-B),
multimodal safety: MM-SafetyBench, SafeBench, WhatsApp-style delivery
semantics (ordering, exactly-once), group scaling tests, scam-detection
evals: Smishing datasets, FraudGPT countermeasures, voice-note ASR
evals: WER (LibriSpeech, Common Voice, Indic TTS/ASR: Bhashini
benchmarks), speaker verification (VoxCeleb).
Our instance: kit4_messaging fixture (family rent agreement + scam
call), trust/answer gate, escalation test.

## 08 ENTERPRISE OPS / GOVERNANCE
[PREFILL] RACI + policy-as-code (OPA Rego test suites), audit log
standards (SIEM: Splunk/Cribl/Elastic ingestion, MITRE ATT&CK mapping),
approval workflow benchmarks: human-in-the-loop studies (METR RCT,
Glean UX studies), enterprise RAG evals (RAGAS on enterprise corpora,
ARES), KPI dashboards (Tableau/PowerBI validation), ISO 38500 IT
governance, COBIT 2019, TOGAF, DORA for AI adoption (Accenture
research), responsible AI governance: NIST AI RMF, EU AI Act tiers,
MeitY AI governance framework 2025-2026.
Our instance: approval.py policy gate + 13/13 approval suite, trace
ring audit, 7-stage approval queue in UI brief.

## 09 HEALTH
[PREFILL] MedQA (USMLE), MedBench, PubMedQA, MIMIC-III/IV tasks,
Med-HALT, HealthBench (Anthropic), GatorTron, EHR QA: emrQA,
discharge summary evals, clinical safety: NEVER give diagnosis tests,
consent/records: DPDPA health rules, HIPAA-style access logging,
WHO digital health guidelines 2026, ICMR telemedicine guidelines,
drug interaction checks (DDI benchmarks), accessibility: WCAG for
health apps, medical device software: IEC 62304.
Risk gate: our kits refuse clinical claims (honest "not medical
advice" pattern from kit3).

## 10 EDUCATION
[PREFILL] MMLU (edu subsets), ARC, ARC-AGI-2, BEEAR (AI tutor evals),
Khanmigo-style tutoring quality, grader consistency evals (Cohen's
kappa, quadratic weighted kappa), Bloom's taxonomy alignment,
NEP 2020 alignment, UGC guidelines, plagiarism/cheating resistance,
question generation evals (BLEU/ROUGE + human), feedback quality
(EdTech benchmarks), accessibility (WCAG + UDL).
Our instance: 2025 lane = lecture generator + lab grader; kit mapping
KIT-1/KIT-4.

## 11 WEB3
[PREFILL] smart contract audits (Slither, Mythril, CertiK), ERC
standards conformance (ERC-721/1155/4337), gas benchmarks, tokenomics
stress, replay/signature replay tests, wallet security (EIP-712),
NFT metadata standards, ticketing anti-bot tests.
2025 lanes: NFT ticketing, Web3 loyalty SBT. Low 2026 prior, but
covered if PS-04 goes this way.

## 12 HARDWARE / EDGE
[PREFILL] MLPerf Inference/Tiny, TinyMLPerf, EdgeBench, MLCommons
Mobile, Qualcomm AI Hub benchmarks, power/thermal (UL, IEC 62368),
latency p99 budgets, NPU SDK evals (ExecuTorch, XNNPACK), sensor
accuracy (IMU, camera), OTA update integrity, boot time, sleep/wake.
Our rule: software companion only, never fresh hardware on stage.

## 13 GOVERNMENT / CITIZEN
[PREFILL] DPDPA compliance, DigiLocker API integration, UMANG
standards, grievance redressal: CPGRAMS data, language access:
Bhashini ASR/MT evals (WER, BLEU on Indic), accessibility: WCAG
2.2 AA, W3C WAI, digital literacy usability studies (NIELIT),
open data standards (data.gov.in, OGD), RTI workflows.
Judge resonance: security + ops judges both lean civic tech.

## 14 CLIMATE / SUSTAINABILITY
[PREFILL] GHG Protocol reporting, BEE/EESL standards, energy
optimization benchmarks, ESG reporting frameworks (GRI, SASB),
India climate targets (NDC 2070), green IT: energy per inference
(MLPerf power), carbon-aware scheduling (WattTime).
WILDCARD domain, low prior.

## 15 HR / PEOPLE OPS
[PREFILL] onboarding completion, leave policy compliance, bias evals
in hiring AI (AI Fairness 360, Fairlearn, disparate impact tests),
resume parsing evals (F1 on NER), payroll accuracy (tax rules:
TDS/80C), policy Q&A hallucination tests.
WILDCARD, fits KIT-5.

## 16 LEGAL / COMPLIANCE
[PREFILL] LegalBench, CUAD (contracts), CaseHOLD, LexGLUE, SCOTUS
datasets, contract redline accuracy, "not legal advice" guardrail,
DPDPA/GDPR clause detection, policy-vs-action audit tests,
ISO 37301 compliance management.
Careful: never present as legal advice; gate + disclaimer tested.

## 17 RETAIL / E-COMMERCE
[PREFILL] checkout flow correctness, refund idempotency, inventory
consistency (Eventual vs strong), catalog search evals (NDCG@k,
MRR), recommendation evals (precision/recall, diversity), fraud
flags (transaction velocity), return prediction, OWASP API Top 10
for storefronts, payment reconciliation.
Fits KIT-1 (triage shape).

## 18 TRAVEL / LOGISTICS
[PREFILL] delay prediction evals, rerouting optimization, booking
idempotency, fare consistency, ETA accuracy (MAPE), GPS/geofence
tests, shipment tracking integrity, SLAs on disruption alerts.
Fits KIT-1/KIT-5.

## 19 MEDIA / NEWS
[PREFILL] fact-checking evals: FEVER, SciFact, LIAR-PLUS, AVeriTeC,
provenance: C2PA verification tests, summarization: ROUGE/BERTScore/
SummEdits, hallucination: HaluEval, FActScore, XSumFaith, news
classification: AG-News, source credibility ranking, deepfake
detection: FaceForensics++, DFDC, Celeb-DF.
Fits KIT-2 with provenance story.

## 20 SOCIAL GOOD / ACCESSIBILITY
[PREFILL] WCAG 2.2 AA/AAA, axe-core rule coverage, screen reader
compat (NVDA/VoiceOver), keyboard-only navigation, color contrast,
voice-first UX, inclusive language audits, UDID/divyang schemes
(accessibility funding), assistive AI evals (SeeSay-style), low
bandwidth adaptation (Lighthouse on 2G/3G).
Strong judge resonance on both axes.

## 21 DEVTOOLS / CODE
[PREFILL] SWE-bench Verified, SWE-Lancer, HumanEval, MBPP,
LiveCodeBench, Aider polyglot, CodeContests, Defects4J,
CodeQL/static analysis rules, linting standards (Ruff/ESLint),
review evals (CodeReviewer, CRScore), MCP conformance tests,
semver correctness, CI gate standards.
MCP words -> KIT-1 + tool adapters.

## 22 MEETINGS / COLLABORATION
[PREFILL] meeting summarization: MeetingBank, QMSum, AMI, ICSI,
action-item extraction evals, speaker diarization (DER: DIHARD),
ASR WER, agenda adherence, hallucination on who-said-what,
calendar conflict tests, notification fatigue.
Fits KIT-1.

## 23 RESEARCH / ACADEMIC
[PREFILL] paper QA: QASPER, SciQA, ARC (science), literature review
coverage evals, citation accuracy (NEVER fabricate: tested), MathQA/
MATH for math reasoning, retrieval: SciFact, aggregation quality,
"grounded citations" tests (our research standard: every claim [n]).
Our instance: every research wave report cites inline URLs.

## 24 AGRICULTURE
[PREFILL] weather API accuracy (IMD), soil sensor calibration,
advisory correctness (Krishi Vigyan Kendra guidelines), crop
recommendation evals, voice-first Indic support (Bhashini),
MSP/APMC price data integrity, low-bandwidth design.
AI for Bharat family.

## 25 AI FOR BHARAT / INDIC
[PREFILL] Indic ASR: Bhashini datasets, WER benchmarks; Indic MT:
WAT, FLORES-200, IN22; Indic LLM evals: Hinglish, Romanized
transliteration; voice-first UX evals; rural usability studies;
Bhashini API integration tests; multilingual code-switch evals.
VERIFIED theme: AI for Bharat confirmed 2026 hackathon theme.
Kavach DNA fits here (Hindi-first voice).

## 26 RESPONSIBLE AI
[PREFILL] bias: BBQ, CrowS-Pairs, Winogender, StereoSet, FairFace,
disparate impact; explainability: SHAP/LIME fidelity, feature
attribution evals; safety: Anthropic Safety Evaluations, METR
Autonomy, Aviary, AgentHarm, SafetyBench; alignment: HHH
(helpful-harmless-honest), NIST AI RMF conformance, EU AI Act
tiers, MeitY framework 2025-2026; red-team: adversarial suites
(our stress suite S2 injection is an instance).
VERIFIED theme: responsible AI confirmed 2026.

## 27 GAMING / ENTERTAINMENT
[PREFILL] game master coherence evals, NPC response quality,
procedural generation (diversity, novelty), latency (p95 < 100ms),
LLM story consistency (long-context), moderation of user content,
accessibility (colorblind modes).
WILDCARD.

## 28 MUSIC / AUDIO
[PREFILL] playlist eval (precision/recall, diversity), audio quality
(PESQ, STOI), music generation (FAD), ASR on voice notes (WER),
copyright-safe generation tests, metadata correctness.
WILDCARD.

## 29 FOOD / RECIPE
[PREFILL] recipe correctness (ingredient math), dietary constraint
compliance (allergen detection), image->ingredient recognition
(Food-101), nutrition accuracy, regional cuisine coverage.
WILDCARD.

## 30 SMART CITY
[PREFILL] multi-agent dashboard evals (data fusion accuracy),
sensor ingestion integrity, anomaly detection (Numenta NAB,
SWaT), alert fatigue, citizen report routing accuracy
(CPGRAMS-style), geospatial QA.
WILDCARD.

## CROSS-CUTTING: the 5-layer scorecard (VERIFIED from wave-2)
1. outcome correctness -> our 81/81 suites (code-based assertions,
   fresh DBs, zero LLM judges)
2. policy adherence -> approval.py gate + 13/13 policy suite
3. tool-call correctness -> typed registry tests (providers 9/9)
4. trajectory efficiency -> trace ring (200-step cap) + stress
   suite (deadline gates, retry storms)
5. failure recovery -> provider_errors counter, offline flip,
   H1-H6 honesty suite, feeds fallback ladder
Cite these as our benchmark stack: ASVS-grade security checks,
DORA-grade ops checks, HCAST-grade honesty framing, all implemented
as deterministic code tests, not LLM-as-judge.

## TOOLS WE SHIP WITH (for the "how do you test" answer)
k6/JMeter-class load (our stress suite), OWASP ZAP-class checks
(our traversal/injection), Lighthouse-class (our latency budgets
in deadline gates), RAGAS-class (our evidence/rank tests), all
implemented zero-dep in scaffold/tests/. Honest claim: we implement
the CATEGORIES as deterministic checks, and we cite the standards
they instantiate.
