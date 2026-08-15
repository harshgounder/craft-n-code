# NIGHT-CHEAT-SHEET-2026.md: the 21:30 quick-mount table (print me)

Built from: WAVE-SYNTHESIS-2026 (12 verified waves), SKIN-KITS-2026,
IDEA-DILIGENCE-2026, PER-TOPIC-BENCHMARKS/STRESS. One line per domain:
kit + fixture + the numbers to quote + the judge attack to pre-answer.

## THE 21:30 PROTOCOL (2 min fingerprint, 10 min tree, 30 s mount)

1. Fingerprint (Harsh, 2 min): company vocab cue table (IDEA-BANK s5).
   Security words ANYWHERE -> KIT-4B overrides everything.
2. Tree (10 min): shape -> kit -> domain row below -> freeze the
   one-line thesis: "[Verb] [outcome] for [person] at [constraint]."
3. Mount (30 s): cp fixtures/<kit>.json fixtures/current.json;
   ./demo.sh. Nouns swapped in deck only.
4. Ammo: grab this sheet's row for the domain + the numbers line.
5. LIVE DATA: feeds.py --refresh, restart --feeds, PRE-WARM 15 min
   before the demo (never cold-boot, 3+ min cold).

## MOUNT CARDS (the 5 kits, full protocol)

KIT-1 (agentic ops / governed router) fixture: kit1_agent.json
- Story: AI ranks email/Slack/tickets into actions; risky actions stop
  at a human-approved policy gate; every step traced. Operator leaves
  this gap open (still research preview, no approval queue, no audit).
- Numbers: HCAST 70-80% <1h vs <20% >4h; MAST 41-86.7% failure; 68%
  prod agents run <=10 steps before human intervention; PocketOS 9 s
  DB+backup delete, 30 h outage (CONFIRMED).
- Judge attack: "this exists" -> Operator/Claude Code are single-app;
  we rank + gate + trace across channels in one place, zero deps.
- Judge attack: "why human approval?" -> HCAST gap line, verbatim.

KIT-4B (fraud guard, OVERRIDE on security words) fixture: kit4_messaging.json
- Story: family WhatsApp room sees a "digital arrest" script; the
  pipeline flags the pattern, the badge shows evidence, a human
  approves the freeze report; one tap submits the 1930 packet.
- Numbers (all VERIFIED wave-10): Rs 4,057 cr / ~3 lakh victims since
  2022; Rs 481.1 cr in Jan-May 2026; AI scams Rs 22,495 cr in 2025;
  1930 helpline 3.28M calls / Rs 11,158 cr frozen; PSBs 74% of loss
  value; 70%+ of entries are WhatsApp-driven.
- Regulator vocab: RBI FREE-AI Sutra 5 ("AI for customer protection"),
  DPIP, Master Directions 2024, Sanchar Saathi/Chakshu, NCRP/I4C.
- Judge attack: "how do you detect deepfake voice <2 s on a mid
  Android?" -> offline analysis + policy gate + honest badge, and the
  eval plan (IEEE-CIS/PaySim corpus, <5% FP target).
- Judge attack: "banks already do this" -> banks are post-hoc (Falcon/
  SAS over 1930); Sutra 5 is the customer-side opening, DPIP is closed
  to students, Neural Defend has no India install base.

KIT-2 (creative provenance) fixture: kit2_creative.json
- Story: campaign briefs from clients; every generated asset carries a
  C2PA-style provenance chain; a human approves before it ships.
- Numbers: Adobe Content Credentials = marquee 2026 (3 pillars, 22 Jan
  2026); C2PA hardware is real (Leica/Sony/Nikon/Canon/S26) but the
  software verification layer is a desert (email/CMS strip metadata).
- Judge attack: "Adobe does this" -> we make verification visible in
  the workflow judges see, with a per-asset evidence panel.

KIT-3 (privacy / DPDPA-ready) fixture: kit3_privacy.json
- Story: lab results and do-not-upload flags; consent-first UX; 72 h
  breach endpoint; everything local-first.
- Numbers: DPDPA Rules notified 14 Nov 2025, obligations from mid-May
  2026; penalties to Rs 250 cr (Rs 500 cr aggravated); breach clock
  72 h; child consent Rule 10; PrivateGPT proved run-time privacy but
  build-time audit (what got chunked, who saw it) is the open gap.
- Judge attack: "DPDPA is a legal layer, not a feature" -> consent UX
  + breach endpoint + provenance are the product; we never claim legal
  compliance, we show the honest badge.

KIT-5 (enterprise router / MSME) fixture: kit5_enterprise.json
- Story: branch loan case routing; governed, tiered approvals; audit
  trace. SME is the white space: Agentforce/Otto are Fortune-500-tuned;
  Accenture + Google Cloud announced mid-market lines in 2026.
- Numbers: 63M MSMEs, 31.1% GDP, 48.5% exports, <5% on accounting
  software; GeM + ONDC (370K vendors, 800+ cities) rails; iStart
  Rs 10K/mo sustenance + Rs 2.4L pre-seed; DPIIT to Rs 200 cr.
- Judge attack: "why not a spreadsheet" -> ranking + evidence + audit
  across 30+ sources in one read; the 5-layer scorecard answer.

## DOMAIN ROWS (25 more, one line each)

edu: KIT-1 | ATL Saathi + DeepMind 56h curriculum exist (Google);
  BEEAR/MMLU-edu bench; openai evals; the "tutor that never lies"
  line = badge honesty.
health: KIT-1/3 | AIIMS x MedGemma + ABDM ABHA rails; MedQA/MedBench/
  MIMIC bench; DPDPA health carve-out; consent-first demo.
fintech/UPI: KIT-4B | UPI 24,161 cr txns FY26, Jul 2026 23.66 bn /
  Rs 29.88L cr; RBI FREE-AI + DPIP vocab; IEEE-CIS/PaySim datasets.
agriculture: KIT-1 | PM-Kisan + AgriStack rails; SIH 2025 agri wins;
  iStart Rajasthan agri agenda; 63M MSMEs incl. farmers.
civic/grievance: KIT-1 | SIH 2024 ministry PS (Social Justice SIH1714,
  Housing SIH1726); GeM/state portal rails; grievance datasets on
  data.gov.in.
creative: KIT-2 | Adobe Content Credentials 3 pillars; D2C India 11K
  cos / 800 funded; C2PA verification desert line.
enterprise ops: KIT-5 | MSME <5% software; GeM AI sellers; ONDC;
  Accenture agentic line; DORA/SRE bench for the ops story.
security: KIT-4B | CSC MUJ identity + NTRO SIH PS; OWASP ASVS/WSTG/
  LLM01-10; CyberSecEval 3; the 81/81 suite IS the security story.
privacy: KIT-3 | DPDPA 3 phases; penalties; consent Rule 10; SDF
  notified status; PrivateGPT build-time gap.
web3: KIT-1 | MCP registry 9,652 + spec dates; tool poisoning class;
  do not lead with blockchain, lead with trust.
hardware/edge: KIT-4B | on-device AI story (Whisper/Phi on 5K phone);
  MLPerf/TinyMLPerf bench; Apple on-device alignment.
gov/citizen: KIT-1 | SIH rails; iStart + Bhamashah/RIICO; DPDPA
  sovereign angle (Gemini Distributed Cloud); ministry vocab.
climate: KIT-1 | HackX environmental track; SIH 2025 drones/SAR;
  Smart Cities Mission; data.gov.in weather endpoints.
HR/people ops: KIT-5 | approval queue UX (7-stage) as the story;
  Glean pause-before-write pattern; audit ring.
legal/compliance: KIT-3/5 | DPDPA + RBI + MeitY 4-pillar stack; RAG
  legal bench (RAGAS/ARES); 72 h breach endpoint.
retail/e-com: KIT-1 | ONDC 370K vendors; fraud datasets (IEEE-CIS);
  idempotency story (Stripe keys) for any money path.
travel/logistics: KIT-1 | FedEx/DHL customs scam ammo (Rs 1,800 cr);
  DHL-customs one-tap report; data.gov.in transport.
media/news: KIT-2 | provenance on every output; deepfake bench
  (AutoDAN/HarmBench + wave-10 family-emergency scam); C2PA line.
social good/accessibility: KIT-3 | Bhashini 22 langs + Vaani 109
  datasets; WCAG 2.2 + axe; Apple accessibility alignment.
devtools: KIT-1 | SWE-bench Verified saturation (96/95.5/95%); the
  "model cannot self-attest" line; external harness story.
meetings/collab: KIT-1 | Operator/Claude Code single-app gap; approval
  UX patterns (Claude Code DENY/ASK/ALLOW, Glean edit-first).
research/academic: KIT-1/3 | FEVER/LIAR datasets; Wikipedia REST
  200 rps keyless; RAGAS/ARES; citation-provenance story.
ai-for-bharat/Indic: KIT-1 | Vaani 109 languages, Gemini Live 25+
  Indic, Bhashini; the differentiation line: "not a GPT clone, it
  speaks the district"; iStart + MeitY alignment.
responsible AI: KIT-1/3 | Accenture CRAIO + Blueprint vocab; NIST AI
  RMF; the honest badge = the governance story.
gaming/entertainment: KIT-2 | provenance for generated assets; C2PA
  line; Meta OpenEnv $30K Bengaluru alignment.
music/audio: KIT-2 | deepfake audio detection bench; AI scams
  Rs 22,495 cr line; on-device latency story.
food/recipe: KIT-1 | ONDC food rails; local + Indic angle; data.gov.in.
smart city: KIT-1 | SIH urban infra PS; Smart Cities Mission; ONDC
  civic vendors; dashboard with data.gov.in feeds.
mcp/ecosystem: KIT-1 | 9,652 servers + 3 spec dates + tool poisoning;
  compose gold-plated servers, never rebuild; 15-line FastMCP. WEDGE
  (idea-lab mock-drop, 13:05 today): approval-gated MCP is the
  least-shipped sub-niche (~52% dead-server share in registries). If
  the PS is shape 6/7/12 flavored, research/MOCK-DROP-20260815.md is
  the parse playbook. GAP: no dedicated MCP deck slide yet, 30-45 min
  fix (deck-gen.js), "MCP" should appear on the cover.
multi-agent: KIT-1 | MAST 14 failure modes / 1,242 traces / kappa
  0.77; our one-controller-2-tools answer; HCAST gap line.

## JUDGE ATTACK ANSWERS (the top 6, verbatim-ready)

1. "How is it tested?" -> 81/81 checks, order-independent, fresh DBs,
   zero LLM judges; multi-run stance (AgentBoard pass@k lesson).
2. "How does it scale?" -> SLOs at p99 (SRE workbook: 90% <100 ms AND
   99% <400 ms); error budget 1h/6h/72h burn; we show the honest
   limits, not fake load.
3. "Why not just use ChatGPT?" -> ChatGPT has no policy gate, no
   evidence panel, no trace, no honest offline badge. The 7-stage
   approval queue is the product.
4. "What if the LLM fails?" -> kill the key live: badge flips to
   offline, feed keeps ranking (THE HONESTY MOMENT); fallback ladder:
   OLLAMA -> OpenRouter :free -> Cerebras 1M tokens -> deep offline.
5. "Is this a real problem?" -> name the number + source: the fraud
   row above, or MSME <5%, or UPI volume. One sentence, one source.
6. "Who adopts it?" -> one rail, one pilot, one quarter: GeM / ONDC /
   ABDM / iStart / a Jaipur mandi. Never "someday, everyone".

## THE 3-MINUTE SCRIPT (wave-14, second-level)

Act 1 (30-45 s): victim + cost in 10 s ("Rs 4,057 crore, 3 lakh
victims, one call"), why now 15 s, why unsolved 15 s.
Act 2 (90-120 s): demo intro 5 s, LIVE demo 70 s (failure-case 20 s ->
success 50 s), credibility line 10 s ("81/81 checks, zero deps, badge
that cannot lie").
Act 3 (30-45 s): one quantified number 20 s, vision 15 s, planted ask
15 s ("Ask us how we tested it").
Recovery line (rehearse 5x): "Let me show you a moment in our test
data that captures exactly what the live system does."
