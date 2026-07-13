# Skill: Daily Ops (Focus + Accountability System)

**Version:** 1.0
**Created:** 2026-07-06
**Trigger phrases:** "start my day", "plan my day", "start of day", "SOD", "end my day", "end of day", "EOD", "wrap the day", "midday check", "weekly review", "what should I be doing"
**Supersedes:** `skills/ops/save-recap.md` (its end-of-day recap + calendar job is now the EOD ritual here). Keep save-recap only for one-off "log this session" requests.

---

## Why this skill exists (read this — it's the point)

Mauro's problem is **not** planning. He knows what to do. The failure is **execution**: he batches everything onto Monday and it never happens, he does easy/shallow work instead of the needle-mover, action items slip to "next Monday," he doesn't fill his calendar, and he starts the day reactive (wake → YouTube → drift). He has used self-triggered logging systems before (`recaps/`) and abandoned them in 2 days.

So this system is built on three rules:

1. **The plan is not on his willpower.** Claude drafts it, fills the calendar, and *nudges him* — he mostly confirms and edits. Automated pings (AM / midday / EOD) are the core mechanism, not a nice-to-have.
2. **Needle-mover first, before the noise.** Every day names ONE big rock and it gets the first real block, before 11:00 and before reactive work.
3. **Nothing waits for Monday.** Action items get a real due-day spread across the week the moment they exist. "Monday" is never the default dumping ground.

If output ever drifts back toward "a nice journal Mauro will ignore," you've failed the brief. Optimize for *him actually doing the thing*, and for an honest scoreboard he has to look at.

---

## The pieces

```
ops/daily/
  backlog.md              — single source of truth for tasks (due-day + needle-mover flag)
  automation-backlog.md   — content Mauro does manually → candidates to automate (improvement cycle)
  YYYY-MM-DD.md           — one file per day: morning plan + EOD review + content shipped
  weekly/YYYY-Www.md       — weekly review (hit-rate trend, blockers, automation wins)
```

Plus: **Google Calendar** (primary calendar) gets the timed blocks. **Scheduled agents** fire the three daily nudges.

---

## Component 1 — The Backlog (`ops/daily/backlog.md`)

The one list. Every task row:

| field | meaning |
|---|---|
| task | what it is, concretely (not "do content" — "write Tue LinkedIn post from X article") |
| due | a real weekday date (`2026-07-08`). Never blank, never "Monday" unless it's genuinely a Monday-only task |
| rock? | ⭐ if it's a needle-mover (moves acquisition / revenue / a real project), blank if shallow/admin |
| source | `monday-call` / `ad-hoc` / `rolled-over` / `content` |
| status | `todo` / `doing` / `done` / `dropped` |

Rules:
- **Spread, don't stack.** When several items land at once (esp. Monday call items), distribute them across the week's days. Cap needle-movers at ~1–2 per day.
- **Roll-over is explicit.** Unfinished tasks at EOD get a new due-day (default: next working day) and `source: rolled-over`. If a task rolls over 3+ times, flag it at the top of the backlog — it's either too big (break it down) or being avoided (say so out loud).
- Keep it lean. Done/dropped items older than the current week get moved to the bottom `## Archive` section, not deleted (they feed the weekly hit-rate).

---

## Component 2 — Start of Day ("start my day", or the AM nudge)

Goal: a confirmed, time-blocked day on the calendar in under 5 minutes, big rock first.

Steps:
1. **Gather inputs:**
   - Today's due items from `backlog.md`
   - Anything left `todo`/`doing` from yesterday's daily file (roll it in)
   - New Monday action items if today is Monday (see Component 6)
   - Today's existing Google Calendar events (real meetings — block around them). Use `mcp__claude_ai_Google_Calendar__list_events` for today.
2. **Pick the big rock.** Exactly one needle-mover for the day. If Mauro didn't name one, propose the highest-leverage ⭐ item and say why.
3. **Draft a 30-minute-block day.** Mauro likes half-hour granularity. Structure:
   - Big rock gets the **first deep block of the day, before 11:00**, minimum 90 min, protected (no reactive work, phone/Slack off — YouTube in the background is fine only for shallow blocks, not this one).
   - Batch reactive/admin (Slack, email, small action items) into ONE afternoon block, not sprinkled.
   - Leave realistic gaps — do the time math. If the blocks don't fit the hours available, cut scope and say what got cut. Overcommitting is one of the documented failure modes.
4. **Confirm with Mauro** (he can edit by voice). Show the block plan as a simple table.
5. **Write today's file** `ops/daily/YYYY-MM-DD.md` (structure below).
6. **Fill the calendar.** Create each block as a Google Calendar event on his **primary** calendar via `mcp__claude_ai_Google_Calendar__create_event`. Title format: `[⭐ if rock] HH:MM Task`. Event body: the task detail + which backlog item it maps to.
7. **Report:** the plan table + calendar confirmation + the one line "today's win condition = [big rock done]".

### Daily file structure
```markdown
# Daily — [Weekday] YYYY-MM-DD

**Big rock:** [the one needle-mover] — win condition for the day
**Planned blocks:** N   **Hit:** —/N (filled at EOD)

## Plan (set AM)
| Time | Block | Rock? | Backlog item |
|------|-------|-------|--------------|
| 09:00–10:30 | ... | ⭐ | ... |

## Content shipped today
(filled at EOD — see Component 4)

## EOD review
(filled at EOD)
```

---

## Component 3 — Midday check ("midday check", or the midday nudge)

One job: catch the big rock before the day gets away. Short.
- Ask: "Big rock was [X] — done, in progress, or not started?"
- If not started: help him protect the next available block for it right now, and move something shallow out of the way. Don't lecture — re-plan.
- Note the midday status in the daily file under a `## Midday HH:MM` line.

---

## Component 4 — End of Day ("end my day", or the EOD nudge)

This replaces `save-recap`'s recap. Honest scoreboard, then set tomorrow up.

Steps:
1. **Walk the blocks.** For each planned block: `done` / `partial` / `no`. Pull git log for the day as corroboration (`git log --since` — see below) but the plan blocks are the primary scorecard, not commits.
2. **Compute hit-rate** = done blocks / planned blocks. State it plainly. Big rock done? That's the headline (a day where the big rock got done is a win even if shallow stuff slipped).
3. **Content shipped.** List what content actually went out / got produced today (posts, articles, auto-DMs, YouTube, scripts). Also append it to the existing dashboard log `future-projects/dashboard/data/content-log.csv` (don't build a second log). Feeds Component 5 + `ops/daily/weekly-inputs.md`.
4. **Ask three quick things:** 1–10 day score, one win, one blocker (what actually stopped you — be specific, this is the data that finds patterns).
5. **Roll over.** Every unfinished task → new due-day in `backlog.md`, `source: rolled-over`. Flag 3x-rollovers.
6. **Tee up tomorrow.** Propose tomorrow's big rock candidate so the AM ritual starts warm.
7. **Update the daily file, calendar summary (optional), commit + push.**

### EOD section structure
```markdown
## EOD review — HH:MM
**Hit-rate:** X/N blocks   **Big rock:** ✅/❌   **Day score:** N/10
**Win:** ...
**Blocker:** ...
**Rolled to tomorrow:** [tasks + new due-days]

| Time | Block | Result |
|------|-------|--------|
| ... | ... | done/partial/no |
```

### Git log for corroboration
```bash
cd /Users/mauro/growthub-os
git log --since="YYYY-MM-DD 00:00" --until="YYYY-MM-DD 23:59" \
  --pretty=format:"%ad|%s" --date=format:"%H:%M"
```

---

## Component 5 — Content output + automation / improvement cycle

Mauro wants to track **what content he actually does** and **push it toward automation**, on a constant-improvement loop. Two moving parts:

**a) Content-shipped log** — appended to `future-projects/dashboard/data/content-log.csv` at EOD (Component 4, step 3), and summarized in the daily file. Recurring weekly targets live in `ops/daily/weekly-inputs.md`. Over a week this shows what he's really producing vs. those targets.

**b) Automation backlog** (`ops/daily/automation-backlog.md`) — every recurring content task Mauro does by hand is a candidate to automate. Each row:

| field | meaning |
|---|---|
| task | the recurring content job (e.g. "turn YouTube breakdown → X article") |
| freq | how often he does it (daily / weekly / per-video) |
| current | `manual` / `semi` (a skill exists but needs babysitting) / `automated` |
| lever | the skill/tool that could do it — link to an existing `skills/` file or the Agency Tools hub build |
| next step | the single next action to move it one notch toward automated |

**The improvement cycle (runs in the weekly review):**
1. Look at the week's content-shipped logs → what did Mauro do repeatedly by hand?
2. Anything done 2+ times manually becomes/updates an `automation-backlog.md` row.
3. Pick ONE automation to advance that week; its "next step" becomes a ⭐ backlog task with a due-day.
4. When a task moves `manual → semi → automated`, log it as a win in the weekly review. That's the visible progress.

This ties into the existing content skills and the planned Agency Tools content generators — automating a step usually means wrapping an existing `growthub-os` skill, not building from zero. Prefer reusing skills already in `skills/`.

---

## Component 6 — Monday action-item auto-import

On Mondays (or when a new `acquisition-calls/YYYY-MM-DD.md` appears):
1. Read the latest acquisition-call note.
2. Extract every `**Mauro** →` action item.
3. Add each to `backlog.md` with `source: monday-call` and a **due-day spread across the week** (don't stack them all on Monday — that's the exact failure this fixes). Put needle-movers earlier in the week.
4. Surface the list at the next Start of Day for confirmation.

---

## Component 7 — Weekly review ("weekly review", or a Sunday/Monday-AM nudge)

Write `ops/daily/weekly/YYYY-Www.md`:
- **Hit-rate trend:** each day's X/N + the week's average. Is it climbing?
- **Big-rock completion:** how many days did the needle-mover get done?
- **Monday items:** did this week's action items get done *in-week* (not rolled to next Monday)?
- **Blocker patterns:** recurring blockers from the daily EODs — name the pattern.
- **Automation win:** what moved a notch toward automated (Component 5).
- **Next week's setup:** carry-over big rocks + import next Monday's items.

Keep it to one screen. The trend line is the product.

---

## The nudges (scheduled agents)

Three scheduled runs per day drive the whole thing (set up via the `schedule` skill / routines). Each run executes the matching component autonomously, then **notifies Mauro** so he actually engages:

| When | Fires | Does |
|---|---|---|
| Morning | Start of Day | Drafts the day, proposes the big rock, waits for his confirm/edit before finalizing the calendar |
| Midday | Midday check | One line: is the big rock moving? Re-plans if not |
| Evening | End of Day | Prompts the review; if no response, still logs the git-based recap + rolls over open tasks |

### Live setup (as built 2026-07-06)
GitHub cloud-routine access was blocked for Mauro's account, so the automation runs **through Slack, not this repo**. The live single source of truth for the nudges is a **Slack canvas**, not `ops/daily/backlog.md` (the repo files remain the method spec + anything run locally in a Claude session).
- Channel `#mauro-daily-ops` = `C0BFGEW82VA` · backlog canvas = `F0BF9EJFQ05`
- Routines (weekdays, Europe/Madrid, claude-sonnet-4-6, Slack + Google-Calendar connectors):
  - Morning 09:00 → `trig_01UvirY7vLLDmNW9V6WXbwAS`
  - Midday 13:00 → `trig_014Pd7XeyniHCjQZYEsFaLDG`
  - EOD 16:45 → `trig_01F5mTtZadEMwbJbEsqATcxm`
- Manage: https://claude.ai/code/routines. The EOD nudge degrades gracefully — if Mauro goes dark it still updates the canvas and rolls tasks so nothing is lost. If GitHub routine access is ever enabled, migrate state from the canvas back to `ops/daily/`.

---

## Running this skill (quick reference)

| Mauro says | Do |
|---|---|
| "start my day" / AM nudge | Component 2 |
| "midday check" / midday nudge | Component 3 |
| "end my day" / EOD nudge | Component 4 (+ 5b capture) |
| "weekly review" | Component 7 |
| "what should I be doing" | Read backlog, name the current block's task + the big rock |
| new acquisition-call note | Component 6 |

---

## Edge cases
- **Mauro skips SOD:** the day has no plan → EOD scores against git log only and flags "no plan set today" (don't let unplanned days silently score 0 with no signal).
- **Meeting-heavy day:** if real calendar events leave <90 min free, say so and shrink the big rock to what fits; don't pretend there's deep-work time there isn't.
- **He argues with the plan:** good — edit it. His buy-in matters more than the draft being "right."
- **Rollover ≥3x:** stop rolling silently. Surface it: break the task down, or decide to drop it.
- **YouTube-in-background:** allowed for shallow/admin blocks, explicitly not for the protected big-rock block.

---

## Non-negotiable
Per repo CLAUDE.md: this skill file and all `ops/daily/` state changes are committed and pushed to GitHub. Daily/backlog files commit as `daily: YYYY-MM-DD` / `backlog: update`. Never leave state only in conversation.
