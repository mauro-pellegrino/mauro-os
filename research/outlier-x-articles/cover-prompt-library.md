# Cover prompt library

> **STATUS: RESEARCH INPUT. NOT ADOPTED.** Reference covers saved for their look and their device, with
> copy-paste image prompts derived from them. Saved for prompting, not as a style Mauro has committed to.
> Nothing here enters `skills/` without sign-off.

Each entry: what the image is, the device that makes it work, and a prompt built to reproduce the device on
a different subject. Prompts are written for GPT image generation, plain prose, no parameter flags.

---

## 01. Watercolour plain, scribble head, annotated headline

**Captured:** 2026-09-02, pasted by Mauro. Image file not supplied, description is from the paste.
**Saved for:** the photo only. Not the title, not the body.

### What it looks like

- **Format:** wide landscape banner crop.
- **Medium:** watercolour and ink illustration. Soft, bleeding washes with loose charcoal linework over the top. Visible paper texture. Hand-made, not vector, not photographic.
- **Palette:** dusty rose and coral sky fading to pale cream at the horizon, muted sage and warm grey ground, charcoal-black ink for all line detail. Two colours doing all the work plus black.
- **Setting:** an open empty plain under a large sky. Low rolling hills on the horizon. Sparse scrubby grass sketched in quick ink strokes along the bottom edge. A single thin horizontal line, like a wire or a distant fence, crosses the frame.
- **Subject:** one man, centred, seated on the thin line with his legs hanging and hands resting in his lap. Light denim jacket, dark trousers. Slouched, patient, slightly defeated posture. Small in the frame, dwarfed by the empty landscape.
- **The device:** where his head should be there is a **dense scribbled ball of tangled black ink**, drawn as one continuous frantic loop, rising above the shoulders. No face at all.
- **Text:** the headline in heavy white sans-serif across the lower middle of the frame. Above it, one phrase in loose handwritten pink-red script, positioned as a correction sitting on top of a word in the printed headline, the way someone marks up a draft.

### Why it works

**1. The scribble carries the emotion with no face.** Overwhelm, confusion, too many open loops. It reads instantly and it never dates. It also means no likeness, no stock-photo person, no faceless-figure cliché.

**2. The empty landscape does the second half of the job.** One small figure in a huge empty plain says stuck and alone before you read anything. The scribble says why.

**3. The handwritten annotation over the printed headline is the best part.** The typed headline states the obvious version of the subject, and a scrawled edit corrects it to the real one. It reads as a marked-up draft, so the reader watches the author change their mind in the frame. It signals "the honest version is the handwritten one" without a word of argument.

**4. Soft palette against a hard subject.** Pretty watercolour, bleak content. The contrast is what stops the scroll.

### Prompt: the base

```
A wide landscape watercolour and ink illustration. An open empty plain under a
large dusty rose and coral sky that fades to pale cream at the horizon. Low
rolling hills far in the distance. Muted sage and warm grey ground with sparse
scrubby grass sketched in quick loose charcoal ink strokes along the bottom
edge. A single thin horizontal line like a distant wire crosses the frame.

One man sits centred on that line, legs hanging, hands resting in his lap,
slouched and patient. He wears a light denim jacket and dark trousers. He is
small in the frame, dwarfed by the landscape.

Where his head should be there is a dense scribbled ball of tangled black ink,
drawn as one continuous frantic loop, rising above his shoulders. No face.

Soft bleeding watercolour washes, visible paper texture, loose charcoal
linework over the top. Hand-painted, not digital, not photographic. Muted
two-colour palette plus black. Large areas of empty sky and empty ground.
Leave the lower middle third clear for text.
```

### Prompt: the swappable parts

Keep the medium, palette and the emptiness. Change these:

| Slot | This cover | Alternatives that keep the device |
|---|---|---|
| The scribble | Tangled ink ball for a head | A padlock, a maze, a closed laptop, a knot of cable, a stack of unopened envelopes |
| The posture | Seated on a wire, legs hanging, waiting | Standing at the end of a road that stops, walking in a circle of own footprints, holding a rope with no other end |
| The emptiness | Open plain, big sky | A flat salt pan, an empty car park, a bare field with one fence post, an open sea horizon |
| The palette | Dusty rose and sage | Any two muted colours plus charcoal. Keep it to two. |

### The annotation device, on its own

This part is done in the editor, not the generator, and it is the most reusable thing in the image. Generate the illustration clean, leave dead space, then add two text layers:

1. **The printed headline.** Heavy white sans-serif, lower middle of the frame, spanning most of the width. This states the flat, obvious version of the subject.
2. **The handwritten correction.** Loose script in one accent colour pulled from the illustration, sitting above and slightly overlapping a word in the printed headline, angled a few degrees off horizontal. Small, casual, clearly added after.

The correction should replace the *vague* word in the headline with the *specific* one. That is the whole mechanic: the reader sees the generic framing get overwritten with the real one.

Ask GPT for the illustration only. Do not ask it to render the headline or the handwritten note. Generated text comes back malformed and the annotation has to sit in a precise relationship to the printed word, which needs a layer you control.

---

## 02. Sunrise vista, lone figure from behind, no text at all

**From:** [02-first-ai-consulting-retainer.md](02-first-ai-consulting-retainer.md), `@coreyganim`, **170K views**.
**Captured:** 2026-09-02. Image file not supplied, description is from the paste.

### What it looks like

- **Format:** landscape, rendered above the title by the platform.
- **Medium:** soft digital painting in an anime / concept-art register (reads as AI-generated). Clean, glowing, no visible brushwork or paper texture.
- **Palette:** warm gold at the horizon through peach cloud to soft blue at the top. Saturated green meadow. Bright, optimistic, high key.
- **Setting:** sunrise over layered mountain ranges with a sea of low cloud filling the valleys. The sun sits low, left of centre, throwing rays across the frame. Foreground is a wildflower meadow in yellow, purple, pink and blue.
- **Subject:** one small figure sitting cross-legged in the meadow, **seen from behind**, dark hooded top, looking out at the view. Small in the frame.
- **Text:** none. No overlay, no lettering, no logo. The headline renders below the image as platform-styled white text.

### Why it works

**1. It sells the feeling, not the subject.** Nothing in the frame refers to AI, consulting, or retainers. It is
calm, arrival, the view after the climb. Pure aspiration.

**2. The figure is seen from behind, so the reader occupies it.** No face means no one to compare yourself to.
You are the person sitting there looking at the view. That is the entire mechanic, and it pairs exactly with a
"how to land your **first**" title aimed at someone who has not arrived yet.

**3. Clean image, platform-rendered title.** Nothing competes with the headline and nothing is at risk of being
cropped. It also means one illustration can be reused with any title.

**This is the opposite strategy to entry 01** and it is on the higher-reach article. Keep both.

### Prompt: the base

```
A wide landscape digital painting in a soft anime concept-art style. Sunrise
over layered mountain ranges, with a sea of low cloud filling the valleys
between them. The sun sits low on the horizon, left of centre, throwing warm
rays across the scene. The sky graduates from pale gold at the horizon through
peach clouds to soft blue at the top.

The foreground is a green meadow scattered with wildflowers in yellow, purple,
pink and blue.

One small figure sits cross-legged in the meadow, seen from behind, wearing a
dark hooded top, looking out at the view. Small in the frame, calm and still.
No face visible.

Soft glowing light, clean rendering, high-key and optimistic. No text, no
lettering, no logo anywhere in the image.
```

### Prompt: the swappable parts

Keep the from-behind figure, the high-key light and the absence of text. Change these:

| Slot | This cover | Alternatives that keep the device |
|---|---|---|
| The vantage | Cross-legged in a meadow above cloud-filled valleys | On a rooftop over a waking city, at the end of a pier at first light, on a ridge above a river valley |
| The time of day | Sunrise | Golden hour, first light after rain, clear dawn with mist burning off |
| The distance | Small in frame, vista dominates | Keep it small. The scale is what makes it aspirational rather than a portrait. |
| Text | None | None. Let the platform render the title. |

### When to use which

| | 01 engraving / argument cover | 02 vista / feeling cover |
|---|---|---|
| Says | here is the take | here is where this gets you |
| Suits | a rebuttal, a contrarian stance, a named enemy | a how-to, a ladder, a first-time-doing-this piece |
| Title sits | baked into the image | rendered below by the platform |
| Reader is | being argued with | being invited in |

---

## Also on file

The engraving-style cover in [01-saaspocalypse-is-overblown.md](01-saaspocalypse-is-overblown.md) is described in
that article's capture. Different device entirely: a single visual joke that states the thesis, black and
white, category name lettered into the set. Worth reading alongside this one, since between them they cover
the two cover classes the reach lane rewards.
