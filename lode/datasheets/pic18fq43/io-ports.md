# PIC18F27/47/57Q43 Family I/O Ports

## Port Availability by Package

| Device | 28-pin | 40/44-pin | 48-pin | Ports |
|--------|--------|-----------|--------|-------|
| PIC18F25Q43 | Yes | — | — | A, B, C, E(3) |
| PIC18F26Q43 | Yes | — | — | A, B, C, E(3) |
| PIC18F27Q43 | Yes | — | — | A, B, C, E(3) |
| PIC18F45Q43 | — | Yes | — | A, B, C, D, E |
| PIC18F46Q43 | — | Yes | — | A, B, C, D, E |
| PIC18F47Q43 | — | Yes | — | A, B, C, D, E |
| PIC18F55Q43 | — | — | Yes | A, B, C, D, E, F |
| PIC18F56Q43 | — | — | Yes | A, B, C, D, E, F |
| PIC18F57Q43 | — | — | Yes | A, B, C, D, E, F |

**28-pin**: PORTD and PORTE[2:0] unimplemented. PORTF unimplemented.
**40/44-pin**: PORTF unimplemented.
**48-pin**: All ports available.

## Register Summary by Port

| Reg | PORTA | PORTB | PORTC | PORTD | PORTE | PORTF |
|-----|-------|-------|-------|-------|-------|-------|
| PORTx | RA[7:0] | RB[7:0] | RC[7:0] | RD[7:0]¹ | RE3² + RE[2:0]¹ | RF[7:0]³ |
| LATx | LATA[7:0] | LATB[7:0] | LATC[7:0] | LATD[7:0]¹ | LATE2:0¹ + — | LATF[7:0]³ |
| TRISx | TRISA[7:0] | TRISB[7:0] | TRISC[7:0] | TRISD[7:0]¹ | TRISE[2:0]¹ + —³ | TRISF[7:0]³ |
| ANSELx | ANSELA[7:0]² | ANSELB[7:0] | ANSELC[7:0] | ANSELD[7:0]¹ | ANSELE[2:0]¹ | ANSELF[7:0]³ |
| WPUx | WPUA[7:0] | WPUB[7:0] | WPUC[7:0] | WPUD[7:0]¹ | WPU E3⁴ + E[2:0]¹ | WPUF[7:0]³ |
| ODCONx | ODCA[7:0] | ODCB[7:0] | ODCC[7:0] | ODCD[7:0]¹ | ODCE[2:0]¹ | ODCF[7:0]³ |
| SLRCONx | SLRA[7:0] | SLRB[7:0] | SLRC[7:0] | SLRD[7:0]¹ | SLRE[2:0]¹ | SLRF[7:0]³ |
| INLVLx | INLVLA[7:0] | INLVLB[7:0] | INLVLC[7:0] | INLVLD[7:0]¹ | INLVLE[3:0] | INLVLF[7:0]³ |

¹ Unimplemented in 28-pin devices. ² RA0–RA7; all default analog. ³ Unimplemented in 28/40/44-pin devices. ⁴ WPUE3: if MCLRE=1 or LVP=1, pull-up always on.

## Register Addresses

| Address | Name | Bits [7:0] |
|---------|------|------------|
| 0x0286 | RC4I2C | SLEW[1:0], PU[1:0], —, —, —, —, TH[1:0] |
| 0x0287 | RC3I2C | SLEW[1:0], PU[1:0], —, —, —, —, TH[1:0] |
| 0x0288 | RB2I2C | SLEW[1:0], PU[1:0], —, —, —, —, TH[1:0] |
| 0x0289 | RB1I2C | SLEW[1:0], PU[1:0], —, —, —, —, TH[1:0] |
| 0x0400 | ANSELA | ANSELA[7:0] |
| 0x0401 | WPUA | WPUA[7:0] |
| 0x0402 | ODCONA | ODCA[7:0] |
| 0x0403 | SLRCONA | SLRA[7:0] |
| 0x0404 | INLVLA | INLVLA[7:0] |
| 0x0408 | ANSELB | ANSELB[7:0] |
| 0x0409 | WPUB | WPUB[7:0] |
| 0x040A | ODCONB | ODCB[7:0] |
| 0x040B | SLRCONB | SLRB[7:0] |
| 0x040C | INLVLB | INLVLB[7:0] |
| 0x0410 | ANSELC | ANSELC[7:0] |
| 0x0411 | WPUC | WPUC[7:0] |
| 0x0412 | ODCONC | ODCC[7:0] |
| 0x0413 | SLRCONC | SLRC[7:0] |
| 0x0414 | INLVLC | INLVLC[7:0] |
| 0x0418 | ANSELD | ANSELD[7:0] |
| 0x0419 | WPUD | WPUD[7:0] |
| 0x041A | ODCOND | ODCD[7:0] |
| 0x041B | SLRCOND | SLRD[7:0] |
| 0x041C | INLVLD | INLVLD[7:0] |
| 0x0420 | ANSELE | —, —, —, —, —, ANSELE2, ANSELE1, ANSELE0 |
| 0x0421 | WPUE | —, —, —, —, WPUE3, WPUE2, WPUE1, WPUE0 |
| 0x0422 | ODCONE | —, —, —, —, —, ODCE2, ODCE1, ODCE0 |
| 0x0423 | SLRCONE | —, —, —, —, —, SLRE2, SLRE1, SLRE0 |
| 0x0424 | INLVLE | —, —, —, —, INLVLE3, INLVLE2, INLVLE1, INLVLE0 |
| 0x0428 | ANSELF | ANSELF[7:0] |
| 0x0429 | WPUF | WPUF[7:0] |
| 0x042A | ODCONF | ODCF[7:0] |
| 0x042B | SLRCONF | SLRF[7:0] |
| 0x042C | INLVLF | INLVLF[7:0] |
| 0x04BE | LATA | LATA[7:0] |
| 0x04BF | LATB | LATB[7:0] |
| 0x04C0 | LATC | LATC[7:0] |
| 0x04C1 | LATD | LATD[7:0]¹ |
| 0x04C2 | LATE | —, —, —, —, —, LATE2, LATE1, LATE0 |
| 0x04C3 | LATF | LATF[7:0]³ |
| 0x04C6 | TRISA | TRISA[7:0] |
| 0x04C7 | TRISB | TRISB[7:0] |
| 0x04C8 | TRISC | TRISC[7:0] |
| 0x04C9 | TRISD | TRISD[7:0]¹ |
| 0x04CA | TRISE | —, —, —, —, —, TRISE2, TRISE1, TRISE0 |
| 0x04CB | TRISF | TRISF[7:0]³ |
| 0x04CE | PORTA | RA[7:0] |
| 0x04CF | PORTB | RB[7:0] |
| 0x04D0 | PORTC | RC[7:0] |
| 0x04D1 | PORTD | RD[7:0]¹ |
| 0x04D2 | PORTE | —, —, —, —, RE3, RE2, RE1, RE0 |
| 0x04D3 | PORTF | RF[7:0]³ |

## TRISx — Direction (Reset = all 1s = input)

| Bit | 1 | 0 |
|-----|---|---|
| | Input (tri-stated) | Output (driver enabled) |

RE3 has no TRIS bit (always input). RB6/RB7 read '1' in Debug mode.

## PORTx vs LATx

- **PORTx read**: actual pin level. **LATx read**: output latch value
- **Both writes** target the same output latch
- **RMW problem**: bit-set/clear on PORTx reads pin level; stale values corrupt under load
- **Rule**: Always use **LATx** for output bit operations

## ANSELx — Analog Select (Reset = all 1s = analog)

| Bit | 1 | 0 |
|-----|---|---|
| | Analog input (digital buffer disabled, reads '0') | Digital I/O |

Clear ANSEL before using as digital input or PPS input. ANSEL=1 + TRIS=0 still drives output, but PORTx reads '0'.

## WPUx — Weak Pull-Up (Reset = 0x00)

| Bit | 1 | 0 |
|-----|---|---|
| | Pull-up enabled | Pull-up disabled |

WPUE3: if MCLRE=1 or LVP=1, pull-up is always on regardless of bit. WPU auto-disabled when pin is output.

## ODCONx — Open-Drain (Reset = 0x00)

| Bit | 1 | 0 |
|-----|---|---|
| | Open-drain (sink only) | Push-pull (source + sink) |

Set ODCON bit on I2C SDA/SCL pins before enabling I2C.

## SLRCONx — Slew Rate (Reset = all 1s = slew-limited)

| Bit | 1 | 0 |
|-----|---|---|
| | Slew rate limited | Maximum slew rate |

Defaults to limited. Clear for fast output edges.

## INLVLx — Input Threshold (Reset = all 1s = Schmitt Trigger)

| Bit | 1 | 0 |
|-----|---|---|
| | Schmitt Trigger (ST) | TTL compatible |

Affects PORTx reads and IOC edge detection. Change only with peripherals disabled.

## I2C Pad Control (RxyI2C)

Available on RB1, RB2, RC3, RC4 pins.

| Register | Pin |
|----------|-----|
| RB1I2C (0x0289) | RB1 |
| RB2I2C (0x0288) | RB2 |
| RC3I2C (0x0287) | RC3 |
| RC4I2C (0x0286) | RC4 |

**RxyI2C fields:**

| Bits | Field | Description |
|------|-------|-------------|
| 7:6 | SLEW[1:0] | I2C slew rate: 00=standard GPIO (per SLRCON), 01=400 kHz, 10=Reserved, 11=1 MHz |
| 5:4 | PU[1:0] | Pull-up: 00=standard GPIO (per WPU), 01=2x, 10=10x (or 5x if FME=10), 11=20x (if FME) or Reserved |
| 1:0 | TH[1:0] | Input threshold: 00=standard GPIO (per INLVL), 01=I2C-specific, 10=SMBus 2.0 (2.1V), 11=SMBus 3.0 (1.35V) |

I2C pad settings override SLRCON/INLVL/WPU when enabled via RxyI2C.

## IOC — Interrupt-on-Change

Available on **PORTA, PORTB, PORTC** (all pins), and **RE3** (PORTE).

| Reg | Addr | PORTA | PORTB | PORTC | PORTE |
|-----|------|-------|-------|-------|-------|
| IOCxF (flags) | — | IOCAF[7:0] | IOCBF[7:0] | IOCCF[7:0] | IOCEF bit 3 |
| IOCxP (rising) | — | IOCAP[7:0] | IOCBP[7:0] | IOCCP[7:0] | IOCEP bit 3 |
| IOCxN (falling) | — | IOCAN[7:0] | IOCBN[7:0] | IOCCN[7:0] | IOCEN bit 3 |

| Address | Name |
|---------|------|
| 0x0405 | IOCAP |
| 0x0406 | IOCAN |
| 0x0407 | IOCAF |
| 0x040D | IOCBP |
| 0x040E | IOCBN |
| 0x040F | IOCBF |
| 0x0415 | IOCCP |
| 0x0416 | IOCCN |
| 0x0417 | IOCCF |
| 0x0425 | IOCEP |
| 0x0426 | IOCEN |
| 0x0427 | IOCEF |

IOCxF flags are hardware-set on edge detection; clear by writing 0 (use AND-mask on changed bits only). IOC wakes from Sleep if IOCIE=1. RE3 IOC unavailable when MCLRE=1 or LVP=1.

## RE3 / MCLR Special Cases

- Input-only: no TRIS or LAT bits
- Dual function: MCLR/VPP when MCLRE=1, or digital input when MCLRE=0 (and LVP=0)
- Also serves as VPP during programming
- IOC available when MCLRE=0 and LVP=0
- WPUE3 pull-up always on when MCLRE=1 or LVP=1

## Key Gotchas

1. **ANSEL defaults analog** — clear ANSEL before using any pin as digital input or PPS input
2. **Use LATx for writes** — PORTx RMW reads pin level (stale under load)
3. **RE3 is input-only** — no TRIS/LAT; reads '1' when MCLR enabled
4. **Slew rate defaults limited** — SLRCONx=1 on reset; clear for fast edges
5. **I2C needs open-drain** — set ODCON bit on I2C SDA/SCL pins
6. **Digital output works with ANSEL=1** — but PORTx reads '0', causing RMW corruption
7. **Unimplemented bits read '0'**
8. **INLVL change** — may cause spurious IOC if changed while peripheral active