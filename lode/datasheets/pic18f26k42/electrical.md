# PIC18F26K42 Electrical Specifications

All specs at 3.0V, 25°C unless noted. Characterized but not tested values marked *.
Two voltage ranges: PIC18F (2.3–5.5V) and PIC18LF (1.8–3.6V).

## Absolute Maximum Ratings

| Parameter | Rating |
|---|---|
| Ambient temp under bias | -40°C to +125°C |
| Storage temp | -65°C to +150°C |
| VDD pin voltage (PIC18F) | -0.3V to +6.5V |
| VDD pin voltage (PIC18LF) | -0.3V to +4.0V |
| MCLR pin voltage | -0.3V to +9.0V |
| All other pins voltage | -0.3V to (VDD + 0.3V) |
| VSS current (≤85°C) | 350 mA |
| VSS current (≤125°C) | 120 mA |
| VDD current 28-pin (≤85°C) | 250 mA |
| VDD current 28-pin (≤125°C) | 85 mA |
| VDD current 40-pin (≤85°C) | 350 mA |
| VDD current 40-pin (≤125°C) | 120 mA |
| Any I/O pin current | ±50 mA |
| Clamp current (VPIN < 0 or > VDD) | ±20 mA |
| Total power dissipation | 800 mW |

## Operating Conditions

| Param | Min | Max | Unit |
|---|---|---|---|
| VDD PIC18LF (Fosc ≤ 16 MHz) | 1.8 | 3.6 | V |
| VDD PIC18LF (Fosc > 16 MHz) | 2.5 | 3.6 | V |
| VDD PIC18LF (Fosc > 32 MHz) | 2.7 | 3.6 | V |
| VDD PIC18F (Fosc ≤ 16 MHz) | 2.3 | 5.5 | V |
| VDD PIC18F (Fosc > 16 MHz) | 2.5 | 5.5 | V |
| VDD PIC18F (Fosc > 32 MHz) | 2.7 | 5.5 | V |
| Temp (industrial) | -40 | +85 | °C |
| Temp (extended) | -40 | +125 | °C |
| VDR (RAM retention in Sleep) | 1.5 | — | V |
| VPOR (POR release) | — | 1.6 | V |
| VPORR (POR rearm) | — | 0.8 | V |
| SVDD (rise rate for POR) | 0.05 | — | V/ms |

## Supply Current IDD (3.0V, 25°C) — 28-pin PIC18F26/45/46K42

| Param | Mode | Typ | Max | Unit |
|---|---|---|---|---|
| D100 | XT 4 MHz | 680 | 1100 | μA |
| D100A | XT 4 MHz, all PMD=1 | 460 | — | μA |
| D101 | HFINTOSC 16 MHz | 3.0 | 4.2 | mA |
| D101A | HFINTOSC 16 MHz, all PMD=1 | 2.1 | — | mA |
| D102 | HFINTOSC 64 MHz (PLL) | 11.6 | 14 | mA |
| D102A | HFINTOSC 64 MHz, all PMD=1 | 7.6 | — | mA |
| D103 | HS+PLL 64 MHz | 9.9 | 13 | mA |
| D104 | Idle, HFINTOSC 16 MHz | 1.9 | 2.9 | mA |
| D105 | Doze 16 MHz, ratio 16 | 1.9 | — | mA |

## Power-Down Current IPD (3.0V)

| Parameter | Typ | Max +85°C | Max +125°C | Unit |
|---|---|---|---|---|
| Base IPD (VREGPM=1) | 0.4 | 4 | 14 | μA |
| Base IPD (VREGPM=0) | 20 | 32 | 42 | μA |
| +WDT | 1 | 4.8 | 14 | μA |
| +SOSC | 1 | 6 | 19 | μA |
| +FVR | 33 | 76 | 81 | μA |
| +BOR | 9.8 | 16 | 21.2 | μA |
| +LPBOR | 0.1 | 3 | 10.8 | μA |
| +HLVD | 9.5 | 14 | 22 | μA |
| +ADC (not converting) | 0.4 | 4 | 14 | μA |
| +Comparator | 26 | 49 | 57 | μA |

## I/O Port Characteristics

### Input Voltage Thresholds

| Buffer Type | VIL Max | VIH Min | VDD Range |
|---|---|---|---|
| TTL | 0.8V | 2.0V | 4.5–5.5V |
| TTL | 0.15·VDD | 0.25·VDD+0.8V | 1.8–4.5V |
| Schmitt Trigger | 0.2·VDD | 0.8·VDD | 2.0–5.5V |
| I2C | 0.3·VDD | 0.7·VDD | 2.0–5.5V |
| SMBus 2.0 | 0.8V | 2.1V | 2.7–5.5V |
| SMBus 3.0 | 0.8V | 1.35V | 1.8–5.5V |
| MCLR | 0.2·VDD | 0.7·VDD | — |

### Output Voltage (3.0V)

| Param | Conditions | Value |
|---|---|---|
| VOL max | IOL = 10 mA | 0.6V |
| VOH min | IOH = 6 mA | VDD - 0.7V |

### Other I/O

Input leakage: typ ±5 nA, max ±125 nA (85°C) / ±1000 nA (125°C). MCLR leakage: typ ±50 nA, max ±200 nA. Weak pull-up: typ 120 μA, max 200 μA (VDD=3V, VPIN=VSS). Pin cap: typ 5 pF, max 50 pF.

## ADC Specifications (12-bit)

| Param | Min | Typ | Max | Unit |
|---|---|---|---|---|
| Resolution | — | — | 12 | bit |
| INL (EIL) | — | ±0.1 | ±2.0 | LSb |
| DNL (EDL) | — | ±0.1 | ±1.0 | LSb |
| Offset (EOFF) | — | 0.5 | 6.0 | LSb |
| Gain (EGN) | — | ±0.2 | ±6.0 | LSb |
| VREF range | 1.8 | — | VDD | V |
| Input range | ADREF- | — | ADREF+ | V |
| Source impedance (rec.) | — | 1 | — | kΩ |
| Ref ladder impedance | — | 50 | — | kΩ |

### ADC Timing

| Param | Value | Conditions |
|---|---|---|
| TAD (FOSC source) | 0.5–9 μs | ADOCS=1 |
| TAD (ADCRC source) | typ 2 μs | ADOCS=0 |
| Conversion (FOSC) | 14·TAD + 2·TCY | ADOCS=1 |
| Conversion (ADCRC) | 16·TAD + 2·TCY | ADOCS=0 |
| S/H disconnect (FOSC) | 2·TAD + 1·TCY | ADOCS=1 |
| S/H disconnect (ADCRC) | 3·TAD + 2·TCY | ADOCS=0 |

## 5-Bit DAC Specifications

| Param | Min | Typ | Max | Unit |
|---|---|---|---|---|
| Resolution | — | — | 5 | bit |
| Step size | — | (VDACREF+/VDACREF-)/32 | — | V |
| Absolute accuracy | — | — | ±0.5 | LSb |
| Unit resistor | — | 5000 | — | Ω |
| Settling time | — | — | 10 | μs |

## Comparator Specifications (3.0V, 25°C)

| Param | Typ | Max | Unit |
|---|---|---|---|
| Input offset voltage | — | ±60 | mV |
| Input common mode range | GND–VDD | — | V |
| CMRR | 50 | — | dB |
| Hysteresis | 25 | 40 | mV (min 10) |
| Response time (rising) | 300 | 900 | ns |
| Response time (falling) | 220 | 500 | ns |

## Oscillator Specifications

### Internal Oscillators

| Source | Frequencies | Accuracy |
|---|---|---|
| HFINTOSC (precision) | 4/8/12/16/32/48/64 MHz | ±2% (0–60°C), ±3% (≤85°C), ±5% otherwise |
| HFINTOSC (low-power) | 1 MHz | ±8% (-40–85°C), ±12% (-40–125°C) |
| HFINTOSC (low-power) | 2 MHz | ±8% (-40–85°C), ±12% (-40–125°C) |
| LFINTOSC | 31 kHz | typ 31 kHz (24.8–37.2 kHz) |

### External Oscillator Ranges

| Mode | Max Freq | Condition |
|---|---|---|
| ECL | 500 kHz | — |
| ECM | 8 MHz | — |
| ECH | 64 MHz | VDD ≥ 2.7V; 32 MHz if VDD < 2.7V |
| LP | 100 kHz | — |
| XT | 4 MHz | — |
| HS | 20 MHz | — |
| SOSC | 32.768 kHz (32.4–33.1) | — |
| System (FOSC) | 64 MHz max | — |

### HFINTOSC Wake-from-Sleep (3.0V, 4 MHz): VREGPM=0: 11/20μs · VREGPM=1: 50/—μs. LFINTOSC wake: typ 0.2 ms.

### PLL

| Param | Min | Max | Unit |
|---|---|---|---|
| Input freq | 4 | 16 | MHz |
| Output freq | 16 | 64 | MHz |
| Lock time | — | typ 200 | μs |
| Output stability | -0.25 | +0.25 | % |

## Reset and WDT

### Brown-Out Reset (BOR) Voltage

| BORV | VBOR Min | Typ | Max |
|---|---|---|---|
| 00 | 2.7 | 2.85 | 3.0 |
| 01 | 2.55 | 2.70 | 2.85 |
| 10 | 2.3 | 2.45 | 2.6 |
| 11 (PIC18F) | 2.3 | 2.45 | 2.6 |
| 11 (PIC18LF) | 1.8 | 1.9 | 2.1 |

BOR hysteresis: typ 40 mV. Response: typ 3 μs. LPBOR: 1.8/2.0/2.5V.

### WDT Time-out (WDTPS=00100)

| Param | Typ | Unit |
|---|---|---|
| TWDT | 16 | ms |

PWRT period: PWRTS=00: 1ms, 01: 16ms, 10: 64ms. OST: 1024 TOSC cycles.

## Memory Programming

| Param | Value | Unit |
|---|---|---|
| EEPROM endurance | 100k | E/W (-40–85°C) |
| EEPROM retention | 40 | years |
| EEPROM byte erase/write | typ 4, max 5 | ms |
| Flash endurance | 10k | E/W (-40–85°C) |
| Flash retention | 40 | years |
| Flash row erase/write | typ 2, max 2.5 | ms |

## I/O Timing (3.0V, CL=50pF)

| Param | Typ | Max | Unit |
|---|---|---|---|
| Port output valid | 50 | 70 | ns |
| Port input setup | 20 | — | ns |
| Port input hold | 50 | — | ns |
| Rise (slew enabled) | 25 | — | ns |
| Rise (slew disabled) | 5 | — | ns |
| Fall (slew enabled) | 25 | — | ns |
| Fall (slew disabled) | 5 | — | ns |
| INT pin min pulse | 25 | — | ns |
| IOC min pulse | 25 | — | ns |

## FVR (Fixed Voltage Reference)

| Gain | Accuracy | VDD Req. |
|---|---|---|
| 1x (1.024V) | ±4% | ≥ 2.5V |
| 2x (2.048V) | ±4% | ≥ 2.5V |
| 4x (4.096V) | ±5% | ≥ 4.75V |

FVR start-up: typ 25 μs.

## HLVD Thresholds (HLVDSEL: min/typ/max)

0000: 1.73/1.90/2.07V · 0001: 1.91/2.10/2.29V · 0010: 2.05/2.25/2.45V · 0011: 2.28/2.50/2.73V · 0100: 2.37/2.60/2.83V · 0101: 2.50/2.75/3.00V · 0110: 2.64/2.90/3.16V · 0111: 2.87/3.15/3.43V · 1000: 3.05/3.35/3.65V · 1001: 3.28/3.60/3.92V · 1010: 3.41/3.75/4.09V · 1011: 3.64/4.00/4.36V · 1100: 3.82/4.20/4.58V · 1101: 3.96/4.35/4.74V · 1110: 4.23/4.65/5.07V

## ZCD Specifications

| Param | Typ | Unit |
|---|---|---|
| Voltage on ZCD pin | 0.75 | V |
| Max source/sink current | 600 | μA |
| Response time (rising/falling) | 1 | μs |

## Thermal (θJA °C/W): 28-SPDIP 60 · 28-SOIC 80 · 28-SSOP 90 · 28-UQFN 4×4 27.5 · 28-QFN 6×6 27.5. TJMAX 150°C.

## Temperature Indicator

| Param | Value | Conditions |
|---|---|---|
| Min ADC acquisition time | 25 μs | — |
| Voltage sensitivity (high range) | -3.684 mV/°C | TSRNG = 1 |
| Voltage sensitivity (low range) | -2.456 mV/°C | TSRNG = 0 |