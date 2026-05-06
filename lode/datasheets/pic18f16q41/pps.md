# PIC18F16Q41 — PPS (Peripheral Pin Select)

## Overview

PPS allows remapping digital peripheral inputs/outputs to any I/O pin. Analog
functions are fixed and cannot be rerouted. Input and output selections are
independent.

## PPS Output Selection (RxyPPS values)

Write the value to the pin's RxyPPS register to route a peripheral output to
that pin. Multiple pins can share the same output source.

| Value | Source          | | Value | Source          |
|-------|-----------------| |-------|-----------------|
| 0x00  | LATxy (port latch) | 0x14 | UART2 TXDE      |
| 0x01  | CLC1OUT         | | 0x15 | UART2 RTS       |
| 0x02  | CLC2OUT         | | 0x16 | UART3 TX        |
| 0x03  | CLC3OUT         | | 0x17 | UART3 TXDE      |
| 0x04  | CLC4OUT         | | 0x18 | UART3 RTS       |
| 0x05  | CWG1A           | | 0x19 | C1OUT           |
| 0x06  | CWG1B           | | 0x1A | C2OUT           |
| 0x07  | CWG1C           | | 0x1B | SPI1 SCK        |
| 0x08  | CWG1D           | | 0x1C | SPI1 SDO         |
| 0x09  | CCP1            | | 0x1D | SPI1 SS          |
| 0x0A  | PWM1S1P1_OUT    | | 0x1E | SPI2 SCK         |
| 0x0B  | PWM1S1P2_OUT    | | 0x1F | SPI2 SDO         |
| 0x0C  | PWM2S1P1_OUT    | | 0x20 | SPI2 SS          |
| 0x0D  | PWM2S1P2_OUT    | | 0x21 | I2C1 SCL*        |
| 0x0E  | PWM3S1P1_OUT    | | 0x22 | I2C1 SDA*        |
| 0x0F  | PWM3S1P2_OUT    | | 0x23 | TMR0             |
| 0x10  | UART1 TX        | | 0x24 | NCO1             |
| 0x11  | UART1 TXDE      | | 0x25 | CLKR             |
| 0x12  | UART1 RTS       | | 0x26 | DSM1             |
| 0x13  | UART2 TX        | | 0x27 | ADGRDA           |
|       |                 | | 0x28 | ADGRDB           |

\* I2C SCL/SDA are bidirectional — input PPS must select the same pin.

## PPS Input Selection (xxxPPS registers)

Each peripheral has a dedicated input register. Value encoding: bits [5:3] =
PORT, bits [2:0] = PIN.

| PORT[2:0] | Port | | PIN[2:0] | Pin |
|-----------|------| |----------|-----|
| 000       | A    | | 000      | Rx0 |
| 001       | B    | | 001      | Rx1 |
| 010       | C    | | 010      | Rx2 |
|           |      | | 011      | Rx3 |
|           |      | | 100      | Rx4 |
|           |      | | 101      | Rx5 |
|           |      | | 110      | Rx6 |
|           |      | | 111      | Rx7 |

Available input ports: A, C (14-pin) / A, B, C (20-pin).

### Input Registers (address | register | 20-pin default)

| Addr   | Register     | Default Pin |
|--------|--------------|-------------|
| 0x023E | INT0PPS      | RC0         |
| 0x023F | INT1PPS      | RC1         |
| 0x0240 | INT2PPS      | RC2         |
| 0x0241 | T0CKIPPS     | RC5         |
| 0x0242 | T1CKIPPS     | RC6         |
| 0x0243 | T1GPPS       | RA4         |
| 0x0244 | T3CKIPPS     | RC5         |
| 0x0245 | T3GPPS       | RC4         |
| 0x0248 | T2INPPS      | RA5         |
| 0x0249 | T4INPPS      | RC1         |
| 0x024F | CCP1PPS      | RC5         |
| 0x0251 | PWM1ERSPPS   | RA5         |
| 0x0252 | PWM2ERSPPS   | RC1         |
| 0x0253 | PWM3ERSPPS   | RC2         |
| 0x0257 | PWMIN0PPS    | RC5         |
| 0x0258 | PWMIN1PPS    | RC3         |
| 0x0259 | SMT1WINPPS   | RA5         |
| 0x025A | SMT1SIGPPS   | RA4         |
| 0x025B | CWG1PPS      | RA2         |
| 0x025E | MD1CARLPPS   | RC2         |
| 0x025F | MD1CARHPPS   | RC5         |
| 0x0260 | MD1SRCPPS    | RA1         |
| 0x0261 | CLCIN0PPS    | RA2         |
| 0x0262 | CLCIN1PPS    | RC3         |
| 0x0263 | CLCIN2PPS    | RB4         |
| 0x0264 | CLCIN3PPS    | RB5         |
| 0x0269 | ADACTPPS     | RC2         |
| 0x026A | SPI1SCKPPS   | RB6         |
| 0x026B | SPI1SDIPPS   | RB4         |
| 0x026C | SPI1SSPPS    | RC6         |
| 0x026D | SPI2SCKPPS   | RB7         |
| 0x026E | SPI2SDIPPS   | RB5         |
| 0x026F | SPI2SSPPS    | RA1         |
| 0x0270 | I2C1SDAPPS*  | RB4         |
| 0x0271 | I2C1SCLPPS*  | RB6         |
| 0x0272 | U1RXPPS      | RB5         |
| 0x0273 | U1CTSPPS     | RB7         |
| 0x0274 | U2RXPPS      | RC1         |
| 0x0275 | U2CTSPPS     | RC2         |
| 0x0276 | U3RXPPS      | RC3         |
| 0x0277 | U3CTSPPS     | RC5         |

\* Bidirectional — output must select same pin.

## Output Pin Registers (RxyPPS addresses)

| Addr   | Register | | Addr   | Register |
|--------|----------| |--------|----------|
| 0x0201 | RA0PPS   | | 0x0211 | RC0PPS   |
| 0x0202 | RA1PPS   | | 0x0212 | RC1PPS   |
| 0x0203 | RA2PPS   | | 0x0213 | RC2PPS   |
| 0x0205 | RA4PPS   | | 0x0214 | RC3PPS   |
| 0x0206 | RA5PPS   | | 0x0215 | RC4PPS   |
| 0x020D | RB4PPS   | | 0x0216 | RC5PPS   |
| 0x020E | RB5PPS   | | 0x0217 | RC6PPS   |
| 0x020F | RB6PPS   | | 0x0218 | RC7PPS   |
| 0x0210 | RB7PPS   | |        |          |

## Lock Register

| Addr   | Register | Bit 0       |
|--------|----------|-------------|
| 0x0200 | PPSLOCK  | PPSLOCKED   |

PPSLOCKED=0 → PPS unlocked (writable). PPSLOCKED=1 → PPS locked (writes
ignored). Cleared on all resets.

## Constraints & Rules

- **Lock/unlock sequence**: Disable interrupts, then write 0x55→PPSLOCK,
  0xAA→PPSLOCK, then set/clear PPSLOCKED bit, then re-enable interrupts.
- **PPS1WAY config bit**: When set, PPSLOCKED can only be set once per reset.
  Once locked, cannot be unlocked until next reset.
- **Bidirectional pins**: I2C SCL/SDA input and output PPS must select the same
  pin. I2C-default pins RB4/RB6 are I2C/SMBus-compatible; other pins operate
  at TTL/ST levels only.
- **ANSEL**: Must clear ANSEL bit for any pin used as a digital PPS input.
- **Output TRIS**: Port TRIS retains control; peripherals that need to drive
  the pin (e.g. I2C) override TRIS automatically.
- **POR defaults**: All input registers get their default pin selection. All
  output registers reset to 0 (LATxy). Non-POR resets preserve PPS settings.
- **Sleep**: PPS selections are unaffected by Sleep.
- **PPS-capable pins**: All digital I/O pins on available ports (14-pin: A,C;
  20-pin: A,B,C). RA3 (MCLR only) and RA4 (input-only on 14-pin) have no
  output PPS register.

## Cross-Check with pps_values.h (FAMILY_Q41 block)

The Q41 output values in `MC-200/src/peripherals/src/pps_values.h` lines 214-254
match the datasheet Table 21-2 exactly:

- 0x28 ADGRDB ✓ | 0x27 ADGRDA ✓ | 0x26 DSM1 ✓ | 0x25 CLKR ✓
- 0x24 NCO1 ✓ | 0x23 TMR0 ✓ | 0x22 I2C1_SDA ✓ | 0x21 I2C1_SCL ✓
- 0x20 SPI2_SS ✓ | 0x1F SPI2_SDO ✓ | 0x1E SPI2_SCK ✓
- 0x1D SPI1_SS ✓ | 0x1C SPI1_SDO ✓ | 0x1B SPI1_SCK ✓
- 0x1A C2OUT ✓ | 0x19 C1OUT ✓
- 0x18–0x10 UART3/2/1 (TX/RTS/TXDE) ✓
- 0x0F–0x0A PWM outputs ✓ | 0x09 CCP1 ✓ | 0x08–0x05 CWG1 ✓
- 0x04–0x01 CLC4–1 ✓ | 0x00 LATxy ✓

All Q41 output values verified consistent with datasheet. No discrepancies found.