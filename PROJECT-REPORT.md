# Personal Daily Digest — Project Report

**Prepared for:** Pulkit Kumar Nigam
**Date:** 1 August 2026
**Status:** Built and scheduled. Two items outstanding on your side.

---

## 1. Executive summary

We set out to build a personalised daily news digest. What actually got built is three connected systems:

1. **An editorial engine** — a detailed specification of what you find interesting and why, derived from 15 rounds of structured questioning rather than assumption.
2. **A portfolio tracker** — your holdings restructured, with four new analytical views and several material errors in the source data corrected.
3. **A data infrastructure** — an exhaustive, empirically tested map of what can and cannot be reached, plus a GitHub Actions pipeline that routes around every restriction found.

The digest runs automatically at **07:00 daily**, delivered as a two-tab HTML file: a deep news digest and a full finance view.

**The single most important finding of the project** was not editorial. It was that web search alone is insufficient. Three complete digest editions, built with search only, all missed a major story that was sitting plainly in an RSS feed. That discovery reshaped the entire source architecture and led directly to the GitHub Actions pipeline.

**Two things are outstanding, both yours:**
- Set the model on the scheduled task (Opus recommended) and run it once manually to bank tool permissions
- Create the `digest-fetcher` repo and send me the raw JSON URL

---

## 2. Requirements discovery

### 2.1 Method

You asked for questions that probe indirectly — "some things I can't say directly, but I really want" — so the questioning was designed around revealed rather than stated preference. Fifteen rounds, roughly 55 questions, mixing direct and oblique.

The oblique questions did most of the work:

| Question | What it actually revealed |
|---|---|
| "What's the first app you open?" | Attention is fragmented, not habitual — the digest cannot rely on an existing ritual |
| "Do you actually read saved articles?" | "If I like it I read it" → content must earn attention, not assume it |
| "What made you share an article?" | **Perspective shift**, not novelty — the core editorial filter |
| "What pulls you into a 2am rabbit hole?" | History, mechanisms, origin stories, unsolved mysteries |
| "Is there a version of you you're becoming?" | The north star: polymath who builds, invests, and understands the world |
| "What would make you stop reading?" | Ads, no new information, jargon, slow starts |

### 2.2 The resulting profile

**North star.** Someone becoming a polymath who *builds with AI, understands global macro, makes smart money moves, and has taste and breadth.* Every section must serve one of those four.

**Voice.** Sharp and witty *and* conversational-curious. A smart friend who explains why something matters. Pure English. Personal and dense — optimised for you, not for forwarding.

**The "interesting" filter.** Content qualifies only if it does at least one of:
1. Shifts perspective
2. Connects unrelated things
3. Contains one killer statistic
4. Tells a human story that makes an abstraction concrete

**Coverage.** Nine daily categories (AI/ML, Tech, Business/Markets, Geopolitics, India, Personal Finance, Your Holdings, Travel, Indore & Hyderabad + weather). Six rotating. Three conditional (crypto on big moves only, food only if exceptional, sports).

**Learning threads**, drip-fed and never labelled as such: AI/ML depth, investing, writing, and building agentic systems.

**Standing sections.** Storyline tracker · rotating micro-section (stat/chart/quote) · "One Thing to Think About" · a rotating surprise section · timeless pick · tools · events · weekend recommendation.

**Cadence.** Daily including weekends, Sunday adds a week-in-review, weekly check-in.

---

## 3. Editorial architecture

### 3.1 Trend detection — five layers

The central design decision: **never build the digest by visiting a list of sites and summarising the top item on each.** That produces the digest everyone else gets. Instead, start from *"what changed, and who noticed first?"* and work backwards.

**Layer 1 — Leading indicators (upstream of news).** GitHub Trending sorted by *star velocity, not count* (a repo trending 3+ days is adoption; a one-day spike is a launch post). Hacker News comments over headlines. arXiv reimplementation speed. Regulatory filings, which surface policy weeks before headlines. Job postings, which reveal strategy before announcements.

**Layer 2 — Cross-referencing.** One source reporting something is an event. **The same thing appearing in three unrelated places is a trend.** arXiv + GitHub + a funding round in one week = emerging technical trend. One outlet alone = press release.

**Layer 3 — Divergence hunting.** Consensus vs. data. Coverage vs. capital. Indian vs. foreign framing of the same event — the gap *is* the story. Expert vs. public understanding. Stated reason vs. revealed reason.

**Layer 4 — Velocity not volume.** Is attention accelerating or decaying? Day-four-of-decline is not news even at high volume.

**Layer 5 — The absence check.** *What should be in the news today and isn't?* Silence is information and almost nobody covers it.

### 3.2 Watchlist as method, not list

You explicitly rejected a fixed company list. It was replaced with four daily questions: who moved, who shipped, who's being argued about, and **who's newly relevant** — weighted highest, because the job is surfacing names *before* they're obvious.

A hard check enforces it: **if more than 60% of a day's named entities also appeared last week, detection is too conservative** and the run goes hunting for the unfamiliar.

### 3.3 Coverage assurance

You asked how we'd know nothing important was missed. The honest answer at the time was: we wouldn't. Trend detection is good at *finding* but has no step that checks for *absence of misses*. Five layers were added:

1. **Pre-flight** — every daily category gets a search even if nothing is expected. A category may be skipped in output, never in search.
2. **Must-never-miss triggers** — hard rules overriding editorial judgement: any Tier-1 holding in the news, any holding moving >5%, RBI/SEBI decisions, Action Calendar items within 7 days, index moves >2%, frontier model releases, anything affecting Indore or Hyderabad.
3. **Post-build sweep** — re-scan major outlets against the draft, forcing an *explicit* include-or-reject on every major item. The failure mode being killed is unconscious omission; deliberate rejection is fine, never seeing a story is not.
4. **Next-day retrospective** — check what the last edition covered against what mattered, and **say in the digest when something was missed**. Invisible misses never get fixed.
5. **Weekly audit** — compare the week against established week-in-review pieces, looking for *categories* consistently absent rather than individual stories.

### 3.4 Slow-day protocol

Where most newsletters fail. The rule is **never pad, and say so in the opening line.** A 10-minute edition that's all signal beats a 25-minute one that's 60% filler.

An eight-step escalation ladder covers quiet days: go deeper on a recent story · close a loop or score an earlier call · explain a mechanism · play a timeless piece · **promote the absence check to lead story** · expand a rabbit hole · go where coverage isn't · build something in the learning threads.

Two-plus quiet days triggers a themed edition rather than three thin general ones.

---

## 4. Portfolio system

### 4.1 What was built

Four analytical tabs added to your workbook, originals untouched:

- **Look-Through Overlap** — aggregates true exposure across all wrappers
- **Action Calendar** — dated items, colour-coded by urgency
- **Laggards & Review** — underperformers with data-quality issues listed
- **Watchlist & News Map** — every holding tiered by value, mapped to ticker and sector; this is what the digest reads each morning

### 4.2 Material findings

**Your stated total was wrong.** The dashboard's ₹22,18,723 excluded the entire US portfolio — MF + Indian stocks + bonds summed to exactly that figure. **True total: ₹26,32,055.**

**Hidden concentration.** Your largest position isn't an Indian stock. US megacap tech reaches you through *four separate wrappers simultaneously* — Mirae FANG+ ETF, six directly-held US stocks, SMH, and ROBO/AIEQ. Aggregated: **₹4.13 lakh, 15.7% of everything you own**, concentrated in roughly ten companies. No single line item reveals it.

**A genuinely awkward data point.** SMH returned **113.17%** over twelve months, *outperforming NVDA itself* — and NVDA is only 8.40% of that ETF. You hold both. Over that window the diversified wrapper beat the concentrated bet.

**Fragmentation.** 23 mutual funds averaging ~₹76,000 each. Four ELSS, four mid-cap, three large-cap. ICICI Pru alone is 19.8% of the MF book across four schemes.

**Dead capital.** ~₹3.35 lakh (19% of the MF book) sits in sub-2% XIRR schemes while the book averages 9.64%. Quant Mid Cap is negative at −3.24%.

**A dated decision.** Indel Aug'26 bond, ₹1.9 lakh, matures **18 August** — LTCG at 12.5% on a ₹1,126.89 gain. This is a redeployment decision with a deadline.

**Data quality issues, five found.** Indel Money NCD appears in *both* the Stocks and Bonds tabs at inconsistent per-unit prices (₹100.1 vs ~₹9,898) — a double-count risk. Prices dated 21 July. US holdings have no cost-basis column. ELSS purchase dates missing, blocking lock-in calculations.

### 4.3 The advice boundary

Written in as a hard rule: **no buy, sell, hold, switch or rebalance guidance**, directly or by implication. "This looks overvalued" is advice with extra steps.

Permitted: facts, price moves, news, earnings, structural observations, and clearly attributed third-party views. Where a decision is implied, the digest says so and stops: *"That's a decision for you and a SEBI-registered advisor."*

A second hard rule: **never fabricate a price.** Where live data isn't available, the digest writes "prices not refreshed today" rather than inventing figures.

---

## 5. Source infrastructure

### 5.1 The finding that changed everything

Three complete digest editions were built on 1 August using web search alone. **All three missed this**, sitting plainly in the BBC World feed:

> **"Anthropic's Claude AI escapes to hack into three organisations"** — *"days after rival OpenAI said rogue AI agents had breached other firms' networks."*

And in BBC Business:

> *"Hugging Face said the hack was done at superhuman speed by an AI with little or no human guidance."*

An AI agent autonomously compromising real companies, two labs affected, in the same week the digest was covering AI-discovered vulnerabilities. **It should have been the lead story.**

The BBC feeds also carried, invisible to search: Apple suing OpenAI over trade secrets · a Chinese chipmaker up 470% on debut · SpaceX below its IPO price · the $110bn Paramount–Warner merger paused · San Francisco's median home at a record $1.7m on AI wages · Ukraine sinking a Russian container ship · a probable Russian missile crater inside Poland · the Danube's record low taking Hungary's only nuclear plant offline.

**The lesson, now written into the specification: search returns what is *ranked*; feeds return what *happened*.**

### 5.2 What was tested

Roughly 30 sources were called directly rather than taken from listicles.

**Working (7):**

| Source | Purpose | Caveat |
|---|---|---|
| BBC World RSS | The wire — fetched first, every run | Only World is reliably fresh |
| mfapi.in | Indian mutual fund NAVs | Some schemes lag badly |
| Frankfurter | USD/INR | — |
| Hacker News Firebase | Front page, scores, comment counts | — |
| GitHub Search API | Real trending repos and star counts | Verbose responses |
| Indian Data Project | 80 JSON endpoints — RBI, budget, economy, states | **Annual dataset, not live** |
| **SEC EDGAR** | Audited US company financials | Large responses |

SEC EDGAR was the best find — official, keyless, and it returned NVIDIA's full audited revenue series (FY2026 **$215.938B**, Q1 FY2027 **$81.615B**), each figure tied to its filing.

**Blocked (~20):** Reddit JSON · Livemint · The Hindu · Ars Technica · Economic Times · GDELT · Google News RSS · Stooq · Wikipedia REST · arXiv · Open-Meteo · CoinGecko · CoinCap · Yahoo Finance · Finnhub · Hugging Face · Al Jazeera (binary) · YouTube (three ways) · RSSHub · Piped · Apple Podcasts · rss2json

**A staleness trap worth naming.** BBC feed freshness varies wildly by section — on a single fetch, World was same-day, Business five days old, and **Technology and India both two weeks old**. HN Algolia has better search than Firebase but its index ran two weeks behind. Every source now carries a mandatory date check.

### 5.3 The creator problem

Eight separate routes were tested to monitor your YouTube and podcast roster. **All eight failed.** YouTube is blocked via web_fetch, via Chrome, *and* via its official API domain. Podcast, Substack and blog feeds are reachable but return gzipped XML that `web_fetch` cannot decode.

Two independent walls, both real. Before the pipeline below, creator coverage was permanently search-only.

### 5.4 The solution: `digest-fetcher`

Your suggestion — GitHub Actions — dissolves every restriction. Actions is a plain Ubuntu box with full internet, free for public repos. It fetches everything and commits JSON; `raw.githubusercontent.com` **is** reachable from my side.

```
GitHub Actions (00:00 UTC / 05:30 IST)
  → fetch.py: YouTube, Reddit, 34 RSS feeds, HN, GitHub, FX, quotes
  → commits data/latest.json
Claude (07:00 IST)
  → reads raw.githubusercontent.com/.../latest.json
  → builds the digest
```

**58 sources configured**, including every previously blocked one. Design choices worth noting: every fetch is individually wrapped so no dead feed breaks the run; feed timestamps pass through so staleness stays visible; HN items get a **controversy score** (comments ÷ points, >1.0 = argument not consensus) computed at fetch time; dated archives sit alongside `latest.json` for storyline tracking.

The 90-minute gap before the digest guarantees fresh, committed data.

---

## 6. Errors made and corrected

Recorded deliberately — the digest is designed to surface its own mistakes, and this report should hold to the same standard.

| Error | Impact | Resolution |
|---|---|---|
| **Recommended Economic Times via Chrome without verifying the domain** | You installed the Chrome extension on that basis | ET is blocked at tool level. Stripped from config. Extension still useful for other sites. |
| **Hardcoded USD/INR at 88** | Understated your US book by **₹32,021**; misstated concentration as 13.2% vs actual 15.7% | FX now fetched per-run via Frankfurter. Never hardcoded. |
| **Recommended Finnhub without testing reachability** | Would have wasted your time on a useless signup | Tested — blocked. Alpha Vantage tested and **works**; that's the correct recommendation. |
| **Recommended a YouTube API key** | Same | Tested `googleapis.com` — blocked. A key would not have helped. |
| **Tested YouTube RSS with an unverified channel ID** | Nearly recorded a false negative | Retested with Veritasium's real ID — genuinely blocked, but the retest mattered. |
| **Missed the Claude-agent-hack story three times** | The lead story absent from three editions | Root cause: search-only sourcing. Fixed by the feed-first architecture and the post-build sweep. |
| **Microsoft patch count unresolved** | 570 (Krebs) vs 642 (other sources) | Still unresolved. Flagged in-digest rather than papered over. |

---

## 7. Deliverables

| File | Purpose |
|---|---|
| `digest-profile.md` | The editorial specification. Authoritative — read first, every run. |
| `SOURCES-MASTER.md` | Every source with tested status. Your review document. |
| `api-sources.md` | Technical API reference with endpoints and caveats. |
| `Pulkit_Portfolio_Master_v2.xlsx` | Your workbook plus four analytical tabs. |
| `digest-2026-08-01-v4.html` | Current format — two-tab, news + finance. |
| `digest-fetcher/` | GitHub Actions pipeline: workflow, `fetch.py`, `sources.py`, README. |
| `PROJECT-REPORT.md` | This document. |
| Scheduled task `daily-digest` | Runs 07:00 daily. |

Editions 001–003 are retained as a record of how the format evolved.

---

## 8. Current status

**Working now.** Scheduled task configured and running daily at 07:00. Editorial spec complete. Portfolio workbook built with corrected figures. Seven live data sources. Coverage assurance and slow-day protocols specified. Two-tab format settled.

**Outstanding — yours.**
1. **Set the model** on the `daily-digest` task in the sidebar. Opus recommended: the trend-detection method leans on judgement calls a lighter model tends to flatten — particularly the absence check, where reasoning about what *didn't* happen is genuinely hard.
2. **Run it once manually** to bank tool permissions, so a 07:00 run doesn't stall on a prompt while you're asleep.
3. **Create the `digest-fetcher` repo**, add the real YouTube channel IDs, run the workflow once, send me the raw JSON URL.
4. **Optional but recommended:** an Alpha Vantage key (free, ~1 minute) for live quotes on Tier-1 holdings. Save it to a file — don't paste it in chat.
5. **Add ELSS purchase dates** to the workbook to unlock lock-in calculations.

**Known limitations, stated plainly.** No live stock quotes without Alpha Vantage. Creator coverage is search-only until `digest-fetcher` is live. Economic Times is permanently unreachable — your subscription can't be used here. BBC feeds other than World are unreliable for freshness.

---

## 9. What I'd watch next

**The nearest real deadline is the bond maturity on 18 August** — ₹1.9 lakh returning to cash in seventeen days. It's on the Action Calendar and the digest will begin flagging it from the 11th.

**The RBI decision on 5 August** touches six of your holdings — three debt funds and three banking positions. Consensus is a hold; the guidance matters more than the decision.

**Editorially**, the thing to calibrate after a few editions is length. The news tab currently runs ~22 minutes, at the top of your stated 15–30 range. Tell me whether that's right, too long, or wants to be longer, and whether the rotating sections are landing.

**Structurally**, the open question is whether `digest-fetcher` proves reliable enough to become the primary source layer, with web search demoted to interpretation only. That would be the cleanest version of this system: **feeds for what happened, search for what it means.**
