"""Doc 09: one transcript becomes a full X article. Source: research/video-knowledge/09-transcript-to-article.md.
On-screen numbers from brand/claims.md: 41 captures / 24 accounts, the word-band medians (73,300 and 225,900),
0.48x and 0.30x (another account, n=12, labelled), 673 of 678 UTM empty. Not in claims.md and rendered as
[NEEDS]: the 2.27x top lift, the 738 to 1,012 converter word range, the cleared worked-example pair.
Doc 09's "4 of 541" is replaced by the published 673 of 678 Calendly rows."""
from engine import (needs, lbl, c, window, tree, flow, split, bars, hbar, tiles, cycle, skel)

FACE = '<div class="face">MAURO CUTOUT HERE</div>'


def wave(n=60, hot=(), w=1300, h=120):
    import math
    bars_ = []
    bw = w / n
    for i in range(n):
        v = 0.25 + 0.75 * abs(math.sin(i * 0.7) * math.cos(i * 0.23))
        col = "#E9B949" if any(a <= i < b for a, b in hot) else "#B9C7BE"
        bh = v * h
        bars_.append(f'<rect x="{i * bw + 2:.0f}" y="{(h - bh) / 2:.0f}" width="{bw - 5:.0f}" height="{bh:.0f}" rx="4" fill="{col}"/>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(bars_)}</svg>'


def vwave(n=22, h=440, w=120):
    import math
    bh = h / n
    out = []
    for i in range(n):
        v = 0.25 + 0.75 * abs(math.sin(i * 0.7) * math.cos(i * 0.23))
        col = "#E9B949" if i in (4, 5, 10, 11, 16, 17) else "#B9C7BE"
        out.append(f'<rect x="{(w - v * w) / 2:.0f}" y="{i * bh + 2:.0f}" width="{v * w:.0f}" height="{bh - 6:.0f}" rx="4" fill="{col}"/>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(out)}</svg>'


def first_screen(dup):
    """Mock X article first screen. dup=True: cover and title say the same thing (red)."""
    a = "red" if dup else "sage"
    b = "red" if dup else "hot"
    cover = (f'<div style="height:180px;border-radius:12px;background:{"#F6D5D0" if dup else "#1B4332"};display:flex;align-items:center;justify-content:center;gap:16px;padding:20px">'
             + (skel([70], "red") if dup else '<svg width="300" height="120"><rect x="10" y="40" width="70" height="40" fill="#E9B949"/><rect x="115" y="40" width="70" height="40" fill="#52B788"/><rect x="220" y="40" width="70" height="40" fill="#F7F3EA"/><path d="M80 60h35M185 60h35" stroke="#F7F3EA" stroke-width="5"/></svg>')
             + '</div>')
    return (f'<div style="width:520px;background:#fff;border:4px solid #1B4332;border-radius:16px;padding:18px">{cover}'
            f'<div class="sk {a}" style="width:85%;height:34px;margin-top:20px"></div>'
            f'<div class="sk {b}" style="width:95%"></div><div class="sk" style="width:80%"></div><div class="sk" style="width:88%"></div></div>')


THUMBS = [
    # T1: call in, article out
    '<div style="position:absolute;left:64px;top:60px;width:760px">'
    '<div class="huge" style="margin-top:16px;font-size:136px">Call in.<br><em>Article out.</em></div></div>'
    '<div style="position:absolute;left:64px;bottom:70px;display:flex;align-items:center;gap:26px">'
    + wave(22, hot=((6, 12),), w=360, h=140).replace("#B9C7BE", "#3C6B52")
    + '<div style="font:900 80px Inter;color:#E9B949">&rarr;</div>'
    '<div style="width:230px;height:200px;background:#F7F3EA;border-radius:12px;padding:16px;border:5px solid #E9B949">'
    '<div style="height:70px;background:#1B4332;border-radius:8px"></div>'
    '<div style="height:16px;background:#1B4332;margin-top:14px;width:90%;border-radius:4px"></div>'
    '<div style="height:12px;background:#B9C7BE;margin-top:10px;width:80%;border-radius:4px"></div>'
    '<div style="height:12px;background:#B9C7BE;margin-top:8px;width:70%;border-radius:4px"></div></div></div>' + FACE,
    # T2: the chain
    '<div style="position:absolute;left:64px;top:60px">'
    '<div class="huge" style="margin-top:16px;font-size:140px">Stop writing<br><em>articles</em></div></div>'
    '<div style="position:absolute;left:64px;bottom:80px;display:flex;gap:16px;align-items:center">'
    + "".join(f'<div class="tile7 {"on" if i == 7 else ""}">{i}</div>' for i in range(1, 8)) + '</div>',
    # T3: the NEEDS tag
    '<div style="position:absolute;left:64px;top:60px">'
    '<div class="huge" style="margin-top:16px;font-size:132px">No fake<br><em>numbers</em></div></div>'
    '<div style="position:absolute;left:70px;bottom:90px"><span class="needs">[NEEDS: x]</span></div>' + FACE,
]

VIDEO = {
    "doc": "09",
    "slug": "transcript-to-article",
    "title_text": "One call becomes a full X article",
    "title_html": "One call becomes<br>a full <em>X article</em>",
    "title_size": 430,
    "titles": [
        {"title": "Watch me turn one call into a full X article",
         "modelled_on": "01-outliers.csv: Nick Saraev, \"Watch me start & sell an AI service in 10 hours\", 366K"},
        {"title": "Build X articles from your calls: here's how",
         "modelled_on": "01-outliers.csv: David Ondrej, \"Build Everything with AI Agents: Here's How\", 1.7M"},
        {"title": "I let Claude turn my calls into X articles",
         "modelled_on": "01-outliers.csv: Jordan Platten, \"I Let Claude AI Get Me Clients for 30 Days (240 Meetings Booked)\", 39K"},
    ],
    "thumbs": THUMBS,
    "needs": ["a cleared transcript and finished article pair for the worked example (doc 09 gap)",
              "the top converter lift, 2.27x in doc 09, not in claims.md",
              "the converter word range, 738 to 1,012 in doc 09, not in claims.md"],
    "overview": {"sec": 10, "on": "The whole map, zoomed out: the input, the chain, the proof. The title top right.",
                 "say": ["This is the system that turns one call recording into a full X article, on one map.",
                         "Input on the left, the chain in the middle, the proof on the right."]},
    "result": {"id": "result", "num": "", "tag": "the result", "sec": 10, "vcls": "col", "head": "",
               "on": "The number 41, with: real captures behind every rule. Source label: the corpus, 24 accounts.",
               "body": '<div class="bign">41</div>' + c("real captures behind every rule", cls="bigl") + lbl("the x-articles corpus &middot; 24 accounts"),
               "say": ["The result first. Every rule in this article system traces back to one corpus of 41 real captures from 24 accounts.",
                       "Nothing in it is a guess about what works. When a rule has no evidence, it says so.",
                       "By the end you will see the whole chain, from a recording you already have to a published article."]},
    "roadmap": {"id": "roadmap", "num": "", "tag": "today we go over", "sec": 10, "head": "",
                "on": "Three cards: 01 The input, 02 The chain, 03 The proof.",
                "body": '<div class="rm">'
                        '<div class="rmc"><div class="k">01</div><div class="t c">The input</div><div class="ico">' + wave(14, hot=((4, 8),), w=330, h=110) + '</div></div>'
                        '<div class="rmc"><div class="k">02</div><div class="t c">The chain</div><div class="ico" style="gap:8px">'
                        + "".join(f'<span class="chip {"on" if i == 2 else ""}" style="padding:10px 14px">{i}</span>' for i in range(1, 5)) + '</div></div>'
                        '<div class="rmc"><div class="k">03</div><div class="t c">The proof</div><div class="ico">' + needs("x") + '</div></div></div>',
                "say": ["Today we go over three things.",
                        "First, the input: what you feed it, and why the hard part is choosing.",
                        "Second, the chain: the skills, the order they run in, and why the order matters.",
                        "Third, the proof: how an article gets measured, and what happens when the evidence has a gap."]},
    "regions": [
        {"num": "01", "label": "The input", "sec": 25,
         "on": "Region 01 framed: the inputs, the transcript strip, the two lanes.",
         "say": ["Section one. The input.", "You already have it. It is sitting in your recordings."],
         "zones": [
             {"id": "inputs", "num": "01", "tag": "the input", "sec": 68,
              "on": "Seven input chips flowing into skill 1: call transcript, Miro board, client debrief, YouTube script, Slack thread, account export, raw notes.",
              "head": "The input is already recorded.",
              "body": '<div style="display:flex;flex-wrap:wrap;gap:18px;max-width:820px">'
                      + "".join(f'<span class="chip {"on" if k == 0 else ""}">{t}</span>' for k, t in enumerate(
                          ["call transcript", "Miro board", "client debrief", "YouTube script", "Slack thread", "account export", "raw notes"]))
                      + '</div><div class="arr" style="font-size:80px">&rarr;</div>' + flow([("skill 1", "extracts the subject", "dark")]).replace('class="flow "', 'class="flow" style="width:300px"'),
              "say": ["What can go in. A call transcript, a Miro board, a client debrief, a YouTube script, a Slack thread, an export, a pile of raw notes.",
                      "The skills do not assume any of it is organised. Skill one does the extraction."]},
             {"id": "select", "num": "01", "tag": "worked example", "sec": 83,
              "on": "A transcript drawn as a waveform with four highlighted stretches, one of them picked. A red tag for the real cleared example.",
              "head": "The job is selection.",
              "body": '<div style="display:flex;flex-direction:column;gap:30px;align-items:center;width:100%">'
                      + wave(60, hot=((5, 10), (19, 24), (33, 37), (47, 53))) +
                      '<div style="display:flex;gap:120px">' + "".join(f'<span class="chip {"on" if k == "B" else ""}">subject {k}</span>' for k in "ABCD") + '</div>'
                      + flow([("subjects presented", "", ""), ("one picked", "", "on")], cls="sm").replace('class="flow sm"', 'class="flow sm" style="width:640px"')
                      + needs("a cleared transcript + finished article, side by side") + '</div>',
              "say": ["This is the part people underestimate. They think they need to write something. They need to select something.",
                      "Skill one reads the whole recording and comes back with a few candidate subjects. I pick one.",
                      "[NEEDS: a real transcript and its finished article, cleared for public use, to replace this diagram with the real pair.]"]},
             {"id": "intent", "num": "01", "tag": "declare first", "sec": 73,
              "on": "Two lanes side by side: reach, judged on impressions; convert, judged on booked calls. Dated 2026-09-01.",
              "head": "Declare reach or convert first.",
              "body": tiles([("REACH", "judged on impressions", "on"), ("CONVERT", "judged on booked calls", "dark")], cols=2)
                      .replace('min-height:150px', 'min-height:150px'),
              "src": "set 2026-09-01",
              "say": ["Before anything gets written, the article declares its intent. Reach or convert.",
                      "My own words on this, from the first of September: I would rather optimize some articles to go viral and others to convert than to just have singularity.",
                      "Reach rules and convert rules are both real, and they are different rules."]},
             {"id": "intent-ba", "num": "01", "tag": "before / after", "sec": 68,
              "on": "Before: one article judged on everything, both scores red. After: a reach article judged only on reach, a convert article judged only on calls, both green.",
              "head": "One article, one metric.",
              "body": split(
                  tiles([("reach", "low", "red"), ("calls", "none", "red")], cols=2) + lbl("judged on everything: always a failure"),
                  tiles([("reach article", "judged on reach", "sage"), ("convert article", "judged on calls", "sage")], cols=2) + lbl("judged on the metric it declared")),
              "say": ["Before: every article gets judged on everything, so every article looks like a failure at something.",
                      "After: a reach article that books nothing is fine. A convert article with low reach is fine. Each one is judged on the metric it declared."]},
         ]},
        {"num": "02", "label": "The chain", "sec": 25,
         "on": "Region 02 framed: the chain of seven, the first screen, the body, the keyword, the keeper.",
         "say": ["Section two. The chain.", "The skills, in the order they run."],
         "zones": [
             {"id": "chain", "num": "02", "tag": "the chain", "sec": 83,
              "on": "Seven numbered blocks in a chain: subject, first screen, title, cover, body, companion, keeper. Each with its done-when label.",
              "head": "The chain, in order.",
              "body": '<div style="width:100%">' + flow([
                  ("subject", "1", ""), ("first screen", "2", "on"), ("title", "3", ""), ("cover", "4", ""),
                  ("body", "5", ""), ("companion", "6", ""), ("keeper", "7", "dark")], cls="sm xa")
                      + '<div style="margin-top:36px;display:flex;justify-content:space-between">'
                      + lbl("skills/content/x-articles/") + lbl("six run in order. the seventh keeps them honest") + '</div></div>',
              "say": ["Here is the set. Six skills in a fixed order, plus a seventh.",
                      "One, the subject. Two, the first screen: cover, title and first three lines as one unit. Three, the title. Four, the cover. Five, the body. Six, the companion post and the measurement hook.",
                      "And seven, whose only job is keeping the other six honest as evidence lands."]},
             {"id": "order", "num": "02", "tag": "order matters", "sec": 68,
              "on": "Three stages: subject, then first screen with title and cover nested inside it, then body.",
              "head": "Subject. First screen. Then body.",
              "body": '<div class="flow">'
                      '<div class="node"><b>subject</b><small>skill 1</small></div><div class="arr">&rarr;</div>'
                      '<div class="node on" style="flex:2"><b>first screen</b><small>skill 2</small>'
                      '<div style="display:flex;gap:14px;margin-top:18px;justify-content:center"><span class="chip">title &middot; 3</span><span class="chip">cover &middot; 4</span></div></div>'
                      '<div class="arr">&rarr;</div><div class="node dark"><b>body</b><small>skill 5</small></div></div>',
              "say": ["Order matters. Subject before title. Title and cover together. Body last.",
                      "Skills three and four are components of skill two. You draft them inside the first-screen pass, then sharpen each one."]},
             {"id": "screen-ba", "num": "02", "tag": "before / after", "sec": 78,
              "on": "Before: a first screen where the cover text and the title say the same thing, both red. After: the cover is a diagram, the title is the claim, the first lines carry the proof.",
              "head": "Title and cover, drafted together.",
              "body": split(first_screen(True) + lbl("says the same thing twice"), first_screen(False) + lbl("three parts, three jobs")),
              "say": ["Before: write the title alone, pick the cover alone. You get a first screen that says the same thing twice.",
                      "After: draft them together. The cover shows something, the title claims something, the first lines back it up. Three parts, three jobs."]},
             {"id": "body", "num": "02", "tag": "skill 5", "sec": 68,
              "on": "The article body as text lines on the right, each with a pin line back to a point on the transcript waveform on the left.",
              "head": "Every claim points at the input.",
              "body": '<div style="display:flex;align-items:center;gap:30px">' +
                      vwave() + '<svg width="220" height="440"><path d="M0 110 C110 110 110 60 220 60M0 220 C110 220 110 210 220 210M0 330 C110 330 110 360 220 360" fill="none" stroke="#E9B949" stroke-width="6"/></svg>'
                      + window("article body", skel([95, 80]) + '<div class="sk hot" style="width:70%"></div>' + skel([90, 85]) + '<div class="sk hot" style="width:60%"></div>' + skel([92, 78]) + '<div class="sk hot" style="width:66%"></div>', style="width:620px")
                      + '</div>',
              "say": ["Skill five writes the body. The constraint is simple: every claim in the article traces back to the input document.",
                      "If it is not in the recording, it is not in the article."]},
             {"id": "keyword", "num": "02", "tag": "skill 6", "sec": 68,
              "on": "A companion post with a highlighted keyword chip, then a DM, then a booking.",
              "head": "The post carries a keyword.",
              "body": flow([("companion post", "written by skill 6", ""), ("unique DM keyword", "assigned per article", "on"),
                            ("DM", "the reader asks", ""), ("booking", "attributable, in principle", "dark")]),
              "say": ["Skill six writes the companion post and assigns a unique DM keyword.",
                      "That keyword could tie a booking to the article. The join from keyword to booking is not built yet, so today it is the plan, and section three shows why it matters."]},
             {"id": "keeper", "num": "02", "tag": "skill 7", "sec": 68,
              "on": "The corpus file regenerating, with arrows out to skills 1 to 6, each reconciled.",
              "head": "The keeper rewrites the rules.",
              "body": flow([("new evidence", "a capture lands", ""), ("_corpus.md", "regenerated", "on"), ("skills 1 to 6", "reconciled", "dark")]),
              "say": ["Skill seven is the keeper. When new evidence lands, it regenerates the corpus file and reconciles the other six against it.",
                      "So the rules move when the data moves. Nobody has to remember to update them."]},
         ]},
        {"num": "03", "label": "The proof", "sec": 25,
         "on": "Region 03 framed: the keyword, what converted, length, the gap tag, how a rule dies.",
         "say": ["Section three. The proof.", "How an article gets measured, and what the system does when the data has a hole."],
         "zones": [
             {"id": "utm", "num": "03", "tag": "why the keyword", "sec": 73,
              "on": "A bar: Calendly rows with the UTM field empty, 673 of 678.",
              "head": "Only a keyword can carry attribution.",
              "body": '<div>' + hbar("UTM empty", 673, 678, "673 / 678", "#B42318", 900) + hbar("UTM filled", 5, 678, "5 / 678", "#52B788", 900) + '</div>',
              "src": "Calendly rows",
              "say": ["Why the keyword matters. On the booking export, the UTM field is empty on 673 of 678 rows.",
                      "So a link tag tells you almost nothing. The DM keyword is the one path left that could tie a booking to an article. Nothing joins the two yet. What runs today is same-day correlation."]},
             {"id": "converts", "num": "03", "tag": "worked example", "sec": 88,
              "on": "A converters tile with a red NEEDS tag, then two bars against a 1x line: a tool tutorial at 0.48x, a client case study at 0.30x. Label: measured on another account, n=12.",
              "head": "What converted: a process we run.",
              "body": '<div class="tile sage" style="width:380px;min-height:300px"><b>converters</b><small>every one documents a process we operate</small>' + needs("top lift, 2.27x per doc 09") + '</div>'
                      + bars([("tool tutorial", 0.48, "#E9B949", "0.48x"), ("client case study", 0.30, "#B42318", "0.30x")], w=860, h=500, ref=1.0, ref_label="1x"),
              "src": "measured on another account I run content for &middot; n=12",
              "say": ["The worked example for this section. Twelve articles, on another account I run content for, so read this as my strongest hypothesis, measured somewhere else.",
                      "Every article that converted documented a process we operate. The two that failed did something else: a tool tutorial did 0.48x, a client case study 0.30x.",
                      "[NEEDS: the converters' top lift. Doc 09 says 2.27x, claims.md does not carry it yet.]"]},
             {"id": "length", "num": "03", "tag": "length", "sec": 73,
              "on": "Two bars: median impressions for 900 to 1,800 words at 73,300 and 1,800 to 3,000 words at 225,900. A red tag for the converter word range.",
              "head": "Length does not transfer.",
              "body": bars([("900 to 1,800 words", 73300, "#E9B949", "73,300"), ("1,800 to 3,000 words", 225900, "#52B788", "225,900")], w=900, h=480)
                      + '<div style="display:flex;flex-direction:column;gap:20px;max-width:380px">' + lbl("median impressions, reach only") + needs("converter word range, 738 to 1,012 per doc 09") + '</div>',
              "src": "41 captures &middot; 24 accounts",
              "say": ["Length. For reach, the long band wins. 1,800 to 3,000 words has a median of 225,900 impressions, against 73,300 for 900 to 1,800.",
                      "But the converters sat in a much shorter band. So a length rule from the reach lane does not carry over to the convert lane.",
                      "[NEEDS: the converter word range, 738 to 1,012 in doc 09, before it goes on screen as a number.]"]},
             {"id": "gap-ba", "num": "03", "tag": "before / after", "sec": 73,
              "on": "Before: an article paragraph with an invented number, crossed out. After: the same paragraph with a red NEEDS tag in the slot.",
              "head": "A gap beats a made-up number.",
              "body": split(
                  window("draft", skel([95, 80]) + '<div class="chip red strike">a number that sounds right</div>' + skel([85, 70]), style="width:600px") + lbl("plausible, unsourced"),
                  window("draft", skel([95, 80]) + needs("x") + skel([85, 70]), style="width:600px") + lbl("the gap stays visible")),
              "say": ["Before: the structure wants a number in a slot, so a plausible one appears. Nobody can trace it.",
                      "After: the skill writes NEEDS and leaves it visible. A gap beats a plausible fabrication, in articles, briefs and reports the same way.",
                      "You have seen these red tags all through this video. That is the rule, working on this board."]},
             {"id": "dies", "num": "03", "tag": "how a rule dies", "sec": 68,
              "on": "Three states: measured, two contradictions to observed, three contradictions to deleted.",
              "head": "How a rule dies.",
              "body": flow([("[measured]", "a rule with a script", "sage"), ("2 contradictions", "", ""), ("[observed]", "downgraded", "on"),
                            ("3 contradictions", "", ""), ("deleted", "gone from the skill", "red")], cls="sm"),
              "say": ["And when a belief dies. A measured rule that loses two contradictions inside one account is downgraded to observed. Three, and it is deleted.",
                      "The keeper does this. No one has to argue for it in a meeting."]},
             {"id": "legacy", "num": "03", "tag": "the old skill", "sec": 58,
              "on": "The legacy article skill's header, with its contradicted specs flagged in red.",
              "head": "The old skill admits its errors.",
              "body": window("legacy article skill · header", '<div class="row bad"><b>spec</b><span>contradicted by measured data</span></div>'
                             '<div class="row bad"><b>spec</b><span>contradicted by measured data</span></div>' + skel([90, 70, 80]), style="width:1100px"),
              "src": "recorded in ops/MAP.md",
              "say": ["The legacy version of the article skill still carries specs the measured data contradicts.",
                      "Its header says so, out loud, instead of quietly keeping both versions."]},
         ]},
    ],
    "cta": {"id": "cta", "num": "", "tag": "", "cls": "dark", "sec": 45, "vcls": "col", "head": "",
            "on": "Dark card: Agency Booked Calls, and Link in the description.",
            "body": '<div class="bign" style="color:#E9B949;font-size:150px;letter-spacing:-.04em;text-align:center;line-height:1">'
                    + c("Agency Booked Calls", tag="span") + '</div><div class="bigl c" style="color:#fff">Link in the description</div>',
            "say": ["If you run an established agency and want this running on your own calls, that is Agency Booked Calls. The link is in the description.",
                    "Everyone else: take one recording from this week and run step one on it. Tell me in the comments what subject came out."]},
    "final": {"sec": 15, "on": "The whole map again, zoomed out.",
              "say": ["The input, the chain, the proof. One recording in, one article out.", "Screenshot it if you want the map."]},
}
