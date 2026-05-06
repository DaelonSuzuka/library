# PIC18F16Q41 Electrical Specifications

All specs at 3.0V, 25°C unless noted. Characterized but not tested values marked *.

## Absolute Maximum Ratings

| Parameter | Rating |
|---|---|
| Ambient temp under bias | -40°C to +125°C |
| Storage temp | -65°C to +150°C |
| VDD pin voltage | -0.3V to +6.5V |
| MCLR pin voltage | -0.3V to +9.0V |
| All other pins voltage | -0.3V to (VDD + 0.3V) |
| VSS current (≤85°C) | 350 mA |
| VSS current (≤125°C) | 120 mA |
| VDD current 14-pin (≤85°C) | 140 mA |
| VDD current 14-pin (≤125°C) | 50 mA |
| VDD current 20-pin (≤85°C) | 190 mA |
| VDD current 20-pin (≤125°C) | 65 mA |
| Any I/O pin current | ±50 mA |
| Clamp current (VPIN < 0 or > VDD) | ±20 mA |
| Total power dissipation | 800 mW |

## Operating Conditions

| Param | Min | Max | Unit |
|---|---|---|---|
| VDD (operating) | 1.8 | 5.5 | V |
| Temp (industrial) | -40 | +85 | °C |
| Temp (extended) | -40 | +125 | °C |
| VDR (RAM retention in Sleep) | 1.7 | — | V |
| VPOR (POR release) | — | 1.6 | V |
| VPORR (POR rearm) | — | 1.0 | V |
| SVDD (rise rate for POR) | 0.05 | — | V/ms |

## Supply Current IDD (3.0V, 25°C)

| Param | Mode | Typ | Max | Unit |
|---|---|---|---|---|
| D100 | XT 4 MHz | 640 | 870 | μA |
| D100A | XT 4 MHz, all PMD=1 | 490 | 700 | μA |
| D101 | HFINTOSC 16 MHz | 2.0 | 2.5 | mA |
| D101A | HFINTOSC 16 MHz, all PMD=1 | 1.5 | 1.9 | mA |
| D102 | HFINTOSC 64 MHz (PLL) | 6.7 | 8.2 | mA |
| D102A | HFINTOSC 64 MHz, all PMD=1 | 4.5 | 5.4 | mA |
| D103 | HS+PLL 64 MHz | 5.6 | 13.8 | mA |
| D104 | Idle, HFINTOSC 16 MHz | 1.4 | 1.8 | mA |
| D105 | Doze 16 MHz, ratio 16 | 1.5 | 1.9 | mA |

## Power-Down Current IPD (3.0V, VREGPM='b11)

| Parameter | Typ | Max +85°C | Max +125°C | Unit |
|---|---|---|---|---|
| Base IPD | 1 | 3 | 4 | μA |
| +WDT | 1.41 | 3.50 | 4.50 | μA |
| +SOSC | 2.1 | 4.6 | 7.9 | μA |
| +LPBOR | 1.2 | 3.2 | 4.2 | μA |
| +FVR Buf1 (ADC) | 183 | 215 | 221 | μA |
| +FVR Buf2 (DAC/CMP) | 59 | 74.2 | 90.7 | μA |
| +BOR | 16.6 | 20.4 | 20.8 | μA |
| +HLVD | 16.9 | 20.8 | 22.5 | μA |
| +ADC active | 485 | 789 | 790 | μA |
| +Comparator | 60 | 95 | 105 | μA |
| +OPA (pump on) | 959 | 1670 | 1730 | μA |
| +OPA (pump off) | 680 | 1200 | 1400 | μA |

VREGPM='b10 base: typ 0.5 μA, max +85°C 4.0 μA, +125°C 9.0 μA.

## I/O Port Characteristics

### Input Voltage Thresholds

| Buffer Type | VIL Max | VIH Min | VDD Range |
|---|---|---|---|
| TTL | 0.8V | 2.0V | 4.5–5.5V |
| TTL | 0.15·VDD | 0.25·VDD+0.8V | 1.8–4.5V |
| Schmitt Trigger | 0.2·VDD | 0.8·VDD | 2.0–5.5V |
| I2C | 0.3·VDD | 0.7·VDD | 2.0–5.5V |
| SMBus 2.0 | 0.8V | 2.1V | 2.7–5.5V |
| SMBus 3.0 | 0.8V | 1.35V | — |
| MCLR | 0.2·VDD | 0.7·VDD | — |

### Output Voltage (3.0V)

| Param | Conditions | Value |
|---|---|---|
| VOL max | IOL = 10 mA | 0.6V |
| VOH min | IOH = 6 mA | VDD - 0.7V |

### Other I/O

Input leakage: typ ±5 nA, max ±125 nA (85°C) / ±1000 nA (125°C). MCLR leakage: typ ±50 nA, max ±200 nA. Weak pull-up: typ 140 μA, max 200 μA (VDD=3V, VPIN=VSS). Pin cap: typ 5 pF, max 50 pF.

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
| TAD (FOSC source) | 0.5–9 μs | ADOCS=0 |
| TAD (ADCRC source) | typ 2 μs | ADOCS=1 |
| Conversion (FOSC) | 14·TAD + 2·TCY | ADOCS=0 |
| Conversion (ADCRC) | 16·TAD + 2·TCY | ADOCS=1 |
| S/H disconnect (FOSC) | 2·TAD + 1·TCY | ADOCS=0 |
| S/H disconnect (ADCRC) | 3·TAD + 2·TCY | ADOCS=1 |

## DAC Specifications (8-bit)

| Param | Min | Typ | Max | Unit |
|---|---|---|---|---|
| Resolution | — | — | 8 | bit |
| Step size | — | (VREF+/VREF-)/256 | — | V |
| Absolute accuracy | -2.5 | 1.9 | 7.0 | LSb |
| INL | -1.7 | 1.0 | 1.9 | LSb |
| DNL | -0.5 | 0.4 | 1.2 | LSb |
| Offset error | -0.8 | 1.4 | 2.5 | LSb |
| Gain error | -1.7 | -1.2 | 0.8 | LSb |
| Buffer offset (DAC1) | — | 20 | 45 | mV |
| Unit resistor | — | 20 | — | kΩ |
| Settling time | — | 10 | — | μs |

INL/DNL/offset/gain specs valid for 0x09 ≤ DAC.DATA < 0x246.

## Oscillator Specifications

### Internal Oscillators

| Source | Frequencies | Accuracy |
|---|---|---|
| HFINTOSC (precision) | 4/8/12/16/32/48/64 MHz | ±2% (0–60°C), ±3% (≤85°C), ±5% otherwise |
| HFINTOSC (low-power) | 1 MHz | ±8% (-40–85°C), ±12% (-40–125°C) |
| HFINTOSC (low-power) | 2 MHz | ±8% (-40–85°C), ±12% (-40–125°C) |
| MFINTOSC | 500 kHz | — |
| LFINTOSC | 31 kHz | typ 31 kHz (24.8–37.2 kHz) |

### External Oscillator Ranges

| Mode | Max Freq | Condition |
|---|---|---|
| ECL | 1 MHz | — |
| ECM | 16 MHz | — |
| ECH | 64 MHz | VDD ≥ 2.7V; 32 MHz if VDD < 2.7V |
| LP | 32 kHz typ | — |
| XT | 4 MHz | — |
| HS | 20 MHz | VDD > 2.5V |
| SOSC | 32.768 kHz (32.4–33.1) | — |
| System (FOSC) | 64 MHz max | — |

### HFINTOSC Wake-from-Sleep (3.0V, 4 MHz): VREGPM='b00 13/20μs · 'b01 30/48 · 'b10 115/210 · 'b11 120/220. LFINTOSC wake: typ 292 μs, max 420 μs.

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
| 11 | 1.8 | 1.9 | 2.1 |

BOR hysteresis: typ 60 mV. Response: typ 3 μs. LPBOR: 1.8/1.9/2.1V.

### WDT Time-out (WDTCPS=00100)

| Param | Typ | Unit |
|---|---|---|
| TWDT | 16 | ms |

PWRT period: typ 65 ms. OST: 1024 TOSC cycles.

## Memory Programming

| Param | Value | Unit |
|---|---|---|
| EEPROM endurance | 100k | E/W (-40–85°C) |
| EEPROM retention | 40 | years |
| EEPROM byte erase/write | 11 | ms max |
| Flash endurance | 1k | E/W (-40–85°C) |
| Flash retention | 40 | years |
| Flash page write | 10 | ms max |
| Flash page erase | 11 | ms max |
| Flash word write | 75 | μs max |

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

0000: 1.73/1.90/2.07V · 0101: 2.50/2.75/3.00V · 1010: 3.41/3.75/4.09V · 1110: 4.23/4.65/5.07V

## Thermal (θJA °C/W): 14-SOIC 95.3 · 14-TSSOP 100 · 20-PDIP 62.2 · 20-SOIC 77.7 · 20-SSOP 87.3 · 20-VQFN 79.7. TJMAX 150°C.