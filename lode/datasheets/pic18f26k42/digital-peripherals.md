# PIC18F26K42 — Digital Peripherals (CLC, NCO, CWG, DSM, ZCD)

## CLC — Configurable Logic Cell (4 instances: CLC1–CLC4)

### Operating Modes (MODE<2:0> in CLCxCON)

| MODE | Function |
|------|----------|
| 000 | AND-OR |
| 001 | OR-XOR |
| 010 | 4-input AND |
| 011 | S-R Latch |
| 100 | 1-input D-FF with S and R |
| 101 | 2-input D-FF with R |
| 110 | J-K FF with R |
| 111 | 1-input transparent latch with S and R |

### Key Registers

| Register | Bits | Purpose |
|---|---|---|
| CLCxCON | EN, OUT, INTP, INTN, MODE<2:0> | Enable, output read, interrupt edges, mode |
| CLCxPOL | POL, G4POL–G1POL | Output & gate polarity inversion |
| CLCxSEL0–3 | D1S<5:0>–D4S<5:0> | Input mux select for each of 4 data inputs |
| CLCxGLS0–3 | GxDxT/GxDxN per gate | Gate logic select (true/negated per input per gate) |
| CLCDATA | CLC4OUT–CLC1OUT | Simultaneous output read of all CLCs |

### Input Mux Selection (DxS<5:0>)

Key selections: 0=CLCIN0PPS, 1=CLCIN1PPS, 2=CLCIN2PPS, 3=CLCIN3PPS, 4=FOSC, 5=HFINTOSC, 6=LFINTOSC, 7=MFINTOSC(500kHz), 8=MFINTOSC/4(32kHz), 9=SOSC, 10=CLKR, 11=ADCRC, 12–15=TMR0–3, 16=TMR4_out, 17=TMR5_overflow, 18=TMR6_out, 19=SMT1_out, 20–23=CCP1–4_out, 24–27=PWM5–8_out, 28–29=reserved, 30=NCO1_out, 31=CMP1_out, 32=CMP2_out, 33=ZCD_out, 34=IOC_flag, 35=DSM1_out, 36–39=CLC1–4_out, 40=UART1_tx, 41=UART2_tx, 42=reserved, 43=SDO1, 44=SCK1, 45=SS1, 46=CWG1A, 47=CWG1B, 48=CWG2A, 49=CWG2B, 50=CWG3A, 51=CWG3B

### Gate Logic (CLCxGLSy)

Each gate ANDs its enabled inputs; polarity bit inverts the gate output. Key patterns:
- 0x55 + GyPOL=1 → AND; 0x55 + GyPOL=0 → NAND
- 0xAA + GyPOL=1 → NOR; 0xAA + GyPOL=0 → OR
- 0x00 + GyPOL=1 → Logic 1; 0x00 + GyPOL=0 → Logic 0

### K42 vs Q41 Differences
- K42 has **4 CLC modules** (CLC1–4); Q41 also has 4.
- K42 input mux includes UART1/2 TX outputs (values 40–41), CWG1–3 A/B outputs (46–51) which Q41 may not have (different CWG instance count).
- CLCxCON bit layout identical to Q41.

---

## NCO — Numerically Controlled Oscillator (1 instance: NCO1)

### Operating Modes

| PFM bit | Mode |
|---------|------|
| 0 | Fixed Duty Cycle (FDC) — toggles on overflow, 50% duty |
| 1 | Pulse Frequency (PF) — active output for PWS<2:0> clock periods |

### NCO Overflow Frequency

`F_OVERFLOW = (NCO_Clock_Freq × Increment_Value) / 2^20`

### Key Registers

| Register | Bits | Purpose |
|---|---|---|
| NCO1CON | EN, OUT, POL, PFM | Enable, current output read, polarity, mode |
| NCO1CLK | PWS<2:0>, CKS<3:0> | Pulse width select, clock source |
| NCO1ACCL/H/U | ACC<19:0> | 20-bit accumulator (live, not atomic — undefined if written while running) |
| NCO1INCL/H/U | INC<19:0> | 20-bit increment value (double-buffered; buffer loads on next falling NCOCLK edge after NCO1INCL write) |

### Clock Sources (CKS<3:0>)

| Value | Source |
|---|---|
| 0000 | FOSC |
| 0001 | HFINTOSC |
| 0010 | LFINTOSC |
| 0011 | MFINTOSC (500 kHz) |
| 0100 | MFINTOSC/4 (32 kHz) |
| 0101 | SOSC |
| 0110 | CLKREF |
| 0111–1010 | CLC1–4_out |
| 1011–1111 | Reserved |

### Pulse Width Select (PWS<2:0>) — PF mode only

| PWS | Active Periods |
|---|---|
| 000 | 1 |
| 001 | 2 |
| 010 | 4 |
| 011 | 8 |
| 100 | 16 |
| 101 | 32 |
| 110 | 64 |
| 111 | 128 |

If pulse width > overflow period → undefined operation.

### K42 vs Q41 Differences
- K42 NCO1CLK uses 4-bit CKS<3:0> (supporting CLC1–4); Q41 uses same layout.
- NCO1INCL default = 0x01 on POR; NCO1ACCU bits 7–4 unimplemented.

---

## CWG — Complementary Waveform Generator (3 instances: CWG1–3)

### Operating Modes (MODE<2:0> in CWGxCON0)

| MODE | Function |
|------|----------|
| 000 | Asynchronous Steering |
| 001 | Synchronous Steering |
| 010 | Forward Full Bridge |
| 011 | Reverse Full Bridge |
| 100 | Half Bridge |
| 101 | Push Pull |
| 110–111 | Reserved |

Mode changes only allowed when EN=0, except Forward↔Reverse toggle via MODE<0>.

### Key Registers

| Register | Key Bits | Purpose |
|---|---|---|
| CWGxCON0 | EN, LD, MODE<2:0> | Enable, load buffers, mode select |
| CWGxCON1 | IN, POLD, POLC, POLB, POLA | Input read, output polarity (4 outputs) |
| CWGxCLK | CS | Clock: 0=FOSC, 1=HFINTOSC |
| CWGxISM | ISM<4:0> | Input source select |
| CWGxSTR | OVRD–OVRA, STRD–STRA | Steering override data & enable (steering modes only) |
| CWGxAS0 | SHUTDOWN, REN, LSBD<1:0>, LSAC<1:0> | Auto-shutdown control & override levels |
| CWGxAS1 | AS6E–AS0E | Auto-shutdown source enables |
| CWGxDBR | DBR<5:0> | Rising/reverse dead-band count (0–63 CWG clocks) |
| CWGxDBF | DBF<5:0> | Falling/forward dead-band count |

### Input Source Select (ISM<4:0>)

| Value | CWG1/2/3 Input |
|---|---|
| 00000 | Pin via CWGxPPS |
| 00001 | CCP1_out |
| 00010 | CCP2_out |
| 00011 | CCP3_out |
| 00100 | CCP4_out |
| 00101 | PWM5_out |
| 00110 | PWM6_out |
| 00111 | PWM7_out |
| 01000 | PWM8_out |
| 01100 | CMP1OUT |
| 01101 | CMP2OUT |
| 01110 | NCO1OUT |
| 01111 | DSM_out |
| 10000 | CLC2_out |
| 10001 | CLC3_out |
| 10010 | CLC4_out |

### Auto-Shutdown Override Levels (LSBD/LSAC)

| Value | Output State During Shutdown |
|---|---|
| 00 | Inactive (after dead-band) |
| 01 | Tri-state (High-Z) |
| 10 | Logic 0 |
| 11 | Logic 1 |

Shutdown sources (all active-low): Pin (CWGxPPS), TMR2/4/6 postscaled, CMP1/2, CLC2/3/4.

### K42 vs Q41 Differences
- K42 has **3 CWG instances** where Q41 may have fewer; input mux table matches for common entries.
- K42 AS1 bit 6 maps to CLC2_out for CWG1, CLC3_out for CWG2, CLC4_out for CWG3.

---

## DSM — Data Signal Modulator (1 instance: DSM1)

### Key Registers

| Register | Key Bits | Purpose |
|---|---|---|
| MD1CON0 | EN, OUT, OPOL, BIT | Enable, read output, output polarity, sw modulator bit |
| MD1CON1 | CHPOL, CHSYNC, CLPOL, CLSYNC | Carrier high/low polarity & synchronization |
| MD1CARH | CH<4:0> | Carrier high source select |
| MD1CARL | CL<4:0> | Carrier low source select |
| MD1SRC | MS<4:0> | Modulator source select |

### Carrier/Modulator Source Selection

Carrier High/Low (CH/CL<4:0>):

| Value | Source |
|---|---|
| 00000 | Pin (MD1CARHPPS / MD1CARLPPS) |
| 00001 | FOSC |
| 00010 | HFINTOSC |
| 00011 | CLKREF |
| 00100–00111 | CCP1–4_out |
| 01000–01011 | PWM5–8_out |
| 01110 | NCO1_out |
| 01111–10000 | CLC1–4_out |

Modulator (MS<4:0>):

| Value | Source |
|---|---|
| 00000 | Pin (MDSRCPPS) |
| 00001 | DSM1 BIT (register) |
| 00010 | CCP1_out |
| 00011–00101 | CCP2–4_out |
| 00110–00111 | PWM5–6_out |
| 01000–01001 | PWM7–8_out |
| 01100 | NCO1_out |
| 01101 | CMP1_out |
| 01110 | CMP2_out |
| 01111–10000 | CLC1–4_out |
| 10001 | DSM1_out |
| 10010 | SPI1 SDO |
| 10011 | UART1 TX |
| 10100 | UART2 TX |

### K42 vs Q41 Differences
- K42 DSM source tables include UART1/2 TX and SPI SDO that Q41 may share.
- DSM operates independently of Sleep; will run if carrier/modulator sources remain active.

---

## ZCD — Zero-Cross Detector (1 instance: ZCD1)

### Key Registers

| Register | Bits | Purpose |
|---|---|---|
| ZCDCON | SEN, OUT, POL, INTP, INTN | Enable, output status, polarity, interrupt edges |

- **SEN**: 1=ZCD enabled; 0=disabled (pin per PPS/TRIS). Ignored when ZCD config bit is set.
- **OUT**: POL=0: 1=sinking current, 0=sourcing current; POL=1: inverted.
- **POL**: 1=inverts ZCD logic output relative to current source/sink.
- **INTP**: 1=set ZCDIF on rising edge of ZCD output.
- **INTN**: 1=set ZCDIF on falling edge of ZCD output.

Changing POL can cause spurious interrupts. ZCD operates during Sleep.

### External Resistor Selection

- Series resistor: `R_SERIES = V_PEAK / (3 × 10^-4) - 4`
- Current limits: 100 µA min to 600 µA max.
- Pull-up/down resistor for VCPINV offset compensation.

### K42 vs Q41 Differences
- ZCD module is largely identical between K42 and Q41.
- K42 ZCD output can serve as gate source for TMR1/3/5 and clock/reset for TMR2/4/6.