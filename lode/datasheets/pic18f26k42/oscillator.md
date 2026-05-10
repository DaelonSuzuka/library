# PIC18F26K42 Oscillator Module (OSC)

## Clock Sources

| Type | Source | Description |
|------|--------|-------------|
| External | EXTOSC | External clock via FEXTOSC config (ECH/ECM/ECL/LP/XT/HS modes) |
| External | EXTOSC + 4xPLL | EXTOSC multiplied by PLL; input must meet PLL timing specs |
| External | SOSC | 32.768 kHz secondary oscillator on SOSCI/SOSCO pins |
| Internal | HFINTOSC | 1/2/4/8/12/16/32/48/64 MHz, selected via OSCFRQ |
| Internal | LFINTOSC | Fixed ~31 kHz; drives PWRT, WWDT, FSCM |
| Internal | MFINTOSC | 500 kHz and 31.25 kHz (derived from HFINTOSC; peripheral-only, not system clock) |
| Internal | ADCRC | ~600 kHz, dedicated to ADC2; auto-enabled when selected as ADC clock |

## Clock Source Selection (NOSC/COSC)

NOSC (requested, OSCCON1) and COSC (current, OSCCON2) use same encoding:

| Value | Source |
|-------|--------|
| 111 | EXTOSC |
| 110 | HFINTOSC |
| 101 | LFINTOSC |
| 100 | SOSC |
| 010 | EXTOSC + 4xPLL |
| 011, 001, 000 | Reserved (write ignored; NOSC/NDIV unchanged) |

## Postscaler Divider (NDIV/CDIV)

| Value | Divider |
|-------|---------|
| 0000 | 1 |
| 0001 | 2 |
| 0010 | 4 |
| 0011 | 8 |
| 0100 | 16 |
| 0101 | 32 |
| 0110 | 64 |
| 0111 | 128 |
| 1000 | 256 |
| 1001 | 512 |
| 1010-1111 | Reserved |

## RSTOSC Reset Defaults (Configuration)

| RSTOSC | COSC | CDIV | OSCFRQ | Initial FOSC |
|--------|------|------|--------|-------------|
| 000 | 110 | 1:1 | 64 MHz | HFINTOSC @ 64 MHz |
| 010 | 010 | 1:1 | 4 MHz | EXTOSC + 4xPLL |
| 100 | 100 | 1:1 | — | SOSC |
| 101 | 101 | 1:1 | — | LFINTOSC |
| 110 | 110 | 4:1 | 4 MHz | HFINTOSC @ 1 MHz (FRQ=4 MHz, NDIV=4) |
| 111 | 111 | 1:1 | — | EXTOSC per FEXTOSC |

## OSCFRQ - HFINTOSC Frequency Selection (0xB1)

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
| 1001-1111 | Reserved |

Changing OSCFRQ clears HFOR/MFOR; they reassert once HFINTOSC stabilizes. MFINTOSC may stall (high or low) during transition.

## OSCTUNE - HFINTOSC Tuning (0xB0)

| Bits | Field | Description |
|------|-------|-------------|
| 7-6 | — | Unimplemented, read as 0 |
| 5-0 | TUN[5:0] | 6-bit two's complement frequency adjustment |

- 0x00 = center (calibrated) frequency
- 0x01–0x1F = increase frequency (0x1F = max)
- 0x20–0x3F = decrease frequency (0x20 = min)
- Does not affect LFINTOSC

## OSCEN - Oscillator Manual Enable (0xB3)

| Bit | Name | Value | Description |
|-----|------|-------|-------------|
| 7 | EXTOEN | 1 | EXTOSC explicitly enabled (per FEXTOSC config) |
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

Note: K42 OSCEN has no PLLEN bit (unlike Q41). PLL is enabled via RSTOSC or NOSC selection only.

## OSCSTAT - Oscillator Status (0xB2)

| Bit | Name | Description |
|-----|------|-------------|
| 7 | EXTOR | EXTOSC ready |
| 6 | HFOR | HFINTOSC ready |
| 5 | MFOR | MFINTOSC ready |
| 4 | LFOR | LFINTOSC ready |
| 3 | SOR | SOSC ready |
| 2 | ADOR | ADCRC ready |
| 1 | — | Unimplemented, read as 0 |
| 0 | PLLR | PLL ready (locked and input source ready) |

All bits read-only; reset values determined by hardware.

## OSCCON1/2/3 Registers

### OSCCON1 - Oscillator Control 1 (0xAD)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | — | U | 0 | Unimplemented |
| 6-4 | NOSC[2:0] | R/W | f/f | New oscillator source request (see NOSC table) |
| 3-0 | NDIV[3:0] | R/W | q/q | New divider selection request (see NDIV table) |

Writing reserved NOSC value causes entire write to be ignored. When CSWEN=0 (config), this register is read-only.

### OSCCON2 - Oscillator Control 2 (0xAE)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | — | U | 0 | Unimplemented |
| 6-4 | COSC[2:0] | R | f/f | Current oscillator source (read-only) |
| 3-0 | CDIV[3:0] | R | f/f | Current divider (read-only) |

### OSCCON3 - Oscillator Control 3 (0xAF)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | CSWHOLD | R/W/HC | 0 | 1=hold switch when new osc ready; 0=allow switch |
| 6 | SOSCPWR | R/W | 0 | 1=SOSC high power; 0=SOSC low power (disable SOSC before changing) |
| 5 | — | U | 0 | Unimplemented |
| 4 | ORDY | R | 0 | 1=OSCCON1 matches OSCCON2 (switch not pending) |
| 3 | NOSCR | R | 0 | 1=new oscillator ready (may be transient if CSWHOLD=0) |
| 2-0 | — | U | 0 | Unimplemented |

CSWHOLD cleared by hardware on switch completion. NOSCR may be too transient to observe when CSWHOLD=0.

## Clock Switching Procedure

Requires CSWEN config bit = 1. When CSWEN=0, NOSC/NDIV are read-only.

1. Write desired NOSC[2:0] and/or NDIV[3:0] to OSCCON1.
2. Current clock continues while new source starts/stabilizes.
3. Hardware sets NOSCR (OSCCON3<3>) and CSWIF interrupt flag when new source is ready.
4. If CSWHOLD=0: switch completes immediately → NOSC→COSC, NDIV→CDIV, ORDY set, NOSCR cleared.
5. If CSWHOLD=1: switch is suspended. Software reconfigures peripherals, then clears CSWHOLD to complete. To abandon: write COSC back to NOSC.

Sleep before switch completes: switch does not occur. On wake: if CSWHOLD=0, wakes with new clock; if CSWHOLD=1, wakes with old clock and re-requests new clock.

## Fail-Safe Clock Monitor (FSCM)

Enabled by FCMEN config bit. Monitors external oscillator modes (LP, XT, HS, ECL/ECM/ECH, SOSC).

**Detection**: LFINTOSC ÷ 64 ≈ 488 Hz sample clock latches external clock edges. Failure = no edge within one half-period (~2 ms). On detection:
- COSC overwritten to HFINTOSC (110); frequency set by prior FRQ/NDIV state.
- OSCFIF flag set in PIR register; interrupt if OSFIE=1.

**Clearing FSCM condition**: Reset, SLEEP instruction, or writing NOSC/NDIV. OST restarts when switching back to external/PLL. OSFIF must be software-cleared.

## Reference Clock Output (CLKR)

### CLKRCON - Reference Clock Control (Register 8-1)

| Bit | Field | R/W | Reset | Description |
|-----|-------|-----|-------|-------------|
| 7 | EN | R/W | 0 | 1=enable reference clock module |
| 6-5 | — | U | 0 | Unimplemented |
| 4-3 | DC[1:0] | R/W | 10 | Duty cycle (default 50%) |
| 2-0 | DIV[2:0] | R/W | 000 | Clock divider |

**DC[1:0] encoding:**
| Value | Duty Cycle |
|-------|-----------|
| 00 | 0% (valid only for DIV ≥ 2) |
| 01 | 25% |
| 10 | 50% (default) |
| 11 | 75% |

**DIV[2:0] encoding:**
| Value | Divider |
|-------|---------|
| 000 | Base FOSC (no division) |
| 001 | ÷2 |
| 010 | ÷4 |
| 011 | ÷8 |
| 100 | ÷16 |
| 101 | ÷32 |
| 110 | ÷64 |
| 111 | ÷128 |

DC and DIV should only be changed when EN=0 to avoid glitches. DC default is 50% (DC1=1 at reset).

### CLKRCLK - CLKR Clock Source Selection (Register 8-2)

| Bit | Field | R/W | Description |
|-----|-------|-----|-------------|
| 7-4 | — | U | Unimplemented |
| 3-0 | CLK[3:0] | R/W | CLKR clock source mux |

| CLK[3:0] | Source |
|----------|--------|
| 0000 | FOSC |
| 0001 | HFINTOSC |
| 0010 | LFINTOSC (31 kHz) |
| 0011 | MFINTOSC (500 kHz) |
| 0100 | MFINTOSC (31.25 kHz) |
| 0101 | SOSC |
| 0110 | NCO1 Output |
| 0111 | CLC1 Output |
| 1000 | CLC2 Output |
| 1001 | CLC3 Output |
| 1010 | CLC4 Output |
| 1011-1111 | Reserved |

## Key Register Map

| Addr | Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|------|----------|-------|---|---|---|---|---|---|---|
| 0xAD | OSCCON1 | — | NOSC[2:0] | | NDIV[3:0] | | | | |
| 0xAE | OSCCON2 | — | COSC[2:0] | | CDIV[3:0] | | | | |
| 0xAF | OSCCON3 | CSWHOLD | SOSCPWR | — | ORDY | NOSCR | — | — | — |
| 0xB0 | OSCTUNE | — | — | | | TUN[5:0] | | | |
| 0xB1 | OSCFRQ | — | — | — | — | | FRQ[3:0] | | |
| 0xB2 | OSCSTAT | EXTOR | HFOR | MFOR | LFOR | SOR | ADOR | — | PLLR |
| 0xB3 | OSCEN | EXTOEN | HFOEN | MFOEN | LFOEN | SOSCEN | ADOEN | — | — |

Note: K42 has no PLLEN bit in OSCEN; PLL for system clock is enabled only via NOSC/RSTOSC = 010.

## K42-Specific Errata

- **No oscillator-specific errata** for current silicon (A3). See DS80000773H for full errata list.
- Errata items affecting other modules: DMA reads from EEPROM (A1), DMA in Doze (A1), ADC in FOSC mode (A1), MOVFF/MOVSF corruption (A1/A3), FSR shadow registers (A1/A3), Low-Power Sleep at 3.1–3.3V on F devices (A1).

## Other Notes

- **OST**: 1024 oscillation periods after POR/BOR/wake-from-Sleep for crystal/ceramic modes. Not used in EC modes.
- **SOSCPWR** (OSCCON3<6>): 0=Low Power, 1=High Power. Disable SOSC before changing.
- **CLKOUT**: FOSC/4 output on OSC2 when CLKOUTEN config = 0 and mode does not use OSC2.
- **MFINTOSC**: Cannot be system clock source; peripheral-only (Timers, WWDT, etc.).