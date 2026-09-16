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

## The X "For You" ranking code, as Mauro published it 2026-09-04

Every row below is from Mauro's own published thread, verbatim source at
`research/transcripts/maurojpelle/2026-09-04-x-source-code-myth-buster-thread.md`. Already public.
The authority is the open-source repo, not him, so state it that way.

| Claim | Source | Public |
|---|---|---|
| The For You ranking code is open source; the scoring formula is a weighted sum of predicted actions | published thread #2 | yes |
| The code gives the exact formula and the full list of scored actions, and none of the weight values | published thread #2 | yes |
| Scored actions include profile click, follow author, share via DM, share via copy link, dwell time, quoted click | published thread #3 | yes |
| A post that earns a profile visit and a follow works more of the scorer than one that earns a like | published thread #3 | yes |
| Four actions are scored negative and subtracted: not interested, block author, mute author, report | published thread #7 | yes |
| Hand-engineered features were eliminated; the model reads the viewer's own engagement history. No post-at-9am, hashtag or reply-to-yourself lever exists | published thread #4 | yes |
| A diversity function decays your own posts against each other inside one feed response: it sorts by score not time, the best post keeps its value, weaker posts absorb the decay | published thread #5 | yes |
| Five posts don't buy five slots in one person's feed | published thread #5 | yes |
| There is no link filter in the published code and nothing in the scorer touches external links | published thread #6 | yes |
| Nothing resurfaces: old posts get removed, and a post whose age can't be read is dropped | published thread #9 | yes |
| "reply = 13.5 likes", "repost = 20x" and "one reply beats 150 likes" are 2023 numbers from a system that got replaced | published thread #1 | yes |

**Never quote a weight value.** The code publishes none, and Mauro said so publicly. Any specific
multiplier is a CLAIM failure.

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
| Reply-reach spread that week: one reply under a large in-niche account did 124 impressions, while 7 replies under a smaller account did 68 between them | content export | yes |
| Link/media posts: 7 posts, 33.7% of the week's impressions, 11 of 15 bookmarks | content export | yes |
| Length buckets: 15 words or under n=4 median 529 impressions; 30-60 words n=17 median 143. All four posts in the short bucket are bare t.co links | content export | yes, **always with the confound stated** |

**Two cautions on this block.** Two weeks is not a trend, say so when quoting it. And the
≤15-word length result is confounded with format (every post in the bucket is an article link),
so it never ships as a length finding.

## The video board system, as written up 2026-09-16

Source for every row: Mauro's own article draft on generating the Miro video boards, handed over
2026-09-16, plus `research/article-source-pack/topics/01-miro-boards-fast.md` (his answers,
2026-09-14). The API rows were confirmed against `skills/miro/api-gotchas.md` in the agency repo on
the dates shown. The article is not saved to this repo, per the standing rule.

| Claim | Source | Public |
|---|---|---|
| A board took 4 hours by hand and is close to 2 hours now | source pack, answered 2026-09-14 | yes |
| Four boards a week, standing | article draft | yes |
| A real board runs 200 to 400 items | article draft + source pack | yes |
| Past 200 items the edit call parses the whole board and gives up; creating still works, editing and deleting do not. Confirmed 2026-08-04 | claims row above + source pack | yes |
| A 37-item create returned 17 created and one error covering the other 20, naming no item and no attribute. 2026-08-03 | claims row above + source pack | yes |
| The response body showed plausible urls for items that had not been created | article draft + source pack | yes |
| Two attribute values caused it, neither documented as invalid | article draft | yes |
| The build is four steps, beats then components then geometry then write, and only the write touches the board | article draft | yes |
| Shapes take an explicit width and height; a sticky accepts one or the other and grows to fit its text | article draft | yes |
| The quick inspection call returns frames, docs, tables and diagrams, and does not see images, text, shapes or stickies | article draft | yes |
| Diagrams are authored in markup, rendered and pasted in as images. Hand-placing and prompting a diagram are both banned, approved as the default 2026-08-25 | article draft | yes |
| Eight files, read in the same order every time: master, visual, archetype, writing, gotchas, assets, diagram, QA. The order is dependency | article draft | yes |
| Font size takes one size for headers, labels and one-liners and a smaller one for multi-sentence body cells. It was corrected three times before it stuck | article draft | yes |
| The board gate is fifteen checks; the first four are blockers and the run stops there | article draft + claims row above | yes |
| Roughly half the gate checks run as a script and the rest need eyes | article draft | yes |
| Something placed wrong stays wrong, or gets lassoed by hand in the ui | article draft | yes |
| The limit made placing boxes by hand impossible and forced a different shape of work | article draft, Mauro's own framing | yes |
| The script is split into distinct points with no summarising and no merging, and the beat count is checked against the target runtime first | article draft | yes |
| Each beat gets a form and a colour family: text read out loud exactly as written, diagrams, and pasted media that is real captures only | article draft | yes |
| Every coordinate, every height and every gap is computed up front | article draft | yes |
| A fixed row pitch computed in advance drifts when a sticky grows, because a sticky takes a width or a height and never both | article draft | yes |
| A full process map was built that duplicated one already on the same board, because nobody listed the board first | article draft | yes |


**On the forty-shapes example.** The article illustrates the blind inspection call with "a board
holding forty shapes and a dozen images reports as empty". That is an illustration of the
mechanism, not a measurement of a specific board, so it never ships as a stat on a panel or in a
post. State the mechanism instead.

**The generalised rule in the article** ("any system with no undo forces correctness up front, and
correctness up front is faster than fixing") is Mauro's own framing of his own measurement, so it
ships as a stance. It is not a measured finding about other people's systems and never gets stated
as one.

## The @shannholmberg profile study, run 2026-09-15

Source for every row: `research/profile-studies/shannholmberg-2026-09-15-analysis.md`,
`vehicles-from-shannholmberg.md` and `shannholmberg-2026-09-15-stats.py`, re-run and confirmed
2026-09-16. Process rows come from Mauro's loom to Juan, 2026-09-15.

**Limits that ship with any of these numbers.** One account, 35 days, n=52. Impressions are
timeline figures read at one moment and they keep climbing after. Topic labels are Mauro's
assignment, not the author's, so every topic-sliced row is the softest thing in the block. No
follower count or follower delta was captured, so nothing here says whether reach converts to
follows, and a draft that implies it does is a CLAIM failure.

| Claim | Source | Public |
|---|---|---|
| 52 items captured, 2026-08-11 to 2026-09-14, median 9,553 impressions | raw capture + stats.py | yes |
| Total 2,318,220 impressions; top 10 items carry 81%, top 5 carry 59%, the article carries 11% alone | stats.py | yes |
| Outlier line set at 3x median, 28,659, leaving 13 outliers of 52 | stats.py | yes |
| Quote tweets: 35 of 52, median 16,823, 11 of 13 outliers, 81% of reach | stats.py | yes |
| Standalone posts: 16 of 52, median 2,239, 1 outlier, 7% of reach | stats.py | yes |
| Article: 1 item, 257,640 impressions | stats.py | yes |
| A quote tweet's median is 7.5x a standalone post's | derived from the two rows above | yes |
| Carousel: 18 items, median 22,988, 8 outliers, 63% of reach | stats.py | yes |
| Single image: 17 items, median 22,876, 5 outliers, 33% of reach | stats.py | yes |
| Text only: 6 items, median 10,678, zero outliers, 3% of reach | stats.py | yes |
| Video: 5 items, median 3,140, zero outliers, 1% of reach | stats.py | yes |
| Link card: 6 items, median 682, zero outliers, 0% of reach, all below median | stats.py | yes |
| The text-only median, 10,678, is why a plain text post gets 13,000 views: that is the floor, not the ceiling | analysis.md, Step 2 | yes, **13,000 is illustrative of the floor, not a sourced single-post figure; don't state it as one item's count** |
| The split-CTA vehicle: expect roughly 700 views on the follow-up link post, never judge it on reach | vehicles-from-shannholmberg.md | yes |
| 22 of 52 items open with "how": median 23,378, 8 of 13 outliers. The other 30 median 3,539 | stats.py opener pass | yes, **the 6.6x is one account** |
| Tool reactions: 15% of items, 23% of reach, 4 outliers | stats.py topic table | yes |
| Stack posts: 10% of items, 35% of reach, 2 outliers | stats.py topic table | yes |
| Second brain, context and skills library posts: 24% of items, 20% of reach | stats.py topic table | yes |
| Biggest item of the month: 546,619 impressions, seven words of text over a carousel, "my AI stack has changed over the past months" | raw capture | yes |
| Bookmark-to-like on the top eight: the 546,619 post sits at 0.67, the only one under 1.0; the rest run 1.50 to 2.37, article 2.37 | stats.py | yes |
| Repost-to-like is flat by topic, 0.049 to 0.083, with no separation | stats.py | yes |
| Cadence: 52 items in 35 days, about 1.5 a day, one narrow subject. Two personal posts, both under 2,000 | raw capture + stats.py | yes |
| His article: 41,813 characters, 12 sections, 43 in-body images, 257,640 impressions | raw capture | yes |
| Named launches he translated: Wayfinder, a grill-me skill, Hermes bot mode, an x ads mcp, GPT-6 Astra | raw capture | yes |
| Ronin has about 500 youtube subscribers and no videos on the channel | Mauro's loom, 2026-09-15 | yes |
| The four steps: study content strategy, understand success and outliers, break down, templatize vehicles | Mauro's loom | yes |
| Verdict column is adopt / adapt / reject, with the reason written under a reject | Mauro's loom + vehicles file | yes |
| The first pass read one post's repost-to-like ratio as a finding; it did not hold across 52 items | vehicles file, Mauro's own correction | yes |

**The Andromeda comparison does not ship on Mauro's own copy.** The vehicles file cites Meta
Andromeda posts at roughly 4x the comment rate of anything else on the account. That is the
agency's account and the agency's lane, per `CLAUDE.md` section 1. Stating it in Mauro's voice
positions him as an ad-creative practitioner and is a CLAIM and POSITIONING failure.

**Naming @shannholmberg publicly is the point of the vehicle**, not an incidental mention. He is
not a client, so the no-naming rule in `CLAUDE.md` section 7 does not apply. Mauro still signs off
on naming him before anything publishes.

## The outlier X-article corpus process, run 2026-08-28

Source: `research/transcripts/maurojpelle/2026-08-28-how-to-save-outlier-x-articles-loom.md`, plus
`research/outlier-x-articles/README.md` and `cover-prompt-library.md` for the state of the corpus
itself. All process rows are Mauro's own spec, not measured findings, and are public as method.

| Claim | Source | Public |
|---|---|---|
| Rule: save only, build nothing (no skill, no template, no hardened pattern) until roughly 50 articles are in | loom | yes |
| X has no filter to sort articles by views; outliers are found by hand, from accounts already rated and by browsing Home for large accounts not yet followed | loom | yes |
| A big follower count is a reason to look, not a reason to save | loom | yes |
| Most common disqualifying pattern: a YouTube script pasted into X, reading as a transcript with headers | loom | yes |
| Five components saved per article: title screenshot (from the feed, not inside the article), the cover image, full text, the link, the view count | loom | yes |
| Cover capture rule: a plain-screenshot cover is already in the title shot; an HTML/detailed cover is right-clicked and copied, never screenshotted | loom | yes |
| Captures are batched and handed over together, not one at a time; each becomes a numbered file with its cover stored alongside it | loom | yes |
| The first seven captures: only one of seven (@coreyganim, "How to land your first AI consulting retainer") had a recorded view count, 170,000 | README.md corpus table | yes |
| Three of the seven captures were cover-and-title only, no body text and no view count, and were moved into a separate cover library rather than counted as outlier captures | README.md | yes |
| Links were missing on nearly all seven; the link and the view count are treated as the two non-optional fields, since a link lets everything else be re-fetched | loom + README.md | yes |
| Rule added after the first seven: tag the author on every row, since the corpus spans many different authors and a pattern must be checked per-author before it's treated as real | loom + README.md | yes |
| Reading discipline: an observation across seven captures is a note; the same observation across fifty, held per author, is a rule | loom | yes |
| Cross-capture reading, n=5 with numbers on one: none of the five saved covers is a raw screenshot, four are illustrations and one arranges real screenshots into a designed composite | README.md, "Patterns and tensions" | yes, **stated as a hypothesis, n=5** |
| Three of six covers borrow a recognisable external logo (Claude asterisk, LinkedIn mark as a lighthouse lamp, OpenAI mark as a movie mask); the strongest versions make the logo carry the argument's meaning rather than just appear in frame | README.md | yes, **n=6, one account's worth of covers each** |
| The @coreyganim piece is the only capture with a view count (170K) and the only cover that carries no argument, selling a feeling instead | README.md | yes |
| Titles across the five: three lowercase, two capitalised, lengths 7 to 16 words, every one naming a concrete referent | README.md | yes |
| The seven authors captured so far: @denk_tweets, @coreyganim, @knoxtwts, @Ecombos_Ai, @Aidanb2b, @immortalhowwl, and one not supplied | README.md corpus table | yes |

**Two forms of borrowed authority, same as the profile-study process:** the name ("I broke down
@author's article") and the number ("I broke down 40 articles"), and the number form is why the
corpus target is 50 rather than 5.

**Nothing above is a finding about what wins.** The corpus is mid-collection (7 of a ~50 target, one
of them with a view count). Any sentence that states a pattern as proven rather than as a live
hypothesis pending a fuller corpus is a CLAIM failure.

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
