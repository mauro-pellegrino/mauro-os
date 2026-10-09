#!/usr/bin/env python3
"""Traffic baseline for @maurojpelle from the X content exports (built 2026-10-08 for the plan page).

Usage:
    python3 tools/maurojpelle-traffic.py research/x-analytics/maurojpelle-2026-05-25-to-2026-08-22.csv \
        research/x-analytics/maurojpelle-2026-07-08-to-2026-10-05.csv

Rows are deduped on Post id; when a post is in two exports, the later file wins (its counts are newer).
Note: the file named 2026-07-08-to-2026-10-05 only holds rows from 2026-08-17 on.

Format classes, from the post text only (the export has no media or quote flag, and it truncates text):
  reply      text starts with @
  bare link  text is only a t.co link (an article drop or a media-only post, the export cannot tell)
  bullets    text holds a "- " list
  plain      everything else
Impressions are summed for original posts (all but replies). Follows and profile visits are summed
for all rows, because a reply can earn a follow too.
"""
import collections
import csv
import datetime as dt
import re
import statistics
import sys

rows = {}
for path in sys.argv[1:]:
    for r in csv.DictReader(open(path, encoding="utf-8")):
        rows[r["Post id"]] = r
rows = list(rows.values())


def num(r, k):
    try:
        return int(float(r.get(k) or 0))
    except ValueError:
        return 0


for r in rows:
    r["day"] = dt.datetime.strptime(r["Date"].strip(), "%a, %b %d, %Y").date()
    t = (r.get("Post text") or "").strip()
    if t.startswith("@"):
        r["fmt"] = "reply"
    elif re.fullmatch(r"https://t\.co/\S+", t):
        r["fmt"] = "bare link"
    elif re.search(r"(^|\s)- \S", t):
        r["fmt"] = "bullets"
    else:
        r["fmt"] = "plain"

days = sorted(r["day"] for r in rows)
print(f"{len(rows)} unique rows, {days[0]} to {days[-1]}")
print(f"follows {sum(num(r, 'New follows') for r in rows)}, profile visits {sum(num(r, 'Profile visits') for r in rows)}")

print("\nmonth    first..last day   orig  replies  impr(orig)  impr(all)  median  follows  visits")
bm = collections.defaultdict(list)
for r in rows:
    bm[r["day"].strftime("%Y-%m")].append(r)
for m in sorted(bm):
    rs = bm[m]
    o = [r for r in rs if r["fmt"] != "reply"]
    imps = [num(r, "Impressions") for r in o]
    d = sorted(r["day"] for r in rs)
    print(f"{m}  {d[0].day:2}..{d[-1].day:2}          {len(o):5} {len(rs) - len(o):8} {sum(imps):11,} {sum(num(r, 'Impressions') for r in rs):10,} "
          f"{int(statistics.median(imps)) if imps else 0:7} {sum(num(r, 'New follows') for r in rs):8} "
          f"{sum(num(r, 'Profile visits') for r in rs):7}")

print("\nformat     posts  impr   median  follows  visits  follows/1k impr")
bf = collections.defaultdict(list)
for r in rows:
    bf[r["fmt"]].append(r)
for f, rs in sorted(bf.items(), key=lambda kv: -sum(num(r, "New follows") for r in kv[1])):
    imps = [num(r, "Impressions") for r in rs]
    fol = sum(num(r, "New follows") for r in rs)
    print(f"{f:10} {len(rs):5} {sum(imps):6,} {int(statistics.median(imps)):6} {fol:8} "
          f"{sum(num(r, 'Profile visits') for r in rs):7}  {fol / max(sum(imps), 1) * 1000:.2f}")

print("\nposts that earned a follow")
for r in sorted([r for r in rows if num(r, "New follows")], key=lambda r: r["day"]):
    t = (r.get("Post text") or "").replace("\n", " ")[:70]
    print(f"{r['day']}  {r['fmt']:9} {num(r, 'New follows')} fol {num(r, 'Impressions'):6,} imp  {t}")

print("\ntop 8 original posts by impressions")
for r in sorted([r for r in rows if r["fmt"] != "reply"], key=lambda r: -num(r, "Impressions"))[:8]:
    t = (r.get("Post text") or "").replace("\n", " ")[:70]
    print(f"{r['day']}  {r['fmt']:9} {num(r, 'Impressions'):6,} imp {num(r, 'New follows')} fol "
          f"{num(r, 'Profile visits'):3} vis  {t}")
