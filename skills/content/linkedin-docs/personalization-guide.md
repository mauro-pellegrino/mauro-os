# LinkedIn Doc Personalization Skill

How Nathan adapts a generic industry deck (e.g., `supplement-scaling.html`) into a per-prospect personalized deck before sending it as the second message in the DM 2-message punch.

Goal: prospect opens a doc with their brand name in the title and feels like Lorenzo built it specifically for them. Reality: ~5 string swaps in a generic master file. High perceived effort, low actual effort. Same wiz-style move that converts well on LinkedIn.

## Inputs Nathan needs before starting

1. **Prospect's brand name** (the client/company being DM'd). Example: "ProteinCo"
2. **Industry** of the prospect (supplement / skincare / pet / app)
3. **Approximate monthly spend tier** if known (optional, used in CTA only)
4. **Decision-maker name** (founder or CMO) — used in the DM, not in the deck

## The master files

- Supplement: `skills/content/linkedin-docs/industry-decks/supplement-scaling.html`
- Skincare: `skills/content/linkedin-docs/industry-decks/skincare-scaling.html`
- Pet: pending
- App: pending

## The swap checklist (open master HTML in a text editor, do find-and-replace)

| # | Find | Replace with | Required? |
|---|---|---|---|
| 1 | `How to Scale a Supplement Brand` (or appropriate industry phrasing) | `How [BrandName] Could Scale` | Required |
| 2 | `to $1M/Month on Meta` | Keep as-is, OR adapt to prospect's likely target tier ("to $1M/Month" stays generic) | Optional |
| 3 | `your supplement brand` (appears in bookmark hook) | `[BrandName]` | Required |
| 4 | `your [industry] account` (appears in CTA paragraph, section 5) | `[BrandName]'s account` | Recommended |
| 5 | `DM me "audit"` (CTA close) | `Reply to this thread for an audit on [BrandName]` (since this comes via DM, not a public post) | Required for DM use |

## Output handling

1. **Save the personalized HTML.** Default location: `accounts/lorenzo-x/personalized-decks/[industry]/[brand-slug].html`. Easier later for tracking which prospects got which version.
2. **Convert to PDF before sending** (LinkedIn renders HTML poorly inline; PDF carries the formatting). Use `Cmd+P → Save as PDF` on the rendered HTML page.
3. **Filename convention:** `[brand-slug]-supplement-scaling-deck.pdf` (e.g., `proteinco-supplement-scaling-deck.pdf`).

## Workflow Nathan runs (per prospect)

1. Prospect responds "yes" to Message 1 (permission ask) → trigger this skill.
2. Open the master HTML for their industry.
3. Run find-and-replace per the checklist above.
4. Save as `[brand-slug]-[industry]-deck.html` in `accounts/lorenzo-x/personalized-decks/[industry]/`.
5. Open the saved HTML in browser. Verify swaps look correct in rendered view.
6. Print to PDF. Save with same slug + `.pdf` extension.
7. Attach the PDF to Message 2 in the DM thread.
8. Log the prospect + version sent in the LinkedIn tracking sheet (per Mauro ↔ Nathan Apr 30 call decision).

## What NOT to change

- The $107M+ authority anchor (canonical, do not vary)
- Section structure (5 sections, fixed order)
- Public-example brand names in the body (Primal Queen, Arrae, etc. — these are positioning case studies, not client work)
- Footer ("— Lorenzo" + Growthub Brand Breakdowns)
- The closer italic line (universal across industries)

## Time budget per personalization

5-10 minutes. The swaps are minimal. The bulk of value comes from the deck quality itself, not the customization depth.

## Quality check before sending

- Brand name appears at least 3 times across the deck (title, bookmark hook, CTA)
- No leftover generic phrasing where a swap was missed
- PDF renders both pages cleanly with no overflow
- Filename matches the brand-slug convention
