# BACKLOG — the standing list for mauro-os

**This file survives session clears. Read it at the start of every session.**

Started 2026-09-06. This is the ghostedcalls / @maurojpelle backlog. The growthub one lives in
`~/growthub-os/BACKLOG.md` and the two do not mix: agency work there, personal brand here.

**How to use it.** Items are `[ ]` open, `[~]` in progress, `[x]` done, `[?]` blocked on Mauro.
A blocked item names what unblocks it. If you close something, tick it and say what happened.
If you find something open that is not here, add it. Nothing auto-closes; ticking is a judgement
call. The statusline reads this file (blocked count, Tier 1 open, total left).

## AT A GLANCE

| Blocked on Mauro | Open | In progress | Done | Tier 1 still open |
|---|---|---|---|---|
| 4 | 16 | 0 | 5 | 9 |

*Counts updated 2026-09-12 after the Gate build (2026-09-11), matched to what the statusline prints. Tier 1 open counts
`[ ]` and `[~]` only, blocked items are counted in their own column. Update them when the list moves.*

**The single objective:** a YouTube engine that runs without Mauro being the bottleneck, feeding
X, where the conversion happens.

---

## TIER 1 — the YouTube video flow (the "own vidIQ")

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
- [ ] Mauro reviews that board against `boards/board-video-1-trickle-down.html` and says what the
  MCP version gets wrong. The design-system spec has no yellow-background text widget, so
  narration blocks were built as filled rects; that substitution needs a verdict.
- [ ] Fold the verdict back into `skills/youtube/miro-design-system.md` as an MCP section, so the
  next board does not re-derive the layout maths (centre axis 1000, the y-stack, the rect-for-
  narration workaround).
- [ ] Decide the board path: Chrome extension (`skills/youtube/miro-design-system.md`) or MCP.
  Two skills currently describe the same job two ways. One of them should win and the other
  gets marked deprecated.
- [ ] `brand/scripts/` does not exist. Both Miro skills tell the agent to look there first, so
  step 0 of the board flow fails on a missing folder. The scripts that do exist are buried in
  `research/ideas/2026-07-31-youtube-first-batch/ideas-and-scripts.md` (3 of them, titles locked).
  Decide whether they move to `brand/scripts/` or the skills get repointed.
- [?] **Blocked on Mauro:** VIDEO 1's script ends on a DM keyword CTA ("send me youtube on X").
  Per the operating rules that asset has to exist before the video ships. It does not yet.

- [x] **Done 2026-09-07.** Twelve knowledge docs in `research/video-knowledge/`, one per planned
  video, sourced from both repos. Information first, evidence-tagged, script second. Docs 11 and 12
  are the full system tour and the agent gap it exposes.
- [?] **Blocked on Mauro:** sign off the `$100k/mo` framing in doc 11. It is the organic share of
  the pre-cleared `$300k/mo`, and it is a public number, so it needs his word before it is said on
  camera. `Owner: Mauro · Ask: is "the organic share of a ~$300k/mo agency" the right framing ·
  Unblocks: recording doc 11 · Cost: seconds`
- [ ] Mauro picks which of the ten get scripted, and in what order. The docs are ready; nothing
  downstream moves until the order is set.

**The research end (the actual vidIQ part)**

- [ ] Define what the research tool scores. vidIQ scores keywords and outliers; decide what the
  equivalent is here, given the channel goal is subscriber growth on broad B2B, not the tight ICP.
- [ ] `skills/youtube/01-outliers.csv` is a static snapshot. Decide whether it gets refreshed on a
  schedule and by what (YouTube API key is already in the local permissions).
- [ ] Wire the title step to the outlier data. `youtube-title-generator.md` and the Charlie Morgan
  pattern work in `research/charlie-morgan/` are not connected to each other.
- [x] **Superseded 2026-09-07.** The ten titles now exist as ten full knowledge docs with sources
  and evidence tags, in `research/video-knowledge/`. The sign-off question is now which order to
  shoot them in, tracked above.

**The recording end**

- [ ] Thumbnail render mode (`thumb`, 1280x720) is proposed and not built. Working recommendation
  is AI or photo for the image plus an HTML render for the bold text.
- [?] **Blocked on Mauro:** no video has been recorded off a board yet. The flow is unproven until
  one is.

---

## TIER 2 — everything else in mauro-os

**The Gate (built 2026-09-11, `8100d65`)**

The writing rules kept getting skipped because nothing enforced them. Four files shipped:
`.claude/hooks/voice-gate.py` (UserPromptSubmit, injects the rules on any content prompt),
`.claude/agents/gate.md` (four-pass review on sonnet), `brand/claims.md`, and
`skills/content/gate-playbook.md`. Routed in `CLAUDE.md`.

- [ ] **Prove the Gate catches what Mauro rejected.** Run it against the quote-tweet drafts he
  rejected on 2026-09-11. It has to flag the lesson closers, the capitalised product names, and
  "One. Two reads as carelessness." If it passes them, delete the agent and keep the hook. The
  Gate is unproven until this runs, and the hook may already fix the root cause on its own.
- [ ] **Make the Gate automatic, or accept that it is not.** Today it only runs because
  `CLAIMS.md`-style routing in `CLAUDE.md` tells Claude to call it. A rule of exactly that kind
  got skipped on 2026-09-11, which is what caused the whole problem. A blocking hook would fix
  it. Decide after the test above.
- [ ] **Decide how growthub gets the Gate.** Most content work happens in growthub-os and the
  Gate is only here. Three options: copy it there (the two then drift, which is what already
  happened to `x-article-creator.md`), add a pointer there aimed at this copy, or leave the Gate
  scoped to personal-brand copy only. Recommendation is the pointer, matching
  `x-articles-POINTER.md`.
- [ ] **Keep `gate-playbook.md` alive.** Seven entries from one session. It works only if new
  rejections keep arriving as entries. If nothing appends for a month, it is dead weight and
  should be deleted rather than left to rot.
- [?] **Blocked on Mauro:** three rows in `brand/claims.md` are marked *needs sign-off*, so the
  CLAIM pass fails any draft that uses them. They are the ~$300k/mo agency figure, the "at least
  a third from the organic accounts he manages" figure, and the $28k deal closed off X. Unblocks
  when Mauro approves each for public use, or tells me to keep them internal.

**Anti-slop protocol overlap**

- [ ] `skills/content/anti-slop-protocol.md` and `brand/voice.md` ban several of the same things
  (hedging, parallel structures, invented numbers). Two rule files covering one subject is how
  drift starts. Decide whether the protocol folds into `voice.md` or stays separate for its
  quotas and self-audit block, which `voice.md` does not have.

---

- [ ] Statusline and worklog hook still point at growthub by config. Statusline was scoped to the
  session's project on 2026-09-06 (`growthub-os@40f0b3f`); the Stop hook still writes every turn
  into `~/growthub-os/ops/daily/`. Decide whether mauro-os gets its own worklog.

---

## RESOLVED, do not re-litigate

- **2026-09-06.** The statusline showed growthub's counts in every repo because the path was
  hardcoded while the setting is global. Fixed by walking up from the session cwd to the first
  BACKLOG.md. This file is what the statusline now counts here.
