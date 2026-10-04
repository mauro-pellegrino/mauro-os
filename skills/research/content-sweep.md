---
name: content-sweep
description: "Input 2 · Our real work (weekly grab). Reads the week's Slack, call recordings, docs and Looms, and turns the operator's real work into sourced insight cards for content. Triggers on \"weekly grab\", \"content sweep\", \"what did we do this week\", \"real work sweep\". Runs Mondays, last 7 days."
---

# Input 2 · Our real work (weekly grab)

Real work is the content engine (belief 9). This skill reads one week of the operator's own work and turns each real workflow or result into an insight card with a source. The cards feed posts, articles, case studies, YouTube and lead magnets.

It works in two setups:

- **Mauro (@maurojpelle).** The operator is Mauro. The work is the content engine he runs and builds.
- **A Ghosted Calls client install.** The operator is the client agency owner. The work is their team's client delivery. Fill the `[SLOT]` tables at install time and keep them in their repo.

**This skill collects content.** It does not collect tasks or requests. If a message is an ask, skip it.

## Trigger and window

- Phrases: "weekly grab", "content sweep", "what did we do this week", "real work sweep".
- Runs Mondays. Window = the last 7 days. For Slack, set `oldest` to the Unix time of 00:00 seven days ago.
- Week label `YYYY-Www` = the ISO week the window ends in.

## Load first

1. `brand/claims.md`: which numbers and facts are safe to state in public.
2. `brand/positioning.md` and `brand/audience.md`: what the cards are for.
3. Last week's `research/real-work/YYYY-Www/cards.md`, if it exists, so a repeat is marked as a repeat.

Tools, with ToolSearch:

```
ToolSearch("select:mcp__claude_ai_Slack__slack_read_channel,mcp__claude_ai_Slack__slack_read_thread,mcp__claude_ai_tldv__search-meetings,mcp__claude_ai_tldv__get-meeting-transcript,mcp__claude_ai_Notion__notion-search,mcp__claude_ai_Notion__notion-fetch,mcp__claude_ai_Google_Drive__search_files,mcp__claude_ai_Google_Drive__read_file_content")
```

A source whose connector is not authenticated goes in the run report as `[NEEDS: <connector> connected]`. Never guess what an unread recording says.

## Sources

### The source map (fill once per install)

| Source | Where | Connector | Tier |
|---|---|---|---|
| Slack channels | see the channel table below | Slack | primary |
| Call recordings | `[SLOT: tl;dv / Fathom / other]` | `[SLOT]` | primary |
| Docs and SOPs | `[SLOT: Notion workspace / Drive folders]` | Notion, Drive | primary |
| Looms | `[SLOT: Loom workspace]` | Loom | primary |
| Sales and acquisition channels | `[SLOT]` | Slack | lead only |

**Mauro's setup.** His own work also lives in this repo: `research/transcripts/maurojpelle/` (voice notes and Looms), `brand/sessions/`, and the week's commits (`git log --since="7 days ago"`). A commit that shipped a skill, a tool or a diagram is a real workflow with a date and a diff. Read those first.

### Slack: read every channel by ID

| Channel | ID | What lands there |
|---|---|---|
| `[SLOT: #wins]` | `[SLOT]` | results with numbers |
| `[SLOT: #team-updates]` | `[SLOT]` | new workflows, tools tried |
| `[SLOT: #ideas]` | `[SLOT]` | formats and tests |

Method:

- Read each channel directly with `slack_read_channel`, `oldest` set to the window start. Do not use search to find messages. Search is ranked and skips quiet channels.
- Open every thread with replies through `slack_read_thread`. The steps of a workflow are usually in the replies.
- Low-volume channels carry high signal. Never skip a channel because it looks quiet.

### Calls

Search the window. Pull the full transcript for every team sync, training and client call where a workflow is shown. Notes summaries are often empty, so use the transcript. Skip recruiter calls and pure reporting calls.

### Docs, Drive, Looms

Search for docs, SOPs and trainings edited in the window. Fetch each changed one. In Drive, look for files modified in the window in the delivery folders. Record the link on the card. Record each new folder or workspace in the source map the first time you use it.

**Not a primary source:** docs that Claude drafted (lead magnets, format libraries, articles, anything built from someone else's material). They repeat unchecked detail. Use them to find a lead, then confirm it in a primary source.

## Save the raw pulls

Save to `research/real-work/YYYY-Www/`:

- Slack: `slack-<channel>.md`, one file per channel, each message with its permalink.
- Calls: `call-YYYY-MM-DD-<slug>.md`, verbatim transcript, meeting link at the top.
- Docs: `doc-<slug>.md`, with the URL and the edit date at the top.

Redact credentials. Mark the operator's own messages and anything Claude wrote `OPERATOR/CLAUDE, not primary`.

## The insight card

One card per real workflow or result. All cards go in `research/real-work/YYYY-Www/cards.md`.

```
### C-YYYY-Www-NN · <short name of the workflow>
- Tool: <the tools named in the source, exactly as named>
- Step: <the steps, in the order the source gives them>
- Result: <the number or outcome, verbatim, or [NEEDS: result]>
- Failure: <where it broke or what did not work, or [NEEDS: failure]>
- Who: <the person who built or ran it>
- Source: <Slack permalink / call link + mm:ss / doc URL / Loom link / commit hash> · raw file: <repo path>
- Tier: primary | lead (unconfirmed)
- Public-ok: yes | no, <reason: client result without permission, internal number, client named>
- Claims: <the brand/claims.md row, or "not in claims">
- Route: post | X article | case study | YouTube | lead magnet
```

A field the source does not fill gets `[NEEDS: x]`. Never fill a field from a label or a guess.

## Rules

1. **Every card cites a source** with a link and a timestamp. No source, no card.
2. **A client result needs the client's yes.** Set `Public-ok: no` until the operator confirms the client's permission in chat.
3. **Never name a client in public.** Write "an account we manage" or "a client". The card also drops the client name and the account manager's name. Keep the niche only when the niche carries the lesson.
4. **Internal numbers stay internal.** Revenue, spend, margins, team pay, and anything someone marked "keep internal" get `Public-ok: no`.
5. **A number goes public only through `brand/claims.md`.** If it is not there, propose a claims row in the run report. Do not use it in a draft.
6. **The builder checks the draft.** The person in `Who` sees the draft before it posts. They fix the steps, not the style.
7. **Primary sources make cards. Lead sources only point.** A lead from a sales channel becomes a card only after a primary source confirms it.
8. **No invented detail.** Every descriptive claim points at a source line.

**Mauro's setup, one extra rule.** Work he does for the agency he runs content for is the agency's, and its numbers are the agency's. They never become his personal proof. A card from that work is `Public-ok: no` unless the exact claim is already in `brand/claims.md` as public.

## Route each card

| Route | When |
|---|---|
| post | One workflow step or one result, enough for a post |
| X article | A workflow with 5+ steps, a failure and a fix: `skills/content/article-origination.md` |
| case study | A client result with numbers, after the client says yes: `skills/ops/case-study-production.md` |
| YouTube | A workflow with enough steps and screen footage for one episode of a series |
| lead magnet | A workflow the reader can copy and run: `skills/lead-gen/lead-magnet/_master.md` |

A card can have two routes. Put the main route first.

Add a row to `content-log/post-tags.csv` **only when a post from a card is staged**, not when the card is written. See `content-log/README.md`.

## Output in chat

The top 5 cards by route, each with its source link and `Public-ok`. Then the permission asks (which client must say yes to which card), the `[NEEDS: x]` gaps, the proposed claims rows, and the paths of the files saved. The operator picks the cards.

## Done when

- Every channel in the table was read by ID for the full window. The run report lists each channel with its message count (0 is a valid count).
- Every call in the window is saved or listed as skipped with a reason.
- Changed docs and Drive files are saved or linked.
- `research/real-work/YYYY-Www/cards.md` exists, and every card has all fields filled or marked `[NEEDS: x]`.
- Each unconnected source is in the report as `[NEEDS]`.

## Self-check before the reply

- [ ] Each card has a link and a timestamp that opens the exact message or moment.
- [ ] No client name or account manager name appears in a card.
- [ ] Every internal number is `Public-ok: no`.
- [ ] Every number marked public is in `brand/claims.md`.
- [ ] No card rests on a lead source or a Claude-drafted doc alone.
- [ ] Each card names the builder who checks the draft.
- [ ] No row went into `post-tags.csv` for a card that is not staged.
