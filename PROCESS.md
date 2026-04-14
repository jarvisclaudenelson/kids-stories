# Story Writing Process

## Canon policy

This repo has **one active continuity**:

- Active canon lives in `stories/chapter-001.md` through the current latest chapter in `stories/`
- `stories/archive/` contains superseded / alternate continuation drafts
- Do **not** merge archive details back into canon unless we intentionally promote them

## Source-of-truth order

Before writing or illustrating, check these in order:

1. Latest active chapter(s) in `stories/`
2. `world/WORLD.md`
3. `world/PLOT.md`
4. `world/IMAGE_TRACKING.md`
5. `world/CHARACTER_PROMPTS.md`
6. Existing `prompts/chapter-XXX-prompts.md` files for format/style consistency

## Pre-writing checklist

- [ ] Read the latest active chapter
- [ ] Review `world/WORLD.md`
- [ ] Review `world/PLOT.md`
- [ ] Review `world/IMAGE_TRACKING.md`
- [ ] Confirm any open continuity threads that must advance
- [ ] Confirm the next chapter number before creating files

## Core canon guardrails

### The Nelson boys
- **Julian "Juju" Nelson (7)** — planner, determined, competitive, brave, no fragment
- **Ezra "EZ" Nelson (5)** — empathetic, emotionally perceptive, carries the gold fragment in his chest
- **Declan "Decker" Nelson (2)** — toddler, brave, socially fearless, no fragment; sound/vibration gift
- **Ollie** — family Schnoodle, protective, senses danger

### Pronouns
- Julian = **he/him**
- Ezra = **he/him**
- Declan = **he/him**
- Ollie = **he/him**

### Ongoing active-team cast
- Sable — silver-blue fragment, pattern sense
- Rafe — amber fragment, telekinesis
- Petra — violet-white fragment, light/energy projection
- Noa — yellow-green fragment, boosts systems / hears machine patterns

## Chapter standards

- Format: chapter markdown in `stories/chapter-XXX.md`
- Typical length: ~900–1600 words unless a specific chapter wants a different rhythm
- POV: close third, kid-centered
- Tone: adventurous, emotionally warm, age-appropriate
- Endings: usually land on wonder, momentum, or a mild cliffhanger
- Include **page-level illustration thinking** while drafting

## Illustration workflow

### Page planning
- Aim for **3–9 strong illustration beats** depending on chapter structure
- Recent chapters are trending toward **full page-by-page prompt coverage**; prefer that format going forward
- Capture a mix of:
  - establishing shots
  - action beats
  - emotional character moments
  - end-of-chapter image-worthy reveal or landing beat

### Prompt requirements
Every prompt should preserve:
- consistent character faces
- correct fragment holder / non-holder status
- correct fragment color + placement
- warm cinematic storybook feel
- **no text bubbles / no captions in the image**

### Reference assets
Use these whenever relevant:
- `world/assets/nelson-boys-photo.jpg`
- `world/assets/boy-final.png`
- `world/assets/ollie-final.png`
- existing finished chapter art for continuity

### Prompt helper
```bash
cd /root/.hermes/repos/kids-stories
python3 scripts/gen_prompt.py --list
python3 scripts/gen_prompt.py --cast 20
python3 scripts/gen_prompt.py 20 6 "Declan at the communications console" declan julian sable noa petra rafe
```

## Post-writing checklist

After finishing a chapter:

1. Save it as `stories/chapter-XXX.md`
2. Create/update `prompts/chapter-XXX-prompts.md`
3. Verify names, ages, pronouns, fragment details, and continuity
4. Update `world/WORLD.md` if canon changed
5. Update `world/PLOT.md` with resolved and open threads
6. Add page art into `images/chapterN/` when available
7. If a chapter is being replaced, move the old version into `stories/archive/`

## When replacing existing canon

If a chapter or continuation is superseded:

- move the old markdown into `stories/archive/`
- keep the active version in `stories/`
- update `WORLD.md` and `PLOT.md` so they only reflect active canon
- avoid mixing archive details into future chapters accidentally

---

*This process doc is for the cleaned current workflow, not older external app-specific image pipelines.*
