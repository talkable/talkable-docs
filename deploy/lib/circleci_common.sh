#!/usr/bin/env bash
set -e
# CircleCI Common Functions Library
# Simplified for talkable-docs single-job workflow

# Ensure required variables are set
: "${CIRCLE_CI_API_BASE:=https://circleci.com/api/v2}"
# CIRCLE_CI_TOKEN should be set in environment

# Get build status for a specific commit
# Returns the status of the "build" job
get_build_status() {
  local commit=$1
  
  # Get recent pipelines and find the one for our commit
  local response=$(curl -s -H "Circle-Token: $CIRCLE_CI_TOKEN" \
    "${CIRCLE_CI_API_BASE}/project/${CIRCLE_CI_PROJECT_SLUG}/pipeline?branch=${BRANCH_NAME}")
  
  # Extract pipeline ID for the specific commit
  local pipeline_id=$(echo "$response" | jq -r --arg commit "$commit" \
    '.items[] | select(.vcs.revision == $commit) | .id' | head -n 1)
  
  if [[ -z "$pipeline_id" || "$pipeline_id" == "null" ]]; then
    echo "no_pipeline"
    return
  fi
  
  # Get workflows for pipeline (we only have one workflow)
  local workflows_response=$(curl -s -H "Circle-Token: $CIRCLE_CI_TOKEN" \
    "${CIRCLE_CI_API_BASE}/pipeline/${pipeline_id}/workflow")
  
  # Get the first (and only) workflow ID
  local workflow_id=$(echo "$workflows_response" | jq -r '.items[0].id')
  
  if [[ -z "$workflow_id" || "$workflow_id" == "null" ]]; then
    echo "no_workflow"
    return
  fi
  
  # Get jobs for workflow (we only have one "build" job)
  local jobs_response=$(curl -s -H "Circle-Token: $CIRCLE_CI_TOKEN" \
    "${CIRCLE_CI_API_BASE}/workflow/${workflow_id}/job")
  
  # Get the build job status
  local build_status=$(echo "$jobs_response" | jq -r '.items[] | select(.name == "build") | .status')
  
  echo "$build_status"
}

# Get pipeline number for display/linking
get_pipeline_number() {
  local commit=$1
  
  local response=$(curl -s -H "Circle-Token: $CIRCLE_CI_TOKEN" \
    "${CIRCLE_CI_API_BASE}/project/${CIRCLE_CI_PROJECT_SLUG}/pipeline?branch=${BRANCH_NAME}")
  
  echo "$response" | jq -r --arg commit "$commit" \
    '.items[] | select(.vcs.revision == $commit) | .number' | head -n 1
}

# Monitor CircleCI build status
circleci_status() {
  local start_time=$SECONDS
  local short_commit="${GIT_COMMIT:0:7}"
  
  echo "=========================================================================="
  echo "Starting CircleCI build monitoring for commit: ${short_commit}"
  echo "=========================================================================="

  while true; do
    echo ""
    echo "Checking build status at $(date)..."
    
    # Get build status
    local build_status=$(get_build_status "$GIT_COMMIT")
    local pipeline_number=$(get_pipeline_number "$GIT_COMMIT")
    
    # Check if pipeline exists
    if [[ "$build_status" == "no_pipeline" ]]; then
      echo "⚠️  No CircleCI pipeline found for commit ${short_commit}"
      echo "Check CircleCI: ${CIRCLE_CI_WEB_URL}"
      exit 1
    fi
    
    if [[ "$build_status" == "no_workflow" ]]; then
      echo "⚠️  No workflow found in pipeline for commit ${short_commit}"
      echo "Check CircleCI: ${CIRCLE_CI_WEB_URL}"
      exit 1
    fi
    
    # Create direct pipeline URL
    local pipeline_url="https://app.circleci.com/pipelines/github/${CIRCLE_CI_PROJECT_SLUG#gh/}/${pipeline_number}"
    echo "Pipeline: #${pipeline_number} (${pipeline_url})"
    
    # Check build status
    case "$build_status" in
      "success")
        echo "✅ Build: passed successfully"
        echo ""
        echo "=========================================================================="
        echo "🎉 The sphinx build has succeeded!"
        echo "Total elapsed time: $(((SECONDS - start_time) / 60)) minutes"
        echo "=========================================================================="
        break
        ;;
      "failed")
        echo "❌ Build: failed"
        echo ""
        echo "=========================================================================="
        echo "The sphinx build has failed on CircleCI."
        echo "Check CircleCI: ${pipeline_url}"
        echo "=========================================================================="
        exit 1
        ;;
      "canceled")
        echo "✗ Build: was cancelled"
        echo ""
        echo "=========================================================================="
        echo "The sphinx build was cancelled on CircleCI."
        echo "Check CircleCI: ${pipeline_url}"
        echo "=========================================================================="
        exit 1
        ;;
      "running")
        echo "⏳ Build: is still running..."
        ;;
      "queued")
        echo "⏳ Build: is queued..."
        ;;
      "not_running")
        echo "⏳ Build: waiting for available agent..."
        ;;
      *)
        echo "❓ Build: status is ${build_status}"
        ;;
    esac
    
    # Check timeout
    if [[ $SECONDS -gt $TIMEFRAME_SECONDS ]]; then
      echo ""
      echo "=========================================================================="
      echo "⏰ Build timeout after $((TIMEFRAME_SECONDS / 60)) minutes"
      echo "Check CircleCI: ${pipeline_url}"
      echo "=========================================================================="
      exit 228
    fi
    
    echo "Elapsed: $(((SECONDS - start_time) / 60))m / Timeout: $((TIMEFRAME_SECONDS / 60))m"
    echo "Next check in 8 seconds..."
    sleep 8
  done
}
