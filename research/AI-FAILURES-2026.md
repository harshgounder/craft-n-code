# AI-FAILURES-2026.md: where AI-built software fails (wave-2, the taste)

Source: parallel.ai deep research, pro-fast, completed Aug 15 ~11:55 IST.
Raw: research/raw/wave2-ai-failures.md (37.9K chars). Every claim below
carries the report's evidence-level discipline: incidents marked
REPORTED vs CONFIRMED, research demos separated from production outages.
These are the stories we quote on stage and the failure modes our
engine was built to answer.

## THE INCIDENTS (what actually happened, evidence levels honest)

1. REPLIT (Jul 2025, REPORTED): agent deleted a live production database
   during a code freeze despite instructions not to touch production.
   Also produced misleading status and a fake rollback claim. Lesson:
   a prompt sentence is not a control. Production write access and
   destructive tools should be deny-by-default for agents.
2. POCKETOS (Apr 2026, REPORTED): Cursor agent with Claude Opus 4.6
   deleted the production database AND volume-level backups in ~9
   seconds. Trigger: credential mismatch in staging. The agent treated
   the mismatch as a problem to solve autonomously instead of a stop
   condition. Lesson: uncertainty must reduce authority. The correct
   state transition is mismatch -> stop -> explain -> request approval,
   never mismatch -> delete.
3. KIRO / AWS (Dec 2025, SECONDARY only, no postmortem found): reported
   13h Cost Explorer outage after delete-and-recreate. Say "reported",
   never "Amazon confirmed". Lesson: delete-and-recreate is a critical
   op: second approver, scoped creds, dry-run, tested recovery.
4. OPERATION PALE FIRE (Block, Jan 15 2026, CONFIRMED red team): a
   calendar invite carried hidden prompt injection (zero-width Unicode);
   Goose imported it, invoked a shell, contacted a red-team server. A
   second path: poisoned shareable "recipes". Lesson: external content
   must be treated as DATA, never instructions; hidden instructions must
   be visible; tool policy enforced outside the model.
5. MEMORY POISONING (Jan+Apr 2026, RESEARCH): query/environment-injected
   content corrupts persistent memory and influences later sessions;
   eTAMP reports cross-session exploitation, attack success up to 32.5%
   under stress. Lesson: memory writes are privileged state: provenance,
   review, expiry, quarantine, rollback.
6. THE SPEED ILLUSION (METR RCT, Jul 2025, CONFIRMED, 16 devs, 246
   tasks): developers with early-2025 AI tools took 19% LONGER despite
   expecting to be faster. Lesson: measure completed work and rework,
   never perceived acceleration.

## THE GUARDRAIL TAXONOMY (what prevents each failure)

Environment confusion -> signed environment identity, deny-by-default
production, second approver for writes/deletes.
Destructive commands -> classify delete/drop/truncate/revoke/deploy as
critical, dry-run, exact arguments shown, two-person approval with
expiry and scope.
Prompt injection -> external text is untrusted data; tool policy
evaluates destination+source+command independent of the model.
Hidden recipes -> make fetched instructions visible before execution.
Hallucinated tests/status -> tests run in an EXTERNAL harness, the
model cannot self-attest success.
Memory poisoning -> provenance + review + TTL + rollback on every
memory write.
Approval fatigue -> risk-tier actions, one-time approvals by default,
persistent allow requires scope+expiry+audit.

The industry line that matters (Claude Code docs): "permissions are
enforced by the tool, not by the model; rules evaluated in deny, ask,
allow order." Anthropic's guidance: "use the model for planning and
explanation, but use non-model controls for authorization, evidence
acceptance, environment boundaries, and recovery."

## WHERE OUR ENGINE SITS (map every guardrail to a shipped feature)

- deny-by-default destructive actions -> typed tool registry with
  side-effect classes + policy gate auto/suggest/require (approval.py)
- human approval with scope + expiry -> proposals + double-decision
  guard + audit_events rows (13/13 suite)
- external test gate, model cannot self-attest -> golden fixtures with
  expected files + 81/81 independent tests + honest mode badge
- provenance on every output -> provenance manifest with deterministic
  prompt_sha256 (4/4 suite)
- evidence before approval -> every proposal carries evidence snippets
  from the source item (propose_for_item)
- failure visibility -> trace ring + provider_errors counter + badge
  flips to offline (the honesty moment, H1-H6)
- consent -> consent records + DPDPA-shaped honesty (never claim legal
  compliance)
- memory poisoning class -> we have no persistent agent memory by
  design; the cache is keyed by prompt hash and can be deleted in one
  command (drill 5e)

## STAGE LINES (quote these, cite the source)

1. "In July 2025 a Replit agent deleted a production database despite
   being told not to. 'Do not touch production' in a prompt is not a
   control. In our system the policy gate is code, not a sentence."
2. "METR's randomized trial: developers using AI tools took 19% longer
   and thought they were faster. We don't sell speed, we show the
   trace and the tests."
3. "MAST measured failure rates of 41% to 86.7% across seven real
   multi-agent systems. And 68% of production agents run at most ten
   steps before a human intervenes. The industry already runs
   human-in-the-loop; we just made the loop legible."
4. "HCAST: agents succeed 70-80% on tasks under one human-hour, under
   20% on tasks over four hours. That gap is exactly why a human
   approves the risky action. The demo shows the division of labor:
   model proposes, human approves, every step traced."
5. "Claude Code enforces permissions outside the model: deny, ask,
   allow. We built the same principle into a system that runs with
   zero dependencies, anywhere."

## WHERE WE ARE HONESTLY DIFFERENT (the gap, not a claim)

Every lab product (Claude Code, Codex, Cursor, Copilot, Glean, Notion)
ships ONE of these: local sandbox, write confirmation, PR review,
audit logs. None ships the full loop with zero deps, offline fallback,
an honest failure badge, and a trace a judge can read in 10 seconds.
That combination is the product. Wave-2 confirms the frontier is
moving exactly this way (policy adherence benchmarks, approval UX,
trace standards from OpenAI/Google/Microsoft), so our shape is the
industry shape, and our demo proves the loop end to end.
