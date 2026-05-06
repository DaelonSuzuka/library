# PIC18F16Q41 — Reset System

## Reset Types and Sources

| Reset Type | Trigger | PCON0 Flag |
|---|---|---|
| Power-on Reset (POR) | VDD rises above threshold | POR (bit 1) |
| Brown-out Reset (BOR) | VDD falls below VBOR | BOR (bit 0) |
| Low-Power BOR (LPBOR) | Low-power VDD monitor trips | BOR (bit 0) — OR'd with BOR |
| MCLR Reset | External /MCLR pin driven low | RMCLR (bit 3) |
| WDT Time-out Reset | Watchdog timer overflow | RWDT (bit 4) |
| WWDT Window Violation | CLRWDT issued outside window | WDTWV (bit 5) |
| RESET Instruction | Software `RESET` opcode | RI (bit 2) |
| Stack Overflow | CALL exceeds stack depth (STVREN=1) | STKOVF (bit 7) |
| Stack Underflow | RETURN with empty stack (STVREN=1) | STKUNF (bit 6) |
| Memory Execution Violation | Execute from invalid address | MEMV (PCON1 bit 1) |
| Main LDO Regulator Reset | VDDCORE below minimum | RVREG (PCON1 bit 2) |
| Configuration Memory Reset | Corrupted config/cal latches | RCM (PCON1 bit 0) |

Internal resets ( RESET, BOR, WWDT, POR, STKOVF, STKUNF ) do **not** drive the MCLR pin low.

## Reset Status Registers

### PCON0 — Power Control Register 0 (0x04F0)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|---|---|---|---|---|---|---|---|
| Field | STKOVF | STKUNF | WDTWV | RWDT | RMCLR | RI | POR | BOR |
| Access | R/W/HS | R/W/HS | R/W/HC | R/W/HC | R/W/HC | R/W/HC | R/W/HC | R/W/HC |
| POR default | 0 | 0 | 1 | 1 | 1 | 1 | 0 | q |

- All flags are **active-low** when set (0 = that reset occurred), except STKOVF/STKUNF which are active-high.
- `HS` = set by hardware only; `HC` = set/cleared by hardware, writable by software.
- `q` = depends on BOR configuration (reflects BOR state at POR time).
- Software must set flags back to inactive state after reading; hardware does not auto-clear them.

### PCON1 — Power Control Register 1 (0x04F1)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|---|---|---|---|---|---|---|---|
| Field | — | — | — | — | — | RVREG | MEMV | RCM |
| Access | — | — | — | — | — | R/W/HC | R/W/HC | R/W/HC |
| POR default | — | — | — | — | — | 1 | 0 | q |

- MEMV: 0 = memory violation reset occurred. Must be re-set by firmware to detect further violations.
- RCM: 0 = config/calibration latch corruption detected.
- RVREG: 0 = LDO/ULP "ready" fault (VDDCORE below spec).

### STATUS Register (0x04E8) — Reset-Relevant Bits

| Bit | Field | Meaning After Reset |
|-----|-------|---------------------|
| 6 | nTO | 1 = no WDT time-out; 0 = WDT time-out occurred |
| 5 | nPD | 1 = not in Sleep; 0 = was in Sleep |

Set by hardware; Z/C/DC cleared only by POR/BOR.

## Reset Cause Determination

| Condition | PCON0 | PCON1 | STATUS<6:5> |
|---|---|---|---|
| POR | BOR=q, POR=0, rest=1 | RCM=q, MEMV=0, RVREG=1 | 1,1 |
| BOR | BOR=0, POR=0, rest=1 | RCM=u, MEMV=0, RVREG=u | 1,1 |
| MCLR (awake) | RMCLR=0 | unchanged | u,u |
| MCLR (sleep) | RMCLR=0 | unchanged | 1,0 |
| WDT time-out reset | RWDT=0 | unchanged | 0,u |
| WDT wake from sleep | unchanged | unchanged | 0,0 |
| WWDT window violation | WDTWV=0 | unchanged | u,u |
| RESET instruction | RI=0 | unchanged | u,u |
| Stack overflow | STKOVF=1 | unchanged | u,u |
| Stack underflow | STKUNF=1 | unchanged | u,u |
| Memory violation | unchanged | MEMV=0 | u,u |
| VREG/ULP fault | BOR=u, POR=0, rest=1 | RVREG=0, RCM=u | 1,1 |
| Config memory reset | unchanged | RCM=0 | u,u |

## BOR Operating Modes (BOREN config bits)

| BOREN | SBOREN | Mode | POR Release | Sleep Wake |
|-------|--------|------|-------------|------------|
| 11 | X | Always on | Wait BORRDY=1 | Immediate |
| 10 | X | Off in Sleep | Wait BORRDY=1 | Wait BORRDY=1 |
| 01 | 1 | Software-enabled | Wait BORRDY=1 | Immediate |
| 01 | 0 | Software-disabled | Immediate | Immediate |
| 00 | X | Always off | Immediate | Immediate |

BOR is forced ON during PFM Bulk Erase at lowest threshold, regardless of configuration.

## LPBOR

- Controlled by LPBOREN config bit (disabled by default on erased device).
- OR'd with BOR output — shares the BOR flag in PCON0.
- Monitors VDD at low power; holds device in Reset when VDD too low.

## MCLR Configuration

| MCLRE | LVP | MCLR Pin |
|-------|-----|----------|
| X | 1 | Enabled |
| 1 | 0 | Enabled |
| 0 | 0 | Disabled (pin becomes input-only) |

Internal weak pull-up to VDD when MCLR enabled. Noise filter on MCLR path.

## Start-Up Sequence

After POR or BOR release, execution begins only after:

1. **Power-up Timer (PWRT)** runs to completion (if enabled via PWRTS config bits).
2. **Oscillator Start-up Timer (OST)** runs to completion (if required by oscillator source).
3. **MCLR** is released (if enabled).

PWRT starts after POR/BOR release. OST and PWRT run independently of MCLR — if MCLR is held low long enough, both timers expire and execution begins 10 FOSC cycles after MCLR goes high.

## BORCON Register (0x0049)

| Bit | 7 | 6–1 | 0 |
|-----|---|-----|---|
| Field | SBOREN | — | BORRDY |
| Access | R/W | — | R |
| POR default | 1 | — | q |

- **SBOREN**: Software BOR enable. Only effective when BOREN=01. Otherwise read/write but no effect.
- **BORRDY**: 1 = BOR circuit active and armed; 0 = disabled or warming up.

## Key Configuration Bits

| Bit | Purpose |
|-----|---------|
| BOREN<1:0> | BOR operating mode selection |
| LPBOREN | LPBOR enable (default off) |
| MCLRE | MCLR pin function enable |
| LVP | Low-voltage programming enable (affects MCLR) |
| STVREN | Stack overflow/underflow reset enable |
| PWRTS<2:0> | Power-up Timer delay selection |