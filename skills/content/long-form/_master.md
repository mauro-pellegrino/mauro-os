# Long-Form Skill: Master File

**Version:** 1.0
**Created:** 2026-05-26
**Replaces:** None (new skill)
**Status:** Shared shell across all long-form subtypes. Always load this file together with the relevant subtype file.

---

## What This Skill Is

Long-form posts on X and LinkedIn that combine **text plus media** (video, image, screenshot, dashboard, before/after, infographic). Mauro's working definition: "long form" doesn't mean long text. It means a post with media that's substantial enough to drive bookmarks, profile visits, and DMs without an autodm trigger.

This is **distinct from**:
- **Lead magnets** (`skills/lead-gen/lead-magnet/`): always have an autodm keyword trigger and ship with a downloadable asset
- **Articles** (`skills/content/x-article-creator.md`, `miro-to-article.md`): long-form X articles, deeper than long-form posts
- **Short forms**: pure text or single-image posts under ~150 words

Volume target on Lorenzo's account: **7-8 long forms per week** (per Mauro 2026-05-25).

---

## Subtype Index (by media format)

Subtypes are organized by **production format** (the media lift required), not by content pattern. Pattern variants (transformation flex, result+replicable, operator stance, tactical tutorial, etc.) live as sections INSIDE each format file. This matches Growthub's actual production workflow — the team executes against format-based lifts.

Lead generation on long-forms happens through bookmark + profile visit + DM, not autodm.

| Subtype file | Format spec | Production lift |
|---|---|---|
| `video-long-form.md` | Single video clip (team ad, screen recording, talking head) + caption | Video editing, anonymization. Hosts: Transformation Flex, Result Showcase, Tactical Walkthrough, Operator Stance (talking head), Visual transformation video. |
| `infographic-html-long-form.md` | 2-3 HTML infographic images, Claude-generated. Ships standalone OR as quote-tweet companion 6hr after a parent post (same format, different timing). | Claude HTML build via Chrome extension → screenshot. Hosts: Framework breakdown, Before/After (single rendered image), Process flow, Data viz, Tactical step-by-step, Quote / manifesto card. |
| `doc-screenshot-long-form.md` | Single image of REAL internal work product (Google doc, Notion, Slack, framework chart) | Crop + anonymization. Hosts: 3 hook variants (numbers-anchored, question-led, analogy-led). |
| `case-study-long-form.md` | Named (rare) or anonymized client transformation, post-form, image-led | Wins-log cross-ref + anonymization. Hosts: Testimonial arc, Manifesto positioning, Comeback narrative, Aggregate-proof. |

**Killed formats (no longer used):**
- Carousel (Growthub stopped doing multi-image carousels per Mauro 2026-05-26). Before/After patterns now ship via `infographic-html-long-form.md` as single rendered combined image.

**More format types may be added** as Mauro identifies them. Leave room for: screen recording without voiceover, single image not in any of these buckets, etc.

When building a long-form post, load `_master.md` + the relevant subtype file.

---

## BOF post coverage (funnel position cross-reference)

BOF is a funnel position, not a format. BOF posts (named-client wins, dashboard flexes, comeback narratives, aggregate-proof) live across multiple format files. Use this table to route from a BOF win in `accounts/lorenzo-x/wins-log.md` to the right subtype file:

| BOF post intent | Format file | Variant |
|---|---|---|
| Number-led result flex with video | `video-long-form.md` | A (time-compression) |
| Number-led result flex, dashboard IS the post (no video) | `doc-screenshot-long-form.md` | A (numbers-anchored) |
| Named-client transformation arc, video-led | `video-long-form.md` | B (named-client arc) |
| Named-client transformation arc, image-led | `case-study-long-form.md` | A (testimonial arc) |
| Manifesto / niche-philosophy positioning | `case-study-long-form.md` | B (manifesto) |
| Comeback / competitive proof narrative | `case-study-long-form.md` | C (comeback) |
| Aggregate-proof multi-client ("I've scaled N brands, generated $X") | `case-study-long-form.md` | D (aggregate-proof) |
| Result Showcase (someone else's viral asset, AI reveal) | `video-long-form.md` | C (result showcase reveal) |

**Rule of thumb when picking:** if there's a video, default to `video-long-form.md`. If the proof is a single image (dashboard, screenshot, testimonial card, anonymized grid), use `doc-screenshot-long-form.md` or `case-study-long-form.md` based on whether the image IS the asset (doc-screenshot) or supports a narrative (case-study).

---

## Required Reading

- **Active account config** (e.g., `accounts/lorenzo-x/account-config.md`). Substitute every `{{token}}` in this skill's output with values from the active account config. If no account is specified, ask which one.
- `brands/growthub/voice.md`: voice rules, hard bans, signature moves, 60-second pre-publish checklist
- `brands/growthub/audience.md`: ICP v2.2 (qualified buyer profile + verbatim pain phrases)
- `accounts/lorenzo-x/wins-log.md`: source of named wins for BOF Transformation Flex variants
- `research/post-studies/README.md`: the running pattern rubric. Reference for any pattern decisions.

---

## Deliverables Per Long-Form Post

Each long-form ships with:

1. The post copy (X version + LinkedIn version if cross-posting)
2. The media (video, screenshot, before/after image, doc image, infographic — see Media Spec below)
3. CTA decision: no CTA / soft consultative / tier-gated DM / thread funnel (determined by subtype)
4. Scheduling notes (which day, which time slot per `accounts/lorenzo-x/weekly-calendar.md`)
5. Wins-log entry update if the post uses a logged win (mark which post used which win)

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
- **Carousel / multi-image**: up to 4 images stacked.

### Anonymization rules (per `feedback_client_naming`)
- Real client names: never visible publicly. Blur logos, redact brand names, abstract URLs, mask product shots.
- Dashboard / Ads Manager screenshots: blur dollar amounts if they reveal client tier, OR blur client name selector. Keep one or the other visible, never both unblurred.
- DM screenshots (for Transformation Flex): blur the sender's profile pic and last name only if the win is from a client who isn't comfortable being named. Default = blur.
- Public references (non-clients, e.g., PetLabCo, MiamiMD): naming allowed per `accounts/lorenzo-x/wins-log.md` "safe references" list.

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

### Hook formulas (proven across long-form patterns)

| Formula | Subtype | Example | Source |
|---|---|---|---|
| "[Time period]. $[X] spent. [N] [outcome]." | BOF Transformation Flex (time-compression variant) | "11 days. $20K+ spent. ~300 website purchases." | post-006 |
| "[Specific number outcome] from this [artifact/system]" | Result + Replicable | "This brand did $170K with our creative" | post-003 var A |
| "[Big number] [outcome] from this ad" | Result + Replicable | "Quarter million in rev and 3k+ sales from this ad" | post-003 var B |
| "[X months] of testing & $[Y] later:" | Visual Before/After | "3 months of testing & $25,000 later:" | post-005 |
| "[Named client] hired us when [low point]. Today [high point]." | BOF Transformation Flex (named-client arc) | "Marin hired us when he had less than 900 followers. Today he is the most powerful name in the paid ads space." | post-004 var A |
| "[Niche philosophy] is all we care about at [brand]." | BOF Transformation Flex (manifesto variant) | "Niche virality is all we care about at Mogul Media" | post-004 var B |

### Rules
- One specific number anchor in the first 2 lines, always
- Possessive operator credit ("our", "we") in the setup line
- No em dashes anywhere (per voice.md hard ban)
- No "It's not X, it's Y" structures
- No "Most brands / Most people" openers (unless followed by a sharp Growthub-specific counter-claim, per voice.md signature moves)

### Word count target
60-150 words. Long-forms lean shorter on X than on LinkedIn.

---

## LinkedIn Post Template

LinkedIn long-forms run longer and use checkmark bullets instead of dashes. Same patterns apply otherwise.

### Structure (6 parts)

```
[Hook line: 1 sentence, often outcome-led or contrarian]

[Setup: 2-3 sentences. Authority anchor + what's happening + operator credit.]

[Optional aside in parens: "(These are the strategies my team & I are currently using)" or similar]

[Body: depends on subtype. Could be a bullet list, a numbered teaching breakdown, or a short paragraph block.]

[MEDIA: subtype-specific visual]

[CTA: depends on subtype. Could be no CTA, soft consultative, or tier-gated DM trigger.]
```

### Authority anchors (from account config)

Use the anchor list in `accounts/lorenzo-x/account-config.md`:
- "$107M+ in managed Meta ad spend"
- "$100M+ on Meta ads"
- "$20M generated for [N] [vertical] brands"
- "7/8-figure clients"

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
- Pattern: "If you're spending $[X]K+/mo on Meta and want [outcome], DM me '[keyword]'. I'll [free deliverable]."
- The qualifier IS the filter. Cheap operators self-eject.

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
- `[MEDIA: Spokesperson ad video, 9:16 vertical, 28 seconds]`
- `[MEDIA: Ads Manager screenshot, blur client name selector, keep spend + purchases visible]`
- `[MEDIA: Side-by-side before/after product page redesign]`
- `[MEDIA: 4-up grid of anonymized creative thumbnails, logos blurred]`
- `[MEDIA: Internal Notion screenshot of the 5-pillar framework page]`

---

## Voice Rules (Critical Reminders)

Full rules in `brands/growthub/voice.md`. Non-negotiables for long-form copy:

1. **No em dashes.** Never.
2. **No "It's not X, it's Y" structures** or any variant.
3. **No "Most brands / Most people" openers** unless followed by a Growthub-specific counter-claim (per voice.md signature moves).
4. **No problem-to-purpose reversals** ("that's the filter doing its job", "that's a feature not a bug").
5. **Numbers over adjectives.** Always cite a specific dollar, count, or time figure.
6. **Possessive operator credit** ("our", "we") in the setup. Theory-mode language ("brands should") underperforms operator-mode language ("we shipped").
7. **Branded effect closers** are allowed when applicable (e.g., "Stealth Creatives shipped by the team" — Growthub's branded effect, equivalent to Mogul Media's "Effect" frame).

Run every long-form through the 60-second pre-publish checklist at the bottom of voice.md.

---

## After Producing All Outputs

Ask Mauro:

> "Do you want to adjust the CTA mechanic for this post (no CTA / soft consultative / tier-gated DM / thread funnel), or stick with the subtype default?"

Long-form CTA is the highest-leverage tactical decision and worth a conscious choice per post.

---

## External Inspiration (Pattern Watch List)

Per Mauro 2026-05-26, these accounts are reference patterns to study and adapt:

- **@wizofecom (Mubbu, Mogul Media)** — BOF Transformation Flex archetype (post-004 source). Watch for new named-client transformation posts.
- **@0xROAS** — anonymous Meta-ads + AI operator account. Tactical AI workflow drops, prompt walkthroughs. Relevant for: Tactical Tutorial, Doc Screenshot Asset Drop, Operator Stance.
- **@hookrate_** — hook-focused account (examples pending from Mauro). Likely relevant for: Doc Screenshot Asset Drop, Tactical Tutorial when about hooks specifically, Operator Stance.

When patterns from these accounts shift, update the relevant subtype file with new mechanics observed.

---

## File Output Convention

When this skill produces a long-form post, organize the output as:

```
[Subtype + post identifier]
├── X post copy (with [MEDIA: ...] markers)
├── LinkedIn post copy (if cross-posting, with [MEDIA: ...] markers)
├── Media production brief (text description of each [MEDIA: ...] block, ready for Mauro to grab the actual asset)
├── CTA mechanic chosen + rationale
└── Scheduling note (day + slot + any post-volume conflicts on the weekly calendar)
```

If the post uses a logged win from `wins-log.md`, append the win number to the wins-log "Drafted posts using this win" section once shipped.
