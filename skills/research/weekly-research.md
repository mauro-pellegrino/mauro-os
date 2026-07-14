# Weekly Ideation Briefing
**Version:** 3.0 (retargeted to this brand 2026-07)
**Run:** Every Monday morning
**Output:** 4 autodm post ideas + 3 article ideas, each grounded in own-account performance data plus competitor/trend signals.

---

## What This Skill Does

A data-driven ideation pipeline. Takes the previous week's analytics from X (and LinkedIn / booking data where available), cross-references with competitor and trend signals, and produces a structured Monday brief.

The output is two specific buckets: autodm post ideas (for X distribution this week) and article ideas (for longer-form content this week).

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the pre-publish checklist in voice.md. Ground every audience-facing decision (segment, stated pain, language) in the ICP in audience.md: established agency owners whose pipeline runs on referrals and outreach, who want an AI content system installed.

Also load: `brand/positioning.md` (the three content pillars) and any recent wins worth a BOF post. [WINS LOG, create `brand/wins-log.md` as results come in; until then, pull wins from `brand/sessions/` and Mauro directly.]

---

## Inputs Expected

The user pastes file paths or drops files for the previous week's window. Default window is the trailing 30-33 days.

| Input | Format | Source |
|---|---|---|
| X post-level analytics | `account_analytics_content_{start}_{end}.csv` | X Premium → Analytics → Content → Export |
| X account overview | `account_overview_analytics.csv` | X Premium → Analytics → Overview → Export |
| LinkedIn aggregate | `AggregateAnalytics_*.xlsx` | LinkedIn Creator Analytics → Export [add when Mauro posts there consistently] |
| Booking / calls data | export or manual notes | [BOOKING TOOL, no booking flow exists for this brand yet; use DM conversations + call notes in the meantime] |
| Trend signals | inline JSON, CSV, or pasted posts | [TRENDJACK, no X API monitoring set up for this brand; manual scan fallback, see Step 4] |

If any input is missing, run the analysis on what's available and flag the gap. Never block on a missing input.

---

## Step 1: Analyze Own X Data

For the post-level CSV, sort by these metrics and produce a top-20 ranking for each:

1. **Impressions**: raw reach
2. **New follows**: audience growth signal
3. **Profile visits**: intent proxy (highest-intent signal)
4. **Replies**: autodm keyword redemption proxy (when keyword-comment patterns are used)

For each top-10 post in the New Follows + Profile Visits rankings, capture:
- The opening hook line (first 12 words)
- The format (autodm lead magnet / build-in-public breakdown / BOF win / pure link / thread opener / contrarian opener)
- The lead-magnet keyword used (if any)

Identify the dominant pattern: which post format converts engagements to follows + PV at the highest rate.

---

## Step 2: Analyze Own LinkedIn Data (when available)

From the xlsx export:

- Read the `TOP POSTS` sheet (sorted by Engagements and Impressions separately)
- Read the `FOLLOWERS` sheet for daily follower-add spikes (correlate with post dates)
- Read the `DEMOGRAPHICS` sheet for audience composition (industry, seniority, company size)

Cross-reference top X posts with top LinkedIn posts. Note when a post performs cross-platform vs only on one.

Flag the **audience composition** read: the target ICP is agency owners and founders, so check what share of the LinkedIn audience is actually founder/owner seniority in agency-adjacent industries. If the audience skews junior or off-ICP, lead-magnet copy on LinkedIn needs a tighter qualifier.

---

## Step 3: Analyze Calls / Conversations Data

While no booking tool is live, run this on DM conversations and call notes instead of an export.

- **Channel attribution**: where did each qualified conversation start (X post, DM, referral, LinkedIn). Flag the Unknown bucket as a data gap.
- **Qualification**: distribution against the ICP floor (established agency owners, mid six figures a month and up, per `brand/audience.md`).
- **Pain phrases**: pull verbatim from what leads actually said. Cluster into themes (pipeline dried up, can't stay consistent, no time, cringe fear, outbound burnout).

Calculate **qualified-conversation rate** = qualified / total. Compare to the trailing weeks once a baseline exists.

---

## Step 4: Pull Trend Signals

[MONITORED CHANNELS, to be defined for Mauro's lane: AI systems for agency owners. Maintain the list at the bottom of this skill once defined.]

Until an automated pull exists, do a manual scan of the monitored list (WebFetch or pasted from the user) for top-performing posts from the trailing 7 days.

For each trending post, capture:
- Author + post text + engagement metrics
- Core claim or take
- Why it's resonating (contrarian / data-backed / specific result / format play / live anxiety)
- Whether Mauro has a stronger or different angle on the same topic

---

## Step 5: Generate Autodm Ideas (target: 4 per brief)

Each autodm idea must include:

```
### IDEA N: [Working title]

**Hook angle:** [The first line of the X post, must pass voice.md]
**Source signal:** [Specific own-data post + competitor/trend signal that supports this idea]
**Lead magnet promise:** [What the user gets when they comment the keyword]
**Keyword:** [Single word, ALL CAPS, no collision with existing autodm keywords]
**Predicted conversion:** [Why this will outperform, tied to a specific own-data benchmark, or [NO BASELINE YET] while the account is young]
```

Ideas should be sourced from a mix of:
- **Own high-performing patterns**: extend or deepen what's already working
- **Competitor moves**: counter-position or build on what a tracked creator just did
- **Trend signals**: capitalize on a live anxiety or topic spike
- **Pain phrases from conversations**: translate a verbatim ICP frustration into a lead-magnet hook

Aim for diversity across the 4 ideas: vary format (prompt file / framework / playbook / swipe file / live audit offer). All four should map to one of the three pillars (cobbler's children, anti-cringe authority, low-time system that converts).

---

## Step 6: Generate Article Ideas (target: 3 per brief)

Each article idea must include:

```
### ARTICLE N: [Working title]

**Angle:** [The core thesis, one sentence]
**Source:** [Own data signal + competitor/transcript reference that supports this]
**Target reader:** [ICP slice, e.g. "SEO agency founders whose referral pipeline just cracked"]
**Format:** [LinkedIn doc carousel / X long-form / Notion 5-page guide / 10-prompt Claude system]
**Distribution plan:** [Which autodm idea (if any) it pairs with, and on what channel it launches first]
```

Articles should run deeper than autodms. They cover a teardown, a playbook, or a contrarian thesis with multiple supporting examples. Each article should be capable of being repurposed across 2-4 autodm posts over the following weeks.

---

## Step 7: Output Format

```
WEEKLY IDEATION BRIEF: @maurojpelle
Week of: [DATE]
Window analyzed: [START] – [END]

📊 TOP PATTERNS THIS WINDOW
- Dominant own-account pattern: [...]
- Underperformers to retire: [...]
- Cross-platform consistency: [...]

📞 CONVERSATIONS QUALITY SIGNAL
- Held: [N] | Qualified: [N] ([%])
- Channel attribution: [X / LinkedIn / DM / Unknown]
- Top pain themes: [...]

🔥 TREND / COMPETITOR SIGNALS
- [Top 3-5 trending posts from the monitored list with Mauro's angle on each]

🎯 AUTODM IDEAS (4)
[Use Step 5 format]

📰 ARTICLE IDEAS (3)
[Use Step 6 format]

🗣️ ICP LANGUAGE TO MINE
[3-5 verbatim phrases from conversations or the audience.md language bank worth using in hooks this week]

🛠️ ACTION ITEMS
- Memory updates worth pinning: [...]
- Data gaps to close: [...]
- Distribution decisions: [...]
```

---

## Monitored Accounts

[MONITORED CHANNELS, to be defined for Mauro's lane: AI systems for agency owners. Candidates: creators covering AI-powered content ops, agency growth, and personal-brand-to-pipeline systems. Fill this table once chosen.]

| Creator | X Handle | Coverage |
|---|---|---|
| [TBD] | [TBD] | [TBD] |

---

## Routing Instructions

When this skill is triggered:
1. Load: `brand/voice.md`, `brand/positioning.md`, `brand/audience.md`, and any wins log / recent sessions.
2. Run Steps 1-6 above.
3. Output the brief in the Step 7 format.
4. Save the brief to `research/weekly-briefs/{YYYY-MM-DD}-ideation.md` (create the folder on first run).
5. Log any standout ICP language to `brand/audience.md`'s language bank or a learnings note.
6. Suggest 1-2 memory updates if a pattern has shifted.

---

## Trigger Phrases

Run this skill when you see:
- "Monday morning ideation"
- "Weekly research / weekly brief"
- "Run weekly ideation"
- "What should I post this week?"
- "Generate autodm + article ideas"

---

## Anti-Patterns

- Don't suggest a Claude prompts file as more than 50% of the autodm ideas. The format works but the well runs dry if every post is the same shape.
- Don't propose autodm ideas with a keyword that collides with an existing live autodm. Check recent posts before assigning.
- Don't suggest content angles without a specific own-data or trend signal to ground them.
- Don't skip the conversations section. Pain phrases there are the single best source of new hook material.
- Don't recommend retiring an autodm format based on one underperforming post. Look at the rolling 4-week average.
- Don't pitch to beginners. Every idea speaks to the established agency owner (see `feedback_expert_not_beginner_positioning`).
