# System extraction: turning a real system into a card

Produces the source document Juan writes articles from, and the asset the article is built around:
a monospace architecture card plus sparse prose, extracted from a system that actually runs.

**Created 2026-09-14**, after three source docs were written from the wrong repo and in the wrong
shape. Both failures are covered below.

---

## The two rules that caused this file

**1. Extract from the system that runs, not the one that is nearest.**

The working system is `~/growthub-os`. That is where the agents, the 60+ scripts, the eight skill
folders and the gates live, and it is where the work actually happens every day. `mauro-os` holds
the personal brand: voice, positioning, claims, and this skill.

A doc written from `mauro-os` describes a brand, not a machine. Read the growthub system first,
every time, and name the repo you pulled each thing from.

**2. Insight over value.**

Show the **shape** and the **reason**. Do not hand over the implementation.

| Goes in | Stays out |
|---|---|
| The stages, in order, with their names | The prompts themselves |
| What each gate checks, as a category | The checklist contents, gate by gate |
| The failure that created a rule, with its date | The file path, the function, the script name |
| A constraint that shaped the design (a hard API ceiling) | Credentials, board IDs, account IDs |
| The rule that generalises past the tool | The full rule set, copyable as-is |
| Counts that prove scale (how many gates, how many stages) | Client names, the agency name, teammate names |

The test: a reader finishes it understanding **why the system is built that way** and still could
not rebuild it from what they read. If they could rebuild it, too much went in. If they cannot say
why a stage exists, too little did.

---

## What the output is

Two parts, in one file.

**Part 1: the card.** A monospace diagram inside box-drawing characters. It is the thing that gets
screenshotted and posted. It has to read on its own with no article around it.

**Part 2: the notes.** Sparse prose under the card. One block per stage or per constraint. Facts
and numbers only, no framing, no reader-problem section, no lesson.

---

## The card grammar

Fixed. Do not invent new furniture.

```
┌─ SYSTEM NAME · from <input> to <output> ────────────────────────────────┐
│                                                                          │
├─ LAYER · what this layer is for ────────────────────────────────────────┤
│                                                                          │
│   label           the detail, in a second column                         │
│   label           the detail                                             │
│   One plain sentence under the pairs, stating the rule.                  │
│                                                                          │
├─ PIPELINE · plan first, then the work ──────────────────────────────────┤
│                                                                          │
│   1 STAGE NAME      What happens, in one line.                           │
│     │                                                                    │
│     ▼                                                                    │
│   2 STAGE NAME      What happens.                                        │
│     │                                                                    │
│     ├──────────────┬──────────────┐                                      │
│     ▼              ▼              ▼                                      │
│   LANE A         LANE B         LANE C                                   │
│   One line covering all three lanes and how they rejoin.                 │
│     │              │              │                                      │
│     └──────────────┴──────────────┘                                      │
│     ▼                                                                    │
│   3 STAGE NAME      What happens.                                        │
│                                                                          │
├─ GATE · what runs before it reaches me ─────────────────────────────────┤
│                                                                          │
│   build → check against the brief → pass → my review                     │
│            └── fail → name the block → rebuild → check again             │
│                                                                          │
│   Checks     category · category · category · category                   │
│   Stop       the conditions that halt the run                            │
│                                                                          │
│                                                    @maurojpelle          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Rules for the card**

- Layer headers are uppercase, then ` · `, then a lowercase subtitle. The rule fills to the right
  edge.
- Two columns inside a layer: a short label, then the detail. Align the second column.
- One plain sentence per layer, stating the rule that layer enforces. Never more than two.
- A pipeline is numbered, with `│` and `▼` between stages.
- Parallel work fans out with `├──┬──┐` and rejoins with `└──┴──┘`.
- A loop uses `└──` under the step it returns to.
- `@maurojpelle` sits bottom right, inside the frame.
- Everything is monospace. Nothing depends on colour.
- It fits one screenshot. If it does not, the system was described at too fine a grain.

**Banned in a card:** file paths, script names, prompt text, client names, the agency's name, any
number that is not already public, decorative unicode beyond the box-drawing set.

---

## Extraction procedure

1. **Read the real system in `~/growthub-os`.** The skill folder, the scripts that run it, the
   agent if there is one, and the gotchas or QA file. Read them, do not skim.
2. **Find the stages.** A stage is a point where the artifact changes state. Five to eight is
   usually right. More than eight means the grain is too fine for a card.
3. **Find the fan-out.** Almost every system has one point where work splits and rejoins. If you
   cannot find it, the system is a line and the card should be a line.
4. **Find the gate.** What runs before a human sees the output, what it checks, and what stops it.
   If there is no gate, say so. An honest missing gate is a stronger note than an invented one.
5. **Find the constraints that shaped it.** These are the interesting part. A hard limit in a tool,
   a failure with a date, a rule that exists because something broke. Each one gets a note.
6. **Write the card.**
7. **Write the notes.** One block per stage or constraint. State the fact and stop.
8. **Run the disclosure check** in the table above, line by line.

---

## The notes format

```
## <Stage or constraint name>

<What it is, one or two lines.>

<What it costs or what it enforces, with the number if there is one.>

<The date and what broke, if a failure created it.>
```

No lesson at the end of a note. No "this means that you should". The reader draws it.

---

## Numbers

Every number traces to `brand/claims.md` or to the growthub file it was read from. Nothing is
estimated and nothing is rounded to look tidy.

Where a number is missing and the point needs one, write `[NEEDS: x]` and leave it visible. The
gap wins over a plausible stand-in.

## Voice

`brand/voice.md` applies to the notes. No em dashes, no "it's not X it's Y", no "most agencies"
opener, no closing summary.

The card is not prose. Labels and fragments, lowercase where the examples are lowercase.

## Where the output goes

`~/Downloads/juan-mds/`, numbered. Not committed to either repo, because these describe the
internals of a live system and the repo copy would drift from the system it describes.
