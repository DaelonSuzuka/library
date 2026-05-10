                                                                                                      PIC18F27/47/57Q43
                                                                                        VIC - Vectored Interrupt Controller
                                                                                                                   Module

11.    VIC - Vectored Interrupt Controller Module
11.1   Overview
       The Vectored Interrupt Controller (VIC) module reduces the numerous peripheral interrupt request
       signals to a single interrupt request signal to the CPU. This module includes the following major
       features:
       •   Interrupt Vector Table (IVT) with a unique vector for each interrupt source
       •   Fixed and ensured interrupt latency
       •   Programmable base address for IVT with lock
       •   Two user-selectable priority levels: high-priority and low-priority
       •   Two levels of context saving
       •   Interrupt state Status bits to indicate the current execution status of the CPU
       The VIC module assembles all of the interrupt request signals and resolves the interrupts based
       on both a fixed natural order priority (i.e., determined by the IVT) and a user-assigned priority (i.e.,
       determined by the IPRx registers), thereby eliminating scanning of interrupt sources.

11.2   Interrupt Control and Status Registers
       The devices in this family implement the following registers for the interrupt controller:
       •   INTCON0, INTCON1 Control Registers
       •   PIRx - Peripheral Interrupt Status Registers
       •   PIEx - Peripheral Interrupt Enable Registers
       •   IPRx - Peripheral Interrupt Priority Registers
       •   IVTBASE Address Registers
       •   IVTLOCK Register
       Global interrupt control functions and external interrupts are controlled from the INTCON0 register.
       The INTCON1 register contains the status flags for the interrupt controller.
       The PIRx registers contain all of the interrupt request flags. Each source of interrupt has a Status
       bit, which is set by the respective peripherals or an external signal and is either cleared via software
       or automatically cleared by hardware upon clearing of the interrupt condition, depending on the
       peripheral and bit.
       The PIEx registers contain all of the interrupt enable bits. These control bits are used to individually
       enable interrupts from the peripherals or external signals.
       The IPRx registers are used to set the interrupt priority level for each source of interrupt. Each user
       interrupt source can be assigned to either a high or low priority.
       The IVTBASE register is user-programmable and is used to determine the start address of the IVT
       and the IVTLOCK register is used to prevent any unintended writes to the IVTBASE register.
       There are two other Configuration bits that control the way the interrupt controller can be
       configured: The MVECEN and the IVT1WAY bits.
       The MVECEN bit determines whether the IVT is used to determine the interrupt priorities. The
       IVT1WAY bit determines the number of times the IVTLOCKED bit can be cleared and set after a
       device Reset. See the Interrupt Vector Table Address Calculation section for details.

11.3   Interrupt Vector Table
       The interrupt controller supports an IVT that contains the vector address location for each interrupt
       request source.


--- p118 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        VIC - Vectored Interrupt Controller
                                                                                                                   Module
        The IVT resides in program memory, starting at the address location determined by IVTBASE. The IVT
        contains one vector for each source of interrupt. Each interrupt vector location contains the starting
        address of the associated Interrupt Service Routine (ISR). The MVECEN Configuration bit controls the
        availability of the vector table.

11.3.1 Interrupt Vector Table Base Address (IVTBASE)
        The start address of the vector table is user-programmable through the IVTBASE. The user must
        ensure the start address is such that it can encompass the entire vector table inside the program
        memory.
        Each vector address is a 16-bit word (or two address locations on PIC18 devices). For ‘n’ interrupt
        sources, there are ‘2n’ address locations necessary to hold the table, starting from IVTBASE as the
        first location. Thus, the starting address needs to be chosen such that the address range from
        IVTBASE to “IVTBASE+2n-1” can be encompassed within the program Flash memory.
        For example, if the highest vector number was 81, IVTBASE needs to be chosen such that
        “IVTBASE+0xA1” is less than the last memory location in program Flash memory.
        A programmable vector table base address is useful in situations to switch between different sets of
        vector tables, depending on the application. It can also be used when the application program needs
        to update the existing vector table (vector address values).


                    Important: It is required that the user assign an even address to IVTBASE for
                    correct operation.


11.3.2 Interrupt Vector Table Contents
        MVECEN = 0
        When MVECEN = 0, the address location pointed to by IVTBASE has a GOTO instruction for a high-
        priority interrupt. Similarly, the corresponding low-priority vector also has a GOTO instruction, which
        is executed in case of a low-priority interrupt.
        MVECEN = 1
        When MVECEN = 1, the value in the vector table of each interrupt points to the address location
        of the first instruction of the Interrupt Service Routine, hence: ISR Location = Interrupt Vector Table
        entry << 2.

11.3.3 Interrupt Vector Table Address Calculation
        MVECEN = 0
        When the MVECEN Configuration bit is cleared, the address pointed to by IVTBASE is used as
        the high-priority interrupt vector address. The low-priority interrupt vector address is offset eight
        instruction words from the address in IVTBASE.
        For PIC18 devices, IVTBASE defaults to 000008h, hence the high-priority interrupt vector address will
        be 000008h and the low-priority interrupt vector address will be 000018h.
        MVECEN = 1
        Each interrupt has a unique vector number associated with it, as defined in the IVT. This vector
        number is used for calculating the location of the interrupt vector for a particular interrupt source.
        Interrupt Vector Address = IVTBASE + (2*Vector Number). This calculated interrupt vector address
        value is stored in the IVTAD register when an interrupt is received.
        User-assigned software priority, when assigned using the IPRx registers, does not affect address
        calculation and is only used to resolve concurrent interrupts.


--- p119 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
                     Important: If for any reason the address of the ISR cannot be fetched from the
                     vector table, it will cause the system to reset and clear the Memory Execution
                     Violation flag in the Power Control register. This can occur due to any one of the
                     following:
                     • The entry for the interrupt in the vector table lies outside the executable
                         program memory area
                     •   ISR pointed by the vector table lies outside the executable program memory
                         area


        Table 11-1. IVT Calculations Summary
                    IVT Address Calculation                        Interrupt Priority INTCON0 Register, IPEN Bit
                                                                          0                                 1
                                               0                        IVTBASE                   High-priority IVTBASE
              Multivector Enable,
                                                                                             Low-priority IVTBASE + 8 words
            MVECEN Configuration bit
                                               1                              IVTBASE + 2*(Vector Number)


11.3.4 Access Control for IVTBASE Registers
        The interrupt controller has an IVTLOCKED bit, which can be set to avoid inadvertent changes to the
        contents of IVTBASE. Setting and clearing this bit requires a special sequence as an extra precaution
        against inadvertent changes.
        To allow writes to IVTBASE, the interrupts must be disabled (GIEH = 0) and the IVTLOCKED bit must
        be cleared. The user must follow the sequence shown below to clear the IVTLOCKED bit.

                Example 11-1. IVT Unlock Sequence

                 ; Disable Interrupts:
                     BCF INTCON0, GIE;

                 ; Bank to IVTLOCK register
                     BANKSEL IVTLOCK;
                     MOVLW 55h;

                 ; Required sequence, next 4 instructions
                     MOVWF IVTLOCK;
                     MOVLW AAh;
                     MOVWF IVTLOCK;

                 ; Clear IVTLOCKED bit to enable writes
                     BCF IVTLOCK, IVTLOCKED;

                 ; Enable Interrupts
                     BSF INTCON0, GIE;


        The user must follow the following sequence to set the IVTLOCKED bit.

                Example 11-2. IVT Lock Sequence

                 ; Disable Interrupts:
                     BCF INTCON0, GIE;

                 ; Bank to IVTLOCK register
                     BANKSEL IVTLOCK;
                     MOVLW 55h;

                 ; Required sequence, next 4 instructions
                     MOVWF IVTLOCK;
                     MOVLW AAh;
                     MOVWF IVTLOCK;

                 ; Set IVTLOCKED bit to enable writes


--- p120 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        VIC - Vectored Interrupt Controller
                     BSF IVTLOCK, IVTLOCKED;                                                                       Module

                 ; Enable Interrupts
                     BSF INTCON0, GIE;


        When the IVT1WAY Configuration bit is set, the IVTLOCKED bit can be cleared and set only once after
        a device Reset. The unlock operation will have no effect after the lock sequence is used to set the
        IVTLOCKED bit. Unlocking is inhibited until a system Reset occurs.

11.4    Interrupt Priority
        The final priority level for any pending source of interrupt is determined first by the user-assigned
        priority of that source in the IPRx register, then by the natural order priority within the IVT. The
        sections below detail the operation of interrupt priorities.

11.4.1 User (Software) Priority
        User-assigned interrupt priority is enabled by setting IPEN. Each peripheral interrupt source can be
        assigned a high- or low-priority level by the user. The user-assignable interrupt priority control bits
        for each interrupt are located in the IPRx registers, which are device-specific and can be found in the
        respective data sheet for each device.
        The interrupts are serviced based on a predefined interrupt priority scheme detailed below.
        1. Interrupts set by the user as a high-priority interrupt have higher precedence of execution.
           High-priority interrupts will override a low-priority request when:
           a. A low-priority interrupt has been requested or its request is already pending.
           b. A low- and high-priority interrupt are triggered concurrently (i.e., on the same instruction
              cycle).(1)
           c. A low-priority interrupt was requested and the corresponding Interrupt Service Routine is
              currently executing. In this case, the lower priority interrupt routine will be interrupted then
              complete executing after the high-priority interrupt has been serviced.(2)
        2. Interrupts set by the user as low priority have a lower priority of execution and are preempted by
           any high-priority interrupt.
        3. Interrupts defined with the same software priority cannot preempt or interrupt each other.
           Concurrent pending interrupts with the same user priority are resolved using the natural order
           priority (when vectored interrupts are enabled) or in the order the interrupt flag bits are polled in
           the ISR (when vectored interrupts are disabled).


                    Important:
                    1. When a high-priority interrupt preempts a concurrent low-priority interrupt,
                       GIEL may be cleared in the high-priority Interrupt Service Routine. If GIEL is
                       cleared, the low-priority interrupt will NOT be serviced, even if it was originally
                       requested. The corresponding interrupt flag needs to be cleared in user code.
                    2. When a high-priority interrupt is requested while a low-priority Interrupt
                       Service Routine is executing, GIEL may be cleared in the high-priority Interrupt
                       Service Routine. The pending low-priority interrupt will resume, even if GIEL is
                       cleared.


11.4.2 Natural Order (Hardware) Priority
        When vectored interrupts are enabled and more than one interrupt with the same user specified
        priority level is requested, the priority conflict is resolved by using a method called “Natural Order
        Priority”. Natural order priority is a fixed priority scheme that is based on the IVT.


--- p121 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
Table 11-2. Interrupt Vector Priority Table
                                                                      Vector                      Interrupt
  Vector                          Interrupt                          Number                        source
 Number                            source
                                                                      (cont.)                       (cont.)

    0x0                      Software Interrupt                        0x3E                      PWM3RINT
    0x1              HLVD (High/Low-Voltage Detect)                    0x3F                  PWM3GINT
    0x2                    OSF (Oscillator Fail)                       0x40                     U2RX
    0x3                   CSW (Clock Switching)                        0x41                     U2TX
    0x4                               -                                0x42                      U2E
    0x5               CLC1 (Configurable Logic Cell)                   0x43                      U2
    0x6                               -                                0x44                     TMR5
    0x7                 IOC (Interrupt-On-Change)                      0x45                    TMR5G
    0x8                             INT0                               0x46                     CCP2
    0x9                 ZCD (Zero-Cross Detection)                     0x47                     SCAN
    0xA              AD (ADC Conversion Complete)                      0x48                     U3RX
    0xB                  ACT (Active Clock Tuning)                     0x49                     U3TX
    0xC                     CM1 (Comparator)                           0x4A                      U3E
   0xD              SMT1 (Signal Measurement Timer)                    0x4B                      U3
    0xE                          SMT1PRA                               0x4C                       -
    0xF                          SMT1PWA                               0x4D                     CLC4
   0x10                             ADT                             0x4E - 0x4F                   -
0x11 - 0x13                           -                                0x50                     INT2
   0x14             DMA1SCNT (Direct Memory Access)                    0x51                     CLC5
   0x15                         DMA1DCNT                               0x52     CWG2 (Complementary Waveform Generator)
   0x16                          DMA1OR                                0x53                     NCO2
   0x17                           DMA1A                                0x54                  DMA3SCNT
   0x18             SPI1RX (Serial Peripheral Interface)               0x55                  DMA3DCNT
   0x19                            SPI1TX                              0x56                   DMA3OR
   0x1A                             SPI1                               0x57                    DMA3A
   0x1B                            TMR2                                0x58                     CCP3
   0x1C                            TMR1                                0x59                     CLC6
   0x1D                           TMR1G                                0x5A                    CWG3
   0x1E              CCP1 (Capture/Compare/PWM)                        0x5B                     TMR4
   0x1F                             TMR0                               0x5C                      DMA4SCNT
   0x20                             U1RX                               0x5D                      DMA4DCNT
   0x21                             U1TX                               0x5E                       DMA4OR
   0x22                              U1E                               0x5F                        DMA4A
   0x23                              U1                                0x60                         U4RX
0x24 - 0x25                           -                                0x61                         U4TX
   0x26                          PWM1RINT                              0x62                         U4E
   0x27                          PWM1GINT                              0x63                          U4
   0x28                           SPI2RX                               0x64                      DMA5SCNT
   0x29                            SPI2TX                              0x65                      DMA5DCNT
   0x2A                             SPI2                               0x66                       DMA5OR
   0x2B                               -                                0x67                        DMA5A
   0x2C                            TMR3                                0x68                         U5RX
   0x2D                           TMR3G                                0x69                         U5TX
   0x2E                          PWM2RINT                              0x6A                         U5E


--- p122 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
  ...........continued
                                                                  Vector                        Interrupt
    Vector                       Interrupt                       Number                          source
   Number                         source
                                                                  (cont.)                         (cont.)

       0x2F                     PWM2GINT                           0x6B                             U5
       0x30                       INT1                        0x6C                              DMA6SCNT
       0x31                       CLC2                        0x6D                              DMA6DCNT
       0x32     CWG1 (Complementary Waveform Generator)       0x6E                               DMA6OR
       0x33       NCO1 (Numerically Controlled Oscillator)    0x6F                                DMA6A
       0x34                   DMA2SCNT                        0x70                                   -
       0x35                   DMA2DCNT                        0x71                                 CLC7
       0x36                    DMA2OR                         0x72                                 CM2
       0x37                     DMA2A                         0x73                                 NCO3
       0x38                     I2C1RX                     0x74 - 0x77                               -
       0x39                     I2C1TX                        0x78                                 NVM
       0x3A                       I2C1                        0x79                                 CLC8
       0x3B                      I2C1E                        0x7A                    CRC (Cyclic Redundancy Check)
       0x3C                         -                         0x7B                                 TMR6
       0x3D                       CLC3                     0x7C - 0x8F                               -

         The natural order priority scheme goes from high-to-low with increasing vector numbers, with 0
         being the highest priority and decreasing from there.
         For example, when two concurrently occurring interrupt sources that are both designated high
         priority, using the IPRx register will be resolved using the natural order priority (i.e., the interrupt
         with a lower corresponding vector number will preempt the interrupt with the higher vector
         number).
         The ability for the user to assign every interrupt source to high- or low-priority levels means that the
         user program can give an interrupt with a low natural priority, a higher overall priority level.

11.5     Interrupt Operation
         All pending interrupts are indicated by their respective flag bit being equal to a ‘1’ in the PIRx
         register. All pending interrupts are resolved using the priority scheme explained in the Interrupt
         Priority section.
         Once the interrupt source to be serviced is resolved, the program execution vectors to the resolved
         interrupt vector addresses, as explained in Interrupt Vector Table section. The vector number is
         also stored in the WREG register. Most of the flag bits are required to be cleared by the application
         software, but in some cases, device hardware clears the interrupt automatically. Some flag bits
         are read-only in the PIRx registers. These flags are a summary of the source interrupts, and the
         corresponding interrupt flags of the source must be cleared.
         A valid interrupt can be either a high- or low-priority interrupt when in the main routine or a
         high-priority interrupt when in a low-priority Interrupt Service Routine. Depending on the order of
         interrupt requests received and their relative timing, the CPU will be in a state of execution indicated
         by the STAT bit.
         The state machine shown in Figure 11-1 and the subsequent sections detail the execution of
         interrupts when received in different orders.


--- p123 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
                          Important: The state of GIEH/L is not changed by the hardware when servicing
                          an interrupt. The internal state machine is used to keep track of execution states.
                          These bits can be manipulated in the user code, resulting in transferring execution
                          to the main routine and ignoring existing interrupts.


        Figure 11-1. Vectored Interrupts State Transition Diagram

                                                                                                                                                              Rev. 10-000265A
                                                                                                                                                                      7/6/2016


                                                                     MAIN
                                                                  INTSTAT = 00


                                                              High Interrupt addressed,
         High Interrupt                                        Low Interrupt pending                                                                    Low Interrupt
                                 HIGH                                                                               LOW
           requested         INTSTAT = 10                                                                       INTSTAT = 01                              requested
                                                              Low Interrupt addressed,
                                                               High Interrupt pending


                                                                                                                          High Interrupt addressed,
                                                                                             High Interrupt requested,
                                                                                              Low Interrupt pending


                                                                                                                           Low Interrupt pending
                                                                                                               HIGH                                     High Interrupt
                                                                                                            INTSTAT = 11                                  requested


11.5.1 Serving a High- or Low-Priority Interrupt While the Main Routine Code Is Executing
        When a high- or low-priority interrupt is requested while the main routine code is executing, the
        main routine execution is halted and the ISR is addressed. Upon a return from the ISR (by executing
        the RETFIE instruction), the main routine resumes execution.


--- p124 ---
                                                                                                                             PIC18F27/47/57Q43
                                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                                          Module
        Figure 11-2. Interrupt Execution: High/Low-Priority Interrupt While Executing Main Routine

                                                                                                                                                Rev. 10-000267A
                                                                                                                                                       9/12/2016


                                                                              ISR Code Executing

                                                                                                                RETFIE Executed

         Main Code       Main Code Executing                           Main Code Execution Halted                         Main Code Executing


            Interrupt

                                                  Interrupt     Interrupt
                                                  received       cleared


11.5.2 Serving a High-Priority Interrupt While a Low-Priority Interrupt Is Pending
        A high-priority interrupt request will always take precedence over any interrupt of a lower priority.
        The high-priority interrupt is acknowledged first, then the low-priority interrupt is acknowledged.
        Upon a return from the high-priority ISR (by executing the RETFIE instruction), the low-priority
        interrupt is serviced.
        If any other high-priority interrupts are pending and enabled, they are serviced before servicing the
        pending low-priority interrupt. If no other high-priority interrupt requests are active, the low-priority
        interrupt is serviced.

        Figure 11-3. Interrupt Execution: High-Priority Interrupt with a Low-Priority Interrupt Pending

                                                                                                                                                Rev. 10-000267C
                                                                                                                                                       9/12/2016


           High ISR                                                High ISR
                                                                                            RETFIE Executed

           Low ISR                                                                                  Low ISR
                                                                                                              RETFIE Executed

         Main Code        Main routine                                  Main Code Execution Halted                    Main routine

         High Priority
            Interrupt
                                           High Interrupt     High Interrupt
                                              received           cleared
         Low Priority
            Interrupt
                                                       Low Interrupt                         Low Interrupt
                                                         received                               cleared


11.5.3 Preempting Low-Priority Interrupts
        Low-priority interrupts can be preempted by high-priority interrupts. While in the low-priority ISR, if
        a high-priority interrupt arrives, the high-priority interrupt request is generated and the low-priority
        ISR is suspended, while the high-priority ISR is executed.
        After the high-priority ISR is complete and if any other high-priority interrupt requests are not active,
        the execution returns to the preempted low-priority ISR.


--- p125 ---
                                                                                                                                  PIC18F27/47/57Q43
                                                                                                                    VIC - Vectored Interrupt Controller
                                                                                                                                               Module
        Figure 11-4. Interrupt Execution: High-Priority Interrupt Preempting Low-Priority Interrupts

                                                                                                                                                Rev. 10-000267B
                                                                                                                                                       9/12/2016


          High ISR                                                              High ISR
                                           Low Interrupt pending,                                 RETFIE Executed
                                           High Interrupt received
          Low ISR                                         Low ISR      Low ISR Execution Halted     Low ISR
                                                                                                                RETFIE Executed

        Main Code         Main routine                                Main Code Execution Halted                         Main routine

        High Priority
           Interrupt
                                                          High Interrupt     High Interrupt
                                                             received           cleared
        Low Priority
           Interrupt
                                         Low Interrupt       Low Interrupt
                                           received            cleared


11.5.4 Simultaneous High- and Low-Priority Interrupts
        When both high- and low-priority interrupts are active in the same instruction cycle (i.e.,
        simultaneous interrupt events), both the high- and low-priority requests are generated. The high-
        priority ISR is serviced first before servicing the low-priority interrupt.

        Figure 11-5. Interrupt Execution: Simultaneous High- and Low-Priority Interrupts

                                                                                                                                                Rev. 10-000267D
                                                                                                                                                       9/12/2016


          High ISR                                               High ISR
                                                                                           RETFIE Executed

          Low ISR                                                                                   Low ISR
                                                                                                                RETFIE Executed

        Main Code         Main routine                                Main Code Execution Halted                         Main routine

        High Priority
           Interrupt
                                         High Interrupt        High Interrupt
                                            received              cleared
        Low Priority
           Interrupt
                                            Low Interrupt                                     Low Interrupt
                                              received                                          cleared


11.6    Context Saving
        The interrupt controller supports a two-level deep context saving system (main routine context and
        low ISR context). Refer to the state machine shown in Figure 11-6 for details.
        The Program Counter (PC) is saved on the dedicated device PC stack. The CPU registers saved
        include STATUS, WREG, BSR, FSR0/1/2, PRODL/H and PCLATH/U.
        After WREG has been saved to the context registers, the resolved vector number of the interrupt
        source to be serviced is copied into WREG. Context save and restore operation is completed by the
        interrupt controller based on the current state of the interrupts and the order in which they were
        sent to the CPU.


--- p126 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        VIC - Vectored Interrupt Controller
                                                                                                                   Module
       Context save/restore works the same way in both states of MVECEN. When IPEN = 0, there is only
       one level of interrupt active. Hence, only the main context is saved when an interrupt is received.

11.6.1 Accessing Shadow Registers
       The interrupt controller automatically saves the context information in the shadow registers. Both
       the saved context values (i.e., main routine and low ISR) can be accessed using the same set of
       shadow registers. By clearing SHADLO, the CPU register values saved for main routine context can
       be accessed. Low ISR context is automatically restored to the CPU registers upon exiting the high
       ISR. Similarly, the main context is automatically restored to the CPU registers upon exiting the low
       ISR.
       The shadow registers are readable and writable, so if the user desires to modify the context, then
       the corresponding shadow register needs to be modified and the value will be restored when exiting
       the ISR. Depending on the user’s application, other registers may also need to be saved.

       Figure 11-6. Context Save State Machine Diagram

                                                                                                                                             Rev. 10-000266A
                                                                                                                                                     7/6/2016


                                                                 MAIN
                                                              INTSTAT = 00


                                                          No Context Save/Restore
         No Context        HIGH                                                                     LOW                                  No Context
        Save/Restore   INTSTAT = 10                                                             INTSTAT = 01                            Save/Restore
                                                          No Context Save/Restore


                                                                                                               Restore Low context
                                                                                            Save Low context


                                                                                               HIGH                                      No Context
                                                                                            INTSTAT = 11                                Save/Restore


11.7   Returning from Interrupt Service Routine (ISR)
       The Return from Interrupt (RETFIE) instruction is used to mark the end of an ISR.
       When the RETFIE 1 instruction is executed, the PC is loaded with the saved PC value from the top
       of the PC stack. Saved context is also restored with the execution of this instruction. Thus, execution
       returns to the state of operation that existed before the interrupt occurred.
       When the RETFIE 0 instruction is executed, the saved context is not restored back to the registers.

11.8   Interrupt Latency
       When MVECEN = 1, there is a fixed latency of three instruction cycles between the completion of
       the instruction active when the interrupt occurred and the first instruction of the Interrupt Service
       Routine. Figure 11-7, Figure 11-8 and Figure 11-9 illustrate the sequence of events when a peripheral


--- p127 ---
                                                                                                                             PIC18F27/47/57Q43
                                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                                          Module
interrupt is asserted, when the last executed instruction is one-cycle, two-cycle and three-cycle,
respectively.
After the Interrupt Flag Status bit is set, the current instruction completes executing. In the first
latency cycle, the contents of the PC, STATUS, WREG, BSR, FSR0/1/2, PRODL/H and PCLATH/U
registers are context saved, and the IVTBASE + Vector number is calculated. In the second latency
cycle, the PC is loaded with the calculated vector table address for the interrupt source, and the
starting address of the ISR is fetched. In the third latency cycle, the PC is loaded with the ISR address.
All the latency cycles are executed as NOP instructions.
When MVECEN = 0, the interrupt controller requires two clock cycles to vector to the ISR from the
main routine. Note that, as this mode requires additional software to determine which interrupt
source caused the interrupt, the actual latency between the trigger and the beginning of the specific
ISR for each individual interrupt will be longer than two clock cycles and will vary, when not using
vectored interrupts.

Figure 11-7. Interrupt Timing Diagram: One-Cycle Instruction

                                                                                                                                              Rev. 10-000 269A
                                                                                                                                                      1/4/201 9

                    1             2             3               4        5              6             7          8           9           10

  System
   Clock
 Program
                    X             X+2          X+2           0x82      0x218          0x21A         0x21C        X+2        X+4          X+6
 Counter
Instruction
                               Inst @ X(1)    FNOP          FNOP       FNOP        Inst @ 0x218 Inst @ 0x21A    FNOP     Inst @ X+2   Inst @ X+4
 Register
                                                                                       BCF          RETFIE

   Interrupt


  Routine               MAIN                                 FNOP                             ISR               FNOP              MAIN


                    IVTBASE                                0x80

                     Vector
                                                            1
                    Number
              Program Memory
                                                           0x86
                    0x82

                               Interrupt Location = Interrupt vector table entry << 2
                                                  = 0x86 << 2 = 0x218
  Note: 1. Instruction @ X is a One-cycle Instruction.


--- p128 ---
                                                                                                                                                                 PIC18F27/47/57Q43
                                                                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                                                                              Module
       Figure 11-8. Interrupt Timing Diagram: Two-Cycle Instruction

                                                                                                                                                                                     Rev. 10-000 269B
                                                                                                                                                                                             1/4/201 9

                            1              2            3            4                5              6              7                 8               9         10            11

          System
           Clock
          Program
                            Y           Y+2            Y+2           Y+2             0x82          0x218         0x21A              0x21C            Y+2        Y+4           Y+6
          Counter
        Instruction
                                     Inst @ Y(1) Inst @ Y(1)       FNOP              FNOP          FNOP        Inst @ 0x218 Inst @ 0x21A            FNOP     Inst @ Y+2 Inst @ Y+4
         Register
                                                                                                                  BCF               RETFIE

           Interrupt


           Routine                         MAIN                                      FNOP                                     ISR                   FNOP              MAIN


                            IVTBASE                                      0x80

                             Vector
                                                                           1
                            Number
                      Program Memory
                                                                         0x86
                            0x82

                                       Interrupt Location = Interrupt vector table entry << 2
                                                          = 0x86 << 2 = 0x218
            Note: 1. Instruction @ Y is a Two-cycle Instruction.


       Figure 11-9. Interrupt Timing Diagram: Three-Cycle Instruction

                                                                                                                                                                                     Rev. 10-000 269C
                                                                                                                                                                                             1/4/201 9

                           1           2           3           4                5             6            7              8                9          10        11           12

          System
           Clock
          Program
                           Z           Z+2        Z+2          Z+2             Z+2          0x82         0x218          0x21A         0x21C           Z+2       Z+4          Z+6
          Counter
        Instruction                                                                                                     Inst @            Inst @
                                   Inst @ Z(1) Inst @ Z(1) Inst @ Z(1)         FNOP         FNOP         FNOP                                        FNOP    Inst @ Z+2 Inst @ Z+4
         Register                                                                                                       0x218             0x21A
                                                                                                                        BCF           RETFIE

           Interrupt


         Routine                           MAIN                                             FNOP                                    ISR               FNOP            MAIN


                            IVTBASE                                      0x80

                             Vector
                                                                           1
                            Number
                      Program Memory
                                                                         0x86
                            0x82

                                       Interrupt Location = Interrupt vector table entry << 2
                                                          = 0x86 << 2 = 0x218
                          Note: 1. Instruction @ Z is a Three-cycle Instruction.


11.8.1 Aborting Interrupts
       If the last instruction before the interrupt controller vectors to the ISR from the main routine
       clears the GIE, PIE, or PIR bit associated with the interrupt, the controller executes one forced NOP
       instruction cycle before it returns to the main routine.
       Figure 11-10 illustrates the sequence of events when a peripheral interrupt is asserted and then
       cleared on the last executed instruction cycle.


--- p129 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                      VIC - Vectored Interrupt Controller
                                                                                                                                 Module
       If the GIE, PIE or PIR bit associated with the interrupt is cleared prior to vectoring to the ISR, then the
       controller continues executing the main routine.

       Figure 11-10. Interrupt Timing Diagram: Aborting Interrupts

                                                                                                                         Rev. 10-000 269D
                                                                                                                                 1/4/201 9


                                  1             2            3                  4            5

               Instruction
                 Clock
                Program
                                  X             X+2          X+2                X+4          X+6
                Counter
              Instruction
                                             Inst @ X(1)    FNOP          Inst @ X+2     Inst @ X+4
               Register


                  Interrupt


                Routine               MAIN                  FNOP                      MAIN


              Note: 1. Inst @ X clears the interrupt flag, Example BCF INTCON0, GIE.


11.9   Interrupt Setup Procedure
       1. When using interrupt priority levels, set IPEN and then select the user-assigned priority level for
          the interrupt source by writing the control bits in the appropriate IPRx control register.


                             Important: At a device Reset, the IPRx registers are initialized such that all
                             user interrupt sources are assigned to high priority.


       2. Clear the Interrupt Flag Status bit associated with the peripheral in the associated PIRx STATUS
          register.
       3. Enable the interrupt source by setting the interrupt enable control bit associated with the source
          in the appropriate PIEx register.
       4. If the vector table is used (MVECEN = 1), then set up the start address for the Interrupt Vector
          Table using IVTBASE. See the Interrupt Vector Table Contents section for more details.
       5. Once IVTBASE is written to, set the interrupt enable bits in INTCON0.
       6. An example of setting up interrupts and ISRs can be found below.


--- p130 ---
                                                                                                      PIC18F27/47/57Q43
                                                                                        VIC - Vectored Interrupt Controller
                                                                                                                   Module
               Example 11-3. Setting Up Vectored Interrupts Using XC8

                // NOTE 1: If IVTBASE is changed from its default value of 0x000008, then the
                // "base(...)" argument must be provided in the ISR. Otherwise the vector
                // table will be placed at 0x0008 by default regardless of the IVTBASE value.

                // NOTE 2: When MVECEN=0 and IPEN=1, a separate argument as "high_priority"
                // or "low_priority" can be used to distinguish between the two ISRs.
                // If the argument is not provided, the ISR is considered high priority
                // by default.

                // NOTE 3: Multiple interrupts can be handled by the same ISR if they are
                // specified in the "irq(...)" argument. Ex: irq(IRQ_SW, IRQ_HLVD)

                void __interrupt(irq(IRQ_SW), base(0x3008)) SW_ISR(void)
                {
                    PIR0bits.SWIF = 0;    // Clear the interrupt flag
                    LATCbits.LATC0 ^= 1;    // ISR code goes here
                }
                void __interrupt(irq(default), base(0x3008)) DEFAULT_ISR(void)
                {
                    // Unhandled interrupts go here
                }
                void INTERRUPT_Initialize (void)
                {
                    INTCON0bits.GIEH = 1;    // Enable high priority interrupts
                    INTCON0bits.GIEL = 1;    // Enable low priority interrupts
                    INTCON0bits.IPEN = 1;    // Enable interrupt priority
                    PIE0bits.SWIE = 1;     // Enable SW interrupt
                    PIE0bits.HLVDIE = 1;     // Enable HLVD interrupt
                    IPR0bits.SWIP = 0;     // Make SW interrupt low priority

                    // Change IVTBASE if required
                    IVTBASEU = 0x00;          // Optional
                    IVTBASEH = 0x30;          // Default is 0x000008
                    IVTBASEL = 0x08;
                }


11.10 External Interrupt Pins
       Devices may have several external interrupt sources that can be assigned to pins on different ports
       based on PPS settings. Refer to the “PPS - Peripheral Pin Select Module” chapter for possible
       routing options for these external interrupts. The external interrupt sources are edge-triggered. If
       the corresponding INTxEDG bit in INTCON0 is set, the interrupt is triggered by a rising edge. If the bit
       is clear, the trigger is on the falling edge.
       When a valid edge appears on the INTx pin, the corresponding flag bit (INTxF in the PIRx registers) is
       set. This interrupt can be disabled by clearing the corresponding enable bit, INTxE. The flag bit INTxF
       must be cleared by software in the Interrupt Service Routine before re-enabling the interrupt.
       All external interrupts can wake up the processor from Idle or Sleep modes if the INTxE bit was set
       prior to going into those modes. If GIE/GIEH bit is set, the processor will branch to the interrupt
       vector following wake-up. Interrupt priority is determined by the value contained in the respective
       INTxIP interrupt priority bits of the IPRx registers.

11.11 Wake-Up from Sleep
       The interrupt controller provides a wake-up request to the CPU whenever an interrupt event occurs,
       if the interrupt event is enabled. This occurs regardless of whether the part is in Run, Idle/Doze
       or Sleep modes. The status of GIE/GIEH and GIEL bits have no effect on the wake-up request. This
       wake-up request is asynchronous to all clocks.

11.12 Interrupt Compatibility
       When the MVECEN bit is cleared, the IVT feature is disabled, and interrupts are compatible with
       previous high-performance 8-bit PIC18 microcontroller devices. In this mode, the IVT priority has no
       effect.


--- p131 ---
                                                                                                    PIC18F27/47/57Q43
                                                                                      VIC - Vectored Interrupt Controller
                                                                                                                 Module
       When IPEN is also cleared, the interrupt priority feature is disabled and interrupts are compatible
       with PIC16 microcontroller midrange devices. All interrupts branch to address 0008h, since the
       interrupt priority is disabled.

11.13 Register Definitions: Interrupt Control


--- p132 ---
                                                                                                                            PIC18F27/47/57Q43
                                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                                         Module
11.13.1 INTCON0

            Name:           INTCON0
            Address:        0x4D6

            Interrupt Control Register 0

      Bit           7              6                 5                 4                  3          2                1               0
                GIE/GIEH          GIEL             IPEN                                           INT2EDG          INT1EDG         INT0EDG
  Access          R/W             R/W              R/W                                              R/W              R/W             R/W
   Reset            0              0                 0                                               1                1               1

Bit 7 – GIE/GIEH Global Interrupt Enable
            Value          Condition Description
            1              IPEN = 0 Enables all masked interrupts
            0              IPEN = 0   Disables all interrupts
            1              IPEN = 1   Enables all unmasked high-priority interrupts: The bit also needs to be set for enabling low-priority
                                      interrupts
            0              IPEN = 1   Disables all interrupts


Bit 6 – GIEL Global Low-Priority Interrupt Enable
            Value          Condition Description
            n              IPEN = 0 Reserved, read as ‘0’
            1              IPEN = 1    Enables all unmasked low-priority interrupts, GIEH also needs to be set for low-priority interrupts
            0              IPEN = 1    Disables all low-priority interrupts


Bit 5 – IPEN Interrupt Priority Enable
            Value          Description
            1              Enable priority levels on interrupts
            0              Disable priority levels on interrupts, all interrupts are treated as high-priority interrupts

Bit 2 – INT2EDG External Interrupt 2 Edge Select
            Value          Description
            1              Interrupt on rising edge of the INT2 pin
            0              Interrupt on falling edge of the INT2 pin

Bit 1 – INT1EDG External Interrupt 1 Edge Select
            Value          Description
            1              Interrupt on rising edge of the INT1 pin
            0              Interrupt on falling edge of the INT1 pin

Bit 0 – INT0EDG External Interrupt 0 Edge Select
            Value          Description
            1              Interrupt on rising edge of the INT0 pin
            0              Interrupt on falling edge of the INT0 pin


--- p133 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                          VIC - Vectored Interrupt Controller
                                                                                                                                     Module
11.13.2 INTCON1

            Name:          INTCON1
            Address:       0x4D7

            Interrupt Control Register 1

      Bit           7               6              5               4                  3            2               1                 0
                        STAT[1:0]
  Access            R               R
   Reset            0               0

Bits 7:6 – STAT[1:0] Interrupt State Status
            Value         Description
            11            High-priority ISR executing, high-priority interrupt was received while a low-priority ISR was executing
            10            High-priority ISR executing, high-priority interrupt was received in main routine
            01            Low-priority ISR executing, low-priority interrupt was received in main routine
            00            Main routine executing


--- p134 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.3 IVTBASE

            Name:      IVTBASE
            Address:   0x45D

            Interrupt Vector Table Base Address Register

      Bit        23          22          21             20                19         18               17              16
                                                                                IVTBASEU[4:0]
  Access                                               R/W                R/W       R/W              R/W             R/W
   Reset                                                0                  0          0               0               0

      Bit        15          14          13             12           11               10               9               8
                                                         IVTBASEH[7:0]
  Access        R/W         R/W          R/W           R/W          R/W              R/W             R/W             R/W
   Reset         0           0            0             0            0                0               0               0

      Bit        7            6           5             4            3                    2            1               0
                                                         IVTBASEL[7:0]
  Access        R/W         R/W          R/W           R/W          R/W              R/W             R/W             R/W
   Reset         0           0            0             0            0                0               0               0

Bits 20:16 – IVTBASEU[4:0] Interrupt Vector Table Base Address Most Significant 5 bits

Bits 15:8 – IVTBASEH[7:0] Interrupt Vector Table Base Address Middle 8 bits

Bits 7:0 – IVTBASEL[7:0] Interrupt Vector Table Base Address Least Significant 8 bits


--- p135 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                 VIC - Vectored Interrupt Controller
                                                                                                                            Module
11.13.4 IVTAD

            Name:      IVTAD
            Address:   0x45A

            Interrupt Vector Table Address

      Bit        23          22          21                20                  19       18               17              16
                                                                                    IVTADU[4:0]
  Access                                                    R                  R         R                R               R
   Reset                                                    0                  0         0                0               0

      Bit        15          14          13                12           11               10               9               8
                                                             IVTADH[7:0]
  Access         R             R             R             R             R                   R            R               R
   Reset         0             0             0             0             0                   0            0               0

      Bit        7             6             5              4                  3             2            1               0
                                                                IVTADL[7:0]
  Access         R             R             R              R                  R             R            R               R
   Reset         0             0             0              0                  0             0            0               0

Bits 20:16 – IVTADU[4:0] Interrupt Vector Table Address Most Significant 5 bits

Bits 15:8 – IVTADH[7:0] Interrupt Vector Table Address Middle 8 bits

Bits 7:0 – IVTADL[7:0] Interrupt Vector Table Address Least Significant 8 bits


--- p136 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.5 IVTLOCK

            Name:        IVTLOCK
            Address:     0x459

            Interrupt Vector Table Lock Register

      Bit           7           6              5               4                  3            2            1              0
                                                                                                                      IVTLOCKED
  Access                                                                                                                 R/W
   Reset                                                                                                                   0

Bit 0 – IVTLOCKED IVT Registers Lock(1,2)
            Value       Description
            1           IVTBASE Registers are locked and cannot be written
            0           IVTBASE Registers can be modified by write operations

            Notes:
            1. The IVTLOCKED bit can only be set or cleared after the unlock sequence in Example 11-1.
            2. If IVT1WAY = 1, the IVTLOCKED bit cannot be cleared after it has been set.


--- p137 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.6 SHADCON

           Name:        SHADCON
           Address:     0x376

           Shadow Control Register

     Bit           7            6              5               4                  3            2            1              0
                                                                                                                        SHADLO
  Access                                                                                                                  R/W
   Reset                                                                                                                   0

Bit 0 – SHADLO Interrupt Shadow Register Access Switch
           Value       Description
           1           Access Main Context for Interrupt Shadow registers
           0           Access Low-Priority Interrupt Context for Interrupt Shadow registers


--- p138 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.7 PIE0

            Name:       PIE0
            Address:    0x49E

            Peripheral Interrupt Enable Register 0

      Bit        7              6         5              4                3           2              1               0
               IOCIE                    CLC1IE                          CSWIE        OSFIE         HLVDIE           SWIE
  Access        R/W                      R/W                             R/W         R/W            R/W             R/W
   Reset         0                        0                               0           0              0               0

Bit 7 – IOCIE Interrupt-on-Change Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 5 – CLC1IE CLC1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 3 – CSWIE Clock Switch Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 2 – OSFIE Oscillator Failure Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 1 – HLVDIE High/Low-Voltage Detect Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 0 – SWIE Software Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled


--- p139 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.8 PIE1

            Name:       PIE1
            Address:    0x49F

            Peripheral Interrupt Enable Register 1

      Bit    7                6           5             4                 3           2             1               0
         SMT1PWAIE        SMT1PRAIE     SMT1IE        CM1IE             ACTIE        ADIE         ZCDIE           INT0IE
  Access    R/W             R/W          R/W           R/W               R/W         R/W           R/W             R/W
   Reset     0                0           0             0                 0           0             0               0

Bit 7 – SMT1PWAIE SMT1 Pulse-Width Acquisition Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 6 – SMT1PRAIE SMT1 Period Acquisition Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 5 – SMT1IE SMT1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 4 – CM1IE CMP1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 3 – ACTIE Active Clock Tuning Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 2 – ADIE ADC Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 1 – ZCDIE ZCD Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 0 – INT0IE External Interrupt 0 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled


--- p140 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.9 PIE2

           Name:        PIE2
           Address:     0x4A0

           Peripheral Interrupt Enable Register 2

     Bit        7            6         5          4                     3                2            1              0
             DMA1AIE      DMA1ORIE DMA1DCNTIE DMA1SCNTIE                                                           ADTIE
  Access       R/W          R/W       R/W        R/W                                                                R/W
   Reset        0            0         0          0                                                                  0

Bit 7 – DMA1AIE DMA1 Abort Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 6 – DMA1ORIE DMA1 Overrun Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 5 – DMA1DCNTIE DMA1 Destination Count Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 4 – DMA1SCNTIE DMA1 Source Count Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 0 – ADTIE ADC Threshold Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled


--- p141 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.10 PIE3

            Name:       PIE3
            Address:    0x4A1

            Peripheral Interrupt Enable Register 3

      Bit       7             6           5            4               3              2              1                0
              TMR0IE        CCP1IE     TMR1GIE       TMR1IE          TMR2IE         SPI1IE        SPI1TXIE        SPI1RXIE
  Access       R/W           R/W         R/W          R/W             R/W            R/W            R/W             R/W
   Reset        0             0           0            0               0              0              0                0

Bit 7 – TMR0IE TMR0 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 6 – CCP1IE CCP1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 5 – TMR1GIE TMR1 Gate Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 4 – TMR1IE TMR1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 3 – TMR2IE TMR2 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 2 – SPI1IE SPI1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 1 – SPI1TXIE SPI1 Transmit Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 0 – SPI1RXIE SPI1 Receive Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled


--- p142 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.11 PIE4

           Name:       PIE4
           Address:    0x4A2

           Peripheral Interrupt Enable Register 4

     Bit       7             6            5             4                   3         2             1               0
             PWM1IE       PWM1PIE                                          U1IE     U1EIE         U1TXIE          U1RXIE
  Access      R/W           R/W                                            R/W       R/W           R/W             R/W
   Reset       0             0                                              0         0             0               0

Bit 7 – PWM1IE PWM1 Parameter Interrupt Enable
           Value      Description
           1          Enabled
           0          Disabled

Bit 6 – PWM1PIE PWM1 Period Interrupt Enable
           Value      Description
           1          Enabled
           0          Disabled

Bit 3 – U1IE UART1 Interrupt Enable
           Value      Description
           1          Enabled
           0          Disabled

Bit 2 – U1EIE UART1 Framing Error Interrupt Enable
           Value      Description
           1          Enabled
           0          Disabled

Bit 1 – U1TXIE UART1 Transmit Interrupt Enable
           Value      Description
           1          Enabled
           0          Disabled

Bit 0 – U1RXIE UART 1 Receive Interrupt Enable
           Value      Description
           1          Enabled
           0          Disabled


--- p143 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.12 PIE5

            Name:       PIE5
            Address:    0x4A3

            Peripheral Interrupt Enable Register 5

      Bit       7             6           5            4                 3            2              1                0
              PWM2IE       PWM2PIE     TMR3GIE       TMR3IE                         SPI2IE        SPI2TXIE        SPI2RXIE
  Access       R/W           R/W         R/W          R/W                            R/W            R/W             R/W
   Reset        0             0           0            0                              0              0                0

Bit 7 – PWM2IE PWM2 Parameter Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 6 – PWM2PIE PWM2 Period Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 5 – TMR3GIE TMR3 Gate Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 4 – TMR3IE TMR3 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 2 – SPI2IE SPI2 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 1 – SPI2TXIE SPI2 Transmit Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 0 – SPI2RXIE SPI2 Receive Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled


--- p144 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.13 PIE6

            Name:        PIE6
            Address:     0x4A4

            Peripheral Interrupt Enable Register 6

      Bit        7            6         5          4                  3              2              1               0
              DMA2AIE      DMA2ORIE DMA2DCNTIE DMA2SCNTIE           NCO1IE         CWG1IE         CLC2IE          INT1IE
  Access        R/W          R/W       R/W        R/W                R/W            R/W            R/W             R/W
   Reset         0            0         0          0                  0              0              0               0

Bit 7 – DMA2AIE DMA2 Abort Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 6 – DMA2ORIE DMA2 Overrun Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 5 – DMA2DCNTIE DMA2 Destination Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 4 – DMA2SCNTIE DMA2 Source Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 3 – NCO1IE NCO1 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – CWG1IE CWG1 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – CLC2IE CLC2 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 0 – INT1IE External Interrupt 1 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p145 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.14 PIE7

            Name:       PIE7
            Address:    0x4A5

            Peripheral Interrupt Enable Register 7

      Bit       7             6           5              4                3           2              1               0
              PWM3IE       PWM3PIE      CLC3IE                         I2C1EIE      I2C1IE        I2C1TXIE        I2C1RXIE
  Access       R/W           R/W         R/W                             R/W         R/W            R/W             R/W
   Reset        0             0           0                               0           0              0               0

Bit 7 – PWM3IE PWM3 Parameter Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 6 – PWM3PIE PWM3 Period Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 5 – CLC3IE CLC3 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 3 – I2C1EIE I2C1 Error Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 2 – I2C1IE I2C1 Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 1 – I2C1TXIE I2C1 Transmit Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled

Bit 0 – I2C1RXIE I2C1 Receive Interrupt Enable
            Value      Description
            1          Enabled
            0          Disabled


--- p146 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.15 PIE8

           Name:        PIE8
           Address:     0x4A6

           Peripheral Interrupt Enable Register 8

     Bit        7             6          5            4                  3            2             1               0
              SCANIE        CCP2IE    TMR5GIE       TMR5IE              U2IE        U2EIE         U2TXIE          U2RXIE
  Access       R/W           R/W        R/W          R/W                R/W          R/W           R/W             R/W
   Reset        0             0          0            0                  0            0             0               0

Bit 7 – SCANIE Memory Scanner Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 6 – CCP2IE CCP2 Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 5 – TMR5GIE TMR5 Gate Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 4 – TMR5IE TMR5 Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 3 – U2IE UART2 Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 2 – U2EIE UART2 Framing Error Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 1 – U2TXIE UART2 Transmit Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 0 – U2RXIE UART2 Receive Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled


--- p147 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.16 PIE9

            Name:        PIE9
            Address:     0x4A7

            Peripheral Interrupt Enable Register 9

      Bit           7            6        5              4                   3         2             1               0
                                        CLC4IE                              U3IE     U3EIE         U3TXIE          U3RXIE
  Access                                 R/W                                R/W       R/W           R/W             R/W
   Reset                                  0                                  0         0             0               0

Bit 5 – CLC4IE CLC4 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 3 – U3IE UART3 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – U3EIE UART3 Framing Error Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – U3TXIE UART3 Transmit Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 0 – U3RXIE UART3 Receive Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p148 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.17 PIE10

            Name:        PIE10
            Address:     0x4A8

            Peripheral Interrupt Enable Register 10

      Bit        7            6         5          4                  3              2              1               0
              DMA3AIE      DMA3ORIE DMA3DCNTIE DMA3SCNTIE           NCO2IE         CWG2IE         CLC5IE          INT2IE
  Access        R/W          R/W       R/W        R/W                R/W            R/W            R/W             R/W
   Reset         0            0         0          0                  0              0              0               0

Bit 7 – DMA3AIE DMA3 Abort Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 6 – DMA3ORIE DMA3 Overrun Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 5 – DMA3DCNTIE DMA3 Destination Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 4 – DMA3SCNTIE DMA3 Source Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 3 – NCO2IE NCO2 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – CWG2IE CWG2 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – CLC5IE CLC5 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 0 – INT2IE External Interrupt 2 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p149 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.18 PIE11

            Name:        PIE11
            Address:     0x4A9

            Peripheral Interrupt Enable Register 11

      Bit        7            6         5          4                   3             2              1               0
              DMA4AIE      DMA4ORIE DMA4DCNTIE DMA4SCNTIE            TMR4IE        CWG3IE         CLC6IE          CCP3IE
  Access        R/W          R/W       R/W        R/W                 R/W           R/W            R/W             R/W
   Reset         0            0         0          0                   0             0              0               0

Bit 7 – DMA4AIE DMA4 Abort Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 6 – DMA4ORIE DMA4 Overrun Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 5 – DMA4DCNTIE DMA4 Destination Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 4 – DMA4SCNTIE DMA4 Source Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 3 – TMR4IE TMR4 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – CWG3IE CWG3 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – CLC6IE CLC6 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 0 – CCP3IE CCP3 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p150 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.19 PIE12

            Name:        PIE12
            Address:     0x4AA

            Peripheral Interrupt Request Register 12

      Bit        7             6         5         4                      3            2             1               0
              DMA5AIE      DMA5ORIE DMA5DCNTIE DMA5SCNTIE                U4IE        U4EIE         U4TXIE          U4RXIE
  Access        R/W         R/W/HS    R/W/HS      R/W                    R/W          R/W           R/W             R/W
   Reset         0             0         0         0                      0            0             0               0

Bit 7 – DMA5AIE DMA5 Abort Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 6 – DMA5ORIE DMA5 Overrun Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 5 – DMA5DCNTIE DMA5 Destination Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 4 – DMA5SCNTIE DMA5 Source Count Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 3 – U4IE UART 4 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – U4EIE UART4 Framing Error Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – U4TXIE UART4 Transmit Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 0 – U4RXIE UART4 Receive Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p151 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.20 PIE13

           Name:        PIE13
           Address:     0x4AB

           Peripheral Interrupt Enable Register 13

     Bit        7            6         5          4                      3            2             1               0
             DMA6AIE      DMA6ORIE DMA6DCNTIE DMA6SCNTIE                U5IE        U5EIE         U5TXIE          U5RXIE
  Access       R/W          R/W       R/W        R/W                    R/W          R/W           R/W             R/W
   Reset        0            0         0          0                      0            0             0               0

Bit 7 – DMA6AIE DMA6 Abort Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 6 – DMA6ORIE DMA6 Overrun Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 5 – DMA6DCNTIE DMA6 Destination Count Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 4 – DMA6SCNTIE DMA6 Source Count Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 3 – U5IE UART5 Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 2 – U5EIE UART5 Framing Error Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 1 – U5TXIE UART5 Transmit Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled

Bit 0 – U5RXIE UART5 Receive Interrupt Enable
           Value       Description
           1           Enabled
           0           Disabled


--- p152 ---
                                                                                                          PIC18F27/47/57Q43
                                                                                            VIC - Vectored Interrupt Controller
                                                                                                                       Module
11.13.21 PIE14

            Name:        PIE14
            Address:     0x4AC

            Peripheral Interrupt Enable Register 14

      Bit           7           6         5              4               3            2             1                0
                                                                       NCO3IE       CM2IE         CLC7IE
  Access                                                                R/W          R/W           R/W
   Reset                                                                 0            0             0

Bit 3 – NCO3IE NCO3 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – CM2IE CMP2 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – CLC7IE CLC7 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p153 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.22 PIE15

            Name:        PIE15
            Address:     0x4AD

            Peripheral Interrupt Enable Register 15

      Bit           7           6         5              4               3             2             1               0
                                                                       TMR6IE        CRCIE         CLC8IE          NVMIE
  Access                                                                R/W           R/W           R/W             R/W
   Reset                                                                 0             0             0               0

Bit 3 – TMR6IE TMR6 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 2 – CRCIE CRC Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 1 – CLC8IE CLC8 Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled

Bit 0 – NVMIE NVM Interrupt Enable
            Value       Description
            1           Enabled
            0           Disabled


--- p154 ---
                                                                                                                   PIC18F27/47/57Q43
                                                                                                     VIC - Vectored Interrupt Controller
                                                                                                                                Module
11.13.23 PIR0

            Name:        PIR0
            Address:     0x4AE

            Peripheral Interrupt Request Register 0

      Bit         7              6               5                 4                3          2             1               0
                IOCIF                         CLC1IF                              CSWIF      OSFIF        HLVDIF            SWIF
  Access          R                           R/W/HS                             R/W/HS     R/W/HS        R/W/HS            R/W
   Reset          0                              0                                  0          0             0               0

Bit 7 – IOCIF Interrupt-on-Change Interrupt Flag (2)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 5 – CLC1IF CLC1 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – CSWIF Clock Switch Interrupt Flag(3)
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 2 – OSFIF Oscillator Failure Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 1 – HLVDIF High/Low-Voltage Detect Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 0 – SWIF Software Interrupt Flag
            Value       Description
            1           Interrupt will trigger (bit is set and cleared by user software)
            0           Interrupt event has not occurred

            Notes:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.
            2. IOCIF is a read-only bit. To clear the interrupt condition, all bits in the IOCxF registers must be
               cleared.
            3. The CSWIF interrupt will not wake the system from Sleep mode. The system will sleep until
               another interrupt causes the wake-up.


--- p155 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.24 PIR1

            Name:       PIR1
            Address:    0x4AF

            Peripheral Interrupt Request Register 1

      Bit    7                6               5               4              3              2             1               0
         SMT1PWAIF        SMT1PRAIF        SMT1IF           CM1IF          ACTIF          ADIF          ZCDIF          INT0IF
  Access  R/W/HS           R/W/HS          R/W/HS          R/W/HS         R/W/HS         R/W/HS        R/W/HS          R/W/HS
   Reset     0                0               0               0              0              0             0               0

Bit 7 – SMT1PWAIF SMT1 Pulse-Width Acquisition Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 6 – SMT1PRAIF SMT1 Period Acquisition Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 5 – SMT1IF SMT1 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 4 – CM1IF CMP1 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 3 – ACTIF Active Clock Tuning Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 2 – ADIF ADC Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 1 – ZCDIF ZCD Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 0 – INT0IF External Interrupt 0 Interrupt Flag(2)
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred


--- p156 ---
                                                                                             PIC18F27/47/57Q43
                                                                               VIC - Vectored Interrupt Controller
                                                                                                          Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. The external interrupt GPIO pin is selected by the INTxPPS register.


--- p157 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                    VIC - Vectored Interrupt Controller
                                                                                                                               Module
11.13.25 PIR2

            Name:        PIR2
            Address:     0x4B0

            Peripheral Interrupt Request Register 2

      Bit        7             6         5          4                           3               2            1              0
              DMA1AIF      DMA1ORIF DMA1DCNTIF DMA1SCNTIF                                                                 ADTIF
  Access      R/W/HS        R/W/HS    R/W/HS     R/W/HS                                                                  R/W/HS
   Reset         0             0         0          0                                                                       0

Bit 7 – DMA1AIF DMA1 Abort Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 6 – DMA1ORIF DMA1 Overrun Interrupt Flag
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 5 – DMA1DCNTIF DMA1 Destination Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 4 – DMA1SCNTIF DMA1 Source Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 0 – ADTIF ADC Threshold Interrupt Flag
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

            Note:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.


--- p158 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.26 PIR3

            Name:       PIR3
            Address:    0x4B1

            Peripheral Interrupt Request Register 3

      Bit        7             6               5              4              3             2              1               0
              TMR0IF        CCP1IF         TMR1GIF         TMR1IF         TMR2IF         SPI1IF        SPI1TXIF        SPI1RXIF
  Access      R/W/HS        R/W/HS          R/W/HS         R/W/HS         R/W/HS           R              R               R
   Reset         0             0               0              0              0             0              0               0

Bit 7 – TMR0IF TMR0 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 6 – CCP1IF CCP1 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 5 – TMR1GIF TMR1 Gate Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 4 – TMR1IF TMR1 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 3 – TMR2IF TMR2 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 2 – SPI1IF SPI1 Interrupt Flag(2)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 1 – SPI1TXIF SPI1 Transmit Interrupt Flag(3)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 0 – SPI1RXIF SPI1 Receive Interrupt Flag(3)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred


--- p159 ---
                                                                                              PIC18F27/47/57Q43
                                                                                VIC - Vectored Interrupt Controller
                                                                                                           Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. SPI1IF is a read-only bit. TO clear the interrupt condition, all bits in the SPI1INTF register must be
   cleared.
3. SPI1TXIF and SPI1RXIF are read-only bits and cannot be set/cleared by software.


--- p160 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.27 PIR4

            Name:       PIR4
            Address:    0x4B2

            Peripheral Interrupt Request Register 4

      Bit       7              6               5              4                   3         2             1               0
              PWM1IF       PWM1PIF                                               U1IF     U1EIF         U1TXIF          U1RXIF
  Access        R           R/W/HS                                                R         R             R               R
   Reset        0              0                                                  0         0             0               0

Bit 7 – PWM1IF PWM1 Parameter Interrupt Flag(2)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 6 – PWM1PIF PWM1 Period Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 3 – U1IF UART1 Interrupt Flag(3)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 2 – U1EIF UART1 Framing Error Interrupt Flag(4)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 1 – U1TXIF UART1 Transmit Interrupt Flag(5)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 0 – U1RXIF UART 1 Receive Interrupt Flag(5)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

            Notes:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.
            2. PWM1IF is a read-only bit. To clear the interrupt condition, all bits in the PWM1GIR register must
               be cleared.
            3. U1IF is a read-only bit. To clear the interrupt condition, all bits in the U1UIR register must be
               cleared.
            4. U1EIF is a read-only bit. To clear the interrupt condition, all bits in the U1ERR register must be
               cleared.
            5. U1TXIF and U1RXIF are read-only bits and cannot be set/cleared by software.


--- p161 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.28 PIR5

            Name:       PIR5
            Address:    0x4B3

            Peripheral Interrupt Request Register 5

      Bit       7              6               5              4                3           2              1               0
              PWM2IF       PWM2PIF         TMR3GIF         TMR3IF                        SPI2IF        SPI2TXIF        SPI2RXIF
  Access        R           R/W/HS          R/W/HS         R/W/HS                          R              R               R
   Reset        0              0               0              0                            0              0               0

Bit 7 – PWM2IF PWM2 Parameter Interrupt Flag(2)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 6 – PWM2PIF PWM2 Period Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 5 – TMR3GIF TMR3 Gate Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 4 – TMR3IF TMR3 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 2 – SPI2IF SPI2 Interrupt Flag(3)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 1 – SPI2TXIF SPI2 Transmit Interrupt Flag(4)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 0 – SPI2RXIF SPI2 Receive Interrupt Flag(4)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred


--- p162 ---
                                                                                              PIC18F27/47/57Q43
                                                                                VIC - Vectored Interrupt Controller
                                                                                                           Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. PWM2IF is a read-only bit. To clear the interrupt condition, all bits in the PWM2GIR register must
   be cleared.
3. SPI2IF is a read-only bit. TO clear the interrupt condition, all bits in the SPI2INTF register must be
   cleared.
4. SPI2TXIF and SPI2RXIF are read-only bits and cannot be set/cleared by software.


--- p163 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.29 PIR6

            Name:        PIR6
            Address:     0x4B4

            Peripheral Interrupt Request Register 6

      Bit        7             6         5          4                         3             2             1               0
              DMA2AIF      DMA2ORIF DMA2DCNTIF DMA2SCNTIF                  NCO1IF        CWG1IF        CLC2IF          INT1IF
  Access      R/W/HS        R/W/HS    R/W/HS     R/W/HS                    R/W/HS        R/W/HS        R/W/HS          R/W/HS
   Reset         0             0         0          0                         0             0             0               0

Bit 7 – DMA2AIF DMA2 Abort Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 6 – DMA2ORIF DMA2 Overrun Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 5 – DMA2DCNTIF DMA2 Destination Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 4 – DMA2SCNTIF DMA2 Source Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – NCO1IF NCO1 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 2 – CWG1IF CWG1 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 1 – CLC2IF CLC2 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 0 – INT1IF External Interrupt 1 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

            Note:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.


--- p164 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.30 PIR7

            Name:       PIR7
            Address:    0x4B5

            Peripheral Interrupt Request Register 7

      Bit       7              6              5               4                3           2              1               0
              PWM3IF       PWM3PIF         CLC3IF                           I2C1EIF      I2C1IF        I2C1TXIF        I2C1RXIF
  Access        R           R/W/HS         R/W/HS                              R           R              R               R
   Reset        0              0              0                                0           0              0               0

Bit 7 – PWM3IF PWM3 Parameter Interrupt Flag(2)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 6 – PWM3PIF PWM3 Period Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 5 – CLC3IF CLC3 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 3 – I2C1EIF I2C1 Error Interrupt Flag(3)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 2 – I2C1IF I2C1 Interrupt Flag(4)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 1 – I2C1TXIF I2C1 Transmit Interrupt Flag(5)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 0 – I2C1RXIF I2C1 Receive Interrupt Flag(5)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred


--- p165 ---
                                                                                              PIC18F27/47/57Q43
                                                                                VIC - Vectored Interrupt Controller
                                                                                                           Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. PWM3IF is a read-only bit. To clear the interrupt condition, all bits in the PWM3GIR register must
   be cleared.
3. I2C1EIF is a read-only bit. To clear the interrupt condition, all bits in the I2C1ERR register must be
   cleared.
4. I2C1IF is a read-only bit. To clear the interrupt condition, all bits in the I2C1PIR register must be
   cleared.
5. I2C1TXIF and I2C1RXIF are read-only bits. To clear the interrupt condition, the CLRBF bit in
   I2C1STAT1 must be set.


--- p166 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.31 PIR8

            Name:       PIR8
            Address:    0x4B6

            Peripheral Interrupt Request Register 8

      Bit        7             6               5              4                 3           2             1               0
              SCANIF        CCP2IF         TMR5GIF         TMR5IF              U2IF       U2EIF         U2TXIF          U2RXIF
  Access      R/W/HS        R/W/HS          R/W/HS         R/W/HS               R           R             R               R
   Reset         0             0               0              0                 0           0             0               0

Bit 7 – SCANIF Memory Scanner Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 6 – CCP2IF CCP2 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 5 – TMR5GIF TMR5 Gate Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 4 – TMR5IF TMR5 Interrupt Flag
            Value      Description
            1          Interrupt has occurred (must be cleared by software)
            0          Interrupt event has not occurred

Bit 3 – U2IF UART2 Interrupt Flag(2)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 2 – U2EIF UART2 Framing Error Interrupt Flag(3)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 1 – U2TXIF UART2 Transmit Interrupt Flag(4)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred

Bit 0 – U2RXIF UART2 Receive Interrupt Flag(4)
            Value      Description
            1          Interrupt has occurred
            0          Interrupt event has not occurred


--- p167 ---
                                                                                              PIC18F27/47/57Q43
                                                                                VIC - Vectored Interrupt Controller
                                                                                                           Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. U2IF is a read-only bit. To clear the interrupt condition, all bits in the U2UIR register must be
   cleared.
3. U2EIF is a read-only bit. To clear the interrupt condition, all bits in the U2ERR register must be
   cleared.
4. U2TXIF and U2RXIF are read-only bits and cannot be set/cleared by software.


--- p168 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.32 PIR9

            Name:        PIR9
            Address:     0x4B7

            Peripheral Interrupt Request Register 9

      Bit           7            6             5               4                   3         2             1               0
                                            CLC4IF                                U3IF     U3EIF         U3TXIF          U3RXIF
  Access                                    R/W/HS                                 R         R             R               R
   Reset                                       0                                   0         0             0               0

Bit 5 – CLC4IF CLC4 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – U3IF UART3 Interrupt Flag(2)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 2 – U3EIF UART3 Framing Error Interrupt Flag(3)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 1 – U3TXIF UART3 Transmit Interrupt Flag(4)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 0 – U3RXIF UART3 Receive Interrupt Flag(4)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

            Notes:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.
            2. U3IF is a read-only bit. To clear the interrupt condition, all bits in the U3UIR register must be
               cleared.
            3. U3EIF is a read-only bit. To clear the interrupt condition, all bits in the U3ERR register must be
               cleared.
            4. U3TXIF and U3RXIF are read-only bits and cannot be set/cleared by software.


--- p169 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.33 PIR10

            Name:        PIR10
            Address:     0x4B8

            Peripheral Interrupt Request Register 10

      Bit        7             6         5          4                         3             2             1               0
              DMA3AIF      DMA3ORIF DMA3DCNTIF DMA3SCNTIF                  NCO2IF        CWG2IF        CLC5IF          INT2IF
  Access      R/W/HS        R/W/HS    R/W/HS     R/W/HS                    R/W/HS        R/W/HS        R/W/HS          R/W/HS
   Reset         0             0         0          0                         0             0             0               0

Bit 7 – DMA3AIF DMA3 Abort Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 6 – DMA3ORIF DMA3 Overrun Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 5 – DMA3DCNTIF DMA3 Destination Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 4 – DMA3SCNTIF DMA3 Source Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – NCO2IF NCO2 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 2 – CWG2IF CWG2 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 1 – CLC5IF CLC5 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 0 – INT2IF External Interrupt 2 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

            Note:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.


--- p170 ---
                                                                                                                PIC18F27/47/57Q43
                                                                                                  VIC - Vectored Interrupt Controller
                                                                                                                             Module
11.13.34 PIR11

            Name:        PIR11
            Address:     0x4B9

            Peripheral Interrupt Request Register 11

      Bit        7             6         5          4                         3             2             1               0
              DMA4AIF      DMA4ORIF DMA4DCNTIF DMA4SCNTIF                  TMR4IF        CWG3IF        CLC6IF          CCP3IF
  Access      R/W/HS        R/W/HS    R/W/HS     R/W/HS                    R/W/HS        R/W/HS        R/W/HS          R/W/HS
   Reset         0             0         0          0                         0             0             0               0

Bit 7 – DMA4AIF DMA4 Abort Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 6 – DMA4ORIF DMA4 Overrun Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 5 – DMA4DCNTIF DMA4 Destination Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 4 – DMA4SCNTIF DMA4 Source Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – TMR4IF TMR4 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 2 – CWG3IF CWG3 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 1 – CLC6IF CLC6 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 0 – CCP3IF CCP3 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

            Note:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.


--- p171 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.35 PIR12

            Name:        PIR12
            Address:     0x4BA

            Peripheral Interrupt Request Register 12

      Bit        7             6         5          4                            3           2             1               0
              DMA5AIF      DMA5ORIF DMA5DCNTIF DMA5SCNTIF                       U4IF       U4EIF         U4TXIF          U4RXIF
  Access      R/W/HS        R/W/HS    R/W/HS     R/W/HS                          R           R             R               R
   Reset         0             0         0          0                            0           0             0               0

Bit 7 – DMA5AIF DMA5 Abort Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 6 – DMA5ORIF DMA5 Overrun Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 5 – DMA5DCNTIF DMA5 Destination Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 4 – DMA5SCNTIF DMA5 Source Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – U4IF UART 4 Interrupt Flag(2)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 2 – U4EIF UART4 Framing Error Interrupt Flag(3)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 1 – U4TXIF UART4 Transmit Interrupt Flag(4)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 0 – U4RXIF UART4 Receive Interrupt Flag(4)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred


--- p172 ---
                                                                                              PIC18F27/47/57Q43
                                                                                VIC - Vectored Interrupt Controller
                                                                                                           Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. U4IF is a read-only bit. To clear the interrupt condition, all bits in the U4UIR register must be
   cleared.
3. U4EIF is a read-only bit. To clear the interrupt condition, all bits in the U4ERR register must be
   cleared.
4. U4TXIF and U4RXIF are read-only bits and cannot be set/cleared by software.


--- p173 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.36 PIR13

            Name:        PIR13
            Address:     0x4BB

            Peripheral Interrupt Request Register 13

      Bit        7             6         5          4                            3           2             1               0
              DMA6AIF      DMA6ORIF DMA6DCNTIF DMA6SCNTIF                       U5IF       U5EIF         U5TXIF          U5RXIF
  Access      R/W/HS        R/W/HS    R/W/HS     R/W/HS                          R           R             R               R
   Reset         0             0         0          0                            0           0             0               0

Bit 7 – DMA6AIF DMA6 Abort Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 6 – DMA6ORIF DMA6 Overrun Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 5 – DMA6DCNTIF DMA6 Destination Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 4 – DMA6SCNTIF DMA6 Source Count Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 3 – U5IF UART5 Interrupt Flag(2)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 2 – U5EIF UART5 Framing Error Interrupt Flag(3)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 1 – U5TXIF UART5 Transmit Interrupt Flag(4)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred

Bit 0 – U5RXIF UART5 Receive Interrupt Flag(4)
            Value       Description
            1           Interrupt has occurred
            0           Interrupt event has not occurred


--- p174 ---
                                                                                              PIC18F27/47/57Q43
                                                                                VIC - Vectored Interrupt Controller
                                                                                                           Module
Notes:
1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
   corresponding enable bit or the global enable bit. User software will ensure the appropriate
   interrupt flag bits are clear prior to enabling an interrupt.
2. U5IF is a read-only bit. To clear the interrupt condition, all bits in the U5UIR register must be
   cleared.
3. U5EIF is a read-only bit. To clear the interrupt condition, all bits in the U5ERR register must be
   cleared.
4. U5TXIF and U5RXIF are read-only bits and cannot be set/cleared by software.


--- p175 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.37 PIR14

            Name:        PIR14
            Address:     0x4BC

            Peripheral Interrupt Request Register 14

      Bit           7           6               5              4                3            2             1                0
                                                                             NCO3IF        CM2IF        CLC7IF
  Access                                                                     R/W/HS       R/W/HS        R/W/HS
   Reset                                                                        0            0             0

Bit 3 – NCO3IF NCO3 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 2 – CM2IF CMP2 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 1 – CLC7IF CLC7 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

            Note:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.


--- p176 ---
                                                                                                                 PIC18F27/47/57Q43
                                                                                                   VIC - Vectored Interrupt Controller
                                                                                                                              Module
11.13.38 PIR15

            Name:        PIR15
            Address:     0x4BD

            Peripheral Interrupt Request Register 15

      Bit           7           6               5              4                3            2             1               0
                                                                             TMR6IF        CRCIF        CLC8IF          NVMIF
  Access                                                                     R/W/HS       R/W/HS        R/W/HS          R/W/HS
   Reset                                                                        0            0             0               0

Bit 3 – TMR6IF TMR6 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 2 – CRCIF CRC Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 1 – CLC8IF CLC8 Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

Bit 0 – NVMIF NVM Interrupt Flag
            Value       Description
            1           Interrupt has occurred (must be cleared by software)
            0           Interrupt event has not occurred

            Note:
            1. Interrupt flag bits get set when an interrupt condition occurs, regardless of the state of its
               corresponding enable bit or the global enable bit. User software will ensure the appropriate
               interrupt flag bits are clear prior to enabling an interrupt.


--- p177 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.39 IPR0

            Name:       IPR0
            Address:    0x362

            Peripheral Interrupt Request Register 0

      Bit        7              6         5               4                3            2             1               0
               IOCIP                    CLC1IP                           CSWIP        OSFIP         HLVDIP           SWIP
  Access        R/W                      R/W                              R/W          R/W           R/W             R/W
   Reset         1                        1                                1            1             1               1

Bit 7 – IOCIP Interrupt-on-Change Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 5 – CLC1IP CLC1 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 3 – CSWIP Clock Switch Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 2 – OSFIP Oscillator Failure Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 1 – HLVDIP High/Low-Voltage Detect Priority Flag
            Value      Description
            1          High Priority
            0          Low Priority

Bit 0 – SWIP Software Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority


--- p178 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.40 IPR1

            Name:       IPR1
            Address:    0x363

            Peripheral Interrupt Priority Register 1

      Bit    7                6            5              4              3              2             1               0
         SMT1PWAIP        SMT1PRAIP      SMT1IP         CM1IP          ACTIP           ADIP         ZCDIP           INT0IP
  Access    R/W             R/W           R/W            R/W            R/W            R/W           R/W             R/W
   Reset     1                1            1              1              1              1             1               1

Bit 7 – SMT1PWAIP SMT1 Pulse-Width Acquisition Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 6 – SMT1PRAIP SMT1 Period Acquisition Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 5 – SMT1IP SMT1 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 4 – CM1IP CMP1 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 3 – ACTIP Active Clock Tuning Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 2 – ADIP ADC Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 1 – ZCDIP ZCD Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 0 – INT0IP External Interrupt 0 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority


--- p179 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                VIC - Vectored Interrupt Controller
                                                                                                                           Module
11.13.41 IPR2

            Name:        IPR2
            Address:     0x364

            Peripheral Interrupt Priority Register 2

      Bit        7            6         5          4                       3                2            1              0
              DMA1AIP      DMA1ORIP DMA1DCNTIP DMA1SCNTIP                                                             ADTIP
  Access        R/W          R/W       R/W        R/W                                                                  R/W
   Reset         1            1         1          1                                                                    1

Bit 7 – DMA1AIP DMA1 Abort Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – DMA1ORIP DMA1 Overrun Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – DMA1DCNTIP DMA1 Destination Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – DMA1SCNTIP DMA1 Source Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – ADTIP ADC Threshold Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p180 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                          Module
11.13.42 IPR3

            Name:        IPR3
            Address:     0x365

            Peripheral Interrupt Priority Register 3

      Bit        7             6            5            4               3              2               1               0
               TMR0IP        CCP1IP      TMR1GIP       TMR1IP          TMR2IP         SPI1IP        SPI1TXIP        SPI1RXIP
  Access        R/W           R/W          R/W          R/W             R/W            R/W            R/W             R/W
   Reset         1             1            1            1               1              1               1               1

Bit 7 – TMR0IP TMR0 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – CCP1IP CCP1 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – TMR1GIP TMR1 Gate Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – TMR1IP TMR1 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – TMR2IP TMR2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – SPI1IP SPI1 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – SPI1TXIP SPI1 Transmit Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – SPI1RXIP SPI1 Receive Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p181 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                          Module
11.13.43 IPR4

            Name:       IPR4
            Address:    0x366

            Peripheral Interrupt Priority Register 4

      Bit       7             6             5              4                   3         2             1               0
              PWM1IP       PWM1PIP                                            U1IP     U1EIP         U1TXIP          U1RXIP
  Access       R/W           R/W                                              R/W       R/W           R/W             R/W
   Reset        1             1                                                1         1             1               1

Bit 7 – PWM1IP PWM1 Parameter Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 6 – PWM1PIP PWM1 Period Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 3 – U1IP UART1 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 2 – U1EIP UART1 Framing Error Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 1 – U1TXIP UART1 Transmit Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 0 – U1RXIP UART 1 Receive Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority


--- p182 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                          Module
11.13.44 IPR5

            Name:       IPR5
            Address:    0x367

            Peripheral Interrupt Priority Register 5

      Bit       7             6             5            4                 3            2               1               0
              PWM2IP       PWM2PIP       TMR3GIP       TMR3IP                         SPI2IP        SPI2TXIP        SPI2RXIP
  Access       R/W           R/W           R/W          R/W                            R/W            R/W             R/W
   Reset        1             1             1            1                              1               1               1

Bit 7 – PWM2IP PWM2 Parameter Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 6 – PWM2PIP PWM2 Period Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 5 – TMR3GIP TMR3 Gate Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 4 – TMR3IP TMR3 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 2 – SPI2IP SPI2 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 1 – SPI2TXIP SPI2 Transmit Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 0 – SPI2RXIP SPI2 Receive Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority


--- p183 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.45 IPR6

            Name:        IPR6
            Address:     0x368

            Peripheral Interrupt Priority Register 6

      Bit        7            6         5          4                    3              2              1               0
              DMA2AIP      DMA2ORIP DMA2DCNTIP DMA2SCNTIP             NCO1IP         CWG1IP         CLC2IP          INT1IP
  Access        R/W          R/W       R/W        R/W                  R/W            R/W            R/W             R/W
   Reset         1            1         1          1                    1              1              1               1

Bit 7 – DMA2AIP DMA2 Abort Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – DMA2ORIP DMA2 Overrun Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – DMA2DCNTIP DMA2 Destination Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – DMA2SCNTIP DMA2 Source Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – NCO1IP NCO1 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – CWG1IP CWG1 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – CLC2IP CLC2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – INT1IP External Interrupt 1 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p184 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                          Module
11.13.46 IPR7

            Name:       IPR7
            Address:    0x369

            Peripheral Interrupt Priority Register 7

      Bit       7             6            5               4                3            2             1                0
              PWM3IP       PWM3PIP       CLC3IP                          I2C1EIP      I2C1IP        I2C1TXIP        I2C1RXIP
  Access       R/W           R/W          R/W                              R/W         R/W            R/W             R/W
   Reset        1             1            1                                1            1             1                1

Bit 7 – PWM3IP PWM3 Parameter Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 6 – PWM3PIP PWM3 Period Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 5 – CLC3IP CLC3 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 3 – I2C1EIP I2C1 Error Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 2 – I2C1IP I2C1 Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 1 – I2C1TXIP I2C1 Transmit Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority

Bit 0 – I2C1RXIP I2C1 Receive Interrupt Priority
            Value      Description
            1          High Priority
            0          Low Priority


--- p185 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                          Module
11.13.47 IPR8

            Name:        IPR8
            Address:     0x36A

            Peripheral Interrupt Priority Register 8

      Bit        7             6           5             4                  3            2             1               0
               SCANIP        CCP2IP     TMR5GIP        TMR5IP              U2IP        U2EIP         U2TXIP          U2RXIP
  Access        R/W           R/W         R/W           R/W                R/W          R/W           R/W             R/W
   Reset         1             1           1             1                  1            1             1               1

Bit 7 – SCANIP Memory Scanner Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – CCP2IP CCP2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – TMR5GIP TMR5 Gate Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – TMR5IP TMR5 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – U2IP UART2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – U2EIP UART2 Framing Error Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – U2TXIP UART2 Transmit Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – U2RXIP UART2 Receive Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p186 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                               VIC - Vectored Interrupt Controller
                                                                                                                          Module
11.13.48 IPR9

            Name:        IPR9
            Address:     0x36B

            Peripheral Interrupt Priority Register 9

      Bit           7            6         5               4                   3         2             1               0
                                         CLC4IP                               U3IP     U3EIP         U3TXIP          U3RXIP
  Access                                  R/W                                 R/W       R/W           R/W             R/W
   Reset                                   1                                   1         1             1               1

Bit 5 – CLC4IP CLC4 Priority Flag
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – U3IP UART3 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – U3EIP UART3 Framing Error Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – U3TXIP UART3 Transmit Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – U3RXIP UART3 Receive Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p187 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.49 IPR10

            Name:        IPR10
            Address:     0x36C

            Peripheral Interrupt Priority Register 10

      Bit        7            6         5          4                   3              2              1               0
              DMA3AIP      DMA3ORIP DMA3DCNTIP DMA3SCNTIP            NCO2IP         CWG2IP         CLC5IP          INT2IP
  Access        R/W          R/W       R/W        R/W                 R/W            R/W            R/W             R/W
   Reset         1            1         1          1                   1              1              1               1

Bit 7 – DMA3AIP DMA3 Abort Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – DMA3ORIP DMA3 Overrun Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – DMA3DCNTIP DMA3 Destination Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – DMA3SCNTIP DMA3 Source Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – NCO2IP NCO2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – CWG2IP CWG2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – CLC5IP CLC5 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – INT2IP External Interrupt 2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p188 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.50 IPR11

            Name:        IPR11
            Address:     0x36D

            Peripheral Interrupt Priority Register 11

      Bit        7            6         5          4                    3             2              1               0
              DMA4AIP      DMA4ORIP DMA4DCNTIP DMA4SCNTIP             TMR4IP        CWG3IP         CLC6IP          CCP3IP
  Access        R/W          R/W       R/W        R/W                  R/W           R/W            R/W             R/W
   Reset         1            1         1          1                    1             1              1               1

Bit 7 – DMA4AIP DMA4 Abort Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – DMA4ORIP DMA4 Overrun Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – DMA4DCNTIP DMA4 Destination Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – DMA4SCNTIP DMA4 Source Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – TMR4IP TMR4 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – CWG3IP CWG3 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – CLC6IP CLC6 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – CCP3IP CCP3 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p189 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.51 IPR12

            Name:        IPR12
            Address:     0x36E

            Peripheral Interrupt Priority Register 12

      Bit        7            6         5          4                       3            2             1               0
              DMA5AIP      DMA5ORIP DMA5DCNTIP DMA5SCNTIP                 U4IP        U4EIP         U4TXIP          U4RXIP
  Access        R/W          R/W       R/W        R/W                     R/W          R/W           R/W             R/W
   Reset         1            1         1          1                       1            1             1               1

Bit 7 – DMA5AIP DMA5 Abort Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – DMA5ORIP DMA5 Overrun Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – DMA5DCNTIP DMA5 Destination Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – DMA5SCNTIP DMA5 Source Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – U4IP UART 4 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – U4EIP UART4 Framing Error Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – U4TXIP UART4 Transmit Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – U4RXIP UART4 Receive Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p190 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.52 IPR13

            Name:        IPR13
            Address:     0x36F

            Peripheral Interrupt Priority Register 13

      Bit        7            6         5          4                       3            2             1               0
              DMA6AIP      DMA6ORIP DMA6DCNTIP DMA6SCNTIP                 U5IP        U5EIP         U5TXIP          U5RXIP
  Access        R/W          R/W       R/W        R/W                     R/W          R/W           R/W             R/W
   Reset         1            1         1          1                       1            1             1               1

Bit 7 – DMA6AIP DMA6 Abort Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 6 – DMA6ORIP DMA6 Overrun Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 5 – DMA6DCNTIP DMA6 Destination Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 4 – DMA6SCNTIP DMA6 Source Count Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 3 – U5IP UART5 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – U5EIP UART5 Framing Error Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – U5TXIP UART5 Transmit Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – U5RXIP UART5 Receive Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p191 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                             VIC - Vectored Interrupt Controller
                                                                                                                        Module
11.13.53 IPR14

            Name:        IPR14
            Address:     0x370

            Peripheral Interrupt Priority Register 14

      Bit           7            6          5             4               3            2             1                0
                                                                        NCO3IP       CM2IP         CLC7IP
  Access                                                                 R/W          R/W           R/W
   Reset                                                                  1            1             1

Bit 3 – NCO3IP NCO3 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – CM2IP CMP2 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – CLC7IP CLC7 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p192 ---
                                                                                                            PIC18F27/47/57Q43
                                                                                              VIC - Vectored Interrupt Controller
                                                                                                                         Module
11.13.54 IPR15

            Name:        IPR15
            Address:     0x371

            Peripheral Interrupt Priority Register 15

      Bit           7            6          5             4               3             2             1               0
                                                                        TMR6IP        CRCIP         CLC8IP          NVMIP
  Access                                                                 R/W           R/W           R/W             R/W
   Reset                                                                  1             1             1               1

Bit 3 – TMR6IP TMR6 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 2 – CRCIP CRC Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 1 – CLC8IP CLC8 Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority

Bit 0 – NVMIP NVM Interrupt Priority
            Value       Description
            1           High Priority
            0           Low Priority


--- p193 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                    VIC - Vectored Interrupt Controller
                                                                                                                               Module
11.14 Register Summary - Interrupts
Address    Name      Bit Pos.       7            6           5             4                 3         2            1            0
 0x0362     IPR0       7:0        IOCIP                 CLC1IP                          CSWIP       OSFIP        HLVDIP         SWIP
 0x0363     IPR1       7:0      SMT1PWAIP    SMT1PRAIP  SMT1IP     CM1IP                ACTIP       ADIP         ZCDIP         INT0IP
 0x0364     IPR2       7:0       DMA1AIP     DMA1ORIP DMA1DCNTIP DMA1SCNTIP                                                    ADTIP
0x0365      IPR3       7:0       TMR0IP       CCP1IP   TMR1GIP     TMR1IP              TMR2IP       SPI1IP       SPI1TXIP     SPI1RXIP
0x0366      IPR4       7:0      PWM1IP       PWM1PIP                                    U1IP        U1EIP         U1TXIP       U1RXIP
0x0367      IPR5       7:0      PWM2IP       PWM2PIP   TMR3GIP     TMR3IP                           SPI2IP       SPI2TXIP     SPI2RXIP
0x0368      IPR6       7:0      DMA2AIP      DMA2ORIP DMA2DCNTIP DMA2SCNTIP            NCO1IP      CWG1IP         CLC2IP       INT1IP
0x0369      IPR7       7:0      PWM3IP       PWM3PIP    CLC3IP                         I2C1EIP      I2C1IP       I2C1TXIP     I2C1RXIP
0x036A      IPR8       7:0       SCANIP       CCP2IP   TMR5GIP     TMR5IP                U2IP       U2EIP         U2TXIP       U2RXIP
0x036B      IPR9       7:0                              CLC4IP                           U3IP       U3EIP         U3TXIP       U3RXIP
0x036C     IPR10       7:0      DMA3AIP      DMA3ORIP DMA3DCNTIP DMA3SCNTIP            NCO2IP      CWG2IP         CLC5IP       INT2IP
0x036D     IPR11       7:0      DMA4AIP      DMA4ORIP DMA4DCNTIP DMA4SCNTIP            TMR4IP      CWG3IP         CLC6IP       CCP3IP
0x036E     IPR12       7:0      DMA5AIP      DMA5ORIP DMA5DCNTIP DMA5SCNTIP              U4IP       U4EIP         U4TXIP       U4RXIP
0x036F     IPR13       7:0      DMA6AIP      DMA6ORIP DMA6DCNTIP DMA6SCNTIP              U5IP       U5EIP         U5TXIP       U5RXIP
0x0370     IPR14       7:0                                                             NCO3IP       CM2IP         CLC7IP
0x0371     IPR15       7:0                                                             TMR6IP       CRCIP         CLC8IP       NVMIP
0x0372
  ...     Reserved
0x0375
0x0376    SHADCON      7:0                                                                                                    SHADLO
0x0377
  ...     Reserved
0x0458
0x0459    IVTLOCK       7:0                                                                                                  IVTLOCKED
                        7:0                                                    IVTADL[7:0]
 0x045A    IVTAD       15:8                                                    IVTADH[7:0]
                      23:16                                                                       IVTADU[4:0]
                        7:0                                                IVTBASEL[7:0]
0x045D    IVTBASE      15:8                                                IVTBASEH[7:0]
                      23:16                                                                      IVTBASEU[4:0]
0x0460
   ...    Reserved
0x049D
0x049E     PIE0        7:0         IOCIE                CLC1IE                          CSWIE       OSFIE        HLVDIE         SWIE
0x049F     PIE1        7:0      SMT1PWAIE    SMT1PRAIE  SMT1IE     CM1IE                ACTIE       ADIE         ZCDIE         INT0IE
0x04A0     PIE2        7:0       DMA1AIE     DMA1ORIE DMA1DCNTIE DMA1SCNTIE                                                     ADTIE
0x04A1     PIE3        7:0        TMR0IE       CCP1IE  TMR1GIE     TMR1IE              TMR2IE       SPI1IE       SPI1TXIE     SPI1RXIE
0x04A2     PIE4        7:0       PWM1IE       PWM1PIE                                   U1IE        U1EIE         U1TXIE       U1RXIE
0x04A3     PIE5        7:0       PWM2IE       PWM2PIE  TMR3GIE     TMR3IE                           SPI2IE       SPI2TXIE     SPI2RXIE
0x04A4     PIE6        7:0       DMA2AIE     DMA2ORIE DMA2DCNTIE DMA2SCNTIE            NCO1IE      CWG1IE         CLC2IE       INT1IE
0x04A5     PIE7        7:0       PWM3IE       PWM3PIE   CLC3IE                         I2C1EIE      I2C1IE       I2C1TXIE     I2C1RXIE
0x04A6     PIE8        7:0        SCANIE       CCP2IE  TMR5GIE     TMR5IE                U2IE       U2EIE         U2TXIE       U2RXIE
0x04A7     PIE9        7:0                              CLC4IE                           U3IE       U3EIE         U3TXIE       U3RXIE
0x04A8     PIE10       7:0       DMA3AIE     DMA3ORIE DMA3DCNTIE DMA3SCNTIE            NCO2IE      CWG2IE         CLC5IE       INT2IE
0x04A9     PIE11       7:0       DMA4AIE     DMA4ORIE DMA4DCNTIE DMA4SCNTIE            TMR4IE      CWG3IE         CLC6IE       CCP3IE
0x04AA     PIE12       7:0       DMA5AIE     DMA5ORIE DMA5DCNTIE DMA5SCNTIE              U4IE       U4EIE         U4TXIE       U4RXIE
0x04AB     PIE13       7:0       DMA6AIE     DMA6ORIE DMA6DCNTIE DMA6SCNTIE              U5IE       U5EIE         U5TXIE       U5RXIE
0x04AC     PIE14       7:0                                                             NCO3IE       CM2IE         CLC7IE
0x04AD     PIE15       7:0                                                             TMR6IE       CRCIE         CLC8IE       NVMIE
0x04AE     PIR0        7:0         IOCIF                CLC1IF                          CSWIF       OSFIF         HLVDIF        SWIF
0x04AF     PIR1        7:0      SMT1PWAIF    SMT1PRAIF  SMT1IF     CM1IF                ACTIF        ADIF          ZCDIF       INT0IF
0x04B0     PIR2        7:0       DMA1AIF     DMA1ORIF DMA1DCNTIF DMA1SCNTIF                                                     ADTIF
0x04B1     PIR3        7:0        TMR0IF       CCP1IF  TMR1GIF     TMR1IF              TMR2IF       SPI1IF       SPI1TXIF     SPI1RXIF
0x04B2     PIR4        7:0       PWM1IF       PWM1PIF                                   U1IF        U1EIF         U1TXIF       U1RXIF
0x04B3     PIR5        7:0       PWM2IF       PWM2PIF  TMR3GIF     TMR3IF                           SPI2IF       SPI2TXIF     SPI2RXIF
0x04B4     PIR6        7:0       DMA2AIF     DMA2ORIF DMA2DCNTIF DMA2SCNTIF            NCO1IF      CWG1IF         CLC2IF       INT1IF
0x04B5     PIR7        7:0       PWM3IF       PWM3PIF   CLC3IF                         I2C1EIF      I2C1IF       I2C1TXIF     I2C1RXIF
0x04B6     PIR8        7:0        SCANIF       CCP2IF  TMR5GIF     TMR5IF                U2IF       U2EIF         U2TXIF       U2RXIF
0x04B7     PIR9        7:0                              CLC4IF                           U3IF       U3EIF         U3TXIF       U3RXIF


--- p194 ---
                                                                                                                    PIC18F27/47/57Q43
                                                                                                      VIC - Vectored Interrupt Controller
                                                                                                                                 Module
...........continued
 Address               Name    Bit Pos.       7             6         5             4         3         2           1             0
  0x04B8               PIR10     7:0      DMA3AIF      DMA3ORIF   DMA3DCNTIF DMA3SCNTIF    NCO2IF    CWG2IF       CLC5IF       INT2IF
  0x04B9               PIR11     7:0      DMA4AIF      DMA4ORIF   DMA4DCNTIF DMA4SCNTIF    TMR4IF    CWG3IF       CLC6IF       CCP3IF
  0x04BA               PIR12     7:0      DMA5AIF      DMA5ORIF   DMA5DCNTIF DMA5SCNTIF     U4IF      U4EIF       U4TXIF       U4RXIF
  0x04BB               PIR13     7:0      DMA6AIF      DMA6ORIF   DMA6DCNTIF DMA6SCNTIF     U5IF      U5EIF       U5TXIF       U5RXIF
 0x04BC                PIR14     7:0                                                       NCO3IF     CM2IF       CLC7IF
 0x04BD                PIR15     7:0                                                       TMR6IF     CRCIF       CLC8IF        NVMIF
 0x04BE
    ...           Reserved
 0x04D5
 0x04D6           INTCON0        7:0      GIE/GIEH         GIEL      IPEN                            INT2EDG     INT1EDG       INT0EDG
 0x04D7           INTCON1        7:0             STAT[1:0]


--- p195 ---
