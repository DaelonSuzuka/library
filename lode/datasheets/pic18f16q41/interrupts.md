# PIC18F16Q41 — Interrupt System (VIC)

## VIC Overview

The Vectored Interrupt Controller (VIC) consolidates all peripheral interrupt requests into a single CPU
interrupt request. Key features:

- **Fixed 2-cycle latency** (MVECEN=0) or **3-cycle latency** (MVECEN=1, vectored mode) from end of
  current instruction to first ISR instruction
- **Two priority levels**: High and Low (enabled via IPEN in INTCON0)
- **Interrupt Vector Table (IVT)** with unique vector per source (MVECEN=1) or single-polling mode (MVECEN=0)
- **Two-level context saving**: Main routine + Low-ISR context auto-saved/restored (STATUS, WREG, BSR,
  FSR0/1/2, PRODL/H, PCLATH/U, PC)
- WREG receives the resolved vector number upon interrupt entry

## Interrupt Vector Table (IVT)

- Base address register: **IVTBASE** (default `0x0008` for PIC18), must be even
- Vector address = `IVTBASE + (2 × Vector Number)` when MVECEN=1
- IVT range: `IVTBASE` to `IVTBASE + 2n - 1` (n = max vector number + 1)
- IVTBASE is lockable via IVTLOCK (unlock sequence: write 0x55, 0xAA to IVTLOCK then clear IVTLOCKED;
  requires GIE=0 beforehand)
- IVT1WAY config bit: if set, IVTLOCKED can only be unlocked once after reset

### Key Vector Numbers & XC8 IRQ Names

| Vec | XC8 IRQ | Source | Vec | XC8 IRQ | Source |
|---:|:--------|:-------|---:|:--------|:-------|
| 0 | IRQ_SWINT | Software | 30 | IRQ_CCP1 | CCP1 |
| 1 | IRQ_HLVD | HLVD | 31 | IRQ_TMR0 | TMR0 |
| 2 | IRQ_OSF | Osc Fail | 32 | IRQ_U1RX | UART1 RX |
| 3 | IRQ_CSW | Clock Switch | 35 | IRQ_U1 | UART1 |
| 4 | IRQ_NVMIP | NVM | 36 | IRQ_TMR3 | TMR3 |
| 5 | IRQ_CLC1 | CLC1 | 39 | IRQ_PWM1 | PWM1 |
| 6 | IRQ_CRC | CRC | 44 | IRQ_CMP2 | CMP2 |
| 7 | IRQ_IOC | IOC | 45 | IRQ_CLC2 | CLC2 |
| 8 | IRQ_INT0 | INT0 | 48 | IRQ_INT1 | INT1 |
| 9 | IRQ_ZCD | ZCD | 50 | IRQ_NCO1 | NCO1 |
| 10 | IRQ_AD | ADC | 56 | IRQ_I2C1RX | I2C1 RX |
| 11 | IRQ_ACT | ACT | 58 | IRQ_I2C1 | I2C1 |
| 12 | IRQ_CMP1 | CMP1 | 59 | IRQ_I2C1E | I2C1 Error |
| 13 | IRQ_SMT1 | SMT1 | 61 | IRQ_CLC3 | CLC3 |
| 16 | IRQ_ADT | ADC Thresh | 64 | IRQ_U2RX | UART2 RX |
| 20 | IRQ_DMA1SCNT | DMA1 SCNT | 67 | IRQ_U2 | UART2 |
| 24 | IRQ_SPI1RX | SPI1 RX | 69 | IRQ_CLC4 | CLC4 |
| 26 | IRQ_SPI1 | SPI1 | 71 | IRQ_SCAN | Scanner |
| 27 | IRQ_TMR2 | TMR2 | 72 | IRQ_U3RX | UART3 RX |
| 28 | IRQ_TMR1 | TMR1 | 75 | IRQ_U3 | UART3 |
| 29 | IRQ_TMR1G | TMR1 Gate | 80 | IRQ_INT2 | INT2 |
|  |  |  | 83 | IRQ_TMR4 | TMR4 |

Natural order priority: lower vector number = higher hardware priority. Used to break ties when
multiple same-user-priority interrupts are pending concurrently.

## Enabling an Interrupt

1. **Set IPEN** in INTCON0 (enables 2-level priority; default after reset: all sources high priority)
2. **Set IPRx bit** to choose High (1, default) or Low (0) priority for the source
3. **Clear the PIRx flag** for the source (prevent spurious entry)
4. **Set the PIEx enable bit** for the source
5. **Set IVTBASE** if not using default (0x0008); then lock with IVTLOCKED
6. **Set GIEH=1** in INTCON0 (enables high-priority interrupts; also required for low-priority)
7. **Set GIEL=1** in INTCON0 (enables low-priority interrupts; requires GIEH=1 as well)

When IPEN=0: GIE/GIEH controls all interrupts; no priority distinction. All vector to IVTBASE.

### XC8 ISR Syntax

```c
void __interrupt(irq(IRQ_TMR0), base(0x3008)) TMR0_ISR(void) {
    PIR3bits.TMR0IF = 0;
    // ISR body
}
void __interrupt(irq(default), base(0x3008)) DEFAULT_ISR(void) {
    // unhandled interrupts
}
```

## Control Register Map

| Register | Addr | Function |
|----------|------|----------|
| INTCON0 | 0x4D6 | GIE/GIEH (b7), GIEL (b6), IPEN (b5), INT2EDG (b2), INT1EDG (b1), INT0EDG (b0) |
| INTCON1 | 0x4D7 | STAT[1:0] (b7:6) — 00=Main, 01=Low ISR, 10=High ISR, 11=High ISR in Low ISR |
| IVTBASE | 0x45D | 21-bit IVT base address (U/H/L bytes) |
| IVTAD | 0x45A | Read-only: resolved vector table address (auto-loaded on interrupt) |
| IVTLOCK | 0x459 | IVTLOCKED (b0): 1=locked, 0=writable (special unlock sequence required) |
| SHADCON | 0x376 | SHADLO (b0): 0=access low-ISR context, 1=access main context in shadow regs |

## PIE / PIR / IPR Register Triads

Each interrupt source has a matching bit across the three register families. All registers are 8-bit.

| Reg | Addr | Bits [7:0] |
|-----|------|-------------|
| PIE0 | 0x4A8 | IOCIE, CRCIE, CLC1IE, NVMIE, CSWIE, OSFIE, HLVDIE, SWIE |
| PIE1 | 0x4A9 | SMT1PWAIE, SMT1PRAIE, SMT1IE, CM1IE, ACTIE, ADIE, ZCDIE, INT0IE |
| PIE2 | 0x4AA | DMA1AIE, DMA1ORIE, DMA1DCNTIE, DMA1SCNTIE, —, —, —, ADTIE |
| PIE3 | 0x4AB | TMR0IE, CCP1IE, TMR1GIE, TMR1IE, TMR2IE, SPI1IE, SPI1TXIE, SPI1RXIE |
| PIE4 | 0x4AC | PWM1IE, PWM1PIE, TMR3GIE, TMR3IE, U1IE, U1EIE, U1TXIE, U1RXIE |
| PIE5 | 0x4AD | PWM2IE, PWM2PIE, CLC2IE, CM2IE, —, SPI2IE, SPI2TXIE, SPI2RXIE |
| PIE6 | 0x4AE | DMA2AIE, DMA2ORIE, DMA2DCNTIE, DMA2SCNTIE, NCO1IE, CWG1IE, —, INT1IE |
| PIE7 | 0x4AF | PWM3IE, PWM3PIE, CLC3IE, —, I2C1EIE, I2C1IE, I2C1TXIE, I2C1RXIE |
| PIE8 | 0x4B0 | SCANIE, —, CLC4IE, —, U2IE, U2EIE, U2TXIE, U2RXIE |
| PIE9 | 0x4B1 | DMA3AIE, DMA3ORIE, DMA3DCNTIE, DMA3SCNTIE, U3IE, U3EIE, U3TXIE, U3RXIE |
| PIE10| 0x4B2 | DMA4AIE, DMA4ORIE, DMA4DCNTIE, DMA4SCNTIE, TMR4IE, —, —, INT2IE |

| Reg | Addr | Bits [7:0] |
|-----|------|-------------|
| PIR0 | 0x4B3 | IOCIF(R), CRCIF, CLC1IF, NVMIF, CSWIF, OSFIF, HLVDIF, SWIF |
| PIR1 | 0x4B4 | SMT1PWAIF, SMT1PRAIF, SMT1IF, CM1IF, ACTIF, ADIF, ZCDIF, INT0IF |
| PIR2 | 0x4B5 | DMA1AIF, DMA1ORIF, DMA1DCNTIF, DMA1SCNTIF, —, —, —, ADTIF |
| PIR3 | 0x4B6 | TMR0IF, CCP1IF, TMR1GIF, TMR1IF, TMR2IF, SPI1IF(R), SPI1TXIF(R), SPI1RXIF(R) |
| PIR4 | 0x4B7 | PWM1IF(R), PWM1PIF, TMR3GIF, TMR3IF, U1IF(R), U1EIF(R), U1TXIF(R), U1RXIF(R) |
| PIR5 | 0x4B8 | PWM2IF(R), PWM2PIF, CLC2IF, CM2IF, —, SPI2IF(R), SPI2TXIF(R), SPI2RXIF(R) |
| PIR6 | 0x4B9 | DMA2AIF, DMA2ORIF, DMA2DCNTIF, DMA2SCNTIF, NCO1IF, CWG1IF, —, INT1IF |
| PIR7 | 0x4BA | PWM3IF(R), PWM3PIF, CLC3IF, —, I2C1EIF(R), I2C1IF(R), I2C1TXIF(R), I2C1RXIF(R) |
| PIR8 | 0x4BB | SCANIF, —, CLC4IF, —, U2IF(R), U2EIF(R), U2TXIF(R), U2RXIF(R) |
| PIR9 | 0x4BC | DMA3AIF, DMA3ORIF, DMA3DCNTIF, DMA3SCNTIF, U3IF(R), U3EIF(R), U3TXIF(R), U3RXIF(R) |
| PIR10| 0x4BD | DMA4AIF, DMA4ORIF, DMA4DCNTIF, DMA4SCNTIF, TMR4IF, —, —, INT2IF |

| Reg | Addr | Bits [7:0] (1=High, 0=Low priority) |
|-----|------|--------------------------------------|
| IPR0 | 0x367 | IOCIP, CRCIP, CLC1IP, NVMIP, CSWIP, OSFIP, HLVDIP, SWIP |
| IPR1 | 0x368 | SMT1PWAIP, SMT1PRAIP, SMT1IP, CM1IP, ACTIP, ADIP, ZCDIP, INT0IP |
| IPR2 | 0x369 | DMA1AIP, DMA1ORIP, DMA1DCNTIP, DMA1SCNTIP, —, —, —, ADTIP |
| IPR3 | 0x36A | TMR0IP, CCP1IP, TMR1GIP, TMR1IP, TMR2IP, SPI1IP, SPI1TXIP, SPI1RXIP |
| IPR4 | 0x36B | PWM1IP, PWM1PIP, TMR3GIP, TMR3IP, U1IP, U1EIP, U1TXIP, U1RXIP |
| IPR5 | 0x36C | PWM2IP, PWM2PIP, CLC2IP, CMI2P, —, SPI2IP, SPI2TXIP, SPI2RXIP |
| IPR6 | 0x36D | DMA2AIP, DMA2ORIP, DMA2DCNTIP, DMA2SCNTIP, NCO1IP, CWG1IP, —, INT1IP |
| IPR7 | 0x36E | PWM3IP, PWM3PIP, CLC3IP, —, I2C1EIP, I2C1IP, I2C1TXIP, I2C1RXIP |
| IPR8 | 0x36F | SCANIP, —, CLC4IP, —, U2IP, U2EIP, U2TXIP, U2RXIP |
| IPR9 | 0x370 | DMA3AIP, DMA3ORIP, DMA3DCNTIP, DMA3SCNTIP, U3IP, U3EIP, U3TXIP, U3RXIP |
| IPR10| 0x371 | DMA4AIP, DMA4ORIP, DMA4DCNTIP, DMA4SCNTIP, TMR4IP, —, —, INT2IP |

(R) = read-only flag; clear via peripheral register, not by direct write to PIR bit.

## Interrupt-on-Change (IOC)

IOC is vector number 7 (IRQ_IOC), enabled by IOCIE in PIE0, flagged by IOCIF (read-only) in PIR0.
IOCIF cannot be cleared directly — all bits in the port-specific IOCAF/IOCBF/IOCCF registers must be
cleared instead.

### Key IOC Registers

| Register | Addr | Function |
|----------|------|----------|
| IOCAP | 0x405 | Port A positive-edge enable |
| IOCAN | 0x406 | Port A negative-edge enable |
| IOCAF | 0x407 | Port A flag (clear to clear IOCIF) |
| IOCBP | 0x40D | Port B positive-edge enable |
| IOCBN | 0x40E | Port B negative-edge enable |
| IOCBF | 0x40F | Port B flag |
| IOCCP | 0x415 | Port C positive-edge enable |
| IOCCN | 0x416 | Port C negative-edge enable |
| IOCCF | 0x417 | Port C flag |

IOC priority via IOCIP (IPR0 bit 7, default high). IOC interacts with VIC like any other interrupt
source once IOCIF is set.

## External Interrupts (INT0/INT1/INT2)

- Edge-select via INT0EDG/INT1EDG/INT2EDG in INTCON0 (1=rising, 0=falling, default=1)
- Pin assignment via PPS (INTxPPS registers)
- Flags (INT0IF/INT1IF/INT2IF) must be cleared by software before re-enabling
- Can wake from Sleep/Idle if INTxE is set prior to entering low-power mode

## Priority Behavior

- High-priority interrupts preempt low-priority ISRs; low cannot preempt high
- Same-priority concurrent interrupts resolved by natural order (lower vector number wins)
- GIEH/GIEL are NOT auto-modified by hardware on ISR entry — the internal state machine tracks context
- RETFIE 1 restores saved context; RETFIE 0 does not