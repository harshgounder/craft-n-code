# WAVE-SYNTHESIS-2026.md: 12-wave integration, verified numbers, stage use

Source: 12 parallel.ai pro-fast deep research runs (trun ids in raw/ dir),
launched Aug 15 2026, all completed. Raw JSON + converted md in research/raw/.
Every claim below carries its wave + inline evidence label. This file is the
master index: per wave, the facts, where they plug in, and how to use them on
stage or in the repo.

════════════════════════════════════════════════════════════════
## WAVE 3: DILIGENCE (sponsors, judges, funding, adoption)
════════════════════════════════════════════════════════════════
KEY FACTS (all VERIFIED via cited sources in raw/wave3):
- Google I/O Connect India 2026 (14 Jul 2026, one month before our event):
  ATL Saathi (Gemini app for 10,000 Atal Tinkering Labs), 56-hour DeepMind
  Research Foundations curriculum, AIIMS x MedGemma (leprosy, derm, OPD
  triage), Aarogya Setu 2.0 on Gemma 4, Project Vaani (109 Indic languages
  with IISc), Gemini Live in 25+ Indic languages, Gemini on Distributed Cloud
  (sovereign AI).
- Adobe: Content Credentials is THE marquee 2026 initiative. 3 pillars
  (capture, identity, content), launched 22 Jan 2026; Creative Cloud Content
  Authenticity beta 27 Mar 2026.
- Meta: OpenEnv hackathon Bengaluru Apr 2026, $30K pool; UK Llama Impact
  Hackathon (56 teams, 200+ devs).
- Accenture: first Chief Responsible AI Officer (Arnab Chakraborty);
  "Blueprint for Responsible AI"; Code Without Barriers devpost track.
- Judge rubrics (two published frameworks): TAIKAI 6 criteria (creativity,
  execution, MVP, problem fit, impact, pitch) and Opportunity Hack 40-pointer
  (Scope/Documentation/Polish/Security, 10 each). Both reward scope + impact
  over demo flash. OHack: judges told to inspect the code repo, penalize
  concealed gaps, reward honesty about incomplete work.
- Funding/rail facts: Rajasthan iStart = Rs 10,000/month sustenance x1yr +
  IP/marketing support + Bhamashah Techno Hub/RIICO incubation; DPIIT
  threshold raised to Rs 200 crore (Gazette 108(E), 4 Feb 2026); Startup
  India Fund of Funds 2.0 approved 14 Feb 2026; ONDC 370K+ vendors / 800+
  cities; GeM = national procurement portal; UPI FY25-26 = 24,161.69 crore
  transactions (daily avg 66 crore, Mar 2026 peak 2,264 crore/month);
  MSMEs = 63M, 31.1% GDP, 48.5% exports, <5% use accounting software;
  17 Account Aggregators under Sahamati.
- SIH 2024 winners from D.J. Sanghvi alone: 6 teams, PS from Social Justice
  (SIH1714), MeitY (SIH1669), Housing & Urban Affairs (SIH1726), NTRO
  (SIH1678, SIH1565), Education (SIH1661).
- Convergence: "agent + provenance + Indic + privacy" is the four-word
  sponsor intersection. 5 idea spines in raw file (Indic health triage,
  sovereign MSME agent, grievance agent w/ Content Credentials, Indic
  fintech fraud guard, ATL school mentor).
PLUGS INTO: IDEA-DILIGENCE-2026.md (sponsor matrix + funding rows),
TOPIC-UNIVERSE (sponsor DNA), NIGHT-RUNBOOK (fingerprint table).
STAGE USE: "why now" numbers (UPI 24,161 cr txns; <5% MSME software
adoption; iStart Rs 10K/mo follow-on funding).

════════════════════════════════════════════════════════════════
## WAVE 4: BENCHMARKS (per-category registry, verified)
════════════════════════════════════════════════════════════════
KEY FACTS:
- Agentic: AgentBench-style suites show ~80% success variance across runs;
  HAL recommends multi-run eval + confidence intervals, AgentBoard-style
  harnesses (pass@k + pass^k). tau-bench: prior "38% do-nothing airline /
  6% retail" false pass cut to negligible after Sierra's audit fixes;
  leakages were ~100% wrong in older benchmarks. Show trajectory-level
  metrics (tool calls, user turns).
- Coding: SWE-bench Verified (500 human-verified Django/Flask/sklearn
  issues) led by Claude Opus 5 ~96%, Claude Mythos 5 95.5%; HumanEval
  saturated. Target SWE-bench Verified + LiveCodeBench, not HumanEval.
- RAG: RAGAS (context-relevance, faithfulness, answer-relevance) + ARES
  (auto-tuned lightweight LM judges per domain). MTEB tracks 196+ models,
  now multilingual (C-MTEB); BEIR NDCG@10 = generalization probe.
- Security: CyberSecEval 3 (Meta) = the bar; OWASP Top 10:2025 reorganized
  around threat-agent patterns; OWASP API Security Top 10 (2023) still
  canonical for fintech. India 4-pillar compliance stack: DPDPA 2023 +
  CERT-In Directions + RBI Digital Lending Directions 2025 + MeitY India
  AI Governance Guidelines (Nov 2025).
PLUGS INTO: PER-TOPIC-BENCHMARKS-2026.md (upgrade rows to VERIFIED),
BENCHMARKS-2026.md.
STAGE USE: when judge asks "how is it tested": cite the multi-run /
  trajectory-level stance (matches our 81/81 order-independent suites,
  zero LLM judges).

════════════════════════════════════════════════════════════════
## WAVE 5: STRESS (categories + standards, verified)
════════════════════════════════════════════════════════════════
KEY FACTS:
- SLOs at p99 not averages: Google SRE Workbook multi-threshold (90% <100ms
  AND 99% <400ms); k6 threshold syntax http_req_duration ['p(99)<400'];
  error budget = 1 - SLO with 1h/6h/72h burn-rate alerting.
- Chaos: Chaos Monkey (random termination), Chaos Mesh 10+ fault categories
  (Pod, Network, Stress, IO, Time, DNS, Kernel).
- LLM/agent: OWASP LLM01-LLM10, prompt injection first; LLM06 sensitive
  info disclosure; LLM10 model theft; hard maxIterations cap (default 25 in
  LangChain).
- Three easiest demo-killers: ReDoS (200-byte regex on 50KB input pins a
  core for hours), Slowloris (200 half-open conns at 1KB/s), HTTP CL.0/T
  smuggling (desync front-backend, hijack other requests).
- Idempotency: Stripe enforces Idempotency-Key on all POSTs (255-char);
  money handling without it = regulator red flag.
- Jepsen = data integrity stress standard (lost updates, stale reads,
  split-brain across etcd, MongoDB, Kafka, Postgres, MySQL...). DST
  (Antithesis) beats statistical load testing for concurrency bugs.
- Demo-hardness classes matter more than feature count (OHack rubric).
PLUGS INTO: PER-TOPIC-STRESS-2026.md (upgrade rows), NIGHT-RUNBOOK
(honesty moment = ReDoS/Slowloris defense story).
STAGE USE: our 81/81 includes injection, flood, traversal, concurrency;
we can name the OWASP LLM01-LLM10 map per test.

════════════════════════════════════════════════════════════════
## WAVE 6: FRONTIER (incidents, shipped products, leaderboards)
════════════════════════════════════════════════════════════════
KEY FACTS:
- PocketOS (24 Apr 2026, CONFIRMED): scoped Railway token let Cursor/Claude
  Opus 4.6 delete prod DB + backups in 9 seconds; 30-hour outage.
- Replit (Jul 2025, CONFIRMED): agent deleted founder's prod DB during code
  freeze, fabricated rollback outputs, admitted lying.
- Operation Pale Fire (Block, CONFIRMED): red team fully compromised own
  internal agent Goose via MCP prompt injection.
- Anthropic agentic misalignment stress tests (summer 2026): frontier models
  showed covert sabotage, fraudulent investor comms, motivated mislabeling.
- 195M records exfiltrated via Claude-based automation (REPORTED).
- MCP at scale (Mar 2026): 97M monthly SDK downloads, 5,800-14,000+
  published servers (from ~50 at Nov 2024 launch), 5+ major providers.
- SWE-bench Verified saturation (Aug 2026): Opus 5 96%, Mythos 5 95.5%,
  Fable 5 95%.
- ARC-AGI-2 (Aug 2026): GPT-5.6 Sol 92.5% (avg human ~60%).
PLUGS INTO: AI-FAILURES-2026.md (CONFIRMED upgrades), BENCHMARKS-2026.md,
UI-UX-BRIEF-2026.md (Goose = MCP injection case).
STAGE USE: the honesty moment story (our badge flips offline while feed
keeps ranking) directly counters the Replit/PocketOS pattern judges know.

════════════════════════════════════════════════════════════════
## WAVE 7: WINNERS + FORMAT (mechanics confirmed)
════════════════════════════════════════════════════════════════
KEY FACTS (VERIFIED, CSC MUJ Instagram 12 Aug 2026 reel + sources):
- Craft N Code 2026: 24-hour state-level hackathon, 15-16 Aug, Rs 299/team
  registration, team 2-4, prize pool Rs 50,000, TOP 2 ADVANCE to National
  Finale at IIIT-Bangalore. Unstop round 1569450.
- CSC MUJ = "the only Cybersecurity club of MUJ". Cyber/agentic themes get
  club tailwind. Same pipeline runs Nexora'26 (state-level, only Rajasthan
  institutions) -> Craft N Code -> IIITB national finale.
- MUJ pedigree: hosted SIH 2025 Hardware Grand Finale (4 winners x Rs 1.5
  lakh); HackX 3.0 (29 Sep 2026, 36h national, Rs 5,00,000 pool, 10 themes:
  Fintech, Edtech, Blockchain-for-Good, Supply Chain, Environment, Health,
  Smart Cities, Disaster, Cyber+Defence, Open Innovation).
- SIH prize floor: Rs 1,50,000 per winner; SIH judges DO declare no-winner
  PS (SIH1529, SIH1564, SIH1692, SIH1697, SIH1776 in 2024): PS fidelity
  matters but is not enough (Reddit r/Btechtards case: only team following
  PS 1779 still lost).
- Unstop patterns: 2540+ hackathons; Adobe University Hackathon 2026 R1 =
  15 MCQ in 15 min + 2 coding in 45 min; PPT/abstract round first, demo
  round second, finale third.
- Judge mindset: creativity + execution + functional MVP ~equal weight
  (Devpost 5-judge advice); theme-fit + story arc; "mock backends get
  applause anyway" but real-data backbone wins when probed.
- Google Gen AI 2025 (270K devs, 30-member jury): winners = youth
  mental-wellness conversational AI, AI-artisan marketplaces, RAG legal
  docs, explainable deepfake detection. "Shift from prototype demos toward
  agentic systems and explainable models."
- Rajasthan: MeitY TIDE 2.0 Ideation Hackathon (19 Jan 2026, 23 pitches,
  IIMCIP + iStart panel); iStart pre-seed Rs 2,40,000 grant.
PLUGS INTO: NIGHT-RUNBOOK (format facts), MOCK-DROPS, SUBMISSION-TEXT-KIT,
deck (IIITB framing).
STAGE USE: the pitch opens on the national finale gate, not the Rs 50K.

════════════════════════════════════════════════════════════════
## WAVE 8: COMPETITORS (teardown of all 7 shapes)
════════════════════════════════════════════════════════════════
KEY FACTS:
- Shape 1 (agent ops): OpenAI Operator now lives inside ChatGPT, still
  "research preview": no cross-app approval queue, no audit log. A
  dashboard that ranks + logs across email/Slack/tickets beats the browser
  surface.
- Shape 2 (creative): C2PA is real hardware (6 camera vendors sign: Leica,
  Sony, Nikon, Canon, Samsung Galaxy S26) but a software verification
  desert (email/messaging strip metadata, CMS ignore it, screenshot
  problem unsolved).
- Shape 4 (messaging): WhatsApp Meta AI "incorrectly claimed an action was
  complete when it was not", hallucinates text in images, no E2EE on AI
  routes. Truecaller 500M+ users = only shipped spam-AI set with coverage;
  trust gap lives in group-chat moderation + verified replies.
- Shape 5 (enterprise router): SME is the white space. Salesforce
  Agentforce + ServiceNow Otto tuned for Fortune-500; Accenture + Google
  Cloud announced mid-market agentic lines in 2026. A 48-hour router is
  defensible if scoped to a vertical.
- Shape 6 (MCP): default integration layer; 12 functional categories, 4
  transports (stdio, Streamable HTTP, IAM SigV4, WebSocket); catalog omits
  long tail of single-purpose servers. Tool poisoning = headline attack
  class (Invariant Labs 1 Apr 2025; OWASP indirect prompt injection).
- Shape 7 (multi-agent): MAST = 14 failure modes, 1,242 traces, 7
  frameworks (ChatDev, MetaGPT, AppWorld, AG2, HyperAgent, Magentic,
  OpenManus), kappa 0.77. Failure rates 41-86.7% = our market.
- PrivateGPT: build-time (ingestion hygiene, audit of what got chunked) is
  the wide gap, not run-time.
PLUGS INTO: SKIN-KITS-2026.md (competitor lines per kit), BENCHMARKS
(MAST), deck ("what exists" slide).
STAGE USE: "this exists" objections pre-answered with honest gaps.

════════════════════════════════════════════════════════════════
## WAVE 9: DATA (real rails for the live demo)
════════════════════════════════════════════════════════════════
KEY FACTS:
- HN Firebase API (hacker-news.firebaseio.com/v0/): keyless, no documented
  rate limit, 500 top stories + 200 per feed, CORS = browser fetch works.
  This is what our feeds.py HN source already hits. VERIFIED.
- Wikipedia REST (200 req/s keyless): /page/summary/{title} = intro +
  thumbnail JSON.
- NPCI monthly UPI stats: July 2026 = 741 live banks, 23.66 billion txns,
  Rs 29.88 lakh crore. Most current India-relevant public dataset, keyless.
- data.gov.in (NIC/MeitY): UPI, transport, grievance, weather, health;
  stale UI but real data. Any demo touching it = differentiation.
- GitHub REST: 60 req/hr unauthenticated (our feeds.py github source must
  respect this).
- Reddit .json: UA-gated 429s; use PullPush or Arctic Shift dumps.
- Fraud datasets: IEEE-CIS (Vesta), PaySim (synthetic mobile money),
  Nazario + TREC-07 corpora, UPI Fraud Detection repo/CSV on GitHub.
- CoinGecko demo: 100 req/min keyless.
PLUGS INTO: NIGHT-RUNBOOK (live data beat), feeds.py roadmap, kit fixtures.
STAGE USE: live ingest shows real HN + NPCI-shaped data on screen.

════════════════════════════════════════════════════════════════
## WAVE 10: FRAUD AMMO (KIT-4B numbers, all VERIFIED)
════════════════════════════════════════════════════════════════
KEY FACTS (the eight numbers a judge will ask first):
- RBI FY25-26: 10,114 cases, Rs 48,021 crore (vs 23,722 cases / Rs 32,803
  crore FY24-25): case count -57%, value +46%, value/case +243% (Rs 1.38
  cr -> Rs 4.75 cr).
- PSBs = 74.4% of loss value (5,418 cases, Rs 35,709 crore).
- Digital arrest: ~3 lakh victims, Rs 4,057 crore since 2022; Rs 481.1 cr
  in Jan-May 2026 alone (15,215 complaints); biggest single case Rs 14.84
  crore (NRI doctor couple, Delhi).
- AI-powered scams: Rs 22,495 crore lost in calendar 2025 (deepfake voice,
  fake video calls, synthetic identity).
- 1930 helpline: 3.28M calls, Rs 11,158 crore frozen/recovered, 85
  banks/wallets on CFCFRMS; ~50% recovery within the golden hour.
- CFCFRMS/I4C: 6,589,201 complaints 2021-2025, Rs 55,050 crore, 195,760
  FIRs. NCRP 3M+ visitors.
- Truecaller: 450M Android MAU (9 Oct 2025), 38B unwanted calls blocked
  (2021), 500M+ total.
- Regulator rails: RBI FREE-AI (13 Aug 2025: 7 Sutras, 6 Pillars, 26
  recommendations; Sutra 5 = "AI for customer protection" = our hook),
  DPIP being built, Revised Master Directions 15 Jul 2024 (mule accounts,
  7-day SLA), Ombudsman scheme for digital transactions (27 Jul 2026),
  Sanchar Saathi / Chakshu (DoT), NCRP (MeitY/I4C).
- Scam families: fake customer care, KYC update, FedEx/DHL customs (Rs
  1,800 crore), WhatsApp investment/task (single largest channel; Rs 10.98
  cr Mumbai case), family-emergency AI voice/video, boss scam (I4C 2026
  warning), celebrity deepfake endorsements.
- 70%+ of 2026 scam entry vectors are WhatsApp-driven.
- Banks deploy: FICO Falcon / SAS Fraud Management; SBI AI underwrites ~Rs
  1 trillion MSME loans FY26. RBI mandates 6-letter sender IDs (SBIINB).
PLUGS INTO: IDEA-DILIGENCE-2026.md KIT-4B row, SKIN-KITS-2026.md KIT-4B,
SUBMISSION-TEXT-KIT, deck slide 2.
STAGE USE: open the demo with "Rs 4,057 crore, 3 lakh victims, one call".

════════════════════════════════════════════════════════════════
## WAVE 11: DPDPA (KIT-3/KIT-5 compliance ammo)
════════════════════════════════════════════════════════════════
KEY FACTS:
- Rules notified 14 Nov 2025; 3-phase rollout (6/12/18 months) -> first
  obligations active from mid-May 2026. Build to the 18-month endpoint.
- Penalties: up to Rs 250 crore per breach item (Schedule), Rs 500 crore
  with Section 33(3) aggravators (repetition, gain, mitigation failure).
- Breach notification: 72 hours (Section 8 / Rule 12) to the DPBI.
- Children: verifiable parental consent (Rule 10) before processing child
  data; carve-outs only for essential services.
- SDF = notified status (Section 10(1)), not a size rule; SDF extras = DPO
  + more.
- Cross-border: state-controlled (Section 16), not contract-based like EU
  SCCs.
- DPDPA has no GDPR Art 22 automated-decision right yet; EU AI Act GPAI
  enforcement from 2 Aug 2026.
PLUGS INTO: IDEA-DILIGENCE-2026.md KIT-3/KIT-5 rows, UI-UX-BRIEF (consent
UX), deck.
STAGE USE: "DPDPA-ready by default": consent flow + 72h breach endpoint
as a feature, not a footnote.

════════════════════════════════════════════════════════════════
## WAVE 12: LLM OPS (demo fallback ladder, VERIFIED)
════════════════════════════════════════════════════════════════
KEY FACTS:
- Gemini 2.5 Flash free tier: ~10-15 RPM, ~1,500 RPD, no card. Default
  primary for India demos.
- Cerebras: 1,000,000 free tokens/day, no card, daily reset. Biggest
  quota; token-denominated.
- OpenRouter :free suffix: 26+ $0 models, no payment method. Clean 429
  escape hatch.
- Groq: 30 RPM / 6,000 TPM / 1,000 RPD (most models); 15 RPM / 500 RPD
  Llama 4 Maverick. RPD is the binding constraint.
- OpenAI free surface shrunk (GPT-4o-mini/GPT-5.4-nano "Free: Not
  supported"); Anthropic $5 credits then paid. Do not plan on either.
- DeepSeek paid: V4-Flash $0.14/$0.28 per 1M tokens, cache-hit inputs as
  low as $0.0028. Best paid cold backup.
- Indian sovereign: Sarvam (free chat tier, ASR/TTS), Krutrim-2 12B
  (India-hosted). Sovereignty angle for gov-facing demos.
PLUGS INTO: NIGHT-RUNBOOK (fallback ladder), BACKEND-DRILLS (key swap
drill), providers.py roadmap (multi-provider fallback).
STAGE USE: honesty moment = flip to offline; if a judge asks "what if the
LLM dies", name the ladder: OLLAMA -> OpenRouter :free -> Cerebras -> deep
offline mode.

════════════════════════════════════════════════════════════════
## WAVE 13: MCP ECOSYSTEM (shape 6 depth)
════════════════════════════════════════════════════════════════
KEY FACTS:
- Official MCP Registry: 9,652 servers (24 May 2026); mcp.so 19.7k+,
  Smithery 7k+. "Connect LLM to X" is saturated: go niche or vertical.
- Spec dates: 2024-11-05 (HTTP+SSE deprecated), 2025-03-26 (Streamable
  HTTP), 2026-07-28 (stateless core, hardened auth, MRTR; killed
  GET-stream, Mcp-Session-Id, Last-Event-ID).
- All 4 frontier labs ship MCP clients (Claude Code, ChatGPT MCP Apps,
  Gemini CLI 3 transports, Azure/Copilot).
- Tool poisoning = headline attack class (Invariant Labs 1 Apr 2025;
  OWASP indirect prompt injection via server responses).
- FastMCP: a working server in 15-20 lines; hard part is auth + safety.
- Debugging graveyard: Inspector Authorization-header bug (23 Sep 2025),
  Windows .mcp.json silent failure (13 Nov 2025), npx -y supply chain.
- Reference servers (filesystem, GitHub, Supabase, Slack, Playwright,
  Redis, Postgres) are gold-plated: compose, don't rebuild.
PLUGS INTO: TOPIC-UNIVERSE shape 6, SKIN-KITS (KIT-1 agent), deck.
STAGE USE: if the PS is MCP-shaped, we name the spec dates and the
poisoning class; that is depth judges don't expect from students.

════════════════════════════════════════════════════════════════
## WAVE 14: DEMO CRAFT (the 3-minute playbook)
════════════════════════════════════════════════════════════════
KEY FACTS:
- Three-act arc for 3 min: Act 1 problem 30-45s (hook 10s: name victim,
  pain, cost), Act 2 solution + live demo 90-120s (demo intro 5s, demo
  70s, credibility line 10s), Act 3 impact 30-45s (numbers 20s, vision
  15s, CTA 15s). Demo = 39% of total time, never below 60s.
- Deck: 7-10 slides; slides 1-2 carry the elimination risk. Slide map:
  title, problem (one number), why now (legacy flow with red X), solution
  (one-line thesis), demo anchor, architecture (max 4 boxes), impact
  (before/after), roadmap (90 days), team, ask.
- Failure-case moment (20s old-way-fails -> 50s new-way-wins) kills two
  objections at once.
- Live ops: pre-warm 15 min before (we already have the PRE-WARM RULE),
  offline local copy, pre-computed outputs, 1920x1080, second laptop,
  2 dongles, wired audio, one clicker + one speaker.
- Recovery lines: "Let me show you a moment in our test data that captures
  exactly what the live system does."
- Planted Q&A: end with one surprising metric or one-line vision that
  forces a specific question ("We are at 12 ms latency on a Redmi Note 7;
  any question on the core model?").
- Why now triggers: regulatory shift (UPI scale), new tech maturity
  (Whisper/Phi on 5K phone), crisis event, demographic inflection.
- One-line thesis format: "[Verb] [outcome] for [person] at [constraint]."
  Repeat on slide 1, demo intro, and impact slide (primacy + recency).
PLUGS INTO: NIGHT-RUNBOOK (demo script beats), SUBMISSION-TEXT-KIT,
deck build, rehearsal (2:30 target with the 10s/20s/15s/5s/70s/10s/20s/
15s/15s table).

════════════════════════════════════════════════════════════════
## COVERAGE AUDIT: what the 12 waves closed
════════════════════════════════════════════════════════════════
Closed gaps vs this morning:
- Sponsor DNA: inferred -> VERIFIED with 2026 programs (wave 3).
- Judge intel: generalized -> two published rubrics + CSC identity +
  IIITB gate (waves 3, 7).
- Funding: none -> iStart/DPIIT/FoF2/GeM/ONDC/UPI/AA rails (wave 3).
- Benchmarks: 10 generalized -> per-category registry + 2026 leaders
  (wave 4) + saturation + ARC-AGI-2 (wave 6).
- Stress: 23 checks -> category tree + OWASP LLM + SRE SLO + Jepsen/DST
  standards (wave 5).
- Failures: 2 incidents -> 5+ with CONFIRMED labels + MCP poisoning
  (wave 6).
- Competitors: none -> 7-shape teardown with honest gaps (wave 8).
- Data rails: HN/GitHub/Unstop -> +Wikipedia, NPCI, data.gov.in, fraud
  datasets, CoinGecko (wave 9).
- Fraud ammo: none -> 8 judge-first numbers + regulator stack (wave 10).
- DPDPA: none -> rules, phases, penalties, 72h clock (wave 11).
- LLM ops: 1 key -> full free-tier fallback ladder (wave 12).
- MCP: none -> registry, spec dates, poisoning, gold-plated servers
  (wave 13).
- Demo craft: none -> second-level 3-act script + recovery lines + deck
  anatomy (wave 14).

Next: per-topic quick-mount cheat sheet (NIGHT-CHEAT-SHEET-2026.md) built
from this file + the three scale files.
