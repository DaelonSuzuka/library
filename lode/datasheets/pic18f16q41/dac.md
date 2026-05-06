# DAC — Digital-to-Analog Converter

Source: DS40002214F §41 (pp 756–763)

## Overview

Two 8-bit ratiometric DAC modules. DAC1 has a buffered output routable to pins; DAC2 is internal-only (feeds CMP/OPA, no output buffer or pins).

**Output:** `DACx_output = ((VREF+ − VREF−) × DACR / 256) + VREF−` (n=8)

## Registers

### DAC1CON — 0x7F (127)

```
  7   6   5   4   3   2   1   0
| EN |    OE[2:0]  | PSS[1:0] | NSS[1:0] |
```

| Field | Bits | Mask | R/W | Reset | Description |
|-------|------|------|-----|-------|-------------|
| EN | 7 | 0x80 | R/W | 0 | DAC enable: 1=on, 0=off |
| OE[2:0] | 6:4 | 0x70 | R/W | 000 | Output enable (one-hot; DAC2: absent) |
| PSS[1:0] | 3:2 | 0x0C | R/W | 00 | Positive reference select |
| NSS[1:0] | 1:0 | 0x03 | R/W | 00 | Negative reference select |

### DAC2CON — 0xA2 (162)

```
  7   6   5   4   3   2   1   0
| EN |  unimpl.     | PSS[1:0] | NSS[1:0] |
```

Same PSS/NSS/EN as DAC1. No OE bits — DAC2 has no output pins.

### DAC1DATL — 0x7D (125) / DAC2DATL — 0xA0 (160)

| Field | Bits | Mask | R/W | Reset |
|-------|------|------|-----|-------|
| DACxR[7:0] | 7:0 | 0xFF | R/W | 0x00 |

## Field Encodings

### OE[2:0] — Output Enable (DAC1 only)

One-hot: only one pin active at a time.

| OE[2:0] | Output |
|---------|--------|
| 000 | Disabled |
| 001 | DAC1OUT on RA0 |
| 010 | DAC1OUT on RA2 |
| 100–111 | Reserved/invalid |

> Datasheet documents OE as 2-bit (5:4) with values 00=off, 01=RA0, 10=RA2, 11=off. The register DB defines OE as 3-bit (6:4). Both agree on the one-hot pin-select pattern. Use the 3-bit field when writing position-level masks; use the 2-bit encoding documented in the datasheet for semantic values.

### PSS[1:0] — Positive Source Select

| PSS | Reference |
|-----|-----------|
| 00 | VDD |
| 01 | VREF+ pin |
| 10 | FVR Buffer 2 output |
| 11 | Reserved (do not use) |

### NSS[1:0] — Negative Source Select

| NSS | Reference |
|-----|-----------|
| 00 | VSS |
| 01 | VREF− pin |
| 10–11 | Reserved |

> Datasheet documents NSS as 1-bit (0=VSS, 1=VREF−). Register DB defines it as 2-bit (1:0). The 2-bit encoding above is consistent with both: treat bit 0 as the selector with bit 1 reserved.

## DAC1 vs DAC2

| Feature | DAC1 | DAC2 |
|---------|------|------|
| Output buffer | Yes | No |
| Output pins | RA0, RA2 | None |
| OE bits | Yes (bits 6:4) | Absent |
| PSS/NSS/EN | Same | Same |
| Internal consumers | Peripherals | CMP, OPA |
| Address base | 0x7D–0x7F | 0xA0–0xA2 |

## Operational Notes

- **Ratiometric:** Output tracks VREF+/VREF− fluctuations proportionally (resistor ladder).
- **Sleep:** Voltage reference disabled (minimizes current); DAC1CON/DAC2CON/DAC1DATL/DAC2DATL contents preserved on wake.
- **Reset:** Module disabled, output removed from pins, DACxR cleared to zero.
- **One-hot OE:** Only one DAC1 output pin can be enabled at a time; enabling both is undefined/invalid.
- **Resolution:** 8-bit → 256 steps (0–255).
- **PSS=11 reserved:** Must not be used; result undefined.