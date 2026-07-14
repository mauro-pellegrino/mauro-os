# Brand Breakdown Skill
**Version:** 1.0
**Purpose:** Run a full creative breakdown of a competitor or client brand for use in a YouTube video and Miro board. Produces a structured analysis ready for scripting and visual mapping.

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the pre-publish checklist in voice.md. Ground every audience-facing decision (stated pain, language, framing) in the ICP in audience.md.

---

## When to use this skill

Use when:
- Analysing a brand's Meta ad library for a YouTube breakdown video
- Building a creative strategy map for a client pitch
- Researching what is working in a category before building new creative

Inputs needed before starting:
- Brand name and product category
- Raw ad scripts or transcripts (longest-running ads preferred, minimum 5)
- Ad account data: active ads count, total library size, media mix if available
- Any additional research (funnel details, offer structure, Atria/Foreplay data)

If inputs are missing, ask for them one at a time. Never guess at ad data.

---

## Output Structure

Produce the breakdown in this exact order.

---

### 1. AD ACCOUNT OVERVIEW

Cover:
- Total active ads and library size
- How long the brand has been running ads (oldest creative date)
- New ads launched in last 30 days and growth rate if known
- Media mix: video vs image vs carousel, percentages
- Hook, copy, headline, and landing page variant counts if available
- One-line read on what the volume and mix signals about their strategy

Keep this section factual. No padding. If data is missing, say so and flag what the user should send.

---

### 2. HERO PRODUCTS

Identify which products appear most across the ad scripts. This section comes before personas because the product concentration tells you how the brand structures its funnel and which persona they have committed to.

Cover:
- Which product appears in the most scripts (the primary acquisition driver)
- Which products appear occasionally or in specific formats only
- Whether the brand runs a single hero product or splits attention across multiple SKUs
- What the product concentration signals about their strategy

Format:

**Primary product:** [Name] — appears in [X of Y] scripts. [One sentence on what problem it solves and who it targets.]

**Secondary products (if any):** [Name] — appears in [X of Y] scripts. [One sentence on where it fits relative to the primary.]

**What the concentration tells you:**
If one product dominates, the brand has found a single conversion vehicle and is scaling it. If multiple products share airtime roughly equally, the brand is either testing or has multiple personas with distinct needs. Note which scenario applies and what it means for gap analysis later.

---

### 3. PERSONA BREAKDOWN

Identify 2 to 5 personas based on what the ads actually target. Do not use age ranges as the persona definition. Build each persona around:
- Who they are in the context of the problem (not demographics)
- Their emotional state relative to the product
- The specific physical or psychological pain they are in
- What language they use internally about their problem
- What makes them respond to this brand specifically

Format each persona as:

**Persona Name — [Short descriptor]**
[3 to 5 sentences. Who they are, what they feel, what they want, what makes them respond.]

If two or more personas share pain points, note the overlap but keep them separate if they respond to different angles or formats.

---

### 4. AWARENESS LEVEL BRAINSTORM

For each persona, map one internal thought per awareness stage. These are not ad hooks. These are the actual thoughts inside the persona's head before they see any ad.

Stages:
- Unaware: Does not connect their symptom to a solvable problem
- Problem Aware: Knows something is wrong, does not know what to do
- Solution Aware: Knows solutions exist, has not found the right one
- Product Aware: Knows the brand or product, has not bought
- Most Aware: Ready to buy, needs a final push

Format:
**Persona Name**
Unaware: [Thought]
Problem Aware: [Thought]
Solution Aware: [Thought]
Product Aware: [Thought]
Most Aware: [Thought]

Keep each thought one sentence. Write it as the persona's internal voice, not a description of their state.

---

### 5. ANGLES (PAIN POINTS) PER PERSONA

List 3 to 5 pain points per persona. These are the raw emotional entry points the ads can use. Not messaging. Not hooks. Just the underlying pain the ad enters from.

Format:
**Persona Name**
- [Pain point]
- [Pain point]
- [Pain point]

Pull these directly from the ad scripts where possible. If a specific script illustrates the pain point best, note the script number.

---

### 6. FORMATS PER AWARENESS LEVEL

Map which ad formats the brand uses at each awareness level. Note which scripts are examples. Then add one line on why that format works at that stage.

Use this as the format map:

| Awareness Level | Format Used | Example Scripts | Why It Works |
|---|---|---|---|
| Unaware | | | |
| Problem Aware | | | |
| Solution Aware | | | |
| Product Aware | | | |
| Most Aware | | | |

---

### SIDE SECTION — LONG FORM FORMATS (if applicable)

Only include this section if the brand runs VSLs, long-form podcast ads, or educational video ads over 5 minutes.

Cover:
- How the video opens (failure story, problem statement, curiosity hook)
- Where the villain or root cause is introduced and how it is framed
- How authority is built across the script (credentials, studies, specificity)
- When the product enters and why the late reveal works
- How the close is structured (price, discount ladder, urgency, guarantee)
- Why the length itself functions as a credibility signal for this specific audience

Keep this section analytical. Explain the mechanics, not just what happens.

---

## Rules for this skill

- Never invent ad data. Use what the user provides or flag the gap.
- Never describe personas by age range alone. Age can appear as context but is never the defining trait.
- Angles are pain points, not messaging directions. Keep them raw.
- If the brand runs fewer than 5 scripts, note that the analysis is limited and which sections may be incomplete.
- Do not save ad transcripts or raw scripts to the research folder unless the user explicitly asks.
- Do not save Miro board briefs unless the user explicitly asks.
- After completing the breakdown, ask the user what they want to do next: script, Miro board, or titles.

---

## Integration with other skills

- To turn this breakdown into a YouTube script: use `skills/youtube/youtube-hook-script.md`
- To turn this breakdown into a Miro board: use `skills/youtube/miro-design-system.md`
- To generate titles for the video: use `skills/youtube/youtube-title-generator.md`
