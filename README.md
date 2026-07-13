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

## Push to GitHub

```bash
gh repo create maurojpelle/mauro-os --private --source ~/mauro-os --push
# or manually:
git remote add origin git@github.com:maurojpelle/mauro-os.git
git push -u origin main
```

Note: the skill auto-save hook in `.claude/settings.json` runs `git push`, so add the remote before editing skills in Claude Code (it fails silently otherwise).
