# Provider adapter - swap the LLM backend without editing engine.py.
# BUILD-SPEC-2 item A. Pure stdlib. Lazy env reads so serve.py can force a
# provider at runtime (same pattern as the API key).
#
# The default (SIGNAL_PROVIDER unset) must behave exactly as before: ollama-cloud
# when a key is present, offline fallback otherwise.

from __future__ import annotations

import json
import os
import socket
import sys
import threading
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Optional, Protocol

# ────────────────────────────────────────────────────────────────
# Provider outcome stats (BUILD-SPEC B2). Thread-safe plain dict +
# lock. Records every real chat outcome so the mode badge can be
# derived from what actually happened, never from intent.
# ────────────────────────────────────────────────────────────────

_ERROR_KEYS = ["timeout", "http_4xx", "http_5xx", "network", "other", "disabled"]

_STATS_LOCK = threading.Lock()
_STATS = {
    "attempts": 0,
    "ok": 0,
    "errors": {k: 0 for k in _ERROR_KEYS},
    "last_error_at": None,
    "last_ok_at": None,
}

INJECT_FAILURES = False


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _record_attempt() -> None:
    with _STATS_LOCK:
        _STATS["attempts"] += 1


def _record_ok() -> None:
    with _STATS_LOCK:
        _STATS["ok"] += 1
        _STATS["last_ok_at"] = _now_iso()


def _record_error(kind: str) -> None:
    with _STATS_LOCK:
        _STATS["errors"][kind] = _STATS["errors"].get(kind, 0) + 1
        _STATS["last_error_at"] = _now_iso()


def get_stats() -> dict:
    """Snapshot of the provider outcome stats (safe to serialize)."""
    with _STATS_LOCK:
        return {
            "attempts": _STATS["attempts"],
            "ok": _STATS["ok"],
            "errors": dict(_STATS["errors"]),
            "last_error_at": _STATS["last_error_at"],
            "last_ok_at": _STATS["last_ok_at"],
        }


def reset_stats() -> None:
    """Clear provider stats (used by tests between scenarios)."""
    global _STATS
    with _STATS_LOCK:
        _STATS = {
            "attempts": 0,
            "ok": 0,
            "errors": {k: 0 for k in _ERROR_KEYS},
            "last_error_at": None,
            "last_ok_at": None,
        }


def set_inject_failures(value: bool) -> None:
    """Turn the --inject-failures drill on or off (set at server startup)."""
    global INJECT_FAILURES
    INJECT_FAILURES = bool(value)


def is_injecting() -> bool:
    return INJECT_FAILURES


def _classify_error(exc: BaseException) -> str:
    """Map an exception to a stats bucket: timeout/http_4xx/http_5xx/network/other."""
    if isinstance(exc, socket.timeout) or isinstance(exc, TimeoutError):
        return "timeout"
    if isinstance(exc, urllib.error.HTTPError):
        code = exc.code
        if 400 <= code < 500:
            return "http_4xx"
        if code >= 500:
            return "http_5xx"
        return "other"
    if isinstance(exc, urllib.error.URLError):
        return "network"
    if isinstance(exc, (OSError, ConnectionError)):
        return "network"
    return "other"


class Provider(Protocol):
    """A chat backend. Returns None when it cannot produce an answer."""

    def chat(self, system: str, user: str, max_tokens: int, temperature: float) -> Optional[str]:
        ...


class OllamaProvider:
    """Current behavior: ollama-cloud (OpenAI-compatible). Lazy env reads."""

    def __init__(self):
        self.failures = 0

    def chat(self, system: str, user: str, max_tokens: int = 400, temperature: float = 0.2) -> Optional[str]:
        _record_attempt()
        if INJECT_FAILURES:
            # Simulated timeout before any network IO (--inject-failures drill).
            _record_error("timeout")
            self.failures += 1
            print("  [llm] injected timeout (--inject-failures); using offline", file=sys.stderr)
            return None
        api_key = os.environ.get("OLLAMA_API_KEY", "")
        if not api_key:
            # No key: the provider is disabled at config time, not a call failure.
            return None
        model = os.environ.get("SIGNAL_MODEL", "deepseek-v4-flash:0731")
        base_url = os.environ.get("OLLAMA_BASE_URL", "https://ollama.com/v1").rstrip("/")
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        req = urllib.request.Request(
            f"{base_url}/chat/completions",
            data=json.dumps(payload).encode(),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = json.loads(resp.read().decode())
            out = data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            _record_error(_classify_error(e))
            self.failures += 1
            print(f"  [llm] ollama-cloud failed ({e}); using offline", file=sys.stderr)
            return None
        _record_ok()
        return out


class NullProvider:
    """Pure offline: never returns a result, never touches the network."""

    def __init__(self):
        self.failures = 0

    def chat(self, system: str, user: str, max_tokens: int = 400, temperature: float = 0.2) -> Optional[str]:
        _record_attempt()
        _record_error("disabled")
        return None


PROVIDERS: dict[str, type] = {
    "ollama": OllamaProvider,
    "null": NullProvider,
}


def get_provider() -> Provider:
    """Resolve the active provider from SIGNAL_PROVIDER (lazy, default ollama)."""
    name = os.environ.get("SIGNAL_PROVIDER", "ollama")
    cls = PROVIDERS.get(name, OllamaProvider)
    return cls()
