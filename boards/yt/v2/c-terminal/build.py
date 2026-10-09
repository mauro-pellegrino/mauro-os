#!/usr/bin/env python3
"""Build the format C (terminal / IDE) boards: video-knowledge docs 11 and 05.

    python3 boards/yt/v2/c-terminal/build.py          # HTML, notes, thumbs, meta.json
    python3 boards/yt/v2/c-terminal/build.py --png    # also the cover and thumbs PNGs

Sources. Every number on screen comes from brand/claims.md. Doc 11 terminal output comes from
research/video-knowledge/assets/repo-tree-screen-safe.txt and from real file lines in the agency repo,
redacted (root renamed to agency-os, client and account names replaced with [redacted]). Doc 05 uses the
param.rs block in brand/claims.md (read 2026-10-01); its old "no weights" premise is retired.

Limit. The param.rs pane in video 05 is a defaults view built from claims.md, not a capture of the file.
Its exact source syntax is not reproduced. Capture the real file on the recording day.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import (ACC, BAR, GREEN, MUTED, TXT, chart, columns, cta, esc, file, flow, hbar, page, src, stack,
                    stacked, term, tiles, words)

HERE = os.path.dirname(os.path.abspath(__file__))


def F(sec, t, mins, caption, notes, left, right=None, tabs=(), tab_on=0, on=(), tree=None, needs=(), status=""):
    assert words(caption) <= 8, f"caption over 8 words: {caption}"
    for bad in ("—", "Growthub", "growthub", "Lorenzo", "lorenzo", "300k"):
        assert bad not in json.dumps([caption, notes, left, right], ensure_ascii=False), f"banned string {bad!r} in frame {caption}"
    d = {"sec": sec, "t": t, "mins": mins, "caption": caption, "notes": esc(notes).replace("\n", "<br>"), "left": left,
         "tabs": list(tabs), "tabOn": tab_on, "on": list(on), "needs": list(needs), "status": status}
    if right:
        d["right"] = right
    if tree:
        d["tree"] = tree
    return d


# ====================================================================== VIDEO 11

TREE11 = {"title": "explorer · agency-os", "rows": [
    ["agency-os/", "dir"], ["├─ skills/", "dir"], ["│  ├─ content/", ""], ["│  │  └─ x-articles/", ""], ["│  ├─ research/", ""],
    ["│  ├─ ops/", ""], ["│  ├─ miro/", ""], ["│  ├─ lead-gen/", ""], ["│  ├─ youtube/", ""], ["│  ├─ creative-strategy/", ""],
    ["│  └─ dm-setting/", ""], ["├─ .claude/agents/", "dir"], ["│  ├─ performance-loop.md", ""], ["│  ├─ signal-sweep.md", ""],
    ["│  ├─ board-qa.md", ""], ["│  └─ youtube-lead-magnet.md", ""], ["├─ ops/", "dir"], ["│  ├─ MAP.md", ""],
    ["│  ├─ CONVENTIONS.md", ""], ["│  ├─ tools/", ""], ["│  └─ daily/", ""], ["├─ research/", "dir"],
    ["├─ accounts/  [redacted]", "red"], ["├─ acquisition-calls/", "dir"], ["├─ outbound-calls/", "dir"], ["└─ BACKLOG.md", ""]]}

SKILL_ROWS = list(range(1, 11))
AGENT_ROWS = [11, 12, 13, 14, 15]

TREE_OUT = [
    "[[b:agency-os/]]                     [[dim:the whole operation, one repo]]",
    "├── skills/                    [[dim:73 markdown files, split by activity]]",
    "│   ├── content/  research/  ops/  miro/",
    "│   └── lead-gen/  youtube/  creative-strategy/  dm-setting/",
    "├── .claude/agents/            [[dim:4 installed agents]]",
    "├── ops/",
    "│   ├── MAP.md                 [[dim:the index]]",
    "│   ├── CONVENTIONS.md         [[dim:nine rules]]",
    "│   ├── tools/                 [[dim:25 python scripts]]",
    "│   └── daily/",
    "├── research/  acquisition-calls/  outbound-calls/",
    "├── accounts/                  [[red:[redacted]]]",
    "└── BACKLOG.md",
    "",
    "[[y:73 skills · 4 agents · 25 tools]]   [[dim:counted 2026-09-07]]",
]

AGENDA11 = [
    "## Today we go over",
    "",
    "[[y:01]]  The skeleton: one repo, one map, skills by activity",
    "[[y:02]]  The agents: four of them, and the incident behind each",
    "[[y:03]]  The honesty layer: scripts, limits, evidence tags",
    "",
    "[[dim:Each section: one worked example, one before and after.]]",
]

V11 = [
    # ---------------- HOOK
    F("hook", "0:00-0:10", 0.17, "My whole <em>Claude Code</em> content system",
      "ON SCREEN: the terminal types the tree of the repo. The explorer on the left is the same repo.\n"
      "SAY: This is the whole repo. Every skill, every agent and every script that runs the content and the inbound for the agency I run. "
      "73 skill files, 4 agents, 25 scripts. I'm going to open it folder by folder.",
      term(("tree -L 2 ~/agency-os", TREE_OUT)), tabs=["zsh · agency-os"], on=[0], status="agency-os"),
    F("hook", "0:10-0:20", 0.17, "<em>150+</em> booked calls for the agency, 2026",
      "ON SCREEN: grep pulls the one line from the claims file.\n"
      "SAY: The result first. This system generated over 150 qualified booked calls for the agency this year. "
      "That's the Calendly total. I don't split it by channel, and later in the video I show you why the data can't carry that split.",
      term(("grep -n \"150 qualified\" ~/mauro-os/brand/claims.md",
            ["24:| [[hl:Generated over 150 qualified booked calls for the agency in 2026]]",
             "   | Calendly export, confirmed by Mauro 2026-09-14 | yes, **see the attribution note below** |"])),
      tabs=["zsh · mauro-os"], status="brand/claims.md"),
    F("hook", "0:20-0:30", 0.17, "Repo. Agents. Proof. In that order.",
      "ON SCREEN: the editor opens this video's own notes file at the agenda.\n"
      "SAY: Today we go over three things. The skeleton, so one repo and one map. The four agents, and the thing that broke to create each one. "
      "And the honesty layer, which is the part that makes every number in here traceable.",
      file(AGENDA11, hl=[8, 9, 10], start=6), tabs=["11-claude-code-content-system.notes.md"], status="the agenda"),

    # ---------------- SECTION 1: the skeleton
    F("01 skeleton", "0:30-1:40", 1.17, "One repo. Eleven areas. One map.",
      "ON SCREEN: the full tree, area by area. Highlight moves down the explorer as you name each folder.\n"
      "SAY: One repo. Eleven top-level areas. Skills, agents, ops, research, the accounts, the Monday acquisition calls, outbound, and the backlog. "
      "Each area has an owner and an entry point, and all of them are indexed in one file, ops/MAP.md. "
      "The account folders are blurred on purpose, those are client names.",
      term(("ls ~/agency-os", ["[[b:skills/]]   [[b:.claude/]]   [[b:ops/]]   [[b:research/]]   [[red:accounts/]]",
                               "[[b:acquisition-calls/]]   [[b:outbound-calls/]]   [[b:emails/]]   [[b:brands/]]",
                               "[[b:recaps/]]   [[b:future-projects/]]   BACKLOG.md",
                               "", "[[dim:# eleven areas, one index:]] [[y:ops/MAP.md]]"])),
      tabs=["zsh · agency-os"], on=[0, 1, 11, 16, 21, 22, 23, 24, 25], status="agency-os"),
    F("01 skeleton", "1:40-2:50", 1.17, "Route it, or it gets <em>rebuilt</em>",
      "ON SCREEN: ops/MAP.md, the first lines. The highlight lands on the corollary.\n"
      "SAY: This is the first file any agent reads. It exists because an agent wrote a full outbound reply SOP from scratch, pushed it, "
      "and then found a better one already sitting in outbound-calls. The routing table didn't list that folder, so there was no way to know. "
      "So the rule became: work is finished when it's routed. Read the time lost only if Mauro signs it off.",
      file(["# MAP: read this before building anything",
            "The index. Its one job is to stop an agent rebuilding work that already exists.",
            "**Why it exists:** on 2026-09-01 an agent wrote a full outbound-reply SOP from scratch and pushed it, "
            "then discovered `outbound-calls/` already held a better one. [[red:[NEEDS: time lost]]] of work deleted. [[dim:...]]",
            "**Before writing any new doc, skill, script or SOP: find its owner in this file.** If a body of work is not "
            "listed here, list it. A thing that exists and is not indexed will be rebuilt.",
            "**Corollary: work is not finished until it is routed.** A new skill that is not in `CLAUDE.md` and not here is "
            "invisible, which means it is worse than not existing, because the next agent builds a second one."],
           hl=[9, 11], nums=[1, 3, 5, 9, 11]),
      tabs=["ops/MAP.md"], on=[17], needs=["the 45 minutes lost, not in claims.md"], status="ops/MAP.md"),
    F("01 skeleton", "2:50-3:50", 1.0, "Before: rebuilt. After: found in the map.",
      "ON SCREEN: the before and after as two flows.\n"
      "SAY: Before. A new request comes in, the agent can't see the folder, it builds a second copy, and you only find out after it's pushed. "
      "After. Every request checks the map first. If the thing exists, use it. If it doesn't, build it and add the row in the same session.",
      chart(stack(
          '<div class="tk" style="margin-bottom:10px">BEFORE · 2026-09-01</div>',
          flow([("", "New request", None, ""), ("", "Folder not in the routing table", None, "ghost"),
                ("", "Second copy built", "then found the first one", "hl")], box_h=104),
          '<div class="tk" style="margin:26px 0 10px">AFTER · the MAP rule</div>',
          flow([("", "New request", None, ""), ("STEP 1", "Check ops/MAP.md", None, ""),
                ("FOUND", "Use it", None, ""), ("NOT FOUND", "Build it, add the row", "same session", "hl")], box_h=104), gap=0)),
      tabs=["before-after.svg"], on=[17], status="ops/MAP.md"),
    F("01 skeleton", "3:50-4:50", 1.0, "Every skill folder is an <em>activity</em>",
      "ON SCREEN: eight skill folders, then the count.\n"
      "SAY: 73 skill files across eight folders. Content, research, ops, miro, lead-gen, youtube, creative strategy, dm setting. "
      "Every folder is an activity. There is no folder per client anywhere in skills.",
      term(("ls skills/", ["[[b:content/]]   [[b:research/]]   [[b:ops/]]   [[b:miro/]]",
                           "[[b:lead-gen/]]   [[b:youtube/]]   [[b:creative-strategy/]]   [[b:dm-setting/]]"]),
           ("find skills -name \"*.md\" | wc -l", ["      [[y:73]]   [[dim:# as published 2026-09-10, re-count on the day]]"])),
      tabs=["zsh · agency-os"], on=SKILL_ROWS, status="skills/"),
    F("01 skeleton", "4:50-5:50", 1.0, "A client folder dies with the client",
      "ON SCREEN: two layouts side by side.\n"
      "SAY: Before, you put the skills inside the client. The client leaves, the folder rots, and the next client gets the same skill rebuilt from zero. "
      "After, the skill lives under the activity. It survives every client, and every client makes it better.",
      chart(stack(
          '<div class="tk" style="margin-bottom:10px">BEFORE · split by client</div>',
          flow([("CLIENT A", "skills/case-study.md", "rots when A leaves", "ghost"), ("CLIENT B", "skills/case-study.md", "rebuilt from zero", "ghost"),
                ("CLIENT C", "skills/case-study.md", "rebuilt again", "ghost")], box_h=104, label_size=19),
          '<div class="tk" style="margin:26px 0 10px">AFTER · split by activity</div>',
          flow([("A, B, C", "All clients", None, ""), ("ONE FILE", "skills/content/...", "improved by each", "hl")], box_h=104), gap=0)
          + src("illustration of the folder rule · file names are examples, not repo paths")),
      tabs=["before-after.svg"], on=SKILL_ROWS, status="skills/"),
    F("01 skeleton", "5:50-6:50", 1.0, "Worked example: transcript to article, in order",
      "ON SCREEN: the article skill set.\n"
      "SAY: Here's one skill set opened up. This folder turns any transcript into a published X article. "
      "Six files in a fixed order, a seventh whose only job is to keep the other six honest, a README, and one corpus file.",
      term(("ls skills/content/x-articles/", ["[[y:01-subject.md]]        [[y:02-first-screen.md]]   [[y:03-title.md]]",
                                               "[[y:04-cover.md]]          [[y:05-body.md]]           [[y:06-distribution.md]]",
                                               "[[g:07-improve.md]]        README.md          [[b:_corpus.md]]"])),
      tabs=["zsh · agency-os"], on=[2, 3], status="skills/content/x-articles/"),
    F("01 skeleton", "6:50-7:50", 1.0, "Six steps in order. One keeps them honest.",
      "ON SCREEN: the seven files as a pipeline.\n"
      "SAY: Subject before title. Title and cover get drafted together, as one first screen. Body last, every claim sourced to the input. "
      "Then distribution. And 07-improve runs when new evidence lands, and reconciles the other six.",
      chart(flow([("01", "Subject", "pick 1 of 3-4", ""), ("02", "First screen", "cover + title", "hl"), ("03", "Title", "5 scored", ""),
                  ("04", "Cover", "archetype", ""), ("05", "Body", "every claim sourced", ""), ("06", "Distribution", "companion post", "")],
                 gap=26, box_h=130, label_size=20)
            + '<div style="height:30px"></div>'
            + flow([("07", "Improve", "keeps 01-06 honest as evidence lands", "dark"), ("", "_corpus.md", "every number they cite", "hl")], box_h=104)),
      tabs=["skills/content/x-articles/README.md"], on=[3], status="skills/content/x-articles/"),
    F("01 skeleton", "7:50-8:40", 0.83, "Every number cites <em>one</em> corpus file",
      "ON SCREEN: one number out of the corpus, with its source line.\n"
      "SAY: The corpus is 41 real article captures from 24 accounts. One example of what's in it. "
      "Articles in the 1,800 to 3,000 word band had a median of 225,900 impressions. The 900 to 1,800 band, 73,300. "
      "That's reach across those captures, and it's why the body skill defaults long.",
      chart(hbar([("1,800-3,000 words", 225900, True, "median"), ("900-1,800 words", 73300, False, "median")],
                 fmt=lambda v: f"{v:,.0f}", label_w=330, value_w=300, row_h=96, mono_labels=True)
            + src("median impressions · 41 captures, 24 accounts · brand/claims.md, 'Article evidence'")),
      tabs=["_corpus.md"], on=[3], status="skills/content/x-articles/_corpus.md"),

    # ---------------- SECTION 2: the agents
    F("02 agents", "8:40-9:30", 0.83, "Four agents. Each one is a <em>scar</em>.",
      "ON SCREEN: the agents folder.\n"
      "SAY: A skill waits to be asked. An agent runs without being asked. There are four, and every one of them exists because something got missed.",
      term(("ls .claude/agents/", ["[[y:performance-loop.md]]   [[dim:catches a reach drop before it becomes a quarter]]",
                                    "[[y:signal-sweep.md]]       [[dim:catches an ask buried in a chat thread]]",
                                    "[[y:board-qa.md]]           [[dim:15 gates: is this lane recordable]]",
                                    "[[y:youtube-lead-magnet.md]] [[dim:packages a video into a lead magnet]]",
                                    "", "[[dim:# 4 agents, as published 2026-09-10]]"])),
      tabs=["zsh · agency-os"], on=AGENT_ROWS, status=".claude/agents/"),
    F("02 agents", "9:30-10:40", 1.17, "<em>64%</em> drop. Nobody noticed for two months.",
      "ON SCREEN: the first lines of performance-loop.md. The account name is redacted.\n"
      "SAY: Worked example, agent one. Monthly impressions on one of the accounts fell 64% between June and August, and nobody noticed for two months. "
      "That sentence is literally the first thing the agent reads every time it runs.",
      file(["---", "name: performance-loop", "description: Weekly performance loop. Consolidates the X and Calendly exports, "
            "computes reach and above-floor bookings per account, and flags drops before they become quarters. [[dim:...]]",
            "tools: Bash, Read, Write, Edit, Grep, Glob", "---", "",
            "You are the performance loop. You exist because **[[red:[redacted]]]'s monthly impressions fell 64%",
            "between June and August 2026 and nobody noticed for two months.** Your job is to make that",
            "impossible to repeat."], hl=[7, 8, 9]),
      tabs=[".claude/agents/performance-loop.md"], on=[12], status=".claude/agents/performance-loop.md"),
    F("02 agents", "10:40-11:40", 1.0, "Before: the drop sat unseen",
      "ON SCREEN: June indexed to 100, August at 36.\n"
      "SAY: I only publish the percentage, so this is indexed to June. June is 100. August is 36. "
      "Two months of that, and the weekly numbers looked normal enough that nobody stopped.",
      chart('<div style="display:grid;grid-template-columns:640px 1fr;gap:40px;align-items:center">'
            + columns([("June 2026", 100, False), ("August 2026", 36, True)], width=640, height=440)
            + tiles([("unnoticed for", "2 months", "the reason this agent exists", True)], 1) + "</div>"
            + src("indexed, June = 100 · derived from the published 64% · brand/claims.md")),
      tabs=["impressions-indexed.svg"], on=[12], status=".claude/agents/performance-loop.md"),
    F("02 agents", "11:40-12:40", 1.0, "After: it flags the drop <em>unprompted</em>",
      "ON SCREEN: the flag list in the agent file.\n"
      "SAY: After. Every run, it compares the latest week and month against the trailing four. "
      "And it flags these without being asked. The one in yellow is the one that was missed.",
      file(["## What you flag, unprompted", "",
            "- **Any account down more than 20% on impressions** against its trailing four-week average.",
            "- **Any account down more than 40%** against its own peak month. This is the one that was missed.",
            "- Above-floor bookings down more than 25% month on month.",
            "- A week with zero output on any account.",
            "- Exports that have not been refreshed in over 14 days."], hl=[22], start=19),
      tabs=[".claude/agents/performance-loop.md"], on=[12], status=".claude/agents/performance-loop.md"),
    F("02 agents", "12:40-13:40", 1.0, "A missed ask, in a two-message DM",
      "ON SCREEN: why signal-sweep exists. The target number and the names are redacted.\n"
      "SAY: Agent two. A week's catch-up missed a two-message group DM that held one key number, "
      "and it presented an auto-generated queue as if it were the priority list. Both failures were structural. "
      "Now the agent reads every channel and outputs a ranked list of asks.",
      file(["You keep track of what people actually asked Mauro to do. Chat history is the source, the repo is the memory, "
            "and your output is a ranked list of asks, not a summary of conversations.", "",
            "This exists because on 2026-08-14 a week's catch-up missed a two-message group DM containing "
            "[[red:[redacted: one key number]]], and presented an auto-generated Notion queue as if it were "
            "[[red:[redacted]]]'s priorities. Both failures are structural and this agent is the fix."],
           hl=[10], start=8),
      tabs=[".claude/agents/signal-sweep.md"], on=[13], status=".claude/agents/signal-sweep.md"),
    F("02 agents", "13:40-14:40", 1.0, "15 checks. Can this be read aloud?",
      "ON SCREEN: board-qa on the left, the fifteen gates on the right.\n"
      "SAY: Agent three. Boards were going out full rather than recordable. This one answers one question through fifteen checks: "
      "can this be read to camera without stopping. The first four are blockers, the run stops there. About half run as a script, the rest need eyes.",
      file(["You answer one question: **is this lane recordable?**", "",
            "Not built, not full, not finished. Recordable means [[red:[redacted]]] can sit down, open it, and read the",
            "whole thing to camera without stopping to ask what goes in a grey box or where a number came from."], hl=[7], start=7),
      right=chart('<svg class="chart" width="560" height="330" viewBox="0 0 560 330">'
                  + "".join(f'<g class="bar" style="animation-delay:{k*40}ms"><rect x="{(k%5)*108+4}" y="{(k//5)*98+4}" width="92" height="82" rx="6" '
                            f'fill="{ACC if k<4 else "#12301F"}" stroke="{ACC if k<4 else GREEN}" stroke-width="2.5"/>'
                            f'<text x="{(k%5)*108+50}" y="{(k//5)*98+46}" text-anchor="middle" dominant-baseline="middle" font-family="JetBrains Mono" '
                            f'font-size="28" font-weight="800" fill="{"#0B1A12" if k<4 else TXT}">{k+1}</text></g>' for k in range(15))
                  + "</svg>"
                  + src("gold = blockers, the run stops there · brand/claims.md")),
      tabs=[".claude/agents/board-qa.md"], on=[14], status=".claude/agents/board-qa.md"),
    F("02 agents", "14:40-15:30", 0.83, "Run the skill. Never invent rules.",
      "ON SCREEN: the youtube-lead-magnet agent.\n"
      "SAY: Agent four. Packaging drift: every lead magnet came out a little different. "
      "Its first instruction is to run the existing skill and never invent rules, and to read the skill files fresh every run.",
      file(["You build YouTube video lead magnets for [[red:[redacted]]]. Your job is to run the existing skill, not to "
            "invent rules. The skill files are the single source of truth and are updated often [[dim:...]]"], hl=[8], start=8),
      tabs=[".claude/agents/youtube-lead-magnet.md"], on=[15], status=".claude/agents/youtube-lead-magnet.md"),

    # ---------------- SECTION 3: the honesty layer
    F("03 proof", "15:30-16:30", 1.0, "25 scripts. One per number anyone cites.",
      "ON SCREEN: part of the tools folder.\n"
      "SAY: Section three, the part that keeps it honest. 25 Python scripts. The rule behind them: the analysis that produced a number gets saved as a script. "
      "An inline calculation is gone at the next context clear, and then someone re-derives it slightly differently and the two numbers disagree in a meeting.",
      term(("ls ops/tools/", ["[[y:impressions-vs-calls.py]]   consolidate-exports.py   post-to-call.py",
                              "trace-bookings.py         call-structure.py        article-title-features.py",
                              "lane-tables.py            backlog-sync.py          build-dashboard.py",
                              "[[dim:...]]", "[[dim:# 25 scripts, as published 2026-09-10]]"])),
      tabs=["zsh · agency-os"], on=[19], status="ops/tools/"),
    F("03 proof", "16:30-17:40", 1.17, "Every script states its <em>own limit</em>",
      "ON SCREEN: CONVENTIONS.md, rule 3. A script name is redacted.\n"
      "SAY: Rule three. Every script states its own limit, at the top, in the docstring. "
      "One tool was named as if it measured one account's bookings. It measures all inbound. The docstring now says so in capitals.",
      file(["## 3. Every script states its own limit in its docstring",
            "Not in a comment further down. In the opening docstring, where anyone reading the file sees it first.",
            "**Why:** `[[red:[redacted]]]-article-call-window.py` was named as if it measured one account's bookings. "
            "It measures all inbound bookings, because 649 of 678 Calendly rows sit under one owner and UTM is empty on 673. "
            "The name asserted something the data could not support. The docstring now says so in capitals."],
           hl=[29], nums=[25, 27, 29]),
      tabs=["ops/CONVENTIONS.md"], on=[18], status="ops/CONVENTIONS.md"),
    F("03 proof", "17:40-18:40", 1.0, "<em>649</em> of 678 rows. One owner.",
      "ON SCREEN: the two splits that break channel attribution.\n"
      "SAY: Here's why. 649 of 678 Calendly rows sit under one owner. The UTM field is empty on 673 of them. "
      "So you can't attribute a booking to a channel from this export. That's why I gave you the 150 as a total at the start.",
      chart(stacked([("Calendly rows by owner · 678 total", 678, [("649 under one owner", 649, True), ("29 other", 29, False)]),
                     ("UTM field · 678 rows", 678, [("673 empty", 673, True), ("5 filled", 5, False)])])
            + src("649 of 678 · UTM empty on 673 · brand/claims.md · 29 and 5 are 678 minus the published figures")),
      tabs=["calendly-rows.svg"], on=[18], status="ops/CONVENTIONS.md"),
    F("03 proof", "18:40-19:50", 1.17, "Worked example: the claim that <em>felt true</em>",
      "ON SCREEN: rule one, the three evidence tags.\n"
      "SAY: Rule one. Every claim carries one of three tags: measured, observed, assumed. A claim with no tag gets deleted. "
      "Here's the case that made the rule.",
      file(["## 1. Every claim carries its evidence status",
            "Three tags. A claim with no tag is an assertion and gets deleted on sight.",
            "| `[measured]` | a script and a dataset produced it. Name both | [[dim:...]]",
            "| `[observed]` | seen directly, not quantified | [[dim:...]]",
            "| `[assumed]` | a judgement call, stated as one | [[dim:...]]",
            "**Why:** on 2026-09-01 a skill asserted \"the worked example is the section that converts.\" Measuring it "
            "returned 60,000 against 264,000, the opposite direction. The claim had felt obviously true. "
            "Tagging forces the check before the claim ships."], hl=[15], nums=[5, 7, 11, 12, 13, 15]),
      tabs=["ops/CONVENTIONS.md"], on=[18], status="ops/CONVENTIONS.md"),
    F("03 proof", "19:50-20:50", 1.0, "Before: assumed. After: measured, and <em>reversed</em>.",
      "ON SCREEN: the claimed section against the winning section.\n"
      "SAY: Before, the skill said the worked example was the converting section. It felt obviously true. "
      "After measuring: 60,000 against the winning section's 264,000. The opposite direction. Tagging forces that check before a claim ships.",
      chart(hbar([("worked example (claimed)", 60000, False, None), ("winning section", 264000, True, None)],
                 fmt=lambda v: f"{v:,.0f}", label_w=380, value_w=200, row_h=100)
            + src("brand/claims.md, 'The content system, as published 2026-09-10'")),
      tabs=["measured.svg"], on=[18], status="ops/CONVENTIONS.md"),
    F("03 proof", "20:50-21:40", 0.83, "185 tasks pushed. <em>Zero</em> ticked.",
      "ON SCREEN: the daily task log. Only show this if Mauro clears it, it's an internal ops file.\n"
      "SAY: And the honesty layer applies to me too. From 31 August, Claude pushed five backlog tasks a day into Google Tasks. "
      "37 days, 185 tasks, zero ticked. The plan was fine. The tick never happened, so the loop never closed.",
      term(("ls ops/daily/done/*.json | wc -l", ["      [[y:37]]   [[dim:# 2026-08-31 to 2026-10-06]]"]),
           ("# 5 tasks a day into google tasks", ["[[y:185]] pushed · [[red:0]] ticked"])),
      tabs=["zsh · agency-os"], on=[20], needs=["Mauro clears the 185 / 0 file for public use"], status="ops/daily/"),
    F("03 proof", "21:40-22:30", 0.83, "None of them books a call. <em>Yet.</em>",
      "ON SCREEN: what each agent does, and the empty slot.\n"
      "SAY: Look at the four agents again. One catches a drop, one catches a missed ask, one gates a board, one packages an asset. "
      "All defensive. Nothing in this repo reaches out to a human. That's the next video.",
      chart(flow([("CATCHES", "A reach drop", "performance-loop", ""), ("CATCHES", "A missed ask", "signal-sweep", ""),
                  ("GATES", "A board", "board-qa", ""), ("PACKAGES", "An asset", "youtube-lead-magnet", ""),
                  ("NEXT VIDEO", "Reaches a human", "not built", "ghost")], gap=24, box_h=140, label_size=20)
            + src("brand/claims.md: 'Four agents, all defensive, none reaches out to a human'")),
      tabs=["agents.svg"], on=AGENT_ROWS, status=".claude/agents/"),
    F("cta", "22:30-23:15", 0.75, "Link in the description: <em>Agency Booked Calls</em>",
      "ON SCREEN: the CTA.\n"
      "SAY: Recap in two lines. Copy the corrections, the provenance and the agents first. The prompts come last. "
      "If you run an established agency and you want this built for your own inbound, the link is in the description. It's called Agency Booked Calls.",
      cta("Link in the description", "Agency Booked Calls"), tabs=["zsh · agency-os"], status="agency-os"),
]


# ====================================================================== VIDEO 05

TREE05 = {"title": "explorer", "rows": [
    ["x-algorithm/  (xai-org)", "dir"], ["├─ README.md", ""], ["├─ home-mixer/", "dir"], ["│  ├─ params/", ""],
    ["│  │  └─ param.rs", ""], ["│  ├─ scorers/", ""], ["│  │  └─ weighted_scorer.rs", ""], ["│  └─ ads/", ""],
    ["├─ phoenix/", "dir"], ["│  └─ README.md", ""], ["└─ grox/", "dir"], ["", ""],
    ["the-algorithm/  (twitter, 2023)", "red"], ["", ""],
    ["mauro-os/", "dir"], ["├─ brand/claims.md", ""], ["└─ research/transcripts/", ""],
    ["   └─ 2026-09-04-x-source-code", ""], ["      -myth-buster-thread.md", ""]]}

PARAMS_VIEW = [
    "[[dim:// param.rs · defaults as read 2026-10-01 · X can override per experiment or per user]]",
    "",
    "ShareViaCopyLink                     [[y:20.0]]   [[dim:highest positive in the file]]",
    "Reply                                 5.0",
    "Quote                                 5.0",
    "Retweet                               1.0",
    "Like                                  0.5",
    "ContClickDwellTimeWeight              0.4   [[dim:time after the tap]]",
    "ClickWeight                           0.3   [[dim:the tap]]",
    "OpenLink                              0.2",
    "VideoOpen                             0.07",
    "DwellWeight                           0.05  [[dim:dwell with no tap]]",
    "ContDwellTimeWeight                   0.004",
    "VQV                                   0.0   [[dim:video quality view]]",
    "BidirectionalFollowReplyWeightBoost  15.0",
    "NotInterested                       [[red:-47.52]]",
    "BlockAuthor                         [[red:-31.2]]",
    "MuteAuthor                          [[red:-58.8]]",
    "Report                             [[red:-234.0]]",
]

AGENDA05 = [
    "## Today we go over",
    "",
    "[[y:01]]  The folklore: where the numbers you were quoted come from",
    "[[y:02]]  The weights: every default in param.rs, read line by line",
    "[[y:03]]  What to write for, and what costs you",
    "",
    "[[dim:Each section: one worked example, one before and after.]]",
]

POS = [("ShareViaCopyLink", 20.0, True, "copy link"), ("Reply", 5.0, False, None), ("Quote", 5.0, False, None),
       ("Retweet", 1.0, False, None), ("Like", 0.5, False, None), ("ContClickDwellTime", 0.4, False, "time after the tap"),
       ("Click", 0.3, False, "the tap"), ("OpenLink", 0.2, False, None), ("VideoOpen", 0.07, False, None), ("VQV", 0.0, False, "video quality view")]

PV = "param.rs · defaults view"

V05 = [
    # ---------------- HOOK
    F("hook", "0:00-0:10", 0.17, "I read X's <em>ranking code</em>. Every weight.",
      "ON SCREEN: the defaults from param.rs, copy link highlighted.\n"
      "SAY: These are the ranking weights X uses for the For You feed. Every default, read from the file on 1 October. "
      "Share via copy link is the highest positive in the file, at 20. A like is 0.5.",
      file(PARAMS_VIEW, hl=[3, 7]), tabs=[PV], on=[3, 4], tree="x", needs=["live capture of param.rs on the day"],
      status="home-mixer/params/param.rs"),
    F("hook", "0:10-0:20", 0.17, "Every number you were quoted: <em>2023</em>",
      "ON SCREEN: grep pulls the three folklore numbers out of my own thread.\n"
      "SAY: And these are the numbers everyone quotes. Reply equals 13.5 likes. Repost is 20x. One reply beats 150 likes. "
      "All three are from 2023, from a system X replaced.",
      term(("grep \"2023 number\" 2026-09-04-x-source-code-myth-buster-thread.md",
            ["* \"reply = 13.5 likes\" is a [[hl:2023]] number", "* \"repost = 20x\" is a [[hl:2023]] number",
             "* \"one reply beats 150 likes\" is a [[hl:2023]] number"])),
      tabs=["zsh · mauro-os"], on=[17, 18], tree="x", status="mauro-os"),
    F("hook", "0:20-0:30", 0.17, "Folklore. The weights. What to write for.",
      "ON SCREEN: the agenda in this video's notes file.\n"
      "SAY: Today we go over three things. Where the folklore comes from. The real weights, line by line. "
      "And what that means for what you write, including the four actions that cost you.",
      file(AGENDA05, hl=[8, 9, 10], start=6), tabs=["05-x-ranking-code.notes.md"], tree="x", status="the agenda"),

    # ---------------- SECTION 1: the folklore
    F("01 folklore", "0:30-1:40", 1.17, "Two repos. Three years apart.",
      "ON SCREEN: the timeline of releases.\n"
      "SAY: 2023, Twitter open-sourced the-algorithm, and that release shipped explicit weights. That's where 13.5 and 20x come from. "
      "January 2026, xAI published a new system, x-algorithm. The formula and the scored actions, and no values. "
      "Then on 13 and 14 August, a params file landed with every default. I read it line by line on 1 October.",
      chart(flow([("2023", "twitter/the-algorithm", "explicit weights, replaced", "ghost"),
                  ("JAN 2026", "xai-org/x-algorithm", "formula, no values", ""),
                  ("13-14 AUG 2026", "params/param.rs added", "every default", "hl"),
                  ("1 OCT 2026", "Read line by line", "this video", "dark")], gap=30, box_h=140, label_size=20)
            + src("brand/claims.md, 'The no-weights rule is retired, 2026-10-01'")),
      tabs=["timeline.svg"], on=[0, 12], tree="x", status="two repos"),
    F("01 folklore", "1:40-2:50", 1.17, "A weighted sum of <em>predicted</em> actions",
      "ON SCREEN: the scorer. The weights are named constants pulled from the params module.\n"
      "SAY: The score is a weighted sum. For each action, the model predicts the chance this viewer does it, and multiplies it by a weight. "
      "Then it adds them up. The weights come from one place, the params module.",
      file(["[[dim:// home-mixer/scorers/weighted_scorer.rs · reconstructed from the 2026-08-04 dig]]", "",
            "use crate::params as p;", "",
            "[[dim:// each scored action has a named weight, for example]]",
            "p::REPLY_WEIGHT", "p::RETWEET_WEIGHT", "",
            "[[dim:// final score]]",
            "[[y:score = Σ weight × P(action)]]   [[dim:P = predicted probability for this viewer]]"], hl=[3, 10]),
      tabs=["weighted_scorer.rs"], on=[6], tree="x", status="home-mixer/scorers/weighted_scorer.rs"),
    F("01 folklore", "2:50-3:50", 1.0, "Likes are one scored action <em>of many</em>",
      "ON SCREEN: the scored actions, positive then negative.\n"
      "SAY: Here's what gets scored. Like is in there. So are profile click, follow author, share via DM, share via copy link, dwell time, quoted click. "
      "And four negatives at the bottom. A post that earns a profile visit and a follow works more of the scorer than one that earns a like.",
      term(("# scored actions in weighted_scorer.rs", [
          "[[g:+]] favorite   reply   retweet   photo_expand   click",
          "[[g:+]] [[y:profile_click]]   vqv   share   [[y:share_via_dm]]   [[y:share_via_copy_link]]",
          "[[g:+]] dwell   quote   [[y:quoted_click]]   [[y:dwell_time]]   [[y:follow_author]]",
          "[[red:-]] not_interested   block_author   mute_author   report"])),
      tabs=["zsh · x-algorithm"], on=[6], tree="x", status="home-mixer/scorers/"),
    F("01 folklore", "3:50-5:00", 1.17, "January: no file. August: <em>param.rs</em>.",
      "ON SCREEN: worked example. The same ls, before and after August.\n"
      "SAY: Before. On 4 August I searched the whole tree for the params module the scorer imports. It wasn't there, 404 on every path. "
      "After. On 13 and 14 August, home-mixer/params/param.rs was added. Same command, now it returns the file.",
      term(("ls home-mixer/params/   # as of 2026-08-04", ["ls: home-mixer/params/: [[red:No such file or directory]]",
                                                          "[[dim:# the 2026-08-04 dig: 404 on every params path, no file matching param]]"]),
           ("ls home-mixer/params/   # after 13-14 Aug 2026", ["[[y:param.rs]]"])),
      tabs=["zsh · x-algorithm"], on=[3, 4], tree="x", status="home-mixer/params/"),
    F("01 folklore", "5:00-6:20", 1.33, "My own thread is now <em>out of date</em>",
      "ON SCREEN: post 2 of my own thread from 4 September.\n"
      "SAY: And I have to correct myself. On 4 September I posted that the code gives you zero of the weight values. "
      "That was true of the January release. It's out of date now, and if you check, you'll find that. So I'm saying it first.",
      file(["**2.**", "What the x code actually gives you:", "",
            "* the exact formula, a weighted sum of predicted actions",
            "* the full list of what's scored",
            "* [[strike:zero of the weight values]]   [[red:out of date since 13-14 Aug]]"], hl=[29], start=24),
      tabs=["2026-09-04-x-source-code-myth-buster-thread.md"], on=[17, 18], tree="x", status="my thread, post 2"),

    # ---------------- SECTION 2: the weights
    F("02 weights", "6:20-7:30", 1.17, "Every default, read <em>1 October</em> 2026",
      "ON SCREEN: the full defaults list.\n"
      "SAY: Here's the whole block. Positive actions at the top, the boost, then the four negatives. "
      "Every one of these is a default. X can override any of them per experiment or per user without a release. Keep that in your head for the rest of the video.",
      file(PARAMS_VIEW, hl=list(range(3, 20))), tabs=[PV], on=[4], tree="x",
      needs=["live capture of param.rs on the day"], status="home-mixer/params/param.rs"),
    F("02 weights", "7:30-8:40", 1.17, "Copy link tops the file at <em>20</em>",
      "ON SCREEN: the ten positive weights as bars.\n"
      "SAY: Top to bottom. Share via copy link, 20. Reply and quote, 5. Retweet, 1. Like, 0.5. Time after the tap, 0.4. The tap, 0.3. "
      "Open link, 0.2. Video open, 0.07. And video quality view sits at zero.",
      chart(hbar(POS, label_w=330, value_w=300, row_h=50)
            + src("param.rs defaults, read 2026-10-01 · brand/claims.md 'X ranking weights' · every value is a default")),
      tabs=["positive-weights.svg"], on=[4], tree="x", status="home-mixer/params/param.rs"),
    F("02 weights", "8:40-9:50", 1.17, "A like: 0.5. A copy link: <em>20</em>.",
      "ON SCREEN: worked example, three weights side by side.\n"
      "SAY: Worked example. A like is 0.5. A copy-link share is 20. And a reply from someone you follow back gets a boost of 15. "
      "The file doesn't say whether that boost adds to the 5 or multiplies it, so I won't pick one.",
      chart(tiles([("Like", "0.5", "public and cheap", False), ("ShareViaCopyLink", "20.0", "private and deliberate", True),
                   ("BidirectionalFollowReplyWeightBoost", "15.0", "a reply from a mutual follow", False)], 3)
            + src("adds or multiplies: not stated in the file · brand/claims.md")),
      tabs=["three-weights.svg"], on=[4], tree="x", status="home-mixer/params/param.rs"),
    F("02 weights", "9:50-11:00", 1.17, "Weights multiply <em>predicted probabilities</em>",
      "ON SCREEN: the line in my claims file that records the file's own warning.\n"
      "SAY: Before you start doing maths. These weights multiply predicted probabilities. The file says so in a comment, and it names the misreading: "
      "one report cancels 468 likes. That's wrong. A report sits at minus 234 because a report is rare.",
      term(("grep -n -B1 -A1 \"cancels 468\" brand/claims.md",
            ["135-**The weights multiply [[hl:predicted probabilities, not counts]].** The file says so in a comment and names",
             "136:the misreading itself, that \"one report cancels 468 likes\". A report sits at -234 because a report is",
             "137-far rarer than a like, not because it outweighs 468 of them."])),
      tabs=["zsh · mauro-os"], on=[15], tree="x", status="brand/claims.md"),
    F("02 weights", "11:00-12:10", 1.17, "Time after the tap <em>beats</em> the tap",
      "ON SCREEN: the four dwell params.\n"
      "SAY: Four separate dwell params, and people collapse them. Time after a tap, 0.4. The tap itself, 0.3. Dwell with no tap, 0.05. "
      "The continuous dwell time, 0.004. So the time someone spends after they open your post is worth more than the open.",
      chart(hbar([("ContClickDwellTimeWeight", 0.4, True, "time after a tap"), ("ClickWeight", 0.3, False, "the tap"),
                  ("DwellWeight", 0.05, False, "dwell, no tap"), ("ContDwellTimeWeight", 0.004, False, None)],
                 label_w=400, value_w=330, row_h=82)
            + src("four separate params, never collapse them · brand/claims.md")),
      tabs=["dwell-params.svg"], on=[4], tree="x", status="home-mixer/params/param.rs"),
    F("02 weights", "12:10-13:10", 1.0, "Before: one dwell. After: <em>four</em> params.",
      "ON SCREEN: my September list on the left, the four params on the right.\n"
      "SAY: Before. In September I listed dwell time as one thing to aim for. After reading param.rs, it's four params with very different values. "
      "Quote 0.05 as time after the tap and the advice flips. Write the body for the 0.4.",
      file(["**3.**", "A like isn't what you're looking for", "Focus on generating all engagement:", "",
            "* profile click", "* follow author", "* share via dm", "* share via copy link",
            "* [[y:dwell time]]", "* quoted click"], hl=[39], start=31),
      right=chart(hbar([("after a tap", 0.4, True, None), ("the tap", 0.3, False, None), ("no tap", 0.05, False, None), ("continuous", 0.004, False, None)],
                       width=560, label_w=170, value_w=110, row_h=70, mono_labels=False)
                  + src("param.rs defaults · brand/claims.md")),
      tabs=["2026-09-04-x-source-code-myth-buster-thread.md", PV], on=[17, 18], tree="x", status="my thread, post 3"),

    # ---------------- SECTION 3: what to write for
    F("03 write for", "13:10-14:20", 1.17, "Four actions get <em>subtracted</em>",
      "ON SCREEN: the four negatives, drawn on absolute value.\n"
      "SAY: What costs you. Report, minus 234. Mute author, minus 58.8. Not interested, minus 47.52. Block author, minus 31.2. "
      "Same rule as before: these scale probabilities. Ragebait that provokes mutes and blocks lowers the score mechanically.",
      chart(hbar([("Report", -234.0, True, None), ("MuteAuthor", -58.8, False, None), ("NotInterested", -47.52, False, None),
                  ("BlockAuthor", -31.2, False, None)], label_w=300, value_w=200, row_h=84)
            + src("bars drawn on absolute value · param.rs defaults · brand/claims.md")),
      tabs=["negative-weights.svg"], on=[4], tree="x", status="home-mixer/params/param.rs"),
    F("03 write for", "14:20-15:20", 1.0, "Five posts don't buy five <em>slots</em>",
      "ON SCREEN: the shape of the author diversity decay. Shape only, no values.\n"
      "SAY: Posting more doesn't stack. A diversity function decays your own posts against each other inside one feed response. "
      "It sorts by score, so your best post keeps its value and the weaker ones absorb the decay. You're never zeroed, you're just competing with yourself.",
      chart('<svg class="chart" width="1180" height="360" viewBox="0 0 1180 360">'
            + "".join(f'<g class="bar" style="animation-delay:{k*90}ms"><rect x="{60+k*220}" y="{310-h}" width="150" height="{h}" rx="4" fill="{ACC if k==0 else BAR}"/>'
                      f'<text x="{135+k*220}" y="{290-h}" text-anchor="middle" font-family="Inter" font-size="21" font-weight="700" fill="{TXT}">{lab}</text></g>'
                      for k, (h, lab) in enumerate([(250, "your best post"), (175, "decays"), (135, "decays"), (115, "decays"), (105, "floor")]))
            + f'<line x1="20" y1="310" x2="1160" y2="310" stroke="{MUTED}" stroke-width="2"/>'
            + f'<line x1="20" y1="208" x2="1160" y2="208" stroke="{MUTED}" stroke-width="2" stroke-dasharray="9 8"/>'
            + f'<text x="20" y="342" font-family="Inter" font-size="18" fill="{MUTED}">dashed line: the floor, a post never reaches zero</text></svg>'
            + src("schematic, no data · decay values not verified, so none shown · brand/claims.md thread row 5")),
      tabs=["author-diversity.svg"], on=[2], tree="x", status="author diversity"),
    F("03 write for", "15:20-16:20", 1.0, "Under <em>50,000</em> followers: a test window",
      "ON SCREEN: the four cold start values.\n"
      "SAY: Cold start. Accounts under 50,000 followers. Posts under 200 impressions and under two hours old get tested in feed slots 15 to 16. "
      "Same caveat: defaults, and X can change them without a release.",
      chart(tiles([("follower cap", "50,000", "accounts under this", False), ("impression threshold", "200", "impressions", False),
                   ("max post age", "2 hours", "7,200 seconds", True), ("feed slots", "15-16", "where it gets tested", False)], 2)
            + src("param.rs cold start defaults · brand/claims.md")),
      tabs=["cold-start.svg"], on=[4], tree="x", status="home-mixer/params/param.rs"),
    F("03 write for", "16:20-17:30", 1.17, "No 9am lever. No hashtag lever.",
      "ON SCREEN: the README sentence.\n"
      "SAY: The most useful line in the repo is a sentence. They eliminated every hand-engineered feature, and the model reads the viewer's own engagement history. "
      "So no post-at-9am lever, no hashtag lever, no reply-to-yourself lever. And there's no link filter in the published code. Nothing resurfaces, old posts get removed.",
      file(["[[dim:// xai-org/x-algorithm · README.md]]", "",
            "\"We have eliminated every single hand-engineered feature and most heuristics",
            "from the system. The Grok-based transformer does all the heavy lifting by",
            "understanding your engagement history (what you liked, replied to, shared, etc.)",
            "and using that to determine what content is relevant to you.\""], hl=[3, 4, 5]),
      tabs=["README.md"], on=[1], tree="x", status="README.md"),
    F("03 write for", "17:30-18:40", 1.17, "Replies earned <em>10x</em> the profile visits",
      "ON SCREEN: worked example on my own account, one week.\n"
      "SAY: My own account, 9 to 15 September. 173 replies did 22.5 profile visits per 1,000 impressions. "
      "Four bare article links did 2.2. A profile click is a scored action, and replies are where I earn them. "
      "One week, one account, so it's a read, not a trend.",
      chart(hbar([("173 replies", 22.5, True, "69 visits / 3,072 impressions"), ("4 bare article links", 2.2, False, "5 visits / 2,303 impressions")],
                 label_w=300, value_w=520, row_h=100, fmt=lambda v: f"{v:g} per 1k", mono_labels=False)
            + src("@maurojpelle, 2026-09-09 to 2026-09-15 · 10.2x on the rounded pair · brand/claims.md")),
      tabs=["my-account.svg"], on=[15], tree="x", status="@maurojpelle content export"),
    F("03 write for", "18:40-19:40", 1.0, "Before: the hacks. After: the <em>actions</em>.",
      "ON SCREEN: the before and after for what you write.\n"
      "SAY: Before. Post at 9am, add hashtags, avoid links, post more. None of those exist in the code. "
      "After. Write for the actions that are scored: the profile click into a follow, the share by DM or copy link, and the time after the tap.",
      chart(stack(
          '<div class="tk" style="margin-bottom:10px">BEFORE · the folklore levers</div>',
          flow([("", "Post at 9am", "no lever", "ghost"), ("", "Hashtags", "no lever", "ghost"), ("", "Avoid links", "no link filter", "ghost"),
                ("", "Post more", "decays", "ghost")], gap=24, box_h=104),
          '<div class="tk" style="margin:26px 0 10px">AFTER · the scored actions</div>',
          flow([("SCORED", "Profile click", "into follow", ""), ("20.0", "Copy link", "share", "hl"), ("SCORED", "Share via DM", None, ""),
                ("0.4", "Time after tap", None, "")], gap=24, box_h=104), gap=0)
          + src("brand/claims.md, thread rows 3, 4, 5, 6 and the param.rs block")),
      tabs=["before-after.svg"], on=[15], tree="x", status="what to write for"),
    F("03 write for", "19:40-20:30", 0.83, "Check any claim against <em>the file</em>",
      "ON SCREEN: the check, run live.\n"
      "SAY: Here's how you check any algorithm claim yourself. Open the repo, ask Claude to find the param and quote the line, read the value, and check the date. "
      "If a post quotes a number and the file has a different one, the file wins.",
      term(("claude \"find ShareViaCopyLink in home-mixer/params/param.rs and quote the line\"",
            ["[[dim:Reading home-mixer/params/param.rs ...]]", "ShareViaCopyLink: [[y:20.0]] (default)"])),
      tabs=["zsh · x-algorithm"], on=[3, 4], tree="x", needs=["live capture of this run on the day"], status="home-mixer/params/param.rs"),
    F("cta", "20:30-21:15", 0.75, "Link in the description: <em>Agency Booked Calls</em>",
      "ON SCREEN: the CTA.\n"
      "SAY: The formula is public and so are the defaults. Write for the time after the tap and for the share. "
      "If you run an established agency and you want a content system built on this for your own inbound, the link is in the description. It's called Agency Booked Calls.",
      cta("Link in the description", "Agency Booked Calls"), tabs=["zsh · x-algorithm"], tree="x", status="x-algorithm"),
]


# ====================================================================== notes, thumbs, meta

def notes_md(title, doc, frames, agenda, extra):
    total = sum(f["mins"] for f in frames)
    out = [f"# {title}: presenter notes (format C, terminal)", "",
           f"Source: `research/video-knowledge/{doc}`. Numbers: `brand/claims.md` only. Board: `{doc[:2]}-*.html` in this folder.",
           f"Frames: {len(frames)}. Planned length: about {total:.0f} minutes. Press N on the board to see these notes on screen.", ""]
    out += [l.replace("[[y:", "").replace("[[dim:", "").replace("]]", "") for l in agenda] + [""]
    out += extra + [""]
    import html as _h
    for k, f in enumerate(frames, 1):
        cap = _h.unescape(f["caption"].replace("<em>", "").replace("</em>", ""))
        out.append(f"## {k:02d} · {f['t']} · {f['sec']}")
        out.append(f"**Caption:** {cap}")
        if f["needs"]:
            out.append("**On-screen NEEDS:** " + "; ".join(f["needs"]))
        out.append("")
        out.append(_h.unescape(f["notes"]).replace("<br>", "\n\n"))
        out.append("")
    return "\n".join(out)


THUMBS05 = """<!doctype html>
<html><head><meta charset="utf-8"><title>05 thumbnails</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#333;display:flex;flex-direction:column;gap:20px;font-family:'Inter',sans-serif;width:1280px}
.thumb{width:1280px;height:720px;position:relative;overflow:hidden;background:#0B1A12}
.mono{font-family:'JetBrains Mono',monospace}
.face{position:absolute;right:0;bottom:0;width:420px;height:650px;border:5px dashed rgba(233,185,73,.75);border-radius:20px 20px 0 0;
 display:flex;align-items:flex-end;justify-content:center;padding-bottom:26px;font:700 20px 'JetBrains Mono',monospace;color:rgba(233,185,73,.85);letter-spacing:2px}
/* T1: split weights */
.t1 .half{position:absolute;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;padding-left:70px}
.t1 .a{left:0;width:560px;background:#E9B949}.t1 .b{left:560px;width:300px;background:#12301F}
.t1 .n{font:800 210px 'JetBrains Mono',monospace;letter-spacing:-12px;line-height:.9}
.t1 .a .n{color:#0B1A12}.t1 .b .n{color:#5E8C73;font-size:120px;letter-spacing:-6px}
.t1 .l{font:800 44px 'Inter';letter-spacing:-1px;margin-top:18px}.t1 .a .l{color:#0B1A12}.t1 .b .l{color:#B9CCBF}
.t1 .b{padding-left:40px}
/* T2: editor line */
.t2 .ed{position:absolute;left:50px;top:200px;width:780px;background:#0F2219;border:2px solid #1F3A2C;border-radius:10px;padding:26px 28px;
 font:600 30px/1.75 'JetBrains Mono',monospace;color:#5F7C6B}
.t2 .ed .on{background:#2A2410;color:#fff;margin:0 -28px;padding:0 28px;border-left:6px solid #E9B949}
.t2 .ed .on b{color:#E9B949}
.t2 .h{position:absolute;left:56px;top:56px;font:900 104px 'Inter';color:#fff;letter-spacing:-4px;line-height:1}
.t2 .h em{font-style:normal;color:#E9B949}
.t2 .tab{position:absolute;left:50px;top:166px;font:700 20px 'JetBrains Mono',monospace;color:#86A293}
/* T3: struck folklore */
.t3 .q{position:absolute;left:60px;top:110px;font:800 92px 'JetBrains Mono',monospace;color:#86A293;letter-spacing:-3px;line-height:1.25}
.t3 .q s{text-decoration-color:#F2555A;text-decoration-thickness:12px}
.t3 .big{position:absolute;left:60px;bottom:70px;font:900 150px 'Inter';color:#fff;letter-spacing:-6px;line-height:.9}
.t3 .big em{font-style:normal;color:#E9B949}
.t3 .stamp{position:absolute;left:470px;top:250px;transform:rotate(-8deg);border:8px solid #F2555A;color:#F2555A;font:900 64px 'Inter';padding:4px 22px;border-radius:10px}
</style></head><body>

<div class="thumb t1">
  <div class="half a"><div class="n">20.0</div><div class="l">COPY LINK</div></div>
  <div class="half b"><div class="n">0.5</div><div class="l">LIKE</div></div>
  <div class="face">MAURO CUTOUT HERE</div>
</div>

<div class="thumb t2">
  <div class="h">X <em>WEIGHTS</em></div>
  <div class="ed" style="top:250px;font-size:40px">
    <div class="on">ShareViaCopyLink <b>20.0</b></div>
    <div>Like&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.5</div>
  </div>
  <div class="face">MAURO CUTOUT HERE</div>
</div>

<div class="thumb t3">
  <div class="q"><s>reply = 13.5</s></div>
  <div class="stamp">2023</div>
  <div class="big">IT'S <em>OLD</em></div>
  <div class="face">MAURO CUTOUT HERE</div>
</div>

</body></html>
"""

META = [
    {"doc": "11", "file": "11-claude-code-content-system.html", "titles": [], "frames": len(V11),
     "minutes": round(sum(f["mins"] for f in V11)),
     "needs": ["45 minutes lost to the rebuilt SOP (ops/MAP.md) is not in claims.md, shown as [NEEDS] on frame 5",
               "185 tasks pushed / 0 ticked is marked 'Mauro decides' in claims.md, frame 24 carries a [NEEDS] until he clears it",
               "revenue figure for the title ($100k/mo, $150k MRR, ~$500k) unresolved in doc 11 and absent from claims.md; board uses 150+ booked calls instead",
               "re-count skills, agents and tools on the recording day (published counts 73 / 4 / 25)"]},
    {"doc": "05", "file": "05-x-ranking-code.html",
     "titles": [
         {"title": "I Read X's Ranking Code So You Don't Have To",
          "modelled_on": "research/charlie-morgan/charlie-morgan-dig.md #9, Charlie Morgan, 'I Ranked Every Online Business Model So You Don't Have To' (24K)"},
         {"title": "I Cracked the New X Algorithm (Real Weights)",
          "modelled_on": "skills/youtube/01-outliers.csv, Marcos Ruiz, 'I Cracked The NEW Twitter/X Algorithm' (7,400)"},
         {"title": "X Published Its Algorithm Weights (2026)",
          "modelled_on": "skills/youtube/01-outliers.csv, David Ondrej, 'Google just destroyed all vibe-coding apps (Firebase Studio)' (416,000), the newsjack shape"}],
     "frames": len(V05), "minutes": round(sum(f["mins"] for f in V05)),
     "needs": ["live capture of param.rs on the day (frames 1, 9): the pane is a defaults view built from claims.md, not the file's syntax",
               "live capture of the Claude lookup on frame 21",
               "web search found no X-algorithm YouTube outliers with readable view counts; titles anchor on CSV and Charlie Morgan rows"]},
]

EXTRA11 = ["## Redactions on screen",
           "- Repo root shown as `agency-os/`. Account folders, client and person names show as `[redacted]`.",
           "- The signal-sweep target number is redacted (not in claims.md).",
           "- Agents and tools show the published counts (4 and 25). The live repo now holds more; re-count on the day."]
EXTRA05 = ["## Rules for this video",
           "- Every weight is a default. Say so whenever a value is on screen.",
           "- No deltas (tap 0.4 to 0.3 and the rest), no decay percentages, no pre-30-Sep cold start limits: claims.md marks them unverified.",
           "- The 2023 numbers always carry 2023 in the same line.",
           "- The param.rs pane is a defaults view from claims.md. Swap in a live capture of the file on the day."]


def chrome(args):
    exe = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run([exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=4000"] + args,
                   check=True, capture_output=True)


def main():
    builds = [
        ("11-claude-code-content-system", "My whole Claude Code content system", "11-claude-code-content-system.md", V11, TREE11, AGENDA11, EXTRA11,
         "agency-os · zsh"),
        ("05-x-ranking-code", "I read X's ranking code", "05-x-ranking-code.md", V05, TREE05, AGENDA05, EXTRA05, "x-algorithm · zsh"),
    ]
    for slug, title, doc, frames, tree, agenda, extra, window in builds:
        trees = {"main": tree, "x": tree}
        meta = {"prompt": "mauro@mac %", "tree0": "main", "trees": trees}
        comment = f"Format C terminal board, doc {doc}. Numbers: brand/claims.md only. Built by build.py in this folder."
        with open(os.path.join(HERE, slug + ".html"), "w") as fh:
            fh.write(page(title, comment, window, frames, meta))
        with open(os.path.join(HERE, slug + ".notes.md"), "w") as fh:
            fh.write(notes_md(title, doc, frames, agenda, extra))
        print(slug, len(frames), "frames", round(sum(f["mins"] for f in frames), 1), "min")
    with open(os.path.join(HERE, "05-x-ranking-code.thumbs.html"), "w") as fh:
        fh.write(THUMBS05)
    with open(os.path.join(HERE, "meta.json"), "w") as fh:
        json.dump(META, fh, indent=2, ensure_ascii=False)

    if "--png" in sys.argv:
        for slug in ("11-claude-code-content-system", "05-x-ranking-code"):
            chrome([f"--screenshot={os.path.join(HERE, slug + '.cover.png')}", "--window-size=1600,900",
                    f"file://{os.path.join(HERE, slug + '.html')}?static=1#1"])
        chrome([f"--screenshot={os.path.join(HERE, '05-x-ranking-code.thumbs.png')}", "--window-size=1280,2200",
                f"file://{os.path.join(HERE, '05-x-ranking-code.thumbs.html')}"])
        print("pngs written")


if __name__ == "__main__":
    main()
