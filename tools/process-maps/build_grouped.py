#!/usr/bin/env python3
"""Style D process map from a JSON spec. Human steps are single boxes down the left with a side note
that says exactly what to do. Consecutive Claude steps sit in one orange block on the right, each step
with chips naming the skills and tools it uses. A time strip at the bottom shows who holds the work,
step by step, striped where it waits on someone.
Usage: python3 tools/process-maps/build_grouped.py --json specs/<name>.json [more.json ...]
       -> <name>.html + <name>.png next to each spec
Spec format: specs/_example.json.txt. Images in "img" load from tools/process-maps/assets/."""
import subprocess, pathlib, sys, json
HERE = pathlib.Path(__file__).resolve().parent
CHROMES = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
           r"C:\Program Files\Google\Chrome\Application\chrome.exe",
           "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
# who holds the step: Y you (the owner) · C Claude · V VA · P partner · K client · R the Monday review
COL = dict(Y="#F7D95C", C="#F2B69A", V="#A8E6B4", P="#FFC2D1", K="#D7D2C8", R="#E9D8FD")
NAME = dict(Y="You", C="Claude", V="VA", P="Partner", K="Client", R="Monday")
CLAUDE = "#D97757"
CSS = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}body{font-family:Inter,sans-serif;color:#1A1A1A;position:relative;
background:#F1F1F0;background-image:linear-gradient(#E3E3E1 1px,transparent 1px),linear-gradient(90deg,#E3E3E1 1px,transparent 1px);background-size:40px 40px}
.abs{position:absolute}.box{border:2.5px solid #1A1A1A;font-weight:800;text-align:center;display:flex;flex-direction:column;justify-content:center}
.tag{display:inline-block;background:#D9534F;color:#fff;border:2px solid #8E2A27;border-radius:8px;font-weight:700;font-size:14px;padding:3px 8px;white-space:nowrap}
.tag.q{background:#fff;color:#8E2A27;border-style:dashed}
.chip{display:inline-block;background:#fff;border:2px solid #1A1A1A;border-radius:6px;font-size:13px;font-weight:700;padding:3px 8px;margin:3px 4px 0 0}
.engine{background:#FBE3D8;border:4px solid #1A1A1A;border-radius:14px}
.ehead{background:%s;color:#fff;font-weight:900;letter-spacing:.14em;font-size:17px;padding:10px 18px;border-radius:9px 9px 0 0;display:flex;justify-content:space-between}
.mini{background:#fff;border:2.5px solid #1A1A1A;border-radius:8px}
.thumb{border:2px solid #1A1A1A;background:#fff;box-shadow:0 6px 18px rgba(0,0,0,.15);overflow:hidden}
.thumb img{width:100%%;height:100%%;object-fit:cover;object-position:top;display:block}
h1{font-weight:900;letter-spacing:-.02em}.out{font-size:15px;font-weight:600;color:#555}""" % CLAUDE
def tag(t): return f'<span class="tag{"" if t else " q"}">{t or "? MIN"}</span>'
ARROW = '<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1A1A1A"/></marker></defs>'
def line(d): return f'<path d="{d}" stroke="#1A1A1A" stroke-width="2.5" fill="none" marker-end="url(#a)"/>'
def mins(t):
    try: return int(t.split()[0])
    except (AttributeError, ValueError, IndexError): return 0
def legend(spec):
    used = ["C"] + [k for k in "YVPKR" if any(s[0] == "H" and s[1]["who"] == k for s in spec["segs"])]
    return "".join(f'<span style="display:inline-flex;align-items:center;gap:8px;margin-right:20px"><span style="width:26px;height:18px;border:2px solid #1A1A1A;background:{COL[k]}"></span>{NAME[k]}</span>' for k in used)
def render(out, page, w, h):
    f = out.with_suffix(".html"); f.write_text(page, encoding="utf-8"); png = out.with_suffix(".png")
    chrome = next((c for c in CHROMES if pathlib.Path(c).exists()), None)
    if chrome is None: sys.exit("No Chrome/Chromium found. Add its path to CHROMES.")
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2", "--virtual-time-budget=4000",
                    f"--window-size={w},{h}", f"--screenshot={png}", f.as_uri()], stderr=subprocess.DEVNULL, check=True)
    return png
def counts(spec):
    return sum(1 for s in spec["segs"] if s[0] == "H"), sum(len(s[1]) for s in spec["segs"] if s[0] == "C")

def style_d(spec, out):
    A = (HERE / "assets").as_uri()
    W = 1800; hx, hw, hh = 70, 380, 96; ex, ew = 720, 1010
    parts, paths, y, n = [], [], 200, 0; prev = None
    for i, (kind, seg) in enumerate(spec["segs"]):
        if kind == "H":
            n += 1; s = seg
            parts.append(f'<div class="abs box" style="left:{hx}px;top:{y}px;width:{hw}px;height:{hh}px;background:{COL[s["who"]]};font-size:24px">{n}. {s["t"]}<span style="font-size:14px;font-weight:600;color:#333;margin-top:4px">{NAME[s["who"]]} · {s["tool"]}</span></div>')
            parts.append(f'<div class="abs" style="left:{hx+hw-70}px;top:{y-16}px">{tag(s.get("time"))}</div>')
            parts.append(f'<div class="abs out" style="left:{hx}px;top:{y+hh+6}px">→ {s["out"]}</div>')
            if prev: paths.append(line(f'M{prev[0]},{prev[1]} V{y-3}'))
            if s.get("notes"):
                li = "".join(f'<div style="display:flex;gap:8px;margin-top:4px"><span style="color:#D9534F">▸</span><span>{t}</span></div>' for t in s["notes"])
                parts.append(f'<div class="abs" style="left:{hx+hw+18}px;top:{y-6}px;width:330px;background:#fff;border:2px solid #1A1A1A;border-left:8px solid {COL[s["who"]]};padding:8px 12px 10px;font-size:14.5px;font-weight:600;line-height:1.3">{li}</div>')
                paths.append(f'<path d="M{hx+hw},{y+hh/2} H{hx+hw+18}" stroke="#1A1A1A" stroke-width="2" fill="none"/>')
            if s.get("img"):
                parts.append(f'<div class="abs thumb" style="left:{hx+hw+370}px;top:{y-10}px;width:150px;height:{hh+30}px"><img src="{A}/{s["img"]}"></div>')
            prev = (hx + hw / 2, y + hh); y += hh + 92
        else:
            rows = seg; rh = 132; top = y - 40; eh = 56 + len(rows) * (rh + 14) + 20
            total = sum(mins(r.get("time")) for r in rows)
            parts.append(f'<div class="abs engine" style="left:{ex}px;top:{top}px;width:{ew}px;height:{eh}px"><div class="ehead"><span>CLAUDE · {len(rows)} STEP{"S IN A ROW" if len(rows) > 1 else ""}</span><span>{f"{total} MIN" if total else "? MIN"}</span></div></div>')
            if prev: paths.append(line(f'M{prev[0]},{prev[1]} V{top+28} H{ex-3}'))
            ry = top + 70
            for r in rows:
                n += 1
                chips = "".join(f'<span class="chip">{k}</span>' for k in r["skills"])
                br = f'<div style="margin-top:8px;border:2px dashed #1A1A1A;padding:5px 8px;font-size:13px;font-weight:700;background:#FFF8F4;display:inline-block">{r["branch"]}</div>' if r.get("branch") else ""
                img = f'<div class="thumb" style="width:150px;height:{rh-18}px;flex:none"><img src="{A}/{r["img"]}"></div>' if r.get("img") else ""
                parts.append(f'''<div class="abs mini" style="left:{ex+22}px;top:{ry}px;width:{ew-44}px;height:{rh}px;padding:12px 16px;display:flex;gap:16px;align-items:center">
<div style="font-size:34px;font-weight:900;width:44px;color:{CLAUDE}">{n}</div>
<div style="flex:1"><div style="display:flex;align-items:center;gap:12px"><span style="font-size:23px;font-weight:800">{r["t"]}</span>{tag(r.get("time"))}</div>
<div>{chips}</div><div class="out" style="margin-top:6px">→ {r["out"]}</div>{br}</div>{img}</div>''')
                if r is not rows[-1]: paths.append(line(f'M{ex+66},{ry+rh} V{ry+rh+11}'))
                ry += rh + 14
            bottom = top + eh; y = bottom + 60
            if i < len(spec["segs"]) - 1:  # exit arrow back to the human column, only if something follows
                paths.append(f'<path d="M{ex+ew/2},{bottom} V{y-20} H{hx+hw/2}" stroke="#1A1A1A" stroke-width="2.5" fill="none"/>')
            prev = (hx + hw / 2, y - 20)
    # time strip: one cell per step, coloured by who holds the work (value stream view)
    seq = []
    for kind, seg in spec["segs"]:
        if kind == "H": seq.append((seg["who"], seg.get("time"), seg.get("wait")))
        else: seq += [("C", r.get("time"), False) for r in seg]
    sw = (W - 140) / len(seq); cells = ""
    for k, (who, t, wait) in enumerate(seq):
        bg = "repeating-linear-gradient(45deg,%s,%s 8px,#fff 8px,#fff 14px)" % (COL[who], COL[who]) if wait else COL[who]
        cells += f'<div style="width:{sw}px;height:64px;background:{bg};border-right:2px solid #1A1A1A;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;font-size:15px"><span style="font-size:20px">{k+1}</span>{t or "?"}</div>'
    parts.append(f'<div class="abs" style="left:70px;top:{y}px;font-size:16px;font-weight:900;letter-spacing:.12em">TIME STRIP · who holds the work, step by step · striped = waiting on someone</div><div class="abs" style="left:70px;top:{y+28}px;display:flex;border:3px solid #1A1A1A">{cells}</div>')
    y += 130
    H = y + 60; hc, cc = counts(spec)
    pri = f'<div class="abs" style="left:72px;top:132px;font-size:16px;font-weight:800;background:#1A1A1A;color:#fff;padding:6px 12px;border-radius:6px">{spec["priority"]}</div>' if spec.get("priority") else ""
    head = f'<h1 class="abs" style="left:70px;top:36px;font-size:46px">{spec["title"]}</h1><div class="abs" style="left:72px;top:100px;font-size:17px;font-weight:700">{legend(spec)}</div>{pri}'
    foot = f'<div class="abs" style="left:70px;top:{H-50}px;font-size:21px;font-weight:800">{cc} Claude steps · {hc} outside Claude · {spec["foot"]}</div>'
    return render(out, f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}body{{width:{W}px;height:{H}px}}</style></head><body>{head}<svg class="abs" width="{W}" height="{H}" style="left:0;top:0">{ARROW}{"".join(paths)}</svg>{"".join(parts)}{foot}</body></html>', W, H)

def load_json(path):
    d = json.loads(pathlib.Path(path).read_text()); segs = []
    for g in d["segs"]:
        if g["kind"] == "H":
            assert g["who"] in NAME and g["who"] != "C", f'bad "who" {g["who"]!r} in {g["t"]}: use one of Y V P K R'
            segs.append(("H", {k: v for k, v in g.items() if k != "kind"}))
        else: segs.append(("C", g["steps"]))
    return dict(title=d["title"], foot=d.get("foot", ""), priority=d.get("priority"), segs=segs)
if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "--json": sys.exit(__doc__)
    for f in sys.argv[2:]:
        p = pathlib.Path(f).resolve(); print(style_d(load_json(p), p.with_suffix("")))
