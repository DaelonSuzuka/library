# PIC18F26K42 — NVM (Nonvolatile Memory) and CRC with Scanner

## NVM — Nonvolatile Memory Control

### Memory Map

| Region | Address Range | CPU Exec | REG<1:0> | TABLAT Access |
|---|---|---|---|---|
| Program Flash (PFM) | 000000h–01FFFFh (128 KB) | Yes | 10 | Read/Write |
| User IDs | 200000h–20000Fh (8 words) | No | x1 | Read/Write |
| Reserved | 200010h–2FFFFFh | — | — | — |
| Config Words | 300000h–300009h | No | x1 | Read/Write |
| Reserved | 30000Ah–30FFFFh | — | — | — |
| Data EEPROM | 310000h–3103FFh (1 KB) | No | 00 | Read/Write |
| Reserved | 310400h–3EFFFFh | — | — | — |
| DIA | 3F0000h–3F003Fh | No | x1 | Read only |
| DCI | 3FFF00h–3FFF09h | No | x1 | Read only |
| Device/Rev ID | 3FFFC0h–3FFFFFh | No | x1 | Read only |

- PFM erase block: 64 words (128 bytes). PFM write block: varies by device (see Table 5-4). Word/byte programming not supported.
- Data EEPROM: byte-read/write with implicit erase-before-write. Single byte at a time.

### Key Registers

| Register | Key Bits | Purpose |
|---|---|---|
| NVMCON1 | REG<1:0>, FREE, WRERR, WREN, WR, RD | Region select, erase enable, error flag, write enable, start ops |
| NVMCON2 | Unlock pattern (55h then AAh) | Write protection; always reads 00h |
| NVMADRH:NVMADRL | ADR<9:0> | EEPROM address (NVMADRH bits 1:0 only; not impl on 45/55K42) |
| NVMDAT | DAT<7:0> | EEPROM read/write data byte |
| TBLPTRU:H:L | 22-bit pointer | PFM/User ID/Config byte address |
| TABLAT | 8-bit latch | PFM read/write data staging |

### NVMCON1 Register Detail

| Bit | 7–6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|------|---|---|---|---|---|---|
| Field | REG<1:0> | — | FREE | WRERR | WREN | WR | RD |
| Access | R/W | U | R/W | R/S/HC | R/W | R/S/HC | R/S/HC |

- **REG<1:0>**: 00=Data EEPROM, 10=PFM, x1=User IDs/Config/DIA/DCI/Device ID
- **FREE**: 1=erase on next WR (PFM only)
- **WRERR**: 1=write error (interrupted reset, write-protected addr, or invalid addr); must clear by user
- **WREN**: 1=enable program/erase cycles
- **WR**: Set to initiate write/erase (self-clearing); requires unlock sequence
- **RD**: Set to initiate EEPROM read (self-clearing)

### Unlock Sequence (required before WR set for write/erase)

1. Write 55h to NVMCON2
2. Write AAh to NVMCON2
3. Set WR bit in NVMCON1 (must follow immediately, no interruption)

### PFM Write Sequence (summary)

1. Read row into RAM → modify data
2. Load TBLPTR with row address
3. Set FREE=1, WREN=1, REG=10, perform unlock+erase
4. Load TBLPTR with write address
5. TBLWT data bytes into holding registers
6. Set WREN=1, FREE=0, REG=10, perform unlock+write
7. CPU stalls ~2 ms per write block

### EEPROM Read/Write

**Read**: Set REG=00, set NVMADRH:NVMADRL, set RD=1, read NVMDAT next cycle.
**Write**: Set REG=00, load NVMADRH:NVMADRL + NVMDAT, set WREN=1, disable interrupts, unlock sequence, set WR=1. Write includes implicit erase. NVMIF set on completion.

### Protection
- **Code protection** (CP, CPD config bits): blocks external access, does not affect self-write.
- **Write protection** (WRT bits): blocks self-write to protected PFM regions.

### K42 vs Q41 Differences
- K42 uses NVMCON1 REG bits for region select; Q41 also uses EEPGD/CFGS bit names but same layout.
- K42 has 128 KB PFM (PIC18F26K42); Q41 has 64 KB PFM (PIC18F16Q41).
- K42 Data EEPROM: 1024 bytes vs Q41's 256 bytes.
- NVMADRH is implemented on PIC18F26K42 (10-bit EEPROM addressing) but not on PIC18F45/55K42 (8-bit).
- K42 PFM erase = 64 words, write = varies.

---

## CRC — Cyclic Redundancy Check with Memory Scanner

### Features
- Up to 16-bit CRC polynomial
- Configurable polynomial (CRCXORH/L), seed (CRCACCH/L)
- Standard or reversed bit order (SHIFTM)
- Augmented zero mode (ACCM)
- Memory scanner for PFM/Data EEPROM CRC
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
| SCANTRIG | TSEL<3:0> | Trigger source select |

### Scanner Trigger (TSEL<3:0>)

| Value | Source |
|---|---|
| 0000 | LFINTOSC |
| 0001 | CLKREF_output |
| 0010 | TMR0_output |
| 0011 | TMR1_output |
| 0100 | TMR2_postscaled |
| 0101 | TMR3_output |
| 0110 | TMR4_postscaled |
| 0111 | TMR5_output |
| 1000 | TMR6_postscaled |
| 1001 | SMT1_output |

### Scanner Memory Select
- **MREG=0**: Scanner addresses Program Flash Memory
- **MREG=1**: Scanner addresses Data EEPROM

### Scanner Modes

| TRIGEN | BURSTMD | Behavior |
|---|---|---|
| 0 | 0 | CRC-ready gated, CPU arbiter priority |
| 1 | 0 | CRC-ready AND trigger source gated |
| x | 1 | Always request memory access |

### K42 vs Q41 Differences
- K42 CRC/scanner register layout identical to Q41.
- K42 SCANTRIG TSEL values 0–9 match Q41.
- SCANLADR/HADR registers span 22 bits; both devices share this.
- CRCXORL bit 0 unimplemented (reads 0, hardware forces LSb=1) on both.