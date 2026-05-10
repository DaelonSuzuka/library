# PIC18F06Q41 / PIC18F16Q41 — Lode Map

```
lode/datasheets/pic18f16q41/
├── summary.md       # chip overview, key peripherals, used-by
├── lode-map.md      # this file
├── toc.md           # section→page map with extraction priority
├── errata.md         # silicon errata (DS80000901) issues and workarounds
├── config.md        # device configuration bits (CONFIG1-9)
├── memory.md        # memory org, NVM, flash programming
├── interrupts.md    # VIC, IOC, IRQ numbers, priority
├── io-ports.md      # PORT/LAT/TRIS/ANSEL/ODCON registers
├── pps.md           # PPS input/output selection, pin routing
├── timers.md        # TMR0/1/2, prescaler/postscaler, clock sources
├── oscillator.md    # OSCFRQ, clock switching, FSCM, ACT
├── resets.md        # reset types, PCON, BOR, startup sequence
├── uart.md          # UART1/2/3 setup, baud rate, DMX/DALI/LIN
├── spi.md           # SPI1/2 host/client, FIFOs, DMA
├── i2c.md           # I2C host/client, 10-bit, SMBus, DMA
├── dma.md           # 4-channel DMA, setup, priority
├── adc.md           # ADCC, FVR, computation modes, CVD
├── dac.md           # DAC1/2 registers, value encodings
├── registers.md     # SFR address quick-reference by peripheral
├── electrical.md    # absolute max, VDD range, IDD, I/O specs
└── pins.md          # pin diagrams/allocation
```

## Raw Extractions (in datasheets/pic18f16q41/)

- `extracted/s01-s51.md` — all 48 sections, pdftotext + clean (2.4 MB)
- `extracted-errata/errata.md` — Q41 silicon errata (DS80000901)
- `registers.json` — 833 registers from XC8 header (311 KB)
- `sections.txt` — page range map for extract.py
- `headers/` — XC8 device headers (.h + .inc) for all 6 Q41 members
- `headers/pds/` — PDS programming scripts (ICSP protocol)

## Key Cross-Check Finding

`timer_constants.h` uses Q43/Q84 timer clock source values for Q41 —
CLC/TMR offsets are wrong, Timer2 CS field is 4-bit not 5-bit.
See timers.md for full details.