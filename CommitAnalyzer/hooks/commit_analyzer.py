#!/usr/bin/env python3

import subprocess
import re
import os

def main():
    # Load the desired regex pattern from .commitformat in the current repo
    format_file_path = '.commitformat'
    
    if not os.path.exists(format_file_path):
        print("Error: .commitformat file not found in the repository root!")
        return 1

    with open(format_file_path, 'r') as f:
        pattern = f.read().strip()

    # Get the last commit message
    commit_msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()

    # Validate the commit message
    if not re.match(pattern, commit_msg):
        print(f"Error: Commit message does not match the required format specified in .commitformat!")
        print(f"Expected format (regex): {pattern}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
