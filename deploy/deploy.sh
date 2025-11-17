#!/usr/bin/env bash
set -e
echo $SECONDS

echo "=== Environment Variables ==="
printenv | sort

TIMEFRAME_SECONDS=240
PROJECT_ROOT="talkable-docs"
SUBPROJECT="docs"
# GitHub Actions configuration
GITHUB_API_BASE="https://api.github.com"
GITHUB_REPOSITORY="talkable/${PROJECT_ROOT}"
GITHUB_ACTIONS_WEB_URL="https://github.com/talkable/${PROJECT_ROOT}/actions?query=branch%3A${BRANCH_NAME}"

# Source shared GitHub Actions functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/lib/github_actions_common.sh"

TASK=$1

#FUNCTIONS
print_help() {
  clear
  echo 'Available Commands:'
  echo '   deploy           - deploy current version of talkable-docs'
  echo '   ci | cistatus | status   - check GitHub Actions build status'
  echo 'Example:'
  echo '         deploy.sh deploy'
  echo '         deploy.sh ci_status'
  exit 0
}

# GitHub Actions status function is now sourced from lib/github_actions_common.sh

remote_ssh_exec() {
  ssh -o StrictHostKeyChecking=no -i "$SSH_KEY" "$SSH_USER@$HOST_ENV" "$@"
}

deploy_docs() {
  remote_ssh_exec <<EOF
    set -e
    cd ${PROJECT_ROOT}/
    git checkout ${BRANCH_NAME}
    git branch -a
    git pull origin
    docker-compose ls
    docker ps
    docker-compose build --no-cache
    docker-compose up -d --force-recreate
EOF
}

deploy_check() {
  remote_ssh_exec <<EOF
    set -e
    cd ${PROJECT_ROOT}/
    docker-compose ls | grep ${SUBPROJECT}
    docker ps | grep ${SUBPROJECT}
EOF
}

case $TASK in
ci | ci_status | ci_only | status)
  gh_status
  deploy_check
  ;;
deploy)
  echo "Starting deployment..."
  gh_status
  deploy_docs
  deploy_check
  ;;
help|--help|-h)
  print_help
  ;;
*)
  echo "Unknown command: $TASK"
  echo "Use '$0 --help' for usage."
  exit 1
  ;;
esac
