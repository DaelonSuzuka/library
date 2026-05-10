# PIC18F26K42 Family — Table of Contents

Source: DS40001919G, 841 pages. Bookmarks extracted programmatically (1665 entries, 3 levels deep).

## Section Map

| Sec | Title | Page | Priority | Lode File |
|-----|-------|------|----------|-----------|
| 1 | Device Overview | 19 | high | summary.md |
| 2 | Guidelines for Getting Started | 23 | medium | — |
| 3 | PIC18 CPU | 26 | low | — |
| 4 | Memory Organization | 33 | high | memory.md |
| 5 | Device Configuration | 65 | high | config.md |
| 6 | Resets | 81 | high | resets.md |
| 7 | Oscillator Module (with FSCM) | 92 | high | oscillator.md |
| 8 | Reference Clock Output (CLKREF) | 111 | medium | oscillator.md |
| 9 | Interrupt Controller | 115 | high | interrupts.md |
| 10 | Power-Saving Operation Modes | 170 | medium | — |
| 11 | Windowed Watchdog Timer (WWDT) | 178 | low | — |
| 12 | 8x8 Hardware Multiplier | 187 | low | — |
| 13 | Nonvolatile Memory (NVM) Control | 189 | high | nvm-crc.md |
| 14 | CRC Module with Memory Scanner | 213 | medium | nvm-crc.md |
| 15 | Direct Memory Access (DMA) | 228 | high | dma.md |
| 16 | I/O Ports | 260 | high | io-ports.md |
| 17 | Peripheral Pin Select (PPS) | 275 | high | pps.md |
| 18 | Interrupt-on-Change | 286 | medium | io-ports.md |
| 19 | Peripheral Module Disable (PMD) | 290 | medium | — |
| 20 | Timer0 Module | 299 | high | timers.md |
| 21 | Timer1/3/5 Module with Gate Control | 305 | high | timers.md |
| 22 | Timer2/4/6 Module | 320 | high | timers.md |
| 23 | Capture/Compare/PWM (CCP) | 342 | medium | ccp-pwm.md |
| 24 | Pulse-Width Modulation (PWM) | 355 | medium | ccp-pwm.md |
| 25 | Signal Measurement Timer (SMT) | 362 | medium | smt.md |
| 26 | Complementary Waveform Generator (CWG) | 406 | low | digital-peripherals.md |
| 27 | Configurable Logic Cell (CLC) | 434 | medium | digital-peripherals.md |
| 28 | Numerically Controlled Oscillator (NCO) | 449 | medium | digital-peripherals.md |
| 29 | Zero-Cross Detection (ZCD) | 459 | low | digital-peripherals.md |
| 30 | Data Signal Modulator (DSM) | 464 | low | digital-peripherals.md |
| 31 | UART With Protocol Support | 475 | high | uart.md |
| 32 | SPI Module | 513 | high | spi.md |
| 33 | I2C Module | 545 | high | i2c.md |
| 34 | Fixed Voltage Reference (FVR) | 598 | medium | analog.md |
| 35 | Temperature Indicator | 600 | low | analog.md |
| 36 | ADC with Computation (ADC2) | 602 | high | analog.md |
| 37 | 5-Bit DAC Module | 640 | medium | analog.md |
| 38 | Comparator Module | 644 | medium | analog.md |
| 39 | High/Low-Voltage Detect (HLVD) | 653 | low | analog.md |
| 40 | In-Circuit Serial Programming (ICSP) | 661 | medium | — |
| 41 | Instruction Set Summary | 663 | medium | — |
| 42 | Register Summary | 717 | high | registers.md |
| 43 | Development Support | 734 | low | — |
| 44 | Electrical Specifications | 738 | high | electrical.md |
| 45 | DC and AC Characteristics Graphs | 770 | medium | — |
| 46 | Packaging Information | 798 | medium | pins.md |
| 47 | Appendix A: Revision History | 837 | low | — |

## Errata

Source: DS80000773, 12 pages. 12 silicon issues + data sheet clarifications.
Key issues: UART BRGS/DALI, I2C, DMA EEPROM, ADC, WWDT, power-saving.

## Full Bookmark Hierarchy

Extracted programmatically from PDF metadata. 1665 entries total.
For the full tree with register-level detail, run:
```
cd library/tools && uv run python bookmarks.py "../datasheets/pic18f26k42/PIC18(L)F26-27-45-46-47-55-56-57K42-Data-Sheet-40001919G.pdf"
```