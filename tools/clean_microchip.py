#!/usr/bin/env python3
"""Clean Microchip datasheet pdftotext output into readable markdown.

Removes boilerplate lines:
- Page headers (device name, chapter title)
- Page footers ("Data Sheet DS...-NNN", copyright, subsidiaries)
- Form feeds
- Excessive blank lines (3+ → 2)

Preserves:
- Page markers as "--- pNNN ---"
- All content text and table formatting
- Diagram debris (separate pass)
"""

import re
import sys
import argparse

FOOTER_RE = re.compile(r'Data\s+Sheet\s+DS\d+[A-Z]*\s*-\s*(\d+)')
COPYRIGHT_RE = re.compile(r'©.*Microchip\s+Technology', re.UNICODE)
SUBSIDIARIES_RE = re.compile(r'^\s+subsidiaries\s*$')
DEVICE_RE = re.compile(r'PIC1[68]F\d{2,}/?\d*[QK]\d+')


def clean(text: str) -> str:
    # First pass: identify lines to remove (headers/footers)
    lines = text.split('\n')
    remove = [False] * len(lines)

    for i, line in enumerate(lines):
        stripped = line.rstrip()

        # Footer line
        if FOOTER_RE.search(stripped):
            remove[i] = True
            continue

        # Copyright line
        if COPYRIGHT_RE.search(stripped):
            remove[i] = True
            continue

        # Subsidiaries line
        if SUBSIDIARIES_RE.match(stripped):
            remove[i] = True
            continue

        # Device name line (only word on the line is the part number)
        words = stripped.split()
        if len(words) == 1 and DEVICE_RE.match(words[0]):
            remove[i] = True
            # Also remove next line — it's the chapter title running header
            if i + 1 < len(lines):
                remove[i + 1] = True
            continue

    # Second pass: build output, collapse blanks, insert page markers
    out = []
    prev_blank = 0
    page_marker_needed = []  # collect page numbers to emit at page breaks

    for i, line in enumerate(lines):
        if remove[i]:
            # If this was a footer, queue a page marker
            fm = FOOTER_RE.search(line)
            if fm:
                out.append(f'--- p{fm.group(1)} ---')
            continue

        stripped = line.rstrip()
        # Remove form feed characters
        if stripped == '\x0c':
            continue
        stripped = stripped.replace('\x0c', '')

        # Blank line collapsing
        if not stripped:
            prev_blank += 1
            if prev_blank <= 2:
                out.append('')
            continue
        prev_blank = 0

        out.append(stripped)

    # Trim leading/trailing blanks
    while out and not out[0]:
        out.pop(0)
    while out and not out[-1]:
        out.pop()

    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description="Clean Microchip pdftotext output")
    parser.add_argument("input", help="Input file (or - for stdin)")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    parser.add_argument("--in-place", action="store_true", help="Overwrite input file")
    args = parser.parse_args()

    if args.input == '-':
        text = sys.stdin.read()
    else:
        with open(args.input) as f:
            text = f.read()

    result = clean(text)

    if args.in_place:
        with open(args.input, 'w') as f:
            f.write(result)
    elif args.output:
        with open(args.output, 'w') as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()