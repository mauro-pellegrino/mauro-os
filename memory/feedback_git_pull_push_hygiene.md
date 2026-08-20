---
name: feedback_git_pull_push_hygiene
description: Pull main at session start, push after every unit of work; work on main, don't let unpushed commits stack
metadata:
  type: feedback
---

Start every session with `git checkout main && git pull`. End every unit of work with a commit and `git push`. One commit, one push. Never let unpushed commits stack up. Work on `main` by default; if a feature branch is genuinely needed, merge it back and push promptly so `main` stays the single source of truth.

**Why:** In Juan's earlier Claude Code sessions, work happened directly on local `main`, got committed 3 times, and was never pushed. Meanwhile origin/main moved 71 commits ahead. main drifted, diverged, and a later `git pull` forced a conflict-heavy reconciliation across brand-critical files (CLAUDE.md, positioning, audience). Scattering work across stale side branches made it worse.

**How to apply:** Pull first, push last, every session. Keep the working tree clean between tasks. If you spot main is behind or has unpushed commits, flag it and reconcile before starting new work, don't build on top of drift. Codified in CLAUDE.md section 7 Operating Rules.
