#!/usr/bin/env python3
"""Format D, ranked countdown. Builds three recording boards plus thumbnails, notes and meta.json.

    python3 boards/yt/v2/d-countdown/build.py          # writes html, notes, thumbs, meta.json
    python3 boards/yt/v2/d-countdown/build.py --png    # also renders cover + thumbs PNGs

Every number on a frame comes from brand/claims.md. A number that is not there renders as a red
[NEEDS: x] chip. Docs: research/video-knowledge/11, 07, 04.

Board mechanics: a 1600x900 stage scaled to the viewport. Left: the scoreboard rail, one row per rank,
blurred until its reveal frame. Right: the frame. Arrows/space move, N toggles presenter notes,
F fullscreen. #12 in the URL opens frame 12.
"""
import base64
import html
import json
import os
import re
import subprocess
import sys
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import controls  # noqa: E402  (shared recording control bar, boards/yt/v2/controls.py)

NAV_ADAPTER = "{count:()=>frames.length,index:()=>i,go:show,next:()=>show(i+1),prev:()=>show(i-1),label:k=>(frames[k].dataset.time||'')+' · '+frames[k].textContent.slice(0,90)}"

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "../../../.."))
THUMBS = os.path.join(REPO, "research/charlie-morgan/thumbs")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SMALL = os.environ.get("DCOUNT_SMALL", "")  # optional folder of pre-shrunk thumbs; else sips shrinks to 480px

E = html.escape


def img64(name):
    p = os.path.join(SMALL, name)
    if not os.path.exists(p):
        import tempfile
        p = os.path.join(tempfile.gettempdir(), "dcount-" + name)
        subprocess.run(["sips", "-Z", "480", "-s", "formatOptions", "70", os.path.join(THUMBS, name), "--out", p],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(p, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


CM = sorted(f for f in os.listdir(THUMBS) if f.endswith(".jpg"))

FONTS = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap"

CSS = """
:root{--ground:#F7F3EA;--card:#FFFFFF;--ink:#1B4332;--deep:#0E2418;--body:#1B1B1B;--muted:#5F6B62;
--accent:#E9B949;--sage:#52B788;--mint:#B7E4C7;--line:#D8CFBB;--red:#C0392B}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#0B1A12;overflow:hidden}
body{font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;color:var(--body)}
.mono{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace}
#stage{position:absolute;left:50%;top:50%;width:1600px;height:900px;transform-origin:center center;background:var(--ground);overflow:hidden;display:flex}
/* rail */
#rail{width:330px;flex:none;background:var(--deep);color:#fff;padding:34px 22px 26px;display:flex;flex-direction:column;gap:10px;position:relative}
#rail .rh{font:800 14px 'JetBrains Mono',monospace;letter-spacing:.2em;color:var(--sage);text-transform:uppercase;margin-bottom:6px}
#rail .crit{font:600 17px 'Inter';color:#CFE0D5;line-height:1.3;margin-bottom:12px}
.row{flex:1;max-height:120px;display:flex;align-items:center;gap:14px;padding:10px 14px;border-radius:10px;background:rgba(255,255,255,.04);border:2px solid transparent;transition:all .35s}
.row .rk{font:900 48px 'Inter';width:84px;color:#5F7D6C;letter-spacing:-.03em;flex:none}
.row .lb{font:800 22px 'Inter';line-height:1.2;color:#fff;filter:blur(9px);opacity:.55;transition:all .45s}
.row .st{font:700 16px 'JetBrains Mono',monospace;color:var(--accent);margin-top:4px;display:block}
.row.on .lb{filter:none;opacity:1}
.row.on .rk{color:var(--accent)}
.row.focus{background:rgba(233,185,73,.14);border-color:var(--accent)}
.row.focus .rk{color:var(--accent)}
#rail .foot{margin-top:14px;font:600 13px 'JetBrains Mono',monospace;color:#7FA08D;letter-spacing:.08em}
/* frame area */
#frames{flex:1;position:relative}
.frame{position:absolute;inset:0;padding:64px 80px 56px;display:none;flex-direction:column;justify-content:center}
.frame.cur{display:flex}
.frame.dark{background:var(--deep);color:#fff}
.k{font:800 16px 'JetBrains Mono',monospace;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:22px}
.dark .k{color:var(--sage)}
.h{font-size:64px;font-weight:900;line-height:1.04;letter-spacing:-.03em;color:var(--ink)}
.h.md{font-size:52px}.h.sm{font-size:42px}
.dark .h{color:#fff}
.hl{background:var(--accent);color:var(--deep);padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.vis{margin-top:40px}
.src{position:absolute;left:80px;bottom:24px;font:500 13px 'JetBrains Mono',monospace;color:var(--muted)}
.dark .src{color:#7FA08D}
.needs{display:inline-block;background:var(--red);color:#fff;font:800 15px 'JetBrains Mono',monospace;padding:5px 10px;border-radius:4px;letter-spacing:.02em;vertical-align:middle}
#rail .needs{font-size:11px;padding:4px 7px;margin-top:6px}
/* reveal */
.reveal{display:flex;align-items:center;gap:56px}
.reveal .num{font:900 330px 'Inter';line-height:.8;letter-spacing:-.06em;color:var(--accent)}
.reveal .num small{font-size:120px;vertical-align:top;color:var(--sage)}
.reveal .nm{font-size:66px;font-weight:900;line-height:1.02;letter-spacing:-.03em;color:#fff;max-width:640px}
.reveal .stat{margin-top:26px;font:800 24px 'JetBrains Mono',monospace;color:var(--sage)}
/* cards */
.grid{display:grid;gap:18px}
.card{background:var(--card);border:3px solid var(--ink);border-radius:10px;padding:22px 24px}
.card .t{font-size:28px;font-weight:800;color:var(--ink);line-height:1.15}
.card .s{margin-top:8px;font:600 15px 'JetBrains Mono',monospace;color:var(--muted)}
.card.on{border-top:12px solid var(--accent)}
.card.off{opacity:.35}
.card.redx{border-color:var(--red)}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.ba .side{border-radius:12px;padding:26px;min-height:380px;display:flex;flex-direction:column}
.ba .before{background:#EDE6D6;border:3px solid #CBBFA6}
.ba .after{background:var(--card);border:3px solid var(--ink);border-top:12px solid var(--accent)}
.ba .tag{font:800 15px 'JetBrains Mono',monospace;letter-spacing:.2em;margin-bottom:18px;color:var(--muted)}
.ba .after .tag{color:var(--ink)}
/* code / mock screens */
.win{background:#13241B;border-radius:12px;overflow:hidden;border:2px solid #24503A;box-shadow:0 18px 40px rgba(0,0,0,.18)}
.win .bar{height:36px;background:#1E3A2A;display:flex;align-items:center;gap:8px;padding:0 14px}
.win .bar i{width:12px;height:12px;border-radius:50%;background:#5F7D6C;display:block}
.win .bar span{margin-left:12px;font:600 14px 'JetBrains Mono',monospace;color:#9DB8A8}
.win pre{font:500 19px/1.5 'JetBrains Mono',monospace;color:#DDEBE2;padding:20px 24px;white-space:pre}
.win pre b{color:var(--accent);font-weight:700}
.win pre em{color:var(--sage);font-style:normal}
.win pre u{color:#FF8A7A;text-decoration:none}
.win pre s{color:#7FA08D;text-decoration:none}
.thumbs{display:grid;gap:12px}
.thumbs .th{position:relative;border-radius:8px;overflow:hidden;aspect-ratio:16/9;background:#222}
.thumbs .th .img{width:100%;height:100%;background-size:cover;background-position:center}
.thumbs .th.dim .img{filter:grayscale(1) brightness(.45)}
.thumbs .th .lab{position:absolute;left:8px;bottom:8px;background:var(--deep);color:var(--accent);font:800 14px 'JetBrains Mono',monospace;padding:4px 8px;border-radius:4px}
.thumbs .th .no{position:absolute;left:8px;top:8px;background:rgba(0,0,0,.7);color:#fff;font:800 14px 'JetBrains Mono',monospace;padding:3px 7px;border-radius:4px}
.thumbs .th.ring{outline:5px solid var(--accent);outline-offset:-5px}
.tt{font-size:25px;font-weight:700;color:var(--body);line-height:1.3;padding:14px 18px;background:var(--card);border-left:8px solid var(--line);border-radius:6px}
.tt mark{background:var(--accent);color:var(--deep);padding:0 4px;border-radius:3px}
.tt.dim{opacity:.35}
.tt .v{float:right;font:700 15px 'JetBrains Mono',monospace;color:var(--muted);margin-top:6px}
.agenda{display:flex;flex-direction:column;gap:16px;margin-top:36px}
.agenda div{display:flex;align-items:center;gap:20px;font-size:38px;font-weight:800;color:#fff}
.agenda span{font:800 20px 'JetBrains Mono',monospace;background:var(--accent);color:var(--deep);padding:6px 12px;border-radius:4px}
.cta .h{font-size:76px}
.pill{display:inline-block;margin-top:34px;background:var(--accent);color:var(--deep);font-weight:900;font-size:40px;padding:16px 30px;border-radius:10px}
/* notes overlay */
#notes{position:absolute;left:330px;right:0;bottom:0;max-height:62%;overflow:auto;background:rgba(14,36,24,.96);color:#EAF3EE;padding:22px 30px 26px;font:500 21px/1.5 'Inter';display:none;border-top:4px solid var(--accent);z-index:9}
#notes.on{display:block}
#notes .meta{font:700 14px 'JetBrains Mono',monospace;color:var(--accent);letter-spacing:.1em;margin-bottom:8px}
#notes p{margin-bottom:8px}
"""

JS = """
const frames=[...document.querySelectorAll('.frame')];
const rows=[...document.querySelectorAll('#rail .row')];
const notes=document.getElementById('notes');
let i=0;
function fit(){const s=Math.min(innerWidth/1600,innerHeight*__SAFE_H__/900),g=document.getElementById('stage');g.style.top=(450*s)+'px';g.style.transform='translate(-50%,-50%) scale('+s+')';}
function show(n){i=Math.max(0,Math.min(frames.length-1,n));frames.forEach((f,j)=>f.classList.toggle('cur',j===i));
 const f=frames[i];const upto=parseInt(f.dataset.upto||'99');const focus=parseInt(f.dataset.focus||'0');
 rows.forEach(r=>{const rk=parseInt(r.dataset.rank);r.classList.toggle('on',rk>=upto);r.classList.toggle('focus',rk===focus);});
 notes.innerHTML='<div class="meta">FRAME '+(i+1)+' / '+frames.length+' · '+(f.dataset.time||'')+'</div>'+(f.querySelector('template.say')?f.querySelector('template.say').innerHTML:'');
 history.replaceState(null,'','#'+(i+1));}
addEventListener('keydown',e=>{
 if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();show(i+1);}
 else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();show(i-1);}
 else if(e.key==='n'||e.key==='N'){notes.classList.toggle('on');}
 else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
 else if(e.key==='Home'){show(0);} else if(e.key==='End'){show(frames.length-1);}
});
addEventListener('resize',fit);fit();
show((parseInt(location.hash.slice(1))||1)-1);
"""


def needs(x):
    return f'<span class="needs">[NEEDS: {E(x)}]</span>'


def win(title, body):
    return f'<div class="win"><div class="bar"><i></i><i></i><i></i><span>{E(title)}</span></div><pre>{body}</pre></div>'


def bars(items, maxv, w=1000, bh=54, gap=18, fmt=lambda v: f"{v:,}", color="#1B4332", hi=None, labw=260):
    """Horizontal bar chart. items: (label, value). hi: set of labels in accent."""
    h = len(items) * (bh + gap)
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Inter">']
    span = w - labw - 150
    for n, (lab, v) in enumerate(items):
        y = n * (bh + gap)
        bw = max(4, span * v / maxv)
        c = "#E9B949" if hi and lab in hi else color
        out.append(f'<text x="{labw-16}" y="{y+bh/2+8}" text-anchor="end" font-size="22" font-weight="700" fill="#1B1B1B">{E(lab)}</text>')
        out.append(f'<rect x="{labw}" y="{y}" width="{bw:.0f}" height="{bh}" rx="6" fill="{c}"/>')
        out.append(f'<text x="{labw+bw+14:.0f}" y="{y+bh/2+9}" font-size="26" font-weight="900" fill="#1B4332" font-family="JetBrains Mono">{E(fmt(v))}</text>')
    out.append("</svg>")
    return "".join(out)


def thumb(name, cls="", lab="", no=""):
    l = f'<div class="lab">{E(lab)}</div>' if lab else ""
    nn = f'<div class="no">#{no}</div>' if no else ""
    return f'<div class="th {cls}"><div class="img c{CM.index(name)}"></div>{nn}{l}</div>'


IMG = {}


# --------------------------------------------------------------------------------------------
# frame builder

def F(time, body, say, upto=99, focus=0, dark=False, src="", cls=""):
    return dict(time=time, body=body, say=say, upto=upto, focus=focus, dark=dark, src=src, cls=cls)


def reveal(rank, name, stat, time, say, src=""):
    body = (f'<div class="reveal"><div class="num"><small>#</small>{rank}</div>'
            f'<div><div class="nm cp">{E(name)}</div><div class="stat">{stat}</div></div></div>')
    return F(time, body, say, upto=rank, focus=rank, dark=True, src=src)


def head(k, h, size=""):
    return f'<div class="k">{E(k)}</div><div class="h {size} cp">{h}</div>'


def ba(before_html, after_html, bt="BEFORE", at="AFTER"):
    return (f'<div class="ba"><div class="side before"><div class="tag">{bt}</div>{before_html}</div>'
            f'<div class="side after"><div class="tag">{at}</div>{after_html}</div></div>')


# --------------------------------------------------------------------------------------------
# BOARD 11: the content system, ranked by count

def board11():
    rail = [(5, "Skills", "73 files"), (4, "Scripts", "25"), (3, "Areas, one map", "11"),
            (2, "Conventions", "9"), (1, "Agents", "4")]
    crit = "Counted down by size. Biggest first, smallest is #1."
    tree = open(os.path.join(REPO, "research/video-knowledge/assets/repo-tree-screen-safe.txt")).read()
    tree = tree.split("\nCounts verified")[0].replace("growthub-os/", "agency-repo/")
    tree_html = E(tree)
    tree_html = re.sub(r"(\[REDACTED\])", r"<u>\1</u>", tree_html)
    tree_html = re.sub(r"(├── |└── |│   )", r"<s>\1</s>", tree_html)

    fr = []
    fr.append(F("0:00-0:12", head("A Claude Code tour, counted down", "My whole Claude Code <span class='hl'>content system</span>"),
        ["Open on this frame. The rail on the left is blurred on purpose. Five layers, and I reveal them one at a time.",
         "Say the working title out loud, then go straight to the result."], upto=99))
    fr.append(F("0:12-0:22", head("The result first", "150+ qualified booked calls in 2026.") +
        '<div class="vis mono" style="font-size:22px;color:#5F6B62">for the agency I run · Calendly export</div>',
        ["Over 150 qualified booked calls for the agency I run this year. That is the Calendly export.",
         "Do not say which channel they came from. The export cannot split them cleanly, and I show why in layer 4.",
         "Then: the thing that produced them is one repo, and I'm going to open the whole thing."],
        src="claims.md: 150 qualified booked calls in 2026, total only, no channel split"))
    fr.append(F("0:22-0:30",
        '<div class="k">Today we go over</div><div class="agenda cp"><div><span>1</span>The bulk</div><div><span>2</span>The rules</div><div><span>3</span>The agents</div></div>',
        ["Five layers, counted down by how many of each there are. Biggest first.",
         "Today we go over three things. The bulk, which is the skills and the scripts. The rules, which is the map and the conventions. And the agents, which is the smallest layer and the reason the rest works.",
         "Promise: by the end you know which part is worth copying, and it is the part with the fewest files."], dark=True))
    fr.append(F("0:30-1:30", '<div class="k" style="margin-bottom:12px">One repo</div>' + win("agency-repo/  (account folders redacted)", tree_html).replace('font:500 19px/1.5', 'font:500 13px/1.28').replace('<pre>', '<pre style="font:500 15.5px/1.32 JetBrains Mono,monospace;padding:14px 22px">'),
        ["Fly through the tree slowly. This is the whole operation in one repo. Eleven top-level areas.",
         "Point at accounts: redacted on purpose, I never show those on camera.",
         "Every number on the rail comes off this tree. 73, 25, 11, 9, 4. That is the ranking: count, nothing else."],
        src="assets/repo-tree-screen-safe.txt · claims.md: one repo, eleven areas"))
    # section 1
    fr.append(reveal(5, "Skills, split by activity", "73 markdown files · 8 folders", "1:30-2:00",
        ["Number five, the biggest pile: 73 skill files across eight folders.",
         "This is what people think the system is. The prompts. It is the least interesting layer, and it ranks last for that reason too."],
        src="claims.md: 73 markdown skill files across eight activity folders"))
    folders = ["content", "research", "ops", "miro", "lead-gen", "youtube", "creative-strategy", "dm-setting"]
    cards = "".join(f'<div class="card"><div class="t mono" style="font-size:24px">{f}/</div></div>' for f in folders)
    fr.append(F("2:00-3:30", head("Section 1 · the bulk", "Eight folders. Zero client folders.", "md") +
        f'<div class="vis grid" style="grid-template-columns:repeat(4,1fr)">{cards}</div>',
        ["Read the eight names. content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting.",
         "Every one is an activity. None of them is a client.",
         "Open skills/content/x-articles on the real repo here if you can: six files in a fixed order turn a transcript into an article, a seventh keeps the other six honest. [NEEDS: the seven-file count is only in the tree asset, claims.md lacks it. Say 'a set of files' if not cleared.]"],
        upto=5, focus=5, src="claims.md: eight activity folders"))
    fr.append(F("3:30-5:00", head("Before / after", "Activity outlives every client.", "md") + '<div class="vis">' + ba(
        '<div class="card" style="margin-bottom:12px"><div class="t mono" style="font-size:22px">clients/brand-a/hooks.md</div></div>'
        '<div class="card" style="margin-bottom:12px"><div class="t mono" style="font-size:22px">clients/brand-b/hooks.md</div></div>'
        '<div class="card redx"><div class="t mono" style="font-size:22px;color:#C0392B">client leaves → folder rots</div></div>',
        '<div class="card on" style="margin-bottom:12px"><div class="t mono" style="font-size:22px">skills/content/hooks.md</div></div>'
        '<div class="card"><div class="t mono" style="font-size:22px">one skill · every client reads it</div></div>') + '</div>',
        ["Worked example, the folder rule. Left: split by client. The same hooks skill gets written inside brand A, then again inside brand B. Brand A leaves and its folder rots.",
         "Right: split by activity. One hooks skill. Every client reads it. It survives every client.",
         "The file names on screen illustrate the split. They are made-up folders. Say that if asked."],
        upto=5, focus=5))
    fr.append(reveal(4, "One script per number", "25 Python scripts", "5:00-5:30",
        ["Number four: 25 scripts.",
         "The rule that produced them: the analysis that produced a number gets saved as a script."],
        src="claims.md: 25 Python scripts, each declaring its own limit"))
    fr.append(F("5:30-7:30", head("Worked example", "The script states its own limit.", "md") +
        '<div class="vis">' + win("ops/tools/  one tool, its opening lines (paraphrased)",
        '<s>"""</s>\n<b>WHAT THIS MEASURES: ALL INBOUND.</b>\n<b>NOT ONE ACCOUNT.</b>\n\n<em>649 of 678</em> Calendly rows sit under one owner.\nUTM field empty on <em>673</em>.\n\nA channel split is not possible from this file.\n<s>"""</s>') + '</div>',
        ["Worked example. One tool was named as if it measured a single account's bookings.",
         "It measures all inbound. 649 of 678 Calendly rows sit under one owner. The UTM field is empty on 673.",
         "So the opening docstring now says it in capitals. Every script in that folder opens with its own limit.",
         "This is also why I said 150 booked calls and no channel: this file is the reason. The window paraphrases the docstring. Open the real tool on screen if you can. [NEEDS: which tool carries the capitals docstring, doc 11 does not name it]"],
        upto=4, focus=4, src="claims.md: 649 of 678 rows one owner, UTM empty on 673"))
    fr.append(F("7:30-8:45", head("Before / after", "Two numbers in a meeting. Then one.", "md") + '<div class="vis">' + ba(
        '<div class="h sm" style="color:#5F6B62">inline calc</div><div class="mono" style="margin-top:14px;font-size:20px;color:#5F6B62">context clears → re-derived → two answers</div>'
        '<div style="margin-top:28px;display:flex;gap:16px"><div class="card redx"><div class="t mono">number A</div></div><div class="card redx"><div class="t mono">number B</div></div></div>',
        '<div class="h sm">saved script</div><div class="mono" style="margin-top:14px;font-size:20px;color:#5F6B62">same input → same number, every time</div>'
        '<div style="margin-top:28px"><div class="card on"><div class="t mono">one number + its limit</div></div></div>') + '</div>',
        ["Before: an inline calculation. It is lost at the next context clear. Somebody re-derives it slightly differently and two numbers disagree in a meeting.",
         "After: the script is saved. Same input, same number, and the limit travels with it."], upto=4, focus=4))
    # section 2
    fr.append(reveal(3, "Route it or it gets rebuilt", "11 areas · one MAP.md", "8:45-9:15",
        ["Section two, the rules. Number three: eleven areas and one map.",
         "The rule that holds it together: work is not finished until it is routed."],
        src="claims.md: one repo, eleven top-level areas, indexed in ops/MAP.md"))
    areas = ["skills/", ".claude/agents/", "ops/", "research/", "accounts/ [REDACTED]", "acquisition-calls/",
             "outbound-calls/", "emails/", "brands/", "recaps/", "future-projects/"]
    rows = "\n".join(f"<em>{a:<26}</em><s>→ entry point listed</s>" for a in areas)
    fr.append(F("9:15-11:00", head("ops/MAP.md", "Unrouted work gets rebuilt.", "md") + '<div class="vis" style="display:flex;gap:30px;align-items:flex-start">' +
        win("ops/MAP.md", rows).replace('font:500 19px', 'font:500 16px') +
        f'<div style="width:330px"><div class="card redx"><div class="t">An agent rebuilt an SOP from scratch.</div><div class="s">time lost</div><div style="margin-top:10px">{needs("45 min, MAP.md, missing from claims.md")}</div></div></div></div>',
        ["Worked example. One day an agent rebuilt the outbound SOP from scratch, because the SOP existed and was not in the map.",
         "The time lost is in MAP.md. It is not cleared yet, so the frame carries a red tag. Leave the time out until it is cleared.",
         "Before: a file exists, and nobody can find it. After: everything that exists has a line in the map, so the next agent reads it instead of rebuilding it."],
        upto=3, focus=3, src="the eleven areas: doc 11 section 1"))
    fr.append(reveal(2, "Four rules carry the weight", "9 conventions", "11:00-11:30",
        ["Number two: nine conventions. Four of them carry the weight."],
        src="claims.md: nine conventions, four of which carry the weight"))
    four = [("Evidence tag", "every claim"), ("Number → script", "every number"), ("Limit stated", "every script"), ("Dated decision", "in the file it governs")]
    cards = "".join(f'<div class="card on"><div class="t">{a}</div><div class="s">{b}</div></div>' for a, b in four)
    fr.append(F("11:30-12:45", head("The load-bearing four", "Four rules. Nine on file.", "md") +
        f'<div class="vis grid" style="grid-template-columns:repeat(2,1fr)">{cards}</div>',
        ["Read the four. Every claim carries an evidence tag. Every number traces to a script and a dataset. Every script declares its own limit. Decisions are dated lines in the file whose behaviour they govern.",
         "The other five exist. These four are the ones I would install first."], upto=2, focus=2))
    fr.append(F("12:45-14:30", head("Worked example", "It felt obviously true. Then measured.", "md") +
        '<div class="vis">' + bars([("worked example", 60000), ("winning section", 264000)], 264000, hi={"winning section"}) + '</div>',
        ["Worked example, the reason for the tags. A skill asserted that the worked example was the section that converts.",
         "Measuring it returned 60,000 against 264,000. The opposite direction.",
         "Before: the rule felt obviously true, so it went in untagged. After: it carries a tag, and the measurement overruled the feeling."],
        upto=2, focus=2, src="claims.md: worked example 60,000 against the winning section's 264,000"))
    fr.append(F("14:30-15:30", head("The three tags", "An untagged claim is an assertion.", "md") + '<div class="vis">' + win("any skill file",
        "73 skill files, 8 folders.          <b>[measured]</b>\nBoards went out unrecordable.       <em>[observed]</em>\nBroad topics drive subscribers.      <u>[assumed]</u>") + '</div>',
        ["Three tags. Measured: a script produced it. Observed: someone saw it and dated it. Assumed: an inference, flagged as one.",
         "The three lines on screen are tag examples. Read the tags out loud. The lines are only examples."], upto=2, focus=2))
    # section 3
    fr.append(reveal(1, "Every agent is a scar", "4 agents", "15:30-16:00",
        ["Section three. Number one, the smallest layer: four agents.",
         "And this is the part worth copying. Every one of the four exists because something was missed."],
        src="claims.md: four agents, all defensive"))
    fr.append(F("16:00-17:00", head("Skill vs agent", "An agent runs without being asked.", "md") + '<div class="vis">' + ba(
        '<div class="h sm" style="color:#5F6B62">skill</div><div class="mono" style="margin-top:16px;font-size:22px;color:#5F6B62">you → call it → it runs</div>',
        '<div class="h sm">agent</div><div class="mono" style="margin-top:16px;font-size:22px">something happens → it runs</div>', "SKILL", "AGENT") + '</div>',
        ["A skill runs when I call it. An agent runs without being asked.",
         "Four of them. I go through each with the incident behind it."], upto=1, focus=1))
    fr.append(F("17:00-18:30", head("performance-loop", "Down 64%. Nobody noticed for two months.", "sm") +
        '<div class="vis">' + bars([("June", 100), ("August", 36)], 100, fmt=lambda v: f"{v}", hi={"August"}) +
        '<div class="mono" style="margin-top:8px;font-size:16px;color:#5F6B62">monthly impressions, indexed June = 100</div></div>',
        ["Agent one, performance-loop. Monthly impressions fell 64% between June and August 2026, and nobody noticed for two months.",
         "The chart is indexed: June at 100, August at 36. That is the 64% and nothing else.",
         "Before: a drop is found two months late. After: the agent reads it without being asked. [NEEDS: the agent's run cadence, if Mauro wants to say it]"],
        upto=1, focus=1, src="claims.md: monthly impressions fell 64% June to August 2026, unnoticed for two months"))
    bub = "".join(f'<div style="background:#fff;border:2px solid #D8CFBB;border-radius:14px;padding:16px 20px;margin-bottom:12px;width:{w}px"><div style="height:16px;background:#CFC6B2;border-radius:6px;filter:blur(3px);width:{w-80}px"></div></div>' for w in (520, 420))
    fr.append(F("18:30-19:30", head("signal-sweep", "The one ask sat in a group DM.", "md") +
        f'<div class="vis" style="display:flex;gap:40px;align-items:center"><div>{bub}</div><div class="card on" style="width:360px"><div class="t">two messages</div><div class="s">missed in a catch-up</div></div></div>',
        ["Agent two, signal-sweep. A catch-up missed a two-message group DM that held the one number that mattered, and showed an auto-generated queue as if it were the priority list.",
         "The bubbles are blurred on purpose. Do not name who sent it, and do not say the number in it.",
         "After: signal-sweep reads every channel and pulls the asks out."], upto=1, focus=1))
    sq = "".join(f'<div style="height:74px;border-radius:8px;display:flex;align-items:center;justify-content:center;font:800 22px JetBrains Mono;{"background:#C0392B;color:#fff" if n < 4 else "background:#fff;border:3px solid #1B4332;color:#1B4332"}">{n+1}</div>' for n in range(15))
    fr.append(F("19:30-20:30", head("board-qa", "Can this be read to camera?", "md") +
        f'<div class="vis" style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;max-width:820px">{sq}</div>'
        '<div class="mono" style="margin-top:14px;font-size:16px;color:#5F6B62">15 checks · first 4 are blockers, the run stops there</div>',
        ["Agent three, board-qa. Boards were going out full and unrecordable. It answers one question through fifteen checks: can this be read to camera without stopping.",
         "The first four are blockers. If one fails, the run stops there."],
        upto=1, focus=1, src="claims.md: the board gate is fifteen checks; the first four are blockers"))
    fr.append(F("20:30-21:15", head("youtube-lead-magnet", "Run the existing skill. Invent nothing.", "md") +
        '<div class="vis" style="display:flex;gap:16px;align-items:center;font:800 26px Inter;color:#1B4332">'
        '<div class="card">video</div>→<div class="card on">existing skill</div>→<div class="card">post · DM · config</div></div>',
        ["Agent four, youtube-lead-magnet. It exists because of packaging drift. Its first instruction is to run the existing skill and never invent rules.",
         "Four agents. Four incidents."], upto=1, focus=1))
    fr.append(F("21:15-22:00", head("The gap", "None of the four books a call.", "md") +
        '<div class="vis" style="display:flex;gap:14px">' + "".join(f'<div class="card"><div class="t mono" style="font-size:20px">{a}</div><div class="s">defensive</div></div>' for a in ["performance-loop", "signal-sweep", "board-qa", "youtube-lead-magnet"]) + '</div>',
        ["Full rail now. Read it bottom to top: four agents is the smallest number and the most important layer. The 73 prompts are the least interesting part.",
         "What it does not do: every agent is defensive. Nothing in the repo reaches out to a human. That gap is the next video."],
        upto=1, src="claims.md: four agents, all defensive, none reaches out to a human"))
    fr.append(F("22:00-22:40", '<div class="cta"><div class="k">If you run an agency</div><div class="h cp">Link in the description.</div><div class="pill cp">Agency Booked Calls</div></div>',
        ["If you run an established agency and you want this installed for your own inbound, the link is in the description. It is called Agency Booked Calls.",
         "Everyone else: comment which layer you would build first."], upto=1, dark=True))
    return dict(doc="11", slug="11-claude-code-content-system", title="My whole Claude Code content system",
                rail=rail, crit=crit, rail_needs="", frames=fr, minutes=23)


# --------------------------------------------------------------------------------------------
# BOARD 07: reverse-engineer a channel, ranked by how many of the top 10 use it

T = [  # title, views (as scraped, approx)
    ("You'll NEVER Doomscroll Again After Watching This", "638K"),
    ("Why 99.6% Of Men Will NEVER Become Millionaires", "52K"),
    ("How to work & focus for 12 hours a day like a millionaire CEO", "43K"),
    ("How To Make 10 Years Worth Of Progress In 1 Year", "39K"),
    ("I've Coached 50,000 Men. You All Have The Same Problem.", "31K"),
    ("Give me 13 mins, I'll fix your addiction", "31K"),
    ("So you want to be a millionaire? It's all about focus and speed", "30K"),
    ("\"Dopamine Fasting\" is the Easiest Path To Millionaire in 2026", "27K"),
    ("I Ranked Every Online Business Model So You Don't Have To", "24K"),
    ("You'll NEVER Be Lazy Again After Watching This", "23K"),
]


def titles_list(marks, show=None):
    out = []
    for n, (t, v) in enumerate(T):
        if show is not None and n not in show:
            continue
        tt = E(t)
        on = n in marks
        if on:
            for m in marks[n]:
                tt = tt.replace(E(m), f"<mark>{E(m)}</mark>", 1)
        out.append(f'<div class="tt {"" if on else "dim"}">#{n+1} · {tt}</div>')
    return '<div class="grid" style="gap:10px">' + "".join(out) + "</div>"


def board07():
    rail = [(7, "The board is the thumbnail", "3 of 10"), (6, "A time box", "3 of 10"),
            (5, "NEVER ... again", "3 of 10"), (4, "An identity", "5 of 10"),
            (3, "No typed text", "5 of 10"), (2, "One loaded prop", "7 of 10"), (1, "His face", "9 of 10")]
    crit = "Ranked by how many of his top 10 use it. Ties: the bigger best video wins."
    rn = "counts are my read of the dig, missing from claims.md"
    fr = []
    wall = '<div class="thumbs" style="grid-template-columns:repeat(5,1fr)">' + "".join(thumb(c, "dim") for c in CM) + "</div>"
    fr.append(F("0:00-0:10", head("Channel teardown", "I reverse-engineered a big channel in <span class='hl'>one afternoon</span>", "md") + f'<div class="vis" style="opacity:.6">{wall}</div>',
        ["Open on this frame. The rail on the left is blurred: seven moves, counted down.",
         "Say the title. Do not say a subscriber count unless it is re-checked on the day. [NEEDS: subscriber count, the dig says about 310k as scraped 2026-07-16]"]))
    fr.append(F("0:10-0:20", head("The result first", "Ten thumbnails. Seven moves. One afternoon.", "md") +
        '<div class="vis thumbs" style="grid-template-columns:repeat(5,1fr)">' + "".join(thumb(c) for c in CM) + "</div>",
        ["The result: one afternoon of structured looking at one big channel. Out of it came the title formula, the thumbnail formula, and ten titles I can shoot.",
         "These are his top ten videos by views. Charlie Morgan, agency, money and mindset. [NEEDS: Mauro's sign-off to name him on camera]"],
        src="research/charlie-morgan/thumbs/ · saved 2026-07-16"))
    fr.append(F("0:20-0:30", '<div class="k">Today we go over</div><div class="agenda cp"><div><span>1</span>The 3-in-10 moves</div><div><span>2</span>The majority moves</div><div><span>3</span>The #1 move</div></div>',
        ["Today we go over three groups. The moves he uses in three of ten videos. The moves he uses in most of them. And the number one move, which is in nearly every thumbnail.",
         "For each one I show the proof on his channel, then I rewrite it for mine."], dark=True))
    fr.append(F("0:30-1:30", head("The ranking", "Ranked by how many of his top 10.", "md") +
        f'<div class="vis card" style="max-width:900px"><div class="t">Tie? The move whose best video has more views ranks higher.</div><div style="margin-top:14px">{needs(rn)}</div></div>',
        ["How I rank. One criterion: in how many of his top ten videos does the move appear. I counted it off the thumbnails and the titles you see here.",
         "Ties are broken by one thing: which move sits on the bigger video.",
         "These counts are my own read. They carry a red tag until Mauro signs them into claims.md."]))
    views = [638, 52, 43, 39, 31, 31, 30, 27, 24, 23]
    fr.append(F("1:30-3:00", head("Sort by popular", "One video carries the channel.", "md") +
        '<div class="vis">' + bars([(f"#{n+1}", v) for n, v in enumerate(views)], 638, bh=34, gap=10, fmt=lambda v: f"{v}K", hi={"#1"}, labw=80) +
        f'<div style="margin-top:6px">{needs("view counts scraped 2026-07-16, approximate")}</div></div>',
        ["Sort by popular. One video sits far above everything else, then a long drop. The working catalogue sits an order of magnitude below the outlier.",
         "Say 'about' on every view count. They are scraped and approximate, and the feed skews to the last one to two years."],
        src="charlie-morgan-dig.md, top 10 table"))
    # section 1
    fr.append(reveal(7, "The board is the thumbnail", "3 of 10 · best: #4", "3:00-3:20",
        ["Number seven. Three of his top ten are framework videos, and the thumbnail is the board itself."]))
    fr.append(F("3:20-5:00", head("#4 · #6 · #7", "Three framework videos. Three boards.", "md") +
        '<div class="vis thumbs" style="grid-template-columns:repeat(3,1fr)">' + thumb(CM[3], "ring", "whiteboard", 4) + thumb(CM[5], "ring", "hand-drawn funnel", 6) + thumb(CM[6], "ring", "live Miro board", 7) + "</div>",
        ["Number four: a hand-drawn whiteboard. Number six: a hand-drawn funnel with a facecam. Number seven: an actual Miro board, a winding road from a now state to a future state.",
         "This is the format I record in. He validated the board system before I built it."], upto=7, focus=7))
    fr.append(F("5:00-6:00", head("Every system gets a name", "Name it. Draw it. Narrate it.", "md") +
        '<div class="vis grid" style="grid-template-columns:repeat(3,1fr)">' + "".join(f'<div class="card on"><div class="t">{n}</div></div>' for n in ["Time Compression Theory", "The Downfall Plan", "Now State → Future State"]) + "</div>",
        ["Named-framework packaging. Time Compression Theory. The Downfall Plan. Now State to Future State.",
         "Every system gets a proprietary name and a diagram. It costs nothing to adopt."], upto=7, focus=7))
    fr.append(F("6:00-7:00", head("Before / after", "Hook video: a prop. Framework video: a board.", "sm") + '<div class="vis">' + ba(
        '<div class="thumbs">' + thumb(CM[2], "", "broad hook video") + '</div>',
        '<div class="thumbs">' + thumb(CM[6], "", "framework video") + '</div>', "HOOK VIDEO", "FRAMEWORK VIDEO") + '</div>',
        ["The split maps cleanly onto my system. The cinematic photo with one prop goes on the broad hook video. The board goes on the framework video.",
         "So I stopped designing a separate thumbnail for framework videos. The board frame is the thumbnail candidate."], upto=7, focus=7))
    fr.append(reveal(6, "A time box in the title", "3 of 10 · best: #3", "7:00-7:20",
        ["Number six. A time box: a number of minutes, hours or years in the title."]))
    fr.append(F("7:20-8:30", head("Time boxes", "A clock in the title.", "md") + '<div class="vis">' +
        titles_list({2: ["12 hours a day"], 3: ["10 Years", "1 Year"], 5: ["13 mins"]}, show=[2, 3, 5]) + "</div>",
        ["Twelve hours a day. Ten years in one year. Give me thirteen minutes.",
         "A time box makes the result feel close. It ties with NEVER and the board at three, and it ranks here because its best video is number three."],
        upto=6, focus=6))
    fr.append(reveal(5, "NEVER ... again after watching this", "3 of 10 · best: #1", "8:30-8:50",
        ["Number five. The absolute plus a curiosity gap. It ranks above the time box because it sits on his biggest video."]))
    fr.append(F("8:50-10:30", head("Worked example", "His shape. My topic.", "md") + '<div class="vis">' +
        titles_list({0: ["NEVER", "Again After Watching This"], 1: ["NEVER"], 9: ["NEVER", "Again After Watching This"]}, show=[0, 1, 9]) +
        '<div class="tt" style="margin-top:22px;border-left-color:#E9B949;font-size:30px">→ You\'ll never post cringe again after watching this</div></div>',
        ["Three titles use NEVER. Two use the full shape: you'll never X again after watching this.",
         "Worked example. I take the shape and keep my topic: you'll never post cringe again after watching this. That title is on my list from the same afternoon.",
         "Before: a title I would have written from taste. After: a shape that already carried his biggest video."], upto=5, focus=5))
    # section 2
    fr.append(reveal(4, "An identity in the title", "5 of 10 · best: #2", "10:30-10:50",
        ["Section two, the majority moves. Number four: an identity anchor. Men. Millionaire. Millionaire CEO."]))
    fr.append(F("10:50-12:00", head("Identity anchors", "He names who the video is for.", "md") + '<div class="vis">' +
        titles_list({1: ["Men", "Millionaires"], 2: ["millionaire CEO"], 4: ["Men"], 6: ["millionaire"], 7: ["Millionaire"]}, show=[1, 2, 4, 6, 7]) + "</div>",
        ["Five of ten name an identity. The viewer sees himself in the title before he sees the topic.",
         "It ties with no typed text at five, and ranks below it because its best video is number two."], upto=4, focus=4))
    fr.append(F("12:00-13:00", head("Before / after", "Add who it is for.", "md") + '<div class="vis">' + ba(
        '<div class="tt" style="font-size:30px">My Claude Code content system</div>',
        '<div class="tt" style="font-size:30px;border-left-color:#E9B949">The Claude Code content system for <mark>agency owners</mark></div>') + '</div>',
        ["Worked example on my own flagship title. Before: my Claude Code content system. After: the same title with the identity in it, agency owners.",
         "For my channel the identity is the ICP. Established agency owners. Never beginners."], upto=4, focus=4))
    fr.append(reveal(3, "No typed text on it", "5 of 10 · best: #1", "13:00-13:20",
        ["Number three. Half his thumbnails carry no text at all. The image carries it and the title does the words."]))
    nontext = {0, 1, 2, 4, 9}
    fr.append(F("13:20-14:45", head("No text", "The image carries it. The title talks.", "md") +
        '<div class="vis thumbs" style="grid-template-columns:repeat(5,1fr)">' + "".join(thumb(c, "ring" if n in nontext else "dim", "", n + 1) for n, c in enumerate(CM)) + "</div>",
        ["Lit up: the five with no text at all. Dimmed: the five with text, and look what that text is. A handwritten sign, a hand-drawn diagram, a Miro board, tier letters.",
         "When text appears it is handwritten or part of the diagram. Never a typed headline across the top.",
         "This is the fix for my v1 thumbnails: too much text."], upto=3, focus=3))
    fr.append(reveal(2, "One loaded prop that is the promise", "7 of 10 · best: #1", "14:45-15:05",
        ["Number two. One loaded prop, and the prop is the promise."]))
    props = {0: "EEG cap + phone", 1: "empty mansion", 2: "cash on the desk", 4: "tally wall", 7: "handwritten sign", 8: "tier-list rail", 9: "EEG cap + phone"}
    fr.append(F("15:05-16:45", head("The prop", "The prop is the promise.", "md") +
        '<div class="vis thumbs" style="grid-template-columns:repeat(4,1fr)">' + "".join(thumb(CM[n], "", p, n + 1) for n, p in props.items()) + "</div>",
        ["Seven of ten. The EEG cap and the phone is the science of your brain. The empty mansion is hollow wealth. Cash on the desk is the grind. The tally wall is discipline. The tier-list rail is authority.",
         "One prop per thumbnail. The viewer reads the promise before he reads a word."], upto=2, focus=2))
    fr.append(F("16:45-17:45", head("Before / after", "One prop beats four lines.", "md") + '<div class="vis">' + ba(
        '<div style="background:#0E2418;aspect-ratio:16/9;border-radius:8px;padding:18px;color:#fff;font:900 30px Inter;line-height:1.1">HOW I BUILT<br>MY CLAUDE CODE<br>CONTENT SYSTEM<br>(FULL WALKTHROUGH)</div>',
        '<div style="background:#0E2418;aspect-ratio:16/9;border-radius:8px;padding:18px;position:relative">'
        + win("agency-repo/", "<em>├── skills/</em>     73\n<em>├── ops/tools/</em>  25\n<em>└── agents/</em>      4").replace('font:500 19px', 'font:500 15px').replace('class="win"', 'class="win" style="width:62%"')
        + '</div>') + '</div>',
        ["Worked example. Before: my v1 style, four lines of typed text. After: one prop, the repo tree. The tree is the promise: the whole system, open.",
         "My face goes on the right in the real thumbnail. The thumbs file has the slot."], upto=2, focus=2))
    # section 3
    fr.append(reveal(1, "His face. Serious. Almost never smiling.", "9 of 10 · best: #1", "17:45-18:05",
        ["Section three. Number one: his face, in nine of ten. Serious, intense, somber. Almost never smiling."]))
    fr.append(F("18:05-19:30", head("Count them", "Nine readable faces out of ten.", "md") +
        '<div class="vis thumbs" style="grid-template-columns:repeat(5,1fr)">' + "".join(thumb(c, "dim" if n == 1 else "ring", "", n + 1) for n, c in enumerate(CM)) + "</div>",
        ["Count them with me. His face is readable in nine.",
         "Number two is the honest edge case: he is in the frame, small, on the floor of the empty mansion. He is a small figure there, with no readable face. That is why it is nine and not ten.",
         "Nine of ten, high contrast against the background, filmic grade."], upto=1, focus=1))
    crops = "".join(f'<div class="c{n}" style="aspect-ratio:3/4;border-radius:10px;background-position:{pos};background-size:{z};background-repeat:no-repeat"></div>' for n, pos, z in
                    [(0, "70% 30%", "260%"), (2, "52% 25%", "300%"), (4, "8% 40%", "240%"), (8, "28% 35%", "230%"), (9, "40% 45%", "220%")])
    fr.append(F("19:30-20:30", head("The expression", "Serious. Intense. Not smiling.", "md") +
        f'<div class="vis" style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px">{crops}</div>',
        ["Five crops from his own thumbnails. Look at the mouth. No grin anywhere.",
         "For me that means: no thumbs-up, no shocked face. A serious operator looking at the thing."], upto=1, focus=1))
    fr.append(F("20:30-21:15", head("He reuses winners", "Same motif. Number one and number ten.", "sm") +
        '<div class="vis thumbs" style="grid-template-columns:1fr 1fr">' + thumb(CM[0], "ring", "", 1) + thumb(CM[9], "ring", "", 10) + "</div>",
        ["The brain-cap and phone motif. Number one, and again at number ten.",
         "He reuses his own winner. I can reuse mine the same way once I have one."], upto=1, focus=1))
    fr.append(F("21:15-22:15", head("Turn it into titles, live", "His shapes. My topics.", "md") + '<div class="vis grid" style="gap:12px">' +
        "".join(f'<div class="tt"><span style="color:#5F6B62">{E(a)}</span><br>→ <b>{E(b)}</b></div>' for a, b in [
            ("You'll NEVER Doomscroll Again After Watching This", "You'll never post cringe again after watching this"),
            ("Give me 13 mins, I'll fix your addiction", "Give me 10 minutes, I'll fix your agency's inbound"),
            ("I Ranked Every Online Business Model So You Don't Have To", "I ranked every AI tool for agency content so you don't have to")]) + "</div>",
        ["Three of the ten titles I wrote off this teardown. Read his, then mine. Each one keeps his shape and swaps in my topic.",
         "The other seven are in the dig. Point at the description if they are linked there."],
        upto=1, src="charlie-morgan-dig.md, 10 titles for Mauro"))
    fr.append(F("22:15-22:50", head("The limits, said plainly", "Scraped. Approximate. No transcripts.", "md") +
        '<div class="vis grid" style="grid-template-columns:repeat(3,1fr)">' + "".join(f'<div class="card"><div class="t">{a}</div><div class="s">{b}</div></div>' for a, b in [
            ("Views", "as scraped, approximate"), ("Feed", "skews to the last 1-2 years"), ("Transcripts", "blocked, unread")]) +
        f'</div><div style="margin-top:16px">{needs("the ten transcripts, still blocked")}</div>',
        ["The method's limits. Views are as-scraped. The popular feed skews recent, so an all-time cut might surface older videos. I never got the transcripts, so this is packaging only: titles and thumbnails, nothing about what he says.",
         "And copying the formula does not promise his result. I do not know his revenue or his students, and I am not saying anything about them."], upto=1))
    fr.append(F("22:50-23:20", '<div class="cta"><div class="k">If you run an agency</div><div class="h cp">Link in the description.</div><div class="pill cp">Agency Booked Calls</div></div>',
        ["If you run an established agency and you want a content system that books calls, the link is in the description. Agency Booked Calls.",
         "Everyone else: comment the channel you want me to tear down next."], upto=1, dark=True))
    return dict(doc="07", slug="07-reverse-engineer-channel", title="I reverse-engineered a big channel in one afternoon",
                rail=rail, crit=crit, rail_needs=rn, frames=fr, minutes=23)


# --------------------------------------------------------------------------------------------
# BOARD 04: outlier swipe corpus, ranked by how many captures stand behind each lesson

def dots(n, filled, color="#1B4332", on="#E9B949", size=34, cols=None):
    cols = cols or n
    return (f'<div style="display:grid;grid-template-columns:repeat({cols},{size}px);gap:10px">' +
            "".join(f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:{on if k < filled else "transparent"};border:3px solid {color}"></div>' for k in range(n)) + "</div>")


def board04():
    rail = [(5, "No raw screenshot covers", "n = 5"), (4, "The logo carries it", "n = 6"),
            (3, "Link + view count", "n = 7"), (2, "Reach rules only", "n = 41"), (1, "Everything here won", "n = 41")]
    crit = "Ranked by how many captures stand behind it. Weakest evidence first."
    fr = []
    fr.append(F("0:00-0:10", head("Swipe files, counted down", "You'll never trust your <span class='hl'>swipe file</span> again"),
        ["Open on this frame. Rail blurred: five lessons from saving outlier X articles.",
         "Say the title, then the result."]))
    fr.append(F("0:10-0:20", head("The result first", "41 captures. One conclusion retracted.", "md") +
        '<div class="vis">' + dots(41, 41, cols=14, size=30) + '</div>',
        ["41 article captures sit behind the agency's article skills. Each one a winner.",
         "And one conclusion drawn from them had to be retracted. That retraction is the whole video."],
        src="claims.md: 41 real captures, the corpus behind the article skills of the agency I run"))
    fr.append(F("0:20-0:30", '<div class="k">Today we go over</div><div class="agenda cp"><div><span>1</span>The capture</div><div><span>2</span>Reach rules</div><div><span>3</span>The winners trap</div></div>',
        ["Today we go over three things. How a capture is saved. Why every rule out of it is a reach rule. And the trap: everything in a swipe file already won.",
         "Ranked by sample size. The lessons with the least evidence come first, so the countdown climbs toward the ones you can trust."], dark=True))
    fr.append(F("0:30-1:15", head("The ranking", "Ranked by how many captures stand behind it.", "sm") +
        '<div class="vis">' + bars([("#5", 5), ("#4", 6), ("#3", 7), ("#2", 41), ("#1", 41)], 41, bh=40, gap=12, fmt=lambda v: f"n = {v}", labw=80) + '<div class="mono" style="margin-top:6px;font-size:17px;color:#5F6B62">#5-#3: my own corpus · #2-#1: the agency I run</div></div>',
        ["The one criterion: how many captures each lesson rests on. Five, six, seven, then forty-one twice.",
         "Two corpora. #5 to #3 come from my own corpus, seven saved so far. #2 and #1 come from the 41-capture corpus behind the article skills of the agency I run.",
         "#2 and #1 tie at 41. #1 ranks higher because it kills more conclusions. Say that tiebreak out loud."], src="claims.md: n=5, n=6, seven captures (my corpus) · 41 captures (the agency I run)"))
    # section 1
    fr.append(reveal(5, "No saved cover is a raw screenshot", "n = 5 · a hypothesis", "1:15-1:35",
        ["Section one, the capture. Number five, and the weakest: none of the five saved covers is a raw screenshot."],
        src="claims.md: n=5, stated as a hypothesis"))
    covers = [("@denk_tweets", "illustrated visual joke", 1), ("@coreyganim", "anime-style vista", 1),
              ("@knoxtwts", "vintage engraving", 1), ("@Aidanb2b", "monochrome engraving", 1),
              ("@Ecombos_Ai", "screenshots in a designed composite", 0)]
    rows = "".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td style="font-weight:900;color:{"#1B4332" if c else "#B07D00"}">{"illustration" if c else "composite"}</td></tr>' for a, b, c in covers)
    fr.append(F("1:35-3:00", head("My own corpus, five covers", "Four illustrations. One composite.", "md") +
        '<div class="vis"><table style="width:100%;border-collapse:collapse;background:#fff;border:3px solid #1B4332;font-size:24px">'
        '<tr style="background:#1B4332;color:#fff;font:800 15px JetBrains Mono;letter-spacing:.12em"><td style="padding:12px 18px">AUTHOR</td><td>COVER</td><td>TYPE</td></tr>'
        + rows.replace("<td", '<td style="padding:13px 18px;border-top:2px solid #D8CFBB"', ).replace('style="padding:13px 18px;border-top:2px solid #D8CFBB" class="mono"', 'class="mono" style="padding:13px 18px;border-top:2px solid #D8CFBB;font-size:20px"').replace('style="padding:13px 18px;border-top:2px solid #D8CFBB" style="', 'style="padding:13px 18px;border-top:2px solid #D8CFBB;') +
        '</table><div class="mono" style="margin-top:14px;font-size:18px;color:#5F6B62">n = 5 · zero raw screenshots · still a hypothesis</div></div>',
        ["My own corpus, five covers with a description. Four are illustrations. One arranges real screenshots into a designed composite. None is a plain screenshot.",
         "Five is a note. Say it like that.",
         "The authors are public X accounts. None is a client. Mauro signs off on naming them before publish."],
        upto=5, focus=5, src="claims.md: n=5, four illustrations, one composite · research/outlier-x-articles/README.md"))
    fr.append(reveal(4, "The logo carries the argument", "n = 6", "3:00-3:20",
        ["Number four. Three of six covers borrow a logo you already recognise."]))
    fr.append(F("3:20-4:45", head("Three of six", "The logo carries the meaning.", "md") +
        '<div class="vis grid" style="grid-template-columns:repeat(3,1fr)">' + "".join(f'<div class="card on"><div class="t">{a}</div><div class="s">{b}</div></div>' for a, b in [
            ("Claude asterisk", "@Ecombos_Ai · placed in frame"), ("LinkedIn mark", "@Aidanb2b · the lighthouse lamp"), ("OpenAI mark", "@immortalhowwl · the heist mask")]) + "</div>",
        ["Three of six borrow a recognisable logo. The Claude asterisk. The LinkedIn mark drawn as a lighthouse lamp. The OpenAI mark as a movie mask.",
         "The strongest ones make the logo carry the argument, instead of just sitting in the frame.",
         "n = 6, one account's worth of covers each. Still a note."], upto=4, focus=4, src="claims.md: n=6"))
    fr.append(reveal(3, "Save the link and the view count", "n = 7", "4:45-5:05",
        ["Number three. Seven captures in, and only one had a view count."]))
    comps = [("title screenshot", "from the feed"), ("cover image", "right-click copied"), ("full text", "verbatim"), ("link", "non-optional"), ("view count", "non-optional")]
    fr.append(F("5:05-6:45", head("Worked example · one capture", "Five fields. Two are non-optional.", "md") +
        '<div class="vis grid" style="grid-template-columns:repeat(5,1fr)">' + "".join(f'<div class="card {"on" if "non" in b else ""}"><div class="t" style="font-size:23px">{a}</div><div class="s">{b}</div></div>' for a, b in comps) + "</div>",
        ["Worked example: what one capture holds. The title screenshot, taken from the feed and not inside the article. The cover. The full text. The link. The view count.",
         "A plain-screenshot cover is already in the title shot. A designed cover gets right-clicked and copied.",
         "The link and the view count are the two non-optional fields. The link lets you re-fetch everything else."],
        upto=3, focus=3, src="claims.md: five components per article"))
    fr.append(F("6:45-8:15", head("Before / after", "One of seven had a view count.", "md") + '<div class="vis">' + ba(
        dots(7, 1, size=46) + '<div class="mono" style="margin-top:18px;font-size:20px;color:#5F6B62">1 of 7 with views · 170,000</div><div class="mono" style="margin-top:8px;font-size:20px;color:#5F6B62">links missing on nearly all</div>',
        dots(7, 7, size=46) + '<div class="mono" style="margin-top:18px;font-size:20px">link + views on every row</div><div class="mono" style="margin-top:8px;font-size:20px">author tagged on every row</div>') + '</div>',
        ["Before: the first seven captures. One had a recorded view count, 170,000. Links were missing on nearly all of them.",
         "A capture with no view count cannot be scored. Intake divides a post's impressions by the account's own median, so no number means no score.",
         "After: link and views on every row, and the author tagged, because a pattern has to hold per author before it is real."],
        upto=3, focus=3, src="claims.md: only one of seven had a view count, 170,000"))
    fr.append(F("8:15-9:15", head("The capture rule", "Save only. Build nothing until 50.", "md") +
        '<div class="vis">' + dots(50, 7, cols=25, size=28) + '<div class="mono" style="margin-top:14px;font-size:18px;color:#5F6B62">7 saved of a ~50 target</div></div>',
        ["The rule: save only, build nothing. No skill, no template, until roughly fifty are in.",
         "An observation across seven is a note. The same observation across fifty, held per author, is a rule.",
         "Capture only, no judging. Judging at capture time turns a swipe file into a folder of things you already agreed with."],
        upto=3, focus=3, src="claims.md: save only until roughly 50; 7 of a ~50 target"))
    # section 2
    fr.append(reveal(2, "Every rule here is a reach rule", "n = 41", "9:15-9:35",
        ["Section two. Number two: all 41 captures carry impressions. None of them carries a booking. So every rule out of them is a reach rule."]))
    fr.append(F("9:35-11:00", head("What the 41 carry", "Impressions. No bookings.", "md") + '<div class="vis" style="display:flex;gap:60px">' +
        '<div><div class="mono" style="font-size:18px;margin-bottom:10px;color:#1B4332;font-weight:800">IMPRESSIONS</div>' + dots(41, 41, cols=7, size=26) + '</div>' +
        '<div><div class="mono" style="font-size:18px;margin-bottom:10px;color:#1B4332;font-weight:800">BOOKED CALLS</div>' + dots(41, 0, cols=7, size=26, color="#CBBFA6") + '</div></div>',
        ["Left column: impressions, on every capture. Right column: booked calls, on none.",
         "That makes the corpus the right evidence for something written to travel, and the wrong evidence for something written to book a call."],
        upto=2, focus=2, src="doc 04: none of the 41 carry call data [measured] · the agency I run"))
    fr.append(F("11:00-12:45", head("Worked example", "A length rule. Good for reach.", "md") +
        '<div class="vis">' + bars([("1,800-3,000 words", 225900), ("900-1,800 words", 73300)], 225900, hi={"1,800-3,000 words"}, labw=300) +
        '<div class="mono" style="margin-top:6px;font-size:16px;color:#5F6B62">median impressions · 41 captures</div></div>',
        ["Worked example. The 1,800 to 3,000 word band medians 225,900 impressions. The 900 to 1,800 band medians 73,300.",
         "That is a reach rule. It tells you how long to write when you want the piece to travel. It tells you nothing about which length books a call."],
        upto=2, focus=2, src="claims.md: band medians 225,900 and 73,300, reach, 41 captures · the agency I run"))
    fr.append(F("12:45-14:00", head("Before / after", "Tag the rule where you use it.", "md") + '<div class="vis">' + ba(
        '<div class="tt">Write long. Long wins.</div><div class="mono" style="margin-top:16px;font-size:20px;color:#5F6B62">applied to every piece</div>',
        '<div class="tt" style="border-left-color:#E9B949">Write long. <mark>[reach]</mark></div><div class="mono" style="margin-top:16px;font-size:20px">applied where the goal is travel</div>') + '</div>',
        ["Before: the rule is just 'write long', and it gets applied to the article meant to book calls too.",
         "After: it carries a reach tag at the point of use. That tag stops the two lanes contaminating each other."], upto=2, focus=2))
    # section 3
    fr.append(reveal(1, "Everything in here already won", "n = 41 · tie, kills more", "14:00-14:20",
        ["Section three, the deepest one. Number one: everything in a swipe file already won.",
         "Ties with number two at 41. It ranks first because it kills more conclusions."]))
    # distribution svg
    pts = " ".join(f"{x},{360 - 300 * (2.71828 ** (-((x - 360) / 230) ** 2)):.0f}" for x in range(0, 1001, 20))
    dist = (f'<svg width="1000" height="400" viewBox="0 0 1000 400"><polyline points="{pts}" fill="none" stroke="#1B4332" stroke-width="5"/>'
            '<rect x="700" y="0" width="300" height="362" fill="#E9B949" opacity=".35"/>'
            '<line x1="0" y1="362" x2="1000" y2="362" stroke="#1B4332" stroke-width="3"/>'
            '<text x="850" y="40" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="22" fill="#1B4332">CAPTURED</text>'
            '<text x="300" y="395" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="20" fill="#5F6B62">never collected</text>'
            '<text x="1000" y="395" text-anchor="end" font-family="JetBrains Mono" font-weight="700" font-size="20" fill="#5F6B62">impressions →</text></svg>')
    fr.append(F("14:20-15:45", head("The shape of a swipe file", "No bottom. Only the tail.", "md") + f'<div class="vis">{dist}</div>',
        ["Nobody browsed a feed and saved a random article. Every capture was chosen because it performed.",
         "So the lowest capture is the tail of a winners set. It never failed. There is no bottom.",
         "The curve is a diagram of the idea. Nobody measured it. Say that."], upto=1, focus=1))
    fr.append(F("15:45-17:15", head("Medians of outliers", "Read the median the right way.", "md") + '<div class="vis">' + ba(
        '<div class="tt" style="font-size:28px">A 2,000-word article gets 225,900.</div>',
        '<div class="tt" style="font-size:28px;border-left-color:#E9B949">Among winners, the long ones sat at 225,900.</div>', "THE WRONG READ", "THE RIGHT READ") + '</div>',
        ["Every median is a median of outliers. The 225,900 does not mean a long article produces 225,900.",
         "It means that among articles that already worked, the long ones sat there. Say it with the caveat in the same breath, every time."],
        upto=1, focus=1, src="claims.md: 1,800-3,000 band median 225,900 · the agency I run"))
    fr.append(F("17:15-18:30", head("Top vs bottom", "Comparing great to good.", "md") +
        '<div class="vis">' + bars([("top of the set", 10), ("bottom of the set", 7)], 10, fmt=lambda v: "winner", labw=300) + "</div>",
        ["Comparing the top of the set to the bottom compares great to good. Both columns won.",
         "The bars are not to scale. They are both labelled winner, because both are."], upto=1, focus=1))
    fr.append(F("18:30-19:45", head("The retraction", "Drawn. Then marked invalid.", "md") + '<div class="vis">' + win("_corpus.md",
        "<s>## Selection bias</s>\n\nTitle conclusion, top vs bottom of the set\n<u>STATUS: INVALID. Winners-only sample.</u>\nKept in the file, marked invalid.") +
        f'<div style="margin-top:14px">{needs("the retracted title conclusion, verbatim from _corpus.md")}</div></div>',
        ["That top-versus-bottom comparison was made, and a title conclusion was drawn from it. It was invalid, and it is recorded in the file as invalid.",
         "Kept in the file, marked invalid. Anyone who reads the file later sees the mistake and the reason.",
         "The mock window paraphrases. Paste the real line from _corpus.md before recording."], upto=1, focus=1))
    fr.append(F("19:45-20:45", head("What it is still good for", "What winners have in common.", "md") + '<div class="vis">' + ba(
        '<div class="h sm" style="color:#C0392B;text-decoration:line-through">what makes things fail</div><div class="mono" style="margin-top:16px;font-size:20px;color:#5F6B62">failures were never collected</div>',
        '<div class="h sm">what winners share</div><div class="mono" style="margin-top:16px;font-size:20px">the honest use of a swipe file</div>', "CANNOT TELL YOU", "CAN TELL YOU") + '</div>',
        ["The corpus is good for what winners have in common. It cannot tell you what makes something fail, because failures were never collected.",
         "A bigger swipe file does not fix that. More winners is still only winners."], upto=1, focus=1))
    fr.append(F("20:45-21:45", head("Swipe structure", "Take the structure. Leave the line.", "md") + '<div class="vis">' + ba(
        '<div class="tt">a line lifted from one winner</div><div class="mono" style="margin-top:16px;font-size:20px;color:#5F6B62">reads as borrowed</div>',
        '<div class="tt" style="border-left-color:#E9B949">a structure shared by many winners</div><div class="mono" style="margin-top:16px;font-size:20px">reads as competence</div>') + '</div>',
        ["Swipe structure, never lines. A line borrowed from a winner reads as borrowed. A structure borrowed from many winners reads as competence."], upto=1, focus=1))
    fr.append(F("21:45-22:30", head("Where the numbers live", "Two scripts. One file.", "md") +
        '<div class="vis" style="display:flex;gap:16px;align-items:center;font:800 24px Inter;color:#1B4332">'
        '<div class="card">41 captures</div>→<div class="card"><span class="mono" style="font-size:18px">article-title-features.py<br>article-cover-archetypes.py</span></div>→<div class="card on">one file</div>→<div class="card">the skills</div></div>',
        ["Two scripts read the corpus and regenerate the numbers. One pulls title features, one classifies cover archetypes. Both re-run when captures are added.",
         "Every rule in the writing skills points at the regenerated file, never at somebody's memory of it.",
         "[NEEDS: Mauro's call on folding in the 43-file archive batch. It would move every number the article skills cite.]"], upto=1))
    fr.append(F("22:30-23:00", '<div class="cta"><div class="k">If you run an agency</div><div class="h cp">Link in the description.</div><div class="pill cp">Agency Booked Calls</div></div>',
        ["If you run an established agency and want a content system built on evidence like this, the link is in the description. Agency Booked Calls.",
         "Everyone else: comment what is in your swipe file."], upto=1, dark=True))
    return dict(doc="04", slug="04-outlier-swipe-corpus", title="You'll never trust your swipe file again",
                rail=rail, crit=crit, rail_needs="", frames=fr, minutes=23)


# --------------------------------------------------------------------------------------------

def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def check_copy(b):
    """On-screen copy = .h headline, .nm reveal name, .agenda, .cta. At most 8 words."""
    bad = []
    for n, f in enumerate(b["frames"]):
        m = re.findall(r'class="[^"]*\bcp\b[^"]*"[^>]*>(.*?)</div>', f["body"], re.S)
        words = sum(len(re.findall(r"[A-Za-z0-9#'.,+%-]+", strip_tags(html.unescape(x)))) for x in m)
        if words > 8:
            bad.append((n + 1, words))
        txt = strip_tags(f["body"]) + " ".join(f["say"])
        if "—" in txt or "–" in txt:
            bad.append((n + 1, "dash"))
    return bad


def imgcss(b):
    allb = "".join(f["body"] for f in b["frames"])
    return "".join(f".c{n}{{background-image:url({IMG[c]})}}" for n, c in enumerate(CM) if f"c{n}" in allb)


def render_board(b):
    rail = "".join(f'<div class="row" data-rank="{r}"><div class="rk">#{r}</div><div class="lb">{E(l)}<span class="st">{E(s)}</span></div></div>' for r, l, s in b["rail"])
    rn = f'<span class="needs">[NEEDS: {E(b["rail_needs"])}]</span>' if b["rail_needs"] else ""
    frames = []
    for n, f in enumerate(b["frames"]):
        say = "".join(f"<p>{E(p)}</p>" for p in f["say"])
        src = f'<div class="src">{E(f["src"])}</div>' if f["src"] else ""
        frames.append(f'<section class="frame {"dark" if f["dark"] else ""}" data-upto="{f["upto"]}" data-focus="{f["focus"]}" data-time="{f["time"]}">'
                      f'{f["body"]}{src}<template class="say">{say}</template></section>')
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{E(b['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONTS}" rel="stylesheet">
<style>{CSS}{imgcss(b)}</style></head><body>
<div id="stage">
<aside id="rail"><div class="rh">The countdown</div><div class="crit">{E(b['crit'])}{rn}</div>{rail}<div class="foot">→ next · N notes · F full</div></aside>
<main id="frames">{''.join(frames)}</main>
<div id="notes"></div>
</div>
<script>{JS}</script></body></html>"""
    doc = controls.inject(doc, NAV_ADAPTER)
    with open(os.path.join(HERE, b["slug"] + ".html"), "w") as fh:
        fh.write(doc)


def write_notes(b):
    out = [f"# {b['slug']} · presenter notes (format D, ranked countdown)", "",
           f"Working title on frame 1: **{b['title']}**. Source: `research/video-knowledge/{b['doc']}-*.md`.",
           f"Ranking criterion on screen: {b['crit']}", "",
           f"{len(b['frames'])} frames, about {b['minutes']} minutes. Press N on the board to see these lines over the frame.", ""]
    for n, f in enumerate(b["frames"]):
        h = re.findall(r'class="[^"]*\bcp\b[^"]*"[^>]*>(.*?)</div>', f["body"], re.S)
        h = " / ".join(re.sub(r"\s+", " ", strip_tags(html.unescape(x))).strip() for x in h)
        out.append(f"## Frame {n+1} · {f['time']} · {h}")
        out.append("")
        for p in f["say"]:
            out.append(f"- {p}")
        if f["src"]:
            out.append(f"- *Source on frame:* {f['src']}")
        out.append("")
    with open(os.path.join(HERE, b["slug"] + ".notes.md"), "w") as fh:
        fh.write("\n".join(out))


# --------------------------------------------------------------------------------------------
# thumbnails

TCSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#8A8A8A;display:flex;flex-direction:column;align-items:center;gap:30px;padding:30px 0;font-family:'Inter',sans-serif}
.thumb{width:1280px;height:720px;position:relative;overflow:hidden;background:#0E2418}
.kick{font-family:'JetBrains Mono',monospace;font-size:26px;font-weight:800;letter-spacing:4px;color:#52B788}
.huge{font-size:132px;font-weight:900;color:#fff;line-height:.88;letter-spacing:-5px;text-transform:uppercase}
.huge em{font-style:normal;color:#E9B949}
.face{position:absolute;right:0;bottom:0;width:430px;height:640px;border:5px dashed rgba(233,185,73,.75);border-radius:20px 20px 0 0;display:flex;align-items:flex-end;justify-content:center;padding-bottom:26px;font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:700;color:rgba(233,185,73,.85);letter-spacing:2px}
.rail{position:absolute;left:0;top:0;bottom:0;width:120px;display:flex;flex-direction:column}
.rail div{flex:1;display:flex;align-items:center;justify-content:center;font:900 46px Inter;color:#0E2418}
.stamp{position:absolute;border:10px solid #C0392B;color:#C0392B;font:900 84px Inter;padding:6px 26px;transform:rotate(-8deg);letter-spacing:-2px;background:rgba(255,255,255,.08)}
"""


def thumbs07():
    cols = ["#E9B949", "#D9C25A", "#B7E4C7", "#8FD3AE", "#52B788", "#3B9A6E", "#24503A"]
    rail = "".join(f'<div style="background:{c};{"color:#fff" if n > 4 else ""}">{7-n}</div>' for n, c in enumerate(cols))
    wall = "".join(f'<div style="background:url({IMG[c]}) center/cover;border-radius:8px;{"outline:8px solid #E9B949;outline-offset:-8px" if n == 0 else "filter:grayscale(1) brightness(.5)"}"></div>' for n, c in enumerate(CM))
    return f"""
<div class="thumb"><div class="rail">{rail}</div>
<div style="position:absolute;left:170px;top:80px;width:620px"><div class="huge" style="margin-top:60px;font-size:150px">I ranked <em>his</em> channel</div></div>
<div class="face">MAURO CUTOUT HERE</div></div>

<div class="thumb"><div style="position:absolute;inset:0;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(2,1fr);gap:8px;padding:8px">{wall}</div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(14,36,24,.95) 0%,rgba(14,36,24,.6) 40%,rgba(14,36,24,0) 70%)"></div>
<div style="position:absolute;left:60px;bottom:50px" class="huge">Just copy <em>this</em></div>
<div style="position:absolute;left:30px;top:24px;width:150px;height:150px;border-radius:50%;background:#E9B949;display:flex;align-items:center;justify-content:center;font:900 76px Inter;color:#0E2418">#1</div></div>

<div class="thumb" style="background:#F7F3EA"><div style="position:absolute;left:70px;top:70px;width:700px;font-family:'JetBrains Mono',monospace;color:#1B4332">
<div style="font-size:30px;font-weight:800;letter-spacing:4px;color:#5F6B62">THE FORMULA</div>
<div style="margin-top:40px;font:900 96px Inter;letter-spacing:-3px;line-height:1">FACE<br><span style="color:#E9B949;-webkit-text-stroke:3px #1B4332">+ PROP</span></div>
<svg width="560" height="120" style="margin-top:30px"><path d="M10 60 C 150 10, 300 110, 540 50" stroke="#1B4332" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M515 30 L545 50 L512 72" stroke="#1B4332" stroke-width="7" fill="none" stroke-linecap="round"/></svg></div>
<div class="face" style="border-color:rgba(27,67,50,.6);color:#1B4332">MAURO CUTOUT HERE</div></div>
"""


def thumbs04():
    tiles = "".join(f'<div style="background:{"#E9B949" if k % 9 == 4 else "#52B788"};border-radius:6px"></div>' for k in range(41))
    pts = " ".join(f"{x},{560 - 240 * (2.71828 ** (-((x - 470) / 200) ** 2)):.0f}" for x in range(0, 1281, 20))
    return f"""
<div class="thumb"><div style="position:absolute;left:50px;top:60px;width:720px;height:600px;display:grid;grid-template-columns:repeat(7,1fr);gap:10px">{tiles}</div>
<div class="stamp" style="left:110px;top:250px;background:#0E2418">ALL WINNERS</div>
<div class="face">MAURO CUTOUT HERE</div></div>

<div class="thumb"><svg width="1280" height="720" style="position:absolute;inset:0"><rect x="880" y="0" width="400" height="562" fill="#E9B949" opacity=".85"/><polyline points="{pts}" fill="none" stroke="#B7E4C7" stroke-width="10"/><line x1="0" y1="562" x2="1280" y2="562" stroke="#B7E4C7" stroke-width="6"/></svg>
<div style="position:absolute;left:70px;top:70px" class="huge">No<br><em>bottom</em></div>
<div class="face" style="right:40px;height:540px;width:330px">MAURO CUTOUT HERE</div></div>

<div class="thumb"><div style="position:absolute;left:60px;top:20px;font:900 520px Inter;color:#fff;letter-spacing:-30px;line-height:1">41</div>
<div class="stamp" style="left:100px;top:470px;background:#0E2418">WINNERS ONLY</div>
<div class="face">MAURO CUTOUT HERE</div></div>
"""


def write_thumbs(slug, inner):
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>{slug} thumbnails</title>
<link href="{FONTS}" rel="stylesheet"><style>{TCSS}</style></head><body>{inner}</body></html>"""
    with open(os.path.join(HERE, slug + ".thumbs.html"), "w") as fh:
        fh.write(doc)


def chrome(png, size, url):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=4000",
                    f"--screenshot={png}", f"--window-size={size}", url], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


TITLES = {
    "11": [],
    "07": [
        {"title": "I reverse-engineered a big YouTube channel in one afternoon",
         "modelled_on": "01-outliers.csv: Marcos Ruiz, \"I Copied a Twitter/X Account That Makes $100k/mo (it worked?)\" (study someone else's account, report the result)"},
        {"title": "I ranked a top creator's YouTube tricks so you don't have to",
         "modelled_on": "charlie-morgan-dig.md #9: \"I Ranked Every Online Business Model So You Don't Have To\" (save-you-effort authority)"},
        {"title": "Charlie Morgan's YouTube formula (just copy him)",
         "modelled_on": "01-outliers.csv: David Ondrej, \"Matt Pocock's Agentic Engineering Workflow (just copy him)\". Naming him needs Mauro's sign-off"},
    ],
    "04": [
        {"title": "You'll never trust your swipe file again after this",
         "modelled_on": "charlie-morgan-dig.md #1: \"You'll NEVER Doomscroll Again After Watching This\""},
        {"title": "I studied 41 winning X articles (here's the catch)",
         "modelled_on": "01-outliers.csv: Marcos Ruiz, \"I Copied a Twitter/X Account That Makes $100k/mo (it worked?)\" (study, then the twist in brackets)"},
        {"title": "The swipe file that actually works (full system)",
         "modelled_on": "01-outliers.csv: Greg Isenberg, \"Building AI Agents that actually work (Full Course)\""},
    ],
}


def main():
    for c in CM:
        IMG[c] = img64(c)
    boards = [board11(), board07(), board04()]
    problems = []
    meta = []
    for b in boards:
        render_board(b)
        write_notes(b)
        problems += [(b["slug"],) + p for p in check_copy(b)]
        nd = sorted(set(re.findall(r"\[NEEDS: ([^\]]+)\]", "".join(f["body"] + " ".join(f["say"]) for f in b["frames"]) + (f"[NEEDS: {b['rail_needs']}]" if b["rail_needs"] else ""))))
        meta.append({"doc": b["doc"], "file": b["slug"] + ".html", "titles": TITLES[b["doc"]],
                     "frames": len(b["frames"]), "minutes": b["minutes"], "needs": nd})
    write_thumbs("07-reverse-engineer-channel", thumbs07())
    write_thumbs("04-outlier-swipe-corpus", thumbs04())
    with open(os.path.join(HERE, "meta.json"), "w") as fh:
        json.dump(meta, fh, indent=2)
    for p in problems:
        print("COPY CHECK:", p)
    if "--png" in sys.argv:
        for b in boards:
            chrome(os.path.join(HERE, b["slug"] + ".cover.png"), "1600,900", "file://" + os.path.join(HERE, b["slug"] + ".html"))
        for s in ("07-reverse-engineer-channel", "04-outlier-swipe-corpus"):
            chrome(os.path.join(HERE, s + ".thumbs.png"), "1340,2280", "file://" + os.path.join(HERE, s + ".thumbs.html"))
    print("built", [m["file"] for m in meta])


if __name__ == "__main__":
    main()
