# PIC18F27/47/57Q43 — SFR Register Quick Reference

Address map by peripheral. Bit-field details in per-peripheral lode files.
SFR space: 0x000D–0x0FFF (access bank) + 0x3000–0x3FFF (upper). Config words at 0x300000+.

## NVM & Lock

| Addr | Reg | Description |
|------|-----|-------------|
| 0x040 | NVMCON0 | GO bit (start operation) |
| 0x041 | NVMCON1 | WRERR, NVMCMD<2:0> |
| 0x042 | NVMLOCK | Unlock pattern (0x55 then 0xAA) |
| 0x043 | NVMADRL | Address low byte |
| 0x044 | NVMADRH | Address mid byte |
| 0x045 | NVMADRU | Address high byte (bits 21:16) |
| 0x046 | NVMDATL | Data low byte |
| 0x047 | NVMDATH | Data high byte |
| 0x04C | ZCDCON | ZCD control (SEN, OUT, POL, INTP, INTN) |
| 0x06A | MD1CON0 | DSM control (EN, OUT, OPOL, BIT) |
| 0x06B | MD1CON1 | DSM carrier polarity/sync |
| 0x06C | MD1SRC | DSM modulator source (MS<5:0>) |
| 0x06D | MD1CARL | DSM carrier low (CL<4:0>) |
| 0x06E | MD1CARH | DSM carrier high (CH<4:0>) |

## CLC (1–8, shared via CLCSELECT)

| Addr | Reg | Description |
|------|-----|-------------|
| 0x0D4 | CLCDATA | Output status (CLC8OUT–CLC1OUT) |
| 0x0D5 | CLCSELECT | Instance select (SLCT<2:0>) |
| 0x0D6 | CLCnCON | EN, OUT, INTP, INTN, MODE<2:0> |
| 0x0D7 | CLCnPOL | POL, G4POL–G1POL |
| 0x0D8–0xDB | CLCnSEL0–3 | D1S–D4S input mux (8-bit each) |
| 0x0DC–0xDF | CLCnGLS0–3 | Gate logic select |

## DMA (1–6, shared via DMASELECT)

| Addr | Reg | Description |
|------|-----|-------------|
| 0x0E8 | DMASELECT | Instance select (SLCT<2:0>) |
| 0x0E9–0xFF | DMAnBUF–DMAnSIRQ | DMA channel registers |

## PPS Output & Input

| Addr Range | Regs | Description |
|------------|------|-------------|
| 0x0201–0x0207 | RA0PPS–RA7PPS | Port A output selects |
| 0x0209–0x020F | RB0PPS–RB7PPS | Port B output selects |
| 0x0211–0x0217 | RC0PPS–RC7PPS | Port C output selects |
| 0x0219–0x021D | RD0PPS–RD4PPS | Port D output selects (47/57-pin) |
| 0x0229–0x0230 | RF0PPS–RF7PPS | Port F output selects (57-pin only) |
| 0x023E–0x027B | Input PPS | Peripheral input selects |

## UART (1–5)

| Addr | UART1 | UART2 | Description |
|------|-------|-------|-------------|
| — | 0x02A1 | 0x02B4 | UxRXB — RX buffer |
| — | 0x02A3 | 0x02B6 | UxTXB — TX buffer |
| — | 0x02AB | 0x02BE | UxCON0 — Control 0 |
| — | 0x02AC | 0x02BF | UxCON1 — Control 1 |
| — | 0x02AD | 0x02C0 | UxCON2 — Control 2 |
| — | 0x02AE | 0x02C1 | UxBRGL — Baud rate low |
| — | 0x02AF | 0x02C2 | UxBRGH — Baud rate high |

UART3 at 0x02C7, UART4 at 0x02DA, UART5 at 0x02ED (same structure offsets).

## SMT1

| Addr | Reg | Description |
|------|-----|-------------|
| 0x0300–0x030B | SMT1TMR/CPR/CPW/PR | 24-bit timer, capture, period |
| 0x030C | SMT1CON0 | EN, STP, WPOL, SPOL, CPOL, PS<1:0> |
| 0x030D | SMT1CON1 | GO, REPEAT, MODE<3:0> |
| 0x030E | SMT1STAT | CPRUP, CPWUP, RST, TS, WS, AS |
| 0x030F | SMT1CLK | CSEL<3:0> |
| 0x0310 | SMT1SIG | SSEL<5:0> |
| 0x0311 | SMT1WIN | WSEL<5:0> |

## Timers

**Timer0** (0x318–0x31B): TMR0L, TMR0H, T0CON0, T0CON1
**Timer1** (0x31C–0x321): TMR1, T1CON, T1GCON, T1GATE, T1CLK
**Timer3** (0x328–0x32D): TMR3, T3CON, T3GCON, T3GATE, T3CLK
**Timer5** (0x334–0x339): TMR5, T5CON, T5GCON, T5GATE, T5CLK
**Timer2** (0x322–0x327): T2TMR, T2PR, T2CON, T2HLT, T2CLKCON, T2RST
**Timer4** (0x32E–0x333): T4TMR, T4PR, T4CON, T4HLT, T4CLKCON, T4RST
**Timer6** (0x33A–0x33F): T6TMR, T6PR, T6CON, T6HLT, T6CLKCON, T6RST

## CCP & PWM

| Addr | Reg | Description |
|------|-----|-------------|
| 0x340 | CCPR1 | CCP1 capture/compare value |
| 0x342 | CCP1CON | CCP1 control (EN, OUT, FMT, MODE<3:0>) |
| 0x343 | CCP1CAP | CCP1 capture trigger (CTS<3:0>) |
| 0x344 | CCPR2 | CCP2 capture/compare value |
| 0x346 | CCP2CON | CCP2 control |
| 0x347 | CCP2CAP | CCP2 capture trigger |
| 0x348 | CCPR3 | CCP3 capture/compare value |
| 0x34A | CCP3CON | CCP3 control |
| 0x34B | CCP3CAP | CCP3 capture trigger |

PWM1 (0x460–0x48E), PWM2 (0x46F–0x493), PWM3 (0x47E–0x498) — see ccp-pwm.md for full register list.

## CRC & Scanner

| Addr | Reg | Description |
|------|-----|-------------|
| 0x34C | CRCDATH | CRC data high byte |
| 0x34D | CRCDATL | CRC data low byte (write triggers shifter) |
| 0x34E | CRCACCH | CRC accumulator high |
| 0x34F | CRCACCL | CRC accumulator low |
| 0x350 | CRCXORH | CRC polynomial XOR high |
| 0x351 | CRCXORL | CRC polynomial XOR low (bit 0 unimplemented) |
| 0x352 | CRCSHIFTH | CRC shifter high (read-only) |
| 0x353 | CRCSHIFTL | CRC shifter low (read-only) |
| 0x354 | SCANLADRL | Scanner start address low |
| 0x355 | SCANLADRH | Scanner start address mid |
| 0x356 | SCANLADRU | Scanner start address high |
| 0x357 | CRCCON0 | CRC control (EN, GO, BUSY, ACCM, SHIFTM, FULL) |
| 0x358 | CRCCON1 | CRC control (DLEN<3:0>, PLEN<3:0>) |
| 0x359 | SCANCON0 | Scanner control (EN, TRIGEN, SGO, MREG, BURSTMD, BUSY) |
| 0x35A | SCANHADRL | Scanner end address low |
| 0x35B | SCANHADRH | Scanner end address mid |
| 0x35C | SCANHADRU | Scanner end address high |
| 0x35D | SCANTRIG | Scanner trigger source (TSEL<4:0>) |
| 0x35E | SCANPR | Scanner priority |

## NCO (1–3)

| Addr | Instance | Description |
|------|----------|-------------|
| 0x440–0x447 | NCO1 | NCO1ACC, NCO1INCL/H/U, NCO1CON, NCO1CLK |
| 0x44E–0x455 | NCO2 | NCO2 registers |
| 0x456–0x45D | NCO3 | NCO3 registers |

## CWG (1–3)

| Addr | Instance | Description |
|------|----------|-------------|
| 0x492–0x49C | CWG1 | CWG1CON0/1, CLK, ISM, STR, AS0/1, DBR, DBF |
| 0x4A0–0x4AA | CWG2 | CWG2 registers (same structure) |
| 0x4AE–0x4B8 | CWG3 | CWG3 registers (same structure) |

## DSM1

| Addr | Reg | Description |
|------|-----|-------------|
| 0x06A | MD1CON0 | Enable, output, polarity, BIT |
| 0x06B | MD1CON1 | CHPOL, CHSYNC, CLPOL, CLSYNC |
| 0x06C | MD1SRC | Modulator source (MS<5:0>) |
| 0x06D | MD1CARL | Carrier low (CL<4:0>) |
| 0x06E | MD1CARH | Carrier high (CH<4:0>) |

## Oscillator

| Addr | Reg | Description |
|------|-----|-------------|
| 0x0AD | OSCCON1 | NOSC<2:0>, NDIV<3:0> |
| 0x0AE | OSCCON2 | COSC<2:0>, CDIV<3:0> |
| 0x0AF | OSCCON3 | CSWHOLD, SOSCPWR, ORDY, NOSCR |
| 0x0B0 | OSCTUNE | TUN<5:0> |
| 0x0B1 | OSCFRQ | FRQ<3:0> |
| 0x0B2 | OSCSTAT | EXTOR, HFOR, MFOR, LFOR, SOR, ADOR, SFOR, PLLR |
| 0x0B3 | OSCEN | EXTOEN, HFOEN, MFOEN, LFOEN, SOSCEN, ADOEN, PLLEN |

## Power, Reset & WDT

| Addr | Reg | Description |
|------|-----|-------------|
| 0x048 | VREGCON | VREGPM<1:0> |
| 0x049 | BORCON | SBOREN, BORRDY |
| 0x04A–0x04B | HLVDCON0/1 | HLVD config |
| 0x078–0x07C | WDTCON0/1, WDTPSL/H, WDTTMR | WDT config |

## PMD (Peripheral Module Disable)

| Addr | Reg | Description |
|------|-----|-------------|
| 0x060 | PMD0 | SYSCMD, FVRMD, HLVDMD, CRCMD, SCANMD, CLKRMD, IOCMD |
| 0x061 | PMD1 | SMT1MD, TMR6–TMR0MD |
| 0x063 | PMD3 | ACTMD, DAC1MD, ADCMD, C2MD, C1MD, ZCDMD |
| 0x064 | PMD4 | CWG3–1MD, DSM1MD, NCO3–1MD |
| 0x065 | PMD5 | PWM3–1MD, CCP3–1MD |
| 0x066 | PMD6 | U5–1MD, SPI2/1MD, I2C1MD |
| 0x067 | PMD7 | CLC8–1MD |
| 0x068 | PMD8 | DMA6–1MD |

## Config Words (0x300000+)

| Addr | Reg | Key Fields |
|------|-----|------------|
| 0x300000 | CONFIG1 | RSTOSC<2:0>, FEXTOSC<2:0> |
| 0x300001 | CONFIG2 | FCMEN, CSWEN, PR1WAY, CLKOUTEN |
| 0x300002 | CONFIG3 | BOREN<1:0>, LPBOREN, IVT1WAY, MVECEN, PWRTS<1:0>, MCLRE |
| 0x300003 | CONFIG4 | XINST, LVP, STVREN, PPS1WAY, ZCD, BORV<1:0> |
| 0x300004 | CONFIG5 | WDTE<1:0>, WDTCPS<4:0> |
| 0x300005 | CONFIG6 | WDTCCS<2:0>, WDTCWS<2:0> |
| 0x300006 | CONFIG7 | DEBUG, SAFEN, BBEN, BBSIZE<2:0> |
| 0x300007 | CONFIG8 | WRTAPP, WRTSAF, WRTD, WRTC, WRTB |
| 0x300009 | CONFIG10 | CP (code protection) |