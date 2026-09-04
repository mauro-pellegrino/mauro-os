# Outlier X articles

> **STATUS: COLLECTING. NOT ADOPTED.** This is a swipe corpus of high-view X Articles from **many different
> authors**, saved as raw input. Per Mauro's process spec
> (`research/transcripts/maurojpelle/2026-08-28-how-to-save-outlier-x-articles-loom.md`):
> **save only. Do not touch or build any skill until the corpus is full (~50).**

## What gets saved per article

Four components, from the Loom spec:

1. **Title** (screenshot the title from the feed, not from inside the article, so the frame carries title + cover + opening lines)
2. **Thumbnail** (if the cover is an HTML infographic, right-click and copy image instead of screenshotting, so the detail survives)
3. **Text** of the article
4. **Link** to the post

Plus **views**, since views are the only number used to pick an outlier and X has no filter for them.

## How to add one

Hand the four components over in chat, batched, not one at a time. Each article becomes a numbered file in
this folder. Store the cover as `NN-cover.png` alongside it. Add a row below.

## The corpus

| # | Author | Title | Views | Link | Cover class | Saved for |
|---|---|---|---|---|---|---|
| [01](01-saaspocalypse-is-overblown.md) | @denk_tweets | Everyone claims that SaaS is dead. They're all wrong. | *needs filling* | *needs filling* | Illustrated visual joke, category name carved on the object | The cover image and the title |
| [02](02-first-ai-consulting-retainer.md) | @coreyganim | How to land your first AI consulting retainer | **170K** | *needs filling* | Anime-style sunrise vista, lone figure from behind, no text | The whole piece |
| [03](cover-prompt-library.md) | @knoxtwts | how to build a customer acquisition system that gets smarter after every lead | *needs filling* | *needs filling* | Vintage engraving, candlestick phone whose cord climbs into a staircase, spine line baked in | The cover |
| [04](cover-prompt-library.md) | @Ecombos_Ai | How to Make Claude Build AI Ads That Actually Sell | *needs filling* | *needs filling* | Dark integration diagram, Claude logo joined to author's mark, four labelled output tiles | The cover |
| [05](cover-prompt-library.md) | @Aidanb2b | saturation is a skill issue: how the algorithm changed on linkedin and X + how to win now | *needs filling* | *needs filling* | Monochrome engraving, LinkedIn logo as the lighthouse lamp, one spot colour, crowd queueing | The cover |

## Cover prompts

Covers saved for their look and their device, with copy-paste image prompts derived from them, live in
[cover-prompt-library.md](cover-prompt-library.md). An image can be saved there on its own, without the
article it came from.

## Open gaps on the corpus

- **01 needs its link, view count and cover image file.** Text and title are captured.
- **02 needs its link and cover image file.** Title, text and views are captured.
- **03, 04 and 05 are cover and title only.** No body text and no view counts, so none of them can be read as
  an outlier yet. They live in the cover library rather than as their own capture files.
- **Only 02 has a number on it.** Four of five rows have no views, which means the corpus currently selects on
  Mauro liking the craft rather than on measured performance. That is fine for a cover library and not fine for
  drawing rules about reach. Links would fix all of it in one pass.
- Different authors means no house style to average out. Tag the author on every row so a pattern can later be
  checked per-account rather than across the whole pile.

## Patterns and tensions across the five

Five covers in. Log the readings, don't harden them into rules yet.

**Nothing here is a raw screenshot.** Four of five are illustrations, and the fifth (04) arranges real
screenshots into a designed composite. Not one is a bare screengrab of tooling. That runs against the
proof-of-work-screenshot convention recorded elsewhere in `research/`, and the likely split is that
illustration serves the `reach` lane while screenshots serve `convert`. Five captures, four without numbers,
so this stays a hypothesis.

**Two of five borrow a recognisable third-party logo, and it is the strongest repeated move so far.** 04 puts
the Claude asterisk beside the author's own mark. 05 makes the LinkedIn logo the lighthouse lamp. Both buy
instant recognition the author's own brand cannot. **05 does it better**, because the logo is load-bearing in
the metaphor rather than placed next to it, so it cannot read as a sponsor slot.

**Covers split on whether they carry information.** 01, 03, 04 and 05 all argue: an object metaphor, a drawn
thesis, a labelled output set, a crowd and a beacon. 02 carries no information at all and sells a feeling, and
02 is the only one with a number on it (170K). Do not resolve this on the evidence available.

**Baked-in text: three of five bake nothing in.** 02, 05 and (apart from its tile labels) 04 leave the frame
clean and let the platform render the title. 01 bakes in the headline itself and annotates it by hand. 03 bakes
in a three-word compression of the argument that is *not* the title. **03's split is still the most interesting
device in the library**, because it ships two headlines off one cover: a quotable thesis inside the frame and a
long descriptive promise underneath.

**Titles, across all five.** Three lowercase (03, 05, and 01's), two capitalised (02, 04). Every one names a
concrete referent: SaaS, AI consulting retainer, customer acquisition system, Claude, linkedin and X. `actually`
appears twice, doing the same job both times — implying every other version of the advice fails, without naming
anyone. Lengths run 7 to 16 words, and the longest (05) is the most constructed: a stance, then a mechanism,
then an action, joined by a colon and a plus.

**Titles.** The recorded reach rules say winners avoid plain reader-benefit promises and use a qualifier to
filter the ICP. 02 is nothing but a benefit promise, aimed at beginners, with no qualifier, and it is the
highest-reach piece here. The likely reconciliation is that refusing to filter is itself the reach mechanic,
which would put the qualifier rules on the `convert` lane only.
