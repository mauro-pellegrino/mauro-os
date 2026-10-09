"""Keynote engine for the v2 YouTube boards, format A.

Discrete 16:9 slides on a fixed 1600x900 stage, scaled to the viewport. Elements with
data-s="n" build in on the nth arrow press. Elements with data-h="n" are always visible
and light up in honey on the nth press. N toggles the presenter notes, F fullscreen.

URL params for rendering: ?s=7 opens frame 7, &all=1 reveals every build on that frame,
&notes=1 opens the notes overlay.

Palette from boards/yt/build.py: cream ground, Deep Forest #1B4332, Honey #E9B949.
"""
import html as _html
import json
import re
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import controls  # noqa: E402  (shared recording control bar, boards/yt/v2/controls.py)

NAV_ADAPTER = "{count:()=>S.length,index:()=>i,go:n=>{i=Math.max(0,Math.min(S.length-1,n));st=0;show();},next:nx,prev:pv,label:k=>NOTES[k].t+' · '+S[k].textContent.slice(0,90)}"

INK, ACC, GROUND, MUTED, SOFT, LINE, RED = "#1B4332", "#E9B949", "#F7F3EA", "#5F6B62", "#B9C7BE", "#D8CFBB", "#C0392B"

CSS = """
:root{--ground:#F7F3EA;--card:#FFFFFF;--ink:#1B4332;--body:#1B1B1B;--muted:#5F6B62;--accent:#E9B949;
--soft:#B9C7BE;--line:#D8CFBB;--red:#C0392B;--deep:#0E2418}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:var(--ground)}
body{font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;color:var(--body);-webkit-font-smoothing:antialiased}
.mono{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace}
#stage{position:absolute;left:50%;top:50%;width:1600px;height:900px;transform-origin:center center;background:var(--ground);overflow:hidden}
.slide{position:absolute;inset:0;display:none;padding:86px 110px 70px}
.slide.active{display:block}
.slide.dark{background:var(--ink);color:#fff}
.slide.honey{background:var(--accent)}
[data-s]{opacity:0;transition:opacity .4s ease,transform .4s ease}
[data-s].on{opacity:1}
.b[data-s]{transform:translateY(22px)}
.b[data-s].on{transform:none}
[data-h]{transition:background .3s,color .3s,fill .3s,border-color .3s}
.hd{font-size:76px;font-weight:900;line-height:1.02;letter-spacing:-.035em;color:var(--ink);max-width:1380px}
.dark .hd{color:#fff}
.hd em{font-style:normal;background:var(--accent);color:var(--ink);padding:0 .12em}
.hd.c{text-align:center;margin:0 auto}
.hd.sm{font-size:62px}
.vis{position:absolute;left:110px;right:110px;top:250px;bottom:70px;display:flex;align-items:center;justify-content:center}
.vis.top{align-items:flex-start}
.chip,.tag{display:inline-block;font:800 15px 'JetBrains Mono',ui-monospace,monospace;letter-spacing:.16em;text-transform:uppercase;padding:7px 12px;background:var(--ink);color:var(--accent)}
.chip.y,.tag.y{background:var(--accent);color:var(--ink)}
.chip.r,.tag.r{background:var(--red);color:#fff}
.needs{display:inline-block;background:var(--red);color:#fff;font:800 22px 'JetBrains Mono',ui-monospace,monospace;padding:8px 14px;letter-spacing:.02em;line-height:1.2}
.needs.sm{font-size:16px;padding:5px 10px}
.src,.cite{font:600 16px 'JetBrains Mono',ui-monospace,monospace;color:var(--muted);letter-spacing:.04em}
.dark .src,.dark .cite{color:#9FB8A8}
/* giant number */
.giant{font-size:430px;font-weight:900;letter-spacing:-.06em;line-height:.8;color:var(--ink)}
.giant.y{color:var(--accent)}
.dark .giant{color:var(--accent)}
.giant.md{font-size:300px}
.glabel{font-size:58px;font-weight:800;color:var(--ink);letter-spacing:-.02em;line-height:1.05}
.dark .glabel{color:#fff}
/* agenda */
.agenda{display:flex;gap:28px;width:100%}
.ag{flex:1;border:4px solid var(--ink);background:var(--card);padding:34px 32px;height:400px;display:flex;flex-direction:column;justify-content:space-between}
.ag .n{font-size:150px;font-weight:900;line-height:.8;color:var(--soft);letter-spacing:-.05em}
.ag .t{font-size:52px;font-weight:900;color:var(--ink);letter-spacing:-.02em}
.ag.live{background:var(--ink)}
.ag.live .n{color:var(--accent)}
.ag.live .t{color:#fff}
.ag.dim{opacity:.35}
/* boxes and flows */
.row{display:flex;align-items:center;gap:0;width:100%}
.nd{flex:1;border:4px solid var(--ink);background:var(--card);padding:22px 18px;font-size:28px;font-weight:800;color:var(--ink);text-align:center;line-height:1.15;min-height:120px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.nd small{display:block;font:600 19px 'JetBrains Mono',monospace;color:var(--muted);margin-top:8px;letter-spacing:.04em}
.nd.dk{background:var(--ink);color:#fff}
.nd.dk small{color:#9FB8A8}
.nd.y{background:var(--accent)}
.nd.bad{border-color:var(--red);color:var(--red);background:#FBEDEA}
.nd.ghost{border-style:dashed;background:transparent;color:var(--muted)}
.ar{flex:none;width:58px;text-align:center;font-size:40px;font-weight:900;color:var(--ink)}
.ar.r{color:var(--red)}
.panel{border:4px solid var(--ink);background:var(--card);padding:26px 28px}
.panel .lab{font:800 16px 'JetBrains Mono',monospace;letter-spacing:.18em;color:var(--muted);margin-bottom:16px;text-transform:uppercase}
.split{display:grid;grid-template-columns:1fr 1fr;gap:40px;width:100%}
.lit{background:var(--accent)!important;color:var(--ink)!important}
pre.tree{background:var(--deep);color:#EAF2EC;font:500 25px/1.36 'JetBrains Mono',ui-monospace,monospace;padding:26px 32px;white-space:pre;border:4px solid var(--ink)}
pre.tree .r{display:inline-block;padding:0 6px;margin:0 -6px}
pre.tree em{font-style:normal;color:#7FA08C}
pre.code{background:var(--deep);color:#EAF2EC;font:500 24px/1.5 'JetBrains Mono',ui-monospace,monospace;padding:28px 34px;white-space:pre;border:4px solid var(--ink)}
pre.code .del{color:#F19A8E;text-decoration:line-through}
pre.code .add{color:var(--accent)}
pre.code em{font-style:normal;color:#7FA08C}
table.tb{width:100%;border-collapse:collapse;background:var(--card);border:4px solid var(--ink)}
table.tb td{padding:20px 26px;font-size:30px;font-weight:700;color:var(--ink);border-bottom:3px solid var(--line)}
table.tb td:first-child{font:800 26px 'JetBrains Mono',monospace;white-space:nowrap;width:40%}
table.tb tr.lit td{background:var(--accent)}
.sq{display:grid;gap:10px}
.sq i{display:block;aspect-ratio:1;background:var(--soft);border-radius:4px}
.sq i.g{background:var(--ink)}
.sq i.y{background:var(--accent)}
.sq i.r{background:var(--red)}
.cta{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center;gap:40px}
.cta .big{font-size:110px;font-weight:900;letter-spacing:-.04em;color:#fff;line-height:1}
.cta .offer{font-size:64px;font-weight:900;background:var(--accent);color:var(--ink);padding:18px 40px;letter-spacing:-.02em}
svg text{font-family:'Inter',-apple-system,Arial,sans-serif}
svg .m{font-family:'JetBrains Mono',ui-monospace,monospace}
/* notes overlay */
#notes{position:fixed;left:0;right:0;bottom:0;max-height:46vh;overflow:auto;background:rgba(14,36,24,.97);color:#EAF2EC;
padding:18px 28px 22px;font:500 18px/1.5 'Inter',sans-serif;display:none;z-index:9;border-top:4px solid var(--accent)}
#notes.open{display:block}
#notes .meta{font:700 13px 'JetBrains Mono',monospace;letter-spacing:.14em;color:var(--accent);margin-bottom:8px}
#notes p{margin:0 0 8px;max-width:1200px}
"""

JS = r"""
const S=[...document.querySelectorAll('.slide')];const NOTES=JSON.parse(document.getElementById('nd').textContent);
let i=0,st=0;const q=new URLSearchParams(location.search);
function mx(sl){let m=0;sl.querySelectorAll('[data-s],[data-h]').forEach(e=>{m=Math.max(m,+(e.dataset.s||e.dataset.h))});return m}
function show(){S.forEach((s,k)=>s.classList.toggle('active',k===i));const sl=S[i];
 sl.querySelectorAll('[data-s]').forEach(e=>e.classList.toggle('on',+e.dataset.s<=st));
 sl.querySelectorAll('[data-h]').forEach(e=>e.classList.toggle('lit',+e.dataset.h<=st&&+e.dataset.h>0));
 const n=NOTES[i];const box=document.getElementById('notes');
 box.innerHTML='<div class="meta">FRAME '+(i+1)+' / '+S.length+' &middot; '+n.t+' &middot; BUILD '+st+' / '+mx(sl)+'</div>'+n.h;
 history.replaceState(null,'','?s='+(i+1)+(q.get('all')?'&all=1':''));}
function nx(){if(st<mx(S[i]))st++;else if(i<S.length-1){i++;st=0}show()}
function pv(){if(st>0)st--;else if(i>0){i--;st=mx(S[i])}show()}
function fit(){const k=Math.min(innerWidth/1600,innerHeight*__SAFE_H__/900),g=document.getElementById('stage');g.style.top=(450*k)+'px';g.style.transform='translate(-50%,-50%) scale('+k+')'}  // facecam safe zones: stage in the top band
addEventListener('resize',fit);
addEventListener('keydown',e=>{if(['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)){e.preventDefault();nx()}
 else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();pv()}
 else if(e.key==='n'||e.key==='N'){document.getElementById('notes').classList.toggle('open')}
 else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
 else if(e.key==='Home'){i=0;st=0;show()}});
document.getElementById('stage').addEventListener('click',nx);
i=Math.max(0,Math.min(S.length-1,(+q.get('s')||1)-1));if(q.get('all'))st=mx(S[i]);
if(q.get('notes'))document.getElementById('notes').classList.add('open');fit();show();
"""

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<!-- Keys: right/left or space to build and move, N notes, F fullscreen. ?s=N&all=1 opens frame N fully built. -->
<div id="stage">
"""


def esc(s):
    return _html.escape(s, quote=False)


# ------------------------------------------------------------------ building blocks

def B(inner, s=None, cls="", style="", tag="div", h=None):
    a = f' data-s="{s}"' if s is not None else ""
    a += f' data-h="{h}"' if h is not None else ""
    c = f' class="b {cls}"' if s is not None else (f' class="{cls}"' if cls else "")
    st = f' style="{style}"' if style else ""
    return f"<{tag}{c}{a}{st}>{inner}</{tag}>"


def needs(x, sm=False):
    return f'<span class="needs{" sm" if sm else ""}">[NEEDS: {esc(x)}]</span>'


def hd(text, cls=""):
    return f'<h1 class="hd {cls}">{text}</h1>'


def vis(inner, cls="", style=""):
    return f'<div class="vis {cls}" style="{style}">{inner}</div>'


def agenda(items, live=None, steps=False):
    out = []
    for k, t in enumerate(items, 1):
        cls = "ag" + (" live" if live == k else (" dim" if live and live > k else ""))
        out.append(B(f'<div class="n">{k}</div><div class="t">{t}</div>', s=k if steps else None, cls=cls))
    return f'<div class="agenda">{"".join(out)}</div>'


def flow(nodes, arrows=None):
    """nodes: list of (html, cls, step). arrows: list of (char, cls) between nodes."""
    out = []
    for k, (h, cls, s) in enumerate(nodes):
        if k:
            ch, acls = (arrows[k - 1] if arrows else ("&rarr;", ""))
            out.append(B(ch, s=s, cls="ar " + acls) if s is not None else f'<div class="ar {acls}">{ch}</div>')
        out.append(B(h, s=s, cls="nd " + cls) if s is not None else f'<div class="nd {cls}">{h}</div>')
    return f'<div class="row">{"".join(out)}</div>'


def squares(n, cols, colors, size=None, s_map=None):
    """colors: function k -> css class. s_map: function k -> step or None."""
    cells = []
    for k in range(n):
        s = s_map(k) if s_map else None
        cells.append(f'<i class="{colors(k)}"{f" data-s={chr(34)}{s}{chr(34)}" if s is not None else ""}></i>')
    w = f"width:{size}px;" if size else ""
    return f'<div class="sq" style="grid-template-columns:repeat({cols},1fr);{w}">{"".join(cells)}</div>'


def vbars(bars, w=900, h=470, maxv=None, unit=""):
    """bars: list of (label, value, color, step, valuetext)."""
    maxv = maxv or max(b[1] for b in bars)
    n = len(bars)
    gap = 70
    bw = (w - gap * (n + 1)) / n
    base = h - 70
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
           f'<line x1="0" y1="{base}" x2="{w}" y2="{base}" stroke="{INK}" stroke-width="4"/>']
    for k, (lab, v, col, s, vt) in enumerate(bars):
        x = gap + k * (bw + gap)
        bh = (base - 70) * v / maxv
        sa = f' data-s="{s}"' if s is not None else ""
        out.append(f'<g{sa}><rect x="{x:.0f}" y="{base-bh:.0f}" width="{bw:.0f}" height="{bh:.0f}" fill="{col}"/>'
                   f'<text x="{x+bw/2:.0f}" y="{base-bh-18:.0f}" text-anchor="middle" font-size="54" font-weight="900" fill="{INK}">{vt}</text>'
                   f'<text x="{x+bw/2:.0f}" y="{base+48:.0f}" text-anchor="middle" font-size="28" font-weight="700" fill="{MUTED}" class="m">{lab}</text></g>')
    out.append("</svg>")
    return "".join(out)


def hbars(rows, w=1380, label_w=420, row_h=96, maxv=None):
    """rows: (label, value, color, step, valuetext)."""
    maxv = maxv or max(r[1] for r in rows)
    area = w - label_w - 230
    h = row_h * len(rows)
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    for k, (lab, v, col, s, vt) in enumerate(rows):
        y = k * row_h
        bl = area * v / maxv
        sa = f' data-s="{s}"' if s is not None else ""
        out.append(f'<g{sa}><text x="0" y="{y+row_h/2+10:.0f}" font-size="30" font-weight="800" fill="{INK}">{lab}</text>'
                   f'<rect x="{label_w}" y="{y+14}" width="{bl:.0f}" height="{row_h-28}" fill="{col}"/>'
                   f'<text x="{label_w+bl+18:.0f}" y="{y+row_h/2+16:.0f}" font-size="46" font-weight="900" fill="{INK}">{vt}</text></g>')
    out.append("</svg>")
    return "".join(out)


# ------------------------------------------------------------------ word check

def counted_words(slide_html):
    """Words a viewer reads as copy: the headline plus anything marked .cnt, .glabel, .ag .t, .cta.
    Chart labels (.cite), diagram node labels, code and [NEEDS] tags are exempt per the brief. .src and .chip count."""
    parts = re.findall(r'<h1 class="hd[^"]*">(.*?)</h1>', slide_html, re.S)
    parts += re.findall(r'class="[^"]*\b(?:cnt|glabel|big|offer|src|chip)\b[^"]*"[^>]*>(.*?)</', slide_html, re.S)
    parts += re.findall(r'<div class="t">(.*?)</div>', slide_html, re.S)
    text = " ".join(re.sub(r"<[^>]+>", " ", p) for p in parts)
    text = _html.unescape(text)
    return [w for w in re.split(r"\s+", text) if re.search(r"[A-Za-z0-9]", w)]


# ------------------------------------------------------------------ page

def fmt(sec):
    return f"{sec//60}:{sec%60:02d}"


def build(title, slides, notes_title, sources):
    """slides: list of dicts {html, dur, notes:[str], cls, onscreen}. Returns (html, notes_md, minutes, frames)."""
    t = 0
    nd = []
    body = []
    md = [f"# {notes_title}", "", "Presenter notes for the keynote board. Press N on the board to see the same text.",
          "Timing is cumulative. Lines are a guide to talk over. Say them in your own words.", "",
          "**Sources:** " + sources, ""]
    problems = []
    for k, sl in enumerate(slides, 1):
        a, b_ = t, t + sl["dur"]
        t = b_
        span = f"{fmt(a)} to {fmt(b_)}"
        words = counted_words(sl["html"])
        if len(words) > 8:
            problems.append(f"frame {k}: {len(words)} words: {' '.join(words)}")
        body.append(f'<section class="slide {sl.get("cls","")}">{sl["html"]}</section>')
        on = sl.get("onscreen", "")
        lines = sl["notes"]
        nd.append({"t": span, "h": (f"<p><b>On screen:</b> {esc(on)}</p>" if on else "") +
                   "".join(f"<p>{esc(x)}</p>" for x in lines)})
        md += [f"## Frame {k} · {span} · {sl.get('name','')}", ""]
        if on:
            md += [f"*On screen:* {on}", ""]
        md += [f"- {x}" for x in lines] + [""]
    html_out = HEAD.format(title=esc(title), css=CSS) + "\n".join(body) + "</div>\n" + \
        '<div id="notes"></div>\n<script type="application/json" id="nd">' + \
        json.dumps(nd).replace("</", "<\\/") + "</script>\n<script>" + JS + "</script>\n</body></html>\n"
    html_out = controls.inject(html_out, NAV_ADAPTER)
    md.insert(4, f"**Runtime:** {fmt(t)} across {len(slides)} frames.")
    return html_out, "\n".join(md), t, len(slides), problems
