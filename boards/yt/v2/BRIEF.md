# YT boards v2: the shared brief (2026-10-07)

Mauro rejected the v1 boards (`boards/yt/0*.html`). His words: "too much text, not having a clear
title, not having a proven title, not looking to go viral, not being extense enough". Then:
"generate a ton of mauro videos in a ton of html formats and we go from there".

This batch is a selection round. Six formats, each with different mechanics. The flagship topic
(video-knowledge doc 11, the Claude Code content system) is built in all six formats so Mauro can
compare formats on the same content. The other 11 docs are built in one format each.

## Read before you build

- `research/video-knowledge/<your docs>.md` (the source of every fact)
- `brand/claims.md` (the only source of public numbers)
- `brand/positioning.md`, `brand/voice.md`
- `skills/youtube/ideal-youtube-video.md`, `youtube-hook-script.md`, `youtube-title-generator.md`
- `skills/youtube/01-outliers.csv` and `research/charlie-morgan/charlie-morgan-dig.md` (title shapes)
- `content/boards/yt-thumbs.html` (the existing thumbnail style, 1280x720) and
  `research/charlie-morgan/thumbs/` (real outlier thumbnails)
- `boards/yt/build.py` (palette and the headless Chrome render path) and one v1 board, to see what failed

## Hard rules (each one fixes a v1 failure)

1. **At most 8 words of on-screen copy per frame**, not counting chart labels and code. The visual
   carries the frame. No paragraphs on screen.
2. **Presenter lines are hidden by default.** Put them in a sidecar `<slug>.notes.md` AND in a
   key-toggled overlay (press `N`). Nothing for Mauro to read is visible on a recording.
3. **Zero placeholders on screen.** No dashed SCREEN boxes. Where no capture exists, the board itself
   is the visual: a rendered repo tree, an inline SVG chart, a table, a diagram, a mock UI built in
   HTML. Real assets you may use: `research/video-knowledge/assets/repo-tree-screen-safe.txt`,
   images already in the repo. Never a generated image that a viewer reads as proof.
4. **Length: 20 to 25 minutes.** Structure: hook (0:00-0:30), 3 deep sections, each with one worked
   example and a before/after, then the CTA. Aim for 22-30 frames. Write the timing per frame in the notes.
5. **The hook names what is on screen in the first 30 seconds**, opens with the result first, then
   the promise, then a "today we go over" list of the 3 sections.
6. **Titles: 3 per video.** Each title names the row it copies the shape from: a `01-outliers.csv`
   row (channel + title) or a `charlie-morgan-dig.md` entry. The CSV is AI-automation channels. For
   topics outside it (X algorithm, YouTube process, content attribution, AEO), use WebSearch to find
   2-4 real outlier videos in that niche (title, channel, views) and cite them. Write no unanchored title.
   Titles under 60 characters where you can.
7. **Thumbnails: 3 per video** in one `<slug>.thumbs.html` (each 1280x720), plus a PNG render. A
   face slot is allowed as the only placeholder (Mauro's face goes there). Max 4 words on a thumbnail.
8. **CTA**: the frame says "Link in the description" plus the offer name "Agency Booked Calls". No
   price, no URL.

## Content rules (non-negotiable)

- **`$300k/mo` is OUT of every title, frame and thumbnail.** The video-knowledge README says it is
  pre-cleared. That README is stale on this point: ignore it. It is the agency's number, and
  `positioning.md` forbids borrowing the agency's anchors as Mauro's proof.
- **Numbers only from `brand/claims.md`.** A number that is not there, or is marked "needs sign-off",
  renders as a visible red `[NEEDS: x]` tag on the frame. Never estimate, never drop silently.
  Known offenders: doc 03 "4 of 541", doc 08's dataset (it comes from the agency's account, so each
  panel carries a source label "the agency I run").
- **No client names, no account names, no brand names of clients.** No "Growthub", no "Lorenzo".
  Say "the agency I run".
- **No em dashes** anywhere in on-screen copy, notes or titles. No "not X, Y" contrast lines.
- Never invent descriptive detail. A gap gets `[NEEDS: x]`.

## Mechanics

- Self-contained HTML: inline CSS, inline SVG, inline JS. External requests allowed only for Google
  Fonts. A double-click must work.
- Keyboard: right/left arrow or space to move between frames, `N` toggles notes, `F` fullscreen.
  Frames are 16:9 and fill the viewport.
- Render PNG previews with headless Chrome
  (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless --screenshot`):
  `<slug>.cover.png` (frame 1 at 1600x900) and `<slug>.thumbs.png`. Check each PNG with the Read tool
  and fix what looks broken (overflow, overlap, unreadable text).
- Write ONLY inside `boards/yt/v2/<your-format>/`. Do NOT commit or push. The parent commits once.
- File names: `NN-slug.html`, `NN-slug.notes.md`, `NN-slug.thumbs.html`, `NN-slug.cover.png`,
  `NN-slug.thumbs.png`, where NN is the video-knowledge doc number. Also a `meta.json` in your folder:
  `[{"doc": "11", "file": "...", "titles": [{"title": "...", "modelled_on": "..."}], "frames": 26,
  "minutes": 23, "needs": ["..."]}]`.

## Your final report (short)

Files built, frame count and minutes per board, the 3 titles per board with their source row, every
`[NEEDS]` left, and anything in the source docs that conflicts with claims.md.
