# PIC18F26K42 Analog Peripherals

## ADC2 — Analog-to-Digital Converter with Computation

12-bit successive approximation ADC with computation engine.

### Key Registers

| Register | Key Bits | Description |
|----------|----------|-------------|
| ADCON0 | ON,CONT,CS,FM,GO | Enable, continuous, clock, format, start |
| ADCON1 | PPOL,IPEN,GPOL,DSEN | CVD polarity, double-sample |
| ADCON2 | PSIS,CRS[2:0],ACLR,MD[2:0] | Prev-sample select, shift, accum clear, mode |
| ADCON3 | CALC[2:0],SOI,TMD[2:0] | Error calc, stop-on-int, threshold mode |
| ADSTAT | ADAOV,UTHR,LTHR,MATH,STAT[2:0] | Status flags |
| ADCLK | CS[5:0] | Clock divisor (0=FOSC/2 … 63=FOSC/128) |
| ADREF | NREF,PREF[1:0] | Voltage reference select |
| ADPCH | PCH[5:0] | Channel select |
| ADPREL/H | PRE[12:0] | Precharge time (0=disabled) |
| ADACQL/H | ACQ[12:0] | Acquisition time (0=disabled unless ADPRE!=0, then max) |
| ADCAP | CAP[4:0] | Extra sample capacitance 0–31 pF |
| ADRPT | RPT[7:0] | Repeat threshold count |
| ADACT | ACT[4:0] | Auto-conversion trigger source |
| ADCP | CPON,CPRDY | Charge pump control |

### ADCON0 Bit Encoding

| Bit | Name | Value | Meaning |
|-----|------|-------|---------|
| 7 | ON | 1/0 | Enable/disable |
| 6 | CONT | 1/0 | Continuous retrigger/single |
| 4 | CS | 1/0 | ADCRC / FOSC (div per ADCLK) |
| 2 | FM | 1/0 | Right-justified / left-justified |
| 0 | GO | 1→0 | Start conversion; HW clears on done |

### Computation Modes (MD[2:0])

| MD | Mode | Behavior |
|----|------|----------|
| 000 | Basic | No accumulation; threshold error each sample |
| 001 | Accumulate | Add each result to ACC |
| 010 | Average | Accumulate until CNT>=RPT, then threshold test |
| 011 | Burst Average | Clear ACC, auto-retrigger until CNT>=RPT |
| 100 | Low-pass Filter | IIR filter; CRS sets cutoff |

### Error Calculation (CALC[2:0])

| CALC | Single (DSEN=0) | CVD Double (DSEN=1) |
|------|------------------|----------------------|
| 000 | RES-PREV | RES-PREV |
| 001 | RES-STPT | (RES-PREV)-STPT |
| 010 | RES-FLTR | (RES-PREV)-FLTR |
| 101 | FLTR-STPT | FLTR-STPT |

### Threshold Interrupt Mode (TMD[2:0])

| TMD | ADTIF triggers when |
|-----|---------------------|
| 000 | Never |
| 001 | ERR < LTH |
| 010 | ERR >= LTH |
| 011 | LTH < ERR < UTH |
| 100 | ERR < LTH or ERR > UTH |
| 101 | ERR <= UTH |
| 110 | ERR > UTH |
| 111 | Always |

### Voltage Reference (ADREF)

| PREF[1:0] | Pos Ref | NREF | Neg Ref |
|-----------|---------|------|---------|
| 00 | VDD | 0 | VSS |
| 10 | VREF+ pin | 1 | VREF- pin |
| 11 | FVR buffer 1 | | |

### Channel Select (ADPCH, key channels)

| PCH[5:0] | Channel | PCH[5:0] | Channel |
|----------|---------|----------|---------|
| 000000 | ANA0 | 111011 | VSS |
| 00xxxx | PORTA | 111100 | Temp indicator |
| 01xxxx | PORTB | 111101 | DAC1 output |
| 10xxxx | PORTC | 111110 | FVR buffer 1 |
| 11xxxx | PORTD/E/F | 111111 | FVR buffer 2 |

### Data Registers

ADRESH:ADRESL = 12-bit result; ADFLTRH:L = 16-bit filter (signed); ADACCU:ADACCH:ADACCL = 24-bit accumulator (18-bit + sign extension); ADERRH:L, ADSTPTH:L, ADUTHH:L, ADLTHH:L = 16-bit signed.

---

## DAC — 5-Bit Digital-to-Analog Converter

`DACx_output = (VREF+ - VREF-) * DATA[4:0]/32 + VREF-`

### Registers

| Register | Bits | Description |
|----------|------|-------------|
| DAC1CON0 | EN,OE1,OE2,PSS[1:0],NSS | Enable, output enables, source selects |
| DAC1CON1 | DATA[4:0] | Output level 0–31 |

### DAC1CON0 Encoding

| PSS[1:0] | Pos Source | NSS | Neg Source |
|-----------|-----------|-----|-----------|
| 00 | VDD | 0 | VSS |
| 01 | VREF+ pin | 1 | VREF- pin |
| 10 | FVR buffer 2 | | |

OE1=1: output on DAC1OUT1; OE2=1: output on DAC1OUT2. Outputs are unbuffered.

---

## Comparator Module (C1, C2)

### Registers

| Register | Key Bits | Description |
|----------|----------|-------------|
| CMxCON0 | EN,OUT,POL,HYS,SYNC | Enable, output, polarity, hysteresis, Timer1 sync |
| CMxCON1 | INTP,INTN | Rising/falling edge interrupt enables |
| CMxNCH | NCH[2:0] | Inverting input |
| CMxPCH | PCH[2:0] | Noninverting input |
| CMOUT | C2OUT,C1OUT | Output mirror |

### CMxNCH — Inverting Input

| NCH[2:0] | Source | PCH[2:0] | Source |
|-----------|--------|-----------|--------|
| 000 | CxIN0- | 000 | CxIN0+ |
| 001 | CxIN1- | 001 | CxIN1+ |
| 010 | CxIN2- | 101 | DAC output |
| 011 | CxIN3- | 110 | FVR_Buffer2 |
| 110 | FVR_Buffer2 | 111 | VSS |
| 111 | VSS | | |

POL=1 inverts output. HYS=1 enables hysteresis. SYNC=1 latches output on Timer1 clock. Output routable via PPS.

---

## FVR — Fixed Voltage Reference

1.024V bandgap with two independent buffers.

### FVRCON Register

| Bit | Name | Encoding |
|-----|------|----------|
| 7 | EN | 1=FVR enabled |
| 6 | RDY | 1=output ready |
| 5 | TSEN | 1=Temp indicator enabled |
| 4 | TSRNG | 1=High range (3VT), 0=Low range (2VT) |
| 3:2 | CDAFVR[1:0] | Buffer 2 gain (CMP/DAC) |
| 1:0 | ADFVR[1:0] | Buffer 1 gain (ADC) |

### Gain Encoding (both buffers)

| Value | Gain | Voltage |
|-------|------|---------|
| 00 | Off | — |
| 01 | 1x | 1.024V |
| 10 | 2x | 2.048V |
| 11 | 4x | 4.096V |

Output must not exceed VDD. Buffer 1 → ADC positive ref (PREF=11) and ADC channel. Buffer 2 → DAC positive source, comparator input.

---

## Temperature Indicator

On-die sensor; VMEAS read via ADC channel PCH=111100.

- Enable: TSEN bit in FVRCON; Range: TSRNG bit in FVRCON
- High range (TSRNG=1): VOUT=3VT, min VDD=2.5V
- Low range (TSRNG=0): VOUT=2VT, min VDD=1.8V
- VMEAS decreases with increasing temperature

`TMEAS = 90 + (ADC_MEAS - ADC_DIA) * FVRA2X / ((2^N - 1) * Mv)`

DIA params: TSLR2 (low range), TSHR2 (high range). Average 10 readings recommended.

---

## HLVD — High/Low-Voltage Detect

### Registers

| Register | Bits | Description |
|----------|------|-------------|
| HLVDCON0 | EN,OUT,RDY,INTH,INTL | Enable, output, ready, direction |
| HLVDCON1 | SEL[3:0] | Trip point voltage select (16 taps) |

### HLVDCON0 Encoding

| Bit | Name | Meaning |
|-----|------|---------|
| 7 | EN | 1=enabled |
| 5 | OUT | 1=VDD<=trip, 0=VDD>=trip |
| 4 | RDY | 1=band gap stable |
| 1 | INTH | 1=interrupt on VDD>=trip (rising) |
| 0 | INTL | 1=interrupt on VDD<=trip (falling) |

Disable (EN=0) before changing INTH/INTL/SEL to avoid false events. SEL voltages per Table 44-13. Active in Sleep.