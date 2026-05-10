# PIC18F27/47/57Q43 SPI Peripheral (Lode)

Two SPI instances (SPI1, SPI2) each with 2-deep TX and RX FIFOs and DMA bus connections.

## Register Map

| Register    | SPI1 Addr | SPI2 Addr | Description |
|-------------|----------|----------|-------------|
| SPIxRXB     | 0x080    | 0x08D    | RX FIFO read port (RO) |
| SPIxTXB     | 0x081    | 0x08E    | TX FIFO write port (WO) |
| SPIxTCNTL   | 0x082    | 0x08F    | Transfer counter low byte |
| SPIxTCNTH   | 0x083    | 0x090    | Transfer counter high byte (TCNT[10:8]) |
| SPIxCON0    | 0x084    | 0x091    | Control 0 — EN, LSBF, MST, BMODE |
| SPIxCON1    | 0x085    | 0x092    | Control 1 — SMP, CKE, CKP, FST, SSP, SDIP, SDOP |
| SPIxCON2    | 0x086    | 0x093    | Control 2 — BUSY, SSFLT, SSET, TXR, RXR |
| SPIxSTATUS  | 0x087    | 0x094    | Status — TXWE, TXBE, RXRE, CLB, RXBF |
| SPIxTWIDTH  | 0x088    | 0x095    | Transfer width (TWIDTH[2:0]) |
| SPIxBAUD    | 0x089    | 0x096    | Baud rate divisor BAUD[7:0] |
| SPIxINTF    | 0x08A    | 0x097    | Interrupt flags |
| SPIxINTE    | 0x08B    | 0x098    | Interrupt enables |
| SPIxCLK     | 0x08C    | 0x099    | Clock source select CLKSEL[4:0] |

## PPS Registers

| Register     | SPI1 Addr | SPI2 Addr | Purpose |
|-------------|----------|----------|---------|
| SPIxSCKPPS  | 0x3AD8   | 0x3ADB   | SCK input pin selection |
| SPIxSDIPPS  | 0x3AD9   | 0x3ADC   | SDI input pin selection |
| SPIxSSPPS   | 0x3ADA   | 0x3ADD   | SS input pin selection |

PPS output values: SCK1=0x1E, SDO1=0x1F, SS1=0x20; SCK2=0x29, SDO2=0x2A, SS2=0x2B.

## Key Bit Fields

### SPIxCON0 (0x084/0x091)
| Bit | Field | Description |
|-----|-------|-------------|
| 7   | EN    | SPI enable (1=enabled). Clear to reconfigure. |
| 2   | LSBF  | 0=MSb first, 1=LSb first |
| 1   | MST   | 0=Client, 1=Host |
| 0   | BMODE | 0=total-bit-count mode, 1=variable-transfer-size mode |

### SPIxCON1 (0x085/0x092)
| Bit | Field | Description |
|-----|-------|-------------|
| 7   | SMP   | Host: 0=mid-sample, 1=end-sample. Client: reserved when 1 |
| 6   | CKE   | 0=data changes Idle->Active edge, 1=Active->Idle edge |
| 5   | CKP   | 0=SCK idle low, 1=SCK idle high |
| 4   | FST   | Host: 1=remove 1/2-baud startup delay on SCK |
| 2   | SSP   | 0=SS active-high, 1=SS active-low |
| 1   | SDIP  | 0=SDI active-high, 1=SDI active-low |
| 0   | SDOP  | 0=SDO active-high, 1=SDO active-low |

### SPIxCON2 (0x086/0x093)
| Bit | Field | Description |
|-----|-------|-------------|
| 7   | BUSY  | RO — transfer in progress (up to 2-cycle sync delay) |
| 6   | SSFLT | RO — SS fault detected (client mode) |
| 2   | SSET  | Host: force SS_out active. Client: ignore SS_in |
| 1   | TXR   | 1=TX FIFO data required for transfer |
| 0   | RXR   | 1=RX FIFO space required to continue transfer |

### SPIxSTATUS (0x087/0x094)
| Bit | Field | Access | Description |
|-----|-------|--------|-------------|
| 7   | TXWE  | R/C/HS | TX FIFO write error (wrote when full) |
| 5   | TXBE  | RO     | TX FIFO empty |
| 3   | RXRE  | R/C/HS | RX FIFO read error (read when empty) |
| 2   | CLB   | S      | Set to clear both FIFOs |
| 0   | RXBF  | RO     | RX FIFO full |

### SPIxINTF / SPIxINTE (0x08A-0x08B / 0x097-0x098)
| Bit | Flag   | Enable | Description |
|-----|--------|--------|-------------|
| 7   | SRMTIF | SRMTIE | Shift register empty (Host only) |
| 6   | TCZIF  | TCZIE  | Transfer counter reached zero |
| 5   | SOSIF  | SOSIE  | Start of client select |
| 4   | EOSIF  | EOSIE  | End of client select |
| 2   | RXOIF  | RXOIE  | RX FIFO overflow (client only) |
| 1   | TXUIF  | TXUIE  | TX FIFO underflow (client only) |

### SPIxCLK (0x08C/0x099): CLKSEL[4:0]
| Value | Source | Value | Source |
|-------|--------|-------|--------|
| 0x00  | FOSC (system clock) | 0x08 | TMR6_Postscaled |
| 0x01  | HFINTOSC | 0x09-0x0E | CLC1_OUT through CLC8_OUT |
| 0x02  | MFINTOSC (500 kHz) | 0x0F | SMT1_OUT |
| 0x03  | CLKREF | 0x10 | TMR0_OUT |
| 0x04  | Reserved | 0x11 | TMR2_Postscaled |
| 0x05  | TMR0_overflow | 0x12 | TMR4_Postscaled |
| 0x06  | TMR2_Postscaled | 0x13 | TMR6_Postscaled |
| 0x07  | TMR4_Postscaled | 0x14 | CLC1_OUT |
|       | | 0x15-0x1F | More CLC outputs |

Note: Q43 extends SPIxCLK to 5 bits (vs 4 on K42), adding CLC5-CLC8, SMT1, TMR0, and additional timer postscaled outputs.

## Operating Modes

### Host/Client Selection (MST bit)
- **MST=1 Host**: Drives SCK, initiates transfers. Clock from SPIxBAUD/SPIxCLK.
- **MST=0 Client**: SCK is input, SS input gates transfers.

### TXR/RXR Mode Combinations (Host)

| TXR | RXR | Mode | Behavior |
|-----|-----|------|----------|
| 1 | 1 | Full Duplex | TX when RX FIFO not full and TX FIFO not empty (or TCNT!=0 if BMODE=0) |
| 0 | 1 | Receive Only | Clocks when RX FIFO not full and TCNT!=0. Re-sends last RX data if TX FIFO empty |
| 1 | 0 | Transmit Only | TX when TX FIFO not empty (or TCNT!=0 if BMODE=0). RX data discarded |
| 0 | 0 | Transfer Off | No SCK, no data exchange. TX writes buffered for later |

### Clock Polarity/Phase (CKP, CKE, SMP)
- **CKP**: SCK idle state (0=low, 1=high)
- **CKE**: Data output edge (0=Idle->Active, 1=Active->Idle)
- **SMP** (Host only): SDI sample point (0=mid-Output, 1=end-of-Output)

### Bit Order (LSBF)
- 0=MSb first (default, traditional SPI), 1=LSb first

## Transfer Counter (SPIxTCNT + SPIxTWIDTH)

- **BMODE=0 (total bit count)**: Total bits = TWIDTH[2:0] + TCNTx8. TWIDTH is remainder bits
  for final byte. TCNT must be nonzero for host transfers. Transfer stops at TCNT=0.
- **BMODE=1 (variable transfer size)**: TWIDTH = bits per transfer (0=8 bits). TCNT = number
  of transfers. Only stops transfers in Receive-Only mode (TCNT=0). TCNT can roll below zero.
- **Host Receive-Only**: Writing TCNTL starts transfer clocks. Clocks suspend when RX FIFO full.
- **Host Transmit/Full-Duplex** (BMODE=0): Writing TXB or TCNTL (whichever last) starts transfer.
- **Client mode**: TCNT decrements but doesn't control data; used for SS fault detection.

## FIFO Operation

- **TX FIFO**: 2-deep, write-only via SPIxTXB. TXBE=1 when empty. TXWE set on overflow write.
- **RX FIFO**: 2-deep, read-only via SPIxRXB. RXBF=1 when full. RXRE set on empty read.
- Read from empty RXB returns 0 and sets RXRE. Write to full TXB does nothing and sets TXWE.
- Set CLB bit (SPIxSTATUS<2>) to clear both FIFOs. Also cleared when EN=0.

## Client Select (SS)

### Host mode SS_out control
- **SSET=0**: SS_out asserted while TCNT!=0; auto-deassert after final SCK pulse.
- **SSET=1**: SS_out forced active continuously.
- SS polarity: SSP bit (1=active-low, 0=active-high).
- SS(out) and SCK(out) require TRIS=0 on their PPS output pins.

### Client mode SS_in
- SS gates transfers; SCK ignored when SS inactive.
- SSET=1: ignores SS_in, acts as if SS always active.
- SSFLT set when SS goes inactive during an incomplete transfer.

## Baud Rate (Host only)

```
FBAUD = FCSEL / (2 x (BAUD + 1))
```
Where FCSEL is the clock source selected by SPIxCLK, BAUD is the SPIxBAUD value.

## Interrupts

Three top-level interrupt sources per SPI instance:
1. **SPIxTXIF** (PIR): TX FIFO not full (read-only, DMA trigger)
2. **SPIxRXIF** (PIR): RX FIFO has data (read-only, DMA trigger)
3. **SPIxIF** (PIR): OR of enabled status flags in SPIxINTF/SPIxINTE

Status flags must be cleared in software. TCZIF only indicates count->0, not
transfer completion; use BUSY poll or SRMTIF for completion.

## DMA Support

DMA SIRQ trigger values: SPI1RX=0x18, SPI1TX=0x19, SPI1=0x1A; SPI2RX=0x28, SPI2TX=0x29, SPI2=0x2A.

## Key Setup Steps (Host Full Duplex, 8-bit)

1. Configure PPS: map SCK, SDO outputs; map SDI, SS inputs.
2. Set TRIS for SCK and SS outputs to 0; SDO TRIS=0 optional (always drives).
3. Set SPIxCLK to desired clock source.
4. Write SPIxBAUD for target baud rate.
5. Configure SPIxCON1: CKP, CKE, SMP, SSP, FST as needed.
6. Configure SPIxCON0: MST=1, BMODE=1, LSBF as needed.
7. Configure SPIxCON2: TXR=1, RXR=1.
8. Optionally write SPIxTCNT (required if BMODE=0).
9. Set SPIxCON0.EN=1 to enable.
10. Write data to SPIxTXB to begin transfer.
11. Read received data from SPIxRXB.

## Lock Rules
- Cannot modify SPIxBAUD, SPIxCON1, or SPIxCON0 (except EN) while EN=1.
- Cannot modify SPIxTCNT, SPIxTWIDTH, SPIxCON2, or CLB while BUSY=1.