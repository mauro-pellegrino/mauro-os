# Long-Form Subtype: Infographic / HTML Long-Form

**Version:** 2.0
**Created:** 2026-05-26
**Updated:** 2026-07-14 (retargeted to Mauro's own brand, @maurojpelle)
**Loaded with:** `_master.md` (always load both together)
**CTA mechanic:** Depends on pattern variant (no CTA / soft consultative / thread funnel)
**Funnel:** Cross-stage (TOF through MOF)

---

## What This Subtype Is

A long-form post built around **2-3 images of an HTML infographic** that Claude generates from text content. The infographic is screenshot-rendered (or exported as images) and posted to X / LinkedIn. The infographic is the deliverable. The caption frames it.

Subtype identity: Claude-generated visual content, image-led, bookmark-friendly. Ships in two timing modes (same format, different deployment):

1. **Standalone post** — primary post, image-led, caption framed as standalone teaching
2. **Quote-tweet companion** — posted as a quote tweet of a recent article or video, 6 hours after the parent post, as a second-wave amplifier

Same format, same skill output, different scheduling.

---

## Production Workflow (Critical Context)

Different from other long-form subtypes because the asset is **HTML-generated and rendered to PDF + PNGs**.

**Canonical visual production guide:** `skills/content/visual-docs/mauro-visual-doc-system.md`. That file is the source of truth for: page dimensions (1080×1080 square, 1080×1350 portrait, 1080×1620 long), the doc palette, typography (Inter + JetBrains Mono), recurring visual blocks (table-3, insight-box, math-bar, timeline, formats-grid, hook-pattern-grid, cta-block), and the per-doc workflow.

**Render utility:** `skills/content/visual-docs/render_one.py` (lives in the repo). Takes an HTML file path + dimension flag, outputs PDF + per-page PNGs at exact canvas dimensions. Requires `playwright`, `pypdfium2`, `Pillow`.

```
python3 skills/content/visual-docs/render_one.py path/to/deck.html portrait    # 1080x1350 default
python3 skills/content/visual-docs/render_one.py path/to/deck.html square      # 1080x1080
python3 skills/content/visual-docs/render_one.py path/to/deck.html long        # 1080x1620
python3 skills/content/visual-docs/render_one.py path/to/deck.html board       # long scroll breakdown
```

**This file** (`infographic-html-long-form.md`) is the **post wrapper guide**: how the HTML doc gets framed in the X / LinkedIn caption, which pattern variant the post is, what CTA mechanic fires. It assumes the doc is built per `mauro-visual-doc-system.md` standards.

Workflow per post:
1. Build the HTML doc following `mauro-visual-doc-system.md`
2. Render to PDF + PNGs via the render script
3. Write the post caption per this file's variant + length targets
4. Attach 2-3 PNG pages to the X / LinkedIn post
5. Optionally use PDF for LinkedIn document carousel post

**Scope:** all output is for @maurojpelle. [CALIBRATE: Mauro's own visual palette is not locked yet. The doc-guide palette is the current default; revisit when he defines his brand look.]

---

## Pattern Variants (Inside This Format)

The infographic format hosts multiple content patterns. Pick one per post.

### Variant A: Framework Breakdown
- **Anchor:** a teaching framework worth showing visually
- **Infographic content:** 2-3 panels showing the framework's components (e.g., "The Content Engine: Capture → Produce → Measure")
- **Caption hook:** "Here's how I [outcome] for [tier-specific audience]" or "The [N-step] system that [outcome]"
- **CTA:** No CTA. Framework infographic is the deliverable.

### Variant B: Before / After (single rendered image)
- **Anchor:** a visual transformation
- **Infographic content:** 2 panels side-by-side OR stacked top/bottom, "BEFORE" and "AFTER" labeled, with an anonymized workflow or output comparison
- **Caption hook:** "[Time period] of testing & [real invested effort/number] later: here's what changed"
- **CTA:** No CTA OR thread funnel if there's step-by-step underneath

### Variant C: Process Flow
- **Anchor:** a workflow that benefits from being visualized step-by-step
- **Infographic content:** 2-3 panels showing the flow (e.g., "Step 1: [action] → Step 2: [action] → Step 3: [result]")
- **Caption hook:** "Here's the exact [N-step] process I use for [outcome]"
- **CTA:** Soft consultative OR tier-gated DM

### Variant D: Data Visualization
- **Anchor:** a striking number or pattern from real work
- **Infographic content:** 2-3 panels with charts, comparison tables, or KPI breakdowns
- **Caption hook:** number-led, e.g. "After [N] months of tracking every post against booked calls, here's the pattern" (real numbers only, signed off)
- **CTA:** Soft consultative

### Variant E: Tactical Step-by-Step
- **Anchor:** a workflow with exact prompts / settings / tool calls worth visualizing
- **Infographic content:** 2-3 panels with code blocks, prompt text, tool screenshots embedded
- **Caption hook:** "The exact prompts I use to [outcome]"
- **CTA:** Tier-gated DM OR thread funnel

### Variant F: Quote / Manifesto Card
- **Anchor:** a sharp operator stance worth memorializing visually (pull from the 15 beliefs in `brand/business-context-answers.md`)
- **Infographic content:** 1-2 panels with the quote / stance in large type
- **Caption hook:** pattern-interrupt counter-claim
- **CTA:** Soft consultative OR no CTA
- **Use when:** the stance benefits from being shareable as an image

---

## Input Form

Before drafting, get these from Mauro:

1. **Topic** — what the infographic teaches / shows
2. **Pattern variant** — A through F from above
3. **Deployment mode** — standalone OR quote-tweet companion
   - If quote-tweet companion: which parent post (article URL or video post URL) + scheduled time gap (default 6 hours)
4. **Content source** — a logged win, a transcript from `research/transcripts/maurojpelle/`, a session note from `brand/sessions/`, or fresh thinking
5. **Visual style preferences** — default to the `mauro-visual-doc-system.md` system until Mauro locks his own palette
6. **Anonymization scope** — what's visible vs blurred in any data panels
7. **CTA decision** matched to variant default

---

## Asset Structure

### Skill output components

1. **HTML for the infographic** (2-3 page-equivalents of styled content)
2. **Caption / post copy** (X version + LinkedIn version if cross-posting)
3. **Quote-tweet target URL** (if applicable)
4. **Scheduling note** (parent post + 6hr gap if quote-tweet companion)

### HTML structure template

```html
<!-- Panel 1 -->
<div class="panel" style="background: #F5D679; padding: 60px; color: #24243C;">
  <h1>[Title]</h1>
  <p>[Subtitle]</p>
</div>

<!-- Panel 2 -->
<div class="panel" style="background: #24243C; padding: 60px; color: white;">
  <h2>[Section header]</h2>
  <ul>
    <li>[Point 1]</li>
    <li>[Point 2]</li>
    <li>[Point 3]</li>
  </ul>
</div>

<!-- Panel 3 -->
<div class="panel" style="background: #24243C; padding: 60px; color: white;">
  <h2>[Conclusion / Result]</h2>
  <p>[Closing line]</p>
  <small>@maurojpelle</small>
</div>
```

Aspect ratio per panel: 1080x1080 square OR 1080x1350 portrait. Generates clean 2-3 image carousel on X / LinkedIn.

### Caption length targets per variant

| Variant | Words | Lines |
|---|---|---|
| A (framework breakdown) | 40-80 | 4-6 |
| B (before / after) | 50-90 | 5-7 |
| C (process flow) | 40-70 | 4-5 |
| D (data viz) | 60-100 | 5-7 |
| E (tactical step-by-step) | 80-140 | 6-10 |
| F (quote / manifesto card) | 30-60 | 3-4 |

---

## Media Spec (Infographic Image Output)

### Format
- 2-3 images per post (X allows up to 4, LinkedIn similar)
- Square 1080x1080 or portrait 1080x1350 per panel
- High contrast, legible at thumbnail scale (test on mobile)

### Style anchors
- Follow the `mauro-visual-doc-system.md` palette and type system
- Title in large type on the first panel; the first panel is the thumbnail
- `@maurojpelle` credit line on the last panel

### Anonymization
- No identifiable client data in any panel
- Real numbers are OK if aggregated or tier-anonymized, and signed off by Mauro
- Public (non-client) names: OK to use when they're positioning examples, not client work

### Quote-tweet companion specifics
- Same image format as standalone
- Caption tone: shorter, more amplification-flavored (e.g., "Pulled the key insight from yesterday's article into 3 panels. Save this one.")
- Posted as a quote tweet of the parent post URL, not a fresh standalone
- Default delay: 6 hours after parent post (per Mauro's workflow)

---

## CTA Patterns Per Variant

| Variant | CTA mechanic |
|---|---|
| A (framework breakdown) | No CTA. The framework IS the value. |
| B (before / after) | No CTA OR thread funnel if step-by-step thread underneath |
| C (process flow) | Soft consultative OR tier-gated DM (if the process is differentiated enough) |
| D (data viz) | Soft consultative ("If you want this running for your agency, link in bio.") |
| E (tactical step-by-step) | Tier-gated DM ("If you're running an agency at $[X]k+/mo, DM me '[keyword]' for the playbook") OR thread funnel |
| F (quote / manifesto card) | Soft consultative OR no CTA |

**Never use on this subtype:**
- Autodm keyword (lead-magnet territory)
- Multiple stacked CTAs
- "Save this and reply with what you'd add" (reply-bait, performs poorly)

---

## Post Hook Formulas

Inherits universal long-form hooks from `_master.md`. Variant-specific hooks (fill with real numbers or bracketed placeholders only):

| Hook formula | Variant | Example shape |
|---|---|---|
| "Here's how I [outcome] for [tier audience]" | A | "Here's how I structure the weekly content loop for an agency doing $[X]k/mo" |
| "[Time] of testing & [effort] later: [what changed]" | B | "[N] months of testing later: I rebuilt the whole posting system" |
| "Here's the exact [N-step] process I use" | C | "Here's the exact 5-step process I use to turn one call into a week of content" |
| "After [X], here's the pattern" | D | "After [N] months tracking posts against booked calls, here's the only metric that mattered" |
| "The exact prompts I use to [outcome]" | E | "The exact 3-prompt sequence I use to write hooks from client transcripts" |
| "[Sharp stance line]" (stance becomes the image headline) | F | "The best content doesn't look like content" (rendered in large type) |

### Quote-tweet companion variant on hooks

When the post is a quote-tweet of a parent article or video, the hook can reference the parent:
- "The key insight from yesterday's article in 3 panels"
- "Yesterday's video, broken down visually"
- "Saving this from yesterday's thread"

Lower friction caption since the value is in the visual.

---

## Output Checklist

Before scheduling, confirm:

- [ ] Variant chosen (A through F)
- [ ] Deployment mode confirmed (standalone OR quote-tweet companion)
- [ ] If quote-tweet companion: parent post URL captured + 6hr scheduling note
- [ ] HTML for the infographic produced (2-3 panels)
- [ ] Style matches `mauro-visual-doc-system.md` (palette, type, credit line)
- [ ] Each panel legible at thumbnail scale
- [ ] No identifiable client data in any panel
- [ ] X caption follows `_master.md` X post structure + variant length target
- [ ] LinkedIn caption (if cross-posting) adapts per `_master.md` LinkedIn template
- [ ] CTA matches variant default (or explicit override)
- [ ] Numbers verified (real and signed off, or bracketed placeholders)
- [ ] No em dashes, no "It's not X, it's Y", no "Most brands" openers
- [ ] Voice.md pre-publish checklist passed
- [ ] If standalone, post is on the calendar; if quote-tweet companion, parent post is shipped first

---

## Anti-Patterns (Specific to This Subtype)

- Marketing-designed infographic that doesn't look like a real artifact. Doc-screenshot mechanics work because the doc reads as real work product. Infographics that read as agency-marketing-collateral underperform.
- Too many panels (4+). 2-3 is the sweet spot. Past 3, attention drops in-feed.
- Panel 1 with no contrast or hook. Panel 1 is the thumbnail. If it doesn't stop the scroll, the rest doesn't get seen.
- Identical visual style as the lead magnet cover images. Lead magnet covers are about ASKING (autodm CTA). Infographics are about GIVING (asset in-feed). Different visual rhythm.
- Text-heavy panels (>40 words per panel). Infographic should be readable in 3-5 seconds per panel.
- Quote-tweet companion without 6hr delay. Posting the companion too close to the parent dilutes both posts in the algorithm.
- Autodm trigger on this subtype. If you want autodm, build it as a lead magnet, not a long-form infographic.

---

## Cross-Reference

- **Visual system**: `skills/content/visual-docs/mauro-visual-doc-system.md` (palette, typography, blocks, render workflow)
- **Variant B (before / after)**: renders as a single combined HTML before/after image (carousels are killed per `_master.md`)
- **Variant E (tactical step-by-step)**: the compressed visual version of a playbook article; pair with `skills/content/x-article-creator.md` when the same content ships as an article
- **Variant F (quote / manifesto)**: pull the strongest single line from a stance piece or the 15 beliefs into a shareable image
- **HTML build constraint**: Claude Chrome extension generates HTML, Mauro screenshots / exports to images, attaches to post. See `skills/lead-gen/lead-magnet/_master.md` Asset Build Constraints section for the build environment notes.
