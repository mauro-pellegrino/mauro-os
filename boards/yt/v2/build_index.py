#!/usr/bin/env python3
"""Build boards/yt/v2/index.html: one gallery of every v2 board, grouped by video.

Reads <format>/meta.json from each format folder. Doc 11 (the flagship) is built in every
format, so it comes first as the side-by-side format comparison.

    python3 boards/yt/v2/build_index.py
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FORMATS = {
    "a-keynote": "A · Keynote",
    "b-canvas": "B · Canvas flythrough",
    "c-terminal": "C · Terminal / IDE",
    "d-countdown": "D · Ranked countdown",
    "e-whiteboard": "E · Doodle whiteboard",
    "f-casefile": "F · Case file",
}
TOPICS = {
    "01": "Skills to agents", "02": "Skills structure", "03": "Lead magnets in 15 minutes",
    "04": "Outlier swipe corpus", "05": "X ranking code", "06": "Cited inside ChatGPT",
    "07": "Reverse-engineer a channel", "08": "Content working, can't prove it",
    "09": "Transcript to article", "10": "Record off a board",
    "11": "The Claude Code content system (flagship)", "12": "Q3 agents for booked calls",
}

boards = []
for fmt, label in FORMATS.items():
    path = os.path.join(HERE, fmt, "meta.json")
    if not os.path.exists(path):
        continue
    for m in json.load(open(path)):
        m["fmt"], m["fmt_label"] = fmt, label
        boards.append(m)

by_doc = {}
for b in boards:
    by_doc.setdefault(str(b["doc"]).zfill(2), []).append(b)
titles_11 = [t for b in by_doc.get("11", []) for t in b.get("titles", [])]


def esc(s):
    return html.escape(str(s))


def card(b):
    base = os.path.splitext(b["file"])[0]
    cover = f"{b['fmt']}/{base}.cover.png"
    thumbs = f"{b['fmt']}/{base}.thumbs.html"
    has_thumbs = os.path.exists(os.path.join(HERE, thumbs))
    titles = b.get("titles") or ([{"title": t["title"], "modelled_on": t.get("modelled_on", "")} for t in titles_11]
                                 if str(b["doc"]).zfill(2) == "11" else [])
    tl = "".join(f"<li>{esc(t['title'])}<span>{esc(t.get('modelled_on', ''))}</span></li>" for t in titles[:3])
    needs = b.get("needs") or []
    nd = f"<div class='needs'>{len(needs)} NEEDS: {esc('; '.join(needs))}</div>" if needs else ""
    links = f"<a href='{b['fmt']}/{esc(b['file'])}'>Open board</a>"
    if has_thumbs:
        links += f"<a href='{thumbs}'>Thumbnails</a>"
    links += f"<a href='{b['fmt']}/{base}.notes.md'>Notes</a>"
    img = f"<a href='{b['fmt']}/{esc(b['file'])}'><img src='{cover}' loading='lazy'></a>" if os.path.exists(os.path.join(HERE, cover)) else "<div class='noimg'>no preview</div>"
    return (f"<div class='card'>{img}<div class='meta'><div class='fmt'>{esc(b['fmt_label'])}</div>"
            f"<div class='stats'>{b.get('frames', '?')} frames · ~{b.get('minutes', '?')} min</div>"
            f"<ol>{tl}</ol>{nd}<div class='links'>{links}</div></div></div>")


sections = []
for doc in sorted(by_doc, key=lambda d: (d != "11", d)):
    bs = sorted(by_doc[doc], key=lambda b: b["fmt"])
    head = "Same video, every format. Pick the format." if doc == "11" else ""
    sections.append(f"<section><h2><span>{doc}</span>{esc(TOPICS.get(doc, ''))}</h2>"
                    f"<p class='lede'>{head}</p><div class='grid'>{''.join(card(b) for b in bs)}</div></section>")

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>YT Boards v2</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{{--ground:#F7F3EA;--ink:#1B4332;--muted:#5F6B62;--accent:#E9B949;--line:#D8CFBB;--card:#fff}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--ground);color:#1B1B1B;font-family:Inter,system-ui,sans-serif;padding:48px 32px 96px}}
h1{{font-size:56px;font-weight:900;color:var(--ink);letter-spacing:-.03em}}
.how{{margin:14px 0 0;padding:10px 14px;background:#fff;border:2px solid var(--ink);font-size:16px;display:inline-block}}
.sub{{color:var(--muted);margin:10px 0 40px;font-size:18px}}
section{{margin-top:56px}}
h2{{font-size:30px;font-weight:800;color:var(--ink);display:flex;gap:14px;align-items:center}}
h2 span{{font:700 18px 'JetBrains Mono',monospace;background:var(--ink);color:var(--accent);padding:6px 10px}}
.lede{{color:var(--muted);margin:8px 0 18px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:24px}}
.card{{background:var(--card);border:3px solid var(--ink)}}
.card img{{width:100%;display:block;border-bottom:3px solid var(--ink);aspect-ratio:16/9;object-fit:cover}}
.noimg{{aspect-ratio:16/9;display:grid;place-items:center;color:var(--muted);border-bottom:3px solid var(--ink)}}
.meta{{padding:16px 18px}}
.fmt{{font:700 14px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ink)}}
.stats{{color:var(--muted);font-size:14px;margin-top:4px}}
ol{{margin:12px 0 0 18px;font-weight:700;font-size:16px;line-height:1.35}}
ol span{{display:block;font-weight:400;font-size:12px;color:var(--muted);margin-bottom:6px}}
.needs{{margin-top:10px;font-size:12px;color:#B42318;font-family:'JetBrains Mono',monospace}}
.links{{margin-top:14px;display:flex;gap:10px;flex-wrap:wrap}}
.links a{{font-weight:800;font-size:14px;color:var(--ink);background:var(--accent);padding:6px 12px;border:2px solid var(--ink);text-decoration:none}}
@media (max-width:600px){{.grid{{grid-template-columns:1fr}}h1{{font-size:38px}}}}
</style></head><body>
<h1>YT boards v2</h1>
<p class="how"><b>How to use:</b> arrows or Space move, the bar at the bottom has Prev / Next and the frame list. <b>H</b> hides the bar before you record, <b>N</b> shows the notes, <b>F</b> goes fullscreen.</p>
<p class="sub">{len(boards)} boards · {len(set(b['fmt'] for b in boards))} formats · {len(by_doc)} videos. Doc 11 is built in every format.</p>
{''.join(sections)}
</body></html>"""

open(os.path.join(HERE, "index.html"), "w").write(page)
print(f"index.html: {len(boards)} boards in {len(by_doc)} videos")
