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

## Cover prompts

Covers saved for their look and their device, with copy-paste image prompts derived from them, live in
[cover-prompt-library.md](cover-prompt-library.md). An image can be saved there on its own, without the
article it came from.

## Open gaps on the corpus

- **01 needs its link, view count and cover image file.** Text and title are captured.
- Different authors means no house style to average out. Tag the author on every row so a pattern can later be
  checked per-account rather than across the whole pile.
