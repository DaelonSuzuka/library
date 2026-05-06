# PIC18F16Q41 Device Configuration

Configuration registers live at 0x300000–0x300008. They are written during programming (not at runtime by default). Write-protected once WRTC=0.

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
| 011,001 | **Reserved** |

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
| 7 | FCMENS | FSCM on SOSC failure | FSCM disabled |
| 6 | FCMENP | FSCM on EXTOSC failure | FSCM disabled |
| 5 | FCMEN | FSCM enabled | FSCM disabled |
| 3 | CSWEN | NOSC/NDIV writable | NOSC/NDIV locked |
| 1 | PR1WAY | PRLOCK set/clear once only | PRLOCK set/clear repeatedly |
| 0 | CLKOUTEN | OSC2 = I/O | OSC2 = FOSC/4 output |

> CLKOUTEN is ignored when FEXTOSC = HS/XT/LP.

### CONFIG3 — 0x300002 (Reset: 0x59)

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

**MCLRE interaction:** If LVP=1, MCLR is always active. If LVP=0, MCLRE=1→MCLR, MCLRE=0→RA3 GPIO.

### CONFIG4 — 0x300003 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 7 | XINST | Legacy mode (disabled) | Extended ISA enabled |
| 5 | LVP | LVP enabled, MCLR forced | HV programming only |
| 4 | STVREN | Stack overflow→Reset | No reset on overflow |
| 3 | PPS1WAY | PPSLOCK set once permanently | PPSLOCK repeatable |
| 2 | ZCD | ZCD disabled at boot | ZCD always enabled |
| 1:0 | BORV[1:0] | Brown-out voltage select |

**BORV values:** 11=1.90V, 10=2.45V, 01=2.7V, 00=2.85V.

> LVP=0 cannot be written from the LVP interface. Setting LVP=0 requires HV on MCLR/VPP.

### CONFIG5 — 0x300004 (Reset: 0xFF)

| Bits | Field | Description |
|------|-------|-------------|
| 6:5 | WDTE[1:0] | WDT operating mode |
| 4:0 | WDTCPS[4:0] | WDT period at POR |

**WDTE values:** 11=always on, 10=on when running/off in Sleep, 01=per WDTCON0.SEN, 00=disabled.

**WDTCPS common values:**

| WDTCPS | Divider | Timeout (31 kHz) | SWControl WDTPS? |
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

> WDTCPS=11111 is the only value where software can modify WDTPS at runtime.

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
| 5 | DEBUG | Debugger disabled | Debugger enabled |
| 4 | SAFEN | SAF disabled | SAF enabled |
| 3 | BBEN | Boot block disabled | Boot block enabled |
| 2:0 | BBSIZE[2:0] | Boot block size | |

**BBSIZE (PIC18F16Q41, BBEN=0):**

| Value | End Addr | Size (words) |
|-------|-----------|-------------|
| 110 | 0x07FF | 1024 |
| 101 | 0x0FFF | 2048 |
| 100 | 0x1FFF | 4096 |
| 011 | 0x3FFF | 8192 |
| 010 | 0x7FFF | 16384 |

> BBSIZE is locked once BBEN=0. Changes require Bulk Erase. SAFEN/BBEN protection is one-time-set.

### CONFIG8 — 0x300007 (Reset: 0xFF)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 7 | WRTAPP | App block writable | App block write-protected |
| 3 | WRTSAF | SAF writable | SAF write-protected |
| 2 | WRTD | EEPROM writable | EEPROM write-protected |
| 1 | WRTC | Config regs writable | Config regs write-protected |
| 0 | WRTB | Boot block writable | Boot block write-protected |

> All write-protection bits are one-time-set; Bulk Erase required to clear.
> WRTSAF requires SAFEN=0. WRTB requires BBEN=0.

### CONFIG9 — 0x300008 (Reset: 0x01)

| Bit | Field | 1 | 0 |
|-----|-------|---|---|
| 0 | CP | Code protection off | Code protection on |

> CP=0: external reads return 0, CPU still reads normally. Bulk Erase required to clear.

## Device ID / Revision ID

| Register | Address | Field |
|----------|---------|-------|
| DEVICEID | 0x3FFFFE | DEV[15:0] read-only |
| REVISIONID | 0x3FFFFC | 1010[3:0] \| MJRREV[5:0] \| MNRREV[5:0] |

PIC18F16Q41 Device ID = 0x7560. Revision format: bits[15:12]=0xA fixed, bits[11:6]=major rev (A=0,B=1), bits[5:0]=minor rev. Example: B1 = 0xA041.

## User ID

32 words at 0x200000–0x20003F. Readable/writable during execution.

## Operational Notes

- **DEBUG bit**: Must stay 1 for normal operation; managed by dev tools.
- **LVP trap**: Cannot clear LVP from the LVP interface. If LVP=1, MCLRE is forced.
- **One-way locks**: PR1WAY, IVT1WAY, PPS1WAY each restrict their respective lock bit to a single clear/set cycle. Choose 0 for development, 1 for production lockdown.
- **Code protection (CP)**: Does not block CPU reads; only blocks external (ICSP) access.
- **Write protection (WRTC)**: Once set, config registers cannot be changed without Bulk Erase. Set other CONFIG bits before setting WRTC=0.
- **WDT window**: WDTCWS values ≤011 enable keyed CLRWDT access — clear only within window or trigger premature reset.
- **WDTCPS 0b11111 vs 0b01011**: Both give 1:65536 divider but only 11111 allows runtime WDTPS override via WDTCON0.
- **Oscillator startup**: RSTOSC selects the initial COSC after POR. CSWEN must be 1 for runtime clock switching via NOSC/NDIV.
- **Boot block**: Set BBSIZE before BBEN=0. Once BBEN=0, both BBEN and BBSIZE are locked.