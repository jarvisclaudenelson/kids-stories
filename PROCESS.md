# Story Writing Process

## Pre-Writing Checklist

Before writing any story chapter:

- [ ] Read `world/WORLD.md` - understand current canon
- [ ] Read `world/PLOT.md` - understand active plot threads
- [ ] Read previous chapter(s) - maintain continuity
- [ ] Check for any pending plot threads to advance
- [ ] Read `world/CHARACTER_PROMPTS.md` - for image generation

## Character Facts (MUST REMEMBER)

### The Nelson Boys
- **Julian "Juju"** (7) - oldest, competitive, fierce, wants to be hero
- **Ezra "EZ"** (5) - middle, creative, empathetic, big emotions
- **Declan "Decker"** (2) - youngest, social, stubborn, brave
- **Ollie** - family dog, brave, protective, senses danger, Schnoodle breed

### Key Facts
- All three are BOYS (he/him)
- Last name: Nelson
- Ship: USS Mayflower (crashed)
- Current location: Monscollis Colony planet
- Goal: Rescue separated parents, find other colonists

## Writing Standards

- Length: 800-1200 words (~10-15 min read)
- Tone: Fun, adventurous, age-appropriate
- Format: Engaging chapter with mild cliffhanger
- Point of view: Third person, focus on kids
- Structure: Plan 3-5 illustration moments (every 2-3 pages)

## Post-Writing Process

After completing a chapter:

1. **Save to** `stories/chapter-XXX.md` (next sequential number)
2. **Verify** character names, pronouns (he/him for all 3 boys)
3. **Verify** details match WORLD.md
4. **Update WORLD.md** with any new details
5. **Update PLOT.md** with completed threads
6. **Generate Illustrations** (see below)
7. **Push to GitHub** - `git add -A && git commit -m "Add Chapter X" && git push`
8. **Send** to Erik on Discord for review

## Image Generation Process

### When to Generate
After completing a chapter, generate **3-5 illustrations** (every 2-3 pages of content).

### Steps
1. **Read CHARACTER_PROMPTS.md** - always use character descriptions
2. **Identify key scenes** - pick 3-5 pivotal moments in the chapter
3. **Write prompts** using the template:
   ```
   Pixar-style 3D animated scene of [scene description],
   including CHARACTERS:
   - Julian: 7-year-old Caucasian boy, sandy blonde short hair, blue/hazel eyes, [expression/action]
   - Ezra: 5-year-old Caucasian boy, dark brown medium-length hair, brown eyes, [expression/action]
   - Declan: 2-year-old Caucasian boy, medium brown short hair, brown eyes, [expression/action]
   - Ollie: medium-sized scruffy Schnoodle, white and gray curly fur, [expression/action]
   
   [Additional scene details...], Disney Pixar quality, adventure movie style
   ```
4. **Generate using DALL-E 3:**
   ```bash
   python3 /app/skills/openai-image-gen/scripts/gen.py \
     --model dall-e-3 --size 1792x1024 --style vivid \
     --prompt "[your prompt]" --count 1 \
     --out-dir /home/node/.openclaw/workspace/kids-stories-reader/public/images/chapter{N}
   ```
5. **Rename files** to descriptive names (crash.png, forest.png, etc.)
6. **Update App.jsx** - add illustrations to CHAPTER_IMAGES mapping
7. **Push** changes to kids-stories-reader GitHub repo

### Settings
- Model: dall-e-3
- Size: 1792x1024 (landscape)
- Style: vivid
- Cost: ~$0.04-0.08/image

## Pronoun Checklist (ALWAYS VERIFY)

- [ ] Julian = he/him
- [ ] Ezra = he/him (BOY)
- [ ] Declan = he/him
- [ ] Ollie = he/him
- [ ] Mom = she/her
- [ ] Dad = he/him

---

*Process document - update as needed*
