# Roadmap

## Register Enum Audit

Audit all hand-written register value enums across MC-7300 and AT-200ProIIv2 codebases against datasheet extractions. All three extracted families (Q41, K42, Q43) now have complete lodes. The Q84 family uses the same register values as Q43 (per pic_family.h).

**Files to audit** (in `MC-7300/src/peripherals/` and `AT-200ProIIv2/src/peripherals/`):
- `timer_constants.h` — Timer0/1/2 clock sources, prescalers, HLT modes (KNOWN BUG: Q41 uses Q43/Q84 Timer2 CS values)
- `src/pps_values.h` — PPS input/output routing values per family
- `oscillator.h` — OSCFRQ, OSCCON, OSCEN, clock source enums
- `clc.h` — CLC input selection mux values
- `adc.h` — ADC channel selection, computation mode enums
- `nonvolatile_memory.h` — NVM control register values
- `numerically_controlled_oscillator.h` — NCO clock sources, modes
- `signal_measurement_timer.h` — SMT input/clock selection values
- `pmd.h` — Peripheral Module Disable bit assignments
- `interrupt.h` — Interrupt vector/flag enums per family
- `ports.h` — Port register definitions
- `reset.h` — Reset control register values
- `fixed_voltage_reference.h` — FVR gain values
- `hlvd.h` — HLVD threshold values
- `spi.h` — SPI clock source, mode enums
- `uart.h` — UART config register enums
- `src/pps_values.h` — PPS output/input source value tables (detailed)

**Datasheets available**: Q41 (DS40002214), K42 (DS40001919), Q43 (DS40002147)
**Erratas available**: Q41 (DS80000901), K42 (DS80000773), Q43 (DS80000870)
**Q84**: Uses same register layout as Q43 per family header; no separate datasheet needed

**Approach**: For each file, cross-check every `#if FAMILY_*` branch's enum values against the corresponding lode register tables. Flag any mismatches, missing values, or wrong bit widths.

## Register Database Format Design

Design the merged register data format by surveying all consumer systems first. We have header structure (833 registers, addresses, bit fields, masks) and PDF semantics (value encodings, functional descriptions) as separate artifacts. The merge format must serve the systems that will programmatically consume it — not be designed in isolation. Needs a dedicated session to inventory consumers and review their APIs before committing to a schema.

## Server-Hosted Library

Move the master copy of the library to the proxmox server. An agent harness (hermes) autonomously maintains it — staleness checks, pulling updates, verifying lode sections. Dependency: proxmox rack rebuild. Related: `~/projects/lode/roadmap.md`.

## Librarian Agent Release

Package the library structure, procedures, directed indexing, synthesis, and hands-off testing as a reusable "librarian agent" project. Preconfigured so others can deploy it and start indexing their own reference repos.