# Provider adapter - swap the LLM backend without editing engine.py.
# BUILD-SPEC-2 item A. Pure stdlib. Lazy env reads so serve.py can force a
# provider at runtime (same pattern as the API key).
#
# The default (SIGNAL_PROVIDER unset) must behave exactly as before: ollama-cloud
# when a key is present, offline fallback otherwise.

from __future__ import annotations

import json
import os
import sys
import urllib.request
from typing import Optional, Protocol


class Provider(Protocol):
    """A chat backend. Returns None when it cannot produce an answer."""

    def chat(self, system: str, user: str, max_tokens: int, temperature: float) -> Optional[str]:
        ...


class OllamaProvider:
    """Current behavior: ollama-cloud (OpenAI-compatible). Lazy env reads."""

    def chat(self, system: str, user: str, max_tokens: int = 400, temperature: float = 0.2) -> Optional[str]:
        api_key = os.environ.get("OLLAMA_API_KEY", "")
        model = os.environ.get("SIGNAL_MODEL", "deepseek-v4-flash:0731")
        base_url = os.environ.get("OLLAMA_BASE_URL", "https://ollama.com/v1").rstrip("/")
        if not api_key:
            return None
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
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"  [llm] ollama-cloud failed ({e}); using offline", file=sys.stderr)
            return None


class NullProvider:
    """Pure offline: never returns a result, never touches the network."""

    def chat(self, system: str, user: str, max_tokens: int = 400, temperature: float = 0.2) -> Optional[str]:
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
