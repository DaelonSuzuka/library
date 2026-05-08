# Lode Map

```
library/
├── repos/                           # cloned repos (git-ignored)
│   ├── godot/
│   ├── godot-docs/
│   ├── vscode-docs/
│   └── vscode-extension-samples/
├── datasheets/                      # PDFs + extracted markdown (git-ignored)
│   ├── pic18f16q41/
│   │   ├── DS40002214.pdf
│   │   ├── sections.txt             # page-range → filename map for extract.py
│   │   ├── registers.json           # 833 registers parsed from XC8 header
│   │   └── extracted/              # 48 section .md files (s01-s51, full 962pp)
│   ├── ad8310/
│   │   └── AD8310.pdf
│   ├── in-pi554fch/
│   │   └── IN-PI554FCH_v2.5.pdf
│   ├── esp32-s3/
│   │   ├── esp32-s3_datasheet.pdf
│   │   └── esp32-s3_technical_reference_manual.pdf
│   └── esp32-s3-wroom/
│       └── esp32-s3-wroom_datasheet.pdf
├── lode/                            # agent-navigable tree
│   ├── summary.md                   # library overview
│   ├── lode-map.md                  # this file
│   ├── terminology.md               # library-specific terms
│   ├── practices.md                 # library maintenance patterns
│   ├── opencode-config.md           # global opencode config documentation
│   ├── roadmap.md                   # active work items
│   ├── todo.md                      # unvetted ideas
│   ├── procedures.md                # re-clone, staleness check, pull & verify
│   ├── registry.md                  # list of all content with source URLs
│   ├── version-markers.md           # date + commit hash per repo
│   ├── use-cases.md                 # directed indexing and synthesis patterns
│   ├── tmp/                         # session scraps (git-ignored)
│   ├── repos/                       # repo lode subtrees
│   │   ├── godot/
│   │   │   ├── summary.md
│   │   │   ├── lode-map.md
│   │   │   ├── core.md
│   │   │   ├── servers.md
│   │   │   ├── scene.md
│   │   │   ├── editor.md
│   │   │   ├── modules.md
│   │   │   ├── platform.md
│   │   │   └── gdextension.md
│   │   ├── godot-docs/
│   │   │   ├── summary.md
│   │   │   └── lode-map.md
│   │   ├── vscode-docs/
│   │   │   ├── summary.md
│   │   │   └── lode-map.md
│   │   └── vscode-extension-samples/
│   │       ├── summary.md
│   │       └── lode-map.md
│   └── datasheets/                  # datasheet lode subtrees
│       ├── practices.md            # datasheet tending practices
│       └── pic18f16q41/
│           ├── summary.md
│           ├── lode-map.md
│           ├── toc.md
│           └── pins.md
├── tools/                            # extraction scripts (uv project)
│   ├── pyproject.toml
│   ├── bookmarks.py                 # PDF bookmark/TOC extraction
│   ├── extract.py                   # PDF section extraction via pdftotext
│   ├── clean_microchip.py           # strip Microchip page boilerplate
│   ├── scan_figures.py              # find Figure labels with page/line refs
│   └── parse_header.py              # XC8 .h → structured register JSON
├── reclone.sh
```

## Related Lodes

- **Workspace Lode**: `~/projects/lode/` — environment context and project index
