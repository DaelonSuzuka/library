# PIC18F16Q41 — Memory & NVM Reference

## Program Memory Map

| Region | Address Range | Size |
|---|---|---|
| Program Flash | 0x000000–0x003FFF | 8KW (16KB) |
| User IDs | 0x200000–0x20003F | 32 words |
| Reserved | 0x200040–0x2BFFFF | — |
| DIA (read-only) | 0x2C0000–0x2C00FF | Factory calibration data |
| Config Bytes | 0x300000–0x300008 | 9 bytes (CONFIG1–CONFIG9) |
| Reserved | 0x300009–0x37FFFF | — |
| Data EEPROM (DFM) | 0x380000–0x3801FF | 512 bytes |
| DCI (read-only) | 0x3C0000–0x3C0009 | Device config info |
| Revision ID | 0x3FFFFC | 1 word (read-only) |
| **Device ID** | **0x3FFFFE** | **1 word (read-only)** |

PIC18F16Q41 Device ID = **0x7560**.

## PFM Partitioning

Controlled by config bits BBEN, SAFEN, BBSIZE:
- **Application Block**: Default when BBEN=1, SAFEN=1 — all flash is app space
- **Boot Block**: Enabled when BBEN=0; size set by BBSIZE[2:0] (512–8192 words)
- **Storage Area Flash (SAF)**: Last 128 words of user flash when SAFEN=0; non-executable, data only

Write protection: WRTAPP, WRTB, WRTSAF config bits. Writing a write-protected area clears GO and sets WRERR.

## Data Memory (RAM)

- 64 banks of 256 bytes each (up to 16KB total, BSR selects bank)
- **PIC18F16Q41**: Banks 0–13 are GPR (3.5KB), Bank 38 is Buffer RAM for NVM, Banks 39–63 are SFR space

### Access Bank (virtual, no BSR needed)

| Region | Addresses | Size |
|---|---|---|
| Access RAM (GPR) | 0x0500–0x055F | 96 bytes (Bank 5 lower half) |
| Fast SFRs | 0x0460–0x04FF | 160 bytes (Bank 4 upper half) |

Access Bank: instruction bit `a=0` forces access bank; `a=1` uses BSR.

### Buffer RAM

NVM page buffer occupies Bank 21 for PIC18F16Q41 (per NVM Buffer Banks table — PIC18Fx4Q41 = Bank 9, PIC18Fx5Q41 = Bank 13, PIC18Fx6Q41 = Bank 21). Maps 1:1 to PFM page bytes via TBLPTRL/FSR low byte.

## Data EEPROM (DFM)

- 512 bytes at PFM address 0x380000–0x3801FF
- Byte-wide read/write only (no page ops for DFM)
- Auto erase-before-write on each byte
- No explicit Page Erase support; write 0xFF to "erase"

## Device Information Area (DIA) — 0x2C0000–0x2C00FF

| Address | Name | Content |
|---|---|---|
| 0x2C0000–0x2C0013 | MUI0–MUI9 | Microchip Unique Identifier |
| 0x2C0014–0x2C0023 | EUI0–EUI7 | External Unique Identifier |
| 0x2C0024–0x2C0029 | TSLR1–TSLR3 | Temp sensor low range calibration |
| 0x2C002A–0x2C002F | TSHR1–TSHR3 | Temp sensor high range calibration |
| 0x2C0030–0x2C0039 | FVRA/FVRC | FVR calibration (1x/2x/4x, ADC & Comp) |

All DIA is read-only, not affected by Bulk Erase.

## Device Configuration Info (DCI) — 0x3C0000–0x3C0009

| Address | Name | Value (PIC18F16Q41) |
|---|---|---|
| 0x3C0000 | ERSIZ | 128 words (erase page size) |
| 0x3C0002 | WLSIZ | 0 (write latches per row) |
| 0x3C0004 | URSIZ | 256 pages |
| 0x3C0006 | EESIZ | 512 bytes |
| 0x3C0008 | PCNT | 14/20 pins |

## Configuration Registers

| Address | Name | Key Bits |
|---|---|---|
| 0x300000 | CONFIG1 | RSTOSC[2:0], FEXTOSC[2:0] |
| 0x300001 | CONFIG2 | FCMEN, FCMENS, FCMENP, CSWEN, PR1WAY, CLKOUTEN |
| 0x300002 | CONFIG3 | BOREN[1:0], LPBOREN, IVT1WAY, MVECEN, PWRTS[1:0], MCLRE |
| 0x300003 | CONFIG4 | XINST, LVP, STVREN, PPS1WAY, ZCD, BORV[1:0] |
| 0x300004 | CONFIG5 | WDTE[1:0], WDTCPS[4:0] |
| 0x300005 | CONFIG6 | WDTCCS[2:0], WDTCWS[2:0] |
| 0x300006 | CONFIG7 | DEBUG, SAFEN, BBEN, BBSIZE[2:0] |
| 0x300007 | CONFIG8 | WRTAPP, WRTSAF, WRTD, WRTC, WRTB |
| 0x300008 | CONFIG9 | CP |

Config writes use NVMCMD=0b011 (byte write) with unlock sequence. Auto-erase-before-write. Enabled code protection cannot be disabled by self-write. **Write-once**: once protection bits are set, only Bulk Erase (external programmer) clears them.

## NVM Registers

| Register | Addr | Width | Key Fields |
|---|---|---|---|
| NVMCON0 | 0x040 | 8 | bit 0: GO (start op; R/S/HC; cleared by HW on completion) |
| NVMCON1 | 0x041 | 8 | bit 7: WRERR (R/C/HS); bits 2:0: NVMCMD[2:0] (R/W) |
| NVMLOCK | 0x042 | 8 | bits 7:0: unlock key (WO; reads as 0) |
| NVMADR | 0x043 | 22* | bits 21:0: NVM address (R/W) |
| NVMADRL | 0x043 | 8 | bits 7:0: NVMADR[7:0] |
| NVMADRH | 0x044 | 8 | bits 7:0: NVMADR[15:8] |
| NVMADRU | 0x045 | 8 | bits 5:0: NVMADR[21:16] |
| NVMDAT | 0x046 | 16* | bits 15:0: NVM data (R/W) |
| NVMDATL | 0x046 | 8 | bits 7:0: NVMDAT[7:0] (DFM uses only this byte) |
| NVMDATH | 0x047 | 8 | bits 7:0: NVMDAT[15:8] |
| TBLPTR | 0x04F6 | 24* | bit 21: config/UserID space flag; bits 20:0: address |
| TBLPTRL | 0x04F6 | 8 | bits 7:0: TBLPTR[7:0] |
| TBLPTRH | 0x04F7 | 8 | bits 7:0: TBLPTR[15:8] |
| TBLPTRU | 0x04F8 | 8 | bits 5:0: TBLPTR[20:16], bit 5: ACSS (access config space) |
| TABLAT | 0x04F5 | 8 | bits 7:0: table latch data |

*NVMADR is 22 bits (3 bytes at 0x043–0x045). NVMDAT is 16 bits (2 bytes at 0x046–0x047). TBLPTR is 22 effective bits + bit 21 config flag.*

## NVMCMD Operations

| NVMCMD | Op | Unlock? | DFM | PFM | WRERR? | INT? |
|---|---|---|---|---|---|---|
| 000 | Read | No | byte | word | No | No |
| 001 | Read & Post-Increment | No | byte | word | No | No |
| 010 | Read Page | No | — | page→buffer RAM | No | No |
| 011 | Write | Yes | byte | word | Yes | Yes |
| 100 | Write & Post-Increment | Yes | byte | word | Yes | Yes |
| 101 | Write Page | Yes | — | buffer RAM→page | Yes | Yes |
| 110 | Erase Page | Yes | — | page erase | Yes | Yes |
| 111 | Reserved | — | — | — | — | — |

## Unlock Sequence (CRITICAL)

Must disable interrupts first. Must be two consecutive writes then GO:

```c
NVMLOCK = 0x55;
NVMLOCK = 0xAA;
NVMCON0bits.GO = 1;
```

**Gotcha**: The unlock sequence must execute uninterrupted. If an interrupt fires between the two NVMLOCK writes, the unlock is lost and the write/erase will not occur. Always disable GIE before unlock.

## Key Sequences

### PFM Word Write
1. NVMADR = target address
2. NVMDAT = word value
3. NVMCON1bits.CMD = 0b011
4. Disable interrupts
5. Unlock sequence + set GO
6. Wait for GO to clear
7. Re-enable interrupts; set NVMCMD = 0b000

### PFM Page Erase
1. NVMADR = any address in page (bits 7:0 ignored)
2. NVMCON1bits.CMD = 0b110
3. Disable interrupts
4. Unlock + GO
5. Wait for GO clear
6. Re-enable interrupts; NVMCMD = 0b000

### PFM Page Write (after erase)
1. Load buffer RAM with 128 words (or do Page Read first to preserve unmodified data)
2. NVMADR = page base address
3. NVMCON1bits.CMD = 0b101
4. Disable interrupts
5. Unlock + GO
6. Wait for GO clear; restore interrupts; NVMCMD = 0b000

### DFM Byte Write
1. NVMADR = byte address; NVMDATL = data
2. NVMCON1bits.CMD = 0b011
3. Disable interrupts → unlock → GO
4. Wait for GO; re-enable; clear NVMCMD
- Auto-erase-before-write; no separate erase step needed

### Config Byte Write
Same as DFM byte write but NVMADR points to config address (0x300000–0x300008). Auto erase+write in one operation.

## Key Gotchas

1. **Unlock is two instructions**: NVMLOCK=0x55 then NVMLOCK=0xAA must be consecutive; any interrupt between them voids the unlock.
2. **GO cannot be cleared by software** — it is cleared by hardware when the operation completes. Writing operations block all NVM register access while GO=1.
3. **Always clear NVMCMD to 0b000 after operation** — prevents accidental writes.
4. **Page erase is 128 words minimum** — no single-word erase for PFM. To modify one word in a programmed page: Read Page → modify buffer → Erase Page → Write Page.
5. **DFM has no Page Erase** — erase by writing 0xFF to individual bytes; auto erase-before-write is implicit.
6. **Config writes are write-once for protection bits** — once WRTx or CP bits enable protection, they cannot be cleared by self-write; only Bulk Erase (external programmer) clears them.
7. **CPU stalls during PFM write/erase** — instruction fetch is halted; code cannot execute from flash during the operation.
8. **WRERR**: Set on write-protected area access, invalid address, unexpected Reset during operation, page op directed at DFM, or unlock failure. Check after every write/erase.
9. **DFM byte read**: NVMCMD=0b000, set GO, then read NVMDATL next instruction.
10. **TBLPTR bit 21** selects config/UserID/DIA/DCI space when set; PFM space when clear.
11. **Access Bank**: `a=0` remaps to 0x0460–0x055F; `a=1` uses BSR. Extended instruction set (XINST=0 in CONFIG4) changes this — when enabled, `a=0` with offset ≤0x5F becomes indexed literal offset via FSR2.