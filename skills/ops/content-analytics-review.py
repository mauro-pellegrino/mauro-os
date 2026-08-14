# -*- coding: utf-8 -*-
"""
Content Analytics Review — monthly reach/distribution report for @maurojpelle.

Ingests an X (Twitter) account analytics content export and prints a report the
content-analytics-review skill turns into recommendations. Reach-first: the goal
is impressions + follows, so the script surfaces distribution levers, not vanity.

Usage:
    python content-analytics-review.py "<path-to-export.csv>" [--prev "<prior-month.csv>"]

The CSV must have X's standard content-export columns:
    Post id, Date, Post text, Post Link, Impressions, Likes, Engagements,
    Bookmarks, Shares, New follows, Replies, Reposts, Profile visits,
    Detail Expands, URL Clicks, Hashtag Clicks, Permalink Clicks
"""
import csv, sys, re, statistics
from collections import defaultdict

NUM_COLS = ["Impressions","Likes","Engagements","Bookmarks","Shares",
            "New follows","Replies","Reposts","Profile visits","Detail Expands","URL Clicks"]

def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            for k in NUM_COLS:
                try: r[k] = int(r[k])
                except: r[k] = 0
            r["_text"] = (r.get("Post text","") or "").strip()
            r["_wc"] = len(r["_text"].split())
            r["_fmt"] = fmt(r)
            r["_mentions"] = re.findall(r"@(\w+)", r["_text"])
            rows.append(r)
    return rows

def fmt(r):
    t = r["_text"] if "_text" in r else (r.get("Post text","") or "").strip()
    if t.startswith("@"): return "reply"
    if "http" in t or r["URL Clicks"] > 0: return "link/media"
    if len(t.split()) >= 45: return "longform"
    return "short original"

def med(xs): return statistics.median(xs) if xs else 0

def totals(rows):
    return {
        "posts": len(rows),
        "imp": sum(r["Impressions"] for r in rows),
        "fol": sum(r["New follows"] for r in rows),
        "eng": sum(r["Engagements"] for r in rows),
        "bkm": sum(r["Bookmarks"] for r in rows),
        "pv":  sum(r["Profile visits"] for r in rows),
    }

def report(rows, prev=None):
    t = totals(rows)
    n = t["posts"]
    print("="*70)
    print("CONTENT ANALYTICS REVIEW  —  reach & distribution")
    print("="*70)
    print(f"Posts: {n}   Impressions: {t['imp']:,}   New follows: {t['fol']}   "
          f"Bookmarks: {t['bkm']}   Profile visits: {t['pv']}")
    print(f"Median impressions/post: {med([r['Impressions'] for r in rows]):.0f}   "
          f"Mean: {t['imp']/n:.0f}" if n else "")
    if prev:
        pt = totals(prev)
        def delta(a,b):
            return f"{(a-b):+,} ({((a-b)/b*100):+.0f}%)" if b else f"{a:+,} (n/a)"
        print("\n-- vs prior period --")
        print(f"  Impressions: {delta(t['imp'], pt['imp'])}")
        print(f"  New follows: {delta(t['fol'], pt['fol'])}")
        print(f"  Bookmarks:   {delta(t['bkm'], pt['bkm'])}")
        print(f"  Median imp:  {med([r['Impressions'] for r in rows]):.0f} vs {med([r['Impressions'] for r in prev]):.0f}")

    # FORMAT
    print("\n=== FORMAT (what to post more of) ===")
    byf = defaultdict(list)
    for r in rows: byf[r["_fmt"]].append(r)
    print(f"{'format':16}{'#':>5}{'imp share':>11}{'med imp':>9}{'mean imp':>10}{'follows':>9}{'bkm':>6}")
    for k,v in sorted(byf.items(), key=lambda x:-(sum(p['Impressions'] for p in x[1])/max(len(x[1]),1))):
        imp = sum(p['Impressions'] for p in v); fol = sum(p['New follows'] for p in v)
        bkm = sum(p['Bookmarks'] for p in v)
        share = imp/t['imp']*100 if t['imp'] else 0
        print(f"{k:16}{len(v):>5}{share:>10.1f}%{med([p['Impressions'] for p in v]):>9.0f}"
              f"{imp/len(v):>10.0f}{fol:>9}{bkm:>6}")

    # DISTRIBUTION: which accounts you reply to actually reach
    print("\n=== DISTRIBUTION: reply reach by account (top 12 by total imp) ===")
    acc = defaultdict(lambda: {"n":0,"imp":0,"fol":0})
    for r in rows:
        if r["_fmt"]=="reply" and r["_mentions"]:
            a = r["_mentions"][0]
            acc[a]["n"]+=1; acc[a]["imp"]+=r["Impressions"]; acc[a]["fol"]+=r["New follows"]
    for a,d in sorted(acc.items(), key=lambda x:-x[1]["imp"])[:12]:
        print(f"  @{a:20} replies:{d['n']:>3}  imp:{d['imp']:>6}  avg:{d['imp']/d['n']:>6.0f}  fol:{d['fol']:>3}")

    # TOP POSTS (reach)
    print("\n=== TOP 12 POSTS BY IMPRESSIONS ===")
    for r in sorted(rows, key=lambda r:-r["Impressions"])[:12]:
        print(f"  {r['Impressions']:>6} imp | {r['New follows']:>2} fol | {r['Bookmarks']:>2} bkm | "
              f"{r['_fmt']:14} | {r['_text'][:70].replace(chr(10),' ')}")

    # FOLLOW DRIVERS
    print("\n=== POSTS THAT DROVE FOLLOWS ===")
    for r in sorted([r for r in rows if r["New follows"]>0], key=lambda r:-r["New follows"]):
        print(f"  {r['New follows']:>2} fol | {r['Impressions']:>6} imp | {r['_fmt']:14} | "
              f"{r['_text'][:70].replace(chr(10),' ')}")

    # VALUE (bookmarks = save-worthy, the raw material to redistribute)
    print("\n=== SAVE-WORTHY (top bookmarks — redistribute these) ===")
    for r in sorted([r for r in rows if r["Bookmarks"]>0], key=lambda r:-r["Bookmarks"])[:10]:
        print(f"  {r['Bookmarks']:>2} bkm | {r['Impressions']:>6} imp | {r['_fmt']:14} | "
              f"{r['_text'][:70].replace(chr(10),' ')}")

    # LENGTH (original only)
    print("\n=== IMPRESSIONS BY LENGTH (original posts only) ===")
    orig = [r for r in rows if r["_fmt"]!="reply"]
    for lo,hi in [(0,15),(15,30),(30,60),(60,120),(120,99999)]:
        b=[r for r in orig if lo<=r["_wc"]<hi]
        if b:
            print(f"  {lo:>3}-{hi if hi<99999 else '+':>4} words | n={len(b):>3} | "
                  f"med {med([r['Impressions'] for r in b]):>5.0f} | mean {sum(r['Impressions'] for r in b)/len(b):>6.0f}")
    print("\nNOTE: any bucket / account with n<3 is directional only, not a trend.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    path = sys.argv[1]
    prev = None
    if "--prev" in sys.argv:
        prev = load(sys.argv[sys.argv.index("--prev")+1])
    report(load(path), prev)
