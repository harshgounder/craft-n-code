# Craft N Code 2026: Evidence, Gaps, and Build-Lane Predictions

## Executive Summary

- **Direct-Text Gap**: The research run did not retrieve a publicly readable Craft N Code 2024 or 2025 state-round problem statement, nor an organizer statement proving that Google, Apple, Meta, Accenture, or Adobe authored the 2026 questions. Treat the sponsor-set claim as **UNVERIFIED**, not as established fact. The public Rewind & Recode listing was blocked by a cookies-disabled page [1], while the 2025 Instagram result exposed no description [2]. -> Do not design around an alleged sponsor brief until the prompt drops.
- **Google Signal**: The strongest verified current Google direction is agent construction: ADK is described as an open-source framework for building, debugging, and deploying AI agents, including multi-agent systems and business workflows [3]. -> Prepare a tool-using agent with explicit approvals, logs, and fallback behavior.
- **Meta Signal**: Meta's official Llama 4 announcement describes Scout and Maverick as open-weight, natively multimodal models with long-context support [4]. -> Prepare an image-plus-text workflow, but keep a non-LLM fallback because model access and latency may vary.
- **Adobe Signal**: Adobe's official Firefly documentation says its API integrates generative AI into creative workflows [5], and the audio/video reference covers generation and processing [6]. -> Prepare a provenance-aware media workflow rather than a generic chatbot.
- **Apple Signal**: Apple's 2026 Swift Student Challenge page reports that the 2026 results are available [7], and Apple's newsroom highlights 2026 winners creating AI-enabled accessibility apps [8]. -> If the task is mobile or hardware-adjacent, prioritize accessibility, on-device interaction, and a polished SwiftUI prototype.
- **Accenture Signal**: The Accenture Ventures Tech Next Challenge 2026 page says its focus is startups using autonomous intelligence to shape the next era of work [9]. -> Frame an enterprise workflow with measurable time, quality, or compliance benefits, not only a model demo.
- **Fallback Tracks**: The five internal tracks in the brief, Legacy, Night Ops, Signal, Open, and Hardware, remain useful as preparation categories, but the research did not independently verify that they are official 2026 problem categories. -> Build a modular core that can be re-skinned for any one of the five.
- **Decision Rule**: Evidence supports preparing for agentic, multimodal, accessible, creative, and enterprise workflow prompts; it does not support claiming that any one sponsor will write a particular statement. -> Bring three thin vertical slices and select only after the 21:30 IST release.

## Scope, Labels, and Evidence Standard

This is a constrained research report based on the sources actually retrieved in the run. **VERIFIED** means the retrieved source visibly states the proposition. **INFERRED** means the recommendation is a reasoned preparation strategy derived from verified product or event signals. **UNVERIFIED** means the requested claim was searched for but not established by a readable source. A search hit or event listing is not treated as proof that a sponsor authored a problem.

The requested output asked for 15 or more verbatim sponsor problem texts, 25 or more tables, 50 or more unique sources, and 120 or more inline citations. The run did not obtain that evidence set. Inventing missing quotations would be worse than returning a clearly bounded partial answer. The tables below therefore distinguish source-backed texts from leads and negative findings.

| Status | Meaning | Use in decisions |
|---|---|---|
| VERIFIED | Exact proposition visible in a retrieved source | Safe to use as evidence |
| INFERRED | Strategy derived from verified evidence | Use as preparation, not as history |
| UNVERIFIED | Search did not expose adequate evidence | Do not present as fact |

| Evidence type | Retrieved? | Confidence |
|---|---:|---|
| Official product documentation | Yes | High |
| Official company newsroom or blog | Yes | High |
| Official student challenge page | Yes | High |
| College event listing | Yes | Medium for event existence |
| Search-result lead without readable text | Yes | Low for problem content |
| Craft N Code question-writing proof | No | Unverified |
| Craft N Code 2024 MUJ problem | No | Unverified |

## A1. Google: What Is Verified and What Is Not

### A1.1 Google Solution Challenge

The retrieved 2023 Google FAQ confirms that teams are expected to identify a challenge and problem statement and explain success using metrics, goals, and outcomes [10]. That is evidence about the evaluation framework, not a single sponsor-authored problem text. The retrieved material did not provide exact 2023, 2024, or 2025 theme wording that can safely be quoted as a verbatim statement.

A 2026 Google Developer Groups on Campus listing describes Solution Challenge 2026 as an AI-powered innovation event in which participants design and build impactful solutions using Google technologies and modern AI tools [11]. A separate India-facing listing says participants must be enrolled in an Indian university or college [12]. These are useful current signals, but neither establishes that Google will write Craft N Code's Rajasthan prompt.

> "Does the solution address the challenge (and problem statement) identified by the team? Does the team adequately describe the success of their solution using metrics, goals, and outcomes?" [10]
>
> Event: Google Solution Challenge FAQ, 2023. URL: https://developers.google.com/community/gdsc-solution-challenge/faq

| Google item | Year | Location | Retrieved wording | Status |
|---|---:|---|---|---|
| Solution Challenge FAQ | 2023 | Global / student program | Challenge and problem statement are identified by the team; success uses metrics, goals, and outcomes [10] | VERIFIED |
| Solution Challenge campus listing | 2026 | Bhubaneswar, India / virtual listing | AI-powered innovation event using Google technologies and modern AI tools [11] | VERIFIED |
| India eligibility listing | 2026 | India | Participants must be enrolled in a university or college of India [12] | VERIFIED |
| Google-authored Craft N Code statement | 2026 | MUJ | No readable source retrieved | UNVERIFIED |
| Google Girl Hackathon exact statement | 2023-2026 | India | No readable exact statement retrieved | UNVERIFIED |

### A1.2 Google preparation implication

The safe Google-shaped preparation is not a guessed quote. It is an agent or AI application whose success can be measured. ADK documentation describes agents, tools, debugging, deployment, and multi-agent systems [3]. That makes tool orchestration, human approval, observability, and a measurable outcome stronger preparation targets than a plain generative interface.

## A2. Apple: Swift Student Challenge and Accessibility

Apple's official Swift Student Challenge page says the challenge has given thousands of student developers opportunities to demonstrate creativity and coding capability through app playgrounds [7]. The retrieved page does not provide an Indian college hackathon problem statement. It therefore cannot support a claim that Apple authored a Craft N Code problem.

The strongest current Apple signal is the 2026 accessibility direction. Apple's newsroom describes four 2026 Swift Student Challenge winners creating innovative apps that leverage AI and focus on accessibility [8]. Apple's 2026 terms state that applicants must be enrolled in, or have graduated within the last 90 days from, an accredited academic institution or official homeschool equivalent, or be an Apple Developer Academy student [13]. These facts support an accessibility-first mobile build, but not a verbatim sponsor prompt.

> "Meet four Swift Student Challenge winners who are creating innovative apps that leverage AI and focus on accessibility." [8]
>
> Event: Apple Newsroom, 2026 Swift Student Challenge winners. URL: https://www.apple.com/newsroom/2026/05/ai-meets-accessibility-in-this-years-swift-student-challenge

| Apple item | Year | Retrieved fact | Status |
|---|---:|---|---|
| Swift Student Challenge | Current page | Thousands of student developers; app playgrounds [7] | VERIFIED |
| Swift Student Challenge terms | 2026 | Enrollment or recent graduation eligibility [13] | VERIFIED |
| Accessibility winner coverage | 2026 | AI plus accessibility apps [8] | VERIFIED |
| Indian Apple college hackathon statement | 2023-2026 | Not retrieved | UNVERIFIED |
| Apple-authored Craft N Code statement | 2026 | Not retrieved | UNVERIFIED |

| If the dropped prompt asks for... | Build response | Main risk |
|---|---|---|
| Accessible personal tool | SwiftUI interface, VoiceOver labels, large text, low-friction input | Accessibility treated as decoration |
| On-device assistant | Local-first state, graceful offline mode, clear privacy boundary | Network or model unavailability |
| Sensor or hardware app | Simple sensor abstraction and simulator data | Hardware integration consumes the build window |

## A3. Meta: Llama 4 and the Limits of the Hackathon Evidence

The retrieved Meta search did not reveal a readable Indian Build with AI, GenAI Genesis, or Llama Impact India problem statement. A search result for an unrelated 2026 emerging technologies hackathon exposed a page with 21 statements across nine technology verticals [14], but it does not establish Meta sponsorship or authorship. A Smart India Hackathon 2024 page provides one unrelated example, "Downscaling of Satellite based air quality map using AI/ML," with named experts [15]. It should not be relabeled as a Meta problem.

Meta's official Llama 4 announcement is materially more useful for current preparation. It introduces Scout and Maverick as the first open-weight natively multimodal models and mentions unprecedented context-length support [4]. Meta's model-card result identifies Scout and Maverick as pretrained and instruction-tuned mixture-of-experts models [16]. The public Llama site emphasizes multimodality, low costs, and efficiency [17].

> "We're introducing Llama 4 Scout and Llama 4 Maverick, the first open-weight natively multimodal models with unprecedented context length support." [4]
>
> Source: Meta AI, "The Llama 4 herd." URL: https://ai.meta.com/blog/llama-4-multimodal-intelligence

| Meta lead or fact | Year | What it establishes | Status |
|---|---:|---|---|
| Llama 4 Scout and Maverick | 2025 announcement | Open-weight, natively multimodal, long context [4] | VERIFIED |
| Llama 4 model cards | Current docs | Scout and Maverick model families [16] | VERIFIED |
| Llama public product page | Current | Multimodality, cost, efficiency positioning [17] | VERIFIED |
| Meta Build with AI India statement | 2023-2026 | Exact readable text not retrieved | UNVERIFIED |
| GenAI Genesis India statement | 2023-2026 | Exact readable text not retrieved | UNVERIFIED |
| Llama Impact India statement | 2023-2026 | Exact readable text not retrieved | UNVERIFIED |

| Likely multimodal task shape | Evidence basis | Preparation |
|---|---|---|
| Image plus text understanding | Llama 4 is described as natively multimodal [4] | OCR, image upload, structured extraction |
| Long-context evidence review | Official announcement mentions unprecedented context support [4] | Chunking, citations, retrieval limits |
| Low-cost deployable assistant | Llama site emphasizes low costs and efficiency [17] | Quantized or API-agnostic interface |

## A4. Accenture: Enterprise Workflow Rather Than a Guessed Theme

The run did not retrieve the requested 2023-2026 Accenture Innovation Challenge texts from Unstop. A Devpost forum lead titled "Accenture Problem Statements" lists examples including speech-to-sign-language conversion, a personalized gym trainer, and an AI-themed item [18]. Because the retrieved snippet is a forum listing and not an official Unstop or Accenture event brief, these are **VERIFIED only as visible lead text**, not verified as a specific Indian college event, year, city, or official Accenture-authored brief.

The current official Accenture Ventures Tech Next Challenge page says the eighth edition focuses on startups using autonomous intelligence to shape the next era of work [9]. That is a strong product-direction signal. It supports a workflow problem with a user, a business process, an agent, measurable performance, and human escalation.

> "Speech to sign language conversion. AI for community initiative." [18]
>
> Source: Code Without Barriers Devpost forum, "Accenture Problem Statements." URL: https://codewithoutbarriers.devpost.com/forum_topics/36101-accenture-problem-statements

| Accenture item | Event/year/city | Text or signal | Status |
|---|---|---|---|
| Devpost forum lead | Not established | Speech-to-sign-language conversion [18] | VERIFIED lead, event metadata UNVERIFIED |
| Devpost forum lead | Not established | Personalized Gym TrAIner [18] | VERIFIED lead, event metadata UNVERIFIED |
| Tech Next Challenge | 2026 | Autonomous intelligence and next era of work [9] | VERIFIED |
| Innovation Challenge 2023 | India | Exact official statement not retrieved | UNVERIFIED |
| Innovation Challenge 2024 | India | Exact official statement not retrieved | UNVERIFIED |
| Innovation Challenge 2025 | India | Exact official statement not retrieved | UNVERIFIED |
| Innovation Challenge 2026 | India | Exact official statement not retrieved | UNVERIFIED |

| Enterprise requirement | Why it matters | Build artifact |
|---|---|---|
| Measurable outcome | Autonomous intelligence is framed around work transformation [9] | Before/after time or error metric |
| Human escalation | Enterprise workflows cannot assume perfect autonomy | Approval queue and override |
| Auditability | Generated actions need traceability | Event log and decision record |
| Accessibility | The visible lead includes speech-to-sign conversion [18] | Alternative input/output mode |

## A5. Adobe: Firefly API Is Verified; Adobe India Problem Text Is Not

The retrieved Adobe search found an Adobe DevCraft listing on Unstop, described as "Adobe DevCraft - 2024," associated with Invictus24 at DTU in New Delhi [19]. The search preview did not expose the problem text. Therefore the event lead is usable for further investigation but not as a verbatim quote.

Adobe's official Firefly API overview says the API makes it easy to integrate generative AI into creative workflows [5]. The Firefly API reference covers image generation and related services [20]. Adobe's audio and video reference says its REST API provides resources for audio and video generation and processing [6], while the broader documentation describes Firefly, Lightroom, Photoshop, and Content Tagging APIs as a combined suite [21].

> "The Adobe Firefly API makes it easy for you to integrate generative AI into your creative workflows." [5]
>
> Source: Adobe Developer, Firefly API overview. URL: https://developer.adobe.com/firefly-services/docs/firefly-api

| Adobe item | Year/location | Evidence | Status |
|---|---|---|---|
| Adobe DevCraft | 2024, DTU New Delhi | Event listing visible, problem text absent [19] | VERIFIED event lead |
| Firefly API overview | Current | Generative AI in creative workflows [5] | VERIFIED |
| Firefly API reference | Current | Image generation and related services [20] | VERIFIED |
| Audio and Video API | Current | Audio/video generation and processing [6] | VERIFIED |
| Firefly documentation suite | Current | Firefly, Lightroom, Photoshop, Content Tagging APIs [21] | VERIFIED |
| Adobe Creative Jams India exact brief | 2023-2026 | Not retrieved | UNVERIFIED |
| Adobe-authored Craft N Code statement | 2026 | Not retrieved | UNVERIFIED |

| Adobe-shaped task | Preparation | Failure case |
|---|---|---|
| Generate campaign assets | Prompt, generate, edit, export | Uncontrolled brand or factual errors |
| Transform audio/video | Upload, process, caption, summarize | Large files and timeout |
| Creative provenance | Store prompt, model, asset lineage | Cannot explain generated output |

## B1. Craft N Code and Rewind & Recode State-Round History

The retrieved Unstop result is a Rewind and Recode listing associated with D3 Tech Fest and IIIT Bhubaneswar [1]. The page could not be read because it reported cookies disabled. Search results also surfaced 2025 Instagram posts titled "Join the Rewind & Recode Hackathon 2025" and "The Rewind & Recode Hackathon is here," but both exposed no usable description [2][22]. These results support the existence of a public event trail, not the problem text, state-round host, or question author.

| Requested history item | Result | Status |
|---|---|---|
| 2024 state-round statement, any state | Not retrieved | UNVERIFIED |
| 2025 state-round statement, any state | Not retrieved | UNVERIFIED |
| Rajasthan 2024 MUJ problem | Not retrieved | UNVERIFIED |
| Rajasthan 2024 problem author | Not retrieved | UNVERIFIED |
| Karnataka state-round problem | Not retrieved | UNVERIFIED |
| Organizer statement on club versus sponsors | Not retrieved | UNVERIFIED |
| 2025 finals exact text | Not retrieved | UNVERIFIED |
| Rewind & Recode public listing | Unstop result found but blocked [1] | VERIFIED lead |
| 2025 social posts | Titles found, descriptions unavailable [2][22] | VERIFIED lead |

| Source trail | What was visible | What cannot be inferred |
|---|---|---|
| Unstop listing | Rewind and Recode / D3 Tech Fest / IIIT Bhubaneswar [1] | Exact problem, author, sponsor authorship |
| Instagram post 1 | Rewind & Recode Hackathon 2025 title [2] | State, prompt, organizer decision |
| Instagram post 2 | Rewind & Recode announcement title [22] | State, prompt, sponsor role |
| Participant repository search | No qualifying repository result surfaced | Absence of a repo cannot be proven |

The practical conclusion is negative but important: no source retrieved in this run proves that sponsor companies write Craft N Code questions. The insider claim may be true, false, or only partly true, but it must remain **UNVERIFIED** until a sponsor announcement, organizer statement, or problem PDF says so.

## B2. 2024 Rajasthan Round at MUJ

The targeted search for Manipal University Jaipur returned a LinkedIn profile and MUJ Instagram accounts, including the university account and the LearnIT: School of IT account, but no readable Craft N Code problem text or author attribution. Prior context verifies that IEEE SB MUJ operates at Manipal University Jaipur and runs technology activities, but that does not establish that CSC MUJ authored the 2024 Rajasthan prompt [23].

| MUJ 2024 question | Evidence found | Conclusion |
|---|---|---|
| Was a Rajasthan round at MUJ held? | Search returned MUJ social leads | Event lead only |
| What was the problem? | No readable statement | UNVERIFIED |
| Who wrote it? | No attribution | UNVERIFIED |
| Did a sponsor write it? | No sponsor announcement | UNVERIFIED |
| Did CSC MUJ write it? | No organizer statement | UNVERIFIED |
| Is a participant repo available? | No qualifying result surfaced | UNVERIFIED, not disproven |

| Candidate source | URL | Status |
|---|---|---|
| Durga Prasad Goud LinkedIn result | https://in.linkedin.com/in/durga-prasad-goud | Lead only |
| Manipal University Jaipur Instagram | https://www.instagram.com/jaipurmanipal | Lead only |
| LearnIT MUJ Instagram | https://www.instagram.com/learnitmuj/ | Lead only |
| IEEE SB MUJ LinkedIn/company trail | https://www.linkedin.com/company/ieeesbmuj | Organization activity verified in prior context [23] |

The correct operational response is not to guess the 2024 prompt. Use the unverified history only as a hypothesis generator: search local drives, WhatsApp/Discord attachments, event certificates, finalist GitHub READMEs, and organizer photo captions after the current round. Do not cite a guessed 2024 problem to justify a 2026 build.

## B3. 2025 National Finals

The requested final themes, "AI for Personal Development" and "Agentic Healthcare Systems," were included in the research brief, but the run did not retrieve a participant repository or write-up quoting either full statement. The search for the first phrase returned an unrelated CraftAI repository describing a self-hostable AI application for customizable personal AI tools [24], and the search for the second did not surface a qualifying Craft N Code source. Neither result can be treated as a final-round statement.

| 2025 final item | Exact text retrieved? | Status |
|---|---:|---|
| AI for Personal Development | No | UNVERIFIED |
| Agentic Healthcare Systems | No | UNVERIFIED |
| National finalist repository quoting prompt | No qualifying result | UNVERIFIED |
| Official final problem PDF | Not retrieved | UNVERIFIED |
| Sponsor authorship | Not retrieved | UNVERIFIED |

| Search hit | Why it is insufficient |
|---|---|
| CraftAI repository | It describes a personal AI product, but not Craft N Code [24] |
| Generic agentic-healthcare results | No qualifying Craft N Code event attribution surfaced |
| Organizer/event leads | No full text was readable |

A preparation inference is still possible: the two labels suggest personal productivity and healthcare agents as prior themes, but labels are not specifications. Teams should not assume required users, data, APIs, safety criteria, or deployment constraints from the labels alone.

## C1. 2026 Traces and Question-Writer Claims

The targeted 2026 search did not find a readable sponsor announcement, official Craft N Code page, or CSC MUJ post saying that Google, Apple, Meta, Accenture, or Adobe will author the questions. It returned irrelevant problem-statement and research-problem pages, including a MUJ Central site unrelated to Craft N Code [25][26]. The search therefore provides no public confirmation of the insider claim.

| 2026 trace requested | Retrieved result | Status |
|---|---|---|
| Craft N Code 2026 sponsor announcement | None qualifying | UNVERIFIED |
| craftncode-2026.vercel.app sponsor page | No qualifying readable result | UNVERIFIED |
| CSC MUJ question-author post | None qualifying | UNVERIFIED |
| Google announcement naming Craft N Code | None qualifying | UNVERIFIED |
| Apple announcement naming Craft N Code | None qualifying | UNVERIFIED |
| Meta announcement naming Craft N Code | None qualifying | UNVERIFIED |
| Accenture announcement naming Craft N Code | None qualifying | UNVERIFIED |
| Adobe announcement naming Craft N Code | None qualifying | UNVERIFIED |

| Claim | Evidence threshold needed | Current decision |
|---|---|---|
| Sponsors authored questions | Official sponsor or organizer statement, or prompt document attribution | Do not rely on it |
| Five fallback tracks are official | Event page or released rules | Treat as internal preparation categories only |
| 21:30 release time | Organizer communication | Use only as team-provided logistics, not independently verified here |
| Rajasthan round is at MUJ | Official event communication | Search produced MUJ leads but not readable confirmation |

## C2. Product Pushes That Can Shape an August 2026 Prompt

### C2.1 Product signal matrix

| Company | Current source | Verified capability or positioning | Prompt implication |
|---|---|---|---|
| Google | ADK documentation | Build, debug, and deploy reliable AI agents at enterprise scale [3] | Tool-using agent with logs and approvals |
| Google | Solution Challenge campus listing | AI-powered innovation using Google technologies and modern AI tools [11] | Real-world impact plus measurable outcome |
| Meta | Llama 4 announcement | Open-weight, natively multimodal Scout and Maverick [4] | Text-image or document reasoning |
| Meta | Llama site | Multimodality, low costs, efficiency [17] | API-agnostic or local-friendly build |
| Adobe | Firefly overview | Integrate generative AI into creative workflows [5] | Creative asset pipeline |
| Adobe | Audio/video reference | Audio/video generation and processing [6] | Media transformation or accessibility |
| Apple | 2026 newsroom | AI plus accessibility app examples [8] | Accessible mobile experience |
| Apple | Swift Challenge page | App playgrounds and student creativity [7] | Polished Swift prototype |
| Accenture | Tech Next Challenge 2026 | Autonomous intelligence and the future of work [9] | Enterprise process automation |

### C2.2 Google agentic APIs

ADK is the clearest source-backed direction. The documentation explicitly covers agents and tools, movement toward multi-agent systems, debugging, and deployment [3]. A likely prompt may therefore ask teams to coordinate tools or agents, but that is **INFERRED**, not a prediction of the actual question.

Recommended minimum architecture: a task router, one or two deterministic tools, a structured state object, a human approval gate, an audit log, and a failure response. A demo that only streams text will be weaker than a small agent that visibly performs and records a useful action.

### C2.3 Meta multimodality

Llama 4's official announcement supports preparing for multimodal input [4]. A robust prototype should accept an image or document, extract structured facts, show uncertainty, and let the user correct the result. The non-obvious risk is that a multimodal demo can look impressive while failing on poor lighting, regional language, handwriting, or ambiguous images.

### C2.4 Adobe creative APIs

Firefly Services combines creative and content-related APIs, while the Firefly API supports generative creative workflows [5][21]. Prepare a content pipeline with input, generation, edit, review, export, and provenance. A static image generator is less defensible than a workflow that solves a real communication or accessibility problem.

### C2.5 Apple accessibility

Apple's 2026 coverage makes accessibility a credible preparation direction [8]. Prepare VoiceOver labels, dynamic type, contrast, keyboard navigation, and an interaction mode that remains useful without perfect vision or fine motor control. This is an inference from Apple's current public emphasis, not evidence that Craft N Code will ask for an accessibility app.

### C2.6 Accenture enterprise agents

Accenture's 2026 Tech Next description centers autonomous intelligence and the next era of work [9]. Prepare a business process with a baseline, an intervention, and a measurable result. Add escalation and auditability because an autonomous workflow without controls is a liability rather than an enterprise solution.

## D. Synthesis: What Team 511 Should Build Before the Prompt Drops

### D.1 Comparative strategy table

| Direction | Mechanism | Scope | Trade-off | Best 10-minute decision |
|---|---|---|---|---|
| Google | Agent plus tools and workflows [3] | Process execution | Integration and reliability work | Choose if prompt names agents, automation, or operations |
| Meta | Multimodal open-weight model [4] | Images, documents, long context | Model/runtime uncertainty | Choose if prompt contains visual or document input |
| Adobe | Generative creative workflow [5] | Assets, media, content tagging [21] | Provenance and brand safety | Choose if prompt concerns communication or media |
| Apple | Swift app, AI, accessibility [8] | Personal/mobile experience | Platform and device constraints | Choose if prompt is user-facing or accessibility-led |
| Accenture | Autonomous intelligence for work [9] | Enterprise process | Need ROI, controls, and measurable outcomes | Choose if prompt names organizations or workflows |
| Internal tracks | Club-defined preparation categories | Legacy, Night Ops, Signal, Open, Hardware | Official status unverified | Use only as a routing taxonomy until release |

The major tension is between sponsor-product specificity and hackathon adaptability. A sponsor-shaped solution can score well if the released problem names that ecosystem, but it can waste the ten-minute selection window if the actual task is unrelated. The modular strategy wins because the core can retain the same data model, evaluation harness, and UI shell while swapping the model or tool adapter.

### D.2 Recommended pre-release architecture

| Component | Prepare now | Why |
|---|---|---|
| Input adapter | Text, image, PDF, sensor/mock event | Covers multimodal and hardware prompts |
| Orchestrator | Deterministic router plus optional agent | Supports Google and Accenture-shaped tasks |
| Model adapter | Pluggable Google, Llama, and local mock | Avoids vendor lock-in |
| Creative adapter | Image/media generation interface | Supports Adobe-shaped tasks |
| Mobile shell | Responsive web shell or SwiftUI starter | Supports Apple-shaped tasks |
| Safety layer | PII redaction, consent, approval | Important for healthcare and enterprise |
| Evidence layer | Source links, confidence, audit events | Turns a demo into a defensible system |
| Evaluation | Latency, accuracy, completion, fallback | Aligns with measurable success expectations [10] |

### D.3 Failure cases to avoid

| Failure | Why it fails | Countermeasure |
|---|---|---|
| Building a guessed sponsor prompt | Sponsor authorship is unverified | Wait for released text |
| Generic chatbot | No measurable workflow outcome | Define user, action, metric |
| Agent with unrestricted actions | Unsafe and hard to demo | Approval gates and mock tools |
| Multimodal demo without error handling | Poor inputs break the story | Confidence and correction UI |
| Media generator without provenance | Reviewers cannot assess origin or safety | Store prompts and asset lineage |
| Mobile-only build before prompt | Wrong platform or time cost | Keep web and API fallback |
| Healthcare claims without boundaries | Risk of unsafe advice | Triage, escalation, and non-diagnostic framing |

## Final Ranked Predictions and Build Responses

The following are **INFERRED predictions**, not recovered historical or official text. They are intentionally written as exact candidate text for rehearsal only. Do not claim that these are the real questions.

### 1. Agentic operations and personal productivity

> **Predicted text, UNVERIFIED:** "Build an AI agent system that helps a student or worker plan, execute, and review a personal development goal. The system must use tools, maintain task state, explain its actions, request approval before consequential actions, and report measurable progress."

**Why ranked first:** Google publicly emphasizes agents, tools, multi-agent systems, debugging, and deployment [3], while the supplied history names "AI for Personal Development" as a 2025 final theme, though its exact text was not retrieved. **Build response:** task intake, planner, calendar or checklist mock tool, approval gate, progress dashboard, and a metric such as completed milestones or reduced planning time. Keep all external actions simulated until the prompt confirms integration requirements.

### 2. Multimodal community or campus assistant

> **Predicted text, UNVERIFIED:** "Create an accessible multimodal assistant that accepts text, images, or documents, extracts relevant information, answers questions with evidence, and routes uncertain or high-risk cases to a human. Demonstrate support for diverse users and imperfect inputs."

**Why ranked second:** Llama 4 is officially positioned as natively multimodal, open-weight, and long-context [4], while Apple's 2026 winner coverage connects AI with accessibility [8]. **Build response:** upload or camera input, OCR/extraction, evidence panel, confidence score, correction flow, multilingual-ready strings, and a human escalation path. Do not promise clinical diagnosis or legal certainty.

### 3. Responsible creative and enterprise media workflow

> **Predicted text, UNVERIFIED:** "Build a workflow that converts a real organizational brief into accessible, brand-consistent media assets using generative AI. The system must support review, revision, content provenance, and delivery in more than one media format."

**Why ranked third:** Adobe documents generative AI integration into creative workflows [5] and audio/video generation and processing [6], while Accenture's 2026 challenge emphasizes autonomous intelligence and the future of work [9]. **Build response:** brief intake, asset generation mock or API adapter, captions or alt text, reviewer approval, provenance record, and export. Use a clearly labeled mock if credentials or network access are unavailable.

## References

1. *Unstop - Competitions, Quizzes, Hackathons, Scholarships and Internships for Students and Corporates*. https://unstop.com/hackathons/rewind-and-recodeodisha-d3-tech-fest-iiit-bhubaneswar-international-institute-of-information-technology-iiit--1547834
2. *Join the Rewind & Recode Hackathon 2025*. https://www.instagram.com/p/DPIxKR8kQaN/
3. *Agent Development Kit | Gemini Enterprise Agent Platform ...*. https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
4. *The Llama 4 herd: The beginning of a new era of natively ... - Meta AI*. https://ai.meta.com/blog/llama-4-multimodal-intelligence
5. *Overview - Adobe Firefly API*. https://developer.adobe.com/firefly-services/docs/firefly-api
6. *Firefly Audio and Video API Reference - developer.adobe.com*. https://developer.adobe.com/audio-video-firefly-services/api
7. *Swift Student Challenge*. https://developer.apple.com/swift-student-challenge
8. *AI meets accessibility in this year's Swift Student Challenge*. https://www.apple.com/newsroom/2026/05/ai-meets-accessibility-in-this-years-swift-student-challenge
9. *Accenture Ventures Tech Next Challenge 2026 Banner*. https://technextchallenge.in/
10. *2023 Solution Challenge Frequently Asked Questions | Google for Developers*. https://developers.google.com/community/gdsc-solution-challenge/faq
11. *See Solution Challenge 2026 at Google Developer Groups GDG on Campus C. V. Raman Global University - Bhubaneswar, India*. https://gdg.community.dev/events/details/google-gdg-on-campus-c-v-raman-global-university-bhubaneswar-india-presents-solution-challenge-2026/
12. *Solution Challenge 2026 - Build with AI*. https://hack2skill.com/event/solution-challenge-2026
13. *Swift Student Challenge 2026 Terms and Conditions*. https://developer.apple.com/swift-student-challenge/policy
14. *Problem Statements | Emerging Technologies Hackathon 2026*. https://hackathon2026.tcoe.in/problem-statements.html
15. *Smart India Hackathon 2024 | Official website of ...*. https://vedas.sac.gov.in/en/sih2024.html
16. *Llama 4 | Model Cards and Prompt formats*. https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama4
17. *Llama: Industry Leading, Open-Source AI*. https://www.llama.com/
18. *Accenture Problem Statements*. https://codewithoutbarriers.devpost.com/forum_topics/36101-accenture-problem-statements
19. *Adobe DevCraft - 2024 Unstop https://unstop.com › hackathons*. https://unstop.com/hackathons/adobe-devcraft-invictus24-dtu-new-delhi-880209
20. *Firefly API Reference - developer.adobe.com*. https://developer.adobe.com/firefly-services/docs/firefly-api/api
21. *Documentation - Adobe Firefly Services*. https://developer.adobe.com/firefly-services/docs/guides
22. *The Rewind & Recode Hackathon is here! 🚀 Organized by ...*. https://www.instagram.com/p/DOyLQIPDB0x/
23. *http://linkedin.com/company/ieeesbmuj*. http://linkedin.com/company/ieeesbmuj
24. *GitHub - batuhan0sanli/CraftAI: CraftAI - Crafting Personalized AI Experiences · GitHub*. https://github.com/batuhan0sanli/CraftAI
25. *Crafting a Research Problem Statement | PDF | Methodology Scribd https://www.scribd.com › What...*. https://www.scribd.com/document/731275408/What-Is-a-Research-Problem-Statement
26. *MUJ CENTRAL 2.0*. https://mujcentral2-0.vercel.app/
