# Ownership inventory: what Mauro can sell

Phase 0 of `content/plan/ghosted-calls-plan.html`. Built 2026-10-08.

**Scope:** every file in mauro-os `skills/`, `tools/`, `.claude/`, and the global `~/.claude/skills/`,
matched against `/Users/mauro/growthub-os`.

**Evidence:** `tools/ownership/twin-scan.py`, output in `tools/ownership/twin-scan.csv`. One row per file:
twin path in growthub-os, lines that differ, first commit in each repo, count of agency names.

**Limit of the scan:** it matches by file name only. A file renamed between the repos shows no
twin. Four renames were found by hand and are in the table (`render_one.py`, `content-sweep.md`,
`first-messages.md`, `outlier-score.py`). Others can exist.

This is a reading of git history and file contents. It is not a legal view. The agency has the
final word on anything built while Mauro works there. `[NEEDS: Mauro asks the agency, per system]`

---

## The answer

**4 systems are clean, 6 are mixed, the rest are Growthub's or third-party.**

- Clean: the ASCII visuals kit, the Gate, the voice extraction method and the profile study set. All four started in mauro-os and have no growthub-os twin, or the growthub-os copy cites mauro-os as its source.
- The system the plan and the JK review put first, outlier to template, is **mixed**. Its scorer landed in growthub-os two days before mauro-os.
- 46 of 99 mauro-os text files have a twin in growthub-os. 40 were first committed on 2026-07-13, in the commit "Initial extraction from growthub-os" (`1d723dc`). 36 of the twins are older in growthub-os than that date.
- `growthub-os/ops/MAP.md` line 84 says: "`growthub-os` is canonical for skills. `mauro-os` (ghostedcalls) holds @maurojpelle's voice and points at the canonical skills rather than copying them". The agency repo claims the shared skills in writing.

---

## How each row is classified

| Class | Rule |
|---|---|
| **Sellable** | First commit in mauro-os after 2026-07-13, no growthub-os twin (or the twin cites mauro-os), no third-party source |
| **Mixed** | The method is Mauro's, but code landed in growthub-os first, or it reads agency paths, or a co-author must agree. Needs a clean rebuild and a yes |
| **Not sellable** | The growthub-os twin predates 2026-07-13, or the file holds agency names, data or service work, or it is a third-party pack |

---

## The table

| # | System | Files | Class | Evidence |
|---|---|---|---|---|
| 1 | ASCII visuals kit (diagram renderer, 5:2 cover, animation) | `content/ascii/render.py`, `content/ascii/build_cover.py`, `skills/content/ascii-diagrams.md`, `skills/content/ascii-article.md`, `tools/ascii-anim/` | **Sellable** | `render.py` first commit 2026-09-30 in mauro-os. growthub-os calls it by absolute path: `brands/growthub/article-media/scripts-scaling/ascii/build.py` line 5. No twins. `ascii-article.md` is a port (`fbcfb40`, 2026-10-04) after the ASCII articles for Lorenzo (growthub-os, 2026-10-02): keep the skill, drop every Lorenzo example. `ascii-anim/README.md` line 17 uses a Growthub founder's handle as the example |
| 2 | The Gate (review agent + hook + rejections log + claims file) | `.claude/agents/gate.md`, `.claude/hooks/voice-gate.py`, `skills/content/gate-playbook.md`, the `brand/claims.md` pattern | **Sellable** (as a pattern) | mauro-os `gate.md` first commit 2026-09-11. growthub-os `gate.md` first commit 2026-09-30, and its line 11 says "Modelled on the mauro-os Gate". `gate-playbook.md` holds Mauro's own rejections: ship a blank one plus a scrubbed example |
| 3 | Voice extraction method | `skills/research/voice-extraction.md` | **Sellable** | First commit 2026-08-06, no twin. The method is his. The output it replaced, `brand/voice.md`, is a fork of the agency's voice doc (`voice-extraction.md` lines 13-15: "124 of 360 lines differ"). `brand/voice.md` stays out |
| 4 | Profile study set | `skills/research/profile-extraction.md`, `profile-study.md`, `article-corpus.md` | **Sellable** | First commits 2026-09-15 to 09-17, no twins. `profile-study.md` names a collaborator 3 times and `article-corpus.md` has 1 private path: scrub |
| 5 | Outlier to template intake | `skills/research/template-intake.md`, `tools/outlier-score.py`, `research/tracked-profiles.csv`, `content/lead-magnets/outlier-to-template-intake/` | **Mixed** | Method source is Mauro's own Loom (`research/transcripts/maurojpelle/2026-08-28-how-to-save-outlier-x-articles-loom.md`), recorded before the agency map. Code: `growthub-os/ops/tools/outlier-score.py` first commit 2026-10-02 ("Speed-up #3"), mauro-os port 2026-10-04 (`fbcfb40`), 20 lines differ. The rules came from the agency process map: the 10x line is credited to "Paolo" in `growthub-os/ops/process-maps/README.md` line 37. The process map was "Lorenzo asked for a map" (same file, line 3). Mauro's own offer page frames the intake as part of "the engine I built and run for a B2B agency" (`content/offer/agency-booked-calls.html`) |
| 6 | Process maps | `skills/ops/process-maps.md`, `tools/process-maps/` | **Mixed**, leaning Growthub | growthub-os `ops/process-maps/` first commit 2026-10-01, built at Lorenzo's request. mauro-os copy 2026-10-04. `build_grouped.py` differs by 230 lines, `ranked_queue.py` by 43 |
| 7 | Review queue + approval-rate loop | `~/.claude/skills/review-queue/` (SKILL.md, build.py) | **Mixed** | Lives outside both repos. SKILL.md reads the Growthub Notion staging page (line 20), Growthub media folders (line 22), Growthub exports (line 41) and card types per Growthub founder (line 65). The builder is general |
| 8 | Week calendar | `~/.claude/skills/week-calendar/` | **Mixed** (light) | His. SKILL.md line 38 splits hours between growthub-os and mauro-os. The paths must become settings |
| 9 | X analytics scripts | `tools/maurojpelle-baseline.py`, `maurojpelle-traffic.py`, `x-three-accounts.py`, `x-follow-drivers.py`, `x-keywords.py`, `x-autoplugs.py` | **Mixed** | All first committed 2026-10-05 to 10-08 in mauro-os. The four `x-*` scripts read the Growthub founders' exports (2 to 3 agency mentions each). The method is general; the inputs are agency data |
| 10 | X reply assistant + content analytics review | `skills/content/x-reply-assistant.md`, `x-replies-prompt.md`, `x-reply-mobile-prompt.md`, `.claude/commands/reply.md`, `skills/ops/content-analytics-review.md/.py` | **Mixed** (co-author) | No twins. First commits by `jlago-del <jlago@ghostedcalls.com>` (2026-08-14 to 08-25), the second ghostedcalls account in the log (132 of 282 mauro-os commits). `[NEEDS: confirm this is Juan, and that his work is assigned to Ghosted Calls]` |
| 11 | Lead magnet system ($500 product of 22 Aug) | `skills/lead-gen/lead-magnet/` (7 files), `brand/engine/module-01-lead-magnets/` (9 pages, 1,901 lines) | **Not sellable as it is** | All 7 skill files exist in growthub-os `skills/lead-gen/lead-magnet/`; the 6 matched by the scan have twins from 2026-05-26 to 06-25. The proof in it comes from an account Mauro runs for the agency (`research/jk-molina/cashie-studio/offer/lead-magnet-system-500.md`, "Constraint"). Delivery is comment-to-DM (35 mentions of comment, autodm or LeadShark in the module), which stopped after the X automation bans (Wiz call, 2026-08-28) |
| 12 | Long-form, short-form, LinkedIn docs, miro-to-article, x-article-creator | `skills/content/long-form/` (5), `short-form/` (2), `linkedin-docs/`, `miro-to-article.md`, `x-article-creator.md` | **Not sellable** | Twins in growthub-os from 2026-03-05 to 07-06. mauro-os copies are rewrites (46 to 825 lines differ) of agency files. A yes from the agency moves them to Mixed |
| 13 | YouTube pipeline | `skills/youtube/` (11) | **Not sellable** | 8 twins in growthub-os from 2026-03-04 to 04-10. Of the other 3, two came in with the YouTube research batch (`jlago-del`, 2026-07-23) and one is Mauro's (`ideal-youtube-video.md`, 2026-08-04) |
| 14 | Ops loop | `skills/ops/daily-ops.md`, `content-loop.md`, `monday-acquisition-analysis.md`, `case-study-production.md`, `save-recap.md` | **Not sellable** | Twins in growthub-os from 2026-05-27 to 07-08 |
| 15 | Lead gen and DM setting | `skills/lead-gen/email-to-call.md`, `skills/dm-setting/` | **Not sellable** | `email-to-call.md` twin 2026-03-27. `first-messages.md` matches growthub-os `dm-setting/industries/supplement/first-messages.md` (2026-05-11). `setter-playbook.md` came from the "Scrub all Growthub material" commit (`319d084`) |
| 16 | Research and creative strategy | `skills/research/ad-teardown.md`, `brand-breakdown.md`, `weekly-research.md`, `content-sweep.md`, `skills/creative-strategy/` | **Not sellable** | Ad creative is the agency's service. Twins from 2026-03-04 to 06-29. `content-sweep.md` matches growthub-os `skills/content/content-sweep.md` (2026-10-02, 150 lines differ) |
| 17 | Visual docs | `skills/content/visual-docs/` | **Not sellable** (mixed parts) | `render_one.py` matches growthub-os `scripts/render_one.py` (2026-05-27). `page-craft.md` and `reference/client-brand-2page.html` hold the agency palette and a client page (7 and 5 agency mentions) |
| 18 | Pointers and extraction | `skills/content/x-articles-POINTER.md`, `system-extraction.md` | **Not sellable** | Both read growthub-os as the working system (8 and 4 agency mentions) |
| 19 | Anti-slop protocol | `skills/content/anti-slop-protocol.md` | **Not sellable** (third party) | No twin, but it is Ronin's public protocol: `research/competitors/ronin-post-ledger-synthesis.md` line 68, "It is not proprietary to Mauro". Committed the same day Ronin posted it (2026-09-10, `03def52`) |
| 20 | Org-synced skills | `~/.claude/skills/synced/` (actor-swap, animated-ad, format-playbook and others) | **Not sellable** | The agency's org skills and Anthropic example skills, synced by the account |
| 21 | Productivity pack | `~/.claude/skills/` grill-me, grilling, handoff, teach, to-questionnaire, wait-what, writing-for-agents | **Not sellable** (third party) | A third-party pack (`PRODUCTIVITY-README.md`). No agency mentions. Not his to sell |

---

## What changes in the plan

1. **The cleanest system is not the one the plan puts first.** The ASCII kit and the Gate have the
   clearest chain. The outlier intake is closer to ready (it has the only stranger test, the LI1 card)
   but needs the agency's yes. `content/plan/whop-product-v1.md` keeps the intake as v1 and names the
   Gate as the fallback.
2. **The plan's system 2 ("Voice and the Gate") shrinks.** `anti-slop-protocol.md` is Ronin's, and
   `brand/voice.md` is a fork of the agency's. The sellable part is the Gate agent, the hook, the
   rejections-log pattern, the claims-file pattern and the voice extraction method.
3. **The $500 lead magnet system from 22 Aug is out.** Agency twins, agency proof, and a delivery
   method that stopped working on X.
4. **One question to the agency covers most of it.** Ask per row 5, 6, 7 and 12: "Can I sell a
   rebuilt, generic version of this under Ghosted Calls?" Write the answer into this table.
   `[NEEDS: Mauro asks, and the date of the answer]`
