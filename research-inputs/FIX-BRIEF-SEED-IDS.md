# FIX-BRIEF-SEED-IDS.md (executed via opencode, branch core-lane)

Change the seed identifiers in scaffold/agri/seed.py to the merge
protocol ids. This is the contract with the backend lane: farm ids,
incident ids must match EXACTLY what window C seeds in its SQLite API.

## CHANGES (exact)
1. asha_farm(): "id": "asha" -> "id": "asha-001"
2. high_field_farm(): "id": "high-field" -> "id": "highfield-002"
3. flood_warning_incident(): "id": "inc-2026-flood-01" -> "id": "demo-2026"
4. sample_advisories(): farmer references "asha" -> "asha-001",
   "high-field" -> "highfield-002" (keep every other field identical).

Do NOT touch any other logic. Run the agri test suite after the change:
cd scaffold/tests && python3 test_agri.py
All tests must stay green (they only use asha_farm()/high_field_farm()
results, not hardcoded ids, except the incident id which the tests do
not assert on). Report the four diffs + test result. Do NOT commit.
