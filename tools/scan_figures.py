#!/usr/bin/env python3
"""Scan Microchip datasheet extractions for Figure labels.

Finds all "Figure X-Y. Title" lines in cleaned extraction files and reports
their location (file, line number, page number from nearest page marker).

Output formats:
  summary  — one line per figure: file, figure number, title, page
  json     — structured JSON for further processing
"""

import re
import json
import sys
import argparse
from pathlib import Path

FIGURE_RE = re.compile(r'^\s*Figure\s+(\d+-\d+)\.\s*(.+?)\s*$', re.MULTILINE)


def find_page_markers(text: str) -> list[int]:
    """Build a map from line number to page number using --- pNNN --- markers."""
    pages = []
    for i, line in enumerate(text.split('\n')):
        m = re.match(r'^--- p(\d+) ---$', line.strip())
        if m:
            pages.append((i, int(m.group(1))))
    return pages


def page_for_line(pages: list[tuple[int, int]], line_no: int) -> int | None:
    """Return the page number for a given line using nearest preceding marker."""
    for i in range(len(pages) - 1, -1, -1):
        if pages[i][0] <= line_no:
            return pages[i][1]
    return None


def scan_file(filepath: Path) -> list[dict]:
    """Scan a single extraction file for figures."""
    text = filepath.read_text()
    pages = find_page_markers(text)
    first_page = pages[0][1] if pages else None

    figures = []
    for m in FIGURE_RE.finditer(text):
        fig_num = m.group(1)
        title = m.group(2).strip()
        # Line number (1-indexed)
        line_no = text[:m.start()].count('\n') + 1
        page = page_for_line(pages, text[:m.start()].count('\n'))

        figures.append({
            'file': filepath.name,
            'figure': fig_num,
            'title': title,
            'line': line_no,
            'page': page,
        })

    return figures


def main():
    parser = argparse.ArgumentParser(description="Scan extracted sections for Figure labels")
    parser.add_argument('directory', help='Directory of s*.md extraction files')
    parser.add_argument('-f', '--format', choices=['summary', 'json'], default='summary')
    args = parser.parse_args()

    directory = Path(args.directory)
    files = sorted(directory.glob('s*.md'))

    all_figures = []
    for f in files:
        all_figures.extend(scan_file(f))

    if args.format == 'json':
        json.dump(all_figures, sys.stdout, indent=2)
        print()
    else:
        # Summary: table format
        print(f"{'File':<38} {'Figure':<10} {'Page':<6} Title")
        print('-' * 90)
        for fig in all_figures:
            page_str = str(fig['page']) if fig['page'] else '?'
            print(f"{fig['file']:<38} {fig['figure']:<10} {page_str:<6} {fig['title']}")

        print(f"\nTotal: {len(all_figures)} figures across {len(files)} sections")


if __name__ == "__main__":
    main()