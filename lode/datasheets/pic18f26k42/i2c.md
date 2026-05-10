# PIC18F26K42 — I2C Module

## Overview

Two independent I2C modules: **I2C1** and **I2C2**. Each supports Host, Client, and
Multi-Host modes with 7-bit and 10-bit addressing. SDA and SCL are open-drain
bidirectional lines requiring external pull-ups.

## Mode Selection (I2CxCON0 MODE[2:0])

| MODE[2:0] | Mode |
|-----------|------|
| 000 | Client, four 7-bit addresses |
| 001 | Client, two 7-bit addresses with masking |
| 010 | Client, two 10-bit addresses |
| 011 | Client, one 10-bit address with masking |
| 100 | Host, 7-bit address |
| 101 | Host, 10-bit address |
| 110 | Multi-Host (SMBus 2.0), 7-bit client + 7-bit host |
| 111 | Multi-Host (SMBus 2.0), 7-bit client w/mask + 7-bit host |

Enable the module with I2CxCON0.EN = 1. SDA/SCL must be open-drain (clear TRIS,
set ODCON). Both PPS input and output must select the same pin.

## Registers (replace x with 1 or 2)

| Register | Description |
|----------|-------------|
| I2CxCON0 | Control 0: EN, RSEN, S, CSTR, MDR, MODE[2:0] |
| I2CxCON1 | Control 1: ACKCNT, ACKDT, ACKSTAT, ACKT, RXO, TXU, CSD |
| I2CxCON2 | Control 2: ACNT, GCEN, FME, ADB, SDAHT[1:0], BFRET[1:0] |
| I2CxCLK | Clock source selection: CLK[3:0] |
| I2CxBTO | Bus timeout source: BTO[2:0] |
| I2CxSTAT0 | Status 0: BFRE, SMA, MMA, R, D |
| I2CxSTAT1 | Status 1: TXWE, TXBE, RXRE, CLRBF, RXBF |
| I2CxERR | Error: BTOIF, BCLIF, NACKIF, BTOIE, BCLIE, NACKIE |
| I2CxPIR | Interrupt flags: CNTIF, ACKTIF, WRIF, ADRIF, PCIF, RSCIF, SCIF |
| I2CxPIE | Interrupt/hold enables: CNTIE, ACKTIE, WRIE, ADRIE, PCIE, RSCIE, SCIE |
| I2CxCNT | Byte count: CNT[7:0] |
| I2CxADR0 | Client address 0 |
| I2CxADR1 | Client address 1 / 10-bit high address |
| I2CxADR2 | Client address 2 / 10-bit low address / mask |
| I2CxADR3 | Client address 3 / 10-bit high mask |
| I2CxADB0 | Address data buffer 0 |
| I2CxADB1 | Address data buffer 1 |
| I2CxTXB | Transmit buffer (write-only) |
| I2CxRXB | Receive buffer (read-only) |

### I2CxCON0 — Control Register 0 (reset 0x00)

| Bit | Name | Description |
|-----|------|-------------|
| 7 | EN | Module enable (1=enabled) |
| 6 | RSEN | Restart enable (host: 1=restart instead of stop when CNT=0) |
| 5 | S | Start/Restart bit (set by software or TXB write; cleared by HW) |
| 4 | CSTR | Clock stretch (1=SCL held low; cleared by software or buffer ops) |
| 3 | MDR | Host data request (host pauses, 1=SCL held low) |
| 2:0 | MODE[2:0] | Mode select (see table above) |

### I2CxCON1 — Control Register 1 (reset 0x04)

| Bit | Name | Description |
|-----|------|-------------|
| 7 | ACKCNT | ACK sent when I2CxCNT=0 (1=NACK, 0=ACK) |
| 6 | ACKDT | ACK sent when I2CxCNT!=0 (1=NACK, 0=ACK) |
| 5 | ACKSTAT | ACK status (1=NACK received, 0=ACK received) |
| 4 | ACKT | ACK time (1=in ACK sequence, 8th SCL falling edge) |
| 3 | — | Unimplemented |
| 2 | RXO | Receive overflow (SMA=1 & data clocked when RXBF=1) |
| 1 | TXU | Transmit underflow (SMA=1 & clocked out when TXBE=1) |
| 0 | CSD | Clock stretch disable (1=never; 0=enabled) |

RXO/TXU only set when CSD=1. Both force NACK until cleared.

### I2CxCON2 — Control Register 2 (reset 0x00)

| Bit | Name | Description |
|-----|------|-------------|
| 7 | ACNT | Auto-load CNT from first data byte after address |
| 6 | GCEN | General call enable (address 0x00 triggers match) |
| 5 | FME | Fast mode (1=SCL sampled once; FSCL=FI2CXCLK/4; 0=sampled twice, /5) |
| 4 | ADB | Address buffer disable (1=address via RXB/TXB; 0=via ADB0/1) |
| 3:2 | SDAHT[1:0] | SDA hold time: 00=300ns, 01=100ns, 10=30ns, 11=reserved |
| 1:0 | BFRET[1:0] | Bus free time: 00=8, 01=16, 10=32, 11=64 I2C clock pulses |

### I2CxSTAT0 — Status Register 0 (reset 0x00)

| Bit | Name | Description |
|-----|------|-------------|
| 7 | BFRE | Bus free (1=idle; requires valid I2CxCLK source) |
| 6 | SMA | Client active (1=addressed as client) |
| 5 | MMA | Host active (1=host state machine active) |
| 4 | R | Read info (1=last match was read request) |
| 3 | D | Data (1=last byte was data; 0=address) |

### I2CxERR — Error Register (reset 0x00)

| Bit | Name | Description |
|-----|------|-------------|
| 6 | BTOIF | Bus timeout flag (HW set; SW clear) |
| 5 | BCLIF | Bus collision flag (SW clear) |
| 4 | NACKIF | NACK detect flag (also set on TXWE/RXRE/TXU/RXO errors) |
| 2 | BTOIE | Bus timeout interrupt enable |
| 1 | BCLIE | Bus collision interrupt enable |
| 0 | NACKIE | NACK detect interrupt enable |

Enabled error flags are OR'd to produce PIRx.I2CxEIF.

## Clock Source Selection (I2CxCLK)

| CLK[3:0] | Source |
|----------|--------|
| 0000 | FOSC/4 |
| 0001 | FOSC |
| 0010 | HFINTOSC |
| 0011 | MFINTOSC (500 kHz) |
| 0100 | Clock Reference output |
| 0101 | TMR0 overflow |
| 0110 | TMR2 postscaled output |
| 0111 | TMR4 postscaled output |
| 1000 | TMR6 postscaled output |
| 1001 | SMT1 overflow |
| 1010–1111 | Reserved |

BFRE requires a valid clock source to function. FME selects between /4 and /5 divider.

## Bus Timeout (I2CxBTO)

| BTO[2:0] | Source |
|-----------|--------|
| 000 | Reserved (disabled) |
| 001 | TMR2 postscaled output |
| 010 | TMR4 postscaled output |
| 011 | TMR6 postscaled output |
| 100 | CLC1OUT |
| 101 | CLC2OUT |
| 110 | CLC3OUT |
| 111 | CLC4OUT |

When the selected timeout source goes high, the I2C module resets. In client mode with
SMA=1, the module resets immediately and sets BTOIF. In host mode with MMA=1, the
module attempts a Stop condition then clears MMA and sets BTOIF.

## Addressing Modes

### 7-bit Client Addressing (MODE=000/001/110/111)
- MODE=000: Four independent 7-bit addresses in ADR0–ADR3; LSb of received byte
  ignored during comparison
- MODE=001: ADR1 acts as mask for ADR0; ADR3 acts as mask for ADR2
- All seven address bits can be masked

### 10-bit Client Addressing (MODE=010/011)
- MODE=010: Two 10-bit addresses from ADR0/ADR1 and ADR2/ADR3
- MODE=011: One 10-bit address (ADR0/ADR1) with mask (ADR2/ADR3)
- High byte format: 11110A9A8 (all 7 bits compared, not just upper 5)
- SMA set only after both high and low address bytes match
- Read requires Restart with high address byte R/W=1

### Host Addressing
- MODE=100 (7-bit): Address in I2CxADB1[7:1], R/W in I2CxADB1[0] (ABD=0);
  or address byte in I2CxTXB (ABD=1)
- MODE=101 (10-bit): High address in I2CxADB1, low in I2CxADB0 (ABD=0);
  or through I2CxTXB (ABD=1). Read requires Restart.

### General Call
- Enable via GCEN bit (7-bit modes only); address 0x00 triggers match regardless of ADR registers

## Client Clock Stretching

Disabled by setting CSD=1. When CSD=0, stretching occurs on:

| Condition | Stretch Point | Release Action |
|-----------|--------------|----------------|
| RXBF=1 & SMA=1 | 7th SCL falling edge | Read I2CxRXB |
| TXBE=1 & CNT!=0 & SMA=1 | 8th SCL falling edge | Write I2CxTXB |
| ADRIE=1 & address match | 8th SCL falling edge | Clear CSTR |
| WRIE=1 & data received | 8th SCL falling edge | Clear CSTR |
| ACKTIE=1 (any ACK) | 9th SCL falling edge | Clear CSTR |

CSTR can be set by multiple sources simultaneously; all must be resolved before SCL releases.

## Host Operation Quick Reference

1. Load I2CxCNT with byte count
2. Load address (I2CxADB0/1 if ABD=0, or I2CxTXB if ABD=1)
3. Set S bit (or write TXB if ABD=1) — waits for BFRE=1
4. Host sets MMA, SCIF set
5. Address shifted out, ACK received → ACKSTAT updated
6. If NACK: Stop sent (or MDR set if RSEN=1)
7. If ACK: data transfer proceeds, I2CxCNT decrements
8. I2CxCNT=0 → CNTIF set, Stop (or Restart if RSEN=1)

For host receive: set ACKDT=0 (ACK during transfer), ACKCNT=1 (NACK at end).

## Interrupt Flags (I2CxPIR) and Enables (I2CxPIE)

| Bit | Flag | Set Condition | Enable | Effect when enabled |
|-----|------|--------------|--------|---------------------|
| 7 | CNTIF | I2CxCNT=0 at 9th SCL falling edge | CNTIE | — |
| 6 | ACKTIF | 9th SCL falling edge (client addressed) | ACKTIE | CSTR set on ACK |
| 4 | WRIF | 8th SCL falling edge of data byte | WRIE | CSTR set after data |
| 3 | ADRIF | 8th SCL falling edge of matching address | ADRIE | CSTR set after address |
| 2 | PCIF | Stop condition detected | PCIE | — |
| 1 | RSCIF | Restart condition detected | RSCIE | — |
| 0 | SCIF | Start condition detected | SCIE | — |

All enabled PIR flags OR'd → PIRx.I2CxIF (generic interrupt).
All enabled ERR flags OR'd → PIRx.I2CxEIF (error interrupt).

Interrupt vector numbers: I2C1=25, I2C1E=26, I2C1RX=23, I2C1TX=24; I2C2=48,
I2C2E=49, I2C2RX=46, I2C2TX=47.

## Byte Count (I2CxCNT)

- Decrements on 8th SCL edge (RX) or 9th SCL edge (TX)
- Cannot decrement past zero
- CNTIF set at 9th falling SCL edge when CNT reaches 0
- If ACNT=1, first data byte after address auto-loads into CNT
- Write CNT only when module Idle (MMA=0, SMA=0) or during clock stretch

## Data Buffers

- **I2CxTXB**: Write transmit data; TXBE=1 when empty. Write when TXBE=0 → TXWE error.
- **I2CxRXB**: Read received data; RXBF=1 when full. Read when RXBF=0 → RXRE error.
- **CLRBF** (I2CxSTAT1 bit 2): Write-1-only; clears both buffers and RXBF/TXBE flags,
  also clears I2CxRXIF and I2CxTXIF.

## PPS Bidirectional Pin Handling

I2C SCL/SDA are bidirectional — **input and output PPS must select the same pin**.

| Instance | Default Pin | RxyPPS Output Value | xxxPPS Input Register |
|----------|-------------|--------------------|-----------------------|
| I2C1 SCL | RC3 | 0x21 | I2C1SCLPPS (default RC3=0x13) |
| I2C1 SDA | RC4 | 0x22 | I2C1SDAPPS (default RC4=0x14) |
| I2C2 SCL | RB1 | 0x23 | I2C2SCLPPS (default RB1=0x09) |
| I2C2 SDA | RB2 | 0x24 | I2C2SDAPPS (default RB2=0x0A) |

### PPS Configuration Steps (per I2Cx instance)

1. Clear ANSEL for both pins (digital mode)
2. Clear TRIS for both pins (output enable; I2C overrides when active)
3. Set ODCON for both pins (open-drain)
4. Write RxyPPS for SCL pin → output value (e.g. 0x21 for I2C1 SCL)
5. Write RxyPPS for SDA pin → output value (e.g. 0x22 for I2C1 SDA)
6. Write I2CxSCLPPS → input pin code (e.g. 0x13 for RC3)
7. Write I2CxSDAPPS → input pin code (e.g. 0x14 for RC4)
8. Optionally configure RxyI2C registers for input threshold/slew-rate
9. Enable module: I2CxCON0.EN = 1

Do NOT set TRIS=1 for I2C pins; I2C hardware overrides TRIS when driving the bus.