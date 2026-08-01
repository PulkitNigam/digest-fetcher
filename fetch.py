#!/usr/bin/env python3
"""Fetches all sources into data/latest.json. Runs on GitHub Actions.
HARDENED after adversarial review:
- feedparser never raises; we now fetch with requests first, check status, and
  treat bozo/empty as recorded errors instead of silent empty lists
- Alpha Vantage: 15s spacing (free tier = 5/min) and rate-limit notes logged
- staleness contract: consumer must reject data older than 26h (generated_utc)
"""
import os, json, time, datetime, requests, feedparser
import sources as S

UA = {"User-Agent": "Mozilla/5.0 (digest-fetcher/2.0; personal news digest)"}
OUT = {"generated_utc": datetime.datetime.utcnow().isoformat() + "Z",
       "youtube": {}, "rss": {}, "reddit": {}, "hackernews": [],
       "github": [], "quotes": {}, "fx": {}, "errors": []}
def err(w, m): OUT["errors"].append({"source": w, "error": str(m)[:300]})
def get(url, **kw): return requests.get(url, headers=UA, timeout=25, **kw)

def feed(url):
    """Fetch a feed properly: HTTP errors and empty/bozo results are ERRORS, not silence."""
    r = get(url); r.raise_for_status()
    f = feedparser.parse(r.content)
    if f.bozo and not f.entries:
        raise ValueError(f"unparseable feed: {f.bozo_exception}")
    if not f.entries:
        raise ValueError("feed parsed but zero entries")
    return f

for cid, label in S.YOUTUBE.items():
    try:
        f = feed(f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}")
        OUT["youtube"][label] = [{"title": e.title, "url": e.link,
            "published": e.get("published", "")} for e in f.entries[:5]]
    except Exception as e: err(f"youtube:{label}", e)

for label, url in S.RSS.items():
    try:
        f = feed(url)
        OUT["rss"][label] = {
            "updated": f.feed.get("updated", f.feed.get("lastbuilddate", "")),
            "items": [{"title": e.get("title",""), "summary": (e.get("summary","") or "")[:400],
                       "url": e.get("link",""), "published": e.get("published", e.get("updated",""))}
                      for e in f.entries[:12]]}
    except Exception as e: err(f"rss:{label}", e)

# Reddit: datacenter IPs are often blocked; try old.reddit fallback, record both failures
for sub, sort in S.REDDIT.items():
    got = False
    for host in ("www", "old"):
        try:
            r = get(f"https://{host}.reddit.com/r/{sub}/{sort}.json", params={"t":"day","limit":10})
            r.raise_for_status()
            posts = r.json()["data"]["children"]
            OUT["reddit"][sub] = [{"title": p["data"]["title"], "score": p["data"]["score"],
                "comments": p["data"]["num_comments"],
                "url": "https://reddit.com"+p["data"]["permalink"]} for p in posts]
            got = True; break
        except Exception as e: last = e
    if not got: err(f"reddit:{sub}", f"{last} (datacenter-IP block likely; fix=OAuth script app)")

try:
    ids = get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:25]
    for i in ids:
        d = get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json").json()
        if not d: continue
        sc, nc = d.get("score",0), d.get("descendants",0)
        OUT["hackernews"].append({"title": d.get("title"), "url": d.get("url"),
            "score": sc, "comments": nc,
            "hn_url": f"https://news.ycombinator.com/item?id={i}",
            "controversy": round(nc/sc,2) if sc else 0})
except Exception as e: err("hackernews", e)

try:
    since = (datetime.date.today()-datetime.timedelta(days=S.GITHUB_DAYS)).isoformat()
    r = get("https://api.github.com/search/repositories",
            params={"q": f"created:>{since} stars:>300","sort":"stars","order":"desc","per_page":20})
    r.raise_for_status()
    for x in r.json().get("items", []):
        OUT["github"].append({"name": x["full_name"], "desc": x.get("description"),
            "stars": x["stargazers_count"], "created": x["created_at"],
            "lang": x.get("language"), "url": x["html_url"]})
except Exception as e: err("github", e)

try:
    r = get("https://api.frankfurter.app/latest", params={"from":"USD","to":"INR"})
    r.raise_for_status(); OUT["fx"] = r.json()
except Exception as e: err("fx", e)

key = os.environ.get("ALPHAVANTAGE_KEY","").strip()
if key:
    for n, sym in enumerate(S.QUOTES):
        if n: time.sleep(15)                     # free tier: 5 calls/min — never burst
        try:
            j = get("https://www.alphavantage.co/query",
                    params={"function":"GLOBAL_QUOTE","symbol":sym,"apikey":key}).json()
            if "Note" in j or "Information" in j:
                err(f"quote:{sym}", j.get("Note") or j.get("Information")); continue
            q = j.get("Global Quote", {})
            if q: OUT["quotes"][sym] = {"price": q.get("05. price"),
                "change_pct": q.get("10. change percent"), "day": q.get("07. latest trading day")}
            else: err(f"quote:{sym}", "empty Global Quote")
        except Exception as e: err(f"quote:{sym}", e)
else:
    err("quotes", "ALPHAVANTAGE_KEY not set — skipped")

os.makedirs("data", exist_ok=True)
for name in ("latest.json", f"{datetime.date.today().isoformat()}.json"):
    with open(f"data/{name}", "w", encoding="utf-8") as fh:
        json.dump(OUT, fh, indent=1, ensure_ascii=False)

# summary.json — tiny manifest the consumer fetches FIRST (staleness check +
# full error list + headline index), immune to size-limit truncation
SUM = {"generated_utc": OUT["generated_utc"],
  "counts": {"youtube": len(OUT["youtube"]), "rss": len(OUT["rss"]),
             "reddit": len(OUT["reddit"]), "hackernews": len(OUT["hackernews"]),
             "github": len(OUT["github"]), "quotes": len(OUT["quotes"])},
  "fx": OUT["fx"].get("rates", {}),
  "alive_rss": sorted(OUT["rss"].keys()),
  "alive_reddit": sorted(OUT["reddit"].keys()),
  "headlines": {k: [i["title"] for i in v["items"][:6]] for k, v in OUT["rss"].items()},
  "youtube_latest": {k: (v[0]["title"] if v else None) for k, v in OUT["youtube"].items()},
  "hn_top": [{"t": h["title"], "s": h["score"], "c": h["controversy"]} for h in OUT["hackernews"][:15]],
  "github_top": [{"n": g["name"], "s": g["stars"]} for g in OUT["github"][:10]],
  "quotes": OUT["quotes"],
  "errors": OUT["errors"]}
with open("data/summary.json", "w", encoding="utf-8") as fh:
    json.dump(SUM, fh, indent=1, ensure_ascii=False)
open("data/.keepalive","w").write(OUT["generated_utc"])   # prevents 60-day workflow auto-disable

ok = sum(len(v) if isinstance(v,(list,dict)) else 0 for k,v in OUT.items() if k not in("errors","generated_utc"))
print(f"sections ok≈{ok} | errors {len(OUT['errors'])}")
for e in OUT["errors"][:20]: print("  ERR", e["source"], "→", e["error"][:80])
