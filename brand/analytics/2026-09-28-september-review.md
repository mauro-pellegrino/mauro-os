# CONTENT ANALYTICS REVIEW — September 2026 (Sep 1-28)

> **Superseded 29 Sep 2026** by `2026-09-content-review.md`, once the post-level export for
> Sep 2-29 arrived. Two calls in here are wrong: the reach peaks were banter replies, not content,
> and bare links are not the month's top bookmark format. Kept for the audit trail.

**Inputs:** `exports/2026-09-01_2026-09-28-account-overview.csv` (daily, 28 days),
`exports/2026-09-09_2026-09-15-content.csv` (per-post, 7 days, the only post-level data for the month).
Internal working doc. Does not publish.

---

## What this export cannot answer

The account overview is daily account totals. It has no post id, no post text, no per-post row.
It cannot rank tweets. The question "which tweets performed best" is unanswerable from this file
for 21 of the month's 28 days.

Post-level data exists for Sep 9-15 only. Everything below marked **(post-level)** rests on that
week. Everything marked **(daily)** rests on the full month and is account-level.

To close this, pull the **content** export for Sep 1 to Sep 28 from X analytics (Content tab,
same date range, separate download from the overview).

---

**Headline (daily):** 63,443 impressions, 285 new follows, 33 unfollows, 366 profile visits,
55 bookmarks across 69 posts. Impressions fell 78% from week 1 to week 4. Zero video views all month.

## The month, week by week (daily)

| | Sep 1-7 | Sep 8-14 | Sep 15-21 | Sep 22-28 |
|---|---|---|---|---|
| Impressions | 31,974 | 12,593 | 11,868 | 7,008 |
| Posts | 23 | 18 | 15 | 13 |
| Impressions / post | 1,390 | 700 | 791 | 539 |
| New follows | 79 | 144 | 37 | 25 |
| Unfollows | 4 | 18 | 6 | 5 |
| Net follows | 75 | 126 | 31 | 20 |
| Follows / 1k imp | 2.47 | 11.43 | 3.12 | 3.57 |
| Profile visits | 132 | 104 | 78 | 52 |
| Bookmarks | 22 | 19 | 6 | 8 |

Two things move together and one does not. Impressions, posts and profile visits all decline
week over week. Follows spike in week 2 on less than half of week 1's reach, then collapse.

## The two days worth identifying

**Sep 6: 18 bookmarks on 3,583 impressions.** That is 33% of the month's bookmarks in one day.
The next best day is 6. Whatever went out on Sep 6 is the single most save-worthy thing of the
month and there is no post-level row for it.

**Sep 5: 8,826 impressions on 2 posts.** The month's reach peak, 14% of all September impressions,
and it converted at 1.6 follows per 1k against a month average of 4.49. High reach, poor
conversion. Also unidentified.

Both sit outside the Sep 9-15 post export. These are the two rows to look up first when the
content export lands.

## Follows are decoupled from reach (daily)

| Day | Imp | New follows | Follows/1k |
|---|---|---|---|
| Sep 05 | 8,826 | 14 | 1.6 |
| Sep 03 | 4,823 | 0 | 0.0 |
| Sep 10 | 2,144 | 38 | 17.7 |
| Sep 08 | 2,784 | 36 | 12.9 |
| Sep 28 | 412 | 0 | 0.0 |

The best follow day of the month (Sep 10, 38 follows) did a quarter of the reach of the best
impression day (Sep 5, 14 follows). Ranking anything on impressions alone points the wrong way.

Caveat carried forward from the 15 Sep review: per-post `New follows` summed to 2 against an
account-reported 109 for the same week. Follow attribution at post level is broken in X's export.
Profile visits is the reliable per-post outcome column.

## Format (post-level, Sep 9-15, n=196)

| Format | # | Imp | Share | Bookmarks | Profile visits |
|---|---|---|---|---|---|
| link/media (article drops) | 7 | 2,783 | 33.7% | 13 of 15 | 5 |
| short original | 8 | 1,222 | 14.8% | 1 | 15 |
| longform | 8 | 1,175 | 14.2% | 1 | 5 |
| reply | 173 | 3,072 | 37.2% | 0 | 69 |

Three jobs, three formats, and they do not overlap:
- **Article drops earn reach and saves.** 7 posts, a third of the week's impressions, 13 of 15
  bookmarks. Five profile visits between them.
- **Replies earn profile visits.** 173 posts, 67% of profile visits, zero bookmarks.
- **Short originals earn profile visits per impression.** The top two (7 pv on 234 imp, 6 pv on
  192 imp) beat the 876-impression article drop (4 pv) on visits.

## Top originals, Sep 9-15 (post-level)

By impressions:

| Imp | Bkm | PV | Post |
|---|---|---|---|
| 876 | 7 | 4 | article drop (bare link) |
| 678 | 1 | 1 | article drop (bare link) |
| 380 | 4 | 0 | article drop (bare link) |
| 369 | 0 | 0 | article drop (bare link) |
| 261 | 0 | 2 | "Here's why these anti-slop writing prompts are so important" |
| 247 | 0 | 0 | the repo state post (11 areas, 73 skills, 25 scripts) |
| 234 | 0 | 7 | "You don't have a writing problem. You have a selection problem." |
| 217 | 1 | 3 | "I ran my own x export through the analysis prompt... It refused to rank my formats" |
| 213 | 1 | 0 | "An analysis that names its own blind spot lets you go get the missing data" |
| 192 | 0 | 6 | the engagement-signal list (profile click, follow, share via dm) |

The two highest profile-visit posts of the week are both single-idea reframes with no link:
the selection-problem post (7 pv) and the engagement-signal list (6 pv).

## Replies: rooms that put him in front of people (post-level, Sep 9-15)

| Account | Replies | Imp | Imp/reply | PV |
|---|---|---|---|---|
| @danielfazio | 1 | 124 | 124.0 | 6 |
| @umzrs | 1 | 109 | 109.0 | 1 |
| @eshaankansal | 1 | 103 | 103.0 | 3 |
| @ethanejk | 1 | 99 | 99.0 | 4 |
| @retentiongoat | 1 | 90 | 90.0 | 4 |
| @atishayhyperke | 2 | 165 | 82.5 | 0 |
| @lorenzo_pravata | 6 | 227 | 37.8 | 0 |
| @theroborourke | 6 | 141 | 23.5 | 0 |
| @revenumaxxing | 7 | 68 | 9.7 | 0 |

The pattern: one-off replies under larger in-niche accounts return 80-124 impressions each and
carry profile visits. The three accounts he replies to most (19 replies between them) return
9-38 impressions each and produced zero profile visits.

## Levers for October

1. **Pull the content export for Sep 1-28 and identify Sep 6 and Sep 5.** Every format and topic
   call below is resting on one week of 196 rows. The month's best save day and best reach day
   are both blind.
2. **Posting volume is down 43% (23 to 13 posts/week) and impressions are down 78%.** Impressions
   per post fell too (1,390 to 539), so volume is not the whole story, but it is the half that is
   directly controllable.
3. **Reallocate reply volume.** 19 replies went to three accounts returning under 38 imp each and
   zero profile visits. The same 19 replies spread across large in-niche accounts at the observed
   80-124 imp rate is roughly 1,500-2,300 additional impressions per week.
4. **Keep article drops as bare links.** They did a third of the week's reach and nearly all the
   bookmarks on 7 posts. They do not drive profile visits, so do not judge them on that.
5. **Pair every article drop with a standalone reframe post.** The selection-problem and
   engagement-signal posts out-earned the 876-impression link on profile visits at a quarter of
   the reach.

## Sample-size flags

- Format and reply tables are n=196 posts across 7 days. One week. Directional.
- Per-post follow attribution is unusable (2 attributed against 109 reported). Not used here.
- Reply-target rows with n=1 (@danielfazio, @umzrs, @eshaankansal, @ethanejk, @retentiongoat)
  are single observations. The pattern across all five is consistent, each row alone is not.
- Video: the `Video views` and `Media views` columns are 0 on all 28 days. There is no video
  signal in this data at all.

---

*Run 28 September 2026 per `skills/ops/content-analytics-review.md`.*
