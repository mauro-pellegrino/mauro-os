# YouTube Slide Visuals — VA Production Brief Generator
**Version 1.1 | Updated 30 March 2026**

This skill takes the numbered slide deck output from `skills/youtube-canva-slides.md` and produces a row-by-row visual production brief for the VA to build the final Canva deck. Every row is specific enough that the VA can execute without asking a clarifying question.

---

## Required Reading

Before producing any written output, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. All copy must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

## Step 0 — Surface What's Already Available

Before generating any production table, check what already exists. Output what's found. Then ask for the numbered slide list.

### 1. Check for an existing slide list or script

```bash
grep -rli "[topic keyword]" /Users/mauro/growthub-os/scripts/
```

If a script or slide list exists: confirm the file path before proceeding.
If nothing exists: flag that the slide list must come from `skills/youtube-canva-slides.md` first.

### 2. Identify which slide types this topic will likely generate

Based on the topic, pre-identify which slide types from the classification system (below) are most likely to appear. This helps the requester know which assets to prepare.

For example, a video on "unaware ads" will likely generate:
- DIAGRAM-AWARENESS (the 5-stage awareness diagram)
- YELLOW-TEXT (belief-breaking statements)
- AD-EXAMPLE (unaware-format ad examples Lorenzo needs to supply)
- PROOF-DATA (Meta spend or results screenshots)
- DIAGRAM-FLOW (the unaware ad structure / script structure)

### 3. Output a pre-build summary

```
PRE-BUILD CHECK: [VIDEO TITLE / TOPIC]
----------------------------------------
Slide list status: [Found / Not yet generated]

Slide types likely in this video:
- [Slide type] — [rough count if known]

Assets Lorenzo will need to supply:
- [Ad thumbnails / screenshots / DMs — what type and how many estimated]
```

### 4. Request what's still needed

After the summary, ask:

> "Paste the numbered slide list from `skills/youtube-canva-slides.md` and I'll produce the full VA production table."

Wait for the slide list before producing any output.

---

## VA SOP — Read This Before You Open Canva

### Canva Setup

**Slide size:** 1920 × 1080px (16:9 widescreen). Do not use presentation defaults — set this manually under Custom Size.

**Brand colours — add these to your Canva palette before starting:**
| Name | Hex | Use |
|---|---|---|
| Growthub Yellow | `#FBBF24` | Yellow statement slide backgrounds |
| Lavender White | `#F9F0FF` | All content slide backgrounds |
| Dark Navy | `#1A1A2E` | Logo block, dark callout boxes |
| Growthub Green | `#00D4A1` | Logo G mark only |
| Body Black | `#0A0A0A` | All text on yellow and lavender backgrounds |
| White | `#FFFFFF` | Text inside dark callout boxes and dark screenshot overlays |

**Font:** Use **Plus Jakarta Sans** throughout (available free in Canva). If unavailable, substitute **Inter** or **DM Sans**. Use Bold weight for all headlines and statement text. Use Medium weight for body description text only.

**Font size hierarchy:**
| Element | Size | Weight | Alignment |
|---|---|---|---|
| Yellow slide statement | 72–80pt | Bold | Centred |
| Section number | 96pt | Bold | Centred |
| Section title | 60pt | Bold | Centred |
| Content slide title | 48pt | Bold | Left |
| Content slide body | 28–32pt | Bold | Left |
| Supporting text / captions | 22–24pt | Medium | Left |
| Dark callout box label | 16pt | Medium | Left |
| Dark callout box body | 22pt | Bold | Left |

**Logos and recurring elements — save these as Canva Brand Kit or as pre-built elements:**
- Growthub logo block: Dark navy square (`#1A1A2E`), Growthub G in Growthub Green. Used bottom-right on cover slide only.
- Lorenzo profile pill: Black rounded rectangle with Lorenzo's headshot + "@lorenzo_pravata". Used bottom-left on awareness diagram and framework slides.
- "Growthub" label pill: Small yellow rounded rectangle (`#FBBF24`) with "Growthub" in black bold. Used bottom-right on diagram slides.
- Yellow horizontal bar: Full-width yellow bar at bottom of cover slide. "GROWTHUB.AGENCY" in bold black, left-aligned inside it.

---

### How to Import the Starting Point

1. If a `.pptx` file has been provided: open Canva → Import → Upload the `.pptx`. It will create a presentation with all slides pre-populated. Use it as a structural reference only — do not rely on its fonts or colours. Restyle every slide against this production brief.
2. If no `.pptx` exists: start from a blank 1920×1080 Canva presentation and build slide by slide using this brief.
3. Duplicate the blank template before starting so the original is preserved.

---

### Order to Work Through Slides

Work in this order to minimise repeated setup:

1. **Build all yellow slides first** — same background, same font, same layout. Do them as a batch.
2. **Build all section divider slides** — lavender background, number + title only. Quick batch.
3. **Build all text-only content slides** (lavender, no visuals) — copy/paste text, adjust size.
4. **Build all diagram slides** — use the diagram specs in each row. Most time-intensive. Do one at a time.
5. **Build all proof/data slides** — placeholder boxes first, then paste screenshots when Lorenzo provides them.
6. **Build all ad example slides** — placeholder boxes for ad thumbnails Lorenzo will supply.
7. **Build cover slide last** — it requires the most elements and you will have brand kit ready by then.

---

### What to Do When an Asset Needs to Come From Lorenzo

When a row in the production table says **"Screenshot — Lorenzo supplies"**, do the following:

1. Build the slide with a clearly labelled placeholder box: grey fill, white border, text inside reading `[SCREENSHOT: {description of what goes here}]`.
2. Add a Canva comment on that slide (click the comment icon) describing exactly what Lorenzo needs to provide. Example: *"Need Meta Ads Manager screenshot showing $63M spend figure from the last 6 months."*
3. Flag the slide number in the delivery message to Lorenzo: *"Slides 8, 14, and 22 need screenshots from you — I've left labelled placeholders."*
4. Never use stock imagery as a substitute for a real screenshot. Leave the placeholder.

---

### Final QA Before Delivery

Before sharing the deck:
- [ ] Every yellow slide: `#FBBF24` background, black bold text, centred, no visuals
- [ ] Every content slide: `#F9F0FF` background
- [ ] No slide has bullet points — text is statements, not lists
- [ ] No slide uses decorative fonts, gradients, or text shadows
- [ ] All screenshot placeholders are clearly labelled
- [ ] Font is consistent throughout (Plus Jakarta Sans Bold)
- [ ] Slide count matches the numbered list from the script output

---

## Visual Pattern Rules — How to Determine Each Slide's Design

Before running the production table, the AI uses these rules to classify every numbered slide.

### Rule 1 — Background Type

**Use YELLOW (`#FBBF24`) when the slide:**
- Contains a single rhetorical question (e.g. "Why do educational ads scale better in 2026?")
- Contains a single contrarian statement or problem framing (e.g. "Because most brands only know how to target warmer customers.")
- Contains a transitional insight or "so what" conclusion (e.g. "Structure is what help us turn education into great ads.")
- Contains a philosophical or belief statement with no supporting visual
- Is a pure verbal punchline — one or two sentences, no diagram needed

**Use LAVENDER WHITE (`#F9F0FF`) when the slide:**
- Is a section number divider
- Contains a framework, diagram, or flow chart
- Contains a proof screenshot or data table
- Contains an ad creative example or examples
- Contains body text with supporting information
- Contains a social proof element (tweet, DM, Slack message)
- Contains a before/after comparison
- Contains a split layout (text left, visual right)
- Is the cover slide or CTA slide

**Never use dark backgrounds** for full slides. Dark is only used for embedded callout boxes within a lavender slide.

---

### Rule 2 — Slide Type Classification

Once the background is set, classify the slide into one of these types. The type determines the layout.

| Type | Description | Background |
|---|---|---|
| **COVER** | Title, subtitle, ad creative collage, logo, yellow bar | Lavender White |
| **YELLOW-TEXT** | Single statement or question, centred text only | Yellow |
| **SECTION-DIVIDER** | Large number + section title, centred | Lavender White |
| **TEXT-ONLY** | Multi-line explanation, no diagram, no image | Lavender White |
| **DIAGRAM-FLOW** | Linear or vertical flow chart (steps, paths) | Lavender White |
| **DIAGRAM-AWARENESS** | Awareness level 5-stage horizontal diagram | Yellow (diagram sits on yellow bg) |
| **DIAGRAM-FRAMEWORK** | Named framework map (Creative Strategy Map etc) | Lavender White |
| **PROOF-DATA** | Ad performance data, Meta dashboard screenshot | Lavender White |
| **AD-EXAMPLE** | Real ad creative(s) shown as phone/portrait thumbnails | Lavender White |
| **SOCIAL-PROOF** | Tweet, DM, Slack screenshot | Lavender White |
| **SPLIT-TEXT-VISUAL** | Left text explanation, right visual (screenshot or example) | Lavender White |
| **DARK-CALLOUT** | Lavender slide with embedded dark box containing a key rule | Lavender White |
| **CTA** | Call to action — minimal, clean, low pressure | Lavender White |

---

### Rule 3 — Visual Asset Decision

For each slide, determine the asset needed:

| Situation | Asset type | Source |
|---|---|---|
| Yellow text slide | None — text only | Build in Canva |
| Section divider | None — number + title | Build in Canva |
| Awareness level diagram | Recreate the 5-stage coloured box diagram | Build in Canva |
| Framework flow (vertical) | Recreate as rounded box flow chart | Build in Canva |
| Path comparison diagram | Recreate as 2-column box layout | Build in Canva |
| Before/After | Recreate with red BEFORE pill + green AFTER pill | Build in Canva |
| Meta dashboard / spend proof | Real screenshot from Meta Ads Manager | Lorenzo supplies |
| Meta Partner badge | Real screenshot from Meta Business Suite | Lorenzo supplies |
| Ad creative example | Real ad video thumbnail (portrait) | Lorenzo supplies |
| Twitter/X screenshot | Real screenshot from Lorenzo's X account | Lorenzo supplies |
| Slack/Discord DM | Real screenshot from internal Slack/Discord | Lorenzo supplies |
| Client data table | Real screenshot from reporting tool | Lorenzo supplies |
| Illustration / icon (person, animal) | Simple icon from Canva icon library (no stock photos) | Build in Canva |
| Technical diagram (Andromeda architecture etc) | Recreate as simplified diagram OR use supplied image | Lorenzo supplies or Build in Canva |

**Stock photography is never used.** If it is not a Canva-built graphic and Lorenzo cannot supply a real screenshot, the slide gets a placeholder.

---

### Rule 4 — The Awareness Level Diagram (Exact Spec)

When a slide requires the awareness level diagram, build it exactly as follows:

**Background:** Full yellow slide (`#FBBF24`)

**5 boxes in a row, connected by right-pointing arrows:**
| Stage | Label | Box colour | Text colour |
|---|---|---|---|
| 1 | UNAWARE | Coral/orange `#F97316` | White |
| 2 | PROBLEM-AWARE | Amber `#F59E0B` | Black |
| 3 | SOLUTION AWARE | Pink/magenta `#EC4899` | White |
| 4 | PRODUCT AWARE | Teal `#14B8A6` | White |
| 5 | MOST AWARE | Sky blue `#38BDF8` | Black |

Each box has:
- Rounded rectangle shape
- Stage label in bold caps at top of box
- Description text in smaller regular text below the label (inside or below box)
- A dark/black action label at the very bottom (e.g. "EDUCATE, DEMONSTRATE OR ENTERTAIN")

**Annotations:** If the script highlights a specific stage, add a red hand-drawn circle around that stage's box and a red arrow pointing to it. Canva has a "marker" or "doodle" element for this — use red.

**Bottom-left:** Lorenzo profile pill (black rounded rectangle, Lorenzo's photo + "@lorenzo_pravata" in white). Size: ~220px wide.

**Bottom-right:** "Growthub" small yellow pill label with black text.

---

### Rule 5 — The Dark Callout Box (Exact Spec)

When a slide contains a key rule or principle that needs to stand out:

- Box colour: `#1F2937` (dark charcoal, not pure black)
- Corner radius: 8px
- Padding: 24px inside
- Label text (top): Small, medium weight, grey `#9CA3AF` — e.g. "Simple rule to remember"
- Body text: White `#FFFFFF`, bold, 22pt
- Width: ~60% of slide width, centred or positioned in lower half of slide
- The rest of the slide is lavender white with standard body text above

---

### Rule 6 — Framework Diagram Colours (VSL Structure)

When building the VSL script structure diagram (vertical flow):
- All boxes: Rounded rectangles, amber/orange `#F59E0B`, black text, bold labels
- Connected by downward arrows in dark grey
- Steps: Problem → Discredit Alternative 1 → Explanation → Agitate → Desired Outcome → Discredit Alternative 2 → Handle Objection → Introduce Product → CTA

When building the Stealth Creative reasons diagram (horizontal 3-step):
- Box 1: Orange `#F97316`, white text
- Box 2: Amber `#F59E0B`, black text
- Box 3: Pink `#EC4899`, white text
- Connected by right-pointing arrows
- Each box has a smaller description text box below it (lavender background, black text)

When building the "Two Paths" comparison diagram:
- Path 1 box: Orange `#F97316`, black text
- Path 2 box: Amber `#F59E0B`, black text
- Recommendation box: Teal `#14B8A6`, black text
- 4 result boxes below: Pink `#EC4899`, white text

---

## Production Table Output Format

When this skill is run with a numbered slide list as input, output a production table in this exact format. One row per slide.

```
| # | Slide text (exact, truncated to 15 words if long) | Background | Visual asset needed | Asset source |
|---|---|---|---|---|
| 1 | [text] | Yellow / Lavender White | [exact description] | Build in Canva / Lorenzo supplies / Text only |
```

**Column 4 (Visual asset needed) must be specific enough that the VA does not need to ask.** Examples of acceptable descriptions:
- "No visual — text only, centred"
- "5-stage awareness diagram: Unaware (orange) → Problem-Aware (amber) → Solution Aware (pink) → Product Aware (teal) → Most Aware (blue), each with description and dark action box below. Red circle annotation on [stage name]. Lorenzo profile pill bottom-left. Growthub pill bottom-right."
- "Meta Ads Manager dashboard screenshot showing [specific figure]. Positioned bottom-half of slide. Title above."
- "Vertical amber flow: 7 rounded boxes (Problem → Discredit Alt 1 → Explanation → Agitate → Desired Outcome → Discredit Alt 2 → Handle Objection) connected by downward arrows, centred."
- "3 vertical ad phone thumbnails (portrait), evenly spaced, showing actual ad creatives with red text overlay hooks visible. Slide title 'Examples' centred above."
- "Dark callout box (#1F2937), label: 'Simple rule to remember', body text: '[exact text]'. Positioned bottom-centre of slide. Body text above in lavender area."
- "Left column (60%): explanation text. Right column (40%): Meta Partner Growth Insights badge screenshot showing $[figure] in spend."

---

## Example Output (Partial — VSL Ads That Scale in 2026)

This is what correctly formatted output looks like. Use this as the quality benchmark.

| # | Slide text | Background | Visual asset needed | Asset source |
|---|---|---|---|---|
| 1 | VSL Ads That Scale in 2026 — GROWTHUB.AGENCY | Lavender White | Title bold top-left. Ad creative collage (5 overlapping portrait thumbnails, angled). Yellow horizontal full-width bar at bottom with "GROWTHUB.AGENCY" bold black left. Growthub logo block (dark navy square, green G) bottom-right. | Lorenzo supplies ad thumbnails; bar + logo built in Canva |
| 2 | Check out our case studies & creative portfolio here | Lavender White | Large bold centred title. URL as underlined body text. Grid of 10 ad thumbnails in 2 rows of 5, equal size. | Lorenzo supplies thumbnails; layout built in Canva |
| 3 | Why do educational ads scale better in 2026? | Yellow | No visual — single question, bold, centred, ~72pt, vertically centred on slide | Text only |
| 4 | Because most brands only know how to target warmer customers | Yellow | No visual — single statement, bold, centred, 2 lines | Text only |
| 5 | They present the problem vaguely and then expect customers to fall in love | Yellow | No visual — single statement, bold, centred, 2 lines | Text only |
| 6 | Awareness levels diagram | Yellow | Full 5-stage horizontal awareness diagram. Unaware (coral), Problem-Aware (amber), Solution Aware (pink), Product Aware (teal), Most Aware (sky blue). Descriptions below each. Dark action boxes at bottom. Red circle and arrow on UNAWARE. Lorenzo profile pill bottom-left. Growthub pill bottom-right. | Build in Canva |
| 7 | VSL ads work because they teach first, establish authority | Yellow | No visual — single statement, bold, centred, 3 lines | Text only |
| 8 | In this video, I'm breaking down how we create VSL ads | Yellow | No visual — single statement, bold, centred, 3 lines | Text only |
| 9 | By the end of this, you'll understand: Why less aware ads are needed | Yellow | No visual — two-part text: smaller "By the end of this, you'll understand:" above, larger key point below. Both centred. | Text only |
| 10 | How authority-driven VSLs work with different niches | Yellow | No visual — single statement, bold, centred | Text only |
| 11 | And how top brands create ads that educate but also convert | Yellow | No visual — single statement, bold, centred, 2 lines | Text only |
| 12 | 1 — Why "Less Aware" Ads Are Needed | Lavender White | Section divider. "1" in ~96pt bold centred above. Section title in ~60pt bold centred below. | Text only |
| 13 | Most brands advertise to people who are already close to buying | Lavender White | Bold title top-centre. Below: dark navy rectangle containing 5 stage boxes (Stage 1 Unaware blue, Stage 2 Problem Aware blue, Stage 3 Solution Aware amber, Stage 4 Product Aware blue, Stage 5 Most Aware teal, white label text). Pink hand-drawn rectangular annotation around Stages 3–5. | Build in Canva |
| 14 | Those typical structures used to work before | Lavender White | Bold title top-centre. Below: 4 horizontal pill shapes connected by arrows: red (Hook/Problem), mint (Solution), dark green (Benefits/Features), lime green (Social Proof). Each labelled in black. | Build in Canva |
| 15 | Even I used to tweet about them | Lavender White | Bold title top-centre. Dark rounded rectangle screenshot of Lorenzo's tweet (Mar 2, 2023: "1. Hook 2. Problem Agitator 3. Present the Solution 4. Specific Benefits/Features 5. Testimonial"). Tweet embedded centred below title. | Lorenzo supplies tweet screenshot |
| 16 | VSL ads expand the pool of people who can convert | Lavender White | No visual — 3 bold statement lines, centred | Text only |
| 17 | Focus on a creative strategy that can take care of both | Lavender White | Bold centred title at top. Split layout: left = 4 blue person icons (large group), right = 2 orange person icons (small group). Below each group: bold label + 2 lines description. Build icons using Canva person icon. | Build in Canva |
| 18 | By just adding educational ads, they scaled +46% in 2 months | Lavender White | Bold title top (3 lines). Below: Meta analytics table screenshot — shows ad performance data with green/red percentage changes. Table positioned in bottom 60% of slide. | Lorenzo supplies screenshot |
| 19 | So if education is the entry point, who delivers it in a way people trust? | Yellow | No visual — single question, bold, centred, 2 lines | Text only |
| 20 | 2 — How Authority Figures Work | Lavender White | Section divider. "2" in ~96pt bold centred above. Section title in ~60pt bold centred below. | Text only |
| 29 | Educational VSLs still sell. But not like the old structures. | Lavender White | Bold multi-line text top-centre. Below: dark callout box (#1F2937), label: "Simple rule to remember", body text: "If a creative cannot convert a skeptical stranger, it is not a strong creative — it's just a reminder." | Build in Canva |
| 30 | VSL structure example — insoles client | Lavender White | Three-column layout. Left (40%): bold explanation text. Centre (30%): vertical amber flow chart — 7 rounded boxes (Problem → Discredit Alternative 1 → Explanation → Agitate → Desired Outcome → Discredit Alternative 2 → Handle Objection), connected by downward arrows. Right (30%): dark script panel with small white body text showing actual script lines. | Build in Canva (flow); Lorenzo supplies script panel screenshot |
| 31 | Skincare example — data-driven VSL | Lavender White | Left (55%): bold title + 2 bullet lines + body explanation text. Right (45%): vertical phone ad mockup showing skincare creator ad with red subtitle text overlay ("STOP! Anti-aging is aging you" / "Your skincare routine"). | Lorenzo supplies ad screenshot |

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

- **Never leave a row with "visual TBD"** — every row must have a complete asset description or a specific placeholder instruction
- **Never specify stock photos** — real screenshots or Canva-built graphics only
- **Never describe a yellow slide as needing a visual** — yellow slides are always text only
- **Never combine two different diagram types on one slide** — if a slide needs a diagram and a screenshot, flag it as split layout
- **Never guess at a screenshot's content** — if the data or image Lorenzo needs to supply is unknown, the asset column says "Placeholder — [describe what specific data/screenshot is needed]"
- **Never use bullet points inside slide designs** — all text on slides is declarative statements, not lists (the one exception is the awareness level description text, which is short phrases)
