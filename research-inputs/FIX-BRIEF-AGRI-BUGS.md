# FIX-BRIEF-AGRI-BUGS.md (executed via opencode, branch core-lane)

Three bugs found by the acceptance test run. Fix exactly these, nothing
else. No em dashes in code or comments. stdlib only.

## BUG 1 (critical, math direction): scaffold/agri/cvar.py cvar_95
Line ~107: `tail = sorted(samples)[:k]` takes the LOWEST k samples.
For LOSS samples the worst tail is the HIGHEST k. CVaR_95 must be the
mean of the worst 5% of losses.
FIX: `tail = sorted(samples)[-k:]`
Keep the empty-list ValueError. Docstring already says "worst 5%".

## BUG 2: scaffold/agri/replay.py band() (line ~83)
`lo, _, hi = quantiles(values, n=40)` crashes: statistics.quantiles
returns n-1 cut points (39 values for n=40), not 3.
FIX: cuts = quantiles(values, n=40); lo = cuts[0]; hi = cuts[-1]
(cuts[0] is the 2.5th percentile, cuts[-1] the 97.5th, matching the
docstring). Keep the mean() in the returned dict.

## BUG 3: scaffold/agri/claims.py build_packet (line ~36)
`deadline = event_time + timedelta(...)` crashes when claim has no
event_time key (the contract's claim_packet has no event_time).
FIX: if event_time is None, set event_time = now and add
"event_time_unknown": True to the returned packet (honest label).
Compute deadline and hours_since from that. Keep the rest unchanged.

## VERIFY
- python3 -c "import sys; sys.path.insert(0,'scaffold/agri'); import cvar; print(cvar.cvar_95(list(range(1,101))))"
  must print 98.0 (mean of 96..100, the worst 5%).
- python3 scaffold/agri/replay.py must run end to end and print a
  posterior with affected_ha band.
- python3 -c "import sys; sys.path.insert(0,'scaffold/agri'); import claims; print(claims.build_packet({'claim_id':'X'})['event_time_unknown'])"
  must print True.
Do NOT commit. Report the three diffs.
