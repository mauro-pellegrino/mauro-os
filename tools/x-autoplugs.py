#!/usr/bin/env python3
"""Lorenzo's auto-plugs (the self-reply under each post that links the portfolio / bio): reach,
URL clicks, profile visits and follows per month, plus the most-used plug texts.

    python3 tools/x-autoplugs.py [Lorenzo|Bogdan]
"""
import collections, contextlib, io, re, runpy, statistics, sys
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(__file__.replace("x-autoplugs.py", "x-keywords.py"), run_name="lib")
rows, n, is_plug = ns["rows"], ns["n"], ns["is_plug"]  # one plug rule, shared with x-keyword-tracker.py
acc = (sys.argv[1:] or ["Lorenzo"])[0]
by = collections.defaultdict(list)
for r in rows.values():
    if r["acc"] == acc and r["kind"] != "reply" and is_plug(r["Post text"]) and r["day"].strftime("%Y-%m") >= "2026-05":
        by[r["day"].strftime("%Y-%m")].append(r)
print("month   plugs  impressions  median  url_clicks  clicks/plug  visits  follows")
for m in sorted(by):
    x = by[m]
    c = sum(n(r, "URL Clicks") for r in x)
    print(f"{m}  {len(x):5} {sum(n(r,'Impressions') for r in x):12,} {int(statistics.median([n(r,'Impressions') for r in x])):7} "
          f"{c:10} {c/len(x):11.1f} {sum(n(r,'Profile visits') for r in x):7} {sum(n(r,'New follows') for r in x):8}")
for t, c in collections.Counter(re.sub(r"https?://\S+", "<url>", r["Post text"]).strip()[:100] for v in by.values() for r in v).most_common(5):
    print(c, "|", t.replace("\n", " / "))
