#!/usr/bin/env python3
"""Weekly keyword tracking per X account (Wiz, 28 Aug call: about 25 topic keywords per account,
place them on purpose, track which win, repeat them).

The list lives in tools/x-keyword-list.json: per account a "track" list (the keywords to place on
purpose) and an "avoid" list (keywords that sink reach). Seeded 8 Oct 2026 from x-keywords.py
(top reach lifts since 1 Jun) and, for Mauro, ICP terms from brand/audience.md.

Scoring: original posts only (no replies). Last week (Mon-Sun) against the 8 weeks before it.
  lift      = median impressions of the posts that contain the keyword / the account's 8-week median
  vis/post  = profile visits per post, fol/post = new follows per post
  WINNER    = 2+ posts last week and lift >= 2      LOSER = 2+ posts last week and lift < 0.7
  NEW WINNER (not tracked yet) = 2+ posts last week and lift >= 2.5 -> add it to the list
  DROP?     = 3+ posts in the 8 weeks and 8-week lift < 0.7
  (R)       = every post behind the number is a resource/autodm post. That format is dead since
              the X automation ban (Wiz, 28 Aug), so an (R) winner does not repeat as is.

    python3 tools/x-keyword-tracker.py                       # all accounts, last complete week
    python3 tools/x-keyword-tracker.py Lorenzo Bogdan        # from growthub-os, by absolute path
    python3 tools/x-keyword-tracker.py --week 2026-09-28     # score another week (its Monday)
    python3 tools/x-keyword-tracker.py --out FILE.md         # also write the markdown block
    python3 tools/x-keyword-tracker.py --list OTHER.json     # another keyword list
    python3 tools/x-keyword-tracker.py --seed Lorenzo        # top-lift candidates to curate the list
Data: every X export the loader in x-three-accounts.py finds (Downloads, mauro-os, growthub-os).
"""
import argparse, contextlib, datetime as dt, io, json, os, runpy, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    kw = runpy.run_path(os.path.join(HERE, "x-keywords.py"), run_name="lib")
rows, n, M, words = kw["rows"], kw["n"], kw["M"], kw["words"]
for r in rows.values():
    r["_w"] = words(r["Post text"])

ap = argparse.ArgumentParser()
ap.add_argument("accounts", nargs="*", default=["Lorenzo", "Bogdan", "Mauro"])
ap.add_argument("--week", help="Monday of the week to score (default: last complete Mon-Sun week)")
ap.add_argument("--list", default=os.path.join(HERE, "x-keyword-list.json"))
ap.add_argument("--out")
ap.add_argument("--seed", action="store_true")
a = ap.parse_args()


def norm(k):
    """Put a list keyword in the same form as words(): 'Link in bio' -> 'link bio'."""
    w = sorted(words(k), key=len, reverse=True)
    return w[0] if w else k.lower()


def med(xs):
    return statistics.median(xs) if xs else 0


def stat(ps, k, base):
    hit = [r for r in ps if k in r["_w"]]
    if not hit:
        return dict(n=0, lift=None, vis=None, fol=None, res=False)
    return dict(n=len(hit), lift=med([n(r, "Impressions") for r in hit]) / base if base else 0,
                vis=sum(n(r, "Profile visits") for r in hit) / len(hit),
                fol=sum(n(r, "New follows") for r in hit) / len(hit),
                res=all(M.search(r["Post text"] or "") for r in hit))


def f(x, d=1):
    return "-" if x is None else f"{x:.{d}f}"


newest = max(r["day"] for r in rows.values())
today = dt.date.today()
mon = dt.date.fromisoformat(a.week) if a.week else today - dt.timedelta(days=today.weekday() + 7)
sun, start = mon + dt.timedelta(days=6), mon - dt.timedelta(weeks=8)

if a.seed:
    for acc in a.accounts:
        ps = [r for r in rows.values() if r["acc"] == acc and r["kind"] != "reply" and r["day"] >= dt.date(2026, 6, 1)]
        base = med([n(r, "Impressions") for r in ps])
        allk = {k for r in ps for k in r["_w"]}
        st = [(k, stat(ps, k, base)) for k in allk]
        st = sorted([x for x in st if x[1]["n"] >= 6], key=lambda x: -x[1]["lift"])[:60]
        print(f"\n{acc}: top 60 lifts since 1 Jun (6+ posts), median {base:,.0f}")
        for k, s in st:
            print(f"  {k:28} {s['n']:4} {s['lift']:5.2f} vis {s['vis']:6.1f} fol {s['fol']:5.1f}{' (R)' if s['res'] else ''}")
    raise SystemExit

cfg = json.load(open(a.list, encoding="utf-8"))
out = [f"### X keyword tracker: {mon:%d %b} - {sun:%d %b %Y} vs the 8 weeks before",
       f"Newest export row: {newest:%d %b %Y}. List: `{a.list}`."]
if newest < sun:
    out.append(f"**WARNING:** the exports stop on {newest:%d %b}, before the week ends on {sun:%d %b}. "
               "Download a fresh X content export, or the week reads low.")
for acc in a.accounts:
    lst = cfg.get(acc) or {}
    track, avoid = [norm(k) for k in lst.get("track", [])], [norm(k) for k in lst.get("avoid", [])]
    orig = [r for r in rows.values() if r["acc"] == acc and r["kind"] != "reply"]
    lw = [r for r in orig if mon <= r["day"] <= sun]
    tr = [r for r in orig if start <= r["day"] < mon]
    base = med([n(r, "Impressions") for r in tr])
    out.append(f"\n**{acc}**: {len(lw)} original posts last week, median {med([n(r, 'Impressions') for r in lw]):,.0f} "
               f"impressions (8-week median {base:,.0f} over {len(tr)} posts). "
               f"Visits/post {f(sum(n(r, 'Profile visits') for r in lw) / len(lw) if lw else None)} "
               f"(8w {f(sum(n(r, 'Profile visits') for r in tr) / len(tr) if tr else None)}), "
               f"follows/post {f(sum(n(r, 'New follows') for r in lw) / len(lw) if lw else None, 2)} "
               f"(8w {f(sum(n(r, 'New follows') for r in tr) / len(tr) if tr else None, 2)}).")
    if not track:
        out.append(f"No keyword list for {acc} in the JSON.")
        continue
    if not lw:
        out.append("No original posts in the week. Nothing to score.")
        continue
    table, unplaced, drop = [], [], []
    for k in track:
        s, t = stat(lw, k, base), stat(tr, k, base)
        if t["n"] >= 3 and t["lift"] < 0.7:
            drop.append(f"{k} ({t['lift']:.2f}x over {t['n']})")
        if not s["n"]:
            unplaced.append(k)
            continue
        flag = "WINNER" if s["n"] >= 2 and s["lift"] >= 2 else "LOSER" if s["n"] >= 2 and s["lift"] < 0.7 else ""
        if flag and s["res"]:
            flag += " (R)"
        table.append((s["lift"], f"| {k} | {s['n']} | {f(s['lift'], 2)} | {f(t['lift'], 2)} ({t['n']}) | "
                                 f"{f(s['vis'])} / {f(t['vis'])} | {f(s['fol'], 2)} / {f(t['fol'], 2)} | {flag} |"))
    out.append(f"\nPlaced last week: {len(table)} of {len(track)} tracked keywords.\n")
    out.append("| keyword | posts | lift | 8w lift (posts) | vis/post lw / 8w | fol/post lw / 8w | flag |")
    out.append("|---|---|---|---|---|---|---|")
    out += [row for _, row in sorted(table, key=lambda x: -x[0])] or ["| (none placed) | | | | | | |"]
    if unplaced:
        out.append(f"\nNot placed last week ({len(unplaced)}): {', '.join(unplaced)}.")
    known = set(track) | set(avoid)
    cand, seen = [], {}
    for k in sorted({k for r in lw for k in r["_w"]} - known, key=lambda k: (-len(k), k)):
        s = stat(lw, k, base)
        ids = frozenset(r["Post id"] for r in lw if k in r["_w"])
        if s["n"] >= 2 and s["lift"] >= 2.5 and ids not in seen:  # one keyword per identical set of posts
            seen[ids] = k
            cand.append((s["lift"], f"{k} ({s['lift']:.2f}x over {s['n']}{', R' if s['res'] else ''})"))
    if cand:
        out.append("New winners, not tracked yet (add?): " + "; ".join(c for _, c in sorted(cand, reverse=True)[:6]) + ".")
    if drop:
        out.append("Tracked but under 0.7x over 8 weeks (drop?): " + "; ".join(drop) + ".")
    used = [f"{k} ({stat(lw, k, base)['n']})" for k in avoid if stat(lw, k, base)["n"]]
    if used:
        out.append("Avoid-list keywords used last week: " + ", ".join(used) + ".")

md = "\n".join(out)
print(md)
if a.out:
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(md + "\n")
