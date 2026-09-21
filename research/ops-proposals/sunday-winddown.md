# Sunday wind-down: proposal + the week review that prompted it

> **STATUS: NOT ADOPTED.** Proposed in the session of 2026-09-06. Mauro asked for a Sunday
> wind-down so Monday starts decided, then parked the decision. Nothing here enters `skills/`
> until he answers the open questions at the bottom. Saved so the work is not re-derived.

---

## Part 1: what Juan did, week of Mon 31 Aug to Fri 4 Sep 2026

Read from git. Juan commits as `jlago-del`. 18 commits in the window, last one Friday 13:54,
nothing Saturday or Sunday.

**Reply engine**
- Quote-tweet rules added to `skills/content/x-reply-assistant.md` (v1.3), plus the matching
  changes in `x-reply-mobile-prompt.md`.
- OPTIONAL kept in the quote-tweet verdicts (`8ba9159`).
- A quote bank added to the reply assistant (`6cd35ab`).
- The portable mobile prompt rewritten as v2 with full session behaviour (`dd38226`).
- New `skills/content/x-replies-prompt.md`.

**Outlier X article corpus** (started from zero this week)
- `research/outlier-x-articles/` created with README and process spec (`4108f0f`).
- Capture 01: SaaSpocalypse, @denk_tweets.
- Capture 02: the 170K AI consulting retainer, @coreyganim.
- `cover-prompt-library.md` created, then covers 03 (@knoxtwts), 04 (@Ecombos_Ai) and
  05 (@Aidanb2b) written up as reusable image prompts.

**Visual**
- Two article infographics for the pipeline-layers piece, in `content/boards/`
  (`7fb6ced`, `aac9a81`).

**Voice and source material**
- `brand/voice.md` edits, Type 4 closer rules refined (`3e1f501`).
- X algo myth-buster thread finalised.
- `research/transcripts/maurojpelle/maurojpelle-raw-tweets.md` collection started.
- Jacob C. Edmunds transcript saved (`e703b14`).

### Two observations to carry into the planning

1. **None of Juan's week touched Tier 1.** `BACKLOG.md` names the single objective as a YouTube
   engine that runs without Mauro as the bottleneck. Juan's whole week was X-side. Both ends of
   the YouTube flow, research and board creation, are still on Mauro. That is an allocation
   decision to make deliberately, not a fault in his output.
2. **The corpus cannot be read for reach yet.** 5 captures against a target of ~50, and 4 of the
   5 rows have no link and no view count, so selection is currently on craft rather than measured
   performance. One pass of links and views fixes all four rows.

---

## Part 2: the proposal

**Verdict on the idea: worth doing, and there is precedent in this repo.**
`research/wiz-of-ecom/synthesis.md` item 12 describes the same shape: a control panel filled
Friday, then Sunday one person reads it and sets the next seven days of tasks and vehicles. That
material is the consultant's and stays internal per the attribution rules in that file. The shape
is what transfers, none of his numbers and nothing about his architecture.

**The trap to avoid:** building a second review. `skills/ops/monday-acquisition-analysis.md`
already reads last week's numbers, and `skills/ops/daily-ops.md` already spreads action items
across the week. A Sunday session that re-reads metrics duplicates Monday and gets abandoned in
two days, the same way `recaps/` was.

**The split that keeps them distinct**

| | Monday acquisition analysis | Sunday wind-down (proposed) |
|---|---|---|
| Question | How did acquisition perform, what do I act on | What am I doing Monday, and what is Juan doing |
| Input | X analytics, booking data, call notes | git log, `BACKLOG.md`, last week's commitments |
| Output | The dated analysis in `ops/acquisition/` | Blocked column cleared, Monday's big rock named, Juan's queue set |
| Length | Full read | 20 to 30 minutes, not 3 to 4 hours |

**The job the wind-down actually does: clear the blocked column.** As of 2026-09-06, three
`BACKLOG.md` items are `[?] blocked on Mauro` and nothing downstream in Tier 1 moves until they
are answered:

1. The ~10 titles drafted off the Charlie Morgan patterns were never signed off.
2. VIDEO 1's script ends on a DM keyword CTA and the asset it promises does not exist. Per the
   operating rules in `CLAUDE.md`, that blocks the video shipping.
3. No video has been recorded off a board, so the Tier 1 flow is unproven end to end.

A weekly ritual whose one measurable job is to empty that column would pay for itself on the
first run.

---

## Part 3: open questions, Mauro to answer

These were put to him on 2026-09-06 and left unanswered. They are the inputs the skill needs.

1. **Next week's one big rock.** Record a video off a board (proves Tier 1 end to end, needs the
   board verdict first) / sign off the 10 titles (unblocks the research end) / build the DM asset
   for VIDEO 1 / hold X cadence and park YouTube another week deliberately.
2. **Juan's lane.** Pull him onto YouTube (board building, scripts, research end) / keep him on X
   (corpus, covers, replies) / split the week between both / fix the corpus data first (links and
   views on all five captures).
3. **What actually publishes next week.** Daily X posts from the raw-tweets collection / the
   pipeline-layers X article, which already has its infographics built and waiting / replies only /
   a YouTube video.
4. **Where the output lands.** Written into `BACKLOG.md` (one file, survives session clears, the
   statusline already counts it) / `BACKLOG.md` plus a short dated Monday brief naming the big rock
   and Juan's queue / chat only, nothing saved / write `skills/ops/sunday-winddown.md` first so it
   runs the same way every week.

Once 4 is answered the skill can be written. Questions 1 to 3 are the first run of it.
