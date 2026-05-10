# PIC18F26K42 — Interrupt System (VIC)

## VIC Overview

The Vectored Interrupt Controller (VIC) consolidates all peripheral interrupt requests into a single CPU
interrupt request. Key features:

- **Fixed 3-cycle latency** (MVECEN=1, vectored mode) or **2-cycle latency** (MVECEN=0, compat mode) from end
  of current instruction to first ISR instruction
- **Two priority levels**: High and Low (enabled via IPEN in INTCON0)
- **Interrupt Vector Table (IVT)** with unique vector per source (MVECEN=1) or single-polling mode (MVECEN=0)
- **Two-level context saving**: Main routine + Low-ISR context auto-saved/restored (STATUS, WREG, BSR,
  FSR0/1/2, PRODL/H, PCLATH/U, PC)
- WREG receives the resolved vector number upon interrupt entry
- **82 interrupt vectors** (vector numbers 0–81)

## IVTBASE and Vector Table Setup

- Base address register: **IVTBASE** (21-bit, spanning IVTBASEU/H/L), default `0x000008`
- IVTBASE **must be even** for correct operation
- Vector address = `IVTBASE + (2 × Vector Number)` when MVECEN=1
- When MVECEN=0, IPEN=1: high-priority vector at IVTBASE, low-priority at IVTBASE+8 words
- When MVECEN=0, IPEN=0: all interrupts vector to IVTBASE (compat mode)
- IVT range: `IVTBASE` to `IVTBASE + 0xA2` must fit within program flash (highest vector=81, so 2×81=0xA2)

### IVTBASE Lock (IVTLOCK)

- **IVTLOCKED** bit in IVTLOCK register controls write access to IVTBASE
- Unlock sequence (requires GIE=0):
  ```
  MOVLW 0x55; MOVWF IVTLOCK
  MOVLW 0xAA; MOVWF IVTLOCK
  BCF   IVTLOCK, IVTLOCKED
  ```
- Lock sequence:
  ```
  MOVLW 0x55; MOVWF IVTLOCK
  MOVLW 0xAA; MOVWF IVTLOCK
  BSF   IVTLOCK, IVTLOCKED
  ```
- **IVT1WAY** config bit (CONFIG2L[4]): if set, IVTLOCKED can only be cleared/locked once after reset

### Configuration Bits (CONFIG2L)

| Bit | Field | Description |
|-----|-------|-------------|
| 4 | IVT1WAY | 1=IVTLOCK set/clear once only after reset |
| 3 | MVECEN | 1=Multi-vector interrupt mode enabled |

## Interrupt Vector Addresses (Default IVTBASE=0x0008)

When MVECEN=0, IPEN=1:
- High priority → IVTBASE (default 0x0008)
- Low priority → IVTBASE + 8 words (default 0x0018)

When MVECEN=1: Vector address = IVTBASE + 2×VectorNumber

## Vector Number Table

| Vec | Source | Vec | Source | Vec | Source | Vec | Source |
|----:|:------|----:|:------|----:|:------|----:|:------|
| 0 | SWINT | 21 | SPI1TX | 42 | DMA2SCNT | 63 | — |
| 1 | HLVD | 22 | SPI1 | 43 | DMA2DCNT | 64 | — |
| 2 | OSF | 23 | I2C1RX | 44 | DMA2OR | 65 | — |
| 3 | CSW | 24 | I2C1TX | 45 | DMA2A | 66 | — |
| 4 | NVM | 25 | I2C1 | 46 | I2C2RX | 67 | — |
| 5 | SCAN | 26 | I2C1E | 47 | I2C2TX | 68 | — |
| 6 | CRC | 27 | U1RX | 48 | I2C2 | 69 | — |
| 7 | IOC | 28 | U1TX | 49 | I2C2E | 70 | TMR5 |
| 8 | INT0 | 29 | U1E | 50 | U2RX | 71 | TMR5G |
| 9 | ZCD | 30 | U1 | 51 | U2TX | 72 | TMR6 |
| 10 | AD | 31 | TMR0 | 52 | U2E | 73 | CCP3 |
| 11 | ADT | 32 | TMR1 | 53 | U2 | 74 | CWG3 |
| 12 | C1 | 33 | TMR1G | 54 | TMR3 | 75 | CLC3 |
| 13 | SMT1 | 34 | TMR2 | 55 | TMR3G | 76 | — |
| 14 | SMT1PRA | 35 | CCP1 | 56 | TMR4 | 77 | — |
| 15 | SMT1PWA | 36 | — | 57 | CCP2 | 78 | — |
| 16 | DMA1SCNT | 37 | NCO | 58 | — | 79 | — |
| 17 | DMA1DCNT | 38 | CWG1 | 59 | CWG2 | 80 | CCP4 |
| 18 | DMA1OR | 39 | CLC1 | 60 | CLC2 | 81 | CLC4 |
| 19 | DMA1A | 40 | INT1 | 61 | INT2 | | |
| 20 | SPI1RX | 41 | C2 | 62 | — | | |

Natural order priority: lower vector number = higher hardware priority. Ties among same-user-priority
interrupts are broken by natural order.

## Priority Levels

- **IPEN** (INTCON0 bit 5) enables 2-level priority; after reset all sources default to high priority
- **IPR x registers**: each bit = 1 → High priority, 0 → Low priority (all default to 1 after reset)
- High-priority interrupts preempt low-priority ISRs; same-priority interrupts cannot preempt each other
- **GIEH** (INTCON0 bit 7): enables all high-priority interrupts (also required for low-priority)
- **GIEL** (INTCON0 bit 6): enables all low-priority interrupts (requires GIEH=1)
- When IPEN=0: GIE/GIEH controls all interrupts; no priority distinction
- GIEH/GIEL are **not auto-modified by hardware** on ISR entry; internal state machine tracks context
- **INTCON1 STAT[1:0]**: 00=Main, 01=Low ISR, 10=High ISR from main, 11=High ISR preempting Low ISR

## Control Register Map

| Register | Addr | Key Bits |
|----------|------|----------|
| INTCON0 | 0x4D6 | GIE/GIEH(b7), GIEL(b6), IPEN(b5), INT2EDG(b2), INT1EDG(b1), INT0EDG(b0) |
| INTCON1 | 0x4D7 | STAT[1:0](b7:6) — CPU interrupt state |
| IVTBASEU | — | BASE[20:16] |
| IVTBASEH | — | BASE[15:8] |
| IVTBASEL | — | BASE[7:0] (reset=0x08) |
| IVTAD | — | Read-only: auto-loaded vector address on interrupt |
| IVTLOCK | — | IVTLOCKED(b0) — lock IVTBASE writes |
| SHADCON | 0x376 | SHADLO(b0) — select shadow register context |

## PIE / PIR / IPR Register Triads

Each interrupt source has matching bit across PIE (enable), PIR (flag), IPR (priority). All 8-bit.

| Reg | Addr | Bits [7:0] |
|-----|------|-------------|
| PIE0 | — | IOCIE, CRCIE, SCANIE, NVMIE, CSWIE, OSFIE, HLVDIE, SWIE |
| PIE1 | — | SMT1PWAIE, SMT1PRAIE, SMT1IE, C1IE, ADTIE, ADIE, ZCDIE, INT0IE |
| PIE2 | — | I2C1RXIE, SPI1IE, SPI1TXIE, SPI1RXIE, DMA1AIE, DMA1ORIE, DMA1DCNTIE, DMA1SCNTIE |
| PIE3 | — | TMR0IE, U1IE, U1EIE, U1TXIE, U1RXIE, I2C1EIE, I2C1IE, I2C1TXIE |
| PIE4 | — | CLC1IE, CWG1IE, NCO1IE, —, CCP1IE, TMR2IE, TMR1GIE, TMR1IE |
| PIE5 | — | I2C2TXIE, I2C2RXIE, DMA2AIE, DMA2ORIE, DMA2DCNTIE, DMA2SCNTIE, C2IE, INT1IE |
| PIE6 | — | TMR3GIE, TMR3IE, U2IE, U2EIE, U2TXIE, U2RXIE, I2C2EIE, I2C2IE |
| PIE7 | — | —, —, INT2IE, CLC2IE, CWG2IE, —, CCP2IE, TMR4IE |
| PIE8 | — | TMR5GIE, TMR5IE, —, —, —, —, —, — |
| PIE9 | — | —, —, —, —, CLC3IE, CWG3IE, CCP3IE, TMR6IE |
| PIE10 | — | —, —, —, —, —, —, CLC4IE, CCP4IE |

| Reg | Addr | Bits [7:0] |
|-----|------|-------------|
| PIR0 | — | IOCIF(R), CRCIF, SCANIF, NVMIF, CSWIF(R), OSFIF, HLVDIF, SWIF |
| PIR1 | — | SMT1PWAIF, SMT1PRAIF, SMT1IF, C1IF, ADTIF, ADIF, ZCDIF, INT0IF |
| PIR2 | — | I2C1RXIF(R), SPI1IF(R), SPI1TXIF(R), SPI1RXIF(R), DMA1AIF, DMA1ORIF, DMA1DCNTIF, DMA1SCNTIF |
| PIR3 | — | TMR0IF, U1IF(R), U1EIF(R), U1TXIF(R), U1RXIF(R), I2C1EIF(R), I2C1IF(R), I2C1TXIF(R) |
| PIR4 | — | CLC1IF, CWG1IF, NCO1IF, —, CCP1IF, TMR2IF, TMR1GIF, TMR1IF |
| PIR5 | — | I2C2TXIF(R), I2C2RXIF(R), DMA2AIF, DMA2ORIF, DMA2DCNTIF, DMA2SCNTIF, C2IF, INT1IF |
| PIR6 | — | TMR3GIF, TMR3IF, U2IF(R), U2EIF(R), U2TXIF(R), U2RXIF(R), I2C2EIF(R), I2C2IF(R) |
| PIR7 | — | —, —, INT2IF, CLC2IF, CWG2IF, —, CCP2IF, TMR4IF |
| PIR8 | — | TMR5GIF, TMR5IF, —, —, —, —, —, — |
| PIR9 | — | —, —, —, —, CLC3IF, CWG3IF, CCP3IF, TMR6IF |
| PIR10 | — | —, —, —, —, —, —, CLC4IF, CCP4IF |

| Reg | Addr | Bits [7:0] (1=High, 0=Low priority) |
|-----|------|--------------------------------------|
| IPR0 | — | IOCIP, CRCIP, SCANIP, NVMIP, CSWIP, OSFIP, HLVDIP, SWIP |
| IPR1 | — | SMT1PWAIP, SMT1PRAIP, SMT1IP, C1IP, ADTIP, ADIP, ZCDIP, INT0IP |
| IPR2 | — | I2C1RXIP, SPI1IP, SPI1TXIP, SPI1RXIP, DMA1AIP, DMA1ORIP, DMA1DCNTIP, DMA1SCNTIP |
| IPR3 | — | TMR0IP, U1IP, U1EIP, U1TXIP, U1RXIP, I2C1EIP, I2C1IP, I2C1TXIP |
| IPR4 | — | CLC1IP, CWG1IP, NCO1IP, —, CCP1IP, TMR2IP, TMR1GIP, TMR1IP |
| IPR5 | — | I2C2TXIP, I2C2RXIP, DMA2AIP, DMA2ORIP, DMA2DCNTIP, DMA2SCNTIP, C2IP, INT1IP |
| IPR6 | — | TMR3GIP, TMR3IP, U2IP, U2EIP, U2TXIP, U2RXIP, I2C2EIP, I2C2IP |
| IPR7 | — | —, —, INT2IP, CLC2IP, CWG2IP, —, CCP2IP, TMR4IP |
| IPR8 | — | TMR5GIP, TMR5IP, —, —, —, —, —, — |
| IPR9 | — | —, —, —, —, CLC3IP, CWG3IP, CCP3IP, TMR6IP |
| IPR10 | — | —, —, —, —, —, —, CLC4IP (default 0!), CCP4IP (default 0!) |

(R) = read-only flag; clear via peripheral register, not by direct write to PIR bit.

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
| SWIF | Set and cleared by user software only |

## Shadow Registers (SHADCON)

- **SHADLO** (SHADCON bit 0): selects which context's shadow registers are accessible in Bank 56
  - 0 = Access main routine context
  - 1 = Access low-priority ISR context
- Shadow registers hold: STATUS, WREG, BSR, FSR0, FSR1, FSR2, PRODL, PRODH, PCLATH, PCLATU
- Context save/restore is automatic; two levels deep (main + low ISR)
- Shadow registers are readable/writable — modify to alter restored context
- When IPEN=0: only main context is saved (single level)
- Low ISR context is auto-restored on RETFIE from high ISR; main context restored on RETFIE from low ISR

## Context Saving

- PC is saved on the dedicated hardware stack (not on shadow registers)
- CPU registers (STATUS, WREG, BSR, FSR0/1/2, PRODL/H, PCLATH/U) are auto-saved to shadow registers
- After saving WREG, the resolved interrupt vector number is loaded into WREG
- **RETFIE 1** (FAST): restores saved context from shadow registers
- **RETFIE 0**: does NOT restore context — manual save/restore required if used

## Enabling an Interrupt

1. **Set IPEN** in INTCON0 (enables 2-level priority; default after reset: all sources high priority)
2. **Set IPRx bit** to choose High (1, default) or Low (0) priority
3. **Clear the PIRx flag** for the source (prevent spurious entry)
4. **Set the PIEx enable bit** for the source
5. **Set IVTBASE** if not using default (0x0008); then lock with IVTLOCKED
6. **Set GIEH=1** in INTCON0 (enables high-priority; also required for low-priority)
7. **Set GIEL=1** in INTCON0 (enables low-priority; requires GIEH=1)

### XC8 ISR Syntax

```c
void __interrupt(irq(IRQ_TMR0), base(0x4008)) TMR0_ISR(void) {
    PIR3bits.TMR0IF = 0;
    // ISR body
}
void __interrupt(irq(default), base(0x4008)) DEFAULT_ISR(void) {
    // unhandled interrupts
}
```

Note: If IVTBASE is changed from default, the `base(...)` argument must specify the new IVTBASE value.

## External Interrupts (INT0/INT1/INT2)

- Edge-select via INT0EDG/INT1EDG/INT2EDG in INTCON0 (1=rising, 0=falling, default=1)
- Pin assignment via PPS (INTxPPS registers)
- Flags (INT0IF/INT1IF/INT2IF) must be cleared by software before re-enabling
- Can wake from Sleep/Idle if INTxE is set prior to entering low-power mode

## Interrupt-on-Change (IOC)

- Vector number 7, enabled by IOCIE in PIE0, flagged by IOCIF (read-only) in PIR0
- IOCIF cannot be cleared directly — clear all bits in port-specific IOCAF/IOCBF/IOCCF registers instead

## K42-Specific Notes

- **IPR10 defaults differ**: CLC4IP and CCP4IP default to **0** (low priority) after reset, unlike all other IPR bits
  which default to 1 (high priority). This is a K42-specific anomaly.
- **No PWM modules**: K42 has no PWM interrupts (unlike Q41); uses CCP and CWG instead
- **No UART3/SPI2/TMR4 gate/CWG3 on all pin counts**: some PIR/PIE/IPR bits are unimplemented on smaller
  devices (PIE7/PIR7/IPR7 bits 7:6, PIE8/PIR8/IPR8 bits 5:0, PIE9/PIR9/IPR9 bits 7:4,
  PIE10/PIR10/IPR10 bits 7:2)
- **CSWIF** cannot wake from Sleep
- If vector table entry or ISR address lies outside executable PFM (or in SAF when SAFEN=1), a system reset
  occurs and MEMV bit in PCON1 is cleared
- When IVT1WAY=1, IVTLOCKED can only be cleared once after reset — subsequent unlock sequences have no effect