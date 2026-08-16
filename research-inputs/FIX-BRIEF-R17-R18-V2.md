# FIX-BRIEF-R17-R18-V2.md (executed via opencode, branch window-b)

Your previous run updated the deck citation but did NOT add the rules
to rules.json and did NOT add the tests. This run is ONLY about those
two files. The deck work is done, do not touch it.

## TASK 1: APPEND R17 AND R18 to scaffold/agri/rules.json

Read the file first. It has a "rules" key containing 16 rule objects.
Each rule has fields including: id, trigger, action, action_template,
deadline, source, grade, badge, guardrail (check the actual field names
and match them exactly). Append two new rule objects to the rules
array. Keep existing rules untouched, no renumbering.

R17 harvest-now rule:
- id: "R17"
- trigger: hazard in [cyclone, flood], lead_hours >= 24, crop paddy,
  stage in [harvest_window, maturity], tenancy owned, labor available
- action: harvest now, move crop to high ground
- action_template: "{farm_name}: harvest the mature paddy now. Cut and
  move to high ground by {deadline}. Labor estimate 12 hours per
  hectare."
- source: "d32"
- grade: "B"
- badge: "TRANSFER-PRIOR"
- guardrail: "Early harvest costs 5.76% yield (32-study meta): fire
  only when expected flood loss exceeds that, per the CVaR comparison.
  Never fire for flowering or vegetative paddy."

R18 do-not-harvest rule:
- id: "R18"
- trigger: hazard in [cyclone, flood], crop paddy, stage in
  [flowering, vegetative]
- action: do not harvest, protect seed, shelter livestock, photograph
  standing crop for claim
- action_template: "{farm_name}: do not harvest, the paddy is not
  ready. Protect seed, shelter livestock, and photograph the standing
  crop now for your claim packet."
- source: "d34"
- grade: "B"
- badge: "TRANSFER-PRIOR"
- guardrail: "Never advise harvesting green paddy. Embankment work
  gated on tenancy: leased land asks the landlord first (d37)."

## TASK 2: APPEND 2 TESTS to scaffold/tests/test_agri.py

Read the file, find the class structure, append two test methods:

test_r17_fires_for_mature_owned_farm: compile actions for the
high-field farm (harvest_window stage, owned) with a cyclone incident
lead_hours >= 24; assert R17 appears in the compiled action rule ids
or sources.

test_r18_fires_for_flowering_farm: compile actions for Asha
(flowering, leased) with the same incident; assert R18 appears and NO
harvest action appears.

Use the same import style and assertions as existing tests in the
file. Match the real function signatures of compiler.compile_actions
and the real seed function names (read seed.py first).

## HARD RULES
No em dashes anywhere. No invented numbers: use only the values above.
Do not touch any other file. Do not commit. Do not touch
build-krishi-setu.js.

## VERIFY BEFORE DONE
1. python3 scaffold/tests/test_agri.py from scaffold/tests: all tests
   pass (19 existing + 2 new = 21).
2. grep rules.json for "R17" and "R18": both present.
3. Report the actual rule count and the test count.
