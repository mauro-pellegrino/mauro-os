# Article source pack for Juan: @maurojpelle

Juan writes articles for Mauro's X profile. This pack holds the subjects and the evidence behind
them. It does not hold drafts.

**Why this exists.** Mauro's articles do not fail at the writing. They fail at the subject and the
title. Drafting from a good subject is the easy half. So this pack spends all of its effort on the
half that decides the outcome, and none on the half Claude already does well.

**Built 2026-09-14.**

---

## Who the reader is

An established agency owner. Marketing, creative, ads, SEO or social. Mid six figures a month and
up. Their pipeline runs on referrals and cold outreach and it is drying up. They know they should
use AI to produce content and win clients and they have no system for it.

Not beginners. Not freelancers. Full ICP in `brand/audience.md`.

**The one test for any subject:** does it name a problem that person has this week? If the subject
is interesting mainly to someone who builds content systems, it is off-target, however good the
material is.

## The subject rule that gets broken most

**The subject comes from the reader's agency, not from Mauro's analytics.**

Mauro's own numbers pick the format, the title shape and the opener. They are not the subject. An
article about our impressions is an article about us.

The work in this repo is the **evidence**, not the topic. "Here is how our content system is
built" is a topic about us. "Your agency already recorded every article you will publish this
year" is a topic about them, proved with the same material.

---

## The split of work

| Step | Who | What |
|---|---|---|
| 1 | Juan | Pick a subject from `subjects.md`. Assemble the input document. |
| 2 | Juan | Every quote, number and source in one file, each with its repo path. No writing decisions. |
| 3 | Claude | Run the seven article files in order: lane, subject, first screen, title, cover, body. |
| 4 | Mauro | Approve in chat. Nothing publishes without this. |

**Step 3 has a blocker.** The seven files live in `~/growthub-os/skills/content/x-articles/` and
Juan does not have that repo. See `subjects.md`, bottom, for the options. Until it is resolved,
Juan does steps 1 and 2 and hands the input document to Mauro.

## Building an input document

One file per article. Its only job is to put every usable piece of evidence in front of the
article skill so nothing has to be remembered or invented.

```
# Input: [subject]

## The reader's problem
One paragraph. Their words where possible, from brand/audience.md.

## The evidence
For each item:
  - the claim, in one line
  - the number, if there is one
  - the file path it came from
  - whose account or repo it belongs to

## The story
What actually happened, in order, with dates. No lesson attached.

## What is missing
Anything the subject needs that no file in the repo carries. Write [NEEDS: x].
```

`[NEEDS: x]` stays visible. It never gets filled with something plausible.

---

## Hard rules

1. **Never name the agency or a client.** In public it is "the B2B agency I run content and
   acquisition for" or "an account we manage". `CLAUDE.md` §7.
2. **Never invent a number.** Every number traces to `brand/claims.md` or to a file path in the
   input document. Three rows in `claims.md` are marked *needs sign-off* and cannot be used until
   Mauro approves them.
3. **Voice is `brand/voice.md`.** No em dashes, no "it's not X it's Y", no "most agencies" opener,
   no closing summary line.
4. **Articles are not saved to this repo.** They go to Mauro in chat first. `CLAUDE.md` §7.
5. **Length.** Articles default to the long mega-playbook format, not short pieces.
6. **Evidence that belongs to another account gets labelled.** Most of the measured article
   evidence came off `@lorenzo_pravata`, a different ICP. It is a hypothesis for this account,
   never a proven result here.
