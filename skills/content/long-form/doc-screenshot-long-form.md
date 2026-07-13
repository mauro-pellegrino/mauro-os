# Long-Form Subtype: Doc Screenshot Long-Form

**Version:** 1.0
**Created:** 2026-05-26 (consolidated from earlier pattern-based file)
**Loaded with:** `_master.md` (always load both together)
**CTA mechanic:** No CTA (zero-friction consumption, asset is in-feed)
**Funnel:** TOF / MOF cross-stage

---

## What This Subtype Is

A short framing caption paired with **a single image of an internal work product**: Google doc, Notion page, Slack snippet, framework chart, or workspace screenshot. The image IS the value. The reader gets the entire asset in-feed. No DM ask, no link.

Subtype identity: image of REAL work product (not marketing-designed). The "this is the actual doc I use" framing is what makes the mechanic fire. Different from `infographic-html-long-form.md` (which is Claude-generated styled content) because this is an EXISTING internal artifact, not built for the post.

---

## Pattern Variants (3 Hook Modes)

Per `research/post-studies/post-002`, the same image-first format hosts 3 proven hook archetypes:

### Variant A: Numbers-anchored authority flex (MOF-leaning)
- **Hook formula:** "Here's the complete [thing] I use to [outcome] with [average specific metric] for clients"
- **Example:** "Here's the complete checklist that I use to create high-converting sales pages with an average ROI of 15-20% for clients"
- **Tone:** professional, possessive, social-proof-led
- **Best for:** Lorenzo's account (operator-tier MOF positioning)

### Variant B: Question-led peer offer (TOF-leaning)
- **Hook formula:** "Need some [topic] inspiration?"
- **Example:** "Need some new TOF hooks inspiration?"
- **Tone:** casual peer-to-peer, low authority pressure
- **Best for:** broader audience entry, top-of-funnel pull

### Variant C: Analogy-led teaching (TOF-leaning)
- **Hook formula:** "[Vivid memorable analogy]. The same goes for [your topic]."
- **Example:** "You wouldn't crack the same jokes with your grandmother that you'd share with your buddy over drinks. The same goes for your ads."
- **Tone:** teaching, sticky mental image
- **Best for:** when the framework benefits from a metaphor before the reader sees it

Pick one. Don't stack multiple in the same post.

---

## Input Form

Before drafting, get these from Mauro:

1. **The doc / Notion / Slack screenshot itself** — file or URL of the source artifact
2. **Variant** — A / B / C from above
3. **Variant-specific data:**
   - A: specific number / ROI / metric to use as anchor + social proof phrasing
   - B: topic for the question
   - C: the analogy + the bridge to the business point
4. **Doc readability check** — is the doc legible at thumbnail scale? Mobile-readable?
5. **Anonymization scope** — what in the doc needs to be redacted (client names, internal tool names if sensitive, dollar figures tied to specific clients)
6. **Confirm artifact is real** — if it's marketing-designed-to-look-like-a-doc, the mechanic breaks. Mauro confirms this is a real artifact used by the team.

---

## Asset Structure

Two-component post: short framing caption (3-30 words) + one image.

### Variant A caption structure

```
[Caption: "Here's the complete [thing] I use to [outcome] with [metric] for clients"]

[Optional 1 line: brief framing or context]

[MEDIA: Google doc / Notion / framework screenshot, full asset visible]
```

### Variant B caption structure

```
[Caption: question — "Need some [topic] inspiration?"]

[MEDIA: Google doc / Notion / framework screenshot, full asset visible]
```

### Variant C caption structure

```
[Analogy line]

[Bridge line: "The same goes for [your topic]."]

[Optional setup: 1-2 lines extending the bridge]

[MEDIA: Google doc / Notion / framework screenshot, full asset visible]
```

Word count target: under 60 words total across all variants. The image carries the post.

---

## Media Spec (Subtype-Specific)

### What the doc screenshot must look like

- **Real Google doc, Notion page, or framework artifact** — not a Canva graphic designed to look like one
- **Polished but not over-designed** (signals real work product)
- **Sufficient depth** to demonstrate operator-level thinking (20-step checklist, 10+ specific points, not 3 fluffy bullets)
- **Contains specifics** most amateurs don't think about
- **Legible at thumbnail scale** (mobile reader can decide whether to expand)
- **Clean typography** in a system font (not Comic Sans, not display fonts)

### What the doc screenshot must NOT look like

- Marketing graphic with brand colors and logos overlaid
- Lifestyle imagery or stock photos in the background
- "Designed" cover page with a hero header
- Fewer than 10 items in a list (looks thin)
- More than 30 items (looks unmanageable)

### Anonymization

- Client names, brand names: redacted with black bars or blurred
- Internal tool names: usually fine unless they reveal client identity
- Dollar figures: keep aggregate-level ($107M+) visible; redact per-client specifics

### Crop and aspect ratio

- Vertical crop (taller than wide) so the doc reads top-to-bottom in the feed without expansion
- If the asset is wider than tall (e.g., a horizontal framework), split into two stacked images (still 2-image max for this subtype)

---

## CTA Pattern (No CTA)

This subtype uses **No CTA** by design. The full asset is in-feed. No DM ask, no link, no "comment X."

The mechanic: you gave first, asked nothing. Reader thinks "if this is what they give away free, what does the paid version look like?" and clicks the profile.

**Optionally:** if a soft positioning line earns its place, add one line at the bottom: "More frameworks like this on the profile, follow for more." Used sparingly. Most variants work without it.

**Never use on this subtype:**
- Autodm keyword (would defeat the zero-friction mechanic)
- "DM me" or "book a call"
- Calendly link

---

## Output Checklist

Before scheduling, confirm:

- [ ] Variant (A / B / C) chosen and hook formula matches
- [ ] Doc screenshot is a real artifact, not a designed graphic
- [ ] Doc is legible at thumbnail scale (mobile test)
- [ ] Doc has operator-grade depth (10-30 items, not 3 fluffy bullets)
- [ ] Client / brand names redacted per anonymization rules
- [ ] Aggregate anchors preserved ($107M+ etc.)
- [ ] X caption is under 60 words
- [ ] LinkedIn caption (if cross-posting) adapted per `_master.md` LinkedIn template
- [ ] All `{{tokens}}` resolved from `accounts/[active]/account-config.md`
- [ ] No em dashes, no "It's not X, it's Y", no "Most brands" openers
- [ ] No CTA at the bottom (the mechanic depends on no-ask)
- [ ] Voice.md 60-second pre-publish checklist passed

---

## Anti-Patterns (Specific to This Subtype)

- Designing the doc instead of screenshotting a real one. Canva graphics that look like docs break the mechanic. The whole point is that this is REAL work product.
- Hard CTA at the bottom. Kills the give-first signal.
- Doc that's thin on content. If the screenshot doesn't show 10+ items or a real framework structure, the mechanic doesn't fire.
- Doc with too much content. Past 30 items, the screenshot becomes unreadable at feed scale.
- Adding lifestyle imagery or stock photos to the doc. Reads as marketing material, not work product.
- Variant mismatch: numbers-anchored hook paired with an analogy-style framework doc. Each variant has its own hook + asset combo. Don't blend.
- Using this subtype when you actually have a Claude-generated infographic (use `infographic-html-long-form.md` instead). Infographics are GENERATED; doc screenshots are EXTRACTED from real workflow.

---

## Cross-Reference

- **Source pattern study**: `research/post-studies/post-002-doc-screenshot-asset-drop.md`
- **3 hook variations** documented across 3 screenshots in post-studies: post-002-hook-a-sales-checklist.png, post-002-hook-b-tof-hooks.png, post-002-hook-c-generations.png
- **Adjacent variant for AI-flavored content** (relevant for `@stealth_ai`): "Here's the exact prompt I use to audit my client's onboarding emails for [X]" + Notion doc screenshot
- **Distinction from `infographic-html-long-form.md`**: this subtype ships REAL extracted work product. Infographics are Claude-generated styled content. Same image-led format, different production source.
- **Distinction from lead magnets**: this subtype ships the full asset in-feed. Lead magnets gate the asset behind an autodm keyword. Decide which lever you want before drafting.
