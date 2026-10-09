#!/usr/bin/env python3
"""Headless check of the recording control bar on every v2 board.

    python3 boards/yt/v2/test_controls.py          # every board in every format
    python3 boards/yt/v2/test_controls.py 11       # only the doc-11 board in each format

Per board: ArrowRight and Space move forward, ArrowLeft moves back, the Next and Prev buttons move,
a click on a frame-list row jumps there, Space after a button click moves exactly one step
(focus stays on the document), #N in the URL jumps, and H hides the bar (display:none).
Then the recording-view checks (Mauro 2026-10-09 v6), at 1920x1080: on every frame and every build step
both bottom corners (22% x 28%, the facecam safe zones) hold no text, image, video, chart mark or
button (safezone.SCAN_JS, element bounding boxes, clipped by overflow); D on and D off leave #stage
in the same place (draft UI is overlay only), and the stage is centered left to right; C shows the
facecam box and C again moves it to the right.
A and E step through builds inside a frame, so "one step" there is read as the step counter.
Needs Playwright for Python and Google Chrome (channel="chrome").
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from safezone import SCAN_JS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
# JS that returns a comparable "position" per format: frame index, plus the build step where one exists.
POS = {
    "a-keynote": "[i,st]", "b-canvas": "[i,0]", "c-terminal": "[i,0]",
    "d-countdown": "[i,0]", "e-whiteboard": "[fi,st]", "f-casefile": "[cur,0]",
}
IDX = {"a-keynote": "i", "b-canvas": "i", "c-terminal": "i", "d-countdown": "i", "e-whiteboard": "fi", "f-casefile": "cur"}


def boards():
    for fmt in POS:
        for p in sorted(glob.glob(os.path.join(HERE, fmt, "[0-9][0-9]-*.html"))):
            if p.endswith(".thumbs.html") or (ONLY and not os.path.basename(p).startswith(ONLY)):
                continue
            yield fmt, p


def run():
    fails = 0
    with sync_playwright() as pw:
        br = pw.chromium.launch(channel="chrome", headless=True)
        for fmt, path in boards():
            pg = br.new_page(viewport={"width": 1440, "height": 900})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto("file://" + path)
            pg.wait_for_timeout(1500)
            pos = lambda: tuple(pg.evaluate(POS[fmt]))  # noqa: E731
            idx = lambda: pg.evaluate(IDX[fmt])  # noqa: E731
            checks = []

            def check(name, ok):
                checks.append((name, bool(ok)))

            check("bar hidden by default in headless", pg.evaluate("getComputedStyle(ytbar).display") == "none")
            pg.keyboard.press("h")
            check("H shows the bar", pg.evaluate("getComputedStyle(ytbar).display") != "none")
            p0 = pos()
            pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(150)
            p1 = pos(); check("ArrowRight moves forward", p1 > p0)
            pg.keyboard.press(" "); pg.wait_for_timeout(150)
            p2 = pos(); check("Space moves forward", p2 > p1)
            pg.keyboard.press("ArrowLeft"); pg.wait_for_timeout(150)
            check("ArrowLeft moves back", pos() < p2)
            a = pos(); pg.click("#ytbar [data-a=next]"); pg.wait_for_timeout(150)
            b = pos(); check("Next button moves forward", b > a)
            pg.keyboard.press(" "); pg.wait_for_timeout(150)
            c = pos(); check("Space after a button click moves (focus kept)", c > b)
            check("focus stays on the document", pg.evaluate("document.activeElement===document.body"))
            pg.click("#ytbar [data-a=prev]"); pg.wait_for_timeout(150)
            check("Prev button moves back", pos() < c)
            pg.click("#ytbar [data-a=list]"); pg.wait_for_timeout(150)
            n = pg.evaluate("ytlist.children.length")
            check("frame list has one row per frame", n >= 10)
            pg.click("#ytlist [data-k='6']"); pg.wait_for_timeout(200)
            check("list click jumps to frame 7", idx() == 6)
            pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(150)
            check("arrow works after a list click", pos() > (6, 0) or idx() == 7)
            check("counter shows N / M", pg.evaluate("ytbar.querySelector('.ct').textContent").endswith(f"/ {n}"))
            pg.evaluate("location.hash='#12'"); pg.wait_for_timeout(250)
            check("#12 in the URL jumps to frame 12", idx() == 11)
            pg.keyboard.press("h")
            check("H hides the bar (display:none)", pg.evaluate("getComputedStyle(ytbar).display") == "none")
            # Correction tool (boards/board-corrections.js, Mauro 2026-10-09).
            vis = "(s=>{const e=document.querySelector(s);return !!e&&getComputedStyle(e).display!=='none'})"
            check("corrections tool loaded", pg.evaluate("window.__boardCorrections===true"))
            check("corrections hidden in headless (recording view)", not pg.evaluate(vis + "('#bc-panel')"))
            pg.keyboard.press("d"); pg.wait_for_timeout(150)
            check("D shows the corrections panel (draft layer on)", pg.evaluate(vis + "('#bc-panel')"))
            check("D shows the DRAFT BOARD badge", pg.evaluate(vis + "('#bc-draft')"))
            pg.click("#bc-panel [data-a=frame]"); pg.wait_for_timeout(150)
            i0 = idx()
            pg.keyboard.type("fix this d h"); pg.keyboard.press(" "); pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(250)
            check("typing in a correction box never moves the board", idx() == i0)
            check("typing d in a box keeps the draft layer on", pg.evaluate(vis + "('#bc-panel')"))
            saved = pg.evaluate("Object.entries(localStorage).filter(([k])=>k.startsWith('board-corrections:')).map(([,v])=>v).join('')")
            check("the note is saved in localStorage", "fix this d h" in saved)
            pg.keyboard.press("Escape"); pg.keyboard.press("d"); pg.wait_for_timeout(150)
            check("D turns the draft layer off again (tools gone)", not pg.evaluate(vis + "('#bc-panel')"))
            pg.keyboard.press("d"); pg.wait_for_timeout(150)
            check("D turns it back on", pg.evaluate(vis + "('#bc-panel')"))
            # Facecam box (C / F2) and draft layer that never moves the content.
            pg.keyboard.press("c"); pg.wait_for_timeout(100)
            check("C shows the facecam box bottom-left", pg.evaluate(
                "(b=>getComputedStyle(b).display!=='none'&&b.getBoundingClientRect().left<2)(document.getElementById('bc-face'))"))
            pg.keyboard.press("c"); pg.wait_for_timeout(100)
            check("C again moves it bottom-right", pg.evaluate(
                "(b=>Math.abs(b.getBoundingClientRect().right-innerWidth)<2)(document.getElementById('bc-face'))"))
            pg.keyboard.press("F2"); pg.wait_for_timeout(100)
            check("F2 cycles it off", pg.evaluate("getComputedStyle(document.getElementById('bc-face')).display==='none'"))
            check("no page errors", not errs)
            pg.close()
            pg = br.new_page(viewport={"width": 1920, "height": 1080})
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto("file://" + path); pg.wait_for_timeout(1200)
            stage = "(r=>[r.left,r.top,r.width,r.height].map(v=>Math.round(v)))(document.getElementById('stage').getBoundingClientRect())"
            pg.evaluate("YTNAV.go(3)"); pg.wait_for_timeout(700)
            off = pg.evaluate(stage)
            pg.keyboard.press("d"); pg.wait_for_timeout(200)
            on = pg.evaluate(stage)
            check("D on/off does not move the stage", on == off)
            check("stage centered left to right", abs(off[0] * 2 + off[2] - 1920) <= 2)
            pg.keyboard.press("d"); pg.wait_for_timeout(200)
            pg.evaluate("YTNAV.go(0)"); pg.wait_for_timeout(800)
            corner = []
            for _ in range(500):
                for x in pg.evaluate(SCAN_JS):
                    corner.append(f"frame {pg.evaluate('YTNAV.index()') + 1}: {x}")
                before = pos()
                pg.evaluate("YTNAV.next()"); pg.wait_for_timeout(350)
                if pos() == before:
                    break
            check("facecam corners empty on every frame and build step", not corner)
            if corner:
                errs.extend(corner[:3])
            bad = [nm for nm, ok in checks if not ok]
            fails += len(bad)
            print(f"{'FAIL' if bad else 'ok  '} {fmt}/{os.path.basename(path)}  {len(checks) - len(bad)}/{len(checks)}"
                  + (f"  failed: {bad} {errs[:1]}" if bad else ""))
            pg.close()
        br.close()
    return fails


if __name__ == "__main__":
    sys.exit(1 if run() else 0)
