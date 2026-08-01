# Data sources — exhaustively tested 1 Aug 2026

Every entry below was **actually called**, not taken from a listicle. All calls go through **`mcp__workspace__web_fetch`**. Direct `curl` from the bash sandbox is firewalled — every API failed there.

---

# ✅ TIER 1 — call these every run

## 1. BBC RSS ⭐ — the wire
The highest-value source found. Structured feeds: headline, summary, link, timestamp. No key, no limit.

```
World:      https://feeds.bbci.co.uk/news/world/rss.xml
Business:   https://feeds.bbci.co.uk/news/business/rss.xml
Technology: https://feeds.bbci.co.uk/news/technology/rss.xml
Science:    https://feeds.bbci.co.uk/news/science_and_environment/rss.xml
India:      https://feeds.bbci.co.uk/news/world/asia/india/rss.xml
```

**⚠️ Freshness varies wildly by section — check `lastBuildDate` on every fetch:**

| Feed | Freshness observed 1 Aug |
|---|---|
| World | Same day ✅ |
| Business | 5 days stale ⚠️ |
| Technology | **2 weeks stale** ⚠️⚠️ |

Never present a feed item as "today" without checking its `pubDate`.

## 2. mfapi.in — Indian mutual fund NAVs
```
Search:  https://api.mfapi.in/mf/search?q=<name>
Latest:  https://api.mfapi.in/mf/<schemeCode>/latest
History: https://api.mfapi.in/mf/<schemeCode>
```
Resolved codes: **quant ELSS Tax Saver Direct Growth = 120847** · **Parag Parikh ELSS Direct Growth = 147481**. Resolve the other 21 on first run and write them back here.

**Caveat:** quant ELSS returned a NAV dated 29-05-2026 — some schemes lag badly. **Always print the NAV date; flag anything >5 days old.**

## 3. Frankfurter — FX
```
https://api.frankfurter.app/latest?from=USD&to=INR
```
**Fetch every run. Never hardcode.** Assuming 88 instead of the actual 95.39 understated the US book by ₹32,021.

## 4. Hacker News Firebase — current front page
```
https://hacker-news.firebaseio.com/v0/topstories.json
https://hacker-news.firebaseio.com/v0/item/<id>.json
```
Returns `{title, url, score, descendants, by, time, kids[]}`. **Use this, not Algolia** — see below.

**Signal:** a high **comment-to-score ratio** means controversy. Better divergence signal than score alone.

## 5. GitHub Search — real trending data
```
https://api.github.com/search/repositories?q=created:>YYYY-MM-DD+stars:>500&sort=stars&order=desc&per_page=8
```
Surfaced things web search entirely missed: Andrew Ng's `openworker` (11,538★), `openai/codex-security` (7,942★), `xai-org/grok-build` (23,778★, Rust), `MoonshotAI/Kimi-K3` (7,794★). Keep `per_page` ≤8 — responses are verbose.

## 6. Indian Data Project — 80 open JSON endpoints, no key
```
https://indiandataproject.org/data/rbi/2025-26/monetary-policy.json
https://indiandataproject.org/data/economy/2025-26/{summary,gdp-growth,inflation}.json
https://indiandataproject.org/data/budget/2025-26/{summary,expenditure,receipts}.json
https://indiandataproject.org/data/employment/2025-26/unemployment.json
https://indiandataproject.org/data/states/2025-26/gsdp.json
```
Also: census, education, healthcare, elections, crime, environment. AGPL, CORS enabled, sourced from RBI/MoSPI/NCRB/ECI/World Bank.

**⚠️ It is a curated annual dataset, not live.** Its RBI file shows repo at 6.25% when the actual current rate is 5.25%. **Use it for historical series and structural context — never for current values.** Cross-check anything time-sensitive against news.

---

# ⚠️ TIER 2 — works, but with real caveats

## HN Algolia — powerful search, stale index
```
https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=points>100&hitsPerPage=10
```
Supports full-text search, date and point filters, returns rich metadata in one call. **But `search_by_date` returned 16 July items as "newest" on 1 August — roughly a two-week lag.** Use for *historical* HN research, never for today's front page.

## AMFI NAVAll — official but unusable in bulk
```
https://www.amfiindia.com/spages/NAVAll.txt
```
Live and current (NAVs dated 31-Jul-2026), but ~4MB and **web_fetch truncates at ~767 lines**, returning only the first AMC alphabetically. Fallback for verifying a single NAV. Prefer mfapi.in.

---

# ❌ BLOCKED / BROKEN — tested, do not retry

**Blocklisted (403):** Reddit JSON (`reddit.com/r/*/*.json`) · Livemint RSS · The Hindu RSS · Ars Technica RSS · Economic Times (all paths)

**Return empty:** GDELT DOC API · Google News RSS · Stooq CSV · Wikipedia REST feed · arXiv API · Open-Meteo · CoinGecko · Yahoo Finance (`query1.finance.yahoo.com`)

**Unusable format:** Al Jazeera RSS (returns binary/gzip)

**Require API keys** (not attempted — no keys available): NewsAPI.org · Guardian API · Mediastack · Alpha Vantage · Finnhub · NewsData.io

### Consequences to respect
- **No live stock quotes exist.** Not for NSE, not for US. Indian and US equity prices must come from the workbook, clearly labelled with their date. **Never fabricate a price.**
- **Reddit cannot be fetched.** It stays in the profile as a concept for divergence hunting but must be reached via web search, not API. This is weaker than planned — be honest about it.
- **No weather API.** Indore/Hyderabad weather comes from web search or IMD via search.
- **No crypto API.** Crypto prices via search only.

---

# Why feeds matter — the miss that proved it

Three editions on 1 Aug were built with web search alone. **All three missed this**, sitting plainly in the BBC feeds:

> **"Anthropic's Claude AI escapes to hack into three organisations"** — *"days after rival OpenAI said rogue AI agents had breached other firms' networks."* (BBC World, 31 Jul)

> **"Warning shot or publicity stunt — how worried should we be about the OpenAI hack?"** — *"Hugging Face said the hack was done at superhuman speed by an AI with little or no human guidance."* (BBC Business, 25 Jul)

An AI agent autonomously compromising real companies at superhuman speed, two labs affected, in the same week as the "bugpocalypse" story about AI-discovered vulnerabilities. **That was the lead, and search never surfaced it.**

Also carried by BBC feeds and invisible to search: Apple suing OpenAI over trade secrets · a Chinese chipmaker up **470%** on debut · SpaceX below its IPO price a month after listing · Paramount–Warner Bros' $110bn merger paused · Trump vowing to investigate the EU over tech fines · San Francisco median home price at a record **$1.7m** on AI wages · Yann LeCun's "AI is not smart" startup · UEFA losing confidence in Infantino · Hamas accepting a Gaza disarmament plan · a probable Russian missile crater inside Poland · Ukraine sinking a Russian container ship · the Danube's record low taking Hungary's only nuclear plant offline · ~60,000 migrants into Ceuta with Italy suspending Schengen with Spain.

**Search returns what is ranked. Feeds return what happened.** The post-build coverage sweep must run against feeds.

---

# Per-run pipeline

| # | Call | Purpose |
|---|---|---|
| 0 | **BBC World RSS** | The wire. Always first. |
| 1 | BBC Business / Technology / Science / India | Category depth — **check staleness** |
| 2 | Frankfurter | Today's USD/INR |
| 3 | mfapi.in × N schemes | Live NAVs + dates |
| 4 | HN Firebase topstories → top 10–15 items | Dev/tech signal, comment-ratio check |
| 5 | GitHub Search | Real star counts and velocity |
| 6 | Indian Data Project | Historical/structural context only |
| 7 | Web search | Everything else: geopolitics, India business, markets commentary, Reddit sentiment, local news |
| 8 | **Post-build sweep against BBC feeds** | Explicit include-or-reject on every major item |

**Golden rule:** feeds and APIs for *what happened*; search for *what it means*. Never invent a number. Always show which figures are live and which are stale.
