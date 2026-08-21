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

## Structure

```
brand/engine/
├── 00-the-engine.md              the intro. Ships as page 1 of everything
└── module-01-lead-magnets/
    ├── 00-start-here.md          why it works, and whether to bother
    ├── 01-install.md             three paths, Claude Project first
    ├── 02-brand-context.md       the required input. Replaces every "ask Mauro"
    ├── 03-the-rules.md           TO BUILD. Source: ../../lead-magnets/shareable/lead-magnet-system.md
    ├── 04-skill-files.md         TO BUILD. The actual files, in full
    ├── 05-templates.md           TO BUILD. Post, DM, LeadShark, cover, page structure
    ├── 06-worked-example.md      TO BUILD. Source: content/qa/magnet-youtube-to-week-of-content.md
    └── 07-score-your-own.md      20 checks, verdict bands
```

Five of eight written. The three left are assembly from files that already exist.

---

## Rules for every module

**1 · The module is complete on its own.** Someone who installs 01 and never buys another thing has a working system. "One of many" positions the engine, it never means "here's a taste."

**2 · The real artifact, never a description of it.** If a page mentions a template, the template is on that page in full and copy-pasteable. This is what the first Notion assembly got wrong: prose plus a few hook lines, no examples, no templates.

**3 · Assume they've never heard of Claude Code.** Path A needs no terminal. Claude Code is offered second, for people already in one, and stated plainly to produce no different output.

**4 · Operator vocabulary.** Engine, system, module. Never course, program, lesson or curriculum. The ICP runs real businesses and info-product language reads as a downgrade.

**5 · Numbers are real or absent.** Where the evidence comes from an account Mauro runs it ships unnamed. His own numbers replace it as they accrue.

---

## Why the engine framing fits this ICP

The buyer is an operator who already produces good video and isn't converting it into written content. Camilo Castañeda, Brando, Antonio Ventre.

Operators already think in systems, so a module in an engine reads as normal. What reads as a downgrade is a course. The nearest comparable in this space sells "the creative system my agency uses," not a program, and that's the register.

**The risk to manage:** "one of many" can imply incomplete. Module 01 has to be genuinely finished for everything lead-magnet before it ships, which is why 03, 04 and 05 are not optional.
