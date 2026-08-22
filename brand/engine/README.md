# The Engine — build and packaging

Internal. Not shipped to buyers.

---

## Packaging decision, 21 Aug 2026

**Whop is the container. A git repo holds the files. Nothing else.**

| Layer | Tool | Why |
|---|---|---|
| Storefront, payment, access control | **Whop** | Free to start, ~3% per sale plus processing, no monthly fee. Handles checkout, gating and module delivery in one thing. Mauro has no payment processor, so this closes that hole rather than adding a tool |
| Module content | **Whop courses** | Native module structure, so 02 and 03 slot in without a rebuild |
| The skill files | **A git repo, one download link** | Updates are the whole reason. A frozen copy goes stale the day it's duplicated, and this system gets corrected most weeks. Buyer clicks Download ZIP and never sees git |
| Fill-in artifacts | Downloadable template inside the module | Page 07 has to be genuinely fillable. Ship it as a duplicable template, not as prose |

**What changed from the earlier call.** Notion was the plan, and Whop is better for three specific reasons: a Notion duplicate link has no access control so nothing stops resale, Notion can't take payment, and a duplicate freezes at the moment of duplication. Whop solves all three at no monthly cost.

**What Skool would add later.** Community and a live element, at $99/mo. Correct when the group tier opens, not before. Same modules move across.

**Unverified:** whether Whop's course and gating features are all available on the free tier. Check before building.

---

## Pricing, 21 Aug 2026

**$99/month entry. Free trial for selected people.**

Replaces the $500 one-time. Recurring fits the engine shape: modules arrive over time, files get corrected weekly, and a subscription is the honest way to charge for that. $99/mo needs ~51 members to clear $5k/mo.

**The load-bearing risk, stated plainly.** At $99/mo with downloadable files and a free trial, someone can trial, download module 01, and cancel. Access control on files is weak by design, because the files have to leave the platform to be useful.

That is survivable only if the recurring value is in what they cannot download once:
- **New modules.** 02, 03 and 04 have to actually ship. If they don't, churn after month one is correct behaviour by the buyer.
- **Corrections.** The repo has to keep moving. A static repo is a frozen copy with extra steps.
- **A live element.** Not built yet. The weekly roast is the obvious candidate and it's the single strongest retention mechanic available.

If none of those three exist, this should be a one-time purchase instead. Recurring without recurring value is just churn with a subscription button.

**Free trial:** deliberate and hand-picked, not open. Pick people whose feedback is worth the leak, and whose logo or name you'd want next to this later.

---

## Structure

```
brand/engine/
├── 00-the-engine.md              the intro. Ships as page 1 of everything
└── module-01-lead-magnets/
    ├── 00-start-here.md          why it works, and whether to bother
    ├── 01-install.md             three paths, Claude Project first
    ├── 02-brand-context.md       the required input. Replaces every "ask Mauro"
    ├── 03-the-rules.md           written. Evidence still needs the 365-day rebuild
    ├── 04-skill-files.md         written. Ships 1 subtype of 5
    ├── 05-templates.md           written. Post, DM, LeadShark, cover, page structure
    ├── 06-worked-example.md      written. {{calendly_url}} still empty in 2 places
    └── 07-score-your-own.md      20 checks, verdict bands
```

All eight written, verified 22 Aug. See "What module 01 is still objectively missing" below for what remains.

---

## Rules for every module

**1 · The module is complete on its own.** Someone who installs 01 and never buys another thing has a working system. "One of many" positions the engine, it never means "here's a taste."

**2 · The real artifact, never a description of it.** If a page mentions a template, the template is on that page in full and copy-pasteable. This is what the first Notion assembly got wrong: prose plus a few hook lines, no examples, no templates.

**3 · Assume they've never heard of Claude Code.** Path A needs no terminal. Claude Code is offered second, for people already in one, and stated plainly to produce no different output.

**4 · Operator vocabulary.** Engine, system, module. Never course, program, lesson or curriculum. The ICP runs real businesses and info-product language reads as a downgrade.

**5 · Numbers are real or absent.** Where the evidence comes from an account Mauro runs it ships unnamed. His own numbers replace it as they accrue.

---

## Why the engine framing fits this ICP

**The buyer runs a real YouTube channel and wants a LinkedIn and X presence to match.** They already publish video consistently, so the source material is abundant and recurring. What they lack is the written and visual formats, and the system that converts one into the other.

Camilo Castañeda, Brando, Antonio Ventre.

**Why this ICP is the right one.** A big channel means the input problem is already solved. The engine's first stage is source material, and they have more of it than they can use. Nobody in this profile needs convincing that content works, only that there's a way to convert what they already make. That is a much shorter argument.

Operators already think in systems, so a module in an engine reads as normal. What reads as a downgrade is a course. The nearest comparable in this space sells "the creative system my agency uses," not a program, and that's the register.

**The risk to manage:** "one of many" can imply incomplete. Module 01 has to be genuinely finished for everything lead-magnet before it ships, which is why 03, 04 and 05 are not optional.

---

## Module pipeline: what already exists to package

Surveyed the agency repo 21 Aug. Every module below is built from systems already in daily use. None of it needs inventing, only packaging and de-personalising.

| Module | Built from | Why it fits the ICP |
|---|---|---|
| **02 · The Article System** | `x-article-creator`, `miro-to-article`, `long-form/` (6 subtypes incl. the text-only wrong-version-teardown) | One video becomes a long-form authority piece. Cheapest format to ship |
| **03 · The Format Multiplier** | `short-form/bulk-short-form-generator`, the 39-vehicle library | One transcript becomes a month of posts. Directly the "I have video, no written presence" problem |
| **04 · The Measurement Loop** | `content-loop`, `content-control-panel`, `monday-acquisition-analysis`, `content-tracker.py`, `build-dashboard.py` | The stage almost nobody builds. Content matched against booked calls |
| **05 · The Visual Doc System** | `linkedin-docs/`, `linkedin-html-doc-guide`, `visual-docs/`, `render_png.py` | HTML to PNG docs and infographics. The "visuals and slides" half of the pitch |
| **06 · The Board System** | `skills/miro/` (7 files: `visual-language`, `writing-for-boards`, `video-board-generator.py`, `api-gotchas`) | Script to Miro board. Rare, visual, and big-channel operators already plan videos |
| **07 · The YouTube System** | 8 skills: `youtube-title-generator`, `hook-script`, `idea-generator`, `miro-board`, `canva-slides`, `slide-visuals`, `brand-breakdown` | Their own channel, run better. Highest-affinity module for this ICP |

**Off-lane, do not package:** `creative-strategy/research-pipeline/` and `static-ads`. Those are ecom ad creative, which is the agency's service and not Mauro's lane per `positioning.md`.

**What this settles about pricing.** Recurring is viable because six more modules of material already exist. It is not viable *today* because none of them are packaged. The honest sequence is a one-time price for module 01 now, switching to $99/mo the month module 02 ships.

---

## What module 01 is still objectively missing

Checked against its own rules, 21 Aug.

1. **It teaches one subtype of five.** Page 04 ships the prompt-swipe-file subtype only. Framework, case study, video and industry-specific exist internally and are absent. The module claims to cover lead magnets and covers one kind.
2. **One worked example.** The other four subtypes have nothing to copy the shape of.
3. **Zero images.** The rules say a real example screenshot is the strongest option and to use it most. The module contains no screenshots at all, so it breaks its own image rule on every page.
4. **The evidence is buried.** The 40-post table, the seven rejected-to-shipped titles and the fatigue curve are the least reconstructable thing in here, and they sit mid-document inside page 03 instead of leading.
5. **No video.** The buyer's whole profile is that they make video. The module is entirely reading.

Items 1 and 3 are the two that would stop a buyer mid-build.
