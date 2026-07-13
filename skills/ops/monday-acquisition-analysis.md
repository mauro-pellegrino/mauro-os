# Skill: Monday Acquisition Analysis

**Version:** 1.1
**Created:** 2026-06-02
**Run:** Every Monday morning, before the weekly acquisition call with Lorenzo
**Output:** (1) A dated prep doc in `acquisition-calls/YYYY-MM-DD-monday-analysis.md` covering last week's acquisition performance, the trend across the trailing 4 weeks, signals worth raising, action-item status, tracker cells to fill, and Mauro's action items for the week. (2) The same week's numbers appended to the dashboard CSVs in `future-projects/dashboard/data/` so the team dashboard renders live (Step 11).

---

## What This Skill Does

This is the recurring prep analysis Mauro runs ahead of the weekly acquisition call with Lorenzo. It is **acquisition/ops analysis**, not content ideation — keep it distinct from `skills/research/weekly-research.md` (which produces post + article ideas). They share two inputs (Calendly export, X analytics) but answer different questions: this skill answers "how did acquisition perform and what do I raise on the call," not "what should I post."

The skill takes the four canonical inputs, reproduces the fixed 10-section structure, adds a "Diff vs last week" read on every metric block, and carries the action-item and open-question registers forward from the prior week so nothing falls off the list silently.

The first entry in this pattern is `acquisition-calls/2026-06-01-monday-analysis.md` — use it as the reference for tone, depth, and section shape.

---

## Required Reading

Before producing the analysis, read in this order:

1. **The two most recent files in `acquisition-calls/`** — the prior Monday analysis (for the action-item + open-question registers to carry forward) and the most recent raw call notes (for decisions and next-steps committed on the last call).
2. **`project_lorenzo_x_account.md` memory** — current ICP read (brand operators $100K–$1M+/mo Meta spend) and the qualification floor used to score calls.
3. **`CLAUDE.md` §2 (ICP)** — revenue and spend tiers, so tier distribution is bucketed consistently week to week.

---

## Inputs Expected

Mauro drops or paths these for the prior week's window (default window: the trailing Mon–Sun, with W-context for the trailing 4 weeks).

| Input | What it gives | Source |
|---|---|---|
| Call structure tracker | Qualified/unqualified/no-show counts, by-source breakdown, weekly tab | Google Sheet (weekly tabs) |
| Calendly events export | Discovery + pre-audit call volume, channel attribution, revenue/spend tier per booking | Calendly → Reports → Export |
| X analytics | Per-post + weekly impressions, posts, profile visits, top performers | X Premium → Analytics → Export |
| Weekly Targets tracker | Targets vs actuals per metric row; the narrative fields to fill | Google Sheet |

If any input is missing, run on what's available and flag the gap in §8 (do not block). Some cells **always** need separate human input (Francisco's ADS SaaS data, autoDM logs, LinkedIn impressions) — list them under §8 rather than guessing.

### Standing interpretation rules (confirmed by Mauro 2026-06-15)

1. **Conducted vs booked.** The call structure tracker is by **conducted** date and is the source of truth for call volume. Calendly booking dates lead or lag (someone sees a post one week, hits the site, and books a slot that lands in a different week), so do NOT reconcile the two by date. Use Calendly for channel attribution and tier only, never for volume. A call conducted this week can trace to content from one or two weeks earlier — this matters for post→call attribution.
2. **Filter internal/existing-client events.** 15-minute and 30-minute Calendly events are internal or existing-client meetings (e.g. Mauro, Brando, Patrick/Kathmandu/Deepak, Bau Cosmesi). Exclude them from channel attribution. Bau Cosmesi / Stefano Colarieti is a client, ignore.
3. **LinkedIn export has no post text.** The aggregate LinkedIn export shows URLs and metrics but not body copy. Every post URL contains the headline slug, so read the topic from the slug, or from the cross-posted X version (Lorenzo cross-posts X → LinkedIn). Full body text needs the in-app view.
4. **Calendly comes in two forms.** Bogdan/Growthub Agency exports as a full-history CSV (hosted under mauro@growthub.agency); Lorenzo's is often only available as the Slack-automation event paste (booking-level, no rev/spend answers). When only the Slack paste is available, tier distribution for the qualified set goes in §8 as needs-input.

---

## Step 1: Last-week snapshot

From the call structure tracker, build the W[N] table: total showed qualified, total calls, qualified (name them), unqualified, qualified+no-show, unqualified+no-show, qual rate. Then the by-source breakdown (Content / Ads / Cold email / Referrals) with qualified count per source.

**Add the diff:** every figure gets a "vs last week" and "vs target" read. Flag any line that moved >1 standard step (e.g., unqualified no-shows unusually high, qual rate down from prior week).

## Step 2: Trend across the trailing 4 weeks

Two tables, W[N-3] → W[N]:
- **X impressions/week**: impressions, posts, impressions/post, profile visits. The impressions/post ratio is the key signal — overposting collapses it.
- **Discovery call volume** (Calendly): calls, attended, cancelled per week.

Then qualified-showed actuals vs the standing target across all 4 weeks. State plainly how many of the last 4 weeks hit target.

## Step 3: Top signals worth raising with Lorenzo

Build these every week:
- **A. Channel attribution** (Calendly platform field, trailing month): ranked share by channel.
- **B. Tier distribution** (revenue × spend): flag the % of calls below the qualification floor — this is the intake-leak signal.
- **C. Top posts** (X analytics, trailing month): top 5 by impressions, note the format/formula each uses.
- **D. Channel-specific collapses or spikes**: any source that went to zero qualified or spiked no-shows.

## Step 4: Incidents (transparency record)

Any campaign error, spend mistake, or process failure from the week. Record: what happened, when caught, how, spend impact, process fix put in place, current status. This goes in the doc so it's a heads-up before the call, never a surprise reveal.

## Step 5: Action-item status check (carry-forward register)

Pull every open action item from the prior 1–2 call notes. Mark each `[x]` closed or `[ ]` open. **Open items roll forward** — they must reappear next week until closed. This is the mechanism that stops items falling off the list silently.

## Step 6: Narrative fields for the tracker

Draft the Weekly Targets tracker narrative cells in Mauro's voice: Learning of the week / Did we follow last week's plan / Why we did-or-didn't hit the goal / TEST (hypothesis + metrics) / ACTION (what we will do). Ground each in the week's actual numbers.

## Step 7: Metric actuals (from data on hand)

Table of tracker cells the skill *can* fill from the four inputs, with the value and its source cited.

## Step 8: Metric actuals needing separate input

Table of tracker cells that need a human/external source (LinkedIn impressions, autoDM logs, ADS SaaS data from Francisco, NEW article/long-form counts). Name the source for each so Mauro knows who to ask.

## Step 9: Top action items for Mauro this week

The 3–5 highest-leverage moves, each concrete enough to start. Tie each to a signal from §1–4.

## Step 10: Open questions to raise at the call (carry-forward register)

Unresolved questions and undefined terms (e.g., "what does AX mean in the tracker," "is the 8-qualified target still right"). Like §5, **unanswered questions roll forward** until resolved. Resolve them on the call, then retire them.

## Step 11: Feed the dashboard CSVs (repo-native, no Google Sheets)

The team dashboard (`future-projects/dashboard/`) reads committed CSVs in `future-projects/dashboard/data/` and falls back to them when no `*_CSV_URL` env var is set. There is **no Google Sheet / Joao / Form dependency** in the live path — this skill is the data source. After writing the analysis, append this week's row to each CSV. Match the existing header columns exactly (the dashboard reads by column name; the contract is `dashboard/lib/types.ts`). Do not rename columns.

`week_start` is the **Monday** of the analyzed week (the conducted Mon–Sun window), `YYYY-MM-DD`. Append one row per file; never overwrite prior weeks.

| CSV | Row to append | Where the numbers come from |
|---|---|---|
| `weekly-metrics.csv` | `calls_booked`, `calls_booked_qualified`, `calls_conducted`, `calls_conducted_qualified` (conducted = source of truth, §1), `qualified_target`, `x_impressions_organic` (both profiles combined, §3D), `x_paid_impressions`/`x_paid_spend_eur` (only if a clean weekly split exists, else leave blank), `x_new_follows`, `li_impressions_organic` (§2), `notes` (the one-line headline) | §1, §2, §3 |
| `call-sources.csv` | One row per source (Content / Ads / Cold Email / Referral): `qualified`, `unqualified`, `no_show`, `qualified_names` | §1 by-source table |
| `weekly-checkin.csv` | `learning_of_week`, `followed_plan`, `why_hit_or_miss`, `hypothesis_this_week`, `action_this_week` | §6 narrative fields verbatim |

Rules:
- **Anti-fabrication still applies.** If a cell needs a source you don't have this week (e.g. a clean weekly paid-impressions split, new-follows not in the export), leave it blank rather than guessing, and note it in the `notes` cell. A blank renders as 0; that is preferable to a fabricated number.
- **CSV quoting:** wrap any field containing a comma in double quotes; escape internal double quotes by doubling them (`""`).
- `content-log.csv` is the notable-posts log (top performers + flops). Append entries only when you have the post URL + impressions + engagement rate; the §3 top-posts table alone (no URL/eng-rate) is not enough, so skip it rather than half-fill.

## Step 12: X ads report + post to Slack #x-ads

When Mauro provides an X Ads Manager export for the week (an `Exportxads*.xlsx` with results + Location / Platform / Age / Gender breakdowns), produce a standalone X ads report at `accounts/lorenzo-x/x-ads-report-YYYY-MM-DD.md`. Use `accounts/lorenzo-x/x-ads-report-2026-06-22.md` as the reference for structure: verdict, this-week numbers, geo / age / gender breakdowns, what the run proves, **this week's test (which proven organic winners to promote + targeting + booking path)**, recommended fix, decisions for Lorenzo.

The this-week-test section pulls the top 3 proven organic posts from §3 of the analysis (or the content-log) and proposes them as the ad creatives, since organic is what converts. Always include the booking-path block; if `{{calendly_url}}` is still PENDING in `account-config.md`, flag it as a blocker rather than inventing a link.

Then post a concise summary to the private Slack channel **#x-ads** (`C0BC8RCPCV8`) so Lorenzo sees it without opening the repo. **Create it as a draft first** (`slack_send_message_draft`) for Mauro to review, then send on his confirmation, unless Mauro has said to post directly. Keep the Slack summary to: the verdict line, the headline numbers table, the geo + age skew, and this week's 3 creatives-to-test. Link the decisions to the full report.

If no X ads export was provided that week, skip this step (do not regenerate from stale data).

## Step 13: Write the week's row to the Notion Weekly Review DB

After the analysis, create one row in the Notion **Weekly Review & Hypotheses** database (data source `collection://0ad86140-89b1-4605-af4d-3dc1b15be5bc`) via `notion-create-pages`. This is where the Monday analysis lives for the content loop (`skills/ops/content-loop.md`). Fill: Week (e.g. "W28 · [range]"), Week Start (Monday), Qualified Calls, Bookings, X Impressions, X Ads Spend, What Worked, What Didn't Work, Learning of the Week, This Week's Hypotheses, Actions. The hypotheses then become `Idea` rows in Content Calendar v2 (`collection://dfaeb6cb-7420-4af3-8b0d-a3de6a390042`), linked back via the `Week` relation. Anti-fabrication still applies (blank over guessed).

---

## Output Format

Reproduce the 10-section scaffold below verbatim each week. Header block first:

```markdown
# Monday Acquisition Analysis — YYYY-MM-DD

**For:** Mauro's prep ahead of the weekly acquisition call with Lorenzo
**Period analyzed:** [Mon–Sun] (W[N]) with W[N-3]–[N] trend context
**Prior entry:** acquisition-calls/[previous file]

---

## Inputs analyzed
## 1. Last week snapshot (W[N])
## 2. Trend across [month] (W[N-3]–[N])
## 3. Top signals worth raising with Lorenzo
## 4. [Incidents this week — omit heading if none]
## 5. Action items from prior calls — status check
## 6. W[N] — narrative fields to fill in the tracker
## 7. Metric actuals to fill (from data I have)
## 8. Metric actuals that need separate input
## 9. Top action items for Mauro this week
## 10. Open questions to raise at the call
```

Keep it skim-readable: tables over prose for all metric blocks, narrative only in §6, §9, §10.

The CSV rows from Step 11 are a side-output, not part of this markdown scaffold.

---

## Routing Instructions

When this skill is triggered:
1. Read the two most recent `acquisition-calls/` files + `project_lorenzo_x_account` memory + CLAUDE.md §2.
2. Ingest whatever of the four inputs Mauro provides; flag missing ones in §8.
3. Run Steps 1–10.
4. Write to `acquisition-calls/YYYY-MM-DD-monday-analysis.md`.
5. Carry forward any open action items (§5) and unresolved questions (§10) from last week.
6. Run Step 11: append this week's rows to the dashboard CSVs in `future-projects/dashboard/data/`.
7. Run Step 12 if an X ads export was provided: write the X ads report and draft/post the summary to Slack #x-ads.
8. Commit + push per the repo CLAUDE.md non-negotiable rule (the dashboard auto-deploys from the push).
7. After the call: update the file's §5 and §10 with what closed/resolved on the call, and log any new next-steps as a fresh `acquisition-calls/YYYY-MM-DD.md` raw notes file.

---

## Trigger Phrases

- "Monday acquisition analysis" / "Monday call prep"
- "Prep for the acquisition call" / "prep the Lorenzo call"
- "Run the Monday analysis"
- "What do I raise on the call this week?"

---

## Anti-Patterns

- **Don't fabricate metric values.** If a cell needs Francisco's ADS data or autoDM logs, it goes in §8 with the source named — never a guessed number. (See `feedback_no_fabricated_performance_numbers`.)
- **Don't drop open items.** Every unclosed action item and unanswered question rolls forward until it's closed/resolved. Section 5 and 10 are registers, not snapshots.
- **Don't merge this with the content ideation brief.** Different question, different output. If Mauro wants post ideas, that's `weekly-research.md`.
- **Don't bury an incident.** §4 exists so the call has no surprise reveals. Record it with the process fix already attached.
- **Don't recalibrate a target inside the analysis.** Surface "is this target still right" as an open question in §10 for the call to decide; don't silently change it.
- **Don't read one week in isolation.** Every metric block carries a diff vs last week and vs the 4-week trend — a single bad or good week is noise until the trend confirms it.

---

## Notes on the pattern

This SOP was formalized after the first cycle (`2026-06-01`). The structure is expected to stabilize over 2–3 more runs. When it does, fold any consistent additions (new standing tables, new carry-forward registers) back into the §1–10 scaffold above and bump the version.
