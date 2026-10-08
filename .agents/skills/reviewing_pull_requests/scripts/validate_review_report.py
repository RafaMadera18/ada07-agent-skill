#!/usr/bin/env python3
"""
Validates deterministic structure of a PR Readiness Review report.
Ensures required sections and mandatory fields exist before human review.
"""

import sys
import os
import re

REQUIRED_HEADERS = [
    "Review Context",
    "Requirements / Acceptance Criteria Reviewed",
    "Test Evidence",
    "MUST FIX",
    "SHOULD FIX",
    "OPTIONAL",
    "Final Review Summary",
]

REQUIRED_PATTERNS = [
    (r"Human decision required:\s*YES", "Human decision required: YES declaration"),
    (r"MUST FIX count:\s*\d+", "MUST FIX count metric"),
    (r"SHOULD FIX count:\s*\d+", "SHOULD FIX count metric"),
    (r"OPTIONAL count:\s*\d+", "OPTIONAL count metric"),
]


def validate_report(filepath: str) -> bool:
    if not os.path.exists(filepath):
        print(f"ERROR: File does not exist: {filepath}", file=sys.stderr)
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    missing_headers = []
    for header in REQUIRED_HEADERS:
        pattern = rf"^##\s+{re.escape(header)}"
        if not re.search(pattern, content, re.MULTILINE):
            missing_headers.append(header)

    missing_patterns = []
    for pat, desc in REQUIRED_PATTERNS:
        if not re.search(pat, content, re.IGNORECASE):
            missing_patterns.append(desc)

    if missing_headers or missing_patterns:
        print("INVALID: PR readiness review structure is incomplete.", file=sys.stderr)
        for h in missing_headers:
            print(f"  - Missing section header: '## {h}'", file=sys.stderr)
        for p in missing_patterns:
            print(f"  - Missing required field: {p}", file=sys.stderr)
        return False

    print("VALID: PR readiness review structure is complete.")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_review_report.py <path_to_report.md>", file=sys.stderr)
        sys.exit(2)

    target_file = sys.argv[1]
    is_valid = validate_report(target_file)
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
