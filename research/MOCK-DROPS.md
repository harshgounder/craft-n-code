# MOCK DROPS - practice problem statements + the drill

Compiled: 2026-08-14 20:30 IST | Purpose: simulate the 21:30 drop BEFORE the
drop. We never measured the skin mount (the playbook claims 15-40 min, an
unverified number). This drill turns that claim into a measured fact, and
gives the team muscle memory for the decision tree. Written in sponsor voice
using the cue table vocabulary (IDEA-BANK section 5).

## HOW TO RUN THE DRILL (30-60 min, team)

1. One person is the timer + judge. Read ONE mock aloud, exactly once.
2. Team does the real protocol: fingerprint scan (2 min target) -> decision
   tree (10 min target) -> freeze one-sentence story -> pick deck + storyboard
   -> mount the skin (seed data + UI labels) -> ./demo.sh -> note the time.
3. Judge records: fingerprint time, decision time, mount time, gaps found,
   arguments the team had (those arguments are gold, they reveal uncertainty).
4. After each mock: 5 min retro. Fix anything that was missing. Move on.
5. Run all 5 if possible, minimum 3 (mocks 1, 2, 4 cover the setter prior).
6. Do NOT read the expected answer until the team has committed.

## MOCK 1 - Google flavor (agents, tools, deadlines, grounded answers)

"Build an AI agent system for a busy professional. The system must ingest
work items from multiple channels (email, chat, tickets, documents),
deduplicate them, summarize each in one line, and rank them by urgency and
deadline. For concrete items it must propose actions with evidence attached
(source, deadline, amount). No action may execute without human approval,
and every decision must be logged in an audit trail. The agent must answer
questions about its own work with grounded answers, not guesses."

Expected: fingerprint Google/Accenture. Decision tree -> IDEA A BriefLens,
deck-agentic, storyboard A. Acceptance test: every answer has evidence + an
action, approve flips status + audit log grows.

## MOCK 2 - Adobe flavor (brief, brand, assets, provenance, review)

"Create a workflow where a one-paragraph organizational brief becomes
brand-consistent media assets. The system must extract brand rules, tone,
and audience from the brief, generate assets with captions and alt text,
support multiple output formats, and require human review before delivery.
Every asset must carry a provenance record: which prompt, which model, which
reviewer, when. Corrections and revisions must be versioned."

Expected: fingerprint Adobe. Decision tree -> IDEA C SignalStory,
deck-creative, storyboard C. Acceptance test: source becomes an editable
asset with a provenance card.

## MOCK 3 - Apple flavor (privacy, on-device, graceful fallback)

"Design a privacy-first personal intelligence feature that transforms
sensitive documents and notes on the user's device. The user must be able to
see exactly what data moves where, nothing may leave the device without
explicit consent, and the experience must degrade gracefully when the
network is unavailable. Accessibility is a first-class requirement."

Expected: fingerprint Apple. Decision tree -> IDEA B privacy skin,
deck-multimodal. Acceptance test: on-device state, refuse cloud path, safe
fallback without a crash. Note: this is the hardest mount, our scaffold is
server-shaped, be ready to frame the demo honestly (local mode, consent
badges, no data leaves the laptop in the demo).

## MOCK 4 - Meta flavor (multimodal, community, confidence, escalation)

"Build a multimodal assistant for a community platform. It must accept text,
images, and documents, extract structured facts, and answer with confidence
bands and evidence. Queries that are uncertain or high-risk must be routed
to a human reviewer, and user corrections must be remembered. Moderation
hints for suspicious content are a plus."

Expected: fingerprint Meta. Decision tree -> IDEA B Kavach Circle,
deck-multimodal. Acceptance test: message + image -> answer -> escalation
path visible.

## MOCK 5 - Accenture flavor (cases, ownership, policy, KPI, audit)

"Design a governed case-routing system for an enterprise. Unstructured
requests must become structured cases with an owner, a policy check, consent
records, and an approval step before any side effect. Management needs a KPI
dashboard: case volume, cycle time, approvals pending, exceptions. Every
case must be auditable end to end."

Expected: fingerprint Accenture. Decision tree -> IDEA A ops skin,
deck-agentic. Acceptance test: one case moves intake -> owner -> approval ->
KPI visible.

## OFF-MAP MOCK (bonus, do last if time)

"Something completely different: a game, a hardware widget, or a social
cause. The judges want to be surprised." Expected behavior: map to the
closest idea, never pitch fresh (IDEA-BANK section 0). This mock exists to
practice saying no to panic.

## THE METRIC SHEET (fill per mock)

Mock N: sponsor fingerprint ____, fingerprint time ____, decision time ____,
idea chosen ____, deck ____, mount time ____ (target 15-40 min), gaps found
____, fixes needed ____.

After the drill: append the measured times to docs/NUMBERS-2026.md section 1
and replace the UNVERIFIED tag on the mount claim. That is the benchmark
kavach had and we did not, until tonight.
