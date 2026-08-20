# Lead Magnet System: QA Build Log

**Run by:** standing in for "Juan" (someone who is not Mauro), working alone from the docs, per `docs/juan-lead-magnet-test-brief.md`.
**Date:** 19 Aug 2026
**Goal:** build one magnet from the docs alone, log every gap, keep every invented prompt, time each stage. Prove the instructions are followable without Mauro in the room.

**What I built:** a prompt-swipe-file magnet, *"10 Prompts That Turn One Video Into a Week of Content."* Full asset is in [magnet-youtube-to-week-of-content.md](magnet-youtube-to-week-of-content.md). Source material: `research/transcripts/maurojpelle/youtube-first-content-system-with-ai.md`.

**Docs I was told to use:** `_master.md` + `prompt-swipe-file.md` + `notion-delivery-build.md`, cross-checked against `brand/lead-magnets/shareable/lead-magnet-system.md`. I also read the three required-reading brand files (`voice.md`, `audience.md`, `positioning.md`) because `_master.md` says to read them in full before drafting.

---

## THE HEADLINE FINDING (read this first)

**The skill is written to be run *with* Mauro, not alone.** The subtype file's Input Form opens with "Before drafting, get these from Mauro" and closes with "If any of these are missing, ask before drafting. Don't guess on tool name or keyword." `_master.md` ends with "Ask Mauro: do you want to adjust the keyword or the P.S. offer?"

The buyer of a $500 self-serve product has no Mauro to ask. Every instruction that says "ask Mauro" is a dead end for the exact person the product is for. I had to guess all 9 input-form answers myself. That worked, but the docs never tell a solo builder *how* to decide, only to go ask a person who isn't there.

**This is the #1 thing to fix before selling.** Page 1 (Start Here) has to replace every "ask Mauro" with a decision the buyer can make on their own.

---

## Can a customer follow this alone? Verdict

**Partly.** A competent operator can produce a real magnet from these docs, I did. But they'll hit ~16 forks where the docs either contradict each other or assume Mauro is present, and they'll guess. Some guesses are cheap (brand color). Two are expensive and will produce inconsistent products across buyers:

1. **The two build structures don't agree.** `prompt-swipe-file.md` wants grouped prompt pages with a worked example per group. `notion-delivery-build.md` forces 5 fixed subpages with all prompts dumped in one code block. A buyer following the subtype builds one shape; a buyer following the delivery prompt builds a different shape. Both are "correct" per the docs.
2. **The $100 bar's own rule is broken by the canonical structure.** The bar says a magnet is "a thing you fill in, not a thing you read," and "the last two pages are where the $100 lives." The 5 fixed subpages have no fill-in page, and the last page is a sales CTA. The offer plan already knows this (that's what the missing scoring sheet, page 5, is for), but the delivery prompt as written will never produce it.

Fix those two plus the Start Here page and this is sellable.

---

## TIME LOG

Rough wall-clock, first time through, as a human builder would spend it.

| Stage | Time | Note |
|---|---|---|
| Read all docs (3 skill files + 3 brand files + shareable + offer + brief) | ~55 min | ~2,600 lines. Unavoidable first time. A buyer won't read the internal brand files; they get the shareable version only. |
| Pick topic + gather source material | ~15 min | Easy once you find `research/transcripts/`. |
| Answer the 9 Input Form questions alone (the guessing) | ~20 min | This is where you'd normally stop and message Mauro. |
| Write the 10 prompts | ~40 min | The actual work. Grounding them in the transcript took the time. |
| Run the chain / write the worked example | ~30 min | |
| Reconcile the two structures + write all 5 subpages of copy | ~35 min | Slowed by gap #1 (which structure wins). |
| Write the 12 in-asset image/HTML prompt blocks | ~30 min | Pure invention, no template to follow. |
| Delivery kit (X post, LinkedIn post, DM, LeadShark, cover) | ~25 min | Templates in `_master.md` made this fast. |
| Build it live in Notion | **not done** | No Notion account/credentials in this environment, and account creation is off-limits to me. Estimated ~35 min for a human with the Chrome extension connected. |
| Write this build log | ~30 min | |
| **Total (excluding the Notion build)** | **~4.5 hrs** | First-time, from docs, alone. |

**On the "about 15 minutes plus a VA" claim:** that number is only true for *running the finished prompts to produce a week of content* (that part really is ~15 min once the transcript is in hand). **Building the magnet asset itself the first time from these docs is 4-5 hours, not 15 minutes.** The docs never separate "time to run the tool" from "time to build the tool," and a buyer will feel misled if they expect a finished magnet in 15 minutes. Recommend the offer copy say: "~15 minutes per week to produce content, once the magnet is built" and set a separate, honest expectation for the one-time build.

---

## GAP LOG

One line per moment I was unsure. Format: `[file, section] — what I couldn't tell — what I guessed`.

1. `[notion-delivery-build.md, template prompt] vs [prompt-swipe-file.md, Body structure]` — the delivery prompt forces 5 fixed subpages with ALL prompts in one code block on "The Asset," but the subtype wants 5 grouped prompt pairs each with its own worked example. Can't satisfy both. — Followed the delivery prompt (it's the canonical build), kept the group labels as headers *inside* the single code block, and put one combined worked example on Subpage 4. The subtype's grouping is flattened.

2. `[_master.md, In-asset prompt blocks] vs [notion-delivery-build.md, template]` — `_master` says EVERY page ships two prompt blocks (page image + HTML style), but the delivery template has no slot for them and never mentions them. Unclear if prompt-swipe magnets use them at all. — Added both blocks to all 6 pages anyway (best reading of "every page"). Wrote all 12 from scratch.

3. `[_master.md, In-asset prompt blocks / the brief]` — every example prompt block ends in `...`; there's no guidance on what a page image prompt or HTML style prompt should actually say. — Wrote my own for all 6 pages (kept below, this is the product's page 3).

4. `[notion-delivery-build.md, rule 4] + [_master.md, Token resolution]` — `{{calendly_url}}` has no value and no booking link exists. — Left the token visible, flagged it as a blocker in-page, kept the DM "reply yes" offer as the working CTA. (Known problem, not solved.)

5. `[notion-delivery-build.md, rule 1] + [_master.md, Cover fallback]` — `[BRAND COLOR]` is unfilled. — Picked `#5B4BE1` (electric indigo), used it on every page and the cover. Pure guess. (Known problem.)

6. `[notion-delivery-build.md, CRITICAL STRUCTURE RULE]` — hardcoded "FIVE subpages," but the shareable spec says 5-7. — Went with 5 (the build prompt is the thing you actually paste, so it wins). Saying which: **5 subpages.** (Known problem.)

7. `[_master.md, THE $100 BAR] vs [notion-delivery-build.md, subpage 5]` — the bar says the last two pages are the fill-in pages where the $100 lives, but the fixed structure makes the LAST page a sales CTA ("Want a Free Breakdown?") and has no fill-in page anywhere. — Judged the paste-ready prompts clear the bar on their own (they're #1 on the bar's own list). Did not add a scoring page because the template has no slot for one. This is the exact gap the offer's missing "page 5 scoring sheet" is meant to fill.

8. `[prompt-swipe-file.md, Input Form]` — "get these from Mauro" / "ask before drafting, don't guess on tool name or keyword." The test forbids asking, and so does self-serve reality. — Guessed all 9: tool=Claude, use case=one video to a week of content, format=10 prompts (5×2), grouping=Extract/Angle/LinkedIn/X/Finish, worked examples=yes, companion file=the 10-prompt block, reader tier=established agency owner, keyword=ENGINE, trend signal=none forced. See headline finding.

9. `[prompt-swipe-file.md, Input Form #3]` — "Don't default, ask which pattern fits" (5×2, 10 flat, or 5×1). Can't ask. — Chose 10 prompts (5×2) because the topic spans multiple output formats, which is the case the doc pairs with that pattern.

10. `[_master.md, Title Engineering formula] vs [prompt-swipe-file.md, Title format]` — `_master`'s formula requires a number or year; the subtype's Pattern A (`[Tool][Use Case] for [Outcome]`) has neither. The two title rules disagree. — Made the shipped title number-led ("10 Prompts That Turn One Video Into a Week of Content"), which satisfies `_master` AND matches the winning example in the shareable doc ("10 Prompts for Native Ad Copy"). Kept the Pattern-A version as a runner-up option.

11. `[_master.md, Cover Image Spec — Default]` — the default cover is a screenshot of the Notion home page, which doesn't exist until AFTER you build and publish. Chicken-and-egg, and it can't be produced before the page is live. — Wrote the fallback designed-card HTML spec as the shippable cover, and noted the screenshot as the swap-in once the page exists.

12. `[notion-delivery-build.md, After building #1] vs [offer plan, "What it becomes"]` — the delivery doc says "Publish to web, copy the public URL." The offer doc says buyers "hit Duplicate." Those are two different Notion share mechanics for two different jobs. — For a magnet *delivery page*, publish-to-web is right. For the $500 *product*, it's a Duplicate link. Flagged so they don't get conflated in Start Here.

13. `[_master.md, Asset Build Constraints]` — the whole build assumes the Claude Chrome extension with Notion connected. `_master.md:46` admits no production SOP exists. A buyer may have neither the extension nor a Notion account. — Wrote the delivery prompt so it works via the extension OR a manual paste into Notion. This same dependency is why I (headless, no Notion login) couldn't produce a live link.

14. `[prompt-swipe-file.md, Rules "Grounded in real work" + Worked examples "mandatory"]` — prompts must reflect "how the live engine actually uses the tool," and worked examples must be "real," but a buyer doesn't have Mauro's real prompts or outputs. — Built the prompts from the transcript + the skill logic, and the worked example from the real transcript. A buyer swaps in their own video. The docs should say that explicitly.

15. `[_master.md, After Producing All Outputs]` — "Ask Mauro: adjust keyword or P.S. offer?" Again assumes Mauro. — Left the defaults (keyword ENGINE, teardown P.S.). A solo buyer needs a rule for choosing a keyword, not a person to ask.

16. `[CLAUDE.md, Operating Rules] vs [offer plan, Build order]` — CLAUDE.md says "lead magnets are not saved to the repo," but the offer plan says this run becomes product page 4 and the build log lives in `content/qa/`. — Saved the magnet to `content/qa/` as QA evidence (not a shipped magnet). Flagging the tension so it's a conscious call, not an accident.

17. `[prompt-swipe-file.md, Cover — "file icon + file name + file size"]` — the cover is supposed to show a companion file's name and size, but this magnet's "file" is the prompt block inside Notion, there's no downloadable file. — Labeled the block "10-prompt-content-engine" on the cover and left size as a placeholder. Minor, but the doc assumes a downloadable file that this subtype doesn't always have.

18. `[_master.md, Deliverables #7 Landing Page] vs [the brief, Known problems]` — `_master` lists a Kit landing page as a required deliverable for every magnet, but the brief says "There is no landing page. The DM links straight to the Notion page for now." — Skipped the LP per the brief, pointed the DM link straight at the Notion page. Noting that the deliverables list and the current reality disagree, a buyer reading `_master` will expect to build an LP that the system says to skip.

---

## EVERY PROMPT I HAD TO INVENT

Two categories. Both are "page 3 of the product" material.

### A. The 12 in-asset prompt blocks (page image + HTML style, one pair per page)

No template existed, every example ended in `...`. These are written out in full inside each subpage of [magnet-youtube-to-week-of-content.md](magnet-youtube-to-week-of-content.md). Summary of what I wrote, so they're inventoried in one place:

| Page | Page image prompt (style) | HTML style prompt |
|---|---|---|
| Parent | Real screenshot of the finished parent page (doubles as cover) | Dark hero block, indigo band, 5 subpage pills |
| Subpage 1 Start Here | Doodle: one film reel → 5 doc icons (trickle-down) | 3-step checklist card + weekly-run list |
| Subpage 2 The Asset | Real screenshot of Prompt 4 running in Claude | 5-step progress bar of the groups |
| Subpage 3 What's Inside | Worked example: filled Mon-Fri content calendar | 6-item checklist, dark card |
| Subpage 4 Worked Example | Real screenshot: transcript → finished post, side by side | Mon-Fri schedule table as centerpiece |
| Subpage 5 Free Breakdown | Doodle: two speech bubbles + funnel/magnifier | Centered CTA card, indigo border |

**A rule I had to invent because the docs don't state it:** on the page whose whole job is the prompts (Subpage 2), a "real example screenshot" image would just restate the text, which `_master` bans. So I pointed that page's image at *Prompt 4's live output* (the editor saying no) rather than at the prompt list itself. The docs never address what the image should be on a page that IS the asset. Recommend adding that rule.

### B. The 10 content prompts themselves

The subtype gives structure and one-line purposes, not the actual prompt text. I wrote all 10 (SETUP ONCE + Groups 1-5). Full text is in Subpage 2 of the magnet file. Inventory:

1. Pull the beats (extract) · 2. Pull the verbatim lines (voice) · 3. Turn beats into angles · **4. Kill the weak ones (the prompt that tells you no)** · 5. Write the LinkedIn post · 6. LinkedIn carousel outline · 7. Write the X thread · 8. Five standalone X posts · 9. De-AI voice pass · 10. Map the week Mon-Fri.

Prompt 4 is the one the $100 bar specifically requires ("including at least one that tells them no").

---

## PLACEHOLDERS LEFT IN THE ASSET (for Mauro to fill)

- `{{calendly_url}}` — no booking link exists. Left visible, flagged as blocker. (gap #4)
- Brand color `#5B4BE1` — my guess, needs Mauro's real pick. (gap #5)
- LinkedIn full name resolved to "Mauro Pelle" in the LinkedIn post — verify it matches the profile exactly so it links.
- Cover image — fallback designed-card spec written; swap to the real Notion screenshot once the page is live and published.
- No live Notion link produced (no account/credentials available to me). The magnet is fully paste-ready in the companion file; a human with the Chrome extension + Notion runs the delivery prompt below to create it.

---

## THE FILLED-IN DELIVERY PROMPT (paste this into Claude + Chrome extension, Notion connected)

This is `notion-delivery-build.md`'s template with every token resolved from this run, ready to paste. Content bodies come from the companion magnet file.

```
You are building a lead-magnet DELIVERY PAGE in Notion using the Notion integration.

CRITICAL STRUCTURE RULE: Do NOT put all content on one page. Build ONE parent
page, then create FIVE SEPARATE CHILD SUBPAGES nested inside it. Each section is
its own nested child page, not a heading/toggle/divider on the parent.

FORMATTING: Parent cover = solid #5B4BE1. Subpage titles plain text, no emojis.
Authority line at the very top of the parent. Booking CTA at the bottom.
End with "Created by @maurojpelle".

PARENT PAGE
Cover: solid #5B4BE1.
Top line (authority): "Built by Mauro, who runs this exact content engine daily for a real B2B agency."
Title: 10 Prompts That Turn One Video Into a Week of Content
Subtitle: 10 prompts I use to turn one YouTube video into a week of LinkedIn and X posts, from the engine I run daily for a real B2B agency.
Intro: [intro paragraph from magnet file]
Bottom: "Want this installed in your agency? Book a call: {{calendly_url}}" [PENDING] and "Created by @maurojpelle".

SUBPAGE 1 — "Start Here: How to Use"      [body from magnet file]
SUBPAGE 2 — "The Asset (copy this)"        [10-prompt code block from magnet file]
SUBPAGE 3 — "What's Inside"                [body from magnet file]
SUBPAGE 4 — "Worked Example"               [body from magnet file]
SUBPAGE 5 — "Want a Free Breakdown?"       [body from magnet file]

FINAL CHECK: parent page has exactly 5 nested subpages, #5B4BE1 cover, authority
line at top, booking CTA + @maurojpelle credit at bottom, no emojis in titles.
```

---

## RECOMMENDATIONS (what to fix before charging $500)

Ranked by how much each hurts a solo buyer.

1. **Rewrite the Input Form for self-serve.** Replace every "ask Mauro" with a decision rule the buyer makes alone. This is the Start Here page's main job (gaps #8, #9, #15).
2. **Reconcile the two build structures.** Decide whether the prompt-swipe subtype uses grouped pages or the 5 fixed subpages, and make the two files say the same thing (gap #1).
3. **Ship the scoring sheet (product page 5).** It's what makes the magnet clear its own $100 "thing you fill in" bar. Right now the canonical structure can't produce it (gap #7).
4. **Separate "time to run" from "time to build" in the offer copy.** ~15 min is the run; the first build is hours (time log).
5. **Add a rule for the in-asset image blocks:** whether prompt-swipe magnets use them, and what the image should be on a page that IS the asset (gaps #2, #3, and the invented rule in section A).
6. **Fix the small contradictions:** landing page required vs "no LP yet" (gap #18), publish-to-web vs Duplicate link (gap #12), title formula number/year vs Pattern A (gap #10), "not saved to repo" vs "becomes page 4" (gap #16).
7. **Fill the placeholders once:** brand color and booking link. They block nothing conceptually but every buyer hits them (gaps #4, #5).
