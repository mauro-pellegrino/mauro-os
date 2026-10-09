"""Doc 11, the Claude Code content system. Every number is a row in brand/claims.md,
section "The content system, as published 2026-09-10", unless it renders as [NEEDS]."""
from engine import needs

SRC = "the agency I run · published 2026-09-10"
SLUG = "11-claude-code-content-system"
TITLE = "My whole Claude Code content system"

TREE = """<b>agency-repo/</b>
├── <b>skills/</b>            <em>73 files, split by activity</em>
│   ├── content/  research/  ops/  miro/
│   └── lead-gen/  youtube/  creative-strategy/  dm-setting/
├── <b>.claude/agents/</b>    <em>4 installed agents</em>
├── <b>ops/</b>
│   ├── MAP.md          <em>the index</em>
│   ├── CONVENTIONS.md  <em>nine rules</em>
│   └── tools/          <em>25 scripts</em>
├── research/  acquisition-calls/  outbound-calls/
├── accounts/          <u>[REDACTED]</u>
└── BACKLOG.md"""

DOCSTRING = '''<em>\"\"\"</em>
<b>Limit, read this first.</b>
It measures ALL inbound,
every account at once.

  649 of 678 rows: one owner
  673 of 678 rows: UTM empty
<em>\"\"\"</em>'''

TOOLS = """<b>ops/tools/</b>   <em>25 scripts</em>
  impressions-vs-calls.py
  consolidate-exports.py
  post-to-call.py
  trace-bookings.py
  call-structure.py
  article-title-features.py
  lane-tables.py
  backlog-sync.py
  build-dashboard.py
  <em>...</em>"""


def bars(rows, maxv, w=520, unit=""):
    """rows: (label, value, highlight). Horizontal bars, values printed."""
    h = len(rows) * 74 + 6
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    for i, (lab, v, hot) in enumerate(rows):
        y = i * 74
        bw = max(6, (w - 40) * v / maxv)
        out.append(f'<text x="0" y="{y+22}" font-size="21" font-weight="700" fill="#2f3a33">{lab}</text>')
        out.append(f'<rect x="0" y="{y+32}" width="{bw:.0f}" height="34" fill="{"#E9B949" if hot else "#9fb3a7"}" stroke="#1B4332" stroke-width="3"/>')
    out.append("</svg>")
    return "".join(out)


DROP = ('<svg width="520" height="250" viewBox="0 0 520 250">'
        '<line x1="20" y1="226" x2="500" y2="226" stroke="#1B4332" stroke-width="3"/>'
        '<rect x="70" y="20" width="150" height="206" fill="#9fb3a7" stroke="#1B4332" stroke-width="3"/>'
        '<rect x="300" y="152" width="150" height="74" fill="#C62828" stroke="#1B4332" stroke-width="3"/>'
        '<text x="145" y="248" font-size="20" font-weight="700" text-anchor="middle" fill="#2f3a33">June</text>'
        '<text x="375" y="248" font-size="20" font-weight="700" text-anchor="middle" fill="#2f3a33">August</text>'
        '<text x="375" y="134" font-size="44" font-weight="900" text-anchor="middle" fill="#C62828">-64%</text>'
        '</svg>')

EXHIBITS = [
    # hook row
    dict(id="counts", col=0, span=3, kind="paper", dy=60, stamp=("measured", "published counts"), src=SRC, html=
         '<div class="id">Exhibit 0.2 · the inventory</div>'
         '<div class="stat"><b>1</b><span>repo, 11 top-level areas</span><b>73</b><span>skill files, 8 activity folders</span>'
         '<b>25</b><span>scripts, each states its limit</span><b>4</b><span>agents, all defensive</span></div>'),
    dict(id="title", col=3, span=3, kind="folder", tab="CASE FILE 11", html=
         '<div class="h xl">My whole Claude Code content system</div>'),
    dict(id="result", col=6, span=3, kind="paper", dy=60, stamp=("measured", "Calendly export, 2026"), src="the agency I run · total, no channel split", html=
         '<div class="id">Exhibit 0.1 · the result</div><div class="big">150+</div>'
         '<div class="lab">qualified booked calls for the agency in 2026</div>'),
    # section 1 · the skeleton (cols 0-1)
    dict(id="s1", col=0, span=3, kind="folder", tab="EXHIBIT A", html='<div class="h l">The skeleton</div>'),
    dict(id="tree", col=0, span=2, kind="term", stamp=("measured", "counted 2026-09-07"), html=
         f'<div class="bar"><i></i><i></i><i></i><span>repo tree, screen safe</span></div><div class="id">Exhibit A1</div><pre>{TREE}</pre>'
         '<div class="src">the agency I run · account folders redacted</div>'),
    dict(id="map", col=2, span=1, kind="card", stamp=("observed", "MAP.md"), src=SRC, html=
         '<div class="id">Exhibit A2 · ops/MAP.md</div><div class="hand l">Route it, or it gets rebuilt.</div>'),
    dict(id="sop", col=2, span=1, kind="paper", stamp=("observed", "MAP.md"), src=SRC, html=
         '<div class="id">Exhibit A3 · incident</div><div class="h">An agent rebuilt an outbound SOP from scratch</div>'
         f'<div class="lab">time lost</div>{needs("the 45 minutes, add to claims.md", True)}'),
    dict(id="skills", col=0, span=2, kind="paper", stamp=("measured", "published counts"), src=SRC, html=
         '<div class="id">Exhibit A4 · skills/</div><div class="row"><div class="big m">73</div><div class="lab">files in 8 activity folders</div></div>'
         '<div class="chips"><span class="chip">content</span><span class="chip">research</span><span class="chip">ops</span><span class="chip">miro</span>'
         '<span class="chip">lead-gen</span><span class="chip">youtube</span><span class="chip">creative-strategy</span><span class="chip">dm-setting</span></div>'),
    dict(id="client", col=0, span=2, kind="paper", stamp=("assumed", "design rule, untested"), src=SRC, html=
         '<div class="id">Exhibit A5 · before / after</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">A folder per client</div><div class="lab">rots when the client leaves</div></div>'
         '<div><div class="k">AFTER</div><div class="v">A folder per activity</div><div class="lab">survives every client</div></div></div>'),
    dict(id="corpus", col=2, span=1, kind="card", stamp=("measured", "corpus file"), src=SRC, html=
         '<div class="id">Exhibit A6 · x-articles/</div><div class="big m">41</div><div class="hand">real captures behind one evidence file</div>'),
    dict(id="miro", col=2, span=1, kind="term", stamp=("measured", "2026-08-03/04"), html=
         '<div class="bar"><i></i><i></i><i></i><span>miro/api-gotchas.md</span></div><div class="id">Exhibit A7</div>'
         '<pre><b>200</b> items: edit and delete stop\n\n<b>20 of 37</b> items failed\n<u>one bad attribute</u>\n<em>no useful error</em></pre>'
         '<div class="src">the agency I run · published</div>'),
    # section 2 · every agent is a scar (cols 2-3)
    dict(id="s2", col=3, span=3, kind="folder", tab="EXHIBIT B", html='<div class="h l">Every agent is a scar</div>'),
    dict(id="perf", col=3, span=1, kind="card", stamp=("measured", "published"), src=SRC, html=
         '<div class="id">B1 · performance-loop</div><div class="hand">Monthly impressions fell 64%, June to August. Nobody saw it for two months.</div>'),
    dict(id="sweep", col=4, span=1, kind="card", stamp=("observed", "incident log"), src=SRC, html=
         '<div class="id">B2 · signal-sweep</div><div class="hand">A catch-up missed one group DM. It held the number that mattered.</div>'),
    dict(id="qa", col=5, span=1, kind="card", stamp=("measured", "published"), src=SRC, html=
         '<div class="id">B3 · board-qa</div><div class="hand">Boards went out too full to record. Now: 15 checks, the first 4 block.</div>'),
    dict(id="ylm", col=3, span=1, kind="card", stamp=("observed", "agent file"), src=SRC, html=
         '<div class="id">B4 · youtube-lead-magnet</div><div class="hand">Packaging drift. Rule one: run the existing skill.</div>'),
    dict(id="drop", col=4, span=2, kind="paper", stamp=("measured", "published"), src=SRC, html=
         '<div class="id">Exhibit B5 · worked example: the drop</div>'
         f'<div class="row" style="align-items:center;gap:34px">{DROP}<div class="h">Two months before anyone looked.</div></div>'),
    dict(id="ba2", col=3, span=3, kind="paper", stamp=("assumed", "no catch logged yet"), src=SRC, html=
         '<div class="id">Exhibit B6 · before / after</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">A human checks when he remembers</div></div>'
         '<div><div class="k">AFTER</div><div class="v">An agent reads the numbers every run</div></div></div>'),
    dict(id="defensive", col=3, span=3, kind="paper", stamp=("measured", "published"), src=SRC, html=
         '<div class="id">Exhibit B7 · the pattern</div><div class="stat"><b>4</b><span>agents installed</span><b>4</b><span>are defensive</span>'
         '<b>0</b><span>reach out to a human</span></div>'),
    # section 3 · every number has a receipt (cols 4-5)
    dict(id="s3", col=6, span=3, kind="folder", tab="EXHIBIT C", html='<div class="h l">Every number has a receipt</div>'),
    dict(id="tools", col=6, span=1, kind="term", stamp=("measured", "published count"), html=
         f'<div class="bar"><i></i><i></i><i></i><span>ls ops/tools</span></div><div class="id">Exhibit C1</div><pre>{TOOLS}</pre>'
         '<div class="src">the agency I run</div>'),
    dict(id="doc", col=7, span=1, kind="term", stamp=("measured", "published"), html=
         f'<div class="bar"><i></i><i></i><i></i><span>trace-bookings.py, line 1</span></div><div class="id">Exhibit C2</div><pre>{DOCSTRING}</pre>'
         '<div class="src">the agency I run · Calendly export</div>'),
    dict(id="conv", col=8, span=1, kind="paper", stamp=("observed", "CONVENTIONS.md"), src=SRC, html=
         '<div class="id">Exhibit C3 · 9 conventions, 4 carry the weight</div>'
         '<div class="list"><div><span>1</span>Every claim carries an evidence tag</div><div><span>2</span>Every number traces to a script</div>'
         '<div><span>3</span>Every script states its own limit</div><div><span>4</span>Decisions are dated, in the file they govern</div></div>'),
    dict(id="backwards", col=6, span=3, kind="paper", stamp=("measured", "published"), src=SRC, html=
         '<div class="id">Exhibit C4 · worked example: the claim that ran backwards</div>'
         '<div class="hand" style="margin-bottom:16px">"The worked example is the section that converts."</div>'
         + bars([("the worked example section", 60000, False), ("the winning section", 264000, True)], 264000, w=1100) +
         '<div class="row" style="justify-content:space-between"><span class="lab">60,000</span><span class="lab">264,000</span></div>'),
    dict(id="ba3", col=6, span=3, kind="paper", stamp=("observed", "CONVENTIONS.md"), src=SRC, html=
         '<div class="id">Exhibit C5 · before / after</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">A number worked out in chat</div><div class="lab">gone at the next context clear</div></div>'
         '<div><div class="k">AFTER</div><div class="v">A saved script that prints it</div><div class="lab">same number every rerun</div></div></div>'),
    # close
    dict(id="open", col=1, span=3, kind="card", clear=True, stamp=("observed", "case still open"), src=SRC, html=
         '<div class="id">Open case · next video</div><div class="hand l">Nothing in this repo books a call on its own.</div>'),
    dict(id="cta", col=5, span=2, kind="folder", tab="CLOSE THE FILE", dy=-0, html=
         '<div class="h l">Agency Booked Calls</div><div class="lab" style="font-size:34px;font-weight:800">Link in the description</div>'),
]
# the CTA sits beside the open card, same row
EXHIBITS[-1]["clear"] = "same"

STRINGS = [
    ["a1", "tree", "map"], ["a2", "map", "sop"], ["a3", "tree", "skills"], ["a4", "skills", "client"],
    ["a5", "skills", "corpus"], ["a6", "skills", "miro"],
    ["b1", "perf", "drop"], ["b2", "drop", "ba2"], ["b3", "sweep", "defensive"], ["b4", "qa", "defensive"],
    ["b5", "ylm", "defensive"], ["b6", "perf", "defensive"],
    ["c1", "tools", "doc"], ["c2", "conv", "backwards"], ["c3", "backwards", "ba3"], ["c4", "doc", "conv"],
    ["x1", "defensive", "open"], ["x2", "result", "counts"],
]

F = []
def fr(focus, d, say, cap="", stamp=(), string=()):
    F.append(dict(focus=focus, d=d, say=say, cap=cap, stamp=list(stamp), string=list(string)))

fr("all", 8, ["(Flythrough of the whole board, slow.) This is my whole Claude Code content system, pinned up like a case file.",
              "Every card on this board is a real file, and every stamp tells you how sure I am about it."])
fr(["result"], 8, ["Start with the result. Over 150 qualified booked calls for the agency I run, in 2026.",
                   "That is the Calendly total. I am not splitting it by channel, because the data cannot carry that split. I'll show you why later."],
   cap="The result first", stamp=["result"])
fr(["counts"], 7, ["What sits behind it is one repo. 73 skill files, 25 scripts, 4 agents.",
                             "By the end you'll know how to build the same skeleton and keep it honest."],
   cap="One repo behind it", stamp=["counts"], string=["x2"])
fr(["s1", "s2", "s3"], 7, ["Today we go over three exhibits. The skeleton. The agents, and the incident behind each one. And the receipts: how every number traces back to a script."],
   cap="Three exhibits today")
# section 1
fr(["s1", "tree"], 50, ["Exhibit A, the skeleton. One repo, eleven top-level areas, and all of it indexed in one file.",
                        "Skills, agents, ops, research, and the account folders, which I redacted. You'll never see a client name on this board.",
                        "Read the comments on the right. Every area has an owner and a reason to exist."],
   cap="Exhibit A: the skeleton", stamp=["tree"])
fr(["map"], 45, ["The rule that holds it together lives in MAP.md. Route it, or it gets rebuilt.",
                 "If a file exists and the map does not point at it, the next agent cannot find it, so it builds the thing again."],
   cap="One rule holds it together", stamp=["map"], string=["a1"])
fr(["map", "sop"], 70, ["Worked example. An agent rebuilt an outbound SOP from scratch, because the original was not in the map.",
                        "The time lost on that is " + needs("the 45 minutes from MAP.md, add to claims.md") + ". Say the figure only after it is in claims.md.",
                        "That day the rule went into the map. One line, and the rebuild has a place to stop."],
   cap="Worked example: the rebuilt SOP", stamp=["sop"], string=["a2"])
fr(["skills"], 55, ["Now the skills folder. 73 files across eight folders: content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting.",
                    "Each name is an activity. Read it again. None of them is a client."],
   cap="Split by activity", stamp=["skills"], string=["a3"])
fr(["client"], 60, ["Before and after. Before, a folder per client. When the client leaves, the folder rots, and the same skill gets rebuilt inside the next client.",
                    "After, a folder per activity. A content skill survives every client.",
                    "I stamped this one assumed. It is a design rule. I have not measured the rot."],
   cap="Before and after", stamp=["client"], string=["a4"])
fr(["corpus", "miro"], 60, ["Two folders worth opening. The article skills read from one evidence file, built from 41 real captures.",
                            "And the miro folder has a gotchas file that exists only because things broke. Past 200 items you cannot edit or delete through the API. One bad attribute failed 20 of 37 items and the error named none of them."],
   cap="The folders built from breakage", stamp=["corpus", "miro"], string=["a5", "a6"])
# section 2
fr(["s2", "perf", "sweep", "qa", "ylm"], 45, ["Exhibit B. The four agents. An agent runs without being asked, and every one of these exists because something got missed."],
   cap="Exhibit B: every agent is a scar")
fr(["perf"], 50, ["performance-loop. Monthly impressions fell 64% between June and August 2026, and nobody noticed for two months."],
   cap="Scar one", stamp=["perf"])
fr(["drop"], 70, ["Worked example. Here is the drop. June on the left, August on the right, minus 64%.",
                  "Nobody noticed for two months. A drop like that becomes a quarter if nothing is watching."],
   cap="Worked example: the drop", stamp=["drop"], string=["b1"])
fr(["ba2"], 55, ["Before: a human checks the numbers when he remembers. After: an agent reads them on every run.",
                 "I stamped the after as assumed. The agent is installed. I have no logged catch yet to show you."],
   cap="Before and after", stamp=["ba2"], string=["b2"])
fr(["sweep"], 50, ["signal-sweep. A catch-up missed one group DM, and that DM held the number that mattered. It also served an auto-generated queue as if it were the priorities.",
                   "Now an agent reads every channel before anybody tells me what was asked."],
   cap="Scar two", stamp=["sweep"])
fr(["qa"], 45, ["board-qa. Boards went out too full to record. The gate answers one question with fifteen checks, and the first four stop the run."],
   cap="Scar three", stamp=["qa"])
fr(["ylm"], 40, ["youtube-lead-magnet. Packaging drifted from video to video. Its first instruction is to run the existing skill and invent no rules."],
   cap="Scar four", stamp=["ylm"])
fr(["defensive"], 45, ["Pull the strings together and you see the pattern. Four agents, four defensive. Zero of them reach out to a human."],
   cap="All four play defence", stamp=["defensive"], string=["b3", "b4", "b5", "b6"])
# section 3
fr(["s3", "tools"], 50, ["Exhibit C, the receipts. 25 scripts in ops/tools.",
                         "The rule: the analysis that produced a number gets saved as a script. A calculation in a chat dies at the next context clear."],
   cap="Exhibit C: the receipts", stamp=["tools"])
fr(["doc"], 60, ["And every script states its own limit in its first lines. This one looked like it measured one account's bookings.",
                 "It measures all inbound, every account at once. 649 of 678 Calendly rows sit under one owner, and the UTM field is empty on 673. So the docstring says it in capitals."],
   cap="Each script states its limit", stamp=["doc"], string=["c1"])
fr(["conv"], 55, ["Nine conventions. Four carry the weight: an evidence tag on every claim, a script behind every number, a limit in every script, and dated decisions in the file they govern."],
   cap="Four rules carry the weight", stamp=["conv"], string=["c4"])
fr(["backwards"], 70, ["Worked example. A skill said the worked example was the section that converts. It felt obviously true.",
                       "We measured it. The worked example section did 60,000. The winning section did 264,000. The claim ran backwards.",
                       "That is why every claim on this board carries a stamp."],
   cap="Worked example: it ran backwards", stamp=["backwards"], string=["c2"])
fr(["ba3"], 50, ["Before: a number worked out in chat, gone at the next context clear, then re-derived a bit differently, and two numbers disagree in a meeting.",
                 "After: a saved script that prints the same number every rerun."],
   cap="Before and after", stamp=["ba3"], string=["c3"])
# close
fr(["open"], 45, ["The open case. Nothing in this repo books a call on its own. Every agent catches, gates or packages.",
                  "The agent that causes a call is the next video."],
   cap="What it still cannot do", stamp=["open"], string=["x1"])
fr("all", 25, ["Pull back. The skeleton, the scars, the receipts. Every string ends on a file you can open."],
   cap="Three exhibits, one repo")
fr(["cta"], 20, ["If you run an established agency and want this installed for your own inbound, the link is in the description. The offer is called Agency Booked Calls."],
   cap="Link in the description")

for _f in F[4:-2]:
    _f["d"] = int(round(_f["d"] * 1.2 / 5) * 5)
FRAMES = F
NEEDS = ["the 45 minutes lost to the rebuilt SOP (MAP.md), not in claims.md",
         "the working title and the $100k/$150k/$500k figure from doc 11, owned by the titles agent, none cleared"]

NOTES_EXTRA = [
    "## Left off the board on purpose", "",
    "- The $100k/mo, $150k MRR and ~$500k figures from doc 11. None is in `brand/claims.md`. The titles agent owns the title.",
    "- The signal-sweep incident's $1M/month target. It is the agency's number.",
    "- The 26 content vehicles (13 ours), the seven x-articles files and the daily export times. None is in claims.md.",
    "- The daily loop (plan from BACKLOG.md, tick from Google Tasks). Doc 11 presents v3 as the fix, and claims.md now records "
    "185 tasks pushed from 31 Aug and 0 ticked. Mauro decides whether that becomes a scar on this board.",
    "- The 150+ calls are the Calendly total with no channel split, per the attribution note in claims.md. Doc 11 says never claim "
    "the system produces revenue; the board never links the calls to revenue.",
]
