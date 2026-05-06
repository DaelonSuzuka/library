#!/usr/bin/env python3
"""Extract PDF structure to structured markdown.

Strategy:
1. Try embedded bookmarks first (instant, exact, no hallucination)
2. If no bookmarks, fall back to pdftotext TOC extraction (fast, local)
3. If neither works, report that vision extraction is needed
"""

import sys
import subprocess
import argparse
import pymupdf


def extract_bookmarks(pdf_path: str) -> list[tuple[int, str, int]]:
    """Extract embedded PDF bookmarks as list of (level, title, page)."""
    doc = pymupdf.open(pdf_path)
    return doc.get_toc()


def extract_toc_from_text(pdf_path: str) -> list[tuple[int, str, int]] | None:
    """Try to extract TOC from PDF text content using pdftotext.
    
    Looks for common TOC patterns (numbered sections with page numbers).
    Returns list of (1, title, page) or None if no TOC found.
    """
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "10", pdf_path, "-"],
            capture_output=True, text=True, timeout=10
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    
    if result.returncode != 0:
        return None
    
    entries = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        # Match patterns like "1.  Title .... 42" or "1. Title.......42"
        # Dots/periods between title and page number
        import re
        m = re.match(r'^(\d+)\.\s+(.+?)\s*[.·…\s]{3,}\s*(\d+)\s*$', line)
        if m:
            sec_num, title, page = m.groups()
            entries.append((1, f"{sec_num}. {title.strip()}", int(page)))
    
    return entries if len(entries) >= 3 else None


def bookmarks_to_markdown(toc: list[tuple[int, str, int]], min_level: int = 1, max_level: int = 3) -> str:
    """Convert bookmark list to markdown table."""
    lines = ["| Level | Section | Page |", "|-------|---------|------|"]
    for level, title, page in toc:
        if level < min_level or level > max_level:
            continue
        indent = "  " * (level - 1)
        lines.append(f"| {level} | {indent}{title.strip()} | {page} |")
    return "\n".join(lines)


def bookmarks_to_tree(toc: list[tuple[int, str, int]], min_level: int = 1, max_level: int = 2) -> str:
    """Convert bookmark list to indented tree format."""
    lines = []
    for level, title, page in toc:
        if level < min_level or level > max_level:
            continue
        indent = "  " * (level - 1)
        lines.append(f"{indent}{title.strip()} .... p{page}")
    return "\n".join(lines)


def bookmarks_to_csv(toc: list[tuple[int, str, int]]) -> str:
    """Convert bookmark list to CSV."""
    lines = ["level,title,page"]
    for level, title, page in toc:
        title_clean = title.strip().replace('"', '""')
        lines.append(f'{level},"{title_clean}",{page}')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract PDF structure")
    parser.add_argument("pdf", help="Path to PDF file")
    parser.add_argument("-f", "--format", choices=["markdown", "tree", "csv"], default="markdown")
    parser.add_argument("--min-level", type=int, default=1)
    parser.add_argument("--max-level", type=int, default=3)
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    parser.add_argument("--fallback-toc", action="store_true", help="Try text-based TOC extraction if no bookmarks")
    args = parser.parse_args()

    toc = extract_bookmarks(args.pdf)
    source = "bookmarks"
    
    if not toc and args.fallback_toc:
        toc = extract_toc_from_text(args.pdf)
        source = "text-TOC"
    
    if not toc:
        doc = pymupdf.open(args.pdf)
        print(f"No bookmarks found in {args.pdf} ({doc.page_count} pages).", file=sys.stderr)
        if not args.fallback_toc:
            print("Try --fallback-toc to attempt text-based TOC extraction.", file=sys.stderr)
        else:
            print("No text-based TOC found either. Vision extraction required.", file=sys.stderr)
        print("For vision extraction, convert pages to images:", file=sys.stderr)
        print(f"  pdftoppm -png -r 600 {args.pdf} /tmp/opencode/output", file=sys.stderr)
        print("Then feed to vision model with extraction prompt.", file=sys.stderr)
        sys.exit(1)
    
    print(f"# Extracted from {source} ({len(toc)} entries)", file=sys.stderr)
    
    if args.format == "markdown":
        result = bookmarks_to_markdown(toc, args.min_level, args.max_level)
    elif args.format == "tree":
        result = bookmarks_to_tree(toc, args.min_level, args.max_level)
    elif args.format == "csv":
        result = bookmarks_to_csv(toc)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result + "\n")
    else:
        print(result)


if __name__ == "__main__":
    main()
