# YouTube Miro Board
**Version 1.1 | Updated 30 March 2026**

Takes a YouTube script and generates a full Miro board with all diagrams, graphs, and visual frames the VA needs to build the Canva slide deck. Board layout mirrors Lorenzo's visual patterns from his PDF slides.

---

## Required Reading

Before producing any written output, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. All copy must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

## Step 0 — Surface What's Already Available

Before requesting the script or touching Miro, check what already exists. Output what's found. Then ask for what's still needed.

### 1. Check for an existing script

```bash
ls /Users/mauro/growthub-os/scripts/
grep -rli "[topic keyword]" /Users/mauro/growthub-os/scripts/
```

If a script exists: note the file path and confirm it's the right version.
If no script exists: flag this — the script must exist before the board can be built.

### 2. Check which visual types this topic will need

Based on the topic, identify which visual types from the Visual Type Library (below) are most likely to be needed. List them before asking for the script, so the requester knows what to expect.

For example, a video on "unaware ads" will likely need:
- AWARENESS DIAGRAM (the 5-stage horizontal flow)
- TWO-PATH COMPARISON (unaware-optimised vs. direct ads)
- AD EXAMPLE LAYOUT (examples of unaware-format creatives)
- PROOF / DATA LAYOUT (Meta spend or results screenshots)

### 3. Output a pre-build summary

```
PRE-BUILD CHECK: [VIDEO TITLE / TOPIC]
----------------------------------------
Script status: [Found at scripts/[filename] / Not yet written]

Visual types likely needed for this topic:
- [Visual type] — [which part of the video it will cover]

Assets Lorenzo will need to supply before board is complete:
- [Screenshot / ad creative / data — what type and why]
```

### 4. Request what's still needed

After the summary, ask:

> "Here's where we are. [State what exists and what's missing.] Paste the script to proceed."

Wait for the script before building the board.

---

## When to Run This Skill

- A script has been written (from `skills/youtube-hook-script.md` or directly)
- Someone says "build the Miro board for this script"
- Someone says "create the visual plan" or "make the board"

---

## Inputs Required

1. **The full script** — section by section with slide cues
2. **Video title** — used as the board name
3. **Miro access** — via `mcp__miro` tools (requires session restart after first install)

---

## What the Board Contains

Each board is divided into labelled frames. One frame per section of the video. Inside each frame: the diagrams, flow charts, and data layouts the VA needs to build that section's slides in Canva.

The board does not duplicate slide text. It visualises structure — what the diagrams look like, how elements connect, what goes left vs right, how many items are in each row.

---

## Step 1 — Parse the Script into Sections

Read the script. Identify every named section (usually marked as "SECTION X —" or equivalent). For each section, note:

- Section name and number
- Which slides are text-only (yellow or lavender, no diagram needed)
- Which slides need a diagram or visual asset
- What type of visual is needed (use the type list below)

Produce a section map before touching Miro:

```
SECTION MAP
-----------
Section 1: [Name]
  Slides [X–Y]: text-only
  Slide [Z]: needs [visual type]

Section 2: [Name]
  ...
```

---

## Step 2 — Create the Board

Use `mcp__miro__create_board` with the video title as the board name.

```
Board name: [Video title] — Visual Plan
```

---

## Step 3 — Build One Frame Per Section

For each section, use `mcp__miro__create_frame` to create a labelled frame.

Frame naming convention:
```
SECTION [N] — [Section name]
```

Frame size: 2400 × 1600px minimum. Increase width if the section has many diagrams side by side.

Position frames left-to-right across the board in section order, with 200px gaps between them.

---

## Step 4 — Populate Each Frame

Inside each frame, build the visual elements the VA needs. Use the visual type rules below to decide what to build for each slide.

### The Visual Type Library

**AWARENESS DIAGRAM**
When: any slide introducing the 5 awareness levels (Unaware → Most Aware)
Build in Miro:
- 5 rounded rectangles in a horizontal row, connected by right arrows
- Labels (top, bold caps): UNAWARE / PROBLEM-AWARE / SOLUTION AWARE / PRODUCT AWARE / MOST AWARE
- Colours: Coral `#F97316` / Amber `#F59E0B` / Pink `#EC4899` / Teal `#14B8A6` / Sky `#38BDF8`
- Short description text inside each box (what this stage means for the buyer)
- Dark action label below each box (what the ad must do at this stage)
- If a specific stage is highlighted in the script: add a red sticky note above that box labelled "← FOCUS"
- Add a text label above the row: "AWARENESS LEVELS DIAGRAM"

**CREATIVE STRATEGY MAP**
When: script introduces the Creative Strategy Map framework
Build in Miro as a connected tree:
```
[Product Name]
  └── Buyer Persona 1
        Pain Point: [text]
        └── Unaware → [angle idea]
        └── Problem-Aware → [angle idea]
        └── Solution-Aware → [angle idea]
        └── Product-Aware → [angle idea]
  └── Buyer Persona 2
        ...
```
- Use `mcp__miro__create_card` or sticky notes for each node
- Connect nodes with `mcp__miro__create_connector`
- Persona nodes: amber `#F59E0B`
- Awareness level nodes: match awareness diagram colours
- Angle nodes: white with black border
- Add label at top: "CREATIVE STRATEGY MAP"

**VERTICAL FLOW (VSL / Script Structure)**
When: script walks through a step-by-step structure (VSL format, script sections, etc.)
Build in Miro:
- Vertical column of rounded rectangles, connected by downward arrows
- Each box: amber `#F59E0B`, black text, bold label
- Standard VSL flow: Problem → Discredit Alt 1 → Explanation → Agitate → Desired Outcome → Discredit Alt 2 → Handle Objection → Introduce Product → CTA
- Adjust labels to match whatever the script actually calls the steps
- Add label above: "SCRIPT STRUCTURE — [format name]"

**TWO-PATH COMPARISON**
When: script compares two approaches, two audience types, or two outcomes
Build in Miro:
- Two columns side by side, each headed by a rounded rectangle
- Path 1 (orange `#F97316`): the wrong/old approach
- Path 2 (amber `#F59E0B`): the right/new approach
- Recommendation box below (teal `#14B8A6`): what to do instead
- Result boxes below that (pink `#EC4899`): 3–4 outcomes
- Add label above: "TWO-PATH COMPARISON"

**BEFORE / AFTER**
When: script shows a transformation or result contrast
Build in Miro:
- Two side-by-side sticky notes or cards
- Before: red `#EF4444` background, white text, label "BEFORE"
- After: green `#22C55E` background, white text, label "AFTER"
- Arrow pointing right between them
- Add label above: "BEFORE / AFTER"

**HORIZONTAL PROCESS (3–5 steps)**
When: script describes a sequential process with 3–5 distinct steps
Build in Miro:
- Horizontal row of rounded rectangles, connected by right arrows
- Step 1: Orange `#F97316`
- Step 2: Amber `#F59E0B`
- Step 3: Pink `#EC4899`
- Step 4 (if exists): Teal `#14B8A6`
- Step 5 (if exists): Sky `#38BDF8`
- Short description text below each box
- Add label above: "PROCESS — [process name]"

**PROOF / DATA LAYOUT**
When: script references a Meta dashboard screenshot, spend figure, or client result
Build in Miro:
- A placeholder sticky note in dark navy `#1A1A2E` with white text
- Text inside: "SCREENSHOT NEEDED: [exact description of what data / dashboard / figure Lorenzo needs to supply]"
- Size: 400 × 250px minimum
- Add a red sticky above it: "⚠ LORENZO SUPPLIES THIS"

**AD EXAMPLE LAYOUT**
When: script shows 1–3 ad creative examples
Build in Miro:
- One rectangle per ad, sized 300 × 500px (portrait phone ratio)
- Border: dark grey `#374151`
- Fill: light grey `#F3F4F6`
- Text inside: "AD EXAMPLE: [brief description — e.g. 'Street interview, supplement, hook about back pain']"
- Space examples 50px apart in a row
- Add label above: "AD EXAMPLES — [number] needed from Lorenzo"

**ENTITY ID / SIMILARITY DIAGRAM**
When: script explains how Meta groups similar ads (Andromeda entity ID)
Build in Miro:
- Two ad placeholder rectangles side by side, slightly overlapping or connected
- A shared label between them: "SAME ENTITY ID"
- Below: two outcome boxes showing what happens (limited reach, shared learning)
- Add label above: "ENTITY ID — CREATIVE SIMILARITY DIAGRAM"

**DARK CALLOUT**
When: script delivers a key rule or principle that gets a dark callout box on the slide
Build in Miro:
- Rounded rectangle, dark charcoal `#1F2937`, white text
- Top label (small, grey): "Rule to remember"
- Body text (bold, white): exact text of the rule from the script
- Size: 600 × 200px
- Add label above: "DARK CALLOUT BOX"

**PERSON ICONS SPLIT**
When: script contrasts two audience sizes (large pool vs small pool)
Build in Miro:
- Left side: 4–6 person icons clustered (representing large group)
- Right side: 1–2 person icons (representing small group)
- Labels below each group from the script
- Add label above: "AUDIENCE SIZE COMPARISON"

**TEXT-ONLY NOTE (no diagram)**
When: slide is yellow background, single statement — no diagram needed
Build in Miro:
- Yellow sticky note `#FBBF24`, black text
- Text: exact slide statement from the script
- This documents what goes on screen but tells the VA: text only, no build needed
- Add small label: "TEXT SLIDE — VA: no diagram"

---

## Step 5 — Add a Legend Frame

Create one additional frame at the far left of the board labelled:

```
LEGEND — [Video title]
```

Inside the legend frame, add:
- Board title and video title
- Date created
- List of all section frame names in order
- Colour key (amber = flow steps, orange = wrong path, teal = right path / outcome, pink = result, awareness colours)
- Note: "All SCREENSHOT NEEDED items in dark navy must come from Lorenzo before the Canva build starts"

---

## Step 6 — Output a Board Summary

After creating the board, output a summary in this format:

```
MIRO BOARD CREATED
------------------
Board name: [name]
Board URL: [url from miro response]
Total frames: [n]
Total diagrams built: [n]
Screenshots Lorenzo needs to supply: [n]

FRAME LIST:
- Legend
- Section 1: [name] — [n diagrams]
- Section 2: [name] — [n diagrams]
...

SCREENSHOTS NEEDED FROM LORENZO:
1. [exact description]
2. [exact description]
...
```

---

## Miro Tool Reference

The following MCP tools are available via `mcp__miro__*`:

| Tool | Use |
|---|---|
| `mcp__miro__create_board` | Create a new board with a given name |
| `mcp__miro__get_boards` | List existing boards |
| `mcp__miro__create_frame` | Create a labelled frame on the board |
| `mcp__miro__create_sticky_note` | Create a sticky note (good for callouts, labels, placeholders) |
| `mcp__miro__create_shape` | Create a shape (rectangle, rounded rectangle, etc.) |
| `mcp__miro__create_text` | Create a text label |
| `mcp__miro__create_connector` | Draw a connector/arrow between two items |
| `mcp__miro__create_card` | Create a card (for persona/node elements) |
| `mcp__miro__get_board_items` | Read existing items on a board |
| `mcp__miro__update_item` | Update an existing item |

For all create calls, set `parentId` to the frame's ID to place items inside the correct frame.

---

## Colour Reference

| Name | Hex | Used for |
|---|---|---|
| Growthub Yellow | `#FBBF24` | Yellow text slides, process step labels |
| Lavender White | `#F9F0FF` | Background reference |
| Dark Navy | `#1A1A2E` | Dark callout boxes, screenshot placeholders |
| Growthub Green | `#00D4A1` | Reference only (logo) |
| Coral / Orange | `#F97316` | Unaware stage, wrong path, Step 1 |
| Amber | `#F59E0B` | Problem-Aware, flow steps, general process boxes |
| Pink / Magenta | `#EC4899` | Solution-Aware, result boxes |
| Teal | `#14B8A6` | Product-Aware, recommendation / right path |
| Sky Blue | `#38BDF8` | Most-Aware stage |
| Red | `#EF4444` | Before state, highlight annotations |
| Green | `#22C55E` | After state |
| Dark Charcoal | `#1F2937` | Dark callout box background |
| Light Grey | `#F3F4F6` | Ad example placeholder fill |

---

## Handoff to VA

After the board is built, the VA uses it alongside `skills/youtube-canva-slides.md` and `skills/youtube-slide-visuals.md`. The Miro board is the structural reference. The Canva skills are the production spec. The VA does not need to interpret the script — every decision is already made in the board.

Tell the VA:
- Open the Miro board before opening Canva
- Build frame by frame, section by section
- Any dark navy item labelled "SCREENSHOT NEEDED" is a blocker — flag to Lorenzo before building that slide
- Text-only yellow sticky notes = text slides, build directly in Canva with no diagram

---

## Anti-Patterns

- Never put slide text into diagram boxes — diagrams show structure, not copy
- Never build a diagram for a text-only yellow slide
- Never leave a frame empty — if a section has only text slides, add the yellow sticky notes documenting them
- Never use stock icon styles that don't match the colour system above
- Never skip the Legend frame — the VA needs it to navigate the board
- Never create the board without first producing the Section Map — building without a plan creates a disorganised board
