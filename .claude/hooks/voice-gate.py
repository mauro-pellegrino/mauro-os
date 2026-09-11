#!/usr/bin/env python3
"""UserPromptSubmit gate: inject the writing rules whenever the prompt asks for content.

Exists because the SessionStart voice.md injection resolves CLAUDE_PROJECT_DIR, which is
wrong whenever a session starts outside the repo (e.g. in ~). It failed silently and drafts
went out without voice.md ever being read. This fires per prompt and resolves the repo by
walking up from this file, so the cwd cannot break it.
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TRIGGERS = re.compile(
    r"\b(tweet|qt|quote[- ]tweet|post|posts|thread|article|caption|hook|hooks|"
    r"script|copy|draft|newsletter|email|dm|dms|autodm|auto-dm|lead magnet|"
    r"linkedin|carousel|headline|title|titles|opener|cta|bio|reply|replies)\b",
    re.IGNORECASE,
)


def section(text, start, end=None):
    i = text.find(start)
    if i == -1:
        return ""
    j = text.find(end, i + len(start)) if end else -1
    return text[i:j] if j != -1 else text[i:]


def main():
    try:
        prompt = json.load(sys.stdin).get("prompt", "")
    except Exception:
        prompt = ""
    if not TRIGGERS.search(prompt):
        return

    voice = os.path.join(REPO, "brand", "voice.md")
    slop = os.path.join(REPO, "skills", "content", "anti-slop-protocol.md")
    try:
        text = open(voice).read()
    except OSError:
        return

    bans = section(text, "## HARD BANS", "## The Voice in One Sentence")
    finishing = section(text, "### Finishing rules", "## The 60-Second Pre-Publish Checklist")

    msg = (
        "CONTENT REQUEST DETECTED. Before writing a single line of copy you MUST read "
        f"{voice} and {slop} in full. Not a summary, the actual files. "
        "Raw X posts follow the tweet types and finishing rules in voice.md, not generic "
        "post structure. Run the anti-slop self-audit before delivering.\n\n"
        "Loaded inline so there is no excuse for skipping it:\n\n"
        + bans
        + "\n"
        + finishing
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": msg,
        }
    }))


if __name__ == "__main__":
    main()
