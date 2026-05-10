# PIC18F27/47/57Q43 — NVM (Nonvolatile Memory) and CRC with Scanner

## NVM — Nonvolatile Memory Control

### Memory Map

| Region | Address Range | CPU Exec | REG[1:0] | Access |
|---|---|---|---|---|
| Program Flash (PFM) | 000000h–01FFFFh (128 KB) | Yes | 10 | Read/Write |
| User IDs | 200000h–20003Fh (32 words) | No | x1 | Read/Write |
| Reserved | 200040h–2BFFFFh | — | — | — |
| Data Flash (DFM) | 2C0000h–2C03FFh (1 KB) | No | 00 | Read/Write |
| Reserved | 2C0400h–3BFFFFh | — | — | — |
| DIA | 3F0000h–3F003Fh | No | x1 | Read only |
| DCI | 3C0000h–3C0009h | No | x1 | Read only |
| Device/Rev ID | 3FFFFEh–3FFFFFh | No | x1 | Read only |

- PFM erase block: 128 words. PFM write: 1 word or 128-word page via buffer RAM.
- DFM: byte-read/write with implicit erase-before-write per byte. No page erase for DFM.

### Key Registers

| Register | Key Bits | Purpose |
|---|---|---|
| NVMCON0 | GO | Start operation (self-clearing) |
| NVMCON1 | WRERR, NVMCMD<2:0> | Error flag, command select |
| NVMLOCK | NVMLOCK<7:0> | Unlock pattern (0x55 then 0xAA before GO) |
| NVMADR | NVMADR<21:0> | 22-bit target address |
| NVMDAT | NVMDAT<15:0> | 16-bit data (PFM) / NVMDATL byte (DFM) |

### NVMCON0 Register Detail

| Bit | 7–1 | 0 |
|-----|------|---|
| Field | — | GO |
| Access | U | R/S/HC |

- **GO**: Set to start operation. Must follow unlock sequence for write/erase. Self-clearing.

### NVMCON1 Register Detail

| Bit | 7 | 6–3 | 2:0 |
|-----|---|-----|------|
| Field | WRERR | — | NVMCMD |
| Access | R/C/HS | U | R/W |

- **WRERR**: 1=write error (interrupted reset, write-protected addr, invalid addr, locked, or page op on DFM). Must clear by user.
- **NVMCMD<2:0>**: Operation select.

### NVM Operations (NVMCMD<2:0>)

| NVMCMD | Unlock | Operation | DFM | PFM | Source/Dest | WRERR | INT |
|---|---|---|---|---|---|---|---|
| 000 | No | Read | byte | word | NVM→NVMDAT | No | No |
| 001 | No | Read and Post Increment | byte | word | NVM→NVMDAT | No | No |
| 010 | No | Read Page | — | page | NVM→Buffer RAM | No | No |
| 011 | Yes | Write | byte | word | NVMDAT→NVM | Yes | Yes |
| 100 | Yes | Write and Post Increment | byte | word | NVMDAT→NVM | Yes | Yes |
| 101 | Yes | Write Page | — | page | Buffer RAM→NVM | Yes | Yes |
| 110 | Yes | Erase Page | — | page | n/a | Yes | Yes |
| 111 | No | Reserved | — | — | — | No | No |

### Unlock Sequence (required before GO for write/erase)

1. Write 0x55 to NVMLOCK
2. Write 0xAA to NVMLOCK
3. Set GO bit in NVMCON0 (must follow immediately, no interruption)

### PFM Operations Summary

**Page Erase (NVMCMD=110)**:
1. Set NVMADR to address within target page
2. Set NVMCMD=110
3. Disable interrupts
4. Unlock sequence + set GO
5. CPU stalls during erase (~2 ms)
6. Poll GO or NVMIF for completion

**Page Write (NVMCMD=101)**:
1. Load buffer RAM with data (or use Read Page first)
2. Set NVMADR to page address
3. Set NVMCMD=101
4. Disable interrupts
5. Unlock sequence + set GO
6. CPU stalls during write

**Word Write (NVMCMD=011)**:
1. Set NVMADR to target address
2. Load NVMDAT with desired word
3. Set NVMCMD=011
4. Disable interrupts
5. Unlock sequence + set GO
6. CPU stalls during write

**Word Modify (erase+rewrite)**: Read Page → modify buffer → Erase Page → Write Page

### DFM (Data Flash/Eeprom) Operations

**Byte Read (NVMCMD=000)**: Set NVMADR, set NVMCMD=000, set GO, read NVMDATL.

**Byte Write (NVMCMD=011)**:
1. Set NVMADR to target byte address
2. Load NVMDATL with data byte
3. Set NVMCMD=011
4. Disable interrupts
5. Unlock sequence + set GO
6. CPU continues during DFM write (parallel operation)
7. Poll GO/NVMIF for completion

Each DFM write includes implicit erase. DFM does not support Page Erase. To erase DFM, write 0xFF to each location.

### Buffer RAM

| Device | GPR Bank Number |
|---|---|
| PIC18F57Q43 | 37 |
| PIC18F47Q43 | 21 |
| PIC18F27Q43 | 13 |

### Protection
- **Code protection** (CP config bit): blocks external reads; CPU reads unaffected. Bulk Erase to clear.
- **Write protection** (WRTn config bits): blocks self-write to protected PFM regions.
- NVMLOCK must be written with 0x55/0xAA before each write/erase GO. NVMCMD should be kept clear when not actively programming.

### Q43 vs K42 Differences
- Q43 uses **NVMCON0/NVMCON1/NVMLOCK/NVMADR/NVMDAT** register model replacing K42's NVMCON1/NVMCON2/NVMADRH:NVMADRL/NVMDAT.
- Q43 NVMCON1 uses **NVMCMD<2:0>** instead of K42's FREE/WRERR/WREN/WR/RD bits.
- Q43 uses **NVMLOCK** (0x55/0xAA pattern) instead of K42's NVMCON2 unlock.
- Q43 NVMADR is 22-bit (NVMADR at 0x43 with 3 bytes), vs K42's TBLPTR + NVMADRH:NVMADRL.
- Q43 NVMDAT is 16-bit (NVMDATH:NVMDATL), vs K42's 8-bit NVMDAT.
- Q43 DFM byte write runs in parallel (CPU continues); K42 uses same register set for EEPROM.
- Q43 PFM page size is 128 words (same as K42), with same buffer RAM approach.

---

## CRC — Cyclic Redundancy Check with Memory Scanner

### Features
- Up to 16-bit CRC polynomial
- Configurable polynomial (CRCXORH/L), seed (CRCACCH/L)
- Standard or reversed bit order (SHIFTM)
- Augmented zero mode (ACCM)
- Memory scanner for PFM/DFM CRC
- Interrupt on BUSY 1→0 transition

### Key Registers

| Register | Key Bits | Purpose |
|---|---|---|
| CRCCON0 | EN, GO, BUSY(r), ACCM, SHIFTM, FULL(r) | Enable, start, status, augment, shift direction, data path full |
| CRCCON1 | DLEN<3:0>, PLEN<3:0> | Data length-1, polynomial length-1 |
| CRCDATH/L | DATA<15:0> | Input data (shifter loads on CRCDATL write) |
| CRCACCH/L | ACC<15:0> | Accumulator / seed / result |
| CRCXORH/L | X<15:0> (X<0> unimplemented, always 1) | Polynomial XOR terms |
| CRCSHIFTH/L | SHIFT<15:0> (read-only) | Current shifter state |

### CRCCON0 Register

| Bit | 7 | 6 | 5 | 4 | 3–2 | 1 | 0 |
|-----|---|---|---|---|------|---|---|
| Field | EN | GO | BUSY | ACCM | — | SHIFTM | FULL |

- **EN**: Enable CRC module
- **GO**: Start shifter (set by user, cleared when done)
- **BUSY**: 1=shifting in progress or pending
- **ACCM**: 1=augment data with zeros equal to polynomial length
- **SHIFTM**: 0=MSb first (big-endian), 1=LSb first (little-endian)
- **FULL**: 1=CRCDATH/L registers full, waiting for shifter

### CRCCON1 Register

| Bit | 7–4 | 3–0 |
|-----|------|------|
| Field | DLEN<3:0> | PLEN<3:0> |

- **DLEN**: Data word length minus 1 (e.g., 7 for 8-bit data)
- **PLEN**: Polynomial length minus 2 (e.g., 14 for CRC-16, since MSb and LSb=1 are forced by hardware)

### CRCXORL Note
Bit 0 of CRCXORL is unimplemented and always reads as '0'. Hardware always treats polynomial LSb as '1'.

### Configuration Steps
1. Set EN=1
2. Optionally seed CRCACCH/L
3. Write polynomial to CRCXORH/L
4. Set DLEN, PLEN in CRCCON1
5. Set ACCM (augmented zeros) and SHIFTM (bit order) in CRCCON0
6. Set GO=1 to start shifting
7. Write data to CRCDATH/L (shifter loads on CRCDATL write when FULL=0)
8. Monitor BUSY or CRCIF for completion
9. Read result from CRCACCH/L

### Scanner Module

| Register | Key Bits | Purpose |
|---|---|---|
| SCANCON0 | EN, TRIGEN, SGO, MREG, BURSTMD, BUSY(r) | Scanner enable, trigger, start, memory select, burst mode |
| SCANLADRU/H/L | LADR<21:0> | Scan start/current address (incrementing) |
| SCANHADRU/H/L | HADR<21:0> | Scan end address (defaults 0x3FFFFF) |
| SCANTRIG | TSEL<4:0> | Trigger source select |

### Scanner Trigger (TSEL<4:0>)

| Value | Source |
|---|---|
| 00000 | LFINTOSC |
| 00001 | CLKREF_output |
| 00010 | TMR0_output |
| 00011 | TMR1_output |
| 00100 | TMR2_postscaled |
| 00101 | TMR3_output |
| 00110 | TMR4_postscaled |
| 00111 | TMR5_output |
| 01000 | TMR6_postscaled |
| 01001 | SMT1_output |

### Scanner Memory Select
- **MREG=0**: Scanner addresses Program Flash Memory
- **MREG=1**: Scanner addresses Data Flash Memory

### Scanner Modes

| TRIGEN | BURSTMD | Behavior |
|---|---|---|
| 0 | 0 | CRC-ready gated, CPU arbiter priority |
| 1 | 0 | CRC-ready AND trigger source gated |
| x | 1 | Always request memory access |

### Q43 vs K42 Differences
- Q43 CRC/scanner register layout largely identical to K42.
- Q43 SCANTRIG TSEL values 0–9 match K42.
- Q43 CRC address: CRCCON0 at 0x357 (vs K42 different location).
- Q43 SCANLADR/HADR 22-bit address range for PFM up to 128KB.
- CRCXORL bit 0 unimplemented on both devices.