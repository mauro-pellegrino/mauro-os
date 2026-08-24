# Content Analytics Review — week of Tue 18 Aug to Mon 24 Aug 2026

**Input:** `exports/2026-08-18-to-08-24-account-overview.csv` (X account overview, daily rows)
**Not run:** format table, reply-reach-by-account, top posts, follow drivers. Those need the per-post content export (Analytics > Content > Export). This file has no post-level rows.
**Prior period:** none saved. First entry in `brand/analytics/`, so no month-over-month.

---

## Headline

13,041 impressions, 29 new follows, 6 unfollows (net +23), 3 bookmarks, 0 shares, 31 creations logged.

---

## The week in rates

| Metric | Total | Per 1k impressions |
|---|---|---|
| Engagements | 469 | 36.0 (3.60%) |
| Likes | 296 | 22.7 (2.27%) |
| Replies received | 54 | 4.1 |
| Profile visits | 114 | 8.7 (0.87%) |
| New follows | 29 | 2.2 |
| Bookmarks | 3 | 0.23 |
| Shares | 0 | 0 |
| Reposts | 2 | 0.15 |

Profile visit to follow conversion: 29/114 = **25%**. The profile and bio are not the bottleneck.

---

## Finding 1: zero media all week

`Video views` and `Media views` are 0 on all 7 days. Every impression came from plain text.

The Aug 2025-2026 baseline in `skills/ops/content-analytics-review.md` recorded link/media posts earning roughly 4x the reach per post of everything else, off only 10 of 319 posts. He posted none of them this week. Largest single under-use in the file.

## Finding 2: effort is pointed at the low-reach days

| Window | Days | Impressions | Follows | Profile visits | Creations | Imp per creation |
|---|---|---|---|---|---|---|
| Tue 18 to Fri 21 | 4 | 10,034 (77%) | 23 (79%) | 88 | 17 | **590** |
| Sat 22 to Mon 24 | 3 | 3,007 (23%) | 6 | 26 | 14 | **215** |

45% of the week's output went into the window that produced 23% of the reach. Same effort on Tue to Thu at weekday rates is worth roughly +5,250 impressions a week (projection off the 590 vs 215 gap, not a measured result).

## Finding 3: the bookmark rate is the real problem

3 bookmarks against 296 likes across 13,041 impressions. Zero shares. Nothing published last week was worth saving or sending to a colleague.

For an ICP of agency owners at mid six figures a month, bookmarks and shares are the signal that matters. Likes mean they agreed. Bookmarks mean they intend to use it. A 0.02% bookmark rate says the content is agreeable and not usable.

## Finding 4: Wednesday and Thursday reached the same people, Thursday converted 2.3x better

| Day | Impressions | Follows | Follows per 1k | Profile visits |
|---|---|---|---|---|
| Wed 19 | 3,077 | 4 | 1.30 | 19 |
| Thu 20 | 3,026 | 9 | 2.97 | 29 |

Near-identical reach, very different conversion. Thursday is the best day in the file on follows, profile visits and follows per impression. Which posts drove it is not answerable from this export.

## Finding 5: Monday 24 reached wide and converted nothing

1,570 impressions (above the 1,863 daily average, and 2.2x Sunday) with 25 likes, 36 engagements, 7 profile visits, 1 follow.

Like rate 1.59% vs the 2.27% week average. Engagement rate 2.29% vs 3.60%. Profile visit rate 0.45% vs 0.87%. Reach delivered to an audience that did not care. Typical of a banter reply under a big account or an off-lane post. Needs the post-level export to name it.

## Finding 6: Sunday is the inverse

714 impressions, 30 likes. A 4.20% like rate, the highest of the week, on the second-lowest reach. Small audience, strong resonance. Distribution problem, not a content problem.

---

## Levers for next week, ranked

1. **Ship 2 visual/media assets, Tue and Thu.** Media was 0 this week and the baseline puts media at ~4x reach per post. Use `skills/content/visual-docs/mauro-visual-doc-system.md`. This is the only lever that hits impressions, bookmarks and shares at once.
2. **Move the 14 Sat-to-Mon creations into Tue-to-Thu.** 590 imp per creation vs 215. No extra work, more reach.
3. **Raise reply volume hard.** 31 creations across 7 days is the whole distribution budget. Replies are the cheapest impressions available and the account is too small for organic reach to carry it. Target a floor of 15 replies a day under large in-niche accounts, logged so the per-post export can rank the rooms next week.
4. **Make one post a week explicitly save-worthy.** A numbered system, a real teardown with numbers, a checklist. Measure it on bookmarks, not likes. Baseline to beat: 3 a week.
5. **Audit Monday 24 and Thursday 20 post by post** once the content export exists. One converted at 2.97 follows per 1k and one at 0.64. That gap is the highest-value unknown in this data.

---

## Sample-size flags

- 7 days, 1 week, no prior period. Every day-of-week claim rests on a single observation and is directional.
- The Tue-to-Fri vs Sat-to-Mon split is 4 days vs 3 days. Directional.
- `Create Post` (31) may count replies as well as standalone posts. X's overview export does not separate them. Treat it as total creations, not standalone post count.
- Bookmarks (3) and shares (0) are too small for a rate to be stable. The direction is unambiguous regardless.
