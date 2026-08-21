# Content breakdown: the 2026-08-20/21 measurement session

**For:** Juan
**From:** Mauro
**Written:** 2026-08-21
**Source work:** a single working session in the `growthub-os` repo, spanning the evening of 08-20 into 08-21
**Status:** raw material and instructions. Nothing in here is a finished post.

---

## 0. How to use this document

This is a **source file**, not a content calendar. It exists because a lot of usable material got produced in one session and none of it is packaged.

Your job on this document is **extraction and packaging**, per the standing rules in `JUAN-PLAN.md`. Specifically:

- Gather the assets listed in section 6 (screenshots, exports, files).
- Build the scaffolds listed in section 7.
- Do **not** write posts in Mauro's voice from this. That has been tested and it doesn't work. Draft generation runs through the skills, on Mauro's instruction, after he picks an angle from section 5.

**Read section 1 before anything else.** Most of the numbers in this document cannot be published, and getting that wrong is worse than producing nothing.

---

## 1. CLEARANCE — read this first

The session produced three categories of number and they have completely different rules.

| Category | Examples | Can it be published? |
|---|---|---|
| **Growthub's internal financials** | close rate 27.1%, $300k MRR, 118 qualified calls, 32 sales, monthly close rates, AOV targets | **NO. Not without Lorenzo's and Bogdan's explicit sign-off.** This is the agency's confidential performance data. Mauro is an employee reporting on it, not an owner licensed to publish it. |
| **Numbers from a private call** | Blue Sense at 8 figures, A$24-25k average retainer, sub-2% churn, ~40 clients fired, CAC ~$10k, LTGP ~$200k | **NO. Hard no.** These came from a 33-minute private call between Nathan Perdriau, Lorenzo and Bogdan on 2026-08-17. Publishing them would burn a live referral partner for a post. Not a grey area. |
| **Method, process and Mauro's own mistakes** | how to join content output to booked calls, the parsing traps, the correlation approach, the three errors found in his own files | **YES. Publish freely.** This is Mauro's own work product and his own record. It is also the strongest material in the session. |

**The practical consequence:** every publishable angle in section 5 is built on **method and self-correction**, not on Growthub's figures. That is not a limitation — the method is more forwardable than the numbers, because a reader can run it on their own account and a number they can't verify does nothing for them.

**If Mauro does get sign-off** on a redacted version (percentages and ratios, no absolute revenue), section 5 marks which angles get materially stronger. Ask, don't assume.

**One more flag, for Mauro not Juan.** There is a standing rule in the Growthub memory that article subjects must come from the *reader's* ad account, never from our own content analytics. That rule was written for Lorenzo's audience of brand operators. Mauro's own audience is agency owners using AI, where the measurement layer genuinely *is* the subject, and the August objective read recommends publishing exactly that. Those two point in opposite directions here. Worth Mauro deciding explicitly rather than letting it resolve by accident.

---

## 2. What the session actually was

Not a content session. A data session that turned up content as a byproduct.

It started as a question about LinkedIn export data and ended up doing four distinct pieces of work:

1. A six-month correlation study of content output against qualified calls.
2. The recovery of a close-rate figure that had been sitting unread in the repo for seven weeks.
3. A full read of a competitor/peer call transcript that corrected two earlier conclusions.
4. A written action list, and three corrections to existing repo files.

Roughly five hours. Four new or rewritten documents, three corrected files, one transcript saved that should have been saved four days earlier.

---

## 3. Complete work log

### 3.1 The six-month study

**Question:** does content output actually move qualified calls, over a window long enough to mean something?

**Inputs joined:**
- The sales team's own weekly call log (qualification verdict, not our intake guess)
- Lorenzo's Calendly export, 364 bookings, to recover the date each lead *booked* rather than the date the call ran
- Two overlapping X analytics exports, deduplicated by post ID
- Three weeks of the newer content tracker

**Method notes worth keeping:**
- Bucketed by the week the lead **booked**, not the week the call happened. Those are different weeks and using the wrong one smears the signal.
- Filtered X rows by impressions to drop replies, which otherwise trip the post count by 3-4x.
- Deduplicated across two exports by post ID, because they overlap.
- Ran same-week and one-week-lagged correlations, because a lag effect is the obvious objection.

**What came out:**

Across the 20 weeks where both series exist:

| relationship | result |
|---|---|
| posts → qualified calls, same week | **essentially zero** |
| impressions → qualified calls, same week | **moderate and real** |
| either, lagged one week | nothing, slightly negative |

At 20 data points the significance threshold is around 0.44. Reach clears it. Post count is indistinguishable from zero.

**The two weeks that make the point better than the statistics:** one week posted 84 times and produced 3 qualified calls. Another posted 15 times and produced 6, the joint best week in the whole series. The three highest-volume weeks in six months produced 3, 4 and 2.

**The recent three weeks repeated it live:** posts nearly doubled, impressions rose by a third, and floor-qualified calls halved. The added volume went almost entirely into the lowest-reach format available.

### 3.2 The close-rate recovery

This one is the best story in the session and Mauro found it, not the model.

The repo's own README described a file as *"mostly agenda/targets scaffolding; reference only."* Mauro said, roughly, *we also have closed if you go way down to the weekly targets sheet.* He was right. The file held the leadership scorecard: 83 weekly columns, target-and-actual pairs for qualified calls, sales, close rate and average order value.

**The number had been in the repo since June 30 and the README told everyone not to look.** Seven weeks. And a project map written on 2026-08-13 opened by declaring close rate one of two numbers missing before the plan could be arithmetic instead of an argument.

**The trap that nearly broke it.** The sheet's column headers are inconsistent — some in US month/day, some in day/month, none carrying a year. Read naively, the close-rate figures land in 2026. They are actually 2025. The fix was to ignore the labels entirely, anchor the **last** column to a known week, and walk backwards one week per column. Verified two independent ways: one metric that only exists in 2026 appears in the final five columns, another in the final thirteen.

Getting that wrong would have produced a confident, precise, entirely false answer. That is the interesting part.

**Also recovered:** the average-order-value row has **three non-zero entries in its entire history**, the most recent from April 2025, against a target that hasn't changed since February 2025. Sixteen months of an empty row that everyone downstream was blocked on.

### 3.3 The transcript sweep

A 33-minute peer call had been analysed once from a summary. Reading it in full corrected two things:

**Correction one, and it was mine.** A competitor file said the subject had "no own channel" and shouldn't be added to YouTube monitoring. He has had a channel for three years. It's in the transcript, in plain language, and I'd written the opposite. Mauro caught it by asking a simple question.

**Correction two.** An earlier version of the same file called him a competitor. He isn't. He briefs creative and doesn't produce it, which makes Growthub a supplier rather than a rival, and a referral was agreed on the call.

**Also found:** the transcript had never been saved. The folder for it existed and was empty. Four days of it living only in a chat window. It's saved now.

### 3.4 Corrections shipped to the repo

Four files corrected, three of them because something in them was wrong:

- A competitor file, on the "no channel" claim.
- A dataset README, on the file it told people to ignore.
- A monitored-channels list, replacing a wrong row and adding two channels.
- A project map, updated with the recovered figure and what it changes.

---

## 4. The three errors, written down

This section exists because it is the most publishable material in the session and because the pattern matters more than the individual mistakes.

**Error 1: stated a fact that contradicted a source I had already read.** Wrote "no own channel" about someone whose channel is discussed in a transcript I'd summarised. Cause: I summarised the transcript, then worked from my summary instead of the transcript. The summary was lossy and I stopped checking.

**Error 2: trusted a label over the contents.** A README said "reference only" and so nobody opened the file for seven weeks. The label was written once, in good faith, by someone who hadn't looked hard enough, and then it did the work of a fact.

**Error 3: nearly published a precise wrong answer.** The date columns would have put 2025's close rate in 2026. Nothing about the output would have looked broken. It would have been clean, specific, and off by a year.

**What links all three:** none was a computation error. All three were *provenance* errors — working from a summary, from a label, from a header, instead of the underlying thing. The arithmetic was never the risk.

---

## 5. Content angles

Per Mauro's standing preference, four distinct angles rather than one. All four are built on method and self-correction only, so all four are clear to publish as-is.

Titles are drafts, not final.

### Angle A — "I Was Wrong" (recommended)

**Why this one:** the August objective read named "I Was Wrong" as the highest-ceiling series available to Mauro, said five episodes already existed, and called it the anti-guru posture the audience is starving for. This session produced a sixth, with three errors in it, all documented in files with timestamps.

**The substance:** section 4. All three errors were provenance errors, not reasoning errors. The AI didn't compute anything wrong. It worked from a summary, a label and a header, and was confidently wrong three times.

**Why it lands with agency owners using AI:** this is the actual failure mode of AI-assisted work, and nobody publishing in the space describes it. The genre is "here's my prompt." This is "here's how my system produced a clean wrong answer and how I caught it."

Title drafts:
- "Claude was confidently wrong three times yesterday. None of them were reasoning errors."
- "The three ways my AI setup lies to me"
- "I trusted a README for seven weeks"

**Clearance:** fully clear. These are Mauro's own files and his own mistakes.

### Angle B — the method, handed over whole

**Why this one:** "Steal My Skill" was the second-ranked series in the objective read — very high trust, immediately forwardable, and it counters "AI content looks generic" because the corrections are the proof of taste.

**The substance:** the actual procedure for joining content output to booked revenue. Bucket by booking date not call date. Filter replies out of the analytics export or your post count triples. Deduplicate across overlapping exports by post ID. Run the lag as well as the same week. Anchor ambiguous date columns to a known end and walk backwards. State the coverage holes instead of averaging over them.

**Why it lands:** every agency owner has these exports and none of them has joined them. It's a genuinely hard piece of work described in enough detail to run.

Title drafts:
- "How to prove your content is driving revenue (the boring version that actually works)"
- "Your analytics export is lying about how much you post"
- "The join nobody does: content output to booked calls"

**Clearance:** fully clear. Method only.

### Angle C — rolling exports lose history permanently

**Why this one:** it's small, specific, immediately actionable, and it cost real data in this session.

**The substance:** X's analytics export is a rolling window. Two exports on file, overlapping, and together they still have no rows at all for December and January. That history is gone and cannot be re-pulled. One of those missing months was the second-best month in the entire series for qualified calls, so the best month in the dataset has no output data behind it.

**Why it lands:** it's a five-minute fix (export monthly, commit it) against a loss that's already permanent for anyone who hasn't been doing it. This is a service-to-the-reader post rather than a clever one.

Title drafts:
- "Two of my best months have no data behind them and I can't get it back"
- "Export your analytics monthly. I learned this too late."

**Clearance:** fully clear, as long as absolute figures stay out.

### Angle D — volume's real purpose is the ability to refuse

**Why this one:** it's the most contrarian idea in the session and the most likely to travel.

**The substance:** everyone chases lead volume to book more calls. The stronger use of volume is to get selective — enough inbound that you can turn down anyone who isn't a fit, which raises close rate and price without changing anything about the pitch. And the corollary: volume added before your qualification gate works is not neutral, it's actively harmful, because a bad-fit client churns and churn costs more than the call did.

**Handle with care.** The sharpest version of this argument came from a private call and **that version cannot be used.** The idea is publishable as Mauro's own reasoning about his own funnel. The peer's phrasing, numbers and identity are not. If the post needs the quote to work, kill the post.

Title drafts:
- "More leads won't fix a funnel that can't say no"
- "The point of a full pipeline isn't more calls"

**Clearance:** the idea yes, the sourcing no. Read the caution above twice.

### If Mauro gets redaction sign-off

Angles A, B and C do not improve much — they're method pieces and they stand alone.

Angle B gets a stronger opener with one ratio in it. And a fifth angle opens up that is currently blocked: the correlation result itself, published as percentages and relative figures with no absolute revenue. That would be the strongest differentiation available, because the objective read notes nobody in this space publishes a measured loop. It needs Lorenzo's explicit yes.

---

## 6. Assets to gather

Juan, this is your list. Everything here is collection, not creation.

| # | Asset | Where from | Notes |
|---|---|---|---|
| 1 | X analytics export, current month | Mauro's X analytics | **Do this first, it's time-sensitive.** The window is rolling and history dies. Save to `research/` with the date range in the filename. |
| 2 | A monthly export reminder | Calendar or Notion | Recurring, first of the month, both accounts. The point of asset 1 is that it never gets forgotten again. |
| 3 | Screenshot of the ambiguous date headers | The weekly targets sheet, `growthub-os/research/q1-q2-content-vs-calls/raw-data/` | This is the visual for Angle A error 3. Show mixed formats with no year. Ask Mauro before opening the file — it has Growthub financials in it, so **crop to headers only, no data rows.** |
| 4 | Screenshot of the README line | Same repo, git history | The `"reference only"` line as it was written. Visual for Angle A error 2. |
| 5 | Terminal screenshot of the correlation output | Ask Mauro to re-run and screenshot | Visual for Angle B. **Crop or blur any absolute figures** — the r-values are the point. |
| 6 | The four session documents | `growthub-os` | Read-only, for context. Do not copy Growthub financials into `mauro-os`. Paths in section 8. |

**Hard rule on assets 3, 5 and 6:** Growthub's financial figures do not get copied into this repo. This repo is Mauro's personal brand and it is a publishing surface. Keep the wall.

---

## 7. Scaffolds to build

| # | Task | Produces |
|---|---|---|
| 1 | Create `brand/i-was-wrong/` with a README | The home for the series. One file per episode: date, the wrong belief, the correction, the cost, the generalizable lesson. Seed it with the three from section 4. |
| 2 | Add the three errors to `brand/wins-log.md` | They aren't wins, but the log is the source pool. Mark them clearly as corrections. If the log's table doesn't support that, propose a column and ask Mauro. |
| 3 | Draft the method steps from 3.1 as a numbered procedure | Raw skeleton for Angle B. **Procedure only, no numbers.** Not a post — Mauro or a skill writes the post. |
| 4 | Check whether an existing skill covers the output-to-calls join | If nothing does, that's a gap worth naming. Report, don't create — skill files auto-publish. |

---

## 8. Reference paths

All in `growthub-os`, which is a separate repo from this one:

- `research/content-tracker/six-month-output-vs-qualified-calls-2026-08-20.md`
- `research/q1-q2-content-vs-calls/close-rate-and-acv-from-weekly-targets-2026-08-20.md`
- `research/competitors/nathanperdriau-bluesense.md`
- `research/transcripts/nathanperdriau/2026-08-17-bogdan-lorenzo-call.md` — **contains private call content, internal only**
- `ops/mauro-action-points-2026-08-21.md`
- `ops/mauro-objective-read-2026-08-03.md` — the source of the series recommendations in section 5

---

## 9. Open for Mauro

1. **Redaction sign-off from Lorenzo?** Gates the fifth angle entirely and improves Angle B. One conversation.
2. **Which angle ships first?** A is recommended. Nothing in section 5 is written until this is picked.
3. **The rule conflict in section 1** — reader's-account subjects versus publishing the measurement layer. Needs an explicit call.
4. **Does Juan get read access to `growthub-os`?** Section 6 asks him to read files there. Currently unresolved, and if the answer is no then assets 3 to 6 come from Mauro directly.
5. **Angle D without the peer's framing** — is the idea strong enough standing on Mauro's own funnel? Worth a look before it gets drafted.

---

## 10. The uncomfortable note

Worth writing down because it's the actual pattern.

This session produced four documents of analysis for Growthub and **zero published content for Mauro's own brand.** The material for several strong posts is in section 5 and none of it is written.

The August objective read named this exactly: 166 commits of system work against one saved post, one lead magnet, one video. It also named the fix, which is not another plan — it's a rule that runs before the choosing starts. No system work in the personal hours until that week's posts are out.

Today was system work. Good system work, and it found a number that had been missing from a project map for a week. It still wasn't a post.
