# PIC18F26K42/K42 Family — Memory & NVM Reference

## Device Variants and Memory Sizes

| Device | Program Flash | Data SRAM | Data EEPROM | Pins |
|---|---|---|---|---|
| PIC18F45/46K42 | 32KW (16KB) | 4KB | 256B | 40/44 |
| PIC18F26/46/56K42 | 64KW (32KB) | 4KB | 256B | 28/40/44 |
| PIC18F27/47/57K42 | 128KW (64KB) | 4KB | 1024B | 28/40/44 |

LF variants share same memory sizes, lower voltage range. PIC18F26/27K42: 28-pin, no PORTD/PORTE/LATD/LATE.

## Program Flash Memory Map

| Region | 26/46/56K42 | 27/47/57K42 |
|---|---|---|
| Reset Vector | 0x000000 | 0x000000 |
| IV High Vector | 0x000008 | 0x000008 |
| IV Low Vector | 0x000018 | 0x000018 |
| Program Flash | 0x00001A–0x007FFF (32KW) | 0x00001A–0x00FFFF (64KW) |
| Reserved | 0x008000–0x01FFFF | 0x010000–0x1FFFFF |
| User IDs | 0x200000–0x20000F (8 words) | same |
| Reserved | 0x200010–0x2FFFFF | same |
| Config Words | 0x300000–0x300009 (5 words) | same |
| Reserved | 0x30000A–0x30FFFF | same |
| Data EEPROM | 0x310000–0x3100FF (256B) | 0x310000–0x3103FF (1024B) |
| Reserved | 0x310100–0x3EFFFF / 0x310400–0x3EFFFF | same |
| DIA | 0x3F0000–0x3F003F | same |
| Reserved | 0x3F0040–0x3FFEFE | same |
| DCI | 0x3FFF00–0x3FFF09 (5 words) | same |
| Reserved | 0x3FFF0A–0x3FFFBF | same |
| Revision ID | 0x3FFFFC | same |
| Device ID | 0x3FFFFE | same |

PC is 21-bit (2MB address space). Unimplemented memory reads as NOP (all zeros). IVT base relocatable via IVTBASE register.

## Memory Access Partition (MAP)

Program Flash is partitioned into three regions controlled by config bits BBEN and SAFEN:

| BBEN | SAFEN | Partition Layout |
|---|---|---|
| 1 (disabled) | 1 (disabled) | All flash = Application Block |
| 1 (disabled) | 0 (enabled) | Application Block + SAF at end |
| 0 (enabled) | 1 (disabled) | Boot Block + Application Block |
| 0 (enabled) | 0 (enabled) | Boot Block + Application Block + SAF |

- **Application Block**: Default user code region. Write-protected by WRTAPP config bit.
- **Boot Block**: For bootloader code; executable by CPU. Size set by BBSIZE[2:0] config bits (see config section). Write-protected by WRTB config bit.
- **Storage Area Flash (SAF)**: Last 128 words of user flash when SAFEN=0. Non-executable (CPU cannot execute from SAF). Write-protected by WRTSAF config bit.

Write-protected locations: if written, memory is not changed and WRERR bit is set.

## Data SRAM Organization

- 4KB data SRAM (general purpose registers)
- 14-bit address space: up to 64 banks × 256 bytes = 16KB addressable
- **Bank 0**: GPR (0x0000–0x00FF)
- **Banks 1–15**: GPR (0x0100–0x0FFF) — for PIC18F26/27K42
- **Banks 16–31**: Unimplemented for 26/27K42; GPR for larger variants
- **Banks 32–55**: Unimplemented (all variants)
- **Bank 56**: Shadow/IVT registers (0x3800–0x38FF)
- **Banks 57–58**: PPS, peripheral SFRs (0x3900–0x3AFF)
- **Banks 59–60**: DMA, CLC, MD, timer SFRs (0x3B00–0x3CFF)
- **Banks 61**: UART, I2C, SPI SFRs (0x3D00–0x3DFF)
- **Bank 62**: Analog, comparator, DAC, CWG, PWM, CCP, timer SFRs (0x3E00–0x3EFF)
- **Bank 63**: Core SFRs (0x3F00–0x3FFF)

GPR (banks 0–15) = 4KB. Banks 32–55 unimplemented (read as 0, writes ignored).

## BSR and Banked Addressing

- **BSR (Bank Select Register)**: 6-bit field (BSR[5:0]), upper 2 bits unused/read-as-0
- Full data address = BSR[5:0] : offset[7:0] (14-bit address)
- MOVLB instruction loads BSR directly
- Instructions with `a=1` use BSR; `a=0` uses Access Bank
- Indirect addressing via FSR0/FSR1/FSR2 uses full 14-bit address (no banking)
- Unimplemented banks: reads return 0, writes ignored, STATUS still affected

## Access Bank (Virtual, No BSR Needed)

| Region | Addresses | Description |
|---|---|---|
| Access RAM (GPR) | 0x0000–0x005F | Lower 96 bytes of Bank 0 |
| SFR | 0x3F60–0x3FFF → mapped to 0x60–0xFF | Upper 160 bytes of Bank 63 |

Instruction bit `a=0` forces Access Bank; `a=1` uses BSR.

With XINST=1 (extended instruction set): `a=0` with offset ≤0x5F becomes indexed literal offset mode using FSR2 as base pointer. Offsets ≥0x60 still access SFR region normally.

## SFR Overview by Bank

### Bank 63 (0x3F00–0x3FFF) — Core Registers
Key registers: TOSU/TOSH/TOSL, STKPTR, PCLATU/PCLATH/PCL, TBLPTRU/TBLPTRH/TBLPTRL, TABLAT, PRODH/PRODL, PCON0/PCON1, BSR, WREG, FSR0/1/2 (H+L), INDF0/1/2, PLUSW/POSTINC/POSTDEC/PREINC for FSR0/1/2, STATUS, IVTBASE (U/H/L), IVTLOCK, INTCON0/INTCON1, TMR0/1/2/3/5/6, T0CON0/1, T1CON–T6CON, PORTA–F, TRISA–F, LATA–F, CCP1–4, PWM5–8, CWG1–3, NCO1, SMT1.

### Bank 62 (0x3E00–0x3EFF) — Analog & Comparators
ADCON0–3, ADREF, ADSTAT, ADCLK, ADACT, ADPREH/L, ADCAP, ADACQH/L, ADFLTRH/L, ADSTPTH/L, ADERRH/L, ADUTHH/L, ADLTHH/L, ADRESH/L, ADPREVH/L, ADRPT, ADCNT, ADACCU/H/L, CM1/2CON0/1, CM1/2PCH, CM1/2NCH, CMOUT, FVRCON, HLVDCON0/1, ZCDCON, DAC1CON0/1.

### Bank 61 (0x3D00–0x3DFF) — Serial & Comms
U1CON0–2, U1BRGH/L, U1RXB/TXB/RXCHK/TXCHK, U1P1L/H–P3L/H, U1UIR, U1ERRIR/ERRIE, U1FIFO (UART1); U2* (UART2); I2C1/2CON0–2, I2C1/2STAT0/1, I2C1/2ERR, I2C1/2ADR0–3, I2C1/2ADB0/1, I2C1/2CNT, I2C1/2TXB/RXB, I2C1/2CLK, I2C1/2BTO, I2C1/2PIE/PIR; SPI1CON0–2, SPI1BAUD, SPI1STATUS, SPI1CLK, SPI1INTE/INTF, SPI1TXB/RXB, SPI1TCNTH/L, SPI1TWIDTH.

### Bank 60 (0x3C00–0x3CFF) — Logic & Signal
CLC1–4 (CON, POL, SEL0–3, GLS0–3), CLCDATA0, MD1 (CON0/1, SRC, CARL/H), CLKRCLK, CLKRCON.

### Bank 59 (0x3B00–0x3BFF) — DMA
DMA1/2 (CON0/1, SSAU/H/L, SSZH/L, SPTRU/H/L, SCNTH/L, DSAH/L, DSZH/L, DPTRH/L, DCNTH/L, BUF, SIRQ, AIRQ).

### Bank 58 (0x3A00–0x3AFF) — PPS & I/O
PPS input selection (RA0–7PPS, RB0–7PPS, RC0–7PPS, RD0–7PPS, RE0–2PPS, RF0–7PPS, T0–6CKI/GPPS, INT0–2PPS, CCP1–4PPS, SMT1SIG/WINPPS, CWG1–3INPPS, T2–4INPPS, T5CKI/GPPS, SPI1SS/SDI/SCKPPS, I2C1/2SDA/SCLPPS, U1/2RX/CTSPPS, ADACTPPS, CLCIN0–3PPS, MD1SRC/CARL/CARHPPS, PPSLOCK, ANSELA–F, WPUB/C/D/E/F, ODCONA–F, SLRCONA–F, INLVLA–E, IOCAF/B/C/EF, RA0–7I2C, RB1–2I2C, RC3–4I2C, RD0–1I2C.

### Bank 57 (0x3900–0x39FF) — System Control
NVMCON1, NVMCON2, NVMDAT, NVMADRL, NVMADRH, PMD0–7, PIR0–10, PIE0–10, IPR0–10, PRLOCK, ISRPR, MAINPR, DMA1/2PR, SCANPR, BORCON, VREGCON, OSCCON1–3, OSCSTAT, OSCEN, OSCTUNE, OSCFRQ, CPUDOZE, SCANCON0, SCANHADRU/H/L, SCANLADRU/H/L, SCANTRIG, CRC modules, WDT registers.

### Bank 56 (0x3800–0x38FF) — Shadows & IVT
STATUS_CSHAD, WREG_CSHAD, BSR_CSHAD (CALL shadow regs); SHADCON; STATUS/WREG/BSR_SHAD (interrupt shadow regs); FSR0/1/2L/H_SHAD; PCLATH/PU_SHAD; PRODL/H_SHAD; IVTADU/IVTADH/IVTADL. Also holds DMA-mirrored registers at 0x4000+ (CPU-inaccessible, DMA-only).

## Stack

- 31-level hardware return stack (separate SRAM, not in program or data space)
- 5-bit Stack Pointer (STKPTR[4:0]), readable/writable, reset value = 0
- TOSU/TOSH/TOSL: 21-bit Top-of-Stack registers (readable/writable)
- PUSH increments STKPTR then loads PC; POP decrements STKPTR
- CALL/RCALL/CALLW push PC; RETURN/RETLW/RETFIE pop PC
- PCLATU/PCLATH not affected by CALL/RETURN instructions
- Stack overflow (32nd push): STVREN=1 → Reset, sets STKOVF; STVREN=0 → STKOVF set, STKPTR stays at 31, overwrite TOS
- Stack underflow: STVREN=1 → Reset, sets STKUNF, PC=0; STVREN=0 → STKUNF set, no Reset
- Fast Register Stack: 3 levels (1 for CALL, 2 for interrupts) saving STATUS, WREG, BSR
- CALL label, FAST / RETURN, FAST uses the fast register stack

## NVM Control Registers (Summary)

Full NVM details in NVM section (Section 13).

| Register | Addr (Access) | Description |
|---|---|---|
| NVMCON0 | — | GO bit (start op), bits for NVM control |
| NVMCON1 | — | WRERR (R/C/HS), NVMCMD[2:0] (R/W) |
| NVMCON2 | — | NVM unlock key register |
| NVMADRL | — | NVM address low byte |
| NVMADRH | — | NVM address high byte (see note for 27K42) |
| NVMDAT | — | NVM data register |
| TBLPTRU/H/L | 0x3FF8–0x3FF6 | Table pointer (21-bit + config flag) |
| TABLAT | 0x3FF5 | Table latch |

NVM commands: Read (000), Read+Inc (001), Write (011), Erase Page (110), etc. Unlock sequence required for writes: NVMCON2=0x55, NVMCON2=0xAA, GO=1. CPU stalls during flash write/erase.

**Note on NVMADRH**: For 27/47/57K42 (128KB flash), NVMADRH uses more bits to address the larger program space. See NVM section for specifics.

## Key Addressing Facts

- Program memory addressed in bytes; PC[0] fixed to 0 (word alignment)
- PC increments by 2 per instruction fetch
- CALL/GOTO encode word address in PC[20:1]
- Data EEPROM accessed via NVM registers (not directly addressable in data space)
- SAF = last 128 words of user flash, non-executable when SAFEN=0
- Config words at 0x300000–0x300009 are not code-protected, not affected by Bulk Erase for DCI/DIA/revision