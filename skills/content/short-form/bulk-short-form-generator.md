# Skill: Bulk Short-Form Generator (transcripts → TweetHunter CSV)

**Version:** 2.0
**Created:** 2026-07-06
**Updated:** 2026-07-14 (retargeted to Mauro's own brand, @maurojpelle)
**Input:** One or more source transcripts / session notes (`research/transcripts/maurojpelle/`, `brand/sessions/`)
**Output:** A TweetHunter-ready CSV (large batch of short-form posts) + a skim review sheet
**Builds on:** `skills/content/short-form/short-form-from-long-content.md` (same 6 templates + voice). This is the *bulk* version: many posts per source, no per-post human pick, machine QA instead.

---

## What this does + why

Mauro wants a steady short-form cadence without hand-writing every post. This skill mines his own source material (video transcripts, session notes, shipped articles and long-forms) and generates a large batch of short-form posts in his voice, formatted for **TweetHunter bulk import**. Target: ~12-20 usable posts per substantial source.

The source pool is thin today (few published videos). It grows as he ships. Never pad a batch with generic filler to hit a count; a tight 30 beats a padded 100.

Non-negotiable: quality stays at top-performer level. Volume never buys a drop in voice compliance or fabricated numbers.

---

## TweetHunter CSV format (strict)

Two columns, exact lowercase headers (TweetHunter matches headers exactly):

| Column | Required | Rule |
|---|---|---|
| `text` | yes | the post copy |
| `media_url` | no | hosted link ending in `.jpg` `.png` `.gif` `.mp4`; leave blank if none |

Imports land in **Drafts** (not auto-scheduled). So the batch = a draft queue Mauro reviews/schedules in TweetHunter.

Because `media_url` needs a *hosted* link, **skip Template A (caption tease) in bulk** — it depends on attached media we don't have URLs for. Bulk uses text-standalone templates: B, C, D, E, F. If a strong insight really needs media, put it in the review sheet flagged `NEEDS MEDIA`, not the CSV.

## Formatting + style (Mauro's rules, 2026-07-06; extended 2026-07-10 from his post-edit pass on earlier AI batches)

- **Line spacing:** blank line between every line/sentence in a post. Do NOT put blank lines inside a bulleted or numbered list (list items stay tight). In the CSV this means real newlines inside the quoted `text` field: `\n\n` between lines, single `\n` between list items.
- **One sentence per line (2026-07-10):** never put two sentences on the same line. Each sentence gets its own line with a blank line between. Mauro split "Nail the first frame and the video takes care of itself. Rush it and you pay for that mistake in every generation after." into two separate lines.
- **Enumerations become bullets (2026-07-10):** never list 3+ items inline in prose. "A-roll, B-roll, product shots" became a tight dash list, with the preceding line ending in a colon to introduce it. Inline enumeration is a rejection trigger.
- **Closer refinement (2026-07-10, TENTATIVE — confirm after Mauro's full edit pass):** the closer rule stands, but the closer is the last substantive line, not a bolt-on aphorism. Mauro cut "30 seconds per image. There's no excuse for skipping the check." and ended the post on the last real insight. Preachy or clever punchline closers get cut (consistent with voice.md's ban on punchline-preacher one-liners). Do not append a separate closer when the body's final line already lands.
- **Extract, then mimic.** Almost always build a post by extracting the insight from EXISTING material — Mauro's own past posts FIRST, then his transcripts and session notes — and matching his actual writing style. Pull real example posts and copy the rhythm, vocabulary, and structure. Do not write fresh from a blank page.
- **Quote-tweet + infographic is a core format.** Many of the best "short text" posts are actually quote tweets paired with a Claude-made infographic. Analytics exports do NOT flag QT / infographic / media, so treat pure-text length stats as directional only. Calibrate mainly by mimicking real posts.

## Two output types (confirm which per batch)

1. **Standalone text post** — pure text, sharp, one TweetHunter `text` row. Fast, high-volume, lower ceiling.
2. **Infographic companion (quote tweet)** — a short framing line + a Claude infographic. Higher ceiling but needs the infographic built (`skills/content/long-form/infographic-html-long-form.md`) and hosted, then placed in `media_url` or posted as a QT. More production per post.

Default to type 1 unless Mauro asks for type 2.

---

## Length calibration

[CALIBRATE: length-band performance data needs to be rebuilt from @maurojpelle's own X analytics once the account has posting volume. The previous calibration belonged to a different account and was confounded anyway (lead-magnet and media posts inflating the long end).]

What holds regardless of the data (Mauro, 2026-07-06): his real standalone style is **NOT one-liners.** Bare one-liners and thin 2-line tweets are rejected on sight ("where is the meat?"). Standalone posts are **beefy: ~4-6 lines with structure and substance mined from the source.**

**Every standalone post follows this shape:**
1. **Hook / contrarian opener** — a claim or a belief-break setup.
2. **Transition** — e.g. "Try this instead:", "Here's the uncomfortable part:", or a pivot line.
3. **Body (the meat)** — VARY the format across the batch: bulleted list, numbered list, or short story. Pull the specifics from the source so it's substantive, not generic.
4. **Closer** — end with a one-line closer that adds personality and closes it off (subject to the 2026-07-10 refinement above: the closer is the last substantive line, never a bolt-on aphorism).

Vary body format across the batch (~1/3 bullets, ~1/3 numbered, ~1/3 story/prose). Blank line between lines; list items stay tight.

## Winning shapes for pure text

Proven short-text shapes (structures, not copy):

- **Sharp insight statement** (~7-14w): one defensible claim, no setup.
- **Provocative one-liner** (~9-12w): challenge a default the ICP holds.
- **Mini-framework** (~17-20w): "[Setup line]: 1. [item] 2. [item] 3. [item]"

**Out of scope for this text-only skill** (higher ceiling, but need assets): lead-magnet / auto-DM posts and media breakdowns (video/image). Those drive the biggest numbers but require the auto-DM setup or a hosted media_url — handle via the lead-magnet skill or with real media, not here.

## The 6 tone templates

Template details + pattern formulas live in `skills/content/short-form/short-form-from-long-content.md`. Use these as *tone/angle* references, but let the winning structures above drive length:

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

- `brand/voice.md` — hard bans + pre-publish checklist
- `brand/positioning.md` + `brand/audience.md` — ICP (established agency owners) + language bank
- `brand/social-proof/` (create as results come in) — the ONLY source for verifying $ / result claims
- Mauro's own shipped posts (`brand/posts/`) — the style anchors to mimic

---

## Process

1. **Pick the batch** — the sources to mine. Log which sources were used (so the batch is traceable and not re-mined next time).
2. **Extract insights per source** — pull **12-20 distinct** strong insights each where the source supports it. An insight qualifies only if it is: specific to operator-grade work, defensible, compressible under 30 words, and surprising to the ICP (established agency owners at mid six figures/month and up). Write them in shorthand first.
3. **Map each insight to its best template** (B-F). Force template variety across the batch — no more than ~40% of any single template, so the feed doesn't read as a formula.
4. **Draft** each post in Mauro's voice. Sentence-case, full sentences. Compress hard.
5. **Verify every number** against the source or social-proof log. No fabricated specifics (`feedback_no_fabricated_performance_numbers`). If a number can't be verified, cut the claim or the post.
6. **QA each post** against the bans (below). Drop, don't soften, anything that fails twice.
7. **Write outputs** (below).

---

## Voice bans (auto-reject any post that hits one)

1. Em dashes — never.
2. "It's not X, it's Y" / "they aren't X, they're Y" reversal structures.
3. "Most brands/agencies…" openers.
4. Problem-to-purpose reframes ("that's the filter doing its job").
5. Filler openers: "Quick reminder", "Real talk", "Here's the thing", "Friendly reminder".
6. AI-staccato fragments (Mauro's spec is natural full sentences; auto-DMs are the exception, not this).
7. Unverified numbers.
8. Beginner-level framing (per `feedback_expert_not_beginner_positioning`).

---

## Outputs

Save to `brand/short-form-batches/` (create the folder on first batch):

1. **`YYYY-MM-DD-[batch-label].csv`** — columns `text,media_url`. One post per row. Quote fields containing commas; double internal quotes. This is the TweetHunter import.
2. **`YYYY-MM-DD-[batch-label]-review.md`** — a skim sheet: one row per post with `# | template | source | the post`. Mauro reviews here, deletes duds, then imports the CSV. Any `NEEDS MEDIA` posts live here only.

Per `feedback_article_workflow`, show a sample batch in chat and get Mauro's voice sign-off BEFORE writing full batches to the repo.

---

## Content veins (where the batch comes from)

1. **Transcript mining** (primary) — Mauro's own video transcripts in `research/transcripts/maurojpelle/` and session notes in `brand/sessions/`. Case studies and system breakdowns yield the most. Log used sources so the next batch pulls fresh ones.
2. **ICP pain-point FAQs** — the verbatim pains, desires, and failed attempts in `brand/audience.md` (voice-of-customer research). Cluster into recurring questions agency owners actually ask, then answer each as a beefy 4-6 line post (vary bullets / numbered / story). Answers must come from Mauro's real systems, not generic advice.
3. **Shipped long content** — articles, long-forms, and lead magnets already published (`brand/posts/`, `brand/lead-magnets/`), re-mined for standalone insights.

---

## Hand-off

Mauro reviews the review sheet → imports the CSV into TweetHunter Drafts → schedules there himself.

---

## Anti-patterns

- Generating from source surface (title, intro) instead of mining insights from the body.
- Padding a 7-word insight to fill a template's word ceiling.
- Same template 10 times in a row — vary across the batch.
- Fabricating a number to make a Template E post land.
- Putting a `NEEDS MEDIA` post in the CSV with a blank media_url (it'll ship as a naked claim).
- Treating a volume target as a licence to lower the bar. Cut weak posts; a tight 30 beats a padded 100.
