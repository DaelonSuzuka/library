# PIC18F26K42 DMA Module

## Overview
2-channel DMA controller transfers data between memory regions without CPU intervention.
Each byte transfer is a 2-cycle operation (read into DMABUF, then write to destination).
The two DMA modules (DMA1, DMA2) operate independently with separate register sets.

**Memory access:**
- Read: GPR/SFR, Program Flash Memory (PFM), Data EEPROM
- Write: GPR/SFR only (no write to PFM or EEPROM)

**Bus arbitration:** DMA shares the 16-bit instruction bus and 8-bit data bus with the CPU.
When DMA priority > CPU, DMA stalls the CPU until transfer completes. When CPU priority >
DMA, DMA uses "bubble" cycles (unused CPU slots). Priority is configurable via the system
arbiter (PR registers). Priority must be locked with the PRLOCK sequence after configuration.

## Register Map

DMA1 registers (x=1) at base 0x__, DMA2 registers (x=2) at base 0x__:

| Register | Size | Description |
|----------|------|-------------|
| DMAxCON0 | 8 | Control register 0 (EN, SIRQEN, DGO, AIRQEN, XIP) |
| DMAxCON1 | 8 | Control register 1 (DMODE, DSTP, SMR, SMODE, SSTP) |
| DMAxBUF | 8 | Data buffer (read-only) |
| DMAxSSA | 22-bit | Source start address (SSAU:SSAH:SSAL) |
| DMAxSPTR | 22-bit | Source pointer (SPTRU:SPTRH:SPTRL, read-only, runtime) |
| DMAxSSZ | 12-bit | Source message size (SSZH:SSZL) |
| DMAxSCNT | 12-bit | Source count (SCNTH:SCNTL, read-only, runtime) |
| DMAxDSA | 16-bit | Destination start address (DSAH:DSAL) |
| DMAxDPTR | 16-bit | Destination pointer (DPTRH:DPTRL, read-only, runtime) |
| DMAxDSZ | 12-bit | Destination message size (DSZH:DSZL) |
| DMAxDCNT | 12-bit | Destination count (DCNTH:DCNTL, read-only, runtime) |
| DMAxSIRQ | 7-bit | Start interrupt request source select (SIRQ[6:0]) |
| DMAxAIRQ | 7-bit | Abort interrupt request source select (AIRQ[6:0]) |

Priority registers: DMA1PR, DMA2PR (system arbiter scheme).

## Key Bit Fields

### DMAxCON0
| Bit | Name | Access | Function |
|-----|------|--------|----------|
| 7 | EN | R/W | Module enable |
| 6 | SIRQEN | R/W/HC | Enable hardware start triggers; cleared by abort/stop |
| 5 | DGO | R/W/HS/HC | Transfer in progress; set by SW or HW, cleared on stop |
| 2 | AIRQEN | R/W/HC | Enable hardware abort triggers; auto-cleared on abort |
| 0 | XIP | R/HS/HC | 1 = data in buffer not yet written to destination |

### DMAxCON1
| Bits | Name | Function |
|------|------|----------|
| 7:6 | DMODE | Dest addr mode: 00=fixed, 01=increment, 10=decrement, 11=reserved |
| 5 | DSTP | 1 = clear SIRQEN when dest counter reloads |
| 4:3 | SMR | Source memory region: 00=GPR/SFR, 01=PFM, 1x=Data EEPROM |
| 2:1 | SMODE | Source addr mode: 00=fixed, 01=increment, 10=decrement, 11=reserved |
| 0 | SSTP | 1 = clear SIRQEN when source counter reloads |

## Addressing Modes

Source address: 22-bit (DMAxSSA/DMAxSPTR), supports GPR/SFR, PFM, or EEPROM via SMR bits.
Destination address: 16-bit (DMAxDSA/DMAxDPTR), always targets GPR/SFR space.

Each pointer updates after every transaction based on mode:
- 00 (Fixed): pointer unchanged (e.g., SFR register like U1TXB)
- 01 (Increment): pointer increments by 1 (e.g., RAM buffer fill)
- 10 (Decrement): pointer decrements by 1
- 11: Reserved, do not use

## Message Size / Counters

- Transaction = 1 byte transfer (read → DMABUF → write)
- Message = 1+ transactions; SSZ/DSZ define message length
- Process = 1+ messages (when SSZ != DSZ, ratio determines messages per process)
- On trigger, counters (SCNT/DCNT) load from size registers (SSZ/DSZ), pointers load from
  start addresses (SSA→SPTR, DSA→DPTR)
- When a counter decrements from 1, it reloads from its size register and pointer reloads
  from start address
- **SCNT/DCNT never read as zero** — value 1 reloads immediately from corresponding size
- If SSZ != DSZ, the larger counter continues across messages; the smaller counter resets
  each message. Uneven ratios cause remainder skew on subsequent messages.

## Transfer Modes

### One-shot (SSTP=1 or DSTP=1)
When the selected counter reloads (reaches zero), SIRQEN is cleared, stopping further
hardware-triggered messages. Software can re-arm by setting SIRQEN again.

### Repeated (SSTP=0 and DSTP=0, hardware-triggered)
After each message completes (counter reloads), the DMA re-arms and waits for the next
hardware trigger. SCNTIF/DCNTIF flags are set on each counter reload.

### Continuous (SSTP=0 and DSTP=0, with ongoing trigger)
Same as repeated; each trigger starts a new message. Level-triggered sources (e.g. UART RX)
will automatically re-trigger as long as the condition persists.

## Starting Transfers

1. **Software control:** Set DGO bit (requires EN=1). Writing DGO while already set has no
   effect. Clearing DGO performs a soft-stop; DMA state preserved and can resume.
2. **Hardware trigger (SIRQ):** Set SIRQEN=1, select trigger via DMAxSIRQ. When the
   selected interrupt flag is set, DGO is set and transfer begins.

## Stopping Transfers

1. **Clear DGO:** Soft-stop. DMA pauses; setting DGO again resumes from where it left off.
   If source was read but not yet written (XIP=1), buffered data is lost.
2. **Hardware abort (AIRQ):** Set AIRQEN=1, select source via DMAxAIRQ. Clears DGO
   (soft-stop), SIRQEN, and AIRQEN. No state lost; can resume by re-setting DGO+AIRQEN+SIRQEN.
3. **Source count reload + SSTP:** Clears SIRQEN after source counter reloads.
4. **Dest count reload + DSTP:** Clears SIRQEN after dest counter reloads.
5. **Clear EN:** Hard-stop. Resets all DMA state; cannot resume.

**Stop latency:** One extra instruction cycle after stop condition before it takes effect;
one more read or write may still occur.

## Interrupts

| Flag | Condition |
|------|-----------|
| DMAxSCNTIF | Source counter reloaded (message boundary) |
| DMAxDCNTIF | Dest counter reloaded (message boundary) |
| DMAxAIF | Abort trigger received (DMA halted) |
| DMAxORIF | New trigger received while DGO still set (edge triggers only) |

Overrun (ORIF) is only relevant for edge-triggered sources. Level-triggered sources (e.g.,
UART TX) cannot generate overrun because they remain asserted.

## DMA Trigger Sources (DMAxSIRQ / DMAxAIRQ)

7-bit value selects interrupt source. Key mappings:

| Value | Source | Level? |
|-------|--------|--------|
| 0x00 | Reserved | — |
| 0x07 | IOCIF | Yes |
| 0x0A | ADIF | No |
| 0x0B | ADTIF | No |
| 0x10–0x13 | DMA1 SCNT/DCNT/OR/AIF | No |
| 0x14 | SPI1RXIF | Yes |
| 0x15 | SPI1TXIF | Yes |
| 0x17 | I2C1RXIF | Yes |
| 0x18 | I2C1TXIF | Yes |
| 0x1B | U1RXIF | Yes |
| 0x1C | U1TXIF | Yes |
| 0x1F | TMR0IF | No |
| 0x20 | TMR1IF | No |
| 0x22 | TMR2IF | No |
| 0x25 | NCOIF | No |
| 0x28 | INT1IF | No |
| 0x2A–0x2D | DMA2 SCNT/DCNT/OR/AIF | No |
| 0x2E | I2C2RXIF | Yes |
| 0x32 | U2RXIF | Yes |
| 0x33 | U2TXIF | Yes |
| 0x36 | TMR3IF | No |
| 0x46 | TMR5IF | No |
| 0x48 | TMR6IF | No |

"Level-triggered" sources remain asserted while condition is true (e.g., UART RX buffer
has data). "Edge-triggered" sources fire once per event (e.g., timer overflow). The DMA
samples the selected interrupt flag every instruction cycle.

## Setup Procedure

1. Program source address (DMAxSSA) and memory region (SMR bits in DMAxCON1)
2. Program destination address (DMAxDSA) — always GPR/SFR space
3. Set addressing modes: SMODE/DMODE in DMAxCON1
4. Set message sizes: DMAxSSZ (source), DMAxDSZ (dest) — recommend multiples of each other
5. Configure stop behavior: SSTP/DSTP in DMAxCON1 if auto-stop desired
6. Set HW triggers if needed: DMAxSIRQ (start), DMAxAIRQ (abort)
7. Set priority & lock: Configure PR registers, then `PRLOCK=0x55; PRLOCK=0xAA; PRLOCKbits.PRLOCKED=1`
8. Enable DMA: Set EN bit in DMAxCON0
9. Arm/start: Set SIRQEN (HW trigger) or DGO (SW start) in DMAxCON0

## Power Modes & Reset

- **Sleep:** System clock disabled; no DMA operation. In-progress transfers resume on wake.
  Finish transfers before entering Sleep.
- **Idle:** All clocks running; every CPU cycle is a bubble. DMA works normally.
- **Doze:** CPU skips cycles; unused cycles available to DMA. **Errata: DMA may not work
  correctly in Doze mode on rev A1 silicon.**
- **PMD:** DMAxMD bit gates all clocks to the channel.
- **Reset:** All DMA registers reset to defaults. Clearing EN also resets all registers.

## DMA Mirror Registers

Some peripherals (ADC, PWM, timers, UART, CLC, IOC) have DMA-only mirror registers at
0x4000–0x40FF. Use these mirror addresses instead of normal SFR addresses when DMA accesses
them. Refer to Table 4-3 in the datasheet for the full mirror register map.

## K42-Specific Errata

| # | Issue | Revisions | Workaround |
|---|-------|-----------|------------|
| 2.1 | DMA reads from Data EEPROM (SMR=1x) write 0x00 to destination instead of EEPROM data | A1 | Use NVMCON reads or CPU-mediated EEPROM read |
| 2.2 | DMA transfers may not work correctly in Doze mode | A1 | Avoid Doze mode when using DMA |

## Gotchas

- **Two independent channels:** DMA1 and DMA2 have separate register sets (not overlaid
  like the Q41 family). A DMA channel must not read/write its own registers or another DMA's
  arbitration registers.
- **SMODE/DMODE=11 is reserved:** Do not use.
- **XIP hazard:** Clearing DGO after source read but before dest write loses buffered data.
- **Counter read quirk:** DMAxSCNT/DMAxDCNT never read zero; reload from size register
  immediately on decrement from 1.
- **Abort behavior:** Clears DGO (soft-stop), SIRQEN, and AIRQEN. No state lost; resume
  by re-enabling SIRQEN/AIRQEN and DGO.
- **Destination is GPR/SFR only:** No SMR equivalent for destination — it always targets
  the data memory space.
- **PRLOCK sequence mandatory:** Must lock priorities after configuration.