# ascii-anim

Turns a static ASCII diagram (`.txt`) into an MP4 where the diagram draws itself. Text types in with a cursor, box borders sweep in row by row, arrowheads land in the accent colour, packets then flow along every connector that ends in an arrow, and one target pulses. The window is the same terminal frame as `content/ascii/render.py`, so the video matches the stills.

## Run

```
python3 tools/ascii-anim/ascii_anim.py content/ascii/founder-content-engine.txt \
  --theme dark --highlight "GATE: a second AI checks voice · claims · slop"
```

| Flag | Default | What it does |
| --- | --- | --- |
| `--theme` | `dark` | `dark` (gold accent) or `cream` (red accent), palettes copied from `render.py` |
| `--size` | `both` | `1080x1080`, `1600x900`, `both`, or any `WxH` |
| `--highlight` | largest box | Text to pulse. If it sits inside a box, the whole box pulses. Otherwise the text run pulses |
| `--handle` | `@maurojpelle` | Footer handle, e.g. `@lorenzo_pravata` |
| `--reveal` | `9` | Target seconds for the draw-in. Typing speed adapts to the amount of text |
| `--hold` | `5` | Seconds of flow and pulse after the draw-in |
| `--fps` | `30` | Frame rate |
| `--out` | `examples/` | Output folder |
| `--gif` | off | Also write a GIF. X converts GIFs to soft MP4s, so post the MP4 |
| `--loop` | off | Seamless loop. `--loop` or `--loop draw`: draws in, flows, fades back to the empty window. `--loop steady`: flow and pulse only. See below |

Output: `<name>-<theme>-<W>x<H>.mp4`, H.264, yuv420p, faststart. A 14 second video is about 0.3 to 0.5 MB and renders in about 30 seconds.

Needs Google Chrome, python3 `playwright` (it drives the installed Chrome, no browser download) and `ffmpeg`.

## Loop mode

X autoplays a video in the feed and restarts it at the end. Without `--loop` the restart jumps from a full diagram to an empty window. `--loop` removes the jump.

| Mode | What plays | Use it for | File |
| --- | --- | --- | --- |
| `--loop draw` (default for `--loop`) | Draw-in, then the flow and pulse for whole periods, then a 0.8 s fade back to the empty window that frame 0 shows | X posts: the draw-in replays on every loop | `<name>-<theme>-<W>x<H>-loop.mp4` |
| `--loop steady` | The diagram is already drawn. Only the flow and the pulse run, exactly whole periods | `<video autoplay loop muted playsinline>` inside YouTube HTML boards and article diagrams | `<name>-<theme>-<W>x<H>-steady.mp4` |

How the seam stays invisible:

1. Every motion runs on one shared period. The period is a whole number of frames, so it repeats exactly.
2. Every connector wraps on that period. A short connector carries 2 or more packets per period, so it does not sit dark.
3. The pulse runs a whole number of beats per period.
4. `--hold` sets the minimum loop time. The script rounds it up to whole periods.
5. After the render, the script compares frame 0 with the frame after the last one and prints `seam max pixel diff N/255`. 0 or 1 is invisible.

```
python3 tools/ascii-anim/ascii_anim.py content/ascii/process-size-rule.txt \
  --theme cream --size 1080x1080 --loop --highlight "A PROCESS HAS ALL FIVE"
```

Loops work best on a less crowded diagram with at least one connector that ends in an arrow. A diagram with no arrows only pulses.

## How it works

1. The script reads the grid and sorts each cell into text, structure (box and line chars, `+-|=` in ASCII boxes) or arrowhead (`▼ ► ◄ →`, `v` under a `|`, `>` after a `-`).
2. It finds the boxes (`┌┐└┘` or `+--+` / `+==+`), and the connectors that end in an arrow.
3. It gives each cell an appear time: rows top to bottom, structure sweeps left to right, text types.
4. Python writes one HTML page with a `seek(t)` function. Playwright steps time frame by frame in headless Chrome at 2x, and pipes the screenshots to ffmpeg, which scales down with lanczos. The frame steps are exact, so no frame drops.

## Write diagrams for animation

- Tall diagrams (30+ rows) fit the 1080x1080 frame best. In 1600x900 they leave empty sides. Wide banners (100+ columns) suit 1600x900 only.
- The flow packets follow connectors that end in an arrowhead. A plain `|` with no arrow stays still.
- Keep the box edges aligned. A box with a ragged bottom edge still draws, but looks off in the stills too.

## Examples

`examples/` holds the two prototypes, each at 1080x1080 and 1600x900:

- `founder-content-engine-dark-*`: Unicode boxes, three branches, the GATE line pulses.
- `process-map-one-process-cream-*`: ASCII `+==+` boxes, `v` arrows, the CLAUDE block pulses.

And the loop example (8 Oct), 1080x1080, cream:

- `process-size-rule-cream-1080x1080-loop.mp4`: 16.3 s, draws in, 4 periods of 1.6 s, fades out. Seam diff 0/255.
- `process-size-rule-cream-1080x1080-steady.mp4`: 6.4 s, 4 periods, flow and pulse only. Seam diff 1/255.

The rule text in `process-size-rule.txt` is unconfirmed in `brand/claims.md`. The example shows the format only.

## Options checked (8 Oct 2026)

| Option | X format | Cost | Match to the X examples | Claude end to end on this Mac |
| --- | --- | --- | --- | --- |
| HTML/JS page captured frame by frame + ffmpeg (this tool) | MP4 | $0 | Closest: typing, drawing, glow, any palette | Yes |
| Remotion (React video) | MP4 | $0 for individuals, company licence above a size limit | Close, more setup per video | Yes, heavier |
| VHS by Charm (`.tape` script) | MP4, GIF | $0 | Good for terminal typing, nothing moves after the text lands | Yes (`brew install vhs`) |
| asciinema `.cast` + agg / svg-term | GIF, SVG (X refuses SVG) | $0 | Text streams in only | Yes, with ffmpeg for MP4 |
| Manim (`Write` on text) | MP4 | $0 | Poor: reads as a maths video, slow on big text blocks | Yes, needs cairo and pango |
| ASCII Motion (ascii-motion.app) | MP4, WebM, GIF | Free core, paid cloud | Good, keyframes by hand in the editor | Partly. It has an MCP server; headless export is not verified |
| asciiflow, Monosketch, Cascii | static only | $0 | Draft tools, no animation | n/a |

X limits: MP4 up to 140 s and 1920x1200 on standard accounts. GIF up to 15 MB on web, about 5 MB on mobile, and X converts it to MP4.

Sources: Ina Toncheva on Claude-built animated diagrams captured with a headless browser (inatoncheva.substack.com/p/claude-builds-animated-diagrams-now), github.com/charmbracelet/vhs, github.com/cameronfoxly/Ascii-Motion, remotion.dev/prompts/launch-video-on-x, github.com/tungs/timecut. The tool credits on single X posts come from search snippets: x.com blocks fetches.
