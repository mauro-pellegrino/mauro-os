# 12 · agents i'm looking to install in q3 for more booked calls

**Alt title:** every agent i've installed so far is defensive. here's the offensive set.
**What this file is:** the information behind the video. Not a script. It is also a real build
plan, so it doubles as the spec for the work itself.
**Written:** 2026-09-07

**Sources**
- `~/growthub-os/.claude/agents/` (the 4 installed)
- `~/growthub-os/BACKLOG.md` Tier 1, and `ops/BLOCKED-AUDIT.md`
- `~/growthub-os/acquisition-calls/2026-08-31-monday-analysis.md` (the missing motion)
- `~/growthub-os/outbound-calls/00-context.md` (the cold-email motion and its results)
- `~/growthub-os/skills/content/x-articles/_corpus.md` (the attribution finding)
- `~/growthub-os/ops/tools/` (`lead-triage.py`, `post-to-call.py`, `trace-bookings.py`)

**ICP cut:** the owner who has automated his content and still has a pipeline problem, because
none of what he automated touches a human.
**Reach cut:** a build-in-public list with the bottleneck named for each item, published before the
build rather than after it. Nobody publishes the plan while it can still be wrong.

---

## ⚠️ Timing, stated honestly on camera

This is written 2026-09-07. Q3 ends 30 September, so the window is **three weeks**. Two of these can
realistically be installed in that window. The rest are a Q4 list wearing a Q3 title, and saying so
is better than shipping a list nobody could finish.

---

## The one claim

Every agent installed so far is defensive. It catches a drop, catches a missed ask, gates a board,
packages an asset. Not one of them causes a call. That is the gap.

---

## The information

### 1. What is already installed, and what each one prevents

| Agent | Prevents |
|---|---|
| performance-loop | A 64% reach fall going unnoticed for two months, which is what happened between June and August 2026 |
| signal-sweep | A request going missing in a chat thread, which is what happened on 2026-08-14 |
| board-qa | A board shipping full instead of recordable, through 15 gates |
| youtube-lead-magnet | Packaging drift, by forcing the existing skill to be read fresh every run |

Four agents, four scars, zero calls caused.

### 2. The install rule that governs the whole list

An agent goes in only where the skill underneath it is already good, because an agent removes the
correction loop that made it good. Writing is deliberately kept manual for exactly this reason.

So each candidate below carries one honest line: **is there a skill behind it today.** The ones
without a skill are not Q3 items no matter how much they are wanted.

### 3. The candidates, ranked by distance to a booked call

**A. The re-engagement agent.** Works the warmest pool that exists: every past qualified booker who
did not close. Called out as the number one item by an outside consultant, verbatim at 57:20 of the
2026-08-28 call: *"the CRM thing is number one, bro."* It is flagged in the Monday analysis as a
whole motion missing and has never been a row in the backlog.
Skill behind it today: **no.** Blocked on a sequencing decision, because putting it first inverts
the current order. Ranked first anyway, because it is the shortest distance from an existing human
relationship to a call.

**B. The attribution agent.** The UTM Source field is filled on **4 of 541 bookings**, so a unique
DM keyword per asset is the only path from a piece of content to a call. An agent that assigns the
keyword, watches for it, and reports which asset produced which booking turns the whole content
operation from unmeasured to measured.
Skill behind it today: **partly.** The keyword assignment already lives in the article set's sixth
skill, and `post-to-call.py` and `trace-bookings.py` exist. This is the most installable item here.

**C. The cadence agent.** The failure mode named in the backlog in Mauro's own framing: one good
week and then three quiet ones, which is literally what happened after June. An agent that watches
the posting cadence per account and escalates on the second quiet day, before a week is lost.
Skill behind it today: **yes**, the content loop and the performance loop both already read the
inputs it would need.

**D. The dormant-account agent.** One account is down **92% on posts**, and the backlog puts half
the reach the business lost at that door. This is a narrower version of C aimed at restart rather
than maintenance.
Skill behind it today: **yes**, same inputs.

**E. The inbound triage agent.** `lead-triage.py` already exists and the DM skills are written. An
agent that reads inbound, scores against the qualification floor, and drafts the reply for a human
to send. It must never send. The line between drafting and sending is the whole safety design.
Skill behind it today: **yes**, `skills/dm-setting/`.

**F. The outbound reply agent.** The cold-email motion runs at 30k emails a month through an
external operator, and the documented result of the first angle test was **5 responses, 4 to the
Loom angle and 1 to the creative pack**. An agent that watches the lead alerts, pulls context, and
drafts the reply into the right channel.
Skill behind it today: **yes**, the outbound playbook and inbox replies are written. Risk: it is
the closest of all of these to speaking to a stranger, so it drafts only.

**G. The convert-lane loop agent.** Applies the seventh article skill's pattern to bookings rather
than reach: regenerate the evidence, downgrade rules that lose contradictions, and keep the convert
rules separate from the reach rules.
Skill behind it today: **yes**, but it needs enough keyword data to read, which means B ships first.

### 4. The order that follows from all of that

1. **B, attribution.** Highest install-readiness, and everything else becomes measurable once it runs.
2. **C, cadence.** Prevents the failure that has already cost a quarter.
3. Then E and F, both draft-only, in whichever order the inbox is louder.
4. A waits on a sequencing decision that only Mauro makes. D folds into C. G waits on B.

**So the honest Q3 answer is two: B and C.** The rest is Q4 with a date attached.

### 5. The safety rule for every one of them

None of these send. Every candidate drafts, scores, flags or escalates, and a human sends. An agent
that fails quietly is the main new risk of running agents at all, and a quiet failure that has
already spoken to a prospect cannot be taken back.

---

## Evidence

| Claim | Status |
|---|---|
| 4 agents installed, all defensive | `[measured: .claude/agents/, 2026-09-07]` |
| 64% reach fall unnoticed for two months | `[measured: named in the performance-loop agent]` |
| "the CRM thing is number one, bro", 57:20, 2026-08-28 | `[observed: quoted in BACKLOG.md Tier 1]` |
| UTM filled on 4 of 541 bookings | `[measured: _corpus.md]` |
| One account down 92% on posts | `[observed: BACKLOG.md Tier 1]` |
| 5 responses, 4 to Loom, 1 to creatives | `[observed: outbound-calls/00-context.md]` |
| Two agents installable inside the Q3 window | `[assumed: readiness judgement, stated as one]` |

---

## Beats on camera

1. Four agents running. None of them has ever caused a call.
2. The four scars, fast, one line each.
3. The install rule: the skill has to be good first, or the agent freezes a bad one.
4. The seven candidates, each with its bottleneck named.
5. The consultant quote for the CRM motion.
6. 4 of 541, and why attribution ships first.
7. One good week then three quiet ones, and the agent that watches for it.
8. Draft, never send, and why that line exists.
9. The honest count: two in the window, the rest is Q4.
10. CTA, and an invitation to be told which one is wrong.

---

## Do not say

- Any client, account or external operator's name.
- That any of these are installed. None are, as of 2026-09-07.
- A projected number of calls. Nothing here supports one.
- That agents will send outbound messages. They draft.

## Gaps

- `[NEEDS: Mauro's decision on whether the CRM motion jumps the queue]`
- `[NEEDS: a re-check of the installed agent list on the day of recording]`
