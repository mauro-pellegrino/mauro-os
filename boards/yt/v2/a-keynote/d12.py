"""Doc 12: the agents for booked calls. Keynote format.
Doc written 2026-09-07 as a Q3 plan. Q3 closed 30 Sep, so nothing here frames it as Q3 going forward.
Numbers on frames come from brand/claims.md; the doc's 4 of 541, 92%, 30k emails and 5/4/1 replies
are not in claims.md and render as red [NEEDS] tags."""
from engine import B, needs, hd, vis, agenda, flow, squares, vbars, hbars, INK, ACC, SOFT, RED, MUTED

SLUG = "12-agents-for-booked-calls"
DOC = "12"
SOURCES = "research/video-knowledge/12-q3-agents-for-booked-calls.md, brand/claims.md (published-article block)"

AG = ["The scars", "The rule", "The seven"]

CANDS = [("A", "re-engagement", "no"), ("B", "attribution", "partly"), ("C", "cadence", "yes"), ("D", "dormant account", "yes"),
         ("E", "inbound triage", "yes"), ("F", "outbound reply", "yes"), ("G", "convert-lane loop", "yes")]


def distance_axis():
    # candidates placed by rank on a line from "a past relationship" to "a booked call"
    order = ["A", "B", "C", "D", "E", "F", "G"]
    out = ['<svg width="1380" height="470" viewBox="0 0 1380 470">',
           f'<line x1="40" y1="300" x2="1300" y2="300" stroke="{INK}" stroke-width="6"/>',
           f'<polygon points="1300,284 1340,300 1300,316" fill="{INK}"/>',
           f'<text x="1340" y="450" text-anchor="end" font-size="26" font-weight="800" fill="{INK}" class="m">BOOKED CALL</text>',
           f'<text x="40" y="450" font-size="26" font-weight="800" fill="{MUTED}" class="m">FURTHER AWAY</text>']
    xs = [1150, 990, 830, 670, 510, 350, 190]
    for k, (L, x) in enumerate(zip(order, xs)):
        name = dict((c[0], c[1]) for c in CANDS)[L]
        fill = ACC if L in "BC" else ("#fff")
        out.append(f'<g data-s="{k+1}"><circle cx="{x}" cy="300" r="52" fill="{fill}" stroke="{INK}" stroke-width="5"/>'
                   f'<text x="{x}" y="318" text-anchor="middle" font-size="50" font-weight="900" fill="{INK}">{L}</text>'
                   f'<text x="{x}" y="{205 if k%2==0 else 395}" text-anchor="middle" font-size="22" font-weight="800" fill="{INK}" class="m">{name}</text></g>')
    out.append("</svg>")
    return "".join(out)


def correction_loop(cut=False):
    pos = [(690, 60), (1110, 270), (690, 480), (270, 270)]
    labs = ["output", "you correct it", "fix goes in the skill", "run it again"]
    out = ['<svg width="1380" height="560" viewBox="0 0 1380 560">',
           f'<defs><marker id="a2" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>']
    arcs = [((860, 80), (1110, 220)), ((1110, 320), (860, 470)), ((520, 470), (270, 320)), ((270, 220), (520, 80))]
    for k, ((x, y), lab) in enumerate(zip(pos, labs)):
        (x1, y1), (x2, y2) = arcs[k]
        out.append(f'<g data-s="{k+1}"><rect x="{x-170}" y="{y-42}" width="340" height="84" fill="{ACC if k==2 else "#fff"}" stroke="{INK}" stroke-width="4"/>'
                   f'<text x="{x}" y="{y+11}" text-anchor="middle" font-size="29" font-weight="900" fill="{INK}">{lab}</text>'
                   f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{INK}" stroke-width="5" marker-end="url(#a2)"/></g>')
    if cut:
        out.append(f'<g data-s="5"><rect x="520" y="200" width="340" height="140" fill="{RED}"/>'
                   f'<text x="690" y="262" text-anchor="middle" font-size="30" font-weight="900" fill="#fff">agent too early</text>'
                   f'<text x="690" y="304" text-anchor="middle" font-size="24" font-weight="700" fill="#fff" class="m">the loop is cut</text></g>')
    out.append("</svg>")
    return "".join(out)


def slides():
    S = []

    def add(name, html, dur, notes, onscreen="", cls=""):
        S.append({"name": name, "html": html, "dur": dur, "notes": notes, "onscreen": onscreen, "cls": cls})

    # ---------------- HOOK
    add("hook, the result",
        '<div style="display:grid;grid-template-columns:560px 1fr;gap:60px;height:100%;align-items:center">'
        + '<div class="giant y">0</div>'
        + '<div>' + B('<div class="glabel cnt">calls caused by my four agents</div>', s=1)
        + B('<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:40px">'
            + "".join(f'<div class="nd dk mono" style="min-height:80px;font-size:22px;border-color:#E9B949">{a}</div>'
                      for a in ["performance-loop", "signal-sweep", "board-qa", "youtube-lead-magnet"]) + "</div>", s=2)
        + "</div></div>", 15,
        ["Open on the zero. I run four agents every day, and not one of them has ever caused a booked call.",
         "Build 1, the line. Build 2, the four names.",
         "They catch drops, catch missed asks, gate boards and package assets. All defensive."],
        onscreen="A giant honey zero on the dark ground, then the four agent names.", cls="dark")
    add("hook, the promise and the list",
        hd("Today:") + vis(agenda(AG, steps=True)), 15,
        ["The promise: seven agents that could cause a call, ranked by how close each one sits to a booked call, with the bottleneck named for each.",
         "I publish the plan before the build, while it can still be wrong.",
         "Build the cards: one, the four scars I already have. Two, the install rule. Three, the seven candidates and the honest count of what can go in first."],
        onscreen="Three cards build in: The scars, The rule, The seven.")

    # ---------------- SECTION 1: SCARS
    add("section 1 card", vis(agenda(AG, live=1)), 15,
        ["Part one. What is installed, and what each one prevents."], onscreen="Agenda with card 1 live.")
    add("four agents, four scars",
        hd("Four agents. <em>Four scars.</em>")
        + vis('<table class="tb">' + "".join(B(f"<td>{a}</td><td>{b}</td>", s=k + 1, tag="tr") for k, (a, b) in enumerate([
            ("performance-loop", "a reach drop nobody saw"), ("signal-sweep", "an ask lost in a thread"),
            ("board-qa", "a board that can't be read"), ("youtube-lead-magnet", "packaging drift")])) + "</table>", style="top:240px"), 75,
        ["Fast, one line each. Build the rows.",
         "performance-loop prevents a reach fall going unnoticed. signal-sweep prevents a request going missing in a chat thread.",
         "board-qa prevents a board shipping too full to record. youtube-lead-magnet prevents packaging drift by making the skill be read fresh every run.",
         "If you watched the system video, you know the stories. Here they are only the setup."],
        onscreen="Four-row table: agent, the miss it prevents.")
    add("worked example, the 64%",
        hd("64% gone. <em>Two months unseen.</em>", "sm")
        + vis('<div style="display:grid;grid-template-columns:1fr 520px;gap:50px;align-items:center;width:100%">'
              + vbars([("June", 100, INK, None, "100"), ("August", 36, RED, 1, "36")], w=760, h=500)
              + '<div style="display:flex;flex-direction:column;gap:22px">'
              + B('<div class="panel"><div class="lab">Before</div><div style="font-size:38px;font-weight:900;color:#C0392B">nobody looking</div></div>', s=2)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After</div><div style="font-size:38px;font-weight:900;color:#1B4332">flagged weekly</div></div>', s=3)
              + '<div class="cite">monthly impressions, June = 100</div></div></div>', style="top:220px"), 90,
        ["The worked example for part one. Monthly impressions fell 64% between June and August 2026, and it went unnoticed for two months.",
         "Build 1, the August bar. Build 2, the before. Build 3, the after: the agent now flags it every week.",
         "This is a good agent. It still never caused a call. It stops a loss. That is the point of part one."],
        onscreen="June 100, August 36 in red. Before and after panels.")
    add("none of them touches a human",
        hd("None of them <em>touches a human.</em>")
        + vis('<div style="width:100%">'
              + flow([("post", "", 1), ("DM", "", 2), ("conversation", "", 3), ("booked call", "y", 4)])
              + B('<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:60px">'
                  + "".join(f'<div class="nd dk mono" style="min-height:80px;font-size:20px">{a}</div>' for a in
                            ["performance-loop", "signal-sweep", "board-qa", "yt-lead-magnet"]) + "</div>"
                  , s=5)
              + "</div>", style="top:250px"), 75,
        ["Draw the path a call actually takes. Build it: a post, a DM, a conversation, a booked call.",
         "Build 5: all four agents sit behind the post. They protect the inputs. Nothing on the path from the DM to the call is touched by an agent.",
         "That is the gap the rest of this video is about."],
        onscreen="A four-step path to a booked call, then the four agents parked behind it.")

    # ---------------- SECTION 2: THE RULE
    add("section 2 card", vis(agenda(AG, live=2)), 15,
        ["Part two, the install rule that governs the whole list."], onscreen="Agenda with card 2 live.")
    add("the correction loop",
        hd("The skill gets good <em>first.</em>")
        + vis(correction_loop(cut=True), style="top:220px"), 90,
        ["An agent goes in only where the skill underneath it is already good.",
         "Build the loop: output, you correct it, the fix goes into the skill, you run it again. That loop is what makes a skill good.",
         "Build 5: put an agent in too early and it runs on its own, so the loop is cut. It freezes a bad skill in place and repeats it every day."],
        onscreen="A four-step correction loop, then a red block in the middle: agent too early.")
    add("writing stays manual",
        hd("Writing stays <em>a skill.</em>")
        + vis('<div class="split">'
              + B('<div class="panel"><div class="lab">Writing</div>' + flow([("draft", "", None), ("my edit", "y", None), ("skill file", "dk", None)])
                  + "</div>", s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">Agents</div>'
                  + flow([("known good", "dk", None), ("schedule", "", None), ("runs alone", "y", None)])
                  + "</div>", s=2)
              + "</div>", style="top:260px"), 75,
        ["The worked example of the rule: writing is deliberately kept manual.",
         "Build 1: I correct the writing skills constantly. A correction is a file edit I can see.",
         "Build 2: agents go on jobs where I already know what good looks like. Writing is not one of those jobs yet."],
        onscreen="Two panels: writing with my edit in the loop, and agents on known-good jobs.")
    add("is there a skill behind it",
        hd("Is there a skill <em>behind it?</em>", "sm")
        + vis('<table class="tb">' + "".join(
            B(f'<td>{L} &middot; {n}</td><td><span class="tag {"y" if v=="yes" else ("r" if v=="no" else "")}" style="font-size:20px">{v}</span></td>',
              s=k + 1, tag="tr") for k, (L, n, v) in enumerate(CANDS)) + "</table>", style="top:200px"), 75,
        ["Every candidate carries one honest line: is there a skill behind it today.",
         "Build the seven rows. Re-engagement: no. Attribution: partly. Cadence, dormant account, inbound triage, outbound reply and the convert-lane loop: yes.",
         "The ones without a skill are not first in line, however much they are wanted."],
        onscreen="Seven rows, each with a yes, partly or no chip.")

    # ---------------- SECTION 3: THE SEVEN
    add("section 3 card", vis(agenda(AG, live=3)), 15,
        ["Part three, the seven, ranked by distance to a booked call."], onscreen="Agenda with card 3 live.")
    add("ranked by distance",
        hd("Ranked by distance <em>to a call.</em>") + vis(distance_axis(), style="top:250px"), 60,
        ["Build each candidate onto the line as you name it. A sits closest to a call, G furthest away.",
         "B and C are in honey. Hold that, it is the honest count at the end."],
        onscreen="A line from further away to booked call. Seven lettered circles build on.")
    add("A, re-engagement",
        hd("The warmest pool <em>you already have.</em>", "sm")
        + vis('<div style="width:100%">'
              + flow([("past qualified bookers", "dk", 1), ("did not close", "", 2), ("agent re-opens", "y", 3)])
              + B(f'<div style="margin-top:44px;display:flex;gap:20px;align-items:center;flex-wrap:wrap"><span class="chip r">skill: no</span>'
                  f'{needs("sign-off to quote the outside consultant on camera")}</div>', s=4)
              + "</div>", style="top:270px"), 75,
        ["A, the re-engagement agent. It works every past qualified booker who did not close. That is the shortest distance from an existing human relationship to a call.",
         "An outside consultant called this the number one item on a call in August. The doc has the verbatim line. Quote it only after you sign it off, and never name him.",
         "It is flagged in the Monday analysis as a whole missing motion and was never a backlog row.",
         "Skill behind it today: no. It waits on your sequencing decision, because putting it first inverts the current order."],
        onscreen="Past qualified bookers, did not close, agent re-opens. Then a red no chip and a NEEDS tag.")
    add("B, attribution, the gap",
        '<div style="display:grid;grid-template-columns:780px 1fr;gap:40px;height:100%;align-items:center">'
        + '<div><div class="giant md" style="font-size:240px;color:#C0392B">673</div>'
        + B('<div class="glabel cnt" style="margin-top:24px">bookings with no source</div>', s=1) + "</div>"
        + '<div>' + hbars([("Calendly rows", 678, SOFT, None, "678"), ("UTM empty", 673, RED, 2, "673")], w=600, label_w=260, row_h=110)
        + B(f'<div style="margin-top:24px">{needs("doc 12 says UTM filled on 4 of 541 bookings; not in claims.md")}</div>', s=3)
        + "</div></div>", 75,
        ["B, the attribution agent. The UTM field is empty on 673 of 678 Calendly rows. That is the published number, and it is cleared.",
         "Build 3: the doc uses a different cut, 4 of 541 bookings with a source. That one is not in claims.md, so it is tagged and stays out of narration until signed off.",
         "With data like that, a unique DM keyword per asset is the only path from a piece of content to a call."],
        onscreen="Giant red 673, bars 678 against 673, then a NEEDS tag on the doc's 4 of 541 figure.")
    add("B, worked example, one keyword",
        hd("One keyword <em>per asset.</em>")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:30px">'
              + B('<div class="panel"><div class="lab">Before</div>' + flow([("post", "", None), ("same-day calls", "", None), ("a guess", "bad", None)], [("&rarr;", ""), ("&rarr;", "r")]) + "</div>", s=1)
              + B('<div class="panel" style="border-top:12px solid #E9B949"><div class="lab">After</div>'
                  + flow([("asset + keyword", "y", None), ("DM with keyword", "", None), ("booking", "", None), ("joined", "dk", None)]) + "</div>", s=2)
              + B('<span class="chip y" style="font-size:20px">skill: partly</span>', s=3)
              + "</div>", style="top:220px"), 90,
        ["The worked example for part three.",
         "Build 1, the before: today the read is same-day correlation. A post goes out, calls land the same day or the day after, and that is a correlation. Call it a correlation on camera.",
         "Build 2, the after: the agent assigns the keyword, watches for it in the DMs, and joins it to the booking.",
         "Build 3: partly built already. Keyword assignment lives in the sixth article skill, and post-to-call.py and trace-bookings.py exist. The join itself does not exist yet. This is the most installable item on the list."],
        onscreen="Before: post to same-day calls to a guess. After: asset plus keyword joined to the booking.")
    add("C, cadence",
        hd("Escalate on the <em>second quiet day.</em>", "sm")
        + vis('<div style="width:100%">'
              + '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px">'
              + "".join(B(f'<div class="panel" style="padding:18px"><div class="lab">week {w}</div>'
                          + squares(5, 5, (lambda k, w=w: "g" if w == 1 else "") ) + "</div>", s=w) for w in (1, 2, 3, 4))
              + "</div>"
              + B('<div style="margin-top:30px;display:flex;gap:18px;align-items:center"><span class="chip r">alert</span>'
                  '</div>', s=5)
              + "</div>", style="top:240px"), 75,
        ["C, the cadence agent. The failure mode in the backlog, in my own words: one good week and then three quiet ones. That is what happened after June.",
         "Build the four weeks. This is a pattern diagram. The squares show the rule only.",
         "Build 5: the agent watches posting cadence per account and escalates on the second quiet day, before a week is lost.",
         "Skill behind it: yes. The content loop and the performance loop already read the inputs it needs."],
        onscreen="Four week strips: week 1 full, weeks 2 to 4 empty. A red alert chip on day 2 of week 2.")
    add("D, dormant account",
        hd("One account <em>went quiet.</em>")
        + vis('<div style="display:flex;flex-direction:column;align-items:center;gap:36px">'
              + B(needs("doc 12 says one account is down 92% on posts; not in claims.md"), s=1)
              + B(flow([("dormant agent", "", None), ("folds into", "ghost", None), ("cadence agent", "y", None)]), s=2)
              + "</div>", style="top:260px"), 45,
        ["D, the dormant-account agent. It is a narrower version of C, aimed at restarting an account rather than keeping one going.",
         "The doc gives a percentage drop on posts for that account. It is not in claims.md, so it stays tagged. Never name the account.",
         "Build 2: it folds into C. Same inputs, one agent."],
        onscreen="A red NEEDS tag on the drop figure, then D folding into C.")
    add("E, inbound triage",
        hd("It drafts. <em>A human sends.</em>")
        + vis('<div style="width:100%">'
              + flow([("inbound DM", "", 1), ("score vs floor", "", 2), ("draft reply", "dk", 3), ("human sends", "y", 4)])
              + B('<div style="margin-top:40px"><span class="chip y" style="font-size:20px">skill: yes</span></div>', s=5)
              + "</div>", style="top:290px"), 60,
        ["E, the inbound triage agent. Build the four steps: it reads inbound, scores against the qualification floor, and drafts the reply.",
         "Build 4: a human sends it. The line between drafting and sending is the whole safety design.",
         "Skill behind it: yes. lead-triage.py already exists and the DM skills are written."],
        onscreen="Inbound DM, score, draft, then a honey human sends box.")
    add("F, outbound reply",
        hd("Closest to a stranger. <em>Drafts only.</em>", "sm")
        + vis('<div style="width:100%">'
              + flow([("lead alert", "", 1), ("pull context", "", 2), ("draft reply", "dk", 3), ("human sends", "y", 4)])
              + B(f'<div style="margin-top:40px;display:flex;flex-direction:column;gap:12px;align-items:flex-start">'
                  f'{needs("outbound volume per month and first-test reply counts; not in claims.md")}</div>', s=5)
              + "</div>", style="top:270px"), 60,
        ["F, the outbound reply agent. It watches the lead alerts from the cold-email motion, pulls context, and drafts the reply into the right channel.",
         "It is the closest of all seven to speaking to a stranger, so it drafts only.",
         "The doc gives the monthly send volume and the reply count from the first test. Neither is in claims.md, and the operator who runs it is never named. Leave the numbers out of narration."],
        onscreen="Lead alert, context, draft, human sends. A NEEDS tag on the outbound numbers.")
    add("G, convert-lane loop",
        hd("Waits on <em>the keyword data.</em>", "sm")
        + vis(flow([("B ships", "y", 1), ("keyword data builds up", "", 2), ("G reads bookings", "dk", 3), ("convert rules updated", "", 4)]), style="top:300px"), 45,
        ["G, the convert-lane loop. It applies the seventh article skill's pattern to bookings: regenerate the evidence, downgrade rules that lose, keep convert rules apart from reach rules.",
         "Build it: it cannot read anything until B is running and keyword data exists. So G waits on B."],
        onscreen="B ships, data builds, G reads bookings, rules updated.")
    add("the order",
        hd("The order <em>that falls out.</em>", "sm")
        + vis('<div style="width:100%;display:flex;flex-direction:column;gap:22px">'
              + flow([("B &middot; attribution", "y", 1), ("C &middot; cadence", "y", 2), ("E + F &middot; draft-only", "dk", 3)])
              + B('<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:20px">'
                  '<div class="nd ghost">A &middot; your call</div><div class="nd ghost">D &middot; inside C</div><div class="nd ghost">G &middot; after B</div></div>', s=4)
              + "</div>", style="top:280px"), 60,
        ["Build the order. First B, attribution: highest install-readiness, and everything else becomes measurable once it runs.",
         "Then C, cadence: it prevents the failure that already cost a quarter. Then E and F, both draft-only, in whichever order the inbox is louder.",
         "Build 4: A waits on a sequencing decision that only I make. D folds into C. G waits on B."],
        onscreen="Three solid boxes in order, then three dashed boxes for the waiting ones.")
    add("the honest count",
        '<div style="display:grid;grid-template-columns:560px 1fr;gap:60px;height:100%;align-items:center">'
        + '<div class="giant y">2</div>'
        + '<div>' + B('<div class="glabel cnt">go in first: B and C</div>', s=1)
        + B(f'<div style="margin-top:36px">{needs("re-check on recording day which of B and C is installed")}</div>', s=2)
        + "</div></div>", 60,
        ["The honest count is two. B and C. The rest is a later list with a date attached.",
         "This list was written as a Q3 plan on 7 September, with three weeks left in the quarter. Q3 has closed. Say that on camera: it was a Q3 plan and here is where it stands.",
         "Build 2: re-check before recording. As of the brief date, no attribution or cadence agent is in the agents folder. If one has gone in, say so and show it."],
        onscreen="A giant honey 2. B and C go in first. A NEEDS tag to re-check the install status.", cls="dark")
    add("the safety rule",
        hd("None of these <em>send.</em>", "c")
        + vis(squares(7, 7, lambda k: "y", size=980, s_map=lambda k: k + 1)
              + "", style="top:300px;flex-direction:column"), 45,
        ["Every candidate drafts, scores, flags or escalates, and a human sends.",
         "Build the seven squares, one per candidate, all the same colour: all seven are draft-only.",
         "An agent that fails quietly is the main new risk of running agents at all. A quiet failure that already spoke to a prospect cannot be taken back."],
        onscreen="Seven honey squares in a row under the line None of these send.")
    add("CTA",
        '<div class="cta"><div class="big">Link in the description</div><div class="offer">Agency Booked Calls</div></div>', 45,
        ["If you run an established agency and want the agents that touch a human installed for you, the link is in the description. It is called Agency Booked Calls.",
         "And tell me which of the seven I have ranked wrong. I mean that, the order can still change.",
         "No price on screen and no URL."],
        onscreen="Dark frame: Link in the description, and the offer name in honey.", cls="dark")
    return S


TITLES = [
    {"title": "Building AI Agents That Actually Book Calls",
     "modelled_on": "01-outliers.csv, Greg Isenberg, 'Building AI Agents that actually work (Full Course)', 566k: the anti-hype 'that actually' qualifier"},
    {"title": "I Ranked 7 AI Agents by How Close They Get to a Call",
     "modelled_on": "charlie-morgan-dig.md #9, 'I Ranked Every Online Business Model So You Don't Have To', 24k: the save-you-effort ranking"},
    {"title": "The 7 AI Agents I'm Installing for More Booked Calls",
     "modelled_on": "01-outliers.csv, Nate Herk, 'How I Sold These 4 AI Agents for $23000 (as a beginner)', 457k: a counted set of agents tied to a result"},
]

NEEDS = ["doc's 'UTM filled on 4 of 541 bookings' (673 of 678 used instead, from claims.md)",
         "doc's 'one account down 92% on posts'",
         "outbound volume (30k emails a month) and first-test replies (5, 4 to one angle, 1 to the other)",
         "sign-off to quote the outside consultant's line on camera",
         "re-check on recording day which of B and C is installed",
         "Mauro's decision on whether the re-engagement motion (A) jumps the queue"]

THUMBS = [
    """<div class="thumb" style="background:#0E2418">
      <div style="position:absolute;left:60px;top:20px;font-size:560px;font-weight:900;color:#E9B949;line-height:1;letter-spacing:-30px">0</div>
      <div style="position:absolute;left:450px;top:150px;display:grid;grid-template-columns:1fr 1fr;gap:16px;width:360px">
        <i style="height:130px;background:#1B4332;border:5px solid #E9B949"></i><i style="height:130px;background:#1B4332;border:5px solid #E9B949"></i>
        <i style="height:130px;background:#1B4332;border:5px solid #E9B949"></i><i style="height:130px;background:#1B4332;border:5px solid #E9B949"></i></div>
      <div style="position:absolute;left:70px;bottom:60px;font-size:104px;font-weight:900;color:#fff;letter-spacing:-4px">CALLS CAUSED</div>
      <div class="face">FACE</div></div>""",
    """<div class="thumb" style="background:#F7F3EA">
      <div style="position:absolute;left:50px;top:60px;display:flex;flex-direction:column;gap:12px;width:440px">
        """ + "".join(f'<div style="display:flex;align-items:center;gap:16px;background:{"#E9B949" if k < 2 else "#fff"};border:5px solid #1B4332;height:68px;padding:0 20px;font-size:44px;font-weight:900;color:#1B4332">'
                      f'<span style="font-family:JetBrains Mono,monospace">{L}</span><span style="flex:1;height:14px;background:#1B4332;opacity:{1-k*0.12}"></span></div>' for k, L in enumerate("BCEFADG")) + """
      </div>
      <div style="position:absolute;left:540px;top:380px;font-size:118px;font-weight:900;color:#1B4332;letter-spacing:-6px;line-height:.9">7 AGENTS<br><span style="background:#E9B949;padding:0 14px">RANKED</span></div>
      <div class="face" style="border-color:#1B4332;color:#1B4332;width:300px;height:340px;top:0;bottom:auto;border-radius:0 0 20px 20px">FACE</div></div>""",
    """<div class="thumb" style="background:#1B4332">
      <div style="position:absolute;left:70px;top:80px;width:680px;background:#fff;border:6px solid #E9B949;padding:30px 34px">
        
        <div style="margin-top:20px;height:22px;background:#B9C7BE;width:90%"></div><div style="margin-top:14px;height:22px;background:#B9C7BE;width:75%"></div>
        <div style="margin-top:14px;height:22px;background:#B9C7BE;width:82%"></div>
        <div style="margin-top:30px;display:inline-block;background:#C0392B;color:#fff;font-size:44px;font-weight:900;padding:10px 26px;text-decoration:line-through">SEND</div></div>
      <div style="position:absolute;left:70px;bottom:60px;font-size:112px;font-weight:900;color:#E9B949;letter-spacing:-4px">NEVER SENDS</div>
      <div class="face">FACE</div></div>""",
]
