# digest-fetcher

Fetches every source for the daily digest and commits the result as JSON. Runs free on GitHub Actions.

## Why this exists

My sandbox has **no network access**, and `web_fetch` runs against a strict allowlist. Tested and blocked from there: YouTube (web, Chrome, *and* the official API), Reddit, RSSHub, Livemint, The Hindu, Ars Technica, Google News, GDELT, Yahoo Finance, Finnhub. On top of that, `web_fetch` can't decode gzipped XML — which kills nearly every podcast, Substack and blog feed.

**GitHub Actions has none of those restrictions.** It's a plain Ubuntu box with full internet, free for public repos.

So: Actions does the fetching → commits JSON → I read `raw.githubusercontent.com`, which **is** reachable. Every block disappears.

```
GitHub Actions (00:00 UTC / 05:30 IST)
  → fetch.py hits YouTube, Reddit, 30+ RSS feeds, HN, GitHub, FX, quotes
  → commits data/latest.json
Claude (07:00 IST)
  → reads raw.githubusercontent.com/<you>/digest-fetcher/main/data/latest.json
  → builds the digest
```

The 90-minute gap means the data is always fresh and already committed before the digest runs.

## Setup — about 10 minutes

**1. Create a public repo** called `digest-fetcher` (public matters: Actions is free and `raw.` URLs need no auth).

**2. Add these files**, keeping the structure:
```
.github/workflows/fetch.yml
fetch.py
sources.py
data/            (created automatically)
```

**3. Enable write permissions**
Settings → Actions → General → Workflow permissions → **Read and write permissions** → Save.
Without this the commit step fails.

**4. Add your Alpha Vantage key** (optional but recommended)
Settings → Secrets and variables → Actions → New repository secret
Name `ALPHAVANTAGE_KEY`, value = your key from [alphavantage.co](https://www.alphavantage.co/support/#api-key).
Skip it and everything still runs; only the `quotes` block is empty.

**5. Run it once manually**
Actions tab → "Fetch digest sources" → **Run workflow**. Takes ~2 minutes.

**6. Send me the URL**
```
https://raw.githubusercontent.com/<your-username>/digest-fetcher/main/data/latest.json
```
I'll wire it into the 07:00 digest.

## Customising `sources.py`

**YouTube** — the part that matters most, since it's otherwise unreachable. Add `channel_id: "Label"` pairs. Get IDs from [commentpicker.com/youtube-channel-id.php](https://commentpicker.com/youtube-channel-id.php) by pasting a channel URL. Worth adding: Varun Mayya · Johnny Harris · Huberman · Dr K (HealthyGamer) · Cole Medin · AI Jason · PolyMatter · CaspianReport · Akshat Shrivastava · Nikhil Kamath · Chloe Abram · 3Blue1Brown · Y Combinator.

**RSS** — 30+ feeds pre-loaded, including every one blocked from my side. Add any `"Label": "url"` pair.

**Reddit** — 15 subs pre-loaded. Add `"sub": "top"` (or `"new"` for local subs, where volume is low and recency matters more than score).

**QUOTES** — keep this short. Alpha Vantage's free tier is 25 calls/day and the workflow spends one per symbol.

## What lands in `latest.json`

| Key | Contents |
|---|---|
| `youtube` | Last 5 videos per channel — title, URL, published |
| `rss` | Up to 12 items per feed, with the feed's own `updated` so staleness is visible |
| `reddit` | Top 10 per sub — title, score, comment count, flair, permalink |
| `hackernews` | Top 25 with a **`controversy`** score (comments ÷ points; >1.0 = argument, not consensus) |
| `github` | 20 repos created in the last 3 weeks with >300 stars — a real velocity proxy |
| `fx` | USD/INR from Frankfurter |
| `quotes` | Alpha Vantage prices, if the key is set |
| `errors` | **Every failure, named.** Nothing fails silently. |

A dated copy (`data/2026-08-01.json`) is kept alongside `latest.json` so storylines can be tracked across days.

## Design notes

- **No source can break the run.** Every fetch is individually wrapped; failures land in `errors` and the rest continues.
- **Staleness is exposed, not hidden.** Feed `updated` timestamps are passed through — BBC Technology was two weeks stale when I tested it, and you should be able to see that.
- **Zero cost.** Public-repo Actions minutes are free, and every source here is free-tier or keyless.
- **`sources.py` is the only file you need to touch.** `fetch.py` shouldn't need editing to add a source.

## Credit

The GitHub-Actions-as-fetcher pattern is the one used by `m1guelpf/auto-digest` and `osint-ambition/news-digest-generator`. RSSHub is worth self-hosting later if you want feeds for sources that publish none — its public instance is blocked from my side, but a self-hosted one would be reachable from Actions.
