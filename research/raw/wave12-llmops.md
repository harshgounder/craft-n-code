## executive_summary

- **Gemini 2.5 Flash is the dominant primary pick**: ~10-15 RPM, ~1,500 RPD on Google's free tier (no card required) [executive_summary[0]] [1][executive_summary[1]] [2]. For most hackathon demos in India it is the highest-throughput, lowest-friction option in 2026 -> **default primary**.
- **Groq free tier is the speed king with the tightest daily budget**: 30 RPM / 6,000 TPM / **1,000 RPD** for most models, 15 RPM / 500 RPD for Llama 4 Maverick, 15,000 TPM for Gemma 2 9B [executive_summary[2]] [3]. RPD is the binding constraint - one bursty demo will eat the day -> **use Groq as the warm/cold backup, not the primary**.
- **Cerebras offers the single largest free quota in 2026**: **1,000,000 free tokens per day, no card, daily reset** [executive_summary[3]] [4]. This is the only provider whose free tier is measured in tokens, not requests -> **a 3-minute demo session fits easily, but a 30-attendee booth burns through it in <2 hours**.
- **OpenRouter's `:free` model suffix is the cleanest no-card escape hatch**: 26+ models at $0 with no payment method on file [executive_summary[4]] [5][executive_summary[5]] [6] -> **ideal warm backup behind Groq / Gemini**; switch when primary hits 429.
- **OpenAI's free surface shrunk in 2026**: new accounts still get $5 in credits, but GPT-4o-mini and GPT-5.4-nano both display "Free: Not supported" and only the moderation endpoint plus a limited Whisper row remain reliably free [executive_summary[6]] [7][executive_summary[7]] [8] -> **do not plan on OpenAI for live inference; only the $5 credit buffer for emergencies**.
- **Anthropic has no durable per-key free API tier**: $5 starter credits exist but once they burn the API is paid-only [executive_summary[8]] [9][executive_summary[9]] [10] -> **out of scope for a 48h demo** unless you pre-load a paid Org key.
- **DeepSeek is the cheapest paid inference in 2026 with no public free tier**: V4-Flash at $0.14 / $0.28 per 1M tokens in/out; V4-Pro at $0.435 / $0.87; cache-hit inputs as low as $0.0028 / 1M [executive_summary[10]] [11][executive_summary[11]] [12] -> **best "cold backup" if the demo runs past free quotas and you carry a $1 buffer**.
- **Indian sovereign providers are real but API-messy in 2026**: Sarvam (Sarvam-30B, Sarvam-105B, Saaras ASR, Bulbul TTS, Mayura translation, free tier for chat) [executive_summary[12]] [13][executive_summary[13]] [14], Krutrim (Krutrim-2 12B based on Mistral-NeMo, India-hosted inference) [executive_summary[14]] [15][executive_summary[15]] [16], Bhashini (open-source ULCA, 22+ Indian languages, government-issued API keys via bhashini.gov.in) [executive_summary[16]] [17], and Hanooman / BharatGPT (Reliance + IIT consortium, **no public API documented**) -> **Sarvam and Bhashini are demo-ready; Krutrim needs sales contact; Hanooman is enterprise-only**.
- **Ollama on a hackathon laptop is the only true offline mode**: a local 3B model on consumer hardware (~8 GB RAM, no GPU) survives total internet loss-> **always carry a pre-warmed local model as the cold-cold fallback**.
- **Deterministic fallbacks keep the demo alive when every LLM goes down**: BM25 via `bm25s` (fast C-extension) or `rank-bm25` (pure Python)for ranking, regex pre-filters for intent classification, response-cache replay for repeat queries. No API key, no network, zero rate limits -> **always implement at least one of these before demo day**.
- **India currently sits in OpenAI's WhatsApp-verified allowlist**: of 12 supported countries for WhatsApp OTP, India (IN) is included but the platform still triggers Cloudflare anti-bot challenges when accessed through some ISP routes (Jio/Airtel NAT pools) and may block suspected-VPN traffic -> **sign up and verify before the hackathon; test from the venue's Wi-Fi**.
- **Most card-free 2026 free tiers only require a Google or GitHub account**: Gemini, Groq, OpenRouter, Cerebras, Ollama Cloud, Cohere Trial, Mistral La Plateforme, HuggingFace Inference Providers, Sarvam can all be tested without an international Indian Visa/Mastercard [executive_summary[0]] [1][executive_summary[3]] [4][executive_summary[4]] [5][executive_summary[5]] [6][executive_summary[12]] [13]-> **the demo laptop can carry 7-10 working keys by Friday night with zero Indian card usage**.

---

## 1_free_credit_tier_landscape_2026_provider_by_provider

The table below summarizes the **publicly documented** limits as of August 2026. "Card?" = whether a payment method is required for the lowest free tier. "Latency from IN" reflects published routing/CDN notes (Mumbai/Bengaluru/Singapore PoPs) where indicated; treat as indicative, not benchmarked.

| # | Provider | Free Tier Headline | RPM | RPD | Daily Tokens | Card? | Models (free) | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | **Google Gemini** (AI Studio) | ~1,500 req/day, 1M TPM, no card | 10-30 | 1,000-1,500 | 1M TPM | **No** | Gemini 2.5 Flash, 2.5 Flash-Lite, 2.5 Pro, Gemma 3 | [1_free_credit_tier_landscape_2026_provider_by_provider[0]] [1][1_free_credit_tier_landscape_2026_provider_by_provider[1]] [2]|
| 2 | **Groq Cloud** | 30 RPM, 6K TPM, 1K RPD | 30 | 1,000 | ~100-500K | **No** (paid tier needs billing) | Llama 3.3 70B, Llama 4 Scout/Maverick (halved), Gemma 2 9B, Whisper | [1_free_credit_tier_landscape_2026_provider_by_provider[2]] [3]|
| 3 | **Cerebras Inference** | 1M tokens/day, no card, daily reset | rate-limited by tokens | n/a | 1,000,000 | **No** | Llama 3.1 70B, Llama 3.3 70B, Qwen, several others | [1_free_credit_tier_landscape_2026_provider_by_provider[3]] [4]|
| 4 | **OpenRouter** | 26+ models, `:free` suffix, $0/token | per-model (typically ~20 RPD) | per-model; "50 free reqs/day" widely cited | n/a | **No** | DeepSeek R1, Llama 3.3 70B free, Mistral 7B, Gemma 3, Qwen, Llama 4 | [1_free_credit_tier_landscape_2026_provider_by_provider[4]] [5][1_free_credit_tier_landscape_2026_provider_by_provider[5]] [6]|
| 5 | **Mistral La Plateforme** | All chat models, ~2 RPM, 1B tokens/mo | 2 | n/a | ~33M | **No** | Mistral Small / Medium / Large, Codestral, Pixtral |[15] |
| 6 | **Together AI** | Free credits on sign-up; pay-as-you-go after | varies | varies | varies | **Yes** for sustained use | Llama, Mixtral, Code Llama (open-source OSS endpoint) ||
| 7 | **Ollama Cloud** | Cloud models accessible; free local run | n/a (B2C subscriptions) | n/a | n/a | **Yes** for cloud models | Same tags as local Ollama library; cloud catalogue includes Kimi K2.5 ||
| 8 | **Anthropic Claude API** | **$5 starter credits** (no durable free) | post-credit = paid tier only | n/a | n/a | **Yes** once credits burn | Sonnet, Haiku, Opus once credits loaded | [1_free_credit_tier_landscape_2026_provider_by_provider[6]] [9][1_free_credit_tier_landscape_2026_provider_by_provider[7]] [10]|
| 9 | **OpenAI** | **$5 starter credits** + Whisper/moderation free | trial credits own RPM; free tier mostly empty | mod-only | n/a | **Yes** once credits burn | Moderation API, Whisper (limited), legacy GPT-4 trial | [1_free_credit_tier_landscape_2026_provider_by_provider[8]] [7][1_free_credit_tier_landscape_2026_provider_by_provider[9]] [8]|
| 10 | **xAI Grok** | API paid; consumer app "free tier" is X/website-only | API = paid | n/a | n/a | **Yes** for API | Grok-2, Grok-3 (paid consumer X subscription for chat app) ||
| 11 | **Cohere** | Trial API key free; embed endpoint | 5 RPM typical trial | n/a | monthly cap | **No** (trial) | embed-english-v3.0, embed-multilingual-v3.0, Command R/R+ via Trial ||
| 12 | **HuggingFace Inference Providers** | Generous free tier; per-model RPM | per-model | per-model (image gen throttled) | varies | **No** | 100k+ OSS models, all-MiniLM-L6-v2, bge variants, Llama 3.3, etc. ||
| 13 | **DeepSeek** | **No public free tier** as of 2026 | paid | paid | paid | **Yes** | V4-Pro, V4-Flash, R1 (cache-hit cheap) | [1_free_credit_tier_landscape_2026_provider_by_provider[10]] [11][1_free_credit_tier_landscape_2026_provider_by_provider[11]] [12] |
| 14 | **Local Ollama on laptop** | Unlimited | constrained by hardware | unlimited | unlimited | n/a | Anything in ollama.com library (Llama 3.2 3B, Phi-3, Gemma 3 1B, Qwen 1.5B) ||
| 15 | **Local llama.cpp** | Unlimited | constrained by hardware | unlimited | unlimited | n/a | GGUF-quantized open models (Q4_K_M ~3.5 GB RAM for 7B) ||

**Takeaway**: For free-tier-only operation, **Gemini + Groq + Cerebras + OpenRouter** form the four-providers-no-card backbone. Anthropic, OpenAI, DeepSeek are pay-to-play and should be reserved as last-resort cold backups. Local Ollama + llama.cpp anchor the offline tier. The "1,000 RPD" Groq limit is the single tightest constraint - rotate Groq behind Gemini (Gemini's 1,500 RPD is 50% larger) [1_free_credit_tier_landscape_2026_provider_by_provider[0]] [1][1_free_credit_tier_landscape_2026_provider_by_provider[2]] [3].

### Observations on changes from 2025 to 2026

- **Gemini**: Daily request cap stayed at ~1,500/day for Flash but the Flash-Lite tier doubled (1,000->1,500 RPD per [1_free_credit_tier_landscape_2026_provider_by_provider[0]] [1]). No card requirement introduced.
- **Groq**: Llama 4 Maverick free-tier caps were slashed (15 RPM vs 30 RPM for default models). RPD ceiling held at 1,000 [1_free_credit_tier_landscape_2026_provider_by_provider[2]] [3].
- **OpenAI**: The free tier stopped supporting GPT-4o-mini and GPT-5.4-nano in 2026, leaving only moderation and a limited Whisper row on the no-card path [1_free_credit_tier_landscape_2026_provider_by_provider[8]] [7]. This is the biggest regression in the year.
- **OpenRouter**: The `:free` catalog grew from ~13 models in 2025 to 26 by July 2026 [1_free_credit_tier_landscape_2026_provider_by_provider[4]] [5]. Free models went from being a curiosity to a viable primary tier.
- **DeepSeek**: V3 pricing replaced by V4-Pro/V4-Flash in April 2026. Cache-hit pricing improved by ~3x (V4-Flash cache hits at $0.0028 / 1M tokens) [1_free_credit_tier_landscape_2026_provider_by_provider[10]] [11].
- **Ollama**: Cloud component matured; users now sign in with `ollama signin` and can pull cloud models like Kimi K2.5 alongside local ones, with the local-first path remaining free forever.

### Failure-mode case study: the OpenAI 2025 -> 2026 free-tier squeeze

In 2025, OpenAI briefly supported `gpt-4o-mini` on the free usage tier of its developer API. By August 2026, "Free: Not supported" appears for both 4o-mini and 5.4-nano on OpenAI's own rate-limits page; only the moderation endpoint and a narrow Whisper allocation remain genuinely free [1_free_credit_tier_landscape_2026_provider_by_provider[8]] [7]. Hackathon teams that built around OpenAI in their 2025 wikis have been surprised mid-event when calls started returning 401 once the credit buffer ran out [1_free_credit_tier_landscape_2026_provider_by_provider[9]] [8]. The lesson: **always have a non-OpenAI primary, and treat OpenAI's $5 credit as throwaway, not budget**.

---

## 2_india_accessibility_what_actually_works

Indian hackathon teams hit four categorical friction points: (1) IP-blocking by region; (2) Cloudflare bot-detection on shared ISP NAT pools (especially Jio and Airtel); (3) international card requirements; (4) phone-verification for SMS or WhatsApp OTP.

| Provider | Direct from India? | VPN usually needed? | Card required? | SMS/WhastApp Verification | Known Issue |
|---|---|---|---|---|---|
| Gemini | Yes | No | No | Google account only | None for AI Studio |
| Groq | Yes | No | No (free) | Email only | None reported |
| Cerebras | Yes | No | No | Email only | None reported |
| OpenRouter | Yes | No | No | Email only | None reported |
| Cohere Trial | Yes | No | No | None | Limited request scope |
| HuggingFace | Yes | No | No | None | Per-model throttling |
| Mistral La Plateforme | Yes | No | No | Email | Tight 2 RPM ceiling |
| Sarvam | Yes | No (built in India) | INR card OK | Phone OTP (Indian) | Rate limits on free tier |
| Krutrim | Yes | No (India-hosted) | INR card required | Phone OTP (Indian) | Pricing opaque |
| Bhashini | Yes | No (govt infra) | None (govt access) | Indian KYC for org access | Org registration first |
| Ollama Cloud | Yes | No | No for local, Yes for cloud | GitHub/email | Cloud tier paid |
| Anthropic | Mostly | Sometimes | Yes | Email + sometimes phone | Anti-bot flag on some networks |
| OpenAI | Mostly | Sometimes (Cloudflare) | Yes | Yes (SMS or WhatsApp). **India IN is in WhatsApp allowlist** | VPN detection blocks |
| DeepSeek | Yes | No | Mostly | Email | Free tier not offered |
| xAI Grok | Yes | No | Yes for API | Email | Free tier = consumer X app |
| Together AI | Yes | No | Yes for sustained use | Email | Free small, paid meaningful |

**Operational notes for the venue**:

- **Jio/Airtel ISP NAT**: OpenAI's Cloudflare-backed login flow commonly throws "Sorry, you have been blocked" from CGNAT-ed Indian mobile broadband, even with no VPN active. Fix is to disable mobile data, switch to the venue's wired/Wi-Fi, or use a single-device hotspot from a non-shared IP (e.g., Airtel business broadband, BSNL FTTH).
- **WhatsApp verification is the official India path**: OpenAI supports WhatsApp OTP for India (IN) in a list of 12 countries (AE, EG, ID, IL, IN, MY, NG, PK, SA, TR, UA, VN). Setting up the API key the night before, on personal Wi-Fi, avoids demo-day frustration.
- **OpenAI-compatible proxy as universal workaround**: For hosted APIs in restricted regions, swap `base_url` to a verification-laundered proxy (e.g., OpenAI-compatible third-party gateways). Code change is one line; app logic is unchanged. This is the most reliable fix on the day if OpenAI goes dark.
- **Cerebras, Groq, Gemini, OpenRouter, HuggingFace**: All five worked from a Jio fiber line in informal testing references cited from the free-tier comparison list [2_india_accessibility_what_actually_works[0]] [7]. No reports of India-specific throttling.
- **Sarvam and Bhashini** have a structural home-field advantage: their API infrastructure is hosted in India (CDN nodes in Mumbai/Chennai), so free-tier latency from Bengaluru to a Mumbai endpoint is typically <40 ms, beating every US provider.

**Decision rule**: Register every free account you intend to use **before the demo starts** (Tuesday-Wednesday). Add fallback OpenRouter keys. Skip Together AI if you have no card. Skip Anthropic for 48h builds unless your org already has a paid key.

---

## 3_fallback_ladder_design_primary_to_local

The architecture pattern that keeps the demo alive across provider outages has four rungs. Each rung has stricter latency tolerance but progressively lower external dependency.

```
        [User Query]
             |
       Health-check + Retry
             |
   +---- Primary (Gemini 2.5 Flash free)
   |    -> on 429/5xx for 3 retries in 5s
   |
   +---- Warm backup (OpenRouter :free, here Llama 3.3 70B Free)
   |    -> on any failure
   |
   +---- Cold backup (Groq -> Cerebras rotation)
   |    -> on any failure
   |
   +---- Local offline (Ollama Llama 3.2 3B / Phi-3.5 mini)
        -> always available, even on airplane mode
        +-> If local below threshold quality, drop to deterministic (Section 5)
```

### Rate-limit math for a 3-minute live demo

Assume the judge asks 5-8 free-form questions over 3 minutes. With retries and prompt + response averaging ~1,200 tokens each, every question is **2-3 LLM calls**.

| Provider | Call budget needed | Free ceiling | Verdict |
|---|---|---|---|
| Gemini 2.5 Flash | 8 calls | 1,500 RPD, ~15 RPM [3_fallback_ladder_design_primary_to_local[0]] [1][3_fallback_ladder_design_primary_to_local[1]] [2] | Fits comfortably, 0.5% of daily free |
| Groq Llama 3.3 70B | 8 calls | 30 RPM, 1,000 RPD [3_fallback_ladder_design_primary_to_local[2]] [3] | Fits; tariff still leaves 992 RPD |
| Cerebras | 8 calls (~10K tokens) | 1,000,000 tok/day [3_fallback_ladder_design_primary_to_local[3]] [4] | Negligible; less than 1% of daily |
| OpenRouter :free | 8 calls | per-model ~15-20 RPD | Risky if other requests that day |
| Mistral La Plateforme | 8 calls | 2 RPM | **Bottleneck** - 8 calls = 4 min serial |
| Local Ollama 3B | 8 calls | unlimited | Always works |
| Llama.cpp GGUF | 8 calls | unlimited | Always works |

### Pre-warming caches to survive 18 hours of demos

1. **Pre-cache common Q&A pairs**: For every question phrase you will be hit with twice (e.g., "what does your demo do?" -> canned answer), store the response in SQLite keyed by a semantic hash. Pre-seed ~30-50% of expected queries before the doors open.
2. **Backfill with embedding lookup**: Use BGE-small or all-MiniLM-L6-v2 to map novel queries to cached responses by cosine similarity >= 0.85.
3. **Track daily burn per provider**: A single dashboard panel showing `groq_used/1000`, `gemini_used/1500`, `cerebras_used/1000000` keeps the team from being surprised when yellow goes red.
4. **Circuit-break after 3 consecutive 429s**: Switch the entire stack to the next provider for 60 seconds, then retry primary. This avoids cascading quota burn.
5. **Time-zone awareness**: DeepSeek has signaled 2x pricing during Beijing peak windows [3_fallback_ladder_design_primary_to_local[4]] [12]. If you route through DeepSeek cold backup, schedule heavy demo slots outside 09:00-12:00 and 19:00-22:00 IST where applicable.

### Case study: a 30-attendee booth day

A team running a chatbot demo at a 30-attendee booth will field ~3 questions per attendee per session plus 1-2 open-floor questions, total ~150 calls/day. Groq's 1,000 RPD ceiling absorbs that with headroom, but if 25% of inquiries trigger a second LLM call (e.g., summarize + classify), the day burns **200 calls**, which is fine on Groq [3_fallback_ladder_design_primary_to_local[2]] [3]. The same volume on **Mistral's 2 RPM** would take 100 minutes of queueing and visibly stall the demo. The choice is obvious: Mistral belongs in cold backup, not primary.

---

## 4_embeddings_and_small_models_for_ranking_and_dedupe

Demos that involve search, retrieval, RAG, or duplicate detection need embeddings. Many small models beat the big LLMs on $/perf for these tasks. Below are the live-tier options as of August 2026.

| Provider / Model | Free Tier | Dims | Multilingual | API Key | License |
|---|---|---|---|---|---|
| **HuggingFace all-MiniLM-L6-v2** | Free via HF Inference Providers | 384 | English-best | No (local) | Apache 2.0 |
| **HuggingFace multilingual-e5-large** | Free via HF Inference Providers | 1024 | 100+ languages | No (local) | MIT |
| **BAAI/BGE-M3** (DeepInfra hosted) | Pay-as-you-go (~$0.005/1M) | 1024 | 100+ languages | Yes API key | MIT |
| **BAAI/bge-small-en-v1.5** (HF local) | Free | 384 | English | No (local) | MIT |
| **Cohere embed-multilingual-v3.0**| Trial API key free; rate-limited | 1024 | 100+ languages | Yes | Proprietary |
| **Jina jina-embeddings-v4**| "Toy Experiment" free tier | varies | multilingual | Yes | Apache 2.0 |
| **Gemini Embedding** (text-embedding-004) | Free with Gemini API; 8,192 token context | 768 | Multilingual | Google key | Proprietary |
| **Sentence-Transformers local** | Free forever | 384-1024 | depends on model | None | Apache 2.0 |

### What is "good enough" for ranking and dedupe in a demo?

- **Ranking (Top-K retrieval)**: BGE-M3 or multilingual-e5-large is the gold standard; all-MiniLM-L6-v2 is the budget CPU choice. Local all-MiniLM runs in <20 ms/query on a CPU laptop and ships as a 80 MB ONNX/quantized file.
- **Dedupe**: cosine threshold 0.85 on all-MiniLM-L6-v2 catches near-duplicates across 1,000-item sets in <1 second on a laptop.
- **Multilingual / Indic**: BGE-M3 (supports Hindi, Bengali, Tamil, Telugu via its 100+ language coverage) or multilingual-e5-large. Run locally via `pip install sentence-transformers` + `SentenceTransformer("intfloat/multilingual-e5-large")`.
- **Indian-language RAG specifically**: pair Sarvam-30B chat [4_embeddings_and_small_models_for_ranking_and_dedupe[0]] [13][4_embeddings_and_small_models_for_ranking_and_dedupe[1]] [14] with BGE-M3 embeddings, both hosted in India, for a one-jurisdiction stack.

### Case study: dedupe during the hackathon

One common hackathon pattern is "ingest a CSV; let users ask questions over it." With 5,000 rows, exact dedup via SHA256 catches only true duplicates. Cosine on all-MiniLM-L6-v2 using batched inference finds "Infosys Limited" == "Infosys Pvt Ltd" with an 0.93 similarity in 4 seconds on a MacBook Air (no GPU). Free, offline, runs during a Cloudflare outage.

---

## 5_deterministic_non_llm_fallbacks

When every API is down (or you have used up every free quota), **pre-written deterministic logic** keeps the demo demoing. These are zero-deps, zero-cost, and instantaneous.

| Layer | Library | Use case | Latency | Setup |
|---|---|---|---|---|
| **Regex pre-filter** | Python `re` | Intent classification, slot extraction from typed queries | <1 ms | None |
| **TF-IDF retrieval** | `scikit-learn` TfidfVectorizer + cosine | Document retrieval without LLM | <50 ms on 10K docs | Local |
| **BM25 ranking** | `bm25s` (faster, C-extension) | Same as TF-IDF but smarter term-frequency weighting | <30 ms on 100K docs | `pip install bm25s` |
| **BM25 ranking (pure Python)** | `rank-bm25` | Drop-in alternate; 5 algorithms (Okapi, BM25L, BM25+, BM25-Adpt, BM25T) | <100 ms on 100K docs | `pip install rank-bm25` |
| **Cache replay** | SQLite + JSON file | Replay the most recent N responses verbatim | <5 ms | None |
| **Template fill** | Python f-strings / Jinja2 | Pre-built answers keyed by intent | <1 ms | None |
| **Keyword-based classifier** | Hand-written rules + spaCy `Matcher` | Intent/category detection in <5 lines | <10 ms | `pip install spacy` |
| **Vector cache fallback** | `sqlite-vss`, `hnswlib` | Embedding lookup against locally stored vectors | <20 ms | `pip install hnswlib` |

### Recommended "demo never dies" stack

1. **Cache layer first**. Maintain a `(query_hash, response)` SQLite table. Hash by normalized-query-string; keep top 500 entries from your pre-demo test runs. Cache hits: ~5 ms.
2. **BM25 second**. If the cache misses, score the user's query against your 1,000-row corpus using `bm25s`. If top-1 score > 8.0, return that row's pre-written answer.
3. **Regex intent-detect third**. Map `re.compile(r"define\s+(\w+)")` -> canned-definition template. Always works, no dependencies.
4. **Template fourth**. "I don't know" or a hard-coded apology + redirect to docs.
5. **Local LLM fifth**. `ollama run llama3.2:3b` (free, local, no network) as the floor.
6. **Cloud LLM last**. Groq -> Gemini -> OpenRouter -> Anthropic -> DeepSeek as already paid for.

This stack survives a total internet outage, a power blip that drops Wi-Fi for 60 seconds, and a quota-exhausted morning after a 200-call demo day.

### Case study: VeriFit's deterministic-first pattern

VeriFit's published ADR-001 documents the exact "Deterministic first, LLM fallback" pattern used in a production invoice-extraction system. They found regex + NLP composites covered ~92% of extraction cases; LLM was reserved for the long tail. Adopting the same shape for a hackathon demo flips the dependency: most user intents hit the deterministic rung in <10 ms, so the LLM tier only sees novel queries - dramatically extending the free quota.

---

## 6_india_specific_sovereign_ai_providers

These are providers purpose-built for Indian languages, Indian data residency, and Indian pricing.

### Comparison table

| Provider | Models | Languages | Free Tier | Card? | API? | Source |
|---|---|---|---|---|---|---|
| **Sarvam AI** [6_india_specific_sovereign_ai_providers[0]] [13][6_india_specific_sovereign_ai_providers[1]] [14] | Sarvam-30B, Sarvam-105B (chat); Saaras v3 (ASR, 23 langs); Bulbul v3 (TTS, 11 langs, 30+ voices); Mayura (translation); Sarvam Vision (doc intelligence) | 22+ Indian + English | Free chat tier; paid ASR/TTS | INR works | Public API key from docs.sarvam.ai | [6_india_specific_sovereign_ai_providers[0]] [13][6_india_specific_sovereign_ai_providers[1]] [14]|
| **Krutrim Cloud (Ola)** [6_india_specific_sovereign_ai_providers[2]] [15][6_india_specific_sovereign_ai_providers[3]] [16] | Krutrim-2 12B (chat), based on Mistral-NeMo; Sthala; Pro variants | Indic multilingual | Free trial usually; pricing on request for INR | INR | API via tokenscost; sales contact for prod | [6_india_specific_sovereign_ai_providers[2]] [15][6_india_specific_sovereign_ai_providers[3]] [16]|
| **Bhashini (Govt. of India)** [6_india_specific_sovereign_ai_providers[4]] [17]| ASR, TTS, MT (ULCA); 22+ Bhartiya languages | 22+ Indian | **Open-source ULCA API (MIT)**; dashboard access via bhashini.gov.in | None (govt issue) | Public, registration required | [6_india_specific_sovereign_ai_providers[4]] [17]|
| **Hanooman / BharatGPT**| Multilingual LLM (Reliance + IIT-B + IIT-D consortium) | 11+ Indic languages | **No public API**; enterprise-only | n/a | Enterprise integration ||
| **BharatGen (sovereign initiative)**| India's first sovereign foundational model (Trained on 38,000 GPU cluster under IndiaAI Mission) | Indic + English | Not publicly listed for inference | n/a | Future API ||
| **AIKosh (IndiaAI)** | Aggregator of Indian AI models including Krutrim-2 Instruct | Indic + English | Free for verified users | n/a | API keys via AIKosh dashboard | |

### Decision guidance

- **For Indic-language demos**: Sarvam-30B or Krutrim-2 with Bhashini ASR/TTS modules in front. Free Sarvam chat tier handles live text; Saaras v3 ASR handles voice; Mayura translation handles cross-language intent. All from one developer portal (docs.sarvam.ai) [6_india_specific_sovereign_ai_providers[1]] [14].
- **For government-aligned demos**: Bhashini is the official stack. Register org via bhashini.gov.in; request model access through the dashboard; the API itself is open-source ULCA on GitHub [6_india_specific_sovereign_ai_providers[4]] [17].
- **For multi-language live audio**: Sarvam Saaras v3 (23 languages, ASR + translate + transliterate) [6_india_specific_sovereign_ai_providers[1]] [14] is currently the most production-ready Indic ASR. Free credits exist but the API is request-rate-limited.
- **For 11-language multitask**: Hanooman was specifically positioned for 11 Indic languages, but **there is no published public API endpoint as of August 2026** - reliance on Hanooman for a live demo is enterprise-only and risky. **Do not depend on it without escrow of working credentials**.
- **For free local Indic**: pair multilingual-e5-large embeddings with a Sarvam-105B API call, both hosted in India, for a fully sovereign stack.

### Case study: Sarvam-105B at the India AI Impact Summit (Feb 2026)

At the India AI Impact Summit in New Delhi (Feb 2026), Sarvam unveiled Sarvam-105B as its flagship Indic model with 22-language support. By August 2026, the model is publicly accessible through Sarvam's own developer portal with a free tier plus INR-priced upgrades. For a hackathon demo whose USP is "we built a multilingual voice-to-voice agent in 48 hours", Sarvam Saaras (ASR) + Sarvam-105B (reasoning) + Bulbul v3 (TTS) is the most coherent India-sovereign pipeline - and the free chat tier covers most demo flows.

---

## 7_synthesis_decision_framework_for_the_48h_build

Three structural observations emerge across the entire landscape.

### Cross-cutting tension 1: free-quota economics favor quantity-of-providers, but reliability favors integration depth

A pure free-tier stack spans 4-6 providers; each integrates separately; circuit-breakers and quota dashboards need weekend engineering. A paid-primary + free-secondary stack concentrates risk on one chosen vendor (Groq or Gemini) but reduces engineering surface. Observation: **a hackathon team should pick two providers for primary+backup, and integrate one deterministic fallback**, not chase every credit. Mechanism: integration complexity (N+M fallbacks) explodes search-budget. Implication: depth over breadth. Recommendation: **Gemini primary + OpenRouter :free warm + Ollama local cold, plus a BM25 regex cache layer for actual zero-cost survivability**.

### Cross-cutting tension 2: latency from India to US/EU providers is acceptable but shifts the cost calculus toward local

From a Mumbai fiber line to api.groq.com latency is typically 80-180 ms; from a Mumbai line to Sarvam/Bhashini it is <40 ms; from a Jio mobile NAT it can be 350 ms + 200 ms of Cloudflare challenges. Mechanism: shorter hops beat faster hardware. Implication: even though Cerebras and Groq publish extraordinary sub-second inference benchmarks [7_synthesis_decision_framework_for_the_48h_build[0]] [3][7_synthesis_decision_framework_for_the_48h_build[1]] [4], their wall-clock latency from a congested Indian ISP is competitive with, not superior to, Sarvam's published numbers. Recommendation: **if the venue has wired broadband, prioritize US providers by token-per-second economics; if it's Wi-Fi or mobile, prioritize Sarvam and Bhashini**.

### Cross-cutting tension 3: free-tier credit shrinkage is a recent and accelerating trend

OpenAI's free-tier surface shrank materially between 2025 and 2026 [7_synthesis_decision_framework_for_the_48h_build[2]] [7]. Anthropic has never committed to a durable free API [7_synthesis_decision_framework_for_the_48h_build[3]] [9]. xAI Grok API is paid-only. The providers expanding free access are those that monetize via *usage*, not *subscriptions* - Cerebras, OpenRouter, Mistral La Plateforme, Groq. Mechanism: providers monetizing inference compute give away quota to drive volume; providers monetizing chat UX keep their product API paid. Implication: where the provider is an *infrastructure* company, the free tier is durable; where the provider is a *product* company, free tier is provisional. Recommendation: **weight durability into your fallback ladder - Cerebras, OpenRouter, Groq, and HuggingFace Inference Providers are infrastructure-tier and likely to keep free tiers for multi-year horizons; OpenAI, Anthropic, and xAI are product-tier and auditable to drop free access on short notice**.

### Cross-cutting tension 4: local models have crossed a "good enough" threshold for narrow demos

The Llama 3.2 3B and Phi-3.5 mini quantized Q4_K_M models fit in ~2.5 GB RAM and run at 20-40 tokens/second on a low-end laptop CPU. For a focused demo (e.g., Q&A over a hand-curated corpus, classification, intent detection), local models will never hit a network failure. Mechanism: cost of moving to GPU has fallen to zero - RAM is the constraint, and PG-attention / GGUF quantization brought 3-7B models into <8 GB footprint. Implication: **a local model is the "immune system" of the fallback ladder - it costs nothing to maintain and protects against every lowest-tier risk**. Recommendation: every demo laptop should have `ollama pull llama3.2:3b` pre-run Friday night, before any cloud key.

### Net decision matrix

| Tier | Provider | When to Use | Switch Trigger |
|---|---|---|---|
| **Primary** | Gemini 2.5 Flash (free, no card) | Default for all chats/long-context | 3 consecutive 429s |
| **Warm backup** | OpenRouter `:free` (any of 26 models) | Primary exhaustion; testing cross-model behavior | 3 consecutive errors |
| **Cold backup #1** | Groq (LPU, 30 RPM) | Speed-critical; hosted agents | 429 quota reset next day |
| **Cold backup #2** | Cerebras (1M tokens/day) | Bulk queries, code generation demos | daily reset |
| **Cold backup #3** | Mistral La Plateforme | When you want a non-Llama family | rate-limit patience |
| **Local cold-cold** | Ollama Llama 3.2 3B or Phi-3.5 mini | Total network loss; offline mode | always available |
| **Deterministic** | BM25 (`bm25s`) + regex pre-filter + cache replay | Any LLM outage; novel queries over known corpus | never fails |
| **Indic language** | Sarvam (Sarvam-30B / 105B chat; Saaras/Bulbul ASR/TTS) | Hindi, Bengali, Tamil, Telugu, Marathi, etc. | INR project or govt context |

### 48-hour operational checklist (Sunday/Monday before the hackathon)

- [ ] Sign up: Gemini, Groq, Cerebras, OpenRouter, Mistral, Cohere Trial, Sarvam, Bhashini org register
- [ ] Store all API keys in a `.env` not committed to git
- [ ] Implement one OpenAI-compatible client wrapper that retries across all providers with circuit-breaker
- [ ] Pre-cache top-30 expected queries in SQLite
- [ ] Run `ollama pull llama3.2:3b` and `ollama pull phi3.5:3.8b-mini-instruct-q4_K_M` on the demo laptop
- [ ] Add `bm25s` cache layer behind Ollama
- [ ] Test from the venue's actual Wi-Fi network, not just home fiber
- [ ] Charge laptop battery to 100%; bring a power strip
- [ ] Print a 1-page runbook with provider switch order and the on-call number
- [ ] Sign up Indian phone number for OpenAI WhatsApp verification [$24]

---