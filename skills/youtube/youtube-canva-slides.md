# YouTube Canva Slides — Lorenzo Pravatà Style
**Version 2.1 | Updated 30 March 2026**

---

## Required Reading
Before generating any article, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. Every output must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

This skill file defines how to design slide and screen content that pairs with Lorenzo Pravatà's speaking style. It is built entirely from analysis of his transcripts — specifically the moments where he explicitly describes what is on screen, narrates screen content aloud, or references visuals while speaking. Use this when producing Canva slides, screen layouts, or visual assets to accompany his scripts.

---

## Step 0 — Surface What's Already Available

Before requesting the script or building any slides, check what already exists for this video. Output what's found. Then ask for what's still needed.

### 1. Check for an existing script

```bash
ls /Users/mauro/growthub-os/scripts/
grep -rli "[topic keyword]" /Users/mauro/growthub-os/scripts/
```

If a script exists: note the file path and confirm it's the right version before proceeding.
If no script exists: flag this — the script must come from `skills/youtube-hook-script.md` before slides can be built.

### 2. Check for existing visual references for this topic

```bash
grep -rli "[topic keyword]" /Users/mauro/growthub-os/research/transcripts/lorenzopravata/
```

Look for any moments in Lorenzo's existing videos where he has shown slides, dashboards, or visual elements on this topic. These are the reference points for what to put on screen.

### 3. Output a pre-build summary

```
PRE-BUILD CHECK: [VIDEO TITLE / TOPIC]
----------------------------------------
Script status: [Found at scripts/[filename] / Not yet written]
Existing visual references found:
- [Source file] — [What visual Lorenzo showed for this topic]

Assets Lorenzo will need to supply:
- [Screenshot / dashboard / ad creative / data table — based on topic]

Blockers before slides can be built:
- [Missing script / missing screenshots]
```

### 4. Request what's still needed

After the summary, ask:

> "Here's where we are. [State what exists and what's missing.] Paste the script to proceed, and let me know which screenshots Lorenzo can supply now vs. later."

Wait for the script before building any slide output.

---

## How His Screen Content Relates to His Speech

Lorenzo's screen content and speech are tightly coupled. He does not use slides as a backdrop — they are the evidence for what he is saying. But the relationship is specific: **he speaks slightly ahead of or simultaneously with what appears on screen, never behind it.**

The pattern is: he makes a claim verbally, then the visual confirms or illustrates it in the same breath. The viewer hears the idea and sees the proof at the same moment.

**From the transcripts:**

- When introducing his spend figures: *"You can see here how much we spent in the last six months. You can see here the overview from Meta. We spent $47 million in the last 180 days."* — the Meta Business Manager dashboard is on screen as he reads the numbers aloud. He narrates what is visible. The slide is not explaining something he already said — it is the simultaneous proof.

- When showing the Creative Strategy Map: *"First I wanted to show you why creative diversity matters in 2026 especially after Andromeda... so if two ads are similar they'll have the same entity ID and that means that Meta says that their system will treat the creatives as the same entity sharing the learning and delivery which will likely limit your ability to reach new audience cohorts like two ads like these for example are similar."* — as he says "like two ads like these," the similar-looking ads are displayed on screen. He names what he is showing.

- When building the map in Miro: *"First we will start on a mirror with the four buyer personas and I will build the whole creative strategy map. The first thing, as we said, you have to do is deciding the product you're focusing on."* — the screen shows him actively building the map as he narrates.

**Key principle:** His slides exist to prove, not to summarise. They are shown at the moment of maximum relevance, not after he has explained the idea.

---

## Slide Timing Patterns

Based on how Lorenzo narrates screen content, the following timing patterns are consistent:

**New visual appears when:**
1. He introduces a named section or framework — the visual confirms the framework name or structure
2. He references a specific example — the example appears on screen as he describes it
3. He cites a number — the screenshot or data source appears immediately
4. He transitions with "let me show you" or "I'm going to show you an example" — this is a direct cue that the screen is about to change
5. He plays a video ad example — the ad starts playing while he narrates from above or goes silent to let the ad speak

**Slide stays on screen while:**
- He elaborates on a point that the visual illustrates — sometimes 30–60 seconds on one screen
- He is walking through a framework step by step — the full map or structure stays visible while he points to different parts

**Slide changes before or as he says:**
- "So let's look at..." — immediate visual change
- "Here you can see..." — visual already present or appears simultaneously
- "For example..." — example appears on screen as he begins describing it

**He never changes slides pre-emptively.** He does not have slides that appear before he has introduced the topic. The visual follows from the verbal — never leads it.

---

## What Goes On Screen vs What He Says

This is the most important distinction for slide design in his style.

**On screen: the specific data, the concrete example, the framework map.**
**In speech: the interpretation, the principle, the reason it matters.**

They are not the same information. The screen shows facts. The voice adds meaning.

**Examples from the transcripts:**

| What he says | What is on screen |
|---|---|
| "We um have an ad spend of $46 million uh for our clients" | Meta Business Manager dashboard showing $46M figure |
| "So if two ads are similar they'll have the same entity ID" | Two similar-looking ad creatives displayed side by side |
| "So here's what the creative strategy map looks like" | A Miro board or structured map with buyer personas, angles, awareness levels |
| "This one has 49% rate, 267,000 ad spend, and generated 590K" | Ad performance data — likely Meta Ads Manager or reporting dashboard |
| "Here you can see an example" [plays ad] | The actual ad video playing |
| "This is what it looks like in the studio but then actually in the ad it looks like this" | Split: studio BTS shot on one side, final ad creative on the other |

**Rule for slide design:** If Lorenzo has said it verbally in full detail, the slide should show a visual that is more specific or more concrete than his words — a screenshot, a number, a framework map, an ad example. The slide should not just repeat his words in bullet points.

**Text on slides is minimal.** He narrates. The slides do not need to carry the explanation.

---

## Visual Structure Observations

From Lorenzo's transcript descriptions of what he is showing, the following patterns about his visual design can be inferred:

**He uses Miro for frameworks.** Multiple references to building the Creative Strategy Map "on a mirror" (Miro). The maps are visual, node-based, and appear to use a connected structure — buyer personas branch into pain points, which branch into awareness levels, which branch into angles and formats. Not a table. A map.

**He uses Meta Business Manager screenshots for credibility.** Every video includes at least one screenshot of Meta's dashboard showing spend figures. These are unedited — the real interface with real numbers. They appear early in the video.

**He shows ad examples inline.** He plays short clips of actual ads — both his own client work and third-party examples (Feels Good protein bar brand, JumpSpeak, Rise mushroom coffee). These are not screenshots — they are video clips played directly in the video.

**Studio BTS vs final ad.** In Video 4 (5 formats), he shows a side-by-side: the studio setup (raw environment) and the same ad as it looks when exported. This before/after format is a pattern he uses to explain production quality.

**He uses labels/text overlays on screen to name frameworks.** When he walks through the Creative Strategy Map, labels for "buyer persona," "pain point," "awareness level," "angle," "format" are visible on the Miro board. These are not narrated from slides — they are the labels on the live working document.

**He references what is visually obvious without describing it.** He says *"like two ads like these for example are similar"* — he does not describe the ads. The visual does the work. His narration just points.

---

## Core Slide Rules

These five rules override any other design instinct. Apply them to every slide in every video.

### Rule 1 — One declarative sentence per slide
Every slide carries exactly one statement. Not a topic label. Not a bullet list. Not a question. A declarative sentence that makes a claim.

**Wrong:** "Entity ID"
**Wrong:** "Why entity ID matters"
**Right:** "Meta assigns similar ads the same entity ID — and treats them as one creative."

The sentence should be the thing Lorenzo is proving or asserting at that moment, written as if it's a fact being displayed, not a heading for what he's about to explain.

### Rule 2 — 1 slide per 7–10 seconds of speaking
A 12–14 minute video = 80–100 slides. Not 19. Not 30. Slides change constantly. This is not a lecture deck — it is a visual rhythm that matches the pace of spoken content.

If a slide stays on screen for more than 15 seconds, it is either a framework diagram (intentional hold) or a proof screenshot being narrated (also intentional). Everything else rotates every 7–10 seconds.

**Practical implication:** For every sentence Lorenzo speaks, there is likely a corresponding slide. Script the slides sentence by sentence, not section by section.

### Rule 3 — Every slide text works without Lorenzo speaking
Read any slide in isolation. It should make complete sense as a standalone statement — not depend on the audio to be understood.

**Test:** If you muted the video and read the slides like a scroll, would the argument still hold? It should. This is the VSL deck principle applied to YouTube.

**Wrong:** "Here's the problem:" (depends on speech for meaning)
**Right:** "Most brands are running 50 ads that Meta sees as 3." (complete on its own)

### Rule 4 — Text first, visual second
Write the slide text first. Then decide what image, graph, or screenshot supports it. The text is the claim. The visual is the evidence or illustration. Never start with the visual and work backwards.

**The hierarchy:**
1. What is the statement? → Write it.
2. Is there visual evidence that makes it more concrete? → Add it below or behind.
3. Does the visual already exist (screenshot, data, ad example)? → Use it. If not, the text alone is enough.

### Rule 5 — Framework diagrams only when introducing a named concept
The only time a complex visual (map, diagram, multi-node framework) is appropriate is when Lorenzo introduces a named framework for the first time — e.g. "Creative Strategy Map," "Awareness Levels," "Entity ID." That introduction slide can be more complex. Every slide before and after it should follow Rules 1–4.

Do not build a diagram to explain something that can be stated in a sentence.

---

## Slide Pattern Library (VSL-Derived)

These are the slide patterns to pull from. Each has a defined text structure and a defined visual treatment.

**Pattern A — Bold Problem Statement**
Text: Short declarative claim about what's broken. 8–12 words max.
Visual: None, or dark background. The statement is the slide.
> "Most brands confuse volume with diversity."

**Pattern B — Proof Slide**
Text: The claim, followed by the number or data point.
Visual: Screenshot of Meta dashboard, ad manager, or reporting tool — shown simultaneously as he reads the number.
> "We managed $46 million in ad spend in the last 180 days."

**Pattern C — Reframe**
Text: The thing everyone believes, then the correction.
Visual: None needed. Two lines — wrong assumption, then right framing.
> "More ads ≠ more reach."
> "More entities = more reach."

**Pattern D — Definition**
Text: Term being defined, then one-sentence definition.
Visual: Optional — diagram only if the concept has a visual structure (e.g. a flow).
> "Entity ID: the identifier Meta uses to group similar creatives together."

**Pattern E — Named Framework Diagram**
Text: Framework name at top.
Visual: The framework structure — nodes, tiers, or map. Labels only, no explanatory text inside nodes.
Use only once per named concept. Subsequent references return to Pattern A or B.

**Pattern F — Example Slide**
Text: What the example proves, in one sentence.
Visual: The actual ad, screenshot, or data — takes most of the frame.
> "This street interview ad hit 49% hook rate on $267K spend."

**Pattern G — Contrast Slide**
Text: Two short lines — the wrong approach vs the right one.
Visual: Optional side-by-side if visual contrast is available.
> "Iteration: extracts more from the same audience."
> "Diversity: unlocks audiences you haven't reached."

---

## Canva Slide Templates by Section Type

### Hook Slide (Opening)

Purpose: Establish the contrarian problem statement visually the moment he says it.

**Design:**
- Single line of large text — the core provocative claim. No more than 10 words.
- Dark or high-contrast background — this is not a soft intro. It should feel like a statement.
- No logo in the first frame (or logo in corner only, very small). The claim is the hero.
- No bullet points. No subheads. Just the statement.

**Example text for slide:**
- "Most brands are invisible to the algorithm."
- "Their ads look like ads."
- "Meta doesn't reward good ads anymore."

**Font style:** Bold, clean sans-serif. Large. Left-aligned or centred. Not decorative.

---

### Problem Setup Slide

Purpose: Show the mechanism of the problem — why the thing he just claimed is true.

**Design:**
- Diagram or side-by-side comparison — e.g. two similar ads with "Same Entity ID" label
- OR a screenshot with an annotation or highlight box
- Short explanatory caption under the visual — maximum 1 line
- Text is secondary. The visual carries the proof.

**What goes on screen here:**
- Meta's published documentation on entity IDs (screenshot with key text highlighted)
- Two ad creatives placed side by side with a label showing they share an entity ID
- A graph or chart showing scale ceiling effect

**Do not use:** Bullet-pointed explanations of the problem. Those are spoken. The slide shows the evidence.

---

### Framework / Concept Slide

Purpose: Introduce the named framework or structure he is about to walk through.

**Design:**
- The framework name in large text at the top — e.g. "Creative Strategy Map"
- A visual representation of the structure below: nodes, columns, or tiers — not a list
- Each layer clearly labelled: Product → Buyer Persona → Pain Point → Awareness Level → Angle → Format
- Minimal colour — 2 to 3 colours maximum. One for the framework container, one for active node being discussed, one for text.

**Key design rule:** The framework visual should be legible as a whole — the viewer should be able to see the full structure — but as Lorenzo narrates each part, that part should be visually foregrounded (highlighted, circled, or zoomed in).

**What the Miro map appears to look like, based on transcript narration:**
```
[Product Name]
    └── Buyer Persona 1 (e.g. Research Rabbit Hole First-Time Mom)
            Pain Point: Overwhelmed by research, doesn't know what to trust
            └── Unaware: [Angle idea]
            └── Problem Aware: [Angle idea]
            └── Solution Aware: [Angle idea]
            └── Product Aware: [Angle idea]
    └── Buyer Persona 2
            ...
```

Nodes are connected, not in a table. The map expands as he builds it.

---

### Step-by-Step Slides

Purpose: Walk through a process — e.g. how to build the creative strategy map, how to structure a street interview script.

**Design:**
- One step per slide, or one highlighted step in a persistent step list
- The persistent step list stays on screen as a sidebar or column — the active step is highlighted or bold, the others are muted
- Each step label is 3 to 6 words maximum
- The main content area shows the example or screenshot for that step

**Step labels should look like Lorenzo's verbal language:**
- "Decide your product" (not "Step 1: Product Selection")
- "Map your buyer personas"
- "Add awareness levels"
- "List angles for each level"
- "Prioritise with a star"

**Do not number steps explicitly on screen** unless he explicitly numbers them in speech. He rarely does.

---

### Example / Case Study Slide

Purpose: Show a real example — a client result, a specific ad, a performance stat.

**Design:**
- If showing an ad creative: the ad takes most of the frame. No decoration around it.
- If showing performance data: the data interface (Meta Ads Manager) is shown as a screenshot. Key numbers are highlighted with a simple box or colour highlight.
- If showing a concept (e.g. buyer persona for a supplement brand): the Miro map section is shown zoomed in with the relevant persona visible.

**Text overlay rule:** The only text on screen is labels that identify what is being shown — e.g. "49% Hook Rate | $267K Spent | $590K Revenue." These are factual labels, not commentary.

**Lorenzo's narration style on examples:** He reads the numbers aloud as they appear. *"As you can see here, this one has 49% rate, 267,000 ad spend, and generated 590K."* The slide shows the exact numbers. He reads them. This is intentional — it is confirmation, not redundancy.

---

### CTA Slide

Purpose: Convert high-spend viewers to book a call.

**Design:**
- Clean. Simple. Minimal.
- One or two lines of text:
  - Line 1: "Spending 50k/month on Meta?"
  - Line 2: "Book a call with Lorenzo → [link or 'link in description']"
- Optional: a headshot of Lorenzo — simple, direct eye contact
- No aggressive design, no countdown timers, no FOMO tactics. He does not use hype in his CTAs.

**Tone of the CTA slide:** It should feel like a professional offer, not a sales push. The language he uses verbally — *"you can book a call with me, we can take a look at what you do and I give you some tips"* — should be reflected in the slide's low-pressure framing.

---

## Copywriting Rules for Slides

These rules define how text should be written when it does appear on screen.

1. **Headlines only, never full sentences.** If it is a concept label: 3 to 6 words. If it is a claim: 6 to 10 words. Never a paragraph.

2. **No complete bullet-pointed explanations.** He explains in speech. If bullets appear, they are labels only — single words or short noun phrases. Not full sentences.

3. **Numbers appear verbatim.** If the number is $46 million, the slide says "$46 million" — not "~$46M" or "46 Million Dollars." He reads numbers directly from the screen. Accuracy matters.

4. **Framework labels use his exact terminology.** Slides should use:
   - "Buyer Persona" (not "Target Audience" or "Avatar")
   - "Awareness Level" (not "Funnel Stage")
   - "Angle" (not "Hook Idea" or "Messaging Direction")
   - "Format" (not "Creative Type")
   - "Entity ID" (when relevant to Andromeda content)
   - "Creative Strategy Map" (capital letters — it is a named framework)

5. **Text on screen is only there when it earns its place.** If Lorenzo is going to say it clearly in speech, do not put it on screen as well. Only put text on screen when it adds something the voice cannot — a number, a label, a framework name, a data point.

6. **No corporate slide language.** No "Key Takeaways:" or "In Summary:" or "Objective:" labels. These are not keynote slides. They are evidence, maps, and examples.

7. **Avoid decorative text effects.** No gradient text, no animated word reveals, no text shadows. Clean, readable, direct.

---

## Anti-Patterns

These are slide design choices that would look and feel wrong for Lorenzo's style.

- **Bullet-point heavy slides.** His content is not a lecture deck. Slides that look like PowerPoint presentations from a business school — full paragraphs, numbered lists, headers and subheads — are wrong for his format.

- **Slides that pre-summarise what he is about to say.** He does not use "agenda slides" or "in this section we will cover..." slides. The video flows. No road-mapping slides mid-video.

- **Branded overlays that obscure the actual content.** His credibility comes from showing real tools, real data, real ads. A heavily branded Canva frame that hides the Meta dashboard behind a logo and gradient is wrong.

- **Stock imagery.** He shows real things — his Miro maps, his clients' ads, the Meta interface, his studio. Stock photos of people looking at laptops or abstract business imagery are completely off-brand.

- **High-energy ad-style design.** Bright colours, starburst shapes, exclamation points, "LIMITED TIME" energy. His visual style is calm and credible — not hype.

- **Text that duplicates his speech word-for-word.** If the slide just says what he is saying, it adds nothing. The visual channel should add different information — proof, specificity, structure — not just subtitle his narration.

- **Fonts that signal casualness or personality.** He is authoritative. No handwritten fonts, no playful typefaces. Clean, modern, professional sans-serif only.

- **Multiple concepts on one slide.** When he moves to a new idea, the visual changes. Do not try to put the whole framework on one dense slide. Break it across multiple slides as he builds it, matching his pacing.
