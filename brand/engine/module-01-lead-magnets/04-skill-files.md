# The Skill Files

**Three files. Paste them in and the system runs.**

Download all three from the repo link at the top of this module, or copy them from the code blocks below. Either way they go wherever your setup keeps context: Project knowledge if you're on Path A, the folder if you're on Path B.

You'll have four files total once you add your own `brand-context.md` from page 02. That one is not optional. These three tell the system what to do. Yours tells it who it's for.

---

## File 1 · `magnet-master.md`

The rules the system reads before writing anything. Loaded every time.

```markdown
# Lead Magnet: Master

Load this file plus one subtype file before producing anything.
Read brand-context.md in full first. Every decision below is filtered through it.

## WHAT A LEAD MAGNET IS

An artifact someone receives in exchange for a comment or an email.

Two things decide whether it works, and neither is the writing:
1. The title names a thing, not an idea.
2. The inside is worth $100 of work they did not have to do.

## TITLE

Formula: [topic a beginner recognises] + [artifact noun] + [number or year]

Approved artifact nouns: guide, playbook, checklist, sheet, kit, system,
workflow, prompt file, stack, template, swipe file, breakdown, tutorial,
formats, prompts.

The artifact noun is non-negotiable. The title must name the thing that
lands in their DMs.

Two separate effects, do not conflate them:
- Breadth drives reach. The widest word in the niche pulls the most views.
- A concrete, currently-urgent named thing drives redemption, roughly 4x
  the comment rate. Comments are how they claim it, so redemption is the
  number that pays.

Aim broad enough that a beginner recognises the topic, concrete enough
that it feels urgent this month. Pull the urgency from the "live problem"
field in brand-context.md.

BANNED:
- Invented concept nouns. Nobody wants an "autopsy" or a "camouflage file".
- Diagnoses or questions. "Why Your Ads Stopped Scaling" promises nothing
  received.
- Sophistication signalling. Broad title for reach, real depth inside.

Always propose 3 title options. Never ship one without alternatives.

## THE $100 BAR

Every magnet is worth at least $100 to the person who asks for it. Not
$100 of reading. $100 of work they did not have to do.

1. It is a thing you fill in, not a thing you read. If a page has no blank
   field, no row to score and no verdict, it is an article wearing a
   magnet's title.
2. The last two pages are usually where the $100 lives. The explainer
   pages are setup.

The four artifacts that clear the bar, in order of value:
- Paste-ready prompts with variable slots, chained, in order. Include at
  least one that tells the reader no.
- A real swipe file: named examples pulled apart, plus a blank sheet.
- A scoring artifact: their numbers in, a verdict out.
- A filled-in worked example: the template completed for a real case.

MANDATORY STRUCTURE RULE: every magnet contains at least one page the
reader fills in, and it sits second to last. The final page is the CTA.
Order always ends: [content pages] -> [FILL-IN PAGE] -> [CTA PAGE].

TEST BEFORE SHIPPING: if someone read the whole thing and did nothing
differently tomorrow, it failed, regardless of how good the writing was.

## STRUCTURE

5 to 7 pages. Under 5 feels thin. Over 8 and they stop before the fill-in
pages, which are the ones that deliver.

Every section is a real, separately created child page nested inside a
parent. Never headings, toggles or dividers stacked on one long page.

End state: parent = cover + intro + N clickable subpages + CTA + credit.

If a build ends with all content on the parent page, it is wrong. Rebuild.
A 7-page magnet arriving as one scroll reads as a blog post. The same
content as 7 clickable pages reads as a product.

## IMAGES

The image ADDS to the page. It never restates it.

Test before writing any image prompt: cover the page text. Does the image
still teach something? If no, it is decoration and it is wrong.

BANNED: an infographic, stat card or "key takeaways" graphic whose content
repeats the text on the same page.

Three allowed styles:
- Real example screenshot. Any page teaching a format or structure.
  Strongest option, use it most.
- Worked example. Any page whose deliverable is a template. Show it
  filled in.
- Doodle scene. Concept and mechanism pages only.

RENDER as HTML and screenshot when the image has more than ~30 words that
must be exactly right, any table, any checklist, aligned diagram boxes, or
numbers you will want to change later.

GENERATE with an image model only for illustrative work: a doodle, a
scene, a metaphor, one or two short labels.

NEVER generate a fake example of a real thing. No fabricated dashboard, no
invented engagement numbers. If a page teaches by example, the example is
real. This is the fastest way to lose a reader who checks.

Every page ships two prompt blocks so visuals never depend on inventing
prompts later:
> PAGE IMAGE PROMPT (16:9, <style>): ...
> HTML STYLE PROMPT: ...

## COVER

Default: a clean screenshot of the asset's own first screen. Not a
designed card.

Why: it shows the reader the actual thing they are about to receive, and
the visible subpage list does the "what's inside" job for free. A designed
card promises. A screenshot proves.

What makes it work: crop tight, no browser chrome, no cursor, no comment
bubbles. Title legible at thumbnail size. Enough of the page list visible
that they can count the pages. Capture at 2x, then downscale.

Fallback, only when no asset exists yet or its first screen is dull: a
designed card, built as HTML and screenshotted. Never generated.

## FATIGUE

They fatigue fast. Real data from five auto-DMs on one account in one week:
7,839 -> 6,329 -> 4,369 -> 1,637 -> 901. The fifth did 11% of the first,
six days apart. Four of the five were the same asset and three opened on
the same line.

The first one beat every long-form post that week except one, so the
mechanism is fine. Running one offer four times is what dies.

Rotate the asset shape. Do not cut the volume. Maximum one of any given
asset type per week. Recycle a winner after 8 to 12 weeks with a changed
hook rather than building a new one.

## MEASUREMENT

Track the comment rate, not views. Views tell you the title was broad.
Comments are the redemption action, so that is the number that maps to
leads.

Also track DMs received and qualified calls. Without those two you can
correlate titles with attention and never with revenue.

## VOICE

All copy follows brand-context.md. Non-negotiables regardless:
- No em dashes.
- No "it's not X, it's Y" or any variant that sets up a false contrast to
  sound profound.
- No "most brands / most people" openers.
- No taking a downside and recasting it as the intended outcome.
- Numbers over adjectives, and only real numbers. If a number is not in
  brand-context.md, write without it rather than inventing one.
- Speak from experience. "The engine I run daily" beats "I have lots of
  experience."

## OUTPUT

Every magnet ships with:
1. The asset itself
2. Cover image (or the brief for it)
3. Post copy for each channel
4. The DM that fires on the keyword
5. The auto-DM tool config
```

---

## File 2 · `magnet-prompt-file.md`

The subtype. Start with this one, it's the fastest to a shippable magnet.

```markdown
# Subtype: Prompt / Swipe File

Load with magnet-master.md.
DM noun: "file"

## WHAT THIS IS

A package of AI prompts, or a curated swipe file, that the reader can
paste, run or copy on Monday morning. Tactical, file-format,
ready-to-execute.

Start here. Prompt files are the fastest subtype to produce and the
easiest to make genuinely useful, because the artifact is the value.

## INPUTS

Decide these before drafting. If you cannot answer one, answer it from
brand-context.md rather than skipping it.

1. Tool the prompts are for.
2. Use case. Be specific: "turning one video into a week of posts" beats
   "content".
3. Number of prompts and page format. Three patterns work:
   - 5 pages x 2 prompts (10 total). Medium-length prompts across phases.
   - 10 standalone prompts. Short and paste-ready as a flat list.
   - 5 pages x 1 long prompt. Each prompt is 30+ lines and warrants a page.
   Rule: match the format to how the prompts are actually used. Long
   prompts get their own page. Short related prompts pair up.
4. Grouping. Name the phases.
5. Worked examples. Always yes.
6. Trigger keyword. 3-7 characters, all caps, topic-related.
7. Whether a specific tool is having a moment right now. If yes, lead the
   hook into it.

## TITLE

Two patterns:
A. [Tool] [Use Case] for [Outcome]
B. [Tool] [Format] Prompt File

Subtitle formula: [N] prompts I use to [outcome tied to real work].
The subtitle always carries a number anchor and a proof anchor. No
subtitle without both.

## BODY

SETUP ONCE
  [1-2 steps before the prompts: paste your brand context, create the
   project, connect the tool]

PROMPT GROUP 1: [name]
  Prompt 1: [purpose] -> [paste-ready prompt]
  Prompt 2: [purpose] -> [paste-ready prompt]
  Worked example: [real input, real output]

[repeat for 4-5 groups]

FILL-IN PAGE (second to last, mandatory)
  [a blank version of the thing they just watched you fill in]

CTA PAGE (last)

## RULES FOR EACH PROMPT

- Paste-ready. No [TOKEN] placeholders unless a setup step explains them.
- Specific. "Write 5 posts in build-log format for an SEO agency owner
  documenting a client migration, speaking to other agency owners" beats
  "write 5 posts".
- Grounded in real work. Reflect how the tool is actually used, not a
  prompt-engineering exercise.
- Single-output focused. One prompt, one deliverable. No mega-prompts.
- At least one prompt must be able to tell the reader no. A chain that
  only ever agrees is not a system.

## WORKED EXAMPLES: MANDATORY

After each prompt group, ship a real input and its real output.

This is what separates the file from a generic prompt library. Operators
want to see the output before they trust the prompt.

## HOOK

Highest-performing formula when the tool is novel and trending:
"[Tool] is INSANE for [use case]" or "[Tool] is CRAZY good"

The body almost always includes "I've built a file with [N] prompts" as
the bridge between hook and bullets.

Bullets for a 10-prompt file: the N prompts / the companion file / worked
examples. Short. The post is a teaser, not the magnet.

## ANTI-PATTERNS

- Generic prompts. Anyone with a chat window can write "give me 5 posts".
- Prompt walls with no grouping. The grouping IS the magnet.
- Skipping worked examples. Trust dies immediately.
- A subtitle with no proof anchor. Reads like anyone's prompt pack.
- Reusing a tool-hype hook months after the tool peaked.
```

---

## File 3 · `magnet-delivery.md`

The build prompt. Paste this once the content exists and it creates the pages.

```markdown
# Delivery Page Build

Paste this into your AI with Notion connected, or use it as the structure
if you are pasting into Notion by hand.

Substitute everything in [brackets] before running it.

---

You are building a lead-magnet DELIVERY PAGE in Notion.

CRITICAL STRUCTURE RULE, READ TWICE
Do NOT put all content on one page. Build ONE parent page, then create
SEPARATE CHILD SUBPAGES nested inside it, 5 to 7 of them. Each section is
its own nested child page. Not a heading. Not a toggle. Not a divider.
If you catch yourself adding an H2 for a section on the parent page, stop
and make it a nested subpage instead.
End state: a parent page containing 5-7 clickable subpages, the
second-to-last being the fill-in page.

FORMATTING
- Parent page cover: solid [YOUR BRAND COLOR].
- Subpage titles: plain text, no emojis.
- Authority line at the very top of the parent page, before the intro.
- CTA at the bottom of the parent page.
- Final line: "Created by [YOUR HANDLE]".

PARENT PAGE
Cover: solid [YOUR BRAND COLOR]
Authority line: [one real proof line from brand-context.md]
Title: [MAGNET TITLE]
Subtitle: [number anchor + proof anchor]
Intro: [1-2 lines on what this is and where to start]
Bottom: [your CTA] and "Created by [YOUR HANDLE]"

SUBPAGES
[List them here from your subtype's body structure. The second to last is
the fill-in page. The last is the CTA.]

FINAL CHECK
Parent page has 5-7 nested subpages. A fill-in page sits second to last.
Brand colour cover. Authority line at top. CTA and credit at the bottom.
No emojis in any subpage title.

---

## AFTER BUILDING

1. Notion -> Share -> Publish to web -> copy the public URL.
2. Paste that URL into your auto-DM tool as the link.
3. Auto-connect OFF. Follow-up DM OFF.

Publish-to-web is correct for a magnet delivery page. A Duplicate link is
a different mechanic for a different job, do not confuse the two.
```

---

## What to do now

1. Get all three files into your setup, plus your `brand-context.md`.
2. Read page 05 for the post, DM and config templates.
3. Read page 06 to see a finished magnet.
4. Build one. Score it on page 07. Ship it.

**One thing worth knowing.** These files change. When a rule gets corrected because something got measured, the repo updates and you pull the new version. That's the reason the files live in a repo rather than as a frozen copy.
