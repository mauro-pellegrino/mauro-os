"""Doc 08, content working but you can't prove it.

The whole dataset is the agency's account, so every exhibit carries the label "the agency I run".
Cleared in brand/claims.md: Spearman +0.16 across twelve articles; every converter documented a
process we operate; a tool tutorial did 0.48x and a client case study 0.30x (n=12, a hypothesis
measured on another account); 649 of 678 Calendly rows under one owner, UTM empty on 673.
Every other number in doc 08 renders as [NEEDS]."""
from engine import needs

SRC = "the agency I run · 12 articles · one account"
SRCC = "the agency I run · Calendly export"
SLUG = "08-content-working-cant-prove-it"
TITLE = "Your content works. You can't prove it."


def gauge(v):
    w, x0, x1 = 1500, 90, 1410
    x = x0 + (v + 1) / 2 * (x1 - x0)
    return (f'<svg width="100%" viewBox="0 0 {w} 250">'
            f'<rect x="{x0}" y="110" width="{x1-x0}" height="26" fill="#e3dccb" stroke="#1B4332" stroke-width="3"/>'
            f'<line x1="{(x0+x1)/2}" y1="96" x2="{(x0+x1)/2}" y2="150" stroke="#1B4332" stroke-width="4"/>'
            f'<text x="{x0}" y="190" font-size="30" font-weight="800" fill="#1B4332" text-anchor="middle">-1</text>'
            f'<text x="{(x0+x1)/2}" y="190" font-size="30" font-weight="800" fill="#1B4332" text-anchor="middle">0</text>'
            f'<text x="{x1}" y="190" font-size="30" font-weight="800" fill="#1B4332" text-anchor="middle">+1</text>'
            f'<text x="{x0}" y="228" font-size="24" font-weight="600" fill="#5F6B62" text-anchor="middle">opposite</text>'
            f'<text x="{(x0+x1)/2}" y="228" font-size="24" font-weight="600" fill="#5F6B62" text-anchor="middle">no relation</text>'
            f'<text x="{x1}" y="228" font-size="24" font-weight="600" fill="#5F6B62" text-anchor="middle">lockstep</text>'
            f'<polygon points="{x-26},40 {x+26},40 {x},104" fill="#E9B949" stroke="#1B4332" stroke-width="4"/>'
            f'<text x="{x+40}" y="80" font-size="64" font-weight="900" fill="#1B4332">+0.16</text>'
            '</svg>')


def lift():
    rows = [("a tool tutorial", 0.48), ("a client case study", 0.30)]
    w, x0, scale = 1100, 330, 640
    out = [f'<svg width="100%" viewBox="0 0 {w} 250">']
    for i, (lab, v) in enumerate(rows):
        y = 30 + i * 100
        out.append(f'<text x="0" y="{y+44}" font-size="28" font-weight="700" fill="#2f3a33">{lab}</text>')
        out.append(f'<rect x="{x0}" y="{y+8}" width="{v*scale:.0f}" height="56" fill="#C62828" stroke="#1B4332" stroke-width="3"/>')
        out.append(f'<text x="{x0+v*scale+16:.0f}" y="{y+48}" font-size="36" font-weight="900" fill="#1B4332">{v:.2f}x</text>')
    bx = x0 + scale
    out.append(f'<line x1="{bx}" y1="10" x2="{bx}" y2="230" stroke="#1B4332" stroke-width="4" stroke-dasharray="10 8"/>')
    out.append(f'<text x="{bx-12}" y="244" font-size="24" font-weight="800" fill="#1B4332" text-anchor="end">1.0x = the baseline</text>')
    out.append("</svg>")
    return "".join(out)


def grid(n, on, on_col, off_col, cols=57):
    cells = "".join(f'<i style="background:{on_col if k < on else off_col}"></i>' for k in range(n))
    return (f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:4px;margin:10px 0 6px">{cells}</div>'
            '<style>#grids i{display:block;aspect-ratio:1;border-radius:2px}</style>')


DOCSTR = """<em>\"\"\"</em>
<b>post-to-call.py</b>
A booking on day D is credited
to the posts on D and D-1.

<u>This is correlation.</u>
One post, one booking, one day
is noise.
<em>\"\"\"</em>"""

TABLE_ROWS = ["a process we run", "a tool tutorial", "a mechanism we exploit", "a client case study", "a stunt",
                                          "a competitor teardown", "an opinion"]

EXHIBITS = [
    dict(id="promise", col=0, span=3, kind="card", dy=60, src=SRC, html=
         '<div class="id">By the end of this video</div><div class="hand l">You judge each post on its own metric.</div>'),
    dict(id="title", col=3, span=3, kind="folder", tab="CASE FILE 08", src="the agency I run", html=
         '<div class="h xl">Your content works. You can\'t prove it.</div>'),
    dict(id="gauge", col=6, span=3, kind="paper", dy=60, stamp=("measured", "impressions-vs-calls.py"), src=SRC, html=
         '<div class="id">Exhibit 0.1 · impressions against booked calls, Spearman</div>' + gauge(0.16)),
    # S1
    dict(id="s1", col=0, span=3, kind="folder", tab="EXHIBIT A", src="the agency I run", html='<div class="h l">The measurement</div>'),
    dict(id="dataset", col=0, span=1, kind="card", stamp=("measured", "one account"), src=SRC, html=
         '<div class="id">A1 · the set</div><div class="big m">12</div><div class="hand">articles. Impressions and calls on every one.</div>'),
    dict(id="ranks", col=1, span=2, kind="paper", stamp=("measured", "the method"), src=SRC, html=
         '<div class="id">A2 · how the test works</div>'
         '<div class="list"><div><span>1</span>Rank the 12 by impressions</div><div><span>2</span>Rank the same 12 by calls</div>'
         '<div><span>3</span>Compare the two orders</div></div>'),
    dict(id="table", col=0, span=2, kind="paper", src=SRC, html=
         '<div class="id">A3 · the full table: 12 articles, by shape</div>'
         '<div class="chips">' + "".join(f'<span class="chip">{r}</span>' for r in TABLE_ROWS) + '</div>'
         + needs("the 12 rows of impressions, calls and lift (doc 08 section 3), add to claims.md", True)),
    dict(id="pair", col=2, span=1, kind="card", src=SRC, html=
         '<div class="id">A4 · worked example</div><div class="hand">The big article against the small one.</div>'
         '<div class="lab">a tool tutorial · a process we run</div>'
         + needs("rows 3 and 9: impressions, calls, baselines", True)),
    dict(id="nuance", col=2, span=1, kind="card", stamp=("observed", "rank, not count"), src=SRC, html=
         '<div class="id">A5 · say it first</div><div class="hand">The biggest article by reach was also the biggest by calls.</div>'),
    dict(id="ba1", col=0, span=3, kind="paper", stamp=("measured", "Spearman +0.16"), src=SRC, html=
         '<div class="id">A6 · before / after</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">More impressions bring more calls</div></div>'
         '<div><div class="k">AFTER</div><div class="v">Two separate numbers. Work on both.</div></div></div>'),
    # S2
    dict(id="s2", col=3, span=3, kind="folder", tab="EXHIBIT B", src="the agency I run", html='<div class="h l">What converts</div>'),
    dict(id="lift", col=3, span=2, kind="paper", stamp=("observed", "n=12 · hypothesis"), src=SRC + " · booking lift", html=
         '<div class="id">B1 · booking lift by article shape</div>' + lift() +
         '<div class="lab">a process we run</div>' + needs("the converter lift values, doc 08 section 4", True)),
    dict(id="conv", col=5, span=1, kind="card", stamp=("observed", "n=12 · hypothesis"), src=SRC, html=
         '<div class="id">B2 · the pattern</div><div class="hand">Every converter documented a process the agency runs.</div>'),
    dict(id="hypo", col=5, span=1, kind="card", stamp=("observed", "read this stamp"), src=SRC, html=
         '<div class="id">B3 · the limit</div><div class="hand">n=12. One account. A hypothesis, measured on the agency.</div>'),
    dict(id="ba2", col=3, span=3, kind="paper", stamp=("assumed", "applied, not tested"), src=SRC, html=
         '<div class="id">B4 · worked example: rewrite one idea</div>'
         '<div class="ba"><div><div class="k">BEFORE · TOOL TUTORIAL</div><div class="v">How to use [tool]</div></div>'
         '<div><div class="k">AFTER · A PROCESS WE RUN</div><div class="v">How we run [process] with [tool]</div></div></div>'),
    # S3
    dict(id="s3", col=6, span=3, kind="folder", tab="EXHIBIT C", src="the agency I run", html='<div class="h l">Why you can\'t prove it</div>'),
    dict(id="grids", col=6, span=2, kind="paper", stamp=("measured", "published"), src=SRCC, html=
         '<div class="id">C1 · 678 Calendly rows, one square each</div>'
         '<div class="lab" style="font-weight:800">Owner field: 649 under one owner</div>' + grid(678, 649, "#1B4332", "#cfd8d2") +
         '<div class="lab" style="font-weight:800;margin-top:18px">UTM field: empty on 673</div>' + grid(678, 5, "#E9B949", "#cfd8d2")),
    dict(id="utm", col=8, span=1, kind="card", src="the agency I run · booking export", html=
         '<div class="id">C2 · a second export</div><div class="hand">UTM filled on almost none of the bookings.</div>'
         + needs("the 4 of 541 count, not in claims.md", True)),
    dict(id="doc", col=8, span=1, kind="term", stamp=("observed", "docstring"), html=
         f'<div class="bar"><i></i><i></i><i></i><span>post-to-call.py</span></div><div class="id">C3</div><pre>{DOCSTR}</pre>'
         '<div class="src">the agency I run</div>'),
    dict(id="topic", col=6, span=2, kind="paper", src=SRC.replace("12 articles · ", "") + " · one quarter", html=
         '<div class="id">C4 · topic mix on booking days against all days</div>'
         '<div class="chips"><span class="chip">AI / Claude</span><span class="chip on">formats and mechanics</span>'
         '<span class="chip">brand teardown</span><span class="chip">spend and proof</span></div>'
         + needs("the four percentages and gaps (doc 08 section 5), add to claims.md", True)),
    dict(id="monday", col=6, span=3, kind="paper", stamp=("observed", "the Monday skill"), src="the agency I run · every Monday", html=
         '<div class="id">C5 · the weekly run</div>'
         '<div class="chips"><span class="chip">call tracker</span><span class="chip">Calendly export</span>'
         '<span class="chip">X analytics</span><span class="chip">weekly targets</span></div>'
         '<div class="h" style="margin-top:20px">A diff against last week on every metric.</div>'),
    dict(id="ba3", col=6, span=3, kind="paper", stamp=("observed", "standing rules"), src="the agency I run", html=
         '<div class="id">C6 · worked example: two rules</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">Calls by Calendly booking date</div><div class="v" style="margin-top:14px">Total impressions</div></div>'
         '<div><div class="k">AFTER</div><div class="v">Calls by the date they happened</div><div class="v" style="margin-top:14px">Impressions per post</div></div></div>'),
    # close
    dict(id="intent", col=1, span=3, kind="card", clear=True, stamp=("observed", "rule set 2026-09-01"), src="the agency I run", html=
         '<div class="id">Verdict</div><div class="hand l">Declare the intent before you write. Reach piece, or convert piece.</div>'),
    dict(id="cta", col=5, span=2, kind="folder", clear="same", tab="CLOSE THE FILE", src="the agency I run", html=
         '<div class="h l">Agency Booked Calls</div><div class="lab" style="font-size:34px;font-weight:800">Link in the description</div>'),
]

STRINGS = [["a1", "dataset", "ranks"], ["a2", "ranks", "table"], ["a3", "table", "pair"], ["a4", "pair", "nuance"],
           ["a5", "ranks", "ba1"], ["g", "gauge", "ranks"],
           ["b1", "lift", "conv"], ["b2", "conv", "hypo"], ["b3", "lift", "hypo"], ["b4", "conv", "ba2"],
           ["c1", "grids", "utm"], ["c2", "utm", "doc"], ["c3", "doc", "topic"], ["c4", "monday", "ba3"],
           ["x1", "ba1", "intent"], ["x2", "ba2", "intent"], ["x3", "ba3", "intent"]]

F = []
def fr(focus, d, say, cap="", stamp=(), string=()):
    F.append(dict(focus=focus, d=d, say=say, cap=cap, stamp=list(stamp), string=list(string)))

fr("all", 8, ["(Slow flythrough.) This is the case against the most repeated assumption in content: that more impressions bring more calls.",
              "Every exhibit on this board comes from the agency I run. One account, twelve articles."])
fr(["gauge"], 8, ["The result first. Impressions against booked calls, ranked. Spearman plus 0.16. On this scale, zero means no relation. 0.16 is close to zero."],
   cap="Impressions did not predict calls", stamp=["gauge"])
fr(["promise"], 7, ["By the end you'll judge every post on its own metric, and you'll know what you can and cannot prove with the data you have."],
   cap="What you leave with")
fr(["s1", "s2", "s3"], 7, ["Three exhibits. The measurement. What converts. And why the default setup can't prove any of it."],
   cap="Three exhibits today")
fr(["s1", "dataset"], 55, ["Exhibit A. Twelve articles from one account. It is the only set that carries both numbers, impressions and calls.",
                           "Same account, so the audience size is constant. The spread is post by post, which makes it the cleanest test we have."],
   cap="Exhibit A: the measurement", stamp=["dataset"])
fr(["ranks"], 55, ["How the test works. Rank the twelve by impressions. Rank the same twelve by calls. Compare the two orders.",
                   "That comparison is the Spearman number. Plus 0.16."],
   cap="How the test works", stamp=["ranks"], string=["a1", "g"])
fr(["table"], 60, ["Here is the full table, by the shape of each article.",
                   "The values go on screen once they are in claims.md. " + needs("12 rows, doc 08 section 3")],
   cap="The full table", string=["a2"])
fr(["pair"], 70, ["Worked example. Two articles. One a tool tutorial with big reach. One a process we run with a fraction of the reach.",
                  "The small one outbooked the big one. Say the numbers only after sign-off: " + needs("47,000 against 5,500 impressions, 2 against 8 calls")],
   cap="Worked example: big against small", string=["a3"])
fr(["nuance"], 50, ["Now the row someone in the comments will find. The biggest article by reach was also the biggest by calls.",
                    "It does not break the finding. Across all twelve the ranks barely move together. Say it before they do."],
   cap="Say this before the comments do", stamp=["nuance"], string=["a4"])
fr(["ba1"], 60, ["Before: more impressions bring more calls. After: two separate numbers. You work on both, and a rule that lifts one tells you nothing about the other."],
   cap="Before and after", stamp=["ba1"], string=["a5"])
fr(["s2", "lift"], 60, ["Exhibit B, what converts. Booking lift by article shape. 1.0 is the baseline.",
                        "A tool tutorial did 0.48. A client case study did 0.30. The process pieces: " + needs("converter lifts, doc 08 section 4")],
   cap="Exhibit B: what converts", stamp=["lift"])
fr(["conv"], 55, ["Every converter documented a process the agency runs. Both failures taught a tool or narrated a case study."],
   cap="What every converter had", stamp=["conv"], string=["b1"])
fr(["hypo"], 50, ["Read the stamp. n equals twelve, one account, the agency's. This is the sharpest hypothesis I have."],
   cap="Read the stamp first", stamp=["hypo"], string=["b2", "b3"])
fr(["ba2"], 75, ["Worked example. Take an idea that would be a tool tutorial. How to use some tool.",
                 "Rewrite it as the process you run with that tool. Same tool, now the article documents your operation.",
                 "I stamped it assumed. It applies the pattern. Nobody has measured this rewrite yet."],
   cap="Worked example: rewrite one idea", stamp=["ba2"], string=["b4"])
fr(["s3", "grids"], 60, ["Exhibit C, why you can't prove it. 678 Calendly rows. 649 sit under one owner. The UTM field is empty on 673.",
                         "With data like that you cannot tie a booking to a channel, let alone to a post."],
   cap="Exhibit C: why you can't prove it", stamp=["grids"])
fr(["utm"], 50, ["A second export with a different window says the same thing. " + needs("4 of 541 bookings with UTM")],
   cap="A second export, same story", string=["c1"])
fr(["doc"], 60, ["So what actually runs? Same-day correlation. A booking on day D is credited to the posts on D and D minus one.",
                 "The script says in its own docstring that this is correlation, and that one post plus one booking on one day is noise."],
   cap="What runs: same-day correlation", stamp=["doc"], string=["c2"])
fr(["topic"], 55, ["Run across a quarter, it gives the topic mix on booking days against all days. The only topic that moves is formats and mechanics.",
                   "The values: " + needs("the topic-mix table, doc 08 section 5") + ". Close to no signal. That is the honest headline."],
   cap="The honest headline", string=["c3"])
fr(["monday"], 60, ["What replaces the guessing: the weekly run. Four inputs. The call tracker, the Calendly export, X analytics, the weekly targets. A diff against last week on every metric."],
   cap="The weekly run", stamp=["monday"])
fr(["ba3"], 70, ["Worked example, two rules from that run. Count calls by the date they happened. Someone sees a post one week and books a slot that lands in another.",
                 "And watch impressions per post. Overposting collapses the ratio while the headline number keeps climbing."],
   cap="Worked example: two rules", stamp=["ba3"], string=["c4"])
fr(["intent"], 60, ["The verdict. Declare the intent of a piece before you write it. A reach piece that books nothing did its job. A convert piece at low reach did its job. Judge each on its own metric."],
   cap="Declare the intent first", stamp=["intent"], string=["x1", "x2", "x3"])
fr("all", 25, ["Pull back. Every string on this board ends at one account and one rule: decide what the piece is for, then measure that."],
   cap="Measure what the piece is for")
fr(["cta"], 20, ["If you run an established agency and want this measured and running for your own inbound, the link is in the description. The offer is Agency Booked Calls."],
   cap="Link in the description")

for _f in F[4:-2]:
    _f["d"] = int(round(_f["d"] * 1.18 / 5) * 5)
FRAMES = F

TITLES = [
    {"title": "Your Content Is Working. You Just Can't Prove It.",
     "modelled_on": "charlie-morgan-dig.md #5, \"I've Coached 50,000 Men. You All Have The Same Problem.\" (31K): two-sentence universal callout"},
    {"title": "Impressions Didn't Predict Our Booked Calls (I Measured It)",
     "modelled_on": "01-outliers.csv, Marcos Ruiz \"I Copied a Twitter/X Account That Makes $100k/mo (it worked?)\" (6,300): claim plus parenthetical proof. Niche: Neil Patel \"How to measure the ROI of your content efforts in 2023\" (14,203 views, YouTube search 2026-10-07)"},
    {"title": "I Ranked 12 Articles by Booked Calls So You Don't Have To",
     "modelled_on": "charlie-morgan-dig.md #9, \"I Ranked Every Online Business Model So You Don't Have To\" (24K). Niche: HubSpot Marketing \"What Is Attribution Modeling? A Quick Explainer for Marketers\" (117,669 views)"},
]

NEEDS = ["the 12-row table values (impressions, calls, lift), doc 08 section 3",
         "47,000 against 5,500 impressions and 2 against 8 calls (rows 3 and 9) with the 4.2 and 3.8 baselines",
         "the converter lift values (2.27x, 2.20x, 2.12x, 1.30x, 1.03x, 0.88x) and the other shapes",
         "UTM filled on 4 of 541 bookings (_corpus.md)",
         "the topic-mix table under booking days (post-to-call.py run 2026-09-07)",
         "the same test on @maurojpelle's own data"]

NOTES_EXTRA = [
    "## For sign-off: the values behind each [NEEDS] tag", "",
    "These come from `research/video-knowledge/08-content-working-cant-prove-it.md`. None is in `brand/claims.md`. "
    "Add a row there and the tag can become the number. Do not say them on camera before that.", "",
    "- Spearman +0.05 (impressions vs lift) and +0.89 (calls vs lift).",
    "- Top four by impressions: 36 calls on 210,000 impressions. Bottom four: 28 calls on 18,800. Correct sentence: "
    "the bottom four booked 78% as many calls as the top four, on 9% of the reach. Never \"78% of the calls\".",
    "- Rows 3 and 9: 47,000 impressions booked 2 against a 4.2 baseline; 5,500 booked 8 against 3.8.",
    "- The doc has two lift sets for the process articles (2.21/2.29/2.11 in the table, 2.27/2.20/2.12 in the shape list). Reconcile before sign-off.",
    "- claims.md says \"a client case study 0.30x\"; the doc says \"someone else's case study\" (0.29 in the table). The board uses the claims.md wording.",
    "- UTM filled on 4 of 541 bookings.",
    "- Topic mix: AI/Claude 17 vs 16, formats and mechanics 12 vs 9, brand teardown 11 vs 10, spend and proof 9 vs 9.",
    "- All twelve articles run 738 to 1,012 words.",
]


def _grid(n=678, on=5, cols=39):
    return ('<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:3px">' % cols
            + "".join(f'<i style="display:block;aspect-ratio:1;background:{"#E9B949" if k < on else "#c9d2cc"}"></i>' for k in range(n)) + "</div>")


_G = ('<svg width="700" height="150" viewBox="0 0 700 150"><rect x="20" y="70" width="660" height="24" fill="#e3dccb" stroke="#1B4332" stroke-width="4"/>'
      '<line x1="350" y1="56" x2="350" y2="108" stroke="#1B4332" stroke-width="5"/>'
      '<polygon points="380,10 430,10 405,66" fill="#E9B949" stroke="#1B4332" stroke-width="4"/>'
      '<text x="440" y="52" font-size="58" font-weight="900" fill="#1B4332">+0.16</text>'
      '<text x="20" y="138" font-size="26" font-weight="800" fill="#1B4332">-1</text><text x="350" y="138" font-size="26" font-weight="800" fill="#1B4332" text-anchor="middle">0</text>'
      '<text x="680" y="138" font-size="26" font-weight="800" fill="#1B4332" text-anchor="end">+1</text></svg>')

THUMBS = [
    '<div class="word" style="left:56px;top:50px">Impressions<br><em>&#8800; calls</em></div>'
    f'<div class="ex paper" style="left:60px;top:330px;width:780px;transform:rotate(-1.5deg)"><div class="pin"></div>{_G}</div>'
    '<div class="stamp m" style="left:520px;top:520px">MEASURED</div>',
    f'<div class="ex paper" style="left:50px;top:70px;width:800px;transform:rotate(-1.2deg)"><div class="pin"></div>{_grid()}</div>'
    '<div class="word" style="left:60px;top:540px;font-size:128px">UTM: <em>empty</em></div>'
    '<div class="stamp m" style="left:560px;top:70px;transform:rotate(8deg)">MEASURED</div>',
    '<svg style="position:absolute;left:0;top:0" width="1280" height="720"><path d="M295 300 Q 520 440 700 205" fill="none" stroke="#d8a531" stroke-width="6"/></svg>'
    '<div class="ex folder" style="left:60px;top:300px;width:470px;height:330px;transform:rotate(-3deg)"><div class="pin"></div></div>'
    '<div class="ex card" style="left:560px;top:200px;width:270px;height:300px;transform:rotate(4deg);display:flex;align-items:center;justify-content:center">'
    '<div class="pin"></div><span style="font:700 260px/1 Caveat;color:#C62828">?</span></div>'
    '<div class="word" style="left:56px;top:50px;font-size:104px">You can\'t<br><em>prove it</em></div>',
]
