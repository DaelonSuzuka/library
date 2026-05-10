# PIC18F27/47/57Q43 DMA Module

## Overview
4-channel DMA controller transfers data between memory regions without CPU intervention.
Each byte transfer is a 2-cycle operation (read into DMABUF, then write to destination).
All four DMA modules (DMA1-DMA4) share a single register set, selected by DMASELECT.

**Memory access:**
- Read: GPR/SFR, Program Flash Memory (PFM), Data EEPROM
- Write: GPR/SFR only (no write to PFM or EEPROM)

**Bus arbitration:** DMA shares the 16-bit instruction bus and 8-bit data bus with the CPU.
When DMA priority > CPU, DMA stalls the CPU until transfer completes. When CPU priority >
DMA, DMA uses "bubble" cycles (unused CPU slots). Priority is configurable via the system
arbiter (PR registers). Priority must be locked with the PRLOCK sequence after configuration.

## Register Map

All DMA registers are accessed via DMASELECT overlay (DMA1=0, DMA2=1, DMA3=2, DMA4=3):

| Register | Size | Description |
|----------|------|-------------|
| DMAnCON0 | 8 | Control register 0 (EN, SIRQEN, DGO, AIRQEN, XIP) |
| DMAnCON1 | 8 | Control register 1 (DMODE, DSTP, SMR, SMODE, SSTP) |
| DMAnBUF | 8 | Data buffer (read-only) |
| DMAnSSA | 22-bit | Source start address (SSAU:SSAH:SSAL) |
| DMAnSPTR | 22-bit | Source pointer (SPTRU:SPTRH:SPTRL, read-only, runtime) |
| DMAnSSZ | 12-bit | Source message size (SSZH:SSZL) |
| DMAnSCNT | 12-bit | Source count (SCNTH:SCNTL, read-only, runtime) |
| DMAnDSA | 16-bit | Destination start address (DSAH:DSAL) |
| DMAnDPTR | 16-bit | Destination pointer (DPTRH:DPTRL, read-only, runtime) |
| DMAnDSZ | 12-bit | Destination message size (DSZH:DSZL) |
| DMAnDCNT | 12-bit | Destination count (DCNTH:DCNTL, read-only, runtime) |
| DMAnSIRQ | 7-bit | Start interrupt request source select (SIRQ[6:0]) |
| DMAnAIRQ | 7-bit | Abort interrupt request source select (AIRQ[6:0]) |

Priority registers: DMA1PR, DMA2PR, DMA3PR, DMA4PR (system arbiter scheme).

### DMASELECT (0x0E8)

| Bit | Name | Description |
|-----|------|-------------|
| 2:0 | SLCT[2:0] | Selects DMA instance: 0=DMA1, 1=DMA2, 2=DMA3, 3=DMA4 |

## Key Bit Fields

### DMAnCON0 (0x0FC)
| Bit | Name | Access | Function |
|-----|------|--------|----------|
| 7 | EN | R/W | Module enable |
| 6 | SIRQEN | R/W/HC | Enable hardware start triggers; cleared by abort/stop |
| 5 | DGO | R/W/HS/HC | Transfer in progress; set by SW or HW, cleared on stop |
| 2 | AIRQEN | R/W/HC | Enable hardware abort triggers; auto-cleared on abort |
| 0 | XIP | R/HS/HC | 1 = data in buffer not yet written to destination |

### DMAnCON1 (0x0FD)
| Bits | Name | Function |
|------|------|----------|
| 7:6 | DMODE | Dest addr mode: 00=fixed, 01=increment, 10=decrement, 11=reserved |
| 5 | DSTP | 1 = clear SIRQEN when dest counter reloads |
| 4:3 | SMR | Source memory region: 00=GPR/SFR, 01=PFM, 1x=Data EEPROM |
| 2:1 | SMODE | Source addr mode: 00=fixed, 01=increment, 10=decrement, 11=reserved |
| 0 | SSTP | 1 = clear SIRQEN when source counter reloads |

## Addressing Modes

Source address: 22-bit (DMAnSSA/DMAnSPTR), supports GPR/SFR, PFM, or EEPROM via SMR bits.
Destination address: 16-bit (DMAnDSA/DMAnDPTR), always targets GPR/SFR space.

Each pointer updates after every transaction based on mode:
- 00 (Fixed): pointer unchanged (e.g., SFR register like U1TXB)
- 01 (Increment): pointer increments by 1 (e.g., RAM buffer fill)
- 10 (Decrement): pointer decrements by 1
- 11: Reserved, do not use

## Message Size / Counters

- Transaction = 1 byte transfer (read -> DMABUF -> write)
- Message = 1+ transactions; SSZ/DSZ define message length
- Process = 1+ messages (when SSZ != DSZ, ratio determines messages per process)
- On trigger, counters (SCNT/DCNT) load from size registers (SSZ/DSZ), pointers load from
  start addresses (SSA->SPTR, DSA->DPTR)
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
2. **Hardware trigger (SIRQ):** Set SIRQEN=1, select trigger via DMAnSIRQ. When the
   selected interrupt flag is set, DGO is set and transfer begins.

## Stopping Transfers

1. **Clear DGO:** Soft-stop. DMA pauses; setting DGO again resumes from where it left off.
   If source was read but not yet written (XIP=1), buffered data is lost.
2. **Hardware abort (AIRQ):** Set AIRQEN=1, select source via DMAnAIRQ. Clears DGO
   (soft-stop), SIRQEN, and AIRQEN. No state lost; can resume by re-enabling SIRQEN/AIRQEN and DGO.
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

## DMA Trigger Sources (DMAnSIRQ / DMAnAIRQ)

7-bit value selects interrupt source. Key mappings for Q43:

| Value | Source | Level? |
|-------|--------|--------|
| 0x00 | Reserved | — |
| 0x07 | IOCIF | Yes |
| 0x0A | ADIF | No |
| 0x0B | ADTIF | No |
| 0x0B | ACT (Active Clock Tuning) | No |
| 0x14 | SPI1RXIF | Yes |
| 0x15 | SPI1TXIF | Yes |
| 0x16 | SPI1IF | No |
| 0x18 | I2C1RXIF | Yes |
| 0x19 | I2C1TXIF | Yes |
| 0x1A | I2C1IF | No |
| 0x1B | U1RXIF | Yes |
| 0x1C | U1TXIF | Yes |
| 0x1E | CCP1 | No |
| 0x1F | TMR0IF | No |
| 0x20 | TMR1IF | No |
| 0x22 | TMR2IF | No |
| 0x28 | SPI2RXIF | Yes |
| 0x29 | SPI2TXIF | Yes |
| 0x2A | SPI2IF | No |
| 0x2C | TMR3IF | No |
| 0x34 | DMA1SCNT | No |
| 0x35 | DMA1DCNT | No |
| 0x36 | DMA1OR | No |
| 0x37 | DMA1A | No |
| 0x38 | I2C1RX | Yes |
| 0x39 | I2C1TX | Yes |
| 0x3A | I2C1 | No |
| 0x3B | I2C1E | No |
| 0x3D | CLC3 | No |
| 0x40 | U2RXIF | Yes |
| 0x41 | U2TXIF | Yes |
| 0x42 | U2EIF | No |
| 0x43 | U2IF | No |
| 0x54 | DMA3SCNT | No |
| 0x55 | DMA3DCNT | No |
| 0x56 | DMA3OR | No |
| 0x57 | DMA3A | No |
| 0x5C | DMA4SCNT | No |
| 0x5D | DMA4DCNT | No |
| 0x5E | DMA4OR | No |
| 0x5F | DMA4A | No |
| 0x64 | DMA5SCNT | No |
| 0x65 | DMA5DCNT | No |
| 0x66 | DMA5OR | No |
| 0x67 | DMA5A | No |
| 0x6C | DMA6SCNT | No |
| 0x6D | DMA6DCNT | No |
| 0x6E | DMA6OR | No |
| 0x6F | DMA6A | No |
| 0x78 | NVM | No |
| 0x7B | TMR6 | No |

"Level-triggered" sources remain asserted while condition is true (e.g., UART RX buffer has data).
"Edge-triggered" sources fire once per event (e.g., timer overflow). The DMA samples the
selected interrupt flag every instruction cycle.

## Setup Procedure

1. Select DMA channel: Write DMASELECT = n (0 for DMA1, 1 for DMA2, etc.)
2. Program source address (DMAnSSA) and memory region (SMR bits in DMAnCON1)
3. Program destination address (DMAnDSA) — always GPR/SFR space
4. Set addressing modes: SMODE/DMODE in DMAnCON1
5. Set message sizes: DMAnSSZ (source), DMAnDSZ (dest) — recommend multiples of each other
6. Configure stop behavior: SSTP/DSTP in DMAnCON1 if auto-stop desired
7. Set HW triggers if needed: DMAnSIRQ (start), DMAnAIRQ (abort)
8. Set priority & lock: Configure PR registers, then `PRLOCK=0x55; PRLOCK=0xAA; PRLOCKbits.PRLOCKED=1`
9. Enable DMA: Set EN bit in DMAnCON0
10. Arm/start: Set SIRQEN (HW trigger) or DGO (SW start) in DMAnCON0

## Power Modes & Reset

- **Sleep:** System clock disabled; no DMA operation. In-progress transfers resume on wake.
  Finish transfers before entering Sleep.
- **Idle:** All clocks running; every CPU cycle is a bubble. DMA works normally.
- **Doze:** CPU skips cycles; unused cycles available to DMA.
- **PMD:** DMAxMD bit gates all clocks to the channel.
- **Reset:** All DMA registers reset to defaults. Clearing EN also resets registers.

## DMA Mirror Registers

Some peripherals (ADC, PWM, timers, UART, CLC, IOC) have DMA-only mirror registers at
0x4000-0x40FF. Use these mirror addresses instead of normal SFR addresses when DMA accesses
them. The Q43 mirror register map includes entries for ADC1, ADC2, PWM, timer, CCPR, and
other peripherals across channels DMA1-DMA6.

## Key Differences from K42

- **4 channels** (DMA1-DMA4) selected via DMASELECT, vs 2 on K42 with separate register sets
- **6 mirror regions** in DMA-accessible SFR space (0x4000-0x40FF divided among DMA1-DMA6),
  vs 2 on K42 with separate register sets
- **Same DMASELECT overlay scheme** as K42, but SLCT is 3 bits (vs 1 bit on K42) to support 4+ channels
- DMA trigger table includes Q43-specific peripherals (SPI2, U2, ACT, CLC4-CLC8, etc.)

## Gotchas

- **SMODE/DMODE=11 is reserved:** Do not use.
- **XIP hazard:** Clearing DGO after source read but before dest write loses buffered data.
- **Counter read quirk:** DMAnSCNT/DMAnDCNT never read zero; reload from size register
  immediately on decrement from 1.
- **Abort behavior:** Clears DGO (soft-stop), SIRQEN, and AIRQEN. No state lost; resume
  by re-enabling SIRQEN/AIRQEN and DGO.
- **Destination is GPR/SFR only:** No SMR equivalent for destination — always data memory space.
- **PRLOCK sequence mandatory:** Must lock priorities after configuration.
- **Don't access DMA arbitration registers from a DMA channel:** A DMA must not read/write
  its own registers or another DMA's arbitration registers.