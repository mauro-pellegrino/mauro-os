# 11 · our $100k/mo claude code content system

**Alt title:** the full claude code build behind an agency's inbound
**What this file is:** the information behind the video. Not a script.
**Written:** 2026-09-07

**Sources**
- `~/growthub-os/` in full: `ops/MAP.md`, `ops/CONVENTIONS.md`, `skills/` (73 files), `.claude/agents/`
  (4 agents), `ops/tools/` (25 scripts), `ops/daily/`, `BACKLOG.md`
- `skills/ops/daily-ops.md` (v3), `skills/ops/content-loop.md`, `skills/ops/monday-acquisition-analysis.md`
- `research/transcripts/maurojpelle/the-engine-skills-structure-skills-vs-agents.md`

**ICP cut:** the owner who has heard "I built a system in Claude Code" fifty times and has never
once been shown the repo.
**Reach cut:** this is the flagship. A full system tour with the file tree on screen, the failures
that shaped it, and the numbers with their sources attached.

---

## ⚠️ The number in the title, before anything else

**What Mauro said, 2026-09-07, verbatim:** *"$100k/mo is that clients closed from x & li form a
$150k/mmr, but I've closed more than that month by month I think, probably around $500k total."*

That is three different claims and they cannot be used interchangeably on camera.

| Claim | What it would mean | Safe to say |
|---|---|---|
| **$100k/mo** | The title as given. Reads as monthly revenue attributable to the engine. | Only with the definition attached |
| **$150k MRR** | Clients closed out of X and LinkedIn, currently on the books as recurring | Needs confirming as current, not peak |
| **~$500k total** | Cumulative closed across months, not a monthly figure | Carries "I think" and "probably" in the source |

**The rule that applies:** never invent a number, and any specific public figure needs sign-off. The
source sentence carries two hedges, so none of these is camera-ready as stated. `$300k/mo` remains
the one pre-cleared figure for the agency itself.

**The safe version of the title's claim**, if the $150k is confirmed: *clients closed out of X and
LinkedIn represent about $150k in monthly recurring revenue.* That is a closed-revenue claim, which
is stronger than a vague monthly attribution and easier to defend, because it names the channel and
the contract type.

`[NEEDS: confirm the $150k MRR is current rather than peak, and confirm what the ~$500k counts:
cumulative contract value, cumulative cash collected, or something else]`
`[NEEDS: final call on which figure the title uses]`

---

## The one claim

The prompts are the least interesting part. What makes it worth $100k a month is that every
correction is permanent, every number traces to a script, and four agents now run pieces of it
without being asked.

---

## The information

### 1. The skeleton

One repo. Eleven top-level areas, each with an owner and an entry point, all indexed in `ops/MAP.md`.

| Area | Owns |
|---|---|
| `skills/` | 73 markdown files across 8 activity folders |
| `.claude/agents/` | the 4 installed agents |
| `ops/` | conventions, the map, the daily system, 25 analysis tools |
| `research/` | article studies, creative examples, competitor digs, the evidence behind every rule |
| `accounts/` | per-account positioning and exports |
| `acquisition-calls/` | the Monday analysis, one dated file per week |
| `outbound-calls/` | the cold-email motion end to end, context, playbook, dial sheet, inbox replies |
| `emails/`, `brands/`, `recaps/`, `future-projects/` | the rest of the operation |

The rule that holds it together: **work is not finished until it is routed.** A thing that exists
and is not in the map gets rebuilt by the next agent. That rule was written the day an agent
rebuilt an outbound SOP from scratch and lost 45 minutes.

### 2. The skills, split by activity

Eight folders: `content`, `research`, `ops`, `miro`, `lead-gen`, `youtube`, `creative-strategy`,
`dm-setting`. **73 files.** `[measured: 2026-09-07]`

Never split by client. A client folder rots when the client leaves and the same skill gets rebuilt
inside the next one. An activity survives every client.

The notable ones to actually open on camera:

- **`skills/content/x-articles/`**, seven files. Six in a fixed order that turn any transcript into
  a published article, plus a seventh whose only job is keeping the other six honest as evidence
  lands. Every number they cite lives in one corpus file read from 41 real captures.
- **`skills/ops/monday-acquisition-analysis.md`**, the weekly acquisition read. Four inputs, a
  fixed ten-section structure, a diff against last week on every metric, and registers carried
  forward so nothing falls off silently.
- **`skills/ops/content-loop.md`**, the closed weekly loop across Notion and the repo. Performance,
  review, hypothesis, implementation, back to performance. 26 documented content vehicles, 13 of
  them ours and the rest a reference library.
- **`skills/miro/`**, the board system, including a gotchas file that exists entirely because of
  things that broke: the 200-item ceiling past which nothing can be edited or deleted through the
  API, and the single bad attribute that failed 20 of 37 items with no useful error.
- **`skills/lead-gen/lead-magnet/`**, five magnet subtypes under one shared shell.

### 3. The four agents, and the incident behind each

An agent runs without being asked. All four exist because something was missed.

| Agent | Exists because |
|---|---|
| **performance-loop** | Monthly impressions fell **64% between June and August 2026 and nobody noticed for two months.** |
| **signal-sweep** | On 2026-08-14 a catch-up missed a two-message group DM holding the one number tying YouTube cadence to the $1M/month target, and presented an auto-generated queue as if it were the client's priorities. |
| **board-qa** | Boards were going out that were full rather than recordable. It answers one question through 15 gates: can this be read to camera without stopping. |
| **youtube-lead-magnet** | Packaging drift. Its first instruction is to run the existing skill and never invent rules. |

That table is the most quotable thing in the whole video. Every agent is a scar.

### 4. The 25 tools, and the rule that produced them

`ops/tools/` holds 25 Python scripts. Among them: `impressions-vs-calls.py`, `consolidate-exports.py`,
`post-to-call.py`, `trace-bookings.py`, `call-structure.py`, `article-title-features.py`,
`lane-tables.py`, `backlog-sync.py`, `build-dashboard.py`.

They exist because of one convention: **the analysis that produced a number gets saved as a
script.** An inline calculation is lost at the next context clear, and then somebody re-derives it
slightly differently and the two numbers disagree in a meeting.

And every script states its own limit in its opening docstring. One tool was named as if it measured
a single account's bookings; it measures all inbound, because 649 of 678 Calendly rows sit under one
owner and the UTM field is empty on 673. The docstring now says so in capitals.

### 5. The day, and the week

**Daily**, v3 of the ops system, built 2026-08-31 after Mauro's own verdict on v2: calendar blocks
do not get done automatically, so the loop never closed. A block had no done state, so the end of
day inferred completion from Notion, Slack and call transcripts, and got it wrong for two months.
Now the plan comes out of `BACKLOG.md` and the tick comes from Google Tasks. Four moving parts: a
weekly spine capped at three items a day, an export at 07:30 and 16:40, a tasks bridge that creates
at 08:00 and writes completions back at 17:00.

**Weekly**, the Monday run: the acquisition analysis, then the content loop, then the lane on the
Miro control panel carrying last week's performance, this week's hypothesis and the implementation.

The engine's whole shape is that loop. Everything else is a file that the loop reads or writes.

### 6. What keeps it honest

Nine conventions. The load-bearing four: every claim carries an evidence tag, every number traces to
a script and a dataset, every script declares its own limit, and decisions are dated lines in the
file whose behaviour they govern.

The reason for the tags, in one example: a skill asserted that the worked example was the section
that converts. Measuring it returned 60,000 against 264,000, in the opposite direction. It had felt
obviously true.

### 7. What this system does not do

It does not book calls on its own. Every installed agent is defensive: it catches a drop, catches a
missed ask, gates a board, packages an asset. Nothing in the repo today reaches out to a human. That
gap is the subject of the next video.

---

## Evidence

| Claim | Status |
|---|---|
| 73 skill files, 8 activity folders | `[measured: 2026-09-07]` |
| 4 agents, 25 tools | `[measured: directory listings, 2026-09-07]` |
| Impressions fell 64% June to August, unnoticed for two months | `[measured: named in the performance-loop agent]` |
| 45 minutes lost to a rebuilt SOP | `[observed: MAP.md]` |
| 649 of 678 rows one owner, UTM empty on 673 | `[measured: CONVENTIONS.md rule 3]` |
| Worked-example claim measured backwards | `[observed: CONVENTIONS.md rule 1]` |
| $150k MRR closed from X and LinkedIn | `[observed: Mauro, 2026-09-07, hedged in the source]` |
| ~$500k closed in total | `[observed: Mauro, 2026-09-07, "I think", "probably"]` |
| $300k/mo agency revenue | `[observed: the one pre-cleared public figure]` |

---

## Beats on camera

1. The number, and exactly what it means, in the first thirty seconds. Channel, contract type, period.
2. Open the repo. Eleven areas, one map.
3. Route it or it does not exist, with the 45-minute story.
4. The skills folder. Eight names, 73 files, why activity beats client.
5. Open the article set. Seven files, fixed order, one evidence file.
6. Open the Monday analysis. Four inputs, ten sections, a diff on every metric.
7. The four agents, and the incident behind each one.
8. The tools folder. Save the script, state its limit.
9. The day: plan from the backlog, tick from tasks, 08:00 and 17:00.
10. The four conventions, and the claim that measured backwards.
11. What it still cannot do, which sets up the next video.
12. CTA.

---

## Do not say

- Any of the three revenue figures without its definition attached in the same sentence.
- "$500k" as a monthly number. The source describes it as a total.
- That the system produces the revenue. It runs the accounts and the content that produce the calls.
- Any client or account name, on screen or in narration. Blur the repo tree if a folder is named.
- Any impression or booking figure not already in the sources above.
- That it is finished. Two of the four agents were installed after something was missed.

## Gaps

- ~~screen-safe repo tree~~ **Closed 2026-09-07.**
  [`assets/repo-tree-screen-safe.txt`](assets/repo-tree-screen-safe.txt), account names redacted.
- ~~current counts~~ **Verified 2026-09-07: 73 skills, 4 agents, 25 tools.** Re-check on the day.
- `[NEEDS: the revenue figure resolved, see the top of this file]`
