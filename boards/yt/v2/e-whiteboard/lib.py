"""Doodle-whiteboard primitives for the format E boards.

Every shape is an inline SVG path with a small seeded jitter, so it looks drawn by hand and
renders the same on every build. Every element sits in a <g data-s="k"> group: step k of its
frame. The page JS draws step 0 when the frame opens and one more step per arrow press.

Checks enforced at build time (each one fixes a v1 failure, see ../BRIEF.md):
  - headline copy max 8 words, diagram labels max 3 words, chart labels max 6
  - no em dash, no banned names, anywhere
  - every [NEEDS: x] tag is collected into meta.json
"""
import html
import zlib
import math
import random
import re

INK = "#1E1E1E"
GREY = "#8A8577"
HL = "#F3E3A3"
PAPER = "#FBF8F1"
RED = "#C8102E"

BANNED = re.compile(r"growthub|lorenzo|\$300k|—", re.I)


class Frame:
    def __init__(self, head, hl=None, secs=40, notes="", sec=None):
        self.head = head
        self.hl = hl
        self.secs = secs
        self.notes = notes
        self.sec = sec  # section number shown as a circled digit, or None
        self.parts = []
        self.needs = []
        self.words = []  # (kind, text) for the copy checks


R = random.Random(7)
F = None  # the frame being built


def frame(head, hl=None, secs=40, notes="", sec=None):
    global F
    F = Frame(head, hl, secs, notes, sec)
    R.seed(zlib.crc32(head.encode()))
    return F


def add(s, svg):
    F.parts.append((s, svg))


def esc(t):
    return html.escape(t, quote=True)


def j(a=2.2):
    return R.uniform(-a, a)


# ---------- paths ----------

def _smooth(pts, closed=False):
    """Catmull-Rom through the points, as cubic beziers."""
    if closed:
        pts = pts + pts[:3]
    d = "M%.1f %.1f" % pts[0]
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
    return d


def path(d, w=4.2, color=INK, op=1):
    return ('<path class="ink" d="%s" fill="none" stroke="%s" stroke-width="%.1f" '
            'stroke-linecap="round" stroke-linejoin="round" opacity="%s"/>' % (d, color, w, op))


def wline(x1, y1, x2, y2, amp=2.0, w=4.2, color=INK):
    n = max(2, int(math.hypot(x2 - x1, y2 - y1) / 140) + 1)
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append((x1 + (x2 - x1) * t + (j(amp) if 0 < i < n else j(1)),
                    y1 + (y2 - y1) * t + (j(amp) if 0 < i < n else j(1))))
    return path(_smooth(pts), w, color)


def line(s, x1, y1, x2, y2, w=4.2, color=INK):
    add(s, wline(x1, y1, x2, y2, w=w, color=color))


def hlfill(x, y, w, h):
    pts = [(x + j(4), y + j(3)), (x + w + j(4), y + j(5)), (x + w + j(4), y + h + j(3)), (x + j(5), y + h + j(4))]
    return '<polygon class="hl" points="%s" fill="%s"/>' % (" ".join("%.1f,%.1f" % p for p in pts), HL)


def box(s, x, y, w, h, label=None, fill=False, size=34, font="k", bold=False, dashed=False, sub=None):
    o = ""
    if fill:
        o += hlfill(x + 6, y + 6, w - 12, h - 12)
    ov = 6
    for (a, b, c, d) in [(x - ov, y, x + w + ov, y), (x + w, y - ov, x + w, y + h + ov),
                         (x + w + ov, y + h, x - ov, y + h), (x, y + h + ov, x, y - ov)]:
        o += wline(a + j(1.5), b + j(1.5), c + j(1.5), d + j(1.5), amp=1.6)
    add(s, o)
    if label:
        cy = y + h / 2 + size * 0.34 - (size * 0.45 if sub else 0)
        text(s, x + w / 2, cy, label, size, anchor="middle", font=font, bold=bold, maxw=w - 24)
    if sub:
        text(s, x + w / 2, y + h / 2 + size * 0.75, sub, int(size * 0.7), anchor="middle", font="k",
             color=GREY, maxw=w - 24)


def ellipse(s, cx, cy, rx, ry, w=4.2, color=INK, fill=False):
    pts = []
    n = 14
    start = R.uniform(0, 6.28)
    for i in range(n + 2):
        a = start + i * 2 * math.pi / n
        k = 1 + R.uniform(-.035, .035)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    o = ""
    if fill:
        o += '<ellipse class="hl" cx="%d" cy="%d" rx="%d" ry="%d" fill="%s"/>' % (cx, cy, rx - 6, ry - 6, HL)
    o += path(_smooth(pts), w, color)
    add(s, o)


def circle_around(s, cx, cy, rx, ry):
    """The loose marker loop that circles something already on the board."""
    pts = []
    start = R.uniform(0, 6.28)
    for i in range(17):
        a = start + i * 2 * math.pi / 15
        k = 1 + R.uniform(-.05, .05) + i * 0.006
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    add(s, path(_smooth(pts), 4.6))


def arrow(s, x1, y1, x2, y2, bend=0, w=4.4, color=INK, head=True):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    cx, cy = mx + nx * bend + j(2), my + ny * bend + j(2)
    d = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1, y1, cx, cy, x2, y2)
    o = path(d, w, color)
    if head:
        ang = math.atan2(y2 - cy, x2 - cx)
        for da in (2.6, -2.6):
            hx = x2 + 22 * math.cos(ang + da) + j(1.5)
            hy = y2 + 22 * math.sin(ang + da) + j(1.5)
            o += path("M%.1f %.1f L%.1f %.1f" % (hx, hy, x2, y2), w, color)
    add(s, o)


def underline(s, x1, x2, y, w=5):
    pts = [(x1, y + j(1))]
    n = int((x2 - x1) / 60) + 1
    for i in range(1, n + 1):
        pts.append((x1 + (x2 - x1) * i / n, y + j(3)))
    add(s, path(_smooth(pts), w))


def cross(s, x, y, r=40, color=INK, w=6):
    add(s, path("M%.1f %.1f L%.1f %.1f" % (x - r + j(), y - r + j(), x + r + j(), y + r + j()), w, color)
        + path("M%.1f %.1f L%.1f %.1f" % (x + r + j(), y - r + j(), x - r + j(), y + r + j()), w, color))


def strike(s, x1, x2, y, w=6):
    add(s, path("M%.1f %.1f L%.1f %.1f" % (x1, y + j(3), x2, y + j(3)), w))


def tick(s, x, y, r=26, w=6):
    add(s, path("M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (x - r, y, x - r * .3, y + r * .7, x + r, y - r * .8), w))


def hlrect(s, x, y, w, h):
    add(s, hlfill(x, y, w, h))


# ---------- text ----------

def text(s, x, y, t, size=34, anchor="start", font="k", bold=False, color=INK, maxw=None, kind="l"):
    """kind: l = diagram label (max 3 words), c = chart label (max 6), x = exempt (code, numbers)."""
    fam = {"k": "'Kalam',cursive", "c": "'Caveat',cursive", "m": "'JetBrains Mono',monospace"}[font]
    if kind != "x" and font != "m":
        F.words.append((kind, t))
    fit = ' data-maxw="%d"' % maxw if maxw else ""
    add(s, '<text x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" style="font-family:%s;font-weight:%s" '
           'fill="%s"%s>%s</text>' % (x, y, size, anchor, fam, 700 if bold else 400, color, fit, esc(t)))


def num(s, x, y, t, size=80, anchor="middle", color=INK):
    """A number or value on a chart. Every one of these must trace to brand/claims.md."""
    text(s, x, y, t, size, anchor=anchor, font="k", bold=True, color=color, kind="x")


def needs(s, x, y, what, size=26, anchor="start"):
    """The visible red tag for a number or fact that brand/claims.md does not clear."""
    F.needs.append(what)
    t = "[NEEDS: %s]" % what
    w = int(len(t) * size * 0.62) + 32
    x0 = x if anchor == "start" else x - w / 2
    add(s, '<g class="needs"><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="6" fill="%s"/>'
           '<text x="%.1f" y="%.1f" font-size="%d" text-anchor="middle" style="font-family:\'JetBrains Mono\',monospace;font-weight:700" fill="#fff">%s</text></g>'
        % (x0, y - size - 6, w, size + 22, RED, x0 + w / 2, y + 2, size, esc(t)))


def code(s, x, y, lines, size=24, lh=1.38, hl_rows=(), w=None, pad=26):
    """Monospace block in a hand-drawn frame. Code is exempt from the word cap."""
    h = int(len(lines) * size * lh + pad * 2)
    w = w or int(max(len(l) for l in lines) * size * 0.61 + pad * 2)
    for r in hl_rows:
        hlrect(s, x + pad - 8, y + pad + r * size * lh - 2, w - pad * 2 + 16, size * lh)
    box(s, x, y, w, h)
    o = ""
    for i, l in enumerate(lines):
        o += ('<text x="%.1f" y="%.1f" font-size="%d" style="font-family:\'JetBrains Mono\',monospace;font-weight:500;white-space:pre" '
              'xml:space="preserve" fill="%s">%s</text>' % (x + pad, y + pad + (i + .78) * size * lh, size, INK, esc(l)))
    add(s, o)
    return w, h


def image(s, x, y, w, h, href):
    add(s, '<image href="%s" x="%d" y="%d" width="%d" height="%d" preserveAspectRatio="xMidYMid slice"/>' % (href, x, y, w, h))
    box(s, x - 4, y - 4, w + 8, h + 8)


# ---------- composites ----------

def bars(s, x, base, items, maxv, maxh=420, bw=150, gap=90, label_size=30, val_size=60, step_each=False):
    """Vertical hand-drawn bars. items: (label, value, shown_value, filled). Heights are exact to scale."""
    for i, (lab, v, shown, filled) in enumerate(items):
        st = s + i if step_each else s
        h = maxh * v / maxv
        bx = x + i * (bw + gap)
        box(st, bx, base - h, bw, h, fill=filled)
        num(st, bx + bw / 2, base - h - 22, shown, val_size)
        text(st, bx + bw / 2, base + 46, lab, label_size, anchor="middle", kind="c", maxw=bw + gap - 10)
    line(s, x - 40, base, x + len(items) * (bw + gap) - gap + 40, base, w=4.6)


def hbars(s, x, y, items, maxv, maxw=900, bh=74, gap=46, label_w=330, label_size=30, val_size=44, step_each=False):
    for i, (lab, v, shown, filled) in enumerate(items):
        st = s + i if step_each else s
        by = y + i * (bh + gap)
        w = maxw * v / maxv
        text(st, x + label_w - 24, by + bh / 2 + 11, lab, label_size, anchor="end", kind="c", maxw=label_w - 30)
        box(st, x + label_w, by, w, bh, fill=filled)
        num(st, x + label_w + w + 22, by + bh / 2 + 16, shown, val_size, anchor="start")


def flow(s, x, y, labels, w=260, h=120, gap=80, fill_idx=(), size=32, step_each=True, subs=None):
    for i, lab in enumerate(labels):
        st = s + i if step_each else s
        bx = x + i * (w + gap)
        box(st, bx, y, w, h, lab, fill=i in fill_idx, size=size, sub=(subs[i] if subs else None))
        if i:
            arrow(st, bx - gap + 12, y + h / 2, bx - 12, y + h / 2)


def column(s, x, y, labels, w=380, h=74, gap=34, fill_idx=(), size=30, step_each=True):
    for i, lab in enumerate(labels):
        st = s + i if step_each else s
        by = y + i * (h + gap)
        box(st, x, by, w, h, lab, fill=i in fill_idx, size=size)
        if i:
            arrow(st, x + w / 2, by - gap + 6, x + w / 2, by - 6, head=True, w=3.6)


def agenda(s, x, y, items, gap=150):
    for i, it in enumerate(items):
        ellipse(s + i, x + 44, y + i * gap - 14, 44, 44, fill=True)
        num(s + i, x + 44, y + i * gap + 6, str(i + 1), 54)
        text(s + i, x + 130, y + i * gap + 6, it, 64, font="c", bold=True, kind="a")


def section_card(n, title, secs, notes):
    frame(title, secs=secs, notes=notes, sec=n)
    ellipse(0, 800, 470, 150, 150, fill=True, w=6)
    num(0, 800, 540, str(n), 200)
    underline(1, 560, 1040, 700)


def cta(secs, notes, sec=None):
    frame("Link in the description", hl="description", secs=secs, notes=notes, sec=sec)
    box(0, 430, 330, 740, 190, fill=True)
    text(0, 800, 445, "Agency Booked Calls", 74, anchor="middle", font="c", bold=True, maxw=700)
    arrow(1, 800, 560, 800, 800, bend=40, w=6)
    underline(1, 640, 960, 835)


def img_data(p, w=480):
    """Downscale a real image already in the repo and inline it as a data URI."""
    import base64
    import io
    from PIL import Image
    im = Image.open(p).convert("RGB")
    im = im.resize((w, int(im.height * w / im.width)))
    b = io.BytesIO()
    im.save(b, "JPEG", quality=78)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()
