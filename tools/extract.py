#!/usr/bin/env python3
"""Extract PDF sections to individual markdown files using pdftotext.

Given a PDF and a section map (page ranges + filenames), extracts each section
to its own .md file in the output directory. Uses pdftotext -layout for
high-fidelity text extraction that preserves register table formatting.

Usage:
  # Extract from a TOC definition file (one section per line):
  uv run python extract.py pdf_path sections.txt -o output_dir

  # Extract arbitrary page range:
  uv run python extract.py pdf_path -f 17 -l 21 -o output_dir/s04-getting-started.md

Sections file format (one entry per line):
  section_number  first_page-last_page  filename_base
  # e.g.:
  8 43-56 s08-device-configuration
  11 113-174 s11-vic

Lines starting with # are ignored. Blank lines are ignored.
"""

import argparse
import os
import subprocess
import sys


def parse_sections_file(path: str) -> list[tuple[int, int, int, str]]:
    """Parse sections file into list of (sec, first_page, last_page, filename)."""
    sections = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 3:
                print(f"Bad line (expected 3 fields): {line}", file=sys.stderr)
                continue
            sec = int(parts[0])
            first, last = parts[1].split("-")
            fname = parts[2]
            sections.append((sec, int(first), int(last), fname))
    return sections


def extract_range(pdf_path: str, first: int, last: int, output_path: str) -> int:
    """Extract page range from PDF to output file. Returns byte count, 0 on error."""
    result = subprocess.run(
        ["pdftotext", "-layout", "-f", str(first), "-l", str(last), pdf_path, output_path],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"pdftotext error (pp {first}-{last}): {result.stderr}", file=sys.stderr)
        return 0
    return os.path.getsize(output_path)


def extract_section(pdf_path: str, first: int, last: int, output_path: str, force: bool = False) -> None:
    """Extract one section, skip if exists and non-empty unless force."""
    if not force and os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        print(f"SKIP {os.path.basename(output_path)} (exists)")
        return
    size = extract_range(pdf_path, first, last, output_path)
    if size > 0:
        print(f"OK   {os.path.basename(output_path)}  pp{first}-{last}  {size} bytes")
    else:
        print(f"FAIL {os.path.basename(output_path)}  pp{first}-{last}")


def main():
    parser = argparse.ArgumentParser(description="Extract PDF sections to markdown files")
    parser.add_argument("pdf", help="Path to PDF file")
    parser.add_argument("sections", nargs="?", help="Sections definition file (required for batch mode)")
    parser.add_argument("-o", "--output", required=True, help="Output directory (batch) or output file (single)")
    parser.add_argument("-f", "--first", type=int, help="First page (single range mode)")
    parser.add_argument("-l", "--last", type=int, help="Last page (single range mode)")
    parser.add_argument("--force", action="store_true", help="Re-extract even if file exists")
    args = parser.parse_args()

    if not os.path.isfile(args.pdf):
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        sys.exit(1)

    # Single range mode
    if args.first and args.last:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        size = extract_range(args.pdf, args.first, args.last, args.output)
        if size > 0:
            print(f"OK   pp{args.first}-{args.last}  {size} bytes  →  {args.output}")
        else:
            print(f"FAIL pp{args.first}-{args.last}")
        return

    # Batch mode
    if not args.sections:
        print("Either --first/--last for single range, or sections file for batch mode", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(args.sections):
        print(f"Sections file not found: {args.sections}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)
    sections = parse_sections_file(args.sections)

    extracted = 0
    skipped = 0
    for sec, first, last, fname in sections:
        outpath = os.path.join(args.output, f"{fname}.md")
        if not args.force and os.path.exists(outpath) and os.path.getsize(outpath) > 0:
            print(f"SKIP {fname} (exists)")
            skipped += 1
            continue
        size = extract_range(args.pdf, first, last, outpath)
        if size > 0:
            print(f"OK   {fname}  pp{first}-{last}  {size} bytes")
            extracted += 1
        else:
            print(f"FAIL {fname}  pp{first}-{last}")

    print(f"\nExtracted {extracted} new, skipped {skipped} existing, total {len(sections)} sections")


if __name__ == "__main__":
    main()