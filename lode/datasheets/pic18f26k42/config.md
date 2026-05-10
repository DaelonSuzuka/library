# PIC18F26K42 Device Configuration

Configuration registers at 0x300000–0x300009. Written during programming. Write-protected once WRTC=0.

## Configuration Registers

### CONFIG1L — 0x300000 (Reset: 0xFF)

| Bits | Field | Description |
|------|-------|-------------|
| 6:4 | RSTOSC[2:0] | Power-up default for COSC |
| 2:0 | FEXTOSC[2:0] | External oscillator mode |

**RSTOSC values:**

| Value | Meaning |
|-------|---------|
| 111 | EXTOSC per FEXTOSC bits |
| 110 | HFINTOSC 4 MHz, CDIV=4:1 |
| 101 | LFINTOSC |
| 100 | SOSC |
| 010 | EXTOSC with 4x PLL per FEXTOSC |
| 000 | HFINTOSC 64 MHz, CDIV=1:1 |
| 011,001 | **Reserved** |

**FEXTOSC values:**

| Value | Meaning |
|-------|---------|
| 111 | ECH — ext clock high power |
| 110 | ECM — ext clock medium power |
| 101 | ECL — ext clock low power |
| 100 | Oscillator not enabled |
| 010 | HS — crystal >8 MHz |
| 001 | XT — crystal 500 kHz–8 MHz |
| 000 | LP — crystal 32.768 kHz |
| 011 | **Reserved** |

### CONFIG1H — 0x300001 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 5 | FCMEN | FSCM enabled | FSCM disabled |
| 3 | CSWEN | NOSC/NDIV writable | NOSC/NDIV locked |
| 1 | PR1WAY | PRLOCK set/clear once only | PRLOCK repeatable |
| 0 | CLKOUTEN | OSC2 = I/O | OSC2 = FOSC/4 output |

> CLKOUTEN is ignored when FEXTOSC = HS/XT/LP.

### CONFIG2L — 0x300002 (Reset: 0xFF)

| Bits | Field | Description |
|------|-------|-------------|
| 7:6 | BOREN[1:0] | Brown-out Reset mode |
| 5 | LPBOREN | 0=Low-power BOR enabled |
| 4 | IVT1WAY | IVTLOCK set/clear once only |
| 3 | MVECEN | 1=Multivector interrupts |
| 2:1 | PWRTS[1:0] | Power-up timer period |
| 0 | MCLRE | MCLR pin enable (see LVP) |

**BOREN values:** 11=always on, 10=on while running/off in Sleep, 01=per SBOREN, 00=disabled.

**PWRTS values:** 11=disabled, 10=64 ms, 01=16 ms, 00=1 ms.

**MCLRE interaction:** If LVP=1, MCLR is forced. If LVP=0, MCLRE=1→MCLR, MCLRE=0→RE3 GPIO.

### CONFIG2H — 0x300003 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 7 | XINST | Legacy mode (extended ISA disabled) | Extended ISA enabled |
| 5 | DEBUG | Debugger disabled | Debugger enabled |
| 4 | STVREN | Stack overflow→Reset | No reset on overflow |
| 3 | PPS1WAY | PPSLOCK set once permanently | PPSLOCK repeatable |
| 2 | ZCD | ZCD disabled at boot | ZCD always enabled |
| 1:0 | BORV[1:0] | Brown-out voltage select |

**BORV values (PIC18F):** 11=2.45V, 10=2.45V, 01=2.7V, 00=2.85V.
**BORV values (PIC18LF):** 11=1.90V, 10=2.45V, 01=2.7V, 00=2.85V.

> BORV ≥2.7V recommended at ≥16 MHz.

### CONFIG3L — 0x300004 (Reset: 0xFF)

| Bits | Field | Description |
|------|-------|-------------|
| 6:5 | WDTE[1:0] | WDT operating mode |
| 4:0 | WDTCPS[4:0] | WDT period at POR |

**WDTE values:** 11=always on, 10=on when running/off in Sleep, 01=per WDTCON0.SEN, 00=disabled.

**WDTCPS common values:**

| WDTCPS | Divider | Timeout (31 kHz) | SW Control WDTPS? |
|--------|---------|-------------------|-------------------|
| 11111 | 1:65536 | 2 s | Yes |
| 01011 | 1:65536 | 2 s | No |
| 10010 | 1:8M | 256 s | No |
| 01010 | 1:32768 | 1 s | No |
| 01001 | 1:16384 | 512 ms | No |
| 01000 | 1:8192 | 256 ms | No |
| 00111 | 1:4096 | 128 ms | No |
| 00110 | 1:2048 | 64 ms | No |
| 00101 | 1:1024 | 32 ms | No |
| 00100 | 1:512 | 16 ms | No |
| 00000 | 1:32 | 1 ms | No |

> WDTCPS=11111 is the only value allowing runtime WDTPS override.

### CONFIG3H — 0x300005 (Reset: 0xFF)

| Bits | Field | Description |
|------|-------|-------------|
| 5:3 | WDTCCS[2:0] | WDT clock source |
| 2:0 | WDTCWS[2:0] | WDT window select |

**WDTCCS values (requires WDTE≠00):**

| Value | Source |
|-------|--------|
| 111 | Software control |
| 010 | SOSC |
| 001 | 31.25 kHz MFINTOSC |
| 000 | 31.0 kHz LFINTOSC |
| 011–110 | **Reserved** |

**WDTCWS window values:**

| Value | Window Delay % | Window Open % | Keyed Access |
|-------|---------------|---------------|--------------|
| 111 | — | 100% | No |
| 110 | — | 100% | Yes |
| 101 | 25% | 75% | No |
| 100 | 37.5% | 62.5% | No |
| 011 | 50% | 50% | **Yes** |
| 010 | 62.5% | 37.5% | Yes |
| 001 | 75% | 25% | Yes |
| 000 | 87.5% | 12.5% | Yes |

> WDTCWS≤011 enables keyed window access (CLRWDT must happen within open window).

### CONFIG4L — 0x300006 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 7 | WRTAPP | App block writable | App block write-protected |
| 4 | SAFEN | SAF disabled | SAF enabled |
| 3 | BBEN | Boot block disabled | Boot block enabled |
| 2:0 | BBSIZE[2:0] | Boot block size | |

**BBSIZE (BBEN=0):**

| Value | End Addr | Size (words) | 16k | 32k | 64k |
|-------|-----------|-------------|-----|-----|-----|
| 111 | 0x03FF | 512 | X | X | X |
| 110 | 0x07FF | 1024 | X | X | X |
| 101 | 0x0FFF | 2048 | X | X | X |
| 100 | 0x1FFF | 4096 | X | X | X |
| 011 | 0x3FFF | 8192 | X | X | X |
| 010 | 0x7FFF | 16384 | — | X | X |
| 001 | 0xFFFF | 32768 | — | Note² | X |

> BBSIZE locked once BBEN=0. Changes require Bulk Erase. WRTAPP/SAFEN/BBEN are sticky bits.

### CONFIG4H — 0x300007 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 5 | LVP | LVP enabled, MCLR forced | HV programming only |
| 3 | WRTSAF | SAF writable | SAF write-protected |
| 2 | WRTD | EEPROM writable | EEPROM write-protected |
| 1 | WRTC | Config regs writable | Config regs write-protected |
| 0 | WRTB | Boot block writable | Boot block write-protected |

> LVP=0 cannot be written from LVP interface. WRTSAF requires SAFEN=0. WRTB requires BBEN=0. All write-protect bits are one-time-set.

### CONFIG5L — 0x300008 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 0 | CP | Code protection off | Code protection on |

> CP=0: external reads return 0, CPU still reads normally. Bulk Erase required to clear.

### CONFIG5H — 0x300009 (Reset: 0xFF)

All bits unimplemented (read as 1).

## Device ID / Revision ID

| Register | Address | Field |
|----------|---------|-------|
| DEVICEID | 0x3FFFFE | DEV[15:0] read-only |
| REVISIONID | 0x3FFFFC | 1010b\[3:0\] MJRREV[5:0] MNRREV[5:0] |

**Device IDs:** F26K42=0x6C60, F27K42=0x6C40, F45K42=0x6C20, F46K42=0x6C00, F47K42=0x6BE0, F55K42=0x6BC0, F56K42=0x6BA0, F57K42=0x6B80. LF variants: LF26K42=0x6DA0, LF27K42=0x6D80, LF45K42=0x6D60, LF46K42=0x6D40, LF47K42=0x6D20, LF55K42=0x6D00, LF56K42=0x6CE0, LF57K42=0x6CC0.

Revision: bits\[15:12\]=0xA, bits\[11:6\]=major (A=0), bits\[5:0\]=minor.

## Code Protection

CP bit (CONFIG5L[0]) controls entire program memory + Data EEPROM. CP=0 blocks external reads/writes; CPU reads unaffected. Bulk Erase required to clear.

## User ID

8 words at 0x200000–0x20000F. Readable/writable during execution.

## Device Information Area (DIA)

Read-only region at 0x3F0000–0x3F003F. Factory-programmed.

| Address | Name | Description |
|---------|------|-------------|
| 0x3F0000–0x3F000B | MUI[0:5] | Microchip Unique Identifier (6 words) |
| 0x3F000C–0x3F000F | MUI[6:7] | Unassigned (2 words) |
| 0x3F0010–0x3F0023 | EUI[0:9] | Optional External Unique Identifier (10 words) |
| 0x3F0024–0x3F0025 | — | Reserved |
| 0x3F0026–0x3F0027 | TSLR2 | Temp sensor ADC @ 90°C, low range |
| 0x3F002C–0x3F002D | TSHR2 | Temp sensor ADC @ 90°C, high range |
| 0x3F0030–0x3F0031 | FVRA1X | ADC FVR1 output voltage, 1x (mV) |
| 0x3F0032–0x3F0033 | FVRA2X | ADC FVR1 output voltage, 2x (mV) |
| 0x3F0034–0x3F0035 | FVRA4X | ADC FVR1 output voltage, 4x (mV) |
| 0x3F0036–0x3F0037 | FVRC1X | Comparator FVR2 output, 1x (mV) |
| 0x3F0038–0x3F0039 | FVRC2X | Comparator FVR2 output, 2x (mV) |
| 0x3F003A–0x3F003B | FVRC4X | Comparator FVR2 output, 4x (mV) — absent on LF |

## Device Configuration Information (DCI)

Read-only at 0x3FFF00–0x3FFF09.

| Address | Name | Description |
|---------|------|-------------|
| 0x3FFF00 | ERSIZ | Erase row size: 64 words |
| 0x3FFF02 | WLSIZ | Write latches per row: 128 bytes |
| 0x3FFF04 | URSIZ | User rows: 512 (26K42) |
| 0x3FFF06 | EESIZ | Data EEPROM: 1024 bytes (26K42) |
| 0x3FFF08 | PCNT | Pin count: 28/40/48 |

## Operational Notes

- **LVP**: Cannot clear LVP from LVP interface. LVP=1 forces MCLR.
- **One-way locks**: PR1WAY, IVT1WAY, PPS1WAY allow one clear/set cycle.
- **Sticky bits**: WRTAPP, WRTSAF, WRTD, WRTC, WRTB, SAFEN, BBEN, CP — Bulk Erase to clear.
- **Boot block**: Set BBSIZE before BBEN=0. Once BBEN=0, both locked.
- **WDT window**: WDTCWS≤011 → keyed CLRWDT access required.
- **WDTCPS 11111 vs 01011**: Same divider (1:65536) but only 11111 allows runtime WDTPS override.
- **BORV**: ≥2.7V recommended for ≥16 MHz.