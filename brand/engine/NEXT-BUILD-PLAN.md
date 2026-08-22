# Engine: next build plan

**Written 21 Aug 2026** at Mauro's instruction, before a context reset. Everything agreed and everything outstanding, so the next session starts here.

---

## 1 · DECIDED: anonymised, no names

**Mauro's call, 21 Aug: never name the agency owner or the co-founder. Anonymised only.**

Every worked example, every evidence table, every subtype example ships as "a $300k/month agency's account" or "a co-founder's account". Real numbers, real structures, real results. No names, ever, in anything a buyer sees.

This matches the 17 Aug scrub and `CLAUDE.md` §7. No permission needed from anyone, so the examples are unblocked and can be built immediately.

**Nothing below in this section needs re-reading. Kept as the record of why.**

---

## 1b · The conflict this resolved

Mauro asked for the subtype examples and worked examples to use **the agency owner and the co-founder's real accounts as named examples**.

That directly contradicts two standing rules set four days earlier:

- **His own instruction, 17 Aug:** *"we need to make sure that we remove all the agency from my stuff mauro os, ghostedcalls."* 46 mentions across 16 files were scrubbed to zero.
- **`CLAUDE.md` §7:** never name clients in anything public-facing. `positioning.md` adds that any specific public number needs his sign-off, and that he must never borrow the agency's anchors as his own proof.

This is a paid product going to strangers, which is the most public-facing thing in the repo.

**Two ways forward. Mauro picks.**

**A · Anonymised (recommended, no permission needed).** "A $300k/month agency's account." "A co-founder's account, 12k followers." The numbers, the post structures and the results all ship. Only the names don't. This is what the current copy already does and it costs nothing.

**B · Named.** Materially stronger proof, and it needs the agency owner's explicit sign-off in writing, plus a reversal of the scrub decision. Note the person named would be identifiable to anyone in the ads world regardless, so A is not much weaker in practice.

**Do not proceed on the examples until this is answered.** Building them named and then reversing means rewriting every worked example.

---

## 2 · Module 00 · The Second Brain

**Mauro's idea, and it's the right module 00.** Before anyone can use module 01 they need source material in a form the system can read. A big-channel operator has years of video and none of it is text.

Module 00 is: build a transcript library from your entire back catalogue, so every module downstream has fuel.

Why this is the correct entry point:
- It maps to stage 1 of the engine (source), which is currently the only stage with no module
- It is the single highest-leverage hour a big-channel operator can spend, and nobody has done it
- It makes every later module work immediately instead of after they go find material
- It is the cheapest module to build, because it is mostly tooling and a folder convention

**Source material for it:** `research/transcripts/` conventions, the fetch-once-save-always rule in `CLAUDE.md`, and `ops/tools/fetch-competitor-transcripts.py` in the agency repo.

Renumber: 00 Second Brain, 01 Lead Magnets, then 02-07 per the pipeline below.

---

## 3 · Subtype expansion for module 01

Page 04 currently ships one subtype of five. To close gap 1 in the module-01 audit, add to page 04 and give each one a worked example:

| Subtype | Internal source | Example needed |
|---|---|---|
| Framework | `skills/lead-gen/lead-magnet/framework.md` | One 5-component framework magnet |
| Case study | `case-study.md` | One transformation, anonymised per §1 |
| Video-sourced | `youtube-video.md` | One video disguised as a breakdown |
| Industry-specific | `industry-specific.md` | Blocked: its Active Niches table is empty by design |

Worked examples come from the shipped magnets in the agency repo, subject to §1.

---

## 4 · The GPT image prompt system: where it actually is

Mauro asked where it lives. Answer: **it does not exist as a system.** It exists as scattered references:

- `skills/lead-gen/lead-magnet/_master.md` — defines the two prompt-block formats, every example ends in `...`
- `skills/lead-gen/lead-magnet/prompt-swipe-file.md` — names "GPT Image Infographic Prompt File" as a title pattern
- `skills/content/x-article-creator.md` — references image prompts
- `skills/miro/visual-language.md` — the closest thing to a real visual system
- Four daily worklogs mention building image prompts ad hoc

The only written-out image prompts anywhere are the **12 Juan produced during the build test**, now in `content/qa/lead-magnet-build-log.md` and page 04 of module 01.

**So this is a module to build, not a file to find.** It belongs with module 05, the Visual Doc System.

---

## 5 · The evidence: what to replace and with what

Current evidence in `03-the-rules.md` is a 40-row pull from July on one account. Mauro has offered full 365-day exports from both accounts across X and LinkedIn.

**What the exports would let us build, which we cannot build now:**

1. A real comment-rate table across a year instead of 40 rows in one month
2. Title-formula validation at scale: does the artifact-noun rule hold over 12 months
3. LinkedIn versus X comparison, which the module currently has nothing on
4. A fatigue curve with more than one week of data
5. Month-over-month decay, so the recycle-after-8-to-12-weeks rule gets tested rather than asserted

Evidence is the least reconstructable part of the product. This is the highest-value input Mauro can hand over.

---

## 6 · Templates and visuals: where they point

Mauro asked where these take the reader. Current honest answer:

- **The magnet** lives on a published Notion page. The auto-DM links straight to it
- **No landing page**, no email capture, no booking link
- So the chain ends at: they claim it, they read it, they reply in the DM. That is the whole funnel today
- Page 05 templates all point at that, which is coherent but thin

**DECIDED 22 Aug: DM-only.** The product teaches the path Mauro actually runs. A landing page and email capture is a build neither of us has done and it would block shipping for weeks. The 90-day export backs it: 0 URL clicks across 377 posts, so the audience is not clicking out anyway.

`{{calendly_url}}` is replaced with "DM me @maurojpelle" everywhere it appears. A live placeholder in a paid product is worse than either option.

---

## 7 · What Mauro needs to send

Ranked by what unblocks the most.

1. ~~Answer §1.~~ **Answered 21 Aug: anonymised, no names.** Examples unblocked.
2. **The 365-day analytics exports.** X and LinkedIn, both accounts. Blocks the evidence rebuild, which is the most valuable page.
3. **The resources you actually send.** The real lead magnets, as links or exports. Blocks the extra worked examples.
4. **One decision on §6.** DM-only or full funnel.
5. **A voice note on why lead magnets work**, if you want page 00 in your own words rather than my draft.
6. **Nothing for module 00.** I can build the Second Brain module from what is already here.

---

## 8 · The pipeline, restated

| Module | Status |
|---|---|
| 00 · The Second Brain | Agreed, not built. Cheapest to build, highest leverage |
| 01 · Lead Magnets | 8 pages written. Missing 4 subtypes, more worked examples, all images, the evidence rebuild |
| 02 · The Article System | Material exists |
| 03 · The Format Multiplier | Material exists |
| 04 · The Measurement Loop | Material exists |
| 05 · The Visual Doc System | Material exists, plus the image-prompt system from §4 |
| 06 · The Board System | Material exists |
| 07 · The YouTube System | Material exists. Highest affinity for this ICP |

**Pricing, settled 22 Aug:** $500 one-time for module 01. Switch to $99/mo the month module 02 ships, because recurring is only honest once the library is actually arriving. Early buyers get the $500 credited against month one.

**Packaging, settled 22 Aug:** Notion duplicate-template page as the container, manual invoice for payment. A git repo for the skill files behind one download link so corrections reach existing buyers. Whop parked until pricing goes recurring.

---

## 9 · Standing gaps carried forward

- The offer has never been sent to a single person. Two names have been on the list for a month
- The Loom is recorded and unpublished, still needs a title and the naming decision
- Module 01 breaks its own image rule: zero screenshots in a product that says screenshots are the strongest option
- No email platform, and no measurement of any magnet ever shipped. The calendly gap is closed by the 22 Aug DM-only decision
