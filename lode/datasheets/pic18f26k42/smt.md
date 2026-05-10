# PIC18F26K42 — Signal Measurement Timer (SMT1)

## Overview

24-bit counter/accumulator with advanced clock and gating logic. One instance (SMT1). Measures pulse width, frequency, duty cycle, and time between edges.

## Operating Modes (MODE<3:0> in SMT1CON1)

| MODE | Function | Sync? |
|------|----------|-------|
| 0000 | Timer | Yes |
| 0001 | Gated Timer | Yes |
| 0010 | Period & Duty Cycle Acquisition | Yes |
| 0011 | High & Low Time Measurement | Yes |
| 0100 | Windowed Measure | Yes |
| 0101 | Gated Windowed Measure | Yes |
| 0110 | Time of Flight | Yes |
| 0111 | Capture | Yes |
| 1000 | Counter | No |
| 1001 | Gated Counter | No |
| 1010 | Windowed Counter | No |
| 1011–1111 | Reserved | — |

- **REPEAT** bit (SMT1CON1): 0=Single acquisition (GO cleared on completion), 1=Repeat.
- **STP** bit (SMT1CON0): 1=Halt at period match, 0=Reset to zero at period match.
- **GO** bit (SMT1CON1): Set to start; hardware clears on single-acquisition completion.

## Key Registers

| Register | Bits | Purpose |
|---|---|---|
| SMT1CON0 | EN, STP, WPOL, SPOL, CPOL, PS<1:0> | Enable, halt, window/signal/clock polarity, prescale |
| SMT1CON1 | GO, REPEAT, MODE<3:0> | Start, repeat, mode select |
| SMT1STAT | CPRUP, CPWUP, RST, TS, WS, AS | Manual update flags, timer reset, status bits |
| SMT1CLK | CSEL<2:0> | Clock source select |
| SMT1SIG | SSEL<4:0> | Signal input select |
| SMT1WIN | WSEL<4:0> | Window input select |
| SMT1TMRU/H/L | SMT1TMR<23:0> | 24-bit timer (R/W, non-atomic — only when GO=0) |
| SMT1CPRU/H/L | SMT1CPR<23:0> | 24-bit captured period (read-only, latched) |
| SMT1CPWU/H/L | SMT1CPW<23:0> | 24-bit captured pulse width (read-only, latched) |
| SMT1PRU/H/L | SMT1PR<23:0> | 24-bit period match register (R/W, defaults 0xFFFFFF) |

## Clock Sources (CSEL<2:0>)

| Value | Source |
|---|---|
| 000 | FOSC/4 |
| 001 | FOSC |
| 010 | HFINTOSC 16 MHz |
| 011 | LFINTOSC |
| 100 | MFINTOSC (500 kHz) |
| 101 | MFINTOSC/16 (32 kHz) |
| 110 | SOSC |
| 111 | Reference Clock Output |

## Signal Input (SSEL<4:0>)

| Value | Source |
|---|---|
| 00000 | Pin (SMTxSIGPPS) |
| 00001 | TMR0_overflow |
| 00010 | TMR1_postscaled |
| 00011 | TMR2_postscaled |
| 00100 | TMR3_postscaled |
| 00101 | TMR4_postscaled |
| 00110 | TMR5_postscaled |
| 00111 | TMR6_postscaled |
| 01000 | CCP1_out |
| 01001–01011 | CCP2–4_out |
| 01100–01101 | PWM5–6_out |
| 01110–01111 | PWM7–8_out |
| 10001 | CLC1_out |
| 10010 | CLC2_out |
| 10011 | CMP1_out |
| 10100 | CMP2_out |
| 10101 | ZCD1_out |
| 10110 | NCO1_out |

## Window Input (WSEL<4:0>)

| Value | Source |
|---|---|
| 00000 | Pin (SMTxWINPPS) |
| 00001 | LFINTOSC |
| 00010 | MFINTOSC/16 (32 kHz) |
| 00100 | CLKREF |
| 00110 | TMR2_postscaled |
| 00111 | TMR4_postscaled |
| 01000 | TMR6_postscaled |
| 01001 | CCP1_out |
| 01010–01011 | CCP2–3_out |
| 01100 | CCP4_out |
| 01101–01111 | PWM5–8_out |
| 10000–10010 | Reserved |
| 10011 | NCO1_out |
| 10100 | CMP1_out |
| 10101 | CMP2_out |
| 10110 | ZCD1_out |
| 10111 | CLC1_out |
| 11000 | CLC2_out |
| 11001 | CLC3_out |
| 11010 | CLC4_out |

## Polarity & Prescale

- **WPOL**: 0=SMTWIN active-high/rising, 1=active-low/falling
- **SPOL**: 0=SMTSIG active-high/rising, 1=active-low/falling
- **CPOL**: 0=rising clock edge, 1=falling clock edge
- **PS<1:0>**: 00=1:1, 01=1:2, 10=1:4, 11=1:8

## Status Bits

- **TS**: 1=timer incrementing (GO active, synchronized)
- **WS**: 1=window open (only valid when TS=1 in certain modes)
- **AS**: 1=acquisition in progress (only valid when TS=1)

## Manual Updates

- **CPRUP**: Write 1 to copy SMT1TMR→SMT1CPR buffers
- **CPWUP**: Write 1 to copy SMT1TMR→SMT1CPW buffers
- **RST**: Write 1 to reset SMT1TMR to 0

## Interrupts

Three interrupt conditions:
1. **SMT1PWAIF** — PW acquisition complete (CPW latch updated)
2. **SMT1PRAIF** — PR acquisition complete (CPR latch updated)
3. **SMT1IF** — Period match (SMT1TMR = SMT1PR)

## K42 vs Q41 Differences
- K42 has only SMT1; Q41 also has only SMT1.
- SSEL/WSEL mux tables differ: K42 includes CCP3/4, PWM7/8, CLC3/4 entries that Q41 may lack.
- Register layout and mode encodings are identical.