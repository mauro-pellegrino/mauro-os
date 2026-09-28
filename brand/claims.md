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
| Profile visits per 1,000 impressions that week: 22.5 on the 173 replies (69 / 3,072), 2.2 on the four bare article links (5 / 2,303), a 10.2x gap on the rounded pair | derived from the content export | yes |
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

## Cleared in the 21 Sep article brief

Source: `2026-09-21-distribution-system-article-brief.md`, approved by Mauro in chat 21 Sep 2026.
This block supersedes the **needs sign-off** flags on the three rows at the top of this file, for
these exact framings only.

| Claim | Framing that is cleared | Public |
|---|---|---|
| The agency I run is at about $300k/mo | as the agency's number, with the engine as the thing that is Mauro's | yes |
| At least a third of that comes from the organic accounts I manage | same framing | yes |
| I closed a $28k deal off X | yes | yes |
| This brand makes $0 today, about 200 followers, one YouTube video, 5 to 7 hours a week on it | yes, and it is an asset not an embarrassment | yes |

**The framing rule does not bend.** Write it as the engine Mauro runs for the agency, never as his
personal revenue (`brand/positioning.md`).

**Explicitly not cleared, brief says ask Mauro directly:** the channel split on qualified calls over
the last 90 days (roughly 55% X, 10% LinkedIn, 10% YouTube), and the auto-DM cadence of one to two a
day with the performance drop starting 1 August.

**Never, per the same brief:** the "$300k/mo closed from X and LinkedIn" phrasing Mauro used in the
session (looser than the repo version, and the repo version is the one that survives checking); the
"12 to 20 sign-ups per promoting post" figure (ownership unclear); the 40,000-banned-accounts figure
(external consulting call, unverified, never referenced in public content).

## The AI-content angle, 27 June 2026

Source: `research/transcripts/maurojpelle/ai-content-that-doesnt-sound-like-ai.md`, Mauro's own
spoken answers. These are his stances, not measurements, and they ship as stances.

| Claim | Public |
|---|---|
| The AI tell is sameness: everyone runs the same tool, so everyone sounds the same, and sameness is invisible | yes |
| An obviously-AI post tells a prospect the service behind it is slop too | yes |
| He is not arguing against using AI; the aim is to make AI sound less like AI | yes |
| The mechanism is voice notes, because the best writing is when you write like you talk | yes |
| A voice doc does two things: sounds like him in his transcripts, and holds hard bans | yes |
| He has never used an em dash in his life | yes |
| Almost everyone he works with is a non-native English speaker, which makes their AI output obvious | yes |
| Beginner: a new chat every day for a new post. Operator: split by format, each format with its own instructions and context | yes |

## The patience argument, 21 Sep 2026

Source: `research/transcripts/maurojpelle/2026-09-21-article-workflow-and-patience-belief.md`,
06:07 to 09:40. Mauro's own unprompted riff, previously unmined.

| Claim | Public |
|---|---|
| You have to be negative about the timeline to win at content; the realistic horizon is what makes the first year survivable | yes |
| The bad attitude is expecting the first article to hit and bring clients. The good one is planning to publish 50 videos or 150 articles | yes |
| An impossible month-one target is demoralising and is what makes people quit | yes |
| One account Mauro runs took a full year of daily posting before the first genuinely good call | yes, **unnamed only. That account owner is a client, so `CLAUDE.md` §7 applies** |
| Someone tried X by uploading a YouTube link, then a YouTube video, then a link again, 23 posts total, then concluded X does not work | yes, **unnamed only** |
| The Viktor Frankl concentration-camp passage as the analogy for the same point | **Mauro's own words, held back by default.** Reads badly in a marketing article. His call to put it back |

## Vendor prices, checked 21 September 2026

Checked against the vendor's own page on the date shown. Re-check before any republish; a stale
price is a CLAIM failure in a RESOURCES-format piece.

| Item | Price | Source |
|---|---|---|
| Claude Pro | $20/month billed monthly, or $17/month on annual billing at $200 up front | claude.com/pricing, 21 Sep 2026 |
| Claude Max | from $100/month | claude.com/pricing, 21 Sep 2026 |
| Claude Code | included in Pro | claude.com/pricing, 21 Sep 2026 |
| X Basic | $3.00/month, $32.00/year (web, US) | help.x.com/en/using-x/x-premium, 21 Sep 2026 |
| X Premium | $8.00/month, $84.00/year (web, US) | same |
| X Premium+ | $40.00/month, $395.00/year (web, US) | same |
| Articles are not listed in the X Basic tier | | help.x.com/en/using-x/x-premium, 21 Sep 2026 |
| The published For You ranking code is at github.com/twitter/the-algorithm | | repo README, 21 Sep 2026 |

**Two things that did not survive checking, and both ship as stated non-findings.**

X's own Premium page contradicts itself on which tier publishes Articles. The tier summary lists
Articles under Premium+. The features section, under the heading for Premium and Premium+, says
publishing Articles is limited to Premium subscribers. Say the contradiction, don't pick silently.

**The claim that the analytics CSV export is gated behind Premium could not be verified** on any of
X's own help pages. It does not ship as a fact.

## The visual-asset rules, as written up 2026-09-23

Source for every row: Mauro's own article draft on how a visual asset gets decided, built and
placed, handed over 2026-09-23. It follows the video-board write-up above and shares its
provenance. The article is not saved to this repo, per the standing rule.

| Claim | Source | Public |
|---|---|---|
| Three routes to a visual, and they are not interchangeable: author it, draw it, capture it | article draft | yes |
| Author it for a named process, a two or three column comparison, a table, a grid, a matrix, or a snippet shown exactly as written | article draft | yes |
| Draw it for a metaphor, a feeling, a joke, or an article header | article draft | yes |
| Capture it for evidence: a dashboard, a tracker, a real account | article draft | yes |
| The route gets picked before the style file opens, and picking wrong is where most of the wasted time goes | article draft | yes |
| A lane came out too dense and had to be rebuilt by hand, 2 September 2026. Every title and line of text below the render moved into blocks above and below it | article draft | yes |
| Hand-placing a diagram on the canvas is banned, and so is prompting an image model for one. Diagrams are authored in markup, rendered and pasted in. Default since 25 August 2026 | article draft + the 2026-09-16 row above | yes |
| The render spec is headless, at 2x, to a fixed width. The 2x is what stops the text going soft on a bigger screen or a cropped frame | article draft | yes |
| One stylesheet, never forked. Every asset imports the same base | article draft | yes |
| Three files in the skill, and only two get opened for a standalone asset. The lane rules are read only when the asset goes into a recording lane | article draft | yes |
| The sandwich, in this order: a narration block above, the bare render, a consequence block below | article draft | yes |
| The render carries no prose. Words inside it are labels, an axis name, a row name, a number | article draft | yes |
| A standalone asset keeps its headline, takeaway band and source line, because it travels with no narration next to it. In a lane all three come off | article draft | yes |
| Assets sit centred on the reading spine. A side-column asset does not count toward the lane's image density and gets skipped on camera | article draft | yes |
| Side annotations exist at a fixed offset and are commentary, never the asset | article draft | yes |
| A diagram never carries a claim on its own authority. The capture goes inside the diagram and the provenance goes in the production note under the slot | article draft | yes |
| The decide step has no gate on it. Ordering was the fix, and ordering is not enforcement | article draft, Mauro's own framing | yes |
| Capture is the route people skip, and the reason sounds sensible: a real dashboard looks worse than a designed one | article draft, Mauro's own stance | yes |
| A real dashboard looks worse than a designed one: the wrong fonts, a date range nobody asked about, a sidebar full of menu items, and a number lower than you would like | article draft | yes |
| The cost of picking the wrong route is the time spent before you knew the asset was bad, not the bad asset itself. Mauro's framing, and "an hour" in the article is his figure of speech, never a measurement | article draft | yes, **as time spent, never as a stated hour** |

**On the four-columns example.** The article illustrates the image-model failure with "four columns
of confident nonsense". The count is an illustration, never a measurement, so the number itself
never ships on a panel or in a post. The mechanism does ship: an image model returns a table of
confident nonsense in beautiful type, every word slightly off and none of it editable. Same ruling
as the forty-shapes example above.

**On "real creative" in the capture list.** The article names real creative as a thing worth
capturing. It stays out of Mauro's own panels and posts, because ad creative is the agency's
service and `CLAUDE.md` §1 keeps it out of his lane. Use a real account or a real post instead.

## The 90 day distribution build, as written up 2026-09-24

Source for every row: Mauro's own article draft, *how to build a claude code content system in 90
days (that books calls)*, handed over in full 2026-09-24. Same provenance pattern as the video-board
and visual-asset sections above. The article is not saved to this repo, per the standing rule.

These are the framework's own numbers: a plan Mauro wrote, not a measurement of the world. They ship
as his prescription, never as evidence of a result. The measured numbers this article uses live in
the analytics and profile-study sections above, and those are the ones that carry caveats.

| Claim | Source | Public |
|---|---|---|
| Five phases across 90 days, and every phase ends with a file, a sheet or a published piece you own | article draft | yes |
| Phase 1, build the brain, days 1 to 14 | article draft | yes |
| Phase 2, pick one channel, day 15 | article draft | yes |
| Phase 3, choose and track the inputs, days 15 to 45 | article draft | yes |
| Phase 4, study five accounts, days 30 to 60 | article draft | yes |
| Phase 5, split the output by vehicle, days 45 to 90 | article draft | yes |
| Phases 3, 4 and 5 overlap on purpose, and phase 4 is the only one that can slip a week | article draft | yes |
| The voice recording is one sitting, 30 to 40 minutes, no script and no notes | article draft | yes |
| The blind test is three posts written off the doc, shuffled with three you actually wrote, handed over unlabelled | article draft | yes |
| The four tracked inputs: comments on targeted profiles, replies under your own posts, dms sent, articles published | article draft | yes |
| "Conversations started" is the column that moves first, usually around week three | article draft | yes, **as his read, not a measurement** |
| The input targets ship as `[X]`, deliberately left for the reader to set | article draft | yes |
| The target list of accounts to comment on is 20 to 30 | article draft | yes |
| An account study captures 35 days, ten columns, one row per item | article draft + the profile-study section above | yes |
| The week: Monday 90 minutes on one article, Tuesday to Friday 45 minutes each, Friday plus 20 minutes for the sheet, once a month 2 hours for one account capture | article draft | yes |
| Inside those 45 minutes: 30 on comments and dms as one block, 15 to write and ship the short-form post | article draft | yes |
| That week lands a bit over 5 hours | article draft, derived from the row above | yes, **always as "a bit over 5", never as a measured figure** |
| The article block is the one that never moves. Everything else in the week bends | article draft | yes |
| 90 days to a booked call running it alone; 30 days to two booked calls with Mauro in it | article draft, **the offer's own promise** | yes, **needs sign-off before it ships anywhere but this article** |

**On the day ranges.** They are a plan, so they never get written as "it takes 14 days". The form
that ships is the phase and its window, the way the article states it.

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
