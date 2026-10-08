#!/usr/bin/env python3
"""Keyword research from the X exports: which words and phrases lift reach, visits and follows.

For each account, original posts (no replies) from 1 Jun 2026. A keyword's lift = the median
impressions of posts that contain it / the account's median. Resource (autodm-style) posts are
counted apart, because they carry most follows whatever the words.

    python3 tools/x-keywords.py            # all accounts
    python3 tools/x-keywords.py Lorenzo    # one account
"""
import collections, contextlib, datetime as dt, io, re, runpy, statistics, sys
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(__file__.replace("x-keywords.py", "x-follow-drivers.py"), run_name="lib")
rows, n, M = ns["rows"], ns["n"], ns["M"]
STOP = set("""a an the and or but if then so to of in on at for with from by as is are was were be been it its this that these
those i you we he she they my your our their me us them not no do does did done have has had just more most very can will would
should could about into out up down over than too also only all any each every some what which who how why when where there here
one two get got make made like amp https co t im ive dont youre its thats rt s re ll ve d m new now right still way""".split())
MIN = 6


def words(t):
    t = re.sub(r"https?://\S+|@\w+", " ", (t or "").lower())
    w = [x for x in re.findall(r"[a-z][a-z0-9\-\.]+", t) if x.strip(".-") and x.strip(".-") not in STOP]
    w = [x.strip(".-") for x in w]
    return set(w) | {a + " " + b for a, b in zip(w, w[1:])}


accs = sys.argv[1:] or ["Lorenzo", "Bogdan", "Mauro"]
for acc in accs:
    posts = [r for r in rows.values() if r["acc"] == acc and r["kind"] != "reply" and r["day"] >= dt.date(2026, 6, 1)]
    base = statistics.median(n(r, "Impressions") for r in posts)
    idx = collections.defaultdict(list)
    for r in posts:
        for k in words(r["Post text"]):
            idx[k].append(r)
    stats = []
    for k, rs in idx.items():
        if len(rs) < MIN:
            continue
        med = statistics.median(n(r, "Impressions") for r in rs)
        stats.append((k, len(rs), med / base, sum(n(r, "New follows") for r in rs) / len(rs),
                      sum(n(r, "Profile visits") for r in rs) / len(rs), sum(bool(M.search(r["Post text"] or "")) for r in rs)))
    print(f"\n=== {acc}: {len(posts)} original posts since 1 Jun, median {int(base):,} impressions ===")
    for title, sel in (("WORK (highest reach lift)", sorted(stats, key=lambda s: -s[2])[:25]),
                       ("DON'T WORK (lowest reach lift)", sorted(stats, key=lambda s: s[2])[:15])):
        print(f"\n{title}\n  keyword                       posts  lift  fol/post vis/post  resource-posts")
        for k, c, lift, fpp, vpp, res in sel:
            print(f"  {k:30} {c:4} {lift:5.2f} {fpp:8.1f} {vpp:8.1f} {res:6}")
