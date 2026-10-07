#!/usr/bin/env python3
"""Build the format E "doodle whiteboard" boards for docs 11, 10 and 03.

    python3 boards/yt/v2/e-whiteboard/build.py          # html + notes + meta
    python3 boards/yt/v2/e-whiteboard/build.py --png    # also the cover and thumbs PNGs

Each board is one self-contained HTML file. Keys: right arrow or space draws the next step,
left goes back a frame, N shows the presenter notes, F goes fullscreen. Add ?static to the URL
to see every frame fully drawn (the PNG render uses ?static&f=1).
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402
import importlib  # noqa: E402
import thumbs  # noqa: E402

FONTS = ("https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Kalam:wght@400;700"
         "&family=JetBrains+Mono:wght@500;700&display=swap")

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#E9E4D8;overflow:hidden}
#stage{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);aspect-ratio:16/9;
 width:min(100vw,calc(100vh*16/9));background:#FBF8F1}
.f{position:absolute;inset:0;visibility:hidden}
.f.cur{visibility:visible}
.f svg{width:100%;height:100%;display:block}
g[data-s]{opacity:0}
g[data-s].on{opacity:1}
g.on path.ink{stroke-dasharray:var(--L);stroke-dashoffset:var(--L);animation:draw var(--d,.7s) ease-out forwards;animation-delay:var(--dl,0s)}
g.on .hl{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);animation:swipe .45s ease-out forwards}
g.on text,g.on image,g.on .needs{opacity:0;animation:fade .45s ease-out forwards;animation-delay:.15s}
g.done path.ink,g.done .hl,g.done text,g.done image,g.done .needs{animation:none!important;stroke-dasharray:none;opacity:1;transform:none}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes swipe{to{transform:scaleX(1)}}
@keyframes fade{to{opacity:1}}
#notes{position:fixed;left:0;right:0;bottom:0;max-height:46vh;overflow:auto;background:rgba(20,20,20,.94);color:#F2EEE4;
 font:18px/1.5 -apple-system,'Helvetica Neue',Arial,sans-serif;padding:18px 28px 22px;display:none;z-index:9}
#notes.show{display:block}
#notes b{font:700 13px 'JetBrains Mono',monospace;letter-spacing:.12em;color:#F3E3A3;display:block;margin-bottom:8px}
"""

JS = r"""
const frames=[...document.querySelectorAll('.f')];
const NOTES=JSON.parse(document.getElementById('nd').textContent);
const P=new URLSearchParams(location.search);
const STATIC=P.has('static');
let nofx=false;
let fi=Math.max(0,Math.min(frames.length-1,(parseInt(P.get('f'))||1)-1)), st=0;
function maxs(f){return Math.max(0,...[...f.querySelectorAll('g[data-s]')].map(g=>+g.dataset.s))}
function prep(){
 frames.forEach(f=>f.querySelectorAll('g[data-s]').forEach(g=>{
  g.querySelectorAll('path.ink').forEach((p,i)=>{const L=Math.ceil(p.getTotalLength())+2;
   p.style.setProperty('--L',L);p.style.setProperty('--d',Math.min(1.1,.25+L/1400)+'s');
   p.style.setProperty('--dl',Math.min(1.4,i*.05)+'s');});
 }));
 document.querySelectorAll('text[data-maxw]').forEach(t=>{const m=+t.dataset.maxw,L=t.getComputedTextLength();
  if(L>m){t.setAttribute('font-size',(parseFloat(t.getAttribute('font-size'))*m/L).toFixed(1))}});
 document.querySelectorAll('text[data-hl]').forEach(t=>{const [a,n]=t.dataset.hl.split(',').map(Number);
  const x0=t.getStartPositionOfChar(a).x, w=t.getSubStringLength(a,n), bb=t.getBBox();
  const r=document.createElementNS('http://www.w3.org/2000/svg','polygon');
  const y=bb.y+bb.height*.42,h=bb.height*.5;
  r.setAttribute('points',`${x0-10},${y+3} ${x0+w+12},${y-2} ${x0+w+8},${y+h} ${x0-6},${y+h+3}`);
  r.setAttribute('fill','#F3E3A3');r.setAttribute('class','hl');t.parentNode.insertBefore(r,t);});
}
function show(){
 frames.forEach((f,i)=>f.classList.toggle('cur',i===fi));
 const f=frames[fi];
 f.querySelectorAll('g[data-s]').forEach(g=>{const s=+g.dataset.s;
  g.classList.toggle('on',s<=st);
  if(STATIC||nofx||s<st){g.classList.add('done')} else if(s===st){g.classList.remove('done')}
  if(s>st)g.classList.remove('done');});
 const n=NOTES[fi];document.getElementById('notes').innerHTML='<b>FRAME '+(fi+1)+' / '+frames.length+' · '+n.t+'</b>'+n.h;
}
function next(){nofx=false;if(st<maxs(frames[fi])){st++;show()}else if(fi<frames.length-1){fi++;st=0;show()}}
function prev(){if(fi>0){fi--;st=maxs(frames[fi]);nofx=true;show()}}
addEventListener('keydown',e=>{
 if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();next()}
 else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();prev()}
 else if(e.key==='n'||e.key==='N'){document.getElementById('notes').classList.toggle('show')}
 else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
});
document.getElementById('stage').addEventListener('click',next);
(document.fonts?document.fonts.ready:Promise.resolve()).then(()=>{prep();if(STATIC)st=maxs(frames[fi]);show()});
"""

PAPER_DEFS = ('<defs><pattern id="dots" width="40" height="40" patternUnits="userSpaceOnUse">'
              '<circle cx="2" cy="2" r="1.6" fill="#1E1E1E" opacity=".07"/></pattern></defs>'
              '<rect width="1600" height="900" fill="#FBF8F1"/><rect width="1600" height="900" fill="url(#dots)"/>')


def head_svg(fr):
    t = fr.head
    hl = ""
    if fr.hl:
        a = t.find(fr.hl)
        assert a >= 0, (t, fr.hl)
        hl = ' data-hl="%d,%d"' % (a, len(fr.hl))
    o = ('<g data-s="0"><text x="96" y="132" font-size="86" data-maxw="%d"%s style="font-family:\'Caveat\',cursive;'
         'font-weight:700" fill="#1E1E1E">%s</text></g>' % (1240 if fr.sec else 1400, hl, lib.esc(t)))
    if fr.sec:
        o += ('<g data-s="0"><circle cx="1500" cy="98" r="40" fill="none" stroke="#1E1E1E" stroke-width="4"/>'
              '<text x="1500" y="116" font-size="50" text-anchor="middle" style="font-family:\'Kalam\',cursive;font-weight:700">%d</text></g>' % fr.sec)
    return o


def frame_svg(fr):
    groups = {}
    for s, svg in fr.parts:
        groups.setdefault(s, []).append(svg)
    body = "".join('<g data-s="%d">%s</g>' % (s, "".join(v)) for s, v in sorted(groups.items()))
    return ('<div class="f"><svg viewBox="0 0 1600 900" xmlns="http://www.w3.org/2000/svg">%s%s%s</svg></div>'
            % (PAPER_DEFS, head_svg(fr), body))


def mmss(sec):
    return "%d:%02d" % (sec // 60, sec % 60)


def check(slug, frames, titles):
    errs = []
    for i, fr in enumerate(frames, 1):
        n = len(re.findall(r"[\w$%+\-']+", fr.head))
        n += sum(len(t.split()) for k, t in fr.words if k == "a")
        if n > 8:
            errs.append("F%d headline has %d words: %s" % (i, n, fr.head))
        for kind, t in fr.words:
            w = len(t.split())
            if (kind in "la" and w > 3) or (kind == "c" and w > 6):
                errs.append("F%d label too long (%s): %s" % (i, kind, t))
        blob = fr.head + fr.notes + "".join(v for _, v in fr.parts)
        if lib.BANNED.search(blob):
            errs.append("F%d banned string: %s" % (i, lib.BANNED.search(blob).group(0)))
    for t in titles:
        if lib.BANNED.search(t["title"] + t["modelled_on"]):
            errs.append("title banned string: " + t["title"])
    total = sum(f.secs for f in frames)
    if not (20 * 60 <= total <= 25 * 60):
        errs.append("runtime %s outside 20-25 min" % mmss(total))
    if not (22 <= len(frames) <= 30):
        errs.append("%d frames, brief wants 22-30" % len(frames))
    if errs:
        print("\n".join("[%s] %s" % (slug, e) for e in errs))
        sys.exit(1)


def build(slug, title, frames, titles):
    check(slug, frames, titles)
    notes_js, md, t = [], ["# %s: presenter notes\n" % title,
                           "Hidden on the board. Press `N` on the board to see the same lines in an overlay.\n"], 0
    for i, fr in enumerate(frames, 1):
        span = "%s-%s" % (mmss(t), mmss(t + fr.secs))
        notes_js.append({"t": span, "h": "<br><br>".join(lib.esc(p) for p in fr.notes.split("\n\n"))})
        md.append("## F%02d · %s · %s\n\n%s\n" % (i, span, fr.head, fr.notes))
        if fr.needs:
            md.append("On screen: " + ", ".join("`[NEEDS: %s]`" % n for n in fr.needs) + "\n")
        t += fr.secs
    md.append("**Runtime: %s across %d frames.**\n" % (mmss(t), len(frames)))
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title>'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="%s" rel="stylesheet">'
            '<style>%s</style></head><body><div id="stage">%s</div><div id="notes"></div>'
            '<script id="nd" type="application/json">%s</script><script>%s</script></body></html>'
            % (lib.esc(title), FONTS, CSS, "".join(frame_svg(f) for f in frames),
               json.dumps(notes_js).replace("</", "<\\/"), JS))
    assert "—" not in page
    with open(os.path.join(HERE, slug + ".html"), "w") as fh:
        fh.write(page)
    with open(os.path.join(HERE, slug + ".notes.md"), "w") as fh:
        fh.write("\n".join(md))
    needs = []
    for f in frames:
        for n in f.needs:
            if n not in needs:
                needs.append(n)
    return {"doc": slug[:2], "file": slug + ".html", "titles": titles, "frames": len(frames),
            "minutes": round(t / 60), "needs": needs}


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def shot(src, png, w, h):
    subprocess.run([CHROME, "--headless", "--user-data-dir=/tmp/ewb-" + os.path.basename(png), "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000",
                    "--screenshot=" + png, "--window-size=%d,%d" % (w, h), src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)


def main():
    meta = []
    only = [a for a in sys.argv[1:] if not a.startswith('--')]
    for name in (only or ['v11', 'v10', 'v03']):
        mod = importlib.import_module(name)
        frames = mod.frames()
        meta.append(build(mod.SLUG, mod.TITLE, frames, mod.TITLES))
        if getattr(mod, "THUMBS", None):
            n = thumbs.write(mod.SLUG, mod.THUMBS)
            if "--png" in sys.argv:
                shot("file://" + os.path.join(HERE, mod.SLUG + ".thumbs.html"),
                     os.path.join(HERE, mod.SLUG + ".thumbs.png"), 1280, 720 * n + 30 * (n + 1))
        if "--png" in sys.argv:
            shot("file://" + os.path.join(HERE, mod.SLUG + ".html") + "?static&f=1",
                 os.path.join(HERE, mod.SLUG + ".cover.png"), 1600, 900)
    if only:
        meta_path = os.path.join(HERE, "meta.json")
        old = json.load(open(meta_path)) if os.path.exists(meta_path) else []
        keep = [m for m in old if m["doc"] not in {x["doc"] for x in meta}]
        meta = sorted(keep + meta, key=lambda m: -int(m["doc"]))
    with open(os.path.join(HERE, "meta.json"), "w") as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
    for m in meta:
        print("%s  %d frames  %d min  needs=%s" % (m["file"], m["frames"], m["minutes"], m["needs"]))


if __name__ == "__main__":
    main()
