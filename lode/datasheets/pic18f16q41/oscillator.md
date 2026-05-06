# PIC18F16Q41 Oscillator Module (OSC)

## Clock Sources

| Type | Source | Description |
|------|--------|-------------|
| External | EXTOSC | External clock via FEXTOSC config (EC/LP/XT/HS modes) |
| External | EXTOSC + 4xPLL | EXTOSC multiplied by PLL |
| External | SOSC | 32.768 kHz secondary oscillator on SOSCI/SOSCO pins |
| Internal | HFINTOSC | 1/2/4/8/12/16/32/48/64 MHz, selected via OSCFRQ |
| Internal | LFINTOSC | Fixed ~31 kHz |
| Internal | MFINTOSC | 500 kHz and 31.25 kHz (derived from HFINTOSC; peripheral-only, not system clock) |
| Internal | ADCRC | ~600 kHz, dedicated to ADC; auto-enabled when selected |

## Clock Source Selection (NOSC/COSC)

NOSC (requested) and COSC (current active) use the same encoding:

| Value | Source |
|-------|--------|
| 111 | EXTOSC |
| 110 | HFINTOSC |
| 101 | LFINTOSC |
| 100 | SOSC |
| 010 | EXTOSC + 4xPLL |
| 011, 001, 000 | Reserved |

Values 000, 001, 011 are reserved; writing them to NOSC is ignored.

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

| RSTOSC | COSC | NDIV | OSCFRQ | Clock Source |
|--------|------|------|--------|-------------|
| 000 | 000 | 1:1 | 64 MHz | HFINTOSC @ 64 MHz |
| 010 | 010 | 1:1 | 4 MHz | EXTOSC + 4xPLL |
| 100 | 100 | 1:1 | — | SOSC |
| 101 | 101 | 1:1 | — | LFINTOSC |
| 110 | 110 | 4:1 | 4 MHz | HFINTOSC @ 1 MHz (FRQ=4MHz, NDIV=4) |
| 111 | 111 | 1:1 | — | EXTOSC per FEXTOSC |

## OSCFRQ - HFINTOSC Frequency Selection

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

Changing OSCFRQ clears HFOR/MFOR; they reassert once the oscillator stabilizes.

## OSCEN - Oscillator Enable Register

| Bit | Name | Purpose |
|-----|------|---------|
| 7 | EXTOEN | EXTOSC explicitly enabled |
| 6 | HFOEN | HFINTOSC explicitly enabled |
| 5 | MFOEN | MFINTOSC explicitly enabled |
| 4 | LFOEN | LFINTOSC explicitly enabled |
| 3 | SOSCEN | SOSC explicitly enabled |
| 2 | ADOEN | ADCRC explicitly enabled |
| 0 | PLLEN | PLL enable for peripheral clock (no effect on system clock) |

Setting a bit = 1 forces the oscillator on; clearing it = 0 allows peripheral auto-enable only. OSCEN cannot manually enable the 4xPLL for system clock use.

## Clock Switching Procedure

Requires CSWEN config bit = 1. When CSWEN = 0, NOSC/NDIV are read-only.

1. Write desired NOSC[2:0] and NDIV[3:0] to OSCCON1.
2. Current clock continues operating while new source starts.
3. Hardware sets NOSCR (bit 3 of OSCCON3) when the new source is ready.
4. Hardware sets CSWIF interrupt flag; if CSWIE=1, interrupt fires.
5. Switch completes: hardware copies NOSC→COSC, NDIV→CDIV, sets ORDY, clears NOSCR.

**CSWHOLD** (OSCCON3 bit 7): Set to 1 to suspend the switch after NOSCR asserts. Software can then reconfigure peripherals for the new frequency before clearing CSWHOLD to complete the switch. To abandon a held switch, write COSC back into NOSC.

Sleep before switch completes: switch does not occur; on wake-up, switch proceeds (CSWHOLD=0) or re-requests (CSWHOLD=1).

## Fail-Safe Clock Monitor (FSCM)

Three independent monitors, each enabled via config bits:
- **FOSC FSCM** (FCMEN): Monitors system clock. On failure → auto-switches to HFINTOSC, sets OSFIF + FSCMFEV.
- **Primary EXTOSC FSCM** (FCMENP): Monitors EXTOSC. On failure → sets OSFIF + FSCMPEV; no auto-switch.
- **Secondary SOSC FSCM** (FCMENS): Monitors SOSC. On failure → sets OSFIF + FSCMSEV; no auto-switch.

Detection: LFINTOSC ÷ 64 ≈ 484 Hz sample clock latches external clock edges; failure = no edge within ~2 ms half-period.

**FSCMCON register (0x458):**
| Bit | Name | R/W | Purpose |
|-----|------|-----|---------|
| 5 | FSCMSFI | R/W | SOSC fault injection |
| 4 | FSCMSEV | R/W | SOSC failure status |
| 3 | FSCMPFI | R/W | Primary EXTOSC fault injection |
| 2 | FSCMPEV | R/W | Primary EXTOSC failure status |
| 1 | FSCMFFI | R/W | FOSC fault injection |
| 0 | FSCMFEV | R/W | FOSC failure status |

Clearing FOSC fail-safe condition: Reset, SLEEP, or NOSC/NDIV change. OST restarts for external/PLL targets. OSFIF must be software-cleared before switching back to external oscillator.

## Active Clock Tuning (ACT)

Uses SOSC (32.768 kHz) as reference to achieve ±1% HFINTOSC accuracy over voltage/temperature.

**ACTCON register (0xAC):**
| Bit | Name | R/W | Purpose |
|-----|------|-----|---------|
| 7 | ACTEN | R/W | 1=ACT enabled (HW controls OSCTUNE); 0=SW controls OSCTUNE |
| 6 | ACTUD | R/W | 1=suspend OSCTUNE updates; 0=continuous updates |
| 3 | ACTLOCK | R | 1=HFINTOSC locked within ±1%; 0=not locked |
| 1 | ACTORS | R | 1=tuning value out of OSCTUNE range; 0=in range |

When ACTEN=1, OSCTUNE TUN[5:0] becomes read-only (HW-controlled). ACTLOCK asserts when tuned; ACTORS asserts if the required TUN value exceeds range. ACTIF interrupt flag sets on ACTLOCK or ACTORS state changes; enabled by ACTIE.

## Key Register Map

| Addr | Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|------|----------|-------|---|---|---|---|---|---|---|
| 0xAC | ACTCON | ACTEN | ACTUD | — | — | ACTLOCK | — | ACTORS | — |
| 0xAD | OSCCON1 | — | NOSC[2:0] | | NDIV[3:0] | | | | |
| 0xAE | OSCCON2 | — | COSC[2:0] | | CDIV[3:0] | | | | |
| 0xAF | OSCCON3 | CSWHOLD | SOSCPWR | — | ORDY | NOSCR | — | — | — |
| 0xB0 | OSCTUNE | — | — | | | | | TUN[5:0] | |
| 0xB1 | OSCFRQ | — | — | — | — | | | FRQ[3:0] | |
| 0xB2 | OSCSTAT | EXTOR | HFOR | MFOR | LFOR | SOR | ADOR | SFOR | PLLR |
| 0xB3 | OSCEN | EXTOEN | HFOEN | MFOEN | LFOEN | SOSCEN | ADOEN | — | PLLEN |
| 0x458 | FSCMCON | — | — | FSCMSFI | FSCMSEV | FSCMPFI | FSCMPEV | FSCMFFI | FSCMFEV |

## OSCTUNE Frequency Tuning

TUN[5:0] is a 6-bit two's-complement value (default 0x00 = center frequency):
- 0x01–0x1F = increase frequency
- 0x20–0x3F = decrease frequency
- OSCTUNE adjustments do not affect LFINTOSC.

## Other Notes

- **OST**: 1024 oscillation periods after POR/BOR/wake-from-Sleep for crystal/ceramic resonator stability. Sets EXTOR (or SOR for SOSC).
- **SOSCPWR** (OSCCON3 bit 6): 0=Low Power, 1=High Power. Must disable SOSC before changing.
- **CLKOUT**: FOSC/4 output on OSC2 when CLKOUTEN config = 0.
- MFINTOSC (500 kHz / 31.25 kHz) cannot be a system clock source; peripheral-only.