# Library Summary

Reference library at `~/projects/library/`. Contains cloned external repos, extracted datasheets, and parsed device headers. Indexed for directed research and cross-repo synthesis.

## Content

| Directory | Contents |
|-----------|----------|
| `repos/` | Cloned external source repos (git-ignored) |
| `datasheets/` | PDFs + extracted markdown + parsed headers per device (git-ignored) |
| `tools/` | Extraction and parsing scripts (uv project, version-controlled) |

## Datasheet Pipeline

For Microchip PDFs, the full pipeline is:
1. `bookmarks.py` → extract TOC structure
2. Write `sections.txt` → page ranges for each chapter
3. `extract.py` → pdftotext per section into `extracted/s*.md`
4. `clean_microchip.py --in-place` → strip page headers/footers
5. `scan_figures.py` → catalog all Figure labels with page refs
6. `parse_header.py` → XC8 .h → `registers.json`

## PIC18F16Q41 Coverage

- 833 registers parsed from XC8 header (structure + addresses + bit fields)
- 48 sections extracted and cleaned (2.4 MB, full 962 pages)
- 346 figures cataloged (diagrams, timing waveforms, graphs)
- Register value encodings and functional descriptions still in PDF text
- Complete register definition = header structure + PDF semantics

## Lode Structure

Each content item has a mirror lode subtree under `lode/`:
- `lode/repos/<name>/` — repo index lodes
- `lode/datasheets/<part>/` — datasheet lodes

See [lode-map.md](lode-map.md) for full tree.