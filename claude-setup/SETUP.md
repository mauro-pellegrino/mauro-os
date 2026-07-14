# Claude Setup for the New Team (ghostedcalls / mauro-pellegrino)

How to get a new teammate (or a fresh machine) running with this repo and Claude Code.

## 1. Claude plan

Each person doing content/ops work in Claude Code needs their own Claude subscription:

- **Solo / light use:** Claude Pro
- **Heavy daily Claude Code use (recommended for you):** Claude Max — higher usage limits, works with Claude Code CLI, desktop, and web
- **Once the team grows:** Claude Team plan gives centralized billing and admin; premium seats include Claude Code

Check current pricing and limits at https://claude.com/pricing before buying — don't rely on this doc staying accurate.

## 2. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
cd ~/mauro-os && claude
```

Log in with the team member's own Claude account when prompted.

## 3. Repo setup

```bash
git clone git@github.com:mauro-pellegrino/mauro-os.git ~/mauro-os
```

- `CLAUDE.md` loads automatically every session — it's the brain. Keep it current.
- `.claude/settings.json` contains three hooks (paths assume the repo lives at `~/mauro-os`; edit if cloned elsewhere, and replace `/Users/mauro` with the teammate's home dir):
  - **SessionStart** — injects `brand/voice.md` writing rules into every session
  - **PostToolUse** — auto-commits and pushes any edit under `skills/`
  - **Stop** — prompts to capture session notes for the content pipeline

## 4. Memory bootstrap

`claude-setup/memory/` holds the portable memory files (user profile, writing feedback rules, personal-brand context). To seed a new machine:

```bash
# find the project memory dir Claude Code created for this repo, e.g.:
cp claude-setup/memory/* ~/.claude/projects/-Users-<user>-mauro-os/memory/
```

Or simpler: paste the contents into a first session and ask Claude to save them to memory.

## 5. Claude Projects (claude.ai web)

For non-Code work (quick drafts on mobile/web), create a Claude Project per workstream and paste in:
- `CLAUDE.md` (rewritten for ghostedcalls)
- `brand/voice.md`
- `brand/positioning.md` + `brand/audience.md`

That keeps web-drafted content consistent with what Claude Code produces.
