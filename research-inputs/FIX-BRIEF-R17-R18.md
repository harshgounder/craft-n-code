# FIX-BRIEF-R17-R18.md (executed via opencode, branch window-b)

Critical demo gap found by the fresh-eyes audit: the harvest advisory
has no rule behind it. The deck cites "rule 14" for the harvest
decision, but R14 is "Controlled overflow corridor". No rule in
R1-R16 contains harvest now / raised platform / mature paddy as an
action. The demo's two-farm contrast (high-field farm harvest by 18:00)
dies if a judge asks "which rule fired?"

## FIX 1: ADD R17 + R18 to scaffold/agri/rules.json

Follow the EXACT existing rule schema in the file (id, trigger, action,
action_template, deadline logic, source, grade, badge, guardrail).
Keep the same field names as the other 16 rules. Do not renumber
existing rules.

R17 (harvest now, the high-field farm rule):
- id: "R17"
- trigger: hazard in [cyclone, flood] with lead_hours >= 24, crop
  paddy, stage harvest_window or maturity, tenancy owned, labor
  available
- action: harvest now, deadline = lead time minus 6 hours
- action_template: "{farm_name}: harvest the mature paddy now. Cut
  and move to high ground by {deadline}. Labor estimate: 12 hours per
  hectare at current field capacity."
- source: "d32" (5.76% early-harvest cost meta, 32 studies, 977 pairs;
  harvest window 45-55 days after heading; labor 233 man-hours/ha
  manual, 113.5 reaper, 9 combine from d32)
- grade: "B"
- badge: "TRANSFER-PRIOR" (meta-analysis, not an Odisha measurement)
- guardrail: "only when lead_hours >= 24 AND stage in
  harvest_window/maturity AND tenancy owned AND labor_available.
  Early harvest costs 5.76% yield: fire only when expected flood loss
  exceeds that, per the CVaR comparison. Never fire for flowering or
  vegetative paddy (harvesting green paddy is destructive)."

R18 (do NOT harvest, the Asha farm rule):
- id: "R18"
- trigger: hazard in [cyclone, flood], crop paddy, stage flowering or
  vegetative, lead_hours any
- action: do not harvest (green paddy is destructive to cut); protect
  seed, shelter livestock, photograph standing crop for the claim
  packet
- action_template: "{farm_name}: do not harvest, the paddy is not
  ready. Protect seed (elevate + seal), shelter livestock, and
  photograph the standing crop now for your claim packet."
- source: "d34" (tillering no loss under 4 days inundation, 80% at 6
  days; flowering submergence most damaging), "d6" (claim evidence
  routes, 72h intimation)
- grade: "B"
- badge: "TRANSFER-PRIOR"
- guardrail: "never advise harvesting green paddy. Embankment work
  gated on tenancy: leased land asks the landlord first (d37
  adaptation gap)."

## FIX 2: UPDATE THE DECK CITATION

In scaffold/deck/build-krishi-setu.js, find the harvest quote that
references "rule 14" and change the citation to the real rule id. The
harvest advisory quote (slide 6/7 area, the "The advisory says" block
and slide 4's BEFORE stage) must cite "rule R17" instead of "rule 14".
Verify by grep: no "rule 14" remains in build-krishi-setu.js.

## FIX 3: COMPILER TEST

Add two tests to scaffold/tests/test_agri.py (append, do not modify
existing):
- test_r17_fires_for_mature_owned_farm: compile actions for the
  high-field farm (maturity/harvest_window stage, owned) with a
  cyclone incident lead >= 24h; assert R17 appears in the action
  sources/ids.
- test_r18_fires_for_flowering_farm: compile actions for Asha
  (flowering, leased) with the same incident; assert R18 appears and
  NO harvest action appears.

## HARD RULES
No em dashes anywhere. No invented numbers: use only the values stated
above. Do not touch any other rule. Do not renumber. Do not commit:
the orchestrator audits, verifies, and commits.

## VERIFY BEFORE DONE
Run python3 scaffold/tests/test_agri.py: all tests pass (19 existing
+ 2 new = 21). Grep rules.json: R17 and R18 present with correct
badges. Grep build-krishi-setu.js: "rule 14" gone, "R17" present.
Report the results.
