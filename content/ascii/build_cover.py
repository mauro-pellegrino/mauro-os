#!/usr/bin/env python3
"""5:2 article cover in the terminal style: a dark terminal window on a brand background, packed with a
pixel headline, a subtitle, a file tree, 1-2 ASCII diagrams read from .txt files, a 4-5 column strip,
and a prompt + handle footer.
Usage: python3 content/ascii/build_cover.py <spec.json>  -> <slug>-cover.png next to the spec (3000x1200)
Spec keys (required): slug, title, sub, cols [{h, items[]}], tree [lines]
Spec keys (optional, defaults in DEFAULTS): handle, user, host, bg, accent, hsize, mid [{file, from, to}]
See content/ascii/covers/_example.json."""
import json, sys, html, pathlib, subprocess
DEFAULTS = dict(handle="@maurojpelle", user="mauro", host="ghostedcalls",
                bg="#F5EFE4",       # brand/colors.md base / cream
                accent="#E0A854",   # brand/colors.md accent (amber)
                hsize=50)
CHROMES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]
src = pathlib.Path(sys.argv[1]).resolve()
spec = {**DEFAULTS, **json.loads(src.read_text())}
E = html.escape; A = spec["accent"]
cols = "".join(f'''<div class="c"><div class="ch">{E(c["h"])}</div>{"".join(f'<div class="ci">{E(i)}</div>' for i in c["items"])}</div>''' + ('<div class="ar">──&gt;</div>' if k < len(spec["cols"]) - 1 else "") for k, c in enumerate(spec["cols"]))
mids = []
for m in (spec.get("mid") or []):
    f = pathlib.Path(m["file"]); f = f if f.is_absolute() else src.parent / f
    lines = f.read_text(encoding="utf-8").rstrip("\n").split("\n")
    mids.append("\n".join(l.rstrip() for l in lines[m.get("from", 0):m.get("to", 13)]))
tree = "".join(f'<div>{E(t) or "&nbsp;"}</div>' for t in spec["tree"])
page = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1500px;height:600px;overflow:hidden;background:{spec["bg"]};background-image:radial-gradient(#17131022 1.2px,transparent 1.2px);background-size:18px 18px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace}}
.win{{width:1410px;height:540px;background:#121417;border:1px solid #2A2E35;border-radius:12px;box-shadow:0 24px 60px rgba(40,30,0,.35);overflow:hidden;display:flex;flex-direction:column}}
.bar{{height:30px;background:#22262D;display:flex;align-items:center;padding:0 14px;gap:7px;color:#7C8595;font-size:12px}}
.d{{width:11px;height:11px;border-radius:50%}}.t{{flex:1;text-align:center;margin-right:50px}}
.in{{flex:1;display:flex;padding:16px 26px 12px;gap:22px;color:#D7DCE4;min-height:0}}
.tree{{width:250px;flex:none;font-size:12.5px;line-height:1.55;color:#9AA3B2;border-right:1px solid #2E3440;padding-right:16px;white-space:pre}}
.tree div:first-child{{color:{A};font-weight:700}}
.main{{flex:1;display:flex;flex-direction:column;min-width:0}}
.h{{position:relative;font-family:Silkscreen,monospace;font-weight:700;font-size:{spec["hsize"]}px;line-height:1.02;color:#fff;letter-spacing:.5px}}
.h .sh{{position:absolute;left:4px;top:4px;color:{A}55;z-index:0}}.h .fg{{position:relative;z-index:1}}
.sub{{margin-top:8px;font-size:13px;color:#AEB6C4;max-width:960px;line-height:1.45}}
.mids{{margin-top:10px;display:flex;gap:18px;flex:1;min-height:0;overflow:hidden}}
.mid{{font-size:9.6px;line-height:1.22;color:#9AA3B2;white-space:pre;overflow:hidden}}
.sys{{margin-top:8px;display:flex;align-items:stretch;gap:6px;border-top:1px solid #2E3440;padding-top:14px}}
.c{{flex:1;border:1px solid #4A5160;padding:8px 10px;min-width:0}}
.ch{{font-size:12px;font-weight:700;color:{A};letter-spacing:.08em;margin-bottom:6px;border-bottom:1px solid #3A404C;padding-bottom:4px}}
.ci{{font-size:11.5px;line-height:1.35;color:#D7DCE4;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.ar{{align-self:center;color:#7C8595;font-size:13px}}
.foot{{display:flex;justify-content:space-between;margin-top:8px;font-size:12.5px;color:#7C8595}}
.foot b{{color:{A}}} .cur{{display:inline-block;width:8px;height:14px;background:#D7DCE4;vertical-align:-2px;margin-left:4px}}
</style></head><body><div class="win">
<div class="bar"><span class="d" style="background:#FF5F57"></span><span class="d" style="background:#FEBC2E"></span><span class="d" style="background:#28C840"></span><span class="t">{E(spec["user"])} · -zsh · {E(spec["slug"])} · 269x44</span></div>
<div class="in"><div class="tree">{tree}</div>
<div class="main"><div class="h"><div class="sh">{E(spec["title"])}</div><div class="fg">{E(spec["title"])}</div></div>
<div class="sub">{E(spec["sub"])}</div>
<div class="mids">{"".join(f'<pre class="mid">{E(x)}</pre>' for x in mids)}</div>
<div class="sys">{cols}</div>
<div class="foot"><span>{E(spec["user"])}@{E(spec["host"])} ~ % <span class="cur"></span></span><b>{E(spec["handle"])}</b></div></div></div>
</div></body></html>"""
out = src.with_suffix("")
h = out.with_suffix(".html"); h.write_text(page, encoding="utf-8")
png = (src.parent / f'{spec["slug"]}-cover.png').resolve()
chrome = next((c for c in CHROMES if pathlib.Path(c).exists()), None)
if chrome is None:
    sys.exit("No Chrome/Chromium found. Add its path to CHROMES in this script.")
# --virtual-time-budget gives the Google fonts time to load before the screenshot
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                "--virtual-time-budget=6000", "--window-size=1500,600", f"--screenshot={png}", h.resolve().as_uri()],
               stderr=subprocess.DEVNULL, check=True)
if not png.exists():
    sys.exit(f"Chrome ran but wrote no PNG: {png}")
print(png)
