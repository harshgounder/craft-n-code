# PRIOR-ART-MAP-2026.md: what exists per kit, with stars, and our wedge

Source: wave-15 prior-art shapes (parallel.ai, VERIFIED Aug 15, raw in
research/raw/wave15-priorart-shapes.md). Per kit: the existing landscape
with real numbers, the gap, our wedge. This is the "this exists" answer
for every kit, and the "combine don't reinvent" map for the build.

## THE THREE CROSS-SHAPE PATTERNS (no product fully executes any)

1. Consent-receipt + offline inference (Ollama 175k stars + truConsent
   + DPDP Phase 2 consent managers, effective 13 Nov 2026): DPDPA-ready
   local LLM. Nobody combines them; closeable in a weekend.
2. WhatsApp-first agentic UX (Truecaller 433M Android, WhatsApp 500M
   India users, 1930 helpline, indie workflow threads): enterprise tools
   ignore WhatsApp, OSS lacks AI. Single approval surface wins.
3. Approval-gated MCP (9,652 servers, Cerbos perms, 40+ CVEs Jan-Apr
   2026 against MCP SDKs): wrap every tools/call in approval + log.
   MCP offers no approval UX today.

Rule: INTEGRATE star products, never rebuild them. Wrap c2pa-rs, don't
write C2PA; draw on LangGraph/CrewAI primitives; use Ollama as the
engine. The demo story = the wrapper, the ledger, the gate.

## KIT-1 (governed agentic ops)

EXISTS: goose (Block) 51,981 stars, approval via recipes but NO
tamper-evident audit; OpenCode 160,000+ stars / 7.5M MAU, CLI confirm
but no formal approval UX; Operator/Claude Code/Cursor = per-action
confirmations, local-only logs; Glean = compliance exports, used by
~10% of Fortune 500; Notion AI/Zendesk AI/Intercom Fin = strong but
vertical; SaneBox/Superhuman = email-only.
GAP: no tool is horizontal (email+Slack+tickets) with a tamper-evident
approval ledger + shareable audit PDF. r/AI_Agents audit-trail thread
and TheHackerNews governance piece ask for exactly this.
WEDGE: our trace ring + policy gate + audit rows + honest badge =
the trust-shell. One-click audit export is a label away.

## KIT-2 (creative provenance)

EXISTS: C2PA co-led by Adobe/OpenAI/Google/Microsoft, 500+ companies;
BBC, Reuters, AFP, NHK, NYT, WSJ actively sign; Truepic (19 repos);
SynthID (Gemini only); Numbers Protocol; Starling Lab. Adoption tracker
(EditorsWebLog) enumerates the holes: email clients strip C2PA,
messaging apps strip metadata, CMS lacks integration, screenshot
problem unsolved.
GAP: verification is the desert. c2pa-rs SDK exists (API unstable) but
no verifier UX for normal people or Indian languages.
WEDGE: KIT-2 fixture = campaign briefs; our manifest per asset + the
honest badge = a verifier layer. Demo line: "6 camera makers sign,
zero apps verify. We build the verify side."

## KIT-3 (privacy / DPDPA-ready local AI)

EXISTS: Ollama 175k stars, PrivateGPT 50k+, AnythingLLM 30k+, LocalAI,
Jan, GPT4All: all inference-isolation, NONE consent-aware. truConsent
(Bangalore, IITMIC-incubated) and ComplyDP implement DPDPA Consent
Manager flow, but as webform/compliance SaaS, not AI-prompt-level.
DPDPA Phase 2 (consent managers) effective 13 Nov 2026.
GAP: inference consent: which prompts left the box, per-user data
principal status, tamper-evident consent receipt per call. Nobody does
this for local AI.
WEDGE: KIT-3 = consent-first UX + breach endpoint + local-first. The
wave-15 line: "single binary: Ollama + consent receipt + audit log,
DPDPA Phase 2 ready per call." That is our KIT-3 story with a name.

## KIT-4 / KIT-4B (messaging trust + fraud guard)

EXISTS: Truecaller 433M Android MAU, voice+SMS only, not OSS, 2019
data leak; Truecaller Lite (Benojir) OSS but no AI deepfake layer;
RealCall.ai spam blocker; Bureau identity decisioning (enterprise);
Scam AI / DeepfakeGuard OSS detections; Neural Defend / Sign3
enterprise voice defense; 1930 helpline = gov channel, no OSS bot
bridges it. Vishing surged 1,600% in 2025; only 7% of orgs ready for
deepfake fraud (ACFE/SAS). WhatsApp India 500M+ users; 1930 saved
~162 crore in 7 months (Times of India).
GAP: no tool cross-modal-detects WhatsApp voice notes + screenshots +
forwarded PDFs together, offline, with one-tap 1930 filing.
WEDGE: our fixture is the family WhatsApp room; pipeline ranks scam
patterns; badge shows evidence; 1930 packet one-tap. The "Lifeguard
for every messaging app" line, offline-first.

## KIT-5 (enterprise router / MSME)

EXISTS: n8n 192.3k stars (visual approval nodes, 500+ integrations),
Temporal (durable execution, Replay 2026 AI features), Camunda 8/Zeebe
(BPMN, heavyweight), Tranzact (Flutter MSME ERP, voice tasks), CloudAI
Workflow (SMB India, PF/ESI), Salesforce Agentforce (license confusion
for MSMEs), ServiceNow Otto + Moveworks (acquired Mar 2026, enterprise
only), Freshworks (MSME-first SaaS).
GAP: workflow engines = developer-targeted; MSME products = not
agentic; approvals are node-based, never WhatsApp-conversational; no
DPDPA consent per ticket. Indie Hackers thread: "wiring the tools
together turns into its own project every time."
WEDGE: KIT-5 = branch loan case routing with the approval pause +
audit trace; wave-15 line: "agentic router whose primary surface is
WhatsApp, fallback SMS, consent receipt per ticket."

## SHAPE 6 (MCP, if the PS is MCP-flavored)

EXISTS: official registry 9,652 latest / 28,959 server-version records
(24 May 2026); FastMCP, python-sdk, GitHub MCP Registry, OpenTools
(148 official servers, trust-scored); Cerbos MCP permissions (solid
primitive, no UX); Maxim Bifrost gateway; 40+ CVEs against MCP SDKs
Jan-Apr 2026; HN "MCP is dead?" thread (May 30 2026): "not dead, just
overused"; locallama-mcp cost routing.
GAP: no widely-shipped approval-per-call UX; dead-server share high;
security tooling emerging but no ledger.
WEDGE: approval-gated MCP proxy: per-tenant allowlist + human gate on
mutating tools + tamper-evident log of every tools/call. This is the
BUILD-SPEC-4 deck slide story too.

## SHAPE 7 (multi-agent, if the PS goes there)

EXISTS: LangGraph 39.6k stars, 43k downstream projects, human-in-the-
loop native; CrewAI ~30k stars, role-playing not controller; AutoGen
(MSR); OpenAI Swarm handoffs; MetaGPT; ChatDev 33.33% correctness on
ProgramDev per MAST; AgentCenter SPOF post; HN "CrewAI production" =
multiple "would not recommend in production".
GAP: failure recovery underbuilt everywhere; peer-to-peer handoff is
the SPOF; no local/offline option.
WEDGE: our answer = one controller, 2-3 tools, explicit state machine,
retry budgets. The MAST 14 failure modes table = our test map.

## NEXT

Waves 16 (domains), 17 (student builds + venues), 18 (OSS stand-on
map) land next; this file gets the domain rows + the venue search
recipe + the compose table appended.
