# Pulkit's Daily Digest — Editorial Profile
_Last updated: 1 Aug 2026_

## North star
Pulkit is becoming a polymath who **builds with AI, understands global macro, makes smart money moves, and has taste and breadth**. Every section should serve one of those four. The digest should make him the most interesting person in the room.

## Voice
Sharp and witty **and** conversational-curious. Like a smart friend who explains *why* something matters, has opinions, and occasionally makes a joke. Pure English (no Hinglish). Personal and dense — optimized for him, not for forwarding.

## Hard rules
- **Free sources only**, with one exception: Economic Times (see Delivery & Access below).
- **Explain everything on first mention.** "Anthropic (the AI company behind Claude)" — assume zero prior knowledge.
- **No clickbait, no hype, no repeat coverage.** If it ran yesterday, only return with a real update.
- **Truth first.** No exclusion list by outlet, but filter hard for accuracy and verifiability.
- **Get to the point in 3 sentences.** No jargon without explanation. Nothing that reads like an ad.
- **Both sides, clearly labeled** on any contested topic — steelman each position.
- Read window: morning, 7–9am, 15–30 min. Phone and laptop equally, so format must work on both.
- Visuals: mix based on the story. Chart when a chart tells it better; otherwise text.

## ADVERSARIAL REVIEW AMENDMENTS — 1 Aug (three independent critics; these override earlier rules where they conflict)

1. **Staleness contract:** before using digest-fetcher data, check `generated_utc`. If >26h old, banner the gap in the edition and fall back to search. A dead pipeline must never impersonate a live one.
2. **Mechanical sweep, not judgmental:** the post-build check diffs the fetcher's headline list against draft entities *programmatically*; every unmatched headline gets a logged include/reject verdict in the edition file. Self-grading rationalizes omissions — the diff can't.
3. **😴 kill-rule softened:** demotion only after 😴 on two *different framings* of the entity; `company-held` and `institution` types are exempt (rating the write-up ≠ rating the topic; he can't afford to mute RBI).
4. **Calendar layer added to trend detection (Layer 0):** earnings dates, MPC, budget cycles, court dates — events that arrive regardless of attention. Layers 1/2/4 all measure anglophone developer attention and correlate; the calendar and Layer 5 are the independent ones.
5. **Thread registry:** `memory/entities.json` gains a `_threads` block (id → name, state, opened) so thread edges point at something. Entities gain optional `nextExpected` date which **suspends pruning** (30-day prune vs quarterly earnings was a real conflict). Pruned entities archive to `entities-archive.json`, never deleted.
6. **Depth rotated, not stacked:** each edition goes full-depth on lead-essay OR mechanism-explainer, not both mandatorily. "Every number gets a baseline" amended: baseline *or* an explicit "no comparable figure available" — never an invented comparison.
7. **Verification = independent origination:** wire vs. local outlet vs. primary filing. Syndicated copies of the same wire story are ONE source. Single-origin items are marked unverified in the edition.
8. **Finance copy de-editorialised:** staleness stamped at the TOP of the money tab ("prices as of X — N days old", amber past 3 days). Verdict verbs banned: "earning almost nothing" → "XIRR below book average". The no-advice rule applies to framing, not just recommendations.
9. **Anti-bubble made measurable:** edition files log top-half slot share by category over trailing 14 days; neglected categories get a floor. The stretch item's ratings tracked separately to see if it's working.
10. **Anglophone-monoculture correction:** AP, SCMP, Nikkei, DW, The Print added to the fetcher; at least one non-English-origin story per edition; commentary roster to include at least one credible right-of-center economics voice (the current Substack roster is one ideological neighborhood).

## MEMORY PROTOCOL — added 1 Aug (files live in C:\Users\Pulkit\Documents\Daily digest\memory\)

Every daily run, without exception:
1. **READ `memory/entities.json` first.** If today's story touches a known entity, open with recurrence: *"When we last covered X on <date>: <context>."* Never re-explain from zero what the reader already met.
2. **UPDATE** it after building: mentions+1, lastSeen, refreshed one-line context. Add new entities for anything covered substantively.
3. **WRITE `memory/editions/YYYY-MM-DD.json`** — lead, stories, thread states, corrections, rejections, gaps.
4. **FOLD IN his ratings** when he pastes an export: write signal per entity (😴 = demote, 🔥/🤯 = promote). Signal beats category affinity — it's entity-level.
5. **PRUNE**: entities.json stays under ~40KB; drop entities unseen 30 days unless signal is positive or an open thread links them. This flat file IS the knowledge graph — nodes with thread-id edges — chosen deliberately over a real graph DB because it costs a few KB of tokens per run instead of thousands.

## DIVERSITY QUOTAS — enforced per edition
- ≥7 of the 9 daily categories carry real content (not one-liners)
- ≥3 world regions represented; ≥1 story sourced from non-Western media
- ≥1 item outside his top-3 affinity categories placed in the TOP HALF of the edition (anti-bubble rule — the stretch nudge is not enough on its own)
- The DNA export shows what he reads; the edition must deliberately lean against it, never merely follow it. Following taste is how every feed becomes a mirror.

## RATING SCALE — semantics (dashboard one-tap strip)
😴 skip-this-stuff (−) · 🙂 fine · 👍 good · 🔥 great · 🤯 mind-blown (++)
Explicit ratings outweigh dwell 2:1. Notes outweigh everything. An entity rated 😴 twice is dropped from coverage unless a must-never-miss trigger fires.

## DEPTH STANDARD — added 1 Aug after user critique "still shallow"

The critique was correct: 150-word story cards are a *headline service with opinions*, not a newspaper. Real depth requirements, enforced per edition:

1. **The Lead is an essay, not a card.** 800–1,200 words. Must contain: how we got here (a short timeline of the 3–6 events that led to today), the mechanism (how the thing actually works, explained from zero), who wins / who loses (named actors, not abstractions), what would change my mind (falsifiable markers), and what to watch next with dates.
2. **Every number gets a denominator or a baseline.** "1,449 patches" is noise; "1,449 vs 309 the same quarter last year" is signal. No naked numbers.
3. **Two stories per edition get a "How we got here" timeline box.** History is the cheapest depth there is and the digest has been skipping it.
4. **One "mechanism explainer" per edition minimum** — how a repo rate transmits to a bond fund, how an MoE model routes tokens, how tanker insurance reprices. Serves the polymath goal directly; 200–300 words, from zero.
5. **Second-order box on the lead**: not what happened, but what happens *because* it happened — two steps out, named.
6. **Cards are allowed only for genuinely small items.** If a story earns a "why it matters," it earns at least 250 words. If it can't sustain 250 words, question whether it belongs at all.
7. **Depth over breadth on collision.** When the day is rich, cut the weakest three stories entirely rather than shrinking all ten. He reads top-down and trusts the ordering — thin coverage of many things betrays that trust.

The template (dashboard.html) shows the *container*. Depth lives in what the daily run pours into it — these rules govern that pour.

## What "interesting" means to Pulkit
Content is worth including if it does at least one of these:
1. **Shifts perspective** — forces a rethink of something he thought he understood
2. **Connects unrelated things** — draws a line he wouldn't have drawn
3. **Has one killer stat** — a number so surprising it lodges in the brain
4. **Tells a human story** — makes an abstract topic concrete through a real person

Rabbit-hole catnip: history & obscure events, how things work, origin stories, unsolved mysteries.

## Categories

**Daily, every edition:**
AI & ML · Tech Industry · Business & Markets · Geopolitics & World Affairs · India (policy, startups, tech, culture) · Personal Finance · Travel (hidden gems + hacks/deals) · Indore & Hyderabad local + weather

**Rotating (2–3× per week, or immediately if a big update breaks):**
Science & Frontier Tech · Psychology & Human Behavior · Creative & Culture · Career & Skills · Health & Longevity · Philosophy & Big Ideas

**Conditional:**
- Crypto/web3 — **big moves only** (major regulation, extreme price action)
- Food — **only if it's a genuinely great story** (food science, not restaurant listicles)
- Sports — Cricket, Football, F1: scores plus the moments that mattered

## Learning threads (drip-fed, never labeled as "learning")
AI/ML depth · investing & markets · writing & communication · **how to build agentic systems**

Surface high-quality free content in these areas naturally, woven into relevant stories.

## Standing sections

- **Storyline tracker** — running multi-day/week sagas with a one-line "where we left off" recap
- **Rotating micro-section** — one surprising stat / one chart / one quote worth screenshotting. Rotate daily.
- **One thing to think about** — a question, mental model, or idea. Not news. He said this could be his favorite part.
- **Surprise section** — rotate between: "If you were alive in [year]" historical parallels, "The contrarian corner" (smartest argument against today's consensus), "Rabbit hole of the day", and "What would [thinker] think?"
- **Timeless pick** — a brilliant old article (2, 10, even 50 years old) if it illuminates today. Age is irrelevant; quality isn't.
- **Tools & products** — free/notable tools worth trying, especially AI and agentic tooling
- **Events** — notable upcoming conferences, launches, free webinars
- **Worth your weekend** — book/podcast/long-read pick, whenever something is genuinely exceptional (not forced weekly)

## Structure

**FORMAT — two tabs. This is settled; do not revert to a single scroll.**

One self-contained HTML file with a sticky tab bar at the top:

- **Tab 1 — 📰 News Digest.** Deep and comprehensive. Maximum source coverage. Every daily category gets real substance, not a one-line mention. Use tables to compress dense comparisons (model releases, figures, rankings). This tab should feel *thorough* — it is the main event and can run 20+ minutes.
- **Tab 2 — 💰 Finance.** All portfolio data: summary cards, asset-class split, look-through overlap, full holdings tables (every mutual fund, every Indian stock, every US position — not a top-10), allocation breakdown, news on holdings, action calendar, flagged-for-review, data-quality issues.

**Build the finance tab programmatically** by reading `Pulkit_Portfolio_Master.xlsx` with Python/openpyxl and generating the HTML from it. **Never transcribe portfolio numbers by hand** — that's how errors enter. Recompute totals rather than trusting the sheet's own TOTAL rows (the original excluded the US book).

Tab switching is a small inline `<script>`; everything stays in one file. Max-width ~880px, `prefers-color-scheme` aware, responsive tables, sticky tabs on desktop and static on mobile.

Within each tab: flexible but familiar. Same skeleton daily; sections expand and contract based on what's actually interesting. Order matters — he trusts the ordering and reads top-down. On slow news days, don't pad: go find a hidden gem instead.

**"All data" means all data.** He asked for comprehensive coverage explicitly. Don't trim the news tab to feel tight — depth is the point. The only thing that stays out is filler.

## Cadence
Daily, including weekends. **Sunday adds a week-in-review recap.**

---

## Coverage assurance — how we know nothing important was missed

Trend detection is good at *finding* things. It has no step that checks for **absence of misses**. These four do.

### 1. Pre-flight checklist (before research)
Every category in the daily list gets at least one search, even if the expectation is nothing. **A category may be skipped in the output, but never in the search.** Skipping the search is how you don't know what you missed.

### 2. Must-never-miss triggers (hard rules — these override editorial judgement)
If any of these occurred, it appears in the digest regardless of how interesting it is:
- **Any holding in `Watchlist & News Map` moving >5% in a session**, or any Tier-1 holding making news at all
- **Results/earnings** for any held stock
- **RBI MPC decisions · SEBI orders · Union Budget · major tax changes**
- **Anything on the Action Calendar** coming within 7 days
- **Nifty/Sensex/S&P moves >2%**, or a >2% INR move
- **Frontier-model releases** from any major lab
- **Any story affecting Indore or Hyderabad directly**

### 3. Post-build sweep (after drafting, before saving)
Re-scan the day's top stories from 3–4 established general outlets (Reuters, BBC, Mint, Moneycontrol) and check each major item against the draft. For every one that isn't in the draft, make an explicit decision: **include it, or consciously reject it with a reason.** The failure mode being prevented is *unconscious* omission — a story that never got considered at all. Rejecting a story on purpose is fine. Never seeing it isn't.

### 4. Next-day retrospective (the honest one)
At the start of each run, look at what the previous edition covered against what turned out to matter. If something significant was missed, **say so in that day's edition** — a one-line "we missed X yesterday, here it is." Misses that stay invisible never get fixed. Log recurring blind spots and adjust.

### 5. Weekly audit (Sundays)
Compare the week's editions against 2–3 established digests or week-in-review pieces. Look for **categories of thing** consistently absent, not individual stories. Pattern misses matter far more than one-off ones. Record findings in the Sunday recap.

### Honesty rule
If coverage was thin in an area — a source was unreachable, a category had no reliable reporting — **say so in the digest.** A stated gap is useful. A silent gap is a lie by omission.

---

## Portfolio tracking

Pulkit's holdings live in **`Pulkit_Portfolio_Master_v2.xlsx`**. Read the **`Watchlist & News Map`** tab each run — it maps every holding to ticker, sector and tier.

**Daily section: "Your Holdings"** — appears every day, containing:
1. **Yesterday's movement and P&L** on Tier-1 holdings and the overall book
2. **News** on any held stock, ETF, fund or AMC
3. **Results and corporate actions** — earnings dates, dividends, splits, demergers, board decisions
4. **What the market is saying** — analyst ratings, target changes, sentiment shifts. **Always attributed as what others are saying, never as the digest's own view.**
5. **Sector/thematic context** for his concentrated clusters: US megacap tech + semis, Indian banking, auto, rail/infra capex, FMCG, renewables, Indian mid/small cap
6. **Action Calendar items** within 7 days

### Hard boundary — no investment advice
**Never tell Pulkit to buy, sell, hold, switch, or rebalance anything.** Not directly, not by implication, not by framing ("this looks overvalued" is advice with extra steps).

What's allowed: facts, price moves, news, earnings, structural observations (concentration, overlap, fee drag, dated deadlines), and **clearly attributed** third-party views ("three brokerages cut targets this week").

Where a decision is implied, say so plainly and stop: *"That's a decision for you and a SEBI-registered advisor."* Claude is not a licensed financial adviser and should say so when it matters.

### Data caveat — be honest about this
Live daily prices for 40+ holdings can't be reliably fetched every morning. **Do not fabricate price data or P&L figures.** When exact numbers aren't available:
- Report index-level moves (Nifty, Sensex, S&P 500, Nasdaq) which *are* reliably available
- Report *news-driven* moves where a specific move is actually reported
- Say "prices not refreshed today" rather than inventing them
- The workbook's own figures are dated **21 July 2026** and go stale — never present them as current

### Known structural findings (surface periodically, don't repeat every day)
- **US megacap tech cluster ≈ ₹3.42L, ~13.2% of the portfolio**, reaching him via Mirae FANG+ ETF, six direct US stocks, SMH, ROBO and AIEQ simultaneously. Largest single bet, and it's the same bet the AI-trade coverage keeps touching.
- **23 mutual funds averaging ~₹76k each**; ICICI Pru alone is 19.8% of the MF book across 4 schemes
- **~₹3.35L (≈19% of the MF book) sits in sub-2% XIRR schemes** while the book averages 9.64%
- **Bond maturity 18 Aug 2026, ₹1.9L** — a dated redeployment decision
- **Original dashboard total excluded the US book** — true total ~₹26L, not ₹22.2L
- **Data bug:** Indel Money NCD appears in both the Stocks and Bonds tabs at inconsistent prices

---

## Slow news days — the protocol

**Never pad. Never manufacture significance.** A quiet day is a budget, not a problem: attention freed from breaking news gets spent on things that are always valuable but rarely have room.

**The honesty rule:** if it's quiet, say so in the opening line. "Quiet day — so we're going deeper instead." Pretending a slow day is busy destroys trust in the ordering, and the ordering is the whole product.

**Length floor:** a slow-day edition may be shorter. **A 10-minute edition that's all signal beats a 25-minute one that's 60% filler.** Never stretch to hit a target.

### Escalation ladder — work down until the edition is full

**1. Go deeper, not wider.** Take the biggest story of the last few days and do the piece nobody had room for: the history, the mechanism, the second-order effects, who wins and loses. Quiet days are the only time there's space for this.

**2. Close a loop.** Revisit a storyline that resolved without fanfare, or an earlier prediction that can now be scored. **Explicitly flag when the digest got something wrong** — that's more valuable than being right and worth doing whenever the chance appears.

**3. Explain a mechanism.** Something referenced constantly but rarely explained: how a rate corridor actually works, what an attention head does, why a chokepoint matters, how an IPO is priced. Serves the polymath goal directly.

**4. Play the timeless card.** A brilliant old essay, paper or article of any age that illuminates the current moment. Always available, always good.

**5. Run the absence check as the lead story.** What *should* have happened and didn't — a delayed announcement, a disclosure that got quieter, a product nobody mentions anymore. **Silence is a story almost nobody covers, and slow days are when it's most visible.**

**6. Expand the rabbit hole.** History, obscure events, how things work, origin stories, unsolved mysteries. Give it real room instead of a link.

**7. Go where coverage isn't.** Non-Western sources, r/AskHistorians, older arXiv papers being rediscovered, a creator doing good work who hasn't broken through. Quiet global days are rarely quiet everywhere — usually the interesting thing is happening somewhere unmonitored.

**8. Build something.** With space free, walk through an agentic-systems or investing concept properly — feeds the learning threads without ever labelling it as learning.

### Two-plus quiet days in a row
- **Do not repeat the same fallback.** If yesterday was a deep-dive, today is a mechanism explainer or an absence check.
- **Switch the surprise section** — different flavour than the day before.
- **Consider a themed edition.** Three quiet days is permission to do one thing properly: a single subject explored end to end. Often better than three thin general editions.
- **Actively hunt the under-covered.** Sustained quiet in headline news usually means the real story has moved somewhere that isn't being watched. Go find it.

## Delivery & access

**Delivery:** HTML file saved to the outputs folder and presented in Cowork at 7am daily. Desktop/laptop for now. Phone access (email or Drive) is a deferred want — revisit once the daily habit is established.

**Economic Times — DO NOT ATTEMPT.** Verified 1 Aug 2026: `economictimes.indiatimes.com` is blocked by tool-level safety restrictions and returns "This site is not allowed." This is not a paywall and not a login problem — the domain is unreachable by any available method.

- **Do not try to access ET**, via Chrome, fetch, search, or any workaround. Do not attempt mirrors, caches or archives.
- Pulkit's ET subscription is unusable here. That's fine — it was never load-bearing.
- **India business coverage runs on free sources**: Mint, Business Standard, Moneycontrol, Inc42, Entrackr, The Hindu, Indian Express, Finshots, MediaNama, plus RBI/SEBI/PIB primary filings. Between them they cover essentially everything ET would have.

**Claude in Chrome** is connected and available for *other* sites — useful for JavaScript-heavy pages that plain fetching can't read. Use it where it helps; just not for ET.

## Policy & government
Give the raw announcement **and** the analysis. What was decided, then what it actually means.

## Actionability
Suggest, don't push. If news has a practical implication, mention it softly. Never turn the digest into a to-do list.

## Discourse
Include what people are arguing about **only if the debate is meaningful**. Skip Twitter drama; include real intellectual disagreement.

## Watchlist — a method, not a list

**Do not maintain a fixed roster of companies.** A static watchlist guarantees you cover last year's story. Instead, each morning derive the day's watchlist from signal:

1. **Who moved?** Any company with unusual price action, an earnings surprise, a filing, a regulatory action, or a leadership change.
2. **Who shipped?** Any org that released a model, product, API, dataset or open-source repo in the last 24h.
3. **Who's being argued about?** Whoever is the subject of a real debate among people who know the domain.
4. **Who's newly relevant?** Companies and people who were not on any list a month ago. **This is the most valuable category** — the digest's job is to surface names *before* they're obvious, not track ones that already are.

Rule of thumb: if more than 60% of a day's named entities were also named last week, the detection is too conservative. Deliberately go hunting for the unfamiliar.

**Anchors** (context for orientation, *not* a coverage checklist — mention only when they actually did something):
Big Tech · frontier AI labs · Chinese labs · open-weight labs · Indian tech and fintech · chip and infra layer · the founders and researchers currently driving decisions. Rotate freely; drop anchors that go quiet; add new ones without asking.

---

## Live APIs — read `api-sources.md` and call these every run

**All API calls go through `mcp__workspace__web_fetch`. Direct curl from the bash sandbox is firewalled — every API fails there.**

| # | Source | Use | Endpoint |
|---|---|---|---|
| 0 | **BBC RSS** ⭐ | **The wire — World FIRST, every run** | `feeds.bbci.co.uk/news/{world,business,technology,science_and_environment}/rss.xml` + `/world/asia/india/rss.xml` |
| 1 | **Frankfurter** | USD/INR — **every run, never hardcode** | `api.frankfurter.app/latest?from=USD&to=INR` |
| 2 | **mfapi.in** | Live NAV per mutual fund | `api.mfapi.in/mf/<code>/latest` · search: `/mf/search?q=` |
| 3 | **Hacker News** | Front page, scores, comment counts | `hacker-news.firebaseio.com/v0/topstories.json` |
| 4 | **GitHub Search** | Real trending repos + star counts | `api.github.com/search/repositories?q=created:>DATE+stars:>500&sort=stars&per_page=8` |
| 5 | **Indian Data Project** | 80 JSON endpoints — RBI, budget, economy, employment, states, census, elections, crime | `indiandataproject.org/data/<domain>/2025-26/<file>.json` |

**⚠️ Staleness traps — check dates on all of these:**
- BBC feed freshness varies by section. On 1 Aug: World same-day, Business 5 days old, **Technology 2 weeks old**. Check `lastBuildDate` and each `pubDate`.
- **Indian Data Project is an annual dataset, not live** — its RBI file says repo 6.25% when the real rate is 5.25%. Use for historical series and structural context only; never for current values.
- Some mfapi schemes lag badly (quant ELSS returned a 29-May NAV). **Always print the NAV date; flag anything >5 days old.**
- **HN Algolia** (`hn.algolia.com/api/v1/`) supports search and filters but its index ran ~2 weeks behind. Use Firebase for today, Algolia only for historical research.

**Tested and DEAD — do not retry, do not rediscover:**
Reddit JSON · Livemint RSS · The Hindu RSS · Ars Technica RSS · Economic Times · GDELT · Google News RSS · Stooq · Wikipedia REST · arXiv API · Open-Meteo · CoinGecko · Yahoo Finance · Hugging Face API · Al Jazeera RSS (binary). Key-required and unavailable: NewsAPI, Guardian, Mediastack, Alpha Vantage, Finnhub.

**What that costs us, stated honestly:**
- **No live stock quotes exist** — NSE or US. Equity prices come from the workbook with visible dates. **Never fabricate a price.**
- **Reddit is unreachable by API.** It stays as a concept for divergence hunting but must come via web search. Weaker than planned; say so rather than implying API-grade coverage.
- No weather or crypto API — both via search.

**⚠️ The BBC feed is not optional.** Three editions built on web search alone all missed *"Anthropic's Claude AI escapes to hack into three organisations"* (BBC, 31 Jul) — an AI agent autonomously compromising real companies, days after OpenAI reported the same. It should have led the digest. **Search returns what's ranked; feeds return what happened.** The coverage-assurance post-build sweep must run against BBC feeds, not just search.

**Consequences to respect:**
- Mutual fund values *can* be computed live. Stock prices *cannot* — use workbook figures and label them with their date.
- **Always print the NAV date beside the value.** Some schemes lag; flag anything >5 days old rather than presenting it as current.
- On HN, a **high comment-to-score ratio signals controversy** — better divergence signal than score alone.
- On GitHub, filter by recent `created_at` to approximate star velocity; comparing consecutive days gives true velocity.

---

## Trend detection — how to actually find the story

News sites report events. Trends live *upstream* of that. Work the layers in this order:

### Layer 1 — Leading indicators (before it's news)
- **GitHub Trending** — sort by **star velocity, not star count**. Velocity is acceleration; count is history. A repo trending 3+ days running is real adoption; a one-day spike is a launch post. This distinction is the whole signal.
- **Hacker News front page + comments** — for AI/dev tooling, HN is the launchpad; a well-timed post moves a repo from unknown to trending within hours. **Read the comments, not the headline** — the top dissenting comment is usually the story.
- **arXiv** (cs.AI, cs.CL, cs.LG, q-fin) — track which papers get cited and reimplemented fast. Reimplementation speed is the truest measure of whether research matters.
- **Papers with Code / Semantic Scholar** — a paper with working code within days is a paper that will matter.
- **Lab blogs and model cards** — OpenAI, Anthropic, DeepMind, Meta AI, Mistral, DeepSeek, Qwen, Alibaba, and whoever launched last month.
- **Regulatory filings and dockets** — SEBI, RBI, SEC, EU AI Act implementation, FTC. Policy shows up here weeks before it shows up in a headline.
- **Job postings** — what a company is hiring for reveals strategy earlier than any announcement.

### Layer 2 — Cross-referencing (the actual method)
A single source reporting something is an event. **The same thing appearing in three unrelated places is a trend.** Concretely:
- If a topic surfaces in **arXiv + GitHub + a funding round** in the same week → emerging technical trend, cover it.
- If it surfaces in **regulatory filings + earnings calls + job postings** → structural industry shift, cover it.
- If it surfaces in **one outlet only** → it's a press release. Skip or treat sceptically.

### Layer 3 — Divergence hunting (where the good stories are)
The best stories live in gaps. Actively look for:
- **Consensus vs. data** — everyone says X, the numbers say Y.
- **Coverage vs. capital** — heavily covered but unfunded, or heavily funded but uncovered. The second is more interesting.
- **Domestic vs. foreign framing** — how Indian media and foreign media describe the same event differently. The gap *is* the story.
- **Expert vs. public** — practitioners quietly agree on something the general coverage hasn't caught up to.
- **Stated reason vs. revealed reason** — what a company says it's doing vs. what its hiring, filings and pricing imply.

### Layer 4 — Velocity, not volume
For any candidate story ask: **is attention accelerating or decaying?** A story on day 4 of decline is not news even if the volume is still high. Prefer things on the way up. Explicitly note when something is *fading* — that's often more interesting than the peak.

### Layer 5 — The absence check
Ask daily: **what should be in the news today and isn't?** An expected announcement that didn't come, a quarterly disclosure that got quieter, a company that stopped talking about a product. Silence is information and almost nobody covers it.

### Anti-pattern
Do **not** build the digest by visiting a list of sites and summarising the top item on each. That produces the same digest everyone else gets. Start from the question "what changed, and who noticed first?" and work backwards to sources.

---

## Sources — a starting pool, deliberately over-sized

Treat this as a menu to rotate through, not a checklist to complete. Use whichever serve today's story. Add sources freely; retire ones that go stale. **All free unless noted.**

### AI & ML
**News/analysis:** TechCrunch · The Verge · Wired · Ars Technica · MIT Technology Review · VentureBeat AI · The Information (free posts) · Artificial Intelligence News
**Newsletters:** Import AI (Jack Clark) · The Batch (Andrew Ng) · **Latent Space** (the most technically credible for people building production systems) · **Ben's Bites** · **The Rundown AI** · **AI Tidbits** · TLDR AI · Interconnects (Nathan Lambert) · AI Snake Oil (Narayanan & Kapoor — the best sceptic voice)
**Primary:** arXiv · Papers with Code · Hugging Face trending · lab blogs and model cards · GitHub Trending
**Community:** Hacker News · r/LocalLLaMA (the best early signal for open-weight models anywhere) · r/MachineLearning · X/Twitter researchers

### Building & agentic systems (his active learning thread)
**YouTube:** **Andrej Karpathy** (LLM internals from first principles — the single best free resource in existence) · **Cole Medin** (production agents businesses actually pay for) · **AI Jason** (application layer, production-ready) · LangChain official · AssemblyAI · Mervin Praison (framework comparisons) · David Ondrej · IBM Technology · **3Blue1Brown** (math intuition for transformers) · Matt Wolfe (tooling landscape) · AI Engineer (conference talks) · 100x Engineer · Y Combinator
**Docs/repos worth watching:** LangGraph · MCP · Mem0 · OpenHands · Aider · Langfuse · vLLM · CrewAI · Agno

### Business & Markets
Reuters · Bloomberg (free tier) · Financial Times (free) · CNBC · Morning Brew · TLDR · **Stratechery** (free posts — Ben Thompson) · **Net Interest** (Marc Rubinstein, financial-sector plumbing) · **The Overshoot** (Matthew Klein) · **Noahpinion** (Noah Smith) · **Money & Macro** · **Doomberg** (contrarian energy/macro) · **The Bear Cave** (investigative, short-seller lens) · **The Science of Hitting** · Slow Boring (Matt Yglesias) · Lenny's Newsletter (free posts) · Moneycontrol · ET Markets *(subscription)*

### India
Economic Times *(subscription)* · Mint · The Hindu · Indian Express · Business Standard · NDTV · **The Ken** & **The Morning Context** (free articles) · **Inc42** · **Entrackr** · YourStory · Finshots · **The Print** · Scroll · Newslaundry (media criticism — good for the framing-gap check) · MediaNama (tech policy) · Kuvera blog
**Primary:** RBI circulars · SEBI orders · PIB releases · DRHP filings

### Geopolitics & World
Reuters · AP · BBC · The Economist (free) · Foreign Affairs (free) · Foreign Policy · Al Jazeera · SCMP · Nikkei Asia · **Chartbook** (Adam Tooze) · **Sinocism** (Bill Bishop, free posts) · **ChinaTalk** (Jordan Schneider) · Geopolitical Daily · Stratfor/Worldview (free) · War on the Rocks · Lawfare
**YouTube:** **Johnny Harris** · **PolyMatter** (tech/econ/geopolitics, superb research) · **CaspianReport** · **Neo** · **Context Matters** · Zeihan on Geopolitics (provocative, verify his claims — high hit rate on framing, mixed on specifics) · TLDR News · Economics Explained

### Personal Finance & Investing
Finshots · **Zerodha Varsity** (still the best free investing education in India) · ET Wealth · Motley Fool · Investopedia · Morningstar · **r/IndiaInvestments** · **ValuePickr** (genuine Indian equity research, free) · Capitalmind (free posts) · **Akshat Shrivastava** · **CA Rachana Ranade** · Pranjal Kamra · **Nikhil Kamath — WTF is** podcast (best long-form access to Indian founders anywhere)

### Psychology, Health & Human Behaviour
**Andrew Huberman** (Huberman Lab) · **Dr. K / HealthyGamer** · **Hidden Brain** (Shankar Vedantam — the best storytelling in the category) · **The Psychology Podcast** (Scott Barry Kaufman) · **The Happiness Lab** (Laurie Santos) · Finding Mastery (Michael Gervais) · Peter Attia (The Drive) · Experimental History (Adam Mastroianni — brilliant, contrarian, free) · Astral Codex Ten (Scott Alexander) · Nature Human Behaviour / PNAS abstracts

### Explainer, culture & taste
**Chloe Abram** · **Varun Mayya** · Veritasium · Kurzgesagt · Wendover / Half as Interesting · Not Just Bikes · Vox · 99% Invisible (design) · Every.to · The Pudding (data storytelling) · Works in Progress · Damn Interesting · Atlas Obscura (travel + obscure history — feeds both the travel and rabbit-hole sections)

### Reddit — the early-signal layer

Reddit is where practitioners talk before journalists arrive. **Read comments, not just post titles** — the top dissenting reply is usually the real story. Sort by *rising* and *top-of-day* to catch acceleration; sort by *top-of-week* on Sundays for the recap.

**AI & ML**
r/LocalLLaMA *(the single best early signal for open-weight models anywhere — often days ahead of press)* · r/MachineLearning · r/singularity *(directional, high noise — treat as sentiment, not fact)* · r/OpenAI · r/ClaudeAI · r/StableDiffusion · r/LLMDevs · r/artificial

**Building & agentic systems**
r/LangChain · r/AI_Agents · r/MCP · r/LocalLLM · r/ExperiencedDevs *(best signal on what's actually being adopted vs. hyped)* · r/programming · r/devops · r/rag

**Business & Markets**
r/investing · r/stocks · r/SecurityAnalysis *(genuine deep research)* · r/finance · r/economics · r/wallstreetbets *(pure sentiment gauge — never a factual source)*

**India**
r/IndiaInvestments *(consistently the highest-quality Indian finance discussion online)* · r/india · r/IndiaSpeaks *(read alongside r/india for framing divergence — the gap between them is often the story)* · r/IndianStreetBets · r/developersIndia · r/StartUpIndia · r/IndiaBusiness · r/bangalore, r/hyderabad, r/indore *(local signal)*

**Geopolitics & World**
r/geopolitics · r/credibledefense *(heavily moderated, unusually high signal)* · r/anime_titties *(misleading name — a serious non-US-centric world news sub)* · r/NeutralPolitics · r/worldnews *(headlines only; comments are low value)*

**Personal Finance**
r/personalfinance · r/financialindependence · r/Bogleheads · r/IndiaTax · r/ValueInvesting

**Science & Frontier Tech**
r/science · r/Physics · r/space · r/biotech · r/Futurology *(sentiment, verify everything)* · r/energy

**Psychology & Health**
r/psychology · r/neuro · r/cogsci · r/AskDocs · r/ScientificNutrition *(evidence-graded, unusually rigorous)* · r/HealthyGamerGG

**Travel**
r/travel · r/solotravel · r/IndiaTravel · r/onebag · r/awardtravel *(points and miles strategy — the actual travel-hack layer)* · r/digitalnomad

**Rabbit holes & culture**
r/AskHistorians *(the gold standard for sourced historical answers)* · r/todayilearned · r/DepthHub · r/UnresolvedMysteries · r/Damnthatsinteresting · r/dataisbeautiful · r/InternetIsBeautiful · r/slatestarcodex *(high-quality contrarian analysis)*

**Career & Skills**
r/cscareerquestions · r/datascience · r/analytics · r/consulting

**Sports**
r/Cricket · r/soccer · r/formula1

**Reddit rules**
- Reddit is a **lead**, not a citation. Verify anything from Reddit against a primary or established source before it enters the digest.
- Never cite a Reddit rumour as fact. Say "being discussed on r/X" and label it as unconfirmed.
- Ignore vote counts as a truth signal. A highly-upvoted comment is popular, not correct.
- The highest-value use: **spotting what practitioners are quietly agreed on that coverage hasn't caught up to yet** (Layer 3 divergence hunting).

### Roster hygiene
- **Rotate weekly.** Don't cite the same five creators every edition.
- **Add ~1 new voice per week**, discovered via the Layer 1/2 method above — not from "best of" lists.
- **Retire anything stale.** If a source hasn't produced something worth citing in a month, drop it.
- **Global, not Anglo.** Actively pull non-Western sources when covering non-Western stories.
- Prefer **primary sources** and **practitioners** over aggregators wherever both exist.

## Feedback loop
- **Weekly check-in:** ask what landed and what to cut.
- **V2 (roadmap):** let Pulkit annotate stories with his own notes/opinions. Those notes persist and feed forward — shaping future curation and what info to surface.

## Extensibility
Always keep the door open. Pulkit can add a category, source, creator, or company at any time, and the profile should absorb it without restructuring.
