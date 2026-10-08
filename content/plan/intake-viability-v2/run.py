"""Stranger test v2 of content/lead-magnets/outlier-to-template-intake/index.html.

Two personas, each in a fresh headless Chromium context (empty localStorage).
Usage: python3 content/plan/intake-viability-v2/run.py <label>
  label = before | after  (screenshots go to content/plan/intake-viability-v2/<label>/)
Writes <label>/log.json with the page state after every step.

Persona A input: LinkedIn rows. Column layout and cell formats copied from a real LinkedIn
export (TOP POSTS sheet: "Post URL, Post Publish Date, Engagements, '', Post URL, Post Publish
Date, Impressions") and from the LinkedIn feed ("27 comments", relative dates "2w").
The VALUES are [fixture] numbers: they test the parser, they describe no real account.
Persona B input: real public @maurojpelle posts from research/x-analytics (Mauro's own export),
shown the way X displays them ("2.3K", "2,316 Views") and as raw export rows.
"""
import csv, json, pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[3]
PAGE = (ROOT / "content/lead-magnets/outlier-to-template-intake/index.html").as_uri()
LABEL = sys.argv[1] if len(sys.argv) > 1 else "before"
OUT = pathlib.Path(__file__).parent / LABEL
OUT.mkdir(parents=True, exist_ok=True)
LOG = []

# ---------- persona A fixtures (values invented for the test, formats real) ----------
A_FEED = "\n".join([
    "2d\tWe fired our biggest client last month\thttps://www.linkedin.com/posts/peer-agency_fixture-01\t27 comments",
    "4d\tThree hires that changed our margins\thttps://www.linkedin.com/posts/peer-agency_fixture-02\t15 comments",
    "1w\tThe proposal template we stopped using\thttps://www.linkedin.com/posts/peer-agency_fixture-03\t19 comments",
    "1w\tWhat a $40k retainer looks like inside\thttps://www.linkedin.com/posts/peer-agency_fixture-04\t140 comments",
    "2w\tOur Monday meeting has one slide\thttps://www.linkedin.com/posts/peer-agency_fixture-05\t12 comments",
    "2w\tHiring is the wrong fix for churn\thttps://www.linkedin.com/posts/peer-agency_fixture-06\t22 comments",
    "3w\tComment PLAYBOOK and I'll send it\thttps://www.linkedin.com/posts/peer-agency_fixture-07\t1,204 comments",
    "3w\tWhy we stopped doing free audits\thttps://www.linkedin.com/posts/peer-agency_fixture-08\t—",
    "1mo\tThe client call that saved Q3\thttps://www.linkedin.com/posts/peer-agency_fixture-09\t18 comments",
    "1mo\tFive numbers I check every Friday\thttps://www.linkedin.com/posts/peer-agency_fixture-10\t64 comments",
    "1mo\tA rejected pitch, line by line\thttps://www.linkedin.com/posts/peer-agency_fixture-11\t11 comments",
    "1mo\tWe raised prices 30% and lost one client\thttps://www.linkedin.com/posts/peer-agency_fixture-12\t31 comments",
])
A_EXPORT = "\n".join([
    "Post URL\tPost Publish Date\tEngagements\t\tPost URL\tPost Publish Date\tImpressions",
    "https://www.linkedin.com/posts/own-agency_fixture-a\t9/30/2026\t96\t\thttps://www.linkedin.com/posts/own-agency_fixture-b\t10/1/2026\t12400",
    "https://www.linkedin.com/posts/own-agency_fixture-b\t10/1/2026\t71\t\thttps://www.linkedin.com/posts/own-agency_fixture-a\t9/30/2026\t8120",
    "https://www.linkedin.com/posts/own-agency_fixture-c\t9/23/2026\t40\t\thttps://www.linkedin.com/posts/own-agency_fixture-d\t9/16/2026\t3310",
    "https://www.linkedin.com/posts/own-agency_fixture-d\t9/16/2026\t35\t\thttps://www.linkedin.com/posts/own-agency_fixture-c\t9/23/2026\t2950",
    "https://www.linkedin.com/posts/own-agency_fixture-e\t9/9/2026\t22\t\thttps://www.linkedin.com/posts/own-agency_fixture-e\t9/9/2026\t2140",
    "https://www.linkedin.com/posts/own-agency_fixture-f\t9/2/2026\t18\t\thttps://www.linkedin.com/posts/own-agency_fixture-g\t8/26/2026\t1980",
    "https://www.linkedin.com/posts/own-agency_fixture-g\t8/26/2026\t15\t\thttps://www.linkedin.com/posts/own-agency_fixture-f\t9/2/2026\t1710",
])

# ---------- persona B: real @maurojpelle rows ----------
def x_display(n):
    """How the X feed shows a view count."""
    if n >= 1_000_000: return f"{n/1e6:.1f}M".replace(".0M", "M")
    if n >= 10_000: return f"{n/1e3:.1f}K".replace(".0K", "K")
    if n >= 1_000: return f"{n/1e3:.1f}K".replace(".0K", "K")
    return str(n)

csvp = ROOT / "research/x-analytics/maurojpelle-2026-07-08-to-2026-10-05.csv"
raw_lines = csvp.read_text(encoding="utf-8").splitlines()
rows = list(csv.DictReader(raw_lines))
orig = [r for r in rows if not r["Post text"].startswith("@") and not r["Post text"].startswith("RT ")]
pick = orig[:15]  # newest first in the export order is not guaranteed; we take the file order
B_FEED_LINES = []
for k, r in enumerate(pick):
    n = int(r["Impressions"])
    first = r["Post text"].replace("\n", " ")[:45].replace("\t", " ")
    val = x_display(n)
    if k == 2: val = f"{n:,} Views"          # copied from the post detail page
    if k == 6: val = ""                        # views not visible on an article card
    B_FEED_LINES.append(f'{r["Date"]}\t{first}\t{r["Post Link"]}\t{val}')
B_FEED = "\n".join(B_FEED_LINES)
ids = {r["Post id"] for r in pick}
B_EXPORT = "\n".join([raw_lines[0]] + [l for l in raw_lines[1:] if l.split(",", 1)[0] in ids])
B_TRUTH = [int(r["Impressions"]) for r in pick]


def state(p):
    return p.evaluate("""() => ({
      verdict: document.getElementById('verdict').textContent,
      count: document.getElementById('sCount').textContent,
      median: document.getElementById('sMedian').textContent,
      line: document.getElementById('sLine').textContent,
      cap: document.getElementById('sCap').textContent,
      floor: document.getElementById('floor').value,
      rows: [...document.querySelectorAll('#rows tbody tr')].map(tr => {
        const v = [...tr.querySelectorAll('input')].map(i => i.value);
        return {date: v[0], first: v[1], link: v[2], number: v[3],
                ratio: tr.querySelector('.ratio').textContent,
                verdict: tr.lastElementChild.textContent};
      }),
      caps: document.querySelectorAll('#caps .cap').length,
      prompt: document.getElementById('prompt').textContent,
      warn: (document.getElementById('pasteNote')||{}).textContent || ''
    })""")


def shot(p, name, sel=None):
    path = OUT / f"{name}.png"
    if sel: p.locator(sel).screenshot(path=str(path))
    else: p.screenshot(path=str(path), full_page=True)
    return path.name


def step(p, persona, name, note, sel=None):
    s = state(p)
    LOG.append({"persona": persona, "step": name, "note": note, "shot": shot(p, f"{persona}-{name}", sel), "state": s})


def paste(p, text):
    p.evaluate("document.querySelector('details').open = true")
    p.fill("#paste", text)
    p.click("#doPaste")
    p.wait_for_timeout(150)


with sync_playwright() as pw:
    br = pw.chromium.launch()
    errors = []

    # ---------------- Persona A: agency owner, LinkedIn, VA does the copying ----------------
    ctx = br.new_context(viewport={"width": 1366, "height": 900})
    p = ctx.new_page(); p.on("console", lambda m: errors.append(("A", m.type, m.text)) if m.type == "error" else None)
    p.goto(PAGE); p.wait_for_timeout(400)
    step(p, "A", "01-landing", "first screen", None)
    p.fill("#handle", "@peer-agency-owner")
    p.select_option("#platform", "linkedin")
    paste(p, A_FEED)
    step(p, "A", "02-feed-paste", "VA pastes 12 peer posts from a sheet, numbers as LinkedIn shows them", "#s1")
    step(p, "A", "03-capture", "step 2 after the feed paste", "#s2")
    step(p, "A", "04-prompt", "step 3 prompt", "#s3")
    paste(p, A_EXPORT)
    step(p, "A", "05-own-export", "owner pastes his own LinkedIn export TOP POSTS rows with the header", "#s1")
    p.fill("#floor", "50")
    p.dispatch_event("#floor", "input")
    paste(p, A_FEED)
    step(p, "A", "06-floor-50", "back to the peer feed, floor lowered to 50 comments", "#s1")
    step(p, "A", "07-capture-floor-50", "step 2 with floor 50", "#s2")
    step(p, "A", "08-prompt-floor-50", "step 3 with floor 50", "#s3")
    step(p, "A", "09-steps-4-5", "steps 4 and 5 as a stranger sees them", "#s5")
    ctx.close()

    # ---------------- Persona B: B2B consultant, X, ChatGPT ----------------
    ctx = br.new_context(viewport={"width": 1280, "height": 900})
    p = ctx.new_page(); p.on("console", lambda m: errors.append(("B", m.type, m.text)) if m.type == "error" else None)
    p.goto(PAGE); p.wait_for_timeout(400)
    p.fill("#handle", "@MauroJPelle")
    paste(p, B_FEED)
    step(p, "B", "01-feed-paste", "15 real @maurojpelle posts, views as X shows them, one '2,316 Views', one blank", "#s1")
    paste(p, B_EXPORT)
    step(p, "B", "02-export-paste", "same 15 posts pasted as raw rows of the X analytics CSV, header included", "#s1")
    paste(p, B_FEED)
    p.fill("#floor", "1000"); p.dispatch_event("#floor", "input")
    step(p, "B", "03-floor-1000", "feed paste again, floor lowered to 1,000", "#s1")
    step(p, "B", "04-capture", "step 2 with floor 1,000", "#s2")
    step(p, "B", "05-prompt", "step 3 prompt for ChatGPT", "#s3")
    ctx.close()

    # phone width, persona B
    ctx = br.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2)
    p = ctx.new_page(); p.goto(PAGE); p.wait_for_timeout(300)
    paste(p, B_FEED)
    step(p, "B", "06-phone", "390px phone, after the feed paste", "#s1")
    ctx.close()
    br.close()

json.dump({"label": LABEL, "b_truth": B_TRUTH, "console_errors": errors, "log": LOG},
          open(OUT / "log.json", "w"), indent=1, ensure_ascii=False)
print("errors:", errors)
for e in LOG:
    s = e["state"]
    print(f'{e["persona"]} {e["step"]}: count={s["count"]} median={s["median"]} cap={s["cap"]} caps={s["caps"]} floor={s["floor"]}')
    print("   verdict:", s["verdict"][:160])
    if s["warn"]: print("   warn:", s["warn"])
