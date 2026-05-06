# PIC18F16Q41 DMA Module

## Overview
4-channel DMA controller transfers data between memory regions without CPU intervention.
Each byte transfer is a 2-cycle operation (read into DMAnBUF, then write to destination).
All 4 channels share one register set — only one channel is accessible at a time via DMASELECT.

**Memory access:**
- Read: GPR/SFR, Program Flash (PFM), Data EEPROM
- Write: GPR/SFR only (no write to PFM or EEPROM)

**Bus arbitration:** DMA shares the instruction/data bus with the CPU. Priority is configurable
per channel via DMAxPR registers (0x00B6–0x00B9). When DMA priority > CPU, DMA stalls the CPU
until transfer completes. When CPU priority > DMA, DMA uses "bubble" cycles (unused CPU slots).

## Register Map (shared, channel selected by DMASELECT)

| Addr   | Register  | Description                          |
|--------|-----------|--------------------------------------|
| 0x00E8 | DMASELECT | Channel select: SLCT = n selects DMA n+1 |
| 0x00E9 | DMAnBUF   | Data buffer (read-only)              |
| 0x00EA | DMAnDCNT  | Dest count [11:0] (DCNTL/DCNTH)      |
| 0x00EC | DMAnDPTR  | Dest pointer [15:0] (DPTRL/DPTRH, read-only) |
| 0x00EE | DMAnDSZ   | Dest message size [11:0] (DSZL/DSZH)  |
| 0x00F0 | DMAnDSA   | Dest start address [15:0] (DSAL/DSAH) |
| 0x00F2 | DMAnSCNT  | Source count [11:0] (SCNTL/SCNTH)    |
| 0x00F4 | DMAnSPTR  | Source pointer [21:0] (SPTRL/SPTRH/SPTRU, read-only) |
| 0x00F7 | DMAnSSZ   | Source message size [11:0] (SSZL/SSZH) |
| 0x00F9 | DMAnSSA   | Source start address [21:0] (SSAL/SSAH/SSAU) |
| 0x00FC | DMAnCON0  | Control register 0                   |
| 0x00FD | DMAnCON1  | Control register 1                   |
| 0x00FE | DMAnAIRQ  | Abort IRQ source select              |
| 0x00FF | DMAnSIRQ  | Start IRQ source select              |

Priority regs: DMA1PR=0x00B6, DMA2PR=0x00B7, DMA3PR=0x00B8, DMA4PR=0x00B9

## Key Bit Fields

### DMAnCON0 (0x00FC)
| Bit | Name    | Access | Function                                        |
|-----|---------|--------|-------------------------------------------------|
| 7   | EN      | R/W    | Module enable                                    |
| 6   | SIRQEN  | R/W/HC | Enable hardware start triggers; cleared by abort/stop |
| 5   | DGO     | R/W/HS/HC | Transfer in progress; set SW or HW, clear on stop |
| 2   | AIRQEN  | R/W/HC | Enable hardware abort triggers; auto-cleared on abort |
| 0   | XIP     | R/HS/HC | 1 = data in buffer not yet written to dest       |

### DMAnCON1 (0x00FD)
| Bits | Name  | Function                                              |
|------|-------|-------------------------------------------------------|
| 7:6  | DMODE | Dest addr mode: 00=fixed, 01=increment, 10=decrement  |
| 5    | DSTP  | 1 = clear SIRQEN when dest counter reloads             |
| 4:3  | SMR   | Source memory region: 00=GPR/SFR, 01=PFM, 1x=EEPROM   |
| 2:1  | SMODE | Source addr mode: 00=fixed, 01=increment, 10=decrement|
| 0    | SSTP  | 1 = clear SIRQEN when source counter reloads          |

### DMAnSIRQ (0x00FF) / DMAnAIRQ (0x00FE)
8-bit value selects interrupt source. Key mappings:
- 0x0A = ADC, 0x14–0x17 = DMA1 interrupts, 0x18 = SPI1RX, 0x20 = U1RX, 0x21 = U1TX,
- 0x1B = TMR2, 0x1C = TMR1, 0x24 = TMR3, 0x34–0x37 = DMA2, 0x4C–0x4F = DMA3,
- 0x54–0x57 = DMA4, 0x40 = U2RX, 0x48 = U3RX

## Setup Procedure
1. **Select channel:** `DMASELECT = n;` (n = channel-1)
2. **Set source address:** Write DMAnSSAU/SSAH/SSAL (22-bit address)
3. **Set source memory region:** Configure SMR bits in DMAnCON1
4. **Set dest address:** Write DMAnDSAH/DSAL (16-bit address; always GPR/SFR space)
5. **Set addressing modes:** SMODE/DMODE in DMAnCON1 (fixed/incr/decr)
6. **Set message sizes:** DMAnSSZ (source bytes), DMAnDSZ (dest bytes) — recommend multiples of each other
7. **Configure stop behavior:** Set SSTP/DSTP in DMAnCON1 if auto-stop on counter reload desired
8. **Set triggers (if HW):** Write DMAnSIRQ for start source, DMAnAIRQ for abort source
9. **Set priority & lock:** Write DMAxPR, then `PRLOCK=0x55; PRLOCK=0xAA; PRLOCKbits.PRLOCKED=1;`
10. **Enable:** Set EN bit in DMAnCON0
11. **ARM/start:** Set SIRQEN (HW trigger) or DGO (SW start) in DMAnCON0

## Channel Priority & Arbitration
- Each DMA channel has a DMAxPR register (3-bit priority level, shared system arbiter scheme)
- Higher-priority DMA stalls lower-priority DMA and/or CPU
- **PRLOCK sequence is mandatory** for DMA operation: write 0x55, 0xAA, then set PRLOCKED
- Priority must be locked after configuration; changing priority requires unlock

## Transfer Mechanics
- **One byte per transaction** (read source → DMAnBUF → write dest), takes 2 instruction cycles
- Message = 1+ transactions; SSZ/DSZ define message length; SCNT/DCNT are runtime counters
- When a counter decrements from 1, it reloads from corresponding size register and the pointer
  reloads from the start address (SCNT→SSZ/SPTR→SSA, DCNT→DSZ/DPTR→DSA)
- **SCNT/DCNT never read as zero** — reloaded from size register immediately on decrement from 1
- If SSZ != DSZ, the ratio determines how many messages per process; uneven ratios cause skew
- Common patterns: 1:N (SFR→RAM buffer), N:1 (RAM→SFR), N:N (block copy), 1:1 (bridge)

## Interrupts (via PIR registers / VIC)
| Flag          | Condition                                  |
|---------------|-------------------------------------------|
| DMAxSCNTIF    | Source counter reloaded (message complete) |
| DMAxDCNTIF    | Dest counter reloaded (message complete)   |
| DMAxAIF       | Abort trigger received (soft-stop)         |
| DMAxORIF      | New trigger received while DGO still set (edge triggers only) |

## Gotchas & Constraints
- **Register overlay:** All 4 channels share one register set. Writing DMASELECT switches which
  channel the registers control. Must not access arbitration registers (DMAxPR, etc.) via DMA.
- **DMA mirror SFRs:** Some peripherals (ADC, PWM, timers, UART, CLC, IOC) have DMA-only mirror
  registers at 0x4000–0x41FF. Use these instead of normal SFR addresses when DMA accesses them.
- **No DMA in Sleep:** System clock disabled; in-progress transfers resume on wake. Finish
  transfers before entering Sleep.
- **Idle/Doze:** DMA works normally (all CPU cycles become bubbles).
- **Hard stop (EN=0):** Resets all DMA state; cannot resume. Soft stop (DGO=0): resumes on
  next DGO set.
- **Stop latency:** One extra instruction cycle after stop condition before it takes effect —
  one more read or write may still occur.
- **XIP hazard:** If DGO is cleared after source read but before dest write, buffered data is
  lost (never written to destination).
- **Abort behavior:** Clears DGO (soft-stop), clears SIRQEN and AIRQEN. No state lost; can
  resume by re-setting DGO and SIRQEN.
- **Overrun only for edge triggers:** Level-triggered sources (e.g. UART TX) cannot generate
  overrun interrupts because they remain asserted.
- **Counter read quirk:** DMAnSCNT/DMAnDCNT will never read zero; value 1 reloads immediately.
- **SMODE/DMODE=11 is reserved:** Do not use.
- **PMD disable:** DMAxMD bit gates all clocks to the channel.