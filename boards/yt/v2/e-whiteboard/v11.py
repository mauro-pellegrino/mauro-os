"""Doc 11: the Claude Code content system (flagship). Source: research/video-knowledge/11-claude-code-content-system.md.

Titles and thumbnails for 11 belong to another agent: TITLES is empty and there is no thumbs file.
Working title on frame 1 only.

Numbers on screen, each with its brand/claims.md row: 150+ qualified booked calls in 2026 (total,
no channel split, per the attribution note); "The content system, as published 2026-09-10" block
(eleven areas, 73 skills in eight folders, 25 scripts, four agents, nine conventions with four
load-bearing, 64% June to August, fifteen checks, 649 / 678 / 673, 60,000 against 264,000);
41 captures ("Article evidence"); 185 tasks / 0 ticked ("Mauro's own system, 2026-10-07", tagged
for sign-off). No revenue figure anywhere: the doc's $100k / $150k / $500k are all out.
"""
import os
from lib import *  # noqa: F401,F403
import lib

SLUG = "11-claude-code-content-system"
TITLE = "My whole Claude Code content system"
TITLES = []
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))


def tree_lines():
    p = os.path.join(ROOT, "research/video-knowledge/assets/repo-tree-screen-safe.txt")
    ls = [l.rstrip("\n") for l in open(p) if l.strip()]
    ls = [l for l in ls if not l.startswith(("Counts verified", "Account folder"))]
    out = []
    for l in ls:
        l = l.replace("growthub-os/", "repo/       ")
        out.append((l[:33] + l[33:].strip()).rstrip())
    return out


def folder(s, x, y, w, h, label=None, fill=False, size=30):
    add(s, wline(x, y + 18, x + w * .35, y + 18) + wline(x + w * .35, y + 18, x + w * .42, y) +
        wline(x + w * .42, y, x + w * .62, y) + wline(x + w * .62, y, x + w * .66, y + 18))
    box(s, x, y + 18, w, h - 18, label, fill=fill, size=size)


def chip(s, x, y, t, size=30):
    w = int(len(t) * size * .62) + 30
    box(s, x, y, w, size + 30)
    add(s, '<text x="%d" y="%d" font-size="%d" style="font-family:\'JetBrains Mono\',monospace;font-weight:700">%s</text>'
        % (x + 15, y + size + 6, size, lib.esc(t)))


def frames():
    out = []

    # ---------------- HOOK ----------------
    f = frame("My whole Claude Code content system", hl="content system", secs=12, notes=(
        "This is the content system behind more than 150 qualified booked calls for the agency I run "
        "this year. That number is the total from the Calendly export, every channel together, and later "
        "in this video I show you why I cannot split it cleanly by channel.\n\n"
        "Today you see the whole thing, the actual repo."))
    ellipse(0, 560, 500, 230, 170, fill=True, w=6)
    num(0, 560, 545, "150+", 130)
    text(1, 560, 740, "qualified calls booked, 2026", 40, anchor="middle", font="c", bold=True, kind="c")
    text(1, 560, 800, "for the agency I run", 34, anchor="middle", font="k", color=GREY, kind="c")
    folder(1, 1000, 330, 400, 300, "repo/", size=56)
    arrow(1, 980, 480, 810, 500, bend=30)
    out.append(f)

    f = frame("One repo. All of it.", hl="All of it", secs=8, notes=(
        "You have heard people say they built a system in Claude Code, and you have never seen the repo. I am going to open mine, folder by folder, and "
        "show you the parts that took the longest to get right. By the end you will know how to lay out "
        "your own so it does not rot."))
    folder(0, 470, 230, 660, 560, fill=False)
    for i in range(6):
        line(1, 540, 380 + i * 64, 540 + 360 + (i % 3) * 80, 380 + i * 64, w=3, color=GREY)
    ellipse(2, 1270, 300, 60, 60)
    add(2, wline(1312, 342, 1390, 420, w=7))
    out.append(f)

    f = frame("Today", secs=10, notes=(
        "Three parts today. First the skeleton: the folders, the map, and the two worked examples I open "
        "every week. Second the four agents, and the incident behind each one. Third what keeps the numbers "
        "honest, including the claim that measured backwards."))
    agenda(0, 200, 330, ["The skeleton", "The agents", "Keeping it honest"], gap=170)
    out.append(f)

    # ---------------- SECTION 1 ----------------
    out.append(section_card(1, "The skeleton", 20, (
        "Part one, the skeleton. One repo, and an index that every agent reads first.")) or lib.F)

    f = frame("Eleven areas, one map", hl="one map", secs=70, notes=(
        "Here is the repo. One repo, eleven top-level areas, all indexed in one file called MAP.md.\n\n"
        "Skills, the agents, ops with the conventions and the tools, research, the accounts, the weekly "
        "acquisition analysis, the outbound motion and the backlog. The account folder names are redacted on "
        "purpose."))
    tl = tree_lines()
    rows = [i for i, l in enumerate(tl) if "MAP.md" in l]
    code(0, 150, 166, tl, size=20, lh=1.3, hl_rows=rows, w=1300)
    out.append(f)

    f = frame("Route it or it gets rebuilt", hl="rebuilt", secs=55, notes=(
        "The rule that holds it together: work is not finished until it is routed into the map. If a thing "
        "exists and is not in the map, the next agent rebuilds it.\n\n"
        "That rule was written the day an agent rebuilt an outbound SOP from scratch, because the one we "
        "had was not in the map. [The doc says this cost 45 minutes. There is no claims row for that, so do "
        "not say the number until it is signed off.]"))
    box(0, 230, 270, 340, 420, "outbound SOP", size=40)
    text(0, 400, 740, "not mapped", 40, anchor="middle", font="c", bold=True)
    arrow(1, 620, 480, 900, 480, bend=-40, w=6)
    box(1, 960, 270, 340, 420, "outbound SOP", size=40)
    text(1, 1130, 740, "rebuilt", 44, anchor="middle", font="c", bold=True)
    needs(2, 800, 845, "45 min lost, no claims row", size=26, anchor="middle")
    out.append(f)

    f = frame("73 skills, 8 folders", hl="73 skills", secs=55, notes=(
        "The skills folder. 73 markdown files across eight folders: content, research, ops, miro, lead-gen, "
        "youtube, creative-strategy and dm-setting.\n\n"
        "Each folder is an activity, a kind of work that happens every week."))
    for i, n in enumerate(["content", "research", "ops", "miro", "lead-gen", "youtube", "creative-strategy", "dm-setting"]):
        r, c = divmod(i, 4)
        folder(0 if i < 4 else 1, 130 + c * 345, 260 + r * 290, 300, 210, n, fill=(n == "content"), size=32)
    out.append(f)

    f = frame("Split by activity", hl="activity", secs=65, notes=(
        "Before and after. Before, you split by client: a folder per client, and the same skill sits inside "
        "each one. When the client leaves, the folder rots, and the skill gets rebuilt inside the next "
        "client's folder.\n\n"
        "After, you split by activity. Content, research, ops. An activity survives every client."))
    text(0, 380, 240, "before", 48, anchor="middle", font="c", bold=True)
    for i, n in enumerate(["client A", "client B", "client C"]):
        folder(0, 160, 280 + i * 190, 260, 150, n, size=30)
        box(0, 450, 320 + i * 190, 150, 80, "skill", size=28)
    cross(1, 290, 745, 60)
    line(2, 800, 230, 800, 860, w=3, color=GREY)
    text(2, 1180, 240, "after", 48, anchor="middle", font="c", bold=True)
    for i, n in enumerate(["content", "research", "ops"]):
        folder(2, 1000, 280 + i * 190, 360, 150, n, fill=(i == 0), size=34)
    out.append(f)

    f = frame("Worked example: the article set", hl="article set", secs=60, notes=(
        "First worked example, the article skills. Six files run in a fixed order and turn any transcript "
        "into a published article. A seventh file has one job: keeping the other six honest as new evidence "
        "lands.\n\n"
        "Every number they cite lives in one corpus file, built from 41 real captures."))
    for i in range(6):
        box(i // 2, 110 + i * 200, 440, 150, 190, str(i + 1), size=60, bold=True)
        if i:
            arrow(i // 2, 110 + i * 200 - 44, 535, 110 + i * 200 - 8, 535, w=3.6)
    box(3, 520, 230, 360, 120, "keeps them honest", fill=True, size=34)
    arrow(3, 700, 352, 700, 432, w=3.6)
    folder(4, 1300, 640, 230, 170, "corpus", size=34)
    num(4, 1415, 610, "41", 64)
    text(4, 1415, 870, "real captures", 36, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Worked example: the Monday analysis", hl="Monday", secs=55, notes=(
        "Second worked example, the Monday acquisition analysis. A fixed set of inputs, a fixed structure, "
        "a diff against last week on every metric, and registers that carry forward so nothing falls off "
        "silently."))
    flow(0, 90, 400, ["inputs", "fixed sections", "weekly diff", "registers carried"], w=300, h=150, gap=70,
         fill_idx=(2,), size=36)
    out.append(f)

    f = frame("Save the script behind the number", hl="script", secs=55, notes=(
        "The tools folder holds 25 Python scripts. They exist because of one convention: the analysis that "
        "produced a number gets saved as a script.\n\n"
        "An inline calculation is gone at the next context clear. Then somebody re-derives it slightly "
        "differently, and the two numbers disagree in a meeting."))
    code(0, 150, 220, ["ops/tools/", "  impressions-vs-calls.py", "  consolidate-exports.py", "  post-to-call.py",
                       "  trace-bookings.py", "  call-structure.py", "  article-title-features.py", "  lane-tables.py",
                       "  backlog-sync.py", "  build-dashboard.py", "  ..."], size=28, w=640)
    ellipse(1, 1150, 500, 200, 150, fill=True)
    num(1, 1150, 520, "25", 120)
    text(1, 1150, 590, "scripts", 40, anchor="middle", font="c", bold=True)
    out.append(f)

    # ---------------- SECTION 2 ----------------
    out.append(section_card(2, "Four agents, four scars", 20, (
        "Part two, the agents. There are four, and every one of them exists because something got missed.")) or lib.F)

    f = frame("An agent runs without being asked", hl="without being asked", secs=50, notes=(
        "First the difference. A skill runs when I call it. An agent runs without being asked.\n\n"
        "So an agent only makes sense for a job where I already know what good looks like."))
    text(0, 400, 260, "skill", 56, anchor="middle", font="c", bold=True)
    ellipse(0, 260, 470, 60, 60)
    arrow(0, 330, 470, 440, 470, w=5)
    box(0, 460, 420, 200, 100, "skill", size=36)
    text(0, 400, 640, "you call it", 42, anchor="middle", font="c", bold=True)
    line(1, 800, 230, 800, 860, w=3, color=GREY)
    text(1, 1200, 260, "agent", 56, anchor="middle", font="c", bold=True)
    ellipse(1, 1030, 470, 70, 70)
    add(1, wline(1030, 470, 1030, 420, w=5) + wline(1030, 470, 1068, 490, w=5))
    arrow(1, 1110, 470, 1210, 470, w=5)
    box(1, 1230, 420, 220, 100, "agent", fill=True, size=36)
    text(1, 1200, 640, "runs alone", 42, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Impressions fell 64%. Nobody noticed.", hl="Nobody noticed", secs=65, notes=(
        "This is the worked example for this part. Scar one. Monthly impressions fell 64% between June and August 2026, and nobody noticed for two "
        "months.\n\n"
        "That is why the performance-loop agent exists. The bars are indexed to June, so June is 100 and "
        "August is 36."))
    bars(0, 330, 760, [("June", 100, "100", False), ("August", 36, "36", True)], maxv=100, maxh=470, bw=200, gap=200)
    text(1, 1150, 420, "-64%", 90, anchor="middle", font="k", bold=True, kind="x")
    text(1, 1150, 500, "unnoticed, two months", 40, anchor="middle", font="c", bold=True, kind="c")
    chip(2, 1000, 640, "performance-loop")
    text(0, 160, 860, "monthly impressions, June = 100", 30, font="k", color=GREY, kind="c")
    out.append(f)

    f = frame("The ask buried in a group DM", hl="buried", secs=55, notes=(
        "Scar two. A catch-up missed a two-message group DM that held a key number, and "
        "it presented an auto-generated queue as if it were the client's priorities.\n\n"
        "The signal-sweep agent reads every channel and pulls out the asks, so a buried message does not "
        "get lost again."))
    for i, (x, w) in enumerate([(200, 520), (420, 600), (200, 380), (420, 560)]):
        box(0, x, 240 + i * 120, w, 80)
    box(0, 200, 720, 180, 70)
    circle_around(1, 290, 755, 140, 70)
    chip(2, 1150, 560, "signal-sweep")
    arrow(2, 1140, 590, 460, 750, bend=30)
    out.append(f)

    f = frame("One question: can you read it?", hl="read it", secs=50, notes=(
        "Scar three. Boards were going out that could not be recorded straight through. The board-qa "
        "agent answers one question through fifteen checks: can this be read to camera without stopping."))
    for i in range(15):
        r, c = divmod(i, 5)
        box(0, 160 + c * 190, 260 + r * 150, 150, 110, fill=(i < 4))
    chip(1, 1150, 420, "board-qa")
    num(1, 1260, 600, "15", 100)
    text(1, 1260, 660, "checks", 40, anchor="middle", font="c", bold=True)
    text(2, 540, 760, "first four block", 44, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("First rule: run the existing skill", hl="existing skill", secs=45, notes=(
        "Scar four is packaging drift. Each lead magnet package came out a little different. The "
        "youtube-lead-magnet agent's first instruction is to run the existing skill and never invent rules."))
    for i in range(4):
        box(0, 170 + i * 70 + lib.j(30), 280 + i * 120, 260, 90)
    text(0, 380, 820, "drift", 46, anchor="middle", font="c", bold=True)
    line(1, 800, 230, 800, 860, w=3, color=GREY)
    for i in range(4):
        box(1, 1060, 280 + i * 120, 260, 90, fill=(i == 0))
    chip(1, 930, 800, "youtube-lead-magnet", size=26)
    out.append(f)

    f = frame("All four are defensive", hl="defensive", secs=55, notes=(
        "Put the four side by side. performance-loop catches a reach drop. signal-sweep catches a missed ask. "
        "board-qa catches a board you cannot record. youtube-lead-magnet catches packaging drift.\n\n"
        "Every one of them catches something. None of them reaches out to a human."))
    rows = [("performance-loop", "a reach drop"), ("signal-sweep", "a missed ask"),
            ("board-qa", "an unrecordable board"), ("youtube-lead-magnet", "packaging drift")]
    box(0, 150, 230, 1300, 600)
    line(0, 760, 230, 760, 830)
    for i, (a, b) in enumerate(rows):
        if i:
            line(i, 150, 230 + i * 150, 1450, 230 + i * 150, w=3)
        add(i, '<text x="190" y="%d" font-size="34" style="font-family:\'JetBrains Mono\',monospace;font-weight:700">%s</text>' % (318 + i * 150, a))
        text(i, 800, 320 + i * 150, b, 46, font="c", bold=True)
    out.append(f)

    f = frame("Every agent is a scar", hl="scar", secs=55, notes=(
        "The before and after for this whole part. Before, something gets missed, and you find out weeks "
        "later. After, the miss becomes a dated rule in the file it governs, and then the rule becomes an "
        "agent that checks for it without being asked. And it is not finished."))
    flow(0, 130, 400, ["the miss", "dated rule", "agent"], w=340, h=150, gap=120, fill_idx=(2,), size=44)
    out.append(f)

    # ---------------- SECTION 3 ----------------
    out.append(section_card(3, "Keeping it honest", 20, (
        "Part three, what keeps the numbers honest. This is the part that makes the rest worth trusting.")) or lib.F)

    f = frame("Nine conventions. Four carry it.", hl="Four carry it", secs=55, notes=(
        "There are nine conventions, and four of them carry the weight. Every claim carries an evidence tag. "
        "Every number traces to a script and a dataset. Every script declares its own limit. And decisions "
        "are dated lines in the file whose behaviour they govern."))
    labs = {0: "evidence tag", 1: "number to script", 2: "script states limit", 3: "dated decisions"}
    for i in range(9):
        r, c = divmod(i, 3)
        box(0 if i >= 4 else 1, 200 + c * 420, 230 + r * 210, 360, 160, labs.get(i), fill=(i < 4), size=36)
    out.append(f)

    f = frame("Every claim carries a tag", hl="tag", secs=50, notes=(
        "The tags are three words: measured, observed, assumed. An untagged claim is an assertion.\n\n"
        "The 64% drop is measured. The claim that talking beats reading on camera is assumed. You say each "
        "one with its tag attached."))
    for i, (t, fl) in enumerate([("measured", True), ("observed", False), ("assumed", False)]):
        box(i, 220 + i * 410, 380, 330, 140, t, fill=fl, size=50, bold=True)
    out.append(f)

    f = frame("It felt true. It measured backwards.", hl="measured backwards", secs=65, notes=(
        "Here is why the tags exist. A skill said the worked example was the section that converts. It felt "
        "obviously true.\n\n"
        "Then we measured it. The worked example did 60,000. The winning section did 264,000. The opposite "
        "direction."))
    bars(0, 380, 760, [("worked example", 60000, "60,000", False), ("winning section", 264000, "264,000", True)],
         maxv=264000, maxh=470, bw=230, gap=280, step_each=True)
    out.append(f)

    f = frame("Every script states its limit", hl="its limit", secs=65, notes=(
        "And the scripts state their own limits. One tool was named as if it measured a single account's "
        "bookings. It measures all inbound, because 649 of 678 Calendly rows sit under one owner, and the "
        "UTM field is empty on 673 of them.\n\n"
        "The docstring now says so in capitals. This is also why the 150 calls at the start is a total, "
        "with no channel split."))
    hbars(0, 120, 300, [("all rows", 678, "678", False), ("one owner", 649, "649", True), ("UTM empty", 673, "673", True)],
          maxv=678, maxw=900, step_each=True)
    out.append(f)

    f = frame("The daily loop, honestly", hl="honestly", secs=65, notes=(
        "The day, as a before and after. Version two put blocks on the calendar, and a block had no done "
        "state, so the end of day guessed what got done and guessed wrong.\n\n"
        "Version three plans from the backlog and pushes tasks into Google Tasks, so a tick is the done state. "
        "[On screen: the claims file says 185 tasks pushed from 31 August and 0 ticked. Mauro decides "
        "whether that is said on camera.]"))
    text(0, 380, 240, "before", 48, anchor="middle", font="c", bold=True)
    for i in range(4):
        box(0, 200, 280 + i * 120, 360, 90)
    num(0, 600, 470, "?", 90)
    line(1, 800, 230, 800, 860, w=3, color=GREY)
    text(1, 1180, 240, "after", 48, anchor="middle", font="c", bold=True)
    for i in range(4):
        box(1, 1000, 290 + i * 110, 60, 60)
        line(1, 1090, 330 + i * 110, 1380, 330 + i * 110, w=3, color=GREY)
    needs(2, 1190, 820, "185 pushed, 0 ticked: Mauro's call", size=22, anchor="middle")
    out.append(f)

    f = frame("Nothing here reaches out", hl="reaches out", secs=55, notes=(
        "What this system does not do. It does not book calls on its own. Every agent in it is defensive. "
        "Nothing in the repo today reaches out to a human.\n\n"
        "That gap is the subject of the next video."))
    ellipse(0, 600, 540, 200, 170, fill=True)
    text(0, 600, 555, "the repo", 50, anchor="middle", font="c", bold=True)
    for (x, y) in [(220, 300), (220, 780), (980, 300)]:
        arrow(1, x, y, 600 + (x - 600) * .55, 540 + (y - 540) * .55)
    arrow(2, 820, 600, 1180, 720, bend=-30, color=GREY)
    box(2, 1190, 660, 260, 120, "a human", size=40)
    num(2, 1320, 620, "?", 70)
    out.append(f)

    out.append(cta(40, (
        "If you run an established agency and want a system like this installed, the offer is called Agency "
        "Booked Calls. The link is in the description.")) or lib.F)
    return out
