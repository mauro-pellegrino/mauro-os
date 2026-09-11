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
| Never name the client or the agency in public-facing copy | `CLAUDE.md` §7 | rule, not a claim |

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
