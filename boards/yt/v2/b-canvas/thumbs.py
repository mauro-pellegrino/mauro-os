"""Thumbnail page: 1280x720 each, stacked with a 40px gap. Style follows content/boards/yt-thumbs.html
(deep forest ground, honey accent, sage, a dashed face slot as the only placeholder). Max 4 words each."""

CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#8A8A8A;display:flex;flex-direction:column;gap:40px;font-family:'Inter',sans-serif;width:1280px}
.thumb{width:1280px;height:720px;position:relative;overflow:hidden;background:#0E2418}
.kick{font:700 26px 'JetBrains Mono',monospace;letter-spacing:4px;color:#52B788}
.huge{font-size:132px;font-weight:900;color:#fff;line-height:.88;letter-spacing:-5px;text-transform:uppercase}
.huge em{font-style:normal;color:#E9B949}
.face{position:absolute;right:0;bottom:0;width:430px;height:660px;border:5px dashed rgba(233,185,73,.75);border-radius:20px 20px 0 0;
 display:flex;align-items:flex-end;justify-content:center;padding-bottom:26px;font:700 20px 'JetBrains Mono',monospace;
 color:rgba(233,185,73,.85);letter-spacing:2px;text-align:center}
.mono{font-family:'JetBrains Mono',monospace}
.fold{background:#24503A;border-radius:10px;color:#B7E4C7;font:700 22px 'JetBrains Mono',monospace;display:flex;align-items:center;justify-content:center;border-top:14px solid #52B788}
.fold.on{background:#E9B949;color:#0E2418;border-top-color:#fff}
.card{position:absolute;background:#24503A;border-radius:10px;border:3px solid #3C6B52}
.win{position:absolute;background:#F7F3EA;border-radius:16px;overflow:hidden;border:5px solid #E9B949}
.win .bar{height:46px;background:#1B4332;display:flex;align-items:center;gap:10px;padding:0 18px;font:700 22px 'JetBrains Mono',monospace;color:#E9B949}
.win .r{display:flex;gap:20px;padding:12px 22px;border-bottom:2px solid #E2D9C6;font:700 24px 'JetBrains Mono',monospace;color:#1B4332}
.win .r.bad{background:#B42318;color:#fff}
.needs{display:inline-block;background:#B42318;color:#fff;font:800 92px 'JetBrains Mono',monospace;padding:14px 30px;border-radius:14px;box-shadow:0 0 0 8px #0E2418,0 0 0 16px #B42318}
.tile7{width:110px;height:130px;border-radius:14px;background:#24503A;border:4px solid #52B788;color:#fff;font:900 64px 'Inter';display:flex;align-items:center;justify-content:center}
.tile7.on{background:#E9B949;color:#0E2418;border-color:#fff}
"""


def page(items):
    body = "".join(f'<div class="thumb">{t}</div>' for t in items)
    return ('<!doctype html><html><head><meta charset="utf-8"><title>Thumbnails</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">'
            f'<style>{CSS}</style></head><body>{body}</body></html>')
