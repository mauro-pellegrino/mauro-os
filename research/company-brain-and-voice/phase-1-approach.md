# Company brain and voice: phase 1 for Mauro's lane

**Status: NOT ADOPTED.** A proposed approach, 2026-09-30. Nothing here creates a voice file, a
skill or a brain folder. Mauro signs off first.

**Source of the method.** The full analysis sits in the Growthub repo at
`growthub-os/research/company-brain-and-voice/synthesis.md`: 18 videos on company brains and voice
files, each practice ranked against booked calls, with an adopt/adapt/reject table. This file takes
the method only. It copies no client names, no client numbers and no Growthub transcripts.

**The lane it serves.** Established agency owners who need inbound. Mauro shows them how to turn
their real work into booked calls with an AI content engine (`CLAUDE.md` §1 and §2). So the brain
and the voice are judged by one number: calls booked from Mauro's content.

---

## What the synthesis found, in the form that matters here

1. **The videos teach output quality. The operators who book calls work on topic choice and on a
   call-scored loop.** 0 of 18 videos score a post on calls. Paolo says ideas are about 90% of it.
   Wiz tracks which topics produced inbound DMs and conversations. Both playbooks are in this repo:
   `research/paolo-trivellato/linkedin-playbook-2026-09-24.md`, `research/wiz-of-ecom/synthesis.md`.
2. **Voice is a gate, and it has to be extracted from unedited recordings.** 9 of 18 videos agree,
   and spoken sources rank above published ones.
3. **The brain is a ranked topic map fed by recordings, scored on bookings.** The wiki structure
   (raw, compiled cards, one index) only matters because it makes that ranking possible.

This is also the lane's own content. Mauro building it in public is phase 1 of the proof.

---

## Phase 1 contents

### 1. The sources he already has

| Tier | Source | Path | Size |
|---|---|---|---|
| Spoken, unscripted | Voice interview, skills to agents (Q1 to Q8) | `research/transcripts/maurojpelle/2026-08-06-voice-interview-skills-to-agents.md` | 1,751 words |
| Spoken, unscripted | Voice memos and walkthroughs: AI content that does not sound like AI, lead magnets with Claude, installing agents, moving the engine to agents, skills vs agents structure, YouTube-first system | same folder, 6 files | 6,571 words |
| Spoken, unscripted | Working session with Juan, article workflow and the patience belief | `2026-09-21-article-workflow-and-patience-belief.md` | 3,219 words, **in Spanish** |
| Spoken, screen | Loom, saving outlier X articles | `2026-08-28-how-to-save-outlier-x-articles-loom.md` | 1,403 words |
| Typed, published | Raw tweets and the myth-buster thread | `maurojpelle-raw-tweets.md`, `2026-09-04-x-source-code-myth-buster-thread.md` | 968 words |
| Typed, unguarded | His worklog prompts and Slack messages, per `skills/research/voice-extraction.md` | lives in the Growthub repo | see the rule below |
| Outcome | X analytics | `research/x-analytics/maurojpelle-2026-05-25-to-2026-08-22.csv` | ends 2026-08-22 |
| Outcome | Calls booked from his content | `[NEEDS: where @maurojpelle bookings are logged]` | none on disk |

**Rule for the typed corpus.** The worklogs sit in the Growthub repo and mention clients. Phase 1
takes counts only (word frequencies, hedges, punctuation) and copies no text across.

### 2. A first voice build from `research/transcripts/maurojpelle/`

The skill for this already exists: `skills/research/voice-extraction.md` (2026-08-06). Its output,
`brand/voice-mauro.md`, was never written. `brand/voice.md` is still the fork of the agency file.
Phase 1 runs that skill, adding the synthesis method at these points:

1. **English and Spanish apart.** Extract the 3,219-word Spanish session separately. Keep its
   reasoning moves and drop its phrasing.
2. **Count before describing.** Use a phrase counter with a threshold of 3 different recordings.
   The corpus holds 9 spoken files, so 3 is where a phrase stops being a one-off.
3. **Extract with a forensic prompt.** Name specific dimensions and no adjectives. Every rule cites
   the line that proves it. Read for the six things: repeated phrases, analogies, how he disagrees,
   what he never says, rhythm, and the concession move.
4. **Two registers.** Keep a spoken fingerprint from the memos and a written fingerprint from the
   tweets and the typed corpus. Posts use the written register and keep the spoken phrases.
5. **Test it.** Run 3 prompts with the file and 3 without. Mauro picks blind.
6. **Iterate from edits.** Every correction becomes a before/after pair and a line in the file.

**Gap to close before the build.** Q9 to Q11 of the interview were never recorded. Two or three
more 20-minute voice notes on topics he knows cold would give the corpus its breadth.

### 3. The brain skeleton

```
research/company-brain/            PROPOSED, NOT CREATED
  README.md          layers, source tiers, what never goes public
  index.md           one line per topic card, ranked by bookings on post days
  sources.md         every raw folder by path, tier, access state
  log.md             per week: what came in, what changed, what booked
  wiki/
    topics/<slug>.md       claim · receipts (path + timestamp) · times heard · posts · bookings
    objections/<slug>.md   what agency owners push back on, verbatim, and the answer that worked
    beliefs/<slug>.md      the 15 beliefs in CLAUDE.md §3, each with its receipts
  outcomes/
    YYYY-Www.md            per post: card · platform · profile visits · calls booked that day

brand/voice-mauro.md                PROPOSED, output of skills/research/voice-extraction.md
brand/body-of-work.md               PROPOSED: one-line thesis + 7-12 concepts, from the beliefs

raw layer (unchanged): research/transcripts/maurojpelle/, brand/sessions/, research/x-analytics/
```

**Weekly refresh, one pass.** Pull the new recordings. Update the cards. Score last week's posts
on calls booked that day and profile visits. Re-rank `index.md`. The top of the index sets the week.

**Sources to add as phase 1 matures.** Recordings of his own sales and discovery calls with agency
owners. These are the highest-fidelity source for both voice and objections. None are on disk yet.

---

## Out of phase 1

- Visual identity, Obsidian, scheduled nightly jobs, and claude.ai Styles. The synthesis rejects
  each one for the call goal.
- Any public number. `CLAUDE.md` §1 requires Mauro's sign-off before one ships.
