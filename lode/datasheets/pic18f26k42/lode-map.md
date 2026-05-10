# PIC18F26K42 Family — Lode Map

```
lode/datasheets/pic18f26k42/
├── summary.md              # chip overview, key peripherals, family variants, used-by
├── lode-map.md             # this file
├── config.md               # CONFIG1L–5H device configuration bits
├── memory.md               # flash/SRAM org, banked addressing, Access Bank, NVM
├── interrupts.md           # VIC, IVTBASE, PIR/PIE/IPR, shadow registers, vector table
├── io-ports.md             # PORT/LAT/TRIS/ANSEL/ODCON/SLRCON/INLVL/WPU, IOC
├── pps.md                   # PPS input/output selection, value tables, bidirectional pins
├── timers.md                # TMR0/1/3/5, TMR2/4/6, clock sources, HLT modes
├── oscillator.md            # OSCCON1/2/3, OSCFRQ, OSCEN, FSCM, CLKREF
├── resets.md                # reset types, PCON0/1, BOR, start-up sequence
├── uart.md                  # UART1/2, baud rate, DMX/LIN/DALI, FIFOs
├── spi.md                   # SPI1 host/client, FIFOs, clock config
├── i2c.md                   # I2C1/2 host/client, 10-bit, timeout
├── dma.md                   # DMA1/2, trigger sources, addressing modes
├── analog.md                # ADC2, DAC, CMP, FVR, temperature, HLVD
├── digital-peripherals.md   # CLC1–4, NCO1, CWG1–3, DSM, ZCD
├── ccp-pwm.md               # CCP1–4, PWM5–8, capture/compare modes
├── smt.md                   # SMT1, 11 operating modes, signal/window muxes
├── nvm-crc.md               # NVM programming, flash/EEPROM, CRC scanner
├── registers.md             # SFR address quick-ref by peripheral
├── electrical.md            # VDD/IDD, I/O specs, ADC, thermal
└── pins.md                  # pin diagrams/allocation, PPS tables (28-pin full, others need vision)
```

## Raw Extractions (in datasheets/pic18f26k42/)

- `extracted/s01-s47.md` — 47 sections, pdftotext + clean (DS40001919G, 841 pages)
- `extracted-errata/errata.md` — K42 family errata (DS80000773, 12 pages)
- `registers.json` — 792 registers from XC8 header
- `sections.txt` — page range map for extract.py

## Key Cross-Check Finding

See timers.md — K42 Timer1 CS field is 5-bit (vs 4-bit on Q41), Timer2 CS field is 4-bit
(vs 5-bit on Q43/Q84). `timer_constants.h` must use correct per-family clock source encodings.