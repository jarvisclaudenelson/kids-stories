# Kids Stories Project

Bedtime stories for Julian, Ezra, and Declan Nelson set in the **Monscollis** sci-fi adventure world.

This repo holds the active story canon, page-level illustration prompts, and finished chapter art.

## Current status

- **Active story run:** `stories/chapter-001.md` through `stories/chapter-021.md`
- **Prompt files:** `prompts/chapter-001-prompts.md` through `prompts/chapter-021-prompts.md`
- **Finished image sets:** `images/chapter1/` through `images/chapter19/`
- **Chapter 20:** story + prompt file exist; page images have not been added yet
- **Chapter 21:** story + prompt file exist; page images have not been added yet
- **Archive:** `stories/archive/` contains superseded or alternate continuation drafts. Do **not** treat archive files as live canon unless they are deliberately promoted back into `stories/`.

## Repo structure

```text
kids-stories/
├── README.md
├── PROCESS.md                 # Writing + illustration workflow
├── world/
│   ├── WORLD.md              # Active canon / world bible
│   ├── PLOT.md               # Current story position + open threads
│   ├── CHARACTER_PROMPTS.md  # Prompt-ready character descriptions
│   ├── IMAGE_TRACKING.md     # Visual consistency rules
│   ├── characters.json       # Prompt generator metadata
│   └── assets/               # Reference photos and style references
├── stories/                  # Active chapters
│   └── archive/              # Superseded / alternate drafts
├── prompts/                  # Per-chapter image prompt docs
├── images/                   # Final page art by chapter
└── scripts/
    ├── gen_prompt.py         # Generate ChatGPT-ready image prompts
    └── gen-prompt.sh         # Shell wrapper for gen_prompt.py
```

## Source of truth

When writing the next chapter or generating art, use these in order:

1. `stories/chapter-XXX.md` for the latest active chapter continuity
2. `world/WORLD.md` for canon summary
3. `world/PLOT.md` for current open threads and next-step guidance
4. `world/IMAGE_TRACKING.md` for visual canon
5. `world/CHARACTER_PROMPTS.md` for prompt wording
6. `prompts/chapter-XXX-prompts.md` for page-level prompt patterns

## Story tone and audience

- Read-aloud bedtime adventure
- Core audience: Julian (7), Ezra (5), Declan (2)
- Needs to stay accessible for the youngest while still feeling exciting for the oldest
- Emotional center: sibling teamwork, wonder, courage, warmth, gentle humor

## Writing workflow

1. Read `PROCESS.md`
2. Review the most recent active chapter(s)
3. Write the next chapter into `stories/chapter-XXX.md`
4. Create or update page prompts in `prompts/chapter-XXX-prompts.md`
5. Add finished images to `images/chapterN/`
6. Update `world/WORLD.md` and `world/PLOT.md` when canon changes

## Prompt generation helper

Generate a prompt scaffold from the repo metadata:

```bash
cd /root/.hermes/repos/kids-stories
python3 scripts/gen_prompt.py --list
python3 scripts/gen_prompt.py --cast 20
python3 scripts/gen_prompt.py 20 6 "Declan receives the Builder response" declan julian sable noa petra rafe
```

## Illustration references

Core reference assets live in `world/assets/`, including:

- `world/assets/nelson-boys-photo.jpg`
- `world/assets/boy-final.png`
- `world/assets/ollie-final.png`

## Canon note

The active canon currently ends with **Chapter 20: The Voice in the Static**. Anything in `stories/archive/` should be treated as historical material or alternate continuation work, not live continuity.
