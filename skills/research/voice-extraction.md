# Skill: Voice Extraction (derive a real voice doc from how Mauro actually talks)

**Version:** 1.0
**Created:** 2026-08-06
**Owner:** Mauro
**Output:** `brand/voice-mauro.md`, a voice doc built from counted observation of Mauro's own corpus, replacing the Growthub fork currently sitting at `brand/voice.md`.
**Run:** once properly, then re-run quarterly or whenever the voice drifts.

---

## Why this exists

`brand/voice.md` is a fork of `growthub-os/brands/growthub/voice.md`. Diffed 2026-08-05: **124 of 360 lines differ, and almost all of those are swapped examples.** Structure, principles, rhythm patterns and signature moves are Lorenzo's. The examples were changed, the mechanics were not.

The proof it is not Mauro's voice, found in one script run:

> `brand/voice.md` line 76 bans hedging. Across 491 of Mauro's own verbatim prompts he uses "maybe" 21 times, "idk" 8, "feel like" 6, "kinda" 3. **His own voice doc forbids the thing he does most.**

A voice doc written from adjectives ("confident", "direct", "no fluff") will always drift toward generic, because those words describe every operator's voice doc ever written. This skill only allows rules backed by counted evidence from a real corpus.

---

## The three corpora, and why you need all three

| Corpus | Where | What it gives | What it cannot give |
|---|---|---|---|
| **Typed, unguarded** | `growthub-os/ops/daily/*worklog*.md` (543 prompts, ~8,300 words) + Slack `from:me` | Vocabulary, bluntness, punctuation habits, hedging, courtesy markers, verdict words | Anything long-form. Every entry is a short imperative command |
| **Spoken, at length** | A recorded interview, see Step 1. Also `research/transcripts/maurojpelle/` and any tl;dv call where Mauro talks | How he explains, reasons, builds an argument over minutes. **This is the register articles and long forms need** | Typing habits, since speech has no punctuation |
| **Published, the control** | `brand/posts/`, live X and LinkedIn posts | What currently ships | Nothing about how he actually sounds. This is the performance, not the person |

**The gap between corpus 1/2 and corpus 3 is the entire finding.** That gap is what the current doc sands off.

---

## Step 1: Record the long-form corpus

The typed corpus already exists and needs no work. The spoken one does not exist yet and is the binding constraint.

**Source questions:** Juan (VA) supplies an interview set. The 2026-08-05 set was 11 questions on the skills-to-agents transition. Any set works as long as the questions are about things Mauro knows cold, because unfamiliar topics make people perform.

**How to record:**

- One sitting, voice memo, 30 to 40 minutes. No script, no notes.
- **Rule: you are explaining it to Lorenzo or Bogdan on a call.** Not recording content.
- If you catch yourself doing a hook, a punchy opener, or a tidy closing line, stop and restart the sentence.
- Say the real numbers out loud even if they are not public. Brackets get added later.
- Tangents are allowed and wanted. Do not stay on-question.

**Anti-pattern:** answering in writing. Writing is where the performance lives. The whole point is to catch the register before it gets tidied.

## Step 2: Transcribe raw, do not clean

Keep the ums, false starts, repeated words, swearing, self-corrections, abandoned sentences and topic jumps.

Save to `research/transcripts/maurojpelle/YYYY-MM-DD-voice-interview.md` with the standard transcript header.

**Every failed voice doc fails here.** Someone cleans the transcript to make it readable, and the cleaning removes exactly the signal being extracted.

## Step 3: Mine each corpus separately, with counts

Do not read for impressions. Measure. Minimum set per corpus:

- Sentence length distribution, and the % under 8 words
- Average message / paragraph length
- Top 15 sentence openers, with counts
- Most-used content words, stopwords removed
- Hedging markers: maybe, idk, feel like, kinda, I think, probably, might
- Courtesy markers: please, thanks, sorry
- Verdict words, the ones used to praise and to dismiss
- Profanity, where it appears and where it never does
- How uncertainty gets handled. Admitted, hedged, or avoided
- Analogy domains, what he reaches for when explaining
- Capitalisation and punctuation habits, including typos left unfixed

A worked example of this pass on the typed corpus, run 2026-08-05, is in Step 6.

## Step 4: The three-column gap table

One row per observed trait. Columns: **how he talks** (spoken), **how he types** (worklogs/Slack), **how his posts read** (published).

Rows where columns 1 and 2 agree with each other and disagree with column 3 are the findings. Everything else is noise.

Expected finding based on the 2026-08-05 partial run: hedging appears constantly in 1 and 2 and is near-absent in 3, because the current doc bans it.

## Step 5: Write the doc, evidence-only

Create `brand/voice-mauro.md`. Rules for what may go in it:

1. **Every rule cites a real example from the corpus.** No example, no rule.
2. **Every countable rule states its count and sample size.** "40% of sentences under 8 words, n=735" not "writes short".
3. **No adjective-only rules.** "Confident" is banned unless immediately followed by the mechanic that produces it.
4. **Contradictions get kept, not resolved.** If he hedges when proposing and states flatly when reporting, that is two rules with two contexts, not one averaged rule.
5. **Record what he never does**, sourced from absence in the corpus, not from taste.
6. **Do not inherit structure from the Growthub doc.** Start from what the corpus shows, then check whether a Growthub section is warranted. Section order should differ if the voice differs.

## Step 6: Blind test, non-negotiable

Write 3 posts using the new doc. Shuffle with 3 real Mauro posts. Show him all 6 unlabelled.

- **He cannot reliably pick his own** → the doc works, ship it.
- **He picks his own every time** → the doc failed. Return to Step 4 and find what the tells were. The tells are the missing rules.

Log the result at the bottom of `voice-mauro.md` with the date and the score. A voice doc with no passed blind test is a hypothesis.

## Step 7: Retire the fork

Once `voice-mauro.md` passes, rename `brand/voice.md` to `brand/voice-growthub-fork-ARCHIVED.md` and update the `CLAUDE.md` §5 pointer. Do not delete it, it is the control for future comparisons.

---

## Worked output from the 2026-08-05 partial run (typed corpus only)

Ran against 491 usable prompts, 8,024 words, 25 worklog days. Reproduce with a script over `growthub-os/ops/daily/*worklog*.md`, matching `^- \d\d:\d\d · .*? · "(.*)$`.

| Observation | Count |
|---|---|
| Sentences under 8 words | 293 / 735 = **40%** |
| Average prompt length | 16.3 words |
| Top openers | I (47), can (31), okay (25), create (22), what (20), where (17), yeah (12), do (11), how (11), give (11), we (11), alright (10) |
| Hedging | maybe (21), actually (16), idk (8), feel like (6), kinda (3) |
| Courtesy | please (53) |
| Address | bro (14) |
| Negative verdict | ass (13), always as the judgment word, "the htmls are ass" |
| Positive verdict | perfect (13), love (3) |
| Spoken openers | okay (32), yeah (23), alright (10) |

**Three findings already usable:**

1. **He hedges when proposing and the doc bans it.** 38 hedging markers in 8,024 words. This is the single clearest proof the fork is wrong.
2. **He is markedly courteous.** 53 pleases. The current doc's "direct, no fluff" framing misses this completely.
3. **He opens on spoken acknowledgements.** okay / yeah / alright lead 65 messages. Written-voice docs never capture this because it looks like filler on the page.

**What this corpus cannot tell you:** all 491 entries are short imperative commands. There is not one instance of Mauro explaining something at length to another human. That is the entire reason Step 1 exists.

---

## Anti-patterns

- **Cleaning the transcript.** Kills the dataset.
- **Answering the questions in writing.** Produces performance, not voice.
- **Adjective rules.** "Confident and direct" describes every voice doc ever written and constrains nothing.
- **Editing the fork instead of starting fresh.** The fork's structure is Lorenzo's; inheriting it re-imports the problem.
- **Skipping the blind test.** Without it there is no evidence the doc did anything.
- **Averaging contradictions.** Context-dependent behaviour is two rules, not one blurred one.

## Trigger phrases

- "build my voice doc" / "voice extraction" / "the spice project"
- "does this actually sound like me"
- "run the blind test"
