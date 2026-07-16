# Juan — Visual Docs Tutorial

How to make Mauro's visual content inside the "Mauro Visual Docs" project on claude.ai. Read this once, keep it open for your first few docs.

**The one rule that matters most:** you produce, Mauro approves. Nothing you make gets posted. You build it, send Mauro the files, he decides. Never post, never DM, never publish.

---

## What this project makes

Two types of visual content. Every job is one or the other. Figure out which before you start.

### Type 1 · SOCIAL HTML (for LinkedIn + X)

Polished, on-brand infographic images that go into a post. Fixed sizes so they fit the feed. This is the quote-tweet infographic play: an article goes out, then a few hours later it gets quote-tweeted with one of these.

- Looks: clean, green brand.
- Sizes: `square` (1080×1080), `portrait` (1080×1350, the default), `long` (1080×1620).
- You get back: a PDF (for LinkedIn carousels) and PNG images (for X / IG).

### Type 2 · BOARDS (for YouTube)

A long, tall breakdown board with lots of space, the kind Mauro builds in Miro: dark green header bars, mint item cards, green labels, arrows, and slots where Mauro's own screenshots get pasted in. Built to be recorded in a video and easy to edit.

- Looks: green cards on a cream background (with a touch of honey/gold for anything that needs to stand out).
- Size: one long vertical page, as tall as the content needs.
- You get back: one tall PDF and one tall PNG.

If you're unsure which type a job is, ask Mauro before building. Don't guess.

---

## How to work in the project

You don't touch code. You talk to Claude in the project, it builds the HTML, runs the render, and hands back the PDF + PNG. Your job is to give it the right content and check the result against the rules.

### Making a SOCIAL doc

1. Open a new chat in the project.
2. Paste the source (an article, a script, or notes) and say what you want:
   > "Build a portrait social carousel from this article: [paste]"
   > or "Make a square QT-reaction infographic for this: [paste]"
3. Claude picks the layout, writes the copy to Mauro's voice, and renders it.
4. Check it against the voice rules and the checklist below.
5. Send Mauro the PDF + PNG in chat for approval. Note which type and size it is.

### Making a BOARD

1. Open a new chat in the project.
2. Give Claude the breakdown content and tell it which images go where:
   > "Build a board breaking down [topic]. Sections: [list]. I'll paste in a screenshot of the account near the top and a row of 5 ad thumbnails in the formats section."
3. Claude builds the board with your text in the cards and **image slots** where your screenshots go, using dashed placeholder boxes for images that aren't in yet.
4. For the images: Claude puts them in an `images/` folder and references them by name (like `images/account.png`). Give Claude the image files, or tell Mauro which screenshots are needed. Once the images are in, Claude re-renders.
5. Check it, then send Mauro the PDF + PNG for approval.

**Boards are meant to be edited.** If a card's wording is off or the order is wrong, just tell Claude "swap card 2 and 3" or "reword the second item card" and it re-renders. Don't rebuild from scratch.

---

## The voice rules (memorize these)

These are Mauro's hard rules. Claude follows them, but you're the check. If you see any of these in the output, send it back or fix it before it reaches Mauro.

- **No em dashes (—).** Ever. Commas, periods, or parentheses instead. (The only allowed one is the footer signature `— Mauro`.)
- **No "not X, but Y" / "it's not X, it's Y" / "X, not Y"** style contrast lines. Just say the thing.
- **No "most agencies / most people do X" openers.**
- **No hype words:** "insane", "wild", "crazy", "game-changing". (One exception: the "Claude is INSANE for [X]" line is a deliberate hook Mauro uses in auto-DMs. Leave it if it's that.)
- **No made-up numbers.** Only real numbers, or a placeholder like `[X%]`. The only public number you can use is Growthub ~$300k/mo. Any other specific number needs Mauro's OK first.
- **No trailing summary line** at the end that repeats the point. End on the point.
- **Never name a client** in anything. If a real client is involved, keep them unnamed.

---

## Checklist before you send anything to Mauro

- [ ] Right type (social vs board) and right size for where it's going
- [ ] No em dashes, no "not X but Y", no "most people" openers
- [ ] No hype adjectives, no invented numbers, no client names
- [ ] Handle reads `@maurojpelle`, footer reads `— Mauro`
- [ ] Social: no text cut off, images look sharp
- [ ] Board: all images show up (or there's an intentional placeholder), no big empty gaps, cards centered
- [ ] CTA (if any): social ends with "DM me [keyword]"; a YouTube board's CTA points to X, never "subscribe"

---

## First-week guardrails

- **You produce, Mauro approves.** No posting, no DMs, no live comments, no offer mentions.
- **Only approved public number:** Growthub ~$300k/mo. Nothing else.
- **When Claude writes something that sounds off,** trust the voice rules over the draft. Send it back.
- **When in doubt about the type, the content, or a number,** ask Mauro before building. Better a quick question than a rebuild.

---

## Your first task (walk through it)

1. Ask Mauro for one article or breakdown topic to start with, and whether he wants it as a social doc or a board.
2. Build it in the project following the steps above.
3. Run it against the checklist.
4. Send Mauro the PDF + PNG in chat, tell him the type and size, and ask for notes.
5. Apply his notes, re-render, resend. That loop (build → notes → fix) is the whole job in week one.
