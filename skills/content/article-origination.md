# Skill: Article Origination (the question loop)

**Version:** 1.0
**Created:** 21 September 2026
**Source:** Mauro's working session of 2026-09-21, transcript at
`research/transcripts/maurojpelle/2026-09-21-article-workflow-and-patience-belief.md` (19:39 to
20:39 is the board he drew; 03:27 to 06:58 and 10:33 to 11:28 are the two paths being run live)
**Input:** one of Mauro's posts that performed, or one viral article from a top personal brand
**Output:** an article brief (title options + question set + drafted answers), not an article

---

## What this skill does

This is the stage that runs **before** any article gets written. It turns a proven piece of demand
into a briefed subject with the questions already answered, so the writer skill has real material
instead of a topic.

Mauro drew it as one board with two entry paths converging on one output:

```
  [A] tweet w/ good performance  ─┐
                                  ├──►  NEW ARTICLE BRIEF
  [B] viral article from a        │      ├─ better titles
      top personal brand         ─┘      └─ questions, answered by mauro and/or claude
```

**Path A is the preferred one.** Mauro, 20:18: "obviamente yo prefiero que hagas este proceso."
Path B exists because the title and structure quality on outlier articles is still ahead of
anything this system generates cold, and borrowing a shape beats inventing a worse one.

When the brief is signed off, hand it to `skills/content/x-article-creator.md` (voice, register,
correction log) and the set behind `skills/content/x-articles-POINTER.md` (subject, title, cover,
body, distribution). **This skill never writes the article.**

---

## Path A: from a tweet that already performed

The demand is already proven. The tweet is the thesis, the article is the expansion.

**Step 1. Take the post whole.** Paste the actual text, plus its numbers (likes, replies,
impressions if available) and its date. A post gets picked because it performed, not because the
idea is liked internally.

**Step 2. Ask for questions, not an outline.** Mauro's own prompt, 04:34:

> with this tweet that worked for us, we need to ask questions that make sense in order to expand
> on this idea into an article. generate title ideas as well.

The questions are the deliverable. An outline is Claude deciding the article; a question set is
Claude finding the holes and Mauro filling them.

**Step 3. Generate titles in the same pass.** Mauro, 06:34: the titles come back with the questions
so he knows the angle before he answers anything. A question set with no title attached leaves the
angle floating, and he answers into a vacuum.

---

## Path B: from a viral article by a top personal brand

**What gets copied is the shape, never the subject.** Mauro's live example was
`How to become a robotics engineer in six months`, from an account matching AI influencers to
companies. His words, 11:38: "no es nuestro tema, no estamos ni cerca. Lo que me gusta es cómo
escribe y cómo hacen los artículos, no sobre qué habla."

**Step 1. Capture the article whole**, per `skills/research/article-corpus.md`. Save to
`research/outlier-x-articles/` with the account, the view count and the date. Fetch once, save
always.

**Step 2. Paste it in with the retarget instruction.** Mauro's own prompt, 10:59:

> generate an article like this one, but change the title so it makes sense for us.

**Step 3. Lane check before anything else.** The borrowed article will pull the subject toward its
own business. Kill that on sight: Mauro's lane is inbound, personal brand, YouTube, and AI content
systems that book calls for established agency owners (CLAUDE.md §1, §2). A borrowed structure that
only works if Mauro claims a practice he does not run gets rejected at this step, not fixed later.

**Step 4. Same output as Path A:** questions plus titles.

---

## The question set

Between 6 and 12 questions. Each one must be a question whose answer becomes a section or a
paragraph, not an interview warm-up.

**Ask about:**
- the mechanism (how does the thing actually run, step by step)
- the time cost (how long it takes him, how long it took to build)
- who it is for and who it is not for
- the failure mode (what goes wrong, what he tried that did not work)
- the number (what result is attached, and whether it is his or the agency's)
- the objection a sceptical agency owner raises at that exact point

**Do not ask:**
- anything already answered in `brand/positioning.md`, `brand/audience.md` or
  `brand/business-context-answers.md`. Answer it yourself and mark it answered.
- questions that only restate the tweet back as a question.

---

## Answering the questions: Claude drafts first

**This is the part Mauro changed on 2026-09-21.** He does not want a blank question list back. He
wants every question already answered so he is correcting, not writing.

His prompt, 15:00:

> draft a response for each question in mauro's voice. I will check them and tell you what I think.

His reasoning, 15:36: "Claude debería saber las respuestas. Cuánto me dura hacer esto? Lo debería
saber. Para quién? Ya sabe."

**How to draft an answer:**

1. Pull from `brand/voice.md`, `brand/positioning.md`, `brand/audience.md`, `brand/claims.md`,
   `brand/operating-baseline.md` and `research/transcripts/maurojpelle/`. If he has said it before,
   the answer is in the repo.
2. Write it in his voice, short, first person, plain.
3. **Every answer carries its source in brackets:** `[from: 2026-08-06 voice interview]`,
   `[from: positioning.md]`. An answer with no source is an invented answer.
4. **Anything the repo cannot support gets `[NEEDS MAURO]` and nothing else.** Do not guess a
   number, a motivation or an origin story to complete the set (belief 10, gate-playbook G-006).

**Mark every answer with a confidence flag** so he knows where to spend his review:

| Flag | Meaning |
|---|---|
| `[SOLID]` | traced to a specific line in the repo or a transcript |
| `[INFERRED]` | consistent with what he has said, but assembled, not quoted |
| `[NEEDS MAURO]` | no source, do not publish anything built on it |

He expects roughly half to be wrong. His words, 21:21: "hay algunas que son buenas y otras son
malas." That is a working result, not a failure. The corrections come back and get applied.

**Gaps get filled by voice note, not by typing.** Mauro, 02:27 and 02:48: "por eso te digo que me
mandes para hacer audios... si yo te mando audios largos, voy a hablar yo lo que yo considero
importante." Ask for one audio covering all the `[NEEDS MAURO]` questions at once, transcribe it,
and save it to `research/transcripts/maurojpelle/` before using it.

---

## Titles: the known weak spot

**Flagged by Mauro on 2026-09-21 as a system problem, not a one-off.** His words, 09:40 and 12:52:
"muchas veces claude es muy malo dándonos títulos... si nos gusta mucho más estos títulos
comparado con lo que nos dio antes, tenemos un problema del sistema, de los skills que tenemos
dentro de mauro-os."

Until a generated title beats a borrowed one in front of him, every title set follows this:

1. **Between 4 and 6 options, and at least half built on a shape lifted from a named real
   article** that visibly performed. Cite the source next to each one:
   `Full guide on building an inbound engine with claude code [shape: @acct, "How to become a
   robotics engineer in six months", 1.2M views]`.
2. **Recase every borrowed title** to house style: first word capitalised, every product name
   lowercase (gate-playbook G-010, G-003).
3. **The head noun must be concrete and recognisable.** Named tools travel, `this mistake` and
   `what nobody tells you` do not. See the head-noun gate in `x-articles-POINTER.md`.
4. **Never carry a borrowed subject across with the shape.** Retarget it to Mauro's lane or drop
   the option.
5. **When Mauro picks a borrowed shape over a generated one, log it** as a correction-log entry in
   `x-article-creator.md`. That is the evidence the title system is still behind, and it is what
   eventually fixes it.

The shape bank to pull from: `research/outlier-x-articles/`, the six patterns in
`x-article-creator.md` §Title Engineering, and Mauro's standing habit of reading Lorenzo's article
list for what landed (10:33).

---

## Output template for the brief

```
## Brief: [working subject]

**Origin:** [A] tweet, 2026-09-14, 312 likes / 84k impressions  |  [B] article, @acct, 1.2M views
**Lane:** reach | convert
**Lane check:** [one line confirming the subject sits inside Mauro's lane]

### Title options
1. [title]  [shape: generated | @acct "source title", views]
2. ...

### Questions + drafted answers
**Q1. [question]**
[drafted answer in his voice]
`[SOLID] [from: brand/positioning.md]`

**Q2. [question]**
`[NEEDS MAURO]`

### Open gaps for the voice note
- [Q2, Q5, Q7 in one list, so he records once]
```

---

## How to run this skill

1. Take the origin (a post that performed, or a captured outlier article). Refuse to start from a
   bare topic; this skill exists because topics picked internally are the weak input.
2. Read `brand/voice.md`, `brand/positioning.md`, `brand/audience.md`, `brand/claims.md` and
   `skills/content/anti-slop-protocol.md` in full before writing a single answer (gate-playbook
   G-004).
3. Path B only: capture and save the source article first.
4. Build the question set.
5. Draft an answer to every question, flagged and sourced.
6. Build the title set, at least half borrowed-shape, sourced.
7. Send the brief through the `gate` agent, then show it in chat. Nothing in the brief is
   published, and the brief itself is not an article.
8. Apply his corrections, collect the voice note for the gaps, transcribe and save it.
9. Hand the signed-off brief to `x-article-creator.md` and the x-articles set.

**Nothing here bypasses §7 of CLAUDE.md.** The brief is a draft until Mauro approves it in chat.
