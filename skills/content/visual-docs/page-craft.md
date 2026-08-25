# Page Craft — the HTML details that make a doc look designed

Addendum to `mauro-visual-doc-system.md`. That file says *what to build* (types, palette, blocks, voice).
This one says *how to build it well in HTML*, plus how to run the system in a **client's brand** instead
of Mauro's green.

Extracted from a real 2-page doc Mauro produced for Lorenzo (@lorenzo_pravata, GrowtHub) in August 2026.
Reference build: `reference/client-brand-2page.html`. Open it, copy from it, don't rewrite it from scratch.

> **Lane note.** That doc is client work. Its topic (Meta ad creative for DTC) is the agency's lane,
> not Mauro's. The palette, handle, footer, claims and numbers in it are Lorenzo's. Take the *craft*
> from it. Never take the topic, the numbers, or the palette into Mauro's own content.

---

## 1 · The palette contract (this is the upgrade)

The base system hardcoded Mauro's green everywhere, so a client doc meant rewriting every component.
Stop doing that. **Declare the brand once as semantic tokens in `:root`. Below `:root`, no component
ever names a hex.**

```css
:root {
  --ground:    #FFFFFF;  /* page background */
  --ink:       #262151;  /* every heading, every border */
  --body:      #2E2A47;  /* running body text */
  --muted:     #8A8699;  /* captions, footer */
  --dark:      #211E3C;  /* dark callout fill */
  --highlight: #F2CE6B;  /* section header fill + emphasis text on dark */
  --hot:       #E62E8B;  /* number chips, bullets, eyebrow, handle, left bars */
  --mono-dark: #3FDC8F;  /* mono label inside a dark callout */
  --hairline:  #D9D5E2;  /* the footer rule, nothing else */
}
```

| Brand | ground | ink | dark | highlight | hot | mono-dark |
|---|---|---|---|---|---|---|
| **Mauro** (default) | `#FFFFFF` | `#1B4332` | `#1B4332` | `#E9B949` | `#52B788` | `#B7E4C7` |
| **Lorenzo / GrowtHub** | `#FFFFFF` | `#262151` | `#211E3C` | `#F2CE6B` | `#E62E8B` | `#3FDC8F` |

Swapping those six values re-skins the whole doc. That is the test: **if changing `:root` doesn't
fully re-brand the page, a component is cheating with a literal hex. Find it and fix it.**

Board accents (Forest / Clay / Slate) still work the same way, they just move up a level: the section
class sets `--accent` and `--tint`, the tokens above set everything else.

### The role split (why 4 colors don't look busy)

Each color does exactly one job, on every page, without exception:

- **`--highlight`** fills section headers, and is the *text* color inside a dark callout. It is never a
  background behind body copy.
- **`--hot`** only ever appears in small marks: a number chip, a bullet, the eyebrow, the handle, a 7px
  left bar. **Never a fill area wider than ~60px.** This is the whole reason it reads as an accent
  instead of a second brand color.
- **`--dark`** is one callout per page, max. Two dark boxes on one page and neither one lands.
- **`--ink`** is every heading and every border. One color for structure means the page reads as a grid.

Break the role split and the doc immediately looks assembled rather than designed. This is the most
common failure and it is not subtle.

---

## 2 · Components this adds to the library (Type 1 · Social)

Use these alongside the blocks already in `mauro-visual-doc-system.md`. CSS for all of them is in the
reference build.

- **EYEBROW** · mono, uppercase, 2.6px letter-spacing, `--hot`, sits above the H1. Names the *series*
  (`GROWTHUB · CREATIVE PLAYBOOK`), never the doc. 13px. One per carousel, page 1 only.
- **HIGHLIGHT-HEADER** · marker block in `--highlight`, `--ink` text, 32px/800, shrink-wrapped with
  `align-self:flex-start` (see the gotcha in §3).
  Opens every section. **Width follows the text, never full-bleed** — the ragged right edge is the look.
  Every page opens with one, including page 1's second beat. This is what makes pages read as siblings.
- **DARK-CALLOUT** · `--dark` fill, mono label in `--mono-dark`, content in `--highlight`. The label
  names the box's *role* (`WHAT REAL EDUCATIONAL CONTENT HAS`, `WORKED EXAMPLE`), it is not a title and
  it is not a sentence. Two variants: `--bar` (7px `--hot` left bar, for a page-level definition) and
  `--flush` (no bar, when nested inside another bordered block). Arrow list `→` inside, in `--mono-dark`.
- **NUMBERED-BLOCK** · `--ink` 2px border wrapping a two-tone header bar plus a white body. The bar is
  `--highlight`; a `--hot` number chip sits **flush against the border, zero gap, zero radius**, sized by
  `align-items:stretch` so it always matches the bar height even when the title wraps to two lines. That
  one detail is the difference between "built" and "a coloured div next to another coloured div".
- **MINI-CARD ROW** · 3-up bordered cards, each just a mono `--hot` tag plus a bold title. No body copy.
  Works as an index of what the next page covers.
- **BRIDGE LINE** · one bold `--ink` line that closes a page by naming what the next page does
  ("An educational ad reads as boring for one of three reasons. The next page fixes all three.").
- **FOOTER** · 1px `--hairline` rule + the byline in `--muted`, identical on every page.

---

## 3 · Layout mechanics (the HTML part to get right)

**Pin the footer with flex, never with padding.**

```css
.page   { width:1080px; height:1350px; padding:62px 66px 0;
          display:flex; flex-direction:column; }
.footer { margin-top:auto; padding:16px 0 26px; }
```

Fixed page height, column flex, `margin-top:auto` on the footer. The footer lands on the same baseline on
every page no matter how much content sits above it. The page carries `padding-bottom:0` and the footer
owns its own bottom padding. Hand-tuning spacer divs to line footers up is the amateur move and it drifts
the moment copy changes.

**Hold these constant across every page of a doc:**

| Thing | Rule |
|---|---|
| Border radius | Pick one value and use it everywhere. The Lorenzo build is `0` throughout. Sharp cards mixed with rounded ones is the clearest tell of a stitched-together doc. |
| Border weight | `2px --ink` on every card, every block, every mini. `1px --hairline` is reserved for the footer rule alone. |
| Page padding | Same on every page. `62px 66px 0` here. |
| Body measure | `max-width` around `940px` on `p`, inside a `948px` content width, so lines never run the full column. |
| Footer | Byte-identical markup on every page. |

**Bottom whitespace is allowed.** The reference pages end at 952 and 1215 of 1350, so page 1 keeps a
full 20% of air under it. That is correct. A page
that stops when the idea stops reads confident. Stretching type or padding to fill the frame reads
desperate. (The base system's ">30% bottom whitespace" check is a smell test for a page that should merge
with its neighbour, not an instruction to pad.)

**Flex details that carry the numbered block:**

```css
.nblock .bar    { display:flex; align-items:stretch; }   /* chip matches bar height */
.nblock .num    { width:56px; flex:none;                  /* never let it shrink */
                  display:flex; align-items:center; justify-content:center; }
.nblock .bar h2 { align-self:center; padding:14px 22px; } /* title centres, chip stretches */
```

**Two gotchas that bit this exact build:**

1. **`display:inline-block` is ignored on a flex item.** The highlight-header rendered full-bleed
   instead of shrink-wrapping, because a child of `display:flex; flex-direction:column` gets
   `align-self:stretch` by default and the display value is blown away. The fix is
   `align-self:flex-start`, not `inline-block`. Any time a block should hug its text inside a flex
   column, that is the property you want.
2. **A headline that wraps changes the whole page.** `h1` at 60px broke "Educational ads on Meta,
   from zero" onto two lines and pushed every block below it down. 54px holds it on one line.
   Size the H1 to the actual title, not to a number from a spec table.

**Measure before you render.** A render is slow and a page that overflows silently becomes an extra
page in the PDF. Check heights first:

```python
from playwright.sync_api import sync_playwright
import pathlib
u = pathlib.Path("deck.html").resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(u, wait_until="networkidle")
    print(pg.evaluate("""() => [...document.querySelectorAll('.page')].map((el,i)=>{
      const k = [...el.children];
      return {page:i+1, scrollH:el.scrollHeight,
              bodyBottom:Math.max(...k.slice(0,-1).map(x=>x.offsetTop+x.offsetHeight))};
    })"""))
    b.close()
```

`scrollH` must be exactly the page height (1350 for portrait). One pixel over and
`render_one.py` emits a extra page. `bodyBottom` tells you the real slack: the reference build sits
at 952 and 1215 out of 1350, which is the breathing room you want. If a page reads 1350 for both
numbers, it is full to the edge and the next copy edit will overflow it.

**Bullets:** kill `list-style` and draw them with `::before` in `--hot` and `position:absolute; left:0`.
Native bullets can't be coloured independently of the text and their indent won't match your padding.

---

## 4 · Multi-page rhythm

A carousel is a document, not a stack of images. Three rules do most of the work:

1. **Page 1 sets up and hands over.** Cover stack (eyebrow → H1 → lede → handle), then the problem, then
   a bridge line, then the mini-row naming what page 2 will cover. The reader arrives at page 2 already
   knowing its shape.
2. **The handover is literal.** The three mini-cards on page 1 and the three numbered blocks on page 2 are
   the same three items, in the same order, in the same words. `The insight is weak` → `A non-obvious
   insight at the core`. A reader can match them one-to-one without thinking about it. Paraphrasing
   between the two breaks the whole effect.
3. **Every page opens the same way.** Same highlight-header treatment, same footer, same padding. Only the
   *content component* varies (callout, mini-row, numbered blocks).

---

## 5 · Client-brand mode

When the doc is for a client, not for Mauro:

- Swap the `:root` tokens. Everything else is unchanged.
- Handle and footer are **the client's** (`@lorenzo_pravata`, `— Lorenzo`). Never `@maurojpelle` on a
  client asset.
- The client's claims, numbers and topic are theirs. They stay in their doc. They are never reused as
  Mauro's proof, and the topic never migrates into Mauro's own content (see the lane boundary in
  `CLAUDE.md`).
- **Voice follows the client, structure follows this system.** `brand/voice.md` still governs anything
  written for Mauro. On client work, apply it as craft guidance rather than as a hard gate, and keep the
  client's own phrasing. Worth naming: the Lorenzo build contains "When the messenger and the message
  line up, the ad holds. When they don't, the whole thing collapses." That two-sentence contrast is a
  pattern Mauro's own docs would fold into one line. On a client doc in the client's voice, it stays.
- No CTA unless the client asked for one. End on the footer.

---

## 6 · Pre-render check (run on top of the base checklist)

- [ ] Every color below `:root` is a `var()`. Changing `:root` alone fully re-brands the doc.
- [ ] `--hot` appears only in marks under ~60px wide. No large hot fills.
- [ ] One dark callout per page, max.
- [ ] One border radius across the whole doc. One border weight (2px) on cards.
- [ ] Footer is `margin-top:auto`, identical markup on every page, same baseline everywhere.
- [ ] Every page opens with the same header treatment.
- [ ] Page 1's index items and page 2's blocks match one-to-one, same order, same words.
- [ ] Mono labels name a role, not a title, and are uppercase + letterspaced.
- [ ] Number chip is flush to the border, stretches to the bar height, doesn't shrink on a 2-line title.
- [ ] Bullets are `::before`, coloured `--hot`, not native `list-style`.
- [ ] Ran the height measure. Every `.page` `scrollHeight` equals the frame height exactly.
- [ ] Shrink-wrapped blocks use `align-self:flex-start`, not `display:inline-block`.
- [ ] H1 sits on the intended number of lines at the real title length.
- [ ] Client doc: client handle, client footer, client palette, no `@maurojpelle`, no Mauro numbers.

---

## Files

| File | Purpose |
|---|---|
| `page-craft.md` | This file. HTML craft + palette contract + client-brand mode. |
| `reference/client-brand-2page.html` | Working 2-page build. Copy this to start a client doc. |
| `mauro-visual-doc-system.md` | The parent system: types, blocks, voice, workflow. |
