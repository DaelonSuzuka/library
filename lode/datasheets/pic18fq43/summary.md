# PIC18F27Q43 Family — Summary

PIC18 Q43 eXtreme Low Power (XLP) family. 8 device members across three flash densities (32/64/128 KB) and three pin counts (28/40+44/48). All devices share the same peripheral set; larger-pin parts expose more GPIO. VDD range 1.8–5.5V — no separate LF variants needed.

## Family Members

| Device | Flash | RAM | EEPROM | Packages | I/O Ports |
|--------|-------|-----|--------|----------|-----------|
| PIC18F25Q43 | 32KB | 2KB | 1KB | 28-pin SPDIP/SOIC/SSOP/VQFN | A,B,C,E |
| PIC18F26Q43 | 64KB | 4KB | 1KB | 28-pin SPDIP/SOIC/SSOP/VQFN | A,B,C,E |
| PIC18F27Q43 | 128KB | 8KB | 1KB | 28-pin SPDIP/SOIC/SSOP/VQFN | A,B,C,E |
| PIC18F45Q43 | 32KB | 2KB | 1KB | 40-pin PDIP/QFN, 44-pin TQFP | A,B,C,D,E |
| PIC18F46Q43 | 64KB | 4KB | 1KB | 40-pin PDIP/QFN, 44-pin TQFP | A,B,C,D,E |
| PIC18F47Q43 | 128KB | 8KB | 1KB | 40-pin PDIP/QFN, 44-pin TQFP | A,B,C,D,E |
| PIC18F55Q43 | 32KB | 2KB | 1KB | 48-pin TQFP/VQFN | A,B,C,D,E,F |
| PIC18F56Q43 | 64KB | 4KB | 1KB | 48-pin TQFP/VQFN | A,B,C,D,E,F |
| PIC18F57Q43 | 128KB | 8KB | 1KB | 48-pin TQFP/VQFN | A,B,C,D,E,F |

## Architecture

- CPU: PIC18 enhanced RISC, 16-bit instructions, 8-bit data
- Vectored Interrupt Controller (VIC) with fixed priority resolution
- 6 DMA channels (vs 2 on K42, 4 on Q41)
- Active Clock Tuning (ACT) — HFINTOSC auto-calibrated against SOSC
- 8×8 hardware multiplier (single-cycle)
- System arbiter with priority-based memory access (ISR/MAIN/DMA/Scanner)
- Device Information Area (DIA) with factory calibration values
- Memory Access Partition (MAP) for bootloader protection
- 87 instructions with Extended Instruction Set enabled

## Key Peripherals

- 5× UART (1 with DMX/DALI/LIN, 4 standard)
- 2× SPI (host/client with FIFOs)
- 1× I2C (host/client, 10-bit addr, SMBus)
- ADCC (12-bit ADC with computation, CVD, up to 46 external channels on 48-pin)
- 1× DAC (8-bit)
- 2× Comparator
- 1× ZCD (zero-cross detect)
- Timer0–Timer6 (5 16-bit + 2 8-bit with HLT)
- 1× SMT (32-bit signal measurement timer)
- 3× CCP (capture/compare/PWM)
- 3× PWM (16-bit, independent)
- 3× CWG (complementary waveform generator)
- 3× NCO (numerically controlled oscillator)
- 1× DSM (data signal modulator)
- 8× CLC (configurable logic cells)
- CRC with memory scanner
- Windowed WDT
- HLVD (high/low-voltage detect)
- PMD (peripheral module disable)

## Pin Features

- Full PPS — most digital peripherals can route to any pin
- I2C-capable pins on most ports (INLVL selects TTL/ST vs I2C thresholds)
- Maximum I/O: 24 (28-pin), 35 (40/44-pin), 43 (48-pin)
- RE3/MCLR is input-only on 28/40/44-pin variants

## VDD Range

- All F variants: 1.8V–5.5V (XLP — no separate LF needed)
- Max 64 MHz at VDD ≥ 2.7V, 32 MHz at VDD < 2.7V
- Industrial temp: -40°C to +85°C; Extended: -40°C to +125°C

## Used By

- MC-200 (via `pic_family.h` FAMILY_Q43, `timer_constants.h`)
- MC-7300 (via `pic_family.h` FAMILY_Q43, `timer_constants.h`)
- AT-200ProIIv2 (via `pic_family.h` FAMILY_Q43, `timer_constants.h`)

## Datasheet

DS40002147H, 968 pages. Full extraction in `datasheets/pic18fq43/extracted/`.

## Errata

DS80000870 (Rev M, 08/2024). Current silicon: C0. Key issues:
- ADCC: CVD only functional on PORTA[2:0] and PORTB[4:0] (B0); double-sample extra acquisition (all revs)
- Oscillator: XT mode limited to 2 MHz (B0, B2)
- I2C: address registers wrong reset value (B0–B3); spurious Start/Stop on enable (B0–B3); multi-host bus failures (all revs); MDR not cleared after bus timeout (all revs); bus timeout not detected with external clock stretch (all revs); clock stretch disable broken (all revs); bus timeout false Start/Stop (all revs); BFREDR=1 non-functional (all revs); CSTR not cleared after timeout (all revs); bus collision + Stop may hang (all revs); multi-host arbitration may hang (all revs)
- SRAM: read-back may return 0 after power-up (B0 only, needs power cycle)
- ICD: software breakpoints unavailable (all revs)
- SMT: reset bit breaks module if prescaler ≠ 00 (all revs)
- UART: TXDE signal may go low before STOP bit fully transmitted (all revs)

Full details in `datasheets/pic18fq43/extracted-errata/errata.md`.

## Register Database

1023 registers parsed from XC8 header → `datasheets/pic18fq43/registers.json`
Lode register reference → `lode/datasheets/pic18fq43/registers.md`

## Key Differences from K42 and Q41

| Feature | K42 | Q41 | Q43 |
|---------|-----|------|-----|
| UART | 2 (1 w/ DMX/DALI) | 3 (all w/ DMX/DALI) | 5 (1 w/ DMX/DALI) |
| SPI | 1 | 2 (w/ FIFOs) | 2 (w/ FIFOs) |
| I2C | 2 | 1 | 1 |
| CCP/PWM | 4/4 (10-bit) | 1/3 | 3/3 (16-bit) |
| CWG | 3 | 1 | 3 |
| DMA channels | 2 | 4 | 6 |
| NCO | 1 | 1 | 3 |
| CLC | 4 | 4 | 8 |
| DAC | 1 (5-bit) | 2 (8-bit) | 1 (8-bit) |
| SMT | 1 | 1 | 1 |
| ACT | — | — | Yes |
| Flash max | 128KB | 64KB | 128KB |
| RAM max | 8KB | 4KB | 8KB |
| EEPROM | 1KB | 512B | 1KB |
| VDD range | F:2.5–5.5V | 1.8–5.5V | 1.8–5.5V |