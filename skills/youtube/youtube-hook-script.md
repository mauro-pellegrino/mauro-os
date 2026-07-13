# YouTube Hook & Script — Lorenzo Pravatà Style
**Version 1.2 | Updated 30 March 2026**

---

## Required Reading
Before generating any script, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. Every output must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

## Step 0 — Surface What's Already Known (run this before writing)

Before writing a single line of script or requesting any inputs, surface everything already on file about the topic. Output it first. Then ask for additional context.

### 1. Search existing research

```bash
grep -rli "[topic keyword]" /Users/mauro/growthub-os/research/
grep -rli "[topic keyword]" /Users/mauro/growthub-os/brands/
```

For each matching file, read it and extract:
- How the topic has already been covered and which angles were used
- Any data, numbers, or client results already captured
- Any ICP language or direct quotes pulled from real customers or transcripts
- What competitors have said and where their coverage ends (the gap Growthub can own)

### 2. Output a knowledge summary

Output this before requesting anything:

```
WHAT'S ALREADY ON FILE: [TOPIC]
--------------------------------
Source: [filename]
- [Finding — data point, angle, ICP quote, or competitor coverage]

COMPETITOR COVERAGE:
- [Competitor] covered [angle] in [video ID] — gap they left: [what they didn't say]

DATA AVAILABLE:
- [Numbers, spend figures, client results, or benchmarks already on file]

ICP LANGUAGE CAPTURED:
- "[exact quote from transcript or customer language]"

GAPS — WHAT'S STILL NEEDED BEFORE SCRIPTING:
- [Specific data, client result, or context that's missing]
```

### 3. Request additional context

After the summary, ask:

> "That's everything already on file. What do you want to add before I start the script? For example: specific client results, angles Lorenzo wants to push, new data not yet in the research, or competitor videos to pull first."

Wait for the response before writing anything.

### When a competitor transcript is still needed

If a monitored channel (Nick Theriot, Spencer Pawliw, Brando Monetti, Shaun Eng, Ben Heath, Charley T) has covered this topic and the transcript is not yet saved locally, flag it in the gaps section. After receiving the additional context response, fetch and save the transcript if requested:

1. Find the video URL
2. Fetch transcript using the YouTube MCP tools
3. Save to `research/transcripts/[channel-handle]/[video-id].md` following `research/template.md`
4. Read before scripting

### What to request when specific data is still missing after context is given

First check `social-proof/` for any existing client results on this topic before asking:
```bash
ls /Users/mauro/growthub-os/social-proof/
```

| Data type | Where to look first | What to ask if not found |
|---|---|---|
| Client result | `social-proof/` — real numbers stored per client | "Which client result do you want to anchor this on?" |
| Format-specific performance | Research transcripts + `social-proof/` files | "What hook rates / hold rates / CPAs have you seen for [format]?" |
| Growthub angle | `brands/growthub/positioning.md`, `learnings.md` | "What do we know about this topic that nobody else is teaching?" |

**Rule:** Never paste raw numbers from `social-proof/` into the script directly. Use placeholders. The real numbers are for Lorenzo to confirm on camera or in review before the video goes live.

---

This skill file defines how to write YouTube video scripts in Lorenzo Pravatà's exact speaking and structural style. Use it when writing scripts for his channel or producing content that needs to sound authentically like him. Every pattern below is extracted directly from his transcripts — not inferred from general best practices.

---

## Lorenzo's Opening Formula

Lorenzo opens every video with the same structural sequence. It is tight, fast, and never wastes a sentence.

**The pattern (3-part open):**

1. **Contrarian problem statement** — a claim that most brands are doing something wrong, phrased as fact, not question. This immediately signals the video will challenge assumptions.
2. **Stakes anchor** — a credibility number tied to his own spend or data that legitimises the claim before he explains it.
3. **Video road map** — one or two sentences that state exactly what he will show, using "I'm going to show you / walk you through / share."

**Verbatim examples from the transcripts:**

- *"Most brands are testing hundreds of ads while Meta thinks they're running the same ad over and over. And that's the main reason why I see many brands that get stuck at a certain level and they are not able to scale even if they have good ads. So in this video, I'll walk you through how we create a creative strategy map for a client of ours..."*
  — Video 1

- *"The main reason why most brands don't scale as fast as they should is that their ads look like ads. We manage several ad accounts spending over $1 million a month and we see one format that is outperforming everything else... So in this video I'm going to show you what we do to create street interviews and actually scale."*
  — Video 2

- *"Most brands won't scale in 2026. And that's not because of their product. It's because their ads are invisible to the algorithm. Meta doesn't reward the good ads anymore. It rewards creative diversity. And if you don't know how Andromeda works, then you won't be able to scale."*
  — Video 3

- *"The main reason why most brands can scale as fast as they want is that their ads look like ads. We tested more than 10,000 creatives this year. And all the winners had one thing in common. They didn't look like ads."*
  — Video 4

**The opening formula written as a template:**

```
[Contrarian claim about what most brands do wrong.]
[Why this is happening / what it costs them.]
[Credibility anchor: what we've spent / tested / managed.]
So in this video, I'm going to show you [specific promise of what viewer will get].
```

Lorenzo never opens with a question. He never says "have you ever wondered." He leads with a declarative sentence that puts the viewer slightly on the back foot — they already feel they might be making this mistake.

---

## Sentence Rhythm & Pacing

Lorenzo speaks in a specific rhythm that mixes short declarative punches with longer explanatory runs. This is not polished broadcast English — it is spoken thought captured directly, and that naturalness is intentional.

**Key characteristics:**

- **Short sentences establish the point. Longer sentences explain it.** He will drop a two-to-five word punch, then expand with a 30-to-50 word sentence.
- **He repeats the core idea in different words.** He will say the same thing two or three ways before moving on. This is not redundancy — it is his version of emphasis.
- **He uses "so" as a breath word**, not just a connector. "So" signals he is about to land a point or transition the thought.
- **He uses "like" as a filler** but also as a spoken emphasis marker: *"it's like the best way to do this."*
- **He trails unfinished thoughts** that then get corrected or redirected mid-sentence. These appear in the transcripts as natural speech repairs: *"We um have an ad spend of $46 million uh for our clients and uh we have a lot of insights..."* — Write scripts with room for this.
- **Lists are spoken, not bullet-pointed.** He will say: *"the persona you're targeting, the angle, the awareness level they are in, even the sophistication level in especially in some industries and the format you're using and then the actor, the creator."*

**For scripting purposes:** Write in run-on spoken sentences, not tight copy. Include the occasional self-correction or elaboration. Avoid full stops mid-explanation — Lorenzo runs his thoughts together.

---

## Transition Phrases (Verbatim)

These are the exact phrases Lorenzo uses to move between sections, ideas, or levels of explanation. Pull from this list when scripting.

**Moving into a new section:**
- "First thing you have to understand is..."
- "First I wanted to show you..."
- "So in this case..."
- "With that being said then..."
- "So, which formats work best?"
- "Let's also look at another example for..."
- "Now with Andromeda..."
- "Then in terms of [topic]..."
- "Another important part is..."
- "Another one that is working very well for us..."
- "The other thing is..."
- "Then obviously..."

**Introducing an example:**
- "I'm going to show you an example..."
- "Let me show you some examples..."
- "I'll show you a couple of seconds of this one."
- "So I'm going to show you some other winning examples."
- "So for example..."
- "Let's take this one for example."

**Summarising before moving on:**
- "So that's mainly it."
- "So that's all."
- "So as a summary..."
- "So just to recap..."
- "So just like um..."
- "And uh yeah..."
- "Obviously, like..."

**Acknowledging something he is skipping or simplifying:**
- "Obviously there are more but we will show an example with this."
- "Obviously that's pretty obvious, but..."
- "Obviously, there is much more but this gives you an idea."
- "We won't cover all of these um but just a couple of insights."

**Softening a strong claim:**
- "In my opinion..."
- "That's more of experience."
- "In general, I think..."
- "That depends."

**Flagging something important:**
- "One thing that is important is..."
- "One thing that is very important too is..."
- "Something that is very important too is..."
- "Very very important to..."

---

## Credibility Anchors

Lorenzo does not open with credentials. He drops data points in the first 60 seconds of every video, woven into context, not foregrounded as bragging.

**His anchor numbers (pull these for any script in his name):**
- "$46 million in ad spend in the last 180 days" (Videos 1, 3, 4)
- "$94 million in ad spend this year" (Video 5)
- "$90 million managed this year" (Video 4)
- "More than $1 million a month" for individual clients (Videos 2, 5)
- "More than 10,000 creatives tested this year" (Video 4)
- "More than $40 million on testing in the last 6 months" (Video 3)
- Street interview ads "with hook and hold rates above 40%" — specific ad cited: "49% rate, 267,000 ad spend, generated 590K"

**How he introduces these:**
- He never says "I'm an expert because..." — instead the number appears as context: *"Everything I'm going to show you in this video is based on what we see working for our clients in the last six months just for the accounts connected to our business manager because we actually have more. We um have an ad spend of $46 million..."*
- He pairs the number with a qualifier: *"just for the accounts connected to our business manager"* or *"just in the last 180 days."* This makes the number feel more specific and credible, not inflated.
- He shows the number on screen simultaneously (Meta dashboard screenshot) — the spoken line and the visual proof happen together.

**Rule for credibility anchors:** Drop them early (within the first 90 seconds), embed them in explanation rather than presenting them as headlines, and always pair with a qualifier that makes them feel specific.

---

## Signature Language Patterns

These are Lorenzo's recurring word choices, phrases, and verbal patterns. They are identifiable. Any script written in his voice should include several of these.

**Recurring phrases:**
- "...that don't look like ads" — his single most repeated phrase across all 5 videos
- "scale" — used constantly as both noun and verb. "Scale" is his north star word.
- "winning ads" / "winning ad" — distinguishes from ads that run vs. ads that convert at top spend
- "creative diversity" — his core concept, repeated in 4 of 5 videos
- "buyer persona" / "bio persona" — (he pronounces it "bio persona" throughout; this is his consistent usage)
- "awareness levels" — unaware / problem aware / solution aware / product aware / most aware
- "entity ID" — his Andromeda-specific technical term, used to sound specific and current
- "double down" — his phrase for scaling what works
- "unlock new audiences" — his phrase for the benefit of creative diversity
- "looks like an ad" / "doesn't look like ads" — binary framing he returns to constantly
- "educate and entertain" — his formula for what good format ads do
- "hook and hold rate" — his performance metrics language
- "unique mechanism" — his term for the product's core differentiator
- "selling blocks" — his term for organised research insights used to write scripts

**His verbal register:**
- He uses "basically" very frequently as a sentence-opener when simplifying: *"Basically, you have..."*
- He uses "uh" and "um" naturally — do not scrub these from scripts intended to sound like real spoken Lorenzo
- He says "like" in the middle of sentences as emphasis: *"it's like the main thing"*
- He uses "right?" as a trailing confirmation — *"you want to scale, right?"*
- He uses "obviously" often — but never sarcastically, always as a reassurance that what he is saying is reasonable
- He often says "something we see working very well" — note the construction. Not "what works" but "something we see working"

**His Meta-specificity:** He always names the platform specifically — "Meta," never "Facebook," and usually clarifies "Meta (Facebook and Instagram)" only when necessary. He references Andromeda by name as a specific update with specific behaviour.

---

## Teaching Style

Lorenzo does not teach through frameworks with named proprietary systems (he has no "7-step Lorenzo Method"). He teaches through structured examples. His approach is:

**Principle → Why it matters → Example → What to do.**

He almost always introduces an idea as something broken or wrong in how most people do it first. Then he explains why. Then he shows what he does instead. Then he gives a specific example from a client.

**His frameworks are named but simply named:**
- "Creative Strategy Map" — the central framework in Videos 1 and 3
- "Selling Blocks" — how he organises research for scripts
- "Stealth creatives" / "stat creatives" — his category term for non-ad-looking ads
- Awareness levels: unaware → problem aware → solution aware → product aware → most aware

**He teaches with real client examples but anonymises them:**
- *"We use this supplement client"* — not named
- *"We have a mil kit brand"* — not named
- *"Rise"* — named, as a third-party example not his client
- *"JumpSpeak"* — named as a third-party example in the street interview walkthrough

**He narrates through screen content simultaneously.** When showing a creative strategy map, he says: *"The first thing, as we said, you have to do is deciding the product you're focusing on..."* — he describes what is on screen as he points to it. His spoken content and screen content are tightly synchronised. He does not pre-empt what is on screen and does not lag behind it.

**Numbered steps:** He uses numbers implicitly in speech but rarely says "Step 1, Step 2." Instead he uses "first," "then," "and then," "the other thing," "another important part." The structure is implied, not formally labelled.

**Teaching register:** He is a practitioner teaching from results, not an educator teaching from theory. He frequently says "this is based on what we see working" and "this is not theory, this is what actually works for us." He positions himself and his team as the ones with real-world proof.

---

## How He Closes

Lorenzo's closings follow a consistent 3-part structure:

1. **Brief recap in 1–2 sentences** — pulls back to the top-level point.
2. **Call to action for high-spend viewers** — consistently his lead CTA is "if you spend more than 50k a month on Meta, book a call with me." The link is in the description.
3. **Community invitation + next video tease** — invites comments or DMs (Twitter/X), sometimes mentions a related video, ends with "see you in the next."

**Verbatim closing examples:**

- *"If you spend already more than 50k a month on ads on Meta, then I have a link in description. You can book a call with me. We can take a look at what you do and I give you some tips of what you can implement and we can also see if we can help you by creating more ads or improving your creative strategy. If you have any questions on these or you'd like me to show something else in the next videos, just let me know in the comments or send me a message on X and I'll create more content about this. See you in the next video."*
  — Video 1

- *"...you can book a call from the link below. We can have a chat and I can see if we can help you. And um if not like if you have any other questions or anything just add them in the comments and I'll be happy to do another video to show you what we usually do for our clients. See you in the next."*
  — Video 4

- *"I hope this is valuable. This helped us a lot and since we incremented since we implemented a system for creatives, our clients scaled much much more. Um so if you want me to go more into details of specific parts of how to create a script, how to um test new formats uh or anything else, just let me know. I can do another video on that. And if you already spend more than 50k a month on um on the Meta ads, then you can just click the link below and we can uh get on a call and take a look at your account and what you can actually do to scale."*
  — Video 5

**Key closing patterns:**
- He never hard-sells. The CTA is framed as "take a look" or "have a chat" — low commitment language.
- The $50k/month spend qualifier appears in every single video. It is his audience filter.
- "See you in the next" (not "see you in the next video" every time — often just "see you in the next") is his sign-off.
- He occasionally softens the pitch: "if not like if you have any other questions" — he acknowledges not everyone will want to book.

---

## Script Template

This template is written in Lorenzo's actual sentence structure and rhythm. Replace bracketed placeholders.

```
[CONTRARIAN OPENING STATEMENT about what most brands do wrong — declarative, not a question.]
And that's the main reason why [consequence for brands that do this].
So in this video, I'm going to show you [specific promise — what they will walk away knowing or able to do].

[CREDIBILITY ANCHOR — weave in naturally.]
Everything I'm going to show you here is based on [timeframe] of [what you did — e.g. testing, managing, spending].
We [credibility number — spend, creatives tested, clients managed] and uh we have a lot of insights on what is working right now.

[FIRST SECTION — Introduce the core concept]
First thing you have to understand is [core concept].
[Explain why it matters — 3 to 5 sentences.]
[Give a specific example from a client or test.]

So what you need to do is [the solution or approach].

[SECOND SECTION — The framework or format or method]
[Name of the framework or approach] basically [explain what it does or why it works].
The main thing here is [key principle].
[Walk through it step by step using "first," "then," "and then" — not "Step 1, Step 2."]
[Include a specific example — name a product category or use a client example (anonymised).]

[THIRD SECTION — Common mistakes or what most brands do wrong]
One problem we see is that [common mistake].
A lot of brands [describe the mistaken behaviour].
[Explain why it doesn't work / what it costs them.]

[FOURTH SECTION — What to do instead, with examples]
What we usually recommend is [your approach].
Something we see working very well is [specific tactic or format].
[Give an example — ideally reference a real result, a hook rate, a spend number.]
And uh that helps [outcome for the viewer].

[CLOSING RECAP — 1 to 2 sentences max]
So as a summary, [restate the core idea].

[CTA]
If you already spend more than 50k a month on Meta, then I have a link in the description.
You can book a call with me, we can take a look at your account and what you can actually do to scale.
If you have any questions or you'd like me to show something else in the next video, just let me know in the comments or send me a message on X.
See you in the next.
```

---

## Anti-Patterns (What He Never Does)

These are things that would immediately sound off-brand for Lorenzo. Avoid them in any script written in his style.

- **Never opens with a question.** He never says "Have you ever wondered why..." or "Are you struggling with..." — he opens with a statement.
- **Never uses hype adjectives.** He does not say "revolutionary," "game-changing," "incredible," "amazing" (unless quoting what a bad ad sounds like). His credibility comes from data, not adjectives.
- **Never over-produces his language.** He does not write polished, tight copy-style prose. The speech is slightly imperfect, slightly run-on. Scripts that sound too clean do not sound like him.
- **Never credits himself first.** He embeds credentials in context rather than leading with "I am Lorenzo, the founder of..." — he earns authority through data.
- **Never presents a single format or angle as the only answer.** He consistently hedges: "that depends," "in general," "for most brands." He respects complexity.
- **Never gives advice without tying it back to results.** He always grounds advice in "we see this working" or "this is based on what we test."
- **Never ends without the $50k CTA.** Every video has this. It is always framed as a conversation, not a sale.
- **Never says "in today's video."** He does not use standard YouTube intro language.
- **Never name-drops competitors disparagingly.** He references competitor ads as examples to learn from, not to mock.
- **Never skips the awareness level framework.** Once introduced (Video 3 onwards), awareness levels appear in nearly every strategic discussion. Omitting them would feel like a gap.
- **Never opens with "Most brands..." or "Most people..."** This is documented in `brands/growthub/voice.md` Pattern #3 and applies to scripts equally. It is one of the most common AI writing tells and signals immediately that a human didn't write this. Replace with a direct challenge, a personal example, or a specific scenario. Wrong: *"Most brands improving their hooks are fixing the wrong thing."* Right: *"If you've rewritten your hooks and still see 15%, 18% hook rates — you're fixing the wrong thing."*
- **Never uses the "that's not X, it's Y" reframe construction.** Sentences like "That's not a copy problem. That's a format problem." or "That's not a strategy issue — it's a creative issue." are a hallmark of AI-generated prose. They sound like a writing prompt, not a person talking. Lorenzo makes the same point by stating the real cause directly, not by labelling and relabelling. Wrong: *"That's not a copy problem. That's a format problem."* Right: *"The copy isn't why it's failing. Format determines your hook rate before you write a single word."* Or simply: *"Because the copy isn't the problem. The format is."*
