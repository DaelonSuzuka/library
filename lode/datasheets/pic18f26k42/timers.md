# PIC18F26K42 Timer Peripherals — Lode Reference

## Timer0 (8/16-bit, prescaler, postscaler, async capable)

### Register Map
| Reg | Bits | Key Fields |
|-----|------|------------|
| T0CON0 | 8 | EN(7) OUT(5) MD16(4) OUTPS[3:0](3:0) |
| T0CON1 | 8 | CS[2:0](7:5) ASYNC(4) CKPS[3:0](3:0) |
| TMR0L | 8 | TMR0L[7:0] — counter low byte, reset=0x00 |
| TMR0H | 8 | Period (8-bit mode) / high byte (16-bit mode), reset=0xFF |

### Timer0 CS[2:0] — Clock Source (T0CON1 bits 7:5)
| Val | Source |
|-----|--------|
| 000 | T0CKIPPS (non-inverted) |
| 001 | T0CKIPPS (inverted) |
| 010 | FOSC/4 |
| 011 | HFINTOSC |
| 100 | LFINTOSC |
| 101 | MFINTOSC (500 kHz) |
| 110 | SOSC |
| 111 | CLC1_OUT |

### Timer0 CKPS[3:0] — Prescaler (T0CON1 bits 3:0)
| Val | Ratio | Val | Ratio | Val | Ratio | Val | Ratio |
|-----|-------|-----|-------|-----|-------|-----|--------|
| 0 | 1:1 | 4 | 1:16 | 8 | 1:256 | 12 | 1:4096 |
| 1 | 1:2 | 5 | 1:32 | 9 | 1:512 | 13 | 1:8192 |
| 2 | 1:4 | 6 | 1:64 | 10 | 1:1024 | 14 | 1:16384 |
| 3 | 1:8 | 7 | 1:128 | 11 | 1:2048 | 15 | 1:32768 |

### Timer0 OUTPS[3:0] — Postscaler (T0CON0 bits 3:0)
| Val | Ratio | Val | Ratio |
|-----|-------|-----|-------|
| 0 | 1:1 | 8 | 1:9 |
| 1 | 1:2 | 9 | 1:10 |
| 2 | 1:3 | 10 | 1:11 |
| 3 | 1:4 | 11 | 1:12 |
| 4 | 1:5 | 12 | 1:13 |
| 5 | 1:6 | 13 | 1:14 |
| 6 | 1:7 | 14 | 1:15 |
| 7 | 1:8 | 15 | 1:16 |

### Timer0 Notes
- **8-bit mode (MD16=0)**: TMR0H is period register (PR0). TMR0L resets on match.
- **16-bit mode (MD16=1)**: Read TMR0L first (latches TMR0H to buffer). Write TMR0L last (transfers buffer to high byte).
- **ASYNC=1**: Counter increments on each rising edge; operates during Sleep.
- **ASYNC=0**: Clock synchronized to FOSC/4 (max freq ≤ FOSC/4).
- Prescaler/postscaler cleared on: write to TMR0L, write to T0CON0/T0CON1, any Reset.
- IF set every (OUTPS+1) matches (8-bit) or rollovers (16-bit).

## Timer1/3/5 (16-bit, gate control, 2-bit prescaler, no postscaler)

### Register Map
| Reg | Key Fields |
|-----|------------|
| TxCON | —(7:6) CKPS[1:0](5:4) —(3) SYNC(2) RD16(1) ON(0) |
| TxGCON | GE(7) GPOL(6) GTM(5) GSPM(4) GGO/DONE(3) GVAL(2) —(1:0) |
| TxCLK | —(7:5) CS[4:0](4:0) |
| TxGATE | —(7:5) GSS[4:0](4:0) |
| TMRxL | TMRxL[7:0] |
| TMRxH | TMRxH[7:0] |

### Timer1/3/5 CS[4:0] — Clock Source (TxCLK bits 4:0)
| CS | Timer1 Source | Timer3 Source | Timer5 Source |
|----|---------------|----------------|---------------|
| 00000 | T1CKIPPS | T3CKIPPS | T5CKIPPS |
| 00001 | FOSC/4 | FOSC/4 | FOSC/4 |
| 00010 | FOSC | FOSC | FOSC |
| 00011 | HFINTOSC | HFINTOSC | HFINTOSC |
| 00100 | LFINTOSC | LFINTOSC | LFINTOSC |
| 00101 | MFINTOSC (500 kHz) | MFINTOSC (500 kHz) | MFINTOSC (500 kHz) |
| 00110 | MFINTOSC (32 kHz) | MFINTOSC (32 kHz) | MFINTOSC (32 kHz) |
| 00111 | SOSC | SOSC | SOSC |
| 01000 | CLKREF | CLKREF | CLKREF |
| 01001 | TMR0 overflow | TMR0 overflow | TMR0 overflow |
| 01010 | Reserved | TMR1 overflow | TMR1 overflow |
| 01011 | TMR3 overflow | Reserved | TMR3 overflow |
| 01100 | TMR5 overflow | TMR5 overflow | Reserved |
| 01101 | CLC1_OUT | CLC1_OUT | CLC1_OUT |
| 01110 | CLC2_OUT | CLC2_OUT | CLC2_OUT |
| 01111 | CLC3_OUT | CLC3_OUT | CLC3_OUT |
| 10000 | CLC4_OUT | CLC4_OUT | CLC4_OUT |
| 10001–11111 | Reserved | Reserved | Reserved |

**IMPORTANT**: CS=01010 is Timer1-only Reserved, Timer3=TMR1_overflow, Timer5=TMR1_overflow. CS=01011 is TMR3_overflow for T1 but Reserved for T3. These inter-timer references differ per timer instance.

### Timer1/3/5 CKPS[1:0] — Prescaler (TxCON bits 5:4)
| Val | Ratio |
|-----|-------|
| 00 | 1:1 |
| 01 | 1:2 |
| 10 | 1:4 |
| 11 | 1:8 |

### Timer1/3/5 GSS[4:0] — Gate Source (TxGATE bits 4:0)
| GSS | Source (per-timer differences noted) |
|-----|---------------------------------------|
| 00000 | TxGPPS pin |
| 00001 | TMR0 overflow |
| 00010 | Reserved(T1), TMR1 overflow(T3/T5) |
| 00011 | TMR2 postscaled |
| 00100 | TMR3 overflow(T1/T5), Reserved(T3) |
| 00101 | TMR4 postscaled |
| 00110 | TMR5 overflow(T1/T3), Reserved(T5) |
| 00111 | TMR6 postscaled |
| 01000 | SMT1_match |
| 01001–01100 | CCP1–CCP4 OUT |
| 01101–01111 | PWM5–PWM8 OUT |
| 10000 | PWM8OUT |
| 10001–10010 | Reserved |
| 10011 | NCO1OUT |
| 10100–10101 | CMP1/CMP2 OUT |
| 10110 | ZCDOUT |
| 10111–11010 | CLC1–CLC4 OUT |
| 11011–11111 | Reserved |

### Timer1/3/5 Notes
- **SYNC bit**: When TMRxCLK=FOSC/4 or FOSC, SYNC is ignored (clock used as-is). Else: SYNC=1 = async, SYNC=0 = sync to FOSC/4.
- **RD16**: Set before 16-bit reads/writes. Read TMRxL first (latches TMRxH). Preload TMRxH buffer before writing TMRxL.
- **Counter mode gotcha**: After POR, TMRx write, or disable, a falling edge on TxCKI must occur before first rising edge is counted.
- **Sync/async switching**: sync→async may skip an increment; async→sync may add an extra increment.
- **CCP Special Event Trigger**: Clears TMRx without setting IF. Requires synchronous + FOSC/4.
- **Gate modes**: GE=1+ON=1 → count controlled by gate; GE=0+ON=1 → always count.

## Timer2/4/6 (8-bit HLT, prescaler, postscaler, period register)

### Register Map
| Reg | Key Fields | Notes |
|-----|------------|-------|
| TxTMR | TMRx[7:0](7:0) | Counter, reset=0x00 |
| TxPR | PRx[7:0](7:0) | Period, reset=0xFF |
| TxCON | ON(7) CKPS[2:0](6:4) OUTPS[3:0](3:0) | ON is R/W/HC — HW clears in One-Shot |
| TxHLT | PSYNC(7) CKPOL(6) CKSYNC(5) MODE[4:0](4:0) | |
| TxCLK | —(7:4) CS[3:0](3:0) | |
| TxRST | —(7:5) RSEL[4:0](4:0) | |

### Timer2/4/6 CS[3:0] — Clock Source (TxCLK bits 3:0)
| Val | Source |
|-----|--------|
| 0000 | TxINPPS (pin) |
| 0001 | FOSC/4 |
| 0010 | FOSC |
| 0011 | HFINTOSC |
| 0100 | LFINTOSC |
| 0101 | MFINTOSC (500 kHz) |
| 0110 | MFINTOSC (32 kHz) |
| 0111 | SOSC |
| 1000 | CLKREF_OUT |
| 1001 | NCO1OUT |
| 1010 | ZCD_OUT |
| 1011 | CLC1_OUT |
| 1100 | CLC2_OUT |
| 1101 | CLC3_OUT |
| 1110 | CLC4_OUT |
| 1111 | Reserved |

### Timer2/4/6 RSEL[4:0] — Reset Source (TxRST bits 4:0)
| RSEL | Source (T2/T4/T6 notes) |
|------|-------------------------|
| 00000 | TxINPPS pin |
| 00001 | Reserved(T2), T2TMR postscaled(T4/T6) |
| 00010 | TMR4 postscaled(T2/T6), Reserved(T4) |
| 00011 | TMR6 postscaled(T2/T4), Reserved(T6) |
| 00100–00111 | CCP1–CCP4 OUT |
| 01000–01011 | PWM5–PWM8 OUT |
| 01100–01101 | Reserved |
| 01110–01111 | CMP1OUT, CMP2OUT |
| 10000 | ZCD_OUT |
| 10001–10100 | CLC1–CLC4 OUT |
| 10101–10110 | UART1 rx/tx edge |
| 10111–11000 | UART2 rx/tx edge |
| 11001–11111 | Reserved |

### Timer2/4/6 CKPS[2:0] — Prescaler (TxCON bits 6:4)
| Val | Ratio |
|-----|-------|
| 000 | 1:1 |
| 001 | 1:2 |
| 010 | 1:4 |
| 011 | 1:8 |
| 100 | 1:16 |
| 101 | 1:32 |
| 110 | 1:64 |
| 111 | 1:128 |

### Timer2/4/6 OUTPS[3:0] — Postscaler (TxCON bits 3:0)
Same encoding as Timer0. TMR2IF set every (OUTPS+1) period matches.

### Timer2/4/6 HLT MODE[4:0] — Operating Mode (TxHLT bits 4:0)
| MODE | Category | Operation |
|------|----------|-----------|
| 00000 | Free Running Period | Software gate |
| 00001 | | Hardware gate, active-high |
| 00010 | | Hardware gate, active-low |
| 00011 | | Rising/Falling edge reset |
| 00100 | | Rising edge reset |
| 00101 | | Falling edge reset |
| 00110 | | Low level reset |
| 00111 | | High level reset |
| 01000 | One-Shot | Software start |
| 01001 | | Rising edge start |
| 01010 | | Falling edge start |
| 01011 | | Any edge start |
| 01100 | | Rising edge start & reset |
| 01101 | | Falling edge start & reset |
| 01110 | | Low level reset, rising edge start |
| 01111 | | High level reset, falling edge start |
| 10000 | Monostable | Reserved |
| 10001 | | Rising edge start |
| 10010 | | Falling edge start |
| 10011 | | Any edge start |
| 10110 | | Low level start, high level reset |
| 10111 | | High level start, low level reset |

### TxHLT Control Bits
- **PSYNC(7)**: 1=sync prescaler output to FOSC/4 (prevents Sleep); 0=async (valid for Sleep).
- **CKPOL(6)**: 1=falling edge clocks timer; 0=rising edge. Do not change while ON=1.
- **CKSYNC(5)**: 1=ON sync'd to timer clock (glitch-free, +2 clock delay); 0=ON sync'd to FOSC/4.

### Timer2/4/6 Notes
- **Period**: TxTMR resets to 0x00 on match with TxPR (not rollover). Period = (TxPR+1) × prescaler × postscaler.
- **Writing TxCON**: Clears prescaler and postscaler counters but does NOT clear TxTMR.
- **Writing TxTMR**: Clears both prescaler and postscaler counters.
- **One-Shot**: ON bit auto-cleared by hardware on TxPR match. OUTPS >0 is meaningless (timer stops at first match).
- **Edge-triggered modes**: Need 6 timer clocks between external triggers.
- **Level-triggered modes**: Triggering level must be ≥3 timer clock periods.

## Operational Summary

| Feature | Timer0 | Timer1/3/5 | Timer2/4/6 |
|---------|--------|------------|------------|
| Width | 8 or 16-bit | 16-bit only | 8-bit only |
| Period reg | TMR0H (8-bit) | None (rollover FFFF) | TxPR (separate) |
| Prescaler | 1:1–1:32768 | 1:1–1:8 | 1:1–1:128 |
| Postscaler | 1:1–1:16 | None | 1:1–1:16 |
| Gate control | None | Full (GE/GPOL/GTM/GSPM) | Via HLT MODE |
| Async | ASYNC bit | SYNC bit (1=async) | PSYNC/CSYNC bits |
| Clock field | 3-bit | 5-bit | 4-bit |
| One-shot | No | No | Yes (HLT) |
| External reset | No | No | TxRST register |

## K42 Errata — Timer-Related

No timer-specific silicon errata documented for K42 (rev A1/A3). Timers operate per datasheet. However, note:
- UART BRGS in DALI mode broken (A3): if using Timer2 HLT for UART stop-bit detection workaround, ensure HLT is configured correctly.