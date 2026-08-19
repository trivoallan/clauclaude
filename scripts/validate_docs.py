#!/usr/bin/env python3
"""
Validation script for clauclaude documentation repository.
Checks:
 1. Docusaurus frontmatter (sidebar_position) for files under docs/
 2. Internal markdown relative links integrity
 3. Basic formatting / missing files
"""

import sys
import re
from pathlib import Path

def validate():
    root = Path(__file__).resolve().parent.parent
    docs_dir = root / "docs"

    if not docs_dir.exists():
        print("Warning: docs/ directory not found in repository.")

    md_files = list(root.glob("**/*.md"))
    print(f"Checking {len(md_files)} markdown files...")

    errors = []
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for md_file in md_files:
        rel_path = md_file.relative_to(root)
        content = md_file.read_text(encoding="utf-8")

        # Check Docusaurus frontmatter for docs/ files (excluding README.md)
        if "docs" in rel_path.parts and md_file.name != "README.md":
            if not content.startswith("---"):
                errors.append(f"Missing YAML frontmatter in {rel_path}")

        # Check relative links
        matches = link_pattern.findall(content)
        for text, url in matches:
            if url.startswith(("http://", "https://", "#", "mailto:")):
                continue

            clean_url = url.split("#")[0]
            if not clean_url:
                continue

            target_path = (md_file.parent / clean_url).resolve()
            if not target_path.exists():
                errors.append(
                    f"Broken link in {rel_path}: [{text}]({url}) -> Target '{target_path}' does not exist."
                )

    if errors:
        print("\n❌ Validation failed with errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ All markdown files and links validated successfully!")
        sys.exit(0)

if __name__ == "__main__":
    validate()
