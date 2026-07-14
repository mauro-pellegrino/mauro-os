# mauro-os

Mauro's operating system for the ghostedcalls / maurojpelle team. Extracted from growthub-os on 2026-07-13 (all extracted content was authored by Mauro).

## What's here

| Dir | What it is | Status |
|---|---|---|
| `CLAUDE.md` | Session brain — copied from growthub-os | **REWRITE**: sections on agency identity, ICP, clients are Growthub's |
| `brand/` | Personal brand context (positioning, audience, posts, lead magnets) + `voice.md` writing rules | voice.md needs a pass to strip Growthub-specific references |
| `skills/` | All skill dirs (content, creative-strategy, dm-setting, lead-gen, ops, research, youtube) | **REWRITE per skill**: prune what doesn't apply, swap Growthub branding/ICP for ghostedcalls |
| `research/transcripts/` | maurojpelle transcript research | ready |
| `claude-setup/` | Portable Claude memory files + team setup guide (SETUP.md) | ready |
| `.claude/` | Hooks (voice injection, skill auto-save, session-notes prompt) + youtube-lead-magnet agent | paths already rewritten to ~/mauro-os |

## Deliberately NOT copied from growthub-os

Growthub client and team material: `accounts/lorenzo-x`, `accounts/bogdan-x`, `accounts/stealth-ai`, `brands/` (client brands), `acquisition-calls/`, `emails/`, `recaps/`, `ops/`, team-facing scripts. If something from there turns out to be needed, extract it deliberately.

## GitHub

Lives at `github.com/mauro-pellegrino/mauro-os` (private). On Mauro's Mac the remote uses the `github-ghostedcalls` SSH alias (see `~/.ssh/config`) so the ghostedcalls key is used instead of the Growthub one:

```
origin  git@github-ghostedcalls:mauro-pellegrino/mauro-os.git
```

Note: the skill auto-save hook in `.claude/settings.json` runs `git push` on every skill edit.
