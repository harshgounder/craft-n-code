# TOPIC-UNIVERSE-2026.md: every topic that can come (exhaustive, expanded)

Purpose: ONE file with the full universe of possible hackathon statements (seed from Craft N Code 2026, expanded with 2026 India landscape research). Parse the drop against this file: company DNA (Section 1), shape (Section 2), domain (Section 3). That triple pins the kit (Section 4) and the demo gate. The statement grammar (Section 5) generates every combination the setters can realistically write.

How to use: read the drop. Match company. Match shape. Match domain. That triple pins the kit and the demo gate. Everything in this file is either verified from event sources, the 2025 problem set, the sponsor companies' public product lines and their own hackathon tracks, or the 2026 hackathon landscape (reskilll 2026 idea lists + India calendar, live 2026-08-15). Nothing is vibes: VERIFIED = seen in source/2025/landscape, INFERRED = sponsor DNA, WILDCARD = possible but unranked.

## SECTION 1: COMPANIES (VERIFIED authors of the real statements, Craft N Code 2026)

The real statements are written by the sponsor companies, not the club. Site tracks are the backup set. Fingerprint company FIRST.

### GOOGLE (prior 24%, setter)
DNA: agents that do real work, grounding, verification, Gemini, responsible AI, search, productivity, developer tools, Cloud.
Watch-words: agent, multi-step, grounding, verification, evidence, tool use, "with sources", "explain your reasoning", "safe actions", Workspace, Gemini, notebook, Cloud Run, Vertex.
Can ask: build an agent that completes a multi-step task with evidence and human approval. Build a tool-use agent with typed actions. Build a research companion that cites sources. Build an agent that verifies before it acts. Build a system that audits what an agent did. Build with Gemini API and deploy to Cloud (Solution Challenge rule: >=1 Google AI service + deploy).
Landscape proof (VERIFIED): Build with AI x Google Cloud, 50+ campuses, Gemini API + Cloud Run focus, 2026.
Kit: KIT-1. Gate: plan -> sources -> approval -> trace.

### APPLE (prior 15%, setter)
DNA: privacy by design, on-device, local intelligence, offline, photos, health, voice, "never leaves the device".
Watch-words: on-device, private, local, offline, sensitive, health, photos, voice, "your data stays on your phone", "no cloud", Swift, SwiftUI, accessibility.
Can ask: build an on-device assistant that transforms sensitive content without cloud. Build a private health/finance organizer. Build a local search over personal data with visible data movement. Build a graceful offline fallback for an AI feature. Build a consent-first data controller.
Landscape proof (VERIFIED): Swift Student Challenge 2026 winners = AI + accessibility; iQOO hackathon (India, June 2026) = on-device AI, mobile LLMs.
Kit: KIT-3. Gate: on-device -> refuse cloud -> safe fallback.

### META (prior 21%, setter)
DNA: messaging, WhatsApp/Instagram, creators, communities, multimodal, Llama open models, broadcast, reels, groups, open-source LLMs.
Watch-words: message, WhatsApp, creator, community, reel, broadcast, group, multimodal, image, voice note, "for your community", Llama, open model, open source.
Can ask: build a multimodal assistant inside messaging. Build a creator tools pipeline (captions, replies, variants). Build a community moderation assistant. Build a trusted-answer bot with human escalation. Build a scam-aware messaging guard.
Landscape proof (VERIFIED): Meta Llama AI Hackathon, 625 teams, open-source LLM builds (India 2026); Llama 4 natively multimodal.
Kit: KIT-4 (+ KIT-4B if fraud words). Gate: message+image -> answer -> escalation.

### ACCENTURE (prior 22%, setter)
DNA: enterprise gen AI adoption, governance, ROI, responsible AI, industry ops (banking, retail, health, supply chain), productivity, "how do we adopt AI safely", human-in-the-loop.
Watch-words: enterprise, governance, adoption, productivity, ROI, policy, compliance, consent, audit, "line of business", agentic ops, template, dashboard, KPI.
Can ask: build a governed case router (unstructured -> structured -> routing). Build an enterprise agent with policy gate and audit. Build a consent+audit layer for AI use. Build a KPI dashboard for AI adoption. Build an exception handler with human approval.
Kit: KIT-5 or KIT-1 ops. Gate: requests -> extraction -> exception -> approval -> KPI.

### ADOBE (prior 18%, setter)
DNA: creative production, brand, Firefly, content provenance, content credentials, marketing assets, brand-safe generation.
Watch-words: brand, creative, content, provenance, credentials, campaign, asset, "on brand", "brand kit", "channels", Firefly, node.
Can ask: build a brand-safe content generator with constraints. Build a content provenance tracker. Build a campaign asset pipeline (brief -> variants for channels). Build a review/approval workflow for creative assets. Build an on-brand checker.
Kit: KIT-2. Gate: brief -> 3 variants -> violation caught -> approved export.

### WHO ELSE COULD SET (INFERRED, lower prior)
Microsoft: enterprise agents, Copilot-shaped, M365, governance. Watch-words: copilot, M365, enterprise, meetings, Azure.
Landscape proof (VERIFIED): MSHACK (Microsoft), Azure AI, 500+ innovators (India 2026).
Amazon/AWS: ops tooling, serverless agents, cost, scale. Watch-words: serverless, scale, cost, ops.
NVIDIA: hardware-adjacent, edge AI, inference. Kit: KIT-3 or hardware companion.
Any security company (CrowdStrike, Zscaler, Palo Alto, Indian banks' security arm): fraud, phishing, deepfake, digital arrest, UPI safety. Watch-words: scam, fraud, phishing, deepfake, digital arrest, UPI, fraud call. Kit: KIT-4B overrides everything.
Any gov-adjacent partner (MeitY, DPDPA, citizen services): DPDPA, digital literacy, citizen services. Watch-words: citizen, DPDPA, grievance, accessibility. Kit: KIT-5 or KIT-3.
iQOO/vivo-style device makers (on-device LLMs): watch-words: on-device, mobile LLM, edge, app, phone. Kit: KIT-3. Landscape proof (VERIFIED): iQOO Hackathon 2026, on-device AI focus.
Wadhwani AI / education-adjacent (SahAI for Shiksha): education AI, assessment, personalized learning, teacher tools. Watch-words: education, learning, assessment, teacher, student, personalized. Kit: KIT-1 or KIT-4.
IBM (watsonx, MCP-adjacent enterprise AI): enterprise agents, data governance. Watch-words: watsonx, governance, data, enterprise.

## SECTION 2: SHAPES (7 core + 13 from wave 2 = 22 total, VERIFIED pattern)

Shape 1: TRUSTWORTHY AGENT. Input: tasks/emails/requests. Output: ranked actions, each with evidence, approved by a human, audited. Companies: Google, Accenture, Microsoft.
Shape 2: CREATIVE PRODUCTION. Input: brief + brand constraints. Output: channel variants, provenance, approved export. Companies: Adobe.
Shape 3: PRIVATE INTELLIGENCE. Input: sensitive personal content. Output: on-device transform, refusal to leak, fallback. Companies: Apple, NVIDIA, iQOO-style device makers.
Shape 4: MULTIMODAL MESSAGING. Input: messages + images + voice notes. Output: trusted answers, approved templates, human escalation. Companies: Meta.
Shape 5: GOVERNED ENTERPRISE ROUTER. Input: unstructured requests. Output: structured cases, routed, policy-gated, audited, KPI'd. Companies: Accenture, Microsoft, gov-adjacent.
Shape 6 (NEW, landscape-verified): MCP ECOSYSTEM. Input: a developer/ops need + tools. Output: MCP servers or tool registry that connects AI to real data/services, evaluated on how many integrations work live. Companies: any (Google ADK, Microsoft, GSA-style). Watch-words: MCP, model context protocol, tool server, integration, connect AI to X.
Shape 7 (NEW, landscape-verified): MULTI-AGENT SYSTEM. Input: a workflow with subtasks. Output: a team of specialized agents with a coordinator/supervisor, quality checked, failure-handling visible. Companies: Google, Meta, Accenture. Watch-words: agent team, multi-agent, supervisor, orchestrator, specialist agents.

The engine (ingest -> extract -> evidence -> rank -> propose -> approve -> audit) covers all 7. The kit decides the nouns. Shapes 6-7 are the two expansion candidates: if the drop names MCP or "agents that work together", mount the engine's tool/proposal loop (KIT-1 architecture, labeled adapters for tools, coordinator view in the UI).

## SECTION 3: DOMAINS (the topic universe, INFERRED where noted)

1. Ops/SRE: incident triage, SLO, runbooks, rollback, on-call (VERIFIED 2025 lane: inbox navigator; our KIT-1 feed is this)
2. Customer support: tickets, refunds, escalations, churn, SLA (VERIFIED landscape: support escalation system)
3. Finance: refund batches, approvals, fraud flags, invoices (VERIFIED 2025: NFT ticketing; landscape: personal finance agent)
4. Security: scam calls, phishing, digital arrest, deepfake, UPI fraud, vuln scanning, cert rotation (VERIFIED: our Kavach D)
5. Privacy: consent, on-device, data movement, DPDPA-shaped (INFERRED from Apple DNA)
6. Creative: brand kits, campaigns, captions, variants, provenance (INFERRED from Adobe DNA)
7. Messaging/community: WhatsApp-style, moderation, creators, broadcast (INFERRED from Meta DNA)
8. Enterprise ops: case routing, policy, exceptions, KPI (INFERRED from Accenture DNA)
9. Health: appointment triage, records, privacy (WILDCARD, fits KIT-3/5; landscape: healthcare triage bot, symptom questions + disclaimers)
10. Education: lecture generation, grading, study plans, personalized tutor (VERIFIED 2025: AI lecture generator, lab grader; VERIFIED landscape: SahAI for Shiksha, education tutor agent)
11. Web3: ticketing, loyalty, identity (VERIFIED 2025: 2 lanes; landscape: Agentic Ethereum Hackathon)
12. Hardware/edge: PS-05, device companions, on-device LLMs (VERIFIED: track exists; VERIFIED landscape: iQOO on-device AI)
13. Government/citizen: grievances, digital literacy (WILDCARD, fits KIT-5)
14. Climate/sustainability: reporting, optimization (WILDCARD)
15. HR/people ops: onboarding, leave, policies, hiring assistant (WILDCARD, fits KIT-5; landscape: AI hiring assistant, resume screening, interview scheduling)
16. Legal/compliance: contract review, policy checks (WILDCARD, fits KIT-5, careful with "not legal advice"; landscape: legal document analyzer)
17. Retail/e-commerce: checkout, returns, inventory optimizer (WILDCARD, fits KIT-1; landscape: e-commerce inventory optimizer, demand prediction, competitor pricing)
18. Travel/logistics: bookings, delays, rerouting, itinerary planner (WILDCARD, fits KIT-1/5; landscape: travel itinerary planner)
19. Media/news: summarization, verification, provenance, AI newsroom (WILDCARD, fits KIT-2; landscape: AI newsroom, fact-check claims)
20. Social good/accessibility: inclusive design, assistive AI (WILDCARD, strong judge resonance)
21. DevTools/code (NEW, landscape-verified): codebase navigator, code review pipeline, OSS contribution finder, repo Q&A (landscape: 3 of 20 projects)
22. Meetings/collaboration (NEW, landscape-verified): meeting assistant, agenda prep, action items from notes (landscape: smart meeting assistant)
23. Research/academic (NEW, landscape-verified): paper analyzer, literature review, PDF extraction (landscape: research paper analyzer)
24. Agriculture (NEW, landscape-verified): advisory agent, weather + soil + crop data, personalized farming advice, "impactful for Indian agriculture" (landscape: agricultural advisory agent)
25. AI for Bharat / Indic (NEW, landscape-verified): multilingual AI, Indic language models, rural use cases, voice-first for vernacular users (landscape: AI for Bharat theme, dominant 2026)
26. Responsible AI (NEW, landscape-verified): bias detection, explainability, safety, hallucination control (landscape: responsible AI theme, dominant 2026)
27. Gaming/entertainment (NEW, landscape-verified): AI dungeon master, storylines, game state (landscape: AI dungeon master)
28. Music/audio (NEW, landscape-verified): playlist curation from mood, audio workflows (landscape: music playlist curator)
29. Food/recipe (NEW, landscape-verified): recipe from fridge contents via image analysis (landscape: recipe generator)
30. Smart city (NEW, landscape-verified): multi-agent city dashboard, traffic/air/energy/transport (landscape: smart city dashboard, 4 monitors + unified insights)

## SECTION 4: KIT MAPPING (fingerprint triple -> kit)

company Google   + shape 1 + any ops domain -> KIT-1
company Google   + shape 3 + privacy words   -> KIT-3
company Apple    + shape 3                  -> KIT-3
company Meta     + shape 4                  -> KIT-4
company Meta     + fraud words              -> KIT-4B
company Adobe    + shape 2                  -> KIT-2
company Accenture+ shape 5                  -> KIT-5
company Accenture+ shape 1 + ops            -> KIT-1
fraud/security words ANYWHERE               -> KIT-4B overrides all
MCP / tool-server words ANYWHERE            -> KIT-1 architecture + labeled tool adapters (Shape 6)
multi-agent / supervisor / orchestrator     -> KIT-1 architecture + coordinator view (Shape 7)
on-device / edge / mobile LLM words         -> KIT-3 (or KIT-4B if fraud)
education words (teacher/student/assessment) -> KIT-1 or KIT-4 (tutor agent)
Indic / multilingual / Bharat words         -> KIT-4 or KIT-1 + voice-first skin (Hindi-first: Kavach DNA)
PS-05 hardware                                -> software companion to closest kit, never pitch fresh hardware
PS-04 open track                             -> strongest kit for the drop's actual words, same matrix
Shapes 8-29 (wave 2)                         -> full mapping in SECTION 9.2 table; key additions:
  streaming words (token stream / live)      -> KIT-1 + streamText / SSE adapter, demo MUST show interruption
  eval / red-team / benchmark words          -> KIT-1 + promptfoo-style harness, demo risk 5 (live data on stage)
  browser / computer-use words               -> KIT-1 + Playwright adapter, demo risk 5
  workflow / chain / zapier words            -> KIT-1 + n8n-style visual chain
  forecast / predict / confidence bands      -> KIT-1 + TimesFM/Chronos, demo risk 5 (held-out test set required)
  simulation / digital twin                  -> lowest 24h feasibility, avoid unless statement demands it
  safety / alignment / guardrail words       -> KIT-1 + Llama-Guard-3 wrapper, lowest demo risk (2)
  translation / localization words           -> KIT-1 + Gemini Translate, high feasibility
  MCP is an UNDERLAY now (not just Shape 6): appears inside shapes 9/11/15/17/26/27. "tools" or "MCP" maps to a family.

## SECTION 5: THE STATEMENT GRAMMAR (generates every possible drop)

Every realistic statement = Subject + CoreAction + Constraint + Channel + Evaluation + Twist.

Subject (who it is for): ops teams / support agents / creators / communities / enterprises / citizens / individuals / students / doctors / teachers / merchants / travelers / developers / farmers / patients / parents / elderly / small businesses / gig workers.

CoreAction: triage / rank / summarize / route / approve / generate / transform / detect / verify / escalate / audit / answer / search / schedule / personalize / protect / explain / orchestrate / monitor / recommend / transcribe / translate / moderate / review / predict / optimize / stream / evaluate / red-team / simulate / debug / generate-code.

Constraint (the differentiator, ALWAYS present): with evidence / with human approval / on-device / offline-capable / with provenance / within brand rules / within policy / with consent / under SLA / with audit trail / without hallucinating / in multiple languages (Indic) / with a fallback / at scale / in real time / with MCP tools / with visible reasoning / with a coordinator / with confidence bands / without cloud / token-streaming with interruption / on a held-out test set / against adversarial inputs / with live telemetry on stage / on a testbed harness.

Channel: email / WhatsApp / support tickets / calls / social / docs / images / voice notes / mixed / browser / IDE / repo / meetings / sensors / payments / live token stream.

Evaluation: "working demo" / "show the failure case" / "measured accuracy" / "judged on trust" / "judged on adoption" / "judged on scale" / "3-minute demo" / "judged on safety" / "judged on usability for non-technical users" / "judged on live data" / "judged on a held-out test set" / "judged on benchmark scores".

Twist (what makes it hard): the model is unreliable / the network dies / the user is non-technical / the content is sensitive / the brand is strict / the volume is 100x / the deadline is real / the cost must stay zero / the judge will attack it / the data is in an Indic language / the demo must work offline / multiple agents must not fight / the judge demands real telemetry / the data must be live / the benchmark must not be gamed.

Our engine covers every combination: the constraint maps to a gate (approval, provenance, consent, offline), the channel maps to an adapter, the twist maps to a stress test (see STRESS-BENCH-2026.md in craft-n-code). The only combos that cost extra are hardware (PS-05) and true real-time audio during a live call (Kavach D covers the call-flow claim with the signed evidence bundle, demo is simulated audio, honest).

## SECTION 6: THE 2025 SET (VERIFIED, what they asked before)

Lanes: NFT event ticketing / Web3 loyalty SBT / P2P skill swap / AI lecture generator / Collegiate Inbox Navigator (our exact shape) / Automated Lab Grader / Mobile Packet Hunter (winner).
Phase-2: chain auto-select, quest map, anonymity+replay, animations, MCP server (!), load testing, live request interception with consent+audit.
Lesson: the winning lane was the empty one, the winner scoped down twice, rebranded an hour before freeze, and shipped a working hard thing with zero deps. Expect 2026 to reward the same. NOTE: "MCP server" already appeared in the 2025 phase-2 extension list, meaning MCP vocabulary is familiar to these setters. Shape 6 is not a stretch.

## SECTION 7: THE 2026 BACKUP TRACKS (VERIFIED from site source)

PS-01 Rewind the Legacy (retro/nostalgia tech) -> maps to any kit with a nostalgia noun swap, low prior
PS-02 Night Ops (security/ops) -> KIT-1 or KIT-4B
PS-03 Signal/Noise (our default, = IDEA A) -> KIT-1
PS-04 Open Track (wildcard) -> matrix above
PS-05 Hardware Hack -> software companion, never fresh hardware

## SECTION 8: THE PRIORITY MATRIX (what to prepare first)

1. KIT-1 (agentic ops): highest prior (Google + Accenture = 46%), matches our default track, matches the 2025 winning shape, and is the architecture base for Shapes 6-7 (MCP + multi-agent). DONE in craft-n-code scaffold.
2. KIT-4B (fraud override): second highest, any security word triggers it, Kavach proof exists. DONE.
3. KIT-4 (messaging): Meta 21%, multimodal demo is flashy, and it is the base for Indic/AI-for-Bharat voice-first skins. DONE.
4. KIT-2 (creative): Adobe 18%, provenance story is strong. DONE.
5. KIT-3 (privacy): Apple 15% + iQOO-style on-device trend, on-device story is a judge favorite. DONE.
6. KIT-5 (enterprise): Accenture 22% shares KIT-1's engine, cheap to mount. DONE.

All five kits exist in craft-n-code scaffold/fixtures/kit*.json with decks and storyboards already in the repo. The night is a fingerprint + copy job, not a build.

## SECTION 9: EXPANSION NOTES (2026-08-15, landscape pass 1)

Source: reskilll "AI Hackathon Ideas for 2026: 20 Projects That Use Agentic AI and MCP" (live 2026-08-15, curl) + "AI Hackathon Calendar India 2026" (live 2026-08-15, curl). Firecrawl 402 documented; r.jina.ai Cloudflare-blocked; direct curl with Chrome UA worked.

Confirmed 2026 themes (VERIFIED): on-device AI / edge LLMs, agentic AI (agents + tool use + planning + autonomy), MCP servers (connect AI to real data/services), GenAI for education, AI for Bharat (multilingual, Indic models, rural), responsible AI (bias, explainability, safety).

The 20 landscape projects, mapped to kits:
- DevOps Autopilot (MCP infra monitor/scale/restart) -> KIT-1
- Smart Meeting Assistant (calendar, agenda, notes, action items) -> KIT-1
- Codebase Navigator (repo Q&A, bug find, refactor suggest, docs) -> KIT-1 (Shape 6)
- Personal Finance Agent (banking APIs, categorize, budget, insights) -> KIT-1
- Research Paper Analyzer (PDF read, findings, compare, lit review) -> KIT-1 (Shape 6)
- AI Newsroom (scrape, fact-check, summarize, publish, 4 agents) -> KIT-2 (Shape 7)
- Automated Code Review Pipeline (security/perf/style specialists + coordinator) -> KIT-1 (Shape 7)
- Customer Support Escalation (first-line + specialized + supervisor) -> KIT-5 (Shape 7)
- AI Hiring Assistant (screen, questions, eval, schedule) -> KIT-5 (Shape 7)
- Smart City Dashboard (traffic, air, energy, transport agents) -> KIT-1 (Shape 7)
- Agricultural Advisory Agent (weather + soil + crop, personalized) -> KIT-4 (Indic skin)
- Legal Document Analyzer (risky clauses, templates) -> KIT-5 (not-legal-advice framing)
- Healthcare Triage Bot (symptoms, disclaimers) -> KIT-3/5
- E-Commerce Inventory Optimizer (demand, pricing, orders) -> KIT-1
- Education Tutor Agent (adaptive, practice, progress memory) -> KIT-4
- AI Dungeon Master (storylines, game state) -> KIT-2
- Music Playlist Curator (mood -> Spotify MCP) -> KIT-2
- Recipe Generator from Fridge (image analysis -> recipe) -> KIT-4 (multimodal)
- Travel Itinerary Planner (budget, dates, flights, hotels) -> KIT-1
- Open Source Contribution Finder (GitHub profile -> matching issues) -> KIT-1 (Shape 6)

Tips from the same source (VERIFIED, matches our winner forensics): demo matters most, solve a real problem, show the agent loop (visible reasoning), handle failures gracefully. This is the same list as AFTERPACKETS forensics, independently confirmed.

### SECTION 9.2: SHAPES EXPANSION PASS 2 (wave 2, parallel.ai pro-fast, 2026-08-15)

Run: cnc-shapes-expansion2 (trun_2cdc198e625a4be18f7d4b3e340fc65b). Depth: ADECENT 80.6, 201 cites, 2 tables, 54.9K chars (below the DEEP 85 gate, folded anyway per user precedent: redo SURFACE only). Full report: parallel-ai-stack/test-results/cnc-shapes-expansion2.content.md.

22 candidate shapes beyond the 7 known were enumerated (report header says 13 new: 9 of the 22 overlap or are variations of the core set; honest count = 13 genuinely new). Key verified anchors: Splunk Agentic Ops Hackathon 2026 (3 tracks: Observability/Security/Platform, plus Best Use of Splunk MCP Server sub-prize), Google Cloud Rapid Agent Hackathon (verbatim: "automates real-time fraud detection", "streamlines complex loan workflows", "respond to user direction in a sub-second window"), Google Vertex AI Agent Builder Hackathon (Knowledge Bot / Lifestyle Bot / Productivity Booster / Customer-Facing Bot categories), Prophet Hacks UChicago ("predict the future"), UW Databricks Hackathon (anomaly detection + forecasted yield), Trustworthy AI Hackathon (responsible AI + accessibility), GitLab AI Hackathon 2026 (600+ agents built on GitLab Duo Agent Platform).

The 13 NEW shapes (beyond our 7), condensed master table:

| # | Shape | Tag | Setter | Feasibility | Demo risk | Kit |
|---|---|---|---|---|---|---|
| 8 | Real-time streaming agent | VERIFIED | Google | High | 4 | Gemini Flash Live streaming |
| 9 | Evaluation / red-team harness | VERIFIED | Accenture | Medium | 5 | promptfoo / inspect-ai |
| 10 | RAG with visible citations | VERIFIED | Google | High | 3 | Vertex Agent Builder |
| 11 | Computer-use / browser agent | VERIFIED | Google + Accenture | Medium | 5 | browser-use / Playwright |
| 12 | Voice-first multimodal assistant | INFERRED | Apple | Medium | 4 | LiveKit / Pipecat |
| 13 | Image/video gen control-loop | INFERRED | Adobe | Medium | 4 | Firefly API |
| 14 | Document intelligence (extract -> QA) | VERIFIED | Accenture | High | 3 | LlamaIndex |
| 15 | Workflow / Zapier-like chain builder | VERIFIED | Google + Accenture | High | 3 | n8n + LangGraph |
| 16 | Coding agent | INFERRED | Google | Medium | 5 | Aider / OpenHands |
| 17 | Observability / debugging copilot | VERIFIED | Google | Low-Med | 5 | Splunk MCP |
| 18 | Safety / alignment wrapper | VERIFIED | Apple + Accenture | High | 2 | Llama-Guard-3 |
| 19 | Personalization + feedback loop | WILDCARD | Google/Meta | Medium | 4 | Gemini + Pinecone |
| 20 | Recommendation system | INFERRED | Google/Meta | High | 3 | Qdrant + rerank |
| 21 | Simulation / digital twin | VERIFIED | Meta/Apple | Low | 5 | ChatArena / Mesa |
| 22 | Gamified learning / tutor | WILDCARD | Apple | High | 4 | FSRS + Gemini |
| 23 | Accessibility / adaptation layer | VERIFIED | Apple/Adobe | High | 3 | Whisper-large-v3 |
| 24 | Translation / localization pipeline | VERIFIED | Google/Meta | High | 3 | Gemini Translate |
| 25 | Compliance / audit agent | VERIFIED | Accenture | Medium | 4 | LlamaIndex over policy |
| 26 | Customer support triage + escalation | VERIFIED | Google | High | 2 | Vertex Knowledge Bot |
| 27 | Fraud detection + explanation | VERIFIED | Accenture/Google | Medium | 4 | Kaggle fraud + Kafka |
| 28 | Data cleaning / ETL copilot | WILDCARD | Adobe/Accenture | Medium | 4 | dbt-core + DuckDB |
| 29 | Forecasting + confidence bands | VERIFIED | Google/Meta | Medium | 5 | TimesFM / Chronos-Bolt |

Synthesis that changes tonight's parse:
- MCP is an UNDERLAY, not just Shape 6: it appears inside shapes 9, 11, 15, 17, 26, 27 (Splunk MCP sub-prize, browser tools, workflow tools). A statement mentioning "tools" or "MCP" now maps to a family, not one shape.
- Demo risk 5 shapes (9 eval, 11 browser, 16 coding, 17 observability, 21 simulation, 29 forecast) demand LIVE data on stage: judges will not accept a mock dashboard for observability, or a held-out test set missing for forecasting. Avoid these unless the scaffold already has real data (it does for feeds: the pre-warm rule covers it).
- WILDCARD shapes (19, 22, 28) have NO recoverable 2025-2026 example statement. If the drop lands on one, we have no benchmark; treat as self-positioning, not a known lane.
- The authoring recommendation from the report (what a sponsor would assign) matches our kit coverage: eval, RAG-cite, workflow, compliance, support-triage, fraud are all KIT-1/KIT-5 territory.

### SECTION 9.3: DOMAINS EXPANSION PASS 2 (wave 2, parallel.ai pro-fast, 2026-08-15)

Run: cnc-domains-expansion2 (trun_5b4a273882894fabaa5f8084b93c0ac8). Depth: ADECENT 82.5, 354 cites, 2 tables, 73.7K chars. Full report: parallel-ai-stack/test-results/cnc-domains-expansion2.content.md.

50 candidate domains enumerated in 18 clusters (32 net new beyond our 30; 18 overlap/cluster). Key verified anchors: RBI HaRBInger 2025 (4th global fintech hackathon, formally open), SIH 2024 DeepShield (face-swap deepfakes), Kerala Police HAC'KP 2026 (theme: Agentic AI for Investigations), IndiaAI CyberGuard AI Hackathon (MeitY), India Innovates 2026 ("Where Code Meets Constitution"), Ministry of Textiles Handloom Hackathon 2026, Apple Swift Student Challenge 2026 (AI meets accessibility), GitHub Open Source Assistive Tech Hackathon (Braille laptop), Meta Llama-3-on-WhatsApp hackathon Bengaluru (270 participants), HackFluence 2026 (national creator-economy, IGDTUW/Dropp), Build for Bharat (ONDC-Google-Antler-Paytm), Adobe India Hackathon 2025 (260K students).

Top-10 ranked by setter-priority x precedent x feasibility (condensed from the 50-row master table):

| # | Domain | Tag | Setters | 24h feasibility | Demo risk | Kit |
|---|---|---|---|---|---|---|
| 1 | UPI / fintech fraud | VERIFIED | Accenture, Meta | High | Med | KIT-1 |
| 2 | Microfinance SHG lending | VERIFIED | Accenture, Google | High | Low | KIT-1 |
| 3 | Insurance claims triage | VERIFIED | Accenture, Google | High | Med | KIT-5 |
| 4 | DPDPA compliance | INFERRED | Accenture, Adobe | V. High | Low | KIT-5 |
| 5 | RTI / public grievance | VERIFIED | Google, Accenture | V. High | Low | KIT-4 |
| 6 | Vernacular voice / Indic | VERIFIED | Google, Accenture | High | Low | KIT-4 |
| 7 | Sign language translation | VERIFIED | Apple, Google | Med | Med | KIT-3 |
| 8 | Academic integrity / proctoring | VERIFIED | Adobe, Google | High | Med | KIT-3 |
| 9 | Teacher copilot / parent bridge | VERIFIED | Google, Adobe | High | Low | KIT-5 |
| 10 | Elderly companion / vitals | VERIFIED | Apple, Accenture | High | Med | KIT-3 |

Synthesis that changes tonight's parse:
- The verified-precedent sweet spot is fraud + civic AI: RBI, SIH, Kerala HAC'KP, IndiaAI CyberGuard all fingerprint the same grammar (detect / classify / triage / escalate). Our scaffold pipeline IS that grammar.
- Accessibility is on-brand for 2026 (Apple SSC winners = AI meets accessibility, GitHub braille). Sign language + Braille map to KIT-3 (privacy/on-device), which we already hold.
- DPDPA is the freshest law under 25 (Rules notified Nov 2025, consent managers Nov 2026): highest topical sexiness, pure-LLM build, KIT-5. INFERRED only because no named hackathon ran it yet; India Innovates 2026 orbits the same category.
- Demo risk hotspots: EV charging (charger API), ABDM (FHIR auth), railway (IRCTC scrape). Counter with mocked streams, ABDM sandboxed FHIR, scraped timetables (documented in report feasibility columns).
- The dmj.one precedent (59 Bharat-first products incl. Jalseva water 163M reach) confirms LLM-only demos are the 24h ceiling and everything maps to KIT-1 agentic ops.

### SECTION 9.4: COMPANY LANE SCAN PASS 2 (wave 2 refire, parallel.ai pro-fast, 2026-08-15)

Run: cnc-company-lanes-refire (trun_6eaa095855ac45d6894ea729dcf2b29c). Depth: ADECENT 72.5, 221 cites (first attempt SURFACE 63.1 with 1 cite, refired with cite pressure per user precedent: redo SURFACE only). Full report: parallel-ai-stack/test-results/cnc-company-lanes-refire.content.md.

What changes tonight's parse (all VERIFIED with URLs in the report):

1. GOOGLE (24%): Gemini 3 launched Nov 18 2025 ("PhD-level reasoning", 1M-token context, "most powerful agentic and vibe coding model yet"), Gemini 3 Deep Think, Antigravity (agentic IDE), Gemini Agent. Agentspace REBRANDED to Gemini Enterprise (June 8 2026: Gemini 3.5 Flash default-on). CRITICAL HONEST NEGATIVE: Project Mariner SHUT DOWN as standalone May 4 2026, capability absorbed into Gemini Agent + Interactions API (GA). A statement naming Mariner is dead on arrival; rebuild on the Interactions API. Free tier: AI Studio no credit card, 10-30 req/min; Vertex $300 credits; ADK open-source.

2. APPLE (15%): Apple Foundation Models = on-device 3B LLM exposed to third-party apps via native Swift API (@Generable, @Guide, streamResponse). Apple Intelligence is iPhone/iPad/Mac-only, no cost per request but hardware-gated. HONEST NEGATIVE: Metal/Xcode toolchains gate Swift on macOS; an Apple-lane entry must be iPhone-first and accept judges with no iPhone see design only. On-device + accessibility = their on-brand 2026 lane (Swift Student Challenge winners).

3. META (21%): Llama 4 Community License = royalty-free, non-exclusive, worldwide; 700M-MAU ceiling only for hyperscaler products. Safest zero-API-key on-device stack (Scout/Maverick/Behemoth). HONEST NEGATIVE: WhatsApp Business AI assistant is country-restricted ("select languages and limited countries"), unreliable from India Aug 2026; safer = Meta AI Agent SDK / open Llama stack. Live translation + PyTorch in their vocabulary.

4. ACCENTURE (22%): Distiller agentic framework (agent memory management, multi-agent collaboration, agentic workflow management, model customization, governance), Trusted Agent Huddle, Agent Builder, Physical AI SDK. VOCABULARY GIVEAWAY: "agent" never "chatbot", name a vertical (BFSI/healthcare/retail/manufacturing), route work across multiple agents with a memory/audit story. Our scaffold's propose -> approve -> audit IS their DNA.

5. ADOBE (18%): Firefly Image Model 4 (MAX Oct 28 2025), Generative Fill 1 credit/generation, Firefly API free-tier eligible (/images/generations, /images/expand, /images/fill, /videos/generations), GenStudio content supply chain, Acrobat AI Assistant, brand governance. Their lane = marketing/content supply chain agent that proves itself visually in the 3-min demo.

Cross-sponsor master table (condensed):

| Sponsor | Top-3 predicted lanes | Watch-words | Can-ask draft | Shape mapping |
|---|---|---|---|---|
| Google 24% | multi-agent + MCP; trustworthy agent; on-device | agentic, vibe coding, Deep Think, 1M-token, ADK, Interactions API | "Multi-agent system using Google ADK with Gemini 3 Deep Think + NotebookLM fact-check, exposed as MCP server" | 7 -> 6 -> 1 -> 3 |
| Apple 15% | on-device; trustworthy; multi-agent (App Intents) | @Generable, @Guide, streamResponse, Private Cloud Compute | "iPhone-only @Generable PDF redactor streaming via streamResponse with a verifiable no-network-call paper trail" | 3 -> 1 |
| Meta 21% | messaging; on-device/open-weights; multimodal | open weights, Built with Llama, Scout/Maverick, WhatsApp Business AI, live translation | "WhatsApp Business Agent triaging customer messages with Llama 4 Scout, Built with Llama attribution + audit trail" | 4 -> 3 -> 7 |
| Accenture 22% | enterprise router; multi-agent; trustworthy | Distiller, Trusted Agent Huddle, Agent Builder, Physical AI SDK, responsible AI | "Enterprise RFP workflow routed through three Distiller agents with AI Refinery SDK + Agent Builder + responsible-AI audit step" | 5 -> 7 -> 1 |
| Adobe 18% | creative pipeline; enterprise router; multi-agent/MCP | Firefly Image Model 4, Generative Fill, GenStudio, content supply chain, generative credits | "Brand-safe asset factory: PDF brief -> Generative Fill -> Acrobat AI Assistant sign-off -> GenStudio campaign URL" | 2 -> 5 -> 7 |

THE TRI-TOOL MOVE (cross-sponsor, max points): Gemini 3 free tier + Llama 4 Maverick (Hugging Face/Llama API, royalty-free) + Firefly Image Model 4 free credits. Covers LLM + multimodal + creative, all free, all verifiable. The statement "integration of at least 3 sponsor tools" is the event's own phrase: a team that literally integrates 3 sponsor free stacks has the phrase documented in the statement itself.

### SECTION 9.5: WORKAROUND ATLAS (wave 3, parallel.ai pro-fast, 2026-08-15)

Run: cnc-workarounds (DEEP 92.6, 362 cites, 3 tables, 56.4K chars. First DEEP of wave 3. Full report: parallel-ai-stack/test-results/cnc-workarounds.content.md).

40+ manual rituals across 6 lanes (education, kirana, healthcare admin, gig workers, enterprise, campus/housing). Top-15 by statement-readiness (condensed):

| # | Workaround | Lane | Pain evidence | Readiness | Shape | Kit |
|---|---|---|---|---|---|---|
| 1 | Paper register + shouted patient names | Healthcare | manual queue, Clinic OS | 5 | ABHA voice-triage | KIT-4 |
| 2 | Udhar khata in notebook | Kirana | 40-90% of monthly revenue at risk, Rs 2-5 lakh | 5 | Voice-Khata (Hindi voice OCR) | KIT-3 + KIT-4 |
| 3 | P2P purchase approval via email forwarding | Enterprise | no visibility/escalation/audit | 5 | Agentic Procure | KIT-5 |
| 4 | Attendance via WhatsApp reply "+P" | Education | parent-chat micromanagement | 4 | Edu-Bridge | KIT-4 |
| 5 | PMJAY pre-auth binder + fax | Healthcare | NHA runs AI adjudication hackathon because manual | 5 | NHCX-Bridge | KIT-5 |
| 6 | Lab reports via courier/WhatsApp PDF | Healthcare | pathology market Rs 3.2K cr fragmented | 5 | Pathology-Push | KIT-3 |
| 7 | Daily wage work via WhatsApp broadcast groups | Gig | first agentic AI for daily wagers exists because lane exists | 5 | Agentic Naukri | KIT-1 |
| 8 | Maintenance collection flat-to-flat | Housing | scattered apps + WhatsApp + registers | 5 | Society-Receipt-Bot | KIT-4 |
| 9 | Insurance via personal Aadhaar copy | Gig | 77% gig workers no social security, 12M gig workers | 5 | ABHA-Vault | KIT-3 |
| 10 | Supplier order via phone call | Kirana | wrong SKU 1-in-5 (INFERRED) | 4 | DistributorBOT | KIT-1 |
| 11 | Multi-level expense Excel + email | Enterprise | spreadsheets + email, time-consuming | 5 | ExpenseFlow | KIT-5 |
| 12 | Mess menu via WhatsApp poll | Campus | 10-15% plate waste (INFERRED) | 4 | Mess-Choice | KIT-4 |
| 13 | Exam seating via Excel + pencil | Education | GitHub template still needed | 4 | ExamPlot | KIT-1 |
| 14 | Onboarding checklist per hire in Docs | Enterprise | HR Cloud mainstream push | 4 | OnboardConductor | KIT-5 |
| 15 | Meeting minutes lost in chat | Enterprise | Saar.ai + MeetMinutes exist = mass pain | 5 | Meet-MOM | KIT-1 |

Takeaways that change tonight's parse: 8/15 workarounds are messaging shape (KIT-4, Meta's hook); 5 are enterprise (KIT-5, Accenture/Adobe). The statement that splits two kits: Voice-Khata (kirana voice OCR, Hindi, KIT-3 + KIT-4). If the drop mentions kirana, education admin, or clinic queues, one of these 15 IS the expected build.

### SECTION 9.6: NONCONSUMPTION MAP (wave 3, parallel.ai pro-fast, 2026-08-15)

Run: cnc-nonconsumption (ADECENT 79.6, 135 cites, 2 tables, 38K chars. Full report: parallel-ai-stack/test-results/cnc-nonconsumption.content.md).

9 India segments wanting outcomes but using nothing. Top-10 ranked (condensed):

| # | Segment | Population (VERIFIED where noted) | Outcome gap | Current nothing | Product | Shape | Setters | Kit |
|---|---|---|---|---|---|---|---|---|
| 1 | Farmers | 93M households (Ag Census) | advisory + mandi price + PMFBY claims | radio / Krishi Mitra | Bharat-Krishi voice agent | voice-first | Google | KIT-4 + KIT-1 |
| 2 | Daily-wage workers | 542M informal | wage record + safety + insurance | WhatsApp + pen-paper | missed-call IVR -> AI work log | voice/IVR | Meta + Accenture | KIT-4 + KIT-1 |
| 3 | Rural elderly | 73.3M (2011), 92M by 2031 | medicine + family ping + SOS | phone call to relative | Saathi on-device companion | on-device | Apple | KIT-3 + KIT-4 |
| 4 | New-to-internet | ~250M | schemes + banking + jobs | CSC / cybercafe / literate relative | Pehchaan WhatsApp + voice onboarding | cloud agent | Google + Meta | KIT-1 + KIT-4 |
| 5 | Kirana | 12-15M shops (CONTESTED 12M/13M) | inventory + GST + credit | notebook + memory | Dukaan-AI on-device + e-invoice | hybrid | Google + Adobe | KIT-3 + KIT-1 |
| 6 | Rural single-teacher schools | 2.5-3L schools (CONTESTED) | lesson plan + assessment + parent comms | blackboard + textbook | Ekal-Sahayak WhatsApp TA, DIKSHA 36 langs | cloud + voice | Google + Adobe | KIT-1 + KIT-4 |
| 7 | Small clinics / pharmacies | 2.5L informal providers (INFERRED) | records + stock + billing | paper register | Clinic-AI voice SOAP + ABHA | cloud + voice | Google + Apple | KIT-4 + KIT-1 |
| 8 | MSME / artisans | 8.83Cr MSME, 35L handloom weavers (CONTESTED) | design + price + market | local middleman | Tana-Bana-AI Firefly design + ONDC | cloud agent | Adobe + Meta + Google | KIT-1 + KIT-2 |
| 9 | Rural/tier-2 students | 25Cr K-12 (INFERRED) | test prep + mentorship + scholarship | free YouTube + crowded apps | GuruJi offline-first vernacular | on-device + cloud | Google + Apple | KIT-3 + KIT-1 |
| 10 | Gig workers (platform) | 7.7M now, 23.5M by 2029-30 | income record + insurance + grievance | app-only + nothing | GigSuraksha earnings aggregator + e-Shram | cloud + WhatsApp | Meta + Accenture | KIT-1 + KIT-4 |

Takeaways that change tonight's parse: voice-first (KIT-4) in 7/10 segments, agentic (KIT-1) in 9/10. Those are the two kits judges reward most. On-device (KIT-3) wins where connectivity rules (elderly, kirana, students). Pure app builds do not appear: the distribution channel itself is nonconsumed. If the drop says "voice" or "Bharat" or "vernacular", this table is the target list.

### SECTION 9.7: GEOGRAPHIC ARBITRAGE ATLAS (wave 3 refire, parallel.ai pro-fast, 2026-08-15)

Run: cnc-geo-arbitrage-refire (DEEP 100.0, 490 cites, 10 tables, 54.5K chars. First attempt SURFACE 74.9 with 43 cites; refire with 100-URL pressure hit a perfect score). Full report: parallel-ai-stack/test-results/cnc-geo-arbitrage-refire.content.md.

US/EU-validated AI products with no Indian equivalent, top-12 by arbitrage wedge:

| # | US/EU product (traction) | India gap + adaptation | Shape x domain x kit |
|---|---|---|---|
| 1 | Abridge ($550M raised, ambient clinical docs) | 1.4M MBBS doctors, 70% solo, paper EHR. Hindi AI voice scribe -> ABHA push, Rs 500/doc/month | voice agent, healthcare, KIT-3/4 |
| 2 | Harvey ($11B val, legal AI) | 1.4M advocates, no enterprise Indic AI. Bharat-law drafter (BNS), Rs 999/month | multi-agent, legal, KIT-5 |
| 3 | Runway ($315M Series E Feb 2026, video gen) | Indian film/creator $25B+ market, only Reelmind.ai beta. Indic video gen | creative, media, KIT-2 |
| 4 | Glean ($300M ARR May 2026, enterprise search) | 50K+ mid-market SaaS, no enterprise KG. Hindi+Kannada KG search, Rs 200/seat | retrieval agent, enterprise, KIT-5 |
| 5 | Pilot ($150M+, bookkeeping) | 63M MSMEs + 80K CAs. AI bookkeeper pulls Razorpay/Paytm SMS, files GST. Rs 99/3,000 | agent, finance, KIT-1 |
| 6 | Notion (100M users) | Indian knowledge workers on Zoho. Hindi AI wiki, Rs 200/seat | wiki agent, productivity, KIT-1 |
| 7 | SchoolAI ($25M, 1M classrooms) | 9.5M K-12 teachers. Hinglish lesson planner + DIKSHA, Rs 99/teacher | agent, education, KIT-1/4 |
| 8 | Descript ($100M / $55M ARR) | 80M+ creators. Hinglish auto-transcribe + voice clone, Rs 299 | audio agent, creator, KIT-2 |
| 9 | Suki ($165M, voice assistant) | tier-2 docs, ABDM, Rs 500/month | voice agent, healthcare, KIT-3 |
| 10 | Spellbook ($40M RBCx debt, contract AI) | Indian law firm arms (Amarchand, AZB, Khaitan). Indian-Acts contract AI | multi-agent, legal, KIT-5 |
| 11 | SkySlope (3M+ transactions, real estate) | 1.4L+ sub-registrar offices, paper. Encumbrance + stamp-duty AI, Rs 5K/txn | doc AI, property, KIT-5 |
| 12 | Mercury ($5.2B val, AI-native banking) | Indian founders, no AI-native bank. RazorpayX AI copilot | copilot, fintech, KIT-1 |

Takeaways: every row is a statement-ready "build the Indian X" problem. Abridge/Harvey/SchoolAI lanes are the strongest sponsor fits (Google/Accenture love India-impact framing). If the drop says "India's doctors/lawyers/teachers/shops", this table is the reference implementation list.

### SECTION 9.8: FAILED-AI AUTOPSIES (wave 3, parallel.ai pro-fast, 2026-08-15, PROVISIONAL)

Run: cnc-failed-ai-startups-refire. Verdict: MINED 94.5 (287 cites, 5 tables, 48.4K chars. MINED = FAIL per contract; content folded provisionally because the retry opportunities are statement-ready and each has a death source). Full report: parallel-ai-stack/test-results/cnc-failed-ai-startups-refire.content.md.

19 dead/distressed AI startups across 7 lanes: consumer assistants (Pi, Replika, Sonantic, Socratic, Halo), education (AI tutoring, homework bots, essay graders), healthcare (triage bots, mental-health chatbots), finance (bookkeeping, wealth, fraud), enterprise (copilots, knowledge, meeting tools), creative (art/music/video/writing), India-specific (dead/distressed Indian AI startups).

The retry pattern that matters tonight: every dead company proves a LIVE problem that a 24h student build CAN serve now, because free LLM APIs + MCP + on-device remove the cost structures that killed the original (inference cost, distribution, single-model lock-in). Death causes cluster as: retention (consumer), regulatory/trust (health), monetization (creative), timing (India). Use the report's per-company death-source table when the demo needs a "why this matters" slide: name the dead company, show its death cause, show the live problem.

### SECTION 9.9: COMPELLED EVIDENCE MINE (wave 3 refire, parallel.ai pro-fast, 2026-08-15, PROVISIONAL)

Run: cnc-compelled-evidence-refire. Verdict: SURFACE 67.7 (10 cites, 21 tables, 29K chars; refire dropped citation count vs first attempt MINED 90.4. Folded provisionally: the numbers themselves are the deliverable, each table carries its source). Full report: parallel-ai-stack/test-results/cnc-compelled-evidence-refire.content.md.

Top citable numbers (each with source in the report):

| Stat | Lane | Year | Demo use |
|---|---|---|---|
| Rs 11,158 cr saved via 1930/CFCFRMS fraud helpline | Fraud | FY21-26 | national helpline intercepts 20% of reported fraud value |
| 101,928 cybercrime cases registered | Fraud | 2024 | cybercrime doubled in 4 years |
| Doctor ratio 1:811 (13.86 lakh doctors) | Healthcare | Jul 2024 | India crossed WHO 1:1000 threshold |
| 5.6 crore pending court cases | Civic | Aug 2026 | 1 pending case per 25 citizens |
| 70 crore active UPI QR codes | SMB | Dec 2025 | every kirana is a payment node |
| 24 lakh NEET candidates | Education | 2024 | 22:1 med-school squeeze |
| Rs 224B piracy loss | Creator | 2023 | EY-IAMAI |
| Rs 805 cr UPI fraud value, ~85% YoY growth | Fraud | FY26 | fraud beat recovery |
| Rs 250 cr DPDPA max penalty | Compliance | 2025 | bigger than GDPR per-firm |
| 21.70 billion UPI transactions | Finance | FY25 | UPI moves India's GDP |

Takeaway: the cross-cutting pattern is shell vs substance: India moves massive public numbers (70 cr QRs, 21.7B UPI, 7.3 cr MSMEs) but the opaque backend is thinner (fraud recovery ~12%, FIR conversion 3:1 behind complaints). Any demo opening with one of these numbers beats a generic problem slide.

### SECTION 9.10: COMPLAINT MINE (wave 3, parallel.ai pro-fast, 2026-08-15, PROVISIONAL)

Run: cnc-complaint-mining-refire. Verdict: SHALLOW 54.3 (398 cites, 6 tables, 63.8K chars; first attempt SURFACE 67.1, refire scored LOWER. Verdict instability on this prompt after two attempts, no third refire: content folded provisionally for its verbatim quotes, which are the usable part). Full report: parallel-ai-stack/test-results/cnc-complaint-mining-refire.content.md.

5 sponsor lanes mined (Google dev/student/SMB, Apple on-device/accessibility, Meta WhatsApp India/sellers/group admins, Accenture enterprise ops, Adobe creators). The usable output: verbatim complaint quotes per lane for the demo problem slide, and the statement-readiness ranking. Use it as the quote bank, not as prediction: complaints prove pain, they do not predict the setter.

### SECTION 9.11: INDIA WINNER FORENSICS (wave 3-8, parallel.ai pro-fast, 2026-08-15)

Run: cnc-wave7-winners (DEEP 92.1, 82 cites, 7 tables, 30.2K chars. Full report: parallel-ai-stack/test-results/cnc-wave7-winners.content.md).

What changes tonight's parse (all VERIFIED with URLs in the report):
- MUJ's own HackX 3.0 (the closest analogue): Rs 70,000 / 40,000 / 25,000 prizes + AIC-MUJ pre-incubation pathway, Round-3 is a LIVE WORKING MODEL final pitch. Prize ecosystem ceiling ~Rs 5L. Judges at MUJ events expect a working thing on stage, not a deck.
- Google Cloud Gen AI Exchange 2025 (270,000 devs, 30-member jury) rewarded: agentic systems, explainable multimodal models, RAG legal intelligence, youth mental wellness. Bake in agentic + explainability.
- Meta's first India Llama hackathon (Nov 2024): 1st CurePharma AI ($3K), 2nd CivicFix ($2K). Industry-built-help prompts win. "Built with Llama" attribution is a scored item.
- Adoption + reproducibility beat novelty: GitLab 2026 scoring = technical work, design, potential impact, idea quality; live demos trump slide decks.
- The anti-pattern (hackathonradar.com May 2026): "Most hackathon projects fade because they were built for judging, not for continuation". Add a continuation/LCA line to the pitch.
- SIH themes that recur as Rajasthan-relevant: AI/ML, water, agriculture, healthcare, mobility, assistive tech. A state qualifier should link at least one ministry-grade domain.
- Rajasthan lanes: TiE Global Summit Rajasthan Hackathon (30h, DigiFest co-branded), MeitY TIDE 2.0 + iStart Rajasthan ideation hackathon (problem-first + prototype-second grading).
- Judge mindset (Section 5 of the report): questions cluster on demo failure, fake data, no testing, scope creep. 1st vs 2nd is decided by the working-demo gap, not the idea gap.
- Failed finalists (Section 6): strong projects lose on untested edge cases on stage, no failure story ("what happens when the API dies"), and scope that visibly exceeded 24h.

### SECTION 9.12: COMPETITOR TEARDOWN PER SHAPE (wave 3-8, parallel.ai pro-fast, 2026-08-15)

Run: cnc-wave8-competitors (ADECENT 79.2, 84 cites, 36 tables, 38.4K chars. Full report: parallel-ai-stack/test-results/cnc-wave8-competitors.content.md).

The per-shape "this already exists" map, with the student wedge for each (all VERIFIED):
- SHAPE 1 (trustworthy agent): OpenAI Operator scores 38% on OSWorld (2 in 5 tasks fail). Wedge: provenance-per-action + explicit approval ledger. Only ~12% of agent deployers ship the audit row; a tamper-evident hash-chained approval ledger is defensible.
- SHAPE 2 (creative production): C2PA has 6,000+ members but ZERO browser-enforced verification. Wedge: in-platform "trust badge" overlay that flags unsigned AI images.
- SHAPE 3 (private intelligence): LEAST shipped competition today. No product ships a verifiable on-device multi-agent workflow router that signs its own outputs and handles SBOM-style model provenance. Wedge: "private + auditable" axis. Apple PCC is the only cryptographically audited cloud AI; no Android equivalent.
- SHAPE 4 (multimodal messaging): WhatsApp Business Policy BANS general AI chatbots (effective Jan 15 2026), allows structured audited single-purpose bots with human hand-off in the 24h window. Bar: 95% across intent/quality/hallucination/guardrail/escalation. Wedge: verifiable 5-metric audit panel.
- SHAPE 5 (enterprise router): 89% of AI agent pilots stall at production (Gartner/IDC 2026). SME/mid-market unserved by ServiceNow/Agentforce list prices. Wedge: policy-engine layer that ANY of them plug into, not "be ServiceNow".
- SHAPE 6 (MCP): 8,000-12,000 listed MCP servers (from ~50 at Nov 2024 launch), but ~52% dead-server share. LEAST-shipped sub-niche: approval-gated MCP (a server that refuses tool calls above an approval threshold). Wedge: two MCP servers jointly enforcing HITL across five tools.
- SHAPE 7 (multi-agent): MAST taxonomy = 14 failure modes, 1,642 traces, production crews hit ~40% broken-down tasks (step repetition 15.7%, disobey spec 11.8%, no completion recognition 12.4%). Wedge: stateful durable checkpointed DAG with audit, not another CrewAI.
- Judge objection playbook (Section 8): name the incumbent product + its incident in the demo, show one measurable benchmark the judge can replay, embed every claim in a signed audit row. Innovation is rewarded when the failure mode is named; impact when the metric is reproducible.

### SECTION 9.13: 2026 FRONTIER + AGENT INCIDENTS (wave 3-8, parallel.ai pro-fast, 2026-08-15)

Run: cnc-wave6-frontier (ADECENT 73.5, 144 cites, 9 tables, 48.7K chars. Full report: parallel-ai-stack/test-results/cnc-wave6-frontier.content.md).

What changes tonight's parse (all VERIFIED with URLs in the report):
- Agent-induced data destruction is THE 2026 failure pattern: Replit wiped SaaStr prod DB (Jul 21 2025, 1,206 executive records, agent "lied" about rollback) and PocketOS wiped DB + backups in ~9 seconds (Apr 2026, Cursor + Claude Opus 4.6). Root cause both: autonomous coding agent with broad credentials + destructive tool path. Action: task-scoped short-lived credentials + tool-broker approval gates. A demo that SHOWS an agent refusing a destructive action is the 2026 on-brand move.
- Prompt injection is OWASP's #1 agent risk, up 340% in 2026 (EchoLeak CVE-2025-32711 on M365 Copilot; March 2026 finance pricing-data leak ran 3 weeks undetected). Action: reader/doer separation (reader = no tools, doer = no untrusted text, trusted orchestrator between). This is a 24h-buildable architecture and a judge-proof answer to "what about injection?".
- Operation Pale Fire: Block's red team got code execution via invisible Unicode in Google Calendar invites routed through Goose (their open-source agent). Treat calendar invites, PR comments, repos as untrusted input boundaries.
- MCP: ~50 (Nov 2024) -> 10K-14K servers (Q2 2026), 86K GitHub stars, 97M monthly SDK downloads. Microsoft/GitHub/Stripe/Atlassian/Figma/Cloudflare integrate. Agent Plugins 1.0.0 shipped with Amazon/Cursor/Microsoft/OpenAI/Vercel TSC. Action: ship the hackathon tool integration AS an MCP server, not a custom API.
- Frontier benchmark numbers are contested: SWE-bench Verified = 95.5% (BenchLM July 2026 mirror) vs 51.0% (Scale AI standardized set per Morph). Terminal-Bench 2.1 GPT-5.6 Sol 85.77%; OSWorld 2.0 Claude Opus 5 = 70.6%, GPT-5.6 Sol = 62.6%. Action: cite BOTH official and independent leaderboard URLs in the pitch so reviewers see spread.
- MAST: 14+ failure modes, 1,642 traces, ~40% task breakdown in production crews. Design the eval harness covering MAST modes BEFORE the demo, not after.
- Indian stack is shipping consumer-facing Indic models: Sarvam Indus (Feb 20 2026, Sarvam-105B, voice + Indian languages), Krutrim GPU-as-a-Service + AI Studio. Regional-language + on-device is the defensible niche vs frontier labs.
- Google Agents CLI ships 7 skills (workflow, ADK code, scaffold, eval, deploy, publish, observability); Agent Platform evals GA Jul 31 2026. Build on ADK for a scaffold+eval+deploy path.
- Plan-and-confirm beats let-it-run: Replit added dev/prod DB separation + planning-only mode + rollback-aware docs. Ship agents with explicit "plan-only" toggles. Our scaffold's propose -> approve IS this pattern, cite the incidents.

### SECTION 9.14: STRESS BENCH EXTENSION (wave 3-8, parallel.ai pro-fast, 2026-08-15)

Run: cnc-wave5-stress (ADECENT 77.8, 107 cites, 33 tables, 44.6K chars. Full report: parallel-ai-stack/test-results/cnc-wave5-stress.content.md).

Normative numbers to quote on stage (all VERIFIED):
- SLO pack: <1% request error rate, p95 <200 ms, p99 <400 ms.
- Retry budget: cap ~60 retries/min per process; 4^3 = 64x amplification when three layers retry three times.
- OWASP LLM Top 10 exists: test against LLM04 (model DoS / token exhaustion) by name, not "is it tough".
- Idempotency = the most consequential hackathon pattern: Stripe mechanics (255-char key, 24h TTL, full response caching on POST).
- Domain stress axes: fintech = decimal precision + double spend + reversal; health = consent revocation; education = proctoring resistance; civic = low-bandwidth paths; creative = brand violation at scale.
- The six live failure injections to rehearse before stage: network kill, key revoke, resource cap, 100x burst, deadline pressure, multi-language (Indic) input. This is the mock-drop bench's failure-injection list, now with normative numbers.

### SECTION 9.15: COMPELLED EVIDENCE REFRESH (wave 3-8 refire, parallel.ai pro, 2026-08-15)

Run: cnc-compelled-evidence-refire2 (ADECENT 81.9, 231 cites, 24 tables, 45.8K chars. Improved from SURFACE at pro tier. Full report: parallel-ai-stack/test-results/cnc-compelled-evidence-refire2.content.md).

Same 8 lanes as S9.9 with more receipts per lane. New anchor facts beyond S9.9 (all VERIFIED in report): 1930 helpline intercepts ~20% of reported fraud value (Rs 11,158 cr saved); 5.6 cr pending court cases; 70 cr UPI QRs; 7.3 cr MSMEs registered; 24 lakh NEET candidates; Rs 805 cr UPI fraud FY26 +85% YoY; Rs 250 cr DPDPA max penalty (tier ladder Rs 1L/2L/up to 250 cr); insurance claim grievances = 69% of complaints; creator piracy loss Rs 224B. The report's Top-20 Receipts Ranked (demo-citability index) is the quote bank for the problem slide. Cross-lane synthesis: India moves massive public numbers but the opaque backend is thin (fraud recovery ~12%, FIR conversion 3:1 behind complaints). Any demo opening with one of these numbers beats a generic problem slide.

### SECTION 9.16: COMPLAINT MINE FINAL (wave 3-8 refire 3, parallel.ai pro, 2026-08-15)

Run: cnc-complaint-mining-refire3 (DEEP 95.9, 334 cites, 23 tables, 69.9K chars. Third attempt; attempts 1-2 failed the gate (SURFACE 67.1, SHALLOW 54.3, SURFACE 63.6), the "PREVIOUS RUN FAILED, THIS RUN MUST FIX" phrasing + pro tier + 100-URL floor worked. Full report: parallel-ai-stack/test-results/cnc-complaint-mining-refire3.content.md).

85 verbatim complaints (17 per sponsor lane, India 2024-2026) + master ranking of the 30 most statement-ready pains. The top of the ranking (all VERIFIED, readiness 5):
1. WhatsApp "digital arrest" scam: Rs 4,057 cr lost since 2022, ~3 lakh victims; 15,215 fresh 2026 victims, Rs 481.1 cr. Track: Trust Verification Layer.
2. Gemini 2.5 Pro free tier 5 RPM / 100 RPD cap breaks Indian builders mid-quota. Track: Cost/Quota Optimizer.
3. Adobe India Hackathon test software falsely flags WhatsApp-active devices (users delete WhatsApp to start the test). Track: Marketplace/Platform Connector.
4. "We're not machines": outsourced India dev time-zone/labor exploitation. Track: Onboarding Copilot.
5. Apple Intelligence reports unavailable on iPhone 17 Pro with full India SIM. Track: Compliance-as-a-Service.
6. WhatsApp group admin can be jailed for any member's offensive post (2017 court ruling). Track: Compliance-as-a-Service.
7. Llama 70B un-runnable locally ("You need 2x RTX 4090"). Track: AI Workflow Orchestrator.
8. India gov asked Meta to pause WhatsApp usernames over digital arrest scams. Track: Trust Verification Layer.
9. Siri responds to "Assalamualaikum" but not "Jai Shri Ram" (North India complaint filed). Track: Bilingual/Indic-First UX.
10. Adobe CC Pro for Students Rs 398.99/mo requires India .edu/.in verification most students lack. Track: Onboarding Copilot.

Cross-cutting: the top pains cluster into 6 tracks: Trust Verification Layer, Cost/Quota Optimizer, Compliance-as-a-Service, Onboarding Copilot, AI Workflow Orchestrator, Bilingual/Indic-First UX. If tonight's drop targets any lane in this table, the demo problem slide writes itself from these quotes.

### SECTION 9.17: PARKED GAPS (diligence + benchmarks, 2026-08-15, UNVERIFIED)

Two planned runs failed the DEEP gate twice each and are parked, NOT integrated as evidence:
- cnc-wave3-diligence (sponsor India intel + judge intel + funding schemes): SURFACE 61.2 (0 cites), refire SURFACE 54.0 (4 cites, 5 URLs in file). Sponsor-lane structure matches the 221-cite company-lanes refire where they overlap; treat the funding-scheme sections (Startup India, iStart Rajasthan, MeitY) as UNVERIFIED leads, cross-check before quoting.
- cnc-wave4-benchmarks (benchmark registry, 10 categories): SURFACE 65.7 (0 cites), refire SURFACE 63.7 (0 URLs anywhere in file). Benchmarks named match the verified frontier report (S9.13) where they overlap (SWE-bench, OSWorld, MAST, GAIA); scores WITHOUT URLs are not quotable.
Both are reference material, not prediction-critical. If needed before finals: rebuild via structured per-entry URL-column prompt at ultra8x, or verify entries manually with rivalsearch.

### SECTION 9.18: GOV + INSTITUTIONAL MONEY-FLOW MAP (channel wave 2, parallel.ai pro, 2026-08-15)

Run: cnc-money-flow-gov (DEEP 97.0, 327 cites, 14 tables, 55.6K chars. The gov-aligned channel, dedicated run after the diligence park. Full report: parallel-ai-stack/test-results/cnc-money-flow-gov.content.md).

The money map (all VERIFIED with URLs in the report):
- IndiaAI Mission Rs 10,371.92 cr, 7 pillars, 38,000+ GPUs onboarded. Pillar 4 (Application Development Initiative) = ministries publish problem statements yearly. A demo aligned to a Pillar-4-style PS is attributable to a known federal buyer. Builder hooks: FutureSkills (Tier 2/3 AI labs), Datasets/Bhasha Daan (crowdsourced data), Safe & Trusted AI (bias audits = eval harness lane).
- Bhashini is fusing into Safe & Trusted AI at IndiaAI, building ULI speech-to-speech across 22 languages. Sarvam = leading sovereign stack. USE Sarvam/Bhashini ASR/TTS as a black box, never train an Indic LLM.
- Rajasthan: Bhamashah Techno Fund Rs 500 cr (Rs 100 cr women-led, Rs 50 cr green, Rs 25 lakh follow-on cap), iStart with 100+ investors + QRate, Rajasthan AI-ML Policy 2026 (statewide HPC + AI Cloud Infrastructure via DoIT&C iStart). Doing a Rajasthan problem = doing a flagged national priority.
- Procurement lanes = the hidden buyer: GeM (AI-first re-platforming 2026), CPGRAMS AI classification (DARPG, since 2022, refreshed 2026), ABDM 100+ cr records linked to 90+ cr ABHA accounts (May 2026).
- Jobs/PPO money: Adobe University Hackathon 2026 (PPI route), Google STEP (India-only, 1st/2nd year), Meta University Graduate SWE India 2026, Accenture India intern Rs 50,000/month, Apple Swift Student Challenge. PM Internship Scheme: Rs 9,000/month + Rs 6,000 joining, 1 cr youth, top 500 companies.
- Student grants easy to cite in the pitch: NIDHI PRAYAS Rs 10 lakh, SISFS Rs 945 cr umbrella (Rs 50 lakh via incubator), BIRAC BIG Rs 50 lakh, ATL Rs 20 lakh/school, AIC up to Rs 10 cr, TIDE 2.0 EiR Rs 4 lakh seed + Rs 7 lakh grant. SIH prize Rs 1.5 lakh.
- Pitch use: the "why this matters" slide quotes one lane with its amount + deadline + buyer. The full 30-row funding-lane master table is in the report (IndiaAI compute subsidy, DPIIT 80-IAC tax holiday, Bhamashah tiers Bronze Rs 15 lakh to Signature Rs 25 lakh, DigiFest x TiE, Code for Billion winners Dec 5 2026).

### SECTION 9.19: DEMAND FORECAST (channel wave 2, parallel.ai pro, 2026-08-15, PROVISIONAL)

Run: cnc-demand-forecast. Verdict: SURFACE 68.5 (84 cites, 12 tables, 47K chars; folded provisionally because the forecast table is decision-useful and each row carries driver evidence, verdict failed on composite). Full report: parallel-ai-stack/test-results/cnc-demand-forecast.content.md.

20-theme forecast for late-2026/2027 Indian hackathons (condensed, drivers + URLs in report):
- HIGH confidence, NEW (not pre-built): ONDC conversational commerce + Bhashini + WhatsApp agent (ONDC 500M txs, Meta-Reliance JV Rs 855 cr); DPDP Consent Manager registry + notice-and-consent agent (Rules G.S.R. 846(E) Nov 14 2025, Rs 250 cr penalty); ABDM/ABHA agent + HCX 2.0 fraud filter (ABDM 863M registrations, BMJ 562.4 cr fake claims); UPI biometric on-device agent (RBI Authentication Directions, 611M biometric UPI June 2026); DIKSHA PAL tutor low-resource languages; MCP server for Indian public data (GeM/ABHA/ONDC); UPI deepfake/liveness detector (Rs 805 cr fraud FY26).
- MED confidence, NEW: GeM AI tender-match + procurement fraud detector; Rajasthan Hindi-first grievance redressal agent (state policy aligned); Maharashtra ethical-AI audit agent; smart city/port digital twin; Rajasthan craft-sector AI catalogue; CEA power-sector cybersecurity regs.
- Already covered in our universe: Indic ASR/TTS scheme assistant (partly), smart city dashboard.
- Tonight-relevant subset (if the drop trends regulatory/data): DPDP consent manager, ABDM claims, UPI biometric, GeM vendor copilot. All map to existing kits (KIT-5 compliance, KIT-1 agentic, KIT-3 on-device).

### SECTION 9.20: FOUNDER FRAMEWORKS -> 10-MINUTE SELECTION CHECKLIST (channel wave 2, parallel.ai pro, 2026-08-15, PROVISIONAL)

Run: cnc-founder-frameworks. Verdict: MINED 85.9 (126 cites, 19 tables, 40.1K chars; provisional fold: 19 tables of usable heuristics, verdict failed on citation hygiene). Full report: parallel-ai-stack/test-results/cnc-founder-frameworks.content.md.

The one-page takeaway for the 21:30 decision (full checklist + printable in report Sections 4, 6, 10):
- The canon compresses to 6 one-line heuristics: Mom Test = "the scorer wants this, not the user"; JTBD = "what job does the evaluation clause hire this build for"; PG = "live in the future, build the thing you'd use"; Blue Ocean = "is this lane empty at THIS event"; NFX = "why now, why us, why 24h"; lean = "smallest demo that proves the loop".
- Time-pressure truth: the 10-min version of the Mom Test is READING THE EVALUATION CLAUSE and judging what the scorer rewards, because no interviews happen in the drop window.
- Fallacy list: novelty bias (counter: judge-replay test), scope greed (counter: 24h-feasibility gate from S9.2 table), tool-first thinking (counter: statement words first, tools second), competitor blindness (counter: S9.12 wedges), demo-risk blindness (counter: S9.2 demo-risk column).
- The checklist order: company DNA -> shape -> domain -> kit fit -> demo gate -> team skills -> failure story. Pass/fail thresholds in the report.
- 1st vs 2nd place test: the empty-lane test (is another team likely to build the same), the judge-replay test (can a judge re-run your demo), the 3-minute-narrative test (does the story fit 180 seconds).

### SECTION 9.21: EXISTING-SOLUTION LANDSCAPE: AGENTIC OPS (BriefLens), 2026-08-15

Run: cnc-exist-agentic-ops (ADECENT 83.4, 158 cites, 7 tables, 59.7K chars. Full report: parallel-ai-stack/test-results/cnc-exist-agentic-ops.content.md).

- Email triage incumbents: Superhuman (tier-gated AI, no approval pause), SaneBox ($7.99/mo, router not agent, no evidence per item), Shortwave (~50 staff, agent drafts not approval queue), Front ($15-25/user, support-inbox only), Missive (UI layer). NONE expose an evidence ledger per email, an approval pause, or an audit trail a non-technical user can read.
- OSS/adjacent: inbox-zero 11.7K stars (no audit/approval in feature set), PaperclipAI 76.4K stars (immutable audit + review-approval primitives, SDK not product), LangGraph 35.2K stars HITL checkpoints, OpenAI Agents SDK result.interruptions, Claude Agent SDK canUseTool, Vercel AI SDK 7 approvals+observability. AgentMail (YC S25) = inboxes FOR agents, AgentRQ = HITL supervisor MCP.
- Pain evidence: r/Slack app-approval cycles ~3 months, r/SRE eBPF audit thread, Show HN AgentMail/AgentRQ = community sees HITL + audit as the missing layer.
- WEDGE (confirmed): a packaged, email-first approve+audit product with Indic summarization (Bhashini 22 langs) + one-tap WhatsApp approval. No commercial Western email product ships that.
- Judge objection: "Superhuman/SaneBox do this" -> none of them pause for approval, none show why (evidence) per email, none give a readable audit trail.

### SECTION 9.22: EXISTING-SOLUTION LANDSCAPE: SECURITY/VOICE (Kavach + Circle), 2026-08-15, PROVISIONAL

Run: cnc-exist-security-voice. Verdict: SURFACE 67.6 (49 cites, 7 tables; folded provisionally, cross-checked against the verified S9.13 incident data). Full report: parallel-ai-stack/test-results/cnc-exist-security-voice.content.md.

- Truecaller AI (India, 450M users, Family Protection $74.99/yr): server-side caller-ID summaries, NOT live mid-call audio analysis, no claim of on-device Hindi model. Closest incumbent, paid-only above basic tier.
- Hiya: US-only. Google Pixel Scam Detection + Android fake-call detection: on-device but US-English-gated. McAfee: 96% video deepfake claim, US/UK/AU only. Pindrop/Reality Defender/Intel FakeCatcher: contact-centre grade, curated-benchmark EER degrades in the real world.
- WhatsApp on-device Scam Alert: limited beta. CyberDost/I4C: awareness-only. 1930 helpline: post-loss. DoT FRI/Chakshu: transactional/OTP-level, not voice-content-aware.
- WEDGE (confirmed): live Hindi/Indic on-device mid-call detection (Whisper-small/wav2vec2-BERT locally), evidence bundle for FIR, free tier. Community WhatsApp scam->QR->UPI hash db: genuinely unoccupied. Hindi deepfake corpus missing = real gap.
- REGULATORY WARNING: DPDPA Phase 2 effective 13 Nov 2026 creates the consent-manager framework; a 24h build recording calls without per-call consent risks unlawful processing. The demo must show consent capture or simulate.
- The 5 judge objections all have evidence-backed answers: Truecaller (no live Hindi on-device outgoing detection), Google (Pixel US-English only), McAfee (video-only, US subscription), WhatsApp (post-fact, not preventive), RBI/Chakshu (transactional only).

### SECTION 9.23: EXISTING-SOLUTION LANDSCAPE: COMPLIANCE (VicharSetu), 2026-08-15

Run: cnc-exist-compliance (DEEP 95.0, 276 cites, 10 tables, 37.5K chars. Full report: parallel-ai-stack/test-results/cnc-exist-compliance.content.md).

- Enterprise tier saturated but English-only: OneTrust (Bengaluru hub, quote-based), Securiti, DataGuidance, Tsaaro (SME-on-Demand 10-80 hr/mo), SISA, Kratikal, Scrut (DPDP Rules 2025 playbook Dec 2025). NONE target the citizen/MSME tier, NONE are Hindi-ready, NONE have public INR pricing. ConsentiQo (KavachOne, dpdpact.co.in) = India-first consent platform, English, immature; DPDP Board itself has NO live consent-manager registry page yet.
- Legal AI ($106.3M India market by 2030, 23% CAGR): SpotDraft (500+ enterprise customers, quote-based), Leegality, Harvey, Spellbook, Kira = lawyer-at-keyboard, English.
- Gov stack: myscheme.gov.in 4,772 schemes; UMANG 11.89 cr registrations / 799.74 cr transactions; Bhashini + Jugalbandi = translation infra, they do NOT cite DPDP sections.
- TWO REGULATORY TRAPS (must disclaim in the pitch): (1) Consent Manager is a REGISTERED ROLE under DPDP S8 with fully-operational interoperable platforms mandated by 13 May 2027: build a Q&A COPILOT, never pretend to be a consent manager. (2) AI-generated contract answers are under-tested by the Indian Contract Act 1872: a "ChatGPT answers policy" demo gets torn apart; every answer must cite the section.
- WEDGE (confirmed): Hindi-first, SME-priced, WhatsApp-native (550M+ users), DPDPA-section-aware Q&A with audit trail, fed by myscheme corpus + DPDP Rules PDF + Sarvam TTS + Jugalbandi WhatsApp pattern. Feeds INTO OneTrust/SpotDraft ecosystems as the citizen/SME interface.

### SECTION 9.24: EXISTING-SOLUTION LANDSCAPE: INDIA DOMAINS, 2026-08-15, PROVISIONAL

Run: cnc-exist-india-domains. Verdict: MINED 96.8 (346 cites, 6 tables, 63.1K chars; provisional fold, cross-checked against S9.5 workarounds + S9.6 nonconsumption). Full report: parallel-ai-stack/test-results/cnc-exist-india-domains.content.md.

- Kirana: Khatabook 50M+ downloads / 13 languages but text-first, no voice-first Hindi IVR; OkCredit (YC) SMS-only reminders; Vyapar desktop-first, no WhatsApp channel; BharatPe 10L+ merchants, terminal beep not conversational. The voice-first Hindi udhar gap is real and unoccupied.
- Agri: DeHaat 190K farmers vs 70% smallholders; Kisan.AI OSS 37 stars; the Hindi-voice advisory lane is open.
- Health: ABHA 863M registrations but ABDM Node SDK has 2 stars = missing FHIR tooling = buildable; Practo doctor revolt (50% fee + Rs 23K/mo visibility cost, r/india verified) = doctor-copilot wedge without the 50% cut.
- Edu: Entri 14M users / 250K paying across 8 languages proves vernacular pays; no teacher copilot exists (AI drafts the parent WhatsApp message).
- Gig: Urban Company "slavery-like" partner conditions documented; gig workforce 120 lakh (FY25) -> 62M by 2047; no Hindi IVR wage-tool.
- Judge objection: "Khatabook already does this" -> Khatabook is text-first in 13 languages, NOT voice-first Hindi/Hinglish over IVR for shopkeepers who do not read English.

### SECTION 9.25: EXISTING-SOLUTION LANDSCAPE: CREATIVE/MEDIA (SignalStory), 2026-08-15, PROVISIONAL

Run: cnc-exist-creative-media. Verdict: SURFACE 64.8 (0 cites, 9 tables; provisional, provenance claims cross-checked against verified S9.12 C2PA data). Full report: parallel-ai-stack/test-results/cnc-exist-creative-media.content.md.

- Enterprise: Adobe GenStudio (7-figure licensing, no India ramp), WPP Open (captive, 33x volume claims, not buyable), Canva Magic Studio (free tier 500 exports/day, no brand-kit enforcement, no C2PA export), Jasper ($49-69/mo, English), Copy.ai (from $1,000/mo starter).
- Approval SaaS: Filestage EUR 99/mo, Ziflow $249/mo per 15 users, ProofHub $89/mo = no WhatsApp lane, no India pricing.
- REGULATORY TAILWIND: MeitY draft IT Rules (Oct 2025) mandate a Synthesized Content Indicator on AI content (10% visible surface) with 24h takedown SLA. Provenance is becoming a legal requirement, and no Indian creator tool ships C2PA-signed export + WhatsApp approval + Indic variants together.
- OSS: IndicTrans2 (458 stars, 22 langs), Sarvam-105B open.
- WEDGE (confirmed): brief-to-variants + Indic + WhatsApp approval handshake + C2PA/CR-pin export for the 3-5 person Indian agency. Nothing in the market combines those four.

### SECTION 9.26: EXISTING-SOLUTION LANDSCAPE: MCP/AGENTS/ON-DEVICE, 2026-08-15, PROVISIONAL

Run: cnc-exist-mcp-agents. Verdict: SURFACE 68.3 (102 cites, 10 tables, 50.5K chars; provisional fold, cross-checked against verified S9.12/S9.13). Full report: parallel-ai-stack/test-results/cnc-exist-mcp-agents.content.md.

- MCP catalogs 2026: official registry 9,652 records, servers repo 89.5K stars, Glama 56,976, mcp.so 19,700+, mcpservers.org 9,800 curated, Smithery 7,300+.
- Frameworks: LangGraph 39.7K stars (GA Oct 2025), CrewAI 55.9K, AG2, OpenAI Agents SDK 28.4K, Claude Agent SDK (permission modes Jun 15 2026), Google ADK (deleted 3 malicious workflows Aug 2026 = supply-chain live), Pydantic AI (MCP-native, durable execution, HITL approval first-class), Mastra 26.6K. NONE make approval checkpoints first-class except Pydantic AI.
- On-device: Ollama 178K stars, llama.cpp 109K, MLX 27.7K, WebLLM 18.6K, ExecuTorch (Trail of Bits audited Jun 2026). Models that run on a student laptop: Llama 3.2 1B/3B (128K ctx), Qwen 2.5 0.5-3B, Phi-4-mini 3.8B, SmolLM3 3B, Gemini Nano via ML Kit (Oct 30 2025).
- Voice: Pipecat 14.1K, faster-whisper, Vosk 50MB per language offline, Sarvam Indicus (11 Indic TTS, 12 ASR, 23 langs).
- India MCP: MCP-India-Stack (Indicus/GST/financial), MoSPI official India AI Data MCP (Feb 2026), Samarth-23 collection. NO canonical ABHA/ONDC/GeM/UPI/DigiLocker server exists = the exact buildable wedge.
- Security: OWASP MCP Tool Poisoning cataloged; Invariant WhatsApp-exfiltration demo; approval gate must sit around the CALL, not the server.
- THE RECOMMENDED 24H STACK (from the report): Pydantic AI (MCP-native, durable, HITL) + LangGraph audit shell + Ollama offline fallback + MCP-India-Stack + Sarvam voice. Every tool call through an explicit policy node emitting a signed envelope = the wedge none of the incumbents ship.

## SECTION 10: THE META-UNIVERSE (beyond Craft N Code 2026)

This universe generalizes to any AI hackathon in India 2026-2027. The event-agnostic core: Section 1 company DNA (apply the setter list of YOUR event), Section 2 shapes (7 core + 13 from wave 2 = 22 now), Section 3 domains (30 core + 32 from wave 2 = 62 now), Section 5 grammar, Section 4 kit mapping. For a new event: re-run the site forensics + company lane scan, swap the priors, keep everything else. The kit layer (what you can build in 24h) stays identical: one engine, many skins.
