#!/usr/bin/env python3
"""Build the format F (case file / evidence board) YouTube boards.

    python3 build.py           # writes NN-slug.html, NN-slug.notes.md, meta.json
    python3 build.py --png     # also renders NN-slug.cover.png (frame 1) and NN-slug.thumbs.png
    python3 build.py --png --frames   # also renders every frame to _frames/ for checking

Every number on a board is a row in brand/claims.md, or it renders as a red [NEEDS: x] tag.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import engine  # noqa: E402
import v11, v08, v06  # noqa: E402
import thumbs  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VIDEOS = [v11, v08, v06]


def shot(path, png, w, h, frag=""):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=9000",
                    f"--screenshot={png}", f"--window-size={w},{h}", "file://" + path + frag],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    png = "--png" in sys.argv
    meta = []
    for v in VIDEOS:
        page, total = engine.build(v.TITLE, f"format F case file · doc {v.SLUG[:2]} · numbers from brand/claims.md",
                                   v.EXHIBITS, v.STRINGS, v.FRAMES)
        hp = os.path.join(HERE, v.SLUG + ".html")
        open(hp, "w").write(page)
        extra = getattr(v, "NOTES_EXTRA", [])
        open(os.path.join(HERE, v.SLUG + ".notes.md"), "w").write(engine.notes_md(v.TITLE, v.SLUG, v.FRAMES, total, extra))
        meta.append({"doc": v.SLUG[:2], "file": v.SLUG + ".html", "titles": getattr(v, "TITLES", []),
                     "frames": len(v.FRAMES), "minutes": round(total / 60), "needs": v.NEEDS})
        if hasattr(v, "THUMBS"):
            tp = os.path.join(HERE, v.SLUG + ".thumbs.html")
            open(tp, "w").write(thumbs.page(v.TITLE, v.THUMBS))
            if png:
                shot(tp, os.path.join(HERE, v.SLUG + ".thumbs.png"), 1280, 720 * 3 + 40 * 4)
        if png:
            shot(hp, os.path.join(HERE, v.SLUG + ".cover.png"), 1600, 900, "#1")
            if "--frames" in sys.argv:
                d = os.path.join(HERE, "_frames")
                os.makedirs(d, exist_ok=True)
                for i in range(len(v.FRAMES)):
                    shot(hp, os.path.join(d, f"{v.SLUG[:2]}-{i+1:02d}.png"), 1600, 900, f"#{i+1}")
        print(v.SLUG, len(v.FRAMES), "frames", f"{total//60}:{total%60:02d}")
    open(os.path.join(HERE, "meta.json"), "w").write(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
