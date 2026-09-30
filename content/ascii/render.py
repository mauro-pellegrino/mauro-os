#!/usr/bin/env python3
"""Render an ASCII diagram (.txt) into a framed dark-terminal PNG with the @handle.
Usage: python3 content/ascii/render.py content/ascii/<name>.txt [@handle]
Writes <name>.html and <name>.png next to the .txt (2x scale, crisp)."""
import sys, html, pathlib, subprocess
src = pathlib.Path(sys.argv[1]); handle = sys.argv[2] if len(sys.argv) > 2 else "@maurojpelle"
text = src.read_text().rstrip("\n")
lines = text.split("\n"); cols = max(len(l) for l in lines); rows = len(lines)
font = 17; cw = font * 0.6; lh = font * 1.45
w = int(cols * cw + 2 * 56); h = int(rows * lh + 56 * 2 + 44 + 60)
page = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w+80}px;height:{h+80}px;background:#0E1116;display:flex;align-items:center;justify-content:center}}
.win{{width:{w}px;background:#1B1F27;border:1px solid #2E3440;border-radius:14px;box-shadow:0 30px 80px rgba(0,0,0,.55);overflow:hidden}}
.bar{{height:44px;background:#232833;display:flex;align-items:center;padding:0 18px;gap:9px;border-bottom:1px solid #2E3440}}
.d{{width:13px;height:13px;border-radius:50%}}
.t{{flex:1;text-align:center;color:#7C8595;font:13px 'JetBrains Mono',monospace;margin-right:60px}}
pre{{padding:40px 56px 24px;color:#D7DCE4;font:{font}px/{lh}px 'JetBrains Mono',ui-monospace,monospace;white-space:pre}}
.foot{{display:flex;justify-content:space-between;padding:0 56px 26px;font:14px 'JetBrains Mono',monospace;color:#7C8595}}
.foot b{{color:#E8B86A;font-weight:700}}
</style></head><body><div class="win">
<div class="bar"><span class="d" style="background:#FF5F57"></span><span class="d" style="background:#FEBC2E"></span><span class="d" style="background:#28C840"></span><span class="t">~/{src.stem}</span></div>
<pre>{html.escape(text)}</pre>
<div class="foot"><span>{src.stem.replace('-', ' ')}</span><b>{html.escape(handle)}</b></div>
</div></body></html>"""
out_html = src.with_suffix(".html"); out_html.write_text(page)
out_png = src.with_suffix(".png")
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                f"--window-size={w+80},{h+80}", f"--screenshot={out_png}", f"file://{out_html.resolve()}"],
               stderr=subprocess.DEVNULL, check=True)
print(out_png)
