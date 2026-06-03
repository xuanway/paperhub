#!/usr/bin/env bash

set -euo pipefail

REMOTE="${1:-origin}"
BRANCH="${2:-$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)}"

if ! command -v git >/dev/null 2>&1; then
  echo "[ERROR] git is not installed or not in PATH."
  exit 1
fi

if [[ -z "${BRANCH}" ]]; then
  echo "[ERROR] Could not detect current branch."
  echo "Usage: $(basename "$0") [remote] [branch]"
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[ERROR] Current directory is not a git repository."
  exit 1
fi

if ! git remote get-url "${REMOTE}" >/dev/null 2>&1; then
  echo "[ERROR] Remote '${REMOTE}' does not exist."
  echo "Available remotes:"
  git remote -v || true
  exit 1
fi

echo "[INFO] Repo: $(basename "$(git rev-parse --show-toplevel)")"
echo "[INFO] Branch: ${BRANCH}"
echo "[INFO] Remote: ${REMOTE}"
echo

echo "[STEP 1/4] Local quick status"
git status -sb
echo

echo "[STEP 2/4] Push commits"
if ! git push "${REMOTE}" "${BRANCH}"; then
  echo "[ERROR] Push failed."
  echo "[HINT] Check network, credentials, and branch protection rules."
  exit 1
fi
echo

echo "[STEP 3/4] Refresh remote tracking refs"
git fetch "${REMOTE}" --prune
echo

echo "[STEP 4/4] Verify sync status"
SYNC_STATE="$(git status -sb | head -n 1)"
echo "${SYNC_STATE}"
echo

if [[ "${SYNC_STATE}" == "## ${BRANCH}...${REMOTE}/${BRANCH}" ]]; then
  echo "[OK] Local and remote are synchronized."
  exit 0
fi

if [[ "${SYNC_STATE}" == *"ahead"* ]]; then
  echo "[WARN] Local branch is still ahead."
  echo "[HINT] Retry: git push ${REMOTE} ${BRANCH}"
  exit 2
fi

if [[ "${SYNC_STATE}" == *"behind"* ]]; then
  echo "[WARN] Local branch is behind remote."
  echo "[HINT] Pull/rebase before next push."
  exit 3
fi

echo "[WARN] Branch state is not fully synchronized."
echo "[HINT] Inspect with: git status -sb && git log --oneline --decorate -n 5 --all"
exit 4
