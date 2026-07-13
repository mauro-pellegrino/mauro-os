# Skill: Weekly Content Loop (Notion + repo)

**Version:** 1.0
**Created:** 2026-07-08
**Trigger phrases:** "run the content loop", "weekly content review", "set this week's hypotheses", "log last week's content performance"
**What it is:** The closed weekly loop for organic content (Lorenzo + Bogdan, X/LI/YT/Email). Adapted from the wiz-of-ecom Content Control Panel, implemented lean in Notion. Performance → Hypothesis → Implementation → Performance.

---

## Where it lives

**Notion (the execution + measurement surface):**
- **Content Calendar v2** — data source `collection://dfaeb6cb-7420-4af3-8b0d-a3de6a390042` (db page `dc5ed41a968047eb83603a17432e1739`), under the "Client Acquisition" page. ONE database; a post travels through `Status`: Idea → Drafting → Needs Review → Ready to Schedule → Scheduled → Posted. This single flow replaces the wiz system's 3 separate Miro tables (Hypothesis + Implementation + Performance).
- **Content Vehicles** — data source `collection://de7379ce-f98d-4a12-8dbf-f8ba0a9f8ecb` (db `e68b109bee68412c8425bd1510975c2d`). 26 documented formats, funnel-tagged, with when-to-use + features. Related to v2 via the `Vehicle` property (two-way; posts appear under each vehicle's `Posts`).
- **Views:** Pipeline (board by Status = the loop), Lorenzo, Bogdan, Calendar (Joao's day view — keep sacred), BOF Gap Monitor, Performance.
- **Weekly Review & Hypotheses** — db `b098fe2ba8634d238c80e0637b72cd0f`, data source `collection://0ad86140-89b1-4605-af4d-3dc1b15be5bc`. One row per week: last week's performance (Qualified Calls, Bookings, X Impressions, X Ads Spend) + What Worked / What Didn't / Learning + This Week's Hypotheses + Actions. Related to v2 via `Planned Posts` ↔ `Week`. **This is where the Monday analysis lives in Notion.**
- **Vehicle library — use OUR vehicles first.** The "Our Vehicles (use these)" view filters to Origin = "Growthub — we use this" (13 real vehicles). The 26 wiz-of-ecom vehicles are tagged "Reference" — a swipe library, not the default.
- **Old calendar** (`1d5f06a5-b3df-8048-8192-d01349037126`) — legacy; kept for Joao's day-planning habit until v2 is adopted. Do not delete without Mauro's ok.

**Repo (the analysis + source side):**
- `skills/ops/monday-acquisition-analysis.md` — the acquisition-level performance read (calls, qualified, channel, top posts). Feeds the REVIEW step.
- Weekly X analytics exports (Mauro sends every week) — the post-level performance data.
- `accounts/lorenzo-x/faq-tweets.md`, transcript batches, research pipeline — the idea/angle sources feeding HYPOTHESIS.

---

## The weekly loop (run every Monday)

1. **PERFORMANCE (last week).** Take Mauro's weekly X analytics + the Monday acquisition analysis. On each `Posted` row in v2, fill Impressions / Reactions / Comments / DMs Received / Qualified Calls, tick `Posted?`, and write one line in `Insights`. Engagement Rate auto-calculates.
2. **REVIEW.** Read the Performance view + BOF Gap Monitor. What worked / didn't, by Vehicle, Funnel Stage, and Topic. Name the pattern (this is the wiz "what worked on X / LI" board, done as a filter, not a separate board).
3. **HYPOTHESIS.** Create `Idea` rows for the coming week. Each carries: Vehicle, Funnel Stage, Awareness Level, Topic, Owner, Platform, `Hypothesis` (the bet + why), Writer, Strategist, Inspiration. Balance the funnel deliberately — if BOF Gap Monitor is thin, add BOF.
4. **IMPLEMENTATION.** Move rows Idea → Drafting → Needs Review → Ready to Schedule → Scheduled as they get produced. Joao schedules from the Calendar/Pipeline view.
5. **Loop.** After posting, results flow back into step 1 next Monday.

---

## Inputs that feed the loop (Mauro's weekly cadence)

- **Weekly X analytics export** → post-level performance (step 1).
- **Monday acquisition call + analysis** → acquisition outcomes + channel read (steps 1-2).
- ⚠️ **Meeting transcription:** Gemini Meet notes are unreliable. Prefer **tl;dv or Fathom** (both connected) for the Monday call so the analysis input is dependable.

---

## Notes
- Keep it lean. The team barely filled the old simple calendar, so resist rebuilding the full Miro sprawl (mind-maps, swipe files). The 80/20 is: the Status loop + the Vehicle library + the hypothesis fields.
- The Calendar/Pipeline day view is the one thing the old calendar did well (Joao knows what to post when). Never bury it under the strategy layer.
- Foundations / pillars already live in the repo (`brands/`, `accounts/`); mirror to Notion only if needed.
