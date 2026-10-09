# My whole Claude Code content system: presenter notes

Hidden on the board. Press `N` on the board to see the same lines in an overlay.

## F01 · 0:00-0:12 · My whole Claude Code content system

This is the content system behind more than 150 qualified booked calls for the agency I run this year. That number is the total from the Calendly export, every channel together, and later in this video I show you why I cannot split it cleanly by channel.

Today you see the whole thing, the actual repo.

## F02 · 0:12-0:20 · One repo. All of it.

You have heard people say they built a system in Claude Code, and you have never seen the repo. I am going to open mine, folder by folder, and show you the parts that took the longest to get right. By the end you will know how to lay out your own so it does not rot.

## F03 · 0:20-0:30 · Today

Three parts today. First the skeleton: the folders, the map, and the two worked examples I open every week. Second the four agents, and the incident behind each one. Third what keeps the numbers honest, including the claim that measured backwards.

## F04 · 0:30-0:50 · The skeleton

Part one, the skeleton. One repo, and an index that every agent reads first.

## F05 · 0:50-2:00 · Eleven areas, one map

Here is the repo. One repo, eleven top-level areas, all indexed in one file called MAP.md.

Skills, the agents, ops with the conventions and the tools, research, the accounts, the weekly acquisition analysis, the outbound motion and the backlog. The account folder names are redacted on purpose.

## F06 · 2:00-2:55 · Route it or it gets rebuilt

The rule that holds it together: work is not finished until it is routed into the map. If a thing exists and is not in the map, the next agent rebuilds it.

That rule was written the day an agent rebuilt an outbound SOP from scratch, because the one we had was not in the map. [The doc says this cost 45 minutes. There is no claims row for that, so do not say the number until it is signed off.]

On screen: `[NEEDS: 45 min lost, no claims row]`

## F07 · 2:55-3:50 · 73 skills, 8 folders

The skills folder. 73 markdown files across eight folders: content, research, ops, miro, lead-gen, youtube, creative-strategy and dm-setting.

Each folder is an activity, a kind of work that happens every week.

## F08 · 3:50-4:55 · Split by activity

Before and after. Before, you split by client: a folder per client, and the same skill sits inside each one. When the client leaves, the folder rots, and the skill gets rebuilt inside the next client's folder.

After, you split by activity. Content, research, ops. An activity survives every client.

## F09 · 4:55-5:55 · Worked example: the article set

First worked example, the article skills. Six files run in a fixed order and turn any transcript into a published article. A seventh file has one job: keeping the other six honest as new evidence lands.

Every number they cite lives in one corpus file, built from 41 real captures.

## F10 · 5:55-6:50 · Worked example: the Monday analysis

Second worked example, the Monday acquisition analysis. A fixed set of inputs, a fixed structure, a diff against last week on every metric, and registers that carry forward so nothing falls off silently.

## F11 · 6:50-7:45 · Save the script behind the number

The tools folder holds 25 Python scripts. They exist because of one convention: the analysis that produced a number gets saved as a script.

An inline calculation is gone at the next context clear. Then somebody re-derives it slightly differently, and the two numbers disagree in a meeting.

## F12 · 7:45-8:05 · Four agents, four scars

Part two, the agents. There are four, and every one of them exists because something got missed.

## F13 · 8:05-8:55 · An agent runs without being asked

First the difference. A skill runs when I call it. An agent runs without being asked.

So an agent only makes sense for a job where I already know what good looks like.

## F14 · 8:55-10:00 · Impressions fell 64%. Nobody noticed.

This is the worked example for this part. Scar one. Monthly impressions fell 64% between June and August 2026, and nobody noticed for two months.

That is why the performance-loop agent exists. The bars are indexed to June, so June is 100 and August is 36.

## F15 · 10:00-10:55 · The ask buried in a group DM

Scar two. A catch-up missed a two-message group DM that held a key number, and it presented an auto-generated queue as if it were the client's priorities.

The signal-sweep agent reads every channel and pulls out the asks, so a buried message does not get lost again.

## F16 · 10:55-11:45 · One question: can you read it?

Scar three. Boards were going out that could not be recorded straight through. The board-qa agent answers one question through fifteen checks: can this be read to camera without stopping.

## F17 · 11:45-12:30 · First rule: run the existing skill

Scar four is packaging drift. Each lead magnet package came out a little different. The youtube-lead-magnet agent's first instruction is to run the existing skill and never invent rules.

## F18 · 12:30-13:25 · All four are defensive

Put the four side by side. performance-loop catches a reach drop. signal-sweep catches a missed ask. board-qa catches a board you cannot record. youtube-lead-magnet catches packaging drift.

Every one of them catches something. None of them reaches out to a human.

## F19 · 13:25-14:20 · Every agent is a scar

The before and after for this whole part. Before, something gets missed, and you find out weeks later. After, the miss becomes a dated rule in the file it governs, and then the rule becomes an agent that checks for it without being asked. And it is not finished.

## F20 · 14:20-14:40 · Keeping it honest

Part three, what keeps the numbers honest. This is the part that makes the rest worth trusting.

## F21 · 14:40-15:35 · Nine conventions. Four carry it.

There are nine conventions, and four of them carry the weight. Every claim carries an evidence tag. Every number traces to a script and a dataset. Every script declares its own limit. And decisions are dated lines in the file whose behaviour they govern.

## F22 · 15:35-16:25 · Every claim carries a tag

The tags are three words: measured, observed, assumed. An untagged claim is an assertion.

The 64% drop is measured. The claim that talking beats reading on camera is assumed. You say each one with its tag attached.

## F23 · 16:25-17:30 · It felt true. It measured backwards.

Here is why the tags exist. A skill said the worked example was the section that converts. It felt obviously true.

Then we measured it. The worked example did 60,000. The winning section did 264,000. The opposite direction.

## F24 · 17:30-18:35 · Every script states its limit

And the scripts state their own limits. One tool was named as if it measured a single account's bookings. It measures all inbound, because 649 of 678 Calendly rows sit under one owner, and the UTM field is empty on 673 of them.

The docstring now says so in capitals. This is also why the 150 calls at the start is a total, with no channel split.

## F25 · 18:35-19:40 · The daily loop, honestly

The day, as a before and after. Version two put blocks on the calendar, and a block had no done state, so the end of day guessed what got done and guessed wrong.

Version three plans from the backlog and pushes tasks into Google Tasks, so a tick is the done state. [On screen: the claims file says 185 tasks pushed from 31 August and 0 ticked. Mauro decides whether that is said on camera.]

On screen: `[NEEDS: 185 pushed, 0 ticked: Mauro's call]`

## F26 · 19:40-20:35 · Nothing here reaches out

What this system does not do. It does not book calls on its own. Every agent in it is defensive. Nothing in the repo today reaches out to a human.

That gap is the subject of the next video.

## F27 · 20:35-21:15 · Link in the description

If you run an established agency and want a system like this installed, the offer is called Agency Booked Calls. The link is in the description.

**Runtime: 21:15 across 27 frames.**
