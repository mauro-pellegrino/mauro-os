#!/usr/bin/env python3
"""Animate a static ASCII diagram (.txt) into an MP4 where the diagram draws itself.

Lines type in, box borders sweep in row by row, arrowheads land in the accent colour,
then small packets flow along every connector that ends in an arrow, and one target pulses.
--loop makes the video loop seamlessly in X autoplay or an HTML <video loop>: every motion runs on one
shared period, and the last frame leads straight back into the first.
House look: the same terminal window as content/ascii/render.py (dark or cream).

Usage:
  python3 tools/ascii-anim/ascii_anim.py content/ascii/<name>.txt
      [--theme dark|cream] [--size 1080x1080|1600x900|both] [--highlight "TEXT"]
      [--handle @maurojpelle] [--reveal 9] [--hold 5] [--fps 30] [--out DIR] [--gif]
      [--loop [draw|steady]]

Writes <out>/<name>-<theme>-<W>x<H>.mp4 (H.264, yuv420p, faststart; X-ready).
--loop draw   (default for --loop) draw in, flow + pulse for whole periods, fade back to the empty
              window, so the end meets frame 0. Writes ...-loop.mp4
--loop steady the diagram is already drawn, only the flow + pulse run, exactly whole periods.
              For <video autoplay loop muted> inside HTML boards and articles. Writes ...-steady.mp4
Needs: Google Chrome, python3 playwright (no browser download needed), ffmpeg.
"""
import argparse, html, json, pathlib, subprocess, sys, tempfile
from collections import deque

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
THEMES = {  # copied from content/ascii/render.py so stills and videos match
    "cream": dict(page="#EFE8D8", win="#FAF6EC", edge="#D9D2C0", bar="#F1EBDD", title="#8A8578", ink="#1A1A1A",
                  foot="#8A8578", accent="#BD0A0A", glow="189,10,10", shadow="rgba(60,50,30,.18)"),
    "dark": dict(page="#0E1116", win="#1B1F27", edge="#2E3440", bar="#232833", title="#7C8595", ink="#D7DCE4",
                 foot="#7C8595", accent="#E8B86A", glow="232,184,106", shadow="rgba(0,0,0,.55)"),
}
ARROWS = set("▼▲►◄→←↓↑▶◀▸◂")
UNI_BOX = lambda ch: "─" <= ch <= "╿"
H_SET = set("─═━-=┬┴┼╤╧╪+")
V_SET = set("│║┃|├┤┼╟╢╫+")
VCAP = set("│║┃|┬┴┼├┤┌┐└┘╔╗╚╝╭╮╰╯╤╧╪╟╢╫+v^▼▲↓↑")
HCAP = set("─═━-=┬┴┼├┤┌┐└┘╔╗╚╝╭╮╰╯╤╧╪╟╢╫+<>►◄→←▶◀▸◂")
TL, TR, BL, BR = set("┌╔╭+"), set("┐╗╮+"), set("└╚╰+"), set("┘╝╯+")


def parse(text):
    lines = text.rstrip("\n").split("\n")
    cols = max(len(l) for l in lines)
    g = [list(l.ljust(cols)) for l in lines]
    return g, len(g), cols


def classify(g, R, C):
    """kind per cell: ' ' blank, 's' structure (lines, borders), 'a' arrowhead, 't' text."""
    at = lambda r, c: g[r][c] if 0 <= r < R and 0 <= c < C else " "
    k = [[" "] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            ch = g[r][c]
            if ch == " ":
                continue
            L, Rt, U, D = at(r, c - 1), at(r, c + 1), at(r - 1, c), at(r + 1, c)
            if ch in ARROWS:
                k[r][c] = "a"
            elif UNI_BOX(ch):
                k[r][c] = "s"
            elif ch in "-=":
                k[r][c] = "s" if (L in "-=+<>" or Rt in "-=+<>") else "t"
            elif ch == "|":
                k[r][c] = "t" if (L.isalnum() and Rt.isalnum()) else "s"
            elif ch == "+":
                k[r][c] = "s" if (L in "-=" or Rt in "-=" or U == "|" or D == "|") else "t"
            elif ch == ">" and L in "-=─":
                k[r][c] = "a"
            elif ch == "<" and Rt in "-=─":
                k[r][c] = "a"
            elif ch in "v^" and L == " " and Rt == " " and (U in "|│" or D in "|│"):
                k[r][c] = "a"
            else:
                k[r][c] = "t"
    return k


def find_boxes(g, R, C):
    """Rectangles drawn with box chars or +---+ / +===+. Tolerates a ragged bottom edge."""
    at = lambda r, c: g[r][c] if 0 <= r < R and 0 <= c < C else " "
    boxes = []
    for r in range(R):
        for c in range(C):
            if g[r][c] not in TL:
                continue
            c2 = c + 1
            while c2 < C and g[r][c2] in H_SET - TR or (c2 < C and g[r][c2] == "+" and at(r + 1, c2) not in V_SET):
                c2 += 1
            if c2 >= C or g[r][c2] not in TR or c2 - c < 3:
                continue
            r2 = r + 1
            while r2 < R and (g[r2][c] in (V_SET - {"+"}) | {"├", "╟"} or (g[r2][c] == "+" and at(r2 + 1, c) == "|")):
                r2 += 1
            if r2 >= R or g[r2][c] not in BL or r2 - r < 2:
                continue
            cb = c + 1
            while cb < C and g[r2][cb] in H_SET - BR:
                cb += 1
            if cb >= C or g[r2][cb] not in BR:
                continue
            boxes.append((r, c, r2, max(c2, cb)))
    # drop boxes nested as the outer frame of a whole card? keep all; mark border cells
    return boxes


def timeline(g, k, R, C, reveal, start=0.35):
    """Appear time per cell. Rows go top to bottom; structure sweeps left to right; text types."""
    n_text = sum(1 for r in range(R) for c in range(C) if k[r][c] == "t")
    n_rows = sum(1 for r in range(R) if any(x != " " for x in k[r]))
    row_gap = 0.05
    dt = max(0.004, min(0.03, (reveal - start - n_rows * (row_gap + 0.12)) / max(n_text, 1)))
    sweep = min(0.006, 0.35 / max(C, 1))
    t0 = [[None] * C for _ in range(R)]
    T = start
    for r in range(R):
        if all(x == " " for x in k[r]):
            T += 0.03
            continue
        typed = T
        for c in range(C):
            kind = k[r][c]
            if kind in "sa":
                t0[r][c] = T + c * sweep
            elif kind == "t":
                t0[r][c] = typed
                typed += dt
            # spaces inside text runs cost a tick too, so words breathe
            elif c > 0 and k[r][c - 1] == "t":
                typed += dt * 0.6
        T = max(T + C * sweep * 0.5, typed) + row_gap
    return t0, T


def flows(g, k, R, C, boxes, t0):
    """Connector components (structure outside boxes + arrows) that contain an arrowhead.
    Returns per-cell (component id, distance from the component's top row)."""
    border = set()
    for (r1, c1, r2, c2) in boxes:
        for c in range(c1, c2 + 1):
            border.add((r1, c)); border.add((r2, c))
        for r in range(r1, r2 + 1):
            border.add((r, c1)); border.add((r, c2))
    def linked(a, b):  # a vertical step needs two vertical-capable chars, a horizontal step two horizontal ones
        ca, cb = g[a[0]][a[1]], g[b[0]][b[1]]
        pool = VCAP if a[1] == b[1] else HCAP
        return ca in pool and cb in pool
    conn = {(r, c) for r in range(R) for c in range(C) if k[r][c] in "sa" and (r, c) not in border}
    seen, out, comp_len, cid = set(), {}, [], 0
    for cell in sorted(conn):
        if cell in seen:
            continue
        comp, q = [], deque([cell]); seen.add(cell)
        while q:
            cur = q.popleft(); comp.append(cur)
            r, c = cur
            for nb in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if nb in conn and nb not in seen and linked(cur, nb):
                    seen.add(nb); q.append(nb)
        if not any(k[r][c] == "a" for r, c in comp) or len(comp) < 2:
            continue
        top = min(r for r, _ in comp)
        srcs = [x for x in comp if x[0] == top]
        dist = {x: 0 for x in srcs}; q = deque(srcs); cs = set(comp)
        while q:
            r, c = q.popleft()
            for nb in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if nb in cs and nb not in dist and linked((r, c), nb):
                    dist[nb] = dist[(r, c)] + 1; q.append(nb)
        for x, d in dist.items():
            out[x] = (cid, d)
        comp_len.append(max(dist.values()) + 1)
        cid += 1
    return out, comp_len, border


def pick_highlight(g, R, C, boxes, needle):
    """Rect (r1,c1,r2,c2) to pulse: the smallest box containing needle, else the text run, else the largest box."""
    if needle:
        for r in range(R):
            line = "".join(g[r])
            i = line.find(needle)
            if i < 0:
                continue
            inside = [b for b in boxes if b[0] <= r <= b[2] and b[1] <= i <= b[3]]
            inside = [b for b in inside if b[2] - b[0] >= 3] or inside
            if inside:
                return min(inside, key=lambda b: (b[2] - b[0]) * (b[3] - b[1]))
            return (r, i, r, i + len(needle) - 1)
        sys.exit(f"--highlight text not found: {needle!r}")
    if boxes:
        return max(boxes, key=lambda b: (b[2] - b[0]) * (b[3] - b[1]))
    return None


PAGE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://cdn.jsdelivr.net/npm/@fontsource/jetbrains-mono@5/400.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@fontsource/jetbrains-mono@5/700.css" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden}
body{background:%(page)s;display:flex;align-items:center;justify-content:center}
.win{width:%(ww)dpx;height:%(wh)dpx;background:%(win)s;border:1px solid %(edge)s;border-radius:%(rad)dpx;box-shadow:0 30px 80px %(shadow)s;overflow:hidden;display:flex;flex-direction:column}
.bar{height:%(bar)dpx;flex:none;background:%(barc)s;display:flex;align-items:center;padding:0 %(bp)dpx;gap:%(dg)dpx;border-bottom:1px solid %(edge)s}
.d{width:%(dot)dpx;height:%(dot)dpx;border-radius:50%%}
.t{flex:1;text-align:center;color:%(title)s;font:%(tf)dpx 'JetBrains Mono',Menlo,monospace;margin-right:%(dm)dpx}
.mid{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}
.stage{position:relative}
pre{position:relative;color:%(ink)s;font:%(fs).2fpx/%(lh).2fpx 'DejaVu Sans Mono',Menlo,Consolas,'Liberation Mono',monospace;white-space:pre;font-variant-ligatures:none;letter-spacing:0;z-index:1}
pre span{opacity:0}
#hl{position:absolute;border-radius:%(hr)dpx;background:rgba(%(glow)s,0);box-shadow:0 0 0 0 rgba(%(glow)s,0);z-index:0}
#cur{position:absolute;background:%(accent)s;z-index:2;opacity:0}
.foot{flex:none;display:flex;justify-content:space-between;padding:0 %(fp)dpx %(fb)dpx;font:%(ff)dpx 'JetBrains Mono',Menlo,monospace;color:%(foot)s}
.foot b{color:%(accent)s;font-weight:700}
</style></head><body><div class="win">
<div class="bar"><span class="d" style="background:#FF5F57"></span><span class="d" style="background:#FEBC2E"></span><span class="d" style="background:#28C840"></span><span class="t">~/%(stem)s</span></div>
<div class="mid"><div class="stage"><div id="hl"></div><pre id="p">%(pre)s</pre><div id="cur"></div></div></div>
<div class="foot"><span>%(label)s</span><b>%(handle)s</b></div>
</div>
<script>
const D = %(data)s;
const ink = D.ink, accent = D.accent;
const P = document.getElementById('p'), HL = document.getElementById('hl'), CUR = document.getElementById('cur');
const spans = Array.from(P.querySelectorAll('span'));
let cw = 0, lh = D.lh;
function measure(){ if(!spans.length) return; const a = spans[0]; cw = a.getBoundingClientRect().width; }
function mix(a, b, f){ // hex colours
  const pa=[1,3,5].map(i=>parseInt(a.substr(i,2),16)), pb=[1,3,5].map(i=>parseInt(b.substr(i,2),16));
  return 'rgb('+pa.map((v,i)=>Math.round(v+(pb[i]-v)*f)).join(',')+')';
}
window.seek = function(t){
  if(!cw) measure();
  t += D.offset;
  const fade = D.fadeStart === null ? 1 : Math.max(0, Math.min(1, 1 - (t - D.fadeStart) / D.fadeDur));
  P.style.opacity = fade; HL.style.opacity = fade;
  let last = null, lastT = -1;
  for(let i=0;i<spans.length;i++){
    const c = D.cells[i], s = spans[i];
    const age = t - c.t;
    if(age < 0){ s.style.opacity = 0; continue; }
    let op = c.k === 't' ? 1 : Math.min(1, age/0.12);
    let col = c.k === 'a' ? accent : ink;
    if(c.k === 'a' && age < 0.5) { s.style.textShadow = '0 0 '+(8*(1-age/0.5)).toFixed(1)+'px '+accent; } else s.style.textShadow = 'none';
    if(c.k === 't' && c.t > lastT){ lastT = c.t; last = c; }
    // flow packets along connectors after the reveal
    if(c.f && t > D.flowStart){
      const len = D.mod[c.f[0]];
      const pos = ((t - D.flowStart) * D.speed + 1e-6) %% len;  // epsilon: whole periods land on 0, not len-0.0001
      const behind = pos - c.f[1];
      if(behind >= 0 && behind < D.tail){
        const f = 1 - behind / D.tail;
        col = mix(c.k === 'a' ? accent : ink, accent, c.k === 'a' ? 1 : f);
        s.style.textShadow = '0 0 '+(3*f).toFixed(1)+'px '+accent;
      }
    }
    // highlight target text glows during pulse
    if(c.h && t > D.pulseStart){ const ph = 0.5 - 0.5*Math.cos((t - D.pulseStart) * Math.PI * 2 / D.pulsePeriod); col = mix(ink, accent, 0.25 + ph*0.5); }
    s.style.opacity = op; s.style.color = col;
  }
  // typing cursor: one cell right of the newest typed char, only during the reveal
  if(last && t < D.revealEnd + 0.4 && fade === 1){
    CUR.style.opacity = 1; CUR.style.left = ((last.c+1)*cw)+'px'; CUR.style.top = (last.r*lh + lh*0.12)+'px';
    CUR.style.width = (cw*0.9)+'px'; CUR.style.height = (lh*0.76)+'px';
  } else CUR.style.opacity = 0;
  // highlight pulse box
  if(D.hl && t > D.pulseStart){
    const [r1,c1,r2,c2] = D.hl, pad = cw*0.6;
    const ph = 0.5 - 0.5*Math.cos((t - D.pulseStart) * Math.PI * 2 / D.pulsePeriod);
    HL.style.left = (c1*cw - pad)+'px'; HL.style.top = (r1*lh - lh*0.15)+'px';
    HL.style.width = ((c2-c1+1)*cw + 2*pad)+'px'; HL.style.height = ((r2-r1+1)*lh + lh*0.3)+'px';
    HL.style.background = 'rgba('+D.glow+','+(D.hla+D.hla*1.4*ph).toFixed(3)+')';
    HL.style.boxShadow = '0 0 '+(6+22*ph).toFixed(0)+'px '+(2*ph).toFixed(0)+'px rgba('+D.glow+','+(0.10+0.25*ph).toFixed(3)+')';
  } else { HL.style.background = 'rgba('+D.glow+',0)'; HL.style.boxShadow = 'none'; }
};
</script></body></html>"""


def build_page(src, theme, W, H, handle, needle, reveal, hold, loop=None, fps=30):
    Cth = THEMES[theme]
    text = src.read_text(encoding="utf-8")
    g, R, C = parse(text)
    k = classify(g, R, C)
    boxes = find_boxes(g, R, C)
    t0, revealEnd = timeline(g, k, R, C, reveal)
    fl, comp_len, border = flows(g, k, R, C, boxes, t0)
    hl = pick_highlight(g, R, C, boxes, needle)
    # layout: window fills the frame, the diagram is fitted inside it
    m = round(min(W, H) * 0.045)
    ww, wh = W - 2 * m, H - 2 * m
    s = min(W, H) / 1080
    bar, footh = round(44 * s), round(56 * s)
    padx, pady = round(46 * s), round(26 * s)
    fs = min((ww - 2 * padx) / (C * 0.602), (wh - bar - footh - 2 * pady) / (R * 1.38))
    fs = min(fs, 30 * s)
    lh = fs * 1.38
    cells, pre = [], []
    for r in range(R):
        row = []
        for c in range(C):
            ch = g[r][c]
            if k[r][c] == " ":
                row.append(" ")
                continue
            hit = bool(hl) and hl[0] <= r <= hl[2] and hl[1] <= c <= hl[3] and k[r][c] == "t"
            cells.append(dict(r=r, c=c, k=k[r][c], t=round(t0[r][c], 4), f=fl.get((r, c)), h=hit))
            row.append(f"<span>{html.escape(ch)}</span>")
        pre.append("".join(row).rstrip())
    gap, speed, pulsePeriod = 14, 26.0, 1.6
    mod = [n + gap for n in comp_len]  # each connector wraps on its own length: fine once, not loopable
    flowStart, pulseStart = revealEnd + 0.2, revealEnd + 0.5
    offset, fadeStart, fadeDur, cycles, period = 0.0, None, 0.8, 0, None
    if loop:
        # One shared period P for every motion. P*fps is a whole number of frames, so P repeats exactly.
        M = (max(comp_len) if comp_len else 0) + gap
        period = max(round(M / speed * fps), round(pulsePeriod * fps)) / fps
        speed = M / period
        # short connectors carry k packets per period, so they don't sit dark; M/k keeps the period whole
        mod = [M / max(1, (M // (n + gap))) for n in comp_len]
        pulsePeriod = period / max(1, round(period / 1.6))
        cycles = max(1, int(-(-hold // period)))  # whole periods covering at least --hold seconds
        loopStart = round((revealEnd + 0.5) * fps) / fps  # after the cursor and the arrow glow are gone
        flowStart = pulseStart = loopStart
        if loop == "draw":
            fadeStart = loopStart + cycles * period  # flow and pulse are back at phase 0 here
        else:  # steady: frame 0 is the first frame of the loop, the reveal is never shown
            offset = loopStart
            flowStart = pulseStart = loopStart - period  # already running at frame 0, same phase
    data = dict(cells=cells, ink=Cth["ink"], accent=Cth["accent"], glow=Cth["glow"], lh=lh,
                comp=comp_len, mod=mod, gap=gap, speed=speed, tail=5, flowStart=flowStart,
                pulseStart=pulseStart, pulsePeriod=pulsePeriod, revealEnd=revealEnd, offset=offset,
                fadeStart=fadeStart, fadeDur=fadeDur,
                hla=0.05 if theme == 'cream' else 0.08, hl=list(hl) if hl else None)
    page = PAGE % dict(W=W, H=H, page=Cth["page"], ww=ww, wh=wh, win=Cth["win"], edge=Cth["edge"], rad=round(14 * s),
                       shadow=Cth["shadow"], bar=bar, barc=Cth["bar"], bp=round(18 * s), dg=round(9 * s), dot=round(13 * s),
                       title=Cth["title"], tf=round(14 * s), dm=round(60 * s), ink=Cth["ink"], fs=fs, lh=lh,
                       glow=Cth["glow"], hr=round(8 * s), accent=Cth["accent"], fp=round(30 * s), fb=round(22 * s),
                       ff=round(15 * s), foot=Cth["foot"], stem=html.escape(src.stem), pre="\n".join(pre),
                       label=html.escape(src.stem.replace("-", " ")), handle=html.escape(handle), data=json.dumps(data))
    if loop == "draw":
        total = fadeStart + fadeDur + 0.15  # ends on the empty window, which is what frame 0 shows
    elif loop == "steady":
        total = cycles * period
    else:
        total = pulseStart + hold
    return page, total, dict(rows=R, cols=C, boxes=len(boxes), flows=len(comp_len), font=round(fs, 1),
                             reveal=round(revealEnd, 2), total=round(total, 2), highlight=hl,
                             loop=loop, period=period and round(period, 3), cycles=cycles)


def render(page, total, W, H, fps, out, gif, loop=None):
    from playwright.sync_api import sync_playwright
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ascii-anim-"))
    hp = tmp / "page.html"; hp.write_text(page, encoding="utf-8")
    n = int(round(total * fps))
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps), "-i", "-",
                           "-vf", f"scale={W}:{H}:flags=lanczos", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--hide-scrollbars", "--disable-lcd-text"])
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto(hp.as_uri()); pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready.then(()=>1)")
        for i in range(n):
            pg.evaluate(f"seek({i / fps:.4f})")
            ff.stdin.write(pg.screenshot(type="png"))
            if i % (fps * 2) == 0:
                print(f"  frame {i}/{n}", end="\r", flush=True)
        if loop:  # the frame after the last one must look like frame 0, or the loop jumps
            pg.evaluate(f"seek({n / fps:.4f})"); after = pg.screenshot(type="png")
            pg.evaluate("seek(0)"); first = pg.screenshot(type="png")
            print(f"  seam {seam_diff(first, after)}")
        b.close()
    ff.stdin.close(); ff.wait()
    if ff.returncode:
        sys.exit("ffmpeg failed")
    if gif:
        g = out.with_suffix(".gif")
        w = min(W, 1080)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out), "-vf",
                        f"fps=15,scale={w}:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse=dither=none",
                        str(g)], check=True)
        print(f"  gif  {g}")


def seam_diff(a, b):
    """Max and mean per-channel pixel difference between two PNG screenshots (0 = identical)."""
    try:
        from PIL import Image, ImageChops, ImageStat
    except ImportError:
        return "not checked (pip install pillow)"
    import io
    d = ImageChops.difference(Image.open(io.BytesIO(a)).convert("RGB"), Image.open(io.BytesIO(b)).convert("RGB"))
    mx = max(hi for _, hi in d.getextrema())
    return f"max pixel diff {mx}/255, mean {sum(ImageStat.Stat(d).mean) / 3:.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("--theme", choices=["dark", "cream"], default="dark")
    ap.add_argument("--size", default="both", help="1080x1080, 1600x900, both, or any WxH")
    ap.add_argument("--highlight", default=None, help="text to pulse; its box pulses if it sits inside one")
    ap.add_argument("--handle", default="@maurojpelle")
    ap.add_argument("--reveal", type=float, default=9.0, help="target seconds for the draw-in")
    ap.add_argument("--hold", type=float, default=5.0, help="seconds of flow + pulse after the draw-in")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--out", default=None, help="output dir (default: examples/ next to this script)")
    ap.add_argument("--gif", action="store_true", help="also write a GIF (X turns GIFs into soft MP4s; prefer the MP4)")
    ap.add_argument("--loop", nargs="?", const="draw", choices=["draw", "steady"], default=None,
                    help="seamless loop: draw (draw in, flow, fade back to empty) or steady (flow only)")
    a = ap.parse_args()
    src = pathlib.Path(a.src)
    out_dir = pathlib.Path(a.out) if a.out else pathlib.Path(__file__).resolve().parent / "examples"
    out_dir.mkdir(parents=True, exist_ok=True)
    sizes = ["1080x1080", "1600x900"] if a.size == "both" else [a.size]
    for sz in sizes:
        W, H = (int(x) for x in sz.lower().split("x"))
        page, total, info = build_page(src, a.theme, W, H, a.handle, a.highlight, a.reveal, a.hold, a.loop, a.fps)
        tag = {"draw": "-loop", "steady": "-steady"}.get(a.loop, "")
        out = out_dir / f"{src.stem}-{a.theme}-{W}x{H}{tag}.mp4"
        print(f"{out.name}: {info}")
        render(page, total, W, H, a.fps, out, a.gif, a.loop)
        print(f"  mp4  {out}  ({out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
