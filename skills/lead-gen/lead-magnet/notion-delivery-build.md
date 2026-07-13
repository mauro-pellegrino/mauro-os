# Lead Magnet: Notion Delivery Page Build (Chrome Extension Prompt)

**Created:** 2026-06-25
**Loaded with:** `_master.md` + the relevant subtype file
**Purpose:** The canonical Claude-Chrome-extension prompt for building the **Notion page the auto-DM links to** (the magnet's delivery page). The auto-DM lives in LeadShark and contains a LINK; that link points to the page this prompt builds.

---

## Why this exists

The Chrome extension reliably fails the same way: it dumps everything onto one page instead of nested subpages, and it skips the brand polish. This template forces the subpage structure and bakes in the standing formatting rules so every magnet page comes out consistent.

## Standing formatting rules (confirmed by Mauro 2026-06-25)

Apply these to EVERY lead-magnet Notion delivery page:

1. **Yellow cover image.** Set the parent page cover to a solid Growthub-yellow image/color block (brand yellow, ~`#F5D679`/`#FFC83D`).
2. **Growthub agency shout at the very top** of the parent page, before the intro (e.g. "Built by Growthub, the team behind $107M+ in managed Meta ad spend.").
3. **No emojis in subpage titles.** Plain text titles only.
4. **Calendly CTA at the bottom** of the parent page (and/or the final subpage): "Want us to run this for your brand? Book a call: `{{calendly_url}}`". If `{{calendly_url}}` is still PENDING in `accounts/[active]/account-config.md`, flag it as a blocker rather than inventing a link.
5. **"Created by Growthub.Agency"** credit line at the bottom.
6. **Force subpages.** The five sections must each be a nested child page, never headings on the parent.

## Token resolution

Substitute `{{calendly_url}}` and any other tokens from the active `accounts/[active]/account-config.md` before pasting. Magnet-specific content (title, subtitle, the asset, worked example) comes from the subtype's output.

---

## The template prompt (paste into Claude in the Chrome extension, Notion connected)

```
You are building a lead-magnet DELIVERY PAGE in Notion using the Notion integration.

═══════════════════════════════════════════
CRITICAL STRUCTURE RULE — READ TWICE
═══════════════════════════════════════════
Do NOT put all content on one page. Build ONE parent page, then create FIVE SEPARATE CHILD SUBPAGES nested inside it. Each section below is its own nested child page — NOT a heading, NOT a toggle, NOT a divider on the parent page.
If you catch yourself adding an H1/H2 for these sections on the parent page, STOP and make it a nested subpage instead.
End state: a parent page containing 5 clickable subpages.

FORMATTING RULES (apply all):
- Set the parent page COVER to a solid Growthub-yellow image/color.
- Subpage titles are PLAIN TEXT. No emojis.
- Put a Growthub shout line at the very top of the parent page.
- Put a Calendly CTA at the bottom of the parent page.
- End with a "Created by Growthub.Agency" line.
═══════════════════════════════════════════

PARENT PAGE
Cover: solid Growthub yellow.
Top line (Growthub shout): "Built by Growthub — the team behind $107M+ in managed Meta ad spend."
Title: [MAGNET TITLE]
Subtitle: [MAGNET SUBTITLE — number anchor + scale anchor]
Intro paragraph: [1-2 lines on what this is and how to start]
Then create the 5 subpages below as nested child pages.
Bottom of parent page: Calendly CTA — "Want us to run this for your brand? Book a call: {{calendly_url}}" — and a final line: "Created by Growthub.Agency".

SUBPAGE 1 — "Start Here: How to Use"
[Install / how-to steps]

SUBPAGE 2 — "The Asset (copy this)"
[The skill / prompts / file, inside ONE Notion code block if it's text to copy]

SUBPAGE 3 — "What's Inside"
[Bulleted summary of what the asset does]

SUBPAGE 4 — "Worked Example"
[A real, anonymized example showing the output shape]

SUBPAGE 5 — "Want a Free Breakdown?"
[The soft offer / reply CTA]

FINAL CHECK: parent page has exactly 5 nested subpages, a yellow cover, a Growthub shout at top, a Calendly CTA + Growthub.Agency credit at the bottom, and no emojis in any subpage title.
```

---

## After building

1. Notion → Share → Publish (publish to web) → copy the public URL.
2. Paste that URL as the LINK in the LeadShark auto-DM template (keyword + DM per the subtype). Settings: Auto-connect OFF, Partially Engage ON, Follow-up DM OFF.
