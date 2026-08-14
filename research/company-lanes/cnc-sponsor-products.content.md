
# Sponsor DNA to 24-Hour MVPs: Team 511 Playbook

## Executive Summary

- **Event Reality**: [UNVERIFIED] The supplied brief names five sponsors - Google, Apple, Meta, Accenture, and Adobe - but calls for six companies, and no authoritative public Craft N Code 2026 Rajasthan page or sponsor-authored statement was surfaced in the available research. Treat the Aug 15-16 schedule, the 21:30 drop, the 06:00 idea cutoff, and the sponsor attribution as club-insider constraints rather than public facts -> build a portable core that can be retargeted after the statement is revealed.
- **Google's Multimodal Agent Signal**: [VERIFIED] The Android Gemini Developer API is described as supporting text, image, audio, and video generation, multi-turn chat, and image editing, while Google's developer surface puts Gemini API, AI Studio, Android, Firebase, and agent platforms together [15][16] -> make the default architecture a multimodal agent with two or three real tools, not a chatbot wrapper.
- **Apple's Private-Compute Signal**: [VERIFIED] Apple's Foundation Models framework exposes on-device and Private Cloud Compute models, and Apple's WWDC26 iOS guide calls it a native Swift API for the same on-device model that powers Apple Intelligence [27][29] -> include an on-device or privacy mode and demonstrate what still works with the network disabled.
- **Meta's Open-Multimodal Signal**: [VERIFIED] Meta introduced Llama 4 Scout and Llama 4 Maverick on April 5, 2025 as open-weight, natively multimodal models [18] -> keep the model layer replaceable and show a local or open-weight path where it is technically feasible, while avoiding an unsupported claim that Meta requires local inference.
- **Accenture's Workflow Signal**: [VERIFIED] Accenture describes Forward Deployed Engineering with SAP for industry-specific AI solutions and describes Accenture Edge with Google Cloud as providing pre-built, industry-specific agents for mid-market companies [21][22] -> connect the model to a business workflow, system of record, approval step, and measurable outcome.
- **Adobe's Content-System Signal**: [VERIFIED] Adobe's Firefly materials position generative AI as a creative co-pilot, Adobe announced a major Creative Agent expansion across Firefly and Creative Cloud apps including Photoshop and Premiere, and GenStudio has a public REST API for approved experiences and assets [8][9][20] -> build a governed content pipeline with generation, brand checks, approval, and an asset handoff instead of a one-off image generator.
- **What Judges Can Actually See**: [VERIFIED] Google's Gemini Live Agent Challenge used the categories Live Agent, Creative Storyteller, and UI Navigator, while HackerRank's 2026 Orchestrate description says judging covered the agent, the tickets it handled, how the team directed coding tools, and a live defense [24][12] -> rehearse a three-minute happy path, a failure case, a trace, and a human override.
- **Enterprise Reliability Beats Model Theater**: [VERIFIED] A HackerRank Orchestrate team built a terminal support-triage agent using a corpus of 774 Markdown documents as its only knowledge base [7] -> use a small, inspectable corpus, citations, an abstention rule, and ten scripted evaluation cases rather than claiming broad world knowledge.
- **India-First Is a Differentiator, Not Yet a Verified Sponsor Requirement**: [VERIFIED but weakly sponsor-linked] An India-focused hackathon guide explicitly names Indic NLP as a technical theme, and a Masters' Union AI hackathon describes real-world problem solving [26][30] -> offer Hindi, Hinglish, or Rajasthani voice and text as an interface layer, but do not make UPI or a particular Indic language the critical path unless the released statement demands it.

## How to Use the Evidence, and What Is Not Publicly Confirmed

This report separates three evidence states. **[VERIFIED]** means the cited source in the research corpus explicitly names the product, program, date, category, or behavior. **[INFERRED]** means a practical prediction derived from a verified product or challenge signal; it is not a leaked prompt. **[UNVERIFIED]** means the supplied brief, club information, or a plausible but unconfirmed sponsor connection. The distinction matters because the public evidence recovered here is rich on product direction but thin on the actual Craft N Code problem statements.

The event-specific facts in the brief are therefore operational inputs, not independently confirmed facts. The public search for the phrase "Craft N Code 2026" did not return an official event page, rules page, or sponsor list; it returned unrelated craft and weaving social pages rather than a hackathon listing [31][32]. That is not proof that the event is not real. It means Team 511 should not quote the date, sponsor authorship, or judging rubric as externally verified in a pitch or README.

The phrase "six sponsor companies" is also unresolved. Five names are enumerated repeatedly: Google, Apple, Meta, Accenture, and Adobe. No sixth company was identified in the material available for this report. The sixth row in the mapping section is deliberately called **Unknown sixth sponsor** and is a portable strategy, not a guessed company.

| Evidence label | Meaning for Team 511 | How to act during the overnight build |
|---|---|---|
| [VERIFIED] | The source explicitly states the item. | Use the exact product or program name in the pitch and cite it in the README. |
| [INFERRED] | A reasoned prediction from verified product or challenge evidence. | Use it to choose architecture and demo order, not as a claim about the unreleased statement. |
| [UNVERIFIED] | Insider information, an absence that could change, or a sponsor-specific claim not supported by a retrieved source. | Keep the implementation modular and ask the organizers for clarification if the statement conflicts. |

The practical conclusion is not to build five separate applications. Build one narrow workflow shell with swappable model adapters, a retriever, tool registry, approval gate, evidence panel, and interface adapters. Then change the nouns, tools, and demo data in the first hour after the statement arrives.

## Sponsor Comparison: Five Confirmed Names, One Unresolved Slot

| Sponsor named in the brief | Verified current product DNA | Strongest retrieved challenge or program signal | [INFERRED] judgeable 24-hour wedge |
|---|---|---|---|
| Google | Gemini Developer API, Firebase AI Logic, Google AI Studio, Android AI, Gemini API, and Google's agent-oriented developer surface [15][16] | Gemini Live Agent Challenge: Live Agent, Creative Storyteller, UI Navigator [24] | A multimodal agent that sees or hears an input, calls tools, cites evidence, and completes one action. |
| Apple | Foundation Models, Apple Intelligence integration, native Swift access to on-device models, and the Swift Student Challenge [27][28][29] | Student-facing Swift challenge plus WWDC developer education [28][29] | A polished Swift experience with a privacy or offline mode, careful UX, and a clear human benefit. |
| Meta | Llama 4 Scout and Maverick, open-weight and natively multimodal, plus Meta for Developers [18][19] | Llama 4 multimodal model launch; no sponsor-specific student track was verified. | A multimodal community, creator, safety, or commerce workflow with a model abstraction layer. |
| Accenture | Forward Deployed Engineering with SAP and Accenture Edge with pre-built industry-specific agents [21][22] | Industry and mid-market agent deployment; 2026 internship listing mentions cybersecurity, digital engineering, and manufacturing [23] | An industry workflow agent connected to records, rules, approvals, and a measurable service-level outcome. |
| Adobe | Firefly, Creative Agent expansion, Firefly API, and GenStudio Experience API for approved experiences and assets [8][9][20] | Creative production plus enterprise content operations; Adobe reported 99% of Fortune 100 companies had used AI in an Adobe app in September 2025 [6] | Generate, inspect, approve, and publish a brand-safe content package with an audit trail. |
| Sixth sponsor | No identity was verified. | The six-company requirement is [UNVERIFIED]. | Keep the same workflow shell and swap tools only after the statement identifies the company. |

The table shows a useful common denominator. Google and Meta pull toward model and interaction capability; Apple pulls toward native, private, polished device experiences; Accenture pulls toward enterprise workflow execution; Adobe pulls toward governed creative and marketing operations. A generic "AI assistant" misses all five because it has no sponsor-specific surface, no measurable workflow, and no reason to use the sponsor's technology.

## Google: Gemini, Live Agents, and Developer-Visible Tool Use

### Current products and exact names

[VERIFIED] The Android Gemini Developer API page names the **Gemini Developer API** and says it can support text, image, audio, and video generation, multi-turn chat, and image editing through Android applications using **Firebase AI Logic** [15]. Google's main developer surface presents **Google AI Studio**, **Gemini API**, Android, Firebase, Cloud, and an agent-oriented platform as routes from prototype to production [16]. The page also presents the Gemini API as a way to build apps and agents with Gemini models, which is a stronger signal than merely adding a text completion box [16].

[VERIFIED] The retrieved challenge source names the **Gemini Live API**, the **Agent Development Kit (ADK)**, and Google Cloud infrastructure as the stack for multimodal agents that see, hear, speak, and create in real time [24]. These names are concrete choices for a Google-flavored build: Gemini API for reasoning, ADK for orchestration, Gemini Live API for streaming interaction, and Firebase AI Logic or Android for the user-facing surface.

### 2025-2026 challenge shape and student signal

[VERIFIED] Google's Gemini Live Agent Challenge was organized around three categories: **The Live Agent**, **The Creative Storyteller**, and **The UI Navigator** [24]. The mission was to integrate multimodal capabilities so that an agent could see, hear, speak, and create in real time [24]. These are reusable problem-statement shapes, not proof that Craft N Code will copy them.

[VERIFIED but date-limited] The official Google for Developers ecosystem includes a page for **GDSC Solution Challenge Winners** [4]. The retrieved page is specifically a winners page for the 2023 Solution Challenge, so it supports the existence and student orientation of the program but does not prove a 2025-2026 track, current prize, grant, or eligibility rule. Do not promise a Google grant or current incentive in the pitch without a current official rule page.

[VERIFIED] Google's developer homepage also foregrounds developer resources, community events, Gemini, Android, Cloud, Chrome, and AI Studio [16]. The resulting [INFERRED] recruiting and DevRel signal is breadth plus integration: teams that show a complete path from user input to deployed service, rather than a notebook, are more legible to a Google-oriented judge.

### Three Google-shaped problem statements

1. **Live Agent - see, hear, speak, and act. [VERIFIED shape, not Craft N Code prompt]** A user presents a photo, voice message, or live situation; the agent interprets it, asks a clarifying question, and calls a tool. A 24-hour MVP is one camera or audio input, one Gemini Live or Gemini API interaction, two deterministic tools, and a visible action receipt. The judge demo should begin with an intentionally ambiguous input, show the agent asking for clarification, then show the tool result and a recovery path. The challenge source explicitly frames the capability as real-time multimodal interaction [24].

2. **UI Navigator - operate a complex interface safely. [VERIFIED category, [INFERRED] implementation]** The agent identifies a target control or form, explains what it will do, and either performs one safe action or hands off to a person. Scope it to one mock web or Android screen with five controls and a confirmation step. A good demo shows the agent refusing a destructive action without confirmation, which makes tool-use boundaries visible instead of pretending autonomy is always good. The category name is verified; the exact workflow is an inference from that category [24].

3. **Creative Storyteller - transform grounded inputs into a media artifact. [VERIFIED category, [INFERRED] implementation]** The user supplies a photo, short voice note, or document; the app creates a short story, storyboard, or narrated card. Keep it to one input, three scenes or cards, one voice or text output, and a provenance panel. The category is explicitly named by the challenge [24], while the proposed artifact is a 24-hour implementation choice.

### What Team 511 should build for Google

Use a small event-driven loop: input capture -> Gemini multimodal interpretation -> structured intent -> tool call -> result grounding -> human confirmation -> receipt. Put every tool behind a typed schema. Keep the UI able to display the original input, extracted facts, tool arguments, returned evidence, and final action. This simultaneously exposes the Google product surface and gives the judge a way to inspect failure rather than trusting a hidden prompt.

The high-risk failure is a streaming demo with no deterministic fallback. If the network or quota fails, the live demo collapses. Cache a small test fixture, keep a text-only fallback, and show a visible "offline or limited mode" state. That is not anti-Google; it is good engineering for an overnight build.

## Apple: Foundation Models, Swift, Privacy, and Interaction Quality

### Current products and exact names

[VERIFIED] Apple's **Foundation Models** framework provides access to large language models including on-device and **Private Cloud Compute** models designed for Apple Intelligence [27]. Apple's WWDC26 iOS guide describes Foundation Models as a native **Swift API** giving developers access to the same on-device model that powers Apple Intelligence [29]. These are the strongest current Apple-specific AI signals in the retrieved evidence.

[VERIFIED] Apple's **Swift Student Challenge** is an explicit student developer program [28]. The retrieved evidence confirms the program name but not a current 2026 submission rubric, prize, number of winners, or grant. The safe statement is that it is a student challenge, not that a particular incentive is guaranteed.

The Apple signal differs from the Google signal. Google evidence emphasizes a broad, cloud-connected developer surface and multimodal agents. Apple evidence emphasizes a native Swift API and an on-device model. [INFERRED] A student build will look more Apple-native if it treats privacy, responsiveness, accessibility, and interaction polish as first-class functionality rather than adding a Swift front end to a cloud chatbot.

### Student challenge and problem shapes

The public evidence does not provide two or three verbatim Apple sponsor problem statements from 2025-2026. It provides a named student program and current framework documentation. It would be fabrication to invent an Apple challenge prompt. The following are therefore explicitly [INFERRED] shapes derived from the verified product signal:

1. **Private on-device helper. [INFERRED]** A student creates a focused assistant that summarizes a note, class material, or personal task locally, with cloud escalation only after user consent. The 24-hour MVP should use a narrow input schema, a clear privacy indicator, a small set of supported intents, and an offline fixture. The impressive demo is to disable connectivity, complete the core task, then show a user-controlled switch for a more capable cloud path. Foundation Models and the Apple Intelligence relationship support the direction [27][29]; they do not prove that Apple will set this exact problem.

2. **Swift multimodal utility with human-centered interaction. [INFERRED]** A camera, microphone, or document input becomes a structured task such as reading a form, explaining a diagram, or preparing a checklist. Use one screen for capture, one for review, and one for action. The demo should include VoiceOver-friendly labels, large type, a correction flow, and a visible explanation of what leaves the device. The user value and polish are the differentiator; a large model benchmark is not.

3. **Student-built app with a complete story. [INFERRED from Swift Student Challenge]** Build one small app or playground whose outcome is understandable in thirty seconds. Avoid a platform claim. Show the app, the design choice, one failure case, and the human benefit. The verified program name supports the student-app framing [28], but no current judging rubric was retrieved.

### What Team 511 should build for Apple

If the statement has an Apple flavor, make Swift the visible product, not just the submission wrapper. Design a `ModelProvider` interface with an on-device implementation and a remote implementation. Use a mock provider if the exact Foundation Models API is unavailable in the team's environment, but label the mock honestly and keep the privacy behavior demonstrable. A judge should be able to ask, "What happens when the device is offline?" and receive a real answer.

The failure case is a nominally private app that sends raw documents to a server. Add a data classification step: public, personal, sensitive. Require consent before remote processing. Even if the underlying model call is mocked, the policy and UI are testable and visible.

## Meta: Llama 4, Open Weights, and Multimodal Model Choice

### Current products and exact names

[VERIFIED] Meta's AI blog announced **Llama 4 Scout** and **Llama 4 Maverick** on April 5, 2025 and described them as the first open-weight, natively multimodal models in that line [18]. Meta's developer center invites builders to get started with Llama and provides a Meta developer surface [19]. The AI at Meta blog is the official news surface for current AI updates [17].

The precise signal is openness plus native multimodality. The retrieved sources do not establish that Craft N Code will require Llama, that a Meta judge will reward local inference, or that any particular Meta student grant is active. There is also no retrieved Meta-specific 2025-2026 student hackathon statement in this research. Those gaps remain [UNVERIFIED].

### Three Meta-shaped problem statements

1. **Open multimodal assistant for a real community or creator workflow. [INFERRED]** A user supplies an image, caption, voice note, or short video; the system creates a structured answer or content package. The MVP should expose a model selector or provider adapter, keep the task narrow, and show the same input passing through a multimodal model and a deterministic policy layer. The open-weight and multimodal direction is grounded in Llama 4 [18].

2. **Visual commerce or content operations. [INFERRED]** A seller or creator uploads an image and receives a description, catalog fields, accessibility text, and a suggested caption. Do not build a social network. Build one asset-to-record pipeline with human review, prohibited-content checks, and an exportable JSON result. The multimodal model is useful because the input is visual; the business value comes from structured metadata and reduced manual work.

3. **Safety or context assistant. [INFERRED]** A moderation or community operator receives a mixed-media report and gets a triage label, supporting evidence, uncertainty, and escalation route. The output must be a recommendation, not an irreversible ban. Include a red-team test set and a human override. This shape is deliberately cautious because the retrieved sources establish model capability, not a Meta safety challenge.

### What Team 511 should build for Meta

Make model substitution a visible engineering feature. Define one interface for `understand_media`, `classify_intent`, and `draft_response`, then keep policy, retrieval, and audit logs outside the model. If Llama is available, use it for the multimodal path; otherwise use the authorized model available to the team and say so. A strong demo shows that changing the model does not change the safety policy or the evidence trail.

The failure case is to equate open-weight with automatically cheap, private, or easy to run on a student laptop. Those properties depend on hardware, serving, licensing, and deployment choices that the retrieved Llama source does not settle. Pitch the adapter and evaluation harness as the solid contribution, not an unsupported performance claim.

## Accenture: Industry Agents, SAP Workflows, and Operational Outcomes

### Current products and exact names

[VERIFIED] Accenture's offerings and products source describes a **Forward Deployed Engineering Program with SAP** that will deliver industry-specific AI solutions and embed agentic capabilities [21]. A separate Accenture newsroom item says **Accenture Edge and Google Cloud** bring scalable agentic AI solutions to mid-market companies and refers to pre-built, industry-specific agents [22]. These are the most concrete retrieved product and delivery signals for Accenture.

[VERIFIED] A 2026 Accenture internship listing is titled **Accenture Internship Opportunities (Jun/Jul/Aug) 2026** and references cybersecurity, digital engineering, and manufacturing [23]. It does not prove a complete hiring rubric, but it is a real student or early-career signal tied to engineering and industry delivery. No current Accenture student grant, named 2025-2026 hackathon track, or sponsor-authored student problem statement was retrieved.

The Accenture distinction is mechanism, not model novelty. The product evidence says industry-specific agents, SAP, Google Cloud, and mid-market deployment. [INFERRED] A credible Team 511 submission should therefore show a workflow that crosses roles or systems, produces a measurable operational result, and leaves a person in control.

### Three Accenture-shaped problem statements

1. **Industry operations agent. [INFERRED]** A worker reports an issue through text, voice, image, or form; the agent classifies it, looks up a rule or asset record, proposes the next step, and creates a work item. Choose one domain such as campus facilities, manufacturing maintenance, or service desk. The MVP needs one intake form, one small knowledge base, one mock record system, one escalation rule, and one completion receipt. The shape follows the verified industry-agent signal [21][22].

2. **Mid-market workflow automation. [INFERRED]** A small organization has a repetitive process spread across email, spreadsheets, and a ticket queue. The agent extracts fields, checks them against a policy, drafts an update, and waits for approval before writing the record. The demo should compare the old manual steps with the new trace and show a rejected request. The pre-built-agent and mid-market language supports this prediction [22].

3. **Cybersecurity, digital engineering, or manufacturing copilot. [INFERRED from the internship signal]** A student team picks one of the domains visible in the internship listing and builds a narrow investigator or planner. For cybersecurity, use safe synthetic alerts; for manufacturing, use a simulated machine log; for digital engineering, use a requirements-to-test trace. The domain should be synthetic and non-destructive. The internship page supports the domain names [23], not a specific competition prompt.

### What Team 511 should build for Accenture

Use a process diagram in the pitch. Label the intake, retrieval, decision, approval, system write, and audit event. Give the judge a role such as operator, supervisor, or auditor and let the UI change the available action. This turns agentic AI into an implementable operating model.

The failure case is a broad "enterprise platform" with no system of record. A mock API is acceptable in 24 hours; an unbounded claim that the agent integrates with every enterprise system is not. Use a small JSON database or local service, expose the API call in the trace, and report exactly what is simulated.

## Adobe: Firefly, Creative Agent, and Governed Content Operations

### Current products and exact names

[VERIFIED] Adobe's Creative Cloud help describes **Adobe Firefly** as a family of generative AI models that acts as a creative co-pilot in Adobe products [8]. Adobe's June 18, 2026 news item announces a major expansion of **Creative Agent** across Firefly and Creative Cloud apps including Photoshop and Premiere [9]. These names point to generation embedded in an existing creative workflow, not an isolated image toy.

[VERIFIED] The **GenStudio Experience API** is described as a storage-agnostic public REST API for **Adobe GenStudio for Performance Marketing**. It can read approved Experiences, list and filter Experience summaries, and download assets through pre-signed URLs [20]. Adobe's September 2025 announcement also says that 99% of Fortune 100 companies had used AI in an Adobe app [6]. The percentage is an Adobe-reported adoption claim; it is not an independent market estimate.

[VERIFIED, secondary partnership signal] A report on Adobe's Google Cloud partnership says Adobe would be able to integrate Google's Gemini, Veo, and Imagen models into Adobe applications as they become available [2]. Use this only as partnership context, not as proof that every model is available to Team 511 or that Adobe will require Google APIs.

### Three Adobe-shaped problem statements

1. **Brand-approved campaign assembly. [INFERRED from GenStudio API]** A marketer provides a brief and selects an approved product or campaign. The system retrieves approved experiences, generates or proposes variants, applies a checklist, and exports a package with asset links. The MVP should use a tiny approved asset catalog, three variants, one brand rule set, human approval, and a JSON or HTML handoff. The verified API capabilities make approved-asset retrieval and download a stronger Adobe fit than an ungoverned generator [20].

2. **Creative Agent for a production bottleneck. [INFERRED from Creative Agent expansion]** A user turns one source brief into a storyboard, copy variants, an image prompt, and a short edit plan. Do not attempt full Photoshop or Premiere automation. Produce one visible artifact, one revision loop, and one provenance record. The Creative Agent product direction supports the problem shape [9].

3. **Generative media with review and provenance. [INFERRED]** A user creates an image, audio clip, or short video concept; the app records prompt, input asset, model or provider, revision history, approval state, and export URL. The retrieved sources support Firefly and Creative Agent, but they do not establish that Adobe will require a particular provenance standard. If Team 511 uses C2PA or another standard, present it as an engineering choice and verify the exact implementation before claiming compliance.

### What Team 511 should build for Adobe

Make the artifact inspectable. The judge should see the original brief, approved references, generated candidate, rule violations, human edit, final asset, and download link. A side-by-side before and after is more persuasive than a model name. If the team cannot call Firefly in the contest environment, use a clearly labeled mock asset generation step but implement the approval and asset metadata flow for real.

The failure case is an impressive image with no business workflow. Adobe's strongest retrieved signal is the combination of creative generation and approved enterprise experiences [8][9][20]. Connect generation to selection, review, and distribution.

## Programs, Incentives, and Recruitment Signals: What Is Verified and What Is Missing

| Sponsor | Verified student or developer program evidence | Verified incentive or grant evidence in this research | Safe skill signal | Do not claim without a fresh official source |
|---|---|---|---|---|
| Google | Google for Developers and a GDSC Solution Challenge winners page [4][16] | No current 2025-2026 grant, credit, or prize was retrieved. | Gemini, multimodal input, ADK, Android, Firebase, Cloud, deployed agents [15][16][24] | A current GDSC prize, API credit, or hiring preference. |
| Apple | Swift Student Challenge [28] | No current prize, grant, or device incentive was retrieved. | Swift, native app quality, Foundation Models, on-device behavior, privacy [27][29] | A specific 2026 rubric, award, or Apple recruitment promise. |
| Meta | Meta for Developers and the Llama developer entry point [19] | No current student grant or Meta-specific challenge was retrieved. | Open-weight multimodality, model abstraction, mixed-media UX [18][19] | A Meta student prize, Llama credit, or exact hiring rubric. |
| Accenture | A 2026 internship listing and industry engineering categories [23] | No current hackathon grant or student incentive was retrieved. | Industry process design, cybersecurity, digital engineering, manufacturing, agent deployment [21][22][23] | A named student hackathon track or guaranteed interview. |
| Adobe | Adobe developer docs for Firefly and GenStudio [8][20] | No current student grant or Adobe hackathon incentive was retrieved. | Creative tooling, REST integration, approved assets, production workflow [9][20] | A current Adobe student award, Firefly quota, or sponsor rubric. |

The missing incentive data is itself usable. Team 511 should not waste overnight time optimizing for an assumed prize or undocumented API credit. Use free or already authorized tooling, keep a fallback, and make the architecture legible to a judge who may care about a different sponsor than the insider predicts.

## The Hottest Technology Stack for a 24-Hour Build

### 1. AI agents and agentic workflows

**What it is.** An agentic workflow combines model reasoning with structured state, tool calls, retrieval, policy checks, and a human approval path. It is not simply a long prompt. The verified Google challenge uses the Agent Development Kit and Gemini Live API for multimodal agents [24]. Accenture's current newsroom language centers on pre-built, industry-specific agents [22]. A separate 2025 AI Agents Hackathon lists Semantic Kernel, AutoGen, and Azure AI among its framework ecosystem [25]. Those framework references show the broader hackathon direction; they do not mean Team 511 must use Microsoft's stack.

**Why a sponsor could reward it.** Agent workflows map directly to Google's Live Agent and UI Navigator categories, Accenture's industry delivery model, Adobe's production operations, and Meta's model-layer flexibility. They also produce judgeable behavior: the judge can supply an input, observe a tool call, approve or reject it, and inspect the result.

**24-hour MVP.** Use four services only: `interpret_input`, `retrieve_context`, `execute_one_safe_tool`, and `request_approval`. Store state as JSON. Put a hard maximum of two tool calls per task. Add a deterministic fallback for the demo. The minimum evaluation set is ten cases: three happy paths, three ambiguous inputs, two permission failures, and two adversarial or out-of-scope cases.

**Concrete winner pattern.** The Gemini Live Agent Challenge explicitly produced winners and highlights in Live Agent, Creative Storyteller, and UI Navigator categories [24]. HackerRank's Orchestrate recap says participants built a terminal support-triage agent with a corpus of 774 Markdown documents [7]. The lesson is not "build a general autonomous agent." It is "make a narrow agent complete a visible job and explain what happened."

**Demo that wins.** Start with a real-looking request. Show the agent extracting structured intent, retrieve two relevant snippets, call a tool, stop for approval, and produce a receipt. Then deliberately make the tool fail and show the retry or escalation. End with an evaluation panel, not another generated paragraph.

### 2. Multimodal AI: vision, audio, and documents

**What it is.** One workflow accepts more than text: an image, audio clip, video, scanned document, or text can be interpreted together. The Android Gemini Developer API source explicitly names text, image, audio, and video generation, multi-turn chat, and image editing [15]. Llama 4 Scout and Maverick are described as natively multimodal and open-weight [18].

**Why it matters.** Multimodality creates a concrete input advantage. A student team can show a camera or voice interaction that would be awkward with a text-only bot. It also creates a natural test for uncertainty: the app can show the original frame or transcript next to extracted fields.

**24-hour MVP.** Pick one input pair: image plus voice, or PDF plus voice. Extract three fields, ask one clarifying question, call one business tool, and render an evidence card. Do not support every file type. Use a 10-item fixture set and show one low-confidence case.

**Concrete winner pattern.** The Google challenge mission explicitly asks agents to see, hear, speak, and create in real time [24]. That is a direct verified example of a 2025-2026 challenge shape. The winning pattern to copy is the interaction loop, not the likely scale of the original infrastructure.

**Failure case.** Do not hide OCR errors or hallucinated fields. Display confidence as a prompt for human review, not as a scientific probability unless calibrated. If the model cannot parse the document, return "needs review" and preserve the source page.

### 3. Generative media with approval and provenance

**What it is.** A generative media workflow creates or transforms image, video, audio, or copy, then routes the artifact through review, metadata, and publishing. Adobe Firefly is a family of generative AI models positioned as a creative co-pilot [8]. Adobe's Creative Agent expansion spans Firefly and Creative Cloud apps including Photoshop and Premiere [9]. Adobe GenStudio's API works with approved experiences and assets [20].

**Why it matters.** Generation alone is easy to imitate. The sponsor-specific wedge is the production system around it: approved input, brand rule, revision, reviewer, asset record, and export. Provenance is therefore a strong [INFERRED] design choice, but the retrieved sources do not prove that a particular C2PA requirement is part of the contest.

**24-hour MVP.** Given a campaign brief, create three text or image variants using an authorized provider or fixture. Attach source asset IDs, prompt, model/provider name, timestamp, approval state, and reviewer comment. Run three rules such as forbidden claims, missing logo, and unsupported color. Export a small HTML gallery or JSON package.

**Concrete winner pattern.** Creative Storyteller is a named category in the Gemini Live Agent Challenge [24]. It validates the shape of a creative multimodal artifact. The Team 511 improvement is to add review and auditability, making the artifact useful to Adobe or enterprise judges rather than only visually attractive.

**Failure case.** Never claim that a generated asset is licensed, authentic, or Adobe-produced unless the source and API actually establish it. Label fixtures and mock generation. A transparent mock with a real approval pipeline scores better than a misleading claim.

### 4. On-device, edge, and mobile AI

**What it is.** The model or a meaningful part of inference runs on the device or at the edge, reducing network dependence and exposing privacy and latency trade-offs. Apple's Foundation Models framework explicitly includes on-device and Private Cloud Compute models [27], and the WWDC26 guide describes native Swift access to the on-device Apple Intelligence model [29]. Android's Gemini Developer API page frames multimodal capabilities inside Android applications through Firebase AI Logic [15].

**Why a sponsor could reward it.** Apple has a direct product signal. Google has a direct Android and Firebase signal. Even for Meta, a model adapter makes deployment choices visible; Llama's open-weight description supports experimentation but does not establish edge performance [18].

**24-hour MVP.** Implement a privacy toggle with three states: local fixture, remote model, and unavailable. Run a small classifier, summarizer, or field extractor locally or with a deterministic mock, then fall back to the remote path only with consent. Display latency, connectivity status, and data classification. A real offline demonstration is more valuable than an unverified speed claim.

**Failure case.** Do not present a cloud request as on-device. Name the exact path used. If hardware is unavailable, show the architecture and the offline fixture honestly.

### 5. Enterprise AI: RAG, evaluation, human-in-the-loop, and audit trails

**What it is.** Retrieval-augmented generation grounds a response in a bounded corpus. Evaluation measures behavior on a fixed test set. Human-in-the-loop puts a person at a risk-sensitive decision point. An audit trail records input, retrieved evidence, tool arguments, approval, output, and error.

**Why a sponsor could reward it.** Google's developer surface presents an agent-oriented enterprise platform alongside Gemini API and Cloud [16]. Accenture's product evidence is about industry agents and deployment [21][22]. Adobe's GenStudio API deals with approved experiences and assets [20]. HackerRank's Orchestrate example demonstrates the small-corpus pattern: 774 Markdown documents served as the agent's knowledge base [7].

**24-hour MVP.** Index 20 to 50 short documents or records. Every answer must show two evidence snippets or abstain. Add ten expected-answer tests, two prompt-injection documents, one permission test, and one human approval gate before a write action. Store a JSON trace and include an export button.

**Concrete evaluation signal.** HackerRank's 2026 Orchestrate description says the contest evaluated the agent, the tickets handled, the team's direction of coding tools, and a live defense [12]. Its AI judge was to inspect the submission and ask about the approach and AI use [13]. This supports a build-and-defend pattern. Research on LLM judge bias also warns that judge behavior can be biased by prompt and response characteristics [10]. The practical response is to make the evidence and test cases explicit, not to optimize for vague verbosity.

**Failure case.** RAG without permissions can leak content. Add user roles to retrieval, show denied documents as denied, and never let the model invent a citation. A refusal with a reason is a feature.

### 6. India-specific: Indic language, vernacular interfaces, and UPI-adjacent finance

**What it is.** An India-first interface accepts a local language or code-switching voice input, maps it to a structured task, and returns a clear response in the user's preferred language. A financial workflow may add transaction status, budgeting, or payment intent, but real-money movement is a separate security and compliance problem.

**Evidence level.** An India-focused guide names Indic NLP as a technical theme in student-led machine-learning hackathons [26]. A Masters' Union AI hackathon describes real-world applications, data analysis, and AI-powered applications [30]. AIC-MUJ describes support for innovative technology startups through guidance, technology support, infrastructure, investor access, networking, and scaling resources [5]. None of these retrieved sources proves that any of the five named sponsors will set an Indic or UPI problem, and no sponsor-specific UPI requirement was verified.

**24-hour MVP.** Start with one language pair and one task. For example, a Hindi or Hinglish voice note becomes a structured campus maintenance ticket, with the original transcript, normalized fields, confirmation in the user's language, and an English audit record. Rajasthani support can be an [INFERRED] stretch goal only if the team has a reliable dataset or human review. For UPI, use a mock payment intent or status lookup with synthetic data unless the organizers provide an authorized sandbox.

**Why it can win.** It makes the demo locally legible and tests the full agent loop: noisy input, clarification, structured action, confirmation, and trace. It also avoids a shallow "translate the UI" claim. The value is a completed workflow for a user who would otherwise face friction.

**Failure case.** Do not claim language accuracy from a handful of examples. Show the original audio or text, the normalized interpretation, an edit control, and a low-confidence escalation. Do not collect real financial credentials in a hackathon demo.

## What a Sponsor-Ready Submission Should Prove

| Judge question | Evidence Team 511 should put on screen | Failure to avoid |
|---|---|---|
| Why this sponsor? | One exact product/API name and one direct workflow connection. | A logo collage with no integration. |
| Does it work? | A scripted input, tool call, result, and receipt. | A prerecorded happy path only. |
| Is it safe? | Permission check, approval gate, refusal, and error recovery. | Autonomous writes with no confirmation. |
| Is it grounded? | Retrieved source snippets or source asset IDs beside the answer. | Unverifiable citations or invented facts. |
| Is it useful? | A baseline count, time saved, error avoided, or task completed. | "AI makes it faster" with no measurable task. |
| Is it local and inclusive? | One real language or offline mode, with confidence and correction. | Claiming support for every Indian language. |
| Can it scale? | Provider adapter, typed tools, bounded corpus, and a trace. | A monolithic prompt that cannot be tested. |
| Can the team defend it? | Architecture diagram, test cases, known limits, and division of work. | Blaming the model when the design fails. |

The table converts sponsor strategy into observable evidence. A judge does not need the team to reproduce a sponsor's production platform overnight; the judge needs to see that the team understands where a model ends and a product begins.

## Problem-to-Solution Mapping: The Evidence-Mining Method

The brief asks for money flows, complaints, workaround intensity, and second signals. The available sources provide uneven versions of those signals. Product launches and APIs are the money-flow or commercialization signal. Challenge categories are the problem-shape signal. HackerRank's bounded support corpus is workaround intensity: a team used an agent to resolve tickets across HackerRank, Anthropic, and Visa [7]. Internship categories are a second signal for Accenture [23]. Public complaints specific to these Craft N Code sponsors were not retrieved, so the rankings below are directional predictions, not market research claims.

The phrase "winning solution pattern" below means a pattern visible in the retrieved challenge and hackathon evidence, adapted to the sponsor. It does not mean the identical solution won a sponsor-specific Craft N Code round.

### Google: Three ranked shapes

| Rank | [INFERRED] problem shape | Evidence rank | Winning pattern to adapt | 24-hour MVP | Judge-impressing demo |
|---|---|---|---|---|---|
| 1 | Live multimodal agent for a real-time situation | Directly matches Live Agent and the see/hear/speak/create mission [24] | Streaming input plus typed tools, clarification, and receipt | Camera or audio, two tools, one approval gate, fallback | Ambiguous input -> clarifying question -> tool action -> evidence receipt. |
| 2 | UI Navigator for one safe interface | Directly named challenge category [24] | Ground UI state, propose action, confirm before write | One mock screen, five controls, one destructive-action guard | Agent refuses unsafe click, then completes approved action. |
| 3 | Creative Storyteller grounded in user media | Directly named challenge category [24] | Multimodal input -> structured storyboard -> artifact | Three cards, one narration or text output, provenance card | Source photo or voice -> three-scene artifact -> edit one scene. |

Google ranks first for Team 511 if the statement contains camera, voice, live interaction, or agent language. The direct evidence is stronger than a generic assumption because the challenge categories and named APIs are explicit [15][24].

Build a provider-independent tool layer anyway. The risky assumption is that the contest will provide a stable Gemini Live quota or a compatible Android environment. A cached fixture and text fallback preserve the demo without weakening the Google fit.

### Apple: Three ranked shapes

| Rank | [INFERRED] problem shape | Evidence rank | Winning pattern to adapt | 24-hour MVP | Judge-impressing demo |
|---|---|---|---|---|---|
| 1 | Private on-device assistant | Directly connected to Foundation Models on-device and Private Cloud Compute [27][29] | Local-first task with explicit cloud consent | Narrow intent set, offline fixture, privacy toggle | Turn off network, complete task, then opt in to remote enhancement. |
| 2 | Swift multimodal accessibility utility | Product fit from native Swift and Apple Intelligence; exact prompt unverified [29] | Capture -> review -> corrected action | One document or camera input, three extracted fields, VoiceOver labels | Show a noisy input, user correction, and accessible final action. |
| 3 | Focused student app with a complete human story | Swift Student Challenge provides the verified student program signal [28] | Small polished app over broad platform claims | One user journey, one local model or mock, one outcome | Thirty-second story, graceful failure, and design rationale. |

Apple ranks first if privacy, offline behavior, accessibility, or a polished mobile experience appears in the statement. It ranks lower for a team that cannot build a native surface or that merely embeds a web chatbot. The evidence supports the native and on-device direction, but not a specific Apple prompt or current prize [27][28][29].

### Meta: Three ranked shapes

| Rank | [INFERRED] problem shape | Evidence rank | Winning pattern to adapt | 24-hour MVP | Judge-impressing demo |
|---|---|---|---|---|---|
| 1 | Open multimodal creator or community assistant | Directly connected to natively multimodal Llama 4 [18] | Model adapter plus multimodal workflow | Image plus caption or voice, one structured output, policy layer | Switch provider or model adapter while preserving the same safety trace. |
| 2 | Visual catalog and commerce assistant | Multimodal capability signal; no exact Meta challenge verified | Asset -> metadata -> human review | Product image, five catalog fields, caption, export | Show corrected field and generated listing package. |
| 3 | Mixed-media safety triage with escalation | Responsible inference from multimodality; no exact challenge verified | Recommendation, evidence, human decision | Synthetic reports, labels, uncertainty, escalation queue | Show a false positive caught by human review. |

Meta ranks first if the statement asks for open models, mixed media, creator tools, community context, or content scale. It ranks lower if the team cannot explain serving and licensing constraints. The correct pitch is not "Llama is free and private"; the retrieved evidence establishes open-weight multimodality, not those deployment guarantees [18].

### Accenture: Three ranked shapes

| Rank | [INFERRED] problem shape | Evidence rank | Winning pattern to adapt | 24-hour MVP | Judge-impressing demo |
|---|---|---|---|---|---|
| 1 | Industry operations agent | Direct fit with industry-specific agents and SAP engineering [21][22] | Intake -> retrieve -> decide -> approve -> write record | Synthetic records, one policy, one work item, trace | Operator reports issue; agent creates a controlled work order and escalates ambiguity. |
| 2 | Mid-market process automation | Direct fit with Accenture Edge mid-market language [22] | Replace spreadsheet/email handoffs with a governed queue | CSV or JSON records, approval role, SLA timer | Before/after process map and one rejected request. |
| 3 | Cybersecurity, digital engineering, or manufacturing copilot | Second signal from 2026 internship listing [23] | Domain-specific investigator or planner with synthetic data | Ten alerts, logs, requirements, or machine events | Explain one recommendation, evidence, and supervisor override. |

Accenture ranks first when the problem has an industry noun, an enterprise system, a process owner, or a measurable service outcome. It ranks lower for a standalone creative toy. The strongest demo shows a record changing only after approval and includes a role-based trace.

### Adobe: Three ranked shapes

| Rank | [INFERRED] problem shape | Evidence rank | Winning pattern to adapt | 24-hour MVP | Judge-impressing demo |
|---|---|---|---|---|---|
| 1 | Brand-approved campaign assembly | GenStudio API explicitly deals with approved experiences, filtering, and assets [20] | Retrieve approved content, generate variants, review, export | Ten approved assets, three variants, three rules, one export | Brief -> selected assets -> flagged variant -> human approval -> package. |
| 2 | Creative Agent production bottleneck | Creative Agent expansion across Firefly and Creative Cloud [9] | One brief becomes a small editable media plan | Three copy or storyboard variants, one revision loop | Judge changes one instruction and sees the artifact update with history. |
| 3 | Generative media with provenance | Firefly and creative co-pilot evidence; provenance is an engineering inference [8][9] | Generation plus source, prompt, provider, approval, revision metadata | One image or audio artifact, metadata card, reviewer action | Compare generated draft and approved final with the full provenance panel. |

Adobe ranks first if the statement contains content, campaigns, brand rules, visual assets, or marketing operations. It ranks lower if the team cannot produce a real artifact. The proof is not a clever prompt; it is a complete content lifecycle connected to approved assets [8][9][20].

### Unknown sixth sponsor: portable mapping only

| Rank | [UNVERIFIED] shape | Why it is portable | 24-hour MVP | Demo |
|---|---|---|---|---|
| 1 | A narrow workflow agent grounded in sponsor data | Every named sponsor has a workflow or developer surface signal, but the sixth identity is unknown. | Input, retrieval, two tools, approval, trace. | Change the data and tool labels after the statement arrives. |
| 2 | Multimodal intake into a structured record | Google, Meta, and the India hackathon evidence support mixed-media directions [15][18][26]. | Image or voice -> three fields -> user correction -> record. | Show uncertainty and correction. |
| 3 | Create or transform an artifact with review | Adobe and the Creative Storyteller category support this pattern [8][20][24]. | One artifact, one rule set, one approval step. | Draft -> violation -> revision -> approved export. |

Do not guess the sixth company. A portable architecture has positive expected value because it preserves optionality while the statement is unknown.

## Five Cross-Cutting Themes That Can Win Regardless of Sponsor

### 1. A bounded agent that completes one job

Observation: Google and Accenture both provide direct agent signals, and the observed hackathon examples use constrained tasks rather than a claim of universal autonomy [24][22][7]. Mechanism: a bounded state machine makes tool use, errors, and success observable. Implication: a judge can evaluate behavior in minutes. Recommendation: choose one job, two tools, one approval gate, and one receipt.

### 2. Multimodal input followed by structured output

Observation: Gemini's Android API names text, image, audio, and video capabilities, while Llama 4 is described as natively multimodal [15][18]. Mechanism: a photo or voice note exposes a genuine input bottleneck and lets the team demonstrate grounding. Implication: the app has a memorable moment. Recommendation: support one modality pair well, show the original input, and let the user correct extracted fields.

### 3. Trust artifacts: evidence, provenance, permissions, and audit

Observation: HackerRank's agent used a bounded document corpus [7], Adobe's GenStudio API works with approved experiences and assets [20], and Orchestrate judging included live defense [12]. Mechanism: trust is created by inspectable intermediate state, not by a model label. Implication: the same product can be defended to a technical judge and a business judge. Recommendation: make a trace screen a core feature, not a last-minute debug panel.

### 4. Local-first or consent-based fallback

Observation: Apple's current framework signal explicitly includes on-device and Private Cloud Compute models [27], and Android's API is integrated into mobile application development [15]. Mechanism: a network boundary makes privacy and reliability visible. Implication: the demo survives quota, connectivity, and sensitive-data questions. Recommendation: implement a local fixture or lightweight local step, then show remote enhancement only after consent.

### 5. India-first workflow, not India-themed decoration

Observation: the retrieved India hackathon guide names Indic NLP, while the Masters' Union description emphasizes solving real-world problems [26][30]. Mechanism: a vernacular input reduces friction at the point of action, whereas a translated landing page does not complete a task. Implication: the judge sees local relevance plus engineering depth. Recommendation: use one language or code-switching path for intake, preserve the original, show correction, and write a structured ticket or record.

These five themes are complementary. An ideal portable build accepts a voice or image, grounds it in a small corpus, proposes one tool action, waits for approval, records the evidence, and produces a useful artifact or record. That combination can be branded as Google, Apple, Meta, Accenture, Adobe, or the unknown sixth sponsor by changing the interface and integration layer.

## Overnight Build Plan for the Aug 15-16 Constraint

The schedule in the brief is [UNVERIFIED], but if Team 511 is operating overnight, the build needs explicit cut lines. This is an implementation recommendation, not a claim about organizer rules.

| Relative phase | Build output | Cut if late |
|---|---|---|
| Before the statement | Provider adapter, local fixtures, generic trace schema, UI shell, ten test cases. | Fancy landing page and multi-agent collaboration. |
| First 30 minutes after the drop | Extract nouns, actor, input, desired outcome, system of record, and risk. Map each to one tool. | Broad market research during the build. |
| First 2 hours | Happy-path vertical slice from input to receipt. | Multiple modalities. Keep one. |
| Hours 3-6 | Retrieval, typed tools, approval gate, failure path, evidence panel. | Autonomous multi-step loops. |
| Hours 7-10 | Sponsor skin: exact API or product name where available, domain data, local language or offline feature. | A second product integration that does not appear in the demo. |
| Hours 11-14 | Evaluation set, red-team cases, role permissions, latency and quota fallback. | Training a custom model from scratch. |
| Hours 15-18 | Demo script, pitch narrative, architecture diagram, known limitations. | New feature work. |
| Final hours | Rehearsal, seeded data reset, video or screenshots only as backup, README with sources. | Last-minute refactor. |

The first hard cut is scope. A working single-agent workflow with evidence is preferable to a multi-agent architecture whose second agent is only a prompt. The second hard cut is integration. If a sponsor API is unavailable, keep a clearly labeled adapter and demonstrate the product-shaped workflow with a fixture rather than hiding the substitution.

## Pitch Structure: A Judge Can Verify It in Five Minutes

1. **Problem and user**: name the actor, the input, the current manual step, and the measurable outcome.
2. **Sponsor fit**: name one verified product or API, such as Gemini Developer API, Foundation Models, Llama 4, Accenture Edge, Firefly, or GenStudio Experience API. Do not list five logos.
3. **Live input**: use a real-looking image, voice note, document, or record, not a typed lorem ipsum prompt.
4. **Agent trace**: show interpretation, retrieval, tool arguments, permission check, and approval.
5. **Result**: show the completed ticket, approved asset, structured record, or accessible mobile action.
6. **Failure**: deliberately trigger ambiguity, missing evidence, offline mode, or a denied action.
7. **Impact**: report the number of steps removed or the task completed on the fixture. Do not invent production savings.
8. **Limits and next step**: say what is simulated, what is not supported, and the one integration that would be built next.

This structure follows the evidence that current student agent challenges evaluate the artifact and the defense, not only code generation [12][13]. It also protects Team 511 from overclaiming. A candid limitation becomes a product decision when the team shows the fallback and test.

## Risk Register and Failure Cases

| Risk | What can go wrong in 24 hours | Mitigation that is demonstrable |
|---|---|---|
| Unknown statement or sixth sponsor | Team builds the wrong domain. | Keep tools, schema, and provider adapter generic until nouns are known. |
| API quota or authentication | Live model call fails. | Cache fixtures, provide a text or local fallback, and show status. |
| Hallucinated action | Agent writes a bad record or asset. | Typed tool schema, approval gate, validation, and undo or escalation. |
| Prompt injection | Retrieved document instructs the agent to leak or act. | Treat retrieved text as data, filter instructions, use role permissions, test two attacks. |
| Multilingual error | Voice or translation misreads intent. | Preserve original, show normalized fields, allow correction, escalate low confidence. |
| Unclear sponsor fit | Product demo looks generic. | Put one exact sponsor API or program name next to the corresponding code path. |
| Misleading provenance | Mock content is presented as official generated output. | Label provider and fixture status, record prompt and asset lineage. |
| Weak defense | Judge asks why a choice was made and team cannot answer. | Each member owns one diagram: user, model, tools, evaluation, and limits. |

The most serious risk is not an imperfect model response. It is an uninspectable product that cannot tell the judge what it did. Current agent challenge evidence points toward a defenseable system: a bounded task, trace, and explanation [7][12].

## Synthesis: What the Sponsor Divergence Really Means

The five named sponsors converge on applied AI but diverge in the layer they monetize. **Google** exposes models, multimodal APIs, Android, Firebase, Cloud, and agent tooling [15][16][24]. Its strongest student-shaped outcome is an interactive agent. **Apple** exposes native Swift access to on-device and Private Cloud Compute models [27][29]. Its strongest outcome is a private, polished, device-native experience. **Meta** foregrounds open-weight native multimodality through Llama 4 [18]. Its strongest outcome is model choice and mixed-media scale, but deployment claims need care. **Accenture** foregrounds industry-specific agents and enterprise delivery through SAP, Google Cloud, and Accenture Edge [21][22]. Its strongest outcome is a governed operational workflow. **Adobe** foregrounds creative co-pilots, Creative Agent, and approved experiences and assets through GenStudio [8][9][20]. Its strongest outcome is a content lifecycle.

| Dimension | Google | Apple | Meta | Accenture | Adobe |
|---|---|---|---|---|---|
| Primary mechanism | Multimodal model plus agent tools [15][24] | Native on-device model plus Swift UX [27][29] | Open-weight natively multimodal model [18] | Industry agent plus enterprise workflow [21][22] | Generative media plus approved content operations [8][9][20] |
| Best 24-hour proof | Live input -> tool -> receipt | Offline or consented private task | Model adapter -> mixed-media output -> policy | Record -> approval -> system action | Brief -> draft -> review -> approved export |
| Main trade-off | Cloud and quota dependence | Device/API availability and narrower surface | Serving and licensing complexity | Enterprise integration is easy to overclaim | Generation without governance looks shallow |
| Judge-visible differentiator | Real-time multimodal interaction | Privacy, accessibility, polish | Openness and model flexibility | Measurable operational outcome | Asset lineage and brand approval |
| Evidence confidence for a Craft N Code prompt | Product and challenge evidence verified; exact prompt unverified | Product and program verified; exact prompt unverified | Product verified; student prompt unverified | Product and internship signals verified; student prompt unverified | Product and API verified; student prompt unverified |

The non-obvious tension is that "hottest technology" and "most sponsor-aligned product" are not identical. A multi-agent system may sound hot but be less persuasive than one reliable tool loop. A giant model may sound advanced but be less Apple-aligned than a small on-device feature. A generated image may be visually strong but less Adobe-aligned than an approved asset workflow. A polished UI may be Apple-like but fail Accenture if it cannot alter a process or record.

The second tension is openness versus control. Meta's open-weight signal encourages model choice [18], while Accenture and Adobe evidence emphasizes enterprise deployment, approved content, and industry context [20][21][22]. Team 511 can reconcile them by placing the model behind an adapter and keeping policy, retrieval, approval, and audit outside it. That architecture is sponsor-neutral and technically defensible.

The third tension is novelty versus evidence. The available public research verifies products and a few challenge shapes, but not the Craft N Code statement. Therefore, the responsible strategy is not to pretend to know the prompt. It is to pre-build the parts that survive a prompt change: structured input, retrieval, typed tools, approval, evaluation, provenance, and a clear demo. When the statement arrives, choose the sponsor skin that matches the nouns.

### Final decision rule for Team 511

If the statement contains **live camera, voice, or UI control**, select the Google-shaped agent. If it contains **privacy, offline, accessibility, or native mobile polish**, select the Apple-shaped local-first utility. If it contains **open models, creators, mixed media, or community content**, select the Meta-shaped model adapter. If it contains **industry operations, SAP-like records, service levels, manufacturing, cybersecurity, or enterprise roles**, select the Accenture-shaped workflow agent. If it contains **campaigns, brand assets, creative production, image or video, or approvals**, select the Adobe-shaped content pipeline. If none of those cues appears, use the unknown-sixth portable agent with multimodal intake, bounded retrieval, and a trace.

The highest-confidence build choice across all branches is therefore: **one multimodal intake, one bounded knowledge base, two typed tools, one human approval gate, one evidence and provenance panel, one offline or quota fallback, and one measurable completed task**. That is [INFERRED] strategy grounded in the verified challenge and product signals above, not a claim that any sponsor has leaked the Craft N Code problem.

## References

The following URLs are the sources used for the factual claims in this report. Numeric markers in the text bind claims to the corresponding corpus documents.

### Event and uncertainty checks

- https://www.instagram.com/craftncraft
- https://www.instagram.com/rcw.in

### Google

- https://developer.android.com/ai/gemini/developer-api
- https://developers.google.com/
- https://firebase.google.com/products/firebase-ai-logic
- https://cloud.google.com/products/gemini-enterprise-agent-platform
- https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge
- https://developers.google.com/community/gdsc-solution-challenge/winners
- https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26
- https://blog.google/innovation-and-ai/technology/ai

### Apple

- https://developer.apple.com/documentation/foundationmodels
- https://developer.apple.com/swift-student-challenge
- https://developer.apple.com/wwdc26/guides/ios
- https://developer.apple.com/videos/play/wwdc2025/286

### Meta

- https://ai.meta.com/blog
- https://ai.meta.com/blog/llama-4-multimodal-intelligence
- https://developers.meta.com/

### Accenture

- https://newsroom.accenture.com/offerings-and-products-blog
- https://newsroom.accenture.com/news/2026/accenture-edge-and-google-cloud-bring-scalable-agentic-ai-solutions-to-mid-market-companies
- https://www.accenture.com/us-en/careers/jobdetails?id=R00276795_en

### Adobe

- https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-ai-overview.html
- https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion
- https://developer.adobe.com/firefly-services/docs/firefly-api
- https://developer.adobe.com/genstudio-api
- https://news.adobe.com/news/2025/09/global-enterprises-embrace-adobe-ai-innovations-power-growth
- https://finance.yahoo.com/news/adobe-deepens-google-cloud-partnership-122839988.html

### Hackathon and judging patterns

- https://hackerrank.com/blog/behind-the-scenes-of-hackerrank-orchestrate
- https://hackerrank.com/hackerrank-orchestrate-may26
- https://hackerrank.com/hackerrank-orchestrate-august26
- https://hackerrank.com/features/ai-interviewer
- https://microsoft.github.io/AI_Agents_Hackathon/winners
- https://aigrants.in/topics/student-led-machine-learning-hackathons-india
- https://mastersunion.org/events/ai-hackathon
- https://aicmuj.com/
- https://arxiv.org/html/2604.16790v1

## References

1. *http://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26*. http://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26
2. *http://finance.yahoo.com/news/adobe-deepens-google-cloud-partnership-122839988.html*. http://finance.yahoo.com/news/adobe-deepens-google-cloud-partnership-122839988.html
3. *http://blog.google/innovation-and-ai/technology/ai*. http://blog.google/innovation-and-ai/technology/ai
4. *http://developers.google.com/community/gdsc-solution-challenge/winners*. http://developers.google.com/community/gdsc-solution-challenge/winners
5. *http://aicmuj.com/*. http://aicmuj.com/
6. *http://news.adobe.com/news/2025/09/global-enterprises-embrace-adobe-ai-innovations-power-growth*. http://news.adobe.com/news/2025/09/global-enterprises-embrace-adobe-ai-innovations-power-growth
7. *http://hackerrank.com/blog/behind-the-scenes-of-hackerrank-orchestrate*. http://hackerrank.com/blog/behind-the-scenes-of-hackerrank-orchestrate
8. *http://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-ai-overview.html*. http://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-ai-overview.html
9. *http://news.adobe.com/news/2026/06/adobe-unveils-major-expansion*. http://news.adobe.com/news/2026/06/adobe-unveils-major-expansion
10. *http://arxiv.org/html/2604.16790v1*. http://arxiv.org/html/2604.16790v1
11. *http://hackerrank.com/hackerrank-orchestrate-may26*. http://hackerrank.com/hackerrank-orchestrate-may26
12. *http://hackerrank.com/hackerrank-orchestrate-august26*. http://hackerrank.com/hackerrank-orchestrate-august26
13. *http://github.com/nishchayramaul/Hackerrank-Orchestrate--2026*. http://github.com/nishchayramaul/Hackerrank-Orchestrate--2026
14. *http://hackerrank.com/features/ai-interviewer*. http://hackerrank.com/features/ai-interviewer
15. *Gemini Developer API | AI | Android Developers*. https://developer.android.com/ai/gemini/developer-api
16. *Google for Developers | Build with Gemini*. http://developers.google.com/
17. *AI at Meta Blog*. https://ai.meta.com/blog
18. *The Llama 4 herd: The beginning of a new era of natively ...*. https://ai.meta.com/blog/llama-4-multimodal-intelligence
19. *Meta for Developers*. http://developers.meta.com/
20. *GenStudio API overview - developer.adobe.com*. https://developer.adobe.com/genstudio-api
21. *Offerings and Products Blog*. https://newsroom.accenture.com/offerings-and-products-blog
22. *Accenture Edge and Google Cloud Bring Scalable Agentic AI ...*. https://newsroom.accenture.com/news/2026/accenture-edge-and-google-cloud-bring-scalable-agentic-ai-solutions-to-mid-market-companies
23. *Accenture Internship Opportunities (Jun/Jul/Aug) 2026*. https://www.accenture.com/us-en/careers/jobdetails?id=R00276795_en
24. *Winners and highlights of the Gemini Live Agent Challenge ...*. https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge
25. *Winners - AI Agents Hackathon 2025 - microsoft.github.io*. https://microsoft.github.io/AI_Agents_Hackathon/winners
26. *Student-Led Machine Learning Hackathons in India: A Guide*. https://aigrants.in/topics/student-led-machine-learning-hackathons-india
27. *Foundation Models | Apple Developer Documentation*. https://developer.apple.com/documentation/foundationmodels
28. *Swift Student Challenge Apple https://developer.apple.com › swift-student-challenge*. https://developer.apple.com/swift-student-challenge
29. *WWDC26 iOS guide - Apple Developer*. https://developer.apple.com/wwdc26/guides/ios
30. *India’s Biggest High School AI Hackathon by Masters’ Union*. https://mastersunion.org/events/ai-hackathon
31. *Craft n Craft India (@craftncraft) · Jaipur Instagram · craftncraft 440+ फ़ॉलोअर*. https://www.instagram.com/craftncraft
32. *Rajasthan Crafts & Weaves (@rcw.in) · Bangalore Instagram · rcw.in 500+ फ़ॉलोअर*. https://www.instagram.com/rcw.in
