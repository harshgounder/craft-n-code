# IDEA BANK - pre-built for sponsor-set questions (drop-ready)

Compiled: 2026-08-14 | Purpose: the problem statements drop **21:30 IST Aug 15**. We will NOT have time to brainstorm that night. Every idea below is pre-built: problem angle, MVP scope for 24h, stack that matches OUR skills, demo script, judge mapping, risk. We pick within 10 minutes of the drop.

**Source of truth (Aug 14, Rudra in person)**: the REAL questions are written by the sponsor companies (Google, Apple, Meta, Accenture, Adobe), not by the club. The site's track list is a backup set and is NOT a basis for prep. The only site-derived facts we rely on are the timings below.

**Timings (the only website facts we use)**:
- Aug 15 21:00: idea submission opens
- Aug 15 21:30: problem statements drop
- Aug 16 06:00: idea submission closes
- Aug 16 10:00-17:30: pitch to judges at MUJ (3-min demo, 2:30 target)

---

## 0. THE DECISION TREE (fires within 10 minutes of the drop)

```
Real question drops at 21:30
│
├─ Fingerprint = Google (agents, tools, search, summarize,
│   deadlines, grounded answers) ────► IDEA A "BriefLens" (agentic ops)
├─ Fingerprint = Meta (Llama, multimodal, community,
│   moderation, fraud) ──────────────► IDEA B "Kavach Circle" (multimodal assistant)
├─ Fingerprint = Adobe (Firefly, creative, campaign,
│   asset, media) ───────────────────► IDEA C "SignalStory" (creative workflow)
├─ Fingerprint = Apple (Swift, accessibility, mobile,
│   safety, health) ─────────────────► IDEA D "Kavach" or its mobile skin
├─ Fingerprint = Accenture (workflow, case, enterprise,
│   KPI, approval) ──────────────────► IDEA A ops skin (case → owner → approval → metric)
├─ Security / safety / fraud flavor ─► IDEA D "Kavach" (existing product, real demo)
├─ Compliance / DPDPA / policy / consent words ─► IDEA E "VicharSetu" (compliance copilot, S9.16 track)
├─ Onboarding / enrollment / schemes / form words ─► IDEA E "Sahaayak" (onboarding copilot, S9.16 track)
└─ No fingerprint / off-map ─────────► Map to the closest idea. Never pitch a fresh one.
```

The strategic core: ONE engine (ingest → dedupe → summarize → rank → deadlines → propose → approve), domain-agnostic. Every idea mounts on it with a different skin. Kavach is the only pre-existing product and covers the security lane. Idea E skins (VicharSetu/Sahaayak) added from the complaint mine (S9.16, DEEP 95.9, 85 quotes): the 6 pain tracks are Trust Verification, Cost/Quota, Compliance-as-a-Service, Onboarding Copilot, Workflow Orchestrator, Indic-First UX; A covers Workflow + Cost/Quota, B covers Trust, D covers Trust at call level, E covers Compliance + Onboarding, Indic-First is a skin on any of them.

---

## 1. IDEA A - "BriefLens" (agentic ops / personal productivity) (PRIMARY for Google/Accenture)

The deep-research pass-2 #1 predicted shape: an AI agent system that plans, executes, and reviews work using tools, with approval gates and measurable progress.

- **Problem angle**: inputs arrive from everywhere (email, chat, portal, tickets, docs). The ONE action that matters (a deadline, an approval, a payment) drowns under noise. An agent that acts without asking is unsafe; an agent that only chats is useless. The answer is a ranked feed + human-approved actions.
- **What we build (24h MVP)**:
  - Ingest: JSON feed from any channel (connectors are pluggable; demo uses pre-imported data)
  - Engine: dedupe → LLM summarize (one line) → rank by profile + sender authority + deadline → "today in 60 seconds" digest
  - Action proposals: concrete items become proposals (AI proposes, evidence attached: source, deadline, amount)
  - Approval gate: APPROVE / REJECT / SNOOZE per proposal, audit log (who, when, what)
  - Ask: semantic search over everything with sourced answers
- **Stack**: python engine (built) + zero-dep web server (built) + ollama-cloud LLM with offline fallback (built). NO paid keys, NO external deps in the demo (AFTERPACKETS rule).
- **Demo script (3 min)**: open "today" → digest reads out 2 urgent actions → click a proposal → evidence panel → APPROVE → status flips, audit logged → ask a question → sourced answer.
- **Judge mapping**: Google DNA (agents, tools, measurable outcomes), Accenture DNA (workflow + approval + audit), practicality, AI non-negotiable (satisfied).
- **Risk**: if the prompt is pure summarize/rank without actions, the approval gate is a small extra card, costs nothing.
- **Reuse**: THE engine. Already built and verified 13/13.

## 2. IDEA B - "Kavach Circle" (multimodal assistant + human escalation) (PRIMARY for Meta)

The deep-research pass-2 #2 predicted shape: an accessible multimodal assistant that accepts text, images, or documents, answers with evidence, and routes uncertain or high-risk cases to a human.

- **Problem angle**: information arrives in every format (text, image, PDF, chat). Generic assistants answer confidently even when wrong. High-risk cases need a human, not a guess.
- **What we build (24h MVP)**:
  - Input: text paste, image upload, PDF upload (OCR via local tools)
  - Extraction: structured facts + evidence panel with source links
  - Answers: confidence score on everything; uncertain or high-risk routes to human review
  - Correction flow: user fixes the model, the fix is remembered (session cache)
- **Stack**: python engine + webapp + ollama-cloud LLM + OCR (tesseract if available, else offline mock). Zero external deps.
- **Demo script (3 min)**: drop a screenshot + a PDF → both extracted, facts with sources → ask a question → answer with confidence band → ask something risky → visible escalation to human → correct an answer → fix applied.
- **Judge mapping**: Meta DNA (multimodal, Llama), Apple DNA (accessibility, correction flows), safety framing (human-in-the-loop).
- **Risk**: multimodal can fail on bad inputs. Mitigation: error handling + confidence UI + pre-recorded fallback video.
- **Reuse**: engine for the evidence layer; Kavach safety patterns for escalation.

## 3. IDEA C - "SignalStory" (creative / enterprise media workflow) (PRIMARY for Adobe)

The deep-research pass-2 #3 predicted shape: a workflow that converts a real organizational brief into accessible, brand-consistent media assets using generative AI, with review, revision, content provenance, and multi-format delivery.

- **Problem angle**: making content is slow; making content that stays on-brand is slower. Generative AI creates fast but uncontrolled: wrong brand, wrong facts. Nobody can answer where an asset came from.
- **What we build (24h MVP)**:
  - Brief intake: paste a real brief → extract brand rules, tone, audience
  - Asset generation: labeled generator adapter (mock if no credentials; ollama-cloud can produce text assets; image generation optional)
  - Caption + alt text + export (multi-format: text, image card, PDF)
  - Review loop: human approves before delivery, version logged
  - Provenance record: prompt, model, lineage per asset
- **Stack**: engine pipeline (brief → structured output) + webapp + labeled generator adapter. Zero external deps if mock.
- **Demo script (3 min)**: paste a one-paragraph brief → system extracts brand + tone → generate an asset → caption + alt text → edit/regenerate → reviewer approves → provenance card shown.
- **Judge mapping**: Adobe DNA (Firefly, provenance, creative workflows), Accenture DNA (review + approval + measurable output), polish.
- **Risk**: no image-gen credentials on the night. Mitigation: the generator adapter is swappable; a text/asset pipeline still demonstrates the workflow, and provenance is the differentiator regardless.
- **Reuse**: engine for the structured extraction + approval pattern.

## 4. IDEA D - "Kavach" (call-security platform) (SECURITY LANE, existing product)

Our existing product (IIC 3.0, ~/iic-3/kavach): real-time scam-call screening, six detection departments fused into one intervention loop, Hindi-first.

- **Why this wins the security lane**: it is a REAL product with a REAL demo. Judges = industry + cyber + police taste (ACP Anjana Tudu, Sethi). No 24h build risk: it's built, tested, verified (V1 fresh-clone 5/5 scenarios).
- **What we build for THIS round (24h)**: the integration + demo harness: wire the engine's proposal/approval loop into Kavach's intervention flow (AI detects scam → proposes intervention → user approves → audit). Pre-scripted answer to "what did YOU build in the 24h": the integration + demo harness IS the build.
- **Demo script (3 min)**: simulate a digital-arrest call → flagged in <1s → AI proposes intervention → user approves → post-call report.
- **Risk**: "did you build this tonight?" question. Mitigation: pre-scripted honest framing (integration + harness + this round's demo is the build), plus the engine loop is genuinely new work.

---

## 4b. IDEA E (SKIN-ONLY, new) - "VicharSetu" (compliance-as-a-service copilot) + "Sahaayak" (onboarding copilot)

Added 2026-08-15 from the complaint mine (hackathon-idea-lab TOPIC-UNIVERSE S9.16, DEEP 95.9, 334 cites): the 30 most statement-ready pains cluster into 6 tracks. Four are covered by A-D. Two are NOT:

- **Compliance-as-a-Service track**: top pains = WhatsApp group admin jailed for member posts (2017 ruling), DPDPA pressure on 500M-user platforms, RBI data localization, digital arrest scams, Apple Intelligence unavailable on India SIMs. Skin: a compliance copilot that reads a policy/docs and answers "is this allowed" in Hindi with citations, audit trail, escalation. Scaffold = propose -> approve -> audit, fits verbatim. Kit: KIT-5/KIT-4. This is the strongest NEW skin if the drop says compliance, policy, or DPDPA.
- **Onboarding Copilot track**: top pains = Adobe CC student verification wall (no .edu in India), outsourced dev time-zone exploitation, Apple India no-region docs. Skin: an agent that walks a non-technical user through any enrollment/onboarding flow (gov scheme, platform, license) via WhatsApp + voice, offline fallback. Kit: KIT-4 + KIT-3.

Both are 100% scaffold-skins (no engine work), each has a ready quote bank in S9.16 for the problem slide. If the drop's domain is neither A-D nor these two, the S9.16 30-pain table is the tiebreaker.

---

## 5. THE COMPANY-LANE PROTOCOL (Rudra intel: the REAL questions come from the sponsors)

### How to read the drop (2-minute scan)
1. WHO set it? Read the problem text for the company's fingerprints (their product names, their API names, their phrasing).
2. WHAT shape is it? Map to the 22-shape set (TOPIC-UNIVERSE S2 + S9.2, demo-risk column). The 7 core + MCP/multi-agent/voice are the likeliest.
3. WHICH idea mounts? BriefLens / Kavach Circle / SignalStory / Kavach / VicharSetu / Sahaayak. See the lane table + the S9.16 six-track mapping.

### The company fingerprint table

| Sponsor | Their DNA (verified from their own hackathons) | Family they tend to set | Our answer |
|---|---|---|---|
| Google | Solution Challenge: must use ≥1 Google AI service, deploy to Cloud. Themes: asset protection, crisis response, supply chains, unbiased AI, resource allocation. ADK: agents, tools, multi-agent. | Agentic ops / search / summarize / ranking | IDEA A BriefLens |
| Meta/FB | LlamaCon winners: OrgLens (AI expert matching, knowledge graph), Compliance Wizards (fraud analyzer), Llama CCTV (multimodal surveillance). Llama 4: open-weight natively multimodal. | Multimodal assistants / community / fraud | IDEA B Kavach Circle |
| Accenture | Innovation Challenge: trusted enterprise AI, patient care, business insights into action, resilient manufacturing. Human-in-the-loop. Template decks. | Enterprise workflows / dashboards / approvals | IDEA A ops skin |
| Adobe | Creative Jam winners: Sparky AI (node-based Firefly wrapper). Firefly API: generative creative workflows, audio/video, provenance. | Creative / media workflows | IDEA C SignalStory |
| Apple | Swift Student Challenge 2026: AI + accessibility winners. SwiftUI, on-device, polished UX. | Mobile UX / accessibility / safety | IDEA D Kavach mobile skin |

### The 10-minute cue table (pass-1 deep research)

| Cue in released statement | Likely sponsor | Build this | One acceptance test |
|---|---|---|---|
| Documents, sources, notices, search, summarize, deadlines, grounded answer | Google | BriefLens (engine + source map + confidence bands) | Every answer has evidence + an action |
| Swift, SwiftUI, playground, iPhone, camera, sensor, accessibility, native app | Apple | Kavach Swift (native risk timeline, accessible) | Judge completes the core interaction in 1 min |
| Llama, open model, multimodal, video, audio, agent, community, moderation, fraud | Meta | Kavach Circle (user-defined rule + evidence + human override) | User defines a rule, system finds evidence, human approves |
| Workflow, case, hospital, plant, field, employee, KPI, approval, enterprise | Accenture | Kavach Ops (case intake → owner → approval → metric) | One case moves intake → resolution |
| Firefly, creative, campaign, asset, image, video, brand, personalize, node | Adobe | SignalStory (source → editable asset with provenance) | Source becomes an editable asset |

### Setter prior (if exactly one sponsor writes the state question)

Google 24% > Accenture 22% > Meta 21% > Adobe 18% > Apple 15%. Working priors, not facts. The released text OVERWHELMS them: if the statement names a sponsor product/API/vocabulary, that sponsor wins, full stop. Evidence labels in the report: VERIFIED = source seen, INFERRED = reasoned prediction, UNVERIFIED = rumor. The report's key negative finding: public record does NOT prove sponsor authorship. Keep the insider signal as a live hypothesis. The shared engine wins either way.

### Pass-2 findings (cnc-company-lanes-2, DEEP 90.1, 111 cites)

**Status check**: NO public source proves the sponsors write the questions. The sponsor-set claim stays UNVERIFIED until the drop itself. Prep is modular so it wins either way.

**The 3 ranked predicted shapes (INFERRED, rehearsal only, never claim they are real)**:
1. **Agentic operations / personal productivity** (Google ADK: agents, tools, multi-agent, debug, deploy; plus 2025's "AI for Personal Development" theme) → IDEA A.
2. **Multimodal campus/community assistant** (Meta Llama 4: open-weight natively multimodal + Apple 2026 accessibility winners) → IDEA B.
3. **Responsible creative/enterprise media workflow** (Adobe Firefly API + Accenture Tech Next: autonomous intelligence for work) → IDEA C.

**Prep architecture (have ready before 21:30)**:
- Input adapter: text, image, PDF, sensor/mock event
- Orchestrator: deterministic router + optional agent
- Model adapter: pluggable (ollama-cloud / Google / Llama / local mock)
- Creative adapter: image/media generation interface (labeled mock OK)
- Mobile shell: responsive web shell or SwiftUI starter
- Safety layer: PII redaction, consent, approval
- Evidence layer: source links, confidence, audit events
- Evaluation: latency, accuracy, completion, fallback

**Failure cases to avoid**: building a guessed sponsor prompt before the release (wait for text), generic chatbot with no measurable outcome (define user, action, metric), agent with unrestricted actions (approval gates + mock tools), multimodal demo without error handling (confidence + correction UI), media generator without provenance (store prompt + asset lineage), mobile-only build before the prompt (keep web/API fallback), healthcare claims without boundaries (triage + non-diagnostic framing).

**Our scaffold vs this**: the shared engine already IS the input adapter (JSON feed) + orchestrator (dedupe/rank) + model adapter (ollama-cloud + offline) + evidence layer (source_id, deadline, rank_score) + evaluation (verified 13/13). Gaps: creative adapter (none, labeled mock fine), safety layer (Kavach covers it), approval gate (built into IDEA A's demo flow; one POST /api/approve endpoint if needed).

---

## 6. THE SHARED SCAFFOLD (built Aug 14 - verified, committed, pushed)

Whatever drops, these are pre-built (see scaffold/README.md):

1. **The engine** (ingest → dedupe → LLM summarize → rank → deadlines). Domain-agnostic, verified in LLM mode (deepseek-v4-flash:0731) AND full offline mode. 13/13 ad-hoc checks.
2. **The webapp** (zero-dependency python server + dark UI: digest, ranked feed, search, request board). Runs on ANY machine with python3.
3. **4 decks** (deck-gen.js → pptxgenjs): deck-agentic (BriefLens), deck-multimodal (Kavach Circle), deck-creative (SignalStory), deck-kavach. Schema-validated. Swap slides ready.
4. **4 storyboards** (docs/DEMO-STORYBOARDS.md): second-by-second voiceover scripts for pre-recorded 3-min videos.
5. **LLM layer verified TODAY**: ollama-cloud key works (deepseek-v4-flash:0731 live test). Offline fallback means the demo NEVER dies. AFTERPACKETS rule: zero external deps.
6. **demo.sh**: one command → generate feed + serve UI.

## 7. RISK TABLE (honest)

| Risk | Likelihood | Mitigation |
|---|---|---|
| Problem doesn't match any predicted shape | Medium | Off-map protocol: map to closest idea, never pitch fresh |
| Demo fails on stage (network/rate-limit/permissions) | Medium | Pre-recorded videos + local mock mode for every demo |
| Sponsor authorship is wrong (Rudra intel off) | Low | Engine is domain-agnostic, ideas map to any shape |
| Judges ask "what did YOU build in the 24h" (Kavach) | Medium | Pre-scripted answer: the integration + demo harness IS the build |
| LLM quota dies at 3 AM | Low | ollama-cloud + offline rule-based fallback in the engine |
| Pitch overruns 3 min | High | Rehearse with a hard timer today, trim to 2:30 |

## 8. ACTION PLAN (TODAY, Aug 14)

1. [x] Build the engine skeleton (ingest → summarize → rank → deadlines) - verified
2. [x] Webapp (zero-dep server + UI) - verified
3. [x] 4 decks + 4 storyboards (BriefLens, Kavach Circle, SignalStory, Kavach)
4. [x] Verify LLM keys (ollama-cloud live test) + offline fallback
5. [ ] Pre-record 4 demo videos (screen + voiceover) - needs the team
6. [ ] Rehearse pitch with timer (2:30 target), record once
7. [ ] Deep-research pass 1 + 2 folded in (§5) - done, reports in research/company-lanes/
