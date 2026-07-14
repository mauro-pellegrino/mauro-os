# Skill: Miro Breakdown to X Article
**Version:** 2.0
**Created:** 6 April 2026
**Updated:** 14 July 2026 (retargeted to Mauro's own brand, @maurojpelle)
**Input:** Miro board screenshots (brand/content-system breakdown) + subject name
**Output:** Full X article in Mauro's voice (800-1200 words)

---

## What This Skill Does

Takes screenshots of a completed Miro breakdown board and turns the analysis into a standalone X article in Mauro's voice. The Miro board is the research layer. This skill extracts the insights and writes them as publishable content.

This is a different workflow from `youtube-miro-board.md` (which goes script → board) and `x-article-creator.md` (which goes YouTube transcript → article). This skill goes Miro board images → article.

---

## Required Reading

Before writing, read `brand/voice.md`, `brand/positioning.md`, and `brand/audience.md` in full. Run every output through the pre-publish checklist in voice.md. Ground every audience-facing decision (stated pain, language, sophistication level) in the ICP in audience.md.

---

## What to Extract from the Miro Images

Work through the images and pull the following before writing a single word:

**1. The core thesis**
What is the one insight that explains how this subject grew, converted, or scaled? Write it in one sentence before starting the article. The article is built around this, not around everything in the board.

**2. The credential anchor**
What real number makes this credible? Audience size, output volume, revenue estimate, growth rate. This goes in the opening 3 sentences. Never invent one; bracket a placeholder if it isn't verifiable.

**3. The mechanism**
What is the subject's unique mechanism or villain? How do they frame the cause of their audience's problem? This is usually the strongest section.

**4. The personas**
How many audience segments does the subject target? What is the core pain point for each? Which segments dominate their active content?

**5. The format/structure insight**
What content formats do they use and why? How does format match to funnel stage or awareness level?

**6. The actionable takeaway**
What can the reader apply immediately? This becomes the final section before the CTA.

---

## Article Structure

Follow the `x-article-creator.md` output template and patterns exactly. Key rules:

- Title: lowercase, strongest pattern for the piece, under 12 words
- Opening: 3 sentences max before the reader knows what they're getting
- 3-4 sections with short single-noun or short-phrase headers
- Each section 150-250 words minimum, mechanism explained, not just named
- One CTA at the end, always low commitment
- Sign off: "Talk soon, Mauro."
- Target word count: 900-1100 words
- No em dashes. No "It's not X, it's Y." No "Most brands" openers.

---

## How to Run This Skill

**Step 1 — Inventory the board**
List every section visible in the Miro images. Note what's legible and what's cut off. Flag anything unclear before writing.

**Step 2 — Extract the 6 elements above**
Write them out in shorthand before touching the article. This is the research pass.

**Step 3 — Identify the single strongest insight**
The article is not a summary of the whole board. Pick the insight that will resonate most with Mauro's audience (established agency owners building an AI-powered inbound engine). Build the article around that.

**Step 4 — Write the opening 3 lines**
Follow the x-article-creator opening formula. Strongest hook for this input, then the tension, then the promise.

**Step 5 — Write 3 sections**
Each section = one sub-idea supporting the core thesis. 150-250 words each. Mechanism explained, example included, one-line payoff at the end.

**Step 6 — Write the close and CTA**
2-3 sentences wrapping the core insight. One CTA from the approved patterns in `x-article-creator.md`.

**Step 7 — Word count check**
Under 800 words means a section is thin. Expand before outputting.

**Step 8 — Anti-pattern check**
Run the pre-publish checklist from voice.md.

**Step 9 — Review, then save**
Per `feedback_article_workflow`: show the article in chat and get Mauro's review first. Once approved, save to `brand/posts/[subject-name]-breakdown-x-article.md` and commit.

---

## File Naming Convention

```
brand/posts/[subject-name]-breakdown-x-article.md
```

Example:
- `brand/posts/[subject]-breakdown-x-article.md` (kebab-case the subject name)
