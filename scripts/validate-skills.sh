#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$repo_root/skills"
status=0

for skill_dir in "$source_root"/*; do
  [[ -d "$skill_dir" ]] || continue
  skill_name="$(basename "$skill_dir")"
  skill_file="$skill_dir/SKILL.md"
  if [[ ! -f "$skill_file" ]]; then
    printf 'ERROR: missing %s\n' "$skill_file" >&2
    status=1
    continue
  fi
  grep -q '^---$' "$skill_file" || { printf 'ERROR: %s has no frontmatter\n' "$skill_file" >&2; status=1; }
  grep -q "^name: $skill_name$" "$skill_file" || { printf 'ERROR: name mismatch in %s\n' "$skill_file" >&2; status=1; }
  grep -q '^description:' "$skill_file" || { printf 'ERROR: missing description in %s\n' "$skill_file" >&2; status=1; }
  grep -q 'Host portability' "$skill_file" || { printf 'ERROR: missing portability guidance in %s\n' "$skill_file" >&2; status=1; }
  while IFS= read -r reference; do
    reference_path="${reference#*](}"
    reference_path="${reference_path%)}"
    [[ -f "$skill_dir/$reference_path" ]] || {
      printf 'ERROR: broken local reference in %s: %s\n' "$skill_file" "$reference_path" >&2
      status=1
    }
  done < <(grep -oE '\]\(references/[^)]+' "$skill_file" || true)
done

for host_dir in .claude/skills .agents/skills .cursor/skills; do
  for source_dir in "$source_root"/*; do
    [[ -d "$source_dir" ]] || continue
    skill_name="$(basename "$source_dir")"
    mirror="$repo_root/$host_dir/$skill_name"
    if [[ ! -d "$mirror" ]] || ! diff -qr "$source_dir" "$mirror" >/dev/null; then
      printf 'ERROR: mirror out of sync: %s\n' "$mirror" >&2
      status=1
    fi
  done
done

if [[ "$status" -eq 0 ]]; then
  printf 'Skill packages and host mirrors are valid.\n'
fi
exit "$status"
