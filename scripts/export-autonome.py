#!/usr/bin/env python3
"""Convert ALL relative markdown links to plain text + references section.

For each file in 00_caesn/, 01_cnisn/, 02_artsn/, 03_ptisn/:
1. Finds ALL [label](relative-path) links (including inside GENERATED blocks)
2. Replaces them with plain text (just the label)
3. Adds a "## Références" section at the end with title + path for each target
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ['00_caesn', '01_cnisn', '02_artsn', '03_ptisn']


def find_generated_ranges(content):
    """Return list of (start, end) positions for GENERATED blocks."""
    ranges = []
    for m in re.finditer(
        r'<!-- BEGIN:GENERATED.*?-->(.*?)<!-- END:GENERATED.*?-->',
        content, re.DOTALL
    ):
        ranges.append((m.start(), m.end()))
    return ranges


def is_in_generated(pos, gen_ranges):
    """Check if position is inside a GENERATED block."""
    return any(s <= pos <= e for s, e in gen_ranges)


def resolve_target(src_file, link):
    """Resolve a relative link to an absolute file path."""
    src_dir = os.path.dirname(src_file)
    target = os.path.normpath(os.path.join(src_dir, link))
    if not target.endswith('.md'):
        target += '.md'
    if os.path.exists(target):
        return target
    return None


def extract_title(filepath):
    """Extract title from frontmatter of a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Match YAML frontmatter
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if m:
            frontmatter = m.group(1)
            title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
            if title_match:
                return title_match.group(1).strip()
    except Exception:
        pass
    return None


def extract_id_from_link(label, link):
    """Try to extract a short ID from the link path or label."""
    # If label looks like an ID (e.g., CMP-06, ART-1), use it directly
    if re.match(r'^[A-Z]+-?\d+[A-Za-z]?$', label):
        return label
    # Try to extract from path (e.g., cmp-06.md -> CMP-06)
    basename = os.path.basename(link).replace('.md', '')
    # Convert to uppercase ID format
    return label


def format_reference(label, title, rel_path):
    """Format a single reference line."""
    if title:
        # Remove the ID prefix from title if it duplicates the label
        # e.g., "CMP-06 — Intégration..." -> "Intégration..."
        clean_title = re.sub(r'^[A-Z]+-?\d+[A-Za-z]?\s*[—–-]\s*', '', title)
        if clean_title:
            return f"- **{label}** — {clean_title} (`{rel_path}`)"
    return f"- **{label}** (`{rel_path}`)"


def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    gen_ranges = find_generated_ranges(content)

    # Collect all links to convert and their references
    links_to_convert = []  # (start, end, label, link, target_path)
    references = []  # (label, title, rel_path) - deduplicated

    seen_refs = set()

    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        label, link = m.group(1), m.group(2)

        # Skip non-relative links
        if link.startswith(('http://', 'https://', 'mailto:', '#')):
            continue

        # Skip links inside GENERATED blocks (managed by build_wrappers.py)
        pos = m.start()
        if is_in_generated(pos, gen_ranges):
            continue

        # Resolve target
        target = resolve_target(filepath, link)
        if target is None:
            # Can't resolve - just convert to text, no reference
            links_to_convert.append((m.start(), m.end(), label, link, None))
            continue

        links_to_convert.append((m.start(), m.end(), label, link, target))

        # Add to references (deduplicated by label)
        if label not in seen_refs:
            seen_refs.add(label)
            title = extract_title(target)
            rel_path = os.path.relpath(target, ROOT)
            references.append((label, title, rel_path))

    if not links_to_convert:
        return False  # Nothing to change

    # Build new content by replacing links from end to start
    # (to preserve positions)
    new_content = content
    for start, end, label, link, target in sorted(links_to_convert, key=lambda x: x[0], reverse=True):
        new_content = new_content[:start] + label + new_content[end:]

    # Add references section at the end
    # Remove trailing whitespace
    new_content = new_content.rstrip() + '\n\n'

    # Check if there's already a Références section
    if '## Références' not in new_content:
        new_content += '## Références\n\n'
        for label, title, rel_path in references:
            new_content += format_reference(label, title, rel_path) + '\n'
    else:
        # Append to existing section
        ref_start = new_content.index('## Références')
        ref_section = new_content[ref_start:]
        # Add new references after existing ones
        for label, title, rel_path in references:
            ref_line = format_reference(label, title, rel_path)
            if label not in ref_section:
                ref_section += ref_line + '\n'
        new_content = new_content[:ref_start] + ref_section

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    total_files = 0
    modified_files = 0

    for d in DIRS:
        pattern = os.path.join(ROOT, d, '**', '*.md')
        for filepath in sorted(glob.glob(pattern, recursive=True)):
            total_files += 1
            if process_file(filepath):
                modified_files += 1
                rel = os.path.relpath(filepath, ROOT)
                print(f"  ✓ {rel}")

    print(f"\n{modified_files}/{total_files} fichiers modifiés.")


if __name__ == '__main__':
    main()
