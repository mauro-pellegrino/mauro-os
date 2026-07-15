# Juan's Setup Plan: From Fresh Clone to Running Content Engine

Work through the phases in order. Each project says what it produces, the exact steps, and where Mauro is needed. Everything is done inside a Claude Code session in the mauro-os folder unless stated otherwise. Rule zero: anything unclear, ask Mauro before improvising.

---

## Phase 0: Access and environment (Day 1, ~1 hour)

### Project 0.1: Get into the repo
**Produces:** working local copy of mauro-os on Juan's Mac.
1. Create a GitHub account with your ghostedcalls email (github.com/signup). Send Mauro the username.
2. Accept the collaborator invite from your email.
3. Install GitHub Desktop (desktop.github.com), sign in, File → Clone Repository → `mauro-pellegrino/mauro-os`.
4. Open the Claude desktop app with the team account. Start a session in the cloned mauro-os folder.
5. Approve the project hooks when asked. Confirm the writing style rules load at session start (you'll see a "Loading writing style rules" message).
6. Test the loop: ask Claude "summarize brand/positioning.md in 3 lines". If it answers from the file, everything works.

**Mauro needed for:** sending the GitHub invite, deciding read vs write access.

### Project 0.2: Read the brand (same day)
**Produces:** Juan understands who this content is for.
1. Read `ONBOARDING.md` fully.
2. Read `brand/positioning.md`, `brand/audience.md`, `brand/voice.md`.
3. Write Mauro a 5-line summary in Slack of who the ICP is and what the brand promises. This is the check that the reading happened.

---

## Phase 1: Repo scaffolding (Day 1-2, ~1 hour)

### Project 1.1: Create the missing folders
**Produces:** every folder the skills reference actually exists.
Several skills point at folders marked "create when first used". Create them all now with a short README.md inside each saying what belongs there:
- `brand/social-proof/` (screenshots and numbers of real results, internal only)
- `brand/social-proof/case-studies/`
- `brand/wins-log.md` (start it as an empty log with a date/win/source table header)
- `brand/short-form-batches/`
- `ops/daily/` and `ops/acquisition/` and `ops/weekly/`
- `research/weekly-briefs/` and `research/ideas/`
- `skills/content/linkedin-docs/personalized-decks/agency-owners/`

Commit and push through GitHub Desktop with the message "scaffold folders referenced by skills".

**Mauro needed for:** nothing. Careful: create folders and READMEs only, do not touch files inside `skills/` (edits there auto-publish).

---

## Phase 2: Source material (Week 1, ~3-4 hours)

The whole engine runs on Mauro's real material. Right now the source pool is thin. This phase fills it.

### Project 2.1: Transcript pipeline
**Produces:** every existing Mauro video and key post saved as source material.
1. Get the transcript of Mauro's live YouTube video (ask Claude to fetch it, or copy it from YouTube's transcript panel if fetching fails).
2. Save to `research/transcripts/maurojpelle/` following the format of the file already in that folder (title, URL, fetch date at top).
3. Ask Mauro for links to his best X posts and threads so far (including the $28k deal thread). Save each as a small md file in `brand/posts/` with date and link.

**Mauro needed for:** the list of posts worth saving.

### Project 2.2: Social proof collection
**Produces:** a filled `brand/social-proof/` folder so skills stop running on placeholders.
1. Ask Mauro to export/screenshot: X analytics (impressions, follows, DM volume), the $28k deal evidence, any booked-call data.
2. File everything in `brand/social-proof/` with descriptive names and a one-line note per item on where it came from.
3. Add each item as a row in `brand/wins-log.md`.

**Mauro needed for:** supplying the screenshots and confirming which numbers are cleared for public use (mark each item PUBLIC-OK or INTERNAL).

### Project 2.3: Monitored channels shortlist
**Produces:** the research list that fills the `[MONITORED CHANNELS]` placeholder in the skills.
1. In a Claude session, research creators covering: AI content systems, agency growth, personal-brand-to-pipeline, Claude/AI ops for service businesses. YouTube and X both.
2. Build a table of ~10 candidates: name, channel link, subscriber/follower count, what they cover, why relevant to Mauro's lane, 2 example videos/posts.
3. Send to Mauro to pick 4-6. After he picks, update the table in `skills/research/weekly-research.md` ONLY after Mauro approves the exact edit (skills auto-publish).

**Mauro needed for:** final pick of 4-6 channels, approving the skill edit.

---

## Phase 3: First production runs (Week 2, ongoing)

Everything ships to Mauro for review. Nothing publishes directly.

### Project 3.1: Short-form batch #1
**Produces:** first batch of X post drafts from real source material.
1. Run `skills/content/short-form/bulk-short-form-generator.md` on the saved transcripts and posts from Phase 2.
2. Quality-check against `brand/voice.md` (no em dashes, no "not X but Y", sounds human).
3. Deliver the batch to Mauro in Slack. Log what was sent in `brand/short-form-batches/`.

### Project 3.2: First X article draft
**Produces:** one long-form article draft.
1. Run `skills/content/x-article-creator.md` on the strongest transcript.
2. Deliver in Slack for review. Do not save the article to the repo (hard rule).

### Project 3.3: Agency-inbound deck draft
**Produces:** the master LinkedIn deck the DM system is blocked on.
1. Open `skills/content/linkedin-docs/industry-decks/linkedin-doc-template.html` as the base.
2. With Claude, draft `agency-inbound.html` filling the placeholder sections from `brand/positioning.md` and the approved social proof.
3. Render to PNG per `skills/content/long-form/linkedin-html-doc-guide.md` and send pages to Mauro for copy review. Iterate until approved.

**Mauro needed for:** copy approval, final numbers sign-off.

---

## Phase 4: Operating systems (Week 3+)

### Project 4.1: Notion content system
**Produces:** the scheduling backbone.
1. Build the Notion databases per the schema preserved in `skills/ops/content-loop.md` (Content Calendar, Content Vehicles, Weekly Review, plus a scheduling day-view).
2. Load the approved Phase 3 content into the calendar.
3. Send Mauro the Notion links; after approval, ask Mauro to replace the `[NOTION — not set up]` block in the skill himself or approve your exact edit.

### Project 4.2: Weekly rhythm
**Produces:** the recurring loop running without reminders.
1. Every Monday: pull X analytics, save a dated baseline file in `ops/acquisition/`, and run `skills/ops/monday-acquisition-analysis.md` with Mauro.
2. Every week: run `skills/research/weekly-research.md` against the monitored channels (once defined) and file the brief in `research/weekly-briefs/`.
3. Daily: pull the repo before starting, sync the calendar, flag anything stuck.

---

## Standing rules (apply to every project)
1. Nothing publishes without Mauro's review.
2. Never invent numbers; bracket placeholders and flag.
3. Never name clients in public-facing content.
4. Don't edit `skills/` files without Mauro approving the exact change first.
5. Articles and lead magnets are never saved to the repo.
6. Every deliverable lands in Slack with a one-line note on what it is and what skill produced it.
