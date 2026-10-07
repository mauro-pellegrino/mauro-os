"""Doc 03: lead magnets. Source: research/video-knowledge/03-lead-magnets-15-minutes.md.

Restructured so nothing depends on "4 of 541": that line has no brand/claims.md row and is not
used anywhere. The measurement beat runs on the published Calendly row instead (649 of 678 under
one owner, UTM empty on 673), and it is stated as design intent, because no keyword-to-booking
join exists yet (doc 03, Gaps).

The doc's two clocks (about 15 minutes of Claude, 2 to 3 hours hands-on) have no claims row either,
so both render as [NEEDS]. The clock that is cleared is the 24-minute LinkedIn lead-magnet run
("The process-map build, run 2026-10-01"), with its two riders: about five minutes of Mauro's
attention is his estimate, and the 24 minutes only holds because the resource already existed.
"""
from lib import *  # noqa: F401,F403
import lib

SLUG = "03-lead-magnets-workflow"
TITLE = "My lead magnet workflow, start to finish"

TITLES = [
    {"title": "Watch Me Ship a Lead Magnet Post in 24 Minutes",
     "modelled_on": "Marcos Ruiz, \"Watch Me Use AI to Create 100+ Viral Twitter/X Posts in 1 Hour\" (01-outliers.csv)"},
    {"title": "Lead Magnets You Can Actually Measure (Full Workflow)",
     "modelled_on": "Greg Isenberg, \"Building AI Agents that actually work (Full Course)\" (01-outliers.csv, 566,000 views)"},
    {"title": "Build Lead Magnets With Claude: Here's How",
     "modelled_on": "David Ondrej, \"Build Everything with AI Agents: Here's How\" (01-outliers.csv, 1,700,000 views)"},
]

THUMBS = ["keyword_key", "clock24", "missing_call"]


def frames():
    out = []

    # ---------------- HOOK ----------------
    f = frame("Post to live page: 24 minutes", hl="24 minutes", secs=12, notes=(
        "On 1 October I timed one run of my LinkedIn lead magnet process. From pasting the post to a live "
        "staging page took 24 minutes, and I estimate about five of those minutes were my own attention.\n\n"
        "That only holds because the resource it promised already existed. I will show you both sides."))
    ellipse(0, 520, 520, 230, 230, fill=True, w=6)
    add(0, wline(520, 520, 520, 360, w=8) + wline(520, 520, 640, 590, w=8))
    num(1, 1100, 470, "24 min", 110)
    text(1, 1100, 560, "paste to live page", 40, anchor="middle", font="c", bold=True, kind="c")
    num(2, 1100, 690, "~5 min mine", 56)
    text(2, 1100, 750, "my estimate", 34, anchor="middle", font="k", color=GREY)
    out.append(f)

    f = frame("The part you can measure", hl="measure", secs=8, notes=(
        "Free resource in exchange for a comment is the most copied mechanic on X and LinkedIn right now. "
        "The version that gets copied is missing the measurement. By the end of this video you have the whole "
        "workflow, and the one piece of it that could tell you which post booked a call."))
    flow(0, 110, 380, ["post", "comment", "DM", "call"], w=260, h=130, gap=110, fill_idx=(2,), size=44, step_each=False)
    circle_around(1, 110 + 2 * 370 + 130, 445, 190, 110)
    out.append(f)

    f = frame("Today", secs=10, notes=(
        "Three parts. First the clock: what the time numbers actually cover. Second the build itself, phase "
        "by phase, with one run walked through. Third the keyword, and why it is the only instrument you have."))
    agenda(0, 200, 330, ["The clock", "The build", "The keyword"], gap=170)
    out.append(f)

    # ---------------- SECTION 1 ----------------
    out.append(section_card(1, "The clock", 20, (
        "Part one, the clock. Time claims are where this topic gets oversold, so I start there.")) or lib.F)

    f = frame("The mechanic, and the missing part", hl="missing part", secs=60, notes=(
        "Here is the mechanic. A post offers a free resource, people comment a keyword, they get a DM with "
        "the resource. And then nothing. There is no path from the keyword to the calendar.\n\n"
        "That missing arrow is the whole video."))
    flow(0, 90, 360, ["post", "keyword", "DM"], w=250, h=130, gap=100, size=44)
    arrow(1, 1110, 425, 1230, 425, color=GREY)
    box(1, 1250, 360, 230, 130, "calendar", size=40)
    circle_around(2, 1170, 425, 70, 80)
    num(2, 1170, 600, "?", 90)
    out.append(f)

    f = frame("Two clocks. Say both.", hl="Say both", secs=65, notes=(
        "The before and after for this part is how you talk about time. Before: you quote only the short clock. After: you say both. "
        "There are two clocks in this workflow, and they measure different things. One is the Claude pass "
        "that produces the document. The other is the full cycle: ideation, format choice, the human pass, "
        "the cover, the post copy, the DM copy and the handoff.\n\n"
        "[NEEDS sign-off before you say either number. The walkthrough says about fifteen minutes for the "
        "Claude pass. The SOP says two to three hours hands-on. Saying only the short one is the overclaim "
        "this audience has learned to distrust.]"))
    for i, (x, lab, need) in enumerate([(420, "Claude pass", "~15 min, no claims row"), (1180, "full cycle", "2-3 h, no claims row")]):
        ellipse(i, x, 470, 180, 180, fill=(i == 0), w=6)
        add(i, wline(x, 470, x, 340, w=7) + wline(x, 470, x + 90, 520, w=7))
        text(i, x, 720, lab, 54, anchor="middle", font="c", bold=True)
        needs(i, x, 810, need, size=24, anchor="middle")
    out.append(f)

    f = frame("Measured: 24 minutes", hl="24 minutes", secs=65, notes=(
        "The worked example for this part: the one clock I measured. My LinkedIn lead magnet process, 24 minutes from paste to a live staging "
        "page. Inside that, about five minutes were my attention: find the post, capture it, read the draft. "
        "The five is my estimate, the 24 is the clock.\n\n"
        "And the 24 only holds because we already had the resource built."))
    box(0, 160, 380, 1200, 130)
    num(0, 760, 360, "24 min", 64)
    box(1, 160, 380, 250, 130, fill=True)
    num(1, 285, 560, "~5 min", 52)
    text(1, 285, 610, "mine, estimated", 36, anchor="middle", font="c", bold=True, kind="c")
    box(2, 1000, 680, 460, 120, "asset already built", size=40)
    arrow(2, 1060, 670, 1180, 520, bend=-30)
    out.append(f)

    f = frame("Building the asset: not timed yet", hl="not timed", secs=50, notes=(
        "The branch where the resource does not exist yet, where you have to build the magnet itself, has "
        "no measured time. So I do not call it the slowest step, because nothing has timed it."))
    flow(0, 160, 300, ["idea", "asset exists?"], w=300, h=130, gap=110, size=42, step_each=False)
    arrow(1, 870, 365, 1100, 280, bend=-20)
    box(1, 1110, 220, 300, 110, "yes: 24 min", size=38)
    arrow(2, 870, 365, 1100, 560, bend=20)
    box(2, 1110, 510, 300, 110, "no: build it", size=38, fill=True)
    ellipse(3, 1260, 760, 70, 70)
    num(3, 1260, 785, "?", 70)
    out.append(f)

    f = frame("Ideation is the bottleneck", hl="bottleneck", secs=65, notes=(
        "The SOP itself flags ideation as the bottleneck, and it says it is worse on paper than in my head.\n\n"
        "The triggers are a new week, a new YouTube video, an insight from a sales call, a trend, a competitor "
        "move, or a pattern from Monday tracking."))
    trig = ["new week", "new video", "sales call", "a trend", "competitor move", "Monday pattern"]
    for i, t in enumerate(trig):
        r, c = divmod(i, 3)
        box(0 if i < 3 else 1, 140 + c * 360, 260 + r * 170, 300, 120, t, size=36)
    arrow(2, 640, 600, 640, 690, w=5)
    box(2, 400, 700, 480, 120, "one topic", fill=True, size=44, bold=True)
    out.append(f)

    f = frame("Output: one topic, one line", hl="one line", secs=50, notes=(
        "Ideation outputs exactly two things: one topic and a one-line angle. Cadence is deliberately not "
        "fixed. A magnet ships when ideation surfaces one."))
    box(0, 270, 330, 460, 160, "topic", fill=True, size=56, bold=True)
    box(1, 870, 330, 460, 160, "angle", size=56, bold=True)
    underline(1, 900, 1300, 540)
    out.append(f)

    # ---------------- SECTION 2 ----------------
    out.append(section_card(2, "The build", 20, (
        "Part two, the build. Four phases, and one real run walked through at the end.")) or lib.F)

    f = frame("The workflow, phase by phase", hl="phase by phase", secs=60, notes=(
        "Four phases. Ideation and format. Then production, where Claude does its pass. Then packaging and "
        "distribution. Then Monday, where last week's winners get reviewed and the next ones get iterated."))
    flow(0, 90, 380, ["ideation", "production", "packaging", "Monday"], w=290, h=150, gap=80, fill_idx=(1,), size=44)
    out.append(f)

    f = frame("Pick the format from the topic", hl="from the topic", secs=55, notes=(
        "The format pick. A Notion doc with subpages, the five-pager, is the most common. Then a Gamma deck, "
        "an existing YouTube video used as the magnet, or Canva slides. The topic picks the format."))
    for i, t in enumerate(["Notion doc", "Gamma deck", "YouTube video", "Canva slides"]):
        box(i, 120 + i * 350, 360, 300, 160, t, fill=(i == 0), size=40)
    text(1, 270, 600, "most common", 40, anchor="middle", font="c", bold=True)
    arrow(1, 270, 560, 270, 530, w=3.6)
    out.append(f)

    f = frame("The context block", hl="context", secs=65, notes=(
        "Production. The context goes to Claude: topic, angle and format, plus the topic-specific inputs. "
        "The source transcript, the SOP, examples, brand context, the audience and the proof points.\n\n"
        "The SOP flags one fix here: the skill should ask for these inputs instead of waiting to be fed them."))
    ins = ["topic", "angle", "format", "transcript", "SOP", "examples", "brand", "audience", "proof"]
    for i, t in enumerate(ins):
        r, c = divmod(i, 3)
        box(0 if i < 3 else 1, 120 + c * 260, 240 + r * 180, 220, 110, t, size=36, fill=(i < 3))
    arrow(2, 920, 470, 1080, 470, w=6)
    box(2, 1100, 380, 340, 180, "Claude", fill=True, size=58, bold=True)
    out.append(f)

    f = frame("Pick the subtype from the topic", hl="subtype", secs=60, notes=(
        "The magnet itself has a subtype: prompt swipe file, framework, case study, YouTube video and "
        "industry-specific. The subtype comes from what the topic actually is.\n\n"
        "The before and after for this part. Before: a framework forced into a swipe file reads as padding. A case study forced into a framework loses "
        "the one thing that made it credible, the specific account it happened in. After: the topic picks the subtype."))
    for i, t in enumerate(["swipe file", "framework", "case study", "YouTube video", "industry"]):
        box(0, 90 + i * 290, 300, 250, 130, t, size=36)
    arrow(1, 470, 450, 220, 560, bend=-20)
    text(1, 220, 620, "padding", 46, anchor="middle", font="c", bold=True)
    arrow(2, 760, 450, 470, 700, bend=30)
    text(2, 470, 760, "loses the proof", 46, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Packaging: cover, post, DM", hl="cover, post, DM", secs=55, notes=(
        "Packaging. A cover image. The X post copy and its DM message. The LinkedIn post copy and its "
        "LeadShark DM message. And optionally, follow-up images posted after it, each "
        "with a one-liner."))
    for i, (t, fl) in enumerate([("cover", True), ("X post, DM", False), ("LinkedIn + LeadShark", False), ("follow-ups", False)]):
        box(i, 110 + i * 360, 360, 310, 170, t, fill=fl, size=36)
    text(3, 1265, 590, "optional", 38, anchor="middle", font="k", color=GREY)
    out.append(f)

    f = frame("Worked example: one real run", hl="one real run", secs=75, notes=(
        "Here is the run I timed on 1 October. I found a proven LinkedIn post, captured it, Claude drafted "
        "the package, I read the draft, and the staging page went live. 24 minutes end to end.\n\n"
        "My part was finding the post, capturing it and reading the draft. Everything between those was the "
        "system."))
    steps = ["find post", "capture", "Claude drafts", "read draft", "page live"]
    for i, t in enumerate(steps):
        box(i, 70 + i * 300, 360, 250, 140, t, fill=(i in (0, 1, 3)), size=36)
        if i:
            arrow(i, 70 + i * 300 - 46, 430, 70 + i * 300 - 8, 430, w=3.6)
    text(5, 330, 600, "my part", 44, anchor="middle", font="c", bold=True)
    num(5, 1100, 640, "24 min", 70)
    out.append(f)

    f = frame("Start from a proven post", hl="proven post", secs=55, notes=(
        "Where the post comes from matters. The proven LinkedIn posts this process starts from mostly carry "
        "300 or more comments. The reference is already proven before Claude touches it."))
    box(0, 420, 260, 760, 420)
    for i in range(5):
        line(0, 470, 330 + i * 50, 470 + 520 - (i % 2) * 120, 330 + i * 50, w=3, color=GREY)
    hlrect(1, 470, 590, 380, 60)
    num(1, 660, 635, "300+ comments", 44)
    out.append(f)

    f = frame("Then the handoff", hl="handoff", secs=45, notes=(
        "Distribution goes to the VA, who schedules it. In the SOP the VA is an owner, so that step is not "
        "optional."))
    box(0, 250, 380, 380, 160, "the package", fill=True, size=42)
    arrow(1, 660, 460, 940, 460, bend=-40, w=6)
    box(1, 970, 380, 380, 160, "VA schedules", size=42)
    out.append(f)

    # ---------------- SECTION 3 ----------------
    out.append(section_card(3, "The keyword", 20, (
        "Part three, the keyword, and why it is the only instrument on the dashboard.")) or lib.F)

    f = frame("UTM empty on 673 of 678", hl="673 of 678", secs=65, notes=(
        "Here is the booking data. 678 Calendly rows. 649 of them sit under one owner, and the UTM field is "
        "empty on 673 of them.\n\n"
        "So you cannot attribute a booking to a post from the calendar. The data is not there."))
    hbars(0, 120, 300, [("all rows", 678, "678", False), ("one owner", 649, "649", False), ("UTM empty", 673, "673", True)],
          maxv=678, maxw=900, step_each=True)
    out.append(f)

    f = frame("One keyword per asset", hl="One keyword", secs=65, notes=(
        "That is why the keyword matters. A unique DM word per asset is the only path from a piece of content "
        "to a booked call that could be attributed.\n\n"
        "To be straight with you: nothing in my setup joins a keyword to a booking yet. This is the design. "
        "The join is the piece that is still missing, so this part has no real worked example yet."))
    for i, (a, k) in enumerate([("asset A", "word A"), ("asset B", "word B")]):
        y = 280 + i * 260
        box(0, 140, y, 260, 120, a, size=40)
        arrow(0, 410, y + 60, 520, y + 60)
        box(0, 530, y, 260, 120, k, fill=True, size=40)
        arrow(1, 800, y + 60, 920, y + 60, color=GREY)
        box(1, 930, y, 260, 120, "booking", size=40)
    text(2, 1060, 800, "join not built", 48, anchor="middle", font="c", bold=True)
    needs(3, 200, 860, "one real keyword with its calls", size=24)
    out.append(f)

    f = frame("What runs today: same-day read", hl="same-day", secs=60, notes=(
        "What runs instead is a same-day read. A booking on day D gets credited to the posts from day D and "
        "the day before.\n\n"
        "The script that does it calls this correlation. It never calls it attribution, and I say it the same way."))
    line(0, 160, 560, 1440, 560, w=5)
    for i, (x, lab) in enumerate([(500, "day D-1"), (1000, "day D")]):
        line(0, x, 540, x, 580, w=5)
        text(0, x, 640, lab, 46, anchor="middle", font="c", bold=True)
        box(1, x - 90, 390, 180, 100, "post", size=36)
    box(2, 1100, 260, 220, 100, "booking", fill=True, size=36)
    arrow(2, 1100, 320, 600, 390, bend=40, color=GREY)
    arrow(2, 1150, 365, 1000, 390, color=GREY)
    text(3, 800, 780, "correlation", 54, anchor="middle", font="c", bold=True)
    out.append(f)

    f = frame("Asset first, keyword second", hl="Asset first", secs=60, notes=(
        "The rule that stops this from embarrassing you. A keyword is a promise. Never publish a post that "
        "carries a keyword, or a comment-to-DM call to action, unless the resource and the thing that "
        "delivers it are already built.\n\n"
        "Before: the post goes out and the asset is still a plan. After: the asset exists, then the post."))
    text(0, 400, 250, "before", 48, anchor="middle", font="c", bold=True)
    box(0, 220, 300, 360, 120, "keyword post", size=40)
    arrow(0, 400, 430, 400, 520)
    box(0, 220, 530, 360, 120, "asset?", size=40)
    cross(1, 650, 590, 40)
    line(2, 800, 230, 800, 860, w=3, color=GREY)
    text(2, 1200, 250, "after", 48, anchor="middle", font="c", bold=True)
    box(2, 1020, 300, 360, 120, "asset built", fill=True, size=40)
    arrow(2, 1200, 430, 1200, 520)
    box(2, 1020, 530, 360, 120, "keyword post", size=40)
    tick(2, 1440, 590)
    out.append(f)

    f = frame("Monday: review, iterate, exploit", hl="Monday", secs=60, notes=(
        "Monday closes the loop. I review last week's winners, iterate on them, and exploit what worked. "
        "Then the next magnet starts from what the review found."))
    pos = [(800, 330), (1180, 660), (420, 660)]
    for i, (t, (x, y)) in enumerate(zip(["review", "iterate", "exploit"], pos)):
        box(i, x - 140, y - 60, 280, 120, t, fill=(i == 0), size=44)
    arrow(3, 950, 340, 1150, 580, bend=-40)
    arrow(3, 1030, 690, 570, 690, bend=-40)
    arrow(3, 400, 580, 640, 330, bend=-40)
    out.append(f)

    out.append(cta(40, (
        "If you run an established agency and want this workflow installed, with the measurement built in, "
        "the offer is called Agency Booked Calls. The link is in the description.")) or lib.F)
    return out
