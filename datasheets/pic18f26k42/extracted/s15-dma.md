                      PIC18(L)F26/27/45/46/47/55/56/57K42
15.0     DIRECT MEMORY ACCESS                              15.2    DMA Registers
         (DMA)                                             The operation of the DMA module has the following
                                                           registers:
15.1     Introduction                                      • Control registers (DMAxCON0, DMAxCON1)
The Direct Memory Access (DMA) module is designed          • Data buffer register (DMAxBUF)
to service data transfers between different memory         • Source Start Address Register (DMAxSSAU:H:L)
regions directly without intervention from the CPU. By     • Source Pointer Register (DMAxSPTRU:H:L)
eliminating the need for CPU-intensive management of
                                                           • Source Message Size Register (DMAxSSZH:L)
handling interrupts intended for data transfers, the CPU
now can spend more time on other tasks.                    • Source Count Register (DMAxSCNTH:L)
                                                           • Destination Start Address Register
PIC18(L)F26/27/45/46/47/55/56/57K42 family has two
                                                             (DMAxDSAH:L)
DMA modules which can be independently
programmed to transfer data between different              • Destination Pointer Register (DMAxDPTRH:L)
memory locations, move different data sizes, and use a     • Destination Message Size Register
wide range of hardware triggers to initiate transfers.       (DMAxDSZH:L)
The two DMA registers can even be programmed to            • Destination Count Register (DMAxDCNTH:L)
work together, in order to carry out more complex data     • Start Interrupt Request Source Register
transfers without CPU overhead.                              (DMAxSIRQ)
Key features of the DMA module include:                    • Abort Interrupt Request Source Register
• Support access to the following memory regions:            (DMAxAIRQ)
  - GPR and SFR space (R/W)                                These registers are detailed in Section 15.13 “Regis-
  - Program Flash Memory (R only)                          ter definitions: DMA”.
  - Data EEPROM Memory (R only)
• Programmable priority between the DMA and
  CPU Operations. Refer to Section 3.1 “System
  Arbitration” for details.
• Programmable Source and Destination address
  modes
  - Fixed address
  - Post-increment address
  - Post-decrement address
• Programmable Source and Destination sizes
• Source and destination pointer register,
  dynamically updated and reloadable
• Source and destination count register,
  dynamically updated and reloadable
• Programmable auto-stop based on Source or
  Destination counter
• Software triggered transfers
• Multiple user selectable sources for hardware
  triggered transfers
• Multiple user selectable sources for aborting DMA
  transfers


 2017-2021 Microchip Technology Inc.                                                    DS40001919G-page 228
                      PIC18(L)F26/27/45/46/47/55/56/57K42
15.3     DMA Organization
The DMA module on the K42 family of devices is
designed to move data by using the existing Instruction
Bus[16] and Data Bus[8] without the need for any dual-
porting of memory or peripheral systems (Figure 15-1).
The DMA accesses the required bus when it has been
granted to by the System Arbiter.

FIGURE 15-1:           DMA FUNCTIONAL BLOCK DIAGRAM
                                                                                                                 Rev. 10-000 274A
                                                                                                                       11/11/201 6


                                                  Configure DMA
                                                     Module


                                                      EN = 1


                                                   DMA Source/
                                                Destination Pointers/
                                                Counters are loaded


                                                   SIRQEN = 1 &          N
                                                      Trigger?

                                                                Y

                                                     DGO = 1

                                                       Y


                                                                         N
                                                      Bubble?


                                                       Y
                                                                                                DMAxBUF = &DMAxSPTR
                                                   Source Read
                                                                                                XIP = 1


                                                                         N
                                                      Bubble?


                                                           Y
                                                                                                &DMAxDPTR = DMABUF
                                                 Destination Write
                                                                                                XIP = 0


                                                                     Y         Reload
                                                                                          DMAxSCNTIF
                                                  DMAxSCNT = 0               DMAxSCNT &                    DGO = 0
                                                                                             =1
                                                                              DMAxSPTR

                                                               N
                                                      Update                                           Y
                                                     DMAxSSA,                             SIRQEN = 0       SSTP = 1
                                                     DMAxSCNT

                                                                                                                 N


                                                                     Y         Reload
                                                                                          DMAxDCNTIF
                                                  DMAxDCNT = 0               DMAxDCNT &                    DGO = 0
                                                                                             =1
                                                                              DMAxDPTR

                                                            N
                                                                                                       Y
                                                      Update                              AIRQEN = 0       DSTP = 1
                                                     DMAxDSA,
                                                     DMAxDCNT
                                                                                                                 N


                                            N
                                                     DGO = 0


                                                      Y

                                                    End Process


 2017-2021 Microchip Technology Inc.                                                                                                DS40001919G-page 229
                      PIC18(L)F26/27/45/46/47/55/56/57K42
Depending on the priority of the DMA with respect to
CPU execution (Refer to Section 3.2 “Memory                 TABLE 15-1:         DMA MEMORY ACCESS
Access Scheme” for more information), the DMA
Controller can move data through two methods:                     Read Source              Write Destination

• Stalling the CPU execution until it has completed          Program Flash Memory                 GPR
  its transfers (DMA has higher priority over the            Program Flash Memory                 SFR
  CPU in this mode of operation)                                      Data EE                    GPR
• Utilizing unused CPU cycles for DMA transfers
  (CPU has higher priority over the DMA in this                       Data EE                     SFR
  mode of operation). Unused CPU cycles are                            GPR                        GPR
  referred to as bubbles which are instruction cycles                  SFR                       GPR
  available for use by the DMA to perform read and
                                                                       GPR                        SFR
  write operations. In this way, the effective
  bandwidth for handling data is increased; at the                     SFR                        SFR
  same time, DMA operations can proceed without
  causing a processor stall.
                                                              Note:     Even though the DMA module has access
                                                                        to all memory and peripherals that are
15.4      DMA Interface
                                                                        also available to the CPU, it is
The DMA module transfers data from the source to the                    recommended that the DMA does not
destination one byte at a time, this smallest data                      access any register that is part of the
movement is called a DMA data transaction. A DMA                        System arbitration. The DMA, as a system
Message refers to one or more DMA data transactions.                    arbitration client may not be read or
                                                                        written by itself or by another DMA
Each DMA data transaction consists of two separate
                                                                        instantiation.
actions:
• Reading the Source Address Memory and storing             The following sections discuss the various control
  the value in the DMA Buffer register                      interfaces required for DMA data transfers.
• Writing the contents of the DMA Buffer register to
                                                            15.4.1      DMA ADDRESSING
  the Destination Address Memory
                                                            The start addresses for the source read and destination
  Note:     DMA data movement is a two-cycle
                                                            write operations are set using the DMAxSSA [21:0] and
            operation.
                                                            DMAxDSA [15:0] registers, respectively.
The XIP bit (DMAxCON0 register) is a status bit to          When the DMA Message transfers are in progress, the
indicate whether or not the data in the DMAxBUF             DMAxSPTR [21:0] and DMAxDPTR [15:0] registers
register has been written to the destination address. If    contain the current address pointers for each source
the bit is set then data is waiting to be written to the    read and destination write operation, these registers
destination. If clear, it means that either data has been   are modified after each transaction based on the
written to the destination or that no source read has       Address mode selection bits.
occurred.
                                                            The SMODE and DMODE bits in the DMAxCON1
The DMA has read access to PFM, Data EEPROM,                control register determine the address modes of
and SFR/GPR space, and write access to SFR/GPR              operation by controlling how the DMAxSPTR [21:0] and
space. Based on these memory access capabilities,           DMAxDPTR [15:0] bits are updated after every DMA
the DMA can support the following memory                    data transaction combination (Figure 15-2).
transactions:
                                                            Each address can be separately configured to:
                                                            • Remain unchanged
                                                            • Increment by 1
                                                            • Decrement by 1


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 230
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 15-2:           DMA POINTERS BLOCK DIAGRAM
                                                                                        Rev. 10-000272A
                                                                                               3/15/2018


                          DMAxSSA[21:0]                              DMAxDSA[15:0]


                         DMAxSPTR[21:0]                              DMAxDPTR[15:0]


             +1                                           +1
              0                                            0
             -1                                           -1

                  SMODE<1:0>                                   DMODE<1:0>


The DMA can initiate data transfers from the PFM, Data
EEPROM or SFR/GPR Space. The SMR[1:0] bits in the
DMAxCON1 register are used to select the type of
memory being pointed to by the Source Address
Pointer. The SMR[1.0] bits are required because the
PFM and SFR/GPR spaces have overlapping
addresses that do not allow the specified address to
uniquely define the memory location to be accessed.
   Note 1: For proper memory read access to occur,
           the combination of address and space
           selection must be valid.
         2: The destination does not have space
            selection bits because it can only write to
            the SFR/GPR space.


 2017-2021 Microchip Technology Inc.                                           DS40001919G-page 231
                       PIC18(L)F26/27/45/46/47/55/56/57K42
15.4.2      DMA MESSAGE SIZE/COUNTERS
A transaction is the transfer of one byte. A message
consists of one or more transactions. A complete DMA
process consists of one or more messages. The size
registers determine how many transactions are in a
message. The DMAxSSZ registers determine the
source size and DMAxDSZ registers determine the
destination size.
When a DMA transfer is initiated, the size registers are
copied to corresponding counter registers that control
the duration of the message. The DMAxSCNT registers
count the source transactions and the DMAxDCNT
registers count the destination transactions. Both are
simultaneously decremented by one after each
transaction.
A message is started by setting the DGO bit of the
DMAxCON0 register and terminates when the smaller
of the two counters reaches zero.
When either counter reaches zero the DGO bit is
cleared and the counter and pointer registers are
immediately reloaded with the corresponding size and
address data. If the other counter did not reach zero
then the next message will continue with the count and
address corresponding to that register.
When the source and destination size registers are not
equal, then the ratio of the largest to the smallest size
determines how many messages are in the DMA
process. For example, when the destination size is 6
and the source size is 2, then each message will
consist of two transactions and the complete DMA
process will consist of three messages. When the
larger size is not an even integer of the smaller size,
then the last message in the process will terminate
early when the larger count reaches zero. In that case,
the larger counter will reset and the smaller counter will
have a remainder skewing any subsequent messages
by that amount.
  Note:     Reading the DMAxSCNT or DMAxDCNT
            registers will never return zero. When
            either register is decremented from ‘1’ it is
            immediately        reloaded   from      the
            corresponding size register.


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 232
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 15-3:           DMA COUNTERS BLOCK DIAGRAM
                                                                                                    Rev. 10-000273A
                                                                                                            8/8/2016


                                   DMAxSSIZ[11:0]                                  DMAxDSIZ[11:0]


                                   DMAxSCNT[11:0]                                  DMAxDCNT[11:0]


                               1                                               1


Table 15-2 has a few examples of configuring DMA
Message sizes.

TABLE 15-2:       EXAMPLE MESSAGE SIZE TABLE
         Operation                    Example       SCNT   DCNT                     Comments
Read from single SFR                                              N equals the number of bytes desired in the
                             U1RXB                   1      N
location to RAM                                                   destination buffer. N >= 1.
Write to single SFR location                                      N equals the number of bytes desired in the
                             U1TXB                   N      1
from RAM                                                          source buffer. N >= 1.
                                                                  N equals the number of ADC results to be
                               ADRES[H:L]            2     2*N
                                                                  stored in memory. N>= 1
Read from multiple SFR                                            N equals the number of TMR1 Acquisition
                               TMR1[H:L]             2     2*N
location                                                          results to be stored in memory. N>= 1
                                                                  N equals the number of Capture Pulse Width
                               SMT1CPR[U:H:L]        3     3*N
                                                                  measurements to be stored in memory. N>= 1
                                                                  N equals the number of PWM duty cycle val-
                               PWMDC[H:L]           2*N     2
Write to Multiple SFR regis-                                      ues to be loaded from a memory table. N>= 1
ters                                                              Using the DMA to transfer a complete ADC
                               All ADC registers    N*31    31
                                                                  context from RAM to the ADC registers.N>= 1


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 233
                      PIC18(L)F26/27/45/46/47/55/56/57K42
15.5     DMA Message Transfers
Once the Enable bit is set to start DMA message
transfers, the Source/Destination pointer and counter
registers are initialized to the conditions shown in
Table 15-3.
TABLE 15-3:       DMA INITIAL CONDITIONS
                        Register                                                 Value loaded
                   DMAxSPTR[21:0]                                              DMAxSSA[21:0]
                   DMAxSCNT[11:0]                                               DMAxSSZ[11:0]
                   DMAxDPTR[15:0]                                              DMAxDSA[15:0]
                   DMAxDCNT[11:0]                                              DMAxDSZ[11:0]
During the DMA Operation after each transaction,
Table 15-4 and Table 15-5 indicate how the Source/
Destination pointer and counter registers are modified.

TABLE 15-4:       DMA SOURCE POINTER/COUNTER DURING OPERATION
                Register                                    Modified Source Counter/Pointer Value
         DMAxSCNT[11:0] != 1                                     DMAxSCNT = DMAxSCNT -1
                                                           SMODE = 00: DMAxSPTR = DMAxSPTR
                                                          SMODE = 01: DMAxSPTR = DMAxSPTR + 1
                                                          SMODE = 10: DMAxSPTR = DMAxSPTR - 1
         DMAxSCNT[11:0] == 1                                       DMAxSCNT = DMAxSSZ
                                                                   DMAxSPTR = DMAxSSA


TABLE 15-5:       DMA DESTINATION POINTER/COUNTER DURING OPERATION
                Register                                  Modified Destination Counter/Pointer Value
         DMAxDCNT[11:0]!= 1                                      DMAxDCNT = DMAxDCNT -1
                                                           DMODE = 00: DMAxDPTR = DMAxDPTR
                                                          DMODE = 01: DMAxDPTR = DMAxDPTR + 1
                                                          DMODE = 10: DMAxDPTR = DMAxDPTR - 1
         DMAxDCNT[11:0] == 1                                       DMAxDCNT = DMAxDSZ
                                                                   DMAxDPTR = DMAxDSA
The following sections discuss how to initiate and               15.5.1.1     User Software Control
terminate DMA transfers.
                                                                 Software starts or stops DMA transaction by setting/
                                                                 clearing the DGO bit. The DGO bit is also used to
15.5.1      STARTING DMA MESSAGE
                                                                 indicate whether a DMA hardware trigger has been
            TRANSFERS
                                                                 received and a message is in progress.
The DMA can initiate data transactions by either of the
following two conditions:                                          Note 1: Software start can only occur if the EN bit
                                                                           (DMAxCON0) is set.
1.   User software control
                                                                         2: If the CPU writes to the DGO bit while it is
2.   Hardware trigger, SIRQ
                                                                            already set, there is no effect on the
                                                                            system, the DMA will continue to operate
                                                                            normally.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 234
                        PIC18(L)F26/27/45/46/47/55/56/57K42
15.5.1.2      Hardware Trigger, SIRQ                           15.5.2.3      Source Count Reload
A Hardware trigger is an interrupt request from another        A DMA message is considered to be complete when
module sent to the DMA with the purpose of starting a          the Source count register is decremented from 1 and
DMA message. The DMA start trigger source is user              then reloaded (i.e., once the last byte from either the
selectable using the DMAxSIRQ register.                        source read or destination write has occurred). When
The SIRQEN bit (DMAxCON0 register) is used to                  the SSTP bit is set (DMAxCON1 register) and the
enable sampling of external interrupt triggers by which        source count register is reloaded, then further message
a DMA transfer can be started. When set, the DMA will          transfer is stopped.
sample the selected Interrupt source and when
                                                               15.5.2.4      Destination Count Reload
cleared, the DMA will ignore the selected Interrupt
source. Clearing SIRQEN does not stop a DMA                    A DMA message is considered to be complete when
transaction currently in progress, it only stops more          the Destination count register is decremented from 1
hardware request signals from being received.                  and then reloaded (i.e., once the last byte from either
                                                               the source read or destination write has occurred).
15.5.2      STOPPING DMA MESSAGE                               When the DSTP bit is set (DMAxCON1) and the
            TRANSFERS                                          destination count register is reloaded then further
                                                               message transfer is stopped.
The DMA controller can stop data transactions by
either of the following two conditions:                             Note:   Reading the DMAxSCNT or DMAxDCNT
1.   Clearing the DGO bit                                                   registers will never return zero. When
                                                                            either register is decremented from ‘1’ it is
2.   Hardware trigger, AIRQ
                                                                            immediately        reloaded   from      the
3.   Source Count reload                                                    corresponding size register.
4.   Destination Count reload
5.   Clearing the Enable bit                                   15.5.2.5      Clearing the Enable bit
                                                               If the User clears the EN bit, the message will be
15.5.2.1      User Software Control
                                                               stopped and the DMA will return to its default
If the user clears the DGO bit, the message will be            configuration. This is also referred to as a hard-stop as
stopped and the DMA will remain in the current                 the DMA cannot resume operation from where it was
configuration.                                                 stopped.
For example, if the user clears the DGO bit after source            Note:   After the DMA message transfer is
data has been read but before it is written to the                          stopped, it requires an extra instruction
destination, then the data in DMAxBUF will not reach its                    cycle before the Stop condition takes
destination.                                                                effect. Thus, after the Stop condition has
This is also referred to as a soft-stop as the operation                    occurred, a Source read or a Destination
can resume if desired by setting DGO bit again.                             write can occur depending on the Source
                                                                            or Destination Bus availability.
15.5.2.2      Hardware Trigger, AIRQ
The AIRQEN bit (DMAxCON0 register) is used to                  15.5.3       DISABLE DMA MESSAGES
enable sampling of external interrupt triggers by which                     TRANSFERS UPON COMPLETION
a DMA transaction can be aborted.                              Once the DMA message is complete it may be
Once an Abort interrupt request has been received, the         desirable to disable the trigger source to prevent
DMA will perform a soft-stop by clearing the DGO bit as        overrun or under run of data. This can be done by either
well as clearing the SIRQEN bit so overruns do not             of the following methods:
occur. The AIRQEN bit is also cleared to prevent               1.    Clearing the SIRQEN bit
additional abort signals from triggering false aborts.
                                                               2.    Setting the SSTP bit
If desired, the DGO bit can be set again and the DMA           3.    Setting the DSTP bit
will resume operation from where it left off after the soft-
stop had occurred as none of the DMA state
information is changed in the event of an abort.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 235
                      PIC18(L)F26/27/45/46/47/55/56/57K42
15.5.3.1      Clearing the SIRQEN bit                       15.7     Types of Data Transfers
Clearing the SIRQEN bit (DMAxCON1 register) stops           Based on the memory access capabilities of the DMA
the sampling of external start interrupt triggers, hence    (See Table 15-1), the following sections discuss the
preventing further DMA Message transfers.                   different types of data movement between the Source
An example would be a communications peripheral             and Destination Memory regions.
with a level-triggered interrupt. The peripheral will       • N: 1
continue to request data (because its buffer is empty)
even though there is no more data to be moved.              This type of transfer is common when sending
Disabling the SIRQEN bit prevents the DMA from              predefined data packets (such as strings) through a
processing these requests.                                  single interface point (such as communications
                                                            modules transmit registers).
15.5.3.2      Source/Destination Stop                       • N: N
The SSTP and DSTP bits (DMAxCON0 register)                  This type of transfer is useful for moving information out
determine whether or not to disable the hardware            of the Program Flash or Data EEPROM to SRAM for
triggers (SIRQEN = 0) once a DMA message has                manipulation by the CPU or other peripherals.
completed.
                                                            • 1: N
When the SSTP bit is set and the DMAxSCNT = 0, then
                                                            This type of transfer is common when bridging two
the SIRQEN bit will be cleared. Similarly, when the
                                                            different  modules       data  streams   together
DSTP bit is set and the DMAxDCNT = 0, the SIRQEN
                                                            (communications bridge).
bit will be cleared.
                                                            • 1: N
  Note:     The SSTP and DSTP bits are
            independent functions and do not depend         This type of transfer is useful for moving information
            on each other. It is possible for a message     from a single data source into a memory buffer
            to be stopped by either counter at              (communications receive registers).
            message end or both counters at
            message end.                                    15.8     DMA Interrupts
                                                            Each DMA has its own set of four interrupt flags, used
15.6       Types of Hardware Triggers                       to indicate a range of conditions during data transfers.
                                                            The interrupt flag bits can be accessed using the
The DMA has two different trigger inputs namely the
                                                            corresponding PIR registers (Refer to the Interrupt
Source trigger and the abort trigger. Each of these
                                                            Section).
trigger sources is user configurable using the
DMAxSIRQ and DMAxAIRQ registers.                            15.8.1      DMA SOURCE COUNT INTERRUPT
Based on the source selected for each trigger, there        The DMAxSCNTIF source count interrupt flag is set
are two types of requests that can be sent to the DMA.      every time the DMAxSCNT[11:0] reaches zero and is
• Edge triggers                                             reloaded to its starting value.
• Level triggers
                                                            15.8.2      DMA DESTINATION COUNT
15.6.1      EDGE TRIGGER REQUESTS                                       INTERRUPT
Edge triggers are generated by the signal that sets the     The DMAxDCNTIF destination count interrupt flag is
corresponding interrupt flag. The DMA responds to this      set every time the DMAxDCNT[11:0] reaches zero and
event but leaves the interrupt flag set. An Edge request    is reloaded to its starting value.
occurs only once when a given module interrupt              The DMA Source Count zero and Destination Count
requirements are true.                                      zero interrupts are used in conjunction to determine
                                                            when to signal the CPU when the DMA Messages are
15.6.2      LEVEL TRIGGER REQUESTS                          completed.
A level request is asserted as long as the condition that
causes the interrupt is true. For example, the RXIF         15.8.3      ABORT INTERRUPT
interrupt is asserted as long as the UART receive buffer    The DMAxAIF abort interrupt flag is used to signal that
has unread data. The RXIF cannot be cleared except          the DMA has halted activity due to an abort signal from
by emptying the receive buffer.                             one of the abort sources. This is used to indicate that
                                                            the transaction has been halted for some reason.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 236
                      PIC18(L)F26/27/45/46/47/55/56/57K42
15.8.4      OVERRUN INTERRUPT                              15.9     DMA Setup and Operation
When the DMA receives a trigger to start a new             The following steps illustrate how to configure the DMA
message before the current message is completed,           for data transfer:
then the DMAxORIF Overrun interrupt flag is set.
                                                           1.   Program the appropriate Source and
This condition indicates that the DMA is being                  Destination addresses for the transaction into
requested before its current transaction is finished.           the DMAxSSA and DMAxDSA registers
This implies that the active DMA may not be able to
                                                           2.   Select the source memory region that is being
keep up with the demands from the peripheral module
                                                                addressed by DMAxSSA register, using the
being serviced, which may result in data loss.
                                                                SMR[1:0] bits.
The DMAxORIF flag being set does not cause the             3.   Program the SMODE and DMODE bits to select
current DMA transfer to terminate.                              the addressing mode.
The Overrun interrupt is only available for trigger        4.   Program the Source size DMAxSSZ and
sources that are edge based and not available for               Destination size DMAxDSZ registers with the
sources that are level-based. Therefore a level-based           number of bytes to be transferred. It is
interrupt source does not trigger a DMA overrun error           recommended for proper operation that the size
due to the potential latency issues in the system.              registers be a multiple of each other.
An example of an interrupt that could use the overrun      5.   If the user desires to disable data transfers once
interrupt would be a timer overflow (or period match)           the message has completed, then the SSTP and
interrupt. This event only happens every time the timer         DSTP bits in DMAxCON1 register need to be
rolls over and is not dependent on any other system             set. (see Section 15.5.3.2 “Source/Destina-
conditions.                                                     tion Stop”).
An example of an interrupt that does not allow the         6.   If using hardware triggers for data transfer,
overrun interrupt would be the UARTTX buffer. The               setup the hardware trigger interrupt sources for
UART will continue to assert the interrupt until the DMA        the starting and aborting DMA transfers
is able to process the MSG. Due to latency issues, the          (DMAxSIRQ and DMAxAIRQ), and set the
DMA may not be able to service an empty buffer                  corresponding interrupt request enable bits
immediately, but the UART continues to assert its               (SIRQEN and AIRQEN).
transmit interrupt until it is serviced. If overrun was    7.   Select the priority level for the DMA (see
allowed in this case, the overrun would occur almost            Section 3.1 “System Arbitration”) and lock
immediately as the module samples the interrupt                 the priorities (see Section 3.1.1 “Priority
sources every instruction cycle.                                Lock”)
                                                           8.   Enable the DMA (DMAxCON1bits. EN = 1)
                                                           9.   If using software control for data transfer, set the
                                                                DGO bit, else this bit will be set by the hardware
                                                                trigger.
                                                           Once the DMA is set up, the following flow chart
                                                           describes the sequence of operation when the DMA
                                                           uses hardware triggers and utilizes the unused CPU
                                                           cycles (bubble) for DMA transfers.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 237
                      PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 15-4:           DMA OPERATION WITH HARDWARE TRIGGER
                                                                                                                Rev. 10-000274A
                                                                                                                        8/8/2016


                                              Configure DMA
                                                 Module


                                                  EN = 1


                                            Load DMA Source/
                                            Destination Pointers
                                                & Counters


                                              SIRQEN = 1 &             N
                                                 Trigger?

                                                            Y

                                                 DGO = 1


                                                  Bubble?


                                                                                              DMAxBUF = &DMAxSPTR
                                               Source Read
                                                                                              XIP = 1


                                                                       N
                                                  Bubble?


                                                            Y
                                                                                              &DMAxDPTR = DMABUF
                                             Destination Write
                                                                                              XIP = 0


                                                                   Y         Reload
                                                                                        DMAxSCNTIF
                                             DMAxSCNT = 0                  DMAxSCNT &                      DGO = 0
                                                                                           =1
                                                                            DMAxSPTR

                                                        N
                                                 Update                                              Y
                                                DMAxSSA,                                SIRQEN = 0        SSTP = 1
                                                DMAxSCNT

                                                                                                                N


                                                                   Y         Reload
                                                                                        DMAxDCNTIF
                                             DMAxDCNT = 0                  DMAxDCNT &                      DGO = 0
                                                                                           =1
                                                                            DMAxDPTR

                                                       N

                                                                                                     Y
                                                 Update                                 AIRQEN = 0        DSTP = 1
                                                DMAxDSA,
                                                DMAxDCNT
                                                                                                                N


                                        N
                                                 DGO = 0


                                                  Y


                                               End Process


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 238
                          PIC18(L)F26/27/45/46/47/55/56/57K42
The following sections describe with visual reference
the sequence of events for different configurations of
the DMA module

15.9.1        SOURCE STOP
When the Source Stop bit is set (SSTP = 1) and the
DMAxSCNT register reloads, the DMA clears the
SIRQEN bit to stop receiving new start interrupt
request signals and sets the DMAxSCNTIF flag.

FIGURE 15-5:                  GPR-GPR TRANSACTIONS WITH HARDWARE TRIGGERS, SSTP = 1
                                                                                                                                                        Rev. 10-000275A
                                                                                                                                                                8/9/2016

                          1     2      3         4      5     6           7     8     9        10    11    12     13       14   15    16   17      18   19

            Instruction
              Clock

                    EN

              SIRQEN

     Source Hardware
         Trigger

                  DGO

          DMAxSPTR                     0x100                      0x101                      0x102                 0x103                   0x100

          DMAxDPTR                     0x200                      0x201                      0x201                 0x201                   0x200

          DMAxSCNT                     4                            3                           2                      1                   4

          DMAxDCNT                     2                            1                           2                      1                   2


          DMA STATE             IDLE             SR(1) DW(2) SR(1) DW(2)              IDLE           SR(1) DW(2) SR(1) DW(2)               IDLE


         DMAxSCNTIF


       DMAxDCNTIF


                          DMAxSSA      0x100                DMAxDSA           0x200

                          DMAxSSZ          0x4              DMAxDSZ            0x2


          Note 1: SR - Source Read
                 2: DW - Destination Write


 2017-2021 Microchip Technology Inc.                                                                                                DS40001919G-page 239
                          PIC18(L)F26/27/45/46/47/55/56/57K42
15.9.2       DESTINATION STOP
When the Destination Stop bit is set (DSTP = 1) and the
DMAxDCNT register reloads, the DMA clears the
SIRQEN bit to stop receiving new start interrupt
request signals and sets the DMAxDCNTIF flag.

FIGURE 15-6:                  GPR-GPR TRANSACTIONS WITH HARDWARE TRIGGERS, DSTP = 1
                                                                                                                                                                                                Rev. 10-000275B
                                                                                                                                                                                                        8/9/2016

                          1     2      3         4          5           6             7           8     9        10    11         12         13             14         15   16      17     18   19

            Instruction
              Clock

                    EN

              SIRQEN

      Source Hardware
          Trigger

                  DGO

          DMAxSPTR                     0x100                                0x101                              0x100                          0x101                                0x100

          DMAxDPTR                     0x200                                0x201                              0x202                          0x203                                0x200

          DMAxSCNT                     2                                          1                               2                                     1                           2

          DMAxDCNT                     4                                          3                               2                                     1                           4

                                                      (1)       (2)         (1)           (2)                               (1)        (2)        (1)            (2)
          DMA STATE             IDLE             SR         DW         SR         DW                    IDLE           SR         DW         SR             DW                     IDLE


         DMAxSCNTIF


         DMAxDCNTIF


                          DMAxSSA      0x100                      DMAxDSA                       0x200

                          DMAxSSZ          0x2                        DMAxDSZ                    0x4


      Note 1: SR - Source Read
              2: DW - Destination Write


 2017-2021 Microchip Technology Inc.                                                                                                                                            DS40001919G-page 240
                                  PIC18(L)F26/27/45/46/47/55/56/57K42
15.9.3            CONTINUOUS TRANSFER
When the Source or the Destination stop bit is cleared
(SSTP, DSTP = 0), the transactions continue unless
cleared by the user. The DMAxSCNTIF and
DMAxDCNTIF flags are set whenever the respective
counter registers are reloaded.

FIGURE 15-7:                      GPR-GPR TRANSACTIONS WITH HARDWARE TRIGGERS, SSTP, DSTP = 0
                                                                                                                                                                                                                                 Rev. 10-000275D
                                                                                                                                                                                                                                        9/15/2016

                   1   2      3    4         5          6       7    8   9      10    11    12    13       14    15    16    17     18   19    20       21   22   23     24   25    26     27       28   29   30       31   32

    Instruction
      Clock


            EN

     SIRQEN
      Source
     Hardware
      Trigger
         DGO

    DMAxSPTR               0x100                        0x101                0x100                 0x101                    0x100              0x101                0x100                  0x101              0x100

    DMAxDPTR               0x200                        0x201                0x202                 0x203                    0x200              0x201                0x202                  0x203              0x202

    DMAxSCNT                  2                             1                    2                     1                     2                      1                    2                      1                  2

    DMAxDCNT                  4                             3                    2                     1                     4                      3                    2                      1                  2
      DMA                              (1)       (2)
                       IDLE        SR DW               SR(1) DW(2)       IDLE         SR(1) DW(2) SR(1) DW(2)         IDLE        SR(1) DW(2) SR(1) DW(2)         IDLE        SR(1) DW(2) SR(1) DW(2)         IDLE
     STATE


  DMAxSCNTIF


  DMAxDCNTIF


                           DMAxSSA                      0x100                        DMAxDSA           0x200

                           DMAxSSZ                          0x2                      DMAxDSZ               0x4


     Note 1: SR - Source Read
               2: DW - Destination Write


 2017-2021 Microchip Technology Inc.                                                                                                                                                               DS40001919G-page 241
                             PIC18(L)F26/27/45/46/47/55/56/57K42
15.9.4        TRANSFER FROM SFR TO GPR                                                                      Hardware trigger, the Source address can be set to
                                                                                                            point to the ADC Result registers at 3EEF, the
The following visual reference describes the sequence
                                                                                                            Destination address can be set to point to any GPR
of events when copying ADC results to a GPR location.
                                                                                                            location of our choice (Example 0x100).
The ADC Interrupt Flag can be chosen as the Source

FIGURE 15-8:                 SFR SPACE TO GPR SPACE TRANSFER
                                                                                                                                                                                                 Rev. 10-000275C
                                                                                                                                                                                                        8/12/2016

                       1      2       3         4          5           6             7           8      N       N+1         N+2         N+3             N+4         N+5    N+6     N+7     N+x

         Instruction
           Clock

                 EN

           SIRQEN

   Source Hardware
       Trigger

               DGO

       DMAxSPTR                      0x3EEF                            0x3EF0                          0x3EEF                             0x3EF0                          0x3EEF

       DMAxDPTR                      0x100                                 0x101                       0x102                                  0x103                       0x103

       DMAxSCNT                       2                                          1                       2                                          1                        2

       DMAxDCNT                      10                                          9                       8                                          7                        6

                                                     (1)       (2)         (1)           (2)                          (1)         (2)         (1)             (2)
      DMA STATE               IDLE              SR         DW         SR         DW                    IDLE      SR         DW          SR              DW                 IDLE

     DMAxSCNTIF


     DMAxDCNTIF


                       DMAxSSA       0x3EEF                      DMAxDSA                       0x100

                       DMAxSSZ            0x2                        DMAxDSZ                   0xA


                           SMODE          0x1                        DMODE                      0x1


       Note 1: SR - Source Read
               2: DW - Destination Write


 2017-2021 Microchip Technology Inc.                                                                                                                                             DS40001919G-page 242
                           PIC18(L)F26/27/45/46/47/55/56/57K42
15.9.5        OVERRUN INTERRUPT
The Overrun Interrupt flag is set if the DMA receives a
trigger to start a new message before the current
message is completed.

FIGURE 15-9:               OVERRUN INTERRUPT
                                                                                                                                                   Rev. 10-000275E
                                                                                                                                                          8/11/2016

                       1     2     3         4      5     6           7     8     9        10    11    12     13       14   15   16   17      18   19

         Instruction
           Clock

                 EN

           SIRQEN

   Source Hardware
       Trigger

               DGO

       DMAxSPTR                    0x100                      0x101                      0x100                 0x101                  0x100

       DMAxDPTR                    0x200                      0x201                      0x202                 0x203                  0x200

       DMAxSCNT                    2                            1                           2                      1                  2

       DMAxDCNT                    4                            3                           2                      1                  4

      DMA STATE             IDLE             SR(1) DW(2) SR(1) DW(2)              IDLE           SR(1) DW(2) SR(1) DW(2)              IDLE


    DMAxSCNTIF


    DMAxDCNTIF


       DMAxORIF


                       DMAxCON1bits.SMA = 01

                       DMAxSSA     0x100                DMAxDSA           0x200

                       DMAxSSZ         0x2              DMAxDSZ           0x20


         Note 1: SR - Source Read
                 2: DW - Destination Write


 2017-2021 Microchip Technology Inc.                                                                                            DS40001919G-page 243
                           PIC18(L)F26/27/45/46/47/55/56/57K42
15.9.6          ABORT TRIGGER, MESSAGE
                COMPLETE
The AIRQEN needs to be set in order for the DMA to
sample Abort Interrupt sources. When an abort
interrupt is received the SIRQEN bit is cleared and the
AIRQEN bit is cleared to avoid receiving further abort
triggers.

FIGURE 15-10:              ABORT AT THE END OF MESSAGE
                                                                                                                                                    Rev. 10-000275F
                                                                                                                                                           8/12/2016
                       1    2      3         4      5     6           7     8      N       N+1   N+2   N+3       N+4   N+5   N+6        N+7   N+8

         Instruction
           Clock

                 EN

           SIRQEN


           AIRQEN
  Source Hardware
      Trigger
  Abort Hardware
     Trigger

               DGO

      DMAxSPTR                    0x3EEF                   0x3EF0                 0x3EEF                 0x3EF0                    0x3EEF

      DMAxDPTR                    0x100                       0x101               0x109                   0x10A                    0x100

      DMAxSCNT                     2                            1                   2                        1                      2

      DMAxDCNT                    10                            9                   2                        1                     10

     DMA STATE             IDLE              SR(1) DW(2) SR(1) DW(2)              IDLE      SR(1) DW(2) SR(1) DW(2)                IDLE


   DMAxSCNTIF


   DMAxDCNTIF


       DMAxAIF
                       DMAxSSA    0x3EEF                DMAxDSA           0x100

                       DMAxSSZ         0x2              DMAxDSZ           0xA


      Note 1: SR - Source Read
                2: DW - Destination Write


 2017-2021 Microchip Technology Inc.                                                                                              DS40001919G-page 244
                             PIC18(L)F26/27/45/46/47/55/56/57K42
15.9.7      ABORT TRIGGER, MESSAGE IN                                                 The SIREQEN bit is cleared to prevent any overrun and
            PROGRESS                                                                  the AIRQEN bit is cleared to prevent any false aborts.
When an abort interrupt request is received in a DMA                                  When the DGO bit is set again the DMA will resume
transaction, the DMA will perform a soft-stop by                                      operation from where it left off after the soft-stop.
clearing the DGO (i.e., if the DMA was reading the
source register, it will complete the read operation and
then clear the DGO bit).

FIGURE 15-11:                  ABORT DURING MESSAGE TRANSFER

                                                                                                                                                 Rev. 10-000275G
                                                                                                                                                        8/12/2016
                                 1          2      3     4       5            6   7       8    9     10       10           11       12

               Instruction
                 Clock

                          EN

                  SIRQEN


                  AIRQEN
         Source Hardware
             Trigger
         Abort Hardware
            Trigger
                      DGO

             DMAxSPTR                                                0x3EEF                                        0x3EF0           0x3EEF

             DMAxDPTR                                                0x100                                         0x101             0x102

             DMAxSCNT                                                  2                                               1                 2

             DMAxDCNT                                                  10                                              9                 8

             DMA STATE                      IDLE         SR(1)                    IDLE                DW(2)    SR(1)       DW(2)     IDLE


         DMAxCONbits.XIP

               DMAxAIF


                   DMAxSSA           0x3EEF            DMAxDSA        0x100

                   DMAxSSZ            0x2              DMAxDSZ         0xA

         Note 1: SR - Source Read
               2: DW - Destination Write

The following table contains some of the cases in which
the DMA module can be configured to.


 2017-2021 Microchip Technology Inc.                                                                                              DS40001919G-page 245
                                        TABLE 15-6:    EXAMPLE DMA USE CASE TABLE
 2017-2021 Microchip Technology Inc.


                                           Source Module        Source Register(s)     Destination Module   Destination Register(s)   DCHxSIRQ             Comment
                                        Signal Measurement       SMTxCPW[U:H:L]              GPR                  GPR[x,y,z]          SMTxPWAIF   Store Captured Pulse-width
                                        Timer                                                                                                     values
                                        (SMT)                     SMTxCPR[U:H:L]                                                      SMTxPRAIF   Store Captured Period values
                                        GPR/SFR/Program            MEMORY[x,y]               TMR0                 TMR0[H:L]            TMR0IF     Use as a Timer0 reload for
                                        Flash/Data EEPROM                                                                                         custom 16-bit value


                                                                                                                                                                                 PIC18(L)F26/27/45/46/47/55/56/57K42
                                        GPR/SFR/     Program        MEMORY[x]                TMR0                    PR0                ANY       Update TMR0 frequency
                                        Flash/Data EEPROM                                                                                         based on a specific trigger
                                        GPR/SFR/      Program      MEMORY[x,y]               TMR1                 TMR1[H:L]            TMR1IF     Use as a Timer1 reload for
                                        Flash/Data EEPROM                                                                                         custom 16-bit value
                                        TMR1                         TMR1[H:L]               GPR                   GPR[x,y]            TMR1GIF    Use TMR1 Gate interrupt flag
                                                                                                                                                  to read data out of TMR1
                                                                                                                                                  register
                                        GPR/SFR/      Program       MEMORY[x]                TMR2                    PR2               TMR2IF
                                        Flash/Data EEPROM
                                        GPR/SFR/     Program      MEMORY[x,y,z]             TMR2                    PR2                 ANY       Frequency generator with 50%
                                        Flash/Data EEPROM                                 CCP or PWM             CCPR[H:L] or                     duty cycle look-up table
                                                                                                                 PWMDC[H:L]
                                        CCP                         CCPR[H:L]                GPR                  GPR[x,y]             CCPxIF     Move data from CCP 16b
                                                                                                                                                  Capture
                                        GPR/SFR/      Program      MEMORY[x,y]               CCP                  CCPR[H:L]             ANY       Load Compare value or PWM
                                        Flash/Data EEPROM                                                                                         values into the CCP
                                        GPR/SFR/ Program        MEMORY [x,y,z,u,v,w]         CCPx               CCPxR[H:L]              ANY       Update multiple PWM values
                                        Flash/Data EEPROM                                    CCPy               CCPyR[H:L]                        at the same time
                                                                                             CCPz               CCPzR[H:L]                        e.g. 3-phase motor control
                                        GPR/SFR/ Program          MEMORY[x,y,z]              NCO               NCOxINC[U:H:L]           ANY       Frequency Generator look-up
                                        Flash/Data EEPROM                                                                                         table
                                        GPR/SFR/ Program            MEMORY[x]                DAC                 DACxCON0               ANY       Update DAC values
                                        Flash/Data EEPROM
                                        GPR/SFR/ Program            MEMORY[x]              OSCTUNE                OSCTUNE               ANY       Automated Frequency
                                        Flash/Data EEPROM                                                                                         dithering
DS40001919G-page 246
                       PIC18(L)F26/27/45/46/47/55/56/57K42
15.10 Reset                                                   15.12 DMA Register Interfaces
The DMA registers are set to the default state on any         The DMA can transfer data to any GPR or SFR
Reset. The registers are also reset to the default state      location. For better user accessibility, some of the more
when the enable bit is cleared (DMA1CON1bits.EN=0).           commonly used SFR spaces have their Mirror registers
                                                              placed in a separate data memory location (0x4000-
15.11 Power Saving Mode Operation                             0x40FF). These Mirror registers can be only accessed
                                                              through the DMA Source and Destination Address
The DMA utilizes system clocks and it is treated as a         registers. Refer to Table 4-3 for details about these
peripheral when it comes to power saving operations.          mirror registers.
Like other peripherals, the DMA also uses Peripheral
Module Disable bits to further tailor its operation in low-
power states.

15.11.1     SLEEP MODE
When the device enters Sleep mode, the system clock
to the module is shut down, therefore no DMA
operation is supported in Sleep. Once the system clock
is disabled, the requisite read and write clocks are also
disabled, without which the DMA cannot perform any of
its tasks.
Any transfers that may be in progress are resumed on
exiting from Sleep mode. Register contents are not
affected by the device entering or leaving Sleep mode.
It is recommended that DMA transactions be allowed to
finish before entering Sleep mode.

15.11.2     IDLE MODE
In Idle mode, all of the system clocks (including the
read and write clocks) are still operating but the CPU is
not using them to save power.
Therefore, every instruction cycle is available to the
system arbiter and if the bubble is granted to the DMA,
it may be utilized to move data.

15.11.3     DOZE MODE
Similar to the Idle mode, the CPU does not utilize all of
the available instruction cycles slots that are available
to it in order to save power. It only executes instructions
based on its settings from the Doze settings.
Therefore, every instruction not used by the CPU is
available for system arbitration and may be utilized by
the DMA if granted by the arbiter.

15.11.4     PERIPHERAL MODULE DISABLE
The Peripheral Module Disable (PMD) registers
provide a method to disable DMA by gating all clock
sources supplied to it. The respective DMAxMD bit
needs to be set in order to disable the DMA.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 247
                      PIC18(L)F26/27/45/46/47/55/56/57K42
EXAMPLE 15-1:          SETUP DMA1 TO MOVE DATA FROM PROGRAM FLASH MEMORY TO UART1
                       TRANSMIT BUFFER USING HARDWARE TRIGGERS
//This code example illustrates using DMA1 to transfer
//10 bytes of data from 0x1000 in PFM to U1TXB 0x3DEA

void main() {
    //System Initialize
    initializeSystem();

     //Setup UART1
     initializeUART1();

     //Setup DMA1
     //DMA1CON1 - DPTR remains, Source Memory Region PFM, SPTR increments, SSTP
     DMA1CON1 = 0x0B;

     //Source registers
     //Source size
     DMA1SSZH = 0x00;
     DMA1SSZL = 0x0A;

     //Source start address, 0x1000
     DMA1SSAU = 0x00;
     DMA1SSAH = 0x10;
     DMA1SSAL = 0x00;

     //Destination registers
     //Destination size
     DMA1DSZH = 0x00;
     DMA1DSZL = 0x01;

     //Destination start address, 0x3DEA
     DMA1DSAH = 0x3D;
     DMA1DSAL = 0xEA;

     //Start trigger source U1TX
     DMA1SIRQ = 0x1C;

     //Set PRLOCKED bit to grant memory access to DMA
     INTCON0bits.GIE = 0;
     PRLOCK = 0x55;
     PRLOCK = 0xAA;
     PRLOCKbits.PRLOCKED = 1;
     INTCON0bits.GIE = 1;

     //Enable & Start DMA transfer
     DMA1CON0 = 0xC0;

     while (1) {
         doSomething();
     }
}


 2017-2021 Microchip Technology Inc.                                             DS40001919G-page 248
                       PIC18(L)F26/27/45/46/47/55/56/57K42
15.13 Register definitions: DMA
Long bit name prefixes for the DMA peripherals are
shown in Table 15-7. Refer to Section 1.3 “Register
and Bit naming conventions” for more information.


TABLE 15-7:        REGISTER AND BIT NAMING
          Peripheral            Bit Name Prefix
           DMA 1                        DMA1
           DMA 2                        DMA2


REGISTER 15-1: DMAxCON0: DMAx CONTROL REGISTER 0
 R/W-0/0      R/W/HC-0/0   R/W/HS/HC-0/0          U-0         U-0        R/W/HC-0/0       U-0        R/HS/HC-0/0
    EN         SIRQEN            DGO              —            —            AIRQEN         —             XIP
bit 7                                                                                                          bit 0


Legend:
R = Readable bit           W = Writable bit               U = Unimplemented bit, read as ‘0’
-n/n = Value at POR                                       0 = bit is cleared            x = bit is unknown
and BOR/Value at all                                                                    u = bit is unchanged
other Resets


bit 7        EN: DMA Module Enable bit
             1 = Enables module
             0 = Disables module
bit 6        SIRQEN: Start of Transfer Interrupt Request Enable bits
             1 = Hardware triggers are allowed to start DMA transfers
             0 = Hardware triggers are not allowed to start DMA transfers
bit 5        DGO: DMA transaction bit
             1 = DMA transaction is in progress
             0 = DMA transaction is not in progress
bit 4-3      Unimplemented: Read as ‘0’
bit 2        AIRQEN: Abort of Transfer Interrupt Request Enable bits
             1 = Hardware triggers are allowed to abort DMA transfers
             0 = Hardware triggers are not allowed to abort DMA transfers
bit 1        Unimplemented: Read as ‘0’
bit 0        XIP: Transfer in Progress Status bit
             1 = The DMAxBUF register currently holds contents from a read operation and has not transferred data
                  to the destination.
             0 = The DMAxBUF register is empty or has successfully transferred data to the destination address


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 249
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-2: DMAxCON1: DMAx CONTROL REGISTER1
 R/W-0/0      R/W-0/0        R/W-0/0            R/W-0/0      R/W-0/0           R/W-0/0         R/W-0/0        R/W-0/0
        DMODE[1:0]             DSTP                   SMR[1:0]                      SMODE[1:0]                    SSTP
bit 7                                                                                                                bit 0


Legend:
R = Readable bit           W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged       x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets


bit 7-6     DMODE[1:0]: Destination Address Mode Selection bits
            11 = Reserved, Do not use
            10 = DMAxDPTR[15:0] is decremented after each transfer completion
            01 = DMAxDPTR[15:0] is incremented after each transfer completion
            00 = DMAxDPTR[15:0] remains unchanged after each transfer completion
bit 5       DSTP: Destination Counter Reload Stop bit
            1 = SIRQEN bit is cleared when Destination Counter reloads
            0 = SIRQEN bit is not cleared when Destination Counter reloads
bit 4-3     SMR[1:0]: Source Memory Region Select bits
            1x = DMAxSSA[21:0] points to Data EEPROM
            01 = DMAxSSA[21:0] points to Program Flash Memory
            00 = DMAxSSA[21:0] points to SFR/GPR Data Space
bit 2-1     SMODE[1:0]: Source Address Mode Selection bits
            11 = Reserved, Do not use
            10 = DMAxSPTR[21:0] is decremented after each transfer completion
            01 = DMAxSPTR[21:0] is incremented after each transfer completion
            00 = DMAxSPTR[21:0] remains unchanged after each transfer completion
bit 0       SSTP: Source Counter Reload Stop bit
            1 = SIRQEN bit is cleared when Source Counter reloads
            0 = SIRQEN bit is not cleared when Source Counter reloads


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 250
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-3: DMAxBUF: DMAx DATA BUFFER REGISTER
   R-0           R-0            R-0              R-0              R-0               R-0            R-0          R-0
  BUF7         BUF6            BUF5              BUF4            BUF3               BUF2          BUF1         BUF0
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit           W = Writable bit                  U = Unimplemented bit, read as ‘0’
-n/n = Value at POR        1 = bit is set                    0 = bit is cleared              x = bit is unknown
and BOR/Value at all                                                                         u = bit is unchanged
other Resets


bit 7-0     BUF[7:0]: DMA Internal Data Buffer bits
            DMABUF[7:0]
            These bits reflect the content of the internal data buffer the DMA peripheral uses to hold the data being
            moved from the source to destination.

REGISTER 15-4: DMAxSSAL: DMAx SOURCE START ADDRESS LOW REGISTER
 R/W-0/0      R/W-0/0        R/W-0/0            R/W-0/0         R/W-0/0            R/W-0/0     R/W-0/0        R/W-0/0
                                                           SSA[7:0]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit           W = Writable bit                  U = Unimplemented bit, read as ‘0’
-n/n = Value at POR        1 = bit is set                    0 = bit is cleared              x = bit is unknown
and BOR/Value at all                                                                         u = bit is unchanged
other Resets


bit 7-0     SSA[7:0]: Source Start Address bits

REGISTER 15-5: DMAxSSAH: DMAx SOURCE START ADDRESS HIGH REGISTER
 R/W-0/0       R/W-0/0         R/W-0/0           R/W-0/0         R/W-0/0           R/W-0/0        R/W-0/0     R/W-0/0
                                                          SSA[15:8]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared              x = bit is unknown
BOR/Value at all other                                                                        u = bit is unchanged
Resets


bit 7-0     SSA[15:8]: Source Start Address bits


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 251
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-6: DMAxSSAU: DMAx SOURCE START ADDRESS UPPER REGISTER
   U-0           U-0         R/W-0/0          R/W-0/0         R/W-0/0             R/W-0/0     R/W-0/0        R/W-0/0
    —            —                                                   SSA[21:16]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit           W = Writable bit                U = Unimplemented bit, read as ‘0’
-n/n = Value at POR        1 = bit is set                  0 = bit is cleared               x = bit is unknown
and BOR/Value at all                                                                        u = bit is unchanged
other Resets


bit 7-0     SSA[21:16]: Source Start Address bits

REGISTER 15-7: DMAxSPTRL: DMAx SOURCE POINTER LOW REGISTER
     R-0           R-0            R-0            R-0                R-0             R-0           R-0          R-0
                                                        SPTR[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                  0 = bit is cleared              x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 15-0      SPTR[7:0]: Current Source Address Pointer

REGISTER 15-8: DMAxSPTRH: DMAx SOURCE POINTER HIGH REGISTER
     R-0           R-0            R-0            R-0                R-0             R-0           R-0          R-0
                                                        SPTR[15:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                  0 = bit is cleared              x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 5-0       SPTR[15:8]: Current Source Address Pointer


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 252
                      PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-9: DMAxSPTRU: DMAx SOURCE POINTER UPPER REGISTER
     U-0           U-0            R-0            R-0                 R-0            R-0            R-0         R-0
        —           —                                                 SPTR[21:16]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 7-6       Unimplemented: Read as ‘0’
bit 5-0       SPTR[21:16]: Current Source Address Pointer

REGISTER 15-10: DMAxSSZL: DMAx SOURCE SIZE LOW REGISTER
  R/W-0/0        R/W-0/0        R/W-0/0         R/W-0/0          R/W-0/0           R/W-0/0     R/W-0/0       R/W-0/0
                                                          SSZ[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 7-0       SSZ[7:0]: Source Message Size bits

REGISTER 15-11: DMAxSSZH: DMAx SOURCE SIZE HIGH REGISTER
     U-0           U-0            U-0            U-0             R/W-0/0           R/W-0/0     R/W-0/0       R/W-0/0
        —           —              —              —                                    SSZ[11:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 7-4       Unimplemented: Read as ‘0’
bit 3-0       SSZ[11:8]: Source Message Size bits


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 253
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-12: DMAxSCNTL: DMAx SOURCE COUNT LOW REGISTER
     R-0           R-0            R-0            R-0               R-0           R-0            R-0          R-0
                                                       SCNT[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit             W = Writable bit              U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                0 = bit is cleared              x = bit is unknown
BOR/Value at all other                                                                     u = bit is unchanged
Resets


bit 7-0       SCNT[7:0]: Current Source Byte Count

REGISTER 15-13: DMAxSCNTH: DMAx SOURCE COUNT HIGH REGISTER
   U-0           U-0            U-0             U-0            R-0               R-0            R-0          R-0
    —            —               —               —                                 SCNT[11:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit           W = Writable bit               U = Unimplemented bit, read as ‘0’
-n/n = Value at POR        1 = bit is set                 0 = bit is cleared              x = bit is unknown
and BOR/Value at all                                                                      u = bit is unchanged
other Resets


bit 7-4     Unimplemented: Read as ‘0’
bit 3-0     SCNT[11:8]: Current Source Byte Count

REGISTER 15-14: DMAxDSAL: DMAx DESTINATION START ADDRESS LOW REGISTER
  R/W-0/0        R/W-0/0        R/W-0/0         R/W-0/0       R/W-0/0           R/W-0/0        R/W-0/0     R/W-0/0
                                                       DSA[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit             W = Writable bit              U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                0 = bit is cleared              x = bit is unknown
BOR/Value at all other                                                                     u = bit is unchanged
Resets


bit 7-0       DSA[7:0]: Destination Start Address bits


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 254
                      PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-15: DMAxDSAH: DMAx DESTINATION START ADDRESS HIGH REGISTER
  R/W-0/0        R/W-0/0        R/W-0/0         R/W-0/0        R/W-0/0           R/W-0/0    R/W-0/0        R/W-0/0
                                                       DSA[15:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit             W = Writable bit               U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                 0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                     u = bit is unchanged
Resets


bit 7-0       DSA[15:8]: Destination Start Address bits

REGISTER 15-16: DMAxDPTRL: DMAx DESTINATION POINTER LOW REGISTER
     R-0           R-0            R-0            R-0               R-0            R-0            R-0         R-0
                                                       DPTR[7:0]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit             W = Writable bit               U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                 0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                     u = bit is unchanged
Resets


bit 7-0       DPTR[7:0]: Current Destination Address Pointer

REGISTER 15-17: DMAxDPTRH: DMAx DESTINATION POINTER HIGH REGISTER
     R-0           R-0            R-0            R-0               R-0            R-0            R-0         R-0
                                                       DPTR[15:8]
bit 7                                                                                                              bit 0


Legend:
R = Readable bit             W = Writable bit               U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                 0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                     u = bit is unchanged
Resets


bit 7-0       DPTR[15:8]: Current Destination Address Pointer


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 255
                      PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-18: DMAxDSZL: DMAx DESTINATION SIZE LOW REGISTER
  R/W-0/0        R/W-0/0        R/W-0/0         R/W-0/0          R/W-0/0           R/W-0/0     R/W-0/0       R/W-0/0
                                                          DSZ[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 7-0       DSZ[7:0]: Destination Message Size bits

REGISTER 15-19: DMAxDSZH: DMAx DESTINATION SIZE HIGH REGISTER
     U-0           U-0            U-0            U-0             R/W-0/0           R/W-0/0     R/W-0/0       R/W-0/0
        —           —              —              —                                    DSZ[11:8]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 7-4       Unimplemented: Read as ‘0’
bit 3-0       DSZ[11:8]: Destination Message Size bits

REGISTER 15-20: DMAxDCNTL: DMAx DESTINATION COUNT LOW REGISTER
     R-0           R-0            R-0            R-0                 R-0            R-0            R-0         R-0
                                                       DCNT[7:0]
bit 7                                                                                                                bit 0


Legend:
R = Readable bit             W = Writable bit                 U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set                   0 = bit is cleared             x = bit is unknown
BOR/Value at all other                                                                       u = bit is unchanged
Resets


bit 7-0       DCNT[7:0]: Current Destination Byte Count


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 256
                       PIC18(L)F26/27/45/46/47/55/56/57K42
REGISTER 15-21: DMAxDCNTH: DMAx DESTINATION COUNT HIGH REGISTER
     U-0           U-0            U-0            U-0           R-0              R-0            R-0         R-0
        —           —              —              —                               DCNT[11:8]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit             W = Writable bit            U = Unimplemented bit, read as ‘0’
-n/n = Value at POR and      1 = bit is set              0 = bit is cleared              x = bit is unknown
BOR/Value at all other                                                                   u = bit is unchanged
Resets


bit 7-4       Unimplemented: Read as ‘0’
bit 3-0       DCNT[11:8]: Current Destination Byte Count

REGISTER 15-22: DMAxSIRQ: DMAx START INTERRUPT REQUEST SOURCE SELECTION
                REGISTER
   U-0        R/W-0/0        R/W-0/0          R/W-0/0       R/W-0/0           R/W-0/0     R/W-0/0        R/W-0/0
    —                                                      SIRQ[6:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit           W = Writable bit             U = Unimplemented bit, read as ‘0’
-n/n = Value at POR        1 = bit is set               0 = bit is cleared              x = bit is unknown
and BOR/Value at all                                                                    u = bit is unchanged
other Resets


bit 7       Unimplemented: Read as ‘0’
bit 6-0     SIRQ[6:0]: DMAx Start Interrupt Request Source Selection bits
            Please refer to Table 15-2 for more information.

REGISTER 15-23: DMAxAIRQ: DMAx ABORT INTERRUPT REQUEST SOURCE SELECTION
                REGISTER
   U-0        R/W-0/0        R/W-0/0          R/W-0/0       R/W-0/0           R/W-0/0     R/W-0/0        R/W-0/0
    —                                                      AIRQ[6:0]
bit 7                                                                                                            bit 0


Legend:
R = Readable bit           W = Writable bit             U = Unimplemented bit, read as ‘0’
-n/n = Value at POR        1 = bit is set               0 = bit is cleared              x = bit is unknown
and BOR/Value at all                                                                    u = bit is unchanged
other Resets


bit 7       Unimplemented: Read as ‘0’
bit 6-0     AIRQ[6:0]: DMAx Interrupt Request Source Selection bits
            Please refer to Table 15-2 for more information.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 257
                      PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 15-2:       DMAxSIRQ AND DMAxAIRQ TRIGGER SOURCES
  DMAxSIRQ            Trigger              Level                         DMAxSIRQ             Trigger            Level
  DMAxAIRQ           Source(2)          Triggered(1)                     DMAxAIRQ             Source           Triggered
     0x00        Reserved                                                      0x2A         DMA2SCNTIF        No
     0x01        HLVDIF              No                                        0x2B         DMA2DCNTIF        No
     0x02        OSFIF               No                                       0x2C          DMA2ORIF          No
     0x03        CSWIF               No                                       0x2D          DMA2AIF           No
     0x04        NVMIF               No                                        0x2E         I2C2RXIF          Yes
     0x05        SCANIF              No                                        0x2F         I2C2TXIF          Yes
     0x06        CRCIF               No                                        0x30         I2C2IF            Yes
     0x07        IOCIF               Yes                                       0x31         I2C2EIF           Yes
     0x08        INT0IF              No                                        0x32         U2RXIF            Yes
     0x09        ZCDIF               No                                        0x33         U2TXIF            Yes
     0x0A        ADIF                No                                        0x34         U2EIF             Yes
     0x0B        ADTIF               No                                        0x35         U2IF              No
     0x0C        CMP1IF              No                                        0x36         TMR3IF            No
     0x0D        SMT1IF              No                                        0x37         TMR3GIF           No
     0x0E        SMT1PRAIF           No                                        0x38         TMR4IF            No
     0x0F        SMT1PWAIF           No                                        0x39         CCP2IF            No
     0x10        DMA1SCNTIF          No                                        0x3A         Reserved
     0x11        DMA1DCNTIF          No                                        0x3B         CWG2IF            No
     0x12        DMA1ORIF            No                                       0x3C          CLC2IF            No
     0x13        DMA1AIF             No                                       0x3D          INT2IF            No
     0x14        SPI1RXIF            Yes                                       0x3E         Reserved
     0x15        SPI1TXIF            Yes                                       0x3F         Reserved
     0x16        SPI1IF              Yes                                       0x40         Reserved
     0x17        I2C1RXIF            Yes                                       0x41         Reserved
     0x18        I2C1TXIF            Yes                                       0x42         Reserved
     0x19        I2C1IF              Yes                                       0x43         Reserved
     0x1A        I2C1EIF             Yes                                       0x44         Reserved
     0x1B        U1RXIF              Yes                                       0x45         Reserved
     0x1C        U1TXIF              Yes                                       0x46         TMR5IF            No
     0x1D        U1EIF               Yes                                       0x47         TMR5GIF           No
     0x1E        U1IF                No                                        0x48         TMR6IF            No
     0x1F        TMR0IF              No                                        0x49         CCP3IF            No
     0x20        TMR1IF              No                                        0x4A         CWG3IF            No
     0x21        TMR1GIF             No                                        0x4B         CLC3IF            No
     0x22        TMR2IF              No                                       0x4C          Reserved
     0x23        CCP1IF              No                                       0x4D          Reserved
     0x24        Reserved                                                      0x4E         Reserved
     0x25        NCOIF               No                                        0x4F         Reserved
     0x26        CWG1IF              No                                        0x50         CCP4IF            No
     0x27        CLC1IF              No                                        0x51         CLC4IF            No
     0x28        INT1IF              No                                        0x52         Reserved
     0x29        CMP2IF              No                                          –
                                                                               0xFF
Note 1:     All trigger sources that are not Level-triggered are Edge-triggered.
     2:     The event that sets the flag is the interrupt trigger, not the flag itself. The flag remains set.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 258
                      PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 15-3:       SUMMARY OF REGISTERS ASSOCIATED WITH DMA
                                                                                                        Register
     Name           Bit 7       Bit 6   Bit 5    Bit 4      Bit 3        Bit 2       Bit 1     Bit 0
                                                                                                        on Page
DMAxCON0             EN       SIRQEN    DGO       —              —     AIRQEN         —         XIP       250
DMAxCON1              DMODE[1:0]        DSTP        SMR[1:0]              SMODE[1:0]           SSTP       251
DMAxBUF            DBUF7       DBUF6    DBUF5   DBUF4      DBUF3        DBUF2       DBUF1     DBUF0       252
DMAxSSAL                                              SSA[7:0]                                            252
DMAxSSAH                                            SSA[15:8]                                             252
DMAxSSAU              —          —                               SSA[21:16]                               253
DMAxSPTRL                                          SPTR[7:0]                                              253
DMAxSPTRH                                          SPTR[15:8]                                             253
DMAxSPTRU             —          —                               SPTR[21:16]                              254
DMAxSSZL                                              SSZ[7:0]                                            254
DMAxSSZH              —          —       —        —                           SSZ[11:8]                   254
DMAxSCNTL                                          SCNT[7:0]                                              255
DMAxSCNTH             —          —       —        —                        SCNT[11:8]                     255
DMAxDSAL                                            DSA[7:0]                                              255
DMAxDSAH                                           DSA[15:8]                                              256
DMAxDPTRL                                          DPTR[7:0]                                              256
DMAxDPTRH                                          DPTR[15:8]                                             256
DMAxDSZL                                              DSZ[7:0]                                            257
DMAxDSZH              —          —       —        —                           DSZ[11:8]                   257
DMAxDCNTL                                          DCNT[7:0]                                              257
DMAxDCNTH             —          —       —        —                        DCNT[11:8]                     258
DMAxSIRQ              —                                   SIRQ[6:0]                                       258
DMAxAIRQ              —                                   AIRQ[6:0]                                       258
Legend: — = unimplemented location, read as ‘0’. Shaded cells are not used by DMA.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 259
