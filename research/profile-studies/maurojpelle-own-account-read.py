"""What @maurojpelle's own export says, read against the shannholmberg findings.

Source: research/x-analytics/maurojpelle-2026-05-25-to-2026-08-22.csv

LIMITS, read before quoting anything.
- Window ends 2026-08-22. Three weeks are missing as of 2026-09-15.
- The export has no media column and does not mark quote tweets, so the carousel-vs-video and
  the QT findings from the shannholmberg study CANNOT be tested here. Only opener grammar and
  the reply-vs-post split can.
- X exports articles separately. Any article in the window is absent from this file.
- One account, one window.
"""
import csv, re, statistics as st

P = 'research/x-analytics/maurojpelle-2026-05-25-to-2026-08-22.csv'
num = lambda r, k: (int(float(r[k])) if r.get(k) not in (None, '', '-') else 0)
rows = list(csv.DictReader(open(P)))
txt = lambda r: (r.get('Post text') or '').strip()

replies = [r for r in rows if txt(r).startswith('@')]
posts   = [r for r in rows if txt(r) and not txt(r).startswith('@')]

def block(label, rs):
    imp = [num(r, 'Impressions') for r in rs]
    print(f"{label:<12} n={len(rs):>3}  total {sum(imp):>7,}  median {st.median(imp):>5,}  max {max(imp):>6,}")

print(f"window {min(r['Date'] for r in rows)} to {max(r['Date'] for r in rows)}")
block("all rows", rows)
block("replies", replies)
block("own posts", posts)
print(f"\nnew follows over the window: {sum(num(r,'New follows') for r in rows)}")
print(f"profile visits: {sum(num(r,'Profile visits') for r in rows)}")
print(f"replies are {len(replies)/len(rows):.0%} of everything published")
print(f"replies carry {sum(num(r,'Impressions') for r in replies)/sum(num(r,'Impressions') for r in rows):.0%} of impressions")

print("\ntop 10 items by impressions, and what they are:")
for r in sorted(rows, key=lambda r: -num(r, 'Impressions'))[:10]:
    kind = "reply" if txt(r).startswith('@') else "post "
    print(f"  {num(r,'Impressions'):>6,}  {kind}  {txt(r)[:62]!r}")

HOW = re.compile(r'^\s*how\b', re.I)
hit = [r for r in posts if HOW.match(txt(r))]
print(f'\nopener test: posts opening with "how" n={len(hit)}. '
      f'Too few to read. The shannholmberg 6.6x finding is untested here.')
