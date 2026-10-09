# BACKLOG archive

What left BACKLOG.md: closed, stale or merged items, verbatim, newest archive on top.
Written by `ops/tools/backlog-archive.py` (growthub-os). Nothing here is counted by the statusline or the morning page.

## Archived 2026-10-09

From BACKLOG.md. Moved verbatim; notes appended as " · closed / STALE / merged / live 09 Oct: why".

### (file header)
# BACKLOG — the standing list for mauro-os

**This file survives session clears. Read it at the start of every session.**

Started 2026-09-06. This is the ghostedcalls / @maurojpelle backlog. The growthub one lives in
`~/growthub-os/BACKLOG.md` and the two do not mix: agency work there, personal brand here.

**How to use it.** Items are `[ ]` open, `[~]` in progress, `[x]` done, `[?]` blocked on Mauro.
A blocked item names what unblocks it. If you close something, tick it and say what happened.
If you find something open that is not here, add it. Nothing auto-closes; ticking is a judgement
call. The statusline reads this file (blocked count, Tier 1 open, total left).

### AT A GLANCE

| Blocked on Mauro | Open | In progress | Done | Tier 1 still open |
|---|---|---|---|---|
| 4 | 16 | 0 | 5 | 9 |

*Counts updated 2026-09-12 after the Gate build (2026-09-11), matched to what the statusline prints. Tier 1 open counts
`[ ]` and `[~]` only, blocked items are counted in their own column. Update them when the list moves.*

**The single objective:** a YouTube engine that runs without Mauro being the bottleneck, feeding
X, where the conversion happens.

---

### IN PROGRESS 2026-10-08 (paused by Mauro)

- [x] Review queue round 3 is open (`~/review-queue/index.html`): GC posts v3, plan v2, animated ASCII. · closed 09 Oct: round 3 decisions arrived 08 Oct (~/review-queue/decisions/2026-10-08-v3.txt), applied in f62c01c
- [x] Plan pivot: Whop one-time paid group for Mauro's skills and systems, then traffic
  (`content/plan/ghosted-calls-plan.html`, `jk-molina-review.md`). Phase 0 = decide ownership of the
  40+ files that also exist in growthub-os. JK: sell one system with a close date. · closed 09 Oct: superseded by content/plan/offer-decision-2026-10-09.md (whole system free on Whop, paid Install Sprint)
- [?] Sign-off: can the 26% / 46% approval rates appear in public posts? · merged 09 Oct: into TOP 25 'Claims sign-off'
- [?] YT boards v2: pick one format (`boards/yt/v2/index.html`), then convert the other 11 videos. · merged 09 Oct: into TOP 25 'YouTube boards v2'
- [x] Lead magnet INTAKE live: GitHub Pages or private claude.ai link? Viability test: without the repo it
  is a calculator plus a prompt; number-parse bug fixed in index.html and in `tools/outlier-score.py`. · closed 09 Oct: superseded: the intake sheet becomes a free tool inside the system (v4 #13, offer decision section 1)
- [x] Animated ASCII tool shipped (`tools/ascii-anim/`), 4 test videos in ~/Downloads; waits on the look verdict. · closed 09 Oct: v3 #1 to #3: animation approved, loop mode built, the process-map long form written (f62c01c); its slot is in TOP 25 'Post W42'
- [ ] Monday 12 Oct: first `/gc-monday` run; `/life-interview` once. · merged 09 Oct: into OFFER BUILD step 8 and TOP 25 'Offer step 8' (with /life-interview)

### NOW — Ghosted Calls phase one: send the Agency Booked Calls offer (set 2026-10-04)

The offer is ready since July (`research/jk-molina/cashie-studio/offer/agency-booked-calls.md`)
and was never sent. Mauro has the message. Decided 2026-10-04: **remove the $300k/mo number**
(it is Lorenzo's and needs his sign-off). 90-minute block per day on this account, before Slack.

- [ ] **Run the prospect finder.** Target = a strong YouTube channel with an offer and a weak or
  missing X / LinkedIn. `! cd ~/mauro-os && YOUTUBE_API_KEY=<key> python3 tools/yt-prospects.py`
  writes `research/yt-prospects/<date>.csv`. Auto mode blocks Claude from reading the key, so
  Mauro runs it. Not run yet. · merged 09 Oct: into OFFER BUILD step 19 and TOP 25 'Direct messages'
- [ ] Pick the top 15 from the CSV. Check each X profile by hand (followers, last post date). · merged 09 Oct: into OFFER BUILD step 19 and TOP 25 'Direct messages'
- [ ] The message for these 15 is cold: open on their video and the missing X / LinkedIn, not
  on "because we've connected before". · merged 09 Oct: into OFFER BUILD step 19 and TOP 25 'Direct messages'
- [ ] Send. Log who was messaged, who answered, the next step, here. · merged 09 Oct: into OFFER BUILD step 19 and TOP 25 'Direct messages'
- [?] **Blocked on Mauro:** the 5-6 agency owners he ghostwrote for and the 2-3 churned contacts
  are not named anywhere in the repo. They are the warmest list. · merged 09 Oct: into OFFER BUILD step 14 and TOP 25 'Offer step 14'
- [?] **Blocked on Lorenzo:** Brando is helped free in Lorenzo's Slack. Talk to Lorenzo first. · live 09 Oct: kept short in BACKLOG.md, TIER 2
- Warm fallback list (people Mauro replied to most on X, May-Aug): LoganTGott (content agency),
  itsmarcosruiz (X agency), Aidanb2b, Dwriteway, AlexHartsuff (coaches agency owners, referral ask).
- [x] **Produced 2026-10-07, drafts, nothing sent or posted, not gated.**
  - Offer page `content/offer/agency-booked-calls.html` (+ `.png` preview): $300k anchor removed,
    ICP from the 17 Aug formalised version, $200/week x 4, 1 founding spot, starts 1 December,
    CTA = email "Booked" to mauro@ghostedcalls.com.
  - 3 nurture emails `content/offer/nurture-emails.md` (idea, problem, sales; day 1-3).
  - Lead magnet `content/lead-magnets/outlier-to-template-intake/`: fill-in HTML (scores posts vs
    the account's median, capture checklist, auto-written Claude prompt, template record, weekly
    pick), LinkedIn post, 1080x1350 image with the INTAKE keyword in the image.
  - Two weeks of posts `content/drafts/2026-10-w42-w43-posts.md`: 10 X, 4 LinkedIn, 2 X articles.
- [x] Run the `gate` agent on the four files above before Mauro reads them. · closed 09 Oct: the W42-W43 drafts were gated by hand (fa16a2f); the offer page now waits for offer step 22 (day-14 higher option)
- [x] Host the offer page and the intake sheet at public URLs (no host, email tool or payment link
  exists). LeadShark needs the sheet URL before LI1 ships on Wed 14 Oct. · closed 09 Oct: superseded: Whop delivers the system (offer decision section 2); the Agency Booked Calls page is the day-14 option
- [ ] Mauro: sign off the 0-of-185 and 57-minute numbers for public posts (new rows in `brand/claims.md`). · merged 09 Oct: into TOP 25 'Claims sign-off'

---

- [x] **Make the planner usable before any content about it** (review 2026-10-08 #55). Mauro: "do
  you think my calendar, planner is actually helping? I don't think I'm even using it, so help me
  use it first". Next step: ask him which one view he would open each morning, then cut the rest.
  No posts or articles about the planner, his hours or his minutes (gate-playbook G-015). · closed 09 Oct: the morning page (~/morning/index.html, tickboxes, built for 9 Oct after v4 #18) is the one view each morning
- [x] **Fix `tools/outlier-score.py` number parsing** ("12.4K" crashes it, "1.2" reads as 12). Same
  bug was fixed in the intake lead magnet on 2026-10-08. Done 2026-10-08: same rule as the HTML,
  self-test with `python3 tools/outlier-score.py --test`.

### TIER 1 — the YouTube video flow (the "own vidIQ")

The end-to-end path is: research picks the topic, titles get drafted, Mauro answers in a voice
note, the transcript becomes the script, the script becomes a record-ready board, Mauro records
raw off the board. Half of this exists as skills. The two ends, research and board creation, are
the parts still done by hand.

**The board end (started today)**

- [x] **Done 2026-09-06.** Miro connected over MCP (`miro-personal`, board read + write scopes).
- [x] **Done 2026-09-06.** First board built end-to-end through the MCP: 59 items, no failures,
  VIDEO 1 of the 2026-07-31 batch. https://miro.com/app/board/uXjVHqG6AzI=/
- [x] **Answered 2026-09-06.** The connected Miro is Mauro's personal team: no spaces, 6 boards,
  all his own. No client boards are reachable, so the automation writes at the team root.
- [x] Mauro reviews that board against `boards/board-video-1-trickle-down.html` and says what the
  MCP version gets wrong. The design-system spec has no yellow-background text widget, so
  narration blocks were built as filled rects; that substitution needs a verdict. · closed 09 Oct: superseded: YT boards v2 (52e2a15, 17 HTML boards in 6 formats) replaced the Miro board path; the format pick is TOP 25 'YouTube boards v2'
- [x] Fold the verdict back into `skills/youtube/miro-design-system.md` as an MCP section, so the
  next board does not re-derive the layout maths (centre axis 1000, the y-stack, the rect-for-
  narration workaround). · closed 09 Oct: superseded: YT boards v2 (52e2a15, 17 HTML boards in 6 formats) replaced the Miro board path; the format pick is TOP 25 'YouTube boards v2'
- [x] Decide the board path: Chrome extension (`skills/youtube/miro-design-system.md`) or MCP.
  Two skills currently describe the same job two ways. One of them should win and the other
  gets marked deprecated. · closed 09 Oct: superseded: YT boards v2 (52e2a15, 17 HTML boards in 6 formats) replaced the Miro board path; the format pick is TOP 25 'YouTube boards v2'
- [x] `brand/scripts/` does not exist. Both Miro skills tell the agent to look there first, so
  step 0 of the board flow fails on a missing folder. The scripts that do exist are buried in
  `research/ideas/2026-07-31-youtube-first-batch/ideas-and-scripts.md` (3 of them, titles locked).
  Decide whether they move to `brand/scripts/` or the skills get repointed. · closed 09 Oct: superseded: YT boards v2 (52e2a15, 17 HTML boards in 6 formats) replaced the Miro board path; the format pick is TOP 25 'YouTube boards v2'
- [x] **Blocked on Mauro:** VIDEO 1's script ends on a DM keyword CTA ("send me youtube on X").
  Per the operating rules that asset has to exist before the video ships. It does not yet. · closed 09 Oct: superseded: the offer decision cuts DM-keyword and comment-to-DM CTAs (section 2, module 01)

- [x] **Done 2026-09-07.** Twelve knowledge docs in `research/video-knowledge/`, one per planned
  video, sourced from both repos. Information first, evidence-tagged, script second. Docs 11 and 12
  are the full system tour and the agent gap it exposes.
- [?] **Blocked on Mauro:** sign off the `$100k/mo` framing in doc 11. It is the organic share of
  the pre-cleared `$300k/mo`, and it is a public number, so it needs his word before it is said on
  camera. `Owner: Mauro · Ask: is "the organic share of a ~$300k/mo agency" the right framing ·
  Unblocks: recording doc 11 · Cost: seconds` · merged 09 Oct: into TOP 25 'Claims sign-off'
- [ ] Mauro picks which of the ten get scripted, and in what order. The docs are ready; nothing
  downstream moves until the order is set. · merged 09 Oct: into TOP 25 'YouTube boards v2'

**The research end (the actual vidIQ part)**

- [ ] Define what the research tool scores. vidIQ scores keywords and outliers; decide what the
  equivalent is here, given the channel goal is subscriber growth on broad B2B, not the tight ICP. · STALE 09 Oct: no movement since 06 Sep
- [ ] `skills/youtube/01-outliers.csv` is a static snapshot. Decide whether it gets refreshed on a
  schedule and by what (YouTube API key is already in the local permissions). · STALE 09 Oct: no movement since 06 Sep
- [ ] Wire the title step to the outlier data. `youtube-title-generator.md` and the Charlie Morgan
  pattern work in `research/charlie-morgan/` are not connected to each other. · STALE 09 Oct: no movement since 06 Sep
- [x] **Superseded 2026-09-07.** The ten titles now exist as ten full knowledge docs with sources
  and evidence tags, in `research/video-knowledge/`. The sign-off question is now which order to
  shoot them in, tracked above.

**The recording end**

- [ ] Thumbnail render mode (`thumb`, 1280x720) is proposed and not built. Working recommendation
  is AI or photo for the image plus an HTML render for the bold text. · STALE 09 Oct: no movement since 06 Sep
- [?] **Blocked on Mauro:** no video has been recorded off a board yet. The flow is unproven until
  one is. · merged 09 Oct: into TOP 25 'YouTube boards v2'

---

### TIER 2 — everything else in mauro-os

**The Gate (built 2026-09-11, `8100d65`)**

The writing rules kept getting skipped because nothing enforced them. Four files shipped:
`.claude/hooks/voice-gate.py` (UserPromptSubmit, injects the rules on any content prompt),
`.claude/agents/gate.md` (four-pass review on sonnet), `brand/claims.md`, and
`skills/content/gate-playbook.md`. Routed in `CLAUDE.md`.

- [ ] **Prove the Gate catches what Mauro rejected.** Run it against the quote-tweet drafts he
  rejected on 2026-09-11. It has to flag the lesson closers, the capitalised product names, and
  "One. Two reads as carelessness." If it passes them, delete the agent and keep the hook. The
  Gate is unproven until this runs, and the hook may already fix the root cause on its own. · STALE 09 Oct: no movement since 11 Sep; the Gate runs by hand (fa16a2f) and the playbook grows (G-018, G-019)
- [ ] **Make the Gate automatic, or accept that it is not.** Today it only runs because
  `CLAIMS.md`-style routing in `CLAUDE.md` tells Claude to call it. A rule of exactly that kind
  got skipped on 2026-09-11, which is what caused the whole problem. A blocking hook would fix
  it. Decide after the test above. · STALE 09 Oct: no movement since 11 Sep; the Gate runs by hand (fa16a2f) and the playbook grows (G-018, G-019)
- [x] **Decide how growthub gets the Gate.** Most content work happens in growthub-os and the
  Gate is only here. Three options: copy it there (the two then drift, which is what already
  happened to `x-article-creator.md`), add a pointer there aimed at this copy, or leave the Gate
  scoped to personal-brand copy only. Recommendation is the pointer, matching
  `x-articles-POINTER.md`. · closed 09 Oct: growthub-os has its own gate agent (.claude/agents/gate.md, listed in its CLAUDE.md)
- [x] **Keep `gate-playbook.md` alive.** Seven entries from one session. It works only if new
  rejections keep arriving as entries. If nothing appends for a month, it is dead weight and
  should be deleted rather than left to rot. · closed 09 Oct: alive: entries up to G-019 on 08 Oct (f62c01c)
- [?] **Blocked on Mauro:** three rows in `brand/claims.md` are marked *needs sign-off*, so the
  CLAIM pass fails any draft that uses them. They are the ~$300k/mo agency figure, the "at least
  a third from the organic accounts he manages" figure, and the $28k deal closed off X. Unblocks
  when Mauro approves each for public use, or tells me to keep them internal. · merged 09 Oct: into TOP 25 'Claims sign-off'

**Visual format: ASCII diagrams (agent trees), set 2026-09-29**

Mauro wants ASCII diagrams in Ghosted Calls content, for Bogdan's and Lorenzo's too (the growthub
side is tracked in `~/growthub-os/research/ideas/content-assets-ideas.md`). An ASCII diagram is a
plain monospace diagram in a dark terminal window, with boxes and arrows drawn from characters. When
it shows who hands work to whom, it is an **agent tree**. Reference:
`research/visual-references/2026-09-29-claude-code-agent-tree-ascii.png` (main session on Opus at
high effort, advisor on call, three subagents at medium, back to main for review). Draft as text,
edit in Monodraw or ASCIIFlow, screenshot in a dark theme.

- **Scope, widened 2026-09-29:** not only agents. Any process, funnel, comparison or framework can be an ASCII diagram. Reference account: Shann Holmberg (@shannholmberg).
- [x] **Use `skills/content/system-extraction.md` for it.** That skill already produces a monospace
  architecture card from a system that runs. Add the terminal-window screenshot style as its visual
  output, so the card and this format are one thing, not two. · closed 09 Oct: superseded by skills/content/ascii-diagrams.md and the 5:2 terminal cover builder (e0a1879)
- [ ] **First one: the Claude Code agent tree Mauro is setting up now.** It sits inside his lane (AI
  content systems that book calls), and it is a system he really runs. Draw it once the setup is
  finished, never before. · live 09 Oct: kept short in BACKLOG.md, TIER 2

**Anti-slop protocol overlap**

- [ ] `skills/content/anti-slop-protocol.md` and `brand/voice.md` ban several of the same things
  (hedging, parallel structures, invented numbers). Two rule files covering one subject is how
  drift starts. Decide whether the protocol folds into `voice.md` or stays separate for its
  quotas and self-audit block, which `voice.md` does not have. · STALE 09 Oct: no movement since early September

---

- [ ] Statusline and worklog hook still point at growthub by config. Statusline was scoped to the
  session's project on 2026-09-06 (`growthub-os@40f0b3f`); the Stop hook still writes every turn
  into `~/growthub-os/ops/daily/`. Decide whether mauro-os gets its own worklog. · STALE 09 Oct: no movement since early September

---

### RESOLVED, do not re-litigate

- **2026-09-06.** The statusline showed growthub's counts in every repo because the path was
  hardcoded while the setting is global. Fixed by walking up from the session cwd to the first
  BACKLOG.md. This file is what the statusline now counts here.
