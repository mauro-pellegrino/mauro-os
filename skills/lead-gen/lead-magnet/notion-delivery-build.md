# Lead Magnet: Notion Delivery Page Build (Chrome Extension Prompt)

**Version:** 1.1 (retargeted to Mauro's brand, 2026-07-14)
**Loaded with:** `_master.md` + the relevant subtype file
**Purpose:** The canonical Claude-Chrome-extension prompt for building the **Notion page the auto-DM links to** (the magnet's delivery page). The auto-DM lives in LeadShark and contains a LINK; that link points to the page this prompt builds.

---

## Why this exists

The Chrome extension reliably fails the same way: it dumps everything onto one page instead of nested subpages, and it skips the brand polish. This template forces the subpage structure and bakes in the standing formatting rules so every magnet page comes out consistent.

## Standing formatting rules

Apply these to EVERY lead-magnet Notion delivery page:

1. **Brand-color cover image.** Set the parent page cover to a solid brand-color block. [BRAND COLOR — visual identity for @maurojpelle pending; pick one color and reuse it on every magnet so the pages read as one system.]
2. **Authority line at the very top** of the parent page, before the intro. Use a signed-off proof line from `_master.md` (e.g. "Built by Mauro, who runs this exact engine daily for a real B2B agency."). Never borrow the agency's client anchors.
3. **No emojis in subpage titles.** Plain text titles only.
4. **Booking CTA at the bottom** of the parent page (and/or the final subpage): "Want this installed in your agency? Book a call: `{{calendly_url}}`". `{{calendly_url}}` is [PENDING — no booking link exists yet]. Flag it as a blocker rather than inventing a link.
5. **"Created by @maurojpelle"** credit line at the bottom.
6. **Force subpages.** The five sections must each be a nested child page, never headings on the parent.

## Token resolution

Substitute `{{calendly_url}}` and any other tokens per the Token Resolution section in `_master.md` before pasting. Magnet-specific content (title, subtitle, the asset, worked example) comes from the subtype's output.

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
- Set the parent page COVER to a solid [BRAND COLOR] image/color.
- Subpage titles are PLAIN TEXT. No emojis.
- Put the authority line at the very top of the parent page.
- Put a booking CTA at the bottom of the parent page.
- End with a "Created by @maurojpelle" line.
═══════════════════════════════════════════

PARENT PAGE
Cover: solid [BRAND COLOR].
Top line (authority line): "[SIGNED-OFF PROOF LINE, e.g. Built by Mauro, who runs this exact engine daily for a real B2B agency.]"
Title: [MAGNET TITLE]
Subtitle: [MAGNET SUBTITLE — number anchor + scale anchor, real and signed off]
Intro paragraph: [1-2 lines on what this is and how to start]
Then create the 5 subpages below as nested child pages.
Bottom of parent page: booking CTA — "Want this installed in your agency? Book a call: {{calendly_url}}" — and a final line: "Created by @maurojpelle".

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

FINAL CHECK: parent page has exactly 5 nested subpages, a brand-color cover, an authority line at top, a booking CTA + @maurojpelle credit at the bottom, and no emojis in any subpage title.
```

---

## After building

1. Notion → Share → Publish (publish to web) → copy the public URL.
2. Paste that URL as the LINK in the LeadShark auto-DM template (keyword + DM per the subtype). Settings: Auto-connect OFF, Partially Engage ON, Follow-up DM OFF.
