# SUBMISSION TEXT KIT - copy-paste ready for both gates

Compiled: 2026-08-14 20:30 IST | Purpose: every submission field pre-written so
the night is paste + submit, not write-at-5am. Two gates:
- ROUND 0 (organizer msg 19:23 IST): ONLINE, drop 22:00, submission = PPT AND Prototype BOTH. Evaluated by IIIT Bhubaneswar faculty. Midnight surprise. Gates below are the OLD format, verify live at 22:00.
- Unstop round 1569450: PPT (pdf/pptx, max 50MB), v1 at 23:00, final 05:00, closes 06:00
- Club site (cscmuj.com / craftncode.dev form): repo_url (required) + pitch (1-2000 chars) + demo_url (optional), v1 before 06:00, final before 09:00 freeze

## V2 ADDITIONS (Aug 15, after the 17-wave research round)

THE EVALUATOR CLOSING LINE (use as the final line of ANY pitch):
"Most hackathon entries ship agents. Very few ship evaluators that
score whether the agents behave. We ship 81 automated checks, zero LLM
judges, a trace for every step, and a mode badge that cannot lie."
(Source: wave-16 synthesis, the generative vs evaluative tension.)

FORMAT FACTS (verified, cite if asked): 24-hour state-level hackathon,
Rs 299 entry, 2-4 person teams, prize pool Rs 50,000, top 2 advance to
the national finals at IIIT Bhubaneswar (Oct 30 - Nov 1). Cyber Space
Club MUJ runs the state qualifier; cybersecurity is the club's
identity, security-shaped builds sit in the judges' center of mass.

FRAUD KIT NUMBER BLOCK (only if the mounted idea is fraud-shaped):
1,23,672 digital-arrest complaints and Rs 1,935.5 crore lost in 2024
alone; Rs 4,057 crore lost to digital arrest since 2022 across 3 lakh
victims; I4C blocked 59,000 WhatsApp + 1,700 Skype accounts; RBI
disabled the UPI collect feature on 1 Oct 2025; the 1930 helpline
saved about Rs 11,158 crore across 3.28M calls. All cited in
research/raw/wave10-fraud.md.

HONESTY LINE (if the LLM dies mid-demo): "The provider rate-limited
us. The badge flipped to offline, the feed kept ranking, the approval
flow kept working. That is the product." (429 WATCH, runbook)

- IDEA A BriefLens: "The one action that matters drowns under noise; BriefLens
  ranks it, proves it with evidence, and waits for a human to approve."
- IDEA B Kavach Circle: "Every format in, evidence out, and a human for the
  risky calls."
- IDEA C SignalStory: "From a one-line brief to an on-brand asset, with a
  provenance trail a reviewer can trust."
- IDEA D Kavach: "A scam call dies in under a second, on the user's own phone,
  in their own language."
- Any idea, generic fallback: "AI proposes, humans approve, everything is
  audited, and the demo works with zero internet."

## PITCH TEXT, IDEA A (BriefLens, agentic ops) - 1,197 chars, safe under 2000

Inputs arrive from everywhere: email, chat, portals, tickets, documents. The
one action that matters, a deadline, an approval, a payment, drowns under the
noise. An AI agent that acts without asking is unsafe; one that only chats is
useless. BriefLens is the middle path: it ingests every channel, deduplicates,
summarizes each item in one line, ranks by profile and deadline, and turns
concrete items into proposals. Every proposal carries evidence: source, date,
amount. A human presses approve, reject, or snooze. Every decision is audited:
who, when, what. A semantic search answers questions with sourced answers, not
hallucinations. Built as a zero-dependency pipeline that runs live with an LLM
or fully offline with deterministic rules, with a visible mode badge. Verified
by 81 automated acceptance checks, order-independent, fresh databases every
run. Demo: digest reads two urgent actions, approve one, audit trail updates,
ask a question, get a sourced answer. The engine is domain-agnostic and mounts
any workflow in under an hour. AI proposes, humans approve, everything is
audited. That is the trust model enterprise work needs.

## PITCH TEXT, IDEA B (Kavach Circle, multimodal assistant) - 1,196 chars

Information arrives in every format: text, images, PDFs, chat. Generic
assistants answer confidently even when they are wrong, and there is no
escalation when it matters. Kavach Circle accepts text, image, and PDF input,
extracts structured facts, and answers with an evidence panel and a confidence
band on everything. When a question is uncertain or high-risk, it visibly
routes to a human reviewer instead of guessing. Users can correct the model
and the fix is remembered for the session. Built on a zero-dependency
pipeline: runtime-detected extractors for PDF and OCR that degrade gracefully,
a live LLM mode and a deterministic offline mode, and a visible mode badge so
judges always know what is real. Verified by 81 automated acceptance checks,
order-independent. Demo: drop a screenshot and a PDF, both get extracted with
sourced facts, ask a question and get a confidence band, ask something risky
and watch the escalation to a human, correct an answer and see the fix apply.
Human-in-the-loop is not a slogan here, it is the architecture: extraction,
evidence, escalation, correction, audit. Every claim has a source, every risk
has a human, and the whole thing runs on any laptop with no external
dependencies.

## PITCH TEXT, IDEA C (SignalStory, creative workflow) - 1,198 chars

Making content is slow; making content that stays on-brand is slower.
Generative AI creates fast but uncontrolled: wrong brand, wrong facts, and
nobody can answer where an asset came from. SignalStory turns a one-paragraph
brief into brand-consistent assets with a full review loop. Paste a brief, the
system extracts brand rules, tone, and audience. A labeled generator adapter
produces the asset, captions, and alt text. A human approves before anything
is delivered. Every asset carries a provenance record: prompt, model,
timestamp, reviewer, so lineage is always answerable. Export to multiple
formats: text, image card, PDF. The generator adapter is swappable: live model
when credentials exist, honest mock when they do not, and the provenance layer
is the differentiator either way. Built on a zero-dependency pipeline with a
visible mode badge, verified by 81 automated acceptance checks. Demo: paste a
one-paragraph brief, watch brand and tone get extracted, generate an asset,
edit and regenerate, reviewer approves, provenance card shows the full
lineage. On-brand, on-time, and accountable: that is what enterprise
creativity needs from AI.

## PITCH TEXT, IDEA D (Kavach, call security) - 1,196 chars

Scam calls are India's most personal cyber threat: digital arrests, bank
fraud, fake KYC, and the victim is on the call, alone, in the moment. Kavach is
a real-time call-screening platform that fuses six detection departments into
one intervention loop: scam keywords, number reputation, voice stress, social
engineering patterns, and more. It works during the live call, in Hindi and
Hinglish first, on the user's own phone. When a scam is detected, the AI
proposes an intervention and the user approves it, every step consented and
audited, and the session exports a signed evidence bundle usable for police
complaints via 1930 or Chakshu. Built and tested over multiple rounds with a
fresh-clone verification of 5/5 scenarios and 14/14 ad-hoc checks, plus a
real-incident registry of 24 cases across 4 scam families. For this round we
built the integration: the engine's proposal-approval-audit loop wired into
Kavach's intervention flow, so AI proposes, humans approve, and everything is
traceable. Demo: a simulated digital-arrest call is flagged in under a second,
intervention proposed, user approves, post-call report generated. This is the
safety layer India's phone users do not have.

## README-as-pitch (club site repo_url opens the README first)

The scaffold README already reads as a pitch: what, why, verified numbers,
demo command. Before first submit, append one paragraph chosen from the pitch
above matching the chosen idea, plus the one-sentence story at the top.
Do NOT rename the repo on the night; the URL is the URL.

## demo_url PLAN

demo_url is optional on the club form. If a demo video exists (team records
tonight or tomorrow), host it: YouTube unlisted (fastest, reliable at the
venue) and paste the link. If no video exists yet, leave the field empty;
repo_url + pitch + live demo at 09:00 still lands.
