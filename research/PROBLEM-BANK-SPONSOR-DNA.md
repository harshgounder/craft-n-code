# Problem-Bank Forensics + Sponsor DNA — Craft N Code

Compiled: 2026-08-13 | Sources: Unstop API, Scribd via r.jina.ai, Google Open Source, rivalsearch

## 1. 2024 RULES (VERIFIED — full text from Unstop API 1171379)

- **Fee**: ₹200/team (2024). (2026: ₹299 per CSC post / ₹699 per user's Unstop listing — VERIFY.)
- **Team**: 2-4 members, cross-college allowed within same state. No solo.
- **Finals**: 24 hours at IIIT Bhubaneswar.
- **Original work**: pre-existing projects or substantial pre-written code = DISQUALIFICATION.
- **GitHub rule**: push code at least once every 3 HOURS during the hackathon.
- **Submission**: project description + demo + documentation before deadline.
- **Stack**: any language/framework, open source preferred, disclose your stack.
- **Judging criteria**: creativity, technical complexity, practicality, overall presentation. Judges' decisions final.
- **Reimbursement**: sleeper railway fare for non-Odisha teams traveling to finals. Meals provided.
- **Eligibility**: bachelor's students, compete in your own state's prelim.

## 2. 2024 PROBLEM STATEMENTS (status)

- The 2024 brochure (Scribd 781392222, 9 pages) is IMAGE-BASED — text layer is JS-rendered, r.jina.ai returns the page chrome + garbled font glyphs. The actual problem statements are in the brochure images (OCR needed).
- The 2024 national listing details contain RULES but NOT the problem statements (problems were given at the event / via the state organizers).
- 2024 state listing (1175823): "Participants should thoroughly review the problem statements and submit their ideas according to the Internal Round Organizing College's Criteria" — the STATE organizers set the prelim problems.
- **2026 pattern (user intel + CSC post)**: sponsor companies (Google, Apple, Facebook, Accenture, Adobe) set the questions. Club only runs logistics.
- **Implication**: the Rajasthan prelim problem will be released by the sponsors, likely at/just before the Aug 15 21:00 submission window. Watch the Unstop portal + CSC channels.

## 3. SPONSOR COMPANY DNA (what each rewards)

### Google
- Google Open Source hackathon policy (VERIFIED, opensource.google): Google employees can only participate where IP terms are clean (no IP assignment, open-source-friendly). Google's own hackathons (Google Student AI Hackathon 2026, Solution Challenge) reward: practical AI applications, Google tech usage (Gemini, Cloud, Android), real-world impact, working demos.
- Google Solution Challenge criteria: alignment with UN SDGs, technology implementation, impact, scalability.
- **Solution Challenge 2026 (VERIFIED, madhavmadupu/google-solution-challenge-2026 overview.md)**: tagline "Build with AI"; must use ≥1 Google AI service (Gemini/Vertex/Vision); prototype MUST deploy to Google Cloud. 5 themes: PS1 Digital Asset Protection (sports media piracy), PS2 Rapid Crisis Response (hospitality), PS3 Smart Supply Chains, PS4 Unbiased AI Decision (bias detection), PS5 Smart Resource Allocation (volunteer matching). Judging: Technical Merit 40% (complexity, AI integration, scalability, security), Alignment with Cause 25%, Innovation 25%, UX 10%. Winning playbook: pick the theme with the highest technical ceiling + real datasets + natural AI fit; "the LLM is the product" not "we added a chatbot"; consumer-grade UX polish.
- **What a Google-set problem likely rewards**: AI/ML application, mobile (Android), clean engineering, user-centric design, measurable impact.

### Apple
- Apple's hackathon presence: Swift Student Challenge (WWDC) — rewards Swift/SwiftUI skill, creativity, accessibility, polished UX.
- **What an Apple-set problem likely rewards**: iOS/mobile polish, design quality, accessibility, developer experience.

### Facebook/Meta
- Meta hackathons (Meta Hackathon, Llama Impact): reward AI (Llama models), social impact, community platforms, developer tools.
- **LlamaCon Hackathon 2025 (VERIFIED, ai.meta.com blog)**: 238 devs from 600+ registrants, 24h, $35K pool, 44 projects, 2-round judging. Winners: 1st OrgLens (AI expert matching, knowledge graph from Jira/GitHub/docs/resumes, digital twin chat, React+Tailwind+Django+Llama API), 2nd Compliance Wizards (fraud transaction analyzer, Llama multimodality, AI voice assistant), 3rd Llama CCTV Operator (surveillance event detection via Llama 4 multimodal, no fine-tuning), Best Llama API Usage Geo-ML. Partners: Groq, Crew AI, Tavus, Lambda, Nebius, SambaNova (each offered credited usage + workshops + mentors + judges).
- **What a Meta-set problem likely rewards**: AI/LLM applications, social/community platforms, content moderation, AR/VR (if relevant). LlamaCon pattern: LLM-native products (the LLM IS the product), knowledge graphs, multimodal, digital twins, real integrations (GitHub API, Jira).

### Accenture
- Accenture hackathons (e.g. Accenture Innovation Challenge): reward business-relevant innovation, industry solutions (healthcare, finance, retail), AI + cloud + data, presentation quality, feasibility for enterprise adoption.
- **Accenture Innovation Challenge 2026 (VERIFIED, Unstop API 1714566)**: "Reinvent with AI" — 3,879 reg / 2,273 players, Jul 24-Oct 9. Themes: trusted enterprise AI systems, reimagining patient care (intelligent decision support), transforming business insights into action, smarter/resilient manufacturing. Multi-stage: Round 1 = 2-3 slide deck (prescribed template) + 2-3 min video (TeamName_CampusName naming), then prototype development. Teams up to 3, pre-final/final year only. Core ask: "people and AI working together" — human-in-the-loop framing.
- **What an Accenture-set problem likely rewards**: enterprise-grade solutions, industry problem framing, data/AI depth, business case clarity, polished pitch. Their DNA: AI + human ingenuity, measurable business value, structured deliverables (template compliance matters).

### Adobe
- Adobe hackathons (Adobe Creative Jam, Adobe Developer): reward creative tools, design, media tech, AI in creative workflows (Firefly), developer experience with Adobe APIs.
- **Adobe India Hackathon 2025 (VERIFIED, Sibasish11/Adobe-Hackathon-2025 repo)**: Round 1 = pure DSA problem (Corporate Training — Max Employees: T employees, N workshops, rooms with capacities A/B, each employee needs K workshops; constraints up to 1e9, so it's an O(1)/math problem, not brute force). Adobe's coding round tests algorithmic thinking under big constraints.
- **dentsu x Adobe global hackathon Q1'25 (VERIFIED, dentsu.com blog)**: 115 registrants, 28 teams, 12 countries, 72h hacking, 30 Adobe+AWS experts, ~3,000 API calls, 29 AWS accounts, 18 submissions. Winner: Sparky AI — node-based visual interface for image creation/manipulation, democratizing Adobe Firefly for non-developers (text prompts, background removal, element combining). Pattern: Firefly-powered creative tools, no-code/low-code wrappers, AWS infra.
- **What an Adobe-set problem likely rewards**: creative/design tech, media processing, generative AI in creative workflows (Firefly), UI/UX excellence. Their DNA: Firefly integration, visual/no-code tooling, polished creative output, developer experience with Adobe APIs.

### Consensus sponsor DNA (all 5)
1. **AI/ML is non-negotiable** — every one of the 5 has an AI product line (Gemini, Swift+ML, Llama, GenAI consulting, Firefly).
2. **Working demo > deck** — all reward shipped prototypes.
3. **Their platform/API usage is a bonus** — using Google Cloud/Android, Swift, Llama, Adobe APIs, or cloud+data stacks reads as "one of us".
4. **Real-world impact framing** — SDGs, industry problems, social good.
5. **Polish + presentation** — enterprise judges reward clear storytelling.

## 4. 2024-2025 PROBLEM SHAPES (from winner projects)

| Year | Winner | Problem shape | Stack |
|---|---|---|---|
| 2024 | TrueMix (participant) | misinformation/fact-checking | React + Express + Python ML + Firebase |
| 2024 | GENESIS (Hackfest) | food distribution inefficiency | mobile + web + ML |
| 2025 | AFTERPACKETS | mobile network forensics | Android Kotlin + C++ DPI + React + Express |

**Pattern**: security/network + social-impact + ML = the house taste. The Tech Society's judges (Hackfest 2024) included a police ACP + cyber expert — security themes resonate.

## 5. WHAT TEAM 511 SHOULD PREPARE

1. **Flexible stack** (sponsor-agnostic): React/Vite frontend + Express/FastAPI backend + ML component + optional mobile (Kotlin/Flutter). This covers all 5 sponsor domains.
2. **Idea bank across sponsor domains**: AI/ML app, mobile app, creative/media tool, enterprise/industry solution, social/community platform. 2-3 ideas per domain, pre-scoped to 24h build.
3. **GitHub hygiene**: clean repo, no node_modules/.gradle junk (free points vs every past winner), README-as-pitch, push every 3h if finals.
4. **Watch for the problem release**: Aug 15 21:00 IST submission window opens. The sponsor question likely drops then. Have the stack scaffolded BEFORE.
5. **The 24h finals rule**: original work only, no pre-built projects. But pre-built SCAFFOLDS + libraries are fine (all winners used standard stacks).
