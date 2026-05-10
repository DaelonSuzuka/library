                      PIC18(L)F26/27/45/46/47/55/56/57K42
4.0       MEMORY ORGANIZATION                              4.2       Memory Access Partition (MAP)
There are three types         of   memory    in   PIC18    Program Flash memory is partitioned into:
microcontroller devices:                                   • Application Block
• Program Flash Memory                                     • Boot Block, and
• Data RAM                                                 • Storage Area Flash (SAF) Block
• Data EEPROM
                                                           4.2.1      APPLICATION BLOCK
As Harvard architecture devices, the data and program
memories use separate buses; this allows for               Application block is where the user’s program resides
concurrent access of the two memory spaces. The data       by default. Default settings of the configuration bits
EEPROM, for practical purposes, can be regarded as         (BBEN = 1 and SAFEN = 1) assign all memory in the
a peripheral device, since it is addressed and accessed    program Flash memory area to the application block.
through a set of control registers.                        The WRTAPP configuration bit is used to protect the
Additional detailed information on the operation of the    application block.
Program Flash Memory and Data EEPROM Memory is
provided in Section 13.0 “Nonvolatile Memory               4.2.2      BOOT BLOCK
(NVM) Control”.
                                                           Boot block is an area in program memory that is ideal
                                                           for storing bootloader code. Code placed in this area
4.1       Program Flash Memory                             can be executed by the CPU. The boot block can be
          Organization                                     write-protected, independent of the main application
PIC18 microcontrollers implement a 21-bit program          block. The Boot Block is enabled by the BBEN bit and
counter, which is capable of addressing a 2 Mbyte          size is based on the value of the BBSIZE bits of
program       memory    space.   Accessing    any          Configuration word (Register 5-7), see Table 5-1 for
unimplemented memory will return all ‘0’s (a NOP           boot block sizes. The WRTB Configuration bit is used
instruction).                                              to write-protect the Boot Block.
These devices contain the following:
                                                           4.2.3      STORAGE AREA FLASH
• PIC18(L)F45/46K42: 32 Kbytes of Flash memory,
  up to 16,384 single-word instructions                    Storage Area Flash (SAF) is the area in program
• PIC18(L)F26/46/56K42: 64 Kbytes of Flash                 memory that can be used as data storage. SAF is
  memory, up to 32,768 single-word instructions            enabled by the SAFEN bit of the Configuration word in
• PIC18(L)F27/47/57K42: 128 Kbytes of Flash                Register 5-7. If enabled, the code placed in this area
  memory, up to 65,536 single-word instructions            cannot be executed by the CPU. The SAF block is
The Reset vector for the device is at address 000000h.     placed at the end of memory and spans 128 Words.
PIC18(L)F26/27/45/46/47/55/56/57K42              devices   The WRTSAF Configuration bit is used to write-protect
feature a vectored interrupt controller with a dedicated   the Storage Area Flash.
interrupt vector table in the program memory, see
Section 9.0 “Interrupt Controller”.                          Note:    If write-protected locations are written to,
                                                                      memory is not changed and the WRERR
  Note:     For memory information on this family of                  bit defined in Register 13-1 is set.
            devices, see Table 4-1 and Table 4-3.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 33
                         PIC18(L)F26/27/45/46/47/55/56/57K42
TABLE 4-1:         PROGRAM AND DATA EEPROM MEMORY MAP


                             PIC18(L)F45/46K42                 PIC18(L)F26/46/56K42               PIC18(L)F27/47/57K42
                                    PC[21:0]                           PC[21:0]                             PC[21:0]


               Note 1          Stack (31 levels)                   Stack (31 levels)                   Stack (31 levels)          Note 1


             00 0000h             Reset Vector                       Reset Vector                        Reset Vector             00 0000h
                   •••                 •••                                •••                                 •••                 •••
             00 0008h       Interrupt Vector High(2)           Interrupt Vector High(2)            Interrupt Vector High(2)       00 0008h
                   •••                 •••                                •••                                 •••                 •••
             00 0018h       Interrupt Vector Low(2)             Interrupt Vector Low(2)              Interrupt Vector Low(2)      00 0018h
             00 001Ah                                                                                                             00 001Ah
                          Program Flash Memory (16
                    •                                                                                                             •
                                   KW)(3)
             00 7FFFh                                        Program Flash Memory (32                                             00 7FFFh
             00 8000h                                                 KW)(3)                                                      00 8000h
                                                                                                Program Flash Memory (64
                    •                                                                                    KW)(3)                   •
             00 FFFFh                                                                                                             00 FFFFh
             01 0000h             Reserved(4)                                                                                     01 0000h
             01 FFFFh                                                Reserved(4)                                                  01 FFFFh
             02 0000h                                                                                                             02 0000h
             1F FFFFh                                                                                     Reserved(4)             1F FFFFh
              20 0000                                                                                                             20 0000h
                  •••                                           User IDs (8 Words)(5)                                             •••
             20 000Fh                                                                                                             20 000Fh
             20 0010h                                                                                                             20 0010h
                  •••                                                  Reserved                                                   •••
             2F FFFFh                                                                                                             2F FFFFh
             30 0000h                                                                                                             30 0000h
                  •••                                     Configuration Words (5 Words)(5)                                        •••
             30 0009h                                                                                                             30 0009h
             30 000Ah                                                                                                             30 000Ah
                  •••                                                  Reserved                                                   •••
             30 FFFFh                                                                                                             30 FFFFh
             31 0000h                                                                                                             31 0000h
                  •••     Data EEPROM (256 Bytes)                                                                                 •••
             31 00FFh                                                                                                             31 00FFh
                                                                                Data EEPROM (1024Bytes)
             31 0100h                                                                                                             31 0100h
                  •••                                                                                                             •••
             31 03FFh                                                                                                             31 03FFh
                                   Reserved
              31 0400h                                                                                                            31 0400h
                   •••                                                                    Reserved                                •••
             3E FFFFh                                                                                                             3E FFFFh
             3F 0000h                                                                                                             3F 0000h
                  •••                                       Device Information Area(5),(7)                                        •••
             3F 003Fh                                                                                                             3F 003Fh
              3F0040h                                                                                                             3F0040h
                  •••                                                  Reserved                                                   •••
             3F FEFFh                                                                                                             3F FEFFh
             3F FF00h                                                                                                             3F FF00h
                  •••                            Device Configuration Information (5 Words)(5),(6),(7)                            •••
             3F FF09h                                                                                                             3F FF09h
             3F FF0Ah                                                                                                             3F FF0Ah
                  •••                                                  Reserved                                                   •••
             3F FFFBh                                                                                                             3F FFFBh
             3F FFFCh                                                                                                             3F FFFCh
                  •••                                       Revision ID (1 Word)(5),(6),(7)                                       •••
             3F FFFDh                                                                                                             3F FFFDh
             3F FFFEh                                                                                                             3F FFFEh
                  •••                                        Device ID (1 Word)(5),(6),(7)                                        •••
             3F FFFFh                                                                                                             3F FFFFh

            Note   1:    The stack is a separate SRAM panel, apart from all user memory panels.
                   2:    00 0008h location is used as the reset default for the IVTBASE register, the vector table can be relocated in the
                         memory by programming the IVTBASE register.
                   3:    Storage area Flash is implemented as the last 128 Words of user Flash.
                   4:    The addresses do not roll over. The region is read as ‘0’.
                   5:    Not code-protected.
                   6:    Hard-coded in silicon.
                   7:    This region cannot be written by the user and it’s not affected by a Bulk Erase.


 2017-2021 Microchip Technology Inc.                                                                                            DS40001919G-page 34
                      PIC18(L)F26/27/45/46/47/55/56/57K42

TABLE 4-2:        PROGRAM FLASH MEMORY PARTITION
                                                                          Partition(3)
    Region                  Address             BBEN = 1         BBEN = 1         BBEN = 0       BBEN = 0
                                                SAFEN = 1        SAFEN = 0        SAFEN = 1      SAFEN = 0
                 00 0000h
                 • • •                                                              BOOT           BOOT
                 Last Boot Block Memory                                             BLOCK          BLOCK
                 Address
                                                               APPLICATION
                 Last Boot Block Memory                          BLOCK
                 Address(1) + 1
   Program                                                                                      APPLICATION
                 • • •                        APPLICATION
    Flash                                                                                         BLOCK
                 Last Program Memory            BLOCK
   Memory
                 Address(2) - 100h                                               APPLICATION
                 Last Program Memory                                               BLOCK
                 Address(2) - FEh(4)                             STORAGE                          STORAGE
                 • • •                                             AREA                             AREA
                 Last Program Memory                              FLASH                            FLASH
                 Address(2)
Note 1:   Last Boot Block Memory Address is based on BBSIZE[2:0], see Table 5-1.
     2:   For Last Program Memory Address, see Table 4-1.
     3:   Refer to Register 5-7: Configuration Word 4L for BBEN and SAFEN definitions.
     4:   Storage area Flash is implemented as the last 128 Words of User Flash.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 35
                       PIC18(L)F26/27/45/46/47/55/56/57K42
4.2.4       PROGRAM COUNTER                                   4.2.5       RETURN ADDRESS STACK
The Program Counter (PC) specifies the address of the         The return address stack allows any combination of up
instruction to fetch for execution. The PC is 21-bit wide     to 31 program calls and interrupts to occur. The PC is
and is contained in three separate 8-bit registers. The       pushed onto the stack when a CALL or RCALL
low byte, known as the PCL register, is both readable         instruction is executed or an interrupt is acknowledged.
and writable. The high byte, or PCH register, contains        The PC value is pulled off the stack on a RETURN,
the PC[15:8] bits; it is not directly readable or writable.   RETLW or a RETFIE instruction. PCLATU and PCLATH
Updates to the PCH register are performed through the         are not affected by any of the RETURN or CALL
PCLATH register. The upper byte is called PCU. This           instructions.
register contains the PC[20:16] bits; it is also not          The stack operates as a 31-word by 21-bit RAM and a
directly readable or writable. Updates to the PCU             5-bit Stack Pointer. The stack space is not part of either
register are performed through the PCLATU register.           program or data space. The Stack Pointer is readable
The contents of PCLATH and PCLATU are transferred             and writable and the address on the top of the stack is
to the program counter by any operation that writes           readable and writable through the Top-of-Stack (TOS)
PCL. Similarly, the upper two bytes of the program            Special File Registers. Data can also be pushed to, or
counter are transferred to PCLATH and PCLATU by               popped from the stack, using these registers.
any operation that reads PCL. This is useful for              A CALL, CALLW or RCALL instruction causes a push
computed offsets to the PC (see Section                       onto the stack; the Stack Pointer is first incremented
4.3.2.1 “Computed GOTO”).                                     and the location pointed to by the Stack Pointer is
The PC addresses bytes in the program memory. To              written with the contents of the PC (already pointing to
prevent the PC from becoming misaligned with word             the instruction following the CALL). A RETURN type
instructions, the Least Significant bit of PCL is fixed to    instruction causes a pop from the stack; the contents of
a value of ‘0’. The PC increments by two to address           the location pointed to by the STKPTR are transferred
sequential instructions in the program memory.                to the PC and then the Stack Pointer is decremented.
The CALL, RCALL, GOTO and program branch                      The Stack Pointer is initialized to ‘00000’ after all
instructions write to the program counter directly. For       Resets. There is no RAM associated with the location
these instructions, the contents of PCLATH and                corresponding to a Stack Pointer value of ‘00000’; this
PCLATU are not transferred to the program counter.            is only a Reset value. Status bits in the PCON0 register
                                                              indicate if the stack has overflowed or underflowed.

                                                              4.2.5.1       Top-of-Stack Access
                                                              Only the top of the return address stack (TOS) is readable
                                                              and writable. A set of three registers, TOSU:TOSH:TOSL,
                                                              holds the contents of the stack location pointed to by the
                                                              STKPTR register (Figure 4-1). This allows users to
                                                              implement a software stack, if necessary. After a CALL,
                                                              RCALL or interrupt, the software can read the pushed
                                                              value by reading the TOSU:TOSH:TOSL registers. These
                                                              values can be placed on a user-defined software stack. At
                                                              return time, the software can return these values to
                                                              TOSU:TOSH:TOSL and do a return.
                                                              The user must disable the Global Interrupt Enable (GIE)
                                                              bits while accessing the stack to prevent inadvertent
                                                              stack corruption.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 36
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 4-1:             RETURN ADDRESS STACK AND ASSOCIATED REGISTERS
                                                      Return Address Stack [20:0]

                                                                           11111
                                                                           11110
                    Top-of-Stack Registers                                 11101             Stack Pointer

              TOSU           TOSH           TOSL                                             STKPTR[4:0]
               00h            1Ah            34h                                               00010
                                                                           00011
                                               Top-of-Stack   001A34h      00010
                                                              000D58h      00001
                                                                           00000


4.2.5.2       Return Stack Pointer (STKPTR)                      If STVREN is set (default) and the stack has been
                                                                 popped enough times to unload the stack, the next pop
The STKPTR register (Register 4-4) contains the Stack
                                                                 will return a value of zero to the PC, it will set the
Pointer value. The STKOVF (Stack Overflow) Status bit
                                                                 STKUNF bit and a Reset will be generated. This
and the STKUNF (Stack Underflow) Status bit can be
                                                                 condition can be generated by the RETURN, RETLW and
accessed using the PCON0 register. The value of the
                                                                 RETFIE instructions.
Stack Pointer can be 0 through 31. On Reset, the Stack
Pointer value will be zero. The user may read and write          When STVREN = 0, STKUNF will be set but no Reset
the Stack Pointer value. This feature can be used by a           will occur.
Real-Time Operating System (RTOS) for stack mainte-
nance. After the PC is pushed onto the stack 32 times
(without popping any values off the stack), the                    Note:     Returning a value of zero to the PC on an
STKOVF bit is set. The STKOVF bit is cleared by soft-                        underflow has the effect of vectoring the
ware or by a POR. The action that takes place when the                       program to the Reset vector, where the
stack becomes full depends on the state of the                               stack conditions can be verified and
STVREN (Stack Overflow Reset Enable) Configuration                           appropriate actions can be taken. This is
bit. (Refer to Section 5.1 “Configuration Words” for                         not the same as a Reset, as the contents
a description of the device Configuration bits.)                             of the SFRs are not affected.

If STVREN is set (default), a Reset will be generated            4.2.5.3       PUSH and POP Instructions
and a Stack Overflow will be indicated by the STKOVF
bit when the 32nd push is initiated. This includes CALL          Since the Top-of-Stack is readable and writable, the
and CALLW instructions, as well as stacking the return           ability to push values onto the stack and pull values off
address during an interrupt response. The STKOVF bit             the stack without disturbing normal program execution
will remain set and the Stack Pointer will be set to zero.       is a desirable feature. The PIC18 instruction set
                                                                 includes two instructions, PUSH and POP, that permit
If STVREN is cleared, the STKOVF bit will be set on the          the TOS to be manipulated under software control.
32nd push and the Stack Pointer will remain at 31 but            TOSU, TOSH and TOSL can be modified to place data
no Reset will occur. Any additional pushes will                  or a return address on the stack.
overwrite the 31st push but the STKPTR will remain at
31.                                                              The PUSH instruction places the current PC value onto
                                                                 the stack. This increments the Stack Pointer and loads
Setting STKOVF = 1 in software will change the bit, but          the current PC value onto the stack.
will not generate a Reset.
                                                                 The POP instruction discards the current TOS by
The STKUNF bit is set when a stack pop returns a                 decrementing the Stack Pointer. The previous value
value of zero. The STKUNF bit is cleared by software             pushed onto the stack then becomes the TOS value.
or by POR. The action that takes place when the stack
becomes full depends on the state of the STVREN
(Stack Overflow Reset Enable) Configuration bit.
(Refer to Section 5.1 “Configuration Words” for a
description of the device Configuration bits).


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 37
                      PIC18(L)F26/27/45/46/47/55/56/57K42
4.3         Register Definitions: Stack Pointer
REGISTER 4-1:          TOSU: TOP OF STACK UPPER BYTE
        U-0          U-0             U-0           R/W-0            R/W-0            R/W-0      R/W-0          R/W-0
        —             —                 —                                      TOS[20:16]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit               W = Writable bit               U = Unimplemented              C = Clearable only bit
-n = Value at POR               ‘1’ = Bit is set              ‘0’ = Bit is cleared           x = Bit is unknown


bit 7-5          Unimplemented: Read as ‘0’
bit 4-0          TOS[20:16]: Top of Stack Location bits


REGISTER 4-2:          TOSH: TOP OF STACK HIGH BYTE
      R/W-0         R/W-0           R/W-0          R/W-0         R/W-0               R/W-0      R/W-0          R/W-0
                                                        TOS[15:8]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit               W = Writable bit               U = Unimplemented              C = Clearable only bit
-n = Value at POR               ‘1’ = Bit is set              ‘0’ = Bit is cleared           x = Bit is unknown


bit 7-0          TOS[15:8]: Top of Stack Location bits


REGISTER 4-3:          TOSL: TOP OF STACK LOW BYTE
      R/W-0         R/W-0           R/W-0          R/W-0         R/W-0               R/W-0      R/W-0          R/W-0
                                                         TOS[7:0]
bit 7                                                                                                                 bit 0


Legend:
R = Readable bit               W = Writable bit               U = Unimplemented              C = Clearable only bit
-n = Value at POR               ‘1’ = Bit is set              ‘0’ = Bit is cleared           x = Bit is unknown


bit 7-0          TOS[7:0]: Top of Stack Location bits


 2017-2021 Microchip Technology Inc.                                                               DS40001919G-page 38
                          PIC18(L)F26/27/45/46/47/55/56/57K42

REGISTER 4-4:              STKPTR: STACK POINTER REGISTER
        U-0              U-0           U-0           R/W-0         R/W-0               R/W-0      R/W-0          R/W-0
         —                —             —                                       STKPTR[4:0]
bit 7                                                                                                                   bit 0


Legend:
R = Readable bit                  W = Writable bit              U = Unimplemented              C = Clearable only bit
-n = Value at POR                 ‘1’ = Bit is set              ‘0’ = Bit is cleared           x = Bit is unknown


bit 7-5              Unimplemented: Read as ‘0’
bit 4-0              STKPTR[4:0]: Stack Pointer Location bits

4.3.1             FAST REGISTER STACK
There are three levels of fast stack registers available -
one for CALL type instructions and two for interrupts. A
fast register stack is provided for the STATUS, WREG
and BSR registers, to provide a “fast return” option for
interrupts. It is loaded with the current value of the cor-
responding register when the processor vectors for an
interrupt. All interrupt sources will push values into the
stack registers. The values in the registers are then
loaded back into their associated registers if the
RETFIE, FAST instruction is used to return from the
interrupt. Refer to Section 4.5.6 “Call Shadow Regis-
ter” for interrupt call shadow registers.
Example 4-1 shows a source code example that uses
the fast register stack during a subroutine call and
return.

EXAMPLE 4-1:               FAST REGISTER STACK
                           CODE EXAMPLE
CALL SUB1, FAST            ;STATUS, WREG, BSR
                           ;SAVED IN FAST REGISTER
                           ;STACK
              
              

SUB1        
            
        RETURN, FAST       ;RESTORE VALUES SAVED
                           ;IN FAST REGISTER STACK


 2017-2021 Microchip Technology Inc.                                                                 DS40001919G-page 39
                        PIC18(L)F26/27/45/46/47/55/56/57K42
4.3.2       LOOK-UP TABLES IN PROGRAM
            MEMORY
There may be programming situations that require the
creation of data structures, or look-up tables, in
program memory. For PIC18 devices, look-up tables
can be implemented in two ways:
• Computed GOTO
• Table Reads

4.3.2.1       Computed GOTO
A computed GOTO is accomplished by adding an offset
to the program counter. An example is shown in
Example 4-2.
A look-up table can be formed with an ADDWF PCL
instruction and a group of RETLW nn instructions. The
W register is loaded with an offset into the table before
executing a call to that table. The first instruction of the
called routine is the ADDWF PCL instruction. The next
instruction executed will be one of the RETLW nn
instructions that returns the value ‘nn’ to the calling
function.
The offset value (in WREG) specifies the number of
bytes that the program counter may advance and may
be multiples of two (LSb = 0).
In this method, only one data byte may be stored in
each instruction location and room on the return
address stack is required.

EXAMPLE 4-2:            COMPUTED GOTO USING
                        AN OFFSET VALUE
           MOVF      OFFSET, W
           CALL      TABLE
 ORG       nn00h
 TABLE     ADDWF     PCL
           RETLW     nnh
           RETLW     nnh
           RETLW     nnh
           .
           .
           .


4.3.2.2       Table Reads and Table Writes
A better method of storing data in program memory
allows two bytes of data to be stored in each instruction
location.
Look-up table data may be stored two bytes per
program word by using table reads and writes. The
Table Pointer (TBLPTR) register specifies the byte
address and the Table Latch (TABLAT) register
contains the data that is read from or written to program
memory.
Table read and table write operations are discussed
further in Section 13.1.1 “Table Reads and Table
Writes”.


 2017-2021 Microchip Technology Inc.                          DS40001919G-page 40
                      PIC18(L)F26/27/45/46/47/55/56/57K42
4.4        PIC18 Instruction Cycle                              A fetch cycle begins with the Program Counter (PC)
                                                                incrementing followed by the execution cycle.
4.4.1        INSTRUCTION FLOW/PIPELINING                        In the execution cycle, the fetched instruction is latched
An “Instruction Cycle” consists of four cycles of the           into the Instruction Register (IR). This instruction is
oscillator clock. The instruction fetch and execute are         then decoded and executed during the next few
pipelined in such a manner that a fetch takes one               oscillator clock cycles. Data memory is read (operand
instruction cycle, while the decode and execute take            read) and written (destination write) during the
another instruction cycle. However, due to the                  execution cycle as well.
pipelining, each instruction effectively executes in one
cycle. If an instruction causes the program counter to
change (e.g., GOTO), then two cycles are required to
complete the instruction (Example 4-3).

EXAMPLE 4-3:           INSTRUCTION PIPELINE FLOW

                                 TCY0          TCY1          TCY2         TCY3           TCY4             TCY5
 1. MOVLW 55h                   Fetch 1     Execute 1
 2. MOVWF PORTB                              Fetch 2       Execute 2
 3. BRA     SUB_1                                           Fetch 3    Execute 3
 4. BSF      PORTA, BIT3 (Forced NOP)                                   Fetch 4      Flush (NOP)
 5. Instruction @ address SUB_1                                                     Fetch SUB_1 Execute SUB_1


   Note:     There are some instructions that take multiple cycles to execute. Refer to Section 41.0 “Instruction Set
             Summary” for details.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 41
                       PIC18(L)F26/27/45/46/47/55/56/57K42
4.4.2       INSTRUCTIONS IN PROGRAM                              4.4.3       MULTI-WORD INSTRUCTIONS
            MEMORY                                               The standard PIC18 instruction set has four two-word
The program memory is addressed in bytes.                        instructions: CALL, MOVFF, GOTO and LFSR and two
Instructions are stored as either two bytes or four bytes        three-word instructions: MOVFFL and MOVSFL. In all
in program memory. The Least Significant Byte of an              cases, the second and the third word of the instruction
instruction word is always stored in a program memory            always has ‘1111’ as its four Most Significant bits; the
location with an even address (LSb = 0). To maintain             other 12 bits are literal data, usually a data memory
alignment with instruction boundaries, the PC                    address.
increments in steps of two and the LSb will always read          The use of ‘1111’ in the four MSbs of an instruction
‘0’ (see Section 4.2.4 “Program Counter”).                       specifies a special form of NOP. If the instruction is
Figure 4-2 shows an example of how instruction words             executed in proper sequence – immediately after the
are stored in the program memory.                                first word – the data in the second word is accessed
                                                                 and used by the instruction sequence. If the first word
The CALL and GOTO instructions have the absolute
                                                                 is skipped for some reason and the second or third
program memory address embedded into the
                                                                 word is executed by itself, a NOP is executed instead.
instruction. Since instructions are always stored on word
                                                                 This is necessary for cases when the multi-word
boundaries, the data contained in the instruction is a
                                                                 instruction is preceded by a conditional instruction that
word address. The word address is written to PC[20:1],
                                                                 changes the PC. Example 4-4 shows how this works.
which accesses the desired byte address in program
memory. Instruction #2 in Figure 4-2 shows how the
instruction GOTO 0006h is encoded in the program
memory. Program branch instructions, which encode a
relative address offset, operate in the same manner. The
offset value stored in a branch instruction represents the
number of single-word instructions that the PC will be
offset by. Section 41.0 “Instruction Set Summary”
provides further details of the instruction set.

FIGURE 4-2:             INSTRUCTIONS IN PROGRAM MEMORY
                                                                                      Word Address
                                                             LSB = 1      LSB = 0          
                                 Program Memory                                        000000h
                                 Byte Locations                                      000002h
                                                                                       000004h
                                                                                       000006h
                Instruction 1:   MOVLW       055h             0Fh           55h        000008h
                Instruction 2:   GOTO        0006h            EFh           03h        00000Ah
                                                              F0h           00h        00000Ch
                Instruction 3:   MOVFF       123h, 456h       C1h           23h        00000Eh
                                                              F4h           56h        000010h
                Instruction 4:    MOVFFL     123h, 456h       00h           60h        000012h
                                                              F4h           8Ch        000014h
                                                              F4h           56h        000016h
                                                                                       000018h
                                                                                       00001Ah


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 42
                      PIC18(L)F26/27/45/46/47/55/56/57K42
EXAMPLE 4-4:           TWO-WORD INSTRUCTIONS
 CASE 1:
 Object Code                    Source Code
 0110 0110 0000 0000            TSTFSZ     REG1       ; is RAM location 0?
 1100 0001 0010 0011            MOVFF      REG1, REG2 ; Yes, skip this word
 1111 0100 0101 0110                                  ; Execute this word as a NOP
 0010 0100 0000 0000            ADDWF      REG3       ; continue code
 CASE 2:
 Object Code                    Source Code
 0110 0110 0000 0000            TSTFSZ     REG1       ; is RAM location 0?
 1100 0001 0010 0011            MOVFF      REG1, REG2 ; No, execute this word
 1111 0100 0101 0110                                  ; 2nd word of instruction
 0010 0100 0000 0000            ADDWF      REG3       ; continue code

EXAMPLE 4-5:           THREE-WORD INSTRUCTIONS
 CASE 1:
 Object Code                    Source Code
 0110 0110 0000 0000            TSTFSZ     REG1       ; is RAM location 0?
 0000 0000 0110 0000            MOVFFL     REG1, REG2 ; Yes, skip this word
 1111 0100 1000 1100                                  ; Execute this word as a NOP
 1111 0100 0101 0110                                  ; Execute this word as a NOP
 0010 0100 0000 0000            ADDWF      REG3       ; continue code
 CASE 2:
 Object Code                    Source Code
 0110 0110 0000 0000            TSTFSZ     REG1       ; is RAM location 0?
 0000 0000 0110 0000            MOVFFL     REG1, REG2 ; No, execute this word
 1111 0100 1000 1100                                  ; 2nd word of instruction
 1111 0100 0101 0110                                  ; 3rd word of instruction
 0010 0100 0000 0000            ADDWF      REG3       ; continue code


 2017-2021 Microchip Technology Inc.                                             DS40001919G-page 43
                      PIC18(L)F26/27/45/46/47/55/56/57K42
4.5      Data Memory Organization                         4.5.1       BANK SELECT REGISTER (BSR)
Data memory in PIC18F26/27/45/46/47/55/56/57K42           Large areas of data memory require an efficient
devices is implemented as static RAM. Each register in    addressing scheme to make rapid access to any
the data memory has a 14-bit address, allowing up to      address possible. Ideally, this means that an entire
16384 bytes of data memory. The memory space is           address does not need to be provided for each read or
divided into 64 banks that contain 256 bytes each.        write operation. For PIC18 devices, this is accom-
Figure 4-3 shows the data memory organization for the     plished with a RAM banking scheme. This divides the
PIC18F26/27/45/46/47/55/56/57K42 devices in this          memory space into 64 contiguous banks of 256 bytes.
data sheet.                                               Depending on the instruction, each location can be
                                                          addressed directly by its full 14-bit address, or an 8-bit
The data memory contains Special Function Registers       low-order address and a 6-bit Bank Select Register.
(SFRs) and General Purpose Registers (GPRs). The
SFRs are used for control and status of the controller    This SFR holds the six Most Significant bits of a
and peripheral functions, while GPRs are used for data    location address; the instruction itself includes the
storage and scratchpad operations in the user’s           eight Least Significant bits. Only the six lower bits of the
application. Any read of an unimplemented location will   BSR are implemented (BSR[5:0]). The upper two bits
read as ‘0’s.                                             are unused; they will always read ‘0’ and cannot be
                                                          written to. The BSR can be loaded directly by using the
The instruction set and architecture allow operations     MOVLB instruction.
across all banks. The entire data memory may be
accessed by Direct, Indirect or Indexed Addressing        The value of the BSR indicates the bank in data
modes. Addressing modes are discussed later in this       memory; the eight bits in the instruction show the
subsection.                                               location in the bank and can be thought of as an offset
                                                          from the bank’s lower boundary. The relationship
To ensure that commonly used registers (select SFRs       between the BSR’s value and the bank division in data
and GPRs) can be accessed in a single cycle, PIC18        memory is shown in Figure 4-3.
devices implement an Access Bank. This is a 256-byte
memory space that provides fast access to some SFRs       Since up to 64 registers may share the same low-order
and the lower portion of GPR Bank 0 without using the     address, the user must always be careful to ensure that
Bank Select Register (BSR). Section 4.5.4 “Access         the proper bank is selected before performing a data
Bank” provides a detailed description of the Access       read or write. For example, writing what may be
RAM.                                                      program data to an 8-bit address of F9h while the BSR
                                                          is 3Fh will end up corrupting the program counter.
                                                          While any bank can be selected, only those banks that
                                                          are actually implemented can be read or written to.
                                                          Writes to unimplemented banks are ignored, while
                                                          reads from unimplemented banks will return ‘0’s. Even
                                                          so, the STATUS register will still be affected as if the
                                                          operation was successful. The data memory maps in
                                                          Figure 4-3 indicate which banks are implemented.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 44
                                        FIGURE 4-4:        DATA MEMORY MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES
 2017-2021 Microchip Technology Inc.


                                               Bank      BSR[5:0]   Address                        PIC18(L)F26K42   PIC18(L)F27K42       Address
                                                                                  PIC18(L)F45K42
                                                                    addr[7:0]                      PIC18(L)F46K42   PIC18(L)F47K42      addr[13:0]
                                                                                  PIC18(L)F55K42
                                                                                                   PIC18(L)F56K42   PIC18(L)F57K42
                                                                            00h    Access RAM        Access RAM       Access RAM     0000h
                                                                                                                                     005Fh
                                              Bank 0     00 0000
                                                                                       GPR              GPR             GPR          0060h
                                                                           FFh                                                       00FFh


                                                                                                                                                                          PIC18(L)F26/27/45/46/47/55/56/57K42
                                              Bank 1     00 0001            00h                                                      0100h
                                                                           FFh                                                       ·
                                              Bank 2     00 0010            00h                                                      ·
                                                                           FFh                                                       ·
                                                                                       GPR              GPR             GPR          ·
                                                                            00h                                                      ·
                                                                              ·                                                      ·
                                              Bank 3                          ·                                                      ·
                                                         00 0011              ·                                                                      Virtual Bank
                                                                                                                                     03FFh
                                                                           FFh
                                                                           00h                                                       0400h
                                                         00 0100              ·                                                      ·               Access RAM     00h
                                               Banks        -                 ·        GPR              GPR             GPR          ·
                                               4 to 7                                                                                                               5Fh
                                                         00 0111              ·                                                      ·
                                                                           FFh                                                       07FFh              SFR         60h
                                                                           00h                                                       0800h                          FFh
                                                         00 1000              ·                                                      ·
                                              Banks                           ·                         GPR                          ·
                                              8 to 15       -
                                                         00 1111              ·                                                      ·
                                                                           FFh                                                       0FFFh
                                                                           00h                                          GPR          1000h
                                               Banks     01 0000              ·                                                      ·
                                                                              ·   Unimplemented                                      ·
                                              16 to 31      -
                                                         01 1111              ·                                                      ·
                                                                           FFh                     Unimplemented                     1FFFh
                                                                            00h                                                      2000h
                                               Banks     10 0000              ·                                                      ·
                                                                              ·                                     Unimplemented    ·
                                              32 to 55      -                 ·                                                      ·
                                                         11 0111           FFh                                                       37FFh
                                                                           00h                                                       3800h
                                                         11 1000              ·                                                      ·
                                               Banks                          ·        SFR              SFR              SFR         ·
                                              56 to 62      -
                                                         11 1110              ·                                                      ·
                                                                           FFh                                                       3EFFh
                                                                           00h                                                       3800h
                                                         11 1111              ·        SFR              SFR              SFR         3EFFh
                                              Bank 63                         ·                                                      3F60h
                                                                              ·                                                      3FFFh
                                                                           FFh
DS40001919G-page 45
                                        FIGURE 4-5:            USE OF THE BANK SELECT REGISTER (DIRECT ADDRESSING)
 2017-2021 Microchip Technology Inc.


                                                           BSR(1)
                                                                                           Data Memory                               From Opcode
                                               7                             0   0000h                         00h          7                               0
                                               0   0   0   0    0   0   1   0                   Bank 0                       1   1    1   1   1    1   1   1
                                                                                                               FFh
                                                                                 0100h                         00h
                                                                                                Bank 1
                                              Bank Select(2)                     0200h                         FFh
                                                                                                               00h
                                                                                                Bank 2


                                                                                                                                                                                                     PIC18(L)F26/27/45/46/47/55/56/57K42
                                                                                 0300h                         FFh
                                                                                                               00h

                                                                                               Bank 3
                                                                                               through
                                                                                               Bank 61


                                                                                                               FFh
                                                                                 3E00h
                                                                                                               00h
                                                                                               Bank 62
                                                                                 3F00h                         FFh
                                                                                                               00h
                                                                                               Bank 63
                                                                                 3FFFh                         FFh

                                             Note 1:   The Access RAM bit of the instruction can be used to force an override of the selected bank (BSR[5:0]) to the registers of the Access Bank.
DS40001919G-page 46
                      PIC18(L)F26/27/45/46/47/55/56/57K42
4.5.2       GENERAL PURPOSE REGISTER                       4.5.4        ACCESS BANK
            FILE                                           To streamline access for the most commonly used data
General Purpose RAM is available starting Bank 0 of        memory locations, the data memory is configured with
data memory. GPRs are not initialized by a Power-on        an Access Bank, which allows users to access a
Reset and are unchanged on all other Resets.               mapped block of memory without specifying a BSR.
                                                           The Access Bank consists of the first 96 bytes of
4.5.3       SPECIAL FUNCTION REGISTERS                     memory (00h-5Fh) in Bank 0 and the last 160 bytes of
The Special Function Registers (SFRs) are registers        memory (60h-FFh) in Bank 63. The lower half is known
used by the CPU and peripheral modules for controlling     as the “Access RAM” and is composed of GPRs. This
the desired operation of the device. These registers are   upper half is also where some of the SFRs of the device
implemented as static RAM. SFRs start at the top of        are mapped. These two areas are mapped
data memory (3FFFh) and extend downward to occupy          contiguously in the Access Bank and can be addressed
Bank 56 through 63 (3800h to 3FFFh). A list of these       linearly by an 8-bit address (Figure 4-4).
registers is given in Table 4-3 to Table 4-11. A bitwise   The Access Bank is used by core PIC18 instructions
summary of these registers can be found in                 that include the Access RAM bit (the ‘a’ parameter in
Section 42.0 “Register Summary”.                           the instruction). When ‘a’ is equal to ‘1’, the instruction
                                                           uses the BSR and the 8-bit address included in the
                                                           opcode for the data memory address. When ‘a’ is ‘0’,
                                                           however, the instruction uses the Access Bank address
                                                           map; the current value of the BSR is ignored.
                                                           Using this “forced” addressing allows the instruction to
                                                           operate on a data address in a single cycle, without
                                                           updating the BSR first. For 8-bit addresses of 60h and
                                                           above, this means that users can evaluate and operate
                                                           on SFRs more efficiently. The Access RAM below 60h
                                                           is a good place for data values that the user might need
                                                           to access rapidly, such as immediate computational
                                                           results or common program variables. Access RAM
                                                           also allows for faster and more code efficient and
                                                           switching of variables.
                                                           The mapping of the Access Bank is slightly different
                                                           when the extended instruction set is enabled (XINST
                                                           Configuration bit = 1). This is discussed in more detail
                                                           in Section 4.8.3 “Mapping the Access Bank in
                                                           Indexed Literal Offset Mode”.


 2017-2021 Microchip Technology Inc.                                                         DS40001919G-page 47
                                        TABLE 4-3:           SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES (DMA ACCESS ONLY)
 2017-2021 Microchip Technology Inc.


                                         40FFh     —           40DFh           —          40BFh        —         409Fh          —         407Fh         —          405Fh          —           403Fh   —   401Fh   —
                                         40FEh     —          40DEh            —          40BEh        —         409Eh          —         407Eh         —          405Eh          —           403Eh   —   401Eh   —
                                         40FDh     —          40DDh        T6PR_M2        40BDh ADRESH_M2        409Dh          —         407Dh         —          405Dh          —           403Dh   —   401Dh   —
                                         40FCh     —          40DCh PWM5DCH_M2 40BCh ADRESL_M2                   409Ch          —         407Ch         —          405Ch          —           403Ch   —   401Ch   —
                                         40FBh  TMR5H_M1      40DBh PWM5DCL_M2 40BBh ADPCH_M2                    409Bh          —         407Bh         —          405Bh          —           403Bh   —   401Bh   —
                                         40FAh  TMR5L_M1      40DAh        T6PR_M1        40BAh    ADCLK_M1      409Ah          —         407Ah         —          405Ah          —           403Ah   —   401Ah   —
                                         40F9h  TMR3H_M1       40D9h CCPR1H_M2            40B9h    ADACT_M1      4099h          —         4079h         —          4059h          —           4039h   —   4019h   —


                                                                                                                                                                                                                      PIC18(L)F26/27/45/46/47/55/56/57K42
                                         40F8h  TMR3L_M1       40D8h CCPR1L_M2            40B8h    ADREF_M1      4098h          —         4078h         —          4058h          —           4038h   —   4018h   —
                                         40F7h  TMR1H_M1       40D7h       T4PR_M4        40B7h ADCON3_M1        4097h          —         4077h         —          4057h          —           4037h   —   4017h   —
                                         40F6h  TMR1L_M1       40D6h PWM8DCH_M1 40B6h ADCON2_M1                  4096h ADRESH_M1          4076h         —          4056h          —           4036h   —   4016h   —
                                         40F5h     —           40D5h PWM8DCL_M1 40B5h ADCON1_M1                  4095h ADRESL_M1          4075h         —          4055h          —           4035h   —   4015h   —
                                         40F4h     —           40D4h       T4PR_M3        40B4h ADCON0_M1        4094h ADPCH_M1           4074h         —          4054h          —           4034h   —   4014h   —
                                         40F3h     —           40D3h PWM7DCH_M1 40B3h              ADCAP_M2      4093h     ADCAP_M1       4073h         —          4053h          —           4033h   —   4013h   —
                                         40F2h     —           40D2h PWM7DCL_M1 40B2h ADACQH_M2                  4092h ADACQH_M1          4072h         —          4052h          —           4032h   —   4012h   —
                                         40F1h     —           40D1h       T4PR_M2        40B1h ADACQL_M2        4091h ADACQL_M1          4071h         —          4051h          —           4031h   —   4011h   —
                                         40F0h     —           40D0h CCPR4H_M1            40B0h ADPREVH_M2 4090h ADPREVH_M1 4070h                       —          4050h          —           4030h   —   4010h   —
                                         40EFh PWM8DCH_M2 40CFh CCPR4L_M1                 40AFh ADPREVL_M2 408Fh ADPREVL_M1 406Fh                       —          404Fh          —           402Fh   —   400Fh   —
                                         40EEh PWM8DCL_M2 40CEh            T4PR_M1        40AEh    ADRPT_M2      408Eh     ADRPT_M1       406Eh         —          404Eh          —           402Eh   —   400Eh   —
                                        40EDh PWM7DCH_M2 40CDh CCPR3H_M1 40ADh                     ADCNT_M2      408Dh     ADCNT_M1       406Dh         —          404Dh          —           402Dh   —   400Dh   —
                                        40ECh PWM7DCL_M2 40CCh CCPR3L_M1                  40ACh ADACCU_M2        408Ch ADACCU_M1          406Ch         —          404Ch          —           402Ch   —   400Ch   —
                                         40EBh PWM6DCH_M2 40CBh            T2PR_M3        40ABh ADACCH_M2        408Bh ADACCH_M1          406Bh         —          404Bh          —           402Bh   —   400Bh   —
                                         40EAh PWM6DCL_M2 40CAh PWM6DCH_M1 40AAh ADACCL_M2                       408Ah ADACCL_M1          406Ah         —          404Ah          —           402Ah   —   400Ah   —
                                         40E9h PWM5DCH_M3 40C9h PWM6DCL_M1 40A9h ADFLTRH_M2                      4089h ADFLTRH_M1         4069h         —          4049h          —           4029h   —   4009h   —
                                         40E8h PWM5DCL_M3 40C8h            T2PR_M2        40A8h ADFLTRL_M2       4088h ADFLTRL_M1         4068h         —          4048h          —           4028h   —   4008h   —
                                         40E7h CCPR4H_M2       40C7h PWM5DCH_M1 40A7h ADSTPTH_M2 4087h ADSTPTH_M1 4067h                                 —          4047h          —           4027h   —   4007h   —
                                         40E6h CCPR4L_M2       40C6h PWM5DCL_M1 40A6h ADSTPTL_M2                 4086h ADSTPTL_M1         4066h         —          4046h          —           4026h   —   4006h   —
                                         40E5h CCPR3H_M2       40C5h       T2PR_M2        40A5h ADERRH_M2        4085h ADERRH_M1          4065h         —          4045h          —           4025h   —   4005h   —
                                         40E4h CCPR3L_M2       40C4h CCPR2H_M1            40A4h ADERRL_M2        4084h ADERRL_M1          4064h         —          4044h          —           4024h   —   4004h   —
                                         40E3h CCPR2H_M2       40C3h CCPR2L_M1            40A3h ADUTHH_M2        4083h ADUTHH_M1          4063h      IOCEF_M1      4043h          —           4023h   —   4003h   —
                                         40E2h CCPR2L_M2       40C2h       T2PR_M1        40A2h ADUTHL_M2        4082h ADUTHL_M1          4062h      IOCCF_M1      4042h          —           4022h   —   4002h   —
                                         40E1h CCPR1H_M3       40C1h CCPR1H_M1            40A1h ADLTHH_M2        4081h ADLTHH_M1          4061h      IOCBF_M1      4041h          —           4021h   —   4001h   —
                                         40E0h CCPR1L_M3       40C0h CCPR1L_M1            40A0h ADLTHL_M2        4080h ADLTHL_M1          4060h      IOCAF_M1      4040h          —           4020h   —   4000h   —
                                        Note 1:   Addresses in this table are accessible ONLY through DMA Source and Destination Address Registers. CPU does not have access to these registers.
DS40001919G-page 48
                                        TABLE 4-4:           SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 63
 2017-2021 Microchip Technology Inc.


                                         3FFFh       TOSU       3FDFh         INDF2      3FBFh        LATF(3)        3F9Fh     T4PR   3F7Fh   CCP1CAP   3F5Fh   CCPTMRS1   3F3Fh    NCO1CLK   3F1Fh   SMT1CON1
                                         3FFEh       TOSH       3FDEh      POSTINC2      3FBEh        LATE(2)        3F9Eh    T4TMR   3F7Eh   CCP1CON   3F5Eh   CCPTMRS0   3F3Eh   NCO1CON    3F1Eh   SMT1CON0
                                         3FFDh        TOSL      3FDDh     POSTDEC2       3FBDh        LATD(2)        3F9Dh    T5CLK   3F7Dh    CCPR1H   3F5Dh      —       3F3Dh   NCO1INCU   3F1Dh    SMT1PRU
                                         3FFCh     STKPTR       3FDCh       PRECIN2      3FBCh         LATC          3F9Ch   T5GATE   3F7Ch    CCPR1L   3F5Ch      —       3F3Ch   NCO1INCH   3F1Ch    SMT1PRH
                                         3FFBh      PCLATU      3FDBh        PLUSW2      3FBBh         LATB          3F9Bh   T5GCON   3F7Bh   CCP2CAP   3F5Bh      —       3F3Bh   NCO1INCL   3F1Bh    SMT1PRL
                                         3FFAh      PCLATH      3FDAh         FSR2H      3FBAh         LATA          3F9Ah    T5CON   3F7Ah   CCP2CON   3F5Ah    CWG1STR   3F3Ah   NCO1ACCU   3F1Ah   SMT1CPWU
                                         3FF9h         PCL      3FD9h         FSR2L      3FB9h       T0CON1          3F99h    TMR5H   3F79h    CCPR2H   3F59h    CWG1AS1   3F39h   NCO1ACCH   3F19h   SMT1CPWH


                                                                                                                                                                                                                 PIC18(L)F26/27/45/46/47/55/56/57K42
                                         3FF8h     TBLPRTU      3FD8h        STATUS      3FB8h       T0CON0          3F98h    TMR5L   3F78h    CCPR2L   3F58h    CWG1AS0   3F38h   NCO1ACCL   3F18h   SMT1CPWL
                                         3FF7h     TBLPTRH      3FD7h      IVTBASEU      3FB7h        TMR0H          3F97h    T6RST   3F77h   CCP3CAP   3F57h   CWG1CON1   3F37h       —      3F17h   SMT1CPRU
                                         3FF6h     TBLPTRL      3FD6h      IVTBASEH      3FB6h        TMR0L          3F96h    T6CLK   3F76h   CCP3CON   3F56h   CWG1CON0   3F36h       —      3F16h   SMT1CPRH
                                         3FF5h      TABLAT      3FD5h      IVTBASEL      3FB5h        T1CLK          3F95h    T6HLT   3F75h    CCPR3H   3F55h    CWG1DBF   3F35h       —      3F15h   SMT1CPRL
                                         3FF4h      PRODH       3FD4h       IVTLOCK      3FB4h       T1GATE          3F94h    T6CON   3F74h    CCPR3L   3F54h   CWG1DBR    3F34h       —      3F14h   SMT1TMRU
                                         3FF3h      PRODL       3FD3h       INTCON1      3FB3h       T1GCON          3F93h     T6PR   3F73h   CCP4CAP   3F53h    CWG1ISM   3F33h       —      3F13h   SMT1TMRH
                                         3FF2h          —       3FD2h       INTCON0      3FB2h        T1CON          3F92h    T6TMR   3F72h   CCP4CON   3F52h    CWG1CLK   3F32h       —      3F12h   SMT1TMRL
                                         3FF1h      PCON1       3FD1h           —        3FB1h        TMR1H          3F91h      —     3F71h    CCPR4H   3F51h    CWG2STR   3F31h       —      3F11h       —
                                         3FF0h      PCON0       3FD0h           —        3FB0h        TMR1L          3F90h      —     3F70h    CCPR4L   3F50h    CWG2AS1   3F30h       —      3F10h       —
                                                                                    (3)
                                         3FEFh       INDF0      3FCFh       PORTF        3FAFh        T2RST          3F8Fh      —     3F6Fh      —      3F4Fh    CWG2AS0   3F2Fh       —      3F0Fh       —
                                         3FEEh    POSTINC0      3FCEh         PORTE      3FAEh        T2CLK          3F8Eh      —     3F6Eh   PWM5CON   3F4Eh   CWG2CON1   3F2Eh       —      3F0Eh       —
                                        3FEDh     POSTDEC0      3FCDh       PORTD(2)     3FADh        T2HLT          3F8Dh      —     3F6Dh   PWM5DCH   3F4Dh   CWG2CON0   3F2Dh       —      3F0Dh       —
                                        3FECh      PRECIN0      3FCCh        PORTC       3FACh        T2CON          3F8Ch      —     3F6Ch   PWM5DCL   3F4Ch    CWG2DBF   3F2Ch       —      3F0Ch       —
                                         3FEBh     PLUSW0       3FCBh         PORTB      3FABh         T2PR          3F8Bh      —     3F6Bh      —      3F4Bh   CWG2DBR    3F2Bh       —      3F0Bh       —
                                         3FEAh      FSR0H       3FCAh         PORTA      3FAAh        T2TMR          3F8Ah      —     3F6Ah   PWM6CON   3F4Ah    CWG2ISM   3F2Ah       —      3F0Ah       —
                                         3FE9h       FSR0L      3FC9h           —        3FA9h        T3CLK          3F89h      —     3F69h   PWM6DCH   3F49h    CWG2CLK   3F29h       —      3F09h       —
                                         3FE8h       WREG       3FC8h           —        3FA8h       T3GATE          3F88h      —     3F68h   PWM6DCL   3F48h    CWG3STR   3F28h       —      3F08h       —
                                                                                   (3)
                                         3FE7h       INDF1      3FC7h        TRISF       3FA7h       T3GCON          3F87h      —     3F67h      —      3F47h    CWG3AS1   3F27h       —      3F07h       —
                                         3FE6h    POSTINC1      3FC6h        TRISE(2)    3FA6h        T3CON          3F86h      —     3F66h   PWM7CON   3F46h    CWG3AS0   3F26h       —      3F06h       —
                                         3FE5h    POSTDEC1      3FC5h        TRISD(2)    3FA5h        TMR3H          3F85h      —     3F65h   PWM7DCH   3F45h   CWG3CON1   3F25h       —      3F05h       —
                                         3FE4h     PRECIN1      3FC4h         TRISC      3FA4h        TMR3L          3F84h      —     3F64h   PWM7DCL   3F44h   CWG3CON0   3F24h       —      3F04h       —
                                         3FE3h     PLUSW1       3FC3h         TRISB      3FA3h        T4RST          3F83h      —     3F63h      —      3F43h    CWG3DBF   3F23h    SMT1WIN   3F03h       —
                                         3FE2h      FSR1H       3FC2h         TRISA      3FA2h        T4CLK          3F82h      —     3F62h   PWM8CON   3F42h   CWG3DBR    3F22h    SMT1SIG   3F02h       —
                                         3FE1h       FSR1L      3FC1h           —        3FA1h        T4HLT          3F81h      —     3F61h   PWM8DCH   3F41h    CWG3ISM   3F21h    SMT1CLK   3F01h       —
                                         3FE0h        BSR       3FC0h           —        3FA0h        T4CON          3F80h      —     3F60h   PWM8DCL   3F40h    CWG3CLK   3F20h   SMT1STAT   3F00h       —
                                        Legend:      Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:      Unimplemented in LF devices.
                                               2:    Unimplemented in PIC18(L)F26/27K42.
                                               3:    Unimplemented in PIC18(L)F26/27/45/46/47K42.
DS40001919G-page 49
                                        TABLE 4-5:           SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 62
 2017-2021 Microchip Technology Inc.


                                         3EFFh      ADCLK      3EDFh       ADLTHH       3EBFh       CM1PCH          3E9Fh      —       3E7Fh   —   3E5Fh   —   3E3Fh   —   3E1Fh   —
                                         3EFEh      ADACT      3EDEh       ADLTHL       3EBEh       CM1NCH          3E9Eh   DAC1CON0   3E7Eh   —   3E5Eh   —   3E3Eh   —   3E1Eh   —
                                        3EFDh       ADREF     3EDDh           —         3EBDh      CM1CON1          3E9Dh      —       3E7Dh   —   3E5Dh   —   3E3Dh   —   3E1Dh   —
                                        3EFCh      ADSTAT     3EDCh           —         3EBCh      CM1CON0          3E9Ch   DAC1CON1   3E7Ch   —   3E5Ch   —   3E3Ch   —   3E1Ch   —
                                         3EFBh    ADCON3       3EDBh          —         3EBBh       CM2PCH          3E9Bh      —       3E7Bh   —   3E5Bh   —   3E3Bh   —   3E1Bh   —
                                         3EFAh    ADCON2       3EDAh          —         3EBAh       CM2NCH          3E9Ah      —       3E7Ah   —   3E5Ah   —   3E3Ah   —   3E1Ah   —
                                                                              —                                                —               —           —           —           —


                                                                                                                                                                                       PIC18(L)F26/27/45/46/47/55/56/57K42
                                         3EF9h    ADCON1       3ED9h                    3EB9h      CM2CON1          3E99h              3E79h       3E59h       3E39h       3E19h
                                         3EF8h    ADCON0       3ED8h          —         3EB8h      CM2CON0          3E98h      —       3E78h   —   3E58h   —   3E38h   —   3E18h   —
                                         3EF7h    ADPREH       3ED7h        ADCP        3EB7h           —           3E97h      —       3E77h   —   3E57h   —   3E37h   —   3E17h   —
                                         3EF6h     ADPREL      3ED6h          —         3EB6h           —           3E96h      —       3E76h   —   3E56h   —   3E36h   —   3E16h   —
                                         3EF5h     ADCAP       3ED5h          —         3EB5h           —           3E95h      —       3E75h   —   3E55h   —   3E35h   —   3E15h   —
                                         3EF4h    ADACQH       3ED4h          —         3EB4h           —           3E94h      —       3E74h   —   3E54h   —   3E34h   —   3E14h   —
                                         3EF3h     ADACQL      3ED3h          —         3EB3h           —           3E93h      —       3E73h   —   3E53h   —   3E33h   —   3E13h   —
                                         2EF2h        —        3ED2h          —         3EB2h           —           3E92h      —       3E72h   —   3E52h   —   3E32h   —   3E12h   —
                                         3EF1h     ADPCH       3ED1h          —         3EB1h           —           3E91h      —       3E71h   —   3E51h   —   3E31h   —   3E11h   —
                                         3EF0h    ADRESH       3ED0h          —         3EB0h           —           3E90h      —       3E70h   —   3E50h   —   3E30h   —   3E10h   —
                                         3EEFh     ADRESL      3ECFh          —         3EAFh           —           3E8Fh      —       3E6Fh   —   3E4Fh   —   3E2Fh   —   3E0Fh   —
                                        3EEEh     ADPREVH      3ECEh          —         3EAEh           —           3E8Eh      —       3E6Eh   —   3E4Eh   —   3E2Eh   —   3E0Eh   —
                                        3EEDh     ADPREVL     3ECDh           —         3EADh           —           3E8Dh      —       3E6Dh   —   3E4Dh   —   3E2Dh   —   3E0Dh   —
                                        3EECh       ADRPT     3ECCh           —         3EACh           —           3E8Ch      —       3E6Ch   —   3E4Ch   —   3E2Ch   —   3E0Ch   —
                                        3EEBh      ADCNT       3ECBh          —         3EABh           —           3E8Bh      —       3E6Bh   —   3E4Bh   —   3E2Bh   —   3E0Bh   —
                                        3EEAh     ADACCU       3ECAh HLVDCON1           3EAAh           —           3E8Ah      —       3E6Ah   —   3E4Ah   —   3E2Ah   —   3E0Ah   —
                                         3EE9h    ADACCH       3EC9h HLVDCON0           3EA9h           —           3E89h      —       3E69h   —   3E49h   —   3E29h   —   3E09h   —
                                         3EE8h     ADACCL      3EC8h          —         3EA8h           —           3E88h      —       3E68h   —   3E48h   —   3E28h   —   3E08h   —
                                         3EE7h    ADFLTRH      3EC7h          —         3EA7h           —           3E87h      —       3E67h   —   3E47h   —   3E27h   —   3E07h   —
                                         3EE6h    ADFLTRL      3EC6h          —         3EA6h           —           3E86h      —       3E66h   —   3E46h   —   3E26h   —   3E06h   —
                                         3EE5h    ADSTPTH      3EC5h          —         3EA5h           —           3E85h      —       3E65h   —   3E45h   —   3E25h   —   3E05h   —
                                         3EE4h    ADSTPTL      3EC4h          —         3EA4h           —           3E84h      —       3E64h   —   3E44h   —   3E24h   —   3E04h   —
                                         3EE3h    ADERRH       3EC3h      ZCDCON        3EA3h           —           3E83h      —       3E63h   —   3E43h   —   3E23h   —   3E03h   —
                                         3EE2h     ADERRL      3EC2h          —         3EA2h           —           3E82h      —       3E62h   —   3E42h   —   3E22h   —   3E02h   —
                                         3EE1h    ADUTHH       3EC1h      FVRCON        3EA1h           —           3E81h      —       3E61h   —   3E41h   —   3E21h   —   3E01h   —
                                         3EE0h     ADUTHL      3EC0h       CMOUT        3EA0h           —           3E80h      —       3E60h   —   3E40h   —   3E20h   —   3E00h   —
                                        Legend:     Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:     Unimplemented in LF devices.
                                               2:   Unimplemented in PIC18(L)F26/27K42.
                                               3:   Unimplemented in PIC18(L)F26/27/45/46/47K42.
DS40001919G-page 50
                                        TABLE 4-6:            SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 61
 2017-2021 Microchip Technology Inc.


                                          3DFFh        —       3DDFh       U2FIFO        3DBFh           —             3D9Fh   —   3D7Fh         —      3D5Fh   I2C2CON2   3D3Fh   —   3D1Fh      —
                                          3DFEh        —       3DDEh      U2BRGH         3DBEh           —             3D9Eh   —   3D7Eh         —      3D5Eh   I2C2CON1   3D3Eh   —   3D1Eh      —
                                          3DFDh        —       3DDDh       U2BRGL       3DBDh            —             3D9Dh   —   3D7Dh         —      3D5Dh   I2C2CON0   3D3Dh   —   3D1Dh      —
                                          3DFCh        —       3DDCh       U2CON2       3DBCh            —             3D9Ch   —   3D7Ch     I2C1BTO    3D5Ch   I2C2ADR3   3D3Ch   —   3D1Ch   SPI1CLK
                                          3DFBh        —       3DDBh       U2CON1        3DBBh           —             3D9Bh   —   3D7Bh     I2C1CLK    3D5Bh   I2C2ADR2   3D3Bh   —   3D1Bh  SPI1INTE
                                          3DFAh    U1ERRIE     3DDAh       U2CON0        3DBAh           —             3D9Ah   —   3D7Ah      I2C1PIE   3D5Ah   I2C2ADR1   3D3Ah   —   3D1Ah  SPI1INTF
                                          3DF9h    U1ERRIR     3DD9h          —          3DB9h           —             3D99h   —   3D79h      I2C1PIR   3D59h   I2C2ADR0   3D39h   —   3D19h  SPI1BAUD


                                                                                                                                                                                                          PIC18(L)F26/27/45/46/47/55/56/57K42
                                          3DF8h      U1UIR     3DD8h        U2P3L        3DB8h           —             3D98h   —   3D78h   I2C1STAT1    3D58h   I2C2ADB1   3D38h   —   3D18h SPI1TWIDTH
                                          3DF7h     U1FIFO     3DD7h          —          3DB7h           —             3D97h   —   3D77h   I2C1STAT0    3D57h   I2C2ADB0   3D37h   —   3D17h SPI1STATUS
                                          3DF6h    U1BRGH      3DD6h        U2P2L        3DB6h           —             3D96h   —   3D76h     I2C1ERR    3D56h    I2C2CNT   3D36h   —   3D16h  SPI1CON2
                                          3DF5h     U1BRGL     3DD5h          —          3DB5h           —             3D95h   —   3D75h   I2C1CON2     3D55h    I2C2TXB   3D35h   —   3D15h  SPI1CON1
                                          3DF4h     U1CON2     3DD4h        U2P1L        3DB4h           —             3D94h   —   3D74h   I2C1CON1     3D54h    I2C2RXB   3D34h   —   3D14h  SPI1CON0
                                          3DF3h     U1CON1     3DD3h          —          3DB3h           —             3D93h   —   3D73h   I2C1CON0     3D53h       —      3D33h   —   3D13h SPI1TCNTH
                                          3DF2h     U1CON0     3DD2h        U2TXB        3DB2h           —             3D92h   —   3D72h    I2C1ADR3    3D52h       —      3D32h   —   3D12h SPI1TCNTL
                                          3DF1h      U1P3H     3DD1h          —          3DB1h           —             3D91h   —   3D71h    I2C1ADR2    3D51h       —      3D31h   —   3D11h   SPI1TXB
                                          3DF0h      U1P3L     3DD0h       U2RXB         3DB0h           —             3D90h   —   3D70h    I2C1ADR1    3D50h       —      3D30h   —   3D10h   SPI1RXB
                                          3DEFh      U1P2H     3DCFh          —          3DAFh           —             3D8Fh   —   3D6Fh    I2C1ADR0    3D4Fh       —      3D2Fh   —   3D0Fh      —
                                          3DEEh      U1P2L     3DCEh          —          3DAEh           —             3D8Eh   —   3D6Eh    I2C1ADB1    3D4Eh       —      3D2Eh   —   3D0Eh      —
                                          3DEDh      U1P1H     3DCDh          —         3DADh            —             3D8Dh   —   3D6Dh    I2C1ADB0    3D4Dh       —      3D2Dh   —   3D0Dh      —
                                          3DECh      U1P1L     3DCCh          —         3DACh            —             3D8Ch   —   3D6Ch     I2C1CNT    3D4Ch       —      3D2Ch   —   3D0Ch      —
                                          3DEBh    U1TXCHK     3DCBh          —          3DABh           —             3D8Bh   —   3D6Bh     I2C1TXB    3D4Bh       —      3D2Bh   —   3D0Bh      —
                                          3DEAh      U1TXB     3DCAh          —          3DAAh           —             3D8Ah   —   3D6Ah     I2C1RXB    3D4Ah       —      3D2Ah   —   3D0Ah      —
                                          3DE9h    U1RXCHK     3DC9h          —          3DA9h           —             3D89h   —   3D69h         —      3D49h       —      3D29h   —   3D09h      —
                                          3DE8h     U1RXB      3DC8h          —          3DA8h           —             3D88h   —   3D68h         —      3D48h       —      3D28h   —   3D08h      —
                                          3DE7h        —       3DC7h          —          3DA7h           —             3D87h   —   3D67h         —      3D47h       —      3D27h   —   3D07h      —
                                          3DE6h        —       3DC6h          —          3DA6h           —             3D86h   —   3D66h     I2C2BTO    3D46h       —      3D26h   —   3D06h      —
                                          3DE5h        —       3DC5h          —          3DA5h           —             3D85h   —   3D65h     I2C2CLK    3D45h       —      3D25h   —   3D05h      —
                                          3DE4h        —       3DC4h          —          3DA4h           —             3D84h   —   3D64h      I2C2PIE   3D44h       —      3D24h   —   3D04h      —
                                          3DE3h        —       3DC3h          —          3DA3h           —             3D83h   —   3D63h      I2C2PIR   3D43h       —      3D23h   —   3D03h      —
                                          3DE2h    U2ERRIE     3DC2h          —          3DA2h           —             3D82h   —   3D62h   I2C2STAT1    3D42h       —      3D22h   —   3D02h      —
                                          3DE1h    U2ERRIR     3DC1h          —          3DA1h           —             3D81h   —   3D61h   I2C2STAT0    3D41h       —      3D21h   —   3D01h      —
                                          3DE0h      U2UIR     3DC0h          —          3DA0h           —             3D80h   —   3D60h     I2C2ERR    3D40h       —      3D20h   —   3D00h      —
                                        Legend:      Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:      Unimplemented in LF devices.
                                              2:     Unimplemented in PIC18(L)F26/27K42.
                                              3:     Unimplemented in PIC18(L)F26/27/45/46/47K42.
DS40001919G-page 51
                                        TABLE 4-7:           SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 60
 2017-2021 Microchip Technology Inc.


                                         3CFFh       —         3CDFh          —         3CBFh           —           3C9Fh   —   3C7Fh      —       3C5Fh   CLC4GLS3   3C3Fh   —   3C1Fh   —
                                        3CFEh     MD1CARH     3CDEh           —         3CBEh           —           3C9Eh   —   3C7Eh   CLCDATA0   3C5Eh   CLC4GLS2   3C3Eh   —   3C1Eh   —
                                        3CFDh     MD1CARL     3CDDh           —         3CBDh           —           3C9Dh   —   3C7Dh   CLC1GLS3   3C5Dh   CLC4GLS1   3C3Dh   —   3C1Dh   —
                                        3CFCh     MD1SRC      3CDCh           —         3CBCh           —           3C9Ch   —   3C7Ch   CLC1GLS2   3C5Ch   CLC4GLS0   3C3Ch   —   3C1Ch   —
                                        3CFBh     MD1CON1     3CDBh           —         3CBBh           —           3C9Bh   —   3C7Bh   CLC1GLS1   3C5Bh   CLC4SEL3   3C3Bh   —   3C1Bh   —
                                         3CFAh    MD1CON0     3CDAh           —         3CBAh           —           3C9Ah   —   3C7Ah   CLC1GLS0   3C5Ah   CLC4SEL2   3C3Ah   —   3C1Ah   —
                                         3CF9h       —         3CD9h          —         3CB9h           —           3C99h   —   3C79h   CLC1SEL3   3C59h   CLC4SEL1   3C39h   —   3C19h   —


                                                                                                                                                                                              PIC18(L)F26/27/45/46/47/55/56/57K42
                                         3CF8h       —         3CD8h          —         3CB8h           —           3C98h   —   3C78h   CLC1SEL2   3C58h   CLC4SEL0   3C38h   —   3C18h   —
                                         3CF7h       —         3CD7h          —         3CB7h           —           3C97h   —   3C77h   CLC1SEL1   3C57h   CLC4POL    3C37h   —   3C17h   —
                                         3CF6h       —         3CD6h          —         3CB6h           —           3C96h   —   3C76h   CLC1SEL0   3C56h   CLC4CON    3C36h   —   3C16h   —
                                         3CF5h       —         3CD5h          —         3CB5h           —           3C95h   —   3C75h   CLC1POL    3C55h      —       3C35h   —   3C15h   —
                                         3CF4h       —         3CD4h          —         3CB4h           —           3C94h   —   3C74h   CLC1CON    3C54h      —       3C34h   —   3C14h   —
                                         3CF3h       —         3CD3h          —         3CB3h           —           3C93h   —   3C73h   CLC2GLS3   3C53h      —       3C33h   —   3C13h   —
                                         3CF2h       —         3CD2h          —         3CB2h           —           3C92h   —   3C72h   CLC2GLS2   3C52h      —       3C32h   —   3C12h   —
                                         3CF1h       —         3CD1h          —         3CB1h           —           3C91h   —   3C71h   CLC2GLS1   3C51h      —       3C31h   —   3C11h   —
                                         3CF0h       —         3CD0h          —         3CB0h           —           3C90h   —   3C70h   CLC2GLS0   3C50h      —       3C30h   —   3C10h   —
                                        3CEFh        —         3CCFh          —         3CAFh           —           3C8Fh   —   3C6Fh   CLC2SEL3   3C4Fh      —       3C2Fh   —   3C0Fh   —
                                        3CEEh        —        3CCEh           —         3CAEh           —           3C8Eh   —   3C6Eh   CLC2SEL2   3C4Eh      —       3C2Eh   —   3C0Eh   —
                                        3CEDh        —        3CCDh           —         3CADh           —           3C8Dh   —   3C6Dh   CLC2SEL1   3C4Dh      —       3C2Dh   —   3C0Dh   —
                                        3CECh        —        3CCCh           —         3CACh           —           3C8Ch   —   3C6Ch   CLC2SEL0   3C4Ch      —       3C2Ch   —   3C0Ch   —
                                        3CEBh        —        3CCBh           —         3CABh           —           3C8Bh   —   3C6Bh   CLC2POL    3C4Bh      —       3C2Bh   —   3C0Bh   —
                                        3CEAh        —        3CCAh           —         3CAAh           —           3C8Ah   —   3C6Ah   CLC2CON    3C4Ah      —       3C2Ah   —   3C0Ah   —
                                         3CE9h       —         3CC9h          —         3CA9h           —           3C89h   —   3C69h   CLC3GLS3   3C49h      —       3C29h   —   3C09h   —
                                         3CE8h       —         3CC8h          —         3CA8h           —           3C88h   —   3C68h   CLC3GLS2   3C48h      —       3C28h   —   3C08h   —
                                         3CE7h       —         3CC7h          —         3CA7h           —           3C87h   —   3C67h   CLC3GLS1   3C47h      —       3C27h   —   3C07h   —
                                         3CE6h    CLKRCLK      3CC6h          —         3CA6h           —           3C86h   —   3C66h   CLC3GLS0   3C46h      —       3C26h   —   3C06h   —
                                         3CE5h    CLKRCON      3CC5h          —         3CA5h           —           3C85h   —   3C65h   CLC3SEL3   3C45h      —       3C25h   —   3C05h   —
                                         3CE4h       —         3CC4h          —         3CA4h           —           3C84h   —   3C64h   CLC3SEL2   3C44h      —       3C24h   —   3C04h   —
                                         3CE3h       —         3CC3h          —         3CA3h           —           3C83h   —   3C63h   CLC3SEL1   3C43h      —       3C23h   —   3C03h   —
                                         3CE2h       —         3CC2h          —         3CA2h           —           3C82h   —   3C62h   CLC3SEL0   3C42h      —       3C22h   —   3C02h   —
                                         3CE1h       —         3CC1h          —         3CA1h           —           3C81h   —   3C61h   CLC3POL    3C41h      —       3C21h   —   3C01h   —
                                         3CE0h       —         3CC0h          —         3CA0h           —           3C80h   —   3C60h   CLC3CON    3C40h      —       3C20h   —   3C00h   —
                                        Legend:     Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:     Unimplemented in LF devices.
                                               2:   Unimplemented in PIC18(L)F26/27K42.
                                               3:   Unimplemented in PIC18(L)F26/27/45/46/47K42.
DS40001919G-page 52
                                        TABLE 4-8:           SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 59
 2017-2021 Microchip Technology Inc.


                                         3BFFh    DMA1SIRQ     3BDFh     DMA2SIRQ       3BBFh           —           3B9Fh   —   3B7Fh   —   3B5Fh   —   3B3Fh   —   3B1Fh   —
                                         3BFEh    DMA1AIRQ     3BDEh     DMA2AIRQ       3BBEh           —           3B9Eh   —   3B7Eh   —   3B5Eh   —   3B3Eh   —   3B1Eh   —
                                        3BFDh DMA1CON1        3BDDh DMA2CON1            3BBDh           —           3B9Dh   —   3B7Dh   —   3B5Dh   —   3B3Dh   —   3B1Dh   —
                                        3BFCh DMA1CON0        3BDCh DMA2CON0            3BBCh           —           3B9Ch   —   3B7Ch   —   3B5Ch   —   3B3Ch   —   3B1Ch   —
                                         3BFBh DMA1SSAU        3BDBh DMA2SSAU           3BBBh           —           3B9Bh   —   3B7Bh   —   3B5Bh   —   3B3Bh   —   3B1Bh   —
                                         3BFAh DMA1SSAH        3BDAh DMA2SSAH           3BBAh           —           3B9Ah   —   3B7Ah   —   3B5Ah   —   3B3Ah   —   3B1Ah   —
                                         3BF9h    DMA1SSAL     3BD9h     DMA2SSAL       3BB9h           —           3B99h   —   3B79h   —   3B59h   —   3B39h   —   3B19h   —


                                                                                                                                                                                PIC18(L)F26/27/45/46/47/55/56/57K42
                                         3BF8h DMA1SSZH        3BD8h DMA2SSZH           3BB8h           —           3B98h   —   3B78h   —   3B58h   —   3B38h   —   3B18h   —
                                         3BF7h    DMA1SSZL     3BD7h     DMA2SSZL       3BB7h           —           3B97h   —   3B77h   —   3B57h   —   3B37h   —   3B17h   —
                                         3BF6h DMA1SPTRU 3BD6h DMA2SPTRU 3BB6h                          —           3B96h   —   3B76h   —   3B56h   —   3B36h   —   3B16h   —
                                         3BF5h DMA1SPTRH 3BD5h DMA2SPTRH 3BB5h                          —           3B95h   —   3B75h   —   3B55h   —   3B35h   —   3B15h   —
                                         3BF4h DMA1SPTRL 3BD4h DMA2SPTRL                3BB4h           —           3B94h   —   3B74h   —   3B54h   —   3B34h   —   3B14h   —
                                         3BF3h DMA1SCNTH 3BD3h DMA2SCNTH 3BB3h                          —           3B93h   —   3B73h   —   3B53h   —   3B33h   —   3B13h   —
                                         3BF2h DMA1SCNTL 3BD2h DMA2SCNTL                3BB2h           —           3B92h   —   3B72h   —   3B52h   —   3B32h   —   3B12h   —
                                         3BF1h DMA1DSAH        3BD1h DMA2DSAH           3BB1h           —           3B91h   —   3B71h   —   3B51h   —   3B31h   —   3B11h   —
                                         3BF0h    DMA1DSAL     3BD0h     DMA2DSAL       3BB0h           —           3B90h   —   3B70h   —   3B50h   —   3B30h   —   3B10h   —
                                         3BEFh DMA1DSZH        3BCFh DMA2DSZH           3BAFh           —           3B8Fh   —   3B6Fh   —   3B4Fh   —   3B2Fh   —   3B0Fh   —
                                        3BEEh     DMA1DSZL     3BCEh     DMA2DSZL       3BAEh           —           3B8Eh   —   3B6Eh   —   3B4Eh   —   3B2Eh   —   3B0Eh   —
                                        3BEDh DMA1DPTRH 3BCDh DMA2DPTRH 3BADh                           —           3B8Dh   —   3B6Dh   —   3B4Dh   —   3B2Dh   —   3B0Dh   —
                                        3BECh DMA1DPTRL 3BCCh DMA2DPTRL 3BACh                           —           3B8Ch   —   3B6Ch   —   3B4Ch   —   3B2Ch   —   3B0Ch   —
                                        3BEBh DMA1DCNTH 3BCBh DMA2DCNTH 3BABh                           —           3B8Bh   —   3B6Bh   —   3B4Bh   —   3B2Bh   —   3B0Bh   —
                                        3BEAh DMA1DCNTL 3BCAh DMA2DCNTL 3BAAh                           —           3B8Ah   —   3B6Ah   —   3B4Ah   —   3B2Ah   —   3B0Ah   —
                                         3BE9h    DMA1BUF      3BC9h      DMA2BUF       3BA9h           —           3B89h   —   3B69h   —   3B49h   —   3B29h   —   3B09h   —
                                         3BE8h       —         3BC8h          —         3BA8h           —           3B88h   —   3B68h   —   3B48h   —   3B28h   —   3B08h   —
                                         3BE7h       —         3BC7h          —         3BA7h           —           3B87h   —   3B67h   —   3B47h   —   3B27h   —   3B07h   —
                                         3BE6h       —         3BC6h          —         3BA6h           —           3B86h   —   3B66h   —   3B46h   —   3B26h   —   3B06h   —
                                         3BE5h       —         3BC5h          —         3BA5h           —           3B85h   —   3B65h   —   3B45h   —   3B25h   —   3B05h   —
                                         3BE4h       —         3BC4h          —         3BA4h           —           3B84h   —   3B64h   —   3B44h   —   3B24h   —   3B04h   —
                                         3BE3h       —         3BC3h          —         3BA3h           —           3B83h   —   3B63h   —   3B43h   —   3B23h   —   3B03h   —
                                         3BE2h       —         3BC2h          —         3BA2h           —           3B82h   —   3B62h   —   3B42h   —   3B22h   —   3B02h   —
                                         3BE1h       —         3BC1h          —         3BA1h           —           3B81h   —   3B61h   —   3B41h   —   3B21h   —   3B01h   —
                                         3BE0h       —         3BC0h          —         3BA0h           —           3B80h   —   3B60h   —   3B40h   —   3B20h   —   3B00h   —
                                        Legend:     Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:     Unimplemented in LF devices.
                                               2:   Unimplemented in PIC18(L)F26/27K42.
                                               3:   Unimplemented in PIC18(L)F26/27/45/46/47K42.
DS40001919G-page 53
                                        TABLE 4-9:           SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 58
 2017-2021 Microchip Technology Inc.


                                         3AFFh       —         3ADFh SPI1SDIPPS         3ABFh      PPSLOCK          3A9Fh        —       3A7Fh        —       3A5Fh       —     3A3Fh      —        3A1Fh   RD7PPS(2)
                                         3AFEh       —         3ADEh SPI1SCKPPS 3ABEh                  —(4)         3A9Eh        —       3A7Eh        —       3A5Eh       —     3A3Eh      —        3A1Eh   RD6PPS(2)
                                        3AFDh        —         3ADDh       ADACTPPS     3ABDh           —           3A9Dh        —       3A7Dh        —       3A5Dh       —     3A3Dh      —        3A1Dh   RD5PPS(2)
                                        3AFCh        —         3ADCh CLCIN3PPS          3ABCh           —           3A9Ch        —       3A7Ch        —       3A5Ch       —     3A3Ch      —        3A1Ch   RD4PPS(2)
                                         3AFBh       —         3ADBh CLCIN2PPS          3ABBh           —           3A9Bh        —       3A7Bh    RD1I2C(2)   3A5Bh    RB2I2C   3A3Bh      —        3A1Bh   RD3PPS(2)
                                         3AFAh       —         3ADAh CLCIN1PPS          3ABAh           —           3A9Ah        —       3A7Ah    RD0I2C(2)   3A5Ah    RB1I2C   3A3Ah      —        3A1Ah   RD2PPS(2)
                                         3AF9h       —         3AD9h CLCIN0PPS          3AB9h           —           3A99h       —(4)     3A79h       —(4)     3A59h      —(4)   3A39h      —        3A19h   RD1PPS(2)


                                                                                                                                                                                                                        PIC18(L)F26/27/45/46/47/55/56/57K42
                                         3AF8h       —         3AD8h MD1SRCPPS 3AB8h                    —           3A98h       —(4)     3A78h       —(4)     3A58h      —(4)   3A38h      —        3A18h   RD0PPS(2)
                                         3AF7h       —         3AD7h MD1CARHPPS 3AB7h                   —           3A97h        —       3A77h        —       3A57h     IOCBF   3A37h      —        3A17h    RC7PPS
                                         3AF6h       —         3AD6h MD1CARLPPS 3AB6h                   —           3A96h        —       3A76h        —       3A56h     IOCBN   3A36h      —        3A16h    RC6PPS
                                         3AF5h       —         3AD5h CWG3INPPS          3AB5h           —           3A95h        —       3A75h        —       3A55h     IOCBP   3A35h      —        3A15h    RC5PPS
                                         3AF4h       —         3AD4h CWG2INPPS          3AB4h           —           3A94h    INLVLF(3)   3A74h    INLVLD(2)   3A54h    INLVLB   3A34h      —        3A14h    RC4PPS
                                         3AF3h       —         3AD3h CWG1INPPS          3AB3h           —           3A93h   SLRCONF(3)   3A73h   SLRCOND(2)   3A53h   SLRCONB   3A33h      —        3A13h    RC3PPS
                                         3AF2h       —         3AD2h SMT1SIGPPS 3AB2h                   —           3A92h   ODCONF(3)    3A72h   ODCOND(2)    3A52h   ODCONB    3A32h      —        3A12h    RC2PPS
                                         3AF1h       —         3AD1h SMT1WINPPS 3AB1h                   —           3A91h     WPUF(3)    3A71h     WPUD(2)    3A51h     WPUB    3A31h      —        3A11h    RC1PPS
                                         3AF0h       —         3AD0h        CCP4PPS     3AB0h           —           3A90h    ANSELF(3)   3A70h    ANSELD(2)   3A50h    ANSELB   3A30h      —        3A10h    RC0PPS
                                         3AEFh       —         3ACFh        CCP3PPS     3AAFh           —           3A8Fh        —       3A6Fh        —       3A4Fh       —     3A2Fh   RF7PPS(3)   3A0Fh    RB7PPS
                                        3AEEh        —         3ACEh        CCP2PPS     3AAEh           —           3A8Eh        —       3A6Eh        —       3A4Eh       —     3A2Eh   RF6PPS(3)   3A0Eh    RB6PPS
                                        3AEDh        —         3ACDh        CCP1PPS     3AADh           —           3A8Dh        —       3A6Dh        —       3A4Dh       —     3A2Dh   RF5PPS(3)   3A0Dh    RB5PPS
                                        3AECh        —         3ACCh        T6INPPS     3AACh           —           3A8Ch        —       3A6Ch        —       3A4Ch       —     3A2Ch   RF4PPS(3)   3A0Ch    RB4PPS
                                        3AEBh        —         3ACBh        T4INPPS     3AABh           —           3A8Bh        —       3A6Bh     RC4I2C     3A4Bh       —     3A2Bh   RF3PPS(3)   3A0Bh    RB3PPS
                                        3AEAh        —         3ACAh        T2INPPS     3AAAh           —           3A8Ah        —       3A6Ah     RC3I2C     3A4Ah       —     3A2Ah   RF2PPS(3)   3A0Ah    RB2PPS
                                         3AE9h    U2CTSPPS     3AC9h         T5GPPS     3AA9h           —           3A89h       —(4)     3A69h       —(4)     3A49h      —(4)   3A29h   RF1PPS(3)   3A09h    RB1PPS
                                         3AE8h    U2RXPPS      3AC8h       T5CKIPPS     3AA8h           —           3A88h       —(4)     3A68h       —(4)     3A48h      —(4)   3A28h   RF0PPS(3)   3A08h    RB0PPS
                                         3AE7h       —         3AC7h         T3GPPS     3AA7h           —           3A87h      IOCEF     3A67h      IOCCF     3A47h     IOCAF   3A27h      —        3A07h    RA7PPS
                                         3AE6h    U1CTSPPS     3AC6h       T3CKIPPS     3AA6h           —           3A86h     IOCEN      3A66h      IOCCN     3A46h     IOCAN   3A26h      —        3A06h    RA6PPS
                                         3AE5h    U1RXPPS      3AC5h         T1GPPS     3AA5h           —           3A85h     IOCEP      3A65h      IOCCP     3A45h     IOCAP   3A25h      —        3A05h    RA5PPS
                                         3AE4h I2C2SDAPPS 3AC4h            T1CKIPPS     3AA4h           —           3A84h     INLVLE     3A64h     INLVLC     3A44h    INLVLA   3A24h      —        3A04h    RA4PPS
                                         3AE3h I2C2SCLPPS 3AC3h            T0CKIPPS     3AA3h           —           3A83h   SLRCONE(2)   3A63h    SLRCONC     3A43h   SLRCONA   3A23h      —        3A03h    RA3PPS
                                         3AE2h I2C1SDAPPS 3AC2h             INT2PPS     3AA2h           —           3A82h   ODCONE(2)    3A62h    ODCONC      3A42h   ODCONA    3A22h   RE2PPS(2)   3A02h    RA2PPS
                                         3AE1h I2C1SCLPPS 3AC1h             INT1PPS     3AA1h           —           3A81h      WPUE      3A61h      WPUC      3A41h     WPUA    3A21h   RE1PPS(2)   3A01h    RA1PPS
                                         3AE0h SPI1SSPPS       3AC0h        INT0PPS     3AA0h           —           3A80h    ANSELE(2)   3A60h     ANSELC     3A40h    ANSELA   3A20h   RE0PPS(2)   3A00h    RA0PPS
                                        Legend:     Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:     Unimplemented in LF devices.
                                               2:   Unimplemented in PIC18(L)F26/27K42.
                                               3:   Unimplemented in PIC18(L)F26/27/45/46/47K42.
                                               4:   Reserved, maintain as ‘0’.
DS40001919G-page 54
                                        TABLE 4-10:          SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 57
 2017-2021 Microchip Technology Inc.


                                        39FFh         —          39DFh      OSCFRQ        39BFh         —          399Fh      —      397Fh       —        395Fh    WDTU     393Fh   —   391Fh   —
                                         39FEh        —         39DEh      OSCTUNE       39BEh           —           399Eh      —    397Eh        —       395Eh    WDTH     393Eh   —   391Eh   —
                                         39FDh        —         39DDh       OSCEN        39BDh           —           399Dh      —    397Dh    SCANTRIG    395Dh    WDTL     393Dh   —   391Dh   —
                                         39FCh        —         39DCh      OSCSTAT       39BCh           —           399Ch      —    397Ch    SCANCON0    395Ch   WDTCON1   393Ch   —   391Ch   —
                                         39FBh        —         39DBh      OSCCON3       39BBh           —           399Bh      —    397Bh   SCANHADRU    395Bh   WDTCON0   393Bh   —   391Bh   —
                                         39FAh        —         39DAh      OSCCON2       39BAh           —           399Ah   PIE10   397Ah   SCANHADRH    395Ah      —      393Ah   —   391Ah   —
                                         39F9h        —         39D9h      OSCCON1       39B9h           —           3999h    PIE9   3979h   SCANHADRL    3959h      —      3939h   —   3919h   —


                                                                                                                                                                                                    PIC18(L)F26/27/45/46/47/55/56/57K42
                                         39F8h        —         39D8h      CPUDOZE       39B8h           —           3998h    PIE8   3978h   SCANLADRU    3958h      —      3938h   —   3918h   —
                                         39F7h     SCANPR       39D7h          —         39B7h           —           3997h    PIE7   3977h   SCANLADRH    3957h      —      3937h   —   3917h   —
                                         39F6h        —         39D6h          —         39B6h           —           3996h    PIE6   3976h   SCANLADRL    3956h      —      3936h   —   3916h   —
                                         39F5h        —         39D5h          —         39B5h           —           3995h    PIE5   3975h        —       3955h      —      3935h   —   3915h   —
                                         39F4h     DMA2PR       39D4h          —         39B4h           —           3994h    PIE4   3974h        —       3954h      —      3934h   —   3914h   —
                                         39F3h     DMA1PR       39D3h          —         39B3h           —           3993h    PIE3   3973h        —       3953h      —      3933h   —   3913h   —
                                         39F2h     MAINPR       39D2h          —         39B2h           —           3992h    PIE2   3972h        —       3952h      —      3932h   —   3912h   —
                                         39F1h      ISRPR       39D1h VREGCON(1)         39B1h           —           3991h    PIE1   3971h        —       3951h      —      3931h   —   3911h   —
                                         39F0h        —         39D0h      BORCON        39B0h           —           3990h    PIE0   3970h        —       3950h      —      3930h   —   3910h   —
                                         39EFh     PRLOCK       39CFh          —         39AFh           —           398Fh      —    396Fh        —       394Fh      —      392Fh   —   390Fh   —
                                         39EEh        —         39CEh          —         39AEh           —           398Eh      —    396Eh        —       394Eh      —      392Eh   —   390Eh   —
                                         39EDh        —         39CDh          —         39ADh           —           398Dh      —    396Dh        —       394Dh      —      392Dh   —   390Dh   —
                                         39ECh        —         39CCh          —         39ACh           —           398Ch      —    396Ch        —       394Ch      —      392Ch   —   390Ch   —
                                         39EBh        —         39CBh          —         39ABh           —           398Bh      —    396Bh        —       394Bh      —      392Bh   —   390Bh   —
                                         39EAh        —         39CAh          —         39AAh        PIR10          398Ah   IPR10   396Ah        —       394Ah      —      392Ah   —   390Ah   —
                                         39E9h        —         39C9h          —         39A9h         PIR9          3989h    IPR9   3969h    CRCCON1     3949h      —      3929h   —   3909h   —
                                         39E8h        —         39C8h          —         39A8h         PIR8          3988h    IPR8   3968h    CRCCON0     3948h      —      3928h   —   3908h   —
                                         39E7h        —         39C7h        PMD7        39A7h         PIR7          3987h    IPR7   3967h    CRCXORH     3947h      —      3927h   —   3907h   —
                                         39E6h    NVMCON2       39C6h        PMD6        39A6h         PIR6          3986h    IPR6   3966h     CRCXORL    3946h      —      3926h   —   3906h   —
                                         39E5h    NVMCON1       39C5h        PMD5        39A5h         PIR5          3985h    IPR5   3965h   CRCSHIFTH    3945h      —      3925h   —   3905h   —
                                         39E4h        —         39C4h        PMD4        39A4h         PIR4          3984h    IPR4   3964h    CRCSHIFTL   3944h      —      3924h   —   3904h   —
                                         39E3h     NVMDAT       39C3h        PMD3        39A3h         PIR3          3983h    IPR3   3963h    CRCACCH     3943h      —      3923h   —   3903h   —
                                         39E2h        —         39C2h        PMD2        39A2h         PIR2          3982h    IPR2   3962h     CRCACCL    3942h      —      3922h   —   3902h   —
                                         39E1h NVMADRH(4)       39C1h        PMD1        39A1h         PIR1          3981h    IPR1   3961h     CRCDATH    3941h      —      3921h   —   3901h   —
                                         39E0h    NVMADRL       39C0h        PMD0        39A0h         PIR0          3980h    IPR0   3960h     CRCDATL    3940h      —      3920h   —   3900h   —
                                        Legend:      Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:      Unimplemented in LF devices.
                                               2:    Unimplemented in PIC18(L)F26/27K42.
                                               3:    Unimplemented in PIC18(L)F26/27/45/46/47K42.
                                               4:    Unimplemented in PIC18(L)F45/55K42.
DS40001919G-page 55
                                        TABLE 4-11:         SPECIAL FUNCTION REGISTER MAP FOR PIC18(L)F26/27/45/46/47/55/56/57K42 DEVICES BANK 56
 2017-2021 Microchip Technology Inc.


                                         38FFh       —         38DFh          —         38BFh           —           389Fh     IVTADU     387Fh   —   385Fh   —   383Fh   —   381Fh   —
                                         38FEh       —         38DEh          —         38BEh           —           389Eh     IVTADH     387Eh   —   385Eh   —   383Eh   —   381Eh   —
                                         38FDh       —         38DDh          —         38BDh           —           389Dh     IVTADL     387Dh   —   385Dh   —   383Dh   —   381Dh   —
                                         38FCh       —         38DCh          —         38BCh           —           389Ch        —       387Ch   —   385Ch   —   383Ch   —   381Ch   —
                                         38FBh       —         38DBh          —         38BBh           —           389Bh        —       387Bh   —   385Bh   —   383Bh   —   381Bh   —
                                         38FAh       —         38DAh          —         38BAh           —           389Ah        —       387Ah   —   385Ah   —   383Ah   —   381Ah   —
                                         38F9h       —         38D9h          —         38B9h           —           3899h        —       3879h   —   3859h   —   3839h   —   3819h   —


                                                                                                                                                                                         PIC18(L)F26/27/45/46/47/55/56/57K42
                                         38F8h       —         38D8h          —         38B8h           —           3898h        —       3878h   —   3858h   —   3838h   —   3818h   —
                                         38F7h       —         38D7h          —         38B7h           —           3897h        —       3877h   —   3857h   —   3837h   —   3817h   —
                                         38F6h       —         38D6h          —         38B6h           —           3896h        —       3876h   —   3856h   —   3836h   —   3816h   —
                                         38F5h       —         38D5h          —         38B5h           —           3895h        —       3875h   —   3855h   —   3835h   —   3815h   —
                                         38F4h       —         38D4h          —         38B4h           —           3894h        —       3874h   —   3854h   —   3834h   —   3814h   —
                                         38F3h       —         38D3h          —         38B3h           —           3893h        —       3873h   —   3853h   —   3833h   —   3813h   —
                                         38F2h       —         38D2h          —         38B2h           —           3892h        —       3872h   —   3852h   —   3832h   —   3812h   —
                                         38F1h       —         38D1h          —         38B1h           —           3891h        —       3871h   —   3851h   —   3831h   —   3811h   —
                                         38F0h       —         38D0h          —         38B0h           —           3890h PRODH_SHAD     3870h   —   3850h   —   3830h   —   3810h   —
                                         38EFh       —         38CFh          —         38AFh           —           388Fh PRODL_SHAD     386Fh   —   384Fh   —   382Fh   —   380Fh   —
                                         38EEh       —         38CEh          —         38AEh           —           388Eh FSR2H_SHAD     386Eh   —   384Eh   —   382Eh   —   380Eh   —
                                         38EDh       —         38CDh          —         38ADh           —           388Dh FSR2L_SHAD     386Dh   —   384Dh   —   382Dh   —   380Dh   —
                                         38ECh       —         38CCh          —         38ACh           —           388Ch FSR1H_SHAD     386Ch   —   384Ch   —   382Ch   —   380Ch   —
                                         38EBh       —         38CBh          —         38ABh           —           388Bh FSR1L_SHAD     386Bh   —   384Bh   —   382Bh   —   380Bh   —
                                         38EAh       —         38CAh          —         38AAh           —           388Ah FSR0H_SHAD     386Ah   —   384Ah   —   382Ah   —   380Ah   —
                                         38E9h       —         38C9h          —         38A9h           —           3889h FSR0L_SHAD     3869h   —   3849h   —   3829h   —   3809h   —
                                         38E8h       —         38C8h          —         38A8h           —           3888h PCLATU_SHAD    3868h   —   3848h   —   3828h   —   3808h   —
                                         38E7h       —         38C7h          —         38A7h           —           3887h PCLATH_SHAD    3867h   —   3847h   —   3827h   —   3807h   —
                                         38E6h       —         38C6h          —         38A6h           —           3886h   BSR_SHAD     3866h   —   3846h   —   3826h   —   3806h   —
                                         38E5h       —         38C5h          —         38A5h           —           3885h WREG_SHAD      3865h   —   3845h   —   3825h   —   3805h   —
                                         38E4h       —         38C4h          —         38A4h           —           3884h STATUS_SHAD    3864h   —   3844h   —   3824h   —   3804h   —
                                         38E3h       —         38C3h          —         38A3h           —           3883h   SHADCON      3863h   —   3843h   —   3823h   —   3803h   —
                                         38E2h       —         38C2h          —         38A2h           —           3882h BSR_CSHAD      3862h   —   3842h   —   3822h   —   3802h   —
                                         38E1h       —         38C1h          —         38A1h           —           3881h WREG_CSHAD     3861h   —   3841h   —   3821h   —   3801h   —
                                         38E0h       —         38C0h          —         38A0h           —           3880h STATUS_CSHAD   3860h   —   3840h   —   3820h   —   3800h   —
                                        Legend:     Unimplemented data memory locations and registers, read as ‘0’.
                                        Note 1:     Unimplemented in LF devices.
                                               2:   Unimplemented in PIC18(L)F26/27K42.
                                               3:   Unimplemented in PIC18(L)F26/27/45/46/47K42.
DS40001919G-page 56
                       PIC18(L)F26/27/45/46/47/55/56/57K42
4.5.5       STATUS REGISTER
The STATUS register, shown in Register 4-2, contains
the arithmetic status of the ALU. As with any other SFR,
it can be the operand for any instruction.
If the STATUS register is the destination for an
instruction that affects the Z, DC, C, OV or N bits, the
results of the instruction are not written; instead, the
STATUS register is updated according to the
instruction performed. Therefore, the result of an
instruction with the STATUS register as its destination
may be different than intended. As an example, CLRF
STATUS will set the Z bit and leave the remaining
Status bits unchanged (‘0uuu u1uu’).
It is recommended that only BCF, BSF, SWAPF, MOVFF,
MOVWF and MOVFFL instructions are used to alter the
STATUS register, because these instructions do not
affect the Z, C, DC, OV or N bits in the STATUS
register.
For other instructions that do not affect Status bits, see
the instruction set summaries in Section
41.2 “Extended Instruction Set” and Table 41-3.
  Note:     The C and DC bits operate as the borrow
            and digit borrow bits, respectively, in
            subtraction.

4.5.6       CALL SHADOW REGISTER
When CALL instruction is used, the WREG, BSR and
STATUS are automatically saved in hardware and can
be accessed using the WREG_CSHAD, BSR_CSHAD
and STATUS_CSHAD registers.
  Note:     The contents of these registers may be
            handled correctly to avoid erroneous code
            execution.


 2017-2021 Microchip Technology Inc.                        DS40001919G-page 57
                      PIC18(L)F26/27/45/46/47/55/56/57K42
4.6         Register Definitions: Status Registers
REGISTER 4-2:          STATUS: STATUS REGISTER
        U-0          R-1/q          R-1/q          R/W-0/u      R/W-0/u           R/W-0/u      R/W-0/u        R/W-0/u

        —             TO                PD           N            OV                Z            DC              C
bit 7                                                                                                                bit 0


Legend:
R = Readable bit                W = Writable bit             U = Unimplemented bit, read as ‘0’
-n = Value at POR               ‘1’ = Bit is set             ‘0’ = Bit is cleared           x = Bit is unknown


bit 7            Unimplemented: Read as ‘0’
bit 6            TO: Time-Out bit
                 1 = Set at power-up or by execution of CLRWDT or SLEEP instruction
                 0 = A WDT time-out occurred
bit 5            PD: Power-Down bit
                 1 = Set at power-up or by execution of CLRWDT instruction
                 0 = Set by execution of the SLEEP instruction
bit 4            N: Negative bit used for signed arithmetic (2’s complement); indicates if the result is negative,
                 (ALU MSb = 1).
                 1 = The result is negative
                 0 = The result is positive
bit 3            OV: Overflow bit used for signed arithmetic (2’s complement); indicates an overflow of the 7-bit
                 magnitude, which causes the sign bit (bit 7) to change state.
                 1 = Overflow occurred for current signed arithmetic operation
                 0 = No overflow occurred
bit 2            Z: Zero bit
                 1 = The result of an arithmetic or logic operation is zero
                 0 = The result of an arithmetic or logic operation is not zero
bit 1            DC: Digit Carry/Borrow bit (ADDWF, ADDLW, SUBLW, SUBWF instructions)(1)
                 1 = A carry-out from the 4th low-order bit of the result occurred
                 0 = No carry-out from the 4th low-order bit of the result
bit 0            C: Carry/Borrow bit (ADDWF, ADDLW, SUBLW, SUBWF instructions)(1,2)
                 1 = A carry-out from the Most Significant bit of the result occurred
                 0 = No carry-out from the Most Significant bit of the result occurred
Note 1: For Borrow, the polarity is reversed. A subtraction is executed by adding the two’s complement of the
        second operand.
     2: For Rotate (RRF, RLF) instructions, this bit is loaded with either the high or low-order bit of the Source
        register.


 2017-2021 Microchip Technology Inc.                                                              DS40001919G-page 58
                       PIC18(L)F26/27/45/46/47/55/56/57K42
4.7       Data Addressing Modes                           4.7.1       INHERENT AND LITERAL
                                                                      ADDRESSING
  Note:      The execution of some instructions in the
             core PIC18 instruction set are changed       Many PIC18 control instructions do not need any
             when the PIC18 extended instruction set is   argument at all; they either perform an operation that
             enabled. See Section 4.8 “Data Memory        globally affects the device or they operate implicitly on
             and the Extended Instruction Set” for        one register. This addressing mode is known as
             more information.                            Inherent Addressing. Examples include SLEEP, RESET
                                                          and DAW.
While the program memory can be addressed in only         Other instructions work in a similar way but require an
one way – through the program counter – information       additional explicit argument in the opcode. This is
in the data memory space can be addressed in several      known as Literal Addressing mode because they
ways. For most instructions, the addressing mode is       require some literal value as an argument. Examples
fixed. Other instructions may use up to three modes,      include ADDLW and MOVLW, which respectively, add or
depending on which operands are used and whether or       move a literal value to the W register. Other examples
not the extended instruction set is enabled.              include CALL and GOTO, which include a 20-bit
The addressing modes are:                                 program memory address.
• Inherent
• Literal
• Direct
• Indirect
An additional addressing mode, Indexed Literal Offset,
is available when the extended instruction set is
enabled (XINST Configuration bit = 1). Its operation is
discussed in detail in Section 4.8.1 “Indexed
Addressing with Literal Offset”.


 2017-2021 Microchip Technology Inc.                                                       DS40001919G-page 59
                        PIC18(L)F26/27/45/46/47/55/56/57K42
4.7.2        DIRECT ADDRESSING                                  EXAMPLE 4-6:           HOW TO CLEAR RAM
Direct addressing specifies all or part of the source                                  (BANK 1) USING
and/or destination address of the operation within the                                 INDIRECT ADDRESSING
opcode itself. The options are specified by the                            LFSRFSR0, 100h ;
arguments accompanying the instruction.                         NEXT       CLRFPOSTINC0   ; Clear INDF
                                                                                          ; register then
In the core PIC18 instruction set, bit-oriented and byte-                                 ; inc pointer
oriented instructions use some version of direct                         BTFSS FSR0H, 1   ; All done with
addressing by default. All of these instructions include                                  ; Bank1?
some 8-bit literal address as their Least Significant                    BRA   NEXT       ; NO, clear next
Byte. This address specifies either a register address in       CONTINUE                  ; YES, continue
one of the banks of data RAM (Section 4.5.2 “General
Purpose Register File”) or a location in the Access             4.7.3.1      FSR Registers and the INDF
Bank (Section 4.5.4 “Access Bank”) as the data                               Operand
source for the instruction.
                                                                At the core of indirect addressing are three sets of
The Access RAM bit ‘a’ determines how the address is            registers: FSR0, FSR1 and FSR2. Each represents a
interpreted. When ‘a’ is ‘1’, the contents of the BSR           pair of 8-bit registers, FSRnH and FSRnL. Each FSR
(Section 4.5.1 “Bank Select Register (BSR)”) are                pair holds a 14-bit value, therefore, the two upper bits
used with the address to determine the complete 14-bit          of the FSRnH register are not used. The 14-bit FSR
address of the register. When ‘a’ is ‘0’, the address is        value can address the entire range of the data memory
interpreted as being a register in the Access Bank.             in a linear fashion. The FSR register pairs, then, serve
Addressing that uses the Access RAM is sometimes                as pointers to data memory locations.
also known as Direct Forced Addressing mode.
                                                                Indirect addressing is accomplished with a set of
A few instructions, such as MOVFFL, include the entire          Indirect File Operands, INDF0 through INDF2. These
14-bit address (either source or destination) in their          can be thought of as “virtual” registers; they are
opcodes. In these cases, the BSR is ignored entirely.           mapped in the SFR space but are not physically
The destination of the operation’s results is determined        implemented. Reading or writing to a particular INDF
by the destination bit ‘d’. When ‘d’ is ‘1’, the results are    register actually accesses the data addressed by its
stored back in the source register, overwriting its             corresponding FSR register pair. A read from INDF1,
original contents. When ‘d’ is ‘0’, the results are stored      for example, reads the data at the address indicated by
in the W register. Instructions without the ‘d’ argument        FSR1H:FSR1L. Instructions that use the INDF
have a destination that is implicit in the instruction; their   registers as operands actually use the contents of their
destination is either the target register being operated        corresponding FSR as a pointer to the instruction’s
on or the W register.                                           target. The INDF operand is just a convenient way of
                                                                using the pointer.
4.7.3        INDIRECT ADDRESSING                                Because indirect addressing uses a full 14-bit address,
Indirect addressing allows the user to access a location        data RAM banking is not necessary. Thus, the current
in data memory without giving a fixed address in the            contents of the BSR and the Access RAM bit have no
instruction. This is done by using File Select Registers        effect on determining the target address.
(FSRs) as pointers to the locations which are to be read
or written. Since the FSRs are themselves located in
RAM as Special File Registers, they can also be
directly manipulated under program control. This
makes FSRs very useful in implementing data
structures, such as tables and arrays in data memory.
The registers for indirect addressing are also
implemented with Indirect File Operands (INDFs) that
permit automatic manipulation of the pointer value with
auto-incrementing, auto-decrementing or offsetting
with another value. This allows for efficient code, using
loops, such as the example of clearing an entire RAM
bank in Example 4-6.


 2017-2021 Microchip Technology Inc.                                                            DS40001919G-page 60
                         PIC18(L)F26/27/45/46/47/55/56/57K42
4.7.3.2        FSR Registers, POSTINC,                              In this context, accessing an INDF register uses the
               POSTDEC, PREINC and PLUSW                            value in the associated FSR register without changing
                                                                    it. Similarly, accessing a PLUSW register gives the
In addition to the INDF operand, each FSR register pair
                                                                    FSR value an offset by that in the W register; however,
also has four additional indirect operands. Like INDF,
                                                                    neither W nor the FSR is actually changed in the
these are “virtual” registers which cannot be directly
                                                                    operation. Accessing the other virtual registers
read or written. Accessing these registers actually
                                                                    changes the value of the FSR register.
accesses the location to which the associated FSR
register pair points, and also performs a specific action
on the FSR value. They are:
• POSTDEC: accesses the location to which the
  FSR points, then automatically decrements the
  FSR by 1 afterwards
• POSTINC: accesses the location to which the
  FSR points, then automatically increments the
  FSR by 1 afterwards
• PREINC: automatically increments the FSR by 1,
  then uses the location to which the FSR points in
  the operation
• PLUSW: adds the signed value of the W register
  (range of -127 to 128) to that of the FSR and uses
  the location to which the result points in the
  operation.

FIGURE 4-6:               INDIRECT ADDRESSING
                                                                                           0000h
   Using an instruction with one of the             ADDWF, INDF1, 1                                      Bank 0
   indirect addressing registers as the                                                    0100h
   operand....                                                                                           Bank 1
                                                                                           0200h
                                                                                                         Bank 2
                                                                                           0300h
   ...uses the 14-bit address stored in                FSR1H:FSR1L
   the FSR pair associated with that
                                            7               0   7                 0
   register....                                                                                         Bank 3
                                            x x 1 1 1 1 1 0     1 1 0 0 1 1 0 0                         through
                                                                                                        Bank 61


   ...to determine the data memory
   location to be used in that operation.
   In this case, the FSR1 pair contains                                                    3E00h
   3ECCh. This means the contents of                                                                    Bank 62
   location 3ECCh will be added to that                                                    3F00h
   of the W register and stored back in                                                                 Bank 63
   3ECCh.                                                                                  3FFFh
                                                                                                    Data Memory


 2017-2021 Microchip Technology Inc.                                                                DS40001919G-page 61
                       PIC18(L)F26/27/45/46/47/55/56/57K42
Operations on the FSRs with POSTDEC, POSTINC                 4.8.1       INDEXED ADDRESSING WITH
and PREINC affect the entire register pair; that is,                     LITERAL OFFSET
rollovers of the FSRnL register from FFh to 00h carry
                                                             Enabling the PIC18 extended instruction set changes
over to the FSRnH register. On the other hand, results
                                                             the behavior of indirect addressing using the FSR2
of these operations do not change the value of any
                                                             register pair within Access RAM. Under the proper
flags in the STATUS register (e.g., Z, N, OV, etc.).
                                                             conditions, instructions that use the Access Bank – that
The PLUSW register can be used to implement a form           is, most bit-oriented and byte-oriented instructions –
of indexed addressing in the data memory space. By           can invoke a form of indexed addressing using an
manipulating the value in the W register, users can          offset specified in the instruction. This special
reach addresses that are fixed offsets from pointer          addressing mode is known as Indexed Addressing with
addresses. In some applications, this can be used to         Literal Offset, or Indexed Literal Offset mode.
implement some powerful program control structure,
                                                             When using the extended instruction set, this
such as software stacks, inside of data memory.
                                                             addressing mode requires the following:
4.7.3.3       Operations by FSRs on FSRs                     • The use of the Access Bank is forced (‘a’ = 0) and
Indirect addressing operations that target other FSRs        • The file address argument is less than or equal to
or virtual registers represent special cases. For              5Fh.
example, using an FSR to point to one of the virtual         Under these conditions, the file address of the
registers will not result in successful operations. As a     instruction is not interpreted as the lower byte of an
specific case, assume that FSR0H:FSR0L contains              address (used with the BSR in direct addressing), or as
3FE7h, the address of INDF1. Attempts to read the            an 8-bit address in the Access Bank. Instead, the value
value of the INDF1 using INDF0 as an operand will            is interpreted as an offset value to an Address Pointer,
return 00h. Attempts to write to INDF1 using INDF0 as        specified by FSR2. The offset and the contents of
the operand will result in a NOP.                            FSR2 are added to obtain the target address of the
On the other hand, using the virtual registers to write to   operation.
an FSR pair may not occur as planned. In these cases,
the value will be written to the FSR pair but without any    4.8.2       INSTRUCTIONS AFFECTED BY
incrementing or decrementing. Thus, writing to either                    INDEXED LITERAL OFFSET MODE
the INDF2 or POSTDEC2 register will write the same           Any of the core PIC18 instructions that can use direct
value to the FSR2H:FSR2L.                                    addressing are potentially affected by the Indexed
Since the FSRs are physical registers mapped in the          Literal Offset Addressing mode. This includes all
SFR space, they can be manipulated through all direct        byte-oriented and bit-oriented instructions, or almost
operations. Users may proceed cautiously when work-          one-half of the standard PIC18 instruction set.
ing on these registers, particularly if their code uses      Instructions that only use Inherent or Literal Addressing
indirect addressing.                                         modes are unaffected.
Similarly, operations by indirect addressing are generally   Additionally, byte-oriented and bit-oriented instructions
permitted on all other SFRs. Users may exercise the          are not affected if they do not use the Access Bank
appropriate caution that they do not inadvertently change    (Access RAM bit is ‘1’), or include a file address of 60h
settings that might affect the operation of the device.      or above. Instructions meeting these criteria will
                                                             continue to execute as before. A comparison of the
4.8       Data Memory and the Extended                       different possible addressing modes when the
                                                             extended instruction set is enabled is shown in
          Instruction Set                                    Figure 4-7.
Enabling the PIC18 extended instruction set (XINST           Those who desire to use byte-oriented or bit-oriented
Configuration bit = 1) significantly changes certain         instructions in the Indexed Literal Offset mode may
aspects of data memory and its addressing.                   note the changes to assembler syntax for this mode.
Specifically, the use of the Access Bank for many of the     This is described in more detail in Section
core PIC18 instructions is different; this is due to the     41.2.1 “Extended Instruction Syntax”.
introduction of a new addressing mode for the data
memory space.
What does not change is just as important. The size of
the data memory space is unchanged, as well as its
linear addressing. The SFR map remains the same.
Core PIC18 instructions can still operate in both Direct
and Indirect Addressing mode; inherent and literal
instructions do not change at all. Indirect addressing
with FSR0 and FSR1 also remain unchanged.


 2017-2021 Microchip Technology Inc.                                                          DS40001919G-page 62
                       PIC18(L)F26/27/45/46/47/55/56/57K42
FIGURE 4-7:            COMPARING ADDRESSING OPTIONS FOR BIT-ORIENTED AND
                       BYTE-ORIENTED INSTRUCTIONS (EXTENDED INSTRUCTION SET ENABLED)

   EXAMPLE INSTRUCTION: ADDWF, f, d, a (Opcode: 0010 01da ffff ffff)


                                         0000h
   When ‘a’ = 0 and f  60h:
                                         0060h
   The instruction executes in
   Direct Forced mode. ‘f’ is inter-               Bank 0

   preted as a location in the           0100h
   Access RAM between 060h                                                     00h
                                                    Bank 1
   and 0FFh. This is the same as                   through                     60h
   locations 3F60h to 3FFFh                        Bank 62
                                                                                     Valid range
   (Bank 63) of data memory.                                                             for ‘f’
   Locations below 60h are not                                                 FFh
                                         3F00h                    Access RAM
   available in this Addressing
                                                   Bank 63
   mode.
                                         3F60h
                                                    SFRs
                                         3FFFh
                                                 Data Memory


   When ‘a’ = 0 and f5Fh:             0000h
   The instruction executes in
   Indexed Literal Offset mode. ‘f’      0060h
                                                   Bank 0
   is interpreted as an offset to the
                                         0100h                   001001da ffffffff
   address value in FSR2. The
   two are added together to                        Bank 1
   obtain the address of the target                through
                                                   Bank 62
   register for the instruction. The
   address can be anywhere in                                      FSR2H    FSR2L
   the data memory space.
                                         3F00h
   Note that in this mode, the                     Bank 63
   correct syntax is now:                3F60h
   ADDWF [k], d                                     SFRs
   where ‘k’ is the same as ‘f’.         3FFFh
                                                 Data Memory


                                                                   BSR
   When ‘a’ = 1 (all values of f):       0000h                   00000000

   The instruction executes in
                                         0060h
   Direct mode (also known as
                                                   Bank 0
   Direct Long mode). ‘f’ is inter-      0100h
   preted as a location in one of
   the 63 banks of the data                         Bank 1      001001da ffffffff
   memory space. The bank is                       through
                                                   Bank 62
   designated by the Bank Select
   Register (BSR). The address
   can be in any implemented             3F00h
   bank in the data memory                         Bank 63
   space.                                3F60h
                                                    SFRs
                                         3FFFh
                                                 Data Memory


 2017-2021 Microchip Technology Inc.                                       DS40001919G-page 63
                        PIC18(L)F26/27/45/46/47/55/56/57K42
4.8.3       MAPPING THE ACCESS BANK IN                     4.9     PIC18 Instruction Execution and
            INDEXED LITERAL OFFSET MODE                            the Extended Instruction Set
The use of Indexed Literal Offset Addressing mode          Enabling the extended instruction set adds eight
effectively changes how the first 96 locations of Access   additional commands to the existing PIC18 instruction
RAM (00h to 5Fh) are mapped. Rather than containing        set. These instructions are executed as described in
just the contents of the bottom section of Bank 0, this    Section 41.2 “Extended Instruction Set”.
mode maps the contents from a user defined “window”
that can be located anywhere in the data memory
space. The value of FSR2 establishes the lower bound-
ary of the addresses mapped into the window, while the
upper boundary is defined by FSR2 plus 95 (5Fh).
Addresses in the Access RAM above 5Fh are mapped
as previously described (see Section 4.5.4 “Access
Bank”). An example of Access Bank remapping in this
addressing mode is shown in Figure 4-8.
Remapping of the Access Bank applies only to
operations using the Indexed Literal Offset mode.
Operations that use the BSR (Access RAM bit is ‘1’) will
continue to use direct addressing as before.

FIGURE 4-8:              REMAPPING THE ACCESS BANK WITH INDEXED LITERAL OFFSET
                         ADDRESSING
   Example Situation:
    ADDWF f, d, a                 0000h
    FSR2H:FSR2L = 120h
                                            Bank 0
    Locations in the region
    from the FSR2 pointer         0100h
    (0120h) to the pointer plus             Bank 1
                                  0120h
    05Fh (017Fh) are mapped                 Window
                                  017Fh                                                                   00h
    to the bottom of the
                                            Bank 1
    Access RAM (000h-05Fh).       0200h                                                 Bank 1 “Window”
    Special File Registers at                                                                             5Fh
                                                                                                          60h
    3F60h through 3FFFh are
    mapped to 60h through                    Bank 2
    FFh, as usual.                                                                           SFRs
                                            through
    Bank 0 addresses below                  Bank 62
    5Fh can still be addressed                                                                            FFh
    by using the BSR.                                                                    Access Bank
                                  3F00h
                                            Bank 63
                                  3F60h
                                             SFRs
                                  3FFFh
                                          Data Memory


 2017-2021 Microchip Technology Inc.                                                      DS40001919G-page 64
