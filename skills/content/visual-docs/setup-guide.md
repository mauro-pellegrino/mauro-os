# Setup Guide — Mauro Visual Docs Project

One-time setup to stand up the claude.ai project that runs Mauro's visual doc system. Mauro does this once; Juan works inside the finished project (see `juan-tutorial.md`).

The system makes **two output types**: SOCIAL HTML (LinkedIn + X infographics, paged) and BOARDS (long, spacious, editable breakdown boards for YouTube). Both run off the same files.

---

## Step 1 · Create the project

Claude.ai → New Project → name it "Mauro Visual Docs".

---

## Step 2 · Upload these files to project knowledge

Required:

1. **`mauro-visual-doc-system.md`** — the master skill. Single source of truth: palettes, typography, dimensions, block libraries (social + board), voice rules, workflow, QC checklist.
2. **`render_one.py`** — the render script. HTML → PDF + PNG in both modes (social paged + board long-scroll).

Also upload for the VA:

3. **`juan-tutorial.md`** — the usage tutorial Juan follows.

### Optional: reference HTMLs

Upload 3-5 canonical examples so Claude copies working CSS rather than rebuilding from the spec:

- a **portrait** social play-card doc
- a **square QT-reaction** infographic
- a **board** breakdown (Miro grammar, header/item cards + image slots)
- a **banner** template (5:2)

Don't upload everything.

---

## Step 3 · Set the project instructions

Paste into Custom Instructions:

```
Building Mauro's branded visual content (@maurojpelle). Two output types:
  1. SOCIAL HTML — fixed-size infographics for X quote-tweets / LinkedIn (green brand, paged).
  2. BOARDS — long, spacious, editable breakdown boards for YouTube (Miro-card grammar
     on a cream background, green brand, long scroll, Mauro's own pasted-in images).

Follow mauro-visual-doc-system.md as the spec for everything: palettes, typography,
dimensions, blocks, voice rules, workflow, QC checklist.

For every new doc:
1. Confirm the type: SOCIAL (green, paged) or BOARD (warm, long scroll, editable).
2. Pick dimension: square / portrait / long for social, board for breakdowns.
3. Outline structure before drafting. Social: map sections to pages. Board: order
   flow -> header cards -> item cards -> image slots.
4. Run the grep voice sweep BEFORE rendering: em dashes, contrast cadence, preacher
   "Most X" openers, three-fragment staccato, trailing morals.
5. Render with render_one.py (portrait/square/long, or board). Banners: inline render.
6. QA each output (PDF + PNG). On boards, check image paths resolve.
7. Ship HTML + PDF + all PNGs with slug naming. Nothing publishes without Mauro's sign-off.

Voice rules are HARD constraints. If one violation is flagged, fix every instance of
that pattern across the whole doc.

No em dashes in body (footer signature only). No "not X but Y" / "X, not Y" / "rather
than" / "instead of" cadence. No "Most X does Y" openers. No three-fragment staccato.
No trailing summary one-liners. No invented numbers (real or [X%] only; only pre-approved
public number is the agency I run, ~$300k/mo). No Caveat / handwriting fonts.

For boards, keep Mauro's pasted-in images in an ./images/ folder, reference them with
relative paths, and leave a dashed placeholder for any not ready.

CTAs: social posts end with "DM me [keyword]". YouTube CTAs point to X, never
"subscribe / stay on YouTube."
```

---

## Step 4 · First conversation (confirm setup)

**Test 1 — skill loaded:**
> "Read mauro-visual-doc-system.md and give me the brand foundation hexes, and how the two types use them."

Expected: Cream `#F7F3EA`, White `#FFFFFF`, Deep Forest `#1B4332`, Sage `#52B788`, Pale Mint `#B7E4C7`, Mint `#D8F3DC`, Honey (secondary) `#E9B949`. Social = white bg + green blocks; boards = cream bg, Deep Forest header bars, Mint item cards, Pale Mint intro bars, honey for emphasis only. If not, the skill didn't upload right.

**Test 2 — both render modes:**
> "Test render. Build a minimal portrait social page titled 'Setup Test' and render it. Then build a minimal 3-section board and render it as a board."

Expected: Claude builds both HTMLs, runs `python3 render_one.py setup-test.html portrait` and `python3 render_one.py board-test.html board`, and ships PDF + PNG for each. Confirms the Playwright + pypdfium2 + Pillow chain works and the board height-measurement path runs.

If it fails with "module not found": `pip install playwright pypdfium2 Pillow --break-system-packages` then `playwright install chromium`.

---

## Step 5 · Handing off to Juan

Once Tests 1 and 2 pass, point Juan at `juan-tutorial.md` inside the project. He produces; Mauro approves. Nothing publishes without Mauro's sign-off.

---

## File organization in the project

```
/
├── mauro-visual-doc-system.md    (skill — required)
├── render_one.py                  (render script — required)
├── setup-guide.md                 (this file)
├── juan-tutorial.md               (VA usage tutorial)
├── references/                    (optional example HTMLs)
├── images/                        (pasted-in screenshots for boards)
└── outputs/
    ├── 2026-07-doc-name.html
    ├── 2026-07-doc-name.pdf
    └── 2026-07-doc-name-p1.png  /  2026-07-doc-name.png (board)
```

Date-prefix output filenames so the library stays scannable.

---

## When something breaks

**"module not found":** re-run the install from Step 4.
**Social PNG wrong dimension:** check the PDF page size matches the `@page` rule and the final `.resize((PAGE_W, PAGE_H))`.
**Board cut off at the bottom:** content grew after height was measured, usually a late-loading font. Fonts use `display=swap`; if it still clips, add a small delay before measuring.
**Board images don't show:** the `src` path is wrong or the file isn't in `./images/`. Paths are relative to the HTML; the renderer loads over `file://`.
**Board column off-center:** the `.doc` wrapper isn't `margin:0 auto` at a fixed width, or padding is asymmetric.
**Voice grep false positives:** "the most reliable signal" matches the preacher pattern but is a fine superlative. Distinguish "Most [group] does X" from "the most X."

---

## Summary

Send to the project: `mauro-visual-doc-system.md`, `render_one.py`, `juan-tutorial.md`, (optional) reference HTMLs. Set the Step 3 instructions. Run the two Step 4 tests. Point Juan at his tutorial.
