#!/usr/bin/env python3
"""Do weekly X follows (Lorenzo + Bogdan) move with weekly qualified content calls?

Calls: growthub-os/research/q1-q2-content-vs-calls/weekly-dataset.json (weekly_qualcalls, by booking week).
Follows: every X export on the Mac (x-three-accounts.py loader). Spearman, same week and 1-week lag.

    python3 tools/x-follows-vs-calls.py
"""
import ast, collections, contextlib, io, json, os, runpy
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(__file__.replace("x-follows-vs-calls.py", "x-three-accounts.py"), run_name="lib")
rows, n = ns["rows"], ns["n"]
d = json.load(open(os.path.expanduser("~/growthub-os/research/q1-q2-content-vs-calls/weekly-dataset.json")))
calls = d["weekly_qualcalls"]
calls = ast.literal_eval(calls) if isinstance(calls, str) else calls
fol, imp = collections.Counter(), collections.Counter()
for r in rows.values():
    if r["acc"] in ("Lorenzo", "Bogdan"):
        y, w, _ = r["day"].isocalendar()
        k = f"{y}-W{w:02d}"
        fol[k] += n(r, "New follows"); imp[k] += n(r, "Impressions")


def rank(v):
    s = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
    for pos, i in enumerate(s): r[i] = pos
    return r


def spearman(a, b):
    ra, rb = rank(a), rank(b); m = len(a)
    ma, mb = sum(ra) / m, sum(rb) / m
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = sum((x - ma) ** 2 for x in ra) ** .5; vb = sum((y - mb) ** 2 for y in rb) ** .5
    return cov / (va * vb) if va and vb else float("nan")


weeks = sorted(k for k in calls if k in fol and fol[k] > 0)
print("week     follows  impressions  qual_content_calls")
for k in weeks:
    print(f"{k}  {fol[k]:7} {imp[k]:12,} {calls[k]:6}")
a = [fol[k] for k in weeks]; b = [calls[k] for k in weeks]
print(f"\nweeks={len(weeks)}  spearman follows vs calls (same week) = {spearman(a, b):+.2f}")
print(f"spearman impressions vs calls (same week) = {spearman([imp[k] for k in weeks], b):+.2f}")
lag = [k for k in weeks if f"{k[:6]}{int(k[6:]) + 1:02d}" in calls]
print(f"spearman follows vs next-week calls = {spearman([fol[k] for k in lag], [calls[f'{k[:6]}{int(k[6:]) + 1:02d}'] for k in lag]):+.2f} (n={len(lag)})")
