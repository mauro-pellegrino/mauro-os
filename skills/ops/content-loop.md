# Skill: Weekly Content Loop (Notion + repo)

**Version:** 2.0
**Created:** 2026-07-08, retargeted to this brand 2026-07
**Trigger phrases:** "run the content loop", "weekly content review", "set this week's hypotheses", "log last week's content performance"
**What it is:** The closed weekly loop for organic content on Mauro's accounts (X / LinkedIn / YouTube / Email). Adapted from the wiz-of-ecom Content Control Panel, implemented lean in Notion. Performance → Hypothesis → Implementation → Performance.

---

## Where it lives

**Notion (the execution + measurement surface):**

[NOTION, not set up for this brand yet. When it is, create these and record the DB IDs here:]
- **Content Calendar**: ONE database; a post travels through `Status`: Idea → Drafting → Needs Review → Ready to Schedule → Scheduled → Posted. This single flow replaces the wiz system's 3 separate Miro tables (Hypothesis + Implementation + Performance).
- **Content Vehicles**: the format library, funnel-tagged, with when-to-use + features. Related to the calendar via a `Vehicle` property (two-way; posts appear under each vehicle's `Posts`). Seed it with the formats already documented in `skills/content/` and tag borrowed reference formats separately from the ones actually in use. Use own vehicles first; reference vehicles are a swipe library, not the default.
- **Weekly Review & Hypotheses**: one row per week: last week's performance (Qualified Calls, Bookings, X Impressions) + What Worked / What Didn't / Learning + This Week's Hypotheses + Actions. Related to the calendar via `Planned Posts` ↔ `Week`. This is where the Monday analysis lives in Notion.
- **Views:** Pipeline (board by Status = the loop), Calendar (Juan's day view for scheduling: keep sacred), BOF Gap Monitor, Performance.

Until Notion exists, run the same loop in the repo: a weekly file under `ops/weekly/` with the same fields.

**Repo (the analysis + source side):**
- `skills/ops/monday-acquisition-analysis.md`: the acquisition-level performance read (calls, qualified, channel, top posts). Feeds the REVIEW step.
- Weekly X analytics exports: the post-level performance data.
- `brand/posts/`, `brand/sessions/`, transcript batches in `research/transcripts/`: the idea/angle sources feeding HYPOTHESIS.

---

## The weekly loop (run every Monday)

1. **PERFORMANCE (last week).** Take the weekly X analytics + the Monday acquisition analysis. On each `Posted` row, fill Impressions / Reactions / Comments / DMs Received / Qualified Calls, tick `Posted?`, and write one line in `Insights`.
2. **REVIEW.** Read the Performance view + BOF Gap Monitor. What worked / didn't, by Vehicle, Funnel Stage, and Topic. Name the pattern (this is the wiz "what worked on X / LI" board, done as a filter, not a separate board).
3. **HYPOTHESIS.** Create `Idea` rows for the coming week. Each carries: Vehicle, Funnel Stage, Awareness Level, Topic, Platform, `Hypothesis` (the bet + why), Inspiration. Balance the funnel deliberately. If the BOF Gap Monitor is thin, add BOF.
4. **IMPLEMENTATION.** Move rows Idea → Drafting → Needs Review → Ready to Schedule → Scheduled as they get produced. Juan schedules from the Calendar/Pipeline view.
5. **Loop.** After posting, results flow back into step 1 next Monday.

---

## Inputs that feed the loop (weekly cadence)

- **Weekly X analytics export** → post-level performance (step 1).
- **Monday acquisition analysis** → acquisition outcomes + channel read (steps 1-2).
- ⚠️ **Call transcription:** if a weekly review call ever exists, prefer tl;dv or Fathom over Gemini Meet notes (Gemini's are unreliable) so the analysis input is dependable.

---

## Notes
- Keep it lean. A simple calendar already went unfilled in the past, so resist rebuilding the full Miro sprawl (mind-maps, swipe files). The 80/20 is: the Status loop + the Vehicle library + the hypothesis fields.
- The Calendar/Pipeline day view is the one thing a simple calendar does well (Juan knows what to post when). Never bury it under the strategy layer.
- Foundations / pillars already live in the repo (`brand/`); mirror to Notion only if needed.
