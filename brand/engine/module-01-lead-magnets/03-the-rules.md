# The Lead Magnet System

A working skill file. Paste it into Claude, Cursor, or whatever you run, and it will produce magnets that follow these rules instead of guessing.

Built and corrected across ~25 shipped magnets on a performance ad agency's account. Every rule below exists because something got rejected and rewritten, not because it sounded good.

---

## 1. What a lead magnet actually is

An artifact someone receives in exchange for a comment or an email.

Two things decide whether it works, and neither is the writing:

1. **The title names a thing**, not an idea.
2. **The inside is worth $100 of work they didn't have to do.**

Everything below is those two rules, in detail.

---

## 2. Title engineering

### The formula

```
[topic a beginner recognises] + [artifact noun] + [number or year]
```

Three jobs. The topic earns the scroll. The **artifact noun** creates the perceived value. The number or year makes it feel current and finite.

### The artifact noun is non-negotiable

The title has to name the thing that lands in their DMs.

**Approved nouns:** guide, playbook, checklist, sheet, kit, system, workflow, prompt file, stack, template, swipe file, breakdown, tutorial, formats, prompts.

### The evidence

40 magnet posts from one account, pulled July 2026.

| Post | Views | Comment rate |
|---|---|---|
| AUTODM AI | 59,471 | 0.9% |
| Winning Hooks Guide | 38,724 | 1.3% |
| Andromeda 101 | 27,918 | **3.9%** |
| Andromeda Redo | 20,934 | **4.0%** |
| AI Statics Workflow | 21,057 | 3.5% |

**Two separate effects, and people conflate them.**

- **Breadth drives reach.** "AI" is the widest word available and it topped views.
- **A concrete, currently-urgent named thing drives redemption.** Roughly 4x the comment rate. Comments are how they claim it, so redemption is the number that pays.

Aim for broad enough that a beginner recognises it, concrete enough that it feels urgent. Pick whatever is live and unresolved in your niche this month.

### Hard bans

- **No invented concept nouns.** Nobody wants a "camouflage static" or an "autopsy".
- **No diagnoses or questions.** "Why Your Ads Stopped Scaling" promises nothing received.
- **No sophistication signalling.** Broad title for reach, real depth inside for the qualified reader. That split is deliberate.

### Seven real corrections

Every one of these was written, rejected, and rewritten.

| Rejected | Shipped |
|---|---|
| The Camouflage Static Swipe File | Ads That Don't Look Like Ads (Full Playbook) |
| The 3-Bottleneck Ad Account Audit | The Meta Ads Audit Checklist (2026) |
| The Losing-Ad Autopsy Sheet | The Losing Ads Review Sheet |
| Rebuild a Competitor's Winner (Legally) | The Competitor Ad Teardown Kit |
| Selling to People Who Don't Know They Have the Problem | The 5 Awareness Levels Playbook |
| The $3k to $100k a Day Ladder | The Scaling Checklist: $3k to $100k a Day |
| GPT Native Ad Copy Prompt File | 10 Prompts for Native Ad Copy |

**The pattern in every single fix: stop being clever, name the object.**

---

## 3. The $100 bar

**Every magnet has to be worth at least $100 to the person who asks for it.** Not $100 of reading. $100 of work they did not have to do.

Two rules underneath it:

1. **It is a thing you fill in, not a thing you read.** If a page has no blank field, no row to score, and no verdict at the end, it is an article wearing a magnet's title.
2. **The last two pages are usually where the $100 lives.** The explainer pages are setup.

### The four artifacts that clear the bar

In order of value:

| | What it is |
|---|---|
| **Paste-ready prompts** | Variable slots, chained, in order. Include at least one that tells them no |
| **A real swipe file** | Named examples pulled apart beat by beat, plus a blank sheet for their own |
| **A scoring artifact** | Their numbers in, a verdict out: kill, iterate, scale |
| **A filled-in worked example** | The template completed for a real case, so they see what done looks like |

### The test

**If someone read the whole thing and did nothing differently tomorrow, it failed.** Regardless of how good the writing was.

### A worked case

One magnet went from 5 pages to 7. Page 6 added six paste-ready prompts with `[PRODUCT]` slots. Page 7 added seven real examples pulled apart plus a blank capture sheet.

Those two pages are where the $100 lives. The first five were the setup.

---

## 4. Structure

### Build it as separate pages, always

Every section is a **real, separately created child page** nested inside a parent. Never headings, toggles or dividers stacked on one long page.

End state: parent = cover + intro + N clickable subpages + CTA + credit line.

**If a build ends with all the content on the parent page, it is wrong. Rebuild it.**

Why it matters: a 7-page magnet that arrives as one scroll reads as a blog post. The same content as 7 clickable pages reads as a product.

### Page count

5 to 7 pages. Under 5 and it feels thin. Over 8 and they stop before the fill-in pages, which are the ones that actually deliver the value.

---

## 5. Images

### The rule

**The image ADDS to the page. It never restates it.**

The test before writing any prompt: cover the page text. Does the image still teach something? If no, it is decoration and it is wrong.

**Banned outright:** an infographic, stat card or "key takeaways" graphic whose content is a restatement of the text on the same page.

### Three allowed styles

| Style | When |
|---|---|
| **Real example screenshot** | Any page teaching a format or structure. **Strongest option, use it most** |
| **Worked example** | Any page whose deliverable is a template. Show it filled in |
| **Doodle scene** | Concept and mechanism pages only |

### Render vs generate

**Render as HTML and screenshot** when the image has more than ~30 words that must be exactly right, any table, checklist, aligned diagram boxes, or numbers you will want to change later.

**Generate with an image model** only for illustrative work. A doodle, a scene, a metaphor, one or two short labels.

**Never generate a fake example of a real thing.** A fabricated ad, a fabricated dashboard, a fabricated screenshot with invented engagement numbers. If the page teaches by example, the example has to be real. This is the fastest way to lose a reader who checks.

### Ship the prompts inside the asset

Every page carries two prompt blocks so the visuals never depend on inventing prompts later:

```
> **PAGE IMAGE PROMPT (16:9, <style>):** ...
> **HTML STYLE PROMPT:** ...
```

---

## 6. The cover image

It is the magnet's identity in the feed. Skipping it makes the post perform noticeably worse.

### Default: screenshot the magnet's own home page

Not a designed card. A clean screenshot of the asset's first screen.

- **Notion** → the parent page, showing title, intro and the list of subpages
- **Gamma** → slide one
- **PDF or HTML** → page one

**Why.** It shows the reader the actual thing they are about to receive, and the visible subpage list does the "what's inside" job for free. A designed card promises. A screenshot proves.

**What makes it work:** crop tight, no browser chrome, no cursor, no comment bubbles. Title legible at thumbnail size. Enough of the page list visible that they can count the pages. Retina capture, then downscale.

### Fallback: a designed card

Only when there is no asset yet, or its first screen is dull. Build it as HTML and screenshot it, do not generate it.

---

## 7. The post that delivers it

Structure:

1. **Hook** naming the problem, not the asset
2. **One line of proof** or a real number
3. **"I pulled apart / I built / here's what's inside:"**
4. **5 to 7 arrow bullets**, each naming a concrete thing they receive
5. **The keyword CTA**

The bullets are the actual sell. Each one has to name a deliverable, not a topic. "The split you're aiming for" beats "how to think about your funnel".

### The DM

**Name the page to start on.** Not a link and a hope.

> Here's the [magnet]. Page 3 is the one to do first. [One line on why that page matters most.]

That single instruction is the difference between a download and a read.

---

## 8. The five subtypes

Same rules above, different source material.

| Subtype | Source | Natural artifact |
|---|---|---|
| **Prompt swipe file** | Prompts you actually run | Paste-ready prompts with slots |
| **Framework** | A repeatable method you own | A scoring sheet or decision tree |
| **Case study** | One result, pulled apart | A worked example plus a template |
| **Video-sourced** | A transcript, yours or a competitor's | Whatever the video's structure implies |
| **Industry-specific** | One niche, one problem | A swipe file of real examples in that niche |

**The video-sourced one is the cheat code.** The source already exists, so the magnet starts from material rather than a blank page. Keep a transcript library and you never run out.

---

## 9. The thing nobody tells you: they fatigue

Five auto-DMs, one week, one account:

**7,839 → 6,329 → 4,369 → 1,637 → 901**

The fifth did **11% of the first, six days apart.**

Four of the five were the same asset, a file of ~10 prompts. Three opened on the same line.

But the first one beat every long-form post published that week except one. **So the mechanism is fine. Running one offer four times is what dies.**

**Rotate the asset shape, do not cut the volume.** Max one of any given asset type per week.

---

## 10. Measure the right thing

Most people track views. Views tell you the title was broad.

**Track the comment rate.** Comments are the redemption action, so that is the number that maps to leads.

And track two more that almost nobody fills in: **DMs received** and **qualified calls**. Without those you can correlate titles with attention and never with revenue.

---

*Adapt the examples. The rules carry.*
