#! /bin/bash
# Halt script on error
set -e

# Clear the repository
make clean

# Create a virtualenv and clone scancode
make conf

# Get the latest commit
cd scancode-toolkit
COMMIT_LATEST="$(git log -1 --format=format:'%h' --abbrev-commit)"
cd ../

# Check if scancode develop has new commits
# if yes, update latest commit and continue
# if no, fail here
venv/bin/python ./etc/scripts/check_commit.py --commit "$COMMIT_LATEST"

# build docs
make licensedb

# delete cloned scancode as only the doc updates should be commited
rm -rf scancode-toolkit/
