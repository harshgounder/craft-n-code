# SKIN-KITS-2026: mountable templates for every predicted shape

Purpose: turn the 15-40 min skin mount into a copy-paste job. Each kit is
self-contained: a fixture feed (data, mounts instantly via --fixture),
a label-patch brief (one opencode one-liner if UI labels must change),
deck beats, demo script deltas, and judge Q prep. Night flow: fingerprint
the drop (company vocab + topic shape) -> pick the kit -> mount -> ./demo.sh.

Kit anatomy (everything is in this repo, nothing to research at night):
  1. fixture JSON in scaffold/fixtures/<kit>.json (data, my lane, done)
  2. label patch brief below (only if the UI must speak the skin's nouns)
  3. deck beats: which deck slides to swap (decks are generic, noun swaps)
  4. demo script delta: what changes in the 2:30 run
  5. judge Qs: the questions that kit's judges ask + the answers

The 4 skins share one engine, so a kit is mostly seed data + nouns.
The engine does not change between kits. The LLM layer runs live when the
key works, offline otherwise, badge always honest (BUILD-SPEC-3).

## KIT-1: TRUSTWORTHY AGENT / agentic ops (Google, Accenture ops)
Company DNA: multi-step task, evidence, approved tools, confirmation
before side effects, typed audit. Watch-words: agent, multi-step,
grounding, verification, tool use, "with evidence".
Fixture: scaffold/fixtures/kit1_agent.json (ops mail + tickets).
Demo delta: open feed -> approve a propose action -> show audit trace
ring -> show provenance manifest with prompt_sha256 -> show the badge
flip when the key dies (offline fallback, the honesty moment).
Label swaps: "Signal Engine" -> "BriefLens"; "Ranked feed" -> "Decision
queue"; "Approve" stays. Side-effect classes already typed (registry).
Deck beats: 3 (the one action that matters) + 5 (typed audit) + 8
(offline fallback demo, the "we show failure" moment).
Judge Qs: "How do you know the LLM is right?" -> evidence-first answers
+ golden fixtures + trace ring. "What if the model is wrong?" -> human
approval gate + policy auto/suggest/require + provider_errors badge.
"Who adopts it?" -> ops teams drowning in channels (the 2025 Collegiate
Inbox Navigator lane won this shape).

## KIT-2: CREATIVE PRODUCTION AGENT (Adobe)
Company DNA: brief + brand kit -> channel variants, constraints,
provenance, review. Watch-words: brand, creative, content, provenance,
campaign, asset, Firefly.
Fixture: scaffold/fixtures/kit2_creative.json (brand briefs, briefs with
constraints, one brief that violates brand rules on purpose).
Demo delta: ingest a brief -> 3 channel variants proposed -> one variant
catches a brand violation -> approve export -> provenance manifest shows
every input that shaped the output.
Label swaps: "Signal Engine" -> "SignalStory"; "Ranked feed" -> "Brief
queue"; proposals show channel tags.
Deck beats: 2 (creative pipeline) + provenance slide + constraint demo.
Judge Qs: "Is this just a prompt wrapper?" -> no: constraints are typed,
approval is required, provenance is deterministic (prompt_sha256), brand
rules are data not vibes. "Content credentials?" -> provenance manifest
is our version of it, honest about LLM usage.

## KIT-3: PRIVATE PERSONAL INTELLIGENCE (Apple)
Company DNA: on-device, private, local, offline, sensitive content,
visible data movement, graceful fallback. Watch-words: on-device,
private, local, offline, sensitive.
Fixture: scaffold/fixtures/kit3_privacy.json (personal items: health,
financial, family; one item that must NOT leave the device).
Demo delta: show consent records (grant/deny), show a sensitive item
refusing cloud processing (offline fallback), show the mode badge
proving nothing left the machine, show the audit trail of what data
moved where.
Label swaps: "Signal Engine" -> skin noun (privacy-first inbox);
highlight the badge; the refusal moment is the demo beat.
Deck beats: 4 (on-device transform) + consent slide + DPDPA-shaped
honesty (consent as a feature, never claim legal compliance).
Judge Qs: "Is it really on-device?" -> the LLM layer falls back to
offline rules; badge proves it; nothing claims otherwise.
"Who adopts it?" -> anyone with sensitive data; truecaller-adjacent
privacy anxiety is the wedge.

## KIT-4: MULTIMODAL ASSISTANT ON MESSAGING (Meta)
Company DNA: text+image, trusted answers, approved templates, human
escalation. Watch-words: message, creator, community, reel, broadcast,
WhatsApp.
Fixture: scaffold/fixtures/kit4_messaging.json (WhatsApp-style items
incl. a scam message + an image attachment reference + a community
question; multimodal.json already covers attachments).
Demo delta: ingest a message with an image -> trusted answer -> one
risky action escalates to a human -> approve -> trace shows the whole
path. The scam item dies in seconds (Kavach Circle is this skin).
Label swaps: "Signal Engine" -> "Kavach Circle"; channels show as
WhatsApp-style labels.
Deck beats: Kavach deck (if the drop smells security) or IDEA B beats.
Judge Qs: "What if the message is a scam?" -> this kit IS the answer
(Kit-4B below). "Escalation?" -> typed policy gate, human approves risky
side effects only.

## KIT-4B: SECURITY / FRAUD OVERRIDE (any company, fraud words in drop)
If the drop contains scam/fraud/phishing/deepfake/digital-arrest/UPI
words, this overrides everything. Fixture: kit4_messaging.json +
scam corpus. Demo: scam call dies under a second, offline rules catch
it with zero network, signed evidence bundle for 1930/Chakshu.
Deck beats: Kavach security deck. Judge Qs: the 6 verified claims
(defensible gap: Hindi-first + on-device + real-time during live call +
digital-arrest workflow + signed evidence).

## KIT-5: GOVERNED ENTERPRISE CASE ROUTER (Accenture)
Company DNA: unstructured -> structured cases, routing, policy, consent,
audit, ROI. Watch-words: enterprise, governance, adoption, productivity,
ROI, policy.
Fixture: scaffold/fixtures/kit5_enterprise.json (tickets, exceptions,
policy items, one item needing consent before processing).
Demo delta: 3 requests in -> extraction -> one exception flagged ->
approval -> KPI card (SLA hours, channel mix) -> audit trail.
Label swaps: "Signal Engine" -> ops skin noun; "Ranked feed" -> "Case
queue"; SLA badges already exist on complaints.
Deck beats: 5 (governed pipeline) + KPI numbers slide (NUMBERS-2026).
Judge Qs: "ROI?" -> 42/42 tests, zero deps, cold boot 40-50 s, SLA
routing, KPI card. "Governance?" -> policy gate + consent + audit,
nothing claims legal compliance (DPDPA warning in docs).

## COMPANY FLAVOR MATRIX (fingerprint -> kit)
  Google    -> KIT-1 (agent vocab) or KIT-3 (if privacy words)
  Accenture -> KIT-1 ops or KIT-5 (enterprise vocab)
  Meta      -> KIT-4 (messaging vocab) or KIT-4B (fraud words)
  Apple     -> KIT-3 (privacy words) or KIT-4B (fraud)
  Adobe     -> KIT-2 (creative vocab)
  Security words anywhere -> KIT-4B overrides all.

## MOUNT PROTOCOL (measured target: 15-40 min, drill in MOCK-DROPS)
1. fingerprint (2 min): company vocab + topic shape -> kit from matrix
2. mount fixture: cp fixtures/<kit>.json fixtures/<skin>.json (or
   --fixture <kit> directly), swap nouns in the deck (10 min)
3. label patch (5 min): if labels must change, run the brief below via
   opencode or accept generic labels (generic is fine, the badge +
   pipeline carry the story)
4. ./demo.sh + timed run (10 min)
5. submit kit text from SUBMISSION-TEXT-KIT.md, numbers from
   NUMBERS-2026.md

## LABEL PATCH BRIEF (copy-paste to opencode during the night, if needed)
"Edit scaffold/webapp/static/index.html string labels only (no logic):
replace the app title with <KIT NAME>, the feed header with <QUEUE
NAME>, channel labels with <SKIN CHANNELS>. Keep all element ids,
endpoints, and the mode badge untouched. No em dashes. Do not commit."
Estimated 5 min including opencode startup.

## COMPETITOR LINES PER KIT (wave-8 teardown, VERIFIED)

KIT-1 (agentic ops / governed router): OpenAI Operator now lives inside
ChatGPT, still "research preview": sandboxed browser, no cross-app
approval queue, no audit log. Our dashboard ranks + logs across
email/Slack/tickets in one place, with a policy gate. That is the gap
Operator leaves open.

KIT-2 (creative provenance): C2PA is real hardware (6 camera vendors
sign: Leica, Sony, Nikon, Canon, Samsung Galaxy S26) but a software
verification desert: email clients strip metadata, messaging strips it,
CMS ignores it, screenshots unsolved. A verifier layer = the wedge.

KIT-4 (messaging trust): WhatsApp Meta AI "incorrectly claimed an
action was complete when it was not" and hallucinates text in images;
AI routes sit outside E2EE. Truecaller (500M+ users) covers the inbound
call funnel only. Group-chat moderation + verified replies + approval
flows are the trust gap.

KIT-4B (fraud guard): banks deploy FICO Falcon / SAS Fraud Management
over the 1930/CFCFRMS pipeline; RBI DPIP is closed to students. Sutra 5
of RBI FREE-AI ("AI for customer protection") is the explicit opening
for a customer-side tool. Neural Defend (seed, Mar 2025) does live
deepfake detection but has no India consumer install base. The space is
open.

KIT-5 (enterprise router): Salesforce Agentforce + ServiceNow Otto are
tuned for Fortune-500; Accenture + Google Cloud announced mid-market
"agentic AI" lines in 2026, confirming the SME gap. A vertical-scoped
router (one workflow, two tools, hard policy) is defensible in 48 hours.

KIT-3 (privacy): PrivateGPT 1.0 (57k+ stars) proved run-time privacy;
the wide gap is build-time: ingestion hygiene, audit of what got
chunked, who saw the embedding. That audit story is our evidence-first
UX, not an add-on.

MCP shape (if the PS is MCP-flavored): 9,652 servers in the official
registry (24 May 2026), 97M monthly SDK downloads; "connect an LLM to
X" is saturated. Spec dates to name-drop: 2024-11-05 (HTTP+SSE
deprecated), 2025-03-26 (Streamable HTTP), 2026-07-28 (stateless core,
hardened auth, MRTR). Tool poisoning (Invariant Labs, 1 Apr 2025) is
the headline attack class: typed allow-listed tools = the answer.
Compose gold-plated servers (filesystem, GitHub, Supabase, Slack,
Playwright, Redis, Postgres), never rebuild them.
