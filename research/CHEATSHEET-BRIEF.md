# THE CHEATSHEET BRIEF — what matters most, what the sponsors make/look for, hottest tech

Compiled: 2026-08-14 | Source: research/PROBLEM-BANK-SPONSOR-DNA.md + company-lanes reports + winner forensics
Status: synthesis of VERIFIED intel; 3 parallel runs in flight to deepen (cnc-sponsor-products, cnc-winner-anatomy, cnc-problem-lanes)

---

## 1. WHAT MATTERS MOST (the winning formula, every edition)

1. **AI/ML is non-negotiable** - all 5 sponsors have AI product lines (Gemini, Swift+ML, Llama, GenAI consulting, Firefly). A build without AI loses.
2. **Working demo > deck** - every past winner shipped a prototype. AFTERPACKETS won with a working Android app + zero external deps.
3. **Their platform/API usage = "one of us" bonus** - Google Cloud/Android, Swift, Llama, Adobe APIs, cloud+data stacks.
4. **Real-world impact framing** - SDGs, industry problems, social good. Judges are industry + cyber + police taste.
5. **Polish + presentation** - enterprise judges reward clear storytelling. 3-min demo, 2:30 target.
6. **Zero external deps in the demo** (AFTERPACKETS rule) - the demo never dies on stage. Our engine has FULL offline mode.
7. **Clean repo = free points** - README-as-pitch, no node_modules junk, push every 3h (2024 finals rule).
8. **Original work in 24h** - scaffolds + libraries OK, pre-built projects = DISQUALIFICATION. Our scaffold is a scaffold, the skin mounting IS the build.

## 2. WHAT THE COMPANIES ARE MAKING + LOOKING FOR (VERIFIED from their own hackathons)

### Google
- **Making**: Gemini models, ADK (agents, tools, multi-agent, debug, deploy), Google Cloud, Workspace AI.
- **Looking for**: Solution Challenge 2026 "Build with AI" - must use ≥1 Google AI service + deploy to Cloud. Themes: Digital Asset Protection (sports media piracy), Rapid Crisis Response, Smart Supply Chains, Unbiased AI Decision (bias detection), Smart Resource Allocation. Judging: Technical Merit 40%, Alignment 25%, Innovation 25%, UX 10%.
- **Rewards**: search/summarize/ranking products, agents with measurable outcomes, grounded answers with evidence.

### Apple
- **Making**: SwiftUI, on-device AI, accessibility frameworks, HealthKit, Vision.
- **Looking for**: Swift Student Challenge 2026 - AI + accessibility winners. Polished native UX, camera/sensor apps.
- **Rewards**: mobile polish, accessibility, design quality.

### Meta
- **Making**: Llama 4 (open-weight, natively multimodal), knowledge graphs, social/community infra.
- **Looking for**: LlamaCon 2025 winners - OrgLens (AI expert matching, knowledge graph from Jira/GitHub/docs/resumes, digital twin chat), Compliance Wizards (fraud transaction analyzer, Llama multimodal, AI voice), Llama CCTV Operator (surveillance detection, no fine-tuning). $35K pool, 238 devs.
- **Rewards**: LLM-native products (the LLM IS the product), multimodal, real integrations (GitHub API, Jira), community platforms, fraud/moderation.

### Accenture
- **Making**: "Reinvent with AI" (Innovation Challenge 2026, 3,879 reg) - trusted enterprise AI, reimagining patient care, business insights into action, smarter manufacturing.
- **Looking for**: human-in-the-loop framing ("people and AI working together"), measurable business value, template-compliant decks, industry problem framing.
- **Rewards**: enterprise-grade solutions, business case clarity, structured deliverables.

### Adobe
- **Making**: Firefly (generative creative workflows, audio/video, provenance), Photoshop/Lightroom APIs.
- **Looking for**: Creative Jam winners - Sparky AI (node-based visual interface democratizing Firefly for non-developers: text prompts, background removal, element combining). India hackathon had a pure DSA round (O(1) math problem).
- **Rewards**: creative/media tools, Firefly integration, no-code wrappers, UI/UX polish, algorithmic thinking.

## 3. THE CONSENSUS (all 5 sponsors)

1. AI/ML non-negotiable
2. Working demo > deck
3. Their platform/API usage is a bonus
4. Real-world impact framing
5. Polish + presentation

## 4. HOTTEST TECH FOR A 24H BUILD (2026)

| Tech | Why sponsors reward it | 24h MVP shape |
|---|---|---|
| AI agents / agentic workflows | Google ADK push, Accenture autonomous intelligence | task intake → planner → approval gate → progress dashboard (BRIEFLENS = this) |
| Multimodal AI (vision/audio/docs) | Llama 4 native multimodal, Apple accessibility | upload/camera input → OCR → evidence panel → confidence → escalation (KAVACH CIRCLE = this) |
| Generative media + provenance | Adobe Firefly push, content authenticity | brief → asset → caption/alt → reviewer approve → provenance record (SIGNALSTORY = this) |
| RAG with citations | every sponsor's grounded-answer push | sources in, sourced answers out |
| Human-in-the-loop safety | Accenture "people and AI together" | approval gates, audit logs, escalation (KAVACH = this) |
| Indic language / vernacular | India context, DPDPA | Hindi-first interfaces, vernacular speech |
| On-device / edge AI | Apple, privacy framing | offline-first, zero deps (our engine = this) |

## 5. THE 2024-2025 PROBLEM SHAPES (from winner projects)

| Year | Winner | Problem shape | Stack |
|---|---|---|---|
| 2024 | TrueMix | misinformation/fact-checking | React + Express + Python ML + Firebase |
| 2024 | GENESIS | food distribution inefficiency | mobile + web + ML |
| 2025 | AFTERPACKETS | mobile network forensics | Android Kotlin + C++ DPI + React + Express |

**Pattern**: security/network + social-impact + ML = the house taste. Security themes resonate (judges: police ACP + cyber expert).

## 6. THE BEST TOPICS (pre-built, sponsor-shaped) - from IDEA-BANK

| Idea | Shape | Sponsor DNA | Status |
|---|---|---|---|
| A. BriefLens | agentic ops, approval gate | Google + Accenture | engine built, deck built |
| B. Kavach Circle | multimodal assistant, escalation | Meta | engine built, deck built |
| C. SignalStory | creative media workflow, provenance | Adobe | engine built, deck built |
| D. Kavach | call-security platform | security lane (house taste) | real product, deck built |

## 7. WHAT THE 3 IN-FLIGHT RUNS WILL ADD

- cnc-sponsor-products: 2025-2026 product launches + verbatim problem shapes per sponsor
- cnc-winner-anatomy: 10-15 winner case studies + demo techniques + scaffold validation
- cnc-problem-lanes: evidence-mined most-likely problem statements + kill criteria

Reports land in research/company-lanes/ when done.
