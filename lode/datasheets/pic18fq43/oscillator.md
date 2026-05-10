# PIC18F27/47/57Q43 Oscillator Module (OSC) with FSCM & ACT

## Clock Sources

| Type | Source | Description |
|------|--------|-------------|
| External | EXTOSC | External clock via FEXTOSC config (ECH/ECM/ECL/LP/XT/HS modes) |
| External | EXTOSC + 4xPLL | EXTOSC multiplied by PLL; input must meet PLL timing specs |
| External | SOSC | 32.768 kHz secondary oscillator on SOSCI/SOSCO pins |
| Internal | HFINTOSC | 1/2/4/8/12/16/32/48/64 MHz, selected via OSCFRQ |
| Internal | LFINTOSC | Fixed ~31 kHz; drives PWRT, WWDT, FSCM |
| Internal | MFINTOSC | 500 kHz and 31.25 kHz (derived from HFINTOSC; peripheral-only, not system clock) |
| Internal | ADCRC | ~600 kHz, dedicated to ADC; auto-enabled when selected |

## NOSC/COSC Clock Source Selection

NOSC (requested, OSCCON1) and COSC (current, OSCCON2) use same encoding:

| Value | Source |
|-------|--------|
| 111 | EXTOSC (per FEXTOSC config) |
| 110 | HFINTOSC |
| 101 | LFINTOSC |
| 100 | SOSC |
| 010 | EXTOSC + 4xPLL |
| 011, 001, 000 | Reserved (write ignored; NOSC/NDIV unchanged) |

## NDIV/CDIV Postscaler Divider

| Value | Divider | Value | Divider |
|-------|---------|-------|---------|
| 0000 | 1 | 1000 | 256 |
| 0001 | 2 | 1001 | 512 |
| 0010 | 4 | 1010–1111 | Reserved |
| 0011 | 8 | | |
| 0100 | 16 | | |
| 0101 | 32 | | |
| 0110 | 64 | | |
| 0111 | 128 | | |

## RSTOSC Reset Defaults

| RSTOSC | NOSC/COSC | NDIV/CDIV | OSCFRQ | Initial FOSC |
|---------|-----------|-----------|--------|--------------|
| 000 | 000 (HFINTOSC 64 MHz) | 1:1 | 64 MHz | HFINTOSC @ 64 MHz |
| 010 | 010 (EXTOSC+PLL) | 1:1 | 4 MHz | EXTOSC + 4xPLL |
| 100 | 100 (SOSC) | 1:1 | — | SOSC |
| 101 | 101 (LFINTOSC) | 1:1 | — | LFINTOSC |
| 110 | 110 (HFINTOSC) | 4:1 | 4 MHz | HFINTOSC @ 1 MHz |
| 111 | 111 (EXTOSC) | 1:1 | — | EXTOSC per FEXTOSC |

## OSCFRQ — HFINTOSC Frequency Selection (0xB1)

| FRQ[3:0] | Frequency (MHz) |
|----------|-----------------|
| 0000 | 1 |
| 0001 | 2 |
| 0010 | 4 |
| 0011 | 8 |
| 0100 | 12 |
| 0101 | 16 |
| 0110 | 32 |
| 0111 | 48 |
| 1000 | 64 |
| 1001–1111 | Reserved |

Changing OSCFRQ clears HFOR/MFOR; they reassert once HFINTOSC stabilizes. MFINTOSC may stall during transition.

## OSCTUNE — HFINTOSC Tuning (0xB0)

| Bits | Field | Description |
|------|-------|-------------|
| 7-6 | — | Unimplemented, read as 0 |
| 5-0 | TUN[5:0] | 6-bit two's complement frequency adjustment |

- 0x00 = center (calibrated) frequency
- 0x01–0x1F = increase frequency (0x1F = max increase)
- 0x20–0x3F = decrease frequency (0x20 = max decrease)
- Does not affect LFINTOSC
- **When ACT enabled**: TUN bits are read-only; controlled by ACT hardware

## OSCEN — Oscillator Manual Enable (0xB3)

| Bit | Name | Value | Description |
|-----|------|-------|-------------|
| 7 | EXTOEN | 1 | EXTOSC explicitly enabled (per FEXTOSC) |
| | | 0 | EXTOSC only enabled by requesting peripheral |
| 6 | HFOEN | 1 | HFINTOSC explicitly enabled (per OSCFRQ) |
| | | 0 | HFINTOSC only enabled by requesting peripheral |
| 5 | MFOEN | 1 | MFINTOSC explicitly enabled |
| | | 0 | MFINTOSC only enabled by requesting peripheral |
| 4 | LFOEN | 1 | LFINTOSC explicitly enabled |
| | | 0 | LFINTOSC only enabled by requesting peripheral |
| 3 | SOSCEN | 1 | SOSC explicitly enabled (per SOSCPWR) |
| | | 0 | SOSC only enabled by requesting peripheral |
| 2 | ADOEN | 1 | ADCRC explicitly enabled |
| | | 0 | ADCRC only enabled by requesting peripheral |
| 1-0 | — | — | Unimplemented, read as 0 |

**Note**: Q43 OSCEN has no PLLEN bit at bit position 1. Unlike some families, Q43 uses bit 0 for PLLEN (peripheral PLL only, not system clock PLL). The system PLL is enabled via NOSC/RSTOSC = 010 only.

## OSCSTAT — Oscillator Status (0xB2)

| Bit | Name | Description |
|-----|------|-------------|
| 7 | EXTOR | EXTOSC ready |
| 6 | HFOR | HFINTOSC ready |
| 5 | MFOR | MFINTOSC ready |
| 4 | LFOR | LFINTOSC ready |
| 3 | SOR | SOSC ready |
| 2 | ADOR | ADCRC ready |
| 1 | SFOR | **SFINTOSC ready** (unique to Q43 vs K42) |
| 0 | PLLR | PLL ready (locked and input source ready) |

All bits read-only; reset values determined by hardware.

**Q43 vs K42**: Q43 adds bit 1 (SFOR — SFINTOSC Ready). K42 has this bit as unimplemented (reads 0).

## OSCCON1/2/3 Registers

### OSCCON1 — Oscillator Control 1 (0xAD)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | — | U | 0 | Unimplemented |
| 6-4 | NOSC[2:0] | R/W | f/f | New oscillator source request |
| 3-0 | NDIV[3:0] | R/W | q/q | New divider selection request |

Writing reserved NOSC value causes entire write to be ignored. When CSWEN=0, this register is read-only.

### OSCCON2 — Oscillator Control 2 (0xAE)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | — | U | 0 | Unimplemented |
| 6-4 | COSC[2:0] | R | f/f | Current oscillator source (read-only) |
| 3-0 | CDIV[3:0] | R | f/f | Current divider (read-only) |

### OSCCON3 — Oscillator Control 3 (0xAF)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | CSWHOLD | R/W/HC | 0 | 1=hold switch when new osc ready; 0=allow switch |
| 6 | SOSCPWR | R/W | 1 | 1=SOSC high power; 0=SOSC low power. Disable SOSC before changing. |
| 5 | — | U | 0 | Unimplemented |
| 4 | ORDY | R | 0 | 1=OSCCON1 matches OSCCON2 (switch not pending) |
| 3 | NOSCR | R | 0 | 1=new oscillator ready |
| 2-0 | — | U | 0 | Unimplemented |

**Note**: SOSCPWR reset = 1 (high power default on Q43).

## Active Clock Tuning (ACT) — Q43 Unique Feature

The ACT module uses a 32.768 kHz SOSC time base to adjust HFINTOSC frequency over voltage and temperature, achieving ±1% accuracy. **Requires SOSC connected and enabled.**

### ACTCON — Active Clock Tuning Control (0xAC)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | ACTEN | R/W | 0 | 1=ACT enabled (TUN controlled by hardware); 0=TUN controlled by software |
| 6 | ACTUD | R/W | 0 | 1=suspend OSCTUNE updates; 0=allow updates (ACT must be enabled) |
| 5-4 | — | U | 0 | Unimplemented |
| 3 | ACTLOCK | R | 0 | 1=HFINTOSC within ±1% of nominal; 0=not locked or ACT disabled |
| 2-2 | — | U | 0 | Unimplemented |
| 1 | ACTORS | R | 0 | 1=tuning value out of TUN range; 0=within range |
| 0 | — | U | 0 | Unimplemented |

- **ACTEN=1**: TUN bits become read-only to software; controlled by ACT hardware.
- **ACTLOCK**: Read-only. Not locked after Reset or when ACT disabled.
- **ACTORS**: Read-only. Set when HFINTOSC requires TUN value outside ±1% range.
- **ACTUD=1**: Suspends OSCTUNE updates but ACT module continues operating; ACTLOCK updates each cycle.
- **ACT interrupt**: ACTIF set when ACTLOCK or ACTORS changes state. Enable via ACTIE.

## Fail-Safe Clock Monitor (FSCM)

Enabled by FCMEN config bit. Monitors external oscillator modes.

**Detection**: LFINTOSC ÷ 64 ≈ 488 Hz sample clock latches external clock edges. Failure = no edge within one half-period (~2 ms). On detection:
- COSC overwritten to HFINTOSC (110); frequency set by prior FRQ/NDIV state.
- OSCFIF flag set in PIR register; interrupt if OSFIE=1.

**Clearing FSCM condition**: Reset, SLEEP instruction, or writing NOSC/NDIV. OST restarts when switching back to external/PLL. OSFIF must be software-cleared.

## Reference Clock Output (CLKR)

### CLKRCON — Reference Clock Control (0x39)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | EN | R/W | 0 | 1=enable reference clock module |
| 6-5 | — | U | 0 | Unimplemented |
| 4-3 | DC[1:0] | R/W | 10 | Duty cycle (default 50%) |
| 2-0 | DIV[2:0] | R/W | 000 | Clock divider |

**DC[1:0] encoding:**
| Value | Duty Cycle |
|-------|-----------|
| 00 | 0% (constant low; for DIV ≥ 001: 0% is valid, for DIV=000: 0% output) |
| 01 | 25% |
| 10 | 50% (default) |
| 11 | 75% |

For DIV=000, duty cycle is fixed at 50% for all DC values except 00 (0%).

**DIV[2:0] encoding:**
| Value | Divider |
|-------|---------|
| 000 | Base clock (no division) |
| 001 | ÷2 |
| 010 | ÷4 |
| 011 | ÷8 |
| 100 | ÷16 |
| 101 | ÷32 |
| 110 | ÷64 |
| 111 | ÷128 |

DC and DIV should only be changed when EN=0 to avoid glitches.

### CLKRCLK — CLKR Clock Source Selection (0x3A)

| Bit | Field | R/W | Description |
|-----|-------|-----|-------------|
| 7-5 | — | U | Unimplemented |
| 4-0 | CLK[4:0] | R/W | CLKR clock source mux |

| CLK[4:0] | Source |
|----------|--------|
| 00000 | FOSC |
| 00001 | HFINTOSC |
| 00010 | LFINTOSC |
| 00011 | MFINTOSC (500 kHz) |
| 00100 | MFINTOSC (31.25 kHz) |
| 00101 | SOSC |
| 00110 | EXTOSC |
| 00111 | NCO1_OUT |
| 01000 | NCO2_OUT |
| 01001 | NCO3_OUT |
| 01010 | CLC1_OUT |
| 01011 | CLC2_OUT |
| 01100 | CLC3_OUT |
| 01101 | CLC4_OUT |
| 01110 | CLC5_OUT |
| 01111 | CLC6_OUT |
| 10000 | CLC7_OUT |
| 10001 | CLC8_OUT |
| 10010–11111 | Reserved |

**Q43 vs K42**: Q43 CLKRCLK is 5-bit (CLK[4:0]) vs K42 4-bit (CLK[3:0]). Q43 adds NCO2_OUT, NCO3_OUT, EXTOSC, and CLC5–CLC8.

## Key Register Map

| Addr | Register | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|------|----------|---|---|---|---|---|---|---|---|
| 0xAC | ACTCON | ACTEN | ACTUD | — | — | ACTLOCK | — | ACTORS | — |
| 0xAD | OSCCON1 | — | NOSC[2:0] | | NDIV[3:0] | | | | |
| 0xAE | OSCCON2 | — | COSC[2:0] | | CDIV[3:0] | | | | |
| 0xAF | OSCCON3 | CSWHOLD | SOSCPWR | — | ORDY | NOSCR | — | — | — |
| 0xB0 | OSCTUNE | — | — | | TUN[5:0] | | | | |
| 0xB1 | OSCFRQ | — | — | — | — | FRQ[3:0] | | | |
| 0xB2 | OSCSTAT | EXTOR | HFOR | MFOR | LFOR | SOR | ADOR | SFOR | PLLR |
| 0xB3 | OSCEN | EXTOEN | HFOEN | MFOEN | LFOEN | SOSCEN | ADOEN | — | PLLEN |

## Q43 Errata — Oscillator-Related

- **XT mode max frequency**: Limited to 2 MHz (revisions B0, B2). Use HS mode for >2 MHz crystals. (Not affected on B3/C0.)
- No other oscillator-specific errata for B3/C0 revisions.

## Other Notes

- **OST**: 1024 oscillation periods after POR/BOR/wake-from-Sleep for crystal/ceramic modes. Not used in EC modes.
- **SOSCPWR (OSCCON3<6>)**: Must disable SOSC before changing power mode.
- **CLKOUT**: FOSC/4 on OSC2 when CLKOUTEN=0 and mode does not use OSC2.
- **MFINTOSC**: Cannot be system clock; peripheral-only.
- **SFINTOSC**: Present in Q43 OSCSTAT (bit 1). Not documented as independently selectable clock source; internal use only.