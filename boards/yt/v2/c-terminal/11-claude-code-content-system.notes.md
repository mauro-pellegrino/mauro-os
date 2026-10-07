# My whole Claude Code content system: presenter notes (format C, terminal)

Source: `research/video-knowledge/11-claude-code-content-system.md`. Numbers: `brand/claims.md` only. Board: `11-*.html` in this folder.
Frames: 26. Planned length: about 23 minutes. Press N on the board to see these notes on screen.

## Today we go over

01  The skeleton: one repo, one map, skills by activity
02  The agents: four of them, and the incident behind each
03  The honesty layer: scripts, limits, evidence tags

Each section: one worked example, one before and after.

## Redactions on screen
- Repo root shown as `agency-os/`. Account folders, client and person names show as `[redacted]`.
- The signal-sweep target number is redacted (not in claims.md).
- Agents and tools show the published counts (4 and 25). The live repo now holds more; re-count on the day.

## 01 · 0:00-0:10 · hook
**Caption:** My whole Claude Code content system

ON SCREEN: the terminal types the tree of the repo. The explorer on the left is the same repo.

SAY: This is the whole repo. Every skill, every agent and every script that runs the content and the inbound for the agency I run. 73 skill files, 4 agents, 25 scripts. I'm going to open it folder by folder.

## 02 · 0:10-0:20 · hook
**Caption:** 150+ booked calls for the agency, 2026

ON SCREEN: grep pulls the one line from the claims file.

SAY: The result first. This system generated over 150 qualified booked calls for the agency this year. That's the Calendly total. I don't split it by channel, and later in the video I show you why the data can't carry that split.

## 03 · 0:20-0:30 · hook
**Caption:** Repo. Agents. Proof. In that order.

ON SCREEN: the editor opens this video's own notes file at the agenda.

SAY: Today we go over three things. The skeleton, so one repo and one map. The four agents, and the thing that broke to create each one. And the honesty layer, which is the part that makes every number in here traceable.

## 04 · 0:30-1:40 · 01 skeleton
**Caption:** One repo. Eleven areas. One map.

ON SCREEN: the full tree, area by area. Highlight moves down the explorer as you name each folder.

SAY: One repo. Eleven top-level areas. Skills, agents, ops, research, the accounts, the Monday acquisition calls, outbound, and the backlog. Each area has an owner and an entry point, and all of them are indexed in one file, ops/MAP.md. The account folders are blurred on purpose, those are client names.

## 05 · 1:40-2:50 · 01 skeleton
**Caption:** Route it, or it gets rebuilt
**On-screen NEEDS:** the 45 minutes lost, not in claims.md

ON SCREEN: ops/MAP.md, the first lines. The highlight lands on the corollary.

SAY: This is the first file any agent reads. It exists because an agent wrote a full outbound reply SOP from scratch, pushed it, and then found a better one already sitting in outbound-calls. The routing table didn't list that folder, so there was no way to know. So the rule became: work is finished when it's routed. Read the time lost only if Mauro signs it off.

## 06 · 2:50-3:50 · 01 skeleton
**Caption:** Before: rebuilt. After: found in the map.

ON SCREEN: the before and after as two flows.

SAY: Before. A new request comes in, the agent can't see the folder, it builds a second copy, and you only find out after it's pushed. After. Every request checks the map first. If the thing exists, use it. If it doesn't, build it and add the row in the same session.

## 07 · 3:50-4:50 · 01 skeleton
**Caption:** Every skill folder is an activity

ON SCREEN: eight skill folders, then the count.

SAY: 73 skill files across eight folders. Content, research, ops, miro, lead-gen, youtube, creative strategy, dm setting. Every folder is an activity. There is no folder per client anywhere in skills.

## 08 · 4:50-5:50 · 01 skeleton
**Caption:** A client folder dies with the client

ON SCREEN: two layouts side by side.

SAY: Before, you put the skills inside the client. The client leaves, the folder rots, and the next client gets the same skill rebuilt from zero. After, the skill lives under the activity. It survives every client, and every client makes it better.

## 09 · 5:50-6:50 · 01 skeleton
**Caption:** Worked example: transcript to article, in order

ON SCREEN: the article skill set.

SAY: Here's one skill set opened up. This folder turns any transcript into a published X article. Six files in a fixed order, a seventh whose only job is to keep the other six honest, a README, and one corpus file.

## 10 · 6:50-7:50 · 01 skeleton
**Caption:** Six steps in order. One keeps them honest.

ON SCREEN: the seven files as a pipeline.

SAY: Subject before title. Title and cover get drafted together, as one first screen. Body last, every claim sourced to the input. Then distribution. And 07-improve runs when new evidence lands, and reconciles the other six.

## 11 · 7:50-8:40 · 01 skeleton
**Caption:** Every number cites one corpus file

ON SCREEN: one number out of the corpus, with its source line.

SAY: The corpus is 41 real article captures from 24 accounts. One example of what's in it. Articles in the 1,800 to 3,000 word band had a median of 225,900 impressions. The 900 to 1,800 band, 73,300. That's reach across those captures, and it's why the body skill defaults long.

## 12 · 8:40-9:30 · 02 agents
**Caption:** Four agents. Each one is a scar.

ON SCREEN: the agents folder.

SAY: A skill waits to be asked. An agent runs without being asked. There are four, and every one of them exists because something got missed.

## 13 · 9:30-10:40 · 02 agents
**Caption:** 64% drop. Nobody noticed for two months.

ON SCREEN: the first lines of performance-loop.md. The account name is redacted.

SAY: Worked example, agent one. Monthly impressions on one of the accounts fell 64% between June and August, and nobody noticed for two months. That sentence is literally the first thing the agent reads every time it runs.

## 14 · 10:40-11:40 · 02 agents
**Caption:** Before: the drop sat unseen

ON SCREEN: June indexed to 100, August at 36.

SAY: I only publish the percentage, so this is indexed to June. June is 100. August is 36. Two months of that, and the weekly numbers looked normal enough that nobody stopped.

## 15 · 11:40-12:40 · 02 agents
**Caption:** After: it flags the drop unprompted

ON SCREEN: the flag list in the agent file.

SAY: After. Every run, it compares the latest week and month against the trailing four. And it flags these without being asked. The one in yellow is the one that was missed.

## 16 · 12:40-13:40 · 02 agents
**Caption:** A missed ask, in a two-message DM

ON SCREEN: why signal-sweep exists. The target number and the names are redacted.

SAY: Agent two. A week's catch-up missed a two-message group DM that held one key number, and it presented an auto-generated queue as if it were the priority list. Both failures were structural. Now the agent reads every channel and outputs a ranked list of asks.

## 17 · 13:40-14:40 · 02 agents
**Caption:** 15 checks. Can this be read aloud?

ON SCREEN: board-qa on the left, the fifteen gates on the right.

SAY: Agent three. Boards were going out full rather than recordable. This one answers one question through fifteen checks: can this be read to camera without stopping. The first four are blockers, the run stops there. About half run as a script, the rest need eyes.

## 18 · 14:40-15:30 · 02 agents
**Caption:** Run the skill. Never invent rules.

ON SCREEN: the youtube-lead-magnet agent.

SAY: Agent four. Packaging drift: every lead magnet came out a little different. Its first instruction is to run the existing skill and never invent rules, and to read the skill files fresh every run.

## 19 · 15:30-16:30 · 03 proof
**Caption:** 25 scripts. One per number anyone cites.

ON SCREEN: part of the tools folder.

SAY: Section three, the part that keeps it honest. 25 Python scripts. The rule behind them: the analysis that produced a number gets saved as a script. An inline calculation is gone at the next context clear, and then someone re-derives it slightly differently and the two numbers disagree in a meeting.

## 20 · 16:30-17:40 · 03 proof
**Caption:** Every script states its own limit

ON SCREEN: CONVENTIONS.md, rule 3. A script name is redacted.

SAY: Rule three. Every script states its own limit, at the top, in the docstring. One tool was named as if it measured one account's bookings. It measures all inbound. The docstring now says so in capitals.

## 21 · 17:40-18:40 · 03 proof
**Caption:** 649 of 678 rows. One owner.

ON SCREEN: the two splits that break channel attribution.

SAY: Here's why. 649 of 678 Calendly rows sit under one owner. The UTM field is empty on 673 of them. So you can't attribute a booking to a channel from this export. That's why I gave you the 150 as a total at the start.

## 22 · 18:40-19:50 · 03 proof
**Caption:** Worked example: the claim that felt true

ON SCREEN: rule one, the three evidence tags.

SAY: Rule one. Every claim carries one of three tags: measured, observed, assumed. A claim with no tag gets deleted. Here's the case that made the rule.

## 23 · 19:50-20:50 · 03 proof
**Caption:** Before: assumed. After: measured, and reversed.

ON SCREEN: the claimed section against the winning section.

SAY: Before, the skill said the worked example was the converting section. It felt obviously true. After measuring: 60,000 against the winning section's 264,000. The opposite direction. Tagging forces that check before a claim ships.

## 24 · 20:50-21:40 · 03 proof
**Caption:** 185 tasks pushed. Zero ticked.
**On-screen NEEDS:** Mauro clears the 185 / 0 file for public use

ON SCREEN: the daily task log. Only show this if Mauro clears it, it's an internal ops file.

SAY: And the honesty layer applies to me too. From 31 August, Claude pushed five backlog tasks a day into Google Tasks. 37 days, 185 tasks, zero ticked. The plan was fine. The tick never happened, so the loop never closed.

## 25 · 21:40-22:30 · 03 proof
**Caption:** None of them books a call. Yet.

ON SCREEN: what each agent does, and the empty slot.

SAY: Look at the four agents again. One catches a drop, one catches a missed ask, one gates a board, one packages an asset. All defensive. Nothing in this repo reaches out to a human. That's the next video.

## 26 · 22:30-23:15 · cta
**Caption:** Link in the description: Agency Booked Calls

ON SCREEN: the CTA.

SAY: Recap in two lines. Copy the corrections, the provenance and the agents first. The prompts come last. If you run an established agency and you want this built for your own inbound, the link is in the description. It's called Agency Booked Calls.
