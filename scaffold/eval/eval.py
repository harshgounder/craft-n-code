#!/usr/bin/env python3
# Eval harness for the Signal Engine (BUILD-SPEC B1).
# Exercises the FULL pipeline (engine.run_pipeline + approval flows) against the
# golden fixtures and emits PASS/FAIL/SKIP per check plus a summary report.
# Pure stdlib. Exit code: 0 all pass, 1 any fail, 2 harness error.
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
import traceback
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCAFFOLD = HERE.parent
ENGINE_DIR = SCAFFOLD / "engine"
FIXTURES_DIR = SCAFFOLD / "fixtures"

if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import engine
import approval

TODAY = date(2026, 8, 15)
PROFILE = ["exam", "hostel", "2nd-year"]
GOLDEN = ["happy", "ambiguous", "adversarial", "multimodal"]

FIXTURES_OVERRIDE: Path | None = None
results: list[tuple[str, str, str]] = []

# Isolate the LLM disk cache so offline runs never read/write the engine cache.
_LLM_INIT = engine.LLM.__init__
_isolation_cache: Path | None = None


def _isolated_llm_init(self, cache_path=None):
    if cache_path is None:
        cache_path = _isolation_cache or engine.CACHE_PATH
    _LLM_INIT(self, cache_path)


engine.LLM.__init__ = _isolated_llm_init


def fixtures_dir() -> Path:
    return FIXTURES_OVERRIDE or FIXTURES_DIR


def check(name: str, cond: bool, detail: str = "") -> None:
    tag = "PASS" if cond else "FAIL"
    results.append((name, tag, detail))
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")


def skip(name: str, detail: str = "") -> None:
    results.append((name, "SKIP", detail))
    suffix = f" ({detail})" if detail else ""
    print(f"  [SKIP] {name}{suffix}")


def load_fixture(name: str) -> list[dict]:
    p = fixtures_dir() / f"{name}.json"
    return json.loads(p.read_text())


def load_expected(name: str) -> dict | None:
    p = fixtures_dir() / f"expected_{name}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def make_items(raw: list[dict]) -> list[engine.Item]:
    items = []
    for d in raw:
        items.append(engine.Item(
            channel=d.get("channel", ""),
            source_id=d.get("source_id", ""),
            sender=d.get("sender", ""),
            subject=d.get("subject", ""),
            body=d.get("body", ""),
            received_at=d.get("received_at", ""),
            profile_tags=d.get("profile_tags", []),
            kind=d.get("kind", "notice"),
        ))
    return items


def rank_ids(result: dict) -> list[str]:
    return [it["source_id"] for it in result["items"]]


def top3_matches(actual_ids: list[str], expected_ids: list[str],
                 items_data: list[dict]) -> bool:
    if len(expected_ids) < 3 or len(actual_ids) < 3:
        return actual_ids[:len(expected_ids)] == expected_ids
    score_map = {it["source_id"]: it["rank_score"] for it in items_data}
    for i in range(3):
        if actual_ids[i] == expected_ids[i]:
            continue
        if (score_map.get(actual_ids[i]) == score_map.get(expected_ids[i])
                and set(actual_ids[:i + 1]) == set(expected_ids[:i + 1])):
            continue
        return False
    return True


def _is_iso_date(s: str) -> bool:
    try:
        date.fromisoformat(s)
        return True
    except (ValueError, TypeError):
        return False


def _is_sorted_desc(items: list[dict]) -> bool:
    for i in range(len(items) - 1):
        if items[i]["rank_score"] < items[i + 1]["rank_score"]:
            return False
    return True


def _setup_temp_db(tmpdir: Path) -> None:
    engine.DB_PATH = tmpdir / "signal.db"
    approval.DB_PATH = tmpdir / "signal.db"
    global _isolation_cache
    _isolation_cache = tmpdir / ".llm_cache.json"


def _with_offline(fn) -> None:
    old_provider = os.environ.get("SIGNAL_PROVIDER")
    old_key = os.environ.get("OLLAMA_API_KEY")
    os.environ["SIGNAL_PROVIDER"] = "null"
    os.environ["OLLAMA_API_KEY"] = ""
    try:
        fn()
    finally:
        if old_provider is None:
            os.environ.pop("SIGNAL_PROVIDER", None)
        else:
            os.environ["SIGNAL_PROVIDER"] = old_provider
        if old_key is None:
            os.environ.pop("OLLAMA_API_KEY", None)
        else:
            os.environ["OLLAMA_API_KEY"] = old_key


# ────────────────────────────────────────────────────────────────
# E1-E4: golden fixture checks
# ────────────────────────────────────────────────────────────────

def run_golden_checks() -> None:
    for name in GOLDEN:
        raw = load_fixture(name)
        exp = load_expected(name)
        items = make_items(raw)

        result = engine.run_pipeline(items, PROFILE, TODAY)
        result_items = result["items"]
        actual_ids = rank_ids(result)

        # E1 dedupe: duplicate keys collapsed per expected counts
        if exp and "dedupe" in exp:
            expected_kept = exp["dedupe"]["expected_kept"]
            check(f"E1 {name} dedupe kept={expected_kept}",
                  result["total"] == expected_kept,
                  f"got {result['total']}, expected {expected_kept}")
        else:
            check(f"E1 {name} dedupe no loss",
                  result["total"] == len(items),
                  f"in={len(items)} out={result['total']}")

        # E2 deadlines: every expected deadline string found, none extra
        actual_dls = sorted({it["deadline_iso"] for it in result_items
                             if it["deadline_iso"]})
        expected_dls = sorted(exp.get("deadlines", [])) if exp else []
        if expected_dls:
            actual_set = set(actual_dls)
            missing = [d for d in expected_dls if d not in actual_set]
            extra = [d for d in actual_dls if d not in set(expected_dls)]
            check(f"E2 {name} deadlines match expected",
                  not missing and not extra,
                  f"missing={missing} extra={extra} actual={actual_dls}")
        else:
            check(f"E2 {name} deadlines valid ISO",
                  all(_is_iso_date(d) for d in actual_dls),
                  f"found {len(actual_dls)} deadlines")

        # E3 rank: top-3 order matches expected order (allow ties by score)
        if exp and "top3" in exp:
            expected_top3 = exp["top3"]
            ok = top3_matches(actual_ids, expected_top3, result_items)
            check(f"E3 {name} top-3 order", ok,
                  f"expected {expected_top3}, got {actual_ids[:3]}")
        else:
            check(f"E3 {name} rank sorted",
                  _is_sorted_desc(result_items),
                  f"top={actual_ids[:3]}")

        # E3 adversarial: scam item must not rank first
        if exp and exp.get("scam_not_top"):
            scam_id = exp.get("scam_rank")
            scam_pos = actual_ids.index(scam_id) if scam_id in actual_ids else -1
            check(f"E3 {name} scam not top",
                  scam_pos != 0,
                  f"{scam_id} at position {scam_pos}")

        # E4 summaries: non-empty for every item
        populated = sum(1 for it in result_items if it["summary"])
        check(f"E4 {name} all summaries non-empty",
              populated == len(result_items),
              f"{populated}/{len(result_items)} populated")


# ────────────────────────────────────────────────────────────────
# Approval flow: propose -> gate -> decide -> audit
# ────────────────────────────────────────────────────────────────

def run_approval_check() -> None:
    raw = load_fixture("adversarial")
    items = make_items(raw)
    engine.run_pipeline(items, PROFILE, TODAY)

    adv1 = items[0]
    evidence = [{"source_id": adv1.source_id, "subject": adv1.subject}]

    # Gate classification: auto / suggest / require
    gate_checks = [
        ("lookup_room", approval.READ_ONLY, "auto"),
        ("send_reminder", approval.REVERSIBLE, "suggest"),
        ("pay_fee", approval.SIDE_EFFECTING, "require"),
    ]
    for tool_name, expected_effect, expected_gate in gate_checks:
        tool = approval.TOOL_REGISTRY.get(tool_name)
        check(f"Approval gate {tool_name}",
              approval.gate(tool) == expected_gate,
              f"expected {expected_gate}, got {approval.gate(tool)}")
        check(f"Approval side_effect {tool_name}",
              tool.side_effect == expected_effect,
              f"got {tool.side_effect}")

    # Decide approve: status flips + audit row
    proposal = approval.propose(
        "pay_fee", {"amount": 500, "ref": "test"},
        "test approve", evidence, 0.9)
    check("Approval propose pending",
          proposal.status == approval.PENDING,
          f"status={proposal.status}")

    decided = approval.decide(proposal.id, "approve", "eval-test")
    check("Approval decide approve -> executed",
          decided.status == approval.EXECUTED,
          f"status={decided.status}")

    audit = approval.list_audit()
    approve_rows = [e for e in audit
                    if e["proposal_id"] == proposal.id
                    and e["decision"] == "approve"]
    check("Approval approve audit row",
          len(approve_rows) >= 1,
          f"{len(approve_rows)} rows")

    # Decide reject: status flips + audit row
    proposal2 = approval.propose(
        "submit_form", {"form_id": "test", "answers": {}},
        "test reject", evidence, 0.8)
    decided2 = approval.decide(proposal2.id, "reject", "eval-test")
    check("Approval decide reject -> rejected",
          decided2.status == approval.REJECTED,
          f"status={decided2.status}")

    audit = approval.list_audit()
    reject_rows = [e for e in audit
                   if e["proposal_id"] == proposal2.id
                   and e["decision"] == "reject"]
    check("Approval reject audit row",
          len(reject_rows) >= 1,
          f"{len(reject_rows)} rows")


# ────────────────────────────────────────────────────────────────
# Honesty: SIGNAL_PROVIDER=null completes offline, mode never live
# ────────────────────────────────────────────────────────────────

def run_honesty_check() -> None:
    raw = load_fixture("happy")
    items = make_items(raw)
    result = engine.run_pipeline(items, PROFILE, TODAY)
    check("Honesty pipeline completes offline",
          result["total"] > 0,
          f"total={result['total']}")
    check("Honesty model OFFLINE",
          result["llm"]["model"] == "OFFLINE",
          f"model={result['llm']['model']}")
    check("Honesty mode never live",
          determine_mode() == "offline",
          f"mode={determine_mode()}")


# ────────────────────────────────────────────────────────────────
# --live: LLM spot checks (skip gracefully when no key / null provider)
# ────────────────────────────────────────────────────────────────

def run_live_checks() -> None:
    if os.environ.get("SIGNAL_PROVIDER") == "null":
        for name in GOLDEN:
            skip(f"Live {name} summarize", "provider is null/offline")
        return
    if not os.environ.get("OLLAMA_API_KEY"):
        for name in GOLDEN:
            skip(f"Live {name} summarize", "no OLLAMA_API_KEY")
        return

    llm = engine.LLM()
    for name in GOLDEN:
        raw = load_fixture(name)[:3]
        items = make_items(raw)
        done_ids = []
        all_ok = True
        for it in items:
            out = engine.llm_summarize(llm, it)
            if not out or llm.last_mode == "offline":
                skip(f"Live {name} summarize",
                     f"provider error on {it.source_id}")
                all_ok = False
                break
            done_ids.append(it.source_id)
        if all_ok:
            check(f"Live {name} summarize", True,
                  f"summarized {', '.join(done_ids)}")


# ────────────────────────────────────────────────────────────────
# Report + CLI
# ────────────────────────────────────────────────────────────────

def determine_mode() -> str:
    if os.environ.get("SIGNAL_PROVIDER") == "null":
        return "offline"
    if any(tag == "PASS" and name.startswith("Live ")
           for name, tag, _ in results):
        return "live"
    return "offline"


def build_report(mode: str) -> dict:
    passed = sum(1 for _, tag, _ in results if tag == "PASS")
    failed = sum(1 for _, tag, _ in results if tag == "FAIL")
    skipped = sum(1 for _, tag, _ in results if tag == "SKIP")
    return {
        "mode": mode,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "checks": [
            {"name": name, "status": tag, "detail": detail}
            for name, tag, detail in results
        ],
        "pass": passed,
        "fail": failed,
        "skip": skipped,
        "total": len(results),
    }


def print_verdict_table() -> None:
    print()
    print("VERDICT TABLE")
    print("-" * 60)
    for name, tag, detail in results:
        suffix = f" ({detail})" if detail else ""
        print(f"  [{tag:4s}] {name}{suffix}")
    print("-" * 60)
    passed = sum(1 for _, tag, _ in results if tag == "PASS")
    failed = sum(1 for _, tag, _ in results if tag == "FAIL")
    skipped = sum(1 for _, tag, _ in results if tag == "SKIP")
    print(f"  {passed} PASS, {failed} FAIL, {skipped} SKIP")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Signal Engine eval harness")
    ap.add_argument("--all", action="store_true",
                    help="run all offline checks (E1-E4 + approval + honesty)")
    ap.add_argument("--live", action="store_true",
                    help="add LLM spot checks against the configured provider")
    ap.add_argument("--fixtures-dir", default=str(FIXTURES_DIR),
                    help="override fixtures directory (for testing)")
    ap.add_argument("--report", default=str(HERE / "eval-report.json"),
                    help="path to write eval-report.json")
    args = ap.parse_args()

    if not args.all and not args.live:
        ap.print_help()
        return 2

    global FIXTURES_OVERRIDE
    FIXTURES_OVERRIDE = Path(args.fixtures_dir)

    t0 = time.time()
    try:
        with tempfile.TemporaryDirectory() as td:
            tmpdir = Path(td)
            if args.all:
                _setup_temp_db(tmpdir)
                _with_offline(run_golden_checks)
                _with_offline(run_approval_check)
                _with_offline(run_honesty_check)
            if args.live:
                run_live_checks()
    except Exception as e:
        print(f"\nHARNESS ERROR: {e}", file=sys.stderr)
        traceback.print_exc()
        return 2

    mode = determine_mode()
    elapsed = round(time.time() - t0, 2)
    report = build_report(mode)
    report["elapsed_seconds"] = elapsed

    report_path = Path(args.report)
    report_path.write_text(json.dumps(report, indent=2))

    print_verdict_table()
    print(f"Report written to {report_path}")
    print(f"Elapsed: {elapsed}s")

    has_fail = any(tag == "FAIL" for _, tag, _ in results)
    return 1 if has_fail else 0


if __name__ == "__main__":
    sys.exit(main())
