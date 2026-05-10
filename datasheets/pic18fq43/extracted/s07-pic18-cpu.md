                                                                                                                                  PIC18F27/47/57Q43
                                                                                                                                           PIC18 CPU


7.    PIC18 CPU
      This family of devices contains a PIC18 8-bit CPU core based on the modified Harvard architecture.
      The PIC18 CPU supports:
      •   System arbitration which decides memory access allocation depending on user priorities
      •   Vectored interrupt capability with automatic two-level deep context saving
      •   127-level deep hardware stack with overflow and underflow Reset capabilities
      •   Support Direct, Indirect, and Relative Addressing modes
      •   8x8 hardware multiplier

      Figure 7-1. Family Block Diagram

                            Table Pointer

                            inc/dec logic
                                                 PCLATU PCLATH
                                                                                                  Data Latch
                                                         PCU PCH PCL
                                                      Program Counter                            Data Memory

                                                                                                Address Latch

                                                      128-Level Stack
                           Address Latch                                                         Data Address
                                                         STKPTR
                          Program Memory
                                                                                        BSR      FSR0        Access
                                                                                                 FSR1         Bank
                             Data Latch
                                                                                                 FSR2

                                                                                                inc/dec
                                                        Table Latch                               logic


                                                                                                                       Data Bus
                                                         Instruction                            Address
                                    Instruction Bus                                             Decode
                                                           Latch


                                                         Instruction                               PRODH PRODL
                                                                          State Machine
                                                        Decode and
                                                                          Control Signals
                                                           Control                                      8x8 Multiply


                                                                                        BITOP        W


                                                                                                     ALU


7.1   System Arbitration
      The system arbiter resolves memory access between the system level selections (i.e., Main, Interrupt
      Service Routine) and peripheral selection (e.g., DMA and Scanner) based on user-assigned priorities.
      A block diagram of the system arbiter can be found below. Each of the system level and peripheral
      selections has its own priority selection registers. Memory access priority is resolved using the
      number written to the corresponding Priority registers, '0' being the highest priority selection and
      the maximum value being the lowest priority. All system level and peripheral level selections default


--- p28 ---
                                                                                                                          PIC18F27/47/57Q43
                                                                                                                                   PIC18 CPU

        to the lowest priority configuration. If the same value is in two or more Priority registers, priority is
        given to the higher-listed selection according to the following table.


                      Important: When the PRLOCKED bit is set, the Non Volatile Memory (NVM)
                      module has a fixed priority of '0' that cannot be changed. If an interrupt is desired
                      when an NVM read/write operation is in progress, then the ISR priority level must
                      be set to '0'. The NVM module priority is ignored when PRLOCKED bit is cleared.


        Table 7-1. Default Priorities
                                         Selection                                                   Priority Register Reset Value
                   System Level                                     ISR                                           7
                                                               MAIN                                               7
                    Peripheral                                 DMA1                                               7
                                                               DMA2                                               7
                                                               DMA3                                               7
                                                               DMA4                                               7
                                                               DMA5                                               7
                                                               DMA6                                               7
                                                             SCANNER                                              7

        Figure 7-2. System Arbiter Block Diagram

                                                              Memory
                                                                                                  Program Flash
                                             CPU              Access                Scanner                     Data EEPROM
                                                                                                     Memory
                                                             NVMCON


                         Priority                                                System Arbiter


                                                                                                                  SFR/GRP
                                            DMA 1             DMA 2              .......            DMA n
                                                                                                                 SRAM Data


                         Legend
                                        Program Flash Memory Data
                                        Data EEPROM Data
                                        SFR/GPR Data


7.1.1   Priority Lock
        The system arbiter grants memory access to the peripheral selections (DMAx, Scanner) as long as
        the PRLOCKED bit is set. Priority selections are locked by setting the PRLOCKED bit. Setting and
        clearing this bit requires a special sequence as an extra precaution against inadvertent changes. The
        following code examples demonstrate the Priority Lock and Priority Unlock sequences.


--- p29 ---
                                                                                                PIC18F27/47/57Q43
                                                                                                         PIC18 CPU

                Example 7-1. Priority Lock Sequence

                 INTCON0bits.GIE = 0;            // Disable Interrupts;
                 PRLOCK = 0x55;
                 PRLOCK = 0xAA;
                 PRLOCKbits.PRLOCKED = 1;        // Grant memory access to peripherals;
                 INTCON0bits.GIE = 1;            // Enable Interrupts;


                Example 7-2. Priority Unlock Sequence

                 INTCON0bits.GIE = 0;            // Disable Interrupts;
                 PRLOCK = 0x55;
                 PRLOCK = 0xAA;
                 PRLOCKbits.PRLOCKED = 0;        // Allow changing priority settings;
                 INTCON0bits.GIE = 1;            // Enable Interrupts;


7.2     Memory Access Scheme
        The user can assign priorities to both system level and peripheral selections based on which the
        system arbiter grants memory access. Consider the following priority scenarios between ISR, MAIN
        and peripherals.

7.2.1   ISR Priority > Main Priority > Peripheral Priority
        When the peripheral priority (e.g., DMA, Scanner) is lower than ISR and MAIN priority, and the
        peripheral requires:
        1. Access to the Program Flash Memory, then the peripheral waits for an instruction cycle in which
           the CPU does not need to access the PFM (such as a branch instruction) and uses that cycle to do
           its own Program Flash Memory access, unless a PFM Read/Write operation is in progress.
        2. Access to the SFR/GPR, then the peripheral waits for an instruction cycle in which the CPU does
           not need to access the SFR/GPR (such as MOVLW, CALL, NOP) and uses that cycle to do its own
           SFR/GPR access.
        3. Access to the Data EEPROM, then the peripheral has access to Data EEPROM unless a Data
           EEPROM Read/Write operation is being performed.
        This results in the lowest throughput for the peripheral to access the memory and does so without
        any impact on execution times.

7.2.2   Peripheral Priority > ISR Priority > Main Priority
        When the peripheral priority (DMA, Scanner) is higher than ISR and MAIN priority, the CPU operation
        is stalled when the peripheral requests memory. The CPU is held in its current state until the
        peripheral completes its operation. This results in the highest throughput for the peripheral to
        access the memory but has the cost of stalling other execution while it occurs.

7.2.3   ISR Priority > Peripheral Priority > Main Priority
        In this case, interrupt routines and peripheral operation (DMAx, Scanner) will stall the Main loop.
        Interrupt will preempt peripheral operation, which results in lowest interrupt latency.

7.2.4   Peripheral 1 Priority > ISR Priority > Main Priority > Peripheral 2 Priority
        In this case, the Peripheral 1 will stall the execution of the CPU. However, Peripheral 2 can access the
        memory in cycles unused by Peripheral 1, ISR and the Main Routine.

7.3     8x8 Hardware Multiplier
        This device includes an 8x8 hardware multiplier as part of the ALU within the CPU. The multiplier
        performs an unsigned operation and yields a 16-bit result that is stored in the product register,
        PROD. The multiplier’s operation does not affect any flags in the STATUS register.


--- p30 ---
                                                                                                               PIC18F27/47/57Q43
                                                                                                                        PIC18 CPU

        Making multiplication a hardware operation allows it to be completed in a single instruction
        cycle. This has the advantages of higher computational throughput and reduced code size for
        multiplication algorithms and allows the device to be used in many applications previously reserved
        for digital signal processors. A comparison of various hardware and software multiply operations,
        along with the savings in memory and execution time, is shown in Table 7-2.

        Table 7-2. Performance Comparison for Various Multiply Operations
                                                           Program                                    Time
                                                                      Cycles
             Routine              Multiply Method          Memory
                                                                      (Max)      @ 64 MHz   @ 40 MHz     @ 10 MHz          @ 4 MHz
                                                           (Words)
                          Without hardware multiply           13           69     4.3 μs     6.9 μs          27.6 μs        69 μs
        8x8 unsigned
                          Hardware multiply                    1            1     62.5 ns    100 ns          400 ns          1 μs
                          Without hardware multiply           33           91     5.7 μs     9.1 μs          36.4 μs        91 μs
        8x8 signed
                          Hardware multiply                    6            6     375 ns     600 ns           2.4 μs         6 μs
                          Without hardware multiply           21           242    15.1 μs    24.2 μs         96.8 μs        242 μs
        16x16 unsigned
                          Hardware multiply                   28           28     1.8 μs     2.8 μs          11.2 μs        28 μs
                          Without hardware multiply           52           254    15.9 μs    25.4 μs         102.6 μs       254 μs
        16x16 signed
                          Hardware multiply                   35           40     2.5 μs     4.0 μs          16.0 μs        40 μs


7.3.1   Operation
        Example 7-3 shows the instruction sequence for an 8x8 unsigned multiplication. Only one
        instruction is required when one of the arguments is already loaded in the WREG register. Example
        7-4 shows the sequence to do an 8x8 signed multiplication. To account for the sign bits of the
        arguments, each argument’s Most Significant bit (MSb) is tested and the appropriate subtractions
        are done.

                Example 7-3. 8x8 Unsigned Multiply Routine

                          MOVF       ARG1, W      ;

                          MULWF      ARG2         ; ARG1 * ARG2 -> PRODH:PRODL


                Example 7-4. 8x8 Signed Multiply Routine

                          MOVF       ARG1, W
                          MULWF      ARG2           ; ARG1 * ARG2 -> PRODH:PRODL
                          BTFSC      ARG2, SB       ; Test Sign Bit
                          SUBWF      PRODH, F       ; PRODH = PRODH - ARG1
                          MOVF       ARG2, W
                          BTFSC      ARG1, SB       ; Test Sign Bit
                          SUBWF      PRODH, F       ; PRODH = PRODH - ARG2


7.3.2   16x16 Unsigned Multiplication Algorithm
        Example 7-6 shows the sequence to do a 16x16 unsigned multiplication. Example 7-5 shows the
        algorithm that is used. The 32-bit result is stored in four registers.

                Example 7-5. 16x16 Unsigned Multiply Algorithm

                RES3: RES0 = ARG1H: ARG1L • ARG2H: ARG2L = ARG1H • ARG2H • 216 + ARG1H
                • ARG2L • 28 + ARG1L • ARG2H • 28 + ARG1L • ARG2L


--- p31 ---
                                                                                                 PIC18F27/47/57Q43
                                                                                                          PIC18 CPU

                Example 7-6. 16x16 Unsigned Multiply Routine

                          MOVF     ARG1L, W
                          MULWF    ARG2L             ; ARG1L * ARG2L → PRODH:PRODL
                          MOVFF    PRODH, RES1       ;
                          MOVFF    PRODL, RES0       ;
                 ;
                          MOVF     ARG1H, W          ;
                          MULWF    ARG2H             ; ARG1H * ARG2H → PRODH:PRODL
                          MOVFF    PRODH, RES3       ;
                          MOVFF    PRODL, RES2       ;
                 ;
                          MOVF     ARG1L, W
                          MULWF    ARG2H             ; ARG1L * ARG2H → PRODH:PRODL
                          MOVF     PRODL, W          ;
                          ADDWF    RES1, F           ; Add cross products
                          MOVF     PRODH, W          ;
                          ADDWFC   RES2, F           ;
                          CLRF     WREG              ;
                          ADDWFC   RES3, F           ;
                 ;
                          MOVF     ARG1H, W          ;
                          MULWF    ARG2L             ; ARG1H * ARG2L → PRODH:PRODL
                          MOVF     PRODL, W          ;
                          ADDWF    RES1, F           ; Add cross products
                          MOVF     PRODH, W          ;
                          ADDWFC   RES2, F           ;
                          CLRF     WREG              ;
                          ADDWFC   RES3, F           ;


7.3.3   16x16 Signed Multiplication Algorithm
        Example 7-8 shows the sequence to do a 16x16 signed multiply. Example 7-7 shows the algorithm
        used. The 32-bit result is stored in four registers. To account for the sign bits of the arguments, the
        MSb for each argument pair is tested and the appropriate subtractions are done.

                Example 7-7. 16x16 Signed Multiply Algorithm

                RES3: RES0 = ARG1H: ARG1L • ARG2H: ARG2L = ARG1H • ARG2H • 216 + ARG1H
                • ARG2L • 28 + ARG1L • ARG2H • 28 + ARG1L • ARG2L + − 1 • ARG2H < 7 >
                • ARG1H: ARG1L • 216 + − 1 • ARG1H < 7 > • ARG2H: ARG2L • 216


                Example 7-8. 16x16 Signed Multiply Routine

                          MOVF     ARG1L, W
                          MULW     ARG2L             ; ARG1L * ARG2L → PRODH:PRODL
                          MOVF     PRODH, RES1       ;
                          MOVFF    PRODL, RES0       ;
                 ;
                          MOVF     ARG1H, W
                          MULWF    ARG2H             ; ARG1H * ARG2H → PRODH:PRODL
                          MOVFF    PRODH, RES3       ;
                          MOVFF    PRODL, RES2       ;
                 ;
                          MOVF     ARG1L, W
                          MULWF    ARG2H             ; ARG1L * ARG2H → PRODH:PRODL
                          MOVF     PRODL, W          ;
                          ADDWF    RES1, F           ; Add cross products
                          MOVF     PRODH, W          ;
                          ADDWFC   RES2, F           ;
                          CLRF     WREG              ;
                          ADDWFC   RES3, F           ;
                 ;
                          MOVF     ARG1H, W          ;
                          MULWF    ARG2L             ; ARG1H * ARG2L → PRODH:PRODL


--- p32 ---
                                                                                                             PIC18F27/47/57Q43
                                                                                                                      PIC18 CPU
                             MOVF     PRODL, W           ;
                             ADDWF    RES1, F            ; Add cross products
                             MOVF     PRODH, W           ;
                             ADDWFC   RES2, F            ;
                             CLRF     WREG               ;
                             ADDWFC   RES3, F            ;
                  ;
                             BTFSS    ARG2H, 7           ; ARG2H:ARG2L neg?
                             BRA      SIGN_ARG1          ; no, check ARG1
                             MOVF     ARG1L, W           ;
                             SUBWF    RES2               ;
                             MOVF     ARG1H, W           ;
                             SUBWFB   RES3
                  ;

                  SIGN_ARG1:
                          BTFSS       ARG1H, 7           ; ARG1H:ARG1L neg?
                          BRA         CONT_CODE          ; no, done
                          MOVF        ARG2L, W           ;
                          SUBWF       RES2               ;
                          MOVF        ARG2H, W           ;
                          SUBWFB      RES3
                  ;
                  CONT_CODE:
                             :


7.4     PIC18 Instruction Cycle
7.4.1   Instruction Flow/Pipelining
        An “Instruction Cycle” consists of four cycles of the oscillator clock. The instruction fetch and execute
        are pipelined in such a manner that a fetch takes one instruction cycle, while the decode and
        execute take another instruction cycle. However, due to the pipelining, each instruction effectively
        executes in one cycle. If an instruction causes the Program Counter (PC) to change (e.g., GOTO), then
        two cycles are required to complete the instruction (Figure 7-3).
        A fetch cycle begins with the Program Counter (PC) incrementing followed by the execution cycle.
        In the execution cycle, the fetched instruction is latched onto the Instruction Register (IR). This
        instruction is then decoded and executed during the next few oscillator clock cycles. Data memory is
        read (operand read) and written (destination write) during the execution cycle as well.

        Figure 7-3. Instruction Pipeline Flow
                                                                                                                            Rev. 10-000 337A
                                                                                                                                   2/28/201 9


                                          TCY0          TCY1            TCY2        TCY3         TCY4           TCY5


         1. MOVLW      55h               Fetch 1      Execute 1

         2. MOVWF      PORTB                           Fetch 2        Execute 2

         3. BRA        Sub_1                                           Fetch 3    Execute 3

         4. BSF        PORTA, BITS (Forced NOP)                                    Fetch 4    Flush (NOP)

         5. Instruction @ address Sub_1                                                       Fetch Sub_1   Execute Sub_1


        Note: There are some instructions that take multiple cycles to execute. Refer to the “Instruction
        Set Summary” chapter for details.

7.4.2   Instructions in Program Memory
        The program memory is addressed in bytes. Instructions are stored as either two bytes, four bytes,
        or six bytes in program memory. The Least Significant Byte of an instruction word is always stored in
        a program memory location with an even address (LSb = 0). To maintain alignment with instruction
        boundaries, the PC increments in steps of two and the LSb will always read ‘0’. See the “Program


--- p33 ---
                                                                                                              PIC18F27/47/57Q43
                                                                                                                       PIC18 CPU

        Counter” section in the “Memory Organization” chapter for more details. The instructions in the
        Program Memory figure below shows how instruction words are stored in the program memory.
        The CALL and GOTO instructions have the absolute program memory address embedded into the
        instruction. Since instructions are always stored on word boundaries, the data contained in the
        instruction is a word address. The word address is written to the corresponding bits of the Program
        Counter register, which accesses the desired byte address in program memory. Instruction #2 in
        the example shows how the instruction GOTO 0006h is encoded in the program memory. Program
        branch instructions, which encode a relative address offset, operate in the same manner. The offset
        value stored in a branch instruction represents the number of single-word instructions by which the
        PC will be offset.

        Figure 7-4. Instructions in Program Memory

                                                                                               Word Address
                                                                      LSB = 1       LSB = 0
                                         Program Memory                                          000000h
                                         Byte Locations                                          000002h
                                                                                                 000004h
                                                                                                 000006h
                        Instruction 1:   MOVLW      055h                0Fh           55h        000008h
                        Instruction 2:   GOTO       0006h               EFh           03h        00000Ah
                                                                        F0h           00h        00000Ch
                        Instruction 3:   MOVFF      123h, 456h          C1h           23h        00000Eh
                                                                        F4h           56h        000010h
                        Instruction 4:    MOVFFL       123h, 456h       00h           60h        000012h
                                                                        F4h           8Ch        000014h
                                                                        F4h           56h        000016h
                                                                                                 000018h
                                                                                                 00001Ah


7.4.3   Multi-Word Instructions
        The standard PIC18 instruction set has six two-word instructions: CALL, MOVFF, GOTO, LFSR, MOVSF
        and MOVSS and two three-word instructions: MOVFFL and MOVSFL. In all cases, the second and the
        third word of the instruction always has 1111 as its four Most Significant bits; the other 12 bits are
        literal data, usually a data memory address.
        The use of 1111 in the four MSbs of an instruction specifies a special form of NOP. If the instruction
        is executed in proper sequence, immediately after the first word, the data in the second word is
        accessed and used by the instruction sequence. If the first word is skipped for some reason and the
        second word is executed by itself, a NOP is executed instead. This is necessary for cases when the
        two-word instruction is preceded by a conditional instruction that changes the PC.
        Table 7-3 and Table 7-4 show more details of how two-word instructions work. Table 7-5 and Table
        7-6 show more details of how three-word instructions work.


                      Important: See the “PIC18 Instruction Execution and the Extended
                      Instruction Set” section for information on two-word instructions in the
                      extended instruction set.


        Table 7-3. Two-Word Instructions (Case 1)
        Object Code                      Source Code                                 Comment
        0110 0110 0000 0000              TSTFSZ REG1                                 ; is RAM location 0?
        1100 0001 0101 0011              MOVFF REG1,REG2                             ; No, skip this word


--- p34 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                                                PIC18 CPU

      ...........continued
      Object Code                   Source Code                                 Comment
      1111 0100 0101 0110                                                       ; Execute this word as NOP
      0010 0100 0000 0000           ADDWF REG3                                  ; continue code

      Table 7-4. Two-Word Instructions (Case 2)
      Object Code                   Source Code                                 Comment
      0110 0110 0000 0000           TSTFSZ REG1                                 ; is RAM location 0?
      1100 0001 0101 0011           MOVFF REG1,REG2                             ; Yes, execute this word
      1111 0100 0101 0110                                                       ; 2nd word of instruction
      0010 0100 0000 0000           ADDWF REG3                                  ; continue code

      Table 7-5. Three-Word Instructions (Case 1)
      Object Code                   Source Code                                 Comment
      0110 0110 0000 0000           TSTFSZ REG1                                 ; is RAM location 0?
      0000 0000 0110 0000           MOVFFL REG1,REG2                            ; Yes, skip this word
      1111 0100 1000 1100                                                       ; Execute this word as NOP
      1111 0100 0101 0110                                                       ; Execute this word as NOP
      0010 0100 0000 0000           ADDWF REG3                                  ; continue code

      Table 7-6. Three-Word Instructions (Case 2)
      Object Code                   Source Code                                 Comment
      0110 0110 0000 0000           TSTFSZ REG1                                 ; is RAM location 0?
      0000 0000 0110 0000           MOVFFL REG1,REG2                            ; No, execute this word
      1111 0100 1000 1100                                                       ; 2nd word of instruction
      1111 0100 0101 0110                                                       ; 3rd word of instruction
      0010 0100 0000 0000           ADDWF REG3                                  ; continue code


7.5   STATUS Register
      The STATUS register contains the arithmetic status of the ALU. As with any other SFR, it can be the
      operand for any instruction. If the STATUS register is the destination for an instruction that affects
      the Z, DC, C, OV or N bits, the results of the instruction are not written; instead, the STATUS register
      is updated according to the instruction performed. Therefore, the result of an instruction with the
      STATUS register as its destination may be different than intended. As an example, CLRF STATUS will
      set the Z bit and leave the remaining Status bits unchanged (‘000u u1uu’).
      It is recommended that only BCF, BSF, SWAPF, MOVFF and MOVWF instructions are used to alter the
      STATUS register, because these instructions do not affect the Z, C, DC, OV or N bits in the STATUS
      register. For other instructions that do not affect Status bits, see the instruction set summaries.


                    Important: The C and DC bits operate as the Borrow and Digit Borrow bits,
                    respectively, in subtraction.


7.6   Call Shadow Register
      When CALL instruction is used, the WREG, BSR and STATUS are automatically saved in hardware and
      can be accessed using the WREG_CSHAD, BSR_CSHAD and STATUS_CSHAD registers.


--- p35 ---
                                                                                      PIC18F27/47/57Q43
                                                                                               PIC18 CPU

               Important: The contents of these registers need to be handled correctly to avoid
               erroneous code execution.


7.7   Register Definitions: System Arbiter


--- p36 ---
                                                                                                                       PIC18F27/47/57Q43
                                                                                                                                PIC18 CPU

7.7.1         ISRPR

              Name:       ISRPR
              Address:    0x0BF

              Interrupt Service Routine Priority Register

        Bit        7              6           5              4                  3               2              1                 0
                                                                                                             PR[2:0]
  Access                                                                                      R/W             R/W              R/W
   Reset                                                                                       1               1                1

Bits 2:0 – PR[2:0] Interrupt Service Routine Priority Selection
                                      Value                                                         Description
                                      111                                       System Arbiter Priority Level: 7 (Lowest Priority)
                                      110                                               System Arbiter Priority Level: 6
                                      101                                               System Arbiter Priority Level: 5
                                      100                                               System Arbiter Priority Level: 4
                                      011                                               System Arbiter Priority Level: 3
                                      010                                               System Arbiter Priority Level: 2
                                      001                                               System Arbiter Priority Level: 1
                                      000                                       System Arbiter Priority Level: 0 (Highest Priority)


--- p37 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                                                 PIC18 CPU

7.7.2         MAINPR

              Name:       MAINPR
              Address:    0x0BE

              Main Routine Priority Register

        Bit        7            6              5              4                  3               2              1                 0
                                                                                                              PR[2:0]
  Access                                                                                       R/W             R/W              R/W
   Reset                                                                                        1               1                1

Bits 2:0 – PR[2:0] Main Routine Priority Selection
                                     Value                                                           Description
                                     111                                         System Arbiter Priority Level: 7 (Lowest Priority)
                                     110                                                 System Arbiter Priority Level: 6
                                     101                                                 System Arbiter Priority Level: 5
                                     100                                                 System Arbiter Priority Level: 4
                                     011                                                 System Arbiter Priority Level: 3
                                     010                                                 System Arbiter Priority Level: 2
                                     001                                                 System Arbiter Priority Level: 1
                                     000                                         System Arbiter Priority Level: 0 (Highest Priority)


--- p38 ---
                                                                                                                        PIC18F27/47/57Q43
                                                                                                                                 PIC18 CPU

7.7.3         DMAxPR

              Name:      DMAxPR
              Address:   0x0B6,0x0B7,0x0B8,0x0B9,0x0BA,0x0BB

              DMAx Priority Register

        Bit        7           6               5              4                  3               2              1                 0
                                                                                                              PR[2:0]
  Access                                                                                       R/W             R/W              R/W
   Reset                                                                                        1               1                1

Bits 2:0 – PR[2:0] DMAx Priority Selection
                                       Value                                                         Description
                                       111                                       System Arbiter Priority Level: 7 (Lowest Priority)
                                       110                                               System Arbiter Priority Level: 6
                                       101                                               System Arbiter Priority Level: 5
                                       100                                               System Arbiter Priority Level: 4
                                       011                                               System Arbiter Priority Level: 3
                                       010                                               System Arbiter Priority Level: 2
                                       001                                               System Arbiter Priority Level: 1
                                       000                                       System Arbiter Priority Level: 0 (Highest Priority)


--- p39 ---
                                                                                                                      PIC18F27/47/57Q43
                                                                                                                               PIC18 CPU

7.7.4         SCANPR

              Name:       SCANPR
              Address:    0x0B5

              Scanner Priority Register

        Bit        7            6            5              4                  3               2              1                 0
                                                                                                            PR[2:0]
  Access                                                                                     R/W             R/W              R/W
   Reset                                                                                      1               1                1

Bits 2:0 – PR[2:0] Scanner Priority Selection
                                     Value                                                         Description
                                      111                                      System Arbiter Priority Level: 7 (Lowest Priority)
                                      110                                              System Arbiter Priority Level: 6
                                      101                                              System Arbiter Priority Level: 5
                                      100                                              System Arbiter Priority Level: 4
                                      011                                              System Arbiter Priority Level: 3
                                      010                                              System Arbiter Priority Level: 2
                                      001                                              System Arbiter Priority Level: 1
                                      000                                      System Arbiter Priority Level: 0 (Highest Priority)


--- p40 ---
                                                                                                                     PIC18F27/47/57Q43
                                                                                                                              PIC18 CPU

7.7.5         PRLOCK

              Name:        PRLOCK
              Address:     0x0B4

              Priority Lock Register

        Bit           7            6              5               4                  3            2             1             0
                                                                                                                          PRLOCKED
  Access                                                                                                                     R/W
   Reset                                                                                                                      0

Bit 0 – PRLOCKED PR Register Lock
              Value       Description
              1           Priority registers are locked and cannot be written; Peripherals have access to the memory
              0           Priority registers can be modified by write operations; Peripherals do not have access to the memory


                           Important:
                           1. The PRLOCKED bit can only be set or cleared after the unlock sequence.
                           2. If the Configuration Bit PR1WAY = 1, the PRLOCKED bit cannot be cleared after
                              it has been set. A device Reset will clear the bit and allow one more set.


--- p41 ---
                                                                                                       PIC18F27/47/57Q43
                                                                                                                PIC18 CPU

7.7.6         PROD

              Name:       PROD
              Address:    0x4F3

              Timer Register
              Product Register Pair

        Bit        15           14          13             12          11                10       9             8
                                                             PROD[15:8]
  Access           R/W         R/W          R/W           R/W         R/W               R/W      R/W           R/W
   Reset            0           0            0             0            0                0        0             0

        Bit         7             6          5              4          3                     2    1             0
                                                             PROD[7:0]
  Access           R/W         R/W          R/W           R/W         R/W               R/W      R/W           R/W
   Reset            x           x            x             x           x                 x        x             x

Bits 15:0 – PROD[15:0] PROD Most Significant

              Notes: The individual bytes in this multibyte register can be accessed with the following register
              names:
              • PRODH: Accesses the high byte PROD[15:8]
              •   PRODL: Accesses the low byte PROD[7:0]


--- p42 ---
                                                                                                           PIC18F27/47/57Q43
                                                                                                                    PIC18 CPU

7.7.7         STATUS

              Name:        STATUS
              Address:     0x4D8

              STATUS Register

        Bit           7            6                5              4                 3          2     1             0
                                  TO               PD              N                OV          Z    DC             C
  Access                           R                R             R/W               R/W        R/W   R/W           R/W
   Reset                           1                1              0                 0          0     0             0

Bit 6 – TO Time-Out
          Reset States: POR/BOR = 1
                        All Other Resets = q
              Value       Description
              1           Set at power-up or by execution of the CLRWDT or SLEEP instruction
              0           A WDT time-out occurred

Bit 5 – PD Power-Down
         Reset States: POR/BOR = 1
                       All Other Resets = q
              Value       Description
              1           Set at power-up or by execution of the CLRWDT instruction
              0           Cleared by execution of the SLEEP instruction


Bit 4 – N Negative
         Used for signed arithmetic (two’s complement); indicates if the result is negative (ALU MSb = 1).
         Reset States: POR/BOR = 0
                       All Other Resets = u
              Value       Description
              1           The result is negative
              0           The result is positive

Bit 3 – OV Overflow
         Used for signed arithmetic (two’s complement); indicates an overflow of the 7-bit magnitude, which
         causes the sign bit (bit 7) to change state.
         Reset States: POR/BOR = 0
                       All Other Resets = u
              Value       Description
              1           Overflow occurred for current signed arithmetic operation
              0           No overflow occurred

Bit 2 – Z Zero
          Reset States: POR/BOR = 0
                        All Other Resets = u
              Value       Description
              1           The result of an arithmetic or logic operation is zero
              0           The result of an arithmetic or logic operation is not zero

Bit 1 – DC Digit Carry / Borrow
         ADDWF, ADDLW, SUBLW, SUBWF instructions(1)
         Reset States: POR/BOR = 0
                       All Other Resets = u


--- p43 ---
                                                                                                PIC18F27/47/57Q43
                                                                                                         PIC18 CPU
         Value     Description
         1         A carry-out from the 4th low-order bit of the result occurred
         0         No carry-out from the 4th low-order bit of the result

Bit 0 – C Carry / Borrow
         ADDWF, ADDLW, SUBLW, SUBWF instructions(1,2)
         Reset States: POR/BOR = 0
                       All Other Resets = u
         Value     Description
         1         A carry-out from the Most Significant bit of the result occurred
         0         No carry-out from the Most Significant bit of the result occurred

        Notes:
        1. For Borrow, the polarity is reversed. A subtraction is executed by adding the two’s complement
           of the second operand.
        2. For Rotate (RRCF, RLCF) instructions, this bit is loaded with either the high or low-order bit of the
           Source register.


--- p44 ---
                                                                                                                  PIC18F27/47/57Q43
                                                                                                                           PIC18 CPU

7.8       Register Summary - System Arbiter Control
Address      Name        Bit Pos.   7        6           5             4                 3               2         1            0
  0xB4      PRLOCK         7:0                                                                                              PRLOCKED
  0xB5      SCANPR         7:0                                                                                  PR[2:0]
  0xB6      DMA1PR         7:0                                                                                  PR[2:0]
  0xB7      DMA2PR         7:0                                                                                  PR[2:0]
  0xB8      DMA3PR         7:0                                                                                  PR[2:0]
  0xB9      DMA4PR         7:0                                                                                  PR[2:0]
  0xBA      DMA5PR         7:0                                                                                  PR[2:0]
  0xBB      DMA6PR         7:0                                                                                  PR[2:0]
  0xBC
    ...     Reserved
  0xBD
  0xBE      MAINPR         7:0                                                                                  PR[2:0]
  0xBF       ISRPR         7:0                                                                                  PR[2:0]
  0xC0
    ...     Reserved
 0x0372
 0x0373   STATUS_CSHAD     7:0              TO          PD             N                OV               Z        DC            C
 0x0374    WREG_CSHAD      7:0                                             WREG[7:0]
 0x0375     BSR_CSHAD      7:0                                                               BSR[5:0]
 0x0376      Reserved
 0x0377    STATUS_SHAD     7:0              TO          PD             N                OV               Z        DC            C
 0x0378     WREG_SHAD     7:0                                              WREG[7:0]
 0x0379      BSR_SHAD      7:0                                                               BSR[5:0]
                           7:0                                             PCLATH[7:0]
 0x037A    PCLAT_SHAD
                          15:8                                                                    PCLATU[4:0]
                           7:0                                              FSRL[7:0]
 0x037C    FSR0_SHAD
                          15:8                                                               FSRH[5:0]
                           7:0                                              FSRL[7:0]
 0x037E    FSR1_SHAD
                          15:8                                                               FSRH[5:0]
                           7:0                                              FSRL[7:0]
 0x0380    FSR2_SHAD
                          15:8                                                               FSRH[5:0]
                           7:0                                             PROD[7:0]
 0x0382    PROD_SHAD
                          15:8                                             PROD[15:8]
 0x0384
   ...      Reserved
 0x04D7
 0x04D8      STATUS        7:0              TO          PD             N                OV               Z        DC            C
 0x04D9
   ...      Reserved
 0x04F2
                          7:0                                              PROD[7:0]
 0x04F3      PROD
                          15:8                                             PROD[15:8]


--- p45 ---
