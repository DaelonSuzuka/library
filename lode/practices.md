# Practices

## Version Markers

- Every cloned repo must have a version marker (date + commit hash)
- Markers must be updated after every pull
- Never skip the verify step after pulling — always check if lode sections need updating

## Registry

- Every repo in `repos/` must have a corresponding entry in `lode/registry.md`
- The registry is the source of truth for what the library contains

## Effort Asymmetry

- The librarian burns context upfront so consumers don't have to
- Library artifacts are for agents, not humans — prose quality doesn't matter, completeness and structure do
- This means testing is cheap: you can read raw source to craft deep questions, then measure whether a consumer subagent answers efficiently through the lode
- Metric: tool call count. Few calls = lode is doing its job. Falling back to raw source = lode has gaps

## Datasheet Extraction

- Use `tools/extract.py` for pdftotext-based section extraction (fast, no vision needed)
- Each PDF gets a `sections.txt` alongside it defining page ranges and output filenames
- Sections are extracted as individual `.md` files into `extracted/` directory
- Skip existing non-zero files by default; `--force` to re-extract
- `pdftotext -layout` preserves register table formatting; handles ~90% of datasheet content
- Vision model (pdftoppm → Gemini) only for diagrams, pinout graphics, and scanned PDFs
- After extraction, run `tools/clean_microchip.py --in-place` on all section files
- After cleaning, run `tools/scan_figures.py` to catalog Figure labels (page/line refs)
- `pdftotext -layout` with default `-colspacing` is optimal for Microchip PDFs; two-column graph pages need vision extraction anyway

## Register Database

- XC8 device headers are the canonical source for register structure (addresses, bit positions, masks)
- Use `tools/parse_header.py` to extract 833 registers into `registers.json`
- Header provides: name, address, bit fields with position/size/mask, three naming levels (short, prefixed, individual bits)
- PDF text provides: value encodings (what each bit pattern means), functional descriptions, R/W access
- Complete register definition = union of header structure + PDF semantics

## Reports

- Directed indexing and synthesis queries produce structured reports, not raw search results
- Reports should be saved to `lode/tmp/` or a project-specific lode, not the library lode itself