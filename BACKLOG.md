# BACKLOG — the standing list for mauro-os

**This file survives session clears. Read it at the start of every session.**

Started 2026-09-06. This is the ghostedcalls / @maurojpelle backlog. The growthub one lives in
`~/growthub-os/BACKLOG.md` and the two do not mix: agency work there, personal brand here.

**How to use it.** Items are `[ ]` open, `[~]` in progress, `[x]` done, `[?]` blocked on Mauro.
A blocked item names what unblocks it. If you close something, tick it and say what happened.
If you find something open that is not here, add it. Nothing auto-closes; ticking is a judgement
call. The statusline reads this file (blocked count, Tier 1 open, total left).

## AT A GLANCE

| Blocked on Mauro | Open | In progress | Done | Tier 1 still open |
|---|---|---|---|---|
| 3 | 8 | 1 | 0 | 8 |

*Counts written by hand 2026-09-06, matched to what the statusline prints. Tier 1 open counts
`[ ]` and `[~]` only, blocked items are counted in their own column. Update them when the list moves.*

**The single objective:** a YouTube engine that runs without Mauro being the bottleneck, feeding
X, where the conversion happens.

---

## TIER 1 — the YouTube video flow (the "own vidIQ")

The end-to-end path is: research picks the topic, titles get drafted, Mauro answers in a voice
note, the transcript becomes the script, the script becomes a record-ready board, Mauro records
raw off the board. Half of this exists as skills. The two ends, research and board creation, are
the parts still done by hand.

**The board end (started today)**

- [~] Connect the Miro account over MCP. OAuth URL issued 2026-09-06, waiting on Mauro to
  authorize in the browser. Unblocks everything below it.
- [ ] Build one board end-to-end through the MCP from an existing script, and compare it against
  what the Chrome extension produces. This is the test of whether the API path is good enough.
- [?] **Blocked on Mauro:** which Miro team and board the automation is allowed to write into.
  A wrong answer here writes into client boards.
- [ ] Decide the board path: Chrome extension (`skills/youtube/miro-design-system.md`) or MCP.
  Two skills currently describe the same job two ways. One of them should win and the other
  gets marked deprecated.
- [ ] `brand/scripts/` does not exist. Both Miro skills tell the agent to look there first, so
  step 0 of the board flow fails on a missing folder. Create it and put the existing scripts in.

**The research end (the actual vidIQ part)**

- [ ] Define what the research tool scores. vidIQ scores keywords and outliers; decide what the
  equivalent is here, given the channel goal is subscriber growth on broad B2B, not the tight ICP.
- [ ] `skills/youtube/01-outliers.csv` is a static snapshot. Decide whether it gets refreshed on a
  schedule and by what (YouTube API key is already in the local permissions).
- [ ] Wire the title step to the outlier data. `youtube-title-generator.md` and the Charlie Morgan
  pattern work in `research/charlie-morgan/` are not connected to each other.
- [?] **Blocked on Mauro:** the ~10 titles to shoot, drafted off the Charlie Morgan patterns, were
  never signed off. Nothing downstream moves until a topic is picked.

**The recording end**

- [ ] Thumbnail render mode (`thumb`, 1280x720) is proposed and not built. Working recommendation
  is AI or photo for the image plus an HTML render for the bold text.
- [?] **Blocked on Mauro:** no video has been recorded off a board yet. The flow is unproven until
  one is.

---

## TIER 2 — everything else in mauro-os

- [ ] Statusline and worklog hook still point at growthub by config. Statusline was scoped to the
  session's project on 2026-09-06 (`growthub-os@40f0b3f`); the Stop hook still writes every turn
  into `~/growthub-os/ops/daily/`. Decide whether mauro-os gets its own worklog.

---

## RESOLVED, do not re-litigate

- **2026-09-06.** The statusline showed growthub's counts in every repo because the path was
  hardcoded while the setting is global. Fixed by walking up from the session cwd to the first
  BACKLOG.md. This file is what the statusline now counts here.
