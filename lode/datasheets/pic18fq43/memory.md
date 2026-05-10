# PIC18F27/47/57Q43 Family — Memory & NVM Reference

## Device Variants and Memory Sizes

| Device | Program Flash | Data SRAM | Data EEPROM | Pins |
|---|---|---|---|---|
| PIC18F25/45Q43 | 16KW (32KB) | 4KB | 1024B | 28/40/44 |
| PIC18F26/46Q43 | 32KW (64KB) | 4KB | 1024B | 28/40/44 |
| PIC18F27/47Q43 | 64KW (128KB) | 4KB | 1024B | 28/40/44 |
| PIC18F57Q43 | 128KW (256KB) | 4KB | 1024B | 48 |

## Program Flash Memory Map

| Region | PIC18Fx5Q43 | PIC18Fx6Q43 | PIC18Fx7Q43 |
|---|---|---|---|
| Reset Vector | 0x000000 | 0x000000 | 0x000000 |
| Program Flash | 0x000000–0x003FFF (16KW) | 0x000000–0x007FFF (32KW) | 0x000000–0x00FFFF (64KW) |
| Reserved | 0x004000–0x1FFFFF | 0x008000–0x1FFFFF | 0x010000–0x1FFFFF |
| User IDs | 0x200000–0x20003F (32 words) | same | same |
| Reserved | 0x200040–0x2BFFFF | same | same |
| DIA | 0x2C0000–0x2C00FF | same | same |
| Reserved | 0x2C0100–0x2FFFFF | same | same |
| Config Bytes | 0x300000–0x300009 | same | same |
| Reserved | 0x30000A–0x37FFFF | same | same |
| Data EEPROM | 0x380000–0x3803FF (1024B) | same | same |
| Reserved | 0x380400–0x3BFFFF | same | same |
| DCI | 0x3C0000–0x3C0009 | same | same |
| Reserved | 0x3C000A–0x3FFFFB | same | same |
| Revision ID | 0x3FFFFC | same | same |
| Device ID | 0x3FFFFE | same | same |

PC is 21-bit (2MB address space). Unimplemented memory reads as NOP (all zeros). IVT base relocatable via IVTBASE register.

## Memory Access Partition

Program Flash partitioned by BBEN and SAFEN config bits:

| BBEN | SAFEN | Partition Layout |
|---|---|---|
| 1 (disabled) | 1 (disabled) | All flash = Application Block |
| 1 (disabled) | 0 (enabled) | Application Block + SAF at end |
| 0 (enabled) | 1 (disabled) | Boot Block + Application Block |
| 0 (enabled) | 0 (enabled) | Boot Block + Application Block + SAF |

- **Application Block**: Default user code region. Write-protected by WRTAPP.
- **Boot Block**: Bootloader code; size set by BBSIZE[2:0]. Write-protected by WRTB.
- **SAF**: Last 128 words of user flash when SAFEN=0. Non-executable. Write-protected by WRTSAF.Write-protected locations: if written, memory unchanged and WRERR set.

## Data SRAM Organization

- 4KB data SRAM across banks
- 6-bit BSR (BSR[5:0]) selects 256-byte banks
- Full data address = BSR[5:0] : offset[7:0]

| Bank | Address Range | Content |
|------|--------------|---------|
| 0 | 0x0000–0x00FF | GPR |
| 1–3 | 0x0100–0x03FF | GPR |
| 4 | 0x0400–0x045F | Access RAM (GPR) |
| 4 | 0x0460–0x04FF | Fast SFR (Access Bank) |
| 5 | 0x0500–0x055F | Access RAM (GPR) |
| 5 | 0x0560–0x05FF | Access SFR |
| 6–31 | 0x0600–0x1FFF | GPR |
| 32–61 | 0x2000–0x3DFF | GPR/SFR Buffer RAM |
| 62 | 0x3E00–0x3EFF | SFR |
| 63 | 0x3F00–0x3FFF | Core SFR |

Unimplemented banks: read returns 0, writes ignored.

## Access Bank (Virtual, No BSR Needed)

| Region | Addresses | Description |
|---|---|---|
| Access RAM (GPR) | 0x0000–0x005F → Bank 0/5 lower 96 bytes | Lower half |
| SFR | 0x0060–0x00FF → Bank 4 upper 160 bytes | Upper half |

Instruction bit `a=0` forces Access Bank; `a=1` uses BSR.

With XINST=1: `a=0` with offset ≤0x5F becomes Indexed Literal Offset mode using FSR2 as base pointer.

## Stack

- **127-level** hardware return stack (STKPTR[6:0])
- TOSU/TOSH/TOSL: 21-bit Top-of-Stack (readable/writable)
- PUSH increments STKPTR, POP decrements STKPTR
- STKOVF (PCON0 bit 7): set on 128th push; STVREN=1→Reset, STVREN=0→overwrite TOS
- STKUNF (PCON0 bit 6): set on underflow; STVREN=1→Reset, STVREN=0→no Reset
- Fast Register Stack: 3 levels (1 for CALL, 2 for interrupts) saving STATUS, WREG, BSR

## Key Core SFR Addresses

| Register | Address | Description |
|----------|---------|-------------|
| PCL | 0x4F9 | Program Counter low byte |
| PCLAT | 0x4FA | PCLATH[7:0] + PCLATU[4:0] (16-bit register) |
| STKPTR | 0x4FC | Stack Pointer [6:0] |
| TOS | 0x4FD | Top-of-Stack (3-byte: TOSU/H/L) |
| WREG | 0x4E8 | Working register |
| BSR | 0x4E0 | Bank Select [5:0] |
| FSR0 | 0x4E9 | Indirect address register 0 (FSR0H+FSR0L) |
| FSR1 | 0x4E1 | Indirect address register 1 |
| FSR2 | 0x4D9 | Indirect address register 2 |
| INDF0 | 0x4EF | Indirect data 0 |
| INDF1 | 0x4E7 | Indirect data 1 |
| INDF2 | 0x4DF | Indirect data 2 |
| POSTINC0 | 0x4EE | Post-increment FSR0 |
| POSTDEC0 | 0x4ED | Post-decrement FSR0 |
| PREINC0 | 0x4EC | Pre-increment FSR0 |
| PLUSW0 | 0x4EB | FSR0 + signed W offset |

## NVM Control Registers

| Register | Description |
|----------|-------------|
| NVMCON0 | GO bit (start op), NVM control bits |
| NVMCON1 | WRERR (R/C/HS), NVMCMD[2:0] (R/W) |
| NVMCON2 | NVM unlock key register |
| NVMADRL/H | NVM address registers |
| NVMDAT | NVM data register |
| TBLPTRU/H/L | Table pointer (21-bit) |
| TABLAT | Table latch |

NVM commands: Read (000), Write (011), Erase Page (110), etc. Unlock sequence: NVMCON2=0x55, NVMCON2=0xAA, GO=1.

## Addressing Modes

- **Direct**: BSR[5:0] + 8-bit offset (a=1), or Access Bank (a=0)
- **Indirect**: FSR0/1/2 (14-bit address) with INDF, POSTINC, POSTDEC, PREINC, PLUSW
- **Indexed Literal Offset** (XINST=1): FSR2 + offset when a=0 and offset ≤0x5F

## Key Addressing Facts

- Program memory addressed in bytes; PC[0] fixed to 0 (word alignment)
- PC increments by 2 per instruction fetch
- Data EEPROM accessed via NVM registers (not directly addressable in data space)
- SAF = last 128 words of user flash, non-executable when SAFEN=0
- Config words at 0x300000–0x300009 are not code-protected, not affected by Bulk Erase for DCI/DIA/revision