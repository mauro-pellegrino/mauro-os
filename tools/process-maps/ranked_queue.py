#!/usr/bin/env python3
"""Ranked queue: which process to fix first. Reads queue.csv, which you fill by hand every Monday.
Columns: process, posts, reach_x_calls, matched_calls, human_min
  posts          posts shipped by this process in the window you are reading
  reach_x_calls  mean per post of (reach ÷ the account's own median) × (1 + matched calls), blank if unknown
  matched_calls  booked calls on the post day or the next whose source matches the channel
  human_min      human minutes per post, measured on the clock; blank until timed
Rank: calls per human hour when human_min is filled for a row, else reach_x_calls, else "no data yet" at the bottom.
Usage: python3 tools/process-maps/ranked_queue.py [queue.csv]"""
import csv, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "queue.csv"
num = lambda v: float(v) if v and v.strip() else None
rows = []
for r in csv.DictReader(open(src, newline="")):
    p, m, rc, mc = num(r["posts"]), num(r["human_min"]), num(r["reach_x_calls"]), num(r["matched_calls"])
    cph = mc / (p * m / 60) if p and m and mc is not None else None
    tier, score = (0, cph) if cph is not None else (1, rc) if rc is not None else (2, 0)
    rows.append(dict(name=r["process"], posts=p, cph=cph, rc=rc, mc=mc, tier=tier, score=score))
rows.sort(key=lambda d: (d["tier"], -d["score"]))
f = lambda v, fmt="{:.2f}": "-" if v is None else fmt.format(v)
print(f'{"#":>2}  {"process":34} {"posts":>5} {"calls/hr":>8} {"reach×calls":>11} {"matched":>7}  ranked on')
for i, d in enumerate(rows, 1):
    on = ["calls per human hour", "reach × calls (no times yet)", "no data yet"][d["tier"]]
    print(f'{i:>2}  {d["name"][:34]:34} {f(d["posts"], "{:.0f}"):>5} {f(d["cph"]):>8} {f(d["rc"]):>11} {f(d["mc"], "{:.0f}"):>7}  {on}')
print("\nmatched calls are day-level: posts on the same day share that day's calls. Read them as relative, never as a call count.")
