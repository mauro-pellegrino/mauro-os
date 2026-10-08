"""Contact sheet of the key before/after screenshots for the review card."""
from PIL import Image, ImageDraw, ImageFont
import pathlib
D = pathlib.Path(__file__).parent
pairs = [("before/A-02-feed-paste.png", "A before: '27 comments' read as nothing, 0 posts scored"),
         ("after/A-02-feed-paste.png", "A after: 11 scored, median 22, 1 capture (the comment-bait post)"),
         ("before/B-01-feed-paste.png", "B before: '2,316 Views' (the 14.7x post) dropped, blank row shifted the link"),
         ("after/B-03-floor-1000.png", "B after, floor set to 1,000 by hand: 2 captures"),
         ("before/B-02-export-paste.png", "B before: X analytics CSV scored Permalink Clicks, median 0"),
         ("after/A-05-own-export.png", "A after: LinkedIn export read by header, note on the unit")]
W = 760; pad = 24; font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
tiles = []
for p, cap in pairs:
    im = Image.open(D / p).convert("RGB"); h = int(im.height * W / im.width); im = im.resize((W, h))
    tiles.append((im, cap))
rows = [tiles[i:i+2] for i in range(0, len(tiles), 2)]
heights = [max(t[0].height for t in r) + 40 for r in rows]
sheet = Image.new("RGB", (W*2 + pad*3, sum(heights) + pad*(len(rows)+1)), "#F5EFE4")
d = ImageDraw.Draw(sheet); y = pad
for r, h in zip(rows, heights):
    for k, (im, cap) in enumerate(r):
        x = pad + k*(W+pad); d.text((x, y), cap, fill="#171310", font=font); sheet.paste(im, (x, y+34))
    y += h + pad
sheet.save(D / "contact.png", optimize=True); print(sheet.size)
