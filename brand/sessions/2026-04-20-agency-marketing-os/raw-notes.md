# Session: Agency Marketing OS
**Date:** 2026-04-20
**Time spent:** ~1 full session
**Who was involved:** Mauro + Claude Code

---

## What triggered this

The existing weekly tracker (a Google Sheet with 200+ columns, merged headers, target/actual interleaved) was impossible to read patterns from. No visualisation layer. Hard to see what's actually working. Weekly meetings had the data but not the clarity.

The goal: build something Mauro can open every Monday and immediately know where things stand — without digging through a messy sheet.

---

## What we did, in order

### 1. Reorganised the AI skill library first

Before touching the dashboard, noticed the skills folder in growthub-os was a flat list of 15 files with no structure. Skills for YouTube, content repurposing, lead gen, research — all mixed together.

**Problem:** Hard to know what tool to reach for. Hard to explain to someone else what the system does.

**Decision:** Organise into 5 segments that mirror the actual workflow order:
- `research/` → `youtube/` → `content/` → `lead-gen/` → `creative-strategy/`

**Why this order:** That's literally how the work flows. You research first, then produce YouTube content, then repurpose it, then convert attention to leads.

**Also fixed:** CLAUDE.md's routing table was referencing skills that didn't exist on disk anymore. Updated both the routing table and the system architecture diagram.

**Lesson:** If your AI system's "brain file" references things that don't exist, it's working with outdated context. Treat CLAUDE.md like living documentation — if the files change, it has to change too.

---

### 2. Designed the dashboard architecture

**First instinct (rejected):** Connect the dashboard directly to the existing Google Sheet via API.

**Why we rejected it:**
- The sheet is structurally messy — 200+ columns, merged headers. Parsing it programmatically would break every time someone reshaped it.
- Live API connection adds OAuth setup, token refresh, rate limits, and a silent failure mode (dashboard just stops working and you don't know why).
- Every time someone adds a column or moves something, the dashboard breaks.

**Decision:** Create a separate, clean data contract. A new Google Sheet built purely for the dashboard, with a strict schema the VA owns. Total separation between "operational data" and "dashboard data."

**Lesson:** Don't build on top of messy data. Create a clean interface layer between your chaotic operational reality and the thing that needs to read it.

---

### 3. Decided on the data flow

Three options considered for how the VA delivers data:

**Option A:** VA sends CSV files → Mauro drops them in a folder → dashboard reads them.
Rejected: too much friction. VA has to learn CSV format. Files get lost in Slack.

**Option B:** VA fills a Google Sheet tab directly → Mauro exports CSV manually.
Rejected: still manual. Mauro has to remember to export every week.

**Option C:** VA fills a Google Form → responses auto-land in a Google Sheet tab → that tab is published as a live CSV URL → dashboard fetches automatically.
**Chosen.** VA gets a guided form (field by field, descriptions, required fields). Data lands in the sheet without Mauro touching anything. Dashboard always has the latest data.

**Why Google Forms specifically:**
- Forces the VA to fill fields one at a time — harder to skip or misformat
- Descriptions visible per field (Mauro added context for each question)
- No CSV skills required from the VA
- Timestamp column added automatically — useful for auditing

**Lesson:** The interface you give your VA determines the quality of the data you get back. A form with descriptions and required fields produces cleaner data than "fill in this spreadsheet."

---

### 4. Defined the three data sources

**Weekly Check-in (Mauro fills, in the Sheet directly):**
These are strategic reflections — hypothesis, learning, why we hit or missed the goal. Requires judgment. Can't be delegated. Mauro fills this during the Monday call.

The 5 questions (taken from the existing meeting agenda):
1. Learning of the week
2. Did we follow last week's plan?
3. Why we did / didn't hit the goal
4. TEST: Hypothesis & Metrics for this week
5. ACTION: What we will do this week

**Weekly Metrics (Joao/VA fills via Form — 32 fields):**
Every number the agency tracks, organised into sections:
- Call pipeline (the funnel — most important)
- Content output by owner (Lorenzo + Bogdan separately)
- Reach (impressions combined)
- Outreach (cold DMs, lead magnet DMs, cold emails, positive conversations)

**Content Log (Joao fills via Form — 9 fields per post):**
Notable posts only — top performers and clear flops. Not every post. Per post: owner, platform, type, URL, impressions, engagement rate, performance label, one sentence on why it worked or didn't.

---

### 5. Chose the north star metric

**TOTAL SHOWED QUALIFIED CALLS** — the one number everything else feeds into.

Why this one: A booked call that doesn't show is worthless. A call that shows but isn't qualified wastes everyone's time. A qualified call that showed = real pipeline. That's the number.

Dashboard design decision: this number gets the biggest visual treatment on the home page. Everything else is context for it.

---

### 6. Designed the dashboard pages

**Page 1 — Weekly Review (home):**
- Check-in panel: 5 questions for the current week, displayed as cards
- North star: big number, vs prior week, colour coded
- KPI row: Initial Booked, Qualified Booked, Close Rate, Sales
- Quick summary: total posts + total impressions this week

**Page 2 — Metrics:**
- Call funnel chart
- Qualified calls trend over time (with target line)
- Owner output table: Lorenzo vs Bogdan side by side
- Reach chart: X + LI over time
- Outreach row

**Page 3 — Content:**
- Filters: owner, platform, type, performance label, date range
- Grid of post cards

---

### 7. Tech stack decisions

- **Next.js 14 + TypeScript + Tailwind:** standard, fast local dev, handles multiple pages as routes
- **Recharts:** easiest chart API, looks good without heavy config
- **Papa Parse:** best CSV parser for JS, handles edge cases (commas in text, etc.)
- **shadcn/ui:** copy-paste components, no heavy dependency, easy to customise
- **Local fallback:** if Google Sheet URLs aren't set in env vars, reads from local `/data/*.csv` files — makes development possible without a live sheet

---

### 8. Made metrics easy to add/remove

This was a specific requirement: the tracked metrics will change over time. Adding a new platform, dropping something that's no longer relevant.

**How it works:**
1. Add/remove the column in the Google Sheet
2. Add/remove the field in `lib/types.ts`
3. Add/remove from the component that renders it

No other files change. The CSV column name is the contract — the name in the Sheet has to match the name in the types file exactly.

**For the VA:** schema.md has a clear note: "Do not rename existing columns. If Mauro asks you to track something new, add a column and tell Mauro the column name."

---

## Problems we hit

**CLAUDE.md routing table was stale:** Referenced skill files that had been deleted or renamed. Fixed as part of the skill reorganisation — lesson is that the routing table has to be maintained whenever skills change.

**The existing tracker is too messy to migrate:** Made a conscious decision not to try importing historical data from the messy sheet. Start fresh with clean sample data. Historical data can be backfilled later if needed — or just accepted as "pre-dashboard."

**Google Forms adds a Timestamp column:** Auto-added as the first column in response tabs. Not a problem — `fetchData.ts` is built to skip it. But worth knowing so it doesn't confuse anyone looking at the sheet.

---

## What this system assumes

- Joao (VA) fills the form every Monday without being chased
- Mauro fills the check-in tab during the Monday call
- Lorenzo and Bogdan track their own content output (Joao pulls from wherever they log it)
- The tracked metrics stay relatively stable week to week (adding is fine, but frequent renaming breaks things)

---

## Key principles this was built on

1. Clean data contract over live connection to messy operational data
2. One north star metric — everything else is an input to it
3. VA fills numbers, founder fills context and judgment
4. Form-driven input reduces VA errors and format confusion
5. No infrastructure to maintain — just a sheet and a local Next.js app
6. Easy to add/remove metrics without breaking anything else
7. Hypothesis-driven weekly check-in forces you to treat marketing like experiments, not activity

---

## What's next
- Set up the Google Sheet and both Google Forms
- Build the dashboard (Claude Code, following the PLAN.md in groups)
- Wire up the env vars once the Sheet is live
- First real data entry: next Monday (2026-04-27)
