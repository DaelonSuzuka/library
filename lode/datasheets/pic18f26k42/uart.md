# PIC18F26K42 UART Peripheral

## Instances & Register Map
K42 has 2 UART instances. UART1 is full-featured (LIN/DMX/DALI/checksum/collision). UART2 is limited (no UxRXCHK, UxTXCHK, C0EN, UxP1H/UxP2H/UxP3H, TXCIF).

| Register  | UART1 addr | UART2 addr | Description |
|-----------|-----------|-----------|-------------|
| UxRXB     | 0x3DE8    | 0x3DD0    | Receive buffer (read-only FIFO top) |
| UxTXB     | 0x3DEA    | 0x3DD2    | Transmit buffer write |
| UxRXCHK   | 0x3DE9    | —         | RX checksum result (UART1 only) |
| UxTXCHK   | 0x3DEB    | —         | TX checksum result (UART1 only) |
| UxP1L     | 0x3DEC    | 0x3DD4    | Parameter 1 low byte |
| UxP1H     | 0x3DED    | —         | Parameter 1 bit 8 (UART1 only) |
| UxP2L     | 0x3DEE    | 0x3DD6    | Parameter 2 low byte |
| UxP2H     | 0x3DEF    | —         | Parameter 2 bit 8 (UART1 only) |
| UxP3L     | 0x3DF0    | 0x3DD8    | Parameter 3 low byte |
| UxP3H     | 0x3DF1    | —         | Parameter 3 bit 8 (UART1 only) |
| UxCON0    | 0x3DF2    | 0x3DDA    | Control 0 |
| UxCON1    | 0x3DF3    | 0x3DDB    | Control 1 |
| UxCON2    | 0x3DF4    | 0x3DDC    | Control 2 |
| UxBRGL    | 0x3DF5    | 0x3DDD    | Baud rate generator low byte |
| UxBRGH    | 0x3DF6    | 0x3DDE    | Baud rate generator high byte |
| UxFIFO    | 0x3DF7    | 0x3DDF    | FIFO status |
| UxUIR     | 0x3DF8    | 0x3DE0    | General interrupt flags |
| UxERRIR   | 0x3DF9    | 0x3DE1    | Error interrupt flags |
| UxERRIE   | 0x3DFA    | 0x3DE2    | Error interrupt enables |
| U1RXPPS   | 0x3AE5    | —         | UART1 RX pin (PPS input) |
| U1CTSPPS  | 0x3AE6    | —         | UART1 CTS pin (PPS input) |
| U2RXPPS   | 0x3AE8    | —         | UART2 RX pin (PPS input) |
| U2CTSPPS  | 0x3AE9    | —         | UART2 CTS pin (PPS input) |

## Key Register Bit Fields
### UxCON0
| Bit | Name | Description |
|-----|------|-------------|
| 7 | BRGS | 0=normal (x16), 1=high-speed (x4) |
| 6 | ABDEN | Auto-baud detect enable (ignored when MODE=100x) |
| 5 | TXEN | Transmit enable |
| 4 | RXEN | Receive enable |
| 3:0 | MODE[3:0] | Mode select (see Modes table) |

### UxCON1
| Bit | Name | Description |
|-----|------|-------------|
| 7 | ON | UART enable |
| 4 | WUE | Wake-up enable (auto-cleared on break event) |
| 3 | RXBIMD | 0=RXBKIF on rising RX after break; 1=RXBKIF immediately |
| 1 | BRKOVR | Force TX to non-idle (software-timed break) |
| 0 | SENDB | Send fixed break on next UxTXB write (auto-cleared) |

### UxCON2
| Bit | Name | Description |
|-----|------|-------------|
| 7 | RUNOVF | 0=RSR stops on overflow; 1=RSR keeps syncing |
| 6 | RXPOL | Invert RX polarity |
| 5:4 | STP[1:0] | 00=1 stop; 01=1.5 stop; 10=2 stop(verify both); 11=2 stop(verify first) |
| 3 | C0EN | Checksum enable (UART1 only; unimplemented on UART2) |
| 2 | TXPOL | Invert TX polarity |
| 1:0 | FLO[1:0] | 00=off; 01=XON/XOFF; 10=RTS/CTS+TXDE |

### UxERRIR
| Bit | Name | Description |
|-----|------|-------------|
| 7 | TXMTIF | TSR empty (1=done) |
| 6 | PERIF | Parity/address error on FIFO top byte |
| 5 | ABDOVF | Auto-baud overflow |
| 4 | CERIF | Checksum error (LIN) / DALI stop bit detected |
| 3 | FERIF | Framing error on FIFO top byte |
| 2 | RXBKIF | Break detected |
| 1 | RXFOIF | RX FIFO overflow |
| 0 | TXCIF | TX collision (UART1 only) |

### UxERRIE
| Bit | Name | Description |
|-----|------|-------------|
| 7 | TXMTIE | TX shift register empty interrupt enable |
| 6 | PERIE | Parity error interrupt enable |
| 5 | ABDOVE | Auto-baud overflow interrupt enable |
| 4 | CERIE | Checksum error / DALI STP interrupt enable |
| 3 | FERIE | Framing error interrupt enable |
| 2 | RXBKIE | Break reception interrupt enable |
| 1 | RXFOIE | RX FIFO overflow interrupt enable |
| 0 | TXCIE | TX collision interrupt enable (UART1 only) |

### UxUIR
| Bit | Name | Description |
|-----|------|-------------|
| 7 | WUIF | Wake-up detected (clear by software to clear UxIF) |
| 6 | ABDIF | Auto-baud detect complete (clear by software) |
| 2 | ABDIE | ABDIF will set UxIF in PIR register |

### UxFIFO
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

\* UART1 only.

## Interrupt Flags and Enables

**PIR3 (UART1):** U1IF(b5), U1EIF(b4), U1TXIF(b3), U1RXIF(b2)  
**PIE3 (UART1):** U1IE(b5), U1EIE(b4), U1TXIE(b3), U1RXIE(b2)  
**PIR6 (UART2):** U2IF(b5), U2EIF(b4), U2TXIF(b3), U2RXIF(b2)  
**PIE6 (UART2):** U2IE(b5), U2EIE(b4), U2TXIE(b3), U2RXIE(b2)

UxIF is a summary flag: set when WUIF or ABDIF (UxUIR) is set and their enables are active. UxEIF is set when any enabled error flag in UxERRIR is set.

**UxRXIF suppression:** UxRXIF is suppressed (held low) when FERIF=1 and FERIE=1, or when PERIF=1 and PERIE=1. This blocks DMA on errors.

## FIFO Operation
**RX FIFO:** 2-deep + RSR. Overflow discards incoming byte; RUNOVF=1 keeps RSR syncing (first byte after clearing overflow is valid); RUNOVF=0 stops RSR (first byte may be partial).  
**TX FIFO:** 1-deep (UxTXB) + TSR. UxTXIF=1 when buffer empty. TXMTIF=1 when TSR also empty and idle.

**Flush TX:** write TXBE=1 (use MOVWF, not BSF, if UxTXB empty to avoid clearing pending TSR byte).  
**Flush RX:** write RXBE=1 (use MOVWF, not BSF, to avoid clearing pending TSR byte).  
**ON=0:** discards all TX and RX data.

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

**RX flow (client):** Set UxP3 → C0EN → read bytes from UxRXB. After last data byte, checksum byte received; CERIF=1 means checksum fail.

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

## Auto-Baud Detection
Set ABDEN=1 in 8-bit async mode. UART waits for 0x55 sync character. On 5th falling edge, UxBRG is loaded from internal counter and ABDEN auto-clears. ABDIF is set; must be cleared by software. ABDOVF set if counter overflows before 5th edge. Not available in DALI mode (MODE=100x). In LIN mode, auto-baud occurs automatically at each break.

## RS-485/Transceiver Control
Hardware flow control (FLO=10) provides RTS output and CTS input plus TXDE for RS-485 direction control. TXDE is high when TX is actively transmitting, low otherwise. Configure CTS to always-enabled (set UxCTSPPS to unimplemented pin like 0x18) to use TXDE for RS-485 half-duplex. This prevents loopback reception. For collision detection, tie RE low to enable loopback; TXCIF (UART1 only) flags mismatches.

## PPS Routing for UART Pins
**Output (RxyPPS values):**

| Function | RxyPPS Code | Default Pin (PIC18F26K42) |
|----------|------------|--------------------------|
| UART1 TX  | 0x13 | RC6 |
| UART1 TXDE | 0x14 | — |
| UART1 RTS  | 0x15 | — |
| UART2 TX  | 0x16 | RB6 |
| UART2 TXDE | 0x17 | — |
| UART2 RTS  | 0x19 | — |

**Input (UxRxPPS/UxCTSPPS values):**

| Register  | Default Pin | PPS Value |
|-----------|------------|-----------|
| U1RXPPS   | RC7 | 0x17 |
| U1CTSPPS  | RC6 | 0x16 |
| U2RXPPS   | RB7 | 0x0F |
| U2CTSPPS  | RB6 | 0x0E |

## Asynchronous Mode Quick Setup
**TX:** Set UxBRG+BRGS → MODE → TXPOL → ON=1 → TXEN=1 → PPS TX output → UxTXIE → write UxTXB

**RX:** Set UxBRG+BRGS → RXPPS → ANSEL=0 → MODE → RXPOL → ON=1 → UxRXIE → RXEN=1

## Key Gotchas
1. **UxTXIF set when TXEN set** (buffer empty), even before writing data.
2. **UxBRG writes require ON=0**; changing FOSC during RX may cause errors (check RXIDL first).
3. **Changing MODE while ON=1** may cause unexpected results; clear ON first.
4. **Clearing TXEN/RXEN does NOT flush buffers**; use TXBE/RXBE to flush.
5. **RXBE must use MOVWF**, not BSF—BSF may clear a pending TSR byte.
6. **FERIE/PERIE suppress UxRXIF** when FERIF/PERIF=1; blocks DMA on errors.
7. **BRGS=1 not supported in DALI mode**.
8. **RX on analog pins**: must clear ANSEL for that pin.
9. **Address mode**: UxP2L=addr, UxP3L=mask. Match = ((rx XOR UxP2L) AND UxP3L) == 0. PERIF stores 9th bit.
10. **Auto-baud**: sends 0x55; UxBRG measured from 5 falling edges. ABDOVF on overflow.
11. **WUE**: auto-clears on break end; check RXIDL before setting WUE.
12. **STPMD**: delays UxRXIF to end of stop bits—useful for half-duplex direction switching.
13. **TXCIF (UART1 only)**: always active when TXEN+RXEN set, even without loopback.
14. **2-byte RX FIFO**: overflow discards incoming byte. RUNOVF=1 keeps RSR syncing.
15. **UART2 limitations**: no C0EN, UxRXCHK, UxTXCHK, UxP1H/UxP2H/UxP3H, or TXCIF.
16. **SENDB read-only** in LIN/DMX/DALI modes—break generation is automatic.