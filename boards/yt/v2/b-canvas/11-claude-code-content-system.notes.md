# 11 · My whole Claude Code content system · canvas flythrough

Board: `11-claude-code-content-system.html` · 29 frames · about 24 minutes.
Keys: right arrow or space moves the camera to the next zone, left goes back, N shows these lines, F is fullscreen.

**Copy convention.** At most 8 words of copy per frame, counted by the build script. The overview frames count only the map title. Region labels and the short labels inside diagrams, charts, code and trees are map labels, which BRIEF.md rule 1 exempts. A red `[NEEDS: x]` tag is a gap for Mauro, never copy.

**Open gaps on this board:** 45 minutes lost to the rebuilt SOP (doc 11 and MAP.md say it, claims.md does not); the revenue figure in doc 11 ($100k/mo, $150k MRR, ~$500k total) is unresolved and kept off the board

## Frame 1 · 0:00 to 0:10 · overview

**On screen:** The whole map, zoomed out: three regions (the repo, the agents, the loop), the arrows between them, the title top right.

This is my whole Claude Code content system, on one map.

Everything you see here is a real file in a real repo. I run it every week for the agency I run.

## Frame 2 · 0:10 to 0:20 · result

**On screen:** One number, 150+, with its label and source.

The result first. This system sits behind more than 150 qualified booked calls this year for the agency I run.

That is the total from the Calendly export. I am not going to tell you which channel each one came from, because the data cannot say that. You will see why later.

By the end of this video you will know how the whole thing is built, file by file.

## Frame 3 · 0:20 to 0:30 · roadmap

**On screen:** Three cards: 01 The repo, 02 The agents, 03 The loop.

Today we go over three things.

First, the repo: how one folder holds the whole operation and why nothing in it gets built twice.

Second, the agents: four of them, and the incident behind each one.

Third, the loop: the rules that keep every number honest, and the day and the week that run it.

## Frame 4 · 0:30 to 0:55 · region 01

**On screen:** Region 01 framed: seven zones, from the repo tree to the article skill.

Section one. The repo.

One folder, and the one rule that stops it collapsing.

## Frame 5 · 0:55 to 1:59 · tree

**On screen:** The screen-safe repo tree. skills/, .claude/agents/ and ops/ highlighted. accounts/ is redacted.

Here is the repo. One folder, eleven top-level areas.

skills holds the how. .claude/agents holds the four agents. ops holds the conventions, the map, the daily system and the tools.

The accounts folder is redacted on purpose. Client names never go on camera.

Walk the tree top to bottom, slowly. This is the frame people pause on.

## Frame 6 · 1:59 to 2:51 · map

**On screen:** A window on ops/MAP.md: eleven rows, area and what it owns.

Every area has an owner and an entry point, and all of it is indexed in one file, ops/MAP.md.

When an agent starts work, this is the first file it reads. If a thing is not in here, the agent cannot know it exists.

Keep that in mind, because it is the cause of the incident in two frames.

## Frame 7 · 2:51 to 3:51 · folders

**On screen:** Eight folder tiles: content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting. Label: 73 files.

The skills folder. 73 markdown files across eight folders.

Each folder is an activity: content, research, ops, miro, lead-gen, youtube, creative-strategy, dm-setting.

73 is a count on one date. It is a snapshot, and the number is bigger today.

## Frame 8 · 3:51 to 4:51 · client-vs-activity

**On screen:** Before: three client folders, each with its own copy of the same skill, one crossed out. After: one activity folder, one skill, three accounts pointing at it.

Before: you split by client. Each client folder gets its own copy of the article skill.

The client leaves, the folder rots, and the same skill gets rebuilt inside the next client folder.

After: you split by activity. One article skill. Every account reads the same file.

An activity survives every client. A client folder does not.

## Frame 9 · 4:51 to 6:05 · incident

**On screen:** A four-step timeline dated 2026-09-01: agent writes an outbound-reply SOP, pushes it, finds outbound-calls/ held a better one, deletes its own. Red tag on the time lost.

Here is the worked example. On the first of September an agent wrote a full outbound-reply SOP from scratch and pushed it.

Then it found that the outbound-calls folder already held a better one. The new one got deleted.

[NEEDS: say the time lost only after Mauro signs off the 45-minute figure.]

The agent was not careless. That folder was not in the routing table, so it had no way to know.

## Frame 10 · 6:05 to 7:05 · route-rule

**On screen:** A routing table window: four rows lead to a skill, the outbound reply row is red, its folder not listed.

So this is the rule the whole repo runs on. Work is not finished until it is routed.

A skill that is not in the map and not in the routing table is invisible. Invisible is worse than missing, because the next agent builds a second one.

Every time I finish a skill, the last step is a row in this table.

## Frame 11 · 7:05 to 8:09 · x-articles

**On screen:** skills/content/x-articles/ opened: seven numbered blocks in a chain, the seventh one dark. One corpus file under it.

Let me open one skill set so you see what is inside. This is the X article set.

Six files in a fixed order turn any transcript into a published article. The seventh one keeps the other six honest as new evidence lands.

Every number they cite lives in one corpus file, built from 41 real captures.

I made a whole video on this one. It is linked at the end.

## Frame 12 · 8:09 to 8:34 · region 02

**On screen:** Region 02 framed: the four agents, the chart, the tools.

Section two. The agents.

An agent runs without me asking. All four of mine exist because something got missed.

## Frame 13 · 8:34 to 9:42 · scars

**On screen:** Four agent cards, each with the incident that created it.

Four agents. Every one of them is a scar.

performance-loop exists because reach fell and nobody saw it. signal-sweep exists because an ask got buried in a chat.

board-qa exists because boards went out that could not be read to camera. youtube-lead-magnet exists because the packaging drifted.

Its first instruction is to run the existing skill and never invent rules.

## Frame 14 · 9:42 to 10:42 · drop

**On screen:** Two bars: monthly impressions in June indexed to 100, August at 36. Label: unnoticed for two months.

The worked example for this section. Monthly impressions fell 64 percent between June and August.

Nobody noticed for two months. Me included.

The bars are indexed to June so you see the size of the drop. I am not showing the raw count here.

## Frame 15 · 10:42 to 11:34 · drop-ba

**On screen:** Before: a June to August strip with the drop found at the end. After: performance-loop.md reads the numbers and flags the drop.

Before: a person was supposed to notice. Two months went by.

After: the performance-loop agent reads the numbers and flags the drop. Its job is to catch a reach drop before it becomes a quarter.

## Frame 16 · 11:34 to 12:30 · sweep

**On screen:** A chat app mock: channel list, one two-message group DM highlighted, an arrow to signal-sweep.md and a ranked list of asks.

signal-sweep. On the fourteenth of August, a catch-up missed a two-message group DM. That DM held the one number that mattered that week.

Worse, the catch-up showed an auto-generated queue as if it were the client's priorities.

Now an agent reads every channel and pulls out what people actually asked for, ranked.

## Frame 17 · 12:30 to 13:26 · gates

**On screen:** Fifteen check boxes in a 5 by 3 grid. The first four are red blockers. The question on top: can this be read to camera without stopping.

board-qa answers one question through fifteen checks. Can this board be read to camera without stopping?

The first four are blockers. If one fails, the run stops there.

You are looking at a board that went through it.

## Frame 18 · 13:26 to 14:26 · tools

**On screen:** A grid of script file chips from ops/tools/, nine named, one chip for the other sixteen.

ops/tools holds 25 scripts. They exist because of one convention: the analysis that produced a number gets saved as a script.

An inline calculation is lost at the next context clear. Then somebody re-derives it a bit differently, and two numbers disagree in a meeting.

## Frame 19 · 14:26 to 15:30 · limits

**On screen:** A docstring window, paraphrased, in capitals: measures all inbound. Two bars: 649 of 678 rows under one owner, UTM empty on 673 of 678.

Every script states its own limit in its opening docstring.

One tool was named as if it measured one account's bookings. It measures all inbound, because 649 of 678 Calendly rows sit under one owner, and the UTM field is empty on 673 of them.

The name claimed something the data cannot support. So now the docstring says so, in capitals.

This is also why I gave you a total at the start and no channel split.

## Frame 20 · 15:30 to 15:55 · region 03

**On screen:** Region 03 framed: the conventions, the claim that measured backwards, the day, the week, the gap.

Section three. The loop.

What keeps it honest, and what runs it every day and every week.

## Frame 21 · 15:55 to 16:47 · nine

**On screen:** Nine rule tiles, four lit: evidence tag, number to script, script states limit, dated decisions.

Nine conventions in one file. Four of them carry the weight.

Every claim carries an evidence tag. Every number traces to a script and a dataset. Every script declares its limit. Decisions are dated lines in the file they govern.

## Frame 22 · 16:47 to 17:51 · backwards

**On screen:** Two bars: the worked example section at 60,000, the winning section at 264,000.

Here is why the tags exist. A skill said the worked example was the section that converts.

We measured it. 60,000 against the winning section's 264,000. The opposite direction.

It felt obviously true. That is exactly the kind of claim that needs a tag.

## Frame 23 · 17:51 to 18:47 · tags-ba

**On screen:** Before: an untagged claim, struck through. After: the three tags, measured, observed, assumed, each with what it needs.

Before: a claim with no tag. It reads like a fact.

After: three tags. Measured names a script and a dataset. Observed was seen but not counted. Assumed is a judgement, stated as one.

An untagged claim gets deleted on sight.

## Frame 24 · 18:47 to 19:35 · dated

**On screen:** skills/ops/daily-ops.md with one dated line highlighted: 2026-08-31, v3, plan from BACKLOG.md, tick from Google Tasks.

Decisions are dated lines in the file whose behaviour they change. Not in chat, not in a separate log.

This is the line that created version three of my daily system. Which is the next frame.

## Frame 25 · 19:35 to 20:39 · day

**On screen:** A flow: BACKLOG.md, the weekly spine, Google Tasks, done, written back. Above it, v2 struck: calendar blocks with no done state.

The day. Version two put work on calendar blocks, and a block has no done state.

So the end of day guessed completion from Notion, Slack and call transcripts, and it guessed wrong for two months.

Version three: the plan comes out of the backlog, the tasks go to Google Tasks, and the tick comes back from there.

## Frame 26 · 20:39 to 21:39 · week

**On screen:** A cycle of four: Monday acquisition analysis, content loop, Miro control panel lane, performance, back to the analysis.

The week. Monday runs the acquisition analysis, then the content loop, then a lane on the Miro control panel.

The lane carries last week's performance, this week's hypothesis and the implementation. Then performance feeds next Monday.

The whole engine is this loop. Every other file is something the loop reads or writes.

## Frame 27 · 21:39 to 22:31 · gap

**On screen:** Four agent tiles labelled defensive, and a fifth red tile: reaches a human, none yet.

What this system does not do. Every agent here is defensive. It catches a drop, catches a missed ask, gates a board, packages an asset.

Nothing in the repo reaches out to a human. That gap is the next video.

## Frame 28 · 22:31 to 23:16 · cta

**On screen:** Dark card: Agency Booked Calls, and Link in the description.

If you run an established agency and you want this installed for your own inbound, that is what Agency Booked Calls is.

The link is in the description. Everyone else, steal the structure and tell me in the comments what you would add.

## Frame 29 · 23:16 to 23:31 · overview, end

**On screen:** The whole map again, zoomed out.

So that is the whole map. The repo, the agents, the loop.

Pause here if you want to screenshot it.
