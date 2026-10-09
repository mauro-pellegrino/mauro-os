"""Doc 10: record off a board. Source: research/video-knowledge/10-record-off-a-board.md.

Numbers on screen, each with its brand/claims.md row ("The video board system, as written up
2026-09-16"): 4 hours by hand to close to 2; four boards a week; 200 to 400 items; the 200-item
edit ceiling (2026-08-04); 37 sent, 17 created, 20 failed (2026-08-03); four build steps; eight
files; fifteen gate checks, first four blockers. Doc 10's "59 items, zero failures" and "three of
ten top videos" have no claims row, so neither is on a frame.
"""
import os
from lib import *  # noqa: F401,F403
import lib

SLUG = "10-record-off-a-board"
TITLE = "I record off a board now"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

TITLES = [
    {"title": "This One Board Stops You Sounding Like You're Reading",
     "modelled_on": "Chris Goor - Brand Video Pro, \"This One Trick Stops You Sounding Like You're Reading a Script\" (334,757 views, YouTube search 2026-10-07)"},
    {"title": "How to Talk to Camera Without a Script (Use a Board)",
     "modelled_on": "Think Media, \"How to Talk to a Camera (Even if You've Never Done it Before!)\" (564,318 views, YouTube search 2026-10-07)"},
    {"title": "You'll Never Read a Script on Camera Again",
     "modelled_on": "Charlie Morgan, \"You'll NEVER Doomscroll Again After Watching This\" (638K, charlie-morgan-dig.md #1)"},
]

THUMBS = ["board_column", "script_vs_board", "time_bars"]


def frames():
    out = []

    # ---------------- HOOK ----------------
    f = frame("A board: 4 hours, now about 2", hl="about 2", secs=12, notes=(
        "A recording board used to take me four hours to build by hand. It is close to two hours now, "
        "and I build four of them every week.\n\n"
        "Everything you see in this video is one of those boards. I am talking off it right now."))
    bars(0, 470, 760, [("by hand", 4, "4h", False), ("now", 2, "~2h", True)], maxv=4, maxh=470, bw=190, gap=170)
    box(1, 1130, 330, 330, 150, "4 a week", fill=True, size=44, bold=True)
    out.append(f)

    f = frame("Talk off a board", hl="board", secs=8, notes=(
        "A script makes you read, and a board makes you talk. By the end of this video you can turn any "
        "script into a board you record from, without a teleprompter and without memorising anything."))
    # left: a script page full of lines
    box(0, 170, 250, 420, 560)
    for i in range(11):
        line(0, 210, 300 + i * 44, 210 + 330 - (i % 3) * 50, 300 + i * 44, w=3, color=GREY)
    text(0, 380, 860, "script", 46, anchor="middle", font="c", bold=True)
    arrow(1, 640, 530, 900, 530, bend=-30, w=6)
    column(1, 1000, 230, ["hook", "beat", "beat", "example", "CTA"], w=360, h=78, gap=30, fill_idx=(0,), size=34, step_each=False)
    text(1, 1180, 860, "board", 46, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Today", secs=10, notes=(
        "Today we go over three things. First, what a board actually is and what makes it record-ready. "
        "Second, how I build one straight from the script. Third, what breaks when a board gets big, "
        "and what that forced me to change."))
    agenda(0, 200, 330, ["The board", "The build", "What breaks"], gap=170)
    out.append(f)

    # ---------------- SECTION 1 ----------------
    out.append(section_card(1, "What a board is", 25, (
        "Section one. What a board is, and the one standard every board has to meet before I hit record.")) or lib.F)

    f = frame("Before: reading the script", hl="Before", secs=60, notes=(
        "Here is the before. I read one line from a script, straight, the way I used to record. "
        "[Read one scripted line to camera here.]\n\n"
        "You can hear it. The eyes move, the rhythm goes flat, and it sounds read. "
        "Now the same line, off the board on the next frame."))
    box(0, 300, 210, 1000, 610)
    for i in range(10):
        line(0, 350, 270 + i * 58, 350 + 900 - (i % 4) * 90, 270 + i * 58, w=3, color=GREY)
    hlrect(1, 344, 270 + 2 * 58 - 22, 760, 40)
    ellipse(2, 1380, 300, 70, 46)
    ellipse(2, 1380, 300, 22, 22, w=6)
    arrow(2, 1320, 330, 1130, 385, bend=20)
    out.append(f)

    f = frame("After: one column, one beat each", hl="one beat", secs=55, notes=(
        "And the after. A board is a single vertical column that maps the video's flow, top to bottom. "
        "Every concept gets its own container, and there are no raw walls of text.\n\n"
        "[Say the same line again, off the board.]\n\n"
        "Each box holds one beat, one point from the script. You look at the box, you remember the point, "
        "and you say it in your own words."))
    column(0, 610, 200, ["hook", "the point", "the example", "the proof", "CTA"], w=380, h=96, gap=38, fill_idx=(1,), size=36)
    text(4, 1150, 470, "one beat", 46, font="c", bold=True)
    arrow(4, 1140, 455, 1010, 400, bend=-20)
    out.append(f)

    f = frame("Record-ready means nothing missing", hl="nothing missing", secs=50, notes=(
        "The standard is record-ready. Nothing is missing, and nothing needs editing at the moment I record.\n\n"
        "If I have to stop and fix a box while the camera is on, the board was not finished. "
        "That one rule decides whether a board counts as done."))
    for i, lab in enumerate(["nothing missing", "no live edits", "one beat each"]):
        box(i, 420, 260 + i * 180, 90, 90)
        tick(i, 465, 300 + i * 180, r=30)
        text(i, 560, 325 + i * 180, lab, 54, font="c", bold=True)
    out.append(f)

    f = frame("Every section has a type", hl="type", secs=70, notes=(
        "Every beat gets a section type. Title card, section title, question hooks, a narration block, "
        "a two-path comparison, a tree, a pillar layout, a multi-column section, a sticky-note grid, "
        "label to description rows, an emphasis label and a brand badge.\n\n"
        "The palette is fixed too. Yellow for labels and pillars, light yellow for narration, lilac for "
        "section titles, green for a win, red for the negative path, and a dark three-pixel border on every "
        "filled box. That border is what gives the stacked-card look."))
    types = ["title card", "section title", "question hooks", "narration", "two-path", "tree",
             "pillars", "multi-column", "sticky grid", "label rows", "emphasis", "brand badge"]
    for i, t in enumerate(types):
        r, c = divmod(i, 4)
        box(r, 150 + c * 330, 230 + r * 205, 290, 150, t, fill=(i in (3, 4)), size=34)
    out.append(f)

    f = frame("Split at every new topic", hl="new topic", secs=55, notes=(
        "How do you cut a script into beats? I split at every new topic, at every named process, and at "
        "every clear shift in what the script is doing: explaining, demonstrating, listing, concluding.\n\n"
        "I never split mid-thought. One thought stays in one box."))
    box(0, 140, 330, 1320, 110)
    for i in range(4):
        line(0, 170 + i * 330, 385, 170 + i * 330 + 260, 385, w=3, color=GREY)
    for i, (x, lab) in enumerate([(470, "new topic"), (800, "named process"), (1130, "shift in job")]):
        add(1 + i, path("M%d 300 L%d 280 M%d 300 L%d 280" % (x - 6, x, x + 6, x), 4) + wline(x, 300, x, 470, amp=1, w=5))
        text(1 + i, x, 540, lab, 44, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("When in doubt: plain text", hl="plain text", secs=45, notes=(
        "The escape hatch. When I am not sure which container fits, I use plain centred text. "
        "Forcing content into a container that does not fit is worse than no container at all."))
    box(0, 230, 300, 300, 300)
    ellipse(0, 380, 450, 100, 100)
    cross(1, 380, 450, 150)
    text(1, 380, 700, "forced fit", 46, anchor="middle", font="c", bold=True)
    text(2, 1100, 470, "the point, centred", 60, anchor="middle", font="c", bold=True)
    underline(2, 880, 1320, 500)
    tick(2, 1100, 640, r=40)
    out.append(f)

    f = frame("Worked example: this board", hl="this board", secs=60, notes=(
        "The worked example is the board you are looking at. The script for this video went in, and it came "
        "out as a hook, three sections and a call to action.\n\n"
        "Each section holds one worked example and one before and after. That is the whole shape, and it is "
        "the same shape every time."))
    flow(0, 120, 400, ["hook", "section 1", "section 2", "section 3", "CTA"], w=220, h=120, gap=60, fill_idx=(0,), size=36)
    for i in range(3):
        x = 120 + (i + 1) * 280
        box(5, x + 20, 600, 180, 70, "example", size=28)
        box(5, x + 20, 700, 180, 70, "before/after", size=26)
    out.append(f)

    # ---------------- SECTION 2 ----------------
    out.append(section_card(2, "Build it from the script", 20, (
        "Section two. How the board gets built straight from the script. The board is built from the script, "
        "so you still write one. You just stop reading it.")) or lib.F)

    f = frame("Four steps. Only one touches the board.", hl="one", secs=60, notes=(
        "The build is four steps: beats, then components, then geometry, then the write. "
        "Only the last step, the write, touches the board.\n\n"
        "Everything before that happens in a file, where a mistake costs nothing."))
    flow(0, 110, 380, ["beats", "components", "geometry", "write"], w=290, h=140, gap=80, fill_idx=(3,), size=42)
    circle_around(4, 110 + 3 * 370 + 145, 450, 200, 120)
    text(4, 1255, 680, "the board", 44, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Beats: split, never merge", hl="never merge", secs=50, notes=(
        "Step one, the beats. The script gets split into distinct points, with no summarising and no merging. "
        "Then I check the beat count against the runtime I am aiming for, before anything else gets built."))
    box(0, 140, 260, 360, 520)
    for i in range(9):
        line(0, 175, 310 + i * 50, 175 + 290 - (i % 3) * 60, 310 + i * 50, w=3, color=GREY)
    arrow(1, 540, 520, 720, 520, w=6)
    for i in range(5):
        box(1, 780, 250 + i * 110, 360, 80, "point %d" % (i + 1), size=34)
    ellipse(2, 1370, 520, 110, 110)
    add(2, wline(1370, 520, 1370, 450, w=5) + wline(1370, 520, 1425, 545, w=5))
    text(2, 1370, 690, "runtime check", 40, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Every coordinate, computed first", hl="computed first", secs=55, notes=(
        "Step three, the geometry. Every coordinate, every height and every gap is computed up front. "
        "There is a centre axis, a running vertical stack and a width for each section type.\n\n"
        "Nothing gets nudged by hand afterwards."))
    line(0, 800, 200, 800, 860, w=3, color=GREY)
    text(0, 820, 230, "centre axis", 34, font="k", color=GREY)
    for i, w in enumerate([520, 380, 640, 380]):
        box(1 + i, 800 - w / 2, 270 + i * 140, w, 100, fill=(i == 2))
        if i:
            add(1 + i, wline(1300, 270 + i * 140 - 40, 1300, 270 + i * 140, w=3) + wline(1285, 270 + i * 140 - 40, 1315, 270 + i * 140 - 40, w=3)
                + wline(1285, 270 + i * 140, 1315, 270 + i * 140, w=3))
    text(4, 1330, 570, "gap", 36, font="c", bold=True)
    out.append(f)

    f = frame("A sticky grows. The rows drift.", hl="drift", secs=65, notes=(
        "The worked example for this part comes from the geometry step. A sticky note takes a width or a height, never "
        "both, and it grows to fit its text.\n\n"
        "What happened: I computed a fixed row pitch in advance, a sticky grew, and every row under it "
        "drifted into the next one. The fix: shapes take an explicit width and height, so the stack I "
        "computed is the stack that lands."))
    text(0, 380, 250, "before", 48, anchor="middle", font="c", bold=True)
    box(0, 220, 290, 320, 90)
    box(0, 220, 400, 320, 230, fill=True)
    box(0, 230, 590, 320, 90)
    box(0, 240, 700, 320, 90)
    circle_around(1, 390, 640, 230, 70)
    line(2, 800, 230, 800, 860, w=3, color=GREY)
    text(2, 1180, 250, "after", 48, anchor="middle", font="c", bold=True)
    for i in range(4):
        box(2, 1020, 290 + i * 130, 320, 100, fill=(i == 1))
    tick(2, 1460, 500, r=34)
    out.append(f)

    f = frame("Eight files, same order", hl="same order", secs=55, notes=(
        "The build reads eight files, in the same order every time: master, visual, archetype, writing, "
        "gotchas, assets, diagram, QA.\n\n"
        "The order is the dependency. You cannot pick a visual before you know the archetype, and you cannot "
        "run QA on something that is not built."))
    names = ["master", "visual", "archetype", "writing", "gotchas", "assets", "diagram", "QA"]
    for i, n in enumerate(names):
        r, c = divmod(i, 4)
        x, y = 120 + c * 360, 270 + r * 280
        box(r, x, y, 280, 140, n, fill=(n == "gotchas"), size=38)
        num(r, x + 22, y - 14, str(i + 1), 40, anchor="start")
        if c:
            arrow(r, x - 70, y + 70, x - 12, y + 70)
    arrow(1, 1250, 425, 330, 540, bend=-25, w=3.6)
    out.append(f)

    f = frame("Diagrams: markup, render, paste", hl="render", secs=55, notes=(
        "Diagrams are never placed by hand on the canvas, and never prompted out of an image model. "
        "They are written in markup, rendered by headless Chrome, and pasted in as an image. "
        "That has been the default since 25 August."))
    flow(0, 170, 330, ["HTML", "headless Chrome", "PNG on board"], w=340, h=140, gap=90, fill_idx=(2,), size=40)
    text(3, 420, 700, "hand-placed", 58, anchor="middle", font="c", bold=True)
    strike(3, 250, 590, 682)
    text(3, 1180, 700, "image model", 58, anchor="middle", font="c", bold=True)
    strike(3, 1010, 1350, 682)
    out.append(f)

    f = frame("Before: lasso. After: one write.", hl="one write", secs=60, notes=(
        "So the before and after for the whole build. Before, something placed wrong stayed wrong, or I "
        "lassoed it by hand in the Miro UI and dragged it around.\n\n"
        "After, the beats, the components and the geometry all live in a file, and the board gets one write. "
        "That is how four hours by hand came down to close to two."))
    for (x, y) in [(220, 300), (420, 360), (300, 520), (500, 560), (260, 680)]:
        box(0, x + lib.j(20), y, 160, 80)
    ellipse(1, 400, 520, 260, 250)
    text(1, 400, 840, "by hand", 46, anchor="middle", font="c", bold=True)
    line(2, 800, 230, 800, 860, w=3, color=GREY)
    column(2, 1030, 260, ["", "", "", ""], w=340, h=86, gap=40, step_each=False)
    text(2, 1200, 840, "one write", 46, anchor="middle", font="c", bold=True)
    out.append(f)

    # ---------------- SECTION 3 ----------------
    out.append(section_card(3, "What breaks at scale", 20, (
        "Section three, and the worked example is a real failure. What breaks when a board gets big, from the repo that has been building boards "
        "through the Miro API the longest.")) or lib.F)

    f = frame("A real board: 200 to 400 items", hl="200 to 400", secs=55, notes=(
        "A real recording board runs 200 to 400 items. Every box, every arrow and every label is an item.\n\n"
        "Keep that range in your head, because of the line on the next frame."))
    line(0, 160, 560, 1440, 560, w=5)
    for v in (0, 100, 200, 300, 400):
        x = 160 + v * 3.2
        line(0, x, 540, x, 580, w=4)
        num(0, x, 630, str(v), 40)
    hlrect(1, 160 + 200 * 3.2, 440, 200 * 3.2, 100)
    text(1, 160 + 300 * 3.2, 420, "a real board", 44, anchor="middle", font="c", bold=True, kind="c")
    out.append(f)

    f = frame("Past 200 items: create only", hl="create only", secs=55, notes=(
        "Past 200 items, the edit call parses the whole board and gives up. Creating still works. "
        "Editing and deleting do not. That was confirmed on 4 August.\n\n"
        "So on any board of real size you get one shot. Every coordinate has to be right before you send it."))
    line(0, 160, 330, 1440, 330, w=5)
    line(0, 800, 260, 800, 860, w=6)
    num(0, 800, 245, "200", 54)
    for i, (lab, ok) in enumerate([("create", True), ("edit", False), ("delete", False)]):
        y = 470 + i * 140
        text(1 + i, 1000, y, lab, 56, font="c", bold=True)
        if ok:
            tick(1 + i, 1320, y - 18, r=34)
        else:
            cross(1 + i, 1320, y - 18, r=30)
    text(1, 480, 600, "edits work", 46, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("37 sent. 17 created.", hl="17 created", secs=60, notes=(
        "On 3 August a 37-item create came back with 17 created and one error covering the other 20. "
        "The error named no item and no attribute.\n\n"
        "Two attribute values caused it, and neither was documented as invalid."))
    bars(0, 330, 780, [("sent", 37, "37", False), ("created", 17, "17", True), ("failed", 20, "20", False)],
         maxv=37, maxh=480, bw=190, gap=150, step_each=True)
    out.append(f)

    f = frame("URLs for items that never existed", hl="never existed", secs=45, notes=(
        "And the response made it worse. The response body showed plausible URLs for items that had "
        "not been created. It looked like success until you went to the board."))
    box(0, 180, 250, 560, 560)
    text(0, 460, 320, "response", 48, anchor="middle", font="c", bold=True)
    for i in range(3):
        text(0, 260, 440 + i * 120, "link %d" % (i + 1), 46, font="k")
        tick(0, 600, 425 + i * 120, r=24)
    arrow(1, 780, 530, 900, 530, w=5)
    box(1, 940, 250, 480, 560)
    text(1, 1180, 320, "board", 48, anchor="middle", font="c", bold=True)
    ellipse(2, 1180, 560, 90, 90)
    num(2, 1180, 590, "?", 90)
    out.append(f)

    f = frame("No undo means correct up front", hl="correct up front", secs=50, notes=(
        "The before and after for this part. Before the limit, a wrong box got fixed by hand. After it, the work "
        "moved into a file, a check and one write.\n\n"
        "This is my own read of it. Any system with no undo forces you to be correct up front, and being "
        "correct up front turns out to be faster than fixing.\n\n"
        "The limit made placing boxes by hand impossible, and that forced a different shape of work."))
    flow(0, 200, 380, ["file", "check", "one write"], w=320, h=140, gap=110, fill_idx=(2,), size=44)
    arrow(1, 1100, 560, 280, 560, bend=-120, color=GREY, w=3.6)
    cross(1, 690, 690, 40)
    text(1, 690, 790, "undo", 44, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("The gate: 15 checks", hl="15 checks", secs=60, notes=(
        "Before a board counts, it goes through a gate of fifteen checks. The first four are blockers, "
        "and if one of those fails, the run stops right there.\n\n"
        "Roughly half the checks run as a script. The rest need eyes."))
    for i in range(15):
        r, c = divmod(i, 5)
        box(0 if i < 4 else 1, 180 + c * 260, 250 + r * 190, 200, 140, str(i + 1), fill=(i < 4), size=56, bold=True)
    text(2, 800, 860, "first four block", 44, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Charlie Morgan records off boards", hl="boards", secs=60, notes=(
        "Charlie Morgan uses the same format. His framework videos are this exact format: a hand-drawn "
        "whiteboard or a live Miro board, narrated with a facecam in the corner. A winding road from a now "
        "state to a future state, a funnel, a named theory.\n\n"
        "Some of his most-viewed videos are this format, board plus facecam."))
    td = os.path.join(ROOT, "research/charlie-morgan/thumbs")
    for i, fn in enumerate(["04--V0q0tFzagQ.jpg", "06-k3p1sbrWiLw.jpg", "07-wedx1YS-pnw.jpg"]):
        image(i, 85 + i * 485, 380, 460, 259, lib.img_data(os.path.join(td, fn)))
    out.append(f)

    out.append(cta(40, (
        "If you run an established agency and you want this kind of content system installed for you, the "
        "offer is called Agency Booked Calls. The link is in the description.")) or lib.F)
    return out
