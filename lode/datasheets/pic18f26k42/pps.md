# PIC18F26K42 — PPS (Peripheral Pin Select)

## Overview

PPS remaps digital peripheral inputs/outputs to any I/O pin. Analog functions
are fixed. Input and output selections are independent.

## PPS Output Selection (RxyPPS values)

Write the value to a pin's RxyPPS register to route a peripheral output to that
pin. Multiple pins can share the same output source.

| Value  | Source         | | Value  | Source         |
|--------|----------------| |--------|----------------|
| 0x00   | LATxy          | | 0x1C   | C1OUT          |
| 0x01   | CLC1OUT        | | 0x1D   | C2OUT          |
| 0x02   | CLC2OUT        | | 0x1E   | SPI1 SCK       |
| 0x03   | CLC3OUT        | | 0x1F   | SPI1 SDO       |
| 0x04   | CLC4OUT        | | 0x20   | SPI1 SS        |
| 0x05   | CWG1A          | | 0x21   | I2C1 SCL*      |
| 0x06   | CWG1B          | | 0x22   | I2C1 SDA*      |
| 0x07   | CWG1C          | | 0x23   | I2C2 SCL*      |
| 0x08   | CWG1D          | | 0x24   | I2C2 SDA*      |
| 0x09   | CCP1           | | 0x25   | TMR0           |
| 0x0A   | CCP2           | | 0x26   | NCO1           |
| 0x0B   | CCP3           | | 0x27   | CLKR           |
| 0x0C   | CCP4           | | 0x28   | DSM1           |
| 0x0D   | PWM5           | | 0x29   | CWG2A          |
| 0x0E   | PWM6           | | 0x2A   | CWG2B          |
| 0x0F   | PWM7           | | 0x2B   | CWG2C          |
| 0x10   | PWM8           | | 0x2C   | CWG2D          |
| 0x13   | UART1 TX       | | 0x2D   | CWG3A          |
| 0x14   | UART1 TXDE     | | 0x2E   | CWG3B          |
| 0x15   | UART1 RTS      | | 0x2F   | CWG3C          |
| 0x16   | UART2 TX       | | 0x30   | CWG3D          |
| 0x17   | UART2 TXDE     | | 0x31   | ADGRDA         |
| 0x18   | UART2 RTS      | | 0x32   | ADGRDB         |
|        |                | |        |                |

Values 0x11–0x12, 0x19–0x1B, 0x33–0x3F: Reserved. * Bidirectional.

## PPS Input Selection (xxxPPS registers)

Each peripheral has a dedicated input register. Value encoding: bits [5:3] =
PORT, bits [2:0] = PIN.

| PORT[2:0] | Port | | PIN[2:0] | Pin |
|-----------|------| |----------|----|
| 000       | A    | | 000      | Rx0 |
| 001       | B    | | 001      | Rx1 |
| 010       | C    | | 010      | Rx2 |
|           |      | | 011      | Rx3 |
|           |      | | 100      | Rx4 |
|           |      | | 101      | Rx5 |
|           |      | | 110      | Rx6 |
|           |      | | 111      | Rx7 |

28-pin (PIC18F26K42): Ports A, B, C available. Values 0x00–0x27.
Larger packages add ports D, E, F (PORT[2:0] = 011, 100, 101).

### Input Registers and POR Defaults (28-pin)

| Register     | Default Pin | Register     | Default Pin |
|--------------|-------------|--------------|-------------|
| INT0PPS      | RB0 (0x08)  | CWG3PPS      | RB2 (0x0A)  |
| INT1PPS      | RB1 (0x09)  | MD1CARLPPS   | RA3 (0x03)  |
| INT2PPS      | RB2 (0x0A)  | MD1CARHPPS   | RA4 (0x04)  |
| T0CKIPPS     | RA4 (0x04)  | MD1SRCPPS    | RA5 (0x05)  |
| T1CKIPPS     | RC0 (0x10)  | CLCIN0PPS    | RA0 (0x00)  |
| T1GPPS       | RB5 (0x0D)  | CLCIN1PPS    | RA1 (0x01)  |
| T3CKIPPS     | RC0 (0x10)  | CLCIN2PPS    | RB6 (0x0E)  |
| T3GPPS       | RC0 (0x10)  | CLCIN3PPS    | RB7 (0x0F)  |
| T5CKIPPS     | RC2 (0x12)  | ADACTPPS     | RB4 (0x0C)  |
| T5GPPS       | RB4 (0x0C)  | SPI1SCKPPS   | RC3 (0x13)  |
| T2INPPS      | RC3 (0x13)  | SPI1SDIPPS   | RC4 (0x14)  |
| T4INPPS      | RC5 (0x15)  | SPI1SSPPS    | RA5 (0x05)  |
| T6INPPS      | RB7 (0x0F)  | I2C1SCLPPS*  | RC3 (0x13)  |
| CCP1PPS      | RC2 (0x12)  | I2C1SDAPPS*  | RC4 (0x14)  |
| CCP2PPS      | RC1 (0x11)  | I2C2SCLPPS*  | RB1 (0x09)  |
| CCP3PPS      | RB5 (0x0D)  | I2C2SDAPPS*  | RB2 (0x0A)  |
| CCP4PPS      | RB0 (0x08)  | U1RXPPS      | RC7 (0x17)  |
| SMT1WINPPS   | RC0 (0x10)  | U1CTSPPS     | RC6 (0x16)  |
| SMT1SIGPPS   | RC1 (0x11)  | U2RXPPS      | RB7 (0x0F)  |
| CWG1PPS      | RB0 (0x08)  | U2CTSPPS     | RB6 (0x0E)  |
| CWG2PPS      | RB1 (0x09)  |              |             |

\* Bidirectional — input and output PPS must select the same pin.

## Output Pin Registers (RxyPPS)

28-pin K42 has PPS output registers for all digital I/O pins on ports A, B, C:

| Register  | Pin | Register  | Pin | Register  | Pin |
|-----------|-----|-----------|-----|-----------|-----|
| RA0PPS    | RA0 | RB0PPS    | RB0 | RC0PPS    | RC0 |
| RA1PPS    | RA1 | RB1PPS    | RB1 | RC1PPS    | RC1 |
| RA2PPS    | RA2 | RB2PPS    | RB2 | RC2PPS    | RC2 |
| RA4PPS    | RA4 | RB3PPS    | RB3 | RC3PPS    | RC3 |
| RA5PPS    | RA5 | RB4PPS    | RB4 | RC4PPS    | RC4 |
| RA6PPS    | RA6 | RB5PPS    | RB5 | RC5PPS    | RC5 |
| RA7PPS    | RA7 | RB6PPS    | RB6 | RC6PPS    | RC6 |
|           |     | RB7PPS    | RB7 | RC7PPS    | RC7 |

Note: RA3 is input-only (MCLR/VPP) on 28-pin; no RA3PPS output register.

## Lock Register

PPSLOCK (bit 0 = PPSLOCKED): 0 = unlocked (writable), 1 = locked.

**Lock sequence**: Disable INTCON0.GIE → write 0x55 to PPSLOCK → write 0xAA to
PPSLOCK → BSF PPSLOCK,0 (lock) or BCF PPSLOCK,0 (unlock) → enable GIE.

**PPS1WAY config bit**: When set, PPSLOCKED can only be cleared once per reset.
After locking, cannot be unlocked until next reset.

## Constraints & Rules

- **Bidirectional pins**: I2C SCL/SDA — input and output PPS must select the same
  pin. I2C-default pins (RC3/RC4 for I2C1, RB1/RB2 for I2C2) are I2C/SMBus-
  compatible; other pins operate at TTL/ST levels per INLVLCFG.
- **ANSEL**: Clear ANSEL bit for any pin used as digital PPS input.
- **Output TRIS**: TRIS retains control; I2C and UART peripherals override TRIS
  automatically when actively driving the pin.
- **POR defaults**: All input registers get their default pin; all output
  registers reset to 0x00 (LATxy). Non-POR resets preserve PPS settings.
- **Sleep**: PPS selections unaffected by Sleep.

## Key Differences from Q41 PPS

| Feature           | K42                        | Q41                        |
|-------------------|----------------------------|----------------------------|
| CCP modules       | CCP1–4                     | CCP1 only (PWM via PWMxS1Px) |
| PWM generators    | PWM5–8 (0x0D–0x10)         | PWM1–3 with S1P1/S1P2      |
| CWG modules       | CWG1–3 (4 outputs each)   | CWG1 only                  |
| UART instances    | UART1, UART2               | UART1, UART2, UART3        |
| I2C instances     | I2C1, I2C2                 | I2C1 only                  |
| SPI instances     | SPI1 only                  | SPI1, SPI2                 |
| Timers with PPS   | T0–T6 (CKI, G, IN)        | T0–T4                      |
| Comparators out   | C1OUT, C2OUT               | C1OUT, C2OUT               |
| NCO               | NCO1                       | NCO1                       |
| DSM               | DSM1                       | DSM1                       |
| CLC outputs       | CLC1OUT–CLC4OUT            | CLC1OUT–CLC4OUT            |
| Available ports   | A, B, C (28-pin)           | A, B, C (20-pin)          |
| Output value range| 0x00–0x32                  | 0x00–0x28                  |