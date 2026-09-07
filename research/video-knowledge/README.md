# Video knowledge docs

Twelve information files, one per planned video. **These are not scripts.** Each one holds the
information the video is built on: what the system actually is, the numbers with their provenance,
what is measured against what is assumed, and the overclaims to avoid. The script gets written from
the doc, the board gets built from the script, and the video gets recorded off the board.

Written 2026-09-07 from both repos. 11 and 12 are a pair: the system as it runs today, then the
gap it does not cover. `mauro-os` supplied the transcripts, the digs and the voice.
`growthub-os` supplied the live system: 73 skill files, the article corpus, the ops conventions and
the measured numbers.

| # | File | The claim | Strongest evidence |
|---|---|---|---|
| 01 | [skills to agents](01-skills-to-agents.md) | Agents suit jobs where you already know what good looks like. Writing is not one yet. | 73 skill files, the four failures, the deliberate exception |
| 02 | [skills structure](02-skills-structure.md) | The index and the conventions are the asset, not the prompts. | The 45-minute rebuild incident, the three evidence tags |
| 03 | [lead magnets](03-lead-magnets-15-minutes.md) | 15 minutes of Claude sits inside a 2-3 hour cycle, and the keyword is the only measurement. | UTM filled on 4 of 541 bookings |
| 04 | [outlier corpus](04-outlier-swipe-corpus.md) | A swipe file is a dataset, and a winners-only dataset cannot tell you what fails. | 41 captures, the retracted title conclusion |
| 05 | [x ranking code](05-x-ranking-code.md) | The formula is public, the weights are not, and every circulating number is from 2023. | No params module in a 216-file tree |
| 06 | [cited in chatgpt](06-cited-inside-chatgpt.md) | A no-name page is cited as readily as a big publisher, until authority ranking ships. | One unverified source, labelled throughout |
| 07 | [channel teardown](07-reverse-engineer-channel.md) | An afternoon of structured looking gets the title formula, the thumbnail formula and ten titles. | Face in 9 of 10, seven title devices |
| 08 | [can't prove it](08-content-working-cant-prove-it.md) | Impressions and calls are independent on our own data. | Spearman +0.16, and 5,500 impressions outbooking 47,000 |
| 09 | [transcript to article](09-transcript-to-article.md) | Six skills in order plus a seventh that keeps them honest. | Every converter documents a process we operate |
| 10 | [record off a board](10-record-off-a-board.md) | A script makes you read, a board makes you talk. | 59 items built through the MCP, zero failures |
| 11 | [the $100k/mo system](11-claude-code-content-system.md) | The prompts are the least interesting part. The corrections, the provenance and the agents are the asset. | 73 skills, 4 agents, 25 tools, and the incident behind each agent |
| 12 | [q3 agents](12-q3-agents-for-booked-calls.md) | Every agent installed so far is defensive. None of them causes a call. | 4 scars, 7 candidates, and an honest count of two |

## How each file is laid out

The one claim · the information (the dense part) · an evidence table tagging every claim
`[measured]`, `[observed]` or `[assumed]` · the on-camera beats · what not to say · the gaps as
`[NEEDS: x]`.

## Gap status, 2026-09-07

Eight gaps closed by going back to the repos and re-running the scripts. What is left needs either
Mauro's decision or a recording-day re-check. Two things surfaced while closing them:

- **A phrasing error in the corpus.** "The bottom four booked 78% of the calls" is 78% *of what the
  top four booked*, not 78% of the set. Corrected in doc 08. The growthub-os evidence file and the
  script's own print statement still carry the ambiguous wording.
- **The keyword join does not exist yet.** The DM keyword is the only attributable path in
  principle, and nothing in the repo actually joins a keyword to a booking. What runs is same-day
  correlation, D and D-1, which the script itself calls correlation and not attribution.

## Standing rules these were written under

- Never invent a number. `$300k/mo` is the only pre-cleared public figure, and every other specific
  needs Mauro's sign-off before it is said on camera.
- Never name a client or an account, on screen or in narration.
- A gap beats a fabrication. Where a source is missing, the file says `[NEEDS: x]` and leaves it.
- Evidence tags follow `~/growthub-os/ops/CONVENTIONS.md`. An untagged claim is an assertion.
