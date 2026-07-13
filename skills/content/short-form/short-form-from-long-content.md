# Skill: Short-Form from Long Content

**Version:** 1.0
**Created:** 2026-05-27
**Input:** Long content source (article, video transcript, long-form post, internal doc) + which account is active
**Output:** 3-5 short-form post options in Lorenzo's voice, picked by Mauro, finalized as a single post

---

## What This Skill Does

Takes existing long content (an article, a Lorenzo case study video transcript, a 22-page mini-guide, a long-form post that already shipped, an internal SOP) and produces short-form X / LinkedIn posts that can be deployed independently to:

- Tease the long content
- Surface a sharp insight from it
- Compress a framework from it into a 3-item list
- Plant a provocative claim from it
- Highlight a specific number from it

Short forms feed the top of the funnel between bigger drops. The team produces 5-10 short forms per week by repurposing existing long content.

---

## Required Reading

- **Active account config** (e.g., `accounts/lorenzo-x/account-config.md`). Substitute every `{{token}}` in skill output with values from the active account config.
- `brands/growthub/voice.md` — voice rules + 60-second pre-publish checklist
- `brands/growthub/audience.md` — ICP v2.2 (verbatim pain phrases that work as short-form hooks)
- `research/x-analytics-exports/short-forms-2026-top-performers.md` — the data layer this skill was extracted from. Refer to this for actual examples per template.

---

## The 3 Steps

### Step 1: Identify 3-5 strongest single insights

Read the source content. Pull out the 3-5 strongest single insights. An insight is strong if:

- It's specific to operator-grade work (real client, real spend, real artifact)
- It's defensible — Lorenzo or the team can back it under scrutiny
- It's compressible — fits in under 30 words without losing meaning
- It's surprising to someone in the ICP (brand operators $100K-$1M+/mo)

Write each insight in shorthand before drafting the actual posts. The skill is built around these insights, not around the source content itself.

### Step 2: Match each insight to a template

The 6 templates (full examples in `research/x-analytics-exports/short-forms-2026-top-performers.md`):

| # | Template | When to use | Word target |
|---|---|---|---|
| **A** | Caption tease | The post points to attached media (video, image, article URL). Media does the work. | 7-15 |
| **B** | Insight statement | One sharp standalone claim. No setup, no CTA. | 7-15 |
| **C** | Mini-framework | Numbered or bulleted 3-item list. Light teaching. | 17-30 |
| **D** | Provocative one-liner | Challenge claim. Standalone or with attached context. | 7-11 |
| **E** | Specific number flex | Curiosity hook anchored on a real number. | 9-15 |
| **F** | Follow tease | Momentum / upcoming-content signal. Used sparingly. | 10-20 |

Match each insight to whichever template fits best. One insight = one template. Don't force.

### Step 3: Draft 3-5 short-form options + pick one

Output format:

```
SOURCE: [name + path of the source long content]

Option 1 (Template [letter] — [template name]):
  "[draft short-form post]"
  [optional: attached media note]

Option 2 (Template [letter] — [template name]):
  "[draft short-form post]"
  [optional: attached media note]

Option 3 (Template [letter] — [template name]):
  "[draft short-form post]"
  [optional: attached media note]
```

Wait for Mauro to pick before finalizing. The pick gets a voice.md compliance pass + the final hand-off note.

---

## Voice Rules (Critical Reminders)

Full rules in `brands/growthub/voice.md`. Non-negotiables for short-form copy:

1. **No em dashes.** Never.
2. **No "It's not X, it's Y"** structures.
3. **No "Most brands" openers** unless followed by a sharp Growthub-specific counter-claim.
4. **No problem-to-purpose reversals.**
5. **Numbers must be real.** Cross-check `accounts/lorenzo-x/wins-log.md` for any dollar/result claim.
6. **Possessive operator credit** ("our", "we", "I broke down") when the insight comes from team work.
7. **No filler openers.** No "Quick reminder:", "Friendly reminder:", "Real talk:", "Here's the thing:".

---

## Template Details

### Template A: Caption tease

Short framing line that points to attached media. The media is the deliverable; the caption is a curiosity hook.

**Anchor examples:**
- "For all those wondering how we build winning ads..." (9w, 26.2K impressions)
- "This is how you create winning ads" (7w, 16.4K impressions)
- "Want to scale in a crowded market? Read this" (9w, 5.3K impressions)
- "Reminder on what creative diversity REALLY means." (7w, 9.9K impressions)

**Pattern formula:**
- `[Curiosity gap question OR reminder OR statement] [attached media]`

**Required input:** the attached media (video file, article URL, image, screenshot). Without the media, this template doesn't work.

### Template B: Insight statement

Direct standalone claim. The insight IS the post.

**Anchor examples:**
- "This is literally why reviews are so important in your research" (11w, 23.2K imp)
- "you can literally see this in every single TOF ad that's an ACTUAL winner" (14w, 5.9K imp)
- "The example I show in this article is literally worth $1M" (11w, 10.4K imp)

**Pattern formula:**
- `[Direct claim about a tactical truth Lorenzo learned from real work]`

### Template C: Mini-framework

3-item numbered list. Compress a process / category / decision-tree from the long content.

**Anchor examples:**
- "Our 3 highest spending formats this year: 1. Podcast style ads 2. Street interviews 3. Skit conversations" (17w, 15.3K imp)
- "How to create banger hooks: 1. Make your first 3s organic 2. Use facial expressions 3. Give context right away" (20w, 7.2K imp)

**Pattern formula:**
- `[Setup line ending with colon]: 1. [Item] 2. [Item] 3. [Item]`
- 3 items is the sweet spot. 2 feels thin. 4+ runs long.

### Template D: Provocative one-liner

Challenge claim. Stops the scroll without context.

**Anchor examples:**
- "Your ads suck. With this maybe a bit less." (9w, 11.1K imp)

**Pattern formula:**
- `[Strong direct statement that challenges a default assumption]`

**Caution:** the line has to be defensible. Don't ship provocations without backing. If a commenter pushes back, Lorenzo / Mauro should have a 30-second answer ready.

### Template E: Specific number flex

Curiosity hook anchored on a concrete dollar / time / volume number from real work.

**Anchor examples:**
- "The example I show in this article is literally worth $1M" (11w, 10.4K imp)

**Pattern formula:**
- `[Number + specific context] + [pointer to deeper content if applicable]`

**Critical:** number must be real. Cross-check against `accounts/lorenzo-x/wins-log.md` or the source content. No fabricated specifics per `feedback_no_fabricated_performance_numbers`.

### Template F: Follow tease

Forward-looking signal. Sets up future content.

**Anchor examples:**
- "Got a lot of sauce coming regarding AI... Follow me so you don't miss it:" (15w, 7.3K imp)

**Pattern formula:**
- `[Tease about upcoming content theme] [follow CTA] [optional: pointer to teaser asset]`

**Use sparingly.** Over-use looks needy. Max once per week.

---

## Output Checklist

Before handing off (to Joao for scheduling or Mauro for final review):

- [ ] Source long-content path captured (so the lineage is clear)
- [ ] 3-5 options drafted across at least 2 different templates
- [ ] Each option includes its template letter + name
- [ ] All numbers verified against source or wins-log
- [ ] No em dashes, no "It's not X, it's Y", no "Most brands" openers
- [ ] No filler openers ("Quick reminder", "Real talk", etc.)
- [ ] All `{{tokens}}` resolved from `accounts/[active]/account-config.md`
- [ ] If Template A (caption tease): attached media specified
- [ ] Voice.md 60-second pre-publish checklist passed

---

## Hand-Off (Joao)

Once Mauro picks the final post:

1. Save the final short form + any attached media to Notion in the Joao handoff page
2. Slack / DM Joao that the post is ready
3. Joao schedules via Hypefury

Short forms ship throughout the week to keep the algorithm fed between bigger drops.

---

## Anti-Patterns (Specific to This Subtype)

- Drafting from the source's surface (headlines, intros) instead of pulling the strongest insight from inside
- Stretching a 7-word insight into 50 words to "match the template length"
- Faking the number in a Template E post — voice.md and `feedback_no_fabricated_performance_numbers` both ban this
- Provocative one-liner without backing — when commenters push, you have nothing
- Mini-framework with 5+ items — defeats the format
- Caption tease without attached media — the post collapses
- Follow tease more than once a week — looks needy
- Treating this as a long-form skill. Short forms are 30-second consumes, not deep reads. Compress hard.

---

## Cross-Reference

- **Data source**: `research/x-analytics-exports/lorenzo-x-2025-12-08-to-2026-04-28.csv` (1,701 posts, 195 truly-short after filtering)
- **Extracted patterns**: `research/x-analytics-exports/short-forms-2026-top-performers.md`
- **Adjacent skills**: `skills/content/x-article-creator.md` (the article is one of the most common source inputs for this skill), `skills/content/long-form/_master.md` (long-form posts are another common source)
- **Voice rules**: `brands/growthub/voice.md`
- **Wins data**: `accounts/lorenzo-x/wins-log.md` (for fact-checking dollar / result claims in Template E)
