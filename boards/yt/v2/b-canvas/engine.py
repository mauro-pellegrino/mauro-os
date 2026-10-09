#!/usr/bin/env python3
"""Format B, canvas flythrough: the shared engine.

One large 2D map per video (12800x7200 canvas units). The viewport is a fixed 1600x900 stage,
letterboxed to the window. Each frame is a camera target (a zone, a region or the whole map) and
the camera moves with a CSS transform (translate + scale, 0.8s ease).

The content of each video lives in v11.py, v02.py, v09.py. build.py renders all of them.

Copy rule: every zone marks its spoken-style copy with class "c". The builder counts the words in
"c" elements per frame and fails the build above 8. Labels (class "lbl", "ztag", svg text, code,
trees) are diagram labels and are not counted, per BRIEF.md rule 1.
"""
import html
import json
import re
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import controls  # noqa: E402  (shared recording control bar, boards/yt/v2/controls.py)

NAV_ADAPTER = "{count:()=>F.length,index:()=>i,go:cam,next:()=>cam(i+1),prev:()=>cam(i-1),label:k=>F[k].t+' · '+F[k].k}"
from html.parser import HTMLParser

W, H = 12800, 7200          # canvas units, 16:9
ZW, ZH = 1600, 900          # one zone = one 16:9 frame at scale ~1
COLS = [400, 2300, 4600, 6500, 8800, 10700]   # 3 regions x 2 columns
ROWS = [2000, 3250, 4500, 5750]
TOP_Y = 350                 # hook row and CTA row

esc = html.escape


# ---------------------------------------------------------------- components

def needs(x):
    return f'<span class="needs">[NEEDS: {esc(x)}]</span>'


def lbl(x, cls=""):
    return f'<div class="lbl {cls}">{x}</div>'


def c(x, tag="div", cls=""):
    return f'<{tag} class="c {cls}">{x}</{tag}>'


def window(title, body, cls="", style=""):
    return (f'<div class="win {cls}" style="{style}"><div class="wbar"><i></i><i></i><i></i>'
            f'<span>{esc(title)}</span></div><div class="wbody">{body}</div></div>')


def tree(lines, hl=(), red=(), size=21):
    out = []
    for ln in lines:
        e = esc(ln)
        if any(k in ln for k in red):
            e = f'<span class="tred">{e}</span>'
        elif any(k in ln for k in hl):
            e = f'<span class="thl">{e}</span>'
        out.append(e)
    return f'<pre class="tree" style="font-size:{size}px">' + "\n".join(out) + "</pre>"


def flow(nodes, cls=""):
    """nodes: list of (title, sub, kind) kind in '', 'on', 'dark', 'red'."""
    parts = []
    for i, n in enumerate(nodes):
        t, sub, kind = (list(n) + ["", ""])[:3]
        if i:
            parts.append('<div class="arr">&rarr;</div>')
        s = f"<small>{sub}</small>" if sub else ""
        parts.append(f'<div class="node {kind}"><b>{t}</b>{s}</div>')
    return f'<div class="flow {cls}">{"".join(parts)}</div>'


def split(before, after, bl="BEFORE", al="AFTER"):
    return (f'<div class="split"><div class="half bef"><div class="badge">{bl}</div>{before}</div>'
            f'<div class="half aft"><div class="badge">{al}</div>{after}</div></div>')


def bars(items, w=1100, h=470, unit="", ref=None, ref_label=""):
    """Vertical bar chart. items: (label, value, color, value_text)."""
    vmax = max([v for _, v, _, _ in items] + ([ref] if ref else [])) * 1.12
    n = len(items)
    pad_l, pad_b, pad_t = 30, 70, 50
    bw = min(240, (w - pad_l) / n * 0.55)
    gap = (w - pad_l - bw * n) / (n + 1)
    svg = [f'<svg class="chart" width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    base = h - pad_b
    svg.append(f'<line x1="{pad_l}" y1="{base}" x2="{w}" y2="{base}" stroke="#1B4332" stroke-width="4"/>')
    if ref is not None:
        ry = base - (base - pad_t) * ref / vmax
        svg.append(f'<line x1="{pad_l}" y1="{ry:.0f}" x2="{w}" y2="{ry:.0f}" stroke="#5F6B62" stroke-width="3" stroke-dasharray="12 10"/>')
        svg.append(f'<text x="{w - 6}" y="{ry - 12:.0f}" text-anchor="end" class="sv sm">{esc(ref_label)}</text>')
    for i, (label, v, col, vt) in enumerate(items):
        x = pad_l + gap * (i + 1) + bw * i
        bh = (base - pad_t) * v / vmax
        y = base - bh
        svg.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{bw:.0f}" height="{bh:.0f}" fill="{col}" stroke="#1B4332" stroke-width="4"/>')
        svg.append(f'<text x="{x + bw / 2:.0f}" y="{y - 16:.0f}" text-anchor="middle" class="sv big">{esc(vt)}</text>')
        svg.append(f'<text x="{x + bw / 2:.0f}" y="{base + 44}" text-anchor="middle" class="sv">{esc(label)}</text>')
    svg.append("</svg>")
    return "".join(svg)


def hbar(label, part, total, part_label, color="#B42318", w=1100):
    pct = part / total
    return (f'<div class="hb"><div class="hbl">{label}</div><div class="hbt" style="width:{w}px">'
            f'<div class="hbf" style="width:{pct * 100:.1f}%;background:{color}"></div></div>'
            f'<div class="hbv">{part_label}</div></div>')


def tiles(items, cols=4, cls=""):
    """items: (title, sub, kind)."""
    t = "".join(f'<div class="tile {k}"><b>{a}</b><small>{b}</small></div>' for a, b, k in items)
    return f'<div class="tiles {cls}" style="grid-template-columns:repeat({cols},1fr)">{t}</div>'


def cycle(nodes, r=250, size=640):
    """Nodes placed on a circle with curved arrows between them (SVG + html labels)."""
    import math
    n = len(nodes)
    cx = cy = size / 2
    pts = [(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + r * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]
    svg = [f'<svg class="cyc" width="{size}" height="{size}" viewBox="0 0 {size} {size}">',
           '<defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#1B4332"/></marker></defs>',
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#D8CFBB" stroke-width="6"/>']
    for i in range(n):
        a0 = -math.pi / 2 + 2 * math.pi * (i + 0.22) / n
        a1 = -math.pi / 2 + 2 * math.pi * (i + 0.78) / n
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        svg.append(f'<path d="M{x0:.0f},{y0:.0f} A{r},{r} 0 0 1 {x1:.0f},{y1:.0f}" fill="none" stroke="#1B4332" stroke-width="6" marker-end="url(#ah)"/>')
    svg.append("</svg>")
    labels = "".join(f'<div class="cn {k}" style="left:{x:.0f}px;top:{y:.0f}px">{t}</div>' for (x, y), (t, k) in zip(pts, nodes))
    return f'<div class="cycw" style="width:{size}px;height:{size}px">{"".join(svg)}{labels}</div>'


def skel(widths, cls=""):
    """Grey skeleton text lines (a mock UI with no invented words)."""
    return "".join(f'<div class="sk {cls}" style="width:{w}%"></div>' for w in widths)


# ---------------------------------------------------------------- word check

class _CopyCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.words = [], []

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class", "") or ""
        self.stack.append("c" in cls.split() and "needs" not in cls.split())

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if any(self.stack):
            self.words += re.findall(r"[A-Za-z0-9][A-Za-z0-9'.,%+:/-]*", data)


def copy_words(fragment):
    p = _CopyCounter()
    # void tags would break the stack; strip them first
    p.feed(re.sub(r"<(br|i|img|hr)\b[^>]*/?>", " ", fragment))
    return p.words


# ---------------------------------------------------------------- board

CSS = r"""
:root{--ground:#F7F3EA;--card:#fff;--ink:#1B4332;--body:#1B1B1B;--muted:#5F6B62;--accent:#E9B949;
--sage:#52B788;--soft:#B7E4C7;--line:#D8CFBB;--red:#B42318;--deep:#0E2418}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:var(--deep)}
body{font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;color:var(--body);-webkit-font-smoothing:antialiased}
#stage{position:absolute;left:0;top:0;width:1600px;height:900px;overflow:hidden;transform-origin:0 0;background:var(--ground)}
#map{position:absolute;left:0;top:0;width:__W__px;height:__H__px;transform-origin:0 0;
 background-color:var(--ground);background-image:radial-gradient(#D3C9B3 3px,transparent 3.6px);background-size:64px 64px}
#map.anim{transition:transform .8s ease}
.wires{position:absolute;left:0;top:0;pointer-events:none}
.region{position:absolute;border:8px solid var(--line);border-radius:80px;background:rgba(27,67,50,.035)}
.rlabel{position:absolute;left:90px;top:70px;display:flex;align-items:center;gap:50px;font-weight:900;font-size:230px;letter-spacing:-.04em;color:var(--ink);line-height:1;white-space:nowrap}
.rlabel span{font:800 170px 'JetBrains Mono',monospace;background:var(--ink);color:var(--accent);padding:20px 44px;border-radius:30px}
.maptitle{position:absolute;font-weight:900;color:var(--ink);letter-spacing:-.045em;line-height:.95}
.maptitle em{font-style:normal;background:var(--accent);padding:0 .08em;border-radius:.08em}
.zone{position:absolute;width:1600px;height:900px;background:var(--card);border:5px solid var(--ink);border-radius:34px;
 padding:50px 72px 46px;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 22px 0 rgba(27,67,50,.10)}
.zone.dark{background:var(--ink);color:#fff}
.ztag{font:700 22px 'JetBrains Mono',monospace;letter-spacing:.18em;color:var(--muted);text-transform:uppercase;display:flex;gap:16px;align-items:center}
.ztag .n{background:var(--ink);color:var(--accent);padding:5px 14px;border-radius:8px}
.dark .ztag{color:var(--soft)} .dark .ztag .n{background:var(--accent);color:var(--ink)}
.zh{font-size:70px;font-weight:900;letter-spacing:-.035em;color:var(--ink);line-height:1.02;margin-top:16px}
.zh em{font-style:normal;background:var(--accent);padding:0 .1em;border-radius:6px}
.dark .zh{color:#fff}
.zv{flex:1;display:flex;align-items:center;justify-content:center;margin-top:26px;min-height:0;gap:40px;position:relative}
.col{flex-direction:column}
.lbl{font:600 25px 'JetBrains Mono',monospace;color:var(--muted);letter-spacing:.02em}
.src{position:absolute;right:72px;bottom:26px;font:600 22px 'JetBrains Mono',monospace;color:var(--muted)}
.needs{display:inline-block;background:var(--red);color:#fff;font:800 28px 'JetBrains Mono',monospace;padding:8px 16px;border-radius:8px;letter-spacing:.02em;box-shadow:0 0 0 4px #fff,0 0 0 8px var(--red)}
/* window */
.win{background:#fff;border:4px solid var(--ink);border-radius:18px;overflow:hidden;box-shadow:0 14px 0 rgba(27,67,50,.12)}
.wbar{background:var(--ink);height:60px;display:flex;align-items:center;gap:10px;padding:0 20px}
.wbar i{width:16px;height:16px;border-radius:50%;background:#F7F3EA;opacity:.55}
.wbar span{margin-left:14px;font:700 25px 'JetBrains Mono',monospace;color:var(--accent)}
.wbody{padding:26px 34px;font:500 28px 'JetBrains Mono',monospace;color:var(--body)}
.row{display:flex;gap:26px;padding:9px 12px;border-bottom:2px solid #EFE9DC;align-items:center}
.row b{color:var(--ink);min-width:420px;font-weight:700}
.row span{color:var(--muted)}
.row.hot{background:#FBEFC9}
.row.bad{background:#FBE3E0;color:var(--red)} .row.bad b,.row.bad span{color:var(--red)}
/* tree */
.tree{font-family:'JetBrains Mono',monospace;line-height:1.24;color:var(--ink);background:#FBF8F1;border:4px solid var(--ink);border-radius:18px;padding:22px 34px;white-space:pre}
.thl{background:var(--accent);color:var(--ink);font-weight:700}
.tred{background:#FBE3E0;color:var(--red);font-weight:700}
/* flow */
.flow{display:flex;align-items:stretch;width:100%}
.node{flex:1;background:#fff;border:5px solid var(--ink);border-radius:20px;padding:28px 20px;min-height:180px;display:flex;flex-direction:column;justify-content:center;text-align:center}
.node b{font-size:38px;font-weight:800;color:var(--ink);line-height:1.15}
.node small{margin-top:12px;font:600 23px 'JetBrains Mono',monospace;color:var(--muted);line-height:1.3}
.node.on{background:var(--accent)} .node.on small{color:var(--ink)}
.node.dark{background:var(--ink)} .node.dark b{color:#fff} .node.dark small{color:var(--soft)}
.node.red{background:#FBE3E0;border-color:var(--red)} .node.red b,.node.red small{color:var(--red)}
.node.sage{background:var(--soft)}
.arr{display:flex;align-items:center;justify-content:center;width:62px;flex:none;font-size:46px;font-weight:900;color:var(--ink)}
.flow.sm .node b{font-size:32px} .flow.sm .arr{width:44px;font-size:38px} .flow.sm .node{padding:20px 10px;min-height:150px}
.trow{display:flex;align-items:center;gap:22px}
.flow.xa .node b{font-size:27px}.flow.xa .node small{font:900 40px Inter;color:inherit;order:-1;margin:0 0 8px}
.flow.xa .node.dark small{color:#E9B949}
/* split */
.split{display:flex;gap:36px;width:100%;height:100%}
.half{flex:1;border-radius:22px;padding:58px 34px 28px;position:relative;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:22px}
.half.bef{background:#F6E9E6;border:4px solid #D9A79F}
.half.aft{background:#E3F2E8;border:4px solid var(--sage)}
.badge{position:absolute;top:20px;left:26px;font:800 26px 'JetBrains Mono',monospace;letter-spacing:.2em;padding:5px 14px;border-radius:8px;color:#fff}
.bef .badge{background:var(--red)} .aft .badge{background:var(--ink)}
/* tiles */
.tiles{display:grid;gap:22px;width:100%}
.tile{background:#fff;border:5px solid var(--ink);border-radius:20px;padding:28px 28px;display:flex;flex-direction:column;gap:12px;min-height:150px;justify-content:center}
.tile b{font:800 36px 'JetBrains Mono',monospace;color:var(--ink)}
.tile small{font:600 25px 'JetBrains Mono',monospace;color:var(--muted);line-height:1.3}
.tile.on{background:var(--accent)} .tile.on small{color:var(--ink)}
.tile.off{background:#EFE9DC;border-color:#CFC6B2} .tile.off b{color:#B0A68F}
.tile.red{background:#FBE3E0;border-color:var(--red)} .tile.red b,.tile.red small{color:var(--red)}
.tile.sage{background:var(--soft)}
.tile.dark{background:var(--ink)} .tile.dark b{color:var(--accent)} .tile.dark small{color:var(--soft)}
/* chart */
.chart .sv{font:700 28px 'JetBrains Mono',monospace;fill:#1B4332}
.chart .sv.big{font:900 52px 'Inter',sans-serif}
.chart .sv.sm{font:600 20px 'JetBrains Mono',monospace;fill:#5F6B62}
.hb{display:flex;align-items:center;gap:24px;margin:14px 0}
.hbl{font:700 27px 'JetBrains Mono',monospace;color:var(--ink);width:300px;text-align:right}
.hbt{height:72px;background:#EFE9DC;border:4px solid var(--ink);border-radius:10px;overflow:hidden}
.hbf{height:100%}
.hbv{font:900 44px 'Inter';color:var(--ink);white-space:nowrap}
/* big number */
.bign{font-size:300px;font-weight:900;letter-spacing:-.06em;color:var(--ink);line-height:.9}
.bign em{font-style:normal;color:var(--accent);-webkit-text-stroke:6px var(--ink)}
.bigl{font-size:58px;font-weight:800;color:var(--ink);letter-spacing:-.02em;line-height:1.1}
/* cycle */
.cycw{position:relative}
.cyc{position:absolute;left:0;top:0}
.cn{position:absolute;transform:translate(-50%,-50%);background:#fff;border:5px solid var(--ink);border-radius:18px;padding:16px 20px;font:700 26px 'JetBrains Mono',monospace;color:var(--ink);text-align:center;width:310px;line-height:1.25}
.cn.on{background:var(--accent)} .cn.dark{background:var(--ink);color:#fff}
/* skeleton */
.sk{height:26px;background:#DCD5C6;border-radius:6px;margin:12px 0}
.sk.hot{background:var(--accent)} .sk.red{background:#E7A59D} .sk.sage{background:var(--sage)}
.chip{display:inline-flex;align-items:center;gap:12px;background:#fff;border:5px solid var(--ink);border-radius:999px;padding:16px 30px;font:700 30px 'JetBrains Mono',monospace;color:var(--ink)}
.chip.on{background:var(--accent)} .chip.red{border-color:var(--red);color:var(--red);background:#FBE3E0}
.tag3{font:800 40px 'JetBrains Mono',monospace;padding:14px 26px;border-radius:12px;border:4px solid var(--ink)}
.strike{text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:var(--red)}
/* roadmap */
.rm{display:flex;gap:34px;width:100%}
.rmc{flex:1;border:5px solid var(--ink);border-radius:26px;padding:34px;display:flex;flex-direction:column;gap:22px;background:#FBF8F1;height:520px}
.rmc .k{font:800 64px 'JetBrains Mono',monospace;color:var(--ink);background:var(--accent);align-self:flex-start;padding:4px 20px;border-radius:12px}
.rmc .t{font-size:58px;font-weight:900;color:var(--ink);letter-spacing:-.03em}
.rmc .ico{flex:1;display:flex;align-items:flex-end}
/* notes overlay */
#notes{position:fixed;left:0;right:0;bottom:0;max-height:46vh;overflow:auto;background:rgba(14,36,24,.94);color:#F7F3EA;
 padding:22px 32px 26px;font:400 19px/1.5 'Inter',sans-serif;border-top:4px solid var(--accent);z-index:9;display:none}
#notes.on{display:block}
#notes .h{font:700 14px 'JetBrains Mono',monospace;letter-spacing:.16em;color:var(--accent);text-transform:uppercase;margin-bottom:8px}
#notes p{margin:6px 0;max-width:1200px}
#notes .os{color:#B7E4C7}
"""

JS = r"""
const F=__FRAMES__;
const stage=document.getElementById('stage'),map=document.getElementById('map'),nb=document.getElementById('notes');
let i=0;
function fit(){const k=Math.min(innerWidth/1600,innerHeight/900);
 stage.style.transform=`translate(${(innerWidth-1600*k)/2}px,${(innerHeight-900*k)/2}px) scale(${k})`;}
function cam(n){i=Math.max(0,Math.min(F.length-1,n));const f=F[i],[x,y,w,h]=f.r,p=f.p;
 const s=Math.min(1600/w,900/h)*p,tx=(1600-w*s)/2-x*s,ty=(900-h*s)/2-y*s;
 map.style.transform=`translate(${tx}px,${ty}px) scale(${s})`;
 nb.innerHTML=`<div class="h">Frame ${i+1} / ${F.length} &middot; ${f.t} &middot; ${f.k}</div>${f.n}`;
 history.replaceState(null,'','#'+(i+1));}
function start(){const m=(location.hash||'').match(/\d+/);return m?parseInt(m[0],10)-1:0;}
fit();cam(start());
requestAnimationFrame(()=>requestAnimationFrame(()=>map.classList.add('anim')));
addEventListener('resize',fit);
addEventListener('keydown',e=>{
 if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();cam(i+1);}
 else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();cam(i-1);}
 else if(e.key==='Home'){cam(0);} else if(e.key==='End'){cam(F.length-1);}
 else if(e.key==='n'||e.key==='N'){nb.classList.toggle('on');}
 else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
});
"""


def zone_html(z):
    num = z.get("num", "")
    tag = f'<div class="ztag"><span class="n">{esc(num)}</span>{esc(z.get("tag", ""))}</div>' if (num or z.get("tag")) else ""
    head = f'<div class="zh c">{z["head"]}</div>' if z.get("head") else ""
    vcls = "zv " + z.get("vcls", "")
    src = f'<div class="src">{z["src"]}</div>' if z.get("src") else ""
    return (f'<div class="zone {z.get("cls", "")}" data-zone="{z["id"]}" style="left:{z["x"]}px;top:{z["y"]}px">'
            f'{tag}{head}<div class="{vcls}">{z["body"]}</div>{src}</div>')


def anchor(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    if bx >= ax + aw:
        return (ax + aw, ay + ah / 2), (bx, by + bh / 2), "h"
    if bx + bw <= ax:
        return (ax, ay + ah / 2), (bx + bw, by + bh / 2), "h"
    if by >= ay + ah:
        return (ax + aw / 2, ay + ah), (bx + bw / 2, by), "v"
    return (ax + aw / 2, ay), (bx + bw / 2, by + bh), "v"


def wire(a, b, color="#1B4332", width=16, dash=""):
    (x0, y0), (x1, y1), d = anchor(a, b)
    if d == "h":
        m = (x1 - x0) * 0.5
        path = f"M{x0:.0f},{y0:.0f} C{x0 + m:.0f},{y0:.0f} {x1 - m:.0f},{y1:.0f} {x1 - (40 if x1 > x0 else -40):.0f},{y1:.0f}"
    else:
        m = (y1 - y0) * 0.5
        path = f"M{x0:.0f},{y0:.0f} C{x0:.0f},{y0 + m:.0f} {x1:.0f},{y1 - m:.0f} {x1:.0f},{y1 - (40 if y1 > y0 else -40):.0f}"
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{width}"{da} marker-end="url(#wa)"/>'


def snake(col_a, col_b, n):
    """Slots for n zones in a 2-column region: down column a, up column b."""
    rows = (n + 1) // 2
    slots = [(COLS[col_a], ROWS[r]) for r in range(rows)] + [(COLS[col_b], ROWS[r]) for r in reversed(range(rows))]
    return slots[:n], rows


def build(video):
    """video: dict with keys doc, slug, title_html, title_text, hook (result zone, roadmap zone),
    regions: [ {num,label,zones:[...]} x3 ], cta zone, final note, timings in zones as 'sec'."""
    zones, frames, region_html, wires = [], [], [], []
    rects = {}

    def add_zone(z, x, y):
        z = dict(z)
        z["x"], z["y"] = x, y
        rects[z["id"]] = (x, y, ZW, ZH)
        zones.append(z)
        return z

    # hook row: result at col0, roadmap at col1, CTA above the last region column
    res = add_zone(video["result"], COLS[0], TOP_Y)
    road = add_zone(video["roadmap"], COLS[1], TOP_Y)

    path = [res["id"], road["id"]]
    region_rects = []
    for ri, reg in enumerate(video["regions"]):
        slots, rows = snake(ri * 2, ri * 2 + 1, len(reg["zones"]))
        rx, ry = COLS[ri * 2] - 110, 1500
        rw = COLS[ri * 2 + 1] + ZW + 110 - rx
        rh = ROWS[rows - 1] + ZH + 130 - ry
        reg["rect"] = (rx, ry, rw, rh)
        region_rects.append(reg["rect"])
        region_html.append(f'<div class="region" style="left:{rx}px;top:{ry}px;width:{rw}px;height:{rh}px">'
                           f'<div class="rlabel c"><span>{reg["num"]}</span>{esc(reg["label"])}</div></div>')
        for z, (x, y) in zip(reg["zones"], slots):
            add_zone(z, x, y)
            path.append(z["id"])
    last_col = COLS[5]
    cta = add_zone(video["cta"], last_col, TOP_Y)
    path.append(cta["id"])

    # wires: the camera path, plus the entry arrow from the roadmap into region 1
    for a, b in zip(path, path[1:]):
        if a == road["id"]:
            r1 = region_rects[0]
            ra = rects[a]
            x = ra[0] + ra[2] / 2
            wires.append(f'<path d="M{x:.0f},{ra[1] + ra[3]:.0f} L{x:.0f},{r1[1] - 40:.0f}" fill="none" stroke="#E9B949" stroke-width="30" marker-end="url(#wb)"/>')
            continue
        cross = any(a in [z["id"] for z in r["zones"]] and b not in [z["id"] for z in r["zones"]] for r in video["regions"])
        if cross:
            wires.append(wire(rects[a], rects[b], "#E9B949", 30).replace("url(#wa)", "url(#wb)"))
        else:
            wires.append(wire(rects[a], rects[b]))

    # frames
    def fr(kind, rect, pad, sec, notes, onscreen):
        frames.append({"k": kind, "r": list(rect), "p": pad, "sec": sec, "n": notes, "os": onscreen})

    ov = video["overview"]
    fr("overview", (0, 0, W, H), 0.985, ov["sec"], ov["say"], ov["on"])
    for z in (res, road):
        fr(z["id"], rects[z["id"]], 0.95, z["sec"], z["say"], z.get("on", ""))
    for reg in video["regions"]:
        fr("region " + reg["num"], reg["rect"], 0.97, reg["sec"], reg["say"], reg["on"])
        for z in reg["zones"]:
            fr(z["id"], rects[z["id"]], 0.95, z["sec"], z["say"], z.get("on", ""))
    fr(cta["id"], rects[cta["id"]], 0.95, cta["sec"], cta["say"], cta.get("on", ""))
    fin = video["final"]
    fr("overview, end", (0, 0, W, H), 0.985, fin["sec"], fin["say"], fin["on"])

    # timings
    t = 0
    for f in frames:
        f["start"], t = t, t + f["sec"]
        f["t"] = f"{f['start'] // 60}:{f['start'] % 60:02d} to {t // 60}:{t % 60:02d}"
    total = t

    # word check
    problems = []
    title_words = copy_words(f'<div class="c">{video["title_html"]}</div>')
    for f in frames:
        if f["k"].startswith("overview"):
            n = len(title_words)
        elif f["k"].startswith("region"):
            reg = next(r for r in video["regions"] if f["k"] == "region " + r["num"])
            n = len(reg["label"].split())
        else:
            z = next(z for z in zones if z["id"] == f["k"])
            n = len(copy_words(zone_html(z)))
        f["words"] = n
        if n > 8:
            problems.append(f"{video['doc']} {f['k']}: {n} words")
    if problems:
        raise SystemExit("8-word rule broken:\n" + "\n".join(problems))
    for s in ("—", "–"):
        blob = json.dumps(video, ensure_ascii=False)
        if s in blob:
            raise SystemExit(f"{video['doc']}: dash character {s!r} found")

    title = f'<div class="maptitle c" style="left:{COLS[2] - 100}px;top:{TOP_Y - 60}px;font-size:{video.get("title_size", 420)}px;width:{COLS[5] - COLS[2] - 100}px">{video["title_html"]}</div>'
    svg = (f'<svg class="wires" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>'
           '<marker id="wa" viewBox="0 0 10 10" refX="4" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1B4332"/></marker>'
           '<marker id="wb" viewBox="0 0 10 10" refX="4" refY="5" markerWidth="3.4" markerHeight="3.4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#E9B949"/></marker>'
           f'</defs>{"".join(wires)}</svg>')
    js_frames = [{"r": f["r"], "p": f["p"], "t": f["t"], "k": esc(f["k"]),
                  "n": f'<p class="os"><b>On screen:</b> {esc(f["os"])}</p>' + "".join(f"<p>{esc(s)}</p>" for s in f["n"])} for f in frames]
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(video['doc'])} · {esc(video['title_text'])} · canvas</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS.replace('__W__', str(W)).replace('__H__', str(H))}</style></head>
<body><div id="stage"><div id="map">{''.join(region_html)}{svg}{title}{''.join(zone_html(z) for z in zones)}</div></div>
<div id="notes"></div>
<script>{JS.replace('__FRAMES__', json.dumps(js_frames))}</script>
</body></html>"""
    page = controls.inject(page, NAV_ADAPTER)
    return page, frames, total


def notes_md(video, frames, total):
    out = [f"# {video['doc']} · {video['title_text']} · canvas flythrough", "",
           f"Board: `{video['doc']}-{video['slug']}.html` · {len(frames)} frames · about {round(total / 60)} minutes.",
           "Keys: right arrow or space moves the camera to the next zone, left goes back, N shows these lines, F is fullscreen.",
           "",
           "**Copy convention.** At most 8 words of copy per frame, counted by the build script. The overview frames "
           "count only the map title. Region labels and the short labels inside diagrams, charts, code and trees are "
           "map labels, which BRIEF.md rule 1 exempts. A red `[NEEDS: x]` tag is a gap for Mauro, never copy.", ""]
    if video.get("needs"):
        out += ["**Open gaps on this board:** " + "; ".join(video["needs"]), ""]
    for i, f in enumerate(frames, 1):
        out.append(f"## Frame {i} · {f['t']} · {f['k']}")
        out.append("")
        out.append(f"**On screen:** {f['os']}")
        out.append("")
        for s in f["n"]:
            out.append(s)
            out.append("")
    return "\n".join(out)
