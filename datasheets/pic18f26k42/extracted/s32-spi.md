                      PIC18(L)F26/27/45/46/47/55/56/57K42
32.0     SERIAL PERIPHERAL
         INTERFACE (SPI) MODULE

32.1     SPI Module Overview
The SPI (Serial Peripheral Interface) module is a
synchronous serial data communication bus that
operates in Full Duplex mode. Devices communicate in
a host/client environment where the host device
initiates the communication. A client device is
controlled through a Chip Select known as Client
Select. Example client devices include serial
EEPROMs, shift registers, display drivers, A/D
converters, or another PIC® device.
The SPI bus specifies four signal connections:
• Serial Clock (SCK)
• Serial Data Out (SDO)
• Serial Data IN (SDI)
• Client Select (SS)
The SPI interface supports the following modes and
features:
• Host mode
• Client mode
• Clock Polarity and Edge Select
• SDI, SDO, and SS Polarity Control
• Separate Transmit and Receive Enables
• Client Select Synchronization
• Daisy-chain connection of client devices
• Separate Transmit and Receive Buffers with
  2-byte FIFO and DMA capabilities
Figure 32-1 shows the block diagram of the SPI
module.


 2017-2021 Microchip Technology Inc.                  DS40001919G-page 513
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 32-1:                SPI MODULE SIMPLIFIED BLOCK DIAGRAM

                                                       Data bus                                                  Rev. 10-000076B
                                                                                                                        7/18/2018


                                              Read                                      Write

                                                       8                      8

                                                  Receive FIFO          Transmit FIFO
                                                    (2 deep)               (2 deep)

                                                       8                      8

      SDI           SPIxSDIPPS                    Receive Shift           Transmit
                                                                                                       RxyPPS                   SDO
                                                    Register             Serializer(1)
                          SDIP

                                                                                          SDOP


                                        1
                                                                  RXR        TXR
                                                 1
    SS(in)          SPIxSSPPS
                                                 0                                                         RxyPPS
                    SSP
                                                                                                                       SCK(out)

                                                                                                 CKP
                                               SSET                 SPI Control Module
                                                                   and Transfer Counter


                 See
               SPIxCLK
               Register                SCK Generator        1
                                                            0


                                                                         1
                                         SPIxBAUD
                                                                                    1
                                                           MST
                                                                                    0                  RxyPPS
                                                                                                                SS(out)
             CLKSEL<3:0>

                                                                                          SSP
   SCK(in)         SPIxSCKPPS
                                                                                   SSET

                  CKP

        Note 1:     If TXR=1 and the transmit FIFO is empty, the previous value of the
                    receive shift register will be sent to the transmit serializer.


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 514
                        PIC18(L)F26/27/45/46/47/55/56/57K42
The SPI transmit output (SDO_out) is available to the          • Host sends useful data and client sends useful
remappable PPS SDO pin and internally to the                     data
following peripherals:                                         • Host sends dummy data and client sends useful
• Configurable Logic Cell (CLC)                                  data
• Data Signal Modulator (DSM)                                  In this particular SPI module, dummy data may be sent
The SPI bus typically operates with a single host device       without software involvement, by clearing either the
and one or more client devices. When multiple client           RXR bit (for receiving dummy data) or the TXR bit (for
devices are used, an independent Client Select con-            sending dummy data) (see Table 32-1 as well as
nection is required from the host device to each client        Section 32.5 “Host mode” and Section 32.6 “Client
device.                                                        Mode” for further TXR/RXR setting details). This SPI
                                                               module can send transmissions of any number of bits,
The host selects only one client at a time. Most client        and can send information in segments of varying size
devices have tri-state outputs so their output signal          (from 1-8 bits in width). As such, transmissions may
appears disconnected from the bus when they are not            involve any number of clock cycles, depending on the
selected.                                                      amount of data to be transmitted.
Transmissions typically involve shift registers, eight bits    When there is no more data to be transmitted, the host
in size, one in the host and one in the client. With either    stops sending the clock signal and deselects the client.
the host or the client device, data is always shifted out
one bit at a time, with the Most Significant bit (MSb)         Every client device connected to the bus that has not
shifted out first. At the same time, a new bit is shifted      been selected through its client select line disregards
into the device. Unlike older Microchip devices, the SPI       the clock and transmission signals and does not
on the this device contains two separate registers for         transmit out any data of its own.
incoming and outgoing data. Both registers also have
2-byte FIFO buffers and allow for DMA bus connec-
tions.
Figure 32-2 shows a typical connection between two
devices configured as host and client devices.
Data is shifted out of the transmit FIFO on the
programmed clock edge and into the receive shift
register on the opposite edge of the clock.
The host device transmits information on its SDO
output pin which is connected to, and received by, the
client’s SDI input pin. The client device transmits
information on its SDO output pin, which is connected
to, and received by, the host’s SDI input pin.
The host device sends out the clock signal. Both the
host and the client devices may be configured for the
same clock polarity.
During each SPI clock cycle, a full-duplex data
transmission occurs. This means that while the host
device is sending out the MSb from its output register
(on its SDO pin) and the client device is reading this bit
and saving as the LSb of its input register, that the client
device is also sending out the MSb from its shift register
(on its SDO pin) and the host device is reading this bit
and saving it as the LSb of its input register.
After eight bits have been shifted out, the host and cli-
ent have exchanged register values and stored the
incoming data into the receiver FIFOs.
If there is more data to exchange, the registers are
loaded with new data and the process repeats itself.
Whether the data is meaningful or not (dummy data)
depends on the application software. This leads to
three scenarios for data transmission:
• Host sends useful data and client sends dummy
  data


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 515
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 32-2:           SPI HOST/CLIENT CONNECTION WITH FIFOs
                                                                                                              Rev. 10-000080C
                                                                                                                     7/18/2018


                      SPI +RVW MST=1                                                 SPI &OLHQW MST=0

                                                                                     Receive FIFO
                         Transmit FIFO                                                (SPIxRXB)
                           (SPIxTXB)          SDOx                        SDIx
                                                                                      Receive Shift
                                                                                        Register
                       LSb              MSb                                        LSb            MSb

                                   (Note 1)                                                    (Note 1)


                         Receive FIFO
                          (SPIxRXB)                                                  Transmit FIFO
                                              SDIx                        SDOx         (SPIxTXB)
                         Receive Shift
                           Register                     Serial clock
                                              SCKx                        SCKx
                       MSb              LSb                                        MSb                LSb
                                                        &OLHQW Select
                                         SSxOUT/                         SSxIN
                             Device 1     GPIO           (optional)                        Device 2

           Note 1: In some modes, if the Transmit FIFO is empty, the most recently
                received byte of data will be transmitted
                2: This diagram assumes that the LSBF bit is cleared (communications are
                MSb-first). If LSBF is set, the communications will be LSb-first.


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 516
                      PIC18(L)F26/27/45/46/47/55/56/57K42
32.2     SPI REGISTERS                                      and enable for the SPI Transmit Interrupt, as well as the
                                                            SPIxRXIF/SPIxRXIE bits, which are the interrupt flag
• SPI Interrupt Flag Register (SPIxINTF)                    and enable for the SPI Receive Interrupt.
• SPI Interrupt Enable Register (SPIxINTE)
• SPI Byte Count High and Low Registers
  (SPIxTCNTH/L)
• SPI Bit Count Register (SPIxTWIDTH)
• SPI Baud Rate Register (SPIxBAUD)
• SPI Control Register 0 (SPIxCON0)
• SPI Control Register 1 (SPIxCON1)
• SPI Control Register 2 (SPIxCON2)
• SPI FIFO Status Register (SPIxSTATUS)
• SPI Receiver Buffer Register (SPIxRXB)
• SPI Transmit Buffer Register (SPIxTXB)
• SPI Clock Select Register (SPIxCLK)
SPIxCON0, SPIxCON1, and SPIxCON2 are control
registers for the SPI module.
SPIxSTATUS contains several Status bits that indicate
the status of both the SPI module and the receive and
transmit FIFOs.
SPIxBAUD and SPIxCLK control the baud rate gener-
ator of the SPI module when in Host mode. The SPIx-
CLK selects the clock source that is used. The
SPIxBAUD configures the clock divider used on that
clock. More information on the baud rate generator is
available in Section 32.5.6 “Host Mode SPI Clock
Configuration”.”
SPIxTxB and SPIxRxB are the transmit and receive
buffer registers used to send and receive data on the
SPI bus. They both offer indirect access to shift
registers that are used for shifting the data in and out.
Both registers access the two-byte FIFOs, allowing for
multiple transmissions/receptions to be stored between
software transfers the data.
The SPIxTCNTH:L register pair either count or control
the number of bits or bytes in a data transfer. When
BMODE = 1, the SPIxTCNT value signifies bytes and
the SPIxTWIDTH value signifies the number of bits in a
byte. When BMODE = 0, the SPIxTCNT value is
concatenated with the SPIxTWIDTH register to signify
bits. In Host Receive-only mode (TXR = 0 and         RXR
= 1), the data transfer is initiated by writing SPIxTCNT
with the desired bit or byte value to transfer. In Host
Transmit mode (TXR = 1), the data transfer is initiated
by writing the SPIxTxB register, in which case the
SPIxTCNT is a down counter for the bits or bytes
transferred.
The SPIxINTF and SPIxINTE are the flags and
enables, respectively, for SPI-specific interrupts. They
are tied to the SPIxIF flag and SPIxIE enable in the PIR
and PIE registers, which is triggered when any interrupt
contained in the SPIxINTF/SPIxINTE registers is
triggered. The PIR/PIE registers also contain
SPIxTXIF/SPIxTXIE bits, which are the interrupt flag


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 517
                      PIC18(L)F26/27/45/46/47/55/56/57K42
32.3     SPI MODE OPERATION                               32.3.2      BUSY BIT
When initializing the SPI, several options need to be     While a data transfer is in progress, the SPI module
specified. This is done by programming the appropriate    sets the BUSY bit of SPIxCON2. This bit can be polled
control     bits    (SPIxCON0[2:0],      SPIxCON1[7:4],   by the user to determine the current status of the SPI
SPIxCON1[2:0], and SPIxCON2[2:0]). These control          module, and to know when a communication is
bits allow the following to be specified:                 complete. The following registers/bits may not be
                                                          written by software while the BUSY bit is set:
• Host mode (SCK is the clock output)
                                                          • SPIxTCNTH/L
• Client mode (SCK is the clock input)
                                                          • SPIxTWIDTH
• Clock Polarity (Idle state of SCK)
                                                          • SPIxCON2
• Input, Output, and Client Select Polarity
                                                          • The CLRBF bit of SPIxSTATUS
• Data Input Sample Phase (middle or end of data
  output time)                                              Note 1: The BUSY bit is subject to synchronization
• Clock Edge (output data on first/second edge of                   delay of up to two instruction cycles. The
  SCK)                                                              user must wait for it to set after loading the
                                                                    transmit buffer (SPIxTXB register) before
• Clock Rate (Host mode only)
                                                                    using it to determine the status of the SPI
• Client Select Mode (Host or Client mode)                          module.
• MSB-First or LSB-First
                                                                   2: It is also not recommended to read
• Receive/Transmit Modes                                              SPIxTCNTH/L while the BUSY bit is set,
  - Full duplex                                                       as the value in the registers may not be a
  - Receive-without-transmit                                          reliable indicator of the Transfer Counter.
  - Transmit-without-receive                                          Use the Transfer Count Zero Interrupt
• Transfer Counter Mode (Transmit-without-receive                     Flag (the TCZIF bit of SPIxINTF) to
  mode)                                                               accurately determine that the Transfer
                                                                      Counter has reached zero.
32.3.1      ENABLING AND DISABLING THE
            SPI MODULE
To enable the serial peripheral, the SPI enable bit (EN
in SPIxCON0) must be set. To reset or reconfigure SPI
mode, clear the EN bit, re-initialize the SPIxCONx
registers and then set the EN bit. Setting the EN bit
enables the SPI inputs and outputs: SDI, SDO,
SCK(out), SCK(in), SS(out), and SS(in). All of these
inputs and outputs are steered by PPS, and thus must
have their functions properly mapped to device pins to
function (see Section 17.0 “Peripheral Pin Select
(PPS) Module”). In addition, SS(out) and SCK(out)
must have the pins they are steered to set as outputs
(TRIS bits must be ‘0’) in order to properly output.
Clearing the TRIS bit of the SDO pin will cause the SPI
module to always control that pin, but is not necessary
for SDO functionality. (see Section 32.3.5 “Input and
Output Polarity Bits”). Configurations selected by the
following registers may not be changed while the EN bit
is set:
• SPIxBAUD
• SPIxCON1
• SPIxCON0 (except to clear the EN bit)
Clearing the EN bit aborts any transmissions in
progress, disables the setting of interrupt flags by
hardware, and resets the FIFO occupancy (see
Section 32.3.3 “Transmit and Receive FIFOs” for
more FIFO details).


 2017-2021 Microchip Technology Inc.                                                     DS40001919G-page 518
                        PIC18(L)F26/27/45/46/47/55/56/57K42
32.3.3       TRANSMIT AND RECEIVE FIFOS                         32.3.5       INPUT AND OUTPUT POLARITY
The transmission and reception of data from the SPI                          BITS
module is handled by two FIFOs, one for reception and           SPIxCON1 has three bits that control the polarity of the
one for transmission (addressed by the SFRs SPIxRXB             SPI inputs and outputs. The SDIP bit controls the
and SPIxTXB, respectively.). The TXFIFO is written by           polarity of the SDI input, the SDOP bit controls the
software and is read by the SPI module to shift the data        polarity of the SDO output, and the SSP bit controls the
onto the SDO pin. The RXFIFO is written by the SPI              polarity of both the client SS input and the host SS
module as it shifts in the data from the SDI pin and is         output. For all three bits, when the bit is clear, the input
read by software. Setting the CLRBF bit of                      or output is active-high, and when the bit is set, the
SPIxSTATUS resets the occupancy for both FIFOs,                 input or output is active-low. When the EN bit of
emptying both buffers. The FIFOs are also reset by dis-         SPIxCON0 is cleared, SS(out) and SCK(out) both
abling the SPI module.                                          revert to the inactive state dictated by their polarity bits.
                                                                The SDO output state when the EN bit of SPIxCON0 is
  Note:      TXFIFO      occupancy       and    RXFIFO
                                                                cleared is determined by several factors.
             occupancy simply refer to the number of
             bytes that are currently being stored in           • When the associated TRIS bit for the SDO pin is
             each FIFO. These values are used in this             cleared, and the SPI goes idle after a transmis-
             chapter to illustrate the function of these          sion, the SDO output will remain at the last bit
             FIFOs and are not directly accessible                level. The SDO pin will revert to the Idle state if
             through software.                                    EN is cleared.
                                                                • When the associated TRIS bit for the SDO pin is
The SPIxRXB register addresses the receive FIFO and
                                                                  set, behavior varies in Client and Host mode.
is read-only. Reading from this register will read from
the first FIFO location that was written to by hardware           - In Client mode, the SDO pin tri-states when:
and decrease the RXFIFO occupancy. If the FIFO is                 - Client Select is inactive,
empty, reading from this register will instead return a           - the EN bit of SPIxCON0 is cleared, or when
value of zero and set the RXRE (Receive Buffer Read               - the TXR bit of SPIxCON2 is cleared.
Error) bit of the SPIxSTATUS register. The RXRE bit
                                                                  - In Host mode, the SDO pin tri-states when
must then be cleared in software in order to properly
                                                                     TXR = 0. When TXR = 1 and the SPI goes
reflect the status of the read error. When RXFIFO is full,
                                                                     idle after a transmission, the SDO output will
the RXBF bit of the SPIxSTATUS register will be set.
                                                                     remain at the last bit level. The SDO pin will
When the device receives data on the SDI pin, the
                                                                     revert to the Idle state if EN is cleared.
receive FIFO may be written to by hardware and the
occupancy increased, depending on the mode and
receiver settings, as summarized in Table 32-1.
The SPIxTXB register addresses the transmit FIFO
and is write-only. Writing to the register will write to the
first empty FIFO location and increase the occupancy.
If the FIFO is full, writing to this register will not affect
the data and will set the TXWE bit of the SPIxSTATUS
register. When the TXFIFO is empty, the TXBE bit of
SPIxSTATUS will be set. When a data transfer occurs,
data may be read from the first FIFO location written to
and the occupancy decreases, depending on mode
and transmitter settings, as summarized in Table 32-1
and Section 32.6 “Client Mode”.

32.3.4       LSB VS. MSB-FIRST OPERATION
Typically, SPI communication is output Most-Significant
bit first, but some devices/buses may not conform to
this standard. In this case, the LSBF bit may be used to
alter the order in which bits are shifted out during the
data exchange. In both Host and Client mode, the
LSBF bit of SPIxCON0 controls if data is shifted MSb or
LSb first. Clearing the bit (default) configures the data
to transfer MSb first, which is traditional SPI operation,
while setting the bit configures the data to transfer LSb
first.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 519
                       PIC18(L)F26/27/45/46/47/55/56/57K42
32.4      Transfer Counter                                    SPIxTCNTL value is written. Transfer clocks are
                                                              suspended when the receive FIFO is full and resume
In all host modes, the transfer counter can be used to        as the FIFO is read.
determine how many data transfers the SPI will send/
receive. The transfer counter is comprised of the             32.4.2      VARIABLE TRANSFER SIZE MODE
SPIxTCNTH/L set of registers, and is also partially                       (BMODE = 1)
controlled by the SPIxTWIDTH register. The Transfer
Counter has two primary modes, determined by the              In this mode, SPIxTWIDTH specifies the width of every
BMODE bit of the SPIxCON0 register. Each mode uses            individual piece of the data transfer in bits.
the SPIxTCNTH/L and SPIxTWIDTH registers to                   SPIxTCNTH/SPIxTCNTL specifies the number of
determine the number and size of the transfers. In both       transfers of this bit length. If SPIxTWIDTH = 0, each
modes, when the transfer counter reaches zero, the            piece is a full byte of data. If SPIxTWIDTH ≠ 0, then
TCZIF interrupt flag is set.                                  only the specified number of bits from the transmit
                                                              FIFO are shifted out, with the unused bits ignored.
  Note:     When BMODE=1 in all host modes (and               Received data is padded with zeros in the unused bit
            at all times in client modes), the Transfer       areas when transfered into the receive FIFO. The
            Counter will still decrement as transfers         LSBF bit of SPIxCON0 determines whether the Most
            occur and can be used to count the                Significant or Least Significant bits of the transfers are
            number of messages sent/received, as              ignored/padded. In this mode, the transfer counter
            well as to control SS(out) and to trigger         being zero only stops messages from being sent/
            TCZIF. Also when BMODE = 1, the                   received when in Receive-only mode.
            SPIxTWIDTH register can be used in Host
            and Client modes to determine the size of           Note:     With BMODE = 1, it is possible for the
            messages sent and received by the SPI,                        transfer counter (SPIxTCNTH/L) to decre-
            even if the Transfer Counter is not being                     ment below zero, although when in
            actively used to control the number of                        Receive-only Host mode, transfer clocks
            messages being sent/received by the SPI                       will cease when the transfer counter
            module.                                                       reaches zero.

32.4.1      TOTAL BIT COUNT MODE
            (BMODE = 0)
In this mode, SPIxTCNTH/L and SPIxTWIDTH are
concatenated to determine the total number of bits to
be transferred. These bits will be loaded from/into the
transmit/receive FIFOs in 8-bit increments and the
transfer counter will be decremented by eight until the
total number of remaining bits is less than eight. If there
are any remaining bits (SPIxTWIDTH ≠ 0), the transmit
FIFO will send out one final message with any extra bits
greater than the remainder ignored. The SPIxTWIDTH
is the remaining bit count but the value does not
change as it does for the SPIxTCNT value. Similarly,
the receiver will load a final byte into the receiver FIFO,
and pad the extra bits with zeros. The LSBF bit of
SPIxCON0 determines whether the Most Significant or
Least Significant bits of this final byte are ignored/
padded. For example, when LSBF = 0 and the final
transfer contains only two bits then if the last byte sent
was 5Fh then the RXB of the receiver will contain 40h
which are the two MSbits of the final byte padded with
zeros in the LSbits.
In this mode, the SPI host will only transmit messages
when the SPIxTCNT value is greater than zero,
regardless of TXR and RXR settings. In Host Transmit
mode, the transfer starts with the data write to the
SPIxTXB register or the count value written to the
SPIxTCNTL register, which ever occurs last. In Host
Receive-only mode, the transfer clocks start when the


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 520
                       PIC18(L)F26/27/45/46/47/55/56/57K42
32.4.3      TRANSFER COUNTER IN CLIENT                         32.5     Host mode
            MODE
                                                               In host mode, the device controls the SCK line, and as
In Client Mode, the transfer counter will still decrement      such, initiates data transfers and determines when any
as data is shifted in and out of the SPI module, but it will   client broadcast data onto the SPI bus.
not control data transfers. In addition, in Client mode,
                                                               Host mode of this device can be configured in four dif-
the BMODE bit along with the transfer counter is used
                                                               ferent modes, configured by the TXR and RXR bits:
to determine when the device may look for Client
Select faults. If BMODE = 0, the SSFLT bit will be set if      • Full Duplex mode
Client Select transitions from its active to inactive state    • Receive-Only mode
during bytes of data, as well as if it transitions before      • Transmit-Only mode
the last bit sent during the final byte (if
                                                               • Transfer-Off mode
SPIxTWIDTH ≠ 0). If BMODE = 1, the SSFLT bit will be
set if Client Select transitions from its active to inactive   The modes are illustrated in Table 32-1, below:
state before the final bit of each individual transfer is
completed. Note that SSFLT does not have an associ-
ated interrupt, so it may be checked in software. An
ideal time to do this is when the End of Client Select
Interrupt (EOSIF) is triggered (see Section 32.8.3.3
“Start of Client Select and End of Client Select
Interrupts”).
TABLE 32-1:        HOST MODE TXR/RXR SETTINGS
                                        TXR = 1                                          TXR = 0
                                Full Duplex Mode
                                                                                  Receive-Only mode
               If BMODE = 1, transfer when RxFIFO is not full and
                                                                        Transfer when RxFIFO is not full and the
                              TxFIFO is not empty
 RXR = 1                                                                      Transfer Counter is non-zero
                  If BMODE = 0, Transfer when RXFIFO is not full,
                                                                      Transmitted data is either the top of the FIFO
              TXFIFO is not empty, and the Transfer Counter is non-
                                                                           or the most recently received data
                                       zero
                               Transmit-Only Mode
                  If BMODE = 1, transfer when TxFIFO is not empty
 RXR = 0      If BMODE = 0, Transfer when TXFIFO is not empty and                     No Transfers
                         the Transfer Counter is non-zero
                            Received data is not stored


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 521
                                PIC18(L)F26/27/45/46/47/55/56/57K42
32.5.1             FULL DUPLEX MODE
When both TXR and RXR are set, the SPI host is in Full
Duplex mode. In this mode, data transfer triggering is
affected by the BMODE bit of SPIxCON0.
When BMODE = 1, data transfers will occur whenever
both the RXFIFO is not full and there is data present in
the TXFIFO. In practice, as long as the RXFIFO is not
full, data will be transmitted/received as soon as the
SPIxTxB register is written to, matching functionality of
SPI (MSSP) modules on older 8-bit Microchip devices.
The SPIxTCNT will decrement with each transfer.
However, when SPIxTCNT is zero the next transfer is
not inhibited and the corresponding SPIxTCNT
decrement will cause the count to roll over to the
maximum value. Figure 32-3 shows an example of a
communication using this mode.
When BMODE = 0, the transfer counter (SPIxTCNTH/
SPIxTCNTL) must also be written to before transfers
will occur, and transfers will cease when the transfer
counter reaches ‘0’. For example, if SPIxTXB is written
twice and then SPIxTCNTL is written with ‘3’ then the
transfer will start with the SPIxTCNTL write. The two
bytes in the TXFIFO will be sent after which the transfer
will suspend until the third and last byte is written to
SPIxTXB.

FIGURE 32-3:                    SPI HOST OPERATION – DATA EXCHANGE, TXR/RXR = 1/1
                                                                                                                                                   Rev. 10-000281A
                                                                                                                                                          9/22/2016
   Software Write to
                       Note 2
         SPIxTCNT
         SPIxTCNT       0             5               4               3                   2                      1                        0

  Software Write To
               TXR

               TXR
   Software Write to
              RXR
               RXR

           SCK_out                                                                                Note 3

          SDO_out                                                                                          `HX                           `HX

           SRMTIF


             TCZIF                                                                                                    Note 2


     Software Write
        to SPIxTXB
          TXFIFO        0         1       2       1       2       1           2           1           0               1                   0
        Occupancy
           SPIxTIF


     Software Read
     from SPIxRXB
          RXFIFO                  0               1           0           1       0   1       0       1                        0     1         0
        Occupancy

           SPIxRIF


            Note: 1. SS(out) is not shown on this diagram
                   2. SPIxTCNT write is optional TXR/RXR = 1/1 and BMODE=1. If BMODE=0, a write to SPIxTCNT is required to start
                       transmission; TCZIF signals the end of the transmission.
                   3. Transmission gap occurs while waiting for transmitter data.


 2017-2021 Microchip Technology Inc.                                                                                              DS40001919G-page 522
                                      PIC18(L)F26/27/45/46/47/55/56/57K42
32.5.2                TRANSMIT-ONLY MODE
When TXR is set and RXR is clear, the SPI host is in
Transmit-Only mode. In this mode, data transfer
triggering is affected by the BMODE bit of SPIxCON0.
When BMODE = 1, data transfers will occur whenever
TXFIFO is not empty. Data will be transmitted as soon
as the TXFIFO register is written to, matching
functionality of SPI (MSSP) modules on previous 8-bit
Microchip devices. The SPIxTCNT will decrement with
each transfer. However, when SPIxTCNT is zero the
next transfer is not inhibited and the corresponding
SPIxTCNT decrement will cause the count to roll over
to the maximum value. Any data received in this mode
is not stored in RXFIFO. Figure 32-4 shows an
example of sending a command and then sending a
byte of data, using this mode.
When BMODE = 0, the transfer counter (SPIxTCNTH/
L) must also be written to before transfers will occur,
and transfers will cease when the transfer counter
reaches ‘0’.
For example, if SPIxTXB is written twice and then
SPIxTCNTL is written with ‘3’, the transfer will start with
the SPIxTCNTL write. The two bytes in the TXFIFO will
be sent after which the transfer will suspend until the
third and last byte is written to SPIxTXB.

FIGURE 32-4:                              SPI HOST OPERATION, COMMAND+WRITE DATA, TXR/RXR=1/0
                                                                                                                                                         Rev. 10-
                                                                                                                                                         000282A
                                                                                                                                                        9/22/2016


  Software Write to                                               Note 2
        TXTCNTL
      SPIxTXCNT                           0             -1           -2             3                 2                  1                0

    Software Write
           to TXR

              TXR

    Software Write
           to RXR
              RXR

          SCK_out

         SDO_out       Shifted data out

          SRM TIF                                        Note 3


            BCZIF


    Software Write                                                                                         Note 4
       to SPIxTXB
          TxFIFO           0              1   2         1             0        1        2         1       2          1                    0
       Occupancy
          SPIxTIF


            Note: 1. SS(out) is not shown
                  2. The byte counter is optional when TXR/RXR = 1/0;
                  3. After the command bytes, wait for SRMTIF before loading SPIxBYTESL otherwise the command bytes would decrement BYTES.
                     Alternatively, load BC = 5 and count the command bytes also; TCZIF signals the end of the transmission.
                  4. Transmit data interrupt handler (or DMA) must write only the bytes necessary; the byte counter is not available as an indicator.
                  5. Reading the RXFIFO is not required because RXR = 0.


 2017-2021 Microchip Technology Inc.                                                                                                    DS40001919G-page 523
                                   PIC18(L)F26/27/45/46/47/55/56/57K42
32.5.3           RECEIVE-ONLY MODE                                                            data written to the TXFIFO will be transmitted on each
                                                                                              data exchange, although the TXFIFO occupancy will
When RXR is set and TXR is clear, the SPI host is in
                                                                                              not change, meaning that the same message will be
Receive-Only mode. In this mode, data transfers when
                                                                                              sent on each transmission. If there is no data in the
the RXFIFO is not full and the Transfer Counter is non-
                                                                                              TXFIFO, the most recently received data will instead be
zero. In this mode, writing a value to SPIxTCNTL will
                                                                                              transmitted. Figure 32-5 shows an example of sending
start the clocks for transfer. The clocks will suspend
                                                                                              a command using Section 32.5.2 “Transmit-Only
while the RXFIFO is full and cease when the
                                                                                              Mode” and then receiving a byte of data using this
SPIxTCNT reaches zero (see Section 32.4 “Transfer
                                                                                              mode.
Counter”). If there is any data in the TXFIFO, the first

FIGURE 32-5:                         SPI HOST OPERATION, COMMAND+READ DATA, TXR/RXR=0/1
                                                                                                                                                                   Rev. 10-
                                                                                                                                                                   000283A
                                                                                                                                                                 10/13/2016


     Software Write to
             TxCNTL
          SPIxTXCNT                             0               -1        -2              3                 2               1                     0

     Software Write to
                 TXR

                 TXR
       Software Write
              to RXR

                 RXR
             SCK_out

            SDO_out      Shifted data out

             SRMTIF                                             Note 2

               TCZIF


       Software Write
          to SPIxTXB
              TXFIFO         0              1       2       1                                                       0
           Occupancy


       Software Read
       from SPIxRXB

            RXFIFO                                              0                                      1        0       1        0        1           0
          Occupancy

             SPIxRIF


                Note: 1. SS(out) is not shown
                      2. Software must wait for shift-register empty (SRMTIF) before changing TXR, RXR, BYTES and BITS controls.
                         This is not considered an imposition in this case, because the FOLHQW probably needs time to load output data (see also Figure 4-14).


32.5.4           TRANSFER OFF MODE
When both TXR and RXR are cleared, the SPI host is
in Transfer Off mode. In this mode, SCK will not toggle
and no data is exchanged. However, writes to SPIxTXB
will be transferred to the TXFIFO which will be
transmitted if the TXR bit is set.


 2017-2021 Microchip Technology Inc.                                                                                                         DS40001919G-page 524
                                  PIC18(L)F26/27/45/46/47/55/56/57K42
32.5.5                HOST MODE CLIENT SELECT                                                   and its polarity is controlled by the SSP bit of
                      CONTROL                                                                   SPIxCON1. Setting the SSET bit will also assert
                                                                                                SS(out). Clearing the SSET bit will leave SS(out) to be
32.5.5.1               Hardware Client Select Control                                           controlled by the Transfer Counter. When the Transfer
                                                                                                Counter is loaded, the SPI module will automatically
This SPI module allows for direct hardware control of a
                                                                                                assert the SS. When the Transfer Counter decrements
Client Select output. The Client Select output SS(out)
                                                                                                to zero, the SPI module will deassert SS either one
is controlled both directly, through the SSET bit of
                                                                                                baud period after the final SCK pulse of the final
SPIxCON2, as well indirectly by the hardware while the
                                                                                                transfer (if CKE/SMP = 0/1) or one half baud period
transfer counter is non-zero (see Section 32.4
                                                                                                otherwise (see Figure 32-6).
“Transfer Counter”). SS(out) is steered by the PPS
registers to pins (see Section 17.2 “PPS Outputs”)

FIGURE 32-6:                       SPI HOST SS OPERATION- CKE = 0, BMODE = 1, TCWIDTH = 0, SSP = 0
                                                                                                                                                           Rev. 10-
                                                                                                                                                           000284A
                                                                                                                                                          9/14/2016
             SPIEN


       baud_clock


  Software Write to
       SPIxTCNTL


          Transfer                                                        1                                                              0
          Counter


           SS_out

                                               minimum 1 baud clock when FST = 0                                  approx. 1 baud clock

          SCK_out


  SDO_bit_number                                  7         6         5        4    3       2       1        0


     Note:     1. SDO bit number illustrates the transmitted bit number, and is not intended to imply SDO (out) tristate operation.
               2. Assumes SPIxTXB holds data when SPIxTCNTL is written.


32.5.5.2               Software Client Select Control
Client Select can also be controlled through software
via a general purpose I/O pin. In this case, ensure that
the pin in question is configured as a GPIO through
PPS (see Section 17.2 “PPS Outputs”), and ensure
that the pin is set as an output (clear the appropriate bit
in the appropriate TRIS register). In this case, SSET
will not affect the client select, the Transfer Counter will
not automatically control the client select output, and all
setting and clearing of the client select output line must
be directly controlled by software.


 2017-2021 Microchip Technology Inc.                                                                                                        DS40001919G-page 525
                         PIC18(L)F26/27/45/46/47/55/56/57K42
32.5.6      HOST MODE SPI CLOCK
            CONFIGURATION

32.5.6.1      SPI Clock Selection
The clock source for SPI host modes is selected by the
SPIxCLK register. Selections include the following:
• FOSC
• HFINTOSC
• CLKREF
• Timer0_overflow
• Timer2_Postscaled
• Timer4_Postscaled
• Timer6_Postscaled
• SMT_match
The SPIxBAUD register allows for dividing this clock.
The frequency of the SCK output is defined by
Equation 32-1:

EQUATION 32-1:            FREQUENCY OF SCK
                          OUTPUT SIGNAL
                               F C SEL
             F BAU D = ---
                         -----
                             ------------------------
                        2   BAU D + 1 


where FBAUD is the baud rate frequency output on the
SCK pin, FCSEL is the frequency of the input clock
selected by the SPIxCLK register, and BAUD is the
value contained in the SPIxBAUD register.

32.5.6.2      CKE, CKP and SMP
The CKP, CKE, and SMP bits control the relationship
between the SCK clock output, SDO output data
changes, and SDI input data sampling. The bit
functions are as follows:
• CKP - SCK output polarity
• CKE - SDO output change relative to the SCK
  clock
• SMP - SDI input sampling relative to the clock
  edges
The CKE bit, when set, inverts the low Idle state of the
SCK output to a high Idle state.
Figure 32-7 through Figure 32-10 illustrate the eight
possible combinations of the CKP, CKE, and SMP bit
selections.
When the CKE bit is set, the SDO data is valid before
there is a clock edge on SCK. When the CKE bit is
cleared, the SDO data is undefined prior to the first
SCK edge.
  Note:     All timing diagrams assume the LSBF bit
            of SPIxCON0 is cleared.


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 526
                           PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 32-7:                   CLOCKING DETAIL-HOST MODE, CKE/SMP = 0/0
                                                                                                                                                                                       Rev. 10-
                                                                                                                                                                                       000276A
                                                                         MSTEN = ,CKE = , SMP =                                                                                   10/10/2016


                       SCK                       A       I   A       I     A     I   A       I   A       I    A      I   A       I   A       I

                       SDO      Previous bit 0       bit 7       bit 6       bit 5       bit 4       bit 3       bit 2       bit 1   bit 0                         CKP = 

          input sample clock


                       SCK                       A       I   A       I     A     I   A       I   A       I    A      I   A       I   A       I

                       SDO      Previous bit 0       bit 7       bit 6       bit 5       bit 4       bit 3       bit 2       bit 1   bit 0                         CKP = 

          input sample clock


                                                                                                                                                 RXFIFO Occupancy increments
                                   T;FIFO                                                                    Open R;FIFO                         TXFIFO Occupancy decrements
                               determined                                                                           latch                        SPIxRIF and SPIxTIF interrupts
                                                                                                                                                 trigger


FIGURE 32-8:                   CLOCKING DETAIL-HOST MODE, CKE/SMP = 1/1

                                                                                                                                                                                       Rev. 10-
                                                                                                                                                                                       000315A
                                                                                                                                                                                     10/13/2016
                                                                     MSTEN = , CKE = , SMP = 


                       SCK                       A       I   A       I     A     I   A       I   A       I    A      I   A       I   A       I

                       SDO                   bit 7       bit 6       bit 5       bit 4       bit 3       bit 2       bit 1       bit 0       next                  CKP = 
                                    tx_buf
          input sample clock         write


                                                 A       I   A       I     A     I   A       I   A       I    A      I   A       I   A       I
                       SCK

                       SDO                   bit 7       bit 6       bit 5       bit 4       bit 3       bit 2       bit 1       bit 0       next                  CKP = 
                                    tx_buf
          input sample clock         write


                                   T;FIFO                                                                    Open R;FIFO                         RXFIFO Occupancy increments
                               determined                                                                           latch                        TXFIFO Occupancy decrements
                                                                                                                                                 SPIxRIF and SPIxTIF interrupts
                                                                                                                                                 trigger


 2017-2021 Microchip Technology Inc.                                                                                                                                    DS40001919G-page 527
                         PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 32-9:              CLOCKING DETAIL-HOST MODE, CKE = 0, SMP = 1
                                                                                                                                                                                                                      Rev. 10-
                                                                                                                                                                                                                      000277A
                                                                                                                                                                                                                     9/14/2016
                                                                                        MSTEN = , CKE = , SMP = 

                                 SCK                           A       I        A       I       A        I        A       I       A       I       A        I       A       I       A       I

                                 SDO previous bit 0            bit 7            bit 6           bit 5             bit 4            bit 3          bit 2            bit 1           bit 0                      CKP = 

                   input sample clock


                                 SCK                           A       I        A       I       A        I        A       I       A       I       A        I       A       I       A       I

                                 SDO previous bit 0            bit 7            bit 6           bit 5             bit 4            bit 3          bit 2            bit 1           bit 0                      CKP = 

                   input sample clock


                               T;FIFO determined                                                                                   Open R;FIFO latch                                           RXFIFO Occupancy increments,
                                                                                                                                                                                               TXFIFO Occupancy decrements,
                                                                                                                                                                                               SPIxRIF and SPIxTIF interrupts
                                                                                                                                                                                               trigger


FIGURE 32-10:             CLOCKING DETAIL-HOST MODE, CKE = 1, SMP = 0
                                                                                                                                                                                                                         Rev. 10-
                                                                                                                                                                                                                         000278A
                                                                                                                                                                                                                        9/14/2016
                                                                                        MSTEN =, CKE = , SMP = 

                             SCK                   I     A I            A       I A           I       A       I A           I A               I A I             A

                             SDO                       bit 7       bit 6            bit 5           bit 4             bit 3           bit 2           bit 1        bit 0                                   CKP = 

                input sample clock        tx_buf
                                           write


                             SCK                   I     A         I       A        I       A       I        A        I       A       I       A       I        A       I       A

                             SDO                   bit 7           bit 6            bit 5           bit 4             bit 3           bit 2           bit 1            bit 0                               CKP = 

                input sample clock        tx_buf
                                           write


                                     T;FIFO to SDO                                                                                Open R;FIFO latch                                        RXFIFO Occupancy increments,
                                                                                                                                                                                           TXFIFO Occupancy decrements,
                                                                                                                                                                                           SPIxRIF and SPIxTIF interrupts
                                                                                                                                                                                           trigger


32.5.6.3      SCK Start-Up Delay                                                                                              SPIxBAUD (indicating lower SCK frequencies), this
                                                                                                                              delay is much smaller and the first SCK can appear
When starting an SPI data exchange, the host device
                                                                                                                              relatively quickly after SS is set.
sets the SS output (either through hardware or
software) and then triggers the module to send data.                                                                          By default, the SPI module inserts a ½ baud delay (half
These data triggers are synchronized to the clock                                                                             of the period of the clock selected by the SPIxCLK
selected by the SPIxCLK register before the first SCK                                                                         register) before the first SCK pulse. This allows for
pulse appears, usually requiring one or two clocks of                                                                         systems with a high SPIxBAUD value to have extra set-
the selected clock.                                                                                                           up time before the first clock. Setting the FST bit in
                                                                                                                              SPIxCON1 removes this additional delay, allowing
The SPI module includes synchronization delays on
                                                                                                                              systems with low SPIxBAUD values (and thus, long
SCK generation specifically designed to ensure that
                                                                                                                              synchronization delays) to forego this unnecessary
the Client Select output timing is correct, without
                                                                                                                              extra delay.
requiring precision software timing loops.
When the value of the SPIxBAUD register is a small
number (indicating higher SCK frequencies), the
synchronization delay can be relatively long between
setting SS and the first SCK. With larger values of


 2017-2021 Microchip Technology Inc.                                                                                                                                                                     DS40001919G-page 528
                         PIC18(L)F26/27/45/46/47/55/56/57K42
32.6      Client Mode                                                  to the value of the LAT bit associated with the SDO pin.
                                                                       When the SPI module is active, its output is determined
32.6.1        CLIENT MODE TRANSMIT OPTIONS                             by both TXR and whether there is data in the TXFIFO.
The SDO output of the SPI module in Client mode is                     When the TRIS bit associated with the SDO pin is set,
controlled by the TXR bit of SPIxCON2, the TRIS bit                    the pin will only have an output level driven to it when
associated with the SDO pin, the Client Select input,                  TXR = 1 and the client select input is true. In all other
and the current state of the TXFIFO. This control is                   cases, the pin will be tri-stated.
summarized in Table 32-2. In this table, TRISxn refers
to the bit in the TRIS register corresponding to the pin               32.6.1.2         SDO Output Data
that SDO has been assigned with PPS, TXR is the                        The TXR bit controls the nature of the data that is
Transmit Data Required Control bit of SPIxCON2, SS                     transmitted in Client mode. When TXR is set,
is the state of the Client Select input, and TXBE is the               transmitted data is taken from the TXFIFO. If the FIFO
TXFIFO Buffer Empty bit of SPIxSTATUS.                                 is empty, the most recently received data will be
                                                                       transmitted and the TXUIF flag will be set to indicate
32.6.1.1        SDO Drive/Tri-state                                    that a transmit FIFO underflow has occurred.
The TRIS bit associated with the SDO pin controls                      When TXR is cleared, the data will be taken from the
whether the SDO pin will tri-state. When this TRIS bit is              TXFIFO, and the TXFIFO occupancy will not decrease.
cleared, the pin will always be driving to a level, even               If the TXFIFO is empty, the most recently received data
when the SPI module is inactive. When the SPI module                   will be transmitted, and the TXUIF bit will not be set.
is inactive (either due to the host not clocking the SCK               However, if the TRIS bit associated with the SDO pin is
line or the SS being false), the SDO pin will be driven                set, clearing the TXR bit will cause the SPI module to
                                                                       not output any data to the SDO pin.
TABLE 32-2:          CLIENT MODE TRANSMIT
     TRISxn(1)             TXR               SS               TXBE                               SDO State
          0                  0             FALSE                0          Drives state determined by LATxn(2)
          0                  0             FALSE                1          Drives state determined by LATxn(2)
          0                  0             TRUE                 0          Outputs the oldest byte in the TXFIFO
                                                                           Does not remove data from the TXFIFO
          0                  0             TRUE                 1          Outputs the most recently received byte
          0                  1             FALSE                0          Drives state determined by LATxn(2)
          0                  1             FALSE                1          Drives state determined by LATxn(2)
          0                  1             TRUE                 0          Outputs the oldest byte in the TXFIFO
                                                                           Removes transmitted byte from the TXFIFO
                                                                           Decrements occupancy of TXFIFO
          0                  1             TRUE                 1          Outputs the most recently received byte
                                                                           Sets the TXUIF bit of SPIxINTF
          1                  0             FALSE                0          Tri-stated
          1                  0             FALSE                1          Tri-stated
          1                  0             TRUE                 0          Tri-stated
          1                  0             TRUE                 1          Tri-stated
          1                  1             FALSE                0          Tri-stated
          1                  1             FALSE                1          Tri-stated
          1                  1             TRUE                 0          Outputs the oldest byte in the TXFIFO
                                                                           Removes transmitted byte from the TXFIFO
                                                                           Decrements occupancy of TXFIFO
          1                  1             TRUE                 1          Outputs the most recently received byte
                                                                           Sets the TXUIF bit of SPIxINTF
Note 1:       TRISxn is the bit in the TRISx register corresponding to the pin that SDO has been assigned with PPS.
     2:       LATxn is the bit in the LATx register corresponding to the pin that SDO has been assigned with PPS.


 2017-2021 Microchip Technology Inc.                                                                     DS40001919G-page 529
                                  PIC18(L)F26/27/45/46/47/55/56/57K42
32.6.2             CLIENT MODE RECEIVE OPTIONS
The RXR bit controls the nature of receptions in client
mode. When RXR is set, the SDI input data will be
stored in the RXFIFO if it is not full. If the RXFIFO is full,
the RXOIF bit will be set to indicate an RXFIFO over-
flow error and the data is discarded. When RXR is
cleared, all received data will be ignored and not stored
in the RXFIFO (although it may still be used for trans-
mission if TXFIFO is empty). Figure 32-11 shows a typ-
ical Client mode communication, showing a case
where the host writes two then three bytes, showing
interrupts as well as the behavior of the transfer
counter in Client mode (see Section 32.4.3 “Transfer
Counter in Client mode” for more details on
Section 32.8 “SPI Interrupts” the transfer counter in
Client mode as well as Section 32.8 “SPI Interrupts”
for more information on interrupts).

FIGURE 32-11:                         SPI CLIENT MODE OPERATION – INTERRUPT-DRIVEN, HOST WRITES 2+3
                                      BYTES
                                                                                                                                                    Rev. 10-
                                                                                                                                                    000285A
                                                                                                                                                   9/22/2016


              SS_in

            SCK_in                                                    Note 1

           SDO_out      Output data

             SOSIF                    Note 2

             EOSIF


    Transfer Counter                   0                 -1          -2                 3                2                1           0


    Software Write to                                                          Note 3
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


              Note: 1. This delay is exaggerated for illustration, and can be as short as1/2 bit period.
                    2. If the device is sleeping, SOSIF will wake it up for interrupt service.
                    3. Setting SPIxTCNTL is optional in this example, otherwise it will count -3, -4, -5, and TCZIF will not occur


 2017-2021 Microchip Technology Inc.                                                                                                DS40001919G-page 530
                        PIC18(L)F26/27/45/46/47/55/56/57K42
32.6.3       CLIENT MODE CLIENT SELECT                         32.6.5      DAISY-CHAIN CONFIGURATION
In Client mode, an external Client Select Signal can be        The SPI bus can be connected in a daisy-chain
used to synchronize communication with the Host                configuration. The first client output is connected to the
device. The Client Select line is held in its inactive state   second client input, the second client output is
(high by default) until the host device is ready to            connected to the third client input, and so on. The final
communicate. When the Client Select transitions to its         client output is connected to the host input. Each client
active state, the client knows that a new transmission is      sends out, during a second group of clock pulses, an
starting.                                                      exact copy of what was received during the first group
When the Client Select goes false at the end of the            of clock pulses. The whole chain acts as one large
transmission the receive function of the selected SPI          communication shift register. The daisy-chain feature
Client device returns to the inactive state. The client is     only requires a single Client Select line from the host
then ready to receive a new transmission when the Cli-         device connected to all client devices (alternately, the
ent Select goes True again.                                    client devices can be configured to ignore the client
                                                               select line by setting the SSET bit). In a typical Daisy-
The Client Select signal is received on the SS input pin.      Chain configuration, the SCK signal from the host is
This pin is remappable with the SPIxSSPPS register             connected to each of the client device SCK inputs.
(see Section 17.1 “PPS Inputs”). When the input on             However, the SCK input and output are separate
this pin is true, transmission and reception are enabled,      signals selected by the PPS control. When the PPS
and the SDO pin is driven. When the input on this pin is       selection is made to configure the SCK input and SCK
false, the SDO pin is either tri-stated (if the TRIS bit       output on separate pins then, the SCK output will follow
associated with the SDO pin is set) or driven to the           the SCK input, allowing for SCK signals to be daisy-
value of the LAT bit associated with the SDO pin (if the       chained like the SDO/SDI signals.
TRIS bit associated with the SDO pin is cleared). In
addition, the SCK input is ignored.                            Figure 32-12 shows the block diagram of a typical
                                                               daisy-chain connection, and Figure 32-13 shows the
If the SS input goes False, while a data transfer is still     block diagram of a daisy-chain connection possible
in progress, it is considered a client select fault. The       using this SPI module.
SSFLT bit of SPIxCON2 indicates whether such an
event has occurred. The transfer counter value
determines the number of bits in a valid data transfer
(see Section 32.4 “Transfer Counter” for more
details).
The Client Select polarity is controlled by the SSP bit of
SPIxCON1. When SSP is set (its default state), the Cli-
ent Select input is active-low, and when it is cleared,
the Client Select input is active-high.
The Client Select for the SPI module is controlled by
the SSET bit of SPIxCON2. When the bit is cleared (its
default state), the client select will act as described
above. When the bit is set, the SPI module will behave
as if the SS input was always in its active state.


  Note:      When SSET is set, the effective SS(in)
             signal is always active. Hence, the SSFLT
             bit may be disregarded.

32.6.4       CLIENT MODE CLOCK
             CONFIGURATION
In Client Mode, SCK is an input, and must be
configured to the same polarity and clock edge as the
host device. As in Host mode, the polarity of the clock
input is controlled by the CKP bit of SPIxCON1 and the
clock edge used for transmitting data is controlled by
the CKE bit of SPIxCON1.


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 531
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 32-12:          TRADITIONAL SPI DAISY-CHAIN CONNECTION
                                                                                     Rev. 10-000082B
                                                                                            8/11/2016


                                         SCK           SCK
                           SPI +RVW     SDOx           SDIx      SPI &OLHQW
                                        SDIx            SDOx        #1

                                SSxOUT/GPIO            SSxIN


                                                        SCK
                                                        SDIx SPI &OLHQW
                                                        SDOx    #2
                                                       SSxIN


                                                        SCK
                                                        SDIx SPI &OLHQW
                                                        SDOx    #3
                                                       SSxIN


FIGURE 32-13:          SPI DAISY-CHAIN CONNECTION WITH CHAINED SCK


                                                                                   Rev. 10-000082C
                                                                                         10/13/2016


                                        SCK           SCK(in)
                          SPI +RVW      SDOx           SDIx      SPI &OLHQW
                                        SDIx                        #1
                                                      SSxIN
                               SSxOUT/GPIO
                                                      SCK(out)      SDOx


                                                       SCK(in)       SDIx

                                                                SPI &OLHQW
                                                      SSxIN        #2

                                                      SCK(out)      SDOx


                                                       SCK(in)       SDIx

                                                      SSxIN SPI &OLHQW
                                                               #3

                                                                    SDOx


 2017-2021 Microchip Technology Inc.                                         DS40001919G-page 532
                       PIC18(L)F26/27/45/46/47/55/56/57K42
32.7     SPI Operation in Sleep Mode                         32.8.2      SPI TRANSMITTER DATA
                                                                         INTERRUPT
SPI host mode will operate in Sleep, provided the clock
source selected by SPIxCLK is active in Sleep mode.          The SPI Transmitter Data Interrupt is set when TXFIFO
FIFOs will operate as they would when the part is            is not full, and is cleared when the TXFIFO is full. The
awake. When TXR = 1, the TXFIFO will need to contain         interrupt flag SPI1TXIF is located in PIRx and the
data in order for transfers to take place in Sleep. All      interrupt enable SPI1TXIE is located in PIEx. The
interrupts will still set the interrupt flags in Sleep but   interrupt flag is read-only.
only enabled interrupts will wake the device from
Sleep.                                                       32.8.3      SPI MODULE STATUS INTERRUPTS
SPI Client mode will operate in Sleep, because the           The SPIxIF flag in the respective PIR register is set
clock is provided by an external host device. FIFOs will     when any of the individual status flags in SPIxINTF and
still operate and interrupts will set interrupt flags, and   their respective SPIxINTE bits are set. In order for the
enabled interrupts will wake the device from Sleep.          setting of any specific interrupt flag to interrupt normal
                                                             program flow both the SPIxIE bit as well as the specific
                                                             bit in SPIxINTE associated with that interrupt must be
32.8     SPI Interrupts
                                                             set.
There are three top level SPI interrupts in the PIRx         The Status Interrupts are:
register:
                                                             • Shift Register Empty Interrupt
• SPI Transmit
                                                             • Transfer Counter is Zero Interrupt
• SPI Receive
                                                             • Start of Client Select Interrupt
• SPI Module status
                                                             • End of Client Select Interrupt
The status interrupts are enabled at the module level in     • Receiver Overflow Interrupt
the SPIxINTE register. Only enabled status interrupts
                                                             • Transmitter Underflow Interrupt
will cause the single top level SPIxIF flag to be set.

32.8.1      SPI RECEIVER DATA INTERRUPT
The SPI Receiver Data Interrupt is set when RXFIFO
contains data, and is cleared when the RXFIFO is
empty. The interrupt flag SPI1RXIF is located in PIRx
and the interrupt enable SPI1RXIE is located in PIEx.
This interrupt flag is read-only.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 533
                          PIC18(L)F26/27/45/46/47/55/56/57K42
32.8.3.1       Shift Register Empty Interrupt
The Shift Register Empty interrupt flag and enable are                                      Note:        The TCZIF flag only indicates that the
the SRMTIF and SRMTIE bits respectively. This                                                            transfer counter has decremented from
interrupt is only available in host mode and triggers                                                    one to zero, and may not indicate that the
when a data transfer completes and conditions are not                                                    entire data transfer process is complete.
present to start a new transfer, as dictated by the TXR                                                  Either poll the BUSY bit of SPIxCON2 and
and RXR bits (see Table 32-1 for conditions for starting                                                 wait for it to be cleared or use the Shift
a new Host mode data transfer with different TXR/RXR                                                     Register Empty Interrupt (SRMTIF) to
settings). This interrupt will be triggered at the end of                                                determine if a data transfer is fully
the last full bit period, after SCK has been low for one                                                 complete.
½-baud period. See Figure 32-14 for more details of
the timing of this interrupt as well as other interrupts.                              32.8.3.3           Start of Client Select and End of
This bit will not clear itself when the conditions for                                                    Client Select Interrupts
starting a new transfer occur, and must be cleared in
software.                                                                              The start of client select interrupt flag and enable are
                                                                                       the SOSIF and SOSIE bits, respectively, and the end of
32.8.3.2       Transfer Counter is Zero Interrupt                                      client select interrupt flag and enable are similarly
                                                                                       designated by the EOSIF and EOSIE bits. These
The Transfer Counter is zero interrupt flag and enable                                 interrupts trigger at the leading and trailing edges of the
are the TCZIF and TCZIE bits, respectively. This                                       client select input. Note that the interrupts are active in
interrupt will trigger when the transfer counter (defined                              both Host and Client mode, and will trigger on
by BMODE, SPIxTCNTH/L and SPIxTWIDTH)                                                  transitions of the client select input regardless of which
decrements from one to zero. See Figure 32-14 for                                      mode the SPI is in. In Host mode, PPS may be used to
more details on the timing of this interrupt as well as                                route the client select input to the same pin as the client
other interrupts. This bit must be cleared in software.                                select output, allowing these interrupts to trigger on
                                                                                       changes to the client select output. Also note that in
                                                                                       client mode, changing the SSET bit can trigger these
                                                                                       interrupts, as it changes the effective input value of
                                                                                       client select. Both SOSIF and EOSIF must be cleared
                                                                                       in software

FIGURE 32-14:               TRANSFER AND CLIENT SELECT INTERRUPT TIMINGS
                                                                                                                                                   Rev. 10-000286A
                                                                                                                                                          9/14/2016


                 SS(in)

                  SCK


       SDO_bit_number            7    6   5   4    3   2   1       0      7    6   5    4    3   2   1    0   7   6   5   4   3   2   1       0


              SRMTIF


                SOSIF
                Note 3


                TCZIF


                EOSIF                                                                                                                     Note 3


               Note       1: SRMTIF available only in +RVW mode
                          2: Clearing of interrupt flags is shown for illustration; actual interrupt flags must be cleared in software
                          3: SOSIF and EOSIF are set according to SS(in), even in +RVW mode.


 2017-2021 Microchip Technology Inc.                                                                                             DS40001919G-page 534
                        PIC18(L)F26/27/45/46/47/55/56/57K42
32.8.3.4      Receiver Overflow and Transmitter
              Underflow Interrupts
The receiver overflow interrupt triggers if data is
received when the RXFIFO is already full and RXR = 1.
In this case, the data will be discarded and the RXOIF
bit will be set. The receiver overflow interrupt flag is the
RXOIF bit of SPIxINTF. The receiver overflow interrupt
enable bit is the RXOIE bit of SPIxINTE.
The Transmitter Underflow interrupt flag triggers if a
data transfer begins when the TXFIFO is empty and
TXR = 1. In this case, the most recently received data
will be transmitted and the TXUIF bit will be set. The
transmitter underflow interrupt flag is the TXUIF bit of
SPIxINTF. The transmitter underflow interrupt enable
bit is the TXUIE bit of SPIxINTE.
Both of these interrupts will only occur in Client mode,
as Host mode will not allow the RXFIFO to overflow or
the TXFIFO to underflow.


 2017-2021 Microchip Technology Inc.                          DS40001919G-page 535
                      PIC18(L)F26/27/45/46/47/55/56/57K42
32.9     Register definitions: SPI

REGISTER 32-1:         SPIxINTF: SPI INTERRUPT FLAG REGISTER
 R/W/HS-0/0        R/W/HS-0/0      R/W/HS-0/0        R/W/HS-0/0        U-0      R/W/HS-0/0      R/W/HS-0/0    U-0
   SRMTIF            TCZIF              SOSIF          EOSIF            —          RXOIF          TXUIF        —
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                  W = Writable bit                  U = Unimplemented bit, read as ‘0’
                                                                    HS = Bit can be set by hardware


bit 7            SRMTIF: Shift Register Empty Interrupt Flag bit
                 Client mode:
                 This bit is ignored
                 Host mode:
                 1 = The data transfer is complete
                 0 = Either no data transfers have occurred or a data transfer is in progress
bit 6            TCZIF: Transfer Counter is Zero Interrupt Flag bit
                 1 = The transfer counter (as defined by BMODE in Register 32-7, TCNTH/L, and TWIDTH) has
                 decremented to zero
                 0= No interrupt pending
bit 5            SOSIF: Start of Client Select Interrupt Flag bit
                 1 = SS(in) transitioned from false to true
                 0 = No interrupt pending
bit 4            EOSIF: End of Client Select Interrupt Flag bit
                 1 = SS(in) transitioned from true to false
                 0 = No interrupt pending
bit 3            Unimplemented: Read as ‘0’
bit 2            RXOIF: Receiver Overflow Interrupt Flag bit
                 1 = Data transfer completed when RXBF = 1 (edge triggered) and RXR = 1
                 0 = No interrupt pending
bit 1            TXUIF: Transmitter Underflow Interrupt Flag bit
                 1 = Client Data transfer started when TXBE = 1 and TXR = 1
                 0 = No interrupt pending
bit 0            Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 536
                          PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-2:             SPIxINTE: SPI INTERRUPT ENABLE REGISTER
   R/W-0/0             R/W-0/0        R/W-0/0         R/W-0/0           U-0       R/W-0/0         R/W-0/0            U-0
   SRMTIE               TCZIE          SOSIE          EOSIE             —          RXOIE           TXUIE              —
bit 7                                                                                                                        bit 0


Legend:
R = Readable bit                   W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7               SRMTIE: Shift Register Empty Interrupt Enable bit
                    1 = Enables the Shift Register Empty Interrupt
                    0 = Disables the Shift Register Empty Interrupt
bit 6               TCZIE: Transfer Counter is Zero Interrupt Enable bit
                    1 = Enables the Transfer Counter is Zero Interrupt
                    0 = Disables the Transfer Counter is Zero Interrupt
bit 5               SOSIE: Start of Client Select Interrupt Enable bit
                    1 = Enables the Start of Client Select Interrupt
                    0 = Disables the Start of Client Select Interrupt
bit 4               EOSIE: End of Client Select Interrupt Enable bit
                    1 = Enables the End of Client Select Interrupt
                    0 = Disables the End of Client Select Interrupt
bit 3               Unimplemented: Read as ‘0’
bit 2               RXOIE: Receiver Overflow Interrupt Enable bit
                    1 = Enables the Receiver Overflow Interrupt
                    0 = Disables the Receiver Overflow Interrupt
bit 1               TXUIE: Transmitter Underflow Interrupt Enable bit
                    1 = Enables the Transmitter Underflow Interrupt
                    0 = Disables the Transmitter Underflow Interrupt
bit 0               Unimplemented: Read as ‘0’

REGISTER 32-3:             SPIxTCNTL – SPI TRANSFER COUNTER LSB REGISTER
   R/W-0/0             R/W-0/0        R/W-0/0         R/W-0/0      R/W-0/0        R/W-0/0         R/W-0/0       R/W-0/0
    TCNT7              TCNT6          TCNT5           TCNT4          TCNT3         TCNT2          TCNT1          TCNT0
        bit 7                                                                                                        bit 0


Legend:
R = Readable bit                   W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7-0             TCNT[7:0]
                    BMODE = 0
                    Bits 10-3 of the Transfer Counter, counting the total number of bits to transfer
                    BMODE = 1
                    Bits 7-0 of the Transfer Counter, counting the total number of bytes to transfer
  Note:         This register may not be written to while a transfer is in progress (BUSY bit of SPIxCON2 is set).


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 537
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-4:          SPIxTCNTH: SPI TRANSFER COUNTER MSB REGISTER
      U-0             U-0               U-0         U-0           U-0          R/W-0/0         R/W-0/0        R/W-0/0
       —               —                —           —              —           TCNT10              TCNT9       TCNT8
     bit 7                                                                                                        bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7-3          Unimplemented: Read as ‘0’
bit 2-0          TCNT[10:8]:
                 BMODE = 0
                 Bits 13-11 of the Transfer Counter, counting the total number of bits to transfer
                 BMODE = 1
                 Bits 10-8 of the Transfer Counter, counting the total number of bytes to transfer
  Note:      This register may not be written to while a transfer is in progress (BUSY bit of SPIxCON2 is set).

REGISTER 32-5:          SPIxTWIDTH: SPI TRANSFER WIDTH REGISTER
      U-0             U-0               U-0         U-0           U-0          R/W-0/0         R/W-0/0        R/W-0/0
       —               —                —           —              —          TWIDTH2         TWIDTH1         TWIDTH0
     bit 7                                                                                                        bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7-3          Unimplemented: Read as ‘0’
bit 2-0          TWIDTH[2:0]:
                 BMODE = 0
                 Bits 2-0 of the Transfer Counter, counting the total number of bits to transfer
                 BMODE = 1
                 Size (in bits) of each transfer counted by the transfer counter
                 111 = 7 bits
                 110 = 6 bits
                 101 = 5 bits
                 100 = 4 bits
                 011 = 3 bits
                 010 = 2 bits
                 001 = 1 bit
                 000 = 8 bits
  Note:      This register may not be written to while a transfer is in progress (BUSY bit of SPIxCON2 is set).


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 538
                          PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-6:             SPIxBAUD: SPI BAUD RATE REGISTER
   R/W-0/0             R/W-0/0        R/W-0/0          R/W-0/0     R/W-0/0         R/W-0/0         R/W-0/0       R/W-0/0
    BAUD7              BAUD6           BAUD5           BAUD4        BAUD3          BAUD2           BAUD1          BAUD0
        bit 7                                                                                                      bit 0


Legend:
R = Readable bit                    W = Writable bit             U = Unimplemented bit, read as ‘0’


bit 7-0             BAUD[7:0]: Baud Clock Prescaler Select bits
                    SCK high or low time: TSC=SPI Clock Period*(BAUD+1)
                    SCK toggle frequency: FSCK=FBAUD= SPI Clock Frequency/(2*(BAUD+1))
  Note:         This register may not be written while the SPI is enabled (EN bit of SPIxCON0 = 1)

REGISTER 32-7:             SPIxCON0: SPI CONFIGURATION REGISTER 0
   R/W-0/0               U-0             U-0            U-0           U-0          R/W-0/0         R/W-0/0       R/W-0/0
        EN                —                —             —             —            LSBF            MST          BMODE
bit 7                                                                                                                      bit 0


Legend:
R = Readable bit                    W = Writable bit             U = Unimplemented bit, read as ‘0’


bit 7               EN: SPI Module Enable Control bit
                    1 =SPI is enabled
                    0 = SPI is disabled,
bit 6-3             Unimplemented: Read as ‘0’
bit 2               LSBF: LSb-First Data Exchange bit
                    1 = Data is exchanged LSb first
                    0 = Data is exchanged MSb first (traditional SPI operation)
bit 1               MST: SPI Operating Mode Host Select bit
                    1 = SPI module operates as the bus host
                    0 = SPI module operates as a bus client
bit 0               BMODE: Bit-Length Mode Select bit
                    1 = SPIxTWIDTH setting applies to every byte: total bits sent is SPIxTWIDTH*SPIxTCNT, end-of-
                    packet occurs when SPIxTCNT = 0
                    0 = SPIxTWIDTH setting applies only to the last byte exchanged; total bits sent is SPIxTWIDTH +
                    (SPIxTCNT*8)
  Note:         This register may only be written when the EN bit is cleared, or to clear the EN bit.


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 539
                      PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-8:         SPIxCON1: SPI CONFIGURATION REGISTER 1
   R/W-0/0         R/W-0/0         R/W-0/0         R/W-0/0       U-0          R/W-1/1       R/W-0/0        R/W-0/0
        SMP          CKE               CKP             FST        —             SSP          SDIP           SDOP
        bit 7                                                                                                bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’


bit 7            SMP: SPI Input Sample Phase Control bit
                 Client mode:
                 1 = Reserved
                 0 = SDI input is sampled in the middle of data output time
                 Host mode:
                 1 = SDI input is sampled at the end of data output time
                 0 = SDI input is sampled in the middle of data output time
bit 6            CKE: Clock Edge Select bit
                 1 = Output data changes on transition from active to idle clock state
                 0 = Output data changes on transition from idle to active clock state
bit 5            CKP: Clock Polarity Select bit
                 1 = Idle state for SCK is high level
                 0 = Idle state for SCK is low level
bit 4            FST: Fast Start Enable bit
                 Client mode:
                 This bit is ignored
                 Host mode:
                 1 = Delay to first SCK may be less than ½ baud period
                 0 = Delay to first SCK will be at least ½ baud period
bit 3            Unimplemented: Read as ‘0’
bit 2            SSP: SS Input/Output Polarity Control bit
                 1 = SS is active-low
                 0 = SS is active-high
bit 1            SDIP: SDI Input Polarity Control bit
                 1 = SDI input is active-low
                 0 = SDI input is active-high
bit 0            SDOP: SDI Output Polarity Control bit
                 1 = SDO output is active-low
                 0 = SDO output is active-high


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 540
                        PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-9:           SPIxCON2: SPI CONFIGURATION REGISTER 2
        R-0/0         R-0/0             U-0          U-0           U-0          R/W-0/0         R/W-0/0       R/W-0/0
   BUSY(1)            SSFLT             —            —              —             SSET           TXR(2)        RXR(2)
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7             BUSY: SPI Module Busy Status bit(1)
                  1 = Data exchange is busy
                  0 = Data exchange is not taking place
bit 6             SSFLT: SS(in) Fault Status bit
                  If SSET = 0
                  1 = SS(in) ended the transaction unexpectedly, and the data byte being received was lost
                  0 = SS(in) ended normally
                  If SSET = 1
                  This bit is unchanged.
bit 5-3           Unimplemented: Read as ‘0’
bit 2             SSET: Client Select Enable bit
                  Host mode:
                  1 = SS(out) is driven to the active state continuously
                  0 = SS(out) is driven to the active state while the transmit counter is not zero
                  Client mode:
                  1 = SS(in) is ignored and data is clocked on all SCK(in) (as though SS = TRUE at all times)
                  0 = SS(in) enables/disables data input and tri-states SDO if the TRIS bit associated with the SDO pin
                  is set (see Table 32-2 for details)
bit 1             TXR: Transmit Data-Required Control bit(2)
                  1 = TxFIFO data is required for a transfer
                  0 = TxFIFO data is not required for a transfer
bit 0             RXR: Receive FIFO Space-Required Control bit(2)
                  1 = Data transfers are suspended if the RxFIFO is full
                  0 = Received data is not stored in the FIFO
   Note 1: The BUSY bit is subject to synchronization delay of up to two instruction cycles. The user must wait for it
           to set after loading the transmit buffer (SPIxTXB register) before using it to determine the status of the SPI
           module.
           2: See Table 32-1 as well as Section 32.5 “Host mode” and Section 32.6 “Client Mode” for more details
              pertaining to TXR and RXR function.
           3: This register may not be written to while a transfer is in progress (BUSY bit of SPIxCON2 is set).


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 541
                      PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-10: SPIxSTATUS: SPI STATUS REGISTER
  R/C/HS-0/0          U-0           R-1/1           U-0       R/C/HS-0/0        S-0/0          U-0            R-0/0
    TXWE              —             TXBE             —           RXRE          CLRBF               —         RXBF
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’
                                                              C = Clearable bit
                                                              S = Settable bit
                                                              HS = Bit can be set by hardware


bit 7            TXWE: Transmit Buffer Write Error bit
                 1 = SPIxTxB was written while TxFIFO was full
                 0 = No error has occurred
bit 6            Unimplemented: Read as ‘0’
bit 5            TXBE: Transmit Buffer Empty bit (read-only)
                 1 = Transmit buffer TxFIFO is empty
                 0 = Transmit buffer is not empty
bit 4            Unimplemented: Read as ‘0’
bit 3            RXRE: Receive Buffer Read Error bit
                 1 = SPIxRB was read while RxFIFO was empty
                 0 = No error has occurred
bit 2            CLRBF: Clear Buffer Control bit (write-only)
                 1 = Reset the receive and transmit buffers, making both buffers empty
                 0 = Take no action
bit 1            Unimplemented: Read as ‘0’
bit 0            RXBF: Receive Buffer Full bit (read-only)
                 1 = Receive buffer is full
                 0 = Receive buffer is not full

REGISTER 32-11: SPIxRxB: SPI READ BUFFER REGISTER
        R-0           R-0               R-0         R-0           R-0           R-0            R-0             R-0
     RXB7           RXB6            RXB5            RXB4         RXB3          RXB2           RXB1            RXB0
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7-0          RXB[7:0]: Receiver Buffer bits (read-only)
                 If RX buffer is not empty:
                 Contains the top-most byte of RXFIFO, and reading this register will remove the top-most byte
                 RXFIFO and decrease the occupancy of the RXFIFO
                 If RX buffer is empty:
                 Reading this register will read as ‘0’, leave the occupancy unchanged, and set the RXRE bit of
                 SPIxSTATUS


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 542
                      PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 32-12: SPIxTxB: SPI TRANSMIT BUFFER REGISTER
        W-0          W-0                W-0         W-0            W-0           W-0             W-0             W-0
        TXB7         TXB6             TXB5          TXB4          TXB3           TXB2            TXB1           TXB0
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7-0          TXB[7:0]: Transmit Buffer bits (write only)
                 If TXFIFO is not full:
                 Writing to this register adds the data to the top of the TXFIFO and increases the occupancy of the
                 TXFIFO write pointer
                 If TXFIFO is full:
                 Writing to this register does not affect the data in the TXFIFO or the write pointer, and the TXWE bit of
                 SPIxSTATUS will be set

REGISTER 32-13: SPIxCLK: SPI CLOCK SELECTION REGISTER
        U-0           U-0               U-0         U-0          R/W-0/0       R/W-0/0         R/W-0/0        R/W-0/0
         —             —                  —          —          CLKSEL3       CLKSEL2         CLKSEL1         CLKSEL0
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’


bit 7-4          Unimplemented: Read as ‘0’
bit 3-0          CLKSEL[3:0]: SPI Clock Source Selection bits
                 1111-1001 = Reserved
                 1000 = SMT_match
                 0111 = TMR6_Postscaled
                 0110 = TMR4_Postscaled
                 0101 = TMR2_Postscaled
                 0100 = TMR0_overflow
                 0011 = CLKREF
                 0010 = MFINTOSC
                 0001 = HFINTOSC
                 0000 = FOSC


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 543
                           PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 32-3:         SUMMARY OF REGISTERS ASSOCIATED WITH SPI
                                                                                                                Register on
    Name           Bit 7         Bit 6      Bit 5        Bit 4        Bit 3         Bit 2    Bit 1     Bit 0
                                                                                                                   page

SPIxINTF          SRMTIF        TCZIF      SOSIF        EOSIF          —           RXOIF     TXUIF      —          537
SPIxINTE          SRMTIE        TCZIE      SOSIE        EOSIE          —           RXOIE     TXUIE      —          538
SPIxTCNTH            —            —          —            —            —          TCNT10    TCNT9     TCNT8        539
SPIxTCNTL         TCNT7        TCNT6       TCNT5        TCNT4        TCNT3         TCNT2    TCNT1     TCNT0        538
SPIxTWIDTH           —            —          —            —            —         TWIDTH2    TWIDTH1   TWITDH0      539
SPIxBAUD          BAUD7        BAUD6       BAUD5        BAUD4        BAUD3         BAUD2    BAUD1     BAUD0        540
SPIxCON0            EN            —          —            —            —            LSBF     MST      BMODE        540
SPIxCON1           SMP           CKE        CKP          FST           —            SSP      SDIP      SDOP        541
SPIxCON2           BUSY         SSFLT        —            —            —           SSET      TXR       RXR         542
SPIxSTATUS         TXWE           —         TXBE          —           RXRE         CLRBF      —        RXBF        543
SPIxRXB            RXB7         RXB6        RXB5        RXB4          RXB3         RXB2      RXB1      RXB0        543
SPIxTXB            TXB7         TXB6        TXB5         TXB4         TXB3          TXB2     TXB1      TXB0        544
SPIxCLK              —            —          —            —         CLKSEL3       CLKSEL2   CLKSEL1   CLKSEL0      544
Legend:      — = unimplemented, read as ‘0’. Shaded cells are unused by the SPI module.


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 544
