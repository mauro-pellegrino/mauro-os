# Claude Setup for the New Team (ghostedcalls / mauro-pellegrino)

How to get a new teammate (or a fresh machine) running with this repo and Claude Code.

## 1. Claude plan

Each person doing content/ops work in Claude Code needs their own Claude subscription:

- **Solo / light use:** Claude Pro
- **Heavy daily Claude Code use (recommended for you):** Claude Max — higher usage limits, works with Claude Code CLI, desktop, and web
- **Once the team grows:** Claude Team plan gives centralized billing and admin; premium seats include Claude Code

Check current pricing and limits at https://claude.com/pricing before buying — don't rely on this doc staying accurate.

## 1b. Two Claude accounts on one Mac (Mauro's setup)

Verified against the official docs (July 2026):

- On macOS you cannot be logged into two Claude accounts at once in Claude Code; credentials live in the system Keychain. Switch accounts with `/login` (quick browser OAuth, a few seconds). Repos, CLAUDE.md, and memory stay on disk regardless of which account is active.
- If you need both at the same time: run one of them in the browser at claude.ai/code (browser logins are independent of the Keychain) and connect it to the mauro-os GitHub repo.
- Claude Code inside the Claude desktop app is the same Claude Code as the terminal CLI (same skills, hooks, CLAUDE.md, MCP). Use whichever you prefer; the desktop app is the right choice for VAs.

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

`memory/` (repo root) holds the portable memory files (user profile, writing feedback rules, personal-brand context). To seed a new machine:

```bash
# find the project memory dir Claude Code created for this repo, e.g.:
cp memory/* ~/.claude/projects/-Users-<user>-mauro-os/memory/
```

Or simpler: paste the contents into a first session and ask Claude to save them to memory.

## 5. Claude Projects (claude.ai web)

For non-Code work (quick drafts on mobile/web), create a Claude Project per workstream and paste in:
- `CLAUDE.md` (rewritten for ghostedcalls)
- `brand/voice.md`
- `brand/positioning.md` + `brand/audience.md`

That keeps web-drafted content consistent with what Claude Code produces.
