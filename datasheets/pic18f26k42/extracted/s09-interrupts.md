                       PIC18(L)F26/27/45/46/47/55/56/57K42
9.0      INTERRUPT CONTROLLER                                There are two other configuration bits that control the
                                                             way the interrupt controller can be configured.
The Vectored Interrupt Controller module reduces the
                                                             • CONFIG2L[3], MVECEN bit
numerous peripheral interrupt request signals to a
single interrupt request signal to the CPU. This module      • CONFIG2L[4], IVT1WAY bit
includes the following major features:                       The MVECEN bit in CONFIG2L determines whether
• Interrupt Vector Table (IVT) with a unique vector          the Vector table is used to determine the interrupt
  for each interrupt source                                  priorities.
• Fixed and ensured interrupt latency                        • The IVT1WAY determines the number of times
• Programmable base address for Interrupt Vector               the IVTLOCKED bit can be cleared and set after a
  Table (IVT) with lock                                        device Reset. See Section 9.2.3 “Interrupt Vec-
                                                               tor Table (IVT) address calculation” for details.
• Two user-selectable priority levels – High priority
  and Low priority
• Two levels of context saving
• Interrupt state status bits to indicate the current
  execution status of the CPU
The Interrupt Controller module assembles all of the
interrupt request signals and resolves the interrupts
based on both a fixed natural order priority (i.e.,
determined by the Interrupt Vector Table), and a user-
assigned priority (i.e., determined by the IPRx
registers), thereby eliminating scanning of interrupt
sources.

9.1      Interrupt Control and Status
         Registers
The devices in this family implement the following
registers for the interrupt controller:
• INTCON0, INTCON1 Control Registers
• PIRx – Peripheral Interrupt Status Registers
• PIEx – Peripheral Interrupt Enable Registers
• IPRx – Peripheral Interrupt Priority Registers
• IVTBASE[20:0] Address Registers
• IVTLOCK Register
Global interrupt control functions and external
interrupts are controlled from the INTCON0 register.
The INTCON1 register contains the status flags for the
Interrupt controller.
The PIRx registers contain all of the interrupt request
flags. Each source of interrupt has a status bit, which is
set by the respective peripherals or an external signal
and is cleared via software.
The PIEx registers contain all of the interrupt enable
bits. These control bits are used to individually enable
interrupts from the peripherals or external signals.
The IPRx registers are used to set the Interrupt Priority
Level for each source of interrupt. Each user interrupt
source can be assigned to either a high or low priority.
The IVTBASE register is user programmable and is
used to determine the start address of the Interrupt
Vector Table and the IVTLOCK register is used to
prevent any unintended writes to the IVTBASE register.


 2017-2021 Microchip Technology Inc.                                                        DS40001919G-page 115
                      PIC18(L)F26/27/45/46/47/55/56/57K42
9.2       Interrupt Vector Table (IVT)                      9.2.2       INTERRUPT VECTOR TABLE
                                                                        CONTENTS
The interrupt controller supports an Interrupt Vector
Table (IVT) that contains the vector address location for   MVECEN = 0
each interrupt request source.                              When MVECEN = 0, the address location pointed by
The Interrupt Vector Table (IVT) resides in program         the IVTBASE registers has a GOTO instruction for a
memory, starting at address location determined by the      high priority interrupt. Similarly, the corresponding low
IVTBASE registers; refer to Register 9-36, Register 9-      priority vector location also has a GOTO instruction,
37 and Register 9-38 for details. The IVT contains 68       which is executed in case of a low priority interrupt.
vectors, one for each source of interrupt. Each interrupt   MVECEN = 1
vector location contains the starting address of the
                                                            When MVECEN = 1, the value in the vector table of
associated Interrupt Service Routine (ISR).
                                                            each interrupt, points to the address location of the first
The MVECEN bit in Configuration Word 2L controls the        instruction of the interrupt service routine.
availability of the vector table.
                                                            ISR Location = Interrupt Vector Table entry << 2.
9.2.1       INTERRUPT VECTOR TABLE BASE
                                                            9.2.3       INTERRUPT VECTOR TABLE (IVT)
            ADDRESS (IVTBASE)
                                                                        ADDRESS CALCULATION
The start address of the vector table is user
                                                            MVECEN = 0
programmable through the IVTBASE registers. The
user must ensure the start address is such that it can      When the MVECEN bit in Configuration Word 2L
encompass the entire vector table inside the program        (Register 5-3) is cleared, the address pointed by
memory.                                                     IVTBASE registers is used as the high priority interrupt
                                                            vector address. The low priority interrupt vector
Each vector address is a 16-bit word (or two address
                                                            address is offset eight instruction words from the
locations on PIC18 devices). So for n interrupt sources,
                                                            address in IVTBASE registers.
there are 2n address locations necessary to hold the
table starting from IVTBASE as the first location. So the   For PIC18 devices the IVTBASE registers default to
staring address of IVTBASE may be chosen such that          00 0008h, the high priority interrupt vector address will
the address range form IVTBASE to (IVTBASE +2n-1)           be 00 0008h and the low priority interrupt vector
can be encompassed inside the program flash mem-            address will be 00 0018h.
ory.                                                        MVECEN = 1
For example, the K42 devices have the highest vector        Each interrupt has a unique vector number associated
number: 81. So IVTBASE may be chosen such that              with it as defined in Table 9-2. This vector number is
(IVTBASE + 0xA1) is less than the last memory               used for calculating the location of the interrupt vector
location in program flash memory.                           for a particular interrupt source.
A programmable vector table base address is useful in       Interrupt Vector Address = IVTBASE + (2*Vector
situations to switch between different sets of vector       Number).
tables, depending on the application. It can also be
used when the application program needs to update           This calculated Interrupt Vector Address value is stored
the existing vector table (vector address values).          in the IVTAD[20:0] registers when an interrupt is
                                                            received (Registers 9-39 through 9-41).
  Note:     It is required that the user assign an even
                                                            User-assigned software priority assigned using the
            address to the IVTBASE register for
                                                            IPRx registers does not affect address calculation and
            correct operation.
                                                            is only used to resolve concurrent interrupts.


                                                            If for any reason the address of the ISR could not be
                                                            fetched from the vector table, it will cause the system
                                                            to reset and clear the memory execution violation flag
                                                            (MEMV bit) in PCON1 register (Register 6-3). This
                                                            occurs due to any one of the following:
                                                            • The entry for the interrupt in the vector table lies
                                                              outside the executable PFM area (SAF area is
                                                              nonexecutable when SAFEN = 1).
                                                            • ISR pointed by the vector table lies outside the
                                                              executable PFM area (SAF area is
                                                              nonexecutable when SAFEN = 1).


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 116
                       PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 9-1:        IVT ADDRESS CALCULATION SUMMARY
                                                              Interrupt Priority
   IVT Address Calculation                                INTCON0 Register, IPEN bit

                                                    0                                       1
                                                                                       High Priority
 Multi-Vector Enable                                                                    IVTBASE
                            0                   IVTBASE
 CONFIG 2L register                                                                   Low Priority
    MVECEN bit                                                                     IVTBASE + 8 words
                            1                             IVTBASE + 2*(Vector Number)

9.2.4       ACCESS CONTROL FOR IVTBASE                       The user must follow the sequence shown in
            REGISTERS                                        Example 9-2 to set the IVTLOCKED bit.
The Interrupt controller has an IVTLOCKED bit which
can be set to avoid inadvertent changes to the IVT-          EXAMPLE 9-2:         IVT LOCK SEQUENCE
BASE registers contents. Setting and clearing this bit       ; Disable Interrupts:
requires a special sequence as an extra precaution                   BCF            INTCON0, GIE;
                                                             ; Bank to IVTLOCK register
against inadvertent changes.
                                                                     BANKSEL        IVTLOCK;
To allow writes to IVTBASE registers, the interrupts                 MOVLW          55h;
must be disabled (GIEH = 0) and the IVTLOCKED bit
must be cleared. The user must follow the sequence           ; Required sequence, next 4 instructions
shown in Example 9-1 to clear the IVTLOCKED bit.                     MOVWF          IVTLOCK;
                                                                     MOVLW          AAh;
                                                                     MOVWF          IVTLOCK;
EXAMPLE 9-1:           IVT UNLOCK SEQUENCE
; Disable Interrupts:                                        ; Set IVTLOCKED bit to enable writes
        BCF            INTCON0, GIE;                                 BSF            IVTLOCK, IVTLOCKED;
; Bank to IVTLOCK register
        BANKSEL        IVTLOCK;                              ; Enable Interrupts
        MOVLW          55h;                                          BSF                INTCON0, GIE;

; Required sequence, next 4 instructions
        MOVWF          IVTLOCK;                              When the IVT1WAY Configuration bit is set, the
        MOVLW          AAh;                                  IVTLOCKED bit can be cleared and set only once after
        MOVWF          IVTLOCK;                              a device Reset. The unlock operation in Example 9-1
                                                             will have no effect after the lock sequence in
; Clear IVTLOCKED bit to enable writes                       Example 9-2 is used to set the IVTLOCK. Unlocking is
        BCF            IVTLOCK, IVTLOCKED;                   inhibited until a system Reset occurs.

; Enable Interrupts
        BSF                  INTCON0, GIE;


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 117
                         PIC18(L)F26/27/45/46/47/55/56/57K42
9.3        Interrupt Priority
                                                                 Note 1: When a high priority interrupt preempts a
The final priority level for any pending source of interrupt
                                                                         concurrent low priority interrupt, the GIEL
is determined first by the user-assigned priority of that
                                                                         bit may be cleared in the high priority
source in the IPRx register, then by the natural order
                                                                         Interrupt Service Routine. If the GIEL bit
priority within the IVT. The sections below detail the
                                                                         is cleared, the low priority interrupt will
operation of Interrupt priorities.
                                                                         NOT be serviced even if it was originally
9.3.1         USER (SOFTWARE) PRIORITY                                   requested. The corresponding interrupt
                                                                         flag needs to be cleared in user code.
User-assigned interrupt priority is enabled by setting
the IPEN bit in the INTCON0 register (Register 9-1).                  2: When a high priority interrupt is
Each peripheral interrupt source can be assigned a                       requested while a low priority Interrupt
high or low priority level by the user. The user-                        Service Routine is executing, the GIEL bit
assignable interrupt priority control bits for each                      may be cleared in the high priority
interrupt are located in the IPRx registers (Registers 9-                Interrupt Service Routine. The pending
25 through 9-35).                                                        low priority interrupt will resume even if
                                                                         the GIEL bit is cleared.
The interrupts are serviced based on predefined
interrupt priority scheme defined below.
1.    Interrupts set by the user as high-priority
      interrupt have higher precedence of execution.
      High-priority interrupts will override a low-priority
      request when:
      a) A low priority interrupt has been requested or its
         request is already pending.
      b) A low- and high-priority interrupt are triggered
         concurrently, i.e., on the same instruction cycle(1).
      c) A low-priority interrupt was requested and the
         corresponding Interrupt Service Routine is
         currently executing. In this case, the lower
         priority interrupt routine will complete executing
         after the high-priority interrupt has been
         serviced(2).
2.    Interrupts set by the user as a low priority have
      the lower priority of execution and are
      preempted by any high-priority interrupt.
3.    Interrupts defined with the same software priority
      cannot preempt or interrupt each other.
      Concurrent pending interrupts with the same user
      priority are resolved using the natural order priority.
      (when MVECEN = ON) or in the order the interrupt
      flag bits are polled in the ISR (when MVECEN =
      OFF).


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 118
                              PIC18(L)F26/27/45/46/47/55/56/57K42
9.3.2          NATURAL ORDER (HARDWARE)                       The natural order priority scheme has vector interrupt 0
               PRIORITY                                       as the highest priority and vector interrupt 81 as the
                                                              lowest priority.
When more than one interrupt with the same user
specified priority level are requested, the priority          For example, when two concurrently occurring interrupt
conflict is resolved by using a method called “Natural        sources that are both designated high priority using the
Order Priority”. Natural order priority is a fixed priority   IPRx register will be resolved using the natural order
scheme that is based on the Interrupt Vector Table.           priority (i.e., the interrupt with a lower corresponding
Table 9-2 shows the natural order priority and the            vector number will preempt the interrupt with the higher
interrupt vector number assigned for each source.             vector number).
                                                              The ability for the user to assign every interrupt source
TABLE 9-2:             INTERRUPT VECTOR                       to high or low priority levels means that the user
                       PRIORITY TABLE                         program can give an interrupt with a low natural order
  Vector          Interrupt       Vector          Interrupt
                                                              priority a higher overall priority level.
 Number            Source        Number            Source
    0      Software Interrupt      42      DMA2SCNT           9.4       Interrupt Operation
    1      HLVD                    43      DMA2DCNT
                                                              All pending interrupts are indicated by the flag bit being
    2      OSF                     44      DMA2OR
                                                              equal to a ‘1’ in the PIRx register. All pending interrupts
    3      CSW                     45      DMA2A
                                                              are resolved using the priority scheme explained in
    4      NVM                     46      I2C2RX
                                                              Section 9.3 “Interrupt Priority”.
    5      SCAN                    47      I2C2TX
    6      CRC                     48      I2C2               Once the interrupt source to be serviced is resolved,
    7      IOC                     49      I2C2E              the program execution vectors to the resolved interrupt
    8      INT0                    50      U2RX               vector addresses, as explained in Section
    9      ZCD                     51      U2TX               9.2 “Interrupt Vector Table (IVT)”. The vector number
   10      AD                      52      U2E                is also stored in the WREG register. Most of the flag bits
   11      ADT                     53      U2                 are required to be cleared by the application software,
   12      C1                      54      TMR3               but in some cases, device hardware clears the interrupt
   13      SMT1                    55      TMR3G              automatically. Some flag bits are read-only in the PIRx
   14      SMT1PRA                 56      TMR4               registers, these flags are a summary of the source
   15      SMT1PWA                 57      CCP2               interrupts and the corresponding interrupt flags of the
   16      DMA1SCNT                58      —                  source must be cleared.
   17      DMA1DCNT                59      CWG2               A valid interrupt can be either a high or low priority
   18      DMA1OR                  60      CLC2               interrupt when in main routine or a high priority interrupt
   19      DMA1A                   61      INT2               when in low priority Interrupt Service Routine.
   20      SPI1RX                  62      —                  Depending on order of interrupt requests received and
   21      SPI1TX                  63      —                  their relative timing, the CPU will be in the state of
   22      SPI1                    64      —                  execution indicated by the STAT bits of the INTCON1
   23      I2C1RX                  65      —                  register (Register 9-2).
   24      I2C1TX                  66      —
   25      I2C1                    67      —
                                                              The State machine shown in Figure 9-1 and the
   26      I2C1E                   68      —
                                                              subsequent sections detail the execution of interrupts
   27      U1RX                    69      —
                                                              when received in different orders.
   28      U1TX                    70      TMR5
   29      U1E                     71      TMR5G
                                                                Note:     The state of GIEH/L is not changed by the
   30      U1                      72      TMR6
                                                                          hardware when servicing an interrupt. The
   31      TMR0                    73      CCP3
                                                                          internal state machine is used to keep
   32      TMR1                    74      CWG3
                                                                          track of execution states. These bits can
   33      TMR1G                   75      CLC3
                                                                          be manipulated in the user code resulting
   34      TMR2                    76      —
                                                                          in transferring execution to the main
   35      CCP1                    77      —
                                                                          routine and ignoring existing interrupts.
   36      —                       78      —
   37      NCO                     79      —
   38      CWG1                    80      CCP4
   39      CLC1                    81      CLC4
   40      INT1
   41      C2


 2017-2021 Microchip Technology Inc.                                                           DS40001919G-page 119
                                        FIGURE 9-1:            VECTORED INTERRUPTS STATE TRANSITION DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                                             Rev. 10-000265A
                                                                                                                                                                                                     7/6/2016


                                                                                                        MAIN
                                                                                                     INTSTAT = 00


                                                                                                                                                                                                                PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                 High Interrupt addressed,
                                              High Interrupt                                      Low Interrupt pending                                                                Low Interrupt
                                                                        HIGH                                                                         LOW
                                                requested           INTSTAT = 10                                                                 INTSTAT = 01                            requested
                                                                                                 Low Interrupt addressed,
                                                                                                  High Interrupt pending


                                                                                                                                                           High Interrupt addressed,
                                                                                                                             High Interrupt requested,
                                                                                                                              Low Interrupt pending


                                                                                                                                                            Low Interrupt pending
                                                                                                                                               HIGH                                    High Interrupt
                                                                                                                                            INTSTAT = 11                                 requested
DS40001919G-page 120
                                        9.4.1       SERVING A HIGH OR LOW PRIORITY INTERRUPT
 2017-2021 Microchip Technology Inc.


                                                    WHEN MAIN ROUTINE CODE IS EXECUTING
                                        When a high or low priority interrupt is requested when the main routine code
                                        is executing, the main routine execution is halted and the ISR is addressed, see
                                        Figure 9-2. Upon a return from the ISR (by executing the RETFIE instruction),
                                        the main routine resumes execution.

                                        FIGURE 9-2:              INTERRUPT EXECUTION: HIGH/LOW PRIORITY INTERRUPT WHEN EXECUTING MAIN ROUTINE


                                                                                                                                                                                                   PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                                                                                Rev. 10-000267A
                                                                                                                                                                                       9/12/2016


                                                                                                                           ISR Code Executing

                                                                                                                                                 RETFIE Executed

                                                  Main Code            Main Code Executing                          Main Code Execution Halted            Main Code Executing


                                                     Interrupt

                                                                                                 Interrupt   Interrupt
                                                                                                 received     cleared
DS40001919G-page 121
                                        9.4.2       SERVING A HIGH PRIORITY INTERRUPT WHILE A LOW
 2017-2021 Microchip Technology Inc.


                                                    PRIORITY INTERRUPT PENDING
                                        A high priority interrupt request will always take precedence over any interrupt
                                        of a lower priority. The high priority interrupt is acknowledged first, then the low-
                                        priority interrupt is acknowledged. Upon a return from the high priority ISR (by
                                        executing the RETFIE instruction), the low priority interrupt is serviced, see
                                        Figure 9-3.
                                        If any other high priority interrupts are pending and enabled, then they are


                                                                                                                                                                                                              PIC18(L)F26/27/45/46/47/55/56/57K42
                                        serviced before servicing the pending low priority interrupt. If no other high
                                        priority interrupt requests are active, the low priority interrupt is serviced.

                                        FIGURE 9-3:             INTERRUPT EXECUTION: HIGH PRIORITY INTERRUPT WITH A LOW PRIORITY INTERRUPT PENDING

                                                                                                                                                                                           Rev. 10-000267C
                                                                                                                                                                                                  9/12/2016


                                                        High ISR                                                         High ISR
                                                                                                                                                  RETFIE Executed

                                                        Low ISR                                                                                          Low ISR
                                                                                                                                                                    RETFIE Executed

                                                      Main Code                Main routine                                     Main Code Execution Halted                  Main routine

                                                      High Priority
                                                         Interrupt
                                                                                                 High Interrupt     High Interrupt
                                                                                                    received           cleared
                                                       Low Priority
                                                          Interrupt
                                                                                                             Low Interrupt                         Low Interrupt
DS40001919G-page 122


                                                                                                               received                               cleared
                                        9.4.3       PREEMPTING LOW PRIORITY INTERRUPTS
 2017-2021 Microchip Technology Inc.


                                        Low-priority interrupts can be preempted by high priority interrupts. While in the
                                                                                                                                          Note 1: The high priority interrupt flag must be
                                        low priority ISR, if a high-priority interrupt arrives, the high priority interrupt
                                                                                                                                                  cleared to avoid recursive interrupts.
                                        request is generated and the low priority ISR is suspended, while the high
                                        priority ISR is executed, see Figure 9-4.                                                                2: If a low-priority ISR was already serviced
                                                                                                                                                    halfway before moving on to a high
                                        After the high priority ISR is complete and if any other high priority interrupt
                                                                                                                                                    priority ISR, then the low priority ISR is
                                        requests are not active, the execution returns to the preempted low priority ISR.
                                                                                                                                                    completely serviced even if user code


                                                                                                                                                                                                                    PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                                                    clears GIEL.

                                        FIGURE 9-4:              INTERRUPT EXECUTION: HIGH PRIORITY INTERRUPT PREEMPTING LOW PRIORITY INTERRUPTS

                                                                                                                                                                                                 Rev. 10-000267B
                                                                                                                                                                                                        9/12/2016


                                                       High ISR                                                                       High ISR
                                                                                                  Low Interrupt pending,                                 RETFIE Executed
                                                                                                  High Interrupt received
                                                       Low ISR                                                  Low ISR       Low ISR Execution Halted    Low ISR
                                                                                                                                                                       RETFIE Executed

                                                     Main Code               Main routine                                   Main Code Execution Halted                         Main routine

                                                     High Priority
                                                        Interrupt
                                                                                                                High Interrupt      High Interrupt
                                                                                                                   received            cleared
                                                      Low Priority
                                                         Interrupt
                                                                                                Low Interrupt      Low Interrupt
                                                                                                  received           cleared
DS40001919G-page 123
                                        9.4.4       SIMULTANEOUS LOW AND HIGH PRIORITY
 2017-2021 Microchip Technology Inc.


                                                    INTERRUPTS
                                        When both high and low interrupts are active in the same instruction cycle (i.e.,
                                        simultaneous interrupt events), both the high and the low priority requests are
                                        generated. The high priority ISR is serviced first before servicing the low priority
                                        interrupt see Figure 9-5.

                                        FIGURE 9-5:             INTERRUPT EXECUTION: SIMULTANEOUS LOW AND HIGH PRIORITY INTERRUPTS


                                                                                                                                                                                                             PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                                                                                                                          Rev. 10-000267D
                                                                                                                                                                                                 9/12/2016


                                                          High ISR                                                        High ISR
                                                                                                                                                 RETFIE Executed

                                                          Low ISR                                                                                       Low ISR
                                                                                                                                                                   RETFIE Executed

                                                         Main Code               Main routine                                  Main Code Execution Halted                  Main routine

                                                        High Priority
                                                           Interrupt
                                                                                                   High Interrupt       High Interrupt
                                                                                                      received             cleared
                                                         Low Priority
                                                            Interrupt
                                                                                                       Low Interrupt                              Low Interrupt
                                                                                                         received                                   cleared
DS40001919G-page 124
                      PIC18(L)F26/27/45/46/47/55/56/57K42
9.5      Context Saving
The Interrupt controller supports a two-level deep
context saving (Main routine context and Low ISR
context). Refer to state machine shown in Figure 9-6
for details.
The Program Counter (PC) is saved on the dedicated
device PC stack. CPU registers saved include STATUS,
WREG, BSR, FSR0/1/2, PRODL/H and PCLATH/U.
After WREG has been saved to the context registers,
the resolved vector number of the interrupt source to be
serviced is copied into WREG. Context save and
restore operation is completed by the interrupt
controller based on current state of the interrupts and
the order in which they were sent to the CPU.
Context save/restore works the same way in both
states of MVECEN. When IPEN = 0, there is only one
level interrupt active. Hence, only the main context is
saved when an interrupt is received.

9.5.1       ACCESSING SHADOW REGISTERS
The Interrupt controller automatically saves the context
information in the shadow registers available in Bank
56. Both the saved context values (i.e., main routine
and low ISR) can be accessed using the same set of
shadow registers. By clearing the SHADLO bit in the
SHADCON register (Register 9-43), the CPU register
values saved for main routine context can accessed,
and by setting the SHADLO bit of the CPU register,
values saved for low ISR context can accessed. Low
ISR context is automatically restored to the CPU
registers upon exiting the high ISR. Similarly, the main
context is automatically restored to the CPU registers
upon exiting the low ISR.
The Shadow registers in Bank 56 are readable and
writable, so if the user desires to modify the context,
then the corresponding shadow register may be
modified and the value will be restored when exiting the
ISR. Depending on the user’s application, other
registers may also need to be saved.


 2017-2021 Microchip Technology Inc.                      DS40001919G-page 125
                                        FIGURE 9-6:        CONTEXT SAVE STATE MACHINE DIAGRAM
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                   Rev. 10-000266A
                                                                                                                                                                           7/6/2016


                                                                                                   MAIN
                                                                                                INTSTAT = 00


                                                                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                           No Context Save/Restore
                                             No Context          HIGH                                                     LOW                                  No Context
                                            Save/Restore     INTSTAT = 10                                             INTSTAT = 01                            Save/Restore
                                                                                           No Context Save/Restore


                                                                                                                                        Restore Low context
                                                                                                                     Save Low context
                                                                                                                        HIGH                                   No Context
                                                                                                                     INTSTAT = 11                             Save/Restore
DS40001919G-page 126
                       PIC18(L)F26/27/45/46/47/55/56/57K42
9.6      Returning from Interrupt Service
         Routine (ISR)
The “Return from Interrupt” instruction (RETFIE) is
used to mark the end of an ISR.
When RETFIE 1 instruction is executed, the PC is
loaded with the saved PC value from the top of the PC
stack. Saved context is also restored with the execution
of this instruction. Thus, execution returns to the
previous state of operation that existed before the
interrupt occurred.
When RETFIE 0 instruction is executed, the saved
context is not restored back to the registers.

9.7      Interrupt Latency
By assigning each interrupt with a vector address/
number (MVECEN = 1), scanning of all interrupts is not
necessary to determine the source of the interrupt.
When MVECEN = 1, Vectored interrupt controller
requires three clock cycles to vector to the ISR from
main routine, thereby removing dependency of
interrupt timing on compiled code.
There is a fixed latency of three instruction cycles
between the completion of the instruction active when
the interrupt occurred and the first instruction of the
Interrupt Service Routine. Figure 9-7, Figure 9-8 and
Figure 9-9 illustrate the sequence of events when a
peripheral interrupt is asserted when the last executed
instruction is one-cycle, two-cycle and three-cycle
respectively, when MVECEN = 1.
After the Interrupt Flag Status bit is set, the current
instruction completes executing. In the first latency
cycle, the contents of the PC, STATUS, WREG, BSR,
FSR0/1/2, PRODL/H and PCLATH/U registers are
context saved and the IVTBASE+ Vector number is
calculated. In the second latency cycle, the PC is
loaded with the calculated vector table address for the
interrupt source and the starting address of the ISR is
fetched. In the third latency cycle, the PC is loaded with
the ISR address. All the latency cycles are executed as
a FNOP instruction.
When MVECEN = 0, Vectored interrupt controller
requires two clock cycles to vector to the ISR from main
routine. There is a latency of two instruction cycles plus
the software latency between the completion of the
instruction active when the interrupt occurred and the
first instruction of the Interrupt Service Routine.


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 127
                                        FIGURE 9-7:             INTERRUPT TIMING DIAGRAM - ONE CYCLE INSTRUCTION
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                                      Rev. 10-000269A
                                                                                                                                                                                             9/12/2016

                                                                    1             2           3              4         5           6             7         8        9            10

                                                  System
                                                   Clock
                                                 Program
                                                                    X             X+2         X+2         0x82       0x218       0x21A         0x21C      X+2       X+4          X+6
                                                 Counter


                                                                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                                Instruction
                                                                               Inst @ X(1)   FNOP        FNOP        FNOP     Inst @ 0x218 Inst @ 0x21A   FNOP   Inst @ X+2   Inst @ X+4
                                                 Register
                                                                                                                                  BCF          RETFIE

                                                   Interrupt


                                                  Routine               MAIN                              FNOP                           ISR              FNOP            MAIN


                                                                    IVTBASE                            0x80

                                                                   Vector
                                                                                                         1
                                                                   Number
                                                              Program Memory
                                                                                                       0x86
                                                                    0x82

                                                                               Interrupt Location = Interrupt vector table entry << 2
                                                                                                  = 0x86 << 2 = 0x218


                                           Note 1: Instruction @ X is a One-cycle Instruction
DS40001919G-page 128
                                        FIGURE 9-8:             INTERRUPT TIMING DIAGRAM - TWO WORD INSTRUCTION
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                                                Rev. 10-000269B
                                                                                                                                                                                                       9/12/2016

                                                                        1            2            3          4           5       6           7              8       9        10           11

                                                      System
                                                       Clock
                                                      Program
                                                                        Y           Y+2          Y+2        Y+2         0x82   0x218        0x21A         0x21C    Y+2       Y+4          Y+6
                                                      Counter


                                                                                                                                                                                                                   PIC18(L)F26/27/45/46/47/55/56/57K42
                                                    Instruction
                                                                                  Inst @ Y(1) Inst @ Y(1)   FNOP        FNOP   FNOP    Inst @ 0x218 Inst @ 0x21A   FNOP   Inst @ Y+2 Inst @ Y+4
                                                     Register
                                                                                                                                            BCF           RETFIE

                                                       Interrupt


                                                      Routine                       MAIN                                FNOP                        ISR            FNOP            MAIN


                                                                        IVTBASE                                  0x80

                                                                       Vector
                                                                                                                  1
                                                                       Number
                                                                  Program Memory
                                                                                                                 0x86
                                                                        0x82

                                                                                   Interrupt Location = Interrupt vector table entry << 2
                                                                                                      = 0x86 << 2 = 0x218


                                            Note 1: Instruction @ Y is a Two-cycle instruction.
DS40001919G-page 129
                                        FIGURE 9-9:              INTERRUPT TIMING DIAGRAM - THREE CYCLE INSTRUCTION
 2017-2021 Microchip Technology Inc.


                                                                                                                                                                                                      Rev. 10-000269C
                                                                                                                                                                                                             9/12/2016

                                                                    1           2            3           4                5       6     7        8             9       10        11           12

                                                   System
                                                    Clock
                                                   Program
                                                                    Z           Z+2         Z+2         Z+2               Z+2   0x82   0x218   0x21A      0x21C        Z+2       Z+4          Z+6
                                                   Counter


                                                                                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                                 Instruction                                                                                   Inst @         Inst @
                                                                             Inst @ Z(1) Inst @ Z(1) Inst @ Z(1)        FNOP    FNOP   FNOP                            FNOP   Inst @ Z+2 Inst @ Z+4
                                                  Register                                                                                     0x218          0x21A
                                                                                                                                               BCF        RETFIE

                                                    Interrupt


                                                  Routine                           MAIN                                        FNOP                    ISR            FNOP            MAIN


                                                                     IVTBASE                                       0x80

                                                                    Vector
                                                                                                                    1
                                                                    Number
                                                               Program Memory
                                                                                                                   0x86
                                                                     0x82

                                                                                Interrupt Location = Interrupt vector table entry << 2
                                                                                                   = 0x86 << 2 = 0x218


                                          Note 1: Instruction @ Z is a Three-cycle instruction.
DS40001919G-page 130
                                        9.7.1       ABORTING INTERRUPTS
 2017-2021 Microchip Technology Inc.


                                        If the last instruction before the interrupt controller vectors to the ISR from main
                                        routine clears the GIE, PIE or PIR bit associated with the interrupt, the controller
                                        executes one force NOP cycle before it returns to the main routine.
                                        Figure 9-10 illustrates the sequence of events when a peripheral interrupt is
                                        asserted and then cleared on the last executed instruction cycle.
                                        If the GIE, PIE or PIR bit associated with the interrupt is cleared prior to


                                                                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                        vectoring to the ISR, then the controller continues executing the main routine.

                                        FIGURE 9-10:            INTERRUPT TIMING DIAGRAM - ABORTING INTERRUPTS


                                                                                                                                                                   Rev. 10-000269D
                                                                                                                                                                           7/6/2016


                                                                                                      1             2           3        4                5

                                                                                     Instruction
                                                                                       Clock
                                                                                     Program
                                                                                                      X             X+2        X+2       X+4             X+6
                                                                                     Counter
                                                                                    Instruction
                                                                                                                 Inst @ X(1)   FNOP   Inst @ X+2      Inst @ X+4
                                                                                     Register


                                                                                        Interrupt


                                                                                      Routine             MAIN                 FNOP            MAIN


                                                Note 1: Inst @ X clears the interrupt flag, Example BCF INTCON0, GIE.
DS40001919G-page 131
                        PIC18(L)F26/27/45/46/47/55/56/57K42
9.8          Interrupt Setup Procedure                       9.10     Wake-up from Sleep
1.    When using interrupt priority levels, set the IPEN     The interrupt controller provides a wake-up request to
      bit in INTCON0 register and then select the            the CPU whenever an interrupt event occurs, if the
      user-assigned priority level for the interrupt         interrupt event is enabled. This occurs regardless of
      source by writing the control bits in the              whether the part is in Run, Idle/Doze or Sleep modes.
      appropriate IPRx Control register.                     The status of the GIEH/GIEL bits has no effect on the
     Note:     At a device Reset, the IPRx registers are     wake-up request. The wake-up request will be
               initialized, such that all user interrupt     asynchronous to all clocks.
               sources are assigned to high priority.
                                                             9.11     Interrupt Compatibility
2.    Clear the Interrupt Flag Status bit associated
      with the peripheral in the associated PIRx Status      When the MVECEN bit in Configuration Word 2L is
      register.                                              cleared (Register 5-3), the Interrupt Vector Table
3.    Enable the interrupt source by setting the             feature is disabled and interrupts are compatible with
      interrupt enable control bit associated with the       previous high performance 8-bit PIC18 microcontroller
      source in the appropriate PIEx Control register.       devices. In this mode, the Interrupt Vector Table priority
4.    If the vector table is used (MVECEN = 1), then         has no effect.
      setup the start address for the Interrupt Vector       When the IPEN bit is also cleared, the interrupt priority
      Table using the IVTBASE register. See Section          feature is disabled and interrupts are compatible with
      9.2.2 “Interrupt Vector Table Contents”.               PIC®16 microcontroller mid-range devices. All
5.    Once the IVTBASE is written to, set the Interrupt      interrupts branch to address 0008h since the interrupt
      enable bits in INTCON0 register.                       priority is disabled.
6.    An example of setting up interrupts and ISRs
      using assembly and C can be found in
      Examples 9-3 and 9-4.

9.9          External Interrupt Pins
The PIC18(L)F26/27/45/46/47/55/56/57K42 devices
have three external interrupt sources which can be
assigned to any pin on different ports based on the PPS
settings. Refer Section 17.0 “Peripheral Pin Select
(PPS) Module” for possible rerouting options. The
external interrupt sources are edge-triggered. If the
corresponding INTxEDG bit in the INTCON0 register is
set (= 1), the interrupt is triggered by a rising edge. If
the bit is clear, the trigger is on the falling edge.
When a valid edge appears on the INTx pin, the
corresponding flag bit, INTxF in the PIRx registers, is
set. This interrupt can be disabled by clearing the
corresponding enable bit, INTxE. Flag bit, INTxF, must
be cleared by software in the Interrupt Service Routine
before re-enabling the interrupt.
All external interrupts (INT0, INT1 and INT2) can wake
up the processor from Idle or Sleep modes if bit INTxE
was set prior to going into those modes. If the Global
Interrupt Enable bit, GIE/GIEH, is set, the processor
will branch to the interrupt vector following wake-up.
Interrupt priority is determined by the value contained
in the interrupt priority bits, INT0IP, INT1IP and INT2IP
of the IPRx registers.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 132
                      PIC18(L)F26/27/45/46/47/55/56/57K42
EXAMPLE 9-3:           SETTING UP VECTORED INTERRUPTS USING MPASM
; Each ISR routine must have a predetermined origin otherwise there will be
; an assembly error because the address is not determined until link time
; which is too late to do the divide by 4 math on the address.
; Predetermined addresses must be evenly divisible by 4.

ISRCLC2 CODE     0x7E00
; CLC2 interrupt service code here.
   BANKSEL   PIR7
   BCF       PIR7, CLC2IF
   RETFIE    FAST

ISRTMR0 CODE     0x7E40
; Timer0 interrupt service code here.
   BANKSEL   PIR3
   BCF       PIR3, TMR0IF
   RETFIE    FAST

ISRTMR4 CODE     0x7E60
; Timer4 interrupt service code here.
   BANKSEL   PIR7
   BCF       PIR7, TMR4IF
   RETFIE    FAST

IntInit:
   ; Disable all interrupts
   BCF       INTCON0, GIE, ACCESS

    ; Set IVTBASE (optional - default is 0x000008)
    CLRF      IVTBASEU, ACCESS
    MOVLW     0x7F
    MOVWF     IVTBASEH, ACCESS
    CLRF      IVTBASEL, ACCESS

    ; Clear any interrupt flags before enabling interrupts
    BANKSEL   PIR7
    BCF       PIR7, CLC2IF
    BCF       PIR3, TMR0IF
    BCF       PIR7, TMR4IF

    ; Enable interrupts
    BANKSEL   PIE7
    BSF       PIE7, CLC2IE
    BSF       PIE3, TMR0IE
    BSF       PIE7, TMR4IE

    ; Set interrupt priorities if necessary
    BANKSEL   IPR7
    BSF       INTCON0, IPEN_INTCON0, ACCESS   ; Enable interrupt priority
    BCF       IPR7, CLC2IP                    ; Make CLC2 interrupt low priority

    ; Enable interrupts
    BSF     INTCON0, GIEH, ACCESS
    BSF     INTCON0, GIEL, ACCESS

    RETURN 1

; Save TMR0ISR in vector table (IVTBASE+31*2)
ISR1   CODE      0x7F3E
       DW        (0x7E40>>2)             ; (TMR0ISR/4)

; Save TMR4ISR in vector table (IVTBASE+56*2)
ISR2   CODE      0x7F70
       DW        (0x7E60>>2)             ; (TMR4ISR/4)

; Save CLC2ISR in vector table (IVTBASE+60*2)
ISR3   CODE      0x7F78
       DW        (0x7E00>>2)             ; (CLC2ISR/4)


 2017-2021 Microchip Technology Inc.                                              DS40001919G-page 133
                      PIC18(L)F26/27/45/46/47/55/56/57K42
EXAMPLE 9-4:           SETTING UP VECTORED INTERRUPTS USING XC8

 // NOTE 1: If IVTBASE is changed from its default value of 0x000008, then the
 // "base(...)" argument must be provided in the ISR. Otherwise the vector
 // table will be placed at 0x0008 by default regardless of the IVTBASE value.

 // NOTE 2: When MVECEN=0 and IPEN=1, a separate argument as "high_priority"
 // or "low_priority" can be used to distinguish between the two ISRs.
 // If the argument is not provided, the ISR is considered high priority
 // by default.

 // NOTE 3: Multiple interrupts can be handled by the same ISR if they are
 // specified in the "irq(...)" argument. Ex: irq(IRQ_TMR0, IRQ_CCP1)

 void __interrupt(irq(IRQ_TMR0), base(0x4008)) TMR0_ISR(void)
 {
         PIR3bits.TMR0IF = 0;                 // Clear the interrupt flag
         LATCbits.LC0 ^= 1;                   // ISR code goes here
 }

 void __interrupt(irq(default), base(0x4008)) DEFAULT_ISR(void)
 {
         // Unhandled interrupts go here
 }

 void INTERRUPT_Initialize (void)
 {
         INTCON0bits.GIEH = 1;                // Enable high priority interrupts
         INTCON0bits.GIEL = 1;                // Enable low priority interrupts
         INTCON0bits.IPEN = 1;                // Enable interrupt priority

          PIE3bits.TMR0IE = 1;                // Enable TMR0 interrupt
          PIE4bits.TMR1IE = 1;                // Enable TMR1 interrupt

          IPR3bits.TMR0IP = 0;                // Make TMR0 interrupt low priority

          // Change IVTBASE if required
          IVTBASEU = 0x00;                    // Optional
          IVTBASEH = 0x40;                    // Default is 0x0008
          IVTBASEL = 0x08;
 }


 2017-2021 Microchip Technology Inc.                                            DS40001919G-page 134
                      PIC18(L)F26/27/45/46/47/55/56/57K42
9.12      Register Definitions: Interrupt Control
REGISTER 9-1:          INTCON0: INTERRUPT CONTROL REGISTER 0
   R/W-0/0         R/W-0/0         R/W-0/0           U-0            U-0           R/W-1/1         R/W-1/1            R/W-1/1
  GIE/GIEH           GIEL            IPEN             —              —           INT2EDG         INT1EDG         INT0EDG
bit 7                                                                                                                     bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set               ‘0’ = Bit is cleared            x = Bit is unknown


bit 7            GIE/GIEH: Global Interrupt Enable bits
                 If IPEN = 0:
                 GIE:
                 1 = Enables all unmasked interrupts
                 0 = Disables all interrupts
                 If IPEN = 1:
                 GIEH:
                 1 = Enables all unmasked high priority interrupts: bit also needs to be set for enabling low priority
                      interrupts
                 0 = Disables all interrupts
bit 6            GIEL: Global Low Priority Interrupt Enable bit
                 If IPEN = 0:
                 Reserved, read as ‘0’
                 If IPEN = 1:
                 GIEL:
                 1 = Enables all unmasked low priority interrupts, GIEH also needs to be set for low priority interrupts
                 0 = Disables all low priority
bit 5            IPEN: Interrupt Priority Enable bit
                 1 = Enable priority levels on interrupts
                 0 = Disable priority levels on interrupts; all interrupts are treated as high priority interrupts
bit 4-3          Unimplemented: Read as ‘0’
bit 2            INT2EDG: External Interrupt 2 Edge Select bit
                 1 = Interrupt on rising edge of INT2 pin
                 0 = Interrupt on falling edge of INT2 pin
bit 1            INT1EDG: External Interrupt 1 Edge Select bit
                 1 = Interrupt on rising edge of INT1 pin
                 0 = Interrupt on falling edge of INT1 pin
bit 0            INT0EDG: External Interrupt 0 Edge Select bit
                 1 = Interrupt on rising edge of INT0 pin
                 0 = Interrupt on falling edge of INT0 pin


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 135
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-2:             INTCON1: INTERRUPT CONTROL REGISTER 1
        R-0/0           R-0/0           U-0             U-0       U-0           U-0            U-0             U-0
            STAT[1:0]                   —               —          —             —                 —           —

bit 7                                                                                                                bit 0


Legend:
HC = Bit is cleared by hardware
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         q = Value depends on condition


bit 7-6            STAT[1:0]: Interrupt State Status bits
                   11 = High priority ISR executing, high priority interrupt was received while a low priority ISR was
                        executing
                   10 = High priority ISR executing, high priority interrupt was received in main routine
                   01 = Low priority ISR executing, low priority interrupt was received in main routine
                   00 = Main routine executing
bit 5-0            Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 136
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-3:              PIR0: PERIPHERAL INTERRUPT REQUEST REGISTER 0
        R-0/0        R/W/HS-0/0      R/W/HS-0/0 R/W/HS-0/0 R/W/HS-0/0              R/W/HS-0/0    R/W/HS-0/0       R/W-0/0
   IOCIF(2)             CRCIF          SCANIF          NVMIF        CSWIF(3)         OSFIF         HLVDIF          SWIF
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                    W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared          HS = Bit is set in hardware


bit 7                IOCIF: Interrupt-on-Change Interrupt Flag bit(2)
                     1 = Interrupt has occurred
                     0 = Interrupt event has not occurred
bit 6                CRCIF: CRC Interrupt Flag bit
                     1 = Interrupt has occurred (must be cleared by software)
                     0 = Interrupt event has not occurred
bit 5                SCANIF: Memory Scanner Interrupt Flag bit
                     1 = Interrupt has occurred (must be cleared by software)
                     0 = Interrupt event has not occurred
bit 4                NVMIF: NVM Interrupt Flag bit
                     1 = Interrupt has occurred (must be cleared by software)
                     0 = Interrupt event has not occurred
bit 3                CSWIF: Clock Switch Interrupt Flag bit(3)
                     1 = Interrupt has occurred (must be cleared by software)
                     0 = Interrupt event has not occurred
bit 2                OSFIF: Oscillator Fail Interrupt Flag bit
                     1 = Interrupt has occurred (must be cleared by software)
                     0 = Interrupt event has not occurred
bit 1                HLVDIF: HLVD Interrupt Flag bit
                     1 = Interrupt has occurred (must be cleared by software)
                     0 = Interrupt event has not occurred
bit 0                SWIF: Software Interrupt Flag bit
                     1 = Interrupt will trigger (bit is set and cleared by user software)
                     0 = Interrupt event has not occurred
Note 1:         Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
                enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
                prior to enabling an interrupt.
         2:     IOCIF is a read-only bit. To clear the interrupt condition, all bits in the IOCxF registers must be cleared.
         3:     The CSWIF interrupt will not wake the system from Sleep. The system will sleep until another interrupt
                causes the wake-up.


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 137
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-4:           PIR1: PERIPHERAL INTERRUPT REQUEST REGISTER 1
 R/W/HS-0/0        R/W/HS-0/0    R/W/HS-0/0 R/W/HS-0/0 R/W/HS-0/0             R/W/HS-0/0      R/W/HS-0/0     R/W/HS-0/0
 SMT1PWAIF         SMT1PRAIF       SMT1IF               C1IF      ADTIF           ADIF           ZCDIF        INT0IF(2)
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared          HS = Bit is set in hardware


bit 7              SMT1PWAIF: SMT1 Pulse-Width Acquisition Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 6              SMT1PRAIF: SMT1 Period Acquisition Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 5              SMT1IF: SMT1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 4              C1IF: CMP1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 3              ADTIF: ADC Threshold Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 2              ADIF: ADC Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 1              ZCDIF: ZCD Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              INT0IF: External Interrupt 0 Interrupt Flag bit(2)
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
Note 1:      Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
             enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
             prior to enabling an interrupt.
        2:   The external interrupt GPIO pin is selected by the INTxPPS register.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 138
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-5:             PIR2: PERIPHERAL INTERRUPT REGISTER 2(1)
    R-0/0             R-0/0        R-0/0           R-0/0     R/W/HS-0/0       R/W/HS-0/0     R/W/HS-0/0       R/W/HS-0/0
I2C1RXIF(2)         SPI1IF(3)   SPI1TXIF(4) SPI1RXIF(4)       DMA1AIF         DMA1ORIF      DMA1DCNTIF DMA1SCNTIF
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                W = Writable bit            U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown          -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared        HS = Hardware set


bit 7              I2C1RXIF: I2C1 Receive Interrupt Flag bit(2)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 6              SPI1IF: SPI1 Interrupt Flag bit(3)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 5              SPI1TXIF: SPI1 Transmit Interrupt Flag bit(4)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 4              SPI1RXIF: SPI1 Receive Interrupt Flag bit(4)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 3              DMA1AIF: DMA1 Abort Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 2              DMA1ORIF: DMA1 Overrun Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 1              DMA1DCNTIF: DMA1 Destination Count Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              DMA1SCNTIF: DMA1 Source Count Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
Note 1:      Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
             enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
             prior to enabling an interrupt.
        2:   I2CxTXIF and I2CxRXIF are read-only bits. To clear the interrupt condition, the CLRBF bit in I2CxSTAT1
             register must be set.
        3:   SPIxIF is a read-only bit. To clear the interrupt condition, all bits in the SPIxINTF register must be cleared.
        4:   SPIxTXIF and SPIxRXIF are read-only bits and cannot be set/cleared by the software.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 139
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-6:            PIR3: PERIPHERAL INTERRUPT REGISTER 3(1)
 R/W/HS-0/0           R-0/0           R-0/0              R-0/0       R-0/0         R-0/0          R-0/0           R-0/0
   TMR0IF             U1IF(2)       U1EIF(3)       U1TXIF(4)       U1RXIF(4)     I2C1EIF(5)      I2C1IF(6)    I2C1TXIF(7)
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared           HS = Bit is set in hardware


bit 7              TMR0IF: TMR0 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 6              U1IF: UART1 Interrupt Flag bit(2)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 5              U1EIF: UART1 Framing Error Interrupt Flag bit(3)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 4              U1TXIF: UART1 Transmit Interrupt Flag bit(4)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 3              U1RXIF: UART1 Receive Interrupt Flag bit(4)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 2              I2C1EIF: I2C1 Error Interrupt Flag bit(5)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 1              I2C1IF: I2C1 Interrupt Flag bit(6)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 0              I2C1TXIF: I2C1 Transmit Interrupt Flag bit(7)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
Note 1:      Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
             enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
             prior to enabling an interrupt.
        2:   UxIF is a read-only bit. To clear the interrupt condition, all bits in the UxUIR register must be cleared.
        3:   UxEIF is a read-only bit. To clear the interrupt condition, all bits in the UxERRIR register must be cleared.
        4:   UxTXIF and UxRXIF are read-only bits and cannot be set/cleared by the software.
        5:   I2CxEIF is a read-only bit. To clear the interrupt condition, all bits in the I2CxERR register must be cleared.
        6:   I2CxIF is a read-only bit. To clear the interrupt condition, all bits in the I2CxPIR register must be cleared.
        7:   I2CxTXIF and I2CxRXIF are read-only bits. To clear the interrupt condition, the CLRBF bit in I2CxSTAT1
             register must be set.


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 140
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-7:           PIR4: PERIPHERAL INTERRUPT REGISTER 4(1)
 R/W/HS-0/0        R/W/HS-0/0    R/W/HS-0/0             U-0    R/W/HS-0/0     R/W/HS-0/0      R/W/HS-0/0     R/W/HS-0/0
    CLC1IF           CWG1IF        NCO1IF               —        CCP1IF         TMR2IF         TMR1GIF         TMR1IF
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared         HS = Bit is set in hardware


bit 7              CLC1IF: CLC1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 6              CWG1IF: CWG1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 5              NCO1IF: NCO1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 4              Unimplemented: Read as ‘0’
bit 3              CCP1IF: CCP1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 2              TMR2IF: TMR2 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 1              TMR1GIF: TMR1 Gate Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              TMR1IF: TMR1 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
Note 1:      Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
             enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
             prior to enabling an interrupt.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 141
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-8:              PIR5: PERIPHERAL INTERRUPT REGISTER 5(1)
    R-0/0             R-0/0          R/W/HS-0/0        R/W/HS-0/0    R/W/HS-0/0      R/W/HS-0/0    R/W/HS-0/0 R/W/HS-0/0
             (2)              (2)
I2C2TXIF           I2C2RXIF           DMA2AIF          DMA2ORIF     DMA2DCNTIF DMA2SCNTIF                C2IF     INT1IF(3)
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                    W = Writable bit                U = Unimplemented bit, read as ‘0’
u = Bit is unchanged                x = Bit is unknown              -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                    ‘0’ = Bit is cleared            HS = Bit is set in hardware


bit 7              I2C2TXIF: I2C2 Transmit Interrupt Flag bit(2)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 6              I2C2RXIF: I2C2 Receive Interrupt Flag bit(2)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 5              DMA2AIF: DMA2 Abort Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 4              DMA2ORIF: DMA2 Overrun Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 3              DMA2DCNTIF: DMA2 Destination Count Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 2              DMA2SCNTIF: DMA2 Source Count Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 1              C2IF: C2 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              INT1IF: External Interrupt 1 Interrupt Flag bit(3)
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
Note 1:       Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
              enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
              prior to enabling an interrupt.
        2:     I2CxTXIF and I2CxRXIF are read-only bits. To clear the interrupt condition, the CLRBF bit in I2CxSTAT1
              register must be set.
        3:     The external interrupt GPIO pin is selected by the INTxPPS register.


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 142
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-9:            PIR6: PERIPHERAL INTERRUPT REGISTER 6(1)
 R/W/HS-0/0        R/W/HS-0/0         R-0/0              R-0/0      R-0/0          R-0/0          R-0/0           R-0/0
   TMR3GIF           TMR3IF          U2IF(2)         U2EIF(3)     U2TXIF(4)      U2RXIF(4)      I2C2EIF(5)      I2C2IF(6)
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared           HS = Bit is set in hardware


bit 7              TMR3GIF: TMR3 Gate Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 6              TMR3IF: TMR3 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 5              U2IF: UART2 Interrupt Flag bit(2)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 4              U2EIF: UART2 Framing Error Interrupt Flag bit(3)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 3              U2TXIF: UART2 Transmit Interrupt Flag bit(4)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 2              U2RXIF: UART2 Receive Interrupt Flag bit(4)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 1              I2C2EIF: I2C2 Error Interrupt Flag bit(5)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
bit 0              I2C2IF: I2C2 Interrupt Flag bit(6)
                   1 = Interrupt has occurred
                   0 = Interrupt event has not occurred
Note 1:      Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
             enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
             prior to enabling an interrupt.
        2:   UxIF is a read-only bit. To clear the interrupt condition, all bits in the UxUIR register must be cleared.
        3:   UxEIF is a read-only bit. To clear the interrupt condition, all bits in the UxERRIR register must be cleared.
        4:   UxTXIF and UxRXIF are read-only bits and cannot be set/cleared by the software.
        5:   I2CxEIF is a read-only bit. To clear the interrupt condition, all bits in the I2CxERR register must be cleared.
        6:   I2CxIF is a read-only bit. To clear the interrupt condition, all bits in the I2CxPIR register must be cleared.


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 143
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-10:            PIR7: PERIPHERAL INTERRUPT REGISTER 7(1)
        U-0              U-0       R/W/HS-0/0 R/W/HS-0/0 R/W/HS-0/0                 U-0         R/W/HS-0/0     R/W/HS-0/0
        —                —           INT2IF(2)        CLC2IF      CWG2IF             —            CCP2IF         TMR4IF
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                   W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged               x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                   ‘0’ = Bit is cleared         HS = Bit is set in hardware


bit 7-6             Unimplemented: Read as ‘0’
bit 5               INT2IF: External Interrupt 2 Interrupt Flag bit(2)
                    1 = Interrupt has occurred (must be cleared by software)
                    0 = Interrupt event has not occurred
bit 4               CLC2IF: CLC2 Interrupt Flag bit
                    1 = Interrupt has occurred (must be cleared by software)
                    0 = Interrupt event has not occurred
bit 3               CWG2IF: CWG2 Interrupt Flag bit
                    1 = Interrupt has occurred (must be cleared by software)
                    0 = Interrupt event has not occurred
bit 2               Unimplemented: Read as ‘0’
bit 1               CCP2IF: CCP2 Interrupt Flag bit
                    1 = Interrupt has occurred (must be cleared by software)
                    0 = Interrupt event has not occurred
bit 0               TMR4IF: TMR4 Interrupt Flag bit
                    1 = Interrupt has occurred (must be cleared by software)
                    0 = Interrupt event has not occurred
Note 1:        Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
               enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
               prior to enabling an interrupt.
          2:    The external interrupt GPIO pin is selected by the INTxPPS register.


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 144
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-11:           PIR8: PERIPHERAL INTERRUPT REGISTER 8(1)
 R/W/HS-0/0        R/W/HS-0/0           U-0              U-0        U-0            U-0             U-0            U-0
   TMR5GIF           TMR5IF             —                —           —              —               —              —

bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         HS = Bit is set in hardware


bit 7              TMR5GIF: TMR5 Gate Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 6              TMR5IF: TMR5 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 5-0            Unimplemented: Read as ‘0’
Note 1:       Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
              enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
              prior to enabling an interrupt.


REGISTER 9-12:           PIR9: PERIPHERAL INTERRUPT REGISTER 9(1)
        U-0             U-0             U-0              U-0    R/W/HS-0/0     R/W/HS-0/0      R/W/HS-0/0     R/W/HS-0/0
        —               —               —                —        CLC3IF         CWG3IF          CCP3IF         TMR6IF
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3              CLC3IF: CLC3 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 2              CWG3IF: CWG3 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 1              CCP3IF: CCP3 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              TMR6IF: TMR6 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
Note 1:       Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
              enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
              prior to enabling an interrupt.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 145
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-13:           PIR10: PERIPHERAL INTERRUPT REGISTER 10(1)
        U-0             U-0             U-0              U-0        U-0            U-0         R/W/HS-0/0     R/W/HS-0/0
        —               —               —                —           —              —            CLC4IF         CCP4IF
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                  W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared         HS = Bit is set in hardware


bit 7-2            Unimplemented: Read as ‘0’
bit 1              CLC4IF: CLC4 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              CCP4IF: CCP4 Interrupt Flag bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
Note 1:       Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its corresponding
              enable bit, or the global enable bit. User software may ensure the appropriate interrupt flag bits are clear
              prior to enabling an interrupt.


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 146
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-14:           PIE0: PERIPHERAL INTERRUPT ENABLE REGISTER 0
   R/W-0/0           R/W-0/0        R/W-0/0          R/W-0/0       R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
     IOCIE            CRCIE         SCANIE           NVMIE         CSWIE          OSFIE         HLVDIE           SWIE
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              IOCIE: Interrupt-on-Change Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              CRCIE: CRC Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              SCANIE: Memory Scanner Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              NVMIE: NVM Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              CSWIE: Clock Switch Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              OSFIE: Oscillator Fail Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              HLVDIE: HLVD Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              SWIE: Software Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 147
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-15:           PIE1: PERIPHERAL INTERRUPT ENABLE REGISTER 1
   R/W-0/0           R/W-0/0        R/W-0/0         R/W-0/0      R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
 SMT1PWAIE SMT1PRAIE                SMT1IE              C1IE     ADTIE           ADIE          ZCDIE          INT0IE
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              SMT1PWAIE: SMT1 Pulse Width Acquisition Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              SMT1PRAIE: SMT1 Period Acquisition Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              SMT1IE: SMT1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              C1IE: C1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              ADTIE: ADC Threshold Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              ADIE: ADC Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              ZCDIE: ZCD Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              INT0IE: External Interrupt 0 Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 148
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-16:             PIE2: PERIPHERAL INTERRUPT ENABLE REGISTER 2
  R/W-0/0           R/W-0/0       R/W-0/0        R/W-0/0      R/W-0/0        R/W-0/0        R/W-0/0        R/W-0/0
 I2C1RXIE            SPI1IE      SPI1TXIE       SPI1RXIE     DMA1AIE       DMA1ORIE       DMA1DCNTIE DMA1SCNTIE
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                W = Writable bit           U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown         -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7              I2C1RXIE: I2C1 Receive Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              SPI1IE: SPI1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              SPI1TXIE: SPI1 Transmit Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              SPI1RXIE: SPI1 Receive Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              DMA1AIE: DMA1 Abort Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              DMA1ORIE: DMA1 Overrun Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              DMA1DCNTIE: DMA1 Destination Count Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              DMA1SCNTIE: DMA1 Source Count Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 149
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-17:           PIE3: PERIPHERAL INTERRUPT ENABLE REGISTER 3
   R/W-0/0           R/W-0/0        R/W-0/0         R/W-0/0       R/W-0/0     R/W-0/0        R/W-0/0        R/W-0/0
   TMR0IE              U1IE          U1EIE          U1TXIE        U1RXIE      I2C1EIE         I2C1IE        I2C1TXIE
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              TMR0IE: TMR0 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              U1IE: UART1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              U1EIE: UART1 Framing Error Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              U1TXIE: UART1 Transmit Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              U1RXIE: UART1 Receive Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              I2C1EIE: I2C1 Error Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              I2C1IE: I2C1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              I2C1TXIE: I2C1 Transmit Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 150
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-18:          PIE4: PERIPHERAL INTERRUPT ENABLE REGISTER 4
   R/W-0/0           R/W-0/0       R/W-0/0             U-0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
    CLC1IE          CWG1IE         NCO1IE              —       CCP1IE        TMR2IE        TMR1GIE         TMR1IE
bit 7                                                                                                            bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7              CLC1IE: CLC1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              CWG1IE: CWG1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              NCO1IE: NCO1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              Unimplemented: Read as ‘0’
bit 3              CCP1IE: CCP1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              TMR2IE: TMR2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              TMR1GIE: TMR1 Gate Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              TMR1IE: TMR1 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 151
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-19:             PIE5: PERIPHERAL INTERRUPT ENABLE REGISTER 5
  R/W-0/0           R/W-0/0        R/W-0/0             R/W-0/0      R/W-0/0         R/W-0/0       R/W-0/0        R/W-0/0
 I2C2TXIE           I2C2RXIE       DMA2AIE         DMA2ORIE       DMA2DCNTIE DMA2SCNTIE                C2IE      INT1IE
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit                W = Writable bit                  U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown                -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7              I2C2TXIE: I2C2 Transmit Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              I2C2RXIE: I2C2 Receive Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              DMA2AIE: DMA2 Abort Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              DMA2ORIE: DMA2 Overrun Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              DMA2DCNTIE: DMA2 Destination Count Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              DMA2SCNTIE: DMA2 Source Count Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              C2IE: C2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              INT1IE: External Interrupt 1 Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                                  DS40001919G-page 152
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-20:           PIE6: PERIPHERAL INTERRUPT ENABLE REGISTER 6
   R/W-0/0           R/W-0/0        R/W-0/0         R/W-0/0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
  TMR3GIE            TMR3IE          U2IE           U2EIE       U2TXIE        U2RXIE         I2C2EIE         I2C2IE
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              TMR3GIE: TMR3 Gate Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              TMR3IE: TMR3 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5              U2IE: UART2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              U2EIE: UART2 Framing Error Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              U2TXIE: UART2 Transmit Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              U2RXIE: UART2 Receive Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              I2C2EIE: I2C2 Error Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              I2C2IE: I2C2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 153
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-21:           PIE7: PERIPHERAL INTERRUPT ENABLE REGISTER 7
        U-0            U-0          R/W-0/0         R/W-0/0     R/W-0/0         U-0          R/W-0/0        R/W-0/0
        —               —            INT2IE         CLC2IE     CWG2IE            —           CCP2IE         TMR4IE
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5              INT2IE: External Interrupt 2 Enable bit
                   1 = Enabled
                   0 = Disabled
bit 4              CLC2IE: CLC2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 3              CWG2IE: CWG2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              Unimplemented: Read as ‘0’
bit 1              CCP2IE: CCP2 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              TMR4IE: TMR4 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 154
                       PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-22:          PIE8: PERIPHERAL INTERRUPT ENABLE REGISTER 8
   R/W-0/0           R/W-0/0            U-0            U-0       U-0           U-0            U-0             U-0
  TMR5GIE            TMR5IE             —              —          —             —                 —           —

bit 7                                                                                                               bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7              TMR5GIE: TMR5 Gate Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 6              TMR5IE: TMR5 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 5-0            Unimplemented: Read as ‘0’


REGISTER 9-23:          PIE9: PERIPHERAL INTERRUPT ENABLE REGISTER 9
        U-0            U-0              U-0            U-0     R/W-0/0       R/W-0/0        R/W-0/0        R/W-0/0
        —               —               —              —       CLC3IE        CWG3IE         CCP3IE         TMR6IE
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3              CLC3IE: CLC3 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 2              CWG3IE: CWG3 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 1              CCP3IE: CCP3 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled
bit 0              TMR6IE: TMR6 Interrupt Enable bit
                   1 = Enabled
                   0 = Disabled


 2017-2021 Microchip Technology Inc.                                                             DS40001919G-page 155
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-24:          PIE10: PERIPHERAL INTERRUPT ENABLE REGISTER 10
        U-0            U-0              U-0             U-0       U-0           U-0          R/W-0/0        R/W-0/0
        —               —               —               —          —             —           CLC4IE          CCP4IE
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-2            Unimplemented: Read as ‘0’
bit 1              CLC4IE: CLC4 Interrupt Enable bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred
bit 0              CCP4IE: CCP4 Interrupt Enable bit
                   1 = Interrupt has occurred (must be cleared by software)
                   0 = Interrupt event has not occurred


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 156
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-25:           IPR0: PERIPHERAL INTERRUPT PRIORITY REGISTER 0
   R/W-1/1           R/W-1/1         R/W-1/1         R/W-1/1         R/W-1/1       R/W-1/1        R/W-1/1        R/W-1/1
     IOCIP            CRCIP          SCANIP          NVMIP           CSWIP          OSFIP         HLVDIP           SWIP
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                  W = Writable bit                 U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown               -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              IOCIP: Interrupt-on-Change Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              CRCIP: CRC Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              SCANIP: Memory Scanner Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              NVMIP: NVM Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              CSWIP: Clock Switch Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              OSFIP: Oscillator Fail Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              HLVDIP: HLVD Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              SWIP: Software Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                                   DS40001919G-page 157
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-26:           IPR1: PERIPHERAL INTERRUPT PRIORITY REGISTER 1
   R/W-1/1           R/W-1/1         R/W-1/1          R/W-1/1      R/W-1/1       R/W-1/1        R/W-1/1        R/W-1/1
 SMT1PWAIP SMT1PRAIP                 SMT1IP              C1IP       ADTIP          ADIP          ZCDIP          INT0IP
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              SMT1PWAIP: SMT1 Pulse Width Acquisition Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              SMT1PRAIP: SMT1 Period Acquisition Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              SMT1IP: SMT1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              C1IP: C1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              ADTIP: ADC Threshold Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              ADIP: ADC Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              ZCDIP: ZCD Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              INT0IP: External Interrupt 0 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 158
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-27:             IPR2: PERIPHERAL INTERRUPT PRIORITY REGISTER 2
  R/W-1/1           R/W-1/1        R/W-1/1        R/W-1/1         R/W-1/1      R/W-1/1        R/W-1/1        R/W-1/1
 I2C1RXIP            SPI1IP       SPI1TXIP       SPI1RXIP         DMA1AIP    DMA1ORIP      DMA1DCNTIP DMA1SCNTIP
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                 W = Writable bit            U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown          -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              I2C1RXIP: I2C1 Receive Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              SPI1IP: SPI1 Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              SPI1TXIP: I2C1 Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              SPI1RXIP: SPI1 Receive Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              DMA1AIP: DMA1 Abort Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              DMA1ORIP: DMA1 Overrun Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              DMA1DCNTIP: DMA1 Destination Count Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              DMA1SCNTIP: DMA1 Source Count Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 159
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-28:           IPR3: PERIPHERAL INTERRUPT PRIORITY REGISTER 3
   R/W-1/1           R/W-1/1         R/W-1/1         R/W-1/1        R/W-1/1     R/W-1/1        R/W-1/1        R/W-1/1
   TMR0IP              U1IP           U1EIP          U1TXIP         U1RXIP      I2C1EIP         I2C1IP        I2C1TXIP
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              TMR0IP: TMR0 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              U1IP: UART1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              U1EIP: UART1 Framing Error Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              U1TXIP: UART1 Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              U1RXIP: UART1 Receive Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              I2C1EIP: I2C1 Error Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              I2C1IP: I2C1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              I2C1TXIP: I2C1 Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 160
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-29:           IPR4: PERIPHERAL INTERRUPT PRIORITY REGISTER 4
   R/W-1/1           R/W-1/1        R/W-1/1             U-0      R/W-1/1       R/W-1/1        R/W-1/1        R/W-1/1
    CLC1IP           CWG1IP         NCO1IP              —        CCP1IP        TMR2IP        TMR1GIP         TMR1IP
bit 7                                                                                                              bit 0


Legend:
R = Readable bit                 W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              CLC1IP: CLC1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              CWG1IP: CWG1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              NCO1IP: NCO1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              Unimplemented: Read as ‘0’
bit 3              CCP1IP: CCP1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              TMR2IP: TMR2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              TMR1GIP: TMR1 Gate Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              TMR1IP: TMR1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 161
                           PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-30:             IPR5: PERIPHERAL INTERRUPT PRIORITY REGISTER 5
  R/W-1/1            R/W-1/1        R/W-1/1             R/W-1/1          R/W-1/1      R/W-1/1       R/W-1/1        R/W-1/1
 I2C2TXIP           I2C2RXIP        DMA2AIP          DMA2ORIP       DMA2DCNTIP DMA2SCNTIP                C2IP      INT1IP
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                 W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7              I2C2TXIP: I2C2 Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              I2C2RXIP: I2C2 Receive Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              DMA2AIP: DMA2 Abort Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              DMA2ORIP: DMA2 Overrun Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              DMA2DCNTIP: DMA2 Destination Count Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              DMA2SCNTIP: DMA2 Source Count Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              C2IP: C2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              INT1IP: External Interrupt 1 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 162
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-31:           IPR6: PERIPHERAL INTERRUPT PRIORITY REGISTER 6
   R/W-1/1           R/W-1/1         R/W-1/1         R/W-1/1      R/W-1/1       R/W-1/1        R/W-1/1        R/W-1/1
  TMR3GIP            TMR3IP            U2IP          U2EIP        U2TXIP        U2RXIP         I2C2EIP         I2C2IP
bit 7                                                                                                               bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown            -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              TMR3GIP: TMR3 Gate Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              TMR3IP: TMR3 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5              U2IP: UART2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              U2EIP: UART2 Framing Error Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              U2TXIP: UART2 Transmit Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              U2RXIP: UART2 Receive Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              I2C2EIP: I2C2 Error Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              I2C2IP: I2C2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 163
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-32:           IPR7: PERIPHERAL INTERRUPT PRIORITY REGISTER 7
        U-0             U-0          R/W-1/1         R/W-1/1       R/W-1/1         U-0          R/W-1/1        R/W-1/1
        —                —            INT2IP         CLC2IP        CWG2IP           —           CCP2IP         TMR4IP
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7-6            Unimplemented: Read as ‘0’
bit 5              INT2IP: External Interrupt 2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 4              CLC2IP: CLC2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 3              CWG2IP: CWG2 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              Unimplemented: Read as ‘0’
bit 1              CCP2IP: CRC Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              TMR4IP: TMR4 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


REGISTER 9-33:           IPR8: PERIPHERAL INTERRUPT PRIORITY REGISTER 8
   R/W-1/1           R/W-1/1            U-0              U-0             U-0       U-0            U-0             U-0
  TMR5GIP            TMR5IP             —                —               —          —                 —           —

bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged              x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                  ‘0’ = Bit is cleared


bit 7              TMR5GIP: TMR5 Gate Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 6              TMR5IP: TMR5 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 5-0            Unimplemented: Read as ‘0’


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 164
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-34:           IPR9: PERIPHERAL INTERRUPT PRIORITY REGISTER 9
        U-0            U-0              U-0             U-0     R/W-1/1       R/W-1/1        R/W-1/1        R/W-1/1
        —               —               —               —       CLC3IP        CWG3IP         CCP3IP         TMR6IP
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-4            Unimplemented: Read as ‘0’
bit 3              CLC3IP: CLC3 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 2              CWG3IP: CWG3 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 1              CCP3IP: CCP3 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              TMR6IP: TMR6 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


REGISTER 9-35:           IPR10: PERIPHERAL INTERRUPT PRIORITY REGISTER 10
        U-0            U-0              U-0             U-0       U-0           U-0          R/W-0/0        R/W-0/0
        —               —               —               —          —             —           CLC4IP          CCP4IP
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-2            Unimplemented: Read as ‘0’
bit 1              CLC4IP: CLC4 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority
bit 0              CCP4IP: CCP4 Interrupt Priority bit
                   1 = High priority
                   0 = Low priority


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 165
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-36:           IVTBASEU: INTERRUPT VECTOR TABLE BASE ADDRESS UPPER REGISTER
        U-0            U-0            U-0           R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
        —               —               —                                   BASE[20:16]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            BASE[20:16]: Interrupt Vector Table Base Address bits


REGISTER 9-37:           IVTBASEH: INTERRUPT VECTOR TABLE BASE ADDRESS HIGH REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0     R/W-0/0       R/W-0/0       R/W-0/0         R/W-0/0
                                                        BASE[15:8]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            BASE[15:8]: Interrupt Vector Table Base Address bits


REGISTER 9-38:           IVTBASEL: INTERRUPT VECTOR TABLE BASE ADDRESS LOW REGISTER
   R/W-0/0           R/W-0/0       R/W-0/0          R/W-0/0     R/W-1/1       R/W-0/0       R/W-0/0         R/W-0/0
                                                        BASE[7:0]
bit 7                                                                                                             bit 0


Legend:
R = Readable bit                 W = Writable bit             U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown           -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            BASE[7:0]: Interrupt Vector Table Base Address bits


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 166
                        PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-39:           IVTADU: INTERRUPT VECTOR TABLE ADDRESS UPPER REGISTER
        U-0            U-0            U-0               R-0/0             R-0/0      R-0/0          R-0/0          R-0/0
        —               —               —                                          AD[20:16]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                 W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-5            Unimplemented: Read as ‘0’
bit 4-0            AD[20:16]: Interrupt Vector Table Address bits


REGISTER 9-40:           IVTADH: INTERRUPT VECTOR TABLE ADDRESS HIGH REGISTER
     R-0/0            R-0/0          R-0/0              R-0/0             R-0/0      R-0/0          R-0/0          R-0/0
                                                            AD[15:8]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                 W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            AD[15:8]: Interrupt Vector Table Address bits


REGISTER 9-41:           IVTADL: INTERRUPT VECTOR TABLE ADDRESS LOW REGISTER
     R-0/0            R-0/0          R-0/0              R-0/0             R-1/1      R-0/0          R-0/0          R-0/0
                                                                AD[7:0]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                 W = Writable bit                   U = Unimplemented bit, read as ‘0’
u = Bit is unchanged             x = Bit is unknown                 -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                 ‘0’ = Bit is cleared


bit 7-0            AD[7:0]: Interrupt Vector Table Address bits


 2017-2021 Microchip Technology Inc.                                                                    DS40001919G-page 167
                         PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 9-42:              IVTLOCK: INTERRUPT VECTOR TABLE LOCK REGISTER
        U-0            U-0           U-0               U-0         U-0             U-0          U-0           R/W-0/0
        —               —             —                —            —                  —         —         IVTLOCKED(1,2)
bit 7                                                                                                                  bit 0


Legend:
R = Readable bit                W = Writable bit               U = Unimplemented bit, read as ‘0’
u = Bit is unchanged            x = Bit is unknown             -n/n = Value at POR and BOR/Value at all other Resets
‘1’ = Bit is set                ‘0’ = Bit is cleared


bit 7-1            Unimplemented: Read as ‘0’
bit 0              IVTLOCKED: IVT Registers Lock bits(1,2)
                   1 = IVTBASE Registers are locked and cannot be written
                   0 = IVTBASE Registers can be modified by write operations

Note 1:       The IVTLOCK bit can only be set or cleared after the unlock sequence in Example 9-1.
     2:       If IVT1WAY = 1, the IVTLOCK bit cannot be cleared after it has been set. See Register 5-3.


REGISTER 9-43:              SHADCON: SHADOW CONTROL REGISTER
        U-0             U-0             U-0             U-0          U-0               U-0           U-0       R/W-0/0
         —               —                —                —          —                    —          —        SHADLO
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented bit, read as ‘0’
-n = Value at POR                 ‘1’ = Bit is set              ‘0’ = Bit is cleared           x = Bit is unknown


bit 7-1             Unimplemented: Read as ‘0’
bit 0               SHADLO: Interrupt Shadow Register Access Switch bit
                    0 = Access Main Context for Interrupt Shadow Registers
                    1 = Access Low-Priority Interrupt Context for Interrupt Shadow Registers


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 168
                           PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 9-3:          SUMMARY OF REGISTERS ASSOCIATED WITH INTERRUPTS
                                                                                                                                   Register
  Name         Bit 7               Bit 6     Bit 5           Bit 4              Bit 3            Bit 2      Bit 1         Bit 0
                                                                                                                                   on Page

INTCON0     GIE/GIEH               GIEL      IPEN              —                  —
                                                                                           INT2EDG        INT1EDG       INT0EDG     135
INTCON1                STAT[1:0]               —               —                  —               —          —             —        136
PIE0          IOCIE            CRCIE        SCANIE          NVMIE           CSWIE            OSFIE         HLVDIE         SWIE      147
PIE1       SMT1PWAIE        SMT1PRAIE       SMT1IE           C1IE            ADTIE           ADIE          ZCDIE         INT0IE     148
PIE2        I2C1RXIE           SPI1IE      SPI1TXIE       SPI1RXIE         DMA1AIE        DMA1ORIE       DMA1DCNTIE DMA1SCNTIE      149
PIE3         TMR0IE                U1IE     U1EIE           U1TXIE          U1RXIE          I2C1EIE        I2C1IE       I2C1TXIE    150
PIE4         CLC1IE           CWG1IE       NCO1IE              —
                                                                            CCP1IE          TMR2IE        TMR1GIE        TMR1IE     151
PIE5        I2C2TXIE         I2C2RXIE      DMA2AIE        DMA2ORIE       DMA2DCNTIE DMA2SCNTIE              C2IE         INT1IE     152
PIE6        TMR3GIE           TMR3IE         U2IE           U2EIE           U2TXIE          U2RXIE        I2C2EIE        I2C2IE     153
PIE7            —                   —       INT2IE          CLC2IE         CWG2IE                 —        CCP2IE        TMR4IE     154
PIE8        TMR5GIE           TMR5IE           —               —                  —               —          —             —
                                                                                                                                    155
PIE9            —                   —          —               —
                                                                            CLC3IE          CWG3IE         CCP3IE        TMR6IE     155
PIE10           —                   —          —               —                  —               —        CLC4IE        CCP4IE     156
PIR0          IOCIF            CRCIF        SCANIF          NVMIF           CSWIF            OSFIF         HLVDIF         SWIF      137
PIR1       SMT1PWAIF        SMT1PRAIF       SMT1IF           C1IF            ADTIF               ADIF      ZCDIF         INT0IF     138
PIR2        I2C1RXIF           SPI1IF      SPI1TXIF        SPI1RXIF        DMA1AIF        DMA1ORIF       DMA1DCNTIF DMA1SCNTIF      139
PIR3         TMR0IF                U1IF     U1EIF           U1TXIF          U1RXIF          I2C1EIF        I2C1IF       I2C1TXIF    140
PIR4         CLC1IF           CWG1IF       NCO1IF              —
                                                                            CCP1IF          TMR2IF        TMR1GIF        TMR1IF     141
PIR5         I2C2TXF          I2C2RXF      DMA2AIF        DMA2ORIF       DMA2DCNTIF DMA2SCNTIF              C2IF         INT1IF     142
PIR6        TMR3GIF           TMR3IF         U2IF           U2EIF           U2TXIF          U2RXIF         I2C2EIF       I2C2IF     143
PIR7            —                   —       INT2IF          CLC2IF          CWG2IF                —        CCP2IF        TMR4IF     144
PIR8        TMR5GIF           TMR5IF           —               —                  —               —          —             —
                                                                                                                                    145
PIR9            —                   —          —               —
                                                                            CLC3IF          CWG3IF         CCP3IF        TMR6IF     145
PIR10           —                   —          —               —                  —               —
                                                                                                           CLC4IF        CCP4IF     146
IPR0          IOCIP            CRCIP        SCANIP          NVMIP           CSWIP            OSFIP         HLVDIP         SWIP      157
IPR1       SMT1PWAIP        SMT1PRAIP       SMT1IP           C1IP            ADTIP           ADIP          ZCDIP         INT0IP     158
IPR2         I2C1RIP           SPI1IP      SPI1TIP         SPI1RIP         DMA1AIP        DMA1ORIP       DMA1DCNTIP DMA1SCNTIP      159
IPR3         TMR0IP                U1IP     U1EIP           U1TXIP          U1RXIP          I2C1EIP        I2C1IP       I2C1TXIP    160
IPR4         CLC1IP           CWG1IP       NCO1IP              —            CCP1IP          TMR2IP        TMR1GIP        TMR1IP     161
IPR5         I2C2TXP          I2C2RXP      DMA2AIP        DMA2ORIP       DMA2DCNTIP DMA2SCNTIP              C2IP         INT1IP     162
IPR6        TMR3GIP           TMR3IP         U2IP           U2EIP           U2TXIP          U2RXIP        I2C2EIP        I2C2IP     163
IPR7            —                   —       INT2IP          CLC2IP         CWG2IP                 —        CCP2IP        TMR4IP     164
IPR8        TMR5GIP           TMR5IP           —               —                  —               —          —             —        164
IPR9            —                   —          —               —            CLC3IP          CWG3IP         CCP3IP        TMR6IP     165
IPR10           —                   —          —               —                  —               —
                                                                                                           CLC4IP        CCP4IP     165
IVTBASEU        —                   —          —                                          BASE[20:16]                               166
IVTBASEH                                                             BASE[15:8]                                                     166
IVTBASEL                                                             BASE[7:0]                                                      166
IVTADU                                                                                     AD[20:16]                                167
IVTADH                                                                AD[15:8]                                                      167
IVTADL                                                                AD[7:0]                                                       167
IVTLOCK         —                   —         —               —                  —                —          —         IVTLOCKED    168
Legend:     — = unimplemented locations, read as ‘0’. Shaded bits are not used for interrupts.


 2017-2021 Microchip Technology Inc.                                                                                DS40001919G-page 169
