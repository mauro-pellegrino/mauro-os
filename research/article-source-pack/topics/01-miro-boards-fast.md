# Topic 01: building record-ready video boards fast, with Claude

One source document. Juan writes the article from this. Everything below is sourced or marked
`[NEEDS: …]`. Nothing here is invented.

**Status:** evidence is strong, the numbers are missing. Six questions for Mauro at the bottom.

---

## The reader's problem

An agency owner who wants to make video and cannot. The recording is not what stops them. The prep
is. Someone has to turn an idea into something you can actually read off while the camera runs,
and that job lands on them or on a designer who is busy.

So the video does not get made, or it gets made once and never again.

**The promise:** the board is the bottleneck, and the board can be generated.

## What the thing actually is

A Miro board built so a whole video can be read off it to camera without stopping. Big text, laid
out in the order you speak it. Not a slide deck, not a mood board.

The board is generated from a script by code, not placed by hand.

## The mechanism, in order

1. The script exists first, from a transcript or a voice note.
2. Code computes every coordinate, every height and every gap before anything is created.
3. The board is created in one write.
4. A review agent checks it against a fixed list before it is called finished.
5. Mauro records off it.

**Why it is generated and never hand-placed:** diagrams are built in HTML, rendered through
headless Chrome to PNG, and pasted in. Hand-placing shapes for a diagram is banned in the system.
Source: `skills/miro/diagram-style/` in the agency repo, and the standing rule in Mauro's notes.

## The constraints that shaped it, all learned by breaking something

These are the spine of the article. Each one is a real failure with a date.

**The 200-item ceiling.** `layout_update` parses the entire board before it applies any change.
Past 200 items it returns `Line 201: too many items (maximum 200)` and you can no longer edit or
delete anything through the API. `layout_create` still works.

So on a board of real size you get one shot. There is no cleanup pass. Every coordinate has to be
right before the write. Anything that needs removing after that has to be lassoed and deleted by
hand.

Source: `skills/miro/api-gotchas.md`, confirmed 2026-08-04.

**One bad attribute kills the whole batch, silently.** Building the Content Control Panel on
2026-08-03, a 37-item create returned "Created 17 of 37" with HTTP 400 on the other 20. The error
named no item and no attribute.

Worse: the returned DSL showed real URLs for items that had not been created. Trust the failed
list, verify with a board read, ignore the returned DSL on a partial failure.

The cause was two invalid values. `size=383` is rejected, and the sizes that actually write are
144, 288 and 600. A text width of 22,000 is rejected, and 20,000 works.

Source: `skills/miro/api-gotchas.md`, 2026-08-03.

**Deleting is not obvious.** `layout_update` with an empty replacement deletes the matched items,
and a changed x or y on the matched line moves them. Under 200 items that is the whole edit loop.

**A board with placeholders does not count.** A lane that ships with empty boxes where assets
should be is not finished. Assets get requested before the lane is built, not after.

There is a readiness gate with an image-share floor and a script that decides which lanes count as
finished. Source: `skills/miro/lane-readiness.md` and `lane-form-factor.py`, agency repo.

**The board is gated before it ships.** A review agent answers one question through fifteen checks:
can this be read to camera without stopping. Source: Mauro's published article, 2026-09-10.

## The rule worth putting in the title or the close

You get one write. So the work moves from fixing to computing. Everything that would normally be a
cleanup pass has to happen before anything exists.

That is the actual lesson and it generalises past Miro: any system with no undo forces you to be
correct up front, and being correct up front is faster than it sounds.

## What must not go in

- The agency's name, and any client name. It is "the B2B agency I run content and acquisition for".
- Any number not in this file or in `brand/claims.md`.
- A closing summary line. Voice rule.

---

## Questions for Mauro

These are the gaps. The article is weak without at least the first two.

1. **How long does one board take now, start to finish?** The whole claim is "fast as hell" and
   there is no number anywhere in either repo.
2. **How long did it take before, and what was the before?** Hand-placing in Miro, a designer, a
   Canva deck, nothing at all? The contrast is the article.
3. **How many boards a week, and for how long?** There is a standing requirement of four a week.
   Is that the number to use, and since when?
4. **What still breaks?** The gotchas file ends in August. Has anything failed since, and does the
   200-item ceiling still bite in practice or do the boards come in under it now?
5. **Does the board come from a script, or does the board shape the script?** The order matters for
   the reader who wants to copy it.
6. **Is there a public board you would link?** A reader who can open one is worth several
   paragraphs of description.
