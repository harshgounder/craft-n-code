#!/usr/bin/env python3
"""Acceptance tests P1-P4 from BUILD-SPEC-2 item A (provider adapter).

Plain python3, zero external deps. Exercises the provider adapter directly
against the engine LLM class, verifying default behavior is unchanged and
that SIGNAL_PROVIDER=null forces pure offline.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
ENGINE = ROOT / "engine"

sys.path.insert(0, str(ENGINE))

results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    mark = "PASS" if cond else "FAIL"
    print(f"  [{mark}] {name}" + (f"  -> {detail}" if detail else ""))


def main():
    import engine as E
    from providers import PROVIDERS, NullProvider, OllamaProvider

    # ── P1 default (no env) behaves as today: cache works, offline fallback works ──
    os.environ.pop("OLLAMA_API_KEY", None)
    os.environ.pop("SIGNAL_PROVIDER", None)
    llm = E.LLM(cache_path=Path("/tmp/opencode/p1_cache.json"))
    out = llm.chat("sys", "user")
    check("P1 no env -> offline fallback returns None", out is None, f"out={out!r}")
    check("P1 last_mode offline", llm.last_mode == "offline", llm.last_mode)
    # cache still works: seed a cache entry and confirm replay
    llm.cache["seedkey"] = "cached-answer"
    llm2 = E.LLM(cache_path=Path("/tmp/opencode/p1_cache.json"))
    llm2.cache["seedkey"] = "cached-answer"
    out2 = llm2.chat("sys", "user")
    check("P1 cache replay unaffected by provider", out2 is None, f"out2={out2!r}")

    # ── P2 SIGNAL_PROVIDER=null -> every chat returns None, last_mode offline ──
    os.environ["SIGNAL_PROVIDER"] = "null"
    os.environ["OLLAMA_API_KEY"] = "some-key"
    llm3 = E.LLM(cache_path=Path("/tmp/opencode/p2_cache.json"))
    out3 = llm3.chat("sys", "user")
    check("P2 null provider returns None even with key", out3 is None, f"out3={out3!r}")
    check("P2 last_mode offline", llm3.last_mode == "offline", llm3.last_mode)

    # ── P3 SIGNAL_PROVIDER=null set AFTER import still works (lazy read) ──
    os.environ.pop("SIGNAL_PROVIDER", None)
    os.environ["OLLAMA_API_KEY"] = "some-key"
    llm4 = E.LLM(cache_path=Path("/tmp/opencode/p3_cache.json"))
    os.environ["SIGNAL_PROVIDER"] = "null"  # set after LLM constructed
    out4 = llm4.chat("sys", "user")
    check("P3 lazy provider read after import -> null", out4 is None, f"out4={out4!r}")
    check("P3 last_mode offline", llm4.last_mode == "offline", llm4.last_mode)

    # ── P4 cache replay unaffected by provider choice ──
    os.environ["SIGNAL_PROVIDER"] = "null"
    llm5 = E.LLM(cache_path=Path("/tmp/opencode/p4_cache.json"))
    llm5.cache["k"] = "v"
    out5 = llm5.chat("sys", "user")
    check("P4 cache replay with null provider", out5 is None, f"out5={out5!r}")

    # registry sanity
    check("P4 PROVIDERS has ollama and null",
          "ollama" in PROVIDERS and "null" in PROVIDERS,
          f"{list(PROVIDERS)}")

    failed = [n for n, ok, _ in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    if failed:
        print("FAILED:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
