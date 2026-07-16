"""Render an HTML file to PDF + PNG for Mauro's visual doc system.

Two output types:

  SOCIAL  (fixed-size branded infographics — X quote-tweets, LinkedIn carousels)
    python3 render_one.py deck.html square      # 1080x1080
    python3 render_one.py deck.html portrait    # 1080x1350 (default)
    python3 render_one.py deck.html long        # 1080x1620
      -> deck.pdf (multi-page, one .page div per page)
      -> deck-p1.png, deck-p2.png, ...  (exact-dimension, 2x supersampled)

  BOARD   (long, spacious, editable breakdown board — YouTube walkthroughs)
    python3 render_one.py deck.html board       # (alias: scroll)
      -> deck.pdf   (single continuous tall page, vector-crisp text)
      -> deck.png   (one tall high-res image, 2x device scale)
      -> deck-s1.png, deck-s2.png, ...  (one per .section: record-ready cutaways,
         drop straight into Miro or cut to on camera, no editing)

Boards are built to be edited: swap the text, reorder cards, and paste in your
own images. Reference images with relative paths, e.g. <img src="images/ad-1.png">,
and drop the files in an ./images/ folder next to the HTML. The renderer loads the
file over file:// so relative image paths, local fonts, and other local assets
resolve.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

INPUT_HTML = Path(sys.argv[1]).resolve()
DIM = sys.argv[2] if len(sys.argv) > 2 else "portrait"

PAGED_DIMS = {
    "square":   (1080, 1080),
    "portrait": (1080, 1350),
    "long":     (1080, 1620),
}
BOARD_WIDTH = 1080  # boards render at 1080 wide, natural height
BOARD_ALIASES = {"board", "scroll"}

OUTPUT_PDF = INPUT_HTML.with_suffix(".pdf")
FILE_URL = INPUT_HTML.as_uri()
slug = INPUT_HTML.stem

# ---------------------------------------------------------------------------
# BOARD mode: one continuous tall page. No pagination, no @page slicing.
# ---------------------------------------------------------------------------
if DIM in BOARD_ALIASES:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": BOARD_WIDTH, "height": 1400},
            device_scale_factor=2,  # high-res raster output
        )
        page = context.new_page()
        page.goto(FILE_URL, wait_until="networkidle")
        # Measure full rendered height so the PDF is a single page that tall.
        height = page.evaluate("Math.ceil(document.documentElement.scrollHeight)")
        page.emulate_media(media="screen")  # keep grid bg + card styling
        page.pdf(
            path=str(OUTPUT_PDF),
            width=f"{BOARD_WIDTH}px", height=f"{height}px",
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            print_background=True, prefer_css_page_size=False,
        )
        png_path = INPUT_HTML.parent / f"{slug}.png"
        page.screenshot(path=str(png_path), full_page=True)
        browser.close()
    print(f"wrote {OUTPUT_PDF}")
    print(f"wrote {png_path}  (full height {height}px @2x)")
    sys.exit(0)

# ---------------------------------------------------------------------------
# SOCIAL mode: fixed-size pages sliced from .page divs.
# ---------------------------------------------------------------------------
if DIM not in PAGED_DIMS:
    sys.exit(f"unknown dimension '{DIM}'. options: square / portrait / long / board")
PAGE_W, PAGE_H = PAGED_DIMS[DIM]

PRINT_CSS = f"""
@page {{ size: {PAGE_W}px {PAGE_H}px; margin: 0; }}
html, body {{ background: #fff !important; margin: 0 !important; padding: 0 !important; gap: 0 !important; }}
body {{ display: block !important; }}
.page {{ box-shadow: none !important; margin: 0 !important; page-break-after: always; break-after: page; }}
.page:last-child {{ page-break-after: auto; break-after: auto; }}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": PAGE_W, "height": PAGE_H})
    page = context.new_page()
    page.goto(FILE_URL, wait_until="networkidle")
    page.add_style_tag(content=PRINT_CSS)
    page.emulate_media(media="print")
    page.pdf(
        path=str(OUTPUT_PDF),
        width=f"{PAGE_W}px", height=f"{PAGE_H}px",
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        print_background=True, prefer_css_page_size=True,
    )
    browser.close()
print(f"wrote {OUTPUT_PDF}")

# Rasterize each PDF page to an exact-dimension PNG.
# scale=2.0 supersamples then Lanczos-downsamples for clean output.
import pypdfium2 as pdfium
from PIL import Image

pdf = pdfium.PdfDocument(str(OUTPUT_PDF))
png_paths = []
for i, pdf_page in enumerate(pdf, 1):
    pil_image = pdf_page.render(scale=2.0).to_pil()
    pil_image = pil_image.resize((PAGE_W, PAGE_H), Image.LANCZOS)
    png_path = INPUT_HTML.parent / f"{slug}-p{i}.png"
    pil_image.save(png_path, "PNG", optimize=True)
    png_paths.append(png_path)
    print(f"wrote {png_path}")

print(f"\n{len(pdf)} page(s) rendered as PDF + {len(png_paths)} PNG(s).")
