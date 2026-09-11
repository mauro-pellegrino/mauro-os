# Gate playbook

What Mauro has actually rejected, as checkable entries. The Gate loads this on every run and
applies it alongside `brand/voice.md`.

**Why this file exists.** The rules files say what good looks like in general. This one records
what went wrong in a specific draft, so the same mistake stops being regenerated every session.
Before it existed, a rejection was a message in a chat that no later session could see.

## Format rules

Entries are **appended or amended, never bulk rewritten.** A file rewritten each time loses the
strange, specific, earned line, which is the most valuable thing in it.

- Entries are conditional. `WHEN x THEN y` can be checked. "Write better hooks" cannot.
- Every entry carries hits and misses, updated by the Gate on each run.
- Confidence is a field. New entries start `low`, earn `high`, and only `high` is a hard constraint.
- Entries expire. `low` with no hits in 30 days gets pruned.
- At most 3 new entries per session. This is curation, not brainstorming.
- Nothing gets added without evidence from a real draft. An invented lesson is worse than no
  lesson, because it is confidently wrong at scale.

---

[G-001] 2026-09-11  confidence: high  hits: 3  misses: 0
WHEN drafting a raw X post or quote tweet
THEN the last line must be a flat jab, a bullet, or a flat confidence statement, never a lesson,
     a summary, or a "that's the difference between X and Y" closer
EVIDENCE three QT sets rejected in one session, every closer taught something

[G-002] 2026-09-11  confidence: high  hits: 2  misses: 0
WHEN a short declarative sentence restates or labels the point just made
THEN fold it into the surrounding sentence with commas, even if the result runs on
EVIDENCE "One. Two reads as carelessness." rejected; voice.md folding rule, 2026-08-20

[G-003] 2026-09-11  confidence: high  hits: 2  misses: 0
WHEN naming a product or platform in Mauro's copy
THEN lowercase it: claude code, codex, grok, x, linkedin, miro, notion, yt
EVIDENCE capitalised product names in two rejected QT sets

[G-004] 2026-09-11  confidence: high  hits: 1  misses: 0
WHEN any copy is requested, however small, including a single tweet
THEN read `brand/voice.md` and `skills/content/anti-slop-protocol.md` in full before drafting
EVIDENCE a QT request was treated as a small ask, voice.md was never loaded, and three rounds of
     rejection followed before the files were read

[G-005] 2026-09-11  confidence: high  hits: 3  misses: 0
WHEN a closer reads as quotable, aphoristic or designed to be screenshotted
THEN cut it, Mauro's real posts land flat and plain
EVIDENCE "Uniform polish is itself the tell" and "the loudest ai signal there is", both rejected
     as reading like AI

[G-006] 2026-09-11  confidence: high  hits: 1  misses: 0
WHEN a draft includes a personal reason, origin story or motivation for something Mauro built
THEN it must trace to something he actually said, never be constructed to fill the beat
EVIDENCE "I was fixing the same 5 things by hand on every draft" was written to complete a
     Type 3 post structure and had no source

[G-007] 2026-09-11  confidence: medium  hits: 1  misses: 0
WHEN modelling a raw tweet
THEN model it on `research/transcripts/maurojpelle/maurojpelle-raw-tweets.md`, not on the tweet
     types described in prose, the exemplars are looser and plainer than the description implies
EVIDENCE drafts written from the voice.md description alone still read as AI; drafts written
     after reading the exemplar file were accepted as closer

---

## How entries get added

The Gate proposes deltas after a run. Mauro's overrides are the highest-signal source: every time
he passes something the Gate flagged, or kills something the Gate passed, that disagreement is his
taste being made explicit and it becomes an entry.

Allowed operations, and only these:

```
ADD [new-id] WHEN ... THEN ... EVIDENCE ...
HIT [id]      this entry applied and helped
MISS [id]     this entry applied and was wrong here
AMEND [id]    narrow or widen the condition, keep the id
PRUNE [id]    justify with the counters
```

If nothing was learned in a run, output nothing. That is a valid result.
