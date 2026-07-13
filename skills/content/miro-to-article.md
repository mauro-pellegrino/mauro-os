# Skill: Miro Breakdown to X Article
**Version:** 1.0
**Created:** 6 April 2026
**Input:** Miro board screenshots (brand/ad library breakdown) + brand name
**Output:** Full X article in Lorenzo's voice (800-1200 words), saved to `scripts/`

---

## What This Skill Does

Takes screenshots of a completed Miro brand breakdown board and turns the analysis into a standalone X article in Lorenzo's voice. The Miro board is the research layer. This skill extracts the insights and writes them as publishable content.

This is a different workflow from `youtube-miro-board.md` (which goes script → board) and `x-article-creator.md` (which goes YouTube transcript → article). This skill goes Miro board images → article.

---

## Required Reading

Before writing, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. Run every output through the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

## What to Extract from the Miro Images

Work through the images and pull the following before writing a single word:

**1. The core thesis**
What is the one insight that explains how this brand scaled? Write it in one sentence before starting the article. The article is built around this, not around everything in the board.

**2. The credential anchor**
What number makes this credible? Active ad count, revenue estimate, ad spend, brand scale. This goes in the opening 3 sentences.

**3. The mechanism**
What is the brand's unique mechanism or villain? How do they frame the cause of the customer's problem? This is usually the strongest section.

**4. The personas**
How many personas does the brand target? What is the core pain point for each? Which personas dominate the active ad library?

**5. The format/structure insight**
What creative formats do they use and why? What does the VSL structure look like? How does format match to awareness level?

**6. The actionable takeaway**
What can the reader apply immediately? This becomes the final section before the CTA.

---

## Article Structure

Follow the `x-article-creator.md` output template and patterns exactly. Key rules:

- Title: credential number + topic, under 12 words
- Opening: 3 sentences max before the reader knows what they're getting
- 3-4 sections with short single-noun or short-phrase headers
- Each section 150-250 words minimum — mechanism explained, not just named
- One CTA at the end, always low commitment
- Sign off: "Talk soon, Lorenzo."
- Target word count: 900-1100 words
- No em dashes. No "It's not X, it's Y." No "Most brands" openers.

---

## How to Run This Skill

**Step 1 — Inventory the board**
List every section visible in the Miro images. Note what's legible and what's cut off. Flag anything unclear before writing.

**Step 2 — Extract the 6 elements above**
Write them out in shorthand before touching the article. This is the research pass.

**Step 3 — Identify the single strongest insight**
The article is not a summary of the whole board. Pick the insight that will resonate most with Growthub's audience (DTC founders, creative directors, media buyers). Build the article around that.

**Step 4 — Write the opening 3 lines**
Follow the x-article-creator opening formula. Credential anchor, then the tension, then the promise.

**Step 5 — Write 3 sections**
Each section = one sub-idea supporting the core thesis. 150-250 words each. Mechanism explained, example included, one-line payoff at the end.

**Step 6 — Write the close and CTA**
2-3 sentences wrapping the core insight. One CTA from Lorenzo's approved patterns.

**Step 7 — Word count check**
Under 800 words means a section is thin. Expand before outputting.

**Step 8 — Anti-pattern check**
Run the 60-second pre-publish checklist from voice.md.

**Step 9 — Save and commit**
Save to `scripts/[brand-name]-breakdown-x-article.md`.
Commit and push immediately. Never leave it only in conversation.

---

## File Naming Convention

```
scripts/[brand-name]-breakdown-x-article.md
```

Examples:
- `scripts/miamimd-breakdown-x-article.md`
- `scripts/goli-breakdown-x-article.md`
- `scripts/hims-breakdown-x-article.md`
