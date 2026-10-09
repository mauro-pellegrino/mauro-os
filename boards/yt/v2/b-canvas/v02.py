"""Doc 02: how I structure Claude skills. Source: research/video-knowledge/02-skills-structure.md.
Numbers on screen: 73 files, 8 folders, nine conventions (four carry the weight), 60,000 vs 264,000,
649 / 678 / 673. All in brand/claims.md. The 45-minute figure is not, so it renders as [NEEDS]."""
from engine import (needs, lbl, c, window, tree, flow, split, bars, hbar, tiles, cycle, skel)
from v11 import REPO_TREE, map_window, FOLDERS

OWNS = {"content/": "long-form, X articles", "research/": "breakdowns, teardowns", "ops/": "daily, weekly, Monday",
        "miro/": "boards, gotchas", "lead-gen/": "magnets, email to call", "youtube/": "ideas, titles, boards",
        "creative-strategy/": "statics, script QA", "dm-setting/": "DM templates"}

FACE = '<div class="face">MAURO CUTOUT HERE</div>'

THUMBS = [
    # T1: the folder grid + the big number
    '<div style="position:absolute;left:64px;top:70px;width:780px">'
    '<div class="huge" style="margin-top:18px;font-size:122px">73 skills.<br><em>One index.</em></div></div>'
    '<div style="position:absolute;left:64px;bottom:56px;display:grid;grid-template-columns:repeat(4,170px);gap:14px">'
    + "".join(f'<div class="fold {"on" if i in (0, 2) else ""}" style="height:84px">{f}</div>' for i, f in enumerate(
        ["content/", "research/", "ops/", "miro/", "lead-gen/", "youtube/", "creative/", "dm/"])) + '</div>' + FACE,
    # T2: prompt pile vs eight folders, no face
    '<div style="position:absolute;top:0;left:0;right:0;height:120px;background:#E9B949;display:flex;align-items:center;justify-content:center;'
    'font:900 76px Inter;letter-spacing:-2px;color:#0E2418;text-transform:uppercase">Stop saving prompts</div>'
    '<div style="position:absolute;left:0;top:120px;width:640px;bottom:0;background:#2A1A18">'
    + "".join(f'<div class="card" style="left:{60 + (k * 97) % 470}px;top:{40 + (k * 61) % 450}px;width:120px;height:70px;'
              f'transform:rotate({(k * 23) % 50 - 25}deg);background:#5A3A34;border-color:#8A5A50"></div>' for k in range(26))
    + '</div><div style="position:absolute;left:640px;top:120px;right:0;bottom:0;background:#52B788;display:grid;'
    'grid-template-columns:repeat(2,250px);gap:20px;align-content:center;justify-content:center">'
    + "".join(f'<div class="fold on" style="height:82px;background:#0E2418;color:#E9B949;border-top-color:#E9B949">{f}</div>' for f in
              ["content/", "research/", "ops/", "miro/", "lead-gen/", "youtube/", "creative/", "dm-setting/"]) + '</div>',
    # T3: MAP.md with the missing row
    '<div style="position:absolute;left:64px;top:60px">'
    '<div class="huge" style="margin-top:16px;font-size:128px">Unrouted<br>= <em>rebuilt</em></div></div>'
    '<div class="win" style="left:64px;top:380px;width:720px">'
    '<div class="bar">● ● ● routing table</div>'
    '<div class="r">content &rarr; skills/content/</div><div class="r">ops &rarr; skills/ops/</div>'
    '<div class="r bad">outbound reply &rarr; not listed</div></div>' + FACE,
]

VIDEO = {
    "doc": "02",
    "slug": "skills-structure",
    "title_text": "How I structure 73 Claude skills",
    "title_html": "How I structure<br><em>73 Claude skills</em>",
    "title_size": 430,
    "titles": [
        {"title": "How I structure 73 Claude skills (clearly explained)",
         "modelled_on": "01-outliers.csv: Greg Isenberg, \"How AI agents & Claude skills work (Clearly Explained)\", 647K"},
        {"title": "What I'd build instead of another Claude prompt",
         "modelled_on": "01-outliers.csv: Nick Saraev, \"What I'd Learn Instead of Automation in 2026\", 492K"},
        {"title": "The boring Claude Code system behind 73 skills",
         "modelled_on": "01-outliers.csv: Jordan Platten, \"3 Boring AI Systems That Sell For $4000+ Right Now (With PROOF)\", 67K"},
    ],
    "thumbs": THUMBS,
    "needs": ["45 minutes lost to the rebuilt SOP (doc 02 and MAP.md say it, claims.md does not)"],
    "overview": {"sec": 10, "on": "The whole map, zoomed out: the shape, the index, the rules. The title top right.",
                 "say": ["This is how I structure every Claude skill I run, on one map.",
                         "73 files, and none of them gets built twice anymore."]},
    "result": {"id": "result", "num": "", "tag": "the result", "sec": 10, "vcls": "col", "head": "",
               "on": "The number 73, with: skill files, eight folders, one index.",
               "body": '<div class="bign">73</div>' + c("skill files. Eight folders. One index.", cls="bigl") + lbl("counted 2026-09-07 &middot; the repo I run for the agency"),
               "say": ["The result first. 73 skill files in eight folders, and one index that every agent reads before it builds anything.",
                       "The prompts are the part everyone shares. The filing system is the part that decides whether file seventy-three helps you or buries you.",
                       "By the end of this you can copy the whole structure."]},
    "roadmap": {"id": "roadmap", "num": "", "tag": "today we go over", "sec": 10, "head": "",
                "on": "Three cards: 01 The shape, 02 The index, 03 The rules.",
                "body": '<div class="rm">'
                        '<div class="rmc"><div class="k">01</div><div class="t c">The shape</div><div class="ico">' + tree(["skills/", "├── content/", "├── ops/", "└── ..."], size=26) + '</div></div>'
                        '<div class="rmc"><div class="k">02</div><div class="t c">The index</div><div class="ico">' + tree(["ops/MAP.md", "│ skills/", "│ agents/", "│ ..."], size=26) + '</div></div>'
                        '<div class="rmc"><div class="k">03</div><div class="t c">The rules</div><div class="ico">'
                        '<div style="display:flex;flex-direction:column;gap:12px"><span class="chip on">[measured]</span><span class="chip">[observed]</span><span class="chip">[assumed]</span></div></div></div></div>',
                "say": ["Today we go over three things.",
                        "First, the shape: how the folders split, and why I never split by client.",
                        "Second, the index: the one file that stops an agent from rebuilding what already exists.",
                        "Third, the rules: the conventions that keep every claim and every number honest, and the loop that improves a skill."]},
    "regions": [
        {"num": "01", "label": "The shape", "sec": 25,
         "on": "Region 01 framed: the skills tree, the folder grid, the two-repo split.",
         "say": ["Section one. The shape.", "Where every file lives, and why."],
         "zones": [
             {"id": "skills-tree", "num": "01", "tag": "the shape", "sec": 60,
              "on": "The skills/ part of the repo tree: eight folders with what each holds.",
              "head": "Eight folders, split by activity.",
              "body": tree(REPO_TREE[1:10], hl=("├── skills/",), size=26),
              "say": ["Open the skills folder. Eight names.",
                      "content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting. 73 files across them.",
                      "73 is a count on one date. It is bigger today, and that is fine. The shape is what holds."]},
             {"id": "owns", "num": "01", "tag": "the shape", "sec": 60,
              "on": "Eight folder tiles, each with what it owns.",
              "head": "What each folder owns.",
              "body": tiles([(f, OWNS[f], "on" if f in ("content/", "ops/") else "") for f in FOLDERS], cols=4),
              "say": ["Each folder is an activity. A thing you do every week, whatever the client.",
                      "content owns long-form, short-form and the X article set. ops owns the daily system, the content loop and the Monday analysis.",
                      "When I want a new skill, the first question is which activity it belongs to. Never which client asked for it."]},
             {"id": "client-vs-activity", "num": "01", "tag": "before / after", "sec": 70,
              "on": "Before: client folders with the same skill copied in each, one client gone. After: one activity folder, every account reads it.",
              "head": "Client folders rot.",
              "body": split(
                  tree(["client-a/", "└── article-skill.md", "client-b/", "└── article-skill.md", "client-c/   (client left)", "└── article-skill.md"], red=("client-c",), size=31)
                  + lbl("the same skill, rebuilt per client"),
                  tree(["skills/content/", "└── x-articles/", "      ▲    ▲    ▲", "  acct-a acct-b acct-c"], hl=("x-articles",), size=31)
                  + lbl("one skill, every account reads it")),
              "say": ["Before: a folder per client. Each one gets its own article skill.",
                      "The client leaves, that folder rots, and the same skill gets rebuilt inside the next client folder.",
                      "After: a folder per activity. One article skill, and every account reads it.",
                      "An activity survives every client. This one is my judgement from watching it happen, so I tag it as assumed."]},
             {"id": "drift", "num": "01", "tag": "worked example", "sec": 75,
              "on": "Two windows, copy A and copy B of the same article skill, with different lines highlighted red and green. Label: nothing synced them.",
              "head": "Two copies, two answers.",
              "body": window("article skill · copy A", skel([90, 70]) + '<div class="sk sage" style="width:80%"></div>' + skel([60, 85]) + '<div class="sk sage" style="width:55%"></div>', style="width:560px")
                      + window("article skill · copy B", skel([90, 70]) + '<div class="sk red" style="width:72%"></div>' + skel([60, 85]) + '<div class="sk red" style="width:64%"></div>', style="width:560px"),
              "src": "nothing synced them &middot; recorded in ops/MAP.md",
              "say": ["The worked example. I run two repos: the agency repo and my own.",
                      "At one point both held a copy of the same article skill. The two copies drifted apart, and nothing synced them.",
                      "Two copies of a skill means two different answers to the same question. You only find out when the output disagrees."]},
             {"id": "pointer", "num": "01", "tag": "before / after", "sec": 65,
              "on": "Before: two repos each with a skill copy. After: the agency repo holds the skills, my repo holds voice, positioning and audience and points at them.",
              "head": "One copy. Everyone points at it.",
              "body": split(
                  flow([("agency repo", "skill copy", ""), ("my repo", "skill copy", "red")], cls="sm") + lbl("two copies drift"),
                  flow([("my repo", "voice, positioning, audience", ""), ("agency repo", "the skills, once", "dark")], cls="sm") + lbl("my repo points, never copies")),
              "say": ["Before: a copy in each repo.",
                      "After: the agency repo is canonical for skills. My repo holds voice, positioning and audience, and it points at the skills instead of copying them.",
                      "Anything account-agnostic lives in one place once. Voice and positioning stay per repo, because they are the only things that really differ."]},
         ]},
        {"num": "02", "label": "The index", "sec": 25,
         "on": "Region 02 framed: MAP.md, the incident, the rule.",
         "say": ["Section two. The index.", "The one file that every agent reads first."],
         "zones": [
             {"id": "map", "num": "02", "tag": "the index", "sec": 60,
              "on": "A window on ops/MAP.md: eleven areas and what each owns.",
              "head": "One file indexes everything.",
              "body": map_window(hot=("skills/",)),
              "say": ["ops/MAP.md. Eleven top-level areas, each with what it owns.",
                      "When an agent starts work, this is what it reads. If a folder is not in here, the agent has no way to know it exists."]},
             {"id": "incident", "num": "02", "tag": "worked example", "sec": 80,
              "on": "A four-step timeline dated 2026-09-01: writes a SOP, pushes it, finds outbound-calls/ had a better one, deletes its own. Red tag on the time lost.",
              "head": "The SOP that already existed.",
              "body": '<div style="width:100%">' + flow([
                  ("writes a SOP", "outbound reply, from scratch", ""), ("pushes it", "looks finished", ""),
                  ("finds outbound-calls/", "a better one, already there", "on"), ("deletes its own", "work thrown away", "red")]) +
                      '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
                      + lbl("2026-09-01 &middot; recorded in ops/MAP.md") + needs("time lost, 45 min per MAP.md, sign-off") + '</div></div>',
              "say": ["The first of September. An agent wrote a full outbound-reply SOP from scratch and pushed it.",
                      "Then it found that outbound-calls already held a better one. The new one got deleted.",
                      "[NEEDS: say the time lost only after Mauro signs off the 45-minute figure.]"]},
             {"id": "unlisted", "num": "02", "tag": "the cause", "sec": 60,
              "on": "The routing table: four rows lead to a skill, the outbound reply row is red, its folder not listed.",
              "head": "The folder was never listed.",
              "body": window("routing table", "".join([
                  '<div class="row"><b>article from transcript</b><span>skills/content/x-articles/</span></div>',
                  '<div class="row"><b>monday analysis</b><span>skills/ops/monday-acquisition-analysis.md</span></div>',
                  '<div class="row"><b>board build</b><span>skills/miro/</span></div>',
                  '<div class="row"><b>lead magnet</b><span>skills/lead-gen/lead-magnet/</span></div>',
                  '<div class="row bad"><b>outbound reply</b><span>outbound-calls/ &nbsp;not listed</span></div>']), style="width:1250px"),
              "say": ["The cause was not carelessness. The routing table was long, and that folder was not in it.",
                      "The agent did exactly what the map told it. The map was missing a row."]},
             {"id": "rule", "num": "02", "tag": "the rule", "cls": "dark", "sec": 50, "vcls": "col",
              "on": "Dark card, one line: work is not finished until it is routed.",
              "head": "",
              "body": '<div class="c" style="font-size:118px;font-weight:900;letter-spacing:-.04em;line-height:1.02;color:#fff;text-align:center">'
                      'Work is not finished until it is <span style="color:#E9B949">routed.</span></div>',
              "say": ["So here is the rule that carries the whole system. Work is not finished until it is routed.",
                      "If you remember one thing from this video, it is this one."]},
             {"id": "invisible", "num": "02", "tag": "before / after", "sec": 65,
              "on": "Before: an unrouted skill, the next agent builds a second one. After: a routed skill, the agent reads MAP.md and opens the existing one.",
              "head": "Invisible is worse than missing.",
              "body": split(
                  flow([("skill, unrouted", "", "red"), ("next agent", "", ""), ("a second skill", "", "red")], cls="sm") + lbl("you pay for it twice"),
                  flow([("skill, routed", "", "sage"), ("reads MAP.md", "", "dark"), ("opens it", "", "on")], cls="sm") + lbl("built once, found every time")),
              "say": ["A skill that is not in the index is invisible. That is worse than not having it, because the next agent builds a second one.",
                      "Before: unrouted, and you pay twice. After: routed, and the agent finds it on the first read."]},
             {"id": "done", "num": "02", "tag": "the rule", "sec": 50,
              "on": "A flow: skill written, in MAP.md, in the routing table, done.",
              "head": "Done means routed.",
              "body": flow([("skill written", "", ""), ("in MAP.md", "", "on"), ("in the routing table", "", "on"), ("done", "", "dark")]),
              "say": ["So my definition of done changed. A skill is done when it is in the map and in the routing table.",
                      "Before that, it is a draft, however good it is."]},
         ]},
        {"num": "03", "label": "The rules", "sec": 25,
         "on": "Region 03 framed: the conventions, the tags, the chart, the scripts, the loop.",
         "say": ["Section three. The rules.", "The conventions that keep every file honest, and the loop that makes a skill better."],
         "zones": [
             {"id": "nine", "num": "03", "tag": "the conventions", "sec": 50,
              "on": "Nine rule tiles, four lit: tag, trace, limit, date.",
              "head": "Nine rules. Four carry it.",
              "body": tiles([("tag", "every claim", "on"), ("trace", "every number to a script", "on"), ("limit", "every script", "on"),
                             ("date", "every decision", "on"), ("", "", "off"), ("", "", "off"), ("", "", "off"), ("", "", "off"), ("", "", "off")], cols=3),
              "src": "ops/CONVENTIONS.md",
              "say": ["Nine conventions live in one file. Four carry the weight. I will show you each one."]},
             {"id": "tags", "num": "03", "tag": "rule 1", "sec": 60,
              "on": "Three big tags with what each needs: measured, observed, assumed. An untagged claim struck through.",
              "head": "Every claim carries a tag.",
              "body": '<div style="display:flex;flex-direction:column;gap:26px">'
                      '<div class="trow"><span class="tag3" style="background:#52B788">[measured]</span>' + lbl("names a script and a dataset") + '</div>'
                      '<div class="trow"><span class="tag3" style="background:#E9B949">[observed]</span>' + lbl("seen, not counted") + '</div>'
                      '<div class="trow"><span class="tag3" style="background:#fff">[assumed]</span>' + lbl("a judgement, stated as one") + '</div>'
                      '<div class="trow"><span class="chip red strike">untagged claim</span>' + lbl("deleted on sight") + '</div></div>',
              "say": ["Rule one. Every claim carries its evidence status.",
                      "Measured names a script and a dataset. Observed was seen but not counted. Assumed is a judgement, and it says so.",
                      "An untagged claim is an assertion. It gets deleted on sight."]},
             {"id": "backwards", "num": "03", "tag": "worked example", "sec": 70,
              "on": "Two bars: the worked example section at 60,000, the winning section at 264,000.",
              "head": "This claim measured backwards.",
              "body": bars([("the worked example", 60000, "#B42318", "60,000"), ("the winning section", 264000, "#52B788", "264,000")], w=1000, h=520),
              "src": "the skill said: the worked example converts",
              "say": ["Here is why that rule exists. A skill said the worked example was the section that converts.",
                      "Measured, it did 60,000 against the winning section's 264,000. The opposite direction.",
                      "The claim felt obviously true. That is the kind that needs a tag most."]},
             {"id": "trace", "num": "03", "tag": "rule 2", "sec": 55,
              "on": "A chain: a number in a doc, the data file that holds it, the script and the capture behind it.",
              "head": "Every number traces to a script.",
              "body": flow([("a number in a doc", "", ""), ("the data file", "", ""), ("the script", "ops/tools/", "on"), ("the capture", "the raw export", "dark")]),
              "say": ["Rule two. A number in a doc points at the file that holds it. That file points at a script and a capture.",
                      "And the analysis that produced a number gets saved as a script. An inline calculation dies at the next context clear, and then someone re-derives it a bit differently."]},
             {"id": "limits", "num": "03", "tag": "rule 3", "sec": 65,
              "on": "A docstring, paraphrased, in capitals: measures all inbound bookings, every owner. Two bars: 649 of 678 rows under one owner, UTM empty on 673.",
              "head": "Every script states its limit.",
              "body": '<div style="display:flex;flex-direction:column;gap:30px;align-items:center">'
                      + window("ops/tools/ · opening docstring, paraphrased", '<div style="color:#1B4332;font-weight:700">"""<br>MEASURES ALL INBOUND BOOKINGS,<br>EVERY OWNER.<br>"""</div>', style="width:900px")
                      + '<div>' + hbar("one owner", 649, 678, "649 / 678", "#E9B949", 760) + hbar("UTM empty", 673, 678, "673 / 678", "#B42318", 760) + '</div></div>',
              "src": "Calendly rows",
              "say": ["Rule three. Every script states its own limit in its opening docstring.",
                      "One tool was named as if it measured one account's bookings. It measures all inbound, because 649 of 678 Calendly rows sit under one owner and the UTM field is empty on 673.",
                      "The name claimed something the data cannot carry. So the docstring now says so, in capitals."]},
             {"id": "dated", "num": "03", "tag": "rule 4", "sec": 50,
              "on": "A skill file with one dated line highlighted: 2026-08-31, v3, plan from BACKLOG.md, tick from Google Tasks.",
              "head": "Decisions live in the file.",
              "body": window("skills/ops/daily-ops.md", skel([80, 65, 90]) +
                             '<div class="row hot"><b>2026-08-31</b><span style="color:#1B4332">v3: plan from BACKLOG.md, tick from Google Tasks</span></div>'
                             + skel([75, 85, 60]), style="width:1250px"),
              "say": ["Rule four. Decisions are dated lines in the file whose behaviour they govern.",
                      "Not in chat. Not in a separate log. When a call gets made, it goes into the file it changes, with the date and the exact wording."]},
             {"id": "loop", "num": "03", "tag": "the loop", "sec": 70,
              "on": "A cycle: build for one job, run on real work, read the output, find the break, edit the skill, run again.",
              "head": "Run it on real work.",
              "body": cycle([("build for one job", "dark"), ("run on this week's work", "on"), ("read the output", ""),
                             ("find the break", ""), ("edit the skill", "on"), ("run it again", "")], r=250, size=640),
              "say": ["And the loop that makes any of this worth it.",
                      "Build the skill for one job. Run it on real work this week, never a fake example. Read the output, find exactly where it breaks, edit the skill itself, run it again.",
                      "The reference version is the seventh file in my X article set. It exists only to keep the other six honest as evidence lands."]},
         ]},
    ],
    "cta": {"id": "cta", "num": "", "tag": "", "cls": "dark", "sec": 45, "vcls": "col", "head": "",
            "on": "Dark card: Agency Booked Calls, and Link in the description.",
            "body": '<div class="bign" style="color:#E9B949;font-size:150px;letter-spacing:-.04em;text-align:center;line-height:1">'
                    + c("Agency Booked Calls", tag="span") + '</div><div class="bigl c" style="color:#fff">Link in the description</div>',
            "say": ["If you run an established agency and you want this installed for your own inbound, that is Agency Booked Calls. The link is in the description.",
                    "Everyone else: copy the folders, write the map, and tell me in the comments which rule you are adding first."]},
    "final": {"sec": 15, "on": "The whole map again, zoomed out.",
              "say": ["The shape, the index, the rules. That is the whole structure.", "Screenshot it if you want it."]},
}
