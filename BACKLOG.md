# BACKLOG — the standing list for mauro-os

**Read it at the start of every session.** Ghosted Calls / @maurojpelle only; Growthub work lives in
`~/growthub-os/BACKLOG.md`. **Objective (set 2026-10-09): first revenue**, cohort 1 of the Install Sprint
(`content/plan/offer-decision-2026-10-09.md`).

## How this file works

1. On top: today's `## <WEEKDAY> DD MON` block when there is one (the morning page reads it), then the OFFER BUILD steps.
2. Then `## TOP 25`, max 25 lines, ranked against first revenue. Each line: owner, effort, the one next action, the source.
3. Then `## TIER 2`, the other live items, one line each. A new item goes in TIER 2 unless it beats a TOP 25 line.
4. Marks: `[ ]` open, `[~]` in progress, `[?]` blocked on Mauro (write `Owner: Lorenzo` when it is his). Close = tick + "closed DD Mon: why".
5. Archive monthly with `~/growthub-os/ops/tools/backlog-archive.py`: closed, stale (3+ weeks, no movement) and merged lines go verbatim to `BACKLOG-archive.md`. Never delete.

## OFFER BUILD (set 2026-10-09)

Decision: `content/plan/offer-decision-2026-10-09.md`, visual `content/plan/product-ladder.html`. The whole
system (YouTube video to content, voice, company brain) is free on Whop. Paid = Install Sprint, one-time,
$197 founding for 10 seats, then $297. No monthly room until the weekly drop runs 4 weeks. Owners: M = Mauro,
C = Claude, J = Juan. Nothing posts or sends without Mauro.

- [ ] 1. Fri 9 Oct, M, 10 min: send the agency ask (text in section 0 of the decision file). Log the answer and the date in `content/plan/ownership-inventory.md`.
- [ ] 2. Fri 9 Oct, M, 5 min: confirm $197 / $297 and 10 seats. Pick the name (working name "The Engine").
- [ ] 3. Fri 9 Oct, C, 45 min: package skeleton + scrub test. `mkdir -p ~/mauro-os/products/engine/claude-code/{brain,skills,tools}`
- [ ] 4. Sat 10 Oct, M, 30 min: Whop store, one free product, one hidden paid product. Check that free-tier gating and file delivery work.
- [ ] 5. Sat 10 Oct, C, 2 h: write `02-video-to-content/run.md` and run it on `research/transcripts/maurojpelle/how-to-create-lead-magnets-with-claude.md`.
- [ ] 6. Sun 11 Oct, C, 2 h: brain templates, the 3-failures prompt, Gate without paths. From `growthub-os/skills/ops/company-brain-install.md`.
- [ ] 7. Mon 12 Oct, C, 1.5 h: module 01 lead magnets, cut LeadShark and comment-to-DM. `grep -rn -i "leadshark\|autodm\|comment" brand/engine/module-01-lead-magnets/`
- [ ] 8. Mon 12 Oct, M, 30 min: first `/gc-monday`. Its output is the first Monday drop.
- [ ] 9. Tue 13 Oct, J, 2 h: stranger test 1 from the README only. Log every stop in `content/qa/engine-stranger-test-1.md`.
- [ ] 10. Tue 13 Oct, C, 1 h: claude.ai Project version, `products/engine/claude-ai-project/instructions.md`.
- [ ] 11. Wed 14 Oct, M, 45 min: record Looms 1, 2 and 6 (list in section 2 of the decision file).
- [ ] 12. Wed 14 Oct, C, 1.5 h: fix every stop from Juan's test. Scrub grep returns 0: `grep -rniE "growthub|lorenzo|bogdan|/Users/mauro|leadshark" products/engine/`
- [ ] 13. Thu 15 Oct, M + C, 1 h: giveaway article + free Whop page in `content/drafts/`. Gate both. Stage only.
- [ ] 14. Thu 15 Oct, M, 15 min: name the warm list (ghostwritten owners, churned contacts).
- [ ] 15 to 23. Weeks 2 to 4: stranger test 2 (J, Project version), the other Looms (M), `tools/monday-read.py` (C), publish after the agency yes (M), one direct message a day (M + J), weekly drop (C), cohort 1 cart with a close date (M), day-14 Agency Booked Calls offer (M), room decision after 4 drops (M + C). Detail in section 4 of the decision file.
- [?] Blocked on Mauro: cohort 1 open date. One option: Mon 26 Oct, after X6, X7, X8 and LI3 run 19 to 21 Oct.

## TOP 25 (ranked 2026-10-09)

Ranked by "first revenue". Steps are the OFFER BUILD numbers above; this list adds owner, next action and source, and
the work outside the offer that feeds it. Owners: Mauro, Claude, Juan.

- [ ] **1. Offer step 1: the agency ask.** Mauro · 10 min · Next: send the text in §0 of the offer decision; log
  the answer and the date in `content/plan/ownership-inventory.md`. Publishing (step 18) waits on this yes. ·
  Src: offer decision §0, review 9 Oct v4 #12.
- [ ] **2. Offer step 2: price and name.** Mauro · 5 min · Next: confirm $197 founding, 10 seats, $297 after, and
  pick the name (working name "The Engine"). · Src: offer decision §1.
- [ ] **3. Offer steps 3 + 5: package skeleton and the video-to-content orchestrator.** Claude · 3 h · Next:
  `mkdir -p ~/mauro-os/products/engine/claude-code/{brain,skills,tools}`, then write `02-video-to-content/run.md`
  and run it on `research/transcripts/maurojpelle/how-to-create-lead-magnets-with-claude.md`. The orchestrator
  does not exist yet and it is the core of the free system. · Src: offer decision §2, v4 #13.
- [ ] **4. Offer step 4: Whop store.** Mauro · 30 min · Next: one free product, one hidden paid product; check that
  free-tier gating and file delivery work (unverified since 22 Aug). · Src: offer decision §2.
- [ ] **5. Post W42 (Mon 12 to Fri 16 Oct).** Mauro · 10 min a day · Next: pick LI2 option A or B (Fri) and the slot
  for the process-map long form. X1 to X5 and Article 1 are approved; LI1 stays on hold. · Src:
  `content/drafts/2026-10-w42-plan.md`, review 8 Oct v3 #19 to #28.
- [ ] **6. Juan's reply rooms.** Juan · 20 min once, then daily · Next: build the private X List "Reply rooms" from
  `docs/juan-x-list-handles.txt` (30 big rooms added 9 Oct) and reply only there. · Src: `docs/juan-reply-brief.md`,
  v4 #4 (151 replies since 1 Sep, 1 follow).
- [ ] **7. Offer steps 6 + 7: brain port and module 01 rewire.** Claude · 3.5 h · Next: 5 blank brain templates and
  the 3-failures prompt from `growthub-os/skills/ops/company-brain-install.md`; then cut LeadShark and comment-to-DM
  from `brand/engine/module-01-lead-magnets/`. · Src: offer decision §2, §4.
- [ ] **8. Offer step 8: first /gc-monday, Mon 12 Oct.** Mauro · 30 min · Next: run `/gc-monday`; its output is the
  first Monday drop. Run `/life-interview` once the same week. · Src: offer decision §4, IN PROGRESS 8 Oct.
- [ ] **9. Offer steps 9 + 12: stranger test 1, then the fixes.** Juan 2 h, Claude 1.5 h · Next: Juan installs from the
  README only and logs every stop in `content/qa/engine-stranger-test-1.md`; Claude fixes them and runs the scrub
  grep to 0. · Src: offer decision §4.
- [ ] **10. Offer step 10: claude.ai Project version.** Claude · 1 h · Next:
  `products/engine/claude-ai-project/instructions.md`. Both stranger personas use a browser, not a terminal. · Src:
  offer decision §2, `intake-viability-v2.md`.
- [ ] **11. Offer step 11: Looms 1, 2 and 6.** Mauro · 45 min · Next: record them (list in §2 of the offer decision).
- [ ] **12. Offer step 13: giveaway article and the free Whop page.** Mauro + Claude · 1 h · Next: draft both in
  `content/drafts/`, Gate both, stage only. · Src: offer decision §1 point 5.
- [?] **13. Offer step 14: name the warm list.** Mauro · 15 min · Next: name the 5 to 6 agency owners he ghostwrote
  for and the 2 to 3 churned contacts. Blocked since August. · Src: offer decision §4, NOW block 4 Oct.
- [ ] **14. Direct messages, one a day each (offer step 19).** Mauro + Juan · 15 min a day · Next: Mauro runs
  `YOUTUBE_API_KEY=<key> python3 tools/yt-prospects.py` (Claude cannot read the key), picks the top 15, checks each
  X profile, opens on their video. Warm fallback: LoganTGott, itsmarcosruiz, Aidanb2b, Dwriteway, AlexHartsuff. ·
  Src: NOW block 4 Oct, offer decision §4.
- [?] **15. Claims sign-off for public posts.** Mauro · 5 min · Next: rule on each "needs sign-off" row in
  `brand/claims.md`: ~$300k/mo agency, "a third from organic", the $28k deal, the $100k/mo framing (doc 11),
  0-of-185, 57 minutes, the 26% / 46% approval rates (X4 "first-pass approval rate" was approved in v3 #21). ·
  Src: Gate block 11 Sep, NOW block 7 Oct, IN PROGRESS 8 Oct.
- [ ] **16. W43 posts (19 to 23 Oct).** Mauro · 10 min a day · Next: X9, X10 and Article 2 are approved; LI3 is dated
  W43; Thu 22 LinkedIn is empty (LI4 killed). Cohort 1 timing depends on X6 to X8 and LI3. · Src:
  `content/drafts/2026-10-w42-w43-posts.md`, v3 #22, #23, #25, #27.
- [?] **17. YouTube boards v2: pick one format, record one video.** Mauro · 10 min to pick · Next: pick in
  `boards/yt/v2/index.html`, then record the first video off a board (none recorded yet). A recorded video is the
  input of the whole system. · Src: IN PROGRESS 8 Oct, Tier 1 "the recording end".

## TIER 2 — live, below the top 25

- [?] Brando is helped free in Lorenzo's Slack: talk to Lorenzo before any offer to him. Owner: Lorenzo.
- [ ] First ASCII agent tree: draw the Claude Code agent tree once the setup is final (`skills/content/ascii-diagrams.md`).

## AT A GLANCE

| Blocked on Mauro | Open | In progress | Done | Tier 1 still open |
|---|---|---|---|---|
| 5 | 30 | 0 | 0 | 14 |

*Counted by hand 2026-10-09 with the statusline's regex. Tier 1 = the TOP 25 open lines. Update it when the list moves.*

Archive: `BACKLOG-archive.md` (everything closed, stale or merged on 09 Oct, verbatim).
