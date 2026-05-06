# PIC18F16Q41 - I2C Peripheral Reference

## Register Map (Instance 1)

| Addr    | Name      | Bit 7  | Bit 6  | Bit 5   | Bit 4  | Bit 3 | Bit 2  | Bit 1   | Bit 0   |
|---------|-----------|--------|--------|---------|--------|-------|--------|---------|---------|
| 0x028A  | I2C1RXB   | RXB[7:0] (read-only) |
| 0x028B  | I2C1TXB   | TXB[7:0] (write-only) |
| 0x028C  | I2C1CNTL  | CNT[7:0] |
| 0x028D  | I2C1CNTH  | CNT[15:8] |
| 0x028E  | I2C1ADB0  | ADB[7:0] |
| 0x028F  | I2C1ADB1  | ADB[7:0] |
| 0x0290  | I2C1ADR0  | ADR[7:0] |
| 0x0291  | I2C1ADR1  | — ADR[6:0] |
| 0x0292  | I2C1ADR2  | ADR[7:0] |
| 0x0293  | I2C1ADR3  | — ADR[6:0] |
| 0x0294  | I2C1CON0  | EN | RSEN | S | CSTR | MDR | MODE[2:0] |
| 0x0295  | I2C1CON1  | ACKCNT | ACKDT | ACKSTAT | ACKT | P | RXO | TXU | CSD |
| 0x0296  | I2C1CON2  | ACNT | GCEN | FME | ABD | SDAHT[1:0] | BFRET[1:0] |
| 0x0297  | I2C1ERR   | — | BTOIF | BCLIF | NACKIF | — | BTOIE | BLCIE | NACKIE |
| 0x0298  | I2C1STAT0 | BFRE | SMA | MMA | R | D | — | — | — |
| 0x0299  | I2C1STAT1 | TXWE | — | TXBE | — | RXRE | CLRBF | — | RXBF |
| 0x029A  | I2C1PIR   | CNTIF | ACKTIF | — | WRIF | ADRIF | PCIF | RSCIF | SCIF |
| 0x029B  | I2C1PIE   | CNTIE | ACKTIE | — | WRIE | ADRIE | PCIE | RSCIE | SCIE |
| 0x029C  | I2C1BTO   | TOREC | TOBY32 | TOTIME[5:0] |
| 0x029D  | I2C1BAUD  | BAUD[7:0] |
| 0x029E  | I2C1CLK   | CLK[3:0] |
| 0x029F  | I2C1BTOC  | BTOC[2:0] |

PPS input registers: I2C1SDAPPS (0x0270), I2C1SCLPPS (0x0271).

## I2C1CON0 — Control Register 0

| Bit | Name | Description |
|-----|------|-------------|
| 7 | EN | Module enable (1=enabled) |
| 6 | RSEN | Restart enable; when I2CxCNT=0: 1=stretch & wait for Restart, 0=auto-Stop |
| 5 | S | Start condition trigger (set by SW or TXB write; cleared by HW after Start/Restart) |
| 4 | CSTR | Client clock stretching status (1=SCL held low). Set/cleared by HW; SW must clear to release SCL |
| 3 | MDR | Host data request (1=host paused, waiting for read/write). HW-sets on 7th/8th/9th SCL falling edge |
| 2:0 | MODE | 000=Client 4×7-bit, 001=Client 2×7-bit w/mask, 010=Client 2×10-bit, 011=Client 1×10-bit w/mask, 100=Host 7-bit, 101=Host 10-bit, 11x=Multi-Host SMBus 2.0 |

## I2C1CON1 — Control Register 1

| Bit | Name | Description |
|-----|------|-------------|
| 7 | ACKCNT | ACK response when I2CxCNT=0: 0=ACK, 1=NACK |
| 6 | ACKDT | ACK response when I2CxCNT!=0: 0=ACK, 1=NACK |
| 5 | ACKSTAT | ACK status from last xfer: 0=ACK received, 1=NACK received (read-only) |
| 4 | ACKT | ACK time status: 1=in ACK sequence (8th falling SCL), 0=not (9th rising SCL) |
| 3 | P | Stop condition trigger; set by SW when MMA=1, cleared by HW after Stop |
| 2 | RXO | Receive overflow: set when SMA=1 and data received with RXBF=1 (causes NACK) |
| 1 | TXU | Transmit underflow: set when SMA=1 and shift register loads with TXBE=1 (causes NACK) |
| 0 | CSD | Clock stretch disable: 1=no clock stretching, 0=normal stretching |

## I2C1CON2 — Control Register 2

| Bit | Name | Description |
|-----|------|-------------|
| 7 | ACNT | Auto-load I2CxCNT enable; first byte after address loads into I2CxCNTL |
| 6 | GCEN | General call address enable (0x00 causes address match; Client/Multi-Host modes only) |
| 5 | FME | Fast mode enable: 1=FSCL = FPRECLK/4, 0=FSCL = FPRECLK/5 |
| 4 | ABD | Address buffer disable: 1=address routed through TXB/RXB, 0=address uses ADB0/ADB1 |
| 3:2 | SDAHT | SDA hold time: 00=300ns, 01=100ns, 10=30ns, 11=reserved |
| 1:0 | BFRET | Bus free time: 00=8 clk, 01=16 clk, 10=32 clk, 11=64 clk |

## I2C1STAT0 — Status Register 0

| Bit | Name | Description |
|-----|------|-------------|
| 7 | BFRE | Bus free: 1=SDA+SCL both high for BFRET periods |
| 6 | SMA | Client mode active; set on matching address, cleared on Stop/Restart/BTO/BCL |
| 5 | MMA | Host mode active; set on Start, cleared on Stop/BCL/BTO after Stop |
| 4 | R | Read info from last matching address: 1=read, 0=write |
| 3 | D | Data: 1=last byte was data, 0=last byte was address |

## I2C1STAT1 — Status Register 1

| Bit | Name | Description |
|-----|------|-------------|
| 7 | TXWE | TX write error: wrote to TXB while full (must clear by SW) |
| 5 | TXBE | TX buffer empty: 1=I2CxTXB empty (cleared by writing TXB) |
| 3 | RXRE | RX read error: read RXB while empty (must clear by SW) |
| 2 | CLRBF | Clear buffers: write 1 to clear TXB, RXB, TXBE→1, RXBF→0, clear TXIF/RXIF |
| 0 | RXBF | RX buffer full: 1=I2CxRXB has data (cleared by reading RXB) |

## I2C1PIR / I2C1PIE — Interrupt Flags / Enables

Flags (I2C1PIR): CNTIF, ACKTIF, WRIF, ADRIF, PCIF, RSCIF, SCIF
Enables (I2C1PIE): CNTIE, ACKTIE, WRIE, ADRIE, PCIE, RSCIE, SCIE

Key enables with stretch behavior (CSD must be 0):
- ADRIE=1: stretches clock after matching address, sets CSTR
- WRIE=1: stretches clock after data byte received, sets CSTR
- ACKTIE=1: stretches clock after ACK/NACK sequence (ACK only)

## I2C1ERR — Error Register

| Bit | Name | Description |
|-----|------|-------------|
| 6 | BTOIF | Bus time-out flag (must clear by SW; triggers I2CxEIF if BTOIE=1) |
| 5 | BCLIF | Bus collision flag (must clear by SW; resets module if set) |
| 4 | NACKIF | NACK detected (also auto-set by TXWE/RXRE/TXU/RXO errors) |
| 2 | BTOIE | Bus time-out interrupt enable |
| 1 | BLCIE | Bus collision interrupt enable |
| 0 | NACKIE | NACK detect interrupt enable |

## Mode Selection (I2C1CON0 MODE bits)

| MODE[2:0] | Mode |
|-----------|------|
| 000 | Client, four 7-bit addresses |
| 001 | Client, two 7-bit addresses with masking |
| 010 | Client, two 10-bit addresses |
| 011 | Client, one 10-bit address with masking |
| 100 | Host, 7-bit addressing |
| 101 | Host, 10-bit addressing |
| 110 | Multi-Host (SMBus 2.0) |
| 111 | Multi-Host (SMBus 2.0) |

## Host Mode Setup

**7-bit Host (ABD=0):** Configure PPS/ODCON/TRIS → set I2C1CLK → set BAUD → load ADB1 with addr+R/W, I2CxCNT, TXB → set MODE=100, EN=1 → set S bit.

**7-bit Host (ABD=1):** Same config → load I2CxCNT → write addr+R/W to TXB (auto-Starts; do NOT write S bit).

**10-bit Host (ABD=0):** ADB1 = high byte (11110:A9:A8:R/W), ADB0 = low byte (A7:A0), then set S bit.

**Clock formula:** fSCL = fI2CxCLK / (BAUD+1) / (FME?4:5). BFRET sets idle wait in I2C clock periods before Start.

## Client Mode Setup

Configure PPS/ODCON/TRIS → set MODE (000-011) → load ADR0-3 → CSD=0 (stretching recommended) → enable interrupts in PIE → ACKDT=0, ACKCNT=1 → EN=1.

**Address registers per mode:**

| Mode | ADR0 | ADR1 | ADR2 | ADR3 |
|------|------|------|------|------|
| 7-bit (000) | Addr0 | Addr1 | Addr2 | Addr3 |
| 7-bit mask (001) | Addr0 | Mask0 | Addr2 | Mask2 |
| 10-bit (010) | Low0 | High0 | Low1 | High1 |
| 10-bit mask (011) | Low0 | High0 | LowMask | HighMask |

## 7-Bit Addressing

Address byte: A[6:0]+R/W. ADR registers store 7-bit addresses (LSB don't-care). With ABD=0, matching address → ADB0; with ABD=1, → RXB (sets RXBF+RXIF). Masking mode (001): ADR1/ADR3 are masks where 0=don't-care.

## 10-Bit Addressing

High byte: `11110 A9 A8 R/W`, low byte: `A7:A0`. Client must receive both bytes to set SMA. Host read requires Restart: Start→high(R/W=0)→low→Restart→high(R/W=1)→data. No clock stretch after high address with R/W=0 (even if ADRIE=1).

## Clock Stretching

CSD=0 enables stretching; CSD=1 disables it (causes TXU/RXO if CPU slow). CSTR is set by HW for multiple reasons—ALL must be resolved before SW clears CSTR. Stretching conditions: RXBF on 7th SCL falling → read RXB; TXBE+I2CxCNT!=0 on 8th SCL falling → write TXB; ADRIE=1 on address match → clear ADRIF+CSTR; WRIE=1 on data write → clear WRIF+CSTR; ACKTIE=1 on ACK (not NACK) at 9th SCL falling → clear ACKTIF+CSTR.

## I2CxCNT — Byte Count Register

16-bit counter (CNTL+CNTH). Decremented by HW per byte; does NOT wrap below 0. CNTIF set at zero (9th falling SCL). When I2CxCNT=0, ACKCNT used for ACK/NACK; when nonzero, ACKDT used. ACNT (CON2): first byte after address auto-loads I2CxCNTL. Safe to write only when idle (MMA=0, SMA=0) or stretching (CSTR=1, MDR=1).

## Bus Time-Out (BTO)

BTOC selects clock source: 001=TMR2_postscaled, 010=TMR4_postscaled, 011=LFINTOSC(~1ms), 100=MFINTOSC(32kHz), 101=SOSC. BTO time = TOTIME × T_BTOCLK × (TOBY32?1:32). TOREC=1 resets module + sets BTOIF on timeout; TOREC=0 just sets BTOIF (SW must handle reset). **Recommend TOREC=1 for Client mode.** SMBus: 25ms client, 35ms host.

## DMA Integration

Trigger sources: I2CxTXIF (TX), I2CxRXIF (RX), I2CxIF (general), I2CxEIF (error). ABD=0: address via ADB0/ADB1; TXIF fires after address byte. ABD=1: address via TXB; TXIF fires after address transmitted. DMA stops when I2CxCNT reaches 0.

## Host Transmit Flow (7-bit, ABD=0)

```
Load ADB1=(addr<<1|RW), I2CxCNT=N, TXB=first byte
Set S bit → HW: Start → address → ACK check
On TXIF: load next byte into TXB
On I2CxCNT=0: auto-Stop (or Restart if RSEN=1)
```

## Host Receive Flow (7-bit, ABD=0)

```
Load ADB1=(addr<<1|1), I2CxCNT=N, ACKDT=0, ACKCNT=1
Set S bit → HW: Start → address → ACK → clock in data
On RXIF+RXBF: read RXB
On CNTIF: last byte NACKed, HW sends Stop
```

## Client Receive Flow (7-bit, ABD=0, ADRIE+WRIE)

```
MODE=000, CSD=0, ADRIE=1, WRIE=1, ACKDT=0, ACKCNT=1, ADR0-3 addrs, EN=1
On ADRIF: read ADB0 (matched addr), check R bit, clear ADRIF+CSTR
On WRIF: read RXB, set ACKDT, clear WRIF+CSTR
On CNTIF+ACKTIF: ACKCNT=1, clear ACKTIF+CSTR
On PCIF: done
```

## Client Transmit Flow (7-bit, ABD=0)

```
MODE=000, CSD=0, CNTIE=1, ACKTIE=1, ADR0-3 addrs, I2CxCNT=N, EN=1
On ADRIF (R=1): clear ADRIF+CSTR
On TXIF: load TXB with data
On NACK: SMA cleared, NACKIF set
On PCIF: done
```

## Key Gotchas

- **I2CxTXB is write-only;** reading returns 0x00. I2CxRXB is read-only; writes are ignored.
- **CLRBF only reads as 0;** writing 1 clears both buffers and TXIF/RXIF flags.
- **ACKCNT vs ACKDT:** ACKCNT is used when I2CxCNT=0 (last byte), ACKDT for all other bytes. Wrong ACKCNT leaves bus stuck—no Stop is generated if host sees ACK instead of NACK.
- **NACK auto-generation:** TXWE, RXRE, TXU, or RXO errors cause automatic NACK and set NACKIF. Clear the error bit before resuming.
- **Once NACK is detected, all subsequent ACK sequences are NACK until error conditions are cleared.**
- **CSTR can be set by multiple HW sources simultaneously** (address match, buffer full, buffer empty, ACKT). All must be resolved before clearing CSTR.
- **10-bit client mode:** ADRIE clock stretch does NOT occur after the high address byte with R/W=0. Only after low byte match or high byte with R/W=1.
- **I2CxCNT does not wrap below 0.** For transactions >65535 bytes, SW must reload I2CxCNT mid-transaction (safe only when idle or stretching).
- **I2CxTXIF only sets when SMA or MMA is active AND I2CxCNT!=0.** Pre-loading TXB before Start won't trigger TXIF.
- **I2CxIF is read-only;** cleared by HW only when all enabled PIR flags are cleared.
- **I2CxEIF is read-only;** cleared by HW only when all enabled ERR flags are cleared.
- **RSEN (Restart Enable):** When set and I2CxCNT reaches 0, HW stretches clock and waits for S bit instead of issuing Stop. Must set RSEN before I2CxCNT reaches 0.
- **TOBY32 inversion:** TOBY32=0 means time×32, TOBY32=1 means time×1. Confusing naming.
- **When ABD=1,** writing to TXB triggers an automatic Start—do NOT also write S bit.
- **Pins must be configured open-drain (ODCONx), TRIS cleared, AND PPS set for both input and output.**
- **RxyI2C registers** provide I2C-specific input thresholds, slew rate, and pull-ups only on default pins. For remapped pins, use INLVLx, SLRCONx, and external pull-ups instead.
- **SCL frequency (FME=0)** divides by 5 for clock verification; **FME=1** divides by 4 (fast mode+) but gives less setup/hold margin.
- **I2CxCLK note:** When HFINTOSC is selected, the OSCFRQ frequency is used directly; the NDIV clock divider is NOT applied.