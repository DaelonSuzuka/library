# PIC18F16Q41 — Silicon Errata

Source: DS80000901G (Mar 2025). Applies to DS40002214G datasheet.

## Silicon Revisions

| Part | Device ID | A4 | A5 | A6 | B1 |
|------|-----------|----|----|----|----|
| PIC18F06Q41 | 0x7580 | 0xA004 | 0xA005 | 0xA006 | 0xA041 |
| PIC18F18Q41 | 0x7560 | 0xA004 | 0xA005 | 0xA006 | 0xA041 |

**B1 is the current silicon revision.** Earlier revisions (A4–A6) are legacy.

## Silicon Issues (current revision B1)

| # | Module | Issue |
|---|--------|-------|
| 1.3.3 | I2C | MDR bit not cleared after bus time-out |
| 1.3.4 | I2C | Bus time-out not detected properly when external host clock stretches |
| 1.3.5 | I2C | Clock stretch disable (CSD) not working properly |
| 1.3.6 | I2C | Bus time-out causes false Start/Stop on bus |
| 1.3.7 | I2C | CSTR bit not cleared after bus time-out |
| 1.3.8 | I2C | Multi-Host mode causes bus failures |
| 1.9.1 | Instruction Set | PUSHL instruction incorrectly executes with certain FSR2 values |

## Silicon Issues (legacy revisions A4–A6 only)

| # | Module | Issue | Revisions |
|---|--------|-------|-----------|
| 1.1.1 | ADCC | ADC inoperable with LFINTOSC/SOSC + BOR disabled + FVR disabled | A4 |
| 1.1.2 | ADCC | Double sample conversion inserts max acquisition time on 2nd conversion | A4–A6 |
| 1.2.1 | Oscillator | XT mode max freq reduced to 2 MHz (from 4 MHz) | A4 |
| 1.2.2 | Oscillator | FOSC FSCM + primary/secondary FSCM causes false failures in Sleep | A4 |
| 1.2.3 | Oscillator | EC mode max 32 MHz at VDD < 2.0V | A4 |
| 1.3.1 | I2C | I2CxADR0/1/2/3 incorrect reset values | A4 |
| 1.3.2 | I2C | Spurious Start/Stop flags on I2C enable | A4–A5 |
| 1.4.1 | OPA | CPON bit reserved — charge pump always-on when OPA active | A4 |
| 1.4.2 | OPA | Internal resistor ladder not disconnected in unity gain mode | A4 |
| 1.5.1 | UART | TXDE goes low before STOP bit fully transmitted | A4–A6 |
| 1.5.2 | UART | 9-bit async address mode false match/mismatch | A4–A6 |
| 1.6.1 | SMT | RST bit breaks module when prescaler ≠ 1:1 | A4–A6 |
| 1.7.1 | PIC18 Core | FSR Shadow Registers not writable | A4–A6 |
| 1.8.1 | LVP/ICSP | LVP impossible when VDD < BORV with BOR enabled | A4–A6 |

## Workarounds (current revision B1 issues)

- **1.3.3** — Force a Stop on bus (set P bit) on bus time-out in host mode.
- **1.3.4** — Reset I2C module by toggling EN bit.
- **1.3.5** — Reset I2C module by toggling EN bit.
- **1.3.6** — No workaround. Avoid I2C client mode with clock stretching hosts if possible.
- **1.3.7** — Reset I2C module by toggling EN bit.
- **1.3.8** — No workaround. Do not use Multi-Host mode.
- **1.9.1** — Do not use PUSHL when FSR2 = 0xDB, 0xDC, 0xDE, 0xE3, 0xE4, 0xE6, 0xEB, 0xEC, 0xEE.

## Datasheet Clarifications

- **Interrupt Vector Priority Table (Table 11-2):** Vector numbers for CWG1, NCO1, DMA2SCNT, DMA2DCNT, DMA2OR, and DMA2A were incorrect. Corrected values: 0x32=CWG1, 0x33=NCO1, 0x34=DMA2SCNT, 0x35=DMA2DCNT, 0x36=DMA2OR, 0x37=DMA2A.