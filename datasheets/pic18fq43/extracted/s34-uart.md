                                                                                                          PIC18F27/47/57Q43
                                                                                       UART - Universal Asynchronous Receiver
                                                                                            Transmitter with Protocol Support

34.   UART - Universal Asynchronous Receiver Transmitter with Protocol
      Support
      The Universal Asynchronous Receiver Transmitter (UART) module is a serial I/O communications
      peripheral. It contains all the clock generators, shift registers and data buffers necessary to perform
      an input or output serial data transfer, independent of device program execution. The UART, also
      known as a Serial Communications Interface (SCI), can be configured as a full-duplex asynchronous
      system or one of several automated protocols. The Full Duplex mode is useful for communications
      with peripheral systems, such as wireless modems and USB to serial interface modules.
      Supported protocols include:
      •   LIN Host and Client
      •   DMX Controller and Receiver
      •   DALI Control Gear and Control Device
      The UART module includes the following capabilities:
      •   Half and full-duplex asynchronous transmit and receive
      •   Two-byte input buffer
      •   One-byte output buffer
      •   Programmable 7-bit or 8-bit byte width
      •   9th bit address detection
      •   9th bit even or odd parity
      •   Input buffer overrun error detection
      •   Receive framing error detection
      •   Hardware and software flow control
      •   Automatic checksum calculation and verification
      •   Programmable 1, 1.5, and 2 Stop bits
      •   Programmable data polarity
      •   Manchester encoder/decoder
      •   Operation in Sleep
      •   Automatic detection and calibration of the baud rate
      •   Wake-up on Break reception
      •   Automatic and user timed Break period generation
      •   RX and TX inactivity time-outs (with Timer2)
      The operation of the UART module is controlled through 19 8-bit registers:
      •   Three control registers (UxCON0-UxCON2)
      •   Error enable and status (UxERRIE, UxERRIR, UxUIR)
      •   UART buffer status and control (UxFIFO)
      •   Three 9-bit protocol parameters (UxP1-UxP3)
      •   16-bit Baud Rate Generator (UxBRG)
      •   Transmit buffer write (UxTXB)
      •   Receive buffer read (UxRXB)
      •   Receive checksum (UxRXCHK)


--- p541 ---
                                                                                                                                              PIC18F27/47/57Q43
                                                                                                                           UART - Universal Asynchronous Receiver
                                                                                                                                Transmitter with Protocol Support
•   Transmit checksum (UxTXCHK)
The UART transmit output (TX_out) is available to the TX pin and internally to various peripherals.
Block diagrams of the UART transmitter and receiver are shown in the following figures.

Figure 34-1. UART Transmitter Block Diagram

                                                                                        Data bus                                                             Rev. 10-000113D
                                                                                                                                                                    11/2/2018


                                                                                            8
                                                                                                                            UxTXIE

                                                             FIFO                                                                                            Interrupt
                                                        (if equipped)                UxTXB register                           UxTXIF

                                                                                            8
                                                                                                   +          UxTXCHK                                RxyPPS
                                         TXEN
                                                                     MSb                                        LSb                                                       TX pin
                                                                                                                                      Mode
                                                                        (8)                                        0                                   PPS
                                                                                                                                     Control
                                                                              Transmit Shift Register (TSR)

                                                                                                                                                                TX_out


     Baud Rate Generator                                                                                      TXMTIF
                                  FOSC              ÷n                        Address or
                                                                              Parity mode
                                                    n

                      +1        Multiplier    x4         x16
                                  BRGS          1          0
       UxBRGH UxBRGL


Figure 34-2. UART Receiver Block Diagram

                                                                                                                                                       Rev. 10-000114C
                                                                                                                                                              11/2/2018


                                                                                                                              RXFOIF                   RXIDL

                                                RXEN
                           RXPPS
                                                                                                        MSb                RSR Register                LSb
             RX pin
                                              Pin Buffer                      Mode Data
                           PPS                                                                          Stop (8)       7                   1     0     Start
                                             and Control                      Recovery


          Baud Rate Generator
                                         FOSC                  ÷n                                                                         +          UxRXCHK
                                                                                                              Address or
                                                              n                                               Parity Mode
                           +1         Multiplier         x4         x16
                                         BRGS             1         0
            UxBRGH UxBRGL                                                                                                                                      FIFO
                                                                                                FERIF           PERIF           UxRXB Register
                                                                                                                               8
                                                                                                                                      Data Bus


                                                                                                                UxRXIF                     Interrupt
                                                                                                                UxRXIE


--- p542 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                         UART - Universal Asynchronous Receiver
                                                                                              Transmitter with Protocol Support
34.1    UART I/O Pin Configuration
        The RX input pin is selected with the UxRPPS register. The TX output pin is selected with each pin’s
        RxyPPS register. When the TRIS control for the pin corresponding to the TX output is cleared, the
        UART will control the logic level on the TX pin. Changing the TXPOL bit in UxCON2 will immediately
        change the TX pin logic level, regardless of the value of EN or TXEN.

34.2    UART Asynchronous Modes
        The UART has five Asynchronous modes:
        •   7-bit
        •   8-bit
        •   8-bit with even parity in the 9th bit
        •   8-bit with odd parity in the 9th bit
        •   8-bit with address indicator in the 9th bit
        The UART transmits and receives data using the standard Non-Return-to-Zero (NRZ) format. NRZ is
        implemented with two levels: A VOH Mark state, which represents a ‘1’ data bit, and a VOL Space
        state, which represents a ‘0’ data bit. NRZ implies that consecutively transmitted data bits of the
        same value stay at the output level of that bit without returning to a neutral level between each bit
        transmission. An NRZ transmission port idles in the Mark state. Each character transmission consists
        of one Start bit followed by seven or eight data bits, one optional parity or address bit, and is always
        terminated by one or more Stop bits. The Start bit is always a space and the Stop bits are always
        marks. The most common data format is eight bits with no parity. Each transmitted bit persists
        for a period of 1/ (Baud Rate). An on-chip dedicated 16-bit Baud Rate Generator is used to derive
        standard baud rate frequencies from the system oscillator. See the UART Baud Rate Generator
        section for more information.
        In all Asynchronous modes, the UART transmits and receives the LSb first. The UART’s transmitter
        and receiver are functionally independent but share the same data format and baud rate. Parity is
        supported by the hardware with even and odd parity modes.

34.2.1 UART Asynchronous Transmitter
        The UART transmitter block diagram is shown in Figure 34-1. The heart of the transmitter is the
        serial Transmit Shift Register (TSR), which is not directly accessible by software. The TSR obtains its
        data from the transmit buffer, which is the UxTXB register.

34.2.1.1 Enabling the Transmitter
        The UART transmitter is enabled for asynchronous operations by configuring the following control
        bits:
        •   TXEN = 1
        •   MODE = 0000 through 0011
        •   UxBRG = desired baud rate
        •   BRGS = desired baud rate multiplier
        •   RxyPPS = code for desired output pin
        •   ON = 1
        All other UART control bits are assumed to be in their default state.
        Setting the TXEN bit enables the transmitter circuitry of the UART. The MODE bits select the desired
        mode. Setting the ON bit enables the UART. When TXEN is set and the transmitter is not Idle, the
        TX pin is automatically configured as an output. When the transmitter is Idle, the TX pin drive is
        relinquished to the port TRIS control. If the TX pin is shared with an analog peripheral, the analog I/O
        function will be disabled by clearing the corresponding ANSEL bit.


--- p543 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
                      Important: The UxTXIF Transmitter Interrupt flag is set when the TXEN Enable bit
                      is set and the UxTXB register can accept data.


34.2.1.2 Transmitting Data
        A transmission is initiated by writing a character to the UxTXB register. If this is the first character,
        or the previous character has been completely transmitted from the TSR, the data in the UxTXB
        is immediately transferred to the TSR register. If the TSR still contains all or part of a previous
        character, the new character data are held in the UxTXB until the previous character transmission
        is complete. The pending character in the UxTXB is then transferred to the TSR at the beginning of
        the previous character Stop bit transmission. The transmission of the Start bit, data bits and Stop bit
        sequence commences immediately following the completion of all of the previous character’s Stop
        bits.

34.2.1.3 Transmit Data Polarity
        The polarity of the transmit data is controlled with the TXPOL bit. The default state of this bit is ‘0’,
        which selects high true transmit Idle and data bits. Setting the TXPOL bit to ‘1’ will invert the transmit
        data, resulting in low true Idle and data bits. The TXPOL bit controls transmit data polarity in all
        modes.

34.2.1.4 Transmit Interrupt Flag
        The UxTXIF Interrupt Flag bit in the PIR register is set whenever the UART transmitter is enabled
        and no character is being held for transmission in the UxTXB register. In other words, the UxTXIF
        bit is clear only when the TSR is busy with a character and a new character has been queued for
        transmission in the UxTXB register.
        The UxTXIF interrupt is enabled by setting the UxTXIE Interrupt Enable bit in the PIE register.
        However, the UxTXIF Flag bit will be set whenever the UxTXB register is empty, regardless of the
        state of the UxTXIE Enable bit. The UxTXIF bit is read-only and cannot be set or cleared by software.
        To use interrupts when transmitting data, set the UxTXIE bit only when there is more data to send.
        Clear the UxTXIE Interrupt Enable bit upon writing the UxTXB register with the last character of the
        transmission.

34.2.1.5 TSR Status
        The TXMTIF bit indicates the status of the TSR. This is a read-only bit. The TXMTIF bit is set when the
        TSR is empty and Idle. The TXMTIF bit is cleared when a character is transferred to the TSR from the
        UxTXB. The TXMTIF bit remains clear until all bits, including the Stop bits, have been shifted out of
        the TSR and a byte is not waiting in the UxTXB register.
        The TXMTIF will generate a summary UxEIF interrupt when the TXMTIE bit is set.


                      Important: The TSR is not mapped in data memory, so it is not available to the
                      user.


34.2.1.6 Transmitter 7-Bit Mode
        The 7-bit mode is selected when the MODE bits are set to ‘0001’. In 7-bit mode, only the seven Least
        Significant bits of the data written to UxTXB are transmitted. The Most Significant bit is ignored.

34.2.1.7 Transmitter Parity Modes
        When Odd or Even Parity mode is selected, all data are sent as nine bits. The first eight bits are data
        and the 9th bit is parity. Even and odd parity is selected when the MODE bits are set to ‘0011’ and
        ‘0010’, respectively. Parity is automatically determined by the module and inserted in the serial data
        stream.


--- p544 ---
                                                                                                                       PIC18F27/47/57Q43
                                                                                                    UART - Universal Asynchronous Receiver
                                                                                                         Transmitter with Protocol Support
34.2.1.8 Asynchronous Transmission Setup
        Use the following steps as a guide for configuring the UART for asynchronous transmissions.
        1. Initialize the UxBRG register pair and the BRGS bit to achieve the desired baud rate.
        2. Set the MODE bits to the desired Asynchronous mode.
        3. Set the TXPOL bit if inverted TX output is desired.
        4. Enable the asynchronous serial port by setting the ON bit.
        5. Enable the transmitter by setting the TXEN Control bit. This will cause the UxTXIF Interrupt flag to
           be set.
        6. If the device has PPS, configure the desired I/O pin RxyPPS register with the code for the TX
           output.
        7. If interrupts are desired, set the UxTXIE Interrupt Enable bit in the respective PIE register. An
           interrupt will occur immediately provided that global interrupts are also enabled.
        8. Write one byte of data into the UxTXB register. This will start the transmission.
        9. Subsequent bytes may be written when the UxTXIF bit is ‘1’.

        Figure 34-3. UART Asynchronous Transmission

                                                                                                                               Rev. 10-000115B

                                            Word 1
                                                                                                                                       9/1/2017


              Write to UxTXB


                 BRG Output
                 (Shift Clock)

                       TX pin                        Start bit    bit 0         bit 1                   bit 7/8    Stop bit
                  UxTXIF                                                         Word 1
            (Transmit Buffer        1 TCY
                  Reg Empty
                    Flag) bit
           TXMTIF (Transmit
            Shift Reg Empty
                    Flag) bit


        Figure 34-4. UART Asynchronous Transmission (Back-to-Back)

                                                                                                                                       Rev. 10-000116B

                               Word 1     Word 2                                                                                               9/1/2017


             Write to UxTXB

               BRG Output
               (Shift Clock)

                      TX pin             Start bit    bit 0      bit 1                    bit 7/8      Stop bit   Start bit           bit 0

                 UxTXIF                                             Word 1                                                Word 2
           (Transmit Buffer             1 TCY
        Reg Empty Flag) bit
                   TXMTIF
             (Transmit Shift
           Reg Empty Flag)
                         bit


--- p545 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                         UART - Universal Asynchronous Receiver
                                                                                              Transmitter with Protocol Support
34.2.2 UART Asynchronous Receiver
        The Asynchronous mode is typically used in RS-232 systems. The receiver block diagram is shown
        in Figure 34-2. The data are received on the RX pin and drive the data recovery block. The data
        recovery block is actually a high-speed shifter operating at 4 or 16 times the baud rate, whereas
        the serial Receive Shift Register (RSR) operates at the bit rate. When all bits of the character have
        been shifted in, they are immediately transferred to a two-character First-In First-Out (FIFO) memory.
        The FIFO buffering allows reception of two complete characters and the start of a third character
        before software must begin servicing the UART receiver. The FIFO registers and RSR are not directly
        accessible by software. Access to the received data is made via the UxRXB register.
34.2.2.1 Enabling the Receiver
        The UART receiver is enabled for asynchronous operation by configuring the following control bits:
        •   RXEN = 1
        •   MODE = 0000 through 0011
        •   UxBRG = desired baud rate
        •   BRGS = desired baud rate multiplier
        •   RXPPS = code for desired input pin
        •   Input pin ANSEL bit = 0
        •   ON = 1
        All other UART control bits are assumed to be in their default state.
        Setting the RXEN bit enables the receiver circuitry of the UART. Setting the MODE bits configures
        the UART for the desired Asynchronous mode. Setting the ON bit enables the UART. The TRIS bit
        corresponding to the selected RX I/O pin must be set to configure the pin as an input.


                       Important: If the RX function is on an analog pin, the corresponding ANSEL bit
                       must be cleared for the receiver to function.


34.2.2.2 Receiving Data
        Data are recovered from the bit stream by timing to the center of the bits and sampling the input
        level. In High-Speed mode, there are four BRG clocks per bit and only one sample is taken per bit. In
        Normal Speed mode, there are 16 BRG clocks per bit and three samples are taken per bit.
        The receiver data recovery circuit initiates character reception on the falling edge of the Start bit. The
        Start bit is always a ‘0’. The Start bit is qualified in the middle of the bit. In Normal Speed mode only,
        the Start bit is also qualified at the leading edge of the bit. The following paragraphs describe the
        majority-detect sampling of the Normal Speed mode without inverted polarity.
        The falling edge starts the Baud Rate Generator (BRG) clock. The input is sampled at the first and
        second BRG clocks.
        If both samples are high, then the falling edge is deemed a glitch and the UART returns to the Start
        bit detection state without generating an error.
        If either sample is low, the data recovery circuit continues counting BRG clocks and takes samples at
        clock counts: 7, 8 and 9. When less than two samples are low, the Start bit is deemed invalid, and the
        data recovery circuit aborts character reception without generating an error and resumes looking for
        the falling edge of the Start bit.
        When two or more samples are low, the Start bit is deemed valid and the data recovery continues.
        After a valid Start bit is detected, the BRG clock counter continues and resets at count 16. This is the
        beginning of the first data bit.


--- p546 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                           UART - Universal Asynchronous Receiver
                                                                                                Transmitter with Protocol Support
        The data recovery circuit counts the BRG clocks from the beginning of the bit and takes samples at
        clocks 7, 8 and 9. The bit value is determined from the majority of the samples. The resulting ‘0’ or
        ‘1’ is shifted into the RSR. The BRG clock counter continues and resets at count 16. This sequence
        repeats until all data bits have been sampled and shifted into the RSR.
        After all data bits have been shifted in, the first Stop bit is sampled. Stop bits are always a ‘1’. If
        the bit sampling determines that a ‘0’ is in the Stop bit position, the framing error is set for this
        character. Otherwise, the framing error is cleared for this character. See the Receive Framing Error
        section for more information on framing errors.

34.2.2.3 Receive Data Polarity
        The polarity of the receive data is controlled with the RXPOL bit. The default state of this bit is ‘0’,
        which selects high true receive Idle and data bits. Setting the RXPOL bit to ‘1’ will invert the receive
        data, resulting in low true Idle and data bits. The RXPOL bit controls receive data polarity in all
        modes.

34.2.2.4 Receive Interrupts
        Immediately after all data bits and the Stop bit have been received, the character in the RSR is
        transferred to the UART receive FIFO. The UxRXIF Interrupt flag in the respective PIR register is set at
        this time, provided it is not being suppressed.
        The UxRXIF is suppressed by any of the following:
        •   FERIF when FERIE is set
        •   PERIF when PERIE is set
        When the UART uses DMA for reception, suppressing the UxRXIF suspends the DMA transfer of data
        until software processes the error and reads UxRXB to advance the FIFO beyond the error.
        The UxRXIF interrupts are enabled by setting all of the following bits:
        •   UxRXIE, Interrupt Enable bit in the PIE register
        •   Global Interrupt Enable bits
        The UxRXIF Interrupt Flag bit will be set when it is not suppressed and there is an unread character
        in the FIFO, regardless of the state of interrupt enable bits. Reading the UxRXB register will transfer
        the top character out of the FIFO and reduce the FIFO contents by one. The UxRXIF Interrupt Flag bit
        is read-only and therefore cannot be set or cleared by software.

34.2.2.5 Receive Framing Error
        Each character in the receive FIFO buffer has a corresponding Framing Error Flag bit. A framing error
        indicates that the Stop bit was not seen at the expected time. For example, a Break condition will be
        received as a 0x00 byte with the framing error bit set.
        The Framing Error flag is accessed via the FERIF bit. The FERIF bit represents the frame status of
        the top unread character of the receive FIFO. Therefore, the FERIF bit must be read before reading
        UxRXB.
        The FERIF bit is read-only and only applies to the top unread character of the receive FIFO. A framing
        error (FERIF = 1) does not preclude reception of additional characters. It is neither necessary nor
        possible to clear the FERIF bit directly. Reading the next character from the FIFO buffer will advance
        the FIFO to the next character and the next corresponding framing error, if any.
        The FERIF bit is cleared when the character at the top of the FIFO does not have a framing error
        or when all bytes in the receive FIFO have been read. Clearing the ON bit resets the receive FIFO,
        thereby also clearing the FERIF bit.
        A framing error will generate a summary UxEIF interrupt when the FERIE bit is set. The summary
        error is reset when the FERIF bit of the top of the FIFO is ‘0’ or when all FIFO characters have been
        retrieved.


--- p547 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
                    Important: When FERIE is set, UxRXIF interrupts are suppressed by FERIF = 1.


34.2.2.6 Receiver Parity Modes
        Even or odd parity is automatically detected when the MODE bits are set to ‘0011’ or ‘0010’,
        respectively. The parity modes receive eight data bits and one parity bit for a total of nine bits for
        each character. The PERIF bit represents the parity error of the top unread character of the receive
        FIFO rather than the parity bit itself. The parity error must be read before the UxRXB register is read
        because reading the UxRXB register will advance the FIFO pointer to the next byte with its associated
        PERIF flag.
        A parity error will generate a summary UxEIF interrupt when the PERIE bit is set. The summary
        error is reset when the PERIF bit of the top of the FIFO is ‘0’ or when all FIFO characters have been
        retrieved.


                    Important: When PERIE is set, the UxRXIF interrupts are suppressed by PERIF = 1.


34.2.2.7 Receive FIFO Overflow
        When more characters are received than the receive FIFO can hold, the RXFOIF bit is set. The
        character causing the Overflow condition is discarded. The RUNOVF bit determines how the receive
        circuit responds to characters while the Overflow condition persists. When RUNOVF is set, the
        receive shifter stays synchronized to the incoming data stream by responding to Start, data, and
        Stop bits. However, all received bytes not already in the FIFO are discarded. When RUNOVF is
        cleared, the receive shifter ceases operation and Start, data, and Stop bits are ignored. The Receive
        Overflow condition is cleared by reading the UxRXB register and clearing the RXFOIF bit. If the
        UxRXB register is not read, thereby opening a space in the FIFO, the next character received will be
        discarded and cause another Overflow condition.
        A receive overflow error will generate a summary UxEIF interrupt when the RXFOIE bit is set.
34.2.2.8 Asynchronous Reception Setup
        Use the following steps as a guide for configuring the UART for asynchronous reception:
        1. Initialize the UxBRG register pair and the BRGS bit to achieve the desired baud rate.
        2. Configure the RXPPS register for the desired RX pin.
        3. Clear the ANSEL bit for the RX pin (if applicable).
        4. Set the MODE bits to the desired Asynchronous mode.
        5. Set the RXPOL bit if the data stream is inverted.
        6. Enable the serial port by setting the ON bit.
        7. If interrupts are desired, set the UxRXIE bit in the PIEx register and enable global interrupts.
        8. Enable reception by setting the RXEN bit.
        9. Read the UxERRIR register to get the error flags.
        10. The UxRXIF Interrupt Flag bit will be set when a character is transferred from the RSR to the
            receive buffer. An interrupt will be generated if the UxRXIE interrupt enable bit is also set.
        11. Read the UxRXB register to get the received byte.
        12. If an overrun occurred, clear the RXFOIF bit.


--- p548 ---
                                                                                                                              PIC18F27/47/57Q43
                                                                                                           UART - Universal Asynchronous Receiver
                                                                                                                Transmitter with Protocol Support
       Figure 34-5. UART Asynchronous Reception

                                                                                                                                            Rev. 10-000117B
                                                                                                                                                   1/24/2019


                               Start                 Last   Stop   Start                  Last   Stop   Start                 Last   Stop
                    RX pin      bit    bit 0                        bit      bit 0                       bit     bit 0
                                                      bit    bit                           bit    bit                          bit    bit
                                           Word 1                                Word 2                              Word 3
            Rcv Shift Reg
           Rcv Buffer Reg
                                                                   Word 1                               Word 2
                                                                   UxRXB                                UxRXB

                    RXIDL


            Read UxRXB

                   UxRXIF
            (Interrupt flag)

            RXFOIF Flag


                                                                                                                              Cleared by software


                     Note: This timing diagram shows three bytes appearing on the RX input. The UxRXB is not read before the third
                           word is received, causing the RXFOIF (FIFO overrun) bit to be set. STPMD = 0, STP = 00.


34.2.3 Asynchronous Address Mode
       A special Address Detection mode is available for use when multiple receivers share the same
       transmission line, as seen in RS-485 systems.
       When Asynchronous Address mode is enabled, all data are transmitted and received as 9-bit
       characters. The 9th bit determines whether the character is address or data. When the 9th bit is
       set, the eight Least Significant bits are the address. When the 9th bit is clear, the Least Significant
       bits are data. In either case, the 9th bit is stored in PERIF when the byte is written to the receive FIFO.
       When PERIE is also set, the RXIF will be suppressed, thereby suspending DMA transfers allowing
       software to process the received address.
       An address character will enable all receivers that match the address and disable all other receivers.
       Once a receiver is enabled, all non-address characters will be received until an address character
       that does not match is received.

34.2.3.1 Address Mode Transmit
       The UART transmitter is enabled for asynchronous address operation by configuring the following
       control bits:
       •    TXEN = 1
       •    MODE = 0100
       •    UxBRG = desired baud rate
       •    BRGS = desired baud rate multiplier
       •    RxyPPS = code for desired output pin
       •    ON = 1
       Addresses are sent by writing to the UxP1L register. This transmits the written byte with the 9th bit
       set, which indicates that the byte is an address.
       Data are sent by writing to the UxTXB register. This transmits the written byte with the 9th bit
       cleared, which indicates that the byte is data.


--- p549 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                       UART - Universal Asynchronous Receiver
                                                                                            Transmitter with Protocol Support
       To send data to a particular device on the transmission bus, first transmit the address of the
       intended device. All subsequent data will be accepted only by that device until an address of another
       device is transmitted.
       Writes to UxP1L take precedence over writes to UxTXB. When both the UxP1L and UxTXB registers
       are written while the TSR is busy, the next byte to be transmitted will be from UxP1L.
       To ensure all data intended for one device are sent before the address is changed, wait until the
       TXMTIF bit is high before writing UxP1L with the new address.
34.2.3.2 Address Mode Receive
       The UART receiver is enabled for asynchronous address operation by configuring the following
       control bits:
       •   RXEN = 1
       •   MODE = 0100
       •   UxBRG = desired baud rate
       •   BRGS = desired baud rate multiplier
       •   RXPPS = code for desired input pin
       •   Input pin ANSEL bit = 0
       •   UxP2L = receiver address
       •   UxP3L = address mask
       •   ON = 1
       In Address mode, no data will be transferred to the input FIFO until a valid address is received. This
       is the default state. Any of the following conditions will cause the UART to revert to the default state:
       •   ON = 0
       •   RXEN = 0
       •   Received address does not match
       When a character with the 9th bit set is received, the Least Significant eight bits of that character will
       be qualified by the values in the UxP2L and UxP3L registers.
       The byte is XORed with UxP2L then ANDed with UxP3L. A match occurs when the result is 0h, in
       which case, the unaltered received character is stored in the receive FIFO, thereby setting the UxRXIF
       Interrupt bit. The 9th bit is stored in the corresponding PERIF bit, identifying this byte as an address.
       An address match also enables the receiver for all data such that all subsequent characters without
       the 9th bit set will be stored in the receive FIFO.
       When the 9th bit is set and a match does not occur, the character is not stored in the receive FIFO
       and all subsequent data are ignored.
       The UxP3L register mask allows a range of addresses to be accepted. Software can then determine
       the sub-address of the range by processing the received address character.

34.3   DMX Mode (Full-Featured UARTs Only)
       DMX is a protocol used in stage and show equipment. This includes lighting, fog machines,
       motors, etc. The protocol consists of a controller that sends out commands and a receiver, such
       as theater lights, that receive these commands. The DMX protocol is usually unidirectional but
       can be a bidirectional protocol in either Half or Full Duplex mode. An example of a Half Duplex
       mode is the RDM (Remote Device Management) protocol that sits on DMX512A. The controller
       transmits commands and the receiver receives them. There are no Error conditions or retransmit
       mechanisms.


--- p550 ---
                                                                                                                                PIC18F27/47/57Q43
                                                                                                             UART - Universal Asynchronous Receiver
                                                                                                                  Transmitter with Protocol Support
       DMX, or DMX512A, consists of a “universe” of 512 channels. This means that one controller can
       output up to 512 bytes on a single DMX link. Each piece of equipment on the line is programmed to
       listen to a consecutive sequence of one or more of these bytes.
       For example, a fog machine connected to one of the universes may be programmed to receive one
       byte, starting at byte number 10, and a lighting unit may be programmed to receive four bytes
       starting at byte number 22.

34.3.1 DMX Controller
       The DMX Controller mode is configured with the following settings:
       •     MODE = 1010
       •     TXEN = 1
       •     RXEN = 0
       •     TXPOL = 0
       •     UxP1 = one less than the number of bytes to transmit (excluding the Start code)
       •     UxBRG = value to achieve 250K baud rate
       •     STP = 10 for two Stop bits
       •     RxyPPS = TX pin output code
       •     ON = 1
       Each DMX transmission begins with a Break followed by a byte called the “Start Code”. The width of
       the Break is fixed at 25 bit times. The Break is followed by a “Mark After Break” (MAB) Idle period.
       After this Idle period, the first through the ‘n’th byte is transmitted, where ‘n-1’ is the value in UxP1.
       See the following figure.

       Figure 34-6. DMX Transmit Sequence

                                                                                                                                               Rev. 10-000329A
                                  Start                                                                         Start                                  9/5/2017


                                  Code Byte 1                       Byte 2     Byte 3   Byte n                  Code Byte 1
               Write to UxTXB


                        TX pin                              Start                                         Software                     Start
                                         Break    MAB(1)    Code
                                                                     Byte 1 Byte 2               Byte n              Break    MAB(1)   Code
                                                                                                           Delay
                    UxTXIF
             (Transmit Buffer
           Reg Empty Flag) bit
            TXMTIF (Transmit
              Shift Reg Empty
                      Flag) bit
                        TXEN
                     (optional
           synchronization) bit

                 Note: 1. The MAB period is fixed at 3 bit times.


       Software sends the Start Code and the ‘n’ data bytes by writing the UxTXB register with each byte to
       be sent in the desired order. A UxTXIF value of ‘1’ indicates when the UxTXB is ready to accept the
       next byte.
       The internal byte counter is not accessible to software. Software needs to keep track of the number
       of bytes written to UxTXB to ensure that no more and no less than ‘n’ bytes are sent because the
       DMX state machine will automatically insert a Break and reset its internal counter after ‘n’ bytes are
       written. One way to ensure synchronization between hardware and software is to toggle TXEN after


--- p551 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
       the last byte of the universe is completely free of the transmit shift register, as indicated by the
       TXMTIF bit.

34.3.2 DMX Receiver
       The DMX Receiver mode is configured with the following settings:
       •   MODE = 1010
       •   TXEN = 0
       •   RXEN = 1
       •   RXPOL = 0
       •   UxP2 = number of first byte to receive
       •   UxP3 = number of last byte to receive
       •   UxBRG = value to achieve 250K baud rate
       •   STP = 10 for two Stop bits
       •   ON = 1
       •   UxRXPPS = code for desired input pin
       •   Input pin ANSEL bit = 0
       When configured as a DMX Receiver, the UART listens for a Break character that is at least 23 bit
       periods wide. If the Break is shorter than 23 bit times, the Break is ignored and the DMX state
       machine remains in Idle mode. Upon receiving the Break, the DMX counters will be reset to align
       with the incoming data stream. Immediately after the Break, the UART will see the “Mark after Break”
       (MAB). This space is ignored by the UART. The Start Code follows the MAB and will always be stored
       in the receive FIFO.
       After the Start Code, the first through the 512th byte will be received, but not all of them are stored
       in the receive FIFO. The UART ignores all received bytes until the bytes of interest are received. This
       is done using the UxP2 and UxP3 registers. The UxP2 register holds the value of the byte number
       to start the receive process. The byte counter starts at ‘0’ for the first byte after the Start Code. For
       example, to receive four bytes starting at the 10th byte after the Start Code, write 009h (9 decimal)
       to UxP2H:L and 00Ch (12 decimal) to UxP3H:L. The receive FIFO depth is limited, therefore the bytes
       must be retrieved by reading UxRXB as they come in to avoid a receive FIFO Overrun condition.
       Typically, two Stop bits are inserted between bytes. If either Stop bit is detected as a ‘0’, the framing
       error for that byte will be set.
       Since the DMX sequence always starts with a Break, the software can verify that it is in sync with the
       sequence by monitoring the RXBKIF flag to ensure that the next byte received after the RXBKIF flag is
       processed as the Start Code and subsequent bytes are processed as the expected data.

34.4   LIN Modes (Full-Featured UARTs Only)
       LIN is a protocol used primarily in automotive applications. The LIN network consists of two kinds of
       software processes: a Host process and a Client process. Each network has only one Host process
       and one or more Client processes.
       From a physical layer point of view, the UART on one processor may be driven by both a Host and a
       Client process, as long as only one Host process exists on the network.
       A LIN transaction consists of a Host process followed by a Client process. The Client process may
       involve more than one client where one is transmitting and the other(s) receiving. The transaction
       begins by the following Host process transmission sequence:
       1. Break.
       2. Delimiter bit.


--- p552 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
       3. Sync Field.
       4. PID byte.
       The PID determines which Client processes are expected to respond to the host. When the PID
       byte is complete, the TX output remains in the Idle state. One or more of the Client processes may
       respond to the Host process. If no one responds within the inter-byte period, the host is free to
       start another transmission. The inter-byte period is timed by software using a means other than the
       UART.
       The Client process follows the Host process. When the client software recognizes the PID, that Client
       process responds by either transmitting the required response or by receiving the transmitted data.
       Only Client processes send data. Therefore, Client processes receiving data are receiving that of
       another Client process.
       When a client sends data, the client UART automatically calculates the checksum for the transmitted
       bytes as they are sent and appends the inverted checksum byte to the client response.
       When a client receives data, the checksum is accumulated on each byte as it is received using
       the same algorithm as the sending process. The last byte, which is the inverted checksum value
       calculated by the sending process, is added to the locally calculated checksum by the UART. The
       check passes when the result is all ‘1’s, otherwise the check fails and the CERIF bit is set.
       Two methods for computing the checksum are available: legacy and enhanced. The legacy checksum
       includes only the data bytes. The enhanced checksum includes the PID and the data. The C0EN
       control bit determines the checksum method. Setting C0EN to ‘1’ selects the enhanced method.
       Software must select the appropriate method before the Start bit of the checksum byte is received.

34.4.1 LIN Host/Client Mode
       The LIN Host mode includes capabilities to generate client processes. The host process stops at the
       PID transmission. Any data that is transmitted in Host/Client mode is done as a client process. LIN
       Host/Client mode is configured by the following settings:
       •   MODE = 1100
       •   TXEN = 1
       •   RXEN = 1
       •   UxBRG = value to achieve desired baud rate
       •   TXPOL = 0 (for high Idle state)
       •   STP = desired Stop bits selection
       •   C0EN = desired Checksum mode
       •   RxyPPS = TX pin selection code
       •   TX pin TRIS control = 0
       •   ON = 1


                      Important: The TXEN bit must be set before the Host process is received and
                      remain set while in LIN mode whether or not the Client process is a transmitter.


       The Host process is started by writing the PID to the UxP1L register when UxP2 is ‘0’ and the UART
       is Idle. The UxTXIF will not be set in this case. Only the six Least Significant bits of UxP1L are used in
       the PID transmission.
       The two Most Significant bits of the transmitted PID are PID parity bits. PID[6] is the exclusive-or of
       PID bits 0, 1, 2 and 4. PID[7] is the inverse of the exclusive-or of PID bits 1, 3, 4 and 5.
       The UART hardware calculates and inserts these bits in the serial stream.


--- p553 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
        Writing UxP1L automatically clears the UxTXCHK and UxRXCHK registers and generates the Break,
        the delimiter bit, the Sync character (55h), and the PID transmission portion of the transaction. The
        data portion of the transaction that follows, if there is one, is a Client process. See the LIN Client
        Mode section for more details of that process. The host receives its own PID if RXEN is set. Software
        performs the Client process corresponding to the PID that was sent and received. Attempting to
        write UxP1L before an active Host process is complete will not succeed. Instead, the TXWRE bit will
        be set.

34.4.2 LIN Client Mode
        The LIN Client mode is configured by the following settings:
        •   MODE = 1011
        •   TXEN = 1
        •   RXEN = 1
        •   UxP2 = number of data bytes to transmit
        •   UxP3 = number of data bytes to receive
        •   UxBRG = value to achieve default baud rate
        •   TXPOL = 0 (for high Idle state)
        •   STP = desired Stop bits selection
        •   C0EN = desired Checksum mode
        •   RxyPPS = TX pin selection code
        •   TX pin TRIS control = 0
        •   ON = 1
        The Client process starts upon detecting a Break on the RX pin. The Break clears the UxTXCHK,
        UxRXCHK, UxP2 and UxP3 registers. At the end of the Break, the auto-baud circuity is activated
        and the baud rate is automatically set using the Sync character following the Break. The character
        following the Sync character is received as the PID code and is saved in the receive FIFO. The UART
        computes the two PID parity bits from the six Least Significant bits of the PID. If either parity bit
        does not match the corresponding bit of the received PID code, the PERIF flag is set and saved at the
        same FIFO location as the PID code. The UxRXIF bit is set indicating that the PID is available.
        Software retrieves the PID by reading the UxRXB register and determines the Client process to
        execute from that. The checksum method, number of data bytes, and whether to send or receive
        data are defined by the software according to the PID code.

34.4.2.1 LIN Client Receiver
        When the Client process is a Receiver, the software performs the following tasks:
        •   The UxP3 register is written with a value equal to the number of data bytes to receive
        •   The C0EN bit is set or cleared to select the appropriate checksum. This must be completed before
            the Start bit of the checksum byte is received.
        •   Each byte of the process response is read from UxRXB when UxRXIF is set
        The UART updates the checksum on each received byte. When the last data byte is received, the
        computed checksum total is stored in the UxRXCHK register. The next received byte is saved in the
        receive FIFO and added with the value in UxRXCHK. The result of this addition is not accessible.
        However, if the result is not all ‘1’s, the CERIF bit is set. The CERIF flag persists until cleared by
        software. Software needs to read UxRXB to remove the checksum byte from the FIFO, but the byte
        can be discarded if not needed for any other purpose.
        After the checksum is received, the UART ignores all activity on the RX pin until a Break starts the
        next transaction.


--- p554 ---
                                                                                                                            PIC18F27/47/57Q43
                                                                                                         UART - Universal Asynchronous Receiver
                                                                                                              Transmitter with Protocol Support
34.4.2.2 LIN Client Transmitter
        When the Client process is a transmitter, software performs the following tasks in the order shown:
        •     The UxP2 register is written with a value equal to the number of bytes to transmit. This will
              enable the UxTXIF flag which is disabled when UxP2 is ‘0’.
        •     The C0EN bit is set or cleared to select the appropriate checksum
        •     Each byte of the process response is written to UxTXB when UxTXIF is set
        The UART accumulates the checksum as each byte is written to UxTXB. After the last byte is written,
        the UART stores the calculated checksum in the UxTXCHK register and transmits the inverted result
        as the last byte in the response.
        The UxTXIF flag is disabled when the number of bytes specified by the value in the UxP2 register
        have been written. Any writes to UxTXB that exceed the UxP2 count will be ignored and set the
        TXWRE flag.

34.5    DALI Mode (Full-Featured UARTs Only)
        DALI is a protocol used for intelligent lighting control for building automation. The protocol consists
        of Control Devices and Control Gear. A Control Device is an application controller that sends
        out commands to the light fixtures. The light fixture itself is termed as a Control Gear. The
        communication is done using Manchester encoding, which is performed by the UART hardware.
        There are two types of Manchester encoding: traditional and differential. The type used by Microchip
        is traditional manchester encoding. It consists of the clock and data in a single bit stream (refer
        to Figure 34-9). A high-to-low or a low-to-high transition always occurs in the middle of the bit
        period and may or may not occur at the bit period boundaries. When the consecutive bits in the
        bit stream are of the same value (i.e., consecutive ‘1’s or consecutive ‘0’s), a transition occurs at
        the bit boundary. However, when the bit value changes, there is no transition at the bit boundary.
        According to the standard, a half-bit time is typically 416.7 μs long. A double half-bit time or a single
        bit is typically 833.3 μs.
        The protocol is inherently half-duplex. Communication over the bus occurs in the form of forward
        and backward frames. Wait times between the frames are defined in the standard to prevent
        collision between the frames.
        A Control Device transmission is termed as the forward frame. In the DALI 2.0 standard, a forward
        frame can be two or three bytes in length. The two-byte forward frame is used for communication
        between Control Device and Control Gear whereas the three-byte forward frame is used for
        communication between Control Devices on the bus. The first byte in the forward frame is the
        control byte and is followed by either one or two data bytes. The transaction begins when the
        Control Device starts a transmission. Unlike other protocols, each byte in the frame is transmitted
        MSb first. Typical frame timing is shown below.

        Figure 34-7. DALI Frame Timing

                                                                                                                                           Rev. 10-000331A
                                   Control                                                                            Control                      9/5/2017


                                    Code      Byte 1                                                                   Code Byte 1
                Write to UxTXB
                                        Start bit                                                         Stop bits   Wait Period    Start bit
                         TX pin                     CC<7>   CC<6>        CC<0>   byte1<7>     byte1<0>


                       UxTXIF
               (Transmit Buffer
            Reg Empty Flag) bit
             TXMTIF (Transmit
               Shift Reg Empty
                       Flag) bit


--- p555 ---
                                                                                                                                    PIC18F27/47/57Q43
                                                                                                                 UART - Universal Asynchronous Receiver
                                                                                                                      Transmitter with Protocol Support
During the communication between two Control Devices, three bytes are required to be transmitted.
In this case, the software must write the third byte to UxTXB as soon as UxTXIF goes true and
before the output shifter becomes empty. This ensures that the three bytes of the forward frame are
transmitted back-to-back without any interruption.
All Control Gear on the bus receive the forward frame. If the forward frame requires a reply to be
sent, one of the Control Gear may respond with a single byte, called the backward frame. The 2.0
standard requires the Control Gear to begin transmission of the backward frame between 5.5 ms to
10.5 ms (~14 to 22 half-bit times) after reception of the forward frame. Once the backward frame
is received by the Control Device, it is required to wait a minimum of 2.4 ms (~6 half-bit times).
After this wait time, the Control Device is free to transmit another forward frame. Refer to the figure
below.

Figure 34-8. DALI Forward/Backward Frame Timing

                                                                                                                                                      Rev. 10-000332A
                                                                                                                                                              9/7/2017


                                            forward wait period                                    forward wait period
                                Forward                            Forward                                                 Forward
          Device TX              Frame                              Frame                                                   Frame


                                                                                        Backward
            Gear TX                                                                      Frame
                                                       backward wait period


   Gear UxTXB write


A Start bit is used to indicate the start of the forward and backward frames. When ABDEN = 0,
the receiver bit rate is determined by the BRG register. When ABDEN = 1, the first bit synchronizes
the receiver with the transmitter and sets the receiver bit rate. The low period of the Start bit is
measured and is used as the timing reference for all data bits in the forward and backward frames.
The ABDOVF bit is set if the Start bit low period causes the measurement counter to overflow. All the
bits following the Start bit are data bits. The bit stream terminates when no transition is detected in
the middle of a bit period. Refer to the figure below.

Figure 34-9. Manchester Timing

                                                                                                                                                      Rev. 10-000330A
                                                                                                                                                              9/5/2017


                       Byte 0      Byte 1                                                                                                 Byte 0
    Write to UxTXB
                           Start bit                              byte 0                               byte 1                Stop bits   Idle      Start bit
             TX pin
                                          b7 = 1     b6 = 0       b5 = 0    b4 = 1   b0 = 1   b7 = 0    b6 = 1    b0 = 0
           UxTXIF
   (Transmit Buffer
Reg Empty Flag) bit
  TXMTIF (Transmit
   Shift Reg Empty
           Flag) bit


The forward and backward frames are terminated by two Idle bit periods or Stop bits. Normally,
these start in the first bit period of a byte. If both Stop bits are valid, the byte reception is
terminated.
If either of the Stop bits is invalid, the frame is tagged as invalid by saving it as a null byte and setting
the framing error in the receive FIFO.


--- p556 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                       UART - Universal Asynchronous Receiver
                                                                                            Transmitter with Protocol Support
       A framing error also occurs when no transition is detected on the bus in the middle of a bit period
       when the byte reception is not complete. In such a scenario, the byte will be saved with the FERIF bit
       set.

34.5.1 Control Device
       The Control Device mode is configured with the following settings:
       •   MODE = ‘b1000
       •   TXEN = 1
       •   RXEN = 1
       •   UxP1 = forward frames are held for transmission with this number of half-bit periods after the
           completion of a forward or backward frame
       •   UxP2 = forward/backward frame threshold delimiter. Any reception that starts this number of
           half-bit periods after the completion of a forward or backward frame is detected as forward
           frame and sets the PERIF flag of the corresponding received byte.
       •   UxBRG = value to achieve 1200 baud rate
       •   TXPOL = appropriate polarity for interface circuit
       •   STP = ‘b10 for two Stop bits
       •   RxyPPS = TX pin selection code
       •   TX pin TRIS control = 0
       •   ON = 1
       A forward frame is initiated by writing the control byte to the UxTXB register. After sending the
       control byte, each data byte must be written to the UxTXB register as soon as UxTXIF goes true. It is
       necessary to perform every write after UxTXIF goes true to ensure that the transmit buffer is ready
       to accept the byte. Each write must also occur before the TXMTIF bit goes true, to ensure that the bit
       stream of the forward frame is generated without interruption.
       When TXMTIF goes true, indicating the transmit shift register has completed sending the last byte in
       the frame, the TX output is held in Idle state for the number of half-bit periods selected by the STP
       bits.
       After the last Stop bit, the TX output is held in the Idle state for an additional wait time determined
       by the half-bit period count in the UxP1 register. For example, a 2450 μs delay (~6 half-bit times)
       requires a value of 6 in UxP1L.
       Any writes to the UxTXB register that occur after TXMTIF goes true, but before the UxP1 wait time
       expires, are held and then transmitted immediately following the wait time. If a backward frame is
       received during the wait time, any bytes that may have been written to UxTXB will be transmitted
       after completion of the backward frame reception plus the UxP1 wait time.
       The wait timer is reset by the backward frame and starts over immediately following the reception
       of the Stop bits of the backward frame. Data pending in the transmit shift register will be sent when
       the wait time elapses.
       To replace or delete any pending forward frame data, the TXBE bit needs to be set to flush the
       shift register and transmit buffer. A new control byte can then be written to the UxTXB register. The
       control byte will be held in the buffer and sent at the beginning of the next forward frame following
       the UxP1 wait time.
       In Control Device mode, PERIF is set when a forward frame is received. This helps the software to
       determine whether the received byte is part of a forward frame from a Control Device (either from
       the Control Device under consideration or from another Control Device on the bus) or a backward
       frame from a Control Gear.


--- p557 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
34.5.2 Control Gear
       The Control Gear mode is configured with the following settings:
       •   MODE = ‘b1001
       •   TXEN = 1
       •   RXEN = 1
       •   UxP1 = back frames are held for transmission with this number of half-bit periods after the
           completion of a forward frame
       •   UxP2 = forward/back frame threshold delimiter. Idle periods longer than this number of half-bit
           periods are detected as forward frames.
       •   UxBRG = value to achieve 1200 baud rate
       •   TXPOL = appropriate polarity for interface circuit
       •   RXPOL = same as TXPOL
       •   STP = ‘b10 for two Stop bits
       •   RxyPPS = TX pin output code
       •   TX pin TRIS control = 0
       •   RXPPS = RX pin selection code
       •   RX pin TRIS control = 1
       •   Input pin ANSEL bit = 0
       •   ON = 1
       The UART starts listening for a forward frame when the Control Gear mode is entered. Only the
       frames that follow an Idle period longer than UxP2 half-bit periods are detected as forward frames.
       Backward frames from other Control Gear are ignored. Only forward frames will be stored in UxRXB.
       This is necessary because a backward frame can be sent only as a response to a forward frame.
       The forward frame is received one byte at a time in the receive FIFO and retrieved by reading the
       UxRXB register. The end of the forward frame starts a timer to delay the backward frame response
       by a wait time equal to the number of half-bit periods stored in UxP1.
       The data received in the forward frame is processed by the application software. If the application
       decides to send a backward frame in response to the forward frame, the value of the backward
       frame is written to UxTXB. This value is held for transmission in the transmit shift register until the
       wait time expires, being transmitted afterward.
       If the backward frame data are written to UxTXB after the wait time has expired, it is held in the
       UxTXB register until the end of the wait time following the next forward frame. The TXMTIF bit
       is false when the backward frame data are held in the transmit shift register. Receiving a UxRXIF
       interrupt before the TXMTIF goes true indicates that the backward frame write was too late and
       another forward frame was received before sending the backward frame. The pending backward
       frame is flushed by setting the TXBE bit to prevent it from being sent after the next forward frame.

34.6   General Purpose Manchester (Full-Featured UARTs Only)
       General purpose Manchester is a subset of the DALI mode. When the UxP1L register is cleared,
       there is no minimum wait time between frames. This allows full- and half-duplex operation because
       writes to the UxTXB register are not held waiting for a receive operation to complete.
       General purpose Manchester operation maintains all other aspects of DALI mode as shown in Figure
       34-9 such as:
       •   Single-pulse Start bit
       •   Most Significant bit first


--- p558 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                          UART - Universal Asynchronous Receiver
                                                                                               Transmitter with Protocol Support
       •   No stop periods between back-to-back bytes
       The general purpose Manchester mode is configured with the following settings:
       •   MODE = ‘b1000
       •   TXEN = 1
       •   RXEN = 1
       •   UxP1 = 0h
       •   UxBRG = desired baud rate
       •   TXPOL and RXPOL = desired Idle state
       •   STP = desired number of stop periods
       •   RxyPPS = TX pin selection code
       •   TX pin TRIS control = 0
       •   RXPPS = RX pin selection code
       •   RX pin TRIS control = 1
       •   Input pin ANSEL bit = 0
       •   ON = 1
       The Manchester bit stream timing is shown in Figure 34-9.

34.7   Polarity
       Receive and transmit polarity is user selectable and affects all modes of operation.
       The idle level is programmable with the TXPOL and RXPOL polarity control bits. Both control bits
       default to ‘0’, which selects a high idle level for transmit and receive. The low level Idle state is
       selected by setting the control bit to ‘1’. TXPOL controls the TX idle level. RXPOL controls the RX idle
       level.

34.8   Stop Bits
       The number of Stop bits is user selectable with the STP bits. The STP bits affect all modes of
       operation.
       Stop bits selections are shown in the table below:

       Table 34-1. Stop Bits Selections
                          Transmitter Stop Bits                                      Receiver Verification
                                    1                                                       Verify Stop bit
                                   1.5                                                    Verify first Stop bit
                                    2                                                 Verify both Stop bits
                                    2                                               Verify only first Stop bit

       In all modes, except DALI, the transmitter is Idle for the number of Stop bit periods between
       each consecutively transmitted word. In DALI, the Stop bits are generated after the last bit in the
       transmitted data stream.
       The input is checked for the idle level in the middle of the first Stop bit, when receive verify on first is
       selected, as well as in the middle of the second Stop bit, when verify on both is selected. If any Stop
       bit verification indicates a nonidle level, the framing error FERIF bit is set for the received word.

34.8.1 Delayed Receive Interrupt
       When operating in Half Duplex mode, where the microcontroller needs to reverse the transceiver
       direction after a reception, it may be more convenient to hold off the UxRXIF interrupt until the end
       of the Stop bits to avoid line contention. The user selects when the UxRXIF interrupt occurs with


--- p559 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
        the STPMD bit. When STPMD is ‘1’, the UxRXIF interrupt occurs at the end of the last Stop bit. When
        STPMD is ‘0’, the UxRXIF interrupt occurs when the received byte is stored in the receive FIFO. When
        STP = 10, the store operation is performed in the middle of the second Stop bit. Otherwise, it is
        performed in the middle of the first Stop bit.
        The FERIF and PERIF interrupts are not delayed with STPMD. When STPMD is set, the preferred
        indicator for reversing transceiver direction is the UxRXIF interrupt because it is delayed whereas the
        others are not.

34.9    Operation After FIFO Overflow
        The Receive Shift Register (RSR) can be configured to stop or continue running during a receive FIFO
        Overflow condition. Stopped operation is the Legacy mode.
        When the RSR continues to run during an Overflow condition, the first word received after clearing
        the overflow will always be valid.
        When the RSR is stopped during an Overflow condition, the synchronization with the Start bits is
        lost. Therefore, the first word received after the overflow is cleared may start in the middle of a
        word.
        Operation during overflow is selected with the RUNOVF bit. When the RUNOVF bit is set, the receiver
        maintains synchronization with the Start bits throughout the Overflow condition.

34.10 Receive and Transmit Buffers
        The UART uses small buffer areas to transmit and receive data. These are sometimes referred to as
        FIFOs.
        The receiver has a Receive Shift Register (RSR) and two or more buffer registers. The buffer at the
        top of the FIFO (earliest byte to enter the FIFO) is retrieved by reading the UxRXB register.
        The transmitter has one or more Transmit Shift Register (TSR) and one buffer register. Writes to
        UxTXB go to the transmit buffer and then immediately to the TSR, if it is empty. When the TSR is not
        empty, writes to UxTXB are held and then transferred to the TSR when it becomes available.

34.10.1 FIFO Status
        The UxFIFO register contains several Status bits for determining the state of the receive and transmit
        buffers.
        The RXBE bit indicates that the receive FIFO is empty. This bit is essentially the inverse of UxRXIF. The
        RXBF bit indicates that the receive FIFO is full.
        The TXBE bit indicates that the transmit buffer is empty (same as UxTXIF) and the TXBF bit indicates
        that the buffer is full. A third transmitter Status bit, TXWRE (transmit write error), is set whenever a
        UxTXB write is performed when the TXBF bit is set. This indicates that the write was unsuccessful.

34.10.2 FIFO Reset
        All modes support resetting the receive and transmit buffers.
        The receive buffer is flushed and all unread data discarded when the RXBE bit is written to ‘1’.
        Instead of using a BSF instruction to set RXBE, the MOVWF instruction with the TXBE bit cleared will be
        used to avoid inadvertently clearing a byte pending in the TSR when UxTXB is empty.
        Data written to UxTXB when TXEN is low will be held in the Transmit Shift Register (TSR), then sent
        when TXEN is set. The transmit buffer and inactive TSR are flushed by setting the TXBE bit. Setting
        TXBE while a character is actively transmitting from the TSR will complete the transmission without
        being flushed.
        Clearing the ON bit will discard all received data and transmit data pending in the TSR and UxTXB.


--- p560 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                           UART - Universal Asynchronous Receiver
                                                                                                Transmitter with Protocol Support
34.11 Flow Control
        This section does not apply to the LIN, DALI, or DMX modes.
        Flow control is the means by which a sending UART data stream can be suspended by a receiving
        UART. Flow control prevents input buffers from overflowing without software intervention. The UART
        supports both hardware and XON/XOFF methods of flow control.
        The flow control method is selected with the FLO bits. Flow control is disabled when both bits are
        cleared.

34.11.1 Hardware Flow Control
        The hardware flow control is selected by setting the FLO bits to ‘10’.
        The hardware flow control consists of three lines. The RS-232 signal names for two of these are RTS
        and CTS. Both are low true. The third line is called TXDE for transmit drive enable which may be
        used to control an RS-485 transceiver. This output is high when the TX output is actively sending a
        character and low at all other times. The UART is configured as DTE (computer) equipment, which
        means RTS is an output and CTS is an input.
        The RTS and CTS signals work as a pair to control the transmission flow. A DTE-to-DTE configuration
        connects the RTS output of the receiving UART to the CTS input of the sending UART. Refer to the
        following figure.

        Figure 34-10. Hardware Flow Control Connections

                                                                                   Rev. 10-000333A
                                                                                          1/11/2019


                                               UART 1                    UART 2

                                                       RX                TX

                                                      RTS                CTS


                                                       TX                RX

                                                      CTS                RTS


        The UART receiving data asserts the RTS output low when the input FIFO is empty. When a character
        is received, the RTS output goes high until the UxRXB is read to free up both FIFO locations.
        When the CTS input goes high after a byte has started to transmit, the transmission will complete
        normally. The receiver accommodates this by accepting the character in the second FIFO location
        even when the CTS input is high.

34.11.2 RS-485 Transceiver Control
        The hardware flow control can be used to control the direction of an RS-485 transceiver as shown in
        the following figure. The CTS input will be configured to be always enabled by setting the UxCTSPPS
        selection to an unimplemented PORT pin, such as RD0. When the signal and control lines are
        configured as shown in the figure below, the UART will not receive its own transmissions. To verify
        that there are no collisions on the RS-485 lines, the transceiver RE control can be disconnected
        from TXDE and tied low, thereby enabling loopback reception of all transmissions. See the Collision
        Detection section for more information.


--- p561 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                   UART - Universal Asynchronous Receiver
                                                                                                        Transmitter with Protocol Support
       Figure 34-11. RS-485 Configuration

                                                                                    Rev. 10-000334A
                                                                                            9/6/2017


                                                 UART
                                                                        SN75176    Vcc


                                                        RX               R               4k7


                                                                         RE   A
                                                     TXDE
                                                                         DE B
                                                        TX               D               4k7


                                                                                   Gnd
                                                      CTS(1)

                                             Note 1: Configure UxCTSPPS to an
                                                     unimplemented input such as RD0.
                                                     (e.g. UxCTSPPS = 0x18)


34.11.3 XON/XOFF Flow Control
       XON/XOFF flow control is selected by setting the FLO bits to ‘01’.
       XON/XOFF is a data-based flow control method. The signals to suspend and resume transmission
       are special characters sent by the receiver to the transmitter. The advantage is that additional
       hardware lines are not needed.
       XON/XOFF flow control requires full-duplex operation because the transmitter must be able to
       receive the signal to suspend transmitting while the transmission is in progress. Although XON and
       XOFF are not defined in the ASCII code, the generally accepted values are 13h for XOFF and 11h for
       XON. The UART uses those codes.
       The transmitter defaults to XON, or transmitter enabled. This state is also indicated by the read-only
       XON bit.
       When an XOFF character is received, the transmitter stops transmitting after completing the
       character actively being transmitted. The transmitter remains disabled until an XON character is
       received.
       XON will be forced on when software toggles the TXEN bit.
       When the RUNOVF bit is set, the XON and XOFF characters continue to be received and processed
       without the need to clear the input FIFO by reading UxRXB. However, if the RUNOVF bit is clear then
       UxRXB must be read to avoid a receive overflow which will suspend flow control when the receive
       buffer overflows.

34.12 Checksum (Full-Featured UARTs Only)
       This section does not apply to the LIN mode, which handles checksums automatically.
       The transmit and receive checksum adders are enabled when the C0EN bit is set. When enabled,
       the adders accumulate every byte that is transmitted or received. The accumulated sum includes
       the carry of the addition. Software is responsible for clearing the checksum registers before a
       transaction and performing the check at the end of the transaction.
       The following examples illustrate how the checksum registers can be used in the Asynchronous
       modes.

34.12.1 Transmit Checksum Method
       1. Clear the UxTXCHK register.


--- p562 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                        UART - Universal Asynchronous Receiver
                                                                                             Transmitter with Protocol Support
       2. Set the C0EN bit.
       3. Send all bytes of the transaction output.
       4. Invert UxTXCHK and send the result as the last byte of the transaction.

34.12.2 Receive Checksum Method
       1. Clear the UxRXCHK register.
       2. Set the C0EN bit.
       3. Receive all bytes in the transaction including the checksum byte.
       4. Set MSb of UxRXCHK if 7-bit mode is selected.
       5. Add ‘1’ to UxRXCHK.
       6. If the result is ‘0’, the checksum passes, otherwise it fails.
       The CERIF Checksum Interrupt flag is not active in any mode other than LIN.

34.13 Collision Detection (Full-Featured UARTs Only)
       External forces that interfere with the transmit line are detected in all modes of operation with
       collision detection. Collision detection is always active when RXEN and TXEN are both set. When
       the receive input is connected to the transmit output through either the same I/O pin or external
       circuitry, a character will be received for every character transmitted. The collision detection circuit
       provides a warning when the word received does not match the word transmitted.
       The TXCIF flag is used to signal collisions. This signal is only useful when the TX output is looped
       back to the RX input and everything that is transmitted is expected to be received. If more than one
       transmitter is active at the same time, it can be assumed that the TX word will not match the RX
       word. The TXCIF detects this mismatch and flags an interrupt. The TXCIF bit will also be set in DALI
       mode transmissions when the received bit is missing the expected mid-bit transition.
       Collision detection is always active, regardless of whether or not the RX input is connected to the
       TX output. It is up to the user to disable the TXCIE bit when collision interrupts are not required.
       The software overhead of unloading the receive buffer of transmitted data are avoided by setting
       the RUNOVF bit and ignoring the receive interrupt and letting the receive buffer overflow. When
       the transmission is complete, prepare for receiving data by flushing the receive buffer (see the FIFO
       Reset section) and clearing the RXFOIF overflow flag.

34.14 RX/TX Activity Time-Out
       The UART works in conjunction with the HLT timers to monitor activity on the RX and TX lines. Use
       this feature to determine when there has been no activity on the receive or transmit lines for a
       user-specified period of time.
       To use this feature, set the HLT to the desired time-out period by a combination of the HLT clock
       source, timer prescale value and timer period registers. Configure the HLT to reset on the UART TX
       or RX line and start the HLT at the same time the UART is started. UART activity will keep resetting
       the HLT to prevent a full HLT period from elapsing. When there has been no activity on the selected
       TX or RX line for longer than the HLT period, an HLT interrupt will occur signaling the time-out event.
       For example, the following register settings will configure HLT2 for a 5 ms time-out of no activity on
       U1RX:
       • T2PR = 0x9C (156 prescale periods)
       •   T2CLKCON = 0x05 (500 kHz internal oscillator)
       •   T2HLT = 0x04 (free running, reset on rising edge)
       •   T2RST = 0x15 (reset on U1RX)
       •   T2CON = 0xC0 (Timer2 on with 1:16 prescale)


--- p563 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                         UART - Universal Asynchronous Receiver
                                                                                              Transmitter with Protocol Support
34.15 Clock Accuracy with Asynchronous Operation
      The factory calibrates the internal oscillator block output (INTOSC). However, the INTOSC frequency
      may drift as VDD or temperature changes, which directly affects the asynchronous baud rate. Two
      methods may be used to adjust the baud rate clock, but both require a reference clock source of
      some kind.
      The first (preferred) method uses the OSCTUNE register to adjust the INTOSC output. Adjusting the
      value of the OSCTUNE register allows for fine resolution changes to the system clock source. See the
      “HFINTOSC Frequency Tuning” section for more information.
      The other method adjusts the value of the Baud Rate Generator. This can be done automatically
      with the Auto-Baud Detect feature (see the Auto-Baud Detect section). There may not be fine
      enough resolution when adjusting the Baud Rate Generator to compensate for a gradual change of
      the peripheral clock frequency.

34.16 UART Baud Rate Generator
      The Baud Rate Generator (BRG) is a 16-bit timer that is dedicated to the support of the UART
      operation. The UxBRG register pair determines the period of the free-running baud rate timer. The
      multiplier of the baud rate period is determined by the BRGS bit.
      The high baud rate range (BRGS = 1) is intended to extend the baud rate range up to a faster rate
      when the desired baud rate is not otherwise possible and to improve the baud rate resolution at
      high baud rates. Using the normal baud rate range (BRGS = 0) is recommended when the desired
      baud rate is achievable with either range.


                   Important: BRGS = 1 is not supported in the DALI mode.


      Writing a new value to UxBRG causes the BRG timer to be reset (or cleared). This ensures that the
      BRG does not wait for a timer overflow before outputting the new baud rate.
      If the system clock is changed during an active receive operation, a receive error or data loss may
      result. To avoid this problem, check the status of the RXIDL bit to make sure that the receive
      operation is Idle before changing the system clock. The following table contains formulas for
      determining the baud rate.

      Table 34-2. Baud Rate Formulas
           BRGS                        BRG/UART Mode                                      Baud Rate Formula
             1                           High Rate                                        Fosc/[4(UxBRG+1)]
             0                          Normal Rate                                       Fosc/[16(UxBRG+1)]

      The following example provides a sample calculation for determining the baud rate and baud rate
      error.

              Example 34-1. Baud Rate Error Calculation
              For a device with Fosc of 16 MHz, desired baud rate of 9600, Asynchronous mode,
              and BRGS = 0.
                                        FOSC
              DesiredBaudrate =
                                   16 × UxBRG + 1
              Solving for UxBRG:
                                 FOSC
              UxBRG =                         −1
                         16 × DesiredBaudrate


--- p564 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                       UART - Universal Asynchronous Receiver
                                                                                            Transmitter with Protocol Support
               UxBRG = 16000000 − 1
                       16 × 9600
               UxBRG = 103.17 ≃ 103
                                         16000000
               CalculatedBaudrate =
                                       16 × 103 + 1
               CalculatedBaudrate = 9615

               Error = CalculatedBaudrate − DesiredBaudrate
                                 DesiredBaudrate

               Error = 9615 − 9600
                          9600
               Error ≃ 0.16 %


34.16.1 Auto-Baud Detect
       The UART module supports automatic detection and calibration of the baud rate in the 8-bit
       Asynchronous and LIN modes. However, setting ABDEN to start auto-baud detection is neither
       necessary, nor possible in LIN mode because that mode supports auto-baud detection automatically
       at the beginning of every data packet. Enabling auto-baud detect with the ABDEN bit applies to the
       Asynchronous modes only.
       When Auto-Baud Detect (ABD) is active, the clock to the BRG is reversed. Rather than the BRG
       clocking the incoming RX signal, the RX signal is timing the BRG. The Baud Rate Generator is used to
       time the period of a received 55h (ASCII “U”), which is the Sync character for the LIN bus. The unique
       feature of this character is that it has five falling edges, including the Start bit edge, and five rising
       edges, including the Stop bit edge.
       In 8-bit Asynchronous mode, setting the ABDEN bit enables the auto-baud calibration sequence. The
       first falling edge of the RX input after ABDEN is set will start the auto-baud calibration sequence.
       While the ABD sequence takes place, the UART state machine is held in Idle. On the first falling edge
       of the receive line, the UxBRG begins counting up using the BRG counter clock, as shown in the
       following figure. The fifth falling edge will occur on the RX pin at the beginning of the bit 7 period.
       At that time, an accumulated value totaling the proper BRG period is left in the UxBRG register pair,
       the ABDEN bit is automatically cleared and the ABDIF interrupt flag is set. ABDIF must be cleared by
       software.


--- p565 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                 UART - Universal Asynchronous Receiver
                                                                                                      Transmitter with Protocol Support
       Figure 34-12. Automatic Baud Rate Calibration

                                                                                                                           Rev. 10-000120B
                                                                                                                                   9/6/2017


              BRG Value        XXXXh   0000h                                                                     001Ch
                                                     Edge #1      Edge #2      Edge #3    Edge #4      Edge #5

                   RX pin                         start bit 0 bit 1 bit 2 bit 3 bit 4 bit 5 bit 6 bit 7


              BRG Clock


                  ABDEN                  Set by user in 8-bit mode                Auto cleared


                   RXIDL
                                                                                                                         Cleared by
                    ABDIF                                                                                                software
        (Interrupt Flag) bit

                  UxBRG                                  XXXXh                                                   001Ch


       RXIDL indicates that the sync input is active. RXIDL will go low on the first falling edge and go high on
       the fifth rising edge.
       The BRG auto-baud clock is determined by the BRGS bit, as shown in the following table.

       Table 34-3. BRG Counter Clock Rates
                BRGS                           BRG Base Clock                                          BRG ABD Clock
                  1                                Fosc/4                                                  Fosc/32
                  0                               Fosc/16                                                 Fosc/128

       During ABD, the internal BRG register is used as a 16-bit counter. However, the UxBRG registers
       retain the previous BRG value until the auto-baud process is successfully completed. While
       calibrating the baud rate period, the internal BRG register is clocked at 1/8th the BRG base clock
       rate. The resulting byte measurement is the average bit time when clocked at full speed and is
       transferred to the UxBRG registers when complete.


                        Important:
                        1. When both the WUE and ABDEN bits are set, the auto-baud detection will
                           occur on the byte following the Break character (see the Auto Wake-on-Break
                           section).
                        2. It is up to the user to verify that the incoming character baud rate is within
                           the range of the selected BRG clock source. Some combinations of oscillator
                           frequency and UART baud rates are not possible.


34.16.2 Auto-Baud Overflow
       During the course of automatic baud detection, the ABDOVF bit will be set if the baud rate counter
       overflows before the fifth falling edge is detected on the RX pin. The ABDOVF bit indicates that the
       counter has exceeded the maximum count that can fit in the 16 bits of the UxBRG register pair.
       After the ABDOVF bit has been set, the state machine continues to search until the fifth falling edge
       is detected on the RX pin. Upon detecting the fifth falling RX edge, the hardware will set the ABDIF


--- p566 ---
                                                                                                                                                       PIC18F27/47/57Q43
                                                                                                                                    UART - Universal Asynchronous Receiver
                                                                                                                                         Transmitter with Protocol Support
       Interrupt flag and clear the ABDEN bit. The UxBRG register values retain their previous value. The
       ABDIF flag and ABDOVF flag can be cleared by software directly. To generate an interrupt on an
       Auto-Baud Overflow condition, all the following bits must be set:
       • ABDOVE bit
       •   UxEIE bit in the PIEx register
       •   Global Interrupt Enable bits
       To terminate the auto-baud process before the ABDIF flag is set, clear the ABDEN bit, then clear the
       ABDOVF bit.

34.16.3 Auto Wake-on-Break
       During Sleep mode, all clocks to the UART are suspended. Because of this, the Baud Rate Generator
       is inactive and a proper character reception cannot be performed. The Auto Wake-on-Break feature
       allows the controller to wake up due to activity on the RX line.
       The Auto-Wake-up feature is enabled by setting both the WUE bit and the UxIE bit in the PIEx
       register. Once set, the normal receive sequence on RX is disabled, and the UART remains in an Idle
       state, monitoring for a wake-up event independent of the CPU mode. A wake-up event consists of a
       transition out of the Idle state on the RX line (this coincides with the start of a Break or a wake-up
       signal character for the LIN protocol).
       The UART module generates a WUIF interrupt coincident with the wake-up event. The interrupt
       is generated synchronously to the Q clocks in normal CPU operating modes (Figure 34-13) and
       asynchronously if the device is in Sleep mode (Figure 34-14). The interrupt condition is cleared by
       clearing the WUIF bit.

       Figure 34-13. Auto-Wake-Up Timing During Normal Operation

                                                                                                                                                                                   Rev. 10-000326B
                                                                                                                                                                                          1/11/2019


                      q1   q2    q3     q4   q1   q2   q3   q4    q1   q2   q3   q4   q1    q2   q3   q4   q1   q2   q3   q4   q1   q2   q3   q4   q1   q2     q3   q4   q1   q2   q3       q4

            FOSC

                      Bit set by user                                                                                                                   Auto cleared
           WUE bit


            RX line


             WUIF
                                                                                                                                         Cleared by software


            Note 1: The UART remains in Idle while the WUE bit is set.


--- p567 ---
                                                                                                                                            PIC18F27/47/57Q43
                                                                                                                         UART - Universal Asynchronous Receiver
                                                                                                                              Transmitter with Protocol Support
        Figure 34-14. Auto-Wake-Up Timing During Sleep

                                                                                                                                                                       Rev. 10-000327B
                                                                                                                                                                               9/6/2017


                       q1   q2    q3     q4   q1   q2   q3   q4                 q1                  q2   q3   q4   q1   q2   q3   q4   q1   q2     q3   q4   q1   q2   q3       q4

             FOSC

                       Bit set by user                                                                                                      Auto cleared
            WUE bit


             RX line


              WUIF
                                                                                                                             Cleared by software

                                 Sleep command executed                              Sleep ends


             Note 1: The UART remains in Idle while the WUE bit is set.


        To generate an interrupt on a wake-up event, all the following bits must be set:
        • The UxIE bit in the PIEx register
        •   Global interrupt enables
        The WUE bit is automatically cleared by the transition to the Idle state on the RX line at the end of
        the Break. This signals to the user that the Break event is over. At this point, the UART module is in
        Idle mode, waiting to receive the next character.

34.16.3.1 Auto-Wake-Up Special Considerations
        Break Character
        To avoid character errors or character fragments during a wake-up event, all bits in the character
        causing the Wake event must be zero.
        When the wake-up is enabled, the function works independent of the low time on the data stream.
        If the WUE bit is set and a valid nonzero character is received, the low time from the Start bit to the
        first rising edge will be interpreted as the wake-up event. The remaining bits of the character will
        be received as a fragmented character and subsequent characters can result in framing or overrun
        errors.
        Therefore, the initial character of the transmission must be all zeros. This must be eleven or more
        bit times, 13 bit times recommended for LIN bus, or any number of bit times for standard RS-232
        devices.
        Oscillator Start-Up Time
        The oscillator start-up time must be considered, especially in applications using oscillators with
        longer start-up intervals (i.e., LP, XT or HS/PLL modes). The Sync Break (or wake-up signal) character
        must be of sufficient length and must be be followed by a sufficient interval to allow enough time for
        the selected oscillator to start and provide proper initialization of the UART.
        The WUE Bit
        To ensure that no actual data are lost, check the RXIDL bit to verify that a receive operation is not in
        process before setting the WUE bit. If a receive operation is not occurring, the WUE bit may then be
        set just prior to entering the Sleep mode.

34.17 Transmitting a Break
        The UART module has the capability of sending either a fixed length Break period or a software-
        timed Break period. The fixed length Break consists of a Start bit, followed by 12 ‘0’ bits and a Stop
        bit. The software-timed Break is generated by setting and clearing the BRKOVR bit.


--- p568 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                           UART - Universal Asynchronous Receiver
                                                                                                Transmitter with Protocol Support
      To send the fixed length Break, set the SENDB and TXEN bits. The Break sequence is then initiated
      by a write to UxTXB. The timed Break will occur first, followed by the character written to UxTXB that
      initiated the Break. The initiating character is typically the Sync character of the LIN specification.
      SENDB is disabled in the LIN and DMX modes because those modes generate the Break sequence
      automatically.
      The SENDB bit is automatically reset by hardware after the Break Stop bit is complete.
      The TXMTIF bit indicates when the transmit operation is Active or Idle, just as it does during normal
      transmission. The following figure illustrates the Break sequence.

      Figure 34-15. Send-Break Sequence


                                   Sync                                                                                Rev. 10-000118B

                                   Write                                                                                       9/6/2017


           Write to UxTXB


              BRG Output
              (Shift Clock)

                                                                                                                           Sync
                     TX pin                    Start bit   bit 0      bit 1                   bit 11        Stop bit       start
                  UxTXIF                                                  Break
          (Transmit Buffer
       Reg Empty Flag) bit
        TXMTIF (Transmit
          Shift Reg Empty
                  Flag) bit

                  SENDB
                                                                                             Auto cleared
              (send break
                control bit)


34.18 Receiving a Break
      The UART has counters to detect when the RX input remains in the Space state for an extended
      period of time. When this happens, the RXBKIF bit is set.
      A Break is detected when the RX input remains in the Space state for 11 bit periods for
      asynchronous and LIN modes and 23 bit periods for DMX mode.
      The user can select to receive the Break interrupt as soon as the Break is detected or at the end
      of the Break, when the RX input returns to the Idle state. When the RXBIMD bit is ‘1’, then RXBKIF
      is set immediately upon Break detection. When RXBIMD is ‘0’, then RXBKIF is set when the RX input
      returns to the Idle state.

34.19 UART Operation During Sleep
      The UART ceases to operate during Sleep. The safe way to wake the device from Sleep by a serial
      operation is to use the Wake-on-Break feature of the UART. See the Auto Wake-on-Break section.

34.20 Register Definitions: UART
      Long bit name prefixes for the UART peripherals are shown in the following table. Refer to the “Long
      Bit Names” section in the “Register and Bit Naming Conventions” chapter for more information.

      Table 34-4. UART Long Bit Name Prefixes
                                    Peripheral                                                  Bit Name Prefix
                               UART1 (full featured)                                                   U1


--- p569 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                   UART - Universal Asynchronous Receiver
                                                                                        Transmitter with Protocol Support
...........continued
                             Peripheral                                                 Bit Name Prefix
                       UART2 (limited features)                                                U2
                       UART3 (limited features)                                                U3
                       UART4 (limited features)                                                U4
                       UART5 (limited features)                                                U5


--- p570 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                               UART - Universal Asynchronous Receiver
                                                                                                    Transmitter with Protocol Support
34.20.1 UxCON0

            Name:       UxCON0
            Address:    0x2AB,0x2BE,0x2D1,0x2E4,0x2F7

            UART Control Register 0

      Bit         7           6                 5              4                 3             2           1                  0
                BRGS        ABDEN             TXEN           RXEN                                MODE[3:0]
  Access        R/W          R/W              R/W            R/W                R/W           R/W        R/W                R/W
   Reset          0           0                 0              0                 0             0           0                 0

Bit 7 – BRGS Baud Rate Generator Speed Select
            Value      Description
            1          Baud Rate Generator is high speed with 4 baud clocks per bit
            0          Baud Rate Generator is normal speed with 16 baud clocks per bit

Bit 6 – ABDEN Auto-Baud Detect Enable(3)
            Value      Description
            1          Auto-baud is enabled. Receiver is waiting for Sync character (0x55).
            0          Auto-baud is not enabled or auto-baud is complete

Bit 5 – TXEN Transmit Enable Control(2)
            Value      Description
            1          Transmit is enabled. TX output pin drive is forced on when transmission is active and is controlled by PORT
                       TRIS control when transmission is Idle.
            0          Transmit is disabled. TX output pin drive is controlled by PORT TRIS control.

Bit 4 – RXEN Receive Enable Control(2)
            Value      Description
            1          Receiver is enabled
            0          Receiver is disabled

Bits 3:0 – MODE[3:0] UART Mode Select(1)
            Value      Description
            1111 -     Reserved
            1101
            1100       LIN Host/Client mode(4)
            1011       LIN Client Only mode(4)
            1010       DMX mode(4)
            1001       DALI Control Gear mode(4)
            1000       DALI Control Device mode(4)
            0111 -     Reserved
            0101
            0100       Asynchronous 9-bit UART Address mode. 9th bit: 1 = address, 0 = data
            0011       Asynchronous 8-bit UART mode with 9th bit even parity
            0010       Asynchronous 8-bit UART mode with 9th bit odd parity
            0001       Asynchronous 7-bit UART mode
            0000       Asynchronous 8-bit UART mode


--- p571 ---
                                                                                                  PIC18F27/47/57Q43
                                                                               UART - Universal Asynchronous Receiver
                                                                                    Transmitter with Protocol Support
Notes:
1. Changing the UART MODE while ON = 1 may cause unexpected results.
2. Clearing TXEN or RXEN will not clear the corresponding buffers. Use TXBE or RXBE to clear the
   buffers.
3. ABDEN is read-only when MODE > ‘b0111.
4. Full-featured UARTs only.


--- p572 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                UART - Universal Asynchronous Receiver
                                                                                                     Transmitter with Protocol Support
34.20.2 UxCON1

            Name:       UxCON1
            Address:    0x2AC,0x2BF,0x2D2,0x2E5,0x2F8

            UART Control Register 1

      Bit        7              6               5                4             3                2              1               0
                ON                                             WUE          RXBIMD                          BRKOVR          SENDB
  Access        R/W                                           R/W/HC          R/W                             R/W           R/W/HC
   Reset         0                                               0             0                               0               0

Bit 7 – ON Serial Port Enable
            Value      Description
            1          Serial port enabled
            0          Serial port disabled (held in Reset)

Bit 4 – WUE Wake-Up Enable
            Value      Description
            1          Receiver is waiting for falling RX input edge which will set the UxIF bit. Cleared by hardware on wake-up event.
                       Also requires the UxIE bit of PIEx to enable wake.
            0          Receiver operates normally

Bit 3 – RXBIMD Receive Break Interrupt Mode Select
            Value      Description
            1          Set RXBKIF immediately when RX in has been low for the minimum Break time
            0          Set RXBKIF on rising RX input after RX in has been low for the minimum Break time

Bit 1 – BRKOVR Send Break Software Override
            Value      Description
            1          TX output is forced to non-Idle state
            0          TX output is driven by transmit shift register

Bit 0 – SENDB Send Break Control(1)
            Value      Description
            1          Output Break upon UxTXB write. Written byte follows Break. Bit is cleared by hardware.
            0          Break transmission completed or disabled

            Note:
            1. This bit is read-only in LIN, DMX and DALI modes.


--- p573 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                 UART - Universal Asynchronous Receiver
                                                                                                      Transmitter with Protocol Support
34.20.3 UxCON2

            Name:       UxCON2

            UART Control Register 2

      Bit        7             6                 5                4                  3        2                1               0
              RUNOVF        RXPOL                     STP[1:0]                     C0EN     TXPOL                  FLO[1:0]
  Access        R/W         R/W/HC              R/W              R/W               R/W       R/W             R/W              R/W
   Reset         0             0                 0                0                  0        0               0                0

Bit 7 – RUNOVF Run During Overflow Control
            Value      Description
            1          RX input shifter continues to synchronize with Start bits after Overflow condition
            0          RX input shifter stops all activity on receiver Overflow condition

Bit 6 – RXPOL Receive Polarity Control
            Value      Description
            1          Invert RX polarity, Idle state is low
            0          RX polarity is not inverted, Idle state is high

Bits 5:4 – STP[1:0] Stop Bit Mode Control(1)
            Value      Description
            11         Transmit 2 Stop bits, receiver verifies first Stop bit
            10         Transmit 2 Stop bits, receiver verifies first and second Stop bits
            01         Transmit 1.5 Stop bits, receiver verifies first Stop bit
            00         Transmit 1 Stop bit, receiver verifies first Stop bit

Bit 3 – C0EN Checksum Mode Select(2)
            Value      Condition                      Description
            1          MODE = LIN                     Enhanced LIN checksum includes PID in sum
            0          MODE = LIN                     Legacy LIN checksum does not include PID in sum
            1          MODE = not LIN                 Checksum is the sum of all TX and RX characters
            0          MODE = not LIN                 Checksum is disabled

Bit 2 – TXPOL Transmit Control Polarity(1)
            Value      Description
            1          Output data are inverted, TX output is low in Idle state
            0          Output data are not inverted, TX output is high in Idle state

Bits 1:0 – FLO[1:0] Handshake Flow Control
            Value      Description
            11         Reserved
            10         RTS/CTS and TXDE Hardware flow control
            01         XON/XOFF Software flow control
            00         Flow control is off

            Notes:
            1. All modes transmit selected number of Stop bits.
            2. Full-featured UARTs only.


--- p574 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                 UART - Universal Asynchronous Receiver
                                                                                                      Transmitter with Protocol Support
34.20.4 UxERRIR

            Name:        UxERRIR

            UART Error Interrupt Flag Register

      Bit         7             6               5                4                 3            2             1              0
               TXMTIF         PERIF          ABDOVF            CERIF             FERIF        RXBKIF        RXFOIF         TXCIF
  Access        R/S/C        R/W/HC           R/W/S            R/W/S             R/S/C        R/W/S         R/W/S          R/W/S
   Reset          1             0               0                0                 0            0             0              0

Bit 7 – TXMTIF Transmit Shift Register Empty Interrupt Flag
            Value       Description
            1           Transmit shift register is empty (Set at end of Stop bits)
            0           Transmit shift register is actively shifting data

Bit 6 – PERIF Parity Error Interrupt Flag
            Value       Condition                      Description
            1           MODE = LIN or Parity           Unread byte at top of input FIFO has parity error
            0           MODE = LIN or Parity           Unread byte at top of input FIFO does not have parity error
            1           MODE = DALI Device             Unread byte at top of input FIFO received as Forward Frame
            0           MODE = DALI Device             Unread byte at top of input FIFO received as Back Frame
            1           MODE = Address                 Unread byte at top of input FIFO received as address
            0           MODE = Address                 Unread byte at top of input FIFO received as data
            x           MODE = All others              Not used

Bit 5 – ABDOVF Auto-baud Detect Overflow Interrupt Flag
            Value       Condition                Description
            1           MODE = DALI              Start bit measurement overflowed counter
            0           MODE = DALI              No overflow during Start bit measurement
            1           MODE = All others        Baud Rate Generator overflowed during the auto-detection sequence
            0           MODE = All others        Baud Rate Generator has not overflowed

Bit 4 – CERIF Checksum Error Interrupt Flag
            Value       Condition                                            Description
            1           MODE = DALI                                          Stop bit detected
            0           MODE = DALI                                          Stop bit not detected
            x           MODE = not DALI                                      Not used

Bit 3 – FERIF Framing Error Interrupt Flag
            Value       Description
            1           Unread byte at top of input FIFO has framing error
            0           Unread byte at top of input FIFO does not have framing error

Bit 2 – RXBKIF Break Reception Interrupt Flag
            Value       Description
            1           Break detected
            0           No break detected

Bit 1 – RXFOIF Receive FIFO Overflow Interrupt Flag
            Value       Description
            1           Receive FIFO has overflowed
            0           Receive FIFO has not overflowed

Bit 0 – TXCIF Transmit Collision Interrupt Flag(1)


--- p575 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                 UART - Universal Asynchronous Receiver
                                                                                      Transmitter with Protocol Support
Value     Description
1         Transmitted word is not equal to the word received during transmission
0         Transmitted word equals the word received during transmission

Note:
1. Full-featured UARTs only.


--- p576 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                               UART - Universal Asynchronous Receiver
                                                                                                    Transmitter with Protocol Support
34.20.5 UxERRIE

            Name:       UxERRIE

            UART Error Interrupt Enable Register

      Bit       7              6             5               4                 3           2                1              0
              TXMTIE         PERIE        ABDOVE           CERIE             FERIE       RXBKIE           RXFOIE         TXCIE
  Access       R/W            R/W           R/W             R/W               R/W         R/W              R/W            R/W
   Reset        0              0             0               0                 0           0                0              0

Bit 7 – TXMTIE Transmit Shift Register Empty Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 6 – PERIE Parity Error Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 5 – ABDOVE Auto-baud Detect Overflow Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 4 – CERIE Checksum Error Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 3 – FERIE Framing Error Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 2 – RXBKIE Break Reception Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 1 – RXFOIE Receive FIFO Overflow Interrupt Enable
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

Bit 0 – TXCIE Transmit Collision Interrupt Enable(1)
            Value      Description
            1          Interrupt enabled
            0          Interrupt not enabled

            Note:
            1. Full-featured UARTs only.


--- p577 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                 UART - Universal Asynchronous Receiver
                                                                                                      Transmitter with Protocol Support
34.20.6 UxUIR

           Name:        UxUIR
           Address:     0x2B1,0x2C4,0x2D7,0x2EA,0x2FD

           UART General Interrupt Flag Register

     Bit         7             6                 5               4                  3         2                1               0
               WUIF          ABDIF                                                          ABDIE
  Access       R/W/S         R/W/S                                                           R/W
   Reset         0             0                                                              0

Bit 7 – WUIF Wake-Up Interrupt
           Value       Description
           1           Idle to non-Idle transition on RX line detected when WUE is set. Also sets UxIF. (WUIF must be cleared by
                       software to clear UxIF)
           0           WUE not enabled by software or no transition detected

Bit 6 – ABDIF Auto-Baud Detect Interrupt
           Value       Description
           1           Auto-baud detection complete. Status shown in UxIF when ABDIE is set. (Must be cleared by software)
           0           Auto-baud not enabled or auto-baud enabled and auto-baud detection not complete

Bit 2 – ABDIE Auto-Baud Detect Interrupt Enable
           Value       Description
           1           ABDIF will set the UxIF bit in the PIRx register
           0           ABDIF will not set UxIF


--- p578 ---
                                                                                                                       PIC18F27/47/57Q43
                                                                                                    UART - Universal Asynchronous Receiver
                                                                                                         Transmitter with Protocol Support
34.20.7 UxFIFO

            Name:        UxFIFO
            Address:     0x2B0,0x2C3,0x2D6,0x2E9,0x2FC

            UART FIFO Status Register

      Bit         7             6                5                 4               3              2                1                0
                TXWRE         STPMD            TXBE              TXBF            RXIDL           XON             RXBE             RXBF
  Access        R/W/S          R/W            R/W/S/C            R/S/C           R/S/C           S/C            R/W/S/C           R/S/C
   Reset          0             0                1                 0               1              1                1                0

Bit 7 – TXWRE Transmit Write Error Status (must be cleared by software)
            Value       Condition            Description
            1           MODE = LIN Host       UxP1L was written when a host process was active
            1           MODE = LIN Client     UxTXB was written when UxP2 = 0 or more than UxP2 bytes have been written to
                                              UxTXB since last Break
            1           MODE = Address detect UxP1L was written before the previous data in UxP1L was transferred to TX shifter
            1           MODE = All            A new byte was written to UxTXB when the output FIFO was full
            0           MODE = All            No error

Bit 6 – STPMD Stop Bit Detection Mode
            Value       Condition                 Description
            1           STP = 11                  Assert UxRXIF at end of first Stop bit
            1           STP ≠ 11                  Assert UxRXIF at end of last Stop bit
            0           STP = xx                  Assert UxRXIF in middle of first Stop bit


Bit 5 – TXBE Transmit Buffer Empty Status
            Value       Description
            1           Transmit buffer is empty. Setting this bit will clear the transmit buffer and output shift register.
            0           Transmit buffer is not empty. Software cannot clear this bit.

Bit 4 – TXBF Transmit Buffer Full Status
            Value       Description
            1           Transmit buffer is full
            0           Transmit buffer is not full

Bit 3 – RXIDL Receive Pin Idle Status
            Value       Description
            1           Receive pin is in Idle state
            0           UART is receiving Start, Stop, Data, Auto-baud, or Break

Bit 2 – XON Software Flow Control Transmit Enable Status
            Value       Description
            1           Transmitter is enabled
            0           Transmitter is disabled

Bit 1 – RXBE Receive Buffer Empty Status
            Value       Description
            1           Receive buffer is empty. Setting this bit will clear the RX buffer(1).
            0           Receive buffer is not empty. Software cannot clear this bit.

Bit 0 – RXBF Receive Buffer Full Status
            Value       Description
            1           Receive buffer is full
            0           Receive buffer is not full


--- p579 ---
                                                                                                 PIC18F27/47/57Q43
                                                                              UART - Universal Asynchronous Receiver
                                                                                   Transmitter with Protocol Support
Note:
1. The BSF instruction will not be used to set RXBE because doing so will clear a byte pending in the
   transmit shift register when the UxTXB register is empty. Instead, use the MOVWF instruction with
   a ‘0’ in the TXBE bit location.


--- p580 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                          UART - Universal Asynchronous Receiver
                                                                                               Transmitter with Protocol Support
34.20.8 UxBRG

           Name:       UxBRG
           Address:    0x2AE,0x2C1,0x2D4,0x2E7,0x2FA

           UART Baud Rate Generator

     Bit        15          14           13             12          11                10                9              8
                                                          BRG[15:8]
  Access       R/W          R/W         R/W            R/W         R/W               R/W              R/W            R/W
   Reset        0            0           0              0            0                0                0              0

     Bit        7            6            5              4                   3            2             1              0
                                                               BRG[7:0]
  Access       R/W          R/W         R/W            R/W                  R/W      R/W              R/W            R/W
   Reset        0            0           0              0                    0        0                0              0

Bits 15:0 – BRG[15:0] Baud Rate Generator Value
         The UART Baud Rate equals [Fosc*(1+(BRGS*3)]/[(16*(BRG+1))]

           Notes:
           1. The individual bytes in this multibyte register can be accessed with the following register names:
               – UxBRGH: Accesses the high byte BRG[15:8]
                – UxBRGL: Accesses the low byte BRG[7:0]
           2. The UxBRG registers will only be written when ON = 0.
           3. Maximum BRG value when MODE = ‘100x and BRGS = 1 is 0x7FFE.
           4. Maximum BRG value when MODE = ‘100x and BRGS = 0 is 0x1FFE.


--- p581 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                          UART - Universal Asynchronous Receiver
                                                                                               Transmitter with Protocol Support
34.20.9 UxRXB

            Name:      UxRXB
            Address:   0x2A1,0x2B4,0x2C7,0x2DA,0x2ED

            UART Receive Register

      Bit        7           6            5              4                  3             2             1              0
                                                               RXB[7:0]
  Access         R           R            R              R                  R             R             R              R
   Reset         x           x            x              x                  x             x             x              x

Bits 7:0 – RXB[7:0] Top of Receive FIFO


--- p582 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                       UART - Universal Asynchronous Receiver
                                                                                            Transmitter with Protocol Support
34.20.10 UxTXB

            Name:      UxTXB
            Address:   0x2A3,0x2B6,0x2C9,0x2DC,0x2EF

            UART Transmit Register

      Bit        7           6         5              4                   3            2             1              0
                                                            TXB[7:0]
  Access        R/W        R/W        R/W           R/W                  R/W      R/W              R/W            R/W
   Reset         0          0          0             0                    0        0                0              0

Bits 7:0 – TXB[7:0] Bottom of Transmit FIFO


--- p583 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                UART - Universal Asynchronous Receiver
                                                                                                     Transmitter with Protocol Support
34.20.11 UxP1

            Name:        UxP1

            UART Parameter 1

      Bit           15          14             13              12                 11          10               9              8
                                                                                                                            P1[8]
  Access                                                                                                                    R/W
   Reset                                                                                                                      0

      Bit           7            6                 5           4                   3            2              1              0
                                                                      P1[7:0]
  Access         R/W           R/W            R/W             R/W                 R/W        R/W             R/W             R/W
   Reset          0             0              0               0                   0          0               0               0

Bit 8 – P1[8] Parameter 1 Most Significant bit
          UART mode operating parameter values
            Value        Condition                      Description
            n            MODE = DMX                     Most Significant bit of number of bytes to transmit between Start Code and
                                                        automatic Break generation
            n            MODE = DALI Control Device     Most Significant bit of Idle time delay after which a Forward Frame is sent.
                                                        Measured in half-bit periods.
            n            MODE = DALI Control Gear       Most Significant bit of delay between the end of a Forward Frame and the
                                                        start of the Back Frame. Measured in half-bit periods.
            x            All other modes/Limited        Not used
                         featured UART

Bits 7:0 – P1[7:0] Parameter 1 Least Significant bits
          UART mode operating parameter values
            Value        Condition                  Description
            n            MODE = DMX                  Least Significant bits of number of bytes to transmit between Start Code and
                                                     automatic Break generation
            n            MODE = DALI Control Device  Least Significant bits of Idle time delay after which a Forward Frame is sent.
                                                     Measured in half-bit periods.
            n            MODE = DALI Control Gear    Least Significant bits of delay between the end of a Forward Frame and the
                                                     start of the Back Frame. Measured in half-bit periods.
            n            MODE = LIN                  PID to transmit (Only Least Significant six bits used)
            n            MODE = Asynchronous Address Address to transmit (9th transmit bit automatically set to ‘1’)
            x            All other modes                Not used

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • UxP1H: Accesses the high byte P1[8]
            •   UxP1L: Accesses the low byte P1[7:0]


--- p584 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                UART - Universal Asynchronous Receiver
                                                                                                     Transmitter with Protocol Support
34.20.12 UxP2

            Name:         UxP2

            UART Parameter 2

      Bit           15           14             13             12                  11          10               9              8
                                                                                                                             P2[8]
  Access                                                                                                                     R/W
   Reset                                                                                                                       0

      Bit           7            6              5               4                   3           2               1               0
                                                                       P2[7:0]
  Access         R/W           R/W             R/W            R/W                  R/W        R/W             R/W             R/W
   Reset          0             0               0              0                    0          0               0               0

Bit 8 – P2[8] Parameter 2 Most Significant bit
          UART mode operating parameter values
            Value        Condition                            Description
            n            MODE = DMX                           Most Significant bit of first address of receive block
            n            MODE = DALI                          Most Significant bit of number of half-bit periods of Idle time in Forward
                                                              Frame detection threshold
            x            All other modes/Limited featured     Not used
                         UART

Bits 7:0 – P2[7:0] Parameter 2 Least Significant bits
          UART mode operating parameter values
            Value        Condition                  Description
            n            MODE = DMX                  Least Significant bits of first address of receive block
            n            MODE = DALI                 Least Significant bits of number of half-bit periods of Idle time in Forward
                                                     Frame detection threshold
            n            MODE = LIN                  Number of data bytes to transmit
            n            MODE = Asynchronous Address Receiver address
            x            All other modes             Not used

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • UxP2H: Accesses the high byte P2[8]
            •   UxP2L: Accesses the low byte P2[7:0]


--- p585 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                   UART - Universal Asynchronous Receiver
                                                                                                        Transmitter with Protocol Support
34.20.13 UxP3

            Name:         UxP3

            UART Parameter 3

      Bit           15           14            13                12                 11            10               9                  8
                                                                                                                                    P3[8]
  Access                                                                                                                            R/W
   Reset                                                                                                                              0

      Bit           7            6              5                4                   3             2               1                 0
                                                                        P3[7:0]
  Access         R/W           R/W            R/W            R/W                    R/W          R/W              R/W               R/W
   Reset          0             0              0              0                      0            0                0                 0

Bit 8 – P3[8] Parameter 3 Most Significant bit
          UART mode operating parameter values
            Value        Condition                                          Description
            n            MODE = DMX                                         Most Significant bit of last address of receive block
            x            All other modes/Limited featured UART              Not used

Bits 7:0 – P3[7:0] Parameter 3 Least Significant bits
          UART mode operating parameter values
            Value        Condition                  Description
            n            MODE = DMX                  Least Significant bits of last address of receive block
            n            MODE = LIN Client           Number of data bytes to receive
            n            MODE = Asynchronous Address Receiver address mask. Received address is XOR’d with UxP2L, then AND’d
                                                     with UxP3L. Match occurs when result is zero.
            x            All other modes             Not used

            Notes: The individual bytes in this multibyte register can be accessed with the following register
            names:
            • UxP3H: Accesses the high byte P3[8]
            •   UxP3L: Accesses the low byte P3[7:0]


--- p586 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                              UART - Universal Asynchronous Receiver
                                                                                                   Transmitter with Protocol Support
34.20.14 UxTXCHK

           Name:        UxTXCHK
           Address:     0x02A4

           UART Transmit Checksum Result Register

     Bit           7          6              5              4           3                     2               1            0
                                                             TXCHK[7:0]
  Access       R/W           R/W            R/W           R/W         R/W                   R/W             R/W           R/W
   Reset        0             0              0             0            0                    0               0             0

Bits 7:0 – TXCHK[7:0] Transmit Checksum Value
           Value       Condition                                      Description
           n           MODE = LIN and C0EN = 1                        Sum of all transmitted bytes including PID
           n           MODE = LIN and C0EN = 0                        Sum of all transmitted bytes except PID
           n           MODE = All others and C0EN = 1                 Sum of all transmitted bytes since last clear
           x           MODE = All others and C0EN = 0                 Not used


--- p587 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                              UART - Universal Asynchronous Receiver
                                                                                                   Transmitter with Protocol Support
34.20.15 UxRXCHK

           Name:        UxRXCHK
           Address:     0x02A2

           UART Receive Checksum Result Register

     Bit           7          6              5              4           3                     2                1           0
                                                             RXCHK[7:0]
  Access       R/W           R/W            R/W           R/W         R/W                   R/W             R/W          R/W
   Reset        0             0              0             0            0                    0               0            0

Bits 7:0 – RXCHK[7:0] Receive Checksum Value
           Value       Condition                                        Description
           n           MODE = LIN and C0EN = 1                          Sum of all received bytes including PID
           n           MODE = LIN and C0EN = 0                          Sum of all received bytes except PID
           n           MODE = All others and C0EN = 1                   Sum of all received bytes since last clear
           x           MODE = All others and C0EN = 0                   Not used


--- p588 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                     UART - Universal Asynchronous Receiver
                                                                                                          Transmitter with Protocol Support
34.21 Register Summary - UART
Address    Name      Bit Pos.     7           6           5                 4                  3            2           1            0
0x02A1     U1RXB       7:0                                                       RXB[7:0]
0x02A2    U1RXCHK      7:0                                                      RXCHK[7:0]
0x02A3     U1TXB       7:0                                                       TXB[7:0]
0x02A4    U1TXCHK     7:0                                                       TXCHK[7:0]
                      7:0                                                         P1[7:0]
0x02A5     U1P1
                      15:8                                                                                                         P1[8]
                      7:0                                                         P2[7:0]
0x02A7     U1P2
                      15:8                                                                                                         P2[8]
                      7:0                                                         P3[7:0]
0x02A9     U1P3
                      15:8                                                                                                        P3[8]
0x02AB    U1CON0      7:0        BRGS       ABDEN       TXEN              RXEN                                MODE[3:0]
0x02AC    U1CON1      7:0         ON                                      WUE         RXBIMD                        BRKOVR      SENDB
0x02AD    U1CON2      7:0       RUNOVF      RXPOL              STP[1:0]                 C0EN              TXPOL          FLO[1:0]
                      7:0                                                      BRG[7:0]
0x02AE    U1BRG
                      15:8                                                    BRG[15:8]
0x02B0     U1FIFO     7:0       TXWRE       STPMD       TXBE              TXBF         RXIDL               XON        RXBE         RXBF
0x02B1     U1UIR      7:0        WUIF       ABDIF                                                         ABDIE
0x02B2    U1ERRIR     7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF        RXBKIF     RXFOIF        TXCIF
0x02B3    U1ERRIE     7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE        RXBKIE     RXFOIE        TXCIE
0x02B4     U2RXB      7:0                                                         RXB[7:0]
0x02B5    Reserved
0x02B6     U2TXB       7:0                                                        TXB[7:0]
0x02B7    Reserved
                      7:0                                                         P1[7:0]
0x02B8     U2P1
                      15:8
                      7:0                                                         P2[7:0]
0x02BA     U2P2
                      15:8
                      7:0                                                         P3[7:0]
0x02BC     U2P3
                      15:8
0x02BE    U2CON0      7:0        BRGS       ABDEN       TXEN              RXEN                                MODE[3:0]
0x02BF    U2CON1      7:0         ON                                      WUE           RXBIMD                      BRKOVR      SENDB
0x02C0    U2CON2      7:0       RUNOVF      RXPOL              STP[1:0]                                   TXPOL          FLO[1:0]
                      7:0                                                      BRG[7:0]
0x02C1    U2BRG
                      15:8                                                    BRG[15:8]
0x02C3     U2FIFO     7:0       TXWRE       STPMD       TXBE              TXBF         RXIDL               XON        RXBE         RXBF
0x02C4     U2UIR      7:0        WUIF       ABDIF                                                         ABDIE
0x02C5    U2ERRIR     7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF        RXBKIF     RXFOIF
0x02C6    U2ERRIE     7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE        RXBKIE     RXFOIE
0x02C7     U3RXB      7:0                                                         RXB[7:0]
0x02C8    Reserved
0x02C9     U3TXB       7:0                                                        TXB[7:0]
0x02CA    Reserved
                      7:0                                                         P1[7:0]
0x02CB     U3P1
                      15:8
                      7:0                                                         P2[7:0]
0x02CD     U3P2
                      15:8
                      7:0                                                         P3[7:0]
 0x02CF    U3P3
                      15:8
0x02D1    U3CON0      7:0        BRGS       ABDEN       TXEN              RXEN                                MODE[3:0]
0x02D2    U3CON1      7:0         ON                                      WUE           RXBIMD                      BRKOVR      SENDB
0x02D3    U3CON2      7:0       RUNOVF      RXPOL              STP[1:0]                                   TXPOL          FLO[1:0]
                      7:0                                                      BRG[7:0]
0x02D4    U3BRG
                      15:8                                                    BRG[15:8]
0x02D6     U3FIFO     7:0       TXWRE       STPMD       TXBE              TXBF         RXIDL               XON        RXBE         RXBF
0x02D7     U3UIR      7:0        WUIF       ABDIF                                                         ABDIE
0x02D8    U3ERRIR     7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF        RXBKIF     RXFOIF
0x02D9    U3ERRIE     7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE        RXBKIE     RXFOIE
0x02DA     U4RXB      7:0                                                         RXB[7:0]
0x02DB    Reserved


--- p589 ---
                                                                                                                                  PIC18F27/47/57Q43
                                                                                                               UART - Universal Asynchronous Receiver
                                                                                                                    Transmitter with Protocol Support
...........continued
 Address               Name    Bit Pos.     7           6           5                 4                  3            2           1            0
 0x02DC            U4TXB         7:0                                                        TXB[7:0]
 0x02DD           Reserved
                                7:0                                                         P1[7:0]
  0x02DE               U4P1
                                15:8
                                7:0                                                         P2[7:0]
  0x02E0               U4P2
                                15:8
                                7:0                                                         P3[7:0]
  0x02E2               U4P3
                                15:8
  0x02E4           U4CON0       7:0        BRGS       ABDEN       TXEN              RXEN                                MODE[3:0]
  0x02E5           U4CON1       7:0         ON                                      WUE           RXBIMD                      BRKOVR      SENDB
  0x02E6           U4CON2       7:0       RUNOVF      RXPOL              STP[1:0]                                   TXPOL          FLO[1:0]
                                7:0                                                      BRG[7:0]
  0x02E7               U4BRG
                                15:8                                                    BRG[15:8]
  0x02E9           U4FIFO       7:0       TXWRE       STPMD       TXBE              TXBF         RXIDL               XON        RXBE         RXBF
  0x02EA           U4UIR        7:0        WUIF       ABDIF                                                         ABDIE
  0x02EB          U4ERRIR       7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF        RXBKIF     RXFOIF
  0x02EC          U4ERRIE       7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE        RXBKIE     RXFOIE
  0x02ED           U5RXB        7:0                                                         RXB[7:0]
  0x02EE          Reserved
  0x02EF           U5TXB         7:0                                                        TXB[7:0]
  0x02F0          Reserved
                                7:0                                                         P1[7:0]
  0x02F1               U5P1
                                15:8
                                7:0                                                         P2[7:0]
  0x02F3               U5P2
                                15:8
                                7:0                                                         P3[7:0]
  0x02F5               U5P3
                                15:8
  0x02F7           U5CON0       7:0        BRGS       ABDEN       TXEN              RXEN                                MODE[3:0]
  0x02F8           U5CON1       7:0         ON                                      WUE           RXBIMD                      BRKOVR      SENDB
  0x02F9           U5CON2       7:0       RUNOVF      RXPOL              STP[1:0]                                   TXPOL          FLO[1:0]
                                7:0                                                      BRG[7:0]
  0x02FA               U5BRG
                                15:8                                                    BRG[15:8]
  0x02FC           U5FIFO       7:0       TXWRE       STPMD       TXBE              TXBF         RXIDL               XON        RXBE         RXBF
  0x02FD            U5UIR       7:0        WUIF       ABDIF                                                         ABDIE
  0x02FE           U5ERRIR      7:0       TXMTIF       PERIF     ABDOVF             CERIF              FERIF        RXBKIF     RXFOIF
  0x02FF           U5ERRIE      7:0       TXMTIE       PERIE     ABDOVE             CERIE              FERIE        RXBKIE     RXFOIE


--- p590 ---
