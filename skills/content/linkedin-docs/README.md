# Skill: LinkedIn Document Carousel Generator
**Version:** 2.0
**For:** @maurojpelle
**Output:** Multi-page LinkedIn document carousel (1080x1350 per page) as both HTML and PNG images, modeled after the Josh Chin reference style.

> **Repo adaptation note (2026-05-07):** This skill was originally written for a Claude.ai project environment that wrote files to `/mnt/user-data/outputs/`. In this repo, outputs go to `skills/content/linkedin-docs/industry-decks/[name]-linkedin-doc.html` and the corresponding PNGs sit alongside. The Playwright export script needs its paths updated when running locally. The clean structural template is `industry-decks/linkedin-doc-template.html`; start every new deck from it.

---

## When To Use This Skill

Use this skill when the user wants to convert any of the following into a LinkedIn document carousel:

- A long-form article (X article, blog post, newsletter)
- A tweet or short post that has enough substance for visual treatment
- Raw notes or bullets that need to be packaged
- A specific concept or framework Mauro wants to teach

The output is always a LinkedIn-ready visual carousel, not a text post or copy. **This skill never produces the LinkedIn post caption that accompanies the images.** The user writes that themselves.

---

## Required Reading Before Output

Before generating any HTML or copy:

1. Read `brand/voice.md` in full. All copy must pass the pre-publish checklist in voice.md.
2. Read `brand/positioning.md` and `brand/audience.md` so every deck speaks to established agency owners, not beginners.
3. Confirm the user has provided source content (article, tweet, or notes). If not, ask for it.

---

## Step 1: Clarifying Questions

Always ask these questions before building. Never assume. Wait for answers.

**Question 1: Page count**
"How many pages do you want? Based on the content density I'd recommend [X], but options are 1, 2, or 3 pages."

Use this guideline to recommend:
- **1 page:** Short tweet, single concept, simple framework with 3-4 components
- **2 pages:** Standard article (~700-1200 words), 4-5 sections, balanced tactical content
- **3 pages:** Long article (~1500+ words), 5-7 sections, multiple frameworks layered

**Question 2: Target page balance**
For 2-3 page outputs, ask: "Should each page have roughly equal density, or do you want the first page lighter (intro + one section) and later pages denser?"

Default: equal density across pages. The Josh Chin reference uses equal density.

**Question 3: Title and subtitle**
"What's the headline you want on page 1? And do you want a one-line subtitle under it (typically a credibility anchor)?" Anchors come from `brand/positioning.md`; any specific public number needs Mauro's sign-off.

**Question 4: CTA trigger**
"What DM trigger word should the CTA use? Or skip the CTA?" [CALIBRATE: standard trigger words for Mauro's offers are not defined yet. Confirm the trigger with him per deck.]

**Question 5: File naming**
"What should the file be named? I'll use kebab-case based on the topic (e.g., 'inbound-engine-linkedin-doc'). Confirm or suggest your own."

Once these are answered, proceed to build.

---

## Step 2: Content Structuring Logic

### Section count per page
- 1-page output: 2-3 sections
- 2-page output: 2 sections per page (4 total)
- 3-page output: 2 sections per page (6 total)

### Section content rules
Each section needs:
- One section header (orange, 32px)
- 2-4 short body paragraphs (max 3 sentences each)
- One visual element (table OR yellow callout, sometimes both)
- Optional: one italic blue takeaway line at the end

### Visual element selection per section

Pick the right visual element based on the section's content type:

**Use the 3-row key/value table when:**
- The section breaks one concept into 3 named components (e.g., "the play / why it works / the trick")
- The section explains a 3-part framework
- The section lists 3 sub-strategies under one umbrella

**Use the 2-column comparison table when:**
- The section frames "what's wrong vs what works"
- The section compares "before vs after"
- The section contrasts old approach vs new approach
- The section has clear "burned out vs working" framing

**Use a yellow highlighted callout box when:**
- The section has a single punchline that deserves visual emphasis
- A specific stat or quote is the centerpiece
- The body text builds to a one-line "aha" moment

**Use an italic blue takeaway line when:**
- The section ends with a strategic lesson worth isolating
- The takeaway extends beyond the section's specific topic

**You can combine these.** Most sections work best with one table + one italic blue takeaway. Adding a yellow callout makes it denser, useful for the second page when balancing visual weight.

### Density balancing across pages

After drafting all sections, count the visual elements per page:
- Tables per page
- Yellow callouts per page  
- Italic blue takeaways per page
- Total body paragraphs per page

If one page has significantly more visual weight than another, rebalance by either:
- Moving a section to the lighter page
- Adding a yellow callout to the lighter page
- Splitting a body paragraph

The Josh Chin reference shows page 1 and page 2 with similar density (3 sections + 3 tables on page 1, 2 sections + 2 tables on page 2 with the closer/footer adding weight to page 2). Match this balance.

---

## Step 3: HTML Template

Start from `industry-decks/linkedin-doc-template.html` (clean structural template with placeholder copy). Do not modify the CSS values. Only swap content.

### Key template parameters

**Page dimensions:** 1080x1350 per page (4:5 LinkedIn ratio). Hardcoded. Do not change.

**Color palette:**
- Section headers: `#e8572a` (orange)
- Handle (@maurojpelle): `#3b6cdf` (blue)
- Italic blue lines: `#3b6cdf`
- Yellow callouts: `#ffe75e` background, `#1a1a1a` text
- Green inline emphasis: `#188d4d`
- Body text: `#1a1a1a`
- Bookmark border: `#e8572a`

**Table label colors (3-row table):**
- Yellow: `#f5d572`
- Blue: `#7ba0e0` (with white text)
- Pink: `#f4c5d0`
- Orange: `#f5b86b` (rare, for 4-row tables)

**Comparison table colors (2-column):**
- Red header: `#e87870` (white text)
- Green header: `#5fa861` (white text)
- Cell colors rotate: red → yellow → pink (left column), white → green-light → blue-light (right column)

**Footer:**
- "— Mauro" on the left
- Right side empty (the legacy script-font brand mark is retired; see `skills/content/long-form/linkedin-html-doc-guide.md`)
- Footer only on the LAST page

---

## Step 4: Voice Rules

All copy must pass `brand/voice.md`. Run the checklist before finalizing:

1. Zero em dashes. Use commas, periods, or rewrite.
2. Zero "it's not X, it's Y" structures (and all variants like "the X isn't Y, it's Z").
3. Zero "most brands / most people / most X" openers.
4. Maximum 2-3 colons across the entire document.
5. No parallel rhythm triplets (three short stacked sentences).
6. No "powerful," "game-changing," "transformational," "unlock your potential," etc.
7. Specific numbers throughout, only real ones from Mauro's own work or bracketed placeholders. Never fabricate.
8. Named external examples where possible (public examples relevant to agency owners, never client names).
9. Read every body paragraph aloud. If it sounds like a copywriting exercise, rewrite as plain speech.

The handle is always `@maurojpelle`. The footer signature is always `— Mauro` on the left, right side empty.

The CTA pattern is always:
"If you [qualifier matching audience tier], DM me '[trigger]' and I'll [specific deliverable]."

[CALIBRATE: confirm the trigger word with Mauro per deck until standard triggers exist.]

---

## Step 5: PNG Export

After the HTML is finalized, automatically export each page as a separate PNG using Playwright.

### Export script

Save the HTML to the target output directory first.

Then run this Python script to export PNGs:

```python
from playwright.sync_api import sync_playwright
import os

def export_pages(html_path, output_dir, base_name):
    """Export each page from a multi-page LinkedIn doc HTML as separate PNGs."""
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Set viewport wide enough to fit a page + browser background
        page = browser.new_page(viewport={'width': 1200, 'height': 1450})
        
        # Load the HTML file
        page.goto(f'file://{os.path.abspath(html_path)}')
        page.wait_for_load_state('networkidle')
        
        # Find all .page elements
        page_elements = page.query_selector_all('.page')
        print(f"Found {len(page_elements)} pages to export")
        
        exported_files = []
        for i, element in enumerate(page_elements, 1):
            output_path = f"{output_dir}/{base_name}-page-{i}.png"
            element.screenshot(path=output_path)
            exported_files.append(output_path)
            print(f"Exported: {output_path}")
        
        browser.close()
        return exported_files

# Usage:
# export_pages(
#     html_path='skills/content/linkedin-docs/industry-decks/[deck-name].html',
#     output_dir='skills/content/linkedin-docs/industry-decks',
#     base_name='[deck-name]'
# )
```

The output is one PNG per page, named `{base_name}-page-1.png`, `{base_name}-page-2.png`, etc. Each PNG is exactly 1080x1350 (the natural size of the .page div).

Present both the HTML and the PNG files to the user. List the PNGs first since those are what they'll actually post.

---

## Step 6: Output Order

Always deliver in this order:

1. The PNG files (one per page) — present these first, since these are what gets posted
2. The HTML file (in case the user wants to edit before re-exporting)
3. A short summary message that:
   - Lists the page count
   - Names what's on each page (section headers)
   - Confirms the PNG dimensions (1080x1350 each, ready for LinkedIn)
   - Reminds the user that voice.md was applied

Never include the LinkedIn post caption. The user writes that themselves.

---

## File Naming Convention

Always use kebab-case based on the topic. Examples:
- `inbound-engine-linkedin-doc.html` + `inbound-engine-linkedin-doc-page-1.png` + `inbound-engine-linkedin-doc-page-2.png`
- `ai-content-system-linkedin-doc.html` + corresponding PNGs

Drop the year unless the article is explicitly date-anchored.

---

## Common Mistakes to Avoid

1. **Don't write LinkedIn caption copy.** This skill only outputs the visual. The user writes the post text.
2. **Don't use em dashes anywhere in the doc.** Even in the HTML comments. They train the eye to expect them in copy.
3. **Don't make pages overflow.** If content is too dense, propose more pages instead of cramming.
4. **Don't deviate from the Josh Chin visual reference.** The whole point of this format is recognition. Stay on-template.
5. **Don't skip the clarifying questions step.** Page count, page balance, title/subtitle, CTA trigger, and filename should all be confirmed before building.
6. **Don't forget the footer on the last page only.** The "— Mauro" signature appears once, at the bottom of the final page.
7. **Don't use inline `<br>` for line breaks in body copy.** Use separate `<p>` elements. Cleaner styling.
8. **Don't put more than 3 sections on a single page.** Layout breaks. Propose adding a page instead.

---

## Reference: Existing Outputs

- `skills/content/linkedin-docs/industry-decks/linkedin-doc-template.html` (2-page clean structural template, placeholder copy)

When in doubt about visual treatment, open the template and copy the structure. As finished Mauro-lane decks accumulate in `industry-decks/`, prefer the most recent one as the visual reference.

---

## Related skill: per-prospect personalization

`personalization-guide.md` (in this same folder) describes the workflow for adapting a generic deck into a per-prospect personalized version with the prospect's name embedded. Different workflow, downstream of this generation skill.
