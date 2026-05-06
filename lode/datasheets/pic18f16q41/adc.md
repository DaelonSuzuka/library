# PIC18F16Q41 — ADCC & FVR Reference

## ADCC Overview (DS Sec 40)

12-bit successive-approximation ADC with computation, CVD support, auto-trigger,
threshold comparison, and digital filter. Dual result registers (ADRES + ADPREV).

## ADCC Registers

| Addr   | Reg     | Width | Key Fields                                |
|--------|---------|-------|-------------------------------------------|
| 0x3F3  | ADCON0  | 8     | ON(7), CONT(6), CS(4), FM(2), GO(0)      |
| 0x3F4  | ADCON1  | 8     | PPOL(7), IPEN(6), GPOL(5), DSEN(0)       |
| 0x3F5  | ADCON2  | 8     | PSIS(7), CRS[2:0](6:4), ACLR(3), MD[2:0](2:0) |
| 0x3F6  | ADCON3  | 8     | CALC[2:0](6:4), SOI(3), TMD[2:0](2:0)   |
| 0x3F7  | ADSTAT  | 8     | AOV(7), UTHR(6), LTHR(5), MATH(4), STAT[2:0](2:0) |
| 0x3F8  | ADREF   | 8     | NREF(4), PREF[1:0](1:0)                  |
| 0x3F9  | ADACT   | 8     | ACT[4:0](4:0) — auto-conversion trigger  |
| 0x3FA  | ADCLK   | 8     | CS[5:0](5:0) — clock divider              |
| 0x3EC  | ADPCH   | 8     | PCH[7:0] — positive channel select       |
| 0x3EE  | ADACQ   | 13    | ACQ[12:0] — acquisition time              |
| 0x3F0  | ADCAP   | 8     | CAP[4:0] — extra S&H capacitance (1-31 pF)|
| 0x3F1  | ADPRE   | 13    | PRE[12:0] — precharge time                |
| 0x3D8  | ADCP    | 8     | CPON(7), CPRDY(0) — charge pump          |
| 0x3D9  | ADLTH   | 16    | LTH[15:0] — lower threshold (signed)      |
| 0x3DB  | ADUTH   | 16    | UTH[15:0] — upper threshold (signed)      |
| 0x3DD  | ADERR   | 16    | ERR[15:0] — setpoint error (signed, RO)   |
| 0x3DF  | ADSTPT  | 16    | STPT[15:0] — threshold setpoint (signed)  |
| 0x3E1  | ADFLTR  | 16    | FLTR[15:0] — filter output (signed, RO)   |
| 0x3E3  | ADACC   | 18    | ACC[17:0] — accumulator (signed)          |
| 0x3E6  | ADCNT   | 8     | CNT[7:0] — repeat counter                 |
| 0x3E7  | ADRPT   | 8     | RPT[7:0] — repeat threshold               |
| 0x3E8  | ADPREV  | 16    | PREV[15:0] — previous result (RO)         |
| 0x3EA  | ADRES   | 16    | RES[15:0] — conversion result             |

## ADCON0 Bit Fields

- **ON** (bit 7): ADC enable
- **CONT** (bit 6): continuous retrigger mode
- **CS** (bit 4): 0=FOSC (divided by ADCLK), 1=ADCRC
- **FM** (bit 2): 0=left-justified, 1=right-justified
- **GO** (bit 0): set to start conversion; cleared by HW on completion

## Voltage Reference (ADREF)

| PREF[1:0] | Positive Reference    |
|-----------|-----------------------|
| 00        | VDD                   |
| 01        | Reserved              |
| 10        | External VREF+ pin    |
| 11        | FVR Buffer 1          |

| NREF | Negative Reference    |
|------|-----------------------|
| 0    | VSS                   |
| 1    | External VREF- pin    |

## Channel Selection (ADPCH)

Key internal channels:
| PCH   | Channel               |
|-------|-----------------------|
| 0x00  | RA0/ANA0              |
| 0x01  | RA1/ANA1              |
| 0x02  | RA2/ANA2              |
| 0x03  | RA3/ANA3              |
| 0x3B  | VSS                   |
| 0x3C  | Temp Indicator        |
| 0x3D  | DAC1 output            |
| 0x3E  | FVR Buffer 1          |
| 0x3F  | FVR Buffer 2          |

External pins: ANA0-ANA5 (0x00-0x05), ANB4-ANB7 (0x0C-0x0F),
ANC0-ANC7 (0x10-0x17).

## Conversion Clock (ADCLK)

When CS=0 (FOSC): TAD = 2×(n+1)/FOSC, n=ADCLK value (0-63).
When CS=1: ADCRC (1-6 μs typical). Required for Sleep operation.

## Computation Modes (ADCON2 MD[2:0])

| MD  | Mode               | Behavior                                            |
|-----|--------------------|-----------------------------------------------------|
| 000 | Basic (Legacy)     | Single/double sample, no accumulation, threshold every sample |
| 001 | Accumulate         | Each sample added to ADACC; ADCNT++; ADFLTR=ADACC>>CRS |
| 010 | Average            | Accumulates ADRPT samples, then thresholds; clears on next trigger |
| 011 | Burst Average      | Auto-retriggers until ADCNT≥ADRPT, then thresholds |
| 100 | Low-Pass Filter    | IIR filter; cutoff governed by CRS; thresholds after ADRPT samples |

**CRS[2:0]** (bits 6:4 of ADCON2): right-shift of accumulator. In Average mode,
set ADRPT=2^CRS for correct averaging. In LPF mode, controls cutoff:
CRS 1→ωT=0.72, 2→0.284, 3→0.134, 4→0.065, 5→0.032, 6→0.016.

**ACLR** (bit 3): write 1 to clear ADACC+ADCNT+AOV; HW clears when done.
**PSIS** (bit 7): 0=ADRES→ADPREV, 1=ADFLTR→ADPREV.

## Error Calculation (ADCON3 CALC[2:0])

| CALC | DSEN=0 (single)      | DSEN=1 (CVD double)          |
|------|-----------------------|-------------------------------|
| 000  | ADRES-ADPREV          | ADRES-ADPREV (CVD result)    |
| 001  | ADRES-ADSTPT          | (ADRES-ADPREV)-ADSTPT         |
| 010  | ADRES-ADFLTR          | (ADRES-ADPREV)-ADFLTR         |
| 100  | ADPREV-ADFLTR         | ADPREV-ADFLTR (1st deriv filtered, PSIS=1) |
| 101  | ADFLTR-ADSTPT         | ADFLTR-ADSTPT                 |

## Threshold (TMD[2:0])

| TMD | Interrupt Condition            |
|-----|--------------------------------|
| 000 | Never                          |
| 001 | ADERR < ADLTH                   |
| 010 | ADERR ≥ ADLTH                  |
| 011 | ADLTH ≤ ADERR ≤ ADUTH          |
| 100 | ADERR < ADLTH or ADERR > ADUTH |
| 101 | ADERR ≤ ADUTH                  |
| 110 | ADERR > ADUTH                  |
| 111 | Always                         |

**SOI** (bit 3): when CONT=1, stop on threshold interrupt.

## Auto-Conversion Trigger (ADACT ACT[4:0])

Key values: 0x00=disabled, 0x01=ADACTPPS pin, 0x02=TMR0_overflow,
0x03=TMR1_overflow, 0x05=TMR3_overflow, 0x19=CLC1_OUT,
0x1C=software read of ADRESH, 0x1D=software read of ADERRH,
0x1E=software write to ADPCH.

## CVD Mode Setup

CVD measures relative capacitance using internal CHOLD as reference:

1. Configure pin as analog input (TRIS + ANSEL)
2. Set PPOL (ADCON1 bit 7): 1=pin→VDD/CHOLD→VSS, 0=pin→VSS/CHOLD→VDD
3. Set ADPRE > 0 to enable precharge phase (controls precharge duration)
4. Set ADACQ for charge-share (acquisition) time
5. Set DSEN (ADCON1 bit 0) = 1 for double-sample (differential CVD)
6. Set IPEN (ADCON1 bit 6) = 1 to invert precharge on 2nd sample
7. Set GPOL (ADCON1 bit 5) for guard ring initial polarity
8. Additional capacitance: ADCAP CAP[4:0] (0-31 pF, disconnected during conversion)
9. Guard ring outputs: ADGRDA/ADGRDB via PPS

ADERR = (ADRES - ADPREV) when CALC=000, DSEN=1 gives CVD differential result.

## Precharge & Acquisition Timing

- **ADPRE** (13-bit, 0x3F1): precharge clocks. 0=no precharge. Max 8191 clocks.
- **ADACQ** (13-bit, 0x3EE): acquisition clocks. 0=SW-controlled (or 8192 if ADPRE>0).
- Both timed in FOSC clocks (CS=0) or ADCRC clocks (CS=1).

## Charge Pump (ADCP at 0x3D8)

- **CPON** (bit 7): enables charge pump for low-voltage operation.
- **CPRDY** (bit 0): read; 1=charge pump output stable. Wait for this before converting.

## Key Operational Notes

- ADRES writes are always right-justified; reading with FM=0 shifts left 4 bits.
- Threshold comparisons are **signed** operations.
- AOV (accumulator overflow) triggers ADTIF; always check AOV in threshold ISR.
- GO cannot be set in same instruction that sets ON.
- Clearing GO by software during conversion: result still loaded, no ADIF set.
- CONT mode: GO stays set, auto-retriggers after each computation.
- When CS=1 (ADCRC), expect up to 5 ADCRC cycles for ACLR operation.
- Switching channels: discharge CHOLD by converting VSS (PCH=0x3B) first.
- Max recommended source impedance: 10 kΩ.
- CHOLD is **not** discharged after each conversion.

## FVR (DS Sec 38)

Stable voltage reference independent of VDD. Two output buffers:
- **Buffer 1** (ADFVR): routes to ADC as reference (PREF=11) AND as input channel (PCH=0x3E)
- **Buffer 2** (CDAFVR): routes to DAC/comparators AND to ADC as input-only channel (PCH=0x3F)

### FVRCON Register (0x3D7)

| Bit | Field  | R/W | Description                                     |
|-----|--------|-----|--------------------------------------------------|
| 7   | EN     | R/W | FVR enable (must set before use)                 |
| 6   | RDY    | R   | 1=output stable and ready                        |
| 5   | TSEN   | R/W | Temperature indicator enable                     |
| 4   | TSRNG  | R/W | Temp range: 0=Low(2VT), 1=High(3VT)             |
| 3:2 | CDAFVR | R/W | Buffer 2 gain: 00=OFF, 01=1.024V, 10=2.048V, 11=4.096V |
| 1:0 | ADFVR  | R/W | Buffer 1 gain: 00=OFF, 01=1.024V, 10=2.048V, 11=4.096V |

### FVR Output Levels

| Gain | Output Voltage |
|------|----------------|
| 1x   | 1.024 V        |
| 2x   | 2.048 V        |
| 4x   | 4.096 V        |

**FVR output must not exceed VDD.**

### FVR Routing Summary

| Buffer | To ADC as VREF+ | To ADC as Channel | To DAC/Comparator |
|--------|-----------------|-------------------|-------------------|
| 1      | PREF=11         | PCH=0x3E          | No                |
| 2      | No              | PCH=0x3F           | Yes               |

## ADC-FVR Interaction

1. Enable FVR: set FVRCON.EN, configure ADFVR/CDAFVR gain, wait for RDY=1.
2. Use FVR as VREF+: set ADREF.PREF=11 (Buffer 1 only).
3. Use FVR as input channel: select PCH=0x3E (Buffer 1) or PCH=0x3F (Buffer 2).
4. Buffer 2 can simultaneously feed DAC and appear as ADC channel.
5. At 4.096V gain setting, ensure VDD > 4.096V or output clips.
6. FVR Buffer 1 is the **only** path for FVR→ADC positive reference.
   Buffer 2 cannot serve as ADC VREF+, only as an input channel.

## Conversion Sequence (Basic Mode)

1. Configure TRIS/ANSEL for analog pin
2. Select clock (ADCON0.CS), reference (ADREF), channel (ADPCH)
3. Set ADPRE/ADACQ for timing; ADCAP for extra capacitance
4. Enable ADC: ADCON0.ON = 1
5. Set GO = 1; wait for GO to clear (poll or interrupt)
6. Read ADRES (ADRESH:ADRESL); clear ADIF