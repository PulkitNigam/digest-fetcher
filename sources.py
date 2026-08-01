"""Every source the digest wants. Edit freely — the fetcher reads this."""

# ---------- YouTube: channel_id -> label.  Find IDs at commentpicker.com/youtube-channel-id.php
YOUTUBE = {
    "UCHnyfMqiRRG1u-2MsSQLbXA": "Veritasium",
    "UCbfYPyITQ-7l4upoX8nvctg": "Two Minute Papers",
    "UCXUPKJO5MZQN11PqgIvyuvQ": "Andrej Karpathy",
    "UCsBjURrPoezykLs9EqgamOA": "Fireship",
    "UCupvZG-5ko_eiXAupbDfxWw": "CNN",           # replace with your picks
    # --- add yours: Varun Mayya, Johnny Harris, Huberman, Dr K, Cole Medin,
    #     PolyMatter, CaspianReport, Akshat Shrivastava, Nikhil Kamath, Chloe Abram
}

# ---------- RSS: anything. Podcasts, Substack, blogs, news. gzip is fine here.
RSS = {
    # News
    "BBC World":        "https://feeds.bbci.co.uk/news/world/rss.xml",
    "BBC Business":     "https://feeds.bbci.co.uk/news/business/rss.xml",
    "BBC Technology":   "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "Al Jazeera":       "https://www.aljazeera.com/xml/rss/all.xml",
    "The Guardian":     "https://www.theguardian.com/world/rss",
    "NPR":              "https://feeds.npr.org/1001/rss.xml",
    "AP Top":           "https://rsshub.app/apnews/topics/apf-topnews",
    "SCMP China":       "https://www.scmp.com/rss/4/feed",
    "Nikkei Asia":      "https://asia.nikkei.com/rss/feed/nar",
    "Deutsche Welle":   "https://rss.dw.com/rdf/rss-en-world",
    "The Print":        "https://theprint.in/feed/",
    # India
    "Livemint":         "https://www.livemint.com/rss/markets",
    "The Hindu Biz":    "https://www.thehindu.com/business/feeder/default.rss",
    "Indian Express":   "https://indianexpress.com/section/business/feed/",
    "Business Standard":"https://www.business-standard.com/rss/markets-106.rss",
    "Inc42":            "https://inc42.com/feed/",
    "Entrackr":         "https://entrackr.com/feed/",
    "MediaNama":        "https://www.medianama.com/feed/",
    "Moneycontrol":     "https://www.moneycontrol.com/rss/business.xml",
    # Tech / AI
    "TechCrunch":       "https://techcrunch.com/feed/",
    "Ars Technica":     "https://feeds.arstechnica.com/arstechnica/index",
    "The Verge":        "https://www.theverge.com/rss/index.xml",
    "MIT Tech Review":  "https://www.technologyreview.com/feed/",
    "Hacker News best": "https://hnrss.org/best",
    "Simon Willison":   "https://simonwillison.net/atom/everything/",
    "Import AI":        "https://importai.substack.com/feed",
    "Latent Space":     "https://www.latent.space/feed",
    "Interconnects":    "https://www.interconnects.ai/feed",
    "AI Snake Oil":     "https://www.aisnakeoil.com/feed",
    # Markets / macro
    "Stratechery":      "https://stratechery.com/feed/",
    "Noahpinion":       "https://www.noahpinion.blog/feed",
    "Chartbook":        "https://adamtooze.substack.com/feed",
    "Net Interest":     "https://www.netinterest.co/feed",
    "Money & Macro":    "https://www.moneymacro.rocks/feed",
    # Podcasts
    "Huberman Lab":     "https://feeds.megaphone.fm/hubermanlab",
    "ChinaTalk":        "https://www.chinatalk.media/feed",
    # Science
    "ScienceDaily":     "https://www.sciencedaily.com/rss/top/science.xml",
    "Nature":           "https://www.nature.com/nature.rss",
}

# ---------- Reddit: sub -> sort. Actually reachable from Actions.
REDDIT = {
    "LocalLLaMA": "top", "MachineLearning": "top", "AI_Agents": "top",
    "IndiaInvestments": "top", "india": "top", "IndianStreetBets": "top",
    "investing": "top", "geopolitics": "top", "credibledefense": "top",
    "ExperiencedDevs": "top", "AskHistorians": "top", "hyderabad": "new",
    "indore": "new", "developersIndia": "top", "ValueInvesting": "top",
}

# ---------- Alpha Vantage quotes (needs ALPHAVANTAGE_KEY). Keep small: 25 calls/day.
QUOTES = ["NVDA", "GOOGL", "META", "MSFT", "SMH", "AAPL"]

# ---------- GitHub trending window (days)
GITHUB_DAYS = 21
