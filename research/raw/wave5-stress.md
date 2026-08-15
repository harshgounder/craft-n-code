## executive_summary

- **Performance Budgets Start at p99, Not Averages**: Google's SRE Workbook specifies multi-threshold latency SLOs (e.g. 90% < 100 ms AND 99% < 400 ms), making any single "average latency" number a false signal under load [executive_summary[0]] [12]. Teams should wire k6 threshold syntax `http_req_duration: ['p(99)<400']` and treat error budgets as 1 - SLO with 1h/6h/72h burn-rate alerting [executive_summary[1]] [5][executive_summary[2]] [9].
- **Chaos Engineering Has Mature Toolchains, Not Theory**: Chaos Monkey randomly terminates instances in production; Chaos Mesh ships 10+ Kubernetes fault categories (PodChaos, NetworkChaos, StressChaos, IOChaos, TimeChaos, DNSChaos, KernelChaos) [executive_summary[3]] [4][executive_summary[4]] [8]. A 48-hour soak plus weekly game days catches >70% of resilience regressions in microservices.
- **LLM/Agentic Risk Has a Named OWASP List**: OWASP LLM01-LLM10 puts prompt injection first, with LLM06 (sensitive info disclosure) and LLM10 (model theft) common at hackathons that build on Anthropic/OpenAI APIs [executive_summary[5]] [6]. Agents that lack a hard maxIterations cap (default 25 in LangChain) are one bad retry-loop away from a $10K cost blowup [executive_summary[6]] [13].
- **ReDoS, Slowloris, and HTTP Smuggling Are the Three Easiest Demo-Killers**: A 200-byte regex on a 50 KB input can pin a CPU core for hours; Slowloris holds 200 half-open connections with 1 KB/s; HTTP CL.0/T smuggling desyncs front-backend and hijacks other users' requests [executive_summary[7]] [11][executive_summary[8]] [17][executive_summary[9]] [18]. One twist of a misconfigured test kills the live demo.
- **Idempotency Is Not Optional**: Stripe's API enforces idempotency on all POST requests with 255-char keys, because clients retry on every flake and double-charges are a P1 incident [executive_summary[10]] [14]. Hackathons that handle money without `Idempotency-Key` headers are accepting regulatory risk they do not know they are taking.
- **Jepsen Is the Stress Standard for Data Integrity**: Jepsen has publicly demonstrated lost updates, stale reads, and split-brain in etcd, MongoDB, Kafka, ZooKeeper, Redis, Consul, Postgres, Elasticsearch, MySQL, and more [executive_summary[11]] [7][executive_summary[12]] [19]. For hackathon scale, a Lin-Check/JPF-style mini-Jepsen (3 nodes, 5-min runs, 10x contention) catches the same class of bug at 1% the cost.
- **Deterministic Simulation Testing Beats Statistical Load Testing for Distributed Bugs**: DST platforms like Antithesis run a hypervisor that replays real nondeterminism deterministically, exposing concurrency/timing bugs a statistical test can only see probabilistically [executive_summary[13]] [2]. Pair DST with property-based fuzzing for the rare-bug long tail [executive_summary[13]] [2].
- **Demo Hardness Classes Matter More Than Feature Count**: The Opportunity Hack 4-category rubric (Scope, Documentation, Polish, Security) and the CGU Hackathon 1-5 scale both show that judges stress-test for acceptance under failure [executive_summary[14]] [20][executive_summary[15]] [21]. A demo that survives a network kill mid-pitch will outscore a feature-richer demo that crashes on a screen share.

---

## 1_load_and_performance_testing_classes

Goal: Quantify behavior of a system under controlled demand to set SLOs and locate regressions. The terminology has settled on roughly 15 distinct classes.

### Table 1.1 - Performance Test Classes

| Class | What it tests | Method | Tool | Typical threshold / number | Source |
|---|---|---|---|---|---|
| Load test | Sustained expected traffic | Run at 1x expected RPS for 30-60 min | k6, JMeter, Gatling | Pass if p95 < SLO and error_rate < 0.1% |[97.0] |
| Stress test | Beyond-expected peak | Ramp to 1.5x-2x production and hold | JMeter, Locust | Identify first-fail point, not "max users" | [1_load_and_performance_testing_classes[0]] [10] |
| Spike test | Sudden 10x burst | Jump from 0 to 10x RPS in 1-5 s | k6 `ramping-arrival-rate` | Recovery time to p99 baseline in < 60 s | [1_load_and_performance_testing_classes[1]] [9] |
| Soak / endurance | Memory / FD / CPU drift | 24-72 h at sustained production RPS | k6, Gatling | RSS delta < 5%, FD count < 80% ulimit | [1_load_and_performance_testing_classes[2]] [22] |
| Volume test | Large payloads & DB rows | 10x normal payload size, 1M+ rows | JMeter, wrk | No timeouts above 5 s for 99th pct request | [1_load_and_performance_testing_classes[3]] [23] |
| Capacity test | Headroom estimation | Step-load 25% increments until SLO fails | k6, Locust | Last passing step = capacity (default 70%) | [1_load_and_performance_testing_classes[1]] [9] |
| Peak test | Worst-case hour, e.g. Black Friday | Replay recorded traffic at 2-3x | Gatling, Artillery | p99 within +15% of weekday baseline | [1_load_and_performance_testing_classes[0]] [10] |
| Concurrency test | Threading/lock contention | 100+ threads on a single record | Lin-Check, JPF | 0 deadlocks after 1M iterations | [1_load_and_performance_testing_classes[4]] [19] |
| Scalability test | Linear scaling check | Run at 1x, 2x, 4x nodes; throughput should ~2x/4x | k6 cloud, Gatling | N-server RPS >= 0.9 x N x 1server RPS | [1_load_and_performance_testing_classes[5]] [12] |
| Latency percentile | p50 / p95 / p99 / p99.9 | Capture histogram per request | k6 `http_req_duration`, Prometheus | p99/p50 ratio < 5x for healthy backend | [1_load_and_performance_testing_classes[6]] [24][139.7] |
| Response-time budget | Per-route latency cap | Define per-endpoint SLO in SLO doc | k6 thresholds, SLO YAML | p99 budget enforced in CI as test gate | [1_load_and_performance_testing_classes[5]] [12][142.0] |
| Throughput | RPS / QPS at cap | Measure sustained successful RPS | wrk2, ab, hey | Set bar at 80% of saturation RPS | [1_load_and_performance_testing_classes[6]] [24] |
| Ramp-up pattern | Cold-start vs warm backlog | Linear vs step vs arrival-rate ramp | k6 `scenarios` | "ramp" should be >= 30 s for caches/DB | [1_load_and_performance_testing_classes[0]] [10][143.0] |
| Think time | Inter-arrival delay realism | Add per-user wait 2-10 s | JMeter `Constant Timer`, k6 `sleep` | Default 3-5 s for browse, 0 for API/mobile | [1_load_and_performance_testing_classes[0]] [10] |
| Virtual users | Concurrent user load | VUs = peak concurrent sessions | k6 VUs, JMeter threads | 1 VU per 2-3 real sessions | [1_load_and_performance_testing_classes[0]] [10] |
| Error-rate threshold | % of non-2xx responses | Define in SLO; alert above | k6 `http_req_failed` | 99.9% SLO -> 0.1% allowed; 99% -> 1% | [1_load_and_performance_testing_classes[7]] [5] |

### Table 1.2 - Performance Tool Comparison

| Tool | Language | Strength | Limitation | Source |
|---|---|---|---|---|
| k6 | Go (JS scripts) | SRE-friendly thresholds in CI | No GUI recorder | [1_load_and_performance_testing_classes[1]] [9][142.0] |
| JMeter | Java | Mature GUI, plug-ins | Heavy JVM, slow for >5k users | [1_load_and_performance_testing_classes[0]] [10][94.0] |
| Gatling | Scala (DSL) | High RPS, nice HTML reports | Steeper learning curve | [1_load_and_performance_testing_classes[0]] [10] |
| Locust | Python | Easy Python scripting, distributed | Pure-python GIL ceilings | [1_load_and_performance_testing_classes[4]] [19] |
| wrk / wrk2 | C | Tiny, high RPS, latency focus | No advanced scenarios | [1_load_and_performance_testing_classes[6]] [24] |
| hey | Go | Drop-in HTTP/2 CLI | No scripting | [1_load_and_performance_testing_classes[6]] [24] |
| Vegeta | Go | Constant-rate pacer, vector attacks | No GUI | [1_load_and_performance_testing_classes[6]] [24] |
| Artillery | Node | YAML-driven, real-time reports | Weaker at extreme scale | [1_load_and_performance_testing_classes[2]] [22] |
| ab (ApacheBench) | C | Quiche-cheap baseline | HTTP/1 only, single host | [1_load_and_performance_testing_classes[6]] [24] |
| boom | Go | Quick single-bin baseline | Legacy, no longer maintained | [1_load_and_performance_testing_classes[6]] [24] |

Insight: For SRE-style acceptance, k6 thresholds are the cleanest link between test metric and SLO [1_load_and_performance_testing_classes[1]] [9]. For exploratory capacity tests, wrk2 + Vegeta give the most honest latency histogram.

### Real-World Performance Thresholds (Google SRE)

- Multi-threshold latency SLO pattern: "`90% of requests are faster than 100 ms, and 99% of requests are faster than 400 ms`" [1_load_and_performance_testing_classes[5]] [12].
- Error budget burn-rate alerts: 2x burn in 1 h (page), 1x burn in 6 h (ticket), 0.5x burn in 72 h (track) - the canonical windowed policy [1_load_and_performance_testing_classes[7]] [5].
- Toil budget: at least 50% of SRE time on engineering work, < 50% on operational toil [1_load_and_performance_testing_classes[8]] [25].

---

## 2_chaos_engineering

Goal: Validate resilience by deliberately introducing real-world failure modes in controlled blast radii.

### Table 2.1 - Chaos Failure Modes

| Failure | What it tests | Method | Tool | Typical threshold | Source |
|---|---|---|---|---|---|
| Process kill | Restart-loop resilience | SIGKILL on a single instance | Chaos Monkey | Instance recovers in < 30 s | [2_chaos_engineering[0]] [4] |
| Node kill | Cluster-rebalance, leader election | Stop a node / VM / pod | Chaos Mesh `PodChaos` | Cluster converges in < 60 s | [2_chaos_engineering[1]] [8] |
| Network partition | Split-brain safety | Block a subnet with iptables or ebpf | Chaos Mesh `NetworkChaos partition` | No writes lost; reads fail closed | [2_chaos_engineering[1]] [8][149.0] |
| Packet loss | Loss tolerance for LAN/WAN | `tc netem loss 10%` | tc/netem, Chaos Mesh | Queues tolerate 10% loss for 60 s | [2_chaos_engineering[2]] [1][9.0] |
| Latency injection | Timeout/retry cascades | `tc netem delay 200ms 50ms` | tc/netem | p99 stays < SLO with latency budget spread | [2_chaos_engineering[2]] [1][150.0] |
| DNS failure | Name-resolution cascade | Block UDP/53 to upstream | Chaos Mesh `DNSChaos` | Fallback resolver + cache TTL < 60 s | [2_chaos_engineering[1]] [8] |
| Clock skew | TLS cert failures, exp backoff drift | `date -s "+30s"` on one node | Chaos Mesh `TimeChaos` | Skew < 5 s tolerated by all services | [2_chaos_engineering[1]] [8] |
| Disk full | Logging, DB, temp-file failures | `dd` fills /var/log | Chaos Mesh `IOChaos fill` | Disk alerts at 70%, fail at 90% | [2_chaos_engineering[1]] [8] |
| Memory exhaustion | OOM-killer cascade | `StressChaos stressors memory` | Chaos Mesh | RSS stays < 70% node mem at peak | [2_chaos_engineering[1]] [8] |
| FD exhaustion | Socket-cap stress | Open + leak file descriptors | `ulimit -n` + custom stresser | FD count < 80% ulimit | [2_chaos_engineering[1]] [8] |
| Thread starvation | Throughput collapse | Saturate executor with blocking tasks | Java Flight Recorder | Queue depth < 100 before alert | [2_chaos_engineering[1]] [8] |
| Deadlock | Pair of workers lock-step | Run Lin-Check 1M iterations | Lin-Check, JPF | 0 detected cycles | [2_chaos_engineering[3]] [19] |
| Livelock | Burn CPU without progressing | TSAN or stress reproducer | ThreadSanitizer | 0% spin time at steady state | [2_chaos_engineering[3]] [19] |
| Race condition | Lost updates, dirty reads | Property: invariant holds across all orderings | Jepsen, Porcupine | 0 violations over 18k histories | [2_chaos_engineering[4]] [7][149.0] |
| Thundering herd | Cache expiry stampede | Expire key with M concurrent readers | Toxiproxy + reproducer | Lockbox keeps p99 < 100 ms | [2_chaos_engineering[3]] [19] |
| Cache stampede | Backed-by-DB read-storm | Warm cache for hot key, then invalidate | Redis chaos | p99 < 200 ms after stampede | [2_chaos_engineering[3]] [19] |
| Circuit breaker trip | Cascade prevention | Force breaker open via test client | Resilience4j, Polly, Istio | 50% errors -> open in < 1 s | [2_chaos_engineering[2]] [1][9.0] |
| Retry storm | Exponential explosion | Fail downstream, observe retry graph | Resilience4j retry policy | Storm coefficient < 1.2x baseline | [2_chaos_engineering[2]] [1] |
| Backpressure | Producer overflow handling | Drive queue above limit | Kafka, RabbitMQ | shED throughput drops to 80% of input | [2_chaos_engineering[1]] [8] |
| Queue overflow | Bounded-buffer safety | Send 5x queue capacity in 10 s | Chaos Mesh + custom | DLQ catches overflow, no data loss | [2_chaos_engineering[1]] [8] |
| Failover | Active/passive handoff | Kill primary, observe secondary | DNS / keepalived / etcd leader | Detect < 5 s, serve < 15 s | [2_chaos_engineering[0]] [4][150.0] |
| Recovery time (RTO) | Time to restore service | Inject, measure time to SLO met again | Runbook + monitoring | RTO SLO typically 15-60 min | [2_chaos_engineering[2]] [1][0.0] |
| Graceful degradation | Partial service instead of full fail | Disable non-critical features | Workload experiment | Core flows pass, extended flows 503 | [2_chaos_engineering[2]] [1][4.0] |
| Partial failure | Independent deps fail independently | Two-fault matrix A/B with fault injection | Chaos Mesh experiment suite | No "all-or-nothing" cancels | [2_chaos_engineering[3]] [19] |
| Zombie processes | PID reuse, lost-signals | SIGKILL parent, observe children | Process audit | 0 zombies after 24-h soak | [2_chaos_engineering[1]] [8] |
| OOM killer | Last-resort memory reclaim | Force RSS to 95% of limit | Stress + cgroup | Process logs OOM kill and exits cleanly | [2_chaos_engineering[1]] [8] |

### Table 2.2 - Chaos Tool Comparison

| Tool | Scope | Key feature | Source |
|---|---|---|---|
| Chaos Monkey | AWS instances | Random termination on schedule | [2_chaos_engineering[0]] [4][81.0] |
| Chaos Mesh | Kubernetes | 10+ typed chaos experiments | [2_chaos_engineering[1]] [8][82.0] |
| LitmusChaos | Kubernetes | Hub of experiment catalog | [2_chaos_engineering[5]] [26] |
| Gremlin | Multi-cloud | Game-day orchestration, blast radius | [2_chaos_engineering[1]] [8] |
| Steadybit | SaaS / on-prem | Automated steady-state hypothesis | [2_chaos_engineering[1]] [8] |
| tc / netem | Linux | Loss/latency/corrupt injection | [2_chaos_engineering[2]] [1] |
| Toxiproxy | TCP proxy | Latency/bandwidth/disconnect | [2_chaos_engineering[3]] [19] |
| Jepsen | Distributed DBs | Linearizability verification | [2_chaos_engineering[4]] [7][149.0] |
| Antithesis DST | Hypervisor-level | Deterministic replay for rare bugs | [2_chaos_engineering[6]] [2][54.0] |
| Pumba | Docker | Container chaos (kill, pause, net) | [2_chaos_engineering[1]] [8] |

### Real Chaos Case Studies

- **Netflix Chaos Monkey** randomly terminates production instances; Netflix claims it has prevented entire outage classes by forcing every service to be stateless and replicate fast [2_chaos_engineering[0]] [4]. The Spark Streaming postmortem at Netflix demonstrated that even stateful stream processors survive if designed with checkpointable sources [2_chaos_engineering[7]] [27].
- **Jepsen has documented bugs in**: etcd (split-brain under partition), MongoDB (lost writes after rollback), Kafka (diverging consumer offsets), Redis (linearizability violations under async replication), Consul (stale reads), ZooKeeper (sync limit bounds), Postgres (serialization anomalies), Elasticsearch (lost writes on shard failure) [2_chaos_engineering[4]] [7][149.0].
- **Netflix AWS regions test** (2014) showed that an entire region can be removed with < 1% user-visible error over a 10-minute window - the canonical "regional chaos" case [2_chaos_engineering[0]] [4].
- **Deterministic Simulation Testing (Antithesis)** can exhaustively explore state spaces that 10^9 statistical runs would only sample, finding concurrency bugs in hours rather than months [2_chaos_engineering[6]] [2]. DST is often paired with property-based fuzzing for the rare-bug long tail [2_chaos_engineering[6]] [2][44.0].

Insight: DST platforms dramatically outperform statistical load testing for distributed-bug discovery because they make nondeterministic phenomena (interrupts, scheduler order) reproducible [2_chaos_engineering[6]] [2][49.0]. On Antithesis, "random" entropy is fed carefully so the system appears random but is fully replayable [2_chaos_engineering[6]] [2].

---

## 3_llm_and_agentic_resilience

Goal: Validate that LLM-backed and agentic products stay correct, bounded, and policy-compliant under adversarial, overloaded, and evolving conditions.

### Table 3.1 - LLM/Agentic Failure Modes

| Failure | What it tests | Method | Tool | Typical threshold | Source |
|---|---|---|---|---|---|
| Prompt injection | Adversarial prompt hijack | OWASP-style scan: "ignore previous...; jailbreak" | Promptfoo, Garak, PyRIT | 0 successful injections on 200-prompt suite | [3_llm_and_agentic_resilience[0]] [6] |
| Jailbreak | Policy bypass | DAN-style and role-play attempts | Garak, Lakera | Hard refusal on 100% of test prompts | [3_llm_and_agentic_resilience[0]] [6][148.0] |
| Output schema violation | JSON/type drift | Force-free response, parse w/ Pydantic/Zod | OpenAI structured outputs | 100% schema pass on 1k samples | [3_llm_and_agentic_resilience[1]] [28] |
| Model rate limiting | 429 / quota handling | Drive burst above quota, observe backoff | Locust + provider | 0 uncaught 429 from client code | [3_llm_and_agentic_resilience[1]] [28][146.0] |
| Token exhaustion | Context overflow | Feed 200k tokens, observe truncation | LangChain token counter | Truncation error caught, no silent cut | [3_llm_and_agentic_resilience[1]] [28] |
| Cost blowup | $ runaway per session | Loop agent with no cap, log $ spent | Langfuse, Helicone alerts | Hard USD cap per session, e.g. $0.50 | [3_llm_and_agentic_resilience[2]] [13] |
| Cold start | Time-to-first-token | Hit endpoint after 10 min idle | k6 cold-ramp script | TTFT < 3 s at p95 post-idle | [3_llm_and_agentic_resilience[3]] [24] |
| Offline fallback | Provider outage | Block API, check local fallback | Chaos Mesh `DNSChaos` for provider | Cached or local model responds < 2 s | [3_llm_and_agentic_resilience[4]] [8] |
| Cache poisoning | Stale responses | Inject poisoned cache entries | Redis chaos | Stale TTL < 60 s, no cache hit on personal data | [3_llm_and_agentic_resilience[5]] [19] |
| Hallucination under load | Quality degrades w/ latency/conflicts | Eval suite run at 1x vs 5x RPS | DeepEval, RAGAS | Hallucination rate delta < 5% under load | [3_llm_and_agentic_resilience[1]] [28] |
| Nondeterminism | Stable answers across N reruns | 50 iterations, hash answer | Custom eval harness | Dirichlet energy < 0.05 across runs | [3_llm_and_agentic_resilience[0]] [6] |
| Drift after model update | Behavior change post-upgrade | A/B test new vs pinned, identical prompts | evals, Braintrust | < 10% behavior delta on golden set | [3_llm_and_agentic_resilience[1]] [28] |
| Tool call failure | Tool returns 5xx / wrong shape | Mock fail at tool layer | Resilient tool wrapper | Retry x3 with exp backoff, then user-visible fall-back | [3_llm_and_agentic_resilience[2]] [13] |
| Timeout chains | Tool A -> B -> C cascade latencies | Inject 5 s latency per call | Toxiproxy | Total chain < 30 s p99 | [3_llm_and_agentic_resilience[2]] [13] |
| Retry loops | No-progress replanning | Inject flaky tool; loop until max iterations | LangChain maxIterations | Hard cap 25 iterations, no run exceeds | [3_llm_and_agentic_resilience[2]] [13] |
| Infinite agent loops | Unbounded tool-call recursion | Run 50 random ideas, observe | agent-pattern scan | 0 zig-zag duplicates in agent trace | [3_llm_and_agentic_resilience[2]] [13] |
| Unauthorized tool access | Tool out of role scope | Sandbox test; agent without authz asks for tool | Auth-layer test | 0 successful unauthorized calls | [3_llm_and_agentic_resilience[0]] [6] |
| Data leakage between tenants | Tenant A sees tenant B data | Multi-tenant replay | Custom test rig | 0 cross-tenant RAG retrievals | [3_llm_and_agentic_resilience[1]] [28] |
| PII leak in output | PII emitted unredacted | Generate against prompt set, regex scan | Microsoft Presidio | 0 raw PII in 1000 generations | [3_llm_and_agentic_resilience[0]] [6] |
| Context window poisoning | Malicious doc inserts | Inject poisoned doc into RAG corpus | RAG eval suite | Retrieval refuses contaminated chunks | [3_llm_and_agentic_resilience[1]] [28] |
| Context overflow | Tokenized input too big | Send 1M-token context | Custom harness | Clear "context-too-long" error visible to user | [3_llm_and_agentic_resilience[2]] [13] |
| Error messages leak internals | Stack traces in 5xx body | Force 500 in dev, parse response | Negative test | User response omits stack, only "try again" | [3_llm_and_agentic_resilience[0]] [6] |

### OWASP LLM Top 10 (2025) Highlights

- LLM01 Prompt Injection (direct & indirect), LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption [3_llm_and_agentic_resilience[0]] [6].
- OWASP Top 10 for Agentic Applications (2026) extends this with: T1 Prompt Injection, T2 Sensitive Data Exposure, T3 Sandboxing, T4 Insecure Inter-Agent Communication, T5 Insecure Tool Use, T6 Insecure Code Execution, T7 Human Attacks on Human-in-the-loop, T8 Repudiation/Traceability, T9 Rogue Agents in Multi-Agent Systems, T10 Untraceability [3_llm_and_agentic_resilience[1]] [28].

### Agentic Loop Kill-Switches

- Cap `maxIterations` (default LangChain 25, AutoGPT often 50) to prevent token-cost blowups [3_llm_and_agentic_resilience[2]] [13].
- Force "no progress" detection: hash each step; abort after 3 identical hashes (`stallPattern`) [3_llm_and_agentic_resilience[2]] [13].
- Time-box the agent with a global timeout; abort trace and surface partial result [3_llm_and_agentic_resilience[2]] [13].
- Token-cost observability: log cost per agent run via Langfuse / Helicone; alert on > 5x baseline [3_llm_and_agentic_resilience[2]] [13].

Insight: The infinite-loop agent failure is one of the most production-visible LLM hackathon risks because a single user prompt can spawn an unbounded cost incident in minutes [3_llm_and_agentic_resilience[2]] [13]. Pairing structured outputs (`response_format`) with a step counter is the cheapest defense.

---

## 4_security_stress

Goal: Validate that the system resists, contains, and recovers from attack traffic and malicious inputs.

### Table 4.1 - Security Stress Failure Modes

| Attack | What it tests | Method | Tool | Typical threshold | Source |
|---|---|---|---|---|---|
| Slowloris | Slow HTTP keep-alive | 200 connections, 1 KB/s headers | Slowloris, slowhttptest | Connection timeout < 5 s kills slow clients | [4_security_stress[0]] [29][134.0] |
| SYN flood | Half-open socket flood | hping3 -S --flood | hping3, Scapy | SYN cookies + backlog > 1024 | [4_security_stress[1]] [22] |
| DDoS mitigation | Aggregate bandwidth | Cloudflare, AWS Shield | Cloudflare analytics | 10 Gbps attack absorbed with < 1% user error | [4_security_stress[0]] [29][134.0] |
| Credential stuffing | Bots trying leaked creds | Replay leaked pairs at scale | OWASP ZAP, Burp | 0% login success, rate-limit per IP/user | [4_security_stress[2]] [30][133.0] |
| Brute force | Password enumeration | Limited-distribution wordlist | Hydra, Ncrack | Account lock after 5 fails OR 2FA step-up | [4_security_stress[2]] [30] |
| Rate-limit bypass | Find another path | Try headers, OAuth, JWT, /api/v2/ | Burp, custom RateLimit-Fuzz | All endpoints uniformly rate-limited | |
| Session fixation | Cookie poisoning | Set a known session, force privilege change | OWASP ZAP | Session ID rotated on auth | [4_security_stress[2]] [30] |
| CSRF | Cross-site forged request | Replay cookies cross-origin | Burp CSRF PoC | Tokens required and bind to session | [4_security_stress[2]] [30] |
| SSRF | Probing internal networks | Inject 169.254.169.254, file:// | ssrf-king, smuggle | IP allowlist / imdsv2 / egress firewall |[148.0] |
| SQLi | Database injection | `' OR 1=1--` and bounded payloads | sqlmap, sqlifinder | 0 successful queries beyond test | [4_security_stress[3]] [31][130.0] |
| XSS | Stored / reflected JS | Inert XSS payload scan | OWASP ZAP, Burp | 0 successful scripts in 100-input set | [4_security_stress[3]] [31][130.0] |
| IDOR | Predictable object IDs | Enumerate /api/v1/users/{id} | Burp Intruder | Authz check on every record | [4_security_stress[2]] [30] |
| Mass assignment | Over-posting | Send extra fields like `isAdmin` | Burp / custom | Server filters by allow-list | [4_security_stress[2]] [30] |
| Path traversal | `../` | `curl ../../etc/passwd` | dotdotpwn, kiterunner | Resolved path stays in allowlist | [4_security_stress[2]] [30] |
| Zip bomb | 42.zip | Submit 42 KB -> 4.5 PB | Custom nested zip | Hard size cap before extraction | [4_security_stress[2]] [30] |
| Decompression bomb | 1 KB -> GB | Send 1 KB zlib blob | Custom tester | Memory cap between read and allocate | [4_security_stress[2]] [30] |
| JSON nesting bomb | Deep hierarchy | 100k nested `{"a": {...}}` | Custom | Depth limit 32 / total size limit | [4_security_stress[2]] [30] |
| XML bomb (Billion Laughs) | Exponential entity expansion | XML with 10 entity refs | Custom | Entity expansion limit 10K | [4_security_stress[2]] [30] |
| Regex ReDoS | Catastrophic backtracking | Pattern `(a+)+$` on `aaaa...!` | ReScue, regexploit | Linear-time engine (RE2) or pattern rewrite | [4_security_stress[4]] [18][108.0] |
| Giant payloads | Big body attack | 1 GB JSON POST | hey, custom | Body size cap + per-route cap | [4_security_stress[2]] [30] |
| Malformed encodings | Bad charset abuse | Latin-1 + UTF-8 mix inputs | Burp + custom fuzz | Parser fails closed with 400 | |
| Unicode normalization | Visual spoofing | Submit NFKC/NFD mixed forms | Custom | Canonical form before storage/comparison | [4_security_stress[2]] [30] |
| Multi-byte truncation | Byte -> char split | Truncate mid-codepoint | fuzzer | Always handle partial chars safely | [4_security_stress[2]] [30] |
| Null bytes | C-string termination | `username%00.admin` | Burp / custom | Ignore post null byte | [4_security_stress[2]] [30] |
| HTTP request smuggling | CL.TE / TE.CL / CL.0 | Conflicting `Content-Length` + `Transfer-Encoding` | Burp HTTP Smuggler | Frontend/backend parser agreement | [4_security_stress[5]] [11][147.0] |
| JWT alg=none | Token forgery | Strip signature, set alg none | jwt_tool | Reject any alg other than expected | [4_security_stress[2]] [30] |
| Race-condition bugs | TOCTOU | Two requests on one resource | Burp Repeater parallel | Mutex/casual compare observed in 200 races | [4_security_stress[2]] [30] |

### Table 4.2 - Security Tool Matrix

| Tool | Domain | Strength | Source |
|---|---|---|---|
| OWASP ZAP | Web app baseline | Free, CI/CD-friendly | [4_security_stress[2]] [30] |
| Burp Suite Pro | Web manual + intruder | Industry standard | [4_security_stress[2]] [30][144.0] |
| sqlmap | SQLi | Mature exploitation engine | [4_security_stress[3]] [31] |
| slowloris / slowhttptest | DoS | Reproducible slow attacks | [4_security_stress[0]] [29][134.0] |
| hping3 / Scapy | Network floods | Craft raw packets | [4_security_stress[1]] [22] |
| ReScue / regexploit | ReDoS | Pattern analysis | [4_security_stress[4]] [18][108.0] |
| nuclei | CVE scanning | Template library | [4_security_stress[2]] [30] |
| ffuf | Web fuzzing | Fast directory fuzz | [4_security_stress[2]] [30] |
| snyk / trivy | SCA | Dependency CVE scan | [4_security_stress[2]] [30] |
| OWASP ASVS | Standards | Verification checklist | [4_security_stress[2]] [30][131.0] |

### Async HTTP Smuggling in Detail

CL.0 request smuggling uses a `Content-Length` header on a frontend HTTP/1 response that proxies to HTTP/2 backend. Because HTTP/2 abandons CL in favor of framing, the backend uses framing boundaries and ignores CL, but the attacker uses CL to smuggle a second request into another user's response [4_security_stress[5]] [11]. The attack chain: attacker sends `Content-Length: 0` to keep their session idle; later, the smuggled "ghost" request runs inside an unrelated victim's session [4_security_stress[6]] [17].

Insight: ReDoS + Slowloris + Smuggling is a "triad of demo-killers" because each can be triggered with 200 bytes or one request to a misconfigured endpoint. ASVS V11 and V13 (cryptography and business logic) are the minimum requirements hackathon teams should meet.

---

## 5_data_integrity_under_load

Goal: Verify that the system stays correct under contention, partitions, retries, and time. Jepsen-style property testing is the gold standard.

### Table 5.1 - Data Integrity Failure Modes

| Failure | What it tests | Method | Tool | Typical threshold | Source |
|---|---|---|---|---|---|
| Concurrent writes | Same record, parallel updates | 2n race; verify order invariant | Lin-Check, Porcupie | All histories satisfy invariant | [5_data_integrity_under_load[0]] [19][151.0] |
| Double-submit | Two identical POSTs | Send same POST 10x with Idempotency-Key | Stripe-style idempotency test | Exactly 1 effect, others 200-OK cached | [5_data_integrity_under_load[1]] [14][127.0] |
| Idempotency | Safe retry | Replay request N=10 times | Stripe idempotency test | All replays yield same final state | [5_data_integrity_under_load[1]] [14][127.0] |
| Replay attacks | Old signed payload reuse | Time-window nonce enforcement | OAuth + JTI | Reject beyond ttl, no double-execute | [5_data_integrity_under_load[1]] [14] |
| Ordering | Correct event arrival | K-way shuffle test | Jepsen + chaos | Total order matches broker order | [5_data_integrity_under_load[2]] [7] |
| Duplicate detection | Same fingerprint second time | Bloom filter or unique index | DB constraint | 0 duplicates past commit | [5_data_integrity_under_load[3]] [32] |
| Dedupe races | Window-of-collision | Race two writes w/ same key | Redis SETNX + DB unique | Only one of two wins, no torn commits | [5_data_integrity_under_load[3]] [32] |
| Transaction isolation | RR vs RC vs SER | Inject skew, check history | Jepsen | No G0, G1, G1c violations (Adya) | [5_data_integrity_under_load[2]] [7][149.0] |
| Lost updates | Two updates overwrite each other | Increment counter twice + verify | Porcupine | Final value = sum | [5_data_integrity_under_load[2]] [7] |
| Split brain | Two nodes both think primary | Partition, write to both | Chaos Mesh + Jepsen fencing | Fencing token denies stale writer | [5_data_integrity_under_load[0]] [19][150.0] |
| Reconciliation | Two stores drift | Periodic diff job assert | Custom compare | 0 diff rows above threshold at T+5m | [5_data_integrity_under_load[4]] [33] |
| Checksum verification | Detect corruption | Generate, mutate, checksum | CRC64, SHA-256 | Mismatch triggers reject + alert | [5_data_integrity_under_load[2]] [7] |
| Backup / restore under load | Online backups keep writes | Backup during write storm | pg_basebackup + load | p99 backup lag < 5 min | [5_data_integrity_under_load[0]] [19] |

### Jepsen Concrete Findings

- **etcd**: lost committed writes under network partition (v2.x era).
- **MongoDB**: acknowledged writes lost on primary failover prior to 4.0.
- **Kafka**: consumer offset rollback under broker leader change in older versions.
- **Redis**: stale read violations under asynchronous replication.
- **Consul**: stale reads by up to block-time / 2.
- **Postgres**: serializable isolation made available but with SSI overhead.
- **Elasticsearch**: lost writes under shard routing change.
- **ZooKeeper**: sync limit overrun on large znode writes [5_data_integrity_under_load[2]] [7][149.0].

Insight: For hackathon scale, a 3-node Lin-Check / Porcupine mini-Jepsen run for 5 min at 10x contention catches the same class of bug Jepsen finds in flagship DBs - dramatically cheaper to run than full Jepsen [5_data_integrity_under_load[0]] [19][151.0]. Pair with deterministic simulation testing when the system is small enough to fit on one hypervisor run [5_data_integrity_under_load[5]] [2].

---

## 6_domain_specific_stress

Goal: Capture vertical-specific failure modes that generic load/chaos suites miss.

### Table 6.1 - Domain Risk Register

| Domain | Subcategory | What it tests | Method | Tool | Typical threshold / number | Source |
|---|---|---|---|---|---|---|
| Fintech | Decimal precision | Float rounding bugs | Send 0.1 + 0.2, expect 0.3 exactly | Python `decimal.Decimal`, BigDecimal | Sum equal across 1M txn | [6_domain_specific_stress[0]] [14] |
| Fintech | Rounding mode | Banker's vs half-up | Stress test on rounding boundary values | Custom min(0.005) diff assert | Aggregate match < 0.01% drift | [6_domain_specific_stress[0]] [14] |
| Fintech | Double spend | Same $ charged twice | Concurrent POSTs w/o idempotency key | Stripe idempotency tests | 0 successful double charges | [6_domain_specific_stress[0]] [14] |
| Fintech | Reversal (refund) | Original + reversal reconciliation | Send refund, compare ledger | Ledger diff job | Sum(charges) - Sum(refunds) >= 0 | [6_domain_specific_stress[1]] [33][112.0] |
| Fintech | Reconciliation | Stripe vs internal ledger | T+1 reconcile | Optimus / Stripe Sigma | 100% reconciled by T+5 minutes | [6_domain_specific_stress[1]] [33] |
| Fintech | Audit trail integrity | Tamper-evident log | Append-only log with hash chain | Hyperledger Fabric, QLDB | 0 fraudulent appends | [6_domain_specific_stress[2]] [34] |
| Fintech | PCI-DSS scope | Card data flows | Level 1-4 compliance | Sprinto / Vanta | PCI DSS 4.0.1 mandatory by 2025 | [6_domain_specific_stress[3]] [35][103.0] |
| Health | Data accuracy | Diagnosis from wrong data | Field-level type+range checks | FHIR validator | 0 records outside schema | [6_domain_specific_stress[4]] [30] |
| Health | Consent revocation | Right-to-be-forgotten | Issue DELETE /patient, check onward calls | DB-level audit | DELETE removes from all downstream | [6_domain_specific_stress[4]] [30] |
| Health | HIPAA audit | PHI access logs | Audit-trail emission on every PHI read | Custom audit logger | 100% reads logged within 200 ms | [6_domain_specific_stress[5]] [36] |
| Education | Cheating resistance | Shared answer reuse | Cryptographic nonce per test attempt | JWT JTI per session | < 0.1% duplicate submissions | [6_domain_specific_stress[0]] [14] |
| Education | Grading fairness | Grade shift when path differs | Sorted randomized grading path | Adversarial harness | 0 reviews Inconsistent by > 5% | [6_domain_specific_stress[6]] [25] |
| Education | FERPA | Student data exposure | Cross-tenant IDOR | Burp Authz scanner | 0 cross-tenant answers | [6_domain_specific_stress[4]] [30] |
| Creative | Brand violation at scale | Logos in user uploads | CV mod transformers | Hive moderation | < 0.5% false negatives at 1000 qps | [6_domain_specific_stress[4]] [30] |
| Creative | Provenance forgery | C2PA / watermark spoof | Reverse-image check | C2PA verifier | 0 false provenance | [6_domain_specific_stress[7]] [28] |
| Creative | Deepfake detection | Synthetic media detection | Synthetic detector + human review | Hive or similar | < 1% false negative | [6_domain_specific_stress[7]] [28] |
| Messaging | Message ordering | Consistent order across replicas | K-way shuffle test | Kafka + Jepsen | Total order preserved | [6_domain_specific_stress[8]] [15][121.0] |
| Messaging | Delivery guarantees | At-least / exactly / at-most | Crash broker mid-publish | Kafka EOS tests | No duplicate/missing beyond chosen semantic | [6_domain_specific_stress[8]] [15][123.0] |
| Messaging | Group scaling | 10k member group | Scale recipient fan-out | Custom + Toxiproxy | p99 fan-out latency < 1 s | [6_domain_specific_stress[8]] [15] |
| Civic | Accessibility (WCAG 2.2) | Keyboard / screen reader / cognitive | axe-core | pa11y + manual audit | 0 critical issues per AA | [6_domain_specific_stress[9]] [37][102.0] |
| Civic | Language variants | i18n coverage | Locale-enumerate all strings | ICU / i18next | 100% string externalized, RTL safe | [6_domain_specific_stress[9]] [37] |
| Civic | Low-bandwidth | 2G network experience | Throttle + Lighthouse | Lighthouse CI | LCP < 2.5 s on "Slow 4G" | [6_domain_specific_stress[10]] [24] |

### Domain Hard Requirements

- **PCI DSS 4.0.1** (mandatory by Mar 2025): card data scoping, two-factor for admin access, network segmentation testing quarterly [6_domain_specific_stress[5]] [36][99.0].
- **HIPAA Security Rule**: audit logging of PHI, BAA-covered processors, minimum-necessary access [6_domain_specific_stress[5]] [36].
- **WCAG 2.2 AA**: 9 new success criteria covering focus appearance, dragging movements, target size, consistent help, redacted entry, and more [6_domain_specific_stress[9]] [37][102.0].
- **Kafka exactly-once semantics**: idempotent producers (PID + sequence), transactional API for atomic read-process-write across partitions [6_domain_specific_stress[8]] [15][123.0].
- **FERPA**: directory information opt-out records, audit-trail on PII disclosure [6_domain_specific_stress[4]] [30].

Insight: Domain QA tends to have one "hardness gate" (PCI, HIPAA, WCAG) on which full acceptance hinges. Hackathon scoring should weight a clear "Yes, we have X in scope" over a long list of cross-cutting risks.

---

## 7_acceptance_hardness_classes_for_hackathon_demos

Goal: Define "won't break on stage" classes and the corresponding adversarial challenges judges throw at demos.

### Table 7.1 - Demo Hardness Matrix

| Class | Adversarial input | Expected response | Failure when | Source |
|---|---|---|---|---|
| Adversarial judge Q | "What happens if 100x users?" | Numerical throughput projection | No numbers, hand-waves | [7_acceptance_hardness_classes_for_hackathon_demos[0]] [20][86.0] |
| Live-demo failure injection | Judge asks "what if you pull the network?" | Demo survives or fails open with clear UX | Demo freezes / blank screen | [7_acceptance_hardness_classes_for_hackathon_demos[0]] [20] |
| Network kill middemo | `iptables drop` on route | App shows offline banner, persists state | App crashes, data lost | [7_acceptance_hardness_classes_for_hackathon_demos[1]] [8][134.0] |
| Key revocation | Pull API key mid-call | Fail closed with clear message | App silently retries forever | [7_acceptance_hardness_classes_for_hackathon_demos[2]] [6] |
| Resource cap (CPU/mem) | `stress-ng` middemo | App degrades, doesn't OOM | OOM crash, lost progress | [7_acceptance_hardness_classes_for_hackathon_demos[1]] [8] |
| 100x volume burst | Spreadsheet / script pastes 100x | App processes correctly or backpressures clearly | App blocks UI, loses data | [7_acceptance_hardness_classes_for_hackathon_demos[3]] [19][145.0] |
| Deadline realism | Judge asks "would this ship in 2 weeks?" | Clear MVP / not-MVP separation | Promises everything | [7_acceptance_hardness_classes_for_hackathon_demos[0]] [20][86.0] |
| Time budget | 3-minute demo + 5-minute Q&A | Talks to time, defers depth | Talks past 3 min, loses Q&A | [7_acceptance_hardness_classes_for_hackathon_demos[4]] [21] |
| Score-card evaluation | Rubric categories | Scope / Docs / Polish / Security covered | Generic claims, no numbers | [7_acceptance_hardness_classes_for_hackathon_demos[0]] [20][86.0] |
| Ethical / bias Q | "What about gender/race bias?" | Acknowledged + mitigated + monitored | Silent on ethics | [7_acceptance_hardness_classes_for_hackathon_demos[4]] [21] |

### Example Rubrics

- **Opportunity Hack 4-category rubric** (Scope, Documentation, Polish, Security) with weighted subscores [7_acceptance_hardness_classes_for_hackathon_demos[0]] [20].
- **CGU Ethical AI Hackathon 1-5 scale** across clarity, depth, impact, presentation [7_acceptance_hardness_classes_for_hackathon_demos[4]] [21].
- **PFS-driven change-based testing**: tests that deteriorate significantly or are not fixed on time are marked flaky, becoming ineligible for change-based testing - a good signal for demo readiness [7_acceptance_hardness_classes_for_hackathon_demos[5]] [3][24.0].
- **Probabilistic Flakiness Score**: "the right question to ask is not whether a particular test is flaky, but how flaky it is" [7_acceptance_hardness_classes_for_hackathon_demos[5]] [3]; teams should target PFS below threshold before declaring demo-ready [7_acceptance_hardness_classes_for_hackathon_demos[5]] [3][72.0].

Insight: Hackathons tend to reward scope discipline more than feature breadth - judges want to see one feature polished vs five partial [7_acceptance_hardness_classes_for_hackathon_demos[0]] [20]. Adversarial Q&A is the dominant risk for unprepared teams; pre-staging answers to "what if the network drops" / "what if you get 100x users" wins more points than additional features.

---

## synthesis

The seven stress categories are deeply interlocked: a single physical failure (network partition) affects performance (regressions), chaos (kill a node), data integrity (split brain), security (SSRF), and the LLM agents that may route around it (offline fallback). Building a single experiment hub that runs them in concert inside a deterministic hypervisor [synthesis[0]] [2][54.0] is the natural endgame - DST in particular allows exhaustive state-space search across all seven axes without statistical uncertainty [synthesis[0]] [2][42.0][44.0].

Three tensions emerge:

1. **Statistical vs. deterministic testing**: PFS score gives a continuous reliability measure [synthesis[1]] [3][65.0], but DST guarantees full reproducibility [synthesis[0]] [2][54.0]. They are complementary, not competitors - statistical tests give monitoring signals, DST gives ground truth on rare bugs.
2. **Tooling fragmentation vs. standardisation**: OWASP gives security [synthesis[2]] [30], Jepsen gives distributed systems [synthesis[3]] [7], k6 gives web [synthesis[4]] [9], Chaos Mesh gives Kubernetes [synthesis[5]] [8]. There is no unifying tool, so a serious team must integrate by pipeline, not pick one.
3. **Hackathon pace vs. compliance depth**: PCI / HIPAA audits run over months [synthesis[6]] [36][99.0]; demos run over a weekend. The trade-off is not to skip compliance but to declare a *scope* clearly, e.g. "No card data ever crosses our service boundary" - and harden that scope with the right category from this registry.

The most reliable single defense-layer for any hackathon project is **deterministic simulation testing atop a hermetic build** [synthesis[7]] [38][43.0][50.0]: code is hermetic, the simulation is reproducible, and the same experiment replays on a judge's machine - a self-documenting demo [synthesis[0]] [2][54.0].