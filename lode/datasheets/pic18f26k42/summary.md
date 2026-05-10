# PIC18F26K42 — Summary

PIC18 K42 family mid-range 8-bit MCU. Up to 128KB flash, 8KB RAM, 1KB EEPROM, 64 MHz max. 8 device members in F and LF (extended-voltage) variants: 26/27/45/46/47/55/56/57K42. 28-pin (26/27) and 40/44/48-pin (45/46/47/55/56/57) packages. All share the same peripheral set; larger-pin parts expose more GPIO.

## Family Members

| Device | Flash | RAM | EEPROM | Packages | I/O Ports |
|--------|-------|-----|--------|----------|-----------|
| PIC18(L)F26K42 | 64KB | 4KB | 1KB | 28-pin SPDIP/SOIC/SSOP/QFN/UQFN | A,B,C,E |
| PIC18(L)F27K42 | 128KB | 8KB | 1KB | 28-pin SPDIP/SOIC/SSOP/QFN/UQFN | A,B,C,E |
| PIC18(L)F45K42 | 32KB | 2KB | 256B | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A,B,C,D,E |
| PIC18(L)F46K42 | 64KB | 4KB | 1KB | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A,B,C,D,E |
| PIC18(L)F47K42 | 128KB | 8KB | 1KB | 40-pin PDIP/UQFN, 44-pin TQFP/QFN | A,B,C,D,E |
| PIC18(L)F55K42 | 32KB | 2KB | 256B | 48-pin TQFP/UQFN/VQFN | A,B,C,D,E,F |
| PIC18(L)F56K42 | 64KB | 4KB | 1KB | 48-pin TQFP/UQFN/VQFN | A,B,C,D,E,F |
| PIC18(L)F57K42 | 128KB | 8KB | 1KB | 48-pin TQFP/UQFN/VQFN | A,B,C,D,E,F |

LF variants support extended low-voltage operation down to 1.8V.

## Architecture

- CPU: PIC18 enhanced RISC, 16-bit instructions, 8-bit data
- Vectored Interrupt Controller (VIC) with fixed priority resolution
- 2 DMA channels (vs 4 on Q41)
- Memory Access Partition (MAP) for bootloader protection
- Device Information Area (DIA) with factory calibration values
- 87 instructions with Extended Instruction Set enabled

## Key Peripherals

- 2× UART (1 standard, 1 with DMX/DALI/LIN and auto-baud)
- 1× SPI
- 2× I2C (host/client, 10-bit addr, SMBus)
- ADC2 (12-bit ADC with computation, 5 internal + up to 43 external channels)
- 1× DAC (5-bit)
- 2× Comparator
- 1× ZCD (zero-cross detect)
- Timer0 (8/16-bit), Timer1 (16-bit with gate), Timer2/4/6 (with HLT) — 4 16-bit + 3 8-bit
- 1× SMT (32-bit signal measurement)
- 4× CCP, 4× PWM (10-bit, independent)
- 3× CWG (complementary waveform generator)
- 1× NCO, 1× DSM
- 4× CLC (configurable logic cells)
- CRC with memory scanner
- Windowed WDT
- HLVD (high/low-voltage detect)
- PMD (peripheral module disable)

## Pin Features

- Full PPS — most digital peripherals can route to any pin
- Maximum I/O: 24 pins (28-pin), 35 pins (44-pin), 43 pins (48-pin)
- PORTE RE3 is input-only on 28/40/44-pin variants

## VDD Range

- F variants: 2.5V–5.5V (per errata A3: 3.0V min at ≤32 MHz below 25°C; 3.0V min above 32 MHz)
- LF variants: 1.8V–3.6V (per errata A3: 2.5V min at ≤32 MHz below 25°C; 2.7V min above 32 MHz)
- Industrial temp: -40°C to +85°C; Extended: -40°C to +125°C

## Used By

- MC-200 (via `pic_family.h` FAMILY_K42, `timer_constants.h`)
- MC-7300 (via `pic_family.h` FAMILY_K42, `timer_constants.h`)
- AT-200ProIIv2 (via `pic_family.h` FAMILY_K42, `timer_constants.h`)

## Datasheet

DS40001919G, 841 pages. Full extraction in `datasheets/pic18f26k42/extracted/`.

## Errata

DS80000773 (Rev H, 10/2023). Current silicon: A3. Key issues:
- SMBus 3.0 VIL temp/VDD dependent (all revs)
- VDD min spec changed — F devices need ≥3.0V at some conditions (A3)
- FVR accuracy degraded below -20°C (all revs)
- DMA reads from EEPROM don't work (A1); DMA in Doze may fail (A1)
- ADC2: FOSC clock mode fails above 40 MHz (A1); double-sample burst average broken (A1); extra acquisition inserted between double-sample conversions (all revs)
- UART: BRGS non-functional in DALI (A3); stop-bit interrupt unavailable (A1); first char after auto-baud may be corrupted (all revs)
- I2C: RX buffer latched on wrong clock edge (all revs); spurious Start/Stop flags on enable (all revs)
- NVM: WRERR bit cannot be hardware-cleared after first set (A1)
- WWDT: window violation in Doze mode (A1)
- Low-Power Sleep: F devices reset on wake at 3.1V < VDD < 3.3V (A1)
- PFM endurance only 1K cycles (all revs)
- MOVFF/MOVSF corrupts destination when BSR=0x3F (all revs)
- Software breakpoints unavailable (all revs)
- FSR shadow registers not writable (all revs)

Full details in `datasheets/pic18f26k42/extracted-errata/errata.md`.

## Register Database

792 registers parsed from XC8 header → `datasheets/pic18f26k42/registers.json`
Lode register reference → `lode/datasheets/pic18f26k42/registers.md`

## Key Differences from Q41

| Feature | K42 | Q41 |
|---------|-----|------|
| UART | 2 (1 with DMX/DALI/LIN) | 3 (all with DMX/DALI/LIN) |
| SPI | 1 | 2 (with FIFOs) |
| I2C | 2 | 1 |
| CCP/PWM | 4/4 | 1/3 |
| CWG | 3 | 1 |
| DMA channels | 2 | 4 |
| DAC | 1 (5-bit) | 2 (8-bit, one no pin) |
| OPA | — | 1 |
| ADC channels (ext) | up to 43 | up to 24 |
| Instructions | 87 | — |
| Flash max | 128KB | 64KB |
| RAM max | 8KB | 4KB |
| EEPROM max | 1KB | 512B |