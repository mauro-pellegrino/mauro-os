# 02 · how i structure 40+ claude skills so the whole thing doesn't collapse

**Alt title:** your ai setup is a folder of prompts. here's what it should be.
**What this file is:** the information behind the video. Not a script.
**Written:** 2026-09-07

**Sources**
- `~/growthub-os/skills/` (73 markdown files, 8 folders)
- `~/growthub-os/ops/MAP.md` (the index, and the incident that created it)
- `~/growthub-os/ops/CONVENTIONS.md` (the nine rules)
- `research/transcripts/maurojpelle/the-engine-skills-structure-skills-vs-agents.md`

**ICP cut:** the owner whose team already uses Claude and whose "system" is thirty prompts in a
Notion page nobody opens twice.
**Reach cut:** everyone building with AI right now hits the same wall at around file thirty, and
nobody publishes the filing system, only the prompts.

---

## The one claim

The prompts are not the asset. The index, the conventions and the correction loop are the asset,
and they are the parts nobody shows you.

---

## The information

### 1. The shape of the repo

Skills split by **activity**, never by client and never by industry. Eight folders:

| Folder | Owns |
|---|---|
| `content/` | long-form, short-form, LinkedIn docs, the X article set, miro-to-article |
| `research/` | weekly research, brand breakdowns, ad teardowns |
| `ops/` | daily ops, the content loop, the Monday acquisition analysis, case studies, recaps |
| `miro/` | every board build, the DSL gotchas, the house diagram style |
| `lead-gen/` | the five lead magnet subtypes, email to call |
| `youtube/` | ideas, titles, hooks, boards, slides |
| `creative-strategy/` | static ads, the Pixar ad script QA |
| `dm-setting/` | outbound and inbound DM templates |

**73 files.** `[measured: find skills -name "*.md" | wc -l, 2026-09-07]`

The reason for splitting by activity: a client folder rots the day the client leaves, and the same
skill gets rebuilt inside the next client folder. An activity survives every client.

### 2. The incident that created the index

On 2026-09-01 an agent wrote a full outbound-reply SOP from scratch and pushed it, then found that
`outbound-calls/` already held a better one. Forty-five minutes of work deleted. The cause was not
carelessness. The routing table had 40+ rows and that folder was not in it, so there was no way for
the agent to know. `[observed: recorded verbatim in ops/MAP.md]`

Out of that came the rule that carries the whole system:

> **Work is not finished until it is routed.** A skill that is not in the index and not in the
> routing table is invisible, which is worse than not existing, because the next agent builds a
> second one.

This is the single most transferable idea in the video. Anyone with more than about twenty files
has already paid this tax without noticing.

### 3. The conventions that keep it honest

Nine rules in `ops/CONVENTIONS.md`. The four worth showing on camera:

**Every claim carries its evidence status.** Three tags: `[measured]` names a script and a dataset,
`[observed]` was seen but not quantified, `[assumed]` is a judgement stated as one. An untagged
claim is an assertion and gets deleted on sight.

Why the rule exists: a skill once asserted "the worked example is the section that converts."
Measuring it returned 60,000 against 264,000, the opposite direction. The claim had felt obviously
true. `[observed: recorded in CONVENTIONS.md, 2026-09-01]`

**Every number traces to a script and a dataset.** A number in a doc points at the file that holds
it. That file points at a script and a capture. The corollary: the analysis that produced a number
gets saved as a script, because an inline calculation is lost at the next context clear and then
somebody re-derives it slightly differently.

**Every script states its own limit in its opening docstring.** One tool was named as though it
measured one account's bookings. It measures all inbound bookings, because 649 of 678 Calendly rows
sit under a single owner and the UTM field is empty on 673 of them. The name asserted something the
data could not support, so the docstring now says so in capitals.

**Decisions are dated lines in the file they govern.** Not in chat, not in a separate log. When a
call gets made it goes into the file whose behaviour it changes, with the date and the exact wording.

### 4. The two-repo split, and the drift that forced it

`growthub-os` is canonical for skills. `mauro-os` holds voice, positioning and audience, and points
at the canonical skills instead of copying them. That rule exists because two copies of the same
article skill already drifted apart with nothing syncing them.
`[observed: ops/MAP.md, two-repo layout section]`

Anything account-agnostic lives in one repo once. Voice and positioning stay per repo, because they
are the only things that genuinely differ.

### 5. The loop that makes any of it worth having

Build the skill for one job. Run it on real work this week, never a fake example. Read the output,
find exactly where it breaks, edit the skill itself, run it again. The reference implementation is
the seventh file in the X-article set, which exists only to keep the other six honest as evidence
lands.

---

## Evidence

| Claim | Status |
|---|---|
| 73 skill files, 8 activity folders | `[measured: file count, 2026-09-07]` |
| 45 minutes lost to a rebuilt SOP on 2026-09-01 | `[observed: MAP.md]` |
| The worked-example claim measured 60,000 vs 264,000 | `[observed: CONVENTIONS.md]` |
| 649 of 678 Calendly rows under one owner, UTM empty on 673 | `[measured: named in CONVENTIONS.md rule 3]` |
| Splitting by activity beats splitting by client | `[assumed: reasoning from the client-churn case]` |

---

## Beats on camera

1. Open the folder. Eight names, 73 files.
2. Why activity and not client.
3. The 45-minute incident, told straight.
4. Route it or it does not exist.
5. The three evidence tags, and the claim that measured backwards.
6. Numbers trace to a script. Save the script.
7. Scripts declare their own limits.
8. Decisions are dated lines in the file they govern.
9. Two repos, and the drift that forced the rule.
10. The correction loop.
11. CTA.

---

## Do not say

- Any client name.
- That 73 files is a target. It is a count on one date.
- That this is the only correct structure. It is the one that survived contact.

## Gaps

- `[NEEDS: a screen-safe view of the repo tree with client names absent]`
