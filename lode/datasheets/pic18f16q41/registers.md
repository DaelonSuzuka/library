# PIC18F16Q41 — SFR Register Quick Reference

Address map by peripheral. Bit-field details in per-peripheral lode files.
SFR space: 0x000–0x04FF. Config words at 0x300000+.

## Oscillator
| Addr | Reg | Description |
|------|-----|-------------|
| 0xAD | OSCCON1 | Clock source select (NOSC) & divider (NDIV) |
| 0xAE | OSCCON2 | Active source (COSC) & divider (CDIV) |
| 0xAF | OSCCON3 | Clock switch hold, ready flags |
| 0xB0 | OSCTUNE | HFINTOSC tuning (TUN) |
| 0xB1 | OSCFRQ | HFINTOSC frequency select |
| 0xB2 | OSCSTAT | Osc ready flags (HF/MF/LF/SOSC/PLL) |
| 0xB3 | OSCEN | Oscillator enables |
| 0xB4 | PRLOCK | Peripheral reg lock |

## Power, Reset & WDT
| Addr | Reg | Description |
|------|-----|-------------|
| 0x48 | VREGCON | Voltage regulator PM control |
| 0x49 | BORCON | Brown-out enable & status |
| 0x4A–0x4B | HLVDCON0/1 | High/low-voltage detect config |
| 0x4C | ZCDCON | Zero-cross detect control |
| 0x63–0x68 | PMD0–PMD5 | Peripheral module disable |
| 0x78–0x7C | WDTCON0–WDTTMR | WDT config, prescale, window, timer |
| 0x4F0–0x4F2 | PCON0/1, CPUDOZE | Power-on/brown-out status, CPU doze |

## I/O Ports & PPS
| Addr | Reg | Description |
|------|-----|-------------|
| 0x4CE–0x4D0 | PORTA/B/C | Read pins |
| 0x4BE–0x4C0 | LATA/B/C | Output latches |
| 0x4C6–0x4C8 | TRISA/B/C | Direction registers |
| 0x400/0x408/0x410 | ANSELA/B/C | Analog select |
| 0x401/0x409/0x411 | WPUA/B/C | Weak pull-ups |
| 0x402/0x40A/0x412 | ODCONA/B/C | Open-drain |
| 0x403/0x40B/0x413 | SLRCONA/B/C | Slew rate |
| 0x404/0x40C/0x414 | INLVLA/B/C | Input level select |
| 0x405–0x417 | IOCxP/N/F | Interrupt-on-change (A/B/C) |
| 0x200 | PPSLOCK | Lock PPS writes |
| 0x201–0x218 | RxxPPS | Output pin mapping (A0–A5, B4–B7, C0–C7) |
| 0x23E–0x26F | Input PPS | Peripheral input selects (INT, TMR, CCP, PWM, SPI, I2C, UART) |

## Interrupts
| Addr | Reg | Description |
|------|-----|-------------|
| 0x4D6 | INTCON0 | GIE/GIEL, IPEN, edge selects |
| 0x4D7 | INTCON1 | Interrupt status |
| 0x4A8–0x4B2 | PIE0–PIE10 | Interrupt enables |
| 0x4B3–0x4BD | PIR0–PIR10 | Interrupt flags |
| 0x367–0x371 | IPR0–IPR10 | Interrupt priorities |
| 0xBE | MAINPR | Main priority level |
| 0xBF | ISRPR | ISR priority level |

## Timers
**Timer0** (0x318–0x31B): TMR0L/H, T0CON0 (enable/prescale-out/16-bit), T0CON1 (source/async/prescale-in)
**Timer1** (0x312–0x317): TMR1L/H, T1CON, T1GCON, T1GATE, T1CLK
**Timer2** (0x31C–0x321): T2TMR, T2PR, T2CON, T2HLT, T2CLKCON, T2RST
**Timer3** (0x322–0x328): TMR3L/H, T3CON, T3GCON, T3GATE, T3CLK
**Timer4** (0x329–0x32E): T4TMR, T4PR, T4CON, T4HLT, T4CLKCON, T4RST

See timers.md for bit-field details.

## SMT1 (Signal Measurement Timer)
| 0x300–0x30B | SMT1TMR/CPR/CPW/PR | 24-bit timer, capture, window, period |
| 0x30C–0x311 | SMT1CON0–SMT1WIN | Control, mode, status, clock, signal/window select |

## CCP & PWM
| Addr | Reg | Description |
|------|-----|-------------|
| 0x340–0x343 | CCPRx, CCP1CON, CCPxCAP | Capture/compare value, control, trigger |
| 0x34C | CCPTMRS0 | CCP timer selection |
| 0x460–0x46E | PWM1ERS–PWM1S1P2 | PWM1: ERS, CLK, LDS, PR, prescale, config, duty |
| 0x46F–0x47D | PWM2ERS–PWM2S1P2 | PWM2: same structure |
| 0x47E–0x048C | PWM3ERS–PWM3S1P2 | PWM3: same structure |
| 0x49C | PWMLOAD | PWM load control |
| 0x49D | PWMEN | PWM module enable |

## NCO1
| Addr | Reg | Description |
|------|-----|-------------|
| 0x440–0x445 | NCO1ACC/INC | 20-bit accumulator & increment |
| 0x446 | NCO1CON | Enable, output polarity, PFM |
| 0x447 | NCO1CLK | Pulse width & clock select |

## CWG1
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3BC–0x3C4 | CWG1CLK–CWG1STR | Clock, input select, dead-band, control, auto-shutdown, steering |

## Comparators & Mixed-Signal
| Addr | Reg | Description |
|------|-----|-------------|
| 0x6A–0x6E | MD1CON0–MD1CARH | Multiplexer config, source, carry |
| 0x6F | CMOUT | Comparator output status |
| 0x70–0x73 | CM1CON0–CM1PCH | CMP1: enable, output, hysteresis, channel |
| 0x74–0x77 | CM2CON0–CM2PCH | CMP2: same structure |
| 0x7C/0x7E | DAC1DATL/DAC1CON | DAC1 data & control |
| 0xA0/0xA2 | DAC2DATL/DAC2CON | DAC2 data & control |
| 0xA3–0xA9 | OPA1CON0–OPA1ORS | Op-amp 1 config & offset |
| 0x4C | ZCDCON | Zero-cross detect |

## ADC
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3D7 | FVRCON | Fixed voltage reference |
| 0x3D8 | ADCP | ADC charge pump |
| 0x3D9–0x3E0 | ADLTH–ADSTPT | Threshold, error, set point |
| 0x3E1–0x3E6 | ADFLTR–ADCNT | Filter, accumulator, count |
| 0x3E7–0x3EB | ADRPT–ADRES | Repeat, prev, result |
| 0x3EC | ADPCH | Positive channel select |
| 0x3EE–0x3F0 | ADACQ/ADCAP | Acquisition time, capacitance |
| 0x3F1 | ADPRE | Precharge time |
| 0x3F3–0x3FA | ADCON0–ADCLK | ADC control, status, ref, trigger, clock |

## SPI (1 & 2)
SPI1: 0x80–0x8C (RXB, TXB, TCNT, CON0/1/2, STATUS, TWIDTH, BAUD, INTF/INTE, CLK)
SPI2: 0x8D–0x99 (same structure)
See spi.md for bit-field details.

## I2C
| Addr | Reg | Description |
|------|-----|-------------|
| 0x28A–0x28B | I2C1RXB/TXB | RX/TX buffers |
| 0x28C–0x28F | I2C1CNT/ADB | Byte count, address buffers |
| 0x290–0x293 | I2C1ADR0–3 | Address mask registers |
| 0x294–0x296 | I2C1CON0/1/2 | Control: enable, start, mode, ACK |
| 0x297–0x299 | I2C1ERR/STAT0/1 | Error & status flags |
| 0x29A–0x29F | I2C1PIR–I2C1CLK | Interrupts, bus timeout, baud, clock |

## UART (1/2/3)
UART1 (0x2A1–0x2B3): RXB, TXB, RXCHK, TXCHK, P1–P3, CON0/1/2, BRG, FIFO, UIR, ERRIR/ERRIE
UART2 (0x2B4–0x2C6): same structure
UART3 (0x2C7–0x2D9): same structure
Key regs per UART: UxCON0 (mode), UxCON1 (ON), UxCON2 (flow), UxBRG (baud), UxFIFO (status). See uart.md.

## CLC (1–4)
| Addr | Reg | Description |
|------|-----|-------------|
| 0xD4 | CLCDATA | Output status (CLC1–4OUT) |
| 0xD5 | CLCSELECT | Instance select (SLCT) |
| 0xD6–0xDF | CLCnCON–CLCnGLS3 | Per-instance: control, polarity, selects (SEL0–3), gates (GLS0–3) |

## DMA (1–4)
| Addr | Reg | Description |
|------|-----|-------------|
| 0xE8 | DMASELECT | Channel select (SLCT) |
| 0xE9–0xFB | DMAnBUF–DMAnSSA | Per-channel: buffer, counts, pointers, sizes, addresses |
| 0xFC | DMAnCON0 | Enable, interrupt, go, auto-reload |
| 0xFD | DMAnCON1 | Mode, stepping control |

## CRC & Scanner
| Addr | Reg | Description |
|------|-----|-------------|
| 0x34E–0x355 | CRC data/out/shift/XOR | 32-bit CRC engine registers |
| 0x356–0x358 | CRCCON0/1/2 | CRC control, poly/data length |
| 0x35A–0x361 | SCANLADR–SCANTRIG | Scanner address range & control |

## NVM & FSCM
| Addr | Reg | Description |
|------|-----|-------------|
| 0x40–0x44 | NVMCON0–NVMADR | NVM control, command, lock, address, data |
| 0x458 | FSCMCON | Fail-safe clock monitor control |

## Core / CPU
| Addr | Reg | Description |
|------|-----|-------------|
| 0x4D8 | STATUS | ALU flags (N, OV, Z, DC, C) |
| 0x4E0 | BSR | Bank select |
| 0x4E8 | WREG | Working register |
| 0x4D9/0x4E1/0x04E9 | FSR0/1/2 | Indirect data pointers |
| 0x4F3 | PROD | Multiply result (16-bit) |
| 0x4F5 | TABLAT | Table latch |
| 0x4F6 | TBLPTR | Table pointer (22-bit) |
| 0x4F9 | PCL | PC low byte |
| 0x4FA | PCLAT | PC latch |
| 0x4FC | STKPTR | Stack pointer |
| 0x4FD | TOS | Top-of-stack return |

## Config Words (0x300000+)
| Addr | Reg | Key Fields |
|------|-----|------------|
| 0x300000 | CONFIG1 | RSTOSC, FEXTOSC |
| 0x300001 | CONFIG2 | FCMEN, CSWEN, CLKOUTEN |
| 0x300002 | CONFIG3 | BOREN, MVECEN, MCLRE |
| 0x300003 | CONFIG4 | LVP, PPS1WAY, ZCD |
| 0x300004–5 | CONFIG5/6 | WDT enable/prescale/window |
| 0x300006 | CONFIG7 | DEBUG, SAF, BBSIZE |
| 0x300007 | CONFIG8 | Write protection |
| 0x300008 | CONFIG9 | Code protection |