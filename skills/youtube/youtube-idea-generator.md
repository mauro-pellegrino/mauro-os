# YouTube Idea Generator: Mauro's Channel
**Version 2.0 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

This skill takes the output of the Weekly Research Brief and generates ranked YouTube video ideas for Mauro's channel. Every idea must be grounded in what is actually resonating in the space right now, never in generic evergreen topics. Use this after running `skills/research/weekly-research.md`.

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md.

---

## Step 0: Surface What's Already Known

Before generating any ideas, surface everything already on file about the topic or content area. Output it first. Then ask for additional context before generating ideas.

### 1. Search existing research

```bash
grep -rli "[topic keyword]" /Users/mauro/mauro-os/research/
grep -rli "[topic keyword]" /Users/mauro/mauro-os/brand/
```

For each matching file, read it and extract:
- How the topic has already been framed or covered in existing research
- Which angles competitors have already taken
- Any ICP language, pain points, or quotes captured about this topic
- Mauro's existing coverage (avoid suggesting topics he has already made)

### 2. Output a knowledge summary

```
WHAT'S ALREADY ON FILE: [TOPIC/AREA]
--------------------------------------
Source: [filename]
- [Finding: angle, competitor coverage, ICP language, or data point]

COMPETITOR COVERAGE:
- [Competitor] covered [angle]. Gap left: [what they didn't say]

MAURO'S EXISTING COVERAGE:
- [Any videos he has already made on this topic: skip or differentiate]

CONTENT GAPS IDENTIFIED:
- [Angle or sub-topic competitors haven't touched]
```

### 3. Request additional context

After the summary, ask:

> "That's what's already on file. Anything you want to add before I generate ideas? For example: a specific brief, a new research source, or a pillar you want prioritised."

Wait for the response before generating ideas.

---

## When to Run This Skill

Trigger this skill when:
- The weekly research brief has been completed
- Someone asks "What should the channel make this week?"
- Someone asks "Give me video ideas based on the research"
- A content planning session is starting

---

## Inputs Required

Before generating ideas, load all 4 sources:

1. **Weekly research brief** (`research/weekly-briefs/`, create this folder as briefs are produced): YouTube outliers, hot X conversations, ICP language captured, content gaps
2. **Mauro's content ideas backlog** (`research/ideas/`, create as ideas accumulate): his own priority list of topics, systems to document, and ICP beliefs to break. Always cross-reference before generating; don't suggest something he has already planned or deprioritised.
3. **ICP profile** (`brand/audience.md`): who the viewer is, the 5 segments, and what they're struggling with
4. **Positioning + business context** (`brand/positioning.md`, `brand/business-context-answers.md`): the three content pillars, the belief the channel breaks, and the 15 stories the ICP tells themselves

---

## Idea Generation Framework

For each idea generated, the following must be answered. Do not output an idea unless all four are complete.

### 1. Core Angle
What is the specific contrarian claim, reframe, or insight this video is built on? Not the topic: the angle. The angle is the specific take that makes this video worth watching over every other video on the same topic.

**Wrong:** "How to use AI for content"
**Right:** "Why hiring a VA to post for you failed, and what a measured AI engine run off your real client work does differently"

The angle should feel like something only someone who runs the engine daily for a real agency can credibly claim.

### 2. Target Viewer
Who specifically is this video for? Be precise. Use the segments and language bank from `brand/audience.md`.

- Are they the burned-out-on-outreach operator whose referrals just cracked?
- Are they the time-starved solo operator wearing every hat?
- Are they the wants-authority believer who needs the how?
- Are they the reluctant introvert who won't show their face?

**State the viewer in one sentence:** "This is for a decade-in agency owner whose referral pipeline dried up last quarter and who has never once posted about their own work."

### 3. Why It Will Perform
Ground the performance prediction in evidence from the research brief. Reference:
- Which YouTube outlier it echoes (same topic, different angle)
- Which X conversation it responds to or amplifies
- Which ICP pain point it directly addresses
- Whether it fills a content gap competitors are missing

Do not predict performance based on gut feel. Every performance claim should point to something observed in the research.

### 4. One-Line Hook
Write the hook as a declarative statement, not a question. This should work as both the video's opening line and a short-form teaser. It should create mild anxiety in the right viewer: they should feel they might be making this mistake.

Per `brand/voice.md`, never open the hook with "Most brands..." or "Most people...". Use a direct challenge, a personal example, or a specific scenario instead.

**Examples of correctly styled hooks:**
- "You've built the inbound machine for every client you have. You never built your own."
- "If your pipeline is referrals plus cold email, you don't have a pipeline. You have a hope."
- "I ran my agency's content through a VA for six months. Here's exactly why it produced nothing."

---

## Output Format

Produce ideas in ranked order: highest priority first. Rank by the following weighted criteria:

**Priority 1: High conversion potential (likely to drive inbound)**
- Topic directly addresses a pain point of an established agency owner
- The viewer will self-identify as Mauro's ICP
- Watching it nudges them toward Mauro's offer or DMs

**Priority 2: Authority building**
- Demonstrates the real running engine: original systems, real measurement, real outputs
- Competitor channels cannot match the operational specificity
- Builds Mauro's position as the operator who actually runs this daily

**Priority 3: Growth / reach**
- Broad enough to attract new viewers who may not know Mauro
- Timely: tied to a recent model release, tool change, or hot conversation
- High search or discovery potential

---

### Idea Output Template

```
IDEA #[N]: [Short working title]
Priority: [1 / 2 / 3]
Source: [Which research signal triggered this: outlier video, X conversation, content gap, ICP language]

Core Angle:
[1-2 sentences. The specific claim or reframe this video makes.]

Target Viewer:
[1 sentence. Precise ICP description.]

Why It Will Perform:
[2-3 sentences. Ground in research evidence.]

One-Line Hook:
"[Declarative hook, no question, no 'most brands' opener.]"
```

---

## How Many Ideas to Generate

- **Minimum output:** 5 ideas
- **Typical output:** 7-9 ideas
- Always produce at least 2 Priority 1 ideas (inbound-driving topics)
- Always produce at least 1 Priority 3 idea (reach / growth play)

---

## Cross-Channel Fit Check

Before finalising the idea list, run this check on each idea:

1. **Is this already on the channel?** If Mauro has covered this topic in the last 90 days, skip it unless the angle is clearly differentiated.
2. **Can Mauro back this with real work?** His credibility comes from the engine he actually runs. If the angle requires claims he cannot support from real, running systems, downgrade or cut it.
3. **Is the hook specific enough?** A hook that could come from any AI-content creator is not distinctive enough. The hook should only make sense coming from an operator running a measured engine for a real agency.
4. **Does it pass the established-operator filter?** Ideas that target beginners or freelancers hunting cheap prompts are lower priority unless they serve a deliberate volume play (reach). The core viewer runs a real agency.

---

## Routing After This Skill

Once ideas are approved:
- Pass the chosen idea to `skills/youtube/youtube-title-generator.md` to generate title variations
- Pass the chosen idea to `skills/youtube/youtube-hook-script.md` to write the full script
- Log any ICP language pulled from the research brief back into the language bank workflow for `brand/audience.md`

---

## High-Priority Idea Categories

These categories map to the three pillars in `brand/positioning.md` and the belief inventory in `brand/business-context-answers.md`. When in doubt, suggest from these before inventing new angles.

**1. Engine walkthroughs (highest priority: main conversion driver)**
Full builds and walkthroughs of the systems Mauro actually runs: the transcript-to-content pipeline, the skills library, lead magnet production, the weekly acquisition analysis, moving from skills to agents. Show the real thing on screen.

**2. ICP belief-breaking videos**
Pull directly from the 15 stories in `brand/business-context-answers.md`, for example:
- "My work is too custom to systematize or hand to AI"
- "AI content looks generic and will cheapen my brand"
- "I don't have time to build systems, I'm too busy doing the work"
- "Cold email and outbound is just better than content"
- "Why post at all if I can rely on referrals?"
- "I didn't start posting three years ago, so I'm cooked now"

**3. Cobbler's children**
Build your own inbound engine, the one you already build for clients. Turning delivery work into content. Why agencies that crush lead gen for clients starve their own pipeline.

**4. Anti-cringe authority**
Posting as the expert without the guru ick. Faceless and AI-friendly formats for owners who won't go on camera. What separates operator content from guru content.

**5. Low-time system + proof it converts**
The hour-a-day version. Leading indicators so owners don't quit at week three. Tying content to booked calls instead of vanity metrics.

**6. Tool-specific tutorials**
Claude setups, skills, agents, and workflows applied to agency content and acquisition. Near-zero competition at the operator level; most coverage is beginner prompt content.

**7. Result case studies**
What produced a specific confirmed outcome (like the $28k deal off X), broken down as a system, not a brag. Numbers need Mauro's sign-off before publishing.

---

## Anti-Patterns

- **Never generate a generic topic idea.** "How to use AI for your agency" is not an idea, it is a category. The angle is the idea.
- **Never generate more than one idea on the same topic.** If the brief surfaces multiple signals pointing to the same topic, pick the strongest angle.
- **Never base performance predictions on the topic alone.** Base them on the specific research signals observed this week.
- **Never write hooks as questions.** The style is declarative. Hook questions are off-brand.
- **Never write hooks that open with "Most brands..." or "Most people..."** Per `brand/voice.md`, that opener is banned.
- **Never suggest formats.** This skill generates ideas, not formats. Format decisions happen in the script skill.
- **Never ignore the content gap.** If competitors are overdoing a topic, the best play is often to attack the gap next to it, not to compete head-on.
- **Never pitch to beginners.** Reframe beginner-level questions into expert stances for the established operator.
