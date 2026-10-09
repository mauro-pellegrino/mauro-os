#!/usr/bin/env python3
"""Build format B (canvas flythrough) boards for docs 11, 02 and 09.

    python3 build.py            # html + notes + thumbs + meta.json
    python3 build.py --png      # also the cover and thumbs PNGs
    python3 build.py --qa       # also every frame to the scratch dir given in QA_DIR (for checking)

Content lives in v11.py, v02.py, v09.py. Shared engine in engine.py. Thumbnails in thumbs.py.
"""
import importlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import engine  # noqa: E402
import thumbs  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VIDEOS = os.environ.get("ONLY", "v11 v02 v09").split()


def shot(url, png, w, h):
    import tempfile
    for attempt in range(3):
        with tempfile.TemporaryDirectory() as prof:
            try:
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=4000",
                                f"--user-data-dir={prof}", f"--screenshot={png}", f"--window-size={w},{h}", url],
                               check=True, capture_output=True, timeout=40)
                return
            except subprocess.TimeoutExpired:
                print("retry", png, flush=True)


def main():
    png = "--png" in sys.argv
    qa = os.environ.get("QA_DIR") if "--qa" in sys.argv else None
    meta = []
    for mod in VIDEOS:
        v = importlib.import_module(mod).VIDEO
        base = f"{v['doc']}-{v['slug']}"
        page, frames, total = engine.build(v)
        open(os.path.join(HERE, base + ".html"), "w").write(page)
        open(os.path.join(HERE, base + ".notes.md"), "w").write(engine.notes_md(v, frames, total))
        if v.get("thumbs"):
            open(os.path.join(HERE, base + ".thumbs.html"), "w").write(thumbs.page(v["thumbs"]))
        meta.append({"doc": v["doc"], "file": base + ".html", "titles": v.get("titles", []),
                     "frames": len(frames), "minutes": round(total / 60), "needs": v.get("needs", [])})
        print(f"{base}: {len(frames)} frames, {total // 60}:{total % 60:02d}, max words/frame {max(f['words'] for f in frames)}")
        path = "file://" + os.path.join(HERE, base + ".html")
        if png:
            shot(path + "#1", os.path.join(HERE, base + ".cover.png"), 1600, 900)
            if v.get("thumbs"):
                n = len(v["thumbs"])
                shot("file://" + os.path.join(HERE, base + ".thumbs.html"), os.path.join(HERE, base + ".thumbs.png"),
                     1280, 720 * n + 40 * (n - 1))
        if qa:
            os.makedirs(qa, exist_ok=True)
            for i in range(1, len(frames) + 1):
                shot(f"{path}#{i}", os.path.join(qa, f"{v['doc']}-{i:02d}.png"), 1600, 900)
    json.dump(meta, open(os.path.join(HERE, "meta.json"), "w"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
