# Skill: Monday Acquisition Analysis

**Version:** 2.0
**Created:** 2026-06-02, retargeted to this brand 2026-07
**Run:** Every Monday morning
**Output:** A dated analysis in `ops/acquisition/YYYY-MM-DD-monday-analysis.md` (create the folder on first run) covering last week's acquisition performance, the trend across the trailing 4 weeks, signals worth acting on, action-item status, and Mauro's action items for the week.

---

## What This Skill Does

This is the recurring weekly review Mauro runs on his own brand's acquisition. It is **acquisition/ops analysis**, not content ideation. Keep it distinct from `skills/research/weekly-research.md` (which produces post + article ideas). They share inputs (X analytics, booking data) but answer different questions: this skill answers "how did acquisition perform and what do I act on this week," not "what should I post."

The skill takes the canonical inputs, reproduces the fixed 10-section structure, adds a "Diff vs last week" read on every metric block, and carries the action-item and open-question registers forward from the prior week so nothing falls off the list silently.

The action items in §9 feed the daily system (`skills/ops/daily-ops.md`, Component 6), which spreads them across the week's days.

---

## Required Reading

Before producing the analysis, read in this order:

1. **The two most recent files in `ops/acquisition/`**: the prior Monday analysis, for the action-item + open-question registers to carry forward. (On the first run there is no prior file; start both registers fresh.)
2. **`CLAUDE.md` §2 (ICP)**: the qualification read. Established agency owners at mid six figures a month and up. Score calls against this floor consistently week to week.

---

## Inputs Expected

Mauro drops or paths these for the prior week's window (default window: the trailing Mon–Sun, with context for the trailing 4 weeks).

| Input | What it gives | Source |
|---|---|---|
| X analytics | Per-post + weekly impressions, posts, profile visits, top performers | X Premium → Analytics → Export |
| Booking data | Call volume, channel attribution, qualification signal per booking | [BOOKING TOOL, no booking flow exists for this brand yet; flag as gap until one is live] |
| Call notes / DM log | Qualified vs unqualified read, pain phrases, where each lead came from | Manual (Mauro's notes, DM screenshots) |
| LinkedIn analytics | Weekly impressions + top posts | [LINKEDIN, add when Mauro posts there consistently] |

If any input is missing, run on what's available and flag the gap in §8 (do not block). Anything that always needs separate human input gets listed under §8 rather than guessed.

### Standing interpretation rules

1. **Conducted vs booked.** Call volume counts by **conducted** date. Booking dates lead or lag (someone sees a post one week, books a slot that lands in another), so do not reconcile the two by date. Use booking data for channel attribution only, never for volume. A call conducted this week can trace to content from one or two weeks earlier, and this matters for post-to-call attribution.
2. **Filter internal and existing-client events.** Exclude internal meetings and existing-client calls from channel attribution. Only net-new leads count.
3. **LinkedIn exports have no post text.** Aggregate exports show URLs and metrics but not body copy. Read the topic from the URL slug or from the cross-posted X version.

---

## Step 1: Last-week snapshot

Build the W[N] table: total calls (or qualified conversations, while call volume is near zero), qualified, unqualified, no-shows, qual rate. Then the by-source breakdown (Content / DMs / Referrals / Other) with qualified count per source.

**Add the diff:** every figure gets a "vs last week" and "vs target" read. Flag any line that moved more than one standard step.

## Step 2: Trend across the trailing 4 weeks

Two tables, W[N-3] → W[N]:
- **X impressions/week**: impressions, posts, impressions/post, profile visits. The impressions/post ratio is the key signal. Overposting collapses it.
- **Call / conversation volume**: booked, conducted, cancelled per week.

Then actuals vs the standing target across all 4 weeks. State plainly how many of the last 4 weeks hit target. [TARGET, define the weekly qualified-conversation target once the offer is live.]

## Step 3: Top signals worth acting on

Build these every week:
- **A. Channel attribution** (trailing month): ranked share by channel.
- **B. Qualification distribution**: flag the % of conversations below the ICP floor. This is the intake-leak signal.
- **C. Top posts** (X analytics, trailing month): top 5 by impressions, note the format/formula each uses.
- **D. Channel-specific collapses or spikes**: any source that went to zero qualified or spiked no-shows.

## Step 4: Incidents (transparency record)

Any process failure, missed commitment, or execution slip from the week. Record: what happened, when caught, how, impact, process fix put in place, current status. Written down so it can't be quietly forgotten.

## Step 5: Action-item status check (carry-forward register)

Pull every open action item from the prior 1–2 analyses. Mark each `[x]` closed or `[ ]` open. **Open items roll forward**: they must reappear next week until closed. This is the mechanism that stops items falling off the list silently.

## Step 6: Narrative fields

Draft these in Mauro's voice: Learning of the week / Did I follow last week's plan / Why I did-or-didn't hit the goal / TEST (hypothesis + metrics) / ACTION (what I will do). Ground each in the week's actual numbers.

## Step 7: Metric actuals (from data on hand)

Table of metrics the skill *can* fill from the inputs, with the value and its source cited.

## Step 8: Metric actuals needing separate input

Table of metrics that need a human/external source (LinkedIn impressions, auto-DM logs, booking data while no tool is live). Name the source for each so Mauro knows where to get it.

## Step 9: Top action items for Mauro this week

The 3–5 highest-leverage moves, each concrete enough to start. Tie each to a signal from §1–4. These feed `daily-ops` Component 6 and get spread across the week.

## Step 10: Open questions (carry-forward register)

Unresolved questions and undefined terms (e.g. "is the weekly target still right"). Like §5, **unanswered questions roll forward** until resolved. Resolve them during the week, then retire them.

## Integrations (not yet live for this brand)

Mark these as placeholders until they exist; skip them silently in the meantime:
- [DASHBOARD, no performance dashboard exists for this brand. If one is built, append the week's numbers to its data files here as a Step 11.]
- [NOTION WEEKLY REVIEW DB, see `skills/ops/content-loop.md`. When the Notion loop is set up, write the week's row (performance, learnings, hypotheses) there after the analysis.]
- [PAID ADS REPORT, no paid spend is running for this brand. If X ads ever run, add a standalone weekly ads report step.]

Anti-fabrication applies everywhere: blank over guessed.

---

## Output Format

Reproduce the 10-section scaffold below verbatim each week. Header block first:

```markdown
# Monday Acquisition Analysis: YYYY-MM-DD

**For:** Mauro's weekly acquisition review
**Period analyzed:** [Mon–Sun] (W[N]) with W[N-3]–[N] trend context
**Prior entry:** ops/acquisition/[previous file]

---

## Inputs analyzed
## 1. Last week snapshot (W[N])
## 2. Trend across [month] (W[N-3]–[N])
## 3. Top signals worth acting on
## 4. [Incidents this week, omit heading if none]
## 5. Action items from prior weeks: status check
## 6. W[N] narrative fields
## 7. Metric actuals (from data I have)
## 8. Metric actuals that need separate input
## 9. Top action items for Mauro this week
## 10. Open questions
```

Keep it skim-readable: tables over prose for all metric blocks, narrative only in §6, §9, §10.

---

## Routing Instructions

When this skill is triggered:
1. Read the two most recent `ops/acquisition/` files (if any) + `CLAUDE.md` §2.
2. Ingest whatever inputs Mauro provides; flag missing ones in §8.
3. Run Steps 1–10.
4. Write to `ops/acquisition/YYYY-MM-DD-monday-analysis.md`.
5. Carry forward any open action items (§5) and unresolved questions (§10) from last week.
6. Hand the §9 items to the daily system (`daily-ops` Component 6) so they get real due-days.
7. Commit + push per the repo CLAUDE.md non-negotiable rule.

---

## Trigger Phrases

- "Monday acquisition analysis" / "Monday review"
- "Run the Monday analysis"
- "How did acquisition go last week?"

---

## Anti-Patterns

- **Don't fabricate metric values.** If a metric needs data you don't have, it goes in §8 with the source named, never a guessed number. (See `feedback_no_fabricated_performance_numbers`.)
- **Don't drop open items.** Every unclosed action item and unanswered question rolls forward until it's closed/resolved. Sections 5 and 10 are registers, not snapshots.
- **Don't merge this with the content ideation brief.** Different question, different output. If Mauro wants post ideas, that's `weekly-research.md`.
- **Don't bury an incident.** §4 exists so nothing gets quietly forgotten. Record it with the process fix already attached.
- **Don't recalibrate a target inside the analysis.** Surface "is this target still right" as an open question in §10; don't silently change it.
- **Don't read one week in isolation.** Every metric block carries a diff vs last week and vs the 4-week trend. A single bad or good week is noise until the trend confirms it.

---

## Notes on the pattern

The structure is expected to stabilize over the first 2–3 runs on this brand. When it does, fold any consistent additions (new standing tables, new carry-forward registers) back into the §1–10 scaffold above and bump the version.
