# Win the Overnight: A Reusable 24-Hour AI Hackathon Playbook

## Executive Summary

- **End-To-End Beats Novelty**: HackerRank Orchestrate explicitly graded the agent, the tickets it handled, the way builders directed coding tools, and a live defense rather than a flashy isolated prototype [3] -> Build one complete, judgeable workflow before adding features.
- **Bounded Evidence Creates Trust**: The Orchestrate brief describes a terminal support triage agent working from **774 Markdown documents** as its only knowledge base [2] -> Ship a small, inspectable corpus with source-linked answers instead of an open-ended chatbot.
- **Demo Readiness Is A Product Requirement**: Google Solution Challenge 2024 promoted a Final 10 and a live Demo Day on **June 27, 2024** [8] -> Design the pitch and the happy path before polishing the architecture.
- **Impact Needs A Specific User Moment**: The first-place Llama 4 Seattle entry, Team Sussi, is described as a solution for managing student technology use [9], while MongoDB AI Hackathon winner Haven is described as discreet help, mental-health support, and legal guidance for women in abusive situations [10] -> Open with the human decision your system improves, not the model name.
- **Agents Are Now A Familiar Judge Expectation**: The 2025 AI Agents Hackathon positioned itself around agent solutions and exposed builders to Semantic Kernel, AutoGen, Azure AI Agents SDK, and Microsoft 365 Copilot SDK [11] -> Use one reliable planner plus deterministic tools; do not build a fragile swarm overnight.
- **Multimodality Must Change The Decision**: The Meta LlamaCon winner page describes a Llama 4 system using multimodal image understanding to capture and detect movement every five frames for predefined events [UNVERIFIED: official page excerpt was only partially available] -> Add image, audio, or video only when it produces evidence that text alone cannot provide.
- **Safety Is A Visible Feature**: A public 24-hour evidence-review submission combines conversation reading, image inspection, user history, severity, risk flags, and supporting evidence [12] -> Put approval gates, risk flags, and an evidence panel on the main screen.
- **National Problems Reward Concrete Feasibility**: SIH 2025 materials emphasize drones and robots for medical emergencies and search and rescue [13], and contemporary reporting describes winners in renewable energy, disaster management, and smart education [14] -> Turn a large problem statement into one measurable operator action.
- **Public Winner Evidence Is Uneven**: The retrieved SIH 2024 record verifies that D. J. Sanghvi College had five software and one hardware winning teams [5], but the available excerpt does not expose each project's stack or repository -> Treat missing public details as [UNVERIFIED], never fill them with guesses.
- **A Zero-Dependency Demo Is The Rational Overnight Bet**: The team has only **8.5 hours** from the 21:30 problem drop to the 06:00 submission close, based on the supplied schedule -> Preinstall the scaffold, cache fixtures, keep one provider optional, and preserve a deterministic demo mode.
- **The Reusable Asset Is The Decision Pipeline**: Across the strongest evidence, the common unit is input -> extraction -> ranking -> action -> evidence -> human confirmation, not a particular framework -> Pre-build that pipeline and replace only the domain adapter after the problem drops.

## How To Read The Evidence

This report separates winner-level facts from design recommendations. `[VERIFIED]` means the retrieved source explicitly states the fact. `[INFERRED]` means the recommendation follows from the evidence and the team's overnight constraints, but the source does not state it as a rule. `[UNVERIFIED]` means the source page or repository was found, but the available evidence does not establish the claim. The distinction matters: a search result that says "winners" is not enough to invent a team's model, database, or leaderboard position.

The strongest case is HackerRank Orchestrate June 2026. A first-person page says the author won and describes the task as building a terminal support agent for HackerRank, Claude, and Visa in 24 hours [1]. HackerRank's own behind-the-scenes account describes the same event as a 24-hour hackathon in which participants built a terminal-based support triage agent using 774 Markdown documents as the only knowledge base [2]. A public repository separately advertises an evaluation report and a security evaluation report, but its snippet reports 1,773 participants [4], whereas the first-person page reports 12,885 registrations [1]. Those counts conflict, so this report does not use them to estimate competition odds.

The retrieved material also exposes an important research limitation. It confirms official winner pages or winner announcements for several events, but it does not expose enough detail for every named competition. Google exposes a Final 10 and Demo Day, SIH exposes winner counts and problem themes, AWS exposes the top three names, and Llama Seattle exposes a first-place team. By contrast, the retrieved Accenture page is a participation page [7], and the retrieved Adobe evidence is an older Creative Jam judging example rather than a verified 2024-2026 winner. The report therefore gives Team 511 a complete build strategy while marking gaps instead of presenting a fabricated 15-winner database.

## 1. Winner Anatomy: The Verified Cases And The Evidence Gaps

### 1.1 Comparison table: what is actually supported

| ID | Event and public URL | Problem and solution evidence | Stack evidence | Demo technique and judging mapping | Evidence status |
|---|---|---|---|---|---|
| 1 | HackerRank Orchestrate June 2026. http://hackerrank.com/hackerrank-orchestrate-june26. Supporting post: http://hackerrank.com/blog/behind-the-scenes-of-hackerrank-orchestrate | A 24-hour terminal support agent for HackerRank, Claude, and Visa; it handled support triage from 774 Markdown documents [1] [2]. | Terminal interface and Markdown corpus are verified. Exact language, model, vector store, and deployment stack are [UNVERIFIED]. | Live ticket resolution and defense are [INFERRED] from the published evaluation dimensions: agent, handled tickets, tool direction, and live defense [3]. | [VERIFIED] winner claim and workflow; implementation details [UNVERIFIED]. |
| 2 | HackerRank Orchestrate June public implementation evidence. https://github.com/GodVilan/HackerRank-Orchestrate-June-2026 | The repository is associated with the June event and advertises a full evaluation report and security evaluation report [4]. | Repository-level stack details were not exposed in the retrieved excerpt. | Evaluation and security evidence suggest that a measurable, testable demo mattered, but that causal claim is [INFERRED]. | [VERIFIED] public repo and reports; winner identity linkage [UNVERIFIED]. |
| 3 | Google Solution Challenge 2024 Final 10. https://developers.google.com/community/gdsc-solution-challenge/winners | Google says the Final 10 teams presented projects during a live Demo Day on June 27, 2024 [8]. The resources page frames the work around UN Sustainable Development Goals and a sample solution [15]. | Exact project stacks and individual repositories were not exposed in the retrieved excerpt. | Live presentation is [VERIFIED]; a concise before/after user story is the [INFERRED] demo lesson. | [VERIFIED] finalist cohort; not individually documented as a winner in the available excerpt. |
| 4 | Smart India Hackathon 2024 D. J. Sanghvi record. https://www.djsce.ac.in/docs/SIH%20GRAND%20FINALE%202024.pdf | The record says five software teams and one hardware team from D. J. Sanghvi College were declared winners at different nodal centres [5]. | Project-specific stacks, repos, and problem statements are [UNVERIFIED] from the available excerpt. | Winning count is verified; demo and judging reasons are [UNVERIFIED]. | [VERIFIED] winner count; [UNVERIFIED] individual case details. |
| 5 | Smart India Hackathon 2025. https://sih.gov.in/sih2025 | The official page highlights drones and robots for medical emergencies and search and rescue [13]. Reporting on the 2025 winners names renewable energy, disaster management, and smart education as winner themes [14]. | Individual winner stacks and repos are [UNVERIFIED]. | The evidence favors a clearly bounded national use case; the exact judging score is [UNVERIFIED]. | [VERIFIED] event themes and winner themes; individual build details [UNVERIFIED]. |
| 6 | Meta LlamaCon Hackathon winner announcement. https://ai.meta.com/blog/llamacon-hackathon | The official page is titled "Meet the winners of our first-ever LlamaCon Hackathon." The retrieved excerpt mentions Llama 4 multimodal image understanding, movement detection every five frames, and predefined events. | Llama 4 multimodal capability is [VERIFIED] from the excerpt; team names, repository, additional services, and exact placement are [UNVERIFIED]. | The likely winning move is observable event detection rather than a generic image chat, but this mapping is [INFERRED]. | [VERIFIED] winner page and capability excerpt; full case record [UNVERIFIED]. |
| 7 | Llama 4 Seattle Hackathon, Team Sussi. https://www.youtube.com/watch?v=9fk_h4dAfGA | The public video title and snippet identify Team Sussi as first-place winner and describe a solution for managing student technology use [9]. | Stack, repo, and model configuration are [UNVERIFIED]. | A first-place result plus a concrete student problem is verified; the claim that the demo won because it showed a visible user decision is [INFERRED]. | [VERIFIED] first place and problem direction; implementation details [UNVERIFIED]. |
| 8 | AWS AI Agent Global Hackathon, EcoLafaek. https://aws-agent-hackathon.devpost.com/updates/38140-congratulations-to-the-winners-of-the-aws-ai-agent-global-hackathon | The official Devpost update lists EcoLafaek as first place [16]. | Problem, stack, repo, and demo sequence were not exposed in the retrieved excerpt. | Placement is verified; why judges preferred it is [UNVERIFIED]. | [VERIFIED] first-place name only. |
| 9 | AWS AI Agent Global Hackathon, AegisAgent. https://aws-agent-hackathon.devpost.com/updates/38140-congratulations-to-the-winners-of-the-aws-ai-agent-global-hackathon | The same official update lists AegisAgent as second place [16]. | Problem, stack, repo, and demo sequence [UNVERIFIED]. | Placement is verified; judging rationale [UNVERIFIED]. | [VERIFIED] second-place name only. |
| 10 | AWS AI Agent Global Hackathon, Province. https://aws-agent-hackathon.devpost.com/updates/38140-congratulations-to-the-winners-of-the-aws-ai-agent-global-hackathon | The same official update lists Province as third place [16]. | Problem, stack, repo, and demo sequence [UNVERIFIED]. | Placement is verified; judging rationale [UNVERIFIED]. | [VERIFIED] third-place name only. |
| 11 | MongoDB AI Hackathon, Haven. https://github.com/topics/hackathon-winner | The retrieved GitHub topic excerpt calls Haven the winner of the international MongoDB AI Hackathon and describes discreet help, mental-health support, and legal guidance for women in abusive situations [10]. | The topic page does not expose the actual repository URL, dependencies, or model. | The problem is specific and high stakes; a safety-first, discreet demo is [INFERRED], not explicitly documented. | [VERIFIED] winner description; repo and judging details [UNVERIFIED]. |
| 12 | Microsoft AI Agents Hackathon 2025 winners page. https://microsoft.github.io/AI_Agents_Hackathon/winners | The page describes a free three-week event from April 8-30, 2025 with AI agent solutions and sessions on Semantic Kernel, AutoGen, Azure AI Agents SDK, and Microsoft 365 Copilot SDK [11]. | Frameworks were available to participants; the retrieved excerpt does not identify a particular winning build or its stack. | The event demonstrates that agentic workflows were an explicit 2025 competition category, not an accidental novelty [VERIFIED]. | [VERIFIED] event and winner page; named winner details [UNVERIFIED]. |
| 13 | Multimodal Evidence Review System. https://github.com/mehtarachit/hackerrank-orchestrate-june26 | A 24-hour submission reads conversations, inspects images through a pluggable VLM, checks user history, and returns severity, risk flags, and supporting evidence [12]. | Pluggable VLM and structured verdict are verified; exact providers and deployment are [UNVERIFIED]. | The evidence panel and risk flags make a strong safety demo, but winning status is not established. | [VERIFIED] public submission design; [UNVERIFIED] winner status. |
| 14 | WhatsApp Notification Router. https://github.com/16A9DA/whatsapp-notification-router | The public repository describes OCR, speech recognition, semantic retrieval, deterministic rules, and LLM reasoning [17]. | Those capability layers are verified; package versions and hosting are [UNVERIFIED]. | A single message routed to a visible destination is a good demo unit; winning status is [UNVERIFIED]. | [VERIFIED] public submission and architecture; [UNVERIFIED] winner status. |
| 15 | Evidence-review prompt implementation. https://github.com/vidhanjain03/hackerrank-orchestrate-june26/tree/main/code | The prompt includes object-specific guidance, evidence requirements, and structured JSON output [18]. | Prompt and JSON contract are verified; full application stack is [UNVERIFIED]. | The JSON contract supports predictable judging and replay, but winner status is [UNVERIFIED]. | [VERIFIED] public implementation detail; [UNVERIFIED] winner status. |

**Table takeaway:** The verified winner-level evidence supports a clear pattern but not the claim that every named 2024-2026 competition has a public, reproducible repository. Team 511 should copy the behaviors that are repeatedly visible - bounded scope, a concrete user decision, inspectable evidence, and a practiced live story - while treating missing stack and score data as unknown.

### 1.2 Case study: HackerRank Orchestrate and the bounded support agent

The Orchestrate case is the closest match to Team 511's overnight format. The task was not "make a chatbot." It was to build a terminal support agent for three named organizations, use it to resolve actual tickets, direct coding tools, and then defend the result live [1] [3]. HackerRank's own account says the corpus contained 774 Markdown documents and was the only knowledge base [2]. That constraint is strategically important: the team could demonstrate grounded behavior against a finite world rather than claim universal intelligence.

The solution pattern is a bounded decision loop. A ticket arrives, the system identifies the organization and issue type, retrieves relevant documents, drafts a response, and gives the judge a way to inspect the result. The exact model and framework are not verified, so Team 511 should not copy a guessed stack. It should copy the boundary: a fixed corpus, a reproducible input fixture, a visible answer, and an evidence trail.

The published evaluation dimensions make the demo itself part of the product. A feature that cannot help the team show a resolved ticket, explain the agent's action, or survive a defense question has low value even if it is technically interesting. [INFERRED] For Team 511, the equivalent is a vertical slice that takes one problem input to one accepted recommendation with two supporting evidence records and one human approval gate.

The public evidence also teaches a documentation lesson. One first-person page reports 12,885 registrations [1], while a public June repository snippet reports 1,773 participants and points readers to evaluation and security reports [4]. These are not safely combinable. The team should log the exact metric definition and source in its own README: registrations, active participants, submissions, and finalists are different quantities.

### 1.3 Case study: LlamaCon and Llama 4 Seattle show two ways to make AI visible

The Meta LlamaCon winner announcement is a useful multimodal example. The retrieved excerpt describes Llama 4 image understanding, movement detection every five frames, and predefined events. That is a much stronger demo primitive than "upload an image and ask a question" because the judge can see a sequence, a detected event, and a resulting action. The exact team, repository, and scoring rationale remain [UNVERIFIED], so the safe lesson is the capability shape, not a fabricated stack.

Team Sussi provides a separate evidence point. The Llama 4 Seattle Hackathon result identifies the team as first place and describes a solution for managing student technology use [9]. The problem is easy to narrate: a student, parent, teacher, or administrator needs to understand and influence technology use. The page does not give enough information to claim whether the build used a database, a particular UI framework, or a specific agent protocol. What Team 511 can copy is the translation from a broad social concern to a visible intervention.

Together, the two cases suggest a design test: if the AI capability is removed, does the demo lose its central decision? For movement detection, yes. For managing technology use, the answer should be yes if the product presents a concrete intervention rather than a generic chat response. [INFERRED] A Team 511 multimodal feature should therefore produce a field, flag, ranking, or approval request that changes the next screen.

### 1.4 Case study: AWS winners and the danger of winner-name inflation

The AWS AI Agent Global Hackathon winner update verifies three placements: EcoLafaek first, AegisAgent second, and Province third [16]. That is useful evidence that the event published a ranked outcome and that agentic projects were evaluated competitively. It is not evidence of each project's problem, stack, latency, or demo structure. The project pages or repositories must be opened before anyone claims those details in a pitch deck.

This is a practical lesson for Team 511's own submission. A judge may ask, "What happens if the model is unavailable?" A project with only a name and a model call has no strong answer. A project with a fixture, a deterministic parser, a cached evidence store, and a manual approval path can still demonstrate the full decision even when one AI component fails. [INFERRED] The winning move is not to hide uncertainty; it is to isolate it.

The same principle applies to the MongoDB AI Hackathon winner Haven. The available excerpt verifies a highly specific safety-oriented use case: discreet help, mental-health support, and legal guidance for women in abusive situations [10]. It does not verify the implementation. The use case nevertheless illustrates why impact is stronger when the audience, moment of need, and risk are explicit. Team 511 should write its problem statement as one operator or beneficiary moment, then show the decision that becomes safer, faster, or more accessible.

### 1.5 Case study: Google Solution Challenge and SIH reward alignment with a brief

Google Solution Challenge 2024 officially exposed a Final 10 and a live Demo Day on June 27, 2024 [8]. Its resources ask participants to research UN Sustainable Development Goals and provide a sample solution journey [15]. The retrieved evidence does not name the ten projects or prove that each one won a particular prize. It does prove that the event structure made a public, short presentation central.

SIH provides a different scale of evidence. The D. J. Sanghvi record verifies five software and one hardware winning teams in SIH 2024 [5]. SIH 2025 materials highlight drones and robots for medical emergencies and search and rescue [13], while reporting identifies renewable energy, disaster management, and smart education among winner themes [14]. The public excerpts do not identify the individual solution architectures.

The implication is that judging alignment must happen at two levels. At the event level, Team 511 should extract nouns from the problem statement: stakeholder, location, risk, output, and measurable benefit. At the demo level, it should show the exact output the evaluator can score. [INFERRED] If the brief asks for disaster response, do not demo a general assistant; demo one alert, one ranked action list, one evidence panel, and one escalation.

### 1.6 Case study: public submissions reveal the reusable implementation motifs

The public multimodal evidence-review repository is not verified as a winner, but it is highly useful engineering evidence. It describes a system that reads conversations, inspects submitted images through a pluggable VLM, checks user history, and produces a structured verdict with severity, risk flags, and supporting evidence [12]. That is almost a reference implementation for a safe hackathon demo: multiple inputs, one normalized case, a structured decision, and an explanation layer.

The WhatsApp notification router adds an important modality pattern. Its description combines OCR, speech recognition, semantic retrieval, deterministic rules, and LLM reasoning [17]. The evidence-review prompt repository adds the contract discipline: object-specific guidance, evidence requirements, and structured JSON output [18]. These are not proof of winning, but they show how to make an AI system testable under time pressure.

Swayam Mishra's public repository describes monthly HackerRank Orchestrate entries, with each month holding its own data, code, and README [19]. The August AGENTS file describes a message notification router and calls itself the single source of truth for many coding agents [20]. [INFERRED] The reusable lesson is to separate event data, domain rules, prompts, and code. Team 511 can then mount a new problem by replacing configuration and fixtures rather than rewriting the whole application.

## 2. What Winners Have In Common

### 2.1 Comparison table: behavior, mechanism, and Team 511 action

| Winning behavior | Evidence signal | Why it works under a 24-hour clock | Team 511 implementation |
|---|---|---|---|
| One end-to-end path | Orchestrate was evaluated on the agent and the tickets it actually handled [3]. | Judges can observe an outcome rather than trust architecture diagrams. | Implement `input -> decision -> evidence -> action` before adding a second workflow. |
| Finite knowledge boundary | Orchestrate used 774 Markdown documents as the only knowledge base [2]. | Retrieval quality and failure cases can be rehearsed. | Ship a local `data/` folder, source IDs, chunk text, and a no-network fallback. |
| Live presentation | Google Final 10 teams were scheduled for a live Demo Day [8]. | A live flow compresses product value into a memorable moment. | Record a 180-second script and rehearse the exact clicks. |
| Specific beneficiary | Sussi addressed student technology use [9]; Haven addressed discreet support and legal guidance [10]. | A concrete user makes impact and success criteria understandable. | Name the user, trigger, decision, and measurable output in the first 20 seconds. |
| Agent plus tools | The 2025 AI Agents Hackathon centered agent solutions and tool frameworks [11]. | Tool use demonstrates action, not just text generation. | Use one router/planner with 2-3 deterministic tools, not a multi-agent swarm. |
| Safety and evidence | Public evidence-review work exposes risk flags and supporting evidence [12]. | A judge can see why the system did not blindly act. | Add confidence, risk, source, and approval status to the main result card. |
| Structured output | The review prompt requires evidence and JSON [18]. | Deterministic fields make demos repeatable and tests fast. | Define a Pydantic-like JSON schema or plain JSON contract before prompts. |
| Modality with purpose | LlamaCon evidence mentions image movement detection; the router uses OCR and speech [17]. | A modality earns its cost when it opens a new signal. | Use multimodal input only for a high-value field such as damage, scene, receipt, or voice intent. |
| Scope and security | Opportunity Hack's rubric names Scope, Documentation, Polish, and Security [21]. | A small complete build beats a broad unfinished one. | Keep a scope card: in scope, out of scope, known failure, and recovery path. |

The mechanism is consistent: a judge has limited time and incomplete trust. A narrow system creates a smaller surface for failure, while evidence and structured output let the team explain the result. The recommendation is to optimize for observable reliability, not maximum model sophistication.

### 2.2 Scope discipline: the zero-dependency rule

The phrase "zero-dependency" should be interpreted operationally, not literally. Team 511 can use dependencies, but the demo must not depend on an untested network call, a model endpoint that may rate-limit, a database migration that has not been rehearsed, or an external document that may disappear. [INFERRED] The winning overnight scaffold should have zero *uncontrolled* dependencies.

Use three execution modes. `LIVE` calls the chosen model and services. `CACHED` replays a recorded response for a known fixture while preserving the same UI and evidence format. `OFFLINE` uses deterministic rules and local data to prove the workflow. Put a small mode indicator on the screen. A judge is more likely to trust a candid fallback than a frozen demo that pretends a failed API call succeeded.

The 774-document Orchestrate boundary is a useful model for local reproducibility [2]. Team 511 should package a small problem fixture with 8-20 representative records, including one normal case, one ambiguous case, one adversarial or unsafe case, and one empty-result case. Every extracted field should carry `source_id`, `source_span` or quote, `confidence`, and `timestamp` if time matters.

### 2.3 Storytelling: the judge should see the decision before the architecture

The first screen should not be a landing page, a logo animation, or a model leaderboard. It should show the input and the pending decision. Then the system should transform the input in three visible steps: what it found, what it recommends, and what evidence supports that recommendation. The public Google Demo Day format [8] and Orchestrate defense model [3] both support a demo-first interpretation.

A strong story has a tension: manual triage is slow, evidence is scattered, safety is uncertain, or an operator must choose among competing actions. The system resolves one case. The team then shows a second case that triggers a guardrail. This contrast proves that the system is not just a text generator; it has a policy.

[INFERRED] Team 511 should give each feature a sentence in the form: "Because the input contains X, the system does Y, but it refuses or escalates when Z." That sentence is a compact mechanism explanation. It also answers the likely judge question, "Why is this AI and not a normal form?" The answer should point to extraction, ranking, ambiguity resolution, or multimodal interpretation, while deterministic policy controls the final action.

## 3. The Reusable Scaffold: A Domain Adapter Around A Stable Decision Pipeline

### 3.1 Architecture for mounting a new problem in under one hour

The scaffold should have a stable core and a replaceable adapter. The stable core owns input normalization, evidence records, retrieval, ranking, structured extraction, safety checks, audit logging, and the result UI. The adapter owns the problem nouns: which fields to extract, which actions are allowed, which evidence counts, and which escalation rules apply.

```text
                    +-----------------------------+
                    |  Web or terminal interface  |
                    |  input / result / evidence  |
                    +--------------+--------------+
                                   |
                         Case envelope and assets
                                   |
                    +--------------v--------------+
                    |  Domain adapter              |
                    |  schema, prompts, policies   |
                    +--------------+--------------+
                                   |
              +--------------------v--------------------+
              | Normalize and ingest                    |
              | text, image, audio, csv, URLs, forms   |
              +--------------------+--------------------+
                                   |
              +--------------------v--------------------+
              | Deduplicate and index                   |
              | hashes, canonical fields, chunks       |
              +--------------------+--------------------+
                                   |
              +--------------------v--------------------+
              | Retrieve and rank                       |
              | keyword / embeddings / recency / risk  |
              +--------------------+--------------------+
                                   |
              +--------------------v--------------------+
              | Extract and reason                      |
              | JSON fields, summary, deadlines, plan  |
              +--------------------+--------------------+
                                   |
              +--------------------v--------------------+
              | Policy and approval gate                |
              | confidence, risk, allowed action        |
              +--------------------+--------------------+
                                   |
              +--------------------v--------------------+
              | Evidence panel and audit log            |
              | sources, quotes, decisions, overrides   |
              +-----------------------------------------+
```

The architecture is a design target for reuse across roughly 90% of AI-themed problem shapes, not a measured statistic. `[INFERRED]` The repeated components are reusable because most overnight AI problems still require some combination of intake, extraction, prioritization, explanation, and action. The domain adapter prevents the team from hard-coding a disaster workflow into a student-support workflow.

### 3.2 The case envelope and evidence contract

Define the case envelope before choosing a model. A minimal record can look like this:

```json
{
  "case_id": "demo-001",
  "domain": "replace-after-problem-drop",
  "inputs": [{"kind": "text", "uri": "fixture://case-001"}],
  "entities": [],
  "facts": [],
  "ranked_actions": [],
  "deadlines": [],
  "risk_flags": [],
  "approval": {"required": true, "status": "pending"},
  "evidence": [],
  "audit": []
}
```

Every evidence item should contain `evidence_id`, `source_id`, `source_uri`, `quote`, `field`, `confidence`, and `used_for`. A generated statement without an evidence item is not allowed to appear as a verified fact. This is a direct implementation of the evidence and structured-output motif visible in the public review prompt [18] and the multimodal review submission [12].

Every action should contain `action_id`, `label`, `reason`, `required_evidence`, `risk_level`, and `requires_approval`. For example, "send message" and "recommend message" must be different actions. The UI should make the difference obvious. This lets Team 511 answer a safety question without adding a complicated safety subsystem at 04:00.

### 3.3 The eight reusable components requested by Team 511

**1. Ingestion.** Accept a normalized text field even when the source is an image, voice note, PDF, spreadsheet, or form. Store the original asset reference and the derived text separately. If OCR or speech fails, preserve the asset and show an extraction warning.

**2. Dedupe and canonicalization.** Hash exact files and normalize whitespace, phone numbers, IDs, dates, and case. For semantic duplicates, use a cheap similarity threshold only as a suggestion. Never silently delete a record in the demo; mark it as a duplicate of another record so the audit log remains explainable.

**3. Ranking.** Rank records, people, alerts, tasks, or actions using a transparent score. A simple score can combine relevance, urgency, risk, recency, and evidence completeness. Keep the score components visible in an expandable panel. This is more defensible than saying "the agent thought it was important."

**4. Summarization.** Produce a short operator summary with a fixed schema: situation, known facts, unknown facts, recommended next step, and evidence. Add a length limit. A concise summary is easier to test and pitch than a long answer.

**5. Deadline extraction.** Extract date, time, timezone, source quote, and confidence. Convert relative phrases such as "tomorrow" only when a reference date is known. If the date is ambiguous, generate a clarification request instead of inventing a deadline.

**6. Approval gates.** Separate low-risk recommendations from high-risk actions. A system may auto-label a document but should ask for confirmation before sending a message, escalating a safety case, changing a record, or committing a resource. The public evidence-review design's risk flags are a good visible pattern [12].

**7. Audit log.** Append events rather than overwriting them: input received, extraction completed, evidence selected, action recommended, human approved, action executed, and fallback used. A JSONL file is enough for a demo. Show two or three audit events in the pitch.

**8. Evidence panel.** For every result, show the source name, short quote, field supported, confidence, and whether a human approved the action. This panel is the bridge between RAG, provenance, and judge trust. The 774-document knowledge boundary in Orchestrate [2] makes this approach especially practical for a short competition.

### 3.4 Replaceable adapter examples

Keep adapter configuration in one file. A generic adapter might define:

```json
{
  "domain": "campus-response",
  "inputs": ["message", "image", "location"],
  "fields": ["issue_type", "severity", "deadline", "affected_people"],
  "rank_by": ["severity", "deadline", "evidence_completeness"],
  "actions": ["recommend", "request_more_info", "escalate"],
  "approval_for": ["escalate"],
  "required_evidence": ["source_quote", "confidence"]
}
```

If the prompt becomes a disaster-response problem, change `issue_type` to hazard type, `affected_people` to estimated impact, and the allowed actions to alert, route, or request confirmation. If it becomes an education problem, change the fields to learner need, resource, deadline, and intervention. If it becomes a financial or civic problem, add transaction or policy evidence and retain the approval gate.

The adapter should also carry a `demo_fixture` list. The team should not wait until the problem drop to discover that the UI requires five fields that the input does not contain. A fixture test must pass even when the model is disabled. `[INFERRED]` This is the fastest way to mount a novel problem without rewriting the core.

### 3.5 Recommended overnight stack and dependency policy

The exact stack should follow what Team 511 already knows. A pragmatic default is a small Python service, a local JSON or SQLite store, a simple browser UI, and one model provider behind an interface. A terminal UI is also defensible when the task is operational, as Orchestrate demonstrates [2]. Do not add a vector database, message queue, Kubernetes deployment, or multi-agent framework unless the problem explicitly requires it and the team has used it before.

Use a provider interface with three methods: `extract(case)`, `retrieve(query)`, and `draft(case, evidence)`. The default implementation calls the model. The cached implementation returns recorded JSON. The offline implementation uses keyword rules and fixture data. This design makes the model replaceable and lets the team keep developing after an API failure.

Preinstall dependencies before the contest, store credentials in environment variables, and create a one-command launch script. The launch script should validate the environment, load fixtures, start the service, and open the demo. The repository README should include a 60-second setup, a 60-second test, and a failure recovery command. Documentation is not decoration: Opportunity Hack's comparator rubric explicitly includes Documentation alongside Scope, Polish, and Security [21].

## 4. Team 511's 8.5-Hour Build Plan And 3-Minute Demo

### 4.1 Timeline from 21:30 drop to 06:00 submission

The supplied schedule leaves 8.5 hours between the 21:30 problem drop and the 06:00 submission close. The schedule below assumes a three-person team. If Team 511 has a different headcount, preserve the phases and assign ownership explicitly.

| Time | Product objective | Engineering output | Pitch evidence |
|---|---|---|---|
| 21:30-21:50 | Parse the brief and rubric | One-page scope card: user, input, decision, success metric, exclusions | A single sentence problem story |
| 21:50-22:20 | Freeze the domain adapter | Fields, actions, evidence requirements, approval rules | The exact output judges will see |
| 22:20-23:00 | Build the fixture path | Three representative inputs and one unsafe/ambiguous input | Known-good demo data |
| 23:00-00:30 | Ship the vertical slice | Input -> extraction -> ranking -> result -> evidence | First complete happy path |
| 00:30-01:30 | Add retrieval and citations | Local corpus, source IDs, quotes, confidence | Evidence panel |
| 01:30-02:15 | Add policy controls | Approval gate, risk flags, refusal or clarification path | Safety case |
| 02:15-03:00 | Add one high-value modality | OCR, image, audio, or structured file only if needed | Before/after modality moment |
| 03:00-03:45 | Add fallback modes | Cached and offline paths, visible mode badge | Recovery story |
| 03:45-04:30 | Test failure cases | Empty retrieval, malformed input, low confidence, API failure | Honest failure behavior |
| 04:30-05:15 | Polish the result screen | Clear labels, evidence drawer, action status, audit log | Screenshot-ready UI |
| 05:15-05:40 | Record and rehearse | 180-second script, backup screen recording, judge Q&A | Timed pitch |
| 05:40-06:00 | Freeze | Tag commit, export README, verify launch and submission | Reproducible artifact |

The main rule is a feature freeze at 03:45. After that point, work is allowed only if it improves reliability, evidence, or pitch clarity. A new model, a new agent, or a new UI route is not worth the risk unless it fixes the core path.

### 4.2 The 180-second demo script

**0:00-0:15 - Name the user and cost.** Say who receives the input, what is hard today, and what the system will decide. Avoid explaining the stack. The judge should know what success looks like before seeing the interface.

**0:15-0:35 - Show the raw input.** Use one realistic fixture. Highlight the field that requires interpretation: a deadline, a risk signal, an image detail, a conflicting record, or a long policy document. Do not begin with a blank chat box.

**0:35-1:20 - Run the hero path.** Let the system ingest, deduplicate, retrieve, extract, rank, and recommend. Keep the UI state changes visible. Narrate cause and effect: "This sentence produced this extracted deadline; these two sources raised the priority; the system recommends this action."

**1:20-1:55 - Open evidence.** Click exactly two sources. Show the quote, source ID, confidence, and the field it supports. If the system uses RAG, explain that the answer is bounded by the supplied corpus. If it uses an agent, show the tool call or plan step that changed the result.

**1:55-2:20 - Trigger the guardrail.** Use the ambiguous or high-risk fixture. Show a clarification request, a human approval gate, or a refusal. This is the moment that separates a useful system from a confident autocomplete.

**2:20-2:40 - Demonstrate fallback.** Toggle cached or offline mode and rerun the same case. Show that the workflow still renders, while being honest that the AI provider is unavailable. Never fake a successful live call.

**2:40-3:00 - Close with impact and next step.** State the measured demo result, the current boundary, and the first production extension. The close should be: "Today we prove X from Y evidence; next we would add Z after human review." It should not be a list of ten future features.

This structure maps directly to the observable behavior emphasized by Orchestrate's agent, ticket, tool-direction, and defense criteria [3]. It also respects the live presentation pattern visible in Google Solution Challenge [8].

### 4.3 Failure handling and judge questions

When a live demo fails, stop clicking randomly. Say what failed, switch to the cached fixture, and continue the same story. Keep the failed request ID in the audit log if possible. The judge should see that the system has a designed recovery path, not that the team has hidden a broken dependency.

Prepare short answers to these questions:

1. **Why AI?** Which field requires semantic extraction, ranking, multimodal interpretation, or ambiguity resolution?
2. **Why not a rule?** Which part is probabilistic, and which part remains deterministic because it is safety-critical?
3. **Where did the answer come from?** Show the source quote and evidence ID.
4. **What if the model is wrong?** Explain confidence, clarification, approval, and fallback.
5. **What is the smallest useful deployment?** Name one user, one workflow, one data source, and one measured outcome.
6. **How do you prevent prompt injection or unsafe instructions?** Separate untrusted input from system policy, restrict tools, validate structured output, and require approval for high-risk actions.
7. **What did you leave out?** State the exclusions from the scope card.
8. **What did each team member build?** Point to one visible module and one test or decision each person owns.

The strongest answer is a screen action, not a promise. For example, open the evidence panel for question three, toggle approval for question four, and show the exclusion list for question seven.

## 5. 2025-2026 AI Capabilities Judges Are Likely To Reward

### 5.1 Trend matrix: capability -> 24-hour MVP -> proof -> judge test

| Capability | Evidence signal | 24-hour MVP for Team 511 | What to show | Likely judge question and answer shape |
|---|---|---|---|---|
| Agentic workflow | The 2025 AI Agents Hackathon centered agent solutions and named Semantic Kernel, AutoGen, Azure AI Agents SDK, and Microsoft 365 Copilot SDK [11]. The Global Agent Hackathon description names agents, RAG, tool use, and multi-agent systems [22]. | One router chooses among two or three tools: search, extract, rank, notify, or ask for approval. | Show the input, selected tool, tool result, and final action. | "Why is this an agent?" Answer with a bounded decision policy and tool trace, not a claim of autonomy. |
| RAG with citations | Orchestrate used a finite 774-document corpus as the only knowledge base [2]. | Local documents, chunk IDs, keyword or embedding retrieval, top-3 evidence, answer schema. | Click from each generated field to a quote and source. | "Can it hallucinate?" Answer with no-evidence refusal, confidence, and human review. |
| Multimodal input | LlamaCon evidence mentions Llama 4 image understanding and movement detection; the WhatsApp router combines OCR and speech recognition [17]. | One image, audio, or document parser that produces a structured field used by the decision pipeline. | Show raw asset -> extracted signal -> changed ranking or action. | "Why not text?" Answer with the signal that is unavailable or less reliable in text. |
| Human-in-the-loop safety | The evidence-review submission returns severity, risk flags, and supporting evidence [12]. | Three states: auto-recommend, request clarification, require approval. | Trigger an unsafe or low-confidence case and show the gate. | "Who is accountable?" Answer with the approval record and audit event. |
| Provenance and audit | The review prompt calls for evidence and structured JSON [18]; Orchestrate's bounded corpus supplies a natural provenance boundary [2]. | Evidence IDs, source quotes, confidence, prompt version, model mode, and action log. | Expand the audit trail for one recommendation. | "Can you reproduce it?" Answer with case fixture, mode, source IDs, and schema version. |
| Structured extraction | Public submissions use object-specific guidance and structured JSON [18]. | Fixed fields for entities, deadlines, risks, actions, and missing information. | Compare raw input with extracted JSON and correction path. | "What happens on missing fields?" Answer with explicit `unknown` and clarification. |
| Social-impact specificity | Sussi focuses on student technology use [9], Haven on discreet support and legal guidance [10], and SIH themes include disaster and smart education [14]. | One beneficiary, one operator, one intervention, one metric. | Before/after scenario with a measurable time, safety, or access benefit. | "Who uses it tomorrow?" Answer with named user and first deployment boundary. |
| Security and documentation | Opportunity Hack's comparator rubric includes Scope, Documentation, Polish, and Security [21]. | README, threat assumptions, input sanitization, tool allowlist, and a visible scope card. | Open the README or security panel briefly, then return to the demo. | "What can go wrong?" Answer with an explicit failure case and mitigation. |

The late-2026 forecast in this matrix is an inference, not a guaranteed rubric. The evidence says that agents, multimodal understanding, evidence, and safety are prominent in the retrieved 2025-2026 material. It does not prove that every Craft N Code judge will award points for each capability. Team 511 should therefore select the capability that solves the dropped problem rather than adding a trend label for its own sake.

### 5.2 Agentic workflows: use a state machine, not a swarm

An overnight agent should be a visible state machine with optional model decisions. Suggested states are `RECEIVED`, `NORMALIZED`, `RETRIEVED`, `EXTRACTED`, `RANKED`, `PENDING_APPROVAL`, `COMPLETED`, `CLARIFICATION_REQUIRED`, and `FALLBACK`. The model may choose a tool or extract a field, but code owns valid transitions and allowed actions.

The 2025 AI Agents Hackathon and Global Agent Hackathon descriptions establish the direction toward agents, RAG, tool use, and multi-agent systems [11] [22]. They do not imply that a multi-agent system is optimal for eight hours of building. [INFERRED] A single controller with specialized functions gives Team 511 the same visible agentic story with fewer failure modes and a smaller prompt surface.

The hero demo should show one tool trace: "retrieve policy", "extract deadline", or "rank alerts." The judge should be able to understand why that tool was chosen. If the system invokes five hidden agents, the team will spend its pitch explaining architecture rather than value.

### 5.3 RAG with citations: make every important field inspectable

A minimum RAG MVP needs only a small corpus and a source-aware response. Split documents into chunks with stable IDs. Retrieve a small candidate set. Ask the model to return JSON in which each important field contains an evidence ID. Reject or downgrade any field with no supporting evidence. Show the top two quotes in the UI.

The Orchestrate knowledge boundary is the clearest evidence for this approach [2]. A finite corpus makes it possible to test retrieval manually and to build an answer that a judge can audit. The evidence-review prompt's requirement for evidence and structured JSON reinforces the same mechanism [18].

A judge may ask whether citations prove truth. The correct answer is no: citations prove where the system derived a statement, not that the source itself is correct. The product should distinguish `source_found`, `source_conflict`, and `human_verified`. That nuance is a stronger provenance story than a citation icon that implies certainty.

### 5.4 Multimodal input: one signal, one consequence

Use a modality when it creates a field that materially changes the result. Examples include OCR extracting a serial number, speech extracting a request, an image identifying visible damage, or video identifying a predefined motion. The Meta LlamaCon snippet's movement detection every five frames illustrates the useful shape: a stream becomes a concrete event [UNVERIFIED: full winner record not available in the retrieved excerpt]. The WhatsApp router confirms a practical combination of OCR and speech with retrieval and rules [17].

The MVP should not attempt full computer vision, continuous video analytics, and a conversational interface simultaneously. Pick one asset type and one output. Show the raw asset briefly, display the extracted signal, then show how the rank, flag, or action changed. If the modality does not change the action, remove it.

A judge may ask about false positives. Display confidence and offer a correction or approval action. For video or image cases, include a representative fixture and an intentionally ambiguous fixture. [INFERRED] A visible uncertainty path is more persuasive than an unsupported accuracy percentage measured on three hand-picked examples.

### 5.5 Human-in-the-loop safety and provenance

Safety should be a product state, not a paragraph in the README. Use a simple policy table:

| Risk condition | System behavior | Human action | Audit event |
|---|---|---|---|
| High confidence, low risk | Recommend or complete | Optional review | `completed` |
| Low confidence | Ask for missing information | User clarifies | `clarification_requested` |
| Conflicting evidence | Show both sources | Human chooses or escalates | `conflict_reviewed` |
| High impact action | Hold execution | Named approver confirms | `approval_granted` |
| Model or service failure | Use cached or offline result | User sees mode and limitation | `fallback_used` |

The multimodal evidence-review submission explicitly describes severity, risk flags, and supporting evidence [12]. The prompt repository describes evidence requirements and structured output [18]. Those public patterns support a compact safety architecture without requiring a large policy engine.

Provenance should include more than a URL. Record the input fixture, source IDs, extraction prompt version, model mode, retrieved evidence, decision, and approval. This makes the system reproducible during a judge question and gives Team 511 a strong answer to "what did you change after the model responded?"

## 6. Failure Modes, Counterevidence, And What Not To Copy

### 6.1 The public record is not the same as the leaderboard

The evidence shows a recurring mismatch between accessible winner announcements and accessible implementation details. AWS gives placements but not project internals in the retrieved excerpt [16]. SIH gives winner counts and broad themes but not the individual stacks in the available excerpts [5] [14]. Google gives a Final 10 and Demo Day but not the project details in the excerpt [8]. These are real sources, but they cannot support claims they do not state.

This is counterevidence against a simplistic research rule such as "the most starred repo won." Many winners may never publish code. Conversely, many public hackathon repositories are submissions rather than winners. The Mehtarachit, WhatsApp, and Vidhan repositories are valuable architecture evidence, but their winning status is not verified [12] [17] [18]. Team 511 should use the same label in its own portfolio: winner, finalist, submitted build, or reusable prototype.

### 6.2 The framework trap

The Microsoft event mentions several agent frameworks [11], and the Global Agent Hackathon mentions multi-agent systems [22]. That is evidence that frameworks are available and relevant, not evidence that a particular framework wins. A team that spends two hours migrating between agent libraries has created integration risk without improving the judge's observable outcome.

[INFERRED] Choose the simplest architecture that can render the evidence panel and recover from failure. A function call in Python can be an agent tool. A JSON route can be a workflow state. A single model can be a planner. The label matters less than the trace, policy, and result.

### 6.3 The generic chatbot trap

The strongest cases are not generic. Orchestrate names organizations, tickets, and a finite corpus [1] [2]. Sussi names student technology use [9]. Haven names a discreet and high-stakes support context [10]. SIH materials name emergency, search and rescue, renewable energy, disaster management, and smart education [14] [13].

A generic assistant can answer many questions but is difficult to score. A domain adapter can answer one important question with evidence and an action. Team 511 should reject any feature that cannot be tied to a user, trigger, output, or metric in the scope card.

### 6.4 The overclaiming trap

Avoid claims such as "90% reusable," "99% accurate," "production-ready," or "the judges chose it because of X" unless the source or a test supports them. In this report, 90% is explicitly a design target [INFERRED], not a measured result. Winner reasons are marked [UNVERIFIED] when the public page gives only a placement.

This discipline is itself a competitive advantage. A judge who asks about a missing repo, a failed API, or an unsupported statistic should receive a precise answer: "That is not yet verified; here is the boundary and here is how we would test it." The team can then redirect to the working evidence-backed path.

## 7. A Concrete Pre-Build Checklist For Team 511

### 7.1 Before August 15

1. Create the repository with `core/`, `adapters/`, `data/fixtures/`, `prompts/`, `ui/`, `tests/`, and `docs/`.
2. Implement the case envelope and evidence schema.
3. Implement three modes: live, cached, offline.
4. Build one generic result page with input, recommendation, evidence, risk, approval, and audit sections.
5. Add one fake adapter and at least four fixtures: happy path, missing data, conflicting evidence, and high-risk action.
6. Add a tool allowlist and structured-output validator.
7. Preinstall dependencies and test the one-command launch.
8. Record a 60-second screen capture of the scaffold before the problem drops.
9. Prepare a slide with blank slots for user, problem, evidence, output, and impact.
10. Assign roles: problem analyst and script owner, backend and evidence owner, UI and demo reliability owner.

### 7.2 After the problem drops

Write the problem in five lines: user, input, decision, evidence, and success metric. Then map each noun to the adapter. Do not begin with model selection. Select the model only after deciding which field requires language or multimodal interpretation.

Create the fixture before the full data pipeline. A fixture forces the team to decide what the demo result actually is. Then build the happy path, add evidence, add the guardrail, and only then add one optional modality. If the first complete path is not running by 00:30, cut features.

At 03:00, ask a teammate who did not build the feature to run the demo from the README. Every setup failure found at that point is more valuable than another feature. At 05:15, freeze the product and rehearse the three-minute story. A last-minute refactor is forbidden unless the current build cannot launch.

### 7.3 The final acceptance test

| Test | Pass condition |
|---|---|
| Launch | A new machine or clean environment starts with the documented command. |
| Happy path | One input produces a recommendation, evidence, and audit event. |
| Missing data | The system says unknown or asks for clarification; it does not invent. |
| Conflicting evidence | The UI shows conflict and prevents silent execution. |
| High-risk action | Approval is required and recorded. |
| Model failure | Cached or offline mode completes a truthful version of the flow. |
| Provenance | Every important output field points to a source or is labeled inferred. |
| Pitch | The team can complete the hero path in under 90 seconds and the full script in 180 seconds. |
| Scope | The README lists at least one explicit exclusion. |
| Ownership | Each team member can explain one module and one failure test. |

These tests operationalize the documented emphasis on handled tickets, live defense, security evaluation, evidence, and structured output [3] [4] [12] [18]. They also protect the team from the most common overnight failure: a technically impressive feature that cannot be demonstrated twice.

## Synthesis

### 8.1 Comparative analysis across five build philosophies

| Philosophy | Core mechanism | Scope | Trade-off | Best Team 511 adaptation |
|---|---|---|---|---|
| Orchestrate support triage | Bounded corpus plus terminal agent and live resolution | Narrow operational domain | Less generality, more reproducibility | Local evidence store, tool trace, ticket-like case workflow |
| Llama multimodal | Model interprets images or movement to produce an event | One high-value modality | More asset and model failure modes | One image/audio/video field that changes ranking or action |
| Social-impact intervention | Specific beneficiary and high-stakes user moment | Narrow but meaningful user story | Requires careful safety and impact language | Named user, guardrail, and measurable intervention |
| Agent framework display | Planner or agent calls tools and coordinates work | Potentially broad workflow | Framework complexity and hidden behavior | One controller, 2-3 tools, explicit state machine |
| Evidence-review implementation | Multimodal input, structured verdict, risk flags, evidence | Case-by-case decision | Requires schema and review UI | Universal case envelope, approval, audit, evidence panel |

The mechanisms differ, but the winning surface is similar. Orchestrate constrains knowledge, Llama makes a non-text signal visible, Sussi and Haven make the beneficiary concrete, agent competitions make tool use visible, and evidence-review builds make uncertainty visible. The common denominator is an observable decision with a defensible reason, not a particular model or framework [2] [10] [9] [11].

### 8.2 The non-obvious tension: breadth signals intelligence, narrowness wins the clock

Hackathon briefs reward ambition. SIH themes span emergency response, renewable energy, disaster management, and smart education [14] [13]. Agent hackathons advertise tool use, RAG, and even multi-agent systems [11] [22]. Yet the strongest rapid-build evidence points toward finite corpora, named tickets, one modality, and one visible action. The tension is not solved by choosing ambition or narrowness; it is solved by separating the vision from the proof.

Team 511 should pitch the broad outcome but demonstrate the narrow wedge. Say, "This can become an evidence-aware response layer for campus and civic workflows," then prove one case: ingest a message, extract the issue and deadline, rank the response, cite two sources, and ask for approval before escalation. The architecture can generalize; the demo should not.

### 8.3 The non-obvious tension: automation earns applause, control earns trust

Agentic workflows can look autonomous, but high-stakes cases such as Haven and evidence review require discretion, risk flags, or human judgment [10] [12]. A fully automatic demo may look fast but raises the judge's hardest question: who is accountable when the model is wrong? A system that pauses at the right moment can look less magical while being more credible.

The recommendation is a visible autonomy ladder: suggest, clarify, approve, execute. Let low-risk cases move quickly. Let uncertain or high-impact cases expose evidence and ask for a human. That mechanism gives Team 511 a better answer to safety questions and creates more demo moments without adding a second model.

### 8.4 The decision for Craft N Code 2026

Pre-build the scaffold, not a guessed solution. The core should accept text, image, audio, and structured records; normalize them into one case envelope; deduplicate; retrieve and rank; extract deadlines and entities; summarize; attach evidence; apply a policy gate; and append an audit event. The problem-specific adapter should be small enough to rewrite in the first 50 minutes after the drop.

At 21:30, choose one hero path and one guardrail path. At 00:30, have the hero path working. At 03:45, stop adding features. At 05:15, rehearse. At 10:00, show the input, the decision, the evidence, the approval boundary, and the recovery mode. This is the practical synthesis of the verified evidence and the team's 24-hour schedule.

The strongest claim Team 511 can make is also the safest: "We built a working, evidence-aware decision workflow for this exact problem, we can show why it produced this result, and we know what it does when the evidence or model is insufficient." That claim is narrower than "fully autonomous AI," but it is easier to prove in three minutes and easier for judges to remember.

## References

1. *http://hackerrank.com/hackerrank-orchestrate-june26*. http://hackerrank.com/hackerrank-orchestrate-june26
2. *http://hackerrank.com/blog/behind-the-scenes-of-hackerrank-orchestrate*. http://hackerrank.com/blog/behind-the-scenes-of-hackerrank-orchestrate
3. *http://hackerrank.com/hackerrank-orchestrate-august26*. http://hackerrank.com/hackerrank-orchestrate-august26
4. *http://github.com/GodVilan/HackerRank-Orchestrate-June-2026*. http://github.com/GodVilan/HackerRank-Orchestrate-June-2026
5. *SMART INDIA HACKATHON 2024 GRAND FINALE WINNERS*. https://www.djsce.ac.in/docs/SIH%20GRAND%20FINALE%202024.pdf
6. *Central Michigan University's Adobe Creative Jam Winners*. https://www.cmich.edu/research/cmu-library/library-services/academic-support/adobe-creative-campus/creativejamwinners
7. *Online Hackathon | HackerEarth developer event | AI Hackathon*. https://accenture-applied-intelligence-hackathon.hackerearth.com/
8. *GDSC Solution Challenge Winners | Google for Developers*. https://developers.google.com/community/gdsc-solution-challenge/winners
9. *Llama 4 Seattle Hackathon First Place Winner: Team Sussi*. https://www.youtube.com/watch?v=9fk_h4dAfGA
10. *hackathon-winner · GitHub Topics · GitHub*. https://github.com/topics/hackathon-winner
11. *Winners - AI Agents Hackathon 2025 - microsoft.github.io*. https://microsoft.github.io/AI_Agents_Hackathon/winners
12. *http://github.com/mehtarachit/hackerrank-orchestrate-june26/tree/main*. http://github.com/mehtarachit/hackerrank-orchestrate-june26/tree/main
13. *Smart India Hackathon 2025 - sih.gov.in*. https://sih.gov.in/sih2025
14. *Winners at Smart India Hackathon awarded - The Hindu*. https://www.thehindu.com/news/cities/Coimbatore/winners-at-smart-india-hackathon-awarded/article70391898.ece
15. *Solution Challenge Resources | Google for Developers*. https://developers.google.com/community/gdsc-solution-challenge/resources
16. *Congratulations to the Winners of the AWS AI Agent Global Hackathon!*. https://aws-agent-hackathon.devpost.com/updates/38140-congratulations-to-the-winners-of-the-aws-ai-agent-global-hackathon
17. *http://github.com/16A9DA/whatsapp-notification-router*. http://github.com/16A9DA/whatsapp-notification-router
18. *http://github.com/vidhanjain03/hackerrank-orchestrate-june26/tree/main/code*. http://github.com/vidhanjain03/hackerrank-orchestrate-june26/tree/main/code
19. *http://github.com/swayam-mishra/hackerrank-orchestrate*. http://github.com/swayam-mishra/hackerrank-orchestrate
20. *http://github.com/interviewstreet/hackerrank-orchestrate-august26/blob/main/AGENTS.md*. http://github.com/interviewstreet/hackerrank-orchestrate-august26/blob/main/AGENTS.md
21. *Hackathon Judging Criteria & Scorecard Template | Opportunity ...*. https://www.ohack.dev/hackathon-judging-criteria
22. *The Global Agent Hackathon - GitHub*. https://github.com/global-agent-hackathon/global-agent-hackathon-may-2025
