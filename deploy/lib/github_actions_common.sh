#!/usr/bin/env bash
set -eo pipefail

# GitHub Actions Common Functions Library
# Adapted for talkable-docs repository
# Checks overall workflow status for a specific commit

# Ensure required variables are set
: "${GITHUB_API_BASE:=https://api.github.com}"
: "${GITHUB_REPOSITORY:=talkable/talkable-docs}"
: "${GITHUB_ACC_USR:?GITHUB_ACC_USR must be set}"
: "${GITHUB_ACC_PSW:?GITHUB_ACC_PSW must be set}"
: "${BRANCH_NAME:?BRANCH_NAME must be set}"
: "${GIT_COMMIT:?GIT_COMMIT must be set}"

# Constants
CHECK_INTERVAL=8
EXIT_CODE_TIMEOUT=228
MAX_NOT_FOUND_ATTEMPTS=5

# Get workflow run information for a commit
get_workflow_run() {
  local commit=$1
  local short_commit="${commit:0:7}"
  local response http_code run_id workflow_run

  echo "Searching for workflow run with commit: ${short_commit}" >&2

  response=$(curl -s -w "\n%{http_code}" -u "${GITHUB_ACC_USR}:${GITHUB_ACC_PSW}" \
    "${GITHUB_API_BASE}/repos/${GITHUB_REPOSITORY}/actions/runs?branch=${BRANCH_NAME}&per_page=20&head_sha=${commit}")

  http_code=$(echo "$response" | tail -n1)
  response=$(echo "$response" | sed '$d')

  if [[ "$http_code" != "200" ]]; then
    echo "ERROR: GitHub API returned HTTP $http_code" >&2
    case "$http_code" in
      401) echo "  → Check GITHUB_ACC_USR and GITHUB_ACC_PSW credentials" >&2 ;;
      403) echo "  → API rate limit exceeded or access denied" >&2 ;;
      404) echo "  → Repository not found or no access" >&2 ;;
    esac
    return 1
  fi

  if ! echo "$response" | jq empty 2>/dev/null; then
    echo "ERROR: Invalid JSON response from GitHub API" >&2
    return 1
  fi

  run_id=$(echo "$response" | jq -r --arg commit "$commit" \
    '[.workflow_runs[]? | select(.head_sha == $commit)] | sort_by(.created_at) | reverse | .[0].id // empty')

  if [[ -z "$run_id" || "$run_id" == "null" ]]; then
    echo "No workflow run found for commit ${short_commit}" >&2
    return 1
  fi

  workflow_run=$(curl -s -w "\n%{http_code}" -u "${GITHUB_ACC_USR}:${GITHUB_ACC_PSW}" \
    "${GITHUB_API_BASE}/repos/${GITHUB_REPOSITORY}/actions/runs/${run_id}")

  http_code=$(echo "$workflow_run" | tail -n1)
  workflow_run=$(echo "$workflow_run" | sed '$d')

  if [[ "$http_code" != "200" ]]; then
    echo "ERROR: GitHub API returned HTTP $http_code when fetching workflow run" >&2
    return 1
  fi

  if ! echo "$workflow_run" | jq empty 2>/dev/null; then
    echo "ERROR: Invalid JSON response from workflow run API" >&2
    return 1
  fi

  echo "$workflow_run"
}

# Check overall workflow status
# Returns: 0=success/pending, 1=failure
check_workflow_status() {
  local workflow_run=$1
  local run_id run_number status conclusion run_url short_commit

  run_id=$(echo "$workflow_run" | jq -r '.id')
  run_number=$(echo "$workflow_run" | jq -r '.run_number')
  status=$(echo "$workflow_run" | jq -r '.status // "unknown"')
  conclusion=$(echo "$workflow_run" | jq -r '.conclusion // "null"')
  run_url="https://github.com/${GITHUB_REPOSITORY}/actions/runs/${run_id}"
  short_commit="${GIT_COMMIT:0:7}"

  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "GitHub Actions Workflow Run #${run_number}"
  echo "URL: ${run_url}"
  echo "Commit: ${short_commit} (${GIT_COMMIT})"
  echo "Status: ${status}, Conclusion: ${conclusion}"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  if [[ "$status" == "completed" ]]; then
    case "$conclusion" in
      "success"|"neutral")
        echo "✅ Workflow: SUCCESS"
        return 0
        ;;
      *)
        echo "✗ Workflow: FAILED (${conclusion})"
        return 1
        ;;
    esac
  else
    echo "⏳ Workflow: IN PROGRESS (${status})"
    return 0
  fi
}

# Continuous monitoring - waits for workflow to complete
gh_status() {
  local workflow_run result
  local short_commit="${GIT_COMMIT:0:7}"
  local start_time=$SECONDS
  local check_count=0
  local not_found_count=0
  local elapsed_minutes elapsed_secs

  echo "════════════════════════════════════════════════════════════════"
  echo "GitHub Actions Status Monitor"
  echo "Commit: ${short_commit}"
  echo "Timeout: $((TIMEFRAME_SECONDS / 60)) minutes"
  echo "════════════════════════════════════════════════════════════════"

  while true; do
    check_count=$((check_count + 1))
    elapsed_minutes=$(((SECONDS - start_time) / 60))
    elapsed_secs=$(((SECONDS - start_time) % 60))

    echo ""
    echo "Check #${check_count} (elapsed: ${elapsed_minutes}m ${elapsed_secs}s)"

    if [[ $SECONDS -gt $TIMEFRAME_SECONDS ]]; then
      echo "⏰ Build timed out waiting for workflow to complete."
      exit $EXIT_CODE_TIMEOUT
    fi

    workflow_run=$(get_workflow_run "$GIT_COMMIT") || {
      ((not_found_count++))

      if [[ $not_found_count -ge $MAX_NOT_FOUND_ATTEMPTS ]]; then
        echo "❌ Cannot find workflow after $not_found_count attempts"
        echo "   Check if workflow was triggered for this commit"
        exit 1
      fi

      echo "⚠️ Workflow not found (attempt $not_found_count/$MAX_NOT_FOUND_ATTEMPTS)"
      echo "Retrying in ${CHECK_INTERVAL} seconds..."
      sleep $CHECK_INTERVAL
      continue
    }

    not_found_count=0

    check_workflow_status "$workflow_run"
    result=$?

    if [[ $result -eq 0 ]]; then
      local status=$(echo "$workflow_run" | jq -r '.status')
      if [[ "$status" == "completed" ]]; then
        echo ""
        echo "════════════════════════════════════════════════════════════════"
        echo "✅ Workflow has passed on GitHub Actions."
        echo "Total time: ${elapsed_minutes} minutes"
        echo "════════════════════════════════════════════════════════════════"
        return 0
      else
        echo ""
        echo "Waiting for workflow to complete. Checking again in ${CHECK_INTERVAL} seconds..."
        echo "Elapsed: ${elapsed_minutes}m / Timeout: $((TIMEFRAME_SECONDS / 60))m"
        sleep $CHECK_INTERVAL
      fi
    else
      echo ""
      echo "════════════════════════════════════════════════════════════════"
      echo "❌ Workflow has failed on GitHub Actions."
      echo "════════════════════════════════════════════════════════════════"
      exit 1
    fi
  done
}
