# Datasheet Practices

## One Monolithic Lode Per Device

Never factor out shared content across device lodes. Each device gets its own complete lode — even if the CPU core, instruction set, or NVM chapter is identical across three devices. Duplication costs KB; branching costs the agent clarity on every read. When the agent is coding for a specific chip on a specific board, it needs one file per peripheral with every answer for that chip and zero ambiguity about which variant applies.

## Two-Layer Model

- **Raw extraction** (`datasheets/<device>/extracted/`): pdftotext output, per-chapter files, page-marked, boilerplate-stripped. This is the source-of-record for PDF content.
- **Curated lode** (`lode/datasheets/<device>/`): synthesized, agent-friendly topic files. One file per peripheral/feature. Contains merged register structure + value encodings + operational notes.

Never skip the raw extraction step. The lode is a summary; the raw extraction is the audit trail. If the lode says something questionable, the agent can fall back to the raw extraction on the same chapter to verify.

## Extraction Pipeline

For Microchip datasheets:
1. `bookmarks.py` → TOC
2. Write `sections.txt` (page ranges for each chapter)
3. `extract.py` → per-chapter `.md` files
4. `clean_microchip.py --in-place` → strip page headers/footers
5. `scan_figures.py` → catalog Figure labels with page refs
6. `parse_header.py` → XC8 `.h` → `registers.json`

The pipeline is deterministic and re-runnable. If a new PDF revision drops, re-extract from step 3 with `--force`.

## Register Data: Header Structure + PDF Semantics

- XC8 device header → register addresses, bit field names, positions, sizes, masks
- PDF extracted text → value encodings (what each bit pattern means), R/W access, functional descriptions
- Complete register definition = union of both sources
- Don't merge until consumer systems are audited — format must be driven by consumers

## Adding New Families

When adding a new device family (e.g., K42, Q43):
1. Extract that family's datasheet through the full pipeline
2. Build its own monolithic lode — do not attempt to factor shared content with existing lodes
3. Audit hand-written enums in project code against the new extractions
4. Only after several devices are done, consider if any factoring actually helps (it probably won't)

## Figures

- `scan_figures.py` finds all Figure labels (346 for Q41)
- Block diagrams, timing diagrams, and graphs need vision extraction
- Register tables rendered fine as text — not figures
- Two-column graph pages (s49-style) mangle figure labels; those pages need vision regardless
- Figure extraction is a separate pass, done on demand when a specific diagram matters