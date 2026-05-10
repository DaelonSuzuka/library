# PIC18F26K42 — CCP and PWM Modules

## CCP — Capture/Compare/PWM (4 instances: CCP1–4)

### Operating Modes (MODE<3:0> in CCPxCON)

| MODE | Function | Sets CCPxIF? |
|------|----------|---|
| 0000 | Disabled | — |
| 0001 | Compare: Toggle output, clear TMR1 | Yes |
| 0010 | Compare: Toggle output | Yes |
| 0011 | Capture: Every edge (rising+falling) | Yes |
| 0100 | Capture: Every falling edge | Yes |
| 0101 | Capture: Every rising edge | Yes |
| 0110 | Capture: Every 4th rising edge | Yes |
| 0111 | Capture: Every 16th rising edge | Yes |
| 1000 | Compare: Set output | Yes |
| 1001 | Compare: Clear output | Yes |
| 1010 | Compare: Pulse output | Yes |
| 1011 | Compare: Pulse output, clear TMR1 | Yes |
| 11xx | PWM | Yes |

### Key Registers

| Register | Bits | Purpose |
|---|---|---|
| CCPxCON | EN, OUT, FMT, MODE<3:0> | Enable, output read, PWM alignment, mode |
| CCPxCAP | CTS<2:0> | Capture trigger input select |
| CCPRxH:L | RH<7:0>/RL<7:0> | 16-bit capture compare / 10-bit PWM duty cycle |
| CCPTMRS0 | C4TSEL–C1TSEL<1:0> | Timer resource assignment per CCP |

### Timer Selection (CxTSEL<1:0>)

| Value | Capture/Compare Timer | PWM Timer |
|---|---|---|
| 00 | Reserved | Reserved |
| 01 | Timer1 | Timer2 |
| 10 | Timer3 | Timer4 |
| 11 | Timer5 | Timer6 |

Default: TMR1 for Capture/Compare, TMR2 for PWM.

### Capture Input Select (CTS<2:0>)

| Value | Source (all CCP modules) |
|---|---|
| 000 | Pin via CCPxPPS |
| 001 | CMP1_output |
| 010 | CMP2_output |
| 011 | IOC_interrupt |
| 100 | CLC1_out |
| 101 | CLC2_out |
| 110 | CLC3_out |
| 111 | CLC4_out |

### CCPxCON Register

| Bit | 7 | 6 | 5 | 4 | 3–0 |
|-----|---|---|---|---|------|
| Field | EN | — | OUT | FMT | MODE<3:0> |

- **FMT**: PWM alignment only. 1=left-aligned, 0=right-aligned.
- **OUT**: Read-only current output state.

### CCPRxH:CCPRxL in PWM Mode

- FMT=0 (right-aligned): CCPRxL<7:0>=CCPW<7:0>, CCPRxH<1:0>=CCPW<9:8>
- FMT=1 (left-aligned): CCPRxH<7:0>=CCPW<9:2>, CCPRxL<7:6>=CCPW<1:0>

### K42 vs Q41 Differences
- K42 has 4 CCP modules (CCP1–4) vs Q41's 2.
- CCPTMRS0 layout with 4 timer-select pairs; Q41 has CCPTMRS0 with 2 pairs.
- CCPxCAP CTS field is 3 bits (8 sources including CLC4); Q41 may have fewer CLC options.

---

## PWM — Pulse-Width Modulation (4 instances: PWM5–8)

### Key Registers

| Register | Bits | Purpose |
|---|---|---|
| PWMxCON | EN, OUT, POL | Enable, output read, polarity |
| PWMxDCH | DC<9:2> | Duty cycle MSBs |
| PWMxDCL | DC<1:0> (bits 7:6) | Duty cycle LSBs; bits 5:0 unimplemented |
| CCPTMRS1 | P8TSEL–P5TSEL<1:0> | Timer assignment per PWM |

### Timer Selection (PxTSEL<1:0>)

| Value | Timer |
|---|---|
| 00 | Reserved |
| 01 | Timer2 |
| 10 | Timer4 |
| 11 | Timer6 |

### PWM Period and Duty Cycle

- **Period**: `PWM_Period = (T2PR + 1) × 4 × TOSC × TMR2_Prescale`
- **Pulse Width**: `PW = (PWMxDCH:PWMxDCL<7:6>) × TOSC × TMR2_Prescale`
- **Duty Cycle**: `DC_ratio = (PWMxDCH:PWMxDCL<7:6>) / (4 × (T2PR + 1))`
- **Resolution**: `Resolution = log2(4 × (T2PR + 1))` bits (max 10-bit at T2PR=255)
- PWMxDCH/PWMxDCL are double-buffered; latched on T2PR match.
- FOSC/4 must be Timer2 clock input for correct PWM operation.
- Postscaler not used for PWM frequency.

### PWMxCON Register

| Bit | 7 | 6 | 5 | 4 | 3–0 |
|-----|---|---|---|---|------|
| Field | EN | — | OUT | POL | — |

### K42 vs Q41 Differences
- K42 has PWM5–8 (4 modules); Q41 has PWM5–6 (2 modules).
- CCPTMRS1 register layout identical; K42 uses all 4 PxTSEL pairs, Q41 only P5/P6.
- Duty cycle register layout (PWMxDCH:PWMxDCL<7:6>) is the same.