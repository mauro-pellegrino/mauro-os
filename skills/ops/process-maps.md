# Process maps

A map of every content process that gets booked calls, with the time each step takes and who holds it. It shows where human time goes and which process to fix first. The same method works for Mauro's own engine and for an agency owner's engine during a Ghosted Calls install.

North Star: **booked calls per hour of human time.**

## Tools (`tools/process-maps/`)

| File | What it does |
|---|---|
| `overview.json` → `build_overview.py` → `overview.png` | The whole system on one page. Edit the JSON, never the HTML. |
| `build_grouped.py --json specs/<name>.json` | One process in style D, with the time strip. PNG lands next to the spec. |
| `specs/_example.json.txt` | The spec format with every key explained |
| `specs/linkedin-lead-magnet-autodm.json` | A worked example, all times `? MIN` |
| `queue.csv` → `ranked_queue.py` | The ranked queue. Fill the CSV, run the script. |
| `assets/` | Screenshots a spec can show next to a step (`"img": "file.png"`) |

## The system

```
inputs -> processes -> shared -> weekly review -> back to inputs
```

- **Inputs:** where the raw material comes from each week. Template intake (outlier posts from profiles you track), your real work (calls, chat, docs), the market, last week's numbers, partner briefs.
- **Processes:** one shipped output each, grouped by channel.
- **Shared, drawn once:** the gate, the staging page, the person who ships. Never copied into every map.
- **Weekly review:** Monday fills the "this week" line on every process (shipped, your minutes, calls) and adds one changelog line. What won goes back into the inputs.

## Rules

1. **Size rule.** A process has one trigger, one shipped output, one person who presses go, one number that moves on Monday, and 6 to 12 steps. Smaller is a step inside a process. Bigger is a channel. Shared steps become modules. X or LinkedIn is a switch inside one process.
2. **Times.** A time goes on the map only when a timestamp or a document backs it. Everything else shows `? MIN` (write `"time": null`). An honest clean-run estimate can sit in the foot line, marked est.
3. **One process at a time.** Map one, check it with the person who runs it, then the next. Never draw every process in one go.
4. **Outlier.** A post's number divided by that account's own median over its last 10 to 20 posts. Compare to their normal, never to yours.
5. **No sticky notes.** Boxes, side notes and chips only.

## Style D

- Human steps are single boxes down the left. Each has a side note that says exactly what to do, max 4 lines.
- Consecutive Claude steps sit in one orange block on the right. Each step lists chips for the skills and tools it uses, the output after an arrow, and an optional dashed branch note.
- Arrows run in and out of the block.
- **Time strip** at the bottom, value-stream style: one cell per step, coloured by who holds the work, striped where the step waits on someone (`"wait": true`). Waiting is where processes lose days, so it gets its own mark.

**Colours (the `who` key):**

| Key | Who | Colour |
|---|---|---|
| `Y` | You, the owner | yellow `#F7D95C` |
| `C` | Claude (the orange block) | orange `#F2B69A` |
| `V` | VA | green `#A8E6B4` |
| `P` | Partner | pink `#FFC2D1` |
| `K` | Client | grey `#D7D2C8` |
| `R` | Monday review | purple `#E9D8FD` |

## The ranked queue

The order to fix processes in. Fill `queue.csv` every Monday, one row per process:

`process, posts, reach_x_calls, matched_calls, human_min`

- `reach_x_calls`: mean per post of (reach divided by the account's own median) times (1 + matched calls).
- `matched_calls`: booked calls on the post day or the next day whose source matches the channel. Day-level only, so posts on the same day share the calls. Read it as relative.
- `human_min`: minutes of human time per post, from a timed run. Blank until timed.

`ranked_queue.py` ranks on calls per human hour where `human_min` is filled, then on reach x calls, and puts rows with no numbers at the bottom as "no data yet". Never fill a blank with a guess.

## How to present them

Three levels, the standard sequence from process improvement (SIPOC to scope, flow for handoffs, value stream map for time and waste):

1. **Overview, one page** (`overview.png`). Scope only. It answers "is anything missing, and is anything on it that we never run".
2. **Ranked queue.** Processes in the order to fix, by calls per human hour.
3. **One map per process** in style D, with the time strip.

Maps fail when they get drawn once and never opened. This one is generated from data and updated every Monday.

## Steps for a new map

1. Copy `specs/_example.json.txt` to `specs/<process>.json` and remove the notes under the JSON.
2. Walk the process with the person who runs it. Write each human step with its side note, and group consecutive Claude steps.
3. Leave every untimed step as `null`.
4. Run `python3 tools/process-maps/build_grouped.py --json specs/<process>.json`.
5. Open the PNG and check: no text runs outside a box, the arrows connect, the time strip has one cell per step.
6. Set the process to `mapped` in `overview.json`, add a changelog line, run `build_overview.py`.
