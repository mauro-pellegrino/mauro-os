# I record off a board now: presenter notes

Hidden on the board. Press `N` on the board to see the same lines in an overlay.

## F01 · 0:00-0:12 · A board: 4 hours, now about 2

A recording board used to take me four hours to build by hand. It is close to two hours now, and I build four of them every week.

Everything you see in this video is one of those boards. I am talking off it right now.

## F02 · 0:12-0:20 · Talk off a board

A script makes you read, and a board makes you talk. By the end of this video you can turn any script into a board you record from, without a teleprompter and without memorising anything.

## F03 · 0:20-0:30 · Today

Today we go over three things. First, what a board actually is and what makes it record-ready. Second, how I build one straight from the script. Third, what breaks when a board gets big, and what that forced me to change.

## F04 · 0:30-0:55 · What a board is

Section one. What a board is, and the one standard every board has to meet before I hit record.

## F05 · 0:55-1:55 · Before: reading the script

Here is the before. I read one line from a script, straight, the way I used to record. [Read one scripted line to camera here.]

You can hear it. The eyes move, the rhythm goes flat, and it sounds read. Now the same line, off the board on the next frame.

## F06 · 1:55-2:50 · After: one column, one beat each

And the after. A board is a single vertical column that maps the video's flow, top to bottom. Every concept gets its own container, and there are no raw walls of text.

[Say the same line again, off the board.]

Each box holds one beat, one point from the script. You look at the box, you remember the point, and you say it in your own words.

## F07 · 2:50-3:40 · Record-ready means nothing missing

The standard is record-ready. Nothing is missing, and nothing needs editing at the moment I record.

If I have to stop and fix a box while the camera is on, the board was not finished. That one rule decides whether a board counts as done.

## F08 · 3:40-4:50 · Every section has a type

Every beat gets a section type. Title card, section title, question hooks, a narration block, a two-path comparison, a tree, a pillar layout, a multi-column section, a sticky-note grid, label to description rows, an emphasis label and a brand badge.

The palette is fixed too. Yellow for labels and pillars, light yellow for narration, lilac for section titles, green for a win, red for the negative path, and a dark three-pixel border on every filled box. That border is what gives the stacked-card look.

## F09 · 4:50-5:45 · Split at every new topic

How do you cut a script into beats? I split at every new topic, at every named process, and at every clear shift in what the script is doing: explaining, demonstrating, listing, concluding.

I never split mid-thought. One thought stays in one box.

## F10 · 5:45-6:30 · When in doubt: plain text

The escape hatch. When I am not sure which container fits, I use plain centred text. Forcing content into a container that does not fit is worse than no container at all.

## F11 · 6:30-7:30 · Worked example: this board

The worked example is the board you are looking at. The script for this video went in, and it came out as a hook, three sections and a call to action.

Each section holds one worked example and one before and after. That is the whole shape, and it is the same shape every time.

## F12 · 7:30-7:50 · Build it from the script

Section two. How the board gets built straight from the script. The board is built from the script, so you still write one. You just stop reading it.

## F13 · 7:50-8:50 · Four steps. Only one touches the board.

The build is four steps: beats, then components, then geometry, then the write. Only the last step, the write, touches the board.

Everything before that happens in a file, where a mistake costs nothing.

## F14 · 8:50-9:40 · Beats: split, never merge

Step one, the beats. The script gets split into distinct points, with no summarising and no merging. Then I check the beat count against the runtime I am aiming for, before anything else gets built.

## F15 · 9:40-10:35 · Every coordinate, computed first

Step three, the geometry. Every coordinate, every height and every gap is computed up front. There is a centre axis, a running vertical stack and a width for each section type.

Nothing gets nudged by hand afterwards.

## F16 · 10:35-11:40 · A sticky grows. The rows drift.

The worked example for this part comes from the geometry step. A sticky note takes a width or a height, never both, and it grows to fit its text.

What happened: I computed a fixed row pitch in advance, a sticky grew, and every row under it drifted into the next one. The fix: shapes take an explicit width and height, so the stack I computed is the stack that lands.

## F17 · 11:40-12:35 · Eight files, same order

The build reads eight files, in the same order every time: master, visual, archetype, writing, gotchas, assets, diagram, QA.

The order is the dependency. You cannot pick a visual before you know the archetype, and you cannot run QA on something that is not built.

## F18 · 12:35-13:30 · Diagrams: markup, render, paste

Diagrams are never placed by hand on the canvas, and never prompted out of an image model. They are written in markup, rendered by headless Chrome, and pasted in as an image. That has been the default since 25 August.

## F19 · 13:30-14:30 · Before: lasso. After: one write.

So the before and after for the whole build. Before, something placed wrong stayed wrong, or I lassoed it by hand in the Miro UI and dragged it around.

After, the beats, the components and the geometry all live in a file, and the board gets one write. That is how four hours by hand came down to close to two.

## F20 · 14:30-14:50 · What breaks at scale

Section three, and the worked example is a real failure. What breaks when a board gets big, from the repo that has been building boards through the Miro API the longest.

## F21 · 14:50-15:45 · A real board: 200 to 400 items

A real recording board runs 200 to 400 items. Every box, every arrow and every label is an item.

Keep that range in your head, because of the line on the next frame.

## F22 · 15:45-16:40 · Past 200 items: create only

Past 200 items, the edit call parses the whole board and gives up. Creating still works. Editing and deleting do not. That was confirmed on 4 August.

So on any board of real size you get one shot. Every coordinate has to be right before you send it.

## F23 · 16:40-17:40 · 37 sent. 17 created.

On 3 August a 37-item create came back with 17 created and one error covering the other 20. The error named no item and no attribute.

Two attribute values caused it, and neither was documented as invalid.

## F24 · 17:40-18:25 · URLs for items that never existed

And the response made it worse. The response body showed plausible URLs for items that had not been created. It looked like success until you went to the board.

## F25 · 18:25-19:15 · No undo means correct up front

The before and after for this part. Before the limit, a wrong box got fixed by hand. After it, the work moved into a file, a check and one write.

This is my own read of it. Any system with no undo forces you to be correct up front, and being correct up front turns out to be faster than fixing.

The limit made placing boxes by hand impossible, and that forced a different shape of work.

## F26 · 19:15-20:15 · The gate: 15 checks

Before a board counts, it goes through a gate of fifteen checks. The first four are blockers, and if one of those fails, the run stops right there.

Roughly half the checks run as a script. The rest need eyes.

## F27 · 20:15-21:15 · Charlie Morgan records off boards

Charlie Morgan uses the same format. His framework videos are this exact format: a hand-drawn whiteboard or a live Miro board, narrated with a facecam in the corner. A winding road from a now state to a future state, a funnel, a named theory.

Some of his most-viewed videos are this format, board plus facecam.

## F28 · 21:15-21:55 · Link in the description

If you run an established agency and you want this kind of content system installed for you, the offer is called Agency Booked Calls. The link is in the description.

**Runtime: 21:55 across 28 frames.**
