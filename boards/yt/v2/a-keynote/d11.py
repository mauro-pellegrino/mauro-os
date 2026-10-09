"""Doc 11, the flagship: the Claude Code content system. Keynote format.
Every number on a frame is from brand/claims.md ("The content system, as published 2026-09-10"
and "Mauro's own operation"). Anything else renders as a red [NEEDS] tag."""
from engine import B, needs, hd, vis, agenda, flow, squares, vbars, hbars, INK, ACC, SOFT, RED, MUTED

SLUG = "11-claude-code-content-system"
DOC = "11"
SOURCES = ("research/video-knowledge/11-claude-code-content-system.md, "
           "research/video-knowledge/assets/repo-tree-screen-safe.txt, brand/claims.md "
           "(published-article block and the 150 booked calls row)")

AG = ["The map", "The agents", "The rules"]

TREE = """repo/
├── <span class="r" data-h="1">skills/                 73 markdown files, split by activity</span>
│   ├── content/        <em>long-form, short-form, x-articles/</em>
│   ├── research/       <em>weekly research, breakdowns</em>
│   ├── ops/            <em>daily ops, content loop, monday</em>
│   ├── miro/  lead-gen/  youtube/
│   └── creative-strategy/  dm-setting/
├── <span class="r" data-h="2">.claude/agents/         4 installed agents</span>
├── ops/
│   ├── <span class="r" data-h="3">MAP.md                the index</span>
│   ├── CONVENTIONS.md    <em>nine rules</em>
│   └── <span class="r" data-h="4">tools/                25 scripts</span>
├── research/  acquisition-calls/  outbound-calls/
├── accounts/            <em>[REDACTED]</em>
└── BACKLOG.md"""

AREAS = ["skills/", ".claude/agents/", "ops/", "research/", "accounts/", "acquisition-calls/",
         "outbound-calls/", "emails/", "brands/", "recaps/", "future-projects/"]


def areas_map():
    # 11 boxes around a central MAP.md, as SVG
    import math
    cx, cy, R = 690, 300, 270
    out = [f'<svg width="1380" height="610" viewBox="0 0 1380 610">']
    pts = []
    for k, a in enumerate(AREAS):
        ang = -math.pi / 2 + k * 2 * math.pi / 11
        x, y = cx + R * 2.0 * math.cos(ang), cy + R * math.sin(ang)
        pts.append((x, y))
    out.append('<g data-s="2">')
    for x, y in pts:
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{ACC}" stroke-width="5"/>')
    out.append(f'<rect x="{cx-120}" y="{cy-46}" width="240" height="92" fill="{INK}"/>'
               f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="34" font-weight="900" fill="{ACC}" class="m">MAP.md</text></g>')
    out.append('<g data-s="1">')
    for (x, y), a in zip(pts, AREAS):
        out.append(f'<rect x="{x-120:.0f}" y="{y-30:.0f}" width="240" height="60" fill="#fff" stroke="{INK}" stroke-width="4"/>'
                   f'<text x="{x:.0f}" y="{y+9:.0f}" text-anchor="middle" font-size="21" font-weight="800" fill="{INK}" class="m">{a}</text>')
    out.append("</g></svg>")
    return "".join(out)


def loop4(labels, steps=True):
    # square loop of four nodes
    pos = [(690, 70), (1130, 300), (690, 530), (250, 300)]
    out = ['<svg width="1380" height="600" viewBox="0 0 1380 600">',
           f'<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>']
    arcs = [((850, 90), (1130, 230)), ((1130, 370), (850, 515)), ((530, 515), (250, 370)), ((250, 230), (530, 90))]
    for k, ((x, y), lab) in enumerate(zip(pos, labels)):
        s = f' data-s="{k+1}"' if steps else ""
        (x1, y1), (x2, y2) = arcs[k]
        fill = ACC if k == 0 else "#fff"
        out.append(f'<g{s}><rect x="{x-160}" y="{y-44}" width="320" height="88" fill="{fill}" stroke="{INK}" stroke-width="4"/>'
                   f'<text x="{x}" y="{y+12}" text-anchor="middle" font-size="32" font-weight="900" fill="{INK}">{lab}</text>'
                   f'<path d="M{x1},{y1} Q{(x1+x2)/2 + (60 if k in (0,3) else -60) * (1 if k==0 else 1)},{(y1+y2)/2 + (-40 if k in (0,3) else 40)} {x2},{y2}" fill="none" stroke="{INK}" stroke-width="5" marker-end="url(#ah)"/></g>')
    out.append("</svg>")
    return "".join(out)


def contained(agents, outside, needs_tag=None):
    out = ['<svg width="1380" height="560" viewBox="0 0 1380 560">',
           f'<rect x="10" y="20" width="820" height="520" fill="none" stroke="{INK}" stroke-width="5"/>',
           f'<text x="40" y="70" font-size="26" font-weight="800" fill="{MUTED}" class="m">THE REPO</text>']
    for k, a in enumerate(agents):
        x, y = 60 + (k % 2) * 390, 110 + (k // 2) * 210
        out.append(f'<g data-s="1"><rect x="{x}" y="{y}" width="350" height="170" fill="{INK}"/>'
                   f'<text x="{x+175}" y="{y+96}" text-anchor="middle" font-size="27" font-weight="800" fill="#fff" class="m">{a}</text></g>')
    out.append(f'<g data-s="2"><line x1="840" y1="280" x2="1060" y2="280" stroke="{RED}" stroke-width="6" stroke-dasharray="16 12"/>'
               f'<text x="950" y="250" text-anchor="middle" font-size="60" font-weight="900" fill="{RED}">&#215;</text>'
               f'<circle cx="1200" cy="250" r="70" fill="{SOFT}"/><rect x="1110" y="330" width="180" height="120" rx="60" fill="{SOFT}"/>'
               f'<text x="1200" y="505" text-anchor="middle" font-size="28" font-weight="800" fill="{INK}" class="m">{outside}</text></g>')
    out.append("</svg>")
    return "".join(out)


def slides():
    S = []

    def add(name, html, dur, notes, onscreen="", cls=""):
        S.append({"name": name, "html": html, "dur": dur, "notes": notes, "onscreen": onscreen, "cls": cls})

    # ---------------- HOOK
    add("hook, the result",
        '<div style="display:flex;flex-direction:column;justify-content:center;height:100%">'
        + B('<div class="giant y">150+</div>', s=None)
        + B('<div class="glabel cnt" style="margin-top:40px">qualified booked calls in 2026</div>', s=1)
        + B('<div class="cite" style="margin-top:22px">SOURCE: CALENDLY EXPORT &middot; THE AGENCY I RUN</div>', s=2)
        + "</div>", 15,
        ["Open on the number, nothing else on screen. Say it straight: this year I generated over 150 qualified booked calls for the agency I run.",
         "Build 1, the label. Build 2, the source line: it comes off the Calendly export.",
         "Do not say the 150 came from X or LinkedIn. The Calendly data does not carry the channel, and a viewer who reads the article will check.",
         "Then the turn: the content behind that runs out of one Claude Code repo, and nobody who says they built a system in Claude Code ever opens the repo. I am going to open mine."],
        onscreen="One giant honey number, 150+, on the dark ground. Label and source build in.", cls="dark")
    add("hook, the promise and the list",
        hd("Today:") + vis(agenda(AG, steps=True)), 15,
        ["The promise: by the end you have the whole structure, the four agents and the rules that keep it honest, and you can copy the shape into your own agency.",
         "Build each card as you name it. One, the map: how the repo is laid out and why it is split the way it is.",
         "Two, the agents: four of them, and the incident behind each one.",
         "Three, the rules: how every number traces back to a script, and the claim that measured backwards."],
        onscreen="Three cards build in: The map, The agents, The rules.")

    # ---------------- SECTION 1: THE MAP
    add("section 1 card", vis(agenda(AG, live=1)), 15,
        ["Part one, the map. Start with the shape, because the prompts are the least interesting part of the whole thing."],
        onscreen="Agenda with card 1 live.")
    add("eleven areas, one map",
        hd("Eleven areas. <em>One map.</em>") + vis(areas_map(), style="top:220px"), 75,
        ["Build 1: eleven top-level areas. Name a few as they land: skills, the agents, ops, research, the weekly acquisition calls, outbound.",
         "Each area has an owner and an entry point.",
         "Build 2: every one of them is indexed in one file, ops/MAP.md. That file is the thing an agent reads first.",
         "The accounts folder exists but its contents never go on camera. Say: one folder per account, names redacted."],
        onscreen="Eleven folder boxes in a ring, then honey lines into a dark MAP.md box in the middle.")
    add("the repo, opened",
        hd("Here it is. <em>Open.</em>", "sm") + vis(f'<pre class="tree">{TREE}</pre>', style="top:190px"), 75,
        ["This is the screen-safe tree. Account names are redacted on purpose.",
         "Build 1 lights skills: 73 markdown files, split by activity. Build 2 lights the agents folder: four installed.",
         "Build 3 lights MAP.md, the index. Build 4 lights tools: 25 scripts, one per number anyone cites.",
         "These are the counts as published in the article. Live counts drift, so say 'when I published this' and re-count on the day if you want a fresh number."],
        onscreen="The redacted repo tree on a dark panel. Four rows light up honey one by one.")
    add("route it or it gets rebuilt",
        hd("Route it or it gets <em>rebuilt.</em>")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:34px">'
              + B('<div class="panel"><div class="lab">Before</div>'
                  + flow([("new SOP", "", None), ("missing from MAP.md", "bad", None), ("next agent rebuilds it", "bad", None)], [("&rarr;", "r"), ("&rarr;", "r")])
                  + f'<div style="margin-top:16px">{needs("time lost on the rebuild, doc says 45 minutes, not in claims.md")}</div></div>', s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After</div>'
                  + flow([("new SOP", "", None), ("routed in MAP.md", "y", None), ("next agent finds it", "dk", None)])
                  + "</div>", s=2)
              + "</div>", style="top:230px"), 78,
        ["The rule that holds the repo together: work is not finished until it is routed.",
         "Build 1, the before. A thing that exists and is not in the map gets rebuilt by the next agent. That happened with an outbound SOP: an agent rebuilt it from scratch.",
         "The doc says that rebuild cost 45 minutes. That figure is not in claims.md, so it stays off the frame until you sign it off. Say 'a chunk of an afternoon' only if you remember it that way.",
         "Build 2, the after. The SOP is routed in MAP.md, and the next agent reads the map first and finds it.",
         "This is the worked example for part one: one rule, written the day it failed."],
        onscreen="Before panel: three boxes, two red. After panel: the same three boxes, routed. A red NEEDS tag on the lost time.")
    add("73 skill files",
        '<div style="display:grid;grid-template-columns:620px 1fr;gap:60px;height:100%;align-items:center">'
        + '<div><div class="giant md">73</div>' + B('<div class="glabel cnt" style="margin-top:30px">skill files. Eight folders.</div>', s=1) + "</div>"
        + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">'
        + "".join(B(f'<div class="nd" style="min-height:96px;font-size:26px">{f}/</div>', s=2 + k // 2) for k, f in enumerate(
            ["content", "research", "ops", "miro", "lead-gen", "youtube", "creative-strategy", "dm-setting"]))
        + "</div></div>", 60,
        ["73 markdown skill files across eight folders. Each file owns one job.",
         "Build the folders two at a time: content and research, ops and miro, lead-gen and youtube, creative-strategy and dm-setting.",
         "Every folder is an activity. There is no folder per client anywhere in skills, and the next frame is why."],
        onscreen="Giant 73 on the left. Eight folder tiles build in pairs on the right.")
    add("split by activity",
        hd("One folder <em>per activity.</em>")
        + vis('<div class="split">'
              + B('<div class="panel"><div class="lab">By client</div>'
                  + '<pre class="code" style="font-size:22px">client-a/<span class="add">titles.md</span>\n'
                  + '<span class="del">client-b/titles.md</span>  <em>client left</em>\nclient-c/<span class="add">titles.md</span>  <em>rebuilt again</em></pre></div>', s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">By activity</div>'
                  + '<pre class="code" style="font-size:22px">youtube/<span class="add">titles.md</span>\n\n<em>one file, every client</em>\n<em>survives every churn</em></pre></div>', s=2)
              + "</div>", style="top:240px"), 75,
        ["Before and after for the folder split.",
         "Build 1: split by client and a client folder rots when the client leaves. The same skill gets rebuilt inside the next client's folder, slightly different, and now you have two versions that disagree.",
         "Build 2: split by activity and the skill survives every client. One titles file, corrected once, used everywhere.",
         "The client folders here are labelled A, B and C on purpose. No real names on screen."],
        onscreen="Left panel: three client folders with duplicate files, one struck through. Right panel: one activity folder, one file.")
    add("worked example, the article set",
        hd("One transcript in. <em>One article out.</em>", "sm")
        + vis('<div style="width:100%">'
              + flow([("subject<small>skill 1</small>", "", 1), ("first screen<small>skill 2</small>", "", 2), ("title<small>skill 3</small>", "", 3),
                      ("cover<small>skill 4</small>", "", 4), ("body<small>skill 5</small>", "", 5), ("post + keyword<small>skill 6</small>", "y", 6)])
              + B(f'<div style="margin-top:46px;display:flex;gap:30px;align-items:stretch">'
                  f'<div class="nd dk" style="flex:2">keeps the six honest<small>skill 7</small></div>'
                  f'<div class="ar">&larr;</div><div class="nd" style="flex:2">one corpus file<small>41 real captures</small></div></div>', s=7)
              + "</div>", style="top:220px"), 78,
        ["Open skills/content/x-articles on camera. This is the worked example for part one.",
         "Six skills in a fixed order. Build them one by one: the subject first, then the first screen, which is cover, title and first lines as one unit, then the title, the cover, the body, and last the companion post with its keyword.",
         "Order matters. Subject before title. Title and cover together. Body last.",
         "Build 7: the seventh file's only job is keeping the other six honest as evidence lands. Every number the set cites lives in one corpus file read from 41 real captures."],
        onscreen="Six skill boxes build left to right, then skill 7 and the 41-capture corpus below.")
    add("the monday loop",
        hd("Every Monday, <em>the loop closes.</em>", "sm")
        + vis(loop4(["performance", "review", "hypothesis", "implementation"]), style="top:200px"), 75,
        ["The weekly shape. Every Monday the acquisition analysis runs, then the content loop.",
         "Build it round the loop: last week's performance, the review, one hypothesis, the implementation, and back to performance next Monday.",
         "Everything else in the repo is a file that this loop reads or writes.",
         "The doc gives a count of inputs and sections for the Monday analysis. Those counts are not in claims.md, so leave them out of narration until signed off."],
        onscreen="Four boxes in a loop with arrows. Performance in honey.")

    # ---------------- SECTION 2: THE AGENTS
    add("section 2 card", vis(agenda(AG, live=2)), 15,
        ["Part two, the agents. An agent runs without being asked. All four of these exist because something was missed."],
        onscreen="Agenda with card 2 live.")
    add("four agents",
        '<div style="display:grid;grid-template-columns:520px 1fr;gap:60px;height:100%;align-items:center">'
        + '<div><div class="giant">4</div>' + B('<div class="glabel cnt" style="margin-top:20px">agents. Each one a scar.</div>', s=1) + "</div>"
        + '<div style="display:flex;flex-direction:column;gap:16px">'
        + "".join(B(f'<div class="nd dk mono" style="min-height:90px;font-size:28px">{a}</div>', s=2 + k) for k, a in enumerate(
            ["performance-loop", "signal-sweep", "board-qa", "youtube-lead-magnet"]))
        + "</div></div>", 60,
        ["Four installed agents. Build their names in.",
         "Every one of them is defensive. It catches a drop, catches a missed ask, gates a board, or packages an asset.",
         "The next four frames are one incident each. This is the most quotable part of the video: every agent is a scar."],
        onscreen="Giant 4 on the left, four agent names build in on the right.")
    add("performance-loop, the 64%",
        hd("64% gone. <em>Nobody noticed.</em>")
        + vis('<div style="display:grid;grid-template-columns:1fr 520px;gap:50px;align-items:center;width:100%">'
              + vbars([("June", 100, INK, None, "100"), ("August", 36, RED, 1, "36")], w=760, h=500)
              + '<div style="display:flex;flex-direction:column;gap:22px">'
              + B('<div class="panel"><div class="lab">Before</div><div style="font-size:40px;font-weight:900;color:#C0392B">2 months unseen</div></div>', s=2)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After</div><div style="font-size:40px;font-weight:900;color:#1B4332">flagged every week</div></div>', s=3)
              + '<div class="cite">monthly impressions, June = 100</div></div></div>', style="top:230px"), 78,
        ["performance-loop. Monthly impressions fell 64% between June and August 2026, and nobody noticed for two months.",
         "Build 1: the August bar. June is indexed to 100 so the drop reads at a glance. The chart shows the percentage. Raw impressions stay off the frame.",
         "Build 2, the before: two months with nobody looking. Build 3, the after: the agent consolidates the exports every week and flags a drop before it becomes a quarter.",
         "It reports numbers with caveats and never calls one month a trend."],
        onscreen="Two bars, June 100 and August 36 in red. Before and after panels build on the right.")
    add("signal-sweep, the buried ask",
        hd("The ask was in a <em>group DM.</em>", "sm")
        + vis('<div class="split" style="align-items:center">'
              + '<div style="display:flex;flex-direction:column;gap:12px">'
              + "".join(f'<div class="nd" style="min-height:62px;font-size:22px;justify-content:center;align-items:flex-start;padding:12px 20px">{c}</div>'
                        for c in ["#channel", "#channel", "call transcript"])
              + B('<div class="nd bad" style="min-height:62px;font-size:22px;align-items:flex-start;padding:12px 20px">group DM &middot; missed</div>', s=1)
              + "</div>"
              + B('<div style="display:flex;flex-direction:column;gap:14px">'
                  + flow([("read every channel", "dk", None)]) + '<div class="ar" style="width:auto">&darr;</div>'
                  + flow([("diff vs recorded", "", None)]) + '<div class="ar" style="width:auto">&darr;</div>'
                  + flow([("persist the ask", "y", None)]) + "</div>", s=2)
              + "</div>", style="top:220px"), 75,
        ["signal-sweep. A catch-up missed a two-message group DM that held the one number the whole YouTube cadence was tied to.",
         "Worse, the catch-up presented an auto-generated queue as if it were the client's priorities.",
         "Build 1 lights the missed DM in red. The channel unread counts on screen are illustrative UI, say nothing about them.",
         "Build 2: now the agent reads every channel and every call transcript, diffs what it finds against what is already recorded, and persists the durable asks.",
         "Do not say the target number the DM held. It is not cleared."],
        onscreen="A mock inbox list with one red group DM row. Then a three-step sweep: read, diff, persist.")
    add("board-qa, fifteen checks",
        hd("Can this be read <em>to camera?</em>")
        + vis('<div style="width:100%">'
              + squares(15, 15, lambda k: "y" if k < 4 else "g", s_map=lambda k: 1 if k < 4 else 2)
              + '<div style="display:flex;justify-content:space-between;margin-top:20px">'
              + B('<span class="cite">CHECKS 1-4: BLOCKERS</span>', s=1) + B('<span class="cite">CHECKS 5-15</span>', s=2) + "</div></div>", style="top:260px"), 60,
        ["board-qa. Boards were going out so full that nobody could record off them.",
         "It answers one question through fifteen checks: can this be read to camera without stopping.",
         "Build 1, the first four: they are blockers, and if one fails the run stops there. Build 2, the other eleven.",
         "Roughly half the checks run as a script and the rest need eyes."],
        onscreen="Fifteen squares. The first four in honey, then the other eleven in forest.")
    add("youtube-lead-magnet, no drift",
        hd("Read the skill fresh. <em>Every run.</em>", "sm")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:34px">'
              + B('<div class="panel"><div class="lab">Before</div>' + flow([("run 1", "", None), ("run 2", "", None), ("run 3", "bad", None)], [("&rarr;", ""), ("&rarr;", "r")])
                  + "</div>", s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After</div>'
                  + flow([("the skill file", "y", None), ("run 1", "dk", None), ("run 2", "dk", None), ("run 3", "dk", None)])
                  + "</div>", s=2)
              + "</div>", style="top:220px"), 50,
        ["youtube-lead-magnet. The problem was packaging drift.",
         "Build 1: each run copied what the last run did, and the package wandered away from the skill.",
         "Build 2: the agent's first instruction is to run the existing skill and never invent rules. Every run starts from the file."],
        onscreen="Before: three runs in a chain, the last in red. After: one skill file feeding every run.")
    add("every agent is a scar",
        hd("Every agent is <em>a scar.</em>")
        + vis('<table class="tb">'
              + "".join(B(f"<td>{a}</td><td>{b}</td>", s=k + 1, tag="tr") for k, (a, b) in enumerate([
                  ("performance-loop", "a reach drop nobody saw"),
                  ("signal-sweep", "an ask lost in a DM"),
                  ("board-qa", "boards nobody could record"),
                  ("youtube-lead-magnet", "packaging drift")]))
              + "</table>", style="top:240px"), 45,
        ["The recap table for part two. Build the four rows.",
         "None of these was planned as a feature. Each one was installed after something was missed. Two of the four went in after a miss that cost real time.",
         "Say plainly that the system is not finished."],
        onscreen="A four-row table: agent name, the miss behind it.")

    # ---------------- SECTION 3: THE RULES
    add("section 3 card", vis(agenda(AG, live=3)), 15,
        ["Part three, the rules. This is what keeps a repo like this honest when an agent writes into it every day."],
        onscreen="Agenda with card 3 live.")
    add("25 scripts",
        '<div style="display:grid;grid-template-columns:600px 1fr;gap:60px;height:100%;align-items:center">'
        + '<div><div class="giant md">25</div>' + B('<div class="glabel cnt" style="margin-top:30px">scripts. One per number.</div>', s=1) + "</div>"
        + B('<pre class="code" style="font-size:25px">ops/tools/\n  impressions-vs-calls.py\n  consolidate-exports.py\n  post-to-call.py\n  trace-bookings.py\n'
            '  call-structure.py\n  article-title-features.py\n  lane-tables.py\n  <em>... 25 in total</em></pre>', s=2)
        + "</div>", 60,
        ["25 Python scripts in ops/tools. Build 2 opens the folder listing.",
         "The convention behind them: the analysis that produced a number gets saved as a script.",
         "An inline calculation is lost at the next context clear. Then somebody re-derives it slightly differently, and the two numbers disagree in a meeting."],
        onscreen="Giant 25, then the tools folder listing in a code panel.")
    add("worked example, the limit",
        hd("The script states <em>its own limit.</em>", "sm")
        + vis('<div style="width:100%;display:grid;grid-template-columns:1fr 560px;gap:40px;align-items:center">'
              + hbars([("Calendly rows", 678, SOFT, None, "678"), ("under one owner", 649, INK, 1, "649"), ("UTM field empty", 673, RED, 2, "673")],
                      w=820, label_w=300, row_h=110)
              + B('<pre class="code" style="font-size:26px">"""\n<span class="add">MEASURES ALL INBOUND,</span>\n<span class="add">NOT ONE ACCOUNT.</span>\n<em>649 of 678 rows sit</em>\n<em>under one owner.</em>\n"""</pre>', s=3)
              + "</div>", style="top:220px"), 78,
        ["The worked example for part three. Every script states its own limit in its opening lines.",
         "One tool was named as if it measured a single account's bookings.",
         "Build 1: 649 of 678 Calendly rows sit under one owner. Build 2: the UTM field is empty on 673 of them.",
         "So it measures all inbound. Build 3: the docstring now says so in capitals. That is the before and after: a name that implied one thing, and a header that states the truth."],
        onscreen="Three horizontal bars: 678, 649, 673 in red. Then a docstring in capitals.")
    add("four rules carry the weight",
        hd("Nine rules. <em>Four carry the weight.</em>", "sm")
        + vis('<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px;width:100%">'
              + "".join(B(f'<div class="nd {c}" style="min-height:330px;font-size:34px">{a}<small>{b}</small></div>', s=k + 1)
                        for k, (a, b, c) in enumerate([("tag", "every claim", "dk"), ("trace", "number to script", "dk"),
                                                     ("limit", "every script", "dk"), ("date", "every decision", "y")]))
              + "</div>", style="top:240px"), 75,
        ["Nine conventions in CONVENTIONS.md. Four carry the weight. Build them one at a time.",
         "Tag: every claim carries an evidence tag, measured, observed or assumed.",
         "Trace: every number traces to a script and a dataset. Limit: every script declares its own limit.",
         "Date: decisions are dated lines in the file whose behaviour they govern."],
        onscreen="Four tall cards: tag, trace, limit, date.")
    add("the claim that measured backwards",
        hd("It felt <em>obviously true.</em>")
        + vis('<div style="display:grid;grid-template-columns:1fr 500px;gap:40px;align-items:center;width:100%">'
              + vbars([("worked example", 60000, RED, 1, "60,000"), ("winning section", 264000, INK, 2, "264,000")], w=820, h=500)
              + B('<pre class="code" style="font-size:22px"><span class="del">the worked example</span>\n<span class="del">is the section</span>\n<span class="del">that converts</span>\n\n<span class="add">[measured]</span></pre>', s=3)
              + "</div>", style="top:220px"), 78,
        ["The reason for the tags, in one example.",
         "A skill asserted that the worked example was the section that converts. It had felt obviously true.",
         "Build 1 and 2: measured, the worked example did 60,000 against the winning section's 264,000. The opposite direction.",
         "Build 3: the line comes out of the skill, and the replacement carries a measured tag. That is the before and after for the convention."],
        onscreen="Two bars: 60,000 in red against 264,000. Then the struck-through skill line and a measured tag.")
    add("the gotchas file",
        hd("Every failure gets <em>written down.</em>", "sm")
        + vis('<div style="display:grid;grid-template-columns:560px 1fr;gap:60px;align-items:center;width:100%">'
              + '<div>' + squares(37, 8, lambda k: "g" if k < 17 else "r", s_map=lambda k: 1 if k < 17 else 2)
              + B('<div class="cite" style="margin-top:14px">37 items sent &middot; 17 created &middot; 20 failed</div>', s=2) + "</div>"
              + B('<div class="panel"><div class="lab">Miro API</div><div style="font-size:120px;font-weight:900;color:#1B4332;line-height:.9">200</div>'
                  '<div class="cite" style="margin-top:12px">item ceiling</div></div>', s=3)
              + "</div>", style="top:220px"), 75,
        ["skills/miro has a gotchas file that exists entirely because of things that broke.",
         "Build 1 and 2: one bad attribute silently failed 20 of 37 board items, with no useful error.",
         "Build 3: past 200 items the API cannot edit or delete anything. Creating still works.",
         "Both are written down now, so no agent hits them twice."],
        onscreen="A grid of 37 squares, 17 forest then 20 red. Then a panel with 200.")
    add("what it cannot do",
        hd("None of it reaches <em>a human.</em>")
        + vis(contained(["performance-loop", "signal-sweep", "board-qa", "yt-lead-magnet"], "a prospect"), style="top:230px"), 60,
        ["What this system does not do: it does not book calls on its own.",
         "Build 1: every installed agent sits inside the repo and is defensive. Build 2: nothing in the repo today reaches out to a human.",
         "Say it without hedging: it runs the content behind the calls. Keep every revenue figure off camera.",
         "That gap is the subject of the next video. Tease it in one line."],
        onscreen="Four dark agent boxes inside a box marked the repo. A red dashed line with a cross to a figure marked a prospect.")
    add("CTA",
        '<div class="cta"><div class="big">Link in the description</div><div class="offer">Agency Booked Calls</div></div>', 45,
        ["If you run an established agency and want this installed for your own inbound, the link is in the description. It is called Agency Booked Calls.",
         "Everyone else: tell me in the comments which part of the repo you want opened next.",
         "No price on screen and no URL."],
        onscreen="Dark frame: Link in the description, and the offer name in honey.", cls="dark")
    return S


TITLES = [
    {"title": "My Claude Code Content System (150+ Booked Calls)",
     "modelled_on": "01-outliers.csv, Jordan Platten, 'I Let Claude AI Get Me Clients for 30 Days (240 Meetings Booked)', 39k: result in brackets after the claim"},
    {"title": "73 Claude Code Skills That Run an Agency's Inbound",
     "modelled_on": "01-outliers.csv, Liam Ottley, 'The 8 AI Skills That Will Separate Winners From Losers in 2025', 1.6M: a number of skills up front"},
    {"title": "Build Your Content Engine With Claude Code: Here's How",
     "modelled_on": "01-outliers.csv, David Ondrej, 'Build Everything with AI Agents: Here's How', 1.7M: build X with tool, here's how"},
]

NEEDS = ["time lost on the rebuilt SOP (doc says 45 minutes, not in claims.md)",
         "the revenue figure for the title ($100k/mo, $150k MRR, ~$500k total are all uncleared; none used)"]

THUMBS = [
    # T1: the result
    """<div class="thumb" style="background:#1B4332">
      <div style="position:absolute;left:70px;top:60px;font:800 30px 'JetBrains Mono',monospace;letter-spacing:6px;color:#E9B949">CLAUDE CODE</div>
      <div style="position:absolute;left:58px;top:120px;font-size:330px;font-weight:900;letter-spacing:-18px;color:#E9B949;line-height:1">150+</div>
      <div style="position:absolute;left:70px;bottom:70px;font-size:110px;font-weight:900;color:#fff;letter-spacing:-4px">CALLS</div>
      <div class="face">FACE</div></div>""",
    # T2: the repo
    """<div class="thumb" style="background:#F7F3EA">
      <pre style="position:absolute;left:50px;top:50px;width:720px;height:470px;background:#0E2418;color:#EAF2EC;font:600 25px/1.5 'JetBrains Mono',monospace;padding:30px 34px;overflow:hidden;border:6px solid #1B4332">repo/
├── <b style="background:#E9B949;color:#0E2418">skills/       73 files</b>
│   ├── content/
│   ├── research/
│   ├── ops/
│   └── youtube/
├── <b style="background:#E9B949;color:#0E2418">.claude/agents/  4</b>
├── ops/MAP.md
└── ops/tools/   25</pre>
      <div style="position:absolute;left:120px;top:540px;background:#E9B949;border:6px solid #1B4332;padding:6px 26px;font-size:104px;white-space:nowrap;font-weight:900;color:#1B4332;letter-spacing:-5px;transform:rotate(-4deg)">WHOLE REPO</div>
      <div class="face">FACE</div></div>""",
    # T3: four scars
    """<div class="thumb" style="background:#0E2418">
      <div style="position:absolute;left:70px;top:70px;font-size:420px;font-weight:900;color:#E9B949;line-height:.85;letter-spacing:-20px">4</div>
      <div style="position:absolute;left:330px;top:120px;display:grid;grid-template-columns:1fr 1fr;gap:16px;width:420px">
        <i style="height:150px;background:#1B4332;border:5px solid #E9B949"></i><i style="height:150px;background:#1B4332;border:5px solid #E9B949"></i>
        <i style="height:150px;background:#1B4332;border:5px solid #E9B949"></i><i style="height:150px;background:#C0392B;border:5px solid #E9B949"></i></div>
      <div style="position:absolute;left:70px;bottom:60px;font-size:88px;font-weight:900;color:#fff;letter-spacing:-3px;line-height:1">AGENTS, 4 SCARS</div>
      <div class="face" style="height:520px">FACE</div></div>""",
]
