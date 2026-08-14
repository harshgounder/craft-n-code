# WAVE SYNTHESIS  -  what the 4 deep-research runs give us (Aug 14, pre-night)

Compiled: 2026-08-14 | Sources: cnc-problem-lanes (78K chars, ADECENT 333 cites), cnc-sponsor-products (68K, ADECENT 230 cites), cnc-winner-anatomy (62K, SURFACE 138 cites), cnc-state-rounds (in flight), + prior passes 1-2 (company-lanes).

## 1. THE 5 MOST LIKELY PROBLEM STATEMENTS (ranked, with our response)

| Rank | Predicted problem shape | Sponsor | Our idea/deck | Demo gate |
|---|---|---|---|---|
| 1 | Trustworthy agent: multi-step task, evidence, approved tools, confirmation before side effects, typed audit trail | Google (Accenture overlap) | IDEA A BriefLens (deck-agentic) | plan → sources → approval → trace |
| 2 | Creative production agent: brief + brand kit → channel variants, constraints, provenance, review | Adobe | IDEA C SignalStory (deck-creative) | brief → 3 variants → violation caught → approved export |
| 3 | Private personal intelligence: on-device transform of sensitive content, visible data movement, graceful fallback | Apple | IDEA B privacy skin (deck-multimodal) | on-device state → refuse cloud → safe fallback |
| 4 | Multimodal assistant on messaging: text+image, trusted answers, approved templates, human escalation | Meta | IDEA B Kavach Circle (deck-multimodal) | message+image → answer → escalation |
| 5 | Governed enterprise case router: unstructured requests → structured cases, routing, policy, consent, audit | Accenture | IDEA A ops skin | 3 requests → extraction → exception → approval → KPI |

## 2. THE COMMON DENOMINATOR (why one engine wins)

All 5 sponsors converge on the SAME core: input → extraction → evidence → ranking → proposed action → policy gate → human approval → audit trace. The report's words: "The common task is not a model call; it is making AI usable inside a controlled system." Our engine IS this pipeline. A skin = nouns + data + UI labels + provider adapter. Mount time per skin: 15-40 minutes.

## 3. THE 5 PORTABLE PATTERNS (scaffold must-haves)

1. Evidence-first structured answers: every answer = answer + confidence + evidence[] + unknowns + next_action. Source card per claim. JSON schema validation + repair loop.
2. Tool gateway with approval: typed tool registry (name, schema, side-effect class), policy gate (read-only vs reversible vs side-effecting), approval modal, audit event.
3. Multimodal + channel adapter: normalize every event (channel, sender, text, media, conversation_id, consent). WhatsApp/web/phone/fixture all become one object.
4. Privacy/provenance/consent layer: data class, processing location badge, consent record, provenance manifest (prompt, model, timestamp, reviewer).
5. Evaluation + failure observability: 3 golden fixtures (happy, ambiguous, adversarial), trace viewer, provider fallback, replay mode.

## 4. WHAT WE ALREADY HAVE vs THE GAPS

| Pattern | Our scaffold | Gap |
|---|---|---|
| Evidence-first answers | source_id, deadline, rank_score per item; search returns sourced results | no explicit confidence field per answer; no schema validator |
| Tool gateway + approval | NOT built (the "approval gate" discussed but deferred) | BUILD: typed tool registry + policy gate + approval endpoint (30-45 min) |
| Multimodal adapter | none | BUILD if Meta/Apple flavor: image/PDF input + OCR path (60-90 min) |
| Privacy/provenance | none in scaffold (Kavach has it separately) | consent record + provenance manifest (20-30 min) |
| Evaluation/observability | 13/13 ad-hoc checks; offline+LLM dual mode; cache | trace viewer + replay fixture (30-45 min) |
| Provider abstraction | OLLAMA_KEY + URL + model env vars = swappable already | adapter interface for Google/Meta/Adobe providers |

## 5. THE EXECUTION PLAN (report's hour-by-hour, adapted to OUR timeline)

Our real clock: 21:30 drop → 06:00 close = 8.5 hours (not 24). Adjust:
- Hour 0 (21:30-22:30): parse drop for sponsor fingerprint (cue table), run 5 smoke tests in parallel (model key, network, offline mode, fixtures, deck), score lanes, freeze the ONE-SENTENCE story.
- Hour 1-3: mount the skin (nouns, seed data, UI labels). Our engine is pre-built, so this is swap + regenerate decks.
- Hour 3-6: vertical slice + one differentiator + one staged failure (the failure path WINS demos).
- Hour 6-8: polish, KPI card, record backup video, rehearse 2:30.
- Kill criteria (pre-agreed): any dependency failing its time gate (60-90 min) → switch to fixture/replay mode. Never spend 6h on image quality or a blocked API.

## 6. THE ZERO-DEPENDENCY RULE (why AFTERPACKETS won, and we repeat it)

The report: "The winning overnight scaffold should have zero UNCONTROLLED dependencies." Three execution modes: LIVE (real model), CACHED (replayed responses, same UI), OFFLINE (deterministic rules). Put a mode indicator on screen. A judge trusts a candid fallback more than a frozen demo pretending a dead API worked. Our engine already does LIVE + OFFLINE; CACHED is the .llm_cache.json mechanism (exists, used silently).

## 7. INDIA-FIRST = differentiator (not requirement)

Hindi/Hinglish voice+text interface layer is a verified theme in India hackathons. Add as a thin layer, never the critical path. DPDPA: build consent + audit as product features, NEVER claim legal compliance from a prototype (report's explicit warning: don't invent DPDPA deadlines on stage).

## 8. THE 10 QUESTIONS TO ASK AT REVEAL (shortlist)

1. Which sponsor API is mandatory vs optional vs thematic?
2. Is a simulated integration accepted when the workflow is demonstrated honestly?
3. What are judges rewarding: model novelty, user impact, responsible AI, polish, or sponsor integration?
4. Must the demo work offline / on a specific OS?
5. What is the ONE user outcome the sponsor wants improved?

## 9. STATE-ROUND HUNT (in flight)

cnc-state-rounds run is hunting for the 2024-2025 state-round problem texts (esp. Rajasthan 2025) + state format forensics. Landing soon, will append.

## 10. NEXT BUILD PRIORITIES (if we want the scaffold truly complete)

1. APPROVAL GATE (highest ROI: Rank-1 predicted shape = approved tools; judges see the control plane) - 30-45 min
2. Fixture/replay mode + trace viewer (the demo-failure insurance) - 30-45 min
3. Multimodal input adapter (image/PDF → evidence) - 60-90 min
4. Provider adapter interface (Google/Meta/Adobe swap) - 30 min
5. Provenance/consent record - 20-30 min

All 5 fit in ~3h and make every predicted shape mountable with zero surprises.
