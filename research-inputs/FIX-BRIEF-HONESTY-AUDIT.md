# FIX-BRIEF-HONESTY-AUDIT.md (executed via opencode, branch window-b)

Four honesty corrections from the independent numbers audit
(~/krishisetu/research/AGRI-NUMBERS-AUDIT.md, window C). Fix exactly
these, nothing else. No em dashes. stdlib only.

## 1. scaffold/agri/cvar.py: Swarna-Sub1 180 kg/ha reframe
The EVIDENCE dict entry swarna_sub1.no_flood_kg_ha is documented as
"neutral when no flood". The raw evidence (d47) says no-flood effect
is a DISADVANTAGE of about -180 kg/ha and is NOT statistically
significant. FIX: change the note to: "no-flood point estimate -180
kg/ha, not statistically significant (d47)". Keep the value 180 but
add a minus sign context, or keep the number and fix the note: the
note must say the true direction and the non-significance. Simplest
correct fix: note = "no-flood point estimate -180 kg/ha (NS), d47".

## 2. scaffold/agri/claims.py: 33% threshold tag
The constant LOSS_THRESHOLD or its docstring/comment carries "(PMFBY
norms)". The raws (d20/d22) say 33% is Odisha's SRC (State Revenue
Cell) assessment threshold. FIX: change the tag to "(Odisha SRC
assessment threshold, d20/d22)". Do not claim PMFBY.

## 3. scaffold/agri/rules.json: R1 badge
R1 (official-alert lock) carries badge ODISHA-MEASURED but its source
is the Bangladesh Cyclone Preparedness Programme. FIX: change R1 badge
to TRANSFER-PRIOR. Keep the source field.

## 4. scaffold/agri/seed.py: unsourced profile defaults
The default constants in seed profiles (expected_yield_kg_ha 3500,
price_rs_kg 19, wage_rs_per_hour 100, harvest_labor_hours_per_ha 12)
are not in the raws. FIX: add a "defaults_note" key to both farm
profiles: "profile defaults are SCENARIO-ASSUMPTION, not from raws:
yield 3500 kg/ha, price Rs 19/kg, wage Rs 100/hr, labor 12 h/ha".
Do not change the values, only document the badge.

## VERIFY
- python3 scaffold/tests/test_agri.py: all 19 tests stay green
- grep the three files: no "(PMFBY norms)" remains; R1 badge is
  TRANSFER-PRIOR; cvar note mentions "-180" or "not statistically
  significant"; seed has defaults_note
- Do NOT commit. Report the diffs.
