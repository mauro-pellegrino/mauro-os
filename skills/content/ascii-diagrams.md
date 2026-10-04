# ASCII diagrams for articles and carousels

Every diagram in an X article or a carousel can be ASCII: a monospace drawing in a .txt file, rendered into a framed terminal PNG with the handle in the footer. Default handle `@maurojpelle`.

**Use it for:** X articles (in-body diagrams plus the cover), carousels, quote tweets that carry a diagram.
**Do not use it for:** video posts. A video post is a clip cut plus a caption, no diagram.

## Tools

| Tool | What it does |
|---|---|
| `content/ascii/render.py` | One .txt into a framed terminal PNG at 2x. `python3 content/ascii/render.py <file.txt> [@handle] [--cream]`. Writes `.html` and `.png` next to the .txt. Handle defaults to `@maurojpelle`. |
| `content/ascii/build_cover.py` | The 5:2 article cover (3000x1200). `python3 content/ascii/build_cover.py <spec.json>`. Writes `<slug>-cover.png` next to the spec. Sample spec: `content/ascii/covers/_example.json`. |

Leave the existing .txt and .png files in `content/ascii/` as they are. New diagrams for an article go in their own folder.

## Drawing rules

1. **Max 78 columns.** Wider diagrams shrink on a phone until nobody can read them.
2. **Box-drawing characters only:** `┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ─ │`. Arrows are plain `v`, `>`, `->`, `<-`, `^` and `|`.
3. **No emoji, no `▼` or `▲`, no other wide glyphs.** They render wider than one column and break the frame on that line.
4. **Fixed-width boxes.** Build each box from one inner width: pad every content line to that width, and assert no line is longer before you write the file. One long line pushes the right border out.
5. **Verify widths before rendering.** Claude runs this check on every boxed diagram. Every line that starts with a border character must have the same length.

   ```
   python3 -c "import sys; L=[l for l in open(sys.argv[1]).read().split('\n') if l.strip() and l.lstrip()[0] in '┌│└├']; print(sorted(set(map(len,L))))" file.txt
   ```

   One number means the box is square. Two or more means a broken border. Side-by-side boxes of different sizes give one number per box, so check those by eye on the PNG.
6. **Real content only.** Every number on a diagram needs a source, same rule as the copy. A gap is `[NEEDS: x]` in the draft, never a plausible figure.

## Render

- **In-article diagrams render cream:** `python3 content/ascii/render.py <file.txt> --cream`. Cream ground, dark ink, red handle. The dark theme (no flag) is for standalone posts.
- **Open every PNG** with the Read tool after it renders. Check all four borders of every box, that no line wraps, and that the footer handle shows.
- Fix the .txt and render again until every border is clean.

## Files and placement

- Name diagrams in reading order: `01-name.txt`, `02-name.txt`, and so on.
- Plan 4 to 7 diagrams for a long article, plus the cover.
- In the article body, mark each placement on its own line: `[IMAGE: 01-name.png]`.
- Give each diagram one line in the handoff: the file, what it shows, the source of every number on it.

## The 5:2 cover

A dark terminal window on the brand cream, packed with: a Silkscreen pixel headline with an offset amber shadow, a subtitle, a file tree on the left, 1 or 2 ASCII diagrams in the middle (read from .txt files), a 4 or 5 column strip, and a prompt plus handle footer.

Spec keys:

| Key | Required | Notes |
|---|---|---|
| `slug` | yes | Output is `<slug>-cover.png` |
| `title` | yes | The headline. Keep it to two lines at `hsize` 46 to 50 |
| `sub` | yes | One or two lines |
| `cols` | yes | 4 or 5 items: `{"h": "1 SOURCES", "items": ["line", "line"]}`. Keep items short, long ones get cut with an ellipsis |
| `tree` | yes | File tree lines. An empty string is a blank line |
| `mid` | no | Up to 2: `{"file": "x.txt", "from": 0, "to": 12}`. Relative paths resolve next to the spec. Slice on a box boundary, never through the middle of a box |
| `handle`, `user`, `host` | no | Defaults `@maurojpelle`, `mauro`, `ghostedcalls` |
| `bg`, `accent` | no | Defaults `#F5EFE4` cream and `#E0A854` amber from `brand/colors.md` |
| `hsize` | no | Headline size in px, default 50 |

After the render, check the PNG is 3000x1200 (`sips -g pixelWidth -g pixelHeight <png>`) and open it: headline inside the window, strip items not cut, both diagrams whole.

The small card version of a cover (title in a frame, one subtitle line, about 78 x 14) is a normal .txt named `00-cover.txt`, rendered with `render.py`.
