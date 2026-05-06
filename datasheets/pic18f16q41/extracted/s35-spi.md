35.   SPI - Serial Peripheral Interface Module
      The Serial Peripheral Interface (SPI) module is a synchronous serial data communication bus that
      operates in Full Duplex mode. Devices communicate in a host/client environment where the host
      device initiates the communication. A client device is typically controlled through a chip select known
      as Client Select. Some examples of client devices include serial EEPROMs, shift registers, display
      drivers, A/D converters and other PIC® devices with SPI capabilities.
      The SPI bus specifies four signal connections:
      • Serial Clock (SCK)
      •    Serial Data Out (SDO)
      •    Serial Data In (SDI)
      •    Client Select (SS)
      The following figure shows the block diagram of the SPI module.

      Figure 35-1. SPI Module Simplified Block Diagram

                                                                             Data bus
                                                                                                                                            Rev. 10-000076B
                                                                                                                                                   11/2/2018


                                                 Read                                                       Write

                                                           8                                       8

                                                     Receive FIFO                             Transmit FIFO
                                                       (2 deep)                                  (2 deep)

              SDI                                          8                                       8

                      SPIxSDIPPS                       Receive Shift                            Transmit                                           SDO
                                                         Register                              Serializer(1)                      RxyPPS

                            SDIP                                       RXR              TXR
                                                                                                                SDOP
          SS_in
                                            1    1
                    SPIxSSPPS                                                                                                                   SCK_out
                                                 0                                                                                RxyPPS

                          SSP
                                                SSET                                                             CKP
                                                                        SPI Control Module
                                                                       and Transfer Counter

                                                                                                       1    1                                     SS_out
               See                    SCK Generator            1                                            0                      RxyPPS
             SPIxCLK
             Register                                          0
                                                                                                                  SSP
                                                                                                           SSET
                                        SPIxBAUD               MST

                         CLKSEL
          SCK_in
                   SPIxSCKPPS


                           CKP

      Note: 1. If the transmit FIFO is empty and TXR = 1, the previous value of the receive shift register will be sent to the transmit serializer.


      The SPI transmit output (SDO_out) is available to the remappable PPS SDO pin and internally to the
      select peripherals.


--- p567 ---
The SPI bus typically operates with a single host device and one or more client devices. When
multiple client devices are used, an independent Client Select connection is required from the host
device to each client device.
The host selects only one client at a time. Most client devices have tri-state outputs so their output
signal appears disconnected from the bus when they are not selected.
Transmissions typically involve Shift registers, eight bits in size, one in the host and one in the client.
With either the host or the client device, data is always shifted out one bit at a time, with the Most
Significant bit (MSb) shifted out first. At the same time, a new bit is shifted into the device. Unlike
older Microchip devices, the SPI module on this device contains one register for incoming data and
another register for outgoing data. Both registers also have multibyte FIFO buffers and allow for
DMA bus connections.
The figure below shows a typical connection between two devices configured as host and client
devices.

Figure 35-2. SPI Host/Client Connection with FIFOs

                                                                                                                  Rev. 10-000080C
                                                                                                                         1/11/2019


                   SPI Host: MST = 1                                                     SPI Client: MST = 0
                    LSb           MSb                                                    LSb            MSb
                      Transmit Shift        SDOx                             SDIx        Receive Shift
                         Register                                                          Register
                      Transmit FIFO                                                       Receive FIFO
                        (SPIxTXB)                                                          (SPIxRXB)


                                (Note 1)                                                          (Note 1)


                      Receive FIFO                                                       Transmit FIFO
                       (SPIxRXB)                                                           (SPIxTXB)
                      Receive Shift         SDIx                            SDOx        Transmit Shift
                        Register                                                          Register
                                                         Serial clock
                    MSb           LSb       SCKx                             SCKx     MSb           LSb

                                        SSxOUT/          Client Select
                                                                             SSxIN
                         Device 1        GPIO             (optional)                        Device 2

       Notes: 1. In some modes, if the Transmit FIFO is empty, the most recently received byte of data will be transmitted.
              2. This diagram assumes that the LSBF bit is cleared (communications are MSb-first). When LSBF is
              set, the communications will be LSb-first.


Data is shifted out of the transmit FIFO on the programmed clock edge and into the receive Shift
register on the opposite edge of the clock.
The host device transmits information on its SDO output pin which is connected to, and received
by, the client’s SDI input pin. The client device transmits information on its SDO output pin, which is
connected to, and received by, the host’s SDI input pin.
The host device sends out the clock signal. Both the host and the client devices need to be
configured for the same clock phase and clock polarity.
During each SPI clock cycle, a full-duplex data transmission occurs. This means that while the host
device is sending out the MSb from its output register (on its SDO pin) and the client device is
reading this bit and saving it as the LSb of its input register. The client device is also sending out the
MSb from its Shift register (on its SDO pin) and the host device is reading this bit and saving it as the
LSb of its input register.


--- p568 ---
       After eight bits have been shifted out, the host and client have exchanged register values and stored
       the incoming data into the receiver FIFOs.
       If there is more data to exchange, the registers are loaded with new data and the process repeats.
       Whether the data is meaningful or not (dummy data) depends on the application software. This
       leads to three scenarios for data transmission:
       • Host sends useful data and client sends dummy data
       •   Host sends useful data and client sends useful data
       •   Host sends dummy data and client sends useful data
       In this SPI module, dummy data may be sent without software involvement. Dummy transmit data is
       automatically handled by clearing the TXR bit and receive data is ignored by clearing the RXR bit. See
       Table 35-1 as well as Host Mode and Client Mode for further TXR/RXR setting details.
       This SPI module can send transmissions of any number of bits and can send information in
       segments of varying size (from 1-8 bits in width). As such, transmissions may involve any number of
       clock cycles, depending on the amount of data to be transmitted.
       When there is no more data to be transmitted, the host stops sending the clock signal and deselects
       the client. Every client device connected to the bus that has not been selected through its Client
       Select line disregards the clock and transmission signals and does not transmit out any data of its
       own.

35.1   SPI Controls
       The following registers control the SPI operation:
       • SPI Interrupt Flag (SPIxINTF) Register
       •   SPI Interrupt Enable (SPIxINTE) Register
       •   SPI Byte Count High and Low (SPIxTCNTH/L) Registers
       •   SPI Bit Count (SPIxTWIDTH) Register
       •   SPI Baud Rate (SPIxBAUD) Register
       •   SPI Control (SPIxCON0) Register 0
       •   SPI Control (SPIxCON1) Register 1
       •   SPI Control (SPIxCON2) Register 2
       •   SPI FIFO Status (SPIxSTATUS) Register
       •   SPI Receiver Buffer (SPIxRXB) Register
       •   SPI Transmit Buffer (SPIxTXB) Register
       •   SPI Clock Select (SPIxCLK) Register
       SPIxCON0, SPIxCON1 and SPIxCON2 are control registers for the SPI module.
       SPIxSTATUS reflects the status of both the SPI module and the receive and transmit FIFOs.
       SPIxBAUD and SPIxCLK control the Baud Rate Generator (BRG) of the SPI module when in Host
       mode. The SPIxCLK selects the clock source that is used by the BRG. The SPIxBAUD configures the
       clock divider used on that clock source. More information on the BRG is available in the Host Mode
       SPI Clock Configuration section.
       SPIxTxB and SPIxRxB are the Transmit and Receive Buffer registers used to send and receive data on
       the SPI bus. The Transmit and Receive Buffer registers offer indirect access to Shift registers that are
       used for shifting the data in and out. Both registers access the multibyte FIFOs, allowing for multiple
       transmissions or receptions to be stored between software transfers of the data.
       The SPIxTCNTH:L register pair either count or control the number of bits or bytes in a data
       transfer. When BMODE = 1, the SPIxTCNT value signifies bytes and the SPIxTWIDTH value signifies


--- p569 ---
       the number of bits in a byte. When BMODE = 0, the SPIxTCNT value is concatenated with the
       SPIxTWIDTH register to signify bits. In Host Receive Only mode (TXR = 0 and RXR = 1), the data
       transfer is initiated by writing SPIxTCNT with the desired bit or byte value to transfer. In Host
       Transmit mode (TXR = 1), the data transfer is initiated by writing the SPIxTxB register, in which case
       the SPIxTCNT is a down counter for the bits or bytes transferred.
       The SPIxINTF and SPIxINTE are the flags and enables, respectively, for SPI specific interrupts. They
       are tied to the SPIxIF flag and SPIxIE enable bit in the PIR and PIE registers, which is triggered
       when any interrupt contained in the SPIxINTF/SPIxINTE registers is triggered. The PIR/PIE registers
       also contain SPIxTXIF/SPIxTXIE bits, which are the Interrupt flag and Enable bit for the SPI Transmit
       Interrupt, as well as the SPIxRXIF/SPIxRXIE bits, which are the Interrupt flag and Enable bit for the SPI
       receive interrupt.

35.2   SPI Operation
       When initializing the SPI, several options need to be specified. This is done by programming the
       appropriate control bits of the SPIxCON0, SPIxCON1 and SPIxCON2 registers. These control bits
       allow the following to be configured:
       • Host mode (SCK is the clock output)
       •   Client mode (SCK is the clock input)
       •   Clock Polarity (Idle state of SCK)
       •   Input, Output, and Client Select Polarity
       •   Data Input Sample Phase (middle or end of data output time)
       •   Clock Edge (output data on first/second edge of SCK)
       •   Clock Rate (Host mode only)
       •   Client Select mode (Host or Client mode)
       •   MSB-First or LSB-First
       •   Receive/Transmit modes:
            – Full Duplex
            – Receive Only (receive without transmit)
            – Transmit Only (transmit without receive)
       •   Transfer Counter mode (only available in Transmit Only mode)

35.2.1 Enabling and Disabling the SPI Module
       Setting the EN bit enables the SPI peripheral. However, to reset or reconfigure the SPI mode, the EN
       bit must be cleared.
       Setting the EN bit enables the SPI inputs and outputs: SDI, SDO, SCK_out, SCK_in, SS_out and SS_in.
       The pins for all of these inputs and outputs are selected by the PPS controls and thus must have
       their functions mapped properly to the device pins to function. Refer to the “PPS - Peripheral Pin
       Select Module” chapter for more details.
       SS_out and SCK_out must have the pins to which they are assigned set as outputs (TRIS bits must
       be ‘0’) to properly output. Clearing the TRIS bit of the SDO pin will cause the SPI module to always
       control that pin, but is not necessary for SDO functionality (see the Input and Output Polarity Control
       section).
       Configurations selected by the following registers will not be changed while the EN bit is set:
       • SPIxBAUD
       •   SPIxCON1
       •   SPIxCON0 (with the exception of clearing the EN bit)


--- p570 ---
        Clearing the EN bit aborts any transmissions in progress, disables the setting of interrupt flags by
        hardware, and resets the FIFO occupancy (see the Transmit and Receive FIFOs section).

35.2.2 BUSY Bit
        While a data transfer is in progress, the SPI hardware sets the BUSY bit. This bit can be polled by
        the user to determine the current status of the SPI module and to know when a communication is
        complete. The following registers and bits will not be changed by software while the BUSY bit is set:
        • SPIxTCNT
        •   SPIxTWIDTH
        •   SPIxCON2
        •   The CLB bit


                     Important:
                     1. The BUSY bit is subject to synchronization delay of up to two instruction cycles. The
                        user must wait for it to set after loading the transmit buffer (SPIxTXB register) before
                        using it to determine the status of the SPI module.
                     2. It is also not recommended to read SPIxTCNT while the BUSY bit is set, as the value in
                        the registers may not be a reliable indicator of the transfer counter. Use the TCZIF bit to
                        accurately determine that the transfer counter has reached zero.


35.2.3 Transmit and Receive FIFOs
        The transmission and reception of data from the SPI module is handled by two FIFOs, one for
        reception and one for transmission. These are addressed by the SFRs, SPIxRXB and SPIxTXB,
        respectively.
        The transmit FIFO is written to by software and is read by the SPI module to shift the data onto the
        SDO pin. The receive FIFO is written to by the SPI module as it shifts in the data from the SDI pin and
        is read by software. Setting the CLB bit resets the occupancy for both FIFOs, emptying both buffers.
        The FIFOs are also reset by clearing the EN bit, thus disabling the SPI module.


                     Important: The transmit and receive FIFO occupancy refer to the number of bytes that are
                     currently being stored in each FIFO. These values are used in this chapter to illustrate the
                     function of these FIFOs and are not directly accessible through software.


        The SPIxRXB register addresses the receive FIFO and is read-only. Reading from this register will
        read from the first FIFO location that was written to by hardware and decrease the receive FIFO
        occupancy. If the FIFO is empty, reading from this register will instead return a value of ’0’ and set
        the RXRE (Receive Buffer Read Error) bit. The RXRE bit must then be cleared in software to properly
        reflect the status of the read error. When the receive FIFO is full, the RXBF bit will be set.
        The SPIxTXB register addresses the transmit FIFO and is write-only. Writing to the register will write
        to the first empty FIFO location and increase the occupancy. If the FIFO is full, writing to this register
        will not affect the data and will set the TXWE bit. When the transmit FIFO is empty, the TXBE bit will
        be set.
        More details on enabling and disabling the receive and transmit functions is summarized in Table
        35-1 and Client Mode Transmit Options.

35.2.4 LSb vs. MSb-First Operation
        Typically, the SPI communication outputs the Most Significant bit first, but some devices or buses
        may not conform to this standard. In this case, the LSBF bit may be used to alter the order in which


--- p571 ---
        bits are shifted out during the data exchange. In both Host and Client mode, the LSBF bit controls
        whether data is shifted to the MSb or LSb first. Clearing the bit (default) configures the data to
        transfer to the MSb first, which conforms to traditional SPI operation, while setting the bit configures
        the data to transfer to the LSb first.

35.2.5 Input and Output Polarity Control
        SPIxCON1 has three bits that control the polarity of the SPI inputs and outputs:
        • The SDIP bit controls the polarity of the SDI input
        •   The SDOP bit controls the polarity of the SDO output
        •   The SSP bit controls the polarity of both the client SS input and the host SS output
        For all three bits, when the bit is clear, the input or output is active-high, and when the bit is set,
        the input or output is active-low. When the EN bit is cleared, SS_out and SCK_out both revert to the
        Inactive state dictated by their polarity bits. The SDO Output state, when the EN bit is cleared, is
        determined by several factors as follows:
        • When the associated TRIS bit for the SDO pin is cleared and the SPI goes Idle after a transmission,
           the SDO output will remain at the last bit level.
        •   When the associated TRIS bit for the SDO pin is set, its behavior varies in Client and Host modes:
             – In Client mode, the SDO pin tri-states when any of the following is true:
                 • Client Select is inactive
                 • EN = 0
                 • TXR = 0
             – In Host mode:
                 • The SDO pin tri-states when TXR = 0
                 • When TXR = 1 and the SPI goes Idle after a transmission, the SDO output will remain at
                   the last bit level. The SDO pin will revert to the Idle state when EN is cleared.

35.2.6 Transfer Counter
        In all Host modes, the transfer counter can be used to determine how many data transfers the SPI
        will send/receive. The transfer counter is comprised of the SPIxTCNT registers and is also partially
        controlled by the SPIxTWIDTH register.
        The transfer counter has two primary modes, determined by the BMODE bit. Each mode uses the
        SPIxTCNT and SPIxTWIDTH registers to determine the number and size of the transfers. In both
        modes, when the transfer counter reaches zero, the TCZIF interrupt flag is set.


                     Important:
                     In all Client modes and when BMODE = 1 in Host modes, the transfer counter will still
                     decrement as transfers occur and can be used to count the number of messages sent/
                     received, control SS_out, and trigger TCZIF. Also, when BMODE = 1, the SPIxTWIDTH register
                     can be used in Host and Client modes to determine the size of messages sent and received
                     by the SPI, even if the transfer counter is not being actively used to control the number of
                     messages being sent/received by the SPI module.


35.2.6.1 Total Bit Count Mode (BMODE = 0)
        In this mode, SPIxTCNT and SPIxTWIDTH are concatenated to determine the total number of bits
        to be transferred. These bits will be loaded from/into the transmit/receive FIFOs in 8-bit increments
        and the transfer counter will be decremented by eight until the total number of remaining bits is less
        than eight. If there are any remaining bits (SPIxTWIDTH ≠ 0), the transmit FIFO will send out one final
        message with any extra bits greater than the remainder ignored.


--- p572 ---
        The SPIxTWIDTH is the remaining bit count but the value does not change as it does for the
        SPIxTCNT value. The receiver will load a final byte into the receiver FIFO and pad the extra bits with
        zeros. The LSBF bit determines whether the Most Significant or Least Significant bits of this final byte
        are ignored or padded. For example, when LSBF = 0 and the final transfer contains only two bits, if
        the last byte sent was 0x5F, the RXB of the receiver will contain 0x40, which are the two MSbs of the
        final byte padded with zeros in the LSbs.
        In this mode, the SPI host will only transmit messages when the SPIxTCNT value is greater than zero,
        regardless of the TXR and RXR settings.
        In Host Transmit mode, the transfer starts with the data write to the SPIxTXB register or the count
        value written to the SPIxTCNTL register, whichever occurs last.
        In Host Receive Only mode, the transfer clocks start when the SPIxTCNTL value is written. Transfer
        clocks are suspended when the receive FIFO is full and resume as the FIFO is read.

35.2.6.2 Variable Transfer Size Mode (BMODE = 1)
        In this mode, SPIxTWIDTH specifies the width of every individual piece of the data transfer in bits.
        SPIxTCNT specifies the number of transfers of this bit length. If SPIxTWIDTH = 0, each piece is a full
        byte of data. If SPIxTWIDTH ≠ 0, then only that specified number of bits from the transmit FIFO are
        shifted out, with the unused bits ignored.
        Received data is padded with zeros in the unused bit areas when transferred into the receive FIFO.
        The LSBF bit determines whether the Most Significant or Least Significant bits of the transfers are
        ignored or padded.
        In this mode, the transfer counter being zero only stops messages from being sent or received when
        in Receive Only mode.


                    Important:
                    With BMODE = 1, it is possible for the transfer counter (SPIxTCNT) to decrement below
                    zero, although when in Host Receive Only mode, transfer clocks will cease when the
                    transfer counter reaches zero.


35.2.6.3 Transfer Counter in Client Mode
        In Client mode, the transfer counter will still decrement as data is shifted in and out of the SPI
        module, but it will not control data transfers. The BMODE bit along with the transfer counter is used
        to determine when the device will look for Client Select faults.
        When BMODE = 0, the SSFLT bit will be set if Client Select transitions from its Active to Inactive state
        during bytes of data or if it transitions before the last bit sent during the final byte (if SPIxTWIDTH ≠
        0).
        When BMODE = 1, the SSFLT bit will be set if Client Select transitions from its Active to Inactive state
        before the final bit of each individual transfer is completed.
        Note: SSFLT does not have an associated interrupt, so it will be checked in the software. An ideal
        time to do this is when the End of Client Select Interrupt (EOSIF) is triggered (see the Start of Client
        Select and End of Client Select Interrupts section).

35.3    Host Mode
        In Host mode, the device controls the SCK line, and as such, initiates data transfers and determines
        when any clients broadcast data onto the SPI bus.
        Host mode can be configured in four different modes, configured by the TXR and RXR bits:
        • Full Duplex mode
        •   Receive Only mode


--- p573 ---
       •   Transmit Only mode
       •   Transfer Off mode
       The modes are illustrated in the following table:

       Table 35-1. Host Mode TXR/RXR Settings
                                               TXR = 1                                                   TXR = 0
                                         Full Duplex mode                                         Receive Only mode
                  BMODE = 1: Transfer when RxFIFO is not full and TxFIFO is not empty   Transfer when RxFIFO is not full and the
        RXR = 1 BMODE = 0: Transfer when RXFIFO is not full, TXFIFO is not empty, and         Transfer Counter is nonzero
                                 the Transfer Counter is nonzero                        Transmitted data is either the top of the
                                                                                        FIFO or the most recently received data

                                       Transmit Only mode
                            BMODE = 1: Transfer when TxFIFO is not empty
        RXR = 0     BMODE = 0: Transfer when TXFIFO is not empty and the Transfer                     No Transfers
                                         Counter is nonzero
                                      Received data is not stored


35.3.1 Full Duplex Mode
       When both TXR and RXR are set, the SPI host is in Full Duplex mode. In this mode, data transfer
       triggering is affected by the BMODE bit.
       When BMODE = 1, data transfers will occur whenever the receive FIFO is not full and data is
       present in the transmit FIFO. In practice, as long as the receive FIFO is not full, data will be
       transmitted/received as soon as the SPIxTXB register is written to, matching the functionality of SPI
       (MSSP) modules on older 8-bit Microchip devices. The SPIxTCNT will decrement with each transfer.
       However, when SPIxTCNT is zero, the next transfer is not inhibited and the corresponding SPIxTCNT
       decrement will cause the count to roll over to the maximum value. The following figure shows an
       example of a communication using this mode.


--- p574 ---
       Figure 35-3. SPI Host Operation - Data Exchange, RXR = 1, TXR = 1
                                                                                                                                                         Rev. 10-000281A
                                                                                                                                                                11/9/2018

         Software Write to
                             Note 2
               SPIxTCNT
               SPIxTCNT       0             5               4                 3                   2                      1                          0

         Software Write To
                      TXR

                     TXR
         Software Write to
                    RXR
                     RXR

                 SCK_out                                                                                  Note 3

                 SDO_out                                                                                           `HX                             `HX

                  SRMTIF


                   TCZIF                                                                                                         Note 2


            Software Write
               to SPIxTXB
                 TXFIFO       0         1       2       1       2       1             2           1           0                 1                   0
               Occupancy
                  SPIxTIF


           Software Read
           from SPIxRXB
                 RXFIFO                 0               1           0             1       0   1       0       1                           0    1               0
               Occupancy

                  SPIxRIF


                 Notes: 1. SS(out) is not shown on this diagram.
                        2. SPIxTCNT write is optional when TXR/RXR = 1/1 and BMODE = 1. If BMODE = 0, a write to SPIxTCNT is required to
                           start transmission; TCZIF signals the transition of SPIxTCNT from 1 to 0.
                        3. Transmission gap occurs while waiting for transmitter data.


       When BMODE = 0, the transfer counter (SPIxTCNT) must also be written to before transfers will
       occur. Transfers will cease when the transfer counter reaches ‘0’. For example, if SPIxTXB is written
       twice and then SPIxTCNTL is written with ‘3’, the transfer will start with the SPIxTCNTL write. The two
       bytes in the TXFIFO will be sent after which the transfer will suspend until the third and last byte is
       written to SPIxTXB.

35.3.2 Transmit Only Mode
       When TXR is set and RXR is clear, the SPI host is in Transmit Only mode. In this mode, data transfer
       triggering is affected by the BMODE bit.
       When BMODE = 1, data transfers will occur whenever the transmit FIFO is not empty. Data will
       be transmitted as soon as the SPIxTXB register is written to, matching the functionality of the
       SPI (MSSP) modules on previous 8-bit devices. The SPIxTCNT will decrement with each transfer.
       However, when SPIxTCNT is zero, the next transfer is not inhibited and the corresponding SPIxTCNT
       decrement will cause the count to roll over to the maximum value. Any data received in this mode
       is not stored in the receive FIFO. The following figure shows an example of sending a command and
       then sending a byte of data using this mode.


--- p575 ---
       Figure 35-4. SPI Host Operation - Command+Write Data, TXR = 1, RXR = 0
                                                                                                                                                                Rev. 10-000282A
                                                                                                                                                                       11/6/2018


           Software Write to                                                Note 2
                 TXTCNTL
               SPIxTXCNT                           0              -1           -2            3                  2                  1                 0

             Software Write
                    to TXR

                       TXR

             Software Write
                    to RXR
                       RXR

                   SCK_out

                  SDO_out       Shifted data out

                   SRMTIF                                          Note 3


                     BCZIF


             Software Write                                                                                          Note 4
                to SPIxTXB
                   TxFIFO           0              1   2          1             0       1        2          1       2          1                    0
                Occupancy
                   SPIxTIF


                   Notes: 1. SS_out is not shown.
                          2. The byte counter is optional when TXR/RXR = 1/0.
                          3. After the command bytes, wait for SRMTIF before loading SPIxTXB, otherwise the command data will decrement SPIxTXCNT
                             (alternatively, the command bytes can be taken into consideration along with the data being transmitted by loading 0x05 to the
                             SPIxTXCNT register). TCZIF signals the end of the transmission.
                          4. Transmit data interrupt handler (or DMA) must write only the bytes necessary; the byte counter is not available as an indicator.
                          5. Reading the SPIxRXB is not required because RXR = 0.


       When BMODE = 0, the transfer counter (SPIxTCNT) must also be written to before transfers will
       occur, and transfers will cease when the transfer counter reaches ‘0’.
       For example, if SPIxTXB is written twice and then SPIxTCNTL is written with ‘3’, the transfer will start
       with the SPIxTCNTL write. The two bytes in the TXFIFO will be sent after which the transfer will
       suspend until the third and last byte is written to SPIxTXB.

35.3.3 Receive Only Mode
       When RXR is set and TXR is clear, the SPI host is in Receive Only mode. In this mode, data transfers
       when the receive FIFO is not full and the transfer counter is nonzero. In this mode, writing a value to
       SPIxTCNTL will start the clocks for transfer. The clocks will suspend while the receive FIFO is full and
       will cease when the SPIxTCNT reaches zero (see the Transfer Counter section). If there is any data
       in the transmit FIFO, the first data written to SPIxTXB will be transmitted on each data exchange,
       although the transmit FIFO occupancy will not change, meaning that the same message will be sent
       on each transmission. If there is no data in the transmit FIFO, the most recently received data will be
       transmitted. The following figure shows an example of sending a command using the Transmit Only
       mode and then receiving a byte of data using the Receive Only mode.


                               Important: When operating in Receive Only mode and the size of every SPI transaction is
                               less than 8 bits, it is recommended to operate in BMODE = 1 mode. The size of the packet
                               can be configured using the SPIxTWIDTH register.


--- p576 ---
        Figure 35-5. SPI Host Operation - Command+Read Data, TXR = 0, RXR = 1
                                                                                                                                                      Rev. 10-000283A
                                                                                                                                                             11/6/2018


            Software Write to
                    TxCNTL
                 SPIxTXCNT                             0                  -1        -2            3        2                 1                0

            Software Write to
                        TXR

                        TXR
              Software Write
                     to RXR

                        RXR
                    SCK_out

                   SDO_out      Shifted data out

                    SRMTIF                                                Note 2

                      TCZIF


              Software Write
                 to SPIxTXB
                     TXFIFO         0              1       2          1                                            0
                  Occupancy


              Software Read
              from SPIxRXB

                   RXFIFO                                                 0                           1        0         1       0     1          0
                 Occupancy

                    SPIxRIF


                     Notes: 1. SS_out is not shown.
                            2. Software must wait for shift-register empty (SRMTIF) before changing TXR, RXR, SPIxTCNT and SPIxTWIDTH controls.
                               In this case, this is not considered an imposition because the client likely needs time to load output data.


35.3.4 Transfer Off Mode
        When both TXR and RXR are cleared, the SPI host is in Transfer Off mode. In this mode, SCK will not
        toggle and no data is exchanged. However, writes to SPIxTXB will be transferred to the transmit FIFO
        which will then be transmitted when the TXR bit is set.

35.3.5 Host Mode Client Select Control
35.3.5.1 Hardware Client Select Control
        The SPI module allows for direct hardware control of a Client Select output. The Client Select output
        (SS_out) is controlled both directly, through the SSET bit, and indirectly by the hardware while the
        transfer counter is nonzero (see the Transfer Counter section). The SS_out pin is selected with the
        PPS controls. The SS_out polarity is controlled by the SSP bit.
        Setting the SSET bit will assert SS_out. Clearing the SSET bit will leave SS_out to be controlled by
        the transfer counter. When the transfer counter is loaded, the SPI module will automatically assert
        SS_out. When the transfer counter decrements to zero, the SPI module will deassert SS_out either
        one baud period after the final SCK pulse of the final transfer (when CKE/SMP = 0/1) or one half
        baud period otherwise, as shown in the following figure.


--- p577 ---
        Figure 35-6. SPI Host SS Operation - CKE = 0, BMODE = 1, TWIDTH = 0, SSP = 0
                                                                                                                                                          Rev. 10-000284A
                                                                                                                                                                 11/6/2018


                      SPIEN


                 baud_clock


            Software Write to
                 SPIxTCNTL


                    Transfer                                                          1                                                       0
                    Counter


                     SS_out

                                                      minimum 1 baud clock when FST = 0                                approx. 1 baud clock

                    SCK_out


            SDO_bit_number                               7         6         5        4        3       2   1      0


              Notes: 1. SDO bit number illustrates the transmitted bit number and is not intended to imply SDO_out tristate operation.
                     2. Assumes SPIxTXB holds data when SPIxTCNTL is written.


35.3.5.2 Software Client Select Control
        Client Select can be controlled through software via a general purpose I/O pin. In this case, ensure
        that the desired pin is configured as a general purpose output with the PPS and TRIS controls. In
        this case, SSET will not affect the Client Select, the Transfer Counter will not automatically control
        the Client Select output, and all setting and clearing of the Client Select output line must be directly
        controlled by software.

35.3.6 Host Mode SPI Clock Configuration
35.3.6.1 SPI Clock Selection
        The clock source for SPI Host modes is selected by the SPIxCLK register.
        The SPIxBAUD register allows for dividing this clock. The frequency of the SCK output is defined by
        the following equation:

        Equation 35-1. SCK Output Frequency
                              FCSEL
        FBAUD =
                          2 × BAUD + 1

        where FBAUD is the baud rate frequency output on the SCK pin, FCSEL is the frequency of the input
        clock selected by the SPIxCLK register, and BAUD is the value contained in the SPIxBAUD register.
35.3.6.2 Clock and Data Change Alignment
        The CKP, CKE and SMP bits control the relationship between the SCK clock output, SDO output data
        changes, and SDI input data sampling. The bit functions are as follows:
        • CKP controls SCK output polarity
        •     CKE controls SDO output change relative to the SCK clock
        •     SMP controls SDI input sampling relative to the clock edges
        The CKE bit, when set, inverts the low Idle state of the SCK output to a high Idle state.
        The following figures illustrate the eight possible combinations of the CKP, CKE and SMP bit
        selections.


--- p578 ---
             Important: All timing diagrams assume the LSBF bit is cleared.


Figure 35-7. Clocking Detail - Host Mode, CKE = 0, SMP = 0

                                                                                                                                                                             Rev. 10-000276A
                                                                                                                                                                                    11/6/2018
                                                                          MST = 1,CKE = 0, SMP = 0


                           SCK                       A       I   A   I      A     I     A    I      A    I      A    I      A    I   A       I

                           SDO     Previous bit 0        bit 7   bit 6       bit 5       bit 4       bit 3       bit 2       bit 1   bit 0                         CKP = 0

              input sample clock


                           SCK                       A       I   A   I      A     I     A    I      A    I      A    I      A    I   A       I

                           SDO     Previous bit 0        bit 7   bit 6       bit 5       bit 4       bit 3       bit 2       bit 1   bit 0                         CKP = 1

              input sample clock


                                                                                                                                                 RXFIFO Occupancy increments
                                       TXFIFO                                                                 Open RXFIFO                        TXFIFO Occupancy decrements
                                   determined                                                                        latch                       SPIxRIF and SPIxTIF interrupts
                                                                                                                                                 trigger


Figure 35-8. Clocking Detail - Host Mode, CKE = 1, SMP = 1

                                                                                                                                                                             Rev. 10-000315A

                                                                          MST = 1, CKE = 1, SMP = 1                                                                                 11/6/2018


                           SCK                       A       I   A   I      A     I     A    I      A    I      A    I      A    I   A       I

                           SDO                   bit 7       bit 6       bit 5       bit 4       bit 3       bit 2       bit 1   bit 0       next                  CKP = 0
                                       tx_buf
              input sample clock        write


                                                     A       I   A   I      A     I     A    I      A    I      A    I      A    I   A       I
                           SCK

                           SDO                   bit 7       bit 6   bit 5        bit 4      bit 3       bit 2       bit 1       bit 0       next                  CKP = 1
                                        tx_buf
              input sample clock         write


                                       TXFIFO                                                                 Open RXFIFO                        RXFIFO Occupancy increments
                                   determined                                                                        latch                       TXFIFO Occupancy decrements
                                                                                                                                                 SPIxRIF and SPIxTIF interrupts
                                                                                                                                                 trigger


--- p579 ---
        Figure 35-9. Clocking Detail - Host Mode, CKE = 0, SMP = 1

                                                                                                                                                                                                                                     Rev. 10-000277A
                                                                                                                                                                                                                                            11/6/2018

                                                                                                     MST = 1, CKE = 0, SMP = 1

                                          SCK                            A       I       A       I       A       I       A       I       A           I       A       I       A   I     A       I

                                         SDO previous bit 0              bit 7           bit 6           bit 5           bit 4           bit 3               bit 2           bit 1     bit 0                      CKP = 0

                           input sample clock


                                          SCK                            A       I       A       I       A       I       A       I       A           I       A       I       A   I     A       I

                                         SDO previous bit 0              bit 7           bit 6           bit 5           bit 4           bit 3               bit 2           bit 1     bit 0                      CKP = 1

                           input sample clock


                                        TXFIFO determined                                                                                Open RXFIFO latch                                         RXFIFO Occupancy increments,
                                                                                                                                                                                                   TXFIFO Occupancy decrements,
                                                                                                                                                                                                   SPIxRIF and SPIxTIF interrupts
                                                                                                                                                                                                   trigger


        Figure 35-10. Clocking Detail - Host Mode, CKE = 1, SMP = 0


                                                                                                                                                                                                                  Rev. 10-000278A
                                                                                                                                                                                                                         11/6/2018

                                                                                     MST = 1, CKE = 1, SMP = 0

                             SCK                    I      A I       A       I       A       I       A       I       A       I       A           I       A       I       A

                             SDO                        bit 7    bit 6       bit 5           bit 4           bit 3           bit 2           bit 1               bit 0                                  CKP = 0

                input sample clock         tx_buf
                                            write


                             SCK                    I     A      I   A       I       A       I       A       I       A       I       A       I           A       I       A

                             SDO                    bit 7        bit 6       bit 5           bit 4           bit 3           bit 2           bit 1               bit 0                                  CKP = 1

                input sample clock         tx_buf
                                            write


                                     TXFIFO to SDO                                                                   Open RXFIFO latch                                               RXFIFO Occupancy increments,
                                                                                                                                                                                     TXFIFO Occupancy decrements,
                                                                                                                                                                                     SPIxRIF and SPIxTIF interrupts
                                                                                                                                                                                     trigger


35.3.6.3 SCK Start-Up Delay
        When starting an SPI data exchange, the host device asserts the SS output by either setting the
        SSET bit or loading the TCNT value, which then triggers the module to send data by writing SPIxTXB.
        These data triggers are synchronized to the clock selected by the SPIxCLK register before the first
        SCK pulse appears, usually requiring one or two clock periods of the selected SPI source clock.
        The SPI module includes additional synchronization delays on SCK generation specifically designed
        to ensure that the Client Select output timing is correct, without requiring precision software timing
        loops. By default, this synchronization delay is ½ baud period.
        When the value of the SPIxBAUD register is a small number (indicating higher SCK frequencies), the
        code execution delay between asserting SS and writing SPIxTXB is relatively long compared to the
        added synchronization delay before the first SCK edge. With larger values of SPIxBAUD (indicating
        lower SCK frequencies), the code execution delay is much smaller relative to the synchronization
        delay. Therefore, the first SCK edge after SS is asserted will be closer to the synchronization delay.


--- p580 ---
        Setting the FST bit removes the synchronization delay, allowing systems with low SPIxBAUD values
        (and thus, long synchronization delays) to forgo this extra delay, in which case the time between the
        SS assertion and the first SCK edge depends entirely on the code execution delay.

35.4    Client Mode
35.4.1 Client Mode Transmit Options
        The SDO output of the SPI module in Client mode is controlled by the following:
        • TXR bit
        •     TRIS bit associated with the SDO pin
        •     Client Select input
        •     Current state of the transmit FIFO
        This control is summarized in the following table where TRISxn refers to the bit in the TRIS register
        corresponding to the pin that SDO has been assigned with PPS, TXR is the Transmit Data Required
        Control bit, SS is the state of the Client Select input, and TXBE is the transmit FIFO Buffer Empty bit.

        Table 35-2. Client Mode Transmit
              TRISxn(1)         TXR            SS           TXBE       SDO State
                  0               0          FALSE            0        Drives state determined by LATxn(2)
                  0               0          FALSE            1        Drives state determined by LATxn(2)
                                                                       Outputs the oldest byte in the transmit
                  0               0          TRUE             0
                                                                       FIFO Does not remove data from the transmit FIFO
                  0               0          TRUE             1        Outputs the most recently received byte
                  0               1          FALSE            0        Drives state determined by LATxn(2)
                  0               1          FALSE            1        Drives state determined by LATxn(2)
                                                                       Outputs the oldest byte in the transmit FIFO
                  0               1          TRUE             0        Removes transmitted byte from the transmit FIFO
                                                                       Decrements occupancy of transmit FIFO
                                                                       Outputs the most recently received byte
                  0               1          TRUE             1
                                                                       Sets the TXUIF bit
                  1               0          FALSE            0        Tri-stated
                  1               0          FALSE            1        Tri-stated
                  1               0          TRUE             0        Tri-stated
                  1               0          TRUE             1        Tri-stated
                  1               1          FALSE            0        Tri-stated
                  1               1          FALSE            1        Tri-stated
                                                                       Outputs the oldest byte in the transmit FIFO
                  1               1          TRUE             0        Removes transmitted byte from the transmit FIFO
                                                                       Decrements the FIFO occupancy
                                                                       Outputs the most recently received byte
                  1               1          TRUE             1
                                                                       Sets the TXUIF bit
         Notes:
         1.    TRISxn is the bit in the TRISx register corresponding to the pin to which SDO has been assigned with PPS.
         2.    LATxn is the bit in the LATx register corresponding to the pin to which SDO has been assigned with PPS.


35.4.1.1 SDO Drive/Tri-State
        The TRIS bit associated with the SDO pin controls whether the SDO pin will tri-state. When this TRIS
        bit is cleared, the pin will always be driving to a level, even when the SPI module is inactive. When
        the SPI module is inactive (either due to the host not clocking the SCK line or the SS being false), the
        SDO pin will be driven to the value of the LAT bit associated with the SDO pin. When the SPI module
        is active, its output is determined by both TXR and whether there is data in the transmit FIFO.


--- p581 ---
       When the TRIS bit associated with the SDO pin is set, the pin will only have an output level driven to
       it when TXR = 1 and the Client Select input is true. In all other cases, the pin will be tri-stated.

       Table 35-3. Client Mode Transmit
             TRISxn(1)          TXR             SS             TXBE       SDO State
                 0                0           FALSE              0        Output level determined by LATxn(2)
                 0                0           FALSE              1        Output level determined by LATxn(2)
                                                                          Outputs the oldest byte in the TXFIFO.
                 0                0            TRUE              0
                                                                          Does not remove data from the TXFIFO.
                 0                0            TRUE              1        Outputs the most recently received byte
                 0                1           FALSE              0        Output level determined by LATxn(2)
                 0                1           FALSE              1        Output level determined by LATxn(2)
                                                                          Outputs the oldest byte in the TXFIFO.
                 0                1            TRUE              0        Removes transmitted byte from the TXFIFO.
                                                                          Decrements occupancy of TXFIFO.
                                                                          Outputs the most recently received byte.
                 0                1            TRUE              1
                                                                          Sets the TXUIF bit.
                 1                0           FALSE              0        Tri-stated
                 1                0           FALSE              1        Tri-stated
                 1                0            TRUE              0        Tri-stated
                 1                0            TRUE              1        Tri-stated
                 1                1           FALSE              0        Tri-stated
                 1                1           FALSE              1        Tri-stated
                                                                          Outputs the oldest byte in the TXFIFO.
                 1                1            TRUE              0        Removes transmitted byte from the TXFIFO.
                                                                          Decrements occupancy of TXFIFO.
                                                                          Outputs the most recently received byte.
                 1                1            TRUE              1
                                                                          Sets the TXUIF bit.
        Notes:
        1.   TRISxn is the bit in the TRISx register corresponding to the pin that SDO has been assigned with PPS.
        2.   LATxn is the bit in the LATx register corresponding to the pin that SDO has been assigned with PPS.


35.4.1.2 SDO Output Data
       The TXR bit controls the nature of the data that is transmitted in Client mode. When TXR is set,
       transmitted data is taken from the transmit FIFO. If the FIFO is empty, the most recently received
       data will be transmitted and the TXUIF flag will be set to indicate that a transmit FIFO underflow has
       occurred.
       When TXR is cleared, the data will be taken from the transmit FIFO, and the FIFO occupancy will not
       decrease. If the transmit FIFO is empty, the most recently received data will be transmitted, and the
       TXUIF bit will not be set. However, if the TRIS bit associated with the SDO pin is set, clearing the TXR
       bit will cause the SPI module to not output any data to the SDO pin.

35.4.2 Client Mode Receive Options
       The RXR bit controls the nature of receptions in Client mode. When RXR is set, the SDI input data
       will be stored in the receive FIFO if it is not full. If the receive FIFO is full, the RXOIF bit will be set
       to indicate a receive FIFO overflow error and the data is discarded. When RXR is cleared, all received
       data will be ignored and not stored in the receive FIFO (although it may still be used for transmission
       if the transmit FIFO is empty).
       The following figure presents a typical Client mode communication, showing a case where the host
       writes two and then three bytes, showing interrupts as well as the behavior of the transfer counter
       in Client mode (see the Transfer Counter in Client Mode section for more details on the transfer
       counter in Client mode as well as the SPI Interrupts section for more information on interrupts).


--- p582 ---
        Figure 35-11. SPI Client Mode Operation – Interrupt-Driven, Host Writes 2+3 Bytes
                                                                                                                                                    Rev. 10-000285A
                                                                                                                                                           11/8/2018


                     SS_in

                   SCK_in                                                   Note 1

                  SDO_out      Output data

                    SOSIF                    Note 2

                    EOSIF


           Transfer Counter                   0                -1          -2                 3               2                1             0


           Software Write to                                                         Note 3
                SPIxTCNTL
                    TCZIF
            Software Write
                   to TXR
                      TXR
          Software Write to
                     RXR
                      RXR

          Receiver process

                  SPIxRIF

                 Software
                Read from
                 SPIxRXB

          Notes: 1. This delay is exaggerated for illustration, and can be as short as1/2 bit period.
                 2. If the device is sleeping, SOSIF will wake it up for interrupt service.
                 3. Setting SPIxTCNTL is optional in this example, otherwise it will count -3, -4, -5, and TCZIF will not occur.


35.4.3 Client Mode Client Select
        In Client mode, an external Client Select signal can be used to synchronize communication with the
        host device. The Client Select line is held in its Inactive state (high by default) until the host device is
        ready to communicate. When the Client Select transitions to its Active state, the client knows that a
        new transmission is starting.
        When the Client Select goes false at the end of the transmission, the receive function of the selected
        SPI client device returns to the Inactive state. The client is then ready to receive a new transmission
        when the Client Select goes true again.
        The Client Select signal is received on the SS input pin. This pin is selected with the SPIxSSPPS
        register (refer to the “PPS Inputs” section). When the input on this pin is true, transmission and
        reception are enabled, and the SDO pin is driven. When the input on this pin is false, the SDO pin is
        either tri-stated (if the TRIS bit associated with the SDO pin is set) or driven to the value of the LAT
        bit associated with the SDO pin (if the TRIS bit associated with the SDO pin is cleared). The SCK input
        is ignored when the SS input is false.
        If the SS input goes false while a data transfer is still in progress, it is considered a Client Select fault.
        The SSFLT bit indicates whether such an event has occurred. The transfer counter value determines
        the number of bits in a valid data transfer (see the Transfer Counter section for more details).
        The Client Select polarity is controlled by the SSP bit. When SSP is set (its default state), the Client
        Select input is active-low, and when it is cleared, the Client Select input is active-high.
        The Client Select for the SPI module is controlled by the SSET bit. When SSET is cleared (its default
        state), the Client Select will act as described above. When the bit is set, the SPI module will behave as
        if the SS input is always in its Active state.


--- p583 ---
                    Important:
                    When SSET is set, the effective SS_in signal is always active. Hence, the SSFLT bit may be
                    disregarded.


35.4.4 Client Mode Clock Configuration
       In Client mode, SCK is an input and must be configured to the same polarity and clock edge as the
       host device. As in Host mode, the polarity of the clock input is controlled by the CKP bit and the clock
       edge used for transmitting data is controlled by the CKE bit.

35.4.5 Daisy-Chain Configuration
       The SPI bus can be connected in a daisy-chain configuration, where the first client output is
       connected to the second client input, the second client output is connected to the third client input,
       and so on. The final client output is connected to the host input. Each client sends out, during a
       second group of clock pulses, an exact copy of what was received during the first group of clock
       pulses. The whole chain acts as one large communication shift register. The daisy-chain feature only
       requires a single Client Select line from the host device connected to all client devices (alternately,
       the client devices can be configured to ignore the Client Select line by setting the SSET bit).
       In a typical daisy-chain configuration, the SCK signal from the host is connected to each of the client
       device SCK inputs. However, the SCK input and output are separate signals selected by the PPS
       control. When the PPS selection is made to configure the SCK input and SCK output on separate
       pins, the SCK output will follow the SCK input, allowing for SCK signals to be daisy-chained like the
       SDO/SDI signals.
       The following two figures show block diagrams of a typical daisy-chain connection and a daisy-chain
       connection with daisy-chained SPI clocks, respectively.

       Figure 35-12. Traditional SPI Daisy-Chain Connection

                                                                                               Rev. 10-000082B
                                                                                                      11/8/2018


                                                  SCK                            SCK
                                 SPI Host        SDOx                            SDIx SPI Client
                                                  SDIx                           SDOx    #1
                                       SSxOUT/GPIO                               SSxIN


                                                                                  SCK
                                                                                 SDIx SPI Client
                                                                                 SDOx    #2
                                                                                 SSxIN


                                                                                  SCK
                                                                                 SDIx SPI Client
                                                                                 SDOx    #3
                                                                                 SSxIN


--- p584 ---
        Figure 35-13. SPI Daisy-Chain Connection with Chained SCK

                                                                                                   Rev. 10-000082C
                                                                                                          11/8/2018


                                                   SCK                            SCK(in)
                                  SPI Host        SDOx                            SDIx       SPI Client
                                                   SDIx                                         #1
                                                                                  SSxIN
                                       SSxOUT/GPIO
                                                                                  SCK(out)      SDOx


                                                                                  SCK(in)        SDIx

                                                                                            SPI Client
                                                                                  SSxIN        #2

                                                                                  SCK(out)      SDOx


                                                                                  SCK(in)        SDIx

                                                                                  SSxIN SPI Client
                                                                                           #3

                                                                                                SDOx


35.5    SPI Operation in Sleep Mode
        The SPI Host mode will operate in Sleep, provided that the clock source selected by SPIxCLK is active
        in Sleep mode. FIFOs will operate as they do when the part is awake. When TXR = 1, the transmit
        FIFO will need to contain data for transfers to take place in Sleep. All interrupts will still set the
        interrupt flags in Sleep, but only enabled interrupts will wake the device from Sleep.
        The SPI Client mode will operate in Sleep because the clock is provided by an external host device.
        FIFOs will still operate, interrupts will set interrupt flags, and enabled interrupts will wake the device
        from Sleep.

35.6    SPI Interrupts
        There are three top level SPI interrupts in the PIRx register:
        •   SPI Transmit (SPIxTXIF)
        •   SPI Receive (SPIxRXIF)
        •   SPI Module status (SPIxIF)
        The SPI Module status interrupts are enabled at the module level in the SPIxINTE register. Only
        enabled status interrupts will cause the single top level SPIxIF flag to be set.

35.6.1 SPI Receive Interrupt
        The SPI receive interrupt is set when the receive FIFO contains data and is cleared when the receive
        FIFO is empty. The interrupt flag, SPIxRXIF, is located in one of the PIR registers. The interrupt
        enable, SPIxRXIE, is located in the corresponding PIE register. The SPIxRXIF interrupt flag is read-
        only.

35.6.2 SPI Transmit Interrupt
        The SPI Transmit interrupt is set when the transmit FIFO is not full and can accept a character and is
        cleared when the transmit FIFO is full and cannot accept a character. The interrupt flag, SPIxTXIF, is
        located in one of the PIR registers. The interrupt enable, SPIxTXIE, is located in the corresponding PIE
        register. The SPIxTXIF interrupt flag is read-only.


--- p585 ---
35.6.3 SPI Status Interrupts
        The SPIxIF flag is located in one of the PIR registers. This flag is set when any of the individual status
        flags in SPIxINTF and their respective SPIxINTE bits are set. For any specific interrupt flag to interrupt
        normal program flow, both the SPIxIE bit in the PIE register corresponding to the PIR register and the
        specific bit in SPIxINTE associated with that interrupt must be set.
        The Status Interrupts include the following:
        •     Shift Register Empty (SRMTIF)
        •     Transfer Counter is Zero (TCZIF)
        •     Start of Client Select (SOSIF)
        •     End of Client Select (EOSIF)
        •     Receiver Overflow (RXOIF)
        •     Transmitter Underflow (TXUIF)
35.6.3.1 Shift Register Empty Interrupt
        The Shift Register Empty Interrupt Flag and Shift Register Empty Interrupt Enable are the SRMTIF
        and SRMTIE bits, respectively. This interrupt is only available in Host mode and triggers when a data
        transfer completes and conditions are not present to start a new transfer, as dictated by the TXR and
        RXR bits (see Table 35-1 for conditions for starting a new Host mode data transfer with different TXR/
        RXR settings). This interrupt will be triggered at the end of the last full bit period after SCK has been
        low for one ½-baud period. See the figure below for more details of the timing of this interrupt as
        well as other interrupts. This bit will not clear itself when the conditions for starting a new transfer
        occur and must be cleared in software.

        Figure 35-14. Transfer And Client Select Interrupt Timing

                                                                                                                                                                Rev. 10-000286A
                                                                                                                                                                       11/8/2018


                     SS_in

                      SCK


            SDO_bit_number           7   6   5    4   3    2   1      0       7     6   5   4   3   2   1    0   7   6    5   4   3    2     1       0


                   SRMTIF


                    SOSIF
                   Note 3


                    TCZIF


                    EOSIF                                                                                                                        Note 3


                  Notes:     1. SRMTIF available only in Host mode.
                             2. Clearing of interrupt flags is shown for illustration; actual interrupt flags must be cleared in software.
                             3. SOSIF and EOSIF are set according to SS_in, even in Host mode.


35.6.3.2 Transfer Counter Is Zero Interrupt
        The Transfer Counter Is Zero Interrupt Flag and Transfer Counter Is Zero Interrupt Enable are the
        TCZIF and TCZIE bits, respectively. This interrupt will trigger when the transfer counter (defined by
        BMODE, SPIxTCNT and SPIxTWIDTH) decrements from one to zero. See Figure 35-14 for more details
        on the timing of this interrupt as well as other interrupts. This bit must be cleared in software.


--- p586 ---
                      Important:
                      The TCZIF flag only indicates that the transfer counter has decremented from one to zero
                      and may not indicate that the entire data transfer process is complete. Either poll the
                      BUSY bit and wait for it to be cleared or use the Shift Register Empty Interrupt (SRMTIF) to
                      determine when a data transfer is fully complete.


35.6.3.3 Start of Client Select and End of Client Select Interrupts
         The Start of Client Select Interrupt Flag and Start of Client Select Interrupt Enable are the SOSIF and
         SOSIE bits, respectively. The End of Client Select Interrupt Flag and End of Client Select Interrupt
         Enable are the EOSIF and EOSIE bits, respectively. These interrupts trigger at the leading and trailing
         edges of the Client Select input.
         The interrupts are active in both Host and Client mode and will trigger on transitions of the Client
         Select input, regardless of which mode the SPI is in. In Host mode, the PPS controls will be used to
         assign the Client Select input to the same pin as the Client Select output, allowing these interrupts to
         trigger on changes to the Client Select output.
         In Client mode, changing the SSET bit can trigger these interrupts, as it changes the effective input
         value of Client Select.
         Both SOSIF and EOSIF must be cleared in software.
35.6.3.4 Receiver Overflow and Transmitter Underflow Interrupts
         The receiver overflow interrupt triggers if data is received when the receive FIFO is already full and
         RXR = 1. In this case, the data will be discarded and the RXOIF bit will be set. The Receiver Overflow
         Interrupt Enable bit is RXOIE.
         The Transmitter Underflow Interrupt flag triggers if a data transfer begins when the transmit FIFO is
         empty and TXR = 1. In this case, the most recently received data will be transmitted and the TXUIF bit
         will be set. The Transmitter Underflow Interrupt Enable bit is TXUIE.
         Both these interrupts will only occur in Client mode, as Host mode will not allow the receive FIFO to
         overflow or the transmit FIFO to underflow.

35.7     Register Definitions: Serial Peripheral Interface
         Long bit name prefixes for the SPI peripherals are shown in the table below where “x” refers to
         the SPI instance number. Refer to the “Long Bit Names” section in the “Register and Bit Naming
         Conventions” chapter for more information.

         Table 35-4. SPI Long Bit Name Prefixes
                           Peripheral                                              Bit Name Prefix
                              SPI1                                                         SPI1
                              SPI2                                                         SPI2


--- p587 ---
35.7.1 SPIxCON0

            Name:       SPIxCON0
            Address:    0x084,0x091

            SPI Control Register 0

      Bit        7              6               5              4                  3           2              1             0
                EN                                                                          LSBF            MST          BMODE
  Access        R/W                                                                         R/W             R/W           R/W
   Reset         0                                                                            0              0             0

Bit 7 – EN SPI Enable
            Value      Description
            1          SPI is enabled
            0          SPI is disabled

Bit 2 – LSBF LSb-First Data Exchange Select(1)
            Value      Description
            1          Data is exchanged LSb first
            0          Data is exchanged MSb first (traditional SPI operation)

Bit 1 – MST SPI Host Operating Mode Select(1)
            Value      Description
            1          SPI module operates as the bus host
            0          SPI module operates as a bus client

Bit 0 – BMODE Bit-Length Mode Select(1)
            Value      Description
            1          SPIxTWIDTH setting applies to every byte: total bits sent is SPIxTWIDTH*SPIxTCNT, end-of-packet occurs when
                       SPIxTCNT = 0
            0          SPIxTWIDTH setting applies only to the last byte exchanged; total bits sent is SPIxTWIDTH + (SPIxTCNT*8)

            Note:
            1. Do not change this bit when EN = 1.


--- p588 ---
35.7.2 SPIxCON1

            Name:       SPIxCON1
            Address:    0x085,0x092

            SPI Control Register 1

      Bit        7               6              5                4                3             2              1               0
                SMP             CKE            CKP              FST                            SSP            SDIP           SDOP
  Access        R/W             R/W            R/W              R/W                            R/W            R/W             R/W
   Reset         0               0              0                0                              1              0               0

Bit 7 – SMP SPI Input Sample Phase Control
            Value      Mode                       Description
            1          Client                     Reserved
            1          Host                       SDI input is sampled at the end of data output time
            0          Client or Host             SDI input is sampled in the middle of data output time

Bit 6 – CKE Clock Edge Select
            Value      Description
            1          Output data changes on transition from Active to Idle clock state
            0          Output data changes on transition from Idle to Active clock state

Bit 5 – CKP Clock Polarity Select
            Value      Description
            1          Idle state for SCK is high level
            0          Idle state for SCK is low level

Bit 4 – FST Fast Start Enable
            Value      Mode           Description
            x          Client         This bit is ignored
            1          Host           Delay to first SCK may be less than ½ baud period
            0          Host           Delay to first SCK will be at least ½ baud period

Bit 2 – SSP Client Select Input/Output Polarity Control
            Value      Description
            1          SS is active-low
            0          SS is active-high

Bit 1 – SDIP SPI Input Polarity Control
            Value      Description
            1          SDI input is active-low
            0          SDI input is active-high

Bit 0 – SDOP SPI Output Polarity Control
            Value      Description
            1          SDO output is active-low
            0          SDO output is active-high


--- p589 ---
35.7.3 SPIxCON2

            Name:       SPIxCON2
            Address:    0x086,0x093
            SPI Control Register 2(3)

      Bit        7             6                5               4                  3           2               1               0
                BUSY         SSFLT                                                            SSET            TXR             RXR
  Access         R             R                                                              R/W             R/W             R/W
   Reset         0             0                                                               0               0               0

Bit 7 – BUSY SPI Module Busy Status(1)
            Value      Description
            1          Data exchange is busy
            0          Data exchange is not taking place

Bit 6 – SSFLT SS_in Fault Status
            Value      Condition   Description
            x          SSET = 1    This bit is unchanged
            1           SSET = 0    SS_in ended the transaction unexpectedly, and the data byte being received was lost
            0           SSET = 0    SS_in ended normally


Bit 2 – SSET Client Select Enable
            Value      Mode Description
            1          Host SS_out is driven to the Active state continuously
            0          Host SS_out is driven to the Active state while the transmit counter is not zero
            1          Client SS_in is ignored and data is clocked on all SCK_in (as though SS = TRUE at all times)
            0          Client SS_in enables/disables data input and tri-states SDO if the TRIS bit associated with the SDO pin is set
                              (see the Client Mode Transmit table for details)

Bit 1 – TXR Transmit Data-Required Control(2)
            Value      Description
            1          TxFIFO data is required for a transfer
            0          TxFIFO data is not required for a transfer

Bit 0 – RXR Receive FIFO Space-Required Control(2)
            Value      Description
            1          Data transfers are suspended when RxFIFO is full
            0          Received data is not stored in the FIFO

            Notes:
            1. The BUSY bit is subject to synchronization delay of up to two instruction cycles. The user must
               wait after loading the transmit buffer (the SPIxTXB register) before using it to determine the
               status of the SPI module.
            2. See the Host Mode TXR/RXR Settings table as well as the Host Mode and Client Mode sections for
               more details pertaining to TXR and RXR function.
            3. This register will not be written to while a transfer is in progress (the BUSY bit is set).


--- p590 ---
35.7.4 SPIxCLK

            Name:        SPIxCLK
            Address:     0x08C,0x099

            SPI Clock Selection Register

      Bit         7             6              5              4                   3            2         1                       0
                                                                                             CLKSEL[3:0]
  Access                                                                         R/W      R/W          R/W                     R/W
   Reset                                                                          0        0             0                      0

Bits 3:0 – CLKSEL[3:0] SPI Clock Source Selection

            Table 35-5. SPI CLK Source Selections
                                       CLK                                                           Selection
                                    1111 - 1101                                                 Reserved
                                        1100                                                    CLC4_OUT
                                        1011                                                    CLC3_OUT
                                        1010                                                    CLC2_OUT
                                        1001                                                    CLC1_OUT
                                        1000                                                   SMT1_OUT
                                        0111                                              TMR4_Postscaler_OUT
                                        0110                                              TMR2_Postscaler_OUT
                                        0101                                                   TMR0_OUT
                                        0100                                             Clock Reference Output
                                        0011                                                     EXTOSC
                                        0010                                               MFINTOSC (500 kHz)
                                        0001                                                    HFINTOSC
                                        0000                                               FOSC (System Clock)


--- p591 ---
35.7.5 SPIxBAUD

            Name:        SPIxBAUD
            Address:     0x089,0x096

            SPI Baud Rate Register

      Bit           7           6         5              4          3                     2                 1               0
                                                          BAUD[7:0]
  Access        R/W           R/W        R/W           R/W         R/W               R/W                  R/W             R/W
   Reset         0             0          0             0           0                 0                    0               0

Bits 7:0 – BAUD[7:0] Baud Clock Prescaler Select
            Value       Description
            n
                        SCK high or low time: TSC = SPI Clock Period*(n+1)
                        SCK toggle frequency: FSCK = FBAUD = SPI Clock Frequency/(2*(n+1))


--- p592 ---
35.7.6 SPIxTCNT

            Name:         SPIxTCNT
            Address:      0x082,0x08F

            SPI Transfer Counter Register

      Bit           15         14           13               12                 11       10                 9                 8
                                                                                                        TCNTH[2:0]
  Access                                                                                 R/W               R/W              R/W
   Reset                                                                                  0                 0                0

      Bit           7          6             5               4            3                 2                 1               0
                                                               TCNTL[7:0]
  Access        R/W           R/W           R/W             R/W         R/W              R/W                R/W             R/W
   Reset         0             0             0               0            0               0                  0               0

Bits 10:8 – TCNTH[2:0] SPI Transfer Counter Most Significant Byte
            Value        Condition                Description
            n            BMODE = 0                Bits 13-11 of the transfer bit count
            n            BMODE = 1                Bits 10-8 of the transfer byte count


Bits 7:0 – TCNTL[7:0] SPI Transfer Counter Least Significant Byte
            Value        Condition                Description
            n            BMODE = 0                Bits 10-3 of the transfer bit count
            n            BMODE = 1                 Bits 7-0 of the transfer byte count


--- p593 ---
35.7.7 SPIxTWIDTH

            Name:        SPIxTWIDTH
            Address:     0x088,0x095

            SPI Transfer Width Register

      Bit           7         6               5                4                  3           2              1                  0
                                                                                                         TWIDTH[2:0]
  Access                                                                                    R/W             R/W               R/W
   Reset                                                                                     0               0                 0

Bits 2:0 – TWIDTH[2:0] SPI Transfer Count Byte Width or three LSbs of the Transfer Bit Count
            Value       Condition   Description
            n           BMODE = 0   Bits 2-0 of the transfer bit count
            n           BMODE = 1   Number of bits in each transfer byte count. Bits = n (when n > 0) or 8 (when n = 0).


--- p594 ---
35.7.8 SPIxSTATUS

            Name:        SPIxSTATUS
            Address:     0x087,0x094

            SPI Status Register

      Bit         7              6               5              4                 3           2                1              0
                TXWE                           TXBE                             RXRE         CLB                             RXBF
  Access       R/C/HS                            R                             R/C/HS         S                               R
   Reset          0                              1                                0           0                               0

Bit 7 – TXWE Transmit Buffer Write Error
            Value       Description
            1           SPIxTXB was written while TxFIFO was full
            0           No error has occurred

Bit 5 – TXBE Transmit Buffer Empty
            Value       Description
            1           Transmit buffer TxFIFO is empty
            0           Transmit buffer is not empty

Bit 3 – RXRE Receive Buffer Read Error
            Value       Description
            1           SPIxRXB was read while RxFIFO was empty
            0           No error has occurred

Bit 2 – CLB Clear Buffer Control
            Value       Description
            1           Reset the receive and transmit buffers, making both buffers empty
            0           Take no action

Bit 0 – RXBF Receive Buffer Full
            Value       Description
            1           Receive buffer is full
            0           Receive buffer is not full


--- p595 ---
35.7.9 SPIxRXB

            Name:        SPIxRXB
            Address:     0x080,0x08D

            SPI Receive Buffer

      Bit           7            6                5                4                  3            2                 1               0
                                                                         RXB[7:0]
  Access            R            R                R                R                  R            R                 R               R
   Reset            x            x                x                x                  x            x                 x               x

Bits 7:0 – RXB[7:0] Receive Buffer
            Value       Condition                     Description
            n           Receive buffer is not         Contains the top-most byte of the RXFIFO. Reading this register will remove the
                        empty                         RXFIFO top-most byte and decrease the occupancy of the RXFIFO by 1.
            0           Receive buffer is empty       Reading this register will return ‘0’, leave the occupancy unchanged, and set the
                                                      RXRE Status bit


--- p596 ---
35.7.10 SPIxTXB

            Name:        SPIxTXB
            Address:     0x081,0x08E

            SPI Transmit Buffer

      Bit           7            6               5               4                  3            2                 1               0
                                                                       TXB[7:0]
  Access            W           W                W               W                  W            W                 W               W
   Reset            x           x                x               x                  x            x                 x               x

Bits 7:0 – TXB[7:0] Transmit Buffer
            Value       Condition                  Description
            n           Transmit buffer is not full Writing to this register adds the data to the top of the TXFIFO and increases the
                                                    occupancy of the TXFIFO by 1.
            x           Transmit buffer is full     Writing to this register does not affect the data in the TXFIFO or the occupancy
                                                    count. The TXWE Status bit will be set.


--- p597 ---
35.7.11 SPIxINTE

            Name:       SPIxINTE
            Address:    0x08B,0x098

            SPI Interrupt Enable Register

      Bit       7              6              5                 4                3            2                1                0
              SRMTIE         TCZIE          SOSIE             EOSIE                         RXOIE            TXUIE
  Access       R/W            R/W            R/W               R/W                           R/W              R/W
   Reset        0              0              0                 0                             0                0

Bit 7 – SRMTIE Shift Register Empty Interrupt Enable
            Value      Description
            1          Interrupt is enabled
            0          Interrupt is not enabled

Bit 6 – TCZIE Transfer Counter is Zero Interrupt Enable
            Value      Description
            1          Interrupt is enabled
            0          Interrupt is not enabled

Bit 5 – SOSIE Start of Client Select Interrupt Enable
            Value      Description
            1          Interrupt is enabled
            0          Interrupt is not enabled

Bit 4 – EOSIE End of Client Select Interrupt Enable
            Value      Description
            1          Interrupt is enabled
            0          Interrupt is not enabled

Bit 2 – RXOIE Receiver Overflow Interrupt Enable
            Value      Description
            1          Interrupt is enabled
            0          Interrupt is not enabled

Bit 1 – TXUIE Transmitter Underflow Interrupt Enable
            Value      Description
            1          Interrupt is enabled
            0          Interrupt is not enabled


--- p598 ---
35.7.12 SPIxINTF

            Name:         SPIxINTF
            Address:      0x08A,0x097

            SPI Interrupt Flag Register

      Bit          7             6               5                  4              3             2               1               0
                SRMTIF         TCZIF           SOSIF              EOSIF                        RXOIF           TXUIF
  Access        R/W/HS        R/W/HS          R/W/HS             R/W/HS                       R/W/HS          R/W/HS
   Reset           0             0               0                  0                            0               0

Bit 7 – SRMTIF Shift Register Empty Interrupt Flag
            Value        Mode      Description
            x            Client    This bit is ignored
            1            Host      The data transfer is complete
            0            Host      Either no data transfers have occurred or a data transfer is in progress

Bit 6 – TCZIF Transfer Counter is Zero Interrupt Flag
            Value        Description
            1            The transfer counter has decremented to zero
            0            No interrupt pending

Bit 5 – SOSIF Start of Client Select Interrupt Flag
            Value        Description
            1            SS_in transitioned from false to true
            0            No interrupt pending

Bit 4 – EOSIF End of Client Select Interrupt Flag
            Value        Description
            1            SS_in transitioned from true to false
            0            No interrupt pending

Bit 2 – RXOIF Receiver Overflow Interrupt Flag
            Value        Description
            1            Data transfer completed when RXBF = 1 (edge-triggered) and RXR = 1
            0            No interrupt pending

Bit 1 – TXUIF Transmitter Underflow Interrupt Flag
            Value        Description
            1            Client Data transfer started when TXBE = 1 and TXR = 1
            0            No interrupt pending


--- p599 ---
35.8      Register Summary - SPI Control
Address      Name       Bit Pos.     7           6           5              4                3          2           1            0
 0x00
  ...       Reserved
 0x7F
 0x80       SPI1RXB      7:0                                                     RXB[7:0]
 0x81       SPI1TXB      7:0                                                     TXB[7:0]
                         7:0                                                    TCNTL[7:0]
 0x82       SPI1TCNT
                         15:8                                                                                   TCNTH[2:0]
 0x84       SPI1CON0     7:0         EN                                                               LSBF         MST        BMODE
 0x85       SPI1CON1     7:0        SMP         CKE         CKP            FST                         SSP         SDIP        SDOP
 0x86       SPI1CON2     7:0       BUSY        SSFLT                                                  SSET         TXR          RXR
 0x87      SPI1STATUS    7:0       TXWE                    TXBE                          RXRE         CLB                      RXBF
 0x88      SPI1TWIDTH    7:0                                                                                   TWIDTH[2:0]
 0x89       SPI1BAUD     7:0                                               BAUD[7:0]
 0x8A        SPI1INTF    7:0       SRMTIF      TCZIF       SOSIF       EOSIF                         RXOIF       TXUIF
 0x8B        SPI1INTE    7:0       SRMTIE      TCZIE       SOSIE       EOSIE                         RXOIE       TXUIE
 0x8C        SPI1CLK     7:0                                                                            CLKSEL[3:0]
 0x8D        SPI2RXB     7:0                                                     RXB[7:0]
 0x8E        SPI2TXB     7:0                                                     TXB[7:0]
                         7:0                                                    TCNTL[7:0]
 0x8F       SPI2TCNT
                         15:8                                                                                   TCNTH[2:0]
 0x91       SPI2CON0     7:0         EN                                                               LSBF         MST        BMODE
 0x92       SPI2CON1     7:0        SMP         CKE         CKP            FST                         SSP         SDIP        SDOP
 0x93       SPI2CON2     7:0       BUSY        SSFLT                                                  SSET         TXR          RXR
 0x94      SPI2STATUS    7:0       TXWE                    TXBE                          RXRE         CLB                      RXBF
 0x95      SPI2TWIDTH    7:0                                                                                   TWIDTH[2:0]
 0x96       SPI2BAUD     7:0                                               BAUD[7:0]
 0x97        SPI2INTF    7:0       SRMTIF      TCZIF       SOSIF       EOSIF                         RXOIF       TXUIF
 0x98        SPI2INTE    7:0       SRMTIE      TCZIE       SOSIE       EOSIE                         RXOIE       TXUIE
 0x99        SPI2CLK     7:0                                                                            CLKSEL[3:0]


--- p600 ---
