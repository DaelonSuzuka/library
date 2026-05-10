# PIC18F27/47/57Q43 — Digital Peripherals (CLC, NCO, CWG, DSM, ZCD)

## CLC — Configurable Logic Cell (8 instances: CLC1–CLC8, shared registers)

### Operating Modes (MODE<2:0> in CLCnCON)

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
| CLCSELECT | SLCT<2:0> | Instance select (0=CLC1, 1=CLC2, …, 7=CLC8) |
| CLCnCON | EN, OUT, INTP, INTN, MODE<2:0> | Enable, output read, interrupt edges, mode |
| CLCnPOL | POL, G4POL–G1POL | Output & gate polarity inversion |
| CLCnSEL0–3 | D1S<7:0>–D4S<7:0> | Input mux select for each of 4 data inputs |
| CLCnGLS0–3 | GxDxT/GxDxN per gate | Gate logic select (true/negated per input per gate) |
| CLCDATA | CLC8OUT–CLC1OUT | Simultaneous output read of all CLCs |

### Input Mux Selection (DxS<7:0>)

Key selections: 0–7=CLCIN0–CLCIN7PPS, 8=FOSC, 9=HFINTOSC, 10=LFINTOSC, 11=MFINTOSC(500kHz), 12=MFINTOSC(31.25kHz), 13=SFINTOSC(1MHz), 14=SOSC, 15=EXTOSC, 16=ADCRC, 17=CLKR, 18=TMR0, 19=TMR1, 20=TMR2, 21=TMR3, 22=TMR4, 23=TMR5, 24=TMR6, 31=CCP1, 32=CCP2, 33=CCP3, 34-39=PWM1S1P1/P2–PWM3S1P1/P2, 42=NCO1, 43=NCO2, 44=NCO3, 45=CMP1_OUT, 46=CMP2_OUT, 47=ZCD, 48=IOC, 49=DSM1, 50=HLVD_OUT, 51=CLC1, 52=CLC2, 53=CLC3, 54=CLC4, 55=CLC5, 56=CLC6, 57=CLC7, 58=CLC8, 59=U1TX, 60=U2TX, 61=U3TX, 62=U4TX, 63=U5TX, 64=SPI1_SDO, 65=SPI1_SCK, 66=SPI1_SS, 67=SPI2_SDO, 68=SPI2_SCK, 69=SPI2_SS, 70=I2C_SCL, 71=I2C_SDA, 72=CWG1A, 73=CWG1B, 74=CWG2A, 75=CWG2B, 76=CWG3A, 77=CWG3B

### Gate Logic (CLCnGLSy)

Each gate ANDs its enabled inputs; polarity bit inverts the gate output. Key patterns:
- 0x55 + GyPOL=1 → AND; 0x55 + GyPOL=0 → NAND
- 0xAA + GyPOL=1 → NOR; 0xAA + GyPOL=0 → OR
- 0x00 + GyPOL=1 → Logic 1; 0x00 + GyPOL=0 → Logic 0

### Q43 vs K42 Differences
- Q43 has **8 CLC modules** (CLC1–8) vs K42's 4. Uses CLCSELECT register (addr 0x0D5) to select active instance; all registers shared.
- Q43 CLC input mux is 8-bit (DxS<7:0>) supporting up to 128+ sources vs K42's 6-bit (DxS<5:0>) with 52 entries.
- Q43 adds: CLCIN4–7PPS, CCP3, PWM slice outputs (PWM1S1P1/P2, PWM2S1P1/P2, PWM3S1P1/P2), NCO2/3, CMP2, CLC5–8, U3–5TX, SPI2, I2C, SFINTOSC(1MHz), EXTOSC, CWG3A/B.

---

## NCO — Numerically Controlled Oscillator (3 instances: NCO1–3)

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
| NCOxCON | EN, OUT, POL, PFM | Enable, current output read, polarity, mode |
| NCOxCLK | PWS<2:0>, CKS<4:0> | Pulse width select, clock source |
| NCOxACCL/H/U | ACC<19:0> | 20-bit accumulator (live, not atomic — undefined if written while running) |
| NCOxINCL/H/U | INC<19:0> | 20-bit increment value (double-buffered; buffer loads on next falling NCOCLK edge after NCOxINCL write) |

### Clock Sources (CKS<4:0>)

| Value | Source |
|---|---|
| 00000 | FOSC |
| 00001 | HFINTOSC |
| 00010 | LFINTOSC |
| 00011 | MFINTOSC (500 kHz) |
| 00100 | MFINTOSC/32 (31.25 kHz) |
| 00101 | SOSC |
| 00110 | CLKREF |
| 00111–10001 | CLC1–CLC8_out |
| 10010–11111 | Reserved |

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

### Q43 vs K42 Differences
- Q43 has **3 NCO modules** (NCO1–3) vs K42's 1.
- Q43 NCO1CLK uses 5-bit CKS<4:0> with CLC1–8 and MFINTOSC/32 (31.25kHz) replacing K42's MFINTOSC/4 (32kHz).
- Q43 clock source encoding differs: CLKREF at 00110 vs K42's 0110; CLC range shifted to 00111–10001.

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
| CWGxAS1 | ASyE bits | Auto-shutdown source enables |
| CWGxDBR | DBR<5:0> | Rising/reverse dead-band count (0–63 CWG clocks) |
| CWGxDBF | DBF<5:0> | Falling/forward dead-band count |

### Input Source Select (ISM<4:0>)

| Value | CWG1/2/3 Input |
|---|---|
| 00000 | Pin via CWGxPPS |
| 00001 | CCP1_out |
| 00010 | CCP2_out |
| 00011 | CCP3_out |
| 00100 | PWM1S1P1_out |
| 00101 | PWM1S1P2_out |
| 00110 | PWM2S1P1_out |
| 00111 | PWM2S1P2_out |
| 01000 | PWM3S1P1_out |
| 01001 | PWM3S1P2_out |
| 01010 | Reserved |
| 01011 | Reserved |
| 01100 | CMP1OUT |
| 01101 | CMP2OUT |
| 01110 | NCO1OUT |
| 01111 | NCO2OUT |
| 10000 | CLC2_out |
| 10001 | CLC3_out |
| 10010 | CLC4_out |
| 10011 | CLC5_out |
| 10100 | CLC6_out |
| 10101 | CLC7_out |
| 10110 | CLC8_out |

### Auto-Shutdown Override Levels (LSBD/LSAC)

| Value | Output State During Shutdown |
|---|---|
| 00 | Inactive (after dead-band) |
| 01 | Tri-state (High-Z) |
| 10 | Logic 0 |
| 11 | Logic 1 |

### Q43 vs K42 Differences
- Q43 has **3 CWG instances** (same as K42).
- Q43 CWG ISM mux replaces PWM5–8 with PWM1S1P1/P2–PWM3S1P1/P2 (slice outputs) and adds NCO2OUT, CLC5–8.
- Q43 CWG AS1 shutdown sources include PWM slice outputs and NCO2.

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
| 00100 | CCP1_out |
| 00101 | CCP2_out |
| 00110 | CCP3_out |
| 00111–01010 | PWM1S1P1/P2_out–PWM2S1P1/P2_out |
| 01011 | Reserved |
| 01100 | NCO1_out |
| 01101 | NCO2_out |
| 01110 | NCO3_out |
| 01111 | CLC1_out |
| 10000 | CLC2_out |
| 10001 | CLC3_out |
| 10010 | CLC4_out |
| 10011 | CLC5_out |
| 10100 | CLC6_out |
| 10101 | CLC7_out |
| 10110 | CLC8_out |

Modulator (MS<4:0>):

| Value | Source |
|---|---|
| 00000 | Pin (MDSRCPPS) |
| 00001 | DSM1 BIT (register) |
| 00010 | CCP1_out |
| 00011 | CCP2_out |
| 00100 | CCP3_out |
| 00101–01010 | Reserved |
| 01011 | NCO1_out |
| 01100 | NCO2_out |
| 01101 | NCO3_out |
| 01110 | CMP1_out |
| 01111 | CMP2_out |
| 10000 | CLC1_out |
| 10001 | CLC2_out |
| 10010 | CLC3_out |
| 10011 | CLC4_out |
| 10100 | CLC5_out |
| 10101 | CLC6_out |
| 10110 | CLC7_out |
| 10111 | CLC8_out |
| 11000 | DSM1_out |
| 11001 | SPI1 SDO |
| 11010 | UART1 TX |
| 11011 | UART2 TX |

### Q43 vs K42 Differences
- Q43 DSM source tables include CCP3, PWM slice outputs (PWM1S1P1/P2 etc.), NCO2/3, CLC5–8.
- K42 has UART1/2 TX and SPI1 SDO; Q43 adds SPI1 SDO and reorganizes the mux values.

---

## ZCD — Zero-Cross Detector (1 instance: ZCD1)

### Key Registers

| Register | Bits | Purpose |
|---|---|---|
| ZCDCON | SEN, OUT, POL, INTP, INTN | Enable, output status, polarity, interrupt edges |

- **SEN**: 1=ZCD enabled; 0=disabled (pin per PPS/TRIS). Ignored when ZCD config bit is cleared.
- **OUT**: POL=0: 1=sinking current, 0=sourcing current; POL=1: inverted.
- **POL**: 1=inverts ZCD logic output relative to current source/sink.
- **INTP**: 1=set ZCDIF on rising edge of ZCD output.
- **INTN**: 1=set ZCDIF on falling edge of ZCD output.

Changing POL can cause spurious interrupts. ZCD operates during Sleep.

### External Resistor Selection

- Series resistor: `R_SERIES = V_PEAK / (3 × 10^-4) - 4`
- Current limits: 100 µA min to 600 µA max.

### Q43 vs K42 Differences
- ZCD module is largely identical between K42 and Q43.
- Q43 ZCDCON register at address 0x04C vs K42's 0x3EC3.