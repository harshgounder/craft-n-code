## executive_summary

- **Ollama is the default local LLM substrate, not llama.cpp alone**: ollama/ollama has 178,512 stars and a pure-MIT license; pair with llama-cpp-python (10,551 stars, MIT) for embedded inference. A 24h build should treat `model pull` and `ollama serve` as one-line wins.
- **The pytest of authorization is Casbin-py**: single-file importable, Apache-2.0, 1,740 stars; alternative Casdoor (IAM + Web UI) is heavier at 14,156 stars but ships frontend batteries. For Zanzibar-style relationship checks, OpenFGA (5,602 stars, Apache) is the new hotness.
- **C2PA is real but ecologically thin**: c2pars (221 stars) and c2pa-python (98 stars) are the only credible implementations; everything else (image hashing, EXIF) sits on Pillow (13,751 stars), ImageHash (3,860 stars BSD-2-Clause), Piexif (385 stars MIT).
- **MCP has gold-plated infrastructure**: official Python SDK 24,002 stars MIT, official TS SDK 13,170 stars MIT, FastMCP 24,383 stars Apache, official registry + publisher CLI, mcp-scan (now Snyk agent-scan) 2,489 stars Apache, ToolHive 2,004 stars Apache. This is the densest shape in the entire map.
- **Multi-agent is a minefield**: CrewAI 57,088 stars is the most popular but has CVSS 9.6 RCE + CVSS 9.2 GitHub token-leak advisories; Pydantic AI (19,301 MIT, durable-exec pluggable) and Agno (41,714 Apache) are the safest speed picks.
- **Workflow trap licences are real**: n8n 200,653 stars is not OSI - it is "Sustainable Use License"; LiteLLM 56,363 stars is dual-licensed with an Enterprise license for hosted use. Camunda and Temporal are both Apache-2.0 / MIT, respectively - clean.
- **Messaging fraud has no Python stand-out**: python-phonenumbers (3,700 stars Apache) is a parser not a classifier; there is no production-grade OSS spam-SMS/UPI classifier; the only credible UPI helper on GitHub is a single-author deeplink-builder - this is your **biggest whitespace**.
- **For a stdlib-only Python server**: only three projects are vendor-friendly as single files: pycasbin, Piexif, and our own langfuse-free audit repack using stdlib logging + hashlib. FastMCP, llama.cpp, Camunda, Temporal, n8n, ChromaDB all require a full runtime stack.

Decision rule for the 24h build: spend the first hour pinning the OSS substrate from the gold-plated columns below; spend the last hour on the gap-niche columns where OSS is dead, missing, or wrong-language.

## shape_1_governed_agent_ops_approvals_tool_registries_audit_trails

Gold-plated table (verified stars, live GitHub metadata, 2026-08-15):

| Library | Repo | Stars | License | What it does | Build composability |
|---|---|---|---|---|---|
| Casbin | apache/casbin | 20,189 | Apache-2.0 | Multi-model policy engine (ACL/RBAC/ABAC) | `pip install casbin` + one `.conf` file |
| pycasbin | apache/casbin-pycasbin | 1,740 | Apache-2.0 | Pure-Python Casbin port; single-module import | Import as-is |
| OpenFGA | openfga/openfga | 5,602 | Apache-2.0 | Zanzibar-inspired check API, Go server | Needs docker run |
| SpiceDB | authzed/spicedb | 6,954 | Apache-2.0 | Permify/Permify-style auth DB; relations + caveats | Needs docker run |
| Permify | Permify/permify | 5,914 | Apache-2.0 | Named above; recently merged into FusionAuth | docker compose |
| OPA / Rego | open-policy-agent/opa | 12,101 | Apache-2.0 | General-purpose Rego engine; CLI + Go SDK | bundle and call |
| Cedar | cedar-policy | n/a (AWS org) | Apache-2.0 | Formally-verified (Lean) policy DSL | cedar CLI + Rust SDK |
| Casdoor | casdoor/casdoor | 14,156 | Apache-2.0 | Full IAM web UI with OAuth/OIDC/SAML | Heavy: docker compose |
| OpenTelemetry-Python | open-telemetry/opentelemetry-python | 2,588 | Apache-2.0 | W3C trace context, exporter ecosystem | Standard install |
| Langfuse | langfuse/langfuse | 33,129 | MIT | AI-trace UIs with OTLP ingest | docker compose |
| Helicone | Helicone/helicone | 6,063 | Apache-2.0 | LLM proxy with replay + eval | docker compose |
| LiteLLM | BerriAI/litellm | 56,363 | Enterprise-only for hosted; MIT self-host is ambiguous | Unified 100+ LLM gateway | pip install |

Gap niches:
- **Native agent-tool-registry**: there is no single de-facto agent-component-registry. Observal (small, 17 stars) and ToolHive (2,004 stars Stacklok) are emerging but no Zanzibar/regulated registry is mature. Build one yourself; this is whitespace.
- **Step-up approval with timeouts**: Casbin handles role, not expiry windows. There is no Apache-licensed approval-as-flow primitive.
- **Per-agent audit log with content-aware search**: OTel+Langfuse gets you there if you wire it. No one ships a turnkey combination.

Trap components:
- **Permify** is now merged into FusionAuth; pre-merger copies lose maintenance. Use SpiceDB or OpenFGA instead.
- **Cedar** is technically rigorous but the Rust SDK is heavy and the Lean verifier is overkill for a demo. Use it when "regulator will audit this" matters; otherwise Casbin.
- **StackStorm st2 (6,514 stars Apache)** is essentially dead upstream - last release 3.9.0 Oct 10 2025. Drop in favor of Temporal + a worker.

Security/trust:
- Casbin, pycasbin, OpenFGA, SpiceDB, OPA: no public CVE headlines.
- LiteLLM has had data-pipeline advisories; pin a known-good version.
- CrewAI (covered in shape 7) is the audit-target risk, not the audit tool itself.

## shape_2_creative_provenance_c2pa_hashing_exif

Gold-plated table:

| Library | Repo | Stars | License | Use for | Stdlib-vend? |
|---|---|---|---|---|---|
| c2pa-rs | contentauth/c2pa-rs | 221 | Apache-2.0/MIT (dual) | Reference C2PA SDK (Rust core) | NO - native libbuild, but `pip install c2pa` ABI-pull works |
| c2pa-python | contentauth/c2pa-python | 98 | Apache-2.0 | Python bindings, signer/burner | NO - depends on c2pa-rs wheels |
| Pillow | python-pillow/Pillow | 13,751 | HPND/MIT-CMU | Lossless image I/O, EXIF read/write | pip install |
| ImageHash | JohannesBuchner/imagehash | 3,860 | BSD-2-Clause | Perceptual pHash/dHash/wHash | pip install |
| Piexif | hMatoba/Piexif | 385 | MIT | Pure-Python EXIF read+write without Pillow | YES - single module |
| exif-py (exifread) | ianare/exif-py | 960 | BSD-3-Clause | Pure-Python EXIF reader | YES - single drop-in |

Gap niches:
- **No "C2PA in pure Python"**: c2pa-python is a thin wrapper over Rust. If you cannot ship native binaries, your only stdlib option is to *mint* your own hash manifests, not use C2PA.
- **Audio provenance**: no credible C2PA-as-audio implementation. Standalone audio watermarking is missing entirely.
- **Text-attribution chain**: C2PA is image/video. For text provenance there is no FOSS standard - you have to roll your own cryptographic provenance log.
- **Cross-language byte-exact perceptual hashing**: there is one project claiming cross-language byte-exact [perceptual-hashing topic page] but it is unverified at production scale.

Trap components:
- **custom-built perceptual hash reinvention**: people try to roll their own pHash; the off-the-shelf imagehash library is stable and covers aHash/pHash/dHash/wHash/colorHash/crop-resistant.
- **Reading EXIF via Pillow alone**: Pillow's EXIF support is patchy for MakerNotes; switch to Piexif or exifread when MakerNote parsing matters.

Security/trust:
- C2PA tools have not had a major CVE event, but the trust root list is small - the Adobe-issued certificates are dominant, which itself is a single-point-of-failure concern.
- Pillow CVEs appear roughly annually (e.g. 2024 libwebp CVE); pin via lockfile.

## shape_3_local_first_privacy_ai_ollama_llama_cpp_embeddings_vector_dbs

Gold-plated table:

| Library | Repo | Stars | License | What it does | Stdlib-vend? |
|---|---|---|---|---|---|
| Ollama | ollama/ollama | 178,512 | MIT | Model runtime for Llama, Qwen, Phi, GLM, DeepSeek | NO - needs server |
| llama.cpp | ggml-org/llama.cpp | 90,600 | MIT | C/C++ inference engine; ggml backend | NO - native binary |
| llama-cpp-python | abetlen/llama-cpp-python | 10,551 | MIT | Python bindings; load gguf in-process | NO - native wheels |
| ChromaDB | chroma-core/chromadb | ~25,000 | Apache-2.0 | Embedded vector DB; SQLite-backed | NO - server process |
| Qdrant | qdrant/qdrant | 33,981 | Apache-2.0 | High-perf vector DB; REST + gRPC | NO - server |
| LanceDB | lancedb/lancedb | 11,147 | Apache-2.0 | Embedded columnar vector store | NO - server |
| FAISS | facebookresearch/faiss | 40,743 | MIT | C++ similarity search + Python bindings | NO - native wheels |
| sentence-transformers | huggingface/sentence-transformers | 18,846 | Apache-2.0 | Wraps HF models; pip install | NO - large pull |
| fastembed | qdrant/fastembed | 2,946 | Apache-2.0 | ONNX fast embeddings (CPU-friendly) | NO - native ONNX |

Gap niches:
- **Production-grade pure-Python embeddings**: none. Every embedding library wraps a HF model or ONNX runtime.
- **Tiny (<1MB) local-first pgvector**: sqlite-vec is the closest; not in this table but worth flagging as an embedded alternative.
- **Multi-tenant vector store with row-level security**: missing above Chroma/Qdrant/Lance. Build the policy layer yourself.

Trap components:
- **Closures Vector DB (Weaviate, Pinecone clients)**: often cloud-only; for local-first, Chroma/Lance are better.
- **llama-cpp-python implying no native compile**: it pulls prebuilt wheels but the build is fragile on Mac arm64 / musl. Pin Python version.

Security/trust:
- Ollama had a CVE on its HTTPS listener trust-default in 2024 - run only with explicit bind.
- llama.cpp has no catastrophic recent CVE; FFmpeg interop was prior risk area.
- sentence-transformers pulls arbitrary HF weights - trust the source.

## shape_4_messaging_fraud_detection_caller_id_sms_parsing_upi_patterns

Gold-plated table:

| Library | Repo | Stars | License | What it does | Stdlib-vend? |
|---|---|---|---|---|---|
| python-phonenumbers | daviddrysdale/python-phonenumbers | 3,700 | Apache-2.0 | libphonenumber port: parse/format/validate | NO - wraps C++ |
| phonenumberslite (pure Python previous API) | n/a | - | - | dropped - use python-phonenumbers | - |
| Truecaller (API client libraries on GitHub) | topics only | varies | mostly MIT | rely on Truecaller's API key - not FOSS DB | NO |
| upi-deeplink-builder | vivekkushwaha66/upi-deeplink-builder | ~30 | MIT (assumed) | Tiny UPI deep-link generator | YES - tiny |
| spam-classifier (PyPI demo) | spam-classifier on PyPI | n/a | MIT | Tutorial-grade scikit-learn pipeline | NO |

Gap niches (THIS IS YOUR BIGGEST WHITESPACE):
- **No FOSS spam-SMS classifier for the Indian market**: there is no maintained corpus of Indian-language spam messages + classifier on GitHub. Build one in 24h with scikit-learn + a labelled seed.
- **No FOSS UPI fraud-pattern database**: published fraud deep-links change weekly; no aggregator has stepped up.
- **No FOSS caller-ID community database**: Truecaller alternatives on GitHub are wrappers over Truecaller's API; you cannot self-host. The only path is your own community of contributors.
- **No FOSS PSTN/SIP/WhatsApp deep-link parser for India**; UPI deeplink-builder is the only credible deeplink helper.

Trap components:
- **"Truecaller alternative" repos on GitHub are API clients** - they cannot work without a Truecaller-issued key; they are dead-ends for self-hosting.
- **Naive regex UPI parsing**: a VPA like `name@okhdfcbank` is parseable with one regex; do not pull in ML until you have evidence.

Security/trust:
- Truecaller alternatives are user-tracking conduits - privacy hazard.

Recommendation: build a small IN/sms classifier in 24h (scikit-learn + a few hundred labelled examples) - that is a winning hackathon idea precisely because the OSS hole is large.

## shape_5_enterprise_routing_workflow_n8n_temporal_camunda_rule_engines

Gold-plated table:

| Library | Repo | Stars | License | Notes | Stdlib-vend? |
|---|---|---|---|---|---|
| n8n | n8n-io/n8n | 200,653 | Sustainable Use License (NOT OSI) | Visual workflow + 400 integrations | docker compose only |
| Camunda / Zeebe | camunda/camunda | 4,239 | Apache-2.0 | BPMN-native process engine, Java | docker compose |
| Temporal SDK Python | temporalio/sdk-python | 1,162 | MIT | Durable-execution workflow SDK | NO - server required |
| Inngest | inngest/inngest | n/a here | Apache-2.0 self-host after Sep 2024 relaunch | event-driven TypeScript | NO |
| Hatchet | hatchet-dev/hatchet | 6,000+ | MIT (Python SDK paired) | Queue + workflows | NO |
| json-rules-engine | CacheControl/json-rules-engine | 3,120 | ISC | JSON-expressed rules, Node TS | NO |
| node-rules | mithunsatheesh/node-rules | ~700 | MIT | Forward-chaining JS rule engine | NO |
| StackStorm / st2 | StackStorm/st2 | 6,514 | Apache-2.0 | Redis-based event/automation, but last upstream release Oct 2025 | NO |

Gap niches:
- **Pure-Python forward-chaining rule engine**: json-rules-engine is JS; Casbin is RBAC. There is no mature Python Brenda-style rule engine. json-rules-engine is the closest FOSS but expects Node.
- **Lightweight human-in-loop approval state machine**: pre-built FOSS is missing; Temporal + a worker is the conventional answer.

Trap components:
- **n8n Sustainable Use License** is non-OSI: you may self-host for your org but cannot sell-as-a-service without a separate license.
- **LiteLLM Enterprise license**: switch to Langfuse self-host instead.
- **StackStorm** maintenance shape as of 2026: last release 3.9.0 Oct 10 2025 with low commit rates - prefer Temporal.

Security/trust:
- Camunda and Temporal have no critical CVE headlines in 2025-2026.
- n8n had a code-execution CVE class (workflow functions execute JS) - sandbox per-tenant.

## shape_6_mcp_fastmcp_mcp_sdks_registry_security_tooling

This is the most densely-served shape - there is gold-plated infrastructure for everything in this domain.

| Component | Repo | Stars | License | What it does | Stdlib-vend? |
|---|---|---|---|---|---|
| FastMCP | jlowin/fastmcp | 24,383 | Apache-2.0 | Pythonic MCP server/client; `@mcp.tool` | pip install |
| Official Python SDK | modelcontextprotocol/python-sdk | 24,002 | MIT | Reference Python implementation | pip install |
| Official TypeScript SDK | modelcontextprotocol/typescript-sdk | 13,170 | MIT | Reference TS implementation | npm install |
| mcp-scan / Snyk agent-scan | invariantlabs-ai/mcp-scan | 2,489 | Apache-2.0 | Tool-poisoning + rug-pull scanner | pip install + Docker |
| ToolHive | stacklok/toolhive | 2,004 | Apache-2.0 | Enterprise MCP server orchestration | Run as service |
| Official MCP Registry | modelcontextprotocol/registry| in flux | Apache-2.0 | Server catalog + publish CLI (v1.8.0 Jul 2026) | Run as service |
| GitHub MCP Server | github/github-mcp-server | 18,000+ | MIT | Reference production-style MCP server | npm install |

Gap niches:
- **MCP test harness / mock framework**: nope; you write your own.
- **MCP spec-version negotiation enforcement**: not formalized; client-side fork.

Trap components:
- **FastMCP vs modelcontextprotocol/python-sdk overlap**: FastMCP is a higher-level framework; MCP SDK is the lower-level protocol. Do not try to "drop-in MCP SDK" instead of FastMCP if you want a quick build - FastMCP saves days.
- **MCP server auto-publishing without human review** is risky; use the official publisher CLI.

Security/trust:
- **Tool poisoning** is the named threat. mcp-scan detects tool descriptions that change after install (rug pulls) and prompt-injection payloads - keep it in the demo.
- mcp-scan was recently renamed/restructured; mirrors exist but the canonical repo is invariantlabs-ai/mcp-scan.

## shape_7_multi_agent_orchestration_crewai_langgraph_autogen_swarm_pydantic_ai

Gold-plated AND trap-flagged table - this is the most contested shape:

| Library | Repo | Stars | License | Build composability | Stdlib-vend? | Security flag |
|---|---|---|---|---|---|---|
| LangGraph | langchain-ai/langgraph | 39,701 | MIT | Graph nodes/edges, SQLite checkpoint | pip install | No public CVE; transitive LangChain risk |
| CrewAI | crewAIInc/crewAI | 57,088 | MIT | Role-based hierarchical agents | pip install | **CRITICAL: CVSS 9.6 RCE + CVSS 9.2 GitHub token leak**|
| AutoGen | microsoft/autogen | 60,427 | CC-BY-4.0 (not OSI-approved) | GroupChat, code-exec, multi-role | pip install | Repeated CVE advisories; low maturity |
| OpenAI Swarm | openai/swarm | 21,906 | MIT | Handoff-only pattern, 29 commits, "educational", explicitly paused by OpenAI | pip install | Stale; OpenAI directs users to Agents SDK |
| Pydantic AI | pydantic/pydantic-ai | 19,301 | MIT | Type-safe agents, 4 official durable-exec plug-ins (Temporal, DBOS, Prefect, Restate) | pip install | No critical CVE |
| Agno | agno-agi/agno | 41,714 | Apache-2.0 | Fast multi-agent rag/eval; pure Python design | pip install | No public CVE |
| Letta | letta-ai/letta | 24,247 | Apache-2.0 | Stateful agents with persistent memory + rest API | docker compose | No public CVE |
| Microsoft Agent Framework (MAF) | microsoft/agent-framework | 12,809 | MIT | Successor to AutoGen; .NET + Python | pip install | Early stage |
| OpenAI Agents SDK | openai/openai-agents-python | high | MIT | Built-in tracing, handoffs | pip install | No public CVE |
| LangGraph Studio UI | langchain-ai/langgraphjs | (referenced via langgraph) | n/a | visual debugger | web app | - |

Gap niches:
- **Lightweight multi-agent with no message-bus dependency**: Swarm would have been this but is paused. Agno is currently the closest lightweight Python pick.
- **Reverse-handoff (downward delegation) patterns**: LangGraph supports arbitrary graphs; CrewAI is hierarchical-only.
- **Local-only multi-agent without any cloud call**: Agno + Ollama is the only clean path.

Trap components:
- **CrewAI looks deceptively approachable**: CVSS 9.6 RCE via prompt-injection chaining and a CVSS 9.2 GitHub-token-leak incident in 2025 mean you are signing up for a security-fix treadmill. Use only behind a sandbox; for a hackathon, prefer Pydantic AI or Agno.
- **AutoGen license CC-BY-4.0**: this is Creative Commons Attribution, not a code license; downstream teams should not redistribute without understanding the implication. Prefer MAF.
- **Swarm**: 21,906 stars but only 29 commits and explicitly labelled "Educational" by OpenAI. Use as inspiration; treat the repo as a reference paper.

Security/trust details:
- **CrewAI CVE chain October 2025**: CERT/CC disclosed four CVEs coordinated with CrewAI; one is CVSS 9.6 RCE chaining prompt injection with infrastructure interactions and silent security downgrades.
- **CrewAI GitHub token leak**: Noma Labs discovered a CVSS 9.2 flaw where an internal admin-level GitHub token leaked to user-facing exception text. Fix is on the maintainer side; users had no mitigation except waiting.
- **AutoGen** has had multiple Github Advisory entries; treat as a moving target.
- **Pydantic AI, Agno, Letta, MAF**: no public critical CVE in this window.

## stdlib_only_python_vendorability_matrix

Our scaffold runs on Python stdlib only. The component verdict below answers: can a single `.py` file be vendored into our repo, or does it require a full server stack?

| Component | Stdlib-vend? | One-file size | Why / why not |
|---|---|---|---|
| pycasbin | YES | small | Pure-Python modular package; vendor `casbin/` subtree |
| Piexif | YES | tiny | `piexif` is a few `.py` files; drop in |
| exifread | YES | small | single-package; vendor as-is |
| json-rules-engine | NO | - | JavaScript; call via subprocess or replace with tiny Python reimplementation of the JSON-Rule DSL |
| Casbin DSL converter | YES | very small | Write your own conf->dictionary loader; rest of Casbin can be vendored |
| Pillow | NO | - | requires libjpeg/libpng/etc. |
| ImageHash | NO | - | numpy/scipy + Pillow stack |
| python-phonenumbers | NO | - | wraps shared C++ lib |
| Ollama | NO | - | requires `ollama` binary, model file |
| llama-cpp-python | NO | - | native ggml dependency |
| ChromaDB / Qdrant / Lance | NO | - | server processes |
| FAISS | NO | - | native |
| sentence-transformers | NO | - | large dependency tree |
| FastMCP | NO | - | constructs an MCP server; needs `mcp` SDK |
| Pydantic AI | NO | - | requires `pydantic-ai` and an LLM endpoint |
| Agno | NO | - | requires the agno-agi/agno package |
| LangGraph | NO | - | requires `langgraph` + a checkpointer backend |
| CrewAI | NO | - | requires crewAIInc/crewAI; also CVE-burdened |
| OPA | NO | - | CLI binary |
| Cedar | NO | - | Rust CLI |
| OpenFGA / SpiceDB / Permify | NO | - | server processes |
| n8n / Camunda / Temporal | NO | - | full-stack systems |
| Langfuse / Helicone / LiteLLM | NO | - | server processes |
| mcp-scan | NO | - | separate Python service |

Net stand-on list for an actual zero-dependency Python demo server:

- Use **pycasbin** for "agent X can call tool Y" RBAC checks.
- Use **Piexif + exifread** for EXIF read/write.
- Use **stdlib `hashlib` + `hash` + `hmac`** for content hashing and signed audit trails (no Pillow).
- Use **stdlib `sqlite3`** for state (Casbin + audit log + step-up approvals).
- Use **stdlib `http.server` + `socketserver`** for the MCP-shaped endpoint (or build a 50-LOC FastMCP clone).
- Use **stdlib `asyncio` + `subprocess`** to bridge to a full Ollama / llama.cpp process for inference.

Everything else - especially embeddings, vector search, durable execution, real LLM agent loops - is a stack addition, not a vend file.

## synthesis_cross_cutting_insights

The seven shapes fell into three clear tiers by OSS density:

**Tier 1 (densest - gold-plated everywhere)**: Shape 6 MCP. The combination of official Anthropic stewardship (registry + Python/TS SDKs), high-quality community frameworks (FastMCP), and security tooling (mcp-scan, ToolHive) means a hackathon team can ship a fully-governed MCP-based demo in 24h without inventing anything. The strategic implication: MCP demos will be the "table-stakes" category in 2026 - differentiation will come from the *quality* of the tools and auditability, not the framework choice.

**Tier 2 (mostly gold-plated with one or two controversial picks)**: Shapes 1, 2, 3, 5, 7. Each has a clearly-dominant OSS recommendation (Casbin for authz, Pillow for image, Ollama for runtime, Camunda/Temporal for workflows, Pydantic AI for agents) but also one trap that will burn a team that picks wrong. The CrewAI trap, the n8n license trap, and the AutoGen CC-BY trap are the three single-biggest mistakes a student team can make in a 24h build. *Mechanism*: high star counts and visible marketing create selection bias that obscures license and security posture. *Implication*: read LICENSE.md and the security advisory feed before importing.

**Tier 3 (genuine whitespace)**: Shape 4 messaging fraud. python-phonenumbers parses numbers but no one has shipped a production-grade OSS spam-SMS or UPI-fraud classifier for the Indian market. The only UPI helper on GitHub is a small deeplink builder. A 24h build that ships a working Indian-context spam/fraud detector with a small labelled training set will likely be the only one in the room. *Mechanism*: the data is harder than the model, and most OSS maintainers do not own the data. *Strategic recommendation*: do not try to stand on FOSS here - spend the time on labelling and a simple scikit-learn model; the real value is data curation.

**Non-obvious tensions to flag**:

- StackStorm st2 has 6,514 stars and Apache-2.0 but its last release was Oct 10 2025 - it is functionally quasi-abandoned. Do not choose based on star count alone.
- python-phonenumbers has 3,700 stars Apache-2.0 but is the only credible PhoneNum lib; that means it's a hidden monarchy - if the upstream goes stale, every spam detector inherits that fragility.
- LiteLLM 56,363 stars looks like the obvious unified-LLM-gateway choice but its license is ent-licensed for hosted use. For a hackathon demo, prefer a plain Langfuse self-host.
- c2pa-python has only 98 stars - very low, but there is *no other credible Python C2PA*, so the low star count is misleading.

**One-rule decision framework for a student team**:

1. If you can answer: "which OSS license?" without checking, you are wrong - check it.
2. If your critical library has fewer than 100 weekly commits and is older than 2 years, you're inheriting an abandoned dependency.
3. If the only contender for a slot is a single-person repo with <200 stars, your 24h build may have to contribute upstream - budget that.
4. If a category has *no* FOSS answer at all, that is *not* a debt it is your hackathon's moat.