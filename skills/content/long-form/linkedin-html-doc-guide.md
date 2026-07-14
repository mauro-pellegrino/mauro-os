# LinkedIn HTML Doc Skill

How Mauro builds branded LinkedIn carousel docs (2-4 page HTML → PDF + per-page PNG) in one consistent visual system. Every doc follows the same page dimensions, palette, type system, and voice rules so the brand reads consistently across articles, retweets, and DM wedges. Each render produces a PDF for LinkedIn document posts and individual PNGs for Twitter, Instagram, Threads, and screen recording.

[CALIBRATE: the palette below is the inherited doc system. Swap it once Mauro locks his own brand palette; everything else (dimensions, type, blocks, workflow) carries over unchanged.]

## When to use this skill

- Turning a LinkedIn article draft into a styled carousel doc
- Building a generic framework/strategy doc for a public post
- Producing the master industry deck that downstream personalization skills (e.g., `personalization-guide.md`) edit per prospect

Do NOT use this skill for: short text posts, image-only carousels, or video scripts.

## The master frame (every page)

- **Page dimensions** are picked once per doc from this fixed set. All pages in a single doc must use the same dimension:
  - `1080 × 1080` — **Square.** For short docs with 3-5 punchy concepts and no walked example. Cleanest read on mobile, no whitespace pressure if you scale type appropriately.
  - `1080 × 1350` — **Standard LinkedIn portrait (4:5).** Default for article-length docs and multi-step playbooks.
  - `1080 × 1620` — **Long portrait (2:3).** Only for content-dense docs that overflow 1350 with no compression options left.
- Padding: `50px 60px` to `55px 65px` depending on density (use the lower numbers if cramming a long doc into fewer pages).
- **Scale typography to the page.** If a page lands with significant bottom whitespace, scaling up font sizes (body 17-19px, section headings 28-32px) is preferable to leaving the dead space. Whitespace below content reads as missing content. Mid-air visuals do not.
- White background, hard-edged sections (no soft shadows on internal elements).
- Each page is a self-contained `.page` div in the HTML.
- The CSS forces a page break after each `.page` div via the print stylesheet, so 1 div = 1 PDF page.

## The doc palette

| Name | Hex | Use |
|---|---|---|
| Space Indigo | `#24243C` | Primary text, table borders, dark callout fills |
| Jasmine | `#F5D679` | Section headings (sticker style), accent fills, CTA blocks |
| Shocking Pink | `#E830B8` | Handle line, step-number badges, italic-pink lines (used sparingly), insight box left bar |
| Aquamarine | `#95F9C0` | "Working / do this" cells, math-bar fill, sub-labels inside dark callouts |
| White | `#FFFFFF` | Background, format-chip fills |

**Critical:** never use Jasmine as text color on white — it disappears. Jasmine is a fill color (block of color behind dark text), never a text color on light backgrounds.

## Typography

- Body: Inter, font-weights 400/500/700/800
- Monospace (timeline labels, math bar, code-style callouts): JetBrains Mono
- Script (legacy brand mark — see "What's banned"): Caveat
- Title: 44-46px, weight 800, color Space Indigo, letter-spacing -1px
- Subtitle: 19-21px, weight 400, Space Indigo
- Handle (@maurojpelle): 17-19px, weight 400, Shocking Pink
- Section heading: 24-28px, weight 800, sticker style (Jasmine background, Space Indigo text, padded `4px 12px`, `display: inline-block` + `align-self: flex-start`)
- Step heading: same as section heading + Shocking Pink circle badge with white step number, 30-34px diameter
- Body text: 15-17px, weight 400, Space Indigo, line-height 1.5

## Recurring visual blocks

| Block | When to use | Visual recipe |
|---|---|---|
| `table-3` (label + body grid) | Frameworks with 3-5 labeled rows. Awareness stages, persona cells, comparison rows. | 170-200px label column with rotating Jasmine/Pink/Aqua/Indigo fills, Space Indigo border, white body cells. |
| `insight-box` | One quote, one definition, one "the shape of X". | Space Indigo background, Jasmine text, Shocking Pink left bar 5-6px, italic body, small Aquamarine uppercase label above. |
| `math-bar` | A multiplication readout or numeric payoff. | Aquamarine fill, Space Indigo border, monospace font, the headline number in Shocking Pink at 20-22px. |
| `timeline` | Process with sequential phases (e.g., 14-day sprint). | 5-column grid, each cell with monospace day-range label (white on Space Indigo) at top, bold phase name, short body. |
| `formats-grid` | List of named items where each has a short definition. | 2-col grid of bordered chips. Item name in Shocking Pink + bold, definition in Space Indigo. |
| `hook-pattern-grid` / `hook-box` | Quoted hook examples or pattern descriptions. | Light pink fill (`#fbd5ed`), Shocking Pink left bar, monospace uppercase label. |
| `cta-block` | The audit ask at the end of a public post. | Jasmine fill, Space Indigo border 2-3px, bold title, body text with "DM me [keyword]" in bold. |

## Page-count and dimension guide

Pick dimension first based on content shape, then count pages. Both choices serve readability.

| Content shape | Dimension | Page count |
|---|---|---|
| 3-5 punchy concepts, no walked example, short prose | `1080 × 1080` square | 2-3 pages |
| Single framework + one worked example | `1080 × 1350` portrait | 2 pages |
| Multi-step playbook with 3-5 steps, no examples | `1080 × 1350` portrait | 2-3 pages |
| Article-length post with steps + examples + CTA | `1080 × 1350` portrait | 3-4 pages |
| Content-dense single page that won't compress | `1080 × 1620` long portrait | 1-2 pages |
| Internal reference with multiple frameworks | `1080 × 1350` portrait | 4+ pages |

**On whitespace.** A natural section break landing mid-page is fine, but persistent bottom whitespace across multiple pages means the dimension is wrong for the content. If two or more pages in a row land with significant dead space, either (a) switch to a smaller dimension (portrait → square), (b) scale type up by 15-20%, or (c) consolidate content to fewer pages. Don't ship a doc where each page only uses 60% of its canvas.

## Voice rules

These apply to every word inside every deck. Violating them dates the doc as AI-generated or "agency LinkedIn-speak."

### Banned constructions

- **Em dashes** in body content. Replace with commas, periods, or colons. The only allowed em dash is in the footer `— Mauro` signature (see "Footer" below).
- **"Not X but Y" patterns.** "It isn't volume, it's structural." Cringe.
- **Italic one-liners that summarize the section.** The kind of "if your X needs three sentences, it's not sharp enough" punchline-preacher voice. If the section was clear, it doesn't need a moral at the end. Cut them. (Originally rendered as `.body-italic-pink` paragraphs after a section. Class can stay defined in CSS for backwards compat, but don't add new instances.)
- **"Most brands [bad thing]. Operators [good thing]."** Same energy as the above. Cut.
- **"That's the difference between [a] and [b]."** Cut.
- **Generic agency openers.** "Let's talk about X." "Here's the thing." "Here's the truth." Cut.
- **Multiple questions stacked.** One question per CTA, never two.

### Allowed and encouraged

- Direct declaratives. "Performance is structural before it's creative."
- Concrete numbers and specifics. "14 days", "45 posts", "30+ days." Only real numbers from Mauro's own work (any public one needs his sign-off) or bracketed placeholders.
- Worked-example callouts (the Space Indigo `insight-box` shape) when you have a real example. Skip when generalizing.
- First-person from Mauro. "I", "the engine I run", "the agency I run."

## Footer

The footer used to include a Caveat-script brand mark on the right side. **As of the May 2026 update, the brand mark is removed from all new docs.** Footer is now just `— Mauro` on the left, sitting above the horizontal divider, with the right side empty.

```html
<hr class="footer-divider">
<div class="footer-row">
  <span class="author">— Mauro</span>
</div>
```

The `.brand-mark` CSS class can stay defined in the stylesheet for legacy decks but should not be instantiated in new ones.

## CTA handling (public vs private)

**Public posts (LinkedIn carousel for retweet/share):** keep the CTA at the end. Use the `cta-block` Jasmine-fill box with "DM me [keyword]" bolded. Soften any tier gates (a hard "$500k+/mo agencies" gate reads narrow; prefer "if you're running a real agency" for broader applicability unless the gate is intentional).

**Private DM wedge (personalized deck sent to a single prospect):** strip the CTA entirely. The deck ends on the closer-italic line + footer. The CTA belongs in the DM message wrapper, not in the deck itself. (See `personalization-guide.md` for the private-send personalization workflow.)

## Output formats (PDF + PNG per page)

Every render produces both a multi-page PDF and individual PNG files (one per page). Different platforms want different formats. Always export both so the same source supports every channel.

| Platform / use case | Use this output | Why |
|---|---|---|
| LinkedIn document post (carousel) | PDF | LinkedIn renders multi-page PDFs as native swipeable carousels. Algorithmic boost over image posts. This is the only platform where PDF is the right choice. |
| Twitter / X (single image post) | PNG (one page per tweet) | PDFs don't render in-feed. Use page 1 PNG as the standalone tweet image, or post multiple pages as a thread (4-image cap per tweet). |
| Twitter / X (QT with image) | PNG | The infographic-tweet pattern (one-liner + visual) needs a PNG that renders inline. |
| Instagram / Threads | PNG | No PDF support. Post as image or multi-image carousel using individual PNGs. |
| LinkedIn image post (not document) | PNG | If you'd rather post the doc as a regular image instead of a document post. Trades carousel reach for higher inline-feed visibility. |
| Screen recording for video content | PNG | Stepping through PNGs in a slideshow or video editor produces cleaner footage than recording through a PDF viewer's UI chrome. |
| Email signature, deck embed, web embed | PNG | Universally supported, predictable rendering across email clients and browsers. |

**Naming convention:** the render script outputs `slug.pdf` and `slug-p1.png`, `slug-p2.png`, etc. Single-page docs still get the `-p1` suffix on the PNG so the convention stays consistent.

**Spec:** PNGs are exact-dimension match to the chosen canvas (1080×1080, 1080×1350, or 1080×1620), RGB mode, supersampled at 2× scale then Lanczos-downsampled for crisp edges. Typical file size 300-600KB depending on visual density.

## Workflow per new doc

1. **Decide the type.** Article/framework/wedge? Public or private send?
2. **Outline the page split.** Map content to pages before writing. Each step or section should land cleanly on a page boundary or pair with one other section. Avoid orphaning a single paragraph at the top of a page.
3. **Copy the master CSS** from `skills/content/linkedin-docs/industry-decks/linkedin-doc-template.html` (or the most recent matching finished doc in that folder).
4. **Write the body content** following the voice rules above. No em dashes, no cringe one-liners.
5. **Render with the dual-output script** at the chosen dimension. Produces both `slug.pdf` and `slug-p1.png`, `slug-p2.png`, etc. Verify page count matches the plan.
6. **Visual QA each page in PNG form.** PNGs are what most platforms will actually display. Check no overflow, no missing-font fallbacks, no leftover screen-only chrome (gray body background, card shadows).
7. **Save** the HTML, PDF, and all PNGs in the project outputs folder with the slug-based naming.

## Quality check before sending

- [ ] No em dashes in body content (footer `— Mauro` is the only exception)
- [ ] No italic-pink summary one-liners after sections
- [ ] No script-font brand mark in any footer
- [ ] Page count matches the plan (2-4 pages typical)
- [ ] All pages render cleanly with no overflow in BOTH the PDF and PNG outputs
- [ ] Colored table fills, Jasmine section stickers, and Shocking Pink step badges all rendered
- [ ] Inter loaded for body, JetBrains Mono loaded for monospace blocks, Caveat NOT used anywhere
- [ ] If public: CTA present with "DM me [keyword]" bolded inside a Jasmine `cta-block`
- [ ] If private: no CTA, deck ends on closer-italic + footer
- [ ] PNG dimensions match the canvas spec exactly (1080×1080, 1080×1350, or 1080×1620)
- [ ] If posting to Twitter/IG: preview the PNG, not the PDF, since that is what those platforms will display

## Files in this skill family

| File | Purpose |
|---|---|
| `linkedin-html-doc-guide.md` | This file. The visual + voice system. |
| `../linkedin-docs/personalization-guide.md` | How to adapt a generic master deck per prospect (find-and-replace workflow). |
| `../linkedin-docs/industry-decks/linkedin-doc-template.html` | Clean structural template with placeholder copy. Start every new deck from this. |

## Render snippet (Playwright)

Reusable Python snippet for HTML → PDF + per-page PNG. Drop into a script next to the HTML file. Requires `playwright`, `pypdfium2`, and `Pillow`.

```python
"""Render an HTML file to PDF + per-page PNGs.

Usage:
    python3 render_one.py path/to/deck.html portrait    # 1080x1350 (default)
    python3 render_one.py path/to/deck.html square      # 1080x1080
    python3 render_one.py path/to/deck.html long        # 1080x1620
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import pypdfium2 as pdfium
from PIL import Image

INPUT_HTML = Path(sys.argv[1])
DIM = sys.argv[2] if len(sys.argv) > 2 else "portrait"

DIM_MAP = {"square": (1080, 1080), "portrait": (1080, 1350), "long": (1080, 1620)}
PAGE_W, PAGE_H = DIM_MAP[DIM]
OUTPUT_PDF = INPUT_HTML.with_suffix(".pdf")

PRINT_CSS = f"""
@page {{ size: {PAGE_W}px {PAGE_H}px; margin: 0; }}
html, body {{ background: #fff !important; margin: 0 !important; padding: 0 !important; gap: 0 !important; }}
body {{ display: block !important; }}
.page {{ box-shadow: none !important; margin: 0 !important; page-break-after: always; break-after: page; }}
.page:last-child {{ page-break-after: auto; break-after: auto; }}
"""

# Render PDF
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": PAGE_W, "height": PAGE_H})
    page = context.new_page()
    page.set_content(INPUT_HTML.read_text(), wait_until="networkidle")
    page.add_style_tag(content=PRINT_CSS)
    page.emulate_media(media="print")
    page.pdf(
        path=str(OUTPUT_PDF),
        width=f"{PAGE_W}px", height=f"{PAGE_H}px",
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        print_background=True, prefer_css_page_size=True,
    )
    browser.close()

# Rasterize each PDF page to a per-page PNG at exact canvas dimensions.
# scale=2.0 supersamples then Lanczos downsamples for crisp edges.
pdf = pdfium.PdfDocument(str(OUTPUT_PDF))
slug = INPUT_HTML.stem
for i, pdf_page in enumerate(pdf, 1):
    img = pdf_page.render(scale=2.0).to_pil()
    img = img.resize((PAGE_W, PAGE_H), Image.LANCZOS)
    img.save(INPUT_HTML.parent / f"{slug}-p{i}.png", "PNG", optimize=True)
```
