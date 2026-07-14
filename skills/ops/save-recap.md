# Skill: Save Recap

**Version:** 1.0
**Created:** 2026-05-27
**Trigger phrases:** "save this recap", "save the recap", "log this", "calendar this"
**Output:** Per-day recap file in `recaps/` + Google Calendar event with the recap in the event description

---

## What This Skill Does

When Mauro asks to save a recap (of work done in a session, of decisions made, of any meaningful chunk of activity), this skill:

1. Generates a per-day recap from the conversation + git log
2. Saves the recap to `recaps/YYYY-MM-DD.md` in the repo
3. Creates a Google Calendar event titled `mauro-os work — [date]` with the recap pasted into the event description
4. Commits + pushes the recap file
5. Reports back with the saved paths + the calendar event URL

---

## Trigger phrases (Mauro recognizes these as "save it")

Any of these (and reasonable variants):
- "save this recap"
- "save the recap"
- "log this"
- "calendar this"
- "put this on my calendar"
- "save what we did"

---

## How to generate the recap

Pull from two sources:

**1. Git log for the day:**
```bash
cd /Users/mauro/mauro-os
git log --since="YYYY-MM-DD 00:00" --until="YYYY-MM-DD 23:59" --pretty=format:"%ad|%s" --date=format:"%H:%M"
```

This gives the committed work in chronological order.

**2. Conversation context:**
What was discussed, what was decided, what shifted strategy-wise. Especially capture decisions that aren't visible from commit messages alone.

---

## Recap file structure

```markdown
# Recap — [Day of week] YYYY-MM-DD

**Commits:** [count]
**Net theme:** [1-2 sentence summary of what the day was really about]

---

## Commits (in order)

| Time | Commit | What shipped |
|---|---|---|
| HH:MM | `commit subject` | One-line description of what landed |
| ... | ... | ... |

---

## Decisions made

1. Decision 1 (with brief reasoning if non-obvious)
2. Decision 2
...

---

## Files added or modified (key paths)

```
[paths in a code block, grouped logically]
```

---

## Net outcome

[2-3 sentences: what's now true at the end of the day that wasn't true at the start, what's pending]
```

Keep it to ~150-250 lines max per day. Skim-readable in 2 minutes.

---

## File location + naming

- **Path:** `recaps/YYYY-MM-DD.md`
- One file per day. If multiple recap requests in the same day, append to the existing file with a `## Update HH:MM` heading.

---

## Google Calendar event spec

When the Google Calendar MCP is authenticated and the `mcp__claude_ai_Google_Calendar__*` tools are available:

- **Event title:** `mauro-os work — [Day] YYYY-MM-DD`
- **Event date:** the date the recap covers (NOT today's date if recapping a previous day)
- **Event time:** all-day event (no specific time block needed)
- **Event description:** the full recap content (the same markdown, formatted as plain text where needed)
- **Calendar:** Mauro's primary calendar (default; ask if unclear)

If the MCP is NOT authenticated yet (e.g., a new session), call `mcp__claude_ai_Google_Calendar__authenticate` to trigger the OAuth flow and ask Mauro to complete it via `/mcp`.

---

## Commit message format

When committing the recap file to the repo:

```
recap: YYYY-MM-DD work log

[1-line summary of the day]

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
```

Push after committing per the repo CLAUDE.md non-negotiable rule.

---

## How to run this skill

1. Identify the date(s) being recapped (today by default, or per Mauro's instruction)
2. Pull git log for that date range
3. Extract decisions / strategy shifts from conversation context
4. Draft the recap file following the structure above
5. Write to `recaps/YYYY-MM-DD.md`
6. Commit + push
7. If Google Calendar MCP is authenticated: create the calendar event with the recap as description
8. Report back to Mauro: file path, commit hash, calendar event URL

If multiple days are in the same request (e.g., "save Tuesday and Wednesday"), produce one file per day. Each gets its own calendar event.

---

## Edge cases

- **Recap requested for a future date**: ask which date Mauro means. Don't pre-emptively create future-dated recaps.
- **Recap requested for a day with no commits**: still produce the recap from conversation context. Note "no commits this day" in the file.
- **Recap requested mid-day**: produce a partial recap. Note "partial recap as of HH:MM" in the file header. Future "save this recap" requests for the same day append to the file.
- **Multiple updates in one day**: append `## Update HH:MM` sections to the existing file rather than overwriting.

---

## Output checklist

- [ ] Recap file written to `recaps/YYYY-MM-DD.md`
- [ ] Commit log accurately reflects the day's work (cross-checked against `git log`)
- [ ] Decisions section captures non-obvious calls (not just commit messages)
- [ ] Files-modified section lists key paths
- [ ] Net outcome section is honest about what's pending
- [ ] File committed + pushed
- [ ] Calendar event created (if MCP authenticated)
- [ ] Mauro reported back with file path + commit hash + calendar URL
