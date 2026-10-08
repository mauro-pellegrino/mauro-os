#!/usr/bin/env python3
"""Per-handle reply scoreboard for @maurojpelle, used to re-tier brand/analytics/reply-target-list.md.

A reply = a row whose post text starts with "@". The handle credited is the FIRST @ in the text
(X puts the thread participants first; for a multi-handle reply the first one is usually the
original poster, but not always).

    python3 tools/x-reply-targets.py                # since 1 Sep (default)
    python3 tools/x-reply-targets.py --since 2026-07-08 --csv path.csv
    python3 tools/x-reply-targets.py --rows         # also print best and worst replies

Weekly (Monday): export X Analytics > Content for the last 7 days, save it to research/x-analytics/,
then run with --since <last Monday> --csv <that file>. The two numbers Juan is measured on are
"profile visits per reply" (outside the team) and "follows", plus the share of replies on the roster.
"""
import argparse, collections, csv, datetime as dt, re, statistics

TEAM = {"lorenzo_pravata", "bogzabs96"}          # own team: zero-reach rooms, never a target
ap = argparse.ArgumentParser()
ap.add_argument("--csv", default="research/x-analytics/maurojpelle-2026-07-08-to-2026-10-05.csv")
ap.add_argument("--since", default="2026-09-01")
ap.add_argument("--rows", action="store_true")
a = ap.parse_args()
since = dt.date.fromisoformat(a.since)

def n(r, k):
    try: return int(float(r[k] or 0))
    except ValueError: return 0

rows = []
for r in csv.DictReader(open(a.csv, encoding="utf-8")):
    d = dt.datetime.strptime(r["Date"], "%a, %b %d, %Y").date()
    t = (r["Post text"] or "").strip()
    m = re.match(r"@(\w+)", t)
    if not m:
        continue
    rows.append(dict(day=d, h=m.group(1), text=t, imp=n(r, "Impressions"), pv=n(r, "Profile visits"),
                     fol=n(r, "New follows"), likes=n(r, "Likes"), link=r["Post Link"]))

aug = [x for x in rows if dt.date(2026, 8, 1) <= x["day"] < dt.date(2026, 9, 1)]
cur = [x for x in rows if x["day"] >= since]
print(f"replies since {since}: {len(cur)} | follows {sum(x['fol'] for x in cur)} | "
      f"profile visits {sum(x['pv'] for x in cur)} | impressions {sum(x['imp'] for x in cur)}")
if aug:
    print(f"median impressions per reply: Aug {statistics.median(x['imp'] for x in aug)} "
          f"({len(aug)} replies in this export) -> since {since} {statistics.median(x['imp'] for x in cur)}")
words = [x for x in cur if len(re.sub(r"@\w+", "", x["text"]).split()) <= 3]
print(f"replies of 3 words or fewer: {len(words)}")
team = [x for x in cur if x["h"].lower() in TEAM]
print(f"replies to own team ({', '.join(TEAM)}): {len(team)}, {sum(x['imp'] for x in team)} imp, "
      f"{sum(x['pv'] for x in team)} visits, {sum(x['fol'] for x in team)} follows")

out = [x for x in cur if x["h"].lower() not in TEAM]
print(f"replies outside the team: {len(out)} | profile visits per reply {sum(x['pv'] for x in out)/max(len(out),1):.2f} | "
      f"follows {sum(x['fol'] for x in out)}")

# share of replies that went to a handle on the roster (every @handle above the RED section)
try:
    md = open("brand/analytics/reply-target-list.md", encoding="utf-8").read()
    roster = {h.lower() for h in re.findall(r"@(\w+)", md.split("## RED")[0])}
    on = [x for x in out if x["h"].lower() in roster]
    print(f"replies to roster handles: {len(on)} of {len(out)} | visits per reply on roster "
          f"{sum(x['pv'] for x in on)/max(len(on),1):.2f} vs off roster "
          f"{sum(x['pv'] for x in out if x not in on)/max(len(out)-len(on),1):.2f}")
except FileNotFoundError:
    pass

by = collections.defaultdict(list)
for x in cur:
    by[x["h"]].append(x)

def tier(h, xs):
    reps, pv, fol = len(xs), sum(x["pv"] for x in xs), sum(x["fol"] for x in xs)
    if h.lower() in TEAM: return "TEAM"
    if fol: return "KEEP"
    if pv == 0 and reps >= 2: return "DROP"
    if pv == 0: return "ONE-OFF-0"
    if reps >= 3 and pv <= 1: return "DROP"
    if pv >= 2: return "TEST"
    return "ONE-OFF"

print(f"\n{'handle':22} rep   imp  pv fol  pv/rep  tier")
for h, xs in sorted(by.items(), key=lambda kv: (-sum(x['pv'] for x in kv[1]), -len(kv[1]))):
    pv = sum(x["pv"] for x in xs)
    print(f"@{h:21} {len(xs):3} {sum(x['imp'] for x in xs):5} {pv:3} {sum(x['fol'] for x in xs):3}"
          f"  {pv/len(xs):6.2f}  {tier(h, xs)}")

c = collections.Counter(tier(h, xs) for h, xs in by.items())
print("\ntier counts:", dict(c), "| handles:", len(by),
      "| replied to once:", sum(1 for xs in by.values() if len(xs) == 1))

if a.rows:
    print("\nBEST (by profile visits, then impressions)")
    for x in sorted(cur, key=lambda x: (-x["pv"], -x["imp"]))[:15]:
        print(f"{x['day']} imp {x['imp']:4} pv {x['pv']} fol {x['fol']} | {x['text'][:150]} | {x['link']}")
    print("\nWORST (0 visits, lowest impressions)")
    for x in sorted([x for x in cur if x["pv"] == 0], key=lambda x: x["imp"])[:15]:
        print(f"{x['day']} imp {x['imp']:4} pv {x['pv']} fol {x['fol']} | {x['text'][:150]}")
