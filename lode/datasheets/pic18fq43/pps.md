# PIC18F27/47/57Q43 — PPS (Peripheral Pin Select)

## Overview

PPS remaps digital peripheral inputs/outputs to I/O pins. Analog functions
remain fixed. Input and output selections are independent.

## PPS Output Selection (RxyPPS values)

Write value to a pin's RxyPPS register to route a peripheral output to that pin.
Multiple pins can share the same output source. All RxyPPS values reset to 0x00
(POR/BOR) which selects LATxy (no peripheral drive). Non-POR resets preserve PPS.

| Value | Source | Value | Source |
|-------|--------|-------|--------|
| 0x00 | LATxy | 0x23 | UART1 TXDE |
| 0x01 | CLC1OUT | 0x22 | UART1 RTS |
| 0x02 | CLC2OUT | 0x25 | UART2 TXDE |
| 0x03 | CLC3OUT | 0x24 | UART2 RTS |
| 0x04 | CLC4OUT | 0x28 | UART3 RTS |
| 0x05 | CLC5OUT | 0x27 | UART3 TXDE |
| 0x06 | CLC6OUT | 0x26 | UART3 TX |
| 0x07 | CLC7OUT | 0x2B | UART4 RTS |
| 0x08 | CLC8OUT | 0x2A | UART4 TXDE |
| 0x09 | CWG1A | 0x29 | UART4 TX |
| 0x0A | CWG1B | 0x2E | UART5 RTS |
| 0x0B | CWG1C | 0x2D | UART5 TXDE |
| 0x0C | CWG1D | 0x2C | UART5 TX |
| 0x0D | CWG2A | 0x20 | UART1 TX |
| 0x0E | CWG2B | 0x30 | C1OUT |
| 0x0F | CWG2C | 0x2F | C2OUT |
| 0x10 | CWG2D | 0x31 | SPI1 SCK |
| 0x11 | CWG3A | 0x32 | SPI1 SDO |
| 0x12 | CWG3B | 0x33 | SPI1 SS |
| 0x13 | CWG3C | 0x34 | SPI2 SCK |
| 0x14 | CWG3D | 0x35 | SPI2 SDO |
| 0x15 | CCP1 | 0x36 | SPI2 SS |
| 0x16 | CCP2 | 0x37 | I2C1 SCL* |
| 0x17 | CCP3 | 0x38 | I2C1 SDA* |
| 0x18 | PWM1S1P1_OUT | 0x39 | TMR0 |
| 0x19 | PWM1S1P2_OUT | 0x3F | NCO1 |
| 0x1A | PWM2S1P1_OUT | 0x40 | NCO2 |
| 0x1B | PWM2S1P2_OUT | 0x41 | NCO3 |
| 0x1C | PWM3S1P1_OUT | 0x42 | CLKR |
| 0x1D | PWM3S1P2_OUT | 0x43 | DSM1 |
| 0x1E–0x1F | Reserved | 0x44 | ADGRDA |
| | | 0x45 | ADGRDB |

\* Bidirectional pins — input and output PPS must select the same pin.

## PPS Input Selection (xxxPPS registers)

Each peripheral has a dedicated input register. Value encoding: bits [5:3] = PORT,
bits [2:0] = PIN.

| PORT[2:0] | Port | PIN[2:0] | Pin |
|-----------|------|----------|-----|
| 000 | A | 000 | Rx0 |
| 001 | B | 001 | Rx1 |
| 010 | C | 010 | Rx2 |
| 011 | D | 011 | Rx3 |
| 100 | E | 100 | Rx4 |
| 101 | F | 101 | Rx5 |
| | | 110 | Rx6 |
| | | 111 | Rx7 |

28-pin (PIC18F27Q43): Ports A, B, C available. 40-pin adds D. 48-pin adds D, E, F.
PPS input encoding uses up to 6 bits; some registers use only PORT[1:0] (2-bit) or
PORT[2:0] (3-bit) depending on available ports for that peripheral.

### Input Register POR Defaults (28-pin PIC18F27Q43)

| Register | Default Pin | Register | Default Pin |
|----------|-------------|----------|-------------|
| INT0PPS | RB0 (0x08) | CWG1PPS | RB0 (0x08) |
| INT1PPS | RB1 (0x09) | CWG2PPS | RB1 (0x09) |
| INT2PPS | RB2 (0x0A) | CWG3PPS | RB2 (0x0A) |
| T0CKIPPS | RA4 (0x04) | MD1CARLPPS | RA3 (0x03) |
| T1CKIPPS | RC0 (0x10) | MD1CARHPPS | RA4 (0x04) |
| T1GPPS | RB5 (0x0D) | MD1SRCPPS | RA5 (0x05) |
| T3CKIPPS | RC0 (0x10) | CLCIN0PPS | RA0 (0x00) |
| T3GPPS | RC0 (0x10) | CLCIN1PPS | RA1 (0x01) |
| T5CKIPPS | RC2 (0x12) | CLCIN2PPS | RB6 (0x0E) |
| T5GPPS | RB4 (0x0C) | CLCIN3PPS | RB7 (0x0F) |
| T2INPPS | RC3 (0x13) | CLCIN4PPS | RA0 (0x00) |
| T4INPPS | RC5 (0x15) | CLCIN5PPS | RA1 (0x01) |
| T6INPPS | RB7 (0x0F) | CLCIN6PPS | RB6 (0x0E) |
| CCP1PPS | RC2 (0x12) | CLCIN7PPS | RB7 (0x0F) |
| CCP2PPS | RC1 (0x11) | ADACTPPS | RB4 (0x0C) |
| CCP3PPS | RB5 (0x0D) | SPI1SCKPPS | RC3 (0x13) |
| SMT1WINPPS | RC0 (0x10) | SPI1SDIPPS | RC4 (0x14) |
| SMT1SIGPPS | RC1 (0x11) | SPI1SSPPS | RA5 (0x05) |
| PWMIN0PPS | RC2 (0x12) | SPI2SCKPPS | RB3 (0x0B) |
| PWMIN1PPS | RC6 (0x16) | SPI2SDIPPS | RB2 (0x0A) |
| PWM1ERSPPS | RC3 (0x13) | SPI2SSPPS | RA4 (0x04) |
| PWM2ERSPPS | RC5 (0x15) | I2C1SDAPPS* | RC4 (0x14) |
| PWM3ERSPPS | RB7 (0x0F) | I2C1SCLPPS* | RC3 (0x13) |
| U1RXPPS | RC7 (0x17) | U1CTSPPS | RC6 (0x16) |
| U2RXPPS | RB7 (0x0F) | U2CTSPPS | RB6 (0x0E) |
| U3RXPPS | RA7 (0x07) | U3CTSPPS | RA6 (0x06) |
| U4RXPPS | RB5 (0x0D) | U4CTSPPS | RB4 (0x0C) |
| U5RXPPS | RA5 (0x05) | U5CTSPPS | RA4 (0x04) |

\* Bidirectional — input and output PPS must select the same pin.

## Output Pin Registers (RxyPPS)

28-pin Q43 has PPS output registers for RA0–RA7, RB0–RB7, RC0–RC7:

| Addr | Register | Addr | Register | Addr | Register |
|------|----------|------|----------|------|----------|
| 0x201 | RA0PPS | 0x209 | RB0PPS | 0x211 | RC0PPS |
| 0x202 | RA1PPS | 0x20A | RB1PPS | 0x212 | RC1PPS |
| 0x203 | RA2PPS | 0x20B | RB2PPS | 0x213 | RC2PPS |
| 0x204 | RA3PPS | 0x20C | RB3PPS | 0x214 | RC3PPS |
| 0x205 | RA4PPS | 0x20D | RB4PPS | 0x215 | RC4PPS |
| 0x206 | RA5PPS | 0x20E | RB5PPS | 0x216 | RC5PPS |
| 0x207 | RA6PPS | 0x20F | RB6PPS | 0x217 | RC6PPS |
| 0x208 | RA7PPS | 0x210 | RB7PPS | 0x218 | RC7PPS |

40-pin adds RD0–RD7, RE0–RE2. 48-pin adds RF0–RF7.

## PPS Lock Register

PPSLOCK (0x200), bit 0 = PPSLOCKED:
- 0 = unlocked (writable)
- 1 = locked (writes ignored)

**Lock sequence**: Disable INTCON0.GIE → write 0x55 to PPSLOCK → write 0xAA to
PPSLOCK → BSF PPSLOCK,0 (lock) or BCF PPSLOCK,0 (unlock) → enable GIE.

**PPS1WAY config bit**: When set, PPSLOCKED can only transition 0→1 once per reset.
After locking, cannot be unlocked until next reset.

## Bidirectional Pins

I2C SCL/SDA — input and output PPS must select the same pin. Default I2C-compatible
pins (RC3/RC4 for I2C1) support I2C/SMBus voltage levels. Other pins operate at
TTL/ST levels per INLVL register.

## Key Differences from K42 PPS

| Feature | K42 | Q43 |
|---------|-----|-----|
| CLC instances | CLC1–4 | CLC1–8 |
| NCO instances | NCO1 | NCO1–3 |
| CCP modules | CCP1–4 | CCP1–3 only |
| PWM generators | PWM5–8 (4 generators) | PWM1–3 (S1P1/S1P2 outputs) |
| CWG modules | CWG1–3 (4 outputs each) | CWG1–3 (A/B/C/D outputs) |
| UART instances | UART1–2 | UART1–5 |
| SPI instances | SPI1 only | SPI1–2 |
| I2C instances | I2C1–2 | I2C1 only |
| Comparators out | C1OUT, C2OUT | C1OUT, C2OUT |
| Timer outputs (PPS) | TMR0 only | TMR0 only |
| DSM | DSM1 | DSM1 |
| CLKR source | CLK[3:0] 4-bit | CLK[4:0] 5-bit (more sources) |
| ADC guardrail outputs | ADGRDA, ADGRDB | ADGRDA, ADGRDB |
| Output value range | 0x00–0x32 | 0x00–0x45 |
| Available ports (28-pin) | A, B, C | A, B, C |
| Additional ports (48-pin) | — | D, E, F |

## Q43 Errata — PPS-Related

No PPS-specific silicon errata documented for Q43 (revisions B0–C0). PPS operates per datasheet specifications.