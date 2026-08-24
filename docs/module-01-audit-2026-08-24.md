# Module 01 audit: what's missing for it to be worth more

Ran 24 Aug 2026 against every page of the module, the skill files behind it, and the module's own rules in `brand/engine/README.md`.

---

## Fixed in this pass

**1. Page 00 promised a module that doesn't exist.** Its contents list named five pages (Rules, Prompts, Worked Example, Score Your Own, Delivery Kit) and ended with "start with page 2." The module has eight pages with different names and a different order. A buyer hit that contradiction in the first sixty seconds. Rewritten to the real eight.

**2. The one line the build test flagged as not sounding like Mauro.** "They fatigue. Fast." was called out in `content/qa/notion-assembly-log.md` as the single AI-punchy staccato spot and never changed. It's now a sentence.

**3. A second delivery format, which is new value rather than a fix.** The module taught one way to ship a magnet. It now teaches two. See below.

---

## Added: the document format (page 08)

The module built magnets as workspaces only. That is now one of two lanes.

The document lane ships a magnet as a single PDF with hand-drawn diagrams, in the register of the JK Molina docs. It travels better than a workspace, opens on a phone, and needs no account on the reader's side.

**What shipped with it:**

- `brand/engine/module-01-lead-magnets/08-document-format.md`: when to use it, seven layout rules, the diagram style spec, the full render pipeline, the prompt
- `brand/lead-magnets/the-lead-magnet-machine.pdf`: a complete magnet in the format, built from Mauro's own Topic 1 answers
- `brand/lead-magnets/the-lead-magnet-machine.html`: the source
- `brand/lead-magnets/assets/machine-doc/`: four diagram generators, SVG and PNG, plus `gen.py`
- A Google Doc version, editable, images by hand: https://docs.google.com/document/d/1gdsWBdObXC16w8IixbIGVI8iYg3Ay-hmVArmbnsRUNI/edit

**Why this is worth more than another page of rules.** The module now contains a finished artifact a buyer can hold up against their own attempt, in a format nobody else in this space teaches. It also closes the "zero images" gap for one lane, because the diagram generators are the images.

---

## Still missing, ranked by what it adds

**1. ~~Three subtypes~~ CLOSED 24 Aug.** Framework and video-sourced are now Files 3 and 4 on page 04. Case study and industry-specific are stated as deliberately out, with reasons, on page 03 §8. Original finding: Page 03 §8 lists five subtypes in a table. Page 04 ships the skill file for one. The module names its own gap and leaves it open, which is worse than not listing five.

Two are ready to port with no new thinking: `skills/lead-gen/lead-magnet/framework.md` (207 lines, solid) and `youtube-video.md` (227 lines). `case-study.md` and `industry-specific.md` were marked unusable during the build test, so they stay out and page 03 should say why rather than list them.

**2. Screenshots, for the workspace lane.** The rules say a real screenshot is the strongest image option and to use it most. The workspace pages still contain none. Minimum set is five: the input folder, the skill file open, the generated doc with build status, one finished magnet, one auto-DM thread. Only Mauro can take these.

**3. The evidence rebuild on page 03.** Still 40 rows from one month on one account. Blocked on the 365-day exports. Until they land, the page should say out loud that it's 40 rows from one month, which is more credible than presenting it as a study.

**4. One worked example per subtype.** Needed once the subtypes land. Blocked on Mauro naming which shipped magnets can be used.

**5. No video anywhere.** The buyer's whole profile is that they make video and the module is entirely reading. The lead magnet board built on 23 Aug is the script for the first one.

---

## Two contradictions worth resolving

**The magnet format vs the product container.** Notion is out as the container for the product. The module still teaches building magnets inside Notion, which is a different decision and may still be right. Open question A1 in the voice notes.

**The landing page.** `skills/lead-gen/lead-magnet/_master.md` ships a Landing Page Spec and says the DM links to an email-capture page. The 22 Aug decision was DM-only and no landing page exists. The skill and the product now disagree. The document format page states the DM-only reality; `_master.md` has not been updated to match.
