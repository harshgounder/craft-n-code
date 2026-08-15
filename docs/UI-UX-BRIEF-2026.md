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

## PATTERNS TO STEAL (merged after wave-2 lands)

[DRAFT] placeholders: Claude Code permission prompts (diff preview
before accept), Codex plan-then-execute, Cursor agent review mode,
Glean citation chips, Notion AI inline evidence, Stripe-style audit
logs, Linear-style keyboard-first triage.

## WHAT TO AVOID (from AI-failure cases, wave-2 pending)

[DRAFT] placeholders: hidden auto-execute, no evidence on proposals,
approve buttons that fire side effects twice, badges that lie, feeds
that look live but are static, trace that hides failures.

## DELIVERABLE

After wave-2: this file becomes the spec for a UI polish pass via
opencode (labels, badge placement, card layout in index.html, no logic
changes), plus the demo script beats that use the UI intentionally.
