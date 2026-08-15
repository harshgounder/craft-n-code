# UI-UX-BRIEF-2026.md: what good human-in-the-loop UX looks like (draft)

Purpose: decide the demo UI standards BEFORE the night, so the skin mount
includes a look, not just nouns. Wave-2 deep research (parallel.ai,
pro-fast, run trun_4dd3f131a592407cbfde93c94ca73dc5) is pulling real
product patterns + failure cases; this file merges them. Sections marked
[DRAFT] get replaced with cited findings.

## THE ONE PRINCIPLE (locked, no research needed)

The judge must understand the system in 10 seconds without a word:
what came in, what the AI proposed, what a human approved, what the
system did, and what it refused. If the UI needs explaining, it loses.

## LAYOUT RULES (draft, from demo needs)

1. Top bar: product name + MODE BADGE (live/cached/fixture/offline) +
   FEEDS BADGE (live/cached/offline) + provider_errors count when > 0.
   The badge is the honesty story, make it visible, not a footer.
2. Left column: ranked queue. Each card: subject, source channel,
   rank score, deadline flag, evidence snippet (the source text, not a
   paraphrase). The card answers "why is this first".
3. Right column / drawer: proposal pane. Tool name, side-effect class,
   params, confidence, evidence list, Approve / Reject / Snooze buttons
   with a re-decision guard (second click = already decided, shown
   disabled).
4. Bottom strip: trace timeline (last N steps, clickable), audit
   counter, consent records. The judge scrolls once and sees the whole
   loop: ingest -> rank -> propose -> approve -> audit.
5. Failure visibility: when the provider dies, the badge flips and a
   toast explains "model unreachable, showing offline rules". Showing
   the failure state on purpose is the demo beat, not an accident.

## PATTERNS TO STEAL (wave-2 VERIFIED, parallel.ai pro-fast)

1. Claude Code: read-only by default, ask before edits/commands, rules
   evaluated in DENY, ASK, ALLOW order, enforced outside the model.
   Our map: policy gate auto/suggest/require IS deny/ask/allow. The UI
   must show which rule class fired on each proposal.
2. Glean: pause BEFORE a write, let the user review AND EDIT the
   proposed change, then approve. Better than approving an opaque
   plan. Our map: proposals show params + evidence; the UI should show
   the exact side-effect class and let the approver see what changes.
3. GitHub PR model: durable artifact + tests + discussion between
   proposal and merge. Our map: the audit row + trace ring is the
   artifact; tests are the 81/81 suite, runnable by the judge.
4. Approval queue = operational review surface, not a chat transcript.
   7 stages from wave-2: triage (risk tier, environment), action
   summary (exact tool+args+blast radius, never a generic "run"),
   evidence (diff, tests, logs, provenance, confidence), safety preview
   (dry-run, rollback, what cannot be undone), decision (scoped to
   exact action+resource+time window), execution (live status, each
   tool call, policy check), closure (before/after state, approver
   identities, immutable export).
5. Three interaction patterns that win: DIFF-FIRST (show the mutation
   before the rationale), EVIDENCE-LINKED (green status must link to an
   external test result, never the model's assertion), SCOPED approval
   (approve one call or a narrow class for a short window).
6. Failure visibility is UX: a credential mismatch must appear as a
   high-risk STOP condition, not get silently "fixed". Our honesty
   moment is this exact principle on stage.
7. Notion is the cautionary tale: automation while people are away
   raises the provenance bar. We always show the trace, so automation
   stays explainable.

## WHAT TO AVOID (from the real failures, wave-2 VERIFIED)

- Hidden auto-execute: the Replit/PocketOS class. Never hide what will
  change.
- Approve buttons that fire side effects twice: our double-decision
  guard kills it; the UI must disable the buttons after decision.
- Badges that lie: fixed Aug 15 (provider_errors -> offline). The UI
  shows the badge and the failure count, never hides it.
- Feeds that look live but are static: feeds badge shows live/cached/
  offline with fetched_at timestamps.
- Traces that hide failures: the trace ring keeps every step including
  provider failures (engine prints "using offline" to the ring).

## DELIVERABLE

This file + wave-2 = the spec for a UI polish pass via opencode
(labels, badge placement, card layout in index.html, no logic changes).
The polish pass is optional pre-drop; the functional UI already tells
the story. Priority: rehearsal beats polish.
