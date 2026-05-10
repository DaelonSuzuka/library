                         PIC18(L)F26/27/45/46/47/55/56/57K42
31.0     UNIVERSAL ASYNCHRONOUS                                               The UART module includes the following capabilities:
         RECEIVER TRANSMITTER                                                 • Full-duplex asynchronous transmit and receive
         (UART) WITH PROTOCOL                                                 • Two-character input buffer
                                                                              • One-character output buffer
         SUPPORT                                                              • Programmable 7-bit or 8-bit character length
The Universal Asynchronous Receiver Transmitter                               • 9th bit Address detection
(UART) module is a serial I/O communications                                  • 9th bit even or odd parity
peripheral. It contains all the clock generators, shift                       • Input buffer overrun error detection
registers and data buffers necessary to perform an                            • Received character framing error detection
input or output serial data transfer, independent of                          • Hardware and software flow control
device program execution. The UART, also known as a                           • Automatic checksums
Serial Communications Interface (SCI), can be                                 • Programmable 1, 1.5, and 2 Stop bits
configured as a full-duplex asynchronous system or                            • Programmable data polarity
one of several automated protocols. Full Duplex mode                          • Manchester encoder/decoder
is useful for communications with peripheral systems,                         • Operation in Sleep
such as CRT terminals and personal computers.                                 • Automatic detection and calibration of the baud
                                                                                rate
Supported protocols include:                                                  • Wake-up on Break reception
• LIN Host and Client                                                         • Automatic and user timed Break period
• DMX mode                                                                      generation
• DALI control gear and control device                                        • RX and TX inactivity timeouts (with Timer2)
                                                                              Block diagrams of the UART transmitter and receiver
                                                                              are shown in Figure 31-1 and Figure 31-2.
                                                                              The UART transmit output (TX_out) is available to the
                                                                              TX pin and internally to various peripherals.

FIGURE 31-1:                 UART TRANSMIT BLOCK DIAGRAM
                                                                                  Data Bus
                                                                                                              UxTXIE

                                                           +                                                                   Interrupt
                                            UxTXCHK                    UxTXB Register                     UxTXIF
                                                                                 8                                           RxyPPS
                                        TXEN
                                                           MSb                                    LSb                                 TX pin
                                                           (8)                                     0               Mode
                                                                            • • •                                  Control    PPS
                                                                 Transmit Shift Register (TSR)


                                                                                                 TXMTIF        TX_out
                                                                   Address or
  Baud Rate Generator         FOSC                                 Parity Mode
                                            ÷n

                                                 n
                        +1     Multiplier    x4      x16
                                BRGS         1       0
   UxBRGH    UxBRGL


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 475
                        PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 31-2:                 UART RECEIVE BLOCK DIAGRAM

                                              RXEN                                                             RXFOIF                 RXIDL


                       RXPPS
             RX pin                                                                      MSb              RSR Register           LSb
                                         Pin Buffer                   Mode Data
                        PPS              and Control                  Recovery
                                                                                        Stop    (8)   7      •••       1      0 Start


       Baud Rate Generator                                 FOSC
                                                                      ÷n
                                                                                               Address or          +
                                                                                               Parity Mode                   UxRXCHK

                         +1                                       n
                                 Multiplier   x4     x16
                                  BRGS        1        0
       UxBRGH      UxBRGL                                                                                                                     FIFO
                                                                                     FERIF     PERIF          UxRXB Register


                                                                                                                   8
                                                                                                                           Data Bus

                                                                                                                       RXIF             Interrupt
                                                                                                                       RXIE


The operation of the UART module is controlled                                represents a ‘1’ data bit, and a VOL space state, which
through nineteen registers:                                                   represents a ‘0’ data bit. NRZ refers to the fact that
• Three control registers (UxCON0-UxCON2)                                     consecutively transmitted data bits of the same value
• Error enable and status (UxERRIE, UxERRIR,                                  stay at the output level of that bit without returning to a
  UxUIR)                                                                      neutral level between each bit transmission. An NRZ
• UART buffer status and control (UxFIFO)                                     transmission port idles in the Mark state. Each character
• Three 9-bit protocol parameters (UxP1-UxP3)                                 transmission consists of one Start bit followed by seven
• 16-bit baud rate generator (UxBRGH:L)                                       or eight data bits, one optional parity or address bit, and
• Transmit buffer write (UxTXB)                                               is always terminated by one or more Stop bits. The Start
• Receive buffer read (UxRXB)                                                 bit is always a space and the Stop bits are always
• Receive checksum (UxRXCHK)                                                  marks. The most common data format is eight bits with
• Transmit checksum (UxTXCHK)                                                 no parity. Each transmitted bit persists for a period of 1/
                                                                              (Baud Rate). An on-chip dedicated 16-bit Baud Rate
These registers are detailed in Section 31.21 “Register                       Generator is used to derive standard baud rate
Definitions: UART Control”.                                                   frequencies from the system oscillator. See
                                                                              Section 31.17 “UART Baud Rate Generator (BRG)”
31.1      UART I/O Pin Configuration                                          for more information.
The RX input pin is selected with the UxRPPS register.                        In all the asynchronous modes, the UART transmits
The TX output pin is selected with each pin’s RxyPPS                          and receives the LSb first. The UART’s transmitter and
register. When the TRIS control for the pin corresponding                     receiver are functionally independent, but share the
to the TX output is cleared, then the UART will maintain                      same data format and baud rate. Parity is supported by
control and the logic level on the TX pin. Changing the                       the hardware by Even and Odd Parity modes.
TXPOL bit in UxCON2 will immediately change the TX
pin logic level regardless of the value of EN or TXEN.                        31.2.1      UART ASYNCHRONOUS
                                                                                          TRANSMITTER
31.2      UART Asynchronous Modes                                             The UART transmitter block diagram is shown in
                                                                              Figure 31-1. The heart of the transmitter is the serial
The UART has five asynchronous modes:                                         Transmit Shift Register (TSR), which is not directly
• 7-bit                                                                       accessible by software. The TSR obtains its data from
• 8-bit                                                                       the transmit buffer, which is the UxTXB register.
• 8-bit with even parity in the 9th bit
• 8-bit with odd parity in the 9th bit
• 8-bit with address indicator in the 9th bit
The UART transmits and receives data using the
standard Non-Return-to-Zero (NRZ) format. NRZ is
implemented with two levels: a VOH mark state, which


 2017-2021 Microchip Technology Inc.                                                                              DS40001919G-page 476
                        PIC18(L)F26/27/45/46/47/55/56/57K42
31.2.1.1      Enabling the Transmitter                         The UxTXIF interrupt can be enabled by setting the
                                                               UxTXIE interrupt enable bit in the PIE register.
The UART transmitter is enabled for asynchronous
                                                               However, the UxTXIF flag bit will be set whenever the
operations by configuring the following control bits:
                                                               UxTXB is empty, regardless of the state of UxTXIE
• TXEN = 1                                                     enable bit.The UxTXIF bit is read-only and cannot be
• MODE[3:0] = 0h through 3h                                    set or cleared by software.
• UxBRGH:L = desired baud rate
                                                               To use interrupts when transmitting data, set the
• UxBRGS = desired baud rate multiplier
                                                               UxTXIE bit only when there is more data to send. Clear
• RxyPPS = code for desired output pin
                                                               the UxTXIE interrupt enable bit upon writing UxTXB
• ON = 1
                                                               with the last character of the transmission.
All other UART control bits are assumed to be in their
default state.                                                 31.2.1.5      TSR Status
Setting the TXEN bit in the UxCON0 register enables            The TXMTIF bit in the UxERRIR register indicates the
the transmitter circuitry of the UART. The MODE[3:0]           status of the TSR. This is a read-only bit. The TXMTIF
bits in the UxCON0 register select the desired mode.           bit is set when the TSR is empty and idle. The TXMTIF
Setting the ON bit in the UxCON1 register enables the          bit is cleared when a character is transferred to the
UART. When TXEN is set and the transmitter is not idle,        TSR from the UxTXB. The TXMTIF bit remains clear
the TX pin is automatically configured as an output.           until all bits, including the Stop bits, have been shifted
When the transmitter is idle, the TX pin drive is              out of the TSR and a byte is not waiting in the UxTXB
relinquished to the port TRIS control. If the TX pin is        register.
shared with an analog peripheral, the analog I/O
                                                               The TXMTIF will generate an interrupt when the
function may be disabled by clearing the corresponding
                                                               TXMTIE bit in the UxERRIE register is set.
ANSEL bit.
                                                                 Note:     The TSR is not mapped in data memory,
  Note:     The UxTXIF Transmitter Interrupt flag is
                                                                           so it is not available to the user.
            set when the TXEN enable bit is set and
            the UxTXB register can accept data.
                                                               31.2.1.6      Transmitter 7-bit Mode
31.2.1.2      Transmitting Data                                7-Bit mode is selected when the MODE[3:0] bits are set
                                                               to ‘0001’. In 7-bit mode, only the seven Least
A transmission is initiated by writing a character to the
                                                               Significant bits of the data written to UxTXB are
UxTXB register. If this is the first character, or the
                                                               transmitted. The Most Significant bit is ignored.
previous character has been completely transmitted
from the TSR, the data in the UxTXB is immediately             31.2.1.7      Transmitter Parity Modes
transferred to the TSR register. If the TSR still contains
all or part of a previous character, the new character         When the Odd or even Parity mode is selected, all data
data is held in the UxTXB until the previous character         is sent as nine bits. The first eight bits are data and the
transmission is complete. The pending character in the         9th bit is parity. Even and odd parity is selected when
UxTXB is then transferred to the TSR at the beginning          the MODE[3:0] bits are set to ‘0011’ and ‘0010’,
of the previous character Stop bit transmission. The           respectively. Parity is automatically determined by the
transmission of the Start bit, data bits and Stop bit          module and inserted in the serial data stream.
sequence commences immediately following the
completion of all of the previous character’s Stop bits.

31.2.1.3      Transmit Data Polarity
The polarity of the transmit data is controlled with the
TXPOL bit in the UxCON2 register. The default state of
this bit is ‘0’ which selects high true transmit idle and
data bits. Setting the TXPOL bit to ‘1’ will invert the
transmit data, resulting in low true idle and data bits. The
TXPOL bit controls transmit data polarity in all modes.

31.2.1.4      Transmit Interrupt Flag
The UxTXIF interrupt flag bit in the PIR register is set
whenever the UART transmitter is enabled and no
character is being held for transmission in the UxTXB. In
other words, the UxTXIF bit is clear only when the TSR
is busy with a character and a new character has been
queued for transmission in the UxTXB.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 477
                              PIC18(L)F26/27/45/46/47/55/56/57K42
31.2.1.8            Asynchronous Transmission Setup
1.     Initialize the UxBRGH, UxBRGL register pair and
       the BRGS bit to achieve the desired baud rate
       (see Section 31.17 “UART Baud Rate
       Generator (BRG)”).
2.     Set the MODE[3:0] bits to the desired
       Asynchronous mode.
3.     Set TXPOL bit if inverted TX output is desired.
4.     Enable the asynchronous serial port by setting
       the ON bit.
5.     Enable the transmitter by setting the TXEN
       control bit. This will cause the UxTXIF interrupt
       flag to be set.
6.     If the device has PPS, configure the desired I/O
       pin RxyPPS register with the code for TX output.
7.     If interrupts are desired, set the UxTXIE interrupt
       enable bit in the respective PIE register. An
       interrupt will occur immediately provided that the
       GIE bits in the INTCON0 register are also set.
8.     Write one byte of data into the UxTXB register.
       This will start the transmission.
9.     Subsequent bytes may be written when the
       UxTXIF bit is ‘1’.

FIGURE 31-3:                   ASYNCHRONOUS TRANSMISSION

      Write to UxTXB
                                   Word 1
          BRG Output
          (Shift Clock)
                      TX
                      pin                        Start bit        bit 0         bit 1                       last bit       Stop bit
                                                                                 Word 1
           UxTXIF bit
      (Transmit Buffer                        1 TCY
     Reg. Empty Flag)


                                  Word 1
           TXMTIF bit             Transmit Shift Reg.
       (Transmit Shift
     Reg. Empty Flag)


FIGURE 31-4:                   ASYNCHRONOUS TRANSMISSION (BACK-TO-BACK)

       Write to UxTXB
                                     Word 1           Word 2
             BRG Output
             (Shift Clock)
                      TX
                      pin                        Start bit        bit 0       bit 1                     last bit       Stop bit       Start bit     bit 0
            UxTXIF bit         1 TCY                                           Word 1                                                      Word 2
       (Transmit Buffer
      Reg. Empty Flag)                                         1 TCY

           TXMTIF bit              Word 1                                                                          Word 2
       (Transmit Shift             Transmit Shift Reg.                                                             Transmit Shift Reg.
     Reg. Empty Flag)


     Note:         This timing diagram shows the first transmission and the start of the second consecutive transmission.


 2017-2021 Microchip Technology Inc.                                                                                             DS40001919G-page 478
                        PIC18(L)F26/27/45/46/47/55/56/57K42
31.2.2       UART ASYNCHRONOUS RECEIVER                          If both samples are high then the falling edge is
                                                                 deemed a glitch and the UART returns to the Start bit
The Asynchronous mode is typically used in RS-232
                                                                 detection state without generating an error.
systems. The receiver block diagram is shown in
Figure 31-2. The data is received on the RX pin and              If either sample is low, the data recovery circuit
drives the data recovery block. The data recovery block          continues counting BRG clocks and takes samples at
is actually a high-speed shifter operating at 4 or 16            clock counts 7, 8, and 9. When less than two samples
times the baud rate, whereas the serial Receive Shift            are low, the Start bit is deemed invalid and the data
Register (RSR) operates at the bit rate. When all bits of        recovery circuit aborts character reception, without
the character have been shifted in, they are                     generating an error, and resumes looking for the falling
immediately transferred to a two character First-In-             edge of the Start bit.
First-Out (FIFO) memory. The FIFO buffering allows               When two or more samples are low, the Start bit is
reception of two complete characters and the start of a          deemed valid and the data recovery continues. After a
third character before software must start servicing the         valid Start bit is detected, the BRG clock counter
UART receiver. The FIFO registers and RSR are not                continues and resets at count 16. This is the beginning
directly accessible by software. Access to the received          of the first data bit.
data is via the UxRXB register.
                                                                 The data recovery circuit counts BRG clocks from the
31.2.2.1       Enabling the Receiver                             beginning of the bit and takes samples at clocks 7, 8,
                                                                 and 9. The bit value is determined from the majority of
The UART receiver is enabled for asynchronous                    the samples. The resulting ‘0’ or ‘1’ is shifted into the
operation by configuring the following control bits:             RSR.The BRG clock counter continues and resets at
• RXEN = 1                                                       count 16. This sequence repeats until all data bits have
• MODE[3:0] = 0h through 3h                                      been sampled and shifted into the RSR.
• UxBRGH:L = desired baud rate                                   After all data bits have been shifted in, the first Stop bit
• RXPPS = code for desired input pin                             is sampled. Stop bits are always a ‘1’. If the bit sampling
• Input pin ANSEL bit = 0                                        determines that a ‘0’ is in the Stop bit position, the
• ON = 1                                                         framing error is set for this character. Otherwise, the
All other UART control bits are assumed to be in their           framing error is cleared for this character. See Section
default state.                                                   31.2.2.4 “Receive Framing Error” for more
Setting the RXEN bit in the UxCON0 register enables              information on framing errors.
the receiver circuitry of the UART. Setting the
                                                                 31.2.2.3      Receive Interrupts
MODE[3:0] bits in the UxCON0 register configures the
UART for the desired Asynchronous mode. Setting the              Immediately after all data bits and the Stop bit have
ON bit in the UxCON1 register enables the UART. The              been received, the character in the RSR is transferred
TRIS bit corresponding to the selected RX I/O pin must           to the UART receive FIFO. The UxRXIF interrupt flag in
be set to configure the pin as an input.                         the respective PIR register is set at this time, provided
                                                                 it is not being suppressed.
  Note:      If the RX function is on an analog pin, the
             corresponding ANSEL bit must be cleared             The UxRXIF is suppressed by any of the following:
             for the receiver to function.                       • FERIF if FERIE is set
                                                                 • PERIF if PERIE is set
31.2.2.2       Receiving Data                                    This suspends DMA transfer of data until software
Data is recovered from the bit stream by timing to the           processes the error and reads UxRXB to advance the
center of the bits and sampling the input level. In High-        FIFO beyond the error.
Speed mode, there are four BRG clocks per bit and                UxRXIF interrupts are enabled by setting all of the
only one sample is taken per bit. In Normal Speed                following bits:
mode, there are 16 BRG clocks per bit and three
samples are taken per bit.                                       • UxRXIE, Interrupt Enable bit in the PIE register
                                                                 • GIE, Global Interrupt Enable bits in the INTCON0
The receiver data recovery circuit initiates character             register
reception on the falling edge of the Start bit. The Start
bit, is always a ‘0’. The Start bit is qualified in the middle   The UxRXIF interrupt flag bit will be set when not
of the bit. In Normal Speed mode only, the Start bit is          suppressed and there is an unread character in the
also qualified at the leading edge of the bit. The               FIFO, regardless of the state of interrupt enable bits.
following paragraphs describe the majority detect                Reading the UxRXB register will transfer the top
sampling of Normal Speed mode.                                   character out of the FIFO and reduce the FIFO
                                                                 contents by one. The UxRXIF interrupt flag bit is read-
The falling edge starts the baud rate generator (BRG)            only, it cannot be set or cleared by software.
clock. The input is sampled at the first and second BRG
clocks.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 479
                        PIC18(L)F26/27/45/46/47/55/56/57K42
31.2.2.4       Receive Framing Error                            31.2.2.6     Receive FIFO Overflow
Each character in the receive FIFO buffer has a                 When more characters are received than the receive
corresponding framing error flag bit. A framing error           FIFO can hold, the RXFOIF bit in the UxERRIR register
indicates that the Stop bit was not seen at the expected        is set. The character causing the overflow condition is
time. The framing error flag is accessed via the FERIF          discarded. The RUNOVF bit in the UxCON2 register
bit in the UxERRIR register. The FERIF bit represents           determines how the receive circuit responds to
the frame status of the top unread character of the             characters while the overflow condition persists. When
receive FIFO. Therefore, the FERIF bit must be read             RUNOVF is set, the receive shifter stays synchronized
before reading UxRXB.                                           to the incoming data stream by responding to Start,
The FERIF bit is read-only and only applies to the top          data, and Stop bits. However, all received bytes not
unread character of the receive FIFO. A framing error           already in the FIFO are discarded. When RUNOVF is
(FERIF = 1) does not preclude reception of additional           cleared, the receive shifter ceases operation and Start,
characters. It is neither necessary nor possible to clear       data, and Stop bits are ignored. The receive overflow
the FERIF bit directly. Reading the next character from         condition is cleared by reading the UxRXB register and
the FIFO buffer will advance the FIFO to the next               clearing the RXFOIF bit. If the UxRXB register is not
character and the next corresponding framing error.             read to open a space in the FIFO, the next character
                                                                received will be discarded and cause another overflow
The FERIF bit is cleared when the character at the top          condition.
of the FIFO does not have a framing error or when all
bytes in the receive FIFO have been read. Clearing the          A receive overflow error will generate a summary
ON bit resets the receive FIFO, thereby also clearing           UxEIF interrupt when the RXFOIE bit in the UxERRIE
the FERIF bit.                                                  register is set.

A framing error will generate a summary UxERR                   31.2.2.7     Asynchronous Reception Setup
interrupt when the FERIE bit in the UxERRIE register is
                                                                1.  Initialize the UxBRGH, UxBRGL register pair
set. The summary error is reset when the FERIF bit of
                                                                    and the BRGS bit to achieve the desired baud
the top of the FIFO is ‘0’ or when all FIFO characters
                                                                    rate (see Section 31.17 “UART Baud Rate
have been retrieved.
                                                                    Generator (BRG)”).
When FERIE is set, UxRXIF interrupts are suppressed             2. Configure the RXPPS register for the desired RX
when FERIF is ‘1’.                                                  pin
                                                                3. Clear the ANSEL bit for the RX pin (if
31.2.2.5       Receiver Parity Modes
                                                                    applicable).
Even and odd parity is automatically detected when the          4. Set the MODE[3:0] bits to the desired
MODE[3:0] bits are set to ‘0011’ and ‘0010’,                        Asynchronous mode.
respectively. Parity modes receive eight data bits and
                                                                5. Set the RXPOL bit if the data stream is inverted.
one parity bit for a total of nine bits for each character.
The PERIF bit in the UxERRIR register represents the            6. Enable the serial port by setting the ON bit.
parity error of the top unread character of the receive         7. If interrupts are desired, set the UxRXIE bit in
FIFO rather than the parity bit itself. The parity error must       the PIEx register and the GIE bits in the
be read before reading the UxRXB register advances                  INTCON0 register.
the FIFO.                                                       8. Enable reception by setting the RXEN bit.
A parity error will generate a summary UxERR interrupt          9. The UxRXIF interrupt flag bit will be set when a
when the PERIE bit in the UxERRIE register is set.The               character is transferred from the RSR to the
summary error is reset when the PERIF bit of the top of             receive buffer. An interrupt will be generated if
the FIFO is ‘0’ or when all FIFO characters have been               the UxRXIE interrupt enable bit is also set.
retrieved.                                                      10. Read the UxERRIR register to get the error
When PERIE is set, UxRXIF interrupts are suppressed                 flags.
when PERIF is ‘1’.                                              11. Read the UxRXB register to get the received
                                                                    byte.
                                                                12. If an overrun occurred, clear the RXFOIF bit.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 480
                            PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 31-5:                 ASYNCHRONOUS RECEPTION
                          Start                                       Start                                 Start
  RX pin                  bit   bit 0   bit 1         last bit Stop    bit    bit 0         last bit Stop    bit           last bit   Stop
                                                                bit                                   bit                              bit
  Rcv Shift
  Reg
  Rcv Buffer Reg.                                       Word 1                               Word 2
                                                        UxRXB                                UxRXB
     RXIDL


  Read Rcv
  Buffer Reg.
  UxRXB

  UxRXIF
  (Interrupt Flag)

  RXFOIF bit


                                                                                                                           Cleared by software

  Note:         This timing diagram shows three words appearing on the RX input. The UxRXB (receive buffer) is not read before the third word
                is received, causing the RXFOIF (FIFO overrun) bit to be set. STPMD = 0, STP[1:0] = 00.


 2017-2021 Microchip Technology Inc.                                                                                      DS40001919G-page 481
                       PIC18(L)F26/27/45/46/47/55/56/57K42
31.3     Asynchronous Address Mode                            31.3.2      ADDRESS MODE RECEIVE
A special Address Detection mode is available for use         The UART receiver is enabled for asynchronous
when multiple receivers share the same transmission           address operation by configuring the following control
line, such as in RS-485 systems.                              bits:

When Asynchronous Address mode is enabled, all                • RXEN = 1
data is transmitted and received as 9-bit characters.         • MODE[3:0] = 0100
The 9th bit determines whether the character is an            • UxBRGH:L = desired baud rate
address or data. When the 9th bit is set, the eight Least     • RXPPS = code for desired input pin
Significant bits are the address. When the 9th bit is         • Input pin ANSEL bit = 0
clear, the Least Significant bits are data. In either case,   • UxP2L = receiver address
the 9th bit is stored in PERIF when the byte is written to    • UxP3L = address mask
the receive FIFO. When PERIE is also set, the RXIF            • ON = 1
will be suppressed, thereby suspending DMA transfers          In Address mode, no data will be transferred to the
allowing software to process the received address.            input FIFO until a valid address is received. This is the
An address character will enable all receivers that           default state. Any of the following conditions will cause
match the address and disable all other receivers.            the UART to revert to the default state:
Once a receiver is enabled, all non-address characters        • ON = 0
will be received until an address character is received       • RXEN = 0
that does not match.                                          • Received address does not match
                                                              When a character with the 9th bit set is received, the
31.3.1      ADDRESS MODE TRANSMIT
                                                              Least Significant eight bits of that character will be
The UART transmitter is enabled for asynchronous              qualified by the values in the UxP2L and UxP3L
address operation by configuring the following control        registers.
bits:
                                                              The byte is XOR’d with UxP2L then AND’d with UxP3L.
• TXEN = 1                                                    A match occurs when the result is 0h, in which case,
• MODE[3:0] = 0100                                            the unaltered received character is stored in the
• UxBRGH:L = desired baud rate                                receive FIFO, thereby setting the UxRXIF interrupt bit.
• RxyPPS = code for desired output pin                        The 9th bit is stored in the corresponding PERIF bit,
• ON = 1                                                      identifying this byte as an address.
Addresses are sent by writing to the UxP1L register.          An address match also enables the receiver for all data
This transmits the written byte with the 9th bit set, which   such that all subsequent characters without the 9th bit
indicates that the byte is an address.                        set will be stored in the receive FIFO.
Data is sent by writing to the UxTXB register. This           When the 9th bit is set and a match does not occur, the
transmits the written byte with the 9th bit cleared, which    character is not stored in the receive FIFO and all
indicates that the byte is data.                              subsequent data is ignored.
To send data to a particular device on the transmission       The UxP3L register mask allows a range of addresses
bus, first transmit the address of the intended device. All   to be accepted. Software can then determine the sub-
subsequent data will be accepted only by that device          address of the range by processing the received
until an address of another device is transmitted.            address character.
Writes to UxP1L take precedence over writes to
UxTXB. When both the UxP1L and UxTXB registers
are written while the TSR is busy, the next byte to be
transmitted will be from UxP1L.
To ensure that all data intended for one device is sent
before the address is changed, wait until the TXMTIF
bit is high before writing UxP1L with the new address.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 482
                      PIC18(L)F26/27/45/46/47/55/56/57K42
31.4     DMX Mode (UART1 only)                             toggle TXEN after the last byte of the universe is
                                                           completely free of the transmit shift register as
DMX is a protocol used in stage and show equipment.        indicated by the TXMTIF bit.
This includes lighting, fog machines, motors, etc. The
protocol consists of a controller that sends out           31.4.2      DMX RECEIVER
commands, and receiver such as theater lights that
                                                           DMX Receiver mode is configured with the following
receive these commands. DMX protocol is usually
                                                           settings:
unidirectional, but can be a bidirectional protocol in
either Half or Full Duplex modes. An example of Half       • MODE[3:0] = 1010
Duplex mode is the RDM (Remote Device                      • TXEN = 0
Management) protocol that sits on DMX512A. The             • RXEN = 1
controller transmits commands and the receiver             • RXPOL = 0
receives them. Also there are no error conditions or re-   • UxP2 = number of first byte to receive
transmit mechanisms.                                       • UxP3 = number of last byte to receive
                                                           • UxBRGH:L = Value to achieve 250K baud rate
DMX, or DMX512A as it is known, consists of a
                                                           • STP[1:0] = 10 for 2 Stop bits
“Universe” of 512 channels. This means that one
                                                           • ON = 1
controller can output up to 512 bytes on a single DMX
                                                           • UxRXPPS = code for desired input pin
link. Each equipment on the line is programmed to
                                                           • Input pin ANSEL bit = 0
listen to a consecutive sequence of one or more of
these bytes.                                               When configured as DMX Receiver, the UART listens
                                                           for a Break character that is at least 23 bit periods wide.
For example, a fog machine connected to one of the
                                                           If the Break is shorter than 23 bit times, the Break is
universes may be programmed to receive one byte,
                                                           ignored and the DMX state machine remains in Idle
starting at byte number 10, and a lighting unit may be
                                                           mode. Upon receiving the Break, the DMX counters will
programmed to receive four bytes starting at byte
                                                           be reset to align with the incoming data stream.
number 22.
                                                           Immediately after the Break, the UART will see the
31.4.1      DMX CONTROLLER                                 “Mark after Break” (MAB). This space is ignored by the
                                                           UART. The Start Code follows the MAB and will always
DMX Controller mode is configured with the following       be stored in the receive FIFO.
settings:
                                                           After the Start Code, the 1st through 512th byte will be
• MODE[3:0] = 1010                                         received, but not all of them are stored in the receive
• TXEN = 1                                                 FIFO. The UART ignores all received bytes until the
• RXEN = 0                                                 ones of interest are received. This is done using the
• TXPOL = 0                                                UxP2 and UxP3 registers. The UxP2 register holds the
• UxP1 = One less than the number of bytes to              value of the byte number to start the receive process.
  transmit (excluding the Start code)                      The byte counter starts at 0 for the first byte after the
• UxBRGH:L = Value to achieve 250K baud rate               Start Code. For example, to receive four bytes starting
• STP[1:0] = 10 for two Stop bits                          at the 10th byte after the Start Code, write 009h
• RxyPPS = TX pin output code                              (9 decimal) to UxP2H:L and 00Ch (12 decimal) to
• ON = 1                                                   UxP3H:L. The receive FIFO is only 2 bytes deep,
Each DMX transmission begins with a Break followed         therefore the bytes must be retrieved by reading
by a byte called the ‘Start Code’. The width of the        UxRXB as they come in to avoid a receive FIFO
BREAK is fixed at 25 bit times. The Break is followed      overrun condition.
by a “Mark After Break” (MAB) Idle period. After this      Typically two Stop bits are inserted between bytes. If
Idle period, the 1st through ‘n’th byte is transmitted,    either Stop bit is detected as a ‘0’ then the framing error
where ‘n-1’ is the value in UxP1. See Figure 31-6.         for that byte will be set.
Software sends the Start Code and the ‘n’ data bytes by    Since the DMX sequence always starts with a Break,
writing the UxTXB register with each byte to be sent in    the software can verify that it is in sync with the
the desired order. A UxTXIF value of ‘1’ indicates when    sequence by monitoring the RXBKIF flag to ensure that
the UxTXB is ready to accept the next byte.                the next byte received after the RXBKIF is processed
The internal byte counter is not accessible to software.   as the Start Code and subsequent bytes are processed
Software needs to keep track of the number of bytes        as the expected data.
written to UxTXB to ensure that no more and no less
than ‘n’ bytes are sent because the DMX state machine
will automatically insert a Break and reset its internal
counter after ‘n’ bytes are written. One way to ensure
synchronization between hardware and software is to


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 483
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 31-6:                DMX TRANSMIT SEQUENCE

                             Start Code Byte 1                   Byte 2    Byte 3     Byte n                Start Code Byte 1
       Write to UxTXB

                                             MAB(1)
                TX pin               Break         Start Code     byte 1    byte 2             byte n   software    Break   MAB Start Code
           UxTXIF bit                                                                                    delay
      (Transmit Buffer
     Reg. Empty Flag)

           TXMTIF bit
       (Transmit Shift
     Reg. Empty Flag)

            TXEN bit
            (optional
      synchronization)

         Note   1:   The MAB period is fixed at 3-bits period.


31.5       LIN Modes (UART1 only)                                            When a Client receives data, the checksum is
                                                                             accumulated on each byte as it is received using the
LIN is a protocol used primarily in automotive                               same algorithm as the sending process. The last byte,
applications. The LIN network consists of two kinds of                       which is the inverted checksum value calculated by the
software processes: a Host process and a Client                              sending process, is added to the locally calculated
process. Each network has only one Host process and                          checksum by the UART. The check passes when the
one or more Client processes.                                                result is all ‘1’s, otherwise the check fails and the
From a physical layer point of view, the UART on one                         CERIF bit is set.
processor may be driven by both a Host and a Client                          Two methods for computing the checksum are
process, as long as only one Host process exists on the                      available: legacy and enhanced. The legacy checksum
network.                                                                     includes only the data bytes. The enhanced checksum
A LIN transaction consists of a Host process followed                        includes the PID and the data. The C0EN control bit in
by a Client process. The Client process may involve                          the UxCON2 register determines the checksum
more than one Client where one is transmitting and the                       method. Setting C0EN to ‘1’ selects the enhanced
other(s) are receiving. The transaction begins by the                        method. Software must select the appropriate method
following Host process transmission sequence:                                before the Start bit of the checksum byte is received.
1.   Break
                                                                             31.5.1       LIN HOST/CLIENT MODE
2.   Delimiter bit
                                                                             The LIN Host mode includes capabilities to generate
3.   Sync Field
                                                                             Client processes. The Host process stops at the PID
4.   PID byte                                                                transmission. Any data that is transmitted in Host/Client
The PID determines which Client processes are                                mode is done as a Client process. LIN Host/Client
expected to respond to the Host. When the PID byte is                        mode is configured by the following settings:
complete, the TX output remains in the Idle state. One                       • MODE[3:0] = 1100
or more of the Client processes may respond to the                           • TXEN = 1
Host process. If no one responds within the inter-byte                       • RXEN = 1
period, the Host is free to start another transmission.                      • UxBRGH:L = Value to achieve desired baud rate
The inter-byte period is timed by software using a                           • TXPOL = 0 (for high Idle state)
means other than the UART.                                                   • STP = desired Stop bits selection
The Client process follows the Host process. When the                        • C0EN = desired checksum mode
Client software recognizes the PID then that Client                          • RxyPPS = TX pin selection code
process responds by either transmitting the required                         • TX pin TRIS control = 0
response or by receiving the transmitted data. Only                          • ON = 1
Client processes send data. Therefore, Client
processes receiving data are receiving that of another
Client process.                                                                 Note:     The TXEN bit must be set before the Host
                                                                                          process is received and remain set while
When a Client sends data, the Client UART
                                                                                          in LIN mode whether or not the client
automatically calculates the checksum for the
                                                                                          process is a transmitter.
transmitted bytes as they are sent and appends the
inverted checksum byte to the client response.


 2017-2021 Microchip Technology Inc.                                                                              DS40001919G-page 484
                       PIC18(L)F26/27/45/46/47/55/56/57K42
The Host process is started by writing the PID to the         31.5.2.1      LIN Client Receiver
UxP1L register when UxP2 is ‘0’ and the UART is idle.
                                                              When the Client process is a receiver, the software
The UxTXIF will not be set in this case. Only the six
                                                              performs the following tasks:
Least Significant bits of UxP1L are used in the PID
transmission.                                                 • UxP3 register is written with a value equal to the
                                                                number of data bytes to receive.
The two Most Significant bits of the transmitted PID are
                                                              • C0EN bit is set or cleared to select the
PID parity bits. PID[6] is the exclusive-or of PID bits
                                                                appropriate checksum. This must be completed
0,1,2,and 4. PID[7] is the inverse of the exclusive-or of
                                                                before the Start bit of the checksum byte is
PID bits 1,3,4,and 5.
                                                                received.
The UART calculates and inserts these bits in the serial      • Each byte of the process response is read from
stream.                                                         UxRXB when UxRXIF is set.
Writing UxP1L automatically clears the UxTXCHK and            The UART updates the checksum on each received
UxRXCHK registers and generates the Break, delimiter          byte. When the last data byte is received, the computed
bit, Sync character (55h), and PID transmission portion       checksum total is stored in the UxRXCHK register. The
of the transaction. The data portion of the transaction       next received byte is saved in the receive FIFO and
that follows, if there is one, is a Client process. See       added with the value in UxRXCHK. The result of this
Section 31.5.2 “LIN Client Mode” for more details of          addition is not accessible. However, if the result is not
that process. The Host receives it’s own PID when             all ‘1’s, the CERIF bit in the UxERRIR is set. The
RXEN is set. Software performs the Client process             CERIF flag persists until cleared by software. Software
corresponding to the PID that was sent and received.          needs to read UxRXB to remove the checksum byte
Attempting to write UxP1L before an active host               from the FIFO, but the byte can be discarded if not
process is complete will not succeed. Instead, the            needed for any other purpose.
TXWRE bit will be set.
                                                              After the checksum is received, the UART ignores all
                                                              activity on the RX pin until a Break starts the next
31.5.2      LIN CLIENT MODE
                                                              transaction.
LIN Client mode is configured by the following settings:
• MODE[3:0] = 1011                                            31.5.2.2      LIN Client Transmitter
• TXEN = 1                                                    When the Client process is a transmitter, software
• RXEN = 1                                                    performs the following tasks in the order shown:
• UxP2 = Number of data bytes to transmit
                                                              • UxP2 register is written with a value equal to the
• UxP3 = Number of data bytes to receive
                                                                number of bytes to transmit. This will enable TXIF
• UxBRGH:L = Value to achieve default baud rate
                                                                flag which is disabled when UxP2 is ‘0’.
• TXPOL = 0 (for high Idle state)
                                                              • C0EN bit is set or cleared to select the
• STP = desired Stop bits selection
                                                                appropriate checksum
• C0EN = desired checksum mode
                                                              • Inter-byte delay is performed
• RxyPPS = TX pin selection code
                                                              • Each byte of the process response is written to
• TX pin TRIS control = 0
                                                                UxTXB when UxTXIF is set
• ON = 1
                                                              The UART accumulates the checksum as each byte is
The Client process starts upon detecting a Break on the
                                                              written to UxTXB. After the last byte is written, the
RX pin. The Break clears the UxTXCHK, UxRXCHK,
                                                              UART stores the calculated checksum in the
UxP2, and UxP3 registers. At the end of the Break, the
                                                              UxTXCHK register and transmits the inverted result as
auto-baud circuity is activated and the baud rate is
                                                              the last byte in the response.
automatically set using the Sync character following
the Break. The character following the Sync character         The TXIF flag is disabled when UxP2 bytes have been
is received as the PID code and is saved in the receive       written. Any writes to UxTXB that exceed the UxP2
FIFO. The UART computes the two PID parity bits from          count will be ignored and set the TXWRE flag in the
the six Least Significant bits of the PID. If either parity   UxFIFO register.
bit does not match the corresponding bit of the received
PID code, the PERIF flag is set and saved at the same
FIFO location as the PID code. The UxRXIF bit is set
indicating that the PID is available.
Software retrieves the PID by reading the UxRXB
register and determines the Client process to execute
from that. The checksum method, number of data
bytes, and whether to send or receive data, is defined
by software according to the PID code.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 485
                        PIC18(L)F26/27/45/46/47/55/56/57K42
31.6     DALI Mode (UART1 only)                                A Start bit is used to indicate the start of the forward and
                                                               backward frames. The receiver bit rate is determined
DALI is a protocol used for intelligent lighting control for   by the BRG register. The low period of the Start bit is
building automation. The protocol consists of Control          measured and is used as the timing reference for all
Devices and Control Gear. A Control Device is an               data bits in the forward and backward frames. The
application controller that sends out commands to the          ABDOVF bit is set if the Stat bit low period causes the
light fixtures. The light fixture itself is termed as a        measurement counter to overflow. All the bits following
Control Gear. The communication is done using                  the Start bit are data bits. The bit stream terminates
Manchester encoding, which is performed by the UART            when no transition is detected in the middle of a bit
hardware.                                                      period (see Figure 31-7).
Manchester encoding consists of the clock and data in          Forward and backward frames are terminated by two
a single bit stream. A high-to-low or a low-to-high            Idle bit periods or Stop bits. Normally, these start in the
transition always occurs in the middle of the bit period       first bit period of a byte. If both Stop bits are valid, the
and is not ensured to occur at the bit period                  byte reception is terminated and the CERIF bit in
boundaries. When the consecutive bits in the bit stream        UxERRIR register is set. This bit needs to be cleared in
are of the same value (i.e., consecutive '1's or               the software.
consecutive '0's), a transition occurs at the bit
boundary. However, when the bit value changes, there           If either of the Stop bits is invalid, the frame is tagged
is no transition at the bit boundary. According to the         as invalid by saving it as a null byte and setting the
standard, a half-bit time is typically 416.7 µs long. A        framing error in the receive FIFO.
double half-bit time or a single bit is typically 833.3 µs.    A framing error also occurs when no transition is
The protocol is inherently half-duplex. Communication          detected on the bus in the middle of a bit period when
over the bus occurs in the form of forward and                 the byte reception is not complete. In such a scenario,
backward frames. Wait times between the frames are             the byte will be saved with the FERIF bit.
defined in the standard to prevent collision between the
                                                               31.6.1       CONTROL DEVICE
frames.
                                                               Control Device mode is configured with the following
A Control Device transmission is termed as the forward
                                                               settings:
frame. In the DALI 2.0 standard, a forward frame can
be two or three bytes in length. The two-byte forward          • MODE = 0b1000
frame is used for communication between Control                • TXEN = 1
Device and Control Gear whereas the three-byte for-            • RXEN = 1
ward frame is used for communication between Control
                                                               • UxP1 = Forward frames are held for transmission
Devices on the bus. The first byte in the forward frame
                                                                 with this number of half-bit periods after the
is the control byte and is followed by either one or two
                                                                 completion of a forward or backward frame.
data bytes. The transaction begins when the Control
Device starts a transmission. Unlike other protocols,          • UxP2 = Forward/backward frame threshold
each byte in the frame is transmitted MSB first. Typical         delimiter. Any reception that starts this number of
frame timing is as shown in Figure 31-8.                         half bit periods after the completion of a forward or
                                                                 backward frame is detected as forward frame and
During communication between two Control Devices,                sets the PERIF flag of the corresponding received
three bytes are required to be transmitted. In this case,        byte.
the software must write the third byte to UxTXB as soon
                                                               • UxBRGH:L = Value to achieve 1200 baud rate
as UxTXIF goes True and before the output shifter
becomes empty. This ensures that the three bytes of            • TXPOL = appropriate polarity for interface circuit
the forward frame are transmitted back-to-back without         • STP = 0b10 for two Stop bits
any interruption.                                              • CERIE = 1 to enable interrupt when STP bit is
All Control Gear on the bus receive the forward frame.           received (if applicable)
If the forward frame requires a reply to be sent, one of       • RxyPPS = TX pin selection code
the Control Gear may respond with a single byte, called        • TX pin TRIS control = 0
the backward frame. The 2.0 standard requires the              • ON = 1.
Control Gear to begin transmission of the backward
                                                               A forward frame is initiated by writing the control byte to
frame between 5.5 ms to 10.5 ms (~14 to 22 half-bit
                                                               the UxTXB register. After sending the control byte,
times) after reception of the forward frame. Once the
                                                               each data byte must be written to the UxTXB register
backward frame is received by the Control Device, it is
                                                               as soon as UxTXIF goes true. It is necessary to
required to wait a minimum of 2.4 ms (~6 half-bit times).
                                                               perform every write after UxTXIF goes true, to ensure
After this wait time, the Control Device is free to
                                                               that the transmit buffer is ready to accept the byte.
transmit another forward frame (see Figure 31-9).


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 486
                        PIC18(L)F26/27/45/46/47/55/56/57K42
Each write must also occur before the TXMTIF bit goes            received (if applicable)
true, to ensure that the bit stream of forward frame is        • RxyPPS = TX pin output code
generated without an interruption.                             • TX pin TRIS control = 0
When TXMTIF goes true, indicating the transmit shift           • RXPPS = RX pin selection code
register has completed sending the last byte in the            • RX pin TRIS control = 1
frame, the TX output is held in Idle state for the number      • Input pin ANSEL bit = 0
of half-bit periods selected by the STP bits in the            • ON = 1
UxCON2 register and the CERIF bit in UxERRIR                   The UART starts listening for a forward frame when the
register is set. This bit needs to be cleared in the           Control Gear mode is entered. Only the frames that
software.                                                      follow an Idle period longer than UxP2 half-bit periods
After the last Stop bit, the TX output is held in Idle state   are detected as forward frames. Backward frames from
for an additional wait time determined by the half-bit         other Control Gear are ignored. Only forward frames
period count in the UxP1 register. For example, a 2450         will be stored in UxRXB. This is necessary because a
µs delay (~6 half-bit times) requires a value of 6 in          backward frame can be sent only as a response to a
UxP1L.                                                         forward frame.

Any writes to the UxTXB register that occur after              The forward frame is received one byte at a time in the
TXMTIF goes true, but before the UxP1 wait time                receive FIFO and retrieved by reading the UxRXB
expires, are held and then transmitted immediately             register. At the end of the forward frame, when the stop
following the wait time. If a backward frame is received       bit is received, the CERIF bit in UxERRIR register is
during the wait time, any bytes that may have been             set. This bit needs to be cleared in the software. The
written to UxTXB will be transmitted after completion of       end of the forward frame starts a timer to delay the
the backward frame reception plus the UxP1 wait time.          backward frame response by wait time equal to the
                                                               number of half-bit periods stored in UxP1.
The wait timer is reset by the backward frame and
starts over immediately following the reception of the         The data received in the forward frame is processed by
Stop bits of the backward frame. Data pending in the           the application software. If the application decides to
transmit shift register will be sent when the wait time        send a backward frame in response to the forward
elapses.                                                       frame, the value of the backward frame is written to
                                                               UxTXB. This value is held for transmission in the
To replace or delete any pending forward frame data,           transmit shift register until the wait time expires and is
the TXBE bit needs to be set to flush the shift register       then transmitted.
and transmit buffer. A new control byte can then be
written to the UxTXB register. The control byte will be        If the backward frame data is written to UxTXB after the
held in the buffer and sent at the beginning of the next       wait time has expired, it is held in the UxTXB register
forward frame following the UxP1 wait time.                    until the end of the wait time following the next forward
                                                               frame. The TXMTIF bit is false when the backward
In Control Device mode, PERIF is set when a forward            frame data is held in the transmit shift register.
frame is received. This helps the software to determine        Receiving a UxRXIF interrupt before the TXMTIF goes
whether the received byte is part of a forward frame           true indicates that the backward frame write was too
from a Control Device (either from the Control Device          late and another forward frame was received before
under consideration or from another Control Device on          sending the backward frame. The pending backward
the bus) or a backward frame from a Control Gear.              frame has to be flushed by setting the TXBE bit, to
                                                               prevent it from being sent after the next Forward
31.6.2      CONTROL GEAR                                       Frame.
The Control Gear mode is configured with the following
settings:
• MODE = 0b1001
• TXEN = 1
• RXEN = 1
• UxP1 = Back Frames are held for transmission
  this number of half-bit periods after the completion
  of a Forward Frame.
• UxP2 = Forward/Back Frame threshold delimiter.
  Idle periods more than this number of half-bit
  periods are detected as Forward Frames.
• UxBRGH:L = Value to achieve 1200 baud rate
• TXPOL = appropriate polarity for interface circuit
• RXPOL = same as TXPOL
• STP = 0b10 for two Stop bits
• CERIE = 1 to enable interrupt when STP bit is


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 487
                            PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 31-7:                 MANCHESTER TIMING
                              byte0      byte1
    Write to UxTXB
                                   Start                      byte0                             byte1              Stop bit(s)          idle       Start
                                    bit                                                                                                             bit
            TX pin
                                               b7=1 b6=0      b5=0     b4=1   b0=1    b7=0      b6=1      b0=0
        UxTXIF bit
   (Transmit Buffer
  Reg. Empty Flag)

        TXMTIF bit
    (Transmit Shift
  Reg. Empty Flag)


FIGURE 31-8:                 DALI FRAME TIMING
                              Control                                                                                        Control
                                         Byte 1                                                                              Code      Byte 1
                              Code
    Write to UxTXB

                                   Start bit                                                                     Stop bits       wait period    Start bit
            TX pin                                CC[7]        CC[6]      CC[0]      byte1[7]       byte1[0]
        UxTXIF bit
   (Transmit Buffer
  Reg. Empty Flag)

        TXMTIF bit
    (Transmit Shift
  Reg. Empty Flag)


FIGURE 31-9:                 DALI FORWARD/BACK FRAME TIMING

                                        forward wait period                                               forward wait period
   Device TX          Forward Frame                           Forward Frame                                                        Forward Frame


     Gear TX                                                                              Back Frame
                                                              back wait period
       Gear
 UxTXB Write


31.7      General Purpose Manchester                                                 • STP = desired number of stop periods
          (UART1 only)                                                               • RxyPPS = TX pin selection code
                                                                                     • TX pin TRIS control = 0
General purpose Manchester is a subset of the DALI                                   • RXPPS = RX pin selection code
mode. When the UxP1L register is cleared, there is no                                • RX pin TRIS control = 1
minimum wait time between frames. This allows full                                   • Input pin ANSEL bit = 0
and half-duplex operation because writes to the UxTXB                                • ON = 1
are not held waiting for a receive operation to complete.
                                                                                     The Manchester bit stream timing is shown in
General purpose Manchester operation maintains all                                   Figure 31-7.
other aspects of DALI mode such as:
• Single-pulse Start bit
• Most Significant bit first
• No stop periods between back-to-back bytes
General purpose Manchester mode is configured with
the following settings:
• MODE[3:0] = 1000
• TXEN = 1
• RXEN = 1
• UxP1 = 0h
• UxBRGH:L = desired baud rate
• TXPOL and RXPOL = desired Idle state


 2017-2021 Microchip Technology Inc.                                                                                              DS40001919G-page 488
                       PIC18(L)F26/27/45/46/47/55/56/57K42
31.8     Polarity
Receive and transmit polarity is user selectable and
affects all modes of operation.
The idle level is programmable with the polarity control
bits in the UxCON2 register. The control bits default to
‘0’, which select a high idle level. The low level Idle
state is selected by setting the control bit to ‘1’. TXPOL
controls the TX idle level. RXPOL controls the RX idle
level.


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 489
                        PIC18(L)F26/27/45/46/47/55/56/57K42
31.9      Stop Bits                                             31.11 Receive and Transmit Buffers
The number of Stop bits is user selectable with the STP         The UART uses small buffer areas to transmit and
bits in the UxCON2 register.The STP bits affect all             receive data. These are sometimes referred to as
modes of operation.                                             FIFOs.
Stop bits selections include:                                   The receiver has a Receive Shift Register (RSR) and
• 1 transmit with receive verify on first                       two buffer registers. The buffer at the top of the FIFO
• 1.5 transmit with receive verify on first                     (earliest byte to enter the FIFO) is by retrieved by
• 2 transmit with receive verify on both                        reading the UxRXB register.
• 2 transmit with receive verify on first only                  The transmitter has one Transmit Shift Register (TSR)
In all modes, except DALI, the transmitter is idle for the      and one buffer register. Writes to UxTXB go to the
number of Stop bit periods between each consecutively           transmit buffer then immediately to the TSR, if it is
transmitted word. In DALI, the Stop bits are generated          empty. When the TSR is not empty, writes to UxTXB
after the last bit in the transmitted data stream.              are held then transferred to the TSR when it becomes
                                                                available.
The input is checked for the idle level in the middle of
the first Stop bit, when receive verify on first is selected,   31.11.1     FIFO STATUS
as well as in the middle of the second Stop bit, when
                                                                The UxFIFO register contains several status bits for
verify on both is selected. If any Stop bit verification
                                                                determining the state of the receive and transmit
indicates a non-idle level, the framing error FERIF bit is
                                                                buffers.
set for the received word.
                                                                The RXBE bit indicates that the receive FIFO is empty.
31.9.1       DELAYED UXRXIF                                     This bit is essentially the inverse of UxRXIF. The RXBF
When operating in Half Duplex mode, where the                   bit indicates that the receive FIFO is full.
microcontroller needs to reverse the transceiver                The transmitter has only one buffer register so the
direction after a reception, it may be more convenient          status bits are essentially a copy and inverse of the
to hold off the UxRXIF interrupt until the end of the Stop      UxTXIF bit. The TXBE bit indicates that the buffer is
bits to avoid line contention. The user selects when the        empty (same as UxTXIF) and the TXBF bit indicates
UxRXIF interrupt occurs with the STPMD bit in the               that the buffer is full (UxTXIF inverse). A third
UxFIFO register. When STPMD is ‘1’, the UxRXIF                  transmitter status bit, TXWRE (transmit write error), is
occurs at the end of the last Stop bit. When STPMD is           set whenever a UxTXB write is performed when the
‘0’, UxRXIF occurs when the received byte is stored in          TXBF bit is set. This indicates that the write was
the receive FIFO. When STP[1:0] = 10, the store                 unsuccessful.
operation is performed in the middle of the second Stop
bit, otherwise, it is performed in the middle of the first      31.11.2     FIFO RESET
Stop bit. The FERIF and PERIF interrupts are not                All modes support resetting the receive and transmit
delayed with STPMD. Only UxRXIF is delayed when                 buffers.
STPMD is set and may be the only indicator for
reversing transceiver direction.                                The receive buffer is flushed and all unread data
                                                                discarded when the RXBE bit in the UxFIFO register is
                                                                written to ‘1’. The MOVWF instruction with the TXBE bit
31.10 Operation after FIFO overflow                             cleared may be used to avoid inadvertently clearing a
The Receive Shift Register (RSR) can be configured to           byte pending in the TSR when UxTXB is empty.
stop or continue running during a receive FIFO                  Data written to UxTXB when TXEN is low will be held in
overflow condition. Stopped operation is the Legacy             the Transmit Shift Register (TSR) then sent when
mode.                                                           TXEN is set. The transmit buffer and inactive TSR are
When the RSR continues to run during an overflow                flushed by setting the TXBE bit in the UxFIFO register.
condition, the first word received after clearing the           Setting TXBE while a character is actively transmitting
overflow will always be valid.                                  from the TSR will complete the transmission without
                                                                being flushed.
When the RSR is stopped during an overflow condition,
synchronization with the Start bits is lost. Therefore, the     Clearing the ON bit will discard all received data and
first word received after the overflow is cleared may           transmit data pending in the TSR and UxTXB.
start in the middle of a word.
Operation during overflow is selected with the
RUNOVF bit in the UxCON2 register. Setting the
RUNOVF bit selects the run during overflow method.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 490
                      PIC18(L)F26/27/45/46/47/55/56/57K42
31.12 Flow Control                                         FIGURE 31-10:          FLOW CONTROL
This section does not apply to the LIN, DALI, or DMX                 UART 1                   UART 2
modes.                                                                (DTE)                    (DTE)
Flow control is the means by which a sending UART
data stream can be suspended by a receiving UART.
                                                                            RX                 TX
Flow control prevents input buffers from overflowing
without software intervention. The UART supports both
                                                                           RTS                 CTS
hardware and XON/XOFF methods of flow control.
The flow control method is selected with the FLO[1:0]
                                                                            TX                 RX
bits in the UxCON2 register. Flow control is disabled
when are both bits are cleared.                                            CTS                 RTS

31.12.1     HARDWARE FLOW CONTROL
Hardware flow control is selected by setting the           31.12.2       RS-485 TRANSCEIVER CONTROL
FLO[1:0] bits to ‘10’.
                                                           Hardware flow control can be used to control the
Hardware flow control consists of three lines. The RS-     direction of an RS-485 transceiver as shown in
232 signal names for two of these are RTS, and CTS.        Figure 31-11. Configure the CTS input to be always
Both are low true. The third line may be used to control   enabled by setting the UxCTSPPS selection to an
an RS-485 transceiver. The signal name for this is         unimplemented port pin such as RD0. When the signal
TXDE for transmit drive enable. This output is high        and control lines are configured as shown in Figure 31-
when the TX output is actively sending a character and     11, then the UART will not receive its own
low at all other times. The UART is configured as DTE      transmissions. To verify that there are no collisions on
(computer) equipment which means RTS is an output          the RS-485 lines then the transceiver RE control can
and CTS is an input.                                       be disconnected from TXDE and tied low thereby
The RTS and CTS signals work as a pair to control the      enabling loop-back reception of all transmissions. See
transmission flow. A DTE-to-DTE configuration              Section 31.14 “Collision Detection (UART1 Only)”
connects the RTS output of the receiving UART to the       for more information.
CTS input of the sending UART. Refer to Figure 31-10.
The UART receiving data asserts the RTS output low         FIGURE 31-11:          RS-485 CONFIGURATION
when the input FIFO is empty. When a character is
received, the RTS output goes high until the UxRXB is
read to free up both FIFO locations.                                     UART                             VCC
When the CTS input goes high after a byte has started
to transmit, the transmission will complete normally.
The receiver accommodates this by accepting the                            RX                 R              4k7
character in the second FIFO location even when the                (1)                        RE     A
CTS input is high.                                                       TXDE
                                                                                              DE     B
                                                                           TX                 D              4k7
                                                                                             SN75176
                                                                                                         Gnd


                                                             Note 1:      Configure UxCTSPPS to an
                                                                          unimplemented input such as RD0
                                                                          (UxCTSPPS = 0x18).


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 491
                      PIC18(L)F26/27/45/46/47/55/56/57K42
31.12.3     XON/XOFF FLOW CONTROL
XON/XOFF flow control is selected by setting the
FLO[1:0] bits to ‘01’.
XON/XOFF is a data based flow control method. The
signals to suspend and resume transmission are
special characters sent by the receiver to the
transmitter The advantage is that additional hardware
lines are not needed.
XON/XOFF flow control requires full duplex operation
because the transmitter must be able to receive the
signal to suspend transmitting while the transmission is
in progress. Although XON and XOFF are not defined
in the ASCII code, the generally accepted values are
13h for XOFF and 11h for XON. The UART uses those
codes.
The transmitter defaults to XON, or transmitter
enabled. This state is also indicated by the read-only
XON bit in the UxFIFO register.
When an XOFF character is received, the transmitter
stops transmitting after completing the character
actively being transmitted. The transmitter remains
disabled until an XON character is received.
XON will be forced on when software toggles the TXEN
bit.
When the RUNOVF bit in the UxCON2 register is set
then XON and XOFF characters continue to be
received and processed without the need to clear the
input FIFO by reading the UxRXB. However, if the
RUNOVF bit is clear then the UxRXB must be read to
avoid a receive overflow which will suspend flow
control when the receive buffer overflows.


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 492
                       PIC18(L)F26/27/45/46/47/55/56/57K42
31.13 Checksum (UART1 only)                                 The TXCIF flag in the UxERRIR register is used to
                                                            signal collisions. This signal is only useful when the TX
This section does not apply to the LIN mode, which          output is looped back to the RX input and everything
handles checksums automatically.                            that is transmitted is expected to be received. If more
The transmit and receive checksum adders are                than one transmitter is active at the same time, it can
enabled when the C0EN bit in the UxCON2 register is         be assumed that the TX word will not match the RX
set. When enabled, the adders accumulate every byte         word. The TXCIF detects this mismatch and flags an
that is transmitted or received. The accumulated sum        interrupt. The TXCIF bit will also be set in DALI mode
includes the carry of the addition. Software is             transmissions when the received bit is missing the
responsible for clearing the checksum registers before      expected mid-bit transition.
a transaction and performing the check at the end of        Collision detection is always active, regardless of
the transaction.                                            whether or not the RX input is connected to the TX
The following is an example of how the checksum             output. It is up to the user to disable the TXCIE bit when
registers could be used in the Asynchronous modes.          collision interrupts are not required.
                                                            The software overhead of unloading the receive buffer
31.13.1     TRANSMIT CHECKSUM METHOD                        of transmitted data is avoided by setting the RUNOVF
1.   Clear the UxTXCHK register.                            bit in UxCON2 and ignoring the receive interrupt and
2.   Set the C0EN bit.                                      letting the receive buffer overflow. When the
3.   Send all bytes of the transaction output.              transmission is complete, prepare for receiving data by
                                                            flushing the receive buffer (see Section 31.11.2, FIFO
4.   Invert UxTXCHK and send the result as the last
                                                            Reset) and clearing the RXFOIF overflow flag in the
     byte of the transaction.
                                                            UxERRIR register.
31.13.2     RECEIVE CHECKSUM METHOD
                                                            31.15 RX/TX Activity Timeout
1.   Clear the UxRXCHK register.
2.   Set the C0EN bit.                                      The UART works in conjunction with the HLT timers to
3.   Receive all bytes in the transaction including the     monitor activity on the RX and TX lines. Use this
     checksum byte.                                         feature to determine when there has been no activity
                                                            on the receive or transmit lines for a user specified
4.   Set MSb of UxRXCHK if 7-bit mode is selected.
                                                            period of time.
5.   Add 1 to UxRXCHK.
                                                            To use this feature, set the HLT to the desired timeout
6.   If the result is ‘0’, the checksum passes,
                                                            period by a combination of the HLT clock source, timer
     otherwise it fails.
                                                            prescale value, and timer period registers. Configure
                                                            the HLT to reset on the UART TX or RX line and start
31.14 Collision Detection (UART1 Only)                      the HLT at the same time the UART is started. UART
External forces that interfere with the transmit line are   activity will keep resetting the HLT to prevent a full HLT
detected in all modes of operation with collision           period from elapsing. When there has been no activity
detection. Collision detection is always active when        on the selected TX or RX line for longer than the HLT
RXEN and TXEN are both set.                                 period then an HLT interrupt will occur signaling the
                                                            timeout event.
When the receive input is connected to the transmit
output through either the same I/O pin or external          For example, the following register settings will
circuitry, a character will be received for every           configure HLT2 for a 5 ms timeout of no activity on
character transmitted. The collision detection circuit      U1RX:
provides a warning when the word received does not          • T2PR = 0x9C (156 prescale periods)
match the word transmitted.                                 • T2CLKCON = 0x05 (500 kHz internal oscillator)
                                                            • T2HLT = 0x04 (free running, reset on rising edge)
                                                            • T2RST = 0x15 (reset on U1RX)
                                                            • T2CON = 0xC0 (Timer2 on with 1:16 prescale)


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 493
                       PIC18(L)F26/27/45/46/47/55/56/57K42
31.16 Clock Accuracy with                                    EXAMPLE 31-1:                               CALCULATING BAUD
      Asynchronous Operation                                                                             RATE ERROR
The factory calibrates the internal oscillator block         For a device with FOSC of 16 MHz, desired baud rate
output (INTOSC). However, the INTOSC frequency               of 9600, Asynchronous mode, BRGS = 0:
may drift as VDD or temperature changes, and this
directly affects the asynchronous baud rate. Two
methods may be used to adjust the baud rate clock, but                                                           F O SC
                                                                            D esired Baud Rate = --------------------------------------------
both require a reference clock source of some kind.                                              16 [U xBRG ] + 1
The first (preferred) method uses the OSCTUNE                                                                            F O SC
register to adjust the INTOSC output. Adjusting the                                                      ---------------------------------------------
                                                                                                         D esired Baud Rate
value of the OSCTUNE register allows for fine resolution                                             X = ---------------------------------------------– 1
                                                                                                                                 16
changes to the system clock source. See Section
7.2.2.3 “Internal Oscillator Frequency Adjustment”                                                           16000000
                                                                                                             --------------------------
for more information.                                                                                               9600
                                                                                                           = -------------------------- – 1
The other method adjusts the value of the Baud Rate                                                                    16
Generator. This can be done automatically with the
Auto-Baud      Detect     feature  (see     Section                                                       =  103.17 = 103
31.17.1 “Auto-Baud Detect”). There may not be fine
enough resolution when adjusting the Baud Rate
                                                                                                                               16000000
Generator to compensate for a gradual change of the                 C alculated Baud Rate = ------------------------------
                                                                                            16 103 + 1
peripheral clock frequency.
                                                                                                                        = 9615
31.17 UART Baud Rate Generator (BRG)
                                                                               Calc.Baud Rate – D esired Baud Rate
The Baud Rate Generator (BRG) is a 16-bit timer that                   Error = --------------------------------------------------------------------------------------------
                                                                                                      D esired Baud Rate
is dedicated to the support of the UART operation.
The UxBRGH, UxBRGL register pair determines the                                           9615 – 9600
period of the free running baud rate timer. The multiplier                             = ------------------------------------- = 0.16%
                                                                                                       9600
of the baud rate period is determined by the BRGS bit in
the UxCON0 register.
Table 31-1 contains the formulas for determining the
                                                             TABLE 31-1:                      BAUD RATE FORMULAS
baud rate. Example 31-1 provides a sample calculation
for determining the baud rate and baud rate error.            BRGS              BRG/UART Mode                                      Baud Rate Formula

The high baud rate range (BRGS = 1) is intended to              1                        High Rate                                        FOSC/[4 (n+1)]
extend the baud rate range up to a faster rate when the
                                                                0                     Normal Rate                                         FOSC/[16(n+1)]
desired baud rate is not possible otherwise. Using the
normal baud rate range (BRGS = 0) is recommended             Legend:         n = value of UxBRGH, UxBRGL register pair.
when the desired baud rate is achievable with either
range.
Writing a new value to the UxBRGH, UxBRGL register
pair causes the BRG timer to be reset (or cleared). This
ensures that the BRG does not wait for a timer overflow
before outputting the new baud rate.
If the system clock is changed during an active receive
operation, a receive error or data loss may result. To
avoid this problem, check the status of the RXIDL bit to
make sure that the receive operation is idle before
changing the system clock.


 2017-2021 Microchip Technology Inc.                                                                                           DS40001919G-page 494
                            PIC18(L)F26/27/45/46/47/55/56/57K42
31.17.1        AUTO-BAUD DETECT                                                left in the UxBRGH, UxBRGL register pair, the ABDEN
                                                                               bit is automatically cleared and the ABDIF interrupt flag
The UART module supports automatic detection and
                                                                               is set. ABDIF must be cleared by software.
calibration of the baud rate in the 8-bit Asynchronous
and LIN modes. However, setting ABDEN to start auto-                           RXIDL indicates that the sync input is active. RXIDL will
baud detection is neither necessary, nor possible in LIN                       go low on the first falling edge and go high on the fifth
mode because that mode supports auto-baud detec-                               rising edge.
tion automatically at the beginning of every data                              The BRG auto-baud clock is determined by the BRGS
packet. Enabling auto-baud detect with the ABDEN bit                           bit as shown in Table 31-2. During ABD, the internal
applies to the Asynchronous modes only.                                        BRG register is used as a 16-bit counter. However, the
  Note:        In DALI Mode, ABDEN is ignored. The                             UxBRGH and UxBRGL registers retain the previous
               baud rate needs to be manually set to                           BRG value until the auto-baud process is successfully
               1200 using the BRG registers.                                   completed. While calibrating the baud rate period, the
                                                                               internal BRG register is clocked at 1/8th the BRG base
When Auto-Baud Detect (ABD) is active, the clock to                            clock rate. The resulting byte measurement is the
the BRG is reversed. Rather than the BRG clocking the                          average bit time when clocked at full speed and is
incoming RX signal, the RX signal is timing the BRG.                           transferred to the UxBRGH and UxBRGL registers
The Baud Rate Generator is used to time the period of                          when complete.
a received 55h (ASCII “U”), which is the Sync character
for the LIN bus. The unique feature of this character is                           Note 1: If the WUE bit is set with the ABDEN bit,
that it has five falling edges, including the Start bit edge,                              auto-baud detection will occur on the byte
five rising edges including the Stop bit edge.                                             following the Break character (see Sec-
                                                                                           tion     31.17.3 “Auto-Wake-up         on
In 8-bit Asynchronous mode, setting the ABDEN bit in                                       Break”).
the UxCON0 register enables the auto-baud calibration
sequence. The first falling edge of the RX input after                                      2: It is up to the user to determine that the
ABDEN is set will start the auto-baud calibration                                              incoming character baud rate is within the
sequence. While the ABD sequence takes place, the                                              range of the selected BRG clock source.
UART state machine is held in idle. On the first falling                                       Some combinations of oscillator frequency
edge of the receive line, the UxBRG begins counting up                                         and UART baud rates are not possible.
using the BRG counter clock as shown in Figure 31-12.
The fifth falling edge will occur on the RX pin at the                         TABLE 31-2:             BRG COUNTER CLOCK RATES
beginning of the bit 7 period. At that time, an                                    BRGS         BRG Base Clock            BRG ABD Clock
accumulated value totaling the proper BRG period is
                                                                                      1               FOSC/4                   FOSC/32
                                                                                      0              FOSC/16                   FOSC/128

FIGURE 31-12:                AUTOMATIC BAUD RATE CALIBRATION

    BRG Value         XXXXh             0000h                                                                             001Ch

                                                    Edge #1          Edge #2           Edge #3        Edge #4        Edge #5
        RX pin                                     Start  bit 0     bit 1  bit 2      bit 3  bit 4   bit 5  bit 6   bit 7  Stop bit


   BRG Clock

                   Set by User                                                                                          Auto Cleared
                   in 8-bit mode
    ABDEN bit

         RXIDL

     ABDIF bit
     (Interrupt)
                                                                                                                     Cleared by software
       UxBRG                                                XXXXh                                                         001Ch


       Note 1:     Auto-baud is supported in LIN and 8-bit Asynchronous modes only.


 2017-2021 Microchip Technology Inc.                                                                                  DS40001919G-page 495
                        PIC18(L)F26/27/45/46/47/55/56/57K42
31.17.2      AUTO-BAUD OVERFLOW                                31.17.3.1      Special Considerations
During the course of automatic baud detection, the             Break Character
ABDOVF bit in the UxERRIR register will be set if the          To avoid character errors or character fragments during
baud rate counter overflows before the fifth falling edge      a wake-up event, the wake-up character must be all
is detected on the RX pin. The ABDOVF bit indicates            zeros.
that the counter has exceeded the maximum count that
can fit in the 16 bits of the UxBRGH:UxBRGL register           When the wake-up is enabled, the function works
pair. After the ABDOVF bit has been set, the state             independent of the low time on the data stream. If the
machine continues to search until the fifth falling edge       WUE bit is set and a valid non-zero character is
is detected on the RX pin. Upon detecting the fifth            received, the low time from the Start bit to the first rising
falling RX edge, the hardware will set the ABDIF               edge will be interpreted as the wake-up event. The
interrupt flag and clear the ABDEN bit in the UxCON0           remaining bits of the character will be received as a
register. The UxBRGH and UxBRGL register values                fragmented character and subsequent characters can
retain their previous value. The ABDIF flag in the             result in framing or overrun errors.
UxUIR register and ABDOVF flag in the UxERRIR                  Therefore, the initial character of the transmission must
register can be cleared by software directly. To               be all zeros. This must be eleven or more bit times, 13-
generate an interrupt on an auto-baud overflow                 bit times recommended for LIN bus, or any number of
condition, all the following bits must be set:                 bit times for standard RS-232 devices.
• ABDOVE bit in the UxERRIE register                           Oscillator Start-up Time
• UxEIE bit in the PIEx register
                                                               Oscillator start-up time must be considered, especially
• PIE and GIE bits in the INTCON register
                                                               in applications using oscillators with longer start-up
To terminate the auto-baud process before the ABDIF            intervals (i.e., LP, XT or HS/PLL modes). The Sync
flag is set, clear the ABDEN bit, then clear the ABDOVF        Break (or wake-up signal) character must be of
bit in the UxERRIR register.                                   sufficient length, and be followed by a sufficient
                                                               interval, to allow enough time for the selected oscillator
31.17.3     AUTO-WAKE-UP ON BREAK                              to start and provide proper initialization of the UART.
During Sleep mode, all clocks to the UART are                  WUE Bit
suspended. Because of this, the Baud Rate Generator
                                                               To ensure that no actual data is lost, check the RXIDL
is inactive and a proper character reception cannot be
                                                               bit to verify that a receive operation is not in process
performed. The Auto-Wake-up feature allows the
                                                               before setting the WUE bit. If a receive operation is not
controller to wake up due to activity on the RX line.
                                                               occurring, the WUE bit may then be set just prior to
The Auto-Wake-up feature is enabled by setting both the        entering the Sleep mode.
WUE bit in the UxCON1 register and the UxIE bit in the
PIEx register. Once set, the normal receive sequence on
RX is disabled, and the UART remains in an Idle state,
monitoring for a wake-up event independent of the CPU
mode. A wake-up event consists of a transition out of the
Idle state on the RX line. (This coincides with the start of
a Break or a wake-up signal character for the LIN
protocol.)
The UART module generates a WUIF interrupt
coincident with the wake-up event. The interrupt is
generated synchronously to the Q clocks in normal CPU
operating modes (Figure 31-13), and asynchronously, if
the device is in Sleep mode (Figure 31-14). The
interrupt condition is cleared by clearing the WUIF bit in
the UxUIR register. To generate an interrupt on a wake-
up event, all the following bits must be set:
• UxIE bit in the PIEx register
• PIE and GIE bits in the INTCON register
The WUE bit is automatically cleared by the transition
to the Idle state on the RX line at the end of the Break.
This signals to the user that the Break event is over. At
this point, the UART module is in Idle mode, waiting to
receive the next character.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 496
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 31-13:                AUTO-WAKE-UP BIT (WUE) TIMING DURING NORMAL OPERATION
             Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4
    OSC1
               Bit set by user                                                                                                     Auto Cleared
   WUE bit
   RX Line

     WUIF
                                                                                                             Cleared by software

  Note 1:    The UART remains in idle while the WUE bit is set.


FIGURE 31-14:                AUTO-WAKE-UP BIT (WUE) TIMINGS DURING SLEEP

             Q1Q2 Q3 Q4 Q1Q2 Q3 Q4 Q1Q2 Q3 Q4                     Q1              Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1Q2 Q3 Q4
     OSC1
               Bit Set by User                                                                                                 Auto Cleared
   WUE bit
   RX Line
                                                                                                                    Note 1
     WUIF
                                                                                                           Cleared by software
                        Sleep Command Executed                     Sleep Ends

  Note 1:    If the wake-up event requires long oscillator warm-up time, the automatic clearing of the WUE bit can occur while the stposc signal is
             still active. This sequence may not depend on the presence of Q clocks.
       2:    The UART remains in idle while the WUE bit is set.


31.18 Transmitting a Break                                                      31.19 Receiving a Break
The UART module has the capability of sending either                            The UART has counters to detect when the RX input
a fixed length Break period or a software timed Break                           remains in the space state for an extended period of
period. The fixed length Break consists of a Start bit,                         time. When this happens, the RXBKIF bit in the
followed by 12 ‘0’ bits and a Stop bit. The software                            UxERRIR register is set.
timed Break is generated by setting and clearing the                            A Break is detected when the RX input remains in the
BRKOVR bit in the UxCON1 register.                                              space state for 11 bit periods for asynchronous and LIN
To send the fixed length Break, set the SENDB and                               modes, and 23 bit periods for DMX mode.
TXEN bits in the UxCON0 register. The Break                                     The user can select to receive the Break interrupt as
sequence is then initiated by a write to UxTXB. The                             soon as the Break is detected or at the end of the
timed Break will occur first, followed by the character                         Break, when the RX input returns to the Idle state.
written to UxTXB that initiated the Break. The initiating                       When the RXBIMD bit in the UxCON1 is ‘1’ then
character is typically the Sync character of the LIN                            RXBKIF is set immediately upon Break detection.
specification.                                                                  When RXBIMD is ‘0’ then RXBKIF is set when the RX
SENB is disabled in the LIN and DMX modes because                               input returns to the Idle state.
those modes generate the Break sequence
automatically.                                                                  31.20 UART Operation During Sleep
The SENDB bit is automatically reset by hardware after
                                                                                The UART ceases to operate during Sleep. The safe
the Break Stop bit is complete.
                                                                                way to wake the device from Sleep by a serial
The TXMTIF bit in the UxERRIR register indicates when                           operation is to use the Wake-on-Break feature of the
the transmit operation is active or idle, just as it does                       UART. See Section 31.17.3, Auto-Wake-up on Break
during normal transmission. See Figure 31-15 for the
timing of the Break sequence.


 2017-2021 Microchip Technology Inc.                                                                                   DS40001919G-page 497
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 31-15:          SEND BREAK CHARACTER SEQUENCE

   Write to UxTXB
                           Sync Write

      BRG Output
      (Shift Clock)

           TX (pin)                     Start bit   bit 0   bit 1    bit 11              Sync start
                                                                              Stop bit
                                                             Break
        UxTXIF bit
         (Transmit
    Interrupt Flag)
        TXMTIF bit
    (Transmit Shift
      Empty Flag)
                                                                         Auto Cleared
          SENDB
      (send Break
        control bit)


 2017-2021 Microchip Technology Inc.                                              DS40001919G-page 498
                          PIC18(L)F26/27/45/46/47/55/56/57K42
31.21 Register Definitions: UART Control
Long bit name prefixes for the UART peripherals are
shown below. Refer to Section 1.3 “Register and Bit
naming conventions”for more information.


          Peripheral                  Bit Name Prefix
            UART 1                           U1
            UART 2                           U2

REGISTER 31-1:             UxCON0: UART CONTROL REGISTER 0
    R/W-0/0         R/W/HS/HC-0/0        R/W-0/0             R/W-0/0     R/W-0/0         R/W-0/0            R/W-0/0      R/W-0/0
        BRGS            ABDEN              TXEN              RXEN                               MODE[3:0]
bit 7                                                                                                                           bit 0


Legend:
R = Readable bit                      W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                  x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                      ‘0’ = Bit is cleared             HC = Hardware clear


bit 7              BRGS: Baud rate Generator Speed Select bit
                   1 = Baud rate generator is high speed with 4 baud clocks per bit
                   0 = Baud rate generator is normal speed with 16 baud clocks per bit
bit 6              ABDEN: Auto-baud Detect Enable bit(3)
                   1 = Auto-baud is enabled. Receiver is waiting for Sync character (0x55)
                   0 = Auto-baud is not enabled or auto-baud is complete
bit 5              TXEN: Transmit Enable Control bit(2)
                   1 = Transmit is enabled. TX output pin drive is forced on when transmission is active, and controlled by PORT TRIS
                       control when transmission is idle.
                   0 = Transmit is disabled. TX output pin drive is controlled by PORT TRIS control
bit 4              RXEN: Receive Enable Control bit(2)
                   1 = Receiver is enabled
                   0 = Receiver is disabled
bit 3-0            MODE[3:0]: UART Mode Select bits(1)
                   1111 = Reserved
                   1110 = Reserved
                   1101 = Reserved
                   1100 = LIN Host/Client mode(4)
                   1011 = LIN Client-Only mode(4)
                   1010 = DMX mode(4)
                   1001 = DALI Control Gear mode(4)
                   1000 = DALI Control Device mode(4)
                   0111 = Reserved
                   0110 = Reserved
                   0101 = Reserved
                   0100 = Asynchronous 9-bit UART Address mode. 9th bit: 1 = address, 0 = data
                   0011 = Asynchronous 8-bit UART mode with 9th bit even parity
                   0010 = Asynchronous 8-bit UART mode with 9th bit odd parity
                   0001 = Asynchronous 7-bit UART mode
                   0000 = Asynchronous 8-bit UART mode

Note 1:        Changing the UART MODE while ON = 1 may cause unexpected results.
     2:        Clearing TXEN or RXEN will not clear the corresponding buffers. Use TXBE or RXBE to clear the buffers.
     3:        When MODE = 100x, then ABDEN bit is ignored.
     4:        UART1 only.


 2017-2021 Microchip Technology Inc.                                                                         DS40001919G-page 499
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-2:           UxCON1: UART CONTROL REGISTER 1
   R/W-0/0             U-0              U-0       R/W/HC-0/0      R/W-0/0        U-0          R/W-0/0       R/W/HC-0/0
        ON              —               —                WUE     RXBIMD           —           BRKOVR          SENDB
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         HC = Hardware clear


bit 7              ON: Serial Port Enable bit
                   1 = Serial port enabled
                   0 = Serial port disabled (held in Reset)
bit 6-5            Unimplemented: Read as ‘0’
bit 4              WUE: Wake-up Enable bit
                   1 = Receiver is waiting for falling RX input edge which will set the UxIF bit. Cleared by hardware on
                       wake event. Also requires UxIE bit of PIEx to enable wake
                   0 = Receiver operates normally
bit 3              RXBIMD: Receive Break Interrupt Mode Select bit
                   1 = Set RXBKIF immediately when RX in has been low for the minimum Break time
                   0 = Set RXBKIF on rising RX input after RX in has been low for the minimum Break time
bit 2              Unimplemented: Read as ‘0’
bit 1              BRKOVR: Send Break Software Override bit
                   1 = TX output is forced to non-idle state
                   0 = TX output is driven by transmit shift register
bit 0              SENDB: Send Break Control bit(1)
                   1 = Output Break upon UxTXB write. Written byte follows Break. Bit is cleared by hardware.
                   0 = Break transmission completed or disabled

Note 1:      This bit is read-only in LIN, DMX, and DALI modes.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 500
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-3:           UxCON2: UART CONTROL REGISTER 2
   R/W-0/0            R/W-0/0        R/W-0/0         R/W-0/0       R/W-0/0       R/W-0/0        R/W-0/0       R/W-0/0
   RUNOVF             RXPOL                 STP[1:0]                C0EN          TXPOL                 FLO[1:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              RUNOVF: Run During Overflow Control bit
                   1 = RX input shifter continues to synchronize with Start bits after overflow condition
                   0 = RX input shifter stops all activity on receiver overflow condition
bit 6              RXPOL: Receive Polarity Control bit
                   1 = Invert RX polarity, Idle state is low
                   0 = RX polarity is not inverted, Idle state is high
bit 5-4            STP[1:0]: Stop Bit Mode Control bits(1)
                   11 = Transmit 2 Stop bits, receiver verifies first Stop bit
                   10 = Transmit 2 Stop bits, receiver verifies first and second Stop bits
                   01 = Transmit 1.5 Stop bits, receiver verifies first Stop bit
                   00 = Transmit 1 Stop bit, receiver verifies first Stop bit
bit 3              C0EN: Checksum Mode Select bit(2)
                   LIN mode:
                   1 = Checksum Mode 1, enhanced LIN checksum includes PID in sum
                   0 = Checksum Mode 0, legacy LIN checksum does not include PID in sum
                   Other modes:
                   1 = Add all TX and RX characters
                   0 = Checksums disabled
bit 2              TXPOL: Transmit Polarity Control bit
                   1 = Output data is inverted, TX output is low in Idle state
                   0 = Output data is not inverted, TX output is high in Idle state
bit 1-0            FLO[1:0]: Handshake Flow Control bits
                   11 = Reserved
                   10 = RTS/CTS and TXDE Hardware flow control
                   01 = XON/XOFF Software flow control
                   00 = Flow control is off

Note 1:        All modes transmit selected number of Stop bits. Only DMX and DALI receivers verify selected number of
               Stop bits and all others verify only the first Stop bit.
          2:   UART1 only.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 501
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-4:           UxERRIR: UART ERROR INTERRUPT FLAG REGISTER
   R/S/C-1/1        R/S/C-0/0      R/W/S-0/0       R/W/S-0/0     R/S/C-0/0      R/W/S-0/0     R/W/S-0/0      R/W/S-0/0
   TXMTIF             PERIF         ABDOVF           CERIF         FERIF            RXBKIF      RXFOIF        TXCIF
bit 7                                                                                                              bit 0
Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         S = Hardware set              C = Hardware clear
bit 7              TXMTIF: Transmit Shift Register Empty Interrupt Flag bit
                   1 = Transmit shift register is empty (Set at end of Stop bits)
                   0 = Transmit shift register is actively shifting data
bit 6              PERIF: Parity Error Interrupt Flag bit
                   LIN and Parity modes:
                   1 = Unread byte at top of input FIFO has parity error
                   0 = Unread byte at top of input FIFO does not have parity error
                   DALI Device mode:
                   1 = Unread byte at top of input FIFO received as Forward Frame
                   0 = Unread byte at top of input FIFO received as Back Frame
                   Address mode:
                   1 = Unread byte at top of input FIFO received as address
                   0 = Unread byte at top of input FIFO received as data
                   Other modes:
                   Not used
bit 5              ABDOVF: Auto-baud Detect Overflow Interrupt Flag bit
                   DALI mode:
                   1 = Start bit measurement overflowed counter
                   0 = No overflow during Start bit measurement
                   Other modes:
                   1 = Baud rate generator overflowed during the auto detection sequence
                   0 = Baud rate generator has not overflowed
bit 4              CERIF: Checksum Error/DALI STP bit Interrupt Flag bit
                   DALI modes:
                   1 = Stop bit detected
                   0 = Stop bit not detected
                   LIN Mode:
                   1 = Checksum error
                   0 = No Checksum error
bit 3              FERIF: Framing Error Interrupt Flag bit
                   1 = Unread byte at top of input FIFO has framing error
                   0 = Unread byte at top of input FIFO does not have framing error
bit 2              RXBKIF: Break Reception Interrupt Flag bit
                   1 = Break detected
                   0 = No Break detected
bit 1              RXFOIF: Receive FIFO Overflow Interrupt Flag bit
                   1 = Receive FIFO has overflowed
                   0 = Receive FIFO has not overflowed
bit 0              TXCIF: Transmit Collision Interrupt Flag bit(1)
                   1 = Transmitted word is not equal to the word received during transmission
                   0 = Transmitted word equals the word received during transmission

Note 1:      UART1 only.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 502
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-5:           UxERRIE: UART ERROR INTERRUPT ENABLE REGISTER
   R/W-0/0           R/W-0/0        R/W-0/0         R/W-0/0      R/W-0/0        R/W-0/0       R/W-0/0        R/W-0/0
   TXMTIE             PERIE        ABDOVE           CERIE         FERIE         RXBKIE        RXFOIE          TXCIE
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              TXMTIE: Transmit Shift Register Empty Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 6              PERIE: Parity Error Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 5              ABDOVE: Auto-baud Detect Overflow Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 4              CERIE: Checksum Error/DALI STP bit Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 3              FERIE: Framing Error Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 2              RXBKIE: Break Reception Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 1              RXFOIE: Receive FIFO Overflow Interrupt Enable bit
                   1 = Interrupt enabled
                   0 = Interrupt not enabled
bit 0              TXCIE: Transmit Collision Interrupt Enable bit(1)
                   1 = Interrupt enabled
                   0 = Interrupt not enabled

Note 1:      UART1 only.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 503
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-6:          UxUIR: UART GENERAL INTERRUPT REGISTER
  R/S/W-0/0         R/S/W-0/0           U-0             U-0       U-0         R/W-0/0          U-0             U-0
     WUIF             ABDIF             —               —          —             ABDIE             —           —
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         S = Hardware set


bit 7              WUIF: Wake-up Interrupt bit
                   1 = Idle to non-idle transition on RX line detected when WUE is set. Also sets UxIF. (WUIF must be
                       cleared by software to clear UxIF)
                   0 = WUE not enabled by software or no transition detected
bit 6              ABDIF: Auto-baud detect interrupt bit
                   1 = Auto-baud detection complete. Status shown in UxIF when ABDIE is set. (Must be cleared by
                       software)
                   0 = Auto-baud not enabled or auto-baud enabled and auto-baud detection not complete
bit 5-3            Unimplemented: Read as ‘0’
bit 2              ABDIE: Auto-baud Detect Interrupt Enable bit
                   1 = ABDIF will set UxIF bit in PIRx register
                   0 = ABDIF will not set UxIF
bit 1-0            Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 504
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-7:           UxFIFO: UART FIFO STATUS REGISTER
  R/W/S-0/0          R/W-0/0      R/W/S/C-1/1      R/S/C-0/0      R/S/C-1/1        S/C-1/1       R/W/S/C-1/1      R/S/C-0/0
   TXWRE             STPMD            TXBE               TXBF       RXIDL            XON            RXBE            RXBF
bit 7                                                                                                                     bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared           S = Hardware set                C = Hardware clear


bit 7              TXWRE: Transmit Write Error Status bit (Must be cleared by software)
                   LIN Host mode:
                   1 = UxP1L was written when a host process was active
                   LIN Client mode:
                   1 = UxTXB was written when UxP2 = 0 or more than UxP2 bytes have been written to UxTXB since
                        last Break
                   Address Detect mode:
                   1 = UxP1L was written before the previous data in UxP1L was transferred to TX shifter
                   All modes:
                   1 = A new byte was written to UxTXB when the output FIFO was full
                   0 = No error
bit 6              STPMD: Stop Bit Detection Mode bit
                   1 = Assert UxRXIF at end of last Stop bit or end of first Stop bit when STP = 11
                   0 = Assert UxRXIF in middle of first Stop bit
bit 5              TXBE: Transmit Buffer Empty Status bit
                   1 = Transmit buffer is empty. Setting this bit will clear the transmit buffer and output shift register.
                   0 = Transmit buffer is not empty. Software cannot clear this bit.
bit 4              TXBF: Transmit Buffer Full Status bit
                   1 = Transmit buffer is full
                   0 = Transmit buffer is not full
bit 3              RXIDL: Receive Pin Idle Status bit
                   1 = Receive pin is in Idle state
                   0 = UART is receiving Start, Stop, Data, Auto-baud, or Break
bit 2              XON: Software Flow Control Transmit Enable Status bit
                   1 = Transmitter is enabled
                   0 = Transmitter is disabled
bit 1              RXBE: Receive Buffer Empty Status bit
                   1 = Receive buffer is empty. Setting this bit will clear the RX buffer(1)
                   0 = Receive buffer is not empty. Software cannot clear this bit.
bit 0              RXBF: Receive Buffer Full Status bit
                   1 = Receive buffer is full
                   0 = Receive buffer is not full

Note 1:      The BSF instruction may not be used to set RXBE because doing so will clear a byte pending in the trans-
             mit shift register when the UxTXB register is empty. Instead, use the MOVWF instruction with a ‘0’ in the
             TXBE bit location.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 505
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-8:          UxBRGL: UART BAUD RATE GENERATOR LOW REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                        BRG[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            BRG[7:0]: Least Significant Byte of Baud Rate Generator


REGISTER 31-9:          UxBRGH: UART BAUD RATE GENERATOR HIGH REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0         R/W-0/0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                       BRG[15:8]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            BRG[15:8]: Most Significant Byte of Baud Rate Generator
Note 1:      The UxBRG registers may only be written when ON = 0.
     2:      Maximum BRG value when MODE = ‘100x’ and BRGS = 1 is 0x7FFE.
     3:      Maximum BRG value when MODE = ‘100x’ and BRGS = 0 is 0x1FFE.


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 506
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-10: UxRXB: UART RECEIVE REGISTER
        R-x/u         R-x/u          R-x/u              R-x/u      R-x/u          R-x/u         R-x/u           R-x/u
                                                            RXB[7:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            RXB[7:0]: Top of Receive Buffer


REGISTER 31-11: UxTXB: UART TRANSMIT REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0       R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                            TXB[7:0]
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            TXB[7:0]: Bottom of Transmit Buffer


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 507
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-12: UxP1H: UART PARAMETER 1 HIGH REGISTER
        U-0             U-0             U-0              U-0             U-0         U-0             U-0          R/W-0/0
        —               —               —                —               —            —                 —           P1[8]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 0              P1[8]: Most Significant Bit of Parameter 1
                   DMX mode:
                   Most Significant bit of number of bytes to transmit between Start Code and automatic Break generation
                   DALI Control Device mode:
                   Most Significant bit of idle time delay after which a Forward Frame is sent. Measured in half-bit periods
                   DALI Control Gear mode:
                   Most Significant bit of delay between the end of a Forward Frame and the start of the Back Frame
                   Measured in half-bit periods
                   Other modes:
                   Not used


REGISTER 31-13: UxP1L: UART PARAMETER 1 LOW REGISTER
   R/W-0/0           R/W-0/0         R/W-0/0         R/W-0/0         R/W-0/0       R/W-0/0         R/W-0/0        R/W-0/0
                                                               P1[7:0]
bit 7                                                                                                                    bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            P1[7:0]: Least Significant Bits of Parameter 1
                   DMX mode:
                   Least Significant Byte of number of bytes to transmit between Start Code and automatic Break
                   generation
                   DALI Control Device mode:
                   Least Significant Byte of idle time delay after which a Forward Frame is sent. Measured in half-bit periods
                   DALI Control Gear mode:
                   Least Significant Byte of delay between the end of a Forward Frame and the start of the Back Frame
                   Measured in half-bit periods
                   LIN mode:
                   PID to transmit (Only Least Significant 6 bits used)
                   Asynchronous Address mode:
                   Address to transmit (9th transmit bit automatically set to ‘1’)
                   Other modes:
                   Not used


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 508
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-14: UxP2H: UART PARAMETER 2 HIGH REGISTER
        U-0            U-0              U-0              U-0             U-0         U-0            U-0          R/W-0/0
        —               —               —                —               —            —                 —          P2[8]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 0              P2[8]: Most Significant Bit of Parameter 2
                   DMX mode:
                   Most Significant bit of first address of receive block
                   DALI mode:
                   Most Significant bit of number of half-bit periods of idle time in Forward Frame detection threshold
                   Other modes:
                   Not used


REGISTER 31-15: UxP2L: UART PARAMETER 2 LOW REGISTER
   R/W-0/0           R/W-0/0        R/W-0/0          R/W-0/0         R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                               P2[7:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            P2[7:0]: Least Significant Bits of Parameter 2
                   DMX mode:
                   Least Significant Byte of first address of receive block
                   LIN Client mode:
                   Number of data bytes to transmit
                   DALI mode:
                   Least Significant Byte of number of half-bit periods of idle time in Forward Frame detection threshold
                   Asynchronous Address mode:
                   Receiver address
                   Other modes:
                   Not used


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 509
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-16: UxP3H: UART PARAMETER 3 HIGH REGISTER
        U-0            U-0              U-0              U-0             U-0         U-0            U-0          R/W-0/0
        —               —               —                —               —            —                 —          P3[8]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 0              P3[8]: Most Significant Bit of Parameter 3
                   DMX mode:
                   Most Significant bit of last address of receive block
                   Other modes:
                   Not used


REGISTER 31-17: UxP3L: UART PARAMETER 3 LOW REGISTER
   R/W-0/0           R/W-0/0        R/W-0/0          R/W-0/0         R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                               P3[7:0]
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-0            P3[7:0]: Least Significant Bits of Parameter 3
                   DMX mode:
                   Least Significant Byte of last address of receive block
                   LIN Client mode:
                   Number of data bytes to receive
                   Asynchronous Address mode:
                   Receiver address mask. Received address is XOR’d with UxP2L then AND’d with UxP3L
                   Match occurs when result is zero
                   Other modes:
                   Not used


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 510
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 31-18: UxTXCHK: UART TRANSMIT CHECKSUM RESULT REGISTER
   R/W-0/0           R/W-0/0      R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                       TXCHK[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            TXCHK[7:0]: Checksum calculated from TX bytes
                   LIN mode and C0EN = 1:
                   Sum of all transmitted bytes including PID
                   LIN mode and C0EN = 0:
                   Sum of all transmitted bytes except PID
                   All other modes and C0EN = 1:
                   Sum of all transmitted bytes since last clear
                   All other modes and C0EN = 0:
                   Not used


REGISTER 31-19: UxRXCHK: UART RECEIVE CHECKSUM RESULT REGISTER
   R/W-0/0           R/W-0/0      R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
                                                       RXCHK[7:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-0            RXCHK[7:0]: Checksum calculated from RX bytes
                   LIN mode and C0EN = 1:
                   Sum of all received bytes including PID
                   LIN mode and C0EN = 0:
                   Sum of all received bytes except PID
                   All other modes and C0EN = 1:
                   Sum of all received bytes since last clear
                   All other modes and C0EN = 0:
                   Not used


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 511
                         PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 31-3:       SUMMARY OF REGISTERS ASSOCIATED WITH THE UART
                                                                                                                Register
    Name         Bit 7       Bit 6        Bit 5       Bit 4              Bit 3    Bit 2     Bit 1       Bit 0
                                                                                                                on page
UxCON0          BRGS        ABDEN        TXEN         RXEN                           MODE[3:0]                    500
UxCON1            ON           —           —          WUE           RXBIMD         —      BRKOVR       SENDB      501
UxCON2         RUNOVF       RXPOL              STP[1:0]              C0EN        TXPOL           FLO[1:0]         502
UxERRIR         TXMTIF       PERIF      ABDOVF       CERIF           FERIF       RXBKIF    RXFOIF       TXCIF     503
UxERRIE         TXMTIE       PERIE      ABDOVE       CERIE           FERIE;      RXBKIE    RXFOIE      TXCIE      504
UxUIR            WUIF        ABDIF         —              —               —      ABDIE       —              —     505
UxFIFO          TXWRE       STPMD        TXBE         TXBF           RXIDL        XON       RXBE        RXBF      506
UxBRGL                                                        BRG[7:0]                                            507
UxBRGH                                                        BRG[15:8]                                           507
UxRXB                                                         RXB[7:0]                                            508
UxTXB                                                         TXB[7:0]                                            508
UxP1H             —            —           —              —               —        —         —          P1[8]     509
UxP1L                                                          P1[7:0]                                            509
UxP2H             —            —           —              —               —        —         —          P2[8]     510
UxP2L                                                          P2[7:0]                                            510
UxP3H             —            —           —              —               —        —         —          P3[8]     511
UxP3L                                                          P3[7:0]                                            511
UxTXCHK                                                   TXCHK[7:0]                                              512
UxRXCHK                                                   RXCHK[7:0]                                              512
Legend:     — = unimplemented, read as ‘0’. Shaded cells are unused by the UART module.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 512
