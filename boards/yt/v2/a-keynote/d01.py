"""Doc 01: skills to agents, what broke. Keynote format.
Cleared numbers: 73 skill files across eight folders, four agents (claims.md, published article).
The doc's 30 minutes a day, the 221-view / 22.2% statistic, the 1,000-view floor and the 'two months'
of wrong end-of-day reports are not in claims.md and render as red [NEEDS] tags.
claims.md 2026-10-07: 185 Google Tasks pushed, 0 ticked. That contradicts the doc's 'fixed' story,
so the fix is shown as unproven, with a sign-off tag."""
from engine import B, needs, hd, vis, agenda, flow, squares, vbars, hbars, INK, ACC, SOFT, RED, MUTED

SLUG = "01-skills-to-agents"
DOC = "01"
SOURCES = ("research/video-knowledge/01-skills-to-agents.md, research/transcripts/maurojpelle/installing-agents-what-changed-what-broke.md, "
           "brand/claims.md (published-article block, Mauro's own system 2026-10-07)")

AG = ["The skill", "The agent", "What broke"]


def hub():
    tools = ["Notion", "tl;dv", "Drive", "Slack"]
    out = ['<svg width="1380" height="560" viewBox="0 0 1380 560">',
           f'<defs><marker id="a3" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>']
    for k, t in enumerate(tools):
        y = 40 + k * 130
        out.append(f'<g data-s="{k+1}"><rect x="20" y="{y}" width="300" height="96" fill="#fff" stroke="{INK}" stroke-width="4"/>'
                   f'<text x="170" y="{y+60}" text-anchor="middle" font-size="36" font-weight="900" fill="{INK}">{t}</text>'
                   f'<path d="M320,{y+48} L560,280" stroke="{INK}" stroke-width="4" fill="none" marker-end="url(#a3)"/></g>')
    out.append(f'<g data-s="5"><rect x="570" y="210" width="300" height="140" fill="{INK}"/>'
               f'<text x="720" y="292" text-anchor="middle" font-size="36" font-weight="900" fill="{ACC}" class="m">agent</text>'
               f'<path d="M870,280 L1010,280" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/></g>')
    out.append(f'<g data-s="6"><rect x="1020" y="120" width="340" height="320" fill="#fff" stroke="{INK}" stroke-width="4"/>'
               f'<text x="1190" y="165" text-anchor="middle" font-size="24" font-weight="800" fill="{MUTED}" class="m">CALENDAR</text>')
    for k in range(4):
        out.append(f'<rect x="1045" y="{190+k*60}" width="{290 - (k%2)*80}" height="44" fill="{ACC if k==1 else SOFT}"/>')
    out.append("</g></svg>")
    return "".join(out)


def grow():
    # the file grows as corrections land: a stack that gets taller, no values
    out = ['<svg width="1380" height="520" viewBox="0 0 1380 520">',
           f'<line x1="40" y1="460" x2="1340" y2="460" stroke="{INK}" stroke-width="4"/>']
    hs = [80, 140, 200, 260, 330, 400]
    for k, h in enumerate(hs):
        x = 80 + k * 210
        out.append(f'<g data-s="{k+1}"><rect x="{x}" y="{460-h}" width="150" height="{h}" fill="{ACC if k==5 else INK}"/>'
                   + "".join(f'<rect x="{x+18}" y="{460-h+20+j*30}" width="{114 - (j%3)*20}" height="10" fill="{"#1B4332" if k==5 else "#7FA08C"}"/>'
                             for j in range(int((h-30)/30)))
                   + f'<text x="{x+75}" y="500" text-anchor="middle" font-size="24" font-weight="800" fill="{MUTED}" class="m">fix {k+1}</text></g>')
    out.append("</svg>")
    return "".join(out)


def slides():
    S = []

    def add(name, html, dur, notes, onscreen="", cls=""):
        S.append({"name": name, "html": html, "dur": dur, "notes": notes, "onscreen": onscreen, "cls": cls})

    # ---------------- HOOK
    add("hook, the result",
        '<div style="display:flex;align-items:center;justify-content:center;gap:50px;height:100%">'
        + '<div style="text-align:center"><div class="giant md y">73</div><div class="cite" style="font-size:24px;margin-top:14px">SKILL FILES</div></div>'
        + B('<div style="font-size:160px;font-weight:900;color:#fff">&rarr;</div>', s=1)
        + B('<div style="text-align:center"><div class="giant md y">4</div><div class="cite" style="font-size:24px;margin-top:14px">AGENTS</div></div>', s=1)
        + "</div>"
        + B('<div class="glabel cnt" style="position:absolute;left:0;right:0;bottom:90px;text-align:center">and writing still stays with me.</div>', s=2), 15,
        ["Result first. 73 skill files, and on top of them four agents that run without being asked.",
         "Build 2: and the writing still stays a skill, on purpose. That is the bit nobody telling you to switch to agents will say.",
         "This migration is still in progress. Say so in the first thirty seconds."],
        onscreen="73, an arrow, 4, on the dark ground. Then: and writing still stays with me.", cls="dark")
    add("hook, the promise and the list",
        hd("Today:") + vis(agenda(AG, steps=True)), 15,
        ["The promise: by the end you know which jobs to hand to an agent, which to keep, and what it costs you when it goes wrong.",
         "Build the cards. One, the skill: what it is and why it compounds. Two, the agent: what it adds. Three, what broke, all of it, nothing softened."],
        onscreen="Three cards build in: The skill, The agent, What broke.")

    # ---------------- SECTION 1: THE SKILL
    add("section 1 card", vis(agenda(AG, live=1)), 15,
        ["Part one, the skill. Start where most of you are right now."], onscreen="Agenda with card 1 live.")
    add("where it started",
        hd("Where it started: <em>one endless chat.</em>", "sm")
        + vis('<div style="display:grid;grid-template-columns:340px 1fr;width:100%;height:540px;border:4px solid #1B4332;background:#fff">'
              + '<div style="background:#EFE9DC;padding:24px;display:flex;flex-direction:column;gap:12px">'
              + "".join(B(f'<div class="nd" style="min-height:56px;font-size:20px;align-items:flex-start;padding:10px 16px">{p}</div>', s=1)
                        for p in ["project 1", "project 2", "project 3", "project 4"])
              + "</div>"
              + '<div style="padding:28px;display:flex;flex-direction:column;gap:14px;overflow:hidden">'
              + "".join(B(f'<div style="height:34px;background:{c};width:{w}%;align-self:{a}"></div>', s=2)
                        for c, w, a in [("#B9C7BE", 70, "flex-end"), ("#EFE9DC", 85, "flex-start"), ("#B9C7BE", 60, "flex-end"), ("#EFE9DC", 90, "flex-start"),
                                        ("#B9C7BE", 50, "flex-end"), ("#EFE9DC", 80, "flex-start"), ("#B9C7BE", 65, "flex-end"), ("#EFE9DC", 75, "flex-start")])
              + B('<div style="margin-top:auto"><span class="chip r">fixes lost</span></div>', s=3)
              + "</div></div>", style="top:220px"), 75,
        ["Through 2025 and into 2026 it was ChatGPT projects. Build 1: different projects, different instructions inside each one.",
         "Build 2: and in practice everything happened in the same chat session, scrolling forever.",
         "Build 3: no repo, no versioning, and no way for a correction made on a Tuesday to survive to Thursday.",
         "Name it precisely. Most of the people watching are here right now and will recognise it."],
        onscreen="A mock chat app: four projects in the sidebar, one long thread, a red chip: no repo, no versions, fixes lost.")
    add("one file, one job",
        hd("One file <em>owns one job.</em>")
        + vis('<pre class="code" style="width:100%;font-size:25px"><em># skills/youtube/youtube-title-generator.md</em>\n\n'
              + B('<span>## Required reading</span>', s=1, tag="span") + "\n"
              + B('<span>brand/voice.md, brand/audience.md</span>', s=1, tag="span") + "\n\n"
              + B('<span>## Step 1: extract the mechanism</span>', s=2, tag="span") + "\n"
              + B('<span>## Step 2: map it to the topic</span>', s=2, tag="span") + "\n"
              + B('<span class="add">## Step 3: rebuild it with the angle</span>', s=3, tag="span") + "</pre>", style="top:230px"), 75,
        ["A skill is a markdown file that owns one job. Open one on camera. This is the title generator.",
         "Build it: what it reads first, then the steps in order.",
         "It is plain text. You can read it, edit it, and see every change in the history."],
        onscreen="A real skill file open in a code panel, its sections building in.")
    add("73 files, eight folders",
        '<div style="display:grid;grid-template-columns:620px 1fr;gap:60px;height:100%;align-items:center">'
        + '<div><div class="giant md">73</div>' + B('<div class="glabel cnt" style="margin-top:30px">files, split by activity.</div>', s=1) + "</div>"
        + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">'
        + "".join(B(f'<div class="nd" style="min-height:96px;font-size:26px">{f}/</div>', s=2 + k // 4) for k, f in enumerate(
            ["content", "research", "ops", "miro", "lead-gen", "youtube", "creative-strategy", "dm-setting"]))
        + "</div></div>", 60,
        ["73 markdown files across eight folders, as published. Build the folders.",
         "The split is by activity. A client leaves. An activity survives every client."],
        onscreen="Giant 73, then eight folder tiles.")
    add("the file compounds",
        hd("Every correction goes <em>back in.</em>", "sm") + vis(grow(), style="top:220px"), 75,
        ["The property that matters is cumulative. Every correction goes back into the file.",
         "Build the bars: each one is the same file after one more fix. The bars are a picture of the idea. They carry no values.",
         "So the file is worth more this month than last month. In my own words from the voice note: you keep building and building, and it is satisfying to watch the folder grow."],
        onscreen="Six bars of the same file growing, fix 1 to fix 6, the last in honey.")
    add("worked example, a fix that holds",
        hd("Tuesday's fix still holds <em>Thursday.</em>", "sm")
        + vis('<div class="split">'
              + B('<div class="panel"><div class="lab">Before: the chat</div><pre class="code" style="font-size:22px">draft:\n<span class="del">"Most agencies skip</span>\n<span class="del"> this step."</span>\n\n<em>you fix it in the chat</em>\n<em>next chat: back again</em></pre></div>', s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After: the skill</div><pre class="code" style="font-size:22px"><em>brand/voice.md</em>\n<span class="add">HARD BAN 3:</span>\n<span class="add">no "most X" openers.</span>\n\n<em>every run reads it</em></pre></div>', s=2)
              + "</div>", style="top:230px"), 90,
        ["The worked example for part one.",
         "Build 1, the before. A draft opens with 'most agencies skip this step', the most generic opener there is. In the chat you fix it, and the next chat it is back.",
         "Build 2, the after. The fix goes into voice.md as a hard ban, and every skill that writes reads that file first. The fix holds on Thursday because it lives in a file."],
        onscreen="Left: a struck 'most agencies' opener and the note next chat back again. Right: voice.md, hard ban 3.")

    # ---------------- SECTION 2: THE AGENT
    add("section 2 card", vis(agenda(AG, live=2)), 15,
        ["Part two, the agent. What it adds on top of the skills."], onscreen="Agenda with card 2 live.")
    add("runs without being asked",
        hd("Runs without <em>being asked.</em>")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:30px">'
              + B('<div class="panel"><div class="lab">A skill</div>' + flow([("you ask", "", None), ("skill runs", "dk", None), ("you read it", "", None)]) + "</div>", s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">An agent</div>' + flow([("schedule fires", "y", None), ("agent runs", "dk", None), ("output waits", "", None)]) + "</div>", s=2)
              + "</div>", style="top:230px"), 60,
        ["Build 1: a skill runs when you ask it to.",
         "Build 2: an agent runs on its own. A schedule fires, it runs, the output is waiting for you.",
         "Agents run on top of the skills, and the skills stay underneath."],
        onscreen="Two flows: you ask then skill runs, and schedule fires then agent runs.")
    add("the live example",
        hd("Reads four tools. <em>Writes the day.</em>", "sm") + vis(hub(), style="top:220px"), 90,
        ["The first agent I installed. Build the four inputs: it checks Notion, tl;dv, Drive and Slack before it proposes anything.",
         "Build 5: the agent. Build 6: it writes blocks straight into the calendar.",
         "Keep the calendar blocks generic on screen. No client names, no real meeting titles."],
        onscreen="Notion, tl;dv, Drive, Slack feed an agent box, which writes blocks into a calendar.")
    add("the time claim",
        hd("Time saved goes into <em>more agents.</em>", "sm")
        + vis('<div style="display:flex;flex-direction:column;align-items:center;gap:40px">'
              + B(needs("about 30 minutes a day saved: his own estimate, not in claims.md"), s=1)
              + B(flow([("time saved", "", None), ("build the next agent", "y", None)]), s=2)
              + "</div>", style="top:280px"), 45,
        ["The time claim. In the voice note I said it saves things that used to take about thirty minutes a day. That is my estimate, and nobody measured it.",
         "It is not in claims.md, so it is a NEEDS tag on the frame. Say it as an estimate only if you sign it off.",
         "Build 2: and those minutes go straight into building more agents."],
        onscreen="A red NEEDS tag on the time estimate, then time saved feeding the next agent.")
    add("four installed",
        hd("Four installed <em>today.</em>")
        + vis('<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;width:100%">'
              + "".join(B(f'<div class="nd dk" style="min-height:150px"><span class="mono" style="font-size:28px">{a}</span><small>{b}</small></div>', s=k + 1)
                        for k, (a, b) in enumerate([("performance-loop", "flags a reach drop"), ("signal-sweep", "catches a missed ask"),
                                                   ("board-qa", "gates a board"), ("youtube-lead-magnet", "packages a video")]))
              + "</div>", style="top:240px"), 60,
        ["Four agents installed, as published. Build them.",
         "performance-loop flags a reach drop before it becomes a quarter. signal-sweep catches an ask buried in a chat thread.",
         "board-qa gates a video board. youtube-lead-magnet turns a video into the lead magnet package, and its first instruction is to run the existing skill and never invent rules."],
        onscreen="Four dark cards with the agent names and one label each.")
    add("before and after, the day",
        hd("The tax of <em>the jump.</em>")
        + vis('<div class="split">'
              + B('<div class="panel"><div class="lab">Before: manual</div>' + squares(15, 5, lambda k: "g") +
                  '</div>', s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After: agent-run</div>' + squares(15, 5, lambda k: "g" if k % 4 else "r") +
                  '</div>', s=2)
              + "</div>", style="top:240px"), 60,
        ["Before and after for part two.",
         "Build 1: coming from neat, organised manual content.",
         "Build 2: an AI running the day produces disparities. The squares are a picture of the idea: some blocks land where you did not picture them. That is the tax of the jump."],
        onscreen="Two grids of blocks: all even on the left, some red on the right.")

    # ---------------- SECTION 3: WHAT BROKE
    add("section 3 card", vis(agenda(AG, live=3)), 15,
        ["Part three, what broke. All four, from the voice notes, none invented."], onscreen="Agenda with card 3 live.")
    add("four things broke",
        hd("Four things <em>broke.</em>")
        + vis('<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;width:100%">'
              + "".join(B(f'<div class="nd {c}" style="min-height:160px;font-size:32px">{a}</div>', s=k + 1)
                        for k, (a, c) in enumerate([("quiet failures", "bad"), ("too little context", ""), ("not what I pictured", ""), ("the manual-to-AI jump", "")]))
              + "</div>", style="top:240px"), 75,
        ["Build them one by one.",
         "One: failures you do not notice straight away. An agent on a schedule fails quietly and you find it a week later. That is the big one, in red.",
         "Two: not enough context given to the model. The root cause under most of the surprises.",
         "Three: output that is not what you pictured, because building from scratch never matches the picture on the first pass. Four: the jump from a neat manual calendar."],
        onscreen="Four tiles, the first in red: quiet failures.")
    add("quiet failure, the end-of-day report",
        hd("Nothing errored. <em>It was wrong.</em>", "sm")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:30px">'
              + B('<div class="panel"><div class="lab">Before</div>' + flow([("calendar block", "", None), ("no done state", "bad", None), ("guessed from Notion, Slack, calls", "bad", None)], [("&rarr;", "r"), ("&rarr;", "r")])
                  + f'<div style="margin-top:14px">{needs("how long the reports were wrong; doc says two months")}</div></div>', s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">The fix, 31 Aug</div>' + flow([("backlog", "", None), ("Google Tasks", "y", None), ("tick written back", "dk", None)]) + "</div>", s=2)
              + "</div>", style="top:220px"), 90,
        ["The first quiet failure, dated. A calendar block has no done state.",
         "Build 1: so the end-of-day ritual inferred what got done from Notion, Slack and call transcripts, and got it wrong. The doc says for two months. That duration is not in claims.md, so it is tagged.",
         "My verdict on the old version, verbatim: calendar blocks don't get done automatically, so that makes it ass.",
         "Build 2: the fix on 31 August. The plan comes out of the backlog, and the tick comes from Google Tasks."],
        onscreen="Before: calendar block, no done state, a guess, in red. The fix: backlog, Google Tasks, tick written back.")
    add("the fix that did not hold",
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:50px;height:100%;align-items:center">'
        + '<div><div class="giant md" style="font-size:250px">185</div><div class="cite" style="font-size:24px">TASKS PUSHED SINCE 31 AUG</div></div>'
        + '<div>' + B('<div class="giant md" style="font-size:250px;color:#C0392B">0</div><div class="cite" style="font-size:24px">TICKED</div>', s=1)
        + B(f'<div style="margin-top:30px">{needs("sign-off: internal ops file, Mauro decides")}</div>', s=2) + "</div></div>"
        + '<div class="glabel cnt" style="position:absolute;left:110px;top:80px;font-size:56px">Then the fix failed too.</div>', 75,
        ["The honest follow-up. From 31 August Claude pushed five backlog tasks a day into Google Tasks. 37 days, 185 tasks, zero ticked.",
         "So the fix closed the loop on paper and nobody used it. Same shape again: nothing errored.",
         "Build 2: this row is marked Mauro decides in claims.md. Keep it in only if you sign it off. If you cut it, cut this frame and add its 75 seconds to the next one."],
        onscreen="185 against a red 0, under the line Then the fix failed too. A NEEDS sign-off tag.")
    add("quiet failure, the noise statistic",
        hd("A tiny denominator <em>topped the week.</em>", "sm")
        + vis('<div style="width:100%">'
              + '<table class="tb">'
              + B('<td>post A</td><td>top engagement rate &middot; ' + needs("221 views, 22.2%: not in claims.md", sm=True) + '</td>', s=1, tag="tr", cls="")
              + '<tr><td>post B</td><td>lower rate</td></tr><tr><td>post C</td><td>lower rate</td></tr></table>'
              + B(f'<div style="margin-top:30px;display:flex;gap:18px;align-items:center"><span class="chip y">floor first</span>'
                  f'{needs("the floor, doc says 1,000+ views", sm=True)}</div>', s=2)
              + "</div>", style="top:250px"), 75,
        ["The second quiet failure. A reporting script nominated a post with almost no views and zero likes and replies as the highest engagement rate of the week. A rate on a tiny denominator.",
         "The exact view count and rate in the doc are not in claims.md, so they are tagged.",
         "Build 2: it was caught before it reached the board. The insight rules now require a view floor before any rate counts."],
        onscreen="A leaderboard with a tiny post on top, NEEDS tags on its numbers, then the rule: a view floor before any rate.")
    add("it looked correct",
        hd("It looked exactly like <em>a correct output.</em>", "sm")
        + vis('<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;width:100%">'
              + "".join(B('<div class="panel">' + "".join(f'<div style="height:26px;background:#B9C7BE;width:{w}%;margin-bottom:16px"></div>' for w in (90, 70, 85, 60, 78))
                          + f'<span class="cite">{t}</span></div>', s=k + 1) for k, (c, t) in enumerate([("", "report A"), ("", "report B")]))
              + "</div>"
              ,
              style="top:250px"), 60,
        ["The shape all three failures share, and the line worth saying slowly: nothing errored, nothing alerted, and the output looked exactly like a correct output.",
         "Build both reports. Build 3: one of them is wrong, and there is nothing on screen to tell you which.",
         "That is the main new risk of running agents."],
        onscreen="Two identical report cards. Then: one of these is wrong, nothing says which.")
    add("too little context",
        hd("It did what <em>it was told.</em>")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:30px">'
              + flow([("what I meant", "y", 1), ("what I wrote", "", 2), ("what it did", "dk", 3)], [("&rarr;", "r"), ("&rarr;", "")])
              
              + "</div>", style="top:300px"), 60,
        ["The root cause under most of the surprises: not enough context given to the model.",
         "Build it. What I meant, what I wrote, what it did. The agent did exactly what it was told, which was less than what was meant.",
         "Build 4: the gap sits between the first two boxes, which means the fix is in the skill file, every time."],
        onscreen="Three boxes: what I meant, what I wrote, what it did.")
    add("writing stays a skill",
        hd("Writing stays <em>a skill.</em>")
        + vis('<div class="split">'
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">Writing</div>' + flow([("draft", "", None), ("my edit", "y", None), ("skill", "dk", None)])
                  + "</div>", s=1)
              + B('<div class="panel"><div class="lab">If an agent wrote</div>' + flow([("draft", "", None), ("published", "bad", None)], [("&rarr;", "r")])
                  + "</div>", s=2)
              + "</div>", style="top:260px"), 75,
        ["The one job deliberately kept as a skill: writing.",
         "Build 1: I correct the writing skills constantly, and I want the writing close to me. A correction is a file edit I can see.",
         "Build 2: hand writing to something that runs on its own and the correction loop that made the writing good is gone."],
        onscreen="Left: draft, my edit, skill. Right: draft straight to published, in red.")
    add("the ceiling",
        hd("Agents come after <em>the skill is good.</em>", "sm")
        + vis(flow([("skill", "", 1), ("correct it", "", 2), ("run again", "", 3), ("good enough", "y", 4), ("then the agent", "dk", 5)]), style="top:320px"), 75,
        ["The ceiling, in my own words: I am not fully installing agents yet, because I am not yet happy with what the skills produce.",
         "Build the order. The confidence comes from the loop: correct the output, push the correction into the skill, run it again.",
         "That loop is the actual product. Build 5: the agent is what you install after it."],
        onscreen="Five boxes in a row ending in: then the agent.")
    add("CTA",
        '<div class="cta"><div class="big">Link in the description</div><div class="offer">Agency Booked Calls</div></div>', 45,
        ["If you run an established agency and want this built for your own inbound, the link is in the description. It is called Agency Booked Calls.",
         "Everyone else, drop your questions in the comments. The next video is the agents I want to install to cause calls.",
         "No price on screen and no URL."],
        onscreen="Dark frame: Link in the description, and the offer name in honey.", cls="dark")
    return S


TITLES = [
    {"title": "I Moved My Content Engine to AI Agents (What Broke)",
     "modelled_on": "01-outliers.csv, Marcos Ruiz, 'I Copied a Twitter/X Account That Makes $100k/mo (it worked?)': first-person move plus a bracketed honest-outcome tag (6.3k on a small channel, 1.6x its other top videos)"},
    {"title": "What I'd Build Before AI Agents in 2026",
     "modelled_on": "01-outliers.csv, Nick Saraev, 'What I'd Learn Instead of Automation in 2026', 492k: contrarian 'what I'd do first' with the year"},
    {"title": "When to Turn Claude Skills Into Agents (Clearly Explained)",
     "modelled_on": "01-outliers.csv, Greg Isenberg, 'How AI agents & Claude skills work (Clearly Explained)', 647k: the hot mechanic plus the Clearly Explained tag"},
]

NEEDS = ["about 30 minutes a day saved (his estimate, voice note 2026-08-20)",
         "how long the end-of-day reports were wrong (doc says two months)",
         "185 tasks pushed, 0 ticked: in claims.md but marked 'Mauro decides'",
         "the noise statistic: 221 views, 22.2% engagement rate",
         "the view floor for insight rules (doc says 1,000+)"]

THUMBS = [
    """<div class="thumb" style="background:#0E2418">
      <div style="position:absolute;left:60px;top:70px;display:flex;align-items:center;gap:24px">
        <div style="width:220px;height:280px;background:#F7F3EA;border:6px solid #E9B949;padding:24px">
          <div style="height:16px;background:#1B4332;margin-bottom:14px"></div><div style="height:16px;background:#1B4332;width:70%;margin-bottom:14px"></div>
          <div style="height:16px;background:#1B4332;width:85%;margin-bottom:14px"></div><div style="height:16px;background:#1B4332;width:60%"></div></div>
        <div style="font-size:120px;font-weight:900;color:#E9B949">&rarr;</div>
        <div style="width:220px;height:280px;background:#1B4332;border:6px solid #C0392B;display:flex;align-items:center;justify-content:center;font-size:160px;font-weight:900;color:#C0392B">!</div></div>
      <div style="position:absolute;left:70px;bottom:60px;font-size:108px;font-weight:900;color:#fff;letter-spacing:-4px;line-height:1">WHAT <span style="color:#E9B949">BROKE</span></div>
      <div class="face">FACE</div></div>""",
    """<div class="thumb" style="background:#F7F3EA">
      <div style="position:absolute;left:60px;top:90px;font-size:330px;font-weight:900;color:#1B4332;letter-spacing:-18px;line-height:1">73</div>
      <div style="position:absolute;left:470px;top:190px;font-size:150px;font-weight:900;color:#E9B949">&rarr;</div>
      <div style="position:absolute;left:600px;top:90px;font-size:330px;font-weight:900;color:#C0392B;letter-spacing:-18px;line-height:1">4</div>
      <div style="position:absolute;left:70px;bottom:60px;background:#1B4332;color:#E9B949;font-size:90px;font-weight:900;padding:8px 28px;letter-spacing:-3px">SKILLS TO AGENTS</div>
      <div class="face" style="border-color:#1B4332;color:#1B4332;width:360px;height:520px">FACE</div></div>""",
    """<div class="thumb" style="background:#1B4332">
      <div style="position:absolute;left:70px;top:60px;width:640px;height:360px;background:#0E2418;border:6px solid #E9B949;padding:30px;font:700 34px/1.5 'JetBrains Mono',monospace;color:#EAF2EC">
        <div style="height:22px;background:#7FA08C;width:50%;margin-bottom:22px"></div><div style="height:22px;background:#E9B949;width:80%;margin-bottom:22px"></div><div style="height:22px;background:#EAF2EC;width:65%;margin-bottom:22px"></div><div style="height:22px;background:#EAF2EC;width:72%"></div></div>
      <div style="position:absolute;left:70px;bottom:50px;font-size:92px;font-weight:900;color:#fff;letter-spacing:-3px;line-height:.95">WRITING STAYS<br><span style="color:#E9B949">MANUAL</span></div>
      <div class="face">FACE</div></div>""",
]
