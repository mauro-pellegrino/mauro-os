"""Doc 06, getting an agency cited inside ChatGPT answers.

The whole doc rests on one podcast guest, captured and unverified. No number from it is in
brand/claims.md, so every number renders as [NEEDS]. Every guest claim carries the stamp
OBSERVED · 1 guest · unverified, and every string on the board runs back to the one source card."""
from engine import needs

SRC = "source: 1 podcast guest · unverified"
SLUG = "06-cited-inside-chatgpt"
TITLE = "Get your agency cited inside ChatGPT"
UNV = ("observed", "1 guest · unverified")

RESULT = (
    '<div style="background:#fff;border:3px solid #1B4332;border-radius:14px;padding:22px 26px;margin-top:6px">'
    '<div style="display:flex;justify-content:flex-end"><div style="background:#e9ecef;border-radius:18px;padding:12px 20px;font:600 26px Inter">'
    'Shortlist agencies for [your niche]</div></div>'
    '<div style="margin-top:18px;font:600 25px/1.5 Inter;color:#222">Here are three options:'
    '<div style="margin-top:10px">1. Agency A <span class="chip" style="font-size:16px;padding:2px 10px">a no-name blog</span></div>'
    '<div>2. Agency B <span class="chip" style="font-size:16px;padding:2px 10px">a major publication</span></div>'
    '<div>3. Agency C <span class="chip on" style="font-size:16px;padding:2px 10px">the agency\'s own site</span></div></div></div>'
    '<div class="lab" style="font-size:18px">mock built in HTML · no real capture yet</div>')

PLATFORMS = [("Reddit", "ChatGPT only", False), ("YouTube", "cited, views irrelevant", False), ("Medium / Quora", "yes, open by default", False),
             ("Substack", "barely, gating kills it", False), ("X", "never observed", True), ("LinkedIn", "yes, chaotically", False),
             ("Instagram", "not yet", False)]

EXHIBITS = [
    dict(id="result", col=0, span=3, kind="paper", dy=40, stamp=UNV, src=SRC, html=
         '<div class="id">Exhibit 0.1 · the claim</div><div class="h">A no-name page gets cited like a big publisher.</div>' + RESULT),
    dict(id="title", col=3, span=3, kind="folder", tab="CASE FILE 06", html=
         '<div class="h xl">Get your agency cited inside ChatGPT</div>'),
    dict(id="source", col=6, span=3, kind="paper", dy=40, stamp=("none", "0 claims verified"), src="Distribution podcast, episode 1", html=
         '<div class="id">Exhibit 0.2 · the only source</div>'
         '<div class="stat"><b>1</b><span>podcast episode</span><b>1</b><span>guest, leads growth at Gamma</span>'
         '<b>0</b><span>claims verified by me</span></div>'),
    # S1
    dict(id="s1", col=0, span=3, kind="folder", tab="EXHIBIT A", html='<div class="h l">Where answers come from</div>'),
    dict(id="split", col=0, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">A1 · two pools</div><div class="hand">Live web, or memory. You need to be in both.</div>'
         + needs("the guest's web / memory split", True)),
    dict(id="bing", col=1, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">A2 · the index</div><div class="hand">ChatGPT search runs on Bing.</div>'
         + needs("verify independently", True)),
    dict(id="memory", col=2, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">A3 · memory compounds</div><div class="hand">The first citation wins every repeat answer to that user.</div>'),
    dict(id="authority", col=0, span=2, kind="paper", stamp=UNV, src=SRC, html=
         '<div class="id">A4 · the arbitrage</div>'
         '<div class="ba"><div style="background:#fff;border-right:3px solid #1B4332"><div class="k">A NO-NAME BLOG</div><div class="v" style="text-decoration:none">cited</div></div>'
         '<div><div class="k">A MAJOR PUBLICATION</div><div class="v">cited about as often</div></div></div>'),
    dict(id="window", col=2, span=1, kind="card", stamp=("assumed", "the guest's framing"), src=SRC, html=
         '<div class="id">A5 · the clock</div><div class="hand">The window closes when the labs ship authority ranking.</div>'),
    dict(id="claude", col=0, span=3, kind="paper", stamp=UNV, src=SRC, html=
         '<div class="id">A6 · worked example: Claude barely cites anyone</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">Write pages for Claude to cite</div></div>'
         '<div><div class="k">AFTER · GAMMA</div><div class="v">Ship an official Claude app, get surfaced as a tool</div></div></div>'),
    # S2
    dict(id="s2", col=3, span=3, kind="folder", tab="EXHIBIT B", html='<div class="h l">What gets cited</div>'),
    dict(id="compare", col=3, span=3, kind="paper", stamp=UNV, src=SRC, html=
         '<div class="id">B1 · comparisons get cited</div>'
         '<div class="ba"><div><div class="k">PRAISE</div><div class="v">Why our agency is great</div></div>'
         '<div><div class="k">COMPARISON</div><div class="v">Agency A vs Agency B for [niche]</div></div></div>'),
    dict(id="ownsite", col=3, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">B2 · your own site</div><div class="hand">Your comparison pages become what the model says about competitors.</div>'),
    dict(id="open", col=4, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">B3 · open wins</div><div class="hand">Medium and Quora are indexed. A signup wall is invisible.</div>'),
    dict(id="negative", col=5, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">B4 · sentiment</div><div class="hand">One negative Reddit comment stayed in answers for months.</div>'),
    dict(id="outline", col=3, span=3, kind="term", stamp=("assumed", "shape, not tested"), html=
         '<div class="bar"><i></i><i></i><i></i><span>comparison-page.md</span></div><div class="id">B5 · worked example: one page, outlined</div>'
         '<pre><b># [Agency A] vs [Agency B] for [niche]</b>\n## Who each one fits\n## Where A wins\n## Where B wins\n## Price model, side by side\n'
         '## The verdict, by situation\n<em>open page, no signup wall</em></pre><div class="src">a template shape, no result attached</div>'),
    # S3
    dict(id="s3", col=6, span=3, kind="folder", tab="EXHIBIT C", html='<div class="h l">Where, and for how long</div>'),
    dict(id="platform", col=6, span=3, kind="paper", stamp=UNV, src=SRC, html=
         '<div class="id">C1 · the platform map</div><table class="t">'
         + "".join(f'<tr class="{"hot" if hot else ""}"><td>{p}</td><td>{v}</td></tr>' for p, v, hot in PLATFORMS) + '</table>'),
    dict(id="xrow", col=6, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">C2 · the X claim</div><div class="hand l">X: never observed being cited.</div>'
         + needs("verify before acting", True)),
    dict(id="yt", col=7, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">C3 · YouTube</div><div class="hand">Titles decide it. View count is irrelevant.</div>'
         + needs("the guest's view-count example", True)),
    dict(id="timing", col=8, span=1, kind="card", stamp=UNV, src=SRC, html=
         '<div class="id">C4 · the clock</div><div class="hand">Broad topics take weeks. Niche ones can take a day. Citations decay.</div>'
         + needs("the guest's day counts and decay window", True)),
    dict(id="ba3", col=6, span=3, kind="paper", stamp=("assumed", "if the X claim holds"), src=SRC, html=
         '<div class="id">C5 · before / after, for a brand built on X</div>'
         '<div class="ba"><div><div class="k">BEFORE</div><div class="v">Everything lives on X</div></div>'
         '<div><div class="k">AFTER</div><div class="v">Owned pages and YouTube carry the citable version</div></div></div>'),
    dict(id="test", col=6, span=3, kind="card", src="to run on camera", html=
         '<div class="id">C6 · the test</div><div class="hand l">Ask three models for an agency shortlist. Record what comes back.</div>'
         + needs("run the test, then stamp it", True)),
    # close
    dict(id="cta", col=3, span=3, kind="folder", clear=True, tab="CLOSE THE FILE", html=
         '<div class="h l">Agency Booked Calls</div><div class="lab" style="font-size:34px;font-weight:800">Link in the description</div>'),
]

GUEST = ["result", "split", "bing", "memory", "authority", "window", "claude", "compare", "ownsite", "open", "negative",
         "platform", "xrow", "yt", "timing"]
STRINGS = [[f"g_{k}", k, "source"] for k in GUEST] + [["t1", "xrow", "ba3"], ["t2", "ba3", "test"], ["t3", "compare", "outline"]]

F = []
def fr(focus, d, say, cap="", stamp=(), string=()):
    F.append(dict(focus=focus, d=d, say=say, cap=cap, stamp=list(stamp), string=list(string)))

fr("all", 8, ["(Slow flythrough.) Agency owners now ask a model for a shortlist before they ask a person. This board is how the model picks, according to one source.",
              "Watch the stamps. Nothing here is measured yet."])
fr(["result"], 8, ["The claim first. A page from nobody gets cited about as readily as a big publisher. That is the arbitrage."],
   cap="A no-name page, cited like a publisher", stamp=["result"])
fr(["source"], 7, ["And the honesty line, early. One podcast episode. One guest, who leads growth at Gamma. Zero of these claims verified by me. So today you get what to test, and you get the stamps."],
   cap="Every claim traces to one source", stamp=["source"], string=["g_result"])
fr(["s1", "s2", "s3"], 7, ["Three exhibits. Where answers come from. What gets cited. Where, and for how long."],
   cap="Three exhibits today")
fr(["s1", "split"], 55, ["Exhibit A. The guest says ChatGPT answers partly from the live web and partly from memory. " + needs("the guest's split"),
                         "So half the game is being fetchable today, and half is having been indexed already."],
   cap="Exhibit A: where answers come from", stamp=["split"], string=["g_split"])
fr(["bing"], 50, ["ChatGPT search runs on Bing, per the guest. If that holds, Bing indexing is a prerequisite. Check this one yourself before you act on it."],
   cap="Check this one yourself", stamp=["bing"], string=["g_bing"])
fr(["memory"], 50, ["Memory compounds. The model re-recommends brands it already showed a user, so the first citation wins every repeat answer to that user."],
   cap="The first citation keeps winning", stamp=["memory"], string=["g_memory"])
fr(["authority"], 55, ["The arbitrage. Publisher authority does not appear to be weighted. A no-name blog gets cited about as readily as a major publication."],
   cap="The arbitrage", stamp=["authority"], string=["g_authority"])
fr(["window"], 45, ["And the clock on it. The guest's framing is that the window closes when the labs ship authority ranking. I stamped that assumed. It is a prediction."],
   cap="Why the window closes", stamp=["window"], string=["g_window"])
fr(["claude"], 70, ["Worked example. Claude barely cites anyone, per the guest. Writing to get cited in Claude is close to wasted effort.",
                    "Gamma's answer: stop trying, ship an official Claude app. Now the model surfaces Gamma as a tool."],
   cap="Worked example: the Claude route", stamp=["claude"], string=["g_claude"])
fr(["s2", "compare"], 65, ["Exhibit B, what gets cited. Comparisons get cited. Praise never does.",
                           "Why our agency is great: never quoted. Agency A versus Agency B for your niche: quoted. The model wants pages that judge between options."],
   cap="Exhibit B: what gets cited", stamp=["compare"], string=["g_compare"])
fr(["ownsite"], 50, ["Your own site is a top source. Gamma's own website is one of its most cited sources, per the guest. So the comparison page you write is what the model repeats about your competitors."],
   cap="Your site, quoted about competitors", stamp=["ownsite"], string=["g_ownsite"])
fr(["open"], 45, ["Open content wins. Medium and Quora are still indexed. Substack barely gets cited because writers gate posts. Anything behind a signup wall is invisible."],
   cap="Gated pages are invisible", stamp=["open"], string=["g_open"])
fr(["negative"], 45, ["Negative sentiment gets cited as readily as positive. One negative Reddit comment stayed in answers for months."],
   cap="Bad comments get cited too", stamp=["negative"], string=["g_negative"])
fr(["outline"], 75, ["Worked example. One comparison page, outlined. Who each option fits, where each wins, price model side by side, the verdict by situation. Open page, no signup wall.",
                     "Stamped assumed. This is a template shape. Nobody has measured a citation off it yet."],
   cap="Worked example: one comparison page", stamp=["outline"], string=["t3"])
fr(["s3", "platform"], 65, ["Exhibit C, the platform map, one row at a time. Reddit: ChatGPT only. YouTube: cited, and view count is irrelevant. Medium and Quora: yes. Substack: barely. LinkedIn: yes, chaotically. Instagram: not yet."],
   cap="Exhibit C: the platform map", stamp=["platform"], string=["g_platform"])
fr(["xrow"], 55, ["And X. Never observed being cited. That is the most consequential claim in the whole set if you live on X, and the guest's own source flags it for checking."],
   cap="The claim that matters most here", stamp=["xrow"], string=["g_xrow"])
fr(["yt"], 50, ["YouTube: per the guest, a small video gets cited the same as a big one. The title is what matters. " + needs("the guest's view counts")],
   cap="Titles over views", stamp=["yt"], string=["g_yt"])
fr(["timing"], 55, ["Timing. Broad topics take weeks to earn a citation. Niche ones can take a day. And a citation decays, so Gamma tracks every one in a spreadsheet and re-wins the phrase. " + needs("the day counts and the decay window"),
                    "That makes this a maintenance channel."],
   cap="A maintenance channel", stamp=["timing"], string=["g_timing"])
fr(["ba3"], 65, ["If the X claim holds, here is the before and after for a brand built on X. Before: everything lives on X. After: owned pages and YouTube carry the citable version, and X keeps booking the calls."],
   cap="Before and after", stamp=["ba3"], string=["t1"])
fr(["test"], 60, ["So the test, this week, on camera, unrehearsed. Ask three models for an agency shortlist in a niche. Record what comes back. Then this board gets its first measured stamp."],
   cap="The test to run this week", string=["t2"])
fr("all", 25, ["Pull back. Every string on this board ends at one source. That is the honest state of this topic today."],
   cap="Every string ends at one source")
fr(["cta"], 20, ["If you run an established agency and want your inbound built and measured, the link is in the description. The offer is Agency Booked Calls."],
   cap="Link in the description")

for _f in F[4:-2]:
    _f["d"] = int(round(_f["d"] * 1.2 / 5) * 5)
FRAMES = F

TITLES = [
    {"title": "How Agencies Get Cited Inside ChatGPT (Clearly Explained)",
     "modelled_on": "01-outliers.csv, Greg Isenberg \"Model Context Protocol (MCP) clearly explained (why it matters)\" (1.3M). Niche: Jamie Stenton \"How to Get ChatGPT to Recommend Your Business | AI SEO Strategy for Local Businesses\" (22,454 views, YouTube search 2026-10-07)"},
    {"title": "How ChatGPT Picks Agencies (One Operator's Playbook)",
     "modelled_on": "01-outliers.csv, David Ondrej \"Build Everything with AI Agents: Here's How\" (1.7M): the how promise, with the one-source framing in the parenthetical. Niche: Exposure Ninja \"How To Rank in ChatGPT (with REAL Examples!)\" (17,930 views)"},
    {"title": "Before You Write Another Blog Post, Watch This",
     "modelled_on": "Liam Ottley \"Before You Move Your Business to ChatGPT, Watch This\" (26,755 views, YouTube search 2026-10-07); Liam Ottley is a 01-outliers.csv channel"},
]

NEEDS = ["the guest's live web / memory split (60/40 in doc 06)",
         "verify independently that ChatGPT search runs on Bing",
         "the guest's YouTube view-count example (18k vs 400k)",
         "the day counts (45 days broad, about a day niche, 30-45 days Reddit) and the three-month decay",
         "run the test: three models, one agency shortlist, recorded"]

NOTES_EXTRA = [
    "## For sign-off", "",
    "Every number in doc 06 is the guest's, and none is in `brand/claims.md`: the 60/40 web/memory split, 45 days for a broad "
    "topic, a day or 24 hours for a niche one, 30 to 45 days from a Reddit post to a citation, the 18k and 400k view videos, "
    "500k-like LinkedIn posts, a three-month decay, a 6 to 12 month Instagram bet. To say any of them on camera, add a claims.md "
    "row that states it as the guest's claim, then the tag can become the number with the UNVERIFIED stamp still on it.", "",
    "Naming the podcast and Gamma is source attribution. Gamma is not a client.",
]


_LINES = "".join(f'<div style="height:26px;margin:16px 0;width:{w}%;background:{c};border-radius:4px"></div>'
                 for w, c in [(70, "#d5d9d6"), (90, "#d5d9d6"), (55, "#E9B949"), (80, "#d5d9d6")])
_STR = "".join(f'<path d="M{x} {y} Q {(x+300)/2} {(y+520)/2+60} 300 520" fill="none" stroke="#d8a531" stroke-width="5"/>'
               for x, y in [(40, 60), (200, 30), (420, 50), (640, 90), (820, 40), (60, 300), (760, 300), (40, 680)])

THUMBS = [
    '<div class="word" style="left:56px;top:46px">Picked by<br><em>ChatGPT</em></div>'
    f'<div class="ex paper" style="left:60px;top:320px;width:780px;transform:rotate(-1.5deg)"><div class="pin"></div>'
    f'<div style="background:#fff;border:4px solid #1B4332;border-radius:16px;padding:10px 26px">{_LINES}</div></div>'
    '<div class="stamp r" style="left:470px;top:560px">UNVERIFIED</div>',
    f'<svg style="position:absolute;left:0;top:0" width="1280" height="720">{_STR}</svg>'
    '<div class="ex card" style="left:210px;top:500px;width:180px;height:170px;transform:rotate(-3deg);display:flex;align-items:center;justify-content:center">'
    '<div class="pin" style="top:6px"></div><span style="font:700 130px/1 Caveat;color:#1d2a52">1</span></div>'
    '<div class="word" style="left:430px;top:420px;font-size:120px">One<br><em>source</em></div>'
    '<div class="stamp r" style="left:60px;top:90px">UNVERIFIED</div>',
    '<div class="ex card" style="left:80px;top:250px;width:380px;height:400px;transform:rotate(-3deg);display:flex;align-items:center;justify-content:center">'
    '<div class="pin"></div><span style="font:900 300px/1 Inter;color:#111">X</span></div>'
    '<div class="word" style="left:490px;top:310px;font-size:108px">Never<br><em>cited?</em></div>'
    '<div class="stamp r" style="left:60px;top:70px">UNVERIFIED</div>',
]
