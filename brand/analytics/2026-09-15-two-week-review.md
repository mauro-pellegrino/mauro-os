# CONTENT ANALYTICS REVIEW — 2 to 15 September 2026

**Inputs:** `exports/2026-09-02_2026-09-15-account-overview.csv` (daily, 14 days),
`exports/2026-09-09_2026-09-15-content.csv` (per-post, 7 days).
Internal working doc. Does not publish.

---

**Headline:** impressions fell 68.4% week over week (32,455 → 10,258) and new follows fell by 4
(113 → 109). Follows per 1,000 impressions went 3.48 → 10.63.

## Week over week

| | Sep 2-8 | Sep 9-15 |
|---|---|---|
| Impressions | 32,455 | 10,258 |
| New follows | 113 | 109 |
| Unfollows | 3 | 17 |
| Net follows | 110 | 92 |
| Profile visits | 134 | 95 |
| Engagements | 625 | 538 |
| Follows / 1k imp | 3.48 | 10.63 |

## Daily, and the inverse

| Date | Imp | New fol | Unfol | PV | Fol/1k |
|---|---|---|---|---|---|
| Sep 2 | 3,921 | 2 | 1 | 19 | 0.5 |
| Sep 3 | 4,823 | 0 | 1 | 13 | 0.0 |
| Sep 4 | 5,336 | 14 | 0 | 21 | 2.6 |
| Sep 5 | 8,826 | 14 | 0 | 24 | 1.6 |
| Sep 6 | 3,583 | 16 | 0 | 10 | 4.5 |
| Sep 7 | 3,182 | 31 | 0 | 33 | 9.7 |
| Sep 8 | 2,784 | 36 | 1 | 14 | 12.9 |
| Sep 9 | 2,156 | 29 | 1 | 18 | 13.5 |
| Sep 10 | 2,144 | 38 | 4 | 22 | 17.7 |
| Sep 11 | 1,939 | 18 | 2 | 25 | 9.3 |
| Sep 12 | 996 | 6 | 2 | 7 | 6.0 |
| Sep 13 | 1,121 | 0 | 7 | 12 | 0.0 |
| Sep 14 | 1,453 | 17 | 1 | 6 | 11.7 |
| Sep 15 | 449 | 1 | 0 | 5 | 2.2 |

Peak reach day (Sep 5, 8,826 imp) converted at 1.6 follows per 1k. Best day (Sep 10, 2,144 imp)
converted at 17.7. Sep 3 did 4,823 impressions and produced zero follows.

## The attribution gap

The per-post `New follows` column sums to **2** across the Sep 9-15 export. The overview reports
**109** new follows over the same seven days. 107 of 109 carry no post.

The 2 that are attributed: one 234-impression original post ("You don't have a writing problem.
You have a selection problem."), one 12-impression reply to @david_bassey_.

Consequence: **no per-post follow conclusion is drawable from this export.** Rank formats on
profile visits instead, which is attributed properly.

## Format (Sep 9-15 post export)

| Format | # | Imp | Share | Med imp | Profile visits | PV / 1k imp | Bkm |
|---|---|---|---|---|---|---|---|
| link/media | 7 | 2,783 | 33.7% | 369 | 5 (top 4 only) | ~2 | 13 |
| short original | 8 | 1,222 | 14.8% | 136 | — | — | 1 |
| longform | 8 | 1,175 | 14.2% | 160 | — | — | 1 |
| reply | 173 | 3,072 | 37.2% | 11 | 69 | 22.5 | 0 |

Replies: 88% of posts, 37% of impressions, **67% of profile visits (69 of 103)**.
The four bare-link posts (the week's four highest-reach posts, 876 / 678 / 380 / 369 = 2,303 imp)
produced **5 profile visits and 0 attributed follows** between them, and 11 of 15 bookmarks.

Highest-reach reply of the week: 124 imp (@danielfazio), 0 follows. The one reply that produced a
follow did 12 imp.

## The length table is a format table

The script's impressions-by-length output reads as a clean win for short posts:

- ≤15 words: n=4, median 529 imp
- 15-30 words: n=2, median 204 imp
- 30-60 words: n=17, median 143 imp

**All four posts in the ≤15 bucket are bare t.co links with no body text**, i.e. the article
posts. The bucket is measuring format, not length. Do not act on it as a length finding.

## Open, unexplained

Unfollows went 3 → 17 week over week, and Sep 13 produced 0 new follows against 7 unfollows on
1,121 impressions. There is no per-post unfollow column and no way to attribute it from this
export. Logged, not diagnosed. Re-check on the full-month export.

## Levers

1. **Rank formats on profile visits per 1k, not impressions.** It is the only outcome column in
   this export that is filled in.
2. **Reply volume is carrying account growth signal** (22.5 PV/1k vs ~2 on links) and costs the
   least reach. Hold or raise it. Note the follow link is unproven, see the attribution gap.
3. **Link posts earn reach and bookmarks, not profile visits.** 33.7% of impressions and 11 of 15
   bookmarks, 5 profile visits. Treat them as distribution and save-worthiness, not growth.

## Sample-size flags

- Every per-post follow conclusion rests on n=2. Directional at best, treated as unusable here.
- The ≤15-word length bucket is n=4 and confounded with format. Discarded.
- Two weeks is not a trend. Re-run the same four passes on the full September export.

---

*Run 15 September 2026 per `skills/ops/content-analytics-review.md`.*
