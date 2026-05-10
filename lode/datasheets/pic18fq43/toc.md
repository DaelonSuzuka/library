# PIC18F27Q43 Family — Table of Contents

Source: DS40002147H, 968 pages. Bookmarks extracted programmatically.

## Section Map

| Sec | Title | Page | Priority | Lode File |
|-----|-------|------|----------|-----------|
| 1 | Packages | 10 | low | pins.md |
| 2 | Pin Diagrams | 11 | low | pins.md |
| 3 | Pin Allocation Tables | 15 | high | pins.md |
| 4 | Guidelines for Getting Started | 20 | medium | — |
| 5 | Register Naming | 25 | low | — |
| 6 | Register Legend | 27 | low | — |
| 7 | PIC18 CPU | 28 | medium | — |
| 8 | Device Configuration | 46 | high | config.md |
| 9 | Memory Organization | 61 | high | memory.md |
| 10 | NVM — Nonvolatile Memory | 92 | high | nvm-crc.md |
| 11 | VIC — Vectored Interrupt Controller | 118 | high | interrupts.md |
| 12 | Oscillator Module | 196 | high | oscillator.md |
| 13 | CRC with Memory Scanner | 222 | medium | nvm-crc.md |
| 14 | Resets | 239 | high | resets.md |
| 15 | Windowed WDT | 253 | low | — |
| 16 | DMA — Direct Memory Access | 263 | high | dma.md |
| 17 | Power-Saving Operation Modes | 300 | medium | — |
| 18 | PMD — Peripheral Module Disable | 309 | medium | — |
| 19 | I/O Ports | 319 | high | io-ports.md |
| 20 | Interrupt-on-Change | 335 | medium | io-ports.md |
| 21 | PPS — Peripheral Pin Select | 341 | high | pps.md |
| 22 | CLC — Configurable Logic Cell | 353 | medium | digital-peripherals.md |
| 23 | CLKREF — Reference Clock Output | 373 | medium | oscillator.md |
| 24 | Timer0 Module | 378 | high | timers.md |
| 25 | Timer1/3/5 with Gate Control | 386 | high | timers.md |
| 26 | Timer2/4/6 with HLT | 402 | high | timers.md |
| 27 | SMT — Signal Measurement Timer | 424 | medium | smt.md |
| 28 | CCP — Capture/Compare/PWM | 449 | medium | ccp-pwm.md |
| 29 | Timer Selection | 462 | low | timers.md |
| 30 | PWM — Pulse-Width Modulation | 465 | medium | ccp-pwm.md |
| 31 | CWG — Complementary Waveform Generator | 492 | medium | digital-peripherals.md |
| 32 | NCO — Numerically Controlled Oscillator | 520 | medium | digital-peripherals.md |
| 33 | DSM — Data Signal Modulator | 530 | low | digital-peripherals.md |
| 34 | UART with Protocol Support | 541 | high | uart.md |
| 35 | SPI Module | 591 | high | spi.md |
| 36 | I2C Module | 625 | high | i2c.md |
| 37 | HLVD — High/Low-Voltage Detect | 711 | low | analog.md |
| 38 | FVR — Fixed Voltage Reference | 719 | medium | analog.md |
| 39 | Temperature Indicator | 723 | low | analog.md |
| 40 | ADCC — ADC with Computation | 728 | high | analog.md |
| 41 | DAC — 8-Bit DAC | 774 | medium | analog.md |
| 42 | CMP — Comparator | 779 | medium | analog.md |
| 43 | ZCD — Zero-Cross Detection | 790 | low | analog.md |
| 44 | Instruction Set Summary | 798 | medium | — |
| 45 | ICSP | 874 | medium | — |
| 46 | Register Summary | 877 | high | registers.md |
| 47 | Electrical Specifications | 891 | high | electrical.md |
| 48 | DC/AC Characteristics Graphs | 917 | medium | — |
| 49 | Packaging Information | 936 | low | pins.md |
| 50 | Appendix A: Revision History | 963 | low | — |

## Errata

Source: DS80000870M, 15 pages. 13+ silicon issues across 4 revisions (B0–C0).
Key issues: I2C (11 errata, multi-host broken), ADCC CVD, SMT reset, SRAM read-back (B0), ICD software breakpoints, UART TXDE, XT mode 2 MHz limit.
Full details in `datasheets/pic18fq43/extracted-errata/errata.md`.