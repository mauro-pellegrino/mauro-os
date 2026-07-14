# Long-Form Skill: Master File

**Version:** 2.0
**Created:** 2026-05-26
**Updated:** 2026-07-14 (retargeted to Mauro's own brand, @maurojpelle)
**Status:** Shared shell across all long-form subtypes. Always load this file together with the relevant subtype file.

---

## What This Skill Is

Long-form posts on X and LinkedIn that combine **text plus media** (video, image, screenshot, dashboard, before/after, infographic). Mauro's working definition: "long form" doesn't mean long text. It means a post with media that's substantial enough to drive bookmarks, profile visits, and DMs without an autodm trigger.

This is **distinct from**:
- **Lead magnets** (`skills/lead-gen/lead-magnet/`): always have an autodm keyword trigger and ship with a downloadable asset
- **Articles** (`skills/content/x-article-creator.md`, `miro-to-article.md`): long-form X articles, deeper than long-form posts
- **Short forms**: pure text or single-image posts under ~150 words

Volume target on @maurojpelle: [CALIBRATE: set a realistic weekly long-form count with Mauro; his available time is roughly an hour a day.]

---

## Subtype Index (by media format)

Subtypes are organized by **production format** (the media lift required), not by content pattern. Pattern variants (transformation flex, result+replicable, operator stance, tactical tutorial, etc.) live as sections INSIDE each format file. This matches the actual production workflow: execution happens against format-based media lifts.

Lead generation on long-forms happens through bookmark + profile visit + DM, not autodm.

| Subtype file | Format spec | Production lift |
|---|---|---|
| `video-long-form.md` | Single video clip (screen recording, talking head, system demo) + caption | Video editing, anonymization. Hosts: Transformation Flex, Result Showcase, Tactical Walkthrough, Operator Stance (talking head). |
| `infographic-html-long-form.md` | 2-3 HTML infographic images, Claude-generated. Ships standalone OR as quote-tweet companion 6hr after a parent post (same format, different timing). | Claude HTML build → render → screenshot. Hosts: Framework breakdown, Before/After (single rendered image), Process flow, Data viz, Tactical step-by-step, Quote / manifesto card. |
| `doc-screenshot-long-form.md` | Single image of REAL internal work product (Google doc, Notion, Slack, framework chart, skill file) | Crop + anonymization. Hosts: 3 hook variants (numbers-anchored, question-led, analogy-led). |
| `case-study-long-form.md` | Named (rare) or anonymized client/system transformation, post-form, image-led | Proof cross-ref + anonymization. Hosts: Testimonial arc, Manifesto positioning, Comeback narrative, Aggregate-proof. |

**Killed formats (no longer used):**
- Carousel (multi-image carousels killed per Mauro 2026-05-26). Before/After patterns now ship via `infographic-html-long-form.md` as single rendered combined image.

**More format types may be added** as Mauro identifies them. Leave room for: screen recording without voiceover, single image not in any of these buckets, etc.

When building a long-form post, load `_master.md` + the relevant subtype file.

---

## BOF post coverage (funnel position cross-reference)

BOF is a funnel position, not a format. BOF posts (named wins, dashboard flexes, comeback narratives, aggregate-proof) live across multiple format files. Use this table to route from a logged win (`brand/social-proof/` — create as results come in) to the right subtype file:

| BOF post intent | Format file | Variant |
|---|---|---|
| Number-led result flex with video | `video-long-form.md` | A (time-compression) |
| Number-led result flex, dashboard IS the post (no video) | `doc-screenshot-long-form.md` | A (numbers-anchored) |
| Named transformation arc, video-led | `video-long-form.md` | B (named arc) |
| Named transformation arc, image-led | `case-study-long-form.md` | A (testimonial arc) |
| Manifesto / lane-philosophy positioning | `case-study-long-form.md` | B (manifesto) |
| Comeback / competitive proof narrative | `case-study-long-form.md` | C (comeback) |
| Aggregate-proof multi-result ("I've built N systems, they produced $X") | `case-study-long-form.md` | D (aggregate-proof) |
| Result Showcase (someone else's viral asset, AI reveal) | `video-long-form.md` | C (result showcase reveal) |

**Rule of thumb when picking:** if there's a video, default to `video-long-form.md`. If the proof is a single image (dashboard, screenshot, testimonial card, anonymized grid), use `doc-screenshot-long-form.md` or `case-study-long-form.md` based on whether the image IS the asset (doc-screenshot) or supports a narrative (case-study).

---

## Required Reading

- `brand/voice.md`: voice rules, hard bans, pre-publish checklist
- `brand/positioning.md`: identity, proof, content pillars
- `brand/audience.md`: ICP (established agency owners) + verbatim pain phrases
- `brand/social-proof/` (create as results come in): the only source of named wins for BOF variants
- All posts are written for @maurojpelle in Mauro's first-person voice.

---

## Deliverables Per Long-Form Post

Each long-form ships with:

1. The post copy (X version + LinkedIn version if cross-posting)
2. The media (video, screenshot, before/after image, doc image, infographic — see Media Spec below)
3. CTA decision: no CTA / soft consultative / tier-gated DM / thread funnel (determined by subtype)
4. Scheduling notes (which day, which time slot)
5. Social-proof log update if the post uses a logged win (mark which post used which win)

**Not used by default:**
- Autodm keyword trigger (lead magnet territory, not long form)
- Promo email (article territory)
- Follow-up DM

---

## Media Spec (Critical)

The media does more work on long-forms than the copy does. Subtypes have their own media specs. Universal rules across all subtypes:

### Format
- **Video**: 9:16 portrait preferred for X feed performance. 1080p minimum. Under 30 seconds for in-feed autoplay.
- **Image**: 1200x675 (16:9) or square 1080x1080. PNG for screenshots, JPG for photos.
- **Multi-image**: up to 4 images stacked.

### Anonymization rules (per `feedback_client_naming`)
- Real client names: never visible publicly. Blur logos, redact names, abstract URLs.
- Dashboard / analytics screenshots: blur dollar amounts if they reveal a client's tier, OR blur the client name selector. Keep one or the other visible, never both unblurred.
- DM screenshots (for Transformation Flex): blur the sender's profile pic and last name unless the person has consented to being named. Default = blur.
- Public references (non-clients): naming allowed. [CALIBRATE: build a safe-references list in `brand/social-proof/` as it comes up.]

### Production reality (Claude Chrome extension constraint)
The Chrome extension output is **text + prompts only** (per the lead magnet `_master.md` Asset Build Constraints section). Media is added manually by Mauro after the build. Skill output should mark media insertion points with `[MEDIA: description of what to insert here]` blocks.

---

## X Post Template

### Structure (5 parts, varies by subtype)

```
[Hook line: 1 sentence, often numbers-led or pattern-interrupt]

[Setup: 1-2 sentences. Operator-possessive credit + specifics.]

[Optional middle: 1-3 lines. Differentiator or arc compression.]

[Optional closer line: branded effect, anti-fluff signal, or follow promise]

[MEDIA: subtype-specific visual]
```

### Hook formulas (proven long-form shapes)

These structures were extracted from studied high-performers. Fill them only with real, verified numbers or bracketed placeholders.

| Formula | Subtype | Example shape |
|---|---|---|
| "[Time period]. $[X] spent/invested. [N] [outcome]." | BOF Transformation Flex (time-compression variant) | "[N] days. $[X] spent. [Y] booked calls." |
| "[Specific number outcome] from this [artifact/system]" | Result + Replicable | "[Result] came from this one system" |
| "[X months] of testing & $[Y] later:" | Visual Before/After | "[N] months of testing & $[Y] later:" |
| "[Named person] started when [low point]. Today [high point]." | BOF Transformation Flex (named arc) | "[Name] started with [low point]. Today [high point]." |
| "[Lane philosophy] is all I care about." | BOF Transformation Flex (manifesto variant) | "[Philosophy line] is all I care about." |

### Rules
- One specific number anchor in the first 2 lines, always. Real or bracketed, never invented.
- Possessive operator credit ("my", "I built") in the setup line
- No em dashes anywhere (per voice.md hard ban)
- No "It's not X, it's Y" structures
- No "Most brands / Most people" openers

### Word count target
60-150 words. Long-forms lean shorter on X than on LinkedIn.

---

## LinkedIn Post Template

LinkedIn long-forms run longer and use checkmark bullets instead of dashes. Same patterns apply otherwise.

### Structure (6 parts)

```
[Hook line: 1 sentence, often outcome-led or contrarian]

[Setup: 2-3 sentences. Authority anchor + what's happening + operator credit.]

[Optional aside in parens: "(This is the exact system I run every week)" or similar]

[Body: depends on subtype. Could be a bullet list, a numbered teaching breakdown, or a short paragraph block.]

[MEDIA: subtype-specific visual]

[CTA: depends on subtype. Could be no CTA, soft consultative, or tier-gated DM trigger.]
```

### Authority anchors

Pull from the proof section of `brand/positioning.md` (his own operational proof: the AI content and acquisition engine he runs daily for a real agency, content tied to booked calls). Any specific public number needs Mauro's sign-off before use. Never borrow anyone else's anchors.

Rotate by post topic, gut call.

### Word count target
140-260 words. LinkedIn long-forms tolerate more setup.

---

## CTA Patterns (Subtype-Determined)

Unlike lead magnets, long-forms have **multiple CTA mechanics**. The subtype file specifies which to use:

### 1. No hard CTA (BOF default)
- Used by: BOF Transformation Flex, BOF Visual Before/After
- Confidence positioning. No "DM me" or "book a call." Optional soft positioning link.
- The post itself filters for high-ticket buyers who DM with their own framing.

### 2. Soft consultative CTA
- Used by: Operator Stance, some Tactical Tutorial variants
- Pattern: "If you want [specific outcome]... let me know. In a quick call I can go over if this fits, or where else to focus. Link in bio."
- Reads as advice, not sales. Filters for self-aware ICPs.

### 3. Tier-gated DM trigger
- Used by: Tactical Tutorial (when adapted as long-form short of full article)
- Pattern: "If you're running an agency at $[X]k+/mo and want [outcome], DM me '[keyword]'. I'll [free deliverable]."
- The qualifier IS the filter. Beginners self-eject.

### 4. Thread funnel
- Used by: BOF Visual Before/After (thread cover post)
- Pattern: "(Before / after image 👇) Keep reading as I walk you through..."
- The thread does the teaching. The cover post earns the click into the thread.

### 5. Reply CTA (lowest commitment)
- Used by: occasional Result+Replicable variants
- Pattern: "Reply '[keyword]' and I'll send over the full breakdown."
- Lower commitment than DM, used when the give-away is light.

The subtype file picks one. Do not stack multiple CTAs in a single post.

---

## Asset Build Constraints

Same as lead-magnet `_master.md`. The Claude Chrome extension output is text + prompts only. Media is added manually by Mauro after the build.

Mark media insertion points as `[MEDIA: description of what to insert here]`. Examples:
- `[MEDIA: Screen recording of the weekly content loop running, 9:16 vertical, 28 seconds]`
- `[MEDIA: Analytics screenshot, blur account selector, keep numbers + date range visible]`
- `[MEDIA: Side-by-side before/after of the content calendar]`
- `[MEDIA: 4-up grid of anonymized post thumbnails]`
- `[MEDIA: Internal Notion screenshot of the weekly loop framework page]`

---

## Voice Rules (Critical Reminders)

Full rules in `brand/voice.md`. Non-negotiables for long-form copy:

1. **No em dashes.** Never.
2. **No "It's not X, it's Y" structures** or any variant.
3. **No "Most brands / Most people" openers.**
4. **No problem-to-purpose reversals** ("that's the filter doing its job", "that's a feature not a bug").
5. **Numbers over adjectives.** Always cite a specific dollar, count, or time figure. Real or bracketed, never invented.
6. **Possessive operator credit** ("my", "I") in the setup. Theory-mode language ("agencies should") underperforms operator-mode language ("I shipped").
7. **Branded effect closers** are allowed when applicable. [CALIBRATE: Mauro has not named his branded effect yet. Propose options; don't invent one silently per post.]

Run every long-form through the pre-publish checklist in voice.md.

---

## After Producing All Outputs

Ask Mauro:

> "Do you want to adjust the CTA mechanic for this post (no CTA / soft consultative / tier-gated DM / thread funnel), or stick with the subtype default?"

Long-form CTA is the highest-leverage tactical decision and worth a conscious choice per post.

---

## External Inspiration (Pattern Watch List)

[MONITORED ACCOUNTS — to be defined for Mauro's lane: AI systems for agency owners. When accounts are picked, log what pattern each is a reference for, and update the relevant subtype file when their mechanics shift.]

---

## File Output Convention

When this skill produces a long-form post, organize the output as:

```
[Subtype + post identifier]
├── X post copy (with [MEDIA: ...] markers)
├── LinkedIn post copy (if cross-posting, with [MEDIA: ...] markers)
├── Media production brief (text description of each [MEDIA: ...] block, ready for Mauro to grab the actual asset)
├── CTA mechanic chosen + rationale
└── Scheduling note (day + slot)
```

If the post uses a logged win, append the post reference to that win's entry in `brand/social-proof/` once shipped.
