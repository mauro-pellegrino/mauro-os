# mauro-os

Mauro's operating system for the ghostedcalls / maurojpelle brand. Everything here was authored by Mauro and serves his own brand only. Internal agency material (client brands, team accounts, agency ops) lives elsewhere; if something from there is ever needed, extract it deliberately.

## What's here

| Dir | What it is | Status |
|---|---|---|
| `CLAUDE.md` | Session brain: identity, ICP, beliefs, routing, output rules | ready |
| `brand/` | Personal brand context (positioning, audience, posts, lead magnets) + `voice.md` writing rules | ready |
| `skills/` | All skill dirs (content, creative-strategy, dm-setting, lead-gen, ops, research, youtube) | being retargeted to Mauro's ICP where examples still assume a different one |
| `research/transcripts/` | maurojpelle transcript research | ready |
| `claude-setup/` | Portable Claude memory files + team setup guide (SETUP.md) | ready |
| `.claude/` | Hooks (voice injection, skill auto-save, session-notes prompt) + youtube-lead-magnet agent | ready |

## GitHub

Lives at `github.com/mauro-pellegrino/mauro-os` (private). On Mauro's Mac the remote uses the `github-ghostedcalls` SSH alias (see `~/.ssh/config`) so the ghostedcalls key is used for this repo:

```
origin  git@github-ghostedcalls:mauro-pellegrino/mauro-os.git
```

Note: the skill auto-save hook in `.claude/settings.json` runs `git push` on every skill edit.
