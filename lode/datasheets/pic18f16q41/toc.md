# PIC18F06Q41 / PIC18F16Q41 — Table of Contents

Source: DS40002214F, 962 pages. Bookmarks extracted programmatically (1243 entries, 4 levels deep).

## Section Map

| Sec | Title | Page | Priority | Lode File |
|-----|-------|------|----------|-----------|
| 1 | Packages | 10 | high | pins.md |
| 2 | Pin Diagrams | 11 | high | pins.md |
| 3 | Pin Allocation Tables | 13 | high | pins.md |
| 4 | Guidelines for Getting Started with PIC18-Q41 | 17 | medium | — |
| 5 | Register and Bit Naming Conventions | 22 | medium | registers.md |
| 6 | Register Legend | 24 | medium | registers.md |
| 7 | PIC18 CPU | 25 | low | — |
| 8 | Device Configuration | 43 | high | config.md |
| 9 | Memory Organization | 57 | high | memory.md |
| 10 | NVM - Nonvolatile Memory Module | 87 | high | memory.md |
| 11 | VIC - Vectored Interrupt Controller | 113 | high | interrupts.md |
| 12 | OSC - Oscillator Module (with FSCM) | 175 | medium | — |
| 13 | CRC - Cyclic Redundancy Check with Memory Scanner | 203 | low | — |
| 14 | Resets | 222 | medium | — |
| 15 | WWDT - Windowed Watchdog Timer | 236 | low | — |
| 16 | DMA - Direct Memory Access | 246 | medium | — |
| 17 | Power-Saving Modes | 283 | low | — |
| 18 | PMD - Peripheral Module Disable | 292 | low | — |
| 19 | I/O Ports | 300 | high | pins.md |
| 20 | IOC - Interrupt-on-Change | 315 | medium | interrupts.md |
| 21 | PPS - Peripheral Pin Select | 321 | high | pps.md |
| 22 | CLC - Configurable Logic Cell | 332 | low | — |
| 23 | CLKREF - Reference Clock Output | 352 | low | — |
| 24 | TMR0 - Timer0 Module | 357 | medium | timers.md |
| 25 | TMR1 - Timer1 Module with Gate Control | 365 | medium | timers.md |
| 26 | TMR2 - Timer2 Module | 381 | medium | timers.md |
| 27 | SMT - Signal Measurement Timer | 402 | medium | timers.md |
| 28 | CCP - Capture/Compare/PWM Module | 426 | medium | timers.md |
| 29 | Capture, Compare, and PWM Timers Selection | 439 | low | — |
| 30 | PWM - Pulse-Width Modulator with Compare | 442 | medium | timers.md |
| 31 | CWG - Complementary Waveform Generator | 469 | low | — |
| 32 | NCO - Numerically Controlled Oscillator | 497 | medium | timers.md |
| 33 | DSM - Data Signal Modulator | 506 | low | — |
| 34 | UART - Universal Asynchronous Receiver Transmitter | 517 | high | uart.md |
| 35 | SPI - Serial Peripheral Interface | 567 | medium | spi.md |
| 36 | I2C - Inter-Integrated Circuit | 601 | low | — |
| 37 | HLVD - High/Low-Voltage Detect | 692 | low | — |
| 38 | FVR - Fixed Voltage Reference | 700 | medium | adc.md |
| 39 | Temperature Indicator | 705 | low | — |
| 40 | ADCC - Analog-to-Digital Converter with Computation | 711 | high | adc.md |
| 41 | DAC - Digital-to-Analog Converter | 756 | high | dac.md |
| 42 | OPA - Operational Amplifier | 764 | low | — |
| 43 | CMP - Comparator Module | 776 | low | — |
| 44 | ZCD - Zero-Cross Detection | 787 | low | — |
| 45 | Instruction Set Summary | 795 | medium | — |
| 46 | ICSP - In-Circuit Serial Programming | 871 | medium | — |
| 47 | Register Summary | 874 | high | registers.md |
| 48 | Electrical Specifications | 886 | high | electrical.md |
| 49 | DC and AC Characteristics Graphs and Tables | 914 | medium | electrical.md |
| 50 | Packaging Information | 938 | low | — |
| 51 | Appendix A: Revision History | 957 | low | — |

## Extraction Plan

Phase 1 — High priority (firmware essentials):
- Sec 1-3: Pins & packages (pp 10-16) ✅
- Sec 8: Device configuration (pp 43-56)
- Sec 9-10: Memory organization & NVM (pp 57-112)
- Sec 11: VIC interrupts (pp 113-174)
- Sec 19: I/O Ports (pp 300-314)
- Sec 21: PPS (pp 321-331)
- Sec 34: UART (pp 517-566)
- Sec 40: ADCC (pp 711-755)
- Sec 41: DAC (pp 756-763)
- Sec 47: Register summary (pp 874-885)
- Sec 48: Electrical specs (pp 886-913)

Phase 2 — Medium priority:
- Sec 5-6: Register conventions & legend (pp 22-24)
- Sec 12: OSC (pp 175-202)
- Sec 14: Resets (pp 222-235)
- Sec 16: DMA (pp 246-282)
- Sec 20: IOC (pp 315-320)
- Sec 24-28: Timers (pp 357-438)
- Sec 30,32: PWM, NCO (pp 442-505)
- Sec 35: SPI (pp 567-600)
- Sec 38: FVR (pp 700-704)
- Sec 45: Instruction set (pp 795-870)
- Sec 46: ICSP (pp 871-873)

Phase 3 — Low priority (extract on demand):
- Sec 4,7,13,15,17,18,22,23,29,31,33,36,37,39,42-44,49-51

## Full Bookmark Hierarchy

Extracted programmatically from PDF metadata. 1243 entries total.
For the full tree with register-level detail, run:
```
cd library/tools && uv run python bookmarks.py -f tree --max-level 3 ../datasheets/pic18f16q41/DS40002214.pdf
```
