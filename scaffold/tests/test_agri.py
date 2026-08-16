"""Acceptance tests for the KrishiSetu core (agri package). Hermes-written
test suite (tests are allowed; source is opencode-written). Covers the
two-farm contrast, CVaR decisions, Fani replay anchor coverage, state
machine transitions, claims gates, badges, doability, research index."""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "agri"))

import claims
import compiler
import cvar
import doability
import replay
import research_index
import seed
import state_machine

RULES = json.load(open(os.path.join(os.path.dirname(__file__), "..", "agri", "rules.json")))
if isinstance(RULES, dict):
    RULES = RULES.get("rules", RULES.get("registry", []))

VALID_BADGES = {"ODISHA-MEASURED", "TRANSFER-PRIOR", "SCENARIO-ASSUMPTION", "UNKNOWN"}


class TestRulesRegistry(unittest.TestCase):
    def test_sixteen_rules(self):
        self.assertGreaterEqual(len(RULES), 16)

    def test_every_rule_has_fields(self):
        for r in RULES:
            for f in ("id", "trigger", "action_template", "source", "grade", "badge"):
                self.assertIn(f, r, f"rule missing {f}: {r.get('id')}")

    def test_badges_valid(self):
        for r in RULES:
            self.assertIn(r.get("badge"), VALID_BADGES, f"bad badge in {r.get('id')}")


class TestTwoFarmContrast(unittest.TestCase):
    def setUp(self):
        self.asha = seed.asha_farm()
        self.high = seed.high_field_farm()
        self.incident = seed.flood_warning_incident()

    def test_same_incident_different_actions(self):
        a = compiler.compile_actions(self.asha, self.incident, RULES)
        b = compiler.compile_actions(self.high, self.incident, RULES)
        self.assertGreater(len(a), 0)
        self.assertGreater(len(b), 0)
        actions_a = [x.get("rule_id") for x in a]
        actions_b = [x.get("rule_id") for x in b]
        self.assertNotEqual(actions_a, actions_b)

    def test_actions_carry_badges_and_source(self):
        for farm in (self.asha, self.high):
            for x in compiler.compile_actions(farm, self.incident, RULES):
                self.assertIn(x.get("badge"), VALID_BADGES)
                self.assertTrue(x.get("source"))
                self.assertIn(x.get("grade"), "ABCD")
                self.assertTrue(x.get("deadline"))


class TestCVaR(unittest.TestCase):
    def test_cvar_95_worst_tail(self):
        # worst 5% of 1..100 is 96..100, mean = 98
        self.assertAlmostEqual(cvar.cvar_95(list(range(1, 101))), 98.0, places=3)

    def test_harvest_under_flood_risk(self):
        # high-field farm is in harvest_window (mature paddy): harvest is
        # feasible, so high flood risk must pick immediate over wait
        incident = dict(seed.flood_warning_incident(),
                        flood_probability=0.9, deep_flood_share=0.6,
                        inundation_days_mean=5)
        decision = cvar.harvest_decision(seed.high_field_farm(), incident, n=600, seed=7)
        self.assertEqual(decision["best"], "immediate", decision)

    def test_wait_when_low_risk(self):
        incident = dict(seed.flood_warning_incident(),
                        flood_probability=0.05, deep_flood_share=0.2,
                        inundation_days_mean=2)
        decision = cvar.harvest_decision(seed.high_field_farm(), incident, n=600, seed=7)
        self.assertEqual(decision["best"], "wait", decision)

    def test_tillering_farm_never_harvests_green(self):
        # Asha is tillering: harvesting green paddy is destructive, so
        # wait is forced even under high risk (the doability gate)
        incident = dict(seed.flood_warning_incident(),
                        flood_probability=0.9, deep_flood_share=0.6,
                        inundation_days_mean=5)
        decision = cvar.harvest_decision(seed.asha_farm(), incident, n=600, seed=7)
        self.assertEqual(decision["best"], "wait", decision)
        self.assertFalse(decision["options"]["immediate"]["feasible"])


class TestFaniReplay(unittest.TestCase):
    def test_posterior_band_covers_anchor(self):
        post = replay.fani_posterior(pilot_n=300, main_n=900)
        band = post["posterior"]["affected_ha"]
        self.assertIn("p2_5", band)
        self.assertIn("p97_5", band)
        anchor = 108220.0
        self.assertGreaterEqual(band["p97_5"], anchor)
        self.assertLessEqual(band["p2_5"], anchor)
        self.assertTrue(post["anchor_ha_in_band"], post.get("explanation"))


class TestStateMachine(unittest.TestCase):
    FULL = ["MONITOR", "PRE_CYCLONE_WATCH", "CYCLONE_ALERT", "CYCLONE_WARNING",
            "POST_LAND_FALL_OUTLOOK", "IMPACT_SUSPECTED", "IMPACT_CONFIRMED",
            "RESPONSE", "RECOVERY", "NEXT_SEASON", "CLOSED"]

    def _walk(self, m, targets):
        for t in targets:
            m.apply({"state": t})

    def test_transitions_full_chain(self):
        m = state_machine.IncidentMachine("inc-test")
        self._walk(m, self.FULL)
        self.assertEqual(m.state, "CLOSED")

    def test_never_closes_on_first_recession(self):
        m = state_machine.IncidentMachine("inc-test")
        self._walk(m, self.FULL[:9])   # up to RECOVERY (index 8, slice 9)
        res = m.apply({"kind": "recession"})
        self.assertEqual(res["kind"], "update")
        self.assertEqual(m.state, "RECOVERY")
        # a second recession is still an update, still not closed
        res = m.apply({"kind": "recession"})
        self.assertEqual(res["kind"], "update")
        self.assertEqual(m.state, "RECOVERY")

    def test_second_flood_returns_to_impact(self):
        m = state_machine.IncidentMachine("inc-test")
        self._walk(m, ["PRE_CYCLONE_WATCH", "CYCLONE_ALERT", "CYCLONE_WARNING",
                       "POST_LAND_FALL_OUTLOOK", "IMPACT_SUSPECTED",
                       "IMPACT_CONFIRMED", "RESPONSE", "RECOVERY"])
        res = m.apply({"kind": "flood_renewed"})
        self.assertEqual(m.state, "IMPACT_SUSPECTED")

    def test_illegal_transition_rejected(self):
        m = state_machine.IncidentMachine("inc-test")
        res = m.apply({"state": "CLOSED"})  # MONITOR has no CLOSED edge
        self.assertEqual(res["kind"], "rejected")
        self.assertEqual(m.state, "MONITOR")

    def test_cap_update_never_duplicates(self):
        m = state_machine.IncidentMachine("inc-test")
        m.apply({"state": "PRE_CYCLONE_WATCH"})
        res = m.apply({"state": "PRE_CYCLONE_WATCH"})
        self.assertEqual(res["kind"], "update")
        self.assertEqual(m.state, "PRE_CYCLONE_WATCH")


class TestClaims(unittest.TestCase):
    def test_72h_gate_and_unknown_event_time(self):
        packet = claims.build_packet({"claim_id": "C1", "intimation_72h": True,
                                      "loss_threshold_33": True})
        self.assertTrue(packet.get("event_time_unknown", False))
        self.assertIn("intimation_on_time", packet)
        self.assertIn("eligible", packet)
        self.assertTrue(packet.get("simulated"))

    def test_export_text_mentions_claim(self):
        packet = claims.build_packet({"claim_id": "C1", "intimation_72h": True,
                                      "loss_threshold_33": True})
        text = claims.export_text(packet)
        self.assertIn("claim", text.lower())


class TestDoability(unittest.TestCase):
    def test_infeasible_flagged(self):
        farm = seed.asha_farm()
        rec = doability.score(farm, {"labor_hours": 40, "cost_rs": 5000, "credit_needed": True})
        self.assertIn("feasible", rec)
        self.assertIn("infeasible_reason", rec)


class TestResearchIndex(unittest.TestCase):
    def test_load_and_search(self):
        path = os.path.join(os.path.dirname(__file__), "..", "..", "research-inputs", "EVIDENCE-INDEX.md")
        rows = research_index.load_index(path)
        self.assertGreaterEqual(len(rows), 40)
        hits = research_index.search(rows, "Fani")
        self.assertGreaterEqual(len(hits), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
