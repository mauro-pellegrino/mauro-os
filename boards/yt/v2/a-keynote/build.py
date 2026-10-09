#!/usr/bin/env python3
"""Build the format A (keynote) boards: python3 build.py [--png] [--frames]

--png     renders <slug>.cover.png (frame 1, fully built, 1600x900) and <slug>.thumbs.png
--frames  also renders every frame, fully built, to the scratch dir given by $FRAMES_DIR (QA only)
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import engine  # noqa: E402
import d11, d12, d01  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DOCS = [d11, d12, d01]

THUMB_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@700;800;900&family=JetBrains+Mono:wght@700;800&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{background:#8A8A8A;font-family:'Inter',sans-serif;width:1280px}
.thumb{width:1280px;height:720px;position:relative;overflow:hidden;margin-bottom:20px}
.thumb:last-child{margin-bottom:0}
.thumb i{display:block}
.face{position:absolute;right:0;bottom:0;width:420px;height:640px;border:5px dashed rgba(233,185,73,.85);border-radius:20px 20px 0 0;
display:flex;align-items:flex-end;justify-content:center;padding-bottom:24px;font:700 22px 'JetBrains Mono',monospace;
color:rgba(233,185,73,.95);letter-spacing:3px}
"""


def shot(url, png, w, h):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=6000",
                    f"--screenshot={png}", f"--window-size={w},{h}", url],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    png = "--png" in sys.argv
    frames = "--frames" in sys.argv
    meta = []
    bad = []
    for d in DOCS:
        slides = d.slides()
        html_out, md, secs, n, problems = engine.build(d.TITLES[0]["title"], slides, f"{d.SLUG}: presenter notes", d.SOURCES)
        md += "\n## Titles\n\n" + "\n".join(f"{k}. {t['title']}  \n   modelled on: {t['modelled_on']}" for k, t in enumerate(d.TITLES, 1)) + "\n"
        md += "\n## [NEEDS] left on this board\n\n" + "\n".join(f"- {x}" for x in d.NEEDS) + "\n"
        p = os.path.join(HERE, d.SLUG + ".html")
        open(p, "w").write(html_out)
        open(os.path.join(HERE, d.SLUG + ".notes.md"), "w").write(md)
        th = ('<!doctype html><html><head><meta charset="utf-8"><title>' + d.SLUG + ' thumbnails</title><style>' + THUMB_CSS +
              '</style></head><body>' + "\n".join(d.THUMBS) + "</body></html>\n")
        tp = os.path.join(HERE, d.SLUG + ".thumbs.html")
        open(tp, "w").write(th)
        for f in (p, tp, os.path.join(HERE, d.SLUG + ".notes.md")):
            if "—" in open(f).read():
                bad.append(f"em dash in {f}")
        for t in d.TITLES:
            if "—" in t["title"] or len(t["title"]) > 60:
                bad.append(f"title check: {t['title']} ({len(t['title'])} chars)")
        bad += [f"{d.SLUG} {x}" for x in problems]
        meta.append({"doc": d.DOC, "file": d.SLUG + ".html", "titles": d.TITLES, "frames": n,
                     "minutes": round(secs / 60), "needs": d.NEEDS})
        print(f"{d.SLUG}: {n} frames, {secs//60}:{secs%60:02d}")
        if png:
            shot("file://" + p + "?s=1&all=1", os.path.join(HERE, d.SLUG + ".cover.png"), 1600, 900)
            shot("file://" + tp, os.path.join(HERE, d.SLUG + ".thumbs.png"), 1280, 720 * 3 + 40)
        if frames:
            out = os.environ["FRAMES_DIR"]
            os.makedirs(out, exist_ok=True)
            for k in range(1, n + 1):
                shot("file://" + p + f"?s={k}&all=1", os.path.join(out, f"{d.DOC}-{k:02d}.png"), 1600, 900)
    json.dump(meta, open(os.path.join(HERE, "meta.json"), "w"), indent=2, ensure_ascii=False)
    print("\n".join(bad) if bad else "checks clean: words <= 8 per frame, no em dashes, titles <= 60 chars")


if __name__ == "__main__":
    main()
