# Mauro Visual Doc System

How Mauro (@maurojpelle) builds branded visual content as HTML → PDF + PNG. One render engine, **two output types.** Pick which one you're making before anything else.

---

## THE TWO TYPES (read this first)

### Type 1 · SOCIAL HTML — for LinkedIn + X

Fixed-size branded infographic pages. The polished, on-brand assets that go straight into a post: X quote-tweet infographics, LinkedIn document carousels, single punch graphics. Green brand palette. Rendered as fixed dimensions (square / portrait / long) so they fit the feed exactly.

This is the format behind the quote-tweet play: post the article, wait a few hours, quote-tweet it with an HTML infographic that maximizes dwell time.

- Dimensions: `square` 1080×1080, `portrait` 1080×1350, `long` 1080×1620
- Palette: green brand
- Output: `deck.pdf` (carousel) + `deck-p1.png`, `deck-p2.png` (per page)
- Render: `python3 render_one.py deck.html portrait`

### Type 2 · BOARDS — spacious, editable breakdown boards

A long vertical board with plenty of room, built to be **edited and screen-recorded.** The "Miro breakdown" look, composed from a real component set (tables, stat tiles, compare columns, grids, timelines, clean SVG connectors, image slots), color-coded section by section, with almost no prose so it reads on screen while Mauro narrates. Used for YouTube walkthroughs and analysis breakdowns.

Built to be worked on: swap a label, reorder sections, drop new images in, re-render. One continuous tall page, any height, high quality.

- Dimension: `board` (1080 wide, natural height, single continuous page)
- Palette: cream ground, green as the brand anchor, sections color-coded across a small accent set (green / clay / slate), honey for the one thing that must pop
- Text: sparse. Labels and anchors, not sentences. Mauro says the detail on camera.
- Structure: varies section to section. Never the same card stack repeated down the page.
- Output: `deck.pdf` (one tall page) + `deck.png` (one tall image)
- Render: `python3 render_one.py deck.html board`

**Both types share** the same render script, typography, and voice rules, so everything reads as one brand across X, LinkedIn, and YouTube.

---

## When to use this skill

- X article or video script → styled social carousel or single infographic (Type 1)
- Single QT-reaction visual alongside an article (Type 1)
- Long breakdown board to screen-record in a YouTube video, with your own images dropped in (Type 2)
- Brand banner for a cover / lead magnet / hero (banner asset class, below)

Do NOT use for: short text-only posts, video scripts, image-only carousels with no layout.

---

## Brand

One owner: **Mauro, @maurojpelle.** No second brand variant.

### Brand foundation

Cream/white ground, green as the brand anchor, plus a small disciplined accent set so boards aren't monotone. Green still dominates; the accents color-code sections and components so a long board reads as distinct chapters instead of one green wall.

**Core (both types):**

| Name | Hex | Role |
|---|---|---|
| Cream | `#F7F3EA` | Board background |
| White | `#FFFFFF` | Social background + card fills |
| Deep Forest | `#1B4332` | Primary text, borders, dark fills, brand anchor |
| Sage | `#52B788` | Green accent, connectors, badges, handle, links |
| Pale Mint | `#B7E4C7` | Section stickers, intro bars, light fills |
| Mint | `#D8F3DC` | Green-section card fills |
| Ink | `#1B1B1B` | Body text on light cards |
| Muted | `#5F6B62` | Sub-labels, captions |

**Board accent families (Type 2 — rotate ONE per section, never two adjacent the same):**

| Family | Header fill (white text) | Card tint (Ink text) | Border / pill / number |
|---|---|---|---|
| Forest (brand default — open + close on it) | `#1B4332` | `#D8F3DC` | `#1B4332` |
| Clay | `#C15F3C` | `#F7DFD3` | `#C15F3C` |
| Slate | `#3F5E77` | `#DDE7EF` | `#3F5E77` |

**Emphasis pop (both types):** Honey `#E9B949` with Ink text. One or two touches per board, max: a `WINNING`-style tag, one highlighted stat, an underline on a key word. Never a section color, never a background wall.

**Handle:** `@maurojpelle` (Sage) · **Footer:** `— Mauro` (left-aligned, above a thin Deep Forest divider). Optional on boards.

### How the two types use it

- **Social (Type 1):** white background, green blocks (Pale Mint stickers, Sage badges, Deep Forest callouts). The accent families are available for section variety, but green is the default. Honey only when one thing must pop.
- **Boards (Type 2):** cream background (faint grid optional). Each section picks ONE accent family and applies it to that section's header bar, card tint, border, and pill. The next section uses a different family. Open and close on Forest, vary in between. This color-coding is what keeps a long board from reading as a green wall.

### Critical color rules

- **Rotate section accents.** No two adjacent sections share a family. An all-Forest board is the exact mistake this rule exists to prevent.
- **Never use Pale Mint, Mint, Honey, or any card tint as text on cream/white.** They are fills, never text on a light ground.
- **Honey is a garnish, not a base.** One or two touches per board. Carrying a whole card or background = wrong.
- Header fills (Forest / Clay / Slate) always use white text. Card tints always use Ink text.

---

## Typography

**Fonts:** Inter (body + headings), JetBrains Mono (mono pills, labels, header-card subtitles, code-style callouts). Handwriting / display fonts banned. No Caveat.

**Social scale (portrait 1080×1350 default):** H1 42-50px/800 · subtitle 18-21px · handle 16-18px Sage · section sticker 26-30px/800 · body 15-17px/1.55 · card title 18-22px/800 · mono labels 10.5-12px/700 uppercase · stat numbers 26-36px/800 Sage · footer 13-14px.

**Board scale (board, 1080 wide, big and sparse):** doc title 46-56px/800 · header-card title 28-32px/800 centered · header-card subtitle 15-16px mono · card title 22-26px/700 · card support line 17-19px (one line, optional) · stat-tile number 44-64px/800 accent · table cell 16-18px · pill 11-13px/700 mono uppercase · caption 13-14px Muted.

**Recordability rule (hard).** Boards are screen-recorded while Mauro talks, so the board carries labels, not sentences. Enforce it:

- Every card = a title plus at most ONE short support line (≤ 10 words). No paragraphs. If it needs a paragraph, that's Mauro's talking point on camera, not board text.
- One idea per block. One accent family per section.
- Type stays big (nothing under ~16px). Height is free, so use whitespace; never shrink type to cram more words.
- More than ~5 short items in a section means it's two sections or a table, not a longer stack.
- Gut check: from six feet back, can you read every word on screen? If not, cut words, don't shrink type.

**Length + coverage rule (hard).** A board is B-roll for a whole video, so it scales to the source and the target runtime. It does NOT compress the source into a summary. This is the opposite failure from the recordability rule, and both are true at once: few words per beat, many beats.

- **One beat per distinct point in the source.** A 7-minute Q&A holds ~10-12 separate points; each becomes its own section or component. Keep every one. Never merge them into a single page.
- **Scale to runtime.** Aim for roughly one visual beat per 30-45s of finished video, so there's always a fresh cut to make. An 8-minute video wants ~10-16 beats.
- **"Sparse" governs words inside a beat, never the number of beats.** Strip the sentence down to a label; never drop the point.
- A 12-answer Q&A becomes a ~12-section board, and it gets long. That is correct. Height is free; length is the point.
- **Failure mode this prevents:** 7 minutes of content rendered as one short page. If the board is shorter than the video it feeds, it is wrong. When source is thin for the target length, tell Mauro the board is short rather than padding it with filler.
- Accent families keep rotating across a long board (Forest → Clay → Slate → repeat); components keep varying. A 12-beat board should never be 12 identical cards.

---

## Recurring blocks — TYPE 1 · SOCIAL (green, paged)

Compose social docs from this library. Pick the block that fits; don't invent unless none fit.

- **SECTION-H** · Pale Mint inline-block section header, Deep Forest text.
- **INSIGHT-BOX** · Deep Forest fill, Pale Mint text, Sage left bar, mono Sage label. One per page.
- **TABLE-3** · label + body grid, rotating Pale Mint / Sage / Mint fills.
- **TABLE-COMPARE** · wrong-vs-right, muted header vs Sage header, light-tint body cells.
- **MATH-BAR** · Mint fill, Deep Forest border, mono; payoff number in Sage.
- **STEP-ROW** · Sage number badge + white body cell.
- **FORMAT-CARD** · 2.5px Deep Forest border, colored header bar, white body.
- **CTA-BLOCK** · Pale Mint fill, "DM me [keyword]" bolded. Public posts only.
- **PLAY-CARD / PATTERN-CARD / SIGN-CARD / MATRIX-WRAP / STAT-CARD-ROW / BEAT-ROW** · the structural cards (numbered plays, quoted-example patterns, TEST/DIAGNOSIS/FIX diagnostics, 2×2 matrices, stat rows, sequential beat flows), recolored to green. Use whichever matches the framework's actual shape.

Dimensions: `square` for tight 3-card / QT reactions, `portrait` (default) for article-length and playbooks, `long` for content-dense single pages. Padding `55-65px / 65-75px`.

---

## Recurring blocks — TYPE 2 · BOARDS

Compose each section from the block that fits its content. **Vary it:** a comparison is a 2-col or a table, numbers are stat-tiles, a sequence is a timeline, a matrix is a grid, a plain list is item-cards. Consecutive sections should look different AND use different accent families. Everything is centered in an ~880-940px column inside the 1080 canvas.

**The variety rule (hard):** never build a board as the same header→item-cards stack repeated for every section. That is the failure mode this section exists to prevent. Before drafting, assign each section a component and an accent family, and confirm no two neighbors match on either.

**Structure / flow**

- **DOC-TITLE** · big Ink title at the top + one short subtitle. No card.
- **HEADER-CARD** · full-width bar in the section's accent (white text) + optional mono subtitle. Opens each section, connected to what follows by a clean connector.
- **CONNECTOR** · clean SVG, never a text glyph like `▼`. Variants: straight down-arrow, elbow (turns a corner), split (one-to-many branch), labeled (a word riding the line). 2px stroke in the section accent, triangle arrowhead. Snippets in the skeleton.
- **CALLOUT** · one full-width accent bar holding the single line that matters in a section. Big type. Once per section, max.

**Content components (pick one per section, rotate)**

- **ITEM-CARD** · card-tint fill, 2px accent border, a title + at most one short line. Optional accent PILL top-left. Stack 3-5, no more.
- **TABLE** · 2-4 columns, accent header row (white text), alternating cream/white body rows, short cells only. For criteria matrices, feature grids, awareness-by-format.
- **STAT-TILES** · row of 2-4 tiles, each a big accent number + a tiny label. Lead a section with magnitude.
- **COMPARE-2COL** · two columns with accent headers (Before/After, Old/New, Them/You), 2-4 short bullets each.
- **GRID** · 2×2 or 3-up cards for a framework or parallel options. Each cell a short label + one line.
- **TIMELINE / STEP-RAIL** · numbered steps on a connecting rail (vertical or horizontal), accent number badges. For sequences and workflows.
- **AWARENESS-PILL** · accent pill, white mono uppercase (`PROBLEM AWARE`, a category, a step), top-left inside a card.

**Images (your paste-ins)**

- **IMAGE-FULL** · full-width `<img>`, rounded, optional caption. Primary paste-in slot.
- **IMAGE-GRID** · 2-5 images in a row (the ad-thumbnail look), optional label to the left.
- **IMAGE-INLINE** · short label block beside an image.
- **SECTION-DIVIDER** · vertical breathing room + optional thin rule.

### Image handling (how paste-in works)

Reference images with **relative paths** and keep them in an `images/` folder next to the HTML:

```html
<img src="images/account-screenshot.png" alt="">
```

Drop files into `./images/` before rendering. `render_one.py` loads over `file://`, so relative paths resolve. To swap or reorder, change the `src`, drop the new file in, re-render. No base64. Leave a dashed placeholder box sized to the image anywhere a file isn't ready, so the layout still reads.

---

## Board HTML skeleton

Starting point for a `board`. Copy, fill, drop images in `./images/`, render with `python3 render_one.py deck.html board`.

Note how each `.section` sets its own accent family and uses a different component. Copy it, keep the rotation, keep the text sparse.

```html
<!doctype html>
<html><head><meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&family=JetBrains+Mono:wght@400;700&display=swap');
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    font-family:'Inter',sans-serif; color:#1B1B1B;
    background:#F7F3EA;   /* cream */
    background-image:
      linear-gradient(#ECE6D8 1px, transparent 1px),
      linear-gradient(90deg, #ECE6D8 1px, transparent 1px);
    background-size:54px 54px;   /* faint grid. delete these 3 lines for plain cream */
  }
  .doc { width:1080px; margin:0 auto; padding:90px 100px; }
  .doc-title { font-size:54px; font-weight:800; letter-spacing:-1px; color:#1B4332; }
  .doc-sub { font-size:19px; color:#5F6B62; margin-bottom:36px; }

  /* ONE accent family per section: set --accent + --tint on .section, then rotate */
  .section { max-width:760px; margin:26px auto; }
  .section.forest { --accent:#1B4332; --tint:#D8F3DC; }
  .section.clay   { --accent:#C15F3C; --tint:#F7DFD3; }
  .section.slate  { --accent:#3F5E77; --tint:#DDE7EF; }

  .header-card { background:var(--accent); border-radius:12px; padding:22px 30px; text-align:center; }
  .header-card h2 { font-size:30px; font-weight:800; color:#fff; }
  .header-card .sub { font-family:'JetBrains Mono',monospace; font-size:15px; color:#fff; opacity:.8; margin-top:3px; }

  /* clean SVG connectors (inherit the section accent via var) */
  .conn { display:block; margin:6px auto; }
  .conn line, .conn path { stroke:var(--accent,#1B4332); stroke-width:2; fill:none; }
  .conn polygon { fill:var(--accent,#1B4332); }

  .item { background:var(--tint); border:2px solid var(--accent); border-radius:12px; padding:20px 26px; margin:12px 0; }
  .item .pill { display:inline-block; background:var(--accent); color:#fff; font-family:'JetBrains Mono',monospace;
    font-size:12px; font-weight:700; letter-spacing:1.5px; padding:4px 11px; border-radius:6px; margin-bottom:10px; }
  .item h3 { font-size:24px; font-weight:700; color:#1B1B1B; }
  .item p  { font-size:18px; color:#33413B; margin-top:4px; }

  .tiles { display:flex; gap:14px; }
  .tile { flex:1; background:#fff; border:2px solid var(--accent); border-radius:12px; padding:20px; text-align:center; }
  .tile .n { font-size:56px; font-weight:800; color:var(--accent); line-height:1; }
  .tile .l { font-size:14px; color:#5F6B62; margin-top:6px; }

  table { width:100%; border-collapse:collapse; border-radius:12px; overflow:hidden; }
  th { background:var(--accent); color:#fff; font-size:15px; text-align:left; padding:12px 16px; }
  td { background:#fff; font-size:17px; padding:12px 16px; border-top:1px solid #EAE3D4; }
  tr:nth-child(even) td { background:#FBF8F1; }

  .compare { display:flex; gap:14px; }
  .col { flex:1; border:2px solid var(--accent); border-radius:12px; overflow:hidden; }
  .col .h { background:var(--accent); color:#fff; font-weight:700; padding:12px 16px; font-size:16px; }
  .col ul { list-style:none; padding:12px 16px; }
  .col li { font-size:17px; padding:5px 0; }

  .callout { background:var(--accent); color:#fff; border-radius:12px; padding:24px 30px;
    font-size:25px; font-weight:700; text-align:center; }

  /* honey emphasis, sparing */
  .tag-win { display:inline-block; background:#E9B949; color:#1B4332; font-family:'JetBrains Mono',monospace;
    font-size:11px; font-weight:700; letter-spacing:1px; padding:3px 9px; border-radius:5px; margin-left:8px; }
  .hl { border-bottom:3px solid #E9B949; }

  .img-full { max-width:760px; margin:26px auto; text-align:center; }
  .img-full img { width:100%; border-radius:12px; border:1px solid #D8CFBB; }
  .img-grid { display:flex; gap:12px; max-width:760px; margin:26px auto; }
  .img-grid img { flex:1; border-radius:8px; border:1px solid #D8CFBB; min-width:0; }
  .caption { font-size:13px; color:#5F6B62; text-align:center; margin-top:8px; }
  .placeholder { border:2px dashed #B7A98A; border-radius:12px; min-height:200px; max-width:760px; margin:26px auto;
    display:flex; align-items:center; justify-content:center; color:#9A8E72; font-family:'JetBrains Mono',monospace; font-size:14px; }

  .footer { text-align:center; margin-top:56px; color:#1B4332; font-size:14px; opacity:.7; }
</style></head>
<body>
  <div class="doc">
    <div class="doc-title">How to scale winning ads</div>
    <div class="doc-sub">the loop, start to finish</div>

    <!-- SECTION 1 · Forest · item cards (short list) -->
    <div class="section forest">
      <div class="header-card"><h2>New Formats</h2><div class="sub">break the 1-format wall</div></div>
      <svg class="conn" width="26" height="38" viewBox="0 0 26 38">
        <line x1="13" y1="0" x2="13" y2="26"/><polygon points="6,25 20,25 13,38"/>
      </svg>
      <div class="item"><span class="pill">UGC</span><h3>Real-customer reaction <span class="tag-win">WINNING</span></h3><p>Skeptic-to-convert arc.</p></div>
      <div class="item"><span class="pill">SCREEN REC</span><h3>Walkthrough</h3><p>Product as the creative.</p></div>
      <div class="item"><span class="pill">FOUNDER</span><h3>Direct to camera</h3><p>Raw, ties to the CEO angle.</p></div>
    </div>

    <!-- SECTION 2 · Clay · stat tiles (lead with numbers) -->
    <div class="section clay">
      <div class="header-card"><h2>The gap today</h2></div>
      <div class="tiles">
        <div class="tile"><div class="n">1</div><div class="l">format running</div></div>
        <div class="tile"><div class="n">0</div><div class="l">female-targeted</div></div>
        <div class="tile"><div class="n">3</div><div class="l">angles untested</div></div>
      </div>
    </div>

    <!-- SECTION 3 · Slate · table -->
    <div class="section slate">
      <div class="header-card"><h2>New angles</h2><div class="sub">by awareness</div></div>
      <table>
        <tr><th>Angle</th><th>Awareness</th></tr>
        <tr><td>Second opinion</td><td>Problem</td></tr>
        <tr><td>Founder reads every report</td><td>Product</td></tr>
        <tr><td>Progress tracker</td><td>Most</td></tr>
      </table>
    </div>

    <!-- SECTION 4 · Forest · 2-col compare -->
    <div class="section forest">
      <div class="header-card"><h2>Old vs new</h2></div>
      <div class="compare">
        <div class="col"><div class="h">Old</div><ul><li>1 format</li><li>1 persona</li><li>Guessing</li></ul></div>
        <div class="col"><div class="h">New</div><ul><li>5 formats</li><li>3 personas</li><li>Tested</li></ul></div>
      </div>
    </div>

    <!-- paste-in image + a not-ready placeholder -->
    <div class="img-full"><img src="images/account.png" alt=""><div class="caption">The account, mid-scroll.</div></div>
    <div class="placeholder">images/landing-page.png</div>

    <!-- SECTION 5 · Clay · callout (the one line that matters) -->
    <div class="section clay">
      <div class="callout">Volume without a map is guessing with a bigger budget.</div>
    </div>

    <div class="footer">@maurojpelle</div>
  </div>
</body></html>
```

Five sections, three accent families rotated (forest → clay → slate → forest → clay), five different components (item-cards, stat-tiles, table, compare, callout), clean SVG connector, sparse text throughout. That is the target, not a repeated card stack. Other connector variants (swap the `<svg>` innards):

```
<!-- elbow: down, across, down -->
<svg class="conn" width="200" height="60" viewBox="0 0 200 60"><path d="M20 0 V30 H180 V52"/><polygon points="173,50 187,50 180,60"/></svg>
<!-- split: one to three -->
<svg class="conn" width="360" height="60" viewBox="0 0 360 60"><path d="M180 0 V20 M40 40 V20 H320 V40 M180 20 V40"/><polygon points="33,38 47,38 40,50"/><polygon points="173,38 187,38 180,50"/><polygon points="313,38 327,38 320,50"/></svg>
```

Everything scrolls in one column. The renderer measures total height and outputs one tall PDF + one tall PNG.

---

## Voice rules

**`brand/voice.md` is the gate.** Read it before writing any board or social copy. This section is the render-time checklist; when the two differ, `brand/voice.md` wins. Applies to every word in every doc, both types. Quoted real ad copy or real customer quotes pass through as-is.

### Hard-banned constructions (grep-sweep before every render)

- **Off-voice slang (see `brand/voice.md`).** Notably **"clock / clocks"** as slang for detecting AI ("prospects clock it", "nobody clocks the output") — use "spot", "catch", or "can tell". Mauro does not talk like this.

- **Em dashes (`—`)** in body. Replace with commas, periods, colons, or restructure. Only allowed em dash is the footer `— Mauro`.
- **"Not X but Y" / "It's not X. It's Y." / "X, not Y." / "X rather than Y." / "X instead of Y." / "X, never Y."** State Y directly.
- **"Most [group] does X."** Preacher opener. Reframe to the observation or principle. ("the most X" superlative is fine.)
- **Two-sentence X/Y contrast.** Fold into one statement.
- **Three-fragment staccato** ("Bigger. Faster. Cheaper."). Fold into a sentence. Bulleted lists are fine.
- **Hot-take openers**, **hype adjectives** ("insane", "wild", "game-changing"), **generic openers** ("Here's the thing / the truth").
  - Exception: the proven "Claude is INSANE for [X]" auto-DM opener is a deliberate hook, not body prose.
- **Trailing summary / moral one-liners.** End on the point.
- **Stacked questions.** One question per CTA.

### Standard grep sweep

```bash
grep "—" file.html | grep -v "Mauro\|<title>\|<!--\|/\*"
grep -nE "[Ii]t's not |[Nn]ot a |[Nn]ot just |, not [a-z]+\.|[Nn]ot [A-Z][a-z]+ but|rather than [a-z]+|, never [a-z]+\.|instead of [a-z]+\." file.html | grep -v "compare-cell\|<!--\|pill\|label"
grep -nE "[Mm]ost [a-z]+ [a-z]+ [a-z]+" file.html | grep -v "compare-cell\|<!--"
grep -nE "[A-Z][a-z]+\. [A-Z][a-z]+\. [A-Z][a-z]+\." file.html | grep -v "compare-cell\|<!--"
grep -niE "\bclock(s|ed|ing)?\b" file.html | grep -viE "o'clock|clockwise"   # off-voice slang for "detect"
```

When a violation hits, **fix every instance of that pattern across the whole doc**, not just the flagged one.

### Numbers rule

Never invent a performance number. Real numbers from source only, or a bracket placeholder like `[X%]`. Only pre-approved public number: Growthub ~$300k/mo. Anything else specific needs Mauro's sign-off before it goes in a doc.

---

## CTA handling

- **X / social public posts:** end with the CTA block, "DM me [keyword]" bolded.
- **YouTube boards:** the CTA points to X (DM me on X), never "subscribe / stay on YouTube." YouTube is top-of-funnel; conversion happens on X.
- **QT reactions:** the visual carries the reframe, the article carries the CTA. No separate CTA.
- **Private / internal:** no CTA, end on the footer or nothing.

---

## Workflow per new doc

1. **Pick the type.** Type 1 SOCIAL (green, paged) or Type 2 BOARD (warm, long-scroll, editable)? Public or private?
2. **Pick the dimension.** `square` / `portrait` / `long` for social; `board` for breakdowns.
3. **Outline the structure.** Social: map sections to pages. Board: first pull EVERY distinct point out of the source (one beat each, don't summarize) and check the beat count against the target video runtime (~1 beat per 30-45s; 8 min → ~10-16 beats). Then assign each beat a component (table / stat-tiles / compare / grid / timeline / item-cards / image / callout) and a rotating accent family, confirm no two neighbors match on either, and write the sparse labels (not sentences). Never the same card stack twice, never collapse the source into one page.
4. **Copy the matching skeleton / closest existing doc.** Boards start from the skeleton above.
5. **Write body content** to `brand/voice.md` and the voice rules here (hard constraints). On boards this means labels, not sentences.
6. **Drop images** into `./images/` (boards). Dashed placeholders for any not ready.
7. **Run the grep sweep.** Fix every hit before rendering.
8. **Render.** `python3 render_one.py deck.html portrait` (social) or `... board` (board). Banners: inline 1500×600.
9. **QA the output.** Social: no overflow, PNG dims exact. Board: image paths resolve (or intentional placeholders), no dead gaps, column centered. Fonts loaded, colors right, handle + footer right.
10. **Ship** HTML + PDF + PNG(s). Nothing publishes without Mauro's sign-off.

---

## Quality check before sending

- [ ] Ran `brand/voice.md` banned-words check (incl. "clock/clocks")
- [ ] No em dashes in body (footer only)
- [ ] No contrast cadence ("not X but Y", "X, not Y", "rather than", "instead of")
- [ ] No "Most [group] does X" openers, no three-fragment staccato, no trailing morals
- [ ] No invented numbers (real or `[X%]`; specifics signed off)
- [ ] No handwriting / Caveat fonts
- [ ] Type 1: page count matches plan, no page >30% bottom whitespace, PNG dims exact
- [ ] Type 2: all image `src` paths resolve (or intentional dashed placeholders), no dead gaps, column centered
- [ ] Type 2: every distinct point in the source is its own beat (source not compressed into one page)
- [ ] Type 2: beat count fits the target runtime (~1 beat per 30-45s; 8 min → ~10-16 beats)
- [ ] Type 2: reads on screen (every card ≤ a title + one short line, nothing under ~16px, no paragraphs)
- [ ] Type 2: structure varies section to section (not the same card stack repeated)
- [ ] Type 2: accent families rotate, no two adjacent sections the same, opens/closes on Forest
- [ ] Type 2: connectors are clean SVG, not `▼` text glyphs
- [ ] Colors used as fills not text-on-white; Inter body + JetBrains Mono for mono
- [ ] Handle `@maurojpelle`, footer `— Mauro`
- [ ] CTA: social ends "DM me [keyword]"; YouTube points to X; private has none

---

## QT reaction pattern

One square `1080×1080` infographic + a one-line tweet naming the underweighted insight and pointing at the carousel. Pick the single operator-eye-view insight the average reader skims past; build a focused punch visual (math comparison, paired Stop/Start, single-card definition). Not a 3-card breakdown. Lead the carousel with the reaction visual, then the supporting infographics.

---

## Banner asset class (5:2 = 1500×600)

Separate dimension outside the two types. Covers, lead magnet headers, article heroes.

- Top ~30%: Pale Mint band, mono label left + `@maurojpelle` right, heavy Deep Forest bottom border.
- Bottom ~70%: Deep Forest with the title (88px Inter 800 white, max-width 1200px) and subtitle (26px Sage).
- Bottom-right: small Sage accent bar + a mono edition label.

Keep `[TITLE]` / `[SUBTITLE]` as placeholders. Render with a one-off inline `python3 -c '...'` at `W, H = 1500, 600`. Do NOT add a banner mode to `render_one.py`.

---

## Files in this skill family

| File | Purpose |
|---|---|
| `mauro-visual-doc-system.md` | This file. The visual + voice system spec (both types). |
| `render_one.py` | Render pipeline: social (square/portrait/long) + board (long breakdown). |
| `setup-guide.md` | One-time setup: standing up the claude.ai project. |
| `juan-tutorial.md` | VA usage tutorial (how Juan produces docs in the project). |

---

## Render reference

```
python3 render_one.py deck.html square      # 1080x1080 social
python3 render_one.py deck.html portrait    # 1080x1350 social (default)
python3 render_one.py deck.html long        # 1080x1620 social
python3 render_one.py deck.html board       # 1080 x natural height, single tall PDF + PNG
```

Board mode loads over `file://`, measures `document.documentElement.scrollHeight`, and renders one continuous page at 2× device scale so pasted-in images and text stay crisp. Banners stay a one-off inline render at 1500×600.
