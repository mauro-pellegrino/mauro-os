#!/usr/bin/env python3
"""Render ghosted-calls-plan.html to a 1600px-wide full-page PNG with headless Chrome.

A temporary copy marks the page end with a magenta line; the PNG is cropped at that line.
    python3 content/plan/render.py
"""
import os, subprocess, tempfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "ghosted-calls-plan.html")
OUT = os.path.join(HERE, "ghosted-calls-plan.png")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1600, 12000

html = open(SRC).read().replace("#end{height:1px}", "#end{height:2px;background:#FF00FF}")
tmp = os.path.join(HERE, ".render-tmp.html")
open(tmp, "w").write(html)
raw = os.path.join(tempfile.gettempdir(), "gc-plan-raw.png")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000",
                f"--screenshot={raw}", f"--window-size={W},{H}", "file://" + tmp], check=True, capture_output=True)
os.remove(tmp)
im = Image.open(raw).convert("RGB")
px = im.load()
x = im.width // 2
end = next((y for y in range(im.height) if px[x, y] == (255, 0, 255)), im.height - 40)
out = Image.new("RGB", (im.width, end + 40), (245, 239, 228))
out.paste(im.crop((0, 0, im.width, end)), (0, 0))
out.save(OUT)
print(OUT, im.width, end + 40)
