#!/bin/bash
# Generate a ChatGPT image prompt for a story page
# Usage: ./gen-prompt.sh <chapter> <page> <scene_description>
# Example: ./gen-prompt.sh 4 3 "Julian and Ezra exploring a dark cave with Ollie leading the way"
#
# Output: A ready-to-paste prompt for ChatGPT with:
#   - Character descriptions for everyone in the scene
#   - Reference image paths to upload
#   - Scene description
#   - Style instructions

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

python3 "$SCRIPT_DIR/gen_prompt.py" "$@"
