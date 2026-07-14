# YouTube Hook & Script: Mauro's Channel
**Version 2.0 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

---

## Required Reading
Before generating any script, read `brand/voice.md` and `brand/audience.md` in full. Every output must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP defined in audience.md, and mirror its language bank.

---

## Step 0: Surface What's Already Known (run this before writing)

Before writing a single line of script or requesting any inputs, surface everything already on file about the topic. Output it first. Then ask for additional context.

### 1. Search existing research

```bash
grep -rli "[topic keyword]" /Users/mauro/mauro-os/research/
grep -rli "[topic keyword]" /Users/mauro/mauro-os/brand/
```

For each matching file, read it and extract:
- How the topic has already been covered and which angles were used
- Any data, numbers, or results already captured
- Any ICP language or direct quotes pulled from real agency owners (see the language bank in `brand/audience.md`)
- What competitors have said and where their coverage ends (the gap Mauro can own)

### 2. Output a knowledge summary

Output this before requesting anything:

```
WHAT'S ALREADY ON FILE: [TOPIC]
--------------------------------
Source: [filename]
- [Finding: data point, angle, ICP quote, or competitor coverage]

COMPETITOR COVERAGE:
- [Competitor] covered [angle] in [video ID]. Gap they left: [what they didn't say]

DATA AVAILABLE:
- [Numbers, results, or benchmarks already on file]

ICP LANGUAGE CAPTURED:
- "[exact quote from transcript or audience research]"

GAPS: WHAT'S STILL NEEDED BEFORE SCRIPTING:
- [Specific data, result, or context that's missing]
```

### 3. Request additional context

After the summary, ask:

> "That's everything already on file. What do you want to add before I start the script? For example: specific results, angles you want to push, new data not yet in the research, or competitor videos to pull first."

Wait for the response before writing anything.

### When a competitor transcript is still needed

[MONITORED CHANNELS: to be defined for Mauro's lane, AI systems for agency owners.] Once the monitored-channel list exists, if one of them has covered this topic and the transcript is not yet saved locally, flag it in the gaps section. After receiving the additional context response, fetch and save the transcript if requested:

1. Find the video URL
2. Fetch transcript using the YouTube MCP tools
3. Save to `research/transcripts/[channel-handle]/[video-id].md`
4. Read before scripting

### What to request when specific data is still missing after context is given

First check `brand/social-proof/` (create this folder as results come in) for any existing results on this topic before asking:
```bash
ls /Users/mauro/mauro-os/brand/social-proof/
```

| Data type | Where to look first | What to ask if not found |
|---|---|---|
| Result / proof point | `brand/social-proof/` (create as results come in) | "Which result do you want to anchor this on?" |
| System performance | `research/transcripts/` + brand session notes | "What numbers has the engine actually produced for [system]?" |
| Mauro's angle | `brand/positioning.md`, `brand/business-context-answers.md` | "What do we know about this topic that nobody else is teaching?" |

**Rule:** Never paste unconfirmed numbers into the script directly. Use placeholders. Real numbers are for Mauro to confirm on camera or in review before the video goes live.

---

This skill file defines how to write YouTube video scripts for Mauro's channel. The audience is established agency owners (mid six figures a month and up) who want AI content and client-acquisition systems installed, per `brand/audience.md`. The structural rules below are proven long-form patterns. The voice layer must come from Mauro's own recordings.

[CALIBRATE: extract Mauro's actual speaking patterns from his own video transcripts in `research/transcripts/maurojpelle/` as they accumulate. Every section below marked CALIBRATE needs verbatim source material from those transcripts before it can be treated as settled voice.]

---

## The Opening Formula

Open every video with the same structural sequence. Tight, fast, no wasted sentences.

**The pattern (3-part open):**

1. **Contrarian problem statement.** A claim that challenges what the viewer currently believes about content, AI, or client acquisition, phrased as fact, not question. It should make the right viewer feel they might be making this mistake.
2. **Stakes anchor.** A credibility point tied to Mauro's own work that legitimises the claim before he explains it (see Credibility Anchors below).
3. **Video road map.** One or two sentences that state exactly what he will show: "I'm going to show you / walk you through / share."

**The opening formula written as a template:**

```
[Contrarian claim about what the viewer is getting wrong.]
[Why this is happening / what it costs them.]
[Credibility anchor: what I've built / run / measured.]
So in this video, I'm going to show you [specific promise of what the viewer will get].
```

Never open with a question. Never "have you ever wondered." Lead with a declarative sentence.

[CALIBRATE: pull 3-4 verbatim openings from Mauro's own videos once recorded, and store them here as the reference examples.]

---

## Sentence Rhythm & Pacing

The target register is spoken thought captured directly, not polished broadcast English. That naturalness is intentional.

**Structural rules that hold regardless of speaker:**

- **Short sentences establish the point. Longer sentences explain it.** Drop a two-to-five word punch, then expand with a longer explanatory run.
- **Repeat the core idea in different words.** Saying the same thing two or three ways before moving on is spoken emphasis, not redundancy.
- **Lists are spoken, not bullet-pointed.** Run list items together the way a person talks, connected with "and" and "then," not read as a numbered list.
- **Write in run-on spoken sentences, not tight copy.** Include the occasional self-correction or elaboration. Scripts that sound too clean don't sound human on camera.

[CALIBRATE: Mauro's filler words, breath words, and connector habits must come from his own transcripts. Do not import another speaker's verbal tics.]

---

## Transition Phrases

Use plain, functional transitions to move between sections: introducing a section, introducing an example, summarising before moving on, acknowledging what's being skipped, softening a strong claim, flagging something important.

[CALIBRATE: build the verbatim transition-phrase bank from Mauro's own transcripts. Until then, keep transitions simple and unmannered: "First thing to understand is...", "Let me show you an example...", "So as a summary...", "One thing that matters here is...".]

---

## Credibility Anchors

Do not open with credentials. Drop proof points inside the first 90 seconds, woven into context, never foregrounded as bragging.

**Mauro's anchor material (his own results):**
- He architected and runs the AI content and acquisition engine for the agency he runs (about $300k/mo)
- At least a third of that agency's revenue comes from the organic accounts he manages
- He closed a $28k deal off X
- He ties content to booked calls and runs a weekly acquisition analysis
- He built a full skills library and is moving from skills toward agents

**Sign-off rule:** any specific number used publicly (revenue, calls per week, reach) needs Mauro's sign-off before the video goes live. Draft with the anchor in place, flag it for confirmation, and use a bracket placeholder if it isn't confirmed.

**How to introduce anchors:**
- Never "I'm an expert because..." The number appears as context inside an explanation: "everything I'm going to show you is based on the engine I run every week for a real agency."
- Pair the number with a qualifier that makes it specific and credible, not inflated: "just from the organic accounts I manage," "just in the last 90 days."
- Show the proof on screen simultaneously (dashboard, analytics, booked-calls tracker). The spoken line and the visual proof happen together.

---

## Signature Language Patterns

[CALIBRATE: extract Mauro's recurring phrases, register, and word choices from his own video transcripts. Do not invent a signature vocabulary for him.]

Until that bank exists, follow these defaults from `brand/voice.md` and `brand/business-context-answers.md`:

- Plain, direct English. One idea per line.
- Specific tool names: "Claude," not "AI tools." Name the actual platform, skill, or file.
- Operator-to-operator register: expert speaking to a sophisticated peer, never teacher to beginner.
- "The best content doesn't look like content" is an existing belief of Mauro's and safe to use.
- Hand over the actual goods: real prompts, real steps, real numbers (confirmed ones), no gatekeeping.

---

## Teaching Style

Teach through structured examples, not through named proprietary systems.

**The pattern: Principle → Why it matters → Example → What to do.**

Introduce an idea as something broken or wrong in how it's commonly done first. Then explain why. Then show what you do instead. Then give a specific example from the actual engine (a real skill, a real post, a real week of output).

**Real examples, anonymised where needed:** reference "a B2B agency I run this for" or "one deal that came through X" without naming clients. Never name a client.

**Narrate through screen content simultaneously.** When showing a system, describe what is on screen as you point to it. Spoken content and screen content stay tightly synchronised: don't pre-empt what's on screen and don't lag behind it.

**Numbered steps:** use numbers implicitly in speech ("first," "then," "and then," "the other thing") rather than "Step 1, Step 2." The structure is implied, not formally labelled.

**Teaching register:** a practitioner teaching from what he runs daily, not an educator teaching from theory. "This is what I actually run every week" is the trust layer. Be honest about the messy middle; that honesty is the brand.

---

## How to Close

Closings follow a consistent 3-part structure:

1. **Brief recap in 1-2 sentences.** Pull back to the top-level point.
2. **Call to action for qualified viewers.** The audience filter is established agency owners. [CTA: define once Mauro's offer exists. Until then, default to: "If you run an established agency and want this system, follow @maurojpelle on X / grab the linked resource." Confirm the current CTA with Mauro before recording.]
3. **Community invitation + next video tease.** Invite comments or DMs on X, optionally mention a related video, then sign off.

**Closing rules:**
- Never hard-sell. Frame any CTA as low-commitment: "take a look," "have a chat," "grab this."
- The qualifier (established agency owners, not beginners) appears in every close. It is the audience filter.
- Acknowledge that not everyone will act: "and if not, drop your questions in the comments."

[CALIBRATE: capture Mauro's natural sign-off phrasing from his own recordings.]

---

## Script Template

Replace bracketed placeholders. Keep the rhythm spoken, not polished.

```
[CONTRARIAN OPENING STATEMENT about what the viewer is getting wrong. Declarative, not a question.]
And that's the main reason why [consequence for agency owners who do this].
So in this video, I'm going to show you [specific promise: what they will walk away knowing or able to do].

[CREDIBILITY ANCHOR, woven in naturally.]
Everything I'm going to show you here is based on [what you run / built / measured, e.g. the AI content engine I run every week for a real agency].

[FIRST SECTION: introduce the core concept]
First thing to understand is [core concept].
[Explain why it matters, 3 to 5 sentences.]
[Give a specific example from the engine, a client situation (anonymised), or a real week of output.]

So what you need to do is [the solution or approach].

[SECOND SECTION: the system, workflow, or method]
[Name of the system or approach] basically [explain what it does or why it works].
The main thing here is [key principle].
[Walk through it step by step using "first," "then," "and then," not "Step 1, Step 2."]
[Include a specific example: a real skill file, a real prompt, a real output.]

[THIRD SECTION: common mistakes]
One problem I keep seeing is [common mistake].
A lot of agency owners [describe the mistaken behaviour].
[Explain why it doesn't work / what it costs them.]

[FOURTH SECTION: what to do instead, with examples]
What I'd do instead is [your approach].
Something I see working very well is [specific tactic or system].
[Give an example, ideally with a confirmed number or a bracket placeholder.]
And that gets you [outcome for the viewer].

[CLOSING RECAP, 1 to 2 sentences max]
So as a summary, [restate the core idea].

[CTA]
[Qualified-viewer CTA per the How to Close section. Placeholder until Mauro's offer exists.]
If you have any questions or you'd like me to cover something else in the next video, let me know in the comments or send me a message on X.
[Sign-off.]
```

---

## Anti-Patterns (What Never Goes in a Script)

- **Never open with a question.** No "Have you ever wondered why..." or "Are you struggling with..." Open with a statement.
- **Never use hype adjectives.** No "revolutionary," "game-changing," "incredible," "amazing." Credibility comes from real work, not adjectives.
- **Never over-produce the language.** Slightly imperfect, slightly run-on spoken prose. Scripts that sound too clean sound like AI.
- **Never lead with credentials.** Embed proof in context rather than opening with "I am Mauro, I run..." Authority is earned through the work shown.
- **Never present a single approach as the only answer.** Hedge honestly where it's true: "that depends," "in general," "for most agencies at this level." Respect complexity.
- **Never give advice without tying it back to what actually ran.** Ground advice in "this is what I run" or "this is what the engine produced."
- **Never end without the qualified-viewer CTA.** Every video has it, always framed as a conversation or a resource, never a hard sale.
- **Never say "in today's video."** Standard YouTube intro language is banned.
- **Never name-drop competitors disparagingly.** Reference other people's content as examples to learn from, not to mock.
- **Never speak to beginners.** The viewer runs a real agency. Reframe beginner questions into expert stances.
- **Never open with "Most brands..." or "Most people..."** This is documented in `brand/voice.md` Pattern #3 and applies to scripts equally. It is one of the most common AI writing tells. Replace with a direct challenge, a personal example, or a specific scenario. Wrong: *"Most agencies posting more content are fixing the wrong thing."* Right: *"If you've doubled your posting volume and your pipeline still looks the same, you're fixing the wrong thing."*
- **Never use the "that's not X, it's Y" reframe construction.** Sentences like "That's not a content problem. That's a system problem." are a hallmark of AI-generated prose. Make the same point by stating the real cause directly. Wrong: *"That's not a consistency problem. That's a system problem."* Right: *"Consistency isn't why it's failing. You have no system underneath the posting."*
