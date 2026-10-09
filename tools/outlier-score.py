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

Metric parsing (same rule as content/lead-magnets/outlier-to-template-intake/index.html):
  "12,400" -> 12400, "12.4K" -> 12400, "1.2M" -> 1200000, "1.2" -> 1.2 ("." is a decimal point,
  "," a thousands separator). A value that does not parse is skipped from the median and printed.

Usage: python3 tools/outlier-score.py content-log/intake/YYYY-MM-DD.csv
       python3 tools/outlier-score.py --test      (self-test of the number parsing)
Prints the outliers first, then writes <input>-scored.csv next to it."""
import csv, statistics, sys, collections, pathlib, re
FLOOR = {"x": 50000, "linkedin": 300}


def num(v):
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([kKmM]?)", str(v if v is not None else "").replace(",", "").replace(" ", ""))
    if not m:
        return None
    x = float(m[1]) * {"": 1, "k": 1e3, "m": 1e6}[m[2].lower()]
    return int(x) if x == int(x) else x


if sys.argv[1:] == ["--test"]:
    cases = {"12.4K": 12400, "1.2": 1.2, "12,400": 12400, "1.2M": 1200000, "850": 850, "3k": 3000, " 12 400 ": 12400, "abc": None, "": None}
    bad = [(k, num(k), v) for k, v in cases.items() if num(k) != v]
    print("FAIL", bad) if bad else print(f"ok: {len(cases)} cases")
    sys.exit(1 if bad else 0)
src = pathlib.Path(sys.argv[1]); rows = list(csv.DictReader(src.open(encoding="utf-8")))
by = collections.defaultdict(list)
for r in rows:
    raw, r["metric"] = r["metric"], num(r["metric"])
    if r["metric"] is None:
        print(f"SKIPPED (metric {raw!r} does not parse): @{r['handle']} {r.get('link', '')}"); continue
    by[r["handle"]].append(r)
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
