# YouTube Canva Slides: Mauro's Channel
**Version 3.0 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

---

## Required Reading
Before generating any slide output, read `brand/voice.md` and `brand/audience.md` in full. Every output must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md.

---

This skill file defines how to design slide and screen content that pairs with the spoken script for Mauro's videos. The rules below are proven long-form patterns for narrated slide videos. Use this when producing Canva slides, screen layouts, or visual assets to accompany a script.

[CALIBRATE: as Mauro's own videos accumulate in `research/transcripts/maurojpelle/`, extract how he actually narrates screen content and adjust the timing and phrasing assumptions below to match.]

---

## Step 0: Surface What's Already Available

Before requesting the script or building any slides, check what already exists for this video. Output what's found. Then ask for what's still needed.

### 1. Check for an existing script

```bash
ls /Users/mauro/mauro-os/brand/scripts/
grep -rli "[topic keyword]" /Users/mauro/mauro-os/brand/scripts/
```

(`brand/scripts/`: create this folder when the first script is saved.)

If a script exists: note the file path and confirm it's the right version before proceeding.
If no script exists: flag this. The script must come from `skills/youtube/youtube-hook-script.md` before slides can be built.

### 2. Check for existing visual references for this topic

```bash
grep -rli "[topic keyword]" /Users/mauro/mauro-os/research/transcripts/maurojpelle/
```

Look for any moments in Mauro's existing videos where he has shown slides, dashboards, or visual elements on this topic. These are the reference points for what to put on screen.

### 3. Output a pre-build summary

```
PRE-BUILD CHECK: [VIDEO TITLE / TOPIC]
----------------------------------------
Script status: [Found at brand/scripts/[filename] / Not yet written]
Existing visual references found:
- [Source file]: [What visual was shown for this topic]

Assets Mauro will need to supply:
- [Screenshot / dashboard / example post / data table, based on topic]

Blockers before slides can be built:
- [Missing script / missing screenshots]
```

### 4. Request what's still needed

After the summary, ask:

> "Here's where we are. [State what exists and what's missing.] Paste the script to proceed, and let me know which screenshots you can supply now vs. later."

Wait for the script before building any slide output.

---

## How Screen Content Relates to Speech

Screen content and speech are tightly coupled. Slides are not a backdrop: they are the evidence for what is being said. The relationship is specific: **speak slightly ahead of or simultaneously with what appears on screen, never behind it.**

The pattern: make a claim verbally, then the visual confirms or illustrates it in the same breath. The viewer hears the idea and sees the proof at the same moment.

**Examples of the pattern in Mauro's lane:**

- Introducing proof: "here's the booked-calls tracker from the last quarter" while the actual tracker or analytics dashboard is on screen. Narrate what is visible. The slide is not explaining something already said; it is the simultaneous proof.
- Introducing a system: "this is the exact skill file that writes the first draft" while the real file is on screen, scrolled to the relevant section.
- Showing an output: "and this post came straight out of that pipeline" while the actual X or LinkedIn post is displayed.

**Key principle:** slides exist to prove, not to summarise. They are shown at the moment of maximum relevance, not after the idea has been explained.

---

## Slide Timing Patterns

**New visual appears when:**
1. A named section or system is introduced: the visual confirms the name or structure
2. A specific example is referenced: the example appears on screen as it's described
3. A number is cited: the screenshot or data source appears immediately
4. The script says "let me show you" or "I'm going to show you an example": a direct cue that the screen is about to change
5. A screen recording or demo plays: it starts while the narration continues above it or goes silent to let it speak

**Slide stays on screen while:**
- A point the visual illustrates is being elaborated, sometimes 30-60 seconds on one screen
- A framework or system map is being walked through step by step: the full structure stays visible while different parts are pointed to

**Slide changes before or as the script says:**
- "So let's look at...": immediate visual change
- "Here you can see...": visual already present or appears simultaneously
- "For example...": example appears on screen as the description begins

**Never change slides pre-emptively.** No slide appears before its topic has been introduced. The visual follows from the verbal, never leads it.

---

## What Goes On Screen vs What Gets Said

This is the most important distinction for slide design.

**On screen: the specific data, the concrete example, the system map.**
**In speech: the interpretation, the principle, the reason it matters.**

They are not the same information. The screen shows facts. The voice adds meaning.

**Examples:**

| What the script says | What is on screen |
|---|---|
| "A third of the agency's revenue comes from the organic accounts I manage" | The analytics or revenue dashboard showing the figure [needs Mauro's sign-off before use] |
| "This is the transcript-to-content pipeline" | The pipeline map: transcript in, posts/articles/long-forms out |
| "This one post turned into a $28k deal" | Screenshot of the actual post plus the DM or call booking that followed |
| "Here's what a week of output looks like" | The content calendar or scheduled-posts view |
| "This is the skill that does it" | The actual skill file open on screen |

**Rule for slide design:** if the script says it verbally in full detail, the slide should show a visual that is more specific or more concrete than the words: a screenshot, a number, a system map, a real output. The slide should not just repeat the words in bullet points.

**Text on slides is minimal.** The narration carries the explanation. The slides do not need to.

---

## Visual Structure Conventions

**Miro for frameworks.** System maps and frameworks are built as visual, node-based maps with a connected structure, not tables. See `skills/youtube/miro-design-system.md` and `skills/youtube/youtube-miro-board.md`.

**Real dashboards for credibility.** Proof screenshots are unedited: the real interface with real numbers (X analytics, booked-calls tracker, the actual repo, Claude running). They appear early in the video. Any specific number shown needs Mauro's sign-off.

**Real outputs shown inline.** Actual posts, articles, lead magnets, and DMs are shown as they exist, not mocked up.

**Before/after.** Side-by-side of the old way vs the system output (for example: a blank calendar vs a scheduled week) is a recurring proof format.

**Labels on the live working document.** When walking through a system map, the labels are on the actual Miro board or file, not narrated from separate slides.

**Point at what is visually obvious without describing it.** "Like these two, for example" while the examples are on screen. The visual does the work; the narration just points.

---

## Core Slide Rules

These five rules override any other design instinct. Apply them to every slide in every video.

### Rule 1: One declarative sentence per slide
Every slide carries exactly one statement. Not a topic label. Not a bullet list. Not a question. A declarative sentence that makes a claim.

**Wrong:** "Content engine"
**Wrong:** "Why a content engine matters"
**Right:** "One client call contains a week of content. You're deleting it."

The sentence should be the thing being proven or asserted at that moment, written as a fact being displayed, not a heading for what's about to be explained.

### Rule 2: 1 slide per 7-10 seconds of speaking
A 12-14 minute video = 80-100 slides. Not 19. Not 30. Slides change constantly. This is not a lecture deck: it is a visual rhythm that matches the pace of spoken content.

If a slide stays on screen for more than 15 seconds, it is either a framework diagram (intentional hold) or a proof screenshot being narrated (also intentional). Everything else rotates every 7-10 seconds.

**Practical implication:** for every sentence spoken, there is likely a corresponding slide. Script the slides sentence by sentence, not section by section.

### Rule 3: Every slide text works without the audio
Read any slide in isolation. It should make complete sense as a standalone statement, not depend on the audio to be understood.

**Test:** if you muted the video and read the slides like a scroll, would the argument still hold? It should.

**Wrong:** "Here's the problem:" (depends on speech for meaning)
**Right:** "Your agency posts less than your worst client." (complete on its own)

### Rule 4: Text first, visual second
Write the slide text first. Then decide what image, graph, or screenshot supports it. The text is the claim. The visual is the evidence or illustration. Never start with the visual and work backwards.

**The hierarchy:**
1. What is the statement? → Write it.
2. Is there visual evidence that makes it more concrete? → Add it below or behind.
3. Does the visual already exist (screenshot, data, real output)? → Use it. If not, the text alone is enough.

### Rule 5: Framework diagrams only when introducing a named concept
The only time a complex visual (map, diagram, multi-node framework) is appropriate is when a named system is introduced for the first time, for example "the content engine" or "the transcript-to-content pipeline." That introduction slide can be more complex. Every slide before and after it follows Rules 1-4.

Do not build a diagram to explain something that can be stated in a sentence.

---

## Slide Pattern Library

These are the slide patterns to pull from. Each has a defined text structure and a defined visual treatment.

**Pattern A: Bold Problem Statement**
Text: short declarative claim about what's broken. 8-12 words max.
Visual: none, or dark background. The statement is the slide.
> "Your pipeline is referrals plus hope."

**Pattern B: Proof Slide**
Text: the claim, followed by the number or data point.
Visual: screenshot of the real dashboard, tracker, or analytics, shown simultaneously as the number is read. Numbers need sign-off.
> "One post. One $28k deal."

**Pattern C: Correction**
Text: the thing everyone believes, then the correction, stated directly (no "it's not X, it's Y" phrasing; see `brand/voice.md`).
Visual: none needed. Two lines.
> "Posting more didn't fix it."
> "A measured system did."

**Pattern D: Definition**
Text: term being defined, then one-sentence definition.
Visual: optional. Diagram only if the concept has a visual structure (a flow, a pipeline).
> "Content engine: the system that turns your real client work into scheduled, measured content."

**Pattern E: Named System Diagram**
Text: system name at top.
Visual: the structure: nodes, tiers, or map. Labels only, no explanatory text inside nodes.
Use only once per named concept. Subsequent references return to Pattern A or B.

**Pattern F: Example Slide**
Text: what the example proves, in one sentence.
Visual: the actual output, screenshot, or data, taking most of the frame.
> "This whole week came from one Tuesday call."

**Pattern G: Contrast Slide**
Text: two short lines, the wrong approach vs the right one.
Visual: optional side-by-side if visual contrast is available.
> "VA posting: activity."
> "Measured engine: booked calls."

---

## Canva Slide Templates by Section Type

### Hook Slide (Opening)

Purpose: establish the contrarian problem statement visually the moment it's said.

**Design:**
- Single line of large text: the core provocative claim. No more than 10 words.
- Dark or high-contrast background. This is not a soft intro. It should feel like a statement.
- No logo in the first frame (or logo in corner only, very small). The claim is the hero.
- No bullet points. No subheads. Just the statement.

**Example text for slide:**
- "You built everyone's inbound machine but yours."
- "Referrals are not a pipeline."
- "Your content isn't failing. It doesn't exist."

**Font style:** bold, clean sans-serif. Large. Left-aligned or centred. Not decorative.

---

### Problem Setup Slide

Purpose: show the mechanism of the problem, why the claim just made is true.

**Design:**
- Diagram or side-by-side comparison, for example: the client's full content calendar next to the agency's own empty one
- OR a screenshot with an annotation or highlight box
- Short explanatory caption under the visual, maximum 1 line
- Text is secondary. The visual carries the proof.

**What goes on screen here:**
- A real (anonymised) example of the pattern being described
- Two artifacts side by side with a label showing the gap
- A simple chart showing the trend (pipeline over time, posts vs booked calls)

**Do not use:** bullet-pointed explanations of the problem. Those are spoken. The slide shows the evidence.

---

### Framework / Concept Slide

Purpose: introduce the named system or structure about to be walked through.

**Design:**
- The system name in large text at the top, for example "The Content Engine"
- A visual representation of the structure below: nodes, columns, or tiers, not a list
- Each layer clearly labelled, for example: Source (calls, delivery work) → Extraction → Drafting → Human pass → Publish → Measure (booked calls)
- Minimal colour: 2 to 3 colours maximum. One for the container, one for the active node being discussed, one for text.

**Key design rule:** the framework visual should be legible as a whole (the viewer sees the full structure), but as each part is narrated, that part is visually foregrounded (highlighted, circled, or zoomed in).

---

### Step-by-Step Slides

Purpose: walk through a process, for example how to set up the transcript-to-content pipeline.

**Design:**
- One step per slide, or one highlighted step in a persistent step list
- The persistent step list stays on screen as a sidebar or column: the active step is highlighted or bold, the others muted
- Each step label is 3 to 6 words maximum
- The main content area shows the example or screenshot for that step

**Step labels should sound spoken, not corporate:**
- "Record the call" (not "Step 1: Source Acquisition")
- "Pull the insights"
- "Draft with the skill"
- "Do the human pass"
- "Schedule and measure"

**Do not number steps explicitly on screen** unless the script explicitly numbers them in speech.

---

### Example / Case Study Slide

Purpose: show a real example: a real output, a real result, a real system running.

**Design:**
- If showing an output (post, article, lead magnet): the output takes most of the frame. No decoration around it.
- If showing performance data: the real interface is shown as a screenshot. Key numbers are highlighted with a simple box or colour highlight. Numbers need sign-off.
- If showing a system: the actual file, board, or terminal, zoomed to the relevant section.

**Text overlay rule:** the only text on screen is labels that identify what is being shown, for example "1 call → 9 posts → 3 booked calls [confirm numbers]". Factual labels, not commentary.

**Narration style on examples:** read the key numbers aloud as they appear on screen. The slide shows the exact numbers, the voice reads them. This is confirmation, not redundancy.

---

### CTA Slide

Purpose: convert qualified viewers (established agency owners).

**Design:**
- Clean. Simple. Minimal.
- One or two lines of text:
  - Line 1: "Run an established agency?"
  - Line 2: [CTA: define once Mauro's offer exists. Placeholder: "Follow @maurojpelle / grab the linked resource"]
- Optional: a headshot of Mauro, simple, direct eye contact
- No aggressive design, no countdown timers, no FOMO tactics. No hype in CTAs.

**Tone of the CTA slide:** a professional offer, not a sales push. Low-pressure framing that matches the spoken close.

---

## Copywriting Rules for Slides

These rules define how text should be written when it does appear on screen.

1. **Headlines only, never paragraphs.** A concept label: 3 to 6 words. A claim: 6 to 12 words. Never a paragraph.

2. **No complete bullet-pointed explanations.** Explanation happens in speech. If bullets appear, they are labels only: single words or short noun phrases.

3. **Numbers appear verbatim.** If the number is $28k, the slide says "$28k", exactly as spoken. Numbers are read directly from the screen. Accuracy matters, and every public number needs Mauro's sign-off.

4. **System labels use Mauro's exact terminology.** [CALIBRATE: lock the canonical names for Mauro's systems as they get named on camera. Current working names: "content engine", "skills library", "transcript-to-content pipeline", "Monday acquisition analysis", "lead magnet", "agents".] Use the same name everywhere; never rename a system between videos.

5. **Text on screen is only there when it earns its place.** If the narration says it clearly, do not put it on screen as well. Only add text that the voice cannot carry: a number, a label, a system name, a data point.

6. **No corporate slide language.** No "Key Takeaways:" or "In Summary:" or "Objective:" labels. These are not keynote slides. They are evidence, maps, and examples.

7. **Avoid decorative text effects.** No gradient text, no animated word reveals, no text shadows. Clean, readable, direct.

---

## Anti-Patterns

These are slide design choices that would look and feel wrong for the channel.

- **Bullet-point heavy slides.** This is not a lecture deck. Slides that look like business-school PowerPoint (full paragraphs, numbered lists, headers and subheads) are wrong for the format.

- **Slides that pre-summarise what's about to be said.** No "agenda slides" or "in this section we will cover..." slides. The video flows. No road-mapping slides mid-video.

- **Branded overlays that obscure the actual content.** Credibility comes from showing real tools, real data, real outputs. A heavily branded frame that hides the actual dashboard behind a logo and gradient is wrong.

- **Stock imagery.** Show real things: the real repo, real posts, real dashboards, Claude actually running. Stock photos of people at laptops are completely off-brand.

- **High-energy ad-style design.** Bright starbursts, exclamation points, "LIMITED TIME" energy. The visual style is calm and credible, never hype.

- **Text that duplicates the speech word-for-word.** If the slide just says what is being said, it adds nothing. The visual channel should add different information: proof, specificity, structure.

- **Fonts that signal casualness or personality.** The register is authoritative. No handwritten fonts, no playful typefaces. Clean, modern, professional sans-serif only.

- **Multiple concepts on one slide.** When the script moves to a new idea, the visual changes. Do not put a whole framework on one dense slide. Break it across multiple slides as it gets built, matching the pacing.

- **Fabricated visuals.** Never mock up a fake dashboard, fake DM, or fake result. If the real asset doesn't exist yet, use a labelled placeholder and flag it for Mauro to supply.
