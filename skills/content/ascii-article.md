---
name: ascii-article
description: "Produce one X article where every visual is an ASCII diagram: brand or subject pick, draft, 4-7 cream diagrams, a 5:2 terminal cover, an independent gate run, and a staged handover with a timing log. Triggers on \"ascii article\", \"article with ascii diagrams\", \"terminal-style article\"."
---

# ASCII article production

One X article for @maurojpelle (or for a Ghosted Calls client's account) in which every visual is an ASCII diagram rendered as a PNG. The article is the reach piece. The path to a booked call is one DM keyword at the end, and only when the thing it promises exists.

**Reader:** established agency owners running a real agency, whose pipeline runs on referrals and outbound (`brand/audience.md`). Speak to the operator, never the beginner. Mauro's lane is inbound content systems. Never make his article about running Meta ads for brands (`CLAUDE.md` §1).

## Read first

1. `skills/content/x-articles-POINTER.md`, then in the set it points to: `02-first-screen.md`, `03-title.md`, `05-body.md`, `06-distribution.md`. Declare the lane (`reach` or `convert`) before the subject is picked.
2. `brand/voice.md`, `skills/content/anti-slop-protocol.md`, `brand/claims.md`, `brand/positioning.md`, `brand/audience.md`.
3. `skills/content/gate-playbook.md`: what Mauro rejected before.
4. The source: a transcript in `research/transcripts/maurojpelle/`, an insight card from `skills/research/content-sweep.md`, or a template from `research/post-templates.md`. No source, no article.

Default format is the long mega-playbook: many steps, each one concrete, built from real work.

## Rules for the body

- No em dashes. No "not X, it's Y" in any form. No "most people / most agencies" openers. No trailing summary line.
- Every number and every named fact is in `brand/claims.md` or in a cited research file. A number from another account stays labelled as theirs.
- Quotes are attributed only after a check against the raw source.
- Never name a client.
- **No `[NEEDS: x]` in the publishable body.** A gap either gets cut from the body or goes in section 8 ("Open before publishing"). The body Mauro reads must be ready to post as it stands.
- A DM keyword CTA only when the resource behind it is built and ready to send (`CLAUDE.md` §7). If it is not built, the CTA offers a conversation or an audit.

## Picking a brand or account to feature

When the article features a brand or an account as its example, check where it operates **before** you pick it. The data tool has to cover that country.

- **TrendTrack reach data covers EU and UK advertisers only.** A US brand shows no reach there.
- For a US brand, use the signals that do exist: duplicates of the same ad, days running, and the count of live ads.
- If neither works for the pick, pick a different example. Do not write around a missing number.

This applies mostly to client installs where the subject is a brand. Mauro's own articles feature agencies and systems.

## Diagrams

Every visual in the article is ASCII.

- Write each diagram as `content/ascii/<slug>/NN-name.txt`. Maximum 78 columns, monospace.
- Box-drawing characters only: `┌ ┐ └ ┘ ├ ┤ ┬ ┴ ─ │`. Arrows with plain `v`, `>`, `->` and `|`. **No emoji and no `▼ ▲`.** They render wider and break the frame.
- Before you render, check with python that every line of a boxed diagram has the same length.
- 4 to 7 diagrams per article.
- **In-article diagrams are cream:**

  ```
  python3 content/ascii/render.py content/ascii/<slug>/NN-name.txt @maurojpelle --cream
  ```

- Open each PNG with the Read tool. Fix any border that does not line up, then render again.
- Mark the placement in the body with a line `[IMAGE: NN-name.png]`.

## Cover

The cover is a **5:2 terminal cover** (3000x1200), built with `content/ascii/build_cover.py` from a JSON spec:

```
python3 content/ascii/build_cover.py content/ascii/covers/<slug>.json
```

Required keys: `slug`, `title`, `sub`, `cols`, `tree`. Optional: `mid` (1-2 of the article's diagram .txt files), `handle`, `accent`. Copy `content/ascii/covers/_example.json` to start, and read the script's docstring for the rest. Every word on the cover follows the same claims rule as the body.

## The output file

Write the article to the scratchpad as `<slug>-article.md`. Articles are not saved to the repo (`CLAUDE.md` §7). The diagrams in `content/ascii/<slug>/` are.

Sections:

1. Titles: 5, scored against `03-title.md`, plus the pick.
2. First screen: cover, title and the first three lines as one unit.
3. The article: the publishable body.
4. Diagram list: file, what it shows, the source of every number on it.
5. Companion quote tweet: 25-55 words, uses one of the diagrams.
6. Sources.
7. Claims to add to `brand/claims.md`.
8. Open before publishing: every gap, every unverified quote, every claim that needs Mauro's sign-off.

## Two gate runs, always

1. **Writer's self-check.** Run the draft against `.claude/agents/gate.md` and fix what you find.
2. **Independent gate run.** Then send the fixed draft to the `gate` agent as a separate subagent. It runs on a different model and has not seen the writing. Fix every failure and run the gate again until it returns PASS.

The second run is never optional. In the first week of this process, 5 of 5 drafts that passed the writer's self-check failed the independent check, all on unsourced claims. A writer checking its own work agrees with itself.

## Stage it

**Mauro:** hand over in chat. The picked title, section 3 with the diagram PNG paths in place, the quote tweet, and section 8. Nothing publishes until he approves it.

**Client install:** stage to `[SLOT: the client's staging surface and the person who schedules]`, with every image attached and the cover first.

At the stage step, add one row to `content-log/post-tags.csv` (process `x-article`, see `content-log/README.md`).

## Timing log

Every run adds one row to `content-log/timing.csv`:

```
date,slug,account,brand_pick,draft_done,diagrams_done,gate_pass,staged,total_min,notes
```

- Each step column is a clock time (HH:MM) taken from a real timestamp at that moment: run `date` or read the tool output time.
- **Measured times only.** If a step was not timed, leave its cell empty and say why in `notes`. Never estimate a time and never back-fill one.
- `total_min` = `staged` minus `brand_pick`, only when both were measured.

Create the file with that header on the first run.

## Done when

- The article file has all 8 sections, and section 3 has no `[NEEDS]`.
- 4-7 cream diagrams and one cover are rendered and checked by eye.
- The independent gate run returned PASS.
- The handover is in chat (or the client's staging surface), the `post-tags.csv` row is in, and the timing row is in.
