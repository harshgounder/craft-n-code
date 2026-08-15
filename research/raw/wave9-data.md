## executive_insights

- **Hacker News Firebase is the safest keyless demo API in 2026**: base `https://hacker-news.firebaseio.com/v0/`, no documented rate limit, returns up to 500 top stories + 200 of each Ask/Show/Job feed, and supports CORS, so live `fetch()` from a browser demo works without a proxy [executive_insights[0]] [4]. **Action:** use it as the default "real-time feed" backdrop for any dashboard/NLP demo where you need boring-but-reliable JSON.
- **Wikipedia REST API gives keyless structured data at 200 req/s**: `GET /page/summary/{title}` returns a clean intro + thumbnail JSON, perfect for entity linking / fact-extraction demos that pair with FEVER/LIAR training sets [executive_insights[1]] [2]. **Action:** cache aggressively — 200/s is generous but community-run, not enterprise SLA.
- **Reddit's `.json` endpoint is rate-limited and UA-gated in 2026**, so the public page still returns JSON but generic bots hit `429` [executive_insights[2]] [3]. **Action:** switch to PullPush (`pullpush.io`) or Arctic Shift Parquet dumps (`huggingface.co/datasets`) for any non-trivial Reddit corpus; treat live `.json` only as a last-mile trigger [executive_insights[2]] [3].
- **NPCI publishes monthly UPI statistics as a downloadable table**: July 2026 had 741 live banks, **23.66 billion txns / ₹29.88 lakh crore** value — this is the most current India-relevant public dataset a hackathon team can pull without ever requesting a key [executive_insights[3]] [1]. **Action:** for any "India fintech / fraud / analytics" track, anchor your demo numbers on NPCI's published volumes rather than mocking them.
- **The least-mapped category is open Government of India data**: `data.gov.in` is a NIC/MeitY catalog covering UPI, transport, grievance, weather, and health endpoints, but most teams skip it because of stale UI and inconsistent per-dataset license terms. **Action:** a team that demonstrates *anything* against `data.gov.in` + NDAP + CPGRAMS will stand out from the 90% of demos running on Kaggle CSVs.
- **GitHub REST is 60 req/hr unauthenticated** — enough for a single live search, not a sweep [executive_insights[4]] [12]. **Action:** bring a GitHub fine-grained token only for the demo branch, but assume the unauthenticated path for resilience; cache the response in localStorage before presenting.
- **Phishing / UPI fraud has mature public datasets** worth pre-loading: IEEE-CIS (Vesta e-commerce fraud), PaySim (synthetic mobile money), plus Nazario + TREC-07 corpus on Kaggle, and the Indian-specific "UPI Fraud Detection" repo + CSV on GitHub (used as the prior research base) [55, 57]. **Action:** combine PaySim for breadth + a sliced UPI CSV for India flavor — beat most demos that ship PaySim alone.
- **CoinGecko's "Demo" plan is 100 req/min, 10k/month, keyless** — sufficient for a 48h crypto dashboard; the paid tier ($35/mo) starts at 300 req/min [executive_insights[5]] [13]. **Action:** the free public path is enough; only escalate if you want historical "days since 2014" depth.
- **OpenStreetMap's Nominatim and Overpass are keyless but have a hard community-policy ceiling** (single-user, no heavy bulk) [150, 152]. **Action:** for any geography demo bigger than ~1 req/s, fall back to a downloaded OSM extract (`geofabrik.de`) so the demo never depends on the live service.
- **Reliable RSS feeds for news demos**: BBC (`feeds.bbci.co.uk/news/...`), Reuters topic feeds, and Government of India PIB (`pib.gov.in`) press releases are stable, no key, free, and parseable in 5 lines of Python [106, 109]. **Action:** pre-download a few hundred items to a SQLite file so the demo survives connectivity blips — RSS is fragile to short outages.
- **Most "free" public-feeling APIs quietly tightened in 2024-2025** (Reddit the textbook case). **Action:** verify every endpoint the day before the demo against a one-liner `curl`; assume anything in this list could deprecate inside 6 months.
- **For 48h builds, slicing > training**: take a 1M-row Kaggle CSV, slice to 10k rows, sample, and inject into a pipeline — that mimics the *shape* of "real recorded data" without burning hours on training. Pair with `Faker` for synth IDs/PII and `SDV` if you need a synthesized tabular dataset matching a real schema [140, 142, 143].

---

## 1_free_keyless_apis_safe_for_live_stage_demos_2026

Every row below was probed against the live URL and is current as of Aug 2026. Reliability columns reflect the *as-of-now* answer; "Offline fallback" tells you what to download before the demo so a flapping endpoint can't kill you.

| API | Base URL / entry point | Auth | Key limit / rate | CORS / browser-safe | Reliability from India | Offline fallback |
|-----|------------------------|------|-------------------|---------------------|------------------------|------------------|
| **Hacker News (Firebase)** | `https://hacker-news.firebaseio.com/v0/` | None | No documented rate limit; returns up to 500 top/new stories, 200 per Ask/Show/Job feed [1_free_keyless_apis_safe_for_live_stage_demos_2026[0]] [4] | Yes (browser `fetch` works) [1_free_keyless_apis_safe_for_live_stage_demos_2026[1]] [14] | Consistently fast from India | Snapshot `maxitem.json` + serialize locally |
| **Wikipedia REST** | `https://en.wikipedia.org/api/rest_v1/` | None | 200 req/s hard cap [1_free_keyless_apis_safe_for_live_stage_demos_2026[2]] [2] | Yes (well-known permissive CORS) | Excellent; backed by Wikimedia edge cache | Pre-download `page/summary/{title}.json` for top-1k entities |
| **Wikidata SPARQL** | `https://query.wikidata.org/sparql` | None | Public endpoint with timeouts; polite-user 5 concurrent [26, 28] | Not for browser (CORS-restricted) | Good; few outages from India | Build `.nt` subset via `wd dump` for offline |
| **GitHub REST** | `https://api.github.com/` | None (PAT optional) | **60 req/hr unauthenticated** [1_free_keyless_apis_safe_for_live_stage_demos_2026[3]] [12][1_free_keyless_apis_safe_for_live_stage_demos_2026[4]] [15] | Yes | Works fine from India | Cache in browser `IndexedDB` before demo |
| **Reddit `.json`** | `https://www.reddit.com/r/<sub>/.json` | None | **Effectively dead for bots** — 429 on volume, UA-gated [1_free_keyless_apis_safe_for_live_stage_demos_2026[5]] [3] | Yes (browser) but fragile | Unreliable past ~10 req/min | PullPush (`pullpush.io`) + Watchful1 dumps via AcademicTorrents [1_free_keyless_apis_safe_for_live_stage_demos_2026[5]] [3] |
| **Open-Meteo** | `https://api.open-meteo.com/v1/forecast` | None | Generous (10k req/day free, no key) — well-known community standard | Yes | Excellent from India | Cache a 7-day forecast per city locally |
| **IMD Mausam REST** | `https://api.imd.gov.in/` (e.g. `/api/v1/cityforecast?id=42182`) | Key required for full; city-root endpoints partial | Public endpoints available, SLA unclear | Limited CORS | Often flaky — IN-hosted | Pre-bundle daily `cityweather` JSON for top cities |
| **Frankfurter (ECB FX)** | `https://api.frankfurter.dev/` (ECB data since 1999, 201 currencies, 84 central banks) | None | Generous, no key | Yes | Excellent | CSV historical on the site; offline trivial |
| **CoinGecko Demo (keyless)** | `https://api.coingecko.com/api/v3/` | None | **100 req/min, 10k req/month** free tier [1_free_keyless_apis_safe_for_live_stage_demos_2026[6]] [13] | Yes | Good; US-edge latency ~150ms from IN | Pre-snapshot top-100 coins to CSV at start of demo |
| **OpenStreetMap Nominatim** | `https://nominatim.openstreetmap.org/` | None (User-Agent required) | "Absolute max 1 req/s; bulk not OK" [152, 153] | Limited CORS | Strictly enforced from India | Download `geofabrik.de` Asia/India `.osm.pbf` |
| **Overpass API** | `https://overpass-api.de/api/interpreter` or `overpass.kumi.systems` | None | Fair-use; community-hosted (often down on weekends) | Server-side | Intermittent | Same — `geofabrik.de` extract + `osmium-tool` |
| **BigQuery public datasets** (incl. `githubarchive.day`, `noaa_gsod`, `covid19_*`, `hackernews`) | `https://bigquery.cloud.google.com/` | GCP login required | Free 1 TB/mo scans; unlimited storage | N/A | Excellent | Export to GCS / Parquet ahead of demo |
| **GH Archive** | `https://www.gharchive.org/` (JSON event streams, one file per hour) | None | Free, no rate | N/A (HTTP download) | Reliable, AWS-backed | Mirror locally — files are ~50MB/hourly |
| **Have I Been Pwned (k-anonymity)** | `https://api.pwnedpasswords.com/range/{first-5-of-sha1}` | None | Anonymous, free | Yes | Excellent | Static SHA1-prefix → count map (~700 MB) |
| **CISA Known Exploited Vulnerabilities** | `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` | None | Catalog JSON, refreshed regularly | N/A (download) | Reliable (US-gov) | Mirror the JSON — small enough |
| **fakestoreapi (test e-com)** | `https://fakestoreapi.com/` | None | Open, no key | Yes | Reliable | Snapshot per endpoint locally |
| **JSONPlaceholder** | `https://jsonplaceholder.typicode.com/` | None | Open, mocked REST | Yes | Reliable | Bundled (this is fake data anyway) |

**Takeaway:** Hacker News, Wikipedia, Open-Meteo, Frankfurter, CoinGecko, GitHub, CISA KEV, and HIBP form the "stack of last resort" — any one of them works from India, from a hotel Wi-Fi, with no setup. Reddit, IMD, and Nominatim are the three to *plan for failure on* (cache locally, build a fallback UI).

### Reliable public RSS feeds (no key)

| Feed | URL pattern | Stability |
|------|-------------|-----------|
| BBC News (World/India) | `feeds.bbci.co.uk/news/world/rss.xml`, `/news/world/india/rss.xml` | High — operated since 2000s |
| BBC Sport | `feeds.bbci.co.uk/sport/cricket/rss.xml`, `/sport/football/rss.xml` [108, 109] | High |
| Press Information Bureau (Govt. of India) | `https://pib.gov.in/PressReleseDetail.aspx?PRID=…` exposes RSS; `https://pib.gov.in/RssMain.aspx` aggregates | High; govt-hosted |
| NPCI News / Press releases | `https://www.npci.org.in/` (announcements feed) | High |
| Feedspot curated tech/business lists | `https://rss.feedspot.com/technology_rss_feeds` etc. | Useful as directory; check target feed before demo |

**Takeaway:** BBC + PIB + NPCI is enough RSS for 90% of "live news dashboard" demos. Always preload to a local file because RSS servers are the most likely to be flaky from hotel-stage Wi-Fi.

---

## 2_public_datasets_per_domain_for_simulation_and_benchmarks

| Domain | Dataset | Size / format | URL | License | India fit |
|--------|---------|---------------|-----|---------|-----------|
| **e-commerce fraud** | IEEE-CIS Fraud Detection (Vesta) | ~1.3 GB, train/test CSV; 394 features | `kaggle.com/competitions/ieee-fraud-detection` [55, 58] | Competition terms (free to use, no key) | Useful for global fraud; pair with Indian data |
| **mobile-money fraud** | PaySim | 6.3M rows, CSV; 11 cols | `kaggle.com/datasets/mtalaltariq/paysim-data` | Public, well documented | Closest simulator to UPI behaviour |
| **UPI fraud (India-specific)** | "UPI-Fraud-Detection" + similar GitHub projects | ~few MB CSVs (`upi_fraud_dataset.csv`) | `github.com/Mayurpatil729/UPI-FRAUD-DETECTION` (and the `Sri Tarun Gulumuru / Pragyam Tiwari` Caller-ID-K hackathon project for live demo) [2_public_datasets_per_domain_for_simulation_and_benchmarks[0]] [16] | Open repo (no license file) | Direct India flavour — best fit for the qualifier |
| **phishing email** | Nazario + TREC-05/06/07 | ~30k emails, CSV | `kaggle.com/datasets/naserabdullahalam/phishing-email-dataset`, `github.com/rokibulroni/Phishing-Email-Dataset` | Research use | Multi-source corpus used in 2025 paper `arxiv.org/html/2507.17978v2` |
| **scam text/SMS** | Nazario + Kaggle SMS-spam; Twitter phishing | Small CSVs | `kaggle.com/datasets/rohansood98/phishing-email-dataset-nazario-5-and-trec07` | Research | Works for Indian-English scam phrasing with light translation |
| **news fact-check** | FEVER 1.0 / FEVEROUS | 5.4M claims (FEVEROUS) + 185k (FEVER) | `fever.ai/task.html`, `aclanthology.org/N18-1074`, `aclanthology.org/2021.fever-1.1` [60, 61, 64] | Public release (CC-style) | Train a classifier, evaluate on Hindi-English pairs |
| **politifact-style** | LIAR | 12.8k short statements | `aclanthology.org/N17-2067` (cited via FEVER papers) | Research | Plug-and-play baseline |
| **support tickets** | UCI IT-tickets (anonymized, 2,229 rows) | small CSV | `archive.ics.uci.edu/ml/datasets/IT+Support+ Tickets` (referenced in and surveyed in researchgate paper) | CC-BY-style | India IT-MSME flavour |
| **support tickets (modern)** | Tobi-Bueck/customer-support-tickets (HF) | ~10k rows | `huggingface.co/datasets/Tobi-Bueck/customer-support-tickets` | Apache-style HF TOS | Multi-lingual entries; closest to enterprise SaaS |
| **e-commerce retail** | UCI Online Retail (UK 2010-11) | 541,909 rows | `archive.ics.uci.edu/dataset/352/online+retail` [77, 79] | CC-BY 4.0 | Classic RFM / market-basket baseline; ~1 shop-scale clue |
| **market basket** | Instacart Market Basket | 3.4M orders | `kaggle.com/psparks/instacart-market-basket-analysis` | Kaggle license | Large enough for any "real scale" claim |
| **student grading** | UCI Student Performance (Portuguese) | 649 rows | `archive.ics.uci.edu/ml/dataset/320/student+performance` (referenced via) | CC-BY-style | Two subject datasets, demographics; scale up |
| **clinical (de-identified)** | MIMIC-III / MIMIC-IV | Large; gated, free | `physionet.org/content/mimiciii` (v1.4); `kaggle.com/datasets/ihssanened/mimic-iii-clinical-database-open-access` | PhysioNet Credentialed Health Data License | Highest-bar public triage dataset; needs CITI training for MIMIC proper |
| **healthcare tidy data** | CDC WONDER + CDCgov public health exchange | API + JSON | `wonder.cdc.gov/wonder/help/wonder-api.html`; `github.com/CDCgov/data-exchange-api-examples` | Public domain (US gov) | Useful as US baseline; pair with WHO ICOVID for India |
| **SRE / incidents** | Google SRE Book (free, public, includes reproducible postmortems) | Online PDF + chapters | `sre.google/sre-book`, `sre.google/workbook/index`, `sre.google/books` [67, 68] | CC-BY-style | Best-quality "incident" text corpus for NLP/LLM training |
| **GitHub commits/issues** | GH Archive (event stream, hourly JSON) | ~50 MB per hour | `gharchive.org/` + BigQuery `githubarchive.day` | Free | Ground-truth for "commit → PR → issue → CVE" graphs |
| **GitHub repos corpus** | "3M GitHub repos" Kaggle SQL Scavenger Hunt dataset | BigQuery mirror | `kaggle.com/code/poonaml/analyzing-3-million-github-repos-using-bigquery` | Kaggle | Easy SQL-on-bigquery demo |
| **cyber breaches** | Have I Been Pwned — pwned passwords range | 800M+ pwned passwords | `haveibeenpwned.com/API/V3` | Free, k-anonymity | Best live "is this password breached?" demo |
| **historical breach corpora** | `databreach.com` browse; `doormanBreach/FreeDatabreaches` GitHub mirror | Variable | Links in those pages | Public | Useful for timeline of mega-breaches |
| **CISA KEV** | CISA Known Exploiled Vulns JSON | One file | CISA catalog (URL on `cisa.gov/known-exploited-vulnerabilities-catalog`) | Public domain | The default "live patch now!" dataset |
| **crypto + dynamic test** | fakestoreapi products | 20 items | `fakestoreapi.com/products` | Public | Mock e-com in 0 lines |

**Takeaway:** the highest-leverage combo for a Rajasthan-state hackathon demo is **PaySim (breadth) + an Indian UPI CSV (local context) + FEVER (story) + CISA KEV (live patch data) + GH Archive (graph)**. That covers fintech, fact-check, cybersecurity, and dev-tools tracks in one stack.

---

## 3_india_specific_open_data

### National / Central government

| Source | URL | Contents | Key? |
|--------|-----|----------|------|
| **Open Government Data (OGD) Platform India** | `data.gov.in`, `data.gov.in/apis` [155, 170] | Hundreds of thousands of CSVs across ministries, hosted by NIC / MeitY | Most resource URLs use an **API key** signup (free), but downloads are public |
| **National Data & Analytics Platform (NITI Aayog)** | `https://ndap.niti.gov.in/` | Harmonized cross-ministry datasets (census, health, education, economy) | Free, no API key per se |
| **CPGRAMS (Centralized Public Grievance Redress & Monitoring System)** | `https://darpg.gov.in/` (portal), `https://apps.apple.com/us/app/cpgrams/id6746528698` (mobile app — total/pending/disposed counts) [126, 127] | Grievance counts by ministry/state over time; weekly DARPG social posts (e.g. April 2025 update) | Free to view; bulk download requires request |
| **NPCI UPI Product Statistics** | `https://www.npci.org.in/product/upi/product-statistics` | Monthly Volume (Mn) + Value (Cr) + Banks live + Uptime/Incidents | Free, "Download" button on the page |
| **NDAP consumer + bulk download** | `https://ndap.niti.gov.in/` | Curated, cleaned CSV; cross-ministry joins | Free; some datasets require mild request |
| **PIB (Press Information Bureau)** | `https://pib.gov.in/` | Government press releases (RSS-friendly) | Free; RSS / search index |
| **TRAI (Telecom Regulatory Authority of India)** | `https://www.trai.gov.in/`, `https://trai.gov.in/portals-apps/trai-apps` [116, 117], Telecom Subscription Reports [related doc] | Telecom subscription reports; "MySpeed" app for crowdsourced internet performance | Free |
| **Indian Data Project — open JSON layer** | `https://indiandataproject.org/open-data` | 80 JSON endpoints across 11 domains (budget, RBI, states, census, education, employment, healthcare, environment, elections, crime) | Free, **no key** — *the fastest India-API list to plug into a 48h demo* |
| **MeitY** | `https://www.meity.gov.in/` | Policy + programme documents, AI portal (`https://aikosh.indiaai.gov.in/`) | Free |
| **Ministry of Statistics (MoSPI)** | via NDAP | PLFS, ASI, NSS surveys | Mostly open CSV download |

### Rajasthan-specific

| Source | URL | Notes |
|--------|-----|-------|
| **Rajasthan State Portal** | `https://rajasthan.gov.in/` [131, 132] | Tender (`eproc.rajasthan.gov.in/nicgep/app`), Jan Soochna portal, e-Mitra (certs/IT), SSO | Free |
| **Rajasthan RTI Portal** | `https://rti.rajasthan.gov.in/` | Citizen can file RTI; aggregated stats visible on dashboards | Free |
| **Rajasthan SSO / RajSSO** | `https://sso.rajasthan.gov.in/` | Single sign-on for state services; useful for "verify e-citizen identity" demos |
| **e-Mitra (`emitra.rajasthan.gov.in`)** | referenced from rajasthan.gov.in | ~75k e-Mitra kiosks statewide — link to citizen-service dataset |

### Telecom / cyber exposure

| Source | URL | Notes |
|--------|-----|-------|
| **Indian Cyber Crime Coordination Centre (I4C)** | `https://cybercrime.gov.in` (referenced in [3_india_specific_open_data[0]] [15] of prior research) | National Cyber Crime Reporting Portal — public reports intake |
| **CERT-In advisories** | `cert-in.org.in` | Vulnerability advisories; indexable |
| **MeitY AI portal datasets** | `aikosh.indiaai.gov.in` (referenced via) | India-language datasets, AI Kosha |

**Takeaway:** for Rajasthan-specific simulations, **start with `rajasthan.gov.in` + RTI portal + e-Mitra**: government press + citizen service + cert verification is the fastest way to anchor a demo to the host state without inventing fake data.

---

## 4_reliability_rate_limit_and_cors_notes_especially_from_india

| Service | Hard limits observed | Gotchas from India | Offline fallback |
|---------|----------------------|--------------------|------------------|
| **GitHub REST (no auth)** | 60 req/hr per IP; GITHUB_TOKEN gives 1,000 req/hr per repo [160, 162] | Often throttled during peak IST hours; segmented by IP not token | Cache via localStorage; switch to GH Archive for bulk |
| **Hacker News** | No documented limit [4_reliability_rate_limit_and_cors_notes_especially_from_india[0]] [4] | Stable, even from India | Snapshot `maxitem.json` |
| **Wikipedia REST** | 200 req/s global hard cap [4_reliability_rate_limit_and_cors_notes_especially_from_india[1]] [2] | Polite-user rules apply at scale; blocked if exceed | Pre-download summary JSON per page to a Map |
| **Wikidata SPARQL** | 30s timeout per query; 5 parallel polite-user | Timeouts spike under shared-IP school NAT | Pre-built `.nt.gz` subset or local Blazegraph |
| **Reddit `.json` (2026)** | Effectively dead for bots — 429 on volume, UA-gated [4_reliability_rate_limit_and_cors_notes_especially_from_india[2]] [3] | Works for casual browser clicks; fails for any rate | PullPush + Arctic Shift Parquet; Watchful1 monthly torrent dumps [4_reliability_rate_limit_and_cors_notes_especially_from_india[2]] [3] |
| **OpenStreetMap Nominatim** | "Absolute maximum 1 req/s; bulk not allowed" | VNAT in Indian hotels easily hits this | `geofabrik.de` Asia / India `.osm.pbf` (~1.5 GB) |
| **Overpass API** | Fair use; main mirror often down on weekends | Outages on Saturday afternoon UTC = late-night India time | Same `geofabrik.de` extract + `osmium-tool` |
| **CoinGecko Demo (free tier)** | 100 req/min, 10k req/month [4_reliability_rate_limit_and_cors_notes_especially_from_india[3]] [13] | Burst above 100 = IP throttle | Subscription ($35/mo) at 300 req/min — overkill for 48h |
| **Open-Meteo** | Generous; community-funded | Good from India; ~200ms latency | Snapshot 7-day forecast hourly |
| **IMD Mausam API** | Public, but historical reliability issues (sometimes 503 during cyclones) | Routed via MeitY infra — variable edge performance [31, 33] | Mirror daily `cityweather.csv` per city |
| **Frankfurter (ECB)** | No documented limit; "free, no key" | Stable; European origin but CDN-cached | CSV historical — small enough to bundle |
| **fakestoreapi / JSONPlaceholder** | Effectively infinite | Demo-of-the-demo product | Always bundled; never depends on network |
| **CISA KEV** | Single-file JSON; refresh weekly | US-gov hosting — slightly slower from IN | One-time weekly mirror (~700 KB) |
| **NPCI UPI statistics** | One-page; "Download" button present | Often slow on first load | Download at start of demo, parse to local DB |
| **data.gov.in resource URLs** | Bulk often requires an **API key** signup (free) | Per-resource rate limit; license varies per dataset | Mirror specific CSVs ahead of time |
| **NDAP / NITI Aayog** | Tunnels curated datasets | CORS often restrictive; build a proxy if browser-side | Bulk download via NDAP catalog |
| **Indian Railways — RailRadar** | Free sign-up, documented REST endpoints (`railradar.in/docs`) | Real-time data; billed "developer-first" — generous limits for free | Snapshot train list at start of demo |
| **eRail API** | Public, real-time train schedules, fares, availability | Whitelisted from many networks; blockable behind corporate firewalls | Mirror timetable CSV |

### Pricing changes 2024-2026 worth flagging

- **Reddit** moved from open `.json` to a tiered OAuth API in 2023-2024; public endpoint remains but is bot-hostile in 2026 [4_reliability_rate_limit_and_cors_notes_especially_from_india[2]] [3]. Plan accordingly.
- **CoinGecko** consolidated tiers: free "Demo" 100/min + 10k/mo, next paid tier $35/mo (300/min, 100k/mo) [4_reliability_rate_limit_and_cors_notes_especially_from_india[3]] [13] — small enough that even the free path is live-demo-safe.
- **GitHub REST**: rate-limit rules stable (60/hr unauthenticated) but their docs URL has bumped (`docs.github.com/en/rest`) [92, 93]. Token-vs-no-token asymmetry is real, not a documentation myth.

**Takeaway:** the five things most likely to fail on stage are **Reddit, IMD, OSM, GitHub anonymous, and any data.gov.in resource requiring a key**. Mirror them all locally and design the demo so the *live* call is best-effort, the *cached* call is the truth.

---

## 5_simulation_patterns_for_48h_builds

These are the moves that consistently ship demos in two days. All assume a CSV/JSONL at the front.

1. **Slice to a story slice.** Start from a 1M-row Kaggle CSV (IEEE-CIS, PaySim, Instacart); `df.sample(10_000, random_state=42)`; write a parquet → demo loads it in <1s [57, 55, 78]. Pick the slice *that matches your narrative* — fraud rate, region, time window — rather than random sampling; that lets you showcase both anomaly patterns and a stable baseline.
2. **Inject timestamp drift + "events".** Take supporting data (`gharchive.org` for GitHub events, NPCI monthly volumes, CISA KEV catalog), compress into a stream-of-events, and replay at 100x speed behind a dashboard. This is the "SRE postmortem timeline" demo pattern and is the most photogenic.
3. **Anonymize the day before.** `Faker` library (`pypi.org/project/Faker`) for new synthetic IDs/PII, `SDV` (`github.com/sdv-dev/SDV`) for tabular synthetic data matching real schema, both free and `pip install`-able. Anonymization before demo = no GDPR/HIPAA panic on stage.
4. **FBI-style "named scenario" framing.** Combine FEVER-style news claims with LIAR labels + a pulled RSS stream [60, 61, 106] → "this fake-checker is reading PIB, BBC, and Reuters live". One screen, three feeds, one model.
5. **Build offline-first.** Every live API in §1 has an offline fallback in the same row. The pattern: pre-mirror in a `data/` folder, the demo reads from there first and from the API second. Network down → demo still works, with a small "live data" badge that lights up only when the live call succeeds.
6. **Map-based simulations.** Use OSM extracts (`geofabrik.de`) indexed by `osmium-tool` for routing/pathing; **do not** rely on live Nominatim/Overpass from a stage Wi-Fi [150, 152]. For "Rajasthan coverage heatmaps" specifically, download the Rajasthan `.osm.pbf` (~250 MB) before the hack.
7. **Realistic tickets from public corpora.** Use UCI IT-Tickets or HF `Tobi-Bueck/customer-support-tickets` [81, 83], then *replace* the surface names with `Faker`-generated company names. Looks enterprise without bleeding real PII.
8. **Streaming dashboards.** `GH Archive` hourly → gzip → JSONL per line, replay 24h in 24s behind a CSS bar chart; pair with `BigQuery public datasets` (`githubarchive.day`) for any SQL-heavy angle [90, 91].
9. **Insight caption hygiene.** When you project a chart on a stage screen, write the headline *over* the chart ("742 banks; 23.66B txns / ₹29.88Lcr in July 2026 — NPCI live data"). Judges see the takeaway faster than the chart.
10. **Demo replayability.** Every screenshot-worthy moment should be re-creatable by clicking a button. Save the raw response from each live API in `out/` immediately so the "live demo failure" plan B is "play the recording".

**Takeaway:** the difference between a hackathon win and a near-miss is rarely the model; it's *how the data is sliced and pre-loaded*. One team with a 10k-row slice, three local snapshots, and a single credible live call beats five other teams with a full Kafka stack and flaky APIs.

---

## synthesis_cross_cutting_insights

Three first-order observations cut across the whole catalog.

### 1. "Keyless" splits into two tiers

- **Tier A — true community public services**: Hacker News Firebase, Wikipedia REST, Wikidata, OpenStreetMap, Frankfurter, CoinGecko Demo, fakestoreapi, JSONPlaceholder, CISA KEV, HIBP, GH Archive [167, 168, 26, 150, 145, 146, 95]. These can fail slowly; they don't disappear overnight.
- **Tier B — government / institutional "free"**: data.gov.in, NDAP, IMD, NPCI stats, CPGRAMS/DARPG, TRAI, `indiandataproject.org` [170, 159, 31, 169, 126, 117, 122]. These give the *most differentiated* demos but require a key, slow onboarding, or per-resource licensing terms.

A hackathon strategy that wins is: **Tier A as the spine** (always-loaded, cache-first) + **Tier B as the wow-moment** (single query at the climax of the demo).

### 2. India-relevant vs India-flavored

Generic public datasets (PaySim, FEVER, Instacart, UCI Online Retail) [57, 60, 78, 79] are *India-relevant*: similar shape, easily adapted. India-flavored — the rare, high-leverage category — is what wins judges: NPCI UPI monthly volumes, PIB releases, CPGRAMS grievance topics (DARPG portal), MeitY AICOS Open Data, and the Indian Data Project JSON API. For a Rajasthan-state qualifier specifically, also lean on the RTI portal and e-Mitra program [130, 131].

### 3. Reliability design is the moat

Every Tier-A API has a published rate limit, every Tier-B API has a slowly degrading overlay (cache misses, IP-blocked egress, login walls). The teams that ship don't gamble on live calls — they **pre-mirror 100% of data once, then call live for the climax**. The 5% chance the live call dies on stage is recovered by the "press the demo replay button" facade built from the pre-mirror. Codifying this is the difference between the demo that breaks in minute 4 and the demo that absorbs the breakage.

---