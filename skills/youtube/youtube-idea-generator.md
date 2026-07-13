# YouTube Idea Generator — Growthub / Lorenzo Pravatà
**Version 1.2 | Updated 30 March 2026**

This skill takes the output of the Weekly Research Brief and generates ranked YouTube video ideas for Lorenzo Pravatà's channel. Every idea must be grounded in what is actually resonating in the space right now — not generic evergreen topics. Use this after running `skills/weekly-research.md`.

---

## Required Reading

Before producing any written output, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. All copy must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

## Step 0 — Surface What's Already Known

Before generating any ideas, surface everything already on file about the topic or content area. Output it first. Then ask for additional context before generating ideas.

### 1. Search existing research

```bash
grep -rli "[topic keyword]" /Users/mauro/growthub-os/research/
grep -rli "[topic keyword]" /Users/mauro/growthub-os/brands/
```

For each matching file, read it and extract:
- How the topic has already been framed or covered in existing research
- Which angles competitors have already taken
- Any ICP language, pain points, or quotes captured about this topic
- Lorenzo's existing coverage (avoid suggesting topics he has already made)

### 2. Output a knowledge summary

```
WHAT'S ALREADY ON FILE: [TOPIC/AREA]
--------------------------------------
Source: [filename]
- [Finding — angle, competitor coverage, ICP language, or data point]

COMPETITOR COVERAGE:
- [Competitor] covered [angle] — gap left: [what they didn't say]

LORENZO'S EXISTING COVERAGE:
- [Any videos he has already made on this topic — skip or differentiate]

CONTENT GAPS IDENTIFIED:
- [Angle or sub-topic competitors haven't touched]
```

### 3. Request additional context

After the summary, ask:

> "That's what's already on file. Anything you want to add before I generate ideas? For example: a specific brief from Lorenzo, a new research source, or a vertical you want prioritised."

Wait for the response before generating ideas.

---

## When to Run This Skill

Trigger this skill when:
- The weekly research brief has been completed
- Someone asks "What should Lorenzo make this week?"
- Someone asks "Give me video ideas based on the research"
- A content planning session is starting

---

## Inputs Required

Before generating ideas, load all 4 sources:

1. **Weekly research brief** (`research/YYYY-MM-DD.md`) — YouTube outliers, hot X conversations, ICP language captured, content gaps
2. **Lorenzo's content asset ideas** (`research/content-assets-ideas.md`) — Lorenzo's own priority list of topics, case study verticals, ICP beliefs to break, and video ideas. Always cross-reference this before generating — don't suggest something Lorenzo has already planned or deprioritised.
3. **ICP profiles** (`brands/growthub/audience.md` or CLAUDE.md Section 2 and 6) — who the viewer is and what they're struggling with
4. **Psychological profiles of 7-figure founders** (CLAUDE.md Section 6) — emotional triggers, fears, and language patterns of ecom and SaaS founders

`brands/growthub/positioning.md` and `brands/growthub/voice.md` should also be loaded if populated.

---

## Idea Generation Framework

For each idea generated, the following must be answered. Do not output an idea unless all four are complete.

### 1. Core Angle
What is the specific contrarian claim, reframe, or insight this video is built on? Not the topic — the angle. The angle is the specific take that makes this video worth watching over every other video on the same topic.

**Wrong:** "How to improve your Meta ads"
**Right:** "Why most brands testing more creatives are actually hurting their performance — and what creative diversity actually means"

The angle should feel like something only someone with Lorenzo's data ($106M+ in managed spend) can credibly claim.

### 2. Target Viewer
Who specifically is this video for? Be precise. Use ICP language from CLAUDE.md.

- Are they ecom founders stuck at a spend level (e.g. £30k–£100k/month)?
- Are they frustrated by a specific recent change (e.g. Andromeda, iOS, creative fatigue)?
- Are they beginners trying to understand a concept Lorenzo has original depth on?
- Are they operators who run their own accounts vs. agency-dependent brands?

**State the viewer in one sentence:** "This is for a 7-figure ecom founder who has been spending £50k/month and has hit a performance ceiling they don't understand."

### 3. Why It Will Perform
Ground the performance prediction in evidence from the research brief. Reference:
- Which YouTube outlier it echoes (same topic, different angle)
- Which X conversation it responds to or amplifies
- Which ICP pain point it directly addresses
- Whether it fills a content gap competitors are missing

Do not predict performance based on gut feel. Every performance claim should point to something observed in the research.

### 4. One-Line Hook
Write the hook in Lorenzo's exact opening style: a declarative contrarian statement, not a question. This should work as both the video's opening line and a short-form teaser.

Pull from Lorenzo's established hook patterns (see `skills/youtube-hook-script.md`):
- Opens with "Most brands..." or "The main reason why most brands..."
- States the wrong thing most people do as fact, not hypothesis
- Creates mild anxiety in the right viewer — they should feel they might be making this mistake

**Examples of correctly styled hooks:**
- "Most brands think they're running 50 ads. Meta thinks they're running 3."
- "The reason your ROAS dropped last month has nothing to do with your creative."
- "Most scaling agencies are giving you more of what already stopped working."

---

## Output Format

Produce ideas in ranked order: highest priority first. Rank by the following weighted criteria:

**Priority 1 — High conversion potential (likely to drive calls)**
- Topic directly addresses a pain point of a brand spending £50k+/month
- The viewer will self-identify as Lorenzo's ICP
- Watching it nudges them toward booking a call

**Priority 2 — Authority building**
- Demonstrates Growthub's original data, frameworks, or methodology
- Competitor channels cannot match the specificity
- Builds Lorenzo's position as the practitioner with the most spend under management

**Priority 3 — Growth / reach**
- Broad enough to attract new viewers who may not know Lorenzo
- Timely — tied to a recent algorithm change, platform announcement, or hot conversation
- High search or discovery potential

---

### Idea Output Template

```
IDEA #[N] — [Short working title]
Priority: [1 / 2 / 3]
Source: [Which research signal triggered this — outlier video, X conversation, content gap, ICP language]

Core Angle:
[1–2 sentences. The specific claim or reframe this video makes.]

Target Viewer:
[1 sentence. Precise ICP description.]

Why It Will Perform:
[2–3 sentences. Ground in research evidence.]

One-Line Hook:
"[Hook written in Lorenzo's declarative style.]"
```

---

## How Many Ideas to Generate

- **Minimum output:** 5 ideas
- **Typical output:** 7–9 ideas
- Always produce at least 2 Priority 1 ideas (call-driving topics)
- Always produce at least 1 Priority 3 idea (reach / growth play)

---

## Cross-Channel Fit Check

Before finalising the idea list, run this check on each idea:

1. **Is this already on the channel?** If Lorenzo has covered this topic in the last 90 days, skip it unless the angle is clearly differentiated.
2. **Can Growthub back this with data?** Lorenzo's credibility comes from real numbers. If the angle requires claims Growthub cannot support from real client data, downgrade or cut it.
3. **Is the hook specific enough?** A hook that could come from any Meta ads creator is not distinctive enough. The hook should only make sense coming from someone managing $106M+/year in spend.
4. **Does it fit the $50k/month audience filter?** Ideas that target beginner audiences are lower priority unless they serve a volume play (reach). Lorenzo's CTA is always to brands spending £50k+/month.

---

## Routing After This Skill

Once ideas are approved:
- Pass the chosen idea to `skills/youtube-title-generator.md` to generate title variations
- Pass the chosen idea to `skills/youtube-hook-script.md` to write the full script
- Log any ICP language pulled from the research brief to `brands/growthub/learnings.md`

---

## High-Priority Idea Categories

These categories come directly from `research/content-assets-ideas.md` and should be prioritised when generating ideas. When in doubt, suggest from these before inventing new angles.

**1. Case studies by vertical** (highest priority — main conversion driver)
SaaS, ecommerce (generic), supplements, apps, skincare, food, men's products, women's products, young vs. older audiences. Each should follow the Pet case study structure with more lessons, less raw data.

**2. ICP belief-breaking videos**
- "I just need more ads" → why quantity without quality/variety fails post-Andromeda
- "I'll find a cheap UGC agency" → why classic UGC agencies underdeliver vs. a real performance team
- "We already run a lot of ads" → the math behind why volume alone doesn't scale
- "We don't need that many ads" → volume matters, here's why

**3. AOV/LTV mechanics**
Why new customer economics matter more than ROAS. Mechanisms: creatives to decrease CAC, CRO to increase AOV, retention (subscriptions, emails, brand experience). Real brand examples where high LTV allows $100+ CPAs that would terrify most brands.

**4. Ad fatigue explainer**
Why 65+ diverse ads beat 5 polished ones. Why ROAS drops when budget increases. Frequency → fatigue curve → cost spike visualised.

**5. App/SaaS Meta ads**
Near-zero competition on YouTube. Already driven inbound. What app/SaaS businesses search for when trying to run Meta ads.

**6. Format-specific tutorials**
Deep dives on podcast-style ads, street interview format, documentary-style creative, VSLs. How to write, brief, and produce each one.

**7. Creative Strategy Map walkthrough**
Full process with a real client example. Miro or slides format.

**8. CRO video**
Main tests with examples, connected to the creative strategy map. Include price and offer testing, weekly processes to implement.

---

## Anti-Patterns

- **Never generate a generic topic idea.** "How to improve your Meta ads" is not an idea — it is a category. The angle is the idea.
- **Never generate more than one idea on the same topic.** If the brief surfaces multiple signals pointing to the same topic, pick the strongest angle.
- **Never base performance predictions on the topic alone.** Base them on the specific research signals observed this week.
- **Never write hooks as questions.** Lorenzo's style is declarative. Hook questions are off-brand.
- **Never suggest formats** — this skill generates ideas, not formats. Format decisions happen in the script skill.
- **Never ignore the content gap.** If competitors are overdoing a topic, the best play is often to attack the gap next to it, not to compete head-on.
