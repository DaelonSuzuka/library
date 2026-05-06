# PIC18F16Q41 Timer Peripherals — Lode Reference

## Register Maps

### Timer0 (8/16-bit, prescaler, postscaler, async capable)
| Reg      | Addr   | Bits | Key Fields                               |
|----------|--------|------|------------------------------------------|
| TMR0L    | 0x318  | 8    | TMR0L[7:0] — counter low byte            |
| TMR0H    | 0x319  | 8    | TMR0H[7:0] — period (8-bit) / high byte  |
| T0CON0   | 0x31A  | 8    | EN(7) OUT(5) MD16(4) OUTPS[3:0](3:0)    |
| T0CON1   | 0x31B  | 8    | CS[2:0](7:5) ASYNC(4) CKPS[3:0](3:0)    |

TMR0H reset = 0xFF. TMR0L reset = 0x00.

### Timer1/3 (16-bit, gate control, 2-bit prescaler, no postscaler)
| Reg      | Addr (T1/T3)    | Key Fields                                |
|----------|-----------------|-------------------------------------------|
| TMRxL    | 0x312 / 0x323   | TMRx[7:0]                                 |
| TMRxH    | 0x313 / 0x324   | TMRx[15:8]                                |
| TxCON    | 0x314 / 0x325   | CKPS[1:0](5:4) SYNC(2) RD16(1) ON(0)     |
| TxGCON   | 0x315 / 0x326   | GE(7) GPOL(6) GTM(5) GSPM(4) GGO(3) GVAL(2) |
| TxGATE   | 0x316 / 0x327   | GSS[4:0](4:0)                             |
| TxCLK    | 0x317 / 0x328   | CS[4:0](4:0)                              |

### Timer2/4 (8-bit, HLT, prescaler, postscaler, period register)
| Reg      | Addr (T2/T4)    | Key Fields                                |
|----------|-----------------|-------------------------------------------|
| TxTMR    | 0x31C / 0x329   | TxTMR[7:0] — counter, reset=0x00         |
| TxPR     | 0x31D / 0x32A   | TxPR[7:0] — period, reset=0xFF           |
| TxCON    | 0x31E / 0x32B   | ON(7) CKPS[2:0](6:4) OUTPS[3:0](3:0)     |
| TxHLT    | 0x31F / 0x32C   | PSYNC(7) CPOL(6) CSYNC(5) MODE[4:0](4:0) |
| TxCLKCON | 0x320 / 0x32D   | CS[3:0](3:0)                              |
| TxRST    | 0x321 / 0x32E   | RSEL[4:0](4:0)                            |

ON bit in T2CON is R/W/HC (hardware can clear in One-Shot modes).

## Clock Source Encodings

### Timer0 CS[2:0] (3 bits, in T0CON1)
| Val | Source                 |
|-----|------------------------|
| 000 | T0CKIPPS (non-inverted)|
| 001 | T0CKIPPS (inverted)    |
| 010 | FOSC/4                |
| 011 | HFINTOSC              |
| 100 | LFINTOSC              |
| 101 | MFINTOSC (500 kHz)    |
| 110 | SOSC                  |
| 111 | CLC1_OUT              |

### Timer1 CS[4:0] (5 bits, in T1CLK)
| Val  | Source              | Val  | Source      |
|------|---------------------|------|-------------|
| 00000| T1CKIPPS            | 01011| Reserved    |
| 00001| FOSC/4              | 01100| TMR3_OUT    |
| 00010| FOSC                | 01101| CLC1_OUT    |
| 00011| HFINTOSC            | 01110| CLC2_OUT    |
| 00100| LFINTOSC            | 01111| CLC3_OUT    |
| 00101| MFINTOSC (500 kHz)  | 10000| CLC4_OUT    |
| 00110| MFINTOSC (32 kHz)   | 10001+| Reserved   |
| 00111| SOSC                |      |             |
| 01000| EXTOSC              |      |             |
| 01001| CLKREF_OUT          |      |             |
| 01010| TMR0_OUT            |      |             |

Note: 01011 Reserved on Q41. On Q43/Q84 with Timer5, this maps differently.

### Timer2 CS[3:0] (4 bits, in T2CLKCON)
| Val | Source               | Val | Source     |
|-----|----------------------|-----|-----------|
| 0000| T2INPPS              | 1000| EXTOSC    |
| 0001| FOSC/4               | 1001| CLKREF_OUT|
| 0010| FOSC                 | 1010| NCO1_OUT  |
| 0011| HFINTOSC             | 1011| ZCD_OUT   |
| 0100| LFINTOSC             | 1100| CLC1_OUT |
| 0101| MFINTOSC (500 kHz)   | 1101| CLC2_OUT |
| 0110| MFINTOSC (32 kHz)    | 1110| CLC3_OUT |
| 0111| SOSC                 | 1111| CLC4_OUT |

## Prescaler Tables

### Timer0 CKPS[3:0] — 16 options
| Val | Ratio | Val | Ratio  | Val | Ratio | Val | Ratio  |
|-----|-------|-----|--------|-----|-------|-----|--------|
| 0   | 1:1   | 4   | 1:16   | 8   | 1:256 | 12  | 1:4096 |
| 1   | 1:2   | 5   | 1:32   | 9   | 1:512 | 13  | 1:8192 |
| 2   | 1:4   | 6   | 1:64   | 10  | 1:1024| 14  | 1:16384|
| 3   | 1:8   | 7   | 1:128  | 11  | 1:2048| 15  | 1:32768|

### Timer1 CKPS[1:0] — 4 options
| Val | Ratio |
|-----|-------|
| 00  | 1:1   |
| 01  | 1:2   |
| 10  | 1:4   |
| 11  | 1:8   |

### Timer2 CKPS[2:0] — 8 options
| Val | Ratio | Val | Ratio |
|-----|-------|-----|-------|
| 000 | 1:1   | 100 | 1:16  |
| 001 | 1:2   | 101 | 1:32  |
| 010 | 1:4   | 110 | 1:64  |
| 011 | 1:8   | 111 | 1:128 |

## Postscaler Tables

### Timer0/2 OUTPS[3:0] — 16 options (same encoding)
| Val | Ratio | Val | Ratio |
|-----|-------|-----|-------|
| 0   | 1:1   | 8   | 1:9   |
| 1   | 1:2   | 9   | 1:10  |
| 2   | 1:3   | 10  | 1:11  |
| 3   | 1:4   | 11  | 1:12  |
| 4   | 1:5   | 12  | 1:13  |
| 5   | 1:6   | 13  | 1:14  |
| 6   | 1:7   | 14  | 1:15  |
| 7   | 1:8   | 15  | 1:16  |

Timer1/3 have **no postscaler**. IF flag fires on every overflow.

Postscaler formula: TMR0IF set every (OUTPS+1) matches/rollovers.

## Operational Differences

| Feature              | Timer0          | Timer1/3            | Timer2/4            |
|----------------------|-----------------|----------------------|---------------------|
| Width                | 8 or 16-bit     | 16-bit only          | 8-bit only          |
| Period reg           | TMR0H (8-bit)   | None (rollover FFFF) | TxPR (separate reg) |
| Prescaler range      | 1:1–1:32768     | 1:1–1:8              | 1:1–1:128           |
| Postscaler           | 1:1–1:16        | None                | 1:1–1:16            |
| Gate control         | None            | Full (GE/GPOL/GTM/GSPM)| Via HLT MODE bits|
| Async operation      | ASYNC bit       | SYNC bit (active low) | PSYNC/CSYNC bits   |
| 16-bit read/write    | Buffered via TMR0L| RD16 bit enables  | N/A (8-bit)         |
| Sleep operation      | Async only       | Async + non-FOSC src  | PSYNC=0 + active clk|
| CCP time base        | No              | Yes (capture/compare) | Yes (PWM period)   |
| Output routing       | T0OUT via PPS   | TMR1_overflow        | TMR2_postscaled     |
| Clock source field   | 3-bit (8 opts)  | 5-bit (many opts)    | 4-bit (16 opts)     |
| One-shot modes       | No              | No                   | Yes (via HLT MODE)  |
| External reset       | No              | No                   | TxRST register      |

## Key Setup Procedures & Gotchas

### Timer0
- **8-bit mode**: TMR0H is period register. TMR0L resets to 0 on match.
- **16-bit mode**: Read TMR0L first (latches TMR0H to buffer). Write TMR0L last
  (transfers TMR0H buffer to high byte). Cannot write while running in 16-bit.
- **Prescaler reset**: Writing TMR0L, T0CON0, or T0CON1 clears prescaler counter.
- **Async + Sleep**: Set ASYNC=1 and use clock source active in Sleep (SOSC, LFINTOSC).

### Timer1
- **Enable sequence**: ON=1, GE=1 for gate mode; ON=1, GE=0 for always-on.
- **RD16**: Set before reading/writing. Read TMR1L first (latches TMR1H buffer).
  Pre-load TMR1H buffer before writing TMR1L.
- **Counter mode gotcha**: After POR, TMRx write, or disable, a falling edge on
  TxCKI must occur before the first rising edge is counted.
- **Async read/write**: Hardware ensures valid individual byte reads, but 16-bit
  coherence requires RD16. Stop timer before writing in async mode.
- **Sync/async switching**: synch→async may skip an increment; async→synch may
  add an extra increment.
- **CCP Special Event Trigger**: Clears TMRx without setting IF. Requires
  FOSC/4 + synchronous mode.
- **SOSC startup**: Set SOSCEN in OSCEN, wait for ready flag before enabling Timer1.

### Timer2
- **Period**: T2TMR resets to 0x00 on match with T2PR (not rollover). Period =
  (T2PR+1) × prescaler × postscaler clock cycles.
- **Writing T2CON**: Clears prescaler and postscaler counters, but does NOT clear T2TMR.
- **Writing T2TMR**: Clears both prescaler and postscaler counters.
- **PSYNC**: Must set when reading TxTMR with async clock. Prescaler output must
  be < FOSC/4 when PSYNC=1. PSYNC=1 prevents Sleep operation.
- **CSYNC**: Set to synchronize ON bit to timer clock (avoids glitches, costs 1
  clock cycle). Clear to sync ON to FOSC/4 (no delay, but glitch risk).
- **CPOL**: Must not change while ON=1.
- **One-shot**: ON bit auto-cleared by hardware on TxPR match.
- **Postscaler in One-shot**: OUTPS values >0 are ignored (timer stops at first match).
- **Edge-triggered modes**: Require 6 timer clock periods between external triggers.
- **Level-triggered modes**: Triggering level must be >=3 timer clock periods.

## Cross-Check: timer_constants.h vs Datasheet (Q41)

### Timer0 Clock Source — MATCH
Enum values 0–7 match datasheet T0CON1 CS[2:0] exactly.

### Timer1 Clock Source — MISMATCHES
The Q41 is grouped under `#if FAMILY_Q43 || FAMILY_Q84 || FAMILY_Q41` but Q41
has a different CS mapping (fewer CLCs, no Timer5):

| Enum                  | Header Val | Datasheet Val | Status  |
|-----------------------|------------|---------------|---------|
| TMR1_CLK_PPS          | 0b00000    | 00000         | OK      |
| TMR1_CLK_FOSC4        | 0b00001    | 00001         | OK      |
| TMR1_CLK_FOSC         | 0b00010    | 00010         | OK      |
| TMR1_CLK_HFINTOSC     | 0b00011    | 00011         | OK      |
| TMR1_CLK_LFINTOSC     | 0b00100    | 00100         | OK      |
| TMR1_CLK_MFINTOSC_500k| 0b00101    | 00101         | OK      |
| TMR1_CLK_MFINTOSC_32k | 0b00110    | 00110         | OK      |
| TMR1_CLK_SOSC         | 0b00111    | 00111         | OK      |
| TMR1_CLK_EXTOSC       | 0b01000    | 01000         | OK      |
| TMR1_CLK_CLKREF       | 0b01001    | 01001         | OK      |
| TMR1_CLK_TMR0         | 0b01010    | 01010         | OK      |
| TMR1_CLK_TMR1         | 0b01011    | Reserved      | WRONG   |
| TMR1_CLK_TMR3         | 0b01100    | 01100         | OK      |
| TMR1_CLK_TMR5         | 0b01101    | =CLC1_OUT     | WRONG   |
| TMR1_CLK_CLC1         | 0b01110    | 01101         | WRONG   |
| TMR1_CLK_CLC2         | 0b01111    | 01110         | WRONG   |
| TMR1_CLK_CLC3         | 0b10000    | 01111         | WRONG   |
| TMR1_CLK_CLC4         | 0b10001    | 10000         | WRONG   |

CLC1–CLC4 encodings are all off by +1. TMR1_CLK_TMR1=01011 is Reserved on Q41.
TMR1_CLK_TMR5=01101 maps to CLC1_OUT on Q41 (Q41 has no Timer5). CLC5–CLC8
entries (header values 17–21) are invalid for Q41 (CS[4:0] 10001+ = Reserved).

### Timer2 Clock Source — MISMATCHES
Timer2 CS is 4 bits on Q41, but header uses 5-bit literals for a Q43/Q84 layout:

| Enum               | Header Val | Datasheet Val | Status |
|--------------------|------------|---------------|--------|
| TMR2_CLK_PPS       | 0b00000    | 0000          | OK     |
| TMR2_CLK_FOSC4     | 0b00001    | 0001          | OK     |
| TMR2_CLK_FOSC      | 0b00010    | 0010          | OK     |
| TMR2_CLK_HFINTOSC  | 0b00011    | 0011          | OK     |
| TMR2_CLK_LFINTOSC  | 0b00100    | 0100          | OK     |
| TMR2_CLK_MFINTOSC_500k|0b00101   | 0101          | OK     |
| TMR2_CLK_MFINTOSC_32k |0b00110   | 0110          | OK     |
| TMR2_CLK_SOSC      | 0b00111    | 0111          | OK     |
| TMR2_CLK_EXTOSC    | 0b01000    | 1000          | OK     |
| TMR2_CLK_CLKREF    | 0b01001    | 1001          | OK     |
| TMR2_CLK_NCO1      | 0b01010    | 1010          | OK     |
| TMR2_CLK_NCO2      | 0b01011    | =ZCD_OUT(1011) | WRONG |
| TMR2_CLK_NCO3      | 0b01100    | =CLC1(1100)   | WRONG  |
| TMR2_CLK_ZCD       | 0b01101    | 1011          | WRONG  |
| TMR2_CLK_CLC1      | 0b01110    | 1100          | WRONG  |
| TMR2_CLK_CLC2      | 0b01111    | 1101          | WRONG  |
| TMR2_CLK_CLC3      | 0b10000    | 1110          | WRONG  |
| TMR2_CLK_CLC4      | 0b10001    | 1111          | WRONG  |
| TMR2_CLK_CLC5–8    | 18–21      | N/A (>4-bit)  | INVALID|

Q41 Timer2 has no NCO2, NCO3. ZCD is at CS=1011, not 1101. CLC1–4 start at
CS=1100, not 1110. Header appears to use Q43/Q84 mapping. Q41 needs its own
`#elif FAMILY_Q41` section.

### Prescaler/Postscaler Enums — MATCH
`timer_prescale` and `timer_postscale` enums match datasheet bit-for-bit.
Caveat: Timer1 only uses CKPS[1:0] (values 0–3 valid); values 4–15 are
applicable only to Timer0/2. Timer2 only uses CKPS[2:0] (values 0–7 valid);
values 8–15 only apply to Timer0.