"""Shared engine for the format F case-file boards.

One board element holds every exhibit at native size. A frame is a camera state: the board is
translated and scaled so one exhibit (or the whole board) fills the 16:9 stage. Stamps and strings
accumulate frame by frame, so going back removes them again.

Keys: right / left / space move, N toggles presenter notes, F fullscreen. #n in the URL opens frame n.
"""
import html
import json
import random
import re
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import controls  # noqa: E402  (shared recording control bar, boards/yt/v2/controls.py)

NAV_ADAPTER = "{count:()=>FR.length,index:()=>cur,go:n=>go(n),next:()=>go(cur+1),prev:()=>go(cur-1),label:k=>FR[k].t+' · '+(FR[k].cap||'')}"

COL_W, GAP, MARGIN, NCOLS = 560, 54, 90, 9
BOARD_W = MARGIN * 2 + NCOLS * COL_W + (NCOLS - 1) * GAP

FONTS = ("https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900"
         "&family=JetBrains+Mono:wght@500;700;800&family=Special+Elite&family=Caveat:wght@600;700&display=swap")

CSS = r"""
:root{--ink:#1B4332;--honey:#E9B949;--paper:#F7F3EA;--red:#C62828;--measured:#1F6B45;--observed:#A8650F;--assumed:#3E4F86}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#0b0f0d;overflow:hidden}
body{font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;color:#1B1B1B}
.mono{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace}
#stage{position:absolute;overflow:hidden;
 background:radial-gradient(rgba(255,255,255,.035) 1px,transparent 1.6px) 0 0/9px 9px,
 radial-gradient(rgba(0,0,0,.28) 1px,transparent 1.6px) 4px 5px/13px 13px,
 radial-gradient(ellipse at 50% 40%,#2c3832 0%,#1a221e 60%,#111613 100%)}
#board{position:absolute;left:0;top:0;transform-origin:0 0;transition:transform 1.15s cubic-bezier(.65,.02,.25,1)}
#board.instant,#board.instant *{transition:none!important}
.ex.hs{padding-bottom:96px}.ex{position:absolute;transform:rotate(var(--r));box-shadow:0 16px 34px rgba(0,0,0,.5),0 2px 4px rgba(0,0,0,.4)}
.pin{position:absolute;top:-16px;left:calc(50% - 15px);width:30px;height:30px;border-radius:50%;z-index:5;
 background:radial-gradient(circle at 35% 32%,#fff6d6 0 12%,#E9B949 30%,#9a7418 100%);box-shadow:0 5px 7px rgba(0,0,0,.55)}
/* exhibit kinds */
.paper{background:var(--paper);padding:34px 38px 30px}
.card{background:repeating-linear-gradient(#fffef9 0 45px,#cfdfe8 45px 47px);border-top:10px solid #d9534f;padding:26px 36px 30px}
.folder{background:#E2C88E;padding:44px 44px 40px;border-radius:0 10px 6px 6px}
.folder:before{content:attr(data-tab);position:absolute;top:-46px;left:0;background:#E2C88E;padding:10px 26px 8px;border-radius:10px 10px 0 0;
 font:700 22px 'JetBrains Mono',monospace;letter-spacing:.12em;color:var(--ink)}
.term{background:#0f2219;color:#E6F0E9;padding:0 0 26px;font-family:'JetBrains Mono',monospace}
.term .bar{height:40px;background:#1d3a2b;display:flex;align-items:center;gap:9px;padding:0 16px;margin-bottom:22px}
.term .bar i{width:13px;height:13px;border-radius:50%;background:#4f6e5d;display:block}
.term .bar span{margin-left:12px;font-size:16px;color:#a9c4b3}
.term pre{font:500 21px/1.5 'JetBrains Mono',monospace;padding:0 28px;white-space:pre}
.term pre b{color:var(--honey);font-weight:700}.term pre em{font-style:normal;color:#8fae9b}
.term pre u{text-decoration:none;color:#ff8a80;font-weight:700}
/* type inside exhibits */
.id{font:700 16px 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#6b6250;margin-bottom:14px}
.term .id{color:#8fae9b;padding:0 28px}
.h{font:900 44px/1.05 'Inter';letter-spacing:-.02em;color:var(--ink)}
.h.xl{font-size:150px;letter-spacing:-.04em;line-height:.95}
.h.l{font-size:60px}
.hand{font:700 46px/1.0 'Caveat',cursive;color:#1d2a52}
.hand.l{font-size:60px}
.big{font:900 150px/.9 'Inter';letter-spacing:-.05em;color:var(--ink)}
.big.m{font-size:104px}
.lab{font:600 25px/1.3 'Inter';color:#2f3a33;margin-top:10px}
.src{margin-top:22px;padding-top:12px;border-top:2px dashed #bcae8f;font:700 15px 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:#7a6e55}
.card .src{border-color:#9fb6c4;color:#5d7383}
.term .src{margin:22px 28px 0;border-color:#355a45;color:#8fae9b}
.row{display:flex;gap:20px;align-items:baseline}
.stat{display:grid;grid-template-columns:auto 1fr;gap:6px 22px;align-items:baseline;margin-top:8px}
.stat b{font:900 64px/1 'Inter';color:var(--ink);letter-spacing:-.03em;text-align:right}
.stat span{font:600 25px 'Inter';color:#2f3a33}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.chip{border:3px solid var(--ink);padding:6px 14px;font:700 21px 'JetBrains Mono',monospace;color:var(--ink);background:#fff}
.chip.on{background:var(--honey)}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:14px;border:3px solid var(--ink)}
.ba>div{padding:20px 22px;min-height:150px}
.ba>div:first-child{background:#e9e2d3;border-right:3px solid var(--ink)}
.ba>div:last-child{background:#fff}
.ba .k{font:800 16px 'JetBrains Mono',monospace;letter-spacing:.16em;color:#6b6250;margin-bottom:10px}
.ba>div:last-child .k{color:var(--measured)}
.ba .v{font:800 30px/1.2 'Inter';color:var(--ink)}
.ba>div:first-child .v{text-decoration:line-through;text-decoration-color:rgba(198,40,40,.7);text-decoration-thickness:4px}
table.t{width:100%;border-collapse:collapse;margin-top:10px}
table.t td{padding:11px 10px;border-bottom:2px solid #d8cfbb;font:600 24px 'Inter';vertical-align:top}
table.t td:first-child{font:800 22px 'JetBrains Mono',monospace;color:var(--ink);white-space:nowrap}
table.t tr.hot td{background:#fbeec6}
.list{margin-top:8px}.list div{font:700 30px/1.25 'Inter';color:var(--ink);padding:9px 0;border-bottom:2px solid #d8cfbb;display:flex;gap:18px}
.list div span{font:800 24px 'JetBrains Mono',monospace;background:var(--honey);padding:2px 10px;height:fit-content}
.needs{display:inline-block;background:var(--red);color:#fff;font:800 19px/1.3 'JetBrains Mono',monospace;padding:4px 10px;border-radius:3px;letter-spacing:.02em}
.needs.blk{display:block;margin-top:14px}
svg text{font-family:'Inter',sans-serif}
/* stamps */
.stamp{position:absolute;bottom:14px;right:20px;z-index:6;transform:rotate(-9deg) scale(2.6);opacity:0;
 transition:transform .38s cubic-bezier(.3,1.6,.5,1),opacity .2s;border:5px double currentColor;padding:6px 14px 4px;text-align:center;
 font:400 34px/1 'Special Elite',monospace;letter-spacing:.06em;background:rgba(247,243,234,.88);border-radius:4px}
.stamp small{display:block;font:700 13px 'JetBrains Mono',monospace;letter-spacing:.1em;margin-top:5px}
.stamp.measured{color:var(--measured)}.stamp.observed{color:var(--observed)}.stamp.assumed{color:var(--assumed)}.stamp.none{color:var(--red)}
.ex.stamped .stamp{opacity:.95;transform:rotate(-9deg) scale(1)}
/* strings */
#strings{position:absolute;left:0;top:0;pointer-events:none;z-index:50;overflow:visible}
#strings path{fill:none;stroke:#d8a531;stroke-width:4;filter:drop-shadow(0 3px 2px rgba(0,0,0,.5));transition:stroke-dashoffset 1.2s ease .35s}
/* caption tape, outside the exhibits (max 8 words) */
#cap{position:absolute;left:50%;bottom:4.2%;transform:translateX(-50%) rotate(-.6deg);background:#f2efe6;color:#111;
 font-weight:900;letter-spacing:-.01em;padding:.35em .8em;box-shadow:0 8px 20px rgba(0,0,0,.5);white-space:nowrap;z-index:60}
#cap:empty{opacity:0}
/* presenter notes (N) */
#notes{position:absolute;top:0;right:0;bottom:0;width:36%;background:rgba(8,12,10,.94);color:#e8eee9;padding:28px 30px;overflow:auto;
 font:500 19px/1.5 'Inter';display:none;z-index:90;border-left:4px solid var(--honey)}
#notes.on{display:block}
#notes .t{font:800 15px 'JetBrains Mono',monospace;color:var(--honey);letter-spacing:.12em;margin-bottom:14px}
#notes p{margin-bottom:12px}
#notes .needs{font-size:14px}
"""

JS = r"""
const W0=__BW__;
const board=document.getElementById('board'),stage=document.getElementById('stage');
const cap=document.getElementById('cap'),notes=document.getElementById('notes');
const svg=document.getElementById('strings');
let cur=0,SW=0,SH=0;
function layout(){
  const cols=new Array(__NC__).fill(__M__+40);
  EX.forEach(e=>{
    const el=document.getElementById(e.id);
    el.style.width=(e.span*__CW__+(e.span-1)*__G__)+'px';
    let y;
    if(e.clear==='same'){y=window.LASTY;}else if(e.clear){y=Math.max(...cols);window.LASTY=y;}else{y=Math.max(...cols.slice(e.col,e.col+e.span));}
    y+=(e.dy||0);
    const x=__M__+e.col*(__CW__+__G__);
    el.style.left=x+'px';el.style.top=y+'px';
    const h=el.offsetHeight;
    if(e.clear){for(let i=0;i<cols.length;i++)cols[i]=y+h+__G__+30;}
    else for(let i=e.col;i<e.col+e.span;i++)cols[i]=y+h+__G__+30;
  });
  const H=Math.max(...cols)+40;
  board.style.width=W0+'px';board.style.height=H+'px';
  svg.setAttribute('width',W0);svg.setAttribute('height',H);
  window.BH=H;
  // strings, pin to pin
  STR.forEach(s=>{
    const a=document.getElementById(s[1]),b=document.getElementById(s[2]);
    const ax=a.offsetLeft+a.offsetWidth/2,ay=a.offsetTop,bx=b.offsetLeft+b.offsetWidth/2,by=b.offsetTop;
    const mx=(ax+bx)/2,my=(ay+by)/2+Math.min(160,Math.hypot(bx-ax,by-ay)*.12);
    let p=document.getElementById('s_'+s[0]);
    if(!p){p=document.createElementNS('http://www.w3.org/2000/svg','path');p.id='s_'+s[0];svg.appendChild(p);}
    p.setAttribute('d',`M${ax} ${ay} Q${mx} ${my} ${bx} ${by}`);
    const L=p.getTotalLength();p.style.strokeDasharray=L;p.dataset.len=L;
  });
}
function fit(){
  const vw=innerWidth,vh=innerHeight;
  SW=Math.min(vw,vh*__SAFE_H__*16/9);SH=SW*9/16;
  stage.style.width=SW+'px';stage.style.height=SH+'px';
  stage.style.left=(vw-SW)/2+'px';stage.style.top='0px';
  cap.style.fontSize=(SW*0.026)+'px';
}
function rectOf(ids){
  if(ids==='all')return{x:0,y:0,w:W0,h:window.BH,pad:0};
  let x1=1e9,y1=1e9,x2=-1e9,y2=-1e9;
  ids.forEach(id=>{const el=document.getElementById(id);x1=Math.min(x1,el.offsetLeft);y1=Math.min(y1,el.offsetTop-20);
    x2=Math.max(x2,el.offsetLeft+el.offsetWidth);y2=Math.max(y2,el.offsetTop+el.offsetHeight);});
  return{x:x1,y:y1,w:x2-x1,h:y2-y1,pad:70};
}
function go(i,instant){
  cur=Math.max(0,Math.min(FR.length-1,i));
  const f=FR[cur];
  const r=rectOf(f.focus);
  const capH=f.cap?SH*0.12:0;
  const availH=SH-capH*(r.pad?1:0);
  let s=Math.min(SW/(r.w+2*r.pad*(SW/1600)),availH/(r.h+2*r.pad*(SH/900)));
  if(f.focus!=='all')s=Math.min(s,SW/1600*1.55);
  const tx=SW/2-s*(r.x+r.w/2),ty=availH/2-s*(r.y+r.h/2);
  if(instant)board.classList.add('instant');
  board.style.transform=`translate(${tx}px,${ty}px) scale(${s})`;
  const st=new Set(),sg=new Set();
  for(let k=0;k<=cur;k++){(FR[k].stamp||[]).forEach(x=>st.add(x));(FR[k].string||[]).forEach(x=>sg.add(x));}
  EX.forEach(e=>document.getElementById(e.id).classList.toggle('stamped',st.has(e.id)));
  STR.forEach(s=>{const p=document.getElementById('s_'+s[0]);p.style.strokeDashoffset=sg.has(s[0])?0:p.dataset.len;});
  cap.textContent=f.cap||'';
  notes.innerHTML=`<div class="t">FRAME ${cur+1} / ${FR.length} · ${f.t} · ${f.d}s</div>`+f.say.map(p=>`<p>${p}</p>`).join('');
  history.replaceState(null,'','#'+(cur+1));
  if(instant){board.offsetHeight;requestAnimationFrame(()=>board.classList.remove('instant'));}
}
addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();go(cur+1);}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(cur-1);}
  else if(e.key==='n'||e.key==='N'){notes.classList.toggle('on');}
  else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
  else if(e.key==='Home'){go(0);}
});
addEventListener('resize',()=>{fit();go(cur,true);});
function start(){fit();layout();const h=parseInt(location.hash.slice(1));go(isNaN(h)?0:h-1,true);}
(document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(start);
"""

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="{fonts}" rel="stylesheet">
<!-- {comment} -->
<style>{css}</style></head>
<body>
<div id="stage"><div id="board">{exhibits}<svg id="strings"></svg></div><div id="cap"></div><div id="notes"></div></div>
<script>
const EX={ex};
const STR={strs};
const FR={frames};
{js}
</script>
</body></html>
"""

STAMP_TXT = {"measured": "MEASURED", "observed": "OBSERVED", "assumed": "ASSUMED", "none": "MEASURED: NONE"}


def needs(x, blk=False):
    return f'<span class="needs{" blk" if blk else ""}">[NEEDS: {html.escape(x)}]</span>'


def words(s):
    return len(re.findall(r"[A-Za-z0-9$%+.,'’:-]+", s or ""))


def build(title, comment, exhibits, strings, frames, seed=7):
    rnd = random.Random(seed)
    ex_html, ex_meta = [], []
    for e in exhibits:
        r = e.get("rot", round(rnd.uniform(-1.6, 1.6), 2))
        stamp = ""
        if e.get("stamp"):
            kind, sub = e["stamp"]
            stamp = f'<div class="stamp {kind}">{STAMP_TXT[kind]}' + (f"<small>{sub}</small>" if sub else "") + "</div>"
        src = f'<div class="src">{e["src"]}</div>' if e.get("src") else ""
        tab = f' data-tab="{e["tab"]}"' if e.get("tab") else ""
        hs = " hs" if e.get("stamp") else ""
        ex_html.append(f'<div class="ex {e["kind"]}{hs}" id="{e["id"]}" style="--r:{r}deg"{tab}><div class="pin"></div>{stamp}{e["html"]}{src}</div>')
        ex_meta.append({"id": e["id"], "col": e["col"], "span": e["span"], "clear": e.get("clear", False), "dy": e.get("dy", 0)})
    ids = {e["id"] for e in exhibits}
    t = 0
    for i, f in enumerate(frames):
        assert words(f.get("cap", "")) <= 8, f"frame {i+1} caption over 8 words: {f['cap']}"
        assert "—" not in json.dumps(f) and "–" not in json.dumps(f), f"dash in frame {i+1}"
        for k in f.get("stamp", []):
            assert k in ids, k
        if f["focus"] != "all":
            for k in f["focus"]:
                assert k in ids, k
        f["t"] = f"{t // 60}:{t % 60:02d}"
        t += f["d"]
    for s in strings:
        assert s[1] in ids and s[2] in ids, s
    js = (JS.replace("__BW__", str(BOARD_W)).replace("__NC__", str(NCOLS)).replace("__M__", str(MARGIN))
          .replace("__CW__", str(COL_W)).replace("__G__", str(GAP)))
    page = PAGE.format(title=html.escape(title), fonts=FONTS, comment=comment, css=CSS, exhibits="\n".join(ex_html),
                       ex=json.dumps(ex_meta), strs=json.dumps(strings), frames=json.dumps(frames, ensure_ascii=False), js=js)
    assert "—" not in page, "em dash in page"
    page = controls.inject(page, NAV_ADAPTER)
    return page, t


def notes_md(title, slug, frames, total, extra):
    out = [f"# {title}: presenter notes", "",
           f"Board: `{slug}.html`. Press N on the board to see these lines over the frame. "
           f"Planned length: {total // 60} min {total % 60:02d} s across {len(frames)} frames.", ""]
    for i, f in enumerate(frames):
        foc = "whole board" if f["focus"] == "all" else ", ".join(f["focus"])
        out.append(f"## Frame {i+1} · {f['t']} · {f['d']}s")
        out.append(f"On screen: {foc}" + (f". Caption: \"{f['cap']}\"" if f.get("cap") else ". No caption."))
        out.append("")
        for p in f["say"]:
            out.append(re.sub(r"<[^>]+>", "", p))
            out.append("")
    out += extra
    return "\n".join(out) + "\n"
