45.    Instruction Set Summary
       The PIC18 devices incorporate the standard set of PIC18 core instructions, as well as an extended set
       of instructions to optimize code that is recursive or that utilizes a software stack. The extended set is
       discussed later in this section.

45.1   Standard Instruction Set
                                                                                               ®
       The standard PIC18 instruction set adds many enhancements to the previous PIC MCU instruction
       sets while maintaining an easy migration from these PIC MCU instruction sets. Most instructions
       are a single program memory word (16 bits), but there are a few instructions that require two- or
       three-program memory locations.
       Each single-word instruction is a 16-bit word divided into an opcode that specifies the instruction
       type and one or more operands, which further specifies the operation of the instruction.
       The instruction set is highly orthogonal and is grouped into four basic categories:
       •   Byte-oriented operations
       •   Bit-oriented operations
       •   Literal operations
       •   Control operations
       The PIC18 instruction set summary in Table 45-2 lists byte-oriented, bit-oriented, literal and control
       operations. Table 45-1 shows the opcode field descriptions.
       Most byte-oriented instructions have three operands:
       •   The file register (specified by ‘f’)
       •   The destination of the result (specified by ‘d’)
       •   The accessed memory (specified by ‘a’)
       The file register designator ‘f’ specifies which file register is to be used by the instruction. The
       destination designator ‘d’ specifies where the result of the operation is to be placed. If ‘d’ is zero, the
       result is placed in the WREG register. If ‘d’ is one, the result is placed in the file register specified in
       the instruction.
       All bit-oriented instructions have three operands:
       •   The file register (specified by ‘f’)
       •   The bit in the file register (specified by ‘b’)
       •   The accessed memory (specified by ‘a’)
       The bit field designator ‘b’ selects the number of the bit affected by the operation, while the file
       register designator ‘f’ represents the number of the file in which the bit is located.
       The literal instructions may use some of the following operands:
       •   A literal value to be loaded into a file register (specified by ‘k’)
       •   The desired FSR register to load the literal value into (specified by ‘f’)
       •   No operand required (specified by ‘—’)
       The control instructions may use some of the following operands:
       •   A program memory address (specified by ‘n’)
       •   The mode of the CALL or RETURN instructions (specified by ‘s’)
       •   The mode of the table read and table write instructions (specified by ‘m’)
       •   No operand required (specified by ‘—’)


--- p795 ---
All instructions are a single word, except for a few two- or three-word instructions. These
instructions were made two- or three-words to contain the required information in 32 or 48 bits.
In the second and third words, the four MSbs are ‘1’s. If this second or third word is executed as an
instruction (by itself), it will execute as a NOP.
All single-word instructions are executed in a single instruction cycle, unless a conditional test is true
or the Program Counter is changed as a result of the instruction. In these cases, the execution takes
two instruction cycles, with the additional instruction cycle(s) executed as a NOP.
The two-word instructions execute in two instruction cycles and three-word instructions execute in
three instruction cycles.
One instruction cycle consists of four oscillator periods. Thus, for an oscillator frequency of 4 MHz,
the normal instruction execution time is 1 μs. If a conditional test is true or the Program Counter
is changed as a result of an instruction, the instruction execution time is 2 μs. Two-word branch
instructions (if true) take 3 μs.
Figure 45-1, Figure 45-2 and Figure 45-3 show the general formats that the instructions can have. All
examples use the convention ‘nnh’ to represent a hexadecimal number.
The Instruction Set Summary, shown in Table 45-2, lists the standard instructions recognized by the
Microchip MPASMTM Assembler.
Standard Instruction Set provides a description of each instruction.

Table 45-1. Opcode Field Descriptions
Field              Description
                   RAM access bit
a                  a = 0: RAM location in Access RAM (BSR register is ignored)
                   a = 1: RAM bank is specified by BSR register (default)
ACCESS             ACCESS = 0: RAM access bit symbol
BANKED             BANKED = 1: RAM access bit symbol
bbb                Bit address within an 8-bit file register (0 to 7)
BSR                Bank Select Register (BSR). Used to select the current RAM bank.
                   Destination select bit
d                  d = 0: store result in WREG
                   d = 1: store result in file register f (default)
dest               Destination: either the WREG register or the specified register file location
f                  8-bit register file address (00h to FFh)
fn                 FSR Number (0 to 2)
                   12-bit register file address (000h to FFFh) or 14-bit register file address (0000h to 3FFFh). This is the
fs
                   source address.
                   12-bit register file address (000h to FFFh) or 14-bit register file address (0000h to 3FFFh). This is the
fd
                   destination address.
zs                 7-bit literal offset for FSR2 to used as register file address (000h to FFFh). This is the source address.
                   7-bit literal offset for FSR2 to used as register file address (000h to FFFh). This is the destination
zd
                   address.
k                  Literal field, constant data or label (may be either a 6-bit, 8-bit, 12-bit or a 20-bit value)
label              Label name
mm                 The mode of the TBLPTR register for the table read and table write instructions. Only used with table
                   read and table write instructions:
*                  No change to register (such as TBLPTR with table reads and writes)
*+                 Post-Increment register (such as TBLPTR with table reads and writes)
*-                 Post-Decrement register (such as TBLPTR with table reads and writes)
+*                 Pre-Increment register (such as TBLPTR with table reads and writes)


--- p796 ---
...........continued
Field               Description
                    The relative address (two’s complement number) for relative branch instructions or the direct address
n
                    for call/branch and return instructions
PRODH               Product of multiply high byte
PRODL               Product of multiply low byte
                    Fast Call/Return mode select bit
s                   s = 0: do not update into/from shadow registers (default)
                    s = 1: certain registers loaded into/from shadow registers (Fast mode)
u                   Unused or unchanged
W                   W = 0: Destination select bit symbol
WREG                Working register (accumulator)
                    Don’t care (‘0’ or ‘1’). The assembler will generate code with x = 0. It is the recommended form of use for
x
                    compatibility with all Microchip software tools.
TBLPTR              21-bit Table Pointer (points to a program memory location)
TABLAT              8-bit table latch
TOS                 Top-of-stack (TOS)
PC                  Program Counter
PCL                 Program Counter low byte
PCH                 Program Counter high byte
PCLATH              Program Counter high byte latch
PCLATU              Program Counter upper byte Latch
GIE                 Global Interrupt Enable bit
WDT                 Watchdog Timer
TO                  Time-Out bit
PD                  Power-Down bit
C, DC, Z, OV, N ALU Status bits: Carry, Digit Carry, Zero, Overflow, Negative
{ }                 Optional argument
[ ]                 Indexed address
( )                 Contents
< >                 Register bit field
[expr]<n>           Specifies bit n of the register indicated by pointer expr
→                   Assigned to
∈                   In the set of
italics             User defined term (font is Courier)


--- p797 ---
Figure 45-1. General Format for Byte-Oriented Instructions

   Byte-oriented file register operations                                              Example Instruction

   15                    10   9    8      7                              0

        OPCODE                d a                   f (FILE #)                         ADDWF MYREG, W, B


   d = 0 for result destination to be WREG register
   d = 1 for result destination to be file register (f)
   a = 0 to force Access Bank
   a = 1 for BSR to select bank
   f = 8-bit file register address


   Byte to Byte move operations (two-word)                                             Example Instruction

   15          12   11                                                   0

    OPCODE                          f (Source FILE #)                                  MOVFF MYREG1, MYREG2

   15          12   11                                                   0

        1111                      f (Destination FILE #)


   f = 12-bit file register address


   Byte to Byte move operations (three-word)                                           Example Instruction

   15                                                  4    3            0

                     OPCODE                                     FILE #                 MOVFFL MYREG1, MYREG2

   15          12   11                                                   0

        1111                                  FILE #

   15          12   11                                                   0

        1111                                  FILE #


--- p798 ---
Figure 45-2. General Format for Bit-Oriented and Literal Instructions

   Bit-oriented file register operations                                           Example Instruction

   15            12   11       9   8    7                               0

     OPCODE           b(BIT #) a                  f (FILE #)                       BSF MYREG, bit, B


   b = 3-bit position of bit in file register (f)
   a = 0 to force Access Bank
   a = 1 for BSR to select bank
   f = 8-bit file register address


   Literal operations                                                              Example Instruction

   15                              8    7                               0

              OPCODE                              k (literal)                      MOVLW 7Fh


   k = 8-bit immediate value


--- p799 ---
Figure 45-3. General Format for Control Instructions

   Control operations                                                               Example Instruction
   CALL, GOTO and Branch operations

   15                               8     7                              0

             OPCODE                             k<7:0> (literal)                    GOTO Label

   15            12   11                                                 0

     OPCODE                             k<19:8> (literal)


   k = 20-bit immediate value


   15                           9   8     7                              0

           OPCODE                   s           k<7:0> (literal)                    CALL MYFUNC

   15            12   11                                                 0

     OPCODE                             k<19:8> (literal)


   k = 20-bit immediate value
   s = Fast bit


   15                 11   10                                            0

        OPCODE                           n<10:0> (literal)                          BRA MYFUNC


   n = 11-bit immediate value


   15                               8     7                              0

             OPCODE                            n<7:0> (literal)                     BC MYFUNC


   n = 8-bit immediate value


--- p800 ---
                                                                              Table 45-2. Standard Instruction Set
                                                                                      Mnemonic,                                                                                     16-Bit Instruction Word
                                                                                                                                                                                                                            Status
                                                                                      Operands                                    Description               Cycles                                                                         Notes
                                                                                                                                                                        MSb                                     LSb        Affected
                                                                                            rotatethispage90


                                                                                                                                                          BYTE-ORIENTED FILE REGISTER INSTRUCTIONS
                                                                                  ADDWF                        f, d, a          Add WREG and f                1         0010         01da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                 ADDWFC                        f, d, a    Add WREG and Carry bit to f         1         0010         00da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                  ANDWF                        f, d, a         AND WREG with f                1         0001         01da            ffff      ffff           Z, N           1
                                                                                   CLRF                         f, a                 Clear f                  1         0110         101a            ffff      ffff            Z
                                                                                   COMF                        f, d, a           Complement f                 1         0001         11da            ffff      ffff           Z, N           1
                                                                                   DECF                        f, d, a            Decrement f                 1         0000         01da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                   INCF                        f, d, a            Increment f                 1         0010         10da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                  IORWF                        f, d, a     Inclusive OR WREG with f           1         0001         00da            ffff      ffff           Z, N           1
                                                                                   MOVF                        f, d, a        Move f to WREG or f             1         0101         00da            ffff      ffff           Z, N           1
                                                                                                                             Move fs (12-bit source)                    1100        fsfsfsfs      fsfsfsfs    fsfsfsfs


                                                                                  MOVFF                        fs, fd                                         2                                                              None          1, 3, 4
                                                                                                                            to fd (12-bit destination)                  1111        fdfdfdfd      fdfdfdfd    fdfdfdfd
                                                                                                                                                                        0000         0000            0110     fsfsfsfs
                                                                                                                             Move fs (14-bit source)
                                                                                  MOVFFL                       fs, fd                                         3         1111        fsfsfsfs      fsfsfsfs    fsfsfdfd       None           1, 3
                                                                                                                            to fd (14-bit destination)
                                                                                                                                                                        1111        fdfdfdfd      fdfdfdfd    fdfdfdfd
                                                                                  MOVWF                         f, a            Move WREG to f                1                                                              None
subsidiaries


                                                                                                                                                                        0110         111a            ffff      ffff
                                                          Data Sheet


                                                                                  MULWF                         f, a         Multiply WREG with f             1         0000         001a            ffff      ffff          None            1
                                                                                   NEGF                         f, a                Negate f                  1         0110         110a            ffff      ffff      C, DC, Z, OV, N     1
                                                                                   RLCF                        f, d, a    Rotate Left f through Carry         1         0011         01da            ffff      ffff          C, Z, N         1
                                                                                   RLNCF                       f, d, a      Rotate Left f (No Carry)          1         0100         01da            ffff      ffff           Z, N           1
                                                                                   RRCF                        f, d, a    Rotate Right f through Carry        1         0011         00da            ffff      ffff          C, Z, N         1
                                                                                  RRNCF                        f, d, a      Rotate Right f (No Carry)         1         0100         00da            ffff      ffff           Z, N           1
                                                                                   SETF                         f, a                  Set f                   1         0110         100a            ffff      ffff          None
                                                                                                                           Subtract f from WREG with
                                                                                  SUBFWB                       f, d, a                                        1         0101         01da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                                                                     Borrow
                                                                                  SUBWF                        f, d, a       Subtract WREG from f             1         0101         11da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                                                           Subtract WREG from f with
                                                                                  SUBWFB                       f, d, a                                        1         0101         10da            ffff      ffff      C, DC, Z, OV, N     1
                                                                                                                                    Borrow


                                                                                                                                                                                                                                                     Instruction Set Summary
                                                                                  SWAPF                        f, d, a         Swap nibbles in f              1         0011         10da            ffff      ffff          None            1
                                                                                  XORWF                        f, d, a     Exclusive OR WREG with f           1         0001         10da            ffff      ffff           Z, N           1


                                                          DS40002214F - 801


                                                                                  CPFSEQ                        f, a     Compare f with WREG, skip if =     1–4         0110         001a            ffff      ffff          None           1, 2
                                                                                  CPFSGT                        f, a     Compare f with WREG, skip if >     1–4         0110         010a            ffff      ffff          None           1, 2
                                                                                  CPFSLT                        f, a     Compare f with WREG, skip if <     1–4         0110         000a            ffff      ffff          None           1, 2
                                                                              ...........continued
                                                                                      Mnemonic,                                                                                  16-Bit Instruction Word
                                                                                                                                                                                                                       Status
                                                                                      Operands                                  Description             Cycles                                                                        Notes
                                                                                                                                                                      MSb                                  LSb        Affected
                                                                                           rotatethispage90


                                                                                  DECFSZ                      f, d, a      Decrement f, Skip if 0        1–4          0010        11da           ffff      ffff        None            1, 2
                                                                                  DCFSNZ                      f, d, a    Decrement f, Skip if Not 0      1–4          0100        11da           ffff      ffff        None            1, 2
                                                                                  INCFSZ                      f, d, a       Increment f, Skip if 0       1–4          0011        11da           ffff      ffff        None            1, 2
                                                                                  INFSNZ                      f, d, a     Increment f, Skip if Not 0     1–4          0100        10da           ffff      ffff        None            1, 2
                                                                                  TSTFSZ                       f, a            Test f, skip if 0         1–4          0110        011a           ffff      ffff        None            1, 2
                                                                                                                                                       BIT-ORIENTED FILE REGISTER INSTRUCTIONS
                                                                                    BCF                       f, b, a            Bit Clear f              1           1001        bbba           ffff      ffff        None             1
                                                                                    BSF                       f, b, a              Bit Set f              1           1000        bbba           ffff      ffff        None             1
                                                                                    BTG                       f, b, a            Bit Toggle f             1           0111        bbba           ffff      ffff        None             1
                                                                                                                                                           BIT-ORIENTED SKIP INSTRUCTIONS
                                                                                   BTFSC                      f, b, a      Bit Test f, Skip if Clear     1–4          1011        bbba           ffff      ffff        None            1, 2


                                                                                   BTFSS                      f, b, a       Bit Test f, Skip if Set      1–4          1010        bbba           ffff      ffff        None            1, 2
                                                                                                                                                                 CONTROL INSTRUCTIONS
                                                                                    BC                          n              Branch if Carry           1–2          1110        0010           nnnn      nnnn        None             2

                                                                                    BN                          n            Branch if Negative          1–2          1110        0110           nnnn      nnnn        None             2
subsidiaries


                                                                                                                                                                                                                       None
                                                          Data Sheet


                                                                                   BNC                          n           Branch if Not Carry          1–2          1110        0011           nnnn      nnnn                         2

                                                                                   BNN                          n          Branch if Not Negative        1–2          1110        0111           nnnn      nnnn        None             2

                                                                                   BNOV                         n          Branch if Not Overflow        1–2          1110        0101           nnnn      nnnn        None             2

                                                                                   BNZ                          n            Branch if Not Zero          1–2          1110        0001           nnnn      nnnn        None             2

                                                                                   BOV                          n            Branch if Overflow          1–2          1110        0100           nnnn      nnnn        None             2

                                                                                    BRA                         n         Branch Unconditionally          2           1101        0nnn           nnnn      nnnn        None             2

                                                                                    BZ                          n              Branch if Zero            1–2          1110        0000           nnnn      nnnn        None             2
                                                                                                                                                                      1110        110s           kkkk      kkkk
                                                                                   CALL                        k, s            Call subroutine            2                                                            None            2, 3
                                                                                                                                                                      1111        kkkk           kkkk      kkkk
                                                                                  CALLW                         —       Call subroutine using WREG        2           0000        0000           0001      0100        None             2
                                                                                                                                                                      1110        1111           kkkk      kkkk
                                                                                   GOTO                         k              Go to address              2                                                            None             3


                                                                                                                                                                                                                                              Instruction Set Summary
                                                                                                                                                                      1111        kkkk           kkkk      kkkk
                                                                                   RCALL                        n               Relative Call             2           1101        1nnn           nnnn      nnnn        None             2
                                                                                  RETFIE                        s       Return from interrupt enable      2           0000        0000           0001      000s   INTCONx STAT bits     2


                                                                                  RETLW                         k        Return with literal in WREG      2           0000        1100           kkkk      kkkk        None             2
                                                                                  RETURN                        s         Return from Subroutine          2           0000        0000           0001      001s        None             2
                                                                                                                                                                 INHERENT INSTRUCTIONS
                                                                              ...........continued
                                                                                      Mnemonic,                                                                                        16-Bit Instruction Word
                                                                                                                                                                                                                           Status
                                                                                      Operands                                   Description                  Cycles                                                                      Notes
                                                                                                                                                                            MSb                                  LSb      Affected
                                                                                            rotatethispage90


                                                                                  CLRWDT                        —           Clear Watchdog Timer                1          0000         0000           0000      0100      TO, PD
                                                                                   DAW                          —           Decimal Adjust WREG                 1          0000         0000           0000      0111         C
                                                                                   NOP                          —               No Operation                    1          0000         0000           0000      0000       None
                                                                                   NOP                          —               No Operation                    1          1111         xxxx           xxxx      xxxx       None           3
                                                                                   POP                          —       Pop top of return stack (TOS)           1          0000         0000           0000      0110       None
                                                                                   PUSH                         —       Push top of return stack (TOS)          1          0000         0000           0000      0101       None
                                                                                   RESET                        —           Software device Reset               1          0000         0000           1111      1111         All
                                                                                   SLEEP                        —          Go into Standby mode                 1          0000         0000           0000      0011      TO, PD
                                                                                                                                                                       LITERAL INSTRUCTIONS
                                                                                  ADDFSR                       fn, k      Add FSR (fn) with literal (k)         1          1110         1000          fnfnkk     kkkk       None
                                                                                  ADDLW                         k           Add literal and WREG                1          0000         1111           kkkk      kkkk   C, DC, Z, OV, N


                                                                                  ANDLW                         k          AND literal with WREG                1          0000         1011           kkkk      kkkk        Z, N
                                                                                  IORLW                         k       Inclusive OR literal with WREG          1          0000         1001           kkkk      kkkk        Z, N
                                                                                                                       Load FSR(fn) with a 14-bit literal                  1110         1110          00fnfn     kkkk
                                                                                   LFSR                        fn, k                                            2                                                           None           3
                                                                                                                                     (k)                                   1111         00kk           kkkk      kkkk
subsidiaries


                                                                                  MOVLB                         k         Move literal to BSR<5:0>              1          0000         0001           00kk      kkkk       None
                                                          Data Sheet


                                                                                  MOVLW                         k           Move literal to WREG                1          0000         1110           kkkk      kkkk       None
                                                                                  MULLW                         k         Multiply literal with WREG            1          0000         1101           kkkk      kkkk       None
                                                                                  RETLW                         k        Return with literal in WREG            2          0000         1100           kkkk      kkkk       None
                                                                                  SUBFSR                       fn, k   Subtract literal (k) from FSR (fn)       1          1110         1001          fnfnkk     kkkk       None
                                                                                  SUBLW                         k        Subtract WREG from literal             1          0000         1000           kkkk      kkkk   C, DC, Z, OV, N
                                                                                  XORLW                         k       Exclusive OR literal with WREG          1          0000         1010           kkkk      kkkk        Z, N

                                                                                                                                                          DATA MEMORY – PROGRAM MEMORY INSTRUCTIONS
                                                                                  TBLRD*                        —                 Table Read                    2          0000         0000           0000      1000       None
                                                                                 TBLRD*+                        —      Table Read with post-increment           2          0000         0000           0000      1001       None
                                                                                  TBLRD*-                       —      Table Read with post-decrement           2          0000         0000           0000      1010       None
                                                                                 TBLRD+*                        —      Table Read with pre-increment            2          0000         0000           0000      1011       None
                                                                                  TBLWT*                        —                 Table Write                   2                                                           None


                                                                                                                                                                                                                                                  Instruction Set Summary
                                                                                                                                                                           0000         0000           0000      1100
                                                                                 TBLWT*+                        —      Table Write with post-increment          2          0000         0000           0000      1101       None
                                                                                 TBLWT*-                        —      Table Write with post-decrement          2          0000         0000           0000      1110       None


                                                                                 TBLWT+*                        —      Table Write with pre-increment           2          0000         0000           0000      1111       None
                                                                              ...........continued
                                                                                             Mnemonic,                                                                            16-Bit Instruction Word
                                                                                                                                                                                                                                      Status
                                                                                             Operands                        Description           Cycles                                                                                                  Notes
                                                                                                                                                                   MSb                                               LSb             Affected
                                                                                                          rotatethispage90


                                                                              Notes:   rotatethispage90


                                                                              1.   When a PORT register is modified as a function of itself (e.g., MOVF PORTB, 1, 0), the value used will be that value present on the pins themselves. For example, if the data
                                                                                   latch is ‘1’ for a pin configured as input and is driven low by an external device, the data will be written back with a ‘0’.
                                                                              2.   If Program Counter (PC) is modified or a conditional test is true, the instruction requires two cycles. The second cycle is executed as a NOP.
                                                                              3.   Some instructions are multi-word instructions. The extra words of these instructions will be executed as a NOP unless the first word of the instruction retrieves the
                                                                                   information embedded in these 16 bits. This ensures that all program memory locations have a valid instruction.
                                                                              4.   fs and fd do not cover the full memory range. 2 MSbs of bank selection are forced to 0b00 to limit the range of these instructions to the lower 4k addressing space.
subsidiaries

                                                          Data Sheet


                                                                                                                                                                                                                                                                   Instruction Set Summary

45.1.1 Standard Instruction Set

                      Important: All PIC18 instructions may take an optional label argument preceding the
                      instruction mnemonic for use in symbolic addressing. If a label is used, the instruction
                      format then becomes:
                      {label} instruction argument(s).


        ADDFSR                Add Literal to FSR
        Syntax                ADDFSR fn, k
        Operands              0 ≤ k ≤ 63
                              fn ∈ [0, 1, 2]
        Operation             (FSRfn) + k → FSRfn
        Status Affected       None
        Encoding                        1110                            1000                  fnfnkk                     kkkk
        Description           The 6-bit literal ‘k’ is added to the contents of the FSR specified by ‘fn’
        Words                 1
        Cycles                1


        Q Cycle Activity:
                      Q1                               Q2                              Q3                              Q4
                    Decode                       Read literal ‘k’                  Process Data                    Write to FSR

        Example: ADDFSR 2, 23h

        Before Instruction
        FSR2 = 03FFh

        After Instruction
        FSR2 = 0422h


        ADDLW                 Add Literal to W
        Syntax                ADDLW k
        Operands              0 ≤ k ≤ 255
        Operation             (W) + k → W
        Status Affected       N, OV, C, DC, Z
        Encoding                        0000                            1111                      kkkk                   kkkk
        Description           The contents of W are added to the 8-bit literal ‘k’ and the result is placed in W
        Words                 1
        Cycles                1


        Q Cycle Activity:
                      Q1                               Q2                              Q3                              Q4
                    Decode                       Read literal ‘k’                  Process Data                    Write to W

        Example: ADDLW 15h


--- p805 ---
Before Instruction
W = 10h

After Instruction
W = 25h


ADDWF                Add W to f
Syntax               ADDWF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (W) + (f) → dest
Status Affected      N, OV, C, DC, Z
Encoding                        0010                         01da                          ffff                          ffff
Description          Add W to register ‘f’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the result is stored back in register
                     ‘f’ (default).
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                   Q3                                   Q4
            Decode                   Read register ‘f’                     Process Data                     Write to destination

Example: ADDWF REG, 0, 0

Before Instruction
W = 17h
REG = 0C2h

After Instruction
W = 0D9h
REG = 0C2h


ADDWFC               Add W and Carry Bit to f
Syntax               ADDWFC f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (W) + (f) + (C) → dest
Status Affected      N, OV, C, DC, Z
Encoding                        0010                         00da                          ffff                          ffff


--- p806 ---
...........continued
ADDWFC                 Add W and Carry Bit to f
Syntax                 ADDWFC f {,d {,a}}
Description            Add W, the Carry flag and data memory location ‘f’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the
                       result is placed in data memory location ‘f’.
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                              Q2                                 Q3                                  Q4
            Decode                    Read register ‘f’                    Process Data                    Write to destination

Example: ADDWFC REG, 0, 1

Before Instruction
Carry bit = 1
REG = 02h
W = 4Dh

After Instruction
Carry bit = 0
REG = 02h
W = 50h


ANDLW                  AND Literal with W
Syntax                 ANDLW k
Operands               0 ≤ k ≤ 255
Operation              (W) .AND. k → W
Status Affected        N, Z
Encoding                         0000                          1011                       kkkk                         kkkk
Description            The contents of W are ANDed with the 8-bit literal ‘k’. The result is placed in W
Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                              Q2                                 Q3                                  Q4
            Decode                      Read literal ‘k’                   Process Data                         Write to W

Example: ANDLW 05Fh

Before Instruction
W = A3h

After Instruction
W = 03h


--- p807 ---
ANDWF                   AND W with f
Syntax                  ANDWF f {,d {,a}}
Operands                0 ≤ f ≤ 255
                        d ∈ [0, 1]
                        a ∈ [0, 1]
Operation               (W) .AND. (f) → dest
Status Affected         N, Z
Encoding                           0001                         01da                        ffff                         ffff
Description             The contents of W are ANDed with register ‘f’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the result
                        is stored back in register ‘f’ (default).
                        If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                        If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                        Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                        Indexed Literal Offset Mode for details.

Words                   1
Cycles                  1


Q Cycle Activity:
              Q1                                  Q2                              Q3                                   Q4
            Decode                      Read register ‘f’                    Process Data                    Write to destination

Example: ANDWF REG, 0, 0

Before Instruction
W = 17h
REG = C2h

After Instruction
W = 02h
REG = C2h


BC                      Branch if Carry
Syntax                  BC n
Operands                -128 ≤ n ≤ 127
Operation               If the Carry bit is ‘1’
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                           1110                         0010                        nnnn                         nnnn
Description             If the Carry bit is ‘1’, then the program will branch. The two’s complement number ‘2n’ is added to
                        the PC. Since the PC will have incremented to fetch the next instruction, the new address will be PC
                        + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                                  Q2                              Q3                                   Q4
            Decode                       Read literal ‘n’                    Process Data                         Write to PC
         No operation                     No operation                       No operation                        No operation


--- p808 ---
If No Jump:

              Q1                              Q2                               Q3                                  Q4
            Decode                    Read literal ‘n’                    Process Data                       No operation

Example: HERE BC 5

Before Instruction
PC = address (HERE)

After Instruction
If Carry = 1; PC = address (HERE + 12)
If Carry = 0; PC = address (HERE + 2)


BCF                  Bit Clear f
Syntax               BCF f, b {,a}
Operands             0 ≤ f ≤ 255
                     0≤b≤7
                     a ∈ [0, 1]
Operation            0 → f<b>
Status Affected      None
Encoding                        1001                           bbba                      ffff                        ffff
Description          Bit ‘b’ in register ‘f’ is cleared.
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                              Q2                               Q3                                  Q4
            Decode                   Read register ‘f’                    Process Data                     Write register ‘f’

Example: BCF FLAG_REG, 7, 0

Before Instruction
FLAG_REG = C7h

After Instruction
FLAG_REG = 47h


BN                   Branch if Negative
Syntax               BN n
Operands             -128 ≤ n ≤ 127
Operation            If NEGATIVE bit is ‘1’
                     (PC) + 2 + 2n → PC
Status Affected      None
Encoding                        1110                           0110                      nnnn                        nnnn


--- p809 ---
...........continued
BN                      Branch if Negative
Syntax                  BN n
Description             If the NEGATIVE bit is ‘1’, then the program will branch. The two’s complement number ‘2n’ is added
                        to the PC. Since the PC will have incremented to fetch the next instruction, the new address will be
                        PC + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                                  Q2                           Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data                Write to PC
         No operation                     No operation                     No operation               No operation

If No Jump:

              Q1                                  Q2                           Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data               No operation

Example: HERE BN Jump

Before Instruction
PC = address (HERE)

After Instruction
If NEGATIVE = 1; PC = address (Jump)
If NEGATIVE = 0; PC = address (HERE + 2)


BNC                     Branch if Not Carry
Syntax                  BNC n
Operands                -128 ≤ n ≤ 127
Operation               If the Carry bit is ‘0’
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                           1110                         0011                      nnnn                nnnn
Description             If the Carry bit is ‘0’, then the program will branch. The two’s complement number ‘2n’ is added to
                        the PC. Since the PC will have incremented to fetch the next instruction, the new address will be PC
                        + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                                  Q2                           Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data                Write to PC
         No operation                     No operation                     No operation               No operation

If No Jump:


--- p810 ---
              Q1                                 Q2                            Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data               No operation

Example: HERE BNC Jump

Before Instruction
PC = address (HERE)

After Instruction
If Carry = 0; PC = address (Jump)
If Carry = 1; PC = address (HERE + 2)


BNN                     Branch if Not Negative
Syntax                  BNN n
Operands                -128 ≤ n ≤ 127
Operation               If NEGATIVE bit is ‘0’
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                          1110                          0111                      nnnn               nnnn
Description             If the NEGATIVE bit is ‘0’, then the program will branch. The two’s complement number ‘2n’ is added
                        to the PC. Since the PC will have incremented to fetch the next instruction, the new address will be
                        PC + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                                 Q2                            Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data                Write to PC
         No operation                    No operation                      No operation               No operation

If No Jump:

              Q1                                 Q2                            Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data               No operation

Example: HERE BNN Jump

Before Instruction
PC = address (HERE)

After Instruction
If NEGATIVE = 0; PC = address (Jump)
If NEGATIVE = 1; PC = address (HERE + 2)


BNOV                    Branch if Not Overflow
Syntax                  BNOV n
Operands                -128 ≤ n ≤ 127
Operation               If OVERFLOW bit is ‘0’
                        (PC) + 2 + 2n → PC


--- p811 ---
...........continued
BNOV                    Branch if Not Overflow
Syntax                  BNOV n
Status Affected         None
Encoding                         1110                           0101                      nnnn                nnnn
Description             If the OVERFLOW bit is ‘0’, then the program will branch. The two’s complement number ‘2n’ is
                        added to the PC. Since the PC will have incremented to fetch the next instruction, the new address
                        will be PC + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                               Q2                              Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data                Write to PC
         No operation                    No operation                      No operation               No operation

If No Jump:

              Q1                               Q2                              Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data               No operation

Example: HERE BNOV Jump

Before Instruction
PC = address (HERE)

After Instruction
If OVERFLOW = 0; PC = address (Jump)
If OVERFLOW = 1; PC = address (HERE + 2)


BNZ                     Branch if Not Zero
Syntax                  BNZ n
Operands                -128 ≤ n ≤ 127
Operation               If ZERO bit is ‘0’
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                         1110                           0001                      nnnn                nnnn
Description             If the ZERO bit is ‘0’, then the program will branch. The two’s complement number ‘2n’ is added to
                        the PC. Since the PC will have incremented to fetch the next instruction, the new address will be PC
                        + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                               Q2                              Q3                          Q4
            Decode                       Read literal ‘n’                  Process Data                Write to PC


--- p812 ---
         No operation                    No operation                      No operation              No operation

If No Jump:

              Q1                               Q2                              Q3                         Q4
            Decode                       Read literal ‘n’                  Process Data              No operation

Example: HERE BNZ Jump

Before Instruction
PC = address (HERE)

After Instruction
If ZERO = 0; PC = address (Jump)
If ZERO = 1; PC = address (HERE + 2)


BOV                     Branch if Overflow
Syntax                  BOV n
Operands                -128 ≤ n ≤ 127
Operation               If OVERFLOW bit is ‘1’
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                         1110                           0100                      nnnn              nnnn
Description             If the OVERFLOW bit is ‘1’, then the program will branch. The two’s complement number ‘2n’ is
                        added to the PC. Since the PC will have incremented to fetch the next instruction, the new address
                        will be PC + 2 + 2n. This instruction is then a two-cycle instruction.
Words                   1
Cycles                  1 (2)


Q Cycle Activity:

If Jump:

              Q1                               Q2                              Q3                         Q4
            Decode                       Read literal ‘n’                  Process Data               Write to PC
         No operation                    No operation                      No operation              No operation

If No Jump:

              Q1                               Q2                              Q3                         Q4
            Decode                       Read literal ‘n’                  Process Data              No operation

Example: HERE BOV Jump

Before Instruction
PC = address (HERE)

After Instruction
If OVERFLOW = 1; PC = address (Jump)
If OVERFLOW = 0; PC = address (HERE + 2)


--- p813 ---
BRA                     Unconditional Branch
Syntax                  BRA n
Operands                -1024 ≤ n ≤ 1023
Operation               (PC) + 2 + 2n → PC
Status Affected         None
Encoding                            1101                         0nnn                      nnnn                         nnnn
Description             The two’s complement number ‘2n’ is added to the PC. Since the PC will have incremented to fetch
                        the next instruction, the new address will be PC + 2 + 2n. This instruction is a two-cycle instruction.
Words                   1
Cycles                  2


Q Cycle Activity:
              Q1                                 Q2                               Q3                                  Q4
            Decode                        Read literal ‘n’                  Process Data                         Write to PC
         No operation                      No operation                     No operation                        No operation

Example: HERE BRA Jump

Before Instruction
PC = address (HERE)

After Instruction
PC = address (Jump)


BSF                     Bit Set f
Syntax                  BSF f, b {,a}
Operands                0 ≤ f ≤ 255
                        0≤b≤7
                        a ∈ [0, 1]
Operation               1 → f<b>
Status Affected         None
Encoding                            1000                         bbba                      ffff                         ffff
Description             Bit ‘b’ in register ‘f’ is set.
                        If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                        If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                        Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                        Indexed Literal Offset Mode for details.

Words                   1
Cycles                  1


Q Cycle Activity:
              Q1                                 Q2                               Q3                                  Q4
            Decode                       Read register ‘f’                  Process Data                      Write register ‘f’

Example: BSF FLAG_REG, 7, 1

Before Instruction
FLAG_REG = 0Ah


--- p814 ---
After Instruction
FLAG_REG = 8Ah


BTFSC                     Bit Test File, Skip if Clear
Syntax                    BTFSC f, b {,a}
Operands                  0 ≤ f ≤ 255
                          0≤b≤7
                          a ∈ [0, 1]
Operation                 Skip if (f<b>) = 0
Status Affected           None
Encoding                            1011                         bbba                        ffff                         ffff
Description               If bit ‘b’ in register ‘f’ is ‘0’, then the next instruction is skipped. If bit ‘b’ is ‘0’, then the next
                          instruction fetched during the current instruction execution is discarded and a NOP is executed
                          instead, making this a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation

If skip:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation
           No operation                    No operation                       No operation                        No operation

If skip and followed by two-word instruction:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation
           No operation                    No operation                       No operation                        No operation
           No operation                    No operation                       No operation                        No operation

If skip and followed by three-word instruction:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation
           No operation                    No operation                       No operation                        No operation
           No operation                    No operation                       No operation                        No operation
           No operation                    No operation                       No operation                        No operation


--- p815 ---
Example:
 HERE   BTFSC          FLAG, 1, 0
 FALSE:
 TRUE:


Before Instruction
PC = address (HERE)

After Instruction
If FLAG<1> = 0; PC = address (TRUE)
If FLAG<1> = 1; PC = address (FALSE)


BTFSS                     Bit Test File, Skip if Set
Syntax                    BTFSS f, b {,a}
Operands                  0 ≤ f ≤ 255
                          0≤b≤7
                          a ∈ [0, 1]
Operation                 Skip if (f<b>) = 1
Status Affected           None
Encoding                            1010                         bbba                        ffff                         ffff
Description               If bit ‘b’ in register ‘f’ is ‘1’, then the next instruction is skipped. If bit ‘b’ is ‘1’, then the next
                          instruction fetched during the current instruction execution is discarded and a NOP is executed
                          instead, making this a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation

If skip:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation
           No operation                    No operation                       No operation                        No operation

If skip and followed by two-word instruction:

               Q1                               Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                    Process Data                        No operation
           No operation                    No operation                       No operation                        No operation
           No operation                    No operation                       No operation                        No operation

If skip and followed by three-word instruction:


--- p816 ---
              Q1                              Q2                                  Q3                                  Q4
            Decode                      Read register ‘f’                   Process Data                        No operation
         No operation                    No operation                       No operation                        No operation
         No operation                    No operation                       No operation                        No operation
         No operation                    No operation                       No operation                        No operation

Example:
 HERE   BTFSS        FLAG, 1, 0
 FALSE:
 TRUE:


Before Instruction
PC = address (HERE)

After Instruction
If FLAG<1> = 0; PC = address (FALSE)
If FLAG<1> = 1; PC = address (TRUE)


BTG                     Bit Toggle f
Syntax                  BTG f, b {,a}
Operands                0 ≤ f ≤ 255
                        0≤b≤7
                        a ∈ [0, 1]
Operation               (f<b>) → f<b>
Status Affected         None
Encoding                          0111                          bbba                       ffff                         ffff
Description             Bit ‘b’ in data memory location ‘f’ is inverted.
                        If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                        If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                        Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                        Indexed Literal Offset Mode for details.

Words                   1
Cycles                  1


Q Cycle Activity:
              Q1                              Q2                                  Q3                                  Q4
            Decode                      Read register ‘f’                   Process Data                      Write register ‘f’

Example: BTG PORTC, 4, 0

Before Instruction
PORTC = 0111 0101 [75h]

After Instruction
PORTC = 0110 0101 [65h]


BZ                      Branch if Zero
Syntax                  BZ n
Operands                -128 ≤ n ≤ 127


--- p817 ---
...........continued
BZ                      Branch if Zero
Syntax                  BZ n
Operation               If ZERO bit is ‘1’
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                         1110                        0000                      nnnn                   nnnn
Description             If the ZERO bit is ‘1’, then the program will branch. The two’s complement number ‘2n’ is added to
                        the PC. Since the PC will have incremented to fetch the next instruction, the new address will be PC
                        + 2 + 2n. This instruction is then a two-cycle instruction.

Words                   1
Cycles                  1 (2)


Q Cycle Activity:
If Jump:

              Q1                             Q2                             Q3                             Q4
            Decode                    Read literal ‘n’                  Process Data                   Write to PC
         No operation                    No operation                   No operation                  No operation

If No Jump:

              Q1                             Q2                             Q3                             Q4
            Decode                    Read literal ‘n’                  Process Data                  No operation

Example: HERE BOV Jump

Before Instruction
PC = address (HERE)

After Instruction
If ZERO = 1; PC = address (Jump)
If ZERO = 0; PC = address (HERE + 2)


CALL                    Subroutine Call
Syntax                  CALL k {,s}
Operands                0 ≤ k ≤ 1048575
                        s ∈ [0, 1]
Operation               (PC) + 4 → TOS
                        k → PC<20:1>
                        If s = 1
                        (W) → WREG_CSHAD
                        (STATUS) → STATUS_CSHAD
                        (BSR) → BSR_CSHAD

Status Affected         None
Encoding                         1110                        110s                   k7kkk                    kkkk0
1st word (k<7:0>)                1111                       k19kkk                     kkkk                  kkkk8
2nd word (k<19:8>)
Description             Subroutine call of entire 2-Mbyte memory range. First, return address (PC + 4) is pushed onto the
                        return stack. If ‘s’ = 1, the WREG, STATUS and BSR registers are also pushed into their respective
                        shadow registers WREG_CSHAD, STATUS_CSHAD and BSR_CSHAD. If ‘s’ = 0, no update occurs
                        (default). Then, the 20-bit value ‘k’ is loaded into PC<20:1>. CALL is a two-cycle instruction.
Words                   2


--- p818 ---
...........continued
CALL                    Subroutine Call
Syntax                  CALL k {,s}
Cycles                  2


Q Cycle Activity:
              Q1                            Q2                              Q3                            Q4
                                                                                                 Read literal ‘k’<19:8>
            Decode                 Read literal ‘k’<7:0>              PUSH PC to stack               Write to PC

         No operation                   No operation                   No operation                  No operation

Example: HERE CALL THERE, 1
Before Instruction

PC = address (HERE)

After Instruction

PC = address (THERE)
TOS = address (HERE + 4)
WREG_CSHAD = (WREG)
BSR_CSHAD = (BSR)
STATUS_CSHAD = (STATUS)


CALLW                   Subroutine Call using WREG
Syntax                  CALLW
Operands                None
Operation               (PC) + 2 → TOS
                        (W) → PCL
                        (PCLATH) → PCH
                        (PCLATU) → PCU
Status Affected         None
Encoding                         0000                      0000                       0001                  0100
Description             First, the return address (PC + 2) is pushed onto the return stack. Next, the contents of W are
                        written to PCL; the existing value is discarded. Then, the contents of PCLATH and PCLATU are
                        latched onto PCH and PCU respectively. The second cycle is executed as a NOP instruction while the
                        new next instruction is fetched. Unlike CALL, there is no option to update W, STATUS or BSR.

Words                   1
Cycles                  2


Q Cycle Activity:
              Q1                            Q2                              Q3                            Q4
            Decode                      Read WREG                     PUSH PC to stack               No operation
         No operation                   No operation                   No operation                  No operation

Example: HERE CALLW
Before Instruction

PC = address (HERE)
PCLATH = 10h


--- p819 ---
PCLATU = 00h
W = 06h

After Instruction

PC = address 001006h
TOS = address (HERE + 2)
PCLATH = 10h
PCLATU = 00h
W = 06h


CLRF                 Clear f
Syntax               CLRF f {,a}
Operands             0 ≤ f ≤ 255
                     a ∈ [0, 1]
Operation            000h → f
                     1→Z
Status Affected      Z
Encoding                        0110                        101a                         ffff                        ffff
Description          Clears the contents of the specified register ‘f’.
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                           Q2                                  Q3                                  Q4
            Decode                  Read register ‘f’                     Process Data                     Write register ‘f’

Example: CLRF FLAG_REG, 1

Before Instruction
FLAG_REG = 5Ah

After Instruction
FLAG_REG = 00h


CLRWDT               Clear Watchdog Timer
Syntax               CLRWDT
Operands             None
Operation            000h → WDT
                     1 → TO
                     1 → PD
Status Affected      TO, PD
Encoding                        0000                        0000                         0000                        0100
Description          CLRWDT instruction resets the Watchdog Timer. It also resets the STATUS bits, and TO and PD are
                     set.
Words                1


--- p820 ---
...........continued
CLRWDT                 Clear Watchdog Timer
Syntax                 CLRWDT
Cycles                 1


Q Cycle Activity:
              Q1                               Q2                                Q3                                  Q4
            Decode                         No operation                    Process Data                        No operation

Example: CLRWDT

Before Instruction
WDT Counter = ?

After Instruction
WDT Counter = 00h
TO = 1
PD = 1


COMF                   Complement f
Syntax                 COMF f {,d {,a}}
Operands               0 ≤ f ≤ 255
                       d ∈ [0, 1]
                       a ∈ [0, 1]
Operation              (f) → dest
Status Affected        N, Z
Encoding                            0001                       11da                        ffff                        ffff
Description            The contents of register ‘f’ are complemented. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the
                       result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                               Q2                                Q3                                  Q4
            Decode                     Read register ‘f’                   Process Data                    Write to destination

Example: COMF REG0, 0, 0

Before Instruction
REG = 13h

After Instruction
REG = 13h
W = ECh


--- p821 ---
CPFSEQ                    Compare f with W, Skip if f = W
Syntax                    CPFSEQ f {,a}
Operands                  0 ≤ f ≤ 255
                          a ∈ [0, 1]
Operation                 (f) – (W), skip if (f) = (W)
                          (unsigned comparison)
Status Affected           None
Encoding                             0110                         001a                       ffff                         ffff
Description               Compares the contents of data memory location ‘f’ to the contents of W by performing an unsigned
                          subtraction. If the contents of ‘f’ are equal to the contents of WREG, then the fetched instruction is
                          discarded and a NOP is executed instead, making this a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation

If skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation
           No operation                     No operation                      No operation                        No operation

If skip and followed by two-word instruction:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation
           No operation                     No operation                      No operation                        No operation
           No operation                     No operation                      No operation                        No operation

If skip and followed by three-word instruction:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation
           No operation                     No operation                      No operation                        No operation
           No operation                     No operation                      No operation                        No operation
           No operation                     No operation                      No operation                        No operation

Example:
 HERE    CPFSEQ        REG, 0
 NEQUAL:
 EQUAL:


--- p822 ---
Before Instruction
PC = address (HERE)
W=?
REG = ?
After Instruction
If REG = W; PC = address (EQUAL)
If REG ≠ W; PC = address (NEQUAL)


CPFSGT                    Compare f with W, Skip if f > W
Syntax                    CPFSGT f {,a}
Operands                  0 ≤ f ≤ 255
                          a ∈ [0, 1]
Operation                 (f) – (W), skip if (f) > (W)
                          (unsigned comparison)
Status Affected           None
Encoding                             0110                         010a                       ffff                         ffff
Description               Compares the contents of data memory location ‘f’ to the contents of W by performing an
                          unsigned subtraction. If the contents of ‘f’ are greater than the contents of WREG, then the fetched
                          instruction is discarded and a NOP is executed instead, making this a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation

If skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation
           No operation                     No operation                      No operation                        No operation

If skip and followed by two-word instruction:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation
           No operation                     No operation                      No operation                        No operation
           No operation                     No operation                      No operation                        No operation

If skip and followed by three-word instruction:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation


--- p823 ---
           No operation                     No operation                      No operation                        No operation
           No operation                     No operation                      No operation                        No operation
           No operation                     No operation                      No operation                        No operation

Example:
 HERE   CPFSGT         REG, 0
 NGREATER:
 GREATER:


Before Instruction
PC = address (HERE)
W=?
REG = ?

After Instruction
If REG > W; PC = address (GREATER)
If REG ≤ W; PC = address (NGREATER)


CPFSLT                    Compare f with W, Skip if f < W
Syntax                    CPFSLT f {,a}
Operands                  0 ≤ f ≤ 255
                          a ∈ [0, 1]
Operation                 (f) – (W), skip if (f) < (W)
                          (unsigned comparison)
Status Affected           None
Encoding                             0110                         000a                       ffff                         ffff
Description               Compares the contents of data memory location ‘f’ to the contents of W by performing an unsigned
                          subtraction. If the contents of ‘f’ are less than the contents of WREG, then the fetched instruction is
                          discarded and a NOP is executed instead, making this a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation

If skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                      Read register ‘f’                   Process Data                        No operation
           No operation                     No operation                      No operation                        No operation

If skip and followed by two-word instruction:


--- p824 ---
              Q1                             Q2                              Q3                              Q4
            Decode                    Read register ‘f’                  Process Data                   No operation
         No operation                   No operation                     No operation                   No operation
         No operation                   No operation                     No operation                   No operation

If skip and followed by three-word instruction:

              Q1                             Q2                              Q3                              Q4
            Decode                    Read register ‘f’                  Process Data                   No operation
         No operation                   No operation                     No operation                   No operation
         No operation                   No operation                     No operation                   No operation
         No operation                   No operation                     No operation                   No operation

Example:
 HERE   CPFSLT       REG, 1
 NLESS:
 LESS:


Before Instruction
PC = address (HERE)
W=?
REG = ?

After Instruction
If REG < W; PC = address (LESS)
If REG ≥ W; PC = address (NLESS)


DAW                     Decimal Adjust W Register
Syntax                  DAW
Operands                None
Operation               If [(W<3:0>) > 9] or [DC = 1] then
                        (W<3:0>) + 6 → W<3:0>;
                        else
                        (W<3:0>) → W<3:0>;
                        If [(W<7:4>) + DC > 9] or [C = 1] then
                        (W<7:4>) + 6 + DC → W<7:4>;
                        else
                        (W<7:4>) + DC → W<7:4>

Status Affected         C
Encoding                         0000                         0000                      0000                   0111
Description             DAW adjusts the 8-bit value in W, resulting from the earlier addition of two variables (each in packed
                        BCD format) and produces a correct packed BCD result.
Words                   1
Cycles                  1


Q Cycle Activity:
              Q1                             Q2                              Q3                              Q4
            Decode                    Read register W                    Process Data                 Write register W

Example 1: DAW


--- p825 ---
Before Instruction
W = A5h
C=0
DC = 0

After Instruction
W = 05h
C=1
DC = 0

Example 2: DAW

Before Instruction
W = CEh
C=0
DC = 0

After Instruction
W = 34h
C=1
DC = 0


DECF                 Decrement f
Syntax               DECF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (f) – 1 → dest
Status Affected      C, DC, N, OV, Z
Encoding                       0000                           01da                        ffff                          ffff
Description          Decrement register ‘f’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the result is stored back in the
                     register ‘f’ (default).
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                   Q3                                  Q4
            Decode                    Read register ‘f’                    Process Data                    Write to destination

Example: DECF CNT, 1, 0

Before Instruction
CNT = 01h
Z=0

After Instruction
CNT = 00h
Z=1


--- p826 ---
DECFSZ                    Decrement f, Skip if 0
Syntax                    DECFSZ f {,d {,a}}
Operands                  0 ≤ f ≤ 255
                          d ∈ [0, 1]
                          a ∈ [0, 1]
Operation                 (f) – 1 → dest, skip if result = 0
Status Affected           None
Encoding                            0010                           11da                       ffff                         ffff
Description               The contents of register ‘f’ are decremented. If ‘d’ is ‘0’, the result is placed in W. If ‘d’ is ‘1’, the result
                          is placed back in register ‘f’ (default).
                          If the result is ‘0’, the next instruction, which is already fetched, is discarded and a NOP is executed
                          instead, making it a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination

If skip:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation

If skip and followed by two-word instruction:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation
           No operation                    No operation                        No operation                        No operation

If skip and followed by three-word instruction:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation
           No operation                    No operation                        No operation                        No operation
           No operation                    No operation                        No operation                        No operation


--- p827 ---
Example:
 HERE   DECFSZ         CNT, 1, 1
        GOTO           LOOP
 CONTINUE


Before Instruction
CNT = ?
PC = address (HERE)

After Instruction
CNT = CNT – 1
If CNT = 0; PC = address (CONTINUE)
If CNT ≠ 0; PC = address (HERE + 2)


DCFSNZ                    Decrement f, Skip if not 0
Syntax                    DCFSNZ f {,d {,a}}
Operands                  0 ≤ f ≤ 255
                          d ∈ [0, 1]
                          a ∈ [0, 1]
Operation                 (f) – 1 → dest, skip if result ≠ 0
Status Affected           None
Encoding                            0100                           11da                       ffff                         ffff
Description               The contents of register ‘f’ are decremented. If ‘d’ is ‘0’, the result is placed in W. If ‘d’ is ‘1’, the result
                          is placed back in register ‘f’ (default).
                          If the result is not ‘0’, the next instruction, which is already fetched, is discarded and a NOP is
                          executed instead, making it a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination

If skip:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation

If skip and followed by two-word instruction:

               Q1                               Q2                                  Q3                                   Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation


--- p828 ---
         No operation                    No operation                     No operation             No operation

If skip and followed by three-word instruction:

              Q1                             Q2                               Q3                         Q4
            Decode                     Read register ‘f’                  Process Data          Write to destination
         No operation                    No operation                     No operation             No operation
         No operation                    No operation                     No operation             No operation
         No operation                    No operation                     No operation             No operation

Example:
 HERE   DCFSNZ       TEMP, 1, 0
 ZERO:
 NZERO:


Before Instruction
TEMP = ?
PC = address (HERE)

After Instruction
TEMP = TEMP – 1
If TEMP = 0; PC = address (ZER0)
If TEMP ≠ 0; PC = address (NZERO)


GOTO                    Unconditional Branch
Syntax                  GOTO k
Operands                0 ≤ k ≤ 1048575
Operation               k → PC<20:1>
Status Affected         None
Encoding                          1110                         1111                  k7kkk                 kkkk0
1st word (k<7:0>)                 1111                        k19kkk                     kkkk              kkkk8
2nd word (k<19:8>)
Description             GOTO allows an unconditional branch anywhere within entire 2-Mbyte memory range. The 20-bit
                        value ‘k’ is loaded into PC<20:1>. GOTO is always a two-cycle instruction.

Words                   2
Cycles                  2


Q Cycle Activity:
              Q1                             Q2                               Q3                         Q4
                                                                                                Read literal ‘k’<19:8>
            Decode                 Read literal ‘k’<7:0>                  No operation              Write to PC

         No operation                    No operation                     No operation             No operation

Example: HERE GOTO THERE
Before Instruction

PC = address (HERE)

After Instruction

PC = address (THERE)


--- p829 ---
INCF                 Increment f
Syntax               INCF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (f) + 1 → dest
Status Affected      C, DC, N, OV, Z
Encoding                       0010                           10da                        ffff                         ffff
Description          The contents of register ‘f’ are incremented. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the result
                     is stored back in the register ‘f’ (default).
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                  Q3                                  Q4
            Decode                    Read register ‘f’                   Process Data                     Write to destination

Example: INCF CNT, 1, 0

Before Instruction
CNT = FFh
Z=0
C=?
DC = ?

After Instruction
CNT = 00h
Z=1
C=1
DC = 1


INCFSZ               Increment f, Skip if 0
Syntax               INCFSZ f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (f) + 1 → dest, skip if result = 0
Status Affected      None
Encoding                       0011                           11da                        ffff                         ffff
Description          The contents of register ‘f’ are incremented. If ‘d’ is ‘0’, the result is placed in W. If ‘d’ is ‘1’, the result
                     is placed back in register ‘f’ (default).
                     If the result is ‘0’, the next instruction, which is already fetched, is discarded and a NOP is executed
                     instead, making it a two-cycle instruction.
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.


--- p830 ---
...........continued
INCFSZ                    Increment f, Skip if 0
Syntax                    INCFSZ f {,d {,a}}
Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                             Q2                               Q3                             Q4
              Decode                    Read register ‘f’                  Process Data              Write to destination

If skip:

               Q1                             Q2                               Q3                             Q4
              Decode                    Read register ‘f’                  Process Data              Write to destination
           No operation                  No operation                      No operation                  No operation

If skip and followed by two-word instruction:

               Q1                             Q2                               Q3                             Q4
              Decode                    Read register ‘f’                  Process Data              Write to destination
           No operation                  No operation                      No operation                  No operation
           No operation                  No operation                      No operation                  No operation

If skip and followed by three-word instruction:

               Q1                             Q2                               Q3                             Q4
              Decode                    Read register ‘f’                  Process Data              Write to destination
           No operation                  No operation                      No operation                  No operation
           No operation                  No operation                      No operation                  No operation
           No operation                  No operation                      No operation                  No operation

Example:
 HERE   INCFSZ         CNT, 1, 0
 NZERO:
 ZERO:


Before Instruction
CNT = ?
PC = address (HERE)

After Instruction
CNT = CNT + 1
If CNT = 0; PC = address (ZERO)
If CNT ≠ 0; PC = address (NZERO)


--- p831 ---
INFSNZ                    Increment f, Skip if not 0
Syntax                    INFSNZ f {,d {,a}}
Operands                  0 ≤ f ≤ 255
                          d ∈ [0, 1]
                          a ∈ [0, 1]
Operation                 (f) + 1 → dest, skip if result ≠ 0
Status Affected           None
Encoding                            0100                          10da                        ffff                          ffff
Description               The contents of register ‘f’ are incremented. If ‘d’ is ‘0’, the result is placed in W. If ‘d’ is ‘1’, the result
                          is placed back in register ‘f’ (default).
                          If the result is not ‘0’, the next instruction, which is already fetched, is discarded and a NOP is
                          executed instead, making it a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                                Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination

If skip:

               Q1                                Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation

If skip and followed by two-word instruction:

               Q1                                Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation
           No operation                    No operation                        No operation                        No operation

If skip and followed by three-word instruction:

               Q1                                Q2                                  Q3                                  Q4
              Decode                     Read register ‘f’                     Process Data                    Write to destination
           No operation                    No operation                        No operation                        No operation
           No operation                    No operation                        No operation                        No operation
           No operation                    No operation                        No operation                        No operation

Example:
 HERE   INFSNZ         REG, 1, 0
 ZERO:
 NZERO:


--- p832 ---
Before Instruction
REG = ?
PC = address (HERE)

After Instruction
REG = REG + 1
If REG = 0; PC = address (ZER0)
If REG ≠ 0; PC = address (NZERO)


IORLW                Inclusive OR Literal with W
Syntax               IORLW k
Operands             0 ≤ k ≤ 255
Operation            (W) .OR. k → W
Status Affected      N, Z
Encoding                        0000                          1001                        kkkk                          kkkk
Description          The contents of W are ORed with the 8-bit literal ‘k’. The result is placed in W.
Words                1
Cycles               1


Q Cycle Activity:
              Q1                             Q2                                  Q3                                   Q4
            Decode                     Read literal ‘k’                    Process Data                          Write to W

Example: IORLW 35h

Before Instruction
W = 9Ah

After Instruction
W = BFh


IORWF                Inclusive OR W with f
Syntax               IORWF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (W) .OR. (f) → dest
Status Affected      N, Z
Encoding                        0001                          00da                        ffff                          ffff
Description          Inclusive OR W with register ‘f’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the result is stored back
                     in the register ‘f’ (default).
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:


--- p833 ---
              Q1                               Q2                                 Q3                            Q4
            Decode                       Read register ‘f’                  Process Data               Write to destination

Example: IORWF RESULT, 0, 1

Before Instruction
RESULT = 13h
W = 91h

After Instruction
RESULT = 13h
W = 93h


LFSR                    Load FSR
Syntax                  LFSR fn, k
Operands                0 ≤ fn ≤ 2
                        0 ≤ k ≤ 16383
Operation               k → FSRfn
Status Affected         None
Encoding                             1110                        1110                     00fnfn                k13kkk10
                                     1111                        00k9k                        kkkk                kkkk0
Description             The 14-bit literal ‘k’ is loaded into the File Select Register ‘fn’
Words                   2
Cycles                  2


Q Cycle Activity:
              Q1                               Q2                                 Q3                            Q4
                                                                                                     Write literal ‘k’<13:10> to
            Decode                    Read literal ‘k’<13:10>               Process Data
                                                                                                          FSRfn<13:10>
                                                                                                      Write literal ‘k’<9:0> to
         No operation                  Read literal ‘k’<9:0>                No operation
                                                                                                           FSRfn<9:0>

Example: LFSR 2, 3ABh

Before Instruction
FSR2H = ?
FSR2L = ?

After Instruction
FSR2H = 03h
FSR2L = ABh


MOVF                    Move f
Syntax                  MOVF f {,d {,a}}
Operands                0 ≤ f ≤ 255
                        d ∈ [0, 1]
                        a ∈ [0, 1]
Operation               (f) → dest
Status Affected         N, Z
Encoding                             0101                        00da                         ffff                 ffff


--- p834 ---
...........continued
MOVF                   Move f
Syntax                 MOVF f {,d {,a}}
Description            The contents of register ‘f’ are moved to a destination. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’,
                       the result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                              Q2                                  Q3                                  Q4
            Decode                     Read register ‘f’                    Process Data                    Write to destination

Example: MOVF REG, 0, 0

Before Instruction
REG = 22h
W = FFh

After Instruction
REG = 22h
W = 22h


MOVFF                  Move f to f
Syntax                 MOVFF fs, fd
Operands               0 ≤ fs ≤ 4095
                       0 ≤ fd ≤ 4095
Operation              (fs) → fd
Status Affected        None
Encoding                           1100                       fsfsfsfs                   fsfsfsfs                     fsfsfsfs
                                   1111                       fdfdfdfd                   fdfdfdfd                     fdfdfdfd
Description            The contents of source register ‘fs’ are moved to destination register ‘fd’. Location of source ‘fs’ can
                       be anywhere in the 4096-byte data space (000h to FFFh) and location of destination ‘fd’ can also be
                       anywhere from 000h to FFFh.
                       MOVFF is particularly useful for transferring a data memory location to a peripheral register (such
                       as the transmit buffer or an I/O port).
                       The MOVFF instruction cannot use the PCL, TOSU, TOSH or TOSL as the destination register.
                       Note:
                       MOVFF has curtailed the source and destination range to the lower 4 Kbyte space of memory (Banks
                       1 through 15). For everything else, use MOVFFL.

Words                  2
Cycles                 2


Q Cycle Activity:
              Q1                              Q2                                  Q3                                  Q4
            Decode                     Read register ‘fs’                   Process Data                        No operation


--- p835 ---
                                    No operation
            Decode                                                      No operation               Write register ‘fd’
                                   No dummy read

Example: MOVFF REG1, REG2

Before Instruction
Address of REG1 = 100h
Address of REG2 = 200h
REG1 = 33h
REG2 = 11h

After Instruction
Address of REG1 = 100h
Address of REG2 = 200h
REG1 = 33h
REG2 = 33h


MOVFFL               Move f to f (Long Range)
Syntax               MOVFFL fs, fd
Operands             0 ≤ fs ≤ 16383
                     0 ≤ fd ≤ 16383
Operation            (fs) → fd
Status Affected      None
Encoding                         0000                        0000                      0110                fsfsfsfs
                                 1111                      fsfsfsfs               fsfsfsfs                 fsfsfdfd
                                 1111                      fdfdfdfd               fdfdfdfd                 fdfdfdfd
Description          The contents of source register ‘fs’ are moved to destination register ‘fd’. Location of source ‘fs’
                     can be anywhere in the 16 Kbyte data space (0000h to 3FFFh) and location of destination ‘fd’ can
                     also be anywhere from 0000h to 3FFFh. Either source or destination can be W (a useful special
                     situation).
                     MOVFFL is particularly useful for transferring a data memory location to a peripheral register (such
                     as the transmit buffer or an I/O port).
                     The MOVFFL instruction cannot use the PCL, TOSU, TOSH or TOSL as the destination register.

Words                3
Cycles               3


Q Cycle Activity:
              Q1                            Q2                              Q3                            Q4
            Decode                      No operation                    No operation                 No operation
            Decode                  Read register ‘fs’                  Process Data                 No operation
                                    No operation
            Decode                                                      No operation               Write register ‘fd’
                                   No dummy read

Example: MOVFFL 2000h, 200Ah

Before Instruction
Contents of 2000h = 33h
Contents of 200Ah = 11h

After Instruction
Contents of 2000h = 33h
Contents of 200Ah = 33h


--- p836 ---
MOVLB                Move Literal to BSR
Syntax               MOVLB k
Operands             0 ≤ k ≤ 63
Operation            k → BSR
Status Affected      None
Encoding                       0000                           0001                     00kk                  kkkk
Description          The 6-bit literal ‘k’ is loaded into the Bank Select Register (BSR<5:0>). The value of BSR<7:6> always
                     remains ‘0’.
Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                              Q3                             Q4
            Decode                    Read literal ‘k’                  Process Data                  Write to BSR

Example: MOVLB 5

Before Instruction
BSR = 02h

After Instruction
BSR = 05h


MOVLW                Move Literal to W
Syntax               MOVLW k
Operands             0 ≤ k ≤ 255
Operation            k→W
Status Affected      None
Encoding                       0000                           1110                     kkkk                  kkkk
Description          The 8-bit literal ‘k’ is loaded into W
Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                              Q3                             Q4
            Decode                    Read literal ‘k’                  Process Data                   Write to W

Example: MOVLW 5Ah

Before Instruction
W=?

After Instruction
W = 5Ah


--- p837 ---
MOVWF                Move W to f
Syntax               MOVWF f {,a}
Operands             0 ≤ f ≤ 255
                     a ∈ [0, 1]
Operation            (W) → f
Status Affected      None
Encoding                       0110                          111a                       ffff                         ffff
Description          Move data from W to register ‘f’. Location ‘f’ can be anywhere in the 256-byte bank.
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                 Q3                                  Q4
            Decode                       Read W                          Process Data                      Write register ‘f’

Example: MOVWF REG, 0

Before Instruction
W = 4Fh
REG = FFh

After Instruction
W = 4Fh
REG = 4Fh


MULLW                Multiply literal with W
Syntax               MULLW k
Operands             0 ≤ k ≤ 255
Operation            (W) x k → PRODH:PRODL
Status Affected      None
Encoding                       0000                          1101                       kkkk                         kkkk
Description          An unsigned multiplication is carried out between the contents of W and the 8-bit literal ‘k’. The
                     16-bit result is placed in the PRODH:PRODL register pair. PRODH contains the high byte. W is
                     unchanged.
                     None of the Status flags are affected. Note that neither overflow nor carry is possible in this
                     operation. A zero result is possible but not detected.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                 Q3                                  Q4
            Decode                    Read literal ‘k’                   Process Data              Write registers PRODH:PRODL

Example: MULLW 0C4h


--- p838 ---
Before Instruction
W = E2h
PRODH = ?
PRODL = ?
After Instruction
W = E2h
PRODH = ADh
PRODL = 08h


MULWF                Multiply W with f
Syntax               MULWF f {,a}
Operands             0 ≤ f ≤ 255
                     a ∈ [0, 1]
Operation            (W) x (f) → PRODH:PRODL
Status Affected      None
Encoding                        0000                        001a                        ffff                         ffff
Description          An unsigned multiplication is carried out between the contents of W and the register file location ‘f’.
                     The 16-bit result is placed in the PRODH:PRODL register pair. PRODH contains the high byte. Both
                     W and ‘f’ are unchanged.
                     None of the Status flags are affected. Note that neither overflow nor carry is possible in this
                     operation. A zero result is possible but not detected.
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                           Q2                                  Q3                                  Q4
            Decode                  Read register ‘f’                    Process Data              Write registers PRODH:PRODL

Example: MULWF REG, 1

Before Instruction
W = C4h
REG = B5h
PRODH = ?
PRODL = ?
After Instruction
W = C4h
REG = B5h
PRODH = 8Ah
PRODL = 94h


NEGF                 Negate f
Syntax               NEGF f {,a}
Operands             0 ≤ f ≤ 255
                     a ∈ [0, 1]


--- p839 ---
...........continued
NEGF                   Negate f
Syntax                 NEGF f {,a}
Operation              (f) + 1 → f
Status Affected        N, OV, C, DC, Z
Encoding                             0110                       110a                      ffff                         ffff
Description            Location ‘f’ is negated using two’s complement. The result is placed in the data memory location ‘f’.
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                                Q2                               Q3                                  Q4
            Decode                      Read register ‘f’                  Process Data                      Write register ‘f’

Example: NEGF REG, 1

Before Instruction
REG = 0011 1010 [3Ah]

After Instruction
REG = 1100 0110 [C6h]


NOP                    No Operation
Syntax                 NOP
Operands               None
Operation              No operation
Status Affected        None
Encoding                             0000                       0000                      0000                         0000
                                     1111                       xxxx                      xxxx                         xxxx
Description            No operation
Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                                Q2                               Q3                                  Q4
            Decode                          No operation                   No operation                        No operation

Example: None.


POP                    Pop Top of Return Stack
Syntax                 POP
Operands               None
Operation              (TOS) → bit bucket


--- p840 ---
...........continued
POP                     Pop Top of Return Stack
Syntax                  POP
Status Affected         None
Encoding                         0000                       0000                      0000                  0110
Description             The TOS value is pulled off the return stack and is discarded. The TOS value then becomes the
                        previous value that was pushed onto the return stack. This instruction is provided to enable the
                        user to properly manage the return stack to incorporate a software stack (see the PUSH instruction
                        description).

Words                   1
Cycles                  1


Q Cycle Activity:
               Q1                            Q2                             Q3                            Q4
              Decode                     No operation                  POP TOS value                 No operation

Example:
       POP
       GOTO       NEW


Before Instruction
TOS = 0031A2h
Stack (1 level down) = 014332h

After Instruction
TOS = 014332h
PC = address (NEW)


PUSH                    Push Top of Return Stack
Syntax                  PUSH
Operands                None
Operation               (PC) + 2 → TOS
Status Affected         None
Encoding                         0000                       0000                      0000                  0101
Description             The PC + 2 is pushed onto the top of the return stack. The previous TOS value is pushed down
                        on the stack. This instruction allows implementing a software stack by modifying TOS and then
                        pushing it onto the return stack (see the POP instruction description).

Words                   1
Cycles                  1


Q Cycle Activity:
               Q1                            Q2                             Q3                            Q4
                                 PUSH PC + 2 onto return
              Decode                                                   No operation                  No operation
                                         stack

Example: PUSH

Before Instruction
TOS = 00345Ah
PC = 000124h


--- p841 ---
After Instruction
TOS = 000126h
PC = 000126h
Stack (1 level down) = 00345Ah


RCALL                   Relative Call
Syntax                  RCALL n
Operands                -1024 ≤ n ≤ 1023
Operation               (PC) + 2 → TOS
                        (PC) + 2 + 2n → PC
Status Affected         None
Encoding                          1101                         1nnn                     nnnn                  nnnn
Description             Subroutine call with a jump up to 1K from the current location. First, return address (PC + 2) is
                        pushed onto the stack. Then, add the two’s complement number ‘2n’ to the PC. Since the PC will
                        have incremented to fetch the next instruction, the new address will be PC + 2 + 2n. This instruction
                        is a two-cycle instruction.

Words                   1
Cycles                  2


Q Cycle Activity:
              Q1                               Q2                            Q3                             Q4
                                         Read literal ‘n’
            Decode                                                       Process Data                   Write to PC
                                        PUSH PC to stack
         No operation                    No operation                    No operation                 No operation

Example: HERE RCALL Jump

Before Instruction
PC = address (HERE)

After Instruction
PC = address (Jump)
TOS = address (HERE + 2)


RESET                   Reset
Syntax                  RESET
Operands                None
Operation               Reset all registers and flags that are affected by a MCLR Reset
Status Affected         All
Encoding                          0000                         0000                     1111                  1111
Description             This instruction provides a way to execute a MCLR Reset by software
Words                   1
Cycles                  1


Q Cycle Activity:
              Q1                               Q2                            Q3                             Q4
            Decode                         Start Reset                   No operation                 No operation


--- p842 ---
Example: RESET

Before Instruction
All Registers = ?
All Flags = ?
After Instruction
All Registers = Reset Value
All Flags = Reset Value


RETFIE                  Return from Interrupt
Syntax                  RETFIE {s}
Operands                s ∈ [0, 1]
Operation               (TOS) → PC
                        If s = 1, context is restored into WREG, STATUS, BSR, FSR0H, FSR0L, FSR1H, FSR1L, FSR2H, FSR2L,
                        PRODH, PRODL, PCLATH and PCLATU registers from the corresponding shadow registers.
                        If s = 0, there is no change in status of any register.
                        PCLATU, PCLATH are unchanged.

Status Affected         STAT bits in INTCONx register
Encoding                             0000                      0000                      0001                000s
Description             Return from interrupt. Stack is popped and Top-of-Stack (TOS) is loaded into the PC. Interrupts are
                        enabled by setting either the high- or low-priority Global Interrupt Enable bit.
                        If ‘s’ = 1, the contents of the shadow registers WREG_SHAD, STATUS_SHAD, BSR_SHAD, FSR0H_SHAD,
                        FSR0L_SHAD, FSR1H_SHAD, FSR1L_SHAD, FSR2H_SHAD, FSR2L_SHAD, PRODH_SHAD, PRODL_SHAD,
                        PCLATH_SHAD and PCLATU_SHAD are loaded into corresponding registers. There are two sets of
                        shadow registers, main context and low context. The set retrieved on RETFIE instruction execution
                        depends on what the state of operation of the CPU was when RETFIE was executed.
                        If ‘s’ = 0, no update of these registers occurs (default).
                        The upper and high address latches (PCLATU/H) remain unchanged.

Words                   1
Cycles                  2


Q Cycle Activity:
              Q1                                Q2                                Q3                       Q4
            Decode                          No operation                  Process Data             POP PC from stack
         No operation                       No operation                  No operation                No operation

Example: RETFIE 1

After Instruction
PC = (TOS)
WREG = (WREG_SHAD)
BSR = (BSR_SHAD)
STATUS = (STATUS_SHAD)
FSR0H/L = (FSR0H/L_SHAD)
FSR1H/L = (FSR1H/L_SHAD)
FSR2H/L = (FSR2H/L_SHAD)
PRODH/L = (PRODH/L_SHAD)
PCLATH/U = (PCLATH/U_SHAD)


--- p843 ---
RETLW                    Return Literal to W
Syntax                   RETLW k
Operands                 0 ≤ k ≤ 255
Operation                k→W
                         (TOS) → PC
                         PCLATU, PCLATH are unchanged
Status Affected          None
Encoding                              0000                          1100                      kkkk               kkkk
Description              W is loaded with the 8-bit literal ‘k’. The Program Counter is loaded from the top of the stack (the
                         return address). The upper and high address latches (PCLATU/H) remain unchanged.
Words                    1
Cycles                   2


Q Cycle Activity:
                Q1                                 Q2                              Q3                          Q4
                                                                                                      POP PC from stack
               Decode                        Read literal ‘k’                  Process Data
                                                                                                         Write to W
         No operation                        No operation                      No operation              No operation

Example:
        CALL     TABLE   ; W contains table offset value
 BACK                    ; W now has table value (after RETLW)
     :
     :
 TABLE
     ADDWF       PCL     ; W = offset
     RETLW       k0      ; Begin table
     RETLW       k1      ;
     :
     :
     RETLW       kn      ; End of table


Before Instruction
W = 07h

After Instruction
W = value of kn


RETURN                   Return from Subroutine
Syntax                   RETURN {s}
Operands                 s ∈ [0, 1]
Operation                (TOS) → PC
                         If s = 1
                         (WREG_CSHAD) → WREG
                         (STATUS_CSHAD) → STATUS
                         (BSR_CSHAD) → BSR
                         PCLATU, PCLATH are unchanged

Status Affected          None
Encoding                              0000                          0000                      0001               001s
Description              Return from subroutine. The stack is popped and the top of the stack (TOS) is loaded into the
                         Program Counter. If ‘s’ = 1, the contents of the shadow registers WREG_CSHAD, STATUS_CSHAD and
                         BSR_CSHAD, are loaded into their corresponding registers. If ‘s’ = 0, no update of these registers
                         occurs (default). The upper and high address latches (PCLATU/H) remain unchanged.

Words                    1


--- p844 ---
...........continued
RETURN                  Return from Subroutine
Syntax                  RETURN {s}
Cycles                  2


Q Cycle Activity:
              Q1                              Q2                                  Q3                                  Q4
            Decode                       No operation                       Process Data                     POP PC from stack
         No operation                    No operation                       No operation                        No operation

Example: RETURN 1

After Instruction
PC = (TOS)
WREG = (WREG_CSHAD)
BSR = (BSR_CSHAD)
STATUS = (STATUS_CSHAD)


RLCF                    Rotate Left f through Carry
Syntax                  RLCF f {,d {,a}}
Operands                0 ≤ f ≤ 255
                        d ∈ [0, 1]
                        a ∈ [0, 1]
Operation               (f<n>) → dest<n+1>
                        (f<7>) → C
                        (C) → dest<0>
Status Affected         C, N, Z
Encoding                          0011                         01da                        ffff                         ffff
Description             The contents of register ‘f’ are rotated one bit to the left through the Carry flag. If ‘d’ is ‘0’, the result
                        is stored in W. If ‘d’ is ‘1’, the result is stored back in the register ‘f’ (default).
                        If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                        If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                        Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                        Indexed Literal Offset Mode for details.

                                                                  C           register f


Words                   1
Cycles                  1


Q Cycle Activity:
              Q1                              Q2                                  Q3                                  Q4
            Decode                     Read register ‘f’                    Process Data                    Write to destination

Example: RLCF REG, 0, 0

Before Instruction
REG = 1110 0110 [E6h]
W=?
C=0


--- p845 ---
After Instruction
REG = 1110 0110 [E6h]
W = 1100 1100 [CCh]
C=1


RLNCF                Rotate Left f (No Carry)
Syntax               RLNCF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (f<n>) → dest<n+1>
                     (f<7>) → dest<0>
Status Affected      N, Z
Encoding                       0100                          01da                         ffff                         ffff
Description          The contents of register ‘f’ are rotated one bit to the left. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is
                     ‘1’, the result is stored back in the register ‘f’ (default).
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

                                                                       register f


Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                  Q3                                   Q4
            Decode                  Read register ‘f’                      Process Data                    Write to destination

Example: RLNCF REG, 1, 0

Before Instruction
REG = 1010 1011 [ABh]

After Instruction
REG = 0101 0111 [57h]


RRCF                 Rotate Right f through Carry
Syntax               RRCF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (f<n>) → dest<n-1>
                     (f<0>) → C
                     (C) → dest<7>
Status Affected      C, N, Z
Encoding                       0011                          00da                         ffff                         ffff


--- p846 ---
...........continued
RRCF                   Rotate Right f through Carry
Syntax                 RRCF f {,d {,a}}
Description            The contents of register ‘f’ are rotated one bit to the right through the Carry flag. If ‘d’ is ‘0’, the
                       result is stored in W. If ‘d’ is ‘1’, the result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

                                                                 C            register f


Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                              Q2                                  Q3                                   Q4
            Decode                    Read register ‘f’                     Process Data                     Write to destination

Example: RRCF REG, 0, 0

Before Instruction
REG = 1110 0110 [E6h]
W=?
C=0

After Instruction
REG = 1110 0110 [E6h]
W = 0111 0011 [73h]
C=0


RRNCF                  Rotate Right f (No Carry)
Syntax                 RRNCF f {,d {,a}}
Operands               0 ≤ f ≤ 255
                       d ∈ [0, 1]
                       a ∈ [0, 1]
Operation              (f<n>) → dest<n-1>
                       (f<0>) → dest<7>
Status Affected        N, Z
Encoding                         0100                          00da                         ffff                         ffff
Description            The contents of register ‘f’ are rotated one bit to the right. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is
                       ‘1’, the result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

                                                                           register f


Words                  1
Cycles                 1


--- p847 ---
Q Cycle Activity:
              Q1                           Q2                                  Q3                                  Q4
            Decode                  Read register ‘f’                    Process Data                    Write to destination

Example 1: RRNCF REG, 1, 0

Before Instruction
REG = 1101 0111 [D7h]

After Instruction
REG = 1110 1011 [EBh]

Example 2: RRNCF REG, 0, 0

Before Instruction
REG = 1101 0111 [D7h]
W=?

After Instruction
REG = 1101 0111 [D7h]
W = 1110 1011 [EBh]


SETF                 Set f
Syntax               SETF f {,a}
Operands             0 ≤ f ≤ 255
                     a ∈ [0, 1]
Operation            FFh → f
Status Affected      None
Encoding                       0110                         100a                        ffff                         ffff
Description          The contents of the specified register ‘f’ are set to FFh.
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                           Q2                                  Q3                                  Q4
            Decode                  Read register ‘f’                    Process Data                      Write register ‘f’

Example: SETF REG, 1

Before Instruction
REG = 5Ah

After Instruction
REG = FFh


--- p848 ---
SLEEP                Enter Sleep Mode
Syntax               SLEEP
Operands             None
Operation            00h → WDT
                     1 → TO
                     0 → PD
Status Affected      TO, PD
Encoding                       0000                            0000                      0000                     0011
Description          The Power-down Status (PD) bit is cleared. The Time-Out Status TO) bit is set. Watchdog Timer is
                     cleared. The processor is put into Sleep mode with the oscillator stopped.
Words                1
Cycles               1


Q Cycle Activity:
              Q1                              Q2                              Q3                                Q4
            Decode                      No operation                      Process Data                      Go to Sleep

Example: SLEEP

Before Instruction
TO = ?
PD = ?

After Instruction
TO = 1 †
PD = 0

† If WDT causes wake-up, this bit is cleared.


SUBFSR               Subtract Literal from FSR
Syntax               SUBFSR fn, k
Operands             0 ≤ k ≤ 63
                     fn ∈ [0, 1, 2]
Operation            (FSRfn) – k → FSRfn
Status Affected      None
Encoding                       1110                            1001                  fnfnkk                       kkkk
Description          The 6-bit literal ‘k’ is subtracted from the contents of the FSR specified by ‘fn’
Words                1
Cycles               1


Q Cycle Activity:
              Q1                              Q2                              Q3                                Q4
            Decode                      Read literal ‘k’                  Process Data                      Write to FSR

Example: SUBFSR 2, 23h

Before Instruction
FSR2 = 03FFh

After Instruction
FSR2 = 03DCh


--- p849 ---
SUBFWB                 Subtract f from W with Borrow
Syntax                 SUBFWB f {,d {,a}}
Operands               0 ≤ f ≤ 255
                       d ∈ [0, 1]
                       a ∈ [0, 1]
Operation              (W) – (f) – (C) → dest
Status Affected        N, OV, C, DC, Z
Encoding                         0101                         01da                        ffff                         ffff
Description            Subtract register ‘f’ and Carry flag (Borrow) from W (two’s complement method). If ‘d’ is ‘0’, the result
                       is stored in W. If ‘d’ is ‘1’, the result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                                Q2                               Q3                                  Q4
            Decode                    Read register ‘f’                    Process Data                    Write to destination

Example 1: SUBFWB REG, 1, 0

Before Instruction
REG = 03h
W = 02h
C=1

After Instruction
REG = FFh (two’s complement)
W = 02h
C=0
Z=0
N = 1 (result is negative)

Example 2: SUBFWB REG, 0, 0

Before Instruction
REG = 02h
W = 05h
C=1

After Instruction
REG = 02h
W = 03h
C=1
Z=0
N = 0 (result is positive)

Example 3: SUBFWB REG, 1, 0


--- p850 ---
Before Instruction
REG = 01h
W = 02h
C=0

After Instruction
REG = 00h
W = 02h
C=1
Z = 1 (result is zero)
N=0


SUBLW                    Subtract W from Literal
Syntax                   SUBLW k
Operands                 0 ≤ k ≤ 255
Operation                k – (W) → W
Status Affected          N, OV, C, DC, Z
Encoding                           0000                           1000                      kkkk           kkkk
Description              W is subtracted from the 8-bit literal ‘k’. The result is placed in W.
Words                    1
Cycles                   1


Q Cycle Activity:
              Q1                                 Q2                              Q3                      Q4
            Decode                         Read literal ‘k’                  Process Data             Write to W

Example 1: SUBLW 02h

Before Instruction
W = 01h
C=?
After Instruction
W = 01h
C = 1 (result is positive)
Z=0
N=0

Example 2: SUBLW 02h

Before Instruction
W = 02h
C=?

After Instruction
W = 00h
C=1
Z = 1 (result is zero)
N=0

Example 3: SUBLW 02h


--- p851 ---
Before Instruction
W = 03h
C=?

After Instruction
W = FFh (two’s complement)
C=0
Z=0
N = 1 (result is negative)


SUBWF                Subtract W from f
Syntax               SUBWF f {,d {,a}}
Operands             0 ≤ f ≤ 255
                     d ∈ [0, 1]
                     a ∈ [0, 1]
Operation            (f) – (W) → dest
Status Affected      N, OV, C, DC, Z
Encoding                       0101                         11da                        ffff                         ffff
Description          Subtract W from register ‘f’ (two’s complement method). If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is
                     ‘1’, the result is stored back in the register ‘f’ (default).
                     If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                     If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                     Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                     Indexed Literal Offset Mode for details.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                           Q2                                  Q3                                  Q4
            Decode                  Read register ‘f’                    Process Data                    Write to destination

Example 1: SUBWF REG, 1, 0

Before Instruction
REG = 03h
W = 02h
C=?

After Instruction
REG = 01h (two’s complement)
W = 02h
C = 1 (result is positive)
Z=0
N=0

Example 2: SUBWF REG, 0, 0

Before Instruction
REG = 02h
W = 02h
C=?


--- p852 ---
After Instruction
REG = 02h
W = 00h
C=1
Z = 1 (result is zero)
N=0

Example 3: SUBWF REG, 1, 0

Before Instruction
REG = 01h
W = 02h
C=?

After Instruction
REG = FFh (two’s complement)
W = 02h
C=0
Z=0
N = 1 (result is negative)


SUBWFB                   Subtract W from f with Borrow
Syntax                   SUBWFB f {,d {,a}}
Operands                 0 ≤ f ≤ 255
                         d ∈ [0, 1]
                         a ∈ [0, 1]
Operation                (f) – (W) – (C) → dest
Status Affected          N, OV, C, DC, Z
Encoding                           0101                         10da                        ffff                         ffff
Description              Subtract W and the Carry flag (Borrow) from register ‘f’ (two’s complement method). If ‘d’ is ‘0’, the
                         result is stored in W. If ‘d’ is ‘1’, the result is stored back in the register ‘f’ (default).
                         If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                         If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                         Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                         Indexed Literal Offset Mode for details.

Words                    1
Cycles                   1


Q Cycle Activity:
              Q1                                  Q2                               Q3                                  Q4
            Decode                      Read register ‘f’                    Process Data                    Write to destination

Example 1: SUBWFB REG, 1, 0

Before Instruction
REG = 19h (0001 1001)
W = 0Dh (0000 1101)
C=1

After Instruction
REG = 0Ch (0000 1100)
W = 0Dh (0000 1101)


--- p853 ---
C = 1 (result is positive)
Z=0
N=0

Example 2: SUBWFB REG, 0, 0

Before Instruction
REG = 1Bh (0001 1011)
W = 1Ah (0001 1010)
C=0

After Instruction
REG = 1Bh (0001 1011)
W = 00h
C=1
Z = 1 (result is zero)
N=0

Example 3: SUBWFB REG, 1, 0

Before Instruction
REG = 03h (0000 0011)
W = 0Eh (0000 1110)
C=1

After Instruction
REG = F5h (1111 0101) (two’s complement)
W = 0Eh (0000 1110)
C=0
Z=0
N = 1 (result is negative)


SWAPF                  Swap f
Syntax                 SWAPF f {,d {,a}}
Operands               0 ≤ f ≤ 255
                       d ∈ [0, 1]
                       a ∈ [0, 1]
Operation              (f<3:0>) → dest<7:4>
                       (f<7:4>) → dest<3:0>
Status Affected        None
Encoding                         0011                         10da                        ffff                         ffff
Description            The upper and lower nibbles of register ‘f’ are exchanged. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is
                       ‘1’, the result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                             Q2                                  Q3                                  Q4


--- p854 ---
            Decode                 Read register ‘f’                  Process Data          Write to destination

Example: SWAPF REG, 1, 0

Before Instruction
REG = 53h

After Instruction
REG = 35h


TBLRD                Table Read
Syntax               TBLRD *
                     TBLRD *+
                     TBLRD *-
                     TBLRD +*
Operands             None
Operation            If TBLRD *
                     (Prog Mem (TBLPTR)) → TABLAT
                     TBLPTR – No Change
                     If TBLRD *+
                     (Prog Mem (TBLPTR)) → TABLAT
                     (TBLPTR) + 1 → TBLPTR
                     If TBLRD *-
                     (Prog Mem (TBLPTR)) → TABLAT
                     (TBLPTR) – 1 → TBLPTR
                     If TBLRD +*
                     (TBLPTR) + 1 → TBLPTR
                     (Prog Mem (TBLPTR)) → TABLAT

Status Affected      None
Encoding                      0000                         0000                      0000             10mm
                                                                                                     mm=0 *
                                                                                                    mm=1 *+
                                                                                                    mm=2 *-
                                                                                                    mm=3 +*

Description          This instruction is used to read the contents of Program Memory. To address the program memory,
                     a pointer called Table Pointer (TBLPTR) is used.
                     The TBLPTR (a 21-bit pointer) points to each byte in the program memory. TBLPTR has a 2-Mbyte
                     address range.
                     TBLPTR[0] = 0: Least Significant Byte of Program Memory Word
                     TBLPTR[0] = 1: Most Significant Byte of Program Memory Word
                     The TBLRD instruction can modify the value of TBLPTR as follows:
                     •   no change (TBLRD *)
                     •   post-increment (TBLRD *+)
                     •   post-decrement (TBLRD *-)
                     •   pre-increment (TBLRD +*)

Words                1
Cycles               2


Q Cycle Activity:
              Q1                         Q2                               Q3                        Q4
            Decode                   No operation                     No operation             No operation


--- p855 ---
                                     No operation                                              No operation
         No operation                                                 No operation
                                (Read Program Memory)                                         (Write TABLAT)

Example 1: TBLRD *+

Before Instruction
TABLAT = 55h
TBLPTR = 00A356h
MEMORY (00A356h) = 34h

After Instruction
TABLAT = 34h
TBLPTR = 00A357h

Example 2: TBLRD +*

Before Instruction
TABLAT = AAh
TBLPTR = 01A357h
MEMORY (01A357h) = 12h
MEMORY (01A358h) = 34h

After Instruction
TABLAT = 34h
TBLPTR = 01A358h


TBLWT                   Table Write
Syntax                  TBLWT *
                        TBLWT *+
                        TBLWT *-
                        TBLWT +*
Operands                None
Operation               If TBLWT *
                        (TABLAT) → Holding Register
                        TBLPTR – No Change
                        If TBLWT *+
                        (TABLAT) → Holding Register
                        (TBLPTR) + 1 → TBLPTR
                        If TBLWT *-
                        (TABLAT) → Holding Register
                        (TBLPTR) – 1 → TBLPTR
                        If TBLWT +*
                        (TBLPTR) + 1 → TBLPTR
                        (TABLAT) → Holding Register

Status Affected         None
Encoding                         0000                      0000                       0000           11mm
                                                                                                   mm=0 *
                                                                                                   mm=1 *+
                                                                                                   mm=2 *-
                                                                                                   mm=3 +*


--- p856 ---
...........continued
TBLWT                   Table Write
Syntax                  TBLWT *
                        TBLWT *+
                        TBLWT *-
                        TBLWT +*
Description             This instruction uses the three LSBs of TBLPTR to determine which of the eight holding registers
                        the TABLAT is written to. The holding registers are used to program the contents of Program
                        Memory (refer to the “Program Flash Memory” section for additional details on programming
                        Flash memory).
                        The TBLPTR (a 21-bit pointer) points to each byte in the program memory. TBLPTR has a 2-Mbyte
                        address range. The LSb of the TBLPTR selects which byte of the program memory location to
                        access.
                        TBLPTR[0] = 0: Least Significant Byte of Program Memory Word
                        TBLPTR[0] = 1: Most Significant Byte of Program Memory Word
                        The TBLWT instruction can modify the value of TBLPTR as follows:
                        •   no change (TBLWT *)
                        •   post-increment (TBLWT *+)
                        •   post-decrement (TBLWT *-)
                        •   pre-increment (TBLWT +*)

Words                   1
Cycles                  2


Q Cycle Activity:
              Q1                             Q2                            Q3                              Q4
           Decode                       No operation                  No operation                   No operation
                                        No operation
                                                                                                 No operation (Write to
         No operation                  (Read TABLAT)                  No operation
                                                                                                   Holding Register)


Example 1: TBLWT *+

Before Instruction
TABLAT = 55h
TBLPTR = 00A356h
HOLDING REGISTER (00A356h) = FFh

After Instruction (table write completion)
TABLAT = 55h
TBLPTR = 00A357h
HOLDING REGISTER (00A356h) = 55h

Example 2: TBLWT +*

Before Instruction
TABLAT = 34h
TBLPTR = 01389Ah
HOLDING REGISTER (01389Ah) = FFh
HOLDING REGISTER (01389Bh) = FFh

After Instruction (table write completion)
TABLAT = 34h
TBLPTR = 01389Bh


--- p857 ---
HOLDING REGISTER (01389Ah) = FFh
HOLDING REGISTER (01389Bh) = 34h


TSTFSZ                    Test f, Skip if 0
Syntax                    TSTFSZ f {,a}
Operands                  0 ≤ f ≤ 255
                          a ∈ [0, 1]
Operation                 Skip if f = 0
Status Affected           None
Encoding                             0110                          011a                      ffff                         ffff
Description               If ‘f’ = 0, the next instruction fetched during the current instruction execution is discarded and a
                          NOP is executed, making this a two-cycle instruction.
                          If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                          If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                          Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                          Indexed Literal Offset Mode for details.

Words                     1
Cycles                    1 (2)
                          Note: Three cycles if skip and followed by a two-word instruction. Four cycles if skip and followed
                          by a three-word instruction.


Q Cycle Activity:

If no skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                       Read register ‘f’                  Process Data                        No operation

If skip:

               Q1                                 Q2                                Q3                                  Q4
              Decode                       Read register ‘f’                  Process Data                        No operation
           No operation                       No operation                    No operation                        No operation

If skip and followed by two-word instruction:

               Q1                                 Q2                                Q3                                  Q4
              Decode                       Read register ‘f’                  Process Data                        No operation
           No operation                       No operation                    No operation                        No operation
           No operation                       No operation                    No operation                        No operation

If skip and followed by three-word instruction:

               Q1                                 Q2                                Q3                                  Q4
              Decode                       Read register ‘f’                  Process Data                        No operation
           No operation                       No operation                    No operation                        No operation
           No operation                       No operation                    No operation                        No operation
           No operation                       No operation                    No operation                        No operation


--- p858 ---
Example:
 HERE   TSTFSZ       CNT, 1
 NZERO:
 ZERO:


Before Instruction
PC = address (HERE)

After Instruction
If CNT = 0; PC = address (ZERO)
If CNT ≠ 0; PC = address (NZERO)


XORLW                  Exclusive OR Literal with W
Syntax                 XORLW k
Operands               0 ≤ k ≤ 255
Operation              (W) .XOR. k → W
Status Affected        N, Z
Encoding                         0000                          1010                         kkkk                         kkkk
Description            The contents of W are XORed with the 8-bit literal ‘k’. The result is placed in W.
Words                  1
Cycles                 1


Q Cycle Activity:
              Q1                              Q2                                  Q3                                   Q4
            Decode                      Read literal ‘k’                     Process Data                          Write to W

Example: XORLW 0AFh

Before Instruction
W = B5h

After Instruction
W = 1Ah


XORWF                  Exclusive OR W with f
Syntax                 XORWF f {,d {,a}}
Operands               0 ≤ f ≤ 255
                       d ∈ [0, 1]
                       a ∈ [0, 1]
Operation              (W) .XOR. (f) → dest
Status Affected        N, Z
Encoding                         0001                          10da                         ffff                         ffff
Description            Exclusive OR the contents of W with register ‘f’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the
                       result is stored back in the register ‘f’ (default).
                       If ‘a’ is ‘0’, the Access Bank is selected. If ‘a’ is ‘1’, the BSR is used to select the GPR bank.
                       If ‘a’ is ‘0’ and the extended instruction set is enabled, this instruction operates in Indexed Literal
                       Offset Addressing mode whenever f ≤ 95 (5Fh). See Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.

Words                  1
Cycles                 1


--- p859 ---
       Q Cycle Activity:
                   Q1                           Q2                               Q3                 Q4
                 Decode                   Read register ‘f’                  Process Data   Write to destination

       Example: XORWF REG, 1, 0

       Before Instruction
       REG = AFh
       W = B5h

       After Instruction
       REG = 1Ah
       W = B5h


45.2   Extended Instruction Set
       In addition to the standard instruction set, PIC18 devices also provide an optional extension to the
       core CPU functionality. The added features include additional instructions that augment Indirect and
       Indexed Addressing operations and the implementation of Indexed Literal Offset Addressing mode
       for many of the standard PIC18 instructions.
       The additional features of the extended instruction set are disabled by default. To enable them,
       users must set the XINST Configuration bit.
       The instructions in the extended set can all be classified as literal operations, which either
       manipulate the File Select registers, or use them for Indexed Addressing. Two of the standard
       instructions, ADDFSR and SUBFSR, each have an additional special instantiation for using FSR2 as
       extended instructions. These versions (ADDULNK and SUBULNK) allow for automatic return after
       execution.
       The extended instructions are specifically implemented to optimize re-entrant program code (that is,
       code that is recursive or that uses a software stack) written in high-level languages, particularly C.
       Among other things, they allow users working in high-level languages to perform certain operations
       on data structures more efficiently. These include:
       •   Dynamic allocation and deallocation of software stack space when entering and leaving
           subroutines
       •   Function pointer invocation
       •   Software Stack Pointer manipulation
       •   Manipulation of variables located in a software stack
       A summary of the instructions in the extended instruction set is provided in Extended Instruction
       Syntax. Detailed descriptions are provided in Extended Instruction Set. The opcode field descriptions
       in Table 45-1 apply to both the standard and extended PIC18 instruction sets.


--- p860 ---
                   Important:
                   • The instruction set extension and the Indexed Literal Offset Addressing mode were
                     designed for optimizing applications written in C; the user may likely never use these
                     instructions directly in assembler. The syntax for these commands is provided as a
                     reference for users who may be reviewing code that has been generated by a compiler.
                   •   Enabling the PIC18 instruction set extension may cause legacy applications to behave
                       erratically or fail entirely. Refer to Byte-Oriented and Bit-Oriented Instructions in
                       Indexed Literal Offset Mode for details.


45.2.1 Extended Instruction Syntax
       Most of the extended instructions use indexed arguments, using one of the File Select registers and
       some offset to specify a source or destination register. When an argument for an instruction serves
       as part of Indexed Addressing, it is enclosed in square brackets (“[ ]”). This is done to indicate that
       the argument is used as an index or offset. MPASM™ Assembler will flag an error if it determines that
       an index or offset value is not bracketed.
       When the extended instruction set is enabled, brackets are also used to indicate index arguments in
       byte-oriented and bit-oriented instructions. This is in addition to other changes in their syntax. For
       more details, see Extended Instruction Syntax with Standard PIC18 Commands.


--- p861 ---
                                                                              Table 45-3. Extensions to the PIC18 Instruction Set
                                                                                                          Mnemonic,                                                                        16-Bit Instruction Word
                                                                                                                                                                                                                                        Status
                                                                                                          Operands                                 Description             Cycles                                                                      Notes
                                                                                                                                                                                    MSb                                  LSb           Affected
                                                                                                              rotatethispage90


                                                                                   ADDULNK                                         k      Add literal to FSR2 and return     2      1110    1000           11kk         kkkk                None            1, 3
                                                                                                                                              Move zs (12-bit source)               1110    1011          0zszszs     zszszszs
                                                                                    MOVSF                                        zs, fd                                      2                                                              None           2, 3, 4
                                                                                                                                             to fd (12-bit destination)             1111   fdfdfdfd       fdfdfdfd    fdfdfdfd
                                                                                                                                                                                    0000    0000           0000         0010
                                                                                                                                              Move zs (14-bit source)
                                                                                   MOVSFL                                        zs, fd                                      3      1111    xxxzs         zszszszs    zszsfdfd              None            2, 3
                                                                                                                                             to fd (14-bit destination)
                                                                                                                                                                                    1111   fdfdfdfd       fdfdfdfd    fdfdfdfd
                                                                                                                                                 Move zs (source)                   1110    1011          1zszszs     zszszszs
                                                                                    MOVSS                                        zs, zd                                      2                                                              None            2, 3
                                                                                                                                                to zd (destination)                 1111    xxxx          xzdzdzd     zdzdzdzd
                                                                                                                                               Store literal at FSR2,
                                                                                    PUSHL                                          k                                         1      1110    1010           kkkk         kkkk                None             3
                                                                                                                                                 decrement FSR2
                                                                                                                                          Subtract literal from FSR2 and
                                                                                   SUBULNK                                         k                                         2      1110    1001           11kk         kkkk                None            1, 3
                                                                                                                                                       return


                                                                              Notes:   rotatethispage90


                                                                              1.   If Program Counter (PC) is modified or a conditional test is true, the instruction requires an additional cycle. The extra cycle is executed as a NOP.
                                                                              2.   Some instructions are multi-word instructions. The extra words of these instructions will be decoded as a NOP, unless the first word of the instruction retrieves the
                                                                                   information embedded in these 16 bits. This ensures that all program memory locations have a valid instruction.
subsidiaries


                                                                              3.   Only available when extended instruction set is enabled.
                                                          Data Sheet


                                                                              4.   fs and fd do not cover the full memory range. 2 MSbs of bank selection are forced to 0b00 to limit the range of these instructions to lower 4k addressing space.


                                                                                                                                                                                                                                                                     Instruction Set Summary

45.2.2 Extended Instruction Set

                      Important: All PIC18 instructions may take an optional label argument preceding the
                      instruction mnemonic for use in symbolic addressing. If a label is used, the instruction
                      format then becomes:
                      {label} instruction argument(s)


        ADDULNK                 Add Literal to FSR2 and Return
        Syntax                  ADDULNK k
        Operands                0 ≤ k ≤ 63
        Operation               (FSR2) + k → FSR2
                                (TOS) → PC
        Status Affected         None
        Encoding                          1110                          1000                      11kk                  kkkk
        Description             The 6-bit literal ‘k’ is added to the contents of FSR2. A RETURN is then executed by loading the PC
                                with the TOS. The instruction takes two cycles to execute; a NOP is performed during the second
                                cycle. This may be thought of as a special case of the ADDFSR instruction, where fn = 3 (binary ‘11’);
                                it operates only on FSR2.

        Words                   1
        Cycles                  2


        Q Cycle Activity:
                      Q1                               Q2                              Q3                             Q4
                    Decode                       Read literal ‘k’                  Process Data              Write to destination
                 No operation                    No operation                      No operation                 No operation

        Example: ADDULNK 23h

        Before Instruction
        FSR2 = 03FFh
        PC = 0100h

        After Instruction
        FSR2 = 0422h
        PC = (TOS)


        MOVSF                   Move Indexed to f
        Syntax                  MOVSF [zs], fd
        Operands                0 ≤ zs ≤ 127
                                0 ≤ fd ≤ 4095
        Operation               ((FSR2) + zs) → fd
        Status Affected         None
        Encoding                          1110                          1011                 0zszszs                  zszszszs
                                          1111                        fdfdfdfd               fdfdfdfd                 fdfdfdfd


--- p863 ---
...........continued
MOVSF                  Move Indexed to f
Syntax                 MOVSF [zs], fd
Description            The contents of the source register are moved to destination register ‘fd’. The actual address of the
                       source register is determined by adding the 7-bit literal offset ‘zs’ in the first word to the value of
                       FSR2. The address of the destination register is specified by the 12-bit literal ‘fd’ in the second word.
                       Both addresses can be anywhere in the 4096-byte data space (000h to FFFh).
                       Note:
                       MOVSF has curtailed the destination range to the lower 4 Kbyte space in memory (Banks 1 through
                       15). For everything else, use MOVSFL.

Words                  2
Cycles                 2


Q Cycle Activity:
              Q1                            Q2                                Q3                                Q4
            Decode              Determine source address         Determine source address              Read source register
                                      No operation
            Decode                                                       No operation                    Write register ‘fd’
                                     No dummy read

Example: MOVSF [05h], REG2

Before Instruction
FSR2 = 80h
Contents of 85h = 33h
REG2 = 11h
Address of REG2 = 100h

After Instruction
FSR2 = 80h
Contents of 85h = 33h
REG2 = 33h
Address of REG2 = 100h


MOVSFL                 Move Indexed to f (Long Range)
Syntax                 MOVSFL [zs], fd
Operands               0 ≤ zs ≤ 127
                       0 ≤ fd ≤ 16383
Operation              ((FSR2) + zs) → fd
Status Affected        None
Encoding                         0000                       0000                        0110                       0010
                                 1111                      xxxzs                     zszszszs                   zszsfdfd
                                 1111                     fdfdfdfd                   fdfdfdfd                   fdfdfdfd
Description            The contents of the source register are moved to destination register ‘fd’. The actual address of
                       the source register is determined by adding the 7-bit literal offset ‘zs’ in the first word to the value
                       of FSR2 (14 bits). The address of the destination register is specified by the 14-bit literal ‘fd’ in the
                       second word. Both addresses can be anywhere in the 16 Kbyte data space (0000h to 3FFFh). The
                       MOVSFL instruction cannot use the PCL, TOSU, TOSH or TOSL as the destination register. If the
                       resultant source address points to an indirect addressing register, the value returned will be 00h.

Words                  3
Cycles                 3


--- p864 ---
Q Cycle Activity:
              Q1                           Q2                              Q3                                Q4
            Decode                    No operation                    No operation                     No operation
            Decode               Read source register                 Process Data                     No operation
                                     No operation
            Decode                                                    No operation                   Write register ‘fd’
                                    No dummy read

Example: MOVSFL [05h], REG2

Before Instruction
FSR2 = 2080h
Contents of 2085h = 33h
REG2 = 11h
Address of REG2 = 2000h

After Instruction
FSR2 = 2080h
Contents of 2085h = 33h
REG2 = 33h
Address of REG2 = 2000h


MOVSS                Move Indexed to Indexed
Syntax               MOVSS [zs], [zd]
Operands             0 ≤ zs ≤ 127
                     0 ≤ zd ≤ 127
Operation            ((FSR2) + zs) → ((FSR2) + zd)
Status Affected      None
Encoding                       1110                      1011                     1zszszs                    zszszszs
                               1111                      xxxx                     xzdzdzd                    zdzdzdzd
Description          The contents of the source register are moved to the destination register. The addresses of
                     the source and destination registers are determined by adding the 7-bit literal offsets ‘zs’ or ‘zd’
                     respectively to the value of FSR2. Both registers can be located anywhere in the 16 Kbyte data
                     memory space (0000h to 3FFFh).
                     The MOVSS instruction cannot use the PCL, TOSU, TOSH or TOSL as the destination register.
                     If the resultant source address points to an indirect addressing register, the value returned will be
                     00h. If the resultant destination address points to an indirect addressing register, the instruction
                     will execute as a NOP.

Words                2
Cycles               2


Q Cycle Activity:
              Q1                           Q2                              Q3                                Q4
            Decode           Determine source address          Determine source address            Read source register
                                Determine destination             Determine destination
            Decode                                                                             Write to destination register
                                      address                           address

Example: MOVSS [05h], [06h]

Before Instruction
FSR2 = 80h


--- p865 ---
Contents of 85h = 33h
Contents of 86h = 11h

After Instruction
FSR2 = 80h
Contents of 85h = 33h
Contents of 86h = 33h


PUSHL                Store Literal at FSR2, Decrement FSR2
Syntax               PUSHL k
Operands             0 ≤ k ≤ 255
Operation            k → FSR2
                     (FSR2) – 1 → FSR2
Status Affected      None
Encoding                       1111                          1010                      kkkk                 kkkk
Description          The 8-bit literal ‘k’ is written to the data memory address specified by FSR2. FSR2 is decremented by
                     1 after the operation. This instruction allows users to push values onto a software stack.

Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                              Q3                            Q4
            Decode                    Read literal ‘k’                  Process Data             Write to destination

Example: PUSHL 08h

Before Instruction
FSR2 = 01ECh
Contents of 01ECh = 00h

After Instruction
FSR2 = 01EBh
Contents of 01ECh = 08h


SUBULNK              Subtract Literal from FSR2 and Return
Syntax               SUBULNK k
Operands             0 ≤ k ≤ 63
Operation            (FSR2) – k → FSR2
                     (TOS) → PC
Status Affected      None
Encoding                       1110                          1001                      11kk                 kkkk
Description          The 6-bit literal ‘k’ is subtracted from the contents of FSR2. A RETURN is then executed by loading
                     the PC with the TOS. The instruction takes two cycles to execute; a NOP is performed during the
                     second cycle. This may be thought of as a special case of the SUBFSR instruction, where fn = 3
                     (binary ‘11’); it operates only on FSR2.

Words                1
Cycles               2


Q Cycle Activity:


--- p866 ---
                    Q1                         Q2                              Q3                  Q4
                  Decode                 Read literal ‘k’                  Process Data    Write to destination
               No operation              No operation                      No operation       No operation

        Example: SUBULNK 23h

        Before Instruction
        FSR2 = 03FFh
        PC = 0100h

        After Instruction
        FSR2 = 03DCh
        PC = (TOS)


45.2.3 Byte-Oriented and Bit-Oriented Instructions in Indexed Literal Offset Mode

                    Important: Enabling the PIC18 instruction set extension may cause legacy applications to
                    behave erratically or fail entirely.


        In addition to the new commands in the extended set, enabling the extended instruction set also
        enables Indexed Literal Offset Addressing mode (see the “Indexed Addressing with Literal Offset”
        section in the “Memory Organization” chapter). This has a significant impact on the way many
        commands of the standard PIC18 instruction set are interpreted.
        When the extended set is disabled, addresses embedded in opcodes are treated as literal memory
        locations, either as a location in the Access Bank (‘a’ = 0) or in a GPR bank designated by the BSR (‘a’
        = 1). When the extended instruction set is enabled and ‘a’ = 0, however, a file register argument of
        5Fh or less is interpreted as an offset from the pointer value in FSR2 and not as a literal address. For
        practical purposes, this means that all instructions using the Access RAM bit as an argument – that
        is, all byte-oriented and bit-oriented instructions, or almost half of the core PIC18 instructions – may
        behave differently when the extended instruction set is enabled.
        When the content of FSR2 is 00h, the boundaries of the Access RAM are essentially remapped to
        their original values. This may be useful in creating backward compatible code. If this technique is
        used, it may be necessary to save the value of FSR2 and restore it when moving back and forth
        between C and assembly routines to preserve the Stack Pointer. Users must also keep in mind the
        syntax requirements of the extended instruction set (see Extended Instruction Syntax with Standard
        PIC18 Commands).
        Although the Indexed Literal Offset Addressing mode can be very useful for dynamic stack and
        pointer manipulation, it can also be very annoying if a simple arithmetic operation is carried out on
        the wrong register. Users who are accustomed to the PIC18 programming must keep in mind that,
        when the extended instruction set is enabled, register addresses of 5Fh or less are used for Indexed
        Literal Offset Addressing.
        Representative examples of typical byte-oriented and bit-oriented instructions in the Indexed Literal
        Offset Addressing mode are provided in the Considerations when Enabling the Extended Instruction
        Set section to show how execution is affected. The operand conditions shown in the examples are
        applicable to all instructions of these types.
        Related Links
        9.6. Data Memory and the Extended Instruction Set


--- p867 ---
45.2.3.1 Extended Instruction Syntax with Standard PIC18 Commands
        When the extended instruction set is enabled, the file register argument, ‘f’, in the standard byte-
        oriented and bit-oriented commands is replaced with the literal offset value, ‘k’. As already noted,
        this occurs only when ‘f’ is less than or equal to 5Fh. When an offset value is used, it must be
        indicated by square brackets (“[ ]”). As with the extended instructions, the use of brackets indicates
        to the compiler that the value is to be interpreted as an index or an offset. Omitting the brackets, or
        using a value greater than 5Fh within brackets, will generate an error in the MPASM Assembler.
        If the index argument is properly bracketed for Indexed Literal Offset Addressing, the Access RAM
        argument is never specified; it will automatically be assumed to be ‘0’. This is in contrast to standard
        operation (extended instruction set disabled) when ‘a’ is set on the basis of the target address.
        Declaring the Access RAM bit in this mode will also generate an error in the MPASM Assembler.
        The destination argument, ‘d’, functions as before.
        In the latest versions of the MPASM Assembler, language support for the extended instruction set
        must be explicitly invoked. This is done with either the command-line option, /y, or the PE directive
        in the source listing.
        Related Links
        9.6. Data Memory and the Extended Instruction Set

45.2.4 Considerations when Enabling the Extended Instruction Set
        It is important to note that the extensions to the instruction set may not be beneficial to all users. In
        particular, users who are not writing code that uses a software stack may not benefit from using the
        extensions to the instruction set.
        Additionally, the Indexed Literal Offset Addressing mode may create issues with legacy applications
        written to the PIC18 assembler. This is because instructions in the legacy code may attempt to
        address registers in the Access Bank below 5Fh. Since these addresses are interpreted as literal
        offsets to FSR2 when the instruction set extension is enabled, the application may read or write to
        the wrong data addresses.
        When porting an application to a PIC18 device supporting extensions to the instruction set, it is
        very important to consider the type of code. A large, re-entrant application that is written in ‘C’ and
        benefits from efficient compilation will do well when using the instruction set extensions. Legacy
        applications that heavily use the Access Bank will most likely not benefit from using the extended
        instruction set.
        ADDWF                Add W to Indexed (Indexed Literal Offset Mode)
        Syntax               ADDWF [k] {,d}
        Operands             0 ≤ k ≤ 95
                             d ∈ [0, 1]
        Operation            (W) + ((FSR2) + k) → dest
        Status Affected      N, OV, C, DC, Z
        Encoding                        0010                           01d0                          kkkk                           kkkk
        Description          The contents of W are added to the contents of the register indicated by FSR2, offset by the value
                             ‘k’. If ‘d’ is ‘0’, the result is stored in W. If ‘d’ is ‘1’, the result is stored back in the register ‘f’ (default).
        Words                1
        Cycles               1


        Q Cycle Activity:
                      Q1                             Q2                                    Q3                                    Q4
                    Decode                     Read literal ‘k’                      Process Data                      Write to destination

        Example: ADDWF [OFST] , 0


--- p868 ---
Before Instruction
W = 17h
OFST = 2Ch
FSR2 = 0A00h
Contents of 0A2Ch = 20h

After Instruction
W = 37h
Contents of 0A2Ch = 20h


BSF                  Bit Set Indexed (Indexed Literal Offset Mode)
Syntax               BSF [k], b
Operands             0 ≤ k ≤ 95
                     0≤b≤7
Operation            1 → ((FSR2) + k)<b>
Status Affected      None
Encoding                       1000                          bbb0                      kkkk                     kkkk
Description          Bit ‘b’ of the register indicated by FSR2, offset by the value ‘k’, is set
Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                Q3                               Q4
            Decode                    Read literal ‘k’                  Process Data               Write to destination

Example: BSF [FLAG_OFST], 7

Before Instruction
FLAG_OFST = 0Ah
FSR2 = 0A00h
Contents of 0A0Ah = 55h

After Instruction
Contents of 0A0Ah = D5h


SETF                 Set Indexed (Indexed Literal Offset Mode)
Syntax               SETF [k]
Operands             0 ≤ k ≤ 95
Operation            FFh → ((FSR2) + k)
Status Affected      None
Encoding                       0110                          1000                      kkkk                     kkkk
Description          The contents of the register indicated by FSR2, offset by the value ‘k’, are set to FFh
Words                1
Cycles               1


Q Cycle Activity:
              Q1                            Q2                                Q3                               Q4
            Decode                    Read literal ‘k’                  Process Data               Write to destination


--- p869 ---
       Example: SETF [OFST]

       Before Instruction
       OFST = 2Ch
       FSR2 = 0A00h
       Contents of 0A2Ch = 00h

       After Instruction
       Contents of 0A2Ch = FFh


                                                             ®
45.2.5 Special Considerations with Microchip MPLAB IDE Tools
       The latest versions of Microchip’s software tools have been designed to fully support the extended
       instruction set on the PIC18 devices. This includes the MPLAB XC8 C compiler, MPASM Assembler
       and MPLAB X Integrated Development Environment (IDE).
       When selecting a target device for software development, MPLAB X IDE will automatically set default
       Configuration bits for that device. The default setting for the XINST Configuration bit is ‘0’, disabling
       the extended instruction set and Indexed Literal Offset Addressing mode. For proper execution of
       applications developed to take advantage of the extended instruction set, XINST must be set during
       programming.
       To develop software for the extended instruction set, the user must enable support for the
       instructions and the Indexed Addressing mode in their language tool(s). Depending on the
       environment being used, this may be done in several ways:
       •   A menu option, or dialog box within the environment, that allows the user to configure the
           language tool and its settings for the project
       •   A command-line option
       •   A directive in the source code
       These options vary between different compilers, assemblers and development environments. Users
       are encouraged to review the documentation accompanying their development systems for the
       appropriate information.


--- p870 ---
