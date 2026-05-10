# PIC18F26K42 Family I/O Ports

## Port Availability by Package

| Device | 28-pin | 40/44/48-pin | Ports |
|--------|--------|--------------|-------|
| PIC18(L)F26K42 | Yes | — | A, B, C, E(RE3 only) |
| PIC18(L)F27K42 | Yes | — | A, B, C, E(RE3 only) |
| PIC18(L)F45K42 | — | Yes | A, B, C, D, E(RE0-RE3) |
| PIC18(L)F46K42 | — | Yes | A, B, C, D, E(RE0-RE3) |
| PIC18(L)F47K42 | — | Yes | A, B, C, D, E(RE0-RE3) |
| PIC18(L)F55K42 | — | Yes (48-pin) | A, B, C, D, E(RE0-RE3), F |
| PIC18(L)F56K42 | — | Yes (48-pin) | A, B, C, D, E(RE0-RE3), F |
| PIC18(L)F57K42 | — | Yes (48-pin) | A, B, C, D, E(RE0-RE3), F |

**28-pin** (26K42/27K42): PORTD and PORTE[2:0] unimplemented. PORTF unimplemented.
**40/44/48-pin** (45/46/47K42): PORTF unimplemented.

## Register Summary

| Reg | PORTA | PORTB | PORTC | PORTD | PORTE | PORTF |
|-----|-------|-------|-------|-------|-------|-------|
| PORTx | RA[7:0] | RB[7:0] | RC[7:0] | RD[7:0]¹ | —[7:4] RE3² RE[2:0]¹ | RF[7:0]³ |
| LATx | LA[7:0]A | LA[7:0]B | LA[7:0]C | LD[7:0]¹ | —[7:3] LA[2:0]E¹ | LF[7:0]³ |
| TRISx | TRISA[7:0] | TRISB[7:0] | TRISC[7:0] | TRISD[7:0]¹ | —[7:3] TRI[2:0]E¹ | TRISF[7:0]³ |
| ANSELx | ANSELA[7:0] | ANSELB[7:0] | ANSELC[7:0] | ANSELD[7:0]¹ | —[7:3] — ANSE[2:0]E¹ | ANSELF[7:0]³ |
| WPUx | WPUA[7:0] | WPUB[7:0] | WPUC[7:0] | WPUD[7:0]¹ | —[7:4] WPUE3⁴ WPUE[2:0]¹ | WPUF[7:0]³ |
| ODCONx | ODCA[7:0] | ODCB[7:0] | ODCC[7:0] | ODCD[7:0]¹ | —[7:3] — OD[2:0]CE¹ | ODCF[7:0]³ |
| SLRCONx | SLRA[7:0] | SLRB[7:0] | SLRC[7:0] | SLRD[7:0]¹ | —[7:3] — SL[2:0]RE¹ | SLRF[7:0]³ |
| INLVLx | INLVLA[7:0] | INLVLB[7:0]⁵ | INLVLC[7:0]⁵ | INLVLD[7:0]¹⁵ | —[7:4] INLVLE3 —[2:0] | INLVLF[7:0]³ |

¹ Unimplemented in 28-pin (26K42/27K42). ² RE3 is read-only in PORT, no TRIS/LAT. ³ Unimplemented in 26/27/45/46/47K42. ⁴ WPUE3: if MCLRE=1, pull-up always on regardless of bit. ⁵ I2C pins override with RxyI2C thresholds when enabled.

## TRISx — Direction (Reset = all 1s = input)

| Bit | 1 | 0 |
|-----|---|---|
| | Input (tri-stated) | Output (driver enabled) |

All TRIS bits default to **1** (input) on reset. RB6/RB7 read '1' in Debug mode. RE3 has no TRIS bit (always input).

## PORTx vs LATx — RMW

- **PORTx read**: actual pin level. **LATx read**: output latch value
- **Both writes** target the same output latch — functionally equivalent
- **RMW problem**: bit-set/clear on PORTx reads the pin; stale values corrupt the write under load
- **Rule**: Always use **LATx** for output bit operations

## ANSELx — Analog Select (Reset = all 1s = analog)

| Bit | 1 | 0 |
|-----|---|---|
| | Analog input (digital buffer disabled, reads '0') | Digital I/O |

All ANSEL bits default to **1 (analog)** on reset. Clear before using as digital input or PPS input. ANSEL has no effect on output — TRIS=0 + ANSEL=1 still drives out, but PORTx reads '0'. This causes RMW corruption if you read PORTx on an analog-configured output pin.

 PORTE (40+ pin): ANSELE has bits [2:0] only. RE0-RE2 default analog on POR. RE3 has no ANSEL bit.

## WPUx — Weak Pull-Up (Reset = 0x00)

| Bit | 1 | 0 |
|-----|---|---|
| | Pull-up enabled | Pull-up disabled |

WPUE3 controls RE3 pull-up. If MCLRE=1 or LVP=1, RE3 pull-up is always enabled and WPUE3 is ignored. WPU is auto-disabled when pin is configured as output.

## ODCONx — Open-Drain (Reset = 0x00)

| Bit | 1 | 0 |
|-----|---|---|
| | Open-drain (sink only) | Push-pull (source + sink) |

Set ODCON bit on I2C SDA/SCL pins before enabling I2C. Open-drain pins require external pull-up.

## SLRCONx — Slew Rate (Reset = all 1s = slew-limited)

| Bit | 1 | 0 |
|-----|---|---|
| | Slew rate limited | Maximum slew rate |

Defaults to limited. Clear for fast output edges.

## INLVLx — Input Threshold (Reset = all 1s = Schmitt Trigger)

| Bit | 1 | 0 |
|-----|---|---|
| | Schmitt Trigger (ST) | TTL compatible |

Affects PORTx reads and IOC edge detection. Change only with peripherals disabled. I2C pad registers (RxyI2C) override INLVL on I2C pins when enabled.

INLVLE: only bit 3 (INLVLE3) is implemented on all devices. Bits [2:0] on 40+ pin only.

I2C pins with RxyI2C override: RB1, RB2, RC3, RC4 always; RD0, RD1 on 40+ pin only.

## Port-Specific Notes

### PORTE (28-pin)
PORTE is **RE3 only**, input-only. Available only when MCLRE=0 (otherwise RE3 is MCLR). No TRISE/LATE registers for RE3. PORT register bit 3 is read-only; reads '1' when MCLRE=1.

### PORTE (40/44/48-pin)
RE0-RE2 are bidirectional I/O with full register set (TRISE[2:0], LATE[2:0], ANSELE[2:0], etc.). RE3 remains input-only as above. POR defaults: RE[2:0] = analog inputs.

### RE3 Special Cases
- Input-only: no TRIS or LAT bits
- Dual function: MCLR/VPP when MCLRE=1, or digital input when MCLRE=0
- Also serves as programming voltage (VPP) input regardless of MCLRE
- IOC available when MCLRE=0 and LVP=0
- WPUE3 pull-up always on when MCLRE=1 or LVP=1

### PORTB
RB6 and RB7 read '1' in Debug mode (ICSP/ICD pins).

### PORTF
Only on 55/56/57K42 (48-pin packages). Full 8-bit port with all control registers.

### I2C Pad Control (RxyI2C)

| Register | Pin | Available |
|----------|-----|-----------|
| RB1I2C | RB1 | All devices |
| RB2I2C | RB2 | All devices |
| RC3I2C | RC3 | All devices |
| RC4I2C | RC4 | All devices |
| RD0I2C | RD0 | 40+ pin only |
| RD1I2C | RD1 | 40+ pin only |

Register fields: SLEW (bit 6) — I2C slew rate limiting; PU[1:0] (bits 5:4) — I2C pull-up strength (00=standard GPIO, 01=2x, 10=10x, 11=reserved); TH[1:0] (bits 1:0) — I2C threshold (00=GPIO INLVL, 01=I2C, 10=SMBus 2.0, 11=SMBus 3.0). I2C pad settings override SLRCON/INLVL/WPU when enabled.

## IOC — Interrupt-on-Change

Available on **PORTA, PORTB, PORTC** (all pins), and **RE3** (PORTE). Not on PORTD or PORTF.

| Reg | PORTA | PORTB | PORTC | PORTE |
|-----|-------|-------|-------|-------|
| IOCxF (flags) | IOCAF[7:0] | IOCBF[7:0] | IOCCF[7:0] | IOCEF bit 3 only |
| IOCxP (rising) | IOCAP[7:0] | IOCBP[7:0] | IOCCP[7:0] | IOCEP bit 3 only |
| IOCxN (falling) | IOCAN[7:0] | IOCBN[7:0] | IOCCN[7:0] | IOCEN bit 3 only |

IOCIE (PIEx) must be set to generate interrupts. Flags (IOCxF) are hardware-set on edge detection; clear by writing 0 (use AND-mask on changed bits only). IOC wakes from Sleep if IOCIE=1. RE3 IOC unavailable when MCLRE=1 or LVP=1.

## Pin Availability by Port (28-pin vs 40/44/48-pin)

| Port | 28-pin (26/27K42) | 40/44/48-pin (45/46/47/55/56/57K42) |
|------|-------------------|--------------------------------------|
| A | RA0-RA7 | RA0-RA7 |
| B | RB0-RB7 | RB0-RB7 |
| C | RC0-RC7 | RC0-RC7 |
| D | — | RD0-RD7 |
| E | RE3 only (input) | RE0-RE2 (bidirectional), RE3 (input-only) |
| F | — | RF0-RF7 (55/56/57K42 only) |

## Key Gotchas

1. **ANSEL defaults analog** — clear ANSEL before using any pin as digital input or PPS input
2. **Use LATx for writes** — PORTx RMW reads pin level (stale under load)
3. **RE3 is input-only** — no TRIS/LAT; reads '1' when MCLR enabled (MCLRE=1)
4. **Slew rate defaults limited** — SLRCONx=1 on reset; clear for fast edges
5. **I2C needs open-drain** — set ODCON bit on I2C SDA/SCL pins
6. **Digital output works with ANSEL=1** — but PORTx reads '0', causing RMW corruption
7. **Unimplemented bits read '0'** — e.g. PORTE bits 7:4, TRISE bits 7:3
8. **RE3 pull-up** — always on when MCLRE=1 or LVP=1; WPUE3 is ignored
9. **RB6/RB7** — read '1' in Debug mode (ICSP/ICD pins)
10. **INLVL change** — may cause spurious IOC if changed while peripheral active