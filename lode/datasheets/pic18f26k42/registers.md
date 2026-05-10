# PIC18F26K42 — SFR Register Quick Reference

Address map by peripheral. Bit-field details in per-peripheral lode files.
SFR space: 0x3800–0x3FFF. Config words at 0x300000+.

## Oscillator
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3FD9 | OSCCON1 | Clock source select (NOSC) & divider (NDIV) |
| 0x3FDA | OSCCON2 | Active source (COSC) & divider (CDIV) |
| 0x3FDB | OSCCON3 | Clock switch hold, ready flags |
| 0x3FDC | OSCSTAT | Osc ready flags (HF/MF/LF/SOSC/PLL) |
| 0x3FDD | OSCEN | Oscillator enables (EXT/HF/MF/LF/SOSC/AD) |
| 0x3FDE | OSCTUNE | HFINTOSC tuning (TUN) |
| 0x3FDF | OSCFRQ | HFINTOSC frequency select |

## Power, Reset & WDT
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3D08 | VREGCON | Voltage regulator PM control (VREGPM) |
| 0x3D09 | BORCON | Brown-out enable & status |
| 0x3ECA–0x3EC9 | HLVDCON1/0 | High/low-voltage detect config |
| 0x3EC3 | ZCDCON | Zero-cross detect control |
| 0x3DC0–0x3DC7 | PMD0–PMD7 | Peripheral module disable |
| 0x3D5B–0x3D5E | WDTCON0/1, WDTPSL/H, WDTTMR | WDT config, prescale, window, timer |
| 0x3FF0/1 | PCON0/1 | Power-on/brown-out status |
| 0x3FD0 | CPUDOZE | CPU doze/idle control |

## I/O Ports & PPS
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3FC8–0x3FCF | PORTA/B/C/D/E/F | Read pins |
| 0x3FBA–0x3FC1 | LATA/B/C/D/E/F | Output latches |
| 0x3FC2–0x3FC9 | TRISA/B/C/D/E/F | Direction registers |
| 0x3A40–0x3A44 | ANSELA/B/C/D/E | Analog select |
| 0x3A41–0x3A45 | WPUA/B/C/D/E | Weak pull-ups |
| 0x3A42–0x3A46 | ODCONA/B/C/D/E | Open-drain |
| 0x3A43–0x3A47 | SLRCONA/B/C/D/E | Slew rate |
| 0x3A44–0x3A48 | INLVLA/B/C/D/E | Input level select |
| 0x3A45–0x3A47 | IOCAP/N/F (A), IOCBP/N/F (B), IOCCP/N/F (C) | Interrupt-on-change |
| 0x3ABF | PPSLOCK | Lock PPS writes |
| 0x3A00–0x3A17 | RxxPPS | Output pin mapping (A0–A7, B0–B7, C0–C7) |
| 0x3AC0–0x3AE4 | Input PPS | Peripheral input selects (INT, TMR, CCP, SMT, CWG, MD, SPI, I2C, UART, CLC, ADC) |

## Interrupts
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3FD2 | INTCON0 | GIE/GIEL, IPEN, edge selects |
| 0x3FD3 | INTCON1 | Interrupt status |
| 0x3990–0x399A | PIE0–PIE10 | Interrupt enables |
| 0x39A0–0x39AA | PIR0–PIR10 | Interrupt flags |
| 0x3980–0x398A | IPR0–IPR10 | Interrupt priorities |
| 0x39F2 | MAINPR | Main priority level |
| 0x39F1 | ISRPR | ISR priority level |

## Timers
**Timer0** (0x3FB5–0x3FB9): TMR0L/H, T0CON0 (enable/prescale-out/16-bit), T0CON1 (source/async/prescale-in)
**Timer1** (0x3FB0–0x3FB6): TMR1L/H, T1CON, T1GCON, T1GATE, T1CLK
**Timer2** (0x3FA9–0x3FAE): T2TMR, T2PR, T2CON, T2HLT, T2CLKCON, T2RST
**Timer3** (0x3FA3–0x3FA9): TMR3L/H, T3CON, T3GCON, T3GATE, T3CLK
**Timer4** (0x3F9D–0x3FA3): T4TMR, T4PR, T4CON, T4HLT, T4CLKCON, T4RST
**Timer5** (0x3F97–0x3F9D): TMR5L/H, T5CON, T5GCON, T5GATE, T5CLK
**Timer6** (0x3F91–0x3F97): T6TMR, T6PR, T6CON, T6HLT, T6CLKCON, T6RST

## SMT1 (Signal Measurement Timer)
| 0x3F11–0x3F1C | SMT1TMR/CPR/CPW/PR | 24-bit timer, capture, window, period |
| 0x3F1D–0x3F23 | SMT1CON0–SMT1WIN | Control, mode, status, clock, signal/window select |

## CCP & PWM
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3F70–0x3F7E | CCPR1–4, CCP1–4CON, CCP1–4CAP | 4× CCP: capture/compare value, control, trigger |
| 0x3F5E | CCPTMRS0 | CCP timer selection (C1–C4TSEL) |
| 0x3F5D | CCPTMRS1 | PWM timer selection (P5–P8TSEL) |
| 0x3F62–0x3F68 | PWM5CON/DCL/DCH | PWM5: enable, polarity, duty |
| 0x3F6A–0x3F70 | PWM6CON/DCL/DCH | PWM6: same |
| 0x3F66–0x3F64 | PWM7CON/DCL/DCH | PWM7: same |
| 0x3F62–0x3F60 | PWM8CON/DCL/DCH | PWM8: same |

## NCO1
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3F38–0x3F3D | NCO1ACC/INC | 20-bit accumulator & increment |
| 0x3F3E | NCO1CON | Enable, output polarity, PFM |
| 0x3F3F | NCO1CLK | Pulse width & clock select |

## CWG (1–3)
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3F40–0x3F4A | CWG3CLK–CWG3STR | CWG3: clock, input, dead-band, control, auto-shutdown, steering |
| 0x3F49–0x3F52 | CWG2CLK–CWG2STR | CWG2: same structure |
| 0x3F52–0x3F5A | CWG1CLK–CWG1STR | CWG1: same structure |

## Comparators & Mixed-Signal
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3EC0 | CMOUT | Comparator output status (C1OUT, C2OUT) |
| 0x3EB8/0x3EBD–0x3EBE | CM2/1CON0 | CMP enable, output, polarity, hysteresis, sync |
| 0x3EB9/0x3EBE | CM2/1CON1 | CMP interrupt flags |
| 0x3EBA/0x3EBF | CM2/1NCH | CMP negative channel select |
| 0x3EBB/0x3EC0 | CM2/1PCH | CMP positive channel select |
| 0x3E9E–0x3E9C | DAC1CON0/1 | DAC1 control & 5-bit data |
| 0x3EC3 | ZCDCON | Zero-cross detect |

## ADC
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3EC1 | FVRCON | Fixed voltage reference |
| 0x3ED7 | ADCP | ADC charge pump |
| 0x3EDE–0x3EDF | ADLTHL/H | Lower threshold |
| 0x3EE0–0x3EE1 | ADUTHL/H | Upper threshold |
| 0x3EE2–0x3EE3 | ADERRL/H | Error |
| 0x3EE4–0x3EE5 | ADSTPTL/H | Set point |
| 0x3EE6–0x3EE7 | ADFLTRL/H | Filter |
| 0x3EE8–0x3EEA | ADACCL–ADACCU | Accumulator |
| 0x3EEB | ADCNT | Accumulator count |
| 0x3EEC | ADRPT | Repeat count |
| 0x3EED–0x3EEE | ADPREVL/H | Previous result |
| 0x3EEF–0x3EF0 | ADRESL/H | ADC result |
| 0x3EF1 | ADPCH | Positive channel select |
| 0x3EF3 | ADACQL | Acquisition time (low) |
| 0x3EF4 | ADACQH | Acquisition time (high) |
| 0x3EF5 | ADCAP | ADC capacitance |
| 0x3EF6–0x3EF7 | ADPREL/H | Precharge time |
| 0x3EF8 | ADCON0 | ADC control (ON, CONT, CS, FM, GO) |
| 0x3EF9 | ADCON1 | ADC control 1 (PPOL, IPEN, GPOL, DSEN) |
| 0x3EFA | ADCON2 | ADC control 2 (PSIS, CRS, ACLR, MODE) |
| 0x3EFB | ADCON3 | ADC control 3 (CALC, SOI, TMD) |
| 0x3EFC | ADSTAT | ADC status (ADAOV, threshold, math, STAT) |
| 0x3EFD | ADREF | Voltage reference select |
| 0x3EFE | ADACT | Auto-conversion trigger |
| 0x3EFF | ADCLK | ADC clock select |

## SPI1
| 0x3D10–0x3D1C | SPI1RXB, TXB, TCNTL/H, CON0/1/2, STATUS, TWIDTH, BAUD, INTF/INTE, CLK |

## I2C (1 & 2)
I2C1: 0x3D6A–0x3D7C (RXB, TXB, CNT, ADR0–3, ADB0/1, CON0/1/2, ERR, STAT0/1, PIR, PIE, BTO, CLK)
I2C2: 0x3D54–0x3D66 (same structure)

## UART (1 & 2)
UART1: 0x3DE8–0x3DFA (RXB, TXB, RXCHK, TXCHK, P1–P3, CON0/1/2, BRGL/H, FIFO, UIR, ERRIR/ERRIE)
UART2: 0x3DD0–0x3DE2 (same structure, note: P2/P3 and some regs not present)

## CLC (1–4)
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3C7E | CLCDATA0 | Output status (CLC1–4OUT) |
| 0x3C74–0x3C76 | CLC1CON/POL/SEL0 | CLC1: control, polarity, select |
| 0x3C77–0x3C7D | CLC1SEL1–GLS3 | CLC1: selects & gates |
| Same structure for CLC2–4 at 0x3C56–0x3C72 | | |

## DMA (1 & 2)
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3BE9–0x3BFE | DMA1BUF–DMA1SIRQ | Channel 1: buffer, pointers, sizes, addresses, IRQ |
| 0x3BC9–0x3BDE | DMA2BUF–DMA2SIRQ | Channel 2: same structure |

## Scanner & CRC
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3D1C–0x3D1F | SPI1CON0/1/2 | SPI1 control |
| 0x3DFB | SCANCON0 | Scanner control |
| 0x397B–0x397F | SCANHADRL/U, SCANLADRL/U | Scanner address |
| 0x3DFA | SCANTRIG | Scanner trigger |
| 0x3DFA–0x3D69 | CRCCON0/1, DATA/ACC/SHIFT/XOR | CRC engine |

## NVM & PPS Lock
| Addr | Reg | Description |
|------|-----|-------------|
| 0x39E0–0x39E5 | NVMADRL/H, NVMDAT, NVMCON1/2 | NVM control, command, address, data |
| 0x39EF | PRLOCK | Peripheral reg lock |

## Clock Reference
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3CE6 | CLKRCON | Clock reference control (enable, divider) |
| 0x3CE5 | CLKRCLK | Clock reference source select |

## Core / CPU
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3FD8 | STATUS | ALU flags (N, OV, Z, DC, C) |
| 0x3FE0 | BSR | Bank select |
| 0x3FE8 | WREG | Working register |
| 0x3FE9–0x3FEB | FSR0 | Indirect data pointer 0 |
| 0x3FE1–0x3FE3 | FSR1 | Indirect data pointer 1 |
| 0x3FDA–0x3FDC | FSR2 | Indirect data pointer 2 |
| 0x3FF3 | PROD | Multiply result (16-bit) |
| 0x3FF5 | TABLAT | Table latch |
| 0x3FF6–0x3FF8 | TBLPTR | Table pointer (22-bit) |
| 0x3FF9 | PCL | PC low byte |
| 0x3FFA | PCLATH | PC latch high |
| 0x3FFB | PCLATU | PC latch upper |
| 0x3FFC | STKPTR | Stack pointer |
| 0x3FFD–0x3FFF | TOS | Top-of-stack return |

## Interrupt Vector
| Addr | Reg | Description |
|------|-----|-------------|
| 0x3FD4 | IVTLOCK | IVT lock |
| 0x3FD5–0x3FD7 | IVTBASEL/H/U | IVT base address |
| 0x389D–0x389F | IVTADL/H/U | IVT address |

## Config Words (0x300000+)
| Addr | Reg | Key Fields |
|------|-----|------------|
| 0x300000 | CONFIG1 | RSTOSC, FEXTOSC |
| 0x300001 | CONFIG2 | FCMEN, CSWEN, CLKOUTEN |
| 0x300002 | CONFIG3 | BOREN, MVECEN, MCLRE |
| 0x300003 | CONFIG4 | LVP, PPS1WAY, ZCD |
| 0x300004–5 | CONFIG5/6 | WDT enable/prescale/window |
| 0x300006 | CONFIG7 | DEBUG, SAF, BBSIZE |