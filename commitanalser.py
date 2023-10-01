#!/usr/bin/env python3

import subprocess
import re
import os

def main():
    # Get the repository root
    repo_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()

    # Load the desired regex pattern from .commitformat
    format_file_path = os.path.join(repo_root, '.commitformat')
    
    if not os.path.exists(format_file_path):
        print("Error: .commitformat file not found in the repository root!")
        exit(1)

    with open(format_file_path, 'r') as f:
        pattern = f.read().strip()

    # Get the last commit message
    commit_msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()

    # Validate the commit message
    if not re.match(pattern, commit_msg):
        print(f"Error: Commit message does not match the required format specified in .commitformat!")
        print(f"Expected format (regex): {pattern}")
        exit(1)

if __name__ == "__main__":
    main()
