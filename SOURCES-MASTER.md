# Master source list — for your review

Everything the digest can draw on, with **honest status on each**. Tick, cut or add — this is the file to mark up.

**Legend**
- ✅ **LIVE** — tested, returns structured data, callable every run
- 🔍 **SEARCH** — reachable only through web search, not direct fetch. Still usable, just slower and less complete.
- ❌ **DEAD** — tested and blocked or broken. Don't retry.
- ❓ **UNTESTED** — plausible, not yet verified

---

# 1. NEWS FEEDS & APIs

## ✅ LIVE
| Source | Endpoint | Freshness (tested 1 Aug) |
|---|---|---|
| **BBC World RSS** ⭐ | `feeds.bbci.co.uk/news/world/rss.xml` | **Same day** — the only reliable one |
| BBC Business RSS | `/news/business/rss.xml` | 5 days stale ⚠️ |
| BBC Technology RSS | `/news/technology/rss.xml` | 2 weeks stale ⚠️⚠️ |
| BBC India RSS | `/news/world/asia/india/rss.xml` | 2 weeks stale ⚠️⚠️ |
| BBC Science RSS | `/news/science_and_environment/rss.xml` | untested |

> **Key finding: only BBC World is dependably current.** The others still carry real stories but must be date-checked item by item — several are weeks old.

## ❌ DEAD — all tested
Reddit JSON · Livemint RSS · The Hindu RSS · Ars Technica RSS · Economic Times (all paths) · **GDELT** (returns empty despite reputation) · **Google News RSS** (empty) · Wikipedia REST feed · Al Jazeera RSS (returns gzip binary) · **Substack RSS generally** (Noahpinion returned gzip binary) · **Personal blog Atom feeds** (Simon Willison returned gzip binary) · **YouTube RSS** (`youtube.com/feeds/videos.xml?channel_id=` returns empty)

> **Two disappointments worth naming.** **YouTube RSS doesn't work**, so your creator roster — Varun Mayya, Johnny Harris, Huberman, Dr. K, Karpathy, Cole Medin — can't be monitored automatically. And **most Substack/blog feeds return gzipped binary** that web_fetch can't decode, which kills Stratechery, Noahpinion, Chartbook, Import AI and similar as direct feeds. All of these drop to 🔍 SEARCH.

## ❓ Require API keys (none available)
NewsAPI.org · Guardian API · Mediastack · NewsData.io · Currents

---

# 2. FINANCE & MARKET DATA

## ✅ SEC EDGAR — official US company financials ⭐ NEW
**Found by searching GitHub's `public-apis` repo (453k★). No key, no rate limit, straight from the SEC.**

```
Company facts:   https://data.sec.gov/api/xbrl/companyfacts/CIK<10-digit>.json
Single concept:  https://data.sec.gov/api/xbrl/companyconcept/CIK<10-digit>/us-gaap/<Tag>.json
Recent filings:  https://data.sec.gov/submissions/CIK<10-digit>.json
```

**Verified working.** NVDA (`CIK0001045810`) returned the full audited revenue series — FY2026 **$215.938B**, Q1 FY2027 (to 26 Apr 2026) **$81.615B**, every figure tied to its 10-K/10-Q accession number and filing date.

**CIKs for your US holdings** — resolve the rest on first run via `https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=<ticker>&action=getcompany`:

| Ticker | CIK |
|---|---|
| NVDA | 0001045810 |
| AAPL | 0000320193 |
| MSFT | 0000789019 |
| GOOGL | 0001652044 |
| META | 0001326801 |
| AMZN | 0001018724 |

Useful tags: `Revenues` · `NetIncomeLoss` · `Assets` · `Liabilities` · `EarningsPerShareDiluted` · `ResearchAndDevelopmentExpense`

**What this unlocks:** actual audited fundamentals for your US book — revenue trends, margins, R&D spend, filing dates. Not prices, but arguably better: this is the ground truth beneath the price. Responses are large, so request a single concept rather than `companyfacts`.

## ✅ LIVE
| Source | Endpoint | Notes |
|---|---|---|
| **mfapi.in** | `api.mfapi.in/mf/<code>/latest` | Indian MF NAVs. Codes resolved: quant ELSS **120847**, PPFAS ELSS **147481**. 21 to go. |
| **Frankfurter** | `api.frankfurter.app/latest?from=USD&to=INR` | FX. **Fetch every run** — assuming 88 vs actual 95.39 cost ₹32,021 of accuracy. |
| **Indian Data Project** | `indiandataproject.org/data/<domain>/2025-26/<file>.json` | 80 endpoints: RBI, budget, GDP, inflation, employment, states, census, elections, crime, healthcare, environment. **Annual dataset — historical context only.** Its RBI file says repo 6.25% when the real rate is 5.25%. |
| AMFI NAVAll | `amfiindia.com/spages/NAVAll.txt` | Official, current, but 4MB and truncates at ~767 lines. Single-NAV fallback only. |

## ❌ DEAD
**Yahoo Finance** · Stooq · CoinGecko · NSE/BSE unofficial APIs

> **The big gap: there is no working live stock-quote source.** Not for your 19 Indian holdings, not for your 18 US ones. Equity prices must come from your workbook with visible dates. Mutual funds are fine — those go live via mfapi.

## ❓ Key-required
Alpha Vantage (25 calls/day free) · Finnhub (60/min free) · Breeze/ICICI Direct · TrueData

## ❓ Found via GitHub `public-apis` — no key required, not yet tested
Worth trying on the next run:

| Source | Endpoint | Use |
|---|---|---|
| **Econdb** | `econdb.com/api/` | Global macroeconomic data |
| **US Treasury Fiscal Data** | `fiscaldata.treasury.gov/api-documentation/` | US debt, yields, spending |
| **Currency-api** | `github.com/fawazahmed0/currency-api` | 150+ currencies, **no rate limits** — backup to Frankfurter |
| **Coinpaprika** | `api.coinpaprika.com` | Crypto — try after CoinCap and CoinGecko both failed |
| **Coinlore** | `coinlore.com/cryptocurrency-data-api` | Crypto alternative |
| **CoinDesk BPI** | `old.coindesk.com/coindesk-api/` | Bitcoin price index |
| **Mempool.space** | `mempool.space/api` | Bitcoin network/fees |
| **Messari** | `messari.io/api` | Crypto fundamentals |
| **Portfolio Optimizer** | `portfoliooptimizer.io` | Portfolio analysis maths |
| **Razorpay IFSC** | `razorpay.com/docs/` | Indian bank branch codes |
| **WallstreetBets sentiment** | `dashboard.nbshare.io/apps/reddit/api/` | **Reddit sentiment without Reddit's API** — possible workaround for the r/ blocklist |
| **UK Carbon Intensity** | `carbon-intensity.github.io/api-definitions/` | Grid carbon data |
| **PM2.5 Open Data** | `pm25.lass-net.org/#apis` | Air quality sensors |

**❌ Tested from this list and dead:** CoinCap (`api.coincap.io`) returns empty.

### How this list was found — repeatable method
GitHub API search → `public-apis/public-apis` (453,956★) → fetch raw README → parse the markdown tables filtering `Auth == No`. Other lists worth mining the same way: `public-api-lists/public-api-lists` (15k★), `cheahjs/free-llm-api-resources` (29k★).

---

# 3. TECH, DEV & RESEARCH

## ✅ LIVE
| Source | Endpoint | Use |
|---|---|---|
| **Hacker News Firebase** | `hacker-news.firebaseio.com/v0/topstories.json` → `/item/<id>.json` | Current front page, scores, comment counts. **High comment-to-score ratio = controversy.** |
| **GitHub Search API** | `api.github.com/search/repositories?q=created:>DATE+stars:>500` | Real star counts. Surfaced Andrew Ng's `openworker` (11.5k★), `openai/codex-security` (7.9k★), `grok-build` (23.8k★), `Kimi-K3` (7.8k★) — all missed by search. |
| HN Algolia | `hn.algolia.com/api/v1/search_by_date` | Great search/filters, but **index ran ~2 weeks behind**. Historical research only. |

## ❌ DEAD
arXiv API · Hugging Face API · Papers with Code

---

# 3b. CREATORS, YOUTUBE & PODCASTS — exhaustively tested, all dead

I tried **eight** separate routes to monitor your creator roster automatically. **None work.** Documented so neither of us tries again.

| Route | Endpoint tested | Result |
|---|---|---|
| YouTube RSS | `youtube.com/feeds/videos.xml?channel_id=UCHnyfMqiRRG1u-2MsSQLbXA` (Veritasium, **verified real ID**) | Empty |
| Piped API (open-source YT frontend) | `pipedapi.kavin.rocks/channel/<id>` | Empty |
| RSSHub (open-source RSS generator) | `rsshub.app/youtube/user/@veritasium` | Empty |
| Apple Podcasts search API | `itunes.apple.com/search?term=huberman+lab&entity=podcast` | Empty |
| Podcast RSS | `feeds.megaphone.fm/hubermanlab` | **Reached, but gzip binary — undecodable** |
| Substack RSS | `noahpinion.blog/feed` | **Reached, but gzip binary** |
| Personal blog Atom | `simonwillison.net/atom/everything` | **Reached, but gzip binary** |
| RSS-to-JSON proxy | `api.rss2json.com/v1/api.json?rss_url=...` | Empty |

### The root cause — two separate walls
1. **YouTube and its open-source mirrors are blocked outright.** Piped and RSSHub exist precisely to solve this and are both unreachable.
2. **`web_fetch` cannot decode gzipped XML.** BBC works only because it serves uncompressed. Almost every podcast host, Substack and personal blog serves gzip — reachable, but the bytes come back unusable. The rss2json proxy would have solved this and is itself blocked.

### What this actually means
**Varun Mayya, Johnny Harris, Andrew Huberman, Dr. K, Karpathy, Cole Medin, Chloe Abram, PolyMatter, CaspianReport, Akshat Shrivastava, Nikhil Kamath's WTF, Stratechery, Import AI, Chartbook, Latent Space** — none can be monitored automatically. There is no subscribe-and-watch mechanism available.

### The honest workaround
Three partial routes, in order of reliability:

1. **Targeted web search per creator.** Works, but only surfaces what's been indexed and ranked — so a video posted this morning is usually invisible. Best for "what did X say about Y", weak for "what did X publish today."
2. **GitHub API** — catches the builders. Karpathy, Cole Medin, AI Engineer and similar ship repos, and star velocity is a real signal of what they're pushing.
3. **HN + Reddit via search** — creator content that matters usually gets *discussed*. Reaching the discussion is second-best to reaching the source, but it filters for significance.

### What would actually fix it
- **A YouTube Data API key** (free tier, 10,000 units/day — roughly 100 channel checks). This is the only real solution for video, and it takes minutes to set up in Google Cloud Console.
- **Self-hosted RSSHub** would fix podcasts, Substack and blogs in one move — but needs somewhere to run it.

Without one of those, treat creator coverage as **best-effort via search**, not monitoring. I'd rather say that plainly than let the digest imply it's watching feeds it isn't.

---

# 4. 🔍 SEARCH-ONLY — the roster

These can't be fetched directly. They're still valuable, but reached via targeted web search each run, which means **coverage is partial and I can't guarantee I'll see everything they publish.**

### AI & ML
TechCrunch · The Verge · Wired · Ars Technica · MIT Technology Review · VentureBeat AI · **Import AI** (Jack Clark) · **The Batch** (Andrew Ng) · **Latent Space** · Ben's Bites · The Rundown AI · AI Tidbits · TLDR AI · **Interconnects** (Nathan Lambert) · **AI Snake Oil** (Narayanan & Kapoor — best sceptic voice) · Simon Willison's blog · lab blogs (OpenAI, Anthropic, DeepMind, Meta AI, Mistral, DeepSeek, Qwen)

### Agentic / building
**Andrej Karpathy** · **Cole Medin** · **AI Jason** · LangChain · AssemblyAI · Mervin Praison · David Ondrej · IBM Technology · **3Blue1Brown** · Matt Wolfe · AI Engineer · **100x Engineer** · Y Combinator
*Repos worth watching:* LangGraph · MCP · Mem0 · OpenHands · Aider · Langfuse · vLLM · CrewAI · Agno

### Business & markets
Reuters · Bloomberg · FT · CNBC · Morning Brew · TLDR · **Stratechery** (Ben Thompson) · **Net Interest** (Marc Rubinstein) · **The Overshoot** (Matthew Klein) · **Noahpinion** (Noah Smith) · **Money & Macro** · **Doomberg** · **The Bear Cave** · The Science of Hitting · Slow Boring · Lenny's Newsletter · Moneycontrol

### India
Mint · The Hindu · Indian Express · Business Standard · NDTV · **The Ken** · **The Morning Context** · **Inc42** · **Entrackr** · YourStory · **Finshots** · The Print · Scroll · **Newslaundry** (media criticism — good for framing-gap checks) · **MediaNama** (tech policy) · Kuvera · Business Today · Zee Business
*Primary:* RBI circulars · SEBI orders · PIB releases · DRHP filings

### Geopolitics
Reuters · AP · BBC · The Economist · Foreign Affairs · Foreign Policy · Al Jazeera · SCMP · Nikkei Asia · **Chartbook** (Adam Tooze) · **Sinocism** (Bill Bishop) · **ChinaTalk** (Jordan Schneider) · Stratfor · War on the Rocks · Lawfare · Geopolitical Daily
*YouTube:* **Johnny Harris** · **PolyMatter** · **CaspianReport** · **Neo** · Context Matters · Zeihan on Geopolitics (verify specifics) · TLDR News · Economics Explained

### Personal finance
**Finshots** · **Zerodha Varsity** · ET Wealth · Motley Fool · Investopedia · Morningstar · Capitalmind · **ValuePickr** · **Akshat Shrivastava** · **CA Rachana Ranade** · Pranjal Kamra · **Nikhil Kamath — "WTF is"** podcast

### Psychology & health
**Huberman Lab** · **Dr. K / HealthyGamer** · **Hidden Brain** (Shankar Vedantam) · The Psychology Podcast (Scott Barry Kaufman) · The Happiness Lab · Finding Mastery · Peter Attia · **Experimental History** (Adam Mastroianni) · Astral Codex Ten · Nature Human Behaviour

### Explainer, culture & taste
**Chloe Abram** · **Varun Mayya** · Veritasium · Kurzgesagt · Wendover · Half as Interesting · Not Just Bikes · Vox · 99% Invisible · Every.to · **The Pudding** · Works in Progress · Damn Interesting · **Atlas Obscura**

### Reddit (search-only — API blocked)
r/LocalLLaMA · r/MachineLearning · r/OpenAI · r/ClaudeAI · r/LLMDevs · r/LangChain · r/AI_Agents · r/MCP · r/ExperiencedDevs · r/investing · r/stocks · r/SecurityAnalysis · r/economics · r/IndiaInvestments · r/india · r/IndiaSpeaks · r/IndianStreetBets · r/developersIndia · r/StartUpIndia · r/hyderabad · r/indore · r/geopolitics · r/credibledefense · r/NeutralPolitics · r/personalfinance · r/Bogleheads · r/IndiaTax · r/ValueInvesting · r/science · r/space · r/biotech · r/psychology · r/cogsci · r/ScientificNutrition · r/travel · r/solotravel · r/IndiaTravel · r/awardtravel · r/AskHistorians · r/DepthHub · r/UnresolvedMysteries · r/dataisbeautiful · r/slatestarcodex · r/Cricket · r/soccer · r/formula1

---

# 5. Honest summary

**7 sources are genuinely live and callable.** BBC World RSS, mfapi.in, Frankfurter, HN Firebase, GitHub Search, Indian Data Project, **SEC EDGAR**.

**~150 sources are search-only.** Real, valuable, but reached by querying rather than subscribing — so coverage is best-effort, not exhaustive.

**The three losses that matter most:**
1. **Creators are unreachable.** Eight routes tested — YouTube RSS, Piped, RSSHub, Apple Podcasts, podcast RSS, Substack, blog Atom, rss2json proxy. All dead or undecodable. Your entire creator roster is best-effort-via-search only.
2. **No live stock quotes anywhere** — your equity book stays on dated workbook figures. (SEC EDGAR now gives audited *fundamentals* for US holdings, which partly compensates.)
3. **Reddit's API is blocked** — though the WallStreetBets sentiment endpoint may be a partial workaround, untested.

## API keys — tested for reachability before recommending

I probed each provider's endpoint with a dummy key. If a domain is blocked, a valid key is worthless — so this was worth checking first.

| Provider | Domain reachable? | Verdict |
|---|---|---|
| **Alpha Vantage** | ✅ **YES** — returned a proper JSON error to the demo key | **GET THIS ONE** |
| Finnhub | ❌ Empty response — blocked | Don't bother |
| YouTube Data API (`googleapis.com`) | ❌ Empty response — blocked | **Don't bother — a key will not help** |
| Chrome route to YouTube | ❌ `youtube.com` blocked in Chrome too | Dead end |

### → Get an Alpha Vantage key. It's the only one that will work.
Free at `alphavantage.co/support/#api-key`, takes under a minute.

**Free tier: 25 calls/day, 5/min.** Tight, but workable if spent deliberately:
- `GLOBAL_QUOTE` for your **Tier-1 holdings only** (~8–10 calls)
- `CURRENCY_EXCHANGE_RATE` as an FX cross-check (1 call)
- A few `OVERVIEW` or `TIME_SERIES_DAILY` calls for whatever's in the news that day

That covers the biggest gap in the finance tab — live prices for the holdings that actually matter — without needing the full book.

**⚠️ Do not paste the key into chat.** Save it to a file in the outputs folder (e.g. `secrets.txt`) and I'll read it from there. Keys pasted into a conversation end up in history and logs; a file you control doesn't.

### Creators: confirmed unfixable
YouTube is blocked via **web_fetch, via Chrome, and via the official API domain**. There is no key, no proxy and no browser route that reaches it. Creator coverage stays best-effort-via-search, permanently, unless the tooling changes.

---

## Your review

Mark this file up however you like:
- Sources to **cut** (never interesting to you)
- Sources to **add** (anything I've missed)
- Sources to **promote** (must appear every day, not just when relevant)
- Whether to get a **Finnhub/Alpha Vantage key** for live stock prices
