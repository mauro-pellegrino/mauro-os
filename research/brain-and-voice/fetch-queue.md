# Company brain + voice doc research: fetch queue

> **STATUS: QUEUED, NOT FETCHED. NOT ADOPTED.** Built 2026-09-29 for the phase 1 research Mauro asked
> for (the company brain and the voice document, best version for the ICP, for Brando's install and
> for internal use). The transcripts could not be pulled: the session's network policy blocks
> youtube.com. When they are fetched, each goes to `research/transcripts/<channel-handle>/` with
> title, URL and fetch date, then `synthesis.md` plus an adopt / adapt / reject table goes in this
> folder. Nothing reaches `skills/` before Mauro signs off row by row.

**How these 20 were picked.** Four web searches restricted to youtube.com, 40 results, cut to 20 on
title fit. Search results carry no view counts or channel sizes, so this list is selected on
relevance, not performance. Add views when the transcripts are pulled, per the corpus rule that views
are the number that picks an outlier. Shorts and developer-only CLAUDE.md tutorials were cut.

**The lens for the synthesis.** Every video gets read against what mauro-os already runs, since this
repo is itself a working company brain: `CLAUDE.md` as the index, `brand/` as context, `brand/claims.md`
as the fact list, `brand/voice.md` built from voice notes, the Gate as the check. The question per
video is what it does that this repo does not, and whether that survives an agency owner with an
hour a day.

## Business brain / context system (12)

| # | Title | URL | Why it's in |
|---|---|---|---|
| 1 | How to setup a business brain (powered by Claude) | https://www.youtube.com/watch?v=7-yAe5Tzn0U | the exact concept, named the same way |
| 2 | I Turned My Second Brain Into Claude's Context Engine (Full Setup) | https://www.youtube.com/watch?v=LGwv4qXGgEo | brain as context engine, full setup |
| 3 | Every Way To Set Up A Claude Second Brain Explained | https://www.youtube.com/watch?v=l8MWXsYk6Mo | survey of approaches, good for the comparison table |
| 4 | Better With This Setup (CLAUDE.md + Skills + MCPs) | https://www.youtube.com/watch?v=pBHKTojO1YY | the three-layer stack this repo uses |
| 5 | Claude Code Setup Guide By The Creator Himself | https://www.youtube.com/watch?v=pGro_uKt-_M | primary source on how CLAUDE.md is meant to work |
| 6 | Build Your Second Brain With Claude Code, Karpathy's Method | https://www.youtube.com/watch?v=lnsExa1UbnM | the LLM-wiki method |
| 7 | Claude Code + Obsidian: Build a Second Brain That Actually Learns | https://www.youtube.com/watch?v=XuRfik_tHd4 | self-updating brain, maps to the learning protocol |
| 8 | I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How) | https://www.youtube.com/watch?v=jYMhDEzNAN0 | brain plus skills |
| 9 | How To Build The ULTIMATE AI Second Brain (Obsidian + Claude Code) | https://www.youtube.com/watch?v=4l8MXYUqGaA | maximalist version, useful as the upper bound |
| 10 | Build A Claude Knowledge Base That Self-Improves! | https://www.youtube.com/watch?v=ib74sLgjIBM | self-improvement loop |
| 11 | I Built a Company-Wide Construction Knowledge Base with Claude (Rates, Lessons, Past Jobs) | https://www.youtube.com/watch?v=u_f43RjQftA | closest analog to "past client work into the brain", off-industry |
| 12 | The Claude Code Skills That 5x'd Her Agency | https://www.youtube.com/watch?v=_KJOJdA___k | the only agency-owner case in the results |

## Voice document (8)

| # | Title | URL | Why it's in |
|---|---|---|---|
| 13 | How to Teach Claude to Write Content Like You | https://www.youtube.com/watch?v=yh_fZZVbNwc | core voice-doc method |
| 14 | How to Make AI Write in YOUR Voice (Claude Skill Tutorial) | https://www.youtube.com/watch?v=C1snRnGbNRM | voice as a skill, the pattern this repo uses |
| 15 | Claude Projects Instructions That Make AI Sound Like You | https://www.youtube.com/watch?v=e59Ha7Dquao | about.me and brandvoice.md files named explicitly |
| 16 | How to Train AI to Write in Your Exact Tone of Voice (Step-by-Step Claude Tutorial) | https://www.youtube.com/watch?v=SUAgeDmqvno | step-by-step extraction |
| 17 | How to Make Claude Write in YOUR Voice (The Complete Setup Guide) | https://www.youtube.com/watch?v=2XhcBr1DFk0 | two-part system, compare to voice.md plus the Gate |
| 18 | LIVE: Using Claude to create your brand voice prompt (so your AI sounds human) | https://www.youtube.com/watch?v=WYafEFr7r5Q | long-form live build, likely the most detail |
| 19 | How to Create a "Brand Voice" Instantly w/Claude.ai | https://www.youtube.com/watch?v=_wdsBPOQlaU | the fast version, the one an hour-a-day owner would actually do |
| 20 | Build Your Brand Identity with Claude AI (Voice, Positioning & Tagline) | https://www.youtube.com/watch?v=q5ZeKizhaIU | voice tied to positioning, the way brand/ is structured here |

## What each synthesis row has to answer

1. What goes in the brain, file by file
2. How the voice gets captured: from writing, from speaking, or from both
3. How it stays current, and who updates it
4. How much setup time it takes, stated or implied
5. What it does that mauro-os does not
6. Whether it survives an established agency owner with about an hour a day
