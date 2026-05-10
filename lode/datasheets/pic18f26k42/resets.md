# PIC18F26K42 — Reset System

## Reset Types and Sources

| Reset Type | Trigger | PCON0/PCON1 Flag |
|---|---|---|
| Power-on Reset (POR) | VDD rises above threshold | POR (PCON0 bit 1) |
| Brown-out Reset (BOR) | VDD falls below VBOR | BOR (PCON0 bit 0) |
| Low-Power BOR (LPBOR) | Low-power VDD monitor trips | BOR (PCON0 bit 0) — OR'd with BOR |
| MCLR Reset | External /MCLR pin driven low | RMCLR (PCON0 bit 3) |
| WDT Time-out Reset | Watchdog timer overflow | RWDT (PCON0 bit 4) |
| WWDT Window Violation | CLRWDT issued outside window | WDTWV (PCON0 bit 5) |
| RESET Instruction | Software `RESET` opcode | RI (PCON0 bit 2) |
| Stack Overflow | CALL exceeds stack depth (STVREN=1) | STKOVF (PCON0 bit 7) |
| Stack Underflow | RETURN with empty stack (STVREN=1) | STKUNF (PCON0 bit 6) |
| Memory Execution Violation | Execute from invalid address or SAF | MEMV (PCON1 bit 1) |

Internal resets (RESET, BOR, WWDT, POR, STKOVF, STKUNF) do **not** drive the MCLR pin low.

## K42 vs Q41 Differences

- K42 has **no** RVREG (LDO regulator fault) or RCM (config memory) flags in PCON1 — only MEMV.
- K42 PCON1 has only bit 1 (MEMV) implemented; Q41 has bits 0 (RCM), 1 (MEMV), 2 (RVREG).
- K42 BORCON is at a different SFR address than Q41's PCON0+BORCON layout.

## Reset Status Registers

### PCON0 — Power Control Register 0

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|---|---|---|---|---|---|---|---|
| Field | STKOVF | STKUNF | WDTWV | RWDT | RMCLR | RI | POR | BOR |
| Access | R/W/HS | R/W/HS | R/W/HC | R/W/HC | R/W/HC | R/W/HC | R/W/HC | R/W/HC |
| POR default | 0 | 0 | 1 | 1 | 1 | 1 | 0 | q |

- POR/BOR flags (bits 0–2, 3–5) are **active-low**: 0 = that reset occurred.
- STKOVF/STKUNF (bits 7–6) are **active-high**: 1 = overflow/underflow occurred.
- Software must set flags back to inactive state; hardware does not auto-clear.

### PCON1 — Power Control Register 1

| Bit | 7–2 | 1 | 0 |
|-----|------|---|---|
| Field | — | MEMV | — |
| Access | U | R/W/HC | U |
| POR default | — | 1 | — |

- MEMV: 0 = memory violation reset occurred. Must re-set by firmware to detect further violations.

## Reset Cause Determination

| Condition | PCON0 | PCON1 | STATUS<6:5> |
|---|---|---|---|
| POR | BOR=q, POR=0, rest=1 | MEMV=1 | 1,1 |
| BOR | BOR=0, POR=0 | unchanged | 1,1 |
| MCLR (awake) | RMCLR=0 | unchanged | u,u |
| MCLR (sleep) | RMCLR=0 | unchanged | 1,0 |
| WDT time-out | RWDT=0 | unchanged | 0,u |
| WWDT window violation | WDTWV=0 | unchanged | u,u |
| RESET instruction | RI=0 | unchanged | u,u |
| Stack overflow | STKOVF=1 | unchanged | u,u |
| Stack underflow | STKUNF=1 | unchanged | u,u |
| Memory violation | unchanged | MEMV=0 | u,u |

## BOR Operating Modes (BOREN config bits)

| BOREN<1:0> | SBOREN | Mode | POR Release | Sleep Wake |
|---|---|---|---|---|
| 11 | X | Always on | Wait BORRDY=1 | Immediate |
| 10 | X | Off in Sleep | Wait BORRDY=1 | Wait BORRDY=1 |
| 01 | 1 | Software-enabled | Wait BORRDY=1 | Immediate |
| 01 | 0 | Software-disabled | Immediate | Immediate |
| 00 | X | Always off | Immediate | Immediate |

BOR is forced ON during PFM Bulk Erase at 2.45V for F/LF devices.

## BORCON Register

| Bit | 7 | 6–1 | 0 |
|-----|---|-----|---|
| Field | SBOREN | — | BORRDY |
| Access | R/W | — | R |
| POR default | 1 | — | q |

- **SBOREN**: Software BOR enable. Only effective when BOREN=01.
- **BORRDY**: 1 = BOR circuit active and armed; 0 = disabled or warming up.

## Start-Up Sequence

After POR/BOR release:
1. **PWRT** runs to completion (if enabled via PWRTS<1:0> config bits).
2. **OST** runs to completion (if required by oscillator source).
3. **MCLR** released (if enabled).

## Key Configuration Bits

| Bit | Purpose |
|-----|---------|
| BOREN<1:0> | BOR operating mode |
| BORV<1:0> | BOR voltage threshold |
| LPBOREN | LPBOR enable (default off on erased device) |
| MCLRE | MCLR pin function |
| LVP | Low-voltage programming (affects MCLR) |
| STVREN | Stack overflow/underflow reset enable |
| PWRTS<1:0> | Power-up Timer delay |