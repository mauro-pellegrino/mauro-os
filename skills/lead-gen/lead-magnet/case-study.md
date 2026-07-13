# Lead Magnet Subtype: Case Study

**Version:** 1.0
**Created:** 2026-05-26
**Loaded with:** `_master.md` (always load both together)
**DM noun:** "breakdown"

---

## What This Subtype Is

A written deep-dive on a single anonymized client transformation. The magnet breaks down the **strategy** the team applied to produce a specific result, plus the replicable layer the operator can take and use in their own brand.

Subtype identity: one client, one transformation, full strategic breakdown. Different from `industry-specific.md` (which packages multiple case studies under a vertical theme) and from `youtube-video.md` (which uses a recorded video as the magnet instead of a written breakdown).

If the case study ships as a video → use `youtube-video.md`.
If the case study is one of many examples under a vertical packaging → use `industry-specific.md`.
If the case study is the magnet itself, in written form → use this file.

---

## Critical Input Requirement

**This subtype almost always needs a real case study input from Mauro or the team. The wins-log alone is not enough.**

A single line in `accounts/lorenzo-x/wins-log.md` ("Pet brand scaled from $29K to $750K") gives you the anchor numbers but not the strategy depth. To write a real case study magnet, you need access to:

- A transcript of how the team actually did it (Lorenzo's case study video transcripts in `research/transcripts/lorenzopravata/` are the primary source)
- Or an internal deck, Notion page, or write-up explaining the moves
- Or Mauro / a strategist explaining the play live, captured as notes

**If only the wins-log is available, do not draft. Ask Mauro for the underlying case study input first.** A case study magnet without strategic depth reads as a result-flex, not a real breakdown, and underperforms.

---

## Input Form

Before drafting, get these from Mauro:

1. **The case study source material** (transcript, deck, write-up, video — see Critical Input Requirement above)
2. **The win** (specific numbers and anchors that are verifiable from the source)
3. **The strategy applied** (the framework, approach, or specific moves the team used)
4. **Replicable layer** (what part of the strategy the operator can take and apply themselves)
5. **Anonymization scope** — what can and cannot be public:
   - Client name (almost always internal-only per [[feedback_client_naming]])
   - Industry / vertical (usually okay to name)
   - Specific dollar figures (verify against the source transcript)
   - Specific timeframes (verify)
   - Public references to competitor brands or non-clients (often okay, see wins-log entries for what's named in source vs what's been published)
6. **Format** the magnet ships in (Notion 5-pager, Gamma deck, Canva carousel, LinkedIn doc)
7. **Cover image** elements (results dashboard screenshot? anonymized creative grid? clean text-only title?)
8. **Trigger keyword** (3-7 chars, ALL CAPS — usually maps to the vertical or the strategy name)
9. **Trend signal** (is this case study hot right now? supplement is a hot vertical, pet is steady, b2b SaaS is deferred per the wins-log)

---

## Framing Variants (Pick One)

Case study posts work in three different framings. Pick based on the source data:

### Variant A: Numbers-led
Headline anchored on a single dollar transformation.
- "I took my pet brand client from $29k to $750k/month."
- "Scaling a skincare brand to $12M in 10 months."

Best when there's a single hero number and the source transcript supports it cleanly.

### Variant B: Arc-led (3-phase)
Headline anchored on the journey, not the endpoint. The strategic shift is the story.
- Phase 1: scaled fast to a number
- Phase 2: hit a ceiling, plateaued
- Phase 3: changed strategy, broke through

Best when the source transcript explicitly walks through phases (the pet brand $29K → $750K transcript does this). Operators relate to plateau-and-break-through more than to one-shot rocket-ship arcs.

### Variant C: Aggregate-proof
Headline anchored on multiple clients in the same vertical, not one.
- "I've scaled over 10 pet brands and generated $20M for them."
- "$17M+ in supplement Meta spend managed across clients last year."

Best when no single client can be named or verified deeply, but the aggregate proof is real. Tends to overlap with `industry-specific.md` — if the magnet is mostly about the vertical, use that file instead.

---

## Asset Structure

The magnet ships as a Notion page (most common), Gamma deck, or LinkedIn doc.

### Title format

Three patterns that have shipped:

- **Outcome-led:** "Scaling a Pet Brand past $1M/month with Ad Creatives (2025)"
- **Strategy-led:** "Scriptwriting $100k Ads (NOT UGC)" (when the case study is really about a strategy applied to a single client)
- **Arc-led:** "How we took [vertical] from [number] to [bigger number]" (only when client is partially identifiable or fully anonymized in a way that doesn't reveal them)

Propose 3 title options for Mauro to pick. Don't commit to one without alternatives.

### Subtitle format

Always include a specific number anchor and a scale signal:
- "How we scaled this brand to $750K/month using a creative system anyone can replicate."
- "The 3-phase arc that took a pet brand from $29K/month to $750K/month."

### Body structure

```
[Opening hook: 1-2 lines naming the result and why it matters]

PART 1: The starting point
  - Where the client was when they came in
  - What was working / not working at that point
  - The specific bottleneck

PART 2: The strategy we applied
  - The framework or approach (anchor on Growthub's named systems where they apply: Stealth Creatives, the 4-lever system, etc.)
  - Why this framework specifically (not generic best practices)
  - 2-3 specific tactical moves with [VISUAL: anonymized creative grid / dashboard / brief sample]

PART 3: The arc (only if Variant B / Arc-led)
  - Phase 1 → Phase 2 → Phase 3 with specific numbers per phase
  - What changed between phases

PART 4: The result
  - Numbers (verified from source transcript)
  - Timeframe (verified)
  - What's next / where this brand is going

PART 5: Replicable layer
  - What the operator reading this can actually take and apply
  - 3-5 specific lessons in operator language, not agency language
  - Where it fits in their own creative system

CLOSING: 1-2 lines on how Growthub can help if they want this for their brand. Soft CTA, never a hard sell.
```

### Anonymization rules

Per `feedback_client_naming.md`:
- Client name: never named publicly. Use "a pet ecom brand we manage", "a supplement brand we manage", etc.
- Wins-log entries note client names internally only. Cross-reference the wins-log to make sure you're following the established anonymization for each client.
- Some wins have a hard "do not store anywhere" rule (see Win 006 in wins-log for the pet brand). Honor that.
- Public references to non-client brands are okay (PetLab Co, MiamiMD, Norse Organics, etc. — see wins-log for the public-reference list per vertical)

### Numbers verification

Every dollar figure, percentage, and timeframe in the magnet must trace back to the source transcript or internal record. If it doesn't, bracket-placeholder it per [[feedback_no_fabricated_performance_numbers]]. Do not invent specifics to make the case study sound better.

---

## Cover Image (Subtype-Specific)

Inherits the base cover spec from `_master.md`.

Subtype-specific elements:
- Title in large white text at the top of the dark section (often includes the headline number)
- Subtitle (1 line) with the framing variant signal (outcome / arc / aggregate)
- "Created by Growthub.Agency" or "Created by @growthub.agency" line
- Optional: a table-of-contents preview (the $20M pet brand magnet did this) showing the section headers, signals depth without revealing content
- Optional: an anonymized dashboard screenshot or creative grid teaser at the bottom (only if the visual doesn't reveal the client identity)

Avoid: any visual that could identify the client. Blur logos, redact brand names, abstract any URL or product shot.

---

## Post Hook Formulas (Subtype-Specific)

`_master.md` has the universal hook formulas. For case-study magnets specifically, the patterns that have worked:

### LinkedIn (primary channel for case studies)
- **"I took [client framing] from [number] to [bigger number]"** (Variant A, pet $29K → $750K example)
- **"I've scaled over [N] [vertical] brands and generated $[Y] for them"** (Variant C aggregate)
- **"Scaling [vertical] [thing] requires a NEW playbook"** (when the case study introduces a strategic shift)

### X
- **"After scaling [N] [vertical] brands past $[X]M/month, here's the [specific framework]"** (less common but works)
- Case studies generally land better on LinkedIn than X. Mauro often leads with LinkedIn for case-study magnets and cross-posts to X only if the angle adapts.

### Authority anchor placement

For case studies, the authority anchor is usually the case study itself ($29K → $750K is its own anchor). When the case study numbers aren't strong enough on their own, add a secondary anchor:
- "Same playbook we've used across $107M+ in managed Meta spend."
- "Same approach that's powered $20M+ generated for pet brands we manage."

---

## DM Override (None)

Use the default DM from `_master.md`:

```
Hey (name), here's the breakdown:

LINK

P.S. Would you like a free audit for your brand? Reply "yes" and we can chat about how it works.
```

Noun: `breakdown` (confirmed). Do not swap.

---

## Output Checklist

Before handing off to Joao for scheduling, confirm:

- [ ] Underlying case study input was actually used (not just wins-log scraps)
- [ ] Notion / Gamma / LinkedIn doc exists with all 5 parts of the body structure
- [ ] Every dollar figure, percentage, and timeframe traces back to source material
- [ ] Client is anonymized per `feedback_client_naming` (no public name, vertical is okay, follow per-client rules in wins-log)
- [ ] Framing variant (A / B / C) is consistent across the post, the asset title, and the cover
- [ ] Replicable layer (Part 5) is operator-facing, not agency-facing — concrete moves the reader can run themselves
- [ ] Cover image follows the subtype spec (no client-identifying visuals)
- [ ] X post copy (if shipping X) follows the X structure in `_master.md`
- [ ] LinkedIn post copy follows the LinkedIn structure in `_master.md`
- [ ] DM copy is the `_master.md` default with noun = "breakdown"
- [ ] Keyword is ALL CAPS, 3-7 chars, topic or vertical-related
- [ ] LeadShark config: Auto-connect OFF, Partially Engage ON, Follow-up DM OFF
- [ ] Voice.md 60-second pre-publish checklist passed

---

## Anti-Patterns (Specific to This Subtype)

- Drafting from wins-log alone, without underlying case study source material. Wins-log gives anchor numbers, not strategic depth.
- Result-flex without strategy. "We scaled a brand to $1M/month" without the HOW reads as a brag, not a case study.
- Replicable layer that's actually agency-facing. "Implement a stealth creative system" is not replicable. "Use the 5-format split with a $5K/format test budget" is.
- Fabricating specifics to make the case study sound better. Use only what's in the source per [[feedback_no_fabricated_performance_numbers]].
- Naming the client. Ever. Even when the client is publicly aware of Growthub managing them, the wins-log rule is internal-only for almost all entries.
- Numbers-led framing (Variant A) when the source transcript doesn't support a clean single-number arc. Use Variant B (arc-led) instead.
- Generic "lessons learned" closing. The replicable layer must be specific or it doesn't earn the DM reply.
