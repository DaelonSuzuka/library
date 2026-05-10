# PIC18F27/47/57Q43 Timer Peripherals — Lode Reference

## Timer0 (8/16-bit, prescaler, postscaler, async capable)

### Register Map
| Reg | Addr | Key Fields |
|-----|------|------------|
| T0CON0 | 0x31A | EN(7) OUT(5) MD16(4) OUTPS[3:0](3:0) |
| T0CON1 | 0x31B | CS[2:0](7:5) ASYNC(4) CKPS[3:0](3:0) |
| TMR0L | 0x318 | TMR0L[7:0] — counter low byte, reset=0x00 |
| TMR0H | 0x319 | Period (8-bit mode) / high byte (16-bit mode), reset=0xFF |

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
- **8-bit mode (MD16=0)**: TMR0H is period register. TMR0L resets on match.
- **16-bit mode (MD16=1)**: Read TMR0L first (latches TMR0H). Write TMR0L last (transfers buffer to high byte). Cannot write while running.
- **ASYNC=1**: Counter increments on each rising edge; operates during Sleep.
- **ASYNC=0**: Clock synchronized to FOSC/4 (max freq ≤ FOSC/4).
- Prescaler/postscaler cleared on: write to TMR0L, write to T0CON0/T0CON1, any Reset.
- IF set every (OUTPS+1) matches (8-bit) or rollovers (16-bit).

## Timer1/3/5 (16-bit, gate control, 2-bit prescaler, no postscaler)

Instances: Timer1 (T1), Timer3 (T3), Timer5 (T5).

### Register Map
| Reg | Addrs | Key Fields |
|-----|-------|------------|
| TxCON | 0x31E,0x32A,0x336 | —(7:6) CKPS[1:0](5:4) —(3) SYNC(2) RD16(1) ON(0) |
| TxGCON | 0x31F,0x32B,0x337 | GE(7) GPOL(6) GTM(5) GSPM(4) GGO/DONE(3) GVAL(2) —(1:0) |
| TxCLK | 0x321,0x32D,0x339 | —(7:5) CS[4:0](4:0) |
| TxGATE | 0x320,0x32C,0x338 | —(7:6) GSS[5:0](5:0) |
| TMRx | 0x31C,0x328,0x334 | TMRx[15:8]:TMRx[7:0] — 16-bit timer, reset=0x0000 |

### Timer1/3/5 CS[4:0] — Clock Source (TxCLK bits 4:0)
| CS | Timer1 Source | Timer3 Source | Timer5 Source |
|----|---------------|---------------|---------------|
| 00000 | T1CKIPPS | T3CKIPPS | T5CKIPPS |
| 00001 | FOSC/4 | FOSC/4 | FOSC/4 |
| 00010 | FOSC | FOSC | FOSC |
| 00011 | HFINTOSC | HFINTOSC | HFINTOSC |
| 00100 | LFINTOSC | LFINTOSC | LFINTOSC |
| 00101 | MFINTOSC (500 kHz) | MFINTOSC (500 kHz) | MFINTOSC (500 kHz) |
| 00110 | MFINTOSC (31.25 kHz) | MFINTOSC (31.25 kHz) | MFINTOSC (31.25 kHz) |
| 00111 | SOSC | SOSC | SOSC |
| 01000 | EXTOSC | EXTOSC | EXTOSC |
| 01001 | CLKREF_OUT | CLKREF_OUT | CLKREF_OUT |
| 01010 | TMR0_OUT | TMR0_OUT | TMR0_OUT |
| 01011 | Reserved | TMR1_OUT | TMR1_OUT |
| 01100 | TMR3_OUT | Reserved | TMR3_OUT |
| 01101 | TMR5_OUT | TMR5_OUT | Reserved |
| 01110 | CLC1_OUT | CLC1_OUT | CLC1_OUT |
| 01111 | CLC2_OUT | CLC2_OUT | CLC2_OUT |
| 10000 | CLC3_OUT | CLC3_OUT | CLC3_OUT |
| 10001 | CLC4_OUT | CLC4_OUT | CLC4_OUT |
| 10010 | CLC5_OUT | CLC5_OUT | CLC5_OUT |
| 10011 | CLC6_OUT | CLC6_OUT | CLC6_OUT |
| 10100 | CLC7_OUT | CLC7_OUT | CLC7_OUT |
| 10101 | CLC8_OUT | CLC8_OUT | CLC8_OUT |
| 10110–11111 | Reserved | Reserved | Reserved |

**IMPORTANT**: CS=01011 is Reserved for Timer1, TMR1_OUT for Timer3/5. CS=01100 is TMR3_OUT for Timer1/5, Reserved for Timer3. Inter-timer cross-references differ per instance.

### Timer1/3/5 CKPS[1:0] — Prescaler (TxCON bits 5:4)
| Val | Ratio |
|-----|-------|
| 00 | 1:1 |
| 01 | 1:2 |
| 10 | 1:4 |
| 11 | 1:8 |

### Timer1/3/5 GSS[5:0] — Gate Source (TxGATE bits 5:0)
| GSS | Source (per-timer differences noted) |
|-----|---------------------------------------|
| 000000 | TxGPPS pin |
| 000001 | TMR0_OUT |
| 000010 | Reserved(T1), TMR1_OUT(T3/T5) |
| 000011 | TMR2_Postscaler_OUT |
| 000100 | TMR3_OUT(T1/T5), Reserved(T3) |
| 000101 | TMR4_Postscaler_OUT |
| 000110 | TMR5_OUT(T1/T3), Reserved(T5) |
| 000111 | TMR6_Postscaler_OUT |
| 001000 | SMT1_OUT |
| 001001 | CCP1_OUT |
| 001010 | CCP2_OUT |
| 001011 | CCP3_OUT |
| 001100 | PWM1S1P1_OUT |
| 001101 | PWM1S1P2_OUT |
| 001110 | PWM2S1P1_OUT |
| 001111 | PWM2S1P2_OUT |
| 010000 | PWM3S1P1_OUT |
| 010001 | PWM3S1P2_OUT |
| 010010–010011 | Reserved |
| 010100 | NCO1_OUT |
| 010101 | NCO2_OUT |
| 010110 | NCO3_OUT |
| 010111 | CMP1_OUT |
| 011000 | CMP2_OUT |
| 011001 | ZCD_OUT |
| 011010 | CLC1_OUT |
| 011011 | CLC2_OUT |
| 011100 | CLC3_OUT |
| 011101 | CLC4_OUT |
| 011110 | CLC5_OUT |
| 011111 | CLC6_OUT |
| 100000 | CLC7_OUT |
| 100001 | CLC8_OUT |
| 100010–111111 | Reserved |

### Timer1/3/5 Notes
- **SYNC bit**: When CS=FOSC/4 or FOSC, SYNC is ignored. Else: SYNC=1=async, SYNC=0=sync to FOSC/4.
- **RD16**: Set before 16-bit reads/writes. Read TMRxL first (latches TMRxH). Preload TMRxH buffer before writing TMRxL.
- **Counter mode**: After POR, TMRx write, or disable, a falling edge on TxCKI must occur before first rising edge is counted.
- **Gate modes**: GE=1+ON=1 → count controlled by gate; GE=0+ON=1 → always count.
- **CCP Special Event Trigger**: Clears TMRx without setting IF. Requires synchronous + FOSC/4.

## Timer2/4/6 (8-bit HLT, prescaler, postscaler, period register)

Instances: Timer2 (T2), Timer4 (T4), Timer6 (T6).

### Register Map
| Reg | Addrs | Key Fields |
|-----|-------|------------|
| TxTMR | 0x322,0x32E,0x33A | TxTMR[7:0](7:0) — counter, reset=0x00 |
| TxPR | 0x323,0x32F,0x33B | TxPR[7:0](7:0) — period, reset=0xFF |
| TxCON | 0x324,0x330,0x33C | ON(7) CKPS[2:0](6:4) OUTPS[3:0](3:0). ON is R/W/HC |
| TxHLT | 0x325,0x331,0x33D | PSYNC(7) CKPOL(6) CKSYNC(5) MODE[4:0](4:0) |
| TxCLKCON | 0x326,0x332,0x33E | —(7:5) CS[4:0](4:0) |
| TxRST | 0x327,0x333,0x33F | —(7:6) RSEL[5:0](5:0) |

### Timer2/4/6 CS[4:0] — Clock Source (TxCLKCON bits 4:0)
| CS | Source |
|----|--------|
| 00000 | TxINPPS (pin) |
| 00001 | FOSC/4 |
| 00010 | FOSC |
| 00011 | HFINTOSC |
| 00100 | LFINTOSC |
| 00101 | MFINTOSC (500 kHz) |
| 00110 | MFINTOSC (31.25 kHz) |
| 00111 | SOSC |
| 01000 | EXTOSC |
| 01001 | CLKREF_OUT |
| 01010 | NCO1_OUT |
| 01011 | NCO2_OUT |
| 01100 | NCO3_OUT |
| 01101 | ZCD_OUT |
| 01110 | CLC1_OUT |
| 01111 | CLC2_OUT |
| 10000 | CLC3_OUT |
| 10001 | CLC4_OUT |
| 10010 | CLC5_OUT |
| 10011 | CLC6_OUT |
| 10100 | CLC7_OUT |
| 10101 | CLC8_OUT |
| 10110–11111 | Reserved |

**IMPORTANT**: Q43 Timer2 CS field is 5 bits wide (CS[4:0]), unlike K42 which uses 4 bits (CS[3:0]). Q43 adds values 01000 (EXTOSC), 01001 (CLKREF_OUT), 01010–01100 (NCO1–3_OUT), and 10010–10101 (CLC5–8_OUT) vs K42. The encoding values 00000–00111 are compatible between K42 and Q43 except Q43 shifts CLKREF to 01001 (was 1000 on K42) and adds EXTOSC at 01000.

### Timer2/4/6 RSEL[5:0] — Reset Source (TxRST bits 5:0)
| RSEL | Source (T2/T4/T6 notes) |
|------|-------------------------|
| 000000 | TxINPPS pin |
| 000001 | Reserved(T2), T2_Postscaler_OUT(T4/T6) |
| 000010 | TMR4_Postscaler_OUT(T2/T6), Reserved(T4) |
| 000011 | TMR6_Postscaler_OUT(T2/T4), Reserved(T6) |
| 000100 | CCP1_OUT |
| 000101 | CCP2_OUT |
| 000110 | CCP3_OUT |
| 000111 | PWM1S1P1_OUT |
| 001000 | PWM1S1P2_OUT |
| 001001 | PWM2S1P1_OUT |
| 001010 | PWM2S1P2_OUT |
| 001011 | PWM3S1P1_OUT |
| 001100 | PWM3S1P2_OUT |
| 001101 | Reserved |
| 001110 | Reserved |
| 001111 | CMP1_OUT |
| 010000 | CMP2_OUT |
| 010001 | ZCD_OUT |
| 010010 | CLC1_OUT |
| 010011 | CLC2_OUT |
| 010100 | CLC3_OUT |
| 010101 | CLC4_OUT |
| 010110 | CLC5_OUT |
| 010111 | CLC6_OUT |
| 011000 | CLC7_OUT |
| 011001 | CLC8_OUT |
| 011010 | U1RX_Edge |
| 011011 | U1TX_Edge |
| 011100 | U2RX_Edge |
| 011101 | U2TX_Edge |
| 011110 | U3RX_Edge |
| 011111 | U3TX_Edge |
| 100000 | U4RX_Edge |
| 100001 | U4TX_Edge |
| 100010 | U5RX_Edge |
| 100011 | U5TX_Edge |
| 100100–111111 | Reserved |

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
Same encoding as Timer0. TMRxIF set every (OUTPS+1) period matches.

### Timer2/4/6 HLT MODE[4:0] — Operating Mode (TxHLT bits 4:0)
| MODE | Category | Operation |
|------|----------|-----------|
| 00000 | Free Running Period | Software gate |
| 00001 | | Hardware gate, active-high |
| 00010 | | Hardware gate, active-low |
| 00011 | | Rising/falling edge reset |
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
| 10001 | Monostable | Rising edge start |
| 10010 | | Falling edge start |
| 10011 | | Any edge start |
| 10110 | One Shot + HW Reset | Low level start, high level reset |
| 10111 | | High level start, low level reset |

### TxHLT Control Bits
- **PSYNC(7)**: 1=sync prescaler output to FOSC/4 (prevents Sleep); 0=async.
- **CKPOL(6)**: 1=falling edge clocks timer; 0=rising edge. Do not change while ON=1.
- **CKSYNC(5)**: 1=ON sync'd to timer clock (glitch-free, +2 clock delay); 0=ON sync'd to FOSC/4.

### Timer2/4/6 Notes
- **Period**: TxTMR resets to 0x00 on match with TxPR. Period = (TxPR+1) × prescaler × postscaler.
- **Writing TxCON**: Clears prescaler and postscaler counters but does NOT clear TxTMR.
- **Writing TxTMR**: Clears both prescaler and postscaler counters.
- **One-Shot**: ON bit auto-cleared by hardware on TxPR match. OUTPS >0 meaningless in one-shot.
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
| Async | ASYNC bit | SYNC bit (1=async) | PSYNC/CKSYNC bits |
| Clock field | 3-bit (CS[2:0]) | 5-bit (CS[4:0]) | 5-bit (CS[4:0]) |
| One-shot | No | No | Yes (HLT) |
| External reset | No | No | TxRST register |

## Q43 Errata — Timer-Related

No timer-specific silicon errata documented for Q43 (revisions B0–C0). SMT Reset Bit errata (1.6.1): if using SMT as timer clock source via CLC, do not set SMT RST bit while prescaler is non-zero.