# PIC18F16Q41 UART Peripheral

## Register Map

| Register  | UART1 addr | UART2 addr | UART3 addr | Description |
|-----------|-----------|-----------|-----------|-------------|
| UxRXB     | 0x02A1    | 0x02B4    | 0x02C7    | Receive buffer (read-only FIFO top) |
| UxTXB     | 0x02A3    | 0x02B6    | 0x02C9    | Transmit buffer write |
| UxRXCHK   | 0x02A2    | —         | —         | RX checksum result (UART1 only) |
| UxTXCHK   | 0x02A4    | —         | —         | TX checksum result (UART1 only) |
| UxP1      | 0x02A5    | 0x02B8    | 0x02CB    | Parameter 1 (9-bit: P1L+P1H bit 0) |
| UxP2      | 0x02A7    | 0x02BA    | 0x02CD    | Parameter 2 (9-bit) |
| UxP3      | 0x02A9    | 0x02BC    | 0x02CF    | Parameter 3 (9-bit) |
| UxCON0    | 0x02AB    | 0x02BE    | 0x02D1    | Control 0 |
| UxCON1    | 0x02AC    | 0x02BF    | 0x02D2    | Control 1 |
| UxCON2    | 0x02AD    | 0x02C0    | 0x02D3    | Control 2 |
| UxBRG     | 0x02AE    | 0x02C1    | 0x02D4    | Baud rate generator (16-bit: BRGL+BRGH) |
| UxFIFO    | 0x02B0    | 0x02C3    | 0x02D6    | FIFO status |
| UxUIR     | 0x02B1    | 0x02C4    | 0x02D7    | General interrupt flags |
| UxERRIR   | 0x02B2    | 0x02C5    | 0x02D8    | Error interrupt flags |
| UxERRIE   | 0x02B3    | 0x02C6    | 0x02D9    | Error interrupt enables |
| UxRXPPS   | 0x0272    | 0x0274    | 0x0276    | RX pin selection (PPS input) |
| UxCTSPPS  | 0x0273    | 0x0275    | 0x0277    | CTS pin selection (PPS input) |

UART1 = full-featured (LIN/DMX/DALI/checksum/collision). UART2/UART3 = limited (no UxRXCHK, UxTXCHK, C0EN, TXCIF, CERIF).

## Key Register Bit Fields

### UxCON0 (0x2AB/2BE/2D1)
| Bit | Name | Description |
|-----|------|-------------|
| 7 | BRGS | 0=normal (x16), 1=high-speed (x4) |
| 6 | ABDEN | Auto-baud detect enable (read-only when MODE>0111) |
| 5 | TXEN | Transmit enable |
| 4 | RXEN | Receive enable |
| 3:0 | MODE[3:0] | Mode select (see Modes table) |

### UxCON1 (0x2AC/2BF/2D2)
| Bit | Name | Description |
|-----|------|-------------|
| 7 | ON | UART enable |
| 4 | WUE | Wake-up enable (auto-cleared on break event) |
| 3 | RXBIMD | 0=RXBKIF on rising RX after break; 1=RXBKIF immediately |
| 1 | BRKOVR | Force TX to non-idle (software-timed break) |
| 0 | SENDB | Send fixed break on next UxTXB write (auto-cleared) |

### UxCON2 (0x2AD/2C0/2D3)
| Bit | Name | Description |
|-----|------|-------------|
| 7 | RUNOVF | 0=RSR stops on overflow; 1=RSR keeps syncing |
| 6 | RXPOL | Invert RX polarity |
| 5:4 | STP[1:0] | 00=1 stop; 01=1.5 stop; 10=2 stop(verify both); 11=2 stop(verify first) |
| 3 | C0EN | Checksum enable (UART1 only) |
| 2 | TXPOL | Invert TX polarity |
| 1:0 | FLO[1:0] | 00=off; 01=XON/XOFF; 10=RTS/CTS+TXDE |

### UxERRIR (0x2B2/2C5/2D8)
| Bit | Name | Description |
|-----|------|-------------|
| 7 | TXMTIF | TSR empty (1=done) |
| 6 | PERIF | Parity/address error on FIFO top byte |
| 5 | ABDOVF | Auto-baud overflow |
| 4 | CERIF | Checksum error (LIN only) |
| 3 | FERIF | Framing error on FIFO top byte |
| 2 | RXBKIF | Break detected |
| 1 | RXFOIF | RX FIFO overflow |
| 0 | TXCIF | TX collision (UART1 only) |

### UxFIFO (0x2B0/2C3/2D6)
| Bit | Name | Description |
|-----|------|-------------|
| 7 | TXWRE | TX write error (write when full); write-1-to-clear |
| 6 | STPMD | 0=RXIF in middle of stop; 1=RXIF at end of stop |
| 5 | TXBE | TX buffer empty (write-1 clears both TX buffer and TSR) |
| 4 | TXBF | TX buffer full |
| 3 | RXIDL | RX idle (1=idle) |
| 2 | XON | XON active (read-only) |
| 1 | RXBE | RX buffer empty (write-1 flushes RX FIFO; use MOVWF, not BSF) |
| 0 | RXBF | RX buffer full |

## Baud Rate Generator

**Formulas:**
- BRGS=0 (normal): `BaudRate = FOSC / [16 × (UxBRG + 1)]`
- BRGS=1 (high-speed): `BaudRate = FOSC / [4 × (UxBRG + 1)]`

**Solving for UxBRG:**
- BRGS=0: `UxBRG = (FOSC / (16 × DesiredBaud)) - 1`
- BRGS=1: `UxBRG = (FOSC / (4 × DesiredBaud)) - 1`

**BRG max values in protocol modes:**
- MODE=100x with BRGS=1: max UxBRG = 0x7FFE
- MODE=100x with BRGS=0: max UxBRG = 0x1FFE

**Auto-baud detect:** BRGS=0 clocks at FOSC/128; BRGS=1 clocks at FOSC/32. On 5th falling edge of 0x55 sync char, UxBRG is set and ABDEN auto-clears.

**Gotcha:** UxBRG can only be written when ON=0. Changing FOSC during active RX may cause errors—check RXIDL first.

## Operating Modes (UxCON0 MODE[3:0])

| MODE | Mode | TXEN | RXEN | Notes |
|------|------|------|------|-------|
| 0000 | 8-bit async | 1 | 0/1 | Default |
| 0001 | 7-bit async | 1 | 0/1 | Low 7 bits transmitted |
| 0010 | 8-bit + odd parity | 1 | 0/1 | 9th bit = odd parity |
| 0011 | 8-bit + even parity | 1 | 0/1 | 9th bit = even parity |
| 0100 | 9-bit address | 1 | 0/1 | UxP1L=address (9th=1); UxTXB=data (9th=0) |
| 1000 | DALI Control Device* | 1 | 1 | MSb-first, Manchester, UxP1=wait half-bits |
| 1001 | DALI Control Gear* | 1 | 1 | MSb-first, Manchester |
| 1010 | DMX* | 1 or 0 | 0 or 1 | 250Kbaud, 2 stop bits (STP=10) |
| 1011 | LIN Client* | 1 | 1 | Auto-baud on sync, auto checksum |
| 1100 | LIN Host/Client* | 1 | 1 | Writes UxP1L to start host process |

\* Full-featured UART (UART1) only.

## Asynchronous Mode Quick Setup

**TX:** Set UxBRG+BRGS → MODE → TXPOL → ON=1 → TXEN=1 → PPS TX output → UxTXIE → write UxTXB

**RX:** Set UxBRG+BRGS → RXPPS → ANSEL=0 → MODE → RXPOL → ON=1 → UxRXIE → RXEN=1

## DMX Mode (UART1 Only)

**Controller (TX):** MODE=1010, TXEN=1, RXEN=0, UxP1=(byte_count-1), STP=10, BRGS+UxBRG for 250K baud, TXPOL=0, ON=1

Auto-generates 25 bit-time break + 3 bit-time MAB. Software writes Start Code then data bytes. After UxP1+1 bytes, HW inserts break automatically. Toggle TXEN after TXMTIF to sync universe boundaries.

**Receiver (RX):** MODE=1010, TXEN=0, RXEN=1, UxP2=first byte number, UxP3=last byte number, STP=10, ON=1

Listens for 23 bit-time break. Start Code always stored. Bytes outside UxP2..UxP3 range are ignored. Monitor RXBKIF to verify sync.

## LIN Mode (UART1 Only)

**Host/Client (MODE=1100):** TXEN=1, RXEN=1, set C0EN for checksum type, STP. Write PID to UxP1L to start host process. HW generates break, delimiter, sync (0x55), PID (with parity). Client data portion follows. TXEN must stay set.

**Client Only (MODE=1011):** TXEN=1, RXEN=1. Break clears UxTXCHK/UxRXCHK/UxP2/UxP3. Auto-baud on sync char. PID received with parity check (PERIF). UxP2=TX byte count, UxP3=RX byte count. Checksum auto-appended on TX, auto-verified on RX.

**Checksum (C0EN):** 0=legacy (data only); 1=enhanced (PID+data). Must set before checksum byte arrives.

**TX flow (client):** Set UxP2 → C0EN → write bytes to UxTXB (UxTXIF gated by UxP2 count). HW sends inverted checksum as last byte.

**RX flow (client):** Set UxP3 → C0EN → read bytes from UxRXB. After last data byte, checksum byte is received; CERIF=1 means checksum fail.

## DALI Mode (UART1 Only)

Manchester-encoded, MSb-first, typically 1200 baud. Forward frames: 2 or 3 bytes. Backward frames: 1 byte. STP=10 (2 stop periods).

**Control Device (MODE=1000):** TXEN=1, RXEN=1. UxP1=forward wait half-bit periods. UxP2=forward/backward threshold. Write control byte to UxTXB; subsequent data to UxTXB while UxTXIF=1. PERIF set on forward frame rx.

**Control Gear (MODE=1001):** TXEN=1, RXEN=1. UxP1=backward wait half-bit periods. UxP2=forward frame idle threshold. Write backward frame byte to UxTXB; HW delays per UxP1.

ABDEN=1: auto-baud on incoming start bit (BRGS=1 not supported in DALI).

## Checksum (Non-LIN Modes, UART1 Only)

1. Clear UxTXCHK/UxRXCHK
2. Set C0EN
3. Send/receive all bytes
4. TX: invert UxTXCHK and send as last byte
5. RX: add 1 to UxRXCHK; result=0x00 means pass

## Key Gotchas

1. **UxTXIF is set when TXEN is set** (buffer empty), even before writing data.
2. **UxBRG writes require ON=0** (UART disabled).
3. **Changing MODE while ON=1** may cause unexpected results; clear ON first.
4. **Clearing TXEN/RXEN does NOT flush buffers**; use TXBE/RXBE bits to flush.
5. **RXBE must not be set with BSF**—use MOVWF to avoid accidentally clearing a pending TSR byte.
6. **FERIE/PERIE suppress UxRXIF** when FERIF/PERIF=1 respectively. This blocks DMA on errors.
7. **BRGS=1 not supported in DALI mode**.
8. **RX on analog pins**: must clear ANSEL for that pin.
9. **Address mode**: UxP2L=address, UxP3L=mask. Match = ((received XOR UxP2L) AND UxP3L) == 0. PERIF stores 9th bit.
10. **Auto-baud**: sends 0x55 ("U"); UxBRG measured from 5 falling edges. ABDOVF set if counter overflow.
11. **WUE wake-on-break**: WUE auto-clears on break end; check RXIDL before setting WUE.
12. **STPMD**: delays UxRXIF to end of stop bits—useful for half-duplex direction switching.
13. **Collision detection** (TXCIF): always active when TXEN+RXEN both set, even without loopback.
14. **2-byte RX FIFO**: overflow discards incoming byte. RUNOVF=1 keeps RSR syncing.
15. **TSR is not accessible** by software; only UxTXB and status bits.