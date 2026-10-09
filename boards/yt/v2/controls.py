"""Shared recording control bar for every v2 board format (a-keynote ... f-casefile).

Each generator imports this module and appends `snippet(adapter_js)` just before </body>.
The adapter is a JS object literal that tells the bar how this format moves:

    {count: () => N, index: () => i, go: n => ..., next: () => ..., prev: () => ..., label: k => '...'}

`next` and `prev` are the format's own step functions (A and E step through builds inside a frame),
so the buttons behave exactly like the arrow keys. `go(n)` jumps to frame n (0-based).

What the bar adds:
- prev / next buttons, "N / M" counter, a frame list (click to jump);
- H hides the bar (display:none, so it is not on the recording); the choice is kept per browser;
- the bar is hidden by default in headless Chrome and with ?static, so PNG renders stay clean;
- typing #N in the address bar jumps to frame N (hashchange);
- clicks never move keyboard focus to a control, so arrows and space keep working after a click;
- boards/board-corrections.js (per-frame correction boxes, Copy/Download, D draft layer) rides along,
  reading frames from window.YTNAV.

Facecam safe zones (Mauro 2026-10-09 v6): both bottom corners of every frame stay empty, 22% of the
width x 28% of the height, because the presenter's face goes in one of them. Every format fits its
16:9 #stage into the top SAFE_H band of the window, centered left to right, with the format's own
fit(). The generators write the token __SAFE_H__ and inject() replaces it with SAFE_H. A wider window
keeps the same band. C or F2 shows the facecam box (board-corrections.js); test_controls.py checks
every frame and every build step with safezone.SCAN_JS.
"""
import os

SAFE_H = 0.72  # the stage never goes below 72% of the window height: the bottom 28% band stays free
CSS = r"""
#ytbar{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:2147483000;display:flex;align-items:center;gap:6px;
 background:rgba(17,17,17,.82);color:#fff;border-radius:999px;padding:6px 8px;font:600 13px/1 -apple-system,'Helvetica Neue',Arial,sans-serif;
 box-shadow:0 6px 24px rgba(0,0,0,.25);user-select:none;-webkit-user-select:none}
#ytbar.off{display:none}
#ytbar button{all:unset;cursor:pointer;padding:7px 11px;border-radius:999px;color:#fff;font:inherit}
#ytbar button:hover{background:rgba(255,255,255,.16)}
#ytbar .ct{min-width:64px;text-align:center;font-variant-numeric:tabular-nums}
#ytbar .hk{opacity:.55;font-weight:500;padding:0 6px;font-size:12px}
#ytlist{position:fixed;left:50%;bottom:62px;transform:translateX(-50%);z-index:2147483000;width:min(560px,92vw);max-height:60vh;overflow:auto;
 background:rgba(17,17,17,.94);color:#fff;border-radius:14px;padding:6px;font:500 13px/1.35 -apple-system,'Helvetica Neue',Arial,sans-serif;
 box-shadow:0 10px 30px rgba(0,0,0,.35);display:none}
#ytlist.on{display:block}
#ytlist div{padding:7px 10px;border-radius:8px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ytlist div:hover{background:rgba(255,255,255,.14)}
#ytlist div.cur{background:#F3E3A3;color:#111}
#ytlist b{display:inline-block;min-width:34px;font-variant-numeric:tabular-nums}
"""

JS = r"""
(function(){
const NAV=__ADAPTER__;
window.YTNAV=NAV;  // board-corrections.js reads the frame count, index and labels from here
const strip=s=>String(s==null?'':s).replace(/<[^>]*>/g,'').replace(/&[a-z#0-9]+;/gi,' ').replace(/\s+/g,' ').trim();
const bar=document.createElement('div');bar.id='ytbar';
bar.innerHTML='<button data-a="prev" title="Previous (Left arrow)">&#9664;</button><span class="ct"></span>'+
 '<button data-a="next" title="Next (Right arrow or Space)">&#9654;</button><button data-a="list" title="Frame list">Frames</button>'+
 '<span class="hk">H hide · N notes · F full · C facecam</span>';
const list=document.createElement('div');list.id='ytlist';
document.body.appendChild(list);document.body.appendChild(bar);
const ct=bar.querySelector('.ct');
let hidden=/HeadlessChrome/.test(navigator.userAgent)||/[?&]static/.test(location.search);
try{const v=localStorage.getItem('ytbar');if(v!==null&&!hidden)hidden=v==='off';}catch(e){}
function paint(){bar.classList.toggle('off',hidden);if(hidden)list.classList.remove('on');}
function fill(){const n=NAV.count(),c=NAV.index();let h='';
 for(let k=0;k<n;k++){h+='<div data-k="'+k+'"'+(k===c?' class="cur"':'')+'><b>'+(k+1)+'</b> '+strip(NAV.label(k))+'</div>';}
 list.innerHTML=h;}
let last=-1;
function sync(){const c=NAV.index(),n=NAV.count();if(c===last)return;last=c;ct.textContent=(c+1)+' / '+n;
 if(list.classList.contains('on'))fill();}
setInterval(sync,120);
// Keep focus on the document: a click on the bar never focuses a control.
[bar,list].forEach(el=>{el.addEventListener('mousedown',e=>e.preventDefault());
 el.addEventListener('click',e=>{e.stopPropagation();});});
bar.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const a=b.dataset.a;
 if(a==='prev')NAV.prev();else if(a==='next')NAV.next();
 else if(a==='list'){list.classList.toggle('on');if(list.classList.contains('on')){fill();const cur=list.querySelector('.cur');if(cur)cur.scrollIntoView({block:'center'});}}
 if(document.activeElement&&document.activeElement!==document.body)document.activeElement.blur();sync();});
list.addEventListener('click',e=>{const d=e.target.closest('[data-k]');if(!d)return;NAV.go(+d.dataset.k);list.classList.remove('on');
 if(document.activeElement&&document.activeElement!==document.body)document.activeElement.blur();sync();});
// If anything else took focus (a link, the list), give it back before the format's key handler runs.
addEventListener('keydown',e=>{const a=document.activeElement;
 if(a&&(/^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName)||a.isContentEditable))return;
 if(a&&a!==document.body&&a!==document.documentElement&&!/^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName)&&!a.isContentEditable)a.blur();
 if(e.key==='h'||e.key==='H'){hidden=!hidden;try{localStorage.setItem('ytbar',hidden?'off':'on');}catch(_){}paint();}
 else if(e.key==='Escape'){list.classList.remove('on');}},true);
// #N in the address bar jumps to frame N.
addEventListener('hashchange',()=>{const m=location.hash.match(/\d+/);if(!m)return;const k=parseInt(m[0],10)-1;
 if(k>=0&&k<NAV.count()&&k!==NAV.index())NAV.go(k);});
paint();sync();
})();
"""


CORRECTIONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "board-corrections.js")


def corrections():
    """boards/board-corrections.js inline, between markers (Mauro 2026-10-09: a correction box per frame).
    It goes BEFORE the bar so its capture keydown runs first: typing in a box never moves the board."""
    js = open(CORRECTIONS, encoding="utf-8").read()
    return "<!-- board-corrections:start -->\n<script>\n" + js + "</script>\n<!-- board-corrections:end -->\n"


def snippet(adapter_js):
    """Return the corrections block + the bar's <style> + <script>, to put just before </body>."""
    return corrections() + "<style>" + CSS + "</style>\n<script>" + JS.replace("__ADAPTER__", adapter_js) + "</script>\n"


def inject(page, adapter_js):
    """Insert the control bar into a finished page, just before the last </body>."""
    page = page.replace("__SAFE_H__", repr(SAFE_H))  # before rfind: the token is longer than its value
    k = page.rfind("</body>")
    if k < 0:
        raise SystemExit("controls.inject: no </body> in page")
    return page[:k] + snippet(adapter_js) + page[k:]

