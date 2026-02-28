#!/usr/bin/env python3
"""
Generate ChatGPT image prompts with character consistency.

Usage:
  python3 gen_prompt.py <chapter_num> <page_num> <scene_description> [character_ids...]
  
Examples:
  python3 gen_prompt.py 4 3 "Julian and Ezra exploring a dark cave"
  python3 gen_prompt.py 4 3 "Julian and Ezra exploring a dark cave" julian ezra ollie
  python3 gen_prompt.py --list                    # List all characters
  python3 gen_prompt.py --cast 4                  # Show chapter 4 cast
  python3 gen_prompt.py --refs julian ezra        # Show reference images for characters

If no character IDs are provided, auto-detects from the scene description.
"""

import json
import sys
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARACTERS_FILE = os.path.join(REPO, "world", "characters.json")

def load_characters():
    with open(CHARACTERS_FILE) as f:
        return json.load(f)

def detect_characters(scene_desc, characters):
    """Auto-detect which characters are in a scene from the description."""
    found = []
    desc_lower = scene_desc.lower()
    
    name_map = {}
    for c in characters:
        cid = c["id"]
        # Map all name variants
        name_map[c["name"].split('"')[0].strip().lower()] = cid  # first name
        name_map[cid] = cid
        if '"' in c["name"]:
            nickname = c["name"].split('"')[1].lower()
            name_map[nickname] = cid
        # Full first name
        first = c["name"].split()[0].lower()
        name_map[first] = cid
    
    for name, cid in name_map.items():
        if name in desc_lower and cid not in found:
            found.append(cid)
    
    return found

def get_character(cid, characters):
    for c in characters:
        if c["id"] == cid:
            return c
    return None

def generate_prompt(chapter_num, page_num, scene_desc, char_ids, data):
    characters = data["characters"]
    
    # Auto-detect if no chars specified
    if not char_ids:
        char_ids = detect_characters(scene_desc, characters)
    
    if not char_ids:
        # Fall back to chapter cast
        cast_key = f"chapter-{chapter_num:03d}"
        char_ids = data.get("chapter_cast", {}).get(cast_key, [])
    
    chars = [get_character(cid, characters) for cid in char_ids]
    chars = [c for c in chars if c]
    
    # Build the prompt
    lines = []
    lines.append("=" * 60)
    lines.append(f"IMAGE PROMPT — Chapter {chapter_num}, Page {page_num}")
    lines.append("=" * 60)
    lines.append("")
    
    # Reference images to upload
    lines.append("📎 UPLOAD THESE REFERENCE IMAGES TO CHATGPT:")
    ref_images = set()
    for c in chars:
        ref = c.get("reference_image")
        if ref:
            full_path = os.path.join(REPO, ref)
            if os.path.exists(full_path):
                ref_images.add((c["name"].split('"')[0].strip().split()[0], ref, full_path))
            else:
                ref_images.add((c["name"].split('"')[0].strip().split()[0], ref, "⚠️ FILE NOT FOUND"))
    
    for name, rel, full in sorted(ref_images):
        lines.append(f"  • {rel}  ({name})")
    lines.append("")
    
    # The prompt itself
    lines.append("📋 PASTE THIS PROMPT IN CHATGPT:")
    lines.append("-" * 40)
    lines.append("")
    lines.append(f"Generate a Pixar-style 3D animated illustration for a children's sci-fi adventure book.")
    lines.append("")
    lines.append(f"**Scene:** {scene_desc}")
    lines.append("")
    lines.append(f"**Characters in this scene** (use the uploaded reference images for consistency):")
    for c in chars:
        lines.append(f"- {c['prompt_snippet']}")
    lines.append("")
    lines.append("**Style instructions:**")
    lines.append("- Pixar/Disney quality 3D animation style")
    lines.append("- Warm cinematic lighting, adventure movie feel")
    lines.append("- Landscape format (16:9)")
    lines.append("- Characters must match the uploaded reference images exactly")
    lines.append("- Rich detail in environment and expressions")
    lines.append("")
    lines.append("-" * 40)
    lines.append("")
    lines.append(f"💾 Save output to: images/chapter{chapter_num}/page-{page_num}.png")
    
    return "\n".join(lines)

def list_characters(data):
    print(f"{'ID':<15} {'Name':<30} {'First Appears':<15} {'Reference Image'}")
    print("-" * 80)
    for c in data["characters"]:
        print(f"{c['id']:<15} {c['name']:<30} {c['first_appearance']:<15} {c.get('reference_image', 'none')}")

def show_cast(chapter_num, data):
    cast_key = f"chapter-{chapter_num:03d}"
    char_ids = data.get("chapter_cast", {}).get(cast_key, [])
    if not char_ids:
        print(f"No cast defined for chapter {chapter_num}")
        return
    print(f"Chapter {chapter_num} cast:")
    for cid in char_ids:
        c = get_character(cid, data["characters"])
        if c:
            print(f"  • {c['name']} ({c['id']})")

def show_refs(char_ids, data):
    for cid in char_ids:
        c = get_character(cid, data["characters"])
        if c:
            ref = c.get("reference_image", "none")
            full = os.path.join(REPO, ref) if ref != "none" else ""
            exists = "✅" if full and os.path.exists(full) else "❌"
            print(f"{c['name']}: {ref} {exists}")
            print(f"  {c['prompt_snippet']}")
            print()

def main():
    data = load_characters()
    
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    if sys.argv[1] == "--list":
        list_characters(data)
    elif sys.argv[1] == "--cast":
        show_cast(int(sys.argv[2]), data)
    elif sys.argv[1] == "--refs":
        show_refs(sys.argv[2:], data)
    else:
        chapter = int(sys.argv[1])
        page = int(sys.argv[2])
        scene = sys.argv[3]
        char_ids = sys.argv[4:] if len(sys.argv) > 4 else []
        print(generate_prompt(chapter, page, scene, char_ids, data))

if __name__ == "__main__":
    main()
