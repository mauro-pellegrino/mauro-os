# YouTube Title Generator
**Version 3.0 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

Generates YouTube titles for Mauro's channel in 3 steps: extract the mechanism from outlier titles, map it to the video topic, rebuild it with the angle only Mauro can credibly claim. Every title serves two permanent goals (see below): reach and conversion.

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md.

---

## Step 0: Surface What's Already Known

Before generating any titles, surface all existing title references, competitor examples, and approved directions already on file for this topic. Output first, then ask for additional context.

### 1. Search existing research and skill files

```bash
grep -rli "[topic keyword]" /Users/mauro/mauro-os/research/
grep -ni "[topic keyword]" /Users/mauro/mauro-os/skills/youtube/youtube-title-generator.md
```

Extract from matches:
- Any competitor titles on this topic already saved in the Reference Table or research files
- Any approved directions already listed in this skill for this topic
- Any outlier titles from the weekly brief that overlap with the topic

### 2. Output a title knowledge summary

```
WHAT'S ALREADY ON FILE: [TOPIC] TITLES
----------------------------------------
Competitor titles found:
- "[title]" | Mechanism: [mechanism name]

Approved directions already listed:
- "[title]" | Why it works: [note]

Outlier titles from weekly brief:
- "[title]" | Channel: [channel name]

Mechanisms most applicable to this topic:
- [Mechanism name], because [reason]
```

### 3. Request additional context

After the summary, ask:

> "That's what's already on file for this topic. Anything to add before I generate titles? For example: a specific result to anchor on, a number to use, or a title direction you already have in mind."

Wait for the response before generating titles.

---

## When to Run This Skill

- A video idea has been chosen and needs a title
- Someone asks "give me titles for this video"
- Running the weekly research brief and converting outlier titles into versions for Mauro's channel

---

## Two Permanent Goals

Every title must serve both of these simultaneously. They are not optional and do not change video to video.

**Goal 1: Qualified views**
Attract established agency owners (mid six figures a month and up) whose pipeline is referral- and outreach-dependent and who want AI content and acquisition systems installed. A title that pulls in beginners or prompt-hunters but not this group is a failure. A title that pulls in this group at scale is a win.

**Goal 2: Audience conversion**
Move the existing audience toward Mauro's offer. Every video is also a sales asset. Titles that signal depth, proof, and a real running system build the trust that eventually turns viewers into inbound leads.

When evaluating any title, ask: does this make the owner of a real, established agency stop scrolling? If yes, it passes. If it reads as beginner content or generic AI-tips advice, it fails.

---

## Title Philosophy

These four principles override any other instinct when writing titles.

**1. Reach over voice**
Titles should aim for maximum reach among the right people, not necessarily reflect Mauro's conversational voice. If a format (lowercase, casual, list-style) reaches more of the right audience, use it. The video earns the voice. The title earns the click.

**2. Validate against a competitor outlier**
Before finalising a title, find the closest competitor title that outperformed its channel average on the same topic. Extract the mechanism. Adapt it. Do not write in a vacuum.

**3. Add the angle only Mauro can claim**
The mechanism is borrowed. What makes it Mauro's is the angle only he can credibly back:
- He runs the AI content and acquisition engine for a real B2B agency, daily, and measures it against booked calls
- He builds the actual systems (skills library, agents, lead magnets, weekly analysis loop), and hands over the real goods
- He's honest about the messy middle, which the audience is starving for
- His belief: the best content doesn't look like content

A competitor can use "How to post more on LinkedIn." Mauro's version is "The AI system that turns one client call into a week of content." The running system is the sauce.

**4. Use placeholders when numbers aren't confirmed**
Never invent a specific number. If the result hasn't been confirmed, use a placeholder:
- `$[X]k deal` or `[X] booked calls` (not an invented figure)
- `[X] posts in [X] minutes` for time-compression contrast

Placeholders are swapped for real numbers, with Mauro's sign-off, before the video goes live. If no real number is available, switch to a mechanism that doesn't require one.

---

## Inputs Required

1. **The video topic / angle**: one sentence describing what the video covers
2. **The weekly research brief**: the outlier titles to analyse (from `skills/research/weekly-research.md` output)
3. **Credential numbers**: specific numbers available to use (see below)

---

## Credential Numbers

Use these in titles whenever a number claim is made. Never invent numbers, and get Mauro's sign-off before any of them goes public.

| Credential | Detail |
|---|---|
| The agency he runs | About $300k/mo |
| Organic contribution | At least a third of that revenue comes from the organic accounts he manages |
| Deal closed off X | $28k |
| The engine | Runs daily for a real B2B agency, measured weekly against booked calls |
| Systems built | Full skills library, lead magnets, articles, long-forms, moving toward agents |
| Specific results | Pull from `brand/social-proof/` (create as results come in) or the video brief |

If the video is a case study of a specific result, that result is the number. Use it exactly: odd specificity ($28k) outperforms round numbers ($30k).

---

## Step 1: Extract the Mechanism from Outlier Titles

Before writing any title, analyse the outlier titles from the weekly brief. For each one, identify which tension mechanism makes it work. There are 8 mechanisms. The examples below are illustrative patterns for Mauro's lane; replace them with real outliers from the research as the reference table fills in.

### The 8 Mechanisms

**1. Number Contrast**
Two numbers set against each other. The gap between them is the entire hook. No explanation needed.
- *[X] hours of content work a week to [X] minutes a day*
- *0 inbound leads to [X] booked calls in 90 days*
- Works for: before/after system stories, time-saved breakdowns, pipeline turnarounds

**2. Oddly Specific Proof**
A non-round number signals real data, not a made-up claim. Specificity does the credibility work.
- *The $28k deal that came from one X post*
- Works for: case studies, real results videos. Fails for: conceptual videos with no hard number.

**3. Credential Anchor**
The scale of what you run leads the title. The number establishes who Mauro is before the viewer reads the rest.
- *The AI content engine behind a $300k/mo agency (step by step)*
- Works for: strategy overviews, methodology videos, anything where the running system is the draw. Fails for: narrow tactical videos where the tactic is the draw.

**4. Belief-Breaker**
The title contradicts something the viewer currently believes. Creates mild friction: they either agree and click, or disagree and click.
- *AI content isn't cheapening your brand. Your process is.*
- *Referrals are not a pipeline*
- Works for: ICP belief-breaking videos, contrarian takes. Fails for: tutorials where the mechanism is the draw.

**5. Named Format or Mechanism**
The specific system or format is the subject. Viewer clicks to learn the named thing before their competitors do.
- *The transcript-to-content pipeline*
- *AI lead magnets: the asset that books calls while you deliver*
- Works for: system tutorials, named frameworks. Fails for: general "use AI" content with no named concept.

**6. Platform / Technical Problem**
Names the specific technical problem the viewer is experiencing. Viewer recognises their situation.
- *Why your LinkedIn posts get 12 impressions*
- *Why Claude writes generic content for you (and the fix)*
- Works for: timely platform/tooling content, troubleshooting videos. Fails for: evergreen strategy content.

**7. Speed Compression**
A time frame that makes the result feel achievable. Compresses the timeline to create urgency.
- *A week of agency content in [X] minutes*
- *How to set this up in one afternoon*
- Works for: system builds with a clear timeline, quick tactical videos. Fails for: slow-burn strategy content where speed isn't the point.

**8. Process Transparency**
Shows the work rather than claiming expertise. "Full system", "step by step", "my exact setup": positions Mauro as a practitioner, not a teacher.
- *My exact Claude setup for agency content (full walkthrough)*
- *I run this every Monday. Here's the whole system.*
- Works for: deep-dive tutorials, full walkthroughs, anything where behind-the-scenes access is the value. Fails for: short punchy belief-breaker content.

---

## Step 2: Map the Mechanism to the Video Topic

Not every mechanism is equally strong for every topic. Use this table as a starting point, not a constraint. Any mechanism can work for any topic if executed correctly.

| Video type | Strongest mechanisms |
|---|---|
| Result case study (a deal, a booked-call run) | Number Contrast, Oddly Specific Proof, Speed Compression |
| System overview / methodology | Credential Anchor, Process Transparency, Named Mechanism |
| Tool or workflow tutorial (Claude setup, transcript pipeline, lead magnets) | Named Mechanism, Process Transparency, Speed Compression |
| Belief-breaking / contrarian | Belief-Breaker, Number Contrast |
| Platform or tooling change | Platform/Technical Problem, Belief-Breaker |
| Consistency / time problem | Belief-Breaker, Speed Compression, Number Contrast |
| Tactical how-to | Process Transparency, Named Mechanism, Speed Compression |

Pick the top 2 mechanisms that fit the topic. Write at least 3 title variations per mechanism. Then validate each against the reference table. If no competitor has outperformed on this mechanism for this topic, reconsider.

---

## Step 3: Rebuild for Mauro's Channel

### Voice Rules

**Do:**
- Lead with the result or the system. If the video has a confirmed number, it goes in position 1 or 2.
- Use "My" or "I": personal ownership of the system or result.
- Keep it under 10 words before any parenthetical. Count them.
- Use the parenthetical for specificity: a number, a system name, a time frame, a tool name.
- Use lowercase when the tone is conversational. Not every title needs title case.
- Name the tool. "Claude", not "AI". "X" and "LinkedIn", not "social media".
- Let the gap do the work in contrast titles.

**Don't:**
- No "dark truth", "hidden", "exposed", "secret", "glitch": theatrical language.
- No "Here's why / Here's what / Here's how": YouTube filler.
- No round numbers when you have a real one. $28k beats $30k every time.
- No invented numbers. Use a placeholder (`$[X]k`, `[X] calls`) until the real figure is confirmed and signed off.
- No adjectives that don't add information: "ultimate", "complete", "powerful", "game-changing".
- No explaining the insight in the title. The title creates curiosity. The video delivers the answer.
- No questions. Statements outperform questions for this audience.

### Parenthetical Rules

The parenthetical is for specificity, not punchlines.

Good parentheticals:
- `(step by step)`: process signal
- `(full walkthrough)`: depth signal
- `(with the actual prompts)`: hand-over-the-goods signal
- `(2026)`: timeliness signal
- `($28k deal)`: proof signal, once signed off

Bad parentheticals:
- `(you need to see this)`: theatrical
- `(everyone's missing this)`: theatrical
- `(this changes everything)`: theatrical
- `(it's not what you think)`: theatrical

---

## Reference Table: Competitor Title → Mechanism → Mauro Version

[TO BE REBUILT: this table is populated from outlier titles collected by `skills/research/weekly-research.md` for Mauro's lane (AI systems for agency owners). Log each validated outlier here as research accumulates.]

| Competitor title | Mechanism | Mauro version |
|---|---|---|
| *(log outliers here as the weekly research finds them)* | | |

---

## Approved Direction Examples

[TO BE REBUILT: this list holds titles from Mauro's shortlist once he approves directions for the new lane. Use them as calibration for tone, mechanism, and angle. Starter directions consistent with the positioning, pending Mauro's approval:]

| Title direction | Why it could work |
|---|---|
| *The AI content engine behind a $300k/mo agency (step by step)* | Credential anchor plus process transparency. Only someone actually running the engine can make this video. Number needs sign-off. |
| *You build inbound for clients. Here's how to build yours.* | The cobbler's children pillar stated as a direct challenge. Speaks only to real agency owners. |
| *How I turn one client call into a week of content with Claude* | Named mechanism plus speed compression. Concrete, operational, low-competition. |
| *AI lead magnets that book calls (with the actual prompts)* | Named mechanism plus hand-over-the-goods parenthetical. |
| *Personal branding without the cringe (a system, no face required)* | Hits the ICP's stated fear directly (cringe, being on camera). |
| *The $28k deal that came from one X post* | Oddly specific proof. His own result. Needs sign-off before use. |

---

## Output Format

### Generate titles

For each mechanism selected in Step 2, write 3-5 title variations. Label each clearly.

```
MECHANISM: [Mechanism name]

1. [Title]
2. [Title]
3. [Title]
```

### Shortlist

After generating all titles, pick the top 5. For each one, note in one line why it works and one line where it could fail.

```
TOP 5

1. [Title]
   Works because: [one line]
   Fails if: [one line]

2. [Title]
   ...
```

### Recommendation

State the single recommended title with a one-sentence reason.

```
RECOMMENDED: [Title]
Why: [one sentence, specific to the video topic and Mauro's channel]
```

---

## Anti-Patterns

- Never write a title with a round number when an oddly specific one is available.
- Never use theatrical language ("dark truth", "hidden", "exposed", "secret").
- Never write more than 10 words before the parenthetical. Count them.
- Never use the parenthetical for a punchline. Use it for a fact.
- Never recommend a title that any generic AI-tips channel could have written. The angle must be visible: a real system, a confirmed number, or a perspective only someone running the engine can claim.
- Never write a question title.
- Never explain the insight in the title. If the title gives away the answer, rewrite it.
- Never produce fewer than 6 title variations across at least 2 mechanisms.
- Never use an invented specific number. Use a placeholder (`$[X]`, `[X] calls`) and note that it needs Mauro's confirmation before the video goes live.
