# Long-Form Subtype: Infographic / HTML Long-Form

**Version:** 1.0
**Created:** 2026-05-26
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

Different from other long-form subtypes because the asset is **HTML-generated and rendered to PDF + PNGs via the Growthub visual system**.

**Canonical visual production guide:** `skills/content/long-form/linkedin-html-doc-guide.md`. That file is the source of truth for: page dimensions (1080×1080 square, 1080×1350 portrait, 1080×1620 long), Growthub palette (Space Indigo / Jasmine / Shocking Pink / Aquamarine), typography (Inter + JetBrains Mono), recurring visual blocks (table-3, insight-box, math-bar, timeline, formats-grid, hook-pattern-grid, cta-block), and the per-doc workflow.

**Render utility:** `scripts/render_one.py`. Takes an HTML file path + dimension flag, outputs PDF + per-page PNGs at exact canvas dimensions. Requires `playwright`, `pypdfium2`, `Pillow`.

```
python3 scripts/render_one.py path/to/deck.html portrait    # 1080x1350 default
python3 scripts/render_one.py path/to/deck.html square      # 1080x1080
python3 scripts/render_one.py path/to/deck.html long        # 1080x1620
```

**This file** (`infographic-html-long-form.md`) is the **post wrapper guide**: how the HTML doc gets framed in the X / LinkedIn caption, which pattern variant the post is, what CTA mechanic fires. It assumes the doc is built per `linkedin-html-doc-guide.md` standards.

Workflow per post:
1. Build the HTML doc following `linkedin-html-doc-guide.md`
2. Render to PDF + PNGs via `scripts/render_one.py`
3. Write the post caption per this file's variant + length targets
4. Attach 2-3 PNG pages to the X / LinkedIn post
5. Optionally use PDF for LinkedIn document carousel post

**Scope:** Lorenzo / Growthub form only as of 2026-05-27. Mauro-personal variant, additional palette options, and any per-account customization are deferred until a new brand or account onboarding triggers them. When that happens, revisit `linkedin-html-doc-guide.md` for palette / handle / voice deltas.

---

## Pattern Variants (Inside This Format)

The infographic format hosts multiple content patterns. Pick one per post.

### Variant A: Framework Breakdown
- **Anchor:** a teaching framework worth showing visually
- **Infographic content:** 2-3 panels showing the framework's components (e.g., "The 3-Layer Creative Engine: Ideation → Production → Testing")
- **Caption hook:** "Here's how we [outcome] for our [tier-specific clients]" or "The [N-step] system that [outcome]"
- **CTA:** No CTA. Framework infographic is the deliverable.

### Variant B: Before / After (single rendered image)
- **Anchor:** a visual transformation
- **Infographic content:** 2 panels side-by-side OR stacked top/bottom, "BEFORE" and "AFTER" labeled, with anonymized creative or workflow comparison
- **Caption hook:** "[Time period] of testing & $[Y] later: we [verb]ed this for one of our clients"
- **CTA:** No CTA OR thread funnel if there's step-by-step underneath

### Variant C: Process Flow
- **Anchor:** a workflow that benefits from being visualized step-by-step
- **Infographic content:** 2-3 panels showing the flow (e.g., "Step 1: [action] → Step 2: [action] → Step 3: [result]")
- **Caption hook:** "Here's the exact [N-step] process we use for [outcome]"
- **CTA:** Soft consultative OR tier-gated DM

### Variant D: Data Visualization
- **Anchor:** a striking number or pattern from real client work
- **Infographic content:** 2-3 panels with charts, comparison tables, or KPI breakdowns
- **Caption hook:** number-led, e.g. "After $107M+ in managed Meta spend, here's the pattern across our top accounts"
- **CTA:** Soft consultative

### Variant E: Tactical Step-by-Step
- **Anchor:** a workflow with exact prompts / settings / tool calls worth visualizing
- **Infographic content:** 2-3 panels with code blocks, prompt text, tool screenshots embedded
- **Caption hook:** "The exact prompts we use to [outcome]"
- **CTA:** Tier-gated DM OR thread funnel
- **Source pattern:** post-010 article structure compressed into infographic + caption

### Variant F: Quote / Manifesto Card
- **Anchor:** a sharp operator stance worth memorializing visually
- **Infographic content:** 1-2 panels with the quote / stance in large type, sourced or attributed
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
4. **Content source** — wins-log entry, research/post-studies pattern, transcript, or fresh thinking
5. **Visual style preferences** — Growthub brand colors (yellow accent on dark body) is the default per `best-performing-posts.md` cover image spec
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
<div class="panel" style="background: #FFC83D; padding: 60px; color: black;">
  <h1>[Title]</h1>
  <p>[Subtitle]</p>
</div>

<!-- Panel 2 -->
<div class="panel" style="background: #1A1A1A; padding: 60px; color: white;">
  <h2>[Section header]</h2>
  <ul>
    <li>[Point 1]</li>
    <li>[Point 2]</li>
    <li>[Point 3]</li>
  </ul>
</div>

<!-- Panel 3 -->
<div class="panel" style="background: #1A1A1A; padding: 60px; color: white;">
  <h2>[Conclusion / Result]</h2>
  <p>[Closing line]</p>
  <small>Created by Growthub.Agency</small>
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
- High contrast (Growthub yellow header + dark body is the default style)
- Legible at thumbnail scale (test on mobile)

### Style anchors (matching `best-performing-posts.md` cover image spec)
- Yellow band header (Growthub brand yellow)
- Dark body (near-black background, white text)
- Title in large white sans-serif
- "Created by Growthub.Agency" line on the last panel
- Optional: small emoji or icon prefix for bulleted items

### Anonymization
- No identifiable client data in any panel
- Real numbers from wins-log are OK if aggregated or tier-anonymized ("$107M+ managed spend" vs "Brand X spent $200K/mo")
- Public competitor brand names: OK to use per the wins-log "safe references" list

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
| D (data viz) | Soft consultative ("If you want this run for your brand, link in bio.") |
| E (tactical step-by-step) | Tier-gated DM ("If you're spending $50K+/mo on Meta, DM me 'X' for the playbook") OR thread funnel |
| F (quote / manifesto card) | Soft consultative OR no CTA |

**Never use on this subtype:**
- Autodm keyword (lead-magnet territory)
- Multiple stacked CTAs
- "Save this and reply with what you'd add" (reply-bait, performs poorly)

---

## Post Hook Formulas

Inherits universal long-form hooks from `_master.md`. Variant-specific hooks:

| Hook formula | Variant | Example |
|---|---|---|
| "Here's how we [outcome] for our [tier] clients" | A | "Here's how we structure creative testing for our $100K+/mo Meta clients" |
| "[Time] of testing & $[Y] later: we [verb]ed [thing]" | B | "3 months of testing & $25K later: we rebuilt this brand's creative engine" |
| "Here's the exact [N-step] process we use" | C | "Here's the exact 5-step process we use to ship 20+ creative concepts per week" |
| "After $[X] in spend, here's the pattern" | D | "After $107M+ in managed Meta spend, here's the only metric that predicts scale" |
| "The exact prompts we use to [outcome]" | E | "The exact 3-prompt sequence we use to write hooks for cold traffic" |
| "[Sharp stance line]" (stance becomes the image headline) | F | "Hooks are the 80/20 of any ad" (rendered in large type) |

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
- [ ] Style matches `best-performing-posts.md` cover image spec (yellow header, dark body, Growthub.Agency credit)
- [ ] Each panel legible at thumbnail scale
- [ ] No identifiable client data in any panel
- [ ] X caption follows `_master.md` X post structure + variant length target
- [ ] LinkedIn caption (if cross-posting) adapts per `_master.md` LinkedIn template
- [ ] CTA matches variant default (or explicit override)
- [ ] All `{{tokens}}` resolved from `accounts/[active]/account-config.md`
- [ ] Numbers verified against wins-log
- [ ] No em dashes, no "It's not X, it's Y", no "Most brands" openers
- [ ] Voice.md 60-second pre-publish checklist passed
- [ ] If standalone, original post is on the weekly calendar; if quote-tweet companion, parent post is shipped first

---

## Anti-Patterns (Specific to This Subtype)

- Marketing-designed infographic that doesn't look like a real artifact. Per `research/post-studies/post-002`, doc-screenshot mechanics work because the doc reads as real work product. Infographics that read as agency-marketing-collateral underperform.
- Too many panels (4+). 2-3 is the sweet spot. Past 3, attention drops in-feed.
- Panel 1 with no contrast or hook. Panel 1 is the thumbnail. If it doesn't stop the scroll, the rest doesn't get seen.
- Identical visual style as the lead magnet cover images. Lead magnet covers are about ASKING (autodm CTA). Infographics are about GIVING (asset in-feed). Different visual rhythm.
- Text-heavy panels (>40 words per panel). Infographic should be readable in 3-5 seconds per panel.
- Quote-tweet companion without 6hr delay. Posting the companion too close to the parent dilutes both posts in the algorithm.
- Autodm trigger on this subtype. If you want autodm, build it as a lead magnet, not a long-form infographic.

---

## Cross-Reference

- **Visual style anchor**: `brands/growthub/best-performing-posts.md` cover image spec (yellow header, dark body, Growthub.Agency credit)
- **Source pattern for Variant B (before / after)**: `research/post-studies/post-005-visual-before-after-portfolio.md` — Karalić $25K e-com website redesign. Originally carousel-format, now renders as single combined HTML before/after image.
- **Source pattern for Variant E (tactical step-by-step)**: `research/post-studies/post-010-lorenzo-mar12-ai-broll-tutorial.md` — article-form. Infographic version is the compressed visual of the same content.
- **Source pattern for Variant F (quote / manifesto)**: `research/post-studies/post-009-lorenzo-feb11-operator-manifesto.md` — article-form. Quote-card version pulls the strongest single line from the manifesto into a shareable image.
- **HTML build constraint**: Claude Chrome extension generates HTML, Mauro screenshots / exports to images, attaches to post. See `skills/lead-gen/lead-magnet/_master.md` Asset Build Constraints section for the build environment notes.
