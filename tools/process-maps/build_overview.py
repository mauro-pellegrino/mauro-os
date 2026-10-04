#!/usr/bin/env python3
"""Render the content-system overview from overview.json (the single source of truth).
Edit the JSON, never the HTML: status of each process, its weekly numbers, and the changelog.
The Monday review fills each process's "week" numbers, adds one changelog line, then re-runs this.
Usage: python3 tools/process-maps/build_overview.py [path/to/overview.json]  -> overview.png next to the JSON"""
import json, pathlib, subprocess, sys, html as H
HERE = pathlib.Path(__file__).resolve().parent
CHROMES = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
           r"C:\Program Files\Google\Chrome\Application\chrome.exe",
           "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
src = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / "overview.json"
d = json.loads(src.read_text())
CSS = (HERE / "overview.css").read_text()
TAG = {"mapped": '<span class="st ok">MAPPED</span>', "drafted": '<span class="st dr">DRAFTED</span>', "proposed": '<span class="st pr">PROPOSED</span>'}
def wk(w):
    if not w: return ""
    f = lambda v, u: f"{v if v is not None else '?'}{u}"
    return f'<div class="wk">this week · {f(w.get("shipped"), " shipped")} · {f(w.get("human_min"), " min yours")} · {f(w.get("calls"), " calls")}</div>'
def proc(p): return f'<div class="p{" prop" if p["status"] == "proposed" else ""}">{TAG[p["status"]]}{H.escape(p["t"])}<small>{H.escape(p["d"])}</small>{wk(p.get("week"))}</div>'
lanes = d["lanes"]; big = [l for l in lanes if len(l["processes"]) > 1]; small = [l for l in lanes if len(l["processes"]) == 1]
lane = lambda l, extra="": f'<div class="lane"{extra}><div class="lh">{H.escape(l["name"])}</div><div class="ps">{"".join(proc(p) for p in l["processes"])}</div></div>'
lanes_html = "".join(lane(l) for l in big) + '<div style="display:flex;gap:12px">' + "".join(lane(l, ' style="flex:1;margin:0"') for l in small) + "</div>"
inputs = "".join(f'<div class="in {i["who"]}{" prop" if i["status"] == "proposed" else ""}">{H.escape(i["t"])}<small>{H.escape(i["d"])}</small></div>' for i in d["inputs"])
shared = "".join(f'<div class="m {s["who"]}">{H.escape(s["t"])}<small>{H.escape(s["d"])}</small></div>' for s in d["shared"])
r = d["review"]; cl = "".join(f"<div>{H.escape(c)}</div>" for c in d["changelog"][-3:])
arch = "".join(f'<div class="ab">{H.escape(a["t"])}<small>{H.escape(a["d"])}</small></div>' for a in d.get("arch", []))
arch_html = f'<div class="arch"><div class="ch">{H.escape(d.get("arch_title", "UNDER IT · HOW CLAUDE CODE RUNS THIS"))}</div><div class="ag">{arch}</div></div>' if arch else ""
page = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><h1>{H.escape(d["title"])}</h1>
<div class="sub">inputs → processes → shared → review → back to inputs · black tag = mapped · white = drafted · dashed = proposed</div></div>
<div class="ver"><b>{H.escape(d["version"])}</b><br>North Star: {H.escape(d["north_star"])}</div></div>
<div class="row">
 <div class="col" style="width:420px;background:#FFF9DF"><div class="ch">1 · WEEKLY INPUTS</div>{inputs}</div><div class="arrow">→</div>
 <div class="col" style="flex:1"><div class="ch">2 · PROCESSES, ONE SHIPPED OUTPUT EACH</div>{lanes_html}</div><div class="arrow">→</div>
 <div class="col" style="width:330px"><div class="ch">3 · SHARED, DRAWN ONCE</div>{shared}</div><div class="arrow">→</div>
 <div class="col" style="width:300px;background:#F6EEFF"><div class="ch">4 · WEEKLY REVIEW</div><div class="m R">{H.escape(r["t"])}<small>{H.escape(r["d"])}</small></div>
 <div style="font-size:14px;font-weight:700;margin-top:6px;line-height:1.4">→ fills the "this week" line on every process<br>→ what won goes back into the inputs</div></div>
</div>
<div class="back">↺ <span>LOOP: the Monday review decides next week's inputs. A template that won gets reused. A template that lost gets retired.</span></div>
<div class="rule">
 <div class="rb">One process = one trigger<small>something arrives: a proven post, a brief, a Monday</small></div>
 <div class="rb">One shipped output<small>a post, an article, a board. Never "LinkedIn strategy"</small></div>
 <div class="rb">One person presses go<small>and one number it moves on Monday</small></div>
 <div class="rb">6 to 12 steps<small>shared steps become modules · X or LinkedIn is a switch inside one process</small></div>
</div>
{arch_html}
<div class="log"><b>CHANGELOG</b>{cl}</div>
</body></html>"""
out = src.with_name("overview.html"); out.write_text(page, encoding="utf-8"); png = src.with_name("overview.png")
chrome = next((c for c in CHROMES if pathlib.Path(c).exists()), None)
if chrome is None: sys.exit("No Chrome/Chromium found. Add its path to CHROMES.")
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                "--window-size=2200,1250", f"--screenshot={png}", out.as_uri()], stderr=subprocess.DEVNULL, check=True)
print(png)
