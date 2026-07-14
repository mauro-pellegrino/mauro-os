# Welcome to mauro-os, Juan

This repo is the operating system for Mauro's ghostedcalls work. It contains the brand context, the writing rules, and the skills (step-by-step playbooks) that Claude uses to produce content. Your job is to run these skills and hand the outputs to Mauro. Claude does the heavy lifting. You drive it and quality-check it.

## One-time setup (15 minutes)

1. **GitHub account.** If you don't have one, create it at github.com/signup with your ghostedcalls email. Send Mauro your username so he can invite you to the repo. Accept the invite from your email.
2. **GitHub Desktop.** Download from desktop.github.com and sign in with your GitHub account.
3. **Clone the repo.** In GitHub Desktop: File → Clone Repository → select `mauro-pellegrino/mauro-os` → Clone. Remember the folder location it picks.
4. **Claude app.** You already have it with the team account. Open it and start a Claude Code session in the mauro-os folder you just cloned.
5. **Trust the project.** The first session will ask you to approve the project's hooks. Say yes. This makes the writing style rules load automatically every time you start a session.

You never need the terminal, SSH keys, or git commands. GitHub Desktop and the Claude app handle everything.

## How a work session goes

1. Open the Claude app, session inside the mauro-os folder.
2. Tell Claude what you need and which skill to use. Example: "Use the short-form skill in skills/content/ to turn this transcript into X posts" and paste the input.
3. Claude reads the skill file and produces the output following Mauro's rules.
4. Read the output yourself before sending it anywhere. You are the last check.
5. Send the output to Mauro for review. Nothing goes public without his sign-off.

Each morning, sync first: open GitHub Desktop and click "Fetch origin" then "Pull" if there are changes. This gets you the latest skills before you start.

## The rules that are never broken

1. **Never name clients in anything public-facing.** Client names stay in internal files only.
2. **Never invent numbers.** No made-up hook rates, CPAs, ROAS, revenue figures. If a real number isn't in the source material, use a bracket placeholder like [X%] and flag it for Mauro.
3. **Nothing publishes without Mauro's review.** Your outputs are drafts until he approves them.
4. **Don't edit skill files.** Skills are the playbooks. If you think a skill has a problem, tell Mauro instead of changing it. (Edits to skills auto-push to GitHub, so a wrong edit spreads immediately.)
5. **Articles and lead magnets have their own flow.** Don't save them into the repo. Hand them to Mauro in chat or Slack and he decides where they go.

## Where things live

| Folder | What's in it |
|---|---|
| `skills/content/` | X posts, articles, LinkedIn, long-form playbooks |
| `skills/youtube/` | YouTube scripts, titles, slides, Miro boards |
| `skills/lead-gen/`, `skills/dm-setting/` | Lead magnets and DM playbooks |
| `skills/research/` | Brand breakdowns, ad teardowns, weekly research |
| `brand/` | Mauro's positioning, audience, voice rules. Read `positioning.md` and `audience.md` in your first week |
| `research/transcripts/` | Saved video transcripts used as source material |
| `CLAUDE.md` | The brain. Claude reads it automatically, you don't need to |

## Your first week

- Day 1: setup above, then read `brand/positioning.md` and `brand/audience.md`.
- Day 1 to 5: run only the task type Mauro assigns you, one skill at a time. Send him every output.
- Ask questions early. A two-minute question beats an hour of wrong output.

## If something breaks

- Claude says it can't find a file: make sure your session is opened in the mauro-os folder, not your home folder.
- Style rules didn't load at session start: close the session and open a new one in the folder. If it persists, tell Mauro.
- GitHub Desktop shows errors: screenshot it and send to Mauro. Don't click through error dialogs blindly.

Questions go to Mauro on Slack.
