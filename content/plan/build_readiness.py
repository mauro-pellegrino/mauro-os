#!/usr/bin/env python3
"""Build content/plan/offer-readiness.html from the TILES list below. Saved copy: content/plan/build_readiness.py"""
import html, os
HERE = "/Users/mauro/mauro-os/content/plan"
R, P, N, B = "READY", "PARTLY", "NOT BUILT", "BLOCKED"

# (lane, title, status, proof, missing, effort, owner, step)
TILES = [
 # gates
 ("gate", "Agency yes on the files", B, "content/plan/offer-decision-2026-10-09.md, section 0 (the ask text)", "The ask is not sent. No answer, no date in ownership-inventory.md. Every component built on growthub-os files waits on it", "10 min", "M", "1 · Sat 10"),
 ("gate", "Price, seats and the name", B, "offer-decision-2026-10-09.md, section 1", "$197 founding, 10 seats, then $297 is a proposal. The name is a working name only (\"The Engine\")", "5 min", "M", "2 · Sat 10"),
 ("gate", "Offer decision", R, "content/plan/offer-decision-2026-10-09.md, product-ladder.html (f80782b, 9 Oct)", "Nothing. The two items above are its open [NEEDS]", "done", "M + C", "done 9 Oct"),
 ("gate", "Price evidence: intake stranger test", R, "content/plan/intake-viability-v2.md (7b1f34e, 8 Oct)", "Nothing for the price band. Gaps 1, 2, 4 of the sheet are in the outlier tile", "done", "C", "done 8 Oct"),
 # free system
 ("free", "Video to content orchestrator", N, "None. products/ does not exist. Today the flow is a rule in CLAUDE.md section 7 plus 4 skill files", "Write 02-video-to-content/run.md: transcript in, article + 10 posts + LinkedIn post + cover prompt out, Gate last", "2 h", "C", "5 · Sun 11"),
 ("free", "Article, posts, LinkedIn skill files", B, "growthub-os skills/content/x-articles/ 01 to 07, short-form/, long-form/", "Agency yes, then a clean rewrite: drop account names from the corpus. The mauro-os copies are rewrites of agency files (inventory row 12)", "inside step 5", "C", "after 1"),
 ("free", "Worked example on Mauro's video", N, "Source exists: research/transcripts/maurojpelle/how-to-create-lead-magnets-with-claude.md", "The run itself: one article, 10 posts, LinkedIn post from that transcript, saved as example/", "inside step 5", "C", "5 · Sun 11"),
 ("free", "Company brain", B, "growthub-os skills/ops/company-brain-install.md (17 agency mentions), ops/SOURCE-ORDER.md, ops/tools/staleness-check.py", "Agency yes. Then 5 blank templates, the \"find your 3 failures\" prompt, a worked example on Ghosted Calls failures", "2 h", "C", "6 · Mon 12"),
 ("free", "The Gate", R, ".claude/agents/gate.md, .claude/hooks/voice-gate.py, skills/content/gate-playbook.md (clean, inventory row 2)", "Packaging only: a path-free hook and a blank playbook (in step 6)", "inside step 6", "C", "6 · Mon 12"),
 ("free", "Voice", P, "skills/research/voice-extraction.md (clean, 7 steps). Script: growthub-os ops/tools/voice-extract.py", "A worked example on a public account. A browser version of step 3. The script needs the agency yes or a rewrite", "[NEEDS: estimate]", "C", "not scheduled"),
 ("free", "Lead magnet module 01", P, "brand/engine/module-01-lead-magnets/ (9 pages), skills/lead-gen/lead-magnet/ (7 files), build log content/qa/lead-magnet-build-log.md", "Cut LeadShark and comment-to-DM (26 lines, 5 pages). Page 03 evidence is from an agency account. Agency yes still open (twins)", "1.5 h", "C", "7 · Tue 13"),
 ("free", "Monday read (measurement)", P, "tools/maurojpelle-baseline.py, tools/x-keywords.py, x-follow-drivers.py, /gc-monday", "tools/monday-read.py that reads any X export by column name. The x-* scripts read agency exports today", "1.5 h", "C", "17 · wk 2-4"),
 ("free", "Outlier sheet (free tool)", P, "content/lead-magnets/outlier-to-template-intake/index.html", "Gaps 1, 2, 4 of intake-viability-v2.md: floor line, gated-post flag, 390px layout", "[NEEDS: estimate]", "C", "not scheduled"),
 ("free", "ASCII visuals kit (cohort bonus)", R, "content/ascii/render.py, build_cover.py, tools/ascii-anim/ (inventory row 1: sellable)", "Drop the founder examples from ascii-article.md and the ascii-anim README", "[NEEDS: estimate]", "C", "not scheduled"),
 # package and delivery
 ("pack", "Package skeleton + scrub test", N, "None. products/engine/ does not exist (step 3 was set for Fri 9 Oct and did not run)", "The folder tree, README.md, START-HERE.md, CLAUDE.md template, the scrub grep at 0", "45 min", "C", "3 · Sat 10"),
 ("pack", "claude.ai Project version", N, "None", "instructions.md, the knowledge file list, prompts.md for the Gate and the pasted-CSV Monday read", "1 h", "C", "10 · Tue 13"),
 ("pack", "Notion version", B, "brand/engine/README.md: \"Notion is out, permanently\" (22 Aug)", "Mauro reverses the 22 Aug rule, or it stays out. Not designed", "[NEEDS: Mauro]", "M", "open"),
 ("pack", "Whop store: free + paid product", N, "None. Free-tier gating and file delivery unverified since 22 Aug", "One free product with the ZIP and Looms, one hidden paid product. Check the free tier", "30 min", "M", "4 · Sat 10"),
 ("pack", "Looms (0 of 10)", N, "List: offer-decision-2026-10-09.md, section 2", "Record 1, 2, 6 first (45 min), then 3, 4, 5, 7 to 10 (1.5 h). Evening slot, after the Growthub day", "45 min + 1.5 h", "M", "11 · Thu 15"),
 ("pack", "Stranger test 1 (Claude Code)", N, "None. content/qa/engine-stranger-test-1.md does not exist", "Juan installs from the README only on a public YouTube video, logs every stop. Needs the package first", "2 h", "J", "9 · Wed 14"),
 ("pack", "Stranger test 2 (claude.ai Project)", N, "None", "Same test, no terminal. Needs the Project version", "2 h", "J", "15 · wk 2-4"),
 ("pack", "Giveaway article + free Whop page", N, "Closest draft: LI2 \"the whole content system\" in content/drafts/2026-10-w42-w43-posts.md", "The article (\"the whole system, free\", link in bio, no comment-to-DM) and the page copy. Gate both. Publish only after the agency yes", "1 h", "M + C", "13 · Fri 16"),
 ("pack", "Weekly drop (Mon read, Wed template, Fri Gate catch)", N, "offer-decision-2026-10-09.md, section 3 rows 1, 6, 7", "Not running. The room ($49/mo) waits on 4 weeks of drops", "1 h / week", "C", "20 · wk 2-4"),
 # paid
 ("paid", "Install Sprint: the offer", P, "offer-decision-2026-10-09.md, section 1 point 2; product-ladder.html rung 1", "Defined on paper. Price and name not confirmed (gate tile)", "see gate", "M", "2 · Sat 10"),
 ("paid", "Live group install call", N, "None", "No agenda, no date, no call link. [NEEDS: not in the plan yet]", "[NEEDS: estimate]", "M", "not scheduled"),
 ("paid", "14-day first-run review", N, "None", "The review flow for each buyer's first article, 10 posts and filled brain. [NEEDS: not in the plan yet]", "[NEEDS: estimate]", "M + C", "not scheduled"),
 ("paid", "Sales page", P, "content/plan/whop-product-v1.html (drafted 8 Oct for the old intake offer)", "Rewrite for the Install Sprint: the 2 rungs, the close date, Agency Booked Calls at checkout", "[NEEDS: estimate]", "M + C", "not scheduled"),
 ("paid", "Warm list for cohort 1", B, "BACKLOG.md (blocked since August)", "Mauro names the ghostwritten owners and the churned contacts", "15 min", "M", "14 · Fri 16"),
 ("paid", "Cohort 1 open date", B, "BACKLOG.md OFFER BUILD, last line", "Mauro picks. One option: Mon 26 Oct", "[NEEDS: Mauro]", "M", "open"),
 ("paid", "Agency Booked Calls (higher option)", R, "content/offer/agency-booked-calls.html", "0 sends so far. Offered on day 14 of each Install Sprint buyer", "10 min each", "M", "22 · wk 2-4"),
]

LANES = [
 ("gate", "Before anything ships", "The yes and the decisions the rest depends on."),
 ("free", "Free Whop system: the content", "YouTube video to content, voice, company brain, the Gate, the Monday read."),
 ("pack", "Free Whop system: package and delivery", "What turns the files into something a stranger can install."),
 ("paid", "Paid: Install Sprint", "The one-time paid rung and the higher option."),
]
CLS = {R: "ready", P: "partly", N: "notbuilt", B: "blocked"}
counts = {s: sum(1 for t in TILES if t[2] == s) for s in (R, P, N, B)}
e = html.escape

def tile(t):
    _, title, st, proof, missing, effort, owner, step = t
    return f'''<div class="tile {CLS[st]}"><div class="st">{e(st)}</div><h3>{e(title)}</h3>
<div class="row"><span class="lab">proof</span><span class="mono">{e(proof)}</span></div>
<div class="row"><span class="lab">missing</span><span>{e(missing)}</span></div>
<div class="meta"><span><b>effort</b> {e(effort)}</span><span><b>owner</b> {e(owner)}</span><span><b>step</b> {e(step)}</span></div></div>'''

lanes_html = ""
for key, name, sub in LANES:
    ts = [t for t in TILES if t[0] == key]
    c = {s: sum(1 for t in ts if t[2] == s) for s in (R, P, N, B)}
    tally = " · ".join(f"{c[s]} {s.lower()}" for s in (R, P, N, B) if c[s])
    lanes_html += f'<section><div class="k">{e(tally)}</div><h2>{e(name)}</h2><p class="sub">{e(sub)}</p><div class="tiles">{"".join(tile(t) for t in ts)}</div></section>\n'

PATH = ["Agency yes (M, 10 min)", "Package skeleton (C, 45 min)", "Orchestrator + example (C, 2 h)", "Brain port (C, 2 h)", "Module 01 rewire (C, 1.5 h)", "Stranger test 1 (J, 2 h)", "Fix the stops (C, 1.5 h)", "Publish free product (M)", "Open cohort 1 (M)"]
path_html = '<span class="arr">&rarr;</span>'.join(f'<span class="pstep">{e(s)}</span>' for s in PATH)

page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Offer Readiness</title>
<meta name="description" content="Every component of the Ghosted Calls offer (free Whop system and paid Install Sprint) with its status, the file that proves it, what is missing, effort and owner. 9 Oct 2026.">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#F5EFE4;--card:#FFFDF8;--ink:#171310;--body:#3B342D;--muted:#6B6258;--line:#E2D8C6;--accent:#E0A854;--accent-ink:#8A5A12;
--g:#3F7D4E;--g-soft:#DDEBDD;--a:#B7791F;--a-soft:#F7E6C8;--n:#6B6258;--n-soft:#EFE9DE;--r:#B4442F;--r-soft:#F6DED6}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--ink);font-family:Inter,system-ui,sans-serif;font-size:15px;line-height:1.5;
background-image:radial-gradient(#17131012 1.2px,transparent 1.2px);background-size:18px 18px}}
.wrap{{max-width:1400px;margin:0 auto;padding:32px 16px 72px}}
.mono{{font-family:'JetBrains Mono',monospace;font-size:12px}}
.top{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--muted)}}
h1{{font-size:52px;line-height:1.05;letter-spacing:-.03em;font-weight:800;margin-top:24px}}
h1 span{{background:linear-gradient(transparent 62%,var(--accent) 62%)}}
.lede{{font-size:19px;color:var(--body);margin-top:12px;max-width:900px}}
.counts{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:28px}}
.cnt{{border:2px solid var(--ink);border-radius:14px;padding:14px 18px;background:var(--card)}}
.cnt .v{{font-size:40px;font-weight:800;line-height:1}}
.cnt .l{{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.08em;margin-top:6px}}
.cnt .d{{font-size:13px;color:var(--body);margin-top:4px}}
.cnt.ready{{background:var(--g-soft)}} .cnt.partly{{background:var(--a-soft)}} .cnt.notbuilt{{background:var(--n-soft)}} .cnt.blocked{{background:var(--r-soft)}}
.path{{margin-top:22px;background:var(--ink);color:var(--bg);border-radius:14px;padding:16px 18px}}
.path .k{{color:var(--accent)}}
.psteps{{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin-top:6px}}
.pstep{{font-family:'JetBrains Mono',monospace;font-size:12.5px;border:1px solid #6B6258;border-radius:8px;padding:5px 9px}}
.pstep:first-child{{background:var(--r);border-color:var(--r)}}
.arr{{color:var(--accent);font-weight:700}}
section{{margin-top:44px}}
.k{{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:6px}}
h2{{font-size:28px;letter-spacing:-.02em}}
.sub{{color:var(--body);margin:4px 0 14px}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}}
.tile{{background:var(--card);border:1px solid var(--line);border-left:8px solid var(--n);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:7px}}
.tile .st{{align-self:flex-start;font-family:'JetBrains Mono',monospace;font-size:11.5px;font-weight:700;letter-spacing:.08em;border-radius:999px;padding:3px 10px;color:#fff}}
.tile h3{{font-size:17px;line-height:1.25}}
.row{{display:grid;grid-template-columns:62px 1fr;gap:6px;font-size:13.5px;color:var(--body)}}
.lab{{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);padding-top:2px}}
.meta{{display:flex;flex-wrap:wrap;gap:6px 14px;font-family:'JetBrains Mono',monospace;font-size:12px;border-top:1px dashed var(--line);padding-top:7px;margin-top:auto}}
.meta b{{color:var(--muted);font-weight:400;text-transform:uppercase;font-size:10.5px;letter-spacing:.06em}}
.tile.ready{{border-left-color:var(--g)}} .tile.ready .st{{background:var(--g)}}
.tile.partly{{border-left-color:var(--a)}} .tile.partly .st{{background:var(--a)}}
.tile.notbuilt{{border-left-color:var(--n);background:repeating-linear-gradient(135deg,var(--card),var(--card) 10px,#F8F3EA 10px,#F8F3EA 20px)}} .tile.notbuilt .st{{background:var(--n)}}
.tile.blocked{{border-left-color:var(--r);background:#FFF8F5}} .tile.blocked .st{{background:var(--r)}}
.foot{{margin-top:40px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--muted)}}
#end{{height:1px}}
@media (max-width:700px){{h1{{font-size:36px}} .counts{{grid-template-columns:repeat(2,1fr)}}}}
</style></head><body><div class="wrap">
<div class="top"><span>Ghosted Calls · offer readiness</span><span>9 Oct 2026 · review v6 #17</span></div>
<h1>What is <span>ready</span>, what is not</h1>
<p class="lede">The offer: the whole system free on Whop (YouTube video to content, voice, company brain, the Gate) and a paid one-time Install Sprint. One tile per component. Each tile names the file that proves its status.</p>
<div class="counts">
<div class="cnt ready"><div class="v">{counts[R]}</div><div class="l">READY</div><div class="d">works today, the file exists</div></div>
<div class="cnt partly"><div class="v">{counts[P]}</div><div class="l">PARTLY</div><div class="d">exists, needs named work</div></div>
<div class="cnt notbuilt"><div class="v">{counts[N]}</div><div class="l">NOT BUILT</div><div class="d">no file yet</div></div>
<div class="cnt blocked"><div class="v">{counts[B]}</div><div class="l">BLOCKED</div><div class="d">waits on a yes or a decision</div></div>
</div>
<div class="path"><div class="k">The critical path, in order</div><div class="psteps">{path_html}</div></div>
{lanes_html}
<p class="foot">Sources: content/plan/offer-decision-2026-10-09.md, ownership-inventory.md, whop-product-v1.md, product-ladder.html, BACKLOG.md "OFFER BUILD". Step numbers and dates match BACKLOG.md (re-dated to start Sat 10 Oct). Builder: content/plan/build_readiness.py.</p>
<div id="end"></div>
</div></body></html>'''
open(os.path.join(HERE, "offer-readiness.html"), "w").write(page)
print(counts)
