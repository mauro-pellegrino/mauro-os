#!/usr/bin/env python3
"""Render an ASCII diagram (.txt) into a framed terminal PNG with the @handle.
Usage: python3 content/ascii/render.py content/ascii/<name>.txt [@handle] [--cream]
--cream: cream background, dark ink, red handle (set 2026-10-01). Default is the dark theme.
Writes <name>.html and <name>.png next to the .txt (2x scale, crisp)."""
import sys, html, pathlib, subprocess
args = [a for a in sys.argv[1:] if a != "--cream"]; cream = "--cream" in sys.argv
src = pathlib.Path(args[0]); handle = args[1] if len(args) > 1 else "@maurojpelle"
C = (dict(page="#EFE8D8", win="#FAF6EC", edge="#D9D2C0", bar="#F1EBDD", title="#8A8578", ink="#1A1A1A", foot="#8A8578", accent="#BD0A0A", shadow="rgba(60,50,30,.18)")
     if cream else
     dict(page="#0E1116", win="#1B1F27", edge="#2E3440", bar="#232833", title="#7C8595", ink="#D7DCE4", foot="#7C8595", accent="#E8B86A", shadow="rgba(0,0,0,.55)"))
text = src.read_text().rstrip("\n")
lines = text.split("\n"); cols = max(len(l) for l in lines); rows = len(lines)
font = 17; cw = font * 0.6; lh = font * 1.45
w = int(cols * cw + 2 * 56); h = int(rows * lh + 56 * 2 + 44 + 60)
page = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w+80}px;height:{h+80}px;background:{C['page']};display:flex;align-items:center;justify-content:center}}
.win{{width:{w}px;background:{C['win']};border:1px solid {C['edge']};border-radius:14px;box-shadow:0 30px 80px {C['shadow']};overflow:hidden}}
.bar{{height:44px;background:{C['bar']};display:flex;align-items:center;padding:0 18px;gap:9px;border-bottom:1px solid {C['edge']}}}
.d{{width:13px;height:13px;border-radius:50%}}
.t{{flex:1;text-align:center;color:{C['title']};font:13px 'JetBrains Mono',monospace;margin-right:60px}}
pre{{padding:40px 56px 24px;color:{C['ink']};font:{font}px/{lh}px 'JetBrains Mono',ui-monospace,monospace;white-space:pre}}
.foot{{display:flex;justify-content:space-between;padding:0 56px 26px;font:14px 'JetBrains Mono',monospace;color:{C['foot']}}}
.foot b{{color:{C['accent']};font-weight:700}}
</style></head><body><div class="win">
<div class="bar"><span class="d" style="background:#FF5F57"></span><span class="d" style="background:#FEBC2E"></span><span class="d" style="background:#28C840"></span><span class="t">~/{src.stem}</span></div>
<pre>{html.escape(text)}</pre>
<div class="foot"><span>{src.stem.replace('-', ' ')}</span><b>{html.escape(handle)}</b></div>
</div></body></html>"""
out_html = src.with_suffix(".html"); out_html.write_text(page)
out_png = src.with_suffix(".png")
CHROMES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]
chrome = next((c for c in CHROMES if pathlib.Path(c).exists()), None)
if chrome is None:
    sys.exit("No Chrome/Chromium found. Add its path to CHROMES in this script.")
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                f"--window-size={w+80},{h+80}", f"--screenshot={out_png.resolve()}", out_html.resolve().as_uri()],
               stderr=subprocess.DEVNULL, check=True)
if not out_png.exists():
    sys.exit(f"Chrome ran but wrote no PNG: {out_png}")
print(out_png)
