# Roadmap

## Register Enum Audit

Audit all hand-written register value enums across MC-200 and MC-7300 codebases (timer_constants.h, pps_values.h, oscillator.h, etc.) against the datasheet extractions. Must extract datasheets for all supported families first — Q43/Q84 and K42 have different register values (see the timer_constants.h #if branches). Part of the register database format design session.

## Register Database Format Design

Design the merged register data format by surveying all consumer systems first. We have header structure (833 registers, addresses, bit fields, masks) and PDF semantics (value encodings, functional descriptions) as separate artifacts. The merge format must serve the systems that will programmatically consume it — not be designed in isolation. Needs a dedicated session to inventory consumers and review their APIs before committing to a schema.

## Server-Hosted Library

Move the master copy of the library to the proxmox server. An agent harness (hermes) autonomously maintains it — staleness checks, pulling updates, verifying lode sections. Dependency: proxmox rack rebuild. Related: `~/projects/lode/roadmap.md`.

## Librarian Agent Release

Package the library structure, procedures, directed indexing, synthesis, and hands-off testing as a reusable "librarian agent" project. Preconfigured so others can deploy it and start indexing their own reference repos.