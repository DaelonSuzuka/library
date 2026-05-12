# Lode Map

```
library/
├── repos/                           # cloned repos (git-ignored)
│   ├── godot/
│   ├── godot-docs/
│   ├── nicegui/
│   ├── quasar/
│   ├── fastapi/
│   ├── vue-docs/
│   ├── vscode-docs/
│   └── vscode-extension-samples/
├── datasheets/                      # PDFs + extracted markdown (git-ignored)
│   ├── pic18f16q41/
│   │   ├── DS40002214.pdf
│   │   ├── PIC18F06-16Q41-Si-Errata-Data-Sheet-Clarifications-DS80000901.pdf
│   │   ├── sections.txt             # page-range → filename map for extract.py
│   │   ├── registers.json           # 833 registers parsed from XC8 header
│   │   ├── extracted/              # 48 section .md files (s01-s51, full 962pp)
│   │   └── extracted-errata/        # errata extraction
│   ├── pic18f26k42/
│   │   ├── PIC18(L)F26-27-45-46-47-55-56-57K42-Data-Sheet-40001919G.pdf
│   │   ├── PIC18-L-F27-47-57K42-Si-Errata-Data-Sheet-Clarification-DS80000773.pdf
│   │   ├── sections.txt             # page-range → filename map for extract.py
│   │   ├── registers.json           # 792 registers parsed from XC8 header
│   │   ├── extracted/               # 47 section .md files (s01-s47, full 841pp)
│   │   └── extracted-errata/        # errata extraction (12pp)
│   ├── pic18fq43/
│   │   ├── PIC18F27-47-57Q43-Microcontroller-Data-Sheet-XLP-DS40002147.pdf
│   │   ├── PIC18F27-47-57Q43-Si-Errata-Data-Sheet-Clarifications-DS80000870.pdf
│   │   ├── sections.txt             # page-range → filename map for extract.py
│   │   ├── registers.json           # 1023 registers parsed from XC8 header
│   │   ├── extracted/               # 50 section .md files (s01-s50, full 968pp)
│   │   └── extracted-errata/        # errata extraction (16pp)
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
│   │   │   └── lode-map.md              # deep file-level path index (1434 RST files)
│   │   ├── vscode-docs/
│   │   │   ├── summary.md
│   │   │   └── lode-map.md              # deep file-level path index (API + docs + learn + blogs)
│   │   └── vscode-extension-samples/
│   │       ├── summary.md
│   │       └── lode-map.md              # deep sample index (81+ samples with APIs + guide links)
│   │   ├── nicegui/
│   │   │   ├── summary.md              # Python web UI framework (Vue+Quasar backend)
│   │   │   ├── lode-map.md             # package structure, 90+ elements, 59 examples
│   │   │   └── custom-behavior.md      # 8 mechanisms for customizing/extending elements
│   │   └── quasar/
│   │       ├── summary.md              # Vue.js component library & framework
│   │       └── lode-map.md             # 79 component dirs, composables, directives, plugins
│   │   ├── fastapi/
│   │   │   ├── summary.md              # Python web API framework (Starlette+Pydantic)
│   │   │   └── lode-map.md             # tutorial, advanced, reference, how-to, deployment
│   │   └── vue-docs/
│   │       ├── summary.md              # Vue 3 documentation
│   │       └── lode-map.md             # guide, API reference, examples, tutorial, style guide
│   └── datasheets/                  # datasheet lode subtrees
│       ├── practices.md            # datasheet tending practices
│       ├── pic18f16q41/
│       │   ├── summary.md
│       │   ├── lode-map.md
│       │   ├── toc.md
│       │   ├── pins.md
│       │   └── errata.md
│       ├── pic18f26k42/
│       │   ├── summary.md
│       │   ├── lode-map.md
│       │   ├── toc.md
│       │   ├── config.md
│       │   ├── memory.md
│       │   ├── interrupts.md
│       │   ├── io-ports.md
│       │   ├── pps.md
│       │   ├── timers.md
│       │   ├── oscillator.md
│       │   ├── resets.md
│       │   ├── uart.md
│       │   ├── spi.md
│       │   ├── i2c.md
│       │   ├── dma.md
│       │   ├── analog.md
│       │   ├── digital-peripherals.md
│       │   ├── ccp-pwm.md
│       │   ├── smt.md
│       │   ├── nvm-crc.md
│       │   ├── registers.md
│       │   ├── electrical.md
│       │   └── pins.md
│       └── pic18fq43/
│           ├── summary.md
│           ├── lode-map.md
│           ├── toc.md
│           ├── config.md
│           ├── memory.md
│           ├── interrupts.md
│           ├── io-ports.md
│           ├── pps.md
│           ├── timers.md
│           ├── oscillator.md
│           ├── resets.md
│           ├── uart.md
│           ├── spi.md
│           ├── i2c.md
│           ├── dma.md
│           ├── analog.md
│           ├── digital-peripherals.md
│           ├── ccp-pwm.md
│           ├── smt.md
│           ├── nvm-crc.md
│           ├── registers.md
│           ├── electrical.md
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
