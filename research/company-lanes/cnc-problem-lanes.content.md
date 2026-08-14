# Five Sponsor-Aligned AI Lanes to Prebuild for Craft N Code 2026

## Executive Summary

- **Agentic Infrastructure**: [VERIFIED] Google's 2026 developer messaging centers on an agentic shift, including Managed Agents in the Gemini API, AI Studio expansion, and a stated goal of removing infrastructure friction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights). -> **Decision:** Prebuild a provider-neutral agent runtime with tool calls, approvals, retries, citations, and an event trace; make the Google skin the default demo.

- **Structured Reliability**: [VERIFIED] Gemini supports JSON Schema constrained output, while Google's Java SDK is positioned as a way to switch between the Gemini API and the Gemini Enterprise Agent Platform without rewriting application code [7] (https://ai.google.dev/gemini-api/docs/structured-output) [8] (https://github.com/googleapis/java-genai). -> **Decision:** Treat schema validation, typed actions, and a fallback parser as core infrastructure rather than as a last-minute prompt tweak.

- **Private Personal Intelligence**: [VERIFIED] Apple's Foundation Models framework exposes the on-device and Private Cloud Compute models used for Apple Intelligence [9] (https://developer.apple.com/documentation/foundationmodels), and Apple's research update describes an approximately 3B-parameter on-device language model [10] (https://machinelearning.apple.com/research/apple-foundation-models-2025-updates). -> **Decision:** Keep a privacy-first, offline-capable skin ready, but do not make the whole entry depend on an Apple-only environment unless the event confirms that an actual Apple runtime is available.

- **Multimodal Distribution**: [VERIFIED] Meta introduced Llama 4 Scout and Maverick as open-weight, natively multimodal models with very large context support [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence). Meta's WhatsApp Cloud API onboarding explicitly includes app creation, a test webhook endpoint, secure access tokens, and template and non-template messages [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). -> **Decision:** Prebuild a text-image-message adapter and a human handoff path; use WhatsApp as a distribution skin only after credentials and webhook connectivity pass the first gate.

- **Enterprise AI Operations**: [VERIFIED] Accenture's FY2025 annual report states **$69.7B** in revenue, **$1.5B** invested across **23 strategic acquisitions**, **$0.8B** in R&D, about **$1.0B** in learning and professional development, **77,000** skilled AI and data professionals, and **47M hours** of training [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf). -> **Decision:** Have a document-to-workflow and governance skin ready, because an enterprise problem can reward measurable cycle-time reduction more than a generic chatbot.

- **Creative Production**: [VERIFIED] Adobe describes Firefly as generating image, video, audio, and more with **30+ AI models** [13] (https://firefly.adobe.com/), while its 2026 announcement describes expanded agentic capabilities across Firefly and Creative Cloud [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion). -> **Decision:** Prebuild a creative-brief-to-variants workflow with brand constraints, approval, provenance fields, and a human edit step; do not prebuild a fragile one-shot image generator.

- **Compliance Clock**: [VERIFIED] The European Commission says the AI Act entered into force on 1 August 2024 and became applicable on 2 August 2026, with exceptions including prohibited practices and AI literacy obligations [15] (https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai). The Commission also published an Article 50 transparency FAQ in July 2026 [16] (https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act). -> **Decision:** Add consent, disclosure, source, retention, and audit fields to every skin. India-specific DPDPA timing must be checked against the event brief rather than guessed from the rules page [5] (https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025).

- **Evidence Confidence**: [UNVERIFIED] The search pass did not locate a public, official Craft N Code 2026 Rajasthan qualifier page confirming the five sponsors, the Aug 15-16 dates, the rubric, or the actual challenge wording. Those details are treated as the team's insider premise, not as verified event facts. -> **Decision:** Build a flexible engine, ask for the exact sponsor lane and required APIs at reveal, and score each problem against the kill criteria below before committing.

## 1. How to Read Sponsor Signals Without Mistaking Marketing for a Leak

The evidence-mining method is useful only when it separates observation from prediction. A product launch is an observation. A complaint is an observation only when the team can point to a reproducible issue, a discussion with a concrete failure mode, or a documented workaround. The problem statement is a prediction. The winning solution is a design recommendation. Mixing those levels creates false confidence, especially when a sponsor's public messaging is broad enough to cover almost any AI demo.

Use four labels throughout the weekend. **[VERIFIED]** means the cited primary or near-primary source explicitly states the fact. **[INFERRED]** means the team is connecting at least two verified signals into a plausible problem shape; it is a useful bet, not a leak. **[UNVERIFIED]** means the claim could be true but the research pass did not produce a citable confirmation. An unverified claim can still be a question to ask at the reveal, but it should not be the foundation of the architecture.

The second-signal rule is the central discipline. Do not select a lane because a company announced one fashionable feature. Select it when two independent signals point to the same underlying job. For example, Google has both an agentic product direction and a developer message about removing infrastructure friction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights). That combination is stronger than either announcement alone. Likewise, Adobe has both a broad creative-agent expansion [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion) and an asynchronous Firefly API whose documentation discusses job status for generation, composite, and upscale operations [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api). The likely hole is not merely "make an image"; it is "make a production workflow reliable enough to review and ship."

The third discipline is negative evidence. The search pass found official documentation and product pages for all five sponsor ecosystems, but it did not produce a robust, citable set of Reddit, X, or GitHub complaint excerpts for every sponsor. Therefore, claims such as "developers hate X" are deliberately not presented as facts. The team should mine complaints live only when a post identifies a repeatable failure, the affected API or SDK, and a workaround that a student team can demonstrate.

### Evidence ledger: what is strong, what is directional, and what remains open

| Sponsor | Verified public signal | Likely underlying job | Confidence | What Team 511 should do |
|---|---|---|---|---|
| Google | Agentic era, Managed Agents, AI Studio expansion, and infrastructure-friction language [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights); JSON Schema output [7] (https://ai.google.dev/gemini-api/docs/structured-output) | Make agents reliable, typed, observable, and easy to connect to tools | [INFERRED] High | Build the core runtime around typed actions and traces |
| Apple | Foundation Models access to on-device and Private Cloud Compute models [9] (https://developer.apple.com/documentation/foundationmodels); approximately 3B on-device model described by Apple [10] (https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | Useful private intelligence with graceful device and availability handling | [INFERRED] Medium-high | Build a local-first privacy skin and a non-Apple fallback |
| Meta | Llama 4 Scout and Maverick are open-weight and natively multimodal [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence); WhatsApp setup requires tokens and webhooks [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started) | Multimodal, open-model applications distributed through social and messaging surfaces | [INFERRED] High | Build the message adapter, but gate it on credentials |
| Accenture | FY2025 report gives the scale of AI hiring, training, acquisitions, and R&D [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf); responsible-AI page names an implementation gap [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai) | Move AI from pilot to governed enterprise process and measurable value | [INFERRED] High | Build document-to-decision workflow with audit and human approval |
| Adobe | Firefly supports image, video, audio, and more with 30+ models [13] (https://firefly.adobe.com/); Creative Agent expansion [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion); API status and troubleshooting docs [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting) [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api) | Turn generative output into controlled, reviewable creative production | [INFERRED] High | Build brief, variants, constraints, approval, and provenance |

The table's main takeaway is that the common denominator is not "use an LLM." It is a controlled interface between a model and a real workflow. The reusable primitives are evidence, structured state, tool access, approval, fallback, and a visible outcome. Those primitives let the team change the story without throwing away the code.

## 2. What Each Sponsor Appears Obsessed With in 2026

### 2.1 Google: agents that remove infrastructure friction

[VERIFIED] Google's I/O 2026 developer highlights describe Antigravity, Managed Agents in the Gemini API, and expansions to AI Studio, with the explicit goal of making it easier for developers to bring ideas to life by removing infrastructure friction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights). The broader May 2026 update frames the moment as an "agentic" era and names Gemini 3.5 and Gemini Omni as products for advanced reasoning and creation [19] (https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026). Google Search's I/O update also describes information agents that monitor the web, news, social posts, and fresh finance, shopping, and sports data [20] (https://blog.google/products-and-platforms/products/search/search-io-2026).

The mechanism is straightforward: once the product story moves from chat to agents, the hard problem moves from generating a paragraph to coordinating a chain of retrieval, planning, tool use, state, and user confirmation. A student project that merely wraps a prompt may look interchangeable. A project that shows a plan, cites the evidence used, asks before taking an external action, and recovers from a failed tool call looks like the missing layer around the model.

[VERIFIED] The Gemini developer site presents Gemini as a coding agent that can plan and execute tasks [21] (https://ai.google.dev/), and the structured-output documentation says a developer can configure responses to follow a supplied JSON Schema for predictable, type-safe extraction [7] (https://ai.google.dev/gemini-api/docs/structured-output). The Java Gen AI SDK documentation further emphasizes switching between Gemini API and Gemini Enterprise Agent Platform backends without rewriting the application [8] (https://github.com/googleapis/java-genai). These are direct signals that interface contracts, portability, and orchestration matter.

[INFERRED] The likely Google problem shape is therefore not "build a chatbot for any topic." It is closer to: "Build an agent that completes a multi-step task using trusted data and tools, returns typed results, exposes its reasoning evidence, and fails safely." The best pre-build is an agent gateway that makes model calls replaceable. The team should be able to mount a campus-help, lab-inventory, emergency-information, or student-services skin on the same runtime.

### 2.2 Apple: private intelligence at the device boundary

[VERIFIED] Apple's Foundation Models documentation says the framework provides access to large language models including the on-device and Private Cloud Compute models designed for Apple Intelligence [9] (https://developer.apple.com/documentation/foundationmodels). Apple's research update describes the Foundation Models framework as an access point for production-quality generative AI features and identifies an approximately 3B-parameter on-device language model [10] (https://machinelearning.apple.com/research/apple-foundation-models-2025-updates). Apple's 2026 newsroom announcement says its upcoming software releases deliver the next generation of Apple Intelligence and introduce Siri AI [22] (https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more).

The mechanism is different from Google's cloud-first agent narrative. Apple's distinctive design constraint is the boundary between personal data and computation. The attractive problem is not just better generation. It is useful generation that can remain on the device, use a private cloud path when appropriate, degrade gracefully when the model is unavailable, and make the privacy behavior legible to the user.

There is also a concrete environment-readiness warning. [VERIFIED] An Apple Developer Forums thread about Foundation Models in the simulator says that running Foundation Models in Simulator requires an up-to-date macOS environment [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022). This is not evidence that the framework is broadly unreliable. It is evidence that a student team can lose its entire demo to a platform prerequisite if it treats the Apple integration as an assumption rather than a gate.

[INFERRED] The likely Apple problem shape is: "Build a private, on-device assistant that transforms sensitive personal content into a useful action or structured summary without sending unnecessary data to a server." A strong demo should visibly toggle between on-device, private-cloud, and unavailable states, although the exact runtime must be confirmed at the event. The recommended architecture isolates the Apple adapter behind the same `ModelProvider` interface used by the cloud adapters. That makes privacy a real product property, not a decorative claim.

### 2.3 Meta: open multimodal models plus distribution through conversations

[VERIFIED] Meta's April 2025 Llama 4 announcement introduces Scout and Maverick as the first open-weight, natively multimodal models in the Llama family and highlights unprecedented context-length support [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence). Meta's Llama repository and cookbook position the ecosystem around building, fine-tuning, retrieval-augmented generation, and related workflows [1] (https://github.com/meta-llama). The model signal points toward applications that accept more than a text prompt and can use a large working context.

The distribution signal is equally important. [VERIFIED] Meta's WhatsApp Cloud API getting-started guide describes registering as a developer, creating a Meta app, sending a first message, setting up a test webhook endpoint, and using secure access tokens for template and non-template messages [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). This gives a concrete shape to the platform problem: a useful model has to survive message events, media, identity, templates, and human escalation, not just produce a response in a notebook.

[INFERRED] The likely Meta problem statement is: "Build a multimodal community or commerce assistant that understands text and images in a messaging flow, retrieves trusted information, replies in the user's channel, and escalates uncertain cases to a human." The high-value part is the loop around the model: intake, classification, retrieval, response, confidence, and handoff. A student team should not attempt to train a model in 24 hours. It should demonstrate a small, well-instrumented slice using a provider adapter and a deterministic fixture set when live credentials fail.

The main risk is dependency on the event's Meta app permissions, test phone number, webhook reachability, and template policy. The setup documentation makes those dependencies visible [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). That is why the Meta skin should be a mount, not the engine.

### 2.4 Accenture: enterprise AI that crosses the pilot-to-value gap

[VERIFIED] Accenture's FY2025 annual report reports **$69.7B** in revenue. It also reports **$1.5B** of investment across **23 strategic acquisitions**, **$0.8B** in R&D, approximately **$1.0B** in learning and professional development, **47M training hours**, and approximately **77,000** skilled AI and data practitioners at the end of fiscal 2025, against a goal of doubling its AI and data workforce to **80,000** by the end of fiscal 2026 [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf). The company also announced the acquisition of AI company Halfspace in 2025 [24] (https://newsroom.accenture.com/news/2025/accenture-acquires-halfspace-to-bolster-ai-capabilities-in-the-nordic-region) and agreed to acquire creator and social agency Whalar in 2026 [25] (https://newsroom.accenture.com/news/2026/accenture-to-acquire-leading-creator-and-social-agency-whalar-from-whalar-group).

The mechanism is enterprise integration. Accenture's public AI services page is framed around data and AI solutions for enterprises [3] (https://www.accenture.com/us-en/services/ai-data), not a single consumer feature. Its responsible-AI page explicitly discusses an implementation gap that can undermine trust, compliance, and innovation [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai). Its discussion of sovereign AI says that integrating sovereign solutions can address security and compliance complexities across data, infrastructure, models, and agents [26] (https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value).

[INFERRED] A sponsor-authored Accenture problem is likely to reward a workflow with an owner, a queue, a measurable before-and-after, and a control point. The best lane is not "summarize a PDF." It is "turn incoming documents or requests into structured cases, route them, identify risk, recommend a next action, and preserve an auditable human decision." The demo must show the business metric: fewer manual steps, faster triage, fewer missed fields, or more consistent policy checks.

This lane is particularly useful as a fallback because it can be skinned for a college office, lab safety process, insurance claim, procurement queue, or customer support desk. It is also the lane most likely to survive a sponsor reveal that changes the domain but keeps the workflow shape.

### 2.5 Adobe: generative media moving into controlled production

[VERIFIED] Adobe's Firefly page describes an all-in-one creative AI studio that generates image, video, audio, and more with **30+ AI models** [13] (https://firefly.adobe.com/). Adobe's June 2026 announcement describes a major expansion of its Creative Agent across Firefly and Creative Cloud, with expanded agentic capabilities [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion).

The mechanism is production workflow rather than isolated novelty. Once a creative agent can help with a brief, assets, variations, and edits, the problem becomes managing constraints and review. Brand rules, format requirements, rights or provenance metadata, user approvals, and asynchronous job state become as important as the generated pixels.

[VERIFIED] Adobe's Firefly API reference describes checking the status of an asynchronous job and includes generation, composite, and upscale operation types [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api). Adobe also publishes a troubleshooting guide for common Firefly API issues [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting). An unofficial Firefly MCP server advertises Firefly image and video generation from desktop AI clients [27] (https://github.com/krishnapallapolu/adobe-firefly-mcp/blob/main/README.md). The last item is not an Adobe endorsement; it is a visible workaround-shaped signal that developers want to connect Firefly capabilities to agent tooling.

[INFERRED] The likely Adobe problem statement is: "Build a creative production assistant that turns a brief and brand kit into multiple channel-ready variants, enforces constraints, tracks generation state, and routes the output for human approval." The team can win without competing on raw image quality. It can win on a crisp before-and-after workflow, a constraint violation caught visibly, and a clear path from brief to approved asset.

## 3. Complaint Mining and Workaround Detection: What Is Actually Safe to Claim

The requested method calls for Reddit, GitHub issues, X, and workaround discovery. The evidence pass should not turn search-result absence into a claim about developer sentiment. The safe conclusion is narrower: official documentation exposes several friction surfaces, and a few public artifacts point toward integration workarounds. Those surfaces are enough to design a robust scaffold, but they are not enough to say that a particular API is universally hated.

### Friction ledger

| Ecosystem | Directly observed friction or workaround-shaped signal | Evidence status | Product-shaped hole |
|---|---|---|---|
| Google | Google says its new developer products remove infrastructure friction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights). Structured output is documented as a way to make extraction predictable and type-safe [7] (https://ai.google.dev/gemini-api/docs/structured-output). | [VERIFIED] friction is stated by Google; actual community complaint volume is [UNVERIFIED] | Agent runtime with schema validation, retries, traces, and provider fallback |
| Apple | A Foundation Models simulator thread identifies an up-to-date macOS prerequisite [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022). | [VERIFIED] for the thread's environment issue; general reliability claims are [UNVERIFIED] | Environment check, capability probe, local/cloud fallback, and a prerecorded fixture |
| Meta | WhatsApp onboarding requires app setup, a test webhook, secure tokens, and message-template handling [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). | [VERIFIED] setup surface; developer frustration and workaround frequency are [UNVERIFIED] | Webhook simulator, event replay, token check, template/non-template adapter, human handoff |
| Accenture | Accenture describes a responsible-AI implementation gap [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai) and security/compliance complexity across sovereign AI layers [26] (https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value). | [VERIFIED] strategic problem framing; not a Reddit complaint dataset | Governance layer, policy check, decision log, owner and escalation queue |
| Adobe | Firefly has a troubleshooting guide [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting), asynchronous job status [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api), and an unofficial MCP integration [27] (https://github.com/krishnapallapolu/adobe-firefly-mcp/blob/main/README.md). | [VERIFIED] documentation and workaround artifact; broad complaint claim is [UNVERIFIED] | Job queue, progress state, retry, asset manifest, brand checks, and approval |

The practical implication is that Team 511 should build around failure visibility. A demo that hides the provider call is fragile. A demo that shows "provider unavailable, replaying a cached fixture" or "output rejected by schema, retrying with repair" turns a failure into proof that the system was designed for reality.

### How to mine a real complaint during the event

When the team sees a Reddit, GitHub, or X claim, record five fields before using it: the exact product or endpoint, the date or version, the reproducible symptom, the workaround, and the user value lost. A post that says "API bad" is not evidence. A reproducible report that a webhook event is not replayable, a structured response fails on a known schema, or a generation job has no useful progress state is evidence of a problem shape. The team should convert that into a narrow feature, not a broad complaint narrative.

A good workaround has a cost. Spreadsheets, manual copy-paste, scripts, and unofficial bridges persist because the official path leaves a gap between a model capability and a finished workflow. The solution should remove one such cost in a visible way. Do not build a general platform in 24 hours. Build one repeatable loop with a clear input, one or two actions, a guardrail, and a measurable output.

## 4. Regulatory Clocks That Can Create Forced Problem Statements

### EU AI Act: the clearest dated signal

[VERIFIED] The European Commission says the AI Act entered into force on 1 August 2024 and became applicable on 2 August 2026, with exceptions including prohibited AI practices and AI literacy obligations [15] (https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai). The Commission also has an Article 50 transparency FAQ dated July 24, 2026 [16] (https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act).

[INFERRED] For a hackathon, this creates a reliable cross-cutting skin: an AI interaction should disclose that AI is involved when appropriate, attach source and provenance fields, record the model and version, preserve a human decision, and make escalation visible. The team should not claim legal compliance from a prototype. It should demonstrate compliance-aware product design and clearly state that the prototype is not legal advice.

### India DPDPA: use the official rules page, do not invent a deadline

[VERIFIED] The Ministry of Electronics and Information Technology has an official page titled "Digital Personal Data Protection Rules 2025" with documents and an enforcement entry [5] (https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025). The search excerpt available for this report does not establish a specific effective date, transition period, or event-specific requirement.

[UNVERIFIED] Do not tell judges that a particular DPDPA deadline is active unless the challenge brief or the current official text confirms it. Instead, build consent capture, purpose limitation, deletion or retention state, access control, and an audit trail as product features. These are prudent engineering choices even when the exact legal classification of the demo is unknown.

### United States policy: keep it as an open question

[UNVERIFIED] The research pass did not return a citable White House or agency excerpt that establishes a current 2026 US executive-order requirement relevant to this particular student prototype. The team should not anchor a problem ranking to a claimed US deadline. If the sponsor brief explicitly names a US rule, add it to the policy configuration and ask the sponsor for the intended scope.

### Why regulation belongs in the engine, not a separate demo

A governance panel that is disconnected from the user journey looks like decoration. A governance gate inside the workflow is a product. For example, the same `PolicyDecision` object can determine whether a WhatsApp reply requires human review, whether an Apple private-data action can leave the device, whether an Adobe asset carries a provenance field, or whether an Accenture-style enterprise case can be closed without an approver. This design converts a legal uncertainty into an observable engineering control.

## 5. The Five Most Likely Problem Statements, Ranked

The ranking below is a forecast, not leaked wording. Each statement is intentionally phrased in the style commonly used for sponsor challenge prompts: a user, a painful workflow, an AI capability, a safety or trust constraint, and a measurable outcome. The evidence chain uses a second-signal rule where possible. The team should re-rank immediately after reading the actual brief.

| Rank | Predicted problem statement text shape | Likely sponsor | Evidence chain | Winning solution | 24h MVP and demo gate |
|---:|---|---|---|---|---|
| 1 | "Build a trustworthy agent that plans a multi-step task, retrieves evidence, uses approved tools, requests confirmation before side effects, and produces a typed audit trail." | Google, with Accenture overlap | Google agentic direction and infrastructure-friction language [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights); structured output [7] (https://ai.google.dev/gemini-api/docs/structured-output); Accenture responsible-AI implementation gap [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai) | Evidence-first agent gateway with policy gate, tool registry, approval, retry, and trace | Two tools, one knowledge base, typed action schema, one deliberate failure, one approval, one audit export |
| 2 | "Build a creative production agent that converts a brief into constrained, channel-ready variants and routes them through review with provenance." | Adobe | Firefly supports 30+ models and multiple media types [13] (https://firefly.adobe.com/); Adobe expanded Creative Agent [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion); API has asynchronous job state [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api) | Brand kit plus creative brief, variant generator, constraint checker, asset manifest, approval | Three variants, one constraint failure caught, one approved export, fallback fixture if API is unavailable |
| 3 | "Build private personal intelligence that summarizes or transforms sensitive content on device, discloses data movement, and works when the private model is unavailable." | Apple | Foundation Models uses on-device and Private Cloud Compute models [9] (https://developer.apple.com/documentation/foundationmodels); approximately 3B on-device model [10] (https://machinelearning.apple.com/research/apple-foundation-models-2025-updates); simulator prerequisite [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022) | Local-first privacy cockpit with capability probe and explicit fallback | One sensitive fixture, local transformation, privacy status, unavailable-state fallback, no unverifiable privacy claim |
| 4 | "Build a multimodal assistant on a messaging channel that handles text and images, retrieves trusted answers, uses approved templates, and escalates uncertainty." | Meta | Llama 4 open-weight multimodality [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence); WhatsApp webhook/token/template setup [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started) | Message event adapter, multimodal classifier, RAG, confidence gate, human handoff | One webhook or replay simulator, two modalities, three intents, one escalation, one response template |
| 5 | "Build an AI workflow that turns unstructured requests into governed enterprise cases, routes the next action, and preserves consent, evidence, and a human decision." | Accenture, with Google or Adobe overlap | Accenture's AI workforce and investment scale [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf); responsible-AI gap [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai); sovereign complexity across data, infrastructure, models, and agents [26] (https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value) | Document intake, extraction, risk policy, routing, approval, audit, and KPI card | Ten sample cases, structured extraction, one exception, one human approval, before/after cycle-time counter |

### Why Rank 1 is the safest common denominator

[INFERRED] The agent-reliability lane sits first because it can absorb all five sponsor directions. Google's agent platform is the obvious skin. Accenture's governance and implementation gap provide the enterprise story. Apple's private model becomes a local provider. Meta's WhatsApp becomes a tool or channel. Adobe's generation job becomes an asynchronous tool with approval. A single reliable orchestration core therefore gives the team more optionality than a narrow vertical app.

The risk is genericness. "Trustworthy agent" is not a user problem until it has a concrete job. The team should prepare three interchangeable stories: campus incident triage, lab-equipment service request, and small-business campaign approval. At reveal, select the story whose data and sponsor nouns match the official prompt. Keep the engine unchanged.

### Why Rank 2 can win with a short, visual demo

Adobe is a strong lane because the result is visible in seconds. [VERIFIED] Firefly's public product surface spans image, video, audio, and more with 30+ models [13] (https://firefly.adobe.com/), while the Creative Agent announcement explicitly moves toward expanded agentic capabilities [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion). The inference is that a production workflow around creative output may matter more than a raw generation comparison.

The risk is API access, generation time, credits, and inconsistent output. The solution is to prebuild a fixture mode containing approved sample assets and fake asynchronous job events. If the live call works, use it. If it does not, demonstrate the same state machine with a clearly marked fixture. Never pretend a cached image was generated live.

### Why Rank 3 is high-value but platform-risky

Apple's on-device and Private Cloud Compute positioning [9] (https://developer.apple.com/documentation/foundationmodels) makes privacy a strong differentiator. The approximately 3B on-device model detail [10] (https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) supports a credible local-first story. The simulator thread [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022) supplies the operational warning: platform setup can consume the time that should be spent on the product.

The winning demo is a privacy state machine, not a vague claim that "nothing leaves the device." Show a local fixture, show the transformation, show the data-movement indicator, then deliberately disable the capability and show a safe fallback. If the framework cannot run on the team's available machine, switch to a web simulation that labels the Apple adapter as simulated. A truthful simulation is better than an unsupported privacy claim.

### Why Rank 4 depends on distribution plumbing

Llama 4 gives Meta a strong multimodal model signal [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence). WhatsApp provides a concrete user channel but adds app, token, webhook, and template dependencies [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). The problem statement should therefore include a user and a conversation, not just a model benchmark.

The winning demo starts with a real or replayed inbound message, attaches an image, identifies the intent, retrieves one trusted answer, and either responds through the channel or creates a human task. A response that cannot be audited or escalated is weaker than a smaller response that can. Kill this lane early if the webhook and credentials do not pass the first gate.

### Why Rank 5 is the best non-glamorous enterprise fallback

Accenture's reported AI workforce, acquisition, R&D, and training investment [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf) indicates a large enterprise transformation surface. The responsible-AI page describes an implementation gap [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai), and the sovereign-AI discussion names complexity across data, infrastructure, models, and agents [26] (https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value). These signals support a governed process problem rather than a generic chat experience.

A good enterprise demo is measurable. Start with ten requests and a manual process counter. Extract fields, route the request, flag one exception, and show an approver's decision in the audit log. If the judges ask, "Why does this need AI?" the answer should be that the system converts messy intake into structured work while preserving human control, not that the interface has a chatbot.

## 6. Detailed Build Cards: Solution, MVP, Demo, and Kill Criteria

### Build Card 1: Evidence-first agent gateway

**Predicted prompt.** "Build a trustworthy agent that completes a multi-step task across approved tools, cites the evidence behind each decision, asks for confirmation before side effects, and records a replayable audit trail." This is [INFERRED] from Google's agent and infrastructure-friction direction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights), structured output [7] (https://ai.google.dev/gemini-api/docs/structured-output), and Accenture's stated responsible-AI implementation gap [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai).

**Winning solution.** Build a small state machine, not an autonomous free-for-all. The user request enters a planner. The planner selects from a typed tool registry. Retrieval produces `EvidencePacket` objects containing source, passage, timestamp, and confidence. The model proposes an `Action`; a policy gate checks whether it is read-only, reversible, or side-effecting. Only the last class requires an explicit approval. Every transition becomes a `TraceEvent` that can be replayed.

**24h MVP.** Use one small fixture knowledge base and two tools: a read-only search tool and a simulated update or notification tool. Implement one JSON schema for the answer and one for the action. Add a deliberate invalid tool argument, a retry or repair path, and a visible approval modal. Export the trace as JSON or a readable timeline. Do not attempt ten tools, long-term memory, or a general-purpose agent.

**Demo script.** Start with an ambiguous request such as "Find the lab devices due for calibration and notify the responsible student." The agent asks one clarification or states its assumption. It retrieves two evidence records, shows the due date and source, proposes a notification, pauses for approval, then executes the simulated tool. Trigger a malformed action once. The validator rejects it, the repair path runs, and the final trace shows both the failure and the safe recovery.

**Kill criteria.** Abandon the lane or narrow it if the team cannot produce a stable trace after two hours; if the model cannot reliably emit the typed action after three constrained retries; if the tool call has no deterministic fixture; or if the demo still depends on a live external API that has not passed a smoke test. A smaller read-only evidence assistant is preferable to a broken autonomous agent.

### Build Card 2: Brand-safe creative production agent

**Predicted prompt.** "Given a campaign brief and brand kit, produce channel variants, enforce brand constraints, track asynchronous generation, and send only approved assets to export." This is [INFERRED] from Firefly's multi-media, 30-plus-model product surface [13] (https://firefly.adobe.com/), Creative Agent expansion [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion), and the Firefly API's job-status model [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api).

**Winning solution.** Separate creative intent from generation. Parse the brief into audience, claim, channel, dimensions, tone, forbidden terms, and required elements. Generate or retrieve variants. Run a constraint checker against text and metadata. Put each asset into `draft`, `needs_review`, `approved`, or `rejected`. The strongest visual is a side-by-side showing the original brief, three variants, a flagged violation, and the approved manifest.

**24h MVP.** Use a small brand kit with logo, palette, tone, and prohibited claims. Support one image channel and one copy channel. Implement a fake or live asynchronous job adapter, a progress indicator, a simple constraint checker, and an approval button. Include a provenance record with prompt, model adapter, timestamp, input asset identifiers, and reviewer. Adobe's troubleshooting documentation [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting) is a reminder to expose useful error state rather than leave a blank spinner.

**Demo script.** Paste a campaign brief for a university event. The agent proposes a square social post, a story variant, and a caption. One variant violates the brand rule or contains a banned claim. The checker marks it red, explains the rule, and asks for a revision. The reviewer approves the corrected variant and downloads an asset manifest. If Firefly is connected, show the live job status. If not, label the fixture mode and show the same workflow without misrepresenting its origin.

**Kill criteria.** Switch to an asset-governance or content-review skin if live generation is not authenticated, if generation latency threatens the demo, if the output cannot be distinguished from a preloaded fixture, or if the team has no visible constraint beyond "looks good." Do not spend the final six hours trying to improve image quality by prompt iteration.

### Build Card 3: Private personal intelligence cockpit

**Predicted prompt.** "Build an assistant that transforms sensitive notes, messages, or health-adjacent personal data on device, clearly indicates where processing occurs, and degrades safely when the local model is unavailable." This is [INFERRED] from Apple's Foundation Models documentation [9] (https://developer.apple.com/documentation/foundationmodels), the approximately 3B on-device model description [10] (https://machinelearning.apple.com/research/apple-foundation-models-2025-updates), and the simulator environment signal [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022).

**Winning solution.** Make data movement the main interface. Each request displays a capability state: `on_device`, `private_cloud`, `server_fallback`, or `unavailable`. The user can view the fields that may leave the device and can refuse the fallback. The system returns a structured result, not an unbounded chat paragraph. If no approved model is available, it offers a deterministic local rule or asks the user to retry rather than silently sending data elsewhere.

**24h MVP.** Use one sensitive-looking but synthetic dataset, such as a student's timetable and personal reminders. Implement summarization or task extraction, a privacy indicator, one local or simulated provider, one disabled-provider path, and an audit screen showing what was processed. Include a clear disclaimer that the data is synthetic and the prototype is not a medical or legal product. The fallback should preserve user control, not merely display an error.

**Demo script.** Paste a synthetic personal note. The assistant extracts three tasks and shows `on_device` processing. Disable the local capability. The interface now displays `unavailable` or asks for consent before a cloud fallback. The user refuses; the system retains the note locally and gives a safe alternative. This creates a much stronger privacy story than claiming a backend cannot see data without showing any control.

**Kill criteria.** Pivot after 60-90 minutes if the required Apple framework cannot run on the available environment, if the team cannot verify where computation occurs, or if the privacy state is only a label with no behavior behind it. Mount the same privacy policy on the Google or Meta adapter and present it as a privacy-aware assistant instead.

### Build Card 4: Multimodal WhatsApp or social-channel triage assistant

**Predicted prompt.** "Build a multimodal assistant that accepts text and images in a messaging channel, identifies the request, retrieves a trusted answer, responds with an approved format, and escalates low-confidence cases." This is [INFERRED] from Llama 4's natively multimodal direction [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence) and WhatsApp's documented webhook, token, and template setup [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started).

**Winning solution.** Define a channel-neutral event format: sender, channel, text, media references, timestamp, consent, and conversation id. Route events through an intent classifier and retrieval layer. The response policy chooses between direct answer, clarifying question, approved template, or human task. Store the original media reference and the evidence used. The demo can use WhatsApp, a local event replay, or a simple web chat, but the adapter boundary must be visible.

**24h MVP.** Support three intents and two modalities. Use one trusted FAQ or small catalog. Add one simulated human queue. Include a webhook health check and a replay button that can inject known events. If live credentials are available, connect them. If not, use the same event JSON and disclose that the transport is simulated. The model is not the differentiator; the reliable conversation loop is.

**Demo script.** Send a text question and an image of a product or lab label. The assistant identifies the intent, extracts the relevant attribute, cites the FAQ entry, and returns an approved response. Send an ambiguous image. The confidence gate refuses to guess and creates a human task. Show the conversation id and audit trail. This demonstrates safety and utility in less than three minutes.

**Kill criteria.** Stop investing in the live channel if app creation, access tokens, test phone, or webhook delivery fails the first connectivity check. Switch to replay mode if the same user journey can still be demonstrated. Kill the entire lane if it has no human handoff or if the team is using a fabricated live response.

### Build Card 5: Governed enterprise case router

**Predicted prompt.** "Build an AI workflow that turns unstructured requests into structured cases, recommends routing and next actions, checks policy, and preserves evidence, consent, and a human decision." This is [INFERRED] from Accenture's enterprise AI scale and investment [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf), responsible-AI implementation framing [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai), and sovereign data and compliance concerns across models and agents [26] (https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value).

**Winning solution.** Build a case object with owner, priority, extracted fields, evidence links, policy flags, next action, due date, consent state, and reviewer. Use AI for extraction and recommendation, not final authority. Present a queue with one normal case, one incomplete case, and one policy exception. Give the judge a simple KPI: manual fields reduced, triage time reduced in the fixture, or cases routed consistently.

**24h MVP.** Load ten synthetic documents or messages. Extract five fields into a schema. Route them into two queues. Flag one missing consent or unsupported claim. Add one approval and one rejection. Export a case history. Keep the domain narrow: lab maintenance, campus admissions, scholarship queries, or small-business service requests. Do not attempt an enterprise-grade identity system.

**Demo script.** Drop three requests into the queue. The system extracts fields and shows the source passage for each. A normal request is routed and approved. A missing field triggers a clarification. A high-risk request is held for a human and displays its policy reason. The dashboard compares the manual and assisted steps. Finish by showing a trace that a manager could inspect.

**Kill criteria.** Narrow the domain if field extraction accuracy is poor on the fixture, if the KPI cannot be calculated, or if the policy layer is a static paragraph with no effect on routing. If sponsor language turns out to be creative or messaging-specific, reuse the case object for asset approval or conversation escalation.

## 7. The Five Cross-Cutting Solution Patterns to Prebuild Regardless of the Problem

The following patterns are the portable substrate. They are recommendations, so their mount times are team targets, not externally verified facts. The strategy is to build the engine before the reveal and add only a thin skin after the reveal.

| Pattern | Scaffold component to prebuild | Target mount time after reveal | Demo script | Why it maps to sponsor signals |
|---|---|---:|---|---|
| 1. Evidence-first structured answers | Ingestor, chunk store, retriever, source card, JSON Schema validator, repair loop | 15-25 minutes | Ask a question, show two source cards, deliberately break a field, show repair, export typed answer | Google explicitly promotes structured output for predictable, type-safe results [7] (https://ai.google.dev/gemini-api/docs/structured-output); enterprise governance needs evidence [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai) |
| 2. Tool gateway with approval | Typed tool registry, policy gate, dry-run mode, approval modal, rollback or simulated side effect | 20-30 minutes | Plan task, call read-only tool, pause before write, approve, show audit event | Google's Managed Agents direction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights) and Accenture's agent governance framing [26] (https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value) |
| 3. Multimodal and channel adapter | Normalize text, image, audio placeholder, webhook or replay event, human handoff | 15-25 minutes | Send text, attach image, classify, retrieve, respond, escalate uncertainty | Llama 4 is natively multimodal [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence); WhatsApp requires event and token plumbing [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started) |
| 4. Privacy, provenance, and consent layer | Data classification, processing-location badge, consent record, retention flag, provenance manifest | 10-20 minutes | Show what data is used, where it is processed, ask consent, display source and model metadata | Apple emphasizes on-device and Private Cloud Compute models [9] (https://developer.apple.com/documentation/foundationmodels); EU transparency guidance is current [16] (https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50) |
| 5. Evaluation and failure observability | Golden fixtures, latency and cost placeholders, confidence, trace viewer, provider fallback, demo replay | 10-20 minutes | Run one happy path and two failure paths, compare expected and actual, replay trace | Google's infrastructure-friction message [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights) and Adobe's troubleshooting and async-job surfaces [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting) [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api) |

The takeaway is that the team should prebuild controls, not a finished vertical application. A source card can support a Google research agent, an Accenture case router, an Apple private assistant, a Meta FAQ bot, or an Adobe brief checker. A tool gateway can wrap a notification, a WhatsApp send, an asset export, or a case assignment.

### Pattern 1: evidence-first structured answers

The scaffold should treat every answer as a record, not a string. Define fields for `answer`, `confidence`, `evidence`, `unknowns`, and `next_action`. The evidence card should show a source label, a short passage, and a timestamp or fixture identifier. The JSON Schema validator should reject missing required fields and send a compact repair request. This directly matches Google's documented purpose for structured output: predictable, type-safe results [7] (https://ai.google.dev/gemini-api/docs/structured-output).

The demo skin can change from "find a campus policy" to "extract fields from a service request" to "answer a WhatsApp question" without changing the renderer. If a judge asks whether the model hallucinated, the team can point to the evidence and the validator. If the model is wrong, the failure is visible and recoverable.

### Pattern 2: tool gateway with approval

Represent tools as records: name, description, input schema, side-effect class, required approval, and simulated result. Never let the model invent an arbitrary function call. The policy gate should distinguish read-only, reversible, and side-effecting operations. In the demo, the action should pause before a notification, export, case closure, or external message.

This is a better interpretation of agentic building than adding a loop around a chat call. It makes the causal chain inspectable: observation, plan, proposed action, policy decision, user approval, execution, result. It also makes a failure case easy to stage without damaging a real account.

### Pattern 3: multimodal intake and channel adapters

Normalize every incoming event into one object. Use `channel`, `sender`, `text`, `media`, `conversation_id`, and `consent`. A WhatsApp webhook, a web upload, a phone camera, and a local fixture should all become the same object. The model provider should receive a stable internal representation, while the transport adapter handles channel-specific details.

This pattern is justified by Meta's Llama 4 multimodal signal [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence) and the documented WhatsApp setup surface [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). It also protects the team from credentials. A replay button can prove the product loop even when a webhook is unavailable.

### Pattern 4: privacy, provenance, and consent

Build a small policy object rather than a slide. It should answer: what data class entered, which provider was selected, whether consent is needed, whether the user can refuse a fallback, what sources were used, and what output metadata is retained. Apple provides a strong platform story for on-device and Private Cloud Compute models [9] (https://developer.apple.com/documentation/foundationmodels). The EU Commission's Article 50 transparency FAQ [16] (https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50) makes disclosure a timely product concern, but the team should not present the prototype as legally compliant.

Use synthetic data only. Add a visible `demo_data=true` flag. For Adobe, the provenance manifest can travel with the asset. For Accenture, it can travel with the case. For Meta, it can travel with the message event. For Google, it can travel with the agent trace.

### Pattern 5: evaluation and observability

Prepare three fixtures before the event: a happy path, an ambiguous input, and a malicious or malformed input. Define expected fields and expected policy behavior. The trace viewer should show latency placeholders, provider name, schema status, evidence identifiers, action status, and fallback state. If an API fails, the user interface should say what happened and offer replay or fixture mode.

Adobe's public API docs expose asynchronous job state and troubleshooting [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting) [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api). Google's infrastructure-friction language [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights) points in the same direction. A system that can explain its failure can be judged even when the external service is imperfect.

## 8. One Engine, Many Skins: The Architecture Team 511 Should Build Before Reveal

### The core pipeline

```text
Input adapter
  -> Normalized event
  -> Intent and risk classifier
  -> Retrieval and evidence packet
  -> Planner and typed action proposal
  -> Policy gate and consent check
  -> Human approval when needed
  -> Provider tool or model adapter
  -> Validator and repair loop
  -> Renderer, audit trace, and replay
```

The engine should own the normalized event, evidence packet, action schema, policy decision, trace, and replay. A skin should own only the nouns, sample data, UI labels, channel adapter, and provider configuration. This is the architecture that lets the team respond to a reveal without discarding its work.

### Recommended internal contracts

`NormalizedEvent` should contain `event_id`, `channel`, `actor_id`, `text`, `media_refs`, `consent_state`, and `received_at`. `EvidencePacket` should contain `source_id`, `passage`, `relevance`, and `display_label`. `ActionProposal` should contain `tool_name`, `arguments`, `side_effect_class`, `reason`, and `evidence_ids`. `PolicyDecision` should contain `allow`, `reason`, `needs_approval`, `data_movement`, and `retention`. `TraceEvent` should contain `timestamp`, `stage`, `status`, `input_ref`, `output_ref`, and `error_code`.

These contracts are deliberately boring. Boring contracts are what allow Google JSON output [7] (https://ai.google.dev/gemini-api/docs/structured-output), Meta message events [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started), Adobe asynchronous jobs [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api), and Apple processing states [9] (https://developer.apple.com/documentation/foundationmodels) to plug into the same renderer.

### Skin map and mount sequence

| Skin | User story | Changed components | Expected mount target | First visual proof |
|---|---|---|---:|---|
| Google agent console | Complete a research or operations task with evidence and approved tools | Tool descriptions, fixture corpus, agent labels | 20-30 minutes | Plan, sources, approval, trace |
| Apple private cockpit | Transform sensitive personal content with visible processing state | Privacy badge, local provider, synthetic personal fixture | 20-30 minutes if runtime works; otherwise simulation | On-device state, refusal of cloud fallback |
| Meta conversation assistant | Resolve a multimodal question through message or replay | Channel adapter, intent list, FAQ, handoff queue | 20-40 minutes with credentials; 10-15 in replay mode | Text plus image, answer, escalation |
| Accenture case router | Turn messy requests into governed enterprise work | Case schema, queues, KPI, approver | 15-25 minutes | Before/after queue and decision log |
| Adobe creative workflow | Turn a brief into reviewed, constrained assets | Brief schema, brand kit, asset card, job state | 20-35 minutes with API; 10-15 in fixture mode | Variants, violation, approval, manifest |

The mount targets are team planning estimates, not promises. The takeaway is operational: if a skin needs more than about one focused build session, it is not a skin; it is a second project. Keep the core contracts stable and put sponsor-specific work behind adapters.

### Provider adapter strategy

Create a common `generate(input, schema, policy)` interface. The Google adapter calls the selected Gemini path. The Meta adapter calls the chosen Llama or channel path. The Apple adapter reports capability and processing location. The Adobe adapter returns an asynchronous job handle and later an asset result. The offline adapter returns deterministic fixture output. The Accenture skin can use any provider because its differentiation is the workflow, policy, and KPI.

Do not hard-code a provider into every component. Google's Java SDK positioning around switching backends without rewriting application code [8] (https://github.com/googleapis/java-genai) is a useful model for the team's own abstraction, even if the team uses a different language. The engineering principle is the same: keep application state independent from provider transport.

## 9. 24-Hour Execution Plan and Decision Gates

### Hour 0 to 1: reveal parsing and risk gate

Copy the official problem statement into a shared document. Extract the user, input, desired action, sponsor-specific technology, data constraints, evaluation metric, and forbidden assumptions. Highlight words such as "on device," "WhatsApp," "Firefly," "agent," "enterprise," "audit," and "structured." Do not interpret yet. Ask whether external APIs, pre-trained models, synthetic data, and simulated integrations are allowed.

Run five smoke tests in parallel: model key, Apple environment or simulation, Meta webhook or replay, Adobe generation or fixture, and retrieval plus schema validation. Record pass, partial, or fail. The first failed dependency should trigger a skin change, not a team-wide panic.

### Hour 1 to 3: choose the lane and freeze the story

Score each candidate from 0 to 2 on sponsor fit, user pain, demo visibility, evidence or data availability, API reliability, and measurable outcome. Pick the lane with the highest total, but subtract two points for any unverified dependency. If the top lane depends on a permission that has not passed, select the next lane while keeping the adapter alive in the background.

Write one sentence: "For [user], who struggles with [pain], we build [AI workflow] that produces [measurable outcome] while preserving [trust constraint]." If the team cannot say this without using the words "platform," "ecosystem," or "AI-powered" as the main value, the problem is still too broad.

### Hour 3 to 8: build the vertical slice

Implement only one complete path from input to visible outcome. The vertical slice must include a real fixture, one model or deterministic provider, one evidence card, one policy decision, one output, and one trace. Do not add a second feature until the first path can be demoed without a developer typing commands in the background.

For the agent lane, the slice is retrieve -> propose -> approve -> act. For the creative lane, it is brief -> variant -> constraint -> approve. For the private lane, it is sensitive input -> capability state -> transform or refuse. For the Meta lane, it is event -> multimodal intent -> answer or handoff. For the enterprise lane, it is request -> case -> route -> review.

### Hour 8 to 14: add the differentiator and failure path

Add exactly one differentiator: evidence, privacy, provenance, human handoff, or measurable routing. Then stage a failure that is safe and repeatable. A malformed schema, missing field, denied consent, failed job, ambiguous image, or unavailable provider is enough. The failure must produce a useful UI state and a recovery or escalation action.

### Hour 14 to 19: polish for judging

Remove dead buttons, unsupported claims, and unnecessary settings. Add a three-step onboarding panel. Put the sponsor technology in the architecture diagram and the user outcome in the first sentence. Add a small KPI card and an evidence or audit drawer. Prepare a recorded backup demo using synthetic fixtures, but say when it is a backup.

### Hour 19 to 24: rehearse and freeze

Rehearse a two-minute version, a five-minute version, and a judge-interruption version. The interruption version must answer: What pain exists? Why this sponsor technology? What is new? What happens when the model is wrong? What data leaves the device or channel? How would this scale? Freeze the core code after the first full rehearsal. Spend the remainder on reliability, not new features.

### Kill criteria matrix

| Kill signal | Time limit | Pivot | What survives |
|---|---:|---|---|
| API key, quota, app permission, or webhook not working | 60-90 minutes | Replay or fixture adapter | Event schema, UI, trace, policy gate |
| Apple runtime prerequisite blocks testing | 60 minutes | Simulated local-first skin or provider-neutral privacy workflow | Capability probe and data-movement UI |
| Model output cannot satisfy the schema after three repair attempts | 2 hours | Reduce schema and add deterministic extraction | Evidence cards and renderer |
| Creative output has no controllable constraint | 3 hours | Asset review and provenance workflow | Brief parser, approval, manifest |
| Agent can act without a meaningful human control | 3 hours | Read-only evidence assistant or approval-first flow | Retrieval, tool registry, trace |
| No measurable user outcome | 4 hours | Choose queue time, fields completed, escalations, or approved assets | Core engine and data fixtures |
| Demo requires hidden operator actions | Before rehearsal | Replace with button, fixture, or explicit limitation | Honest product narrative |

A kill criterion is not failure. It is a pre-agreed limit on sunk cost. The strongest team is often the one that abandons a flashy but blocked integration before it consumes the final half-day.

## 10. Questions to Ask When the Official Problem Statement Appears

The team should ask for clarification using questions that reveal the scoring surface without arguing with the prompt.

1. Which sponsor API or model is mandatory, optional, or merely thematic?
2. May the team use a different model for orchestration, retrieval, or evaluation?
3. Is live internet, a webhook, a device, or a cloud credential guaranteed during judging?
4. Is a simulated integration accepted when the product workflow is demonstrated honestly?
5. Are judges rewarding model novelty, user impact, responsible AI, technical depth, visual polish, or sponsor-specific integration?
6. What data may be used, and must the team use synthetic data?
7. Must the demo work offline or on a particular operating system?
8. Is there a required deployment URL, repository, video, or time limit?
9. What is the one user outcome the sponsor wants to see improved?
10. Can the team show an approval, refusal, escalation, or fallback path as part of the solution?

The public Google AI Hackathon rules found in the research pass define a contest in which participants develop an application, product, or prototype using Google generative AI products or APIs [28] (https://googleai.devpost.com/rules). That is evidence that sponsor technology may be an explicit eligibility condition in some events, not proof that Craft N Code uses the same rule. The team should ask rather than assume.

A general hackathon scorecard source says that Opportunity Hack has converged on a four-category rubric after running social-good hackathons since 2013 [29] (https://www.ohack.dev/hackathon-judging-criteria). This is useful as a preparation heuristic, not an official Craft N Code rubric. Prepare for technical implementation, user value, originality, and presentation, but do not claim those are the event's rules until organizers confirm them.

## 11. Evidence Discipline for the Final Pitch

Use the evidence labels on the slide or in the README. A compact evidence panel can say:

- **[VERIFIED]** Google publicly describes Managed Agents, AI Studio expansion, and infrastructure-friction reduction [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights).
- **[VERIFIED]** The product uses constrained structured output or a documented typed interface [7] (https://ai.google.dev/gemini-api/docs/structured-output).
- **[INFERRED]** Those signals suggest a problem around reliable tool-using agents, so the prototype adds approval and replay.
- **[UNVERIFIED]** The team has not confirmed that this exact wording is the sponsor's challenge; it is a forecast prepared before reveal.

This language makes the team sound rigorous rather than uncertain. Sponsors know that a public product announcement is not the same as a leaked prompt. The credible claim is: "We observed these signals, made this bounded inference, and built a system that can adapt if the actual task differs."

Do not cite an unofficial MCP server as an Adobe policy or official integration. It is an example of a developer workaround-shaped artifact [27] (https://github.com/krishnapallapolu/adobe-firefly-mcp/blob/main/README.md), not evidence that Adobe endorses it. Do not describe the Apple simulator thread as proof that Foundation Models are unreliable; it is evidence of a setup prerequisite [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022). Do not describe DPDPA enforcement dates that are not present in the cited MeitY excerpt [5] (https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025).

## Synthesis: One Reliable Engine Beats Five Narrow Guesses

The five sponsor strategies differ in mechanism, scope, trade-offs, evidence base, and time horizon. Google is pushing agentic orchestration and developer infrastructure. Apple is emphasizing the device and private-compute boundary. Meta combines an open multimodal model direction with a high-distribution messaging surface. Accenture is focused on enterprise transformation, people, acquisitions, R&D, and responsible implementation. Adobe is moving creative generation toward an agentic production workflow. The common task is not a model call; it is making AI usable inside a controlled system.

| Dimension | Google | Apple | Meta | Accenture | Adobe |
|---|---|---|---|---|---|
| Primary mechanism | Agent planning, tools, structured results, managed infrastructure [6] (https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights) [7] (https://ai.google.dev/gemini-api/docs/structured-output) | On-device and Private Cloud Compute intelligence [9] (https://developer.apple.com/documentation/foundationmodels) | Open-weight multimodality plus conversation or social distribution [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence) [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started) | Enterprise process, data, skills, acquisitions, R&D, and governance [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf) [4] (https://www.accenture.com/us-en/services/ai-data/responsible-ai) | Creative agents, multi-media generation, asynchronous production jobs [13] (https://firefly.adobe.com/) [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api) |
| Best student demo | Plan, evidence, approval, tool action, trace | Data movement indicator and safe local fallback | Text plus image message and human handoff | Queue, routing, exception, KPI, decision log | Brief, variants, flagged violation, approved asset manifest |
| Main trade-off | Agent complexity and hallucinated actions | Platform availability and environment dependency | Credentials, webhook, templates, channel policies | Generic enterprise language unless KPI is concrete | Generation latency, credits, and output control |
| Best engine primitive | Typed tool gateway and trace | Capability probe and privacy policy | Event adapter and confidence handoff | Case object and governance gate | Job state and asset manifest |
| Time horizon signaled | Immediate 2026 agentic product push [19] (https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026) | Next-generation Apple Intelligence and Siri AI [22] (https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more) | Llama 4 open multimodal direction beginning in 2025 [11] (https://ai.meta.com/blog/llama-4-multimodal-intelligence) | FY2025 investment and FY2026 workforce goal [2] (http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf) | 2026 expansion of Creative Agent [14] (https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion) |

The first non-obvious tension is between autonomy and control. Google and Meta make more capable agents attractive, but Accenture's responsible-AI framing and Apple's privacy boundary make uncontrolled autonomy difficult to defend. That tension is the opportunity: a student team can differentiate by making the control plane visible rather than pretending the model is perfect.

The second tension is between platform-specific authenticity and event-time reliability. An Apple-only demo may be highly aligned but blocked by a simulator prerequisite [23] (https://developer.apple.com/forums/thread/815397?answerId=878358022). A WhatsApp-only demo may be compelling but blocked by tokens or webhooks [12] (https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started). A Firefly-only demo may look great but depend on asynchronous API state [17] (https://developer.adobe.com/firefly-services/docs/firefly-api/api). The one-engine-many-skins architecture resolves the tension by preserving the user journey while swapping transport.

The third tension is between novelty and proof. A generic chatbot is easy to build but hard to defend. A governed workflow is less flashy but gives judges a concrete failure path, a metric, and a reason the sponsor technology matters. Google's structured output [7] (https://ai.google.dev/gemini-api/docs/structured-output), Adobe's troubleshooting surface [18] (https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting), and the EU transparency clock [15] (https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) all point toward the same strategic conclusion: make the system's behavior inspectable.

The final recommendation is therefore decisive. Prebuild the evidence-first agent gateway, tool registry, policy gate, event adapter, trace viewer, replay mode, and five small skins. At reveal, choose the problem with the strongest combination of sponsor fit, visible user pain, available data, and reliable demo path. Start with Rank 1 if the prompt is agentic, Rank 2 if it is creative, Rank 3 if it explicitly requires private or on-device behavior, Rank 4 if it names WhatsApp or multimodal social interaction, and Rank 5 if it names enterprise operations, governance, or measurable process improvement. Abandon any lane whose critical dependency fails its time gate. The team is not trying to predict the exact sentence; it is trying to make five plausible sentences converge on one buildable system.

## References

1. *Meta Llama*. https://github.com/meta-llama
2. *Reinventing what's possible | FY2025 Annual Report | Accenture*. http://investor.accenture.com/~/media/Files/A/accenture-v4/investors/home/annual-report-2025.pdf
3. *Artificial Intelligence (AI) Services & Solutions | Accenture*. https://www.accenture.com/us-en/services/ai-data
4. *Responsible AI Governance Consulting & Solutions | Accenture*. https://www.accenture.com/us-en/services/ai-data/responsible-ai
5. *Digital Personal Data Protection Rules 2025*. https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025
6. *I/O 2026 developer highlights: Antigravity, Gemini API, AI Studio*. https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights
7. *Structured outputs | Gemini API | Google AI for Developers*. https://ai.google.dev/gemini-api/docs/structured-output
8. *GitHub - googleapis/java-genai: Google Gen AI Java SDK ...*. https://github.com/googleapis/java-genai
9. *Foundation Models | Apple Developer Documentation*. https://developer.apple.com/documentation/foundationmodels
10. *Updates to Apple’s On-Device and Server Foundation Language ...*. https://machinelearning.apple.com/research/apple-foundation-models-2025-updates
11. *The Llama 4 herd: The beginning of a new era of natively ... - Meta AI*. https://ai.meta.com/blog/llama-4-multimodal-intelligence
12. *WhatsApp Cloud API Get Started - Meta for Developers*. https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started
13. *Adobe Firefly: Your all-in-one AI creative studio*. https://firefly.adobe.com/
14. *Adobe Unveils Major Expansion of Creative Agent Across ...*. https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion
15. *AI Act | Shaping Europe's digital future - European Union*. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
16. *Transparency obligations under Article 50 of the AI Act*. https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
17. *Firefly API Reference - developer.adobe.com*. https://developer.adobe.com/firefly-services/docs/firefly-api/api
18. *Firefly API Troubleshooting Guide - developer.adobe.com*. https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/help/troubleshooting
19. *The latest AI news we announced in May 2026*. https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026
20. *Google Search’s I/O 2026 updates: AI agents and more*. https://blog.google/products-and-platforms/products/search/search-io-2026
21. *Google AI for Developers: Gemini Developer API | Gemma ...*. https://ai.google.dev/
22. *Apple unveils next generation of Apple Intelligence, Siri AI ...*. https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more
23. *Foundation models not detectable in Xcode simulator*. https://developer.apple.com/forums/thread/815397?answerId=878358022
24. *Accenture Acquires Halfspace to Bolster AI Capabilities in ...*. https://newsroom.accenture.com/news/2025/accenture-acquires-halfspace-to-bolster-ai-capabilities-in-the-nordic-region
25. *Accenture to Acquire Leading Creator and Social Agency ...*. https://newsroom.accenture.com/news/2026/accenture-to-acquire-leading-creator-and-social-agency-whalar-from-whalar-group
26. *New ways forward to the road of AI value | Accenture*. https://www.accenture.com/us-en/blogs/data-ai/how-leaders-unlock-ai-value
27. *adobe-firefly-mcp/README.md at main*. https://github.com/krishnapallapolu/adobe-firefly-mcp/blob/main/README.md
28. *Google AI Hackathon: Build a creative app that uses Google’s ...*. https://googleai.devpost.com/rules
29. *Hackathon Judging Criteria & Scorecard Template | Opportunity ...*. https://www.ohack.dev/hackathon-judging-criteria
