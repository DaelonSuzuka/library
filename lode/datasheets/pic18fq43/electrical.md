# PIC18F27/47/57Q43 Electrical Specifications

All specs at 3.0V, 25°C unless noted. Characterized but not tested values marked *.
Single voltage range: 1.8V–5.5V (PIC18F27Q43; 40/48-pin extends to same range per datasheet).

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
| VDD current 28-pin (≤85°C) | 250 mA |
| VDD current 28-pin (≤125°C) | 85 mA |
| Any I/O pin current | ±50 mA |
| Clamp current | ±20 mA |
| Total power dissipation | 800 mW |

## Operating Conditions

| Param | Min | Max | Unit |
|---|---|---|---|
| VDD (Fosc ≤ 16 MHz) | 1.8 | 5.5 | V |
| VDD (Fosc > 16 MHz) | 2.5 | 5.5 | V |
| VDD (Fosc > 32 MHz) | 2.7 | 5.5 | V |
| Temp (industrial) | -40 | +85 | °C |
| Temp (extended) | -40 | +125 | °C |
| VDR (RAM retention in Sleep) | 1.7 | — | V |
| VPOR (POR release) | — | 1.6 | V |
| VPORR (POR rearm) | — | 1.0 | V |
| SVDD (rise rate for POR) | 0.05 | — | V/ms |

## NVM Specifications

| Param | Value | Unit |
|---|---|---|
| DFM endurance | 100K | E/W (-40–85°C) |
| DFM retention | 40 | years |
| PFM endurance | 10K | E/W (-40–85°C) |
| PFM retention | 40 | years |

## BOR Voltage Thresholds

| BORV | Min | Typ | Max |
|---|---|---|---|
| 11 | 1.90 | 2.10 | 2.30 |
| 10 | 2.55 | 2.70 | 2.85 |
| 01 | 2.70 | 2.85 | 3.00 |
| 00 | 2.70 | 2.85 | 3.00 |

LPBOR: typ 1.9V.

## FVR (Fixed Voltage Reference)

| Gain | Accuracy | VDD Req. |
|---|---|---|
| 1x (1.024V) | ±4% | ≥ 2.5V |
| 2x (2.048V) | ±4% | ≥ 2.5V |
| 4x (4.096V) | ±5% | ≥ 4.75V |

FVR start-up: typ 25 µs.

## ZCD Specifications

| Param | Typ | Unit |
|---|---|---|
| Voltage on ZCD pin | 0.75 | V |
| Max source/sink current | 600 | µA |
| Response time (rising/falling) | 1 | µs |

## Thermal

θJA °C/W: 28-SPDIP 60 · 28-SOIC 80 · 28-SSOP 90 · 28-UQFN 4×4 27.5 · 28-QFN 6×6 27.5 · 40-PDIP 70 · 44-TQFP 72 · 44-QFN 30 · 48-TQFP 67 · 48-UQFN 26 · 48-VQFN 21.

TJMAX: 150°C.

## Temperature Indicator

| Param | Value | Conditions |
|---|---|---|
| Min ADC acquisition time | 25 µs | — |
| Voltage sensitivity (high range) | -3.684 mV/°C | TSRNG = 1 |
| Voltage sensitivity (low range) | -2.456 mV/°C | TSRNG = 0 |