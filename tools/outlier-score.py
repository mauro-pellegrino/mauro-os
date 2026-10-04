#!/usr/bin/env python3
"""Template intake: score other accounts' posts against THEIR OWN median, so only real outliers
get captured as templates. Skill: skills/research/template-intake.md.

Input: a CSV filled while scrolling a tracked profile (research/tracked-profiles.csv). One row per
post, the newest 10-20 posts of each account. Columns:  handle,platform,date,metric,link,first_words
  platform = x or linkedin (lowercase)
  metric   = impressions (X) or comments (LinkedIn), exactly as shown on the post

Rule: outlier = metric / that handle's median over its last 10-20 posts.
  >= 3x  OUTLIER     >= 10x STRONG
  floor: X 50,000 impressions, LinkedIn 300 comments. Under the floor it is not worth a template.
  An account with fewer than 5 posts in the file gets no score ("need 5+ posts").

Usage: python3 tools/outlier-score.py content-log/intake/YYYY-MM-DD.csv
Prints the outliers first, then writes <input>-scored.csv next to it."""
import csv, statistics, sys, collections, pathlib
FLOOR = {"x": 50000, "linkedin": 300}
src = pathlib.Path(sys.argv[1]); rows = list(csv.DictReader(src.open(encoding="utf-8")))
by = collections.defaultdict(list)
for r in rows:
    r["metric"] = int(str(r["metric"]).replace(",", "").replace(".", "") or 0); by[r["handle"]].append(r)
out = []
for h, rs in by.items():
    med = statistics.median(r["metric"] for r in rs) if len(rs) >= 5 else None
    for r in rs:
        ratio = round(r["metric"] / med, 2) if med else None
        floor_ok = r["metric"] >= FLOOR.get(r["platform"].lower(), 0)
        verdict = ("STRONG" if ratio and ratio >= 10 else "OUTLIER" if ratio and ratio >= 3 else "normal") if med else "need 5+ posts"
        if verdict in ("STRONG", "OUTLIER") and not floor_ok: verdict += " (under floor)"
        out.append({**r, "median": med, "ratio": ratio, "verdict": verdict})
out.sort(key=lambda r: -(r["ratio"] or 0))
for r in out:
    if r["verdict"].startswith(("STRONG", "OUTLIER")):
        print(f'{r["verdict"]:24} {r["ratio"]:>6}x  @{r["handle"]:16} {r["metric"]:>9,}  {r["link"]}  {r.get("first_words","")[:50]}')
dst = src.with_name(src.stem + "-scored.csv")
with dst.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print(f"\n{len(out)} posts, {len(by)} accounts -> {dst}")
