# Video Board Corrections — one section = one screen

Addendum to `mauro-visual-doc-system.md`, **Type 2 · BOARDS only.** Use this whenever a board
will be **screen-recorded for a video** (YouTube walkthroughs), not just exported as a static PDF/PNG.

It fixes two problems that only show up on camera:

1. **Section bleed.** While recording section 1, part of section 2 peeks into the frame. We want
   one section to own the screen at a time.
2. **Screenshots break the layout.** Pasted-in images (a tweet screenshot, an account grab) are
   different sizes and push content off the frame.

The base board rules (palette, typography, voice, blocks, image handling) still apply. This only
changes the **layout container** and adds a recording discipline. It stays compatible with
`render_one.py ... board` — a video board still exports as one tall PDF + PNG.

---

## The core idea: frames

Every major section goes inside a **`.frame`** that is at least one screen tall, with its content
vertically centered, plus **scroll-snap** on the page. Result:

- One section fills the recording viewport. Empty space above/below it hides the neighbors.
- Scroll-snap is **mandatory + stop-always**, so scrolling lands exactly on the next frame's top.
  You physically cannot park the view halfway between two sections. No bleed, ever.
- Images are height-capped so a big screenshot can't grow a frame past one screen.

A "section" is one idea: the title, one HEADER-CARD with its item cards, one screenshot with its
caption, one flow. If it doesn't fit in a single screen, it's **two frames**, not one crowded one.

---

## CSS — paste this into the board's `<style>` (in addition to the base board CSS)

```css
:root {
  /* Height of one recording screen. Default follows the browser window (100vh).
     To PIN it to your recorder, set a pixel value, e.g. 1080px for a 1920x1080 capture,
     or 1920px for a 1080x1920 vertical capture, then record at that exact height. */
  --frame-h: 100vh;
}

/* The page itself is the scroll-snap container */
html {
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
}

/* Hide the scrollbar so it never shows in the recording (still scrollable) */
html { scrollbar-width: none; }            /* Firefox */
html::-webkit-scrollbar { display: none; } /* Chrome/Edge/Safari */

/* One section = one screen */
.frame {
  min-height: var(--frame-h);
  scroll-snap-align: start;
  scroll-snap-stop: always;      /* can't skip past or stop between frames */
  display: flex;
  flex-direction: column;
  justify-content: center;       /* content centered in its screen -> neighbors off-frame */
  align-items: center;
  padding: 72px 100px;
  box-sizing: border-box;
}

/* Keep the branded column at 1080 wide, centered on the cream background */
.frame > .inner { width: 100%; max-width: 940px; }

/* Any image inside a frame is capped so it can never blow past one screen.
   60vh leaves room for a title/caption above or below it. */
.frame img,
.frame .shot {
  display: block;
  margin: 0 auto;
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 60vh;
  object-fit: contain;
  border-radius: 12px;
  border: 1px solid #D8CFBB;
}

/* Reserved blank space in a frame. NO visible box, NO label. Just empty room,
   sized in vh so it always fits one frame on any recording resolution.
   Leave it empty and it reads as clean whitespace. Drop an <img class="shot"> or
   type text inside it whenever you need to fill it. */
.slot {
  display: flex; align-items: center; justify-content: center;
  text-align: center; max-width: 100%;
}
.slot--tweet { min-height: 46vh; } /* room for a tweet / wide screenshot */
.slot--wide  { min-height: 44vh; } /* room for a landscape screenshot / dashboard */
.slot--tall  { min-height: 62vh; } /* room for a phone / vertical screenshot */
.slot--square{ min-height: 52vh; } /* room for a product shot / square image */

/* DEBUG: add class="debug" to <body> while editing to see every frame boundary.
   Remove it before you record. */
body.debug .frame { outline: 2px dashed #E9B949; outline-offset: -2px; }
```

Everything else (`.header-card`, `.item-card`, `.pill`, `.intro-bar`, `.flow`, colors, fonts)
comes straight from the base board CSS in `mauro-visual-doc-system.md`. Do not restyle it here.

---

## HTML skeleton — a video board

Each `<section class="frame">` is one screen. Content goes in an `.inner` wrapper so it stays in
the 940px column while the frame fills the width.

```html
<!doctype html>
<html><head><meta charset="utf-8">
<style>
  /* 1) base board CSS from mauro-visual-doc-system.md  2) the video CSS above */
</style></head>
<body>

  <!-- FRAME 1 · title -->
  <section class="frame">
    <div class="inner" style="text-align:center;">
      <div class="doc-title">Breakdown title</div>
      <div class="doc-sub">one-line frame for the video</div>
      <div class="flow">
        <div class="node">How to Scale</div>
        <div class="arrow">&#9660;</div>
        <div class="node">More <span class="hl">Winning</span> Ads</div>
      </div>
    </div>
  </section>

  <!-- FRAME 2 · a section with room for a screenshot -->
  <section class="frame">
    <div class="inner">
      <div class="header-card"><h2>The tweet that started it</h2>
        <div class="sub">problem aware</div></div>
      <!-- blank reserved space. Paste an image or type text inside when you need it:
           <img class="shot" src="images/tweet-1.png" alt="">   or   any text/HTML -->
      <div class="slot slot--tweet"></div>
    </div>
  </section>

  <!-- FRAME 3 · a section with item cards (keep it to what fits one screen) -->
  <section class="frame">
    <div class="inner">
      <div class="header-card"><h2>New Formats</h2>
        <div class="sub">break the 1-format wall</div></div>
      <div class="item-card">
        <span class="pill">PROBLEM AWARE</span>
        <h3>UGC / real-customer reaction <span class="tag-win">WINNING</span></h3>
        <p class="quote">"Skeptic-converted arc, adds social proof in-feed."</p>
      </div>
      <div class="item-card">
        <h3>Screen-recording walkthrough</h3>
        <p>The report and morph reveal. Product as the creative.</p>
      </div>
    </div>
  </section>

  <!-- FRAME 4 · room for a full landscape screenshot -->
  <section class="frame">
    <div class="inner" style="text-align:center;">
      <!-- blank reserved space; drop <img class="shot" src="images/account.png"> here -->
      <div class="slot slot--wide"></div>
    </div>
  </section>

</body></html>
```

### Filling a blank space

A `.slot` renders as **empty whitespace** until you put something in it. It's just reserved room,
not a box. When you need to fill it:

- **An image:** drop the file into `./images/`, then put `<img class="shot" src="images/x.png" alt="">`
  inside the slot. The `max-height: 60vh` cap shrinks an oversized grab to fit instead of blowing
  the frame.
- **Text:** type it straight into the slot (a line, a quote, an `.item-card`, whatever fits).
- **Nothing:** leave the slot empty. It stays clean blank space, no border, no label.

---

## Recording recipe

1. Open the HTML in the browser. Press **F11** (fullscreen) so there's no browser chrome.
2. Leave zoom at 100%. At `--frame-h: 100vh` one frame already equals the window height.
3. Move section to section with **Page Down / Space / arrow down** — scroll-snap lands on the next
   frame's top. **Do not free-scroll with the wheel** mid-section.
4. The 1080 column sits centered on the cream background; on a 16:9 landscape capture you'll get
   cream margins left/right, which is on-brand. If you want the column edge-to-edge, record a
   vertical (9:16) frame instead.
5. To pin exact framing: set `--frame-h` to your capture height (e.g. `1080px`) and size the
   recording area to match. Then every frame is an exact, repeatable screen.

---

## The one rule that keeps it clean

**A frame must fit in one screen.** If content is taller than the viewport, snap can't hide the
overflow and the next section will peek. When a section is too big:

- Split it into two frames (e.g. header + first 2 cards on one, next 2 cards on the next), or
- Cut copy, or
- Rely on the `max-height: 64vh` image cap (already handles oversized screenshots).

**Check before recording:** add `class="debug"` to `<body>`, scroll through, and confirm each
dashed honey outline is exactly one screen tall with nothing spilling past it. Remove `debug`
before you record.

---

## QC additions (on top of the base board checklist)

- [ ] Every section is wrapped in a `.frame` with an `.inner`
- [ ] `scroll-snap-type: y mandatory` on `html`, `scroll-snap-align: start` + `scroll-snap-stop: always` on `.frame`
- [ ] With `body.debug`, no frame's content spills past its one-screen outline
- [ ] Empty `.slot`s read as clean blank space (no visible box, no label); filled ones don't overflow
- [ ] Scrollbar hidden; recorded in fullscreen; navigated with Page Down (not free-scroll)
- [ ] `--frame-h` matches the capture height if pinning exact framing
- [ ] Still passes the base board QC (palette, fonts, voice sweep, handle/footer, CTA points to X)

---

## Note on the static export

`python3 render_one.py deck.html board` still works: each `.frame` becomes a tall section
(headless viewport is 1080×1400, so `100vh` = 1400px per frame) and the whole thing exports as one
continuous PDF + PNG. The video frames and the static deliverable come from the same file.

If you ever want **each frame exported as its own image** (for hard cuts in the edit instead of a
scroll), that's a separate render mode — ask and we'll add a `frames` mode to the pipeline as its
own small skill.
