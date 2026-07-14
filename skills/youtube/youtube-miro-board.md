# YouTube Miro Board
**Version 2.0 | Updated 14 July 2026 | Retargeted to Mauro's channel (AI systems for agency owners)**

Takes a YouTube script and generates a full Miro board with all diagrams, graphs, and visual frames the VA needs to build the Canva slide deck. Board layout mirrors the channel's slide conventions in `skills/youtube/youtube-slide-visuals.md`.

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md.

---

## Step 0: Surface What's Already Available

Before requesting the script or touching Miro, check what already exists. Output what's found. Then ask for what's still needed.

### 1. Check for an existing script

```bash
ls /Users/mauro/mauro-os/brand/scripts/
grep -rli "[topic keyword]" /Users/mauro/mauro-os/brand/scripts/
```

(`brand/scripts/`: create this folder when the first script is saved.)

If a script exists: note the file path and confirm it's the right version.
If no script exists: flag this. The script must exist before the board can be built.

### 2. Check which visual types this topic will need

Based on the topic, identify which visual types from the Visual Type Library (below) are most likely to be needed. List them before asking for the script, so the requester knows what to expect.

For example, a video on "the AI content engine" will likely need:
- VERTICAL FLOW (the pipeline: record the call → pull insights → draft → human pass → schedule → measure)
- TWO-PATH COMPARISON (VA posting vs a measured engine)
- OUTPUT EXAMPLE LAYOUT (real posts or articles the engine produced)
- PROOF / DATA LAYOUT (analytics or booked-calls screenshots)

### 3. Output a pre-build summary

```
PRE-BUILD CHECK: [VIDEO TITLE / TOPIC]
----------------------------------------
Script status: [Found at brand/scripts/[filename] / Not yet written]

Visual types likely needed for this topic:
- [Visual type]: [which part of the video it will cover]

Assets Mauro will need to supply before the board is complete:
- [Screenshot / real output / data: what type and why]
```

### 4. Request what's still needed

After the summary, ask:

> "Here's where we are. [State what exists and what's missing.] Paste the script to proceed."

Wait for the script before building the board.

---

## When to Run This Skill

- A script has been written (from `skills/youtube/youtube-hook-script.md` or directly)
- Someone says "build the Miro board for this script"
- Someone says "create the visual plan" or "make the board"

---

## Inputs Required

1. **The full script**: section by section with slide cues
2. **Video title**: used as the board name
3. **Miro access**: via `mcp__miro` tools (requires session restart after first install)

---

## What the Board Contains

Each board is divided into labelled frames. One frame per section of the video. Inside each frame: the diagrams, flow charts, and data layouts the VA needs to build that section's slides in Canva.

The board does not duplicate slide text. It visualises structure: what the diagrams look like, how elements connect, what goes left vs right, how many items are in each row.

---

## Step 1: Parse the Script into Sections

Read the script. Identify every named section (usually marked as "SECTION X" or equivalent). For each section, note:

- Section name and number
- Which slides are text-only (yellow or lavender, no diagram needed)
- Which slides need a diagram or visual asset
- What type of visual is needed (use the type list below)

Produce a section map before touching Miro:

```
SECTION MAP
-----------
Section 1: [Name]
  Slides [X-Y]: text-only
  Slide [Z]: needs [visual type]

Section 2: [Name]
  ...
```

---

## Step 2: Create the Board

Use `mcp__miro__create_board` with the video title as the board name.

```
Board name: [Video title] — Visual Plan
```

---

## Step 3: Build One Frame Per Section

For each section, use `mcp__miro__create_frame` to create a labelled frame.

Frame naming convention:
```
SECTION [N]: [Section name]
```

Frame size: 2400 × 1600px minimum. Increase width if the section has many diagrams side by side.

Position frames left-to-right across the board in section order, with 200px gaps between them.

---

## Step 4: Populate Each Frame

Inside each frame, build the visual elements the VA needs. Use the visual type rules below to decide what to build for each slide.

### The Visual Type Library

**STAGE DIAGRAM (3-5 horizontal stages)**
When: any slide introducing a staged model (funnel stages, pipeline maturity, content-engine phases)
Build in Miro:
- 3-5 rounded rectangles in a horizontal row, connected by right arrows
- Labels (top, bold caps): the stage names from the script
- Colours in order: Coral `#F97316` / Amber `#F59E0B` / Pink `#EC4899` / Teal `#14B8A6` / Sky `#38BDF8`
- Short description text inside each box (what this stage means)
- Dark action label below each box (what to do at this stage)
- If a specific stage is highlighted in the script: add a red sticky note above that box labelled "← FOCUS"
- Add a text label above the row: "STAGE DIAGRAM: [model name]"

**SYSTEM MAP**
When: script introduces a named system or framework (e.g. the Content Engine)
Build in Miro as a connected tree:
```
[System name]
  └── Source (calls, delivery work, sessions)
        └── Extraction → [what gets pulled]
        └── Drafting → [which skill drafts what]
        └── Human pass → [what gets checked]
        └── Publish → [channels]
        └── Measure → [booked calls, replies, DMs]
```
- Use `mcp__miro__create_card` or sticky notes for each node
- Connect nodes with `mcp__miro__create_connector`
- Top-level nodes: amber `#F59E0B`
- Sub-nodes: white with black border
- Adjust the structure to whatever the script actually names; never force this exact shape
- Add label at top: "[SYSTEM NAME] MAP"

**VERTICAL FLOW (process / script structure)**
When: script walks through a step-by-step structure
Build in Miro:
- Vertical column of rounded rectangles, connected by downward arrows
- Each box: amber `#F59E0B`, black text, bold label
- Example flow: Record the call → Pull the insights → Draft with the skill → Human pass → Schedule → Measure
- Adjust labels to match whatever the script actually calls the steps
- Add label above: "PROCESS FLOW: [process name]"

**TWO-PATH COMPARISON**
When: script compares two approaches, two operator types, or two outcomes
Build in Miro:
- Two columns side by side, each headed by a rounded rectangle
- Path 1 (orange `#F97316`): the wrong/old approach
- Path 2 (amber `#F59E0B`): the right/new approach
- Recommendation box below (teal `#14B8A6`): what to do instead
- Result boxes below that (pink `#EC4899`): 3-4 outcomes
- Add label above: "TWO-PATH COMPARISON"

**BEFORE / AFTER**
When: script shows a transformation or result contrast
Build in Miro:
- Two side-by-side sticky notes or cards
- Before: red `#EF4444` background, white text, label "BEFORE"
- After: green `#22C55E` background, white text, label "AFTER"
- Arrow pointing right between them
- Add label above: "BEFORE / AFTER"

**HORIZONTAL PROCESS (3-5 steps)**
When: script describes a sequential process with 3-5 distinct steps
Build in Miro:
- Horizontal row of rounded rectangles, connected by right arrows
- Step 1: Orange `#F97316`
- Step 2: Amber `#F59E0B`
- Step 3: Pink `#EC4899`
- Step 4 (if exists): Teal `#14B8A6`
- Step 5 (if exists): Sky `#38BDF8`
- Short description text below each box
- Add label above: "PROCESS: [process name]"

**PROOF / DATA LAYOUT**
When: script references a dashboard screenshot, analytics figure, or result
Build in Miro:
- A placeholder sticky note in dark navy `#1A1A2E` with white text
- Text inside: "SCREENSHOT NEEDED: [exact description of what data / dashboard / figure Mauro needs to supply]"
- Size: 400 × 250px minimum
- Add a red sticky above it: "⚠ MAURO SUPPLIES THIS"
- Any number shown publicly needs Mauro's sign-off

**OUTPUT EXAMPLE LAYOUT**
When: script shows 1-3 real outputs (posts, articles, lead magnet pages, DMs)
Build in Miro:
- One rectangle per output. Posts/DMs: 300 × 500px (portrait phone ratio). Articles/docs: 400 × 300px (landscape).
- Border: dark grey `#374151`
- Fill: light grey `#F3F4F6`
- Text inside: "OUTPUT EXAMPLE: [brief description, e.g. 'X post that opened the $28k conversation' or 'lead magnet landing page']"
- Space examples 50px apart in a row
- Add label above: "OUTPUT EXAMPLES: [number] needed from Mauro"

**DARK CALLOUT**
When: script delivers a key rule or principle that gets a dark callout box on the slide
Build in Miro:
- Rounded rectangle, dark charcoal `#1F2937`, white text
- Top label (small, grey): "Rule to remember"
- Body text (bold, white): exact text of the rule from the script
- Size: 600 × 200px
- Add label above: "DARK CALLOUT BOX"

**PERSON ICONS SPLIT**
When: script contrasts two audience or group sizes (large pool vs small pool)
Build in Miro:
- Left side: 4-6 person icons clustered (representing large group)
- Right side: 1-2 person icons (representing small group)
- Labels below each group from the script
- Add label above: "AUDIENCE SIZE COMPARISON"

**TEXT-ONLY NOTE (no diagram)**
When: slide is yellow background, single statement, no diagram needed
Build in Miro:
- Yellow sticky note `#FBBF24`, black text
- Text: exact slide statement from the script
- This documents what goes on screen but tells the VA: text only, no build needed
- Add small label: "TEXT SLIDE — VA: no diagram"

---

## Step 5: Add a Legend Frame

Create one additional frame at the far left of the board labelled:

```
LEGEND: [Video title]
```

Inside the legend frame, add:
- Board title and video title
- Date created
- List of all section frame names in order
- Colour key (amber = flow steps, orange = wrong path, teal = right path / outcome, pink = result, stage-diagram colours)
- Note: "All SCREENSHOT NEEDED items in dark navy must come from Mauro before the Canva build starts"

---

## Step 6: Output a Board Summary

After creating the board, output a summary in this format:

```
MIRO BOARD CREATED
------------------
Board name: [name]
Board URL: [url from miro response]
Total frames: [n]
Total diagrams built: [n]
Screenshots Mauro needs to supply: [n]

FRAME LIST:
- Legend
- Section 1: [name], [n diagrams]
- Section 2: [name], [n diagrams]
...

SCREENSHOTS NEEDED FROM MAURO:
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
| `mcp__miro__create_card` | Create a card (for system-map node elements) |
| `mcp__miro__get_board_items` | Read existing items on a board |
| `mcp__miro__update_item` | Update an existing item |

For all create calls, set `parentId` to the frame's ID to place items inside the correct frame.

---

## Colour Reference

| Name | Hex | Used for |
|---|---|---|
| Brand Yellow | `#FBBF24` | Yellow text slides, process step labels |
| Lavender White | `#F9F0FF` | Background reference |
| Dark Navy | `#1A1A2E` | Dark callout boxes, screenshot placeholders |
| Accent Green | `#00D4A1` | Reference only (logo) |
| Coral / Orange | `#F97316` | Stage 1, wrong path, Step 1 |
| Amber | `#F59E0B` | Stage 2, flow steps, general process boxes |
| Pink / Magenta | `#EC4899` | Stage 3, result boxes |
| Teal | `#14B8A6` | Stage 4, recommendation / right path |
| Sky Blue | `#38BDF8` | Stage 5 |
| Red | `#EF4444` | Before state, highlight annotations |
| Green | `#22C55E` | After state |
| Dark Charcoal | `#1F2937` | Dark callout box background |
| Light Grey | `#F3F4F6` | Output example placeholder fill |

---

## Handoff to VA

After the board is built, the VA uses it alongside `skills/youtube/youtube-canva-slides.md` and `skills/youtube/youtube-slide-visuals.md`. The Miro board is the structural reference. The Canva skills are the production spec. The VA does not need to interpret the script: every decision is already made in the board.

Tell the VA:
- Open the Miro board before opening Canva
- Build frame by frame, section by section
- Any dark navy item labelled "SCREENSHOT NEEDED" is a blocker: flag to Mauro before building that slide
- Text-only yellow sticky notes = text slides, build directly in Canva with no diagram

---

## Anti-Patterns

- Never put slide text into diagram boxes: diagrams show structure, not copy
- Never build a diagram for a text-only yellow slide
- Never leave a frame empty: if a section has only text slides, add the yellow sticky notes documenting them
- Never use stock icon styles that don't match the colour system above
- Never skip the Legend frame: the VA needs it to navigate the board
- Never create the board without first producing the Section Map: building without a plan creates a disorganised board
- Never mock up a fake proof asset: real screenshot from Mauro or a labelled placeholder
