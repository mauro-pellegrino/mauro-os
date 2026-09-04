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

## 03. Vintage engraving, candlestick phone, cord climbing into a staircase

**Source account:** `@knoxtwts` (handle read off the screenshot)
**Article title:** `how to build a customer acquisition system that gets smarter after every lead`
**Captured:** 2026-09-02. **Cover and title only — no body text, no view count.** Image file not supplied.
**Saved for:** the photo.

### What it looks like

- **Format:** landscape, text baked into the image. The article title renders separately below the card.
- **Medium:** vintage engraving / mid-century lithograph. Fine hatching and stipple, printed texture, no gradients.
- **Palette:** four colours doing everything. Pale sage-green sky, cream-white clouds, dark olive-black land, solid black type.
- **Setting:** rolling moorland under a big sky full of billowing cumulus clouds rendered in fine line work. Low, wide, empty.
- **The object:** an oversized antique candlestick telephone standing on the ground mid-frame, receiver on its hook, drawn in heavy engraved detail.
- **The device:** the phone's coiled cord runs out along the ground to the right, then **rises and becomes a flight of steps**, climbing diagonally toward the upper right of the frame. A small laptop or monitor sits on one of the upper steps.
- **Type:** `EVERY LEAD TEACHES` in heavy condensed black display caps, spanning most of the width across the sky. The phone overlaps the type, so the lettering sits *behind* the object rather than on top of the picture.

### Why it works

**1. The metaphor is the article's thesis, drawn.** An old phone is one lead, one call. The cord climbing into a
staircase is that call compounding into a system. The picture argues "every lead teaches" before the words do.
Nothing in the frame is decorative.

**2. The baked-in line is not the title.** `EVERY LEAD TEACHES` is a three-word compression of the argument. The
actual title below is the long descriptive one. **So the image carries the quotable spine line and the title
carries the specifics.** That split is the most liftable idea in this cover, and it's different from both 01
(where the baked text *is* the headline) and 02 (where there's no text at all).

**3. Old medium, modern subject.** An engraving from 1890 about lead-gen systems. Same anachronism trick as the
SaaS coffin in 01, and it's why both read as considered rather than generated.

**4. Type behind the object.** The phone occludes the lettering, which gives depth and makes the composition
read as designed rather than as a caption slapped over a picture.

### Prompt: the base

```
A vintage engraving in the style of a mid-century lithograph, wide landscape
format. Rolling empty moorland under a large sky filled with billowing cumulus
clouds, all rendered in fine hatching and stipple with visible printed texture.

Limited flat palette: pale sage-green sky, cream-white clouds, dark olive-black
land. No gradients.

Standing on the ground mid-frame is an oversized antique candlestick telephone,
receiver on its hook, drawn in heavy engraved detail. Its thick coiled cord runs
out along the ground to the right, then rises off the ground and becomes a
flight of ascending steps climbing diagonally toward the upper right of the
frame. A small laptop sits on one of the upper steps.

Engraved illustration only. No lettering, no text, no logo. Leave the upper
middle of the sky open and uncluttered.
```

### Prompt: the swappable parts

The whole mechanic is **one obsolete object whose own cable, cord, wire or thread turns into the thing it
becomes.** Keep that. Change these:

| Slot | This cover | Alternatives that keep the device |
|---|---|---|
| The obsolete object | Candlestick telephone | A typewriter, a Rolodex, a filing cabinet, a printing press, a ship's telegraph |
| What its cord becomes | A staircase climbing up-right | A railway track heading to the horizon, a river, a beanstalk, a bar chart, a rope bridge |
| What sits at the top | A laptop | A monitor, a dashboard, a small city, an open door |
| The landscape | Moorland under cumulus | Prairie, coastline, ploughed field, desert with mesas. Keep it empty and low. |
| The palette | Sage / cream / olive-black | Any single muted colour plus cream plus near-black. Three, not four. |

### The two-layer text device

Generate the illustration clean, then add the lettering yourself so it can sit behind the object:

1. **The spine line, baked in.** Three or four words, heavy condensed display caps, spanning most of the width across the open sky. This is the *compression* of the argument, not the title. `EVERY LEAD TEACHES` is the model: subject, verb, and nothing else.
2. **Mask the object back over it** so the lettering is occluded. That single step is what separates this from a caption.
3. **Let the platform render the real title** below the card, long and descriptive.

So one cover ships two headlines: a quotable three-word thesis inside the frame, and a specific twelve-word
promise underneath it.

---

## 04. Dark integration diagram, borrowed logo, four labelled output tiles

**Source account:** `@Ecombos_Ai` (EcomBos, verified)
**Article title:** `How to Make Claude Build AI Ads That Actually Sell`
**Captured:** 2026-09-02. **Cover and title only — no body text, no view count.** Image file not supplied.
**Saved for:** the photo.

### What it looks like

- **Format:** landscape, near-black background. The title renders below the card in heavy red-orange type.
- **Medium:** designed composite, not an illustration. Real image tiles arranged on a dark canvas with glow effects and drawn connectors. Dark-mode tech-product aesthetic.
- **Palette:** black ground, orange on the left half, yellow-green on the right half, white labels. Two accent colours, split down the middle.
- **The centre:** a bright yellow lightning bolt running vertically down the middle of the frame, splitting it. Immediately left of it, an orange rounded-square app icon carrying the **Claude asterisk**. Immediately right, a yellow-green rounded-square icon carrying the author's own `EB` mark.
- **The four tiles:** two stacked on the left, two on the right, each a real still from an ad, each with a small icon and an all-caps label in a chip at the bottom left:
  - `UGC` — a woman holding a dropper bottle to camera
  - `PRODUCT DEMO` — a dark studio shot of the bottle with splash and crystals
  - `ANIMATION` — a 3D Pixar-style character with lanterns and the product
  - `CINEMATIC AD` — a skateboarder against a sunset
- **The connectors:** curved cables run from each tile into the centre icons. Orange on the left, yellow-green on the right, glowing.

### Why it works

**1. It borrows a logo the reader already recognises.** The Claude asterisk is doing scroll-stopping work that
the author's own mark cannot do alone. The title names Claude too, so the cover and the title borrow the same
recognition twice. This is the cheapest reach lever in the whole library and it costs nothing to use.

**2. The two logos either side of a lightning bolt read as a collaboration.** No words needed. The reader
understands "these two things, combined" instantly, and the bolt supplies the energy.

**3. Four labelled tiles are a bullet list disguised as a picture.** `UGC / PRODUCT DEMO / ANIMATION /
CINEMATIC AD` tells the reader exactly what they get, as a countable set, before they read the title. A visual
promise of four things.

**4. The tiles are real outputs, presented as design.** This is the hybrid the other three covers do not
attempt: proof-of-work content arranged into a composed graphic rather than shown as a raw screenshot. It gets
the credibility of the artifact and the polish of a designed cover at once.

**5. Dark ground with two neon accents is a hard stop in a light feed.** Every other cover in this library is
pale. This one is the only black frame.

### Prompt: what to generate and what to build

**Do not try to generate this one.** It is an assembly job, not an illustration. A generator will not produce
readable labels, a clean logo, or aligned tiles. Build it in a design tool:

```
LAYOUT (16:9, near-black #0A0A0A ground)

CENTRE       Vertical lightning bolt, bright yellow, full height, soft glow.
             Left of it:  rounded-square icon, accent colour A, the tool's logo.
             Right of it: rounded-square icon, accent colour B, your own mark.
             Both icons glow in their own colour.

TILES        Four image tiles, 2 left and 2 right, rounded corners, slight
             inner border. Each is a real still from actual output.
             Each carries a chip bottom-left: small icon + ALL-CAPS label.

CONNECTORS   Curved cables from each tile into the nearest centre icon.
             Left cables in accent A, right cables in accent B. Glowing,
             rounded corners, no sharp angles.

PALETTE      Black plus exactly two accent colours. Left half is accent A,
             right half is accent B. Nothing else.
```

If you want the tiles themselves generated, prompt each one separately as a plain image and drop it in.

### Prompt: the swappable parts

The mechanic is **a recognisable tool logo joined to yours, feeding a countable set of labelled outputs.**

| Slot | This cover | Mauro's version |
|---|---|---|
| Borrowed logo | Claude asterisk | Claude, Notion, Miro, YouTube, X. Whatever the article actually names. |
| Your mark | `EB` | Mauro's own mark |
| The four tiles | UGC / product demo / animation / cinematic ad | The vehicles he actually ships: `X ARTICLE` / `VISUAL DOC` / `SHORT FORM` / `YOUTUBE BOARD` |
| Tile content | Real ad stills | Real screenshots of his own published pieces |
| Accent pair | Orange and yellow-green | Any two, one per side. Keep the split. |
| The join | Lightning bolt | Bolt, plus sign, seam, socket |

Four tiles is the number. Six gets unreadable at feed size, two is not a set.

### On the title

`How to Make Claude Build AI Ads That Actually Sell`

- **Title Case, and it is the only Title Case title in this library.** The recorded reach corpus says
  capitalised titles beat lowercase on every account that tested both. Worth watching whether the ones here
  that use it outperform.
- **Names a tool with a real referent** (`Claude`), which satisfies the concrete-head-noun rule.
- **`That Actually Sell` pre-empts the objection in the title.** The reader's live doubt about AI ads is that
  they look fake and do not convert, and the title answers it before it is raised.
- **`actually` is now in two covers in this library** (this one and 01's `How to actually use AI in your
  business`). It is doing a specific job both times: implying every other version of this advice does not work,
  without naming anyone. Cheap contrarianism with no target to argue back.

---

## 05. Monochrome lighthouse, borrowed logo as the light source, one spot colour

**Source account:** `@Aidanb2b` (Aidan Collins, verified, bio reads "Scaling B2B Offers on LinkedIn & X")
**Article title:** `saturation is a skill issue: how the algorithm changed on linkedin and X + how to win now`
**Captured:** 2026-09-02. **Cover and title only — no body text, no view count.** Image file not supplied.
**Saved for:** the photo.

### What it looks like

- **Format:** landscape. No text baked in. The title renders below the card in heavy white type.
- **Medium:** high-contrast black-and-white engraving, dramatic and detailed, in the register of a 19th-century steel plate.
- **Palette:** monochrome. **One spot colour in the entire frame** — the LinkedIn blue.
- **Setting:** night storm. Heavy black clouds, a violent sea with breaking waves on both sides, a rocky promontory running from the bottom left into the middle distance.
- **The subject:** a lighthouse standing at the end of the promontory. Its lamp is **the LinkedIn logo**, glowing blue, throwing hard radiating beams across the whole sky.
- **The device:** a long single-file procession of small silhouetted figures walking the causeway toward the lighthouse, stretching from the bottom-left corner into the distance. Dozens of them, queueing.

### Why it works

**1. One spot colour on a monochrome frame is the strongest attention mechanic in this library.** Everything is
black and white except one small blue square, and it is the light source, so the eye has nowhere else to go.

**2. The borrowed logo is built into the metaphor, not pasted beside it.** Entry 04 puts a recognisable logo in
a frame. This one makes the logo *be* the thing the metaphor is about. The platform is the lighthouse. Same
borrowed recognition, far more elegant, and it cannot be read as a sponsor slot.

**3. The queue is the article's subject, drawn.** The title says saturation. The picture shows a hundred people
walking single file toward the one light. You understand the problem before reading a word.

**4. It draws the problem and the answer in one frame.** The crowd is the saturation. The beam still cutting
through the storm is the argument that it still works. Both halves of the thesis, one image.

**5. Storm-and-beacon is a metaphor everyone already holds,** so it needs no decoding. The work went into
swapping the lamp for a logo, not into inventing a new symbol.

### Prompt: the base

```
A dramatic high-contrast black-and-white engraving in the style of a
19th-century steel plate illustration, wide landscape format.

Night storm. Heavy black clouds fill the sky. A violent sea with large breaking
waves on both sides. A rocky promontory runs from the bottom left corner into
the middle distance.

A tall lighthouse stands at the end of the promontory. Its lamp blazes at the
top, throwing hard radiating beams of light across the entire sky.

A long single-file procession of small silhouetted figures walks along the
causeway toward the lighthouse, starting at the bottom left corner and
receding into the distance. Dozens of figures, queueing.

Pure monochrome, fine engraved line work, deep blacks, strong dramatic
contrast. No text, no lettering, no logo.
```

Then, in your editor, **replace the lamp with the logo** and let it be the only colour in the frame. Do not ask
the generator to place a logo. It will deform it.

### Prompt: the swappable parts

The mechanic is **a monochrome engraving where a recognisable logo is the single source of light and the only
colour, with a crowd in the frame carrying the problem.**

| Slot | This cover | Alternatives that keep the device |
|---|---|---|
| The light source | Lighthouse lamp | A campfire, a single lit window, a street lamp, a beacon on a hill, a lit doorway |
| The logo | LinkedIn blue | Whatever platform or tool the article is actually about |
| The crowd | Queue walking the causeway | A crowd facing away, a packed harbour of identical boats, a field of identical tents |
| The weather | Night storm | Fog, blizzard, dust storm. It has to be hostile so the light matters. |
| Spot colour | LinkedIn blue | Exactly one colour. The moment there are two, the device is gone. |

**The rule that makes this work: one colour, and it has to be the light.** A spot colour anywhere else in the
frame reads as a mistake.

### On the title

`saturation is a skill issue: how the algorithm changed on linkedin and X + how to win now`

The most constructed title in this library. Sixteen words, lowercase, and it stacks **three** components with a
colon and a plus:

| Part | Job |
|---|---|
| `saturation is a skill issue` | The stance. Blames the reader in four words. |
| `how the algorithm changed on linkedin and X` | The mechanism. This is what gets it opened. |
| `+ how to win now` | The action. This is what gets it saved. |

Three things worth taking:

1. **`skill issue` is borrowed slang carrying an insult.** It is a gamer idiom meaning "the problem is you, not
   the game." Using it as a diagnosis provokes hard while naming no opponent, so there is nobody to argue back.
2. **The colon-plus construction buys both outcomes at once.** The recorded corpus finding is that articles
   promising one mechanism get *opened* and articles promising a list get *impressions*. This title promises a
   mechanism and an action stapled together, which is an attempt to have both. Worth testing.
3. **Two platforms named plus a recency clamp** (`now`). Category anchoring for scroll recognition and search.

---

## Also on file

The engraving-style cover in [01-saaspocalypse-is-overblown.md](01-saaspocalypse-is-overblown.md) is described in
that article's capture. Different device entirely: a single visual joke that states the thesis, black and
white, category name lettered into the set. Worth reading alongside this one, since between them they cover
the two cover classes the reach lane rewards.
