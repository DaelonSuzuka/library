# PIC18F27/47/57Q43 — Reset System

## Reset Types and Sources

| Reset Type | Trigger | PCON0/PCON1 Flag |
|---|---|---|
| Power-on Reset (POR) | VDD rises above threshold | POR (PCON0 bit 1) |
| Brown-out Reset (BOR) | VDD falls below VBOR | BOR (PCON0 bit 0) |
| Low-Power BOR (LPBOR) | Low-power VDD monitor trips | BOR (PCON0 bit 0) — OR'd with BOR |
| MCLR Reset | External /MCLR pin driven low | RMCLR (PCON0 bit 3) |
| WDT Time-out Reset | Watchdog timer overflow | RWDT (PCON0 bit 4) |
| WWDT Window Violation | CLRWDT outside window | WDTWV (PCON0 bit 5) |
| RESET Instruction | Software `RESET` opcode | RI (PCON0 bit 2) |
| Stack Overflow | CALL exceeds 127-deep stack (STVREN=1) | STKOVF (PCON0 bit 7) |
| Stack Underflow | RETURN with empty stack (STVREN=1) | STKUNF (PCON0 bit 6) |
| Memory Execution Violation | Execute from invalid address or SAF | MEMV (PCON1 bit 1) |
| VREG/ULP Ready Fault | LDO or ULP VREG fault | RVREG (PCON1 bit 2) |
| Config Memory Fault | Corrupted config/calibration latches | RCM (PCON1 bit 0) |

Internal resets (RESET, BOR, WWDT, POR, STKOVF, STKUNF) do **not** drive the MCLR pin low.

## PCON0 — Power Control Register 0 (0x04F0)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|---|---|---|---|---|---|---|---|
| Field | STKOVF | STKUNF | WDTWV | RWDT | RMCLR | RI | POR | BOR |
| Access | R/W/HS | R/W/HS | R/W/HC | R/W/HC | R/W/HC | R/W/HC | R/W/HC | R/W/HC |
| POR default | 0 | 0 | 1 | 1 | 1 | 1 | 0 | q |

- POR/BOR flags (bits 0–2, 3–5) are **active-low**: 0 = that reset occurred
- STKOVF/STKUNF (bits 7–6) are **active-high**: 1 = overflow/underflow occurred
- Software must set flags back to inactive state; hardware does not auto-clear

### PCON0 Bit Details

| Bit | Field | POR | Meaning |
|-----|-------|-----|---------|
| 7 | STKOVF | 0 | 1=Stack overflow occurred; 0=no overflow or cleared by firmware |
| 6 | STKUNF | 0 | 1=Stack underflow occurred; 0=no underflow or cleared by firmware |
| 5 | WDTWV | 1 | 0=WDT window violation occurred (CLRWDT outside window) |
| 4 | RWDT | 1 | 0=WDT time-out Reset occurred |
| 3 | RMCLR | 1 | 0=MCLR Reset occurred |
| 2 | RI | 1 | 0=RESET instruction executed |
| 1 | POR | 0 | 0=Power-on Reset occurred |
| 0 | BOR | q | 0=Brown-out Reset occurred; 1=no BOR (or set by firmware) |

## PCON1 — Power Control Register 1 (0x04F1)

| Bit | 7–3 | 2 | 1 | 0 |
|-----|------|---|---|---|
| Field | — | RVREG | MEMV | RCM |
| Access | — | R/W/HC | R/W/HC | R/W/HC |
| POR default | — | 1 | 0 | q |

| Bit | Field | Meaning |
|-----|-------|---------|
| 2 | RVREG | 0=Main LDO voltage regulator fault Reset occurred |
| 1 | MEMV | 0=Memory execution violation Reset occurred |
| 0 | RCM | 0=Configuration/calibration data corruption Reset occurred |

MEMV must be re-set by firmware after a memory violation to detect further violations.

## Reset Cause Determination

| Condition | PCON0 | PCON1 | STATUS<6:5> |
|---|---|---|---|
| POR | BOR=q, POR=0, rest=1 | RVREG=1, MEMV=0, RCM=q | 1,1 |
| BOR | BOR=0, POR=0 | unchanged | 1,1 |
| MCLR (awake) | RMCLR=0 | unchanged | u,u |
| MCLR (sleep) | RMCLR=0 | unchanged | 1,0 |
| WDT time-out | RWDT=0 | unchanged | 0,u |
| WWDT window violation | WDTWV=0 | unchanged | u,u |
| RESET instruction | RI=0 | unchanged | u,u |
| Stack overflow (STVREN=1) | STKOVF=1 | unchanged | u,u |
| Stack underflow (STVREN=1) | STKUNF=1 | unchanged | u,u |
| Memory violation | unchanged | MEMV=0 | u,u |
| VREG/ULP fault | RVREG=0 | unchanged | 1,1 |
| Config memory | RCM=0 | unchanged | u,u |

Legend: u = unchanged, q = depends on condition.

## BOR Operating Modes (BOREN config bits)

| BOREN<1:0> | SBOREN | Mode | POR Release | Sleep Wake |
|---|---|---|---|---|
| 11 | X | Always on | Wait BORRDY=1 | Immediate |
| 10 | X | Off in Sleep | Wait BORRDY=1 | Wait BORRDY=1 |
| 01 | 1 | Software-enabled | Wait BORRDY=1 | Immediate |
| 01 | 0 | Software-disabled | Immediate | Immediate |
| 00 | X | Always off | Immediate | Immediate |

BOR is forced ON during PFM Bulk Erase at lowest BOR threshold, regardless of configuration.

## BORCON Register (0x0049)

| Bit | 7 | 6–1 | 0 |
|-----|---|-----|---|
| Field | SBOREN | — | BORRDY |
| Access | R/W | — | R |
| POR default | 1 | — | q |

- **SBOREN**: Software BOR enable. Only effective when BOREN=01.
- **BORRDY**: 1=BOR circuit active and armed; 0=disabled or warming up.

## MCLR Configuration

| MCLRE | LVP | MCLR |
|---|---|---|
| x | 1 | Enabled |
| 1 | 0 | Enabled |
| 0 | 0 | Disabled (RE3 = GPIO input) |

When MCLR disabled, pin becomes input-only with software-controlled weak pull-up.

## Start-Up Sequence

After POR/BOR release:
1. **PWRT** runs to completion (if enabled via PWRTS<1:0> config bits)
2. **OST** runs to completion (if required by oscillator source)
3. **MCLR** released (if enabled)

PWRT delays:

| PWRTS | Delay |
|-------|-------|
| 11 | Disabled |
| 10 | 64 ms |
| 01 | 16 ms |
| 00 | 1 ms |

## BOR Voltage Selection (BORV config bits)

| BORV | Voltage |
|------|---------|
| 11 | 1.90V |
| 10 | 2.45V |
| 01 | 2.7V |
| 00 | 2.85V |

## Key Configuration Bits

| Bit | Purpose |
|-----|---------|
| BOREN<1:0> | BOR operating mode |
| BORV<1:0> | BOR voltage threshold |
| LPBOREN | LPBOR enable (default disabled on erased device) |
| MCLRE | MCLR pin function |
| LVP | Low-voltage programming (affects MCLR) |
| STVREN | Stack overflow/underflow reset enable |
| PWRTS<1:0> | Power-up Timer delay |