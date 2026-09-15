# Claims file

The only facts, numbers and named references allowed in copy. The CLAIM pass of the Gate
(`.claude/agents/gate.md`) checks every statement in a draft against this file. Anything not on it
is `UNSUPPORTED` and does not ship.

**Two failure modes this file exists to stop.** Inventing a number, and using a real number that
belongs to a different account. The second one is the likelier of the two here, because most of
the measured content evidence in these repos came off `@lorenzo_pravata`, not off `@maurojpelle`.

Columns: the claim as it may be stated, where it came from, and whether it can be said in public.

---

## Mauro's own operation

| Claim | Source | Public |
|---|---|---|
| Architected and runs the AI content and inbound engine for the B2B agency he handles content and acquisition for | `CLAUDE.md` §1 | yes |
| That agency does about $300k/mo | `CLAUDE.md` §1 | **needs sign-off** |
| At least a third of it comes from the organic accounts he manages | `CLAUDE.md` §1 | **needs sign-off** |
| Closed a $28k deal off X | `CLAUDE.md` §1 | **needs sign-off** |
| Ties content to booked calls and runs a weekly acquisition analysis | `CLAUDE.md` §1 | yes |
| Generated over 150 qualified booked calls for the agency in 2026 | Calendly export, confirmed by Mauro 2026-09-14 | yes, **see the attribution note below** |
| Never name the client or the agency in public-facing copy | `CLAUDE.md` §7 | rule, not a claim |

**Attribution note on the 150.** Mauro's own published article states that 649 of 678 Calendly
rows sit under one owner and the UTM field is empty on 673 of them, and that you cannot cleanly
attribute a booking to a channel with data like that. So "150 booked calls" is defensible from the
export. "150 booked calls **through X and LinkedIn**" is a channel claim the Calendly data alone
does not carry. Either state the total without the channel, or say how the 150 were separated
from the rest. A prospect who reads the article and then the offer will find this.

**Never borrow the agency's anchors as Mauro's personal proof.** Stating the agency's revenue as
his own is a CLAIM failure even though the number is real.

## The content system, as published 2026-09-10

Every row below appeared in Mauro's own published article, so it is already public.

| Claim | Source |
|---|---|
| One repo, eleven top-level areas, indexed in `ops/MAP.md` | published article |
| 73 markdown skill files across eight activity folders | published article |
| 25 Python scripts, each declaring its own limit in its first lines | published article |
| Four agents, all defensive, none reaches out to a human | published article |
| Nine conventions, four of which carry the weight | published article |
| Monthly impressions fell 64% between June and August 2026, unnoticed for two months | published article |
| The board gate answers one question through fifteen checks | published article |
| 649 of 678 Calendly rows sit under one owner; the UTM field is empty on 673 of them | published article |
| A skill claimed the worked example was the converting section; it did 60,000 against the winning section's 264,000 | published article |
| The Miro API has a 200-item ceiling past which nothing can be edited or deleted | published article |
| One bad attribute silently failed 20 of 37 board items | published article |

Live counts drift from the published ones. The repo currently holds more skill files and more
scripts than the article states. **Quote the published numbers when referring to that article**,
and re-measure before publishing a new figure.

## Article evidence

| Claim | Source | Whose account |
|---|---|---|
| The corpus behind the article skills is built from 41 real captures | `x-articles-POINTER.md` | 24 accounts, not one |
| The 1,800-3,000 word band medians 225,900 impressions; the 900-1,800 band medians 73,300 | `_corpus.md` via pointer | reach, 41 captures |
| Three accounts tested capitalised against lowercase titles; capitalised won 5x, 6x and 12x | pointer | three accounts |
| Reach and booked calls are independent, Spearman +0.16 across twelve articles | pointer | **@lorenzo_pravata** |
| Every converter documented a process we operate; a tool tutorial did 0.48x and a client case study 0.30x | pointer | **@lorenzo_pravata, n=12** |
| One capture read 68,000 at four days and 89,000 at five months | `06-distribution.md` | one capture |
| One article did 25,000 on 2026-05-11 and 4,700 when republished 2026-08-31 | `06-distribution.md` | same account, republish |
| A quote tweet did 1,000,000 against its own article's 109,000 | `06-distribution.md` | corpus, `qt-002` |

**The convert-lane rows are Lorenzo's account, selling performance creative to brand operators
spending $100k+/mo on Meta.** Mauro sells to agency owners installing AI systems. Stating those
findings as evidence for this account is a CLAIM failure. Stated as "the strongest hypothesis I
have, measured on another account", it passes.

## @maurojpelle X analytics, 2 to 15 September 2026

Source for every row: `brand/analytics/exports/2026-09-02_2026-09-15-account-overview.csv` (daily)
and `brand/analytics/exports/2026-09-09_2026-09-15-content.csv` (per-post). Working read saved at
`brand/analytics/2026-09-15-two-week-review.md`. All public, these are Mauro's own account numbers.

| Claim | Source | Public |
|---|---|---|
| Sep 2-8: 32,455 impressions, 113 new follows, 3 unfollows, 134 profile visits | overview export | yes |
| Sep 9-15: 10,258 impressions, 109 new follows, 17 unfollows, 95 profile visits | overview export | yes |
| Impressions fell 68.4% week over week; new follows fell by 4 | derived from the two rows above | yes |
| Follows per 1,000 impressions went 3.48 (week one) to 10.63 (week two) | derived | yes |
| Sep 3: 4,823 impressions, 0 new follows | overview export | yes |
| Sep 5: 8,826 impressions, 14 new follows (1.6 per 1k), the fortnight's peak reach day | overview export | yes |
| Sep 8: 2,784 impressions, 36 new follows | overview export | yes |
| Sep 10: 2,144 impressions, 38 new follows (17.7 per 1k), the fortnight's best follow day | overview export | yes |
| Sep 13: 1,121 impressions, 0 new follows, 7 unfollows | overview export | yes |
| Sep 9-15 post export: 196 posts, 173 of them replies, 8,260 impressions total | content export | yes |
| Replies carried 3,072 of 8,260 impressions (37%) and 69 of 103 profile visits (67%) | content export | yes |
| The per-post New follows column sums to 2 across Sep 9-15 against 109 in the daily overview | both exports | yes |
| The 2 attributed follows: one 234-impression original post, one 12-impression reply | content export | yes |
| The four highest-reach posts of that week were bare article links: 876, 678, 380, 369 impressions (2,303 total), 5 profile visits, 0 attributed follows | content export | yes |
| Highest-reach single reply that week: 124 impressions, 0 follows | content export | yes |
| Length buckets: 15 words or under n=4 median 529 impressions; 30-60 words n=17 median 143. All four posts in the short bucket are bare t.co links | content export | yes, **always with the confound stated** |

**Two cautions on this block.** Two weeks is not a trend, say so when quoting it. And the
≤15-word length result is confounded with format (every post in the bucket is an article link),
so it never ships as a length finding.

## Named references

Real people and products may be named. Get the name right, a wrong one burns credibility with an
operator audience. Confirmed spellings in use: Wiz of ecom, Charlie Morgan, Claude Code, LeadShark,
Miro, Notion, Atria, Calendly.

## What is NOT in this file

No hook rates, no CPA figures, no ROAS lifts, no follower counts, no client results, no revenue
for @maurojpelle, no conversion rates on the lead magnets, no numbers for The Content Machine offer.
None of those have a source in the repo. If a draft needs one, it gets `[NEEDS: x]` and Mauro
fills it, per the standing rule that a source gap beats a filled template slot.

---

*Created 11 September 2026. Add a row when a number gets measured, with its source. Never add a
row from memory.*
