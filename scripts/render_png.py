"""Render an HTML file to one tall full-page PNG.

Usage:
    python3 scripts/render_png.py path/to/page.html            # 1200px wide
    python3 scripts/render_png.py path/to/page.html 1080       # custom width

Output: page.png next to the HTML file, at 2x for retina sharpness.

Relative image paths resolve because the page is loaded over file://.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

src = Path(sys.argv[1]).resolve()
width = int(sys.argv[2]) if len(sys.argv) > 2 else 1200
out = src.with_suffix(".png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_context(
        viewport={"width": width, "height": 1200},
        device_scale_factor=2,
    ).new_page()
    page.goto(src.as_uri(), wait_until="networkidle")
    page.screenshot(path=str(out), full_page=True)
    browser.close()

print(f"wrote {out}  ({width}px wide, 2x)")
