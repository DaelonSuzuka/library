# PIC18F27/47/57Q43 Device Configuration

Configuration registers at 0x300000–0x300009. Written during programming. Write-protected once WRTC=0.

## Configuration Registers

### CONFIG1 — 0x300000 (Reset: 0xFF)

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
| 011, 001 | **Reserved** |

**FEXTOSC values:**

| Value | Meaning |
|-------|---------|
| 111 | ECH — ext clock >8 MHz |
| 110 | ECM — ext clock 500 kHz–8 MHz |
| 101 | ECL — ext clock <500 kHz |
| 100 | Oscillator not enabled |
| 010 | HS — crystal >4 MHz |
| 001 | XT — crystal 500 kHz–4 MHz |
| 000 | LP — crystal 32.768 kHz |
| 011 | **Reserved** |

### CONFIG2 — 0x300001 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 5 | FCMEN | FSCM enabled | FSCM disabled |
| 3 | CSWEN | NOSC/NDIV writable | NOSC/NDIV locked |
| 1 | PR1WAY | PRLOCK set/clear once only | PRLOCK repeatable |
| 0 | CLKOUTEN | OSC2 = I/O | OSC2 = FOSC/4 output |

> CLKOUTEN ignored when FEXTOSC = HS/XT/LP.

### CONFIG3 — 0x300002 (Reset: 0xC7)

| Bits | Field | Description |
|------|-------|-------------|
| 7:6 | BOREN[1:0] | BOR operating mode |
| 5 | LPBOREN | 0=Low-power BOR enabled, 1=disabled |
| 4 | IVT1WAY | IVTLOCK set/clear once only |
| 3 | MVECEN | 1=Multivector interrupts enabled |
| 2:1 | PWRTS[1:0] | Power-up timer period |
| 0 | MCLRE | MCLR pin enable (see LVP) |

**BOREN values:** 11=always on, 10=on while running/off in Sleep, 01=per SBOREN, 00=disabled.

**PWRTS values:** 11=disabled, 10=64 ms, 01=16 ms, 00=1 ms.

**MCLRE interaction:** If LVP=1, MCLR is forced. If LVP=0, MCLRE=1→MCLR, MCLRE=0→RE3 GPIO.

### CONFIG4 — 0x300003 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 7 | XINST | Legacy mode (extended ISA disabled) | Extended ISA enabled |
| 5 | LVP | LVP enabled, MCLR forced | HV programming only |
| 4 | STVREN | Stack overflow→Reset | No reset on overflow |
| 3 | PPS1WAY | PPSLOCK set once permanently | PPSLOCK repeatable |
| 2 | ZCD | ZCD disabled at boot | ZCD always enabled |
| 1:0 | BORV[1:0] | Brown-out voltage select |

**BORV values:** 11=1.90V, 10=2.45V, 01=2.7V, 00=2.85V.

> LVP=0 cannot be written from LVP interface.

### CONFIG5 — 0x300004 (Reset: 0xFF)

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

### CONFIG6 — 0x300005 (Reset: 0xFF)

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

### CONFIG7 — 0x300006 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 5 | DEBUG | Background debugger disabled | Background debugger enabled |
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
| 001 | 0xFFFF | 32768 | — | X* | X |
| 000 | 0x1FFFF | 65536 | — | — | X |

> BBSIZE locked once BBEN=0. Changes require Bulk Erase.

### CONFIG8 — 0x300007 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 7 | WRTAPP | App block writable | App block write-protected |
| 3 | WRTSAF | SAF writable | SAF write-protected |
| 2 | WRTD | EEPROM writable | EEPROM write-protected |
| 1 | WRTC | Config regs writable | Config regs write-protected |
| 0 | WRTB | Boot block writable | Boot block write-protected |

> WRTSAF requires SAFEN=0. WRTB requires BBEN=0. All write-protect bits sticky — Bulk Erase to clear.

### CONFIG9 — 0x300008

Reserved.

### CONFIG10 — 0x300009 (Reset: 0x01)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 0 | CP | Code protection off | Code protection on |

> CP=0: external reads return 0, CPU still reads normally. Bulk Erase required to clear.

## Device ID / Revision ID

| Register | Address | Field |
|----------|---------|-------|
| DEVICEID | 0x3FFFFE | DEV[15:0] read-only |
| REVISIONID | 0x3FFFFC | 1010b[3:0] MJRREV[5:0] MNRREV[5:0] |

**Device IDs:** PIC18F27Q43=0x7480, PIC18F47Q43=0x74A0, PIC18F57Q43=0x74C0.

Revision: bits[15:12]=0xA, bits[11:6]=major (A=0), bits[5:0]=minor.

## Code Protection

CP bit (CONFIG10[0]) controls entire program memory + Data EEPROM. CP=0 blocks external reads/writes; CPU reads unaffected. Bulk Erase required to clear.

## User ID

32 words at 0x200000–0x20003F. Readable/writable during execution.

## Device Information Area (DIA)

Read-only at 0x2C0000–0x2C003F. Factory-programmed.

| Address | Name | Description |
|---------|------|-------------|
| 0x2C0000–0x2C0023 | MUI[0:8] + MUI9 | Microchip Unique Identifier (10 words) |
| 0x2C0024–0x2C0029 | TSLR1-3 | Temp sensor low range calibration |
| 0x2C002A–0x2C002F | TSHR1-3 | Temp sensor high range calibration |
| 0x2C0030–0x2C0031 | FVRA1X | ADC FVR1 output, 1x (mV) |
| 0x2C0032–0x2C0033 | FVRA2X | ADC FVR1 output, 2x (mV) |
| 0x2C0034–0x2C0035 | FVRA4X | ADC FVR1 output, 4x (mV) |
| 0x2C0036–0x2C0037 | FVRC1X | Comparator FVR2 output, 1x (mV) |
| 0x2C0038–0x2C0039 | FVRC2X | Comparator FVR2 output, 2x (mV) |
| 0x2C003A–0x2C003B | FVRC4X | Comparator FVR2 output, 4x (mV) |

## Device Configuration Information (DCI)

Read-only at 0x3C0000–0x3C0009.

| Address | Name | 16kW | 32kW | 64kW | Description |
|---------|------|-------|-------|-------|-------------|
| 0x3C0000 | ERSIZ | 128 | 128 | 128 | Erase page size (words) |
| 0x3C0002 | WLSIZ | 0 | 0 | 0 | Write latches per row (words) |
| 0x3C0004 | URSIZ | 128 | 256 | 512 | User-erasable pages |
| 0x3C0006 | EESIZ | 1024 | 1024 | 1024 | Data EEPROM size (bytes) |
| 0x3C0008 | PCNT | 28/40/48 | 28/40/48 | 28/40/48 | Pin count |

## Operational Notes

- **LVP**: Cannot clear LVP from LVP interface. LVP=1 forces MCLR.
- **One-way locks**: PR1WAY, IVT1WAY, PPS1WAY allow one clear/set cycle.
- **Sticky bits**: WRTAPP, WRTSAF, WRTD, WRTC, WRTB, SAFEN, BBEN, CP — Bulk Erase to clear.
- **Boot block**: Set BBSIZE before BBEN=0. Once BBEN=0, both locked.
- **DEBUG bit**: Managed by development tools; must remain 1 for normal operation.