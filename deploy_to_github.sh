    #!/bin/bash
# Usage: ./deploy_to_github.sh <git-remote-url>
set -e
if [ -z "$1" ]; then
  echo "Usage: $0 git@github.com:USER/REPO.git"
  exit 1
fi
REMOTE=$1
git init
git checkout -b main
git add .
git commit -m "Initial commit: quantum-ai-optimizer upgraded"
git remote add origin $REMOTE
git push -u origin main
