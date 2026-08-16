# FIX-BRIEF-R18-TRIGGER.md (executed via opencode, branch window-b)

One small change to scaffold/agri/rules.json:

## TASK: R18 trigger stage list must include "tillering"

R18 (do-not-harvest rule) currently has trigger.stage = ["flowering",
"vegetative"]. The demo's Asha farm is at stage "tillering", and
do-not-harvest applies to any immature paddy (harvesting green paddy
is destructive at every pre-maturity stage). Add "tillering" to the
stage list so the rule reads ["flowering", "vegetative", "tillering"].

Do NOT change R17, do not touch any other rule, do not renumber, do
not touch any other file, do not commit.

## VERIFY BEFORE DONE
grep R18's trigger in scaffold/agri/rules.json and print the stage
list: it must contain flowering, vegetative, tillering. Report the
exact trigger JSON.
