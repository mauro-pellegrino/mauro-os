"""Doc 11: My whole Claude Code content system. Source: research/video-knowledge/11-claude-code-content-system.md.
Every number on screen is in brand/claims.md ("The content system, as published 2026-09-10" and
"Mauro's own operation"). The three revenue figures in doc 11 are not in claims.md and stay off the board."""
from engine import (needs, lbl, c, window, tree, flow, split, bars, hbar, tiles, cycle, skel)

REPO_TREE = """agency-repo/                     the whole operation, one repo
├── skills/                      73 markdown files, split by activity
│   ├── content/                 long-form, short-form, linkedin-docs, x-articles/
│   ├── research/                weekly research, brand breakdowns, ad teardowns
│   ├── ops/                     daily ops, content loop, monday analysis, case studies
│   ├── miro/                    board builds, the DSL gotchas, the house diagram style
│   ├── lead-gen/                five lead magnet subtypes, email to call
│   ├── youtube/                 ideas, titles, hooks, boards, slides
│   ├── creative-strategy/       static ads, the ad script QA
│   └── dm-setting/              outbound and inbound DM templates
├── .claude/agents/              4 installed agents
│   ├── performance-loop.md      catches a reach drop before it becomes a quarter
│   ├── signal-sweep.md          catches an ask buried in a chat thread
│   ├── board-qa.md              15 gates: is this lane recordable
│   └── youtube-lead-magnet.md   packages a video into a lead magnet
├── ops/
│   ├── MAP.md                   the index. route it or it gets rebuilt
│   ├── CONVENTIONS.md           nine rules: evidence tags, provenance, limits
│   ├── tools/                   25 python scripts, one per number anyone cites
│   └── daily/                   the worklog, the weekly spine, today.json
├── research/                    article studies, creative examples, competitor digs
├── accounts/                    [REDACTED] one folder per account
├── acquisition-calls/           one dated analysis per week
├── outbound-calls/              the cold email motion end to end
└── BACKLOG.md                   the standing list, and what is blocked on me""".split("\n")

MAP_ROWS = [("skills/", "73 skill files, 8 folders"), (".claude/agents/", "the 4 installed agents"),
            ("ops/", "conventions, the map, daily, tools"), ("research/", "the evidence behind every rule"),
            ("accounts/", "[REDACTED]"), ("acquisition-calls/", "the Monday analysis"),
            ("outbound-calls/", "the cold email motion"), ("emails/", "the rest of the operation"),
            ("brands/", "the rest of the operation"), ("recaps/", "the rest of the operation"),
            ("future-projects/", "the rest of the operation")]


def map_window(title="ops/MAP.md", hot=()):
    rows = "".join(f'<div class="row {"hot" if a in hot else ""}"><b>{a}</b><span>{b}</span></div>' for a, b in MAP_ROWS)
    return window(title, f'<div style="font-size:22px">{rows}</div>', style="width:1150px")


FOLDERS = ["content/", "research/", "ops/", "miro/", "lead-gen/", "youtube/", "creative-strategy/", "dm-setting/"]

VIDEO = {
    "doc": "11",
    "slug": "claude-code-content-system",
    "title_text": "My whole Claude Code content system",
    "title_html": "My whole <em>Claude Code</em><br>content system",
    "title_size": 430,
    "needs": ["45 minutes lost to the rebuilt SOP (doc 11 and MAP.md say it, claims.md does not)", "the revenue figure in doc 11 ($100k/mo, $150k MRR, ~$500k total) is unresolved and kept off the board"],
    "overview": {"sec": 10, "on": "The whole map, zoomed out: three regions (the repo, the agents, the loop), the arrows between them, the title top right.",
                 "say": ["This is my whole Claude Code content system, on one map.",
                         "Everything you see here is a real file in a real repo. I run it every week for the agency I run."]},
    "result": {
        "id": "result", "num": "", "tag": "the result", "sec": 10,
        "on": "One number, 150+, with its label and source.",
        "head": "",
        "vcls": "col",
        "body": '<div class="bign">150<em>+</em></div>' + c("qualified booked calls in 2026", cls="bigl")
                + lbl("source: Calendly export &middot; for the agency I run"),
        "say": ["The result first. This system sits behind more than 150 qualified booked calls this year for the agency I run.",
                "That is the total from the Calendly export. I am not going to tell you which channel each one came from, because the data cannot say that. You will see why later.",
                "By the end of this video you will know how the whole thing is built, file by file."]},
    "roadmap": {
        "id": "roadmap", "num": "", "tag": "today we go over", "sec": 10,
        "on": "Three cards: 01 The repo, 02 The agents, 03 The loop.",
        "head": "",
        "body": '<div class="rm">'
                '<div class="rmc"><div class="k">01</div><div class="t c">The repo</div><div class="ico">'
                + tree(["skills/", "├── content/", "├── ops/", "└── ..."], size=26) + '</div></div>'
                '<div class="rmc"><div class="k">02</div><div class="t c">The agents</div><div class="ico">'
                + tiles([("●", "", "on"), ("●", "", "on"), ("●", "", "on"), ("●", "", "on")], cols=2) + '</div></div>'
                '<div class="rmc"><div class="k">03</div><div class="t c">The loop</div><div class="ico" style="justify-content:center">'
                + cycle([("", ""), ("", ""), ("", "")], r=110, size=280).replace('class="cn ', 'style="display:none" class="cn ') + '</div></div>'
                '</div>',
        "say": ["Today we go over three things.",
                "First, the repo: how one folder holds the whole operation and why nothing in it gets built twice.",
                "Second, the agents: four of them, and the incident behind each one.",
                "Third, the loop: the rules that keep every number honest, and the day and the week that run it."]},
    "regions": [
        {"num": "01", "label": "The repo", "sec": 25,
         "on": "Region 01 framed: seven zones, from the repo tree to the article skill.",
         "say": ["Section one. The repo.", "One folder, and the one rule that stops it collapsing."],
         "zones": [
             {"id": "tree", "num": "01", "tag": "the repo", "sec": 64,
              "on": "The screen-safe repo tree. skills/, .claude/agents/ and ops/ highlighted. accounts/ is redacted.",
              "head": "One repo. Eleven areas.",
              "body": tree(REPO_TREE, hl=("├── skills/", "├── .claude/agents/", "MAP.md"), size=19),
              "say": ["Here is the repo. One folder, eleven top-level areas.",
                      "skills holds the how. .claude/agents holds the four agents. ops holds the conventions, the map, the daily system and the tools.",
                      "The accounts folder is redacted on purpose. Client names never go on camera.",
                      "Walk the tree top to bottom, slowly. This is the frame people pause on."]},
             {"id": "map", "num": "01", "tag": "the repo", "sec": 52,
              "on": "A window on ops/MAP.md: eleven rows, area and what it owns.",
              "head": "One file maps everything.",
              "body": map_window(hot=("skills/", ".claude/agents/", "ops/")),
              "say": ["Every area has an owner and an entry point, and all of it is indexed in one file, ops/MAP.md.",
                      "When an agent starts work, this is the first file it reads. If a thing is not in here, the agent cannot know it exists.",
                      "Keep that in mind, because it is the cause of the incident in two frames."]},
             {"id": "folders", "num": "01", "tag": "the repo", "sec": 60,
              "on": "Eight folder tiles: content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting. Label: 73 files.",
              "head": "73 skills, split by activity.",
              "body": '<div style="width:100%">' + tiles([(f, "", "on" if f in ("content/", "ops/") else "") for f in FOLDERS], cols=4)
                      + '<div style="margin-top:26px;text-align:center">' + lbl("skills/ &middot; 73 markdown files &middot; 8 folders &middot; counted 2026-09-07") + '</div></div>',
              "say": ["The skills folder. 73 markdown files across eight folders.",
                      "Each folder is an activity: content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting.",
                      "73 is a count on one date. It is a snapshot, and the number is bigger today."]},
             {"id": "client-vs-activity", "num": "01", "tag": "before / after", "sec": 60,
              "on": "Before: three client folders, each with its own copy of the same skill, one crossed out. After: one activity folder, one skill, three accounts pointing at it.",
              "head": "Client folders rot.",
              "body": split(
                  tree(["client-a/", "└── article-skill.md", "client-b/", "└── article-skill.md", "client-c/   (client left)", "└── article-skill.md"],
                       red=("client-c",), size=31)
                  + lbl("the same skill, rebuilt per client"),
                  tree(["skills/content/", "└── x-articles/", "      ▲    ▲    ▲", "  acct-a acct-b acct-c"], hl=("x-articles",), size=31)
                  + lbl("one skill, every account reads it")),
              "say": ["Before: you split by client. Each client folder gets its own copy of the article skill.",
                      "The client leaves, the folder rots, and the same skill gets rebuilt inside the next client folder.",
                      "After: you split by activity. One article skill. Every account reads the same file.",
                      "An activity survives every client. A client folder does not."]},
             {"id": "incident", "num": "01", "tag": "worked example", "sec": 74,
              "on": "A four-step timeline dated 2026-09-01: agent writes an outbound-reply SOP, pushes it, finds outbound-calls/ held a better one, deletes its own. Red tag on the time lost.",
              "head": "The SOP that already existed.",
              "body": '<div style="width:100%">' + flow([
                  ("writes a SOP", "outbound reply, from scratch", ""),
                  ("pushes it", "looks finished", ""),
                  ("finds outbound-calls/", "a better one, already there", "on"),
                  ("deletes its own", "work thrown away", "red")]) +
                      '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
                      + lbl("2026-09-01 &middot; recorded in ops/MAP.md") + needs("time lost, 45 min per MAP.md, sign-off") + '</div></div>',
              "say": ["Here is the worked example. On the first of September an agent wrote a full outbound-reply SOP from scratch and pushed it.",
                      "Then it found that the outbound-calls folder already held a better one. The new one got deleted.",
                      "[NEEDS: say the time lost only after Mauro signs off the 45-minute figure.]",
                      "The agent was not careless. That folder was not in the routing table, so it had no way to know."]},
             {"id": "route-rule", "num": "01", "tag": "the rule", "sec": 60,
              "on": "A routing table window: four rows lead to a skill, the outbound reply row is red, its folder not listed.",
              "head": "Unrouted work gets built twice.",
              "body": window("routing table", "".join([
                  '<div class="row"><b>article from transcript</b><span>skills/content/x-articles/</span></div>',
                  '<div class="row"><b>monday analysis</b><span>skills/ops/monday-acquisition-analysis.md</span></div>',
                  '<div class="row"><b>board build</b><span>skills/miro/</span></div>',
                  '<div class="row"><b>lead magnet</b><span>skills/lead-gen/lead-magnet/</span></div>',
                  '<div class="row bad"><b>outbound reply</b><span>outbound-calls/ &nbsp;not listed</span></div>']), style="width:1250px"),
              "say": ["So this is the rule the whole repo runs on. Work is not finished until it is routed.",
                      "A skill that is not in the map and not in the routing table is invisible. Invisible is worse than missing, because the next agent builds a second one.",
                      "Every time I finish a skill, the last step is a row in this table."]},
             {"id": "x-articles", "num": "01", "tag": "open one skill", "sec": 64,
              "on": "skills/content/x-articles/ opened: seven numbered blocks in a chain, the seventh one dark. One corpus file under it.",
              "head": "One skill set, opened up.",
              "body": '<div style="width:100%">' + flow([
                  ("subject", "1", ""), ("first screen", "2", "on"), ("title", "3", ""), ("cover", "4", ""),
                  ("body", "5", ""), ("companion", "6", ""), ("keeper", "7", "dark")], cls="sm xa")
                      + '<div style="margin-top:40px;display:flex;justify-content:space-between">'
                      + lbl("skills/content/x-articles/") + lbl("every number cited: one corpus file, 41 real captures") + '</div></div>',
              "say": ["Let me open one skill set so you see what is inside. This is the X article set.",
                      "Six files in a fixed order turn any transcript into a published article. The seventh one keeps the other six honest as new evidence lands.",
                      "Every number they cite lives in one corpus file, built from 41 real captures.",
                      "I made a whole video on this one. It is linked at the end."]},
         ]},
        {"num": "02", "label": "The agents", "sec": 25,
         "on": "Region 02 framed: the four agents, the chart, the tools.",
         "say": ["Section two. The agents.", "An agent runs without me asking. All four of mine exist because something got missed."],
         "zones": [
             {"id": "scars", "num": "02", "tag": "the agents", "sec": 68,
              "on": "Four agent cards, each with the incident that created it.",
              "head": "Every agent is a scar.",
              "body": tiles([("performance-loop.md", "reach fell 64%. unseen for two months.", "on"),
                             ("signal-sweep.md", "an ask buried in a chat thread.", ""),
                             ("board-qa.md", "boards went out unrecordable.", ""),
                             ("youtube-lead-magnet.md", "packaging drift.", "")], cols=2),
              "say": ["Four agents. Every one of them is a scar.",
                      "performance-loop exists because reach fell and nobody saw it. signal-sweep exists because an ask got buried in a chat.",
                      "board-qa exists because boards went out that could not be read to camera. youtube-lead-magnet exists because the packaging drifted.",
                      "Its first instruction is to run the existing skill and never invent rules."]},
             {"id": "drop", "num": "02", "tag": "worked example", "sec": 60,
              "on": "Two bars: monthly impressions in June indexed to 100, August at 36. Label: unnoticed for two months.",
              "head": "Impressions fell 64%. Nobody noticed.",
              "body": bars([("June 2026", 100, "#52B788", "100"), ("August 2026", 36, "#B42318", "36")], w=900, h=500)
                      + '<div style="display:flex;flex-direction:column;gap:18px;max-width:380px">'
                      + '<div class="tag3" style="background:#FBE3E0;color:#B42318;border-color:#B42318">&minus;64%</div>'
                      + lbl("monthly impressions, indexed, June = 100") + lbl("unnoticed for two months") + '</div>',
              "say": ["The worked example for this section. Monthly impressions fell 64 percent between June and August.",
                      "Nobody noticed for two months. Me included.",
                      "The bars are indexed to June so you see the size of the drop. I am not showing the raw count here."]},
             {"id": "drop-ba", "num": "02", "tag": "before / after", "sec": 52,
              "on": "Before: a June to August strip with the drop found at the end. After: performance-loop.md reads the numbers and flags the drop.",
              "head": "Now an agent watches it.",
              "body": split(
                  flow([("June", "", ""), ("July", "", ""), ("August", "found here", "red")], cls="sm")
                  + lbl("two months to notice"),
                  flow([("monthly export", "", ""), ("performance-loop.md", "", "dark"), ("flag", "", "on")], cls="sm")
                  + lbl("catches a reach drop before it becomes a quarter")),
              "say": ["Before: a person was supposed to notice. Two months went by.",
                      "After: the performance-loop agent reads the numbers and flags the drop. Its job is to catch a reach drop before it becomes a quarter."]},
             {"id": "sweep", "num": "02", "tag": "signal-sweep", "sec": 56,
              "on": "A chat app mock: channel list, one two-message group DM highlighted, an arrow to signal-sweep.md and a ranked list of asks.",
              "head": "The ask buried in a chat.",
              "body": window("chat, 2026-08-14", '<div style="display:flex;gap:26px;width:760px">'
                             '<div style="width:200px">' + skel([90, 70, 80, 60, 85, 75]) + '<div class="sk hot" style="width:95%;height:30px"></div>' + skel([65, 80]) + '</div>'
                             '<div style="flex:1">' + skel([100, 90, 95, 70]) + '</div></div>')
                      + flow([("signal-sweep.md", "reads every channel", "dark"), ("ranked asks", "what people asked for", "on")], cls="sm").replace('class="flow sm"', 'class="flow sm" style="width:640px"'),
              "say": ["signal-sweep. On the fourteenth of August, a catch-up missed a two-message group DM. That DM held the one number that mattered that week.",
                      "Worse, the catch-up showed an auto-generated queue as if it were the client's priorities.",
                      "Now an agent reads every channel and pulls out what people actually asked for, ranked."]},
             {"id": "gates", "num": "02", "tag": "board-qa", "sec": 56,
              "on": "Fifteen check boxes in a 5 by 3 grid. The first four are red blockers. The question on top: can this be read to camera without stopping.",
              "head": "Fifteen checks before I record.",
              "body": '<div style="width:100%">' + lbl("can this be read to camera without stopping?") + '<div style="height:20px"></div>'
                      + tiles([(f"{i:02d}", "blocker" if i <= 4 else "check", "red" if i <= 4 else "sage") for i in range(1, 16)], cols=5)
                      + '</div>',
              "say": ["board-qa answers one question through fifteen checks. Can this board be read to camera without stopping?",
                      "The first four are blockers. If one fails, the run stops there.",
                      "You are looking at a board that went through it."]},
             {"id": "tools", "num": "02", "tag": "the tools", "sec": 60,
              "on": "A grid of script file chips from ops/tools/, nine named, one chip for the other sixteen.",
              "head": "25 scripts, one per number.",
              "body": '<div style="display:flex;flex-wrap:wrap;gap:18px;justify-content:center;max-width:1300px">'
                      + "".join(f'<span class="chip">{n}</span>' for n in ["impressions-vs-calls.py", "consolidate-exports.py", "post-to-call.py",
                                                                          "trace-bookings.py", "call-structure.py", "article-title-features.py",
                                                                          "lane-tables.py", "backlog-sync.py", "build-dashboard.py"])
                      + '<span class="chip on">+16 more</span></div>',
              "src": "ops/tools/ &middot; 25 scripts",
              "say": ["ops/tools holds 25 scripts. They exist because of one convention: the analysis that produced a number gets saved as a script.",
                      "An inline calculation is lost at the next context clear. Then somebody re-derives it a bit differently, and two numbers disagree in a meeting."]},
             {"id": "limits", "num": "02", "tag": "worked example", "sec": 64,
              "on": "A docstring window, paraphrased, in capitals: measures all inbound. Two bars: 649 of 678 rows under one owner, UTM empty on 673 of 678.",
              "head": "Every script states its limit.",
              "body": '<div style="display:flex;flex-direction:column;gap:30px;align-items:center">'
                      + window("ops/tools/ · opening docstring, paraphrased",
                               '<div style="color:#1B4332;font-weight:700">"""<br>MEASURES ALL INBOUND BOOKINGS,<br>EVERY OWNER.<br>"""</div>', style="width:900px")
                      + '<div>' + hbar("one owner", 649, 678, "649 / 678", "#E9B949", 760) + hbar("UTM empty", 673, 678, "673 / 678", "#B42318", 760) + '</div></div>',
              "src": "Calendly rows",
              "say": ["Every script states its own limit in its opening docstring.",
                      "One tool was named as if it measured one account's bookings. It measures all inbound, because 649 of 678 Calendly rows sit under one owner, and the UTM field is empty on 673 of them.",
                      "The name claimed something the data cannot support. So now the docstring says so, in capitals.",
                      "This is also why I gave you a total at the start and no channel split."]},
         ]},
        {"num": "03", "label": "The loop", "sec": 25,
         "on": "Region 03 framed: the conventions, the claim that measured backwards, the day, the week, the gap.",
         "say": ["Section three. The loop.", "What keeps it honest, and what runs it every day and every week."],
         "zones": [
             {"id": "nine", "num": "03", "tag": "the conventions", "sec": 52,
              "on": "Nine rule tiles, four lit: evidence tag, number to script, script states limit, dated decisions.",
              "head": "Nine rules. Four carry it.",
              "body": tiles([("tag", "every claim", "on"), ("trace", "every number to a script", "on"), ("limit", "every script", "on"),
                             ("date", "every decision", "on"), ("", "", "off"), ("", "", "off"), ("", "", "off"), ("", "", "off"), ("", "", "off")], cols=3),
              "src": "ops/CONVENTIONS.md",
              "say": ["Nine conventions in one file. Four of them carry the weight.",
                      "Every claim carries an evidence tag. Every number traces to a script and a dataset. Every script declares its limit. Decisions are dated lines in the file they govern."]},
             {"id": "backwards", "num": "03", "tag": "worked example", "sec": 64,
              "on": "Two bars: the worked example section at 60,000, the winning section at 264,000.",
              "head": "This claim measured backwards.",
              "body": bars([("the worked example", 60000, "#B42318", "60,000"), ("the winning section", 264000, "#52B788", "264,000")], w=1000, h=520),
              "src": "the skill said: the worked example converts",
              "say": ["Here is why the tags exist. A skill said the worked example was the section that converts.",
                      "We measured it. 60,000 against the winning section's 264,000. The opposite direction.",
                      "It felt obviously true. That is exactly the kind of claim that needs a tag."]},
             {"id": "tags-ba", "num": "03", "tag": "before / after", "sec": 56,
              "on": "Before: an untagged claim, struck through. After: the three tags, measured, observed, assumed, each with what it needs.",
              "head": "Tag it or delete it.",
              "body": split(
                  '<div class="chip red strike" style="font-size:28px">the worked example converts</div>' + lbl("an assertion. deleted on sight"),
                  '<div style="display:flex;flex-direction:column;gap:16px;align-items:flex-start">'
                  '<div class="trow"><span class="tag3" style="background:#52B788">[measured]</span>' + lbl("script + dataset") + '</div>'
                  '<div class="trow"><span class="tag3" style="background:#E9B949">[observed]</span>' + lbl("seen, not counted") + '</div>'
                  '<div class="trow"><span class="tag3" style="background:#fff">[assumed]</span>' + lbl("a judgement") + '</div></div>'),
              "say": ["Before: a claim with no tag. It reads like a fact.",
                      "After: three tags. Measured names a script and a dataset. Observed was seen but not counted. Assumed is a judgement, stated as one.",
                      "An untagged claim gets deleted on sight."]},
             {"id": "dated", "num": "03", "tag": "the conventions", "sec": 48,
              "on": "skills/ops/daily-ops.md with one dated line highlighted: 2026-08-31, v3, plan from BACKLOG.md, tick from Google Tasks.",
              "head": "Decisions live in the file.",
              "body": window("skills/ops/daily-ops.md", skel([80, 65, 90]) +
                             '<div class="row hot"><b>2026-08-31</b><span style="color:#1B4332">v3: plan from BACKLOG.md, tick from Google Tasks</span></div>'
                             + skel([75, 85, 60]), style="width:1250px"),
              "say": ["Decisions are dated lines in the file whose behaviour they change. Not in chat, not in a separate log.",
                      "This is the line that created version three of my daily system. Which is the next frame."]},
             {"id": "day", "num": "03", "tag": "the day", "sec": 64,
              "on": "A flow: BACKLOG.md, the weekly spine, Google Tasks, done, written back. Above it, v2 struck: calendar blocks with no done state.",
              "head": "Backlog in. Tick back.",
              "body": '<div style="width:100%;display:flex;flex-direction:column;gap:40px;align-items:center">'
                      + '<div class="chip red strike">v2: calendar blocks, no done state</div>'
                      + flow([("BACKLOG.md", "the standing list", ""), ("weekly spine", "the week's plan", ""), ("Google Tasks", "created each morning", "on"),
                              ("done", "ticked by me", "sage"), ("written back", "into the worklog", "dark")])
                      + '</div>',
              "say": ["The day. Version two put work on calendar blocks, and a block has no done state.",
                      "So the end of day guessed completion from Notion, Slack and call transcripts, and it guessed wrong for two months.",
                      "Version three: the plan comes out of the backlog, the tasks go to Google Tasks, and the tick comes back from there."]},
             {"id": "week", "num": "03", "tag": "the week", "sec": 60,
              "on": "A cycle of four: Monday acquisition analysis, content loop, Miro control panel lane, performance, back to the analysis.",
              "head": "Monday closes the loop.",
              "body": cycle([("Monday acquisition analysis", "dark"), ("content loop", "on"), ("Miro control panel lane", ""), ("performance", "")], r=235, size=600),
              "say": ["The week. Monday runs the acquisition analysis, then the content loop, then a lane on the Miro control panel.",
                      "The lane carries last week's performance, this week's hypothesis and the implementation. Then performance feeds next Monday.",
                      "The whole engine is this loop. Every other file is something the loop reads or writes."]},
             {"id": "gap", "num": "03", "tag": "what it does not do", "sec": 52,
              "on": "Four agent tiles labelled defensive, and a fifth red tile: reaches a human, none yet.",
              "head": "Nothing here books a call.",
              "body": tiles([("performance-loop", "defensive", "sage"), ("signal-sweep", "defensive", "sage"), ("board-qa", "defensive", "sage"),
                             ("youtube-lead-magnet", "defensive", "sage"), ("reaches a human", "none yet", "red")], cols=5),
              "say": ["What this system does not do. Every agent here is defensive. It catches a drop, catches a missed ask, gates a board, packages an asset.",
                      "Nothing in the repo reaches out to a human. That gap is the next video."]},
         ]},
    ],
    "cta": {"id": "cta", "num": "", "tag": "", "cls": "dark", "sec": 45,
            "on": "Dark card: Agency Booked Calls, and Link in the description.",
            "head": "",
            "vcls": "col",
            "body": '<div class="bign" style="color:#E9B949;font-size:150px;letter-spacing:-.04em;text-align:center;line-height:1">'
                    + c("Agency Booked Calls", tag="span") + '</div>'
                    + '<div class="bigl c" style="color:#fff">Link in the description</div>',
            "say": ["If you run an established agency and you want this installed for your own inbound, that is what Agency Booked Calls is.",
                    "The link is in the description. Everyone else, steal the structure and tell me in the comments what you would add."]},
    "final": {"sec": 15, "on": "The whole map again, zoomed out.",
              "say": ["So that is the whole map. The repo, the agents, the loop.", "Pause here if you want to screenshot it."]},
}
