# YouTube Slide Visuals: VA Production Brief Generator
**Version 2.0 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

This skill takes the numbered slide deck output from `skills/youtube/youtube-canva-slides.md` and produces a row-by-row visual production brief for a VA to build the final Canva deck. Every row is specific enough that the VA can execute without asking a clarifying question.

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md.

---

## Step 0: Surface What's Already Available

Before generating any production table, check what already exists. Output what's found. Then ask for the numbered slide list.

### 1. Check for an existing slide list or script

```bash
grep -rli "[topic keyword]" /Users/mauro/mauro-os/brand/scripts/
```

(`brand/scripts/`: create this folder when the first script is saved.)

If a script or slide list exists: confirm the file path before proceeding.
If nothing exists: flag that the slide list must come from `skills/youtube/youtube-canva-slides.md` first.

### 2. Identify which slide types this topic will likely generate

Based on the topic, pre-identify which slide types from the classification system (below) are most likely to appear. This helps the requester know which assets to prepare.

For example, a video on "the AI content engine" will likely generate:
- DIAGRAM-FLOW (the pipeline: call transcript → extraction → drafts → human pass → schedule → measure)
- YELLOW-TEXT (belief-breaking statements)
- OUTPUT-EXAMPLE (real posts, articles, or lead magnets the engine produced, Mauro supplies)
- PROOF-DATA (analytics or booked-calls screenshots, Mauro supplies)

### 3. Output a pre-build summary

```
PRE-BUILD CHECK: [VIDEO TITLE / TOPIC]
----------------------------------------
Slide list status: [Found / Not yet generated]

Slide types likely in this video:
- [Slide type]: [rough count if known]

Assets Mauro will need to supply:
- [Screenshots / real outputs / DMs: what type and how many estimated]
```

### 4. Request what's still needed

After the summary, ask:

> "Paste the numbered slide list from `skills/youtube/youtube-canva-slides.md` and I'll produce the full VA production table."

Wait for the slide list before producing any output.

---

## VA SOP: Read This Before You Open Canva

### Canva Setup

**Slide size:** 1920 × 1080px (16:9 widescreen). Do not use presentation defaults; set this manually under Custom Size.

**Brand colours: add these to your Canva palette before starting.**
This is the working palette for the channel. [CALIBRATE: swap for Mauro's final brand kit once his visual identity is locked.]

| Name | Hex | Use |
|---|---|---|
| Brand Yellow | `#FBBF24` | Yellow statement slide backgrounds |
| Lavender White | `#F9F0FF` | All content slide backgrounds |
| Dark Navy | `#1A1A2E` | Logo block, dark callout boxes |
| Accent Green | `#00D4A1` | Logo mark only |
| Body Black | `#0A0A0A` | All text on yellow and lavender backgrounds |
| White | `#FFFFFF` | Text inside dark callout boxes and dark screenshot overlays |

**Font:** use **Plus Jakarta Sans** throughout (available free in Canva). If unavailable, substitute **Inter** or **DM Sans**. Use Bold weight for all headlines and statement text. Use Medium weight for body description text only.

**Font size hierarchy:**
| Element | Size | Weight | Alignment |
|---|---|---|---|
| Yellow slide statement | 72-80pt | Bold | Centred |
| Section number | 96pt | Bold | Centred |
| Section title | 60pt | Bold | Centred |
| Content slide title | 48pt | Bold | Left |
| Content slide body | 28-32pt | Bold | Left |
| Supporting text / captions | 22-24pt | Medium | Left |
| Dark callout box label | 16pt | Medium | Left |
| Dark callout box body | 22pt | Bold | Left |

**Logos and recurring elements: save these as Canva Brand Kit or as pre-built elements.**
- Logo block: [LOGO: supply when Mauro's brand mark exists. Until then, use a dark navy square (`#1A1A2E`) with "M" in Accent Green as the placeholder mark.] Used bottom-right on cover slide only.
- Profile pill: black rounded rectangle with Mauro's headshot + "@maurojpelle" in white. Used bottom-left on framework and diagram slides.
- Brand label pill: small yellow rounded rectangle (`#FBBF24`) with "ghostedcalls" in black bold. Used bottom-right on diagram slides.
- Yellow horizontal bar: full-width yellow bar at bottom of cover slide. "GHOSTEDCALLS.COM" in bold black, left-aligned inside it. (Confirm the final URL with Mauro before first use.)

---

### How to Import the Starting Point

1. If a `.pptx` file has been provided: open Canva → Import → Upload the `.pptx`. It will create a presentation with all slides pre-populated. Use it as a structural reference only; do not rely on its fonts or colours. Restyle every slide against this production brief.
2. If no `.pptx` exists: start from a blank 1920×1080 Canva presentation and build slide by slide using this brief.
3. Duplicate the blank template before starting so the original is preserved.

---

### Order to Work Through Slides

Work in this order to minimise repeated setup:

1. **Build all yellow slides first**: same background, same font, same layout. Do them as a batch.
2. **Build all section divider slides**: lavender background, number + title only. Quick batch.
3. **Build all text-only content slides** (lavender, no visuals): copy/paste text, adjust size.
4. **Build all diagram slides**: use the diagram specs in each row. Most time-intensive. Do one at a time.
5. **Build all proof/data slides**: placeholder boxes first, then paste screenshots when Mauro provides them.
6. **Build all output-example slides**: placeholder boxes for the real posts, articles, or screenshots Mauro will supply.
7. **Build cover slide last**: it requires the most elements and you will have the brand kit ready by then.

---

### What to Do When an Asset Needs to Come From Mauro

When a row in the production table says **"Screenshot: Mauro supplies"**, do the following:

1. Build the slide with a clearly labelled placeholder box: grey fill, white border, text inside reading `[SCREENSHOT: {description of what goes here}]`.
2. Add a Canva comment on that slide (click the comment icon) describing exactly what Mauro needs to provide. Example: *"Need the X analytics screenshot showing the impressions for the post that led to the $28k deal."*
3. Flag the slide number in the delivery message to Mauro: *"Slides 8, 14, and 22 need screenshots from you. I've left labelled placeholders."*
4. Never use stock imagery as a substitute for a real screenshot. Leave the placeholder.

---

### Final QA Before Delivery

Before sharing the deck:
- [ ] Every yellow slide: `#FBBF24` background, black bold text, centred, no visuals
- [ ] Every content slide: `#F9F0FF` background
- [ ] No slide has bullet points; text is statements, not lists
- [ ] No slide uses decorative fonts, gradients, or text shadows
- [ ] All screenshot placeholders are clearly labelled
- [ ] Font is consistent throughout (Plus Jakarta Sans Bold)
- [ ] Slide count matches the numbered list from the script output

---

## Visual Pattern Rules: How to Determine Each Slide's Design

Before running the production table, the AI uses these rules to classify every numbered slide.

### Rule 1: Background Type

**Use YELLOW (`#FBBF24`) when the slide:**
- Contains a single rhetorical question (e.g. "So why does nobody build this for themselves?")
- Contains a single contrarian statement or problem framing (e.g. "You built everyone's inbound machine but yours.")
- Contains a transitional insight or "so what" conclusion
- Contains a philosophical or belief statement with no supporting visual
- Is a pure verbal punchline: one or two sentences, no diagram needed

**Use LAVENDER WHITE (`#F9F0FF`) when the slide:**
- Is a section number divider
- Contains a framework, diagram, or flow chart
- Contains a proof screenshot or data table
- Contains a real output example (post, article, lead magnet, DM)
- Contains body text with supporting information
- Contains a social proof element (tweet, DM, Slack message)
- Contains a before/after comparison
- Contains a split layout (text left, visual right)
- Is the cover slide or CTA slide

**Never use dark backgrounds** for full slides. Dark is only used for embedded callout boxes within a lavender slide.

---

### Rule 2: Slide Type Classification

Once the background is set, classify the slide into one of these types. The type determines the layout.

| Type | Description | Background |
|---|---|---|
| **COVER** | Title, subtitle, output collage, logo, yellow bar | Lavender White |
| **YELLOW-TEXT** | Single statement or question, centred text only | Yellow |
| **SECTION-DIVIDER** | Large number + section title, centred | Lavender White |
| **TEXT-ONLY** | Multi-line explanation, no diagram, no image | Lavender White |
| **DIAGRAM-FLOW** | Linear or vertical flow chart (pipeline, steps, paths) | Lavender White |
| **DIAGRAM-STAGES** | Horizontal 3-5 stage diagram (e.g. pipeline maturity, funnel stages) | Yellow (diagram sits on yellow bg) |
| **DIAGRAM-FRAMEWORK** | Named system map (Content Engine etc) | Lavender White |
| **PROOF-DATA** | Analytics, booked-calls tracker, revenue dashboard screenshot | Lavender White |
| **OUTPUT-EXAMPLE** | Real outputs shown (posts, articles, lead magnet pages) | Lavender White |
| **SOCIAL-PROOF** | Tweet, DM, Slack screenshot | Lavender White |
| **SPLIT-TEXT-VISUAL** | Left text explanation, right visual (screenshot or example) | Lavender White |
| **DARK-CALLOUT** | Lavender slide with embedded dark box containing a key rule | Lavender White |
| **CTA** | Call to action: minimal, clean, low pressure | Lavender White |

---

### Rule 3: Visual Asset Decision

For each slide, determine the asset needed:

| Situation | Asset type | Source |
|---|---|---|
| Yellow text slide | None, text only | Build in Canva |
| Section divider | None, number + title | Build in Canva |
| Stage diagram | Recreate the coloured multi-stage box diagram | Build in Canva |
| System flow (vertical) | Recreate as rounded box flow chart | Build in Canva |
| Path comparison diagram | Recreate as 2-column box layout | Build in Canva |
| Before/After | Recreate with red BEFORE pill + green AFTER pill | Build in Canva |
| Analytics / revenue / booked-calls proof | Real screenshot from the actual tool | Mauro supplies |
| X or LinkedIn post | Real screenshot of the actual post | Mauro supplies |
| DM / Slack conversation | Real screenshot (anonymise client names) | Mauro supplies |
| Skill file / repo / Claude running | Real screenshot or screen recording frame | Mauro supplies |
| Lead magnet or article page | Real screenshot of the published asset | Mauro supplies |
| Illustration / icon (person, object) | Simple icon from Canva icon library (no stock photos) | Build in Canva |
| Technical diagram (architecture etc) | Recreate as simplified diagram OR use supplied image | Mauro supplies or Build in Canva |

**Stock photography is never used.** If it is not a Canva-built graphic and Mauro cannot supply a real screenshot, the slide gets a placeholder.

---

### Rule 4: The Stage Diagram (Exact Spec)

When a slide requires a horizontal multi-stage diagram (3-5 stages of a process, funnel, or maturity model), build it as follows:

**Background:** full yellow slide (`#FBBF24`)

**Boxes in a row, connected by right-pointing arrows.** Colour each stage in order:
| Stage | Box colour | Text colour |
|---|---|---|
| 1 | Coral/orange `#F97316` | White |
| 2 | Amber `#F59E0B` | Black |
| 3 | Pink/magenta `#EC4899` | White |
| 4 | Teal `#14B8A6` | White |
| 5 | Sky blue `#38BDF8` | Black |

Each box has:
- Rounded rectangle shape
- Stage label in bold caps at top of box
- Description text in smaller regular text below the label (inside or below box)
- A dark/black action label at the very bottom (what to do at this stage)

**Annotations:** if the script highlights a specific stage, add a red hand-drawn circle around that stage's box and a red arrow pointing to it. Canva has a "marker" or "doodle" element for this; use red.

**Bottom-left:** profile pill (black rounded rectangle, Mauro's photo + "@maurojpelle" in white). Size: ~220px wide.

**Bottom-right:** "ghostedcalls" small yellow pill label with black text.

---

### Rule 5: The Dark Callout Box (Exact Spec)

When a slide contains a key rule or principle that needs to stand out:

- Box colour: `#1F2937` (dark charcoal, not pure black)
- Corner radius: 8px
- Padding: 24px inside
- Label text (top): small, medium weight, grey `#9CA3AF`, e.g. "Simple rule to remember"
- Body text: white `#FFFFFF`, bold, 22pt
- Width: ~60% of slide width, centred or positioned in lower half of slide
- The rest of the slide is lavender white with standard body text above

---

### Rule 6: Flow Diagram Colours

When building a vertical process flow (e.g. the content pipeline):
- All boxes: rounded rectangles, amber/orange `#F59E0B`, black text, bold labels
- Connected by downward arrows in dark grey
- Example steps: Record the call → Pull the insights → Draft with the skill → Human pass → Schedule → Measure against booked calls
- Adjust labels to match whatever the script actually calls the steps

When building a horizontal 3-step reasons diagram:
- Box 1: Orange `#F97316`, white text
- Box 2: Amber `#F59E0B`, black text
- Box 3: Pink `#EC4899`, white text
- Connected by right-pointing arrows
- Each box has a smaller description text box below it (lavender background, black text)

When building a "Two Paths" comparison diagram:
- Path 1 box: Orange `#F97316`, black text
- Path 2 box: Amber `#F59E0B`, black text
- Recommendation box: Teal `#14B8A6`, black text
- Result boxes below: Pink `#EC4899`, white text

---

## Production Table Output Format

When this skill is run with a numbered slide list as input, output a production table in this exact format. One row per slide.

```
| # | Slide text (exact, truncated to 15 words if long) | Background | Visual asset needed | Asset source |
|---|---|---|---|---|
| 1 | [text] | Yellow / Lavender White | [exact description] | Build in Canva / Mauro supplies / Text only |
```

**Column 4 (Visual asset needed) must be specific enough that the VA does not need to ask.** Examples of acceptable descriptions:
- "No visual: text only, centred"
- "Vertical amber flow: 6 rounded boxes (Record the call → Pull the insights → Draft with the skill → Human pass → Schedule → Measure) connected by downward arrows, centred."
- "X analytics screenshot showing [specific post's impressions]. Positioned bottom-half of slide. Title above."
- "Screenshot of the actual X post that opened the [$X]k conversation, centred, with light shadow."
- "Dark callout box (#1F2937), label: 'Simple rule to remember', body text: '[exact text]'. Positioned bottom-centre of slide. Body text above in lavender area."
- "Left column (60%): explanation text. Right column (40%): booked-calls tracker screenshot showing [figure, needs Mauro's sign-off]."
- "Before/after split: red BEFORE pill over empty content calendar screenshot, green AFTER pill over the scheduled week."

---

## Example Output (Partial: The AI Content Engine Behind My Agency)

This is what correctly formatted output looks like. Use it as the quality benchmark. Bracketed figures stay as placeholders until Mauro confirms them.

| # | Slide text | Background | Visual asset needed | Asset source |
|---|---|---|---|---|
| 1 | The AI Content Engine Behind a Real Agency | Lavender White | Title bold top-left. Collage of 5 overlapping output screenshots (posts, article, lead magnet), angled. Yellow horizontal full-width bar at bottom with "GHOSTEDCALLS.COM" bold black left. Logo block placeholder bottom-right. | Mauro supplies output screenshots; bar + logo built in Canva |
| 2 | You built everyone's inbound machine but yours | Yellow | No visual: single statement, bold, centred, 2 lines | Text only |
| 3 | Referrals dried up and there was nothing behind them | Yellow | No visual: single statement, bold, centred, 2 lines | Text only |
| 4 | The fix wasn't posting more. It was a system. | Yellow | No visual: single statement, bold, centred | Text only |
| 5 | 1: What the Engine Is | Lavender White | Section divider. "1" in ~96pt bold centred above. Section title in ~60pt bold centred below. | Text only |
| 6 | One client call contains a week of content | Lavender White | Bold title top-centre. Below: split layout, left = transcript file screenshot, right = 5 small post thumbnails produced from it, arrow between. | Mauro supplies screenshots |
| 7 | The pipeline runs in six steps | Lavender White | Vertical amber flow: 6 rounded boxes (Record the call → Pull the insights → Draft with the skill → Human pass → Schedule → Measure), downward arrows, centred. | Build in Canva |
| 8 | The whole thing is measured against booked calls | Lavender White | Bold title top-centre. Below: booked-calls tracker screenshot with key column highlighted. [Figures need sign-off.] | Mauro supplies screenshot |
| 9 | This isn't theory. It runs every week. | Yellow | No visual: single statement, bold, centred | Text only |
| 10 | 2: What It Produced | Lavender White | Section divider. "2" in ~96pt bold centred above. Section title in ~60pt bold centred below. | Text only |
| 11 | One post opened a $[X]k conversation | Lavender White | Screenshot of the actual X post, centred, light shadow. Caption below: "[the post that started it]". | Mauro supplies screenshot |
| 12 | The DM that followed | Lavender White | DM screenshot, client name blurred, centred. | Mauro supplies screenshot |
| 13 | If a system can't survive a busy week, it isn't a system | Lavender White | Bold multi-line text top-centre. Below: dark callout box (#1F2937), label: "Simple rule to remember", body text: "If the engine needs you every day, you built a job, not a system." | Build in Canva |
| 14 | Run an established agency? | Lavender White | CTA slide. Line 1 bold centred. Line 2: [CTA placeholder until offer exists]. Optional headshot right. | Build in Canva; Mauro supplies headshot |

---

## Trigger Phrases

Run this skill when you see:
- "Build the visual brief for slide deck"
- "Create the VA production table"
- "Make the Canva brief for [video title]"
- "Turn this slide list into a production table"
- "What does the VA need to build this deck?"

---

## Anti-Patterns

- **Never leave a row with "visual TBD"**: every row must have a complete asset description or a specific placeholder instruction
- **Never specify stock photos**: real screenshots or Canva-built graphics only
- **Never describe a yellow slide as needing a visual**: yellow slides are always text only
- **Never combine two different diagram types on one slide**: if a slide needs a diagram and a screenshot, flag it as split layout
- **Never guess at a screenshot's content**: if the data or image Mauro needs to supply is unknown, the asset column says "Placeholder: [describe what specific data/screenshot is needed]"
- **Never fabricate a proof asset**: no mocked-up dashboards, DMs, or numbers. Real asset or labelled placeholder.
- **Never use bullet points inside slide designs**: all text on slides is declarative statements, not lists (the one exception is stage-diagram description text, which is short phrases)
