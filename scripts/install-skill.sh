#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/install-skill.sh --target claude|codex|cursor|all [options]

Options:
  --target NAME       Host directory to install into (required)
  --project PATH      Project root; defaults to the current directory
  --skill NAME        Install one skill; defaults to all bundled skills
  -h, --help          Show this help
EOF
}

target=""
project="$(pwd)"
skill_filter=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) target="${2:?missing value for --target}"; shift 2 ;;
    --project) project="${2:?missing value for --project}"; shift 2 ;;
    --skill) skill_filter="${2:?missing value for --skill}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
done

case "$target" in
  claude) host_dir=".claude/skills" ;;
  codex) host_dir=".agents/skills" ;;
  cursor) host_dir=".cursor/skills" ;;
  all) host_dir="" ;;
  *) printf '%s\n' 'Choose --target claude, codex, cursor, or all.' >&2; exit 2 ;;
esac

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$repo_root/skills"
project="$(cd "$project" && pwd)"

install_one() {
  local skill_dir="$1"
  local skill_name="$(basename "$skill_dir")"
  local destination="$2/$skill_name"
  mkdir -p "$2"
  mkdir -p "$destination"
  cp -R "$skill_dir/" "$destination/"
  printf 'Installed %s -> %s\n' "$skill_name" "$destination"
}

if [[ -n "$skill_filter" ]]; then
  skill_dir="$source_root/$skill_filter"
  [[ -d "$skill_dir" ]] || { printf 'Unknown skill: %s\n' "$skill_filter" >&2; exit 2; }
  skill_dirs=("$skill_dir")
else
  skill_dirs=()
  while IFS= read -r skill_dir; do
    skill_dirs+=("$skill_dir")
  done < <(find "$source_root" -mindepth 1 -maxdepth 1 -type d | sort)
fi

if [[ "$target" == all ]]; then
  for host in .claude/skills .agents/skills .cursor/skills; do
    for skill_dir in "${skill_dirs[@]}"; do install_one "$skill_dir" "$project/$host"; done
  done
else
  for skill_dir in "${skill_dirs[@]}"; do install_one "$skill_dir" "$project/$host_dir"; done
fi
