# PIC18F16Q41 I/O Ports

## Register Address Map

| Reg | PORTA | PORTB | PORTC |
|-----|-------|-------|-------|
| PORTx | 0x04CE | 0x04CF | 0x04D0 |
| LATx | 0x04BE | 0x04BF | 0x04C0 |
| TRISx | 0x04C6 | 0x04C7 | 0x04C8 |
| ANSELx | 0x0400 | 0x0408 | 0x0410 |
| WPUx | 0x0401 | 0x0409 | 0x0411 |
| ODCONx | 0x0402 | 0x040A | 0x0412 |
| SLRCONx | 0x0403 | 0x040B | 0x0413 |
| INLVLx | 0x0404 | 0x040C | 0x0414 |

## Pin Availability

- **PORTA**: RA0-RA5 (RA3 = MCLR/VPP, input-only if MCLRE=0)
- **PORTB**: RB4-RB7 (20-pin devices); RB4-RB7 on 14-pin
- **PORTC**: RC0-RC7 (20-pin devices); RC0-RC5 on 14-pin

## TRISx — Direction (Reset = 0x3F/0xF0/0xFF)

| Bit | 1 | 0 |
|-----|---|---|
| | Input (tri-stated) | Output (driver enabled) |

All TRIS bits default to **1** (input) on reset. RA3/MCLR TRIS bit is read-only='1'.

## PORTx vs LATx — Read-Modify-Write (RMW) Issue

- **PORTx read**: returns actual pin level; **LATx read**: returns output latch value
- **Both writes** go to the same output latch — functionally equivalent
- **RMW problem**: A bit-set/clear on PORTx reads the *pin*, modifies, writes back. If a previous output change hasn't settled (capacitive load), the stale pin value corrupts the write
- **Rule**: Always use **LATx** for output bit operations (BSF/BCF/|= etc.). Read LATx to get what you wrote; read PORTx to get what's on the pin

## ANSELx — Analog Select (Reset = all 1s = analog)

| Bit | 1 | 0 |
|-----|---|---|
| | Analog input (digital buffer disabled, always reads '0') | Digital I/O |

**All ANSEL bits default to 1 (analog) on reset.** Pins won't work as digital inputs until cleared. This is the #1 gotcha — a pin that "doesn't read" likely has ANSEL still set. ANSEL has no effect on digital/analog *output* — a pin with TRIS=0, ANSEL=1 still drives out, but reads back '0'.

PORTA implemented bits: 0,1,2,4,5 (no bit 3 in ANSELA; RA3 is MCLR-only)
PORTB implemented bits: 4,5,6,7
PORTC implemented bits: 0-7

## WPUx — Weak Pull-Up (Reset = 0x00)

| Bit | 1 | 0 |
|-----|---|---|
| | Pull-up enabled | Pull-up disabled |

Auto-disabled when pin is output (register unchanged). MCLR pull-up is always on when MCLRE=1 or LVP=1 regardless of WPU bit.

## ODCONx — Open-Drain (Reset = 0x00)

| Bit | 1 | 0 |
|-----|---|---|
| | Open-drain (sink only) | Push-pull (source + sink) |

Set ODCON bit before using I2C. Open-drain pins need external pull-up resistor.

## INLVLx — Input Threshold (Reset = all 1s = Schmitt Trigger)

| Bit | 1 | 0 |
|-----|---|---|
| | Schmitt Trigger (ST) | TTL compatible |

Affects PORTx reads and IOC thresholds. Change INLVL only with peripherals disabled to avoid spurious transitions. I2C pins use I2C-specific thresholds when RxyI2C is enabled (RB4, RB6, RC0, RC1).

## SLRCONx — Slew Rate (Reset = all 1s = slew-limited)

| Bit | 1 | 0 |
|-----|---|---|
| | Slew rate limited | Maximum slew rate |

Defaults to slew-limited. Clear for high-speed output edges.

## I2C Pad Registers

| Register | Address | Pins |
|----------|---------|------|
| RB6I2C | 0x0286 | RB6 |
| RB4I2C | 0x0287 | RB4 |
| RC1I2C | 0x0288 | RC1 |
| RC0I2C | 0x0289 | RC0 |

Fields per register: SLEW[7:6] (I2C slew), PU[5:4] (I2C pull-up strength), TH[1:0] (I2C threshold).
I2C pads override SLR/INLVL/WPU when enabled via RxyI2C.

## Key Gotchas

1. **ANSEL defaults analog** — always clear ANSEL before using any pin as digital input or PPS input
2. **Use LATx for writes** — RMW on PORTx reads the pin (not the latch), which can read stale values under load
3. **RA3 is MCLR** — input-only when MCLRE=0; no TRIS/LAT control; reads '1' when MCLR enabled
4. **Slew rate defaults limited** — SLRCONx=1 on reset; clear for fast edges
5. **I2C needs open-drain** — set ODCON bit on I2C SDA/SCL pins
6. **Digital output works with ANSEL=1** — but the pin reads '0' (digital buffer disabled), causing RMW corruption if you PORTx-read
7. **Unimplemented bits read '0'** — e.g. ANSELA bit 3 RA3, PORTA bit 6/7
8. **WPU auto-disabled on output** — check TRIS state, not just WPU register