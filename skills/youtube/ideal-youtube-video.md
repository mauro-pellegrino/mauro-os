# Ideal YouTube Video: Top-to-Bottom Blueprint
**Version 1.0 | Created 4 August 2026 | Mauro's channel (AI systems for agency owners)**

This is the canonical blueprint for a Mauro video, top to bottom. Give it a topic and the system being taught, and it produces a full script in one pass, structured so every beat maps 1:1 to a section on the Miro board. It is the front door for the video pipeline: this skill writes the script, then `skills/youtube/youtube-miro-board.md` turns that script into the board.

It supersedes the fragmented flow (idea → hook → script) for framework videos. Use it when the goal is "write me the video."

---

## Required Reading
Before writing a single line, read `brand/voice.md` and `brand/audience.md` in full. Every line must pass the 60-Second Pre-Publish Checklist at the bottom of voice.md. Speak to the ICP in audience.md: established agency owners installing AI systems, never beginners.

---

## The One Format

Mauro's channel runs on one repeatable format, validated against the top-performing framework videos in `research/charlie-morgan/charlie-morgan-dig.md`:

**A named framework, drawn as a diagram, narrated top to bottom, with the real engine shown on screen.**

- Every video teaches one system and gives it a **proprietary name** ("Time Compression Theory," "The Downfall Plan" are the reference-class examples). The name is the packaging.
- The framework is a **visual spine**: a now-state → future-state road, a funnel, a pipeline, or a tiered breakdown. The board IS the video.
- Proof is **shown, not claimed**: real skills, real posts, real dashboards on screen as Mauro narrates.

If the topic can't be drawn as one diagram with a name, it isn't a video yet. Tighten it until it can.

---

## Inputs (ask only for what's missing)

Run a fast check first, then ask for the gaps in one message:

```bash
grep -rli "[topic keyword]" /Users/mauro/mauro-os/research/ /Users/mauro/mauro-os/brand/
ls /Users/mauro/mauro-os/brand/social-proof/ 2>/dev/null
```

1. **The system being taught.** What repeatable process is this video documenting? (a real skill, the transcript-to-content pipeline, the weekly acquisition analysis, skills → agents, etc.)
2. **The framework name + shape.** If Mauro hasn't named it, propose 2-3 names and the diagram shape (road / funnel / pipeline / tier list).
3. **The real proof to show on screen.** Which screenshots, outputs, or dashboards back it. Pull from `brand/social-proof/` first.
4. **Any numbers.** Real ones only. Anything unconfirmed goes in as a `[bracket placeholder]` for Mauro to confirm on camera. Never invent a number.

If a competitor covered this and the transcript isn't saved, flag it. Fetch and save to `research/transcripts/[handle]/` only if Mauro asks.

---

## The Top-to-Bottom Anatomy

Nine beats, in order. Each beat is one board section. Write the script beat by beat; the board is assembled from the same beats.

### Beat 1 — Cold-open hook (0:00-0:15)
One declarative, contrarian line that makes the right viewer feel they're making this mistake. No question. No "in today's video." No "most agencies."
> "You've built the inbound machine for every client you have. You never built your own."

Model the title/hook energy on the dig's winners: absolutes + curiosity ("You'll never X again"), fake-precise stats, time boxes ("give me 10 minutes"). Keep it in Mauro's plain voice, not guru voice.

### Beat 2 — Stakes anchor (0:15-0:45)
Why this is costing them right now. Land the pain in the ICP's own words (referrals drying up, posting into silence, the cobbler's children gap). One credibility anchor, woven in, never foregrounded: "everything here is based on the engine I run every week for a real agency." Numbers get a bracket until signed off.

### Beat 3 — The promise / roadmap (0:45-1:15)
One or two sentences stating exactly what they'll walk away able to do. Name the framework here for the first time: "I call this [Framework Name], and by the end you'll have the whole thing."

### Beat 4 — The framework reveal (the spine)
Show the full diagram once, whole, before breaking it down. This is the now-state → future-state road (or funnel / pipeline). Left = where they are (broke pipeline, manual posting, silence). Right = where the system gets them (booked calls from content). The middle is the system. This single frame is the thumbnail candidate and the board's centrepiece.

### Beat 5 — Walk the framework, node by node
For each node in the diagram, run the teaching pattern: **principle → why it matters → real example → what to do.** Introduce what's commonly done wrong first, then what Mauro does instead, then a real artifact on screen (a skill file, a real post, a real week of output). Use spoken numbering ("first," "then," "and then"), never "Step 1, Step 2." This is the longest beat and the bulk of the board.

### Beat 6 — Show the proof (demonstrate, don't assert)
Pull back from theory and show the engine running: the dashboard, the booked-calls tracker, the actual output the system produced. Spoken line and on-screen proof happen together. Every public number carries a sign-off flag.

### Beat 7 — The contrarian turn (the mistake most make)
The one thing that makes this fail even when people try it. This is the save-worthy beat. Ground it in something Mauro has actually seen (VA posting that produced nothing, volume without a map). State the real cause directly, no "that's not X, it's Y."

### Beat 8 — Recap (2 sentences, hard stop)
Pull back to the top-level point in one or two sentences. End on the point. No trailing summary sentence beyond this.

### Beat 9 — Qualified CTA + next tease
The audience filter appears here every time: established agency owners. Low-commitment CTA, never a hard sell ("if you run an established agency and want this installed, [current CTA]"). Invite DMs/comments for everyone else. Optional one-line tease of the next video. `[CTA: confirm current offer/link with Mauro before recording.]`

---

## Voice Layer (non-negotiable)

Pulled from `brand/voice.md` and `skills/youtube/youtube-hook-script.md`:

- **No em dashes. Ever.** Commas, periods, or parentheses.
- **No "not X, it's Y" reframes.** Say the cause directly.
- **No "most brands / most people" openers.**
- **No trailing summary sentence** after the recap.
- **Short sentence to land the point, longer sentence to explain it.** Repeat the core idea in different words. Spoken, slightly run-on, not polished broadcast English.
- **Name the tool:** "Claude," not "AI tools." Real skill names, real file names.
- **Operator to operator.** No hype adjectives, no leading with credentials, no beginner framing.
- Full ban list lives in the Anti-Patterns section of `youtube-hook-script.md`. Apply all of it.

---

## Output Format

Produce two things in one pass:

**1. The full script**, written beat by beat with the timing markers above, in spoken voice, ready to record. Bracket every unconfirmed number and the CTA.

**2. A board outline**, one line per beat, naming the diagram type for each, so `skills/youtube/youtube-miro-board.md` can build the Miro board directly:

```
BOARD OUTLINE: [Video title]
Framework name: [name] · Spine shape: [road / funnel / pipeline / tier]
B1 Hook        → title card + hook line
B2 Stakes      → [visual]
B3 Promise     → framework name reveal
B4 Reveal      → FULL DIAGRAM (now → future) [thumbnail candidate]
B5 Node walk   → [one sub-frame per node]
B6 Proof       → [screenshots/dashboards to supply]
B7 Turn        → [visual]
B8 Recap       → single frame
B9 CTA         → CTA card
Assets Mauro must supply: [list of real screenshots/outputs]
```

---

## Routing After This Skill

1. Script approved → `skills/youtube/youtube-miro-board.md` builds the board from the board outline.
2. Board built → push to Miro (via the Miro MCP once wired, or Claude-in-Chrome + the Miro extension).
3. Titles → `skills/youtube/youtube-title-generator.md`. Model on the dig's title formula.

---

## Guardrails

- Nothing publishes without Mauro's review. The script is a draft until he approves it in chat.
- Never name a client. Anonymise as "a B2B agency I run this for."
- Never invent a number. Bracket it or cut it. Every public figure needs Mauro's sign-off.
- If the topic won't collapse into one named diagram, it's not ready. Say so instead of forcing it.
