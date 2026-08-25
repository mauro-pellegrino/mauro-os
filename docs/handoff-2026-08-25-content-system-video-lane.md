# Handoff: build the "full content system" YouTube lane

**Written:** 2026-08-25. **For:** the mauro-os Claude account.
**Deliverable:** one video board lane for @maurojpelle, plus ten HTML diagrams that carry it.

**Nothing in here has been pushed to Miro.** That is deliberate. Read this, build the diagrams
first, get Mauro's sign-off on the copy, and only then put the lane on a board.

Two of the ten diagrams are already built and rendered as a worked reference:
`content/boards/content-system-video/` holds `base.css`, `DIAG-01-the-brain.html` and
`DIAG-03-one-source.html` with their PNGs. Start from those rather than from scratch.

---

## 0. The constraints that override everything below

These come from `CLAUDE.md` §6 and §7 in this repo. If anything in this handoff conflicts with
them, they win.

| Rule | What it means here |
|---|---|
| **No em dashes. Ever.** | Including inside HTML diagram copy and inside file-path labels. Use a middot, a comma, or a full stop. I broke this twice while drafting the two example diagrams and had to go back and fix it. |
| **No "not X, but Y" reframes** | "A skill is a spec, not a prompt" became "A skill is a spec." Say the thing and stop. |
| **No trailing summary sentences** | Every block ends on its point. This applies to `.src` footers too. |
| **Never invent a number** | I wrote "survived nine months of me correcting it" into a draft footer. I do not know that it is true, so it came out and became a `[ NEEDS ]`. Do the same every time. |
| **Natural voice, not AI staccato** | These get read aloud on camera. If a block does not survive being spoken, rewrite it. |
| **Never name the agency, its founders, or any client** | The system is described as "the agency I run content for" at most, and only where Mauro has signed the line off. Default to describing the system in the first person without naming who it serves. |
| **Lane boundary** | This video is about **inbound and content systems**. It is not about ecom, brands, or Meta ad creative. If a diagram drifts into ad-creative territory, cut it. |
| **Nothing publishes without Mauro's review** | The lane is a draft until he approves it in chat. |

---

## 1. The video

**Format:** process breakdown. This is the first one of these produced for the channel, so mark the
lane `v1` and measure it after it goes out rather than treating the structure as settled.

**Audience:** the ICP in `CLAUDE.md` §2. An established agency owner, mid six figures a month and up,
who already knows AI should be writing their content and has no system for it. They are not
looking for prompts. They are looking at whether this is real and whether it would survive contact
with their own business.

**The promise:** you see the actual machine. Every folder, every file, every format, and the loop
that decides what gets made next week. Not a tour of a chat window.

**What has to be true by the end:** they can rebuild the skeleton themselves, and they believe the
person who built it runs it daily.

### Titles, four angles. Pick one, do not blend them

Ranked by how well they filter for the qualified operator rather than the widest audience.

1. **"I Built My Entire Content Team In Claude Code (Full System)"**
   *Recommended.* "Entire content team" is the operator's actual mental model of what this replaces,
   and "Full System" sets the expectation the video then over-delivers on. Maps exactly to what the
   lane contains.
2. **"The Claude Code Setup That Turns One Voice Note Into 9 Posts"**
   Most concrete, best thumbnail, weakest filter. Pulls in people who want the trick, not the system.
   Use it only if the channel needs reach more than it needs qualified viewers right now.
3. **"How I Run Content For An Agency In [X] Hours A Week"**
   Strongest hook for the exact pain in §2 of `CLAUDE.md` ("can't stay consistent, no time").
   **Blocked:** needs Mauro's real weekly figure. Do not fill the bracket with a guess.
4. **"Your AI Content Sounds Like AI. Here's The Fix."**
   Leads with their fear rather than the build. Good title, different video. Park it as its own idea.

**Series note:** this works as episode one of a repeatable series where each later episode opens one
folder in depth (`skills/`, then `research/`, then the weekly loop). Worth deciding before recording,
because episode one is written differently if it is a pilot.

---

## 2. The lane, act by act

The lane is one vertical spine read top to bottom. Block copy below is a starting draft, in Mauro's
voice, and every line of it is his to change. The `[ NEEDS ]` markers are hard blockers, not
suggestions.

### Head (frozen block, top of lane)

- **Status box:** `Lane 1 / Content System / Diagrams Built, Needs Voice Pass`
- **3 titles to test:** the three from §1 that are not blocked
- **Thumbnail note:** `[ NEEDS: thumbnail concept. ]` The strongest visual here is the repo tree
  itself on screen, which nobody in this niche shows.
- **The promise block:** *"Everyone tells you to use AI for content. Almost nobody shows you the
  actual system. This is mine, every folder and every file, running daily."*

### Act 1. The problem with how this normally goes

- Narration: the two ways agency owners currently do it. A chat window and a blank prompt every
  time, or a tool that writes in a voice nobody would recognise as theirs.
- Narration: why both stall. Nothing accumulates. Every session starts from zero, so month six looks
  exactly like month one.
- **Keeper `#ffdc4a`:** *"A prompt is a one-off. A system is something that gets better while you
  are not using it."*
- `DIAG-02` slot (the before/after).

### Act 2. The shape of the whole thing

- Section header: `The repo IS the system`
- Narration: it is a git repo of markdown files. No plugin, no product, nothing to buy.
- **`DIAG-01`** (built).
- Narration: CLAUDE.md is read at the start of every session, and the routing table is the part that
  does the work.
- **`DIAG-04`** (the routing table).
- **Keeper:** *"Skills are verbs. Brand is nouns. Get that split right and the same skills write for
  a completely different business tomorrow."*

### Act 3. What is actually inside a skill

The act that separates this from every other AI content video. Show one real file on screen.

- Section header: `Open one and look`
- Narration: pick `skills/content/long-form/_master.md` or the vehicle library, whichever reads
  better on camera.
- **`DIAG-05`** (anatomy of a skill file, annotated).
- Narration: the parts that matter are the trigger, the shape, the rules, and the anti-patterns.
  The anti-patterns are what stop the output drifting back to generic.
- **Keeper:** *"The anti-patterns section is the most valuable part of every file I have. It is a
  list of every way this has already gone wrong."*
- `[ NEEDS: screen recording of the real file, scrolled. ]`

### Act 4. One source, many formats

- Section header: `Where the leverage actually is`
- Narration: the source is a voice note, a call recording, or a thing that got built this week.
- **`DIAG-03`** (built).
- Narration: nobody writes nine times. Each format is a file that already knows its own shape.
- **`DIAG-06`** (the format library by funnel stage).
- **Keeper:** *"If your source is a topic, you get nine thin posts. If it is a real piece of work,
  you get nine that nobody else could have written."*

### Act 5. The loop that makes it a system

- Section header: `Performance, review, hypothesis, implementation`
- Narration: the weekly loop, straight out of `skills/ops/content-loop.md`.
- **`DIAG-07`** (the loop).
- Narration: what gets written back after a post ships, and why the write-back is the whole thing.
- **`DIAG-08`** (the compounding layer: learning protocol, memory, fetch-once-save-always, auto-push).
- **Keeper:** *"Corrections get written into the file. Say it once, it holds forever. That is the
  difference between a tool and a system."*

### Act 6. What it costs and what it does not do

The honesty act. It is what makes the rest believable to a sceptical operator.

- **`DIAG-09`** (time and cost). `[ NEEDS: Mauro's real hours per week and real tool spend. Do not
  publish this asset with estimates in it. ]`
- Narration: what it does not do. It does not have taste, it does not know what is worth saying,
  and it will happily produce something well-formed and pointless if the source is thin.
- **Keeper:** *"AI is leverage inside your workflow. It is not a replacement for knowing what is
  worth saying."*

### Act 7. Build the skeleton yourself

- Section header: `The version you can build this week`
- **`DIAG-10`** (the minimum viable version: one CLAUDE.md, one brand file, three skills).
- Narration: what to build first and in what order. Start with one format you already publish, not
  with the whole tree.
- CTA block `#bd0a0a`: `[ NEEDS: Mauro's current CTA and booking link. ]`

---

## 3. The ten diagrams

Every one carries the `@maurojpelle` tag and a `.src` footer. Specs below say what has to be
**legible**, which is the only test that matters for a board asset.

| id | shows | what has to be legible | status |
|---|---|---|---|
| **DIAG-01** | The brain file plus four folders | That it is plain folders, and which folder does what | **BUILT** |
| **DIAG-02** | Chat window vs system, side by side | That the left side restarts every time and the right side accumulates | to build |
| **DIAG-03** | One source fanning into nine formats | The count, and that each output names a real file | **BUILT** |
| **DIAG-04** | The routing table | That an incoming request maps to exactly one file. Use 6 to 8 real rows from `CLAUDE.md` §4 | to build |
| **DIAG-05** | Anatomy of one skill file | The four parts: trigger, shape, rules, anti-patterns. Annotate a real file | to build |
| **DIAG-06** | Format library by funnel stage | That there are enough formats to run months without repeating. Source: `skills/content/vehicle-library.md` | to build |
| **DIAG-07** | The weekly loop | That it is a closed circle and where the write-back happens | to build |
| **DIAG-08** | The compounding layer | Four mechanisms: learning protocol, memory, fetch-once-save-always, auto-push | to build |
| **DIAG-09** | Time and cost, honestly | The real weekly hours and the real spend | **BLOCKED on Mauro's numbers** |
| **DIAG-10** | The minimum viable build | That someone could start this Saturday with three files | to build |

**DIAG-06 caution:** `vehicle-library.md` says 39 formats, 13 in active use, and marks the rest as a
borrowed reference swipe library. Show the 13. If the 39 goes on screen, label the split, because
presenting borrowed formats as ours is the exact thing that file warns against.

---

## 4. The HTML style

Approved 2026-08-25. Any board asset made of type, boxes, tables, comparisons or a labelled process
gets authored in HTML and rendered, never hand-placed as shapes on the canvas.

### The palette, fixed

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#FAF6EC` | Background. Off-white, never pure white |
| `--ink` | `#1A1A1A` | Type and borders |
| `--yellow` | `#F3E3A3` | The one accent, and the handle tag |
| `--grey` | `#8A8578` | Kickers, labels, the source footer |
| `--red` | `#BD0A0A` | Only a failure state being called out |
| `--panel` | `#FFFFFF` | Card fills against the paper |

`base.css` in the assets folder is the shared sheet. Do not fork it.

### The handle tag, required on every diagram

Already in `base.css`. It sits bottom-right in the yellow, and `.src` reserves 340px of right
padding so the footer text wraps before it rather than running underneath.

```html
<div class="tag"><b>@maurojpelle</b><i>BUILD IN PUBLIC</i></div>
```

Keep the handle identical on all ten. The second line can change per diagram if there is a better
three-word label, but consistent beats clever across a set.

### Page rules that make them look like one set

- Inter, 900 weight on the headline. Loaded from Google Fonts.
- Borders 4 to 5px, `--ink`, square corners. No rounded corners, no shadows, no gradients.
- **One highlight per page.** The `.hl` span in the `h1` is usually it.
- A kicker above the headline, uppercase, letterspaced, grey.
- **The headline states the finding, not the topic.** "One brain file. Four folders." beats
  "Repo structure".
- Body type floor is 19px, headline 76px. These get re-shot off a screen share.
- **Fill the page.** Dead paper at the bottom is the standard defect. Fix it by cutting the body
  height, never by padding the content.

### Every diagram ends with a `.src` footer

Non-negotiable. It names what is Mauro's own, what is adapted from someone else, and what cannot be
verified. On a subject where everyone claims a system, the footer is what makes it credible instead
of another guru diagram. Saying the limit out loud is better content than a confident graphic.

### Render

```bash
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CH" --headless --disable-gpu --hide-scrollbars --allow-file-access-from-files \
      --virtual-time-budget=8000 --window-size=2400,1265 \
      --screenshot=DIAG-01-the-brain.png "file://$PWD/DIAG-01-the-brain.html"
```

Five things that cost time the first go:

- **`--window-size` must equal the file's `body{width;height}`.** Chrome shoots the window, not the
  document. A mismatch crops the bottom or leaves a slab of dead paper. 2,200 to 2,600 wide is the
  working range.
- **Without `--virtual-time-budget=8000`** the fonts have not loaded and the whole thing renders in
  Times.
- **`--allow-file-access-from-files`** the moment a page pulls in a local image.
- **`object-fit: contain`, never `cover`,** on any thumbnail grid. `cover` on narrow tiles slices
  images into unreadable ribbons.
- **Look at every render before it goes anywhere.** Every single one.

---

## 5. Putting the lane on Miro, when Mauro says go

This repo has no Miro skill, so the spec is inlined here.

### Block specs

| Role | Fill | Text | Width | Size |
|---|---|---|---|---|
| Section header | transparent TEXT | `#1a1a1a` | 12,362 | 288 |
| Sub-header | transparent TEXT | `#1a1a1a` | 6,181 | 144 |
| Narration | `#fff6b6` shape | `#1a1a1a` | 4,945 | 144 |
| Keeper line | `#ffdc4a` shape | `#1a1a1a` | 4,945 | 144 |
| Quote / borrowed voice | `#c6dcff` shape | `#1a1a1a` | 4,945 | 144 |
| Detail or list | `#fff6b6` shape | `#1a1a1a` | 4,945 | 121 |
| Production note | transparent TEXT | `#555555` | 4,945 | 80 |
| Open gap | `#e8e8e8` shape | `#bd0a0a` | 4,945 | 121 |
| CTA | `#bd0a0a` shape | `#ffffff` | 4,945 | 144 |
| Diagram image | | | 11,000 to 12,000 | |

Board yellow `#ffdc4a` is for **blocks**. Artwork yellow `#F3E3A3` is for **inside diagrams**. Swapping
them makes a diagram read as a block.

### Geometry

- **One spine. Every block centred on the same x.** Side by side only for a deliberate comparison row.
- **Never author a text block narrower than 4,000.** If it does not fit at 4,945, cut the copy.
- Vertical rhythm: `300` within a group, `800` between groups, `2,200` between sections.
- Height, computed and never guessed:

```
cpl    = width / (size * 0.62)
lines  = sum over <br/>-split segments of ceil(len / cpl)
height = (lines + 2) * size * 1.25
```

- **Generate the geometry in a script, assert zero overlaps, then emit one SVG.** Hand-placed y
  values are what produce a scattered lane. Images go in the same vertical flow as the text, not on
  top of it.

### Two API facts that will bite

- **`canvas_update_from_svg` will not change an image's height.** It comes back in `skipped[]` as
  `"image does not support updates to: height"`, the call still reports success, and the width still
  applies. Compute image heights from real dimensions, never from a height you want.
- **`board_list_items` returns `height: null` for every `textArea`.** An overlap check that filters
  on height silently skips every text item on the board. Do not report "no overlaps" off a check
  that only looked at shapes and images.

### Upload flow

`image_get_upload_url` → **one `curl -X PUT` per file** → `image_create` with the returned token. A
loop with `set --` mangled a presigned URL and returned a silent 400.

---

## 6. Blocked on Mauro

Nothing below can be filled in by guessing.

1. **Real weekly hours** running the system. Blocks DIAG-09 and title option 3.
2. **Real monthly tool spend.** Blocks DIAG-09.
3. **The CTA and booking link** for the close.
4. **Thumbnail concept**, and whether he is on camera at all.
5. **Sign-off on any line that references the agency**, per `CLAUDE.md` §1. Default is to keep it out.
6. **Which real file to open on camera** in Act 3, and a screen recording of it.
7. **Series or one-off**, which changes how Act 1 and the close are written.

---

## 7. Done means

- Ten diagrams rendered, every one carrying the handle tag and a `.src` footer, every one looked at.
- Zero em dashes anywhere in the diagram copy or the lane copy.
- Zero invented numbers. Every gap is a visible `[ NEEDS ]`, on the asset itself.
- Lane copy read out loud once, start to finish, before it goes on a board.
- Mauro has approved the copy in chat.
- Only then: build the lane, one spine, computed geometry, assert no overlaps.
