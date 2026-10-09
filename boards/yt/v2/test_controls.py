#!/usr/bin/env python3
"""Headless check of the recording control bar on every v2 board.

    python3 boards/yt/v2/test_controls.py          # every board in every format
    python3 boards/yt/v2/test_controls.py 11       # only the doc-11 board in each format

Per board: ArrowRight and Space move forward, ArrowLeft moves back, the Next and Prev buttons move,
a click on a frame-list row jumps there, Space after a button click moves exactly one step
(focus stays on the document), #N in the URL jumps, and H hides the bar (display:none).
A and E step through builds inside a frame, so "one step" there is read as the step counter.
Needs Playwright for Python and Google Chrome (channel="chrome").
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

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
            check("no page errors", not errs)
            bad = [nm for nm, ok in checks if not ok]
            fails += len(bad)
            print(f"{'FAIL' if bad else 'ok  '} {fmt}/{os.path.basename(path)}  {len(checks) - len(bad)}/{len(checks)}"
                  + (f"  failed: {bad} {errs[:1]}" if bad else ""))
            pg.close()
        br.close()
    return fails


if __name__ == "__main__":
    sys.exit(1 if run() else 0)
