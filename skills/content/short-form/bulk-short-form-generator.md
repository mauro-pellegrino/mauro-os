# Skill: Bulk Short-Form Generator (transcripts → TweetHunter CSV)

**Version:** 1.0
**Created:** 2026-07-06
**Input:** One or more YouTube transcripts (`research/transcripts/...`) + active account
**Output:** A TweetHunter-ready CSV (100+ short-form posts across a batch) + a skim review sheet
**Builds on:** `skills/content/short-form/short-form-from-long-content.md` (same 6 templates + voice). This is the *bulk* version: many posts per transcript, no per-post human pick, machine QA instead.

---

## What this does + why

Mauro produces ~15 short-forms/week and wants to stop hand-writing them. This skill mines YouTube transcripts (42+ Lorenzo videos available) and generates a large batch of short-form posts in the account's voice, formatted for **TweetHunter bulk import**. Target: 100+ posts from a batch of ~6-10 transcripts (~12-20 usable posts per transcript).

Non-negotiable: quality stays at the level of the analyzed top-performers. Volume never buys a drop in voice compliance or fabricated numbers.

---

## TweetHunter CSV format (strict)

Two columns, exact lowercase headers (TweetHunter matches headers exactly):

| Column | Required | Rule |
|---|---|---|
| `text` | yes | the post copy; **variable length per the data bands below** (winners run ~40-60 words, not ultra-short) |
| `media_url` | no | hosted link ending in `.jpg` `.png` `.gif` `.mp4`; leave blank if none |

Imports land in **Drafts** (not auto-scheduled). So the batch = a draft queue Mauro reviews/schedules in TweetHunter.

Because `media_url` needs a *hosted* link, **skip Template A (caption tease) in bulk** — it depends on attached media we don't have URLs for. Bulk uses text-standalone templates: B, C, D, E, F. If a strong insight really needs media, put it in the review sheet flagged `NEEDS MEDIA`, not the CSV.

## Formatting + style (Mauro's rules, 2026-07-06; extended 2026-07-10 from his post-edit pass on the Bogdan AI batches)

- **Line spacing:** blank line between every line/sentence in a post. Do NOT put blank lines inside a bulleted or numbered list (list items stay tight). In the CSV this means real newlines inside the quoted `text` field: `\n\n` between lines, single `\n` between list items.
- **One sentence per line (2026-07-10):** never put two sentences on the same line. Each sentence gets its own line with a blank line between. Mauro split "Nail the first frame and the video takes care of itself. Rush it and you pay for that mistake in every generation after." into two separate lines.
- **Enumerations become bullets (2026-07-10):** never list 3+ items inline in prose. "A-roll, B-roll, product shots" became a tight dash list, with the preceding line ending in a colon to introduce it. Inline enumeration is a rejection trigger.
- **Closer refinement (2026-07-10, TENTATIVE — confirm after Mauro's full Notion edit pass):** the closer rule stands, but the closer is the last substantive line, not a bolt-on aphorism. Mauro cut "30 seconds per image. There's no excuse for skipping the check." and ended the post on the last real insight. Preachy or clever punchline closers get cut (consistent with voice.md's ban on punchline-preacher one-liners). Do not append a separate closer when the body's final line already lands.
- **Extract, then mimic.** Almost always build a post by extracting the insight from EXISTING material — their own past posts FIRST, then YouTube transcripts — and matching their actual writing style. Pull real example posts and copy the rhythm, vocabulary, and structure. Do not write fresh from a blank page.
- **Quote-tweet + infographic is a core format.** Many of the best "short text" posts are actually quote tweets paired with a Claude-made infographic (e.g. the "reviews are important" post). The analytics export does NOT flag QT / infographic / media, so treat the pure-text length stats as directional only. Calibrate mainly by mimicking real posts.

## Two output types (confirm which per batch)

1. **Standalone text post** — pure text, sharp, one TweetHunter `text` row. Fast, high-volume, lower ceiling.
2. **Infographic companion (quote tweet)** — a short framing line + a Claude infographic. Higher ceiling but needs the infographic built (`skills/content/long-form/infographic-html-long-form.md`) and hosted, then placed in `media_url` or posted as a QT. More production per post.

Default to type 1 unless Mauro asks for type 2.

---

## Length: short + sharp for pure text (de-confounded)

A first pass looked like "longer wins." It didn't — that read was confounded by lead-magnets and media. Re-analysis of 2,240 posts (2026-01-01+) split by type:

| Class | n | Median imp |
|---|---|---|
| Lead-magnet / auto-DM | 62 | 2,639 |
| Link / CTA-to-media (video, article) | 264 | 1,051 |
| **Pure-text short-form** | 466 | 33 |
| Noise / link-only | 1,448 | 7 |

The long "winners" were lead-magnets and posts with attached video/image, not text. This skill produces **pure text** (TweetHunter text has no media), so calibrate on the pure-text cohort only:

| Words | Median imp | Read |
|---|---|---|
| 4-8 | 27 | hit-or-miss |
| 9-13 | 11 | high variance: most flop, but the biggest absolute hits live here |
| **14-18** | **1,629** | **most reliable band** |
| 19-25 | 765 | fine |
| 26-45 | ~770 | no gain from length |
| 46-60 | 811 | no gain from length |

**OVERRIDE (Mauro, 2026-07-06): the length data above is confounded** (truncated export + infographic/lead-magnet posts inflating the long end). Mauro's real standalone style is **NOT one-liners.** Bare one-liners and thin 2-line tweets are rejected on sight ("where is the meat?"). Standalone posts are **beefy: ~4-6 lines with structure and substance mined from the transcript.**

**Every standalone post follows this shape:**
1. **Hook / contrarian opener** — a claim or a "most people think X" setup.
2. **Transition** — e.g. "Try this instead:", "Here's the uncomfortable part:", or a pivot line.
3. **Body (the meat)** — VARY the format across the batch: bulleted list, numbered list, or short story. Pull the specifics from the transcript so it's substantive, not generic.
4. **Closer** — ALWAYS end with a one-line closer that adds personality and closes it off. Non-negotiable per Mauro; a post without a closer is incomplete.

Vary body format across the batch (~1/3 bullets, ~1/3 numbered, ~1/3 story/prose). Blank line between lines; list items stay tight. Live calibration from the pick-game: `accounts/lorenzo-x/short-form-preferences.md`.

## Winning shapes for pure text (top clean-text posts, Jan 1+)

The highest-impression PURE-TEXT posts are short and sharp:

- **Sharp insight statement** (~7-14w): one defensible claim, no setup. "This is literally why reviews are so important in your research" (23K). "This is how you create winning ads" (16K).
- **Provocative one-liner** (~9-12w): "Your ads suck. With this maybe a bit less." (11K).
- **Mini-framework** (~17-20w): "Our 3 highest spending formats this year: 1. Podcast style ads 2. Street interviews 3. Skit conversations" (15K).

**Out of scope for this text-only skill** (higher ceiling, but need assets): lead-magnet / auto-DM posts (the "$107M... I've built a file with 10 prompts" format) and media breakdowns (video/image). Those drive the biggest numbers but require the auto-DM setup or a hosted media_url — handle via the lead-magnet skill or with real media, not here.

## The 6 tone templates (from the data layer)

Full anchor examples + impression data: `research/x-analytics-exports/short-forms-2026-top-performers.md`. Use these as *tone/angle* references, but let the winning structures above drive length:

| # | Template | Use |
|---|---|---|
| A | Caption tease | points to media *(skip in bulk — no hosted media URL)* |
| B | Insight statement | one sharp standalone claim |
| C | Mini-framework | numbered 3-item list |
| D | Provocative one-liner | challenge a default |
| E | Specific number flex | curiosity on a real number |
| F | Follow tease | upcoming-content signal (max ~1 per batch) |

---

## Required reading before generating

- `accounts/[active]/` voice + positioning (default Lorenzo: `accounts/lorenzo-x/post-voice-positioning.md`)
- `brands/growthub/voice.md` — hard bans + pre-publish checklist
- `accounts/lorenzo-x/wins-log.md` — the ONLY source for verifying $ / result claims
- `research/x-analytics-exports/short-forms-2026-top-performers.md` — the template examples

---

## Process

1. **Pick the batch** — the transcripts to mine + the active account. Log which transcripts were used (so the batch is traceable and not re-mined next time).
2. **Extract insights per transcript** — pull **12-20 distinct** strong insights each (not the 3-5 of the manual skill). An insight qualifies only if it is: specific to operator-grade work, defensible, compressible under 30 words, and surprising to the ICP (brand operators $100K-$1M+/mo). Write them in shorthand first.
3. **Map each insight to its best template** (B-F). Force template variety across the batch — no more than ~40% of any single template, so the feed doesn't read as a formula.
4. **Draft** each post in the account voice. Sentence-case, full sentences (91% of top posts are). Compress hard.
5. **Verify every number** against the transcript or wins-log. No fabricated specifics (`feedback_no_fabricated_performance_numbers`). If a number can't be verified, cut the claim or the post.
6. **QA each post** against the bans (below). Drop, don't soften, anything that fails twice.
7. **Write outputs** (below).

---

## Voice bans (auto-reject any post that hits one)

1. Em dashes — never.
2. "It's not X, it's Y" / "they aren't X, they're Y" reversal structures.
3. "Most brands/accounts…" openers UNLESS immediately followed by a sharp Growthub-specific counter-claim.
4. Problem-to-purpose reframes ("that's the filter doing its job").
5. Filler openers: "Quick reminder", "Real talk", "Here's the thing", "Friendly reminder".
6. AI-staccato fragments for Lorenzo (his spec is natural full sentences; auto-DMs are the exception, not this).
7. Unverified numbers.

---

## Outputs

Save to `accounts/[active]/short-form-batches/`:

1. **`YYYY-MM-DD-[account]-[batch-label].csv`** — columns `text,media_url`. One post per row. Quote fields containing commas; double internal quotes. This is the TweetHunter import.
2. **`YYYY-MM-DD-[account]-[batch-label]-review.md`** — a skim sheet: one row per post with `# | template | source transcript | the post`. Mauro reviews here, deletes duds, then imports the CSV. Any `NEEDS MEDIA` posts live here only.

Per `feedback_article_workflow`, show a sample batch in chat and get Mauro's voice sign-off BEFORE writing full batches to the repo.

---

## Content veins (where the 100+ come from)

1. **Transcript mining** (primary) — ~12-20 posts × 6-10 transcripts. Prioritize Lorenzo's 42 transcripts (case studies + strategy breakdowns yield the most). Log used transcripts so the next batch pulls fresh ones.
2. **Calendly pain-point FAQs** — aggregate the Q4 responses ("What are the main problems you're facing to hit your target revenue?") from `research/q1-q2-content-vs-calls/raw-data/calendly-lorenzo.csv` (364 qualified bookers). Cluster into ~30 recurring FAQs, then answer each as a beefy 4-6 line tweet (vary bullets / numbered / story). This is content pulled straight from what qualified buyers actually say, so it maps 1:1 to booking pain points.

## How to hit 100+

Run vein-by-vein, append to the same batch CSV. Transcripts + the ~30 Calendly FAQs alone clear 100+.

---

## Hand-off

Mauro reviews the review sheet → imports the CSV into TweetHunter Drafts → schedules there. (This replaces the old Joao → Hypefury hand-off for short-form. Keep Hypefury only if a specific post needs it.)

---

## Anti-patterns

- Generating from transcript surface (title, intro) instead of mining insights from the body.
- Padding a 7-word insight to fill a template's word ceiling.
- Same template 10 times in a row — vary across the batch.
- Fabricating a number to make a Template E post land.
- Putting a `NEEDS MEDIA` post in the CSV with a blank media_url (it'll ship as a naked claim).
- Treating 100+ as a licence to lower the bar. Cut weak posts; a tight 80 beats a padded 120.
