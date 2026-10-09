#!/usr/bin/env python3
"""Build the record-ready YouTube boards in boards/yt/.

Each output HTML is self-contained (inline CSS, inline SVG charts). The only external
requests are Google Fonts, with a system-font fallback, so a double-click works offline.

Every chart number below is copied from brand/claims.md (or the file named next to it).
Nothing is computed from live data. Edit a number here, re-run, and the board changes.

    python3 boards/yt/build.py            # writes the three .html files
    python3 boards/yt/build.py --png      # also renders full-page PNG previews

Palette: Type 2 board system, skills/content/visual-docs/mauro-visual-doc-system.md
(cream ground, Deep Forest structure, Honey #E9B949 as the one accent). Set by Mauro 2026-09-23.
"""
import html
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FRAME_H = 900  # one 16:9 recording frame at 1600 wide

CSS = """
:root{--ground:#F7F3EA;--card:#FFFFFF;--ink:#1B4332;--body:#1B1B1B;--muted:#5F6B62;
--accent:#E9B949;--soft:#B9C7BE;--line:#D8CFBB;--frame-h:%dpx}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth;scrollbar-width:none}
html::-webkit-scrollbar{display:none}
body{background:var(--ground);color:var(--body);font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased}
.mono{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace}
.board{width:1600px;margin:0 auto}
.frame{min-height:var(--frame-h);scroll-snap-align:start;scroll-snap-stop:always;display:flex;flex-direction:column;justify-content:center;padding:60px 120px;position:relative}
.beat{font:700 17px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:22px;display:flex;align-items:center;gap:14px}
.beat .n{background:var(--ink);color:#fff;padding:6px 12px;letter-spacing:.08em}
.talk{font-size:58px;font-weight:800;line-height:1.1;letter-spacing:-.02em;color:var(--ink);max-width:1340px}
.talk.sm{font-size:46px}
.hl{background:var(--accent);color:var(--ink);padding:0 .14em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.visual{margin-top:42px}
.note{margin-top:38px;padding-top:16px;border-top:2px solid var(--line);font-size:20px;line-height:1.45;color:var(--muted);display:flex;gap:18px;max-width:1360px}
.note b{font:700 14px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.16em;color:var(--ink);padding-top:4px;white-space:nowrap}
.src{margin-top:14px;font:500 15px 'JetBrains Mono',ui-monospace,Menlo,monospace;color:var(--muted)}
/* title card */
.title .kicker{font:700 20px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.22em;color:var(--muted);text-transform:uppercase}
.title h1{font-size:92px;font-weight:900;line-height:1.02;letter-spacing:-.035em;color:var(--ink);margin:26px 0 30px;max-width:1360px}
.title .sub{font-size:30px;font-weight:600;color:#3D4A42;line-height:1.35;max-width:1200px}
.pill{display:inline-block;margin-top:44px;background:var(--accent);border:3px solid var(--ink);padding:12px 26px;font-weight:800;font-size:22px;color:var(--ink)}
/* hook */
.hook .line{font-size:50px;font-weight:800;line-height:1.15;color:var(--ink);letter-spacing:-.015em;max-width:1360px}
.onscreen{margin-top:30px;border:3px solid var(--ink);background:var(--card);padding:16px 22px;font-size:21px;display:flex;gap:16px;align-items:baseline}
.onscreen b{font:700 14px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.16em;background:var(--ink);color:var(--accent);padding:5px 10px;white-space:nowrap}
.agenda{margin-top:30px;display:grid;grid-template-columns:1fr 1fr;gap:10px 48px}
.agenda .h{grid-column:1/-1;font:700 16px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.18em;color:var(--muted);text-transform:uppercase;margin-bottom:4px}
.agenda div{font-size:24px;font-weight:600;color:var(--body);display:flex;gap:14px}
.agenda span{font:800 18px 'JetBrains Mono',ui-monospace,Menlo,monospace;color:var(--ink);background:var(--accent);min-width:38px;text-align:center;padding:3px 0;height:30px}
/* tiles */
.tiles{display:grid;gap:24px}
.tile{background:var(--card);border:3px solid var(--ink);padding:26px 28px}
.tile .v{font-size:66px;font-weight:900;letter-spacing:-.03em;color:var(--ink);line-height:1}
.tile .l{margin-top:12px;font-size:21px;font-weight:600;color:#3D4A42;line-height:1.3}
.compact .tiles{gap:14px}.compact .tile{padding:14px 22px}.compact .tile .v{font-size:40px}.compact .tile .l{margin-top:6px;font-size:19px}
.tile.on{border-top:12px solid var(--accent)}
.tile .k{font:700 13px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.14em;color:var(--muted);text-transform:uppercase;margin-bottom:10px}
/* flow */
.flow{display:flex;align-items:stretch;gap:0}
.node{flex:1;background:var(--card);border:3px solid var(--ink);padding:20px 20px;font-size:23px;font-weight:700;color:var(--ink);line-height:1.25;display:flex;flex-direction:column;justify-content:center}
.node small{display:block;margin-top:8px;font-size:17px;font-weight:500;color:var(--muted);line-height:1.3}
.node .k{font:700 13px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.14em;color:var(--muted);margin-bottom:8px}
.node.dark{background:var(--ink);color:#fff}
.node.dark small{color:#CFE0D5}
.node.dark .k{color:var(--accent)}
.node.on{border-top:12px solid var(--accent)}
.node.ghost{background:transparent;border:3px dashed var(--muted);color:var(--muted)}
.arrow{display:flex;align-items:center;justify-content:center;width:54px;flex:none;color:var(--ink);font-size:34px;font-weight:800}
.flow.tight .arrow{width:30px;font-size:24px}.flow.tight .node{padding:14px 10px;font-size:19px!important;min-width:0}
.down{text-align:center;font-size:34px;font-weight:800;color:var(--ink);line-height:1;margin:10px 0}
/* table */
table.t{width:100%%;border-collapse:collapse;background:var(--card);border:3px solid var(--ink)}
table.t td,table.t th{padding:16px 22px;font-size:22px;text-align:left;border-bottom:2px solid var(--line);vertical-align:top;line-height:1.35}
table.t th{background:var(--ink);color:#fff;font:700 15px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.14em;text-transform:uppercase}
table.t td:first-child{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace;font-weight:700;color:var(--ink);white-space:nowrap;font-size:20px}
/* code / tree */
pre.tree{background:var(--ink);color:#EAF2EC;font:500 17.5px/1.42 'JetBrains Mono',ui-monospace,Menlo,monospace;padding:26px 30px;border:3px solid var(--ink);white-space:pre;overflow:hidden}
pre.tree i{font-style:normal;color:var(--accent)}
pre.tree em{font-style:normal;color:#9FB8A8}
.formula{background:var(--ink);color:#fff;padding:30px 36px;font:600 34px 'JetBrains Mono',ui-monospace,Menlo,monospace;border:3px solid var(--ink)}
.formula i{font-style:normal;color:var(--accent)}
.formula small{display:block;margin-top:14px;font-size:19px;color:#CFE0D5;font-weight:500}
/* split */
.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.split.w{grid-template-columns:5fr 6fr}
/* images and screen slots */
.shot{display:block;max-width:100%%;max-height:520px;border:3px solid var(--ink);background:#fff;margin:0 auto}
.slot{border:4px dashed var(--ink);background:repeating-linear-gradient(135deg,transparent 0 22px,rgba(27,67,50,.04) 22px 44px);min-height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:30px}
.slot b{font:800 16px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.2em;background:var(--accent);color:var(--ink);padding:6px 12px;margin-bottom:14px}
.slot span{font-size:25px;font-weight:700;color:var(--ink);max-width:900px;line-height:1.3}
.slot small{margin-top:10px;font-size:18px;color:var(--muted)}
.slot.short{min-height:170px}
/* quote cards */
.quotes{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.q{position:relative;background:var(--card);border:3px solid var(--ink);padding:36px 28px 30px;font-size:30px;font-weight:800;color:var(--ink);line-height:1.2}
.q .stamp{position:absolute;top:-18px;right:18px;background:var(--accent);border:3px solid var(--ink);font:800 18px 'JetBrains Mono',ui-monospace,Menlo,monospace;padding:4px 12px}
.chips{display:flex;flex-wrap:wrap;gap:12px}
.chip{border:3px solid var(--ink);background:var(--card);padding:10px 16px;font-size:20px;font-weight:700;color:var(--ink)}
.chip.on{background:var(--accent)}
blockquote{border-left:12px solid var(--accent);background:var(--card);padding:26px 30px;font-size:27px;line-height:1.4;font-weight:600;color:var(--ink);border-top:3px solid var(--ink);border-right:3px solid var(--ink);border-bottom:3px solid var(--ink)}
blockquote cite{display:block;margin-top:12px;font:500 16px 'JetBrains Mono',ui-monospace,Menlo,monospace;color:var(--muted);font-style:normal}
.cta{background:var(--ink);color:#fff;padding:40px 44px;border:3px solid var(--ink)}
.cta .k{font:700 15px 'JetBrains Mono',ui-monospace,Menlo,monospace;letter-spacing:.18em;color:var(--accent)}
.cta .m{font-size:40px;font-weight:800;margin-top:14px;line-height:1.2}
.cta .s{font-size:20px;color:#CFE0D5;margin-top:14px}
.end{margin-top:30px;display:inline-block;background:var(--accent);border:3px solid var(--ink);padding:10px 20px;font-weight:800;font-size:22px;color:var(--ink)}
svg text{font-family:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif}
""" % FRAME_H

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=1600">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
<!-- {comment} -->
<style>{css}</style></head>
<body><main class="board">
"""

INK, ACC, SOFT, MUTED = "#1B4332", "#E9B949", "#B9C7BE", "#5F6B62"


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- chart helpers (inline SVG)

def hbar(rows, width=1360, label_w=430, row_h=60, fmt=lambda v: f"{v:g}", maxv=None, value_w=260):
    """rows: (label, value, highlight, note). Bars drawn on absolute value."""
    maxv = maxv or max(abs(r[1]) for r in rows)
    area = width - label_w - value_w
    h = row_h * len(rows) + 10
    out = [f'<svg width="{width}" height="{h}" viewBox="0 0 {width} {h}" role="img">']
    for i, (label, v, hl, note) in enumerate(rows):
        y = i * row_h + 6
        w = max(abs(v) / maxv * area, 4)
        fill = ACC if hl else INK
        out.append(f'<text x="{label_w-22}" y="{y+row_h/2+2}" text-anchor="end" font-size="24" font-weight="600" fill="#1B1B1B" dominant-baseline="middle">{esc(label)}</text>')
        out.append(f'<rect x="{label_w}" y="{y+8}" width="{w:.1f}" height="{row_h-22}" fill="{fill}" stroke="{INK}" stroke-width="{3 if hl else 0}"/>')
        out.append(f'<text x="{label_w+w+16:.1f}" y="{y+row_h/2+2}" font-size="25" font-weight="800" fill="{INK}" dominant-baseline="middle">{esc(fmt(v))}'
                   + (f'<tspan font-size="18" font-weight="500" fill="{MUTED}">  {esc(note)}</tspan>' if note else "") + '</text>')
    out.append(f'<line x1="{label_w}" y1="0" x2="{label_w}" y2="{h}" stroke="{INK}" stroke-width="3"/>')
    out.append("</svg>")
    return "".join(out)


def stacked(rows, width=1360, label_w=0):
    """rows: (title, total, [(label, value, highlight)]). One full-width stacked bar per row."""
    row_h = 150
    h = row_h * len(rows)
    out = [f'<svg width="{width}" height="{h}" viewBox="0 0 {width} {h}" role="img">']
    for i, (title, total, parts) in enumerate(rows):
        y = i * row_h
        out.append(f'<text x="0" y="{y+26}" font-size="24" font-weight="700" fill="#1B1B1B">{esc(title)}</text>')
        x = 0.0
        for label, v, hl in parts:
            w = v / total * width
            fill = ACC if hl else SOFT
            out.append(f'<rect x="{x:.1f}" y="{y+42}" width="{w:.1f}" height="56" fill="{fill}" stroke="{INK}" stroke-width="3"/>')
            if w > 260:
                out.append(f'<text x="{x+18:.1f}" y="{y+78}" font-size="24" font-weight="800" fill="{INK}">{esc(label)}</text>')
            else:
                out.append(f'<text x="{x+w:.1f}" y="{y+128}" text-anchor="end" font-size="20" font-weight="700" fill="{INK}">{esc(label)}</text>')
            x += w
    out.append("</svg>")
    return "".join(out)


def columns(rows, width=900, height=420, maxv=None, fmt=lambda v: f"{v:g}"):
    """Vertical columns. rows: (label, value, highlight)."""
    maxv = maxv or max(r[1] for r in rows)
    n = len(rows)
    col_w = 200
    gap = (width - n * col_w) / (n + 1)
    base = height - 60
    out = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">']
    for i, (label, v, hl) in enumerate(rows):
        x = gap + i * (col_w + gap)
        hgt = v / maxv * (base - 60)
        out.append(f'<rect x="{x:.1f}" y="{base-hgt:.1f}" width="{col_w}" height="{hgt:.1f}" fill="{ACC if hl else INK}" stroke="{INK}" stroke-width="3"/>')
        out.append(f'<text x="{x+col_w/2:.1f}" y="{base-hgt-16:.1f}" text-anchor="middle" font-size="34" font-weight="900" fill="{INK}">{esc(fmt(v))}</text>')
        out.append(f'<text x="{x+col_w/2:.1f}" y="{base+40}" text-anchor="middle" font-size="24" font-weight="700" fill="#1B1B1B">{esc(label)}</text>')
    out.append(f'<line x1="0" y1="{base}" x2="{width}" y2="{base}" stroke="{INK}" stroke-width="3"/>')
    out.append("</svg>")
    return "".join(out)


# ---------------------------------------------------------------- frame helpers

def title_frame(kicker, h1, sub, pill="Mauro · @maurojpelle"):
    return f'<section class="frame title"><div class="kicker">{kicker}</div><h1>{h1}</h1><div class="sub">{sub}</div><div><span class="pill">{pill}</span></div></section>\n'


def hook_frame(line, onscreen, agenda, note):
    items = "".join(f"<div><span>{i+1:02d}</span>{a}</div>" for i, a in enumerate(agenda))
    return (f'<section class="frame hook"><div class="beat"><span class="n">HOOK</span>0:00 · cold open + today we\'ll go over</div>'
            f'<div class="line">{line}</div>'
            f'<div class="onscreen"><b>ON SCREEN</b><div>{onscreen}</div></div>'
            f'<div class="agenda"><div class="h">Today we\'ll go over</div>{items}</div>'
            f'<div class="note"><b>SAY</b><div>{note}</div></div></section>\n')


def frame(n, label, talk, visual, note, src=None, comment=None, small=False):
    c = f"<!-- {comment} -->" if comment else ""
    s = f'<div class="src">{src}</div>' if src else ""
    return (f'<section class="frame">{c}<div class="beat"><span class="n">BEAT {n:02d}</span>{label}</div>'
            f'<div class="talk{" sm" if small else ""}">{talk}</div>'
            f'<div class="visual">{visual}{s}</div>'
            f'<div class="note"><b>SAY</b><div>{note}</div></div></section>\n')


def split_frame(n, label, talk, left_extra, right, note, src=None, comment=None):
    c = f"<!-- {comment} -->" if comment else ""
    s = f'<div class="src">{src}</div>' if src else ""
    return (f'<section class="frame">{c}<div class="split w"><div>'
            f'<div class="beat"><span class="n">BEAT {n:02d}</span>{label}</div>'
            f'<div class="talk sm">{talk}</div>{left_extra}'
            f'<div class="note"><b>SAY</b><div>{note}</div></div></div>'
            f'<div>{right}{s}</div></div></section>\n')


def flow(nodes, cls=""):
    """nodes: list of (k, title, small, cls)."""
    parts = []
    for i, (k, t, sm, ncls) in enumerate(nodes):
        if i:
            parts.append('<div class="arrow">&rarr;</div>')
        kk = f'<div class="k">{k}</div>' if k else ""
        ss = f"<small>{sm}</small>" if sm else ""
        parts.append(f'<div class="node {ncls}">{kk}{t}{ss}</div>')
    return f'<div class="flow {cls}">{"".join(parts)}</div>'


def tiles(items, cols):
    """items: (k, value, label, on)."""
    t = "".join(f'<div class="tile{" on" if on else ""}">' + (f'<div class="k">{k}</div>' if k else "")
                + f'<div class="v">{v}</div><div class="l">{l}</div></div>' for k, v, l, on in items)
    return f'<div class="tiles" style="grid-template-columns:repeat({cols},1fr)">{t}</div>'


def slot(text, small=None, short=False):
    sm = f"<small>{small}</small>" if small else ""
    return f'<div class="slot{" short" if short else ""}"><b>SCREEN</b><span>{text}</span>{sm}</div>'


def img(path, alt, maxh=None):
    st = f' style="max-height:{maxh}px"' if maxh else ""
    return f'<img class="shot" src="{path}" alt="{esc(alt)}"{st}>'


def cta_frame(n, talk, msg, sub, note):
    return (f'<section class="frame"><div class="beat"><span class="n">BEAT {n:02d}</span>recap + CTA</div>'
            f'<div class="talk sm">{talk}</div><div class="visual"><div class="cta"><div class="k">IF YOU RUN AN ESTABLISHED AGENCY</div>'
            f'<div class="m">{msg}</div><div class="s">{sub}</div></div><span class="end">@maurojpelle on X</span></div>'
            f'<div class="note"><b>SAY</b><div>{note}</div></div></section>\n')


def page(title, comment, frames):
    return HEAD.format(title=esc(title), comment=comment, css=CSS) + "".join(frames) + "</main></body></html>\n"


CTA_SUB = "[CTA: confirm the current offer and link with Mauro before recording]"

# ================================================================ VIDEO 01 · the content system (doc 11)

ROOT = "../.."
V1 = [
    title_frame("Video 01 · AI content systems that book calls",
                "The Claude Code system I run for a <span class=\"hl\">$300k/mo</span> agency",
                "One repo, 73 skill files, 25 scripts and four agents, with the incident that created each agent."),
    hook_frame(
        "Everyone says they built a system in Claude Code. I am going to open mine folder by folder, and show you what broke to make each part of it.",
        "Flythrough of this board top to bottom at speed, then cut to the repo tree in the terminal.",
        ["What the number means", "One repo and the map", "Skills split by activity", "The seven-file article set",
         "The Monday analysis", "Four agents, four incidents", "25 scripts, each with its limit", "The claim that measured backwards",
         "How the day runs", "What it still can't do"],
        "Name the agency's number once, with its definition. Then go straight to the repo."),
    frame(1, "the number, defined",
          "The agency is at about <span class=\"hl\">$300k a month</span>. The engine behind its inbound is the part I run.",
          tiles([("agency revenue", "$300k/mo", "the agency's number, not mine", False),
                 ("from organic", "&ge; 1/3", "comes from the organic accounts I manage", False),
                 ("2026 to date", "150+", "qualified booked calls generated for the agency", True)], 3),
          "Say the definition in the same sentence as the number. The 150 is the Calendly total. Do not split it by channel: the export can't carry that.",
          src="source: brand/claims.md, 'Cleared in the 21 Sep article brief' + 'Mauro's own operation' (150, confirmed 2026-09-14)",
          comment="Numbers: brand/claims.md. $300k/mo and 1/3 cleared 21 Sep as the agency's number. 150+ public, total only, no channel claim."),
    split_frame(2, "the skeleton",
                "One repo. Eleven areas, and one map that indexes all of them.",
                '<div class="visual">' + slot("Open the repo in the terminal and run the tree. Blur any account folder name.", short=True) + "</div>",
                '<pre class="tree"><i>agency-os/</i>                <em>the whole operation</em>\n'
                '├── skills/               <em>73 files, by activity</em>\n'
                '│   ├── content/          <em>incl. x-articles/ (7)</em>\n'
                '│   ├── research/\n│   ├── ops/\n│   ├── miro/\n│   ├── lead-gen/\n│   ├── youtube/\n'
                '│   ├── creative-strategy/\n│   └── dm-setting/\n'
                '├── .claude/agents/       <em>4 installed agents</em>\n'
                '├── ops/\n'
                '│   ├── <i>MAP.md</i>            <em>the index</em>\n'
                '│   ├── CONVENTIONS.md    <em>nine rules</em>\n'
                '│   ├── tools/            <em>25 scripts</em>\n'
                '│   └── daily/\n'
                '├── research/\n'
                '├── accounts/             <em>[REDACTED]</em>\n'
                '├── acquisition-calls/    <em>one analysis a week</em>\n'
                '├── outbound-calls/\n'
                '└── BACKLOG.md</pre>',
                "Read the folder names out loud. Each area has an owner and an entry point in the map.",
                src="counts as published 2026-09-10 · re-count on the day",
                comment="Tree: research/video-knowledge/assets/repo-tree-screen-safe.txt, root renamed so the agency is never named on screen."),
    frame(3, "route it or it doesn't exist",
          "Work is not finished until it is <span class=\"hl\">routed</span> in the map.",
          flow([("TRIGGER", "A new request", None, ""), ("STEP", "Check ops/MAP.md", "the routing table", "dark"),
                ("FOUND", "Use the file that exists", None, ""), ("NOT FOUND", "Build it, then add the row", "same session", "on")])
          + '<div style="height:28px"></div>' + slot("Open ops/MAP.md and scroll the routing table.", short=True),
          "An agent once rebuilt an outbound SOP that already existed, because that folder was missing from the routing table. That day the rule went in. [NEEDS: confirm the time lost, MAP.md says 45 minutes, not yet in claims.md]",
          comment="Story: research/video-knowledge/11 section 1 + 02 section 2 (observed, ops/MAP.md). The 45 minutes is not in brand/claims.md, so it stays in the note as a NEEDS."),
    frame(4, "the skills",
          "73 skill files, split by <span class=\"hl\">activity</span>. A client folder dies with the client.",
          tiles([(None, "content/", "long-form, short-form, articles", False), (None, "research/", "breakdowns, teardowns", False),
                 (None, "ops/", "daily, weekly, Monday", False), (None, "miro/", "boards and the gotchas", False),
                 (None, "lead-gen/", "five magnet subtypes", False), (None, "youtube/", "ideas, titles, hooks, boards", False),
                 (None, "creative-strategy/", "statics, script QA", False), (None, "dm-setting/", "inbound and outbound", False)], 4)
          .replace('class="v"', 'class="v" style="font-size:30px;font-family:JetBrains Mono,monospace"'),
          "An activity survives every client. The same skill rebuilt inside the next client folder is the cost you avoid.",
          src="73 files across 8 folders · brand/claims.md, 'The content system, as published 2026-09-10'"),
    frame(5, "open the article set",
          "Seven files turn one transcript into an X article, in a fixed order.",
          flow([("1", "Subject", "3 to 4, pick one", ""), ("2", "First screen", "cover, title, 3 lines", "on"), ("3", "Title", "5 scored", ""),
                ("4", "Cover", "archetype + prompt", ""), ("5", "Body", "every claim sourced", ""), ("6", "Companion", "post + keyword", ""),
                ("7", "Keeper", "keeps 1-6 honest", "dark")]).replace("font-size:23px", "")
          + '<div style="height:28px"></div>' + slot("Open skills/content/x-articles/ and show the seven files in order.", short=True),
          "Subject before title. Title and cover get drafted together. The seventh file only exists to keep the other six honest as evidence lands.",
          comment="Order: research/video-knowledge/09-transcript-to-article.md section 1."),
    frame(6, "the Monday analysis",
          "Every Monday, four inputs become one ten-section read.",
          '<div class="split" style="grid-template-columns:1fr 60px 1fr 60px 1fr;gap:0;align-items:stretch">'
          '<div class="chips" style="flex-direction:column;justify-content:center"><div class="chip">Call structure tracker</div><div class="chip">Calendly export</div><div class="chip">X analytics</div><div class="chip">Weekly targets</div></div>'
          '<div class="arrow">&rarr;</div><div class="node dark"><div class="k">THE READ</div>Ten fixed sections<small>same order every week</small></div>'
          '<div class="arrow">&rarr;</div><div class="node on"><div class="k">THE DIFF</div>Every metric against last week<small>open items carried forward</small></div></div>'
          + '<div style="height:28px"></div>' + slot("Open last Monday's analysis. Blur names and accounts.", short=True),
          "Two rules worth stealing. Count calls by the date they were conducted. And watch impressions per post, because the headline number keeps climbing while the ratio collapses.",
          comment="Structure: skills/ops/monday-acquisition-analysis.md as described in research/video-knowledge/11 + 08 section 6."),
    frame(7, "four agents, four incidents",
          "An agent runs without being asked. Each of these four exists because something was missed.",
          '<table class="t"><tr><th>Agent</th><th>Exists because</th></tr>'
          '<tr><td>performance-loop</td><td>Monthly impressions fell 64% from June to August 2026, and nobody noticed for two months.</td></tr>'
          '<tr><td>signal-sweep</td><td>A catch-up missed a two-message group DM that held one key number.</td></tr>'
          '<tr><td>board-qa</td><td>Boards went out full rather than recordable. It asks one question through fifteen checks.</td></tr>'
          '<tr><td>youtube-lead-magnet</td><td>Packaging drift. Its first instruction is to run the existing skill.</td></tr></table>',
          "Every agent is a scar. Read the right-hand column, one row at a time.",
          src="brand/claims.md, 'The content system, as published 2026-09-10' (64%, fifteen checks, four agents)",
          comment="The signal-sweep number is not named on purpose: it is not in brand/claims.md."),
    frame(8, "the drop nobody saw",
          "Monthly impressions fell <span class=\"hl\">64%</span> between June and August.",
          '<div class="split" style="grid-template-columns:900px 1fr">' + columns([("June 2026", 100, False), ("August 2026", 36, True)], width=900, height=400)
          + '<div class="tile on"><div class="k">unnoticed for</div><div class="v">2 months</div><div class="l">That gap is the reason performance-loop exists.</div></div></div>',
          "I only publish the percentage, so the chart is indexed to June. Then open .claude/agents/performance-loop.md.",
          src="indexed, June = 100 · derived from the published 64% · brand/claims.md",
          comment="Data: brand/claims.md row 'Monthly impressions fell 64% between June and August 2026'. Index 100 -> 36 is that percentage; raw monthly impressions are not shown."),
    frame(9, "save the script, state its limit",
          "25 scripts. The analysis behind any number gets saved as a script, and the script states what it can't measure.",
          stacked([("Calendly rows by owner, 678 total", 678, [("649 under one owner", 649, True), ("29 other", 29, False)]),
                   ("UTM field, 678 rows", 678, [("673 empty", 673, True), ("5 filled", 5, False)])]),
          "One tool was named as if it measured a single account's bookings. It measures all inbound. Its docstring now says so in capitals.",
          src="649 of 678 · UTM empty on 673 · brand/claims.md, published 2026-09-10",
          comment="Data: brand/claims.md 'The content system, as published 2026-09-10'. 29 and 5 are 678 minus the published figures.", small=True),
    frame(10, "the claim that measured backwards",
          "A skill said the worked example was the section that converts. I measured it.",
          hbar([("Worked example section", 60000, False, "what the skill claimed"), ("Winning section", 264000, True, None)],
               fmt=lambda v: f"{v:,.0f}", label_w=400, value_w=340, row_h=80)
          + '<div style="height:30px"></div><div class="chips"><div class="chip on">Every claim carries an evidence tag</div><div class="chip">Every number traces to a script</div><div class="chip">Every script states its limit</div><div class="chip">Decisions are dated lines</div></div>',
          "It felt obviously true. These are the four conventions out of nine that carry the weight.",
          src="60,000 against 264,000 · brand/claims.md, published 2026-09-10",
          comment="Data: brand/claims.md row 'A skill claimed the worked example was the converting section; it did 60,000 against the winning section's 264,000'."),
    frame(11, "how the day runs",
          "The plan comes out of the backlog. The tick comes from Google Tasks.",
          flow([("07:30", "Export", "the day's inputs", ""), ("08:00", "Tasks created", "from BACKLOG.md", "on"), ("DAY", "Work", "max 3 spine items", "ghost"),
                ("16:40", "Export", None, ""), ("17:00", "Completions written back", None, "dark")]),
          "Version two failed because a calendar block had no done state. Version three takes the tick from the task itself.",
          comment="Times: research/video-knowledge/11 section 5 (daily ops v3, built 2026-08-31)."),
    frame(12, "what it can't do yet",
          "Every agent here is defensive. None of them reaches out to a human.",
          flow([("CATCHES", "A reach drop", "performance-loop", ""), ("CATCHES", "A missed ask", "signal-sweep", ""), ("GATES", "A board", "board-qa", ""),
                ("PACKAGES", "An asset", "youtube-lead-magnet", ""), ("NEXT VIDEO", "The agent that causes a call", "not built", "ghost")]),
          "That gap is the next video. Say it plainly: nothing in this repo books a call on its own.",
          src="brand/claims.md: 'Four agents, all defensive, none reaches out to a human'"),
    cta_frame(13, "Copy the corrections, the provenance and the four agents first. The prompts come last.",
              "DM me on X and I'll show you how this gets installed in your agency.", CTA_SUB,
              "Two sentences of recap, then the CTA. Qualify the viewer: established agency owners."),
]

# ================================================================ VIDEO 02 · X ranking weights (doc 05, rebuilt on param.rs)

POS = [("share via copy link", 20.0, True, "highest positive in the file"), ("reply", 5.0, False, None), ("quote", 5.0, False, None),
       ("retweet", 1.0, False, None), ("like", 0.5, False, None), ("time after the tap", 0.4, False, None), ("the tap", 0.3, False, None),
       ("open link", 0.2, False, None), ("video open", 0.07, False, None), ("video quality view", 0.0, False, None)]
V2 = [
    title_frame("Video 02 · AI content systems that book calls",
                "I read X's ranking code so you don't have to",
                "Every default weight in the For You ranker, read line by line from param.rs on 1 October 2026."),
    hook_frame(
        "Every X algorithm number you were quoted this year comes from a system X replaced. The real defaults are public now, so I'm going to read them to you from the file.",
        "Flythrough of this board, then cut to github.com/xai-org/x-algorithm with the params file open.",
        ["Where the old numbers came from", "The formula", "When the weights landed", "The ten positive weights",
         "Copy link and the reply boost", "Four dwell params", "What costs you", "Why posting more doesn't stack",
         "Cold start", "What my own account shows", "Check any claim yourself"],
        "The authority is the open-source repo. Say that early, and keep saying it."),
    frame(1, "the folklore",
          "Three numbers everyone quotes. All three are from <span class=\"hl\">2023</span>.",
          '<div class="quotes"><div class="q"><span class="stamp">2023</span>"a reply is worth 13.5 likes"</div>'
          '<div class="q"><span class="stamp">2023</span>"a repost is 20x a like"</div>'
          '<div class="q"><span class="stamp">2023</span>"one reply beats 150 likes"</div></div>'
          '<div style="height:28px"></div>' + slot("Paste two or three real posts that quote these numbers. Crop out the handles.", short=True),
          "They come from the 2023 release of twitter/the-algorithm. That system got replaced. Say 2023 every time one of these is on screen.",
          src="brand/claims.md, 'The X For You ranking code' row #1"),
    frame(2, "open the repo",
          "The ranker is open source. Open it with me.",
          slot("Open github.com/xai-org/x-algorithm. Read the stars and the last push date live.",
               "The 4 Aug figures (26,909 stars, 216 files) are stale. Re-read them on the day."),
          "Then open home-mixer/params/param.rs. This is the file the rest of the video reads from.",
          comment="research/video-knowledge/05: repo facts are at fetch time 2026-08-04 and will have moved."),
    split_frame(3, "the formula",
                "The score is a weighted sum of predicted actions.",
                '<div class="visual"><div class="formula">score = &Sigma; <i>weight</i> &times; P(action)<small>P = the model\'s predicted chance this viewer does it</small></div></div>',
                img(f"{ROOT}/content/ascii/xalgo-01-the-scorer.png", "How a post is scored, param.rs", 600),
                "The weights multiply probabilities. A report sits at -234 because a report is rare, and the file says so in a comment.",
                src="content/ascii/xalgo-01-the-scorer.png"),
    frame(4, "when the weights landed",
          "The formula shipped in January. The weight values landed in August.",
          flow([("2023", "twitter/the-algorithm", "explicit weights, since replaced", "ghost"),
                ("JAN 2026", "xai-org/x-algorithm", "formula + scored actions, no values", ""),
                ("13-14 AUG 2026", "params/param.rs added", "every default published", "on"),
                ("1 OCT 2026", "Read line by line", "the numbers on this board", "dark")]),
          "My own thread from 4 September said the code shows no weight values. That was true of the January release, and it's out of date now. Say so on camera.",
          src="brand/claims.md, 'The no-weights rule is retired, 2026-10-01'"),
    frame(5, "the positives",
          "Ten positive weights, read straight from the file.",
          hbar(POS, row_h=50, label_w=380, value_w=420),
          "Read top to bottom. Copy link is the highest positive in the file. Video quality view is zero.",
          src="param.rs defaults, read 2026-10-01 · brand/claims.md 'X ranking weights' · every value is a default",
          comment="Data: brand/claims.md, 'X ranking weights, read from param.rs on 2026-10-01'. Defaults; X can override per experiment or per user.",
          small=True),
    split_frame(6, "copy link and the reply boost",
                "Copy link carries <span class=\"hl\">20.0</span>. A like carries 0.5.",
                '<div class="visual compact">' + tiles([("ShareViaCopyLink", "20.0", "private and deliberate", True), ("Like", "0.5", "public and cheap", False),
                                                ("BidirectionalFollowReplyWeightBoost", "15.0", "a reply from someone you follow back", False)], 1)
                 + "</div>",
                img(f"{ROOT}/content/ascii/xalgo-04-positives.png", "The weights worth writing for", 640),
                "Weights scale predicted probability, and a copy-link share is rare. The file never says if the 15 adds or multiplies.",
                src="content/ascii/xalgo-04-positives.png"),
    frame(7, "four dwell params",
          "Time after the tap is worth more than the tap itself.",
          hbar([("ContClickDwellTimeWeight", 0.4, True, "time after a tap"), ("ClickWeight", 0.3, False, "the tap"),
                ("DwellWeight", 0.05, False, "dwell with no tap"), ("ContDwellTimeWeight", 0.004, False, None)],
               label_w=420, value_w=380, row_h=70),
          "Four separate params. Quote 0.05 as 'time after the tap' and the advice inverts. Write the body for the 0.4.",
          src="brand/claims.md, 'Four separate dwell params, don't collapse them'",
          comment="Data: brand/claims.md X ranking weights table."),
    frame(8, "what costs you",
          "Four actions get subtracted from the score.",
          hbar([("Report", -234.0, True, None), ("Mute author", -58.8, False, None), ("Not interested", -47.52, False, None), ("Block author", -31.2, False, None)],
               label_w=340, value_w=260, row_h=72, fmt=lambda v: f"{v:g}"),
          "The file names the misreading itself: 'one report cancels 468 likes'. That's wrong, because these weights scale probabilities, not counts.",
          src="bars drawn on absolute value · brand/claims.md X ranking weights",
          comment="Data: brand/claims.md. No before/after deltas shown: those are marked unverified."),
    frame(9, "why posting more doesn't stack",
          "Five posts don't buy five slots in one person's feed.",
          '<svg width="1360" height="330" viewBox="0 0 1360 330">'
          + "".join(f'<rect x="{60+i*250}" y="{300-h}" width="170" height="{h}" fill="{ACC if i==0 else INK}" stroke="{INK}" stroke-width="3"/>'
                    f'<text x="{145+i*250}" y="{290-h}" text-anchor="middle" font-size="22" font-weight="700" fill="{INK}">{lbl}</text>'
                    for i, (h, lbl) in enumerate([(240, "best post"), (170, "decays"), (130, "decays"), (110, "decays"), (100, "floor")]))
          + f'<line x1="20" y1="300" x2="1340" y2="300" stroke="{INK}" stroke-width="3"/><line x1="20" y1="200" x2="1340" y2="200" stroke="{MUTED}" stroke-width="2" stroke-dasharray="10 8"/>'
          + f'<text x="1340" y="190" text-anchor="end" font-size="18" fill="{MUTED}">never drops to zero</text></svg>',
          "A diversity function decays your own posts against each other inside one feed response. It sorts by score, so your best post keeps its value and the weaker ones absorb the decay.",
          src="shape only · the decay values are not verified and are not shown · brand/claims.md thread row #5",
          comment="Schematic, no data. claims.md marks the self-decay curve figures as not shippable."),
    frame(10, "cold start",
          "Under 50,000 followers, a new post gets a cold start window.",
          tiles([("follower cap", "50,000", "accounts under this", False), ("impression threshold", "200", "impressions", False),
                 ("max post age", "2 hours", "7,200 seconds", True), ("feed slots", "15-16", "where it gets placed", False)], 4),
          "Every value in that file is a default. X can override any of them per experiment or per user without a release.",
          src="brand/claims.md 'Cold start: follower cap / impression threshold / max post age / feed slots'"),
    frame(11, "no levers left",
          "There is no 9am lever, no hashtag lever and no link penalty in the code.",
          '<blockquote>"We have eliminated every single hand-engineered feature and most heuristics from the system. The Grok-based transformer does all the heavy lifting by understanding your engagement history."<cite>xai-org/x-algorithm README</cite></blockquote>'
          '<div style="height:24px"></div><div class="chips"><div class="chip on">open link: +0.2</div><div class="chip">no link filter in the published code</div><div class="chip">old posts are removed, nothing resurfaces</div></div>',
          "The model reads the viewer's own history. What's left to work on is who sees the post first.",
          src="brand/claims.md thread rows #4, #6, #9 · README quote from research/video-knowledge/05"),
    frame(12, "my own account",
          "On my account, replies earned <span class=\"hl\">10x</span> the profile visits per impression of bare article links.",
          hbar([("173 replies", 22.5, True, "69 visits / 3,072 impressions"), ("4 bare article links", 2.2, False, "5 visits / 2,303 impressions")],
               label_w=360, value_w=520, row_h=84, fmt=lambda v: f"{v:g} per 1k"),
          "One week, 9 to 15 September, one account. Two weeks is not a trend. A profile visit and a follow are scored actions, and replies are where I earn them.",
          src="brand/analytics/exports/2026-09-09_2026-09-15-content.csv · brand/claims.md '@maurojpelle X analytics' · 10.2x on the rounded pair",
          comment="Data: brand/claims.md rows 'Profile visits per 1,000 impressions that week: 22.5 ... 2.2 ... 10.2x' and 'Replies carried 3,072 of 8,260 impressions and 69 of 103 profile visits'."),
    frame(13, "check any claim yourself",
          "Check any algorithm claim against the file in five minutes.",
          flow([("1", "Open param.rs", "home-mixer/params/", ""), ("2", "Search the param name", "e.g. ShareViaCopyLink", "on"),
                ("3", "Read the value and the comment", None, ""), ("4", "Check the date", "defaults move without notice", "dark")])
          + '<div style="height:28px"></div>' + slot("Search param.rs for ShareViaCopyLink live, and read the line.", short=True),
          "If a post quotes a number and the file has a different one, the file wins. If the file has no such param, the claim is that author's reading.",
          comment="Method: research/video-knowledge/05 beat 9, updated for param.rs."),
    cta_frame(14, "The formula is public and so are the defaults. Write for the time after the tap and for the share.",
              "DM me on X if you want this built into your agency's content system.", CTA_SUB,
              "Recap in two sentences. Then the CTA, qualified: established agency owners."),
]

# ================================================================ VIDEO 03 · record off a board (doc 10)

THUMBS = f"{ROOT}/research/charlie-morgan/thumbs"
V3 = [
    title_frame("Video 03 · AI content systems that book calls",
                "I stopped reading scripts on camera. I record off a board.",
                "How a board gets built in about two hours, and what broke when the build moved to an API."),
    hook_frame(
        "When you read a script on camera, people hear you reading. I build a board from the script and talk off it, and you are looking at one right now.",
        "This page scrolled top to bottom at recording speed. Then a five-second clip of me reading a scripted line [SCREEN: record it].",
        ["What a board is", "The record-ready standard", "Four hours down to two", "The four-step build", "Eight files, one order",
         "The 200-item ceiling", "The batch that failed silently", "Why stickies drift", "Diagrams written as code",
         "A 310k channel runs this format", "How corrections come back"],
        "Let the viewer notice they're watching a board while you say this."),
    frame(1, "same line, said twice",
          "Watch the same line read from a script, then said off a board.",
          '<div class="split" style="gap:40px;align-items:stretch">' + slot("Take 1: read the paragraph from a script, eyes on the text.", short=False)
          + slot("Take 2: say the same point off three labels on the board.", short=False) + "</div>",
          "Cut the two takes back to back. Say nothing about which is better. Let the difference land.",
          comment="research/video-knowledge/10 beat 1. No retention claim: nothing here measures retention."),
    split_frame(2, "what a board is",
                "One column. One beat per point. Ten to sixteen beats for an eight-minute video.",
                "",
                '<div style="display:flex;flex-direction:column;align-items:center;gap:10px">'
                + "".join(f'<div class="node{" on" if i==0 else (" dark" if i==9 else "")}" style="width:480px;flex:none;padding:12px 18px;font-size:20px">{t}</div>'
                          for i, t in enumerate(["Title + hook", "Beat 01 · talking point", "Beat 02 · chart", "Beat 03 · diagram", "Beat 04 · screen",
                                                 "Beat 05 · flow", "...", "Beat 12", "Recap", "CTA"])) + "</div>",
                "The board gets built from the script. It never replaces it. Each beat is one frame on screen.",
                src="spec: skills/youtube/miro-design-system.md"),
    frame(3, "record-ready",
          "Record-ready means nothing is missing and nothing needs a fix while the camera runs.",
          '<svg width="1360" height="200" viewBox="0 0 1360 200">'
          + "".join(f'<rect x="{i*90+4}" y="20" width="76" height="76" fill="{ACC if i<4 else "#FFFFFF"}" stroke="{INK}" stroke-width="3"/>'
                    f'<text x="{i*90+42}" y="66" text-anchor="middle" font-size="24" font-weight="800" fill="{INK}">{i+1}</text>' for i in range(15))
          + f'<text x="4" y="140" font-size="24" font-weight="800" fill="{INK}">first four are blockers: the run stops there</text>'
          + f'<text x="724" y="140" font-size="20" font-weight="600" fill="{MUTED}">checks 5 to 15: about half run as a script</text></svg>',
          "The board gate is fifteen checks, and it asks one question: can this be read to camera without stopping. Roughly half run as a script, the rest need eyes.",
          src="brand/claims.md, 'The video board system, as written up 2026-09-16'"),
    frame(4, "the time",
          "A board took <span class=\"hl\">4 hours</span> by hand. It is close to 2 now.",
          hbar([("By hand", 4, False, None), ("Now", 2, True, "close to 2")], label_w=260, value_w=420, row_h=96, fmt=lambda v: f"{v:g} hours")
          + '<div style="height:26px"></div>' + tiles([("standing", "4 boards a week", "that's why the two hours matter", False)], 1).replace('class="v"', 'class="v" style="font-size:44px"'),
          "Say 'close to two', the way it's written. Four boards a week is the standing target.",
          src="brand/claims.md: 'A board took 4 hours by hand and is close to 2 hours now' · 'Four boards a week, standing'",
          comment="Data: brand/claims.md, 'The video board system' block."),
    frame(5, "the build",
          "Four steps, and only the last one touches the board.",
          flow([("1", "Beats", "split the script, no merging", ""), ("2", "Components", "a form + colour per beat", ""),
                ("3", "Geometry", "every coordinate computed", ""), ("4", "Write", "the only step on the board", "on")]),
          "Check the beat count against the target runtime first. Text, diagrams and pasted media: real captures only.",
          src="brand/claims.md, 'The build is four steps, beats then components then geometry then write'"),
    frame(6, "eight files, one order",
          "Eight files, read in the same order every time.",
          flow([(str(i+1), t, None, "on" if t == "gotchas" else ("dark" if t == "QA" else "")) for i, t in
                enumerate(["master", "visual", "archetype", "writing", "gotchas", "assets", "diagram", "QA"])], cls="tight"),
          "The order is dependency. Font size got corrected three times before it stuck.",
          src="brand/claims.md, 'Eight files, read in the same order every time'"),
    frame(7, "the ceiling",
          "Past <span class=\"hl\">200 items</span> you can't edit or delete through the API.",
          '<svg width="1360" height="300" viewBox="0 0 1360 300">'
          f'<rect x="680" y="40" width="640" height="120" fill="{ACC}" fill-opacity=".35" stroke="{INK}" stroke-width="3"/>'
          f'<text x="1000" y="92" text-anchor="middle" font-size="26" font-weight="800" fill="{INK}">a real board: 200 to 400 items</text>'
          f'<text x="1000" y="128" text-anchor="middle" font-size="20" font-weight="600" fill="{INK}">create works · edit and delete fail</text>'
          f'<rect x="40" y="40" width="640" height="120" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>'
          f'<text x="360" y="108" text-anchor="middle" font-size="24" font-weight="700" fill="{INK}">edit and delete work</text>'
          f'<line x1="680" y1="10" x2="680" y2="200" stroke="{INK}" stroke-width="6"/>'
          f'<text x="680" y="236" text-anchor="middle" font-size="26" font-weight="900" fill="{INK}">200</text>'
          f'<text x="40" y="236" text-anchor="middle" font-size="22" font-weight="700" fill="{MUTED}">0</text>'
          f'<text x="1320" y="236" text-anchor="middle" font-size="22" font-weight="700" fill="{MUTED}">400</text>'
          f'<text x="680" y="276" text-anchor="middle" font-size="19" fill="{MUTED}">items on the board</text></svg>',
          "The edit call parses the whole board and gives up past 200. Create still works, so you get one shot, and every coordinate has to be right before you send it.",
          src="brand/claims.md: confirmed 2026-08-04 · 'A real board runs 200 to 400 items'"),
    frame(8, "the silent failure",
          "One create call: 37 items in, 17 created, and one error for the other 20.",
          stacked([("37 items in one create call", 37, [("17 created", 17, False), ("20 failed, one error", 20, True)])])
          + '<div style="height:10px"></div><div class="chips"><div class="chip on">the error named no item and no attribute</div><div class="chip">the response showed URLs for items never created</div><div class="chip">two attribute values, neither documented as invalid</div></div>',
          "That's why a batch is small whenever a line uses a value I have not written before. [NEEDS: Mauro's verdict on the rect-for-narration substitution before this beat is recorded]",
          src="brand/claims.md, 2026-08-03",
          comment="Data: brand/claims.md 'A 37-item create returned 17 created and one error covering the other 20'."),
    frame(9, "why stickies drift",
          "A sticky grows to fit its text, so a fixed row pitch drifts.",
          '<svg width="1360" height="330" viewBox="0 0 1360 330">'
          f'<text x="0" y="28" font-size="22" font-weight="800" fill="{INK}">SHAPES · explicit width and height</text>'
          + "".join(f'<rect x="{i*230}" y="46" width="200" height="90" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>' for i in range(3))
          + "".join(f'<rect x="{i*230}" y="150" width="200" height="90" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>' for i in range(3))
          + f'<text x="720" y="28" font-size="22" font-weight="800" fill="{INK}">STICKIES · one dimension, grows to fit</text>'
          + f'<rect x="720" y="46" width="180" height="90" fill="{ACC}" stroke="{INK}" stroke-width="3"/><rect x="940" y="46" width="180" height="170" fill="{ACC}" stroke="{INK}" stroke-width="3"/><rect x="1160" y="46" width="180" height="90" fill="{ACC}" stroke="{INK}" stroke-width="3"/>'
          + f'<rect x="720" y="150" width="180" height="90" fill="{ACC}" fill-opacity=".55" stroke="{INK}" stroke-width="3" stroke-dasharray="8 6"/><rect x="940" y="150" width="180" height="90" fill="{ACC}" fill-opacity=".55" stroke="#C15F3C" stroke-width="5" stroke-dasharray="8 6"/><rect x="1160" y="150" width="180" height="90" fill="{ACC}" fill-opacity=".55" stroke="{INK}" stroke-width="3" stroke-dasharray="8 6"/>'
          + f'<text x="1030" y="290" text-anchor="middle" font-size="21" font-weight="700" fill="{INK}">the next row lands on top of the grown sticky</text></svg>',
          "Shapes take an explicit width and height. A sticky takes one or the other. So every height and every gap gets computed up front.",
          src="brand/claims.md: 'A fixed row pitch computed in advance drifts when a sticky grows'"),
    split_frame(10, "diagrams written as code",
                "Diagrams get written in HTML, rendered, and pasted in as images.",
                '<div class="visual">' + flow([("", "HTML", None, ""), ("", "Headless Chrome at 2x", None, "dark"), ("", "PNG on the board", None, "on")]).replace("font-size:23px", "") + "</div>",
                img(f"{ROOT}/content/boards/content-system-video/DIAG-03-one-source.png", "One source in, nine formats out: a rendered board diagram", 560),
                "Hand-placing a diagram and prompting an image model for one are both banned. That's the default since 25 August.",
                src="content/boards/content-system-video/DIAG-03-one-source.png · rule: brand/claims.md"),
    frame(11, "the format, at scale",
          "A 310k channel runs this exact format in three of its top ten videos.",
          '<div class="split" style="grid-template-columns:repeat(3,1fr);gap:28px">'
          + img(f"{THUMBS}/04--V0q0tFzagQ.jpg", "Charlie Morgan, whiteboard framework thumbnail")
          + img(f"{THUMBS}/06-k3p1sbrWiLw.jpg", "Charlie Morgan, funnel board thumbnail")
          + img(f"{THUMBS}/07-wedx1YS-pnw.jpg", "Charlie Morgan, Miro board thumbnail") + "</div>",
          "Charlie Morgan: a hand-drawn whiteboard or a live Miro board, narrated with a facecam in the corner. Board plus facecam is a proven format at scale.",
          src="research/charlie-morgan/charlie-morgan-dig.md, thumbnails 4, 6, 7 · fetched 2026-07-16, views as scraped",
          comment="Thumbnails: research/charlie-morgan/thumbs/. Public channel, named reference confirmed in brand/claims.md 'Named references'."),
    frame(12, "how corrections come back",
          "Corrections come back as one-word comments on the board.",
          flow([("", "One-word comment", "on the item", ""), ("", "Fix pass", "pasted media never deleted", ""),
                ("", "Readiness check", "minimum image share", "on"), ("", "Record", None, "dark")]),
          "A lane can't ship as a wall of text, because the readiness check counts the images.",
          comment="research/video-knowledge/10 section 6 (observed)."),
    cta_frame(13, "Build the board from the script, then talk off it. That's the whole system.",
              "DM me on X and I'll show you how the board build runs inside a content system.", CTA_SUB,
              "Recap in two sentences, then the qualified CTA."),
]

VIDEOS = [
    ("01-claude-code-content-system.html", "Claude Code content system", V1,
     "Video 01 board. Source: research/video-knowledge/11-claude-code-content-system.md. Numbers: brand/claims.md only."),
    ("02-x-ranking-weights.html", "X ranking weights", V2,
     "Video 02 board. Source: research/video-knowledge/05-x-ranking-code.md, rebuilt on brand/claims.md 'X ranking weights, read from param.rs on 2026-10-01'."),
    ("03-record-off-a-board.html", "Record off a board", V3,
     "Video 03 board. Source: research/video-knowledge/10-record-off-a-board.md. Numbers: brand/claims.md 'The video board system'."),
]

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main():
    for fname, title, frames, comment in VIDEOS:
        path = os.path.join(HERE, fname)
        with open(path, "w") as f:
            f.write(page(title, comment, frames))
        print("wrote", path, f"({len(frames)} frames)")
        if "--png" in sys.argv:
            h = len(frames) * FRAME_H
            png = path.replace(".html", ".png")
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000",
                            f"--screenshot={png}", f"--window-size=1600,{h}", "file://" + path],
                           check=True, capture_output=True)
            print("rendered", png)


if __name__ == "__main__":
    main()
