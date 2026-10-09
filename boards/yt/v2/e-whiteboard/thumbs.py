"""Three 1280x720 doodle thumbnails per video. Max 4 words each, one face slot (the only placeholder).

Modelled on the whiteboard-plus-facecam thumbnails in research/charlie-morgan/thumbs/ (04, 06, 07):
the diagram is the thumbnail, the face sits in a corner, almost no typed text.
"""
import os
import re

import lib
from lib import *  # noqa: F401,F403

HERE = os.path.dirname(os.path.abspath(__file__))


def _face(x=880, y=150, w=360, h=570):
    lib.add(0, '<rect x="%d" y="%d" width="%d" height="%d" rx="26" fill="none" stroke="#8A8577" stroke-width="5" '
               'stroke-dasharray="18 12"/><text x="%d" y="%d" font-size="34" text-anchor="middle" '
               'style="font-family:\'JetBrains Mono\',monospace;font-weight:700" fill="#8A8577">FACE</text>'
            % (x, y, w, h, x + w / 2, y + h - 40))


def _big(x, y, t, size=128, anchor="start"):
    lib.add(0, '<text x="%d" y="%d" font-size="%d" text-anchor="%s" data-maxw="780" style="font-family:\'Caveat\',cursive;'
               'font-weight:700" fill="#1E1E1E">%s</text>' % (x, y, size, anchor, lib.esc(t)))
    lib.F.words.append(("t", t))


# ---- doc 10 ----
def board_column():
    _big(60, 150, "I record off this")
    column(0, 140, 210, ["hook", "the point", "example", "CTA"], w=380, h=92, gap=36, fill_idx=(1,), size=40, step_each=False)
    arrow(0, 640, 340, 540, 420, bend=30, w=7)
    _face()


def script_vs_board():
    _big(60, 140, "Stop reading")
    box(0, 70, 200, 330, 460)
    for i in range(8):
        line(0, 105, 250 + i * 50, 105 + 250 - (i % 3) * 40, 250 + i * 50, w=3, color=GREY)
    cross(0, 235, 430, 150, w=12)
    arrow(0, 430, 430, 520, 430, w=7)
    column(0, 550, 220, ["", "", "", ""], w=260, h=80, gap=34, fill_idx=(0, 2), step_each=False)
    _face(900, 150, 340, 570)


def time_bars():
    _big(60, 140, "Half the time")
    bars(0, 140, 640, [("by hand", 4, "4h", False), ("now", 2, "~2h", True)], maxv=4, maxh=330, bw=200, gap=140, val_size=80, label_size=44)
    _face()


# ---- doc 03 ----
def keyword_key():
    _big(60, 140, "The only trackable part")
    ellipse(0, 220, 400, 90, 90, w=7)
    line(0, 310, 400, 640, 400, w=8)
    line(0, 560, 400, 560, 470, w=8)
    line(0, 620, 400, 620, 450, w=8)
    arrow(0, 660, 400, 740, 400, w=7)
    box(0, 70, 540, 300, 110, "KEYWORD", fill=True, size=54, bold=True)
    box(0, 560, 520, 260, 170)
    for r in range(2):
        for c in range(4):
            lib.add(0, lib.wline(585 + c * 60, 575 + r * 55, 615 + c * 60, 575 + r * 55, w=4))
    circle_around(0, 690, 640, 60, 34)
    _face()


def clock24():
    _big(60, 150, "24 min to live")
    ellipse(0, 330, 450, 220, 220, w=8, fill=True)
    lib.add(0, lib.wline(330, 450, 330, 290, w=9) + lib.wline(330, 450, 450, 520, w=9))
    _face()


def missing_call():
    _big(60, 140, "Where's the call?")
    flow(0, 60, 260, ["post", "comment", "DM"], w=170, h=110, gap=70, size=38, step_each=False)
    arrow(0, 625, 400, 625, 470, w=6)
    ellipse(0, 625, 570, 120, 90, w=7)
    lib.add(0, '<text x="625" y="605" font-size="110" text-anchor="middle" style="font-family:\'Kalam\',cursive;font-weight:700">?</text>')
    _face()


DRAW = {f.__name__: f for f in (board_column, script_vs_board, time_bars, keyword_key, clock24, missing_call)}


def write(slug, names):
    svgs = []
    for n in names:
        fr = lib.frame("thumb " + slug + n)
        DRAW[n]()
        words = sum(len(t.split()) for k, t in fr.words if k == "t")
        assert words <= 4, (n, words)
        assert not fr.needs and not lib.BANNED.search("".join(v for _, v in fr.parts)), n
        body = "".join(v for _, v in fr.parts)
        svgs.append('<div class="thumb"><svg viewBox="0 0 1280 720" width="1280" height="720" xmlns="http://www.w3.org/2000/svg">'
                    '<rect width="1280" height="720" fill="#FBF8F1"/>%s</svg></div>' % body)
    page = ('<!doctype html><html><head><meta charset="utf-8"><title>%s thumbnails</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Kalam:wght@400;700&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">'
            '<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#8A8A8A;display:flex;flex-direction:column;'
            'align-items:center;gap:30px;padding:30px 0}.thumb{width:1280px;height:720px;overflow:hidden}</style></head><body>%s'
            '<script>document.fonts.ready.then(()=>document.querySelectorAll("text[data-maxw]").forEach(t=>{const m=+t.dataset.maxw,L=t.getComputedTextLength();'
            'if(L>m)t.setAttribute("font-size",(parseFloat(t.getAttribute("font-size"))*m/L).toFixed(1))}))</script></body></html>'
            % (slug, "".join(svgs)))
    with open(os.path.join(HERE, slug + ".thumbs.html"), "w") as fh:
        fh.write(page)
    return len(names)
