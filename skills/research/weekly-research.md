# Weekly Ideation Briefing
**Version:** 2.0
**Run:** Every Monday morning
**Output:** 4 autodm post ideas + 3 article ideas, each grounded in own-account performance data plus competitor/trend signals.

---

## What This Skill Does

Replaces the v1 channel-scan flow with a data-driven ideation pipeline. Takes the previous week's analytics from X, LinkedIn, and Calendly, cross-references with competitor and trend signals (from the trendjack X API or manual scan), and produces a structured Monday brief.

The output is two specific buckets: autodm post ideas (for X distribution this week) and article ideas (for longer-form content this week).

---

## Required Reading

Before producing any written output, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. All copy must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.2 ICP in audience.md.

Also load: `accounts/lorenzo-x/wins-log.md` (recent named wins eligible for BOF posts) and the most recent `project_lorenzo_x_account` memory note for the current ICP read.

---

## Inputs Expected

The user pastes file paths or drops files for the previous week's window. Default window is the trailing 30-33 days.

| Input | Format | Source |
|---|---|---|
| X post-level analytics | `account_analytics_content_{start}_{end}.csv` | X Premium → Analytics → Content → Export |
| X account overview | `account_overview_analytics.csv` | X Premium → Analytics → Overview → Export |
| LinkedIn aggregate | `AggregateAnalytics_*.xlsx` | LinkedIn Creator Analytics → Export |
| Calendly events | `event-data-from-{start}-to-{end}.csv` | Calendly → Reports → Export |
| Trendjack X API output | inline JSON or CSV | Trendjack system (see Step 4) |

If any input is missing, run the analysis on what's available and flag the gap. Never block on a missing input.

---

## Step 1: Analyze Own X Data

For the post-level CSV, sort by these metrics and produce a top-20 ranking for each:

1. **Impressions** — raw reach
2. **New follows** — audience growth signal
3. **Profile visits** — call-booking proxy (highest-intent signal)
4. **Replies** — autodm keyword redemption proxy (when keyword-comment patterns are used)

For each top-10 post in the New Follows + Profile Visits rankings, capture:
- The opening hook line (first 12 words)
- The format (autodm lead magnet / brand breakdown / BOF win / pure link / thread opener / contrarian opener)
- The lead-magnet keyword used (if any)

Identify the dominant pattern: which post format converts engagements to follows + PV at the highest rate.

---

## Step 2: Analyze Own LinkedIn Data

From the xlsx export:

- Read the `TOP POSTS` sheet (sorted by Engagements and Impressions separately)
- Read the `FOLLOWERS` sheet for daily follower-add spikes (correlate with post dates)
- Read the `DEMOGRAPHICS` sheet for audience composition (industry, seniority, company size)

Cross-reference top X posts with top LinkedIn posts. The Claude-prompts format has consistently dominated both platforms in this window. Note when a post performs cross-platform vs. only on one.

Flag the **audience composition risk**: if >30% of the LinkedIn audience is in agency/marketing industries (vs the target brand-operator ICP), LinkedIn redemptions are lower-fit on average than X redemptions. Lead-magnet copy on LinkedIn may need a tighter qualifier.

---

## Step 3: Analyze Calls Data

From the Calendly CSV (filter out `Canceled = true`):

- **Channel attribution** — count responses to the "platform was this call booked on" question. Flag the Unknown bucket as a data gap.
- **Revenue tier** — distribution across the audience.md tiers (T1 / T2a / T2b / T3)
- **Spend tier** — distribution across $25K+, $50K+, $100K+ buckets
- **Pain phrases** — pull verbatim from the "main problems you're facing" response. Cluster into themes (creative diversity, creative fatigue, scaling ceiling, CPA inflation, restricted category, etc.)

Calculate **qualified-call rate** = (calls at $25K+/month spend OR $200K+/mo rev) / total held calls. Compare to historical baseline from `project_lorenzo_x_account.md`.

---

## Step 4: Pull Trendjack Signals

The trendjack X API output gives top-performing posts from the monitored creator list over the last 7 days. Default monitored list lives at the bottom of this skill.

For each trending post, capture:
- Author + post text + engagement metrics
- Core claim or take
- Why it's resonating (contrarian / data-backed / specific result / format play / live anxiety)
- Whether Growthub has a stronger / different angle on the same topic

**If the trendjack API output is not yet available**, fall back to manual scan of the monitored list (use WebFetch or paste from the user).

---

## Step 5: Generate Autodm Ideas (target: 4 per brief)

Each autodm idea must include:

```
### IDEA N: [Working title]

**Hook angle:** [The first line of the X post — must pass voice.md]
**Source signal:** [Specific own-data post + competitor/trend signal that supports this idea]
**Lead magnet promise:** [What the user gets when they comment the keyword]
**Keyword:** [Single word, ALL CAPS, no collision with existing autodm keywords]
**Predicted conversion:** [Why this will outperform — tie to a specific own-data benchmark]
```

Ideas should be sourced from a mix of:
- **Own high-performing patterns** — extend or deepen what's already working (e.g., new Claude prompts file in a different vertical)
- **Competitor moves** — counter-position or build on what a tracked competitor just did
- **Trend signals** — capitalize on a live anxiety or topic spike
- **Pain phrases from calls** — translate a verbatim ICP frustration into a lead-magnet hook

Aim for diversity across the 4 ideas: not all should be Claude prompt files. Vary format (prompt file / framework / playbook / swipe file / live audit offer).

---

## Step 6: Generate Article Ideas (target: 3 per brief)

Each article idea must include:

```
### ARTICLE N: [Working title]

**Angle:** [The core thesis, one sentence]
**Source:** [Own data signal + competitor/transcript reference that supports this]
**Target reader:** [ICP slice — e.g., "skincare DTC operators at $25K-$100K/mo Meta spend"]
**Format:** [LinkedIn doc carousel / X long-form / Notion 5-page guide / 10-prompt Claude system]
**Distribution plan:** [Which autodm idea (if any) it pairs with, and on what channel it launches first]
```

Articles should run deeper than autodms. They cover a teardown, a playbook, or a contrarian thesis with multiple supporting examples. Each article should be capable of being repurposed across 2-4 autodm posts over the following weeks.

---

## Step 7: Output Format

```
GROWTHUB WEEKLY IDEATION BRIEF
Week of: [DATE]
Window analyzed: [START] – [END]

📊 TOP PATTERNS THIS WINDOW
- Dominant own-account pattern: [...]
- Underperformers to retire: [...]
- Cross-platform consistency: [...]

📞 CALLS QUALITY SIGNAL
- Held: [N] | Qualified: [N] ([%])
- Channel attribution: [X / LinkedIn / Email / Unknown]
- Top pain themes: [...]

🔥 TRENDJACK / COMPETITOR SIGNALS
- [Top 3-5 trending posts from monitored list with the Growthub angle]

🎯 AUTODM IDEAS (4)
[Use Step 5 format]

📰 ARTICLE IDEAS (3)
[Use Step 6 format]

🗣️ ICP LANGUAGE TO MINE
[3-5 verbatim phrases from calls worth using in hooks this week]

🛠️ ACTION ITEMS
- Memory updates worth pinning: [...]
- Data gaps to close: [...]
- Distribution decisions: [...]
```

---

## Monitored Trendjack Accounts

The trendjack X API should pull top posts from the trailing 7 days for these accounts. Maintain this list as the operator landscape evolves.

| Creator | X Handle | Coverage |
|---|---|---|
| Fraser Cottrell | @sourfraser | Portfolio threads, ad format breakdowns, $300M+ spend authority |
| Nick Theriot | @nicktheriot_ | Meta ads scaling, frameworks |
| Spencer Pawliw | @spencerpawliw | Creative strategy, performance |
| Andrew Faris | @andrewjfaris | Ecom / Meta sharp operator takes |
| Cody Plofker | @codyplofker | CMO perspective, transparent results |
| DTC Alchemist | @dtc_alchemist | Creative strategy, operator |
| DTC Midas | @DTCMidas | Ecom operator, real results |
| Shaun Eng | @shauneng | Ecom scaling, buyer psychology |
| Chase Chappell | @chasechappell | Hook formulas, $600M+ managed |

---

## Routing Instructions

When this skill is triggered:
1. Resolve active brand → Growthub
2. Load: `voice.md`, `positioning.md`, `audience.md`, `learnings.md`, `accounts/lorenzo-x/wins-log.md`
3. Cross-reference current memory in `project_lorenzo_x_account` for the latest ICP read
4. Run Steps 1-6 above
5. Output the brief in the Step 7 format
6. Save the brief to `research/weekly-briefs/{YYYY-MM-DD}-ideation.md`
7. Log any standout ICP language to `brands/growthub/learnings.md`
8. Suggest 1-2 memory updates if a pattern has shifted

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
- Don't propose autodm ideas with a keyword that collides with an existing live autodm. Check the wins-log + recent posts before assigning.
- Don't suggest content angles without a specific own-data or trend signal to ground them.
- Don't skip the calls section — pain phrases there are the single best source of new hook material.
- Don't recommend retiring an autodm format based on one underperforming post. Look at the rolling 4-week average.
