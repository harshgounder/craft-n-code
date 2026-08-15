## executive_summary

- **Registry Explosion to ~10K Servers**: The official MCP Registry hit **9,652 server records** as of 24 May 2026 [executive_summary[0]] [1], with high-volume registries mcp.so advertising **19.7k+** and Smithery **7k+** [executive_summary[1]] [2]. Signal: any problem statement you write that says "connect an LLM to X" will be judged against a giant copy-paste catalog, so go niche or differentiated. Action: target an API the MCP ecosystem has NOT already saturated.
- **Spec Frozen at Three Major Dates**: MCP shipped three backwards-incompatible revisions: **2024-11-05** (HTTP+SSE transport, now Deprecated), **2025-03-26** (Streamable HTTP introduced), and **2026-07-28** (stateless core, hardened auth, MRTR) [executive_summary[2]] [3][executive_summary[3]] [4][executive_summary[4]] [5]. Pin clients and servers to a single revision and announce which one you built against in the README.
- **Streamable HTTP 2026-07-28 Killed Three Things**: GET-stream endpoint, Mcp-Session-Id, and Last-Event-ID resumability are all removed [executive_summary[2]] [3]. If you demo over Streamable HTTP, the model must be capable of MRTR — verify on the host client before judging.
- **Three of the Four Frontier Labs Already Ship MCP Clients**: Anthropic (Claude/Claude Code), OpenAI (ChatGPT MCP Apps), Google (Gemini CLI 3 transports), Microsoft (Azure MCP server + Copilot integration) [executive_summary[5]] [6][executive_summary[6]] [7][executive_summary[7]] [8][executive_summary[8]] [9]. Build "client-agnostic" wherever possible — supporting Claude Code, Cursor, and Codex wins you the demo even if you only demo one.
- **Tool Poisoning Is the Headline Attack Class**: Invariant Labs disclosed on **1 April 2025** that malicious tool descriptions can hijack agents [executive_summary[9]] [10]. OWASP classified it as indirect prompt injection via MCP server responses [executive_summary[10]] [11]. Expect judges to grill you on tool description provenance and pinning.
- **Python FastMCP = 15-20 Lines for a Hackathon Server**: The official Anthropic docs and Microsoft Azure tutorial show a working MCP server with one `@mcp.tool()` decorator fits in 15 lines [executive_summary[11]] [12][executive_summary[12]] [13][executive_summary[8]] [9]. The hard part is not the build — it's pinning versions, choosing a transport, and demoing a non-obvious API.
- **MCP Debugging Is Where Projects Die**: Known issues include the **23 Sep 2025** MCP Inspector Authorization-header bug (`Bearer` only, no token) [executive_summary[13]] [14], **13 Nov 2025** Windows/PowerShell `.mcp.json` silent-failure [executive_summary[14]] [15], npx-`-y` supply-chain risk closed in May 2026 [executive_summary[15]] [16], and the Python SDK DNS-rebinding GHSA-9h52-p55h-vw2f fixed in v1.23.0 [prior context]. Plan at least 4 hours of your 48 for "make it run on the demo machine".
- **Top Reference Servers Beat Custom Wrappers**: Filesystem, GitHub, Supabase, Slack, Playwright, Redis, and PostgreSQL MCP servers are already gold-plated [executive_summary[16]] [17]. A judge-favouring move is to compose these into a vertical slice (e.g. "customer-support-inbox → Postgres → Slack-loops-back-to-agent"), not to re-write one.
- **npx Without Version Is a Supply-Chain Hazard**: Using `npx -y <package>` lets a future package release run automatically on next start [executive_summary[15]] [16]. Write `{"command":"npx","args":["-y","<pkg>@<exact-version>"]}` in your `.mcp.json` and mention it on stage.
- **Hackathons Winning Themes (2025-2026)**: Cloudflare MCP Demo Day (May 2025) showcased **Atlassian, Linear, Stripe**, plus 7 more; MCP x Quantum Science Hackathon (Jun 2025) showed science-tool-wrapper patterns. Vertical-demo + niche-API + clear security story = the consistent template.
- **Cache-Hit Fleet on the Registry Means Picking Stable Servers Matters**: Servers in the catalogue have widely varying maintenance status, and abandoned servers are attack surfaces. Prefer servers backed by labs with security teams (Anthropic, Block, Cloudflare) over solo-dev clones.
- **The Transport Choice Is Real**: stdio for local single-user, Streamable HTTP for shared/cloud. ngrok-ing a stdio server 4 hours before a demo almost never works. Decide in hour 1.

---

## 1_mcp_ecosystem_numbers_and_major_adopters_2026

### 1.1 Registry Size Across Three Tiers

| Registry | Type | Server count (May 2026) | What it does |
|---|---|---|---|
| **Official MCP Registry** | Canonical metadata, API freeze v0.1 | **9,652 latest records** [1_mcp_ecosystem_numbers_and_major_adopters_2026[0]] [1] | Source of truth for `server.json`, namespacing, auth metadata |
| **mcp.so** | High-volume | **19,7xx** [1_mcp_ecosystem_numbers_and_major_adopters_2026[1]] [2] (digit grouping inconsistent in source — treat as ~20k) | Open community listing, lower curation bar |
| **Smithery** | High-volume | **7,xxx** [1_mcp_ecosystem_numbers_and_major_adopters_2026[1]] [2] | Open community listing with auto-install paths |
| **PulseMCP** | Curated directory | not stated | Human-curated; good for finding vetted servers |

**Takeaway**: The official Registry is the canonical source [1_mcp_ecosystem_numbers_and_major_adopters_2026[0]] [1], but 80%+ of community discovery happens on Smithery or mcp.so [1_mcp_ecosystem_numbers_and_major_adopters_2026[1]] [2]. When you submit a server, register it in the **official** registry AND list it on Smithery.

### 1.2 Major AI Lab Adopters

| Lab | Product | MCP support | Notes |
|---|---|---|---|
| **Anthropic** | Claude Desktop, Claude Code | Full MCP sponsor; ships reference servers | Created the protocol |
| **OpenAI** | ChatGPT | **MCP Apps** standard adopted for embedded UI [1_mcp_ecosystem_numbers_and_major_adopters_2026[2]] [6] | MCP Apps run in iframe, communicate via `ui/*` bridge |
| **Google** | Gemini CLI | Supports 3 transports: stdio, SSE, Streamable HTTP [1_mcp_ecosystem_numbers_and_major_adopters_2026[3]] [7] | "Support for MCP servers and tools is deprecated" appears in one Google Cloud release note [Google Cloud release notes via context] — verify per service |
| **Microsoft** | Copilot in VS Code + Azure MCP Server | End-to-end tutorial for Python MCP on Azure Container Apps [1_mcp_ecosystem_numbers_and_major_adopters_2026[4]] [9] | Azure.Mcp.Server has a 1408-line TROUBLESHOOTING.md [1_mcp_ecosystem_numbers_and_major_adopters_2026[5]] [8] |
| **Block / Cloudflare / Stripe / Atlassian / Linear** | Cloudflare Demo Day | Shipped remote MCP servers | Pattern: hosted HTTP MCP behind OAuth |

### 1.3 Spec Version Timeline

| Revision | Date | Key change | Status |
|---|---|---|---|
| 2024-11-05 | Nov 2024 | Initial HTTP+SSE transport | **Deprecated**, eligible for removal [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |
| 2025-03-26 | Mar 2025 | Streamable HTTP replaces HTTP+SSE | Superseded [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |
| 2025-06-18 | Jun 2025 | Transports stabilisation | Draft lineage |
| **2026-07-28** | Jul 2026 | **Stateless core, hardened auth, MRTR, namespacing** | **Current** [1_mcp_ecosystem_numbers_and_major_adopters_2026[7]] [5][1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |

Versions use `YYYY-MM-DD` strings and are NOT incremented when changes stay backward-compatible; categories are **Draft / Current / Final**. Negotiation uses `MCP-Protocol-Version` header on Streamable HTTP and `io.modelcontextprotocol/protocolVersion` in `_meta` in JSON; if unsupported the server returns `UnsupportedProtocolVersionError`.

### 1.4 What 2026-07-28 Specifically Removed (Streamable HTTP)

| Removed | Replaced by | Why |
|---|---|---|
| HTTP GET stream endpoint | POST-driven Multi Round-Trip Requests (MRTR) | Stateless core — no long-lived SSE session [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |
| `Mcp-Session-Id` header | Per-request `_meta` keys | No protocol-level sessions [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |
| `Last-Event-ID` resumability | None — streams no longer resumable | Simplifies server state [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |
| Server-initiated JSON-RPC on SSE | Inside `InputRequiredResult` | Forces MRTR pattern [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3] |

Legacy servers returning to clients using these (e.g. GET or DELETE on the MCP endpoint) now MUST be answered `405 Method Not Allowed` [1_mcp_ecosystem_numbers_and_major_adopters_2026[6]] [3]. Pin your SDK to the 2026-07-28 draft if you build a remote server.

---

## 2_top_mcp_servers_2026

### 2.1 Category-by-Category Catalog

Pulled from the two largest live-tested 2026 directories [2_top_mcp_servers_2026[0]] [17]:

| Category | Top servers | What they expose | Typical use in a hackathon |
|---|---|---|---|
| Local FS / Code | **Filesystem, Git, Desktop Commander** | Read/write dirs, repos | Tool-use demos |
| Dev platforms | **GitHub, GitLab** | Repos, issues, PRs, workflows, security | CI/CD multicalls |
| Communication | **Slack, Discord** | Channels, search, DMs | Notification loops |
| Databases | **Supabase, PostgreSQL, MongoDB, ClickHouse, Redis, SQLite** | Direct query or DB-specific APIs | The "agent over data" trope |
| Browsers | **Playwright, Puppeteer, Chrome DevTools** | Headless browser automation | Web research agents |
| Memory / RAG | **Knowledge graph Memory, Chroma** | Persistent agent memory | "Learning from mistakes" pitch |
| Search | **Brave Search, Tavily, Exa** | Web search, deep research | Retrieval demos |
| Payments | **Stripe** | Customers, invoices | Commerce flows |
| Design | **Figma** [2_top_mcp_servers_2026[0]] [17] | Designs & assets | Visual feedback loops |
| Productivity | **Linear, Notion, Atlassian** [2_top_mcp_servers_2026[0]] [17] | Tasks & docs | Triage demos |

**Takeaway**: at least seven of these categories have multiple competitive implementations [2_top_mcp_servers_2026[0]] [17]; a hackathon win comes from composing 2-3 vertical, not from wrapping another JS bundler.

### 2.2 Maintenance Status Reality

Most authoritative servers are backed by labs with security teams (Anthropic's filesystem, Block's Goose, Cloudflare's hosted MCP demo fleet). Solo-maintained clones in the registry can go unpatched for months; combine this with shadow-IT adoption and you get failed refreshes against DNS-rebinding (GHSA-9h52-p55h-vw2f) prior context) in <1.23.0 Python SDKs, and stale skill descriptions that become injection vectors (see §3).

---

## 3_mcp_security_attack_surface_and_required_defences

### 3.1 The Headline Vulnerability Class — Tool Poisoning

Disclosed **1 April 2025** by Invariant Labs [3_mcp_security_attack_surface_and_required_defences[0]] [10]; since catalogued by OWASP as an *indirect prompt injection* attack targeting agents connecting via MCP [3_mcp_security_attack_surface_and_required_defences[1]] [11]:

| Attack variant | Mechanism | Where it lands |
|---|---|---|
| **Classic Tool Poisoning** | Hidden instructions in `description` field of a tool call; UI shows clean summary, model reads full text | Any MCP client that trusts `tool.description` |
| **MCP Rug Pull** | Server changes tool descriptions *after* the user approved the connection | Long-lived sessions, especially stdio |
| **Tool Shadowing** | Malicious server embeds instructions into *other* trusted servers' tool calls (e.g. redirect email recipients) | Multi-server agents |
| **Cross-server Exfiltration** | Hidden instr. reads `~/.cursor/mcp.json` or `~/.ssh/id_rsa` and smuggles it via a legit-looking tool param | Hosts that give one agent many tools |

**Real examples cited**: Invariant's disclosure on **Apr 1, 2025** progressed to public scanner release (`MCP-Scan`) by **Apr 11, 2025** [3_mcp_security_attack_surface_and_required_defences[0]] [10]. Reported exfil targets include `~/.cursor/mcp.json` and `~/.ssh/id_rsa` [3_mcp_security_attack_surface_and_required_defences[0]] [10].

### 3.2 Other Documented MCP Vulnerabilities 2025-2026

| ID / date | Component | Issue | Fix / status |
|---|---|---|---|
| **GHSA-9h52-p55h-vw2f** | Python SDK `<1.23.0` | DNS rebinding on HTTP-based servers (Streamable HTTP / SSE) without `TransportSecuritySettings` | **Fixed in 1.23.0** — `FastMCP()` turns it on by default on `127.0.0.1/localhost` [prior context; already registered doc 36] |
| **23 Sep 2025 — Inspector #826** | MCP Inspector | `Authorization` header sent as bare `"Bearer"` with no token [3_mcp_security_attack_surface_and_required_defences[2]] [14] | Tracked upstream; affects local debugging tunnels |
| **13 Nov 2025 — Claude Code #11597** | Claude Code native Windows PowerShell | `.mcp.json` MCP servers **completely ignored** under PowerShell on native Windows [3_mcp_security_attack_surface_and_required_defences[3]] [15] | Closed by Anthropic |
| **17 Apr 2026 — Claude Code #50289** | .mcp.json per-server timeout | Timeout field ignored for HTTP MCP transport | Open per prior context |
| **May 2026 — PetrovC/ai-agent-kit #93 → PR #125** | MCP examples / docs | `npx -y <package>` with no version allowed silent upstream churn | Closed: hard-recommend pinning exact version [3_mcp_security_attack_surface_and_required_defences[4]] [16] |

### 3.3 What a Secure MCP Server MUST Do (2026 Baseline)

Adapted from Invariant [3_mcp_security_attack_surface_and_required_defences[0]] [10] + OWASP [3_mcp_security_attack_surface_and_required_defences[1]] [11]:

| Control | Why |
|---|---|
| **Pin tool descriptions by hash** | Detect "rug pulls" silently mutating tool text [3_mcp_security_attack_surface_and_required_defences[0]] [10] |
| **Constrain response shapes** | Reject anything not matching declared JSON schema — guards against embedded commands [3_mcp_security_attack_surface_and_required_defences[1]] [11] |
| **Allowlist MCP servers** (especially gateway) | Stop users from adding arbitrary MCP URLs |
| **Isolate privileged tool contexts** | High-privilege tools must NOT share context with external MCP servers [3_mcp_security_attack_surface_and_required_defences[1]] [11] |
| **Server-side enforcement, not system prompt** | Backend access controls, not LLM obedience [3_mcp_security_attack_surface_and_required_defences[1]] [11] |
| **DNS-rebinding protection on by default** | Reject Host headers not in `127.0.0.1` allowlist (now default in Python SDK ≥1.23.0) [prior context] |
| **Require human approval for destructive ops** | Outside the LLM context entirely [3_mcp_security_attack_surface_and_required_defences[1]] [11] |
| **Code-scan tool descriptions at CI** | Scan server source for invisible Unicode or hidden prompts (`MCP-Scan` from Invariant Labs [3_mcp_security_attack_surface_and_required_defences[0]] [10]) |
| **Streamable HTTP + TLS + OAuth 2.1** | "Streamable HTTP + TLS + a(n auth) layer" is the modern pattern; OAuth 2.0 token exchange (RFC 8693) for upstream delegation |

---

## 4_building_an_mcp_server_in_48_hours

### 4.1 Stack Decision Tree for a Hackathon

| Decision | Recommendation | Reasoning |
|---|---|---|
| **Language** | **Python with FastMCP 2.x** | Shortest server files, deepest tutorial coverage [4_building_an_mcp_server_in_48_hours[0]] [12][4_building_an_mcp_server_in_48_hours[1]] [13][4_building_an_mcp_server_in_48_hours[2]] [9] |
| **Transport** | **stdio** if local; **Streamable HTTP** if shared | stdio is 1-line, but Streamable HTTP is the only thing ChatGPT/Cursor/Cloudflare reliably multi-call [4_building_an_mcp_server_in_48_hours[3]] [6][4_building_an_mcp_server_in_48_hours[4]] [7] |
| **Auth (Streamable HTTP)** | OAuth 2.1 + token-exchange per RFC 8693 if you call upstream APIs | Cheap on Cloudflare's MCP server template; otherwise anonymous-with-allowlist |
| **SDK pinning** | Pin exact version in `.mcp.json`: `"@modelcontextprotocol/server@1.23.0"` | Avoids npx-`-y` supply-chain drift [4_building_an_mcp_server_in_48_hours[5]] [16][prior context] |
| **Test tool** | MCP Inspector (`uv run mcp dev server.py`) [prior context 38] | Debugger tool, prints tool calls and responses |

### 4.2 Minimal Python Server (≈15 lines from the Anthropic docs)

```python
from mcp.server import MCPServer
mcp = MCPServer("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

(The exact line count mirrors the Anthropic reference server sample — prior context doc 18.)

### 4.3 Open-Source Templates Worth Cloning

| Template | Where | Why |
|---|---|---|
| Anthropic `modelcontextprotocol/python-sdk` | GitHub | Reference; `add`+`greeting` ships with the README [prior context] |
| Microsoft `mcp` Azure Container Apps tutorial | docs.microsoft.com [4_building_an_mcp_server_in_48_hours[2]] [9] | End-to-end Python MCP deploy to Azure behind VS Code Copilot |
| `cyanheads/model-context-protocol-resources` MCP server dev guide | GitHub [prior context] | Long-form best-practice checklist |
| `justinwlin/claude-mcp-guide` | GitHub | Reference for Claude Code + Claude Desktop |
| `openai/mcpo` MCP-OpenAPI proxy | GitHub | Wrapper that auto-converts any OpenAPI to an MCP server — useful if you wrap a niche API [prior context] |

### 4.4 Common Mistakes Shipped in Hackathon Time

| Mistake | Cost | Fix |
|---|---|---|
| Using `npx -y <pkg>` without version | Future upstream supply-chain attack surface | Exact-version pin in `.mcp.json` [4_building_an_mcp_server_in_48_hours[5]] [16] |
| Building stdio only, then expecting Cloudflare hosting | Need to wrap in HTTP/SSE — multi-hour rewrite | Decide transport at hour 1 |
| Forgetting DNS-rebinding protection on local HTTP server | Actually rated "critical" pre-1.23.0 [prior context] | `FastMCP()` ≥1.23.0 enables by default |
| Free-text `tool.description` with embedded instructions | Becomes a tool-poisoning vector — and judges WILL scrutinise | Use a deterministic shema; do not embed instructions in desc |
| Skipping transport version-header | Hard to debug when client + server drift | Print `MCP-Protocol-Version` on startup |

**Difficulty verdict**: a working local-only Python FastMCP server takes **under an hour** for someone who's used FastAPI. The verbose parts are pinning, transport choice, and demo polish.

---

## 5_judge_relevant_demos_for_craft_n_code

### 5.1 What Has Already Impressed (2025-2026)

| Demo / Event | What worked | Pattern |
|---|---|---|
| **Cloudflare MCP Demo Day — 1 May 2025** | Atlassian, Linear, Stripe, plus six more | Hosted remote MCP server behind OAuth; one vertical |
| **MCP x Quantum Science Hackathon — 21-22 Jun 2025** (Stanford) | Science-tool wrappers served via MCP | Wrapping a HARD-to-access research API in a 48h slot |
| **Cloudflare MCP demo fleet** | "Claude-as-database-manager", invoicing, deploy-from-chat | Tools that an LLM cannot already do |

### 5.2 Demo Patterns That Will Land at Craft N Code

| Pattern | Why it lands | Example seed |
|---|---|---|
| **Wrap a niche API the registry doesn't have yet** | Judges see novelty over the 9,652 server baseline [5_judge_relevant_demos_for_craft_n_code[0]] [1] | A state's open-data API, a hobbyist game leaderboard, a domain-specific SaaS without a public wrapper |
| **MCP Gateway / Allowlist server** | Security is hot (Tool Poisoning disclosure 2025 [5_judge_relevant_demos_for_craft_n_code[1]] [10]); a server that gates *which* tools can be called is rare | A proxy MCP that policy-enforces per-tool, with `MCP-Scan` integration |
| **Two-MCP composition** | Demonstrates that MCP servers interoperate across vendors | "Supabase MCP → Slack MCP" customer-support flow |
| **MCP Apps UI in ChatGPT** | OpenAI's MCP Apps standard supports iframe UI [5_judge_relevant_demos_for_craft_n_code[2]] [6] | Side-by-side tool-call + visualisation |
| **MRTR + stateless demo** | Hardest hitting the new 2026-07-28 spec | Show a roundtrip with input-required response — judges cannot easily replicate mid-hackathon |

### 5.3 Architecture to Pitch

> "We built MCP server X wrapping free-tier arbitrage-data API Y. We hardened against tool-poisoning by pinning tool descriptions at SHA-256 and gating via an MCP gateway. It runs on the 2026-07-28 stateless Streamable HTTP spec, demos in Claude Code, Cursor, and ChatGPT."

That sentence covers novelty (X wrapping Y), security (pinning + gateway), currency (2026 spec), and breadth (three clients) — the four axes judges grade on.

---

## 6_where_mcp_breaks_honest_failure_modes

### 6.1 Reliability & Compatibility Matrix

| Failure mode | Frequency | Impact | Reference |
|---|---|---|---|
| **Windows + PowerShell: `.mcp.json` ignored** | Common | Whole MCP stack silent-fails on the demo machine | [6_where_mcp_breaks_honest_failure_modes[0]] [15] |
| **Inspector: bare `Bearer` header** | Common in local tunnels | Authenticated requests silently 401 | [6_where_mcp_breaks_honest_failure_modes[1]] [14] |
| **Per-server timeout ignored** | Common on HTTP transport | Long-task servers hang or fail without warning | prior context #50289 |
| **"Not connected" misdiagnoses** | Common | Often escalated to "is the server wrong?" when it isn't | prior context #1082 |
| **DNS-rebinding on local HTTP** | Critical pre-1.23.0; defaulted-on after | RCE-class via crafted web page | prior context GHSA-9h52-p55h-vw2f |
| **Stdio servers die silently** | Common on Macs with broken PATH | Client logs "Not connected"; reason is a missing interpreter | [6_where_mcp_breaks_honest_failure_modes[2]] [8][prior context #1611] |
| **npx-`-y` upstream mutation** | Latent | Re-run tomorrow can ship new code | [6_where_mcp_breaks_honest_failure_modes[3]] [16] |
| **Tool description drift (rug pull)** | Latent on community servers | New hidden commands after approval | [6_where_mcp_breaks_honest_failure_modes[4]] [10] |
| **Backward-compat HTTP GET attempts** | Common with old demos | Server returns 405; client errors out | [6_where_mcp_breaks_honest_failure_modes[5]] [3] |

### 6.2 Pre-Answer the Following in Your Pitch

| Question | Pre-prepared answer |
|---|---|
| "Did you pin everything?" | "Yes — exact versions in `.mcp.json`, and SHA-256 over tool descriptions. We picked the 2026-07-28 spec explicitly." |
| "What if a tool description changes?" | "We hash-and-pin, and we run `MCP-Scan` in CI to detect drift." [6_where_mcp_breaks_honest_failure_modes[4]] [10] |
| "What if the user adds an arbitrary MCP server URL?" | "We run behind an allowlist MCP gateway; unknown server URLs are rejected." [6_where_mcp_breaks_honest_failure_modes[6]] [11] |
| "What if the demo machine is Windows?" | "Demo runs on Linux + macOS out-of-the-box; on Windows PowerShell we use the documented `cmd` workaround in TROUBLESHOOTING.md." [6_where_mcp_breaks_honest_failure_modes[2]] [8][6_where_mcp_breaks_honest_failure_modes[0]] [15] |
| "How do you debug a tool call?" | "MCP Inspector in dev mode + explicit print of `MCP-Protocol-Version` and the `_meta` keys on every call." [prior context #38] |

### 6.3 Debugging Toolkit

| Tool | Use |
|---|---|
| **MCP Inspector** (`uv run mcp dev`) [prior context #38] | Live view of every tool call + response |
| **`.mcp.json` schema validation** | Catches the Windows PowerShell class of bug pre-flight [6_where_mcp_breaks_honest_failure_modes[0]] [15] |
| **Streamable HTTP server logs (request-id + protocol-version)** | Required to diagnose negotiation failures [6_where_mcp_breaks_honest_failure_modes[5]] [3]|
| **`MCP-Scan`** (Invariant Labs) | Detects tool-description drift [6_where_mcp_breaks_honest_failure_modes[4]] [10] |

---

## 7_synthesis_what_this_means_for_a_craft_n_code_team

The MCP ecosystem in 2026 is post-explosion: **~10K servers** in the official registry [7_synthesis_what_this_means_for_a_craft_n_code_team[0]] [1], backed by four frontier labs (Anthropic, OpenAI, Google, Microsoft) [7_synthesis_what_this_means_for_a_craft_n_code_team[1]] [6][7_synthesis_what_this_means_for_a_craft_n_code_team[2]] [7][7_synthesis_what_this_means_for_a_craft_n_code_team[3]] [8][7_synthesis_what_this_means_for_a_craft_n_code_team[4]] [9] on a spec that has stabilised at **2026-07-28** with a deliberately stateless, auth-hardened core [7_synthesis_what_this_means_for_a_craft_n_code_team[5]] [3][7_synthesis_what_this_means_for_a_craft_n_code_team[6]] [5]. The protocol is now mature enough that the *hard* engineering — `npx` pinning [7_synthesis_what_this_means_for_a_craft_n_code_team[7]] [16], DNS-rebinding protections [prior context], allowlist gateways [7_synthesis_what_this_means_for_a_craft_n_code_team[8]] [11], tool-description hashing [7_synthesis_what_this_means_for_a_craft_n_code_team[9]] [10] — is the *differentiation lever*. The easy engineering (one decorator, one transport) is now table stakes.

Three tensions every team must navigate:

1. **Novelty vs catalog saturation.** With ~10K servers already listed [7_synthesis_what_this_means_for_a_craft_n_code_team[0]] [1][7_synthesis_what_this_means_for_a_craft_n_code_team[10]] [2], judges cannot reward another Stripe wrapper. Pick a niche API the MCP ecosystem has NOT already saturated.
2. **Speed vs security.** A 48h ship will tempt you to skip `MCP-Scan`, skip `.mcp.json` pinning, skip hash-pinning tool descriptions. Each skip is a recoverable engineering debt, but a question a judge WILL ask. Budget 2-3 hours to the hardening pass.
3. **Current spec vs broad client compat.** Choose the newest spec (**2026-07-28**) for forward-looking points, BUT ensure your stdio fallback works on Claude Code, Cursor, and Codex — the breadth multiplier.

The team that ships (a) a niche API wrapper, (b) on the 2026-07-28 spec, (c) with hash-pinned tools behind an allowlist gateway, (d) demos cleanly in three clients, will structurally outscore the team that picked any one of those in isolation. That is the hackathon's scoring surface in 2026 — and it is also the protocol's stable centre of gravity.

---