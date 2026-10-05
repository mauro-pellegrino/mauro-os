#!/usr/bin/env python3
"""Find prospects: a strong YouTube channel with an offer, and a weak or missing X / LinkedIn.

Usage:
  YOUTUBE_API_KEY=... python3 tools/yt-prospects.py               # default search terms
  YOUTUBE_API_KEY=... python3 tools/yt-prospects.py "google ads" "ai for ecom"

Writes research/yt-prospects/YYYY-MM-DD.csv, ranked. Quota: about 100 units per search
term plus ~3 per channel, well inside the 10K daily default.

The rules (same outlier rule as tools/outlier-score.py):
  - channel size 2K to 100K subscribers
  - outlier = best of the last 20 uploads / median of the last 20; 3x+ passes
  - offer = a booking, application, course or community link in the channel or video
    descriptions
  - social gap = no X link and no LinkedIn link found. A linked X still needs a manual
    check of followers and last post date; the API cannot see X.
"""
import csv, datetime, json, os, re, statistics, sys, urllib.parse, urllib.request

TERMS = [
    "google ads agency", "google ads for ecommerce", "performance max ecommerce",
    "AI for ecommerce", "AI ads ecommerce", "meta ads agency", "facebook ads ecommerce",
    "ecom creative strategy", "shopify ads strategy", "ugc ads agency",
]
SUBS_MIN, SUBS_MAX, LAST_N = 2_000, 100_000, 20

OFFER_RE = re.compile(
    r"(calendly\.com|cal\.com|typeform\.com|tidycal\.com|savvycal\.com|hubspot\.com/meetings|"
    r"leadconnectorhq|skool\.com|stan\.store|whop\.com|gumroad\.com|kajabi|teachable|"
    r"book (a|your) (free )?(call|consult|strategy)|apply (here|now)|work with (me|us))", re.I)
X_RE = re.compile(r"(?:twitter\.com|x\.com)/(?!intent|share|home|search|hashtag)([A-Za-z0-9_]{2,15})", re.I)
LI_RE = re.compile(r"linkedin\.com/(in|company)/([A-Za-z0-9_\-%]+)", re.I)

KEY = os.environ.get("YOUTUBE_API_KEY")
API = "https://www.googleapis.com/youtube/v3/"


def get(endpoint, **params):
    params["key"] = KEY
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def chunks(xs, n=50):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def main():
    if not KEY:
        sys.exit("Set YOUTUBE_API_KEY first.")
    terms = sys.argv[1:] or TERMS
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ")

    found = {}  # channel_id -> search term that found it
    for t in terms:
        res = get("search", part="snippet", q=t, type="video", maxResults=50,
                  relevanceLanguage="en", publishedAfter=since)
        for it in res.get("items", []):
            found.setdefault(it["snippet"]["channelId"], t)
    print(f"{len(found)} channels from {len(terms)} terms", file=sys.stderr)

    channels = []
    for batch in chunks(list(found)):
        res = get("channels", part="snippet,statistics,contentDetails", id=",".join(batch))
        for c in res.get("items", []):
            subs = int(c["statistics"].get("subscriberCount", 0))
            if SUBS_MIN <= subs <= SUBS_MAX:
                channels.append(c)
    print(f"{len(channels)} in the {SUBS_MIN}-{SUBS_MAX} subscriber band", file=sys.stderr)

    rows = []
    for c in channels:
        uploads = c["contentDetails"]["relatedPlaylists"]["uploads"]
        try:
            pl = get("playlistItems", part="contentDetails", playlistId=uploads, maxResults=LAST_N)
        except Exception:
            continue
        vids = [i["contentDetails"]["videoId"] for i in pl.get("items", [])]
        if len(vids) < 5:
            continue
        vres = get("videos", part="snippet,statistics", id=",".join(vids))["items"]
        views = [int(v["statistics"].get("viewCount", 0)) for v in vres]
        med = statistics.median(views) or 1
        best = max(vres, key=lambda v: int(v["statistics"].get("viewCount", 0)))
        best_views = int(best["statistics"].get("viewCount", 0))
        ratio = best_views / med

        text = c["snippet"].get("description", "") + "\n" + "\n".join(
            v["snippet"].get("description", "") for v in vres)
        offers = sorted({m.group(0).lower() for m in OFFER_RE.finditer(text)})
        xs = sorted({h.lower() for h in X_RE.findall(text)})
        lis = sorted({"/".join(m) for m in LI_RE.findall(text)})
        gap = "none linked" if not xs and not lis else ("X only" if xs and not lis else
               "LinkedIn only" if lis and not xs else "both linked")

        score = min(ratio, 10) * (2 if offers else 0.5) * {"none linked": 2, "LinkedIn only": 1.5,
                                                           "X only": 1.2, "both linked": 1}[gap]
        rows.append({
            "score": round(score, 1),
            "channel": c["snippet"]["title"],
            "url": f"https://www.youtube.com/channel/{c['id']}",
            "subs": c["statistics"].get("subscriberCount"),
            "median_views": int(med),
            "best_views": best_views,
            "outlier_x": round(ratio, 1),
            "best_video": best["snippet"]["title"],
            "best_video_url": f"https://www.youtube.com/watch?v={best['id']}",
            "offer_links": "; ".join(offers),
            "x_handles": "; ".join(xs),
            "linkedin": "; ".join(lis),
            "social_gap": gap,
            "found_by": found[c["id"]],
            "x_followers_manual": "",
            "x_last_post_manual": "",
        })

    rows.sort(key=lambda r: -r["score"])
    out_dir = os.path.join(os.path.dirname(__file__), "..", "research", "yt-prospects")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.abspath(os.path.join(out_dir, f"{datetime.date.today()}.csv"))
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["score"])
        w.writeheader()
        w.writerows(rows)
    passing = [r for r in rows if r["outlier_x"] >= 3 and r["offer_links"]]
    print(f"{len(rows)} scored, {len(passing)} pass outlier 3x + offer. Wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
