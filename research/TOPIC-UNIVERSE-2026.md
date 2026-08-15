# TOPIC-UNIVERSE-2026.md: every topic that can come (exhaustive)

Purpose: ONE file with the full universe of possible Craft N Code 2026
statements, so the team can build an idea finder + benchmark kit against
it. Parse the 21:30 drop against this file: company DNA, topic shape,
watch-words, kit mapping, demo gate, deck. The statement grammar at the
bottom generates every combination the sponsors can realistically write.

How to use: read the drop. Match company (Section 1). Match shape
(Section 2). Match domain (Section 3). That triple pins the kit
(Section 4) and the demo gate. Everything in this file is either
verified from the event site source, the 2025 problem set, or inferred
from the sponsor companies' public product lines. Nothing is vibes:
VERIFIED = seen in source/2025, INFERRED = sponsor DNA, WILDCARD =
possible but unranked.

## SECTION 1: COMPANIES (VERIFIED authors of the real statements)

The real statements are written by the sponsor companies, not the club.
Site tracks are the backup set. Fingerprint company FIRST.

### GOOGLE (prior 24%, setter)
DNA: agents that do real work, grounding, verification, Gemini,
responsible AI, search, productivity, developer tools.
Watch-words: agent, multi-step, grounding, verification, evidence,
tool use, "with sources", "explain your reasoning", "safe actions",
Workspace, Gemini, notebook.
Can ask: build an agent that completes a multi-step task with evidence
and human approval. Build a tool-use agent with typed actions. Build a
research companion that cites sources. Build an agent that verifies
before it acts. Build a system that audits what an agent did.
Kit: KIT-1. Gate: plan -> sources -> approval -> trace.

### APPLE (prior 15%, setter)
DNA: privacy by design, on-device, local intelligence, offline, photos,
health, voice, "never leaves the device".
Watch-words: on-device, private, local, offline, sensitive, health,
photos, voice, "your data stays on your phone", "no cloud".
Can ask: build an on-device assistant that transforms sensitive content
without cloud. Build a private health/finance organizer. Build a local
search over personal data with visible data movement. Build a graceful
offline fallback for an AI feature. Build a consent-first data
controller.
Kit: KIT-3. Gate: on-device -> refuse cloud -> safe fallback.

### META (prior 21%, setter)
DNA: messaging, WhatsApp/Instagram, creators, communities, multimodal,
Llama open models, broadcast, reels, groups.
Watch-words: message, WhatsApp, creator, community, reel, broadcast,
group, multimodal, image, voice note, "for your community".
Can ask: build a multimodal assistant inside messaging. Build a creator
tools pipeline (captions, replies, variants). Build a community
moderation assistant. Build a trusted-answer bot with human escalation.
Build a scam-aware messaging guard.
Kit: KIT-4 (+ KIT-4B if fraud words). Gate: message+image -> answer ->
escalation.

### ACCENTURE (prior 22%, setter)
DNA: enterprise gen AI adoption, governance, ROI, responsible AI,
industry ops (banking, retail, health, supply chain), productivity,
"how do we adopt AI safely".
Watch-words: enterprise, governance, adoption, productivity, ROI,
policy, compliance, consent, audit, "line of business", agentic ops.
Can ask: build a governed case router (unstructured -> structured ->
routing). Build an enterprise agent with policy gate and audit. Build a
consent+audit layer for AI use. Build a KPI dashboard for AI adoption.
Build an exception handler with human approval.
Kit: KIT-5 or KIT-1 ops. Gate: requests -> extraction -> exception ->
approval -> KPI.

### ADOBE (prior 18%, setter)
DNA: creative production, brand, Firefly, content provenance, content
credentials, marketing assets, brand-safe generation.
Watch-words: brand, creative, content, provenance, credentials,
campaign, asset, "on brand", "brand kit", "channels".
Can ask: build a brand-safe content generator with constraints. Build a
content provenance tracker. Build a campaign asset pipeline (brief ->
variants for channels). Build a review/approval workflow for creative
assets. Build an on-brand checker.
Kit: KIT-2. Gate: brief -> 3 variants -> violation caught -> approved
export.

### WHO ELSE COULD SET (INFERRED, lower prior)
Microsoft: enterprise agents, Copilot-shaped, M365, governance.
Watch-words: copilot, M365, enterprise, meetings.
Amazon/AWS: ops tooling, serverless agents, cost, scale.
Watch-words: serverless, scale, cost, ops.
NVIDIA: hardware-adjacent, edge AI, inference. Kit: KIT-3 or hardware
companion.
Any security company (CrowdStrike, Zscaler, Palo Alto, Indian banks'
security arm): fraud, phishing, deepfake, digital arrest, UPI safety.
Watch-words: scam, fraud, phishing, deepfake, digital arrest, UPI,
fraud call. Kit: KIT-4B overrides everything.
Any gov-adjacent partner: DPDPA, digital literacy, citizen services.
Watch-words: citizen, DPDPA, grievance, accessibility. Kit: KIT-5 or
KIT-3.

## SECTION 2: SHAPES (the 5 predicted structures, VERIFIED pattern)

Shape 1: TRUSTWORTHY AGENT. Input: tasks/emails/requests. Output:
ranked actions, each with evidence, approved by a human, audited.
Companies: Google, Accenture, Microsoft.
Shape 2: CREATIVE PRODUCTION. Input: brief + brand constraints. Output:
channel variants, provenance, approved export. Companies: Adobe.
Shape 3: PRIVATE INTELLIGENCE. Input: sensitive personal content.
Output: on-device transform, refusal to leak, fallback. Companies:
Apple, NVIDIA.
Shape 4: MULTIMODAL MESSAGING. Input: messages + images + voice notes.
Output: trusted answers, approved templates, human escalation.
Companies: Meta.
Shape 5: GOVERNED ENTERPRISE ROUTER. Input: unstructured requests.
Output: structured cases, routed, policy-gated, audited, KPI'd.
Companies: Accenture, Microsoft, gov-adjacent.

The engine (ingest -> extract -> evidence -> rank -> propose -> approve
-> audit) covers all 5. The kit decides the nouns.

## SECTION 3: DOMAINS (the topic universe, INFERRED where noted)

1. Ops/SRE: incident triage, SLO, runbooks, rollback, on-call (VERIFIED
   2025 lane: inbox navigator; our KIT-1 feed is this)
2. Customer support: tickets, refunds, escalations, churn, SLA
3. Finance: refund batches, approvals, fraud flags, invoices (VERIFIED
   2025: NFT ticketing)
4. Security: scam calls, phishing, digital arrest, deepfake, UPI fraud,
   vuln scanning, cert rotation (VERIFIED: our Kavach D)
5. Privacy: consent, on-device, data movement, DPDPA-shaped (INFERRED
   from Apple DNA)
6. Creative: brand kits, campaigns, captions, variants, provenance
   (INFERRED from Adobe DNA)
7. Messaging/community: WhatsApp-style, moderation, creators, broadcast
   (INFERRED from Meta DNA)
8. Enterprise ops: case routing, policy, exceptions, KPI (INFERRED from
   Accenture DNA)
9. Health: appointment triage, records, privacy (WILDCARD, fits KIT-3/5)
10. Education: lecture generation, grading, study plans (VERIFIED 2025:
    AI lecture generator, lab grader)
11. Web3: ticketing, loyalty, identity (VERIFIED 2025: 2 lanes)
12. Hardware/edge: PS-05, device companions (VERIFIED: track exists)
13. Government/citizen: grievances, digital literacy (WILDCARD, fits
    KIT-5)
14. Climate/sustainability: reporting, optimization (WILDCARD)
15. HR/people ops: onboarding, leave, policies (WILDCARD, fits KIT-5)
16. Legal/compliance: contract review, policy checks (WILDCARD, fits
    KIT-5, careful with "not legal advice")
17. Retail/e-commerce: checkout, returns, inventory (WILDCARD, fits
    KIT-1)
18. Travel/logistics: bookings, delays, rerouting (WILDCARD, fits
    KIT-1/5)
19. Media/news: summarization, verification, provenance (WILDCARD, fits
    KIT-2)
20. Social good/accessibility: inclusive design, assistive AI
    (WILDCARD, strong judge resonance)

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
PS-05 hardware                                -> software companion to
   closest kit, never pitch fresh hardware
PS-04 open track                             -> strongest kit for the
   drop's actual words, same matrix

## SECTION 5: THE STATEMENT GRAMMAR (generates every possible drop)

Every realistic statement = Subject + CoreAction + Constraint +
Channel + Evaluation + Twist.

Subject (who it is for): ops teams / support agents / creators /
communities / enterprises / citizens / individuals / students /
doctors / teachers / merchants / travelers / developers.

CoreAction: triage / rank / summarize / route / approve / generate /
transform / detect / verify / escalate / audit / answer / search /
schedule / personalize / protect / explain.

Constraint (the differentiator, ALWAYS present): with evidence / with
human approval / on-device / offline-capable / with provenance / within
brand rules / within policy / with consent / under SLA / with audit
trail / without hallucinating / in multiple languages / with a fallback
/ at scale / in real time.

Channel: email / WhatsApp / support tickets / calls / social / docs /
images / voice notes / mixed.

Evaluation: "working demo" / "show the failure case" / "measured
accuracy" / "judged on trust" / "judged on adoption" / "judged on
scale" / "3-minute demo".

Twist (what makes it hard): the model is unreliable / the network dies /
the user is non-technical / the content is sensitive / the brand is
strict / the volume is 100x / the deadline is real / the cost must stay
zero / the judge will attack it.

Our engine covers every combination: the constraint maps to a gate
(approval, provenance, consent, offline), the channel maps to an
adapter, the twist maps to a stress test (see STRESS-BENCH-2026.md).
The only combos that cost extra are hardware (PS-05) and true real-time
audio during a live call (Kavach D covers the call-flow claim with the
signed evidence bundle, demo is simulated audio, honest).

## SECTION 6: THE 2025 SET (VERIFIED, what they asked before)

Lanes: NFT event ticketing / Web3 loyalty SBT / P2P skill swap / AI
lecture generator / Collegiate Inbox Navigator (our exact shape) /
Automated Lab Grader / Mobile Packet Hunter (winner).
Phase-2: chain auto-select, quest map, anonymity+replay, animations,
MCP server, load testing, live request interception with consent+audit.
Lesson: the winning lane was the empty one, the winner scoped down
twice, rebranded an hour before freeze, and shipped a working hard
thing with zero deps. Expect 2026 to reward the same.

## SECTION 7: THE 2026 BACKUP TRACKS (VERIFIED from site source)

PS-01 Rewind the Legacy (retro/nostalgia tech) -> maps to any kit with
a nostalgia noun swap, low prior
PS-02 Night Ops (security/ops) -> KIT-1 or KIT-4B
PS-03 Signal/Noise (our default, = IDEA A) -> KIT-1
PS-04 Open Track (wildcard) -> matrix above
PS-05 Hardware Hack -> software companion, never fresh hardware

## SECTION 8: THE PRIORITY MATRIX (what to prepare first)

1. KIT-1 (agentic ops): highest prior (Google + Accenture = 46%),
   matches our default track, matches the 2025 winning shape. DONE.
2. KIT-4B (fraud override): second highest, any security word triggers
   it, Kavach proof exists. DONE (fixture below).
3. KIT-4 (messaging): Meta 21%, multimodal demo is flashy. DONE.
4. KIT-2 (creative): Adobe 18%, provenance story is strong. DONE.
5. KIT-3 (privacy): Apple 15%, on-device story is a judge favorite.
   DONE.
6. KIT-5 (enterprise): Accenture 22% shares KIT-1's engine, cheap to
   mount. DONE.

All five kits exist in scaffold/fixtures/kit*.json with decks and
storyboards already in the repo. The night is a fingerprint + copy
job, not a build.

## SECTION 9: EXPANSION PASS 1 (2026-08-15, landscape scan)

Source: reskilll "AI Hackathon Ideas for 2026: 20 Projects That Use Agentic AI and MCP" + "AI Hackathon Calendar India 2026" (both live 2026-08-15 via curl, Firecrawl 402). Full detail in ~/hackathon-idea-lab/research/TOPIC-UNIVERSE-2026.md (master copy lives there; this file stays in sync for the night).

NEW SHAPES (VERIFIED landscape, both mount on the existing engine):
- Shape 6: MCP ECOSYSTEM. Watch-words: MCP, model context protocol, tool server, integration. Kit: KIT-1 architecture + labeled tool adapters. NOTE: "MCP server" already appeared in the 2025 phase-2 extension list, so this vocabulary is familiar to these setters.
- Shape 7: MULTI-AGENT SYSTEM. Watch-words: agent team, multi-agent, supervisor, orchestrator, specialist agents. Kit: KIT-1 architecture + coordinator view in the UI.

NEW DOMAINS (30 total now): DevTools/code (codebase navigator, code review pipeline, OSS contribution finder), meetings/collaboration (meeting assistant, action items), research/academic (paper analyzer, lit review), agriculture (advisory agent, weather+soil+crop), AI for Bharat / Indic (multilingual, Indic models, rural, voice-first: Kavach DNA fits), responsible AI (bias, explainability, safety), gaming/entertainment (AI dungeon master), music/audio (playlist curator), food/recipe (fridge image -> recipe), smart city (multi-agent dashboard).

CONFIRMED 2026 THEMES (VERIFIED): on-device AI / edge LLMs (iQOO hackathon June 2026), agentic AI, MCP servers, GenAI education (SahAI for Shiksha, Wadhwani AI), AI for Bharat, responsible AI. Same tips independently confirmed: demo matters, show the agent loop, handle failures gracefully.

Kit mapping additions: MCP words -> KIT-1 + tool adapters. Multi-agent words -> KIT-1 + coordinator view. Education words -> KIT-1/KIT-4. Indic/Bharat words -> KIT-4/KIT-1 voice-first (Hindi-first Kavach DNA). On-device words -> KIT-3.
