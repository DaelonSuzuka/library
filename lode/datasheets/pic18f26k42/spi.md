# PIC18F26K42 SPI Peripheral (Lode)

Single SPI module (SPI1) with 2-deep TX and RX FIFOs and DMA bus connections.

## Register Map (SPI1)

| Register    | Addr     | Description |
|-------------|----------|-------------|
| SPI1RXB     | 0x3D10   | RX FIFO read port (RO) |
| SPI1TXB     | 0x3D11   | TX FIFO write port (WO) |
| SPI1TCNTL   | 0x3D12   | Transfer counter low byte |
| SPI1TCNTH   | 0x3D13   | Transfer counter high byte (TCNT[10:8]) |
| SPI1CON0    | 0x3D14   | Control 0 — EN, LSBF, MST, BMODE |
| SPI1CON1    | 0x3D15   | Control 1 — SMP, CKE, CKP, FST, SSP, SDIP, SDOP |
| SPI1CON2    | 0x3D16   | Control 2 — BUSY, SSFLT, SSET, TXR, RXR |
| SPI1STATUS  | 0x3D17   | Status — TXWE, TXBE, RXRE, CLRBF, RXBF |
| SPI1TWIDTH  | 0x3D18   | Transfer width (TWIDTH[2:0]) |
| SPI1BAUD    | 0x3D19   | Baud rate divisor BAUD[7:0] |
| SPI1INTF    | 0x3D1A   | Interrupt flags |
| SPI1INTE    | 0x3D1B   | Interrupt enables |
| SPI1CLK     | 0x3D1C   | Clock source select CLKSEL[3:0] |

## PPS Registers

| Register    | Addr  | Purpose |
|-------------|-------|---------|
| SPI1SCKPPS  | 0x3ADE | SCK input pin selection |
| SPI1SDIPPS  | 0x3ADF | SDI input pin selection |
| SPI1SSPPS   | 0x3AE0 | SS input pin selection |

PPS output values: SCK=0b011110, SDO=0b011111, SS=0b100000.

## Key Bit Fields

### SPI1CON0 (0x3D14)
| Bit | Field | Description |
|-----|-------|-------------|
| 7   | EN    | SPI enable (1=enabled). Clear to reconfigure. |
| 2   | LSBF  | 0=MSb first, 1=LSb first |
| 1   | MST   | 0=Client, 1=Host |
| 0   | BMODE | 0=total-bit-count mode, 1=variable-transfer-size mode |

### SPI1CON1 (0x3D15)
| Bit | Field | Description |
|-----|-------|-------------|
| 7   | SMP   | Host: 0=mid-sample, 1=end-sample. Client: reserved when 1 |
| 6   | CKE   | 0=data changes Idle→Active edge, 1=Active→Idle edge |
| 5   | CKP   | 0=SCK idle low, 1=SCK idle high |
| 4   | FST   | Host: 1=remove ½-baud startup delay on SCK |
| 2   | SSP   | 0=SS active-high, 1=SS active-low |
| 1   | SDIP  | 0=SDI active-high, 1=SDI active-low |
| 0   | SDOP  | 0=SDO active-high, 1=SDO active-low |

### SPI1CON2 (0x3D16)
| Bit | Field | Description |
|-----|-------|-------------|
| 7   | BUSY  | RO — transfer in progress (up to 2-cycle sync delay) |
| 6   | SSFLT | RO — SS fault detected (client mode) |
| 2   | SSET   | Host: force SS_out active. Client: ignore SS_in |
| 1   | TXR    | 1=TX FIFO data required for transfer |
| 0   | RXR    | 1=RX FIFO space required to continue transfer |

### SPI1STATUS (0x3D17)
| Bit | Field | Access | Description |
|-----|-------|--------|-------------|
| 7   | TXWE  | R/C/HS | TX FIFO write error (wrote when full) |
| 5   | TXBE  | RO     | TX FIFO empty |
| 3   | RXRE  | R/C/HS | RX FIFO read error (read when empty) |
| 2   | CLB   | S      | Set to clear both FIFOs |
| 0   | RXBF  | RO     | RX FIFO full |

### SPI1INTF / SPI1INTE (0x3D1A–0x3D1B)
| Bit | Flag   | Enable | Description |
|-----|--------|--------|-------------|
| 7   | SRMTIF | SRMTIE | Shift register empty (Host only) |
| 6   | TCZIF  | TCZIE  | Transfer counter reached zero |
| 5   | SOSIF  | SOSIE  | Start of client select |
| 4   | EOSIF  | EOSIE  | End of client select |
| 2   | RXOIF  | RXOIE  | RX FIFO overflow (client only) |
| 1   | TXUIF  | TXUIE  | TX FIFO underflow (client only) |

### SPI1CLK (0x3D1C): CLKSEL[3:0]
| Value | Source | Value | Source |
|-------|--------|-------|--------|
| 0x0   | FOSC   | 0x5   | TMR0_overflow |
| 0x1   | HFINTOSC | 0x6 | TMR2_Postscaled |
| 0x2   | MFINTOSC | 0x7  | TMR4_Postscaled |
| 0x3   | CLKREF | 0x8   | TMR6_Postscaled |
| 0x4   | Reserved | 0x9-0xF | Reserved |
|       |         | 0x8   | SMT_match |

## Operating Modes

### Host/Client Selection (MST bit)
- **MST=1 Host**: Drives SCK, initiates transfers. Clock from SPI1BAUD/SPI1CLK.
- **MST=0 Client**: SCK is input, SS input gates transfers.

### TXR/RXR Mode Combinations (Host)

| TXR | RXR | Mode | Behavior |
|-----|-----|------|----------|
| 1 | 1 | Full Duplex | TX when RX FIFO not full and TX FIFO not empty (or TCNT≠0 if BMODE=0) |
| 0 | 1 | Receive Only | Clocks when RX FIFO not full and TCNT≠0. Re-sends last RX data if TX FIFO empty |
| 1 | 0 | Transmit Only | TX when TX FIFO not empty (or TCNT≠0 if BMODE=0). RX data discarded |
| 0 | 0 | Transfer Off | No SCK, no data exchange. TX writes buffered for later |

### Clock Polarity/Phase (CKP, CKE, SMP)
- **CKP**: SCK idle state (0=low, 1=high)
- **CKE**: Data output edge (0=Idle→Active, 1=Active→Idle)
- **SMP** (Host only): SDI sample point (0=mid-Output, 1=end-of-Output)

### Bit Order (LSBF)
- 0=MSb first (default, traditional SPI), 1=LSb first

## Transfer Counter (SPI1TCNT + SPI1TWIDTH)

- **BMODE=0 (total bit count)**: Total bits = TWIDTH[2:0] + TCNT×8. TWIDTH is remainder bits
  for final byte. TCNT must be nonzero for host transfers. Transfer stops at TCNT=0.
- **BMODE=1 (variable transfer size)**: TWIDTH = bits per transfer (0→8 bits). TCNT = number
  of transfers. Only stops transfers in Receive-Only mode (TCNT=0). TCNT can roll below zero.
- **Host Receive-Only**: Writing TCNTL starts transfer clocks. Clocks suspend when RX FIFO full.
- **Host Transmit/Full-Duplex** (BMODE=0): Writing TXB or TCNTL (whichever last) starts transfer.
- **Client mode**: TCNT decrements but doesn't control data; used for SS fault detection.

## FIFO Operation

- **TX FIFO**: 2-deep, write-only via SPI1TXB. TXBE=1 when empty. TXWE set on overflow write.
- **RX FIFO**: 2-deep, read-only via SPI1RXB. RXBF=1 when full. RXRE set on empty read.
- Read from empty RXB returns 0 and sets RXRE. Write to full TXB does nothing and sets TXWE.
- Set CLB bit (SPI1STATUS<2>) to clear both FIFOs. Also cleared when EN=0.

## Client Select (SS)

### Host mode SS_out control
- **SSET=0**: SS_out asserted while TCNT≠0; auto-deassert after final SCK pulse.
- **SSET=1**: SS_out forced active continuously.
- SS polarity: SSP bit (1=active-low, 0=active-high).
- SS(out) and SCK(out) require TRIS=0 on their PPS output pins.

### Client mode SS_in
- SS gates transfers; SCK ignored when SS inactive.
- SSET=1: ignores SS_in, acts as if SS always active.
- SSFLT set when SS goes inactive during an incomplete transfer.

## Baud Rate (Host only)

```
FBAUD = FCSEL / (2 × (BAUD + 1))
```
Where FCSEL is the clock source selected by SPI1CLK, BAUD is the SPI1BAUD value.

## Interrupts

Three top-level interrupt sources in PIR2/PIE2/IPR2:
1. **SPI1TXIF** (PIR2<5>): TX FIFO not full (read-only, DMA trigger)
2. **SPI1RXIF** (PIR2<4>): RX FIFO has data (read-only, DMA trigger)
3. **SPI1IF** (PIR2<6>): OR of enabled status flags in SPI1INTF/SPI1INTE

Status flags must be cleared in software. TCZIF only indicates count→0, not
transfer completion; use BUSY poll or SRMTIF for completion.

## DMA Support

DMA SIRQ trigger values: SPI1RX=0x14, SPI1TX=0x15, SPI1=0x16.

## Key Setup Steps (Host Full Duplex, 8-bit)

1. Configure PPS: map SCK (0x1E), SDO (0x1F) outputs; map SDI, SS inputs.
2. Set TRIS for SCK and SS outputs to 0; SDO TRIS=0 optional (always drives).
3. Set SPI1CLK to desired clock source.
4. Write SPI1BAUD for target baud rate.
5. Configure SPI1CON1: CKP, CKE, SMP, SSP, FST as needed.
6. Configure SPI1CON0: MST=1, BMODE=1, LSBF as needed.
7. Configure SPI1CON2: TXR=1, RXR=1.
8. Optionally write SPI1TCNT (required if BMODE=0).
9. Set SPI1CON0.EN=1 to enable.
10. Write data to SPI1TXB to begin transfer.
11. Read received data from SPI1RXB.

## Lock Rules
- Cannot modify SPI1BAUD, SPI1CON1, or SPI1CON0 (except EN) while EN=1.
- Cannot modify SPI1TCNT, SPI1TWIDTH, SPI1CON2, or CLB while BUSY=1.