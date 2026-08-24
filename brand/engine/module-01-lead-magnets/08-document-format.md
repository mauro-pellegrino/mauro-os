# The Document Format

The second delivery lane. Everything up to here builds the magnet as a workspace someone duplicates. This page builds it as a document someone reads top to bottom, with hand-drawn diagrams carrying the ideas.

Same rules, same system, different container.

---

## When to use a document instead of a workspace

| Use a document when | Use a workspace when |
|---|---|
| The magnet is one argument, read in order | The magnet is a set of things they pick from |
| The value is in the reasoning and the diagrams | The value is in templates they copy out |
| You want it forwardable in one file | You want them to edit inside it |
| You have no landing page yet | You want a home they keep coming back to |

A document travels better. It's one attachment, it opens on a phone, and nothing about it depends on the reader having an account anywhere. That last part matters more than it sounds, because every extra step between the DM and the content loses people.

**The tradeoff, stated plainly:** a document can't be filled in the way a workspace can. You solve that with a fill-in grid drawn as an image, which they screenshot or print. It's weaker than a real editable table and it's still enough to clear the $100 bar.

---

## The layout rules

Copy these exactly. They're what makes it read as a document rather than a slide deck that lost its slides.

1. **One column, cream ground, near-black text.** `#F5EFE4` background, `#171310` text. No white pages.
2. **Headings unbolded and one size up.** The document should look calm. Bold headings read as a landing page.
3. **Paragraphs of one to three sentences.** A wall of text with a diagram under it is still a wall of text.
4. **One diagram per section, full width.** The diagram carries the idea, the paragraph around it says what to do with it.
5. **The diagram never repeats the heading.** If the section is called "They fatigue," the image doesn't say "They fatigue" again.
6. **No page numbers, no header, no footer.** It ends with two grey lines: who made it, and how to reach them.
7. **The last section is the fill-in.** Always. It's the difference between something they read and something they use.

---

## The diagram style

Hand-drawn marker, not infographic. This is the single thing that makes the format feel like a person made it.

- **Line:** near-black `#171310`, 4px, with a rough displacement filter so edges wobble
- **Type:** a handwriting face for everything inside a diagram. Bradley Hand on macOS
- **Fills:** amber `#E0A854` for the one thing that matters, stone `#D8C9B4` for supporting shapes, nothing for the rest
- **One amber per diagram.** If two things are amber, neither reads as important
- **Ground:** the same cream as the page, so the diagram sits on the paper rather than on a card

Three shapes cover almost everything: circles in a chain for a process, bars for a comparison, and a two-column grid for a fill-in.

---

## The build pipeline

No design tool required. The whole thing renders from files.

1. Write the diagrams as SVG. Working generator: `brand/lead-magnets/assets/machine-doc/`
2. Render each SVG to PNG with headless Chrome at 2x:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=WIDTH,HEIGHT --screenshot=out.png wrapper.html
```

3. Write the document as one HTML file, images referenced locally, `@page{size:A4;margin:0}` and the padding on `body` so the cream runs to the edge.
4. Print to PDF with the same binary:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=magnet.pdf file:///path/to/doc.html
```

That's the whole toolchain. The PDF is what you send.

**If you want it as a Google Doc too:** import the same HTML with the images swapped for slot markers, then drag the PNGs in. Google's HTML import drops embedded image data, so the images go in by hand. It's about thirty seconds and it's the only manual step in the format.

---

## The worked example

`brand/lead-magnets/the-lead-magnet-machine.pdf` is a complete magnet built in this format, from Mauro's own answers about how the machine works. Source HTML and the four diagram generators sit next to it.

Read it before you build one. It's shorter than this page and it shows the shape better than the rules do.

---

## The prompt

Paste this after your source material.

```
Build a lead magnet as a document, not a workspace.

Structure:
- One argument, in order, 6 to 8 short sections
- One hand-drawn diagram per section
- Last section is a fill-in grid the reader completes on their own numbers

For each diagram give me: what it shows, the shapes to use
(chain of circles / bars / grid), and which single element is amber.

Rules:
- Paragraphs of 1 to 3 sentences
- The diagram never repeats its section heading
- Real numbers only, from the source material. If a number would help
  and I have not given you one, write [NEEDS: x] and move on
- End with the fill-in, then two lines: who built it, how to reach them
```
