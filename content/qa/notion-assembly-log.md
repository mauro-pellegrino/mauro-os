# Notion Assembly Log: The Lead Magnet System ($500 product)

**Run by:** standing in for "Juan," working alone from `docs/juan-notion-assembly-brief.md`.
**Date:** 21 Aug 2026.
**Job:** assemble the six written pages into one duplicable Notion product page. Assembly, not writing.

---

## THE DELIVERABLE

**Duplicate link (send to Mauro, no one else):**
`https://observant-forest-a43.notion.site/The-Lead-Magnet-System-3c36b44bd5d080debdc5c3f235d3201c`

**Publish settings on that link:**

| Setting | State | Why |
|---|---|---|
| Duplicate as template | ON | This is what makes it the product. A buyer opens the link and hits Duplicate to copy it into their own workspace. |
| Search engine indexing | OFF | Keeps a paid product off Google. Reachable only by someone Mauro sends the link to. |

**Editor (private) page:** `https://app.notion.com/p/The-Lead-Magnet-System-3c36b44bd5d080debdc5c3f235d3201c`
Built in Juan Cruz Lago's Notion account (workspace "Espacio de trabajo de Lorenzo Pellegrino").

---

## WHAT GOT BUILT

One parent page, six real nested child pages, in the brief's order.

- **Parent cover:** solid `#4A392C`, uploaded as an image (see contradiction #4 for why an image and not a colour swatch).
- **Top of parent (authority line):** "Built by Mauro, who runs this exact content engine daily for a real B2B agency."
- **Intro:** one paragraph on what it is and how to start.
- **Bottom of parent (credit):** "Created by @maurojpelle."
- **No booking CTA.** `{{calendly_url}}` left out entirely, per brief.

| # | Page | Source | Notes |
|---|---|---|---|
| 1 | Start Here | `brand/lead-magnets/shareable/start-here.md` | Lifted. Voice check below. |
| 2 | The Rules | `brand/lead-magnets/shareable/lead-magnet-system.md` | Lifted. |
| 3 | The Prompts | build log, "EVERY PROMPT I HAD TO INVENT" A + B | The 10 content prompts in one code block, then the in-asset visual-prompt table. |
| 4 | Worked Example | `content/qa/magnet-youtube-to-week-of-content.md` | The finished example magnet shown as sections. |
| 5 | Score Your Own | `brand/lead-magnets/shareable/magnet-scoring-sheet.md` | Made fillable: real checkboxes + blank table cells. |
| 6 | Delivery Kit | `_master.md` (X post, LinkedIn, DM, LeadShark, cover) | Lifted the five template sections. |

Page 5 is genuinely fillable: the 20 checks are real Notion to-do checkboxes, and "Magnet being scored" is a table with empty cells a buyer types into. Not a picture of a checklist.

**Method (for the next build):** the six pages were authored as clean `.md` files and brought in with Notion's Markdown import (`/import` inside the parent page, so they nest as children). The importer preserved headings, tables, code blocks, and `- [ ]` checkboxes. The product `.md` files were NOT committed to the repo (per CLAUDE.md: lead magnets are not saved to the repo). Only this log is.

---

## CONTRADICTIONS FLAGGED, NOT FIXED

Per the brief: the log of contradictions is worth as much as the page.

**1. The source files break the brand's #1 voice rule.** `start-here.md`, `magnet-youtube-to-week-of-content.md`, the build log, and `_master.md` all contain em dashes, which `voice.md` and `CLAUDE.md` hard-ban. 49 em dashes came through into my first import. I stripped every one before the product went live (em dash to comma, period, colon, or parenthesis depending on context). **The product is em-dash clean. The source files still are not.** Worth a pass on the shareable sources so the next builder doesn't reintroduce them.

**2. Dead brand colour in pages 3 and 4.** The brief said lift pages 3 and 4 as they are, but their source files use `#5B4BE1` (the electric indigo the build test guessed), which `brand/colors.md` explicitly marks dead ("do not reuse"). I replaced the indigo styling references with the real palette (`#4A392C`, `#E0A854`, `#F5EFE4`, `#171310`). "Lift as they are" and "the indigo is dead" can't both hold; I kept the substance and swapped the colour.

**3. "Lift pages 3 and 4 as they are" vs internal QA scaffolding.** Those source files carry build-test scaffolding a buyer should never see: `[GUESS]` flags, `[BLOCKER pending]` notes, "delete before shipping" structure notes, `{{calendly_url}}` placeholders, and title-option menus. I read "lift as they are" as "use your build-test content, don't re-derive it," not "paste QA markers into a paid product." I lifted the substance and removed the scaffolding. Flagging because it's an interpretation, not a literal follow.

**4. Notion cannot render the exact brand hex.** Notion's covers and text/callout colours are a fixed preset palette, not custom hex. Two consequences:
   - **Cover:** solved. I generated a solid `#4A392C` PNG and uploaded it as the cover, so the exact brand colour is on the page.
   - **Amber `#E0A854` accent:** NOT applied. No preset matches it, and a wrong-hex orange would break the "amber is the only saturated colour" rule as much as help it. I left the pages clean rather than fake it. If Mauro wants a single accent, the closest Notion offers is an "orange" background on one callout, applied by hand.

**5. Publish-to-web vs Duplicate link (gap log item 12, now resolved).** The build test flagged these as two different mechanics. Building it surfaced the real constraint: **in Notion, the only way to produce a duplicate-into-your-workspace link is Publish to web with "Duplicate as template" turned on.** There is no "Duplicate link" that sits outside web-publish. So "Duplicate link, not publish-to-web" is not a choice Notion offers. Confirmed the call with Mauro before publishing, then published with Duplicate-as-template ON and search indexing OFF. The distinction that survives: a plain publish is a read-only page (magnet delivery); publish + duplicate-toggle is the product. Same menu, one switch apart.

**6. Page 4 overlaps The Prompts.** The Worked Example source is a full 5-page magnet whose page 2 is the same 10 prompts that now live on page 3 (The Prompts). Rather than paste the 10-prompt block twice, page 4's "The Asset" section names them and points to The Prompts page, and shows the run's actual outputs (beats, verbatim lines, the editor's cuts, the LinkedIn post, the mapped week) in full. Faithful to the worked-example job without a 90-line duplicate.

---

## DOES START HERE SOUND LIKE MAURO?

Mostly yes. It is confident, expert-to-expert, argues a clear stance, and (after the em-dash strip) obeys the hard rules. One line reads as AI-punchy staccato rather than how Mauro actually talks, which `voice.md` calls out specifically:

> "They fatigue. Fast."

That two-word fragment is the one spot that sounds like content, not speech. Everything else holds. Mauro's call on whether to keep it for punch or flatten it to "They fatigue fast, and it's worth knowing why." Leaving it as drafted until he says otherwise.

---

## LEFTOVERS CLEANED UP

- Notion auto-created two "Import Log" pages during the two import passes (the first pass had em dashes and was rebuilt). Both moved to trash.
- The first, em-dash version of the parent page and its children: moved to trash.
- Nothing stray left in the workspace root.
