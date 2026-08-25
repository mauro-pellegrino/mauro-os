# Synthesis: "The 8 Content Formats That Actually Book Calls On X"

> **STATUS: NOT ADOPTED.** Research input only. Nothing in this file enters `skills/` until Mauro signs off row by row on the adopt/adapt/reject table below.

**Source:** `source-2026-08-24-x-top-formats-q3.md`, saved 2026-08-25.
**Whose data:** every example links to **@lorenzo_pravata**, not @maurojpelle. Treat every number below as **Lorenzo's account**, not ours. Window: 4 Jun to 24 Aug 2026, 521 posts, 1,423,324 impressions, 1,734 link clicks, 107 DM conversations.
**Open question for Mauro:** is this an account we run, or an outside account? It changes whether the numbers are usable internally and whether the account can ever be named. See "Attribution" at the bottom.

---

## What the doc actually argues

Eight formats do eight different jobs, and the jobs barely overlap. Ranked by what each one buys:

| Format | What it buys | Their evidence |
|---|---|---|
| Self-reply carrying the offer | **Clicks** | 90.5% of all clicks from 11.6% of reach, on the worst engagement in the account |
| Giving away an internal asset | **Audience** | 6% of posts → 71% of follows, 74% of replies |
| Breaking down someone else's operation | **Reach** | 15,160 avg vs 2,731 baseline, but 9 posts → only 106 follows |
| Comment-gated offer | **Conversations** | 6 posts → 107 DMs in 12 weeks |
| Long-form article on-platform | **Depth** | 3.48% expand vs 1.18%, 30% of shares, and 17 follows total |
| Pitch with the name swapped | **Intent** | low reach, 1.83% save rate vs 0.94% baseline |
| Showing work + reasons | **Saves** | best save rate of the quarter at 2.72% |
| One-line replies on others' posts | **Residency** | 21 avg impressions, best profile-visit rate at 7.81/1k |

The through-line: reach, audience, clicks and conversations are bought by four different formats, so an account optimised on any single metric will structurally underbuy three of them.

**The decay finding is the strongest part.** Reach per post fell 40% across the quarter while the *median never moved* (1,633 June → 1,719 August). The p90 halved and the best post fell 65%. Their read: the floor held and the ceiling caved in, which is evidence of one saturated format rather than account suppression, because suppression would drag the median down too. The saturated format was the internal-asset giveaway, dropping 82% in average reach over ten weeks with the mechanic unchanged.

**The doc is honest about its own limits,** which is worth noting given how much research isn't: it explicitly refuses to invent a platform changelog for Jun-Aug 2026, and it labels the semantic-dedup idea as a hypothesis to test rather than a finding.

---

## Adopt / adapt / reject

| # | Item from the source | Call | Reason |
|---|---|---|---|
| 1 | **The median-vs-p90 decay diagnostic.** Split monthly reach into median, p90 and best post to separate format saturation from account suppression. | **ADOPT (method only)** | It's arithmetic on our own export, not their conclusion. Runs on `research/x-analytics/maurojpelle-*.csv` today. Slots into `skills/ops/content-analytics-review.md`. |
| 2 | **Format-tag every post, then report per-format outcome instead of account averages.** | **ADOPT (method only)** | Same argument. Our analytics review currently reads reach-first at account level, which the source correctly shows is misleading when one format carries most of the outcome. |
| 3 | **Measure save rate, self-reply clicks, DMs opened/week, article opens.** | **ADOPT** | Consistent with belief 3 (specificity) and with what the Monday analysis already tries to do. No borrowed numbers involved. |
| 4 | **Self-reply stack carrying the offer under posts that are already moving.** | **ADAPT** | The mechanic is free to test and we're not running it systematically. Adapt: Mauro's version points at his own engine/case work, not a booking link, and the ban on naming clients applies to whatever the reply points at. **Test on our account before it becomes a rule.** |
| 5 | **"Announce the work has been updated" beats "book a call" as the ask.** | **ADAPT** | Fits Mauro's positioning (operator showing the machine, not a coach selling calls) better than it fits most accounts. Adopt the framing, verify the lift on our own data. |
| 6 | **Run the same gated offer 3+ times across two months.** | **ADAPT** | Sound reasoning (different slice of the same audience each time). Gated by the standing rule that the asset must exist before the keyword ships. |
| 7 | **Six-week rotation clock on the winning format, rotate on schedule not on evidence of decline.** | **ADAPT** | The logic is good, six weeks is *their* saturation curve in *their* niche. Take the clock, set our own interval from our own p90 trend. |
| 8 | **Credit what's working before naming the gap in a teardown.** | **ADOPT** | Already how `skills/research/brand-breakdown.md` should behave; worth making explicit. Costs nothing. |
| 9 | **"Articles promising one mechanism get opened, articles promising a list get impressions."** | **ADAPT** | A title rule worth testing in `x-article-creator.md`. One account, 34 articles, so it's a hypothesis not a law. |
| 10 | **Every specific number in the doc** (90.5%, 107 DMs, 1,437 opens, 2.72% save rate, the appendix table). | **REJECT for our content** | Lorenzo's account, different niche, different offer. Belief 10: never present someone else's numbers as ours. Usable internally as a comparison baseline, never in a Mauro post. |
| 11 | **The doc's eight-format taxonomy as a replacement for our vehicle library.** | **REJECT** | We have 13 in-use vehicles built around Mauro's actual production. Cross-map the two, don't swap. The value is the *outcome column* the taxonomy adds, not the taxonomy. |
| 12 | **The semantic-dedup hypothesis** (platform collapsing near-identical posts like ad creative). | **REJECT for now** | The source flags it as untested itself. Interesting, unverifiable, no action attached. |
| 13 | **"Formats one and five are where you sell, everything else earns the right to."** | **ADAPT** | Clean allocation principle. Our version needs the BOF gap monitor in `content-loop.md` to actually track the split. |

---

## What this unlocks, in order

1. **Run the method on Mauro's own export.** 376 posts, 25 May to 22 Aug 2026, already in the repo, and the columns match what the analysis needs exactly (Impressions, Bookmarks, New follows, Replies, Profile visits, Detail Expands, URL Clicks). Output is the same table with **our** numbers, which is the only version that can ever be published.
2. **Skill upgrades** (items 1, 2, 3, 8): analytics review, Monday analysis, brand breakdown. Cheap, no new numbers needed.
3. **The self-reply stack test** (items 4, 5): the largest claimed effect in the doc and the one we're least likely to be running.
4. **Content assets** off step 1, never off this doc.

## Attribution

Do not publish, quote, or paraphrase this document's numbers under Mauro's name. If @lorenzo_pravata is an account we run, the numbers are usable internally and the account still cannot be named publicly per the standing client rule. If it isn't ours, the doc is a competitor's analysis and stays purely as a comparison baseline.
