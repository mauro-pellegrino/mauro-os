# Miro Board Design System: YouTube Video Ready
**Version 1.4 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

Converts any YouTube video script into a visually structured Miro board that mirrors the video's flow. These are the channel's production board conventions. Use this for the Chrome extension workflow: paste the output brief into Claude in the browser with the Miro extension active.

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md.

---

## Global Layout Rules

- The board flows as a single vertical column, top to bottom. No side-by-side macro sections (exception: Two-Path Comparison).
- Every concept gets a visual container. Never raw text walls. Use diagrams, grids, flows, or image placeholders for every idea.
- Generous vertical spacing between sections. Each major section should feel like its own slide.
- All content is centre-aligned on the vertical axis.
- Image placeholders are compact — small inline rectangles (w:300–400, h:40) labelled `[IMG: description]`. Never large standalone blocks. Place them beside or below the element they support, not as a separate full-width section.

---

## Visual Style Rules (apply everywhere)

- **Shape type:** Use `rectangle` for all boxes (NOT `round_rectangle`). The only exception is the creator name pill and the brand badge, which use `round_rectangle`.
- **Border rule:** All filled label/content boxes use `borderColor: #1a1a1a`, `borderWidth: 3`. This gives the signature stacked-card look.
- **Color pairing rule:** The fill color of a label box = the fill color of its paired description box. Both use the same yellow (`#ffdc4a`) with `#1a1a1a` borders throughout.
- **Description boxes** are `rectangle` shapes with `#ffdc4a` fill, `#1a1a1a` border, `borderWidth: 3`. Body text inside is centred, regular weight. Font size 16.
- **Arrows** between elements: Use simple black line arrows or `→` text connectors, no decoration.
- **Yellow** = Miro hex `#ffdc4a` throughout. Use it for label boxes, pillar boxes, tree nodes, and title pill. Light yellow = `#fff6b6` for narration text blocks.
- **Narration text blocks** use Miro's `text` element with `fillColor: '#fff6b6'` (light yellow background), NOT shape elements. Font size 18, width 773, centre-aligned.
- **Plain body text** uses Miro's `text` element with `fillColor: 'transparent'`, font size 18, width 773, centre-aligned.
- **Numbered steps** (e.g. "1. Decide on the main personas") are plain centred text — bold or regular. They are NOT boxed. They introduce a diagram or element that follows immediately below.

---

## Exact Element Specifications

| Element | Shape | Width | Height | Fill | Border | Border Width | Font Size |
|---|---|---|---|---|---|---|---|
| Title text | text | 777 | auto | transparent | — | — | 36 |
| Creator pill | round_rectangle | 350 | 50 | #ffdc4a | #000000 | 0 | 16 |
| Process/Section title | rectangle | 695 | 102 | #dedaff | #1a1a1a | 3 | 47 |
| Question hook | rectangle | 350–500 | 51 | #dedaff | #1a1a1a | 3 | 18 |
| Yellow label box | rectangle | 350 | 51 | #ffdc4a | #1a1a1a | 3 | 16 |
| Yellow pillar header | rectangle | 350 | 75 | #ffdc4a | #1a1a1a | 3 | 24 |
| Yellow pillar description | rectangle | 350 | 120 | #ffdc4a | #1a1a1a | 3 | 16 |
| Tree node (parent) | rectangle | 350 | 196 | #ffdc4a | #1a1a1a | 3 | 48 |
| Tree node (child) | rectangle | 350 | 196 | #ffdc4a | #1a1a1a | 3 | 36 |
| Green label | rectangle | 269–500 | 51 | #adf0c7 | #1a1a1a | 3 | 18 |
| Red/negative label | rectangle | 350 | 51 | #ff6464 | #1a1a1a | 3 | 16 |
| Narration text block | text | 773 | auto | #fff6b6 | — | — | 18 |
| Body text | text | 773 | auto | transparent | — | — | 18 |
| Emphasis narration | text | 773–1500 | auto | #fff6b6 | — | — | 36–48 |
| Image placeholder | rectangle | 300–400 | 40 | #e6e6e6 | #cccccc | 1 | 12 |
| Sticky note (header) | sticky_note square | 213 | 244 | dark_green | — | — | — |
| Sticky note (content) | sticky_note square | 274 | 314 | red / pink | — | — | — |
| Sticky note (context) | sticky_note square | 274 | 314 | light_yellow | — | — | — |
| Brand badge | round_rectangle | 350 | 51 | #1a1a1a | #1a1a1a | 0 | 16 |

---

## Script Segmentation Rule

Split the script into sections at every:
- New topic or subheading
- Named process (e.g. "Process #1", "Step 2")
- Clear shift in what the script is doing (explaining → demonstrating → listing → concluding)

Do not split mid-thought. Each section should map cleanly to one section type below.

**When in doubt about what visual to use:** default to plain centred text (text element, fs:18, transparent fill). Never force content into a container that doesn't fit.

---

## Section Types

### 1. TITLE CARD
**When to use:** The very first element — the video's headline.

- Text element, width: 777, fontSize: 36, bold, centred, fillColor: transparent
- Yellow filled pill below: round_rectangle, w:350, h:50, fill: #ffdc4a, border: #000000, borderWidth: 0, fontSize: 16, with creator name ("Mauro, @maurojpelle")
- Compact image placeholder inline if script references credibility proof: rectangle, w:400, h:40, fill: #e6e6e6, fontSize: 12
- Body text underneath for the intro premise: text element, width: 773, fontSize: 18, regular weight, centred, fillColor: transparent

---

### 2. PROCESS / SECTION TITLE
**When to use:** Every time a new named process or major section begins.

- rectangle, w:695, h:102, fill: #dedaff, border: #1a1a1a, borderWidth: 3, fontSize: 47, bold italic text inside
- Format: "Process #1: [Name]" or "[Section Name]"
- Centred, stands alone with spacing above and below
- Acts as a clear visual divider — nothing else on the same row

---

### 3. QUESTION HOOKS
**When to use:** When the script poses a rhetorical question or introduces a key term before explaining it.

- rectangle, w:350–500, h:51, fill: #dedaff, border: #1a1a1a, borderWidth: 3, fontSize: 18, bold text
- Stack multiple hooks vertically, each as its own box
- Follow immediately with a narration text block answering or expanding on the question

---

### 4. NARRATION TEXT BLOCK
**When to use:** Explanatory text, bridges, summaries, setup text, or any script passage that is the narrator's voice — not a concept label or list.

- **Yellow narration** (primary explanatory content): Miro text element, width: 773, fontSize: 18, centred, fillColor: `#fff6b6`
- **Plain narration** (transitions, simple statements): Miro text element, width: 773, fontSize: 18, centred, fillColor: `transparent`
- **Emphasis narration** (key rules, big statements): Miro text element, width: 773–1500, fontSize: 36–48, centred, bold, fillColor: `#fff6b6`

This is the default container for any script text that doesn't fit a more specific section type.

---

### 5. TWO-PATH COMPARISON
**When to use:** When the script contrasts two approaches, paths, or outcomes.

- Left path top node: rectangle, w:350, h:51, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 16, bold
- Right path top node: same specs as left
- Child nodes below each path: rectangle, w:350, h:51, fill: #ffdc4a (or #e6e6e6 for image placeholders)
- Negative outcome: rectangle, w:350, h:51, fill: #ff6464, border: #1a1a1a, borderWidth: 3, fontSize: 16
- Positive/winning outcome: rectangle, w:350, h:51, fill: #adf0c7, border: #1a1a1a, borderWidth: 3, fontSize: 16
- Convergence conclusion: rectangle, w:500, h:51, fill: #adf0c7, border: #1a1a1a, borderWidth: 3, fontSize: 18, centred below both paths
- Left path centred at X - 450, right path at X + 450
- Node spacing: 70px vertical between child nodes, 90px below top node to first child

---

### 6. TREE / ORG-CHART DIAGRAM
**When to use:** When the script breaks one parent concept into sub-categories, personas, pillars, or branches.

- Use Miro Diagram widget (tree/org-chart layout)
- Top node: rectangle, w:350, h:196, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 48, bold — the parent concept
- Child nodes: rectangle, w:350, h:196, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 36, bold
- Below each child: text blocks (fontSize: 36, fill: #fff6b6) listing sub-details
- Keep node text short — labels only, detail goes in sub-text blocks

---

### 7. HORIZONTAL PILLAR LAYOUT
**When to use:** When the script lists 3–5 parallel concepts of equal weight, each needing a label and a short explanation.

- Top row pillar headers: rectangle, w:350, h:75, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 24, bold
- Below each header: description box rectangle, w:350, h:120, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 16, italic
- Horizontal spacing between pillars: 450px centre-to-centre
- Arrangement: 3 across top row, 2 centred below if 5 pillars (3+2)
- Vertical gap between header and description: 130px

---

### 8. MULTI-COLUMN EXPANDED SECTION
**When to use:** When the script dives deep into 2–3 parallel topics, each with sub-steps, examples, and visuals.

- Column headers: rectangle, w:350, h:75, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 24, bold
- Under each column:
  - Body text blocks (text element, fontSize: 18, fillColor: transparent)
  - Green label sub-steps: rectangle, fill: #adf0c7, border: #1a1a1a, borderWidth: 3, fontSize: 18
  - Compact image placeholders: rectangle, w:300, h:40, fill: #e6e6e6
  - Dialog script blocks: text element with fillColor: `#fff6b6`, A:/B: format

---

### 9. STICKY NOTE GRID
**When to use:** When the script presents a matrix — personas × angles × awareness levels, or any rows × columns structure.

- Top-left cell: sticky note square, w:274, h:314, color light_yellow
- Header row: sticky notes square, w:213, h:244, color dark_green
- Left column: sticky notes square, w:274, h:314, color red
- Content cells: sticky notes square, w:274, h:314, color red or pink
- Keep cell text to 1–2 short lines

---

### 10. LABEL → DESCRIPTION ROWS
**When to use:** When the script lists reasons, features, variations, or principles — each with a label and an explanation.

- Label box: rectangle, w:350, h:51, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 16, bold
- Arrow: text element `→` or connector
- Description box: rectangle, w:350–400, h:51–75, fill: #ffdc4a, border: #1a1a1a, borderWidth: 3, fontSize: 16
- Label centred at X - 250, description at X + 250
- Stack rows vertically with 80px spacing between them
- No image placeholders needed in this section type

---

### 11. GREEN EMPHASIS LABEL
**When to use:** When the script lands a key action step, sub-step, or important takeaway that isn't a full conclusion banner.

- rectangle, w:269–500, h:51, fill: #adf0c7, border: #1a1a1a, borderWidth: 3, fontSize: 18, bold centred text
- Stands alone, centred

---

### 12. BRAND BADGE
**When to use:** The very last element on the board.

- round_rectangle, w:350, h:51, fill: #1a1a1a, border: #1a1a1a, borderWidth: 0, fontSize: 16
- White text: "@maurojpelle · ghostedcalls.com" (confirm the final URL with Mauro before first use)
- Centred at the bottom of the board

---

## Colour System

| Colour | Hex | Always used for |
|---|---|---|
| Yellow | #ffdc4a | Label boxes, pillar headers, tree nodes, title pill, description boxes |
| Light Yellow | #fff6b6 | Narration text block fill (text element fillColor) |
| Light Purple | #dedaff | Process/section title boxes, question hook boxes |
| Green | #adf0c7 | Positive outcome nodes, sub-step labels, emphasis labels |
| Red | #ff6464 | Negative outcome nodes in comparisons |
| Dark Grey/Black | #1a1a1a | All box borders, brand badge fill |
| Grey placeholder | #e6e6e6 | Image placeholder fills |
| Grey border | #cccccc | Image placeholder borders |
| Black | #000000 | Main title text, body text, creator pill border |
| White | #ffffff | Brand badge text |
| Sticky: dark_green | Miro preset | Grid header row sticky notes |
| Sticky: light_yellow | Miro preset | Grid context cell sticky notes |
| Sticky: red | Miro preset | Grid content / row header sticky notes |
| Sticky: pink | Miro preset | Grid alt-content sticky notes |

---

## Element Types (Miro-specific)

| Element | Miro Type | Use for |
|---|---|---|
| Miro Diagram widget | diagram | Tree charts, org charts |
| Sticky notes | sticky_note (square) | Grids only — colour-coded per the system above |
| Text block | text | Body text (transparent fill), narration (fill: #fff6b6), emphasis narration, numbered steps |
| Shapes | rectangle | Labels, pillar headers, description boxes, question hooks, process titles, green labels, red/negative labels |
| Shapes | round_rectangle | Creator pill and brand badge ONLY |
| Arrow connectors / text arrows | text with → | Between label and description boxes, between flow elements |
| Image placeholders | rectangle | Small compact rectangles (w:300–400, h:40) labelled `[IMG: description]` |

---

## Vertical Spacing Guide

| Between | Gap (px) |
|---|---|
| Title text → Creator pill | 150 |
| Creator pill → Image placeholder | 100 |
| Image placeholder → Body text | 120 |
| Narration block → Next element | 100–120 |
| Process title → Following content | 150 |
| Pillar headers → Description boxes | 130 |
| Label → Description rows | 80 between rows |
| Two-path child nodes | 70 between nodes |
| Section end → Next Process title | 250–300 |
| Last content → Brand badge | 200 |

---

## How to Convert a Script into a Board

1. **Segment the script** — split at every new topic, subheading, named process, or clear shift in what the script is doing
2. **Assign a section type** to each segment:
   - Video headline → Title Card
   - New named process → Process / Section Title
   - Rhetorical question or key term intro → Question Hooks
   - Explanatory narration, bridge, or summary → Narration Text Block
   - Two contrasting paths/approaches → Two-Path Comparison
   - One concept branching into sub-categories → Tree Diagram
   - 3–5 parallel pillars with explanations → Horizontal Pillar Layout
   - 2–3 deep parallel topics with sub-steps → Multi-Column Expanded Section
   - Rows × columns matrix → Sticky Note Grid
   - List of reasons/features/formats → Label → Description Rows
   - Key action step or takeaway → Green Emphasis Label
   - Anything that doesn't fit → plain centred text (Narration Text Block with transparent fill)
3. Apply exact element specs from the table above — every element must match the specified width, height, fill, border, and font size
4. Keep image placeholders compact (w:300–400, h:40) and inline
5. End with the Brand Badge

---

## Output Format

When producing a board brief for the Chrome extension, output section by section using this schema. One element per line. Be explicit — the extension should not have to infer anything.

```
SECTION [N] — [Section Type]
ELEMENT: [miro type] | SHAPE: [rectangle/round_rectangle/text/sticky_note] | TEXT: [exact text] | W: [width] | H: [height] | FILL: [hex] | BORDER: [hex] | BW: [border width] | FS: [font size] | STYLE: [bold/italic/bold-italic/regular]
VISUAL: [IMG: description] or "none"
LAYOUT: [positioning — e.g. "centred", "side by side at X-450 / X+450", "3 across at 450px spacing"]
```

Produce the **complete brief for the entire board** before the Chrome extension starts building. Never build section by section — the full brief must come first.

---

## Worked Example

**Script excerpt:** "You build the inbound machine for your clients. You never built your own. I run an AI content engine for a real agency every week, measured against booked calls."

```
SECTION 1 - Title Card
ELEMENT: text | TEXT: The AI Content Engine Behind a Real Agency (Step by Step) | W: 777 | FILL: transparent | FS: 36 | STYLE: bold centred
ELEMENT: round_rectangle | TEXT: Mauro, @maurojpelle | W: 350 | H: 50 | FILL: #ffdc4a | BORDER: #000000 | BW: 0 | FS: 16 | STYLE: bold
VISUAL: [IMG: booked-calls tracker screenshot, figures need Mauro's sign-off] rectangle W:400 H:40 FILL:#e6e6e6
ELEMENT: text | TEXT: I run this engine every week for a real B2B agency, and it's measured against booked calls... | W: 773 | FILL: transparent | FS: 18 | STYLE: regular centred
LAYOUT: vertical stack, centred

SECTION 2 - Narration Text Block
ELEMENT: text | TEXT: You've built the inbound machine for every client you have. This video shows you how to build your own... | W: 773 | FILL: #fff6b6 | FS: 18 | STYLE: regular centred
VISUAL: [IMG: content calendar screenshot, one week of scheduled output] rectangle W:350 H:40 FILL:#e6e6e6
LAYOUT: centred

SECTION 3 - Question Hooks
ELEMENT: rectangle | TEXT: Why does your own pipeline starve? | W: 350 | H: 51 | FILL: #dedaff | BORDER: #1a1a1a | BW: 3 | FS: 18 | STYLE: bold
ELEMENT: rectangle | TEXT: Because there is NO SYSTEM: | W: 350 | H: 51 | FILL: #dedaff | BORDER: #1a1a1a | BW: 3 | FS: 18 | STYLE: bold
LAYOUT: stacked vertically, centred

SECTION 4 - Process / Section Title
ELEMENT: rectangle | TEXT: Process #1: The Transcript-to-Content Pipeline | W: 695 | H: 102 | FILL: #dedaff | BORDER: #1a1a1a | BW: 3 | FS: 47 | STYLE: bold-italic
LAYOUT: centred
```

---

## Trigger Phrases

Run this skill when you see:
- "Build the Miro board for [script/video]"
- "Create the visual plan"
- "Make the board"
- "Miro brief for this script"

**WAIT FOR THE SCRIPT TO BE SENT BEFORE BUILDING.**

---

## Changelog

**v1.3 (13 March 2026)**
- All boxes now use `rectangle` shape (not `round_rectangle`) except creator pill and logo badge
- Added exact element specifications table with precise W, H, fill, border, borderWidth, and fontSize for every element type
- Narration blocks are now Miro text elements with `fillColor: #fff6b6`, not shape elements
- Updated colour hex values to match production boards: #ffdc4a (yellow), #dedaff (light purple), #fff6b6 (light yellow narration), #adf0c7 (green), #ff6464 (red), #1a1a1a (borders)
- Added vertical spacing guide with exact pixel gaps
- Updated output format to include W, H, FILL, BORDER, BW, FS per element
- Removed old "Conclusion Banner" section type — use emphasis narration text or green emphasis label instead
- Removed colour-per-row cycling from Label → Description Rows — all rows now use consistent #ffdc4a yellow
