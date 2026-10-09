"""Format C, terminal / IDE. Shared engine: page shell, player JS, dark-theme SVG helpers.

Every board is one HTML file. The frames are a JSON list embedded in the page. The player draws a
dark editor mock (explorer on the left, a terminal or an editor on the right, a status bar) and a
caption strip of at most 8 words. Arrow keys or space move between frames, N toggles the presenter
notes, F goes fullscreen. Add ?static=1 to the URL to skip the typing animation (used for the PNG).
"""
import html
import json
import re
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import controls  # noqa: E402  (shared recording control bar, boards/yt/v2/controls.py)

NAV_ADAPTER = "{count:()=>F.length,index:()=>i,go:show,next:()=>show(i+1),prev:()=>show(i-1),label:k=>F[k].t+' · '+F[k].caption}"

BG = "#0B1A12"
PANE = "#0F2219"
SIDE = "#0C1D15"
LINE = "#1F3A2C"
TXT = "#DCE8DF"
MUTED = "#86A293"
ACC = "#E9B949"
GREEN = "#52B788"
RED = "#F2555A"
BAR = "#5E8C73"


def esc(s):
    return html.escape(str(s), quote=False)


def mark(s):
    """Inline markup for terminal and editor lines: [[hl:..]] [[dim:..]] [[red:..]] [[g:..]] [[y:..]] [[b:..]]."""
    s = esc(s)
    return re.sub(r"\[\[(hl|dim|red|g|y|b|strike):(.*?)\]\]", lambda m: f'<span class="m-{m.group(1)}">{m.group(2)}</span>', s)


def words(caption):
    return len(re.sub(r"<[^>]+>", " ", caption).replace("&amp;", "&").split())


# ------------------------------------------------------------------ SVG helpers (dark theme)

def _t(x, y, s, size=22, fill=TXT, weight=600, anchor="start", family="Inter", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}, sans-serif" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" dominant-baseline="middle" {extra}>{esc(s)}</text>')


def hbar(rows, width=1180, label_w=360, row_h=52, fmt=lambda v: f"{v:g}", value_w=300, maxv=None, mono_labels=True):
    """Single-series horizontal bars. rows: (label, value, highlight, note). Bars drawn on |value|."""
    maxv = maxv or max(abs(r[1]) for r in rows) or 1
    area = width - label_w - value_w
    h = row_h * len(rows) + 8
    fam = "JetBrains Mono" if mono_labels else "Inter"
    out = [f'<svg class="chart" width="{width}" height="{h}" viewBox="0 0 {width} {h}" role="img">']
    for i, (label, v, hl, note) in enumerate(rows):
        y = i * row_h + 4
        w = max(abs(v) / maxv * area, 3)
        fill = ACC if hl else BAR
        cy = y + row_h / 2
        out.append(f'<g class="bar" style="animation-delay:{i*70}ms"><title>{esc(label)}: {esc(fmt(v))}</title>')
        out.append(_t(label_w - 18, cy, label, 21, TXT if hl else "#C4D3C9", 600, "end", fam))
        out.append(f'<rect x="{label_w}" y="{y+10}" width="{w:.1f}" height="{row_h-20}" rx="4" fill="{fill}"/>')
        val = esc(fmt(v)) + (f'<tspan font-size="17" font-weight="500" fill="{MUTED}">   {esc(note)}</tspan>' if note else "")
        out.append(f'<text x="{label_w+w+14:.1f}" y="{cy}" font-family="JetBrains Mono, monospace" font-size="23" font-weight="800" '
                   f'fill="{ACC if hl else TXT}" dominant-baseline="middle">{val}</text></g>')
    out.append(f'<line x1="{label_w}" y1="0" x2="{label_w}" y2="{h}" stroke="{MUTED}" stroke-width="2"/>')
    out.append("</svg>")
    return "".join(out)


def columns(rows, width=640, height=440, maxv=None, fmt=lambda v: f"{v:g}", col_w=170):
    """Vertical columns, single series. rows: (label, value, highlight)."""
    maxv = maxv or max(r[1] for r in rows)
    n = len(rows)
    gap = (width - n * col_w) / (n + 1)
    base = height - 56
    out = [f'<svg class="chart" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">']
    for i, (label, v, hl) in enumerate(rows):
        x = gap + i * (col_w + gap)
        hgt = v / maxv * (base - 70)
        out.append(f'<g class="bar" style="animation-delay:{i*90}ms"><title>{esc(label)}: {esc(fmt(v))}</title>'
                   f'<rect x="{x:.1f}" y="{base-hgt:.1f}" width="{col_w}" height="{hgt:.1f}" rx="4" fill="{ACC if hl else BAR}"/>')
        out.append(_t(x + col_w / 2, base - hgt - 24, fmt(v), 34, ACC if hl else TXT, 800, "middle", "JetBrains Mono"))
        out.append(_t(x + col_w / 2, base + 30, label, 21, TXT, 600, "middle") + "</g>")
    out.append(f'<line x1="0" y1="{base}" x2="{width}" y2="{base}" stroke="{MUTED}" stroke-width="2"/></svg>')
    return "".join(out)


def stacked(rows, width=1180):
    """rows: (title, total, [(label, value, highlight)]). One full-width bar per row, 2px surface gap between parts."""
    row_h = 140
    h = row_h * len(rows)
    out = [f'<svg class="chart" width="{width}" height="{h}" viewBox="0 0 {width} {h}" role="img">']
    for i, (title, total, parts) in enumerate(rows):
        y = i * row_h
        out.append(_t(0, y + 20, title, 22, TXT, 700))
        x = 0.0
        for j, (label, v, hl) in enumerate(parts):
            w = v / total * width
            gap = 2 if j else 0
            out.append(f'<g class="bar" style="animation-delay:{(i*2+j)*80}ms"><title>{esc(label)}</title>'
                       f'<rect x="{x+gap:.1f}" y="{y+40}" width="{max(w-gap,2):.1f}" height="54" rx="4" fill="{ACC if hl else BAR}"/>')
            if w > 300:
                out.append(_t(x + 18, y + 67, label, 22, "#0B1A12", 800))
            else:
                out.append(_t(x + w, y + 116, label, 19, TXT, 700, "end"))
            out.append("</g>")
            x += w
    out.append("</svg>")
    return "".join(out)


def flow(nodes, width=1180, box_h=120, gap=46, y0=10, label_size=22):
    """Left-to-right boxes. nodes: (kicker, label, sub, kind) with kind in '', 'hl', 'ghost', 'dark'."""
    n = len(nodes)
    bw = (width - gap * (n - 1)) / n
    h = box_h + y0 * 2
    out = [f'<svg class="chart" width="{width}" height="{h}" viewBox="0 0 {width} {h}" role="img">']
    for i, (k, lab, sub, kind) in enumerate(nodes):
        x = i * (bw + gap)
        stroke = ACC if kind == "hl" else (MUTED if kind == "ghost" else GREEN)
        fill = "#2A2410" if kind == "hl" else ("none" if kind == "ghost" else "#12301F")
        dash = ' stroke-dasharray="8 7"' if kind == "ghost" else ""
        out.append(f'<g class="bar" style="animation-delay:{i*90}ms"><rect x="{x:.1f}" y="{y0}" width="{bw:.1f}" height="{box_h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="2.5"{dash}/>')
        if k:
            out.append(_t(x + 16, y0 + 24, k, 15, ACC if kind == "hl" else MUTED, 700, "start", "JetBrains Mono"))
        out.append(_t(x + 16, y0 + (58 if k else 48), lab, label_size, MUTED if kind == "ghost" else TXT, 800))
        if sub:
            out.append(_t(x + 16, y0 + (92 if k else 82), sub, 16, MUTED, 500))
        out.append("</g>")
        if i < n - 1:
            ax = x + bw + 8
            out.append(f'<path d="M{ax:.1f} {y0+box_h/2} L{ax+gap-16:.1f} {y0+box_h/2}" stroke="{MUTED}" stroke-width="2.5" marker-end="url(#ah)"/>')
    out.insert(1, f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker></defs>')
    out.append("</svg>")
    return "".join(out)


def tiles(items, cols):
    """HTML stat tiles. items: (kicker, value, label, highlight)."""
    t = "".join(f'<div class="tile{" on" if on else ""}"><div class="tk">{esc(k)}</div><div class="tv">{esc(v)}</div>'
                f'<div class="tl">{esc(l)}</div></div>' for k, v, l, on in items)
    return f'<div class="tiles" style="grid-template-columns:repeat({cols},1fr)">{t}</div>'


def src(s):
    return f'<div class="src">{esc(s)}</div>'


def stack(*parts, gap=30):
    return f'<div class="vstack" style="gap:{gap}px">' + "".join(parts) + "</div>"


# ------------------------------------------------------------------ page shell

CSS = """
:root{--bg:%(BG)s;--pane:%(PANE)s;--side:%(SIDE)s;--line:%(LINE)s;--txt:%(TXT)s;--muted:%(MUTED)s;--acc:%(ACC)s;--green:%(GREEN)s;--red:%(RED)s}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%%;background:#050B08;overflow:hidden}
body{font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;color:var(--txt);-webkit-font-smoothing:antialiased}
.mono,pre,code{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace}
#stage{width:1600px;height:900px;position:absolute;left:50%%;top:50%%;transform-origin:center center;background:var(--bg);display:grid;
 grid-template-rows:34px 1fr 128px 28px;overflow:hidden}
.titlebar{display:flex;align-items:center;gap:9px;padding:0 16px;background:#081510;border-bottom:1px solid var(--line);font:600 14px 'JetBrains Mono',monospace;color:var(--muted)}
.titlebar i{width:12px;height:12px;border-radius:50%%;display:inline-block;background:#2B4637}
.titlebar i:nth-child(1){background:#E5484D}.titlebar i:nth-child(2){background:#E9B949}.titlebar i:nth-child(3){background:#52B788}
.titlebar span{margin-left:auto;margin-right:auto;transform:translateX(-30px)}
.mid{display:grid;grid-template-columns:318px 1fr;min-height:0}
.side{background:var(--side);border-right:1px solid var(--line);padding:14px 0;overflow:hidden;font:500 15.5px/1.62 'JetBrains Mono',monospace}
.side .h{font:700 12px 'JetBrains Mono',monospace;letter-spacing:.16em;color:var(--muted);padding:0 18px 8px;text-transform:uppercase}
.side .r{white-space:pre;padding:0 18px;color:#A9BDB0;transition:background .25s,color .25s}
.side .r.on{background:#1C3A2A;color:#fff;box-shadow:inset 3px 0 0 var(--acc)}
.side .r.dir{color:#D3E2D8}
.side .r.red{color:#6C8576;font-style:italic}
.main{display:grid;grid-template-rows:40px 1fr;min-width:0;min-height:0;background:var(--pane)}
.tabs{display:flex;align-items:flex-end;background:#0B1C14;border-bottom:1px solid var(--line);padding-left:6px;gap:2px}
.tab{font:600 14px 'JetBrains Mono',monospace;color:var(--muted);padding:10px 18px;border-top:2px solid transparent}
.tab.on{background:var(--pane);color:#fff;border-top-color:var(--acc)}
.content{position:relative;padding:26px 34px 18px;min-height:0;overflow:hidden}
.term{font:500 21px/1.55 'JetBrains Mono',monospace;white-space:pre-wrap;word-break:break-word;color:#CFDDD4}
.term .p{color:var(--green);font-weight:700}
.term .c{color:#fff;font-weight:700}
.cursor{display:inline-block;width:11px;height:24px;background:var(--acc);vertical-align:-4px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%%{opacity:0}}
.ed{font:500 19.5px/1.62 'JetBrains Mono',monospace;white-space:pre-wrap;word-break:break-word}
.ed .ln{display:grid;grid-template-columns:52px 1fr;gap:16px;padding:1px 10px 1px 0;border-left:3px solid transparent;transition:background .4s,opacity .4s}
.ed .ln b{color:#4E6A5A;font-weight:500;text-align:right}
.ed.focus .ln{opacity:.38}
.ed.focus .ln.hl{opacity:1;background:#2A2410;border-left-color:var(--acc);color:#fff}
.m-hl{background:var(--acc);color:#0B1A12;padding:0 4px;border-radius:3px;font-weight:800}
.m-dim{color:#5F7C6B}.m-red{color:var(--red);font-weight:700}.m-g{color:var(--green);font-weight:700}.m-y{color:var(--acc);font-weight:700}.m-b{color:#fff;font-weight:800}
.m-strike{text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:3px;color:#9AB0A2}
.split{display:grid;grid-template-columns:1fr 1fr;gap:34px;height:100%%}
.split>div{min-width:0;overflow:hidden}
.chartwrap{display:flex;flex-direction:column;justify-content:center;height:100%%}
.vstack{display:flex;flex-direction:column}
.src{margin-top:16px;font:500 14px 'JetBrains Mono',monospace;color:var(--muted)}
svg.chart{max-width:100%%;height:auto;overflow:visible}
svg.chart .bar{animation:grow .55s ease-out both}
@keyframes grow{from{opacity:0;transform:translateX(-12px)}to{opacity:1;transform:none}}
.tiles{display:grid;gap:18px}
.tile{background:#12301F;border:2px solid #2C5640;border-radius:8px;padding:18px 22px}
.tile.on{border-color:var(--acc);background:#2A2410}
.tk{font:700 13px 'JetBrains Mono',monospace;letter-spacing:.12em;color:var(--muted);text-transform:uppercase}
.tv{font:800 50px 'JetBrains Mono',monospace;color:#fff;margin-top:8px;letter-spacing:-.02em}
.tile.on .tv{color:var(--acc)}
.tl{font-size:18px;color:#B9CCBF;margin-top:6px;font-weight:600}
.needs{position:absolute;right:26px;bottom:14px;display:flex;flex-direction:column;align-items:flex-end;gap:8px;z-index:5}
.needs div{background:var(--red);color:#fff;font:800 15px 'JetBrains Mono',monospace;padding:6px 12px;border-radius:4px}
.cap{display:flex;align-items:center;gap:26px;padding:0 44px;background:#081510;border-top:1px solid var(--line)}
.cap .k{font:800 15px 'JetBrains Mono',monospace;letter-spacing:.14em;color:#0B1A12;background:var(--acc);padding:7px 12px;border-radius:4px;white-space:nowrap;text-transform:uppercase}
.cap .t{font-size:52px;font-weight:900;letter-spacing:-.025em;color:#fff;line-height:1.05}
.cap .t em{font-style:normal;color:var(--acc)}
.status{display:flex;align-items:center;gap:22px;padding:0 16px;background:#174A33;font:600 13.5px 'JetBrains Mono',monospace;color:#D7EADF}
.status .r{margin-left:auto}
.cta{height:100%%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;text-align:center}
.cta .a{font-size:64px;font-weight:900;color:#fff;letter-spacing:-.02em}
.cta .b{font:800 40px 'JetBrains Mono',monospace;color:#0B1A12;background:var(--acc);padding:16px 30px;border-radius:6px}
#notes{position:fixed;left:0;right:0;bottom:0;max-height:62vh;overflow:auto;background:rgba(8,16,12,.97);border-top:3px solid var(--acc);
 padding:22px 34px;font:500 19px/1.55 'Inter',sans-serif;color:#E8F0EA;display:none;z-index:50}
#notes.on{display:block}
#notes h4{font:700 14px 'JetBrains Mono',monospace;letter-spacing:.14em;color:var(--acc);margin-bottom:8px}
#hint{position:fixed;right:10px;top:8px;font:500 11px 'JetBrains Mono',monospace;color:#3D5A4A;z-index:40}
"""

JS = r"""
const F = FRAMES, META = META_OBJ;
const STATIC = /static=1/.test(location.search);
let i = 0, timers = [];
const $ = s => document.querySelector(s);
function fit(){const s=Math.min(innerWidth/1600, innerHeight*__SAFE_H__/900);$('#stage').style.top=(450*s)+'px';$('#stage').style.transform=`translate(-50%,-50%) scale(${s})`;}
addEventListener('resize', fit);
function clear(){timers.forEach(clearTimeout); timers=[];}
function later(fn, ms){ if(STATIC){fn();return;} timers.push(setTimeout(fn, ms)); }
function tree(f){
  const t = META.trees[f.tree || META.tree0];
  $('#side').innerHTML = `<div class="h">${t.title}</div>` + t.rows.map((r,k)=>{
    const on = (f.on||[]).includes(k) ? ' on' : '';
    return `<div class="r ${r[1]}${on}">${r[0]}</div>`;}).join('');
}
function termHTML(cmds){
  // cmds: [{cmd, out:[html]}]
  return cmds.map((c,ci)=>`<div class="blk" id="b${ci}"><span class="p">${META.prompt}</span> <span class="c" id="c${ci}"></span><span class="cursor" id="k${ci}"></span>\n<div id="o${ci}"></div></div>`).join('');
}
function runTerm(el, cmds){
  el.innerHTML = `<div class="term">${termHTML(cmds)}</div>`;
  let t = 250;
  cmds.forEach((c,ci)=>{
    const ce = el.querySelector('#c'+ci), oe = el.querySelector('#o'+ci), ke = el.querySelector('#k'+ci);
    if(ci>0){ el.querySelector('#b'+ci).style.display = STATIC ? '' : 'none'; later(()=>{el.querySelector('#b'+ci).style.display='';}, t); }
    if(STATIC){ ce.textContent = c.cmd; } else {
      for(let k=1;k<=c.cmd.length;k++){ later(()=>{ce.textContent=c.cmd.slice(0,k);}, t + k*26); }
    }
    t += c.cmd.length*26 + 260;
    later(()=>{ ke.style.display='none'; }, t);
    c.out.forEach((ln,li)=>{ later(()=>{ oe.insertAdjacentHTML('beforeend', ln + '\n'); }, t + li*45); });
    t += c.out.length*45 + 500;
  });
  if(STATIC) el.querySelectorAll('.cursor').forEach(k=>k.style.display='none');
}
function edHTML(f){
  const start = f.start || 1;
  const num = k => f.nums ? f.nums[k] : start+k;
  return `<div class="ed${(f.hl&&f.hl.length)?' focus':''}" id="ed">` + f.lines.map((l,k)=>
    `<div class="ln" data-n="${num(k)}"><b>${num(k)}</b><span>${l || ' '}</span></div>`).join('') + `</div>`;
}
function runEd(el, f){
  el.innerHTML = edHTML(f);
  const ed = el.querySelector('#ed');
  if(ed.classList.contains('focus')){ ed.classList.remove('focus'); later(()=>{
    ed.classList.add('focus');
    ed.querySelectorAll('.ln').forEach(n=>{ if(f.hl.includes(+n.dataset.n)) n.classList.add('hl'); });
  }, 650); }
}
function pane(el, p){
  if(p.kind==='term') runTerm(el, p.cmds);
  else if(p.kind==='file') runEd(el, p);
  else if(p.kind==='chart') el.innerHTML = `<div class="chartwrap">${p.html}</div>`;
  else if(p.kind==='cta') el.innerHTML = `<div class="cta"><div class="a">${p.a}</div><div class="b">${p.b}</div></div>`;
}
function show(n){
  clear(); i = Math.max(0, Math.min(F.length-1, n)); const f = F[i];
  history.replaceState(null, '', '#'+(i+1));
  tree(f);
  $('#tabs').innerHTML = (f.tabs||[]).map((t,k)=>`<div class="tab${k===(f.tabOn||0)?' on':''}">${t}</div>`).join('');
  const c = $('#content');
  c.innerHTML = '';
  if(f.right){
    c.innerHTML = '<div class="split"><div id="L"></div><div id="R"></div></div>';
    pane($('#L'), f.left); pane($('#R'), f.right);
  } else { const d=document.createElement('div'); d.style.height='100%'; c.appendChild(d); pane(d, f.left); }
  if(f.needs && f.needs.length){ c.insertAdjacentHTML('beforeend', '<div class="needs">' + f.needs.map(x=>`<div>[NEEDS: ${x}]</div>`).join('') + '</div>'); }
  $('#capk').textContent = f.sec; $('#capt').innerHTML = f.caption;
  $('#stl').textContent = f.status || ''; $('#str').textContent = `${i+1} / ${F.length}`;
  $('#notes').innerHTML = `<h4>FRAME ${i+1} / ${F.length} · ${f.t} · ${f.sec}</h4>${f.notes}`;
}
addEventListener('keydown', e=>{
  document.getElementById('hint').style.display='none';
  if(['ArrowRight',' ','PageDown'].includes(e.key)){e.preventDefault(); show(i+1);}
  else if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault(); show(i-1);}
  else if(e.key==='n'||e.key==='N'){ $('#notes').classList.toggle('on'); }
  else if(e.key==='f'||e.key==='F'){ document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen(); }
  else if(e.key==='Home'){ show(0); } else if(e.key==='End'){ show(F.length-1); }
});
if(STATIC) document.getElementById('hint').style.display='none';
fit(); show((parseInt(location.hash.slice(1))||1)-1);
"""

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<!-- {comment} -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>
<div id="stage">
  <div class="titlebar"><i></i><i></i><i></i><span>{window}</span></div>
  <div class="mid"><div class="side" id="side"></div><div class="main"><div class="tabs" id="tabs"></div><div class="content" id="content"></div></div></div>
  <div class="cap"><div class="k" id="capk"></div><div class="t" id="capt"></div></div>
  <div class="status"><span>&#9095; main</span><span id="stl"></span><span class="r" id="str"></span></div>
</div>
<div id="notes"></div>
<div id="hint">&larr; &rarr; frames · N notes · F fullscreen</div>
<script>
const FRAMES = {frames};
const META_OBJ = {meta};
{js}
</script>
</body></html>
"""


def page(title, comment, window, frames, meta):
    css = CSS % dict(BG=BG, PANE=PANE, SIDE=SIDE, LINE=LINE, TXT=TXT, MUTED=MUTED, ACC=ACC, GREEN=GREEN, RED=RED)
    return controls.inject(PAGE.format(title=esc(title), comment=comment.replace("--", "-"), css=css, window=esc(window),
                       frames=json.dumps(frames, ensure_ascii=False), meta=json.dumps(meta, ensure_ascii=False), js=JS), NAV_ADAPTER)


# ------------------------------------------------------------------ frame constructors

def term(*cmds):
    """cmds: (command, [output lines with markup])"""
    return {"kind": "term", "cmds": [{"cmd": c, "out": [mark(x) for x in out]} for c, out in cmds]}


def file(lines, hl=(), start=1, nums=None):
    """nums: explicit real line numbers for a non-contiguous excerpt."""
    d = {"kind": "file", "lines": [mark(x) for x in lines], "hl": list(hl), "start": start}
    if nums:
        assert len(nums) == len(lines)
        d["nums"] = list(nums)
    return d


def chart(html_):
    return {"kind": "chart", "html": html_}


def cta(a, b):
    return {"kind": "cta", "a": esc(a), "b": esc(b)}
