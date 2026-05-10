# PIC18F27Q43 Family — Lode Map

```
lode/datasheets/pic18fq43/
├── summary.md              # chip overview, key peripherals, family variants, used-by
├── lode-map.md             # this file
├── toc.md                  # section-to-page map
├── config.md               # CONFIG1L–5H device configuration bits
├── memory.md               # flash/SRAM org, banked addressing, Access Bank, NVM, DIA/DCI
├── interrupts.md           # VIC, IVTBASE, PIR/PIE/IPR, shadow registers, vector table
├── io-ports.md             # PORT/LAT/TRIS/ANSEL/ODCON/SLRCON/INLVL/WPU, IOC
├── pps.md                  # PPS input/output selection, value tables, bidirectional pins
├── timers.md               # TMR0/1/3/5, TMR2/4/6, clock sources, HLT modes
├── oscillator.md           # OSCCON1/2/3, OSCFRQ, OSCEN, FSCM, ACT, CLKREF
├── resets.md               # reset types, PCON0/1, BOR, start-up sequence
├── uart.md                 # UART1–5, baud rate, DMX/LIN/DALI, TXDE errata
├── spi.md                  # SPI1/2 host/client, FIFOs, clock config
├── i2c.md                  # I2C1 host/client, 10-bit, timeout, extensive errata
├── dma.md                  # DMA1–6, trigger sources, addressing modes, system arbiter
├── analog.md               # ADCC, DAC1 (8-bit), CMP1-2, FVR, temperature, HLVD, ZCD
├── digital-peripherals.md  # CLC1–8, NCO1–3, CWG1–3, DSM, PWM1–3
├── ccp-pwm.md              # CCP1–3, PWM1–3 (16-bit), capture/compare modes
├── smt.md                  # SMT1, 11 operating modes, signal/window muxes, errata
├── nvm-crc.md              # NVM programming, flash/EEPROM, CRC scanner
├── registers.md            # SFR address quick-ref by peripheral
├── electrical.md            # VDD/IDD, I/O specs, ADC, thermal
└── pins.md                  # pin diagrams/allocation, PPS tables
```

## Raw Extractions (in datasheets/pic18fq43/)

- `extracted/s01-s50.md` — 50 sections, pdftotext + clean (DS40002147H, 968 pages)
- `extracted-errata/errata.md` — Q43 family errata (DS80000870M, 15 pages)
- `registers.json` — 1023 registers from XC8 header
- `sections.txt` — page range map for extract.py

## Key Cross-Check Findings

- Q43 has 6 DMA channels (DMA1–6) vs 2 on K42 and 4 on Q41; system arbiter priority registers include DMA1PR–DMA6PR plus SCANPR
- I2C has extensive errata across all silicon revisions (B0–C0); multi-host mode is broken — avoid I2C multi-host
- Timer clock source fields differ by family; Q43 Timer2 CS is 4-bit (same width as K42, different from Q84)
- SMT reset bit must not be set when prescaler ≠ 00 (all revisions)
- PWM is 16-bit on Q43 (vs 10-bit on K42); 3 instances vs 4 on K42