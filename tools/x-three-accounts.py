#!/usr/bin/env python3
"""Compare @maurojpelle, @lorenzo_pravata and @Bogzabs96 from every X content export on the Mac.

Reads ~/Downloads/account_analytics_content_*.csv and research/x-analytics/*.csv, assigns each row to
an account by its Post Link, dedupes by Post id, and prints per-account month stats (original posts vs
replies), weekly reply volume and the best/worst replies for Mauro.

    python3 tools/x-three-accounts.py
"""
import collections, csv, datetime as dt, glob, os, statistics

FILES = glob.glob(os.path.expanduser("~/Downloads/account_analytics_content_*.csv")) + \
        glob.glob(os.path.join(os.path.dirname(__file__), "..", "research", "x-analytics", "*.csv"))
ACC = {"maurojpelle": "Mauro", "lorenzo_pravata": "Lorenzo", "bogzabs96": "Bogdan"}
rows = {}
for f in FILES:
    for r in csv.DictReader(open(f, encoding="utf-8")):
        link = (r.get("Post Link") or "").lower()
        acc = next((v for k, v in ACC.items() if f"x.com/{k}/" in link), None)
        if not acc:
            continue
        r["acc"] = acc
        rows[r["Post id"]] = r  # later files overwrite: newer counts


def n(r, k):
    try:
        return int(float(r.get(k) or 0))
    except ValueError:
        return 0


for r in rows.values():
    r["day"] = dt.datetime.strptime(r["Date"].strip(), "%a, %b %d, %Y").date()
    t = (r.get("Post text") or "").strip()
    r["kind"] = "reply" if t.startswith("@") else ("long" if len(t) > 280 else "short")

print("account  month    | orig  imp(orig)  med  fol  vis | replies  imp(rep)  med  fol  vis | fol/1k")
for acc in ("Mauro", "Lorenzo", "Bogdan"):
    by = collections.defaultdict(list)
    for r in rows.values():
        if r["acc"] == acc:
            by[r["day"].strftime("%Y-%m")].append(r)
    for m in sorted(by):
        if m < "2026-06":
            continue
        o = [r for r in by[m] if r["kind"] != "reply"]
        p = [r for r in by[m] if r["kind"] == "reply"]
        def s(x):
            imps = [n(r, "Impressions") for r in x]
            return (len(x), sum(imps), int(statistics.median(imps)) if imps else 0,
                    sum(n(r, "New follows") for r in x), sum(n(r, "Profile visits") for r in x))
        so, sp = s(o), s(p)
        tot_imp = so[1] + sp[1]
        fol = so[3] + sp[3]
        print(f"{acc:8} {m}  | {so[0]:4} {so[1]:10,} {so[2]:5} {so[3]:4} {so[4]:4} | {sp[0]:6} {sp[1]:9,} {sp[2]:4} {sp[3]:4} {sp[4]:4} | "
              f"{(1000 * fol / tot_imp if tot_imp else 0):.2f}")
    print()

mr = sorted([r for r in rows.values() if r["acc"] == "Mauro" and r["kind"] == "reply"], key=lambda r: r["day"])
wk = collections.Counter(r["day"] - dt.timedelta(days=r["day"].weekday()) for r in mr)
print("Mauro replies per week:", ", ".join(f"{d:%m-%d} {c}" for d, c in sorted(wk.items()) if d >= dt.date(2026, 7, 1)))
rec = [r for r in mr if r["day"] >= dt.date(2026, 9, 1)]
print(f"\nMauro replies since 1 Sep: {len(rec)}; with 0-20 impressions: {sum(n(r,'Impressions') <= 20 for r in rec)}; "
      f"with a follow: {sum(n(r,'New follows') > 0 for r in rec)}; with a profile visit: {sum(n(r,'Profile visits') > 0 for r in rec)}")
targets = collections.Counter((r["Post text"].split()[0]).lower() for r in rec)
print("most-replied handles since 1 Sep:", ", ".join(f"{h} {c}" for h, c in targets.most_common(12)))
for label, sel in (("TOP", sorted(rec, key=lambda r: -n(r, "Impressions"))[:8]), ("BOTTOM", sorted(rec, key=lambda r: n(r, "Impressions"))[:8])):
    print(f"\n{label} replies since 1 Sep")
    for r in sel:
        print(f"  {r['day']} {n(r,'Impressions'):6,} imp {n(r,'New follows')} fol {n(r,'Profile visits')} vis | {r['Post text'].replace(chr(10),' ')[:150]}")
mo = sorted([r for r in rows.values() if r["acc"] == "Mauro" and r["kind"] != "reply" and r["day"] >= dt.date(2026, 9, 1)], key=lambda r: -n(r, "Impressions"))
print(f"\nMauro original posts since 1 Sep: {len(mo)}")
for r in mo[:10] + [None] + mo[-5:]:
    if r is None:
        print("  ..."); continue
    print(f"  {r['day']} {r['kind']:5} {n(r,'Impressions'):6,} imp {n(r,'New follows')} fol {n(r,'Profile visits')} vis {n(r,'Bookmarks')} bm | {r['Post text'].replace(chr(10),' ')[:120]}")
