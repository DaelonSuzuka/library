# PIC18F27/47/57Q43 — Interrupt System (VIC)

## VIC Overview

The Vectored Interrupt Controller (VIC) consolidates all peripheral interrupt requests into a single CPU
interrupt request. Key features:

- **Fixed 3-cycle latency** (MVECEN=1, vectored mode) or **2-cycle latency** (MVECEN=0, compat mode)
- **Two priority levels**: High and Low (enabled via IPEN in INTCON0)
- **Interrupt Vector Table (IVT)** with unique vector per source (MVECEN=1) or single-polling mode (MVECEN=0)
- **Two-level context saving**: Main routine + Low-ISR context auto-saved/restored (STATUS, WREG, BSR,
  FSR0/1/2, PRODL/H, PCLATH/U, PC)
- WREG receives the resolved vector number upon interrupt entry

## IVTBASE and Vector Table Setup

- Base address register: **IVTBASE** (21-bit, spanning IVTBASEU/H/L at 0x45D), default `0x000008`
- IVTBASE **must be even** for correct operation
- Vector address = `IVTBASE + (2 × Vector Number)` when MVECEN=1
- When MVECEN=0, IPEN=1: high-priority vector at IVTBASE, low-priority at IVTBASE+8 words
- When MVECEN=0, IPEN=0: all interrupts vector to IVTBASE (compat mode)

### IVTBASE Lock (IVTLOCK)

- **IVTLOCKED** bit in IVTLOCK register (0x459) controls write access to IVTBASE
- Unlock sequence (requires GIE=0):
  ```
  MOVLW 0x55; MOVWF IVTLOCK
  MOVLW 0xAA; MOVWF IVTLOCK
  BCF   IVTLOCK, IVTLOCKED
  ```
- Lock sequence: same with BSF IVTLOCK, IVTLOCKED
- **IVT1WAY** config bit (CONFIG3[4]): if set, IVTLOCKED can only be cleared/set once after reset

## Vector Number Table

| Vec | Source | Vec | Source | Vec | Source | Vec | Source |
|----:|:-------|----:|:-------|----:|:-------|----:|:-------|
| 0 | SWINT | 21 | SPI1TX | 42 | DMA1SCNT | 63 | PWM3RINT |
| 1 | HLVD | 22 | SPI1 | 43 | PWM3GINT | 64 | — |
| 2 | OSF | 23 | — | 44 | TMR5 | 65 | — |
| 3 | CSW | 24 | — | 45 | TMR5G | 66 | — |
| 4 | — | 25 | CLC1 | 46 | CCP2 | 67 | — |
| 5 | — | 26 | — | 47 | SCAN | 68 | — |
| 6 | — | 27 | — | 48 | U3RX | 69 | — |
| 7 | IOC | 28 | — | 49 | U3TX | 70 | TMR5 |
| 8 | INT0 | 29 | ZCD | 50 | U3E | 71 | TMR5G |
| 9 | — | 30 | — | 51 | U3 | 72 | — |
| 10 | AD | 31 | CLC2 | 52 | INT2 | 73 | CCP3 |
| 11 | ACT | 32 | CWG1 | 53 | CLC5 | 74 | — |
| 12 | CM1 | 33 | NCO1 | 54 | CWG2 | 75 | CLC6 |
| 13 | SMT1 | 34 | DMA2SCNT | 55 | NCO2 | 76 | — |
| 14 | SMT1PRA | 35 | DMA2DCNT | 56 | DMA3SCNT | 77 | — |
| 15 | SMT1PWA | 36 | DMA2OR | 57 | DMA3DCNT | 78 | — |
| 16 | — | 37 | DMA2A | 58 | DMA3OR | 79 | — |
| 17 | — | 38 | I2C1RX | 59 | DMA3A | 80 | — |
| 18 | SPI1RX | 39 | I2C1TX | 60 | U4RX | 81 | — |
| 19 | — | 40 | I2C1 | 61 | U4TX | 82 | — |
| 20 | — | 41 | I2C1E | 62 | U4E | | |

(See datasheet Table 11-2 for complete vector table through 0x7C.)

Natural order priority: lower vector number = higher hardware priority.

## Priority Levels

- **IPEN** (INTCON0 bit 5) enables 2-level priority; all sources default to high priority after reset
- **IPRx registers**: each bit = 1 → High priority, 0 → Low priority (default all 1)
- High-priority interrupts preempt low-priority ISRs; same-priority cannot preempt each other
- **GIEH** (INTCON0 bit 7): enables all high-priority interrupts (also required for low-priority)
- **GIEL** (INTCON0 bit 6): enables all low-priority interrupts (requires GIEH=1)
- GIEH/GIEL are **not auto-modified** by hardware on ISR entry; internal state machine tracks context
- **INTCON1 STAT[1:0]**: 00=Main, 01=Low ISR, 10=High ISR from main, 11=High ISR preempting Low ISR

## Control Register Map

| Register | Addr | Key Bits |
|----------|------|----------|
| INTCON0 | 0x4D6 | GIE/GIEH(b7), GIEL(b6), IPEN(b5), INT2EDG(b2), INT1EDG(b1), INT0EDG(b0) |
| INTCON1 | 0x4D7 | STAT[1:0](b7:6) — CPU interrupt state |
| IVTBASEU | — | BASE[20:16] |
| IVTBASEH | — | BASE[15:8] |
| IVTBASEL | — | BASE[7:0] (reset=0x08) |
| IVTAD | 0x45A | Read-only: auto-loaded vector address on interrupt |
| IVTLOCK | 0x459 | IVTLOCKED(b0) |
| SHADCON | 0x376 | SHADLO(b0) — select shadow register context |

## PIE Register Bit Maps

| Reg | Addr | Bits [7:0] |
|-----|------|-------------|
| PIE0 | 0x49E | IOCIE, —, CLC1IE, —, CSWIE, OSFIE, HLVDIE, SWIE |
| PIE1 | 0x49F | SMT1PWAIE, SMT1PRAIE, SMT1IE, CM1IE, ACTIE, ADIE, ZCDIE, INT0IE |
| PIE2 | 0x4A0 | DMA1AIE, DMA1ORIE, DMA1DCNTIE, DMA1SCNTIE, —, —, —, ADTIE |
| PIE3 | 0x4A1 | TMR0IE, CCP1IE, TMR1GIE, TMR1IE, TMR2IE, SPI1IE, SPI1TXIE, SPI1RXIE |
| PIE4 | 0x4A2 | PWM1IE, PWM1PIE, —, —, —, U1IE, U1EIE, U1TXIE, U1RXIE |
| PIE5 | 0x4A3 | PWM2IE, PWM2PIE, TMR3GIE, TMR3IE, —, SPI2IE, SPI2TXIE, SPI2RXIE |
| PIE6 | 0x4A4 | DMA2AIE, DMA2ORIE, DMA2DCNTIE, DMA2SCNTIE, NCO1IE, CWG1IE, CLC2IE, INT1IE |
| PIE7 | 0x4A5 | PWM3IE, PWM3PIE, CLC3IE, —, I2C1EIE, I2C1IE, I2C1TXIE, I2C1RXIE |
| PIE8 | 0x4A6 | SCANIE, CCP2IE, TMR5GIE, TMR5IE, U2IE, U2EIE, U2TXIE, U2RXIE |
| PIE9 | 0x4A7 | —, —, CLC4IE, —, U3IE, U3EIE, U3TXIE, U3RXIE |
| PIE10 | 0x4A8 | DMA3AIE, DMA3ORIE, DMA3DCNTIE, DMA3SCNTIE, NCO2IE, CWG2IE, CLC5IE, INT2IE |
| PIE11 | 0x4A9 | DMA4AIE, DMA4ORIE, DMA4DCNTIE, DMA4SCNTIE, TMR4IE, CWG3IE, CLC6IE, CCP3IE |
| PIE12 | 0x4AA | DMA5AIE, DMA5ORIE, DMA5DCNTIE, DMA5SCNTIE, U4IE, U4EIE, U4TXIE, U4RXIE |
| PIE13 | 0x4AB | DMA6AIE, DMA6ORIE, DMA6DCNTIE, DMA6SCNTIE, U5IE, U5EIE, U5TXIE, U5RXIE |
| PIE14 | 0x4AC | —, —, —, —, NCO3IE, CM2IE, CLC7IE, — |
| PIE15 | 0x4AD | —, —, —, —, TMR6IE, CRCIE, CLC8IE, NVMIE |

## PIR Register Bit Maps

| Reg | Addr | Bits [7:0] |
|-----|------|-------------|
| PIR0 | 0x4AE | IOCIF(R), —, CLC1IF, —, CSWIF(R), OSFIF, HLVDIF, SWIF |
| PIR1 | 0x4AF | SMT1PWAIF, SMT1PRAIF, SMT1IF, CM1IF, ACTIF, ADIF, ZCDIF, INT0IF |
| PIR2 | 0x4B0 | DMA1AIF, DMA1ORIF, DMA1DCNTIF, DMA1SCNTIF, —, —, —, ADTIF |
| PIR3 | 0x4B1 | TMR0IF, CCP1IF, TMR1GIF, TMR1IF, TMR2IF, SPI1IF(R), SPI1TXIF(R), SPI1RXIF(R) |
| PIR4 | 0x4B2 | PWM1IF(R), PWM1PIF, —, —, —, U1IF(R), U1EIF(R), U1TXIF(R), U1RXIF(R) |
| PIR5 | 0x4B3 | PWM2IF(R), PWM2PIF, TMR3GIF, TMR3IF, —, SPI2IF(R), SPI2TXIF(R), SPI2RXIF(R) |
| PIR6 | 0x4B4 | DMA2AIF, DMA2ORIF, DMA2DCNTIF, DMA2SCNTIF, NCO1IF, CWG1IF, CLC2IF, INT1IF |
| PIR7 | 0x4B5 | PWM3IF(R), PWM3PIF, CLC3IF, —, I2C1EIF(R), I2C1IF(R), I2C1TXIF(R), I2C1RXIF(R) |
| PIR8 | 0x4B6 | SCANIF, CCP2IF, TMR5GIF, TMR5IF, U2IF(R), U2EIF(R), U2TXIF(R), U2RXIF(R) |
| PIR9 | 0x4B7 | —, —, CLC4IF, —, U3IF(R), U3EIF(R), U3TXIF(R), U3RXIF(R) |
| PIR10 | 0x4B8 | DMA3AIF, DMA3ORIF, DMA3DCNTIF, DMA3SCNTIF, NCO2IF, CWG2IF, CLC5IF, INT2IF |
| PIR11 | 0x4B9 | DMA4AIF, DMA4ORIF, DMA4DCNTIF, DMA4SCNTIF, TMR4IF, CWG3IF, CLC6IF, CCP3IF |
| PIR12 | 0x4BA | DMA5AIF, DMA5ORIF, DMA5DCNTIF, DMA5SCNTIF, U4IF(R), U4EIF(R), U4TXIF(R), U4RXIF(R) |
| PIR13 | 0x4BB | DMA6AIF, DMA6ORIF, DMA6DCNTIF, DMA6SCNTIF, U5IF(R), U5EIF(R), U5TXIF(R), U5RXIF(R) |
| PIR14 | 0x4BC | —, —, —, —, NCO3IF, CM2IF, CLC7IF, — |
| PIR15 | 0x4BD | —, —, —, —, TMR6IF, CRCIF, CLC8IF, NVMIF |

(R) = read-only flag; clear via peripheral register, not by direct write to PIR bit.

## IPR Register Bit Maps (default all 1 = high priority)

| Reg | Addr | Bits [7:0] (1=High, 0=Low) |
|-----|------|------------------------------|
| IPR0 | 0x362 | IOCIP, —, CLC1IP, —, CSWIP, OSFIP, HLVDIP, SWIP |
| IPR1 | 0x363 | SMT1PWAIP, SMT1PRAIP, SMT1IP, CM1IP, ACTIP, ADIP, ZCDIP, INT0IP |
| IPR2 | 0x364 | DMA1AIP, DMA1ORIP, DMA1DCNTIP, DMA1SCNTIP, —, —, —, ADTIP |
| IPR3 | 0x365 | TMR0IP, CCP1IP, TMR1GIP, TMR1IP, TMR2IP, SPI1IP, SPI1TXIP, SPI1RXIP |
| IPR4 | 0x366 | PWM1IP, PWM1PIP, —, —, —, U1IP, U1EIP, U1TXIP, U1RXIP |
| IPR5 | 0x367 | PWM2IP, PWM2PIP, TMR3GIP, TMR3IP, —, SPI2IP, SPI2TXIP, SPI2RXIP |
| IPR6 | 0x368 | DMA2AIP, DMA2ORIP, DMA2DCNTIP, DMA2SCNTIP, NCO1IP, CWG1IP, CLC2IP, INT1IP |
| IPR7 | 0x369 | PWM3IP, PWM3PIP, CLC3IP, —, I2C1EIP, I2C1IP, I2C1TXIP, I2C1RXIP |
| IPR8 | 0x36A | SCANIP, CCP2IP, TMR5GIP, TMR5IP, U2IP, U2EIP, U2TXIP, U2RXIP |
| IPR9 | 0x36B | —, —, CLC4IP, —, U3IP, U3EIP, U3TXIP, U3RXIP |
| IPR10 | 0x36C | DMA3AIP, DMA3ORIP, DMA3DCNTP, DMA3SCNTIP, NCO2IP, CWG2IP, CLC5IP, INT2IP |
| IPR11 | 0x36D | DMA4AIP, DMA4ORIP, DMA4DCNTIP, DMA4SCNTIP, TMR4IP, CWG3IP, CLC6IP, CCP3IP |
| IPR12 | 0x36E | DMA5AIP, DMA5ORIP, DMA5DCNTIP, DMA5SCNTIP, U4IP, U4EIP, U4TXIP, U4RXIP |
| IPR13 | 0x36F | DMA6AIP, DMA6ORIP, DMA6DCNTIP, DMA6SCNTIP, U5IP, U5EIP, U5TXIP, U5RXIP |
| IPR14 | 0x370 | —, —, —, —, NCO3IP, CM2IP, CLC7IP, — |
| IPR15 | 0x371 | —, —, —, —, TMR6IP, CRCIP, CLC8IP, NVMIP |

### Read-Only Flag Clearing Summary

| Flag | Clear Method |
|------|-------------|
| IOCIF | Clear all bits in IOCAF/IOCBF/IOCCF |
| CSWIF | Cannot wake from Sleep |
| SPIxIF | Clear all bits in SPIxINTF |
| SPIxTXIF, SPIxRXIF | Hardware-only; cannot be set/cleared by software |
| I2CxTXIF, I2CxRXIF | Set CLRBF bit in I2CxSTAT1 |
| I2CxIF | Clear all bits in I2CxPIR |
| I2CxEIF | Clear all bits in I2CxERR |
| UxIF | Clear all bits in UxUIR |
| UxEIF | Clear all bits in UxERRIR |
| UxTXIF, UxRXIF | Hardware-only; cannot be set/cleared by software |
| PWMxIF | Clear all bits in PWMxGIR |
| SWIF | Set and cleared by user software only |

## Shadow Registers (SHADCON)

- **SHADLO** (SHADCON bit 0): selects which context's shadow registers are accessible
  - 0 = Access low-priority ISR context
  - 1 = Access main routine context
- Shadow registers hold: STATUS, WREG, BSR, FSR0, FSR1, FSR2, PRODL, PRODH, PCLATH, PCLATU
- Two levels deep (main + low ISR); when IPEN=0 only main context is saved
- **RETFIE 1** (FAST): restores saved context; **RETFIE 0**: does NOT restore context

## Enabling an Interrupt

1. Set IPEN in INTCON0 (enables 2-level priority; all sources default high)
2. Set IPRx bit to choose High (1, default) or Low (0) priority
3. Clear the PIRx flag for the source
4. Set the PIEx enable bit for the source
5. Set IVTBASE if not using default (0x0008); then lock with IVTLOCKED
6. Set GIEH=1 in INTCON0
7. Set GIEL=1 in INTCON0 (for low-priority)

## Q43-Specific Notes

- **PWM modules**: Q43 has PWM1–3 with PWMxIF (parameter) and PWMxPIF (period) interrupts — differs from K42 CCP-only
- **DMA channels**: 6 DMA channels (DMA1–6) with SCNT/DCNT/OR/A abort/overrun/count interrupts
- **UART5**: Q43 adds U5 interrupts (PIE13/PIR13)
- **No NVM interrupt in PIE0**: Q43 has NVM at vector 0x78 via PIE15
- **CSWIF** cannot wake from Sleep
- If vector table entry or ISR address lies outside executable PFM (or in SAF when SAFEN=1), system reset occurs and MEMV bit in PCON1 is cleared
- When IVT1WAY=1, IVTLOCKED can only be cleared once after reset