#!/usr/bin/env python3
"""Follows per month from autodm (resource-gated) posts vs everything else, per account.

Autodm = "built a file", "put every prompt", "comment WORD", "I'll send" style posts.
Uses the loader in x-three-accounts.py (all X exports on the Mac).

    python3 tools/x-follow-drivers.py
"""
import collections, contextlib, io, re, runpy
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(__file__.replace("x-follow-drivers.py", "x-three-accounts.py"), run_name="lib")
rows, n = ns["rows"], ns["n"]
M = re.compile(r"built a file|put every prompt|put all my learnings|comment ['\"“]?[A-Z]{3,}|I'll send|I will send|send it to you|DM you", re.I)
for acc in ("Lorenzo", "Bogdan", "Mauro"):
    by = collections.defaultdict(lambda: [[0, 0], [0, 0]])
    for r in rows.values():
        if r["acc"] != acc or r["kind"] == "reply" or r["day"].strftime("%Y-%m") < "2026-05":
            continue
        i = 0 if M.search(r["Post text"] or "") else 1
        by[r["day"].strftime("%Y-%m")][i][0] += 1
        by[r["day"].strftime("%Y-%m")][i][1] += n(r, "New follows")
    print(acc)
    for m, (a, o) in sorted(by.items()):
        print(f"  {m}: autodm {a[0]} posts {a[1]} follows | other {o[0]} posts {o[1]} follows")
