#!/usr/bin/env python3
"""Audience baseline for @maurojpelle from an X content export.

Usage: python3 tools/maurojpelle-baseline.py research/x-analytics/<export>.csv

Replies = post text starting with @. Long form = original post over 280 characters.
Prints per-month totals for original posts, follows and profile visits across all rows,
and the top 8 original posts.
"""
import collections
import csv
import datetime as dt
import statistics
import sys

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))


def num(r, k):
    try:
        return int(float(r.get(k) or 0))
    except ValueError:
        return 0


for r in rows:
    r["day"] = dt.datetime.strptime(r["Date"].strip(), "%a, %b %d, %Y").date()
    text = (r.get("Post text") or "").strip()
    r["kind"] = "reply" if text.startswith("@") else ("long form" if len(text) > 280 else "short")

days = sorted(r["day"] for r in rows)
print(f"{len(rows)} rows, {days[0]} to {days[-1]}")

orig = [r for r in rows if r["kind"] != "reply"]
print(f"original posts {len(orig)}, replies {len(rows) - len(orig)}")
print(f"follows (all rows) {sum(num(r, 'New follows') for r in rows)}, "
      f"profile visits (all rows) {sum(num(r, 'Profile visits') for r in rows)}")

by_month = collections.defaultdict(list)
for r in rows:
    by_month[r["day"].strftime("%Y-%m")].append(r)
print("\nmonth    orig  impr(orig)  median  follows  visits")
for m in sorted(by_month):
    rs = by_month[m]
    o = [r for r in rs if r["kind"] != "reply"]
    imps = [num(r, "Impressions") for r in o]
    print(f"{m}  {len(o):5} {sum(imps):11,} {int(statistics.median(imps)) if imps else 0:7} "
          f"{sum(num(r, 'New follows') for r in rs):8} {sum(num(r, 'Profile visits') for r in rs):7}")

kinds = collections.defaultdict(list)
for r in orig:
    kinds[r["kind"]].append(num(r, "Impressions"))
print("\nkind       posts  median  mean")
for k, v in kinds.items():
    print(f"{k:10} {len(v):5} {int(statistics.median(v)):7} {int(statistics.mean(v)):5}")

print("\ntop 8 original posts")
for r in sorted(orig, key=lambda r: -num(r, "Impressions"))[:8]:
    t = (r.get("Post text") or "").replace("\n", " ")[:70]
    print(f"{r['day']}  {num(r, 'Impressions'):6,} imp  {num(r, 'New follows'):3} fol  {num(r, 'Profile visits'):4} vis  {t}")
