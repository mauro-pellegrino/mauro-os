# The Anti-Slop Protocol: Human Signal Enforcement

> Load alongside `brand/voice.md` for any drafted text: articles, posts, emails, scripts, lead magnets.
> `voice.md` says how Mauro sounds. This file says what makes prose read as written by a person at all.
> Where the two collide, `voice.md` wins on voice, this file wins on structure.

**Instructions for Claude:** This is a combined negative and positive constraint set. You are forbidden
from the patterns below, and you are required to hit the quotas below. During the mandatory self-audit
step you must scan the draft for every pattern listed, rewrite any sentence containing one, and confirm
every quota before delivering output. If a quota cannot be met honestly, report it. Never pad to hit a
number.

---

## 1. Banned emotional shortcuts (highest priority)

### The Named Feeling

**Definition:** stating an emotion instead of causing it.

Prohibited examples:

- "I was frustrated."
- "It was exciting."
- "I felt proud of what we built."
- "It was a humbling experience."
- "I couldn't believe what I was seeing."

**Why it fails:** naming a feeling asks the reader to take your word for it, and a reader who is told
what to feel feels nothing. It is also the cheapest sentence in the language to produce, which is
exactly why models reach for it first.

**The fix: the Evidence Principle.** Delete the label and write the thing that caused it. "I was
frustrated" becomes "the fourth build failed at 2am and I put the laptop in a drawer." The reader
supplies the word.

### The Clean Resolution

**Definition:** every thread tied off, every lesson learned, the piece landing in a state of completion.

Prohibited examples:

- "And that's when it all clicked."
- "Looking back, I wouldn't change a thing."
- "The lesson here is simple."

**Why it fails:** real experience leaves loose ends. A piece where everything resolves was constructed
backwards from its conclusion, and readers can feel the reverse-engineering.

**The fix:** leave one thing unfixed and say so plainly. Name what you still do not know.

---

## 2. Banned rhythm patterns

### The Metronome

**Definition:** consecutive sentences of near-identical length.

- **Prohibited:** three sentences in a row within five words of each other in length.
- **Required:** at least one sentence under five words and one over thirty in every section.

**Why it fails:** sentence-length variance is the single most measurable difference between human and
machine prose. Machines write at a steady pulse. People speed up, stall, interrupt themselves, then
run long.

**The fix: the Variance Rule.** After drafting, count the words in each sentence and break any run of
three similar ones.

### The Uniform Block

**Definition:** every paragraph the same size.

- **Prohibited:** a page where every paragraph is three to four lines.

**The fix:** some paragraphs run six lines, some run one. Use at least two single-sentence paragraphs
per piece.

---

## 3. Banned abstraction

### The Weightless Noun

**Definition:** a general word standing where a specific one belongs.

Prohibited examples: "businesses", "solutions", "a tool", "results", "the industry", "stakeholders",
"content".

**Why it fails:** abstraction costs nothing to generate and proves nothing. Specificity is the only
quality that cannot be faked cheaply, which is why its absence reads as machine output.

**The fix: the Specificity Quota.** Per 500 words, minimum three proper nouns, one physical detail with
a sense attached, one time anchor, and one true detail that is irrelevant to the argument.

### The Round Number

**Definition:** figures that end in zero or five.

Prohibited examples: "about 50%", "roughly 3x", "around $10k", "hundreds of hours".

**Why it fails:** real measurement produces ugly numbers. A round number tells the reader you estimated
or invented it.

**The fix:** 47%, 2.8x, $9,340, 213 hours. Minimum two non-round numbers per 500 words. If you do not
have the real figure, say you are estimating rather than smoothing it.

> Read this against the standing rule in `CLAUDE.md` section 6.6: never invent performance numbers.
> This section forbids rounding a real figure. It does not license inventing an ugly one. No number,
> no source, then bracket it: `[X%]`.

---

## 4. Banned safety

### The Balanced Take

**Definition:** hedging both sides so the sentence cannot be argued with.

Prohibited: "might", "could potentially", "in many cases", "some would argue", "while X, it is also
true that Y".

**Why it fails:** text nobody can disagree with is text nobody remembers or shares.

**The fix:** one claim per piece stated flat, with no balancing paragraph after it. If you are not
willing to defend it in the replies, cut it entirely rather than hedging it.

### The Costless Claim

**Definition:** advice from someone who risked nothing.

**Why it fails:** authority comes from having paid for the knowledge. Text with no cost attached reads
as compiled rather than lived.

**The fix:** name one real cost, money, hours, a relationship or a reputation, and one moment you were
wrong. Do not soften either.

---

## 5. Banned borrowed language

### The Inherited Sentence

**Definition:** phrasing that could appear word for word in any other piece on this topic, including
anything lifted from material the user pastes as reference.

**Why it fails:** it is both the loudest generic-writing signal and a genuine originality risk.

**The fix:** reference material sets direction, never wording. Quotes maximum fifteen words, always
attributed. When using a fact from a source, restate the underlying mechanism in your own construction
rather than paraphrasing the sentence. Flag any sentence you suspect is inherited.

---

## 6. Required: the one wrong note

Uniform polish is itself a tell. Include exactly one deliberate imperfection: a sentence that runs
slightly too long, a tangent that pays off two paragraphs later, a joke that lands a little dry, or a
bracketed aside that undercuts the sentence before it. One only. Two reads as carelessness.

---

## 7. Mandatory self-audit

Before returning anything, output this filled in:

```
named emotions found (must be 0):
clean resolution present (must be false):
shortest sentence / longest sentence, in words:
three-in-a-row length violation (must be false):
paragraph length range:
proper nouns per 500w (min 3):
non-round numbers per 500w (min 2):
sensory detail / time anchor / irrelevant true detail:
unhedged strong claim:
cost admitted:
unresolved thread:
wrong note used:
suspected inherited sentences:
```

Fix every failure, then deliver. Finally, list three phrases you almost used and cut for being generic.

---

*Added 10 September 2026.*
