# Subjects, with the evidence already attached

Each subject names the reader's problem first, then the evidence that proves it. Evidence is real
and sourced. Nothing here is a topic about Mauro's analytics.

**Status key:** `ready` means every piece of evidence is in a repo Juan can read. `blocked` means
some of it sits in `~/growthub-os/`, which Juan does not have.

---

## S-01 · Your agency already recorded every article you will publish this year · `ready`

**Their problem:** they have nothing to say and no time to write, while sitting on hundreds of
hours of recorded calls.

**Evidence**
- Sales calls: an agency runs several a week, and on each one someone explains the whole
  methodology out loud to a stranger, in plain language. That is the clearest version of their
  offer that exists, and it is deleted.
- Onboarding calls hold "what have you tried", which is the competitor landscape in the buyer's
  own words.
- Internal training calls hold the IP being taught, unpolished, which reads as more credible.
- Frequency across transcripts is demand evidence. Five clients asking the same question is a
  proven subject.
- Voice: a transcript is how the person actually talks, and it is the only reliable fix for
  AI-sounding output. Most of Mauro's clients are non-native English speakers, so AI writing is
  obvious on them immediately. `brand/voice.md`, "the non-native-speaker angle".
- Mauro's own method: 10 to 15 minutes of talking becomes a voice file. His highest-performing raw
  post is this exact workflow. `research/transcripts/maurojpelle/maurojpelle-raw-tweets.md`.

**The likely title noun:** transcripts, or call recordings. Concrete and recognisable.

## S-02 · The rule that broke your content system was never written down · `ready`

**Their problem:** they fix the same mistake every month and it never stays fixed, because the fix
lives in someone's head.

**Evidence**
- `skills/content/gate-playbook.md`, seven entries, each one a real rejection from a single
  session on 2026-09-11, with the counters.
- The failure that produced it: a writing-rules file existed and was skipped, because the request
  looked small. Three rounds of rejected drafts followed.
- The mechanism: a rule a human has to remember is a rule that fails under time pressure.
- `skills/content/anti-slop-protocol.md` is the static version. The playbook is the version that
  learns.

**Note:** this subject is about their process, not about Mauro's tooling. Keep the repo out of the
first screen.

## S-03 · Your review step is the ceiling on your output · `ready`

**Their problem:** they hired or automated production, and everything still waits on them.

**Evidence**
- mauro-os holds roughly 80 skill files and 4 agents feeding one reviewer.
- The fix built on 2026-09-11: a review agent running four separate passes, on a different model
  than the writer, so only work that passes reaches the human. `.claude/agents/gate.md`.
- Why four passes and not one: a single blended review misses a category every time.
- Why a different model: a writer checking its own work agrees with itself for the same reasons it
  made the mistake.
- **The honest limit, which belongs in the article:** it is unproven. Nothing forces the agent to
  run. That admission is worth more than the build.

## S-04 · A calendar block has no done-state · `ready`

**Their problem:** they plan the week, the week happens, and they cannot say what actually got
finished.

**Evidence**
- Mauro's daily system is on its third version. Version two inferred what was done from Notion,
  Slack and call transcripts, and got it wrong for two months.
- The cause: a thing being on a calendar tells you nothing about whether it happened.
- Version three: the plan comes from a backlog file, capped at three items a day, and the tick
  comes from Google Tasks, which has a completed state.
- Exports run morning and afternoon, tasks are created at 08:00, completions written back at 17:00.
- Source: the published article, 2026-09-10, and `brand/claims.md`.

## S-05 · You cannot prove which post produced the call, and here is what to measure instead · `ready`

**Their problem:** they post, calls arrive, and they have no idea which is causing which.

**Evidence**
- The attribution limit, stated honestly: 649 of 678 Calendly rows sit under one owner and the
  UTM field is empty on 673 of them. You cannot cleanly attribute a booking to a channel with data
  like that. Published 2026-09-10.
- What works instead: a unique reply keyword per piece, an auto-DM that delivers, and a keyword
  ledger. DM volume per keyword is the only directly attributable number in the chain.
- The second-best measure: count bookings on the publish date and the two days after, against the
  baseline daily rate for that month. Day-level correlation, stated as correlation.
- **The uncomfortable finding that makes this article:** reach and booked calls are independent.
  Spearman +0.16 across twelve articles. **That measurement is `@lorenzo_pravata`'s account, a
  different ICP.** It must be labelled as a hypothesis here, never as proven for this audience.

## S-06 · The section you think converts probably does not · `ready`

**Their problem:** they build content around a section that feels obviously right and never test it.

**Evidence**
- A skill asserted the worked example was the section that converts. Measured, the worked example
  did 60,000 against the winning section's 264,000. The exact opposite.
- Why it survived so long: it felt true, and nothing tagged the claim so nothing forced a check.
- The fix: every claim carries an evidence tag, so it can be found and re-tested later.
- Source: the published article, 2026-09-10.

## S-07 · Nobody noticed for two months · `ready`

**Their problem:** they have no standing alarm on the numbers that matter, so drops are found late.

**Evidence**
- Monthly impressions fell 64% between June and August 2026 and it went unnoticed for two months.
- By the time it was caught manually, the damage was priced in.
- The fix: something checks the trend on a schedule and shouts, rather than a human remembering
  to look.
- The design rule that follows: the agent is defensive. It catches, it does not reach out.
- Source: the published article, 2026-09-10.

## S-08 · Split your system by activity, never by client · `blocked`

**Their problem:** they build a folder per client, the client leaves, and the work rots with them.

**Evidence**
- 73 skill files across eight activity folders, none split by client. Published 2026-09-10.
- The mechanism: an activity survives every client. "Turn a transcript into an article" is the
  same job for one account or five, so it lives once and improves every time anyone touches it.
- **Blocked part:** the strongest supporting detail is the `MAP.md` story in `~/growthub-os/`,
  where an agent rebuilt an SOP that already existed and 45 minutes was deleted. Juan cannot read
  that file. Mauro can paste the passage, or the subject runs without it.

---

## The blocker on step 3

The seven article files are at `~/growthub-os/skills/content/x-articles/`. Juan has `mauro-os`
only, so he cannot run them.

`skills/content/x-articles-POINTER.md` forbids forking them, and the reason is real: two copies of
`x-article-creator.md` already exist in the two repos and have drifted apart with nothing syncing
them.

Three options, for Mauro to pick:

1. **Snapshot with a sync script.** Copy the seven files into `mauro-os` under a header saying they
   are a read-only snapshot, never edited here, re-synced before each batch. Keeps Juan working.
   Drift is bounded by the script, not by discipline.
2. **Juan stops at the input document.** He does steps 1 and 2 and hands off. No drift, and Mauro
   stays in the loop on every article.
3. **Give Juan access to growthub-os.** Fastest, and it puts agency and client material in front
   of someone onboarded only onto the personal brand. Not recommended.

Recommendation is 1, with the sync script, because option 2 puts the bottleneck back on Mauro,
which is the exact problem S-03 is about.
