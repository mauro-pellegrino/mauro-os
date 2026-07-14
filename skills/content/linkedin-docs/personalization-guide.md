# LinkedIn Doc Personalization Skill

How to adapt a generic niche deck into a per-prospect personalized deck before sending it as the second message in a DM 2-message punch. Runnable by Mauro or a VA.

Goal: the prospect opens a doc with their name in the title and feels like Mauro built it specifically for them. Reality: ~5 string swaps in a generic master file. High perceived effort, low actual effort.

## Inputs needed before starting

1. **Prospect's business name** (the agency being DM'd). Example: "NorthPeak Digital"
2. **Niche** of the prospect (which master deck fits: their agency type or vertical)
3. **Approximate size tier** if known (optional, used in CTA only)
4. **Decision-maker name** (founder) — used in the DM, not in the deck

## The master files

- `skills/content/linkedin-docs/industry-decks/linkedin-doc-template.html` (clean structural template with placeholder copy)
- Mauro-lane master decks (e.g., "How to Build an Inbound Engine for a [niche] Agency"): pending. Build them with `skills/content/linkedin-docs/README.md` + `skills/content/long-form/linkedin-html-doc-guide.md` before running this workflow at volume.

## The swap checklist (open master HTML in a text editor, do find-and-replace)

| # | Find | Replace with | Required? |
|---|---|---|---|
| 1 | The generic title (e.g., `How to Build an Inbound Engine for a [Niche] Agency`) | `How [ProspectName] Could Build an Inbound Engine` | Required |
| 2 | The outcome phrase in the subtitle | Keep as-is, OR adapt to the prospect's likely target tier | Optional |
| 3 | `your agency` (appears in the bookmark hook) | `[ProspectName]` | Required |
| 4 | `your [niche] agency` (appears in the CTA paragraph) | `[ProspectName]` | Recommended |
| 5 | `DM me "[trigger]"` (CTA close) | `Reply to this thread and I'll [specific deliverable] for [ProspectName]` (since this comes via DM, not a public post) | Required for DM use |

## Output handling

1. **Save the personalized HTML.** Default location: `skills/content/linkedin-docs/personalized-decks/[niche]/[prospect-slug].html` (create the folder as prospects come in). Easier later for tracking which prospects got which version.
2. **Convert to PDF before sending** (LinkedIn renders HTML poorly inline; PDF carries the formatting). Use `Cmd+P → Save as PDF` on the rendered HTML page.
3. **Filename convention:** `[prospect-slug]-[niche]-deck.pdf` (e.g., `northpeak-seo-agency-deck.pdf`).

## Workflow per prospect

1. Prospect responds "yes" to Message 1 (permission ask) → trigger this skill.
2. Open the master HTML for their niche.
3. Run find-and-replace per the checklist above.
4. Save as `[prospect-slug]-[niche]-deck.html` in `skills/content/linkedin-docs/personalized-decks/[niche]/`.
5. Open the saved HTML in browser. Verify swaps look correct in rendered view.
6. Print to PDF. Save with same slug + `.pdf` extension.
7. Attach the PDF to Message 2 in the DM thread.
8. Log the prospect + version sent in a tracking sheet.

## What NOT to change

- The authority anchor line (keep it canonical across all sends; pull it from `brand/positioning.md` and get Mauro's sign-off on any specific number)
- Section structure (fixed order)
- Public-example names in the body (positioning case studies, never client work)
- Footer ("— Mauro")
- The closer italic line (universal across niches)

## Time budget per personalization

5-10 minutes. The swaps are minimal. The bulk of value comes from the deck quality itself, not the customization depth.

## Quality check before sending

- Prospect name appears at least 3 times across the deck (title, bookmark hook, CTA)
- No leftover generic phrasing where a swap was missed
- PDF renders both pages cleanly with no overflow
- Filename matches the prospect-slug convention
