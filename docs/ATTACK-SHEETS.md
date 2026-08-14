# ATTACK SHEETS - the face-off kit (one answer per question, per idea)

Compiled: 2026-08-14 | Purpose: every question a judge can ask, answered before
the stage. Grouped by judge lens (JUDGE-DOSSIERS.md, VERIFIED). Answers are
honest, grounded in our verified numbers, never strawmen.

---

## 0. UNIVERSAL (all 4 ideas)

1. What did you build in the 24 hours?
   A: the skin mount (nouns, seed data, UI labels), the one differentiator, the
   staged failure beat, the deck, the demo. The engine core was pre-verified
   (42/42), the integration is the build. Honest, pre-scripted.
2. Is this production-ready? No, it is a 24h MVP with a verified core and a
   clean architecture. That is the point of a hackathon build.
3. What if the LLM fails? Mode badge on screen: live -> cached -> offline in
   under 2 seconds. Zero uncontrolled dependencies (AFTERPACKETS rule).
4. What data did you use? Golden fixtures (happy/ambiguous/adversarial) plus
   real public data seeded today (event deadlines, notices). Honest about scope.
5. How does it scale? Stateless engine, sqlite, zero deps. Horizontal by design.
6. Security? Consent records, typed approval gate, audit trail, PII handled
   locally. We claim features, never legal compliance (DPDPA framing rule).
7. What does it cost to run? Free: ollama-cloud key, no paid APIs in the demo.
8. Who is the user? One line per idea below.
9. What is the ONE metric? One line per idea below.
10. Why should this win? One line per idea below.

## 1. JUDGE LENS QUESTIONS (ask these to yourself in rehearsal)

Sarthak (ML-validation): training data? baselines? metrics? false-positive rate?
overfitting? error analysis? why this model choice? reproducibility?
Lingaraj (security-depth): threat model? controls? test evidence? residual risk?
authorization? data leakage paths? logging? incident response?
Anjana (safety): who is protected? abuse resistance? privacy? legal exposure?
false-alarm harm? measurable real-world impact? deployment path?
Ayushi (business): quantified outcome? cost reduction? workflow fit? sustainability?
unit economics? who pays?
Sonali (impact): who adopts? why persist? how is value communicated? business model?
beneficiaries? team credibility?
Shivani (data/process): reliable data handling? quality controls? documentation?
what did you learn? what would you do next?

---

## 2. IDEA A BRIEFLENS (agentic ops, Google/Accenture lane)

- User: one professional drowning in inputs (email, chat, tickets, notices).
- Metric: urgent items surfaced with zero missed deadlines in replay tests.
- One-line win: we turn a flood of inputs into one approved action, with evidence
  and a full audit trail, and it works with zero internet.
- Competitor diff: Gmail Gemini/Superhuman summarize; we add the policy gate and
  the audit. An agent that acts without asking is unsafe, an agent that only
  chats is useless. We are the middle.
- Staged failure: LLM dies mid-demo -> offline mode takes over, badge flips,
  ranking still correct (regex dates + tf-idf), recovery under 2 seconds.

## 3. IDEA B KAVACH CIRCLE (multimodal assistant, Meta/Apple lane)

- User: a student or citizen with information in every format (text, image, PDF)
  who needs answers they can trust.
- Metric: answers carry evidence + confidence; high-risk cases escalate to a
  human, never guessed.
- One-line win: every answer shows its sources, every uncertain answer goes to a
  human, and corrections stick for the session.
- Competitor diff: Pixel 9 and Truecaller proved demand for scam detection but
  not Hindi-first consumer workflow with evidence export; ChatGPT answers but
  does not escalate. We fuse both.
- Staged failure: a bad OCR input -> graceful None + reason, confidence UI shows
  low, route to human. The failure path is the demo.

## 4. IDEA C SIGNALSTORY (creative workflow, Adobe lane)

- User: a team making on-brand content from a real brief, fast.
- Metric: brief -> approved asset in minutes, every asset has a provenance card.
- One-line win: generative AI creates fast but uncontrolled; we make it
  controlled: brand rules, review loop, provenance on every asset.
- Competitor diff: Canva/Firefly generate; we enforce brand constraints and
  provenance through an approval loop. The workflow is the product, not the
  generator.
- Staged failure: generator adapter returns off-brand text -> violation caught
  by rule check, human review, regenerated. Provenance card shows the full path.

## 5. IDEA D KAVACH (security lane, real product)

- User: the Hindi-first consumer being targeted by digital-arrest and vishing
  scams, and the family that wants them protected.
- Metric: 5/5 fresh-clone scenarios (KILL/KILL/PAUSE/PASS/PASS), 24 real
  incidents registry, would-have-caught table.
- One-line win: real-time scam-call screening in Hindi, on-device, six detection
  departments fused into one intervention loop, with a signed evidence packet
  for 1930/Chakshu.
- Competitor diff: Truecaller labels, Pixel 9 detects, MuleHunter is bank-side;
  nobody does consumer-side Hindi-first real-time vishing defense with evidence
  export for the digital-arrest victim. Verified gap from 23 research runs.
- Staged failure: a clean call that must NOT be flagged (PASS scenario), then a
  digital-arrest call flagged in under 1 second (KILL). Both in the same demo.

---

## 6. THE THREE WEAKEST SPOTS (pre-scripted, honest)

1. "Did you build this tonight?" (Kavach): the integration + demo harness + this
   round's demo IS the build; the engine loop is genuinely new work. Say it
   straight, then show the audit trail.
2. "Why is this different from Truecaller/Pixel 9?" (any security flavor): name
   them first, then the combination gap: Hindi-first + consumer-side + real-time
   during the call + digital-arrest-specific + evidence export.
3. "Any legal/compliance claim?" (any idea): no. We build consent + audit as
   product features. Never invent DPDPA deadlines on stage.

## 7. THE ASK-BACKS (end of pitch, pick one)

- If you were the sponsor company, which single metric would you watch first?
- What is the one thing you would ask us to cut if this went to production?
- Which of the six judges' lenses should we stress most in the demo?
