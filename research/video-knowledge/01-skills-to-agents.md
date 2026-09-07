# 01 · i moved my whole content engine from skills to agents (what broke)

**Alt title:** give me 12 minutes, i'll show you what agents actually change
**What this file is:** the information behind the video. Not a script. The script gets written from
this, and the board gets built from the script.
**Written:** 2026-09-07

**Sources**
- `research/transcripts/maurojpelle/installing-agents-what-changed-what-broke.md` (voice note, 2026-08-20)
- `research/transcripts/maurojpelle/moving-content-engine-from-skills-to-agents.md` (voice memo, 2026-08-06)
- `research/transcripts/maurojpelle/the-engine-skills-structure-skills-vs-agents.md` (voice note, 2026-08-20)
- `research/transcripts/maurojpelle/2026-08-06-voice-interview-skills-to-agents.md` (Q1 to Q8, raw)
- `~/growthub-os/.claude/agents/`, `~/growthub-os/skills/` (the live system)

**ICP cut:** the agency owner who already uses AI daily and is being told by everyone on X to
"switch to agents". He wants to know what actually changes and what it costs him.
**Reach cut:** the skills-versus-agents question is the loudest open argument in the AI-builder
lane right now, and almost nobody answering it is running the thing daily on real client work.

---

## The one claim

Agents are worth installing for the jobs where you already know what good looks like. Writing is
not one of those jobs yet, and saying so out loud is the whole credibility of the video.

---

## The information

### 1. What the setup was before

The starting point was ChatGPT projects through 2025 and early 2026. Different projects, different
instructions inside each one, and in practice everything happening in the same chat session. There
was no repo, no versioning, and no way for a correction made on a Tuesday to survive to Thursday.

That is the state most of the audience is in right now. Name it precisely, because they recognise
themselves in it and it earns the rest of the video.

### 2. What a skill is, in this system

A skill is a markdown file that owns one job: research, ops, content, lead gen, Miro, YouTube. The
repo splits them by activity, never by industry or client. `~/growthub-os/skills/` currently holds
**73 markdown files** across eight folders (`content`, `creative-strategy`, `dm-setting`, `lead-gen`,
`miro`, `ops`, `research`, `youtube`). `[measured: find skills -name "*.md" | wc -l, 2026-09-07]`

The property that matters is cumulative. Every correction goes back into the file, so the file is
worth more this month than last month. In his own words from the voice note: you keep building and
building, and it is satisfying to watch the folder grow.

### 3. What an agent adds

An agent runs without being asked. The first one installed checks Notion, tl;dv, Drive and Slack
before proposing anything, then writes blocks straight into the calendar. The stated target for the
next ones is proactive acquisition: agents that produce qualified calls with ecom operators at real
spend, rather than calls with people learning what AI is.

The time claim from the voice note, in his words: it saves time on things that used to take about
30 minutes a day, and those 30 minutes now go into building more agents.
`[observed: his own account in the 2026-08-20 voice note. Not measured, do not present as a metric.]`

### 4. What broke, honestly

Four failures, all from the transcripts, none invented.

| What broke | Why it matters |
|---|---|
| Failures you do not notice straight away | An agent that runs on a schedule fails quietly. Nothing shouts. You find it a week later. |
| Not enough context given to the model | The root cause under most of the surprises. The agent did what it was told, which was less than what was meant. |
| Output that is not what you pictured | Building from scratch means it never matches the picture in your head on the first pass. |
| The jump from a neat manual calendar | Coming from organised manual content into an AI running the day produces disparities, and that is the tax. |

### 5. The one thing deliberately kept as a skill

Writing. The reason given is direct: he corrects the skills constantly, and he wants the writing
close to him. Correcting a skill is a file edit he can see. Handing writing to something that runs
on its own removes the correction loop that made the writing good.

### 6. The ceiling, stated in his own words

He is not fully installing agents yet because he is not yet happy with what the skills produce.
The confidence that it gets there comes from the loop: correct the output, push the correction into
the skill, run it again. That loop is the actual product. Agents are what you install after it.

---

## Evidence

| Claim | Status |
|---|---|
| 73 skill files across 8 activity folders | `[measured: file count in growthub-os, 2026-09-07]` |
| First agent checks Notion, tl;dv, Drive, Slack and writes calendar blocks | `[observed: voice note 2026-08-20]` |
| About 30 minutes a day saved | `[observed: his own estimate, unmeasured]` |
| Writing stays a skill on purpose | `[observed: stated decision, 2026-08-20]` |
| Agents fail quietly and that is the main new risk | `[assumed: his description of the failures, generalised]` |

---

## Beats on camera

1. The setup everyone is in: projects and one endless chat.
2. What a skill actually is, on screen, one file open.
3. Why the split is by activity and not by client.
4. The cumulative property. Corrections make the file worth more.
5. What an agent adds: it runs without being asked.
6. The live example: Notion, tl;dv, Drive, Slack, then calendar blocks.
7. The honest time claim, framed as an estimate.
8. What broke, all four, no softening.
9. The one job kept manual, and why.
10. The ceiling: agents come after the skill is good, never before.
11. CTA.

---

## Do not say

- Any productivity multiple. "10x" is not in the source and does not belong here.
- That agents replaced the skills. They run on top of them.
- Any client name.
- That the migration is finished. It is explicitly not.

## Gaps

- `[NEEDS: the current count of installed agents and what each one does]`
- `[NEEDS: one concrete example of an agent failing quietly, with the date]`
