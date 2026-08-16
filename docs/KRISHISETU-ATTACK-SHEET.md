# KRISHISETU ATTACK SHEET  (PS-07, Craft N Code Round 0)

Compiled 2026-08-16, pitch day. Companion to ATTACK-SHEETS.md (which covers the
four pre-drop ideas). This sheet is for the ACTUAL deck: KrishiSetu, PS-07,
Cyclone and Flood Resilient Smart Agriculture Advisory.

## The one line (repeat under pressure)

"KrishiSetu turns a cyclone forecast into a crop-stage-specific action and an
insurance claim packet, in Odia, on a basic phone. Warnings are infrastructure.
Decisions are the product."

## Universal questions

1. What did you build in 24h?
   A: the engine core was pre-verified (85/85 suites). In the window we mounted
   it on the agri domain: the PS-07 rule seed set, the Odia delivery layer (SMS
   + IVR through simulators), the farm-profile schema, the deck. The integration
   is the build. Honest and pre-scripted.

2. Is this production-ready?
   A: No. It is a 24h prototype with a verified governed core. The IMD feed is
   simulated, SMS and IVR run through simulators, the rule set is a curated seed
   awaiting agronomist review. We say this ON the slide. That is the point.

3. What if the network dies?
   A: that is a feature, not a risk. The advisory queues offline and syncs when
   the tower returns. A cyclone takes the tower with it. We demo exactly that
   beat.

4. What data do you use?
   A: farm profile (crop, stage, plot, soil, connectivity) plus IMD forecast.
   For the demo the IMD feed is a curated seed, clearly labeled simulated. Real
   data is Round 1: live IMD connector and Odia voice.

5. Why not just use Meghdoot or the existing alerts?
   A: Meghdoot sends alerts and agromet advisories. It has no farm profile, no
   staged action, no deadline, no cost of waiting, no claims path. We sit on
   top of the alert rail and turn the warning into a decision. (Prior-art slide.)

6. What does it cost?
   A: the prototype is zero-dep stdlib, free to run. At pilot scale: one FPO,
   one season, measured renewal. The claims rail pays per evidence packet,
   because PMFBY already pays for verified loss events. No consumer-subscription
   fantasy.

7. What is the ONE metric?
   A: claim conversion plus comprehension, not downloads. One FPO, one coastal
   block, measured renewal in one quarter.

8. Why should this win?
   A: the problem is measured (5,428 acres lost in Dana, 5,882 ha salt-affected
   in Yaas). The rail is real (78.4 crore PMFBY applications). We built a
   governed pipeline with an audit trail, not another alert, and we are honest
   about exactly what is simulated.

## Judge lens: ML validation (Sarthak)

- Q: Where is the ML?
  A: Deliberately not ML yet. The advisory is an agronomist-reviewed rule engine
  (pre/during/post × crop × stage × hazard). Rules are auditable and
  correct-by-review. ML is the wrong tool for a 24h prototype of a
  safety-critical decision. ML arrives in Round 1 (crop-stage from satellite,
  demand forecasting) and will be validated against the same A-D evidence
  grades we use today.

- Q: How do you measure correctness?
  A: comprehension tests with extension workers (does the farmer act
  correctly?) and claim conversion on evidence packets. We named that as the
  pilot metric on the market slide.

## Judge lens: security depth (Lingaraj)

- Q: Threat model?
  A: four failure classes: wrong forecast, wrong rule, spoofed advisory, lost
  evidence. Mitigations: every advisory carries source + rule id + deadline
  (verifiable), audit trail per action, evidence packets are signed and dated,
  SMS sender verification in Round 1. The governed pipeline (propose, approve,
  audit) means no action ships without a trace.

- Q: PII?
  A: the farm profile is PII. Handled locally, consent-gated, no cloud
  dependency in the demo. We claim features, never compliance (DPDPA framing
  rule from our own kit).

## Judge lens: safety (Anjana)

- Q: Who is protected?
  A: coastal Odisha smallholders, the people who get the warning but not the
  decision. Asha, 47, flowering paddy, Balasore. 5,882 ha salt-affected, 5,428
  acres lost. The alert leaves these people behind.

- Q: False-alarm harm?
  A: the real risk, and why we chose rules over ML: a wrong action can cost a
  harvest. Every action carries source + deadline + cost of waiting. The rule
  set is human-reviewed before it ships. We stage actions (BEFORE, DURING,
  AFTER) so a farmer gets a sequence to follow, not a single wrong move.

- Q: Deployment path?
  A: OSDMA and the agriculture department (B2G), KVK extension workers (FPO),
  PMFBY insurers (claims rail). Named, not hypothetical.

## Judge lens: business (Ayushi)

- Q: Who pays?
  A: three buyers, one verified loop. FPO + extension (per-verified-advisory
  subscription), B2G district (per-block deployment with auditable outreach
  evidence), claims rail (per evidence packet). The claims rail is the wedge:
  PMFBY already pays for verified loss events.

- Q: Unit economics?
  A: one FPO, one season, measured renewal. No TAM multiplication. The slide
  says it: named rail, named pilot, dated outcome.

## Judge lens: impact (Sonali)

- Q: Why will farmers adopt?
  A: because it is in Odia on a basic phone and it tells them what to do, not
  that something bad is coming. Adoption rides the extension workers who
  already visit, and the insurance claim that already pays.

- Q: How is value communicated?
  A: voice-first, staged, with a deadline and a fallback. The farmer's job is to
  act, not to read a dashboard.

## Judge lens: data/process (Shivani)

- Q: Data handling?
  A: farm profile + IMD forecast + agronomist rule pack. Golden fixtures
  (happy, ambiguous, adversarial) verified 46/46 order-independent. Every claim
  in the deck traces to a dated source (proof ledger P1-P6).

- Q: What did you learn?
  A: the alert is not the gap; the decision is. And the insurance rail is
  bigger than the agri-tech consumer market everyone else is chasing.

- Q: What next?
  A: live IMD connector, Odia TTS and IVR on real infrastructure, agronomist
  review of the seed set, one pilot block.

## The honesty card (use it, do not hide it)

"One limitation, stated openly: the rule set is a curated seed awaiting
agronomist review; the IMD feed and telecom delivery are simulated; nothing is
sent over live SMS or WhatsApp."

Every probe that lands on a simulated part of the system gets this line FIRST,
then the Round 1 plan. Faculty reward the team that knows exactly what its
prototype is not. It is the same move the close slide makes: grade our decision
quality.
