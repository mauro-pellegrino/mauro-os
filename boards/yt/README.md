# YouTube boards, record-ready (built 2026-10-07)

Three boards for Mauro's channel. Open the HTML by double-click and record off it. Each board is one
vertical column, 1600 px wide, cut into 900 px frames (16:9). One frame is one beat.

Every number on a board comes from `brand/claims.md`. The HTML comment above each chart names the row.
To change a number or a line, edit `build.py` and run `python3 boards/yt/build.py --png`. That
rewrites the three HTML files and the full-page PNG previews next to them.

## The three videos

| # | File | Source doc | Why this one now |
|---|---|---|---|
| 01 | `01-claude-code-content-system.html` | `research/video-knowledge/11` | The flagship. Every count (73 skills, 25 scripts, 4 agents, 64%, 649 of 678, 60,000 against 264,000) is already public through the 2026-09-10 article. |
| 02 | `02-x-ranking-weights.html` | `research/video-knowledge/05`, rebuilt | Highest-reach idea, and since 1 Oct every default weight in `param.rs` is verified. The old "no weights in the repo" premise is retired, so this board tells the January-to-August story. |
| 03 | `03-record-off-a-board.html` | `research/video-knowledge/10` | The format proves itself on screen. 4 hours to close to 2, the 200-item ceiling and the 37/17/20 batch are all cleared numbers. |

Left out on purpose: 03 lead magnets (its headline 4 of 541 is not in claims.md) and 08 impressions
vs calls (the whole dataset is another account, every panel would need that label).

## Titles, 3 options each

Modelled on the outliers in `skills/youtube/01-outliers.csv` and `research/charlie-morgan/`.

**01 · the content system** (about 14 minutes, 13 beats)
1. The Claude Code system behind a $300k/mo agency (full walkthrough). Credential anchor, the approved direction in `youtube-title-generator.md`. The $300k is the agency's number.
2. I built 4 Claude Code agents. Each one exists because something broke. Process transparency, modelled on Nate Herk "I Built the Ultimate Team of AI Agents".
3. Give me 15 minutes, I'll show you my whole Claude Code repo. Time box, modelled on Charlie Morgan "Give me 13 mins, I'll fix your addiction".

**02 · X ranking weights** (about 13 minutes, 14 beats)
1. I read X's ranking code so you don't have to. Save-you-effort authority, Charlie Morgan "I Ranked Every Online Business Model So You Don't Have To".
2. Every X algorithm number you've seen is from 2023. Belief-breaker.
3. X just published its algorithm weights (2026). Newsjack, David Ondrej "Google just destroyed all vibe-coding apps".

**03 · record off a board** (about 12 minutes, 13 beats)
1. I stopped reading scripts on camera. I record off a board. Belief-breaker. The board is built from the script, so the title never says "I stopped writing scripts".
2. You'll never read a script on camera again after watching this. Charlie Morgan's #1 shape.
3. How I build a YouTube board in 2 hours with Claude (step by step). Speed compression, "close to 2 hours" is cleared.

The length estimates assume about one minute a beat. They are a plan, not a measurement.

## How to record

- **Window:** Chrome at 1600 x 900 (or full screen at 1920 x 1080; the column stays centred). Hide the bookmarks bar.
- **Scroll:** the page snaps one frame at a time. Press Page Down or the space bar once per beat. Each frame fills the screen, and the next frame stays out of view.
- **Flythrough for the hook:** hold the down arrow from the top to the bottom. That takes about 10 to 15 seconds. Then press Home and start on the title card.
- **Per frame:** say the big line first. Then talk over the visual. The grey SAY line at the bottom is your note, so do not read it word for word.
- **SCREEN boxes:** a dashed box marks a cut to the real tool. Record that capture separately and drop it in during the edit. Or open the tool and show it live.

## Open SCREEN slots (a real capture is needed)

- 01: the repo tree in the terminal (blur the account folders), `ops/MAP.md` routing table, `skills/content/x-articles/`, last Monday's analysis (blur names).
- 02: 2 or 3 real posts that quote the 2023 numbers, `github.com/xai-org/x-algorithm` with the stars and last push read live, a live search of `param.rs` for `ShareViaCopyLink`.
- 03: take 1 and take 2 of the same line (script, then board), and a five-second clip of a scripted read for the hook.

## Open NEEDS before recording

- 01 beat 3: the time lost to the rebuilt SOP. `MAP.md` says 45 minutes, and claims.md does not carry it yet.
- 03 beat 8: Mauro's verdict on the rect-for-narration substitution (from doc 10).
- All three: the CTA. Every board says `[CTA: confirm the current offer and link]`.
