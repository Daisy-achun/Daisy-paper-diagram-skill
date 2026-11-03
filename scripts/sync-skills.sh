#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$repo_root/skills"

for host_dir in .claude/skills .agents/skills .cursor/skills; do
  destination="$repo_root/$host_dir"
  mkdir -p "$destination"
  for skill_dir in "$source_root"/*; do
    [[ -d "$skill_dir" ]] || continue
    skill_name="$(basename "$skill_dir")"
    rm -rf "$destination/$skill_name"
    cp -R "$skill_dir" "$destination/$skill_name"
  done
done

cp "$source_root/paper-framework-diagram/SKILL.md" "$repo_root/SKILL.md"
cp "$source_root/paper-framework-diagram/references/reference-qa.md" \
  "$repo_root/references/reference-qa.md"
cp "$source_root/paper-framework-diagram/references/ppt-computer-use.md" \
  "$repo_root/references/ppt-computer-use.md"
cp "$source_root/paper-framework-diagram/agents/openai.yaml" \
  "$repo_root/agents/openai.yaml"

printf 'Synced %s skill packages to .claude/skills, .agents/skills, and .cursor/skills.\n' \
  "$(find "$source_root" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
