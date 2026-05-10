# PIC18F27/47/57Q43 — CCP and PWM Modules

## CCP — Capture/Compare/PWM (3 instances: CCP1–3)

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
| CCPxCAP | CTS<3:0> | Capture trigger input select |
| CCPRxH:L | RH<7:0>/RL<7:0> | 16-bit capture compare / 10-bit PWM duty cycle |

### Capture Input Select (CTS<3:0>)

| Value | Source |
|---|---|
| 000 | Pin via CCPxPPS |
| 001 | CMP1_output |
| 010 | CMP2_output |
| 011 | IOC_interrupt |
| 100 | CLC1_out |
| 101 | CLC2_out |
| 110 | CLC3_out |
| 111 | CLC4_out–CLC8_out (100=CLC1, 101=CLC2, ... 1011=CLC8) |

Actual CTS encoding for Q43 (4-bit field):
| Value | Source |
|---|---|
| 0000 | Pin via CCPxPPS |
| 0001 | CMP1_output |
| 0010 | CMP2_output |
| 0011 | IOC_interrupt |
| 0100 | CLC1_out |
| 0101 | CLC2_out |
| 0110 | CLC3_out |
| 0111 | CLC4_out |
| 1000 | CLC5_out |
| 1001 | CLC6_out |
| 1010 | CLC7_out |
| 1011 | CLC8_out |

### CCPxCON Register

| Bit | 7 | 6 | 5 | 4 | 3–0 |
|-----|---|---|---|---|------|
| Field | EN | — | OUT | FMT | MODE<3:0> |

- **FMT**: PWM alignment only. 1=left-aligned, 0=right-aligned.
- **OUT**: Read-only current output state.

### CCPRxH:CCPRxL in PWM Mode

- FMT=0 (right-aligned): CCPRxL<7:0>=CCPW<7:0>, CCPRxH<1:0>=CCPW<9:8>
- FMT=1 (left-aligned): CCPRxH<7:0>=CCPW<9:2>, CCPRxL<7:6>=CCPW<1:0>

### Q43 vs K42 Differences
- Q43 has **3 CCP modules** (CCP1–3) vs K42's 4 (CCP1–4).
- Q43 CCPxCAP uses 4-bit CTS<3:0> (12 sources including CLC1–8) vs K42's 3-bit (8 sources, CLC1–4).
- No CCPTMRS0 on Q43; timer selection is per-module via CCPxCLK register (see PWM timer resources below).

---

## PWM — Pulse-Width Modulator with Compare (3 instances: PWM1–3)

Q43 uses a **unique slice architecture** that differs significantly from K42's simple PWM5–8 modules.

### Slice Architecture

Each PWM module can have up to **4 output slices**. Each slice has two outputs (P1 and P2) sharing the same operating mode but with independent duty cycles. Slices are configured via PWMSLCx registers.

### Operating Modes (MODE<2:0> in PWMSLCx)

| MODE | Function |
|------|----------|
| 000 | Left Aligned |
| 001 | Right Aligned |
| 010 | Center-Aligned |
| 011 | Variable Aligned |
| 100 | Compare: Pulsed |
| 101 | Compare: Toggled |

Left and Right Aligned modes additionally support Push-Pull via PPEN bit.

### Key Registers

| Register | Key Bits | Purpose |
|---|---|---|
| PWMxCON | EN(PWMS) | Enable (mirror copies in PWMEN register for sync start) |
| PWMxCLK | CLK<4:0> | Clock source select |
| PWMxERS | ERS<4:0> | External reset source select |
| PWMxLDS | LDS<4:0> | Auto-load trigger source |
| PWMxPR | PR<15:0> | Period register (double-buffered) |
| PWMxCPRE | CPRE<7:0> | Clock prescale (n+1) |
| PWMxPIPOS | PIPOS<7:0> | Period interrupt postscaler (n+1) |
| PWMSLCx | MODE<2:0>, PPEN, POL2, POL1 | Slice mode, push-pull enable, polarities |
| PWMxSxDCL/PCH | P1/P2 duty cycle | Parameter (double-buffered, 16-bit) |
| PWMxGIR | S1P2, S1P1 | Parameter interrupt flags per slice |
| PWMxGIE | S1P2E, S1P1E | Parameter interrupt enables per slice |

### Clock Sources (CLK<4:0>)

| Value | Source | Sleep? |
|---|---|---|
| 00000 | PWMIN0PPS (pin) | Yes |
| 00001 | PWMIN1PPS (pin) | Yes |
| 00010 | FOSC | No |
| 00011 | HFINTOSC | Yes |
| 00100 | LFINTOSC | Yes |
| 00101 | MFINTOSC (500 kHz) | Yes |
| 00110 | MFINTOSC (31.25 kHz) | Yes |
| 00111 | SOSC | Yes |
| 01000 | EXTOSC | Yes |
| 01001 | CLKREF | Yes |
| 01010 | NCO1_out | Yes |
| 01011 | NCO2_out | Yes |
| 01100 | NCO3_out | Yes |
| 01101– | Reserved | — |
| 01101 | CLC1_out | Yes |
| 01110 | CLC2_out | Yes |
| 01111 | CLC3_out | Yes |
| 10000 | CLC4_out | Yes |
| 10001 | CLC5_out | Yes |
| 10010 | CLC6_out | Yes |
| 10011 | CLC7_out | Yes |
| 10100 | CLC8_out | Yes |
| 10101–11111 | Reserved | — |

### External Reset Sources (ERS<4:0>)

| Value | PWM1 | PWM2 | PWM3 |
|---|---|---|---|
| 00000 | Disabled | Disabled | Disabled |
| 00001 | PWM1ERSPPS | PWM2ERSPPS | PWM3ERSPPS |
| 00010 | PWM1S1P1_out | PWM1S1P1_out | Reserved |
| 00011 | Reserved | PWM1S1P2_out | PWM1S1P2_out |
| 00100 | PWM2S1P1_out | Reserved | PWM2S1P1_out |
| 00101 | PWM2S1P2_out | Reserved | PWM2S1P2_out |
| 00110 | PWM3S1P1_out | PWM3S1P1_out | Reserved |
| 00111 | PWM3S1P2_out | PWM3S1P2_out | Reserved |
| 01010 | CLC1_out | CLC1_out | CLC1_out |
| 01011– | CLC2–8_out | CLC2–8_out | CLC2–8_out |

### Auto-Load Trigger Sources (LDS<4:0>)

| Value | Source |
|---|---|
| 00000 | Auto-load Disabled |
| 00001 | PWMIN0PPS |
| 00010 | PWMIN1PPS |
| 00011 | CLC1_out |
| 00100–01110 | CLC2–8_out |
| 01111–10000 | DMA1–6 Destination Count Done |
| 10001–10010 | Reserved |
| 10011–11111 | Auto-load Disabled (except reserved) |

### Period and Duty Cycle

- **Period**: `PWM_Period = (PWMxPR + 1) × T_PWMxCLK × (CPRE + 1)`
- **Duty Cycle**: Set by PWMSLCx mode and PWMxSxDCL/PCH parameter values
- **Left Aligned**: Output active for parameter value clock periods, starting at timer=0
- **Right Aligned**: Output active for parameter value clock periods before end of period
- **Center-Aligned**: Period = 2 × (PR+1); output centered around period midpoint
- **Variable Aligned**: P1=start time, P2=end time (both outputs identical)
- **Compare Pulsed**: 1 clock period pulse at parameter match
- **Compare Toggled**: Toggle output at parameter match

### Push-Pull Mode (PPEN=1)

Available only in Left and Right Aligned modes. Alternates P1 and P2 outputs every other period. Sequencer resets on EN=0 or auto-shutdown.

### Output Polarity

POL1/POL2 bits in PWMSLCx invert the respective output. Toggling polarity while enabled changes output state regardless of PWM operation.

### Interrupts

- **PWMxPIF**: Period interrupt, set on PR match (post-scalable via PIPOS)
- **PWMxGIR S1P1/S1P2**: Parameter match flags (meaning depends on mode)

### Buffering

PWMxPR, PWMxSxDCL/PCH are double-buffered. Buffers load when LD bit is set or external load event occurs. PWMEN register allows synchronized enabling of multiple PWMs.

### Q43 vs K42 Differences
- Q43 PWM is an **entirely different architecture** from K42's simple PWM5–8.
- K42 has fixed-frequency simple PWM with PWMxDCH/DCL (10-bit). Q43 has 16-bit period (PWMxPR), 16-bit duty cycle parameters, slice architecture (PWMSLCx), multiple modes (left/right/center/variable/compare), and up to 4 slices per module.
- Q43 PWM has external reset sources (ERS), auto-load triggers (LDS), and push-pull support — none of which exist on K42.
- Q43 has **3 PWM modules** each with slice support, vs K42's 4 simple PWM generators.