# 10 · i stopped writing scripts. i record off a board.

**Alt title:** the reason your talking-head videos sound read
**What this file is:** the information behind the video. Not a script.
**Written:** 2026-09-07

**Sources**
- `skills/youtube/miro-design-system.md` (the twelve section types and their exact specs)
- `skills/youtube/youtube-miro-board.md` (the build flow)
- `~/growthub-os/skills/miro/api-gotchas.md` (what breaks when you build boards over an API)
- `~/growthub-os/skills/miro/lane-readiness.md`, `review-flow.md`
- `research/charlie-morgan/charlie-morgan-dig.md` (the format validation)
- The board built through the MCP on 2026-09-06: https://miro.com/app/board/uXjVHqG6AzI=/

**ICP cut:** the owner who will not go on camera because reading a script makes him sound like a
hostage, and improvising makes him ramble for twenty minutes.
**Reach cut:** every creator has this problem and the usual answers are teleprompter or memorise.
A third answer with a visible artefact behind it travels.

---

## The one claim

A script makes you read. A board makes you talk. The board is the deliverable, and it is built from
the script rather than replacing it.

---

## The information

### 1. What a board is

A single vertical column, top to bottom, that maps the video's flow. Every concept gets a visual
container. No raw text walls. Generous vertical spacing so each section feels like its own slide.
All content centred on the vertical axis. One beat per point in the script, roughly ten to sixteen
beats for an eight-minute video.

The board has to be **record-ready: nothing missing, no editing needed at the moment of recording.**

### 2. The twelve section types

Title card, process or section title, question hooks, narration text block, two-path comparison,
tree diagram, horizontal pillar layout, multi-column expanded section, sticky-note grid, label to
description rows, green emphasis label, brand badge.

The segmentation rule: split at every new topic, every named process, and every clear shift in what
the script is doing (explaining, demonstrating, listing, concluding). Never split mid-thought. When
in doubt, plain centred text, because forcing content into a container that does not fit is worse
than no container.

The house palette is fixed: yellow `#ffdc4a` for labels and pillars, light yellow `#fff6b6` for
narration, lilac `#dedaff` for section titles and question hooks, green `#adf0c7` for a win, red
`#ff6464` for the negative path, `#1a1a1a` borders at 3px on every filled box. That border rule is
what produces the stacked-card look the whole system is recognisable by.

### 3. What happened when the build moved to the API

On 2026-09-06 a full board was built through the Miro MCP straight from a script: **59 items, zero
failures.** `[measured: the create call's own result, 2026-09-06]`

Two things had to be solved to get there, and they are the interesting content:

- **There is no text widget with a background colour in the DSL.** The yellow narration blocks are
  filled rectangles carrying centred content instead. Visually identical, different to hand-edit.
- **Coordinates are computed before anything is created.** A centre axis, a running vertical stack,
  and a width per section type. Nothing is nudged by hand afterwards.

### 4. What breaks, from the repo that has been doing this longest

The agency's Miro skills carry the scar tissue, all of it dated:

- **Past 200 items you can no longer edit or delete through the API.** The editor parses the whole
  board before applying a change and refuses beyond that line. Create still works. So on any board
  of real size you get one shot, and every coordinate has to be right before you send it.
- **One bad item fails the entire batch, opaquely.** A 37-item create returned 17 created and an
  HTTP 400 on the rest, and the response showed URLs for items that had not been created. The cause
  was a single invalid attribute value. The habit that saves the time: cap a batch at about ten
  items whenever a line uses an attribute value you have not successfully written before.
- **Table rows come back in random order.** Insertion order is not preserved and there is no way to
  set a default sort, so ordering has to live in a column rather than in the sequence.

### 5. The format is externally validated

The teardown of a 310k-subscriber channel found that three of its top ten videos are exactly this:
a hand-drawn whiteboard or a live Miro board narrated with a facecam in the corner. A winding road
from a now state to a future state, a funnel, a named theory. Board plus facecam is a proven format
at scale, not a workaround for people who hate scripts.

### 6. The review loop

Boards get corrected with a one-word comment vocabulary, and pasted media is never deleted during a
correction pass. A lane is not finished until it clears a readiness check, which includes a minimum
image share so a lane cannot ship as a wall of text.

---

## Evidence

| Claim | Status |
|---|---|
| 59 items created through the MCP, zero failures | `[measured: the 2026-09-06 create result]` |
| No background-colour text widget in the DSL | `[measured: the DSL spec, text fill is the text colour]` |
| 200-item ceiling on edit and delete | `[measured: recorded in api-gotchas.md, 2026-08-04]` |
| 37-item batch returned 17 created, 400 on the rest | `[observed: recorded 2026-08-03]` |
| Three of ten top videos on the reference channel use this format | `[observed: thumbnails 4, 6, 7 in the dig]` |
| Talking beats reading on camera | `[assumed: the premise of the whole system, unmeasured]` |

---

## Beats on camera

1. Read a scripted line, then say the same line off a board. Let the difference land.
2. What a board is: one column, one beat per point, ten to sixteen beats.
3. Record-ready as the standard.
4. The twelve section types, fast, with the palette on screen.
5. The segmentation rule and the default-to-plain-text escape hatch.
6. Building one live from a script through the API.
7. The two problems that had to be solved, named.
8. What breaks past 200 items, and why you get one shot.
9. The channel teardown that says the format works at scale.
10. The one-word review loop.
11. CTA.

---

## Do not say

- That boards replace scripts. The board is built from the script.
- Any claim that this improves retention. Nothing here measures retention.
- A client board or a client name, on screen or otherwise.

## Gaps

- `[NEEDS: Mauro's verdict on the rect-for-narration substitution before this is recorded]`
- `[NEEDS: a side-by-side of the extension-built board and the MCP-built board]`
