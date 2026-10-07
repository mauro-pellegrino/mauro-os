"""Thumbnails for the case-file boards: 1280x720 each, max 4 words, the face slot is the only placeholder."""
import html

CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#777;display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0;font-family:'Inter',sans-serif}
.th{width:1280px;height:720px;position:relative;overflow:hidden;
 background:radial-gradient(rgba(255,255,255,.04) 1px,transparent 1.6px) 0 0/9px 9px,radial-gradient(ellipse at 40% 40%,#2f3d36 0%,#18201c 70%,#0f1411 100%)}
.face{position:absolute;right:0;bottom:0;width:400px;height:640px;border:5px dashed rgba(233,185,73,.8);border-radius:20px 20px 0 0;
 display:flex;align-items:flex-end;justify-content:center;padding-bottom:24px;font:700 19px 'JetBrains Mono',monospace;color:rgba(233,185,73,.9);letter-spacing:2px}
.ex{position:absolute;box-shadow:0 18px 36px rgba(0,0,0,.55)}
.pin{position:absolute;top:-16px;left:calc(50% - 16px);width:32px;height:32px;border-radius:50%;z-index:3;
 background:radial-gradient(circle at 35% 32%,#fff6d6 0 12%,#E9B949 30%,#9a7418 100%);box-shadow:0 5px 7px rgba(0,0,0,.55)}
.paper{background:#F7F3EA;padding:30px 34px}
.card{background:repeating-linear-gradient(#fffef9 0 45px,#cfdfe8 45px 47px);border-top:12px solid #d9534f;padding:26px 34px}
.folder{background:#E2C88E;padding:36px 40px;border-radius:0 10px 6px 6px}
.word{position:absolute;font:900 112px/.9 'Inter';letter-spacing:-.045em;color:#fff;text-transform:uppercase;text-shadow:0 6px 18px rgba(0,0,0,.6)}
.word em{font-style:normal;color:#E9B949}
.stamp{position:absolute;border:7px double currentColor;padding:8px 18px 6px;font:400 54px/1 'Special Elite',monospace;letter-spacing:.05em;
 background:rgba(247,243,234,.9);border-radius:6px;transform:rotate(-10deg);z-index:4}
.m{color:#1F6B45}.o{color:#A8650F}.r{color:#C62828}
svg text{font-family:'Inter',sans-serif}
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800;900&family=JetBrains+Mono:wght@700"
         "&family=Special+Elite&family=Caveat:wght@700&display=swap")


def page(title, thumbs):
    body = "\n".join(f'<div class="th" id="t{i+1}">{t}<div class="face">MAURO CUTOUT HERE</div></div>' for i, t in enumerate(thumbs))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)} · thumbnails</title>'
            f'<link href="{FONTS}" rel="stylesheet"><style>{CSS}</style></head><body>{body}</body></html>')
