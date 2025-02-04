#!/usr/bin/env bash
set -ex
echo $SECONDS

echo "=== Environment Variables ==="
printenv | sort

TIMEFRAME_SECONDS=240
PROJECT_ROOT="talkable-docs"
SUBPROJECT="docs"
CIRCLE_CI_API_URL="https://api.github.com/repos/talkable/${PROJECT_ROOT}/commits/${GIT_COMMIT}/status"
CIRCLE_CI_URL="https://app.circleci.com/pipelines/github/talkable/${PROJECT_ROOT}?branch="
TASK=$1

#FUNCTIONS
print_help() {
  clear
  echo 'Available Commands:'
  echo '   deploy           - deploy current version of talkable'
  echo '   ci | cistatus | status   - status on CircleCI'
  echo 'Example:'
  echo '         deploy.sh deploy'
  echo '         deploy.sh cistatus'
  exit 0
}

ci_status() {
  show_status() {
    curl -s -u "$GITHUB_ACC_USR":"$GITHUB_ACC_PSW" "$CIRCLE_CI_API_URL" | jq -r '.statuses[]' | jq '.context, .state' | grep ci/circleci -A1
  }

  while true; do
    local tests_status
    tests_status=$(curl -s -u "$GITHUB_ACC_USR":"$GITHUB_ACC_PSW" "$CIRCLE_CI_API_URL" |
      jq -e -r '
      [.statuses[].state] as $states |
      if ($states | length) == 0 then
        "no_tests"
      elif $states | all(. == "success") then
        "success"
      elif $states | any(. == "failure" or . == "error") then
        "failure"
      elif $states | any(. == "pending") then
        "pending"
      else
        "unknown"
      end
    ')

    if [[ -z $tests_status ]]; then
      echo "Error: Could not retrieve tests statuses. Check API response or credentials."
      exit 1
    fi

    if [[ $tests_status == "success" ]]; then
      show_status
      echo "The sphinx build has succeeded!"
      break
    elif [[ $tests_status == "failure" ]]; then
      show_status
      echo -e "The Sphinx build failed on CircleCI.\nCheck the CircleCI results here: $CIRCLE_CI_URL$BRANCH_NAME"
      exit 1
    elif [[ $tests_status == "no_tests" ]]; then
      show_status
      echo -e "There is no sphinx build on CircleCI for the commit.\nCheck the CircleCI results here: $CIRCLE_CI_URL$ENV_BRANCH"
      exit 1
    elif [[ $tests_status == "pending" ]]; then
      echo "Tests is pending or queued. Waiting for sphinx build ..."
    fi

    if [[ $SECONDS -gt $TIMEFRAME_SECONDS ]]; then
      show_status
      echo -e "The build is marked as FAILURE by timeout.\nCheck the CircleCI results here: $CIRCLE_CI_URL$ENV_BRANCH"
      echo "Total elapsed time: $((SECONDS / 60)) minutes"
      exit 228
    fi

    echo "Waiting for all tests to succeed. Next check in 8 seconds..."
    echo "Elapsed time: $((SECONDS / 60)) minutes. Timeout at $((TIMEFRAME_SECONDS / 60)) minutes."
    sleep 8
  done

  echo "CI checks completed successfully."
  echo "Total elapsed time: $((SECONDS / 60)) minutes"
}

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
    docker-compose down -v
    docker-compose up -d --build --remove-orphans
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
  ci_status
  deploy_check
  ;;
deploy)
  echo "Starting deployment..."
  ci_status
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
